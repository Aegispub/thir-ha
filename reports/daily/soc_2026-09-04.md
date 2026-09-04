# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-09-04 |
| **Generated At** | 2026-09-04T18:55:11Z |
| **Shift Time** | 18:55 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **318** |
| Confirmed Threats | **291** |
| False Positives Filtered | **27** (8.5%) |
| Unique Attacker IPs | **64** |
| Countries of Origin | **27** |
| High Severity Cases | **254** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **64** |
| Malware Samples Analyzed | **4** HIGH · **20** MED · 19 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **271** |
| Unique Credential Pairs | **218** |
| Unique Usernames | **62** |
| Unique Passwords | **177** |
| Successful Auth Pairs | **255** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 138 |
| `345gs5662d34` | 13 |
| `ubuntu` | 10 |
| `support` | 10 |
| `user` | 8 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 13 |
| `3245gs5662d34` | 13 |
| `support` | 10 |
| `admin` | 7 |
| `123456` | 7 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 13 |
| `support` | `support` | 10 |
| `root` | `3245gs5662d34` | 5 |
| `admin` | `admin` | 4 |
| `root` | `admin` | 3 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `123456789` | `80.94.92.179` | 2026-09-04T12:55:14 |
| `ubuntu` | `qwer1234` | `45.148.10.240` | 2026-09-04T12:55:14 |
| `ubuntu` | `1234qwer` | `45.148.10.240` | 2026-09-04T12:56:58 |
| `root` | `1234abcd` | `80.94.92.179` | 2026-09-04T12:57:41 |
| `root` | `asd123!` | `217.60.255.130` | 2026-09-04T12:58:29 |
| `ubuntu` | `1q2w3e4r` | `45.148.10.240` | 2026-09-04T12:58:40 |
| `root` | `123abc` | `80.94.92.179` | 2026-09-04T13:00:13 |
| `ubuntu` | `p@ssw0rd` | `45.148.10.240` | 2026-09-04T13:00:21 |
| `ubuntu` | `!@#$%^` | `45.148.10.240` | 2026-09-04T13:02:05 |
| `root` | `123qwe` | `80.94.92.179` | 2026-09-04T13:02:24 |
| `root` | `blockchain1!` | `45.148.10.240` | 2026-09-04T13:03:49 |
| `root` | `1q2w3e` | `80.94.92.179` | 2026-09-04T13:04:38 |
| `support` | `support` | `176.53.159.196` | 2026-09-04T13:04:39 |
| `sol-docker` | `sol-docker` | `45.148.10.240` | 2026-09-04T13:05:30 |
| `root` | `1q2w3e4r` | `80.94.92.179` | 2026-09-04T13:06:53 |
| `soldocker` | `soldocker` | `45.148.10.240` | 2026-09-04T13:07:07 |
| `solana` | `postgres` | `45.148.10.240` | 2026-09-04T13:08:48 |
| `root` | `1qaz2wsx` | `80.94.92.179` | 2026-09-04T13:09:10 |
| `root` | `rememberme` | `217.60.255.130` | 2026-09-04T13:09:42 |
| `postgres` | `solana` | `45.148.10.240` | 2026-09-04T13:10:32 |
| `root` | `321` | `80.94.92.179` | 2026-09-04T13:11:31 |
| `root` | `solana1!` | `45.148.10.240` | 2026-09-04T13:12:14 |
| `root` | `654321` | `80.94.92.179` | 2026-09-04T13:13:49 |
| `root` | `Solana1!` | `45.148.10.240` | 2026-09-04T13:13:55 |
| `root` | `Solana!` | `45.148.10.240` | 2026-09-04T13:15:42 |
| `root` | `P@ssw0rd` | `80.94.92.179` | 2026-09-04T13:16:08 |
| `root` | `solana1` | `45.148.10.240` | 2026-09-04T13:17:28 |
| `root` | `---fuck_you----` | `10.0.0.73` | 2026-09-04T13:18:21 |
| `root` | `P@ssword` | `80.94.92.179` | 2026-09-04T13:18:23 |
| `solana` | `solana1!` | `45.148.10.240` | 2026-09-04T13:19:08 |
| `root` | `Root123` | `80.94.92.179` | 2026-09-04T13:20:40 |
| `root` | `Password1234!` | `217.60.255.130` | 2026-09-04T13:20:45 |
| `solana` | `Solana1!` | `45.148.10.240` | 2026-09-04T13:20:48 |
| `defi` | `defi` | `45.148.10.240` | 2026-09-04T13:22:33 |
| `root` | `admin` | `80.94.92.179` | 2026-09-04T13:22:57 |
| `support` | `support` | `10.0.0.73` | 2026-09-04T13:23:59 |
| `user1` | `123456` | `45.148.10.240` | 2026-09-04T13:24:14 |
| `trash` | `trash` | `76.79.213.70` | 2026-09-04T13:24:52 |
| `345gs5662d34` | `345gs5662d34` | `76.79.213.70` | 2026-09-04T13:24:55 |
| `trash` | `3245gs5662d34` | `76.79.213.70` | 2026-09-04T13:24:56 |
| `root` | `admin123` | `80.94.92.179` | 2026-09-04T13:25:11 |
| `user1` | `12345678` | `45.148.10.240` | 2026-09-04T13:25:53 |
| `root` | `Wu@123456` | `163.7.9.84` | 2026-09-04T13:26:56 |
| `345gs5662d34` | `345gs5662d34` | `163.7.9.84` | 2026-09-04T13:27:00 |
| `root` | `3245gs5662d34` | `163.7.9.84` | 2026-09-04T13:27:02 |
| `root` | `letmein` | `80.94.92.179` | 2026-09-04T13:27:24 |
| `john` | `a` | `85.69.240.210` | 2026-09-04T13:27:34 |
| `user2` | `123456` | `45.148.10.240` | 2026-09-04T13:27:37 |
| `345gs5662d34` | `345gs5662d34` | `85.69.240.210` | 2026-09-04T13:27:37 |
| `john` | `3245gs5662d34` | `85.69.240.210` | 2026-09-04T13:27:38 |
| `user` | `root@1234` | `51.75.253.68` | 2026-09-04T13:28:49 |
| `345gs5662d34` | `345gs5662d34` | `51.75.253.68` | 2026-09-04T13:28:51 |
| `user` | `3245gs5662d34` | `51.75.253.68` | 2026-09-04T13:28:52 |
| `user2` | `12345678` | `45.148.10.240` | 2026-09-04T13:29:23 |
| `root` | `pass` | `80.94.92.179` | 2026-09-04T13:29:35 |
| `odoo17` | `123456789` | `161.248.202.88` | 2026-09-04T13:29:48 |
| `345gs5662d34` | `345gs5662d34` | `161.248.202.88` | 2026-09-04T13:29:52 |
| `odoo17` | `3245gs5662d34` | `161.248.202.88` | 2026-09-04T13:29:53 |
| `geth` | `geth` | `45.148.10.240` | 2026-09-04T13:31:07 |
| `root` | `passw0rd` | `80.94.92.179` | 2026-09-04T13:31:42 |
| `root` | `Admin123456` | `217.60.255.130` | 2026-09-04T13:31:53 |
| `ethereum` | `ethereum` | `45.148.10.240` | 2026-09-04T13:32:48 |
| `root` | `password` | `80.94.92.179` | 2026-09-04T13:33:49 |
| `eth` | `eth` | `45.148.10.240` | 2026-09-04T13:34:33 |
| `root` | `password1` | `80.94.92.179` | 2026-09-04T13:36:15 |
| `eth-docker` | `eth-docker` | `45.148.10.240` | 2026-09-04T13:36:19 |
| `eth` | `docker` | `45.148.10.240` | 2026-09-04T13:38:00 |
| `root` | `qwerty` | `80.94.92.179` | 2026-09-04T13:38:28 |
| `eth` | `test` | `45.148.10.240` | 2026-09-04T13:39:41 |
| `admin` | `admin` | `117.50.194.182` | 2026-09-04T13:40:11 |
| `root` | `r00t` | `80.94.92.179` | 2026-09-04T13:40:20 |
| `sol` | `test` | `45.148.10.240` | 2026-09-04T13:41:29 |
| `admin` | `admin` | `47.236.238.212` | 2026-09-04T13:42:41 |
| `admin` | `admin` | `130.12.180.51` | 2026-09-04T13:42:41 |
| `root` | `Admin789` | `217.60.255.130` | 2026-09-04T13:43:02 |
| `claude` | `claude` | `45.148.10.240` | 2026-09-04T13:43:14 |
| `root` | `root!@#` | `80.94.92.179` | 2026-09-04T13:44:08 |
| `validator` | `validator` | `45.148.10.240` | 2026-09-04T13:44:55 |
| `root` | `root#123` | `80.94.92.179` | 2026-09-04T13:45:59 |
| `node` | `node` | `45.148.10.240` | 2026-09-04T13:46:38 |
| `root` | `root0000` | `80.94.92.179` | 2026-09-04T13:47:53 |
| `operator` | `operator` | `45.148.10.240` | 2026-09-04T13:48:24 |
| `root` | `123@@@` | `64.110.90.250` | 2026-09-04T13:49:27 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-09-04T13:49:27 |
| `root` | `root1111` | `80.94.92.179` | 2026-09-04T13:49:44 |
| `trader` | `trader` | `45.148.10.240` | 2026-09-04T13:50:07 |
| `root` | `root123` | `80.94.92.179` | 2026-09-04T13:51:35 |
| `trading` | `trading` | `45.148.10.240` | 2026-09-04T13:51:48 |
| `root` | `root1234` | `80.94.92.179` | 2026-09-04T13:53:28 |
| `trader` | `trader123` | `45.148.10.240` | 2026-09-04T13:53:34 |
| `root` | `Ustech3` | `217.60.255.130` | 2026-09-04T13:54:24 |
| `root` | `root2024` | `80.94.92.179` | 2026-09-04T13:55:18 |
| `trader` | `123456` | `45.148.10.240` | 2026-09-04T13:55:22 |
| `trader` | `12345678` | `45.148.10.240` | 2026-09-04T13:57:05 |
| `root` | `root2222` | `80.94.92.179` | 2026-09-04T13:57:14 |
| `trading` | `trading@123` | `45.148.10.240` | 2026-09-04T13:58:48 |
| `root` | `root321` | `80.94.92.179` | 2026-09-04T13:59:08 |
| `root` | `root@123` | `45.148.10.240` | 2026-09-04T14:00:35 |
| `root` | `root4444` | `80.94.92.179` | 2026-09-04T14:00:54 |
| `shardeum` | `shardeum` | `45.148.10.240` | 2026-09-04T14:02:21 |
| `root` | `root5555` | `80.94.92.179` | 2026-09-04T14:02:42 |
| `root` | `admin@123` | `45.148.10.240` | 2026-09-04T14:04:03 |
| `root` | `root5678` | `80.94.92.179` | 2026-09-04T14:04:29 |
| `root` | `solana` | `45.148.10.240` | 2026-09-04T14:05:48 |
| `root` | `Software2010` | `217.60.255.130` | 2026-09-04T14:05:59 |
| `root` | `root6666` | `80.94.92.179` | 2026-09-04T14:06:16 |
| `root` | `validator` | `45.148.10.240` | 2026-09-04T14:07:37 |
| `root` | `root9999` | `80.94.92.179` | 2026-09-04T14:07:58 |
| `firedancer` | `firedancer` | `45.148.10.240` | 2026-09-04T14:09:23 |
| `root` | `root@123` | `80.94.92.179` | 2026-09-04T14:09:44 |
| `blockchain` | `blockchain` | `45.148.10.240` | 2026-09-04T14:11:07 |
| `root` | `rootaccess` | `80.94.92.179` | 2026-09-04T14:11:31 |
| `www-data` | `www-data` | `45.148.10.240` | 2026-09-04T14:12:55 |
| `root` | `rootadmin` | `80.94.92.179` | 2026-09-04T14:13:15 |
| `user` | `1qq2w3e4r5t` | `45.148.10.240` | 2026-09-04T14:14:42 |
| `root` | `Abc.12345` | `10.0.0.73` | 2026-09-04T14:14:52 |
| `345gs5662d34` | `345gs5662d34` | `10.0.0.73` | 2026-09-04T14:14:55 |
| `root` | `3245gs5662d34` | `10.0.0.73` | 2026-09-04T14:14:55 |
| `root` | `rootme` | `80.94.92.179` | 2026-09-04T14:14:59 |
| `user` | `11q2w3e4r5t` | `45.148.10.240` | 2026-09-04T14:16:24 |
| `root` | `rootpass` | `80.94.92.179` | 2026-09-04T14:16:49 |
| `root` | `zxc123...` | `217.60.255.130` | 2026-09-04T14:17:21 |
| `profe` | `profe` | `10.0.0.73` | 2026-09-04T14:18:07 |
| `root` | `1qq2w3e4r5t` | `45.148.10.240` | 2026-09-04T14:18:09 |
| `profe` | `3245gs5662d34` | `10.0.0.73` | 2026-09-04T14:18:11 |
| `root` | `rootpw` | `80.94.92.179` | 2026-09-04T14:18:35 |
| `elround` | `elround` | `45.148.10.240` | 2026-09-04T14:19:56 |
| `root` | `Welcome@2025` | `10.0.0.73` | 2026-09-04T14:20:50 |
| `elrond` | `elrond` | `45.148.10.240` | 2026-09-04T14:21:42 |
| `support` | `support` | `138.226.239.233` | 2026-09-04T14:22:07 |
| `support` | `support` | `80.94.95.116` | 2026-09-04T14:22:53 |
| `admin` | `admin1` | `45.148.10.240` | 2026-09-04T14:23:27 |
| `ftpuser1` | `123456` | `212.64.201.210` | 2026-09-04T14:23:32 |
| `345gs5662d34` | `345gs5662d34` | `212.64.201.210` | 2026-09-04T14:23:35 |
| `ftpuser1` | `3245gs5662d34` | `212.64.201.210` | 2026-09-04T14:23:36 |
| `root` | `root1` | `45.148.10.240` | 2026-09-04T14:25:16 |
| `user` | `user1` | `45.148.10.240` | 2026-09-04T14:27:07 |
| `root` | `Aliyun@123` | `103.76.120.90` | 2026-09-04T14:27:28 |
| `345gs5662d34` | `345gs5662d34` | `103.76.120.90` | 2026-09-04T14:27:34 |
| `root` | `3245gs5662d34` | `103.76.120.90` | 2026-09-04T14:27:36 |
| `user` | `1` | `45.148.10.240` | 2026-09-04T14:28:52 |
| `root` | `Fuckyou` | `217.60.255.130` | 2026-09-04T14:29:18 |
| `miner` | `mmpOS` | `45.148.10.240` | 2026-09-04T14:30:37 |
| `root` | `admin` | `45.148.10.240` | 2026-09-04T14:32:27 |
| `git` | `git` | `45.148.10.240` | 2026-09-04T14:34:14 |
| `admin` | `blockchain1!` | `45.148.10.240` | 2026-09-04T14:37:48 |
| `ubuntu` | `blockchain1!` | `45.148.10.240` | 2026-09-04T14:39:40 |
| `root` | `Asiatech@1403` | `217.60.255.130` | 2026-09-04T14:41:14 |
| `ari` | `ari` | `45.148.10.240` | 2026-09-04T14:41:30 |
| `sedu` | `sedu` | `45.148.10.240` | 2026-09-04T14:43:17 |
| `solana123` | `solana123` | `45.148.10.240` | 2026-09-04T14:45:08 |
| `sol123` | `sol123` | `45.148.10.240` | 2026-09-04T14:46:54 |
| `sol` | `sol123` | `45.148.10.240` | 2026-09-04T14:48:38 |
| `sol` | `1234` | `45.148.10.240` | 2026-09-04T14:50:25 |
| `root` | `LSiuY7pOmZG2s` | `92.52.184.245` | 2026-09-04T14:51:52 |
| `binance` | `binance` | `45.148.10.240` | 2026-09-04T14:52:18 |
| `root` | `Server@1404` | `217.60.255.130` | 2026-09-04T14:52:33 |
| `okx` | `okx` | `45.148.10.240` | 2026-09-04T14:54:07 |
| `bot` | `bot` | `45.148.10.240` | 2026-09-04T14:55:57 |
| `telegram` | `telegram` | `45.148.10.240` | 2026-09-04T14:57:48 |
| `jito` | `jito` | `45.148.10.240` | 2026-09-04T14:59:38 |
| `firedancer` | `firedancer1!` | `45.148.10.240` | 2026-09-04T15:01:23 |
| `root` | `firedancer` | `45.148.10.240` | 2026-09-04T15:03:11 |
| `root` | `asdf123$` | `217.60.255.130` | 2026-09-04T15:03:37 |
| `bitcoin` | `bitcoin` | `45.148.10.240` | 2026-09-04T15:05:01 |
| `pool` | `pool` | `45.148.10.240` | 2026-09-04T15:06:51 |
| `admin` | `admin` | `2.29.16.86` | 2026-09-04T15:07:23 |
| `miner` | `miner` | `45.148.10.240` | 2026-09-04T15:08:42 |
| `ibkr` | `ibkr` | `45.148.10.240` | 2026-09-04T15:10:36 |
| `ibkrpro` | `ibkrpro` | `45.148.10.240` | 2026-09-04T15:12:26 |
| `root` | `ibkr` | `45.148.10.240` | 2026-09-04T15:14:11 |
| `root` | `123456789aA` | `217.60.255.130` | 2026-09-04T15:14:42 |
| `root` | `broker` | `45.148.10.240` | 2026-09-04T15:16:00 |
| `root` | `password` | `45.148.10.240` | 2026-09-04T15:23:28 |
| `root` | `1234` | `45.148.10.240` | 2026-09-04T15:25:23 |
| `root` | `123qweQWE` | `217.60.255.130` | 2026-09-04T15:25:49 |
| `root` | `admin123` | `45.148.10.240` | 2026-09-04T15:27:16 |
| `root` | `toor` | `45.148.10.240` | 2026-09-04T15:29:11 |
| `root` | `root123` | `45.148.10.240` | 2026-09-04T15:31:05 |
| `root` | `12345678` | `45.148.10.240` | 2026-09-04T15:32:54 |
| `root` | `1` | `45.148.10.240` | 2026-09-04T15:34:46 |
| `root` | `12345` | `45.148.10.240` | 2026-09-04T15:36:39 |
| `root` | `admin@789` | `217.60.255.130` | 2026-09-04T15:36:57 |
| `root` | `abcd1234` | `45.148.10.240` | 2026-09-04T15:38:30 |
| `root` | `default` | `45.148.10.240` | 2026-09-04T15:40:21 |
| `root` | `1qaz@WSX` | `45.148.10.240` | 2026-09-04T15:42:19 |
| `root` | `test` | `45.148.10.240` | 2026-09-04T15:44:15 |
| `root` | `abc123` | `45.148.10.240` | 2026-09-04T15:46:09 |
| `root` | `mustang@2016` | `217.60.255.130` | 2026-09-04T15:47:57 |
| `root` | `111111` | `45.148.10.240` | 2026-09-04T15:48:07 |
| `root` | `pass` | `45.148.10.240` | 2026-09-04T15:50:04 |
| `root` | `123` | `45.148.10.240` | 2026-09-04T15:51:55 |
| `root` | `qwerty` | `45.148.10.240` | 2026-09-04T15:53:46 |
| `root` | `123456789` | `45.148.10.240` | 2026-09-04T15:55:41 |
| `solana` | `solana` | `2.57.122.53` | 2026-09-04T15:56:15 |
| `root` | `1q2w3e4r` | `45.148.10.240` | 2026-09-04T15:57:33 |
| `rohit` | `123456` | `181.228.80.171` | 2026-09-04T15:58:24 |
| `345gs5662d34` | `345gs5662d34` | `181.228.80.171` | 2026-09-04T15:58:27 |
| `rohit` | `3245gs5662d34` | `181.228.80.171` | 2026-09-04T15:58:28 |
| `ubuntu` | `ubuntu` | `2.57.122.53` | 2026-09-04T15:58:31 |
| `root` | `1234qwerASDF` | `217.60.255.130` | 2026-09-04T15:58:58 |
| `root` | `ubuntu` | `45.148.10.240` | 2026-09-04T15:59:27 |
| `sol` | `sol` | `2.57.122.53` | 2026-09-04T16:00:53 |
| `root` | `server` | `45.148.10.240` | 2026-09-04T16:01:29 |
| `root` | `test123!@#` | `103.88.76.27` | 2026-09-04T16:02:33 |
| `345gs5662d34` | `345gs5662d34` | `103.88.76.27` | 2026-09-04T16:02:37 |
| `root` | `3245gs5662d34` | `103.88.76.27` | 2026-09-04T16:02:39 |
| `ubuntu` | `123456` | `2.57.122.53` | 2026-09-04T16:03:11 |
| `root` | `root1234` | `45.148.10.240` | 2026-09-04T16:03:29 |
| `sol` | `sol123` | `2.57.122.53` | 2026-09-04T16:05:20 |
| `root` | `raspberry` | `45.148.10.240` | 2026-09-04T16:05:26 |
| `root` | `qwe123` | `45.148.10.240` | 2026-09-04T16:07:26 |
| `sol` | `123` | `2.57.122.53` | 2026-09-04T16:07:35 |
| `root` | `q1w2e3r4` | `45.148.10.240` | 2026-09-04T16:09:24 |
| `eth-docker` | `eth-docker` | `2.57.122.53` | 2026-09-04T16:09:49 |
| `root` | `arman1234` | `217.60.255.130` | 2026-09-04T16:10:03 |
| `root` | `123123` | `45.148.10.240` | 2026-09-04T16:11:16 |
| `ethdocker` | `ethdocker` | `2.57.122.53` | 2026-09-04T16:12:05 |
| `root` | `P@ssw0rd` | `45.148.10.240` | 2026-09-04T16:13:14 |
| `ethd` | `ethd` | `2.57.122.53` | 2026-09-04T16:14:40 |
| `root` | `123qweasd` | `45.148.10.240` | 2026-09-04T16:15:11 |
| `firedancer` | `firedancer123` | `2.57.122.53` | 2026-09-04T16:17:04 |
| `root` | `rootroot` | `45.148.10.240` | 2026-09-04T16:17:06 |
| `root` | `1qaz2wsx` | `45.148.10.240` | 2026-09-04T16:19:04 |
| `lab` | `lab` | `2.57.122.53` | 2026-09-04T16:19:24 |
| `root` | `﻿------fuck------` | `64.112.40.44` | 2026-09-04T16:20:34 |
| `root` | `qwer1234` | `45.148.10.240` | 2026-09-04T16:21:06 |
| `root` | `Aditya@123` | `217.60.255.130` | 2026-09-04T16:21:07 |
| `lab` | `lab@123` | `2.57.122.53` | 2026-09-04T16:21:45 |
| `root` | `test123` | `45.148.10.240` | 2026-09-04T16:23:04 |
| `lab` | `lab123` | `2.57.122.53` | 2026-09-04T16:23:59 |
| `root` | `sysadmin` | `45.148.10.240` | 2026-09-04T16:25:03 |
| `user` | `1` | `2.57.122.53` | 2026-09-04T16:26:20 |
| `user` | `1234` | `2.57.122.53` | 2026-09-04T16:28:47 |
| `root` | `administrator` | `45.148.10.240` | 2026-09-04T16:29:04 |
| `root` | `000000` | `45.148.10.240` | 2026-09-04T16:30:58 |
| `radar` | `radar` | `2.57.122.53` | 2026-09-04T16:31:16 |
| `root` | `Servid0r123` | `217.60.255.130` | 2026-09-04T16:32:04 |
| `root` | `redhat` | `45.148.10.240` | 2026-09-04T16:32:57 |
| `postfix` | `postfix` | `2.57.122.53` | 2026-09-04T16:33:48 |
| `support` | `support` | `80.94.95.118` | 2026-09-04T16:34:46 |
| `root` | `passw0rd` | `45.148.10.240` | 2026-09-04T16:34:55 |
| `airflow` | `airflow` | `2.57.122.53` | 2026-09-04T16:36:13 |
| `pgsql` | `pgsql` | `2.57.122.53` | 2026-09-04T16:38:37 |
| `ethereumdocker` | `ethereumdocker` | `2.57.122.53` | 2026-09-04T16:41:05 |
| `root` | `admin#10` | `217.60.255.130` | 2026-09-04T16:43:04 |
| `docker` | `ethereum` | `2.57.122.53` | 2026-09-04T16:43:26 |
| `firedancer` | `firedancer` | `2.57.122.53` | 2026-09-04T16:45:56 |
| `steamcmd` | `1234` | `86.97.240.189` | 2026-09-04T16:47:35 |
| `345gs5662d34` | `345gs5662d34` | `86.97.240.189` | 2026-09-04T16:47:38 |
| `steamcmd` | `3245gs5662d34` | `86.97.240.189` | 2026-09-04T16:47:40 |
| `ubuntu` | `qwer1234` | `2.57.122.53` | 2026-09-04T16:48:27 |
| `ubuntu` | `1234qwer` | `2.57.122.53` | 2026-09-04T16:50:58 |
| `raydium` | `raydium` | `2.57.122.53` | 2026-09-04T16:53:33 |
| `root` | `Aa112233` | `217.60.255.130` | 2026-09-04T16:54:08 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **318** |
| Sessions with Fingerprint | **16** |
| Unique HASSH Fingerprints | **16** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 197 |
| libssh | 57 |
| Paramiko (Python) | 5 |
| OpenSSH | 2 |
| PuTTY | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `16443846184e...` | Generic scanner | 148 | 3 |
| `2ec37a7cc8da...` | Mirai/variant | 43 | 1 |
| `f555226df196...` | Mirai/variant | 31 | 11 |
| `419da4c91ddb...` | Modern SSH client | 22 | 1 |
| `a2de0f306611...` | Mirai/variant | 4 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `16443846184e...` | Go SSH scanner | 148 | 3 | Generic scanner |
| `2ec37a7cc8da...` | Go SSH scanner | 43 | 1 | Mirai/variant |
| `f555226df196...` | libssh | 31 | 11 | Mirai/variant |
| `419da4c91ddb...` | libssh | 22 | 1 | Modern SSH client |
| `a2de0f306611...` | Paramiko (Python) | 4 | 1 | Mirai/variant |
| `eff4c24daffc...` | Go SSH scanner | 2 | 1 | Modern SSH client |
| `98f63c4d9c87...` | Go SSH scanner | 2 | 2 | Generic scanner |
| `1f2f2f9b0a73...` | libssh | 2 | 2 | Mirai/variant |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **8** |
| Campaign Clusters | **3** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **Recon Loader Script** | 🟡 MEDIUM | 41 | 1 | `T1082, T1592, T1078, T1083` |
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1105, T1140, T1059.004` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 10 | 10 | `T1021.004, T1078, T1070, T1140` |

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
Source IPs: `80.94.92.179`

**🔴 HIGH · Mirai/IoT Botnet**

> Mirai-family IoT botnet. Executes busybox payloads for DDoS bot recruitment.

Representative commands:
```
enable
```
```
system
```
```
shell
```
```
sh
```
```
/bin/busybox TOKEN
```
Source IPs: `92.52.184.245`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `51.75.253.68`, `103.76.120.90`, `161.248.202.88`, `181.228.80.171`, `85.69.240.210`, `76.79.213.70`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **64** |
| Unique ASNs | **48** |
| High-Risk ASNs | **30** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS0` |  | 15 | HIGH |
| `AS204428` | SS-Net | 2 | HIGH |
| `AS7303` | Telecom Argentina S.A. | 2 | HIGH |
| `AS15557` | Societe Francaise Du Radiotelephone - SFR SA | 1 | HIGH |
| `AS24940` | Hetzner Online GmbH | 1 | HIGH |
| `AS265817` | Ruben Oscar Mosso(INTERZONA WIFI) | 1 | LOW |
| `AS202103` | Lanet Network Ltd | 1 | HIGH |
| `AS41608` | NextGenWebs, S.L. | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (253)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-8b0ace3d9c51

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-09-04 12:55 |
| **Last Seen** | 2026-09-04 12:55 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 12:55:12` | `cowrie.session.connect` |
| `2026-09-04 12:55:13` | `cowrie.client.version` |
| `2026-09-04 12:55:13` | `cowrie.client.kex` |
| `2026-09-04 12:55:14` | `cowrie.login.success` |
| `2026-09-04 12:55:16` | `cowrie.session.params` |
| `2026-09-04 12:55:16` | `cowrie.command.input` |
| `2026-09-04 12:55:16` | `cowrie.command.input` |
| `2026-09-04 12:55:16` | `cowrie.command.input` |
| `2026-09-04 12:55:16` | `cowrie.command.input` |
| `2026-09-04 12:55:16` | `cowrie.command.input` |
| `2026-09-04 12:55:16` | `cowrie.command.success` |
| `2026-09-04 12:55:16` | `cowrie.command.input` |
| `2026-09-04 12:55:16` | `cowrie.command.input` |
| `2026-09-04 12:55:16` | `cowrie.command.input` |
| `2026-09-04 12:55:16` | `cowrie.command.input` |
| `2026-09-04 12:55:17` | `cowrie.log.closed` |
| `2026-09-04 12:55:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-94dacc8e8627

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-09-04 12:55 |
| **Last Seen** | 2026-09-04 12:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 12:55:14` | `cowrie.session.connect` |
| `2026-09-04 12:55:14` | `cowrie.client.version` |
| `2026-09-04 12:55:14` | `cowrie.client.kex` |
| `2026-09-04 12:55:14` | `cowrie.login.success` |
| `2026-09-04 12:55:15` | `cowrie.session.params` |
| `2026-09-04 12:55:15` | `cowrie.command.input` |
| `2026-09-04 12:55:15` | `cowrie.log.closed` |
| `2026-09-04 12:55:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-345bb07fe1a8

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-09-04 12:56 |
| **Last Seen** | 2026-09-04 12:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 12:56:58` | `cowrie.session.connect` |
| `2026-09-04 12:56:58` | `cowrie.client.version` |
| `2026-09-04 12:56:58` | `cowrie.client.kex` |
| `2026-09-04 12:56:58` | `cowrie.login.success` |
| `2026-09-04 12:56:59` | `cowrie.session.params` |
| `2026-09-04 12:56:59` | `cowrie.command.input` |
| `2026-09-04 12:56:59` | `cowrie.log.closed` |
| `2026-09-04 12:56:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bff365cbad0d

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-09-04 12:57 |
| **Last Seen** | 2026-09-04 12:57 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 12:57:40` | `cowrie.session.connect` |
| `2026-09-04 12:57:40` | `cowrie.client.version` |
| `2026-09-04 12:57:40` | `cowrie.client.kex` |
| `2026-09-04 12:57:41` | `cowrie.login.success` |
| `2026-09-04 12:57:43` | `cowrie.session.params` |
| `2026-09-04 12:57:43` | `cowrie.command.input` |
| `2026-09-04 12:57:43` | `cowrie.command.input` |
| `2026-09-04 12:57:43` | `cowrie.command.input` |
| `2026-09-04 12:57:43` | `cowrie.command.input` |
| `2026-09-04 12:57:43` | `cowrie.command.input` |
| `2026-09-04 12:57:43` | `cowrie.command.success` |
| `2026-09-04 12:57:43` | `cowrie.command.input` |
| `2026-09-04 12:57:43` | `cowrie.command.input` |
| `2026-09-04 12:57:43` | `cowrie.command.input` |
| `2026-09-04 12:57:43` | `cowrie.command.input` |
| `2026-09-04 12:57:43` | `cowrie.log.closed` |
| `2026-09-04 12:57:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1be375de2fd4

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-04 12:58 |
| **Last Seen** | 2026-09-04 12:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 12:58:28` | `cowrie.session.connect` |
| `2026-09-04 12:58:28` | `cowrie.client.version` |
| `2026-09-04 12:58:28` | `cowrie.client.kex` |
| `2026-09-04 12:58:29` | `cowrie.login.success` |
| `2026-09-04 12:58:29` | `cowrie.direct-tcpip.request` |
| `2026-09-04 12:58:30` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-04 12:58:30` | `cowrie.direct-tcpip.data` |
| `2026-09-04 12:58:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-07c252790f9d

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-09-04 12:58 |
| **Last Seen** | 2026-09-04 12:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 12:58:40` | `cowrie.session.connect` |
| `2026-09-04 12:58:40` | `cowrie.client.version` |
| `2026-09-04 12:58:40` | `cowrie.client.kex` |
| `2026-09-04 12:58:40` | `cowrie.login.success` |
| `2026-09-04 12:58:41` | `cowrie.session.params` |
| `2026-09-04 12:58:41` | `cowrie.command.input` |
| `2026-09-04 12:58:41` | `cowrie.log.closed` |
| `2026-09-04 12:58:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-df8119a78f39

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-09-04 13:00 |
| **Last Seen** | 2026-09-04 13:00 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 13:00:11` | `cowrie.session.connect` |
| `2026-09-04 13:00:11` | `cowrie.client.version` |
| `2026-09-04 13:00:11` | `cowrie.client.kex` |
| `2026-09-04 13:00:13` | `cowrie.login.success` |
| `2026-09-04 13:00:17` | `cowrie.session.params` |
| `2026-09-04 13:00:17` | `cowrie.command.input` |
| `2026-09-04 13:00:17` | `cowrie.command.input` |
| `2026-09-04 13:00:17` | `cowrie.command.input` |
| `2026-09-04 13:00:17` | `cowrie.command.input` |
| `2026-09-04 13:00:17` | `cowrie.command.input` |
| `2026-09-04 13:00:17` | `cowrie.command.success` |
| `2026-09-04 13:00:17` | `cowrie.command.input` |
| `2026-09-04 13:00:17` | `cowrie.command.input` |
| `2026-09-04 13:00:17` | `cowrie.command.input` |
| `2026-09-04 13:00:17` | `cowrie.command.input` |
| `2026-09-04 13:00:17` | `cowrie.log.closed` |
| `2026-09-04 13:00:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8a3b943767de

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-09-04 13:00 |
| **Last Seen** | 2026-09-04 13:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 13:00:21` | `cowrie.session.connect` |
| `2026-09-04 13:00:21` | `cowrie.client.version` |
| `2026-09-04 13:00:21` | `cowrie.client.kex` |
| `2026-09-04 13:00:21` | `cowrie.login.success` |
| `2026-09-04 13:00:22` | `cowrie.session.params` |
| `2026-09-04 13:00:22` | `cowrie.command.input` |
| `2026-09-04 13:00:22` | `cowrie.log.closed` |
| `2026-09-04 13:00:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-07b4e11da420

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-09-04 13:02 |
| **Last Seen** | 2026-09-04 13:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 13:02:04` | `cowrie.session.connect` |
| `2026-09-04 13:02:04` | `cowrie.client.version` |
| `2026-09-04 13:02:04` | `cowrie.client.kex` |
| `2026-09-04 13:02:05` | `cowrie.login.success` |
| `2026-09-04 13:02:06` | `cowrie.session.params` |
| `2026-09-04 13:02:06` | `cowrie.command.input` |
| `2026-09-04 13:02:06` | `cowrie.log.closed` |
| `2026-09-04 13:02:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e49fdd5faced

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-09-04 13:02 |
| **Last Seen** | 2026-09-04 13:02 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 13:02:22` | `cowrie.session.connect` |
| `2026-09-04 13:02:22` | `cowrie.client.version` |
| `2026-09-04 13:02:22` | `cowrie.client.kex` |
| `2026-09-04 13:02:24` | `cowrie.login.success` |
| `2026-09-04 13:02:26` | `cowrie.session.params` |
| `2026-09-04 13:02:26` | `cowrie.command.input` |
| `2026-09-04 13:02:26` | `cowrie.command.input` |
| `2026-09-04 13:02:26` | `cowrie.command.input` |
| `2026-09-04 13:02:26` | `cowrie.command.input` |
| `2026-09-04 13:02:26` | `cowrie.command.input` |
| `2026-09-04 13:02:26` | `cowrie.command.success` |
| `2026-09-04 13:02:26` | `cowrie.command.input` |
| `2026-09-04 13:02:26` | `cowrie.command.input` |
| `2026-09-04 13:02:26` | `cowrie.command.input` |
| `2026-09-04 13:02:26` | `cowrie.command.input` |
| `2026-09-04 13:02:27` | `cowrie.log.closed` |
| `2026-09-04 13:02:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-73522ee2207d

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-09-04 13:03 |
| **Last Seen** | 2026-09-04 13:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 13:03:48` | `cowrie.session.connect` |
| `2026-09-04 13:03:48` | `cowrie.client.version` |
| `2026-09-04 13:03:48` | `cowrie.client.kex` |
| `2026-09-04 13:03:49` | `cowrie.login.success` |
| `2026-09-04 13:03:49` | `cowrie.session.params` |
| `2026-09-04 13:03:49` | `cowrie.command.input` |
| `2026-09-04 13:03:49` | `cowrie.log.closed` |
| `2026-09-04 13:03:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a0dcb5133d4c

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-09-04 13:04 |
| **Last Seen** | 2026-09-04 13:04 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 13:04:37` | `cowrie.session.connect` |
| `2026-09-04 13:04:37` | `cowrie.client.version` |
| `2026-09-04 13:04:37` | `cowrie.client.kex` |
| `2026-09-04 13:04:38` | `cowrie.login.success` |
| `2026-09-04 13:04:40` | `cowrie.session.params` |
| `2026-09-04 13:04:40` | `cowrie.command.input` |
| `2026-09-04 13:04:40` | `cowrie.command.input` |
| `2026-09-04 13:04:40` | `cowrie.command.input` |
| `2026-09-04 13:04:40` | `cowrie.command.input` |
| `2026-09-04 13:04:40` | `cowrie.command.input` |
| `2026-09-04 13:04:40` | `cowrie.command.success` |
| `2026-09-04 13:04:40` | `cowrie.command.input` |
| `2026-09-04 13:04:40` | `cowrie.command.input` |
| `2026-09-04 13:04:40` | `cowrie.command.input` |
| `2026-09-04 13:04:40` | `cowrie.command.input` |
| `2026-09-04 13:04:41` | `cowrie.log.closed` |
| `2026-09-04 13:04:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9b9278677891

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-09-04 13:04 |
| **Last Seen** | 2026-09-04 13:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 13:04:39` | `cowrie.session.connect` |
| `2026-09-04 13:04:39` | `cowrie.client.version` |
| `2026-09-04 13:04:39` | `cowrie.client.kex` |
| `2026-09-04 13:04:39` | `cowrie.login.success` |
| `2026-09-04 13:04:39` | `cowrie.direct-tcpip.request` |
| `2026-09-04 13:04:39` | `cowrie.direct-tcpip.data` |
| `2026-09-04 13:04:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-506c22171ef8

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-09-04 13:05 |
| **Last Seen** | 2026-09-04 13:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 13:05:29` | `cowrie.session.connect` |
| `2026-09-04 13:05:29` | `cowrie.client.version` |
| `2026-09-04 13:05:29` | `cowrie.client.kex` |
| `2026-09-04 13:05:30` | `cowrie.login.success` |
| `2026-09-04 13:05:30` | `cowrie.session.params` |
| `2026-09-04 13:05:30` | `cowrie.command.input` |
| `2026-09-04 13:05:30` | `cowrie.log.closed` |
| `2026-09-04 13:05:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f361747f41bb

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-09-04 13:06 |
| **Last Seen** | 2026-09-04 13:06 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 13:06:51` | `cowrie.session.connect` |
| `2026-09-04 13:06:51` | `cowrie.client.version` |
| `2026-09-04 13:06:51` | `cowrie.client.kex` |
| `2026-09-04 13:06:53` | `cowrie.login.success` |
| `2026-09-04 13:06:54` | `cowrie.session.params` |
| `2026-09-04 13:06:54` | `cowrie.command.input` |
| `2026-09-04 13:06:54` | `cowrie.command.input` |
| `2026-09-04 13:06:54` | `cowrie.command.input` |
| `2026-09-04 13:06:54` | `cowrie.command.input` |
| `2026-09-04 13:06:54` | `cowrie.command.input` |
| `2026-09-04 13:06:54` | `cowrie.command.success` |
| `2026-09-04 13:06:54` | `cowrie.command.input` |
| `2026-09-04 13:06:54` | `cowrie.command.input` |
| `2026-09-04 13:06:54` | `cowrie.command.input` |
| `2026-09-04 13:06:54` | `cowrie.command.input` |
| `2026-09-04 13:06:55` | `cowrie.log.closed` |
| `2026-09-04 13:06:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e6c58438bb6a

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-09-04 13:07 |
| **Last Seen** | 2026-09-04 13:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 13:07:06` | `cowrie.session.connect` |
| `2026-09-04 13:07:06` | `cowrie.client.version` |
| `2026-09-04 13:07:06` | `cowrie.client.kex` |
| `2026-09-04 13:07:07` | `cowrie.login.success` |
| `2026-09-04 13:07:08` | `cowrie.session.params` |
| `2026-09-04 13:07:08` | `cowrie.command.input` |
| `2026-09-04 13:07:08` | `cowrie.log.closed` |
| `2026-09-04 13:07:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-58f5902dc8d5

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-09-04 13:08 |
| **Last Seen** | 2026-09-04 13:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 13:08:47` | `cowrie.session.connect` |
| `2026-09-04 13:08:47` | `cowrie.client.version` |
| `2026-09-04 13:08:47` | `cowrie.client.kex` |
| `2026-09-04 13:08:48` | `cowrie.login.success` |
| `2026-09-04 13:08:48` | `cowrie.session.params` |
| `2026-09-04 13:08:48` | `cowrie.command.input` |
| `2026-09-04 13:08:48` | `cowrie.log.closed` |
| `2026-09-04 13:08:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9373762195ed

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-09-04 13:09 |
| **Last Seen** | 2026-09-04 13:09 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 13:09:09` | `cowrie.session.connect` |
| `2026-09-04 13:09:09` | `cowrie.client.version` |
| `2026-09-04 13:09:09` | `cowrie.client.kex` |
| `2026-09-04 13:09:10` | `cowrie.login.success` |
| `2026-09-04 13:09:12` | `cowrie.session.params` |
| `2026-09-04 13:09:12` | `cowrie.command.input` |
| `2026-09-04 13:09:12` | `cowrie.command.input` |
| `2026-09-04 13:09:12` | `cowrie.command.input` |
| `2026-09-04 13:09:12` | `cowrie.command.input` |
| `2026-09-04 13:09:12` | `cowrie.command.input` |
| `2026-09-04 13:09:12` | `cowrie.command.success` |
| `2026-09-04 13:09:12` | `cowrie.command.input` |
| `2026-09-04 13:09:12` | `cowrie.command.input` |
| `2026-09-04 13:09:12` | `cowrie.command.input` |
| `2026-09-04 13:09:12` | `cowrie.command.input` |
| `2026-09-04 13:09:12` | `cowrie.log.closed` |
| `2026-09-04 13:09:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-20ad5d73d021

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-04 13:09 |
| **Last Seen** | 2026-09-04 13:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 13:09:41` | `cowrie.session.connect` |
| `2026-09-04 13:09:41` | `cowrie.client.version` |
| `2026-09-04 13:09:41` | `cowrie.client.kex` |
| `2026-09-04 13:09:42` | `cowrie.login.success` |
| `2026-09-04 13:09:42` | `cowrie.direct-tcpip.request` |
| `2026-09-04 13:09:43` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-04 13:09:43` | `cowrie.direct-tcpip.data` |
| `2026-09-04 13:09:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9c96539d434b

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-09-04 13:10 |
| **Last Seen** | 2026-09-04 13:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 13:10:31` | `cowrie.session.connect` |
| `2026-09-04 13:10:31` | `cowrie.client.version` |
| `2026-09-04 13:10:31` | `cowrie.client.kex` |
| `2026-09-04 13:10:32` | `cowrie.login.success` |
| `2026-09-04 13:10:32` | `cowrie.session.params` |
| `2026-09-04 13:10:32` | `cowrie.command.input` |
| `2026-09-04 13:10:33` | `cowrie.log.closed` |
| `2026-09-04 13:10:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0e0149e32b73

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-09-04 13:11 |
| **Last Seen** | 2026-09-04 13:11 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 13:11:29` | `cowrie.session.connect` |
| `2026-09-04 13:11:29` | `cowrie.client.version` |
| `2026-09-04 13:11:29` | `cowrie.client.kex` |
| `2026-09-04 13:11:31` | `cowrie.login.success` |
| `2026-09-04 13:11:32` | `cowrie.session.params` |
| `2026-09-04 13:11:32` | `cowrie.command.input` |
| `2026-09-04 13:11:32` | `cowrie.command.input` |
| `2026-09-04 13:11:32` | `cowrie.command.input` |
| `2026-09-04 13:11:32` | `cowrie.command.input` |
| `2026-09-04 13:11:32` | `cowrie.command.input` |
| `2026-09-04 13:11:32` | `cowrie.command.success` |
| `2026-09-04 13:11:32` | `cowrie.command.input` |
| `2026-09-04 13:11:32` | `cowrie.command.input` |
| `2026-09-04 13:11:32` | `cowrie.command.input` |
| `2026-09-04 13:11:32` | `cowrie.command.input` |
| `2026-09-04 13:11:32` | `cowrie.log.closed` |
| `2026-09-04 13:11:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c58b77b75d23

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-09-04 13:12 |
| **Last Seen** | 2026-09-04 13:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 13:12:13` | `cowrie.session.connect` |
| `2026-09-04 13:12:13` | `cowrie.client.version` |
| `2026-09-04 13:12:14` | `cowrie.client.kex` |
| `2026-09-04 13:12:14` | `cowrie.login.success` |
| `2026-09-04 13:12:15` | `cowrie.session.params` |
| `2026-09-04 13:12:15` | `cowrie.command.input` |
| `2026-09-04 13:12:15` | `cowrie.log.closed` |
| `2026-09-04 13:12:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2cf6b8d9444e

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-09-04 13:13 |
| **Last Seen** | 2026-09-04 13:13 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 13:13:47` | `cowrie.session.connect` |
| `2026-09-04 13:13:47` | `cowrie.client.version` |
| `2026-09-04 13:13:47` | `cowrie.client.kex` |
| `2026-09-04 13:13:49` | `cowrie.login.success` |
| `2026-09-04 13:13:50` | `cowrie.session.params` |
| `2026-09-04 13:13:50` | `cowrie.command.input` |
| `2026-09-04 13:13:50` | `cowrie.command.input` |
| `2026-09-04 13:13:50` | `cowrie.command.input` |
| `2026-09-04 13:13:50` | `cowrie.command.input` |
| `2026-09-04 13:13:50` | `cowrie.command.input` |
| `2026-09-04 13:13:50` | `cowrie.command.success` |
| `2026-09-04 13:13:50` | `cowrie.command.input` |
| `2026-09-04 13:13:50` | `cowrie.command.input` |
| `2026-09-04 13:13:50` | `cowrie.command.input` |
| `2026-09-04 13:13:50` | `cowrie.command.input` |
| `2026-09-04 13:13:50` | `cowrie.log.closed` |
| `2026-09-04 13:13:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-54ed405a1c4f

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-09-04 13:13 |
| **Last Seen** | 2026-09-04 13:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 13:13:55` | `cowrie.session.connect` |
| `2026-09-04 13:13:55` | `cowrie.client.version` |
| `2026-09-04 13:13:55` | `cowrie.client.kex` |
| `2026-09-04 13:13:55` | `cowrie.login.success` |
| `2026-09-04 13:13:56` | `cowrie.session.params` |
| `2026-09-04 13:13:56` | `cowrie.command.input` |
| `2026-09-04 13:13:56` | `cowrie.log.closed` |
| `2026-09-04 13:13:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-29718285ab44

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-09-04 13:15 |
| **Last Seen** | 2026-09-04 13:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 13:15:42` | `cowrie.session.connect` |
| `2026-09-04 13:15:42` | `cowrie.client.version` |
| `2026-09-04 13:15:42` | `cowrie.client.kex` |
| `2026-09-04 13:15:42` | `cowrie.login.success` |
| `2026-09-04 13:15:43` | `cowrie.session.params` |
| `2026-09-04 13:15:43` | `cowrie.command.input` |
| `2026-09-04 13:15:43` | `cowrie.log.closed` |
| `2026-09-04 13:15:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9a276aa82efd

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-09-04 13:16 |
| **Last Seen** | 2026-09-04 13:16 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 13:16:06` | `cowrie.session.connect` |
| `2026-09-04 13:16:06` | `cowrie.client.version` |
| `2026-09-04 13:16:06` | `cowrie.client.kex` |
| `2026-09-04 13:16:08` | `cowrie.login.success` |
| `2026-09-04 13:16:09` | `cowrie.session.params` |
| `2026-09-04 13:16:09` | `cowrie.command.input` |
| `2026-09-04 13:16:09` | `cowrie.command.input` |
| `2026-09-04 13:16:09` | `cowrie.command.input` |
| `2026-09-04 13:16:09` | `cowrie.command.input` |
| `2026-09-04 13:16:09` | `cowrie.command.input` |
| `2026-09-04 13:16:09` | `cowrie.command.success` |
| `2026-09-04 13:16:09` | `cowrie.command.input` |
| `2026-09-04 13:16:09` | `cowrie.command.input` |
| `2026-09-04 13:16:09` | `cowrie.command.input` |
| `2026-09-04 13:16:09` | `cowrie.command.input` |
| `2026-09-04 13:16:09` | `cowrie.log.closed` |
| `2026-09-04 13:16:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cccf03f3c0ff

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-09-04 13:17 |
| **Last Seen** | 2026-09-04 13:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 13:17:27` | `cowrie.session.connect` |
| `2026-09-04 13:17:27` | `cowrie.client.version` |
| `2026-09-04 13:17:27` | `cowrie.client.kex` |
| `2026-09-04 13:17:28` | `cowrie.login.success` |
| `2026-09-04 13:17:28` | `cowrie.session.params` |
| `2026-09-04 13:17:28` | `cowrie.command.input` |
| `2026-09-04 13:17:29` | `cowrie.log.closed` |
| `2026-09-04 13:17:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8653465e2d08

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-09-04 13:18 |
| **Last Seen** | 2026-09-04 13:18 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 13:18:22` | `cowrie.session.connect` |
| `2026-09-04 13:18:22` | `cowrie.client.version` |
| `2026-09-04 13:18:22` | `cowrie.client.kex` |
| `2026-09-04 13:18:23` | `cowrie.login.success` |
| `2026-09-04 13:18:25` | `cowrie.session.params` |
| `2026-09-04 13:18:25` | `cowrie.command.input` |
| `2026-09-04 13:18:25` | `cowrie.command.input` |
| `2026-09-04 13:18:25` | `cowrie.command.input` |
| `2026-09-04 13:18:25` | `cowrie.command.input` |
| `2026-09-04 13:18:25` | `cowrie.command.input` |
| `2026-09-04 13:18:25` | `cowrie.command.success` |
| `2026-09-04 13:18:25` | `cowrie.command.input` |
| `2026-09-04 13:18:25` | `cowrie.command.input` |
| `2026-09-04 13:18:25` | `cowrie.command.input` |
| `2026-09-04 13:18:25` | `cowrie.command.input` |
| `2026-09-04 13:18:25` | `cowrie.log.closed` |
| `2026-09-04 13:18:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6117ea015959

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-09-04 13:19 |
| **Last Seen** | 2026-09-04 13:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 13:19:07` | `cowrie.session.connect` |
| `2026-09-04 13:19:07` | `cowrie.client.version` |
| `2026-09-04 13:19:07` | `cowrie.client.kex` |
| `2026-09-04 13:19:08` | `cowrie.login.success` |
| `2026-09-04 13:19:08` | `cowrie.session.params` |
| `2026-09-04 13:19:08` | `cowrie.command.input` |
| `2026-09-04 13:19:08` | `cowrie.log.closed` |
| `2026-09-04 13:19:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1b147ccfaa73

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-09-04 13:20 |
| **Last Seen** | 2026-09-04 13:20 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 13:20:38` | `cowrie.session.connect` |
| `2026-09-04 13:20:39` | `cowrie.client.version` |
| `2026-09-04 13:20:39` | `cowrie.client.kex` |
| `2026-09-04 13:20:40` | `cowrie.login.success` |
| `2026-09-04 13:20:42` | `cowrie.session.params` |
| `2026-09-04 13:20:42` | `cowrie.command.input` |
| `2026-09-04 13:20:42` | `cowrie.command.input` |
| `2026-09-04 13:20:42` | `cowrie.command.input` |
| `2026-09-04 13:20:42` | `cowrie.command.input` |
| `2026-09-04 13:20:42` | `cowrie.command.input` |
| `2026-09-04 13:20:42` | `cowrie.command.success` |
| `2026-09-04 13:20:42` | `cowrie.command.input` |
| `2026-09-04 13:20:42` | `cowrie.command.input` |
| `2026-09-04 13:20:42` | `cowrie.command.input` |
| `2026-09-04 13:20:42` | `cowrie.command.input` |
| `2026-09-04 13:20:42` | `cowrie.log.closed` |
| `2026-09-04 13:20:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-85620f067f7d

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-04 13:20 |
| **Last Seen** | 2026-09-04 13:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 13:20:44` | `cowrie.session.connect` |
| `2026-09-04 13:20:44` | `cowrie.client.version` |
| `2026-09-04 13:20:44` | `cowrie.client.kex` |
| `2026-09-04 13:20:45` | `cowrie.login.success` |
| `2026-09-04 13:20:45` | `cowrie.direct-tcpip.request` |
| `2026-09-04 13:20:45` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-04 13:20:45` | `cowrie.direct-tcpip.data` |
| `2026-09-04 13:20:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-392465fdaae7

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-09-04 13:20 |
| **Last Seen** | 2026-09-04 13:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 13:20:47` | `cowrie.session.connect` |
| `2026-09-04 13:20:47` | `cowrie.client.version` |
| `2026-09-04 13:20:47` | `cowrie.client.kex` |
| `2026-09-04 13:20:48` | `cowrie.login.success` |
| `2026-09-04 13:20:48` | `cowrie.session.params` |
| `2026-09-04 13:20:48` | `cowrie.command.input` |
| `2026-09-04 13:20:48` | `cowrie.log.closed` |
| `2026-09-04 13:20:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2dbbeacc72ca

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-09-04 13:22 |
| **Last Seen** | 2026-09-04 13:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 13:22:32` | `cowrie.session.connect` |
| `2026-09-04 13:22:32` | `cowrie.client.version` |
| `2026-09-04 13:22:32` | `cowrie.client.kex` |
| `2026-09-04 13:22:33` | `cowrie.login.success` |
| `2026-09-04 13:22:34` | `cowrie.session.params` |
| `2026-09-04 13:22:34` | `cowrie.command.input` |
| `2026-09-04 13:22:34` | `cowrie.log.closed` |
| `2026-09-04 13:22:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9726ab4380d2

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-09-04 13:22 |
| **Last Seen** | 2026-09-04 13:22 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 13:22:54` | `cowrie.session.connect` |
| `2026-09-04 13:22:55` | `cowrie.client.version` |
| `2026-09-04 13:22:55` | `cowrie.client.kex` |
| `2026-09-04 13:22:57` | `cowrie.login.success` |
| `2026-09-04 13:22:58` | `cowrie.session.params` |
| `2026-09-04 13:22:58` | `cowrie.command.input` |
| `2026-09-04 13:22:58` | `cowrie.command.input` |
| `2026-09-04 13:22:58` | `cowrie.command.input` |
| `2026-09-04 13:22:58` | `cowrie.command.input` |
| `2026-09-04 13:22:58` | `cowrie.command.input` |
| `2026-09-04 13:22:58` | `cowrie.command.success` |
| `2026-09-04 13:22:58` | `cowrie.command.input` |
| `2026-09-04 13:22:58` | `cowrie.command.input` |
| `2026-09-04 13:22:58` | `cowrie.command.input` |
| `2026-09-04 13:22:58` | `cowrie.command.input` |
| `2026-09-04 13:22:59` | `cowrie.log.closed` |
| `2026-09-04 13:22:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bdf4e1abc9ee

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-09-04 13:24 |
| **Last Seen** | 2026-09-04 13:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 13:24:14` | `cowrie.session.connect` |
| `2026-09-04 13:24:14` | `cowrie.client.version` |
| `2026-09-04 13:24:14` | `cowrie.client.kex` |
| `2026-09-04 13:24:14` | `cowrie.login.success` |
| `2026-09-04 13:24:15` | `cowrie.session.params` |
| `2026-09-04 13:24:15` | `cowrie.command.input` |
| `2026-09-04 13:24:15` | `cowrie.log.closed` |
| `2026-09-04 13:24:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-42fdf308a6fb

| Field | Detail |
|---|---|
| **Source IP** | `76.79.213[.]70` |
| **First Seen** | 2026-09-04 13:24 |
| **Last Seen** | 2026-09-04 13:24 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 13:24:52` | `cowrie.session.connect` |
| `2026-09-04 13:24:52` | `cowrie.client.version` |
| `2026-09-04 13:24:52` | `cowrie.client.kex` |
| `2026-09-04 13:24:52` | `cowrie.login.success` |
| `2026-09-04 13:24:53` | `cowrie.session.params` |
| `2026-09-04 13:24:53` | `cowrie.command.input` |
| `2026-09-04 13:24:53` | `cowrie.command.failed` |
| `2026-09-04 13:24:53` | `cowrie.log.closed` |
| `2026-09-04 13:24:54` | `cowrie.session.params` |
| `2026-09-04 13:24:54` | `cowrie.command.input` |
| `2026-09-04 13:24:54` | `cowrie.session.file_download` |
| `2026-09-04 13:24:54` | `cowrie.log.closed` |
| `2026-09-04 13:24:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `76.79.213[.]70` to AbuseIPDB if not already reported
- [ ] Block `76.79.213[.]70` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e37bcd0504a1

| Field | Detail |
|---|---|
| **Source IP** | `76.79.213[.]70` |
| **First Seen** | 2026-09-04 13:24 |
| **Last Seen** | 2026-09-04 13:24 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 13:24:54` | `cowrie.session.connect` |
| `2026-09-04 13:24:54` | `cowrie.client.version` |
| `2026-09-04 13:24:54` | `cowrie.client.kex` |
| `2026-09-04 13:24:55` | `cowrie.login.success` |
| `2026-09-04 13:24:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `76.79.213[.]70` to AbuseIPDB if not already reported
- [ ] Block `76.79.213[.]70` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b3ba6dfd69ce

| Field | Detail |
|---|---|
| **Source IP** | `76.79.213[.]70` |
| **First Seen** | 2026-09-04 13:24 |
| **Last Seen** | 2026-09-04 13:24 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 13:24:55` | `cowrie.session.connect` |
| `2026-09-04 13:24:55` | `cowrie.client.version` |
| `2026-09-04 13:24:55` | `cowrie.client.kex` |
| `2026-09-04 13:24:56` | `cowrie.login.success` |
| `2026-09-04 13:24:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `76.79.213[.]70` to AbuseIPDB if not already reported
- [ ] Block `76.79.213[.]70` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e7ef95523099

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-09-04 13:25 |
| **Last Seen** | 2026-09-04 13:25 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 13:25:09` | `cowrie.session.connect` |
| `2026-09-04 13:25:09` | `cowrie.client.version` |
| `2026-09-04 13:25:09` | `cowrie.client.kex` |
| `2026-09-04 13:25:11` | `cowrie.login.success` |
| `2026-09-04 13:25:13` | `cowrie.session.params` |
| `2026-09-04 13:25:13` | `cowrie.command.input` |
| `2026-09-04 13:25:13` | `cowrie.command.input` |
| `2026-09-04 13:25:13` | `cowrie.command.input` |
| `2026-09-04 13:25:13` | `cowrie.command.input` |
| `2026-09-04 13:25:13` | `cowrie.command.input` |
| `2026-09-04 13:25:13` | `cowrie.command.success` |
| `2026-09-04 13:25:13` | `cowrie.command.input` |
| `2026-09-04 13:25:13` | `cowrie.command.input` |
| `2026-09-04 13:25:13` | `cowrie.command.input` |
| `2026-09-04 13:25:13` | `cowrie.command.input` |
| `2026-09-04 13:25:13` | `cowrie.log.closed` |
| `2026-09-04 13:25:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c5fcf69b5541

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-09-04 13:25 |
| **Last Seen** | 2026-09-04 13:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 13:25:53` | `cowrie.session.connect` |
| `2026-09-04 13:25:53` | `cowrie.client.version` |
| `2026-09-04 13:25:53` | `cowrie.client.kex` |
| `2026-09-04 13:25:53` | `cowrie.login.success` |
| `2026-09-04 13:25:54` | `cowrie.session.params` |
| `2026-09-04 13:25:54` | `cowrie.command.input` |
| `2026-09-04 13:25:54` | `cowrie.log.closed` |
| `2026-09-04 13:25:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-40a9246e87cf

| Field | Detail |
|---|---|
| **Source IP** | `163.7.9[.]84` |
| **First Seen** | 2026-09-04 13:26 |
| **Last Seen** | 2026-09-04 13:27 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 13:26:55` | `cowrie.session.connect` |
| `2026-09-04 13:26:55` | `cowrie.client.version` |
| `2026-09-04 13:26:55` | `cowrie.client.kex` |
| `2026-09-04 13:26:56` | `cowrie.login.success` |
| `2026-09-04 13:26:57` | `cowrie.session.params` |
| `2026-09-04 13:26:57` | `cowrie.command.input` |
| `2026-09-04 13:26:57` | `cowrie.command.failed` |
| `2026-09-04 13:26:57` | `cowrie.log.closed` |
| `2026-09-04 13:26:58` | `cowrie.session.params` |
| `2026-09-04 13:26:58` | `cowrie.command.input` |
| `2026-09-04 13:26:59` | `cowrie.session.file_download` |
| `2026-09-04 13:26:59` | `cowrie.log.closed` |
| `2026-09-04 13:27:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `163.7.9[.]84` to AbuseIPDB if not already reported
- [ ] Block `163.7.9[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e30055dca94f

| Field | Detail |
|---|---|
| **Source IP** | `163.7.9[.]84` |
| **First Seen** | 2026-09-04 13:26 |
| **Last Seen** | 2026-09-04 13:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 13:26:59` | `cowrie.session.connect` |
| `2026-09-04 13:26:59` | `cowrie.client.version` |
| `2026-09-04 13:26:59` | `cowrie.client.kex` |
| `2026-09-04 13:27:00` | `cowrie.login.success` |
| `2026-09-04 13:27:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `163.7.9[.]84` to AbuseIPDB if not already reported
- [ ] Block `163.7.9[.]84` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-de1bd78af1ba

| Field | Detail |
|---|---|
| **Source IP** | `163.7.9[.]84` |
| **First Seen** | 2026-09-04 13:27 |
| **Last Seen** | 2026-09-04 13:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 13:27:01` | `cowrie.session.connect` |
| `2026-09-04 13:27:01` | `cowrie.client.version` |
| `2026-09-04 13:27:01` | `cowrie.client.kex` |
| `2026-09-04 13:27:02` | `cowrie.login.success` |
| `2026-09-04 13:27:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `163.7.9[.]84` to AbuseIPDB if not already reported
- [ ] Block `163.7.9[.]84` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e79cb9a8c57d

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-09-04 13:27 |
| **Last Seen** | 2026-09-04 13:27 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 13:27:23` | `cowrie.session.connect` |
| `2026-09-04 13:27:23` | `cowrie.client.version` |
| `2026-09-04 13:27:23` | `cowrie.client.kex` |
| `2026-09-04 13:27:24` | `cowrie.login.success` |
| `2026-09-04 13:27:26` | `cowrie.session.params` |
| `2026-09-04 13:27:26` | `cowrie.command.input` |
| `2026-09-04 13:27:26` | `cowrie.command.input` |
| `2026-09-04 13:27:26` | `cowrie.command.input` |
| `2026-09-04 13:27:26` | `cowrie.command.input` |
| `2026-09-04 13:27:26` | `cowrie.command.input` |
| `2026-09-04 13:27:26` | `cowrie.command.success` |
| `2026-09-04 13:27:26` | `cowrie.command.input` |
| `2026-09-04 13:27:26` | `cowrie.command.input` |
| `2026-09-04 13:27:26` | `cowrie.command.input` |
| `2026-09-04 13:27:26` | `cowrie.command.input` |
| `2026-09-04 13:27:27` | `cowrie.log.closed` |
| `2026-09-04 13:27:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d4653403e4c0

| Field | Detail |
|---|---|
| **Source IP** | `85.69.240[.]210` |
| **First Seen** | 2026-09-04 13:27 |
| **Last Seen** | 2026-09-04 13:27 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 13:27:34` | `cowrie.session.connect` |
| `2026-09-04 13:27:34` | `cowrie.client.version` |
| `2026-09-04 13:27:34` | `cowrie.client.kex` |
| `2026-09-04 13:27:34` | `cowrie.login.success` |
| `2026-09-04 13:27:35` | `cowrie.session.params` |
| `2026-09-04 13:27:35` | `cowrie.command.input` |
| `2026-09-04 13:27:35` | `cowrie.command.failed` |
| `2026-09-04 13:27:35` | `cowrie.log.closed` |
| `2026-09-04 13:27:36` | `cowrie.session.params` |
| `2026-09-04 13:27:36` | `cowrie.command.input` |
| `2026-09-04 13:27:36` | `cowrie.session.file_download` |
| `2026-09-04 13:27:36` | `cowrie.log.closed` |
| `2026-09-04 13:27:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.69.240[.]210` to AbuseIPDB if not already reported
- [ ] Block `85.69.240[.]210` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6b41f3b3c174

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-09-04 13:27 |
| **Last Seen** | 2026-09-04 13:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 13:27:36` | `cowrie.session.connect` |
| `2026-09-04 13:27:36` | `cowrie.client.version` |
| `2026-09-04 13:27:36` | `cowrie.client.kex` |
| `2026-09-04 13:27:37` | `cowrie.login.success` |
| `2026-09-04 13:27:37` | `cowrie.session.params` |
| `2026-09-04 13:27:37` | `cowrie.command.input` |
| `2026-09-04 13:27:37` | `cowrie.log.closed` |
| `2026-09-04 13:27:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-48f0d9e88511

| Field | Detail |
|---|---|
| **Source IP** | `85.69.240[.]210` |
| **First Seen** | 2026-09-04 13:27 |
| **Last Seen** | 2026-09-04 13:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 13:27:36` | `cowrie.session.connect` |
| `2026-09-04 13:27:36` | `cowrie.client.version` |
| `2026-09-04 13:27:36` | `cowrie.client.kex` |
| `2026-09-04 13:27:37` | `cowrie.login.success` |
| `2026-09-04 13:27:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.69.240[.]210` to AbuseIPDB if not already reported
- [ ] Block `85.69.240[.]210` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ce54fbd2fa70

| Field | Detail |
|---|---|
| **Source IP** | `85.69.240[.]210` |
| **First Seen** | 2026-09-04 13:27 |
| **Last Seen** | 2026-09-04 13:27 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 13:27:37` | `cowrie.session.connect` |
| `2026-09-04 13:27:37` | `cowrie.client.version` |
| `2026-09-04 13:27:38` | `cowrie.client.kex` |
| `2026-09-04 13:27:38` | `cowrie.login.success` |
| `2026-09-04 13:27:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.69.240[.]210` to AbuseIPDB if not already reported
- [ ] Block `85.69.240[.]210` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9cb76c614702

| Field | Detail |
|---|---|
| **Source IP** | `51.75.253[.]68` |
| **First Seen** | 2026-09-04 13:28 |
| **Last Seen** | 2026-09-04 13:28 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 13:28:49` | `cowrie.session.connect` |
| `2026-09-04 13:28:49` | `cowrie.client.version` |
| `2026-09-04 13:28:49` | `cowrie.client.kex` |
| `2026-09-04 13:28:49` | `cowrie.login.success` |
| `2026-09-04 13:28:50` | `cowrie.session.params` |
| `2026-09-04 13:28:50` | `cowrie.command.input` |
| `2026-09-04 13:28:50` | `cowrie.command.failed` |
| `2026-09-04 13:28:50` | `cowrie.log.closed` |
| `2026-09-04 13:28:51` | `cowrie.session.params` |
| `2026-09-04 13:28:51` | `cowrie.command.input` |
| `2026-09-04 13:28:51` | `cowrie.session.file_download` |
| `2026-09-04 13:28:51` | `cowrie.log.closed` |
| `2026-09-04 13:28:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.75.253[.]68` to AbuseIPDB if not already reported
- [ ] Block `51.75.253[.]68` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f74ba0051bf4

| Field | Detail |
|---|---|
| **Source IP** | `51.75.253[.]68` |
| **First Seen** | 2026-09-04 13:28 |
| **Last Seen** | 2026-09-04 13:28 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 13:28:51` | `cowrie.session.connect` |
| `2026-09-04 13:28:51` | `cowrie.client.version` |
| `2026-09-04 13:28:51` | `cowrie.client.kex` |
| `2026-09-04 13:28:51` | `cowrie.login.success` |
| `2026-09-04 13:28:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.75.253[.]68` to AbuseIPDB if not already reported
- [ ] Block `51.75.253[.]68` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ecbf3ebc0548

| Field | Detail |
|---|---|
| **Source IP** | `51.75.253[.]68` |
| **First Seen** | 2026-09-04 13:28 |
| **Last Seen** | 2026-09-04 13:28 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 13:28:52` | `cowrie.session.connect` |
| `2026-09-04 13:28:52` | `cowrie.client.version` |
| `2026-09-04 13:28:52` | `cowrie.client.kex` |
| `2026-09-04 13:28:52` | `cowrie.login.success` |
| `2026-09-04 13:28:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.75.253[.]68` to AbuseIPDB if not already reported
- [ ] Block `51.75.253[.]68` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-97e62448475c

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-09-04 13:29 |
| **Last Seen** | 2026-09-04 13:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 13:29:23` | `cowrie.session.connect` |
| `2026-09-04 13:29:23` | `cowrie.client.version` |
| `2026-09-04 13:29:23` | `cowrie.client.kex` |
| `2026-09-04 13:29:23` | `cowrie.login.success` |
| `2026-09-04 13:29:24` | `cowrie.session.params` |
| `2026-09-04 13:29:24` | `cowrie.command.input` |
| `2026-09-04 13:29:24` | `cowrie.log.closed` |
| `2026-09-04 13:29:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-feb4ac39aaee

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-09-04 13:29 |
| **Last Seen** | 2026-09-04 13:29 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 13:29:33` | `cowrie.session.connect` |
| `2026-09-04 13:29:34` | `cowrie.client.version` |
| `2026-09-04 13:29:34` | `cowrie.client.kex` |
| `2026-09-04 13:29:35` | `cowrie.login.success` |
| `2026-09-04 13:29:37` | `cowrie.session.params` |
| `2026-09-04 13:29:37` | `cowrie.command.input` |
| `2026-09-04 13:29:37` | `cowrie.command.input` |
| `2026-09-04 13:29:37` | `cowrie.command.input` |
| `2026-09-04 13:29:37` | `cowrie.command.input` |
| `2026-09-04 13:29:37` | `cowrie.command.input` |
| `2026-09-04 13:29:37` | `cowrie.command.success` |
| `2026-09-04 13:29:37` | `cowrie.command.input` |
| `2026-09-04 13:29:37` | `cowrie.command.input` |
| `2026-09-04 13:29:37` | `cowrie.command.input` |
| `2026-09-04 13:29:37` | `cowrie.command.input` |
| `2026-09-04 13:29:37` | `cowrie.log.closed` |
| `2026-09-04 13:29:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a3b6028dd829

| Field | Detail |
|---|---|
| **Source IP** | `161.248.202[.]88` |
| **First Seen** | 2026-09-04 13:29 |
| **Last Seen** | 2026-09-04 13:29 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 13:29:47` | `cowrie.session.connect` |
| `2026-09-04 13:29:47` | `cowrie.client.version` |
| `2026-09-04 13:29:47` | `cowrie.client.kex` |
| `2026-09-04 13:29:48` | `cowrie.login.success` |
| `2026-09-04 13:29:49` | `cowrie.session.params` |
| `2026-09-04 13:29:49` | `cowrie.command.input` |
| `2026-09-04 13:29:49` | `cowrie.command.failed` |
| `2026-09-04 13:29:50` | `cowrie.log.closed` |
| `2026-09-04 13:29:50` | `cowrie.session.params` |
| `2026-09-04 13:29:50` | `cowrie.command.input` |
| `2026-09-04 13:29:51` | `cowrie.session.file_download` |
| `2026-09-04 13:29:51` | `cowrie.log.closed` |
| `2026-09-04 13:29:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `161.248.202[.]88` to AbuseIPDB if not already reported
- [ ] Block `161.248.202[.]88` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e27e699954a9

| Field | Detail |
|---|---|
| **Source IP** | `161.248.202[.]88` |
| **First Seen** | 2026-09-04 13:29 |
| **Last Seen** | 2026-09-04 13:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 13:29:51` | `cowrie.session.connect` |
| `2026-09-04 13:29:51` | `cowrie.client.version` |
| `2026-09-04 13:29:51` | `cowrie.client.kex` |
| `2026-09-04 13:29:52` | `cowrie.login.success` |
| `2026-09-04 13:29:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `161.248.202[.]88` to AbuseIPDB if not already reported
- [ ] Block `161.248.202[.]88` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-284f876c5115

| Field | Detail |
|---|---|
| **Source IP** | `161.248.202[.]88` |
| **First Seen** | 2026-09-04 13:29 |
| **Last Seen** | 2026-09-04 13:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 13:29:52` | `cowrie.session.connect` |
| `2026-09-04 13:29:52` | `cowrie.client.version` |
| `2026-09-04 13:29:52` | `cowrie.client.kex` |
| `2026-09-04 13:29:53` | `cowrie.login.success` |
| `2026-09-04 13:29:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `161.248.202[.]88` to AbuseIPDB if not already reported
- [ ] Block `161.248.202[.]88` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f3c0c85cbe76

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-09-04 13:31 |
| **Last Seen** | 2026-09-04 13:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 13:31:06` | `cowrie.session.connect` |
| `2026-09-04 13:31:06` | `cowrie.client.version` |
| `2026-09-04 13:31:06` | `cowrie.client.kex` |
| `2026-09-04 13:31:07` | `cowrie.login.success` |
| `2026-09-04 13:31:07` | `cowrie.session.params` |
| `2026-09-04 13:31:07` | `cowrie.command.input` |
| `2026-09-04 13:31:07` | `cowrie.log.closed` |
| `2026-09-04 13:31:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2a8702c4729f

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-09-04 13:31 |
| **Last Seen** | 2026-09-04 13:31 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 13:31:40` | `cowrie.session.connect` |
| `2026-09-04 13:31:40` | `cowrie.client.version` |
| `2026-09-04 13:31:40` | `cowrie.client.kex` |
| `2026-09-04 13:31:42` | `cowrie.login.success` |
| `2026-09-04 13:31:44` | `cowrie.session.params` |
| `2026-09-04 13:31:44` | `cowrie.command.input` |
| `2026-09-04 13:31:44` | `cowrie.command.input` |
| `2026-09-04 13:31:44` | `cowrie.command.input` |
| `2026-09-04 13:31:44` | `cowrie.command.input` |
| `2026-09-04 13:31:44` | `cowrie.command.input` |
| `2026-09-04 13:31:44` | `cowrie.command.success` |
| `2026-09-04 13:31:44` | `cowrie.command.input` |
| `2026-09-04 13:31:44` | `cowrie.command.input` |
| `2026-09-04 13:31:44` | `cowrie.command.input` |
| `2026-09-04 13:31:44` | `cowrie.command.input` |
| `2026-09-04 13:31:44` | `cowrie.log.closed` |
| `2026-09-04 13:31:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-40f55b85577c

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-04 13:31 |
| **Last Seen** | 2026-09-04 13:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 13:31:52` | `cowrie.session.connect` |
| `2026-09-04 13:31:52` | `cowrie.client.version` |
| `2026-09-04 13:31:52` | `cowrie.client.kex` |
| `2026-09-04 13:31:53` | `cowrie.login.success` |
| `2026-09-04 13:31:53` | `cowrie.direct-tcpip.request` |
| `2026-09-04 13:31:53` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-04 13:31:53` | `cowrie.direct-tcpip.data` |
| `2026-09-04 13:31:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2dce7475c176

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-09-04 13:32 |
| **Last Seen** | 2026-09-04 13:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 13:32:47` | `cowrie.session.connect` |
| `2026-09-04 13:32:47` | `cowrie.client.version` |
| `2026-09-04 13:32:47` | `cowrie.client.kex` |
| `2026-09-04 13:32:48` | `cowrie.login.success` |
| `2026-09-04 13:32:49` | `cowrie.session.params` |
| `2026-09-04 13:32:49` | `cowrie.command.input` |
| `2026-09-04 13:32:49` | `cowrie.log.closed` |
| `2026-09-04 13:32:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b72a28d4d139

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-09-04 13:33 |
| **Last Seen** | 2026-09-04 13:33 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 13:33:47` | `cowrie.session.connect` |
| `2026-09-04 13:33:48` | `cowrie.client.version` |
| `2026-09-04 13:33:48` | `cowrie.client.kex` |
| `2026-09-04 13:33:49` | `cowrie.login.success` |
| `2026-09-04 13:33:51` | `cowrie.session.params` |
| `2026-09-04 13:33:51` | `cowrie.command.input` |
| `2026-09-04 13:33:51` | `cowrie.command.input` |
| `2026-09-04 13:33:51` | `cowrie.command.input` |
| `2026-09-04 13:33:51` | `cowrie.command.input` |
| `2026-09-04 13:33:51` | `cowrie.command.input` |
| `2026-09-04 13:33:51` | `cowrie.command.success` |
| `2026-09-04 13:33:51` | `cowrie.command.input` |
| `2026-09-04 13:33:51` | `cowrie.command.input` |
| `2026-09-04 13:33:51` | `cowrie.command.input` |
| `2026-09-04 13:33:51` | `cowrie.command.input` |
| `2026-09-04 13:33:51` | `cowrie.log.closed` |
| `2026-09-04 13:33:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1edf7b02dcda

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-09-04 13:34 |
| **Last Seen** | 2026-09-04 13:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 13:34:32` | `cowrie.session.connect` |
| `2026-09-04 13:34:32` | `cowrie.client.version` |
| `2026-09-04 13:34:32` | `cowrie.client.kex` |
| `2026-09-04 13:34:33` | `cowrie.login.success` |
| `2026-09-04 13:34:33` | `cowrie.session.params` |
| `2026-09-04 13:34:33` | `cowrie.command.input` |
| `2026-09-04 13:34:33` | `cowrie.log.closed` |
| `2026-09-04 13:34:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-44f674010029

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-09-04 13:36 |
| **Last Seen** | 2026-09-04 13:36 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 13:36:12` | `cowrie.session.connect` |
| `2026-09-04 13:36:12` | `cowrie.client.version` |
| `2026-09-04 13:36:14` | `cowrie.client.kex` |
| `2026-09-04 13:36:15` | `cowrie.login.success` |
| `2026-09-04 13:36:16` | `cowrie.session.params` |
| `2026-09-04 13:36:16` | `cowrie.command.input` |
| `2026-09-04 13:36:16` | `cowrie.command.input` |
| `2026-09-04 13:36:16` | `cowrie.command.input` |
| `2026-09-04 13:36:16` | `cowrie.command.input` |
| `2026-09-04 13:36:16` | `cowrie.command.input` |
| `2026-09-04 13:36:16` | `cowrie.command.success` |
| `2026-09-04 13:36:16` | `cowrie.command.input` |
| `2026-09-04 13:36:16` | `cowrie.command.input` |
| `2026-09-04 13:36:16` | `cowrie.command.input` |
| `2026-09-04 13:36:16` | `cowrie.command.input` |
| `2026-09-04 13:36:17` | `cowrie.log.closed` |
| `2026-09-04 13:36:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-380dd5e9cb9c

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-09-04 13:36 |
| **Last Seen** | 2026-09-04 13:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 13:36:18` | `cowrie.session.connect` |
| `2026-09-04 13:36:18` | `cowrie.client.version` |
| `2026-09-04 13:36:18` | `cowrie.client.kex` |
| `2026-09-04 13:36:19` | `cowrie.login.success` |
| `2026-09-04 13:36:19` | `cowrie.session.params` |
| `2026-09-04 13:36:19` | `cowrie.command.input` |
| `2026-09-04 13:36:20` | `cowrie.log.closed` |
| `2026-09-04 13:36:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e4013ae75479

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-09-04 13:38 |
| **Last Seen** | 2026-09-04 13:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 13:38:00` | `cowrie.session.connect` |
| `2026-09-04 13:38:00` | `cowrie.client.version` |
| `2026-09-04 13:38:00` | `cowrie.client.kex` |
| `2026-09-04 13:38:00` | `cowrie.login.success` |
| `2026-09-04 13:38:01` | `cowrie.session.params` |
| `2026-09-04 13:38:01` | `cowrie.command.input` |
| `2026-09-04 13:38:01` | `cowrie.log.closed` |
| `2026-09-04 13:38:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c29114af4655

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-09-04 13:38 |
| **Last Seen** | 2026-09-04 13:38 |
| **Session Duration** | 16s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 13:38:19` | `cowrie.session.connect` |
| `2026-09-04 13:38:21` | `cowrie.client.version` |
| `2026-09-04 13:38:21` | `cowrie.client.kex` |
| `2026-09-04 13:38:28` | `cowrie.login.success` |
| `2026-09-04 13:38:32` | `cowrie.session.params` |
| `2026-09-04 13:38:32` | `cowrie.command.input` |
| `2026-09-04 13:38:32` | `cowrie.command.input` |
| `2026-09-04 13:38:32` | `cowrie.command.input` |
| `2026-09-04 13:38:32` | `cowrie.command.input` |
| `2026-09-04 13:38:32` | `cowrie.command.input` |
| `2026-09-04 13:38:32` | `cowrie.command.success` |
| `2026-09-04 13:38:32` | `cowrie.command.input` |
| `2026-09-04 13:38:32` | `cowrie.command.input` |
| `2026-09-04 13:38:32` | `cowrie.command.input` |
| `2026-09-04 13:38:32` | `cowrie.command.input` |
| `2026-09-04 13:38:34` | `cowrie.log.closed` |
| `2026-09-04 13:38:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1dfd48f07bd0

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-09-04 13:39 |
| **Last Seen** | 2026-09-04 13:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 13:39:41` | `cowrie.session.connect` |
| `2026-09-04 13:39:41` | `cowrie.client.version` |
| `2026-09-04 13:39:41` | `cowrie.client.kex` |
| `2026-09-04 13:39:41` | `cowrie.login.success` |
| `2026-09-04 13:39:42` | `cowrie.session.params` |
| `2026-09-04 13:39:42` | `cowrie.command.input` |
| `2026-09-04 13:39:42` | `cowrie.log.closed` |
| `2026-09-04 13:39:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7ea5d4f06c1c

| Field | Detail |
|---|---|
| **Source IP** | `117.50.194[.]182` |
| **First Seen** | 2026-09-04 13:40 |
| **Last Seen** | 2026-09-04 13:43 |
| **Session Duration** | 184s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `id, cat /etc/passwd, echo -e "\x61\x75\x74\x68\x5F\x6F\x6B\x0A"` |
| **TTPs (MITRE)** | T1003.008 · T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 13:40:07` | `cowrie.session.connect` |
| `2026-09-04 13:40:10` | `cowrie.telnet.option` |
| `2026-09-04 13:40:11` | `cowrie.telnet.option` |
| `2026-09-04 13:40:11` | `cowrie.login.success` |
| `2026-09-04 13:40:11` | `cowrie.session.params` |
| `2026-09-04 13:40:13` | `cowrie.telnet.option` |
| `2026-09-04 13:40:13` | `cowrie.telnet.option` |
| `2026-09-04 13:40:13` | `cowrie.command.input` |
| `2026-09-04 13:40:13` | `cowrie.command.input` |
| `2026-09-04 13:40:13` | `cowrie.command.input` |
| `2026-09-04 13:43:11` | `cowrie.log.closed` |
| `2026-09-04 13:43:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.50.194[.]182` to AbuseIPDB if not already reported
- [ ] Block `117.50.194[.]182` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-43cde4e841bf

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-09-04 13:40 |
| **Last Seen** | 2026-09-04 13:40 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 13:40:11` | `cowrie.session.connect` |
| `2026-09-04 13:40:12` | `cowrie.client.version` |
| `2026-09-04 13:40:12` | `cowrie.client.kex` |
| `2026-09-04 13:40:20` | `cowrie.login.success` |
| `2026-09-04 13:40:24` | `cowrie.session.params` |
| `2026-09-04 13:40:24` | `cowrie.command.input` |
| `2026-09-04 13:40:24` | `cowrie.command.input` |
| `2026-09-04 13:40:24` | `cowrie.command.input` |
| `2026-09-04 13:40:24` | `cowrie.command.input` |
| `2026-09-04 13:40:24` | `cowrie.command.input` |
| `2026-09-04 13:40:24` | `cowrie.command.success` |
| `2026-09-04 13:40:24` | `cowrie.command.input` |
| `2026-09-04 13:40:24` | `cowrie.command.input` |
| `2026-09-04 13:40:24` | `cowrie.command.input` |
| `2026-09-04 13:40:24` | `cowrie.command.input` |
| `2026-09-04 13:40:26` | `cowrie.log.closed` |
| `2026-09-04 13:40:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fc2516d59baa

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-09-04 13:41 |
| **Last Seen** | 2026-09-04 13:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 13:41:28` | `cowrie.session.connect` |
| `2026-09-04 13:41:28` | `cowrie.client.version` |
| `2026-09-04 13:41:28` | `cowrie.client.kex` |
| `2026-09-04 13:41:29` | `cowrie.login.success` |
| `2026-09-04 13:41:29` | `cowrie.session.params` |
| `2026-09-04 13:41:29` | `cowrie.command.input` |
| `2026-09-04 13:41:29` | `cowrie.log.closed` |
| `2026-09-04 13:41:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-46a03331e391

| Field | Detail |
|---|---|
| **Source IP** | `47.236.238[.]212` |
| **First Seen** | 2026-09-04 13:42 |
| **Last Seen** | 2026-09-04 13:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 13:42:40` | `cowrie.session.connect` |
| `2026-09-04 13:42:40` | `cowrie.client.version` |
| `2026-09-04 13:42:40` | `cowrie.client.kex` |
| `2026-09-04 13:42:41` | `cowrie.login.success` |
| `2026-09-04 13:42:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.236.238[.]212` to AbuseIPDB if not already reported
- [ ] Block `47.236.238[.]212` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eef41c67614a

| Field | Detail |
|---|---|
| **Source IP** | `130.12.180[.]51` |
| **First Seen** | 2026-09-04 13:42 |
| **Last Seen** | 2026-09-04 13:42 |
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
| `2026-09-04 13:42:41` | `cowrie.session.connect` |
| `2026-09-04 13:42:41` | `cowrie.client.version` |
| `2026-09-04 13:42:41` | `cowrie.client.kex` |
| `2026-09-04 13:42:41` | `cowrie.login.success` |
| `2026-09-04 13:42:43` | `cowrie.session.params` |
| `2026-09-04 13:42:43` | `cowrie.command.input` |
| `2026-09-04 13:42:43` | `cowrie.session.file_download` |
| `2026-09-04 13:42:43` | `cowrie.session.file_download` |
| `2026-09-04 13:42:43` | `cowrie.log.closed` |
| `2026-09-04 13:42:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.180[.]51` to AbuseIPDB if not already reported
- [ ] Block `130.12.180[.]51` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ae00aa626fdb

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-04 13:43 |
| **Last Seen** | 2026-09-04 13:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 13:43:00` | `cowrie.session.connect` |
| `2026-09-04 13:43:00` | `cowrie.client.version` |
| `2026-09-04 13:43:01` | `cowrie.client.kex` |
| `2026-09-04 13:43:02` | `cowrie.login.success` |
| `2026-09-04 13:43:02` | `cowrie.direct-tcpip.request` |
| `2026-09-04 13:43:02` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-04 13:43:02` | `cowrie.direct-tcpip.data` |
| `2026-09-04 13:43:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1344b34efa6e

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-09-04 13:43 |
| **Last Seen** | 2026-09-04 13:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 13:43:13` | `cowrie.session.connect` |
| `2026-09-04 13:43:13` | `cowrie.client.version` |
| `2026-09-04 13:43:13` | `cowrie.client.kex` |
| `2026-09-04 13:43:14` | `cowrie.login.success` |
| `2026-09-04 13:43:14` | `cowrie.session.params` |
| `2026-09-04 13:43:14` | `cowrie.command.input` |
| `2026-09-04 13:43:14` | `cowrie.log.closed` |
| `2026-09-04 13:43:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-97e273c55c4c

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-09-04 13:43 |
| **Last Seen** | 2026-09-04 13:44 |
| **Session Duration** | 16s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 13:43:59` | `cowrie.session.connect` |
| `2026-09-04 13:44:01` | `cowrie.client.version` |
| `2026-09-04 13:44:01` | `cowrie.client.kex` |
| `2026-09-04 13:44:08` | `cowrie.login.success` |
| `2026-09-04 13:44:12` | `cowrie.session.params` |
| `2026-09-04 13:44:12` | `cowrie.command.input` |
| `2026-09-04 13:44:12` | `cowrie.command.input` |
| `2026-09-04 13:44:12` | `cowrie.command.input` |
| `2026-09-04 13:44:12` | `cowrie.command.input` |
| `2026-09-04 13:44:12` | `cowrie.command.input` |
| `2026-09-04 13:44:12` | `cowrie.command.success` |
| `2026-09-04 13:44:12` | `cowrie.command.input` |
| `2026-09-04 13:44:12` | `cowrie.command.input` |
| `2026-09-04 13:44:12` | `cowrie.command.input` |
| `2026-09-04 13:44:12` | `cowrie.command.input` |
| `2026-09-04 13:44:14` | `cowrie.log.closed` |
| `2026-09-04 13:44:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8ed960d1997e

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-09-04 13:44 |
| **Last Seen** | 2026-09-04 13:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 13:44:54` | `cowrie.session.connect` |
| `2026-09-04 13:44:54` | `cowrie.client.version` |
| `2026-09-04 13:44:54` | `cowrie.client.kex` |
| `2026-09-04 13:44:55` | `cowrie.login.success` |
| `2026-09-04 13:44:55` | `cowrie.session.params` |
| `2026-09-04 13:44:55` | `cowrie.command.input` |
| `2026-09-04 13:44:55` | `cowrie.log.closed` |
| `2026-09-04 13:44:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-92ab4a9c9722

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-09-04 13:45 |
| **Last Seen** | 2026-09-04 13:46 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 13:45:51` | `cowrie.session.connect` |
| `2026-09-04 13:45:53` | `cowrie.client.version` |
| `2026-09-04 13:45:53` | `cowrie.client.kex` |
| `2026-09-04 13:45:59` | `cowrie.login.success` |
| `2026-09-04 13:46:03` | `cowrie.session.params` |
| `2026-09-04 13:46:03` | `cowrie.command.input` |
| `2026-09-04 13:46:03` | `cowrie.command.input` |
| `2026-09-04 13:46:03` | `cowrie.command.input` |
| `2026-09-04 13:46:03` | `cowrie.command.input` |
| `2026-09-04 13:46:03` | `cowrie.command.input` |
| `2026-09-04 13:46:03` | `cowrie.command.success` |
| `2026-09-04 13:46:03` | `cowrie.command.input` |
| `2026-09-04 13:46:03` | `cowrie.command.input` |
| `2026-09-04 13:46:03` | `cowrie.command.input` |
| `2026-09-04 13:46:03` | `cowrie.command.input` |
| `2026-09-04 13:46:05` | `cowrie.log.closed` |
| `2026-09-04 13:46:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e0db81e10da0

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-09-04 13:46 |
| **Last Seen** | 2026-09-04 13:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 13:46:37` | `cowrie.session.connect` |
| `2026-09-04 13:46:37` | `cowrie.client.version` |
| `2026-09-04 13:46:37` | `cowrie.client.kex` |
| `2026-09-04 13:46:38` | `cowrie.login.success` |
| `2026-09-04 13:46:38` | `cowrie.session.params` |
| `2026-09-04 13:46:38` | `cowrie.command.input` |
| `2026-09-04 13:46:39` | `cowrie.log.closed` |
| `2026-09-04 13:46:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-670dad360ca4

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-09-04 13:47 |
| **Last Seen** | 2026-09-04 13:47 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 13:47:46` | `cowrie.session.connect` |
| `2026-09-04 13:47:47` | `cowrie.client.version` |
| `2026-09-04 13:47:47` | `cowrie.client.kex` |
| `2026-09-04 13:47:53` | `cowrie.login.success` |
| `2026-09-04 13:47:55` | `cowrie.session.params` |
| `2026-09-04 13:47:55` | `cowrie.command.input` |
| `2026-09-04 13:47:55` | `cowrie.command.input` |
| `2026-09-04 13:47:55` | `cowrie.command.input` |
| `2026-09-04 13:47:55` | `cowrie.command.input` |
| `2026-09-04 13:47:55` | `cowrie.command.input` |
| `2026-09-04 13:47:55` | `cowrie.command.success` |
| `2026-09-04 13:47:55` | `cowrie.command.input` |
| `2026-09-04 13:47:55` | `cowrie.command.input` |
| `2026-09-04 13:47:55` | `cowrie.command.input` |
| `2026-09-04 13:47:55` | `cowrie.command.input` |
| `2026-09-04 13:47:56` | `cowrie.log.closed` |
| `2026-09-04 13:47:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7dda6441d867

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-09-04 13:48 |
| **Last Seen** | 2026-09-04 13:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 13:48:23` | `cowrie.session.connect` |
| `2026-09-04 13:48:23` | `cowrie.client.version` |
| `2026-09-04 13:48:23` | `cowrie.client.kex` |
| `2026-09-04 13:48:24` | `cowrie.login.success` |
| `2026-09-04 13:48:25` | `cowrie.session.params` |
| `2026-09-04 13:48:25` | `cowrie.command.input` |
| `2026-09-04 13:48:25` | `cowrie.log.closed` |
| `2026-09-04 13:48:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9ddcf06c8f49

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-09-04 13:49 |
| **Last Seen** | 2026-09-04 13:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 13:49:26` | `cowrie.session.connect` |
| `2026-09-04 13:49:26` | `cowrie.client.version` |
| `2026-09-04 13:49:26` | `cowrie.client.kex` |
| `2026-09-04 13:49:27` | `cowrie.login.success` |
| `2026-09-04 13:49:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-65e4dd2d79b0

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-09-04 13:49 |
| **Last Seen** | 2026-09-04 13:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 13:49:26` | `cowrie.session.connect` |
| `2026-09-04 13:49:26` | `cowrie.client.version` |
| `2026-09-04 13:49:26` | `cowrie.client.kex` |
| `2026-09-04 13:49:27` | `cowrie.login.success` |
| `2026-09-04 13:49:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e07405d6cb10

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-09-04 13:49 |
| **Last Seen** | 2026-09-04 13:49 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 13:49:37` | `cowrie.session.connect` |
| `2026-09-04 13:49:38` | `cowrie.client.version` |
| `2026-09-04 13:49:38` | `cowrie.client.kex` |
| `2026-09-04 13:49:44` | `cowrie.login.success` |
| `2026-09-04 13:49:48` | `cowrie.session.params` |
| `2026-09-04 13:49:48` | `cowrie.command.input` |
| `2026-09-04 13:49:48` | `cowrie.command.input` |
| `2026-09-04 13:49:48` | `cowrie.command.input` |
| `2026-09-04 13:49:48` | `cowrie.command.input` |
| `2026-09-04 13:49:48` | `cowrie.command.input` |
| `2026-09-04 13:49:48` | `cowrie.command.success` |
| `2026-09-04 13:49:48` | `cowrie.command.input` |
| `2026-09-04 13:49:48` | `cowrie.command.input` |
| `2026-09-04 13:49:48` | `cowrie.command.input` |
| `2026-09-04 13:49:48` | `cowrie.command.input` |
| `2026-09-04 13:49:49` | `cowrie.log.closed` |
| `2026-09-04 13:49:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e4a0803be3fa

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-09-04 13:50 |
| **Last Seen** | 2026-09-04 13:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 13:50:07` | `cowrie.session.connect` |
| `2026-09-04 13:50:07` | `cowrie.client.version` |
| `2026-09-04 13:50:07` | `cowrie.client.kex` |
| `2026-09-04 13:50:07` | `cowrie.login.success` |
| `2026-09-04 13:50:08` | `cowrie.session.params` |
| `2026-09-04 13:50:08` | `cowrie.command.input` |
| `2026-09-04 13:50:08` | `cowrie.log.closed` |
| `2026-09-04 13:50:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4f46041fea63

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-09-04 13:51 |
| **Last Seen** | 2026-09-04 13:51 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 13:51:28` | `cowrie.session.connect` |
| `2026-09-04 13:51:30` | `cowrie.client.version` |
| `2026-09-04 13:51:30` | `cowrie.client.kex` |
| `2026-09-04 13:51:35` | `cowrie.login.success` |
| `2026-09-04 13:51:39` | `cowrie.session.params` |
| `2026-09-04 13:51:39` | `cowrie.command.input` |
| `2026-09-04 13:51:39` | `cowrie.command.input` |
| `2026-09-04 13:51:39` | `cowrie.command.input` |
| `2026-09-04 13:51:39` | `cowrie.command.input` |
| `2026-09-04 13:51:39` | `cowrie.command.input` |
| `2026-09-04 13:51:39` | `cowrie.command.success` |
| `2026-09-04 13:51:39` | `cowrie.command.input` |
| `2026-09-04 13:51:39` | `cowrie.command.input` |
| `2026-09-04 13:51:39` | `cowrie.command.input` |
| `2026-09-04 13:51:39` | `cowrie.command.input` |
| `2026-09-04 13:51:40` | `cowrie.log.closed` |
| `2026-09-04 13:51:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2cf5853462b1

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-09-04 13:51 |
| **Last Seen** | 2026-09-04 13:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 13:51:48` | `cowrie.session.connect` |
| `2026-09-04 13:51:48` | `cowrie.client.version` |
| `2026-09-04 13:51:48` | `cowrie.client.kex` |
| `2026-09-04 13:51:48` | `cowrie.login.success` |
| `2026-09-04 13:51:49` | `cowrie.session.params` |
| `2026-09-04 13:51:49` | `cowrie.command.input` |
| `2026-09-04 13:51:49` | `cowrie.log.closed` |
| `2026-09-04 13:51:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-41c471ef2c6f

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-09-04 13:53 |
| **Last Seen** | 2026-09-04 13:53 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 13:53:20` | `cowrie.session.connect` |
| `2026-09-04 13:53:21` | `cowrie.client.version` |
| `2026-09-04 13:53:21` | `cowrie.client.kex` |
| `2026-09-04 13:53:28` | `cowrie.login.success` |
| `2026-09-04 13:53:31` | `cowrie.session.params` |
| `2026-09-04 13:53:31` | `cowrie.command.input` |
| `2026-09-04 13:53:31` | `cowrie.command.input` |
| `2026-09-04 13:53:31` | `cowrie.command.input` |
| `2026-09-04 13:53:31` | `cowrie.command.input` |
| `2026-09-04 13:53:31` | `cowrie.command.input` |
| `2026-09-04 13:53:31` | `cowrie.command.success` |
| `2026-09-04 13:53:31` | `cowrie.command.input` |
| `2026-09-04 13:53:31` | `cowrie.command.input` |
| `2026-09-04 13:53:31` | `cowrie.command.input` |
| `2026-09-04 13:53:31` | `cowrie.command.input` |
| `2026-09-04 13:53:33` | `cowrie.log.closed` |
| `2026-09-04 13:53:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ea7316c055cf

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-09-04 13:53 |
| **Last Seen** | 2026-09-04 13:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 13:53:34` | `cowrie.session.connect` |
| `2026-09-04 13:53:34` | `cowrie.client.version` |
| `2026-09-04 13:53:34` | `cowrie.client.kex` |
| `2026-09-04 13:53:34` | `cowrie.login.success` |
| `2026-09-04 13:53:35` | `cowrie.session.params` |
| `2026-09-04 13:53:35` | `cowrie.command.input` |
| `2026-09-04 13:53:35` | `cowrie.log.closed` |
| `2026-09-04 13:53:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b05f35929c7e

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-04 13:54 |
| **Last Seen** | 2026-09-04 13:54 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 13:54:22` | `cowrie.session.connect` |
| `2026-09-04 13:54:22` | `cowrie.client.version` |
| `2026-09-04 13:54:23` | `cowrie.client.kex` |
| `2026-09-04 13:54:24` | `cowrie.login.success` |
| `2026-09-04 13:54:24` | `cowrie.direct-tcpip.request` |
| `2026-09-04 13:54:24` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-04 13:54:24` | `cowrie.direct-tcpip.data` |
| `2026-09-04 13:54:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-43afc1837c87

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-09-04 13:55 |
| **Last Seen** | 2026-09-04 13:55 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 13:55:10` | `cowrie.session.connect` |
| `2026-09-04 13:55:11` | `cowrie.client.version` |
| `2026-09-04 13:55:11` | `cowrie.client.kex` |
| `2026-09-04 13:55:18` | `cowrie.login.success` |
| `2026-09-04 13:55:21` | `cowrie.session.params` |
| `2026-09-04 13:55:21` | `cowrie.command.input` |
| `2026-09-04 13:55:21` | `cowrie.command.input` |
| `2026-09-04 13:55:21` | `cowrie.command.input` |
| `2026-09-04 13:55:21` | `cowrie.command.input` |
| `2026-09-04 13:55:21` | `cowrie.command.input` |
| `2026-09-04 13:55:21` | `cowrie.command.success` |
| `2026-09-04 13:55:21` | `cowrie.command.input` |
| `2026-09-04 13:55:21` | `cowrie.command.input` |
| `2026-09-04 13:55:21` | `cowrie.command.input` |
| `2026-09-04 13:55:21` | `cowrie.command.input` |
| `2026-09-04 13:55:22` | `cowrie.log.closed` |
| `2026-09-04 13:55:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-95aef4ca6bc6

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-09-04 13:55 |
| **Last Seen** | 2026-09-04 13:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 13:55:21` | `cowrie.session.connect` |
| `2026-09-04 13:55:21` | `cowrie.client.version` |
| `2026-09-04 13:55:21` | `cowrie.client.kex` |
| `2026-09-04 13:55:22` | `cowrie.login.success` |
| `2026-09-04 13:55:22` | `cowrie.session.params` |
| `2026-09-04 13:55:22` | `cowrie.command.input` |
| `2026-09-04 13:55:23` | `cowrie.log.closed` |
| `2026-09-04 13:55:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-54db13c9e10e

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-09-04 13:57 |
| **Last Seen** | 2026-09-04 13:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 13:57:05` | `cowrie.session.connect` |
| `2026-09-04 13:57:05` | `cowrie.client.version` |
| `2026-09-04 13:57:05` | `cowrie.client.kex` |
| `2026-09-04 13:57:05` | `cowrie.login.success` |
| `2026-09-04 13:57:06` | `cowrie.session.params` |
| `2026-09-04 13:57:06` | `cowrie.command.input` |
| `2026-09-04 13:57:06` | `cowrie.log.closed` |
| `2026-09-04 13:57:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-647ef015f091

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-09-04 13:57 |
| **Last Seen** | 2026-09-04 13:57 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 13:57:07` | `cowrie.session.connect` |
| `2026-09-04 13:57:08` | `cowrie.client.version` |
| `2026-09-04 13:57:08` | `cowrie.client.kex` |
| `2026-09-04 13:57:14` | `cowrie.login.success` |
| `2026-09-04 13:57:17` | `cowrie.session.params` |
| `2026-09-04 13:57:17` | `cowrie.command.input` |
| `2026-09-04 13:57:17` | `cowrie.command.input` |
| `2026-09-04 13:57:17` | `cowrie.command.input` |
| `2026-09-04 13:57:17` | `cowrie.command.input` |
| `2026-09-04 13:57:17` | `cowrie.command.input` |
| `2026-09-04 13:57:17` | `cowrie.command.success` |
| `2026-09-04 13:57:17` | `cowrie.command.input` |
| `2026-09-04 13:57:17` | `cowrie.command.input` |
| `2026-09-04 13:57:17` | `cowrie.command.input` |
| `2026-09-04 13:57:17` | `cowrie.command.input` |
| `2026-09-04 13:57:19` | `cowrie.log.closed` |
| `2026-09-04 13:57:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7df99b98fd38

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-09-04 13:58 |
| **Last Seen** | 2026-09-04 13:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 13:58:47` | `cowrie.session.connect` |
| `2026-09-04 13:58:47` | `cowrie.client.version` |
| `2026-09-04 13:58:47` | `cowrie.client.kex` |
| `2026-09-04 13:58:48` | `cowrie.login.success` |
| `2026-09-04 13:58:49` | `cowrie.session.params` |
| `2026-09-04 13:58:49` | `cowrie.command.input` |
| `2026-09-04 13:58:49` | `cowrie.log.closed` |
| `2026-09-04 13:58:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a22a9a24c832

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-09-04 13:59 |
| **Last Seen** | 2026-09-04 13:59 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 13:59:00` | `cowrie.session.connect` |
| `2026-09-04 13:59:01` | `cowrie.client.version` |
| `2026-09-04 13:59:01` | `cowrie.client.kex` |
| `2026-09-04 13:59:08` | `cowrie.login.success` |
| `2026-09-04 13:59:11` | `cowrie.session.params` |
| `2026-09-04 13:59:11` | `cowrie.command.input` |
| `2026-09-04 13:59:11` | `cowrie.command.input` |
| `2026-09-04 13:59:11` | `cowrie.command.input` |
| `2026-09-04 13:59:11` | `cowrie.command.input` |
| `2026-09-04 13:59:11` | `cowrie.command.input` |
| `2026-09-04 13:59:11` | `cowrie.command.success` |
| `2026-09-04 13:59:11` | `cowrie.command.input` |
| `2026-09-04 13:59:11` | `cowrie.command.input` |
| `2026-09-04 13:59:11` | `cowrie.command.input` |
| `2026-09-04 13:59:11` | `cowrie.command.input` |
| `2026-09-04 13:59:12` | `cowrie.log.closed` |
| `2026-09-04 13:59:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-62aba93cffe4

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-09-04 14:00 |
| **Last Seen** | 2026-09-04 14:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 14:00:35` | `cowrie.session.connect` |
| `2026-09-04 14:00:35` | `cowrie.client.version` |
| `2026-09-04 14:00:35` | `cowrie.client.kex` |
| `2026-09-04 14:00:35` | `cowrie.login.success` |
| `2026-09-04 14:00:36` | `cowrie.session.params` |
| `2026-09-04 14:00:36` | `cowrie.command.input` |
| `2026-09-04 14:00:36` | `cowrie.log.closed` |
| `2026-09-04 14:00:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-209feeb144dc

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-09-04 14:00 |
| **Last Seen** | 2026-09-04 14:01 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 14:00:47` | `cowrie.session.connect` |
| `2026-09-04 14:00:48` | `cowrie.client.version` |
| `2026-09-04 14:00:48` | `cowrie.client.kex` |
| `2026-09-04 14:00:54` | `cowrie.login.success` |
| `2026-09-04 14:00:58` | `cowrie.session.params` |
| `2026-09-04 14:00:58` | `cowrie.command.input` |
| `2026-09-04 14:00:58` | `cowrie.command.input` |
| `2026-09-04 14:00:58` | `cowrie.command.input` |
| `2026-09-04 14:00:58` | `cowrie.command.input` |
| `2026-09-04 14:00:58` | `cowrie.command.input` |
| `2026-09-04 14:00:58` | `cowrie.command.success` |
| `2026-09-04 14:00:58` | `cowrie.command.input` |
| `2026-09-04 14:00:58` | `cowrie.command.input` |
| `2026-09-04 14:00:58` | `cowrie.command.input` |
| `2026-09-04 14:00:58` | `cowrie.command.input` |
| `2026-09-04 14:00:59` | `cowrie.log.closed` |
| `2026-09-04 14:01:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cfde2e26856f

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-09-04 14:02 |
| **Last Seen** | 2026-09-04 14:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 14:02:20` | `cowrie.session.connect` |
| `2026-09-04 14:02:20` | `cowrie.client.version` |
| `2026-09-04 14:02:21` | `cowrie.client.kex` |
| `2026-09-04 14:02:21` | `cowrie.login.success` |
| `2026-09-04 14:02:21` | `cowrie.session.params` |
| `2026-09-04 14:02:21` | `cowrie.command.input` |
| `2026-09-04 14:02:22` | `cowrie.log.closed` |
| `2026-09-04 14:02:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4c8b43f960de

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-09-04 14:02 |
| **Last Seen** | 2026-09-04 14:02 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 14:02:34` | `cowrie.session.connect` |
| `2026-09-04 14:02:36` | `cowrie.client.version` |
| `2026-09-04 14:02:36` | `cowrie.client.kex` |
| `2026-09-04 14:02:42` | `cowrie.login.success` |
| `2026-09-04 14:02:45` | `cowrie.session.params` |
| `2026-09-04 14:02:45` | `cowrie.command.input` |
| `2026-09-04 14:02:45` | `cowrie.command.input` |
| `2026-09-04 14:02:45` | `cowrie.command.input` |
| `2026-09-04 14:02:45` | `cowrie.command.input` |
| `2026-09-04 14:02:45` | `cowrie.command.input` |
| `2026-09-04 14:02:45` | `cowrie.command.success` |
| `2026-09-04 14:02:45` | `cowrie.command.input` |
| `2026-09-04 14:02:45` | `cowrie.command.input` |
| `2026-09-04 14:02:45` | `cowrie.command.input` |
| `2026-09-04 14:02:45` | `cowrie.command.input` |
| `2026-09-04 14:02:46` | `cowrie.log.closed` |
| `2026-09-04 14:02:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c5d82e20dcc5

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-09-04 14:04 |
| **Last Seen** | 2026-09-04 14:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 14:04:02` | `cowrie.session.connect` |
| `2026-09-04 14:04:02` | `cowrie.client.version` |
| `2026-09-04 14:04:02` | `cowrie.client.kex` |
| `2026-09-04 14:04:03` | `cowrie.login.success` |
| `2026-09-04 14:04:04` | `cowrie.session.params` |
| `2026-09-04 14:04:04` | `cowrie.command.input` |
| `2026-09-04 14:04:04` | `cowrie.log.closed` |
| `2026-09-04 14:04:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-52c4232197c9

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-09-04 14:04 |
| **Last Seen** | 2026-09-04 14:04 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 14:04:22` | `cowrie.session.connect` |
| `2026-09-04 14:04:23` | `cowrie.client.version` |
| `2026-09-04 14:04:23` | `cowrie.client.kex` |
| `2026-09-04 14:04:29` | `cowrie.login.success` |
| `2026-09-04 14:04:31` | `cowrie.session.params` |
| `2026-09-04 14:04:31` | `cowrie.command.input` |
| `2026-09-04 14:04:31` | `cowrie.command.input` |
| `2026-09-04 14:04:31` | `cowrie.command.input` |
| `2026-09-04 14:04:31` | `cowrie.command.input` |
| `2026-09-04 14:04:31` | `cowrie.command.input` |
| `2026-09-04 14:04:31` | `cowrie.command.success` |
| `2026-09-04 14:04:31` | `cowrie.command.input` |
| `2026-09-04 14:04:31` | `cowrie.command.input` |
| `2026-09-04 14:04:31` | `cowrie.command.input` |
| `2026-09-04 14:04:31` | `cowrie.command.input` |
| `2026-09-04 14:04:33` | `cowrie.log.closed` |
| `2026-09-04 14:04:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3d093fd3841c

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-09-04 14:05 |
| **Last Seen** | 2026-09-04 14:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 14:05:48` | `cowrie.session.connect` |
| `2026-09-04 14:05:48` | `cowrie.client.version` |
| `2026-09-04 14:05:48` | `cowrie.client.kex` |
| `2026-09-04 14:05:48` | `cowrie.login.success` |
| `2026-09-04 14:05:49` | `cowrie.session.params` |
| `2026-09-04 14:05:49` | `cowrie.command.input` |
| `2026-09-04 14:05:49` | `cowrie.log.closed` |
| `2026-09-04 14:05:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6956c90da3d2

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-04 14:05 |
| **Last Seen** | 2026-09-04 14:05 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 14:05:57` | `cowrie.session.connect` |
| `2026-09-04 14:05:57` | `cowrie.client.version` |
| `2026-09-04 14:05:57` | `cowrie.client.kex` |
| `2026-09-04 14:05:59` | `cowrie.login.success` |
| `2026-09-04 14:05:59` | `cowrie.direct-tcpip.request` |
| `2026-09-04 14:05:59` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-04 14:05:59` | `cowrie.direct-tcpip.data` |
| `2026-09-04 14:05:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-475173097247

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-09-04 14:06 |
| **Last Seen** | 2026-09-04 14:06 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 14:06:09` | `cowrie.session.connect` |
| `2026-09-04 14:06:10` | `cowrie.client.version` |
| `2026-09-04 14:06:10` | `cowrie.client.kex` |
| `2026-09-04 14:06:16` | `cowrie.login.success` |
| `2026-09-04 14:06:18` | `cowrie.session.params` |
| `2026-09-04 14:06:18` | `cowrie.command.input` |
| `2026-09-04 14:06:18` | `cowrie.command.input` |
| `2026-09-04 14:06:18` | `cowrie.command.input` |
| `2026-09-04 14:06:18` | `cowrie.command.input` |
| `2026-09-04 14:06:18` | `cowrie.command.input` |
| `2026-09-04 14:06:18` | `cowrie.command.success` |
| `2026-09-04 14:06:18` | `cowrie.command.input` |
| `2026-09-04 14:06:18` | `cowrie.command.input` |
| `2026-09-04 14:06:18` | `cowrie.command.input` |
| `2026-09-04 14:06:18` | `cowrie.command.input` |
| `2026-09-04 14:06:19` | `cowrie.log.closed` |
| `2026-09-04 14:06:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f9f49c97d839

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-09-04 14:07 |
| **Last Seen** | 2026-09-04 14:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 14:07:37` | `cowrie.session.connect` |
| `2026-09-04 14:07:37` | `cowrie.client.version` |
| `2026-09-04 14:07:37` | `cowrie.client.kex` |
| `2026-09-04 14:07:37` | `cowrie.login.success` |
| `2026-09-04 14:07:38` | `cowrie.session.params` |
| `2026-09-04 14:07:38` | `cowrie.command.input` |
| `2026-09-04 14:07:38` | `cowrie.log.closed` |
| `2026-09-04 14:07:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2614375a4295

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-09-04 14:07 |
| **Last Seen** | 2026-09-04 14:08 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 14:07:52` | `cowrie.session.connect` |
| `2026-09-04 14:07:53` | `cowrie.client.version` |
| `2026-09-04 14:07:53` | `cowrie.client.kex` |
| `2026-09-04 14:07:58` | `cowrie.login.success` |
| `2026-09-04 14:08:01` | `cowrie.session.params` |
| `2026-09-04 14:08:01` | `cowrie.command.input` |
| `2026-09-04 14:08:01` | `cowrie.command.input` |
| `2026-09-04 14:08:01` | `cowrie.command.input` |
| `2026-09-04 14:08:01` | `cowrie.command.input` |
| `2026-09-04 14:08:01` | `cowrie.command.input` |
| `2026-09-04 14:08:01` | `cowrie.command.success` |
| `2026-09-04 14:08:01` | `cowrie.command.input` |
| `2026-09-04 14:08:01` | `cowrie.command.input` |
| `2026-09-04 14:08:01` | `cowrie.command.input` |
| `2026-09-04 14:08:01` | `cowrie.command.input` |
| `2026-09-04 14:08:02` | `cowrie.log.closed` |
| `2026-09-04 14:08:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-77e360535427

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-09-04 14:09 |
| **Last Seen** | 2026-09-04 14:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 14:09:23` | `cowrie.session.connect` |
| `2026-09-04 14:09:23` | `cowrie.client.version` |
| `2026-09-04 14:09:23` | `cowrie.client.kex` |
| `2026-09-04 14:09:23` | `cowrie.login.success` |
| `2026-09-04 14:09:24` | `cowrie.session.params` |
| `2026-09-04 14:09:24` | `cowrie.command.input` |
| `2026-09-04 14:09:24` | `cowrie.log.closed` |
| `2026-09-04 14:09:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a4c51d37887c

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-09-04 14:09 |
| **Last Seen** | 2026-09-04 14:09 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 14:09:38` | `cowrie.session.connect` |
| `2026-09-04 14:09:39` | `cowrie.client.version` |
| `2026-09-04 14:09:39` | `cowrie.client.kex` |
| `2026-09-04 14:09:44` | `cowrie.login.success` |
| `2026-09-04 14:09:47` | `cowrie.session.params` |
| `2026-09-04 14:09:47` | `cowrie.command.input` |
| `2026-09-04 14:09:47` | `cowrie.command.input` |
| `2026-09-04 14:09:47` | `cowrie.command.input` |
| `2026-09-04 14:09:47` | `cowrie.command.input` |
| `2026-09-04 14:09:47` | `cowrie.command.input` |
| `2026-09-04 14:09:47` | `cowrie.command.success` |
| `2026-09-04 14:09:47` | `cowrie.command.input` |
| `2026-09-04 14:09:47` | `cowrie.command.input` |
| `2026-09-04 14:09:47` | `cowrie.command.input` |
| `2026-09-04 14:09:47` | `cowrie.command.input` |
| `2026-09-04 14:09:49` | `cowrie.log.closed` |
| `2026-09-04 14:09:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c95077c07457

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-09-04 14:11 |
| **Last Seen** | 2026-09-04 14:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 14:11:07` | `cowrie.session.connect` |
| `2026-09-04 14:11:07` | `cowrie.client.version` |
| `2026-09-04 14:11:07` | `cowrie.client.kex` |
| `2026-09-04 14:11:07` | `cowrie.login.success` |
| `2026-09-04 14:11:08` | `cowrie.session.params` |
| `2026-09-04 14:11:08` | `cowrie.command.input` |
| `2026-09-04 14:11:08` | `cowrie.log.closed` |
| `2026-09-04 14:11:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7da0db5b42fd

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-09-04 14:11 |
| **Last Seen** | 2026-09-04 14:11 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 14:11:24` | `cowrie.session.connect` |
| `2026-09-04 14:11:25` | `cowrie.client.version` |
| `2026-09-04 14:11:25` | `cowrie.client.kex` |
| `2026-09-04 14:11:31` | `cowrie.login.success` |
| `2026-09-04 14:11:33` | `cowrie.session.params` |
| `2026-09-04 14:11:33` | `cowrie.command.input` |
| `2026-09-04 14:11:33` | `cowrie.command.input` |
| `2026-09-04 14:11:33` | `cowrie.command.input` |
| `2026-09-04 14:11:33` | `cowrie.command.input` |
| `2026-09-04 14:11:33` | `cowrie.command.input` |
| `2026-09-04 14:11:33` | `cowrie.command.success` |
| `2026-09-04 14:11:33` | `cowrie.command.input` |
| `2026-09-04 14:11:33` | `cowrie.command.input` |
| `2026-09-04 14:11:33` | `cowrie.command.input` |
| `2026-09-04 14:11:33` | `cowrie.command.input` |
| `2026-09-04 14:11:34` | `cowrie.log.closed` |
| `2026-09-04 14:11:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-90ab4ddbd922

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-09-04 14:12 |
| **Last Seen** | 2026-09-04 14:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 14:12:55` | `cowrie.session.connect` |
| `2026-09-04 14:12:55` | `cowrie.client.version` |
| `2026-09-04 14:12:55` | `cowrie.client.kex` |
| `2026-09-04 14:12:55` | `cowrie.login.success` |
| `2026-09-04 14:12:56` | `cowrie.session.params` |
| `2026-09-04 14:12:56` | `cowrie.command.input` |
| `2026-09-04 14:12:56` | `cowrie.log.closed` |
| `2026-09-04 14:12:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6c6638575c3d

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-09-04 14:13 |
| **Last Seen** | 2026-09-04 14:13 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 14:13:09` | `cowrie.session.connect` |
| `2026-09-04 14:13:10` | `cowrie.client.version` |
| `2026-09-04 14:13:10` | `cowrie.client.kex` |
| `2026-09-04 14:13:15` | `cowrie.login.success` |
| `2026-09-04 14:13:18` | `cowrie.session.params` |
| `2026-09-04 14:13:18` | `cowrie.command.input` |
| `2026-09-04 14:13:18` | `cowrie.command.input` |
| `2026-09-04 14:13:18` | `cowrie.command.input` |
| `2026-09-04 14:13:18` | `cowrie.command.input` |
| `2026-09-04 14:13:18` | `cowrie.command.input` |
| `2026-09-04 14:13:18` | `cowrie.command.success` |
| `2026-09-04 14:13:18` | `cowrie.command.input` |
| `2026-09-04 14:13:18` | `cowrie.command.input` |
| `2026-09-04 14:13:18` | `cowrie.command.input` |
| `2026-09-04 14:13:18` | `cowrie.command.input` |
| `2026-09-04 14:13:20` | `cowrie.log.closed` |
| `2026-09-04 14:13:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-34a86c0defdf

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-09-04 14:14 |
| **Last Seen** | 2026-09-04 14:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 14:14:41` | `cowrie.session.connect` |
| `2026-09-04 14:14:41` | `cowrie.client.version` |
| `2026-09-04 14:14:41` | `cowrie.client.kex` |
| `2026-09-04 14:14:42` | `cowrie.login.success` |
| `2026-09-04 14:14:42` | `cowrie.session.params` |
| `2026-09-04 14:14:42` | `cowrie.command.input` |
| `2026-09-04 14:14:42` | `cowrie.log.closed` |
| `2026-09-04 14:14:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9c43da7eecf6

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-09-04 14:14 |
| **Last Seen** | 2026-09-04 14:15 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 14:14:54` | `cowrie.session.connect` |
| `2026-09-04 14:14:54` | `cowrie.client.version` |
| `2026-09-04 14:14:54` | `cowrie.client.kex` |
| `2026-09-04 14:14:59` | `cowrie.login.success` |
| `2026-09-04 14:15:02` | `cowrie.session.params` |
| `2026-09-04 14:15:02` | `cowrie.command.input` |
| `2026-09-04 14:15:02` | `cowrie.command.input` |
| `2026-09-04 14:15:02` | `cowrie.command.input` |
| `2026-09-04 14:15:02` | `cowrie.command.input` |
| `2026-09-04 14:15:02` | `cowrie.command.input` |
| `2026-09-04 14:15:02` | `cowrie.command.success` |
| `2026-09-04 14:15:02` | `cowrie.command.input` |
| `2026-09-04 14:15:02` | `cowrie.command.input` |
| `2026-09-04 14:15:02` | `cowrie.command.input` |
| `2026-09-04 14:15:02` | `cowrie.command.input` |
| `2026-09-04 14:15:03` | `cowrie.log.closed` |
| `2026-09-04 14:15:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-16dd8b82bd65

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-09-04 14:16 |
| **Last Seen** | 2026-09-04 14:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 14:16:23` | `cowrie.session.connect` |
| `2026-09-04 14:16:23` | `cowrie.client.version` |
| `2026-09-04 14:16:23` | `cowrie.client.kex` |
| `2026-09-04 14:16:24` | `cowrie.login.success` |
| `2026-09-04 14:16:25` | `cowrie.session.params` |
| `2026-09-04 14:16:25` | `cowrie.command.input` |
| `2026-09-04 14:16:25` | `cowrie.log.closed` |
| `2026-09-04 14:16:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-273868cb3d13

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-09-04 14:16 |
| **Last Seen** | 2026-09-04 14:16 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 14:16:43` | `cowrie.session.connect` |
| `2026-09-04 14:16:44` | `cowrie.client.version` |
| `2026-09-04 14:16:44` | `cowrie.client.kex` |
| `2026-09-04 14:16:49` | `cowrie.login.success` |
| `2026-09-04 14:16:52` | `cowrie.session.params` |
| `2026-09-04 14:16:52` | `cowrie.command.input` |
| `2026-09-04 14:16:52` | `cowrie.command.input` |
| `2026-09-04 14:16:52` | `cowrie.command.input` |
| `2026-09-04 14:16:52` | `cowrie.command.input` |
| `2026-09-04 14:16:52` | `cowrie.command.input` |
| `2026-09-04 14:16:52` | `cowrie.command.success` |
| `2026-09-04 14:16:52` | `cowrie.command.input` |
| `2026-09-04 14:16:52` | `cowrie.command.input` |
| `2026-09-04 14:16:52` | `cowrie.command.input` |
| `2026-09-04 14:16:52` | `cowrie.command.input` |
| `2026-09-04 14:16:53` | `cowrie.log.closed` |
| `2026-09-04 14:16:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f7bfdbcc28be

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-04 14:17 |
| **Last Seen** | 2026-09-04 14:17 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 14:17:19` | `cowrie.session.connect` |
| `2026-09-04 14:17:19` | `cowrie.client.version` |
| `2026-09-04 14:17:19` | `cowrie.client.kex` |
| `2026-09-04 14:17:21` | `cowrie.login.success` |
| `2026-09-04 14:17:21` | `cowrie.direct-tcpip.request` |
| `2026-09-04 14:17:21` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-04 14:17:21` | `cowrie.direct-tcpip.data` |
| `2026-09-04 14:17:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-88c75941c35d

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-09-04 14:18 |
| **Last Seen** | 2026-09-04 14:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 14:18:08` | `cowrie.session.connect` |
| `2026-09-04 14:18:08` | `cowrie.client.version` |
| `2026-09-04 14:18:08` | `cowrie.client.kex` |
| `2026-09-04 14:18:09` | `cowrie.login.success` |
| `2026-09-04 14:18:10` | `cowrie.session.params` |
| `2026-09-04 14:18:10` | `cowrie.command.input` |
| `2026-09-04 14:18:10` | `cowrie.log.closed` |
| `2026-09-04 14:18:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8b3c3b3c1fde

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-09-04 14:18 |
| **Last Seen** | 2026-09-04 14:18 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 14:18:29` | `cowrie.session.connect` |
| `2026-09-04 14:18:30` | `cowrie.client.version` |
| `2026-09-04 14:18:30` | `cowrie.client.kex` |
| `2026-09-04 14:18:35` | `cowrie.login.success` |
| `2026-09-04 14:18:38` | `cowrie.session.params` |
| `2026-09-04 14:18:38` | `cowrie.command.input` |
| `2026-09-04 14:18:38` | `cowrie.command.input` |
| `2026-09-04 14:18:38` | `cowrie.command.input` |
| `2026-09-04 14:18:38` | `cowrie.command.input` |
| `2026-09-04 14:18:38` | `cowrie.command.input` |
| `2026-09-04 14:18:38` | `cowrie.command.success` |
| `2026-09-04 14:18:38` | `cowrie.command.input` |
| `2026-09-04 14:18:38` | `cowrie.command.input` |
| `2026-09-04 14:18:38` | `cowrie.command.input` |
| `2026-09-04 14:18:38` | `cowrie.command.input` |
| `2026-09-04 14:18:39` | `cowrie.log.closed` |
| `2026-09-04 14:18:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5aa03d58b0b4

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-09-04 14:19 |
| **Last Seen** | 2026-09-04 14:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 14:19:56` | `cowrie.session.connect` |
| `2026-09-04 14:19:56` | `cowrie.client.version` |
| `2026-09-04 14:19:56` | `cowrie.client.kex` |
| `2026-09-04 14:19:56` | `cowrie.login.success` |
| `2026-09-04 14:19:57` | `cowrie.session.params` |
| `2026-09-04 14:19:57` | `cowrie.command.input` |
| `2026-09-04 14:19:57` | `cowrie.log.closed` |
| `2026-09-04 14:19:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b6c5c6087371

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-09-04 14:21 |
| **Last Seen** | 2026-09-04 14:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 14:21:42` | `cowrie.session.connect` |
| `2026-09-04 14:21:42` | `cowrie.client.version` |
| `2026-09-04 14:21:42` | `cowrie.client.kex` |
| `2026-09-04 14:21:42` | `cowrie.login.success` |
| `2026-09-04 14:21:43` | `cowrie.session.params` |
| `2026-09-04 14:21:43` | `cowrie.command.input` |
| `2026-09-04 14:21:43` | `cowrie.log.closed` |
| `2026-09-04 14:21:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-490af672be9e

| Field | Detail |
|---|---|
| **Source IP** | `138.226.239[.]233` |
| **First Seen** | 2026-09-04 14:22 |
| **Last Seen** | 2026-09-04 14:22 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 14:22:02` | `cowrie.session.connect` |
| `2026-09-04 14:22:06` | `cowrie.client.version` |
| `2026-09-04 14:22:06` | `cowrie.client.kex` |
| `2026-09-04 14:22:07` | `cowrie.login.success` |
| `2026-09-04 14:22:07` | `cowrie.direct-tcpip.request` |
| `2026-09-04 14:22:08` | `cowrie.direct-tcpip.data` |
| `2026-09-04 14:22:08` | `cowrie.direct-tcpip.request` |
| `2026-09-04 14:22:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.226.239[.]233` to AbuseIPDB if not already reported
- [ ] Block `138.226.239[.]233` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8d4421f2f65a

| Field | Detail |
|---|---|
| **Source IP** | `80.94.95[.]116` |
| **First Seen** | 2026-09-04 14:22 |
| **Last Seen** | 2026-09-04 14:22 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 14:22:50` | `cowrie.session.connect` |
| `2026-09-04 14:22:52` | `cowrie.client.version` |
| `2026-09-04 14:22:52` | `cowrie.client.kex` |
| `2026-09-04 14:22:53` | `cowrie.login.success` |
| `2026-09-04 14:22:53` | `cowrie.direct-tcpip.request` |
| `2026-09-04 14:22:54` | `cowrie.direct-tcpip.data` |
| `2026-09-04 14:22:54` | `cowrie.direct-tcpip.request` |
| `2026-09-04 14:22:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.95[.]116` to AbuseIPDB if not already reported
- [ ] Block `80.94.95[.]116` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d799c6ea2b20

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-09-04 14:23 |
| **Last Seen** | 2026-09-04 14:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 14:23:26` | `cowrie.session.connect` |
| `2026-09-04 14:23:26` | `cowrie.client.version` |
| `2026-09-04 14:23:26` | `cowrie.client.kex` |
| `2026-09-04 14:23:27` | `cowrie.login.success` |
| `2026-09-04 14:23:27` | `cowrie.session.params` |
| `2026-09-04 14:23:27` | `cowrie.command.input` |
| `2026-09-04 14:23:27` | `cowrie.log.closed` |
| `2026-09-04 14:23:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cc322bbd5449

| Field | Detail |
|---|---|
| **Source IP** | `212.64.201[.]210` |
| **First Seen** | 2026-09-04 14:23 |
| **Last Seen** | 2026-09-04 14:23 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 14:23:32` | `cowrie.session.connect` |
| `2026-09-04 14:23:32` | `cowrie.client.version` |
| `2026-09-04 14:23:32` | `cowrie.client.kex` |
| `2026-09-04 14:23:32` | `cowrie.login.success` |
| `2026-09-04 14:23:33` | `cowrie.session.params` |
| `2026-09-04 14:23:33` | `cowrie.command.input` |
| `2026-09-04 14:23:33` | `cowrie.command.failed` |
| `2026-09-04 14:23:34` | `cowrie.log.closed` |
| `2026-09-04 14:23:34` | `cowrie.session.params` |
| `2026-09-04 14:23:34` | `cowrie.command.input` |
| `2026-09-04 14:23:34` | `cowrie.session.file_download` |
| `2026-09-04 14:23:34` | `cowrie.log.closed` |
| `2026-09-04 14:23:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `212.64.201[.]210` to AbuseIPDB if not already reported
- [ ] Block `212.64.201[.]210` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4a811c4275c6

| Field | Detail |
|---|---|
| **Source IP** | `212.64.201[.]210` |
| **First Seen** | 2026-09-04 14:23 |
| **Last Seen** | 2026-09-04 14:23 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 14:23:34` | `cowrie.session.connect` |
| `2026-09-04 14:23:34` | `cowrie.client.version` |
| `2026-09-04 14:23:35` | `cowrie.client.kex` |
| `2026-09-04 14:23:35` | `cowrie.login.success` |
| `2026-09-04 14:23:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `212.64.201[.]210` to AbuseIPDB if not already reported
- [ ] Block `212.64.201[.]210` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a771f08048a7

| Field | Detail |
|---|---|
| **Source IP** | `212.64.201[.]210` |
| **First Seen** | 2026-09-04 14:23 |
| **Last Seen** | 2026-09-04 14:23 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 14:23:35` | `cowrie.session.connect` |
| `2026-09-04 14:23:35` | `cowrie.client.version` |
| `2026-09-04 14:23:36` | `cowrie.client.kex` |
| `2026-09-04 14:23:36` | `cowrie.login.success` |
| `2026-09-04 14:23:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `212.64.201[.]210` to AbuseIPDB if not already reported
- [ ] Block `212.64.201[.]210` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ccdda26a9e54

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-09-04 14:25 |
| **Last Seen** | 2026-09-04 14:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 14:25:16` | `cowrie.session.connect` |
| `2026-09-04 14:25:16` | `cowrie.client.version` |
| `2026-09-04 14:25:16` | `cowrie.client.kex` |
| `2026-09-04 14:25:16` | `cowrie.login.success` |
| `2026-09-04 14:25:17` | `cowrie.session.params` |
| `2026-09-04 14:25:17` | `cowrie.command.input` |
| `2026-09-04 14:25:17` | `cowrie.log.closed` |
| `2026-09-04 14:25:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eae94beffaec

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-09-04 14:27 |
| **Last Seen** | 2026-09-04 14:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 14:27:06` | `cowrie.session.connect` |
| `2026-09-04 14:27:06` | `cowrie.client.version` |
| `2026-09-04 14:27:06` | `cowrie.client.kex` |
| `2026-09-04 14:27:07` | `cowrie.login.success` |
| `2026-09-04 14:27:07` | `cowrie.session.params` |
| `2026-09-04 14:27:07` | `cowrie.command.input` |
| `2026-09-04 14:27:08` | `cowrie.log.closed` |
| `2026-09-04 14:27:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ddee917bbb77

| Field | Detail |
|---|---|
| **Source IP** | `103.76.120[.]90` |
| **First Seen** | 2026-09-04 14:27 |
| **Last Seen** | 2026-09-04 14:27 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 14:27:27` | `cowrie.session.connect` |
| `2026-09-04 14:27:27` | `cowrie.client.version` |
| `2026-09-04 14:27:27` | `cowrie.client.kex` |
| `2026-09-04 14:27:28` | `cowrie.login.success` |
| `2026-09-04 14:27:30` | `cowrie.session.params` |
| `2026-09-04 14:27:30` | `cowrie.command.input` |
| `2026-09-04 14:27:30` | `cowrie.command.failed` |
| `2026-09-04 14:27:30` | `cowrie.log.closed` |
| `2026-09-04 14:27:32` | `cowrie.session.params` |
| `2026-09-04 14:27:32` | `cowrie.command.input` |
| `2026-09-04 14:27:32` | `cowrie.session.file_download` |
| `2026-09-04 14:27:32` | `cowrie.log.closed` |
| `2026-09-04 14:27:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.76.120[.]90` to AbuseIPDB if not already reported
- [ ] Block `103.76.120[.]90` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9604c847eed8

| Field | Detail |
|---|---|
| **Source IP** | `103.76.120[.]90` |
| **First Seen** | 2026-09-04 14:27 |
| **Last Seen** | 2026-09-04 14:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 14:27:33` | `cowrie.session.connect` |
| `2026-09-04 14:27:33` | `cowrie.client.version` |
| `2026-09-04 14:27:33` | `cowrie.client.kex` |
| `2026-09-04 14:27:34` | `cowrie.login.success` |
| `2026-09-04 14:27:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.76.120[.]90` to AbuseIPDB if not already reported
- [ ] Block `103.76.120[.]90` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-296483ec2c0f

| Field | Detail |
|---|---|
| **Source IP** | `103.76.120[.]90` |
| **First Seen** | 2026-09-04 14:27 |
| **Last Seen** | 2026-09-04 14:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 14:27:35` | `cowrie.session.connect` |
| `2026-09-04 14:27:35` | `cowrie.client.version` |
| `2026-09-04 14:27:35` | `cowrie.client.kex` |
| `2026-09-04 14:27:36` | `cowrie.login.success` |
| `2026-09-04 14:27:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.76.120[.]90` to AbuseIPDB if not already reported
- [ ] Block `103.76.120[.]90` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a7c8a2ae0e38

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-09-04 14:28 |
| **Last Seen** | 2026-09-04 14:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 14:28:52` | `cowrie.session.connect` |
| `2026-09-04 14:28:52` | `cowrie.client.version` |
| `2026-09-04 14:28:52` | `cowrie.client.kex` |
| `2026-09-04 14:28:52` | `cowrie.login.success` |
| `2026-09-04 14:28:53` | `cowrie.session.params` |
| `2026-09-04 14:28:53` | `cowrie.command.input` |
| `2026-09-04 14:28:53` | `cowrie.log.closed` |
| `2026-09-04 14:28:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9a67df94742f

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-04 14:29 |
| **Last Seen** | 2026-09-04 14:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 14:29:17` | `cowrie.session.connect` |
| `2026-09-04 14:29:17` | `cowrie.client.version` |
| `2026-09-04 14:29:17` | `cowrie.client.kex` |
| `2026-09-04 14:29:18` | `cowrie.login.success` |
| `2026-09-04 14:29:18` | `cowrie.direct-tcpip.request` |
| `2026-09-04 14:29:19` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-04 14:29:19` | `cowrie.direct-tcpip.data` |
| `2026-09-04 14:29:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d54bd1f43ad1

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-09-04 14:30 |
| **Last Seen** | 2026-09-04 14:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 14:30:37` | `cowrie.session.connect` |
| `2026-09-04 14:30:37` | `cowrie.client.version` |
| `2026-09-04 14:30:37` | `cowrie.client.kex` |
| `2026-09-04 14:30:37` | `cowrie.login.success` |
| `2026-09-04 14:30:38` | `cowrie.session.params` |
| `2026-09-04 14:30:38` | `cowrie.command.input` |
| `2026-09-04 14:30:38` | `cowrie.log.closed` |
| `2026-09-04 14:30:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8b32aa52107a

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-09-04 14:32 |
| **Last Seen** | 2026-09-04 14:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 14:32:26` | `cowrie.session.connect` |
| `2026-09-04 14:32:26` | `cowrie.client.version` |
| `2026-09-04 14:32:26` | `cowrie.client.kex` |
| `2026-09-04 14:32:27` | `cowrie.login.success` |
| `2026-09-04 14:32:27` | `cowrie.session.params` |
| `2026-09-04 14:32:27` | `cowrie.command.input` |
| `2026-09-04 14:32:28` | `cowrie.log.closed` |
| `2026-09-04 14:32:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fa31aa907372

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-09-04 14:34 |
| **Last Seen** | 2026-09-04 14:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 14:34:13` | `cowrie.session.connect` |
| `2026-09-04 14:34:13` | `cowrie.client.version` |
| `2026-09-04 14:34:13` | `cowrie.client.kex` |
| `2026-09-04 14:34:14` | `cowrie.login.success` |
| `2026-09-04 14:34:14` | `cowrie.session.params` |
| `2026-09-04 14:34:14` | `cowrie.command.input` |
| `2026-09-04 14:34:14` | `cowrie.log.closed` |
| `2026-09-04 14:34:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fc2d0f284be5

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-09-04 14:35 |
| **Last Seen** | 2026-09-04 14:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 14:35:57` | `cowrie.session.connect` |
| `2026-09-04 14:35:57` | `cowrie.client.version` |
| `2026-09-04 14:35:58` | `cowrie.client.kex` |
| `2026-09-04 14:35:58` | `cowrie.login.success` |
| `2026-09-04 14:35:59` | `cowrie.session.params` |
| `2026-09-04 14:35:59` | `cowrie.command.input` |
| `2026-09-04 14:35:59` | `cowrie.log.closed` |
| `2026-09-04 14:35:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7dd9724902c8

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-09-04 14:37 |
| **Last Seen** | 2026-09-04 14:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 14:37:48` | `cowrie.session.connect` |
| `2026-09-04 14:37:48` | `cowrie.client.version` |
| `2026-09-04 14:37:48` | `cowrie.client.kex` |
| `2026-09-04 14:37:48` | `cowrie.login.success` |
| `2026-09-04 14:37:49` | `cowrie.session.params` |
| `2026-09-04 14:37:49` | `cowrie.command.input` |
| `2026-09-04 14:37:49` | `cowrie.log.closed` |
| `2026-09-04 14:37:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-edb596628f0d

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-09-04 14:39 |
| **Last Seen** | 2026-09-04 14:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 14:39:39` | `cowrie.session.connect` |
| `2026-09-04 14:39:39` | `cowrie.client.version` |
| `2026-09-04 14:39:39` | `cowrie.client.kex` |
| `2026-09-04 14:39:40` | `cowrie.login.success` |
| `2026-09-04 14:39:40` | `cowrie.session.params` |
| `2026-09-04 14:39:40` | `cowrie.command.input` |
| `2026-09-04 14:39:40` | `cowrie.log.closed` |
| `2026-09-04 14:39:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4847a11354ce

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-04 14:41 |
| **Last Seen** | 2026-09-04 14:41 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 14:41:12` | `cowrie.session.connect` |
| `2026-09-04 14:41:12` | `cowrie.client.version` |
| `2026-09-04 14:41:12` | `cowrie.client.kex` |
| `2026-09-04 14:41:14` | `cowrie.login.success` |
| `2026-09-04 14:41:15` | `cowrie.direct-tcpip.request` |
| `2026-09-04 14:41:15` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-04 14:41:15` | `cowrie.direct-tcpip.data` |
| `2026-09-04 14:41:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5ba4f683a427

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-09-04 14:41 |
| **Last Seen** | 2026-09-04 14:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 14:41:30` | `cowrie.session.connect` |
| `2026-09-04 14:41:30` | `cowrie.client.version` |
| `2026-09-04 14:41:30` | `cowrie.client.kex` |
| `2026-09-04 14:41:30` | `cowrie.login.success` |
| `2026-09-04 14:41:31` | `cowrie.session.params` |
| `2026-09-04 14:41:31` | `cowrie.command.input` |
| `2026-09-04 14:41:31` | `cowrie.log.closed` |
| `2026-09-04 14:41:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-23e279fb6fcd

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-09-04 14:43 |
| **Last Seen** | 2026-09-04 14:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 14:43:17` | `cowrie.session.connect` |
| `2026-09-04 14:43:17` | `cowrie.client.version` |
| `2026-09-04 14:43:17` | `cowrie.client.kex` |
| `2026-09-04 14:43:17` | `cowrie.login.success` |
| `2026-09-04 14:43:18` | `cowrie.session.params` |
| `2026-09-04 14:43:18` | `cowrie.command.input` |
| `2026-09-04 14:43:18` | `cowrie.log.closed` |
| `2026-09-04 14:43:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-23a232196ef4

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-09-04 14:45 |
| **Last Seen** | 2026-09-04 14:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 14:45:07` | `cowrie.session.connect` |
| `2026-09-04 14:45:07` | `cowrie.client.version` |
| `2026-09-04 14:45:08` | `cowrie.client.kex` |
| `2026-09-04 14:45:08` | `cowrie.login.success` |
| `2026-09-04 14:45:09` | `cowrie.session.params` |
| `2026-09-04 14:45:09` | `cowrie.command.input` |
| `2026-09-04 14:45:09` | `cowrie.log.closed` |
| `2026-09-04 14:45:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-894d76842d05

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-09-04 14:46 |
| **Last Seen** | 2026-09-04 14:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 14:46:54` | `cowrie.session.connect` |
| `2026-09-04 14:46:54` | `cowrie.client.version` |
| `2026-09-04 14:46:54` | `cowrie.client.kex` |
| `2026-09-04 14:46:54` | `cowrie.login.success` |
| `2026-09-04 14:46:55` | `cowrie.session.params` |
| `2026-09-04 14:46:55` | `cowrie.command.input` |
| `2026-09-04 14:46:55` | `cowrie.log.closed` |
| `2026-09-04 14:46:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7db0dcbaedcb

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-09-04 14:48 |
| **Last Seen** | 2026-09-04 14:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 14:48:37` | `cowrie.session.connect` |
| `2026-09-04 14:48:37` | `cowrie.client.version` |
| `2026-09-04 14:48:37` | `cowrie.client.kex` |
| `2026-09-04 14:48:38` | `cowrie.login.success` |
| `2026-09-04 14:48:38` | `cowrie.session.params` |
| `2026-09-04 14:48:38` | `cowrie.command.input` |
| `2026-09-04 14:48:38` | `cowrie.log.closed` |
| `2026-09-04 14:48:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-72bcf6f46ab1

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-09-04 14:50 |
| **Last Seen** | 2026-09-04 14:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 14:50:24` | `cowrie.session.connect` |
| `2026-09-04 14:50:24` | `cowrie.client.version` |
| `2026-09-04 14:50:25` | `cowrie.client.kex` |
| `2026-09-04 14:50:25` | `cowrie.login.success` |
| `2026-09-04 14:50:26` | `cowrie.session.params` |
| `2026-09-04 14:50:26` | `cowrie.command.input` |
| `2026-09-04 14:50:26` | `cowrie.log.closed` |
| `2026-09-04 14:50:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-758643564d54

| Field | Detail |
|---|---|
| **Source IP** | `92.52.184[.]245` |
| **First Seen** | 2026-09-04 14:51 |
| **Last Seen** | 2026-09-04 14:52 |
| **Session Duration** | 63s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `enable, system, shell, sh, /bin/busybox TOKEN` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 14:51:51` | `cowrie.session.connect` |
| `2026-09-04 14:51:52` | `cowrie.login.success` |
| `2026-09-04 14:51:52` | `cowrie.session.params` |
| `2026-09-04 14:51:53` | `cowrie.command.input` |
| `2026-09-04 14:51:53` | `cowrie.command.failed` |
| `2026-09-04 14:51:53` | `cowrie.command.input` |
| `2026-09-04 14:51:53` | `cowrie.command.failed` |
| `2026-09-04 14:51:53` | `cowrie.command.input` |
| `2026-09-04 14:51:53` | `cowrie.command.failed` |
| `2026-09-04 14:51:54` | `cowrie.command.input` |
| `2026-09-04 14:51:54` | `cowrie.command.input` |
| `2026-09-04 14:51:54` | `cowrie.command.input` |
| `2026-09-04 14:51:54` | `cowrie.command.success` |
| `2026-09-04 14:52:04` | `cowrie.session.file_download.failed` |
| `2026-09-04 14:52:14` | `cowrie.session.file_download.failed` |
| `2026-09-04 14:52:54` | `cowrie.log.closed` |
| `2026-09-04 14:52:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.52.184[.]245` to AbuseIPDB if not already reported
- [ ] Block `92.52.184[.]245` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-916e0be0cc96

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-09-04 14:52 |
| **Last Seen** | 2026-09-04 14:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 14:52:17` | `cowrie.session.connect` |
| `2026-09-04 14:52:17` | `cowrie.client.version` |
| `2026-09-04 14:52:17` | `cowrie.client.kex` |
| `2026-09-04 14:52:18` | `cowrie.login.success` |
| `2026-09-04 14:52:18` | `cowrie.session.params` |
| `2026-09-04 14:52:18` | `cowrie.command.input` |
| `2026-09-04 14:52:18` | `cowrie.log.closed` |
| `2026-09-04 14:52:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e7d21c73d3ef

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-04 14:52 |
| **Last Seen** | 2026-09-04 14:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 14:52:32` | `cowrie.session.connect` |
| `2026-09-04 14:52:32` | `cowrie.client.version` |
| `2026-09-04 14:52:33` | `cowrie.client.kex` |
| `2026-09-04 14:52:33` | `cowrie.login.success` |
| `2026-09-04 14:52:34` | `cowrie.direct-tcpip.request` |
| `2026-09-04 14:52:34` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-04 14:52:34` | `cowrie.direct-tcpip.data` |
| `2026-09-04 14:52:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-789f6d7b8373

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-09-04 14:54 |
| **Last Seen** | 2026-09-04 14:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 14:54:07` | `cowrie.session.connect` |
| `2026-09-04 14:54:07` | `cowrie.client.version` |
| `2026-09-04 14:54:07` | `cowrie.client.kex` |
| `2026-09-04 14:54:07` | `cowrie.login.success` |
| `2026-09-04 14:54:08` | `cowrie.session.params` |
| `2026-09-04 14:54:08` | `cowrie.command.input` |
| `2026-09-04 14:54:08` | `cowrie.log.closed` |
| `2026-09-04 14:54:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a7c897552590

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-09-04 14:55 |
| **Last Seen** | 2026-09-04 14:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 14:55:56` | `cowrie.session.connect` |
| `2026-09-04 14:55:56` | `cowrie.client.version` |
| `2026-09-04 14:55:56` | `cowrie.client.kex` |
| `2026-09-04 14:55:57` | `cowrie.login.success` |
| `2026-09-04 14:55:58` | `cowrie.session.params` |
| `2026-09-04 14:55:58` | `cowrie.command.input` |
| `2026-09-04 14:55:58` | `cowrie.log.closed` |
| `2026-09-04 14:55:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2a97c141aed7

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-09-04 14:57 |
| **Last Seen** | 2026-09-04 14:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 14:57:48` | `cowrie.session.connect` |
| `2026-09-04 14:57:48` | `cowrie.client.version` |
| `2026-09-04 14:57:48` | `cowrie.client.kex` |
| `2026-09-04 14:57:48` | `cowrie.login.success` |
| `2026-09-04 14:57:49` | `cowrie.session.params` |
| `2026-09-04 14:57:49` | `cowrie.command.input` |
| `2026-09-04 14:57:49` | `cowrie.log.closed` |
| `2026-09-04 14:57:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bb3736d4ebf8

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-09-04 14:59 |
| **Last Seen** | 2026-09-04 14:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 14:59:38` | `cowrie.session.connect` |
| `2026-09-04 14:59:38` | `cowrie.client.version` |
| `2026-09-04 14:59:38` | `cowrie.client.kex` |
| `2026-09-04 14:59:38` | `cowrie.login.success` |
| `2026-09-04 14:59:39` | `cowrie.session.params` |
| `2026-09-04 14:59:39` | `cowrie.command.input` |
| `2026-09-04 14:59:39` | `cowrie.log.closed` |
| `2026-09-04 14:59:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-242008cf6356

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-09-04 15:01 |
| **Last Seen** | 2026-09-04 15:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 15:01:23` | `cowrie.session.connect` |
| `2026-09-04 15:01:23` | `cowrie.client.version` |
| `2026-09-04 15:01:23` | `cowrie.client.kex` |
| `2026-09-04 15:01:23` | `cowrie.login.success` |
| `2026-09-04 15:01:24` | `cowrie.session.params` |
| `2026-09-04 15:01:24` | `cowrie.command.input` |
| `2026-09-04 15:01:24` | `cowrie.log.closed` |
| `2026-09-04 15:01:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bc248f17d2e5

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-09-04 15:03 |
| **Last Seen** | 2026-09-04 15:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 15:03:11` | `cowrie.session.connect` |
| `2026-09-04 15:03:11` | `cowrie.client.version` |
| `2026-09-04 15:03:11` | `cowrie.client.kex` |
| `2026-09-04 15:03:11` | `cowrie.login.success` |
| `2026-09-04 15:03:12` | `cowrie.session.params` |
| `2026-09-04 15:03:12` | `cowrie.command.input` |
| `2026-09-04 15:03:12` | `cowrie.log.closed` |
| `2026-09-04 15:03:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d16901fe7c20

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-04 15:03 |
| **Last Seen** | 2026-09-04 15:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 15:03:36` | `cowrie.session.connect` |
| `2026-09-04 15:03:36` | `cowrie.client.version` |
| `2026-09-04 15:03:36` | `cowrie.client.kex` |
| `2026-09-04 15:03:37` | `cowrie.login.success` |
| `2026-09-04 15:03:37` | `cowrie.direct-tcpip.request` |
| `2026-09-04 15:03:38` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-04 15:03:38` | `cowrie.direct-tcpip.data` |
| `2026-09-04 15:03:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-91757d23b5bc

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-09-04 15:05 |
| **Last Seen** | 2026-09-04 15:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 15:05:01` | `cowrie.session.connect` |
| `2026-09-04 15:05:01` | `cowrie.client.version` |
| `2026-09-04 15:05:01` | `cowrie.client.kex` |
| `2026-09-04 15:05:01` | `cowrie.login.success` |
| `2026-09-04 15:05:02` | `cowrie.session.params` |
| `2026-09-04 15:05:02` | `cowrie.command.input` |
| `2026-09-04 15:05:02` | `cowrie.log.closed` |
| `2026-09-04 15:05:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aff38b3abf70

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-09-04 15:06 |
| **Last Seen** | 2026-09-04 15:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 15:06:51` | `cowrie.session.connect` |
| `2026-09-04 15:06:51` | `cowrie.client.version` |
| `2026-09-04 15:06:51` | `cowrie.client.kex` |
| `2026-09-04 15:06:51` | `cowrie.login.success` |
| `2026-09-04 15:06:52` | `cowrie.session.params` |
| `2026-09-04 15:06:52` | `cowrie.command.input` |
| `2026-09-04 15:06:52` | `cowrie.log.closed` |
| `2026-09-04 15:06:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-767678f69fa3

| Field | Detail |
|---|---|
| **Source IP** | `2.29.16[.]86` |
| **First Seen** | 2026-09-04 15:07 |
| **Last Seen** | 2026-09-04 15:08 |
| **Session Duration** | 61s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `id, cat /etc/passwd, echo -e "\x61\x75\x74\x68\x5F\x6F\x6B\x0A", enable, system` |
| **TTPs (MITRE)** | T1003.008 · T1021.004 · T1059.004 · T1078 · T1083 · T1105 · T1222.002 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 15:07:23` | `cowrie.session.connect` |
| `2026-09-04 15:07:23` | `cowrie.telnet.option` |
| `2026-09-04 15:07:23` | `cowrie.telnet.option` |
| `2026-09-04 15:07:23` | `cowrie.login.success` |
| `2026-09-04 15:07:24` | `cowrie.session.params` |
| `2026-09-04 15:07:24` | `cowrie.telnet.option` |
| `2026-09-04 15:07:24` | `cowrie.telnet.option` |
| `2026-09-04 15:07:24` | `cowrie.command.input` |
| `2026-09-04 15:07:24` | `cowrie.command.input` |
| `2026-09-04 15:07:24` | `cowrie.command.input` |
| `2026-09-04 15:07:24` | `cowrie.command.input` |
| `2026-09-04 15:07:24` | `cowrie.command.failed` |
| `2026-09-04 15:07:24` | `cowrie.command.input` |
| `2026-09-04 15:07:24` | `cowrie.command.failed` |
| `2026-09-04 15:07:24` | `cowrie.command.input` |
| `2026-09-04 15:07:24` | `cowrie.command.failed` |
| `2026-09-04 15:07:24` | `cowrie.command.input` |
| `2026-09-04 15:07:24` | `cowrie.command.input` |
| `2026-09-04 15:07:24` | `cowrie.command.input` |
| `2026-09-04 15:07:24` | `cowrie.command.input` |
| `2026-09-04 15:07:24` | `cowrie.command.failed` |
| `2026-09-04 15:07:24` | `cowrie.command.input` |
| `2026-09-04 15:07:24` | `cowrie.command.failed` |
| `2026-09-04 15:07:24` | `cowrie.command.input` |
| `2026-09-04 15:07:24` | `cowrie.command.failed` |
| `2026-09-04 15:07:24` | `cowrie.command.input` |
| `2026-09-04 15:07:24` | `cowrie.command.failed` |
| `2026-09-04 15:07:24` | `cowrie.command.input` |
| `2026-09-04 15:07:24` | `cowrie.command.input` |
| `2026-09-04 15:07:24` | `cowrie.command.failed` |
| `2026-09-04 15:07:24` | `cowrie.command.input` |
| `2026-09-04 15:07:24` | `cowrie.command.input` |
| `2026-09-04 15:08:24` | `cowrie.log.closed` |
| `2026-09-04 15:08:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.29.16[.]86` to AbuseIPDB if not already reported
- [ ] Block `2.29.16[.]86` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b42691dd047d

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-09-04 15:08 |
| **Last Seen** | 2026-09-04 15:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 15:08:42` | `cowrie.session.connect` |
| `2026-09-04 15:08:42` | `cowrie.client.version` |
| `2026-09-04 15:08:42` | `cowrie.client.kex` |
| `2026-09-04 15:08:42` | `cowrie.login.success` |
| `2026-09-04 15:08:43` | `cowrie.session.params` |
| `2026-09-04 15:08:43` | `cowrie.command.input` |
| `2026-09-04 15:08:43` | `cowrie.log.closed` |
| `2026-09-04 15:08:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e1f3855eaec3

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-09-04 15:10 |
| **Last Seen** | 2026-09-04 15:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 15:10:35` | `cowrie.session.connect` |
| `2026-09-04 15:10:35` | `cowrie.client.version` |
| `2026-09-04 15:10:35` | `cowrie.client.kex` |
| `2026-09-04 15:10:36` | `cowrie.login.success` |
| `2026-09-04 15:10:36` | `cowrie.session.params` |
| `2026-09-04 15:10:36` | `cowrie.command.input` |
| `2026-09-04 15:10:36` | `cowrie.log.closed` |
| `2026-09-04 15:10:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-500d14909988

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-09-04 15:12 |
| **Last Seen** | 2026-09-04 15:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 15:12:25` | `cowrie.session.connect` |
| `2026-09-04 15:12:25` | `cowrie.client.version` |
| `2026-09-04 15:12:25` | `cowrie.client.kex` |
| `2026-09-04 15:12:26` | `cowrie.login.success` |
| `2026-09-04 15:12:26` | `cowrie.session.params` |
| `2026-09-04 15:12:26` | `cowrie.command.input` |
| `2026-09-04 15:12:26` | `cowrie.log.closed` |
| `2026-09-04 15:12:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2a6b3e3113ef

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-09-04 15:14 |
| **Last Seen** | 2026-09-04 15:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 15:14:11` | `cowrie.session.connect` |
| `2026-09-04 15:14:11` | `cowrie.client.version` |
| `2026-09-04 15:14:11` | `cowrie.client.kex` |
| `2026-09-04 15:14:11` | `cowrie.login.success` |
| `2026-09-04 15:14:12` | `cowrie.session.params` |
| `2026-09-04 15:14:12` | `cowrie.command.input` |
| `2026-09-04 15:14:12` | `cowrie.log.closed` |
| `2026-09-04 15:14:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6eb1fa061454

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-04 15:14 |
| **Last Seen** | 2026-09-04 15:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 15:14:41` | `cowrie.session.connect` |
| `2026-09-04 15:14:41` | `cowrie.client.version` |
| `2026-09-04 15:14:41` | `cowrie.client.kex` |
| `2026-09-04 15:14:42` | `cowrie.login.success` |
| `2026-09-04 15:14:42` | `cowrie.direct-tcpip.request` |
| `2026-09-04 15:14:43` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-04 15:14:43` | `cowrie.direct-tcpip.data` |
| `2026-09-04 15:14:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6a0834085414

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-09-04 15:16 |
| **Last Seen** | 2026-09-04 15:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 15:16:00` | `cowrie.session.connect` |
| `2026-09-04 15:16:00` | `cowrie.client.version` |
| `2026-09-04 15:16:00` | `cowrie.client.kex` |
| `2026-09-04 15:16:00` | `cowrie.login.success` |
| `2026-09-04 15:16:01` | `cowrie.session.params` |
| `2026-09-04 15:16:01` | `cowrie.command.input` |
| `2026-09-04 15:16:01` | `cowrie.log.closed` |
| `2026-09-04 15:16:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e18983a5a546

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-09-04 15:17 |
| **Last Seen** | 2026-09-04 15:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 15:17:51` | `cowrie.session.connect` |
| `2026-09-04 15:17:51` | `cowrie.client.version` |
| `2026-09-04 15:17:51` | `cowrie.client.kex` |
| `2026-09-04 15:17:51` | `cowrie.login.success` |
| `2026-09-04 15:17:52` | `cowrie.session.params` |
| `2026-09-04 15:17:52` | `cowrie.command.input` |
| `2026-09-04 15:17:52` | `cowrie.log.closed` |
| `2026-09-04 15:17:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-328a26622e50

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-09-04 15:23 |
| **Last Seen** | 2026-09-04 15:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 15:23:28` | `cowrie.session.connect` |
| `2026-09-04 15:23:28` | `cowrie.client.version` |
| `2026-09-04 15:23:28` | `cowrie.client.kex` |
| `2026-09-04 15:23:28` | `cowrie.login.success` |
| `2026-09-04 15:23:29` | `cowrie.session.params` |
| `2026-09-04 15:23:29` | `cowrie.command.input` |
| `2026-09-04 15:23:29` | `cowrie.log.closed` |
| `2026-09-04 15:23:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-711965d3b200

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-09-04 15:25 |
| **Last Seen** | 2026-09-04 15:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 15:25:23` | `cowrie.session.connect` |
| `2026-09-04 15:25:23` | `cowrie.client.version` |
| `2026-09-04 15:25:23` | `cowrie.client.kex` |
| `2026-09-04 15:25:23` | `cowrie.login.success` |
| `2026-09-04 15:25:24` | `cowrie.session.params` |
| `2026-09-04 15:25:24` | `cowrie.command.input` |
| `2026-09-04 15:25:24` | `cowrie.log.closed` |
| `2026-09-04 15:25:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dc555791adc1

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-04 15:25 |
| **Last Seen** | 2026-09-04 15:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 15:25:48` | `cowrie.session.connect` |
| `2026-09-04 15:25:48` | `cowrie.client.version` |
| `2026-09-04 15:25:48` | `cowrie.client.kex` |
| `2026-09-04 15:25:49` | `cowrie.login.success` |
| `2026-09-04 15:25:49` | `cowrie.direct-tcpip.request` |
| `2026-09-04 15:25:50` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-04 15:25:50` | `cowrie.direct-tcpip.data` |
| `2026-09-04 15:25:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3495ab4179f4

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-09-04 15:27 |
| **Last Seen** | 2026-09-04 15:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 15:27:16` | `cowrie.session.connect` |
| `2026-09-04 15:27:16` | `cowrie.client.version` |
| `2026-09-04 15:27:16` | `cowrie.client.kex` |
| `2026-09-04 15:27:16` | `cowrie.login.success` |
| `2026-09-04 15:27:17` | `cowrie.session.params` |
| `2026-09-04 15:27:17` | `cowrie.command.input` |
| `2026-09-04 15:27:17` | `cowrie.log.closed` |
| `2026-09-04 15:27:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ff97d340dfac

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-09-04 15:29 |
| **Last Seen** | 2026-09-04 15:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 15:29:11` | `cowrie.session.connect` |
| `2026-09-04 15:29:11` | `cowrie.client.version` |
| `2026-09-04 15:29:11` | `cowrie.client.kex` |
| `2026-09-04 15:29:11` | `cowrie.login.success` |
| `2026-09-04 15:29:12` | `cowrie.session.params` |
| `2026-09-04 15:29:12` | `cowrie.command.input` |
| `2026-09-04 15:29:12` | `cowrie.log.closed` |
| `2026-09-04 15:29:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-63b099037479

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-09-04 15:31 |
| **Last Seen** | 2026-09-04 15:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 15:31:04` | `cowrie.session.connect` |
| `2026-09-04 15:31:04` | `cowrie.client.version` |
| `2026-09-04 15:31:04` | `cowrie.client.kex` |
| `2026-09-04 15:31:05` | `cowrie.login.success` |
| `2026-09-04 15:31:05` | `cowrie.session.params` |
| `2026-09-04 15:31:05` | `cowrie.command.input` |
| `2026-09-04 15:31:06` | `cowrie.log.closed` |
| `2026-09-04 15:31:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b80c0ab6f909

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-09-04 15:32 |
| **Last Seen** | 2026-09-04 15:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 15:32:53` | `cowrie.session.connect` |
| `2026-09-04 15:32:53` | `cowrie.client.version` |
| `2026-09-04 15:32:54` | `cowrie.client.kex` |
| `2026-09-04 15:32:54` | `cowrie.login.success` |
| `2026-09-04 15:32:55` | `cowrie.session.params` |
| `2026-09-04 15:32:55` | `cowrie.command.input` |
| `2026-09-04 15:32:55` | `cowrie.log.closed` |
| `2026-09-04 15:32:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c4008e980c54

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-09-04 15:34 |
| **Last Seen** | 2026-09-04 15:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 15:34:45` | `cowrie.session.connect` |
| `2026-09-04 15:34:45` | `cowrie.client.version` |
| `2026-09-04 15:34:45` | `cowrie.client.kex` |
| `2026-09-04 15:34:46` | `cowrie.login.success` |
| `2026-09-04 15:34:46` | `cowrie.session.params` |
| `2026-09-04 15:34:46` | `cowrie.command.input` |
| `2026-09-04 15:34:46` | `cowrie.log.closed` |
| `2026-09-04 15:34:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8aa759f63f56

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-09-04 15:36 |
| **Last Seen** | 2026-09-04 15:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 15:36:39` | `cowrie.session.connect` |
| `2026-09-04 15:36:39` | `cowrie.client.version` |
| `2026-09-04 15:36:39` | `cowrie.client.kex` |
| `2026-09-04 15:36:39` | `cowrie.login.success` |
| `2026-09-04 15:36:40` | `cowrie.session.params` |
| `2026-09-04 15:36:40` | `cowrie.command.input` |
| `2026-09-04 15:36:40` | `cowrie.log.closed` |
| `2026-09-04 15:36:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-00a9f48c1871

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-04 15:36 |
| **Last Seen** | 2026-09-04 15:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 15:36:56` | `cowrie.session.connect` |
| `2026-09-04 15:36:56` | `cowrie.client.version` |
| `2026-09-04 15:36:56` | `cowrie.client.kex` |
| `2026-09-04 15:36:57` | `cowrie.login.success` |
| `2026-09-04 15:36:57` | `cowrie.direct-tcpip.request` |
| `2026-09-04 15:36:57` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-04 15:36:57` | `cowrie.direct-tcpip.data` |
| `2026-09-04 15:36:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bb69f67f2dea

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-09-04 15:38 |
| **Last Seen** | 2026-09-04 15:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 15:38:30` | `cowrie.session.connect` |
| `2026-09-04 15:38:30` | `cowrie.client.version` |
| `2026-09-04 15:38:30` | `cowrie.client.kex` |
| `2026-09-04 15:38:30` | `cowrie.login.success` |
| `2026-09-04 15:38:31` | `cowrie.session.params` |
| `2026-09-04 15:38:31` | `cowrie.command.input` |
| `2026-09-04 15:38:31` | `cowrie.log.closed` |
| `2026-09-04 15:38:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-06cb1136fa88

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-09-04 15:40 |
| **Last Seen** | 2026-09-04 15:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 15:40:21` | `cowrie.session.connect` |
| `2026-09-04 15:40:21` | `cowrie.client.version` |
| `2026-09-04 15:40:21` | `cowrie.client.kex` |
| `2026-09-04 15:40:21` | `cowrie.login.success` |
| `2026-09-04 15:40:22` | `cowrie.session.params` |
| `2026-09-04 15:40:22` | `cowrie.command.input` |
| `2026-09-04 15:40:22` | `cowrie.log.closed` |
| `2026-09-04 15:40:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2484d62b19ef

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-09-04 15:42 |
| **Last Seen** | 2026-09-04 15:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 15:42:19` | `cowrie.session.connect` |
| `2026-09-04 15:42:19` | `cowrie.client.version` |
| `2026-09-04 15:42:19` | `cowrie.client.kex` |
| `2026-09-04 15:42:19` | `cowrie.login.success` |
| `2026-09-04 15:42:20` | `cowrie.session.params` |
| `2026-09-04 15:42:20` | `cowrie.command.input` |
| `2026-09-04 15:42:20` | `cowrie.log.closed` |
| `2026-09-04 15:42:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4fdfa5ab8605

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-09-04 15:44 |
| **Last Seen** | 2026-09-04 15:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 15:44:15` | `cowrie.session.connect` |
| `2026-09-04 15:44:15` | `cowrie.client.version` |
| `2026-09-04 15:44:15` | `cowrie.client.kex` |
| `2026-09-04 15:44:15` | `cowrie.login.success` |
| `2026-09-04 15:44:16` | `cowrie.session.params` |
| `2026-09-04 15:44:16` | `cowrie.command.input` |
| `2026-09-04 15:44:16` | `cowrie.log.closed` |
| `2026-09-04 15:44:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ffe248cbf4a5

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-09-04 15:46 |
| **Last Seen** | 2026-09-04 15:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 15:46:09` | `cowrie.session.connect` |
| `2026-09-04 15:46:09` | `cowrie.client.version` |
| `2026-09-04 15:46:09` | `cowrie.client.kex` |
| `2026-09-04 15:46:09` | `cowrie.login.success` |
| `2026-09-04 15:46:10` | `cowrie.session.params` |
| `2026-09-04 15:46:10` | `cowrie.command.input` |
| `2026-09-04 15:46:10` | `cowrie.log.closed` |
| `2026-09-04 15:46:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-482379af83b2

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-04 15:47 |
| **Last Seen** | 2026-09-04 15:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 15:47:56` | `cowrie.session.connect` |
| `2026-09-04 15:47:56` | `cowrie.client.version` |
| `2026-09-04 15:47:56` | `cowrie.client.kex` |
| `2026-09-04 15:47:57` | `cowrie.login.success` |
| `2026-09-04 15:47:57` | `cowrie.direct-tcpip.request` |
| `2026-09-04 15:47:57` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-04 15:47:57` | `cowrie.direct-tcpip.data` |
| `2026-09-04 15:47:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7e7b1c4bc746

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-09-04 15:48 |
| **Last Seen** | 2026-09-04 15:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 15:48:07` | `cowrie.session.connect` |
| `2026-09-04 15:48:07` | `cowrie.client.version` |
| `2026-09-04 15:48:07` | `cowrie.client.kex` |
| `2026-09-04 15:48:07` | `cowrie.login.success` |
| `2026-09-04 15:48:08` | `cowrie.session.params` |
| `2026-09-04 15:48:08` | `cowrie.command.input` |
| `2026-09-04 15:48:08` | `cowrie.log.closed` |
| `2026-09-04 15:48:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fbd34a8fc08a

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-09-04 15:50 |
| **Last Seen** | 2026-09-04 15:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 15:50:03` | `cowrie.session.connect` |
| `2026-09-04 15:50:03` | `cowrie.client.version` |
| `2026-09-04 15:50:03` | `cowrie.client.kex` |
| `2026-09-04 15:50:04` | `cowrie.login.success` |
| `2026-09-04 15:50:04` | `cowrie.session.params` |
| `2026-09-04 15:50:04` | `cowrie.command.input` |
| `2026-09-04 15:50:04` | `cowrie.log.closed` |
| `2026-09-04 15:50:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-42ff050a7e79

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-09-04 15:51 |
| **Last Seen** | 2026-09-04 15:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 15:51:54` | `cowrie.session.connect` |
| `2026-09-04 15:51:54` | `cowrie.client.version` |
| `2026-09-04 15:51:54` | `cowrie.client.kex` |
| `2026-09-04 15:51:55` | `cowrie.login.success` |
| `2026-09-04 15:51:56` | `cowrie.session.params` |
| `2026-09-04 15:51:56` | `cowrie.command.input` |
| `2026-09-04 15:51:56` | `cowrie.log.closed` |
| `2026-09-04 15:51:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cab95517a874

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-09-04 15:53 |
| **Last Seen** | 2026-09-04 15:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 15:53:46` | `cowrie.session.connect` |
| `2026-09-04 15:53:46` | `cowrie.client.version` |
| `2026-09-04 15:53:46` | `cowrie.client.kex` |
| `2026-09-04 15:53:46` | `cowrie.login.success` |
| `2026-09-04 15:53:47` | `cowrie.session.params` |
| `2026-09-04 15:53:47` | `cowrie.command.input` |
| `2026-09-04 15:53:47` | `cowrie.log.closed` |
| `2026-09-04 15:53:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9a89fbb3ea0c

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-09-04 15:55 |
| **Last Seen** | 2026-09-04 15:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 15:55:41` | `cowrie.session.connect` |
| `2026-09-04 15:55:41` | `cowrie.client.version` |
| `2026-09-04 15:55:41` | `cowrie.client.kex` |
| `2026-09-04 15:55:41` | `cowrie.login.success` |
| `2026-09-04 15:55:42` | `cowrie.session.params` |
| `2026-09-04 15:55:42` | `cowrie.command.input` |
| `2026-09-04 15:55:42` | `cowrie.log.closed` |
| `2026-09-04 15:55:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ab22be42daf1

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]53` |
| **First Seen** | 2026-09-04 15:56 |
| **Last Seen** | 2026-09-04 15:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 15:56:14` | `cowrie.session.connect` |
| `2026-09-04 15:56:14` | `cowrie.client.version` |
| `2026-09-04 15:56:14` | `cowrie.client.kex` |
| `2026-09-04 15:56:15` | `cowrie.login.success` |
| `2026-09-04 15:56:16` | `cowrie.session.params` |
| `2026-09-04 15:56:16` | `cowrie.command.input` |
| `2026-09-04 15:56:16` | `cowrie.log.closed` |
| `2026-09-04 15:56:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]53` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-76036121457b

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-09-04 15:57 |
| **Last Seen** | 2026-09-04 15:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 15:57:32` | `cowrie.session.connect` |
| `2026-09-04 15:57:32` | `cowrie.client.version` |
| `2026-09-04 15:57:32` | `cowrie.client.kex` |
| `2026-09-04 15:57:33` | `cowrie.login.success` |
| `2026-09-04 15:57:33` | `cowrie.session.params` |
| `2026-09-04 15:57:33` | `cowrie.command.input` |
| `2026-09-04 15:57:33` | `cowrie.log.closed` |
| `2026-09-04 15:57:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-faddee54f762

| Field | Detail |
|---|---|
| **Source IP** | `181.228.80[.]171` |
| **First Seen** | 2026-09-04 15:58 |
| **Last Seen** | 2026-09-04 15:58 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 15:58:23` | `cowrie.session.connect` |
| `2026-09-04 15:58:23` | `cowrie.client.version` |
| `2026-09-04 15:58:23` | `cowrie.client.kex` |
| `2026-09-04 15:58:24` | `cowrie.login.success` |
| `2026-09-04 15:58:25` | `cowrie.session.params` |
| `2026-09-04 15:58:25` | `cowrie.command.input` |
| `2026-09-04 15:58:25` | `cowrie.command.failed` |
| `2026-09-04 15:58:25` | `cowrie.log.closed` |
| `2026-09-04 15:58:26` | `cowrie.session.params` |
| `2026-09-04 15:58:26` | `cowrie.command.input` |
| `2026-09-04 15:58:26` | `cowrie.session.file_download` |
| `2026-09-04 15:58:26` | `cowrie.log.closed` |
| `2026-09-04 15:58:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `181.228.80[.]171` to AbuseIPDB if not already reported
- [ ] Block `181.228.80[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-936aa149ac18

| Field | Detail |
|---|---|
| **Source IP** | `181.228.80[.]171` |
| **First Seen** | 2026-09-04 15:58 |
| **Last Seen** | 2026-09-04 15:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 15:58:26` | `cowrie.session.connect` |
| `2026-09-04 15:58:26` | `cowrie.client.version` |
| `2026-09-04 15:58:27` | `cowrie.client.kex` |
| `2026-09-04 15:58:27` | `cowrie.login.success` |
| `2026-09-04 15:58:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `181.228.80[.]171` to AbuseIPDB if not already reported
- [ ] Block `181.228.80[.]171` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a95c06d558a2

| Field | Detail |
|---|---|
| **Source IP** | `181.228.80[.]171` |
| **First Seen** | 2026-09-04 15:58 |
| **Last Seen** | 2026-09-04 15:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 15:58:28` | `cowrie.session.connect` |
| `2026-09-04 15:58:28` | `cowrie.client.version` |
| `2026-09-04 15:58:28` | `cowrie.client.kex` |
| `2026-09-04 15:58:28` | `cowrie.login.success` |
| `2026-09-04 15:58:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `181.228.80[.]171` to AbuseIPDB if not already reported
- [ ] Block `181.228.80[.]171` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cb9eef7e92c3

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]53` |
| **First Seen** | 2026-09-04 15:58 |
| **Last Seen** | 2026-09-04 15:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 15:58:30` | `cowrie.session.connect` |
| `2026-09-04 15:58:30` | `cowrie.client.version` |
| `2026-09-04 15:58:30` | `cowrie.client.kex` |
| `2026-09-04 15:58:31` | `cowrie.login.success` |
| `2026-09-04 15:58:32` | `cowrie.session.params` |
| `2026-09-04 15:58:32` | `cowrie.command.input` |
| `2026-09-04 15:58:32` | `cowrie.log.closed` |
| `2026-09-04 15:58:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]53` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a8ba409a9045

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-04 15:58 |
| **Last Seen** | 2026-09-04 15:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 15:58:57` | `cowrie.session.connect` |
| `2026-09-04 15:58:57` | `cowrie.client.version` |
| `2026-09-04 15:58:57` | `cowrie.client.kex` |
| `2026-09-04 15:58:58` | `cowrie.login.success` |
| `2026-09-04 15:58:58` | `cowrie.direct-tcpip.request` |
| `2026-09-04 15:58:58` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-04 15:58:58` | `cowrie.direct-tcpip.data` |
| `2026-09-04 15:58:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ff997ad53feb

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-09-04 15:59 |
| **Last Seen** | 2026-09-04 15:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 15:59:27` | `cowrie.session.connect` |
| `2026-09-04 15:59:27` | `cowrie.client.version` |
| `2026-09-04 15:59:27` | `cowrie.client.kex` |
| `2026-09-04 15:59:27` | `cowrie.login.success` |
| `2026-09-04 15:59:28` | `cowrie.session.params` |
| `2026-09-04 15:59:28` | `cowrie.command.input` |
| `2026-09-04 15:59:28` | `cowrie.log.closed` |
| `2026-09-04 15:59:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c78e4b54dc5f

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]53` |
| **First Seen** | 2026-09-04 16:00 |
| **Last Seen** | 2026-09-04 16:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 16:00:52` | `cowrie.session.connect` |
| `2026-09-04 16:00:52` | `cowrie.client.version` |
| `2026-09-04 16:00:52` | `cowrie.client.kex` |
| `2026-09-04 16:00:53` | `cowrie.login.success` |
| `2026-09-04 16:00:54` | `cowrie.session.params` |
| `2026-09-04 16:00:54` | `cowrie.command.input` |
| `2026-09-04 16:00:54` | `cowrie.log.closed` |
| `2026-09-04 16:00:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]53` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f51cb6c832d8

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-09-04 16:01 |
| **Last Seen** | 2026-09-04 16:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 16:01:28` | `cowrie.session.connect` |
| `2026-09-04 16:01:28` | `cowrie.client.version` |
| `2026-09-04 16:01:29` | `cowrie.client.kex` |
| `2026-09-04 16:01:29` | `cowrie.login.success` |
| `2026-09-04 16:01:29` | `cowrie.session.params` |
| `2026-09-04 16:01:29` | `cowrie.command.input` |
| `2026-09-04 16:01:30` | `cowrie.log.closed` |
| `2026-09-04 16:01:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a21b5d258ace

| Field | Detail |
|---|---|
| **Source IP** | `103.88.76[.]27` |
| **First Seen** | 2026-09-04 16:02 |
| **Last Seen** | 2026-09-04 16:02 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 16:02:31` | `cowrie.session.connect` |
| `2026-09-04 16:02:31` | `cowrie.client.version` |
| `2026-09-04 16:02:32` | `cowrie.client.kex` |
| `2026-09-04 16:02:33` | `cowrie.login.success` |
| `2026-09-04 16:02:34` | `cowrie.session.params` |
| `2026-09-04 16:02:34` | `cowrie.command.input` |
| `2026-09-04 16:02:34` | `cowrie.command.failed` |
| `2026-09-04 16:02:34` | `cowrie.log.closed` |
| `2026-09-04 16:02:35` | `cowrie.session.params` |
| `2026-09-04 16:02:35` | `cowrie.command.input` |
| `2026-09-04 16:02:36` | `cowrie.session.file_download` |
| `2026-09-04 16:02:36` | `cowrie.log.closed` |
| `2026-09-04 16:02:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.88.76[.]27` to AbuseIPDB if not already reported
- [ ] Block `103.88.76[.]27` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b3a498580520

| Field | Detail |
|---|---|
| **Source IP** | `103.88.76[.]27` |
| **First Seen** | 2026-09-04 16:02 |
| **Last Seen** | 2026-09-04 16:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 16:02:36` | `cowrie.session.connect` |
| `2026-09-04 16:02:36` | `cowrie.client.version` |
| `2026-09-04 16:02:36` | `cowrie.client.kex` |
| `2026-09-04 16:02:37` | `cowrie.login.success` |
| `2026-09-04 16:02:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.88.76[.]27` to AbuseIPDB if not already reported
- [ ] Block `103.88.76[.]27` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c3421910b065

| Field | Detail |
|---|---|
| **Source IP** | `103.88.76[.]27` |
| **First Seen** | 2026-09-04 16:02 |
| **Last Seen** | 2026-09-04 16:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 16:02:38` | `cowrie.session.connect` |
| `2026-09-04 16:02:38` | `cowrie.client.version` |
| `2026-09-04 16:02:38` | `cowrie.client.kex` |
| `2026-09-04 16:02:39` | `cowrie.login.success` |
| `2026-09-04 16:02:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.88.76[.]27` to AbuseIPDB if not already reported
- [ ] Block `103.88.76[.]27` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3c53d02dc90d

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]53` |
| **First Seen** | 2026-09-04 16:03 |
| **Last Seen** | 2026-09-04 16:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 16:03:11` | `cowrie.session.connect` |
| `2026-09-04 16:03:11` | `cowrie.client.version` |
| `2026-09-04 16:03:11` | `cowrie.client.kex` |
| `2026-09-04 16:03:11` | `cowrie.login.success` |
| `2026-09-04 16:03:12` | `cowrie.session.params` |
| `2026-09-04 16:03:12` | `cowrie.command.input` |
| `2026-09-04 16:03:12` | `cowrie.log.closed` |
| `2026-09-04 16:03:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]53` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-89b587f553ce

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-09-04 16:03 |
| **Last Seen** | 2026-09-04 16:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 16:03:29` | `cowrie.session.connect` |
| `2026-09-04 16:03:29` | `cowrie.client.version` |
| `2026-09-04 16:03:29` | `cowrie.client.kex` |
| `2026-09-04 16:03:29` | `cowrie.login.success` |
| `2026-09-04 16:03:30` | `cowrie.session.params` |
| `2026-09-04 16:03:30` | `cowrie.command.input` |
| `2026-09-04 16:03:30` | `cowrie.log.closed` |
| `2026-09-04 16:03:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5fa108df7156

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]53` |
| **First Seen** | 2026-09-04 16:05 |
| **Last Seen** | 2026-09-04 16:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 16:05:20` | `cowrie.session.connect` |
| `2026-09-04 16:05:20` | `cowrie.client.version` |
| `2026-09-04 16:05:20` | `cowrie.client.kex` |
| `2026-09-04 16:05:20` | `cowrie.login.success` |
| `2026-09-04 16:05:21` | `cowrie.session.params` |
| `2026-09-04 16:05:21` | `cowrie.command.input` |
| `2026-09-04 16:05:21` | `cowrie.log.closed` |
| `2026-09-04 16:05:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]53` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9b2550e2b5dd

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-09-04 16:05 |
| **Last Seen** | 2026-09-04 16:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 16:05:25` | `cowrie.session.connect` |
| `2026-09-04 16:05:25` | `cowrie.client.version` |
| `2026-09-04 16:05:26` | `cowrie.client.kex` |
| `2026-09-04 16:05:26` | `cowrie.login.success` |
| `2026-09-04 16:05:27` | `cowrie.session.params` |
| `2026-09-04 16:05:27` | `cowrie.command.input` |
| `2026-09-04 16:05:27` | `cowrie.log.closed` |
| `2026-09-04 16:05:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-338ccbcf67b0

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-09-04 16:07 |
| **Last Seen** | 2026-09-04 16:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 16:07:26` | `cowrie.session.connect` |
| `2026-09-04 16:07:26` | `cowrie.client.version` |
| `2026-09-04 16:07:26` | `cowrie.client.kex` |
| `2026-09-04 16:07:26` | `cowrie.login.success` |
| `2026-09-04 16:07:27` | `cowrie.session.params` |
| `2026-09-04 16:07:27` | `cowrie.command.input` |
| `2026-09-04 16:07:27` | `cowrie.log.closed` |
| `2026-09-04 16:07:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-555fff3b4645

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]53` |
| **First Seen** | 2026-09-04 16:07 |
| **Last Seen** | 2026-09-04 16:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 16:07:34` | `cowrie.session.connect` |
| `2026-09-04 16:07:34` | `cowrie.client.version` |
| `2026-09-04 16:07:34` | `cowrie.client.kex` |
| `2026-09-04 16:07:35` | `cowrie.login.success` |
| `2026-09-04 16:07:35` | `cowrie.session.params` |
| `2026-09-04 16:07:35` | `cowrie.command.input` |
| `2026-09-04 16:07:36` | `cowrie.log.closed` |
| `2026-09-04 16:07:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]53` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3c598e0e49e7

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-09-04 16:09 |
| **Last Seen** | 2026-09-04 16:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 16:09:23` | `cowrie.session.connect` |
| `2026-09-04 16:09:23` | `cowrie.client.version` |
| `2026-09-04 16:09:23` | `cowrie.client.kex` |
| `2026-09-04 16:09:24` | `cowrie.login.success` |
| `2026-09-04 16:09:24` | `cowrie.session.params` |
| `2026-09-04 16:09:24` | `cowrie.command.input` |
| `2026-09-04 16:09:25` | `cowrie.log.closed` |
| `2026-09-04 16:09:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8c10bd2ccb47

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]53` |
| **First Seen** | 2026-09-04 16:09 |
| **Last Seen** | 2026-09-04 16:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 16:09:49` | `cowrie.session.connect` |
| `2026-09-04 16:09:49` | `cowrie.client.version` |
| `2026-09-04 16:09:49` | `cowrie.client.kex` |
| `2026-09-04 16:09:49` | `cowrie.login.success` |
| `2026-09-04 16:09:50` | `cowrie.session.params` |
| `2026-09-04 16:09:50` | `cowrie.command.input` |
| `2026-09-04 16:09:50` | `cowrie.log.closed` |
| `2026-09-04 16:09:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]53` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-11d3dc33933c

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-04 16:10 |
| **Last Seen** | 2026-09-04 16:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 16:10:02` | `cowrie.session.connect` |
| `2026-09-04 16:10:02` | `cowrie.client.version` |
| `2026-09-04 16:10:02` | `cowrie.client.kex` |
| `2026-09-04 16:10:03` | `cowrie.login.success` |
| `2026-09-04 16:10:03` | `cowrie.direct-tcpip.request` |
| `2026-09-04 16:10:03` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-04 16:10:03` | `cowrie.direct-tcpip.data` |
| `2026-09-04 16:10:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-708dcfa74063

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-09-04 16:11 |
| **Last Seen** | 2026-09-04 16:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 16:11:16` | `cowrie.session.connect` |
| `2026-09-04 16:11:16` | `cowrie.client.version` |
| `2026-09-04 16:11:16` | `cowrie.client.kex` |
| `2026-09-04 16:11:16` | `cowrie.login.success` |
| `2026-09-04 16:11:17` | `cowrie.session.params` |
| `2026-09-04 16:11:17` | `cowrie.command.input` |
| `2026-09-04 16:11:17` | `cowrie.log.closed` |
| `2026-09-04 16:11:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cdae1e4b460a

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]53` |
| **First Seen** | 2026-09-04 16:12 |
| **Last Seen** | 2026-09-04 16:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 16:12:05` | `cowrie.session.connect` |
| `2026-09-04 16:12:05` | `cowrie.client.version` |
| `2026-09-04 16:12:05` | `cowrie.client.kex` |
| `2026-09-04 16:12:05` | `cowrie.login.success` |
| `2026-09-04 16:12:06` | `cowrie.session.params` |
| `2026-09-04 16:12:06` | `cowrie.command.input` |
| `2026-09-04 16:12:06` | `cowrie.log.closed` |
| `2026-09-04 16:12:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]53` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0dc40fd9ab62

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-09-04 16:13 |
| **Last Seen** | 2026-09-04 16:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 16:13:13` | `cowrie.session.connect` |
| `2026-09-04 16:13:13` | `cowrie.client.version` |
| `2026-09-04 16:13:13` | `cowrie.client.kex` |
| `2026-09-04 16:13:14` | `cowrie.login.success` |
| `2026-09-04 16:13:14` | `cowrie.session.params` |
| `2026-09-04 16:13:14` | `cowrie.command.input` |
| `2026-09-04 16:13:15` | `cowrie.log.closed` |
| `2026-09-04 16:13:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-247234a3171e

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]53` |
| **First Seen** | 2026-09-04 16:14 |
| **Last Seen** | 2026-09-04 16:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 16:14:40` | `cowrie.session.connect` |
| `2026-09-04 16:14:40` | `cowrie.client.version` |
| `2026-09-04 16:14:40` | `cowrie.client.kex` |
| `2026-09-04 16:14:40` | `cowrie.login.success` |
| `2026-09-04 16:14:41` | `cowrie.session.params` |
| `2026-09-04 16:14:41` | `cowrie.command.input` |
| `2026-09-04 16:14:42` | `cowrie.log.closed` |
| `2026-09-04 16:14:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]53` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7f87d6ff97f1

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-09-04 16:15 |
| **Last Seen** | 2026-09-04 16:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 16:15:11` | `cowrie.session.connect` |
| `2026-09-04 16:15:11` | `cowrie.client.version` |
| `2026-09-04 16:15:11` | `cowrie.client.kex` |
| `2026-09-04 16:15:11` | `cowrie.login.success` |
| `2026-09-04 16:15:12` | `cowrie.session.params` |
| `2026-09-04 16:15:12` | `cowrie.command.input` |
| `2026-09-04 16:15:12` | `cowrie.log.closed` |
| `2026-09-04 16:15:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4551ec99cc9a

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]53` |
| **First Seen** | 2026-09-04 16:17 |
| **Last Seen** | 2026-09-04 16:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 16:17:04` | `cowrie.session.connect` |
| `2026-09-04 16:17:04` | `cowrie.client.version` |
| `2026-09-04 16:17:04` | `cowrie.client.kex` |
| `2026-09-04 16:17:04` | `cowrie.login.success` |
| `2026-09-04 16:17:05` | `cowrie.session.params` |
| `2026-09-04 16:17:05` | `cowrie.command.input` |
| `2026-09-04 16:17:05` | `cowrie.log.closed` |
| `2026-09-04 16:17:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]53` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-901fe1d50bab

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-09-04 16:17 |
| **Last Seen** | 2026-09-04 16:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 16:17:06` | `cowrie.session.connect` |
| `2026-09-04 16:17:06` | `cowrie.client.version` |
| `2026-09-04 16:17:06` | `cowrie.client.kex` |
| `2026-09-04 16:17:06` | `cowrie.login.success` |
| `2026-09-04 16:17:07` | `cowrie.session.params` |
| `2026-09-04 16:17:07` | `cowrie.command.input` |
| `2026-09-04 16:17:07` | `cowrie.log.closed` |
| `2026-09-04 16:17:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d5554ce2fc65

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-09-04 16:19 |
| **Last Seen** | 2026-09-04 16:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 16:19:03` | `cowrie.session.connect` |
| `2026-09-04 16:19:03` | `cowrie.client.version` |
| `2026-09-04 16:19:03` | `cowrie.client.kex` |
| `2026-09-04 16:19:04` | `cowrie.login.success` |
| `2026-09-04 16:19:05` | `cowrie.session.params` |
| `2026-09-04 16:19:05` | `cowrie.command.input` |
| `2026-09-04 16:19:05` | `cowrie.log.closed` |
| `2026-09-04 16:19:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8613e9e877bf

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]53` |
| **First Seen** | 2026-09-04 16:19 |
| **Last Seen** | 2026-09-04 16:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 16:19:24` | `cowrie.session.connect` |
| `2026-09-04 16:19:24` | `cowrie.client.version` |
| `2026-09-04 16:19:24` | `cowrie.client.kex` |
| `2026-09-04 16:19:24` | `cowrie.login.success` |
| `2026-09-04 16:19:25` | `cowrie.session.params` |
| `2026-09-04 16:19:25` | `cowrie.command.input` |
| `2026-09-04 16:19:25` | `cowrie.log.closed` |
| `2026-09-04 16:19:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]53` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d4484e81b5c4

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-09-04 16:20 |
| **Last Seen** | 2026-09-04 16:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 16:20:11` | `cowrie.session.connect` |
| `2026-09-04 16:20:11` | `cowrie.client.version` |
| `2026-09-04 16:20:11` | `cowrie.client.kex` |
| `2026-09-04 16:20:12` | `cowrie.login.success` |
| `2026-09-04 16:20:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-805f6a5b08fe

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-09-04 16:20 |
| **Last Seen** | 2026-09-04 16:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 16:20:11` | `cowrie.session.connect` |
| `2026-09-04 16:20:11` | `cowrie.client.version` |
| `2026-09-04 16:20:12` | `cowrie.client.kex` |
| `2026-09-04 16:20:12` | `cowrie.login.success` |
| `2026-09-04 16:20:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-075b9a646072

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-09-04 16:21 |
| **Last Seen** | 2026-09-04 16:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 16:21:05` | `cowrie.session.connect` |
| `2026-09-04 16:21:05` | `cowrie.client.version` |
| `2026-09-04 16:21:05` | `cowrie.client.kex` |
| `2026-09-04 16:21:06` | `cowrie.login.success` |
| `2026-09-04 16:21:06` | `cowrie.session.params` |
| `2026-09-04 16:21:06` | `cowrie.command.input` |
| `2026-09-04 16:21:06` | `cowrie.log.closed` |
| `2026-09-04 16:21:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8db2ad28d6b2

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-04 16:21 |
| **Last Seen** | 2026-09-04 16:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 16:21:05` | `cowrie.session.connect` |
| `2026-09-04 16:21:05` | `cowrie.client.version` |
| `2026-09-04 16:21:06` | `cowrie.client.kex` |
| `2026-09-04 16:21:07` | `cowrie.login.success` |
| `2026-09-04 16:21:07` | `cowrie.direct-tcpip.request` |
| `2026-09-04 16:21:07` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-04 16:21:07` | `cowrie.direct-tcpip.data` |
| `2026-09-04 16:21:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4003619fbdb7

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]53` |
| **First Seen** | 2026-09-04 16:21 |
| **Last Seen** | 2026-09-04 16:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 16:21:45` | `cowrie.session.connect` |
| `2026-09-04 16:21:45` | `cowrie.client.version` |
| `2026-09-04 16:21:45` | `cowrie.client.kex` |
| `2026-09-04 16:21:45` | `cowrie.login.success` |
| `2026-09-04 16:21:46` | `cowrie.session.params` |
| `2026-09-04 16:21:46` | `cowrie.command.input` |
| `2026-09-04 16:21:46` | `cowrie.log.closed` |
| `2026-09-04 16:21:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]53` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e3a28eb4abaa

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-09-04 16:23 |
| **Last Seen** | 2026-09-04 16:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 16:23:03` | `cowrie.session.connect` |
| `2026-09-04 16:23:03` | `cowrie.client.version` |
| `2026-09-04 16:23:03` | `cowrie.client.kex` |
| `2026-09-04 16:23:04` | `cowrie.login.success` |
| `2026-09-04 16:23:04` | `cowrie.session.params` |
| `2026-09-04 16:23:04` | `cowrie.command.input` |
| `2026-09-04 16:23:05` | `cowrie.log.closed` |
| `2026-09-04 16:23:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a09aadc5d864

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-09-04 16:23 |
| **Last Seen** | 2026-09-04 16:23 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 16:23:53` | `cowrie.session.connect` |
| `2026-09-04 16:23:53` | `cowrie.client.version` |
| `2026-09-04 16:23:53` | `cowrie.client.kex` |
| `2026-09-04 16:23:53` | `cowrie.login.success` |
| `2026-09-04 16:23:53` | `cowrie.direct-tcpip.request` |
| `2026-09-04 16:23:54` | `cowrie.direct-tcpip.data` |
| `2026-09-04 16:23:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8e6c28583be3

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]53` |
| **First Seen** | 2026-09-04 16:23 |
| **Last Seen** | 2026-09-04 16:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 16:23:58` | `cowrie.session.connect` |
| `2026-09-04 16:23:58` | `cowrie.client.version` |
| `2026-09-04 16:23:58` | `cowrie.client.kex` |
| `2026-09-04 16:23:59` | `cowrie.login.success` |
| `2026-09-04 16:23:59` | `cowrie.session.params` |
| `2026-09-04 16:23:59` | `cowrie.command.input` |
| `2026-09-04 16:24:00` | `cowrie.log.closed` |
| `2026-09-04 16:24:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]53` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8fd564e7f359

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-09-04 16:25 |
| **Last Seen** | 2026-09-04 16:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 16:25:02` | `cowrie.session.connect` |
| `2026-09-04 16:25:02` | `cowrie.client.version` |
| `2026-09-04 16:25:02` | `cowrie.client.kex` |
| `2026-09-04 16:25:03` | `cowrie.login.success` |
| `2026-09-04 16:25:03` | `cowrie.session.params` |
| `2026-09-04 16:25:03` | `cowrie.command.input` |
| `2026-09-04 16:25:04` | `cowrie.log.closed` |
| `2026-09-04 16:25:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3ee05da36191

| Field | Detail |
|---|---|
| **Source IP** | `138.226.239[.]233` |
| **First Seen** | 2026-09-04 16:25 |
| **Last Seen** | 2026-09-04 16:25 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 16:25:18` | `cowrie.session.connect` |
| `2026-09-04 16:25:18` | `cowrie.client.version` |
| `2026-09-04 16:25:18` | `cowrie.client.kex` |
| `2026-09-04 16:25:18` | `cowrie.login.success` |
| `2026-09-04 16:25:20` | `cowrie.direct-tcpip.request` |
| `2026-09-04 16:25:22` | `cowrie.direct-tcpip.ja4` |
| `2026-09-04 16:25:22` | `cowrie.direct-tcpip.data` |
| `2026-09-04 16:25:23` | `cowrie.direct-tcpip.request` |
| `2026-09-04 16:25:23` | `cowrie.direct-tcpip.ja4` |
| `2026-09-04 16:25:23` | `cowrie.direct-tcpip.data` |
| `2026-09-04 16:25:26` | `cowrie.direct-tcpip.request` |
| `2026-09-04 16:25:27` | `cowrie.direct-tcpip.ja4` |
| `2026-09-04 16:25:27` | `cowrie.direct-tcpip.data` |
| `2026-09-04 16:25:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.226.239[.]233` to AbuseIPDB if not already reported
- [ ] Block `138.226.239[.]233` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ca6d97c1c3da

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]53` |
| **First Seen** | 2026-09-04 16:26 |
| **Last Seen** | 2026-09-04 16:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 16:26:20` | `cowrie.session.connect` |
| `2026-09-04 16:26:20` | `cowrie.client.version` |
| `2026-09-04 16:26:20` | `cowrie.client.kex` |
| `2026-09-04 16:26:20` | `cowrie.login.success` |
| `2026-09-04 16:26:21` | `cowrie.session.params` |
| `2026-09-04 16:26:21` | `cowrie.command.input` |
| `2026-09-04 16:26:21` | `cowrie.log.closed` |
| `2026-09-04 16:26:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]53` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1119aa73e105

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-09-04 16:27 |
| **Last Seen** | 2026-09-04 16:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 16:27:05` | `cowrie.session.connect` |
| `2026-09-04 16:27:05` | `cowrie.client.version` |
| `2026-09-04 16:27:06` | `cowrie.client.kex` |
| `2026-09-04 16:27:06` | `cowrie.login.success` |
| `2026-09-04 16:27:07` | `cowrie.session.params` |
| `2026-09-04 16:27:07` | `cowrie.command.input` |
| `2026-09-04 16:27:07` | `cowrie.log.closed` |
| `2026-09-04 16:27:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-04aa4c868dd5

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]53` |
| **First Seen** | 2026-09-04 16:28 |
| **Last Seen** | 2026-09-04 16:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 16:28:47` | `cowrie.session.connect` |
| `2026-09-04 16:28:47` | `cowrie.client.version` |
| `2026-09-04 16:28:47` | `cowrie.client.kex` |
| `2026-09-04 16:28:47` | `cowrie.login.success` |
| `2026-09-04 16:28:49` | `cowrie.session.params` |
| `2026-09-04 16:28:49` | `cowrie.command.input` |
| `2026-09-04 16:28:49` | `cowrie.log.closed` |
| `2026-09-04 16:28:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]53` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8c72f7f68fb0

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-09-04 16:29 |
| **Last Seen** | 2026-09-04 16:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 16:29:03` | `cowrie.session.connect` |
| `2026-09-04 16:29:03` | `cowrie.client.version` |
| `2026-09-04 16:29:03` | `cowrie.client.kex` |
| `2026-09-04 16:29:04` | `cowrie.login.success` |
| `2026-09-04 16:29:04` | `cowrie.session.params` |
| `2026-09-04 16:29:04` | `cowrie.command.input` |
| `2026-09-04 16:29:04` | `cowrie.log.closed` |
| `2026-09-04 16:29:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1203e80996ba

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-09-04 16:30 |
| **Last Seen** | 2026-09-04 16:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 16:30:58` | `cowrie.session.connect` |
| `2026-09-04 16:30:58` | `cowrie.client.version` |
| `2026-09-04 16:30:58` | `cowrie.client.kex` |
| `2026-09-04 16:30:58` | `cowrie.login.success` |
| `2026-09-04 16:30:59` | `cowrie.session.params` |
| `2026-09-04 16:30:59` | `cowrie.command.input` |
| `2026-09-04 16:30:59` | `cowrie.log.closed` |
| `2026-09-04 16:30:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-605ffd50b3a7

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]53` |
| **First Seen** | 2026-09-04 16:31 |
| **Last Seen** | 2026-09-04 16:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 16:31:15` | `cowrie.session.connect` |
| `2026-09-04 16:31:15` | `cowrie.client.version` |
| `2026-09-04 16:31:15` | `cowrie.client.kex` |
| `2026-09-04 16:31:16` | `cowrie.login.success` |
| `2026-09-04 16:31:17` | `cowrie.session.params` |
| `2026-09-04 16:31:17` | `cowrie.command.input` |
| `2026-09-04 16:31:17` | `cowrie.log.closed` |
| `2026-09-04 16:31:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]53` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6105a9cd2a31

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-04 16:32 |
| **Last Seen** | 2026-09-04 16:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 16:32:03` | `cowrie.session.connect` |
| `2026-09-04 16:32:03` | `cowrie.client.version` |
| `2026-09-04 16:32:03` | `cowrie.client.kex` |
| `2026-09-04 16:32:04` | `cowrie.login.success` |
| `2026-09-04 16:32:04` | `cowrie.direct-tcpip.request` |
| `2026-09-04 16:32:04` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-04 16:32:04` | `cowrie.direct-tcpip.data` |
| `2026-09-04 16:32:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c5807ae5e854

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-09-04 16:32 |
| **Last Seen** | 2026-09-04 16:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 16:32:57` | `cowrie.session.connect` |
| `2026-09-04 16:32:57` | `cowrie.client.version` |
| `2026-09-04 16:32:57` | `cowrie.client.kex` |
| `2026-09-04 16:32:57` | `cowrie.login.success` |
| `2026-09-04 16:32:58` | `cowrie.session.params` |
| `2026-09-04 16:32:58` | `cowrie.command.input` |
| `2026-09-04 16:32:58` | `cowrie.log.closed` |
| `2026-09-04 16:32:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cb8ab3a2f313

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]53` |
| **First Seen** | 2026-09-04 16:33 |
| **Last Seen** | 2026-09-04 16:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 16:33:48` | `cowrie.session.connect` |
| `2026-09-04 16:33:48` | `cowrie.client.version` |
| `2026-09-04 16:33:48` | `cowrie.client.kex` |
| `2026-09-04 16:33:48` | `cowrie.login.success` |
| `2026-09-04 16:33:49` | `cowrie.session.params` |
| `2026-09-04 16:33:49` | `cowrie.command.input` |
| `2026-09-04 16:33:49` | `cowrie.log.closed` |
| `2026-09-04 16:33:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]53` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-34671a1e9743

| Field | Detail |
|---|---|
| **Source IP** | `80.94.95[.]118` |
| **First Seen** | 2026-09-04 16:34 |
| **Last Seen** | 2026-09-04 16:35 |
| **Session Duration** | 21s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 16:34:45` | `cowrie.session.connect` |
| `2026-09-04 16:34:45` | `cowrie.client.version` |
| `2026-09-04 16:34:45` | `cowrie.client.kex` |
| `2026-09-04 16:34:46` | `cowrie.login.success` |
| `2026-09-04 16:34:50` | `cowrie.direct-tcpip.request` |
| `2026-09-04 16:34:53` | `cowrie.direct-tcpip.ja4` |
| `2026-09-04 16:34:53` | `cowrie.direct-tcpip.data` |
| `2026-09-04 16:34:56` | `cowrie.direct-tcpip.request` |
| `2026-09-04 16:34:58` | `cowrie.direct-tcpip.ja4` |
| `2026-09-04 16:34:58` | `cowrie.direct-tcpip.data` |
| `2026-09-04 16:35:03` | `cowrie.direct-tcpip.request` |
| `2026-09-04 16:35:05` | `cowrie.direct-tcpip.ja4` |
| `2026-09-04 16:35:05` | `cowrie.direct-tcpip.data` |
| `2026-09-04 16:35:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.95[.]118` to AbuseIPDB if not already reported
- [ ] Block `80.94.95[.]118` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ec6240bcadb8

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-09-04 16:34 |
| **Last Seen** | 2026-09-04 16:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 16:34:55` | `cowrie.session.connect` |
| `2026-09-04 16:34:55` | `cowrie.client.version` |
| `2026-09-04 16:34:55` | `cowrie.client.kex` |
| `2026-09-04 16:34:55` | `cowrie.login.success` |
| `2026-09-04 16:34:56` | `cowrie.session.params` |
| `2026-09-04 16:34:56` | `cowrie.command.input` |
| `2026-09-04 16:34:56` | `cowrie.log.closed` |
| `2026-09-04 16:34:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-990b517a86f2

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]53` |
| **First Seen** | 2026-09-04 16:36 |
| **Last Seen** | 2026-09-04 16:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 16:36:12` | `cowrie.session.connect` |
| `2026-09-04 16:36:12` | `cowrie.client.version` |
| `2026-09-04 16:36:12` | `cowrie.client.kex` |
| `2026-09-04 16:36:13` | `cowrie.login.success` |
| `2026-09-04 16:36:13` | `cowrie.session.params` |
| `2026-09-04 16:36:13` | `cowrie.command.input` |
| `2026-09-04 16:36:13` | `cowrie.log.closed` |
| `2026-09-04 16:36:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]53` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7f51cee2d4ff

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]53` |
| **First Seen** | 2026-09-04 16:38 |
| **Last Seen** | 2026-09-04 16:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 16:38:37` | `cowrie.session.connect` |
| `2026-09-04 16:38:37` | `cowrie.client.version` |
| `2026-09-04 16:38:37` | `cowrie.client.kex` |
| `2026-09-04 16:38:37` | `cowrie.login.success` |
| `2026-09-04 16:38:38` | `cowrie.session.params` |
| `2026-09-04 16:38:38` | `cowrie.command.input` |
| `2026-09-04 16:38:38` | `cowrie.log.closed` |
| `2026-09-04 16:38:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]53` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1f63f51c3a5e

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]53` |
| **First Seen** | 2026-09-04 16:41 |
| **Last Seen** | 2026-09-04 16:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 16:41:04` | `cowrie.session.connect` |
| `2026-09-04 16:41:04` | `cowrie.client.version` |
| `2026-09-04 16:41:04` | `cowrie.client.kex` |
| `2026-09-04 16:41:05` | `cowrie.login.success` |
| `2026-09-04 16:41:05` | `cowrie.session.params` |
| `2026-09-04 16:41:05` | `cowrie.command.input` |
| `2026-09-04 16:41:06` | `cowrie.log.closed` |
| `2026-09-04 16:41:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]53` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-57522e65fd8a

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-04 16:43 |
| **Last Seen** | 2026-09-04 16:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 16:43:02` | `cowrie.session.connect` |
| `2026-09-04 16:43:02` | `cowrie.client.version` |
| `2026-09-04 16:43:03` | `cowrie.client.kex` |
| `2026-09-04 16:43:04` | `cowrie.login.success` |
| `2026-09-04 16:43:04` | `cowrie.direct-tcpip.request` |
| `2026-09-04 16:43:04` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-04 16:43:04` | `cowrie.direct-tcpip.data` |
| `2026-09-04 16:43:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-072c578a55f7

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]53` |
| **First Seen** | 2026-09-04 16:43 |
| **Last Seen** | 2026-09-04 16:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 16:43:25` | `cowrie.session.connect` |
| `2026-09-04 16:43:25` | `cowrie.client.version` |
| `2026-09-04 16:43:25` | `cowrie.client.kex` |
| `2026-09-04 16:43:26` | `cowrie.login.success` |
| `2026-09-04 16:43:27` | `cowrie.session.params` |
| `2026-09-04 16:43:27` | `cowrie.command.input` |
| `2026-09-04 16:43:27` | `cowrie.log.closed` |
| `2026-09-04 16:43:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]53` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0b47abdbdd62

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]53` |
| **First Seen** | 2026-09-04 16:45 |
| **Last Seen** | 2026-09-04 16:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 16:45:56` | `cowrie.session.connect` |
| `2026-09-04 16:45:56` | `cowrie.client.version` |
| `2026-09-04 16:45:56` | `cowrie.client.kex` |
| `2026-09-04 16:45:56` | `cowrie.login.success` |
| `2026-09-04 16:45:57` | `cowrie.session.params` |
| `2026-09-04 16:45:57` | `cowrie.command.input` |
| `2026-09-04 16:45:57` | `cowrie.log.closed` |
| `2026-09-04 16:45:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]53` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a91f1e5efe0a

| Field | Detail |
|---|---|
| **Source IP** | `86.97.240[.]189` |
| **First Seen** | 2026-09-04 16:47 |
| **Last Seen** | 2026-09-04 16:47 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 16:47:34` | `cowrie.session.connect` |
| `2026-09-04 16:47:34` | `cowrie.client.version` |
| `2026-09-04 16:47:34` | `cowrie.client.kex` |
| `2026-09-04 16:47:35` | `cowrie.login.success` |
| `2026-09-04 16:47:36` | `cowrie.session.params` |
| `2026-09-04 16:47:36` | `cowrie.command.input` |
| `2026-09-04 16:47:36` | `cowrie.command.failed` |
| `2026-09-04 16:47:36` | `cowrie.log.closed` |
| `2026-09-04 16:47:37` | `cowrie.session.params` |
| `2026-09-04 16:47:37` | `cowrie.command.input` |
| `2026-09-04 16:47:37` | `cowrie.session.file_download` |
| `2026-09-04 16:47:37` | `cowrie.log.closed` |
| `2026-09-04 16:47:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `86.97.240[.]189` to AbuseIPDB if not already reported
- [ ] Block `86.97.240[.]189` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-465c3abb2a37

| Field | Detail |
|---|---|
| **Source IP** | `86.97.240[.]189` |
| **First Seen** | 2026-09-04 16:47 |
| **Last Seen** | 2026-09-04 16:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 16:47:37` | `cowrie.session.connect` |
| `2026-09-04 16:47:37` | `cowrie.client.version` |
| `2026-09-04 16:47:37` | `cowrie.client.kex` |
| `2026-09-04 16:47:38` | `cowrie.login.success` |
| `2026-09-04 16:47:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `86.97.240[.]189` to AbuseIPDB if not already reported
- [ ] Block `86.97.240[.]189` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fe588ec59dc2

| Field | Detail |
|---|---|
| **Source IP** | `86.97.240[.]189` |
| **First Seen** | 2026-09-04 16:47 |
| **Last Seen** | 2026-09-04 16:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 16:47:39` | `cowrie.session.connect` |
| `2026-09-04 16:47:39` | `cowrie.client.version` |
| `2026-09-04 16:47:39` | `cowrie.client.kex` |
| `2026-09-04 16:47:40` | `cowrie.login.success` |
| `2026-09-04 16:47:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `86.97.240[.]189` to AbuseIPDB if not already reported
- [ ] Block `86.97.240[.]189` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f3c661ca3448

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]53` |
| **First Seen** | 2026-09-04 16:48 |
| **Last Seen** | 2026-09-04 16:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 16:48:26` | `cowrie.session.connect` |
| `2026-09-04 16:48:26` | `cowrie.client.version` |
| `2026-09-04 16:48:26` | `cowrie.client.kex` |
| `2026-09-04 16:48:27` | `cowrie.login.success` |
| `2026-09-04 16:48:28` | `cowrie.session.params` |
| `2026-09-04 16:48:28` | `cowrie.command.input` |
| `2026-09-04 16:48:28` | `cowrie.log.closed` |
| `2026-09-04 16:48:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]53` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9d0d52677c2a

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]53` |
| **First Seen** | 2026-09-04 16:50 |
| **Last Seen** | 2026-09-04 16:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 16:50:57` | `cowrie.session.connect` |
| `2026-09-04 16:50:57` | `cowrie.client.version` |
| `2026-09-04 16:50:57` | `cowrie.client.kex` |
| `2026-09-04 16:50:58` | `cowrie.login.success` |
| `2026-09-04 16:50:58` | `cowrie.session.params` |
| `2026-09-04 16:50:58` | `cowrie.command.input` |
| `2026-09-04 16:50:59` | `cowrie.log.closed` |
| `2026-09-04 16:50:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]53` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6412a65313cb

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]53` |
| **First Seen** | 2026-09-04 16:53 |
| **Last Seen** | 2026-09-04 16:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 16:53:33` | `cowrie.session.connect` |
| `2026-09-04 16:53:33` | `cowrie.client.version` |
| `2026-09-04 16:53:33` | `cowrie.client.kex` |
| `2026-09-04 16:53:33` | `cowrie.login.success` |
| `2026-09-04 16:53:34` | `cowrie.session.params` |
| `2026-09-04 16:53:34` | `cowrie.command.input` |
| `2026-09-04 16:53:34` | `cowrie.log.closed` |
| `2026-09-04 16:53:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]53` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-44a9525b7dda

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-04 16:54 |
| **Last Seen** | 2026-09-04 16:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 16:54:07` | `cowrie.session.connect` |
| `2026-09-04 16:54:07` | `cowrie.client.version` |
| `2026-09-04 16:54:08` | `cowrie.client.kex` |
| `2026-09-04 16:54:08` | `cowrie.login.success` |
| `2026-09-04 16:54:09` | `cowrie.direct-tcpip.request` |
| `2026-09-04 16:54:09` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-04 16:54:09` | `cowrie.direct-tcpip.data` |
| `2026-09-04 16:54:09` | `cowrie.session.closed` |

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
| `170.4.51[.]161` | **4** | 2026-09-04 16:00 | 2026-09-04 16:01 | 0m | 0 | `T1592` | 🟢 LOW |
| `181.47.126[.]240` | **3** | 2026-09-04 13:47 | 2026-09-04 13:48 | 0m | 0 | `T1592` | 🟢 LOW |
| `118.190.113[.]81` | **2** | 2026-09-04 14:40 | 2026-09-04 14:40 | 0m | 0 | `T1592` | 🟢 LOW |
| `193.90.12[.]122` | **2** | 2026-09-04 14:42 | 2026-09-04 15:15 | 2m | 0 | `T1592` | 🟢 LOW |
| `195.140.224[.]113` | **2** | 2026-09-04 14:03 | 2026-09-04 14:05 | 0m | 0 | `T1592` | 🟢 LOW |
| `213.230.92[.]6` | **2** | 2026-09-04 16:08 | 2026-09-04 16:08 | 0m | 0 | `T1592` | 🟢 LOW |
| `3.130.168[.]2` | **2** | 2026-09-04 15:09 | 2026-09-04 15:14 | 0m | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]240` | **2** | 2026-09-04 15:19 | 2026-09-04 15:21 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `80.94.92[.]179` | **2** | 2026-09-04 13:42 | 2026-09-04 14:20 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `104.152.52[.]208` | 1 | 2026-09-04 15:34 | 2026-09-04 15:34 | 0s | 0 | `T1592` | 🟢 LOW |
| `107.150.146[.]69` | 1 | 2026-09-04 15:47 | 2026-09-04 15:48 | 44s | 0 | `T1592` | 🟢 LOW |
| `115.190.188[.]79` | 1 | 2026-09-04 16:52 | 2026-09-04 16:52 | 0s | 0 | `T1592` | 🟢 LOW |
| `139.159.142[.]7` | 1 | 2026-09-04 16:53 | 2026-09-04 16:53 | 0s | 0 | `T1592` | 🟢 LOW |
| `170.84.134[.]172` | 1 | 2026-09-04 13:59 | 2026-09-04 13:59 | 10s | 0 | `T1592` | 🟢 LOW |
| `18.97.26[.]51` | 1 | 2026-09-04 13:01 | 2026-09-04 13:01 | 0s | 0 | `T1592` | 🟢 LOW |
| `180.76.174[.]141` | 1 | 2026-09-04 14:34 | 2026-09-04 14:36 | 120s | 0 | `T1592` | 🟢 LOW |
| `185.213.174[.]233` | 1 | 2026-09-04 14:45 | 2026-09-04 14:45 | 5s | 0 | `T1592` | 🟢 LOW |
| `185.230.206[.]151` | 1 | 2026-09-04 15:09 | 2026-09-04 15:09 | 0s | 0 | `T1592` | 🟢 LOW |
| `195.96.139[.]86` | 1 | 2026-09-04 15:08 | 2026-09-04 15:08 | 1s | 0 | `T1592` | 🟢 LOW |
| `2.57.122[.]53` | 1 | 2026-09-04 15:52 | 2026-09-04 15:52 | 0s | 0 | `T1592` | 🟢 LOW |
| `213.109.226[.]18` | 1 | 2026-09-04 13:59 | 2026-09-04 14:00 | 30s | 0 | `T1592` | 🟢 LOW |
| `39.99.32[.]133` | 1 | 2026-09-04 16:35 | 2026-09-04 16:37 | 120s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]157` | 1 | 2026-09-04 13:03 | 2026-09-04 13:03 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.115[.]59` | 1 | 2026-09-04 14:35 | 2026-09-04 14:35 | 0s | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]50` | 1 | 2026-09-04 14:52 | 2026-09-04 14:52 | 15s | 0 | `T1592` | 🟢 LOW |
| `81.23.170[.]238` | 1 | 2026-09-04 16:01 | 2026-09-04 16:03 | 120s | 0 | `T1592` | 🟢 LOW |

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
| `45.148.10[.]240` | NL | TECHOFF SRV LIMITED | **100** ⚠️ | 50 |
| `45.148.10[.]157` | NL | TECHOFF SRV LIMITED | **100** ⚠️ | 50 |
| `81.23.170[.]238` | RU | MTS PJSC | **100** ⚠️ | 15 |
| `64.110.90[.]250` | KR | Oracle Corporation | **100** ⚠️ | 8 |
| `80.94.92[.]179` | RO | TECHOFF SRV LIMITED | **100** ⚠️ | 0 |
| `47.236.238[.]212` | SG | Alibaba Cloud LLC | **100** ⚠️ | 9 |
| `170.84.134[.]172` | NI | Daibutsu Tipitapa | **100** ⚠️ | 2 |
| `117.50.194[.]182` | CN | Shanghai UCloud Information Technology Company Limited | **100** ⚠️ | 10 |
| `180.76.174[.]141` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 41 |
| `45.79.115[.]59` | US | Linode | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 263 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 254 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 44 |
| [T1222.002](https://attack.mitre.org/techniques/T1222/002) | 43 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 43 |

---

## 🔕 False Positive Summary (27 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 8 |
| AbuseIPDB score 14 below threshold 25 | 2 |
| AbuseIPDB score 15 below threshold 25 | 2 |
| AbuseIPDB score 22 below threshold 25 | 2 |
| AbuseIPDB score 24 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 12 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 318 cases |
| Tool 34  | Credential Extractor        | ✅ 271 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 16 fingerprints |
| Tool 36  | Command Clustering          | ✅ 8 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 64 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 27 filtered (8.5%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 48 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 21 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 253 priority case(s) shown individually · 26 recon entry/entries in table (9 group(s) consolidating 21 session(s)).

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
_Report time: 2026-09-04T18:55:11Z_

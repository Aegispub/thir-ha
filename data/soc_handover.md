# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-06-12 |
| **Generated At** | 2026-06-12T04:58:32Z |
| **Shift Time** | 04:58 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **237** |
| Confirmed Threats | **223** |
| False Positives Filtered | **14** (5.9%) |
| Unique Attacker IPs | **38** |
| Countries of Origin | **14** |
| High Severity Cases | **44** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **193** |
| Malware Samples Analyzed | **0** HIGH · **20** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **44** |
| Unique Credential Pairs | **35** |
| Unique Usernames | **17** |
| Unique Passwords | **30** |
| Successful Auth Pairs | **40** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 16 |
| `trader` | 5 |
| `ubuntu` | 4 |
| `admin` | 3 |
| `sol` | 3 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `smo@@kkklss` | 4 |
| `123` | 3 |
| `trader` | 3 |
| `LeitboGi0ro` | 3 |
| `123@@@` | 3 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `smo@@kkklss` | 4 |
| `root` | `LeitboGi0ro` | 3 |
| `root` | `123@@@` | 3 |
| `trading` | `trading` | 2 |
| `trader` | `trader123` | 2 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `hadoop` | `123` | `45.156.87.166` | 2026-06-12T02:55:04 |
| `test` | `passwd` | `45.156.87.166` | 2026-06-12T02:55:10 |
| `root` | `firedancer` | `45.148.10.183` | 2026-06-12T02:55:35 |
| `root` | `shredstream` | `45.148.10.183` | 2026-06-12T02:57:49 |
| `shred` | `shred` | `45.148.10.183` | 2026-06-12T02:59:56 |
| `root` | `ankurkudintzi` | `176.65.139.29` | 2026-06-12T03:01:56 |
| `validator` | `123` | `45.148.10.183` | 2026-06-12T03:02:00 |
| `binance` | `binance` | `45.148.10.183` | 2026-06-12T03:04:15 |
| `trader` | `trader` | `45.148.10.183` | 2026-06-12T03:06:26 |
| `trading` | `trading` | `45.148.10.183` | 2026-06-12T03:08:39 |
| `ubuntu` | `trader` | `45.148.10.183` | 2026-06-12T03:10:52 |
| `bitcoin` | `bitcoin` | `45.148.10.183` | 2026-06-12T03:12:57 |
| `ethereum` | `ethereum` | `45.148.10.183` | 2026-06-12T03:15:01 |
| `root` | `trader` | `45.148.10.183` | 2026-06-12T03:17:11 |
| `root` | `LeitboGi0ro` | `138.2.98.41` | 2026-06-12T03:17:49 |
| `root` | `123@@@` | `138.2.98.41` | 2026-06-12T03:17:49 |
| `admin` | `camaroz28` | `2.57.121.112` | 2026-06-12T03:18:24 |
| `trader` | `trader123` | `45.148.10.183` | 2026-06-12T03:19:21 |
| `root` | `﻿------fuck------` | `212.83.145.101` | 2026-06-12T03:19:25 |
| `trader` | `trader1234` | `45.148.10.183` | 2026-06-12T03:21:35 |
| `trader` | `ibkr123` | `45.148.10.183` | 2026-06-12T03:23:53 |
| `root` | `ibkr123` | `45.148.10.183` | 2026-06-12T03:26:01 |
| `exchange` | `exchange` | `45.148.10.183` | 2026-06-12T03:28:09 |
| `solana` | `solana` | `45.148.10.183` | 2026-06-12T03:30:20 |
| `sol` | `sol` | `45.148.10.183` | 2026-06-12T03:32:25 |
| `sol` | `123` | `45.148.10.183` | 2026-06-12T03:34:40 |
| `sol` | `1234` | `45.148.10.183` | 2026-06-12T03:36:56 |
| `ubuntu` | `ubuntu` | `45.148.10.183` | 2026-06-12T03:39:06 |
| `ubuntu` | `123456` | `45.148.10.183` | 2026-06-12T03:41:16 |
| `root` | `123@@@` | `129.153.145.135` | 2026-06-12T03:42:07 |
| `root` | `LeitboGi0ro` | `129.153.145.135` | 2026-06-12T03:42:07 |
| `root` | `smo@@kkklss` | `129.153.145.135` | 2026-06-12T03:42:14 |
| `ubuntu` | `12345678` | `45.148.10.183` | 2026-06-12T03:43:28 |
| `jajuan` | `jajuan` | `213.209.159.56` | 2026-06-12T03:46:11 |
| `pool` | `pool` | `45.148.10.183` | 2026-06-12T03:50:02 |
| `admin` | `admin` | `114.33.12.13` | 2026-06-12T04:11:02 |
| `root` | `LeitboGi0ro` | `144.22.238.238` | 2026-06-12T04:19:40 |
| `root` | `123@@@` | `144.22.238.238` | 2026-06-12T04:19:41 |
| `root` | `smo@@kkklss` | `144.22.238.238` | 2026-06-12T04:19:51 |
| `admin` | `cajun1` | `2.57.121.112` | 2026-06-12T04:32:08 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **237** |
| Sessions with Fingerprint | **8** |
| Unique HASSH Fingerprints | **8** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 29 |
| Paramiko (Python) | 10 |
| PuTTY | 4 |
| OpenSSH | 2 |
| Unknown | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `16443846184e...` | Generic scanner | 27 | 2 |
| `a2de0f306611...` | Mirai/variant | 10 | 3 |
| `57446c12547a...` | Mirai/variant | 3 | 2 |
| `bc9e7273cde2...` | Mirai/variant | 2 | 2 |
| `0a07365cc01f...` | Generic scanner | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `16443846184e...` | Go SSH scanner | 27 | 2 | Generic scanner |
| `a2de0f306611...` | Paramiko (Python) | 10 | 3 | Mirai/variant |
| `57446c12547a...` | PuTTY | 3 | 2 | Mirai/variant |
| `bc9e7273cde2...` | OpenSSH | 2 | 2 | Mirai/variant |
| `0a07365cc01f...` | Go SSH scanner | 1 | 1 | Generic scanner |
| `98f63c4d9c87...` | Go SSH scanner | 1 | 1 | Generic scanner |
| `5bd26477da54...` | PuTTY | 1 | 1 | Mirai/variant |
| `dd9bcf093c35...` | Unknown | 1 | 1 | Mirai/variant |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **4** |
| Campaign Clusters | **1** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1082, T1592, T1105, T1059.004` |

**🔴 HIGH · Mirai/IoT Botnet**

> Mirai-family IoT botnet. Executes busybox payloads for DDoS bot recruitment.

Representative commands:
```
sh
```
```
shell
```
```
enable
```
```
system
```
```
ping; sh
```
Source IPs: `114.33.12.13`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **38** |
| Unique ASNs | **22** |
| High-Risk ASNs | **17** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS25369` | Hydra Communications Ltd | 4 | HIGH |
| `AS396982` | Google LLC | 4 | LOW |
| `AS4134` | CHINANET BACKBONE | 4 | HIGH |
| `AS63949` | Akamai Connected Cloud | 3 | HIGH |
| `AS31898` | Oracle Corporation | 3 | HIGH |
| `AS47890` | UNMANAGED LTD | 2 | HIGH |
| `AS3462` | Data Communication Business Group | 2 | HIGH |
| `AS14061` | DigitalOcean, LLC | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (44)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-d725becf72b9

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]166` |
| **First Seen** | 2026-06-12 02:55 |
| **Last Seen** | 2026-06-12 02:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 02:55:04` | `cowrie.login.success` |
| `2026-06-12 02:55:05` | `cowrie.session.params` |
| `2026-06-12 02:55:05` | `cowrie.command.input` |
| `2026-06-12 02:55:05` | `cowrie.log.closed` |
| `2026-06-12 02:55:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]166` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]166` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-364a7256448e

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]166` |
| **First Seen** | 2026-06-12 02:55 |
| **Last Seen** | 2026-06-12 02:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 02:55:10` | `cowrie.session.connect` |
| `2026-06-12 02:55:10` | `cowrie.client.version` |
| `2026-06-12 02:55:10` | `cowrie.client.kex` |
| `2026-06-12 02:55:10` | `cowrie.login.success` |
| `2026-06-12 02:55:11` | `cowrie.session.params` |
| `2026-06-12 02:55:11` | `cowrie.command.input` |
| `2026-06-12 02:55:11` | `cowrie.log.closed` |
| `2026-06-12 02:55:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]166` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]166` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aff543cbfd71

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-12 02:55 |
| **Last Seen** | 2026-06-12 02:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 02:55:35` | `cowrie.session.connect` |
| `2026-06-12 02:55:35` | `cowrie.client.version` |
| `2026-06-12 02:55:35` | `cowrie.client.kex` |
| `2026-06-12 02:55:35` | `cowrie.login.success` |
| `2026-06-12 02:55:36` | `cowrie.session.params` |
| `2026-06-12 02:55:36` | `cowrie.command.input` |
| `2026-06-12 02:55:36` | `cowrie.log.closed` |
| `2026-06-12 02:55:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c3e39db70946

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-12 02:57 |
| **Last Seen** | 2026-06-12 02:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 02:57:49` | `cowrie.session.connect` |
| `2026-06-12 02:57:49` | `cowrie.client.version` |
| `2026-06-12 02:57:49` | `cowrie.client.kex` |
| `2026-06-12 02:57:49` | `cowrie.login.success` |
| `2026-06-12 02:57:50` | `cowrie.session.params` |
| `2026-06-12 02:57:50` | `cowrie.command.input` |
| `2026-06-12 02:57:50` | `cowrie.log.closed` |
| `2026-06-12 02:57:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e944e045c877

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-12 02:59 |
| **Last Seen** | 2026-06-12 02:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 02:59:56` | `cowrie.session.connect` |
| `2026-06-12 02:59:56` | `cowrie.client.version` |
| `2026-06-12 02:59:56` | `cowrie.client.kex` |
| `2026-06-12 02:59:56` | `cowrie.login.success` |
| `2026-06-12 02:59:57` | `cowrie.session.params` |
| `2026-06-12 02:59:57` | `cowrie.command.input` |
| `2026-06-12 02:59:57` | `cowrie.log.closed` |
| `2026-06-12 02:59:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f0a649afa553

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]29` |
| **First Seen** | 2026-06-12 03:01 |
| **Last Seen** | 2026-06-12 03:01 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 03:01:55` | `cowrie.session.connect` |
| `2026-06-12 03:01:55` | `cowrie.client.version` |
| `2026-06-12 03:01:56` | `cowrie.client.kex` |
| `2026-06-12 03:01:56` | `cowrie.login.success` |
| `2026-06-12 03:01:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]29` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]29` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-213d9ae27242

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-12 03:02 |
| **Last Seen** | 2026-06-12 03:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 03:02:00` | `cowrie.session.connect` |
| `2026-06-12 03:02:00` | `cowrie.client.version` |
| `2026-06-12 03:02:00` | `cowrie.client.kex` |
| `2026-06-12 03:02:00` | `cowrie.login.success` |
| `2026-06-12 03:02:01` | `cowrie.session.params` |
| `2026-06-12 03:02:01` | `cowrie.command.input` |
| `2026-06-12 03:02:01` | `cowrie.log.closed` |
| `2026-06-12 03:02:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ee9e308337e5

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-12 03:04 |
| **Last Seen** | 2026-06-12 03:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 03:04:15` | `cowrie.session.connect` |
| `2026-06-12 03:04:15` | `cowrie.client.version` |
| `2026-06-12 03:04:15` | `cowrie.client.kex` |
| `2026-06-12 03:04:15` | `cowrie.login.success` |
| `2026-06-12 03:04:16` | `cowrie.session.params` |
| `2026-06-12 03:04:16` | `cowrie.command.input` |
| `2026-06-12 03:04:16` | `cowrie.log.closed` |
| `2026-06-12 03:04:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b1f5e05b7094

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-12 03:06 |
| **Last Seen** | 2026-06-12 03:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 03:06:25` | `cowrie.session.connect` |
| `2026-06-12 03:06:25` | `cowrie.client.version` |
| `2026-06-12 03:06:25` | `cowrie.client.kex` |
| `2026-06-12 03:06:26` | `cowrie.login.success` |
| `2026-06-12 03:06:27` | `cowrie.session.params` |
| `2026-06-12 03:06:27` | `cowrie.command.input` |
| `2026-06-12 03:06:27` | `cowrie.log.closed` |
| `2026-06-12 03:06:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c06400b43cbe

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-12 03:08 |
| **Last Seen** | 2026-06-12 03:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 03:08:38` | `cowrie.session.connect` |
| `2026-06-12 03:08:38` | `cowrie.client.version` |
| `2026-06-12 03:08:38` | `cowrie.client.kex` |
| `2026-06-12 03:08:39` | `cowrie.login.success` |
| `2026-06-12 03:08:39` | `cowrie.session.params` |
| `2026-06-12 03:08:39` | `cowrie.command.input` |
| `2026-06-12 03:08:40` | `cowrie.log.closed` |
| `2026-06-12 03:08:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ae38e2fb84fe

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-12 03:10 |
| **Last Seen** | 2026-06-12 03:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 03:10:51` | `cowrie.session.connect` |
| `2026-06-12 03:10:51` | `cowrie.client.version` |
| `2026-06-12 03:10:51` | `cowrie.client.kex` |
| `2026-06-12 03:10:52` | `cowrie.login.success` |
| `2026-06-12 03:10:52` | `cowrie.session.params` |
| `2026-06-12 03:10:52` | `cowrie.command.input` |
| `2026-06-12 03:10:52` | `cowrie.log.closed` |
| `2026-06-12 03:10:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-107d8c8618dc

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-12 03:12 |
| **Last Seen** | 2026-06-12 03:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 03:12:57` | `cowrie.session.connect` |
| `2026-06-12 03:12:57` | `cowrie.client.version` |
| `2026-06-12 03:12:57` | `cowrie.client.kex` |
| `2026-06-12 03:12:57` | `cowrie.login.success` |
| `2026-06-12 03:12:58` | `cowrie.session.params` |
| `2026-06-12 03:12:58` | `cowrie.command.input` |
| `2026-06-12 03:12:58` | `cowrie.log.closed` |
| `2026-06-12 03:12:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9f441ce60081

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-12 03:15 |
| **Last Seen** | 2026-06-12 03:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 03:15:01` | `cowrie.session.connect` |
| `2026-06-12 03:15:01` | `cowrie.client.version` |
| `2026-06-12 03:15:01` | `cowrie.client.kex` |
| `2026-06-12 03:15:01` | `cowrie.login.success` |
| `2026-06-12 03:15:02` | `cowrie.session.params` |
| `2026-06-12 03:15:02` | `cowrie.command.input` |
| `2026-06-12 03:15:02` | `cowrie.log.closed` |
| `2026-06-12 03:15:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-31e6e3e8f788

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-12 03:17 |
| **Last Seen** | 2026-06-12 03:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 03:17:11` | `cowrie.session.connect` |
| `2026-06-12 03:17:11` | `cowrie.client.version` |
| `2026-06-12 03:17:11` | `cowrie.client.kex` |
| `2026-06-12 03:17:11` | `cowrie.login.success` |
| `2026-06-12 03:17:12` | `cowrie.session.params` |
| `2026-06-12 03:17:12` | `cowrie.command.input` |
| `2026-06-12 03:17:12` | `cowrie.log.closed` |
| `2026-06-12 03:17:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5f5075987424

| Field | Detail |
|---|---|
| **Source IP** | `138.2.98[.]41` |
| **First Seen** | 2026-06-12 03:17 |
| **Last Seen** | 2026-06-12 03:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 03:17:47` | `cowrie.session.connect` |
| `2026-06-12 03:17:47` | `cowrie.client.version` |
| `2026-06-12 03:17:48` | `cowrie.client.kex` |
| `2026-06-12 03:17:49` | `cowrie.login.success` |
| `2026-06-12 03:17:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.2.98[.]41` to AbuseIPDB if not already reported
- [ ] Block `138.2.98[.]41` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2ca677a44e3c

| Field | Detail |
|---|---|
| **Source IP** | `138.2.98[.]41` |
| **First Seen** | 2026-06-12 03:17 |
| **Last Seen** | 2026-06-12 03:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 03:17:47` | `cowrie.session.connect` |
| `2026-06-12 03:17:47` | `cowrie.client.version` |
| `2026-06-12 03:17:48` | `cowrie.client.kex` |
| `2026-06-12 03:17:49` | `cowrie.login.success` |
| `2026-06-12 03:17:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.2.98[.]41` to AbuseIPDB if not already reported
- [ ] Block `138.2.98[.]41` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a8277b7d6943

| Field | Detail |
|---|---|
| **Source IP** | `2.57.121[.]112` |
| **First Seen** | 2026-06-12 03:18 |
| **Last Seen** | 2026-06-12 03:18 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 03:18:24` | `cowrie.session.connect` |
| `2026-06-12 03:18:24` | `cowrie.client.version` |
| `2026-06-12 03:18:24` | `cowrie.client.kex` |
| `2026-06-12 03:18:24` | `cowrie.login.success` |
| `2026-06-12 03:18:25` | `cowrie.direct-tcpip.request` |
| `2026-06-12 03:18:25` | `cowrie.direct-tcpip.data` |
| `2026-06-12 03:18:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.121[.]112` to AbuseIPDB if not already reported
- [ ] Block `2.57.121[.]112` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-83500b132de3

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-12 03:19 |
| **Last Seen** | 2026-06-12 03:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 03:19:21` | `cowrie.session.connect` |
| `2026-06-12 03:19:21` | `cowrie.client.version` |
| `2026-06-12 03:19:21` | `cowrie.client.kex` |
| `2026-06-12 03:19:21` | `cowrie.login.success` |
| `2026-06-12 03:19:22` | `cowrie.session.params` |
| `2026-06-12 03:19:22` | `cowrie.command.input` |
| `2026-06-12 03:19:22` | `cowrie.log.closed` |
| `2026-06-12 03:19:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d79a34c6a6e1

| Field | Detail |
|---|---|
| **Source IP** | `212.83.145[.]101` |
| **First Seen** | 2026-06-12 03:19 |
| **Last Seen** | 2026-06-12 03:19 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 03:19:24` | `cowrie.session.connect` |
| `2026-06-12 03:19:24` | `cowrie.client.version` |
| `2026-06-12 03:19:24` | `cowrie.client.kex` |
| `2026-06-12 03:19:25` | `cowrie.login.success` |
| `2026-06-12 03:19:26` | `cowrie.session.params` |
| `2026-06-12 03:19:26` | `cowrie.command.input` |
| `2026-06-12 03:19:26` | `cowrie.log.closed` |
| `2026-06-12 03:19:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `212.83.145[.]101` to AbuseIPDB if not already reported
- [ ] Block `212.83.145[.]101` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e2d9ace6c65d

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-12 03:21 |
| **Last Seen** | 2026-06-12 03:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 03:21:35` | `cowrie.session.connect` |
| `2026-06-12 03:21:35` | `cowrie.client.version` |
| `2026-06-12 03:21:35` | `cowrie.client.kex` |
| `2026-06-12 03:21:35` | `cowrie.login.success` |
| `2026-06-12 03:21:36` | `cowrie.session.params` |
| `2026-06-12 03:21:36` | `cowrie.command.input` |
| `2026-06-12 03:21:36` | `cowrie.log.closed` |
| `2026-06-12 03:21:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b36f93f2562b

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-12 03:23 |
| **Last Seen** | 2026-06-12 03:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 03:23:53` | `cowrie.session.connect` |
| `2026-06-12 03:23:53` | `cowrie.client.version` |
| `2026-06-12 03:23:53` | `cowrie.client.kex` |
| `2026-06-12 03:23:53` | `cowrie.login.success` |
| `2026-06-12 03:23:54` | `cowrie.session.params` |
| `2026-06-12 03:23:54` | `cowrie.command.input` |
| `2026-06-12 03:23:54` | `cowrie.log.closed` |
| `2026-06-12 03:23:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-50212d71f299

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-12 03:26 |
| **Last Seen** | 2026-06-12 03:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 03:26:00` | `cowrie.session.connect` |
| `2026-06-12 03:26:00` | `cowrie.client.version` |
| `2026-06-12 03:26:00` | `cowrie.client.kex` |
| `2026-06-12 03:26:01` | `cowrie.login.success` |
| `2026-06-12 03:26:01` | `cowrie.session.params` |
| `2026-06-12 03:26:01` | `cowrie.command.input` |
| `2026-06-12 03:26:01` | `cowrie.log.closed` |
| `2026-06-12 03:26:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dca7bc1ba195

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-12 03:28 |
| **Last Seen** | 2026-06-12 03:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 03:28:08` | `cowrie.session.connect` |
| `2026-06-12 03:28:08` | `cowrie.client.version` |
| `2026-06-12 03:28:08` | `cowrie.client.kex` |
| `2026-06-12 03:28:09` | `cowrie.login.success` |
| `2026-06-12 03:28:09` | `cowrie.session.params` |
| `2026-06-12 03:28:09` | `cowrie.command.input` |
| `2026-06-12 03:28:10` | `cowrie.log.closed` |
| `2026-06-12 03:28:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b3bef764ada2

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-12 03:30 |
| **Last Seen** | 2026-06-12 03:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 03:30:19` | `cowrie.session.connect` |
| `2026-06-12 03:30:19` | `cowrie.client.version` |
| `2026-06-12 03:30:20` | `cowrie.client.kex` |
| `2026-06-12 03:30:20` | `cowrie.login.success` |
| `2026-06-12 03:30:21` | `cowrie.session.params` |
| `2026-06-12 03:30:21` | `cowrie.command.input` |
| `2026-06-12 03:30:21` | `cowrie.log.closed` |
| `2026-06-12 03:30:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c22d86295d52

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-12 03:32 |
| **Last Seen** | 2026-06-12 03:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 03:32:24` | `cowrie.session.connect` |
| `2026-06-12 03:32:24` | `cowrie.client.version` |
| `2026-06-12 03:32:24` | `cowrie.client.kex` |
| `2026-06-12 03:32:25` | `cowrie.login.success` |
| `2026-06-12 03:32:25` | `cowrie.session.params` |
| `2026-06-12 03:32:25` | `cowrie.command.input` |
| `2026-06-12 03:32:26` | `cowrie.log.closed` |
| `2026-06-12 03:32:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-128f84f821e5

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-12 03:34 |
| **Last Seen** | 2026-06-12 03:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 03:34:39` | `cowrie.session.connect` |
| `2026-06-12 03:34:39` | `cowrie.client.version` |
| `2026-06-12 03:34:39` | `cowrie.client.kex` |
| `2026-06-12 03:34:40` | `cowrie.login.success` |
| `2026-06-12 03:34:40` | `cowrie.session.params` |
| `2026-06-12 03:34:40` | `cowrie.command.input` |
| `2026-06-12 03:34:40` | `cowrie.log.closed` |
| `2026-06-12 03:34:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-73938d07cbbf

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-12 03:36 |
| **Last Seen** | 2026-06-12 03:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 03:36:55` | `cowrie.session.connect` |
| `2026-06-12 03:36:55` | `cowrie.client.version` |
| `2026-06-12 03:36:56` | `cowrie.client.kex` |
| `2026-06-12 03:36:56` | `cowrie.login.success` |
| `2026-06-12 03:36:57` | `cowrie.session.params` |
| `2026-06-12 03:36:57` | `cowrie.command.input` |
| `2026-06-12 03:36:57` | `cowrie.log.closed` |
| `2026-06-12 03:36:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9bb5a8b1b7d4

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-12 03:39 |
| **Last Seen** | 2026-06-12 03:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 03:39:05` | `cowrie.session.connect` |
| `2026-06-12 03:39:05` | `cowrie.client.version` |
| `2026-06-12 03:39:05` | `cowrie.client.kex` |
| `2026-06-12 03:39:06` | `cowrie.login.success` |
| `2026-06-12 03:39:06` | `cowrie.session.params` |
| `2026-06-12 03:39:06` | `cowrie.command.input` |
| `2026-06-12 03:39:07` | `cowrie.log.closed` |
| `2026-06-12 03:39:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9836fe192bfe

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-12 03:41 |
| **Last Seen** | 2026-06-12 03:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 03:41:16` | `cowrie.session.connect` |
| `2026-06-12 03:41:16` | `cowrie.client.version` |
| `2026-06-12 03:41:16` | `cowrie.client.kex` |
| `2026-06-12 03:41:16` | `cowrie.login.success` |
| `2026-06-12 03:41:17` | `cowrie.session.params` |
| `2026-06-12 03:41:17` | `cowrie.command.input` |
| `2026-06-12 03:41:17` | `cowrie.log.closed` |
| `2026-06-12 03:41:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9568f36e9d38

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-12 03:42 |
| **Last Seen** | 2026-06-12 03:42 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 03:42:07` | `cowrie.session.connect` |
| `2026-06-12 03:42:07` | `cowrie.client.version` |
| `2026-06-12 03:42:07` | `cowrie.client.kex` |
| `2026-06-12 03:42:07` | `cowrie.login.success` |
| `2026-06-12 03:42:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b9dc312435d9

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-12 03:42 |
| **Last Seen** | 2026-06-12 03:42 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 03:42:07` | `cowrie.session.connect` |
| `2026-06-12 03:42:07` | `cowrie.client.version` |
| `2026-06-12 03:42:07` | `cowrie.client.kex` |
| `2026-06-12 03:42:07` | `cowrie.login.success` |
| `2026-06-12 03:42:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-25a05d796303

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-12 03:42 |
| **Last Seen** | 2026-06-12 03:42 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 03:42:14` | `cowrie.session.connect` |
| `2026-06-12 03:42:14` | `cowrie.client.version` |
| `2026-06-12 03:42:14` | `cowrie.client.kex` |
| `2026-06-12 03:42:14` | `cowrie.login.success` |
| `2026-06-12 03:42:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-02d59fa3005f

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-12 03:42 |
| **Last Seen** | 2026-06-12 03:42 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 03:42:14` | `cowrie.session.connect` |
| `2026-06-12 03:42:14` | `cowrie.client.version` |
| `2026-06-12 03:42:14` | `cowrie.client.kex` |
| `2026-06-12 03:42:14` | `cowrie.login.success` |
| `2026-06-12 03:42:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-37dfd12fbee2

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-12 03:43 |
| **Last Seen** | 2026-06-12 03:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 03:43:27` | `cowrie.session.connect` |
| `2026-06-12 03:43:27` | `cowrie.client.version` |
| `2026-06-12 03:43:27` | `cowrie.client.kex` |
| `2026-06-12 03:43:28` | `cowrie.login.success` |
| `2026-06-12 03:43:29` | `cowrie.session.params` |
| `2026-06-12 03:43:29` | `cowrie.command.input` |
| `2026-06-12 03:43:29` | `cowrie.log.closed` |
| `2026-06-12 03:43:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d63148b94c2b

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-12 03:45 |
| **Last Seen** | 2026-06-12 03:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 03:45:33` | `cowrie.session.connect` |
| `2026-06-12 03:45:33` | `cowrie.client.version` |
| `2026-06-12 03:45:34` | `cowrie.client.kex` |
| `2026-06-12 03:45:34` | `cowrie.login.success` |
| `2026-06-12 03:45:35` | `cowrie.session.params` |
| `2026-06-12 03:45:35` | `cowrie.command.input` |
| `2026-06-12 03:45:35` | `cowrie.log.closed` |
| `2026-06-12 03:45:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9d44e2a388c4

| Field | Detail |
|---|---|
| **Source IP** | `213.209.159[.]56` |
| **First Seen** | 2026-06-12 03:46 |
| **Last Seen** | 2026-06-12 03:46 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 03:46:10` | `cowrie.session.connect` |
| `2026-06-12 03:46:10` | `cowrie.client.version` |
| `2026-06-12 03:46:10` | `cowrie.client.kex` |
| `2026-06-12 03:46:11` | `cowrie.login.success` |
| `2026-06-12 03:46:11` | `cowrie.direct-tcpip.request` |
| `2026-06-12 03:46:11` | `cowrie.direct-tcpip.data` |
| `2026-06-12 03:46:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.209.159[.]56` to AbuseIPDB if not already reported
- [ ] Block `213.209.159[.]56` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-84b988b1dfb6

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-12 03:47 |
| **Last Seen** | 2026-06-12 03:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 03:47:46` | `cowrie.session.connect` |
| `2026-06-12 03:47:46` | `cowrie.client.version` |
| `2026-06-12 03:47:46` | `cowrie.client.kex` |
| `2026-06-12 03:47:46` | `cowrie.login.success` |
| `2026-06-12 03:47:47` | `cowrie.session.params` |
| `2026-06-12 03:47:47` | `cowrie.command.input` |
| `2026-06-12 03:47:47` | `cowrie.log.closed` |
| `2026-06-12 03:47:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d1c6747b2df7

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-12 03:50 |
| **Last Seen** | 2026-06-12 03:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 03:50:02` | `cowrie.session.connect` |
| `2026-06-12 03:50:02` | `cowrie.client.version` |
| `2026-06-12 03:50:02` | `cowrie.client.kex` |
| `2026-06-12 03:50:02` | `cowrie.login.success` |
| `2026-06-12 03:50:03` | `cowrie.session.params` |
| `2026-06-12 03:50:03` | `cowrie.command.input` |
| `2026-06-12 03:50:03` | `cowrie.log.closed` |
| `2026-06-12 03:50:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-37e699887228

| Field | Detail |
|---|---|
| **Source IP** | `114.33.12[.]13` |
| **First Seen** | 2026-06-12 04:11 |
| **Last Seen** | 2026-06-12 04:11 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh, shell, enable, system, ping; sh` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 04:11:01` | `cowrie.session.connect` |
| `2026-06-12 04:11:02` | `cowrie.login.success` |
| `2026-06-12 04:11:02` | `cowrie.session.params` |
| `2026-06-12 04:11:02` | `cowrie.command.input` |
| `2026-06-12 04:11:02` | `cowrie.command.input` |
| `2026-06-12 04:11:02` | `cowrie.command.failed` |
| `2026-06-12 04:11:02` | `cowrie.command.input` |
| `2026-06-12 04:11:02` | `cowrie.command.failed` |
| `2026-06-12 04:11:02` | `cowrie.command.input` |
| `2026-06-12 04:11:02` | `cowrie.command.failed` |
| `2026-06-12 04:11:02` | `cowrie.command.input` |
| `2026-06-12 04:11:02` | `cowrie.command.input` |
| `2026-06-12 04:11:03` | `cowrie.command.input` |
| `2026-06-12 04:11:03` | `cowrie.command.success` |
| `2026-06-12 04:11:03` | `cowrie.log.closed` |
| `2026-06-12 04:11:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `114.33.12[.]13` to AbuseIPDB if not already reported
- [ ] Block `114.33.12[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8a1c607d63d7

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-06-12 04:19 |
| **Last Seen** | 2026-06-12 04:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 04:19:40` | `cowrie.session.connect` |
| `2026-06-12 04:19:40` | `cowrie.client.version` |
| `2026-06-12 04:19:40` | `cowrie.client.kex` |
| `2026-06-12 04:19:41` | `cowrie.login.success` |
| `2026-06-12 04:19:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-23884b7792b2

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-06-12 04:19 |
| **Last Seen** | 2026-06-12 04:19 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 04:19:40` | `cowrie.session.connect` |
| `2026-06-12 04:19:40` | `cowrie.client.version` |
| `2026-06-12 04:19:40` | `cowrie.client.kex` |
| `2026-06-12 04:19:40` | `cowrie.login.success` |
| `2026-06-12 04:19:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cb945331bc6f

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-06-12 04:19 |
| **Last Seen** | 2026-06-12 04:19 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 04:19:50` | `cowrie.session.connect` |
| `2026-06-12 04:19:50` | `cowrie.client.version` |
| `2026-06-12 04:19:50` | `cowrie.client.kex` |
| `2026-06-12 04:19:51` | `cowrie.login.success` |
| `2026-06-12 04:19:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-857ae320897c

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-06-12 04:19 |
| **Last Seen** | 2026-06-12 04:19 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 04:19:51` | `cowrie.session.connect` |
| `2026-06-12 04:19:51` | `cowrie.client.version` |
| `2026-06-12 04:19:51` | `cowrie.client.kex` |
| `2026-06-12 04:19:51` | `cowrie.login.success` |
| `2026-06-12 04:19:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ece81ad0fd8c

| Field | Detail |
|---|---|
| **Source IP** | `2.57.121[.]112` |
| **First Seen** | 2026-06-12 04:32 |
| **Last Seen** | 2026-06-12 04:32 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 04:32:07` | `cowrie.session.connect` |
| `2026-06-12 04:32:07` | `cowrie.client.version` |
| `2026-06-12 04:32:07` | `cowrie.client.kex` |
| `2026-06-12 04:32:08` | `cowrie.login.success` |
| `2026-06-12 04:32:08` | `cowrie.direct-tcpip.request` |
| `2026-06-12 04:32:08` | `cowrie.direct-tcpip.data` |
| `2026-06-12 04:32:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.121[.]112` to AbuseIPDB if not already reported
- [ ] Block `2.57.121[.]112` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `154.16.146[.]65` | **134** | 2026-06-12 02:55 | 2026-06-12 04:54 | 79m | 0 | `T1592` | 🟠 MEDIUM |
| `92.204.138[.]51` | **25** | 2026-06-12 02:59 | 2026-06-12 04:55 | 12m | 0 | `T1592` | 🟠 MEDIUM |
| `188.166.223[.]22` | **2** | 2026-06-12 04:46 | 2026-06-12 04:50 | 1m | 0 | `T1592` | 🟢 LOW |
| `20.65.193[.]19` | **2** | 2026-06-12 03:53 | 2026-06-12 03:53 | 0m | 0 | `T1592` | 🟢 LOW |
| `49.88.156[.]34` | **2** | 2026-06-12 04:50 | 2026-06-12 04:52 | 4m | 0 | `T1592` | 🟢 LOW |
| `114.138.102[.]104` | 1 | 2026-06-12 03:29 | 2026-06-12 03:29 | 12s | 0 | `T1592` | 🟢 LOW |
| `116.208.215[.]179` | 1 | 2026-06-12 03:50 | 2026-06-12 03:50 | 14s | 0 | `T1592` | 🟢 LOW |
| `159.65.233[.]253` | 1 | 2026-06-12 04:07 | 2026-06-12 04:08 | 32s | 0 | `T1592` | 🟢 LOW |
| `176.65.139[.]29` | 1 | 2026-06-12 03:01 | 2026-06-12 03:01 | 0s | 0 | `T1592` | 🟢 LOW |
| `193.176.31[.]205` | 1 | 2026-06-12 04:36 | 2026-06-12 04:36 | 0s | 0 | `T1592` | 🟢 LOW |
| `217.183.47[.]173` | 1 | 2026-06-12 04:35 | 2026-06-12 04:35 | 13s | 0 | `T1592` | 🟢 LOW |
| `45.179.163[.]47` | 1 | 2026-06-12 04:29 | 2026-06-12 04:30 | 30s | 0 | `T1592` | 🟢 LOW |
| `45.33.12[.]122` | 1 | 2026-06-12 04:48 | 2026-06-12 04:48 | 0s | 0 | `T1592` | 🟢 LOW |
| `69.164.217[.]74` | 1 | 2026-06-12 03:44 | 2026-06-12 03:44 | 0s | 0 | `T1592` | 🟢 LOW |
| `69.5.169[.]143` | 1 | 2026-06-12 03:38 | 2026-06-12 03:38 | 0s | 0 | `T1592` | 🟢 LOW |
| `69.5.169[.]240` | 1 | 2026-06-12 04:35 | 2026-06-12 04:35 | 0s | 0 | `T1592` | 🟢 LOW |
| `79.143.42[.]170` | 1 | 2026-06-12 04:05 | 2026-06-12 04:05 | 31s | 0 | `T1592` | 🟢 LOW |
| `81.19.216[.]119` | 1 | 2026-06-12 03:40 | 2026-06-12 03:40 | 10s | 0 | `T1592` | 🟢 LOW |
| `92.118.39[.]236` | 1 | 2026-06-12 04:07 | 2026-06-12 04:07 | 0s | 0 | `T1592` | 🟢 LOW |

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
| `129.153.145[.]135` | US | Oracle Corporation | **100** ⚠️ | 7 |
| `138.2.98[.]41` | SG | Oracle Corporation | **100** ⚠️ | 1 |
| `69.5.169[.]143` | DE | Infrawatch Limited | **100** ⚠️ | 12 |
| `144.22.238[.]238` | BR | Oracle Corporation | **100** ⚠️ | 2 |
| `176.65.139[.]29` | NL | Storm Industries | **100** ⚠️ | 7 |
| `154.16.146[.]65` | US | OC1-HostForWeb, LLC | **100** ⚠️ | 2 |
| `213.209.159[.]56` | DE | Feo Prest SRL | **100** ⚠️ | 50 |
| `81.19.216[.]119` | NL | Infrawatch Limited | **100** ⚠️ | 8 |
| `45.33.12[.]122` | US | Linode | **100** ⚠️ | 50 |
| `79.143.42[.]170` | UA | Telecommunication Company Vinteleport Ltd. | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 46 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 44 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 1 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 1 |

---

## 🔕 False Positive Summary (14 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 8 |
| AbuseIPDB score 16 below threshold 25 | 1 |
| AbuseIPDB score 21 below threshold 25 | 1 |
| AbuseIPDB score 4 below threshold 25 | 1 |
| AbuseIPDB score 5 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 2 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 237 cases |
| Tool 34  | Credential Extractor        | ✅ 44 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 8 fingerprints |
| Tool 36  | Command Clustering          | ✅ 4 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 38 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 14 filtered (5.9%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 22 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 35 files |
| Tool 33  | YARA Classifier             | ✅ 10 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 44 priority case(s) shown individually · 19 recon entry/entries in table (5 group(s) consolidating 165 session(s)).

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
_Report time: 2026-06-12T04:58:32Z_

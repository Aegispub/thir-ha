# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-06-17 |
| **Generated At** | 2026-06-17T15:43:25Z |
| **Shift Time** | 15:43 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **135** |
| Confirmed Threats | **108** |
| False Positives Filtered | **27** (20.0%) |
| Unique Attacker IPs | **61** |
| Countries of Origin | **19** |
| High Severity Cases | **50** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **85** |
| Malware Samples Analyzed | **1** HIGH · **15** MED · 1 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **51** |
| Unique Credential Pairs | **36** |
| Unique Usernames | **21** |
| Unique Passwords | **31** |
| Successful Auth Pairs | **41** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 17 |
| `sol` | 4 |
| `node` | 4 |
| `solv` | 4 |
| `admin` | 4 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `admin` | 5 |
| `smo@@kkklss` | 5 |
| `LeitboGi0ro` | 4 |
| `123@@@` | 4 |
| `ethereum` | 3 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `smo@@kkklss` | 5 |
| `root` | `LeitboGi0ro` | 4 |
| `root` | `123@@@` | 4 |
| `admin` | `admin` | 4 |
| `node` | `node` | 2 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `admin` | `45.135.194.15` | 2026-06-17T10:59:35 |
| `sol` | `sol` | `2.57.122.238` | 2026-06-17T11:09:52 |
| `solana` | `solana` | `2.57.122.238` | 2026-06-17T11:12:14 |
| `ethdocker` | `ethdocker` | `2.57.122.238` | 2026-06-17T11:14:27 |
| `eth-docker` | `eth-docker` | `2.57.122.238` | 2026-06-17T11:16:39 |
| `eth_docker` | `eth_docker` | `2.57.122.238` | 2026-06-17T11:18:50 |
| `raydium` | `raydium` | `2.57.122.238` | 2026-06-17T11:20:52 |
| `firedancer` | `firedancer` | `2.57.122.238` | 2026-06-17T11:22:58 |
| `node` | `node` | `2.57.122.238` | 2026-06-17T11:25:12 |
| `node` | `1234` | `2.57.122.238` | 2026-06-17T11:27:25 |
| `node` | `123456` | `2.57.122.238` | 2026-06-17T11:29:41 |
| `ethereum` | `ethereum` | `2.57.122.238` | 2026-06-17T11:31:57 |
| `eth` | `eth` | `2.57.122.238` | 2026-06-17T11:34:00 |
| `polygon` | `polygon` | `2.57.122.238` | 2026-06-17T11:36:11 |
| `root` | `LeitboGi0ro` | `144.22.238.238` | 2026-06-17T11:36:19 |
| `root` | `123@@@` | `144.22.238.238` | 2026-06-17T11:36:19 |
| `root` | `smo@@kkklss` | `144.22.238.238` | 2026-06-17T11:36:27 |
| `tron` | `tron` | `2.57.122.238` | 2026-06-17T11:38:23 |
| `trx` | `trx` | `2.57.122.238` | 2026-06-17T11:40:33 |
| `validator` | `ethereum` | `2.57.122.238` | 2026-06-17T11:42:54 |
| `sepolia` | `sepolia` | `2.57.122.238` | 2026-06-17T11:45:10 |
| `avalanche` | `avalanche` | `2.57.122.238` | 2026-06-17T11:47:20 |
| `solv` | `solv` | `2.57.122.238` | 2026-06-17T11:49:33 |
| `solv` | `1234` | `2.57.122.238` | 2026-06-17T11:51:44 |
| `solv` | `123456` | `2.57.122.238` | 2026-06-17T11:53:52 |
| `solv` | `12345678` | `2.57.122.238` | 2026-06-17T11:56:10 |
| `root` | `---fuck_you----` | `14.103.114.227` | 2026-06-17T11:59:21 |
| `ubuntu` | `ubuntu` | `2.57.122.238` | 2026-06-17T12:02:57 |
| `root` | `LeitboGi0ro` | `129.153.145.135` | 2026-06-17T12:03:20 |
| `root` | `123@@@` | `129.153.145.135` | 2026-06-17T12:03:20 |
| `root` | `smo@@kkklss` | `129.153.145.135` | 2026-06-17T12:03:29 |
| `validator` | `validator` | `2.57.122.238` | 2026-06-17T12:05:07 |
| `sol` | `sol123` | `2.57.122.238` | 2026-06-17T12:07:19 |
| `sol` | `123` | `2.57.122.238` | 2026-06-17T12:09:35 |
| `sol` | `12345678` | `2.57.122.238` | 2026-06-17T12:11:45 |
| `root` | `123@@@` | `64.110.90.250` | 2026-06-17T12:22:56 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-06-17T12:22:56 |
| `localadmin` | `localadmin` | `176.65.148.251` | 2026-06-17T12:42:30 |
| `admin` | `admin` | `10.0.0.73` | 2026-06-17T14:08:36 |
| `admin` | `admin` | `45.148.10.121` | 2026-06-17T14:19:48 |
| `root` | `﻿------fuck------` | `120.27.205.105` | 2026-06-17T14:30:08 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **135** |
| Sessions with Fingerprint | **10** |
| Unique HASSH Fingerprints | **10** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 41 |
| libssh | 14 |
| Paramiko (Python) | 13 |
| OpenSSH | 3 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `16443846184e...` | Generic scanner | 29 | 1 |
| `a2de0f306611...` | Mirai/variant | 13 | 3 |
| `bf7dbf67fa9b...` | Mirai/variant | 4 | 2 |
| `bc9e7273cde2...` | Mirai/variant | 3 | 3 |
| `98f63c4d9c87...` | Generic scanner | 3 | 3 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `16443846184e...` | Go SSH scanner | 29 | 1 | Generic scanner |
| `a2de0f306611...` | Paramiko (Python) | 13 | 3 | Mirai/variant |
| `95420f9d932d...` | libssh | 12 | 4 | — |
| `bf7dbf67fa9b...` | Go SSH scanner | 4 | 2 | Mirai/variant |
| `bc9e7273cde2...` | OpenSSH | 3 | 3 | Mirai/variant |
| `98f63c4d9c87...` | Go SSH scanner | 3 | 3 | Generic scanner |
| `084386fa7ae5...` | Go SSH scanner | 3 | 3 | Mirai/variant |
| `57e4cc8ee36c...` | libssh | 2 | 1 | Mirai/variant |

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
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1082, T1105, T1059.004` |

**🔴 HIGH · Mirai/IoT Botnet**

> Mirai-family IoT botnet. Executes busybox payloads for DDoS bot recruitment.

Representative commands:
```
echo SHELL_TEST
```
```
uname -h
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
Source IPs: `176.65.148.251`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **61** |
| Unique ASNs | **36** |
| High-Risk ASNs | **27** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS31898` | Oracle Corporation | 6 | HIGH |
| `AS25369` | Hydra Communications Ltd | 6 | HIGH |
| `AS4134` | CHINANET BACKBONE | 5 | HIGH |
| `AS63949` | Akamai Connected Cloud | 4 | HIGH |
| `AS209334` | Modat B.V. | 3 | HIGH |
| `AS4837` | CHINA UNICOM China169 Backbone | 2 | HIGH |
| `AS36352` | HostPapa | 2 | HIGH |
| `AS51396` | Pfcloud UG | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (48)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-a12dd8672a27

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]15` |
| **First Seen** | 2026-06-17 10:59 |
| **Last Seen** | 2026-06-17 10:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo [::loser::]` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-17 10:59:35` | `cowrie.session.connect` |
| `2026-06-17 10:59:35` | `cowrie.client.version` |
| `2026-06-17 10:59:35` | `cowrie.client.kex` |
| `2026-06-17 10:59:35` | `cowrie.login.success` |
| `2026-06-17 10:59:36` | `cowrie.session.params` |
| `2026-06-17 10:59:36` | `cowrie.command.input` |
| `2026-06-17 10:59:36` | `cowrie.log.closed` |
| `2026-06-17 10:59:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]15` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-857fb554e537

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-06-17 11:09 |
| **Last Seen** | 2026-06-17 11:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-17 11:09:51` | `cowrie.session.connect` |
| `2026-06-17 11:09:51` | `cowrie.client.version` |
| `2026-06-17 11:09:51` | `cowrie.client.kex` |
| `2026-06-17 11:09:52` | `cowrie.login.success` |
| `2026-06-17 11:09:52` | `cowrie.session.params` |
| `2026-06-17 11:09:52` | `cowrie.command.input` |
| `2026-06-17 11:09:52` | `cowrie.log.closed` |
| `2026-06-17 11:09:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e5ff4d24ca2a

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-06-17 11:12 |
| **Last Seen** | 2026-06-17 11:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-17 11:12:14` | `cowrie.session.connect` |
| `2026-06-17 11:12:14` | `cowrie.client.version` |
| `2026-06-17 11:12:14` | `cowrie.client.kex` |
| `2026-06-17 11:12:14` | `cowrie.login.success` |
| `2026-06-17 11:12:15` | `cowrie.session.params` |
| `2026-06-17 11:12:15` | `cowrie.command.input` |
| `2026-06-17 11:12:15` | `cowrie.log.closed` |
| `2026-06-17 11:12:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dd88b1c15710

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-06-17 11:14 |
| **Last Seen** | 2026-06-17 11:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-17 11:14:27` | `cowrie.session.connect` |
| `2026-06-17 11:14:27` | `cowrie.client.version` |
| `2026-06-17 11:14:27` | `cowrie.client.kex` |
| `2026-06-17 11:14:27` | `cowrie.login.success` |
| `2026-06-17 11:14:28` | `cowrie.session.params` |
| `2026-06-17 11:14:28` | `cowrie.command.input` |
| `2026-06-17 11:14:28` | `cowrie.log.closed` |
| `2026-06-17 11:14:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a1a0b24271a7

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-06-17 11:16 |
| **Last Seen** | 2026-06-17 11:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-17 11:16:39` | `cowrie.session.connect` |
| `2026-06-17 11:16:39` | `cowrie.client.version` |
| `2026-06-17 11:16:39` | `cowrie.client.kex` |
| `2026-06-17 11:16:39` | `cowrie.login.success` |
| `2026-06-17 11:16:40` | `cowrie.session.params` |
| `2026-06-17 11:16:40` | `cowrie.command.input` |
| `2026-06-17 11:16:40` | `cowrie.log.closed` |
| `2026-06-17 11:16:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-57ad590f69ba

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-06-17 11:18 |
| **Last Seen** | 2026-06-17 11:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-17 11:18:49` | `cowrie.session.connect` |
| `2026-06-17 11:18:49` | `cowrie.client.version` |
| `2026-06-17 11:18:49` | `cowrie.client.kex` |
| `2026-06-17 11:18:50` | `cowrie.login.success` |
| `2026-06-17 11:18:51` | `cowrie.session.params` |
| `2026-06-17 11:18:51` | `cowrie.command.input` |
| `2026-06-17 11:18:51` | `cowrie.log.closed` |
| `2026-06-17 11:18:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-26e56fe4da5a

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-06-17 11:20 |
| **Last Seen** | 2026-06-17 11:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-17 11:20:51` | `cowrie.session.connect` |
| `2026-06-17 11:20:51` | `cowrie.client.version` |
| `2026-06-17 11:20:51` | `cowrie.client.kex` |
| `2026-06-17 11:20:52` | `cowrie.login.success` |
| `2026-06-17 11:20:53` | `cowrie.session.params` |
| `2026-06-17 11:20:53` | `cowrie.command.input` |
| `2026-06-17 11:20:53` | `cowrie.log.closed` |
| `2026-06-17 11:20:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f5548485b896

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-06-17 11:22 |
| **Last Seen** | 2026-06-17 11:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-17 11:22:58` | `cowrie.session.connect` |
| `2026-06-17 11:22:58` | `cowrie.client.version` |
| `2026-06-17 11:22:58` | `cowrie.client.kex` |
| `2026-06-17 11:22:58` | `cowrie.login.success` |
| `2026-06-17 11:22:59` | `cowrie.session.params` |
| `2026-06-17 11:22:59` | `cowrie.command.input` |
| `2026-06-17 11:22:59` | `cowrie.log.closed` |
| `2026-06-17 11:22:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d0e8bba42670

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-06-17 11:25 |
| **Last Seen** | 2026-06-17 11:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-17 11:25:12` | `cowrie.session.connect` |
| `2026-06-17 11:25:12` | `cowrie.client.version` |
| `2026-06-17 11:25:12` | `cowrie.client.kex` |
| `2026-06-17 11:25:12` | `cowrie.login.success` |
| `2026-06-17 11:25:13` | `cowrie.session.params` |
| `2026-06-17 11:25:13` | `cowrie.command.input` |
| `2026-06-17 11:25:13` | `cowrie.log.closed` |
| `2026-06-17 11:25:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1f030f1b6f21

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-06-17 11:27 |
| **Last Seen** | 2026-06-17 11:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-17 11:27:25` | `cowrie.session.connect` |
| `2026-06-17 11:27:25` | `cowrie.client.version` |
| `2026-06-17 11:27:25` | `cowrie.client.kex` |
| `2026-06-17 11:27:25` | `cowrie.login.success` |
| `2026-06-17 11:27:26` | `cowrie.session.params` |
| `2026-06-17 11:27:26` | `cowrie.command.input` |
| `2026-06-17 11:27:26` | `cowrie.log.closed` |
| `2026-06-17 11:27:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0302e58647e9

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-06-17 11:29 |
| **Last Seen** | 2026-06-17 11:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-17 11:29:41` | `cowrie.session.connect` |
| `2026-06-17 11:29:41` | `cowrie.client.version` |
| `2026-06-17 11:29:41` | `cowrie.client.kex` |
| `2026-06-17 11:29:41` | `cowrie.login.success` |
| `2026-06-17 11:29:42` | `cowrie.session.params` |
| `2026-06-17 11:29:42` | `cowrie.command.input` |
| `2026-06-17 11:29:42` | `cowrie.log.closed` |
| `2026-06-17 11:29:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fb15e64dc903

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-06-17 11:31 |
| **Last Seen** | 2026-06-17 11:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-17 11:31:57` | `cowrie.session.connect` |
| `2026-06-17 11:31:57` | `cowrie.client.version` |
| `2026-06-17 11:31:57` | `cowrie.client.kex` |
| `2026-06-17 11:31:57` | `cowrie.login.success` |
| `2026-06-17 11:31:58` | `cowrie.session.params` |
| `2026-06-17 11:31:58` | `cowrie.command.input` |
| `2026-06-17 11:31:58` | `cowrie.log.closed` |
| `2026-06-17 11:31:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1339495187c0

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-06-17 11:34 |
| **Last Seen** | 2026-06-17 11:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-17 11:34:00` | `cowrie.session.connect` |
| `2026-06-17 11:34:00` | `cowrie.client.version` |
| `2026-06-17 11:34:00` | `cowrie.client.kex` |
| `2026-06-17 11:34:00` | `cowrie.login.success` |
| `2026-06-17 11:34:01` | `cowrie.session.params` |
| `2026-06-17 11:34:01` | `cowrie.command.input` |
| `2026-06-17 11:34:01` | `cowrie.log.closed` |
| `2026-06-17 11:34:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e1c8e8657ca1

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-06-17 11:36 |
| **Last Seen** | 2026-06-17 11:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-17 11:36:10` | `cowrie.session.connect` |
| `2026-06-17 11:36:10` | `cowrie.client.version` |
| `2026-06-17 11:36:10` | `cowrie.client.kex` |
| `2026-06-17 11:36:11` | `cowrie.login.success` |
| `2026-06-17 11:36:12` | `cowrie.session.params` |
| `2026-06-17 11:36:12` | `cowrie.command.input` |
| `2026-06-17 11:36:12` | `cowrie.log.closed` |
| `2026-06-17 11:36:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c4915cfb1256

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-06-17 11:36 |
| **Last Seen** | 2026-06-17 11:36 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-17 11:36:18` | `cowrie.session.connect` |
| `2026-06-17 11:36:18` | `cowrie.client.version` |
| `2026-06-17 11:36:18` | `cowrie.client.kex` |
| `2026-06-17 11:36:19` | `cowrie.login.success` |
| `2026-06-17 11:36:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dcbe22409ccb

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-06-17 11:36 |
| **Last Seen** | 2026-06-17 11:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-17 11:36:18` | `cowrie.session.connect` |
| `2026-06-17 11:36:18` | `cowrie.client.version` |
| `2026-06-17 11:36:18` | `cowrie.client.kex` |
| `2026-06-17 11:36:19` | `cowrie.login.success` |
| `2026-06-17 11:36:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cfaa9b45400b

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-06-17 11:36 |
| **Last Seen** | 2026-06-17 11:36 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-17 11:36:27` | `cowrie.session.connect` |
| `2026-06-17 11:36:27` | `cowrie.client.version` |
| `2026-06-17 11:36:27` | `cowrie.client.kex` |
| `2026-06-17 11:36:27` | `cowrie.login.success` |
| `2026-06-17 11:36:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0fc90852131a

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-06-17 11:36 |
| **Last Seen** | 2026-06-17 11:36 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-17 11:36:28` | `cowrie.session.connect` |
| `2026-06-17 11:36:28` | `cowrie.client.version` |
| `2026-06-17 11:36:28` | `cowrie.client.kex` |
| `2026-06-17 11:36:28` | `cowrie.login.success` |
| `2026-06-17 11:36:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c3023ec110ec

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-06-17 11:38 |
| **Last Seen** | 2026-06-17 11:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-17 11:38:23` | `cowrie.session.connect` |
| `2026-06-17 11:38:23` | `cowrie.client.version` |
| `2026-06-17 11:38:23` | `cowrie.client.kex` |
| `2026-06-17 11:38:23` | `cowrie.login.success` |
| `2026-06-17 11:38:24` | `cowrie.session.params` |
| `2026-06-17 11:38:24` | `cowrie.command.input` |
| `2026-06-17 11:38:24` | `cowrie.log.closed` |
| `2026-06-17 11:38:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7bfaf623dab3

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-06-17 11:40 |
| **Last Seen** | 2026-06-17 11:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-17 11:40:33` | `cowrie.session.connect` |
| `2026-06-17 11:40:33` | `cowrie.client.version` |
| `2026-06-17 11:40:33` | `cowrie.client.kex` |
| `2026-06-17 11:40:33` | `cowrie.login.success` |
| `2026-06-17 11:40:34` | `cowrie.session.params` |
| `2026-06-17 11:40:34` | `cowrie.command.input` |
| `2026-06-17 11:40:34` | `cowrie.log.closed` |
| `2026-06-17 11:40:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3ebb648eac70

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-06-17 11:42 |
| **Last Seen** | 2026-06-17 11:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-17 11:42:54` | `cowrie.session.connect` |
| `2026-06-17 11:42:54` | `cowrie.client.version` |
| `2026-06-17 11:42:54` | `cowrie.client.kex` |
| `2026-06-17 11:42:54` | `cowrie.login.success` |
| `2026-06-17 11:42:55` | `cowrie.session.params` |
| `2026-06-17 11:42:55` | `cowrie.command.input` |
| `2026-06-17 11:42:55` | `cowrie.log.closed` |
| `2026-06-17 11:42:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b06bee8b5d27

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-06-17 11:45 |
| **Last Seen** | 2026-06-17 11:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-17 11:45:10` | `cowrie.session.connect` |
| `2026-06-17 11:45:10` | `cowrie.client.version` |
| `2026-06-17 11:45:10` | `cowrie.client.kex` |
| `2026-06-17 11:45:10` | `cowrie.login.success` |
| `2026-06-17 11:45:11` | `cowrie.session.params` |
| `2026-06-17 11:45:11` | `cowrie.command.input` |
| `2026-06-17 11:45:11` | `cowrie.log.closed` |
| `2026-06-17 11:45:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6729e99b3b22

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-06-17 11:47 |
| **Last Seen** | 2026-06-17 11:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-17 11:47:20` | `cowrie.session.connect` |
| `2026-06-17 11:47:20` | `cowrie.client.version` |
| `2026-06-17 11:47:20` | `cowrie.client.kex` |
| `2026-06-17 11:47:20` | `cowrie.login.success` |
| `2026-06-17 11:47:21` | `cowrie.session.params` |
| `2026-06-17 11:47:21` | `cowrie.command.input` |
| `2026-06-17 11:47:21` | `cowrie.log.closed` |
| `2026-06-17 11:47:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6142fa01d442

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-06-17 11:49 |
| **Last Seen** | 2026-06-17 11:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-17 11:49:32` | `cowrie.session.connect` |
| `2026-06-17 11:49:32` | `cowrie.client.version` |
| `2026-06-17 11:49:32` | `cowrie.client.kex` |
| `2026-06-17 11:49:33` | `cowrie.login.success` |
| `2026-06-17 11:49:33` | `cowrie.session.params` |
| `2026-06-17 11:49:33` | `cowrie.command.input` |
| `2026-06-17 11:49:34` | `cowrie.log.closed` |
| `2026-06-17 11:49:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-24a1e235045c

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-06-17 11:51 |
| **Last Seen** | 2026-06-17 11:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-17 11:51:43` | `cowrie.session.connect` |
| `2026-06-17 11:51:43` | `cowrie.client.version` |
| `2026-06-17 11:51:43` | `cowrie.client.kex` |
| `2026-06-17 11:51:44` | `cowrie.login.success` |
| `2026-06-17 11:51:44` | `cowrie.session.params` |
| `2026-06-17 11:51:44` | `cowrie.command.input` |
| `2026-06-17 11:51:45` | `cowrie.log.closed` |
| `2026-06-17 11:51:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ca1048b3643f

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-06-17 11:53 |
| **Last Seen** | 2026-06-17 11:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-17 11:53:52` | `cowrie.session.connect` |
| `2026-06-17 11:53:52` | `cowrie.client.version` |
| `2026-06-17 11:53:52` | `cowrie.client.kex` |
| `2026-06-17 11:53:52` | `cowrie.login.success` |
| `2026-06-17 11:53:53` | `cowrie.session.params` |
| `2026-06-17 11:53:53` | `cowrie.command.input` |
| `2026-06-17 11:53:53` | `cowrie.log.closed` |
| `2026-06-17 11:53:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-efd43a0fd84e

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-06-17 11:56 |
| **Last Seen** | 2026-06-17 11:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-17 11:56:09` | `cowrie.session.connect` |
| `2026-06-17 11:56:09` | `cowrie.client.version` |
| `2026-06-17 11:56:09` | `cowrie.client.kex` |
| `2026-06-17 11:56:10` | `cowrie.login.success` |
| `2026-06-17 11:56:10` | `cowrie.session.params` |
| `2026-06-17 11:56:10` | `cowrie.command.input` |
| `2026-06-17 11:56:11` | `cowrie.log.closed` |
| `2026-06-17 11:56:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3c67d61a5f6d

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-06-17 11:58 |
| **Last Seen** | 2026-06-17 11:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-17 11:58:25` | `cowrie.session.connect` |
| `2026-06-17 11:58:25` | `cowrie.client.version` |
| `2026-06-17 11:58:25` | `cowrie.client.kex` |
| `2026-06-17 11:58:25` | `cowrie.login.success` |
| `2026-06-17 11:58:26` | `cowrie.session.params` |
| `2026-06-17 11:58:26` | `cowrie.command.input` |
| `2026-06-17 11:58:26` | `cowrie.log.closed` |
| `2026-06-17 11:58:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a1d2a1492816

| Field | Detail |
|---|---|
| **Source IP** | `14.103.114[.]227` |
| **First Seen** | 2026-06-17 11:59 |
| **Last Seen** | 2026-06-17 12:04 |
| **Session Duration** | 304s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-17 11:59:17` | `cowrie.session.connect` |
| `2026-06-17 11:59:18` | `cowrie.client.version` |
| `2026-06-17 11:59:18` | `cowrie.client.kex` |
| `2026-06-17 11:59:21` | `cowrie.login.success` |
| `2026-06-17 12:04:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.114[.]227` to AbuseIPDB if not already reported
- [ ] Block `14.103.114[.]227` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-05b0e3c9d73d

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-06-17 12:00 |
| **Last Seen** | 2026-06-17 12:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-17 12:00:39` | `cowrie.session.connect` |
| `2026-06-17 12:00:39` | `cowrie.client.version` |
| `2026-06-17 12:00:39` | `cowrie.client.kex` |
| `2026-06-17 12:00:40` | `cowrie.login.success` |
| `2026-06-17 12:00:41` | `cowrie.session.params` |
| `2026-06-17 12:00:41` | `cowrie.command.input` |
| `2026-06-17 12:00:41` | `cowrie.log.closed` |
| `2026-06-17 12:00:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-af7eca4ee64d

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-06-17 12:02 |
| **Last Seen** | 2026-06-17 12:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-17 12:02:56` | `cowrie.session.connect` |
| `2026-06-17 12:02:56` | `cowrie.client.version` |
| `2026-06-17 12:02:57` | `cowrie.client.kex` |
| `2026-06-17 12:02:57` | `cowrie.login.success` |
| `2026-06-17 12:02:58` | `cowrie.session.params` |
| `2026-06-17 12:02:58` | `cowrie.command.input` |
| `2026-06-17 12:02:58` | `cowrie.log.closed` |
| `2026-06-17 12:02:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f50cbcb7bf18

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-17 12:03 |
| **Last Seen** | 2026-06-17 12:03 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-17 12:03:20` | `cowrie.session.connect` |
| `2026-06-17 12:03:20` | `cowrie.client.version` |
| `2026-06-17 12:03:20` | `cowrie.client.kex` |
| `2026-06-17 12:03:20` | `cowrie.login.success` |
| `2026-06-17 12:03:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bb571423afae

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-17 12:03 |
| **Last Seen** | 2026-06-17 12:03 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-17 12:03:20` | `cowrie.session.connect` |
| `2026-06-17 12:03:20` | `cowrie.client.version` |
| `2026-06-17 12:03:20` | `cowrie.client.kex` |
| `2026-06-17 12:03:20` | `cowrie.login.success` |
| `2026-06-17 12:03:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b05b76a30a0f

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-17 12:03 |
| **Last Seen** | 2026-06-17 12:03 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-17 12:03:29` | `cowrie.session.connect` |
| `2026-06-17 12:03:29` | `cowrie.client.version` |
| `2026-06-17 12:03:29` | `cowrie.client.kex` |
| `2026-06-17 12:03:29` | `cowrie.login.success` |
| `2026-06-17 12:03:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c50b71841359

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-17 12:03 |
| **Last Seen** | 2026-06-17 12:03 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-17 12:03:29` | `cowrie.session.connect` |
| `2026-06-17 12:03:29` | `cowrie.client.version` |
| `2026-06-17 12:03:29` | `cowrie.client.kex` |
| `2026-06-17 12:03:29` | `cowrie.login.success` |
| `2026-06-17 12:03:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-de9b1aac2326

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-06-17 12:05 |
| **Last Seen** | 2026-06-17 12:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-17 12:05:07` | `cowrie.session.connect` |
| `2026-06-17 12:05:07` | `cowrie.client.version` |
| `2026-06-17 12:05:07` | `cowrie.client.kex` |
| `2026-06-17 12:05:07` | `cowrie.login.success` |
| `2026-06-17 12:05:08` | `cowrie.session.params` |
| `2026-06-17 12:05:08` | `cowrie.command.input` |
| `2026-06-17 12:05:08` | `cowrie.log.closed` |
| `2026-06-17 12:05:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6628f718496b

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-06-17 12:07 |
| **Last Seen** | 2026-06-17 12:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-17 12:07:18` | `cowrie.session.connect` |
| `2026-06-17 12:07:18` | `cowrie.client.version` |
| `2026-06-17 12:07:18` | `cowrie.client.kex` |
| `2026-06-17 12:07:19` | `cowrie.login.success` |
| `2026-06-17 12:07:20` | `cowrie.session.params` |
| `2026-06-17 12:07:20` | `cowrie.command.input` |
| `2026-06-17 12:07:20` | `cowrie.log.closed` |
| `2026-06-17 12:07:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dbedb95485fc

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-06-17 12:09 |
| **Last Seen** | 2026-06-17 12:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-17 12:09:34` | `cowrie.session.connect` |
| `2026-06-17 12:09:34` | `cowrie.client.version` |
| `2026-06-17 12:09:34` | `cowrie.client.kex` |
| `2026-06-17 12:09:35` | `cowrie.login.success` |
| `2026-06-17 12:09:35` | `cowrie.session.params` |
| `2026-06-17 12:09:35` | `cowrie.command.input` |
| `2026-06-17 12:09:35` | `cowrie.log.closed` |
| `2026-06-17 12:09:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bdc44a463e9b

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-06-17 12:11 |
| **Last Seen** | 2026-06-17 12:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-17 12:11:45` | `cowrie.session.connect` |
| `2026-06-17 12:11:45` | `cowrie.client.version` |
| `2026-06-17 12:11:45` | `cowrie.client.kex` |
| `2026-06-17 12:11:45` | `cowrie.login.success` |
| `2026-06-17 12:11:46` | `cowrie.session.params` |
| `2026-06-17 12:11:46` | `cowrie.command.input` |
| `2026-06-17 12:11:46` | `cowrie.log.closed` |
| `2026-06-17 12:11:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-db7780314ebc

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-06-17 12:22 |
| **Last Seen** | 2026-06-17 12:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-17 12:22:55` | `cowrie.session.connect` |
| `2026-06-17 12:22:55` | `cowrie.client.version` |
| `2026-06-17 12:22:55` | `cowrie.client.kex` |
| `2026-06-17 12:22:56` | `cowrie.login.success` |
| `2026-06-17 12:22:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-54a88664b8ab

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-06-17 12:22 |
| **Last Seen** | 2026-06-17 12:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-17 12:22:55` | `cowrie.session.connect` |
| `2026-06-17 12:22:55` | `cowrie.client.version` |
| `2026-06-17 12:22:55` | `cowrie.client.kex` |
| `2026-06-17 12:22:56` | `cowrie.login.success` |
| `2026-06-17 12:22:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-727499c1e6ac

| Field | Detail |
|---|---|
| **Source IP** | `176.65.148[.]251` |
| **First Seen** | 2026-06-17 12:42 |
| **Last Seen** | 2026-06-17 12:42 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST, uname -h, /bin/busybox TEST, cat /proc, ./` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-17 12:42:28` | `cowrie.session.connect` |
| `2026-06-17 12:42:30` | `cowrie.login.success` |
| `2026-06-17 12:42:31` | `cowrie.session.params` |
| `2026-06-17 12:42:31` | `cowrie.command.input` |
| `2026-06-17 12:42:32` | `cowrie.command.input` |
| `2026-06-17 12:42:33` | `cowrie.command.input` |
| `2026-06-17 12:42:34` | `cowrie.command.input` |
| `2026-06-17 12:42:35` | `cowrie.command.input` |
| `2026-06-17 12:42:35` | `cowrie.command.failed` |
| `2026-06-17 12:42:35` | `cowrie.log.closed` |
| `2026-06-17 12:42:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.148[.]251` to AbuseIPDB if not already reported
- [ ] Block `176.65.148[.]251` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4f1482a75f4b

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-06-17 12:53 |
| **Last Seen** | 2026-06-17 12:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-17 12:53:29` | `cowrie.session.connect` |
| `2026-06-17 12:53:29` | `cowrie.client.version` |
| `2026-06-17 12:53:29` | `cowrie.client.kex` |
| `2026-06-17 12:53:30` | `cowrie.login.success` |
| `2026-06-17 12:53:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-967904a5526b

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-06-17 12:53 |
| **Last Seen** | 2026-06-17 12:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-17 12:53:29` | `cowrie.session.connect` |
| `2026-06-17 12:53:29` | `cowrie.client.version` |
| `2026-06-17 12:53:29` | `cowrie.client.kex` |
| `2026-06-17 12:53:30` | `cowrie.login.success` |
| `2026-06-17 12:53:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-edd156e01b35

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-06-17 12:53 |
| **Last Seen** | 2026-06-17 12:53 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-17 12:53:40` | `cowrie.session.connect` |
| `2026-06-17 12:53:40` | `cowrie.client.version` |
| `2026-06-17 12:53:40` | `cowrie.client.kex` |
| `2026-06-17 12:53:41` | `cowrie.login.success` |
| `2026-06-17 12:53:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-db825f55e130

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]121` |
| **First Seen** | 2026-06-17 14:19 |
| **Last Seen** | 2026-06-17 14:19 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-17 14:19:47` | `cowrie.session.connect` |
| `2026-06-17 14:19:47` | `cowrie.client.version` |
| `2026-06-17 14:19:47` | `cowrie.client.kex` |
| `2026-06-17 14:19:48` | `cowrie.login.success` |
| `2026-06-17 14:19:48` | `cowrie.direct-tcpip.request` |
| `2026-06-17 14:19:48` | `cowrie.direct-tcpip.ja4h` |
| `2026-06-17 14:19:48` | `cowrie.direct-tcpip.data` |
| `2026-06-17 14:19:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]121` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]121` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1cc32a0725f3

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]121` |
| **First Seen** | 2026-06-17 14:19 |
| **Last Seen** | 2026-06-17 14:19 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-17 14:19:48` | `cowrie.session.connect` |
| `2026-06-17 14:19:48` | `cowrie.client.version` |
| `2026-06-17 14:19:48` | `cowrie.client.kex` |
| `2026-06-17 14:19:48` | `cowrie.login.success` |
| `2026-06-17 14:19:49` | `cowrie.direct-tcpip.request` |
| `2026-06-17 14:19:49` | `cowrie.direct-tcpip.ja4h` |
| `2026-06-17 14:19:49` | `cowrie.direct-tcpip.data` |
| `2026-06-17 14:19:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]121` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]121` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-baaf7f8d8017

| Field | Detail |
|---|---|
| **Source IP** | `120.27.205[.]105` |
| **First Seen** | 2026-06-17 14:30 |
| **Last Seen** | 2026-06-17 14:30 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-17 14:30:05` | `cowrie.session.connect` |
| `2026-06-17 14:30:05` | `cowrie.client.version` |
| `2026-06-17 14:30:06` | `cowrie.client.kex` |
| `2026-06-17 14:30:08` | `cowrie.login.success` |
| `2026-06-17 14:30:10` | `cowrie.session.params` |
| `2026-06-17 14:30:10` | `cowrie.command.input` |
| `2026-06-17 14:30:11` | `cowrie.log.closed` |
| `2026-06-17 14:30:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.27.205[.]105` to AbuseIPDB if not already reported
- [ ] Block `120.27.205[.]105` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `154.16.146[.]65` | **6** | 2026-06-17 11:35 | 2026-06-17 14:37 | 2m | 0 | `T1592` | 🟢 LOW |
| `183.91.11[.]226` | **4** | 2026-06-17 11:14 | 2026-06-17 11:29 | 2m | 0 | `T1592` | 🟢 LOW |
| `20.55.50[.]10` | **2** | 2026-06-17 14:07 | 2026-06-17 14:07 | 0m | 0 | `T1592` | 🟢 LOW |
| `3.131.220[.]121` | **2** | 2026-06-17 14:34 | 2026-06-17 14:35 | 0m | 0 | `T1592` | 🟢 LOW |
| `39.152.240[.]15` | **2** | 2026-06-17 13:35 | 2026-06-17 13:37 | 2m | 0 | `T1592` | 🟢 LOW |
| `45.135.194[.]15` | **2** | 2026-06-17 10:59 | 2026-06-17 10:59 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `45.148.10[.]121` | **2** | 2026-06-17 13:56 | 2026-06-17 14:01 | 0m | 0 | `T1592` | 🟢 LOW |
| `107.172.87[.]21` | 1 | 2026-06-17 13:05 | 2026-06-17 13:06 | 30s | 0 | `T1592` | 🟢 LOW |
| `119.99.250[.]142` | 1 | 2026-06-17 13:13 | 2026-06-17 13:13 | 13s | 0 | `T1592` | 🟢 LOW |
| `138.2.20[.]68` | 1 | 2026-06-17 12:50 | 2026-06-17 12:50 | 30s | 0 | `T1592` | 🟢 LOW |
| `138.204.196[.]164` | 1 | 2026-06-17 12:03 | 2026-06-17 12:03 | 14s | 0 | `T1592` | 🟢 LOW |
| `14.103.114[.]227` | 1 | 2026-06-17 11:59 | 2026-06-17 11:59 | 0s | 0 | `T1592` | 🟢 LOW |
| `159.65.233[.]253` | 1 | 2026-06-17 11:53 | 2026-06-17 11:55 | 120s | 0 | `T1592` | 🟢 LOW |
| `171.109.111[.]69` | 1 | 2026-06-17 11:40 | 2026-06-17 11:40 | 0s | 0 | `T1592` | 🟢 LOW |
| `172.104.93[.]159` | 1 | 2026-06-17 12:01 | 2026-06-17 12:02 | 10s | 0 | `T1592` | 🟢 LOW |
| `172.245.123[.]75` | 1 | 2026-06-17 12:16 | 2026-06-17 12:16 | 31s | 0 | `T1592` | 🟢 LOW |
| `176.65.148[.]251` | 1 | 2026-06-17 12:42 | 2026-06-17 12:42 | 0s | 0 | `T1592` | 🟢 LOW |
| `18.116.101[.]220` | 1 | 2026-06-17 11:22 | 2026-06-17 11:22 | 0s | 0 | `T1592` | 🟢 LOW |
| `188.166.223[.]22` | 1 | 2026-06-17 11:34 | 2026-06-17 11:35 | 34s | 0 | `T1592` | 🟢 LOW |
| `193.176.31[.]201` | 1 | 2026-06-17 12:10 | 2026-06-17 12:10 | 10s | 0 | `T1592` | 🟢 LOW |
| `197.232.46[.]79` | 1 | 2026-06-17 13:04 | 2026-06-17 13:04 | 12s | 0 | `T1592` | 🟢 LOW |
| `2.57.122[.]238` | 1 | 2026-06-17 11:07 | 2026-06-17 11:07 | 0s | 0 | `T1592` | 🟢 LOW |
| `223.242.1[.]240` | 1 | 2026-06-17 11:55 | 2026-06-17 11:55 | 32s | 0 | `T1592` | 🟢 LOW |
| `23.141.52[.]197` | 1 | 2026-06-17 14:18 | 2026-06-17 14:19 | 30s | 0 | `T1592` | 🟢 LOW |
| `35.212.223[.]172` | 1 | 2026-06-17 13:23 | 2026-06-17 13:23 | 31s | 0 | `T1592` | 🟢 LOW |
| `37.46.245[.]126` | 1 | 2026-06-17 11:29 | 2026-06-17 11:29 | 12s | 0 | `T1592` | 🟢 LOW |
| `37.63.88[.]203` | 1 | 2026-06-17 11:46 | 2026-06-17 11:46 | 13s | 0 | `T1592` | 🟢 LOW |
| `45.33.14[.]5` | 1 | 2026-06-17 14:36 | 2026-06-17 14:36 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.207[.]181` | 1 | 2026-06-17 13:36 | 2026-06-17 13:36 | 3s | 0 | `T1592` | 🟢 LOW |
| `47.242.247[.]176` | 1 | 2026-06-17 13:08 | 2026-06-17 13:09 | 30s | 0 | `T1592` | 🟢 LOW |
| `59.55.66[.]192` | 1 | 2026-06-17 13:59 | 2026-06-17 14:00 | 31s | 0 | `T1592` | 🟢 LOW |
| `61.137.140[.]246` | 1 | 2026-06-17 13:03 | 2026-06-17 13:03 | 13s | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]221` | 1 | 2026-06-17 12:49 | 2026-06-17 12:49 | 15s | 0 | `T1592` | 🟢 LOW |
| `66.240.236[.]116` | 1 | 2026-06-17 14:54 | 2026-06-17 14:54 | 10s | 0 | `T1592` | 🟢 LOW |
| `69.5.169[.]222` | 1 | 2026-06-17 11:55 | 2026-06-17 11:55 | 0s | 0 | `T1592` | 🟢 LOW |
| `69.5.169[.]238` | 1 | 2026-06-17 12:06 | 2026-06-17 12:06 | 0s | 0 | `T1592` | 🟢 LOW |
| `69.5.169[.]239` | 1 | 2026-06-17 12:27 | 2026-06-17 12:27 | 0s | 0 | `T1592` | 🟢 LOW |
| `71.6.199[.]87` | 1 | 2026-06-17 13:22 | 2026-06-17 13:22 | 10s | 0 | `T1592` | 🟢 LOW |
| `81.19.216[.]116` | 1 | 2026-06-17 12:31 | 2026-06-17 12:31 | 0s | 0 | `T1592` | 🟢 LOW |
| `81.19.216[.]98` | 1 | 2026-06-17 11:59 | 2026-06-17 11:59 | 0s | 0 | `T1592` | 🟢 LOW |
| `84.8.155[.]112` | 1 | 2026-06-17 14:14 | 2026-06-17 14:14 | 30s | 0 | `T1592` | 🟢 LOW |
| `84.8.249[.]210` | 1 | 2026-06-17 12:28 | 2026-06-17 12:29 | 30s | 0 | `T1592` | 🟢 LOW |
| `85.217.149[.]29` | 1 | 2026-06-17 11:07 | 2026-06-17 11:07 | 0s | 0 | `T1592` | 🟢 LOW |
| `85.217.149[.]6` | 1 | 2026-06-17 11:12 | 2026-06-17 11:12 | 0s | 0 | `T1592` | 🟢 LOW |
| `85.217.149[.]70` | 1 | 2026-06-17 14:14 | 2026-06-17 14:14 | 0s | 0 | `T1592` | 🟢 LOW |
| `91.92.40[.]18` | 1 | 2026-06-17 14:25 | 2026-06-17 14:26 | 29s | 0 | `T1592` | 🟢 LOW |
| `98.213.174[.]120` | 1 | 2026-06-17 11:25 | 2026-06-17 11:26 | 31s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (17 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **13/75** 🔴 |
| `2a39d592018600e4b3db2caed6cdaa8c651d3dacbebf8ac1f0960e493843c435` | ELF Binary (Linux executable) (x86-64 64-bit) | `2a39d592018600e4...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `3625cfdcd6d434bfa672753ef4b197df8a01388d220bafc9edfa2d0d29c7fcef` | ELF Binary (Linux executable) (x86-64 64-bit) | `3625cfdcd6d434bf...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `3625d068896953595e75df328676a08bc071977ac1ff95d44b745bbcb7018c6f` | ELF Binary (Linux executable) (ARM 32-bit) | `3625d06889695359...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `59c29436755b0778e968d49feeae20ed65f5fa5e35f9f7965b8ed93420db91e5` | ELF Binary (Linux executable) (x86-64 64-bit) | `59c29436755b0778...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `75737a0d2987fb60d7a1f17ff2a7122132545e84a327e3a5372be51500a3be12` | ELF Binary (Linux executable) (x86-64 64-bit) | `75737a0d2987fb60...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `765289f938cc2bd64c9778dbabe048afa8ac3277a150c940d2730c14d24687b5` | ELF Binary (Linux executable) (x86-64 64-bit) | `765289f938cc2bd6...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `783adb7ad6b16fe9818f3e6d48b937c3ca1994ef24e50865282eeedeab7e0d59` | Bash Script | `783adb7ad6b16fe9...` | 61/100 | 🟡 MEDIUM | **28/75** 🔴 |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `b1e4374da060cb4bf9ff872f3e060486d9cd400519e0b2823f61670d64148ab4` | ELF Binary (Linux executable) (x86-64 64-bit) | `b1e4374da060cb4b...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `b20f39fc00d242e706b6c30367ad811c676e0575050a4ec2f30104b696944b49` | ELF Binary (Linux executable) (x86-64 64-bit) | `b20f39fc00d242e7...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `d46555af1173d22f07c37ef9c1e0e74fd68db022f2b6fb3ab5388d2c5bc6a98e` | Bash Script | `d46555af1173d22f...` | 70/100 | 🔴 HIGH | **26/75** 🔴 |
| `dbb7ebb960dc0d5a480f97ddde3a227a2d83fcaca7d37ae672e6a0a6785631e9` | ELF Binary (Linux executable) (AArch64 64-bit) | `dbb7ebb960dc0d5a...` | 43/100 | 🟡 MEDIUM | **33/75** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `ea73a088909b53110444807188562c406c6c6c89b3748aee016bc996ab1f1318` | Unknown binary | `ea73a088909b5311...` | 55/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `eaf9adb4bb80316a3aafceabc0f2ed2aed7c76cf134b9b7c66226fc4f003aa97` | ELF Binary (Linux executable) (x86-64 64-bit) | `eaf9adb4bb80316a...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |

**Suspicious Indicators — HIGH Severity Samples:**

_`d46555af1173d22f07c37ef9c1e0e74fd68db022f2b6fb3ab5388d2c5bc6a98e` (d46555af1173d22f07c37ef9...)_
- `Execution from /tmp` — `/tmp/clean_crontab`
- `Base64 decode (obfuscation)` — `base64 -d`
- `Cron persistence` — `crontab`

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `61.137.140[.]246` | CN | China Unicom Liaoning province network | **100** ⚠️ | 1 |
| `84.8.155[.]112` | GB | Oracle Svenska AB | **100** ⚠️ | 3 |
| `91.92.40[.]18` | NL | TechTies Inc. | **100** ⚠️ | 9 |
| `45.79.207[.]181` | US | Linode | **100** ⚠️ | 50 |
| `138.2.20[.]68` | JP | Oracle Corporation | **100** ⚠️ | 1 |
| `37.63.88[.]203` | BG | A1 Bulgaria EAD | **100** ⚠️ | 4 |
| `85.217.149[.]6` | CA | NL MODAT | **100** ⚠️ | 50 |
| `144.22.238[.]238` | BR | Oracle Corporation | **100** ⚠️ | 3 |
| `154.16.146[.]65` | US | OC1-HostForWeb, LLC | **100** ⚠️ | 3 |
| `3.131.220[.]121` | US | Amazon Technologies Inc. | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 73 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 50 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 1 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 1 |

---

## 🔕 False Positive Summary (27 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 15 |
| AbuseIPDB score 12 below threshold 25 | 1 |
| AbuseIPDB score 16 below threshold 25 | 1 |
| AbuseIPDB score 5 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 9 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 135 cases |
| Tool 34  | Credential Extractor        | ✅ 51 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 10 fingerprints |
| Tool 36  | Command Clustering          | ✅ 4 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 61 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 27 filtered (20.0%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 36 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 17 files |
| Tool 33  | YARA Classifier             | ✅ 13 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 48 priority case(s) shown individually · 47 recon entry/entries in table (7 group(s) consolidating 20 session(s)).

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
| CIS-1 | Asset Inventory | ACTIVE | assets.json updated every pipeline run by Tool 05 |
| CIS-2 | Software Inventory | MONITORING | tool_manifest.yaml tracks pipeline tools |
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
_Report time: 2026-06-17T15:43:25Z_

# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-06-14 |
| **Generated At** | 2026-06-14T15:50:46Z |
| **Shift Time** | 15:50 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **263** |
| Confirmed Threats | **222** |
| False Positives Filtered | **41** (15.6%) |
| Unique Attacker IPs | **41** |
| Countries of Origin | **14** |
| High Severity Cases | **83** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **180** |
| Malware Samples Analyzed | **0** HIGH · **20** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **91** |
| Unique Credential Pairs | **60** |
| Unique Usernames | **24** |
| Unique Passwords | **45** |
| Successful Auth Pairs | **71** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 36 |
| `sol` | 12 |
| `solana` | 12 |
| `trader` | 5 |
| `ubuntu` | 4 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `LeitboGi0ro` | 13 |
| `` | 8 |
| `123@@@` | 7 |
| `1234` | 3 |
| `123` | 3 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `LeitboGi0ro` | 13 |
| `root` | `` | 8 |
| `root` | `123@@@` | 7 |
| `sol` | `sol` | 2 |
| `solana` | `solana` | 2 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `LeitboGi0ro` | `40.233.83.131` | 2026-06-14T10:58:14 |
| `root` | `123@@@` | `40.233.83.131` | 2026-06-14T10:58:15 |
| `root` | `ubuntu` | `103.121.91.144` | 2026-06-14T11:05:45 |
| `telnetadmin` | `telnetadmin` | `176.65.148.251` | 2026-06-14T11:06:19 |
| `root` | `123@@@` | `144.22.238.238` | 2026-06-14T11:08:30 |
| `root` | `LeitboGi0ro` | `144.22.238.238` | 2026-06-14T11:08:30 |
| `root` | `LeitboGi0ro` | `129.153.145.135` | 2026-06-14T11:14:40 |
| `root` | `123@@@` | `129.153.145.135` | 2026-06-14T11:14:41 |
| `root` | `LeitboGi0ro` | `161.118.237.181` | 2026-06-14T11:28:30 |
| `root` | `123@@@` | `161.118.237.181` | 2026-06-14T11:28:32 |
| `root` | `﻿------fuck------` | `27.0.135.6` | 2026-06-14T11:38:07 |
| `sol` | `sol` | `45.148.10.183` | 2026-06-14T12:10:32 |
| `solana` | `solana` | `45.148.10.183` | 2026-06-14T12:12:42 |
| `solana` | `1234` | `45.148.10.183` | 2026-06-14T12:14:55 |
| `sol` | `1234` | `45.148.10.183` | 2026-06-14T12:16:53 |
| `sol` | `123` | `45.148.10.183` | 2026-06-14T12:18:56 |
| `sol` | `Solana` | `45.148.10.183` | 2026-06-14T12:21:03 |
| `solana` | `123456789` | `45.148.10.183` | 2026-06-14T12:23:04 |
| `solana` | `12345678` | `45.148.10.183` | 2026-06-14T12:25:11 |
| `solana` | `1234567` | `45.148.10.183` | 2026-06-14T12:27:23 |
| `user` | `12345678` | `50.46.141.125` | 2026-06-14T12:28:12 |
| `user` | `12345678~` | `50.46.141.125` | 2026-06-14T12:28:13 |
| `sol` | `1234567` | `45.148.10.183` | 2026-06-14T12:29:29 |
| `sol` | `1234567890` | `45.148.10.183` | 2026-06-14T12:31:32 |
| `sol` | `!@#$%^` | `45.148.10.183` | 2026-06-14T12:33:42 |
| `sol` | `Solana!` | `45.148.10.183` | 2026-06-14T12:35:46 |
| `root` | `Solana!` | `45.148.10.183` | 2026-06-14T12:37:51 |
| `root` | `solana!@#` | `45.148.10.183` | 2026-06-14T12:40:07 |
| `solana` | `qwer1234` | `45.148.10.183` | 2026-06-14T12:42:15 |
| `solana` | `1234qwer` | `45.148.10.183` | 2026-06-14T12:44:26 |
| `solana` | `1qaz@WSX3edc` | `45.148.10.183` | 2026-06-14T12:46:39 |
| `solana` | `SOL` | `45.148.10.183` | 2026-06-14T12:48:45 |
| `solana` | `sols` | `45.148.10.183` | 2026-06-14T12:50:52 |
| `sols` | `sols` | `45.148.10.183` | 2026-06-14T12:53:03 |
| `jito` | `jito` | `45.148.10.183` | 2026-06-14T12:55:11 |
| `soul` | `soul` | `45.148.10.183` | 2026-06-14T12:57:24 |
| `sol` | `soul` | `45.148.10.183` | 2026-06-14T12:59:42 |
| `solana` | `soul` | `45.148.10.183` | 2026-06-14T13:01:49 |
| `sole` | `sole` | `45.148.10.183` | 2026-06-14T13:04:00 |
| `solv` | `solv123` | `45.148.10.183` | 2026-06-14T13:06:11 |
| `solv` | `123456` | `45.148.10.183` | 2026-06-14T13:08:15 |
| `solb` | `solb` | `45.148.10.183` | 2026-06-14T13:10:30 |
| `solz` | `solz` | `45.148.10.183` | 2026-06-14T13:12:49 |
| `firedancer` | `firedancer` | `45.148.10.183` | 2026-06-14T13:15:03 |
| `root` | `firedancer` | `45.148.10.183` | 2026-06-14T13:17:20 |
| `root` | `shredstream` | `45.148.10.183` | 2026-06-14T13:19:34 |
| `shred` | `shred` | `45.148.10.183` | 2026-06-14T13:21:44 |
| `validator` | `123` | `45.148.10.183` | 2026-06-14T13:24:01 |
| `binance` | `binance` | `45.148.10.183` | 2026-06-14T13:26:19 |
| `trader` | `trader` | `45.148.10.183` | 2026-06-14T13:28:35 |
| `trading` | `trading` | `45.148.10.183` | 2026-06-14T13:30:57 |
| `ubuntu` | `trader` | `45.148.10.183` | 2026-06-14T13:33:07 |
| `admin` | `admin` | `125.20.210.182` | 2026-06-14T13:34:29 |
| `bitcoin` | `bitcoin` | `45.148.10.183` | 2026-06-14T13:35:17 |
| `ethereum` | `ethereum` | `45.148.10.183` | 2026-06-14T13:37:34 |
| `root` | `trader` | `45.148.10.183` | 2026-06-14T13:39:46 |
| `trader` | `trader123` | `45.148.10.183` | 2026-06-14T13:42:05 |
| `trader` | `trader1234` | `45.148.10.183` | 2026-06-14T13:44:25 |
| `trader` | `ibkr123` | `45.148.10.183` | 2026-06-14T13:46:38 |
| `root` | `ibkr123` | `45.148.10.183` | 2026-06-14T13:48:54 |
| `exchange` | `exchange` | `45.148.10.183` | 2026-06-14T13:51:11 |
| `root` | `LeitboGi0ro` | `140.245.67.111` | 2026-06-14T13:59:21 |
| `root` | `123@@@` | `140.245.67.111` | 2026-06-14T13:59:21 |
| `ubuntu` | `ubuntu` | `45.148.10.183` | 2026-06-14T14:02:35 |
| `ubuntu` | `123456` | `45.148.10.183` | 2026-06-14T14:04:49 |
| `ubuntu` | `12345678` | `45.148.10.183` | 2026-06-14T14:07:03 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-06-14T14:10:09 |
| `root` | `123@@@` | `64.110.90.250` | 2026-06-14T14:10:09 |
| `pool` | `pool` | `45.148.10.183` | 2026-06-14T14:13:50 |
| `root` | `123@@@` | `158.178.141.210` | 2026-06-14T14:43:10 |
| `root` | `LeitboGi0ro` | `158.178.141.210` | 2026-06-14T14:43:10 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **263** |
| Sessions with Fingerprint | **13** |
| Unique HASSH Fingerprints | **13** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 65 |
| libssh | 33 |
| Paramiko (Python) | 20 |
| Nmap scanner | 7 |
| OpenSSH | 2 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `16443846184e...` | Generic scanner | 57 | 1 |
| `6372ee695756...` | Modern SSH client | 12 | 3 |
| `a2de0f306611...` | Mirai/variant | 8 | 4 |
| `e788c657d1a2...` | Mirai/variant | 6 | 1 |
| `f1e5e9d24e5e...` | Mirai/variant | 4 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `16443846184e...` | Go SSH scanner | 57 | 1 | Generic scanner |
| `95420f9d932d...` | libssh | 32 | 7 | — |
| `6372ee695756...` | Paramiko (Python) | 12 | 3 | Modern SSH client |
| `a2de0f306611...` | Paramiko (Python) | 8 | 4 | Mirai/variant |
| `e788c657d1a2...` | Nmap scanner | 6 | 1 | Mirai/variant |
| `f1e5e9d24e5e...` | Go SSH scanner | 4 | 1 | Mirai/variant |
| `98f63c4d9c87...` | Go SSH scanner | 2 | 2 | Generic scanner |
| `c8c5fbf80b7b...` | OpenSSH | 2 | 1 | Mirai/variant |

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
| Total IPs Analysed | **41** |
| Unique ASNs | **26** |
| High-Risk ASNs | **23** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS31898` | Oracle Corporation | 7 | HIGH |
| `AS14061` | DigitalOcean, LLC | 4 | HIGH |
| `AS398324` | Censys, Inc. | 4 | HIGH |
| `AS63949` | Akamai Connected Cloud | 3 | HIGH |
| `AS48090` | TECHOFF SRV LIMITED | 2 | HIGH |
| `AS48721` | Flyservers S.A. | 1 | HIGH |
| `AS0` |  | 1 | LOW |
| `AS136180` | Beijing Tiantexin Tech. Co., Ltd. | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (83)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-32cc3e9105db

| Field | Detail |
|---|---|
| **Source IP** | `40.233.83[.]131` |
| **First Seen** | 2026-06-14 10:58 |
| **Last Seen** | 2026-06-14 10:58 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 10:58:14` | `cowrie.session.connect` |
| `2026-06-14 10:58:14` | `cowrie.client.version` |
| `2026-06-14 10:58:14` | `cowrie.client.kex` |
| `2026-06-14 10:58:14` | `cowrie.login.success` |
| `2026-06-14 10:58:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.233.83[.]131` to AbuseIPDB if not already reported
- [ ] Block `40.233.83[.]131` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ab05d3279c20

| Field | Detail |
|---|---|
| **Source IP** | `40.233.83[.]131` |
| **First Seen** | 2026-06-14 10:58 |
| **Last Seen** | 2026-06-14 10:58 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 10:58:15` | `cowrie.session.connect` |
| `2026-06-14 10:58:15` | `cowrie.client.version` |
| `2026-06-14 10:58:15` | `cowrie.client.kex` |
| `2026-06-14 10:58:15` | `cowrie.login.success` |
| `2026-06-14 10:58:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.233.83[.]131` to AbuseIPDB if not already reported
- [ ] Block `40.233.83[.]131` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0540ff33f64a

| Field | Detail |
|---|---|
| **Source IP** | `40.233.83[.]131` |
| **First Seen** | 2026-06-14 10:58 |
| **Last Seen** | 2026-06-14 11:00 |
| **Session Duration** | 125s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 10:58:32` | `cowrie.session.connect` |
| `2026-06-14 10:58:32` | `cowrie.client.version` |
| `2026-06-14 10:58:32` | `cowrie.client.kex` |
| `2026-06-14 10:58:32` | `cowrie.login.success` |
| `2026-06-14 10:58:33` | `cowrie.session.file_upload` |
| `2026-06-14 10:58:34` | `cowrie.session.params` |
| `2026-06-14 10:58:34` | `cowrie.command.input` |
| `2026-06-14 10:58:34` | `cowrie.command.input` |
| `2026-06-14 10:58:34` | `cowrie.command.input` |
| `2026-06-14 10:58:34` | `cowrie.command.failed` |
| `2026-06-14 10:58:34` | `cowrie.log.closed` |
| `2026-06-14 10:58:34` | `cowrie.session.params` |
| `2026-06-14 10:58:34` | `cowrie.command.input` |
| `2026-06-14 10:58:35` | `cowrie.log.closed` |
| `2026-06-14 10:58:35` | `cowrie.session.params` |
| `2026-06-14 10:58:35` | `cowrie.command.input` |
| `2026-06-14 10:58:35` | `cowrie.log.closed` |
| `2026-06-14 10:58:36` | `cowrie.session.params` |
| `2026-06-14 10:58:36` | `cowrie.command.input` |
| `2026-06-14 10:58:36` | `cowrie.command.failed` |
| `2026-06-14 10:58:36` | `cowrie.command.failed` |
| `2026-06-14 10:59:37` | `cowrie.session.params` |
| `2026-06-14 10:59:37` | `cowrie.command.input` |
| `2026-06-14 11:00:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.233.83[.]131` to AbuseIPDB if not already reported
- [ ] Block `40.233.83[.]131` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c9c3e00a256d

| Field | Detail |
|---|---|
| **Source IP** | `40.233.83[.]131` |
| **First Seen** | 2026-06-14 11:00 |
| **Last Seen** | 2026-06-14 11:02 |
| **Session Duration** | 125s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 11:00:52` | `cowrie.session.connect` |
| `2026-06-14 11:00:52` | `cowrie.client.version` |
| `2026-06-14 11:00:52` | `cowrie.client.kex` |
| `2026-06-14 11:00:52` | `cowrie.login.success` |
| `2026-06-14 11:00:53` | `cowrie.session.file_upload` |
| `2026-06-14 11:00:54` | `cowrie.session.params` |
| `2026-06-14 11:00:54` | `cowrie.command.input` |
| `2026-06-14 11:00:54` | `cowrie.command.input` |
| `2026-06-14 11:00:54` | `cowrie.command.input` |
| `2026-06-14 11:00:54` | `cowrie.command.failed` |
| `2026-06-14 11:00:54` | `cowrie.log.closed` |
| `2026-06-14 11:00:55` | `cowrie.session.params` |
| `2026-06-14 11:00:55` | `cowrie.command.input` |
| `2026-06-14 11:00:55` | `cowrie.log.closed` |
| `2026-06-14 11:00:55` | `cowrie.session.params` |
| `2026-06-14 11:00:55` | `cowrie.command.input` |
| `2026-06-14 11:00:55` | `cowrie.log.closed` |
| `2026-06-14 11:00:56` | `cowrie.session.params` |
| `2026-06-14 11:00:56` | `cowrie.command.input` |
| `2026-06-14 11:00:56` | `cowrie.command.failed` |
| `2026-06-14 11:00:56` | `cowrie.command.failed` |
| `2026-06-14 11:01:57` | `cowrie.session.params` |
| `2026-06-14 11:01:57` | `cowrie.command.input` |
| `2026-06-14 11:02:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.233.83[.]131` to AbuseIPDB if not already reported
- [ ] Block `40.233.83[.]131` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8725e8a81d1d

| Field | Detail |
|---|---|
| **Source IP** | `103.121.91[.]144` |
| **First Seen** | 2026-06-14 11:05 |
| **Last Seen** | 2026-06-14 11:07 |
| **Session Duration** | 83s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 11:05:44` | `cowrie.session.connect` |
| `2026-06-14 11:05:44` | `cowrie.client.version` |
| `2026-06-14 11:05:44` | `cowrie.client.kex` |
| `2026-06-14 11:05:45` | `cowrie.login.success` |
| `2026-06-14 11:07:07` | `cowrie.session.file_upload` |
| `2026-06-14 11:07:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.121.91[.]144` to AbuseIPDB if not already reported
- [ ] Block `103.121.91[.]144` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f72cfb2f11fe

| Field | Detail |
|---|---|
| **Source IP** | `176.65.148[.]251` |
| **First Seen** | 2026-06-14 11:06 |
| **Last Seen** | 2026-06-14 11:06 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST, uname -h, /bin/busybox TEST, cat /proc, ./` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 11:06:17` | `cowrie.session.connect` |
| `2026-06-14 11:06:19` | `cowrie.login.success` |
| `2026-06-14 11:06:19` | `cowrie.session.params` |
| `2026-06-14 11:06:20` | `cowrie.command.input` |
| `2026-06-14 11:06:20` | `cowrie.command.input` |
| `2026-06-14 11:06:21` | `cowrie.command.input` |
| `2026-06-14 11:06:22` | `cowrie.command.input` |
| `2026-06-14 11:06:22` | `cowrie.command.input` |
| `2026-06-14 11:06:22` | `cowrie.command.failed` |
| `2026-06-14 11:06:23` | `cowrie.log.closed` |
| `2026-06-14 11:06:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.148[.]251` to AbuseIPDB if not already reported
- [ ] Block `176.65.148[.]251` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-de00d32dcdd0

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-06-14 11:08 |
| **Last Seen** | 2026-06-14 11:08 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 11:08:29` | `cowrie.session.connect` |
| `2026-06-14 11:08:29` | `cowrie.client.version` |
| `2026-06-14 11:08:30` | `cowrie.client.kex` |
| `2026-06-14 11:08:30` | `cowrie.login.success` |
| `2026-06-14 11:08:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-27177a7655c6

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-06-14 11:08 |
| **Last Seen** | 2026-06-14 11:08 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 11:08:30` | `cowrie.session.connect` |
| `2026-06-14 11:08:30` | `cowrie.client.version` |
| `2026-06-14 11:08:30` | `cowrie.client.kex` |
| `2026-06-14 11:08:30` | `cowrie.login.success` |
| `2026-06-14 11:08:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e8cce96ef50e

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-14 11:14 |
| **Last Seen** | 2026-06-14 11:14 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 11:14:40` | `cowrie.session.connect` |
| `2026-06-14 11:14:40` | `cowrie.client.version` |
| `2026-06-14 11:14:40` | `cowrie.client.kex` |
| `2026-06-14 11:14:40` | `cowrie.login.success` |
| `2026-06-14 11:14:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e33f908b83fd

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-14 11:14 |
| **Last Seen** | 2026-06-14 11:14 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 11:14:41` | `cowrie.session.connect` |
| `2026-06-14 11:14:41` | `cowrie.client.version` |
| `2026-06-14 11:14:41` | `cowrie.client.kex` |
| `2026-06-14 11:14:41` | `cowrie.login.success` |
| `2026-06-14 11:14:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e1a7c6fccb63

| Field | Detail |
|---|---|
| **Source IP** | `161.118.237[.]181` |
| **First Seen** | 2026-06-14 11:28 |
| **Last Seen** | 2026-06-14 11:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 11:28:28` | `cowrie.session.connect` |
| `2026-06-14 11:28:28` | `cowrie.client.version` |
| `2026-06-14 11:28:29` | `cowrie.client.kex` |
| `2026-06-14 11:28:30` | `cowrie.login.success` |
| `2026-06-14 11:28:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `161.118.237[.]181` to AbuseIPDB if not already reported
- [ ] Block `161.118.237[.]181` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ab494c8a87f8

| Field | Detail |
|---|---|
| **Source IP** | `161.118.237[.]181` |
| **First Seen** | 2026-06-14 11:28 |
| **Last Seen** | 2026-06-14 11:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 11:28:31` | `cowrie.session.connect` |
| `2026-06-14 11:28:31` | `cowrie.client.version` |
| `2026-06-14 11:28:31` | `cowrie.client.kex` |
| `2026-06-14 11:28:32` | `cowrie.login.success` |
| `2026-06-14 11:28:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `161.118.237[.]181` to AbuseIPDB if not already reported
- [ ] Block `161.118.237[.]181` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-246d09354ff0

| Field | Detail |
|---|---|
| **Source IP** | `161.118.237[.]181` |
| **First Seen** | 2026-06-14 11:28 |
| **Last Seen** | 2026-06-14 11:31 |
| **Session Duration** | 131s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 11:28:53` | `cowrie.session.connect` |
| `2026-06-14 11:28:53` | `cowrie.client.version` |
| `2026-06-14 11:28:54` | `cowrie.client.kex` |
| `2026-06-14 11:28:55` | `cowrie.login.success` |
| `2026-06-14 11:28:57` | `cowrie.session.file_upload` |
| `2026-06-14 11:28:58` | `cowrie.session.params` |
| `2026-06-14 11:28:58` | `cowrie.command.input` |
| `2026-06-14 11:28:58` | `cowrie.command.input` |
| `2026-06-14 11:28:58` | `cowrie.command.input` |
| `2026-06-14 11:28:58` | `cowrie.command.failed` |
| `2026-06-14 11:28:58` | `cowrie.log.closed` |
| `2026-06-14 11:29:00` | `cowrie.session.params` |
| `2026-06-14 11:29:00` | `cowrie.command.input` |
| `2026-06-14 11:29:00` | `cowrie.log.closed` |
| `2026-06-14 11:29:01` | `cowrie.session.params` |
| `2026-06-14 11:29:01` | `cowrie.command.input` |
| `2026-06-14 11:29:01` | `cowrie.log.closed` |
| `2026-06-14 11:29:02` | `cowrie.session.params` |
| `2026-06-14 11:29:02` | `cowrie.command.input` |
| `2026-06-14 11:29:02` | `cowrie.command.failed` |
| `2026-06-14 11:29:02` | `cowrie.command.failed` |
| `2026-06-14 11:30:04` | `cowrie.session.params` |
| `2026-06-14 11:30:04` | `cowrie.command.input` |
| `2026-06-14 11:31:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `161.118.237[.]181` to AbuseIPDB if not already reported
- [ ] Block `161.118.237[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9619eeafa794

| Field | Detail |
|---|---|
| **Source IP** | `161.118.237[.]181` |
| **First Seen** | 2026-06-14 11:31 |
| **Last Seen** | 2026-06-14 11:33 |
| **Session Duration** | 131s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 11:31:20` | `cowrie.session.connect` |
| `2026-06-14 11:31:20` | `cowrie.client.version` |
| `2026-06-14 11:31:20` | `cowrie.client.kex` |
| `2026-06-14 11:31:21` | `cowrie.login.success` |
| `2026-06-14 11:31:24` | `cowrie.session.file_upload` |
| `2026-06-14 11:31:25` | `cowrie.session.params` |
| `2026-06-14 11:31:25` | `cowrie.command.input` |
| `2026-06-14 11:31:25` | `cowrie.command.input` |
| `2026-06-14 11:31:25` | `cowrie.command.input` |
| `2026-06-14 11:31:25` | `cowrie.command.failed` |
| `2026-06-14 11:31:25` | `cowrie.log.closed` |
| `2026-06-14 11:31:26` | `cowrie.session.params` |
| `2026-06-14 11:31:26` | `cowrie.command.input` |
| `2026-06-14 11:31:26` | `cowrie.log.closed` |
| `2026-06-14 11:31:28` | `cowrie.session.params` |
| `2026-06-14 11:31:28` | `cowrie.command.input` |
| `2026-06-14 11:31:28` | `cowrie.log.closed` |
| `2026-06-14 11:31:29` | `cowrie.session.params` |
| `2026-06-14 11:31:29` | `cowrie.command.input` |
| `2026-06-14 11:31:29` | `cowrie.command.failed` |
| `2026-06-14 11:31:29` | `cowrie.command.failed` |
| `2026-06-14 11:32:30` | `cowrie.session.params` |
| `2026-06-14 11:32:30` | `cowrie.command.input` |
| `2026-06-14 11:33:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `161.118.237[.]181` to AbuseIPDB if not already reported
- [ ] Block `161.118.237[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5e9e089bd28d

| Field | Detail |
|---|---|
| **Source IP** | `27.0.135[.]6` |
| **First Seen** | 2026-06-14 11:37 |
| **Last Seen** | 2026-06-14 11:38 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 11:37:59` | `cowrie.session.connect` |
| `2026-06-14 11:38:00` | `cowrie.client.version` |
| `2026-06-14 11:38:00` | `cowrie.client.kex` |
| `2026-06-14 11:38:07` | `cowrie.login.success` |
| `2026-06-14 11:38:12` | `cowrie.session.params` |
| `2026-06-14 11:38:12` | `cowrie.command.input` |
| `2026-06-14 11:38:14` | `cowrie.log.closed` |
| `2026-06-14 11:38:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.0.135[.]6` to AbuseIPDB if not already reported
- [ ] Block `27.0.135[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e8689977b4ac

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-14 12:10 |
| **Last Seen** | 2026-06-14 12:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 12:10:31` | `cowrie.session.connect` |
| `2026-06-14 12:10:31` | `cowrie.client.version` |
| `2026-06-14 12:10:32` | `cowrie.client.kex` |
| `2026-06-14 12:10:32` | `cowrie.login.success` |
| `2026-06-14 12:10:33` | `cowrie.session.params` |
| `2026-06-14 12:10:33` | `cowrie.command.input` |
| `2026-06-14 12:10:33` | `cowrie.log.closed` |
| `2026-06-14 12:10:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ffbfb5d6c024

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-14 12:12 |
| **Last Seen** | 2026-06-14 12:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 12:12:41` | `cowrie.session.connect` |
| `2026-06-14 12:12:41` | `cowrie.client.version` |
| `2026-06-14 12:12:41` | `cowrie.client.kex` |
| `2026-06-14 12:12:42` | `cowrie.login.success` |
| `2026-06-14 12:12:42` | `cowrie.session.params` |
| `2026-06-14 12:12:42` | `cowrie.command.input` |
| `2026-06-14 12:12:42` | `cowrie.log.closed` |
| `2026-06-14 12:12:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e76017135e73

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-14 12:14 |
| **Last Seen** | 2026-06-14 12:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 12:14:54` | `cowrie.session.connect` |
| `2026-06-14 12:14:54` | `cowrie.client.version` |
| `2026-06-14 12:14:54` | `cowrie.client.kex` |
| `2026-06-14 12:14:55` | `cowrie.login.success` |
| `2026-06-14 12:14:55` | `cowrie.session.params` |
| `2026-06-14 12:14:55` | `cowrie.command.input` |
| `2026-06-14 12:14:55` | `cowrie.log.closed` |
| `2026-06-14 12:14:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6801497b4bc9

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-14 12:16 |
| **Last Seen** | 2026-06-14 12:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 12:16:53` | `cowrie.session.connect` |
| `2026-06-14 12:16:53` | `cowrie.client.version` |
| `2026-06-14 12:16:53` | `cowrie.client.kex` |
| `2026-06-14 12:16:53` | `cowrie.login.success` |
| `2026-06-14 12:16:54` | `cowrie.session.params` |
| `2026-06-14 12:16:54` | `cowrie.command.input` |
| `2026-06-14 12:16:54` | `cowrie.log.closed` |
| `2026-06-14 12:16:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f9e84a67c8b7

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-14 12:18 |
| **Last Seen** | 2026-06-14 12:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 12:18:56` | `cowrie.session.connect` |
| `2026-06-14 12:18:56` | `cowrie.client.version` |
| `2026-06-14 12:18:56` | `cowrie.client.kex` |
| `2026-06-14 12:18:56` | `cowrie.login.success` |
| `2026-06-14 12:18:57` | `cowrie.session.params` |
| `2026-06-14 12:18:57` | `cowrie.command.input` |
| `2026-06-14 12:18:57` | `cowrie.log.closed` |
| `2026-06-14 12:18:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-98ac4d09c0fd

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-14 12:21 |
| **Last Seen** | 2026-06-14 12:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 12:21:03` | `cowrie.session.connect` |
| `2026-06-14 12:21:03` | `cowrie.client.version` |
| `2026-06-14 12:21:03` | `cowrie.client.kex` |
| `2026-06-14 12:21:03` | `cowrie.login.success` |
| `2026-06-14 12:21:04` | `cowrie.session.params` |
| `2026-06-14 12:21:04` | `cowrie.command.input` |
| `2026-06-14 12:21:04` | `cowrie.log.closed` |
| `2026-06-14 12:21:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0ffcebde9a25

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-14 12:23 |
| **Last Seen** | 2026-06-14 12:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 12:23:04` | `cowrie.session.connect` |
| `2026-06-14 12:23:04` | `cowrie.client.version` |
| `2026-06-14 12:23:04` | `cowrie.client.kex` |
| `2026-06-14 12:23:04` | `cowrie.login.success` |
| `2026-06-14 12:23:05` | `cowrie.session.params` |
| `2026-06-14 12:23:05` | `cowrie.command.input` |
| `2026-06-14 12:23:05` | `cowrie.log.closed` |
| `2026-06-14 12:23:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f8c540ea4584

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-14 12:25 |
| **Last Seen** | 2026-06-14 12:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 12:25:10` | `cowrie.session.connect` |
| `2026-06-14 12:25:10` | `cowrie.client.version` |
| `2026-06-14 12:25:11` | `cowrie.client.kex` |
| `2026-06-14 12:25:11` | `cowrie.login.success` |
| `2026-06-14 12:25:12` | `cowrie.session.params` |
| `2026-06-14 12:25:12` | `cowrie.command.input` |
| `2026-06-14 12:25:12` | `cowrie.log.closed` |
| `2026-06-14 12:25:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1ad0ed9e2728

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-14 12:27 |
| **Last Seen** | 2026-06-14 12:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 12:27:23` | `cowrie.session.connect` |
| `2026-06-14 12:27:23` | `cowrie.client.version` |
| `2026-06-14 12:27:23` | `cowrie.client.kex` |
| `2026-06-14 12:27:23` | `cowrie.login.success` |
| `2026-06-14 12:27:24` | `cowrie.session.params` |
| `2026-06-14 12:27:24` | `cowrie.command.input` |
| `2026-06-14 12:27:24` | `cowrie.log.closed` |
| `2026-06-14 12:27:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-19c0cb71da1c

| Field | Detail |
|---|---|
| **Source IP** | `50.46.141[.]125` |
| **First Seen** | 2026-06-14 12:28 |
| **Last Seen** | 2026-06-14 12:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 12:28:12` | `cowrie.session.connect` |
| `2026-06-14 12:28:12` | `cowrie.client.version` |
| `2026-06-14 12:28:12` | `cowrie.client.kex` |
| `2026-06-14 12:28:12` | `cowrie.login.success` |
| `2026-06-14 12:28:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `50.46.141[.]125` to AbuseIPDB if not already reported
- [ ] Block `50.46.141[.]125` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fdd4ac49b536

| Field | Detail |
|---|---|
| **Source IP** | `50.46.141[.]125` |
| **First Seen** | 2026-06-14 12:28 |
| **Last Seen** | 2026-06-14 12:28 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 12:28:13` | `cowrie.session.connect` |
| `2026-06-14 12:28:13` | `cowrie.client.version` |
| `2026-06-14 12:28:13` | `cowrie.client.kex` |
| `2026-06-14 12:28:13` | `cowrie.login.success` |
| `2026-06-14 12:28:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `50.46.141[.]125` to AbuseIPDB if not already reported
- [ ] Block `50.46.141[.]125` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-039e6c125534

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-14 12:29 |
| **Last Seen** | 2026-06-14 12:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 12:29:29` | `cowrie.session.connect` |
| `2026-06-14 12:29:29` | `cowrie.client.version` |
| `2026-06-14 12:29:29` | `cowrie.client.kex` |
| `2026-06-14 12:29:29` | `cowrie.login.success` |
| `2026-06-14 12:29:30` | `cowrie.session.params` |
| `2026-06-14 12:29:30` | `cowrie.command.input` |
| `2026-06-14 12:29:30` | `cowrie.log.closed` |
| `2026-06-14 12:29:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c7099b6d593f

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-14 12:31 |
| **Last Seen** | 2026-06-14 12:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 12:31:32` | `cowrie.session.connect` |
| `2026-06-14 12:31:32` | `cowrie.client.version` |
| `2026-06-14 12:31:32` | `cowrie.client.kex` |
| `2026-06-14 12:31:32` | `cowrie.login.success` |
| `2026-06-14 12:31:33` | `cowrie.session.params` |
| `2026-06-14 12:31:33` | `cowrie.command.input` |
| `2026-06-14 12:31:33` | `cowrie.log.closed` |
| `2026-06-14 12:31:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d1c429792dfd

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-14 12:33 |
| **Last Seen** | 2026-06-14 12:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 12:33:41` | `cowrie.session.connect` |
| `2026-06-14 12:33:41` | `cowrie.client.version` |
| `2026-06-14 12:33:41` | `cowrie.client.kex` |
| `2026-06-14 12:33:42` | `cowrie.login.success` |
| `2026-06-14 12:33:43` | `cowrie.session.params` |
| `2026-06-14 12:33:43` | `cowrie.command.input` |
| `2026-06-14 12:33:43` | `cowrie.log.closed` |
| `2026-06-14 12:33:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-01bb77db0385

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-14 12:35 |
| **Last Seen** | 2026-06-14 12:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 12:35:45` | `cowrie.session.connect` |
| `2026-06-14 12:35:45` | `cowrie.client.version` |
| `2026-06-14 12:35:46` | `cowrie.client.kex` |
| `2026-06-14 12:35:46` | `cowrie.login.success` |
| `2026-06-14 12:35:46` | `cowrie.session.params` |
| `2026-06-14 12:35:46` | `cowrie.command.input` |
| `2026-06-14 12:35:47` | `cowrie.log.closed` |
| `2026-06-14 12:35:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-63b0cbafae89

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-14 12:37 |
| **Last Seen** | 2026-06-14 12:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 12:37:51` | `cowrie.session.connect` |
| `2026-06-14 12:37:51` | `cowrie.client.version` |
| `2026-06-14 12:37:51` | `cowrie.client.kex` |
| `2026-06-14 12:37:51` | `cowrie.login.success` |
| `2026-06-14 12:37:52` | `cowrie.session.params` |
| `2026-06-14 12:37:52` | `cowrie.command.input` |
| `2026-06-14 12:37:52` | `cowrie.log.closed` |
| `2026-06-14 12:37:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2641825d6d8a

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-14 12:40 |
| **Last Seen** | 2026-06-14 12:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 12:40:06` | `cowrie.session.connect` |
| `2026-06-14 12:40:06` | `cowrie.client.version` |
| `2026-06-14 12:40:07` | `cowrie.client.kex` |
| `2026-06-14 12:40:07` | `cowrie.login.success` |
| `2026-06-14 12:40:07` | `cowrie.session.params` |
| `2026-06-14 12:40:07` | `cowrie.command.input` |
| `2026-06-14 12:40:08` | `cowrie.log.closed` |
| `2026-06-14 12:40:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e389faf2761d

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-14 12:42 |
| **Last Seen** | 2026-06-14 12:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 12:42:15` | `cowrie.session.connect` |
| `2026-06-14 12:42:15` | `cowrie.client.version` |
| `2026-06-14 12:42:15` | `cowrie.client.kex` |
| `2026-06-14 12:42:15` | `cowrie.login.success` |
| `2026-06-14 12:42:16` | `cowrie.session.params` |
| `2026-06-14 12:42:16` | `cowrie.command.input` |
| `2026-06-14 12:42:16` | `cowrie.log.closed` |
| `2026-06-14 12:42:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ba3d40c41242

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-14 12:44 |
| **Last Seen** | 2026-06-14 12:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 12:44:25` | `cowrie.session.connect` |
| `2026-06-14 12:44:25` | `cowrie.client.version` |
| `2026-06-14 12:44:25` | `cowrie.client.kex` |
| `2026-06-14 12:44:26` | `cowrie.login.success` |
| `2026-06-14 12:44:26` | `cowrie.session.params` |
| `2026-06-14 12:44:26` | `cowrie.command.input` |
| `2026-06-14 12:44:26` | `cowrie.log.closed` |
| `2026-06-14 12:44:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a7f8bf92cc57

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-14 12:46 |
| **Last Seen** | 2026-06-14 12:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 12:46:38` | `cowrie.session.connect` |
| `2026-06-14 12:46:38` | `cowrie.client.version` |
| `2026-06-14 12:46:38` | `cowrie.client.kex` |
| `2026-06-14 12:46:39` | `cowrie.login.success` |
| `2026-06-14 12:46:39` | `cowrie.session.params` |
| `2026-06-14 12:46:39` | `cowrie.command.input` |
| `2026-06-14 12:46:39` | `cowrie.log.closed` |
| `2026-06-14 12:46:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f466bf3947be

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-14 12:48 |
| **Last Seen** | 2026-06-14 12:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 12:48:44` | `cowrie.session.connect` |
| `2026-06-14 12:48:44` | `cowrie.client.version` |
| `2026-06-14 12:48:44` | `cowrie.client.kex` |
| `2026-06-14 12:48:45` | `cowrie.login.success` |
| `2026-06-14 12:48:45` | `cowrie.session.params` |
| `2026-06-14 12:48:45` | `cowrie.command.input` |
| `2026-06-14 12:48:46` | `cowrie.log.closed` |
| `2026-06-14 12:48:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-959eba44a1e8

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-14 12:50 |
| **Last Seen** | 2026-06-14 12:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 12:50:52` | `cowrie.session.connect` |
| `2026-06-14 12:50:52` | `cowrie.client.version` |
| `2026-06-14 12:50:52` | `cowrie.client.kex` |
| `2026-06-14 12:50:52` | `cowrie.login.success` |
| `2026-06-14 12:50:53` | `cowrie.session.params` |
| `2026-06-14 12:50:53` | `cowrie.command.input` |
| `2026-06-14 12:50:53` | `cowrie.log.closed` |
| `2026-06-14 12:50:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-64fb297e89b6

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-14 12:53 |
| **Last Seen** | 2026-06-14 12:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 12:53:03` | `cowrie.session.connect` |
| `2026-06-14 12:53:03` | `cowrie.client.version` |
| `2026-06-14 12:53:03` | `cowrie.client.kex` |
| `2026-06-14 12:53:03` | `cowrie.login.success` |
| `2026-06-14 12:53:04` | `cowrie.session.params` |
| `2026-06-14 12:53:04` | `cowrie.command.input` |
| `2026-06-14 12:53:04` | `cowrie.log.closed` |
| `2026-06-14 12:53:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cefcaa32ee4c

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-14 12:55 |
| **Last Seen** | 2026-06-14 12:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 12:55:11` | `cowrie.session.connect` |
| `2026-06-14 12:55:11` | `cowrie.client.version` |
| `2026-06-14 12:55:11` | `cowrie.client.kex` |
| `2026-06-14 12:55:11` | `cowrie.login.success` |
| `2026-06-14 12:55:12` | `cowrie.session.params` |
| `2026-06-14 12:55:12` | `cowrie.command.input` |
| `2026-06-14 12:55:12` | `cowrie.log.closed` |
| `2026-06-14 12:55:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cdc43371b307

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-14 12:57 |
| **Last Seen** | 2026-06-14 12:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 12:57:24` | `cowrie.session.connect` |
| `2026-06-14 12:57:24` | `cowrie.client.version` |
| `2026-06-14 12:57:24` | `cowrie.client.kex` |
| `2026-06-14 12:57:24` | `cowrie.login.success` |
| `2026-06-14 12:57:25` | `cowrie.session.params` |
| `2026-06-14 12:57:25` | `cowrie.command.input` |
| `2026-06-14 12:57:25` | `cowrie.log.closed` |
| `2026-06-14 12:57:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bf36facb9d60

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-14 12:59 |
| **Last Seen** | 2026-06-14 12:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 12:59:42` | `cowrie.session.connect` |
| `2026-06-14 12:59:42` | `cowrie.client.version` |
| `2026-06-14 12:59:42` | `cowrie.client.kex` |
| `2026-06-14 12:59:42` | `cowrie.login.success` |
| `2026-06-14 12:59:43` | `cowrie.session.params` |
| `2026-06-14 12:59:43` | `cowrie.command.input` |
| `2026-06-14 12:59:43` | `cowrie.log.closed` |
| `2026-06-14 12:59:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1a7d3a5a4689

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-14 13:01 |
| **Last Seen** | 2026-06-14 13:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 13:01:49` | `cowrie.session.connect` |
| `2026-06-14 13:01:49` | `cowrie.client.version` |
| `2026-06-14 13:01:49` | `cowrie.client.kex` |
| `2026-06-14 13:01:49` | `cowrie.login.success` |
| `2026-06-14 13:01:50` | `cowrie.session.params` |
| `2026-06-14 13:01:50` | `cowrie.command.input` |
| `2026-06-14 13:01:50` | `cowrie.log.closed` |
| `2026-06-14 13:01:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d06322894ece

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-14 13:03 |
| **Last Seen** | 2026-06-14 13:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 13:03:59` | `cowrie.session.connect` |
| `2026-06-14 13:03:59` | `cowrie.client.version` |
| `2026-06-14 13:04:00` | `cowrie.client.kex` |
| `2026-06-14 13:04:00` | `cowrie.login.success` |
| `2026-06-14 13:04:01` | `cowrie.session.params` |
| `2026-06-14 13:04:01` | `cowrie.command.input` |
| `2026-06-14 13:04:01` | `cowrie.log.closed` |
| `2026-06-14 13:04:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1775e5a988e8

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-14 13:06 |
| **Last Seen** | 2026-06-14 13:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 13:06:11` | `cowrie.session.connect` |
| `2026-06-14 13:06:11` | `cowrie.client.version` |
| `2026-06-14 13:06:11` | `cowrie.client.kex` |
| `2026-06-14 13:06:11` | `cowrie.login.success` |
| `2026-06-14 13:06:12` | `cowrie.session.params` |
| `2026-06-14 13:06:12` | `cowrie.command.input` |
| `2026-06-14 13:06:12` | `cowrie.log.closed` |
| `2026-06-14 13:06:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-df0e5e8fe725

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-14 13:08 |
| **Last Seen** | 2026-06-14 13:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 13:08:15` | `cowrie.session.connect` |
| `2026-06-14 13:08:15` | `cowrie.client.version` |
| `2026-06-14 13:08:15` | `cowrie.client.kex` |
| `2026-06-14 13:08:15` | `cowrie.login.success` |
| `2026-06-14 13:08:16` | `cowrie.session.params` |
| `2026-06-14 13:08:16` | `cowrie.command.input` |
| `2026-06-14 13:08:16` | `cowrie.log.closed` |
| `2026-06-14 13:08:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9aaacb549b4a

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-14 13:10 |
| **Last Seen** | 2026-06-14 13:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 13:10:29` | `cowrie.session.connect` |
| `2026-06-14 13:10:29` | `cowrie.client.version` |
| `2026-06-14 13:10:30` | `cowrie.client.kex` |
| `2026-06-14 13:10:30` | `cowrie.login.success` |
| `2026-06-14 13:10:31` | `cowrie.session.params` |
| `2026-06-14 13:10:31` | `cowrie.command.input` |
| `2026-06-14 13:10:31` | `cowrie.log.closed` |
| `2026-06-14 13:10:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6c5b70a30f3e

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-14 13:12 |
| **Last Seen** | 2026-06-14 13:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 13:12:49` | `cowrie.session.connect` |
| `2026-06-14 13:12:49` | `cowrie.client.version` |
| `2026-06-14 13:12:49` | `cowrie.client.kex` |
| `2026-06-14 13:12:49` | `cowrie.login.success` |
| `2026-06-14 13:12:50` | `cowrie.session.params` |
| `2026-06-14 13:12:50` | `cowrie.command.input` |
| `2026-06-14 13:12:50` | `cowrie.log.closed` |
| `2026-06-14 13:12:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-42efd956ac34

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-14 13:15 |
| **Last Seen** | 2026-06-14 13:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 13:15:03` | `cowrie.session.connect` |
| `2026-06-14 13:15:03` | `cowrie.client.version` |
| `2026-06-14 13:15:03` | `cowrie.client.kex` |
| `2026-06-14 13:15:03` | `cowrie.login.success` |
| `2026-06-14 13:15:04` | `cowrie.session.params` |
| `2026-06-14 13:15:04` | `cowrie.command.input` |
| `2026-06-14 13:15:04` | `cowrie.log.closed` |
| `2026-06-14 13:15:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d20bb2b20130

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-14 13:17 |
| **Last Seen** | 2026-06-14 13:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 13:17:19` | `cowrie.session.connect` |
| `2026-06-14 13:17:19` | `cowrie.client.version` |
| `2026-06-14 13:17:19` | `cowrie.client.kex` |
| `2026-06-14 13:17:20` | `cowrie.login.success` |
| `2026-06-14 13:17:20` | `cowrie.session.params` |
| `2026-06-14 13:17:20` | `cowrie.command.input` |
| `2026-06-14 13:17:20` | `cowrie.log.closed` |
| `2026-06-14 13:17:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-01ff4bb202bf

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-14 13:19 |
| **Last Seen** | 2026-06-14 13:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 13:19:34` | `cowrie.session.connect` |
| `2026-06-14 13:19:34` | `cowrie.client.version` |
| `2026-06-14 13:19:34` | `cowrie.client.kex` |
| `2026-06-14 13:19:34` | `cowrie.login.success` |
| `2026-06-14 13:19:35` | `cowrie.session.params` |
| `2026-06-14 13:19:35` | `cowrie.command.input` |
| `2026-06-14 13:19:35` | `cowrie.log.closed` |
| `2026-06-14 13:19:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1a89da718549

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-14 13:21 |
| **Last Seen** | 2026-06-14 13:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 13:21:44` | `cowrie.session.connect` |
| `2026-06-14 13:21:44` | `cowrie.client.version` |
| `2026-06-14 13:21:44` | `cowrie.client.kex` |
| `2026-06-14 13:21:44` | `cowrie.login.success` |
| `2026-06-14 13:21:45` | `cowrie.session.params` |
| `2026-06-14 13:21:45` | `cowrie.command.input` |
| `2026-06-14 13:21:45` | `cowrie.log.closed` |
| `2026-06-14 13:21:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5a5e1561e047

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-14 13:24 |
| **Last Seen** | 2026-06-14 13:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 13:24:01` | `cowrie.session.connect` |
| `2026-06-14 13:24:01` | `cowrie.client.version` |
| `2026-06-14 13:24:01` | `cowrie.client.kex` |
| `2026-06-14 13:24:01` | `cowrie.login.success` |
| `2026-06-14 13:24:02` | `cowrie.session.params` |
| `2026-06-14 13:24:02` | `cowrie.command.input` |
| `2026-06-14 13:24:02` | `cowrie.log.closed` |
| `2026-06-14 13:24:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-62bb103709fa

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-14 13:26 |
| **Last Seen** | 2026-06-14 13:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 13:26:19` | `cowrie.session.connect` |
| `2026-06-14 13:26:19` | `cowrie.client.version` |
| `2026-06-14 13:26:19` | `cowrie.client.kex` |
| `2026-06-14 13:26:19` | `cowrie.login.success` |
| `2026-06-14 13:26:20` | `cowrie.session.params` |
| `2026-06-14 13:26:20` | `cowrie.command.input` |
| `2026-06-14 13:26:20` | `cowrie.log.closed` |
| `2026-06-14 13:26:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-22dc65b09c6e

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-14 13:28 |
| **Last Seen** | 2026-06-14 13:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 13:28:34` | `cowrie.session.connect` |
| `2026-06-14 13:28:34` | `cowrie.client.version` |
| `2026-06-14 13:28:34` | `cowrie.client.kex` |
| `2026-06-14 13:28:35` | `cowrie.login.success` |
| `2026-06-14 13:28:36` | `cowrie.session.params` |
| `2026-06-14 13:28:36` | `cowrie.command.input` |
| `2026-06-14 13:28:36` | `cowrie.log.closed` |
| `2026-06-14 13:28:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-98bca5396f15

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-14 13:30 |
| **Last Seen** | 2026-06-14 13:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 13:30:57` | `cowrie.session.connect` |
| `2026-06-14 13:30:57` | `cowrie.client.version` |
| `2026-06-14 13:30:57` | `cowrie.client.kex` |
| `2026-06-14 13:30:57` | `cowrie.login.success` |
| `2026-06-14 13:30:58` | `cowrie.session.params` |
| `2026-06-14 13:30:58` | `cowrie.command.input` |
| `2026-06-14 13:30:58` | `cowrie.log.closed` |
| `2026-06-14 13:30:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-74c5188a36e5

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-14 13:33 |
| **Last Seen** | 2026-06-14 13:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 13:33:06` | `cowrie.session.connect` |
| `2026-06-14 13:33:06` | `cowrie.client.version` |
| `2026-06-14 13:33:07` | `cowrie.client.kex` |
| `2026-06-14 13:33:07` | `cowrie.login.success` |
| `2026-06-14 13:33:08` | `cowrie.session.params` |
| `2026-06-14 13:33:08` | `cowrie.command.input` |
| `2026-06-14 13:33:08` | `cowrie.log.closed` |
| `2026-06-14 13:33:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d6e39644b761

| Field | Detail |
|---|---|
| **Source IP** | `125.20.210[.]182` |
| **First Seen** | 2026-06-14 13:33 |
| **Last Seen** | 2026-06-14 13:34 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 13:33:24` | `cowrie.session.connect` |
| `2026-06-14 13:33:26` | `cowrie.telnet.option` |
| `2026-06-14 13:33:28` | `cowrie.telnet.option` |
| `2026-06-14 13:34:29` | `cowrie.login.success` |
| `2026-06-14 13:34:29` | `cowrie.session.params` |

**Recommended Actions:**
- [ ] Submit `125.20.210[.]182` to AbuseIPDB if not already reported
- [ ] Block `125.20.210[.]182` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-613f0a02725d

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-14 13:35 |
| **Last Seen** | 2026-06-14 13:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 13:35:16` | `cowrie.session.connect` |
| `2026-06-14 13:35:16` | `cowrie.client.version` |
| `2026-06-14 13:35:17` | `cowrie.client.kex` |
| `2026-06-14 13:35:17` | `cowrie.login.success` |
| `2026-06-14 13:35:18` | `cowrie.session.params` |
| `2026-06-14 13:35:18` | `cowrie.command.input` |
| `2026-06-14 13:35:18` | `cowrie.log.closed` |
| `2026-06-14 13:35:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8beb675869d1

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-14 13:37 |
| **Last Seen** | 2026-06-14 13:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 13:37:34` | `cowrie.session.connect` |
| `2026-06-14 13:37:34` | `cowrie.client.version` |
| `2026-06-14 13:37:34` | `cowrie.client.kex` |
| `2026-06-14 13:37:34` | `cowrie.login.success` |
| `2026-06-14 13:37:35` | `cowrie.session.params` |
| `2026-06-14 13:37:35` | `cowrie.command.input` |
| `2026-06-14 13:37:35` | `cowrie.log.closed` |
| `2026-06-14 13:37:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e07b9091a994

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-14 13:39 |
| **Last Seen** | 2026-06-14 13:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 13:39:46` | `cowrie.session.connect` |
| `2026-06-14 13:39:46` | `cowrie.client.version` |
| `2026-06-14 13:39:46` | `cowrie.client.kex` |
| `2026-06-14 13:39:46` | `cowrie.login.success` |
| `2026-06-14 13:39:47` | `cowrie.session.params` |
| `2026-06-14 13:39:47` | `cowrie.command.input` |
| `2026-06-14 13:39:47` | `cowrie.log.closed` |
| `2026-06-14 13:39:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e17decd1472e

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-14 13:42 |
| **Last Seen** | 2026-06-14 13:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 13:42:05` | `cowrie.session.connect` |
| `2026-06-14 13:42:05` | `cowrie.client.version` |
| `2026-06-14 13:42:05` | `cowrie.client.kex` |
| `2026-06-14 13:42:05` | `cowrie.login.success` |
| `2026-06-14 13:42:06` | `cowrie.session.params` |
| `2026-06-14 13:42:06` | `cowrie.command.input` |
| `2026-06-14 13:42:06` | `cowrie.log.closed` |
| `2026-06-14 13:42:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9c2df429db20

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-14 13:44 |
| **Last Seen** | 2026-06-14 13:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 13:44:25` | `cowrie.session.connect` |
| `2026-06-14 13:44:25` | `cowrie.client.version` |
| `2026-06-14 13:44:25` | `cowrie.client.kex` |
| `2026-06-14 13:44:25` | `cowrie.login.success` |
| `2026-06-14 13:44:26` | `cowrie.session.params` |
| `2026-06-14 13:44:26` | `cowrie.command.input` |
| `2026-06-14 13:44:26` | `cowrie.log.closed` |
| `2026-06-14 13:44:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1367d3f02444

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-14 13:46 |
| **Last Seen** | 2026-06-14 13:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 13:46:38` | `cowrie.session.connect` |
| `2026-06-14 13:46:38` | `cowrie.client.version` |
| `2026-06-14 13:46:38` | `cowrie.client.kex` |
| `2026-06-14 13:46:38` | `cowrie.login.success` |
| `2026-06-14 13:46:39` | `cowrie.session.params` |
| `2026-06-14 13:46:39` | `cowrie.command.input` |
| `2026-06-14 13:46:40` | `cowrie.log.closed` |
| `2026-06-14 13:46:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-39d54931e6e0

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-14 13:48 |
| **Last Seen** | 2026-06-14 13:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 13:48:54` | `cowrie.session.connect` |
| `2026-06-14 13:48:54` | `cowrie.client.version` |
| `2026-06-14 13:48:54` | `cowrie.client.kex` |
| `2026-06-14 13:48:54` | `cowrie.login.success` |
| `2026-06-14 13:48:55` | `cowrie.session.params` |
| `2026-06-14 13:48:55` | `cowrie.command.input` |
| `2026-06-14 13:48:55` | `cowrie.log.closed` |
| `2026-06-14 13:48:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-18a9fea4f4c2

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-14 13:51 |
| **Last Seen** | 2026-06-14 13:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 13:51:10` | `cowrie.session.connect` |
| `2026-06-14 13:51:10` | `cowrie.client.version` |
| `2026-06-14 13:51:11` | `cowrie.client.kex` |
| `2026-06-14 13:51:11` | `cowrie.login.success` |
| `2026-06-14 13:51:11` | `cowrie.session.params` |
| `2026-06-14 13:51:11` | `cowrie.command.input` |
| `2026-06-14 13:51:12` | `cowrie.log.closed` |
| `2026-06-14 13:51:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fc38a7b39e32

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-14 13:53 |
| **Last Seen** | 2026-06-14 13:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 13:53:22` | `cowrie.session.connect` |
| `2026-06-14 13:53:22` | `cowrie.client.version` |
| `2026-06-14 13:53:22` | `cowrie.client.kex` |
| `2026-06-14 13:53:22` | `cowrie.login.success` |
| `2026-06-14 13:53:23` | `cowrie.session.params` |
| `2026-06-14 13:53:23` | `cowrie.command.input` |
| `2026-06-14 13:53:23` | `cowrie.log.closed` |
| `2026-06-14 13:53:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-78e88179f2fa

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-14 13:55 |
| **Last Seen** | 2026-06-14 13:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 13:55:40` | `cowrie.session.connect` |
| `2026-06-14 13:55:40` | `cowrie.client.version` |
| `2026-06-14 13:55:40` | `cowrie.client.kex` |
| `2026-06-14 13:55:41` | `cowrie.login.success` |
| `2026-06-14 13:55:41` | `cowrie.session.params` |
| `2026-06-14 13:55:42` | `cowrie.command.input` |
| `2026-06-14 13:55:42` | `cowrie.log.closed` |
| `2026-06-14 13:55:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a8c9438ef648

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-14 13:57 |
| **Last Seen** | 2026-06-14 13:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 13:57:59` | `cowrie.session.connect` |
| `2026-06-14 13:57:59` | `cowrie.client.version` |
| `2026-06-14 13:57:59` | `cowrie.client.kex` |
| `2026-06-14 13:57:59` | `cowrie.login.success` |
| `2026-06-14 13:58:00` | `cowrie.session.params` |
| `2026-06-14 13:58:00` | `cowrie.command.input` |
| `2026-06-14 13:58:00` | `cowrie.log.closed` |
| `2026-06-14 13:58:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-611bfe7db360

| Field | Detail |
|---|---|
| **Source IP** | `140.245.67[.]111` |
| **First Seen** | 2026-06-14 13:59 |
| **Last Seen** | 2026-06-14 13:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 13:59:20` | `cowrie.session.connect` |
| `2026-06-14 13:59:20` | `cowrie.client.version` |
| `2026-06-14 13:59:20` | `cowrie.client.kex` |
| `2026-06-14 13:59:21` | `cowrie.login.success` |
| `2026-06-14 13:59:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `140.245.67[.]111` to AbuseIPDB if not already reported
- [ ] Block `140.245.67[.]111` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9696e3108776

| Field | Detail |
|---|---|
| **Source IP** | `140.245.67[.]111` |
| **First Seen** | 2026-06-14 13:59 |
| **Last Seen** | 2026-06-14 13:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 13:59:20` | `cowrie.session.connect` |
| `2026-06-14 13:59:20` | `cowrie.client.version` |
| `2026-06-14 13:59:20` | `cowrie.client.kex` |
| `2026-06-14 13:59:21` | `cowrie.login.success` |
| `2026-06-14 13:59:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `140.245.67[.]111` to AbuseIPDB if not already reported
- [ ] Block `140.245.67[.]111` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5ed23694fa97

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-14 14:00 |
| **Last Seen** | 2026-06-14 14:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 14:00:13` | `cowrie.session.connect` |
| `2026-06-14 14:00:13` | `cowrie.client.version` |
| `2026-06-14 14:00:13` | `cowrie.client.kex` |
| `2026-06-14 14:00:13` | `cowrie.login.success` |
| `2026-06-14 14:00:14` | `cowrie.session.params` |
| `2026-06-14 14:00:14` | `cowrie.command.input` |
| `2026-06-14 14:00:14` | `cowrie.log.closed` |
| `2026-06-14 14:00:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d400ede65b92

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-14 14:02 |
| **Last Seen** | 2026-06-14 14:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 14:02:35` | `cowrie.session.connect` |
| `2026-06-14 14:02:35` | `cowrie.client.version` |
| `2026-06-14 14:02:35` | `cowrie.client.kex` |
| `2026-06-14 14:02:35` | `cowrie.login.success` |
| `2026-06-14 14:02:36` | `cowrie.session.params` |
| `2026-06-14 14:02:36` | `cowrie.command.input` |
| `2026-06-14 14:02:36` | `cowrie.log.closed` |
| `2026-06-14 14:02:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6eb8ab362ca4

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-14 14:04 |
| **Last Seen** | 2026-06-14 14:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 14:04:49` | `cowrie.session.connect` |
| `2026-06-14 14:04:49` | `cowrie.client.version` |
| `2026-06-14 14:04:49` | `cowrie.client.kex` |
| `2026-06-14 14:04:49` | `cowrie.login.success` |
| `2026-06-14 14:04:50` | `cowrie.session.params` |
| `2026-06-14 14:04:50` | `cowrie.command.input` |
| `2026-06-14 14:04:50` | `cowrie.log.closed` |
| `2026-06-14 14:04:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b7109acf5a0c

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-14 14:07 |
| **Last Seen** | 2026-06-14 14:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 14:07:03` | `cowrie.session.connect` |
| `2026-06-14 14:07:03` | `cowrie.client.version` |
| `2026-06-14 14:07:03` | `cowrie.client.kex` |
| `2026-06-14 14:07:03` | `cowrie.login.success` |
| `2026-06-14 14:07:04` | `cowrie.session.params` |
| `2026-06-14 14:07:04` | `cowrie.command.input` |
| `2026-06-14 14:07:04` | `cowrie.log.closed` |
| `2026-06-14 14:07:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cd0136250fdd

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-14 14:09 |
| **Last Seen** | 2026-06-14 14:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 14:09:21` | `cowrie.session.connect` |
| `2026-06-14 14:09:21` | `cowrie.client.version` |
| `2026-06-14 14:09:21` | `cowrie.client.kex` |
| `2026-06-14 14:09:22` | `cowrie.login.success` |
| `2026-06-14 14:09:22` | `cowrie.session.params` |
| `2026-06-14 14:09:22` | `cowrie.command.input` |
| `2026-06-14 14:09:22` | `cowrie.log.closed` |
| `2026-06-14 14:09:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-26483341cf63

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-06-14 14:10 |
| **Last Seen** | 2026-06-14 14:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 14:10:08` | `cowrie.session.connect` |
| `2026-06-14 14:10:08` | `cowrie.client.version` |
| `2026-06-14 14:10:08` | `cowrie.client.kex` |
| `2026-06-14 14:10:09` | `cowrie.login.success` |
| `2026-06-14 14:10:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2e45cde08f15

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-06-14 14:10 |
| **Last Seen** | 2026-06-14 14:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 14:10:08` | `cowrie.session.connect` |
| `2026-06-14 14:10:08` | `cowrie.client.version` |
| `2026-06-14 14:10:08` | `cowrie.client.kex` |
| `2026-06-14 14:10:09` | `cowrie.login.success` |
| `2026-06-14 14:10:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fb74e75975d8

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-14 14:11 |
| **Last Seen** | 2026-06-14 14:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 14:11:33` | `cowrie.session.connect` |
| `2026-06-14 14:11:33` | `cowrie.client.version` |
| `2026-06-14 14:11:33` | `cowrie.client.kex` |
| `2026-06-14 14:11:33` | `cowrie.login.success` |
| `2026-06-14 14:11:34` | `cowrie.session.params` |
| `2026-06-14 14:11:34` | `cowrie.command.input` |
| `2026-06-14 14:11:34` | `cowrie.log.closed` |
| `2026-06-14 14:11:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-932cb5801984

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-14 14:13 |
| **Last Seen** | 2026-06-14 14:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 14:13:50` | `cowrie.session.connect` |
| `2026-06-14 14:13:50` | `cowrie.client.version` |
| `2026-06-14 14:13:50` | `cowrie.client.kex` |
| `2026-06-14 14:13:50` | `cowrie.login.success` |
| `2026-06-14 14:13:51` | `cowrie.session.params` |
| `2026-06-14 14:13:51` | `cowrie.command.input` |
| `2026-06-14 14:13:51` | `cowrie.log.closed` |
| `2026-06-14 14:13:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0839e0b72e04

| Field | Detail |
|---|---|
| **Source IP** | `158.178.141[.]210` |
| **First Seen** | 2026-06-14 14:43 |
| **Last Seen** | 2026-06-14 14:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 14:43:09` | `cowrie.session.connect` |
| `2026-06-14 14:43:09` | `cowrie.client.version` |
| `2026-06-14 14:43:09` | `cowrie.client.kex` |
| `2026-06-14 14:43:10` | `cowrie.login.success` |
| `2026-06-14 14:43:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `158.178.141[.]210` to AbuseIPDB if not already reported
- [ ] Block `158.178.141[.]210` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-49516e1cb1b9

| Field | Detail |
|---|---|
| **Source IP** | `158.178.141[.]210` |
| **First Seen** | 2026-06-14 14:43 |
| **Last Seen** | 2026-06-14 14:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 14:43:09` | `cowrie.session.connect` |
| `2026-06-14 14:43:09` | `cowrie.client.version` |
| `2026-06-14 14:43:09` | `cowrie.client.kex` |
| `2026-06-14 14:43:10` | `cowrie.login.success` |
| `2026-06-14 14:43:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `158.178.141[.]210` to AbuseIPDB if not already reported
- [ ] Block `158.178.141[.]210` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-06f297bb7dbd

| Field | Detail |
|---|---|
| **Source IP** | `158.178.141[.]210` |
| **First Seen** | 2026-06-14 14:43 |
| **Last Seen** | 2026-06-14 14:45 |
| **Session Duration** | 130s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 14:43:29` | `cowrie.session.connect` |
| `2026-06-14 14:43:29` | `cowrie.client.version` |
| `2026-06-14 14:43:29` | `cowrie.client.kex` |
| `2026-06-14 14:43:30` | `cowrie.login.success` |
| `2026-06-14 14:43:32` | `cowrie.session.file_upload` |
| `2026-06-14 14:43:33` | `cowrie.session.params` |
| `2026-06-14 14:43:33` | `cowrie.command.input` |
| `2026-06-14 14:43:33` | `cowrie.command.input` |
| `2026-06-14 14:43:33` | `cowrie.command.input` |
| `2026-06-14 14:43:33` | `cowrie.command.failed` |
| `2026-06-14 14:43:33` | `cowrie.log.closed` |
| `2026-06-14 14:43:34` | `cowrie.session.params` |
| `2026-06-14 14:43:34` | `cowrie.command.input` |
| `2026-06-14 14:43:34` | `cowrie.log.closed` |
| `2026-06-14 14:43:35` | `cowrie.session.params` |
| `2026-06-14 14:43:35` | `cowrie.command.input` |
| `2026-06-14 14:43:35` | `cowrie.log.closed` |
| `2026-06-14 14:43:37` | `cowrie.session.params` |
| `2026-06-14 14:43:37` | `cowrie.command.input` |
| `2026-06-14 14:43:37` | `cowrie.command.failed` |
| `2026-06-14 14:43:37` | `cowrie.command.failed` |
| `2026-06-14 14:44:38` | `cowrie.session.params` |
| `2026-06-14 14:44:38` | `cowrie.command.input` |
| `2026-06-14 14:45:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `158.178.141[.]210` to AbuseIPDB if not already reported
- [ ] Block `158.178.141[.]210` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3a043340e6b3

| Field | Detail |
|---|---|
| **Source IP** | `158.178.141[.]210` |
| **First Seen** | 2026-06-14 14:45 |
| **Last Seen** | 2026-06-14 14:48 |
| **Session Duration** | 130s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 14:45:54` | `cowrie.session.connect` |
| `2026-06-14 14:45:54` | `cowrie.client.version` |
| `2026-06-14 14:45:54` | `cowrie.client.kex` |
| `2026-06-14 14:45:55` | `cowrie.login.success` |
| `2026-06-14 14:45:57` | `cowrie.session.file_upload` |
| `2026-06-14 14:45:58` | `cowrie.session.params` |
| `2026-06-14 14:45:58` | `cowrie.command.input` |
| `2026-06-14 14:45:58` | `cowrie.command.input` |
| `2026-06-14 14:45:58` | `cowrie.command.input` |
| `2026-06-14 14:45:58` | `cowrie.command.failed` |
| `2026-06-14 14:45:59` | `cowrie.log.closed` |
| `2026-06-14 14:46:00` | `cowrie.session.params` |
| `2026-06-14 14:46:00` | `cowrie.command.input` |
| `2026-06-14 14:46:00` | `cowrie.log.closed` |
| `2026-06-14 14:46:01` | `cowrie.session.params` |
| `2026-06-14 14:46:01` | `cowrie.command.input` |
| `2026-06-14 14:46:01` | `cowrie.log.closed` |
| `2026-06-14 14:46:02` | `cowrie.session.params` |
| `2026-06-14 14:46:02` | `cowrie.command.input` |
| `2026-06-14 14:46:02` | `cowrie.command.failed` |
| `2026-06-14 14:46:02` | `cowrie.command.failed` |
| `2026-06-14 14:47:03` | `cowrie.session.params` |
| `2026-06-14 14:47:03` | `cowrie.command.input` |
| `2026-06-14 14:48:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `158.178.141[.]210` to AbuseIPDB if not already reported
- [ ] Block `158.178.141[.]210` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `134.209.93[.]206` | **69** | 2026-06-14 10:58 | 2026-06-14 14:34 | 62m | 0 | `T1592` | 🟠 MEDIUM |
| `188.166.223[.]22` | **22** | 2026-06-14 10:57 | 2026-06-14 14:38 | 17m | 0 | `T1592` | 🟠 MEDIUM |
| `159.65.233[.]253` | **5** | 2026-06-14 11:39 | 2026-06-14 12:27 | 6m | 0 | `T1592` | 🟢 LOW |
| `139.19.117[.]129` | **4** | 2026-06-14 11:22 | 2026-06-14 14:21 | 0m | 8 | `T1110.001 · T1592` | 🟢 LOW |
| `154.16.146[.]65` | **4** | 2026-06-14 12:00 | 2026-06-14 14:54 | 3m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]44` | **3** | 2026-06-14 11:37 | 2026-06-14 11:37 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.186[.]177` | **3** | 2026-06-14 13:01 | 2026-06-14 13:02 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]100` | **3** | 2026-06-14 11:36 | 2026-06-14 11:37 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]55` | **3** | 2026-06-14 11:37 | 2026-06-14 11:38 | 0m | 0 | `T1592` | 🟢 LOW |
| `111.10.246[.]236` | **2** | 2026-06-14 14:48 | 2026-06-14 14:50 | 2m | 0 | `T1592` | 🟢 LOW |
| `180.76.53[.]175` | **2** | 2026-06-14 11:18 | 2026-06-14 11:20 | 2m | 0 | `T1592` | 🟢 LOW |
| `193.8.186[.]31` | **2** | 2026-06-14 13:29 | 2026-06-14 13:29 | 0m | 0 | `T1592` | 🟢 LOW |
| `74.249.128[.]108` | **2** | 2026-06-14 12:56 | 2026-06-14 12:56 | 0m | 0 | `T1592` | 🟢 LOW |
| `103.203.57[.]2` | 1 | 2026-06-14 14:05 | 2026-06-14 14:05 | 10s | 0 | `T1592` | 🟢 LOW |
| `118.26.110[.]171` | 1 | 2026-06-14 10:57 | 2026-06-14 10:57 | 0s | 0 | `T1592` | 🟢 LOW |
| `14.50.83[.]136` | 1 | 2026-06-14 11:39 | 2026-06-14 11:39 | 13s | 0 | `T1592` | 🟢 LOW |
| `176.65.148[.]251` | 1 | 2026-06-14 11:06 | 2026-06-14 11:06 | 0s | 0 | `T1592` | 🟢 LOW |
| `177.130.50[.]21` | 1 | 2026-06-14 14:27 | 2026-06-14 14:28 | 26s | 0 | `T1592` | 🟢 LOW |
| `191.101.96[.]181` | 1 | 2026-06-14 13:18 | 2026-06-14 13:18 | 30s | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]164` | 1 | 2026-06-14 11:37 | 2026-06-14 11:37 | 0s | 0 | `T1592` | 🟢 LOW |
| `206.81.2[.]201` | 1 | 2026-06-14 12:08 | 2026-06-14 12:09 | 39s | 0 | `T1592` | 🟢 LOW |
| `27.0.135[.]6` | 1 | 2026-06-14 11:37 | 2026-06-14 11:37 | 1s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]141` | 1 | 2026-06-14 13:09 | 2026-06-14 13:09 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]183` | 1 | 2026-06-14 12:08 | 2026-06-14 12:08 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.33.14[.]197` | 1 | 2026-06-14 11:35 | 2026-06-14 11:35 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.115[.]59` | 1 | 2026-06-14 12:35 | 2026-06-14 12:35 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.8[.]221` | 1 | 2026-06-14 14:34 | 2026-06-14 14:34 | 0s | 0 | `T1592` | 🟢 LOW |
| `64.62.156[.]122` | 1 | 2026-06-14 14:14 | 2026-06-14 14:14 | 0s | 0 | `T1592` | 🟢 LOW |

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
| `64.110.90[.]250` | KR | Oracle Corporation | **100** ⚠️ | 3 |
| `154.16.146[.]65` | US | OC1-HostForWeb, LLC | **100** ⚠️ | 3 |
| `161.118.237[.]181` | SG | 500 Oracle Parkway | **100** ⚠️ | 2 |
| `177.130.50[.]21` | BR | Wsp Serviços de Telecomunicações Ltda | **100** ⚠️ | 7 |
| `40.233.83[.]131` | CA | Oracle Corporation | **100** ⚠️ | 2 |
| `140.245.67[.]111` | KR | Oracle Corporation | **100** ⚠️ | 2 |
| `188.166.223[.]22` | SG | DigitalOcean, LLC | **100** ⚠️ | 3 |
| `66.132.195[.]100` | US | Censys, Inc. | **100** ⚠️ | 50 |
| `176.65.148[.]251` | NL | Pfcloud UG | **100** ⚠️ | 50 |
| `158.178.141[.]210` | AU | Oracle Corporation | **100** ⚠️ | 2 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 129 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 83 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 7 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 6 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 4 |

---

## 🔕 False Positive Summary (41 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 30 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 11 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 263 cases |
| Tool 34  | Credential Extractor        | ✅ 91 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 13 fingerprints |
| Tool 36  | Command Clustering          | ✅ 4 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 41 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 41 filtered (15.6%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 26 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 35 files |
| Tool 33  | YARA Classifier             | ✅ 10 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 83 priority case(s) shown individually · 28 recon entry/entries in table (13 group(s) consolidating 124 session(s)).

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
_Report time: 2026-06-14T15:50:46Z_

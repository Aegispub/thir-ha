# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-06-20 |
| **Generated At** | 2026-06-20T23:13:11Z |
| **Shift Time** | 23:13 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **181** |
| Confirmed Threats | **145** |
| False Positives Filtered | **36** (19.9%) |
| Unique Attacker IPs | **23** |
| Countries of Origin | **11** |
| High Severity Cases | **34** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **147** |
| Malware Samples Analyzed | **1** HIGH · **15** MED · 1 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **35** |
| Unique Credential Pairs | **25** |
| Unique Usernames | **8** |
| Unique Passwords | **24** |
| Successful Auth Pairs | **27** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 24 |
| `ubuntu` | 4 |
| `admin` | 2 |
| `lq` | 1 |
| `web2` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `smo@@kkklss` | 6 |
| `LeitboGi0ro` | 3 |
| `123@@@` | 3 |
| `admin` | 3 |
| `qweasd` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `smo@@kkklss` | 6 |
| `root` | `LeitboGi0ro` | 3 |
| `root` | `123@@@` | 3 |
| `admin` | `admin` | 2 |
| `ubuntu` | `qweasd` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `LeitboGi0ro` | `144.22.238.238` | 2026-06-20T20:57:03 |
| `root` | `123@@@` | `144.22.238.238` | 2026-06-20T20:57:03 |
| `root` | `smo@@kkklss` | `144.22.238.238` | 2026-06-20T20:57:06 |
| `ubuntu` | `qweasd` | `45.205.1.42` | 2026-06-20T20:57:31 |
| `ubuntu` | `demo123456789` | `45.198.224.120` | 2026-06-20T20:59:43 |
| `ubuntu` | `abcdpass` | `45.198.224.120` | 2026-06-20T21:08:01 |
| `admin` | `admin` | `10.0.0.73` | 2026-06-20T21:13:23 |
| `root` | `quality` | `45.198.224.120` | 2026-06-20T21:16:28 |
| `lq` | `lq123` | `45.205.1.42` | 2026-06-20T21:17:33 |
| `root` | `Qwe123!!` | `45.198.224.120` | 2026-06-20T21:24:47 |
| `web2` | `123` | `45.198.224.120` | 2026-06-20T21:32:59 |
| `root` | `123@@@` | `129.153.145.135` | 2026-06-20T21:33:53 |
| `root` | `LeitboGi0ro` | `129.153.145.135` | 2026-06-20T21:33:54 |
| `root` | `smo@@kkklss` | `129.153.145.135` | 2026-06-20T21:34:02 |
| `root` | `102030` | `45.205.1.42` | 2026-06-20T21:37:45 |
| `root` | `qwe123qwe123` | `45.198.224.120` | 2026-06-20T21:40:54 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:2323` | `147.185.132.223` | 2026-06-20T21:53:42 |
| `root` | `Parole12` | `45.198.224.120` | 2026-06-20T21:58:03 |
| `root` | `missionimposible` | `45.205.1.42` | 2026-06-20T21:58:22 |
| `root` | `---fuck_you----` | `10.0.0.73` | 2026-06-20T21:59:13 |
| `root` | `Abcd@1234` | `45.198.224.120` | 2026-06-20T22:23:12 |
| `ubuntu` | `q1w2` | `45.198.224.120` | 2026-06-20T22:31:33 |
| `usuario` | `michael` | `45.198.224.120` | 2026-06-20T22:39:58 |
| `lxl` | `lxl` | `209.99.187.52` | 2026-06-20T22:41:55 |
| `root` | `﻿------fuck------` | `10.0.0.73` | 2026-06-20T22:45:41 |
| `root` | `mHLPWHMfn6gd` | `209.99.187.52` | 2026-06-20T22:49:34 |
| `root` | `admin` | `14.55.31.113` | 2026-06-20T22:51:12 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **181** |
| Sessions with Fingerprint | **10** |
| Unique HASSH Fingerprints | **10** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 40 |
| Paramiko (Python) | 12 |
| OpenSSH | 5 |
| Unknown | 2 |
| libssh | 2 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `16443846184e...` | Generic scanner | 17 | 4 |
| `a2de0f306611...` | Mirai/variant | 12 | 2 |
| `a984ff804585...` | libssh-based | 5 | 1 |
| `98f63c4d9c87...` | Generic scanner | 2 | 1 |
| `dd9bcf093c35...` | Mirai/variant | 2 | 2 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `95420f9d932d...` | Go SSH scanner | 19 | 7 | — |
| `16443846184e...` | Go SSH scanner | 17 | 4 | Generic scanner |
| `a2de0f306611...` | Paramiko (Python) | 12 | 2 | Mirai/variant |
| `a984ff804585...` | OpenSSH | 5 | 1 | libssh-based |
| `98f63c4d9c87...` | Go SSH scanner | 2 | 1 | Generic scanner |
| `dd9bcf093c35...` | Unknown | 2 | 2 | Mirai/variant |
| `19532158b559...` | libssh | 1 | 1 | Mirai/variant |
| `5f904648ee89...` | Go SSH scanner | 1 | 1 | Generic scanner |

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **23** |
| Unique ASNs | **13** |
| High-Risk ASNs | **10** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS396982` | Google LLC | 6 | LOW |
| `AS14061` | DigitalOcean, LLC | 3 | HIGH |
| `AS215925` | VPSVAULT.HOST LTD | 2 | HIGH |
| `AS63949` | Akamai Connected Cloud | 2 | HIGH |
| `AS31898` | Oracle Corporation | 2 | HIGH |
| `AS0` |  | 1 | LOW |
| `AS48090` | TECHOFF SRV LIMITED | 1 | HIGH |
| `AS267784` | Flyservers S.A. | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (29)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-f80866493aee

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-06-20 20:57 |
| **Last Seen** | 2026-06-20 20:57 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 20:57:02` | `cowrie.session.connect` |
| `2026-06-20 20:57:02` | `cowrie.client.version` |
| `2026-06-20 20:57:02` | `cowrie.client.kex` |
| `2026-06-20 20:57:03` | `cowrie.login.success` |
| `2026-06-20 20:57:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1491fee5f926

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-06-20 20:57 |
| **Last Seen** | 2026-06-20 20:57 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 20:57:02` | `cowrie.session.connect` |
| `2026-06-20 20:57:02` | `cowrie.client.version` |
| `2026-06-20 20:57:03` | `cowrie.client.kex` |
| `2026-06-20 20:57:03` | `cowrie.login.success` |
| `2026-06-20 20:57:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7401064f8b48

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-06-20 20:57 |
| **Last Seen** | 2026-06-20 20:57 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 20:57:05` | `cowrie.session.connect` |
| `2026-06-20 20:57:05` | `cowrie.client.version` |
| `2026-06-20 20:57:06` | `cowrie.client.kex` |
| `2026-06-20 20:57:06` | `cowrie.login.success` |
| `2026-06-20 20:57:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2bfaaae7ad2e

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-06-20 20:57 |
| **Last Seen** | 2026-06-20 20:57 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 20:57:06` | `cowrie.session.connect` |
| `2026-06-20 20:57:06` | `cowrie.client.version` |
| `2026-06-20 20:57:06` | `cowrie.client.kex` |
| `2026-06-20 20:57:07` | `cowrie.login.success` |
| `2026-06-20 20:57:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c94ef1d9a5f5

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-20 20:57 |
| **Last Seen** | 2026-06-20 20:57 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 20:57:20` | `cowrie.session.connect` |
| `2026-06-20 20:57:22` | `cowrie.client.version` |
| `2026-06-20 20:57:22` | `cowrie.client.kex` |
| `2026-06-20 20:57:31` | `cowrie.login.success` |
| `2026-06-20 20:57:36` | `cowrie.session.params` |
| `2026-06-20 20:57:36` | `cowrie.command.input` |
| `2026-06-20 20:57:38` | `cowrie.log.closed` |
| `2026-06-20 20:57:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0b04d7532a96

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-20 20:59 |
| **Last Seen** | 2026-06-20 20:59 |
| **Session Duration** | 33s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 20:59:23` | `cowrie.session.connect` |
| `2026-06-20 20:59:26` | `cowrie.client.version` |
| `2026-06-20 20:59:26` | `cowrie.client.kex` |
| `2026-06-20 20:59:43` | `cowrie.login.success` |
| `2026-06-20 20:59:54` | `cowrie.session.params` |
| `2026-06-20 20:59:54` | `cowrie.command.input` |
| `2026-06-20 20:59:57` | `cowrie.log.closed` |
| `2026-06-20 20:59:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3bfdca75fc14

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-20 21:07 |
| **Last Seen** | 2026-06-20 21:08 |
| **Session Duration** | 33s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 21:07:40` | `cowrie.session.connect` |
| `2026-06-20 21:07:44` | `cowrie.client.version` |
| `2026-06-20 21:07:44` | `cowrie.client.kex` |
| `2026-06-20 21:08:01` | `cowrie.login.success` |
| `2026-06-20 21:08:09` | `cowrie.session.params` |
| `2026-06-20 21:08:09` | `cowrie.command.input` |
| `2026-06-20 21:08:14` | `cowrie.log.closed` |
| `2026-06-20 21:08:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c9a6e2a5af82

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-20 21:16 |
| **Last Seen** | 2026-06-20 21:16 |
| **Session Duration** | 34s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 21:16:07` | `cowrie.session.connect` |
| `2026-06-20 21:16:11` | `cowrie.client.version` |
| `2026-06-20 21:16:11` | `cowrie.client.kex` |
| `2026-06-20 21:16:28` | `cowrie.login.success` |
| `2026-06-20 21:16:38` | `cowrie.session.params` |
| `2026-06-20 21:16:38` | `cowrie.command.input` |
| `2026-06-20 21:16:42` | `cowrie.log.closed` |
| `2026-06-20 21:16:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-138e06fcb7aa

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-20 21:17 |
| **Last Seen** | 2026-06-20 21:17 |
| **Session Duration** | 18s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 21:17:20` | `cowrie.session.connect` |
| `2026-06-20 21:17:22` | `cowrie.client.version` |
| `2026-06-20 21:17:22` | `cowrie.client.kex` |
| `2026-06-20 21:17:33` | `cowrie.login.success` |
| `2026-06-20 21:17:37` | `cowrie.session.params` |
| `2026-06-20 21:17:37` | `cowrie.command.input` |
| `2026-06-20 21:17:39` | `cowrie.log.closed` |
| `2026-06-20 21:17:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4d1fcc96c0d4

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-20 21:24 |
| **Last Seen** | 2026-06-20 21:25 |
| **Session Duration** | 34s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 21:24:27` | `cowrie.session.connect` |
| `2026-06-20 21:24:30` | `cowrie.client.version` |
| `2026-06-20 21:24:30` | `cowrie.client.kex` |
| `2026-06-20 21:24:47` | `cowrie.login.success` |
| `2026-06-20 21:24:59` | `cowrie.session.params` |
| `2026-06-20 21:24:59` | `cowrie.command.input` |
| `2026-06-20 21:25:02` | `cowrie.log.closed` |
| `2026-06-20 21:25:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-46b0c441988e

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-20 21:32 |
| **Last Seen** | 2026-06-20 21:33 |
| **Session Duration** | 34s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 21:32:37` | `cowrie.session.connect` |
| `2026-06-20 21:32:41` | `cowrie.client.version` |
| `2026-06-20 21:32:41` | `cowrie.client.kex` |
| `2026-06-20 21:32:59` | `cowrie.login.success` |
| `2026-06-20 21:33:09` | `cowrie.session.params` |
| `2026-06-20 21:33:09` | `cowrie.command.input` |
| `2026-06-20 21:33:12` | `cowrie.log.closed` |
| `2026-06-20 21:33:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ce7e63a5d4d5

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-20 21:33 |
| **Last Seen** | 2026-06-20 21:33 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 21:33:53` | `cowrie.session.connect` |
| `2026-06-20 21:33:53` | `cowrie.client.version` |
| `2026-06-20 21:33:53` | `cowrie.client.kex` |
| `2026-06-20 21:33:53` | `cowrie.login.success` |
| `2026-06-20 21:33:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1a69c158c31c

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-20 21:33 |
| **Last Seen** | 2026-06-20 21:33 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 21:33:54` | `cowrie.session.connect` |
| `2026-06-20 21:33:54` | `cowrie.client.version` |
| `2026-06-20 21:33:54` | `cowrie.client.kex` |
| `2026-06-20 21:33:54` | `cowrie.login.success` |
| `2026-06-20 21:33:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-342ef9f7ab13

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-20 21:34 |
| **Last Seen** | 2026-06-20 21:34 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 21:34:02` | `cowrie.session.connect` |
| `2026-06-20 21:34:02` | `cowrie.client.version` |
| `2026-06-20 21:34:02` | `cowrie.client.kex` |
| `2026-06-20 21:34:02` | `cowrie.login.success` |
| `2026-06-20 21:34:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f058bd7b9839

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-20 21:34 |
| **Last Seen** | 2026-06-20 21:34 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 21:34:02` | `cowrie.session.connect` |
| `2026-06-20 21:34:02` | `cowrie.client.version` |
| `2026-06-20 21:34:02` | `cowrie.client.kex` |
| `2026-06-20 21:34:02` | `cowrie.login.success` |
| `2026-06-20 21:34:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aae9953f6abb

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-20 21:37 |
| **Last Seen** | 2026-06-20 21:37 |
| **Session Duration** | 20s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 21:37:33` | `cowrie.session.connect` |
| `2026-06-20 21:37:37` | `cowrie.client.version` |
| `2026-06-20 21:37:37` | `cowrie.client.kex` |
| `2026-06-20 21:37:45` | `cowrie.login.success` |
| `2026-06-20 21:37:51` | `cowrie.session.params` |
| `2026-06-20 21:37:51` | `cowrie.command.input` |
| `2026-06-20 21:37:53` | `cowrie.log.closed` |
| `2026-06-20 21:37:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e0af5630dc6c

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-20 21:40 |
| **Last Seen** | 2026-06-20 21:41 |
| **Session Duration** | 24s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 21:40:40` | `cowrie.session.connect` |
| `2026-06-20 21:40:43` | `cowrie.client.version` |
| `2026-06-20 21:40:43` | `cowrie.client.kex` |
| `2026-06-20 21:40:54` | `cowrie.login.success` |
| `2026-06-20 21:41:02` | `cowrie.session.params` |
| `2026-06-20 21:41:02` | `cowrie.command.input` |
| `2026-06-20 21:41:05` | `cowrie.log.closed` |
| `2026-06-20 21:41:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-081e7e719251

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-20 21:57 |
| **Last Seen** | 2026-06-20 21:58 |
| **Session Duration** | 23s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 21:57:50` | `cowrie.session.connect` |
| `2026-06-20 21:57:53` | `cowrie.client.version` |
| `2026-06-20 21:57:53` | `cowrie.client.kex` |
| `2026-06-20 21:58:03` | `cowrie.login.success` |
| `2026-06-20 21:58:11` | `cowrie.session.params` |
| `2026-06-20 21:58:11` | `cowrie.command.input` |
| `2026-06-20 21:58:14` | `cowrie.log.closed` |
| `2026-06-20 21:58:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5d225fe8558c

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-20 21:58 |
| **Last Seen** | 2026-06-20 21:58 |
| **Session Duration** | 19s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 21:58:11` | `cowrie.session.connect` |
| `2026-06-20 21:58:12` | `cowrie.client.version` |
| `2026-06-20 21:58:12` | `cowrie.client.kex` |
| `2026-06-20 21:58:22` | `cowrie.login.success` |
| `2026-06-20 21:58:28` | `cowrie.session.params` |
| `2026-06-20 21:58:28` | `cowrie.command.input` |
| `2026-06-20 21:58:30` | `cowrie.log.closed` |
| `2026-06-20 21:58:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8e9a44139dfa

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-06-20 22:19 |
| **Last Seen** | 2026-06-20 22:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 22:19:23` | `cowrie.session.connect` |
| `2026-06-20 22:19:23` | `cowrie.client.version` |
| `2026-06-20 22:19:23` | `cowrie.client.kex` |
| `2026-06-20 22:19:23` | `cowrie.login.success` |
| `2026-06-20 22:19:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-18f3466eae09

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-06-20 22:19 |
| **Last Seen** | 2026-06-20 22:19 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 22:19:24` | `cowrie.session.connect` |
| `2026-06-20 22:19:24` | `cowrie.client.version` |
| `2026-06-20 22:19:24` | `cowrie.client.kex` |
| `2026-06-20 22:19:24` | `cowrie.login.success` |
| `2026-06-20 22:19:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a4d5b20575d1

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-06-20 22:19 |
| **Last Seen** | 2026-06-20 22:19 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 22:19:28` | `cowrie.session.connect` |
| `2026-06-20 22:19:28` | `cowrie.client.version` |
| `2026-06-20 22:19:29` | `cowrie.client.kex` |
| `2026-06-20 22:19:29` | `cowrie.login.success` |
| `2026-06-20 22:19:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fa707beccdf7

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-06-20 22:19 |
| **Last Seen** | 2026-06-20 22:19 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 22:19:29` | `cowrie.session.connect` |
| `2026-06-20 22:19:29` | `cowrie.client.version` |
| `2026-06-20 22:19:30` | `cowrie.client.kex` |
| `2026-06-20 22:19:30` | `cowrie.login.success` |
| `2026-06-20 22:19:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-784f045c240e

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-20 22:22 |
| **Last Seen** | 2026-06-20 22:23 |
| **Session Duration** | 27s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 22:22:56` | `cowrie.session.connect` |
| `2026-06-20 22:22:59` | `cowrie.client.version` |
| `2026-06-20 22:22:59` | `cowrie.client.kex` |
| `2026-06-20 22:23:12` | `cowrie.login.success` |
| `2026-06-20 22:23:18` | `cowrie.session.params` |
| `2026-06-20 22:23:18` | `cowrie.command.input` |
| `2026-06-20 22:23:23` | `cowrie.log.closed` |
| `2026-06-20 22:23:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-04d758e94827

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-20 22:31 |
| **Last Seen** | 2026-06-20 22:31 |
| **Session Duration** | 28s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 22:31:16` | `cowrie.session.connect` |
| `2026-06-20 22:31:19` | `cowrie.client.version` |
| `2026-06-20 22:31:19` | `cowrie.client.kex` |
| `2026-06-20 22:31:33` | `cowrie.login.success` |
| `2026-06-20 22:31:42` | `cowrie.session.params` |
| `2026-06-20 22:31:42` | `cowrie.command.input` |
| `2026-06-20 22:31:45` | `cowrie.log.closed` |
| `2026-06-20 22:31:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1da0a1616d0e

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-20 22:39 |
| **Last Seen** | 2026-06-20 22:40 |
| **Session Duration** | 34s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 22:39:38` | `cowrie.session.connect` |
| `2026-06-20 22:39:41` | `cowrie.client.version` |
| `2026-06-20 22:39:41` | `cowrie.client.kex` |
| `2026-06-20 22:39:58` | `cowrie.login.success` |
| `2026-06-20 22:40:08` | `cowrie.session.params` |
| `2026-06-20 22:40:08` | `cowrie.command.input` |
| `2026-06-20 22:40:12` | `cowrie.log.closed` |
| `2026-06-20 22:40:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a7157ba07ffc

| Field | Detail |
|---|---|
| **Source IP** | `209.99.187[.]52` |
| **First Seen** | 2026-06-20 22:41 |
| **Last Seen** | 2026-06-20 22:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 22:41:54` | `cowrie.session.connect` |
| `2026-06-20 22:41:54` | `cowrie.client.version` |
| `2026-06-20 22:41:54` | `cowrie.client.kex` |
| `2026-06-20 22:41:55` | `cowrie.login.success` |
| `2026-06-20 22:41:56` | `cowrie.session.params` |
| `2026-06-20 22:41:56` | `cowrie.command.input` |
| `2026-06-20 22:41:56` | `cowrie.log.closed` |
| `2026-06-20 22:41:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.187[.]52` to AbuseIPDB if not already reported
- [ ] Block `209.99.187[.]52` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5a4413cf32c9

| Field | Detail |
|---|---|
| **Source IP** | `209.99.187[.]52` |
| **First Seen** | 2026-06-20 22:49 |
| **Last Seen** | 2026-06-20 22:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 22:49:33` | `cowrie.session.connect` |
| `2026-06-20 22:49:33` | `cowrie.client.version` |
| `2026-06-20 22:49:34` | `cowrie.client.kex` |
| `2026-06-20 22:49:34` | `cowrie.login.success` |
| `2026-06-20 22:49:35` | `cowrie.session.params` |
| `2026-06-20 22:49:35` | `cowrie.command.input` |
| `2026-06-20 22:49:35` | `cowrie.log.closed` |
| `2026-06-20 22:49:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.187[.]52` to AbuseIPDB if not already reported
- [ ] Block `209.99.187[.]52` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-005d6177fe31

| Field | Detail |
|---|---|
| **Source IP** | `14.55.31[.]113` |
| **First Seen** | 2026-06-20 22:51 |
| **Last Seen** | 2026-06-20 22:51 |
| **Session Duration** | 48s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/ip cloud print, ifconfig, uname -a, cat /proc/cpuinfo, ps | grep '[Mm]iner'` |
| **TTPs (MITRE)** | T1057 · T1078 · T1083 · T1110.001 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 22:51:09` | `cowrie.session.connect` |
| `2026-06-20 22:51:09` | `cowrie.client.version` |
| `2026-06-20 22:51:10` | `cowrie.client.kex` |
| `2026-06-20 22:51:11` | `cowrie.login.failed` |
| `2026-06-20 22:51:12` | `cowrie.login.success` |
| `2026-06-20 22:51:13` | `cowrie.session.params` |
| `2026-06-20 22:51:13` | `cowrie.command.input` |
| `2026-06-20 22:51:13` | `cowrie.command.failed` |
| `2026-06-20 22:51:13` | `cowrie.log.closed` |
| `2026-06-20 22:51:14` | `cowrie.session.params` |
| `2026-06-20 22:51:14` | `cowrie.command.input` |
| `2026-06-20 22:51:14` | `cowrie.log.closed` |
| `2026-06-20 22:51:15` | `cowrie.session.params` |
| `2026-06-20 22:51:15` | `cowrie.command.input` |
| `2026-06-20 22:51:15` | `cowrie.log.closed` |
| `2026-06-20 22:51:16` | `cowrie.session.params` |
| `2026-06-20 22:51:16` | `cowrie.command.input` |
| `2026-06-20 22:51:17` | `cowrie.log.closed` |
| `2026-06-20 22:51:18` | `cowrie.session.params` |
| `2026-06-20 22:51:18` | `cowrie.command.input` |
| `2026-06-20 22:51:18` | `cowrie.log.closed` |
| `2026-06-20 22:51:19` | `cowrie.session.params` |
| `2026-06-20 22:51:19` | `cowrie.command.input` |
| `2026-06-20 22:51:19` | `cowrie.log.closed` |
| `2026-06-20 22:51:20` | `cowrie.session.params` |
| `2026-06-20 22:51:20` | `cowrie.command.input` |
| `2026-06-20 22:51:20` | `cowrie.log.closed` |
| `2026-06-20 22:51:21` | `cowrie.session.params` |
| `2026-06-20 22:51:21` | `cowrie.command.input` |
| `2026-06-20 22:51:22` | `cowrie.log.closed` |
| `2026-06-20 22:51:23` | `cowrie.session.params` |
| `2026-06-20 22:51:23` | `cowrie.command.input` |
| `2026-06-20 22:51:23` | `cowrie.log.closed` |
| `2026-06-20 22:51:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.55.31[.]113` to AbuseIPDB if not already reported
- [ ] Block `14.55.31[.]113` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `138.68.100[.]228` | **97** | 2026-06-20 20:55 | 2026-06-20 22:50 | 103m | 0 | `T1592` | 🟠 MEDIUM |
| `45.198.224[.]120` | **4** | 2026-06-20 21:49 | 2026-06-20 22:47 | 0m | 0 | `T1592` | 🟢 LOW |
| `209.99.187[.]52` | **3** | 2026-06-20 22:30 | 2026-06-20 22:49 | 0m | 0 | `T1592` | 🟢 LOW |
| `45.205.1[.]42` | **2** | 2026-06-20 22:19 | 2026-06-20 22:39 | 0m | 0 | `T1592` | 🟢 LOW |
| `47.84.134[.]121` | **2** | 2026-06-20 22:29 | 2026-06-20 22:29 | 0m | 0 | `T1592` | 🟢 LOW |
| `48.214.144[.]160` | **2** | 2026-06-20 20:56 | 2026-06-20 20:56 | 0m | 0 | `T1592` | 🟢 LOW |
| `159.65.233[.]253` | 1 | 2026-06-20 21:54 | 2026-06-20 21:55 | 89s | 0 | `T1592` | 🟢 LOW |
| `206.81.2[.]201` | 1 | 2026-06-20 22:05 | 2026-06-20 22:05 | 40s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]121` | 1 | 2026-06-20 22:54 | 2026-06-20 22:54 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.227.254[.]155` | 1 | 2026-06-20 21:20 | 2026-06-20 21:20 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.33.12[.]122` | 1 | 2026-06-20 20:57 | 2026-06-20 20:57 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.33.14[.]197` | 1 | 2026-06-20 21:38 | 2026-06-20 21:38 | 0s | 0 | `T1592` | 🟢 LOW |

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
| `45.198.224[.]120` | NL | VPSVAULT.HOST LTD | **100** ⚠️ | 3 |
| `144.22.238[.]238` | BR | Oracle Corporation | **100** ⚠️ | 3 |
| `47.84.134[.]121` | SG | Alibaba Cloud LLC | **100** ⚠️ | 24 |
| `206.81.2[.]201` | US | DigitalOcean, LLC | **100** ⚠️ | 9 |
| `209.99.187[.]52` | CH | SKN Subnet & Telecom Ltd | **100** ⚠️ | 18 |
| `45.205.1[.]42` | BR | VPSVAULT.HOST LTD | **100** ⚠️ | 7 |
| `159.65.233[.]253` | US | DigitalOcean, LLC | **100** ⚠️ | 3 |
| `48.214.144[.]160` | US | Microsoft Limited | **100** ⚠️ | 50 |
| `129.153.145[.]135` | US | Oracle Corporation | **100** ⚠️ | 8 |
| `14.55.31[.]113` | KR | Jeonbukbonbujang | **100** ⚠️ | 28 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 62 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 34 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 2 |
| [T1057](https://attack.mitre.org/techniques/T1057) | 1 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 1 |

---

## 🔕 False Positive Summary (36 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 31 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 5 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 181 cases |
| Tool 34  | Credential Extractor        | ✅ 35 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 10 fingerprints |
| Tool 36  | Command Clustering          | ✅ 5 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 23 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 36 filtered (19.9%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 13 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 17 files |
| Tool 33  | YARA Classifier             | ✅ 13 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 29 priority case(s) shown individually · 12 recon entry/entries in table (6 group(s) consolidating 110 session(s)).

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
_Report time: 2026-06-20T23:13:11Z_

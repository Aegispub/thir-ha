# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-06-16 |
| **Generated At** | 2026-06-16T11:19:56Z |
| **Shift Time** | 11:19 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **98** |
| Confirmed Threats | **70** |
| False Positives Filtered | **28** (28.6%) |
| Unique Attacker IPs | **40** |
| Countries of Origin | **15** |
| High Severity Cases | **23** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **75** |
| Malware Samples Analyzed | **1** HIGH · **15** MED · 1 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **23** |
| Unique Credential Pairs | **18** |
| Unique Usernames | **8** |
| Unique Passwords | **18** |
| Successful Auth Pairs | **22** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 8 |
| `admin` | 5 |
| `sol` | 3 |
| `ubuntu` | 3 |
| `trading` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `admin` | 3 |
| `123@@@` | 2 |
| `LeitboGi0ro` | 2 |
| `smo@@kkklss` | 2 |
| `sol` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `admin` | `admin` | 3 |
| `root` | `123@@@` | 2 |
| `root` | `LeitboGi0ro` | 2 |
| `root` | `smo@@kkklss` | 2 |
| `sol` | `sol` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `sol` | `sol` | `45.148.10.183` | 2026-06-16T08:56:11 |
| `sol` | `123` | `45.148.10.183` | 2026-06-16T08:58:25 |
| `sol` | `1234` | `45.148.10.183` | 2026-06-16T09:00:45 |
| `root` | `123@@@` | `144.22.238.238` | 2026-06-16T09:01:52 |
| `root` | `LeitboGi0ro` | `144.22.238.238` | 2026-06-16T09:01:53 |
| `root` | `smo@@kkklss` | `144.22.238.238` | 2026-06-16T09:01:57 |
| `ubuntu` | `ubuntu` | `45.148.10.183` | 2026-06-16T09:02:56 |
| `ubuntu` | `123456` | `45.148.10.183` | 2026-06-16T09:05:13 |
| `ubuntu` | `12345678` | `45.148.10.183` | 2026-06-16T09:07:28 |
| `trading` | `trading` | `45.148.10.183` | 2026-06-16T09:09:38 |
| `trader` | `trader123` | `45.148.10.183` | 2026-06-16T09:11:53 |
| `pool` | `pool` | `45.148.10.183` | 2026-06-16T09:14:07 |
| `root` | `---fuck_you----` | `10.0.0.73` | 2026-06-16T09:22:15 |
| `admin` | `admin` | `168.110.107.79` | 2026-06-16T09:48:02 |
| `admin` | `password` | `185.93.89.95` | 2026-06-16T09:48:08 |
| `root` | `tSrzQfOy21` | `10.0.0.73` | 2026-06-16T09:50:57 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:2223` | `172.236.228.224` | 2026-06-16T10:18:21 |
| `admin` | `default` | `185.93.89.95` | 2026-06-16T10:21:59 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-06-16T10:25:30 |
| `root` | `123@@@` | `64.110.90.250` | 2026-06-16T10:25:30 |
| `admin` | `admin` | `130.49.189.41` | 2026-06-16T10:41:50 |
| `admin` | `admin` | `130.12.180.51` | 2026-06-16T10:41:51 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **98** |
| Sessions with Fingerprint | **13** |
| Unique HASSH Fingerprints | **13** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 17 |
| libssh | 14 |
| Paramiko (Python) | 6 |
| OpenSSH | 5 |
| Unknown | 2 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `16443846184e...` | Generic scanner | 12 | 3 |
| `a2de0f306611...` | Mirai/variant | 6 | 2 |
| `a984ff804585...` | libssh-based | 5 | 1 |
| `98f63c4d9c87...` | Generic scanner | 2 | 2 |
| `2aec6b44b06b...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `95420f9d932d...` | libssh | 13 | 3 | — |
| `16443846184e...` | Go SSH scanner | 12 | 3 | Generic scanner |
| `a2de0f306611...` | Paramiko (Python) | 6 | 2 | Mirai/variant |
| `a984ff804585...` | OpenSSH | 5 | 1 | libssh-based |
| `98f63c4d9c87...` | Go SSH scanner | 2 | 2 | Generic scanner |
| `2aec6b44b06b...` | Go SSH scanner | 1 | 1 | Mirai/variant |
| `084386fa7ae5...` | Go SSH scanner | 1 | 1 | Mirai/variant |
| `1b8acd46a07d...` | Unknown | 1 | 1 | Modern SSH client |

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **40** |
| Unique ASNs | **26** |
| High-Risk ASNs | **19** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS63949` | Akamai Connected Cloud | 5 | HIGH |
| `AS4134` | CHINANET BACKBONE | 4 | HIGH |
| `AS14061` | DigitalOcean, LLC | 3 | HIGH |
| `AS31898` | Oracle Corporation | 3 | HIGH |
| `AS209334` | Modat B.V. | 2 | HIGH |
| `AS25369` | Hydra Communications Ltd | 2 | HIGH |
| `AS48090` | TECHOFF SRV LIMITED | 2 | HIGH |
| `AS58224` | Iran Telecommunication Company PJS | 1 | LOW |

---

---

## 🚨 Priority Cases — Immediate Attention (21)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-4675b010d27f

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-16 08:56 |
| **Last Seen** | 2026-06-16 08:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-16 08:56:11` | `cowrie.session.connect` |
| `2026-06-16 08:56:11` | `cowrie.client.version` |
| `2026-06-16 08:56:11` | `cowrie.client.kex` |
| `2026-06-16 08:56:11` | `cowrie.login.success` |
| `2026-06-16 08:56:12` | `cowrie.session.params` |
| `2026-06-16 08:56:12` | `cowrie.command.input` |
| `2026-06-16 08:56:12` | `cowrie.log.closed` |
| `2026-06-16 08:56:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-49002a1806c1

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-16 08:58 |
| **Last Seen** | 2026-06-16 08:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-16 08:58:25` | `cowrie.session.connect` |
| `2026-06-16 08:58:25` | `cowrie.client.version` |
| `2026-06-16 08:58:25` | `cowrie.client.kex` |
| `2026-06-16 08:58:25` | `cowrie.login.success` |
| `2026-06-16 08:58:26` | `cowrie.session.params` |
| `2026-06-16 08:58:26` | `cowrie.command.input` |
| `2026-06-16 08:58:26` | `cowrie.log.closed` |
| `2026-06-16 08:58:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e84d11e0c4bd

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-16 09:00 |
| **Last Seen** | 2026-06-16 09:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-16 09:00:44` | `cowrie.session.connect` |
| `2026-06-16 09:00:44` | `cowrie.client.version` |
| `2026-06-16 09:00:44` | `cowrie.client.kex` |
| `2026-06-16 09:00:45` | `cowrie.login.success` |
| `2026-06-16 09:00:45` | `cowrie.session.params` |
| `2026-06-16 09:00:45` | `cowrie.command.input` |
| `2026-06-16 09:00:45` | `cowrie.log.closed` |
| `2026-06-16 09:00:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-622a065ecf14

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-06-16 09:01 |
| **Last Seen** | 2026-06-16 09:01 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-16 09:01:52` | `cowrie.session.connect` |
| `2026-06-16 09:01:52` | `cowrie.client.version` |
| `2026-06-16 09:01:52` | `cowrie.client.kex` |
| `2026-06-16 09:01:52` | `cowrie.login.success` |
| `2026-06-16 09:01:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-108de473888f

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-06-16 09:01 |
| **Last Seen** | 2026-06-16 09:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-16 09:01:52` | `cowrie.session.connect` |
| `2026-06-16 09:01:52` | `cowrie.client.version` |
| `2026-06-16 09:01:52` | `cowrie.client.kex` |
| `2026-06-16 09:01:53` | `cowrie.login.success` |
| `2026-06-16 09:01:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-670911362225

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-06-16 09:01 |
| **Last Seen** | 2026-06-16 09:01 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-16 09:01:57` | `cowrie.session.connect` |
| `2026-06-16 09:01:57` | `cowrie.client.version` |
| `2026-06-16 09:01:57` | `cowrie.client.kex` |
| `2026-06-16 09:01:57` | `cowrie.login.success` |
| `2026-06-16 09:01:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f763652acfb2

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-06-16 09:01 |
| **Last Seen** | 2026-06-16 09:01 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-16 09:01:58` | `cowrie.session.connect` |
| `2026-06-16 09:01:58` | `cowrie.client.version` |
| `2026-06-16 09:01:58` | `cowrie.client.kex` |
| `2026-06-16 09:01:58` | `cowrie.login.success` |
| `2026-06-16 09:01:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cfe8417db138

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-16 09:02 |
| **Last Seen** | 2026-06-16 09:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-16 09:02:56` | `cowrie.session.connect` |
| `2026-06-16 09:02:56` | `cowrie.client.version` |
| `2026-06-16 09:02:56` | `cowrie.client.kex` |
| `2026-06-16 09:02:56` | `cowrie.login.success` |
| `2026-06-16 09:02:57` | `cowrie.session.params` |
| `2026-06-16 09:02:57` | `cowrie.command.input` |
| `2026-06-16 09:02:57` | `cowrie.log.closed` |
| `2026-06-16 09:02:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e35e1a14fbb2

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-16 09:05 |
| **Last Seen** | 2026-06-16 09:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-16 09:05:12` | `cowrie.session.connect` |
| `2026-06-16 09:05:12` | `cowrie.client.version` |
| `2026-06-16 09:05:12` | `cowrie.client.kex` |
| `2026-06-16 09:05:13` | `cowrie.login.success` |
| `2026-06-16 09:05:14` | `cowrie.session.params` |
| `2026-06-16 09:05:14` | `cowrie.command.input` |
| `2026-06-16 09:05:14` | `cowrie.log.closed` |
| `2026-06-16 09:05:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-afa87993e6dc

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-16 09:07 |
| **Last Seen** | 2026-06-16 09:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-16 09:07:28` | `cowrie.session.connect` |
| `2026-06-16 09:07:28` | `cowrie.client.version` |
| `2026-06-16 09:07:28` | `cowrie.client.kex` |
| `2026-06-16 09:07:28` | `cowrie.login.success` |
| `2026-06-16 09:07:29` | `cowrie.session.params` |
| `2026-06-16 09:07:29` | `cowrie.command.input` |
| `2026-06-16 09:07:29` | `cowrie.log.closed` |
| `2026-06-16 09:07:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-144932a06707

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-16 09:09 |
| **Last Seen** | 2026-06-16 09:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-16 09:09:37` | `cowrie.session.connect` |
| `2026-06-16 09:09:37` | `cowrie.client.version` |
| `2026-06-16 09:09:38` | `cowrie.client.kex` |
| `2026-06-16 09:09:38` | `cowrie.login.success` |
| `2026-06-16 09:09:38` | `cowrie.session.params` |
| `2026-06-16 09:09:38` | `cowrie.command.input` |
| `2026-06-16 09:09:39` | `cowrie.log.closed` |
| `2026-06-16 09:09:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-267adc6a74ad

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-16 09:11 |
| **Last Seen** | 2026-06-16 09:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-16 09:11:52` | `cowrie.session.connect` |
| `2026-06-16 09:11:52` | `cowrie.client.version` |
| `2026-06-16 09:11:53` | `cowrie.client.kex` |
| `2026-06-16 09:11:53` | `cowrie.login.success` |
| `2026-06-16 09:11:54` | `cowrie.session.params` |
| `2026-06-16 09:11:54` | `cowrie.command.input` |
| `2026-06-16 09:11:54` | `cowrie.log.closed` |
| `2026-06-16 09:11:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f1a99b617a16

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-16 09:14 |
| **Last Seen** | 2026-06-16 09:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-16 09:14:06` | `cowrie.session.connect` |
| `2026-06-16 09:14:06` | `cowrie.client.version` |
| `2026-06-16 09:14:06` | `cowrie.client.kex` |
| `2026-06-16 09:14:07` | `cowrie.login.success` |
| `2026-06-16 09:14:07` | `cowrie.session.params` |
| `2026-06-16 09:14:07` | `cowrie.command.input` |
| `2026-06-16 09:14:07` | `cowrie.log.closed` |
| `2026-06-16 09:14:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c03d9dc064b0

| Field | Detail |
|---|---|
| **Source IP** | `168.110.107[.]79` |
| **First Seen** | 2026-06-16 09:46 |
| **Last Seen** | 2026-06-16 09:48 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-16 09:46:57` | `cowrie.session.connect` |
| `2026-06-16 09:46:58` | `cowrie.telnet.option` |
| `2026-06-16 09:46:59` | `cowrie.telnet.option` |
| `2026-06-16 09:48:02` | `cowrie.login.success` |
| `2026-06-16 09:48:03` | `cowrie.session.params` |

**Recommended Actions:**
- [ ] Submit `168.110.107[.]79` to AbuseIPDB if not already reported
- [ ] Block `168.110.107[.]79` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b1c2e1ba0cfe

| Field | Detail |
|---|---|
| **Source IP** | `185.93.89[.]95` |
| **First Seen** | 2026-06-16 09:48 |
| **Last Seen** | 2026-06-16 09:48 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a;w` |
| **TTPs (MITRE)** | T1057 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-16 09:48:07` | `cowrie.session.connect` |
| `2026-06-16 09:48:07` | `cowrie.client.version` |
| `2026-06-16 09:48:07` | `cowrie.client.kex` |
| `2026-06-16 09:48:08` | `cowrie.login.success` |
| `2026-06-16 09:48:09` | `cowrie.session.params` |
| `2026-06-16 09:48:09` | `cowrie.command.input` |
| `2026-06-16 09:48:09` | `cowrie.log.closed` |
| `2026-06-16 09:48:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.93.89[.]95` to AbuseIPDB if not already reported
- [ ] Block `185.93.89[.]95` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-644f3aab2825

| Field | Detail |
|---|---|
| **Source IP** | `172.236.228[.]224` |
| **First Seen** | 2026-06-16 10:18 |
| **Last Seen** | 2026-06-16 10:18 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0[.]0 Safari/537.36, Accept: */*, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-16 10:18:21` | `cowrie.session.connect` |
| `2026-06-16 10:18:21` | `cowrie.login.success` |
| `2026-06-16 10:18:22` | `cowrie.session.params` |
| `2026-06-16 10:18:22` | `cowrie.command.input` |
| `2026-06-16 10:18:22` | `cowrie.command.input` |
| `2026-06-16 10:18:22` | `cowrie.command.failed` |
| `2026-06-16 10:18:22` | `cowrie.command.input` |
| `2026-06-16 10:18:22` | `cowrie.command.failed` |
| `2026-06-16 10:18:22` | `cowrie.command.input` |
| `2026-06-16 10:18:22` | `cowrie.log.closed` |
| `2026-06-16 10:18:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.236.228[.]224` to AbuseIPDB if not already reported
- [ ] Block `172.236.228[.]224` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8a1b3faf877d

| Field | Detail |
|---|---|
| **Source IP** | `185.93.89[.]95` |
| **First Seen** | 2026-06-16 10:21 |
| **Last Seen** | 2026-06-16 10:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a;w` |
| **TTPs (MITRE)** | T1057 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-16 10:21:58` | `cowrie.session.connect` |
| `2026-06-16 10:21:58` | `cowrie.client.version` |
| `2026-06-16 10:21:58` | `cowrie.client.kex` |
| `2026-06-16 10:21:59` | `cowrie.login.success` |
| `2026-06-16 10:22:00` | `cowrie.session.params` |
| `2026-06-16 10:22:00` | `cowrie.command.input` |
| `2026-06-16 10:22:00` | `cowrie.log.closed` |
| `2026-06-16 10:22:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.93.89[.]95` to AbuseIPDB if not already reported
- [ ] Block `185.93.89[.]95` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dda57b3ea2c4

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-06-16 10:25 |
| **Last Seen** | 2026-06-16 10:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-16 10:25:29` | `cowrie.session.connect` |
| `2026-06-16 10:25:29` | `cowrie.client.version` |
| `2026-06-16 10:25:29` | `cowrie.client.kex` |
| `2026-06-16 10:25:30` | `cowrie.login.success` |
| `2026-06-16 10:25:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b03a8de8e185

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-06-16 10:25 |
| **Last Seen** | 2026-06-16 10:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-16 10:25:29` | `cowrie.session.connect` |
| `2026-06-16 10:25:29` | `cowrie.client.version` |
| `2026-06-16 10:25:29` | `cowrie.client.kex` |
| `2026-06-16 10:25:30` | `cowrie.login.success` |
| `2026-06-16 10:25:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-189492cefbd7

| Field | Detail |
|---|---|
| **Source IP** | `130.49.189[.]41` |
| **First Seen** | 2026-06-16 10:41 |
| **Last Seen** | 2026-06-16 10:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-16 10:41:50` | `cowrie.session.connect` |
| `2026-06-16 10:41:50` | `cowrie.client.version` |
| `2026-06-16 10:41:50` | `cowrie.client.kex` |
| `2026-06-16 10:41:50` | `cowrie.login.success` |
| `2026-06-16 10:41:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.49.189[.]41` to AbuseIPDB if not already reported
- [ ] Block `130.49.189[.]41` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-669256c75567

| Field | Detail |
|---|---|
| **Source IP** | `130.12.180[.]51` |
| **First Seen** | 2026-06-16 10:41 |
| **Last Seen** | 2026-06-16 10:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-16 10:41:51` | `cowrie.session.connect` |
| `2026-06-16 10:41:51` | `cowrie.client.version` |
| `2026-06-16 10:41:51` | `cowrie.client.kex` |
| `2026-06-16 10:41:51` | `cowrie.login.success` |
| `2026-06-16 10:41:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.180[.]51` to AbuseIPDB if not already reported
- [ ] Block `130.12.180[.]51` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `183.91.11[.]226` | **8** | 2026-06-16 08:58 | 2026-06-16 10:33 | 5m | 0 | `T1592` | 🟢 LOW |
| `188.166.223[.]22` | **7** | 2026-06-16 08:58 | 2026-06-16 10:21 | 6m | 0 | `T1592` | 🟢 LOW |
| `51.158.205[.]203` | **6** | 2026-06-16 10:37 | 2026-06-16 10:41 | 0m | 0 | `T1592` | 🟢 LOW |
| `176.65.139[.]22` | **5** | 2026-06-16 09:20 | 2026-06-16 09:21 | 2m | 0 | `T1592` | 🟢 LOW |
| `111.26.6[.]111` | **2** | 2026-06-16 10:46 | 2026-06-16 10:48 | 2m | 0 | `T1592` | 🟢 LOW |
| `114.66.38[.]47` | **2** | 2026-06-16 10:30 | 2026-06-16 10:32 | 2m | 0 | `T1592` | 🟢 LOW |
| `159.223.31[.]72` | **2** | 2026-06-16 09:36 | 2026-06-16 09:36 | 0m | 0 | `T1592` | 🟢 LOW |
| `103.203.57[.]2` | 1 | 2026-06-16 09:36 | 2026-06-16 09:36 | 10s | 0 | `T1592` | 🟢 LOW |
| `117.252.242[.]249` | 1 | 2026-06-16 10:53 | 2026-06-16 10:53 | 13s | 0 | `T1592` | 🟢 LOW |
| `159.223.20[.]8` | 1 | 2026-06-16 09:36 | 2026-06-16 09:36 | 20s | 0 | `T1592` | 🟢 LOW |
| `172.236.228[.]224` | 1 | 2026-06-16 10:18 | 2026-06-16 10:18 | 0s | 0 | `T1592` | 🟢 LOW |
| `185.16.39[.]100` | 1 | 2026-06-16 10:44 | 2026-06-16 10:44 | 0s | 0 | `T1592` | 🟢 LOW |
| `193.124.20[.]246` | 1 | 2026-06-16 09:18 | 2026-06-16 09:18 | 0s | 0 | `T1592` | 🟢 LOW |
| `42.100.24[.]36` | 1 | 2026-06-16 10:25 | 2026-06-16 10:25 | 13s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]152` | 1 | 2026-06-16 10:03 | 2026-06-16 10:03 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.33.12[.]214` | 1 | 2026-06-16 09:34 | 2026-06-16 09:34 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.207[.]111` | 1 | 2026-06-16 09:34 | 2026-06-16 09:35 | 13s | 0 | `T1592` | 🟢 LOW |
| `49.88.156[.]34` | 1 | 2026-06-16 10:33 | 2026-06-16 10:35 | 120s | 0 | `T1592` | 🟢 LOW |
| `50.116.26[.]161` | 1 | 2026-06-16 10:40 | 2026-06-16 10:40 | 0s | 0 | `T1592` | 🟢 LOW |
| `64.89.160[.]135` | 1 | 2026-06-16 10:07 | 2026-06-16 10:07 | 0s | 0 | `T1592` | 🟢 LOW |
| `85.217.149[.]43` | 1 | 2026-06-16 10:41 | 2026-06-16 10:41 | 0s | 0 | `T1592` | 🟢 LOW |
| `85.217.149[.]59` | 1 | 2026-06-16 10:26 | 2026-06-16 10:26 | 0s | 0 | `T1592` | 🟢 LOW |
| `89.21.67[.]168` | 1 | 2026-06-16 09:18 | 2026-06-16 09:18 | 10s | 0 | `T1592` | 🟢 LOW |
| `95.77.9[.]9` | 1 | 2026-06-16 10:12 | 2026-06-16 10:12 | 12s | 0 | `T1592` | 🟢 LOW |

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
| `130.12.180[.]51` | DE | Virtualine Technologies | **100** ⚠️ | 50 |
| `185.16.39[.]100` | PL | MEVSPACE sp. z o.o. | **100** ⚠️ | 17 |
| `185.93.89[.]95` | NL | Limited Network LTD | **100** ⚠️ | 19 |
| `188.166.223[.]22` | SG | DigitalOcean, LLC | **100** ⚠️ | 3 |
| `176.65.139[.]22` | NL | Storm Industries LLC | **100** ⚠️ | 8 |
| `64.110.90[.]250` | KR | Oracle Corporation | **100** ⚠️ | 4 |
| `172.236.228[.]224` | US | Linode | **100** ⚠️ | 50 |
| `51.158.205[.]203` | NL | Scaleway - Amsterdam, Netherlands | **100** ⚠️ | 50 |
| `144.22.238[.]238` | BR | Oracle Corporation | **100** ⚠️ | 3 |
| `114.66.38[.]47` | CN | Beijing Yunlin Network Technology Co.,Ltd | **100** ⚠️ | 8 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 46 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 23 |
| [T1057](https://attack.mitre.org/techniques/T1057) | 2 |

---

## 🔕 False Positive Summary (28 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 18 |
| AbuseIPDB score 15 below threshold 25 | 1 |
| AbuseIPDB score 24 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 8 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 98 cases |
| Tool 34  | Credential Extractor        | ✅ 23 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 13 fingerprints |
| Tool 36  | Command Clustering          | ✅ 4 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 40 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 28 filtered (28.6%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 26 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 17 files |
| Tool 33  | YARA Classifier             | ✅ 13 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 21 priority case(s) shown individually · 24 recon entry/entries in table (7 group(s) consolidating 32 session(s)).

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
_Report time: 2026-06-16T11:19:56Z_

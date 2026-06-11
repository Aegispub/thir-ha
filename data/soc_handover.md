# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-06-11 |
| **Generated At** | 2026-06-11T10:43:55Z |
| **Shift Time** | 10:43 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **103** |
| Confirmed Threats | **88** |
| False Positives Filtered | **15** (14.6%) |
| Unique Attacker IPs | **45** |
| Countries of Origin | **15** |
| High Severity Cases | **32** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **71** |
| Malware Samples Analyzed | **0** HIGH · **20** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **33** |
| Unique Credential Pairs | **19** |
| Unique Usernames | **8** |
| Unique Passwords | **19** |
| Successful Auth Pairs | **27** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 22 |
| `admin` | 5 |
| `config` | 1 |
| `support` | 1 |
| `system` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `LeitboGi0ro` | 9 |
| `123@@@` | 6 |
| `smo@@kkklss` | 2 |
| `config` | 1 |
| `support` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `LeitboGi0ro` | 9 |
| `root` | `123@@@` | 6 |
| `root` | `smo@@kkklss` | 2 |
| `config` | `config` | 1 |
| `support` | `support` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `config` | `config` | `116.99.174.228` | 2026-06-11T04:59:16 |
| `support` | `support` | `116.99.174.228` | 2026-06-11T05:01:57 |
| `root` | `LeitboGi0ro` | `129.153.145.135` | 2026-06-11T05:04:56 |
| `root` | `123@@@` | `129.153.145.135` | 2026-06-11T05:04:56 |
| `root` | `@` | `116.99.174.228` | 2026-06-11T05:06:27 |
| `admin` | `admin@123` | `116.99.174.228` | 2026-06-11T05:15:26 |
| `root` | `root123` | `116.99.174.228` | 2026-06-11T05:19:30 |
| `system` | `OkwKcECs8qJP2Z` | `116.99.174.228` | 2026-06-11T05:23:52 |
| `alani` | `alani` | `213.209.159.56` | 2026-06-11T05:28:41 |
| `root` | `LeitboGi0ro` | `40.233.83.131` | 2026-06-11T05:37:07 |
| `root` | `123@@@` | `40.233.83.131` | 2026-06-11T05:37:08 |
| `admin` | `dario` | `2.57.121.112` | 2026-06-11T05:44:41 |
| `dixie` | `dixie` | `213.209.159.56` | 2026-06-11T06:48:15 |
| `root` | `password` | `188.64.139.147` | 2026-06-11T07:01:14 |
| `root` | `LeitboGi0ro` | `188.64.139.147` | 2026-06-11T07:01:17 |
| `root` | `MoeClub.org` | `188.64.139.147` | 2026-06-11T07:01:21 |
| `admin` | `damascus` | `2.57.121.112` | 2026-06-11T07:04:15 |
| `root` | `LeitboGi0ro` | `144.22.238.238` | 2026-06-11T07:06:47 |
| `root` | `123@@@` | `144.22.238.238` | 2026-06-11T07:06:47 |
| `root` | `smo@@kkklss` | `144.22.238.238` | 2026-06-11T07:06:56 |
| `admin` | `admin` | `34.38.219.198` | 2026-06-11T07:28:25 |
| `emelia` | `emelia` | `213.209.159.56` | 2026-06-11T08:06:56 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-06-11T08:09:27 |
| `root` | `123@@@` | `64.110.90.250` | 2026-06-11T08:09:27 |
| `root` | `LeitboGi0ro` | `138.2.98.41` | 2026-06-11T08:23:07 |
| `root` | `123@@@` | `138.2.98.41` | 2026-06-11T08:23:07 |
| `admin` | `curious1` | `2.57.121.112` | 2026-06-11T08:24:58 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **103** |
| Sessions with Fingerprint | **15** |
| Unique HASSH Fingerprints | **15** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Paramiko (Python) | 16 |
| Go SSH scanner | 13 |
| AsyncSSH (Python) | 7 |
| PuTTY | 7 |
| Nmap scanner | 7 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `a2de0f306611...` | Mirai/variant | 12 | 4 |
| `fda360b1b4f4...` | Mirai/variant | 7 | 1 |
| `57446c12547a...` | Mirai/variant | 6 | 2 |
| `e788c657d1a2...` | Mirai/variant | 6 | 1 |
| `6372ee695756...` | Modern SSH client | 4 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `a2de0f306611...` | Paramiko (Python) | 12 | 4 | Mirai/variant |
| `fda360b1b4f4...` | AsyncSSH (Python) | 7 | 1 | Mirai/variant |
| `95420f9d932d...` | Go SSH scanner | 7 | 5 | — |
| `57446c12547a...` | PuTTY | 6 | 2 | Mirai/variant |
| `e788c657d1a2...` | Nmap scanner | 6 | 1 | Mirai/variant |
| `6372ee695756...` | Paramiko (Python) | 4 | 1 | Modern SSH client |
| `16443846184e...` | Go SSH scanner | 3 | 1 | Generic scanner |
| `dd9bcf093c35...` | Unknown | 2 | 2 | Mirai/variant |

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **45** |
| Unique ASNs | **25** |
| High-Risk ASNs | **21** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS63949` | Akamai Connected Cloud | 5 | HIGH |
| `AS31898` | Oracle Corporation | 5 | HIGH |
| `AS396982` | Google LLC | 4 | HIGH |
| `AS48090` | TECHOFF SRV LIMITED | 3 | HIGH |
| `AS25369` | Hydra Communications Ltd | 3 | HIGH |
| `AS14061` | DigitalOcean, LLC | 2 | HIGH |
| `AS6939` | Hurricane Electric LLC | 2 | HIGH |
| `AS398324` | Censys, Inc. | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (32)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-be12e0a2fc71

| Field | Detail |
|---|---|
| **Source IP** | `116.99.174[.]228` |
| **First Seen** | 2026-06-11 04:59 |
| **Last Seen** | 2026-06-11 05:00 |
| **Session Duration** | 91s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 04:59:01` | `cowrie.session.connect` |
| `2026-06-11 04:59:09` | `cowrie.client.version` |
| `2026-06-11 04:59:14` | `cowrie.client.kex` |
| `2026-06-11 04:59:16` | `cowrie.login.success` |
| `2026-06-11 05:00:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.99.174[.]228` to AbuseIPDB if not already reported
- [ ] Block `116.99.174[.]228` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c295b9e91b1d

| Field | Detail |
|---|---|
| **Source IP** | `116.99.174[.]228` |
| **First Seen** | 2026-06-11 05:01 |
| **Last Seen** | 2026-06-11 05:02 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 05:01:49` | `cowrie.session.connect` |
| `2026-06-11 05:01:49` | `cowrie.client.version` |
| `2026-06-11 05:01:50` | `cowrie.client.kex` |
| `2026-06-11 05:01:57` | `cowrie.login.success` |
| `2026-06-11 05:01:58` | `cowrie.direct-tcpip.request` |
| `2026-06-11 05:02:04` | `cowrie.direct-tcpip.ja4h` |
| `2026-06-11 05:02:04` | `cowrie.direct-tcpip.data` |
| `2026-06-11 05:02:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.99.174[.]228` to AbuseIPDB if not already reported
- [ ] Block `116.99.174[.]228` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-942900b2f893

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-11 05:04 |
| **Last Seen** | 2026-06-11 05:04 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 05:04:56` | `cowrie.session.connect` |
| `2026-06-11 05:04:56` | `cowrie.client.version` |
| `2026-06-11 05:04:56` | `cowrie.client.kex` |
| `2026-06-11 05:04:56` | `cowrie.login.success` |
| `2026-06-11 05:04:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5a3cc50630b0

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-11 05:04 |
| **Last Seen** | 2026-06-11 05:04 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 05:04:56` | `cowrie.session.connect` |
| `2026-06-11 05:04:56` | `cowrie.client.version` |
| `2026-06-11 05:04:56` | `cowrie.client.kex` |
| `2026-06-11 05:04:56` | `cowrie.login.success` |
| `2026-06-11 05:04:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-12d34df33330

| Field | Detail |
|---|---|
| **Source IP** | `116.99.174[.]228` |
| **First Seen** | 2026-06-11 05:06 |
| **Last Seen** | 2026-06-11 05:06 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 05:06:25` | `cowrie.session.connect` |
| `2026-06-11 05:06:25` | `cowrie.client.version` |
| `2026-06-11 05:06:25` | `cowrie.client.kex` |
| `2026-06-11 05:06:27` | `cowrie.login.success` |
| `2026-06-11 05:06:27` | `cowrie.direct-tcpip.request` |
| `2026-06-11 05:06:27` | `cowrie.direct-tcpip.ja4h` |
| `2026-06-11 05:06:27` | `cowrie.direct-tcpip.data` |
| `2026-06-11 05:06:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.99.174[.]228` to AbuseIPDB if not already reported
- [ ] Block `116.99.174[.]228` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b243de2a1c89

| Field | Detail |
|---|---|
| **Source IP** | `116.99.174[.]228` |
| **First Seen** | 2026-06-11 05:15 |
| **Last Seen** | 2026-06-11 05:15 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 05:15:24` | `cowrie.session.connect` |
| `2026-06-11 05:15:24` | `cowrie.client.version` |
| `2026-06-11 05:15:25` | `cowrie.client.kex` |
| `2026-06-11 05:15:26` | `cowrie.login.success` |
| `2026-06-11 05:15:26` | `cowrie.direct-tcpip.request` |
| `2026-06-11 05:15:27` | `cowrie.direct-tcpip.ja4h` |
| `2026-06-11 05:15:27` | `cowrie.direct-tcpip.data` |
| `2026-06-11 05:15:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.99.174[.]228` to AbuseIPDB if not already reported
- [ ] Block `116.99.174[.]228` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c8b7cc6d57a3

| Field | Detail |
|---|---|
| **Source IP** | `116.99.174[.]228` |
| **First Seen** | 2026-06-11 05:19 |
| **Last Seen** | 2026-06-11 05:19 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 05:19:29` | `cowrie.session.connect` |
| `2026-06-11 05:19:29` | `cowrie.client.version` |
| `2026-06-11 05:19:29` | `cowrie.client.kex` |
| `2026-06-11 05:19:30` | `cowrie.login.success` |
| `2026-06-11 05:19:31` | `cowrie.direct-tcpip.request` |
| `2026-06-11 05:19:31` | `cowrie.direct-tcpip.ja4h` |
| `2026-06-11 05:19:31` | `cowrie.direct-tcpip.data` |
| `2026-06-11 05:19:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.99.174[.]228` to AbuseIPDB if not already reported
- [ ] Block `116.99.174[.]228` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c404266affbb

| Field | Detail |
|---|---|
| **Source IP** | `116.99.174[.]228` |
| **First Seen** | 2026-06-11 05:23 |
| **Last Seen** | 2026-06-11 05:23 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 05:23:50` | `cowrie.session.connect` |
| `2026-06-11 05:23:50` | `cowrie.client.version` |
| `2026-06-11 05:23:50` | `cowrie.client.kex` |
| `2026-06-11 05:23:52` | `cowrie.login.success` |
| `2026-06-11 05:23:52` | `cowrie.direct-tcpip.request` |
| `2026-06-11 05:23:53` | `cowrie.direct-tcpip.ja4h` |
| `2026-06-11 05:23:53` | `cowrie.direct-tcpip.data` |
| `2026-06-11 05:23:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.99.174[.]228` to AbuseIPDB if not already reported
- [ ] Block `116.99.174[.]228` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aad7429ebeda

| Field | Detail |
|---|---|
| **Source IP** | `213.209.159[.]56` |
| **First Seen** | 2026-06-11 05:28 |
| **Last Seen** | 2026-06-11 05:28 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 05:28:41` | `cowrie.session.connect` |
| `2026-06-11 05:28:41` | `cowrie.client.version` |
| `2026-06-11 05:28:41` | `cowrie.client.kex` |
| `2026-06-11 05:28:41` | `cowrie.login.success` |
| `2026-06-11 05:28:41` | `cowrie.direct-tcpip.request` |
| `2026-06-11 05:28:41` | `cowrie.direct-tcpip.data` |
| `2026-06-11 05:28:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.209.159[.]56` to AbuseIPDB if not already reported
- [ ] Block `213.209.159[.]56` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7fca00572adc

| Field | Detail |
|---|---|
| **Source IP** | `40.233.83[.]131` |
| **First Seen** | 2026-06-11 05:37 |
| **Last Seen** | 2026-06-11 05:37 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 05:37:07` | `cowrie.session.connect` |
| `2026-06-11 05:37:07` | `cowrie.client.version` |
| `2026-06-11 05:37:07` | `cowrie.client.kex` |
| `2026-06-11 05:37:07` | `cowrie.login.success` |
| `2026-06-11 05:37:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.233.83[.]131` to AbuseIPDB if not already reported
- [ ] Block `40.233.83[.]131` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-21b638dca763

| Field | Detail |
|---|---|
| **Source IP** | `40.233.83[.]131` |
| **First Seen** | 2026-06-11 05:37 |
| **Last Seen** | 2026-06-11 05:37 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 05:37:08` | `cowrie.session.connect` |
| `2026-06-11 05:37:08` | `cowrie.client.version` |
| `2026-06-11 05:37:08` | `cowrie.client.kex` |
| `2026-06-11 05:37:08` | `cowrie.login.success` |
| `2026-06-11 05:37:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.233.83[.]131` to AbuseIPDB if not already reported
- [ ] Block `40.233.83[.]131` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-74d1ddf9fe95

| Field | Detail |
|---|---|
| **Source IP** | `40.233.83[.]131` |
| **First Seen** | 2026-06-11 05:37 |
| **Last Seen** | 2026-06-11 05:39 |
| **Session Duration** | 124s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 05:37:26` | `cowrie.session.connect` |
| `2026-06-11 05:37:26` | `cowrie.client.version` |
| `2026-06-11 05:37:26` | `cowrie.client.kex` |
| `2026-06-11 05:37:26` | `cowrie.login.success` |
| `2026-06-11 05:37:27` | `cowrie.session.file_upload` |
| `2026-06-11 05:37:27` | `cowrie.session.params` |
| `2026-06-11 05:37:27` | `cowrie.command.input` |
| `2026-06-11 05:37:27` | `cowrie.command.input` |
| `2026-06-11 05:37:27` | `cowrie.command.input` |
| `2026-06-11 05:37:27` | `cowrie.command.failed` |
| `2026-06-11 05:37:28` | `cowrie.log.closed` |
| `2026-06-11 05:37:28` | `cowrie.session.params` |
| `2026-06-11 05:37:28` | `cowrie.command.input` |
| `2026-06-11 05:37:28` | `cowrie.log.closed` |
| `2026-06-11 05:37:29` | `cowrie.session.params` |
| `2026-06-11 05:37:29` | `cowrie.command.input` |
| `2026-06-11 05:37:29` | `cowrie.log.closed` |
| `2026-06-11 05:37:30` | `cowrie.session.params` |
| `2026-06-11 05:37:30` | `cowrie.command.input` |
| `2026-06-11 05:37:30` | `cowrie.command.failed` |
| `2026-06-11 05:37:30` | `cowrie.command.failed` |
| `2026-06-11 05:38:30` | `cowrie.session.params` |
| `2026-06-11 05:38:30` | `cowrie.command.input` |
| `2026-06-11 05:39:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.233.83[.]131` to AbuseIPDB if not already reported
- [ ] Block `40.233.83[.]131` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-feeee729b16e

| Field | Detail |
|---|---|
| **Source IP** | `40.233.83[.]131` |
| **First Seen** | 2026-06-11 05:39 |
| **Last Seen** | 2026-06-11 05:41 |
| **Session Duration** | 125s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 05:39:46` | `cowrie.session.connect` |
| `2026-06-11 05:39:46` | `cowrie.client.version` |
| `2026-06-11 05:39:46` | `cowrie.client.kex` |
| `2026-06-11 05:39:46` | `cowrie.login.success` |
| `2026-06-11 05:39:47` | `cowrie.session.file_upload` |
| `2026-06-11 05:39:47` | `cowrie.session.params` |
| `2026-06-11 05:39:47` | `cowrie.command.input` |
| `2026-06-11 05:39:47` | `cowrie.command.input` |
| `2026-06-11 05:39:47` | `cowrie.command.input` |
| `2026-06-11 05:39:47` | `cowrie.command.failed` |
| `2026-06-11 05:39:47` | `cowrie.log.closed` |
| `2026-06-11 05:39:48` | `cowrie.session.params` |
| `2026-06-11 05:39:48` | `cowrie.command.input` |
| `2026-06-11 05:39:48` | `cowrie.log.closed` |
| `2026-06-11 05:39:49` | `cowrie.session.params` |
| `2026-06-11 05:39:49` | `cowrie.command.input` |
| `2026-06-11 05:39:49` | `cowrie.log.closed` |
| `2026-06-11 05:39:49` | `cowrie.session.params` |
| `2026-06-11 05:39:49` | `cowrie.command.input` |
| `2026-06-11 05:39:49` | `cowrie.command.failed` |
| `2026-06-11 05:39:49` | `cowrie.command.failed` |
| `2026-06-11 05:40:50` | `cowrie.session.params` |
| `2026-06-11 05:40:50` | `cowrie.command.input` |
| `2026-06-11 05:41:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.233.83[.]131` to AbuseIPDB if not already reported
- [ ] Block `40.233.83[.]131` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d9fc0e734fb9

| Field | Detail |
|---|---|
| **Source IP** | `2.57.121[.]112` |
| **First Seen** | 2026-06-11 05:44 |
| **Last Seen** | 2026-06-11 05:44 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 05:44:40` | `cowrie.session.connect` |
| `2026-06-11 05:44:40` | `cowrie.client.version` |
| `2026-06-11 05:44:40` | `cowrie.client.kex` |
| `2026-06-11 05:44:41` | `cowrie.login.success` |
| `2026-06-11 05:44:41` | `cowrie.direct-tcpip.request` |
| `2026-06-11 05:44:41` | `cowrie.direct-tcpip.data` |
| `2026-06-11 05:44:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.121[.]112` to AbuseIPDB if not already reported
- [ ] Block `2.57.121[.]112` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fb670686a831

| Field | Detail |
|---|---|
| **Source IP** | `213.209.159[.]56` |
| **First Seen** | 2026-06-11 06:48 |
| **Last Seen** | 2026-06-11 06:48 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 06:48:14` | `cowrie.session.connect` |
| `2026-06-11 06:48:14` | `cowrie.client.version` |
| `2026-06-11 06:48:14` | `cowrie.client.kex` |
| `2026-06-11 06:48:15` | `cowrie.login.success` |
| `2026-06-11 06:48:15` | `cowrie.direct-tcpip.request` |
| `2026-06-11 06:48:15` | `cowrie.direct-tcpip.data` |
| `2026-06-11 06:48:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.209.159[.]56` to AbuseIPDB if not already reported
- [ ] Block `213.209.159[.]56` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-110640d11692

| Field | Detail |
|---|---|
| **Source IP** | `188.64.139[.]147` |
| **First Seen** | 2026-06-11 07:01 |
| **Last Seen** | 2026-06-11 07:01 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -m 2>/dev/null | tr -d '\n\r' || echo 'unknown'; echo '---SEP---'; cat /etc/os-release 2>/dev/null | grep '^NAME=' | cut -d'=' -f2 | tr -d '"' | tr -d '\n\r' || echo 'Linux'; echo '---SEP---'; hostname 2>/dev/null | tr -d '\n\r' || echo 'unknown'; echo '---SEP---'; curl -s --connect-timeout 2 ipinfo.io/country 2>/dev/null | tr -d '\n\r' || echo 'N/A'; echo '---SEP---'; nproc 2>/dev/null | tr -d '\n\r' || echo '1'; echo '---SEP---'; free -h 2>/dev/null | awk '/^Mem:/ {print $2}' | tr -d '\n\r' || echo ` |
| **TTPs (MITRE)** | T1078 · T1083 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 07:01:13` | `cowrie.session.connect` |
| `2026-06-11 07:01:13` | `cowrie.client.version` |
| `2026-06-11 07:01:13` | `cowrie.client.kex` |
| `2026-06-11 07:01:14` | `cowrie.login.success` |
| `2026-06-11 07:01:16` | `cowrie.session.params` |
| `2026-06-11 07:01:16` | `cowrie.command.input` |
| `2026-06-11 07:01:16` | `cowrie.log.closed` |
| `2026-06-11 07:01:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `188.64.139[.]147` to AbuseIPDB if not already reported
- [ ] Block `188.64.139[.]147` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-235df465905a

| Field | Detail |
|---|---|
| **Source IP** | `188.64.139[.]147` |
| **First Seen** | 2026-06-11 07:01 |
| **Last Seen** | 2026-06-11 07:01 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -m 2>/dev/null | tr -d '\n\r' || echo 'unknown'; echo '---SEP---'; cat /etc/os-release 2>/dev/null | grep '^NAME=' | cut -d'=' -f2 | tr -d '"' | tr -d '\n\r' || echo 'Linux'; echo '---SEP---'; hostname 2>/dev/null | tr -d '\n\r' || echo 'unknown'; echo '---SEP---'; curl -s --connect-timeout 2 ipinfo.io/country 2>/dev/null | tr -d '\n\r' || echo 'N/A'; echo '---SEP---'; nproc 2>/dev/null | tr -d '\n\r' || echo '1'; echo '---SEP---'; free -h 2>/dev/null | awk '/^Mem:/ {print $2}' | tr -d '\n\r' || echo ` |
| **TTPs (MITRE)** | T1078 · T1083 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 07:01:16` | `cowrie.session.connect` |
| `2026-06-11 07:01:17` | `cowrie.client.version` |
| `2026-06-11 07:01:17` | `cowrie.client.kex` |
| `2026-06-11 07:01:17` | `cowrie.login.success` |
| `2026-06-11 07:01:19` | `cowrie.session.params` |
| `2026-06-11 07:01:19` | `cowrie.command.input` |
| `2026-06-11 07:01:20` | `cowrie.log.closed` |
| `2026-06-11 07:01:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `188.64.139[.]147` to AbuseIPDB if not already reported
- [ ] Block `188.64.139[.]147` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5c52b7bc665e

| Field | Detail |
|---|---|
| **Source IP** | `188.64.139[.]147` |
| **First Seen** | 2026-06-11 07:01 |
| **Last Seen** | 2026-06-11 07:01 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -m 2>/dev/null | tr -d '\n\r' || echo 'unknown'; echo '---SEP---'; cat /etc/os-release 2>/dev/null | grep '^NAME=' | cut -d'=' -f2 | tr -d '"' | tr -d '\n\r' || echo 'Linux'; echo '---SEP---'; hostname 2>/dev/null | tr -d '\n\r' || echo 'unknown'; echo '---SEP---'; curl -s --connect-timeout 2 ipinfo.io/country 2>/dev/null | tr -d '\n\r' || echo 'N/A'; echo '---SEP---'; nproc 2>/dev/null | tr -d '\n\r' || echo '1'; echo '---SEP---'; free -h 2>/dev/null | awk '/^Mem:/ {print $2}' | tr -d '\n\r' || echo ` |
| **TTPs (MITRE)** | T1078 · T1083 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 07:01:20` | `cowrie.session.connect` |
| `2026-06-11 07:01:20` | `cowrie.client.version` |
| `2026-06-11 07:01:20` | `cowrie.client.kex` |
| `2026-06-11 07:01:21` | `cowrie.login.success` |
| `2026-06-11 07:01:22` | `cowrie.session.params` |
| `2026-06-11 07:01:22` | `cowrie.command.input` |
| `2026-06-11 07:01:22` | `cowrie.log.closed` |
| `2026-06-11 07:01:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `188.64.139[.]147` to AbuseIPDB if not already reported
- [ ] Block `188.64.139[.]147` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-128c55da31f1

| Field | Detail |
|---|---|
| **Source IP** | `2.57.121[.]112` |
| **First Seen** | 2026-06-11 07:04 |
| **Last Seen** | 2026-06-11 07:04 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 07:04:15` | `cowrie.session.connect` |
| `2026-06-11 07:04:15` | `cowrie.client.version` |
| `2026-06-11 07:04:15` | `cowrie.client.kex` |
| `2026-06-11 07:04:15` | `cowrie.login.success` |
| `2026-06-11 07:04:15` | `cowrie.direct-tcpip.request` |
| `2026-06-11 07:04:15` | `cowrie.direct-tcpip.data` |
| `2026-06-11 07:04:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.121[.]112` to AbuseIPDB if not already reported
- [ ] Block `2.57.121[.]112` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b2c914637542

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-06-11 07:06 |
| **Last Seen** | 2026-06-11 07:06 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 07:06:46` | `cowrie.session.connect` |
| `2026-06-11 07:06:46` | `cowrie.client.version` |
| `2026-06-11 07:06:47` | `cowrie.client.kex` |
| `2026-06-11 07:06:47` | `cowrie.login.success` |
| `2026-06-11 07:06:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-053837e714e1

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-06-11 07:06 |
| **Last Seen** | 2026-06-11 07:06 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 07:06:47` | `cowrie.session.connect` |
| `2026-06-11 07:06:47` | `cowrie.client.version` |
| `2026-06-11 07:06:47` | `cowrie.client.kex` |
| `2026-06-11 07:06:47` | `cowrie.login.success` |
| `2026-06-11 07:06:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f0fba5fea623

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-06-11 07:06 |
| **Last Seen** | 2026-06-11 07:06 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 07:06:56` | `cowrie.session.connect` |
| `2026-06-11 07:06:56` | `cowrie.client.version` |
| `2026-06-11 07:06:56` | `cowrie.client.kex` |
| `2026-06-11 07:06:56` | `cowrie.login.success` |
| `2026-06-11 07:06:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-df363f7beab9

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-06-11 07:06 |
| **Last Seen** | 2026-06-11 07:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 07:06:57` | `cowrie.session.connect` |
| `2026-06-11 07:06:57` | `cowrie.client.version` |
| `2026-06-11 07:06:57` | `cowrie.client.kex` |
| `2026-06-11 07:06:57` | `cowrie.login.success` |
| `2026-06-11 07:06:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-009dcfef1604

| Field | Detail |
|---|---|
| **Source IP** | `34.38.219[.]198` |
| **First Seen** | 2026-06-11 07:28 |
| **Last Seen** | 2026-06-11 07:28 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 07:28:23` | `cowrie.session.connect` |
| `2026-06-11 07:28:23` | `cowrie.client.version` |
| `2026-06-11 07:28:23` | `cowrie.client.kex` |
| `2026-06-11 07:28:25` | `cowrie.login.success` |
| `2026-06-11 07:28:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.38.219[.]198` to AbuseIPDB if not already reported
- [ ] Block `34.38.219[.]198` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-90ce1513e7ca

| Field | Detail |
|---|---|
| **Source IP** | `213.209.159[.]56` |
| **First Seen** | 2026-06-11 08:06 |
| **Last Seen** | 2026-06-11 08:07 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 08:06:56` | `cowrie.session.connect` |
| `2026-06-11 08:06:56` | `cowrie.client.version` |
| `2026-06-11 08:06:56` | `cowrie.client.kex` |
| `2026-06-11 08:06:56` | `cowrie.login.success` |
| `2026-06-11 08:06:57` | `cowrie.direct-tcpip.request` |
| `2026-06-11 08:06:57` | `cowrie.direct-tcpip.data` |
| `2026-06-11 08:07:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.209.159[.]56` to AbuseIPDB if not already reported
- [ ] Block `213.209.159[.]56` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-055bb3487139

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-06-11 08:09 |
| **Last Seen** | 2026-06-11 08:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 08:09:26` | `cowrie.session.connect` |
| `2026-06-11 08:09:26` | `cowrie.client.version` |
| `2026-06-11 08:09:26` | `cowrie.client.kex` |
| `2026-06-11 08:09:27` | `cowrie.login.success` |
| `2026-06-11 08:09:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-474e0d9db3a5

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-06-11 08:09 |
| **Last Seen** | 2026-06-11 08:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 08:09:26` | `cowrie.session.connect` |
| `2026-06-11 08:09:26` | `cowrie.client.version` |
| `2026-06-11 08:09:26` | `cowrie.client.kex` |
| `2026-06-11 08:09:27` | `cowrie.login.success` |
| `2026-06-11 08:09:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-097eed7ead7e

| Field | Detail |
|---|---|
| **Source IP** | `138.2.98[.]41` |
| **First Seen** | 2026-06-11 08:23 |
| **Last Seen** | 2026-06-11 08:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 08:23:05` | `cowrie.session.connect` |
| `2026-06-11 08:23:05` | `cowrie.client.version` |
| `2026-06-11 08:23:06` | `cowrie.client.kex` |
| `2026-06-11 08:23:07` | `cowrie.login.success` |
| `2026-06-11 08:23:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.2.98[.]41` to AbuseIPDB if not already reported
- [ ] Block `138.2.98[.]41` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3854e1aa1520

| Field | Detail |
|---|---|
| **Source IP** | `138.2.98[.]41` |
| **First Seen** | 2026-06-11 08:23 |
| **Last Seen** | 2026-06-11 08:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 08:23:05` | `cowrie.session.connect` |
| `2026-06-11 08:23:05` | `cowrie.client.version` |
| `2026-06-11 08:23:06` | `cowrie.client.kex` |
| `2026-06-11 08:23:07` | `cowrie.login.success` |
| `2026-06-11 08:23:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.2.98[.]41` to AbuseIPDB if not already reported
- [ ] Block `138.2.98[.]41` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f1dd60de424a

| Field | Detail |
|---|---|
| **Source IP** | `2.57.121[.]112` |
| **First Seen** | 2026-06-11 08:24 |
| **Last Seen** | 2026-06-11 08:25 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 08:24:58` | `cowrie.session.connect` |
| `2026-06-11 08:24:58` | `cowrie.client.version` |
| `2026-06-11 08:24:58` | `cowrie.client.kex` |
| `2026-06-11 08:24:58` | `cowrie.login.success` |
| `2026-06-11 08:24:59` | `cowrie.direct-tcpip.request` |
| `2026-06-11 08:24:59` | `cowrie.direct-tcpip.data` |
| `2026-06-11 08:25:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.121[.]112` to AbuseIPDB if not already reported
- [ ] Block `2.57.121[.]112` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-05c4c01e0f1a

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-11 08:34 |
| **Last Seen** | 2026-06-11 08:34 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 08:34:48` | `cowrie.session.connect` |
| `2026-06-11 08:34:48` | `cowrie.client.version` |
| `2026-06-11 08:34:48` | `cowrie.client.kex` |
| `2026-06-11 08:34:48` | `cowrie.login.success` |
| `2026-06-11 08:34:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5167ab07f537

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-11 08:34 |
| **Last Seen** | 2026-06-11 08:34 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 08:34:49` | `cowrie.session.connect` |
| `2026-06-11 08:34:49` | `cowrie.client.version` |
| `2026-06-11 08:34:49` | `cowrie.client.kex` |
| `2026-06-11 08:34:49` | `cowrie.login.success` |
| `2026-06-11 08:34:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `34.140.236[.]248` | **10** | 2026-06-11 07:29 | 2026-06-11 07:30 | 0m | 0 | `T1592` | 🟠 MEDIUM |
| `206.81.2[.]201` | **8** | 2026-06-11 06:08 | 2026-06-11 08:24 | 4m | 0 | `T1592` | 🟢 LOW |
| `154.16.146[.]65` | **4** | 2026-06-11 06:53 | 2026-06-11 06:54 | 1m | 0 | `T1592` | 🟢 LOW |
| `93.123.109[.]121` | **3** | 2026-06-11 08:41 | 2026-06-11 08:41 | 0m | 0 | `T1592` | 🟢 LOW |
| `192.119.13[.]58` | **2** | 2026-06-11 05:38 | 2026-06-11 07:07 | 0m | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]121` | **2** | 2026-06-11 08:26 | 2026-06-11 08:27 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.186[.]184` | **2** | 2026-06-11 06:08 | 2026-06-11 06:09 | 0m | 0 | `T1592` | 🟢 LOW |
| `111.35.78[.]2` | 1 | 2026-06-11 06:26 | 2026-06-11 06:26 | 30s | 0 | `T1592` | 🟢 LOW |
| `116.99.174[.]228` | 1 | 2026-06-11 05:11 | 2026-06-11 05:11 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `117.50.245[.]253` | 1 | 2026-06-11 07:59 | 2026-06-11 08:00 | 30s | 0 | `T1592` | 🟢 LOW |
| `121.56.226[.]236` | 1 | 2026-06-11 08:01 | 2026-06-11 08:01 | 13s | 0 | `T1592` | 🟢 LOW |
| `159.65.233[.]253` | 1 | 2026-06-11 05:59 | 2026-06-11 06:00 | 33s | 0 | `T1592` | 🟢 LOW |
| `159.65.233[.]253` | 1 | 2026-06-11 08:48 | 2026-06-11 08:48 | 31s | 0 | `T1592` | 🟢 LOW |
| `175.204.224[.]188` | 1 | 2026-06-11 08:27 | 2026-06-11 08:28 | 30s | 0 | `T1592` | 🟢 LOW |
| `177.22.44[.]30` | 1 | 2026-06-11 04:57 | 2026-06-11 04:58 | 30s | 0 | `T1592` | 🟢 LOW |
| `20.115.99[.]68` | 1 | 2026-06-11 07:35 | 2026-06-11 07:35 | 30s | 0 | `T1592` | 🟢 LOW |
| `20.188.116[.]111` | 1 | 2026-06-11 07:01 | 2026-06-11 07:02 | 30s | 0 | `T1592` | 🟢 LOW |
| `34.38.219[.]198` | 1 | 2026-06-11 07:28 | 2026-06-11 07:28 | 3s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]141` | 1 | 2026-06-11 07:09 | 2026-06-11 07:09 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.115[.]134` | 1 | 2026-06-11 06:36 | 2026-06-11 06:36 | 3s | 0 | `T1592` | 🟢 LOW |
| `45.79.207[.]110` | 1 | 2026-06-11 07:33 | 2026-06-11 07:33 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.211[.]97` | 1 | 2026-06-11 07:37 | 2026-06-11 07:37 | 0s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]182` | 1 | 2026-06-11 05:10 | 2026-06-11 05:10 | 2s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]2` | 1 | 2026-06-11 06:55 | 2026-06-11 06:55 | 2s | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]69` | 1 | 2026-06-11 08:35 | 2026-06-11 08:35 | 15s | 0 | `T1592` | 🟢 LOW |
| `69.5.169[.]109` | 1 | 2026-06-11 05:26 | 2026-06-11 05:26 | 0s | 0 | `T1592` | 🟢 LOW |
| `69.5.169[.]94` | 1 | 2026-06-11 05:59 | 2026-06-11 05:59 | 0s | 0 | `T1592` | 🟢 LOW |
| `72.14.178[.]148` | 1 | 2026-06-11 06:36 | 2026-06-11 06:36 | 6s | 0 | `T1592` | 🟢 LOW |
| `81.102.69[.]40` | 1 | 2026-06-11 07:15 | 2026-06-11 07:16 | 13s | 0 | `T1592` | 🟢 LOW |
| `81.19.216[.]68` | 1 | 2026-06-11 08:42 | 2026-06-11 08:42 | 0s | 0 | `T1592` | 🟢 LOW |
| `91.230.168[.]241` | 1 | 2026-06-11 07:15 | 2026-06-11 07:15 | 3s | 0 | `T1592` | 🟢 LOW |
| `91.230.168[.]244` | 1 | 2026-06-11 07:15 | 2026-06-11 07:15 | 0s | 0 | `T1592` | 🟢 LOW |

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
| `116.99.174[.]228` | VN | Viettel Group | **100** ⚠️ | 1 |
| `175.204.224[.]188` | KR | Korea Telecom | **100** ⚠️ | 9 |
| `192.119.13[.]58` | US | Host World Net LLC | **100** ⚠️ | 3 |
| `34.38.219[.]198` | BE | Google LLC | **100** ⚠️ | 3 |
| `45.79.211[.]97` | US | Linode | **100** ⚠️ | 50 |
| `138.2.98[.]41` | SG | Oracle Corporation | **100** ⚠️ | 1 |
| `111.35.78[.]2` | CN | China Mobile Communications Corporation | **100** ⚠️ | 50 |
| `177.22.44[.]30` | BR | Conecta Tecnologia LTDA | **100** ⚠️ | 14 |
| `154.16.146[.]65` | US | OC1-HostForWeb, LLC | **100** ⚠️ | 2 |
| `34.140.236[.]248` | BE | Google LLC | **100** ⚠️ | 0 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 56 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 32 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 5 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 3 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 2 |

---

## 🔕 False Positive Summary (15 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 12 |
| AbuseIPDB score 24 below threshold 25 | 2 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 1 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 103 cases |
| Tool 34  | Credential Extractor        | ✅ 33 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 15 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 45 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 15 filtered (14.6%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 25 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 35 files |
| Tool 33  | YARA Classifier             | ✅ 10 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 32 priority case(s) shown individually · 32 recon entry/entries in table (7 group(s) consolidating 31 session(s)).

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
_Report time: 2026-06-11T10:43:55Z_

# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-06-10 |
| **Generated At** | 2026-06-10T22:07:05Z |
| **Shift Time** | 22:07 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222f |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **208** |
| Confirmed Threats | **178** |
| False Positives Filtered | **30** (14.4%) |
| Unique Attacker IPs | **45** |
| Countries of Origin | **17** |
| High Severity Cases | **55** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **153** |
| Malware Samples Analyzed | **0** HIGH · **20** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **57** |
| Unique Credential Pairs | **24** |
| Unique Usernames | **8** |
| Unique Passwords | **22** |
| Successful Auth Pairs | **38** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 43 |
| `admin` | 7 |
| `user` | 2 |
| `support` | 1 |
| `valery` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `LeitboGi0ro` | 15 |
| `admin` | 7 |
| `123@@@` | 7 |
| `smo@@kkklss` | 5 |
| `12345` | 2 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `LeitboGi0ro` | 15 |
| `root` | `123@@@` | 7 |
| `admin` | `admin` | 5 |
| `root` | `smo@@kkklss` | 5 |
| `root` | `admin` | 2 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `admin` | `188.166.218.0` | 2026-06-10T16:56:10 |
| `admin` | `admin` | `188.166.218.0` | 2026-06-10T16:56:12 |
| `root` | `12345` | `188.166.218.0` | 2026-06-10T16:56:14 |
| `admin` | `12345` | `188.166.218.0` | 2026-06-10T16:56:15 |
| `root` | `default` | `188.166.218.0` | 2026-06-10T16:56:17 |
| `root` | `vizxv` | `188.166.218.0` | 2026-06-10T16:56:19 |
| `support` | `support` | `188.166.218.0` | 2026-06-10T16:56:21 |
| `user` | `user` | `188.166.218.0` | 2026-06-10T16:56:23 |
| `valery` | `valery` | `213.209.159.56` | 2026-06-10T17:06:26 |
| `root` | `LeitboGi0ro` | `129.153.145.135` | 2026-06-10T17:07:55 |
| `root` | `123@@@` | `129.153.145.135` | 2026-06-10T17:07:55 |
| `root` | `smo@@kkklss` | `129.153.145.135` | 2026-06-10T17:08:04 |
| `root` | `password` | `139.59.227.143` | 2026-06-10T17:30:37 |
| `root` | `LeitboGi0ro` | `139.59.227.143` | 2026-06-10T17:30:42 |
| `root` | `MoeClub.org` | `139.59.227.143` | 2026-06-10T17:30:46 |
| `root` | `123@@@` | `165.1.75.106` | 2026-06-10T17:40:24 |
| `root` | `LeitboGi0ro` | `165.1.75.106` | 2026-06-10T17:40:24 |
| `root` | `ubuntu` | `103.161.16.196` | 2026-06-10T17:41:38 |
| `admin` | `admin` | `10.0.0.73` | 2026-06-10T17:52:33 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-06-10T17:58:23 |
| `root` | `123@@@` | `64.110.90.250` | 2026-06-10T17:58:23 |
| `armand` | `armand` | `213.209.159.56` | 2026-06-10T18:10:35 |
| `root` | `---fuck_you----` | `106.13.78.62` | 2026-06-10T18:18:12 |
| `root` | `﻿------fuck------` | `61.169.193.210` | 2026-06-10T18:28:15 |
| `user` | `handcuff` | `193.46.255.86` | 2026-06-10T19:06:59 |
| `root` | `ubuntu` | `120.48.141.101` | 2026-06-10T19:07:35 |
| `bill` | `bill` | `213.209.159.56` | 2026-06-10T19:14:10 |
| `admin` | `doherty` | `2.57.121.112` | 2026-06-10T19:21:33 |
| `root` | `admin` | `94.75.225.81` | 2026-06-10T20:04:43 |
| `root` | `123@@@` | `138.2.98.41` | 2026-06-10T20:07:26 |
| `root` | `LeitboGi0ro` | `138.2.98.41` | 2026-06-10T20:07:26 |
| `root` | `123@@@` | `137.131.9.65` | 2026-06-10T20:14:00 |
| `root` | `LeitboGi0ro` | `137.131.9.65` | 2026-06-10T20:14:05 |
| `root` | `---fuck_you----` | `10.0.0.73` | 2026-06-10T20:17:35 |
| `dejon` | `dejon` | `213.209.159.56` | 2026-06-10T20:17:40 |
| `root` | `123@@@` | `144.22.238.238` | 2026-06-10T20:27:37 |
| `root` | `LeitboGi0ro` | `144.22.238.238` | 2026-06-10T20:27:37 |
| `root` | `smo@@kkklss` | `144.22.238.238` | 2026-06-10T20:27:39 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **208** |
| Sessions with Fingerprint | **14** |
| Unique HASSH Fingerprints | **14** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 30 |
| Paramiko (Python) | 25 |
| PuTTY | 7 |
| libssh | 2 |
| OpenSSH | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `a2de0f306611...` | Mirai/variant | 21 | 5 |
| `16443846184e...` | Generic scanner | 6 | 1 |
| `4e066189c3bb...` | Generic scanner | 6 | 2 |
| `57446c12547a...` | Mirai/variant | 5 | 2 |
| `98f63c4d9c87...` | Generic scanner | 4 | 3 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `a2de0f306611...` | Paramiko (Python) | 21 | 5 | Mirai/variant |
| `95420f9d932d...` | Go SSH scanner | 9 | 6 | — |
| `16443846184e...` | Go SSH scanner | 6 | 1 | Generic scanner |
| `4e066189c3bb...` | Go SSH scanner | 6 | 2 | Generic scanner |
| `57446c12547a...` | PuTTY | 5 | 2 | Mirai/variant |
| `98f63c4d9c87...` | Go SSH scanner | 4 | 3 | Generic scanner |
| `6372ee695756...` | Paramiko (Python) | 4 | 1 | Modern SSH client |
| `98ddc5604ef6...` | Go SSH scanner | 2 | 2 | Modern SSH client |

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **45** |
| Unique ASNs | **24** |
| High-Risk ASNs | **15** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS31898` | Oracle Corporation | 6 | HIGH |
| `AS63949` | Akamai Connected Cloud | 5 | HIGH |
| `AS14061` | DigitalOcean, LLC | 5 | HIGH |
| `AS396982` | Google LLC | 4 | LOW |
| `AS4134` | CHINANET BACKBONE | 3 | LOW |
| `AS38365` | Beijing Baidu Netcom Science and Technology Co., Ltd. | 2 | HIGH |
| `AS47890` | UNMANAGED LTD | 2 | HIGH |
| `AS4837` | CHINA UNICOM China169 Backbone | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (50)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-1227f58be0b2

| Field | Detail |
|---|---|
| **Source IP** | `188.166.218[.]0` |
| **First Seen** | 2026-06-10 16:56 |
| **Last Seen** | 2026-06-10 16:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 16:56:10` | `cowrie.session.connect` |
| `2026-06-10 16:56:10` | `cowrie.telnet.option` |
| `2026-06-10 16:56:10` | `cowrie.login.success` |
| `2026-06-10 16:56:11` | `cowrie.session.params` |
| `2026-06-10 16:56:11` | `cowrie.log.closed` |
| `2026-06-10 16:56:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `188.166.218[.]0` to AbuseIPDB if not already reported
- [ ] Block `188.166.218[.]0` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5b14aae988ce

| Field | Detail |
|---|---|
| **Source IP** | `188.166.218[.]0` |
| **First Seen** | 2026-06-10 16:56 |
| **Last Seen** | 2026-06-10 16:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 16:56:11` | `cowrie.session.connect` |
| `2026-06-10 16:56:12` | `cowrie.telnet.option` |
| `2026-06-10 16:56:12` | `cowrie.login.success` |
| `2026-06-10 16:56:13` | `cowrie.session.params` |
| `2026-06-10 16:56:13` | `cowrie.log.closed` |
| `2026-06-10 16:56:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `188.166.218[.]0` to AbuseIPDB if not already reported
- [ ] Block `188.166.218[.]0` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-db6feffdc854

| Field | Detail |
|---|---|
| **Source IP** | `188.166.218[.]0` |
| **First Seen** | 2026-06-10 16:56 |
| **Last Seen** | 2026-06-10 16:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 16:56:13` | `cowrie.session.connect` |
| `2026-06-10 16:56:14` | `cowrie.telnet.option` |
| `2026-06-10 16:56:14` | `cowrie.login.success` |
| `2026-06-10 16:56:14` | `cowrie.session.params` |
| `2026-06-10 16:56:15` | `cowrie.log.closed` |
| `2026-06-10 16:56:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `188.166.218[.]0` to AbuseIPDB if not already reported
- [ ] Block `188.166.218[.]0` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4bceed6d43a9

| Field | Detail |
|---|---|
| **Source IP** | `188.166.218[.]0` |
| **First Seen** | 2026-06-10 16:56 |
| **Last Seen** | 2026-06-10 16:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 16:56:15` | `cowrie.session.connect` |
| `2026-06-10 16:56:15` | `cowrie.telnet.option` |
| `2026-06-10 16:56:15` | `cowrie.login.success` |
| `2026-06-10 16:56:16` | `cowrie.session.params` |
| `2026-06-10 16:56:16` | `cowrie.log.closed` |
| `2026-06-10 16:56:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `188.166.218[.]0` to AbuseIPDB if not already reported
- [ ] Block `188.166.218[.]0` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e11bd4038de6

| Field | Detail |
|---|---|
| **Source IP** | `188.166.218[.]0` |
| **First Seen** | 2026-06-10 16:56 |
| **Last Seen** | 2026-06-10 16:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 16:56:16` | `cowrie.session.connect` |
| `2026-06-10 16:56:17` | `cowrie.telnet.option` |
| `2026-06-10 16:56:17` | `cowrie.login.success` |
| `2026-06-10 16:56:18` | `cowrie.session.params` |
| `2026-06-10 16:56:18` | `cowrie.log.closed` |
| `2026-06-10 16:56:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `188.166.218[.]0` to AbuseIPDB if not already reported
- [ ] Block `188.166.218[.]0` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-66bdc927b8f9

| Field | Detail |
|---|---|
| **Source IP** | `188.166.218[.]0` |
| **First Seen** | 2026-06-10 16:56 |
| **Last Seen** | 2026-06-10 16:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 16:56:18` | `cowrie.session.connect` |
| `2026-06-10 16:56:19` | `cowrie.telnet.option` |
| `2026-06-10 16:56:19` | `cowrie.login.success` |
| `2026-06-10 16:56:19` | `cowrie.session.params` |
| `2026-06-10 16:56:20` | `cowrie.log.closed` |
| `2026-06-10 16:56:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `188.166.218[.]0` to AbuseIPDB if not already reported
- [ ] Block `188.166.218[.]0` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1427e00d1ac5

| Field | Detail |
|---|---|
| **Source IP** | `188.166.218[.]0` |
| **First Seen** | 2026-06-10 16:56 |
| **Last Seen** | 2026-06-10 16:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 16:56:20` | `cowrie.session.connect` |
| `2026-06-10 16:56:20` | `cowrie.telnet.option` |
| `2026-06-10 16:56:21` | `cowrie.login.success` |
| `2026-06-10 16:56:21` | `cowrie.session.params` |
| `2026-06-10 16:56:21` | `cowrie.log.closed` |
| `2026-06-10 16:56:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `188.166.218[.]0` to AbuseIPDB if not already reported
- [ ] Block `188.166.218[.]0` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-06a5ea71b47f

| Field | Detail |
|---|---|
| **Source IP** | `188.166.218[.]0` |
| **First Seen** | 2026-06-10 16:56 |
| **Last Seen** | 2026-06-10 16:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 16:56:22` | `cowrie.session.connect` |
| `2026-06-10 16:56:22` | `cowrie.telnet.option` |
| `2026-06-10 16:56:23` | `cowrie.login.success` |
| `2026-06-10 16:56:23` | `cowrie.session.params` |
| `2026-06-10 16:56:23` | `cowrie.log.closed` |
| `2026-06-10 16:56:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `188.166.218[.]0` to AbuseIPDB if not already reported
- [ ] Block `188.166.218[.]0` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-da8ec48b8f3d

| Field | Detail |
|---|---|
| **Source IP** | `213.209.159[.]56` |
| **First Seen** | 2026-06-10 17:06 |
| **Last Seen** | 2026-06-10 17:06 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 17:06:26` | `cowrie.session.connect` |
| `2026-06-10 17:06:26` | `cowrie.client.version` |
| `2026-06-10 17:06:26` | `cowrie.client.kex` |
| `2026-06-10 17:06:26` | `cowrie.login.success` |
| `2026-06-10 17:06:26` | `cowrie.direct-tcpip.request` |
| `2026-06-10 17:06:27` | `cowrie.direct-tcpip.data` |
| `2026-06-10 17:06:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.209.159[.]56` to AbuseIPDB if not already reported
- [ ] Block `213.209.159[.]56` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b1ff1371a1d5

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-10 17:07 |
| **Last Seen** | 2026-06-10 17:07 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 17:07:55` | `cowrie.session.connect` |
| `2026-06-10 17:07:55` | `cowrie.client.version` |
| `2026-06-10 17:07:55` | `cowrie.client.kex` |
| `2026-06-10 17:07:55` | `cowrie.login.success` |
| `2026-06-10 17:07:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cf02fa9d4a59

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-10 17:07 |
| **Last Seen** | 2026-06-10 17:07 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 17:07:55` | `cowrie.session.connect` |
| `2026-06-10 17:07:55` | `cowrie.client.version` |
| `2026-06-10 17:07:55` | `cowrie.client.kex` |
| `2026-06-10 17:07:55` | `cowrie.login.success` |
| `2026-06-10 17:07:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-347c2f40f8ba

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-10 17:08 |
| **Last Seen** | 2026-06-10 17:08 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 17:08:04` | `cowrie.session.connect` |
| `2026-06-10 17:08:04` | `cowrie.client.version` |
| `2026-06-10 17:08:04` | `cowrie.client.kex` |
| `2026-06-10 17:08:04` | `cowrie.login.success` |
| `2026-06-10 17:08:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5b1154b16ddc

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-10 17:08 |
| **Last Seen** | 2026-06-10 17:08 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 17:08:04` | `cowrie.session.connect` |
| `2026-06-10 17:08:04` | `cowrie.client.version` |
| `2026-06-10 17:08:04` | `cowrie.client.kex` |
| `2026-06-10 17:08:04` | `cowrie.login.success` |
| `2026-06-10 17:08:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cf3f9389b691

| Field | Detail |
|---|---|
| **Source IP** | `139.59.227[.]143` |
| **First Seen** | 2026-06-10 17:30 |
| **Last Seen** | 2026-06-10 17:30 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -m 2>/dev/null | tr -d '\n\r' || echo 'unknown'; echo '---SEP---'; cat /etc/os-release 2>/dev/null | grep '^NAME=' | cut -d'=' -f2 | tr -d '"' | tr -d '\n\r' || echo 'Linux'; echo '---SEP---'; hostname 2>/dev/null | tr -d '\n\r' || echo 'unknown'; echo '---SEP---'; curl -s --connect-timeout 2 ipinfo.io/country 2>/dev/null | tr -d '\n\r' || echo 'N/A'; echo '---SEP---'; nproc 2>/dev/null | tr -d '\n\r' || echo '1'; echo '---SEP---'; free -h 2>/dev/null | awk '/^Mem:/ {print $2}' | tr -d '\n\r' || echo ` |
| **TTPs (MITRE)** | T1078 · T1083 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 17:30:35` | `cowrie.session.connect` |
| `2026-06-10 17:30:35` | `cowrie.client.version` |
| `2026-06-10 17:30:36` | `cowrie.client.kex` |
| `2026-06-10 17:30:37` | `cowrie.login.success` |
| `2026-06-10 17:30:39` | `cowrie.session.params` |
| `2026-06-10 17:30:39` | `cowrie.command.input` |
| `2026-06-10 17:30:39` | `cowrie.log.closed` |
| `2026-06-10 17:30:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.227[.]143` to AbuseIPDB if not already reported
- [ ] Block `139.59.227[.]143` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0445f4a01fe8

| Field | Detail |
|---|---|
| **Source IP** | `139.59.227[.]143` |
| **First Seen** | 2026-06-10 17:30 |
| **Last Seen** | 2026-06-10 17:30 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -m 2>/dev/null | tr -d '\n\r' || echo 'unknown'; echo '---SEP---'; cat /etc/os-release 2>/dev/null | grep '^NAME=' | cut -d'=' -f2 | tr -d '"' | tr -d '\n\r' || echo 'Linux'; echo '---SEP---'; hostname 2>/dev/null | tr -d '\n\r' || echo 'unknown'; echo '---SEP---'; curl -s --connect-timeout 2 ipinfo.io/country 2>/dev/null | tr -d '\n\r' || echo 'N/A'; echo '---SEP---'; nproc 2>/dev/null | tr -d '\n\r' || echo '1'; echo '---SEP---'; free -h 2>/dev/null | awk '/^Mem:/ {print $2}' | tr -d '\n\r' || echo ` |
| **TTPs (MITRE)** | T1078 · T1083 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 17:30:39` | `cowrie.session.connect` |
| `2026-06-10 17:30:39` | `cowrie.client.version` |
| `2026-06-10 17:30:40` | `cowrie.client.kex` |
| `2026-06-10 17:30:42` | `cowrie.login.success` |
| `2026-06-10 17:30:43` | `cowrie.session.params` |
| `2026-06-10 17:30:43` | `cowrie.command.input` |
| `2026-06-10 17:30:44` | `cowrie.log.closed` |
| `2026-06-10 17:30:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.227[.]143` to AbuseIPDB if not already reported
- [ ] Block `139.59.227[.]143` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-501688941c62

| Field | Detail |
|---|---|
| **Source IP** | `139.59.227[.]143` |
| **First Seen** | 2026-06-10 17:30 |
| **Last Seen** | 2026-06-10 17:30 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -m 2>/dev/null | tr -d '\n\r' || echo 'unknown'; echo '---SEP---'; cat /etc/os-release 2>/dev/null | grep '^NAME=' | cut -d'=' -f2 | tr -d '"' | tr -d '\n\r' || echo 'Linux'; echo '---SEP---'; hostname 2>/dev/null | tr -d '\n\r' || echo 'unknown'; echo '---SEP---'; curl -s --connect-timeout 2 ipinfo.io/country 2>/dev/null | tr -d '\n\r' || echo 'N/A'; echo '---SEP---'; nproc 2>/dev/null | tr -d '\n\r' || echo '1'; echo '---SEP---'; free -h 2>/dev/null | awk '/^Mem:/ {print $2}' | tr -d '\n\r' || echo ` |
| **TTPs (MITRE)** | T1078 · T1083 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 17:30:44` | `cowrie.session.connect` |
| `2026-06-10 17:30:45` | `cowrie.client.version` |
| `2026-06-10 17:30:45` | `cowrie.client.kex` |
| `2026-06-10 17:30:46` | `cowrie.login.success` |
| `2026-06-10 17:30:48` | `cowrie.session.params` |
| `2026-06-10 17:30:48` | `cowrie.command.input` |
| `2026-06-10 17:30:49` | `cowrie.log.closed` |
| `2026-06-10 17:30:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.227[.]143` to AbuseIPDB if not already reported
- [ ] Block `139.59.227[.]143` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b1ff6fa59335

| Field | Detail |
|---|---|
| **Source IP** | `165.1.75[.]106` |
| **First Seen** | 2026-06-10 17:40 |
| **Last Seen** | 2026-06-10 17:40 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 17:40:24` | `cowrie.session.connect` |
| `2026-06-10 17:40:24` | `cowrie.client.version` |
| `2026-06-10 17:40:24` | `cowrie.client.kex` |
| `2026-06-10 17:40:24` | `cowrie.login.success` |
| `2026-06-10 17:40:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.1.75[.]106` to AbuseIPDB if not already reported
- [ ] Block `165.1.75[.]106` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b799b2dc9597

| Field | Detail |
|---|---|
| **Source IP** | `165.1.75[.]106` |
| **First Seen** | 2026-06-10 17:40 |
| **Last Seen** | 2026-06-10 17:40 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 17:40:24` | `cowrie.session.connect` |
| `2026-06-10 17:40:24` | `cowrie.client.version` |
| `2026-06-10 17:40:24` | `cowrie.client.kex` |
| `2026-06-10 17:40:24` | `cowrie.login.success` |
| `2026-06-10 17:40:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.1.75[.]106` to AbuseIPDB if not already reported
- [ ] Block `165.1.75[.]106` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-55ed8991010b

| Field | Detail |
|---|---|
| **Source IP** | `165.1.75[.]106` |
| **First Seen** | 2026-06-10 17:40 |
| **Last Seen** | 2026-06-10 17:42 |
| **Session Duration** | 126s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 17:40:41` | `cowrie.session.connect` |
| `2026-06-10 17:40:41` | `cowrie.client.version` |
| `2026-06-10 17:40:41` | `cowrie.client.kex` |
| `2026-06-10 17:40:41` | `cowrie.login.success` |
| `2026-06-10 17:40:42` | `cowrie.session.file_upload` |
| `2026-06-10 17:40:43` | `cowrie.session.params` |
| `2026-06-10 17:40:43` | `cowrie.command.input` |
| `2026-06-10 17:40:43` | `cowrie.command.input` |
| `2026-06-10 17:40:43` | `cowrie.command.input` |
| `2026-06-10 17:40:43` | `cowrie.command.failed` |
| `2026-06-10 17:40:43` | `cowrie.log.closed` |
| `2026-06-10 17:40:44` | `cowrie.session.params` |
| `2026-06-10 17:40:44` | `cowrie.command.input` |
| `2026-06-10 17:40:44` | `cowrie.log.closed` |
| `2026-06-10 17:40:44` | `cowrie.session.params` |
| `2026-06-10 17:40:44` | `cowrie.command.input` |
| `2026-06-10 17:40:45` | `cowrie.log.closed` |
| `2026-06-10 17:40:45` | `cowrie.session.params` |
| `2026-06-10 17:40:45` | `cowrie.command.input` |
| `2026-06-10 17:40:45` | `cowrie.command.failed` |
| `2026-06-10 17:40:45` | `cowrie.command.failed` |
| `2026-06-10 17:41:46` | `cowrie.session.params` |
| `2026-06-10 17:41:46` | `cowrie.command.input` |
| `2026-06-10 17:42:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.1.75[.]106` to AbuseIPDB if not already reported
- [ ] Block `165.1.75[.]106` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d213e8114121

| Field | Detail |
|---|---|
| **Source IP** | `103.161.16[.]196` |
| **First Seen** | 2026-06-10 17:41 |
| **Last Seen** | 2026-06-10 17:43 |
| **Session Duration** | 93s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 17:41:37` | `cowrie.session.connect` |
| `2026-06-10 17:41:37` | `cowrie.client.version` |
| `2026-06-10 17:41:37` | `cowrie.client.kex` |
| `2026-06-10 17:41:38` | `cowrie.login.success` |
| `2026-06-10 17:43:09` | `cowrie.session.file_upload` |
| `2026-06-10 17:43:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.161.16[.]196` to AbuseIPDB if not already reported
- [ ] Block `103.161.16[.]196` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-72824c3cf972

| Field | Detail |
|---|---|
| **Source IP** | `165.1.75[.]106` |
| **First Seen** | 2026-06-10 17:43 |
| **Last Seen** | 2026-06-10 17:45 |
| **Session Duration** | 126s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 17:43:02` | `cowrie.session.connect` |
| `2026-06-10 17:43:02` | `cowrie.client.version` |
| `2026-06-10 17:43:02` | `cowrie.client.kex` |
| `2026-06-10 17:43:02` | `cowrie.login.success` |
| `2026-06-10 17:43:03` | `cowrie.session.file_upload` |
| `2026-06-10 17:43:04` | `cowrie.session.params` |
| `2026-06-10 17:43:04` | `cowrie.command.input` |
| `2026-06-10 17:43:04` | `cowrie.command.input` |
| `2026-06-10 17:43:04` | `cowrie.command.input` |
| `2026-06-10 17:43:04` | `cowrie.command.failed` |
| `2026-06-10 17:43:04` | `cowrie.log.closed` |
| `2026-06-10 17:43:05` | `cowrie.session.params` |
| `2026-06-10 17:43:05` | `cowrie.command.input` |
| `2026-06-10 17:43:05` | `cowrie.log.closed` |
| `2026-06-10 17:43:06` | `cowrie.session.params` |
| `2026-06-10 17:43:06` | `cowrie.command.input` |
| `2026-06-10 17:43:06` | `cowrie.log.closed` |
| `2026-06-10 17:43:07` | `cowrie.session.params` |
| `2026-06-10 17:43:07` | `cowrie.command.input` |
| `2026-06-10 17:43:07` | `cowrie.command.failed` |
| `2026-06-10 17:43:07` | `cowrie.command.failed` |
| `2026-06-10 17:44:08` | `cowrie.session.params` |
| `2026-06-10 17:44:08` | `cowrie.command.input` |
| `2026-06-10 17:45:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.1.75[.]106` to AbuseIPDB if not already reported
- [ ] Block `165.1.75[.]106` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3d67fafdea7b

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-06-10 17:58 |
| **Last Seen** | 2026-06-10 17:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 17:58:21` | `cowrie.session.connect` |
| `2026-06-10 17:58:21` | `cowrie.client.version` |
| `2026-06-10 17:58:22` | `cowrie.client.kex` |
| `2026-06-10 17:58:23` | `cowrie.login.success` |
| `2026-06-10 17:58:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-965fbdfd91ca

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-06-10 17:58 |
| **Last Seen** | 2026-06-10 17:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 17:58:22` | `cowrie.session.connect` |
| `2026-06-10 17:58:22` | `cowrie.client.version` |
| `2026-06-10 17:58:22` | `cowrie.client.kex` |
| `2026-06-10 17:58:23` | `cowrie.login.success` |
| `2026-06-10 17:58:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1b99e418c3cc

| Field | Detail |
|---|---|
| **Source IP** | `213.209.159[.]56` |
| **First Seen** | 2026-06-10 18:10 |
| **Last Seen** | 2026-06-10 18:10 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 18:10:35` | `cowrie.session.connect` |
| `2026-06-10 18:10:35` | `cowrie.client.version` |
| `2026-06-10 18:10:35` | `cowrie.client.kex` |
| `2026-06-10 18:10:35` | `cowrie.login.success` |
| `2026-06-10 18:10:35` | `cowrie.direct-tcpip.request` |
| `2026-06-10 18:10:36` | `cowrie.direct-tcpip.data` |
| `2026-06-10 18:10:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.209.159[.]56` to AbuseIPDB if not already reported
- [ ] Block `213.209.159[.]56` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ab793a426420

| Field | Detail |
|---|---|
| **Source IP** | `106.13.78[.]62` |
| **First Seen** | 2026-06-10 18:18 |
| **Last Seen** | 2026-06-10 18:18 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 18:18:08` | `cowrie.session.connect` |
| `2026-06-10 18:18:08` | `cowrie.client.version` |
| `2026-06-10 18:18:09` | `cowrie.client.kex` |
| `2026-06-10 18:18:12` | `cowrie.login.success` |
| `2026-06-10 18:18:13` | `cowrie.session.params` |
| `2026-06-10 18:18:13` | `cowrie.command.input` |
| `2026-06-10 18:18:14` | `cowrie.log.closed` |
| `2026-06-10 18:18:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.13.78[.]62` to AbuseIPDB if not already reported
- [ ] Block `106.13.78[.]62` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-00ade656d77d

| Field | Detail |
|---|---|
| **Source IP** | `61.169.193[.]210` |
| **First Seen** | 2026-06-10 18:28 |
| **Last Seen** | 2026-06-10 18:28 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 18:28:14` | `cowrie.session.connect` |
| `2026-06-10 18:28:14` | `cowrie.client.version` |
| `2026-06-10 18:28:14` | `cowrie.client.kex` |
| `2026-06-10 18:28:15` | `cowrie.login.success` |
| `2026-06-10 18:28:16` | `cowrie.session.params` |
| `2026-06-10 18:28:16` | `cowrie.command.input` |
| `2026-06-10 18:28:16` | `cowrie.log.closed` |
| `2026-06-10 18:28:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.169.193[.]210` to AbuseIPDB if not already reported
- [ ] Block `61.169.193[.]210` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-270413063026

| Field | Detail |
|---|---|
| **Source IP** | `139.59.227[.]143` |
| **First Seen** | 2026-06-10 18:32 |
| **Last Seen** | 2026-06-10 18:32 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -m 2>/dev/null | tr -d '\n\r' || echo 'unknown'; echo '---SEP---'; cat /etc/os-release 2>/dev/null | grep '^NAME=' | cut -d'=' -f2 | tr -d '"' | tr -d '\n\r' || echo 'Linux'; echo '---SEP---'; hostname 2>/dev/null | tr -d '\n\r' || echo 'unknown'; echo '---SEP---'; curl -s --connect-timeout 2 ipinfo.io/country 2>/dev/null | tr -d '\n\r' || echo 'N/A'; echo '---SEP---'; nproc 2>/dev/null | tr -d '\n\r' || echo '1'; echo '---SEP---'; free -h 2>/dev/null | awk '/^Mem:/ {print $2}' | tr -d '\n\r' || echo ` |
| **TTPs (MITRE)** | T1078 · T1083 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 18:32:51` | `cowrie.session.connect` |
| `2026-06-10 18:32:51` | `cowrie.client.version` |
| `2026-06-10 18:32:51` | `cowrie.client.kex` |
| `2026-06-10 18:32:53` | `cowrie.login.success` |
| `2026-06-10 18:32:54` | `cowrie.session.params` |
| `2026-06-10 18:32:54` | `cowrie.command.input` |
| `2026-06-10 18:32:55` | `cowrie.log.closed` |
| `2026-06-10 18:32:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.227[.]143` to AbuseIPDB if not already reported
- [ ] Block `139.59.227[.]143` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c635268777f6

| Field | Detail |
|---|---|
| **Source IP** | `139.59.227[.]143` |
| **First Seen** | 2026-06-10 18:32 |
| **Last Seen** | 2026-06-10 18:32 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -m 2>/dev/null | tr -d '\n\r' || echo 'unknown'; echo '---SEP---'; cat /etc/os-release 2>/dev/null | grep '^NAME=' | cut -d'=' -f2 | tr -d '"' | tr -d '\n\r' || echo 'Linux'; echo '---SEP---'; hostname 2>/dev/null | tr -d '\n\r' || echo 'unknown'; echo '---SEP---'; curl -s --connect-timeout 2 ipinfo.io/country 2>/dev/null | tr -d '\n\r' || echo 'N/A'; echo '---SEP---'; nproc 2>/dev/null | tr -d '\n\r' || echo '1'; echo '---SEP---'; free -h 2>/dev/null | awk '/^Mem:/ {print $2}' | tr -d '\n\r' || echo ` |
| **TTPs (MITRE)** | T1078 · T1083 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 18:32:56` | `cowrie.session.connect` |
| `2026-06-10 18:32:56` | `cowrie.client.version` |
| `2026-06-10 18:32:56` | `cowrie.client.kex` |
| `2026-06-10 18:32:57` | `cowrie.login.success` |
| `2026-06-10 18:32:59` | `cowrie.session.params` |
| `2026-06-10 18:32:59` | `cowrie.command.input` |
| `2026-06-10 18:32:59` | `cowrie.log.closed` |
| `2026-06-10 18:32:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.227[.]143` to AbuseIPDB if not already reported
- [ ] Block `139.59.227[.]143` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a6356df91e61

| Field | Detail |
|---|---|
| **Source IP** | `139.59.227[.]143` |
| **First Seen** | 2026-06-10 18:32 |
| **Last Seen** | 2026-06-10 18:33 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -m 2>/dev/null | tr -d '\n\r' || echo 'unknown'; echo '---SEP---'; cat /etc/os-release 2>/dev/null | grep '^NAME=' | cut -d'=' -f2 | tr -d '"' | tr -d '\n\r' || echo 'Linux'; echo '---SEP---'; hostname 2>/dev/null | tr -d '\n\r' || echo 'unknown'; echo '---SEP---'; curl -s --connect-timeout 2 ipinfo.io/country 2>/dev/null | tr -d '\n\r' || echo 'N/A'; echo '---SEP---'; nproc 2>/dev/null | tr -d '\n\r' || echo '1'; echo '---SEP---'; free -h 2>/dev/null | awk '/^Mem:/ {print $2}' | tr -d '\n\r' || echo ` |
| **TTPs (MITRE)** | T1078 · T1083 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 18:32:59` | `cowrie.session.connect` |
| `2026-06-10 18:32:59` | `cowrie.client.version` |
| `2026-06-10 18:33:00` | `cowrie.client.kex` |
| `2026-06-10 18:33:02` | `cowrie.login.success` |
| `2026-06-10 18:33:03` | `cowrie.session.params` |
| `2026-06-10 18:33:03` | `cowrie.command.input` |
| `2026-06-10 18:33:04` | `cowrie.log.closed` |
| `2026-06-10 18:33:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.227[.]143` to AbuseIPDB if not already reported
- [ ] Block `139.59.227[.]143` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c5a42a26bddb

| Field | Detail |
|---|---|
| **Source IP** | `193.46.255[.]86` |
| **First Seen** | 2026-06-10 19:06 |
| **Last Seen** | 2026-06-10 19:07 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 19:06:59` | `cowrie.session.connect` |
| `2026-06-10 19:06:59` | `cowrie.client.version` |
| `2026-06-10 19:06:59` | `cowrie.client.kex` |
| `2026-06-10 19:06:59` | `cowrie.login.success` |
| `2026-06-10 19:07:00` | `cowrie.direct-tcpip.request` |
| `2026-06-10 19:07:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.46.255[.]86` to AbuseIPDB if not already reported
- [ ] Block `193.46.255[.]86` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a942a6287adf

| Field | Detail |
|---|---|
| **Source IP** | `120.48.141[.]101` |
| **First Seen** | 2026-06-10 19:07 |
| **Last Seen** | 2026-06-10 19:12 |
| **Session Duration** | 303s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 19:07:32` | `cowrie.session.connect` |
| `2026-06-10 19:07:32` | `cowrie.client.version` |
| `2026-06-10 19:07:33` | `cowrie.client.kex` |
| `2026-06-10 19:07:35` | `cowrie.login.success` |
| `2026-06-10 19:12:35` | `cowrie.session.file_upload` |
| `2026-06-10 19:12:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.141[.]101` to AbuseIPDB if not already reported
- [ ] Block `120.48.141[.]101` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5b08c184053b

| Field | Detail |
|---|---|
| **Source IP** | `213.209.159[.]56` |
| **First Seen** | 2026-06-10 19:14 |
| **Last Seen** | 2026-06-10 19:14 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 19:14:09` | `cowrie.session.connect` |
| `2026-06-10 19:14:09` | `cowrie.client.version` |
| `2026-06-10 19:14:09` | `cowrie.client.kex` |
| `2026-06-10 19:14:10` | `cowrie.login.success` |
| `2026-06-10 19:14:10` | `cowrie.direct-tcpip.request` |
| `2026-06-10 19:14:10` | `cowrie.direct-tcpip.data` |
| `2026-06-10 19:14:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.209.159[.]56` to AbuseIPDB if not already reported
- [ ] Block `213.209.159[.]56` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-538e47e62759

| Field | Detail |
|---|---|
| **Source IP** | `2.57.121[.]112` |
| **First Seen** | 2026-06-10 19:21 |
| **Last Seen** | 2026-06-10 19:21 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 19:21:32` | `cowrie.session.connect` |
| `2026-06-10 19:21:32` | `cowrie.client.version` |
| `2026-06-10 19:21:32` | `cowrie.client.kex` |
| `2026-06-10 19:21:33` | `cowrie.login.success` |
| `2026-06-10 19:21:33` | `cowrie.direct-tcpip.request` |
| `2026-06-10 19:21:33` | `cowrie.direct-tcpip.data` |
| `2026-06-10 19:21:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.121[.]112` to AbuseIPDB if not already reported
- [ ] Block `2.57.121[.]112` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fad240d41209

| Field | Detail |
|---|---|
| **Source IP** | `94.75.225[.]81` |
| **First Seen** | 2026-06-10 20:04 |
| **Last Seen** | 2026-06-10 20:05 |
| **Session Duration** | 21s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1110.001 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 20:04:41` | `cowrie.session.connect` |
| `2026-06-10 20:04:41` | `cowrie.client.version` |
| `2026-06-10 20:04:41` | `cowrie.client.kex` |
| `2026-06-10 20:04:43` | `cowrie.client.fingerprint` |
| `2026-06-10 20:04:43` | `cowrie.login.failed` |
| `2026-06-10 20:04:43` | `cowrie.login.success` |
| `2026-06-10 20:05:01` | `cowrie.direct-tcpip.request` |
| `2026-06-10 20:05:02` | `cowrie.direct-tcpip.ja4` |
| `2026-06-10 20:05:02` | `cowrie.direct-tcpip.data` |
| `2026-06-10 20:05:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.75.225[.]81` to AbuseIPDB if not already reported
- [ ] Block `94.75.225[.]81` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-60dbc3caf134

| Field | Detail |
|---|---|
| **Source IP** | `138.2.98[.]41` |
| **First Seen** | 2026-06-10 20:07 |
| **Last Seen** | 2026-06-10 20:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 20:07:24` | `cowrie.session.connect` |
| `2026-06-10 20:07:24` | `cowrie.client.version` |
| `2026-06-10 20:07:24` | `cowrie.client.kex` |
| `2026-06-10 20:07:26` | `cowrie.login.success` |
| `2026-06-10 20:07:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.2.98[.]41` to AbuseIPDB if not already reported
- [ ] Block `138.2.98[.]41` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2834a4a7a365

| Field | Detail |
|---|---|
| **Source IP** | `138.2.98[.]41` |
| **First Seen** | 2026-06-10 20:07 |
| **Last Seen** | 2026-06-10 20:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 20:07:25` | `cowrie.session.connect` |
| `2026-06-10 20:07:25` | `cowrie.client.version` |
| `2026-06-10 20:07:25` | `cowrie.client.kex` |
| `2026-06-10 20:07:26` | `cowrie.login.success` |
| `2026-06-10 20:07:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.2.98[.]41` to AbuseIPDB if not already reported
- [ ] Block `138.2.98[.]41` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8dc485519ea3

| Field | Detail |
|---|---|
| **Source IP** | `138.2.98[.]41` |
| **First Seen** | 2026-06-10 20:07 |
| **Last Seen** | 2026-06-10 20:10 |
| **Session Duration** | 131s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 20:07:50` | `cowrie.session.connect` |
| `2026-06-10 20:07:50` | `cowrie.client.version` |
| `2026-06-10 20:07:50` | `cowrie.client.kex` |
| `2026-06-10 20:07:51` | `cowrie.login.success` |
| `2026-06-10 20:07:53` | `cowrie.session.file_upload` |
| `2026-06-10 20:07:55` | `cowrie.session.params` |
| `2026-06-10 20:07:55` | `cowrie.command.input` |
| `2026-06-10 20:07:55` | `cowrie.command.input` |
| `2026-06-10 20:07:55` | `cowrie.command.input` |
| `2026-06-10 20:07:55` | `cowrie.command.failed` |
| `2026-06-10 20:07:55` | `cowrie.log.closed` |
| `2026-06-10 20:07:56` | `cowrie.session.params` |
| `2026-06-10 20:07:56` | `cowrie.command.input` |
| `2026-06-10 20:07:56` | `cowrie.log.closed` |
| `2026-06-10 20:07:57` | `cowrie.session.params` |
| `2026-06-10 20:07:57` | `cowrie.command.input` |
| `2026-06-10 20:07:58` | `cowrie.log.closed` |
| `2026-06-10 20:07:59` | `cowrie.session.params` |
| `2026-06-10 20:07:59` | `cowrie.command.input` |
| `2026-06-10 20:07:59` | `cowrie.command.failed` |
| `2026-06-10 20:07:59` | `cowrie.command.failed` |
| `2026-06-10 20:09:00` | `cowrie.session.params` |
| `2026-06-10 20:09:00` | `cowrie.command.input` |
| `2026-06-10 20:10:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.2.98[.]41` to AbuseIPDB if not already reported
- [ ] Block `138.2.98[.]41` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-84a97500e481

| Field | Detail |
|---|---|
| **Source IP** | `138.2.98[.]41` |
| **First Seen** | 2026-06-10 20:10 |
| **Last Seen** | 2026-06-10 20:12 |
| **Session Duration** | 131s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 20:10:16` | `cowrie.session.connect` |
| `2026-06-10 20:10:16` | `cowrie.client.version` |
| `2026-06-10 20:10:17` | `cowrie.client.kex` |
| `2026-06-10 20:10:18` | `cowrie.login.success` |
| `2026-06-10 20:10:20` | `cowrie.session.file_upload` |
| `2026-06-10 20:10:21` | `cowrie.session.params` |
| `2026-06-10 20:10:21` | `cowrie.command.input` |
| `2026-06-10 20:10:21` | `cowrie.command.input` |
| `2026-06-10 20:10:21` | `cowrie.command.input` |
| `2026-06-10 20:10:21` | `cowrie.command.failed` |
| `2026-06-10 20:10:21` | `cowrie.log.closed` |
| `2026-06-10 20:10:22` | `cowrie.session.params` |
| `2026-06-10 20:10:22` | `cowrie.command.input` |
| `2026-06-10 20:10:23` | `cowrie.log.closed` |
| `2026-06-10 20:10:24` | `cowrie.session.params` |
| `2026-06-10 20:10:24` | `cowrie.command.input` |
| `2026-06-10 20:10:24` | `cowrie.log.closed` |
| `2026-06-10 20:10:25` | `cowrie.session.params` |
| `2026-06-10 20:10:25` | `cowrie.command.input` |
| `2026-06-10 20:10:25` | `cowrie.command.failed` |
| `2026-06-10 20:10:25` | `cowrie.command.failed` |
| `2026-06-10 20:11:26` | `cowrie.session.params` |
| `2026-06-10 20:11:26` | `cowrie.command.input` |
| `2026-06-10 20:12:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.2.98[.]41` to AbuseIPDB if not already reported
- [ ] Block `138.2.98[.]41` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cab1bff19421

| Field | Detail |
|---|---|
| **Source IP** | `137.131.9[.]65` |
| **First Seen** | 2026-06-10 20:14 |
| **Last Seen** | 2026-06-10 20:14 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 20:14:00` | `cowrie.session.connect` |
| `2026-06-10 20:14:00` | `cowrie.client.version` |
| `2026-06-10 20:14:00` | `cowrie.client.kex` |
| `2026-06-10 20:14:00` | `cowrie.login.success` |
| `2026-06-10 20:14:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `137.131.9[.]65` to AbuseIPDB if not already reported
- [ ] Block `137.131.9[.]65` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9876c243d7f8

| Field | Detail |
|---|---|
| **Source IP** | `137.131.9[.]65` |
| **First Seen** | 2026-06-10 20:14 |
| **Last Seen** | 2026-06-10 20:14 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 20:14:05` | `cowrie.session.connect` |
| `2026-06-10 20:14:05` | `cowrie.client.version` |
| `2026-06-10 20:14:05` | `cowrie.client.kex` |
| `2026-06-10 20:14:05` | `cowrie.login.success` |
| `2026-06-10 20:14:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `137.131.9[.]65` to AbuseIPDB if not already reported
- [ ] Block `137.131.9[.]65` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dff3cd0c0393

| Field | Detail |
|---|---|
| **Source IP** | `137.131.9[.]65` |
| **First Seen** | 2026-06-10 20:14 |
| **Last Seen** | 2026-06-10 20:16 |
| **Session Duration** | 137s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 20:14:23` | `cowrie.session.connect` |
| `2026-06-10 20:14:23` | `cowrie.client.version` |
| `2026-06-10 20:14:23` | `cowrie.client.kex` |
| `2026-06-10 20:14:24` | `cowrie.login.success` |
| `2026-06-10 20:14:25` | `cowrie.session.file_upload` |
| `2026-06-10 20:14:26` | `cowrie.session.params` |
| `2026-06-10 20:14:26` | `cowrie.command.input` |
| `2026-06-10 20:14:26` | `cowrie.command.input` |
| `2026-06-10 20:14:26` | `cowrie.command.input` |
| `2026-06-10 20:14:26` | `cowrie.command.failed` |
| `2026-06-10 20:14:26` | `cowrie.log.closed` |
| `2026-06-10 20:14:27` | `cowrie.session.params` |
| `2026-06-10 20:14:27` | `cowrie.command.input` |
| `2026-06-10 20:14:27` | `cowrie.log.closed` |
| `2026-06-10 20:14:28` | `cowrie.session.params` |
| `2026-06-10 20:14:28` | `cowrie.command.input` |
| `2026-06-10 20:14:28` | `cowrie.log.closed` |
| `2026-06-10 20:14:28` | `cowrie.session.params` |
| `2026-06-10 20:14:28` | `cowrie.command.input` |
| `2026-06-10 20:14:28` | `cowrie.command.failed` |
| `2026-06-10 20:14:28` | `cowrie.command.failed` |
| `2026-06-10 20:15:29` | `cowrie.session.params` |
| `2026-06-10 20:15:29` | `cowrie.command.input` |
| `2026-06-10 20:16:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `137.131.9[.]65` to AbuseIPDB if not already reported
- [ ] Block `137.131.9[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-13f45b2ba6b9

| Field | Detail |
|---|---|
| **Source IP** | `137.131.9[.]65` |
| **First Seen** | 2026-06-10 20:16 |
| **Last Seen** | 2026-06-10 20:19 |
| **Session Duration** | 136s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 20:16:55` | `cowrie.session.connect` |
| `2026-06-10 20:16:55` | `cowrie.client.version` |
| `2026-06-10 20:16:55` | `cowrie.client.kex` |
| `2026-06-10 20:16:56` | `cowrie.login.success` |
| `2026-06-10 20:16:57` | `cowrie.session.file_upload` |
| `2026-06-10 20:16:58` | `cowrie.session.params` |
| `2026-06-10 20:16:58` | `cowrie.command.input` |
| `2026-06-10 20:16:58` | `cowrie.command.input` |
| `2026-06-10 20:16:58` | `cowrie.command.input` |
| `2026-06-10 20:16:58` | `cowrie.command.failed` |
| `2026-06-10 20:16:58` | `cowrie.log.closed` |
| `2026-06-10 20:16:59` | `cowrie.session.params` |
| `2026-06-10 20:16:59` | `cowrie.command.input` |
| `2026-06-10 20:16:59` | `cowrie.log.closed` |
| `2026-06-10 20:16:59` | `cowrie.session.params` |
| `2026-06-10 20:16:59` | `cowrie.command.input` |
| `2026-06-10 20:17:00` | `cowrie.log.closed` |
| `2026-06-10 20:17:00` | `cowrie.session.params` |
| `2026-06-10 20:17:00` | `cowrie.command.input` |
| `2026-06-10 20:17:00` | `cowrie.command.failed` |
| `2026-06-10 20:17:00` | `cowrie.command.failed` |
| `2026-06-10 20:18:01` | `cowrie.session.params` |
| `2026-06-10 20:18:01` | `cowrie.command.input` |
| `2026-06-10 20:19:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `137.131.9[.]65` to AbuseIPDB if not already reported
- [ ] Block `137.131.9[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3fd0101ebf71

| Field | Detail |
|---|---|
| **Source IP** | `213.209.159[.]56` |
| **First Seen** | 2026-06-10 20:17 |
| **Last Seen** | 2026-06-10 20:17 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 20:17:40` | `cowrie.session.connect` |
| `2026-06-10 20:17:40` | `cowrie.client.version` |
| `2026-06-10 20:17:40` | `cowrie.client.kex` |
| `2026-06-10 20:17:40` | `cowrie.login.success` |
| `2026-06-10 20:17:41` | `cowrie.direct-tcpip.request` |
| `2026-06-10 20:17:41` | `cowrie.direct-tcpip.data` |
| `2026-06-10 20:17:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.209.159[.]56` to AbuseIPDB if not already reported
- [ ] Block `213.209.159[.]56` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5a14ce9e269e

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-06-10 20:27 |
| **Last Seen** | 2026-06-10 20:27 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 20:27:36` | `cowrie.session.connect` |
| `2026-06-10 20:27:36` | `cowrie.client.version` |
| `2026-06-10 20:27:36` | `cowrie.client.kex` |
| `2026-06-10 20:27:37` | `cowrie.login.success` |
| `2026-06-10 20:27:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5e80412e1e8f

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-06-10 20:27 |
| **Last Seen** | 2026-06-10 20:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 20:27:36` | `cowrie.session.connect` |
| `2026-06-10 20:27:36` | `cowrie.client.version` |
| `2026-06-10 20:27:36` | `cowrie.client.kex` |
| `2026-06-10 20:27:37` | `cowrie.login.success` |
| `2026-06-10 20:27:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b6c5a316542f

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-06-10 20:27 |
| **Last Seen** | 2026-06-10 20:27 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 20:27:38` | `cowrie.session.connect` |
| `2026-06-10 20:27:38` | `cowrie.client.version` |
| `2026-06-10 20:27:38` | `cowrie.client.kex` |
| `2026-06-10 20:27:39` | `cowrie.login.success` |
| `2026-06-10 20:27:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7e97195359ad

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-06-10 20:27 |
| **Last Seen** | 2026-06-10 20:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 20:27:39` | `cowrie.session.connect` |
| `2026-06-10 20:27:39` | `cowrie.client.version` |
| `2026-06-10 20:27:39` | `cowrie.client.kex` |
| `2026-06-10 20:27:40` | `cowrie.login.success` |
| `2026-06-10 20:27:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-76b15eea5cbe

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-10 20:29 |
| **Last Seen** | 2026-06-10 20:29 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 20:29:13` | `cowrie.session.connect` |
| `2026-06-10 20:29:13` | `cowrie.client.version` |
| `2026-06-10 20:29:13` | `cowrie.client.kex` |
| `2026-06-10 20:29:13` | `cowrie.login.success` |
| `2026-06-10 20:29:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8cc12591e749

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-10 20:29 |
| **Last Seen** | 2026-06-10 20:29 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 20:29:14` | `cowrie.session.connect` |
| `2026-06-10 20:29:14` | `cowrie.client.version` |
| `2026-06-10 20:29:14` | `cowrie.client.kex` |
| `2026-06-10 20:29:14` | `cowrie.login.success` |
| `2026-06-10 20:29:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1232b8e6ac92

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-10 20:29 |
| **Last Seen** | 2026-06-10 20:29 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 20:29:20` | `cowrie.session.connect` |
| `2026-06-10 20:29:20` | `cowrie.client.version` |
| `2026-06-10 20:29:20` | `cowrie.client.kex` |
| `2026-06-10 20:29:20` | `cowrie.login.success` |
| `2026-06-10 20:29:20` | `cowrie.session.closed` |

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
| `143.198.150[.]219` | **94** | 2026-06-10 16:57 | 2026-06-10 18:19 | 80m | 0 | `T1592` | 🟠 MEDIUM |
| `206.81.2[.]201` | **13** | 2026-06-10 17:06 | 2026-06-10 20:10 | 9m | 0 | `T1592` | 🟠 MEDIUM |
| `172.236.228[.]220` | **3** | 2026-06-10 19:56 | 2026-06-10 19:56 | 0m | 0 | `T1592` | 🟢 LOW |
| `172.236.228[.]86` | **3** | 2026-06-10 19:57 | 2026-06-10 19:57 | 0m | 0 | `T1592` | 🟢 LOW |
| `101.75.224[.]26` | **2** | 2026-06-10 18:57 | 2026-06-10 18:59 | 2m | 0 | `T1592` | 🟢 LOW |
| `193.8.186[.]31` | **2** | 2026-06-10 19:05 | 2026-06-10 19:05 | 0m | 0 | `T1592` | 🟢 LOW |
| `20.171.8[.]156` | **2** | 2026-06-10 19:33 | 2026-06-10 19:33 | 0m | 0 | `T1592` | 🟢 LOW |
| `106.13.78[.]62` | 1 | 2026-06-10 18:18 | 2026-06-10 18:18 | 2s | 0 | `T1592` | 🟢 LOW |
| `159.65.233[.]253` | 1 | 2026-06-10 20:46 | 2026-06-10 20:46 | 31s | 0 | `T1592` | 🟢 LOW |
| `188.166.218[.]0` | 1 | 2026-06-10 16:56 | 2026-06-10 16:56 | 1s | 1 | `T1110.001` | 🟢 LOW |
| `45.148.10[.]121` | 1 | 2026-06-10 20:48 | 2026-06-10 20:48 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.227.254[.]170` | 1 | 2026-06-10 19:07 | 2026-06-10 19:07 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.115[.]134` | 1 | 2026-06-10 19:55 | 2026-06-10 19:55 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.207[.]252` | 1 | 2026-06-10 19:57 | 2026-06-10 19:57 | 0s | 0 | `T1592` | 🟢 LOW |
| `49.243.7[.]105` | 1 | 2026-06-10 16:59 | 2026-06-10 17:00 | 31s | 0 | `T1592` | 🟢 LOW |
| `61.169.193[.]210` | 1 | 2026-06-10 18:28 | 2026-06-10 18:28 | 0s | 0 | `T1592` | 🟢 LOW |

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
| `188.166.218[.]0` | SG | DigitalOcean, LLC | **100** ⚠️ | 0 |
| `193.8.186[.]31` | GB | Vlad Cojuhari | **100** ⚠️ | 13 |
| `129.153.145[.]135` | US | Oracle Corporation | **100** ⚠️ | 7 |
| `120.48.141[.]101` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 25 |
| `45.79.115[.]134` | US | Linode | **100** ⚠️ | 50 |
| `144.22.238[.]238` | BR | Oracle Corporation | **100** ⚠️ | 2 |
| `172.236.228[.]220` | US | Linode | **100** ⚠️ | 50 |
| `45.148.10[.]121` | NL | TECHOFF SRV LIMITED | **100** ⚠️ | 50 |
| `49.243.7[.]105` | JP | FreeBit Co., Ltd. | **100** ⚠️ | 1 |
| `103.161.16[.]196` | VN | BK INFORMATION SYSTEM JOINT STOCK COMPANY | **100** ⚠️ | 39 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 65 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 55 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 14 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 6 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 6 |

---

## 🔕 False Positive Summary (30 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 20 |
| AbuseIPDB score 11 below threshold 25 | 1 |
| AbuseIPDB score 16 below threshold 25 | 1 |
| AbuseIPDB score 4 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 7 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 208 cases |
| Tool 34  | Credential Extractor        | ✅ 57 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 14 fingerprints |
| Tool 36  | Command Clustering          | ✅ 3 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 45 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 30 filtered (14.4%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 24 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 35 files |
| Tool 33  | YARA Classifier             | ✅ 10 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 50 priority case(s) shown individually · 16 recon entry/entries in table (7 group(s) consolidating 119 session(s)).

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
_Report time: 2026-06-10T22:07:05Z_

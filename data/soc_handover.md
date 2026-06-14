# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-06-14 |
| **Generated At** | 2026-06-14T23:12:22Z |
| **Shift Time** | 23:12 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **70** |
| Confirmed Threats | **43** |
| False Positives Filtered | **27** (38.6%) |
| Unique Attacker IPs | **24** |
| Countries of Origin | **12** |
| High Severity Cases | **14** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **56** |
| Malware Samples Analyzed | **0** HIGH · **20** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **17** |
| Unique Credential Pairs | **8** |
| Unique Usernames | **1** |
| Unique Passwords | **8** |
| Successful Auth Pairs | **10** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 17 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `LeitboGi0ro` | 4 |
| `` | 3 |
| `﻿------fuck------` | 2 |
| `123@@@` | 2 |
| `testusr` | 2 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `LeitboGi0ro` | 4 |
| `root` | `` | 3 |
| `root` | `﻿------fuck------` | 2 |
| `root` | `123@@@` | 2 |
| `root` | `testusr` | 2 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `﻿------fuck------` | `10.0.0.73` | 2026-06-14T21:29:10 |
| `root` | `LeitboGi0ro` | `137.131.9.65` | 2026-06-14T21:34:33 |
| `root` | `123@@@` | `137.131.9.65` | 2026-06-14T21:34:33 |
| `root` | `testusr` | `10.0.0.73` | 2026-06-14T21:41:38 |
| `root` | `123@@@` | `129.153.145.135` | 2026-06-14T21:43:55 |
| `root` | `LeitboGi0ro` | `129.153.145.135` | 2026-06-14T21:43:55 |
| `root` | `smo@@kkklss` | `129.153.145.135` | 2026-06-14T21:43:56 |
| `root` | `admin` | `192.42.116.117` | 2026-06-14T21:53:08 |
| `root` | `debian` | `113.0.152.164` | 2026-06-14T22:17:28 |
| `root` | `﻿------fuck------` | `111.29.52.71` | 2026-06-14T22:28:41 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **70** |
| Sessions with Fingerprint | **12** |
| Unique HASSH Fingerprints | **12** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 16 |
| Paramiko (Python) | 8 |
| Go SSH scanner | 8 |
| OpenSSH | 1 |
| PuTTY | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `6372ee695756...` | Modern SSH client | 4 | 1 |
| `a2de0f306611...` | Mirai/variant | 4 | 1 |
| `4e066189c3bb...` | Generic scanner | 3 | 1 |
| `98f63c4d9c87...` | Generic scanner | 2 | 2 |
| `f1e5e9d24e5e...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `95420f9d932d...` | libssh | 15 | 4 | — |
| `6372ee695756...` | Paramiko (Python) | 4 | 1 | Modern SSH client |
| `a2de0f306611...` | Paramiko (Python) | 4 | 1 | Mirai/variant |
| `4e066189c3bb...` | Go SSH scanner | 3 | 1 | Generic scanner |
| `98f63c4d9c87...` | Go SSH scanner | 2 | 2 | Generic scanner |
| `f1e5e9d24e5e...` | Go SSH scanner | 1 | 1 | Mirai/variant |
| `19532158b559...` | libssh | 1 | 1 | Mirai/variant |
| `5f904648ee89...` | Go SSH scanner | 1 | 1 | Generic scanner |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **3** |
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
Source IPs: `10.0.0.73`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **24** |
| Unique ASNs | **19** |
| High-Risk ASNs | **14** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS396982` | Google LLC | 3 | LOW |
| `AS63949` | Akamai Connected Cloud | 2 | HIGH |
| `AS14061` | DigitalOcean, LLC | 2 | HIGH |
| `AS31898` | Oracle Corporation | 2 | HIGH |
| `AS45090` | Shenzhen Tencent Computer Systems Company Limited | 1 | MEDIUM |
| `AS209334` | Modat B.V. | 1 | HIGH |
| `AS21723` | GOCO TECHNOLOGY LIMITED PARTNERSHIP | 1 | HIGH |
| `AS9808` | China Mobile Communications Group Co., Ltd. | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (11)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-b138cc7bf778

| Field | Detail |
|---|---|
| **Source IP** | `137.131.9[.]65` |
| **First Seen** | 2026-06-14 21:34 |
| **Last Seen** | 2026-06-14 21:34 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 21:34:33` | `cowrie.session.connect` |
| `2026-06-14 21:34:33` | `cowrie.client.version` |
| `2026-06-14 21:34:33` | `cowrie.client.kex` |
| `2026-06-14 21:34:33` | `cowrie.login.success` |
| `2026-06-14 21:34:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `137.131.9[.]65` to AbuseIPDB if not already reported
- [ ] Block `137.131.9[.]65` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-33f2e891ce27

| Field | Detail |
|---|---|
| **Source IP** | `137.131.9[.]65` |
| **First Seen** | 2026-06-14 21:34 |
| **Last Seen** | 2026-06-14 21:34 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 21:34:33` | `cowrie.session.connect` |
| `2026-06-14 21:34:33` | `cowrie.client.version` |
| `2026-06-14 21:34:33` | `cowrie.client.kex` |
| `2026-06-14 21:34:33` | `cowrie.login.success` |
| `2026-06-14 21:34:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `137.131.9[.]65` to AbuseIPDB if not already reported
- [ ] Block `137.131.9[.]65` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-13d3313712e1

| Field | Detail |
|---|---|
| **Source IP** | `137.131.9[.]65` |
| **First Seen** | 2026-06-14 21:34 |
| **Last Seen** | 2026-06-14 21:37 |
| **Session Duration** | 137s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 21:34:49` | `cowrie.session.connect` |
| `2026-06-14 21:34:49` | `cowrie.client.version` |
| `2026-06-14 21:34:49` | `cowrie.client.kex` |
| `2026-06-14 21:34:49` | `cowrie.login.success` |
| `2026-06-14 21:34:51` | `cowrie.session.file_upload` |
| `2026-06-14 21:34:51` | `cowrie.session.params` |
| `2026-06-14 21:34:51` | `cowrie.command.input` |
| `2026-06-14 21:34:51` | `cowrie.command.input` |
| `2026-06-14 21:34:51` | `cowrie.command.input` |
| `2026-06-14 21:34:51` | `cowrie.command.failed` |
| `2026-06-14 21:34:51` | `cowrie.log.closed` |
| `2026-06-14 21:34:52` | `cowrie.session.params` |
| `2026-06-14 21:34:52` | `cowrie.command.input` |
| `2026-06-14 21:34:52` | `cowrie.log.closed` |
| `2026-06-14 21:34:53` | `cowrie.session.params` |
| `2026-06-14 21:34:53` | `cowrie.command.input` |
| `2026-06-14 21:34:53` | `cowrie.log.closed` |
| `2026-06-14 21:34:54` | `cowrie.session.params` |
| `2026-06-14 21:34:54` | `cowrie.command.input` |
| `2026-06-14 21:34:54` | `cowrie.command.failed` |
| `2026-06-14 21:34:54` | `cowrie.command.failed` |
| `2026-06-14 21:35:55` | `cowrie.session.params` |
| `2026-06-14 21:35:55` | `cowrie.command.input` |
| `2026-06-14 21:37:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `137.131.9[.]65` to AbuseIPDB if not already reported
- [ ] Block `137.131.9[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-43fda8de5949

| Field | Detail |
|---|---|
| **Source IP** | `137.131.9[.]65` |
| **First Seen** | 2026-06-14 21:37 |
| **Last Seen** | 2026-06-14 21:39 |
| **Session Duration** | 137s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 21:37:21` | `cowrie.session.connect` |
| `2026-06-14 21:37:21` | `cowrie.client.version` |
| `2026-06-14 21:37:21` | `cowrie.client.kex` |
| `2026-06-14 21:37:22` | `cowrie.login.success` |
| `2026-06-14 21:37:23` | `cowrie.session.file_upload` |
| `2026-06-14 21:37:24` | `cowrie.session.params` |
| `2026-06-14 21:37:24` | `cowrie.command.input` |
| `2026-06-14 21:37:24` | `cowrie.command.input` |
| `2026-06-14 21:37:24` | `cowrie.command.input` |
| `2026-06-14 21:37:24` | `cowrie.command.failed` |
| `2026-06-14 21:37:24` | `cowrie.log.closed` |
| `2026-06-14 21:37:25` | `cowrie.session.params` |
| `2026-06-14 21:37:25` | `cowrie.command.input` |
| `2026-06-14 21:37:25` | `cowrie.log.closed` |
| `2026-06-14 21:37:26` | `cowrie.session.params` |
| `2026-06-14 21:37:26` | `cowrie.command.input` |
| `2026-06-14 21:37:26` | `cowrie.log.closed` |
| `2026-06-14 21:37:27` | `cowrie.session.params` |
| `2026-06-14 21:37:27` | `cowrie.command.input` |
| `2026-06-14 21:37:27` | `cowrie.command.failed` |
| `2026-06-14 21:37:27` | `cowrie.command.failed` |
| `2026-06-14 21:38:28` | `cowrie.session.params` |
| `2026-06-14 21:38:28` | `cowrie.command.input` |
| `2026-06-14 21:39:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `137.131.9[.]65` to AbuseIPDB if not already reported
- [ ] Block `137.131.9[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-26655bf643dc

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-14 21:43 |
| **Last Seen** | 2026-06-14 21:43 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 21:43:55` | `cowrie.session.connect` |
| `2026-06-14 21:43:55` | `cowrie.client.version` |
| `2026-06-14 21:43:55` | `cowrie.client.kex` |
| `2026-06-14 21:43:55` | `cowrie.login.success` |
| `2026-06-14 21:43:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-589f6666e25e

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-14 21:43 |
| **Last Seen** | 2026-06-14 21:43 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 21:43:55` | `cowrie.session.connect` |
| `2026-06-14 21:43:55` | `cowrie.client.version` |
| `2026-06-14 21:43:55` | `cowrie.client.kex` |
| `2026-06-14 21:43:55` | `cowrie.login.success` |
| `2026-06-14 21:43:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c8aeb447da85

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-14 21:43 |
| **Last Seen** | 2026-06-14 21:43 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 21:43:56` | `cowrie.session.connect` |
| `2026-06-14 21:43:56` | `cowrie.client.version` |
| `2026-06-14 21:43:56` | `cowrie.client.kex` |
| `2026-06-14 21:43:56` | `cowrie.login.success` |
| `2026-06-14 21:43:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e8d4e50ae2fd

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-14 21:43 |
| **Last Seen** | 2026-06-14 21:43 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 21:43:56` | `cowrie.session.connect` |
| `2026-06-14 21:43:56` | `cowrie.client.version` |
| `2026-06-14 21:43:56` | `cowrie.client.kex` |
| `2026-06-14 21:43:56` | `cowrie.login.success` |
| `2026-06-14 21:43:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c1c13764f7ec

| Field | Detail |
|---|---|
| **Source IP** | `192.42.116[.]117` |
| **First Seen** | 2026-06-14 21:53 |
| **Last Seen** | 2026-06-14 21:53 |
| **Session Duration** | 24s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1110.001 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 21:53:06` | `cowrie.session.connect` |
| `2026-06-14 21:53:07` | `cowrie.client.version` |
| `2026-06-14 21:53:07` | `cowrie.client.kex` |
| `2026-06-14 21:53:08` | `cowrie.client.fingerprint` |
| `2026-06-14 21:53:08` | `cowrie.login.failed` |
| `2026-06-14 21:53:08` | `cowrie.login.success` |
| `2026-06-14 21:53:30` | `cowrie.direct-tcpip.request` |
| `2026-06-14 21:53:30` | `cowrie.direct-tcpip.ja4` |
| `2026-06-14 21:53:30` | `cowrie.direct-tcpip.data` |
| `2026-06-14 21:53:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `192.42.116[.]117` to AbuseIPDB if not already reported
- [ ] Block `192.42.116[.]117` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bca5265fe4e0

| Field | Detail |
|---|---|
| **Source IP** | `113.0.152[.]164` |
| **First Seen** | 2026-06-14 22:15 |
| **Last Seen** | 2026-06-14 22:22 |
| **Session Duration** | 402s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 22:15:46` | `cowrie.session.connect` |
| `2026-06-14 22:17:27` | `cowrie.client.version` |
| `2026-06-14 22:17:27` | `cowrie.client.kex` |
| `2026-06-14 22:17:28` | `cowrie.login.success` |
| `2026-06-14 22:22:28` | `cowrie.session.file_upload` |
| `2026-06-14 22:22:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.0.152[.]164` to AbuseIPDB if not already reported
- [ ] Block `113.0.152[.]164` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e5e108cf4597

| Field | Detail |
|---|---|
| **Source IP** | `111.29.52[.]71` |
| **First Seen** | 2026-06-14 22:28 |
| **Last Seen** | 2026-06-14 22:28 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 22:28:40` | `cowrie.session.connect` |
| `2026-06-14 22:28:40` | `cowrie.client.version` |
| `2026-06-14 22:28:40` | `cowrie.client.kex` |
| `2026-06-14 22:28:41` | `cowrie.login.success` |
| `2026-06-14 22:28:42` | `cowrie.session.params` |
| `2026-06-14 22:28:42` | `cowrie.command.input` |
| `2026-06-14 22:28:42` | `cowrie.log.closed` |
| `2026-06-14 22:28:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.29.52[.]71` to AbuseIPDB if not already reported
- [ ] Block `111.29.52[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `188.166.223[.]22` | **9** | 2026-06-14 20:56 | 2026-06-14 22:32 | 7m | 0 | `T1592` | 🟢 LOW |
| `154.16.146[.]65` | **8** | 2026-06-14 21:10 | 2026-06-14 22:52 | 6m | 0 | `T1592` | 🟢 LOW |
| `45.82.78[.]106` | **3** | 2026-06-14 21:13 | 2026-06-14 21:13 | 0m | 0 | `T1592` | 🟢 LOW |
| `172.235.41[.]110` | **2** | 2026-06-14 21:33 | 2026-06-14 21:33 | 0m | 0 | `T1592` | 🟢 LOW |
| `111.29.52[.]71` | 1 | 2026-06-14 22:28 | 2026-06-14 22:28 | 0s | 0 | `T1592` | 🟢 LOW |
| `113.0.152[.]164` | 1 | 2026-06-14 22:00 | 2026-06-14 22:02 | 120s | 0 | `T1592` | 🟢 LOW |
| `120.28.189[.]223` | 1 | 2026-06-14 21:07 | 2026-06-14 21:07 | 13s | 0 | `T1592` | 🟢 LOW |
| `134.209.93[.]206` | 1 | 2026-06-14 21:17 | 2026-06-14 21:19 | 120s | 0 | `T1592` | 🟢 LOW |
| `139.19.117[.]129` | 1 | 2026-06-14 21:18 | 2026-06-14 21:18 | 10s | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `162.255.251[.]91` | 1 | 2026-06-14 20:57 | 2026-06-14 20:57 | 13s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]151` | 1 | 2026-06-14 22:06 | 2026-06-14 22:06 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.207[.]110` | 1 | 2026-06-14 20:58 | 2026-06-14 20:58 | 0s | 0 | `T1592` | 🟢 LOW |
| `64.89.160[.]135` | 1 | 2026-06-14 22:37 | 2026-06-14 22:37 | 0s | 0 | `T1592` | 🟢 LOW |
| `85.217.149[.]22` | 1 | 2026-06-14 21:18 | 2026-06-14 21:18 | 0s | 0 | `T1592` | 🟢 LOW |

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
| `154.16.146[.]65` | US | OC1-HostForWeb, LLC | **100** ⚠️ | 3 |
| `64.89.160[.]135` | LU | Ghosty Networks LLC | **100** ⚠️ | 50 |
| `134.209.93[.]206` | NL | DigitalOcean, LLC | **100** ⚠️ | 3 |
| `45.79.207[.]110` | US | Linode | **100** ⚠️ | 50 |
| `172.235.41[.]110` | US | Linode | **100** ⚠️ | 12 |
| `137.131.9[.]65` | US | Oracle Corporation | **100** ⚠️ | 4 |
| `113.0.152[.]164` | CN | China Unicom Heilongjiang Province Network | **100** ⚠️ | 26 |
| `111.29.52[.]71` | CN | China Mobile Communications Corporation | **100** ⚠️ | 6 |
| `188.166.223[.]22` | SG | DigitalOcean, LLC | **100** ⚠️ | 3 |
| `45.82.78[.]106` | SG | Detai Prosperous Technologies Limited | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 35 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 14 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 4 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 3 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 2 |

---

## 🔕 False Positive Summary (27 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 20 |
| AbuseIPDB score 5 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 6 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 70 cases |
| Tool 34  | Credential Extractor        | ✅ 17 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 12 fingerprints |
| Tool 36  | Command Clustering          | ✅ 3 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 24 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 27 filtered (38.6%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 19 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 35 files |
| Tool 33  | YARA Classifier             | ✅ 10 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 11 priority case(s) shown individually · 14 recon entry/entries in table (4 group(s) consolidating 22 session(s)).

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
_Report time: 2026-06-14T23:12:22Z_

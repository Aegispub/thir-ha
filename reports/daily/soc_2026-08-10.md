# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-08-10 |
| **Generated At** | 2026-08-10T09:26:24Z |
| **Shift Time** | 09:26 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **123** |
| Confirmed Threats | **100** |
| False Positives Filtered | **23** (18.7%) |
| Unique Attacker IPs | **57** |
| Countries of Origin | **29** |
| High Severity Cases | **22** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **101** |
| Malware Samples Analyzed | **2** HIGH · **24** MED · 20 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **31** |
| Unique Credential Pairs | **14** |
| Unique Usernames | **8** |
| Unique Passwords | **14** |
| Successful Auth Pairs | **26** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 13 |
| `debian` | 4 |
| `support` | 4 |
| `www` | 4 |
| `default` | 2 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `s553355` | 4 |
| `654321` | 4 |
| `www` | 4 |
| `support` | 3 |
| `123@@@` | 2 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `s553355` | 4 |
| `debian` | `654321` | 4 |
| `www` | `www` | 4 |
| `support` | `support` | 3 |
| `root` | `123@@@` | 2 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `s553355` | `10.0.0.73` | 2026-08-10T06:56:46 |
| `root` | `123@@@` | `64.110.90.250` | 2026-08-10T06:59:52 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-08-10T06:59:52 |
| `debian` | `654321` | `10.0.0.73` | 2026-08-10T07:02:37 |
| `root` | `s553355` | `210.0.90.81` | 2026-08-10T07:15:24 |
| `root` | `s553355` | `110.14.192.20` | 2026-08-10T07:15:32 |
| `root` | `s553355` | `218.149.228.149` | 2026-08-10T07:15:42 |
| `debian` | `654321` | `67.85.146.216` | 2026-08-10T07:20:09 |
| `debian` | `654321` | `111.70.32.2` | 2026-08-10T07:20:18 |
| `root` | `11111111` | `10.0.0.73` | 2026-08-10T07:26:15 |
| `root` | `11111111` | `185.81.94.58` | 2026-08-10T07:27:54 |
| `support` | `support` | `176.53.159.196` | 2026-08-10T07:35:30 |
| `support` | `1qaz2wsx` | `122.166.253.226` | 2026-08-10T07:50:11 |
| `support` | `support` | `10.0.0.73` | 2026-08-10T07:59:18 |
| `www` | `www` | `195.222.57.183` | 2026-08-10T08:02:41 |
| `www` | `www` | `92.126.223.175` | 2026-08-10T08:02:47 |
| `root` | `123321` | `10.0.0.73` | 2026-08-10T08:05:40 |
| `root` | `---fuck_you----` | `10.0.0.73` | 2026-08-10T08:09:09 |
| `www` | `www` | `65.20.217.64` | 2026-08-10T08:19:05 |
| `www` | `www` | `45.178.227.0` | 2026-08-10T08:19:13 |
| `admin` | `admin` | `47.253.5.130` | 2026-08-10T08:25:39 |
| `default` | `default11` | `220.80.223.144` | 2026-08-10T08:29:08 |
| `default` | `default11` | `118.122.196.230` | 2026-08-10T08:29:17 |
| `system` | `OkwKcECs8qJP2Z` | `61.12.86.90` | 2026-08-10T08:34:18 |
| `operator` | `uploader` | `122.224.164.194` | 2026-08-10T08:37:07 |
| `operator` | `uploader` | `179.181.133.153` | 2026-08-10T08:37:21 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **123** |
| Sessions with Fingerprint | **6** |
| Unique HASSH Fingerprints | **6** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| OpenSSH | 16 |
| libssh | 6 |
| Paramiko (Python) | 4 |
| Go SSH scanner | 2 |
| PuTTY | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `acaa53e0a7d7...` | Mirai/variant | 16 | 16 |
| `a2de0f306611...` | Mirai/variant | 4 | 1 |
| `5bd26477da54...` | Mirai/variant | 1 | 1 |
| `eff4c24daffc...` | Modern SSH client | 1 | 1 |
| `2aec6b44b06b...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `acaa53e0a7d7...` | OpenSSH | 16 | 16 | Mirai/variant |
| `95420f9d932d...` | libssh | 6 | 2 | — |
| `a2de0f306611...` | Paramiko (Python) | 4 | 1 | Mirai/variant |
| `5bd26477da54...` | PuTTY | 1 | 1 | Mirai/variant |
| `eff4c24daffc...` | Go SSH scanner | 1 | 1 | Modern SSH client |
| `2aec6b44b06b...` | Go SSH scanner | 1 | 1 | Mirai/variant |

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **57** |
| Unique ASNs | **50** |
| High-Risk ASNs | **35** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS14061` | DigitalOcean, LLC | 3 | HIGH |
| `AS4134` | CHINANET BACKBONE | 3 | HIGH |
| `AS7303` | Telecom Argentina S.A. | 2 | HIGH |
| `AS48721` | Flyservers S.A. | 2 | HIGH |
| `AS4766` | Korea Telecom | 2 | HIGH |
| `AS22773` | Cox Communications Inc. | 1 | MEDIUM |
| `AS17421` | Mobile Business Group | 1 | HIGH |
| `AS36903` | Office National des Postes et Telecommunications ONPT (Maroc Telecom) / IAM | 1 | LOW |

---

---

## 🚨 Priority Cases — Immediate Attention (22)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-840ea6cc06c3

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-08-10 06:59 |
| **Last Seen** | 2026-08-10 06:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 06:59:51` | `cowrie.session.connect` |
| `2026-08-10 06:59:51` | `cowrie.client.version` |
| `2026-08-10 06:59:51` | `cowrie.client.kex` |
| `2026-08-10 06:59:52` | `cowrie.login.success` |
| `2026-08-10 06:59:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0b3bcbf9febe

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-08-10 06:59 |
| **Last Seen** | 2026-08-10 06:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 06:59:51` | `cowrie.session.connect` |
| `2026-08-10 06:59:51` | `cowrie.client.version` |
| `2026-08-10 06:59:51` | `cowrie.client.kex` |
| `2026-08-10 06:59:52` | `cowrie.login.success` |
| `2026-08-10 06:59:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c9f8be7d7063

| Field | Detail |
|---|---|
| **Source IP** | `210.0.90[.]81` |
| **First Seen** | 2026-08-10 07:15 |
| **Last Seen** | 2026-08-10 07:15 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 07:15:20` | `cowrie.session.connect` |
| `2026-08-10 07:15:21` | `cowrie.client.version` |
| `2026-08-10 07:15:21` | `cowrie.client.kex` |
| `2026-08-10 07:15:24` | `cowrie.login.success` |
| `2026-08-10 07:15:25` | `cowrie.direct-tcpip.request` |
| `2026-08-10 07:15:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `210.0.90[.]81` to AbuseIPDB if not already reported
- [ ] Block `210.0.90[.]81` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e89a021a8adb

| Field | Detail |
|---|---|
| **Source IP** | `110.14.192[.]20` |
| **First Seen** | 2026-08-10 07:15 |
| **Last Seen** | 2026-08-10 07:15 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 07:15:29` | `cowrie.session.connect` |
| `2026-08-10 07:15:30` | `cowrie.client.version` |
| `2026-08-10 07:15:30` | `cowrie.client.kex` |
| `2026-08-10 07:15:32` | `cowrie.login.success` |
| `2026-08-10 07:15:33` | `cowrie.direct-tcpip.request` |
| `2026-08-10 07:15:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `110.14.192[.]20` to AbuseIPDB if not already reported
- [ ] Block `110.14.192[.]20` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4d958b5dbea1

| Field | Detail |
|---|---|
| **Source IP** | `218.149.228[.]149` |
| **First Seen** | 2026-08-10 07:15 |
| **Last Seen** | 2026-08-10 07:15 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 07:15:39` | `cowrie.session.connect` |
| `2026-08-10 07:15:40` | `cowrie.client.version` |
| `2026-08-10 07:15:40` | `cowrie.client.kex` |
| `2026-08-10 07:15:42` | `cowrie.login.success` |
| `2026-08-10 07:15:42` | `cowrie.direct-tcpip.request` |
| `2026-08-10 07:15:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.149.228[.]149` to AbuseIPDB if not already reported
- [ ] Block `218.149.228[.]149` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ee5d617aa55a

| Field | Detail |
|---|---|
| **Source IP** | `67.85.146[.]216` |
| **First Seen** | 2026-08-10 07:20 |
| **Last Seen** | 2026-08-10 07:20 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 07:20:08` | `cowrie.session.connect` |
| `2026-08-10 07:20:08` | `cowrie.client.version` |
| `2026-08-10 07:20:08` | `cowrie.client.kex` |
| `2026-08-10 07:20:09` | `cowrie.login.success` |
| `2026-08-10 07:20:09` | `cowrie.direct-tcpip.request` |
| `2026-08-10 07:20:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `67.85.146[.]216` to AbuseIPDB if not already reported
- [ ] Block `67.85.146[.]216` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-68f082616fe0

| Field | Detail |
|---|---|
| **Source IP** | `111.70.32[.]2` |
| **First Seen** | 2026-08-10 07:20 |
| **Last Seen** | 2026-08-10 07:20 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 07:20:15` | `cowrie.session.connect` |
| `2026-08-10 07:20:16` | `cowrie.client.version` |
| `2026-08-10 07:20:16` | `cowrie.client.kex` |
| `2026-08-10 07:20:18` | `cowrie.login.success` |
| `2026-08-10 07:20:18` | `cowrie.direct-tcpip.request` |
| `2026-08-10 07:20:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.70.32[.]2` to AbuseIPDB if not already reported
- [ ] Block `111.70.32[.]2` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f06a841b32d4

| Field | Detail |
|---|---|
| **Source IP** | `185.81.94[.]58` |
| **First Seen** | 2026-08-10 07:27 |
| **Last Seen** | 2026-08-10 07:27 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 07:27:52` | `cowrie.session.connect` |
| `2026-08-10 07:27:53` | `cowrie.client.version` |
| `2026-08-10 07:27:53` | `cowrie.client.kex` |
| `2026-08-10 07:27:54` | `cowrie.login.success` |
| `2026-08-10 07:27:54` | `cowrie.direct-tcpip.request` |
| `2026-08-10 07:27:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.81.94[.]58` to AbuseIPDB if not already reported
- [ ] Block `185.81.94[.]58` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5fdd1cbf5846

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-10 07:35 |
| **Last Seen** | 2026-08-10 07:35 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 07:35:30` | `cowrie.session.connect` |
| `2026-08-10 07:35:30` | `cowrie.client.version` |
| `2026-08-10 07:35:30` | `cowrie.client.kex` |
| `2026-08-10 07:35:30` | `cowrie.login.success` |
| `2026-08-10 07:35:30` | `cowrie.direct-tcpip.request` |
| `2026-08-10 07:35:30` | `cowrie.direct-tcpip.data` |
| `2026-08-10 07:35:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1ccd23f64603

| Field | Detail |
|---|---|
| **Source IP** | `122.166.253[.]226` |
| **First Seen** | 2026-08-10 07:50 |
| **Last Seen** | 2026-08-10 07:50 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 07:50:08` | `cowrie.session.connect` |
| `2026-08-10 07:50:09` | `cowrie.client.version` |
| `2026-08-10 07:50:09` | `cowrie.client.kex` |
| `2026-08-10 07:50:11` | `cowrie.login.success` |
| `2026-08-10 07:50:12` | `cowrie.direct-tcpip.request` |
| `2026-08-10 07:50:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.166.253[.]226` to AbuseIPDB if not already reported
- [ ] Block `122.166.253[.]226` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6bf7de2faf5b

| Field | Detail |
|---|---|
| **Source IP** | `195.222.57[.]183` |
| **First Seen** | 2026-08-10 08:02 |
| **Last Seen** | 2026-08-10 08:02 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 08:02:39` | `cowrie.session.connect` |
| `2026-08-10 08:02:40` | `cowrie.client.version` |
| `2026-08-10 08:02:40` | `cowrie.client.kex` |
| `2026-08-10 08:02:41` | `cowrie.login.success` |
| `2026-08-10 08:02:41` | `cowrie.direct-tcpip.request` |
| `2026-08-10 08:02:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.222.57[.]183` to AbuseIPDB if not already reported
- [ ] Block `195.222.57[.]183` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-10d70b491bef

| Field | Detail |
|---|---|
| **Source IP** | `92.126.223[.]175` |
| **First Seen** | 2026-08-10 08:02 |
| **Last Seen** | 2026-08-10 08:02 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 08:02:46` | `cowrie.session.connect` |
| `2026-08-10 08:02:46` | `cowrie.client.version` |
| `2026-08-10 08:02:46` | `cowrie.client.kex` |
| `2026-08-10 08:02:47` | `cowrie.login.success` |
| `2026-08-10 08:02:48` | `cowrie.direct-tcpip.request` |
| `2026-08-10 08:02:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.126.223[.]175` to AbuseIPDB if not already reported
- [ ] Block `92.126.223[.]175` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b68c5a7ff138

| Field | Detail |
|---|---|
| **Source IP** | `65.20.217[.]64` |
| **First Seen** | 2026-08-10 08:19 |
| **Last Seen** | 2026-08-10 08:19 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 08:19:03` | `cowrie.session.connect` |
| `2026-08-10 08:19:04` | `cowrie.client.version` |
| `2026-08-10 08:19:04` | `cowrie.client.kex` |
| `2026-08-10 08:19:05` | `cowrie.login.success` |
| `2026-08-10 08:19:06` | `cowrie.direct-tcpip.request` |
| `2026-08-10 08:19:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.217[.]64` to AbuseIPDB if not already reported
- [ ] Block `65.20.217[.]64` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6e2208c9a352

| Field | Detail |
|---|---|
| **Source IP** | `45.178.227[.]0` |
| **First Seen** | 2026-08-10 08:19 |
| **Last Seen** | 2026-08-10 08:19 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 08:19:11` | `cowrie.session.connect` |
| `2026-08-10 08:19:11` | `cowrie.client.version` |
| `2026-08-10 08:19:11` | `cowrie.client.kex` |
| `2026-08-10 08:19:13` | `cowrie.login.success` |
| `2026-08-10 08:19:13` | `cowrie.direct-tcpip.request` |
| `2026-08-10 08:19:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.178.227[.]0` to AbuseIPDB if not already reported
- [ ] Block `45.178.227[.]0` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6ca2e7fda867

| Field | Detail |
|---|---|
| **Source IP** | `47.253.5[.]130` |
| **First Seen** | 2026-08-10 08:24 |
| **Last Seen** | 2026-08-10 08:25 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 08:24:39` | `cowrie.session.connect` |
| `2026-08-10 08:24:39` | `cowrie.telnet.option` |
| `2026-08-10 08:24:39` | `cowrie.telnet.option` |
| `2026-08-10 08:25:39` | `cowrie.login.success` |
| `2026-08-10 08:25:40` | `cowrie.session.params` |

**Recommended Actions:**
- [ ] Submit `47.253.5[.]130` to AbuseIPDB if not already reported
- [ ] Block `47.253.5[.]130` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ffcd08cec774

| Field | Detail |
|---|---|
| **Source IP** | `220.80.223[.]144` |
| **First Seen** | 2026-08-10 08:29 |
| **Last Seen** | 2026-08-10 08:29 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 08:29:05` | `cowrie.session.connect` |
| `2026-08-10 08:29:06` | `cowrie.client.version` |
| `2026-08-10 08:29:06` | `cowrie.client.kex` |
| `2026-08-10 08:29:08` | `cowrie.login.success` |
| `2026-08-10 08:29:08` | `cowrie.direct-tcpip.request` |
| `2026-08-10 08:29:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.80.223[.]144` to AbuseIPDB if not already reported
- [ ] Block `220.80.223[.]144` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-72e17088206a

| Field | Detail |
|---|---|
| **Source IP** | `118.122.196[.]230` |
| **First Seen** | 2026-08-10 08:29 |
| **Last Seen** | 2026-08-10 08:29 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 08:29:14` | `cowrie.session.connect` |
| `2026-08-10 08:29:14` | `cowrie.client.version` |
| `2026-08-10 08:29:14` | `cowrie.client.kex` |
| `2026-08-10 08:29:17` | `cowrie.login.success` |
| `2026-08-10 08:29:18` | `cowrie.direct-tcpip.request` |
| `2026-08-10 08:29:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.122.196[.]230` to AbuseIPDB if not already reported
- [ ] Block `118.122.196[.]230` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9d563dc540ea

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-08-10 08:29 |
| **Last Seen** | 2026-08-10 08:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 08:29:23` | `cowrie.session.connect` |
| `2026-08-10 08:29:23` | `cowrie.client.version` |
| `2026-08-10 08:29:23` | `cowrie.client.kex` |
| `2026-08-10 08:29:24` | `cowrie.login.success` |
| `2026-08-10 08:29:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0099894c6a2a

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-08-10 08:29 |
| **Last Seen** | 2026-08-10 08:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 08:29:23` | `cowrie.session.connect` |
| `2026-08-10 08:29:23` | `cowrie.client.version` |
| `2026-08-10 08:29:23` | `cowrie.client.kex` |
| `2026-08-10 08:29:24` | `cowrie.login.success` |
| `2026-08-10 08:29:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8b898bcc81e3

| Field | Detail |
|---|---|
| **Source IP** | `61.12.86[.]90` |
| **First Seen** | 2026-08-10 08:34 |
| **Last Seen** | 2026-08-10 08:34 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 08:34:15` | `cowrie.session.connect` |
| `2026-08-10 08:34:16` | `cowrie.client.version` |
| `2026-08-10 08:34:16` | `cowrie.client.kex` |
| `2026-08-10 08:34:18` | `cowrie.login.success` |
| `2026-08-10 08:34:19` | `cowrie.direct-tcpip.request` |
| `2026-08-10 08:34:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.12.86[.]90` to AbuseIPDB if not already reported
- [ ] Block `61.12.86[.]90` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4c0905dfdb19

| Field | Detail |
|---|---|
| **Source IP** | `122.224.164[.]194` |
| **First Seen** | 2026-08-10 08:37 |
| **Last Seen** | 2026-08-10 08:37 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 08:37:03` | `cowrie.session.connect` |
| `2026-08-10 08:37:04` | `cowrie.client.version` |
| `2026-08-10 08:37:04` | `cowrie.client.kex` |
| `2026-08-10 08:37:07` | `cowrie.login.success` |
| `2026-08-10 08:37:09` | `cowrie.direct-tcpip.request` |
| `2026-08-10 08:37:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.224.164[.]194` to AbuseIPDB if not already reported
- [ ] Block `122.224.164[.]194` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4f8a6d6fcea1

| Field | Detail |
|---|---|
| **Source IP** | `179.181.133[.]153` |
| **First Seen** | 2026-08-10 08:37 |
| **Last Seen** | 2026-08-10 08:37 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 08:37:19` | `cowrie.session.connect` |
| `2026-08-10 08:37:19` | `cowrie.client.version` |
| `2026-08-10 08:37:19` | `cowrie.client.kex` |
| `2026-08-10 08:37:21` | `cowrie.login.success` |
| `2026-08-10 08:37:21` | `cowrie.direct-tcpip.request` |
| `2026-08-10 08:37:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.181.133[.]153` to AbuseIPDB if not already reported
- [ ] Block `179.181.133[.]153` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `92.204.138[.]142` | **36** | 2026-08-10 07:06 | 2026-08-10 08:54 | 17m | 0 | `T1592` | 🟠 MEDIUM |
| `164.92.115[.]22` | **8** | 2026-08-10 07:01 | 2026-08-10 08:32 | 4m | 0 | `T1592` | 🟢 LOW |
| `139.199.80[.]137` | **5** | 2026-08-10 06:58 | 2026-08-10 08:47 | 0m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]122` | **3** | 2026-08-10 08:36 | 2026-08-10 08:36 | 0m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]161` | **3** | 2026-08-10 07:15 | 2026-08-10 07:15 | 0m | 0 | `T1592` | 🟢 LOW |
| `195.214.222[.]59` | **3** | 2026-08-10 07:28 | 2026-08-10 07:32 | 0m | 0 | `T1592` | 🟢 LOW |
| `91.238.181[.]92` | **3** | 2026-08-10 07:46 | 2026-08-10 07:46 | 0m | 0 | `T1592` | 🟢 LOW |
| `218.4.214[.]115` | **2** | 2026-08-10 07:34 | 2026-08-10 07:36 | 2m | 0 | `T1592` | 🟢 LOW |
| `77.90.185[.]16` | **2** | 2026-08-10 07:25 | 2026-08-10 08:02 | 0m | 0 | `T1592` | 🟢 LOW |
| `142.93.218[.]50` | 1 | 2026-08-10 07:47 | 2026-08-10 07:47 | 30s | 0 | `T1592` | 🟢 LOW |
| `185.247.137[.]195` | 1 | 2026-08-10 08:45 | 2026-08-10 08:45 | 2s | 0 | `T1592` | 🟢 LOW |
| `197.156.97[.]198` | 1 | 2026-08-10 08:34 | 2026-08-10 08:36 | 120s | 0 | `T1592` | 🟢 LOW |
| `201.231.74[.]248` | 1 | 2026-08-10 07:31 | 2026-08-10 07:31 | 11s | 0 | `T1592` | 🟢 LOW |
| `213.5.192[.]65` | 1 | 2026-08-10 06:56 | 2026-08-10 06:56 | 15s | 0 | `T1592` | 🟢 LOW |
| `213.65.190[.]48` | 1 | 2026-08-10 07:54 | 2026-08-10 07:56 | 120s | 0 | `T1592` | 🟢 LOW |
| `218.202.91[.]147` | 1 | 2026-08-10 08:36 | 2026-08-10 08:36 | 19s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]141` | 1 | 2026-08-10 07:10 | 2026-08-10 07:10 | 0s | 0 | `T1592` | 🟢 LOW |
| `46.101.240[.]96` | 1 | 2026-08-10 07:59 | 2026-08-10 07:59 | 20s | 0 | `T1592` | 🟢 LOW |
| `5.59.107[.]206` | 1 | 2026-08-10 08:23 | 2026-08-10 08:24 | 13s | 0 | `T1592` | 🟢 LOW |
| `73.16.88[.]172` | 1 | 2026-08-10 07:37 | 2026-08-10 07:37 | 13s | 0 | `T1592` | 🟢 LOW |
| `80.66.83[.]43` | 1 | 2026-08-10 07:30 | 2026-08-10 07:30 | 0s | 0 | `T1592` | 🟢 LOW |
| `91.233.83[.]203` | 1 | 2026-08-10 07:42 | 2026-08-10 07:44 | 62s | 0 | `T1592` | 🟢 LOW |

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
| `195.214.222[.]59` | UA | LLC Global-City-Net | **100** ⚠️ | 2 |
| `5.59.107[.]206` | UA | FLYCOM-NETWORK | **100** ⚠️ | 3 |
| `194.165.16[.]122` | LT | Flyservers S.A. | **100** ⚠️ | 13 |
| `67.85.146[.]216` | US | Optimum Online (Cablevision Systems) | **100** ⚠️ | 50 |
| `92.126.223[.]175` | RU | OJSC Sibirtelecom | **100** ⚠️ | 50 |
| `47.253.5[.]130` | US | Alibaba Cloud - US | **100** ⚠️ | 50 |
| `218.202.91[.]147` | CN | China Mobile Communications Corporation - neimeng | **100** ⚠️ | 50 |
| `142.93.218[.]50` | IN | DigitalOcean, LLC | **100** ⚠️ | 36 |
| `61.12.86[.]90` | IN | TTSL-ISP DIVISION | **100** ⚠️ | 50 |
| `77.90.185[.]16` | LT | Limited Network LTD | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 29 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 22 |

---

## 🔕 False Positive Summary (23 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 1 |
| AbuseIPDB score 1 below threshold 25 | 1 |
| AbuseIPDB score 15 below threshold 25 | 2 |
| AbuseIPDB score 21 below threshold 25 | 1 |
| AbuseIPDB score 22 below threshold 25 | 1 |
| AbuseIPDB score 24 below threshold 25 | 5 |
| AbuseIPDB score 4 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 11 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 123 cases |
| Tool 34  | Credential Extractor        | ✅ 31 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 6 fingerprints |
| Tool 36  | Command Clustering          | ✅ 0 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 57 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 23 filtered (18.7%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 50 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 22 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 22 priority case(s) shown individually · 22 recon entry/entries in table (9 group(s) consolidating 65 session(s)).

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
_Report time: 2026-08-10T09:26:24Z_
